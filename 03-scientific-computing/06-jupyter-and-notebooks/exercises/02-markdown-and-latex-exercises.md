# Exercises — 03-06-02 Markdown and LaTeX in Notebooks

> Solutions, with the measured counts, are in
> [`02-markdown-and-latex-solutions.md`](./02-markdown-and-latex-solutions.md).

The balance rule to apply throughout is the one this repository's quality gate
uses: `$$` occurrences must total an even number, and after removing `$$` and
escaped `\$`, every line must contain an even number of `$`.

---

## ★ Foundational

**★1.** For each source, say whether the balance check passes and why:
(a) `The value is $2.0$ mGal.` (b) `Cost: $5 and $7.` (c) `$$a = b$$ and $$c = d$$`
(d) `Use \$ to escape a dollar.`

**★2.** Write the Markdown for a three-column table of gravity stations: name,
elevation in metres, observed gravity in mGal. State the significant figures each
numeric column claims.

**★3.** Convert to LaTeX by hand, then check with `sympy.latex`:
(a) $g_z = 2\pi G \rho h$, (b) $T(z,t) = T_0 + \Delta T\,\mathrm{erfc}(z/(2\sqrt{\kappa t}))$.

**★4.** Why does an unbalanced `$` raise no error anywhere in the toolchain?

**★5.** What does a fenced code block change about the balance check, and why?

---

## ★★ Applied

**★★6.** Implement the balance checker of the lesson's §3 in a file of your own
and run it over the lesson files of this curriculum. Report the number of files
scanned and the number flagged, and state what you did about the flagged ones.

**★★7.** A markdown cell contains a shell transcript with three `$` prompts. Show,
with counts, what the raw checker reports and what the fence-stripping checker
reports, and explain why the second is the useful one.

**★★8.** Take a formula from your own work, derive it with SymPy, print its LaTeX,
and embed both in a markdown cell. Then change one constant in the derivation and
confirm that prose and code change together. Report the two LaTeX strings.

**★★9.** Export a notebook containing display mathematics to HTML with
`nbconvert --to html`, search the output for the LaTeX source, and report whether
the mathematics was rendered server-side or left for the client, with the
evidence.

**★★10.** Write a units statement (three lines) for a notebook that reports
gravity in mGal, depths in metres and densities in kg/m³, and check that every
number in the notebook's prose is covered by it.

---

## ★★★ Research-oriented

**★★★11.** Design and run an experiment that quantifies the *cost* of a broken
delimiter. Using five formulas of increasing complexity, render each as (a) inline
`$...$`, (b) display `$$...$$`, and (c) inside a fenced block, and report the
character count of the resulting HTML for each. State what your measurement does
and does not tell you about legibility.

**★★★12.** Write a checker that goes beyond delimiter balance: it should detect
(a) a `$` span that opens and closes in different paragraphs, (b) a display span
not on its own line, and (c) a table whose header row has a different number of
columns from its body rows. Report the false-positive rate on this repository's
lesson files and be explicit about the rules you had to weaken to get it down.
