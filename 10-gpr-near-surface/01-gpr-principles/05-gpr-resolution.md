---
id: 10-01-05
title: "Vertical and Horizontal Resolution Limits"
level: advanced
prereqs: ["10-01-01", "10-01-03", "10-01-04"]
tags: [gpr, near-surface, gpr-principles, resolution, fresnel-zone, migration, aliasing]
---

# Vertical and Horizontal Resolution Limits

> **All models and data in this module are SYNTHETIC.** The velocity, source
> wavelet, migration scheme and detectability thresholds below are chosen
> teaching values. The horizontal-resolution numbers come from a simplified
> unweighted Kirchhoff migration written out in full in the demonstration; they
> are properties of that scheme on synthetic data, not published figures.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the Rayleigh-type criterion you are using for vertical resolution,
   and **compute** the separation at which two reflectors are resolved for a
   given wavelet.
2. **Explain** why the answer depends on the criterion, and **quantify** the
   spread between criteria.
3. **Distinguish** detection from resolution, and **compute** the thickness that
   is detectable once resolution is lost.
4. **Derive** the first Fresnel zone radius from a path-difference condition, and
   **state** the convention that fixes the factor inside it.
5. **Measure** lateral resolution as the width of a migrated point-spread
   function and **explain** its dependence on the migration aperture.
6. **Derive** the spatial-sampling (aliasing) conditions
   $\sin\theta_{\max} = \lambda/(4\Delta x)$ and
   $\sin\theta_{\text{app}} = \sin\theta - m\lambda/(2\Delta y)$ and **predict**
   the apparent dip an under-sampled grid produces.
7. **Report** a resolution claim with the criterion, the aperture and the band
   that produced it.

## Prerequisites

- [01 GPR Physics](01-gpr-physics.md) — the Ricker wavelet and its measured
  spectrum.
- [03 Attenuation, Penetration Depth and Frequency Trade-Offs](03-gpr-attenuation-penetration.md) —
  the frequency choice that resolution and penetration compete for.
- [04 Antennas: Frequency, Shielding, Polarisation and Offsets](04-gpr-antennas.md) —
  the footprint and the offset geometry.

## 1. Vertical resolution and the criterion problem

Vertical resolution is the answer to "how close can two reflectors be and still
be seen as two?" There is no unique answer, because "seen as two" is a choice.
Three criteria are in common use, and they differ:

| criterion | statement | result for the SYNTHETIC model below |
|---|---|---|
| Rayleigh-type | two local maxima of comparable height | $0.085\ \mathrm{m} = 0.170\lambda$ ($1.70\ \mathrm{ns}$) |
| classical half period | separation reaches $1/(2f_0)$ | $0.125\ \mathrm{m} = 0.250\lambda$ ($2.50\ \mathrm{ns}$) |
| tuning thickness | largest composite amplitude | $0.100\ \mathrm{m} = 0.200\lambda$ for a thin bed |

The three differ by up to a third. **A resolution number without its criterion is
not a number**, and the criterion must be stated with the wavelet, because the
answer depends on the whole band, not on a single frequency.

The measurement is done on a synthetic doublet: two equal Ricker wavelets,
$f_0 = 200\ \mathrm{MHz}$, $v = 0.09993\ \mathrm{m\,ns^{-1}}$
($\lambda = 0.4996\ \mathrm{m}$), separated by $\Delta t = 2\Delta z/v$. Counting
local maxima each above $0.9$ of the largest avoids the wavelet's own sidelobes,
which for a Ricker sit at $0.446$ of the main lobe — a detail that silently
inflates the count if it is ignored. Scanning the separation in $0.005\
\mathrm{m}$ steps gives:

| $\Delta z$ (m) | $\Delta z/\lambda$ | $\Delta t$ (ns) | peaks above 0.9 max |
|---|---|---|---|
| 0.040 | 0.080 | 0.80 | 1 |
| 0.080 | 0.160 | 1.60 | 1 |
| 0.120 | 0.240 | 2.40 | 2 |
| 0.200 | 0.400 | 4.00 | 2 |
| 0.280 | 0.560 | 5.60 | 2 |

with the first resolved separation at $0.085\ \mathrm{m}$ ($0.170\lambda$).

## 2. Detection is not resolution

A thin layer produces two reflections of **opposite** polarity — top and bottom
of the same contrast — so its composite trace is $w(t) - w(t-\Delta t)$. For
small separations this is $\Delta t$ times the derivative of the wavelet, so the
composite amplitude grows **linearly with thickness**:

$$A(\Delta z) \approx \left|\frac{\mathrm{d}w}{\mathrm{d}t}\right|_{\max}
\frac{2\Delta z}{v} \quad \text{for } \Delta z \ll \lambda. \tag{2.1}$$

The demonstration fits a slope of $21.32$ per metre ($10.65$ per wavelength) over
$\Delta z = 0.005$–$0.050\ \mathrm{m}$, i.e. the response is linear over that
range exactly as (2.1) says, and prints the tuning curve:

| $\Delta z$ (m) | 0.02 | 0.07 | 0.10 | 0.12 | 0.17 | 0.22 | 0.27 |
|---|---|---|---|---|---|---|---|
| $|$composite$|_{\max}$ | 0.4805 | 1.3254 | **1.4451** | 1.3813 | 1.0912 | 1.0068 | 1.0002 |

The maximum sits at $\Delta z = 0.100\ \mathrm{m} = 0.200\lambda$; the
quarters-wavelength rule of thumb ($0.1249\ \mathrm{m}$ here) carries $93.7\%$ of
that maximum, and $\lambda/8$ carries $86.3\%$.

Now the practical point. With a chosen amplitude detection threshold of $0.05$ of
a single reflector's amplitude, the thinnest detectable bed is
$0.0023\ \mathrm{m} = 0.0047\lambda$ — two orders of magnitude thinner than the
resolution limit. **A layer can be detected long after its thickness has become
unresolvable**, which is why inversion for thickness (not visual separation) is
the right ambition, and why reporting a "resolved" thin layer is the commonest
overclaim in shallow GPR.

## 3. The first Fresnel zone

A reflector at depth $d$ is illuminated not at a point but over a zone, because
all paths within a small path difference arrive almost in phase. Define the first
Fresnel zone by the convention that the **two-way** path difference is at most
$\lambda/2$:

$$2\left(\sqrt{d^{2}+r^{2}} - d\right) = \frac{\lambda}{2}
\;\;\Longrightarrow\;\;
r^{2} = \frac{\lambda d}{2} + \frac{\lambda^{2}}{16}. \tag{3.1}$$

Solving the quadratic exactly gives the left form below; the usual
approximation drops the second term and gives $r \approx \sqrt{\lambda d/2}$.
The half-amplitude zone — two-way path difference $\lambda/4$ — is smaller by
$\sqrt{2}$.

| $d$ (m) | $r$ exact (m) | $r \approx \sqrt{\lambda d/2}$ (m) | error | diameter (m) | diameter$/\lambda$ | half-amplitude $r$ (m) |
|---|---|---|---|---|---|---|
| 0.25 | 0.2794 | 0.2499 | $-10.55\%$ | 0.5588 | 1.12 | 0.1874 |
| 0.50 | 0.3749 | 0.3534 | $-5.72\%$ | 0.7497 | 1.50 | 0.2576 |
| 1.00 | 0.5152 | 0.4998 | $-2.98\%$ | 1.0304 | 2.06 | 0.3589 |
| 2.00 | 0.7178 | 0.7069 | $-1.53\%$ | 1.4356 | 2.87 | 0.5037 |
| 4.00 | 1.0074 | 0.9996 | $-0.77\%$ | 2.0148 | 4.03 | 0.7096 |

Three lessons from one table:

- The widely quoted $r=\sqrt{\lambda d/2}$ **underestimates** the zone by $11\%$
  at $d = \lambda/2$; it is a large-depth approximation.
- The *convention* matters. A one-way path difference of $\lambda/2$ gives a
  radius larger by $\sqrt{2}$; quoting "the Fresnel zone" without the convention
  is a factor-of-two error waiting to happen.
- The unmigrated horizontal resolution is the Fresnel **diameter**, between
  $1.1$ and $4.0$ wavelengths for these depths — far worse than a naive
  half-wavelength intuition.

## 4. Lateral resolution after migration

Migration collapses the diffraction hyperbola back to its apex, so the natural
measure of lateral resolution is the **width of the migrated image of a point
scatterer**. The demonstration migrates a single synthetic scatterer at
$z = 1.00\ \mathrm{m}$ with a simplified unweighted Kirchhoff sum and measures
the envelope width at half maximum along $x$:

| migration aperture | image FWHM (m) | FWHM$/\lambda$ |
|---|---|---|
| $\pm0.5\ \mathrm{m}$ | 0.475 | 0.951 |
| $\pm1.0\ \mathrm{m}$ | 0.275 | 0.550 |
| $\pm2.0\ \mathrm{m}$ | 0.225 | 0.450 |
| $\pm4.0\ \mathrm{m}$ | 0.175 | 0.350 |

The unmigrated Fresnel diameter at the same depth is $1.030\ \mathrm{m}$. Two
conclusions, both quantitative:

- With a small aperture (comparable to the depth), migration improves the width
  to about the Fresnel diameter but no further.
- With a large aperture the width falls to a floor set by the **temporal
  bandwidth**, about a third of a wavelength here. The aperture, not the
  frequency alone, is the limiting factor in the middle of this range.

A caution that belongs in any resolution claim: two scatterers separated by
$0.50\lambda$ give a midpoint-to-target envelope ratio of $0.538$, while
$1.50\lambda$ gives $0.008$. The two images interfere **coherently**, so that
ratio is not a monotone measure of separation. Quoting a point-spread width plus
the aperture and the band is honest; quoting a single "resolution" is not.

## 5. Spatial sampling and aliasing

A dipping event in a zero-offset section has time dip
$\mathrm{d}t/\mathrm{d}x = 2\sin\theta/v$, hence spatial wavenumber
$k_x = 2\omega\sin\theta/v$. The Nyquist condition $|k_x| \le \pi/\Delta x$ gives

$$\boxed{\;\sin\theta_{\max} = \frac{v}{4f\,\Delta x} = \frac{\lambda}{4\Delta x}\;}
\tag{5.1}$$

so $\Delta x \le \lambda/4$ records **every** dip and $\Delta x = \lambda/2$
records dips up to $30^\circ$. When the sampling is too coarse the apparent dip
is the true one wrapped into the Nyquist band:

$$\sin\theta_{\text{app}} = \sin\theta - m\,\frac{\lambda}{2\Delta x},
\qquad m \text{ chosen so that } |\sin\theta_{\text{app}}| \le
\frac{\lambda}{4\Delta x}. \tag{5.2}$$

**Worked example 1.** With $\lambda = 0.4996\ \mathrm{m}$ (the medium of this
lesson) and $\Delta x = \lambda/2 = 0.2498\ \mathrm{m}$: (5.1) gives
$\sin\theta_{\max} = 0.5$, i.e. $30.00^\circ$, and a $45^\circ$ event wraps to

$$\sin\theta_{\text{app}} = 0.7071 - 1.0000 = -0.2929
\;\Longrightarrow\; \theta_{\text{app}} = -17.03^\circ.$$

Measuring the adjacent-trace lag of a synthetic narrow-band $45^\circ$ event at
that spacing gives a lag of $-1.425\ \mathrm{ns}$ where the true lag would be
$+3.536\ \mathrm{ns}$ — beyond half a period ($2.500\ \mathrm{ns}$), so the
measurement is modulo the period — and an apparent dip of $-16.56^\circ$, against
the predicted $-17.03^\circ$ (a difference of $0.0079$ in $\sin\theta$).

The event has not moved. It has been sampled too coarsely, and the sign of the
apparent dip is now a property of the acquisition grid. This is why line spacing
and trace spacing are chosen from the shortest wavelength and the steepest
expected dip — see
[02-01 Survey Design](../02-gpr-acquisition-and-processing/01-gpr-survey-design.md)
— and why the same aliased dip appears in the 3-D case as a rotated time slice in
[02-04 3-D GPR Imaging and Time Slices](../02-gpr-acquisition-and-processing/04-gpr-3d-imaging.md).

## 6. Assumptions and regime of validity

1. **Horizontal, constant-velocity medium** for every number in this lesson. A
   velocity gradient changes both the Fresnel geometry and the migration
   operator.
2. **Zero-offset (monostatic) geometry.** With a finite offset the resolution
   perpendicular to the travel direction is the same but the footprint is
   asymmetric.
3. **A Ricker-like, zero-phase, broad-band wavelet.** Resolution scales with the
   band, not with a labelled frequency; a narrow-band source with the same $f_0$
   resolves less.
4. **Small contrasts**, so that single-scattering and the convolutional model
   apply; strong contrasts generate multiples that masquerade as deeper events.
5. **The migration is simplified** (unweighted Kirchhoff, no obliquity or
   aperture weighting) and is applied with the *correct* velocity. Real
   migrations with a wrong velocity are strictly worse; that is quantified in
   [02-02 Processing Steps](../02-gpr-acquisition-and-processing/02-gpr-processing.md).
6. **Noise-free, or a stated threshold.** Every detection statement in this
   lesson names its threshold. Resolution statements do not need one; resolution
   is a property of the band.

## 7. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| resolution (vertical) | m | $\lambda \times$ a pure number |
| Fresnel radius | m | $\sqrt{\mathrm{m}\times\mathrm{m}}$ |
| wavenumber $k_x$ | $\mathrm{rad\,m^{-1}}$ | $2\omega\sin\theta/v$ |
| Nyquist limit | $\mathrm{rad\,m^{-1}}$ | $\pi/\Delta x$ |
| $\sin\theta_{\max}$ | 1 | $v/(4f\Delta x)$ |

The cleanest check on any resolution claim is that it comes out in metres as a
pure multiple of the wavelength, with the multiple stated.

## 8. Python demonstration

`code/gpr_resolution_demo.py` prints every number above and:

1. scans the $0.9$-of-maximum Rayleigh criterion on a doublet and reports the
   first resolved separation in metres, wavelengths and nanoseconds;
2. builds the thin-bed tuning curve, fits the linear thin-bed slope, and solves
   for the thickness detectable at a chosen amplitude threshold;
3. compares the exact, approximate and half-amplitude Fresnel radii and their
   errors;
4. migrates a synthetic point scatterer at four apertures and measures the
   envelope width of the image, then shows the coherent-interference caveat for
   two scatterers;
5. predicts and measures the aliased apparent dip of a $45^\circ$ event at
   $\Delta x = \lambda/2$;
6. verifies the migrated apex position ($0.00\ \mathrm{cm}$ error in this
   noise-free test) and reports the image width in both directions
   ($0.175\ \mathrm{m}$ lateral, $0.300\ \mathrm{m}$ vertical).

## Mastery checkpoint

Without notes:

> A $400\ \mathrm{MHz}$ survey images a target at $1.0\ \mathrm{m}$ depth in a
> medium with $v = 0.07495\ \mathrm{m\,ns^{-1}}$.
> **(a)** Compute $\lambda$, $\lambda/4$ and $\lambda/8$.
> **(b)** A colleague reports resolving two reflectors $0.05\ \mathrm{m}$ apart.
> State what must be true for that claim to be credible, and compute the
> resolution limit for the Rayleigh-type criterion used here.
> **(c)** Compute the first Fresnel zone radius at that depth and state your
> convention.
> **(d)** Compute the maximum unaliased dip for a trace spacing of
> $0.10\ \mathrm{m}$, and the apparent dip of a $40^\circ$ event.
> **(e)** State which single change to the acquisition would most improve the
> lateral resolution at the same frequency, and why.

Parts (a)–(e) are worked in
[`exercises/05-gpr-resolution-solutions.md`](./exercises/05-gpr-resolution-solutions.md).

## Common pitfalls

1. **Quoting a resolution without its criterion.** A third of a wavelength of
   disagreement between reasonable criteria is normal.
2. **Counting the wavelet's sidelobes as signal.** A Ricker has sidelobes at
   $0.446$ of the main lobe; without a height threshold, every pulse "resolves"
   twice.
3. **Confusing detection with resolution.** A $0.0023\ \mathrm{m}$ layer is
   detectable and utterly unresolvable in the same model.
4. **Using $\sqrt{\lambda d/2}$ deep and shallow alike.** The approximation is
   $11\%$ low at $d = \lambda/2$.
5. **Forgetting the convention in the Fresnel radius.** One-way versus two-way
   path difference changes the radius by $\sqrt{2}$.
6. **Treating two close migrated images as independent.** They interfere
   coherently, so amplitudes between them are not monotone in separation.
7. **Aliased dips believed as geology.** At $\Delta x = \lambda/2$ a $45^\circ$
   event appears to dip the *other* way.

## Related modules

- [03 Attenuation, Penetration Depth and Frequency Trade-Offs](03-gpr-attenuation-penetration.md) —
  the other side of the same frequency decision.
- [04 Antennas: Frequency, Shielding, Polarisation and Offsets](04-gpr-antennas.md) —
  the footprint this lesson's Fresnel zone resembles and should not be confused
  with.
- [02-01 Survey Design: Profile, Grid, CMP and Transillumination](../02-gpr-acquisition-and-processing/01-gpr-survey-design.md).
- [02-02 Processing Steps: Dewow, Gain, Filtering, Migration](../02-gpr-acquisition-and-processing/02-gpr-processing.md) —
  what is done to the data before any resolution claim is made.
- [02-03-09 Diffraction, Scattering and Resolution Limits](../../02-physics/03-oscillations-and-waves/09-diffraction.md) —
  the general wave-physics of resolution limits.
- [20-signal-processing](../../20-signal-processing/README.md) — the bandwidth
  and sampling theory underlying Sections 1 and 5.

Materials: [`code/gpr_resolution_demo.py`](./code/gpr_resolution_demo.py),
[`exercises/05-gpr-resolution-exercises.md`](./exercises/05-gpr-resolution-exercises.md),
[`exercises/05-gpr-resolution-solutions.md`](./exercises/05-gpr-resolution-solutions.md).
