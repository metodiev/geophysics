# Solutions — 24-02-06 Figures, Captions and the Self-Contained Visual Argument

> Read after attempting. Numbers computed. Lesson:
> [06 Figures and Captions](../06-figures-and-captions.md).

---

## ★1 — Completeness of a partial caption

Three of the four elements are present:

$$\text{completeness} = \frac{3}{4} = 0.750,$$

which is above the corpus mean of $0.698$. The figure fails the separated-figure
test: interpretability requires **all four** elements, so a missing sample size means
a reader cannot judge whether the plotted statistic is stable or what it is
computed over. The demonstration's weakest element is exactly this one, present in
$50.0\%$ of captions, and fixing it alone would raise the standalone rate from
$22.1\%$ to $45.0\%$.

---

## ★2 — Data-ink ratio

$$\text{ratio} = \frac{0.40}{1.10} = 0.364 .$$

This is below both the demonstration's bar chart ($0.62$) and dot plot ($0.82$),
and it is in the range of the pie chart ($0.29$) — meaning that about two thirds of
the drawn ink encodes nothing. The listed corrective steps are to delete the frame,
remove gridlines that repeat the axis labels, drop any shadow or 3-D effect, and
check whether the same data can be shown as points. None of these changes the data;
all of them change the ratio.

---

## ★3 — Four series in colour only

In greyscale, colour-only encoding leaves the number of distinguishable series
equal to the number of distinct luminance levels, which for four series of similar
lightness is $1$ — the series merge. The remedy is **redundant encoding**: colour
*and* line style (solid, dashed, dotted, dash-dot) or marker shape (circle, square,
triangle, diamond), plus direct labelling of the series on the plot instead of a
legend. The demonstration's corpus shows the size of the problem: $62.9\%$ of
figures survive greyscale and $56.7\%$ use a colour-blind-safe palette, with
$63.7\%$ failing at least one of the two.

---

## ★4 — Standalone rate: independence prediction versus measurement

$$0.888 \times 0.675 \times 0.729 \times 0.500 = 0.2185 \approx 21.9\%.$$

The measured rate is $22.1\%$, essentially identical. Unlike the reporting audit in
[24-01-03 Critiquing Methods, Data and Inference](../../01-reading-research-literature/03-critiquing-methods.md),
where correlated omissions pushed the joint rate below the product, here the
elements behave nearly independently: caption completeness in this generator is
close to a set of independent coin flips. The lesson is that the independence
assumption is neither always wrong nor always right — it is a hypothesis to check
with a measurement, and it takes one line of arithmetic to check.

---

## ★5 — Colour-scale resolution

$$\text{distinct fraction} = \frac{6}{12} = 50.0\%.$$

To make every level distinguishable, remove

$$12 - 6 = 6\ \text{levels},$$

leaving a $6$-level scale. The alternative is to keep $12$ levels and accept that
adjacent steps encode nothing — which is defensible only if the reader never needs
to distinguish neighbours, for example when the quantity is read against a colour
bar with printed values. Choose one of these deliberately; the failure mode is a
scale whose designers believed it had resolution it does not have.

---

## ★6 — Pie charts to dot plots

Total ink before:

$$5 \times 1.20 = 6.00\ \text{units}; \qquad
\text{data ink} = 5 \times 0.35 = 1.75, \qquad \text{ratio} = 0.292 .$$

Total ink after:

$$5 \times 0.55 = 2.75\ \text{units}; \qquad
\text{data ink} = 5 \times 0.45 = 2.25, \qquad \text{ratio} = 0.818 .$$

Saving:

$$6.00 - 2.75 = 3.25\ \text{units}, \qquad \frac{3.25}{6.00} = 54.2\%.$$

The ink falls by $54.2\%$ while the data ink **rises** from $1.75$ to $2.25$ units.
That is the whole point of the data-ink ratio: the edit is not a reduction in
information, it is a change in what the ink is spent on. The pie-chart values are
chosen teaching values, not measurements, so quote the direction and the mechanism,
not the exact percentages.

---

## ★7 — Does the comparison sentence help?

**Design.** Between-subject, three arms on the same figure: (a) caption with the
four sentences including the comparison sentence; (b) the same caption without the
comparison sentence; (c) the comparison sentence only, no caption context. Arm (c)
separates "more text" from "the right text".

**Outcome.** A $100$-point index: state what is plotted, state the units, state what
the comparison shows, and rate confidence in the answer. Pre-register the rubric;
two blinded raters; report their agreement.

**Sample size.** Between-subject at $\alpha = 0.05$, $80\%$ power, difference $15$
points, standard deviation $23$ points:

$$n \text{ per arm} = \frac{2(1.96 + 0.842)^{2}\times 23^{2}}{15^{2}}
= \frac{2\times 7.851\times 529}{225} = 36.9 \approx 37,$$

so $111$ participants across three arms, plus $15\%$ for exclusions: $128$.

**Blinding.** Participants see only the figure and caption, with the journal, authors
and paper title removed. Raters score anonymised responses with the arm order
shuffled. The figure itself is identical in all arms, so the only difference is the
caption text — which is what makes the result interpretable.

---

## ★8 — Accessibility audit of a journal volume

**Sampling.** All figures in all research articles of one stated volume, or a formal
random sample if the volume is large; record the frame, the number of articles and
the number of figures, and report multi-panel figures as one unit with a panel
count, since per-panel coding multiplies the work without changing the conclusion.

**Coding protocol.** Per figure, four binary codes: (1) any series distinguished by
colour alone; (2) palette recognisable as colour-blind-safe from a stated list of
criteria (distinct lightness as well as hue; avoid red–green opposition); (3) the
encoding survives conversion to greyscale (check by desaturating the image or by
comparing luminance values); (4) direct labels or a legend, and whether the legend
is inside the plotting area. Each code gets a definition and two worked examples.

**Agreement.** Two coders on a $10\%$ pilot, Cohen's $\kappa$ per code, target
$\kappa \geq 0.7$ for the binary codes. Codes below target are rewritten, not
averaged; the greyscale code in particular is objective and should reach high
agreement once the luminance rule is written down.

**Metric for the editor.** The headline is the fraction of figures with at least one
colour-only dependence,

$$f = \frac{\text{figures with code (1) true}}{\text{figures coded}},$$

reported with a Wilson interval, together with the fraction that fails the greyscale
test and the per-journal breakdown. The action the journal can take is concrete —
require redundant encoding in the author guidelines and check it at copy-editing —
which is why the audit reports a rate per journal rather than a global verdict.
