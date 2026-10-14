---
id: 12-04-01
title: "Observations of the Core Field and Secular Variation"
level: graduate
prereqs: ["08-01-02", "08-01-04", "12-03-03"]
tags: [global-geophysics, earth-interior, geomagnetism, core-field, secular-variation, core-dynamics]
---

# Observations of the Core Field and Secular Variation

**All models and data in this module are SYNTHETIC.** The Gauss coefficients,
site coordinates, time series and conductivities below are invented teaching
inputs. They are not IGRF, WMM or any published model, and no real observatory,
station code or measured field value appears anywhere. Every number is printed by
[`code/core_field_observations_demo.py`](./code/core_field_observations_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** a measured (declination, inclination, intensity) triple into the
   spherical field components of a Gauss-coefficient model, and **explain** what
   a site measurement determines and what it does not.
2. **Compute** the geocentric dipole moment from the degree-1 coefficients and
   **state** why its rate of change cannot be linearly extrapolated.
3. **Construct** a Mauersberger–Lowes spectrum and **identify** the slope break
   that separates the core field from the crustal field.
4. **Recover** an advection rate from two epochs of a synthetic field and
   **explain** why the recovered rate depends on how much of the field is assumed
   to be moving.
5. **Derive** the free-decay eigenvalue condition for a conducting sphere with an
   insulating exterior and **show** that its slowest mode has decay time
   $R^2/\pi^2\eta$.
6. **Compute** the magnetic Reynolds number from an observed drift rate and
   **conclude** from it that the field must be regenerated.
7. **Quantify** what a truncated model misses and **state** the resolution limit
   of the observable core field.

## Prerequisites

- [08-01-02 The Geocentric Dipole, IGRF and WMM Models](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/02-dipole-and-igrf.md) —
  the potential representation used here.
- [08-01-04 Secular Variation, Jerks and Core Dynamics](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/04-secular-variation.md) —
  the frozen-flux kinematics and the arithmetic of small secular changes; this
  lesson does not repeat them.
- [12-03-03 Thermal Evolution and Secular Cooling](../03-geotherms-and-heat-budget/03-thermal-evolution.md) —
  the core heat flux that a dynamo needs.

## 1. What is actually observed

A magnetic observatory or a satellite magnetometer measures three numbers at a
point: the **intensity** $F$, the **declination** $D$ (the angle between magnetic
north and true north) and the **inclination** $I$ (the angle of the field below
the horizontal). Everything else in this lesson is a model fitted to a
distribution of such triples.

The model is a potential field. With $a$ the Earth's radius and $(r,\theta,\lambda)$
spherical coordinates, the internal part is written

$$V(r,\theta,\lambda) = a\sum_{l=1}^{\infty}\left(\frac{a}{r}\right)^{l+1}
\sum_{m=0}^{l}\left[g_l^m\cos m\lambda + h_l^m\sin m\lambda\right]P_l^m(\cos\theta),$$

with $P_l^m$ Schmidt semi-normalised. The field is $\mathbf{B} = -\nabla V$, so
that

$$B_r = \sum_l (l+1)\left(\frac{a}{r}\right)^{l+2}\!\left[g_l^m\cos m\lambda +
h_l^m\sin m\lambda\right]P_l^m,$$

$$B_\theta = -\sum_l \left(\frac{a}{r}\right)^{l+2}\!\left[\cdots\right]
\frac{\mathrm{d}P_l^m}{\mathrm{d}\theta},\qquad
B_\lambda = \sum_l \left(\frac{a}{r}\right)^{l+2}\frac{m}{\sin\theta}
\left[-g_l^m\sin m\lambda + h_l^m\cos m\lambda\right]P_l^m .$$

Two facts about this representation govern the rest of the lesson.

- **The coefficients are a spectral description, not a depth profile.** Every
  degree $l$ is present everywhere; $l$ is a horizontal wavelength, not a depth.
  Inverting a coefficient set for a current distribution in the core is severely
  non-unique, which is why the field is normally interpreted through a dynamo
  model rather than by direct inversion.
- **The expansion is truncated where the observations stop resolving it.** The
  demonstration's synthetic model runs to degree 8; a real, high-quality model
  resolves the core field to about degree 13–14 before crustal sources dominate.

## 2. From the model to a site measurement

**Worked example (synthetic).** The demonstration adopts
$g_1^0 = -29\,500\ \mathrm{nT}$, $g_1^1 = -1\,800\ \mathrm{nT}$,
$h_1^1 = +5\,100\ \mathrm{nT}$ and random coefficients for degrees 2–8, then
evaluates the field at four synthetic sites. It prints

| Site | lat | lon | $F$ (nT) | $D$ (°) | $I$ (°) |
|---|---|---|---|---|---|
| A | 45.0 | 10.0 | 67 301 | 20.87 | 76.86 |
| B | −30.0 | 140.0 | 26 144 | −4.91 | −45.01 |
| C | 70.0 | −60.0 | 58 979 | 104.81 | 84.29 |
| D | 0.0 | 0.0 | 43 908 | 6.84 | 35.21 |

The transformation from components to angles is

$$F = \sqrt{B_r^2 + B_\theta^2 + B_\lambda^2},\qquad
D = \arctan\frac{B_{\text{east}}}{B_{\text{north}}},\qquad
I = \arctan\frac{B_{\text{down}}}{\sqrt{B_{\text{north}}^2 + B_{\text{east}}^2}},$$

with $B_{\text{north}} = -B_\theta$, $B_{\text{east}} = B_\lambda$ and
$B_{\text{down}} = -B_r$.

Note what site B shows: $I = -45°$ in the southern hemisphere and a total
intensity less than half of site A's. **A single site does not measure the dipole
moment, the tilt, or the secular variation of either.** It measures a local
vector that is the sum of a dominant dipole and a non-dipole field of comparable
local importance.

## 3. The dipole moment and its rate

From the degree-1 coefficients the geocentric dipole moment is

$$\boxed{\;M = \frac{4\pi a^3}{\mu_0}
\sqrt{(g_1^0)^2 + (g_1^1)^2 + (h_1^1)^2}\;}$$

with the coefficients in tesla. For the demonstration's coefficients this gives

$$M = \frac{4\pi (6.371\times10^6)^3}{4\pi\times10^{-7}}
\sqrt{(2.95\times10^{-5})^2 + (1.8\times10^{-6})^2 + (5.1\times10^{-6})^2}
= 7.629\times10^{22}\ \mathrm{A\,m^2},$$

and the dipole axis is tilted

$$\theta_{\text{tilt}} = \arctan\frac{\sqrt{(g_1^1)^2 + (h_1^1)^2}}{|g_1^0|}
= 10.4°$$

from the rotation axis. Both numbers are *derived* from the coefficients: they
are not separate measurements, and their uncertainties are the uncertainties of
the degree-1 coefficients alone, which are the best-determined coefficients in the
whole expansion.

The demonstration then follows a synthetic $g_1^0$ series over 35 years:
$-29\,500$ to $-30\,690\ \mathrm{nT}$, a trend of

$$-33.9\ \mathrm{nT\,yr^{-1}} = 0.115\ \%\ \mathrm{yr^{-1}}.$$

If that trend were extrapolated linearly, $g_1^0$ would vanish in **869 years**.
The demonstration prints that number in order to dismiss it: the dipole moment is
not a linearly decaying quantity, and the extrapolation is a failure of method,
not a prediction. Any statement about the field's future requires the dynamo
model of [02 Numerical Geodynamo Models](02-geodynamo-numerical.md), not a line
through 35 years.

## 4. The spectrum, and where the core field stops

The Mauersberger–Lowes spectrum is the mean square field per degree at the
reference radius,

$$R(l) = (l+1)\sum_{m=0}^{l}\left[(g_l^m)^2 + (h_l^m)^2\right].$$

The synthetic model gives:

| $l$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| $R(l)$ (nT²) | $1.80\times10^9$ | $9.34\times10^7$ | $7.47\times10^7$ | $1.91\times10^7$ | $1.43\times10^7$ | $1.08\times10^7$ | $9.36\times10^6$ | $7.14\times10^6$ |
| ratio to previous | — | 0.052 | 0.800 | 0.255 | 0.748 | 0.759 | 0.864 | 0.762 |

Fitted over degrees 2–8 the log-linear slope is **−0.193 decades per degree**.

The observable that matters is not the slope but the **change of slope**. A
magnetic field generated by a self-sustaining dynamo in the core has a spectrum
that falls rapidly with $l$ up to the point where the core's own small-scale
structure is exhausted; below that point crustal magnetisation — which is
essentially white in $l$, because it is a near-surface distribution — takes over.
The break is the operational definition of "how deep can we see": past it, the
coefficients describe rocks, not the core. In the synthetic model the whole
spectrum to degree 8 is core-generated, so the break is not visible; in a real
model it appears near degree 13–14, and no amount of data improves it, because
the crustal signal is genuinely there.

## 5. Westward drift, and the ambiguity of a drift measurement

The non-dipole field appears to drift westward relative to the mantle. The
demonstration imposes an advection of

$$\omega_{\text{drift}} = -0.200\ \mathrm{deg\,yr^{-1}}$$

on the degrees 2–8 coefficients by rotating each order-$m$ pair through $m\phi$,
accumulates 20 years, and then recovers the rate by minimising the misfit between
the two epochs over a grid of shifts. It finds

$$\omega_{\text{recovered}} = -0.195\ \mathrm{deg\,yr^{-1}},$$

an error of **2.4%**. The error is not numerical noise: the axial part of the
field does not drift, so the best-fit shift is a compromise between the moving
and stationary parts. **A drift estimate therefore depends on how much of the
field the analyst assumes to be drifting**, and two published analyses can
disagree simply by making different assumptions.

At the core–mantle boundary the recovered rate corresponds to

$$|\omega|\,R_{\text{cmb}} = 0.195\times\frac{\pi}{180}\times
3.48\times10^6\ \mathrm{m\,yr^{-1}} = 11.9\ \mathrm{km\,yr^{-1}}
= 0.38\ \mathrm{mm\,s^{-1}},$$

which is a plausible core flow speed — and that plausibility is exactly why the
number is quoted: it is the observation that tells us the core is moving at
millimetres per second, not centimetres and not micrometres.

## 6. Derivation: the free decay of the field, and why a dynamo is required

Consider a sphere of radius $R$ and uniform electrical conductivity, with an
insulating exterior and no fluid motion. The induction equation reduces to pure
diffusion,

$$\frac{\partial \mathbf{B}}{\partial t} = \eta\nabla^2\mathbf{B},
\qquad \eta = \frac{1}{\mu_0\sigma}.$$

Take a poloidal mode $\mathbf{B} = \nabla\times\nabla\times(S\,\hat{\mathbf{r}})$
with $S = f(r)Y_l^m(\theta,\lambda)e^{-\eta k^2t}$. Inside the sphere $f \propto
j_l(kr)$; outside, no current flows, so the exterior potential must decay as
$r^{-(l+1)}$:

$$S_{\text{out}} = A\,r^{-(l+1)}, \qquad S_{\text{in}} = B\,j_l(kr).$$

Matching $S$ and $\partial S/\partial r$ at $r = R$ gives, after cancelling $B$,

$$kR\,j_l'(kR) + (l+1)j_l(kR) = 0 .$$

Using the recurrence $x j_l'(x) = l\,j_l(x) - x\,j_{l+1}(x)$:

$$\boxed{\;(2l+1)\,j_l(x) - x\,j_{l+1}(x) = 0,\qquad x = kR\;}$$

The decay time of a mode is $\tau = 1/(\eta k^2) = R^2/(\eta x^2)$, so the
slowest-decaying mode is the smallest root.

*Numerical check.* For $l = 1$ the first root is $x = \pi$ to machine precision
(the demonstration prints a residual of $2.2\times10^{-16}$). Hence

$$\tau_{\text{dipole}} = \frac{R^2}{\pi^2\eta},$$

the classic result. With an adopted $\sigma = 10^6\ \mathrm{S\,m^{-1}}$,
$\eta = 1/(\mu_0\sigma) = 0.796\ \mathrm{m^2\,s^{-1}}$ and
$R = 3.48\times10^6\ \mathrm{m}$,

$$\tau_{\text{dipole}} = \frac{(3.48\times10^6)^2}{\pi^2\times0.796}
= 1.542\times10^{12}\ \mathrm{s} = 48.9\ \mathrm{kyr}.$$

If the core's conductivity were $10^5\ \mathrm{S\,m^{-1}}$, the same formula
gives 309 kyr — a factor of ten, i.e. exactly the factor by which the
conductivity changed. **The decay time is a conductivity measurement in
disguise.**

The physical conclusion is forced and quantitative: the observed field is older
than 48.9 kyr by seven orders of magnitude, and its magnetic Reynolds number,

$$Rm = \frac{uR}{\eta} = \frac{5\times10^{-4}\times3.48\times10^6}{0.796}
= 2187 \gg 1,$$

shows that advection dominates diffusion. A field with $Rm \gg 1$ that has
existed far longer than its decay time cannot be a relic; it must be sustained by
motion. That is the geodynamo requirement, and it is an inference from two
numbers, not a statement of belief.

## 7. What truncation costs

The demonstration compares the full synthetic model with degree-limited versions
of it, evaluated on a grid:

| $l_{\max}$ | rms residual (nT) | residual / rms field |
|---|---|---|
| 1 | 10 335 | 0.245 |
| 2 | 8 087 | 0.192 |
| 3 | 5 580 | 0.133 |
| 4 | 4 578 | 0.109 |
| 6 | 2 899 | 0.069 |

Reading this table correctly is important. It is **not** a statement that degree
6 is "94% of the truth"; it is the statement that the neglected degrees carry
6.9% of the rms field *of this model*. A real model's residual at degree 13
contains a mixture of unresolved core field and crustal field, and the two cannot
be separated from the spectrum alone — only from their spatial and temporal
statistics, which is the subject of
[03 Palaeomagnetic Record and Reversal Frequency](03-palaeomagnetic-record.md)
and of crustal-field studies elsewhere.

## 8. Assumptions and regime of validity

1. **The model is a potential field from internal sources.** External (ionospheric
   and magnetospheric) fields and their induced counterparts are subtracted
   before fitting; the residual of that subtraction is the largest single
   contaminant of a degree-13 model.
2. **The coefficients are time-dependent.** A "model" is a snapshot or a
   short-interval expansion in time; comparing two epochs assumes both are
   reduced to the same reference radius and the same external-field convention.
3. **The conductivity is taken uniform.** Real values are uncertain by at least a
   factor of a few and vary with depth, so $\eta$ — and hence every decay time —
   carries that factor.
4. **Frozen flux is assumed for the drift estimate**, but the estimate itself
   shows that a non-drifting component biases it. Diffusion, ignored here, adds a
   further bias proportional to the local curvature of the field.
5. **The layered structure below the CMB is invisible** to the field, which is
   why conductivity and flow inversions are non-unique: many combinations of
   thickness and conductivity give the same observable drift.
6. **Site coordinates in the demonstration are synthetic.** Real observatory
   work must additionally deal with the crustal field at the site, which can be
   several thousand nanotesla and is not part of the core field at all.

## 9. Mastery checkpoint

Without notes:

> A synthetic model has $g_1^0 = -30\,000\ \mathrm{nT}$, $g_1^1 = 0$,
> $h_1^1 = +5\,000\ \mathrm{nT}$, and a synthetic drift of
> $-0.15\ \mathrm{deg\,yr^{-1}}$. **(a)** Compute the dipole moment and the tilt
> of the dipole axis. **(b)** Compute the field inclination at the equator for a
> pure axial dipole and say what the non-zero $h_1^1$ does to it. **(c)** Derive
> the free-decay condition and compute the decay time for
> $\sigma = 5\times10^5\ \mathrm{S\,m^{-1}}$. **(d)** Compute the magnetic
> Reynolds number for a 0.5 mm/s flow and state the conclusion. **(e)** Explain
> in one sentence why a drift rate recovered from two epochs depends on the
> assumed fraction of the field that drifts.

## 10. Common pitfalls

1. **Reading a single site's $D$ and $I$ as a dipole measurement.** The
   non-dipole field is locally comparable to the dipole.
2. **Extrapolating a secular variation trend.** The demonstration's own linear fit
   would empty the dipole in 869 years.
3. **Quoting a decay time without a conductivity.** $\tau \propto 1/\sigma$.
4. **Treating the spectrum slope as a depth.** $l$ is a horizontal wavenumber;
   the depth information comes only from a dynamo or current model.
5. **Reporting a drift rate as a measurement.** The choice of what is assumed to
   be drifting changes the answer by tens of per cent.
6. **Confusing the residual of a truncated model with its accuracy.** A 6.9%
   residual at degree 6 is a statement about the neglected degrees, not a
   validation of degree 6.

## 11. Related modules

- [02 Numerical Geodynamo Models](02-geodynamo-numerical.md) — where the field
  comes from and what controls its structure.
- [03 Palaeomagnetic Record and Reversal Frequency](03-palaeomagnetic-record.md) —
  the same field over geological time.
- [08-01 The Earth's Magnetic Field](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/README.md) —
  the description, the dipole, the spherical-harmonic analysis and the
  secular-variation kinematics.
- [08-04 Electromagnetic Induction](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md) —
  how core conductivity is constrained independently.
- [12-02 Composition and Mineral Physics](../02-composition-and-mineral-physics/README.md) —
  the core composition that sets the conductivity used here.
- [12-03 Geotherms and the Earth's Heat Budget](../03-geotherms-and-heat-budget/README.md) —
  the energy that drives the convection.
