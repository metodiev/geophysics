# Solutions — 03-06-02 Markdown and LaTeX in Notebooks

> **Read this after attempting the exercises.** Counts attributed to the
> demonstration are its actual output, produced with nbformat 5.11.1,
> nbconvert 7.17.2 and sympy 1.14.0 on Python 3.14.4.

---

## ★1 — Which sources pass

| Source | `$` count | Passes | Why |
|---|---|---|---|
| (a) `The value is $2.0$ mGal.` | 2 | yes | one balanced inline span |
| (b) `Cost: $5 and $7.` | 2 | yes, accidentally | the rule cannot tell currency from math |
| (c) `$$a = b$$ and $$c = d$$` | 8 (`$$` ×4) | yes | display delimiters are even in total |
| (d) `Use \$ to escape a dollar.` | 1, minus 1 escaped | yes | `\$` is excluded from the count |

Item (b) is the important one: **the balance check is a delimiter check, not a
semantics check.** A line with two currency signs passes and renders as
mathematics; only a human notices. That is why the demonstration's prose cell
contains the sentence "Do not write `$` for currency: `USD 5`."

---

## ★2 — A table with units in the headers

```
| Station | Elevation (m) | Observed gravity (mGal) |
|---|---|---|
| S01 | 412.3 | 979812.37 |
| S02 | 398.7 | 979812.61 |
| S03 | 405.1 | 979812.44 |
```

Significant figures claimed: elevation to 0.1 m (4 s.f. here), gravity to
0.01 mGal (7 s.f.). The demonstration's table produced
`'<table>' elements produced from the pipe table: 1` and `'<td>' cells produced:
9` from five pipe rows — three data rows plus header, in two columns plus the
name column.

---

## ★3 — LaTeX for two formulas

Hand-written:

```latex
g_z = 2 \pi G \rho h
T(z,t) = T_0 + \Delta T \, \operatorname{erfc}\!\left(\frac{z}{2\sqrt{\kappa t}}\right)
```

`sympy.latex` output for the same expressions, from the demonstration's run:

```
  Ricker wavelet        -> \left(- 2 \pi^{2} f^{2} t^{2} + 1\right) e^{- \pi^{2} f^{2} t^{2}}
  diffusion front       -> \operatorname{erfc}{\left(\frac{z}{2 \sqrt{\kappa} \sqrt{t}} \right)}
```

SymPy writes $\sqrt{\kappa}\sqrt{t}$ rather than $\sqrt{\kappa t}$ — algebraically
identical and not what a human would type. **That is the trade: generated LaTeX is
always correct and sometimes ugly.** The demonstration measured lengths of 66
characters for the Ricker and 69 for the diffusion front.

---

## ★4 — Why nothing fails

Because Markdown is not a language with a parser that can fail: it is a set of
textual conventions, and the mathematics inside it is handled by a JavaScript
library in the browser at view time. The demonstration measured the round trip
(`round-trips through nbformat unchanged: True`) and the export
(`'$' preserved: 19 of 19`), with
`'<span class="math' wrappers (server-side rendering): 0`. There is no step at
which an unmatched `$` could be detected, which is exactly why the check has to be
written by hand.

---

## ★5 — What a fence changes

A fenced block is literal text; nothing inside it is markup, so a `$` inside it is
not a delimiter. Measured, on a cell with one display span, two inline spans and a
fence containing a dollar sign:

```
  raw text:      '$$' count = 2, even = True, inline balance ok = False
  code stripped: '$$' count = 2, even = True, inline balance ok = True
  unescaped '$' inside the fenced block: 1
```

Without stripping, the checker reports a failure on a cell that is perfectly
correct. A checker with that false-positive rate gets disabled, which is worse
than not having one.

---

## ★6 — Running the checker

The implementation is the lesson's `_strip_code` plus the parity loop. On this
repository the gate itself reports
`files scanned for formulas: 1040` and `ok` for the LaTeX delimiter check, so a
correct implementation should flag nothing. If your version flags files, compare
your fence detection against the gate's: it treats a line whose stripped form
starts with ```` ``` ```` or `~~~` as a toggle, and it counts `$` **and** `\$$`
differently (`residue.count("$") - residue.count(r"\$")`).

---

## ★7 — A shell transcript

```
$ gmt --version
6.7.0
$ gmt --show-cores
10
$ echo done
done
```

Raw checker: three lines begin with a `$`; two of them (`$ gmt --version`,
`$ gmt --show-cores`) carry one `$` each and one carries... nothing (the `$ echo
done` line has one). Three lines with an odd `$` count flip the running state
three times, leaving it **open** at the end: `unclosed inline '$' math opened at
line ...`. Fence-stripped checker: the transcript is inside a fence, so the lines
are blanked and the state is never toggled: **ok**. The second is the useful one,
because the first reports a fault in a cell that a reader sees correctly.

---

## ★8 — Generated LaTeX from your own formula

The procedure matters more than the formula. Derive, print, paste, and note the
provenance. From the demonstration, the potential of a point mass and its
gradient:

```
  potential V(r)        -> - \frac{G M}{r}
  dV/dr partial         -> \frac{G M}{r^{2}}
```

Change $M$ to $2M$ in the derivation and the printed LaTeX changes to
`- \frac{2 G M}{r}` with no edit to the prose cell, provided the prose quotes the
generated string rather than a hand-typed copy.

---

## ★9 — HTML export

Measured, from the notebooks-to-scripts demonstration rather than this lesson's
own: the exported HTML was 280811 bytes, contained the LaTeX source
`2\pi G\rho h` **verbatim** (`True`), and contained **0** occurrences of
`class="math`. So the mathematics is passed through untouched and typeset in the
browser. The practical consequence is stated in the lesson: a PDF converter that
does not run MathJax shows the raw dollar signs.

---

## ★10 — A units statement

```
All gravity values are reported in mGal
($1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$);
all depths in metres; all densities in $\mathrm{kg\,m^{-3}}$.
All coordinates are WGS 84 geographic (longitude, latitude in degrees).
```

Checking completeness is mechanical: search the notebook's prose for a number and
ask which of the four claims covers it. The demonstration's own prose cell covers
$G$ (m³ kg⁻¹ s⁻²), $M$ (kg) and $g_z$ (m s⁻²) in a table, which is the same
technique in tabular form.

---

## ★11 — The cost of a broken delimiter

A defensible experiment: take five formulas of increasing length, render each in
the three ways, and count characters in the exported HTML. The measurement will
show that inline and display differ mainly in the wrapper tags (`<p>` versus
`<p>` with the same `$...$` content), so **the HTML character count is nearly
insensitive to the distinction** — which is a legitimate finding and a limit of
the experiment. It cannot tell you what a reader perceives, because nothing in the
pipeline measures legibility. State that.

---

## ★12 — A stronger checker

The three rules are implementable, and the false-positive rate is where the work
is. On this repository the rules that had to be weakened were:

- **(a)** a span that opens and closes in different paragraphs is common in long
  lessons where inline math wraps a line, so the rule must be "different paragraph
  *and* the span contains no `$` on any line in between";
- **(b)** display math not on its own line occurs legitimately inside table cells
  in this repository, so the rule must allow a `$$...$$` pair on one line;
- **(c)** header/body column count mismatches do occur in the curriculum's tables
  where a cell contains a `|` inside code, so the rule needs `|`-escaping.

The measured gate output for this repository is `LaTeX delimiters: ok`, which
means a correct implementation should find nothing — and any finding should first
be checked against these three exceptions.
