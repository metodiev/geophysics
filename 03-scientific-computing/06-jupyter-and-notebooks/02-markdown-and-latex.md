---
id: 03-06-02
title: "Markdown and LaTeX in Notebooks"
level: beginner
prereqs: ["03-06-01"]
estimated_minutes: 75
tags: [jupyter, markdown, latex, documentation, reproducibility]
---

# Markdown and LaTeX in Notebooks

Half of a notebook is not code. That half is where the reader learns what the
code is for, which units the numbers carry, and which of the many possible
formulas was actually used. This lesson is about writing that half so that it
cannot silently disagree with the code beside it.

There is a specific failure mode to keep in mind throughout. A notebook is
**JSON**: the markdown source is stored character for character and is typeset
later, in the browser, by MathJax. Nothing is validated at save time. A mistyped
`$` is persisted, not repaired. So the question this lesson answers is: how do
you know your mathematics rendered correctly for the reader, when you are looking
at a screen that rendered it correctly for you?

Every number quoted below comes from running the demonstration:

```bash
.venv/bin/python 03-scientific-computing/06-jupyter-and-notebooks/code/markdown_and_latex_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what a notebook stores for a markdown cell and what it defers to the
   browser, with the measured evidence that the source survives a round trip
   unchanged.
2. **Count** the mathematics in a cell — inline spans and display spans — and
   **check** the delimiter balance the way this repository's own quality gate
   does.
3. **Explain** why fenced code must be removed before that check, with the
   measured count that shows what happens if it is not.
4. **Generate** LaTeX from SymPy so that the formula in the prose and the formula
   in the code have a single source.
5. **Describe** what an HTML export contains, including the fact that the
   mathematics is left for MathJax rather than rendered.

## Prerequisites

- [03-06-01 Notebook Workflow, Cells, Kernels and Execution Order](./01-notebook-workflow.md)
  — the file/kernel/front-end split this lesson builds on.

## 1. Intuition: the notebook is a source file, not a document

Compare a notebook cell with a figure in a paper. A figure is a finished object:
what you see is what every reader sees. A markdown cell is not. It is a source
file in a small markup language, and the rendering happens on the reader's
machine, in a library that may not be the one you used.

That has three consequences:

1. **You cannot check rendering by looking.** Your screen proves your browser
   works, not that the file is right.
2. **The source is what gets archived.** A repository of notebooks ships
   `$\nabla^2 V = 0$`, not an image of it. Anyone reading the notebook as text —
   a diff, a code review, a plain-text search — sees the source.
3. **Errors are cheap to make and invisible.** An unmatched `$` does not raise.
   It simply swallows the rest of the paragraph into a failed math span.

The good news is that the source is checkable, mechanically, and the check is
about ten lines long. Section 3 writes it.

## 2. Precise definitions

**Markdown cell.** A cell whose `cell_type` is `"markdown"`. Its `source` is a
string. The kernel never sees it; the front end renders it.

**Inline mathematics.** A span delimited by single dollar signs, `$...$`,
rendered in the flow of the text.

**Display mathematics.** A span delimited by double dollar signs, `$$...$$`,
usually set on its own line and centred.

**Fenced code block.** A region delimited by ``` ``` ``` on its own line, whose
content is literal. The demonstration found this matters: a dollar sign inside
a fence is not a delimiter.

**Round trip.** Writing a notebook to JSON and reading it back. The measured
result was

```
  round-trips through nbformat unchanged: True
```

**MathJax.** The JavaScript library that the front end uses to typeset the
mathematics in the browser at view time. It is why the HTML export contains
LaTeX source rather than pictures of formulas.

## 3. Counting mathematics, and the balance check

This repository's quality gate checks that every `$` in every markdown file is
matched. The rule it applies is a small state machine:

- count `$$` occurrences in the file — the total must be **even**;
- for inline spans, walk the lines and toggle a flag on each unmatched `$`,
  where a `$` escaped as `\$` does not count;
- if the flag is still set at the end, report the line where the span opened.

The demonstration applies exactly that rule to a markdown cell, first to the raw
text and then after blanking fenced code blocks, as the gate does:

```python
def _strip_code(text: str) -> list[str]:
    """Blank out fenced code blocks -- the same job tools/check_all.py does."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return out


def math_report(text: str, strip_code: bool):
    lines = _strip_code(text) if strip_code else text.splitlines()
    doubled = sum(line.count("$$") for line in lines)
    open_at = None
    for index, line in enumerate(lines, start=1):
        residue = line.replace("$$", "")
        count = residue.count("$") - residue.count(r"\$")
        if count % 2 == 1:
            open_at = index if open_at is None else None
    return doubled, open_at is None, doubled % 2 == 0
```

The measured result on a cell containing one display span, two inline spans, and
a Python fence with a dollar sign in it:

```
  raw text:      '$$' count = 2, even = True, inline balance ok = False
  code stripped: '$$' count = 2, even = True, inline balance ok = True
  unescaped '$' inside the fenced block: 1
```

The raw count reports an unbalanced file. It is wrong, and it is wrong in exactly
the way that would make the check useless in practice: any listing that shows a
shell prompt, a `$PATH`, or a price would be flagged. **Blank the fences
first.** This is a general principle worth carrying beyond notebooks: a checker
that does not know the language it is checking will produce confident nonsense.

## 4. Derivation: what survives, and what does not

Let a markdown cell have source $s$. The pipeline from author to reader is

$$s \;\xrightarrow{\text{save}}\; \text{JSON} \;\xrightarrow{\text{load}}\;
s' \;\xrightarrow{\text{render}}\; R(s'),$$

where $R$ is the renderer. The check we can perform mechanically is $s' = s$.
The check we cannot perform mechanically is that $R(s)$ looks right — that is a
judgement about typesetting, and it is the reader's, not the machine's.

The demonstration measures the first equality and a partial version of the
second:

```
  markdown cell source length: 436 characters, 14 lines
  round-trips through nbformat unchanged: True
  '$' characters in the source: 19
  '$$' occurrences: 2 (display math spans: 1)
  pipe-table rows (lines starting with '|'): 5
  exported HTML length: 771 characters
  '$' preserved: 19 of 19
  '$$' preserved: 2 of 2
  '<table>' elements produced from the pipe table: 1
  '<td>' cells produced: 9
```

Three things follow.

**The source is exact.** $s' = s$ held: the round trip is lossless. That means a
typo is preserved forever, and so is a correct formula, and the machine cannot
tell them apart.

**Delimiters survive into the export.** All 19 dollar signs arrived in the HTML.
Nothing was rendered server-side. The `<span class="math">` wrappers that a
server-side renderer would produce numbered **0**, which is the measured
confirmation that the mathematics is left for the client.

**Structure is converted, mathematics is not.** The five pipe-table rows became
one `<table>` with nine `<td>` cells. Markdown structure is transformed into
HTML by the exporter; mathematical notation passes through untouched.

The practical consequence: **an HTML export rendered without JavaScript (a PDF
converter that does not run MathJax, or a text-only reader) shows the raw
dollar signs.** That is not a bug in your notebook, and it is worth knowing
before you submit a notebook-rendered PDF.

## 5. Units, dimensions and the prose that carries them

A notebook's markdown is the only place where a variable's unit can be stated
without inventing a naming convention. The demonstration uses this definition of
the vertical attraction of a point mass:

$$g_z = \frac{G M z}{(x^2 + z^2)^{3/2}},$$

whose dimensions are

$$[g_z] = \frac{\mathrm{m^3\,kg^{-1}\,s^{-2}} \cdot \mathrm{kg} \cdot
\mathrm{m}}{\mathrm{m^3}} = \mathrm{m\,s^{-2}},$$

and the geophysical reporting convention is

$$g_z\ [\mathrm{mGal}] = \frac{g_z\ [\mathrm{m\,s^{-2}}]}{10^{-5}}.$$

A prose cell that says "g_z in mGal" carries information that no amount of code
can carry, because the code computes in SI. The convention used in this
curriculum is stated once per notebook, in the first markdown cell, in this form:

> All gravity values are reported in mGal ($1\ \mathrm{mGal} = 10^{-5}\
> \mathrm{m\,s^{-2}}$); all depths in metres; all densities in
> $\mathrm{kg\,m^{-3}}$.

Three lines of prose, and every number in the notebook becomes unambiguous. If
the code later changes unit system, the prose changes with it — which is a
diff a reviewer can see, unlike a factor of $10^{-5}$ buried in a multiplication.

## 6. Generating the LaTeX instead of typing it

Hand-typed mathematics can disagree with the code. Generated mathematics cannot.
SymPy's `latex()` printer turns an expression into LaTeX, so the formula in the
prose and the expression in the code can be the same object. The demonstration
prints both, and reports the size of each:

```python
G, M, x, y, z, r, t, f = sp.symbols("G M x y z r t f")
potential = -G * M / r
r_of_xyz = sp.sqrt(x**2 + y**2 + z**2)
gz = sp.simplify(-sp.diff(potential.subs(r, r_of_xyz), z))
print(sp.latex(gz))
```

Measured output:

```
  potential V(r)        -> - \frac{G M}{r}
  dV/dr partial         -> \frac{G M}{r^{2}}
  vertical attraction   -> - \frac{G M z}{\left(x^{2} + y^{2} + z^{2}\right)^{\frac{3}{2}}}
  g_z at y = 0          -> - \frac{G M z}{\left(x^{2} + z^{2}\right)^{\frac{3}{2}}}
  Ricker wavelet        -> \left(- 2 \pi^{2} f^{2} t^{2} + 1\right) e^{- \pi^{2} f^{2} t^{2}}
  barometric factor     -> e^{- \frac{z}{H}}
  diffusion front       -> \operatorname{erfc}{\left(\frac{z}{2 \sqrt{\kappa} \sqrt{t}} \right)}
          V:  15 characters of LaTeX, 3 operations
     Ricker:  66 characters of LaTeX, 14 operations
       erfc:  69 characters of LaTeX, 8 operations
```

The last line of the block is the payoff: `sp.latex()` produced
`\operatorname{erfc}` for the complementary error function, which is the correct
LaTeX for an operator name and not something one types reliably from memory. The
generated string is also the string the code used — a single source for both.

The workflow that makes this practical:

1. Derive the expression in a cell, with the derivation visible.
2. Print `sp.latex(expr)` in that same cell.
3. Paste the output into the markdown cell **with the expression beside it**, and
   note in the prose that it was generated.

Step 3 is the discipline. A generated formula pasted without provenance is
indistinguishable from a typed one after a week.

## 7. Worked examples

### 7.1 A mistyped delimiter, and how it is found

You write:

```
The anomaly is $g_z = GMz / (x^2+z^2)^{3/2} and it decays as $z^{-3}$.
```

There are three `$` characters, so one span is left open, and the renderer
swallows the rest of the paragraph. You will not notice, because the visible
part looks plausible. The balance check finds it in one pass and reports the
line where the span opened. **Run the check on every markdown file you commit**;
this repository does.

### 7.2 Prose that lies about a changed default

A notebook computes a Bouguer correction with $\rho = 2670\ \mathrm{kg\,m^{-3}}$
and its markdown says so. A reviewer asks for $2400\ \mathrm{kg\,m^{-3}}$ to
match a density log. The code is edited; the prose is not. The notebook now
states two different densities and the figure corresponds to the second.

The fix is to make the prose carry the *number from the code*, which is possible
when the prose is generated too. A cheaper fix, which is what most working
notebooks do, is to put the number in one cell and write the prose to reference
it by name rather than by value: "the Bouguer density `rho_b` set in cell 3",
instead of "2670 kg/m³". A prose cell that names a variable cannot go stale,
because it does not contain the value.

### 7.3 A table that is worth a table

Reading ten numbers out of a paragraph is slow and error-prone; a table is
better, and the pipe syntax is compact. The demonstration's table had five rows
in the source and became `<table>` with nine `<td>` cells in the HTML. Two
conventions worth adopting:

- **Every numeric column carries its unit in the header.** `g_z (mGal)`, not
  `g_z` and a sentence later.
- **State the number of significant figures you are claiming.** A column headed
  `RMS misfit (mGal)` with values `0.496` claims three.

## 8. Assumptions and limitations

- **The rendering is the reader's.** This lesson measures the source and the
  export; it cannot measure what your colleague's Jupyter version does with a
  `\begin{aligned}` inside `$$`.
- **`$` is overloaded.** In a notebook about finance, or a shell listing,
  a literal `$` needs escaping (`\$`) or a code span. The gate's rule treats
  `\$` as escaped and everything else as a delimiter.
- **MathJax is not LaTeX.** A notebook cell is typeset by a JavaScript library
  with a subset of LaTeX plus extensions (`\ce{}`, `\pu{}` and so on in some
  configurations). A construct that works in a `.tex` file may not render here.
  I did not test any extended MathJax packages in this environment, so I make no
  claim about which are available.
- **Markdown dialects differ.** Jupyter's markdown is CommonMark-ish with
  extensions; GitHub's rendering of the same `README.md` may differ. A table
  that renders in the notebook may need an HTML `<table>` on a platform that
  disables tables.
- **No rendering was measured in this lesson.** Everything quoted is either a
  byte-level fact about the JSON or the HTML, or an arithmetic count. Nothing in
  Section 4 depends on how anything looked.

## 9. Python demonstration

The full script is `code/markdown_and_latex_demo.py`. Its four parts, and what
each one establishes:

| Part | Does | Measured result |
|---|---|---|
| 1 | Builds a prose cell and round-trips it | `round-trips through nbformat unchanged: True` |
| 2 | Runs the delimiter-balance rule on raw and stripped text | raw reports `inline balance ok = False`, stripped `True` |
| 3 | Generates LaTeX with SymPy | six formulas, `15`–`69` characters each |
| 4 | Exports to HTML with `nbconvert.filters.markdown2html` | `19 of 19` dollar signs preserved, `1` `<table>` |

The one line of guidance: run the balance check on your own notebooks from a
pre-commit hook, not from memory. It is ten lines of code and it catches the only
markdown error that a human being reliably fails to see.

## 10. Exercises

Solutions, with the measured numbers, are in
[`exercises/02-markdown-and-latex-solutions.md`](./exercises/02-markdown-and-latex-solutions.md).

### ★ Foundational

**★1.** For each markdown source, say whether the delimiter balance check passes
and why: (a) `The value is $2.0$ mGal.` (b) `Cost: $5 and $7.` (c) `$$a = b$$
and $$c = d$$` (d) `Use \$ to escape a dollar.`

**★2.** Write the markdown for a three-column table of gravity stations with
columns for name, elevation in metres, and observed gravity in mGal, and state
the significant figures each numeric column claims.

**★3.** Convert to LaTeX by hand and then check with `sympy.latex`:
(a) $g_z = 2\pi G \rho h$, (b) $T(z,t) = T_0 + \Delta T\,
\mathrm{erfc}\!\left(\frac{z}{2\sqrt{\kappa t}}\right)$.

**★4.** Why does an unbalanced `$` not raise an error anywhere in the toolchain?

### ★★ Applied

**★★5.** Implement the balance checker of Section 3 in a file of your own and
run it on this curriculum's lesson files. Report the number of files scanned and
the number flagged, and state what you did about the flagged ones.

**★★6.** A markdown cell contains a shell transcript with three `$` prompts. Show,
with counts, what the raw checker reports and what the fence-stripping checker
reports, and explain why the second is the useful one.

**★★7.** Take a formula you use in your own work, derive it symbolically with
SymPy, print its LaTeX, and embed both in a markdown cell. Then change one
constant in the derivation and confirm that the prose and the code change
together. Report the two LaTeX strings.

**★★8.** Export a notebook containing display mathematics to HTML with
`nbconvert --to html` and search the output for the LaTeX source. Report whether
the mathematics was rendered server-side or left for the client, with the
evidence.

### ★★★ Research-oriented

**★★★9.** Design and run an experiment that quantifies the *cost* of a broken
delimiter. Using five formulas of increasing complexity, render each as (a)
inline `$...$`, (b) display `$$...$$`, and (c) inside a fenced Python block, and
report the character count of the resulting HTML for each. State what your
measurement does and does not tell you about legibility.

**★★★10.** Write a checker that goes beyond delimiter balance: it should detect
(a) a `$` span that opens and closes on different paragraphs, (b) a display span
that is not on its own line, and (c) a table whose header row has a different
number of columns from its body rows. Report the false-positive rate on this
repository's lesson files, and be explicit about the rules you had to weaken to
get the rate down.

## 11. Common mistakes

1. **Typing `$` for a currency symbol** in a cell that also contains real
   mathematics. Escape it, or put the prices in a code span.
2. **Assuming a rendering you saw is a rendering you will get.** The check is on
   the source; the rendering is not yours to control.
3. **Letting prose and code drift apart.** Name the variable, not the value.
4. **Forgetting that a fence is literal.** A dollar sign inside a listing is not
   a delimiter, which is why the checker strips fences first.
5. **Pasting generated LaTeX without provenance.** Note that it was generated and
   from what.
6. **Writing a paragraph where a table belongs.** Five rows of four numbers is a
   table.
7. **Leaving units out of the header row.** A column of numbers without units is
   not data, it is arithmetic.

## 12. Real-world applications

- **A methods section in a notebook.** The derivation, the code that implements
  it, and the figure share one file. When the reviewer asks which formula was
  used, the answer is one cell away and cannot disagree with the code.
- **A field-data report.** Prose states the instrument resolution and the
  calibration date; code applies the corrections; the reader sees both in the
  same document.
- **Teaching material.** Students read the derivation and immediately run the
  implementation. A mistyped formula is visible as a wrong number within seconds.
- **A dissertation chapter's analysis.** The prose and code stay together until
  the figure is exported, at which point lesson
  [04](./04-notebooks-to-scripts.md) takes over.
- **Code review.** Reviewing a notebook diff means reviewing markdown source.
  A line-by-line diff of LaTeX is readable; a diff of rendered equations is not,
  which is one more reason to keep the source in the repository and the rendered
  output beside it.

## 13. Further reading

- **Jupyter documentation** (jupyter.org). Level: beginner. The markdown
  reference for notebooks, including the supported MathJax delimiters.
- **The Jupyter Notebook format specification** (nbformat documentation).
  Level: intermediate. The `cell_type` and `source` fields that Section 2
  defines, and the rule that a markdown cell has no outputs.
- **MathJax documentation** (docs.mathjax.org, cited through the Jupyter
  documentation). Level: intermediate. Which LaTeX constructs are supported and
  which extensions exist.
- **Github-flavored Markdown specification.** Level: beginner. The table and
  fence syntax, and where it differs from CommonMark; relevant because the same
  `README.md` is rendered by several different engines.
- **SymPy printing documentation** (sympy.org). Level: intermediate. The
  `latex()` printer used in Section 6, including how to change the
  multiplication and function-name conventions.

> Note on citations: bibliographic details and project sites are given so you can
> locate the works. This repository does not host or reproduce copyrighted text.

## 14. Related lessons

- [01 Notebook Workflow, Cells, Kernels and Execution Order](./01-notebook-workflow.md)
  — the code half of the same file.
- [03 Making Notebooks Reproducible](./03-reproducible-notebooks.md) — what has
  to hold for the prose to stay true as well as the numbers.
- [04 Converting Notebooks to Scripts, Tests and Reports](./04-notebooks-to-scripts.md)
  — where markdown goes when the notebook is exported.
- [03-07 SymPy and Symbolic Computation](../07-sympy/README.md) — the source of
  generated formulas, and of the `latex()` printer used here.
- [03-05-06 Colormaps and Perception](../05-plotting-and-visualisation/06-colormaps-perception.md)
  — the same argument applied to colour rather than notation.

## 15. Self-assessment checklist

- [ ] I can state what a markdown cell stores and what is deferred. (§1)
- [ ] I can count display and inline math spans in a cell by hand. (§3)
- [ ] I can explain why fenced code is stripped before the balance check. (§3)
- [ ] I can say what the round-trip test proves and what it does not. (§4)
- [ ] I can write a units statement for a notebook in three lines. (§5)
- [ ] I can generate the LaTeX for an expression from SymPy. (§6)
- [ ] I know to check the delimiters mechanically rather than by eye. (§9)
