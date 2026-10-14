---
id: 02-10-02
title: "Interference and Diffraction in Optical Instruments"
level: advanced
prereqs: ["02-10-01", "02-03-09", "01-11-01"]
estimated_minutes: 90
tags: [interference, diffraction, airy, resolution, gratings, coherence]
---

# Interference and Diffraction in Optical Instruments

A lens focuses a plane wave to a spot, and the spot is not a point. The width of
that spot is the resolution limit of every optical instrument that has ever been
built, and it is set by wave physics, not by manufacturing quality. This lesson
derives it, computes it, and connects it to the two places it decides a
geophysical measurement: the pixel size of a satellite imager and the coherence
budget of a fibre interferometer.

The results, in the order the lesson builds them:

| Result | Statement | Geophysical identity |
|---|---|---|
| Fringe spacing | $\Delta y = \lambda L/d$ | The interferometer as a displacement sensor |
| Single-slit minima | $a\sin\theta = m\lambda$ | Beam divergence of any apertured transmitter |
| Airy pattern | First zero at $2\pi a\sin\theta/\lambda = 3.8317$ | The resolution limit of any circular aperture |
| Rayleigh criterion | $\theta_{\min} = 1.2197\,\lambda/D$ | Ground sample distance of an imager |
| Grating/etalon | $\mathcal{R} = mN$; $\mathcal{R} = mF$ | Spectral resolution of a spectrometer |
| Coherence length | $l_c = \lambda^2/\Delta\lambda$ | Whether a fibre interferometer can work at all |

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the two-slit fringe spacing and state the conditions on coherence
   that make fringes visible.
2. **Derive** the Fraunhofer diffraction integral for a one-dimensional aperture
   and obtain the single-slit minima $a\sin\theta = m\lambda$.
3. **Obtain** the Airy pattern from the circular-aperture integral, show that it
   reduces to $2J_1(q)/q$, and verify the zeros $3.8317$ and $7.0156$
   numerically.
4. **Compute** the resolution limit $\theta_{\min} = 1.2197\lambda/D$ for a
   telescope, a satellite imager and the eye, and convert it into a ground
   sample distance.
5. **Decide** whether an instrument is diffraction-limited or pixel-limited, and
   compute the f-number at which the crossover occurs.
6. **Compute** the reflectance of a quarter-wave antireflection coating and the
   residual reflectance of a real coating index.
7. **Compute** the resolving power of a diffraction grating and of a
   Fabry–Perot etalon, and explain the free spectral range that limits the
   etalon.
8. **Compute** a coherence length and state what it forbids.

## Prerequisites

- [02-10-01 Geometrical Optics, Refraction and Lenses](./01-geometrical-optics.md)
  — the thin-lens equation, the plate scale $f$, and the Fresnel reflectance that
  makes coatings necessary.
- [02-03-09 Diffraction, Scattering and Resolution Limits](../03-oscillations-and-waves/09-diffraction.md)
  — the same physics for elastic waves, including Fresnel zones and the
  resolution of a seismic survey.
- [01-11-01 Complex Numbers, Polar Form and Argand Diagrams](../../01-mathematics/11-complex-analysis/01-complex-arithmetic.md)
  — complex amplitudes, the phasor addition used throughout.

## 1. Superposition and the two-slit experiment

### 1.1 Interference of two monochromatic waves

Two scalar waves of the same frequency with complex amplitudes $A_1$ and $A_2$
superpose to give an intensity

$$I = |A_1 + A_2|^2 = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\delta , \tag{1}$$

where $\delta$ is the phase difference. The third term is the interference term;
for equal amplitudes, $I = 2I_0(1+\cos\delta) = 4I_0\cos^2(\delta/2)$, and the
visibility is 1.

For two slits separated by $d$ observed at distance $L$ with $L \gg d$, the path
difference is $d\sin\theta \approx dy/L$, so

$$\delta = \frac{2\pi d}{\lambda}\frac{y}{L}
\qquad\Longrightarrow\qquad
\Delta y = \frac{\lambda L}{d} . \tag{2}$$

Equation (2) is the working equation of every two-beam interferometer. In a
Michelson configuration, where the light traverses one arm twice, changing that
arm's length by $\lambda/2$ advances the whole pattern by one fringe — so a fringe
count is a displacement measured in half-wavelengths. The demo computes:

```text
  slit separation d (mm)   fringe spacing (mm)    fringes per mm
                    0.10               12.6560            0.0790
                    0.25                5.0624            0.1975
                    0.50                2.5312            0.3951
                    1.00                1.2656            0.7901
                    2.00                0.6328            1.5803
```

With $\lambda = 632.8$ nm one fringe corresponds to 316.4 nm of path difference,
and a fringe position can be measured to a thousandth of a fringe. That ratio,
$\sim 0.3$ nm out of a metre-scale apparatus, is why interferometry is the most
precise length measurement available and why it underpins both gravitational-wave
detection and fibre strain sensing.

### 1.2 Coherence: when the fringes vanish

Interference requires the two waves to be mutually coherent. Two limits matter:

- **Temporal coherence** is set by the source bandwidth. A source spanning
  $\Delta\lambda$ loses coherence over a path difference

$$l_c \approx \frac{\lambda^2}{\Delta\lambda} . \tag{3}$$

- **Spatial coherence** is set by the source size: an extended source washes out
  fringes unless it subtends less than $\lambda/d$ at the two slits.

The demo's computed coherence lengths:

```text
source                        lambda (nm)  dlambda (nm)           l_c
He-Ne laser (nominal)               632.8         0.002    200.218 mm
mercury green line                  546.1         0.050      5.965 mm
white light, visible                550.0       300.000      1.008 um
LED, 20 nm FWHM                     850.0        20.000     36.125 um
broadband lamp                     1000.0       500.000      2.000 um
```

Sunlight has a coherence length of about one micrometre, i.e. two wavelengths.
This single number forbids white-light fibre interferometry over more than a
few wavelengths of path difference, and it is why every phase-based fibre sensor
uses a narrowband laser: a laser with 0.002 nm of bandwidth has a coherence
length of 200 mm, ample to match a whole interferometer.

### 1.3 Thin films and the antireflection coating

Two reflections from the two surfaces of a film interfere. For a film of index
$n_c$ and thickness $t$ on a substrate of index $n$, at normal incidence, the
reflectance of the coated surface is

$$R = \left(\frac{n - n_c^2}{n + n_c^2}\right)^2
\qquad\text{at}\qquad n_c t = \frac{\lambda}{4} . \tag{4}$$

This is **zero** when $n_c = \sqrt{n}$ — the *impedance-matching* condition,
identical in form to the quarter-wave matching layer of an ultrasonic transducer
or a seismic geophone. The demo computes, for $n = 1.52$ (bare glass,
$R = 4.26$ per cent):

```text
      nc           R transmission gain vs bare
    1.22     0.00011                    1.0444
    1.30     0.00280                    1.0415
    1.38     0.01260                    1.0313
    1.45     0.02586                    1.0175
    1.52     0.04258                    1.0000
    1.70     0.09651                    0.9437
    2.00     0.20185                    0.8336
```

The ideal index is 1.2329. No hard, durable material has it; MgF₂ at about 1.38
(nominal) leaves 1.26 per cent instead of 4.26 per cent, a factor of 3.4
improvement, at a design thickness of

$$t = \frac{\lambda}{4n_c} = \frac{550\ \mathrm{nm}}{4\times1.38}
= 99.64\ \mathrm{nm} . \tag{5}$$

A 2 per cent thickness error moves the reflectance minimum by about 11.0 nm —
which is why coatings are qualified on a spectrophotometer rather than with a
micrometer, and why multi-layer coatings exist: they can satisfy the
quarter-wave condition at several wavelengths simultaneously and are how an
eight-element lens transmits 99 per cent instead of 50.

## 2. Diffraction: the aperture integral

### 2.1 The Fraunhofer integral

In the far field of a plane aperture, the complex amplitude is the Fourier
transform of the aperture function:

$$A(\theta) \propto \int_{\text{aperture}} e^{-i k x \sin\theta}\,
\mathrm{d}x\,\mathrm{d}y , \qquad k = \frac{2\pi}{\lambda} . \tag{6}$$

Every result in this section is (6) evaluated for a particular aperture. This is
the optical case of the same integral that produces the Fresnel-zone and
diffraction-limit results for seismic waves in
[02-03-09](../03-oscillations-and-waves/09-diffraction.md).

### 2.2 Single slit

For a slit of width $a$, (6) gives the normalised amplitude

$$A(\sin\theta) = \frac{\sin(\pi a\sin\theta/\lambda)}{\pi a\sin\theta/\lambda}
= \operatorname{sinc}\!\left(\frac{\pi a \sin\theta}{\lambda}\right),
\tag{7}$$

with zeros at

$$\boxed{\ a\sin\theta = m\lambda\ } \qquad m = 1,2,\dots \tag{8}$$

The demo checks (8) by integrating (6) numerically over the aperture with a
4001-point Riemann sum and locating the zeros by bisection:

```text
  order m   analytic sin(theta)    numeric zero        diff
        1            0.00300000    0.0030000000    3.49e-15
        2            0.00600000    0.0060000000    3.49e-15
        3            0.00900000    0.0090000000    2.62e-15
```

```text
  The 4001-point Riemann sum over the aperture reproduces the
  magnitude of the closed form sin(x)/x to 2.66e-04 in amplitude over
  0 <= sin(theta) <= 3*lambda/a (worst at sin(theta)/ (lambda/a) =
  0.876).  A magnitude comparison is used because the field
  of a symmetric aperture is real and changes sign at each zero: the
  sum returns the magnitude, the closed form the signed amplitude.
  The located zeros agree with m*lambda/a to the precision of the
  bisection, which is what the exercise asks you to verify.
```

Two points of method, because this curriculum insists on them. First, the zeros
agree with (8) to $3\times10^{-15}$, i.e. to the precision of the bisection —
the numerical result *confirms* the algebra but cannot *prove* it. Second, the
quadrature's own amplitude error is $2.7\times10^{-4}$, and the zero-finding is
only as trustworthy as the function it is given; reporting the zero to fifteen
digits without reporting the quadrature error would be a claim the method cannot
support.

The angular half-width of the central maximum is $\arcsin(\lambda/a)$; with
$a = 0.20$ mm and $\lambda = 600$ nm the demo gives 0.171888°. Halving the slit
doubles the width: **a smaller aperture makes a broader beam**. This is why a
small loudspeaker is not directional, why a small radar dish cannot resolve
anything, and why astronomical interferometry synthesises a large aperture from
separated telescopes instead of building one big mirror.

### 2.3 Circular aperture: the Airy pattern

For a circular aperture of radius $a$ the integral (6) reduces to a Bessel
integral. Writing $q = 2\pi a\sin\theta/\lambda$, the normalised amplitude is

$$A(q) = \frac{2J_1(q)}{q} , \qquad
I(q) = \left(\frac{2J_1(q)}{q}\right)^2 . \tag{9}$$

The demo never calls a Bessel function. It integrates the aperture directly,
using the chord integral

$$A \propto \int_{-a}^{a} \frac{\sin\!\big(k\,s\sqrt{a^2-y^2}\big)}{k\,s}\,
\mathrm{d}y , \qquad s = \sin\theta , \tag{10}$$

and locates the zeros by bisection:

```text
  zero     q numeric    q textbook      |diff|     sin(theta)  theta (arcsec)
     1      3.831650      3.831706    5.63e-05   0.0000022360            0.46
     2      7.015725      7.015587    1.38e-04   0.0000040942            0.84
```

The first zero of $J_1$ is 3.831705970 and the second is 7.015586670; the
quadrature reproduces them to the precision of its own 2001-point sum. This is
the numerical verification the syllabus demands: **the aperture integral is the
Bessel function**, and no special function is needed to obtain it.

The **Rayleigh criterion** places two point sources just resolvable when the
central maximum of one falls on the first zero of the other:

$$\boxed{\ \theta_{\min} = \frac{3.8317}{\pi}\frac{\lambda}{D}
= 1.219670\,\frac{\lambda}{D}\ } \tag{11}$$

with $D = 2a$ the aperture diameter. The demo computes the coefficient:

```text
  Rayleigh coefficient C = 3.831705970/pi = 1.2196699, so the
  textbook 1.22 is a rounding of 1.2197: a 0.027 per cent
  error if you use 1.22 in a calibration.
```

For a slit rather than a disk the coefficient is 1.0 rather than 1.2197 — the
constant is a property of the aperture shape, not of nature. The same
aperture-shape dependence appears in the seismic Fresnel-zone expression.

## 3. What the resolution limit means for an instrument

```text
system                                 D (m)     theta (rad)  theta (arcsec)
eye, dark-adapted pupil                0.007      9.5831e-05          19.767
eye, bright pupil                     0.0025      2.6833e-04          55.346
amateur telescope                        0.2      3.3541e-06           0.692
survey telescope                           1      6.7082e-07           0.138
large telescope                          8.2      8.1807e-08           0.017
satellite imager                         0.3      2.2361e-06           0.461
```

Read the first two rows together: a dark-adapted pupil resolves about 20 arcsec
and a bright pupil about 55 arcsec. The human eye's *physiological* limit is
about 60 arcsec (1 arcmin, the classical value used in charts), so the eye is
marginally diffraction-limited when dark-adapted and *pupil-limited* in
daylight — which is why you can see better resolution at night, and why the
physiological limit quoted in textbooks is a compromise between the two rows.

The same number expressed as a ground sample distance (GSD) from 700 km:

```text
   D (m)     theta (rad)   diffraction GSD (m)
    0.10      6.7082e-06                4.6957
    0.30      2.2361e-06                1.5652
    0.50      1.3416e-06                0.9391
    1.00      6.7082e-07                0.4696
```

A 0.30 m aperture at 700 km is diffraction-limited at 1.565 m. A nominal 10 m
multispectral product is therefore **not** diffraction-limited: its GSD is set by
the detector pixels and the swath width, and the aperture has resolution in
reserve. That is the standard design trade for a wide-swath imager, and it is why
a panchromatic band can be sharper than the multispectral bands of the same
instrument — the pixel, not the aperture, is the limit. Conversely, a
high-resolution pointing imager with a 1 m aperture is diffraction-limited at
0.47 m from the same altitude.

### 3.1 Diffraction-limited or pixel-limited?

An instrument is diffraction-limited when the diffraction blur is larger than
the detector pixel. Diffraction blurs by $1.22\lambda F$ with $F = f/D$ the
f-number, and the pixel samples at pitch $p$, so diffraction dominates when

$$1.22\lambda F > p
\qquad\Longleftrightarrow\qquad
F > \frac{p}{1.22\lambda} \approx \frac{2p}{\lambda} . \tag{12}$$

```text
  pixel pitch p (um)  lambda (nm)   F above which diffraction dominates
                 1.0          450                                   4.4
                 1.0          550                                   3.6
                 2.0          450                                   8.9
                 2.0          550                                   7.3
                 4.0          450                                  17.8
                 4.0          550                                  14.5
                 8.0          450                                  35.6
                 8.0          550                                  29.1
```

A 4 µm pixel at 550 nm is diffraction-limited beyond f/14.5, which is the
computed form of the photographer's rule that a lens stops improving past about
f/16. A 1 µm pixel is diffraction-limited beyond f/3.6: small-pixel sensors
become diffraction-limited almost immediately, and **smaller pixels buy
sampling, not resolution**.

## 4. Spectral resolution: gratings and etalons

A diffraction grating with groove spacing $d$ satisfies

$$d(\sin\theta_i + \sin\theta_m) = m\lambda , \qquad
\mathcal{R} = \frac{\lambda}{\Delta\lambda} = mN , \tag{13}$$

with $N$ the number of illuminated grooves. The demo computes:

```text
  grooves/mm  width (mm)    m         N           R  dlambda (pm)
         600          50    1     30000       30000        16.667
         600          50    2     30000       60000         8.333
        1200          50    1     60000       60000         8.333
        1200         100    1    120000      120000         4.167
        1800          50    1     90000       90000         5.556
```

A 1200 groove mm⁻¹, 50 mm grating in first order resolves $6\times10^4$, i.e.
8.33 pm at 500 nm. That is a laboratory spectrometer. A spaceborne imaging
spectrometer with 10 nm bands has $\mathcal{R} = 50$ — three orders of magnitude
less, and it can still map mineralogy, because the features of lesson
[02-10-04](./04-spectroscopy.md) are 20–100 nm wide.

A Fabry–Perot etalon is a pair of mirrors $d$ apart; its finesse and resolving
power are

$$F = \frac{\pi\sqrt{R_r}}{1-R_r}, \qquad \mathcal{R}_{\text{FP}} = mF,
\qquad m = \frac{2d}{\lambda} . \tag{14}$$

```text
  mirror R   finesse F   m (d=0.5 mm)         R_res  dlambda (fm)
      0.50        4.44           2000     8.886e+03     56269.770
      0.80       14.05           2000     2.810e+04     17794.064
      0.90       29.80           2000     5.961e+04      8388.202
      0.95       61.24           2000     1.225e+05      4082.238
      0.98      155.50           2000     3.110e+05      1607.708
```

At 98 per cent mirror reflectance a 0.5 mm etalon resolves $3.11\times10^5$,
i.e. 1.608 pm at 500 nm, far beyond any grating. What it cannot do is work
broadband: its **free spectral range** is

$$\Delta\lambda_{\text{FSR}} = \frac{\lambda^2}{2d} = 0.250\ \mathrm{nm}
\quad\text{at } \lambda = 500\ \mathrm{nm},\ d = 0.5\ \mathrm{mm}, \tag{15}$$

so orders overlap unless the input is pre-filtered. High resolution and broad
range are traded against each other by the same $d$, in etalons as in every other
resonator — the same trade-off as the free-surface multiples of a seismic
gather.

## 5. Physical interpretation

**Diffraction is what happens when a wave encounters a boundary it cannot pass
with its phase fronts intact.** The aperture is not a window through which rays
pass; it is a set of boundary conditions that truncates the field, and the
far-field pattern is the Fourier transform of that truncation. Resolution limits
are therefore not engineering failures but Fourier uncertainty relations:
confinement in $x$ to a width $a$ forces a spread in $k_x$ of order $2\pi/a$.

**The resolution limit is about information, not blur.** Two point sources
separated by less than $\theta_{\min}$ produce a pattern with no dip between the
peaks, but the *information* about their separation is still present in the
shape and can be recovered by fitting if the signal-to-noise ratio is high. The
Rayleigh criterion is a convention, not a theorem; the true limit is set by
noise, which is why
[02-03-09](../03-oscillations-and-waves/09-diffraction.md) treats resolution
versus SNR explicitly.

**Interference turns a length into a countable.** A fringe is a phase change of
$2\pi$, and phase can be measured to a small fraction of a cycle, so the
interferometer multiplies the resolution of a length measurement by
$1/(\text{fraction of a fringe})$. That multiplier is the whole of optical
metrology, and it is what makes a fibre strainmeter able to measure a strain of
$10^{-11}$ (lesson [02-10-05](./05-fiber-optics-sensing.md)).

**Coherence is the budget that pays for interference.** Every interferometer
needs the two beams to remain coherent over the path difference it imposes. A
system whose path difference exceeds $l_c$ has no fringes at all, no matter how
good its optics.

## 6. Assumptions and regime of validity

| Approximation | Statement | What breaks outside it |
|---|---|---|
| Scalar diffraction | One scalar field; polarisation ignored | High-NA systems, sub-wavelength apertures, polarisation-sensitive instruments |
| Fraunhofer (far field) | Observation distance $\gg a^2/\lambda$ | Near field: use the Fresnel integral, which is what the seismic Fresnel zone solves |
| Monochromatic | Single $\lambda$; no dispersion | Broadband imaging: chromatic aberration; broadband fringes: coherence loss |
| Infinite, perfectly conducting aperture edge | A sharp aperture in an opaque screen | Real apertures: edge roughness, finite screen thickness, surface plasmons at metal edges |
| Uniform illumination | Top-hat amplitude across the aperture | Apodised apertures change the pattern (a Gaussian beam has no rings) |
| Two-beam interference | Two paths only | Multi-beam: Fabry–Perot, thin-film stacks, and multiple reflections change the fringe shape |
| Lossless, non-absorbing film | Real index only | Absorbing coatings; a complex index changes both $R$ and the phase |
| Rayleigh criterion | Two equal incoherent point sources | Unequal sources, coherent sources, noisy data: the achievable limit differs |
| Gaussian optics for the instrument | Paraxial, aberration-free | Wide-field systems: aberrations dominate before diffraction does |
| Bandwidth-limited coherence | $\Delta\lambda$ the only limit | Source size and drift; a multimode fibre; a moving reflector |
| Ideal grating | Uniform groove spacing, no blaze limit | Real gratings have efficiency curves and ghosts |

## 7. Units and dimensional analysis

- $\delta$ in (1) is an angle in radians, dimensionless, as it must be for a
  cosine. Path differences must be converted to phase with $2\pi/\lambda$.
- $\Delta y = \lambda L/d$: $\mathrm{m}\cdot\mathrm{m}/\mathrm{m} =
  \mathrm{m}$ ✓. The ratio $\Delta y/L = \lambda/d$ is dimensionless and is
  literally the fringe angle.
- $a\sin\theta = m\lambda$: $\mathrm{m}$ on both sides ✓. Because $\sin\theta\le1$,
  the number of propagating orders is bounded by $m \le a/\lambda$ — a useful
  sanity check.
- $q = 2\pi a\sin\theta/\lambda$: dimensionless ✓, which is why the zeros of
  $J_1$ are pure numbers and the pattern is scale-invariant in $q$ alone.
- $\theta_{\min} = 1.2197\lambda/D$: $\mathrm{m}/\mathrm{m}$ = rad ✓. Converting
  to arcsec: $1\ \mathrm{rad} = 206\,264.8″$; the demo's $9.5831\times10^{-5}$
  rad is $19.767″$, which checks.
- $R = ((n-n_c^2)/(n+n_c^2))^2$: dimensionless because both terms are indices
  squared, and it has the right limit: $n_c\to0$ recovers the bare-surface
  $((1-n)/(1+n))^2$ ✓ (the demo's nc = 1.22 row gives 0.00011, near zero as the
  matching condition requires).
- $\mathcal{R} = mN$: dimensionless ✓, and it must be $\ge 1$; a computed
  resolving power below 1 means $N$ was confused with a wavelength.
- $l_c = \lambda^2/\Delta\lambda$: $\mathrm{m^2}/\mathrm{m} = \mathrm{m}$ ✓.
  A 0.002 nm bandwidth at 632.8 nm gives 200.2 mm, which is the demo's value;
  note the extreme sensitivity to $\Delta\lambda$: the same laser specified to
  0.02 nm has a coherence length of 20 mm.
- **Useful anchors:** Rayleigh coefficient 1.2197 (disk) or 1.0 (slit);
  $\lambda/D$ in radians; $1\ \mathrm{rad} = 206\,264.8″$;
  $a\sin\theta = m\lambda$; quarter-wave film thickness $\lambda/(4n_c)$.

## 8. Python demonstration

[`code/interference_diffraction_demo.py`](./code/interference_diffraction_demo.py)
computes two-slit fringes, the single-slit pattern by quadrature, the Airy
pattern by aperture integration, the resolution limits of six instruments,
antireflection coatings, grating and etalon resolving powers, and coherence
lengths. It uses the standard library only. Every number quoted in §§1–4 is its
actual output; section 7 is worth reading in full:

```text
  White light at 550 nm with 300 nm of bandwidth has l_c =
  1008.33 nm, i.e. about 1.8 wavelengths: fringes survive only
  a few wavelengths of path difference, which is why white-light
  interferometry works only in a nulled, near-zero path configuration.
  A narrowband laser has a coherence length of centimetres to metres,
  which is what makes phase-based fibre sensing (lesson 02-10-05)
  possible: the two arms of the interferometer must stay matched to
  better than l_c.
```

### What to observe

| Observation | Consequence |
|---|---|
| Fringe spacing scales as $1/d$ | The interferometer's sensitivity is set by the *baseline*, not by the optics |
| The numeric single-slit zeros equal $m\lambda/a$ to $3\times10^{-15}$ | The aperture integral is the closed form; the check is real |
| The quadrature's own amplitude error is $2.7\times10^{-4}$ | Never report more digits than the method supports |
| $q$ zeros at 3.831650 and 7.015725 versus 3.831706 and 7.015587 | The Bessel function is recovered without ever being called |
| $C = 1.2196699$, not 1.22 | A 0.027 per cent systematic error is a real calibration offset |
| Eye: 20″ dark-adapted, 55″ in daylight | The "1 arcmin" physiological limit is a compromise between two physics limits |
| 0.30 m aperture at 700 km: 1.565 m | A 10 m product is pixel-limited, not diffraction-limited |
| 4 µm pixel at 550 nm: diffraction-limited beyond f/14.5 | The photographer's f/16 rule is a computed result |
| MgF₂ coating: 1.26 per cent instead of 4.26 per cent | One layer is a factor 3.4; more layers approach zero |
| 1200 groove/mm grating: 8.33 pm at 500 nm; etalon 1.608 pm | Three orders of magnitude separate a field and a laboratory instrument |
| White light $l_c = 1.008\ \mu$m | Two wavelengths: white-light fringes exist only near zero path difference |

> **Breaking exercise.** Before running anything, predict the GSD at 500 km for
> a 0.25 m aperture, and the f-number at which a 3.45 µm pixel at 700 nm becomes
> diffraction-limited. Then change the constants in the demo and check both.
> Finally: the demo's Airy zeros were located by integrating the aperture on a
> 2001-point grid. Predict what happens to the located zeros if the grid is
> halved, and test it.

## 9. Common mistakes

1. **Using 1.22 as if it were exact.** It is 1.2196699; the difference is small
   but it is systematic, and calibration is where small systematic errors matter.
2. **Applying the disk constant to a slit.** The coefficient is 1.0 for a slit
   and 1.2197 for a circular aperture; it is a property of the aperture.
3. **Confusing resolution with detectability.** Below $\theta_{\min}$ two sources
   are still distinguishable at high SNR; Rayleigh is a convention.
4. **Assuming a satellite's GSD equals its diffraction limit.** Usually the
   pixel and swath set the GSD and the aperture has resolution in reserve.
5. **Thinking a larger aperture makes a wider beam.** For a *transmitter*, a
   larger aperture makes a narrower beam; for a camera, a larger aperture
   increases resolution and reduces depth of field. The two roles are easy to
   mix up in a system budget.
6. **Forgetting the Nyquist sampling condition on the focal plane.** A pixel
   coarser than $\lambda F/2$ discards the resolution the aperture delivered.
7. **Designing a quarter-wave coating without the index constraint.** The
   thickness condition and the index condition are both required; a
   quarter-wave film of the wrong index can make reflectance *worse* (the
   nc = 2.00 row of §1.3).
8. **Quoting an etalon's resolution without its free spectral range.** High
   finesse is useless in a broadband instrument if orders overlap.
9. **Assuming coherence is free.** A path difference larger than
   $\lambda^2/\Delta\lambda$ gives no fringes; this is the first thing to check
   when an interferometer "does not work".
10. **Reporting numerical zeros without the quadrature error.** The located zero
    is only as good as the function the solver is evaluating.

## 10. Real-world applications

- **Satellite imaging.** $\theta_{\min} = 1.2197\lambda/D$ sets the resolution
  floor of every optical imager; the achievable GSD follows from the altitude
  and is then traded against swath and pixel size
  ([17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md)).
- **Spectrometer design.** Grating and etalon resolving power set the band count
  of an imaging spectrometer; $mN$ and $mF$ are the design equations
  ([02-10-04](./04-spectroscopy.md)).
- **Fibre interferometry and DAS.** Coherence length sets the allowable path
  mismatch and hence the laser specification of every phase-based fibre
  interrogator ([02-10-05](./05-fiber-optics-sensing.md)).
- **Lidar and laser ranging.** The beam divergence of the transmitter is
  $\sim\lambda/D$ from §2.2, which sets the footprint on the ground from
  satellite or airborne altitude.
- **Optical coatings.** Antireflection, high-reflectance and bandpass filters are
  thin-film interference devices designed with (4); they set the throughput and
  the stray-light performance of every instrument.
- **Seismic and GPR analogue.** The same Fresnel-zone geometry governs the
  lateral resolution of a seismic migration and of a GPR survey
  ([02-03-09](../03-oscillations-and-waves/09-diffraction.md),
  [10 GPR and Near-Surface](../../10-gpr-near-surface/README.md)).
- **Precision metrology.** Interferometric displacement measurement underlies
  laser strainmeters, tiltmeters and the calibration of seismometers.

## 11. Further reading

- **Hecht, E. *Optics* (5th ed., Pearson).** Interference, coherence, thin
  films, Fraunhofer diffraction and gratings at the undergraduate level, with
  the Airy derivation. Level: intermediate.
- **Born, M., & Wolf, E. *Principles of Optics* (7th ed., Cambridge University
  Press).** The rigorous scalar and vector diffraction theories, the Debye
  integral, and the exact treatment of resolution. Level: advanced.
- **Goodman, J. W. *Introduction to Fourier Optics* (4th ed., W. H. Freeman).**
  The aperture integral as a Fourier transform, transfer functions and the
  imaging chain. Level: advanced.
- **Vaughan, J. M. *The Fabry-Perot Interferometer* (Adam Hilger).** Etalon
  theory, finesse, free spectral range and practical alignment. Level: graduate.
- **den Dekker, A. J., & van den Bos, A. (1997), "Resolution: a survey",
  *Journal of the Optical Society of America A*.** Why the resolution limit is
  a statistical statement, not a geometric one. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [02-10-01 Geometrical Optics, Refraction and Lenses](./01-geometrical-optics.md)
  — the ray picture that this lesson shows is incomplete.
- [02-03-09 Diffraction, Scattering and Resolution Limits](../03-oscillations-and-waves/09-diffraction.md)
  — the same physics for elastic waves, with the SNR discussion.
- [02-10-03 Radiative Transfer, Blackbody Radiation and Kirchhoff's Law](./03-radiative-transfer.md)
  — what the light is, once the instrument has resolved it.
- [02-10-04 Spectroscopy Principles for Remote Sensing](./04-spectroscopy.md)
  — the spectral resolution that $\mathcal{R}$ describes.
- [02-10-05 Fibre-Optic Sensing and Distributed Acoustic Sensing](./05-fiber-optics-sensing.md)
  — where coherence length becomes a hard engineering constraint.
- [02-03-10 Attenuation and Anelasticity](../03-oscillations-and-waves/10-attenuation.md)
  — the wave analogue of the losses that make coatings necessary.

Exercises:
[`exercises/02-interference-diffraction-optics-exercises.md`](./exercises/02-interference-diffraction-optics-exercises.md)
and
[`exercises/02-interference-diffraction-optics-solutions.md`](./exercises/02-interference-diffraction-optics-solutions.md).

## Self-assessment checklist

- [ ] I can derive $\Delta y = \lambda L/d$ and explain the half-wavelength
      displacement-per-fringe rule. (§1.1)
- [ ] I can compute a coherence length and state what path difference it
      prohibits. (§1.2)
- [ ] I can compute the reflectance of a quarter-wave coating and explain why
      the ideal index is $\sqrt{n}$. (§1.3)
- [ ] I can derive the single-slit minima from the aperture integral and check
      them numerically. (§2.2)
- [ ] I can obtain the Airy pattern and verify the zeros 3.8317 and 7.0156.
      (§2.3)
- [ ] I can compute $\theta_{\min}=1.2197\lambda/D$ for a given aperture and
      convert it into a ground sample distance. (§3)
- [ ] I can decide whether an instrument is diffraction-limited or pixel-limited
      and compute the crossover f-number. (§3.1)
- [ ] I can compute a grating or etalon resolving power and its free spectral
      range. (§4)
- [ ] I can state the validity conditions of the Fraunhofer and scalar
      treatments. (§6)
