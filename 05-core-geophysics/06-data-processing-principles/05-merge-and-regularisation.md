---
id: 05-06-05
title: "Gridding, Merging and Levelling of Survey Data"
level: advanced
prereqs: ["05-06-01", "01-10-08"]
tags: [gridding, interpolation, kriging, continuation, rtp, derivatives, levelling]
---

# Gridding, Merging and Levelling of Survey Data

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why gridding is interpolation and therefore the invention of data you
   did not measure, and quantify the invention by comparing interpolators.
2. **Derive** the upward- and downward-continuation transfer functions from Laplace's
   equation, and state why one is stable and the other is not.
3. **Measure** the noise gain of downward continuation and of the $n$-th derivative,
   and use the derived forms $e^{|k|\Delta z}$ and $|k|^{n}$ to design a processing
   step.
4. **Derive** the noise gain $k_N^{n}/\sqrt{2n+1}$ of an $n$-th-order derivative on a
   grid, and check it against a measurement.
5. **Reduce a field to the pole**, state the assumptions, and quantify the error
   produced by a wrong assumed direction.
6. **Level and merge** surveys from different epochs or platforms, and state which
   long-wavelength information the levelling removes.

## Prerequisites

- [05-06-01 The Processing Pipeline](./01-processing-pipeline-concept.md) — why
  gridding is the last stage.
- [01-10-08 Power Spectra, Admittance and Coherence of Geophysical Fields](../../01-mathematics/10-fourier-analysis/08-spatial-spectra.md)
  — reading a spatial spectrum, which is how the operators below are chosen.
- [02-08-02 Laplace's Equation and Harmonic Functions](../../02-physics/08-potential-theory/02-laplace-equation.md)
  — the property that makes continuation possible at all.

## 1. Intuition: three operations, one warning

This lesson covers the three operations that turn measured samples into a map and
then into a derived product:

- **gridding** — placing irregular samples on a regular grid;
- **continuation** — moving a measured field to a different height;
- **differentiation** (and its cousin, reduction to the pole) — computing derived
  fields whose interpretation is easier.

All three are linear operations on a band-limited signal, and all three have a
transfer function that grows with wavenumber:

| operation | transfer function | behaviour at high $k$ |
|---|---|---|
| gridding (any interpolant) | not a filter at all; it is a fitting rule | imposes the interpolant's own spectrum |
| upward continuation by $\Delta z$ | $e^{-|k|\Delta z}$ | decays: **stable** |
| downward continuation by $\Delta z$ | $e^{+|k|\Delta z}$ | grows: **unstable** |
| $n$-th vertical derivative | $|k|^{n}$ | grows: **unstable** |
| reduction to the pole | $\Theta^{-1}(k,\theta)$ | grows along some directions |

The single warning of the lesson: **the operations that make a map prettier and
easier to interpret are exactly the operations that amplify noise**, and each one
must therefore be paired with a band limit whose value is stated and justified.

## 2. Gridding: interpolation is invention

### 2.1 The measured comparison

[`code/gridding_demo.py`](./code/gridding_demo.py) evaluates an analytic two-body
gravity field on a fine 201 × 201 grid at 20 m spacing (the "truth"), samples it on a
21 × 21 grid at 200 m spacing, and asks seven interpolators to rebuild the fine grid.
The bodies are deliberately placed *off* the coarse grid nodes, so the anomaly peak
falls between samples:

| method | RMS error (mGal) | peak (mGal) | peak error (%) |
|---|---|---|---|
| nearest | 0.00897 | 0.33337 | −4.22 |
| linear | 0.00262 | 0.33337 | −4.22 |
| cubic | 0.00065 | 0.34417 | −1.12 |
| inverse distance, $p = 2$ | 0.01917 | 0.33337 | −4.22 |
| inverse distance, $p = 4$ | 0.00531 | 0.33337 | −4.22 |
| thin-plate RBF | 0.00054 | 0.33895 | −2.62 |
| multiquadric RBF | 0.00031 | 0.34341 | −1.34 |

(True peak 0.34807 mGal.) Two measurements matter here:

- **The anomaly peak moves differently for different interpolators.** The spread
  between the best and worst peak is

  | quantity | value |
  |---|---|
  | minimum peak over methods | 0.33337 mGal |
  | maximum peak over methods | 0.34417 mGal |
  | spread | 0.01081 mGal = **3.1 % of the true peak** |

  Three per cent of a peak amplitude is comparable to the differences that
  interpretation treats as real. **The choice of interpolator is part of the
  interpretation, and it belongs in the report.**
- **The RMS error and the peak error rank the methods differently.** Nearest and
  inverse-distance-weighting have similar peak errors (−4.22 %) but RMS errors
  differing by a factor two (0.00897 vs 0.01917), because IDW produces a smoother
  surface everywhere except at the peak. Reporting only one of the two numbers hides
  a real difference.

### 2.2 Undersampling: the error is not the interpolator's fault

The same linear interpolator at four grid spacings:

| spacing (m) | samples | RMS error (mGal) | peak (mGal) | peak error (%) |
|---|---|---|---|---|
| 1000 | 25 | 0.02860 | 0.18676 | −46.34 |
| 500 | 81 | 0.01505 | 0.21603 | −37.93 |
| 250 | 289 | 0.00424 | 0.31497 | −9.51 |
| 100 | 1681 | 0.00073 | 0.33471 | −3.84 |

At 1000 m spacing the recovered peak is **46 % low**. No interpolator recovers it,
because a linear interpolant can never exceed the maximum of its samples — the peak
information was simply not acquired. This is the same statement as
[05-05-03](../05-survey-design-and-acquisition/03-spatial-sampling-theory.md), now
with numbers: **gridding cannot fix undersampling.**

### 2.3 Interpolation is not filtering

With noisy samples ($\sigma = 0.005$ mGal on the 41 × 41 grid), the interpolators that
reproduce the samples exactly also reproduce the noise:

| method | RMS vs truth | RMS of the error at the samples |
|---|---|---|
| linear | 0.00416 | 0.00480 |
| cubic | 0.00405 | 0.00480 |
| multiquadric RBF | 0.00420 | 0.00480 |

The third column is the input noise's own standard deviation (0.00480 for this
realisation, against an input $\sigma = 0.005$): an exact interpolant passes the noise
straight through. **A smooth-looking grid is not evidence that the data are smooth.**

### 2.4 What the methods assume

| family | assumption | failure mode |
|---|---|---|
| nearest neighbour | the field is piecewise constant | visible steps; an anomaly appears as a bullseye |
| linear / cubic on a triangulation | the field is locally a polynomial | overshoot near steep gradients (cubic), faceting (linear) |
| inverse-distance weighting | influence decays with distance, with a chosen exponent | the exponent is arbitrary and controls the smoothing |
| radial basis functions | the field is a sum of translates of one kernel, fitted exactly | can oscillate wildly in data gaps; sensitive to the kernel choice |
| kriging | the field is a realisation of a random process with a stated variogram | the answer is only as good as the variogram model, which is itself estimated |
| minimum curvature | the surface minimises a bending-energy functional, so it is the smoothest surface consistent with the data | smooths real short-wavelength features and can undershoot in gaps |

A useful working rule: **in a data gap, every interpolant is extrapolating**, and the
honest map shows the gap or the interpolation distance. Contouring a region with no
data at all and labelling the result as an anomaly map is the most common
misrepresentation in applied geophysics.

## 3. Continuation: derivation and stability

### 3.1 The transfer function

A potential field measured on a plane satisfies Laplace's equation in the source-free
region above and below it. A Fourier component of the field at horizontal wavenumber
$(k_x,k_y)$ behaves in the vertical direction as $e^{\pm|k| z}$ with
$|k| = \sqrt{k_x^{2}+k_y^{2}}$. Requiring the field to remain finite as $z\to+\infty$
selects the decaying solution, so the field continued from height $z_1$ to
$z_2 > z_1$ (upward by $\Delta z = z_2 - z_1$) is

$$\hat f(k; z_2) = e^{-|k|\Delta z}\,\hat f(k; z_1) .
\tag{1}$$

Downward continuation is the formal inverse,

$$\hat f(k; z_1) = e^{+|k|\Delta z}\,\hat f(k; z_2) ,
\tag{2}$$

and its transfer function exceeds 1 for every non-zero wavenumber. **Every value of the
upward operator is at most 1; every value of the downward operator is at least 1.** That
asymmetry is the whole story.

### 3.2 Measured: upward continuation

The demo synthesises a dipole field at 500 m depth on a 201 × 201 grid at 25 m
spacing, adds noise at $\sigma = 16$ nT = 1 % of the peak, and continues the field
upward. Statistics are taken in the interior, so that FFT wraparound cannot be mistaken
for physics:

| $\Delta z$ (m) | peak (nT) | peak retained (%) | predicted $(h/(h+\Delta z))^{3}$ (%) | noise gain | predicted gain (RMS of $e^{-\lvert k\rvert\Delta z}$) |
|---|---|---|---|---|---|
| 100 | 926.1552 | 57.88 | 57.87 | 0.0476 | 0.0523 |
| 250 | 474.6468 | 29.67 | 29.63 | 0.0180 | 0.0188 |
| 500 | 201.1422 | 12.57 | 12.50 | 0.0082 | 0.0066 |
| 1000 | 61.5158 | 3.84 | 3.70 | 0.0031 | 0.0027 |

Two derivations are checked at once: the signal attenuation matches the inverse-cube
falloff of a dipole at depth $h$, $(h/(h+\Delta z))^{3}$, to better than 0.5 %; and
the noise attenuation matches the RMS of the transfer function over the grid's
wavenumbers. **Upward continuation is safe and lossy.** It removes the shallow
wavelengths permanently — inverting it is exactly the unstable operation next.

### 3.3 Measured: downward continuation and its instability

| $\Delta z$ (m) | signal peak (nT) | predicted $(h/(h-\Delta z))^{3}$ (nT) | noise $\sigma$ (nT) | measured gain | predicted gain | S/N |
|---|---|---|---|---|---|---|
| 25 | 1.8661e+03 | 1.866e+03 | 3.3056e+02 | 2.066e+01 | 2.057e+01 | 5.645 |
| 50 | 2.1947e+03 | 2.197e+03 | 1.4071e+04 | 8.794e+02 | 8.534e+02 | 0.156 |
| 100 | 3.1249e+03 | 3.125e+03 | 5.1486e+07 | 3.218e+06 | 2.989e+06 | ~0 |
| 150 | 4.7412e+03 | — | 2.4961e+11 | 1.560e+10 | 1.428e+10 | ~0 |
| 200 | 2.1773e+05 | — | 1.3350e+15 | 8.344e+13 | 7.700e+13 | ~0 |

The measured gains agree with the predicted RMS of $e^{|k|\Delta z}$ to within a few
per cent — so the instability is the *operator*, not an accumulating numerical error.
Note the three consequences:

- the **signal** grows on continuation (as the field approaches its source), but the
  **noise grows faster**: at $\Delta z = 50$ m the S/N is already 0.156;
- the signal peak departs from the $(h/(h-\Delta z))^{3}$ prediction only where the
  noise has taken over the maximum (150 m and beyond), i.e. beyond the depth at which
  the continuation is meaningful;
- the gain at $\Delta z = 100$ m is $3.2\times10^{6}$ — a stated continuation depth
  without a stated noise level is a meaningless claim.

### 3.4 Stabilised downward continuation

Band-limiting the operator to wavelengths longer than $6\Delta z$ — that is,
multiplying by a Gaussian at wavenumber $k_c = 2\pi/(6\Delta z)$ — gives

| $\Delta z$ (m) | signal peak (nT) | noise $\sigma$ (nT) | gain of the stabilised operator | gain of the plain operator |
|---|---|---|---|---|
| 100 | 2.3612e+03 | 3.9068e+00 | 2.601e−01 | 2.934e+06 |
| 200 | 2.3493e+03 | 1.8751e+00 | 1.112e−01 | 8.389e+13 |
| 400 | 1.5025e+03 | 9.0447e−01 | 5.930e−02 | 1.053e+29 |

The gain falls by seven or more orders of magnitude, and the noise *decreases* with
$\Delta z$ because the band limit tightens with it. The price is the resolution: the
retained wavelengths are those longer than $6\Delta z$, so the shallowest detail is
gone by construction. **That is the honest trade, and it is why a downward
continuation is always quoted with both a depth and a wavelength.**

## 4. Derivatives: the noise gain $|k|^{n}$

### 4.1 Derivation

For a grid of spacing $\Delta x$ with white noise of variance $\sigma^{2}$, the noise
is spread uniformly over the representable band $|k|\le k_N = \pi/\Delta x$. The
$n$-th derivative multiplies each wavenumber by $k^{n}$, so the ratio of the output
variance to the input variance is the mean of $k^{2n}$ over the band:

$$\frac{\sigma_{\text{out}}^{2}}{\sigma_{\text{in}}^{2}}
= \frac{\displaystyle\int_{-k_N}^{k_N} k^{2n}\,\mathrm{d}k}
{\displaystyle\int_{-k_N}^{k_N} \mathrm{d}k}
= \frac{k_N^{2n}}{2n+1},
$$

so the **amplitude** gain is

$$\boxed{\ \text{gain}_n = \frac{k_N^{n}}{\sqrt{2n+1}} = \frac{1}{\sqrt{2n+1}}
\left(\frac{\pi}{\Delta x}\right)^{n}\ }
\tag{3}$$

Dimensionally, gain$_n$ carries $\mathrm{m^{-n}}$, which is why the table below quotes
per-metre values.

### 4.2 Measured

[`code/derivative_noise_gain_demo.py`](./code/derivative_noise_gain_demo.py) measures
the gain by applying the operator to realisations of unit-variance white noise
(1024 samples, $\Delta x = 25$ m, $k_N = 0.12566$ rad/m, 60 realisations):

| order $n$ | measured gain | predicted $k_N^{n}/\sqrt{2n+1}$ | ratio |
|---|---|---|---|
| 1 | 0.07210 | 0.07255 | 0.9938 |
| 2 | 0.00706 | 0.00706 | 0.9991 |
| 3 | 0.00075 | 0.00075 | 0.9984 |
| 4 | 0.00008 | 0.00008 | 0.9968 |

The same measurement at four spacings confirms the $1/\Delta x^{n}$ scaling:

| $\Delta x$ (m) | gain $n=1$ | gain $n=2$ | gain $n=3$ |
|---|---|---|---|
| 100 | 0.01790 | 0.00043 | 0.00001 |
| 50 | 0.03632 | 0.00177 | 0.00009 |
| 25 | 0.07245 | 0.00706 | 0.00075 |
| 10 | 0.18116 | 0.04409 | 0.01171 |

**Halving the spacing doubles the first-derivative gain, quadruples the second and
multiplies the third by eight.** Refining the grid makes a derivative noisier, not
better, because the finer grid admits the higher wavenumbers where white noise lives.

### 4.3 What this does to a real anomaly

Applying the operators to the 1600 nT anomaly of Section 3 with 16 nT of noise:

| operator | peak | noise $\sigma$ | S/N |
|---|---|---|---|
| vertical derivative, order 1 | 6.37575 | 1.65436 | 3.854 |
| vertical derivative, order 2 | 0.03840 | 0.20128 | 0.191 |
| vertical derivative, order 3 | 0.00031 | 0.02659 | 0.012 |

The signal's dominant wavenumber is 0.00125 rad/m, a hundred times smaller than
$k_N = 0.12566$ rad/m, while the noise fills the whole band. Each differentiation
therefore multiplies the signal by a much smaller number than the noise, and the S/N
falls from 3.85 to 0.19 to 0.01. **The third derivative is noise, on this dataset.**

### 4.4 The analytic signal, and an honest account of what it fixes

The analytic signal amplitude $\sqrt{f_x^{2}+f_y^{2}+f_z^{2}}$ is built *from* first
derivatives, so it carries the same $|k|$ amplification:

| quantity | peak | noise $\sigma$ | S/N | noise gain vs input |
|---|---|---|---|---|
| vertical derivative, order 1 | 6.37575 | 1.65436 | 3.854 | 0.0614 |
| total horizontal derivative | 2.74768 | 0.76220 | 3.605 | 0.0476 |
| analytic signal amplitude | 6.37575 | 0.92577 | 6.887 | 0.0579 |

The analytic signal's S/N (6.887) is better than the single vertical derivative's
(3.854) by a factor 1.8 — a real but *modest* improvement, coming from the fact that
it combines three components that each see the source. It is **not** a noise remedy:
its noise gain (0.0579 per metre) is the same order as the first derivative's. Its
genuine advantages are geometric:

- it is **symmetric** over the source, so it locates a body without the skew produced
  by an inclined magnetisation;
- it is **independent of the assumed magnetisation direction**, so it needs no
  reduction to the pole, and therefore no assumption about induced magnetisation.

Use it for the geometry. Band-limit the data before differentiating for the noise.

## 5. Reduction to the pole: a model-based transformation

Reduction to the pole (RTP) transforms a magnetic anomaly measured at a given field
inclination into the anomaly that would have been measured at the magnetic pole, where
the field is vertical and the anomaly sits directly over its source. It is defined by a
transfer function $\Theta^{-1}(k,\theta)$ that depends on the assumed field direction.

### 5.1 Measuring the operator rather than quoting it

Rather than quote a filter (and risk getting its convention wrong), the demo *derives*
the operator from two analytic forward models of the same dipole: one with vertical
magnetisation (the "pole" field) and one with an inclination of 60°. The operator is
their ratio in the Fourier domain:

$$\hat h_{\text{RTP}}(k,\theta) = \frac{\mathcal{F}[\text{vertical model}]}
{\mathcal{F}[\text{model at }60^{\circ}]} ,
\tag{4}$$

and applying it to the 60° field reproduces the vertical field to
$8.0\times10^{-14}$ nT, i.e. to machine precision. The operator's magnitude ranges from
$4.3\times10^{-5}$ to 4.57 — it is not a bounded filter, and it amplifies some
wavenumbers.

Deriving the operator this way has a second benefit: it makes the assumption
*visible*, because the same operator applied to a field generated with a different
inclination is simply wrong. Measured errors against the vertical model:

| true inclination (deg) | peak after RTP (nT) | RMS error (% of peak) |
|---|---|---|
| 45 | 1316.6049 | 5.51 |
| 60 (assumed) | 1600.0000 | 0.00 |
| 75 | 1752.6127 | 5.26 |
| 90 | 1732.8832 | 9.85 |

**Assuming 60° where the true inclination is 90° leaves 9.85 % of the peak as a
systematic error** — a distortion that looks like geology, is spatially coherent, and
will be interpreted as structure. The error at 45° and 75° (about 5 %) is smaller,
which is worse in a way: it is small enough to pass unnoticed.

### 5.2 The assumptions

1. **Induced magnetisation**, so that the magnetisation direction equals the ambient
   field direction. Remanent magnetisation violates this outright, and the error can
   be larger than the anomaly itself. A direction-free quantity (the analytic signal,
   or a derivative magnitude) is the honest alternative when remanence is suspected.
2. **A known ambient field direction**, from a model such as IGRF. The model's own
   uncertainty is small, but the *assumption of induced magnetisation* is not a model
   uncertainty — it is a physical hypothesis.
3. **A single, constant direction over the survey area.** Over hundreds of kilometres
   the inclination and declination change measurably; over a large survey the operator
   must be varied or the survey subdivided.
4. **A flat observation surface and no data gaps.** Both are violated by draped
   airborne surveys and by survey edges.

## 6. Levelling and merging

Merging two surveys means making their long-wavelength levels agree. The operations
are:

| operation | what it does | what it costs |
|---|---|---|
| **DC shift** | adds a constant so the mean agrees in the overlap | removes the absolute datum information of one survey |
| **tilt removal (per line)** | removes a linear trend per line, estimated from tie lines or from the overlap | removes genuine long-wavelength signal, exactly as in [05-06-01](./01-processing-pipeline-concept.md) |
| **tie-line levelling** | uses crossing points to estimate per-line offsets and tilts | needs the tie lines to have been acquired, and they are usually lower resolution |
| **gradient (first or second difference) levelling** | removes along-line trends without external control | imposes a smoothness assumption across the whole grid |
| **micro-levelling** | removes residual line-correlated stripes in two dimensions | can remove real line-correlated structure (dykes, ridges) |

The measured cost of the same operation is in
[05-06-01](./01-processing-pipeline-concept.md): removing a straight line fitted to the
quiet ends of a profile removed 0.1162 mGal of which 0.0134 mGal (**17 %**) was real
regional signal. Merging surveys by tilt removal has the same structure and the same
cost, and the number must be reported.

A further point specific to *merging*: if two surveys have different noise levels or
different resolutions, then after levelling the merged grid has a **spatially varying
resolution**. Contour maps cannot show that, and the limitation belongs in the
metadata. The relevant conventions are in
[22-03-06 Metadata Standards](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md).

## 7. Assumptions

1. **A band-limited, noise-free field for the continuation algebra.** Equations (1)–(2)
   assume the field is exactly harmonic in the region between the two planes; the
   presence of sources, or of noise, breaks the *invertibility*, which is the content
   of Section 3.3.
2. **A regular grid for the Fourier operators.** Continuation and differentiation are
   applied after gridding, so they inherit the interpolant's invention (Section 2).
3. **Periodicity for FFT-based operators.** Real surveys are not periodic, and the
   demo restricts its statistics to the interior for this reason. In practice, data are
   tapered or the operator is applied with padding; the artefact is visible at the
   edges of most processed grids.
4. **A flat observation surface** for continuation, and a constant field direction for
   RTP.
5. **White noise for equation (3).** Coloured or correlated noise changes the gain;
   the correct general statement is $\text{gain}^{2} = \int |k|^{2n} P(k)\,\mathrm{d}k
   \big/ \int P(k)\,\mathrm{d}k$, which reduces to (3) for $P$ constant.
6. **Synthetic parameters.** All numbers in this lesson are measured from the stated
   synthetic configurations.

## 8. Units and dimensional analysis

Continuation transfer functions are dimensionless, since $[|k|\Delta z] =
\mathrm{m^{-1}\cdot m} = 1$. The derivative operators are not:

$$\left[|k|^{n}\right] = \mathrm{m^{-n}},$$

so an $n$-th derivative has units of field per metre$^{n}$, and the noise-gain column of
Section 4.2 is in $\mathrm{m^{-n}}$. Mixing a horizontal derivative with a vertical one
is legitimate only because both are $\mathrm{m^{-1}}$ in these conventions; mixing a
derivative with the field itself is not, and the peak column of Section 4.3 is in
(derivative units) while the noise column is in the same unit, so their ratio (the
S/N) is dimensionless — a useful check that the two columns were computed with the same
operator.

## 9. Python demonstration

Three demos cover this lesson:

- [`code/gridding_demo.py`](./code/gridding_demo.py) — Sections 2.1–2.3, including the
  comparison of seven interpolators and the undersampling sweep;
- [`code/continuation_demo.py`](./code/continuation_demo.py) — Section 3, and the RTP
  measurements of Section 5;
- [`code/derivative_noise_gain_demo.py`](./code/derivative_noise_gain_demo.py) —
  Section 4.

The continuation operator is two lines, and its gain is measured rather than assumed:

```python
H = np.exp(-K * dz)                       # equation (1); +K*dz for downward
field_up = np.real(np.fft.ifft2(np.fft.fft2(field) * H))
gain = np.std(np.real(np.fft.ifft2(np.fft.fft2(white_noise) * H))[lo:hi, lo:hi])
```

Measuring the gain on a *known* noise realisation is the discipline that turns
"downward continuation is unstable" from a warning into a number.

## 10. Exercises, common mistakes, applications

Companion problem sets:
[`exercises/05-merge-and-regularisation-exercises.md`](./exercises/05-merge-and-regularisation-exercises.md)
and [`exercises/05-merge-and-regularisation-solutions.md`](./exercises/05-merge-and-regularisation-solutions.md).

### Common mistakes

1. **Treating the grid as data.** Interpolation across a gap is extrapolation, and the
   map should show the gap.
2. **Not reporting the interpolator.** Measured peak spread 3.1 % between methods.
3. **Downward continuing "to the source".** The operator's gain is $10^{6}$ or more;
   the result is noise unless the data are band-limited, and then it is not the source
   depth you asked for.
4. **Differentiating before band-limiting.** Gain $\propto \Delta x^{-n}$.
5. **Reducing to the pole with an assumed inclination.** Measured error up to 9.85 % of
   the peak at the wrong direction, and 5 % at moderately wrong directions.
6. **Regarding the analytic signal as a noise cure.** Measured: same order of noise
   gain as the first derivative.
7. **Levelling without reporting what was removed.** The measured 17 % of removed real
   signal.

### Real-world applications

- **Aeromagnetic compilation.** Gridding, micro-levelling and RTP are the standard
  sequence, and each has the noise consequence measured above.
- **Regional/residual separation.** Upward continuation by a stated $\Delta z$ is the
  classical separation, and it is exactly a low-pass with a known transfer function.
- **Basement depth estimation.** Uses derivative-based depth rules, which is where the
  $|k|^{n}$ amplification becomes the limiting factor on achievable accuracy.
- **Multi-survey compilations.** National-scale gravity and magnetic compilations are
  levelled and merged from decades of surveys with different instruments and spacings;
  the merged product's spatially varying resolution is a documented limitation.

## 11. Further reading

- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic Applications*.
  Cambridge University Press.** Chapters 8–10: continuation, derivatives, reduction to
  the pole, and their transfer functions. The primary reference for Sections 3–5.
- **Baranov, V., & Naudy, H. (1964). Numerical calculation of the formula of reduction
  to the pole. *Geophysics*, 29(1), 67–79.** The original RTP formulation.
- **Nabighian, M. N., et al. (2005). The historical development of the magnetic method
  in exploration. *Geophysics*, 70(6), 33ND–61ND.** On the interpretation conventions
  and their history.
- **Hinze, W. J., von Frese, R. R. B., & Saad, A. H. (2013). *Gravity and Magnetic
  Exploration* (2nd ed.). Cambridge University Press.** Levelling, merging and
  compilation practice.
- **Scipy interpolation documentation** — <https://scipy.org> — for the exact behaviour
  and options of the interpolators compared in Section 2.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text, and you should
> confirm current availability and editions through your library before citing them.

## 12. Related lessons

- [05-06-01 The Processing Pipeline](./01-processing-pipeline-concept.md) — where gridding belongs in the sequence.
- [05-06-02 Noise Suppression](./02-noise-suppression.md) — the same filter algebra applied to deconvolution.
- [05-06-06 Documenting Processing: Reproducibility in Practice](./06-processing-transparency.md) — recording interpolator, depth and band limits.
- [05-05-03 Spatial Sampling, Wavenumber Aliasing and Reconstruction](../05-survey-design-and-acquisition/03-spatial-sampling-theory.md) — why gridding cannot fix undersampling.
- [02-08-02 Laplace's Equation and Harmonic Functions](../../02-physics/08-potential-theory/02-laplace-equation.md) — the property behind equations (1)–(2).

## 13. Self-assessment checklist

- [ ] I can explain why gridding is invention and give the measured peak spread between interpolators.
- [ ] I can state the undersampling error and say why no interpolator removes it.
- [ ] I can derive $e^{-|k|\Delta z}$ and $e^{+|k|\Delta z}$ and say which is stable.
- [ ] I can measure a continuation operator's noise gain on a known noise realisation.
- [ ] I can derive the derivative noise gain $k_N^{n}/\sqrt{2n+1}$ and check it against a measurement.
- [ ] I can state the RTP assumptions and the measured error from a wrong inclination.
- [ ] I can state what the analytic signal does and does not fix.
- [ ] I can explain what levelling removes and how to report it.
