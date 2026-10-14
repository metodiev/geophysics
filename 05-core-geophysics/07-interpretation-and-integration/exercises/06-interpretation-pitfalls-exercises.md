# Exercises — 05-07-06 Common Interpretation Pitfalls and False Positives

Attempt these **closed-book** before opening the
[solutions](./06-interpretation-pitfalls-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/pitfalls_demo.py`](../code/pitfalls_demo.py) require you to run it and
report its actual output. **Every threshold answer must state the number of trials
it is conditioned on. No answer may report a "detection" without saying how many
models were searched.**

---

## ★ Foundational

**★1.** Compute the family-wise 3σ false-positive rate for:

(a) 100 stations;
(b) 400 stations;
(c) 10 000 stations.

State the per-station tail probability you use.

---

**★2.** A 2 mGal anomaly of half-width 300 m is found on a 500 m station grid.

(a) State the minimum station spacing required by the two-samples-per-half-width
rule.
(b) State what the 500 m grid can and cannot support.
(c) State whether the reported half-width is trustworthy.

---

**★3.** Give the per-station threshold that achieves a 1 per cent family-wise
false-positive rate over 500 stations, and over 10 000 stations.

---

## ★★ Applied

**★★4.** Run [`../code/pitfalls_demo.py`](../code/pitfalls_demo.py) Section 3.

(a) Report the four apparent depths.
(b) Plot or tabulate the apparent depth against spacing and describe the trend.
(c) Explain why the first two spacings give nearly correct answers while the last
gives a depth ten times too large.

---

**★★5.** Using the trend-removal table of the lesson:

(a) Compute the fractional change in recovered mass between successive polynomial
orders.
(b) State the order beyond which the answer stabilises, and why.
(c) Explain why the smallest residual corresponds to the largest mass error.

---

**★★6.** For a 2000-station survey and a search over 12 candidate depths:

(a) Compute the expected maximum of a noise-only statistic.
(b) Compute the per-station threshold that holds the family-wise rate at 5 per
cent, ignoring the search.
(c) Recompute it approximately, accounting for the search, and state which
correction dominates.

---

## ★★★ Research-oriented

**★★★7.** Equation (1) of the lesson assumes independent tests, which gridded data
violate.

(a) For a survey of area $A$ with noise autocorrelation length $\ell$, give the
effective number of independent cells.
(b) Recompute the 5 per cent family-wise threshold for $A = 100$ km²,
$\ell = 500$ m and $\ell = 2$ km.
(c) Discuss the sensitivity of the answer to $\ell$, and state the assumption you
had to make about the noise correlation structure.

---

**★★★8.** Design a processing-blind significance test.

(a) State the full interpretation chain to be applied to each noise realisation.
(b) Report the distribution of "detected bodies" (depths and masses) that noise
alone produces, for 1000 realisations.
(c) Use the distribution to set a threshold for the real survey, and state the
computational cost of the procedure.

---

## Reference list used in this problem set

- [05-07-06 lesson](../06-interpretation-pitfalls.md)
- [05-07-05 Reporting Geophysical Results with Honest Uncertainty](../05-reporting-results.md)
- [Solutions](./06-interpretation-pitfalls-solutions.md)
