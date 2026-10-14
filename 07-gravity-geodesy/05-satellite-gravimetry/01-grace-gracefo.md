---
id: 07-05-01
title: "GRACE and GRACE-FO: Mission Concept and Data Products"
level: graduate
prereqs: ["07-01-02", "07-01-03", "02-02-07"]
tags: [gravity, geodesy, satellite-gravimetry, orbital-mechanics, mass-transport]
---

# GRACE and GRACE-FO: Mission Concept and Data Products

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the orbital period, speed and ground-track spacing of a
   low-Earth orbiter from Kepler's third law and state how each sets a sampling
   limit on the gravity field it can recover.
2. **Derive** the exact relation between the range acceleration measured along a
   satellite-to-satellite link and the gravity gradient, and **verify** it
   against a physical point-mass model.
3. **Estimate** the size of the gravity signal from a specified surface mass
   anomaly and compare it with a stated instrument noise level.
4. **Quantify** the resolution limit imposed by downward continuation by
   computing the amplification factor $(a/R)^{l+1}$ and finding the degree at
   which it exceeds a stated tolerance.
5. **Explain** why a monthly gravity solution is a 30-day average, and
   **demonstrate** how sub-monthly variability is aliased into it.
6. **Convert** a fully normalised Stokes-coefficient change into an equivalent
   water height, and **verify** the conversion factor against exact mass balance
   at degree zero.
7. **State**, for any mass-change number quoted from a satellite solution, which
   part of it is measured and which part comes from the assumed Love numbers,
   the assumed background model, and the chosen temporal parametrisation.

## Prerequisites

- [07-01-02 Gravitational Potential, Equipotentials and the Geoid](../01-gravity-fundamentals/02-gravity-potential.md) —
  the potential, its gradient, and the multipole expansion this lesson uses.
- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../01-gravity-fundamentals/03-normal-gravity.md) —
  the reference field that is subtracted before anything is called an anomaly.
- [02-02-07 Central Forces](../../02-physics/02-classical-mechanics/07-central-forces.md) —
  Kepler orbits and the constants of orbital motion.

> **All models and data in this module are SYNTHETIC.** The orbit altitude, the
> satellite separation, the repeat cycle, the instrument noise and the Love
> number used throughout are teaching values chosen so that the arithmetic can be
> checked by hand. They are not the parameters of any real mission, and no
> measured gravity field appears anywhere in this module.

## 1. What a satellite gravimeter is, and what it is not

A satellite gravimeter is not a gravimeter. Nothing in the spacecraft measures
the local acceleration of gravity directly; the satellites are in free fall and
feel no gravity at all. What a low-low satellite-to-satellite tracking mission
measures is the **difference in the gravitational acceleration between two
spacecraft $220\ \mathrm{km}$ apart**, through the time variation of the distance
between them.

That single sentence explains nearly every property of the data product:

- The observable is a **difference**, so its leading term is the *modelled* orbit
  and the gravity signal is a small residual on top of it. The demonstration
  measures the ratio: for a synthetic $10\ \mathrm{cm}$ water-equivalent anomaly
  the signal is $1.15\times10^{-8}$ of the monopole term.
- The observable is a **gradient over a long baseline**, so the recoverable
  wavelengths are set by the baseline and the altitude, not by the intrinsic
  sharpness of the gravity field.
- The observable is a **function of time**, so the mass change is recovered from
  a time series of global fields, one per month (or per shorter interval), each
  an average over its own span.
- The result is **not an image**. It is a set of fully normalised coefficients of
  a spherical-harmonic expansion, plus a covariance matrix, plus a long list of
  background models that were subtracted first.

The last point is where honest reporting happens or fails. A number such as
"the region lost $X$ of water equivalent per year" is a chain of four
inferences: a measured range acceleration, an inverted set of coefficients, a
conversion to surface mass using assumed Love numbers, and a spatial filter
whose leakage must be quantified. This lesson builds the first three links and
leaves the fourth to [04 Mass Concentration Solutions, Leakage and Filtering](04-mascons-and-leakage.md).

## 2. Orbit geometry: what the orbit fixes before any gravity is measured

For a circular orbit of radius $a = R + h$ around a body of parameter $GM$,
Kepler's third law gives the period, and the balance of gravitational and
centripetal acceleration gives the speed:

$$T = 2\pi\sqrt{\frac{a^{3}}{GM}},
\qquad
v = \sqrt{\frac{GM}{a}}.$$

The ground track advances by $360^\circ$ per sidereal day **minus** one
revolution per orbit, so the number of revolutions per day

$$n = \frac{86400}{T}
\qquad\text{gives an equatorial track spacing}\qquad
d_{\text{track}} = \frac{2\pi R}{n}.$$

Two consequences matter for gravimetry, and both are visible in the
demonstration's first section:

- **Altitude sets the attenuation.** Every harmonic degree $l$ of the potential
  decays as $(R/a)^{l+1}$ between the surface and the satellite. A lower orbit
  sees more signal — and, since it also flies faster, more drag.
- **The ground track sets the spatial sampling.** With $n = 15.24$ rev/day the
  demonstrated orbit leaves a $2626\ \mathrm{km}$ gap between successive
  equatorial tracks, which is why a *repeat* cycle is needed to fill in the
  field: a cycle of $k$ days gives $nk$ distinct tracks spaced $2\pi R/(nk)$
  apart, so a $61$-day cycle clusters them to $43\ \mathrm{km}$ — at the price of
  averaging over $61$ days.

A repeat cycle only closes if $nk$ is (very nearly) an integer, and that is a
constraint on $k$, not a free choice. The demonstration's synthetic orbit gives
$n k = 929.8$ for $k = 61$, so this teaching value is *not* an exact repeat; a
commensurate alternative is $k = 41$, for which $nk = 624.97 \approx 625$ and the
track spacing is $64\ \mathrm{km}$. Real mission cycles are chosen by searching
for small integers that satisfy the constraint.

*Worked example 1.* Take $R = 6371\ \mathrm{km}$ (a rounded mean radius),
$h = 400\ \mathrm{km}$ and $GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$,
so $a = 6.771\times10^{6}\ \mathrm{m}$.

$$a^{3} = 3.10426\times10^{20}\ \mathrm{m^{3}},\qquad
T = 2\pi\sqrt{\frac{3.10426\times10^{20}}{3.986004418\times10^{14}}}
= 2\pi\sqrt{7.7879\times10^{5}} = 2\pi\,(882.49) = 5544.9\ \mathrm{s}.$$

That is $92.41\ \mathrm{min}$, hence $n = 86400/5544.9 = 15.582$ rev/day and
$d_{\text{track}} = 2\pi(6371)/15.582 = 2569\ \mathrm{km}$. Lowering the orbit by
$100\ \mathrm{km}$ (to $300\ \mathrm{km}$) raises $n$ to $15.934$ rev/day and
*narrows* the equatorial spacing to $2512\ \mathrm{km}$ — lower is better for
sampling, and worse for drag, which is why the altitude is a trade rather than an
optimisation.

## 3. What the range link measures

### 3.1 The exact identity

Let the two satellites be at $\mathbf{r}_1$ and $\mathbf{r}_2$ with separation
$\boldsymbol{\rho} = \mathbf{r}_2 - \mathbf{r}_1$, $\rho = |\boldsymbol{\rho}|$,
and unit vector $\hat{\boldsymbol{\rho}}$. The measured quantity (after the
modelled orbit is removed) is the projection of the differential acceleration:

$$\delta a_{\rho} = \hat{\boldsymbol{\rho}}\cdot
\left[\mathbf{a}(\mathbf{r}_2) - \mathbf{a}(\mathbf{r}_1)\right],
\qquad
\mathbf{a} = -\nabla U .$$

Now add a point mass $m$ at position $\mathbf{r}_m$ and write
$\mathbf{q}_i = \mathbf{r}_i - \mathbf{r}_m$. Because
$\mathbf{q}_2 - \mathbf{q}_1 = \boldsymbol{\rho}$, the point-mass contribution is

$$\delta a_{\rho}
= -Gm\,\hat{\boldsymbol{\rho}}\cdot\left[
\frac{\mathbf{q}_2}{q_2^{3}} - \frac{\mathbf{q}_1}{q_1^{3}}\right]
= -Gm\,\rho\,\frac{\hat{\boldsymbol{\rho}}\cdot\mathbf{q}_2 - \hat{\boldsymbol{\rho}}\cdot\mathbf{q}_1}{q^{3}} ,$$

where the last step uses $|\mathbf{q}_1| = |\mathbf{q}_2| = q$, which holds by
symmetry only when the mass lies below the **midpoint of the link** (the chord
direction is then perpendicular to the radius to the mass, so
$\hat{\boldsymbol{\rho}}\cdot\mathbf{q}_2 = -\,\hat{\boldsymbol{\rho}}\cdot\mathbf{q}_1$).
Then

$$\boxed{\;\delta a_{\rho} = -\,\frac{Gm\,\rho}{q^{3}}\;}$$

with $q$ the distance from either satellite to the mass. The demonstration
verifies this identity numerically: for the synthetic anomaly it obtains a
differenced value of $-3.109528\times10^{-9}\ \mathrm{m\,s^{-2}}$ against a
closed form of the same value, agreement $9.3\times10^{-16}$ relative — i.e. the
identity is exact, and the residual is double-precision round-off.

Two honest subtleties follow from that derivation.

- The identity is for a **point** mass under the link midpoint. A distributed
  anomaly is a superposition of point masses, so the observable is a weighted
  average of its contributions — which is exactly why the inverse problem is
  non-unique (see [07-03-04](../03-gravity-anomalies-and-modelling/04-inversion-gravity.md)).
- The observable is the **second difference over a baseline**, not the gradient
  at a point. The demonstration compares the measured value with
  $\rho\times\partial^{2}\phi/\partial s^{2}$ evaluated at the midpoint and finds
  they agree only to $0.98\%$: the second derivative of the point-mass potential
  changes sign along the link, so a longer baseline averages over a longer piece
  of the field and suppresses short wavelengths. That suppression *is* the
  resolution limit, viewed from the observable's side.

### 3.2 Signal size, and why the residual is the whole problem

*Worked example 2.* A synthetic anomaly is $10\ \mathrm{cm}$ of water equivalent
spread over a disc of radius $300\ \mathrm{km}$. Its mass is

$$m = \rho_w\,t\,\pi r^{2} = 1000 \times 0.10 \times \pi (3\times10^{5})^{2}
= 2.8274\times10^{13}\ \mathrm{kg}.$$

Place it below the link midpoint, with $h = 500\ \mathrm{km}$ altitude so that
$q = \sqrt{(R+h)^{2} + R^{2} - 2(R+h)R\cos(0.016)} = 511.10\ \mathrm{km}$. Then

$$\delta a_{\rho} = -\frac{(6.67430\times10^{-11})(2.8274\times10^{13})(2.19991
\times10^{5})}{(5.11096\times10^{5})^{3}} = -3.1095\times10^{-9}\
\mathrm{m\,s^{-2}},$$

while the monopole term over the same baseline is
$-2.7032\times10^{-1}\ \mathrm{m\,s^{-2}}$: the signal is $1.15\times10^{-8}$ of
the modelled background. With a synthetic single-sample noise of
$1\times10^{-10}\ \mathrm{m\,s^{-2}}$ the signal-to-noise ratio is $31$. The
lesson is arithmetic, not rhetoric: a mass anomaly of real hydrological interest
produces an acceleration difference ten-million-fold smaller than the orbit it
rides on.

## 4. The resolution limit: downward continuation

A spherical-harmonic coefficient of degree $l$ refers to a surface at radius
$r$; the same physical field has coefficients that scale as $r^{-(l+1)}$. A
coefficient estimated at the satellite radius $a$ therefore corresponds to a
surface coefficient **larger** by

$$A(l) = \left(\frac{a}{R}\right)^{l+1}.$$

Noise is amplified by the same factor when it is continued down, and this is the
fundamental resolution limit of any satellite gravimetry — not an engineering
shortfall that better hardware removes. The demonstration's table, for
$a/R = 1.07848$:

| degree $l$ | $A(l)$ | half-wavelength $\pi R/l$ |
|---|---|---|
| 10 | 2.30 | 2002 km |
| 20 | 4.89 | 1001 km |
| 40 | 22.15 | 500 km |
| 60 | 100.36 | 334 km |
| 80 | 454.78 | 250 km |
| 100 | 2060.85 | 200 km |
| 120 | 9338.85 | 167 km |

The demonstration then applies a stated tolerance: amplification stays below
$10\times$ only up to degree $29$ (half-wavelength $690\ \mathrm{km}$) and below
$100\times$ only up to degree $59$ (half-wavelength $339\ \mathrm{km}$). A white
coefficient noise of $1\times10^{-12}$ per degree gives an rms error of
$1.69\times10^{-12}$ *at altitude* and $1.52\times10^{-9}$ *continued to the
surface* — a factor $899$. **The usable degree of a satellite solution is fixed
by the ratio of the signal spectrum to the noise spectrum, and every increase of
degree is paid for at the rate of $7.8\%$ per degree.**

*Worked example 3.* For $a/R = 1.07848$, how much amplification at degree $60$?

$$\ln A(60) = 61\ln(1.07848) = 61 \times 0.0755526 = 4.608711,
\qquad A(60) = e^{4.608711} = 100.35,$$

which reproduces the tabulated $100.36$ to the precision of the logarithm. Note
the practical reading: a coefficient error of $10^{-12}$ at degree $60$ becomes a
$1.0\times10^{-10}$ error in the surface field, which in equivalent water height
is of order $1\ \mathrm{mm}$ for the degree-60 term alone — much larger than the
coefficient error, and larger than many real hydrological trends of interest.

## 5. Temporal sampling: monthly means and aliasing

A monthly solution is an average over its own span. The demonstration's fourth
section makes this concrete with a synthetic $5.0\ \mathrm{cm}$ oscillation of
period $3.7$ days:

- the 30-day means have an rms of $0.045\ \mathrm{cm}$ — the oscillation is
  almost entirely averaged away, and what survives is a *bias*, not a signal;
- monthly *instantaneous* samples of the same oscillation fold to an apparent
  period of $278$ days, because the sampling frequency $1/30\
  \mathrm{day^{-1}}$ beats against $1/3.7\ \mathrm{day^{-1}}$:
  $f_{\text{alias}} = |1/3.7 - 8/30| = 0.00360\ \mathrm{day^{-1}}$.

So sub-monthly mass variability appears in a monthly solution either as a small
bias or as a spurious multi-month oscillation, and neither can be undone after
the fact. This is why time-variable gravity products are quoted with their
**averaging kernel**: what the number refers to is a spatial average over a
stated region *and* a temporal average over a stated span.

## 6. From a coefficient to a mass

Assume the time-variable part of the field is produced by a thin surface mass
layer of density $\Delta\sigma(\theta,\phi)$ on a spherically symmetric Earth.
The layer's **own** attraction gives a coefficient change

$$\Delta C^{\text{layer}}_{lm} = \frac{3}{4\pi R\rho_e(2l+1)}
\iint \frac{\Delta\sigma}{\rho_w}\,\bar P_{lm}(\cos\theta)\cos m\phi\;
\mathrm{d}\Omega ,$$

which for a uniform layer of thickness $t$ at $l=0$ reduces to
$\Delta C_{00} = 3\rho_w t/(\rho_e R)$ — identical to the exact mass-balance
result for a uniform shell, so the normalisation is fixed rather than guessed.

The Earth, however, also deforms, and the potential change of the deformed Earth
partly cancels the layer's own attraction. With **load** Love numbers $k_l$,

$$\Delta C^{\text{observed}}_{lm} = \left(1 + k_l\right)\Delta C^{\text{layer}}_{lm},
\qquad k_2 \approx -0.30 \ \text{in the synthetic model used here},$$

so that a degree-2 load is seen at only $70\%$ of its rigid-Earth size.
Inverting the pair of relations gives the working formula

$$\frac{\Delta\sigma(\theta,\phi)}{\rho_w}
= \frac{R\rho_e}{3\rho_w}\sum_{l=0}^{L}\frac{2l+1}{1+k_l}
\sum_{m=0}^{l}\left[\Delta C_{lm}\cos m\phi + \Delta S_{lm}\sin m\phi\right]
\bar P_{lm}(\cos\theta).$$

The left-hand side is the **equivalent water height** (EWH): the thickness of a
layer of water of density $\rho_w$ that would produce the observed change. It is
a *converted* quantity, not a measured one, and the conversion imports three
assumptions: the mass is surface mass, the deformation is elastic with the
assumed $k_l$, and the coefficients are complete to some degree $L$ (the
truncation is the subject of [04](04-mascons-and-leakage.md)).

*Worked example 4.* Compute the EWH corresponding to a synthetic
$\Delta C_{20} = 1\times10^{-11}$, with $R = 6.371\times10^{6}\ \mathrm{m}$,
$\rho_e = 5513.4\ \mathrm{kg\,m^{-3}}$ (computed as $M/(\tfrac{4}{3}\pi R^{3})$
from $M = GM/G = 5.9722\times10^{24}\ \mathrm{kg}$), $\rho_w = 1000\
\mathrm{kg\,m^{-3}}$ and a synthetic $k_2 = -0.30$:

$$\frac{R\rho_e}{3\rho_w}\frac{2l+1}{1+k_l}\Delta C_{20}
= \frac{(6.371\times10^{6})(5513.4)}{3000}\cdot\frac{5}{0.70}\cdot10^{-11}
= (1.1709\times10^{7})(7.1429)(10^{-11}) = 8.363\times10^{-4}\ \mathrm{m},$$

i.e. **$0.836\ \mathrm{mm}$** of equivalent water. Note how small that is, and
that it is *not* the thickness of a local deposit of water: a single low-degree
coefficient describes a global-scale pattern. A $10\ \mathrm{cm}$ disc anomaly of
the kind used in Section 3.2 requires many coefficients of much higher degree.

**Verification of the normalisation.** The one case that can be checked without
a satellite is a uniform global layer of thickness $t$, whose coefficient change
follows from exact mass balance:

$$\Delta C_{00} = \frac{4\pi R^{2}\rho_w t}{M}
= \frac{4\pi(6.371\times10^{6})^{2}(1000)(0.01)}{5.9722\times10^{24}}
= 8.540691\times10^{-10}
\;\;\text{for } t = 1.00\ \mathrm{cm}.$$

Feeding that back through the formula with $l = 0$, $k_0 = 0$ returns
$10.000000\ \mathrm{mm}$ — a relative error of $1.7\times10^{-16}$, i.e. exact to
round-off. The demonstration performs exactly this check, which is what makes the
$3\rho_w$ and $4\pi$ denominators trustworthy rather than merely plausible.

## 7. Assumptions and regime of validity

| Assumption | Where it is used | What breaks if it fails |
|---|---|---|
| The satellites are in Keplerian free fall; only gravity acts | orbit geometry, range observable | drag and radiation pressure enter the range acceleration and dominate at high degrees |
| The link is short compared with the curvature of the field | the point-mass identity | for a long baseline the second-difference and point-derivative forms diverge (measured here: $1\%$ at $220\ \mathrm{km}$) |
| The time-variable field is a thin surface mass layer | the EWH conversion | deep mass changes (mantle flow, core) are misattributed to the surface; a $\sim$ few hundred km deep change leaks into low degrees |
| Deformation is elastic and the load Love numbers are known | the $1/(1+k_l)$ factor | a $10\%$ error in $k_l$ is a $10\%$ error in the mass for that degree (for $k_2 = -0.30$, a $10\%$ error in $k_2$ is a $4.3\%$ error in mass) |
| The monthly solution is an average over the month | temporal interpretation | sub-monthly variability is aliased or biased (Section 5) |
| The background models (static field, tides, atmosphere, ocean, GIA) are correct | everything reported as a mass *change* | errors in the removed models appear as trends |

The last row is the one that most often turns a defensible measurement into an
indefensible one. The instrument measures a range; the coefficients are an
inversion; the mass is a conversion; the trend is a difference of two further
inversions. Any published-looking number should be traceable to a stated choice
in each row of this table.

## 8. Python demonstration

`code/grace_gracefo_demo.py` runs the whole calculation and prints labelled
results with units:

1. **Orbit geometry** — period, speed, revolutions per day and track spacing from
   Kepler's third law; a synthetic orbital period of $94.469\ \mathrm{min}$,
   speed $7.617\ \mathrm{km\,s^{-1}}$, $15.243$ rev/day and $2626\ \mathrm{km}$
   track spacing.
2. **The range observable** — the exact identity $\delta a_\rho = -Gm\rho/q^{3}$
   verified to $9.3\times10^{-16}$ relative, the signal-to-background ratio
   $1.15\times10^{-8}$, the signal-to-noise ratio $31$, and the $0.98\%$
   discrepancy between the baseline difference and the local curvature.
3. **Downward continuation** — the amplification table, the degrees at which a
   $10\times$ and $100\times$ tolerance is exceeded ($29$ and $59$), and a
   $899\times$ rms noise amplification for white coefficient noise.
4. **Temporal sampling** — the aliasing arithmetic for a $3.7$-day oscillation
   sampled monthly.
5. **Coefficient to mass** — EWH from a synthetic $\Delta C_{20}$, and the exact
   degree-0 mass-balance check that validates the normalisation.

The demonstration is print-only, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network access, and exits 0.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-grace-gracefo-exercises.md`](./exercises/01-grace-gracefo-exercises.md)
and [`exercises/01-grace-gracefo-solutions.md`](./exercises/01-grace-gracefo-solutions.md).

- **★** Compute $T$, $v$ and the track spacing for $h = 450\ \mathrm{km}$.
- **★** Compute the EWH for $\Delta C_{20} = 3\times10^{-11}$ and state why it is
  not a local water depth.
- **★★** Derive the point-mass identity and check it against a numerical
  difference, as the demonstration does.
- **★★** Find the degree at which a $3\times$ tolerance on the continuation
  amplification is exceeded, and the half-wavelength that implies.
- **★★★** Quantify how a wrong $k_2$ propagates into a reported EWH trend, and
  design a numerical experiment to measure the leakage of a disc anomaly into the
  coefficients used to report a neighbouring region.

## 10. Mastery checkpoint

Do this without notes, then check the numbers yourself:

> A synthetic two-satellite mission flies at $h = 500\ \mathrm{km}$ with a
> $220\ \mathrm{km}$ separation, a link noise of $1\times10^{-10}\
> \mathrm{m\,s^{-2}}$ and 30-day solutions. **(a)** A synthetic
> $300\ \mathrm{km}$-radius anomaly produces a measured range acceleration of
> $-3.11\times10^{-9}\ \mathrm{m\,s^{-2}}$; recover its mass and its
> equivalent water height. **(b)** State the ratio of this signal to the modelled
> monopole term over the same baseline. **(c)** Find the highest degree for which
> the downward-continuation amplification stays below $20\times$, and the
> half-wavelength that implies. **(d)** Name one process a 30-day solution cannot
> recover, and say why. **(e)** List the three assumptions in your step-(a)
> conversion to water equivalent.

*Answers.* **(a)** From $\delta a_\rho = -Gm\rho/q^{3}$,

$$m = \frac{|\delta a_\rho|\,q^{3}}{G\rho}
= \frac{3.11\times10^{-9}(5.11096\times10^{5})^{3}}
{(6.67430\times10^{-11})(2.19991\times10^{5})}
= 2.83\times10^{13}\ \mathrm{kg},$$

which over a $300\ \mathrm{km}$ disc is $10.0\ \mathrm{cm}$ of equivalent
water (the anomaly the demonstration used). **(b)** $1.15\times10^{-8}$, i.e.
the signal is eight orders of magnitude below the orbit it rides on.
**(c)** $1.07848^{l+1} < 20$ gives $l+1 \le 39$, so $l_{\max} = 38$
($A(38) = 19.04$, $A(39) = 20.53$), a half-wavelength of
$\pi(6371)/38 = 527\ \mathrm{km}$. **(d)** A flood or any event shorter than
the repeat cycle: a 30-day solution is an average, and a synthetic
$3.7$-day, $5\ \mathrm{cm}$ oscillation leaves only $0.045\ \mathrm{cm}$
rms in the monthly means (or, sampled monthly, a spurious 278-day period).
**(e)** The mass change is a thin surface layer; the load Love numbers are known;
and the coefficient set is complete to a stated degree.
## 11. Common pitfalls

1. **Calling the product an image.** A set of coefficients is not a map until a
   filter has been chosen, and the filter is a modelling decision.
2. **Quoting a high-degree coefficient as if it were measured.** It may be
   almost entirely determined by the regularisation (see
   [04](04-mascons-and-leakage.md)).
3. **Forgetting the downward-continuation factor.** The surface amplitude of a
   degree-60 term is two orders of magnitude larger than its measured amplitude.
4. **Reading a monthly solution as a monthly average of a *region*.** The
   averaging kernel spreads mass across the boundary; a "basin trend" is a
   filtered quantity.
5. **Treating GIS/GIA/atmosphere/ocean corrections as small print.** In
   groundwater and ice applications they can exceed the signal.
6. **Mixing units.** Gravity coefficients are dimensionless; gravity gradients
   are quoted in $\mathrm{E}$ ($1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}$);
   surface mass is $\mathrm{kg\,m^{-2}}$ or its water equivalent in
   $\mathrm{m}$ or $\mathrm{cm}$.

## 12. Real-world applications

- **Mass transport.** Time-variable gravity is the only remote-sensing
  measurement of total water storage change, which is why it is used for
  aquifer monitoring, ice-sheet mass balance and sea-level budgets — with
  the caveats above.
- **Static field and the geoid.** Low-degree coefficients from satellite
  gravimetry anchor the global geoid; the long-wavelength content is exactly what
  the satellite geometry measures best.
- **Orbit determination.** The same measurement is inverted to improve
  atmospheric density and drag models, because a mismodelled non-gravitational
  force appears as a spurious gravity signal.
- **Reference systems.** The time-variable field provides the gravity
  coefficients used in precise orbit determination for altimetry and for the
  vertical datum work of [module 07](../07-geoid-and-height-modern/README.md).

## 13. Further reading

- **Heiskanen, W. A. & Moritz, H., *Physical Geodesy*** — the potential-theory
  foundations used in Sections 3 and 6.
- **Torge, W. & Müller, J., *Geodesy*** — the standard textbook treatment of
  satellite methods and height systems.
- **Kaula, W. M., *Theory of Satellite Geodesy*** — orbital perturbations and the
  degree-variance description of the gravity field.
- **Hofmann-Wellenhof, B. & Moritz, H., *Physical Geodesy*** — the modern
  treatment of satellite-only and combined solutions.
- Mission and data documentation for the actual satellites is published by the
  operating agencies; consult it for real mission parameters, which this lesson
  deliberately does not quote.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Editions and years are omitted
> because they differ between printings.

## 14. Related lessons

- [02 GOCE, Gravity Gradients and the Static Field](02-goce.md) — the same physics
  measured as a tensor gradient rather than as a range difference.
- [03 Spherical Harmonic Solutions and Coefficient Interpretation](03-spherical-harmonic-solutions.md) —
  where the coefficients come from and how their spectra are read.
- [04 Mass Concentration Solutions, Leakage and Filtering](04-mascons-and-leakage.md) —
  the filter that turns coefficients into a regional number.
- [05 Applications: Groundwater Depletion, Ice Loss, Sea Level](05-grace-applications.md) —
  what the numbers are used for, and how the error budget is built.
- [07-03-07 Time-Variable Gravity: Hydrology, Ice and Mass Redistribution](../03-gravity-anomalies-and-modelling/07-time-variable-gravity.md) —
  the same observable treated as a geophysical signal rather than as a mission.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general theory
  of the inversion step.

## 15. Related modules

- [Satellite Gravimetry](./README.md) — this module's index, with the lesson map
  and the run commands.
- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — the
  potential, the reference field and the reductions this module assumes.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the inversion and
  regularisation steps behind every coefficient set.
- [26-reference-library](../../26-reference-library/README.md) — symbols, units
  and constants used without re-derivation.

## 16. Self-assessment checklist

- [ ] I can compute an orbital period and track spacing from $R$, $h$ and $GM$.
- [ ] I can derive $\delta a_\rho = -Gm\rho/q^{3}$ and state the symmetry it relies on.
- [ ] I can compare a mass-anomaly signal with a stated instrument noise.
- [ ] I can compute $(a/R)^{l+1}$ and state what tolerance implies for the maximum degree.
- [ ] I can explain why a monthly solution cannot see a flood.
- [ ] I can convert $\Delta C_{20}$ to equivalent water height and verify the factor at degree 0.
- [ ] I can list three assumptions the EWH conversion imports.
