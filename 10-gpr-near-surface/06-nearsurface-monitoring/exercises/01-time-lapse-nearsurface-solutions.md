# Solutions — 10-06-01 Time-Lapse Near-Surface Geophysics

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Teaching sensitivity $\mathrm dv/\mathrm dT = -0.5\
> \mathrm{m\,s^{-1}\,K^{-1}}$ at $v = 400\ \mathrm{m\,s^{-1}}$.

Lesson: [01 Time-Lapse Near-Surface Geophysics](../01-time-lapse-nearsurface.md).

---

## ★1 — Noise level from NRMS

$$\mathrm{NRMS} = \frac{\sqrt{2}\,\sigma}{S} \;\Longrightarrow\;
\frac{\sigma}{S} = \frac{0.030}{\sqrt{2}} = 2.12\%.$$

**Asymmetric repeats.** If repeat 1 has noise $\sigma_1$ and repeat 2 has
$\sigma_2 = 2\sigma_1$, then $a - b = \text{noise}_1 - \text{noise}_2$ has variance
$\sigma_1^2 + \sigma_2^2 = 5\sigma_1^2$, so

$$\mathrm{NRMS} = \frac{\sqrt{\sigma_1^2+\sigma_2^2}}{S}
= \frac{\sqrt{5}\,\sigma_1}{S} = 2.24\frac{\sigma_1}{S},$$

i.e. **the noisier repeat dominates** the repeatability (here $2.24$ instead of
$1.41$ times the quieter repeat's noise). This is why a monitoring design controls
the *worse* of the two epochs: improving an already-good epoch buys almost
nothing.

---

## ★2 — Resolution and the shift it must see

$$\sigma_\epsilon = \frac{\sigma_t}{t} = \frac{0.5}{40} = 1.25\%,$$
$$\delta t = \epsilon\,t = 0.004\times40 = 0.16\ \mathrm{ms}.$$

The $0.4\%$ change is $3.1$ times smaller than the pick: undetectable by picking
alone, and the shift it produces ($0.16\ \mathrm{ms}$) is a third of the pick — a
number worth quoting, because a *systematic* pick bias of $0.16\ \mathrm{ms}$ that
differs between epochs would masquerade as the target.

---

## ★3 — Difference, ratio, inversion

The **difference** $d_2 - d_1$ suits an additive observable such as an arrival
time; it removes a constant part and preserves sign. The **ratio** $d_2/d_1$ suits
a multiplicative observable such as an amplitude or a velocity, and it is
insensitive to a common scale factor — which is a strength for source-strength
variations and a danger for gain drift. The **4-D inversion** solves for a baseline
model and a change together, with a coupling norm, and is the correct treatment
when the baseline is itself uncertain; it is the only one of the three that can
report a change with an honest uncertainty derived from both epochs.

---

## ★★4 — Coda precision against coda length

Measured: $0.355\times10^{-4}$ at 1 s and $0.058\times10^{-4}$ at 4 s, so

$$\text{ratio} = \frac{0.355}{0.058} = 6.1,$$

against the $T^{3/2}$ prediction $4^{1.5} = 8.0$. The measured improvement is
therefore *smaller* than predicted by about 25%.

**Reasons.** (i) The prediction assumes the derivative energy grows as
$\omega^2T^3$ at *constant* $\omega$ and constant amplitude, whereas the synthetic
coda's high-frequency content decays with time (its envelope damps) and the shorter
coda has proportionally more of its energy in the well-determined early part.
(ii) The estimator resamples by linear interpolation, which acts as a low-pass
filter and costs more relative precision on the longer, more rapidly varying
coda. Both are reasons to *measure* the precision on a reference data set rather
than to quote the scaling law.

---

## ★★5 — Six-month temperature aliasing

$$\frac{\delta v}{v} = \frac{-0.5\times6}{400} = -0.0075 = -0.75\%.$$

A $0.3\%$ target change is **not measurable** without a correction: the alias is
$2.5$ times the target, and their sum would be reported as a change of
$0.45\%$–$1.05\%$ depending on sign — an error larger than the quantity sought.

**What the reference site must match.** Not the temperature, but the *sensitivity
to it*: the same $\mathrm dv/\mathrm dT$ over the same depth range, sampled by
paths with the same depth coverage. If the reference is a shallow path and the
target a deep one, the correction removes the shallow response and leaves the
deep one — so a reference should be chosen whose sensitivity vector is *parallel*
to the nuisance, and the residual error is the angle between them times the
nuisance amplitude, not the nuisance amplitude itself.

---

## ★★6 — Amplitude needed for rejection

$$\chi^2_{\text{unit}} = 497 \quad\text{and}\quad
\chi^2_{\text{needed}} = 5.99 = \epsilon^2\,\chi^2_{\text{unit}}
\;\Longrightarrow\;
\epsilon = \sqrt{\frac{5.99}{497}} = 0.110 = 11.0\%.$$

**Scaling with the picking error.** $\chi^2$ contains $(\delta d/\sigma_t)^2$, so
$\chi^2_{\text{unit}} \propto \sigma_t^{-2}$ and therefore

$$\epsilon_{\text{needed}} \propto \sigma_t .$$

Halving the picking error halves the change amplitude needed for a decisive
rejection: a $0.25\ \mathrm{ms}$ pick brings the requirement from $11.0\%$ to
$5.5\%$. **But** this scaling saturates: as $\sigma_t$ falls, the limiting term
becomes the systematic error (coupling, repositioning, and the environmental
alias of Section 3.5), which does not improve with better picking.

---

## ★★★7 — A four-path layout for an embankment (specification)

**Paths.** Four ray paths whose lengths in the target layer differ strongly from
their total lengths, i.e. one path that is almost entirely in the target, two that
cross it obliquely, and one that stays above it. Quantitatively, choose them so
that the correlation between the uniform-change and localised-change signatures
satisfies $|\rho| < 0.5$; that is a computable design criterion for a known
velocity model, and it is what "depth coverage" means in practice.

**Expected $\chi^2$ of the wrong hypothesis.** With $\sigma_t = 0.25\ \mathrm{ms}$
and four data, a two-parameter-free-amplitude hypothesis has 3 degrees of freedom,
so the 95% point is $\chi^2 = 7.81$ (not $5.99$). Compute
$\chi^2_{\text{unit}}$ from the model and the path geometry for a *unit* localised
change; then the detectable change follows from
$\epsilon = \sqrt{7.81/\chi^2_{\text{unit}}}$.

**Smallest detectable change.** With the scale from the lesson's mixed-depth set
($\chi^2_{\text{unit}} = 497$ at $\sigma_t = 0.5\ \mathrm{ms}$), scaling to
$\sigma_t = 0.25\ \mathrm{ms}$ gives $\chi^2_{\text{unit}} = 4\times497 = 1988$, so
$\epsilon = \sqrt{7.81/1988} = 6.3\%$ — better than the lesson's $11\%$ but still a
large change, and the improvement from a fourth path comes through
$\chi^2_{\text{unit}}$, not through the noise.

**Why four and not three.** With three data and one free amplitude there are two
degrees of freedom; the extra path buys both an extra degree of freedom and a
different sensitivity direction. The design criterion is not the number of paths
but the conditioning of the two signature vectors against the noise.

---

## ★★★8 — Testing an unsupported claim (specification)

**Measurement 1: a baseline repeat.** Measure the same geometry twice *now*, at the
same state, and compute NRMS. Falsification: if NRMS is comparable to the reported
change, the claim is unsupported. This test needs no history and can be run
immediately.

**Measurement 2: a temperature (and moisture) record.** Instrument the site with
temperature and moisture sensors at two or three depths spanning the sensitivity of
the measurement, and regress the reported changes on them. Falsification: if the
change correlates with the confounder with a slope consistent with the *independent*
estimate of the sensitivity, the claim is environmental. The word *independent*
matters: using the same data to estimate both the sensitivity and the correction is
circular.

**Measurement 3: a reference site.** Repeat the survey at a control site with the
same instrument, geometry and operator, where the target is known not to change.
Falsification: if the reference site shows a change of the same size, the change is
not a target change.

**Falsification test for all three.** If the anomalies survive all three — i.e.
NRMS is small, the confounder regression leaves the anomaly, and the reference site
is quiet — then the claim is supported *and* the residual uncertainty is the
combination of the three residuals, not the reported $2\%$. The claim as stated has
no error bar, and constructing one is part of the test.
