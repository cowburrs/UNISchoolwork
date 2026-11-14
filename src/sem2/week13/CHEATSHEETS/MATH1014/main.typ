#import "@preview/boxed-sheet:0.1.2": *
//#import "../src/lib.typ": *

#set text(font: (
  "JetBrainsMono NF",
  // "Public Sans",
))

#let homepage = link("https://cowburrs.github.io/portfolio/")[https://example.com]
#let author = "MATH1014 Cheat Sheet"
#let title = "MATH1014 Cheat Sheet"

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
  // title: title, // Title of document
  // homepage: homepage, // Homepage of author
  authors: author, // Author Name
  write-title: true, // Writes Title on the first page
  title-align: center, // Position of titles in concept box
  title-number: true, // Whether to numbered the title (Default = true)
  title-delta: 2pt, // Fonts delta for title scaling (Default = 1pt)
  // scaling-size: true, // Whether to scale the titles (Default = false)
  font-size: 10pt, // Size of font (Default = 5.5pt)
  line-skip: 5.5pt, // Size of line-skip (Default = 5.5pt)
  x-margin: 10pt, // Margin on x-axis (Default = 30pt)
  y-margin: 30pt, // Margin on y-axis (Default = 0pt)
  num-columns: 4, // Number of columns (Default = 5)
  column-gutter: 2pt, // Space between columns (Default = 4pt)
  numbered-units: false, // Numbering of units (Default = false)
  color-box: my-colors, // Color scheme of boxes
)
#let cen(body) = align(center)[#body]
= Divergence/Convergence tests
#concept-block[
  #align(center)[
    #table(
      columns: 2,
      stroke: none,
      inset: 4pt,
      table.hline(),
      [$D$], [Diverge],
      [$C$], [Converge],
      [$I$], [Inconclusive],
      table.hline(),
    )
  ]

  #inline("p-series")
  #cen[$p > 1 => sum 1/n^p = C$, $p <= 1 => D$]

  #inline("Integral")
  $ f > 0 "continuous decreasing", a_n = f(n) $
  $ integral_1^infinity f(x) dif x = C\/D <=> sum a_n = C\/D $

  #inline("Comparison")
  $ 0 <= a_n <= b_n, sum b_n = C => sum a_n = C $
  $ 0 <= b_n <= a_n, sum b_n = D => sum a_n = D $

  #inline("Limit comparison")
  $ a_n, b_n > 0, quad lim_(n -> infinity) a_n / b_n = c, quad 0 < c < infinity $
  $ sum b_n = C => sum a_n = C $
  $ sum b_n = D => sum a_n = D $

  #inline("Alternating series")
  $ sum (-1)^(n-1) b_n, quad b_n > 0 $
  $ b_n "decreasing", b_n -> 0 => C $

  #inline("Absolute convergence")
  $ sum |a_n| = C => sum a_n = C $

  #inline("Ratio")
  $ L = lim_(n -> infinity) |a_(n+1) / a_n| $
  #align(center)[
    $L < 1 => C$,
    $L > 1 => D$,
    $L = 1 => I$
  ]

  #inline("Root")
  $ L = lim_(n -> infinity) root(n, |a_n|) $
  #align(center)[
    $L < 1 => C$,
    $L > 1 => D$,
    $L = 1 => I$
  ]
]
= Lagrange Multipliers
#concept-block[
  #inline("Equation")
  #align(center)[
    $nabla f = lambda nabla g$
  ]
  #inline("Example")
  #grid(
    columns: (1fr, 1fr),
    column-gutter: 1em,
    stroke: (x, y) => if x == 1 { (left: 0.5pt) },
    align: center + horizon,
    [
      $ g(x,y) = x^2 + y^2 = 2 $
      $ vec(2, 2) = lambda vec(2x, 2y) $
      $ (1/lambda)^2 + (1/lambda)^2 = 2 $
      $ vec(2, 2) = 1 times vec(2x, 2y) $
    ],
    [
      $ f(x,y) = 2x + 2y $
      $ x = y = 1/lambda $
      $ lambda = plus.minus 1 $
      $ vec(2, 2) = -1 times vec(2x, 2y) $
    ],
  )
]
= Jacobian
#concept-block[
  $
    J = (partial(x, y))/(partial(u, v)) = mat(delim: "|", (partial x)/(partial u), (partial x)/(partial v); (partial y)/(partial u), (partial y)/(partial v)) = (partial x)/(partial u) (partial y)/(partial v) - (partial x)/(partial v) (partial y)/(partial u)
  $

  #inline("Change of variables")
  $
    integral.double_R f(x,y) dif A \
    = integral.double_S f(x(u,v), y(u,v)) |J| dif u dif v
  $
]
= Least Squares
#concept-block[
  #inline("Normal Formula")
  $ A^T A hat(x) = A^T b $
  #inline("Example")
  #align(center)[From the points $vec(0, 1), vec(1, 2), vec(2, 2)$]
  #columns(2)[
    $ A = mat(1, 0; 1, 1; 1, 2) $
    #colbreak()
    $ b = vec(1, 2, 2) $
  ]
]
= Partial Differentiation
#concept-block[
  #inline("Critical Point")
  $ f_x(x,y) = 0, f_y(x,y) = 0 $
  #inline("Second Derivatives Test")
  $ D = f_(x x) f_(y y) - (f_(x y))^2 $
  #inline("Interpretation of D")
  #align(center)[
    #table(
      columns: 2,
      stroke: none,
      inset: 4pt,
      table.hline(),
      [$D > 0, f_(x x) > 0$], [local min],
      [$D > 0, f_(x x) < 0$], [local max],
      [$D < 0$], [saddle],
      [$D = 0$], [inconclusive],
      table.hline(),
    )
  ]
]
= Polar Integrals
#concept-block[
  #inline("Equations")
  $ A = integral_alpha^beta 1/2 r^2 dif theta $
  $ L = integral_alpha^beta sqrt(r^2 + (dif r / (dif theta))^2) dif theta $
  #inline("Double Integral")
  $
    integral.double_D f(x,y) dif A \
    = integral_alpha^beta integral_(h_1(theta))^(h_2(theta)) f(r cos theta, r sin theta) r dif r dif theta
  $
]
= Plane/Line Equations
#concept-block[
  #inline[Line]
  #columns(2)[
    $ P_0 = (x_0, y_0, z_0) $
    #colbreak()
    $ arrow(v) = (a, b, c) $
  ]
  #table(
    columns: 2,
    stroke: none,
    inset: 4pt,
    table.hline(),
    [Vector], [$bold(r) = bold(r)_0 + t bold(v)$],
    [Parametric], [$x = x_0 + a t, quad y = y_0 + b t, quad z = z_0 + c t$],
    [Symmetric], [$(x - x_0)/a = (y - y_0)/b = (z - z_0)/c$],
    table.hline(),
  )

  #inline[Plane]
  #columns(2)[
    $ P_0 = (x_0, y_0, z_0) $
    #colbreak()
    $ arrow(n) = (a, b, c) $
  ]
  #table(
    columns: 2,
    stroke: none,
    inset: 4pt,
    table.hline(),
    [Vector], [$bold(n) dot (bold(r) - bold(r)_0) = 0$],
    [Scalar], [$a(x - x_0) + b(y - y_0) + c(z - z_0) = 0$],
    [Linear], [$a x + b y + c z = d, quad d = a x_0 + b y_0 + c z_0$],
    table.hline(),
  )

  #inline[Sphere]
  #columns(2)[
    $ arrow(c) = (h, k, l) $
    #colbreak()
    $ R = "radius" $
  ]
  #table(
    columns: 2,
    stroke: none,
    inset: 4pt,
    table.hline(),
    [Vector], [$|bold(r) - bold(c)| = R$],
    [Dot product], [$(bold(r) - bold(c)) dot (bold(r) - bold(c)) = R^2$],
    [Standard], [$(x - h)^2 + (y - k)^2 + (z - l)^2 = R^2$],
    [Expanded], [$x^2 + y^2 + z^2 + A x + B y + C z + E = 0$],
    table.hline(),
  )
]
// = Constants/Identities
// #concept-block[
//   #align(center)[
//     #inline[Arctan Integrals]
//     #table(
//       columns: 2,
//       stroke: none,
//       inset: 4pt,
//       table.hline(),
//       [$integral 1/(a^2+x^2) dif x$], [$1/a arctan(x/a) + C$],
//       [$integral 1/sqrt(a^2-x^2) dif x$], [$arcsin(x/a) + C$],
//       [$integral 1/(x sqrt(x^2-a^2)) dif x$], [$1/a op("arcsec") |x/a| + C$],
//       table.hline(),
//     )
//   ]
// ]
