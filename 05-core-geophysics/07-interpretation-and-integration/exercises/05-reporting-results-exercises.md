# Exercises — 05-07-05 Reporting Geophysical Results with Honest Uncertainty

Attempt these **closed-book** before opening the
[solutions](./05-reporting-results-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/reporting_demo.py`](../code/reporting_demo.py) require you to run it and
report its actual output. **Every numerical answer must state its unit, its
uncertainty and the assumptions the uncertainty depends on. Any claim that cannot
be falsified by a stated observation is wrong.**

---

## ★ Foundational

**★1.** Write a one-sentence detectability statement for a compact body of
$5\times10^{9}$ kg at 300 m depth, at 0.02 mGal noise and a 3σ threshold. Include
all four required parts.

---

**★2.** Convert the statement "depth = 500 ± 10 m" into an honest one, given that
the model choice between a compact body and a 2-D body is worth 117 m.

---

**★3.** List the four metadata items a reader needs in order to reproduce a
Bouguer anomaly map, and state what goes wrong if each is omitted.

---

## ★★ Applied

**★★4.** Run [`../code/reporting_demo.py`](../code/reporting_demo.py).

(a) Report the depth percentiles and the two contributions to the depth
uncertainty.
(b) Re-run with the half-width measured to 10 per cent instead of 2 per cent.
(c) Find the measurement precision at which the two contributions become equal,
and state what that means for survey design.

---

**★★5.** Write the non-detection paragraph of the lesson's §3.4 for a survey with
0.05 mGal noise, a 4σ threshold and a target of 200 kg m⁻³ contrast at 500 m.
Assume the target is a compact body and state the assumed radius.

---

**★★6.** A report states: *"The gravity data confirm the seismic interpretation
of a 300 m deep basin."*

(a) Identify at least three problems with the sentence.
(b) Rewrite it using feasible-set language and the three-part structure of
detection, location and identification.

---

## ★★★ Research-oriented

**★★★7.** Build a full uncertainty budget for a depth estimate including:

- regional-removal order,
- profile half-length,
- station noise,
- shape family.

Compute each term by direct simulation (state the seeds and grid sizes), report
the shares of the total variance, and state which two terms a further field
campaign could reduce. Justify the reduction you claim with the mechanism.

---

**★★★8.** Review a published interpretation of your choice.

(a) State its model, its uncertainties, and its assumptions.
(b) Assess its falsifiability: what observation would contradict it?
(c) Name one independent dataset that would test it, and state precisely what
prediction that dataset would measure.
(d) List every claim you could not assess because the information was not given.

---

## Reference list used in this problem set

- [05-07-05 lesson](../05-reporting-results.md)
- [05-07-06 Common Interpretation Pitfalls and False Positives](../06-interpretation-pitfalls.md)
- [Solutions](./05-reporting-results-solutions.md)
