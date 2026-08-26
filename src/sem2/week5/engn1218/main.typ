
#import "@preview/basic-report:0.5.0": *

#show: it => basic-report(
  doc-category: "Week 3 Lab ENGN1218",
  doc-title: "Week 3 Lab ENGN1218",
  author: "Bryce Tabangcura",
  affiliation: "ANU",
  // logo: image("assets/aerospace-engineering.png", width: 2cm),
  // <a href="https://www.flaticon.com/free-icons/aerospace" title="aerospace icons">Aerospace icons created by gravisio - Flaticon</a>
  language: "en",
  compact-mode: true,
  it,
)

#text(size: 13pt)[
  PRELAB QUESTIONS
]
$
                                    15 - V_x & = (5"k" Omega)I_1 \
                     (15 - V_x)/(5"k" Omega) & = I_1 \
                                         V_x & = (10"k" Omega)I_2 \
                           V_x/(10"k" Omega) & = I_2 \
                                         V_x & = (4"k" Omega)I_3 \
                            V_x/(4"k" Omega) & = 4I_3 \
                                   I_1 - I_2 & = I_3 - 2 "mA" \
                                   I_1 - I_2 & = I_3 - 2 times 10^-3 \
  (15 - V_x)/(5"k" Omega)- V_x/(10"k" Omega) & = V_x/(4"k" Omega) - 2 times 10^-3 \
                                         V_x & approx 9.09 \
$

#let vab = $V_"ab"$
$
           V_y & = #vab \
       V = I R \
      V_x - 10 & = I_1 times 1 \
      V_x - 10 & = I_1 \
     V_x - V_y & = I_2 times 1 \
    V_x - #vab & = I_2 \
           V_y & = I_3 times 1 \
          #vab & = I_3 \
  K #vab - I_1 & = I_2 \
           I_2 & = I_3 - 2"A" \
$
These are all our equations from V = IR, now to simultaneously solve

$
               V_x - #vab & = #vab - 2 \
                      V_x & = 2#vab - 2 \
  K #vab - 2#vab - 2 + 10 & = 2#vab - 2 - #vab \
                     #vab & = 14 \
                     #vab & = V_y = V_z = 14 \
                      V_x & = 2#vab - 2 \
                      V_x & = 2 times 14 - 2 \
                      V_x & = 26 \
$
Now for current through resistors
$
            V/R & = I \
   (V_x-10)/R_1 & = I_1 \
      (26-10)/1 & = I_1 \
            I_1 & = 14 \
  (V_x-V_y)/R_2 & = I_2 \
      (26-14)/1 & = I_2 \
            I_2 & = 12 \
      (V_y)/R_3 & = I_3 \
         (14)/1 & = I_3 \
            I_3 & = 14 \
$
find thevenins resistance
If you draw the circuit, it ends up being two 1 ohm resisters in series, so
$
  1 + 1 = R\
  R = 2\
  V/R = I\
  14/2 = I\
  I = 7
$

