#import "@preview/boxed-sheet:0.1.2": *
//#import "../src/lib.typ": *

#set text(font: (
  "JetBrainsMono NF",
  // "Public Sans",
))

#let homepage = link("https://cowburrs.github.io/portfolio/")[https://cowburrs.github.io/portfolio/]
#let author = "Bryce"
#let title = "PHYS1201 Cheat Sheet"

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
  font-size: 6pt, // Size of font (Default = 5.5pt)
  line-skip: 5.5pt, // Size of line-skip (Default = 5.5pt)
  x-margin: 10pt, // Margin on x-axis (Default = 30pt)
  y-margin: 30pt, // Margin on y-axis (Default = 0pt)
  num-columns: 4, // Number of columns (Default = 5)
  column-gutter: 2pt, // Space between columns (Default = 4pt)
  numbered-units: false, // Numbering of units (Default = false)
  color-box: my-colors, // Color scheme of boxes
)

= Classical Physics
#concept-block[
  #inline("Lagrange")
  $ L = K - V $
  $ d/(d t) (partial L)/(partial dot(x)) = (partial L)/(partial x) $
  Cyclic variables are variables which don't appear in the Lagrangian.
  #inline("Hamiltonian and Stationary action")
  $ H = sum_(i) p_i dot(q)_i - L $ Where $q$ is all cyclic variables.
  $ S = integral_(t_1)^(t_2) L d t $
  $ delta S = 0; (d S)/(d t) = 0 $
  $S >> planck$ means that the paths get cut down a lot, to the
  point where only the stationary action survives.
]
= Quanta
#concept-block[
  #inline("Equations")
  $ phi_(A -> B) = N sum_("paths") e^(i S\/ planck) $
  $ P = abs(phi_(A -> B))^2 $
  #inline("Misc")
  $ planck = h/(2 pi) $
  $ lambda = h/p $
  #inline("Stationary Action")
  $ S = 2pi n planck = n h $
]
= Special Relativity
#concept-block[
  // #inline("Relativistic Lagrangian")
  #inline("Dilation")
  $
    gamma = 1/(sqrt(1 - v^2/c^2)) \
    x' = gamma(x - v t) \
    t' = gamma(t - ((x v)/c^2)) \
    Delta t' = gamma Delta t \
    Delta x' = (Delta x) / gamma \
  $
  #inline("Relativistic Equations")
  $
    E = gamma m c^2 = sqrt(m^2c^4 + p^2c^2) \
    p = gamma m v \
  $
]
= Particles
#concept-block[
  $ Q = (Delta M_"Reactants" - Delta M_"Products")c^2 $ \
  Forbidden if $Q$ value is less than 0
  $ T_(1\/2) = tau ln(2) $
  Same form for oscillators: amplitude has $tau_A = 2/gamma$, energy has $tau_E = 1/gamma$, so $T_(1\/2) = tau ln(2)$ with the matching $tau$.
]
= Oscillation
#concept-block[
  #inline("General Form")
  $ m dot.double(x) + r dot(x) + k x = 0 $
  $ dot.double(x) + gamma dot(x) + omega_0^2 x = 0 $
  $ omega_0^2 = g/L $
  $ omega = 2 pi f $
  - The period of an undamped pendulum: $T = 2 pi sqrt(L/g)$

  $ E = E_0e^(-gamma t) $
  $ A = A_0e^(-(gamma t)/2) $

  $ tau = 2/gamma $
  Max amplitude at $omega = sqrt(omega_0^2 - gamma^2/2)$
  But max velocity and power at $omega_0$ // NOTE: Check this
  #inline("Driven Oscillator")
  $ m dot.double(x) + r dot(x) + k x = F_0e^(i omega t) $
  $ A e^(i phi) = F_0/(m(omega_0^2 - omega^2 + i gamma omega)) $
  $ Q = omega_0/(Delta w) = omega_0/gamma $
  - $Delta w$ is the frequency difference between the two halfway points of the peak
  #inline("Couple Oscillator")
  - The symmetric frequency is when the
    the vector has equal components, so $vec(1, 1)$
    and the antisymmetric node would be $vec(1, -1)$
  #inline("Impedance")
  $ Z = m/omega (i(omega^2 - omega_0^2) + gamma omega) = r + i(m omega - k/omega) $
  $ theta = phi + pi/2 = -arg(Z) $
  $theta$ is phase of velocity and $phi$ is phase of position
  $ r = (Z_1 - Z_2)/(Z_1 + Z_2) $
  $ t = (2 Z_1)/(Z_1 + Z_2) $
  #inline("String and Tension")
  $ c^2 = T/eta $
  $ Z = eta c = sqrt(T eta) $
]
= Lens and Diffraction
#concept-block[
  #inline("Snells Law")
  $ lambda_1/sin(theta_1) = lambda_2/sin(theta_2) $
  $ n_1 sin(theta_1) = n_2 sin(theta_2) $
  $ n = c/v $
  #inline("Lenses")
  $ 1/f = (n_"lens"/n_0 - 1)(1/R_1 - 1/R_2) $
  $ 1/f = 1/o + 1/i $
  $ M = h'/h = -i/o $
  $ tan(theta) = h/f "(Parallel Rays)" $
  #inline("Michelson Interferometer")
  #let eout = $E_"out"$
  $ eout = r E_2 + t E_1 $
  $ t^2 + r^2 = 1 $
  $
    I_"out" & = abs(eout)^2 = 2r^2t^2 E_"in"^2(1 - cos(Delta phi)) \
            & = 4r^2t^2E_"in"^2 sin^2((Delta phi)/2) \
            & = 4r^2t^2E_"in"^2 sin^2((2pi)/lambda (L_2 - L_1))
  $
  \* Note: $L_1$ and $L_2$ order does not matter
  #inline("Abbe's limit/Diffraction")
  $d = lambda/(2n sin(theta))$
  or for air
  $ d = lambda/(2sin(theta)) $
  #inline("Diffraction")
  $ d sin(theta) = m lambda $
  $ r = (v_2 - v_1)/(v_2 + v_1) $
  $ t = (2 v_2)/(v_1 + v_2) $
  $ A_t = t A_i $
  $ A_r = r A_i $
]
= Waves and Modes
#concept-block[
  #inline("Standing Waves")
  Open-Open: $f_n = (n c)/(2 L), quad n = 1, 2, 3, dots$

  Closed-Open: $f_n = ((2n - 1) c)/(4 L), quad n = 1, 2, 3, dots$

  Closed-Closed: $f_n = (n c)/(2 L), quad n = 1, 2, 3, dots$
]
= Constants/Miscellaneous
#concept-block[
  #inline("Taylor Approximation")
  for $abs(x) << 1$
  $
    sin(x) tilde.eq tan(x) tilde.eq x\
    cos(x) tilde.eq 1\
    (1 + x)^n tilde.eq (1 + x n)
  $
  #inline("Trig Identities")
  $ A_1 cos(omega t) + A_2 sin(omega t) = C cos(omega t + phi), quad tan(phi) = -A_2/A_1 $
]
