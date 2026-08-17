use std::env;
use std::process;

const DIGITS: &[(&str, i32)] = &[
    ("black", 0), ("brown", 1), ("red", 2), ("orange", 3), ("yellow", 4),
    ("green", 5), ("blue", 6), ("violet", 7), ("gray", 8), ("grey", 8), ("white", 9),
];

const MULTIPLIERS: &[(&str, f64)] = &[
    ("silver", 0.01), ("gold", 0.1), ("black", 1.0), ("brown", 10.0),
    ("red", 100.0), ("orange", 1_000.0), ("yellow", 10_000.0), ("green", 100_000.0),
    ("blue", 1_000_000.0), ("violet", 10_000_000.0), ("gray", 100_000_000.0),
    ("grey", 100_000_000.0),
];

const TOLERANCES: &[(&str, &str)] = &[
    ("brown", "±1%"), ("red", "±2%"), ("green", "±0.5%"), ("blue", "±0.25%"),
    ("violet", "±0.1%"), ("gray", "±0.05%"), ("grey", "±0.05%"),
    ("gold", "±5%"), ("silver", "±10%"),
];

fn lookup_val<T: Copy>(table: &[(&str, T)], colour: &str) -> Option<T> {
    table.iter().find(|(c, _)| *c == colour).map(|(_, v)| *v)
}

fn lookup_color_by_digit(digit: i32) -> &'static str {
    DIGITS.iter().find(|(_, v)| *v == digit).map(|(c, _)| *c).unwrap_or("black")
}

fn lookup_multiplier_color(mult: f64) -> Option<&'static str> {
    MULTIPLIERS
        .iter()
        .find(|(_, v)| (*v - mult).abs() / mult < 1e-4)
        .map(|(c, _)| *c)
}

fn parse_resistance(val_str: &str) -> Option<f64> {
    let s = val_str.trim();
    if s.is_empty() { return None; }

    let (num_part, mult) = if s.ends_with('k') || s.ends_with('K') {
        (&s[..s.len() - 1], 1_000.0)
    } else if s.ends_with('m') || s.ends_with('M') {
        (&s[..s.len() - 1], 1_000_000.0)
    } else {
        (s, 1.0)
    };

    num_part.parse::<f64>().ok().map(|n| n * mult)
}

fn format_ohms(value: f64) -> String {
    if value >= 1_000_000.0 {
        format!("{:.2} MΩ", value / 1_000_000.0)
    } else if value >= 1_000.0 {
        format!("{:.2} kΩ", value / 1_000.0)
    } else {
        format!("{:.2} Ω", value)
    }
}

fn decode_colors(args: &[String]) {
    let (digit_bands, mult_band, tol_band): (&[String], &str, Option<&str>) = match args.len() {
        3 => (&args[0..2], &args[2], None),
        4 => (&args[0..2], &args[2], Some(&args[3])),
        5 => (&args[0..3], &args[3], Some(&args[4])),
        _ => print_usage_and_exit(),
    };

    let mut value: i64 = 0;
    for c in digit_bands {
        match lookup_val(DIGITS, c) {
            Some(d) => value = value * 10 + d as i64,
            None => {
                eprintln!("unknown digit colour: {c}");
                process::exit(1);
            }
        }
    }

    let mult = match lookup_val(MULTIPLIERS, mult_band) {
        Some(m) => m,
        None => {
            eprintln!("unknown multiplier colour: {mult_band}");
            process::exit(1);
        }
    };

    let tol = match tol_band {
        Some(c) => match lookup_val(TOLERANCES, c) {
            Some(t) => t,
            None => {
                eprintln!("unknown tolerance colour: {c}");
                process::exit(1);
            }
        },
        None => "±20%",
    };

    let ohms = value as f64 * mult;
    println!("{} {}", format_ohms(ohms), tol);
}

fn encode_number(val_str: &str, num_digit_bands: usize) {
    let ohms = match parse_resistance(val_str) {
        Some(v) if v > 0.0 => v,
        _ => {
            eprintln!("invalid positive resistance value: {val_str}");
            process::exit(1);
        }
    };

    // Determine scale for requested number of digit bands (2 for 4-band, 3 for 5-band)
    let min_sig = 10.0_f64.powi((num_digit_bands - 1) as i32);
    let max_sig = min_sig * 10.0;

    let mut temp = ohms;
    let mut exponent: i32 = 0;

    while temp >= max_sig {
        temp /= 10.0;
        exponent += 1;
    }
    while temp < min_sig {
        temp *= 10.0;
        exponent -= 1;
    }

    let sig_digits = temp.round() as i32;
    let mult_val = 10.0_f64.powi(exponent);

    let mult_color = match lookup_multiplier_color(mult_val) {
        Some(c) => c,
        None => {
            eprintln!("value {val_str} requires out-of-range multiplier ({mult_val})");
            process::exit(1);
        }
    };

    let colors: Vec<&str> = if num_digit_bands == 2 {
        let d1 = sig_digits / 10;
        let d2 = sig_digits % 10;
        vec![lookup_color_by_digit(d1), lookup_color_by_digit(d2), mult_color]
    } else {
        let d1 = sig_digits / 100;
        let d2 = (sig_digits / 10) % 10;
        let d3 = sig_digits % 10;
        vec![
            lookup_color_by_digit(d1),
            lookup_color_by_digit(d2),
            lookup_color_by_digit(d3),
            mult_color,
        ]
    };

    println!("{}-band colors: {}", num_digit_bands + 2, colors.join(" "));
}

fn print_usage_and_exit() -> ! {
    eprintln!("usage:");
    eprintln!("  Decode colors:  resistor-colours <digit> <digit> [<digit>] <multiplier> [<tolerance>]");
    eprintln!("  Encode value:   resistor-colours <ohms|1k|4.7k|2.2M> [5]");
    eprintln!("\nexamples:");
    eprintln!("  resistor-colours brown black red gold");
    eprintln!("  resistor-colours 1000       (outputs 4-band: brown black red)");
    eprintln!("  resistor-colours 4.7k 5     (outputs 5-band: yellow violet black brown)");
    process::exit(1);
}

fn main() {
    let args: Vec<String> = env::args().skip(1).map(|a| a.to_lowercase()).collect();

    if args.is_empty() {
        print_usage_and_exit();
    }

    // Check if encoding numeric input
    if parse_resistance(&args[0]).is_some() {
        let band_count = if args.len() > 1 && args[1] == "5" { 3 } else { 2 };
        encode_number(&args[0], band_count);
    } else {
        decode_colors(&args);
    }
}
