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

### 3.4 Poisson's equation, derived from Gauss's law

Section 3.3 quoted $\nabla^2\Phi = 4\pi G\rho$. It is worth deriving, because the
sign and the factor $4\pi$ are both consequences of a physical statement rather
than conventions.

Gauss's law for gravity states that the flux of $\mathbf{g}$ through any closed
surface equals $-4\pi G$ times the enclosed mass:

$$\oint_{\partial V}\mathbf{g}\cdot\mathrm{d}\mathbf{A} = -4\pi G\,M_\text{enc}
= -4\pi G\int_V\rho\,\mathrm{d}V .$$

Apply the divergence theorem to the left side and equate the integrands, valid
for every volume:

$$\int_V \nabla\cdot\mathbf{g}\,\mathrm{d}V = -4\pi G\int_V\rho\,\mathrm{d}V
\qquad\Longrightarrow\qquad
\nabla\cdot\mathbf{g} = -4\pi G\rho .$$

Now substitute the definition of the potential, $\mathbf{g} = -\nabla\Phi$:

$$\nabla\cdot(-\nabla\Phi) = -4\pi G\rho
\qquad\Longrightarrow\qquad
\boxed{\;\nabla^2\Phi = 4\pi G\rho\;}$$

Units: $[\Phi] = \mathrm{m^2\,s^{-2}}$, so $[\nabla^2\Phi] =
\mathrm{m^2s^{-2}/m^2} = \mathrm{s^{-2}}$; and
$[G\rho] = \mathrm{m^3kg^{-1}s^{-2}\cdot kg\,m^{-3}} = \mathrm{s^{-2}}$. ✓

**Physical interpretation.** The Laplacian measures how a function differs from
its local average (Section 3.6 makes this precise). So $\nabla^2\Phi = 4\pi G\rho$
says: *wherever there is mass, the potential at a point lies below the average of
its neighbourhood — the function is "dished" inward toward the mass.* Where
$\rho = 0$ there is no dishing at all, and the function is exactly its own local
average: harmonic.

### 3.5 The dipole field, derived from a potential

The dipole formula was asserted in Section 3.2. Deriving it shows why the
$r^{-3}$ and the factor $(3\cos^2\!-$-type angular dependence are inevitable.

In a current-free region a magnetic scalar potential exists with
$\mathbf{B} = -\mu_0\nabla\psi$. For a dipole,

$$\psi(\mathbf{r}) = \frac{1}{4\pi}\frac{\mathbf{m}\cdot\hat{\mathbf{r}}}{r^2}
= \frac{1}{4\pi}\frac{\mathbf{m}\cdot\mathbf{r}}{r^3}.$$

Differentiate. For a fixed vector $\mathbf{m}$,

$$\frac{\partial}{\partial x_i}\frac{m_jx_j}{r^3}
= \frac{m_i}{r^3} - \frac{3(\mathbf{m}\cdot\mathbf{r})\,x_i}{r^5},$$

so

$$\mathbf{B} = -\mu_0\nabla\psi
= -\frac{\mu_0}{4\pi}\left[\frac{\mathbf{m}}{r^3}
- \frac{3(\mathbf{m}\cdot\mathbf{r})\,\mathbf{r}}{r^5}\right]
= \frac{\mu_0}{4\pi}\,\frac{3(\mathbf{m}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}}
-\mathbf{m}}{r^3},$$

which is the asserted dipole field. Two consequences are now visible rather than
memorised:

- the field is $r^{-3}$ because $\psi$ is $r^{-2}$ (one more derivative, one more
  power — the rule of Section 3.1);
- the field is **tangential to $\hat{\mathbf{r}}$ in the sense that
  $\hat{\mathbf{r}}\cdot\mathbf{B} = 2(\mu_0/4\pi)(\mathbf{m}\cdot\hat{\mathbf{r}})/r^3 \ne 0$**:
  a dipole field is *not* radial, unlike the monopole field of gravity. That is
  why magnetic anomalies have sign reversals and gravity anomalies of a compact
  body do not.

**Measured check.** A synthetic dipole of $|\mathbf{m}| = 5\times10^{6}$ A m²
about 300 m from the observer gives $B_z = -18.518519$ nT while $B_x = B_y = 0$,
so $|\mathbf{B}| = 18.518519$ nT = $\frac{\mu_0}{4\pi}\frac{m}{r^3}$ exactly, as
the algebra requires for a transverse observation. At 100 m the same observable
is 1000.0000 nT against 1.3717 nT at 900 m: a ratio of 729.0 for a ratio of 9.0
in distance, i.e. exactly $9^3$. ✓

### 3.6 Why "no interior extrema": the mean-value property, derived

The smoothness consequence of Section 3.3 becomes precise through the
**mean-value property** of harmonic functions:

$$\Phi(\mathbf{x}_0) = \frac{1}{4\pi R^2}\oint_{|\mathbf{x}-\mathbf{x}_0| = R}
\Phi(\mathbf{x})\,\mathrm{d}A .$$

**Proof sketch.** Apply the divergence theorem to $\mathbf{g} = -\nabla\Phi$ over
the ball $|\mathbf{x}-\mathbf{x}_0| \le R$, the reverse of Section 3.4:
$0 = \int_V\nabla\cdot\mathbf{g}\,\mathrm{d}V = \oint -\partial\Phi/\partial n\,
\mathrm{d}A$ shows the surface integral of the normal derivative vanishes, and
differentiating the spherical average with respect to $R$ gives zero. Hence the
average is independent of $R$; letting $R\to0$ identifies it with $\Phi(\mathbf{x}_0)$. ∎

**Extremum principle.** Suppose $\Phi$ has a strict local maximum at an interior
point $\mathbf{x}_0$. Then for small $R$ every point on the sphere has
$\Phi < \Phi(\mathbf{x}_0)$, so the average of the sphere is strictly less than
$\Phi(\mathbf{x}_0)$ — contradicting the mean-value property. Therefore a
non-constant harmonic function has **no interior extremum**; its extrema lie on
the boundary of the region.

**Consequence for surveys.** For a gravity survey the region is the half-space
above the sources, and its boundary is the observation surface plus "infinity".
So the extreme values of an anomaly occur *on the measurement surface itself* or
at infinity — never floating above it. Practically:

- a potential-field anomaly cannot be narrower than the surface sampling
  suggests without extra information; there is no "lens" above the surface;
- any computed field with an interior extremum is a numerical or processing
  artefact;
- the anomaly's extremum position is where the source is closest, which is how
  half-width depth rules get their physical content.

### 3.7 The multipole hierarchy, and why gravity and magnetics differ

Expand the potential of a finite source in powers of $1/r$ about the origin:

$$\Phi(\mathbf{r}) = -\frac{G}{r}\left[M + \frac{\mathbf{d}\cdot\hat{\mathbf{r}}}{r}
+ \frac{1}{2}\frac{Q_{ij}\hat r_i\hat r_j}{r^2} + \cdots\right],$$

with $M$ the total mass (monopole), $\mathbf{d}$ the dipole moment (which
vanishes when the origin is at the centre of mass), and $Q_{ij}$ the quadrupole
moment. The successive terms fall as $r^{-1}, r^{-2}, r^{-3}$, and each
derivative of the potential adds one power.

**The structural difference.** For gravity the monopole term $M > 0$ always
exists, so the leading far-field behaviour is $r^{-2}$ for the field and the
next term is a *relative* correction of order (size/depth). For magnetostatics no
magnetic monopole exists, so the first term in the expansion is absent, the
leading behaviour is the dipole $r^{-3}$, and the next term is the quadrupole.
This is the *reason* for the decay-exponent difference asserted in Section 3.1,
and it has a practical consequence: a magnetic anomaly's shape is more sensitive
to the body's orientation and internal structure than a gravity anomaly's, while
its amplitude dies faster with depth.

**Measured confirmation.** The demonstration's point mass gives a factor of 64.0
in amplitude for a factor of 8 in depth ($= 8^2$), and its dipole gives 729.0 for
a factor of 9 ($= 9^3$). The exponents are the levels in the hierarchy.

### 3.8 The multipole hierarchy, quantified by measurement

Section 3.7 gave the hierarchy in words. Here it is with the demonstration's
numbers, because the arithmetic makes the structure unmistakable.

| source level | field decay | measured amplitude ratio | depth ratio |
|---|---|---|---|
| monopole (gravity) | $r^{-2}$ | 64.0 at 100 m → 800 m | 8 |
| dipole (magnetics) | $r^{-3}$ | 729.0 at 100 m → 900 m | 9 |

$8^2 = 64$ and $9^3 = 729$ exactly, to the precision of the table. **The exponent
of the decay equals the level of the multipole at which the source first appears**,
and there is no way to change the exponent without changing the source's
symmetry. A distribution with zero total mass (a positive body over a negative
one of equal mass) has no monopole term and decays as $r^{-3}$, which is one
reason gravity interpretations of *compensated* structures (isostatic roots, salt
overhangs) have much shorter spatial reach than the bodies' sizes suggest.

**The practical asymmetry.** Because a magnetic source has no monopole, its
leading term is the dipole and it decays one power faster than a gravitating mass
of the same compactness. That is why magnetometers see shallow geology so well
and deep geologic structure so poorly, while gravimeters see the deep structure
and blur the shallow detail — a division of labour that follows from Section 3.4's
Poisson equation plus Section 3.7's expansion, and from nothing else.

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

### 6.3 Worked arithmetic: from potential to field, both ways

**Forward: potential → field.** For the point mass of Section 6.1 with
$m = 10^{10}$ kg, $d = 250$ m, the potential on the vertical through the mass is

$$\Phi(z) = -\frac{Gm}{|z-d|} = -\frac{(6.6743\times10^{-11})(10^{10})}{|z-250|}
= -\frac{0.66743}{|z-250|}\ \mathrm{m^2\,s^{-2}} .$$

At $z = 0$: $\Phi = -0.66743/250 = -2.6697\times10^{-3}$ m² s⁻². For a
central difference the two samples are

$$\Phi(\pm h) = -\frac{0.66743}{250 \mp h}
\qquad\Longrightarrow\qquad
\frac{\mathrm{d}\Phi}{\mathrm{d}z}\bigg|_{0}
\approx \frac{\Phi(h)-\Phi(-h)}{2h},$$

which is the slowness-average form $-\mathrm{d}\Phi/\mathrm{d}z =
\frac{0.66743}{250^2-h^2}$ — exactly $Gm/(d^2-h^2)$, tending to $Gm/d^2$ as
$h\to0$. Evaluate numerically rather than by hand: the demonstration reports
$-\mathrm{d}\Phi/\mathrm{d}z = 1.067888\times10^{-5}$ m s⁻², and the analytic
value $Gm/d^2 = (6.6743\times10^{-11})(10^{10})/250^2 = 1.067888\times10^{-5}$
m s⁻². The relative difference is $3.1\times10^{-11}$.

**Where that $3\times10^{-11}$ comes from.** It is not physics. The two values of
$\Phi$ being differenced are $-2.6697\times10^{-3}$ and $-2.6718\times10^{-3}$
m² s⁻², which agree to six significant figures; subtracting them discards five of
them, and the surviving digits carry the rounding of each. This is catastrophic
cancellation ([01-01-04](../../01-mathematics/01-arithmetic/04-floating-point.md)),
and the cure is analytic differentiation or a larger step with a Richardson
extrapolation — not a smaller step, which makes it worse.

**Inverse: field → potential.** Because $\Phi = -Gm/r$, inverting the measured
field is a two-step problem: measure $g_z$ (one component of a gradient), then
integrate to get $\Phi$ up to a constant. The constant is unobservable — which is
exactly why every potential-field method ties to a datum, and why "absolute"
gravity is a metrological achievement rather than a geometric one.

### 6.4 A shortcut that fails: "the field is harmonic, so I can extrapolate it"

Because $\Phi$ is harmonic above the sources, an analytic continuation of the
measured field exists and is unique. The temptation is to conclude that
extrapolation is therefore safe.

It is not. Section 3.3's relation $\hat h(k) = 2\pi G e^{-|k|d}$ shows the reason
in one line: continuing *downward* by $\Delta d$ multiplies a component of
wavelength $\lambda$ by $e^{2\pi\Delta d/\lambda}$. For $\Delta d = 300$ m:

| $\lambda$ (m) | amplification |
|---|---|
| 1000 | 6.59 |
| 500 | 43.4 |
| 200 | $1.23\times10^{4}$ |

A 1% error in the data becomes a 123-fold error in the model at $\lambda = 200$ m.
The measurement in
[05-01-04](../01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md)
confirms the practical consequence: inverting for a source at 1200 m depth drives
the condition number to $8.27\times10^{15}$ and the recovered model RMS to
$5.66\times10^{14}$ kg/m², while the data misfit *degrades* to
$1.0\times10^{-4}$ — the linear algebra, not the physics, has taken over.

**The rule.** Harmonicity guarantees uniqueness of the continuation; it says
nothing about stability. Uniqueness and stability are different properties, and
only the first follows from Laplace's equation.

### 6.5 Extended worked example: measuring the maximum principle and the decay powers

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
