---
id: 05-02-01
title: "Scalar and Vector Fields; Potentials and Gradients"
level: advanced
prereqs: ["02-08-01", "02-08-02"]
tags: [potential-theory, scalar-field, vector-field, gradient, laplace]
---

# Scalar and Vector Fields; Potentials and Gradients

## Learning objectives

1. **Distinguish** a scalar field from a vector field and state which
   geophysical observables belong to each class.
2. **Derive** the potential of a point mass and a point dipole, and obtain the
   measured field as a gradient or a curl of the potential.
3. **Show** that in a source-free region both potentials satisfy Laplace's
   equation, and state what that implies for the observable.
4. **Explain** why every potential-field measurement is a *derivative*: this is
   the origin of the $r^{-2}$ and $r^{-3}$ decays and of the resolution limits.
5. **Check** the dimensions of a potential and of each of its derivatives.

## Prerequisites

- [02-08-01 Newtonian Gravitational Potential and Field](../../02-physics/08-potential-theory/01-gravitational-potential.md)
- [02-08-02 Laplace's Equation and Harmonic Functions](../../02-physics/08-potential-theory/02-laplace-equation.md)
- [01-01-03 Units and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)

## 1. Intuition

A scalar field attaches one number to each point in space (temperature,
pressure, gravitational potential). A vector field attaches a vector (velocity,
electric field, magnetic flux density). Geophysics measures both, but the
potential fields — gravity and magnetics — have a special structure: their
vector fields are *derivatives of a single scalar function*. That single fact
explains their smoothness, their non-uniqueness, and why they cannot be focused
the way a wave field can.

## 2. Precise definitions

**Scalar field** $\phi(\mathbf{r})$: a function $\mathbb{R}^3 \to \mathbb{R}$.

**Vector field** $\mathbf{F}(\mathbf{r})$: a function $\mathbb{R}^3 \to
\mathbb{R}^3$.

**Conservative field.** $\mathbf{F}$ is conservative if
$\mathbf{F} = -\nabla\phi$ for some scalar $\phi$, equivalently
$\nabla\times\mathbf{F} = \mathbf{0}$ in a simply connected region.

**Potential.** For gravity, $\Phi(\mathbf{r}) = -G\sum_i m_i/|\mathbf{r}-
\mathbf{r}_i|$, so that the measured acceleration is
$\mathbf{g} = -\nabla\Phi$. For magnetics, one works either with a *scalar*
potential (in current-free regions) or with the *vector* potential
$\mathbf{A}$ such that $\mathbf{B} = \nabla\times\mathbf{A}$.

**Geophysical observables.** A gravimeter measures one component of
$\mathbf{g} = -\nabla\Phi$ (usually the vertical, or a difference of it). A
magnetometer measures either one component of $\mathbf{B}$ or the total
magnitude $|\mathbf{B}|$. Neither measures a potential directly.

## 3. Derivations

### 3.1 Point mass: potential to field

$$\Phi(\mathbf{r}) = -\frac{Gm}{r}, \qquad r = |\mathbf{r}-\mathbf{r}'|.$$

$$\nabla\frac{1}{r} = -\frac{\mathbf{r}-\mathbf{r}'}{r^3}
\implies \mathbf{g} = -\nabla\Phi = -Gm\frac{\mathbf{r}-\mathbf{r}'}{r^3}.$$

So $g_z$ (downward, mass at $(0,0,d)$, observer at origin) is
$Gm\,d/d^3 = Gm/d^2$ directly above — the $r^{-2}$ law, obtained as one
derivative of the $r^{-1}$ potential.

### 3.2 Dipole: one more derivative

For a magnetic dipole of moment $\mathbf{m}$,

$$\mathbf{B} = \frac{\mu_0}{4\pi}\left[\frac{3(\mathbf{m}\cdot\hat{\mathbf{r}})
\hat{\mathbf{r}} - \mathbf{m}}{r^3}\right],$$

which is $r^{-3}$: one power more than the gravitational case, because the
source is a dipole rather than a monopole. Exactly this formula is verified
against a volume integral over a uniformly magnetised sphere in
`../03-forward-modelling-principles/code/dipole_vs_body_demo.py`, where
the measured relative difference is $1.5\times10^{-14}$ at 250 m.

### 3.3 Laplace's equation in a source-free region

$\mathbf{g} = -\nabla\Phi$ and $\nabla\cdot\mathbf{g} = -4\pi G\rho$ give
$\nabla^2\Phi = 4\pi G\rho$. Where $\rho = 0$,

$$\nabla^2\Phi = 0.$$

**Consequence.** A harmonic function is analytic and cannot have a local maximum
or minimum in the interior of its domain (the maximum principle). Therefore a
potential-field anomaly must be a *smooth* function with its extrema on the
boundary of the measurement surface. It cannot be a spike. This is the deepest
reason that potential-field resolution degrades with depth
([05-01-03](../01-what-geophysics-measures/03-resolution-depth-tradeoff.md)).

## 4. Units and dimensional analysis

| Quantity | Symbol | SI unit | Dimension |
|---|---|---|---|
| Gravitational potential | $\Phi$ | m² s⁻² | energy per unit mass |
| Gravitational acceleration | $\mathbf{g}$ | m s⁻² | — |
| Magnetic scalar potential | $\psi$ | A | $[\mathbf{B}]=\mathrm{T}$, $\mu_0\nabla\psi$ has T |
| Magnetic flux density | $\mathbf{B}$ | T | kg s⁻² A⁻¹ |
| Vector potential | $\mathbf{A}$ | T m | $\nabla\times\mathbf{A}$ has T |

Check: $[\Phi] = [G][m]/[r] = \mathrm{m^3kg^{-1}s^{-2}\cdot kg\,m^{-1}} =
\mathrm{m^2\,s^{-2}}$. ✓ And $[\nabla\Phi] = \mathrm{m^2s^{-2}/m} =
\mathrm{m\,s^{-2}}$. ✓

## 5. Assumptions

1. **Newtonian gravity, static sources.** No time variation, no relativistic
   correction.
2. **Current-free region** for the magnetic scalar potential to exist.
3. **Superposition.** The sum over $i$ above assumes linearity, which holds to
   extraordinary precision for gravity.
4. **The measurement surface is outside all sources.** Otherwise Laplace's
   equation does not apply at the observation point and the smoothness argument
   changes.
5. **A magnetometer measures $\Delta T$ as a projection**, not $|\mathbf{B}|$
   in isolation — a first-order approximation valid when the anomaly is small
   compared with the main field.

## 6. Worked examples

**6.1 Numerical gradient versus analytic.** Using
`code/field_conventions_demo.py`:
a synthetic $10^{10}$ kg point mass at 250 m gives a central-difference
$-\mathrm{d}\Phi/\mathrm{d}z = 1.067888\times10^{-5}$ m s⁻², and the analytic
$Gm/d^2 = 1.067888\times10^{-5}$ m s⁻². Relative difference
$3.1\times10^{-11}$, i.e. dominated by the finite-difference truncation error.
This confirms that the observable is the derivative of the potential.

**6.2 Measured decay powers.** The same point mass gives 0.30194 mGal at 100 m
and 0.00472 mGal at 800 m: a factor of 64 for a factor of 8 in depth, exactly
$d^{-2}$. A dipole at the same depths would give $d^{-3}$: 1000 nT at 100 m and
1.37 nT at 900 m (a factor of 730 for a factor of 9).

## 7. Python demonstration

Run `code/field_conventions_demo.py` in module 02. Section 2 prints the
numerical-versus-analytic gradient check; Section 3 prints the dipole
components, $|\mathbf{B}|$, and $\Delta T$ for three ambient inclinations, which
is the projection lesson made numeric.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/01-scalar-vs-vector-fields-exercises.md`](./exercises/01-scalar-vs-vector-fields-exercises.md).

**Common mistakes.**

1. **Saying a gravimeter "measures the potential."** It measures a gradient of
   it — usually one component, usually a difference between two stations.
2. **Confusing $|\mathbf{B}|$ with $\Delta T$.** They agree only when the
   anomaly is small relative to the main field.
3. **Assuming smoothness is a processing artefact.** It is a property of
   harmonic functions.
4. **Dropping signs.** $\mathbf{g} = -\nabla\Phi$ with the negative sign
   defined by the sign convention for $\Phi$.
5. **Using $\mu_0 = 4\pi\times10^{-7}$ without saying so.** It is
   $1.25663706212\times10^{-6}$ H/m in the 2019 SI.

**Real-world applications.** Airborne magnetic gradiometry measures field
*gradients* directly, which suppresses the regional field without any
processing; borehole gravity measures a vertical gradient, which is far more
sensitive to nearby mass than the absolute field.

## Extended worked example: measuring the maximum principle and the decay powers

**The gradient check, in numbers.** A synthetic point mass of
$10^{10}$ kg at 250 m depth has potential $\Phi(z) = -Gm/|z-d|$ along the
vertical through it. A central difference with $h = 10^{-4}$ m at $z = 0$ gives

$$-\frac{\mathrm{d}\Phi}{\mathrm{d}z} \approx \frac{\Phi(h)-\Phi(-h)}{-2h}
= 1.067888\times10^{-5}\ \mathrm{m\,s^{-2}},$$

against the analytic $Gm/d^2 = (6.6743\times10^{-11})(10^{10})/250^2
= 1.067888\times10^{-5}$ m s⁻². The relative difference is
$3.1\times10^{-11}$: the residual is finite-difference truncation error
($O(h^2)$ for a central difference, amplified by cancellation between
$\Phi(\pm h)$, which differ only in the sixth significant figure). **The
observable is confirmed to be a derivative of the potential**, and the size of
that residual is itself a lesson in catastrophic cancellation
([01-01-04](../../01-mathematics/01-arithmetic/04-floating-point.md)).

**The decay powers, in numbers.** The same mass at 100 m and 800 m gives
0.30194 mGal and 0.00472 mGal — a factor of $0.30194/0.00472 = 64.0$ for a
factor of 8 in depth, exactly $8^2$. For a dipole of the same geometry, the
demonstration gives 1000.0000 nT at 100 m and 1.3717 nT at 900 m: a factor of
729.0 for a factor of 9, exactly $9^3$. **Two observables, two different powers,
both predicted by counting derivatives of the potential.**

**Component versus total field, in numbers.** A vertical dipole of moment
$5\times10^{6}$ A·m² observed 300 m due north gives $\mathbf{B}$ with
$B_z = -18.518519$ nT and $B_x = B_y = 0$, so $|\mathbf{B}| = 18.518519$ nT.
Projected onto ambient fields of inclination 0°, 60° and 90°, the total-field
anomaly is 0.000000, $-16.037507$ and $-18.518519$ nT respectively. The first is
exactly zero. A single body, one field, three different "measurements" — and a
survey can be blind in one geometry and sensitive in another.

**The smoothness consequence, stated as a test.** Because $\Phi$ is harmonic
outside the source, the sampled $g_z$ on the surface has no interior extremum
other than the one nearest the source, which sits on the boundary of the
sampled profile. A numerical check: sample $g_z(x)$ densely, locate the maximum,
and confirm it lies at the endpoint closest to the source when the profile does
not include the point directly above it. Any interior sharp spike in a
potential-field anomaly is a processing artefact, not geology.

## 9. Further reading

- **Blakely (1995), *Potential Theory in Gravity and Magnetic Applications*.**
  Chapters 1–2. Level: advanced.
- **Kellogg, O. D. *Foundations of Potential Theory*.** Level: graduate.
  The rigorous treatment of harmonic functions.
- **Telford, Geldart & Sheriff (1990).** Chapters 2–3. Level: intermediate.

## 10. Related lessons

- [05-02-02 Units and Conventions](./02-field-measurement-units.md)
- [05-02-04 Reduction of Observations to Anomalies](./04-reduction-of-observations.md)
- [02-08-03 Spherical Harmonics and Multipole Expansions](../../02-physics/08-potential-theory/03-spherical-harmonics.md)
- [02-08-06 Uniqueness Theorems and Boundary Conditions](../../02-physics/08-potential-theory/06-uniqueness-theorems.md)

## Self-assessment checklist

- [ ] I can convert a potential into its field and check the units.
- [ ] I can state why gravity is $r^{-2}$ and magnetics $r^{-3}$.
- [ ] I can explain the maximum principle and its resolution consequence.
- [ ] I can state precisely what a gravimeter and a magnetometer output.
- [ ] I can compute a numerical gradient and compare it with a closed form.
