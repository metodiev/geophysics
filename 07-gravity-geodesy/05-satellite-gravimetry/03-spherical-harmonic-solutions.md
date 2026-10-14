---
id: 07-05-03
title: "Spherical Harmonic Solutions and Coefficient Interpretation"
level: doctoral
prereqs: ["07-01-02", "07-01-03", "07-05-02"]
tags: [gravity, geodesy, satellite-gravimetry, spherical-harmonics, inverse-problems]
---

# Spherical Harmonic Solutions and Coefficient Interpretation

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the spherical-harmonic expansion of the potential from the
   separability of Laplace's equation in spherical coordinates.
2. **State and use** the $4\pi$ normalisation convention, and **show** by
   quadrature that the functions are orthonormal on the sphere.
3. **Derive** the $(l-1)$ factor in the gravity anomaly and the $1/\gamma$ factor
   in Bruns' formula from the boundary condition on the disturbing potential, and
   **verify** both against finite differences of the potential.
4. **Interpret** a degree-variance spectrum: distinguish a coloured spectrum from
   a white one, and **measure** the exponent of a stated synthetic law.
5. **Compute** the information budget of a model of maximum degree $L$ —
   $(L+1)^{2}$ coefficients against a half-wavelength $\pi R/L$ — and explain why
   resolution is expensive.
6. **Define** the signal-to-noise crossover degree for a stated error spectrum
   and explain why every coefficient beyond it is an assumption, not a
   measurement.
7. **State** the three things a coefficient set does not tell you: its
   normalisation, its error correlation, and its regularisation.

## Prerequisites

- [07-01-02 Gravitational Potential, Equipotentials and the Geoid](../01-gravity-fundamentals/02-gravity-potential.md) —
  the potential, its multipole expansion and the geoid as an equipotential.
- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../01-gravity-fundamentals/03-normal-gravity.md) —
  the reference field whose coefficients are subtracted.
- [02 GOCE, Gravity Gradients and the Static Field](02-goce.md) —
  where the medium- and high-degree coefficients come from.

> **All models and data in this module are SYNTHETIC.** The coefficient set below
> is drawn from a stated synthetic spectrum with a fixed seed; no measured
> gravity model and no published coefficient value is used anywhere.

## 1. Why spherical harmonics, and not something else

Laplace's equation in spherical coordinates,

$$\nabla^{2}U = \frac{1}{r^{2}}\frac{\partial}{\partial r}
\left(r^{2}\frac{\partial U}{\partial r}\right)
+ \frac{1}{r^{2}\sin\theta}\frac{\partial}{\partial\theta}
\left(\sin\theta\frac{\partial U}{\partial\theta}\right)
+ \frac{1}{r^{2}\sin^{2}\theta}\frac{\partial^{2}U}{\partial\phi^{2}} = 0,$$

is separable: writing $U = \mathcal{R}(r)\Theta(\theta)\Phi(\phi)$ gives a
radial equation with solutions $r^{l}$ and $r^{-(l+1)}$, an azimuthal equation
with solutions $\cos m\phi, \sin m\phi$, and a latitudinal equation whose bounded
solutions are the associated Legendre functions. **The basis is not a choice; it
is what the differential equation admits.** That is why every global gravity
model is a list of coefficients rather than a grid of numbers, and why the
coefficients are the natural thing to compare between models.

Between the masses, with the $r^{-(l+1)}$ branch (fields that decay at
infinity), the expansion of the gravitational potential is

$$U(r,\theta,\phi) = \frac{GM}{r}\sum_{l=0}^{\infty}\left(\frac{R}{r}\right)^{l}
\sum_{m=0}^{l}\left[C_{lm}\cos m\phi + S_{lm}\sin m\phi\right]
\bar P_{lm}(\cos\theta),$$

with $R$ a reference radius, $C_{lm}$ and $S_{lm}$ dimensionless, and
$\bar P_{lm}$ the **$4\pi$-normalised** associated Legendre functions,

$$\bar P_{lm}(x) = \sqrt{(2-\delta_{m0})(2l+1)\frac{(l-m)!}{(l+m)!}}\;P_{lm}(x),
\qquad
\iint_{\text{sphere}}\bar P_{lm}^{2}\,\mathrm{d}\Omega = 4\pi .$$

*Worked verification.* The demonstration integrates $\bar P_{lm}^{2}$ over
$x = \cos\theta$ with Gauss–Legendre quadrature (200 nodes) and finds
$2.0000000000$ for every $m = 0$ and $4.0000000000$ for every $m \ge 1$,
matching $2(2-\delta_{m0})$ to between $0$ and $4\times10^{-14}$ relative. So the
stated normalisation is the normalisation in force. **A coefficient set with an
unstated convention is not interpretable**: the same numbers mean a different
field under a Schmidt or unnormalised convention, and the difference grows with
degree.

## 2. The geoid and the gravity anomaly from one coefficient set

Define the **disturbing potential** $T = U - U_{\text{ref}}$, so that for a
spherical reference field $T$ is the $l \ge 2$ part of the sum above. Two
quantities follow from $T$, and both are derived, not looked up.

**Bruns' formula.** The geoid is an equipotential surface displaced from the
reference surface. On the reference sphere the potential of the real Earth
differs from the reference by $T$, and a displacement $N$ along the normal
changes the reference potential by $\gamma N$, so $T = \gamma N$ and

$$\boxed{\;N(\theta,\phi) = \frac{T(R,\theta,\phi)}{\gamma}
= \frac{GM}{R\gamma}\sum_{l=2}^{L}\sum_{m=0}^{l}
\left[C_{lm}\cos m\phi + S_{lm}\sin m\phi\right]
\bar P_{lm}(\cos\theta)\;}$$

with $\gamma$ the normal gravity. The factor $GM/(R\gamma) = 6.3798\times10^{6}\
\mathrm{m}$ for the constants used here.

**The gravity anomaly.** The gravity anomaly is the difference in the *radial
derivative* of the potential, referred to the same surface. Since
$T \propto r^{-(l+1)}$ for each degree,

$$\frac{\partial T}{\partial r} = -\frac{GM}{r^{2}}\sum_{l}(l+1)\left(\frac{R}{r}
\right)^{l}\sum_{m}[\ldots]\bar P_{lm},$$

and using the fundamental equation of physical geodesy at $r = R$,

$$\Delta g = -\frac{\partial T}{\partial r} - \frac{2T}{r}
= \frac{GM}{R^{2}}\sum_{l=2}^{L}(l-1)\sum_{m=0}^{l}
\left[C_{lm}\cos m\phi + S_{lm}\sin m\phi\right]\bar P_{lm}(\cos\theta).$$

The $(l-1)$ factor is the entire reason a *geoid* map and a *gravity anomaly* map
of the same field look different:

| degree $l$ | $(l-1)$ | character |
|---|---|---|
| 2 | 1 | the geoid and the anomaly carry equal weight |
| 5 | 4 | the anomaly begins to emphasise shorter scales |
| 20 | 19 | long-wavelength features nearly cancel in the anomaly |
| 40 | 39 | the anomaly is essentially a high-degree quantity |

So the geoid is a *smooth* field (dominated by low degrees) while the gravity
anomaly is *rough* (dominated by high degrees), and that difference is
arithmetic, not a property of the data.

*Worked example 1.* Take a single synthetic zonal coefficient $C_{20} =
1.0\times10^{-5}$ and evaluate at the pole, where
$\bar P_{20}(1) = \sqrt{5} = 2.236068$.

$$N = \frac{GM}{R\gamma}\,C_{20}\bar P_{20}(1)
= (6.379836\times10^{6})(1.0\times10^{-5})(2.236068)
= 142.66\ \mathrm{m},$$
$$\Delta g = \frac{GM}{R^{2}}(2-1)C_{20}\bar P_{20}(1)
= (9.8203)(1.0\times10^{-5})(2.236068)\ \mathrm{m\,s^{-2}}
= 2.1959\times10^{-4}\ \mathrm{m\,s^{-2}} = 21.96\ \mathrm{mGal}.$$

*Worked example 2 (verification).* The demonstration repeats this computation
for all degrees at five points and compares the analytic $(l-1)$ route with a
finite-difference evaluation of $-\partial T/\partial r - 2T/r$. Agreement is
$2\times10^{-9}$ to $1\times10^{-7}$ relative — the residual being the
$100\ \mathrm{m}$ finite-difference step. The reproduction of the analytic form
by a numerical derivative is what makes the factors trustworthy; a factor of
$l$, $l+1$ or $l-1$ would be invisible in a plot and fatal in a mass budget.

## 3. Reading a spectrum

The natural summary of a global model is the **degree variance**

$$\sigma_{l}^{2} = \frac{1}{2l+1}\sum_{m=0}^{l}\left(C_{lm}^{2} + S_{lm}^{2}
\right),$$

which is the power of the field at degree $l$ and, in the $4\pi$ convention, the
mean-square contribution of that degree to the potential. Real gravity fields
have a **coloured** spectrum: the amplitude falls roughly as a power of $l$,
because the Earth's relief and its compensation have a scale-invariant
appearance. That is an empirical observation about the Earth, not a law; what is
*not* empirical is the behaviour of noise.

*Worked example 3.* The demonstration's synthetic law is
$\sigma_{l} = 1.0\times10^{-5}(2/l)^{2}$, so the degree variance should fall as
$l^{-4}$. Fitting a straight line to $\log\sigma_{l}^{2}$ against $\log l$ over
$2 \le l \le 40$ gives a slope of $-4.103$ for the signal and $-0.088$ for a
white-noise control drawn with the *same* amplitude scale. The $-4.1$ rather than
$-4.0$ is the sampling scatter of one random realisation, not a different law;
the control's slope near zero is what "white" means. **A measured spectrum slope
without a control experiment is not evidence of anything.**

The practical use of the spectrum is comparison: a coefficient is informative
only where the signal spectrum is above the error spectrum.

## 4. The information budget

A model complete to degree $L$ has

$$N_{\text{coef}} = (L+1)^{2}$$

coefficients (including degree 0 and the dipole terms, which are conventionally
set to zero or absorbed into other parameters). The resolution is commonly
expressed as the half-wavelength

$$\lambda_{1/2} \approx \frac{\pi R}{L},$$

so:

| $L$ | $(L+1)^{2}$ | $\pi R/L$ |
|---|---|---|
| 10 | 121 | 2002 km |
| 20 | 441 | 1001 km |
| 40 | 1681 | 500 km |
| 60 | 3721 | 334 km |
| 100 | 10201 | 200 km |
| 200 | 40401 | 100 km |

Doubling the resolution costs **four times** as many parameters, each of which
must be determined by finitely many observations. This is the numerical face of
the same underdetermination that appears in every inverse problem in this folder:
the model space grows as a power of the resolution while the data grow as a
product of the sampling rate and the mission duration.

*Worked example 4.* How many coefficients does a $200\ \mathrm{km}$
half-wavelength model need? $L = \pi R/\lambda_{1/2} = \pi(6371)/200 = 100$,
hence $(101)^{2} = 10201$ coefficients. A month of range-link data contains of
order $10^{6}$ scalar measurements but they are *not* independent, and the
inversion of the resulting normal-equation system is where the rank deficiency
becomes explicit.

## 5. Where the information stops: the crossover degree

Propagating a per-coefficient error spectrum $\epsilon_{l}$ and comparing with the
signal spectrum defines a **crossover degree** $l^{*}$:

$$\sigma_{l} > \epsilon_{l} \quad \text{for } l < l^{*}, \qquad
\sigma_{l} < \epsilon_{l} \quad \text{for } l > l^{*}.$$

For the demonstration's synthetic pair
$\sigma_{l} = 10^{-5}(2/l)^{2}$ and $\epsilon_{l} = 10^{-9}l$, the crossover
occurs where $10^{-5}(2/l)^{2} = 10^{-9}l$, i.e. $l^{3} = 4\times10^{4}$,
$l = 34.2$; the demonstration confirms that the highest degree with signal above
noise is $l = 34$, a half-wavelength of $589\ \mathrm{km}$.

Three honest consequences:

1. **A quoted maximum degree is a model-space statement.** A solution "complete
   to degree $200$" need not carry information at degree $200$.
2. **Above the crossover, the coefficients are set by the regularisation** — the
   a priori spectrum, the damping, the constraint — and therefore by the
   analyst's assumptions. They are not measurements and cannot be tested against
   the data that did not determine them.
3. **The crossover moves with the assumed signal spectrum**, so a claim that
   "the model resolves $X$ km" is a joint claim about the data, the noise model
   and the assumed Earth spectrum. State all three or state nothing.

## 6. Assumptions and regime of validity

1. **Vacuum outside the masses; $r > R$.** The $r^{-(l+1)}$ branch is the branch
   that decays; inside the masses the other branch grows and the expansion is
   invalid.
2. **A single reference radius $R$ and one normalisation.** Mixing conventions or
   reference radii between models produces differences that look like
   geophysics.
3. **A spherical (or ellipsoidal) reference.** The disturbing potential is defined
   relative to a stated normal field; $\gamma$ is the normal gravity at the point
   or a stated mean value, and the difference matters at the $10^{-3}$ level.
4. **The coefficients are complete to $L$ and truncated.** Truncation is not
   noise: it is a systematic removal of signal, which is why
   [remove–restore](../07-geoid-and-height-modern/01-geoid-determination.md)
   exists.
5. **The error spectrum is an error spectrum.** A covariance matrix with
   correlations makes the crossover degree a *direction-dependent* statement;
   per-coefficient errors alone overstate the information.
6. **No a priori information is in the coefficients.** If the inversion used an
   a priori spectrum, the low degrees are contaminated by it too, and the honest
   error budget must say so.

## 7. Python demonstration

`code/spherical_harmonic_solutions_demo.py` prints:

1. **Normalisation check** by $200$-node Gauss–Legendre quadrature: every
   $\bar P_{lm}^{2}$ integrates to $2(2-\delta_{m0})$ to between $0$ and
   $4\times10^{-14}$ relative.
2. **A synthetic coefficient set** with $1677$ coefficients for
   $2 \le l \le 40$ drawn from $\sigma_{l} = 10^{-5}(2/l)^{2}$.
3. **Geoid and anomaly from the same coefficients** at five points: geoid
   undulations $-348.3$ to $+309.3\ \mathrm{m}$ and anomalies $-154.8$ to
   $+52.4\ \mathrm{mGal}$, with the analytic and finite-difference routes agreeing
   to $10^{-9}$–$10^{-7}$ relative.
4. **Degree variance**: fitted slope $-4.103$ for the signal and $-0.088$ for a
   white-noise control.
5. **Information budget**: $(L+1)^{2}$ against $\pi R/L$ up to $L = 200$.
6. **Crossover degree** $34$ ($589\ \mathrm{km}$) for the stated synthetic error
   spectrum.

The demonstration is print-only, fixed-seed, network-free, and runs in under a
second.

## 8. Exercises

Full sets with worked solutions are in
[`exercises/03-spherical-harmonic-solutions-exercises.md`](./exercises/03-spherical-harmonic-solutions-exercises.md)
and
[`exercises/03-spherical-harmonic-solutions-solutions.md`](./exercises/03-spherical-harmonic-solutions-solutions.md).

- **★** Compute $N$ and $\Delta g$ at the equator for $C_{20} = 2\times10^{-5}$
  (note $\bar P_{20}(0) = -\sqrt{5}/2$).
- **★** State the number of coefficients for $L = 75$ and the implied
  half-wavelength.
- **★★** Derive the $(l-1)$ factor from $T \propto r^{-(l+1)}$ and the
  fundamental equation, and check dimensionally.
- **★★** Given $\sigma_{l} = 10^{-5}(2/l)^{2}$ and
  $\epsilon_{l} = 3\times10^{-9}l^{1/2}$, find the crossover degree.
- **★★★** Design a numerical experiment to show that an inverted
  high-degree coefficient set is determined by the chosen regularisation rather
  than the data, and state the diagnostic that reveals it.

## 9. Mastery checkpoint

Do this without notes:

> A synthetic model has a single zonal coefficient $C_{20} = 1.0\times10^{-5}$
> with $R = 6371\ \mathrm{km}$, $GM = 3.986004418\times10^{14}\
> \mathrm{m^{3}\,s^{-2}}$ and
> $\gamma = 9.80665\ \mathrm{m\,s^{-2}}$. **(a)** Compute $N$ and
> $\Delta g$ at the pole and at the equator. **(b)** Explain the sign difference
> using $\bar P_{20}$. **(c)** State the coefficient count and half-wavelength
> for $L = 40$. **(d)** For a synthetic signal spectrum
> $\sigma_l = 10^{-5}(2/l)^{2}$ and error $\epsilon_l = 10^{-9}l$, find the
> crossover degree. **(e)** State what a coefficient above the crossover
> represents.

*Answers.* **(a)** At the pole $\bar P_{20}(1) = \sqrt{5} = 2.236068$:

$$N = (6.379836\times10^{6})(10^{-5})(2.236068) = +142.66\ \mathrm{m},
\qquad \Delta g = (9.8203)(10^{-5})(2.236068) = 21.96\ \mathrm{mGal}.$$

At the equator $\bar P_{20}(0) = -\sqrt{5}/2 = -1.118034$, giving
$N = -142.66\ \mathrm{m}$ and $\Delta g = -21.96\ \mathrm{mGal}$: the same
magnitude and the opposite sign, because $\bar P_{20}$ changes sign at
$\theta = 54.7^{\circ}$. **(c)** $41^{2} = 1681$ coefficients and
$\pi R/40 = 500\ \mathrm{km}$. **(d)** $10^{-5}(2/l)^{2} = 10^{-9}l$
gives $l^{3} = 4\times10^{4}$ and $l^{*} = 34.2$, so the highest integer
degree above noise is $34$ (half-wavelength $589\ \mathrm{km}$). **(e)** It is
determined by the regularisation and the a priori spectrum — an assumption
written into the model, not a measurement.
## 10. Common pitfalls

1. **Ignoring the normalisation.** A factor of $\sqrt{2l+1}$ grows quickly and
   looks like a spectral difference.
2. **Confusing the geoid with the gravity anomaly.** The $(l-1)$ factor makes them
   qualitatively different fields from identical coefficients.
3. **Reading a degree-variance plot without the error spectrum.** Half of such a
   plot may be regularisation.
4. **Quoting "resolution" without the half-wavelength convention.** $\pi R/L$,
   $2\pi R/L$ and the Rayleigh criterion differ by factors of two.
5. **Treating the coefficients as independent.** A real covariance matrix has
   strong correlations, especially near the crossover.
6. **Subtracting two models with different conventions or reference fields** and
   calling the difference a mass change.

## 11. Real-world applications

- **Combined global models.** Every global gravity model is a published list of
  coefficients plus a covariance; the degree range where each data type
  dominates follows from the transfer functions of
  [02](02-goce.md) and [01](01-grace-gracefo.md).
- **Geoid computation for height systems.** The coefficients supply the
  long-wavelength part of the geoid in the remove–restore decomposition of
  [07-07-01](../07-geoid-and-height-modern/01-geoid-determination.md).
- **Orbit determination and altimetry.** Coefficients to a stated degree are an
  operational input for satellite orbits.
- **Model comparison.** Because the basis is fixed by the differential equation,
  two models can be compared degree by degree; that is how differences between
  analyses are attributed to data or to method.

## 12. Further reading

- **Heiskanen, W. A. & Moritz, H., *Physical Geodesy*** — the classical
  boundary-value formulation and Stokes' theory.
- **Kaula, W. M., *Theory of Satellite Geodesy*** — the degree-variance
  description of the gravitational field.
- **Torge, W. & Müller, J., *Geodesy*** — notation, conventions and the
  combination of data types.
- **Hofmann-Wellenhof, B. & Moritz, H., *Physical Geodesy*** — modern
  treatments of geodetic boundary-value problems.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Editions and years are omitted
> because they differ between printings.

## 13. Related lessons

- [01 GRACE and GRACE-FO: Mission Concept and Data Products](01-grace-gracefo.md) —
  the mass-anomaly interpretation of low-degree coefficient changes.
- [02 GOCE, Gravity Gradients and the Static Field](02-goce.md) —
  the curvature observable that determines the higher degrees.
- [04 Mass Concentration Solutions, Leakage and Filtering](04-mascons-and-leakage.md) —
  what happens when these coefficients are filtered into a map.
- [07-07-01 Determining the Geoid: Stokes, Remove-Restore, Kriging](../07-geoid-and-height-modern/01-geoid-determination.md) —
  the boundary-value problem that uses this expansion.
- [18-inverse-problems](../../18-inverse-problems/README.md) — rank, resolution
  and regularisation in general terms.

## 14. Related modules

- [Satellite Gravimetry](./README.md) — this module's index.
- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — the
  boundary-value problem this expansion solves.
- [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md) —
  spherical-harmonic modelling as a numerical method in its own right.
- [26-reference-library](../../26-reference-library/README.md) — symbols, units
  and constants used without re-derivation.

## 15. Self-assessment checklist

- [ ] I can write the potential expansion and state its normalisation.
- [ ] I can verify the normalisation by quadrature.
- [ ] I can derive $N = T/\gamma$ and the $(l-1)$ factor.
- [ ] I can compute $N$ and $\Delta g$ from a single coefficient.
- [ ] I can fit and interpret a degree-variance slope with a control.
- [ ] I can compute $(L+1)^{2}$ and $\pi R/L$ for a stated $L$.
- [ ] I can find a crossover degree and state what lies above it.
