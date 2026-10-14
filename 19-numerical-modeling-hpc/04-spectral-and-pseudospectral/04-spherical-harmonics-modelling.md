---
id: 19-04-04
title: "Spherical Harmonic Modelling of Global Fields"
level: research
prereqs: ["19-04-01", "01-10-07", "12-01-01"]
tags: [numerical-modelling, spherical-harmonics, geodesy, global-fields, downward-continuation, numerical-modelling]
---

# Spherical Harmonic Modelling of Global Fields

**All models and data in this module are SYNTHETIC.** The coefficient sets below
are drawn at random from chosen models; the reference values are exact
mathematical identities (orthonormality, Parseval) or numbers this demonstration
measures.

## Learning objectives

By the end of this lesson you will be able to:

1. **Implement** fully normalised associated Legendre functions by their
   recurrence and **verify** orthonormality of the resulting harmonics by
   quadrature.
2. **State** the Gauss-Legendre latitude quadrature a band-limited field requires,
   and **measure** what happens below it.
3. **Synthesise** a field from coefficients and **analyse** it back, and
   **verify** Parseval's identity to round-off.
4. **Compute** a degree-variance spectrum from coefficients and from samples, and
   **check** that they agree.
5. **Derive** the downward-continuation amplification factor and **compute** the
   degree at which it destroys a field given a stated data error.
6. **Explain** why a band limit is a hard constraint and not a resolution
   preference.
7. **State** what a spherical harmonic model of a global field does and does not
   determine.

## Prerequisites

- [19-04-01 Spectral Methods: Basis Choice and Exponential Convergence](01-spectral-methods.md) —
  basis choice as a modelling decision.
- [01-10-07 Two-Dimensional Fourier Analysis and Wavenumber Filtering](../../01-mathematics/10-fourier-analysis/07-2d-fourier.md) —
  the Cartesian analogue of a two-dimensional spectral basis.
- [12-01-01 PREM and Reference Earth Models](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/01-prem-and-reference-models.md) —
  where a global model's degrees come from.

## 1. Why a sphere needs its own basis

A Fourier series is the right basis for a periodic interval because its
functions satisfy the same boundary condition the geometry imposes. A sphere
imposes a different structure: the domain is closed, there is no boundary, and
every direction is equivalent. The basis that respects this is the **spherical
harmonics** $Y_{lm}(\theta,\varphi)$, eigenfunctions of the surface Laplacian with
eigenvalue $-l(l+1)$.

In the fully normalised convention used in geodesy and geomagnetism,

$$\frac{1}{4\pi}\int_{\Omega} Y_{a}Y_{b}\,\mathrm{d}\Omega = \delta_{ab},
\qquad
Y_{l0} = P_{l0}(\cos\theta), \qquad
Y_{lm}^{\cos} = P_{lm}(\cos\theta)\cos m\varphi, \tag{1.1}$$

where $P_{lm}$ are the normalised associated Legendre functions. Two conventions
are in common use and they differ by factors of $\sqrt{2l+1}$; the rest of this
lesson uses (1.1) and states what that choice implies. A real field is expanded
as

$$f(\theta,\varphi) = \sum_{l=0}^{L}\sum_{m=-l}^{l} f_{lm}\,Y_{lm},
\qquad Y_{l,-m} = P_{lm}(\cos\theta)\sin m\varphi . \tag{1.2}$$

### 1.1 Implementing the Legendre functions stably

The recurrence that matters in practice is on the normalised functions, not the
classical ones, because $P_{lm}$ for high $l$ overflows double precision when
computed conventionally. The demonstration builds them with the standard
sectoral and vertical recurrences, then verifies the result against (1.1) by
quadrature rather than against another implementation. Measured for $l \le 6$
(49 harmonics) with 7 latitude nodes and 14 longitude samples:

$$\max\left|\text{Gram} - I\right| = 4.2\times10^{-15}. \tag{1.3}$$

Round-off. This is the check to make first: a normalisation error of
$\sqrt{2l+1}$ in a factor is invisible in a synthesised picture and fatal to a
coefficient estimate.

## 2. Quadrature: the band limit is exact, not approximate

A field band-limited to degree $L$ is integrated exactly by **$L+1$
Gauss-Legendre nodes in latitude** and at least $2L+1$ equispaced samples in
longitude. The demonstration analyses a degree-8 field with a varying number of
latitude nodes:

| $n_{\rm lat}$ | required | max coefficient error |
|---|---|---|
| 4 | 9 | $2.087\times10^{0}$ |
| 6 | 9 | $6.329\times10^{-1}$ |
| 8 | 9 | $1.104\times10^{-1}$ |
| 9 | 9 | $6.134\times10^{-15}$ |
| 12 | 9 | $6.203\times10^{-15}$ |
| 16 | 9 | $2.068\times10^{-15}$ |

Below $L+1$ nodes the coefficients are wrong by factors of order unity; at $L+1$
and above the error is round-off, not merely small. There is no gradual
degradation to tune against, for the same reason as the Nyquist limit of lesson
[02](02-pseudospectral.md): the product of two degree-$L$ harmonics has degree
$2L$, and a rule that cannot integrate it folds power between degrees.

The practical consequence is the same as in one dimension and worth stating
plainly: **the number of data points a global model needs is set by its
resolution and by nothing else.** A "$1^\circ$ model" and a "$0.5^\circ$ model"
that are quoted without their maximum degree are not specified.

## 3. Synthesis and analysis are inverse, and Parseval closes

From a random degree-4 coefficient set with the mean removed, the demonstration
synthesises the field on the quadrature grid and analyses it back:

- $\max|f_{lm}^{\rm analysed} - f_{lm}^{\rm synthesised}| = 4.0\times10^{-15}$;
- $\frac{1}{4\pi}\int_\Omega f^2\,\mathrm{d}\Omega = 31.421635044902$;
- $\sum_{lm} f_{lm}^2 = 31.421635044902$;
- difference $= +1.1\times10^{-14}$.

The two agree because the quadrature is exact for the band used. **Parseval is a
measurement that closes exactly or not at all** — a small discrepancy in an
otherwise correct-looking expansion is a symptom of a sampling or normalisation
error, not of numerical noise to be averaged away.

## 4. Power spectra, from coefficients and from samples

The degree variance of a global field is

$$\sigma_l^2 = \frac{1}{2l+1}\sum_{m=-l}^{l} f_{lm}^2, \tag{4.1}$$

and it is the standard way to summarise how a field's energy is distributed in
scale. The demonstration builds a synthetic coefficient set with
$f_{lm} \propto l^{-2}$ up to $l = 60$, synthesises it on the exact quadrature
grid, analyses it back, and compares the two spectra:

| $l$ | $\sigma_l$ (model) | $\sigma_l$ (analysed) | relative difference |
|---|---|---|---|
| 1 | $9.693146\times10^{-1}$ | $9.693146\times10^{-1}$ | $-3.4\times10^{-15}$ |
| 2 | $2.502662\times10^{-1}$ | $2.502662\times10^{-1}$ | $+2.4\times10^{-15}$ |
| 10 | $1.052527\times10^{-2}$ | $1.052527\times10^{-2}$ | $-7.9\times10^{-15}$ |
| 20 | $2.904477\times10^{-3}$ | $2.904477\times10^{-3}$ | $-6.3\times10^{-14}$ |
| 40 | $5.935201\times10^{-4}$ | $5.935201\times10^{-4}$ | $+2.7\times10^{-13}$ |
| 60 | $2.631171\times10^{-4}$ | $2.631171\times10^{-4}$ | $+1.2\times10^{-13}$ |

Total power: model $1.018744853\times10^{0}$, analysed $1.018744853\times10^{0}$,
difference $-2.9\times10^{-15}$. The fitted log-log exponent of the power
spectrum over $l = 1\dots60$ is $-4.011$, as the $\sigma_l \propto l^{-2}$
amplitude model predicts. The point of the exercise is that **the spectrum is a
measurement from the coefficients, and it can be recovered from samples** — the
two routes agree to round-off when the sampling is adequate and not otherwise
(Section 2).

Note the growth of the relative difference with $l$: $-3\times10^{-15}$ at $l=1$,
$+2.7\times10^{-13}$ at $l=40$. That growth is the conditioning of the analysis
at high degree, and it is the first hint of the instability that Section 5 turns
into a hard limit.

## 5. Downward continuation: an exact factor with an inexact outcome

A potential field measured on a sphere of radius $r$ is continued to radius $R$
by multiplying each degree by $(r/R)^l$:

$$f_{lm}(R) = \left(\frac{r}{R}\right)^{l} f_{lm}(r), \qquad R < r . \tag{5.1}$$

The factor is exact and it is the source of the method's power — and of its
instability. Measured:

| $l$ | $(r/R)^l$, $r/R = 1.01$ | $r/R = 1.05$ | $r/R = 1.10$ |
|---|---|---|---|
| 10 | $1.105\times10^{0}$ | $1.629\times10^{0}$ | $2.594\times10^{0}$ |
| 50 | $1.645\times10^{0}$ | $1.147\times10^{1}$ | $1.174\times10^{2}$ |
| 100 | $2.705\times10^{0}$ | $1.315\times10^{2}$ | $1.378\times10^{4}$ |
| 200 | $7.316\times10^{0}$ | $1.729\times10^{4}$ | $1.899\times10^{8}$ |
| 500 | $1.448\times10^{2}$ | $3.932\times10^{10}$ | $4.970\times10^{20}$ |

At $l = 200$ with $r/R = 1.10$ the factor is $1.899\times10^{8}$: a coefficient
known to a relative $10^{-6}$ becomes known to a relative $1.9\times10^{2}$ —
190 times the field's own amplitude. **Downward continuation at that degree is
worthless without far better data**, and the factor says exactly how much better.

### 5.1 The useful form of the same statement

The factor's real content is that it fixes where to stop. Requiring the
amplified error to stay below a target $\eta$ gives a maximum usable degree

$$l_{\max} = \frac{\log(\eta/\epsilon)}{\log(r/R)}, \tag{5.2}$$

where $\epsilon$ is the relative coefficient error. Measured for a target
$\eta = 10^{-3}$ and $\epsilon = 10^{-6}$: $l_{\max} = 694.2$ for $r/R = 1.01$,
$348.8$ for $1.02$ and $141.6$ for $1.05$. That is why a satellite-derived field at
$r \approx 1.05R$ supports a much higher degree than a surface survey continued to
the same depth: the geometry, not the instrument, sets the difference, and (5.2)
converts it into a number.

## 6. A fully worked band-limit calculation

A global field is to be represented to $l_{\max} = 60$ and analysed from a
satellite altitude.

1. **Latitude nodes.** At least $l_{\max} + 1 = 61$ Gauss-Legendre nodes. The
   demonstration's degree-8 experiment measured a coefficient error of order
   unity at 8 nodes and round-off at 9, so this is not a guideline to undercut.
2. **Longitude samples.** At least $2l_{\max}+1 = 121$ equispaced values, since
   the highest longitudinal frequency present is $m = 60$.
3. **Storage and cost.** With $l_{\max} = 60$ there are
   $(l_{\max}+1)^2 = 3721$ coefficients, and a synthesis costs $O(l_{\max}^3)$
   operations with the recurrences used here.
4. **Continuation.** Continuing from $r = 1.05R$ to the surface multiplies degree
   60 by $1.05^{60} = 18.68$, so the coefficient error is amplified by that
   factor — tolerable for this band, and the reason (5.2) gives $l_{\max} = 141.6$
   for a $10^{-3}$ target from $r/R = 1.05$.
5. **What is *not* determined.** The coefficients above $l_{\max}$ are not
   constrained by the data at all: they are zero by assumption, not by
   measurement. Any map drawn from a truncated model is smooth for this reason,
   and the smoothness is an artefact of the truncation. That statement is the
   honest boundary of the method, and it belongs in the same paragraph as the map.

## 7. Assumptions and regime of validity

1. **A sphere.** The basis is for a sphere; an ellipsoid of revolution introduces
   a $J_2$-like splitting and, in gravity, the normal-field separation. Numbers
   here do not transfer to an ellipsoidal reference surface without that step
   being done explicitly.
2. **Fully normalised harmonics with the $1/(4\pi)$ inner product.** The
   orthonormality residual of $4.2\times10^{-15}$ in (1.3) verifies *this*
   convention. Mixing conventions shifts every coefficient by $\sqrt{2l+1}$, and
   the error is invisible in a picture.
3. **A hard band limit.** The quadrature requirement of Section 2 is exact. A
   field with power above $l_{\max}$ analysed on a grid for $l_{\max}$ folds that
   power into the retained degrees; the result is not an approximation of the
   high degrees, it is a corruption of the low ones.
4. **Synthetic coefficients.** The $l^{-2}$ model of Section 4 is chosen for the
   demonstration. No published degree-variance law is quoted, and the measured
   exponent $-4.011$ is a property of this synthetic set.
5. **Downward continuation without regularisation.** Equation (5.1) is the exact
   continuation of an exact field. With noisy coefficients a stabilised
   continuation (or a stated $l_{\max}$) is required, and the number to state is
   (5.2)'s.
6. **Random coefficients are not a geophysical field.** The randomised sets here
   exercise the machinery; they do not model any planet.

## 8. Mastery checkpoint

Complete this without notes.

> A satellite measures a global field at $r = 1.02R$ and reports coefficients to
> degree $l_{\max} = 100$ with a relative coefficient error of $10^{-5}$.
>
> **(a)** State the minimum number of latitude nodes and longitude samples needed
> to analyse this band.
> **(b)** Compute the continuation factor for degrees $l = 20$, $100$ and $200$ at
> $r/R = 1.02$.
> **(c)** Using (5.2), compute the maximum degree usable for a target relative
> error of $10^{-2}$ in the continued field (measured value for this geometry:
> $l_{\max} = 348.8$).
> **(d)** State how many coefficients the model contains at $l_{\max} = 100$, and
> say what the model asserts about degrees above it.
> **(e)** The analysis is repeated with 90 latitude nodes and the low-degree
> coefficients change. Diagnose the cause without running anything, and state the
> one measurement that would confirm it.

A worked version appears with the
[exercises](exercises/04-spherical-harmonics-modelling-exercises.md).

## 9. Common pitfalls

1. **Mixing normalisation conventions.** A $\sqrt{2l+1}$ factor is invisible in a
   map and fatal in a coefficient comparison; the orthonormality residual is the
   test that catches it.
2. **Analysing with fewer latitude nodes than $L+1$.** Measured: coefficient
   errors of $1.1\times10^{-1}$ at 8 nodes against round-off at 9 for a degree-8
   field.
3. **Reading a smoothness in a map as a property of the Earth.** Truncation makes
   maps smooth; the smoothness is the model's.
4. **Continuing downward without stating a maximum degree.** Measured
   amplification $1.9\times10^{8}$ at $l=200$, $r/R = 1.10$: a $10^{-6}$
   coefficient error becomes 190 times the signal.
5. **Treating a spectrum as a physical law.** The exponent $-4.011$ measured here
   is the property of a synthetic $l^{-2}$ amplitude model.
6. **Assuming a higher-degree model is a better model.** Above the band the data
   constrain, the extra coefficients are assumptions.
7. **Ignoring the growth of round-off with $l$.** The relative analysis error
   grew from $3\times10^{-15}$ at $l=1$ to $2.7\times10^{-13}$ at $l=40$ in
   Section 4, and that growth is the precursor of Section 5's instability.

## 10. Related modules

- [19-04-01 Spectral Methods: Basis Choice and Exponential Convergence](01-spectral-methods.md) —
  the general principle that the basis must match the geometry.
- [19-04-02 Pseudospectral Methods, Transforms and Aliasing](02-pseudospectral.md) —
  the same band-limit and folding statements in one dimension.
- [08-01-03 Spherical Harmonic Analysis of the Magnetic Field](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/03-spherical-harmonic-magnetic.md) —
  the same machinery applied to a measured field, with its own normalisation
  conventions.
- [12-06-01 Moment of Inertia and Its Constraints](../../12-global-geophysics-interior/06-geodesy-constraints-interior/01-moment-of-inertia.md) —
  what a low-degree-only model still constrains.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the truncation
  degree as a regularisation parameter.

## Materials

- Demonstration: [`code/spherical_harmonics_modelling_demo.py`](./code/spherical_harmonics_modelling_demo.py).
- Exercises: [`exercises/04-spherical-harmonics-modelling-exercises.md`](./exercises/04-spherical-harmonics-modelling-exercises.md)
  with worked [solutions](./exercises/04-spherical-harmonics-modelling-solutions.md).
