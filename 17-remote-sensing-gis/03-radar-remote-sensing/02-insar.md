---
id: 17-03-02
title: "InSAR: Interferometric Phase and Deformation Measurement"
level: research
prereqs: ["17-03-01", "17-01-04", "02-03-04"]
tags: [remote-sensing, radar, insar, interferometry, deformation, coherence, speckle]
---

# InSAR: Interferometric Phase and Deformation Measurement

> All models and data in this module are **SYNTHETIC**. The carrier frequency,
> baselines, coherence values, noise realisations and deformation fields in this
> lesson are teaching values computed by the demonstration. No real scene,
> acquisition or measurement is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the interferometric phase $\Delta\phi = (4\pi/\lambda)\Delta r$
   from the two-way path and **explain** why the measured phase is only defined
   modulo $2\pi$.
2. **Demonstrate** the resulting ambiguity explicitly: list the displacements
   that wrap to the same observed phase, and **state** what additional
   information removes it.
3. **Derive** the height sensitivity
   $\mathrm{d}\phi/\mathrm{d}h = (4\pi/\lambda)\,B_{\perp}\sin\theta/R$, the
   ambiguity height $h_a = \lambda R/(2B_{\perp}\sin\theta)$, and **verify** both
   against the exact non-linearised geometry.
4. **Define** coherence, **derive** the baseline-decorrelation model
   $\gamma = 1 - B_{\perp}/B_c$, and **measure** it in a simulation.
5. **Explain** why single-look coherence is identically one, and **quantify** the
   bias of the multilook coherence estimator.
6. **Derive** the speckle intensity statistics (exponential, unit normalised
   variance) and the $1/L$ variance reduction from multilooking.
7. **Convert** a line-of-sight displacement to vertical and horizontal
   components, and **state** the direction that a single geometry cannot see.

## Prerequisites

- [17-03-01 SAR Principles: Geometry, Polarisation, Backscatter](01-sar-principles.md) —
  range resolution, the synthetic aperture, $\sigma^{0}$ and the geometry.
- [17-01-04 Spatial, Spectral, Temporal and Radiometric Resolution](../01-remote-sensing-physics/04-resolution-concepts.md) —
  the resolution budget that multilooking trades against.
- [02-03-04 Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity](../../02-physics/03-oscillations-and-waves/04-wave-basics.md) —
  phase as an angle, and why only an angle modulo $2\pi$ is measurable.

## 1. Intuition: the phase is a ruler with a wrapped scale

Two SAR images of the same area, taken from slightly different positions, can be
multiplied pixel by pixel. Because both are complex, their product is a complex
image whose **argument** is the difference of the two phases. That argument is
the interferogram, and it is astonishingly sensitive: at a wavelength of
$5.66\ \mathrm{cm}$, the phase changes by a full turn when the range to the
ground changes by $2.83\ \mathrm{cm}$.

The catch is in the phrase "argument": a phase is an angle, and an angle is only
ever known modulo $2\pi$. The interferogram therefore measures the range change
**modulo half a wavelength**, and every statement about deformation rests on how
that integer is resolved. This lesson derives the relation honestly, shows the
ambiguity in numbers, and then builds the two tools that make the measurement
useful: **coherence** (which says how much the phase can be trusted) and the
**geometry** (which says how a phase difference maps to a displacement).

Speckle — the multiplicative granularity of any coherent image — is derived here
rather than in lesson [01](01-sar-principles.md) because it is exactly the
statistics of the two fields whose correlation *is* the coherence.

## 2. Definitions

| Symbol | Meaning | Unit |
|---|---|---|
| $r_1, r_2$ | slant ranges to the same ground point from the two acquisitions | m |
| $\phi_1,\phi_2$ | phases of the master and slave images | rad |
| $\gamma$ | complex coherence between the two images | dimensionless |
| $B$ | baseline vector between the two antenna positions | m |
| $B_{\perp}, B_{\parallel}$ | components of $B$ perpendicular and parallel to the line of sight | m |
| $L$ | number of independent looks averaged | dimensionless |
| $h$ | topographic height above the reference (ellipsoid-local) surface | m |

The **interferogram** is $I = s_1 s_2^{*}$; its argument is
$\Delta\phi = \arg(s_1 s_2^{*})$. **Coherence** is
$\gamma = \dfrac{\langle s_1 s_2^{*}\rangle}
{\sqrt{\langle|s_1|^{2}\rangle\langle|s_2|^{2}\rangle}}$,
where the brackets are an average over a neighbourhood (the multilook window).
Coherence near 1 means the two fields are the same up to a phase; near 0 means
the phase carries no information.

## 3. Derivations

### 3.1 The phase-to-range relation

A monostatic radar transmits and receives, so the phase accumulated along a path
of length $r$ is $\phi = -2\pi\,(2r)/\lambda = -4\pi r/\lambda$. Forming the
interferogram multiplies the master by the conjugate of the slave:

$$I = s_1 s_2^{*} = |s_1||s_2|\,
\exp\!\left[-\mathrm{i}\frac{4\pi}{\lambda}\left(r_1 - r_2\right)\right],
\qquad
\boxed{\;\Delta\phi = -\frac{4\pi}{\lambda}\left(r_1 - r_2\right).\;}$$

The factor $4\pi$ is the price of the round trip, and it is why InSAR is twice as
sensitive per unit range as one might guess. The demonstration prints the
coefficient two ways: $4\pi/\lambda = 222.16\ \mathrm{rad\,m^{-1}}
= 3.8774\ \mathrm{rad\,mm^{-1}}$.

### 3.2 The measured phase is wrapped

The receiver measures a phase only as an angle. Define the wrapped value
$\mathcal{W}(\phi) = (\phi + \pi)\bmod 2\pi - \pi$. Then
$\mathcal{W}(\phi)$ changes by nothing at all when the range changes by
$\lambda/2 = 2.8282\ \mathrm{cm}$ (LOS). The demonstration's table is worth
reading slowly:

| $d_{\text{LOS}}$ (cm) | $\phi$ (rad) | wrapped (rad) | wrapped (deg) |
|---|---|---|---|
| 0.00 | 0.0000 | 0.0000 | 0.00 |
| 0.50 | 1.1108 | 1.1108 | 63.64 |
| 1.00 | 2.2216 | 2.2216 | 127.29 |
| 1.50 | 3.3324 | $-2.9508$ | $-169.07$ |
| 2.00 | 4.4432 | $-1.8400$ | $-105.42$ |
| 2.83 | 6.2871 | 0.0039 | 0.23 |
| 4.00 | 8.8864 | 2.6032 | 149.15 |
| 6.00 | 13.3296 | 0.7632 | 43.73 |

At $2.83\ \mathrm{cm}$ the wrapped phase returns to zero: the interferogram
cannot tell that displacement from no displacement at all.

### 3.3 The ambiguity, stated exactly

Fix an observed wrapped phase, say the one produced by
$d = 1.00\ \mathrm{cm}$. Which displacements produce it? All
$d = 1.00\ \mathrm{cm} + k\,\lambda/2$ for integer $k$ — the demonstration
tabulates $k = -2\ldots+2$ and verifies that the wrapped phases agree to
$1.8\times10^{-15}$ rad, i.e. to double-precision zero:

| $k$ | $d_{\text{LOS}}$ (cm) | $\phi$ (rad) | wrapped (rad) | wrapped $-$ measured |
|---|---|---|---|---|
| $-2$ | $-4.656$ | $-10.3448$ | 2.2216 | $1.8\times10^{-15}$ |
| $-1$ | $-1.828$ | $-4.0616$ | 2.2216 | 0 |
| $0$ | $1.000$ | $2.2216$ | 2.2216 | 0 |
| $+1$ | $3.828$ | $8.5048$ | 2.2216 | 0 |
| $+2$ | $6.656$ | $14.7880$ | 2.2216 | $-1.8\times10^{-15}$ |

Notice that $k = -1$ corresponds to a *negative* displacement of the same
magnitude of wrap: the interferometric measurement is as blind to the sign of
the motion as it is to the multiple. Three ingredients break the ambiguity, and
each is an assumption:

1. **Continuity** — neighbouring pixels differ by less than half a fringe, so
   the integer can be propagated by unwrapping. This is the standard assumption
   and it fails at steep gradients (Section 4).
2. **An external constraint** — a GNSS time series that pins the absolute offset
   of one pixel, or a physical bound on the deformation.
3. **Independence of the reference** — a stacked network measures *differences*
   between epochs, so one epoch (and one region per disconnected component) is
   arbitrary by construction (developed in
   [03 InSAR Time Series](03-insar-time-series.md)).

Unwrapping does **not** remove the ambiguity. It converts one integer per pixel
into one integer per connected region plus an assumption about that region.

### 3.4 Height sensitivity and the ambiguity height

Decompose the baseline in the local frame by the look direction
$\hat{u} = (\sin\theta, -\cos\theta)$ (horizontal toward the radar, vertical):

$$B_{\perp} = B\cdot(\cos\theta,\ \sin\theta), \qquad
B_{\parallel} = B\cdot(\sin\theta,\ -\cos\theta).$$

For a target at the reference surface $r_1 - r_2 = B\cdot\hat{u}$. Raising the
scatterer by $h$ at fixed ground range rotates the look direction:

$$\frac{\mathrm{d}\hat{u}}{\mathrm{d}\theta} = (\cos\theta,\ \sin\theta)
\qquad\Longrightarrow\qquad
\frac{\mathrm{d}\theta}{\mathrm{d}h} = \frac{\sin\theta}{R},$$

because $\tan\theta = X/(H-h)$ with $H-h \approx R\cos\theta$. Combining the two,

$$
\boxed{\;\frac{\mathrm{d}\phi}{\mathrm{d}h}
= \frac{4\pi}{\lambda}\,\frac{B_{\perp}\sin\theta}{R},
\qquad
h_a = \frac{\lambda R}{2B_{\perp}\sin\theta}.\;}
$$

*Numerical check (SYNTHETIC)*, from the demonstration, with
$\lambda = 5.6565\ \mathrm{cm}$, $R = 800\ \mathrm{km}$:

| $\theta$ | $B_{\perp}$ | $\mathrm{d}\phi/\mathrm{d}h$ (rad/m) | $h_a$ (m) |
|---|---|---|---|
| $23^\circ$ | 100 m | 0.010851 | 579.1 |
| $35^\circ$ | 100 m | 0.015928 | 394.5 |
| $35^\circ$ | 200 m | 0.031856 | 197.2 |
| $45^\circ$ | 200 m | 0.039273 | 160.0 |

At $\theta = 35^\circ$, $B_{\perp} = 100\ \mathrm{m}$, a relief of $394.5\
\mathrm{m}$ produces exactly one fringe. The demonstration checks this against
the exact geometry — computing $r_1(h)$, $r_2(h)$ from the antenna and target
coordinates and forming $(4\pi/\lambda)[(r_1-r_2)(h) - (r_1-r_2)(0)]$:

| $h$ (m) | exact (rad) | linear model (rad) | difference (rad) |
|---|---|---|---|
| 0.00 | 0.000000 | $-0.000000$ | 0 |
| 98.62 | $-1.571095$ | $-1.570796$ | $-2.99\times10^{-4}$ |
| 197.23 | $-3.142508$ | $-3.141593$ | $-9.15\times10^{-4}$ |
| 394.47 | $-6.286285$ | $-6.283185$ | $-3.10\times10^{-3}$ |
| 788.94 | $-12.577650$ | $-12.566371$ | $-1.13\times10^{-2}$ |

The exact and linearised values agree to better than $0.2\%$ of a fringe over
the tested range; the residual is the second-order curvature term in $h$.

> **A convention trap.** A displacement $\mathrm{d}s$ along the direction
> *perpendicular to the line of sight* has a vertical component
> $\mathrm{d}s\sin\theta$ and gives
> $\mathrm{d}\phi/\mathrm{d}h = (4\pi/\lambda)B_{\perp}/(R\sin\theta)$ — larger by
> $1/\sin^2\theta$, a factor of 3.04 at $\theta=35^\circ$. That is the origin of
> the widely quoted $h_a = \lambda R\sin\theta/(2B_{\perp})$. The two forms differ
> only in which direction "height" is measured along; the vertical form derived
> above is the one that converts *relief* into fringes, and the demonstration
> verifies it against the exact geometry. Mixing them silently biases every
> topographic correction by $\sin^2\theta$.

### 3.5 Speckle

Each resolution cell contains many scatterers. Their echoes add as complex
numbers with essentially random phases, so the sum is a circular complex
Gaussian field $z$; the intensity $I = |z|^{2}$ is exponentially distributed.
The demonstration measures the normalised moments of $2\times10^{6}$ such
intensities:

| moment | exponential | measured | ratio |
|---|---|---|---|
| $\langle I\rangle$ | 1 | 1.0000 | 1.0000 |
| $\langle I^{2}\rangle/\langle I\rangle^{2}$ | 2 | 2.0008 | 1.0004 |
| $\langle I^{3}\rangle/\langle I\rangle^{3}$ | 6 | 5.9988 | 0.9998 |
| $\langle I^{4}\rangle/\langle I\rangle^{4}$ | 24 | 23.9385 | 0.9974 |
| normalised std | 1 | 1.0004 | 1.0004 |

The normalised standard deviation is **1**: speckle noise is as large as the
signal, on a single look. Averaging $L$ independent looks (multilooking, which
costs resolution) reduces the normalised variance as $1/L$:

| $L$ | $1/L$ | measured |
|---|---|---|
| 1 | 1.000000 | 0.99618 |
| 4 | 0.250000 | 0.25112 |
| 16 | 0.062500 | 0.06244 |
| 64 | 0.015625 | 0.01562 |
| 256 | 0.003906 | 0.00393 |

Speckle is **not** additive noise. It is a deterministic function of the
scatterer arrangement inside the cell, so it does not average away with time;
only more looks (coarser resolution), more independent observations, or a model
of the target removes it. This matters twice in InSAR: it sets the noise floor
of every amplitude measurement, and it *is* the pair of fields whose correlation
defines the coherence.

### 3.6 Coherence: the estimator and its bias

The estimator used everywhere in practice is

$$\hat{\gamma} = \frac{\left|\sum_{l=1}^{L} s_1^{(l)} s_2^{(l)*}\right|}
{\sqrt{\sum_l |s_1^{(l)}|^{2}\;\sum_l |s_2^{(l)}|^{2}}}.$$

It is biased. The demonstration measures its mean for a known true coherence by
simulating circular Gaussian pairs:

| true $\gamma$ | $L=1$ | $L=4$ | $L=16$ | $L=64$ | $L=256$ |
|---|---|---|---|---|---|
| 0.20 | 1.0000 | 0.4810 | 0.2894 | 0.2203 | 0.2041 |
| 0.50 | 1.0000 | 0.6062 | 0.5208 | 0.5042 | 0.5007 |
| 0.80 | 1.0000 | 0.8189 | 0.8037 | 0.8002 | 0.7999 |
| 0.95 | 1.0000 | 0.9505 | 0.9502 | 0.9501 | 0.9501 |

Two facts to carry away. At $L=1$ the estimator is **identically 1** for every
true coherence: a single look contains no information about correlation, because
the normalisation exactly cancels the numerator. And the bias is always
*downward*, so an uncorrected coherence map reports low coherence where the
scene is merely textured. This is why any statement of the form "coherence above
0.3" must be accompanied by the number of looks.

### 3.7 How coherence sets the phase precision

With $L$ looks and coherence $\gamma$ the multilook phase has, asymptotically,

$$\sigma_{\phi}^{2} \approx \frac{1-\gamma^{2}}{2L\gamma^{2}}.$$

The demonstration compares this with the measured spread:

| $\gamma$ | $L$ | asymptotic $\sigma_\phi$ (rad) | measured (rad) |
|---|---|---|---|
| 0.3 | 1 | 2.2485 | 1.5665 |
| 0.3 | 16 | 0.5621 | 0.7144 |
| 0.5 | 1 | 1.2247 | 1.3268 |
| 0.5 | 16 | 0.3062 | 0.3417 |
| 0.8 | 16 | 0.1326 | 0.1382 |

The formula fails where it should: a wrapped phase with no information is
uniform on $(-\pi,\pi]$ and has $\sigma_\phi = \pi/\sqrt{3} = 1.8138\
\mathrm{rad}$, so at $\gamma = 0.3$ and one look the measured spread saturates
near that value while the asymptotic expression still predicts 2.25 rad — a
number larger than the phase distribution can deliver. The relation is a
large-$L$, moderate-to-high-$\gamma$ result. Checking the regime before using it
is not pedantry: it is the difference between a 0.5 rad error bar and no error
bar at all.

At $\lambda = 5.6565\ \mathrm{cm}$, 0.50 rad is 0.225 cm of LOS displacement and
1.00 rad is 0.450 cm. That is the honest precision statement for an InSAR pair,
and it is bounded below by the coherence of the pair.

### 3.8 Baseline decorrelation

Two acquisitions view the surface with slightly different look angles, so the
ground wavenumbers that contribute to a pixel shift by

$$\Delta k = \frac{4\pi\cos\theta}{\lambda}\frac{B_{\perp}}{R},$$

while the reflectivity band the pixel can hold has width $\Delta K = 2\pi/\Delta
g$ with $\Delta g$ the ground pixel spacing. The coherence is the overlap of the
two shifted bands:

$$\gamma = 1 - \frac{|\Delta k|}{\Delta K}
\qquad\Longrightarrow\qquad
B_c = \frac{\lambda R}{2\,\Delta g\,\cos\theta}.$$

The demonstration generates a random reflectivity spectrum, passes it through
two rectangular band-pass filters offset by $\Delta k$, and measures the
coherence of the two resulting fields:

| $B_{\perp}/B_c$ | $B_{\perp}$ (m) | model $\gamma$ | measured $\gamma$ |
|---|---|---|---|
| 0.00 | 0.0 | 1.0000 | 1.0000 |
| 0.25 | 792.8 | 0.7500 | 0.7496 |
| 0.50 | 1585.6 | 0.5000 | 0.5067 |
| 0.75 | 2378.4 | 0.2500 | 0.2508 |
| 1.00 | 3171.2 | 0.0000 | 0.0008 |
| 1.25 | 3964.0 | 0.0000 | 0.0000 |

with $\Delta g = 8.71\ \mathrm{m}$ at $\theta = 35^\circ$ giving
$B_c = 3171.2\ \mathrm{m}$. Beyond the critical baseline there is no spectral
overlap and the interferogram is noise, no matter how strong the echo.

The other decorrelation terms enter multiplicatively:
$\gamma = \gamma_{\text{geom}}\gamma_{\text{temp}}\gamma_{\text{vol}}
\gamma_{\text{thermal}}$. **Temporal** decorrelation grows with the time between
acquisitions and with vegetation; **volume** decorrelation grows when the
scattering comes from a layer (canopy, dry snow) rather than a surface;
**thermal** decorrelation is the SNR limit. Separating them is what
[03 InSAR Time Series](03-insar-time-series.md) does.

## 4. Unwrapping and what it can and cannot fix

Unwrapping estimates the integer field $k(x,y)$ such that
$\phi_{\text{unwrapped}} = \mathcal{W}(\phi) + 2\pi k$. Two properties control
whether it is possible:

- **Residues.** Summing wrapped phase differences around a closed loop gives
  $2\pi$-quantised values. A non-zero residue means at least one pixel in the
  loop is aliased; residues are the fingerprint of unwrapping failure, and
  branch-cut or minimum-cost-flow algorithms route around them.
- **Gradient limit.** Aliasing in the wrapped phase occurs when the phase
  difference between adjacent pixels exceeds $\pi$, i.e. when the LOS
  displacement changes by more than $\lambda/4$ per pixel. At
  $\lambda = 5.6565\ \mathrm{cm}$ and a $20\ \mathrm{m}$ pixel that is
  $1.41\times10^{-3}$ of strain-like gradient (metre of displacement per metre of
  ground), well above the elastic strain of any earthquake but reachable in
  mining subsidence, lava flows and permafrost slumps.

Unwrapping outputs one integer per connected region plus the assumption that
fixes the region. It cannot distinguish a 2.83 cm uniform shift of the whole
scene from no shift, and it cannot repair a region where the fringes are
aliased. Lesson [05](05-insar-applications.md) shows the practical consequences;
lesson [03](03-insar-time-series.md) shows how a network of many dates replaces
"unwrap one big interferogram" with "estimate a consistent set of small ones".

## 5. Worked example — from phase to displacement and back

*All values SYNTHETIC.* A descending pass with $\lambda = 5.6565\
\mathrm{cm}$, $\theta = 35^\circ$ and heading $8^\circ$ west of north observes a
region where the wrapped phase changes by exactly $+4$ fringes between two
epochs, and coherence is 0.8 with $L = 16$ looks.

1. **Phase.** $4$ fringes $= 4 \times 2\pi = 25.133\ \mathrm{rad}$.
2. **LOS displacement.** $\Delta r = \lambda\,\Delta\phi/(4\pi)
   = 0.056565 \times 25.133/(4\pi) = 0.11313\ \mathrm{m} = 11.31\ \mathrm{cm}$
   along the line of sight. (Equivalently $4 \times 2.8282\ \mathrm{cm}$.)
3. **Precision.** From the table, $\gamma = 0.8$, $L = 16$ gives
   $\sigma_\phi \approx 0.1326\ \mathrm{rad}$ (measured 0.1382), i.e.
   $\sigma = 0.056565\times0.1382/(4\pi) = 6.2\times10^{-4}\ \mathrm{m}
   = 0.62\ \mathrm{mm}$. The fringe count itself is exact; the *ambiguity* is
   not, so the honest statement is $11.31\ \mathrm{cm} \pm 0.06\ \mathrm{cm}$
   only if unwrapping is trusted.
4. **Rejection of a competing hypothesis.** A uniform 2.83 cm LOS shift of the
   whole scene would produce exactly the same wrapped phases. Without an
   external constraint, that alternative is admitted by the data.
5. **Vertical versus horizontal.** If the motion is assumed purely vertical,
   $d_v = d_{\text{LOS}}/\cos\theta = 11.31/0.8192 = 13.81\ \mathrm{cm}$. If it
   is assumed purely east–west, the LOS projection uses the horizontal unit
   vector instead and the same LOS change implies a different amplitude; the
   two assumptions differ by $\sim40\%$ at this incidence. The data choose
   neither.

This example is the whole content of the lesson in one calculation: a precise
number for a displacement *along a direction that had to be assumed*, with an
integer that had to be assumed, and an uncertainty that is real but smaller than
the assumption errors.

## 6. Assumptions and regime of validity

1. **Coherence is high enough to unwrap.** $\gamma \gtrsim 0.3$ with a few looks
   in most terrain; the demonstration's saturation table shows why lower values
   leave the phase essentially uninformed.
2. **The scatterers are stable** between acquisitions at the scale of the
   wavelength — the temporal-decorrelation assumption, which fails for
   vegetation, water, snow and agriculture.
3. **The surface is a thin scattering layer.** Volume scattering from a canopy
   or a dry snowpack adds a phase that is not a surface displacement.
4. **The deformation is small compared with the ambiguity** within one pixel:
   less than $\lambda/4$ of LOS change per pixel, or aliasing.
5. **A single scattering mechanism dominates** each resolution cell; mixtures
   bias the phase.
6. **The reference surface and the orbits are known** to a fraction of the
   ambiguity height; otherwise the topographic and orbital phase leak into the
   displacement term ([04](04-insar-atmospheric-correction.md)).
7. **The atmosphere is common** or corrected: an unmodelled path delay is
   indistinguishable from a displacement in a single interferogram
   ([04](04-insar-atmospheric-correction.md)).
8. **Additive thermal noise is white**; the multiplicative speckle is handled by
   multilooking, which is a stated resolution cost.

## 7. Python demonstration

`code/insar_demo.py` prints, in units, nine sections: the wavelength and fringe;
the phase and its wrap; the ambiguity table; the height sensitivity with the
exact-geometry verification; the coherence estimator bias; the measured baseline
decorrelation; the speckle moments and multilook variance; the phase precision
versus coherence; and the LOS projection.

```bash
cd 17-remote-sensing-gis/03-radar-remote-sensing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python insar_demo.py
```

## 8. Exercises

See [`exercises/02-insar-exercises.md`](./exercises/02-insar-exercises.md) and
[`exercises/02-insar-solutions.md`](./exercises/02-insar-solutions.md).

## Mastery checkpoint

Without notes: **(a)** derive $\Delta\phi = -(4\pi/\lambda)\Delta r$ and state the
displacement that produces exactly one fringe. **(b)** Compute $h_a$ for
$\lambda = 5.6565\ \mathrm{cm}$, $R = 800\ \mathrm{km}$, $\theta = 35^\circ$,
$B_{\perp} = 50\ \mathrm{m}$. **(c)** A wrapped phase of $+1.2\ \mathrm{rad}$ is
observed; list three displacements that produce it. **(d)** With $\gamma = 0.5$
and $L = 4$, give the phase uncertainty and convert it to millimetres of
displacement. **(e)** State the direction a single ascending or descending pass
is least sensitive to.

A worked version of (a)–(d) is in the lesson-02
[solutions](./exercises/02-insar-solutions.md).

## Common pitfalls

1. **Treating the wrapped phase as a displacement.** It is a displacement modulo
   $\lambda/2$, with a sign ambiguity as well.
2. **Confusing the two height sensitivities.** The $1/\sin^2\theta$ factor
   between the vertical and perpendicular-to-LOS conventions silently biases
   topographic correction.
3. **Reporting coherence without the number of looks.** At $L=1$ it is
   identically one.
4. **Extrapolating the $\sigma_\phi$ formula to low coherence.** It predicts
   values the wrapped phase cannot produce.
5. **Assuming a displacement direction.** A single geometry measures one
   projection; vertical and horizontal interpretations differ by tens of
   percent.
6. **Believing unwrapping resolves the ambiguity.** It relocates it.
7. **Ignoring the phase of the reference surface.** Topography, orbit error and
   atmosphere all enter the same channel as deformation.

## Related modules

- [01 SAR Principles: Geometry, Polarisation, Backscatter](01-sar-principles.md) —
  where the ranging and speckle come from.
- [03 InSAR Time Series: PS-InSAR and SBAS](03-insar-time-series.md) — how a
  network of pairs replaces one fragile unwrapping.
- [04 Atmospheric and Orbital Error Correction in InSAR](04-insar-atmospheric-correction.md) —
  the delay that mimics displacement.
- [05 InSAR for Earthquakes, Volcanoes, Subsidence and Landslides](05-insar-applications.md) —
  what the numbers are used for.
- [13-04 Tectonophysics and Deformation](../../13-geodynamics-tectonics/04-tectonophysics-deformation/README.md) —
  the elastic and viscoelastic models that interpret the deformation field.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — unwrapping and
  time-series estimation as inverse problems with stated regularisation.
