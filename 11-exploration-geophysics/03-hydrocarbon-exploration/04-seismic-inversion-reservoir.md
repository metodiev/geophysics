---
id: 11-03-04
title: "Seismic Inversion for Reservoir Properties"
level: research
prereqs: ["11-03-01", "11-03-03", "18-03-02", "20-04-02"]
tags: [exploration-geophysics, seismic-inversion, impedance, regularisation, uncertainty]
---

# Seismic Inversion for Reservoir Properties

**All models and data in this module are SYNTHETIC.** The layered model, the
wavelet, the noise level and the regularisation weights below are chosen
teaching values. No well, field or company is described, and no published
inversion result is reproduced.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write down** the convolutional forward model in terms of reflectivity and
   impedance, and **linearise** it as $r \approx \tfrac12 \mathrm{d}\ln Z$.
2. **Explain** why the seismic wavelet's band limits define a null space, so
   that absolute impedance is not recoverable from the trace alone.
3. **Compare** band-limited deconvolution with model-based inversion and
   **state** what each assumes.
4. **Set up** the Tikhonov objective $\lVert Wr-d\rVert^2 + \lambda\lVert Dr\rVert^2 +
   \mu\lVert m\rVert^2$ and **choose** $\lambda$ and $\mu$ against a stated
   criterion.
5. **Quantify** the fraction of impedance variance that lies outside the seismic
   band, and **compute** the error produced by a wrong low-frequency model.
6. **Demonstrate** that a sub-$\lambda/4$ bed is both underestimated in contrast
   and smeared in width, and **explain** why no processing removes it.
7. **Report** an impedance result with its background assumption and its error
   bar, and **compare** the noise-driven and model-driven contributions.

## Prerequisites

- [11-03-01 Reflection Seismic in Exploration](01-seismic-in-exploration.md) —
  resolution, sampling, and what a trace is.
- [11-03-03 Reservoir Characterisation and Property Prediction](03-reservoir-characterisation.md) —
  what the impedance is then mapped *to*.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md) —
  the general theory of the stabiliser used here.
- [20-04-02 Spiking (Predictive) Deconvolution](../../20-signal-processing/04-deconvolution-and-inverse-filtering/02-spiking-deconvolution.md) —
  the signal-processing view of the same operator.

## 1. What inversion is, and the three choices it makes

**Seismic inversion** estimates a subsurface property — usually acoustic
impedance — from seismic traces. It is not a decoding step that removes
processing: it is a **model**, and every inversion result is conditional on
three explicit choices:

1. a **wavelet** (amplitude, phase, and whether it varies laterally);
2. a **parameterisation** (impedance on a time grid, in layers, with a trend?);
3. a **regularisation** (how much roughness is admitted, and what the
   low-frequency answer is).

The demonstration's model is a 0.4 s trace at 1 ms sampling, a 30 Hz Ricker
(61 samples, 61 ms), a 6.00 MRayl background with 400 reflective samples
(coefficients from $-0.139$ to $+0.096$, impedance 3.33–8.22 MRayl), and 3%
random noise. Every number below comes from that configuration.

## 2. The forward model and its null space

With reflectivity $r$ and wavelet $w$, the trace is

$$d(t) = w(t) * r(t) + n(t), \qquad
W = \text{Toeplitz}(w) \quad\Longrightarrow\quad
\mathbf{d} = \mathbf{W}\mathbf{r} + \mathbf{n}.$$

For small contrasts the reflection coefficient at a sample boundary is

$$r_i = \frac{Z_{i+1}-Z_i}{Z_{i+1}+Z_i}
\approx \tfrac12\,\Delta \ln Z_i
\approx \tfrac12 \left(D\ln Z\right)_i,$$

so with $m = \ln Z$ and $D$ the first-difference operator,

$$\mathbf{d} \approx \tfrac12\,\mathbf{W}\mathbf{D}\,\mathbf{m} + \mathbf{n}
\equiv \mathbf{G}\mathbf{m} + \mathbf{n}.$$

The crucial structural fact is that $\mathbf{G}$ is a **band-limited operator**:
its singular values are proportional to $|W(f)|$, so any model component whose
frequency content lies where $|W(f)| \approx 0$ is in the **null space** and is
invisible to the data. Two consequences follow immediately, and they are the
heart of this lesson:

- the *high* frequencies the trace never carried are missing, which is the
  familiar resolution limit;
- the *low* frequencies are missing too, and they are where most of the
  impedance variance lives.

## 3. Route A: band-limited deconvolution

The classical route divides the spectra with a water level and integrates the
result:

$$\hat{r}(f) = \frac{D(f)\,W^*(f)}{|W(f)|^2 + \varepsilon\,|W|^2_{\max}},
\qquad \hat{Z}(t) = Z_0\exp\left(2\sum_{i\le t}\hat{r}_i\right).$$

With the demonstration's trace:

| water level | relative $r$ error | impedance error | corr($Z$) |
|---|---|---|---|
| $10^{-8}$ | 22.578 | 275.0% | 0.061 |
| $10^{-6}$ | 2.735 | 95.9% | 0.190 |
| $10^{-4}$ | 0.950 | 68.9% | −0.177 |
| $10^{-2}$ | 0.937 | 36.7% | 0.248 |

The pattern is diagnostic. A small water level is unstable (a $10^{-8}$ level
turns a few per cent of numerical noise into a 275% impedance error — the
division blowing up), and a large one is stable and useless (the reflectivity
error approaches 1.0, i.e. the estimate is essentially zero while the data are
still fit to within the noise). At no water level does the integrated impedance
resemble the truth, because the low-frequency part of the answer was never in
the data. **Band-limited deconvolution without a background model cannot produce
absolute impedance**, and the honest conclusion is not that the method is
badly tuned but that the information is absent.

## 4. Route B: model-based inversion with a low-frequency background

Write the log-impedance as a supplied background plus an unknown detail,

$$m = m_{\text{bg}} + \Delta m,$$

and minimise

$$\Phi(\Delta m) = \lVert \mathbf{G}\,\Delta m -
(\mathbf{d} - \mathbf{G}m_{\text{bg}})\rVert^2
+ \lambda\lVert \mathbf{D}\,\Delta m\rVert^2
+ \mu\lVert \Delta m\rVert^2 .$$

The normal equations are solved in closed form:

$$\left(\mathbf{G}^{\!\top}\mathbf{G} +
\lambda\,\mathbf{D}^{\!\top}\mathbf{D} + \mu\,\mathbf{I}\right)\Delta m
= \mathbf{G}^{\!\top}\left(\mathbf{d} - \mathbf{G}m_{\text{bg}}\right).$$

- $\lambda$ penalises **roughness** of the detail (a smoothness stabiliser);
- $\mu$ penalises the **magnitude** of the detail, i.e. it keeps the answer
  close to the supplied background — it is the mathematical form of "trust the
  low-frequency model".

The demonstration's scan, using the correct background (the true part of
$\ln Z$ below 5 Hz):

| $\lambda$ | $\mu$ | data residual | impedance error | corr($Z$) |
|---|---|---|---|---|
| $10^{-3}$ | $10^{-6}$ | 0.0279 | 4.82% | 0.9857 |
| $10^{-3}$ | $10^{-4}$ | 0.0287 | 4.34% | 0.9857 |
| $10^{-3}$ | $10^{-2}$ | 0.0607 | 9.48% | 0.9408 |
| $10^{-3}$ | $10^{-1}$ | 0.1493 | 10.56% | 0.9294 |
| $10^{-2}$ | $10^{-4}$ | 0.0297 | 4.34% | 0.9859 |
| $10^{-1}$ | $10^{-4}$ | 0.0378 | 5.11% | 0.9817 |

Best of the scan: $\lambda = 10^{-2}$, $\mu = 10^{-4}$, impedance error 4.3%,
correlation 0.986. Three observations:

1. **The method works when the background is right.** 4.3% on a model whose
   impedance varies by a factor of 2.5 is a good answer for a band-limited
   data set with 3% noise.
2. **Over-regularisation is visible in both columns.** At $\mu = 10^{-1}$ the
   data residual triples (the model can no longer fit the data) *and* the
   impedance error rises: the penalty is now confining the detail, not just
   stabilising it.
3. **In an $L$-curve sense the corner is broad.** Between $\lambda = 10^{-3}$
   and $10^{-1}$ at $\mu = 10^{-4}$ the error moves from 4.82% to 5.11%, so the
   answer is insensitive to $\lambda$ in that range — a common and reassuring
   outcome, and one that must be *checked* rather than assumed
   ([18-03-03](../../18-inverse-problems/03-regularization/03-parameter-choice.md)).

## 5. The low-frequency problem, quantified

The demonstration decomposes the true $\ln Z$ by frequency:

| band | share of variance of $\ln Z$ |
|---|---|
| below 5 Hz | **77.5%** |
| 10–50 Hz (where the wavelet has energy) | **7.3%** |

Read that twice. **Three quarters of the impedance variation lives in
frequencies the 30 Hz Ricker does not carry, and only 7% lives in the band it
does.** The inversion is not estimating impedance; it is estimating a 7%
perturbation and adding it to a background supplied by someone else.

The demonstration makes the cost concrete by re-running the inversion with four
backgrounds:

| background supplied | impedance error |
|---|---|
| the true low-frequency part below 5 Hz | **4.34%** |
| the true $Z_0$ as a constant | 27.66% |
| a constant 10% too high | 36.28% |
| a linear trend 0 to +15% | 38.35% |

A flat background costs an order of magnitude more accuracy than the right one;
a 10% error in the level costs 36%. Compare that with the noise-driven spread
measured in §7: **inversion uncertainty is dominated by the model, not by the
data.** A result quoted with a noise-based error bar alone is therefore
misleading, and the background's provenance — well logs, stacking velocities,
a regional trend — must be stated.

## 6. Resolution: what a thin bed becomes

Take a single bed: reflection coefficients $+0.10$ and $-0.10$ separated by
$h$ of two-way time, in a flat 6.0 MRayl background, giving a true impedance
contrast of 1.088 MRayl. Inverting each with the model-based scheme:

| bed thickness (ms) | recovered contrast (MRayl) | fraction of true | RMS anomaly width (ms) |
|---|---|---|---|
| 4.0 | 0.170 | 15.6% | 17.18 |
| 8.0 | 0.223 | 20.5% | 20.07 |
| 12.0 | 0.197 | 18.1% | 22.81 |
| 16.0 | 0.270 | 24.8% | 24.60 |
| 20.0 | 0.316 | 29.1% | 26.37 |
| 30.0 | 0.396 | 36.4% | 31.20 |
| 40.0 | 0.461 | 42.4% | 35.91 |
| 80.0 | 0.636 | 58.5% | 54.97 |

($\lambda/4$ is 25.0 m = 16.7 ms two-way here; the dominant period is 33.3 ms.)
Two systematic errors, and the second one is the dangerous one:

1. **The contrast is underestimated**, badly for thin beds (15.6% of the truth
   at 4 ms) and only slowly approaching the truth for thick ones (58.5% even at
   80 ms). The missing part is the sub-5 Hz content of a step, which a
   band-limited wavelet cannot supply.
2. **The anomaly is broadened.** A 4 ms bed is reported as a 17 ms anomaly. An
   interpreter measuring the width of the impedance low on a map is measuring
   the wavelet plus the regularisation, not the reservoir. This is the tuning
   problem of [11-03-02](02-seismic-stratigraphy.md) seen through the inversion,
   and the conclusion is the same: below $\lambda/4$, thickness must come from
   amplitude and the low-frequency model together, never from the inversion
   alone.

## 7. Uncertainty: two error bars, one of which matters

The demonstration runs 20 noise realisations and reports the spread of the
recovered impedance:

- mean relative standard deviation **0.67%**;
- mean relative bias **+0.09%**;
- worst-sample standard deviation 1.35%.

Set those against §5: the same inversion with a 10%-wrong background has a 36%
bias. The noise error bar is real, reproducible and an order of magnitude too
small to be the number a decision needs. The honest report is therefore:

> Impedance from a 30 Hz band with 3% noise, background from well logs;
> noise-driven uncertainty ±0.7%, systematic uncertainty from the background
> ±10% of the background level (a sensitivity run is shown).

That sentence is the deliverable. Everything else is a picture.

## 8. Worked examples

### Example 1 — why the null space is a null space

The wavelet is a 30 Hz Ricker, whose spectrum is negligible outside 10–50 Hz.
Consider two models that differ only by a 1 Hz sinusoid of amplitude 0.5% in
$\ln Z$. In the band 10–50 Hz their spectra differ by $|W(f)|\times 0.005$,
which for a Ricker of this length is below the 3% noise level in the trace.
Both models fit the data equally well; the inversion cannot prefer either. The
formal statement is that the model's projection onto the null space is
unconstrained, and the regularisation term ($\mu$, or the supplied background)
is what supplies an answer there. This is not a defect of a particular code —
it is the linear algebra of a band-limited operator.

### Example 2 — choosing $\lambda$ from the data residual

The noise level is known: 3% of the trace rms, i.e. a relative data residual of
about 0.03 for a well-fit model. From the table, $\lambda = 10^{-2}$ with
$\mu = 10^{-4}$ gives a residual of 0.0297 — just at the noise level, so the
model is fitting the data as well as the data deserve. The $\mu = 10^{-1}$ row
gives 0.1493, five times the noise: the inversion is now fitting the
regularisation, not the data. **Choose the smallest penalty that keeps the
residual at the noise level** (the discrepancy-principle version of the
parameter choice, [18-03-03](../../18-inverse-problems/03-regularization/03-parameter-choice.md)),
and check that the answer is not sensitive to it.

### Example 3 — the low-frequency model from a different measurement

Suppose stacking velocities give a smooth $v_p$ trend with a 2% error and the
density trend is assumed constant. The resulting $\ln Z$ background error is
of order 2–3%. From §5 the mapping from background error to answer error is
roughly one-to-one on the level term (36% error from a 10% level error), so the
expected impedance error is a few per cent — but it is a *bias*, not a random
error, and it will be correlated across the whole survey. That is why a
regional trend should be tied to at least one well in the area before any
impedance map is interpreted quantitatively.

## 9. Assumptions and regime of validity

1. **A known, stationary, zero-phase (or known-phase) wavelet.** An unknown
   phase is an unknown time shift and an unknown amplitude gradient; inversion
   without a wavelet estimate produces impedance with a systematic error
   ([11-03-06](06-borehole-and-integration.md)).
2. **Linearisation.** $r \approx \tfrac12 D\ln Z$ drops terms of order
   $r^2 \approx 10^{-2}$ for $r \approx 0.1$; for strong contrasts (evaporites,
   coals) an iterative or exact formulation is required.
3. **1-D convolutional model with primaries only.** Multiples, transmission
   loss and 3-D effects are handled upstream
   ([06-09-02](../../06-seismology/09-reflection-seismology/02-processing-flow.md)),
   and any residual error is absorbed into the model as a bias.
4. **Additive, white, Gaussian noise.** Coloured or coherent noise changes both
   the weighting and the achievable residual.
5. **A low-frequency model exists and is trustworthy in level.** This is the
   binding assumption of the entire method.
6. **The chosen regularisation matches the geology.** A first-difference
   stabiliser assumes a blocky earth; a second-difference stabiliser assumes
   smoothness; either can produce a plausible-looking wrong answer.
7. **The result is a bulk average over a resolution cell**, not a property of a
   point ([11-03-03 §7](03-reservoir-characterisation.md)).

## 10. Units and dimensional consistency

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| wavelet | $w$ | 1 | dimensionless amplitude scaling |
| reflectivity | $r$ | 1 | $(Z_2-Z_1)/(Z_2+Z_1)$ |
| log-impedance | $m = \ln Z$ | 1 (ln of MRayl) | differences are dimensionless |
| data residual | | 1 | $\lVert Wr-d\rVert/\lVert d\rVert$ |
| $\lambda$ | | 1 | scales a squared derivative against squared data |
| $\mu$ | | 1 | scales a squared model against squared data |

The objective function mixes a data misfit and two model penalties, so all
three terms must be dimensionless if the weights are to be compared. If your
residual is in metres and your penalty in seconds, $\lambda$ has units and its
"best value" is meaningless.

## 11. Python demonstration

`code/seismic_inversion_reservoir_demo.py` prints:

1. the synthetic model statistics and the noise level;
2. the band-limited route against water level, with reflectivity error and
   impedance error;
3. the model-based route against $\lambda$ and $\mu$, with the data residual,
   impedance error and correlation;
4. the variance decomposition of $\ln Z$ by band, and the error from four
   low-frequency backgrounds;
5. the thin-bed table (recovered contrast, fraction of true, RMS width);
6. the 20-realisation uncertainty: standard deviation and bias.

It is print-only, seeded with `np.random.default_rng(20261014)` and exits 0.

## 12. Exercises

- [`exercises/04-seismic-inversion-reservoir-exercises.md`](exercises/04-seismic-inversion-reservoir-exercises.md)
- [`exercises/04-seismic-inversion-reservoir-solutions.md`](exercises/04-seismic-inversion-reservoir-solutions.md)

## Mastery checkpoint

> A 0.4 s trace is inverted for impedance with a 30 Hz Ricker, 3% noise, and a
> background taken from a regional velocity trend. **(a)** State the null space
> of the forward operator in one sentence and explain why it includes the
> low frequencies. **(b)** You are told that 77.5% of the impedance variance
> lies below 5 Hz and that your background is 10% too high in level. Estimate
> the resulting impedance bias and compare it with the noise-driven ±0.7%.
> **(c)** A 6 ms thick bed is interpreted from the impedance low. State the two
> systematic errors you would expect and their approximate sizes.
> **(d)** Write the one-sentence uncertainty statement the report should carry.

## Common pitfalls

1. **Reporting an impedance without the background's provenance.** The number
   is the background plus a 7% perturbation.
2. **Tuning the water level or $\lambda$ to taste.** Choose it against a stated
   noise metric (residual ≈ noise) and show the sensitivity.
3. **Quoting only the noise-driven error bar.** It is an order of magnitude
   smaller than the model-driven one.
4. **Measuring bed thickness from the inversion.** Below $\lambda/4$ the
   anomaly is broader than the bed and its contrast is underestimated.
5. **Ignoring the wavelet phase.** A phase error biases impedance and looks
   like a time shift.
6. **Treating a smooth inversion as a measurement.** Smoothness is imposed by
   $\lambda$; the Earth's sharpness is not in the output.

## Related modules

- [18-03 Regularisation](../../18-inverse-problems/03-regularization/README.md) —
  the general theory of $\lambda$, the L-curve and the discrepancy principle.
- [18-07 Joint and Multi-Physics Inversion](../../18-inverse-problems/07-joint-and-multi-physics-inversion/README.md) —
  what changes when a second data set constrains the same model.
- [20-04 Deconvolution and Inverse Filtering](../../20-signal-processing/04-deconvolution-and-inverse-filtering/README.md) —
  the filter-design view of the same operator.
- [11-03-03 Reservoir Characterisation and Property Prediction](03-reservoir-characterisation.md) —
  what the impedance is mapped to.
- [11-03-06 Integrating Borehole Data with Seismic](06-borehole-and-integration.md) —
  where the wavelet and the background should come from.

## Further reading

- Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists. Level: reference. Recursive inversion, model-based inversion
  and wavelet estimation.
- Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press. Level: textbook. Amplitude, impedance and
  inversion in the exploration context.
- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press. Level: textbook. The
  seismic interpretation and modelling chapters.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.
