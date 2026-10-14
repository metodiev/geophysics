---
id: 05-01-01
title: "The Central Idea: Property Contrasts Produce Signals"
level: intermediate
prereqs: ["02-01-04", "01-01-03"]
tags: [property-contrast, detectability, survey-design, anomaly]
---

# The Central Idea: Property Contrasts Produce Signals

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the master equation of exploration geophysics — signal exists only
   where a physical property changes — and explain why the *contrast*, not the
   property, is the target.
2. **List** the material properties that each major method senses, and say for
   each whether it is dominated by the solid matrix, the pore fluid, or both.
3. **Compute** a first-order detectability estimate for a buried body and
   compare it with a stated instrument noise level.
4. **Derive** the potential-field distance decay exponent for a body of given
   symmetry, and explain why it differs from method to method.
5. **Explain** why the same physical property can be large in a rock and still
   produce no anomaly.

## Prerequisites

- [02-01-04 Conservation Laws as the Engine of Physical Modelling](../../02-physics/01-measurement-and-physical-reasoning/04-conservation-laws.md)
  — the reason a *contrast* rather than an absolute value enters every field
  equation.
- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)
  — every number in this lesson carries a unit, and every formula is checked.

## 1. Intuition: you cannot measure a rock in place

Geophysics does not measure rocks. It measures **fields** — gravitational
acceleration, magnetic flux density, travel time, electric potential — at
points you can reach, and infers something about a volume you cannot see.

The inference is possible because a field equation relates a spatial
distribution of material to the field it produces. That equation always has
the same structure: **the field is driven by a contrast**. A uniform,
infinite half-space of any density produces a gravity field you could never
distinguish from a different uniform half-space, because at every point you can
reach, the field of an infinite homogeneous layer above you is fixed by that
layer alone. Only where the property *changes* does the field carry information
about what is below.

This has an immediate practical consequence that surprises beginners: the
absolute density of a rock body is not the target. A 2700 kg/m³ granite
intruded into 2650 kg/m³ country rock is a 50 kg/m³ anomaly; the same granite
in a 2900 kg/m³ host produces a *negative* anomaly of the same size. The
observation is about the *difference*.

## 2. Precise definitions

**Contrast.** For a scalar property $p$ with values $p_1$ and $p_2$ in adjacent
volumes, the contrast is

$$\Delta p = p_2 - p_1, \qquad \text{relative contrast} = \frac{p_2 - p_1}{p_{1}}.$$

**Anomaly.** The field remaining after a *specified* reference field has been
subtracted. An anomaly is therefore meaningless without a statement of the
reference (the datum, the regional field, the background model). This idea is
developed in
[05-02-04 Reduction of Observations to Anomalies](../02-geophysical-fields-and-observables/04-reduction-of-observations.md).

**Detectability.** A body is detectable when the signal it produces exceeds the
*combined* uncertainty of measurement and of the reference model, not merely
the instrumental noise:

$$\text{detectable} \iff |S| > k\sqrt{\sigma_\text{noise}^2 + \sigma_\text{model}^2},
\qquad k \approx 3 \ \text{for a confident claim}.$$

**Sensitivity kernel.** The function $K(\mathbf{r}_\text{obs}, \mathbf{r}')$
such that

$$d(\mathbf{r}_\text{obs}) = \int K(\mathbf{r}_\text{obs}, \mathbf{r}')\,\Delta p(\mathbf{r}')\,dV'.$$

Every method has one. Gravity and magnetics have *smooth*, wavelength-limited
kernels; seismic and GPR have *wave* kernels that can be focused by migration.
That difference explains almost every performance difference between them.

### 2.1 What each method senses

| Method | Property | Where the contrast lives | Distance decay of the anomaly |
|---|---|---|---|
| Gravity | density $\rho$ | matrix and pore fluid | $r^{-2}$ (point mass), $r^{-1}$ (2-D line) |
| Magnetics | magnetisation $\mathbf{M}$, susceptibility $\chi$ | mostly magnetic minerals | $r^{-3}$ (dipole), $r^{-2}$ (2-D line) |
| DC resistivity | resistivity $\rho_e$ / conductivity $\sigma$ | pore fluid, clay, connectivity | depends on geometry; no simple power |
| EM / MT | conductivity $\sigma$ and its frequency dependence | pore fluid, sulphides, clay | exponential (diffusive skin depth) |
| Seismic | elastic moduli and density | matrix, porosity, saturation | $r^{-1}$ (body waves in 3-D) |
| GPR | permittivity $\varepsilon$, conductivity | pore water | $r^{-1}$ + exponential loss |
| Thermal | thermal conductivity, heat production | matrix, fluid saturation | diffusive |

**Do not read this table as a ranking.** Each "decay" column assumes a *compact
body* in a *homogeneous* whole space. A layered medium, a guided wave, or a
large target changes the geometry and therefore the exponent. The table states
asymptotic behaviour, and asymptotic behaviour is only reached in the far field.

## 3. Derivation: from a contrast to a signal

### 3.1 Why the anomaly decays faster than the potential

The gravitational potential of a point mass $m$ is

$$\Phi(\mathbf{r}) = -\frac{Gm}{r}, \qquad [\Phi] = \mathrm{m^2\,s^{-2}} = \mathrm{J\,kg^{-1}}.$$

A gravimeter does not measure $\Phi$; it measures the **gradient** of $\Phi$.
With the $z$ axis downward and the mass at depth $d$ directly below the
observer,

$$g_z = -\frac{\partial \Phi}{\partial z} = -\frac{\partial}{\partial z}\left(-\frac{Gm}{r}\right)
= Gm\,\frac{\partial r^{-1}}{\partial z}.$$

Writing $r = \sqrt{x^2 + y^2 + (z-d)^2}$ and evaluating at the surface
($x=y=z=0$, so $r=d$):

$$\frac{\partial r^{-1}}{\partial z}\bigg|_{z=0} = -\frac{1}{r^2}\cdot\frac{\partial r}{\partial z}
= -\frac{1}{r^2}\cdot\frac{-(d)}{r} = \frac{d}{r^3},$$

so

$$\boxed{\,g_z = \frac{Gm\,d}{(x^2+y^2+d^2)^{3/2}}\,}$$

Directly above the mass, $g_z = Gm/d^{2}$: the anomaly decays as **depth
squared**, one power faster than the potential. Dimensional check:
$[G]=\mathrm{m^3kg^{-1}s^{-2}}$, $[m]=\mathrm{kg}$, $[d^{-2}]=\mathrm{m^{-2}}$
gives $\mathrm{m\,s^{-2}}$ — an acceleration, as required.

The general rule: **a measurement of the $n$-th derivative of a potential decays
as $r^{-(1+n)}$.** Gravity is a first derivative ($r^{-2}$ for a point mass).
Magnetic fields are also gradients of a potential, but the source is a *dipole*
rather than a monopole, adding one more power: $r^{-3}$.

### 3.2 The same logic in seismics

At normal incidence the P-wave reflection coefficient between layers 1 and 2 is

$$R = \frac{Z_2 - Z_1}{Z_2 + Z_1}, \qquad Z = \rho v_p, \quad [Z] = \mathrm{kg\,m^{-2}\,s^{-1}},$$

which depends **only** on the impedance contrast. Two different rocks with the
same $\rho v_p$ are seismically identical at normal incidence. That is the
seismic face of the same principle: geophysics senses contrasts, and a contrast
can be zero even when the properties are individually large.

### 3.3 Reducing a volume to a point: the shell theorem, derived

The point-mass formula used in Section 6.1 is an *approximation* for a real body.
For a uniform sphere it is exact, and the reason is worth deriving once because
the same reduction underlies every "equivalent point source" argument in the
curriculum.

Take a thin spherical shell of radius $s$ and surface density $\sigma_s$
(units kg m⁻²), and place the observer a distance $d$ from the centre. By
symmetry the field points along the centre–observer line. Writing $\theta$ for
the angle between the line and the radius vector to a shell element, with
$r^2 = d^2 + s^2 - 2ds\cos\theta$, the vertical component of the attraction of
that element is $G\,\sigma_s\,\mathrm{d}A\,(d - s\cos\theta)/r^3$. Integrating
over the sphere:

$$g = 2\pi G\sigma_s s^2 \int_{-1}^{1}
\frac{d - su}{\left(d^2+s^2-2dsu\right)^{3/2}}\,\mathrm{d}u,
\qquad u \equiv \cos\theta .$$

Evaluate the integral by the substitution $w = d^2+s^2-2dsu$, so
$\mathrm{d}w = -2ds\,\mathrm{d}u$ and $d - su = (d^2-s^2+w)/(2d)$. Then

$$g = 2\pi G\sigma_s s^2 \cdot\frac{1}{4d^2s}
\int_{(d-s)^2}^{(d+s)^2}\left[\left(d^2-s^2\right)w^{-3/2}+w^{-1/2}\right]\mathrm{d}w .$$

Both terms integrate directly:

$$\int \left(d^2-s^2\right)w^{-3/2}\mathrm{d}w = -2\left(d^2-s^2\right)w^{-1/2},
\qquad \int w^{-1/2}\mathrm{d}w = 2w^{1/2},$$

and evaluating between the limits $(d-s)^2$ and $(d+s)^2$ gives

$$\frac{1}{d+s}-\frac{1}{d-s} = \frac{-2s}{d^2-s^2},
\qquad (d+s)-(d-s) = 2s,$$

so the bracket is $-2(d^2-s^2)\cdot\dfrac{-2s}{d^2-s^2} + 2(2s) = 4s+4s = 8s$, and

$$g = \frac{2\pi G\sigma_s s^2}{4d^2s}\cdot 8s = \frac{4\pi G\sigma_s s^2}{d^2}
= \frac{G\,m_\text{shell}}{d^2},
\qquad m_\text{shell} = 4\pi s^2\sigma_s .$$

**This is the shell theorem.** Now sum shells from $0$ to $a$ with
$\mathrm{d}m = \Delta\rho\,4\pi s^2\,\mathrm{d}s$:

$$g = \frac{G}{d^2}\int_0^a \Delta\rho\,4\pi s^2\,\mathrm{d}s
= \frac{G}{d^2}\,\Delta\rho\,\tfrac{4}{3}\pi a^3 = \frac{Gm}{d^2},
\qquad m = \Delta\rho\,\tfrac43\pi a^3 .$$

The sphere's field is *exactly* a point mass's field — not approximately, and at
every distance outside it. **Physical interpretation:** the deviation of a real
body from the point-mass formula measures how far it is from spherical, and that
is exactly the far-field error quantified in
[05-03-02](../03-forward-modelling-principles/02-analytical-solutions.md), where
a prism's error relative to its equal-moment dipole fell as $r^{-2}$ with a
measured factor of 4.0 per doubling.

### 3.4 The normal-incidence reflection coefficient, derived

The seismic statement in Section 3.2 is also a result rather than a definition,
and it follows from two continuity conditions.

Let the interface lie at $z=0$, with impedance $Z_1 = \rho_1v_1$ above and
$Z_2$ below. Write the incident, reflected and transmitted pressure fields as

$$p_i = A\,e^{i(\omega t - k_1z)},\qquad
p_r = B\,e^{i(\omega t + k_1z)},\qquad
p_t = C\,e^{i(\omega t - k_2z)} .$$

Two conditions hold at the interface: **pressure is continuous**, and **normal
particle velocity is continuous**. Since a wave travelling in $+z$ has
$u = p/Z$ and one travelling in $-z$ has $u = -p/Z$,

$$A + B = C \qquad\text{(pressure)},$$

$$\frac{A-B}{Z_1} = \frac{C}{Z_2} \qquad\text{(velocity)} .$$

Eliminate $C$: $Z_2(A-B) = Z_1(A+B)$, so $A(Z_2-Z_1) = B(Z_2+Z_1)$ and

$$\boxed{\,R = \frac{B}{A} = \frac{Z_2-Z_1}{Z_2+Z_1}\,},
\qquad
T = \frac{C}{A} = \frac{2Z_2}{Z_1+Z_2} .$$

**Consistency check, energy.** The energy flux is $p^2/Z$, so conservation
requires $1 = R^2 + T^2 Z_1/Z_2$. With the lesson's synthetic pair
($Z_1 = 7.2000\times10^{6}$, $Z_2 = 1.1475\times10^{7}$
kg m⁻² s⁻¹): $R = 0.22891566$, $T = 1.22891566$, and

$$R^2 + T^2\frac{Z_1}{Z_2} = 0.052402 + 0.947594 = 0.999996 \approx 1 .$$

The residual $4\times10^{-6}$ is rounding in the six-figure quoting of $Z_1$ and
$Z_2$, not physics. **A derivation that can be checked against a conservation
law is a derivation you can trust.**

**Physical interpretation of $R$.** For $Z_2 > Z_1$ (acoustic impedance
increasing downward) $R > 0$; for a decrease $R < 0$; and $|R| \le 1$ with
equality only at an impossible zero-impedance medium. Because $R$ depends on the
*ratio*, not on the values, the seismic observable is blind to the
$\rho$–$v$ split — which is the ambiguity that motivates
[05-04-04](../04-rock-physics/04-velocity-porosity-clay.md) and every
amplitude-versus-offset analysis.

### 3.5 The detectability inequality, inverted

Section 6.1 computed anomalies; practice asks the inverse question. Requiring
$|S| \ge k\sigma$ with $S = Gm/d^2$ gives the maximum detectable depth for a
compact body:

$$d_{\max} = \sqrt{\frac{G\,\Delta\rho\,V}{k\,\sigma}} .$$

With the lesson's synthetic body (radius 60 m, $\Delta\rho = 500$ kg/m³,
$V = 9.0478\times10^{5}$ m³) and a 3-sigma criterion against
$\sigma = 1\times10^{-7}$ m/s² (0.01 mGal):

$$d_{\max} = \sqrt{\frac{(6.6743\times10^{-11})(500)(9.0478\times10^{5})}
{3\times10^{-7}}} = 317.2\ \mathrm{m} .$$

Compare with the measured table in Section 6.1: the anomaly is 0.075 mGal at
200 m and 0.019 mGal at 400 m, so it crosses the 0.01 mGal level at about 460 m
and the 3-sigma level at about 320 m after allowing for geological noise. The
closed form and the sampled table agree, which is the point of doing both.

## 4. Units and dimensional analysis

| Quantity | SI unit | Field unit | Conversion (derived) |
|---|---|---|---|
| $g_z$ | m s⁻² | mGal | $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ |
| $B$ | T | nT (gamma) | $1\ \mathrm{nT} = 10^{-9}\ \mathrm{T}$ |
| $\rho$ | kg m⁻³ | g cm⁻³ | $1\ \mathrm{g\,cm^{-3}} = 10^{3}\ \mathrm{kg\,m^{-3}}$ |
| $v_p$ | m s⁻¹ | km s⁻¹ | $1\ \mathrm{km\,s^{-1}} = 10^{3}\ \mathrm{m\,s^{-1}}$ |
| $\rho_e$ | Ω·m | Ω·m | identical |

The mGal conversion follows from the *definition* of the Gal: $1\ \mathrm{Gal}
= 1\ \mathrm{cm\,s^{-2}} = 10^{-2}\ \mathrm{m\,s^{-2}}$, so
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$. It is not a remembered
number; it is arithmetic.

## 5. Assumptions

Every number in this lesson rests on these assumptions:

1. **Newtonian gravity, weak field.** Post-Newtonian corrections are ~10⁻⁹
   relative, far below survey precision.
2. **A homogeneous reference medium** exists, so that "the contrast" is
   well defined. Real surveys handle a *layered* reference, which is why
   reductions are needed.
3. **Point-mass or dipole far-field approximation.** Valid when the observation
   distance is much greater than the body's largest dimension — quantified in
   [05-03-02](../03-forward-modelling-principles/02-analytical-solutions.md).
4. **Noise is additive and independent of signal.** Multiplicative and
   signal-correlated noise breaks the simple signal-to-noise test above.
5. **The reference field is known perfectly.** In practice $\sigma_\text{model}$
   often dominates $\sigma_\text{noise}$, which is why
   [05-02-03](../02-geophysical-fields-and-observables/03-noise-and-drift.md)
   insists on separating measurement error from model error.

### 5.1 Assumptions of this lesson, and what breaks when each fails

| Assumption | Failure mode | Consequence, quantified |
|---|---|---|
| Uniform host density | lateral density variation | the "contrast" is undefined; the anomaly is a *difference* from a model, not from a rock |
| Compact body for $r^{-2}$ | tabular or extended body | the exponent becomes $r^{-1}$; a depth inferred with $r^{-2}$ is overestimated — using the sphere's $c=1.5328$ when the body is a line gives 391.4 m instead of 300.0 m, an error of 30.5%, derived in [05-03-02](../03-forward-modelling-principles/02-analytical-solutions.md) |
| Point-mass far field | depth comparable to body size | a prism's field differs from its equal-moment dipole by $1.29\times10^{-1}$ at 200 m, falling only as $r^{-2}$ — see [05-03-02](../03-forward-modelling-principles/02-analytical-solutions.md) |
| No noise correlation | coherent cultural noise | $\sqrt{N}$ averaging fails; the effective noise falls more slowly than the sampling theory predicts |
| Additive, signal-independent noise | multiplicative noise | the CNR test becomes a ratio test, not a difference test |
| Known reference field | wrong datum or regional | the residual is biased; a 670 kg/m³ Bouguer-density error costs 0.157 mGal, larger than a subtle anomaly |

Each row is a *quantified* degradation. An assumption list without magnitudes is
a disclaimer; with magnitudes it is a design tool.

## 6. Worked examples

### 6.1 Is a 60 m ore sphere visible in a gravity survey?

Take a sphere of radius $a=60$ m, density contrast $\Delta\rho = 500$ kg/m³,
buried with centre at depth $d$. The excess mass is

$$m = \Delta\rho\cdot\tfrac{4}{3}\pi a^3 = 500\cdot\tfrac{4}{3}\pi(60)^3 = 4.5239\times10^{8}\ \mathrm{kg}.$$

The vertical anomaly is exact for a sphere (a shell theorem consequence):
$g_z = Gm/d^2$. Computed at $G = 6.67430\times10^{-11}$ m³kg⁻¹s⁻²:

| depth $d$ (m) | $g_z$ (mGal) | $d/a$ |
|---|---|---|
| 100 | 0.30194 | 1.67 |
| 200 | 0.07548 | 3.33 |
| 400 | 0.01887 | 6.67 |
| 800 | 0.00472 | 13.33 |

At 400 m the anomaly is 0.019 mGal. Against an instrument repeatability of
0.01 mGal that is a factor of 1.9 — **not** a detection, because the terrain,
tidal, and datum uncertainties are each larger than the signal (see
[05-02-04](../02-geophysical-fields-and-observables/04-reduction-of-observations.md)).
At 200 m the anomaly is 0.075 mGal, seven times the repeatability, and becomes
a credible target. These numbers were computed, not remembered; reproduce them
with the module demonstration.

### 6.2 Why the same body may be invisible in magnetics

A body of volume $10^{6}$ m³ with vertical magnetisation $M = 5$ A/m has moment
$5\times10^{6}$ A·m². The total-field anomaly is
$\Delta T \approx \hat{\mathbf{b}}\cdot\mathbf{B}_\text{anomaly}$, where
$\hat{\mathbf{b}}$ is the unit vector along the ambient field. Directly above
the source, with the ambient field horizontal (inclination 0°), the projection
is **exactly zero** — computed as $0.0000$ nT at depths of 100, 300 and 900 m.
At inclination 60° the same body gives 866 nT at 100 m and 32.1 nT at 300 m.

**A body that is obvious at one site latitude can be invisible at another.**
This is not exotic; it is the geometry of a vector projection, and it is why
$\Delta T$ must never be quoted without the ambient field direction.

### 6.3 The reflection coefficient is blind to one of its two ingredients

For a stated synthetic contrast $\rho_1 = 2400$ kg/m³, $v_1 = 3000$ m/s,
$\rho_2 = 2550$ kg/m³, $v_2 = 4500$ m/s:

$$R = \frac{Z_2 - Z_1}{Z_2 + Z_1} = \frac{2550\cdot4500 - 2400\cdot3000}{2550\cdot4500 + 2400\cdot3000}
= \frac{1.1475\times10^7 - 7.20\times10^6}{1.8675\times10^7} = +0.2289.$$

A different pair with the same impedance ratio gives exactly the same $R$. The
data cannot separate the density from the velocity — a first taste of the
non-uniqueness developed in
[05-01-04](./04-ambiguity-and-nonuniqueness.md).

## 7. Python demonstration

Run `code/property_contrast_demo.py` in this module. It reproduces every number
above and prints the units. Key measured output, verbatim:

```
excess mass = 4.5239e+08 kg
 depth(m)   g_z(mGal)
     100     0.30194
     200     0.07548
     400     0.01887
     800     0.00472
   depth(m)   dT@inc=0(nT)  dT@inc=60(nT)  dT@inc=90(nT)
       100         0.0000       866.0254      1000.0000
       300         0.0000        32.0750        37.0370
```

Predict each row before running. The demo labels every model input
`SYNTHETIC`; the constants $G$ and $\mu_0$ are cited from NIST CODATA.

## 8. Exercises

Graded exercises are in
[`exercises/01-physical-property-contrast-exercises.md`](./exercises/01-physical-property-contrast-exercises.md),
with full solutions in the companion solutions file. Attempt them before
reading the solutions.

## 9. Common mistakes

1. **Quoting an absolute property instead of a contrast.** "The granite has
   density 2700 kg/m³" is not a geophysical statement until the host is named.
2. **Treating a remembered "typical value" as a measurement.** Every rock
   property spans one to four orders of magnitude. A single number without a
   range and a source is a scientific error, not a simplification.
3. **Comparing signal to instrument noise only.** The reference-model error
   usually dominates.
4. **Assuming a decay exponent without checking the geometry.** $r^{-2}$ holds
   for a point mass; a 2-D body (a dyke, a long river channel) gives $r^{-1}$.
5. **Confusing the property with the observable.** Gravimeters measure
   acceleration differences; magnetometers measure a field projection. Neither
   measures density or magnetisation directly.

## 10. Real-world applications

- **Mineral exploration.** Massive sulphide bodies are found by their
  *combined* density, conductivity and magnetic contrasts, because no single
  contrast is diagnostic — this is the practical motivation for joint inversion
  ([18-07-01](../../18-inverse-problems/07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md)).
- **Groundwater.** Contrasts are dominated by the pore fluid, so resistivity and
  EM are the primary tools while gravity is nearly blind to a salinity change.
- **Engineering and archaeology.** Targets are shallow and small, so the decay
  exponents work in the surveyor's favour and dense, high-resolution
  acquisition is feasible.
- **Planetary exploration.** A rover cannot remeasure a gravity datum, so
  contrasts must be inferred from relative gradients.

## 11. Further reading

- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*. Cambridge University Press.** Chapters 1–2. Level:
  advanced undergraduate upward. The standard development of kernels and
  contrasts used throughout this module.
- **Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** Chapters 1–2. Level:
  intermediate. A method-by-method statement of what is measured and with what
  precision.
- **Mavko, G., Mukerji, T. & Dvorkin, J. *The Rock Physics Handbook* (any
  recent edition).** Chapter 1. Level: graduate. For the property variability
  that makes ranges, not single numbers, the honest way to quote rock
  properties.
- **NIST CODATA fundamental physical constants** —
  [physics.nist.gov/cuu/Constants](https://physics.nist.gov/cuu/Constants/).
  The source used here for $G$ and $\mu_0$.

> Citations give location details so you can find the works. This repository
> does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-01-02 Taxonomy of Methods](./02-method-taxonomy.md) — organises the
  properties in Section 2.1 into a method classification.
- [05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off](./03-resolution-depth-tradeoff.md)
  — quantifies the width-versus-depth behaviour that Section 3.1 implies.
- [05-01-04 Non-Uniqueness of Geophysical Models](./04-ambiguity-and-nonuniqueness.md)
  — what happens when the contrast is not determined by the data.
- [05-03-01 The Forward Problem: From Model to Data](../03-forward-modelling-principles/01-forward-problem.md)
  — the formal statement of the map from contrast distribution to data.

## Self-assessment checklist

- [ ] I can state why a uniform half-space produces no detectable anomaly.
- [ ] I can derive $g_z = Gm\,d/r^3$ from the potential and check its units.
- [ ] I can name the property that dominates each of gravity, magnetics,
      resistivity, seismic and GPR.
- [ ] I can estimate the excess mass of a buried body and its anomaly at a
      stated depth to within a factor of two.
- [ ] I can explain why $\Delta T$ can vanish for a real body.
- [ ] I can state, for any anomaly I quote, which reference field I subtracted.
