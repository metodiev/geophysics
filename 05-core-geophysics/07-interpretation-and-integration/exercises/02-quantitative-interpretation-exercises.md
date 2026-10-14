# Exercises — 05-07-02 Quantitative Interpretation and Depth Estimation

Attempt these **closed-book** before opening the
[solutions](./02-quantitative-interpretation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/quant_interp_demo.py`](../code/quant_interp_demo.py) require you to run
it and report its actual output. **Every depth must be reported with both its
statistical error and its model spread, or with an explicit statement that one of
them is not quantified.**

Constants: $G = 6.674\times10^{-11}$ m³ kg⁻¹ s⁻²;
$1\ \mathrm{mGal} = 10^{-5}$ m s⁻².

---

## ★ Foundational

**★1.** For a point mass at a known horizontal position, the model is
$\mathcal{F}(x) = GMz/\left((x-x_0)^2+z^2\right)^{3/2} + a + bx$.

(a) Identify which parameters enter linearly and which non-linearly.
(b) Write the Jacobian $\partial \mathcal{F}/\partial z$ at $x = x_0$.
(c) Explain why the linear parameters can be eliminated for a given $(x_0, z)$.

---

**★2.** For the point mass, the peak is $GM/z^2$ and the curvature at the peak is
$-3GM/z^4$.

(a) Show the ratio of curvature to peak is $-3/z^2$.
(b) Explain why this makes the depth weakly determined relative to the mass.
(c) State what changes if the profile is only two source depths long.

---

**★3.** A spectral depth fit is performed with $k$ in cycles per metre and returns
a slope of $-5\times10^{-4}$ cycles⁻¹.

(a) Convert to a depth in metres.
(b) Compute the depth that results if the $2\pi$ is omitted.
(c) State the general rule for avoiding this error.

---

## ★★ Applied

**★★4.** Using the demonstration's model, add a linear regional of
0.30 mGal + $1.0\times10^{-4}$ mGal m⁻¹ $x$ and fit with a constant only, for
profile half-lengths of 2.5 km, 5 km and 10 km.

(a) Report the recovered depth and the percentage error for each.
(b) Explain the trend with profile length.
(c) State the diagnostic that would have revealed the problem without knowing the
answer.

---

**★★5.** Run the demonstration's second section.

(a) Report both recovered depths, both statistical errors, and both RMS residuals.
(b) Compute the ratio of the model spread to the statistical error.
(c) Write the two-sentence version of the result suitable for a report.

---

**★★6.** The spectral bias for a 3-D source is measured as $-9.70$ per cent at
6 km aperture and $-9.25$ per cent at 30 km, over the band $kz \in [2, 8]$.

(a) Explain why the bias does not shrink with a longer profile.
(b) Predict the bias over $kz \in [8, 20]$ and test your prediction numerically.
(c) State whether the estimator is usable for 3-D sources and under what
condition.

---

## ★★★ Research-oriented

**★★★7.** The lesson derives Euler's equation (7) from homogeneity.

(a) Implement it for the synthetic point-mass profile, using analytic
$\partial g/\partial z$.
(b) Scan $N$ over $\{0.5, 1, 1.5, 2, 2.5, 3\}$ and report the scatter of the
recovered depths for each.
(c) Explain why the scatter decreases with $N$ and why that makes $N$ an
identification rather than a measurement.

---

**★★★8.** Build a two-body model: a compact body at 300 m and a deeper body at
1200 m on the same axis, with 601 stations over $\pm3$ km and 0.02 mGal noise.

(a) Fit a single body and report the recovered depth and mass as a function of the
mass ratio $m_{\text{deep}}/m_{\text{shallow}} \in \{0, 0.1, 0.5, 1, 2\}$.
(b) Report the ratio below which the recovered depth is within 5 per cent of the
truth.
(c) State what an independent dataset at a *different* depth sensitivity would
have to measure to break the ambiguity, and why.

---

## Reference list used in this problem set

- [05-07-02 lesson](../02-quantitative-interpretation.md)
- [05-07-01 Qualitative Interpretation](../01-qualitative-interpretation.md)
- [Solutions](./02-quantitative-interpretation-solutions.md)
