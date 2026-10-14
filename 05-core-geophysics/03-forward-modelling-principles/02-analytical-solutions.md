---
id: 05-03-02
title: "Analytical Solutions for Simple Bodies (Sphere, Sheet, Dyke)"
level: advanced
prereqs: ["05-03-01"]
tags: [analytical-solutions, sphere, sheet, dyke, depth-rules]
---

# Analytical Solutions for Simple Bodies (Sphere, Sheet, Dyke)

## Learning objectives

1. **State** the exact analytical solution for a sphere, a horizontal sheet and
   a 2-D dyke, with the assumptions of each.
2. **Derive** the sphere solution from the shell theorem and the 2-D line-mass
   solution by direct integration.
3. **Extract** depth from an anomaly profile using the characteristic points of
   each solution, and state the uncertainty of the estimate.
4. **Explain** why these solutions are the standard benchmarks for numerical
   codes.
5. **Quantify** when the far-field point-mass approximation is acceptable.

## Prerequisites

- [05-03-01 The Forward Problem](./01-forward-problem.md)
- [02-08-01 Gravitational Potential](../../02-physics/08-potential-theory/01-gravitational-potential.md)

## 1. Intuition

A handful of source shapes have closed-form fields. They matter for three
reasons: they generate intuition about depth rules; they are the benchmarks
against which every numerical code is tested; and they are the first
interpretation model applied to a real anomaly. Their weakness is that real
bodies are not spheres, so the "depth" they return is a shape-dependent
apparent depth — and the shape is precisely what you are trying to determine.

## 2. The three solutions

**Sphere** (radius $a$, density contrast $\Delta\rho$, centre depth $d$). By the
shell theorem the external field equals that of a point mass at the centre:

$$g_z(x) = \frac{G\,m\,d}{(x^2+d^2)^{3/2}}, \qquad m = \tfrac43\pi a^3\Delta\rho.$$

Exact for all $x$ outside the sphere. Peak $= Gm/d^2$ at $x=0$.

**2-D horizontal cylinder** (line mass, density contrast $\Delta\rho$, radius
$a$, depth $d$, infinite along strike), with $\lambda = \pi a^2\Delta\rho$:

$$g_z(x) = \frac{2G\lambda\,d}{x^2+d^2}.$$

**Semi-infinite horizontal sheet / step** and **dyke**: obtained by integrating
the line-mass solution; the dyke of finite width $w$ is the difference of two
step solutions and requires no elementary closed form for the *magnetic*
equivalent at arbitrary dip — for the *gravity* of a 2-D polygon, the polygon
formula (Talwani) is exact.

## 3. Derivations

### 3.1 Sphere from superposition of shells

A uniform spherical shell produces, outside itself, exactly the field of a point
mass at its centre (Newton's shell theorem). Summing shells of radius $s$ from
$0$ to $a$ with mass $dm = \Delta\rho\,4\pi s^2 ds$:

$$g_z = \frac{G}{d^2}\int_0^a \Delta\rho\,4\pi s^2\,ds
= \frac{G}{d^2}\Delta\rho\tfrac43\pi a^3 = \frac{Gm}{d^2}.$$

Dimensions: $\mathrm{m^3kg^{-1}s^{-2}\cdot kg\,m^{-2}} = \mathrm{m\,s^{-2}}$. ✓

### 3.2 Line mass by integrating a rod

A rod of cross-section $dA$ at depth $d$ with density $\Delta\rho$ has line
density $\lambda = \Delta\rho\,dA$. The 2-D Green's function for gravity is
$g_z = 2G\lambda d/(x^2+d^2)$; equivalently
$\mathbf{g} = 2G\lambda\,\hat{\mathbf{r}}/r$ for the full vector, whose vertical
component is $2G\lambda d/r^2$. Verification: the demo's planar sheet is this
kernel summed over windings.

### 3.3 Depth from half-width

Sphere: setting $g_z(x) = \frac12 g_z(0)$ gives (Section 3 of
[05-01-03](../01-what-geophysics-measures/03-resolution-depth-tradeoff.md))

$$w_{1/2} = 1.532842\,d.$$

Cylinder: setting $d/(x^2+d^2) = 1/(2d)$ gives $x = d$, so
$w_{1/2} = 2.000000\,d$.

**Therefore the same measured half-width implies different depths for different
shapes** — a factor of 1.53/2.00 = 0.77. Depth estimates from potential fields
are shape-dependent, always.

## 4. Units and dimensional analysis

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | excess mass | kg |
| $\lambda$ | line density | kg m⁻¹ |
| $a$ | radius or half-width | m |
| $d$ | depth to centre/axis | m |
| $x$ | horizontal offset | m |

Both formulas give m s⁻²; both are converted to mGal by dividing by $10^{-5}$.

## 5. Assumptions

1. **Homogeneous, uniformly magnetised/dense body.**
2. **The 2-D solutions** assume infinite strike length. A body of length $L$ is
   "2-D" for stations within roughly $L/2$ of its centre; beyond that the
   anomaly decays toward the 3-D form.
3. **No remanence** for the magnetic analogues (induced magnetisation only).
4. **Isolated body**: no interference from other sources.
5. **Flat observation surface** and, for the sheet/step solutions, a
   homogeneous overburden.

## 6. Worked examples (measured)

**6.1 Sphere at three depths** (radius 60 m, contrast 500 kg/m³,
$m = 4.5239\times10^8$ kg): 0.30194, 0.07548, 0.01887 mGal at 100, 200, 400 m,
scaling exactly as $d^{-2}$.

**6.2 Reduced-to-dipole test.** `code/dipole_vs_body_demo.py` shows that a
uniformly magnetised sphere matches the point dipole to a measured relative
difference of $1.5\times10^{-14}$ at 250 m and $5.1\times10^{-15}$ at 1000 m —
the exactness the shell theorem predicts.

**6.3 A prism's far field is** *not* exactly a dipole. For a prism with
half-extents (80, 60, 50) m, the measured relative difference from the
equal-moment dipole falls from $1.29\times10^{-1}$ at 200 m to
$4.88\times10^{-4}$ at 3200 m, by a factor of about 4.0 per doubling of
distance. Since the dipole itself decays as $r^{-3}$, the absolute error decays
as $r^{-5}$: for an observer on the symmetry axis the quadrupole term vanishes
and the octupole dominates. **The far-field approximation converges slowly
enough that it should be checked, not assumed.**

**6.4 Depth rule discrepancy.** A measured half-width of 500 m gives
$d = 500/1.532842 = 326$ m for a sphere but $d = 500/2.000 = 250$ m for a
cylinder — a 30% difference. Report the assumed shape with every depth estimate.

## 7. Python demonstration

`code/prism_gravity_demo.py` (prism closed form versus quadrature) and
`code/dipole_vs_body_demo.py` (body versus dipole, with the measured convergence
in Section 6.3). Both print the model inputs as SYNTHETIC and the constants as
cited.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/02-analytical-solutions-exercises.md`](./exercises/02-analytical-solutions-exercises.md).

**Common mistakes.** (1) Applying a sphere depth rule to a dyke. (2) Assuming
2-D when $L/d$ is small. (3) Quoting a depth without the assumed shape.
(4) Using the point-dipole formula for a body whose dimension is comparable to
its depth. (5) Ignoring remanence in magnetic work, which changes the anomaly
shape and defeats depth rules.

**Applications.** Depth-to-basement from magnetic profiles; dyke location in
mineral exploration; sphere approximations for compact orebodies; benchmark
testing of finite-element and boundary-element codes.

## Extended worked example: apparent depth depends on the assumed shape

Take a single synthetic anomaly and interpret it three ways. Suppose a measured
half-width of 600 m, a peak of 0.5 mGal, and a density contrast of 400 kg/m³.

**Under a sphere assumption**, $w_{1/2} = 1.532842d$ gives
$d = 600/1.532842 = 391.4$ m. Then the required excess mass is
$m = g_\text{peak}d^2/G = (5\times10^{-6})(391.4)^2/(6.6743\times10^{-11})
= 1.148\times10^{10}$ kg, implying a radius
$a = (3m/4\pi\Delta\rho)^{1/3} = 1.90\times10^{2}$ m, i.e. $a/d = 0.485$.

**Under a cylinder assumption**, $w_{1/2} = 2.000d$ gives $d = 300.0$ m. The
required line density is $\lambda = g_\text{peak}d/(2G)
= (5\times10^{-6})(300)/(2\cdot6.6743\times10^{-11}) = 1.124\times10^{7}$ kg/m,
implying a radius $a = \sqrt{\lambda/(\pi\Delta\rho)} = 94.6$ m, so
$a/d = 0.315$.

**Under a prism (2-D) assumption**, depth lands between the other two, closer to
the cylinder.

All three fit the same two numbers. They differ by 30% in depth and by a factor
of two in the implied body size. The data have not chosen; you have. The
defensible statement is: *"the anomaly is consistent with a compact body at
300–400 m depth or with a tabular body at about 300 m; discriminating between
them requires either more data (a second profile, gradients, or a different
method) or an independent constraint."*

**A quantitative rule of thumb.** Because $w_{1/2}$ is proportional to $d$ for
every compact shape, the *ratio* of two half-widths measured on the same anomaly
is a shape-sensitive quantity, whereas a single half-width is not. Where data
permit, measure two characteristic distances (half-width and the width at
one-tenth maximum, for instance) and use their ratio to constrain the shape
before converting the width into a depth.

**Verification against an independent kernel.** The dipole-versus-body
demonstration provides the magnetic analogue: a sphere matches the point dipole
to $1.5\times10^{-14}$ relative, while a prism only approaches it as
$r^{-2}$ in the relative error, with measured factors of 4.07, 4.05, 4.01 and
4.00 per doubling of distance. Interpreters who use the point-dipole formula at
depths comparable to the body size are making an error of tens of percent, and
the demonstration quantifies exactly how large.

## 9. Further reading

- **Blakely (1995).** Chapters 4, 9. Level: advanced.
- **Talwani, M. & Heirtzler, J. R. (1964).** Computation of magnetic anomalies
  caused by two-dimensional structures. Level: advanced. The polygon method.
- **Telford, Geldart & Sheriff (1990).** Chapter 3. Level: intermediate.

## 10. Related lessons

- [05-03-03 Superposition and Building Complex Models](./03-superposition.md)
- [05-03-05 Validating Forward Codes Against Analytic Benchmarks](./05-forward-model-validation.md)
- [08-03-05 Magnetic Depth Estimation](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/05-magnetic-depth-estimation.md)

## Self-assessment checklist

- [ ] I can derive the sphere solution from the shell theorem.
- [ ] I can derive both half-width constants and compute a depth from each.
- [ ] I can state when a body is effectively 2-D.
- [ ] I can explain why a prism is not exactly a dipole.
- [ ] I can quote a depth estimate with its shape assumption.
