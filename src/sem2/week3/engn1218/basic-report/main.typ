
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
R_2 and R_3 are in parallel. so they can be combined to a R_23

#let R_1 = 1.5e3
#let R_2 = 3.3e3
#let R_3 = 5.6e3
$R_23 = (R_2*R_3)/(R_2 + R_3)$

$R_23 = (#R_2*#R_3)/(#R_2 + #R_3)$

#let R_23 = (R_2 * R_3) / (R_2 + R_3)

$R_23 = #R_23$

R_1 and R_23 are in series so

$R_23 + R_1 = R_"total"$

#let R_total = R_23 + R_1

$R_23 + R_1 = R_"total"$

$#R_23 + #R_1 = R_"total"$

$R_"total" = #R_total$


$V_"total" = V_1$

#let V_total = 5

$V_"total" = #V_total$

$I_"total" = V_"total"/R_"total"$

$I_"total" = #V_total/#R_total$

#let I_total = V_total / R_total

$I_"total" = #I_total$

The I through R_1 is V_total

$I_"R1" = I_"total"$

$I_"R1" = #I_total$

$V_"R1" = I_"R1" times R_1$

$V_"R1" = #I_total times #R_1$

#let V_R1 = I_total * R_1

$V_"R1" = #V_R1$

$V_"R1" + V_"R23" = V_"Total"$

$V_"R23" = V_"Total" - V_"R1"$

$V_"R23" = #V_total - #V_R1$

#let V_R23 = V_total - V_R1

$V_"R23" = #V_R23$

Because R_23 and R_3 and R_3 are in series;

$V_"R23" = V_"R3" = V_"R2" = #V_R23$

$I_"R3" = V_"R3"/R_3$

$I_"R3" = #V_R23/#R_3$

#let I_R3 = V_R23/R_3

$I_"R3" = #I_R3$

And similarly for R2

$I_"R2" = V_"R2"/R_2$

$I_"R2" = #V_R23/#R_2$

#let I_R2 = V_R23/R_2

$I_"R2" = #I_R2$

To summise. 

$I_"R1" = #I_total$

$I_"R2" = #I_R2$

$I_"R3" = #I_R3$

$V_"R1" = #V_R1$

$V_"R2" = #V_R23$

$V_"R3" = #V_R23$

