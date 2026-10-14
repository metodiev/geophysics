# Solutions — 02-01-02 Measurement Uncertainty, Significant Figures and Error Bars

> **Read this after attempting the exercises, not before.**
>
> Every number below was computed, not estimated. Where an answer depends on a
> convention (coverage factor, distribution for a type B term), the convention
> is stated in the solution.

---

## ★1 — Defensible reporting

| | Raw | Defensible | Reasoning |
|---|---|---|---|
| (a) | $2.04371 \pm 0.0123$ | $2.044 \pm 0.012$ | uncertainty to two significant figures; value to the same decimal place |
| (b) | $979\,812.37 \pm 41$ | $(979\,812 \pm 41)$ | the tens digit is the first *uncertain* digit; the 0.37 is noise |
| (c) | $5.123456 \pm 0.0004$ | $5.1235 \pm 0.0004$ | the third decimal is the last certain one |
| (d) | $1.000000 \pm 0.3$ | $1.0 \pm 0.3$ | a 30% uncertainty does not support four digits |

**Note on (b).** $979\,812 \pm 41$ mGal would be equally acceptable;
$9.798 \times 10^{5} \pm 4 \times 10^{1}$ mGal is the unambiguous form if the
value might be confused with a different precision.

---

## ★2 — Resolution versus uncertainty

**(a)** Resolution $= 0.01$ mGal (the display step). The uncertainty of one
reading is estimated by the observed scatter, $s = 0.046$ mGal.

**(b)** Single reading: $u = 0.046$ mGal — report as $(x \pm 0.05)$ mGal.
Mean of 20: $u = s/\sqrt{n} = 0.046/\sqrt{20} = 0.0103$ mGal — report as
$(\bar{x} \pm 0.01)$ mGal.

**(c)** The ratio is $0.046/0.01 = 4.6$: the scatter exceeds the resolution
because it contains effects the display step does not describe (a small
gravimeter drift, microseism, imperfect levelling, reading rounding and real
short-period environmental variation). Resolution is a *floor* on the
uncertainty, not an estimate of it: even for pure quantisation the standard
uncertainty would be $\text{step}/\sqrt{12} = 0.0029$ mGal, and here the physics
adds a further factor of 16.

**Coverage.** All values above are standard uncertainties ($k = 1$).

---

## ★3 — Mean, scatter and standard error

Data (in $10^{-6}\ \mathrm{m\,s^{-2}}$):
$9.794, 9.801, 9.789, 9.797, 9.803, 9.792$; $\bar{x} = 9.796$.

**(a)** $\bar{x} = 9.796 \times 10^{-6}\ \mathrm{m\,s^{-2}}$.

**(b)** $\displaystyle s = \sqrt{\frac{\sum(x_i-\bar{x})^{2}}{n-1}}$.
The deviations are $-0.002, +0.005, -0.007, +0.001, +0.007, -0.004$, whose
squares sum to $1.44\times10^{-4}$, so

$$s = \sqrt{\frac{1.44\times10^{-4}}{5}} = 5.367\times10^{-3}.$$

**(c)** $\mathrm{sem} = s/\sqrt{6} = 5.367\times10^{-3}/2.449
= 2.191\times10^{-3}$.

**(d)** $(9.796 \pm 0.002) \times 10^{-6}\ \mathrm{m\,s^{-2}}$ for the mean
($k=1$); $(9.796 \pm 0.005)\times10^{-6}$ for a single reading.

**Comment the exercise is designed to produce.** The standard error is smaller
than the scatter by $\sqrt{6} = 2.45$; reporting the scatter as the uncertainty
of the mean overstates the error by that factor. This is the most common
over-reporting error in student work.

---

## ★4 — Uncertainties through a ratio

$$q = \frac{k\Delta T}{\Delta z} = \frac{2.5\times13.5}{0.30}
= 112.5\ \mathrm{W\,m^{-2}}.$$

Relative contributions (the exponent rule, all powers $+1$ here):

| Input | Value | Relative uncertainty |
|---|---|---|
| $k$ | $2.5 \pm 0.125$ | 5.0% |
| $\Delta T$ | $13.5 \pm 0.27$ | 2.0% |
| $\Delta z$ | $0.30 \pm 0.003$ | 1.0% |
| combined | | $\sqrt{25+4+1} = 5.477$% |

$u(q) = 112.5 \times 0.054\,77 = 6.162\ \mathrm{W\,m^{-2}}$, i.e.

$$q = (112 \pm 6)\ \mathrm{W\,m^{-2}}\ (k=1).$$

**Dominant term: the conductivity**, contributing $25/30 = 83\%$ of the
variance. This is the standard situation in heat-flow work: the effort belongs
in the conductivity measurement, not in the temperature difference.

---

## ★★5 — Combining four contributions

**(a)** $u_{\text{tot}} = \sqrt{0.03^{2}+0.04^{2}+0.02^{2}+0.01^{2}}
= \sqrt{3.0\times10^{-3}} = 0.054\,77$ mGal.

**(b)** Variance shares: $0.0009, 0.0016, 0.0004, 0.0001$ out of $0.0030$:
**30.0%, 53.3%, 13.3%, 3.3%**.

**(c)** Halving each in turn:

| Halved term | New total | Reduction |
|---|---|---|
| 0.03 → 0.015 | 0.04822 | 12.0% |
| 0.04 → 0.020 | 0.04243 | 22.5% |
| 0.02 → 0.010 | 0.05196 | 5.1% |
| 0.01 → 0.005 | 0.05408 | 1.3% |

The largest term gives the largest reduction, but note that halving it buys
only 22.5%: with four comparable contributions the total is dominated by none of
them, which is the practical definition of "well designed". A poorly designed
budget has one term at 90% of the variance; there, halving it is transformative.

---

## ★★6 — Weighted mean and consistency

**(a)**
$$\hat{x} = \frac{\sum x_i/u_i^{2}}{\sum 1/u_i^{2}}, \qquad
u(\hat{x}) = \left(\sum 1/u_i^{2}\right)^{-1/2}.$$
$\sum 1/u_i^{2} = 277.8 + 625 + 100 + 1111.1 = 2113.9$, so
$u(\hat{x}) = 1/\sqrt{2113.9} = 0.021\,750$.

$\sum x_i/u_i^{2} = 583.3 + 1262.5 + 215 + 2266.7 = 4327.5$, so
$\hat{x} = 4327.5/2113.9 = 2.0472$ mGal. Report
$(\mathbf{2.047 \pm 0.022})\ \mathbf{mGal}$ at $k=1$.

**(b)**
$$\chi^{2} = \sum_i\frac{(x_i-\hat{x})^{2}}{u_i^{2}} = 2.3512,\quad \nu = 3,\quad
\chi^{2}/\nu = 0.784.$$

**(c)** The unweighted mean is 2.0775 mGal, 30% larger than the weighted mean;
the difference is $0.030/0.022 = 1.4\sigma$, so the two are consistent but the
weighted mean is the better estimator (it is the minimum-variance one, §3.4).

$\chi^{2}/\nu = 0.78 < 1$ means the quoted uncertainties slightly *overstate* the
scatter: the measurements are more consistent than the error bars claim. With
only 3 degrees of freedom this is not significant, but it is worth saying out
loud rather than reporting $\chi^{2}$ silently. A $\chi^{2}/\nu$ of 5 or 10 would
demand a physical explanation (underestimated errors, or a real inconsistency,
e.g. the four values are not measuring the same thing).

---

## ★★7 — Excess mass from an anomaly

**(a)**
$$M = \frac{g_z d^{2}}{G} = \frac{(5.00\times10^{-6})(250)^{2}}{6.674\,30\times10^{-11}}
= 4.6821\times10^{9}\ \mathrm{kg}.$$

**(b)** Relative contributions:

| Input | Relative uncertainty | In the formula |
|---|---|---|
| $g_z$ | 1.0% | exponent 1 |
| $d$ | 1.0% | exponent 2 → **2.0%** |
| $G$ | $2.2\times10^{-5}$ | exponent 1 |

**(c)** Combined:
$$\sqrt{(10^{-2})^{2} + (2\times10^{-2})^{2} + (2.2\times10^{-5})^{2}}
= 2.236\times10^{-2}.$$
So $u(M) = 4.6821\times10^{9}\times0.022\,36 = 1.047\times10^{8}$ kg, and the
defensible report is
$$M = (4.68 \pm 0.10)\times10^{9}\ \mathrm{kg}\quad (k=1).$$
$G$ contributes $9.7\times10^{-7}$ of the variance — entirely negligible.

**(d)** The Earth's mass is obtained as $M_\oplus = GM_\oplus/G$, where
$GM_\oplus$ is *defining* and exact to all quoted digits; then $G$ is the **only**
source of uncertainty, and at $2.2\times10^{-5}$ it limits the mass to about
$1/(2.2\times10^{-5}) \approx 45\,000$ parts, i.e. 5 significant figures. In the
present problem the mass is derived from a *measured* anomaly whose relative
uncertainty is $10^{-2}$, four orders of magnitude worse than $G$; $G$ therefore
disappears into the noise. The rule is not "G always matters" but "the largest
relative uncertainty dominates, and a smaller one is irrelevant".

---

## ★★8 — A type B specification

The half-width is
$$a = 0.005 \times 120.000 + 3\times0.001 = 0.600 + 0.003 = 0.603\ \mathrm{mGal}.$$

Treating the specification as a rectangular bound (nothing known within it):

$$u = \frac{a}{\sqrt{3}} = \frac{0.603}{1.732} = 0.348\ \mathrm{mGal}.$$

If instead the two terms are treated as independent rectangular contributions,
$u = \sqrt{(0.600/\sqrt{3})^{2} + (0.003/\sqrt{3})^{2}} = 0.346$ mGal — a 0.5%
difference, so the more careful treatment changes nothing material.

**Why type B.** No repeated observations were made; the number comes from the
manufacturer's document. Its *evaluation* is type B, but its *arithmetic* is
identical to a type A term inside the quadrature sum. The rectangular assumption
is a choice: a triangular or normal interpretation would give
$a/\sqrt{6} = 0.246$ or $a/2 = 0.302$ mGal. This factor-of-1.4 spread is why the
distributional assumption must be stated — and why a budget built from several
rectangular assumptions tends to be conservative.

---

## ★★★9 — Designing for a factor of 4

**(a)** Current total:
$u = \sqrt{0.040^{2} + 0.030^{2}} = \sqrt{0.0016+0.0009} = 0.050$ mGal
(0.040 random, 0.030 systematic). The target is $0.050/4 = 0.0125$ mGal.

Repetition reduces only the random term, as $1/\sqrt{n}$. With $n$ measurements
the random term becomes $0.040/\sqrt{n}$, so

$$u(n) = \sqrt{\frac{0.0016}{n} + 0.0009} \xrightarrow[n\to\infty]{} 0.030\ \mathrm{mGal}.$$

**The limit is 0.030 mGal — 2.4 times the target. No number of repetitions can
reach 0.0125 mGal.** Even to reach 0.031 mGal (still above the systematic floor)
requires $n \ge 27$; to reach 0.0301 mGal requires $n \ge 267$.

**(b)** The systematic term must be attacked directly:

- calibration against a reference station, or a better-accuracy instrument;
- a model of the systematic effect (drift, tide, lat/latitude) whose residual is
  smaller than 0.0125 mGal.

Achievable target values, for instance: systematic 0.010 mGal (a threefold
improvement in calibration via a reference station) and random 0.0074 mGal
(from 29 repeats, since $0.040/\sqrt{29} = 0.00743$). Then
$\sqrt{0.00743^{2}+0.010^{2}} = 0.0125$ mGal — exactly the goal.

**(c)** Budget with shares:

| Term | Value (mGal) | Share of variance |
|---|---|---|
| random, mean of 29 | 0.0074 | 35% |
| calibration (systematic) | 0.0100 | 64% |
| **total** | **0.0125** | 100% |

Note the design rule this produces: **do not chase a term that cannot bring the
total below the target.** Any random budget better than 0.0074 mGal is wasted until
the systematic term is reduced again.

---

## ★★★10 — A ratio of normals

**(a)** With $y = N/D$, $\partial y/\partial N = 1/D = 1$, $\partial y/\partial D
= -N/D^{2} = -1$, so the relative uncertainty is
$$\frac{u(y)}{y} = \sqrt{\left(\frac{u_N}{N}\right)^{2}
+ \left(\frac{u_D}{D}\right)^{2}} = \sqrt{0.5^{2}+0.5^{2}} = 0.7071.$$
The first-order answer is $y = 1.0 \pm 0.71$.

**(b)** The exact distribution of a ratio of independent normals is a
*heavy-tailed* distribution (a Cauchy-like ratio density). When the denominator's
support includes zero — here $\mu_D = 0.5$ and $\sigma_D = 0.5$, so zero is
exactly 1σ away — the integrals defining the mean and variance diverge. Neither
$\mathbb{E}[y]$ nor $\mathrm{Var}(y)$ exists, so no standard uncertainty can be
assigned in the ordinary sense. The quadrature rule has produced a number, but
that number is not a standard deviation of anything.

**(c)** **Experiment:** draw $n$ pairs $(N_i,D_i)$ for
$n = 10^{4},10^{5},10^{6}$; compute $y_i$; report the **median** and the 16th and
84th percentiles (the quantile analogue of ±1σ), and *also* the sample standard
deviation. **Expectation:** the sample standard deviation grows without bound as
$n$ increases (it is dominated by the rare $D_i \approx 0$ events), while the
central 68% interval barely moves. The measured behaviour in the lesson's
demonstration is a median near 0.96 with $q_{16} \approx 0.41$ and
$q_{84} \approx 2.04$ that are stable across three decades of $n$, against a
sample standard deviation rising 68 → 125 → 197. The interval is asymmetric
about the median (0.55 below, 1.08 above), which is itself a signature of the
non-Gaussianity.

**(d)** Report the **median and quantiles**, state the assumed input
distributions, and say explicitly that the estimator has heavy tails so no
standard uncertainty is quoted. If a standard-uncertainty-style summary is
required by a downstream convention, say that it is not a stable quantity for
this estimator and give the quantiles instead. When the physical situation
permits a denominator bounded away from zero, state the bound — that is the
substantive fix, not a better summary statistic.

---

## Self-assessment: have you actually learned this?

- [ ] I can rewrite any result in defensible form without hesitating about the
      digits.
- [ ] I can distinguish the resolution, the scatter and the standard error of the
      mean, and say which one a report needs.
- [ ] I can compute a standard error of the mean and explain the $n-1$
      denominator.
- [ ] I can assemble a budget, compute variance shares, and identify the term
      that limits the design.
- [ ] I can recognise when the quadrature rule has stepped outside its regime and
      switch to quantiles.
- [ ] I can tell a type A from a type B uncertainty and state the distributional
      assumption I used.
