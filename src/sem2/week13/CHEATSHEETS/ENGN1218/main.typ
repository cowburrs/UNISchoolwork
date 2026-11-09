#import "@preview/boxed-sheet:0.1.2": *
//#import "../src/lib.typ": *

#set text(font: (
  "JetBrainsMono NF",
  // "Public Sans",
))

#let homepage = link("https://cowburrs.github.io/portfolio/")[https://cowburrs.github.io/portfolio/]
#let author = "Bryce"
#let title = "ENGN1218 Cheat Sheet"

#let my-colors = (
  rgb(183, 189, 248), // Lavender
  rgb(138, 173, 244), // Blue
  rgb(125, 196, 228), // Sapphire
  rgb(145, 215, 227), // Sky
  rgb(139, 213, 202), // Teal
  rgb(166, 218, 149), // Green
  rgb(238, 212, 159), // Yellow
  rgb(245, 169, 127), // Peach
  rgb(238, 153, 160), // Maroon
  rgb(237, 135, 150), // Red
  rgb(198, 160, 246), // Mauve
  rgb(245, 189, 230), // Pink
  rgb(240, 198, 198), // Flamingo
  rgb(244, 219, 214), // Rosewater
)

#show: boxedsheet.with(
  title: title, // Title of document
  homepage: homepage, // Homepage of author
  authors: author, // Author Name
  write-title: true, // Writes Title on the first page
  title-align: left, // Position of titles in concept box
  title-number: true, // Whether to numbered the title (Default = true)
  title-delta: 2pt, // Fonts delta for title scaling (Default = 1pt)
  scaling-size: false, // Whether to scale the titles (Default = false)
  // font-size: 5.5pt, // Size of font (Default = 5.5pt)
  font-size: 7pt, // Size of font (Default = 5.5pt)
  line-skip: 5.5pt, // Size of line-skip (Default = 5.5pt)
  x-margin: 10pt, // Margin on x-axis (Default = 30pt)
  y-margin: 30pt, // Margin on y-axis (Default = 0pt)
  num-columns: 3, // Number of columns (Default = 5)
  column-gutter: 4pt, // Space between columns (Default = 4pt)
  numbered-units: false, // Numbering of units (Default = false)
  color-box: my-colors, // Color scheme of boxes
)

= Thevenin
#concept-block[
  #inline("Dependent sources only")
  - Plug in a VS/CS and find resistance.
  #inline("Dependent and Independent Sources")
  - Open Circuit the Connections
  - Deactivate Sources.
  - Plug in a VS/CS and find resistance.
]
= Conversion tricks
#concept-block[
  #columns(2)[
    #inline("Y to Gamma")
    #text(size: 8pt)[
      $ R_"BC" = (R_A R_B + R_B R_C + R_C R_A) / R_C $
    ]
    #colbreak()
    #inline("Gamma to Y")
    #text(size: 8pt)[
      $ R_A = (R_"AB" R_"AC") / (R_"AB" + R_"AC" + R_"BC") $
    ]
  ]
  // #inline("Voltage and Resistor/Current and Resistor")
  // IDK if i keep this here its pretty shit
]
= Capacitor/Inductors Equations
#concept-block[
  #inline("Natural Response/Step Response")
  The general form of all equations are
  #text(size: 10pt)[
    $ x(infinity) + (x(0^+) - x(infinity))e^(-t/tau) $
  ]
  where $x$ can be substituted with Voltage/Current.
  $Tau = R times C$ or $Tau = L/R$
  #columns(2)[
    #inline("Capacitor Equations")
    $ v(t) = 1/C integral_(t_0)^t i(tau)d tau + v(t_0) $
    $ I = C (d V)/(d T) $
    $ E = 1/2 C V^2 $
    $ Q = C V $
    // - Capacitors in series act like Resistors in Parallel
    //   Capacitors in parallel act like Resistors in Series

    #colbreak()
    #inline("Inductor Equations")
    $ V = L (d I)/(d T) $
    $ i(t) = 1/L integral_(t_0)^t i(tau)d tau + i(t_0) $
    $ E = 1/2 L I^2 $
    $ I = Q T $
    // - Inductors in series and parallel act like Resistors
  ]
]
= Rectifiers
#let vrpp = $V_(r(p p))$
#let vodc = $V_(o(D C))$
#let vop = $V_(o(p))$
#concept-block[
  #text(size: 8pt)[
    $ V_"RMS" times sqrt(2) = V_p $
    $ V_(o(D C)) = V_(o(p)) - 1/2 vrpp $
    $ vrpp tilde.eq vodc/(2 f R_L C) = tilde.eq vop/(2 f R_L C) $
  ]
  For a Full-Wave Rectifier Circuit
  #text(size: 8pt)[
    $ vrpp tilde.eq vrpp/(f R_L C) $
    $ gamma = vrpp/vodc times 100% $
  ]
  - PIV means Peak Internal Voltage, $P I V = V_(i n(P)) - 0.7$ or for a full wave rectifier $P I V = V_(i n(P)) - 1.4$
]
= Diode
#concept-block[
  #inline("Zener Diode")
  $I_(Z K)$ Means Current Knee for a zener diode \
  $I_(Z m)$ Means Current Maximum for a zener diode
]
= Proofs/Questions
#concept-block[
  #inline("Ripple Factor")
  $
         Q & = C V \
         Q & = C vrpp \
         I & = Q/t \
         Q & = I t \
    C vrpp & = I/t \
      vrpp & = (I t)/(C) \
      vrpp & = (I t)/(C) \
         I & tilde.eq vop / R_L \
         t & = 1 / f \
      vrpp & tilde.eq (vop)/(f R_L C) \
  $
  For a full wave rectifier circuit, $t = 1/(2f)$
]
