---
id: 07-03-05
title: "Derivatives, Upward/Downward Continuation and Euler Deconvolution"
level: doctoral
prereqs: ["07-03-03", "18-03-02"]
tags: [gravity, geodesy, derivatives, continuation, euler-deconvolution, filters]
---

# Derivatives, Upward/Downward Continuation and Euler Deconvolution

All models and data in this module are SYNTHETIC. The harmonic field, the noise
level and the compact source used below are chosen teaching values.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the wavenumber-domain operators for horizontal derivatives, the
   vertical derivative, and upward continuation, and **verify** each against an
   analytic field.
2. **Explain** why the vertical derivative filter is $|k|$ and the upward
   continuation operator is $e^{-|k|\Delta z}$.
3. **Measure** the split of the derivative's error into truncation bias and
   noise variance, and **choose** a cutoff against a stated target.
4. **Quantify** the exponential amplification of downward continuation and
   **state** the depth beyond which it cannot be trusted.
5. **Derive** the Euler equation for a homogeneous field and **solve** it in a
   sliding window.
6. **Demonstrate** the structural-index ambiguity and the two-source failure of
   the single-source assumption.
7. **State** when a derivative or a continued field is a better product than the
   original map, and when it is a picture of the noise.

## Prerequisites

- [03 Forward Modelling in 2-D and 3-D](03-forward-modelling-2d3d.md) — how the
  field being filtered is generated.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md) —
  the general form of the bias–variance trade-off used here.

## 1. Why filter a potential field at all

A gravity map is a smoothed image of the subsurface, because the kernel is a
broad, decaying function. Sharpening — taking derivatives — makes shallow, small
features more visible; continuation moves the observation surface, which is a
legitimate way to compare data acquired at different heights; Euler deconvolution
tries to estimate source depth without any inversion at all.

All of these are *linear filters*, and all of them multiply the amplitude
spectrum by a factor that grows with wavenumber. That is the source of their
power and of their danger: the same factor that sharpens a geological edge
amplifies the noise that lives at the shortest wavelengths.

## 2. The operators

Let $\tilde{g}(\mathbf{k})$ be the 2-D Fourier transform of the field on the
observation plane, with $\mathbf{k} = (k_x,k_y)$ and $k = |\mathbf{k}|$. For a
field satisfying Laplace's equation above the sources:

| operation | multiplier in the wavenumber domain |
|---|---|
| $\partial/\partial x$ | $ik_x$ |
| $\partial/\partial y$ | $ik_y$ |
| $\partial/\partial z$ ( $z$ upward) | $-k$ |
| upward continuation by $\Delta z$ | $e^{-k\Delta z}$ |
| downward continuation by $\Delta z$ | $e^{+k\Delta z}$ |
| $n$-th vertical derivative | $(-k)^{n}$ |

The three statements worth deriving rather than memorising:

- **Upward continuation.** A harmonic component of wavenumber $k$ decays upward
  as $e^{-kz}$; that is the defining behaviour of a Laplace solution. Multiplying
  by $e^{-k\Delta z}$ is therefore the exact operator, not an approximation.
- **Vertical derivative.** $\partial_z e^{-kz} = -k\,e^{-kz}$, so the operator is
  $-k$, identical in form to upward continuation with a complex continuation
  distance. A first vertical derivative is "continuation by one wavenumber".
- **Non-locality of the derivative in space.** Because $|k|$ is not a polynomial,
  the corresponding space-domain filter is not compact; a derivative at one point
  depends on the field everywhere. This is why edge effects are severe.

The demonstration builds a synthetic field from four harmonics whose
wavenumbers sit exactly on FFT bins,

$$g(x,y) = \sum_i A_i\cos(k_{x,i}x)\cos(k_{y,i}y)
\quad\text{(mGal)},$$

and compares each filter with the analytic derivative or continuation. The
maximum discrepancy is $1.2\times10^{-16}$ to $1.3\times10^{-15}$ (mGal/m or
mGal) — floating-point round-off. **On a periodic grid the filters are exact**,
so any error in a real application comes from the data, the taper, or the
assumption of periodicity.

## 3. Noise: the bias–variance split, measured

Add white noise of $0.10\ \mathrm{mGal}$ rms to the field (whose own rms is
$3.509\ \mathrm{mGal}$) and compute the vertical derivative with a smooth
low-pass $1/[1+(k/k_c)^{8}]$:

| cutoff wavelength (m) | total error (mGal/m) | bias (mGal/m) | noise (mGal/m) |
|---|---|---|---|
| none | 0.002555 | 0.000000 | 0.002555 |
| 2000 | 0.005298 | 0.005297 | 0.000017 |
| 1000 | 0.000540 | 0.000533 | 0.000067 |
| 500 | 0.000276 | 0.000002 | 0.000275 |
| 300 | 0.000755 | 0.000000 | 0.000755 |

The error splits cleanly. At a $2000\ \mathrm{m}$ cutoff the filter is so gentle
that it removes real short-wavelength content — bias $0.005297\ \mathrm{mGal/m}$
— while passing almost no noise. At $300\ \mathrm{m}$ it keeps the signal and
amplifies noise to $0.000755\ \mathrm{mGal/m}$. The optimum here is near
$500\ \mathrm{m}$, and it is optimum only *for this noise level and this signal*:
there is no universal cutoff, and copying one from another survey is a mistake.

Note the shape of the trade-off: the total error at $500\ \mathrm{m}$ is
$0.000276\ \mathrm{mGal/m}$, a factor of $9$ better than the unfiltered
$0.002555$. Sharpening without denoising is a net loss on noisy data.

## 4. Downward continuation: the amplification that cannot be avoided

Continuing the noisy field downward by $\Delta z$ multiplies each wavenumber by
$e^{k\Delta z}$:

| depth (m) | full-band rms error (mGal) | low-pass 1000 m rms error (mGal) |
|---|---|---|
| 200 | $8.621\times10^{1}$ | $2.940\times10^{-1}$ |
| 500 | $2.031\times10^{7}$ | $5.554\times10^{0}$ |
| 1000 | $4.039\times10^{16}$ | $8.338\times10^{9}$ |
| 2000 | $2.726\times10^{35}$ | $5.165\times10^{28}$ |

At the Nyquist wavenumber $k = 0.0314\ \mathrm{m^{-1}}$ the factor is
$e^{k\Delta z} = 6.64\times10^{6}$ for $\Delta z = 500\ \mathrm{m}$ and
$4.40\times10^{13}$ for $1000\ \mathrm{m}$. A low pass at $1000\ \mathrm{m}$
wavelength buys a factor of $300$ at $\Delta z = 200\ \mathrm{m}$ and $4000$ at
$500\ \mathrm{m}$ — but it cannot rescue a $2\ \mathrm{km}$ continuation, because
the cutoff wavelength is then shorter than the continuation distance and the
retained band is amplified beyond use.

**Practical rule.** Downward continuation is usable to a depth of order the
shortest retained wavelength divided by $2\pi$; beyond that, the result is a map
of the noise's low-wavenumber tail, not of the subsurface.

## 5. Euler deconvolution

For a field $g$ that is homogeneous of degree $-N$ in the vector from the
observation point to the source, Euler's theorem gives

$$(x-x_0)\frac{\partial g}{\partial x} + (y-y_0)\frac{\partial g}{\partial y}
+ (z-z_0)\frac{\partial g}{\partial z} = -N g,$$

and with a background $B$ subtracted from $g$ and the observation plane at
$z = 0$ this becomes a **linear** equation in the unknowns
$(x_0, y_0, z_0, B)$:

$$x_0 g_x + y_0 g_y + z_0 g_z + N B = x g_x + y g_y + N g .$$

The demonstration verifies the convention numerically rather than asserting it:
for a point mass with $M = 2.0\times10^{11}\ \mathrm{kg}$ at
$(200, -300, 800)\ \mathrm{m}$ (peak $2.0827\ \mathrm{mGal}$ on an
$81\times81$ grid at $75\ \mathrm{m}$ spacing), a window of radius
$1200\ \mathrm{m}$ gives

| $N$ | $x_0$ (m) | $y_0$ (m) | $z_0$ (m) | $B$ (mGal) | rms residual (mGal) |
|---|---|---|---|---|---|
| 0 | 200.3 | $-300.0$ | $-319.4$ | 0.0000 | $8.35\times10^{-1}$ |
| 1 | 200.0 | $-300.0$ | 442.4 | $-0.5080$ | $9.06\times10^{-2}$ |
| 2 | 200.0 | $-300.0$ | 800.0 | 0.0000 | $4.48\times10^{-11}$ |
| 3 | 200.0 | $-300.0$ | 1157.6 | 0.1693 | $9.06\times10^{-2}$ |

$N = 2$ is the structural index of a point mass for the gravity field, and it
returns the true location with a residual of $4.5\times10^{-11}\ \mathrm{mGal}$.
The wrong indices return a *compromise* that fits a wrong model: the horizontal
position is still found, but the depth is wrong by a factor of $1.4$–$2.5$, and
the residual rises by nine orders of magnitude. **Structural index is not a
tuning knob; it is a statement about the source class, and the residual tells you
whether it is right.**

### 5.1 Why the window matters

For an isolated exact source the Euler equation holds pointwise, so any window
returns the same answer. That is a property of the ideal case, and it is
misleading. Add a second mass of $3.0\times10^{11}\ \mathrm{kg}$ at
$(-1400, 1400, 1200)\ \mathrm{m}$ and slide the window:

| window centre | radius (m) | recovered $(x_0,y_0,z_0)$ (m) | rms residual (mGal) |
|---|---|---|---|
| $(200,-300)$ | 1000 | $(310.7,\,-418.1,\,780.1)$ | 0.1730 |
| $(-1400,1400)$ | 1500 | $(-1602.1,\,1615.7,\,1089.7)$ | 0.4094 |
| $(-600,500)$ | 800 | $(-484.4,\,366.7,\,1352.3)$ | 0.1953 |

No window recovers either source exactly: each estimate is pulled towards the
other body. The residual — $0.2\ \mathrm{mGal}$ here against
$4.5\times10^{-11}\ \mathrm{mGal}$ for the isolated source — is the honest
diagnostic that the single-source assumption has failed. Real Euler
implementations reject windows above a residual threshold and report the spatial
clustering of accepted solutions, not a single depth.

### 5.2 Noise

Repeating the single-source window 200 times with added noise:

| noise rms (mGal) | mean $z_0$ (m) | scatter of $z_0$ (m) |
|---|---|---|
| 0.00 | 800.0 | 0.00 |
| 0.02 | 800.0 | 1.19 |
| 0.05 | 799.9 | 2.96 |
| 0.10 | 800.5 | 5.84 |

The estimator is unbiased and its scatter grows roughly linearly with the noise,
because the misfit is quadratic in the errors. With a weaker anomaly, or a
narrower window, the same noise produces a proportionally larger scatter.

## 6. Worked example

*A $2000\ \mathrm{m}$-wide derivative anomaly is computed from data with
$0.05\ \mathrm{mGal}$ noise and $100\ \mathrm{m}$ station spacing. Which cutoff,
and how well can the field be continued to $300\ \mathrm{m}$?*

1. Nyquist wavenumber: $k_N = \pi/100\ \mathrm{m} = 0.0314\
   \mathrm{m^{-1}}$, i.e. a $200\ \mathrm{m}$ wavelength. Noise lives at the top
   of this band.
2. Choose a cutoff at the shortest *signal* wavelength, say $600\ \mathrm{m}$
   ($k_c = 0.0105\ \mathrm{m^{-1}}$). From the table's scaling, the noise term
   falls by roughly $(k_c/k_N)^{2} \approx 0.11$ while the bias stays small.
3. Continuation to $300\ \mathrm{m}$ multiplies the retained band by
   $e^{k_c \times 300} = e^{3.14} = 23$. With input noise of
   $0.05\ \mathrm{mGal}$ the continued field's noise is of order
   $0.05\times23 \approx 1.2\ \mathrm{mGal}$ — larger than most signals of
   interest, which is why the continuation depth must be justified explicitly.
4. **Report:** the derivative, with the cutoff wavelength stated; not a
   downward-continued map whose noise floor exceeds its anomalies.

## 7. Assumptions and regime of validity

1. **Laplace's equation above the sources.** True for a field measured outside
   all masses. Inside a mass (a borehole inside an orebody) the operators fail.
2. **A regular grid with a well-defined sampling interval.** Irregular
   observations must be gridded first, and the gridding is itself a filter whose
   cutoff must be stated.
3. **Local stationarity.** A single filter applied to a whole map assumes the
   noise and signal spectra do not vary across it; real surveys violate this.
4. **Periodicity for FFT filters.** Without padding and tapering, the wrap-around
   at the edges contaminates the result; edges must be trimmed or mirrored.
5. **Euler: a single homogeneous source per window** and gradients measured over
   that window. Violating it produces a confident wrong answer with a large
   residual — the residual is the only warning.
6. **Derivative filtering assumes the noise is white or at least known.** If it
   is not, the cutoff is a guess.

## 8. Physical interpretation

- Every operator here multiplies the spectrum by a power of $k$, so they must all
  amplify the short-wavelength end. Continuation is no exception: upward is a
  low pass, downward is a high pass.
- Continuation to a lower surface is *not* "looking deeper"; it is a different
  observation surface. The information content is unchanged — that is why the
  amplification is exactly the inverse of the attenuation.
- Euler deconvolution is a linear-algebra trick that works only because a
  compact source's field has a scale-free shape. It is powerful where that
  assumption holds and worthless where it does not.
- Derivatives enhance edges and destroy amplitudes: never measure an anomaly
  amplitude on a derivative map.

## 9. Python demonstration

`code/derivatives_and_filters_demo.py` prints:

1. the synthetic harmonic field and its analytic derivatives;
2. the filter verification table (analytic versus FFT);
3. the bias–variance table for the vertical derivative versus cutoff;
4. the downward-continuation table with and without a low pass, and the
   $e^{k\Delta z}$ factors;
5. the structural-index table, the two-source window table, and the noise study.

All output is labelled with units; the script uses
`np.random.default_rng(20261014)` and exits 0.

## 10. Exercises

See
[`exercises/05-derivatives-and-filters-exercises.md`](./exercises/05-derivatives-and-filters-exercises.md)
and
[`exercises/05-derivatives-and-filters-solutions.md`](./exercises/05-derivatives-and-filters-solutions.md).

- **★** Write the wavenumber multipliers for $\partial_x$, $\partial_z$ and
  upward continuation by $1\ \mathrm{km}$, and state their units.
- **★** Explain why the space-domain filter for a vertical derivative does not
  have compact support.
- **★★** Using the bias–variance table, choose a cutoff for a survey whose
  smallest target has a $700\ \mathrm{m}$ wavelength and justify it.
- **★★** Derive the Euler equation from the homogeneity of
  $g = GMz_0/r^{3}$ and confirm the coefficient of the $g_z$ term.
- **★★★** Estimate the maximum depth to which continuation is useful given a
  noise level, a station spacing and a tolerance, and state the assumption you
  had to make about the noise spectrum.

## Mastery checkpoint

Without notes:

> A gridded gravity map has $100\ \mathrm{m}$ spacing and $0.03\ \mathrm{mGal}$
> noise. A compact source produces a $1.5\ \mathrm{mGal}$ anomaly.

**(a)** State the Nyquist wavenumber and the shortest resolvable wavelength.
**(b)** Write the operator you would apply for a first vertical derivative and
for upward continuation by $500\ \mathrm{m}$.
**(c)** Estimate the noise in the unfiltered vertical derivative and the effect
of a $500\ \mathrm{m}$ cutoff.
**(d)** Run Euler deconvolution with $N = 2$ and $N = 3$; state which depth you
would report and what evidence you would demand first.

## Common pitfalls

1. **Derivative maps read for amplitude.** Derivatives have units per metre.
2. **Downward continuation used to "see deeper".** It amplifies noise
   exponentially and adds no information.
3. **A cutoff copied from another survey.** The optimum depends on the noise and
   the signal, both of which differ.
4. **Euler with a guessed structural index.** Check the residual.
5. **Euler windows in the field of two sources.** Report accepted windows, not a
   single depth.
6. **FFT filters without padding.** The edges wrap and contaminate the interior.

## 11. Applications

- **Edge detection for mineral exploration.** Horizontal-derivative maxima map
  contacts and dyke edges.
- **Data levelling and merging.** Upward continuation is the standard tool for
  reconciling surveys flown at different heights.
- **Crustal thickness from gravity.** Euler and spectral depth estimates give
  first-order depths before an inversion is attempted.
- **Noise diagnosis.** The shape of the amplified spectrum reveals whether the
  noise is white, cultural, or gridding-induced — see
  [21-01-02 Choosing Probability Models for Earth Data](../../21-statistics-bayesian-ml/01-statistics-in-practice/02-probability-models-earth.md).

## Related modules

- [04 Gravity Inversion and Its Severe Non-Uniqueness](04-inversion-gravity.md) —
  the same ambiguity, approached by inverting instead of filtering.
- [03 Forward Modelling in 2-D and 3-D](03-forward-modelling-2d3d.md).
- [21-02-01 Regionalised Variables and Spatial Continuity](../../21-statistics-bayesian-ml/02-geostatistics/01-regionalized-variables.md) —
  gridding, which is the filter applied before any of these.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md).

## 12. Self-assessment checklist

- [ ] I can write the five wavenumber operators from memory.
- [ ] I can verify a filter against an analytic field.
- [ ] I can split an error into bias and noise and choose a cutoff.
- [ ] I can state the amplification factor of downward continuation and its
      usable depth.
- [ ] I can derive and solve the Euler equation for a compact source.
- [ ] I can explain why the residual, not the depth, is the diagnostic.
