
#import "@preview/basic-report:0.5.0": *

#show: it => basic-report(
  doc-category: "Betriebsanleitung",
  doc-title: "Raketenstart für Dummies",
  author: "Daniel Düsentrieb",
  affiliation: "MouseTec, Entenhausen",
  logo: image("assets/aerospace-engineering.png", width: 2cm),
  // <a href="https://www.flaticon.com/free-icons/aerospace" title="aerospace icons">Aerospace icons created by gravisio - Flaticon</a>
  language: "de",
  compact-mode: true,
  it,
)

#text(size: 13pt)[
  PRELAB QUESTIONS
]
== Theoretical Calculation
#table(
  columns: (1fr, 1fr),
  "Bands 1", "brown",
  "Bands 2", "green",
  "Bands 3", "black",
  "Bands 4", "brown",
  "Bands 5", "brown",
  "R (ohms)", $1.5 k Omega plus.minus 1%$,
)

#table(
  columns: (1fr, 1fr),
  "Bands 1", "orange",
  "Bands 2", "orange",
  "Bands 3", "black",
  "Bands 4", "brown",
  "Bands 5", "brown",
  "R (ohms)", $3.3 k Omega plus.minus 1%$,
)

#table(
  columns: (1fr, 1fr),
  "Bands 1", "green",
  "Bands 2", "blue",
  "Bands 3", "black",
  "Bands 4", "brown",
  "Bands 5", "brown",
  "R (ohms)", $5.6 k Omega plus.minus 1%$,
)
#table(
  columns: (1fr, 1fr),
  "Bands 1", "grey",
  "Bands 2", "red",
  "Bands 3", "black",
  "Bands 4", "brown",
  "Bands 5", "brown",
  "R (ohms)", $8.2 k Omega plus.minus 1%$,
)
#table(
  columns: (1fr, 1fr),
  "Bands 1", "brown",
  "Bands 2", "black",
  "Bands 3", "black",
  "Bands 4", "orange",
  "Bands 5", "brown",
  "R (ohms)", $100 k Omega plus.minus 1%$,
)
= Simple Resistive Circuit
== Theoretical Calculation
$
          V & = I R \
          I & = V/R \
  "Given" R & = R_1 = 8.2 k \
          V & = V_1 = 8.2 k \
          I & = 10/(8.2*10^3) \
            & = 1.2*10^-3 Omega
$
= Simple Resistive Circuit
== Theoretical Calculation
$
          V & = I R \
  I_"total" & = V_"total"/R_"total" \
  "Given" R & = R_1 = 100 k \
          V & = V_1 + V_2 = 10 + 5 V = 15 V \
          I & = 15/(100*10^3) \
            & = 150 mu Omega \
        V_x & = V_"total" = 15 V \
$
#table(
  columns: (1fr,) * 4,
  "", [Voltage $V_x (V)$], [Resistance R_1 (k$Omega$)], [Current I(mA)],
  "Theoretical", "15", "100", "0.15",
  "Simulated", "15", "100", "0.15",
  "Measured", "", "", "",
)
= DC Voltage Sources with Opposite Polarities
== Theoretical Calculation
Using KVL. lets go clockwise around the center.
$
  V_2 - V_1 - I R_1 & = 0 \
                  I & = (V_2 - V_1)/R_1 \
                  I & = (10 - 5)/(100*10^-3) \
                  I & = (10 - 5)/(100*10^-3) \
                  I & = 50 mu A \
                V_x & = I * R_1 \
                V_x & = 50 times 10^-6 * 100*10^3 \
                V_x & = 5 \
$

#table(
  columns: (1fr,) * 4,
  "", [Voltage $V_x (V)$], [Resistance R_1 (k$Omega$)], [Current I(mA)],
  "Theoretical", "5", "100", $0.05$,
  "Simulated", "5", "100", $0.05$,
  "Measured", "", "", "",
)
= Simple Resistive Circuit
== Theoretical Calculation

#let r(x) = calc.round(x, digits: 4)
#table(
  columns: (1.5fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
  "Bands 1",
  table.cell(colspan: 3)[Voltage drop across resistor (V)],
  table.cell(colspan: 3)[Current through resistor (mA)],
  "grey", "R_1", "R_2", "R_3", "R_1", "R_2", "R_3",
  "Theoretical",
  str(r(0.001398052152057807)),
  str(r(0.0008796732642161483)),
  str(r(0.0005183788878416588)),
  str(r(2.0970782280867106)),
  str(r(2.9029217719132894)),
  str(r(2.9029217719132894)),
  "Simulated", "0.0014", "0.00088", "0.00052", "2.1", "2.9", "2.9",
  "Measured", "", "", "", "", "", "",
)

= Resistor Ladder Circuit
== Theoretical Calculation
