#set page(margin: 2.5cm)
#set text(font: "New Computer Modern", size: 11pt)

#align(center)[
  #text(size: 14pt, weight: "bold")[ANU Physics Academic Integrity Declaration Form]
]

#v(0.5em)

// --- Basic info ---
#let fill(width: 4cm) = box(width: width, stroke: (bottom: 0.5pt))

#grid(
  columns: (1fr, 1fr),
  gutter: 1em,
  [Name: Bryce Tabangcura], [Student ID: u7851189],
  [Date: #datetime.today().display("[day]/[month]/[year]")], [Assessment Item: Physics Assignment 3],
)

#v(1em)

// --- Collaboration ---
#text(weight: "bold")[Collaboration with others]

You are encouraged to discuss problems with other students, however you must submit your own work. The minimum penalty for plagiarism is a fail on the assessment task, and all incidents of plagiarism are recorded on a student's academic record.

If you have collaborated with others, please note these people here:

Lachlan Hynd

#v(1em)

// --- AI tools ---
#text(weight: "bold")[Use of AI Tools]

You may not present material produced by generative AI as your own work, as this is an academic integrity breach. If you have used AI in this assessment, the use must be declared here:

#let checkbox(checked: false) = box(
  width: 0.9em,
  height: 0.9em,
  stroke: 0.6pt,
  inset: 0pt,
)[
  #if checked {
    align(center + horizon, text(size: 0.75em, weight: "bold")[×])
  }
]

#grid(
  columns: (auto, auto),
  gutter: 0.6em,
  checkbox(checked: true), [No AI tools were used for this assignment],
)
#grid(
  columns: (auto, auto),
  gutter: 0.6em,
  checkbox(checked: false), [AI tools were used as described below:],
)

AI Tools Used: claude

How AI was used (check all that apply):

#grid(
  columns: (auto, auto, auto, auto, auto, auto),
  gutter: 0.6em,
  checkbox(), [Mathematical calculations], checkbox(), [Problem solving], checkbox(), [Code generation],
)
#grid(
  columns: (auto, auto, auto, auto),
  gutter: 0.6em,
  checkbox(), [Writing assistance], checkbox(), [Research],
  checkbox(), [Other: #fill()],
)

#v(0.5em)
#text(weight: "bold")[Chat Evidence Required] — you must include your complete AI conversation(s):

#grid(
  columns: (auto, auto),
  gutter: 0.6em,
  checkbox(), [Full chat transcript pasted below],
)
#grid(
  columns: (auto, auto),
  gutter: 0.6em,
  checkbox(), [Full chat screenshots/files attached],
)
#grid(
  columns: (auto, auto),
  gutter: 0.6em,
  checkbox(),
)

#v(1em)

I declare that:

#grid(
  columns: (auto, auto),
  gutter: 0.6em,
  checkbox(checked: true), [This AI use declaration is complete and accurate],
)
#grid(
  columns: (auto, auto),
  gutter: 0.6em,
  checkbox(checked: true), [I have included unedited records of all AI interactions],
)
#grid(
  columns: (auto, auto),
  gutter: 0.6em,
  checkbox(checked: true), [I understand the physics concepts and can explain my work],
)
#grid(
  columns: (auto, auto),
  gutter: 0.6em,
  checkbox(checked: true), [I remain responsible for all content in my submission],
)

#v(1.5em)

#grid(
  columns: (1fr, 1fr),
  gutter: 1em,
  [Signature: Bryce Tabangcura], [Date: #datetime.today().display("[day]/[month]/[year]")],
)
