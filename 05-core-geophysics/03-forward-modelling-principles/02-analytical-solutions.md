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

### 3.4 The 2-D line mass, from the Green's function

The line-mass formula follows from the Green's function for the 2-D Laplace
operator. A line source of mass per unit length $\lambda$ (kg m⁻¹) at
$(0,d)$ produces the field

$$\mathbf{g} = \frac{2G\lambda}{r}\,\hat{\mathbf{r}},
\qquad \mathbf{r} = (x,\,-d) \text{ from source to observer},$$

whose vertical component at the surface is

$$g_z(x) = \frac{2G\lambda}{r}\cdot\frac{d}{r}
= \frac{2G\lambda\,d}{x^2+d^2}.$$

Units: $[G\lambda/d] = \mathrm{m^3kg^{-1}s^{-2}\cdot kg\,m^{-1}\cdot m^{-1}}
= \mathrm{m\,s^{-2}}$ ✓. The $2G\lambda/r$ prefactor (rather than $G\lambda/r^2$)
is the signature of two-dimensionality: the field of a line falls as $r^{-1}$ in
the *vector* sense, so its vertical component falls as $r^{-2}$ only because the
projection factor $d/r$ also falls as $r^{-1}$.

### 3.5 The semi-infinite sheet and the dyke, by integration

Any 2-D body can be built by integrating the line kernel over its cross-section.
Integrating from $x' = 0$ to $\infty$ at depth $d$ gives the **semi-infinite
sheet**, which is the 2-D analogue of a fault step:

$$g_z(x) = 2G\sigma\int_0^\infty\frac{d}{\left(x-x'\right)^2+d^2}\,\mathrm{d}x'
= 2G\sigma\left[\arctan\!\left(\frac{x'-x}{d}\right)\right]_{x'=0}^{\infty}
= 2G\sigma\left[\frac{\pi}{2}+\arctan\!\left(\frac{x}{d}\right)\right],$$

using $\arctan(\infty) = \pi/2$ and the oddness of $\arctan$. A finite-width
**dyke** of width $w$ is the difference of two such steps separated by $w$, so

$$g_z^\text{dyke}(x) = 2G\sigma\left[
\arctan\!\left(\frac{x}{d}\right) -
\arctan\!\left(\frac{x-w}{d}\right)\right],$$

a function with two extrema and a closed-form peak. **Physical interpretation:**
the step function saturates — its field tends to $0$ and $2\pi G\sigma$ at the two
ends — while the dyke's field returns to zero at infinity. That is why a *fault*
produces a long-wavelength ramp in a gravity profile and a *dyke* produces a
localised anomaly, even though both are 2-D bodies at the same depth.

### 3.6 Why a prism is not a dipole: the surface-charge argument, derived

Section 6.3 measured that a prism's field differs from its equal-moment dipole
with a *relative* error falling as $r^{-2}$, not $r^{-1}$. That is a strong
statement and it deserves a derivation.

The field of a uniformly magnetised body equals the field of magnetic "charges"
on its surface. Formally, the scalar potential is

$$\psi(\mathbf{r}) = \frac{1}{4\pi}\int_V
\mathbf{M}\cdot\nabla'\!\left(\frac{1}{|\mathbf{r}-\mathbf{r}'|}\right)\mathrm{d}V'
= \frac{1}{4\pi}\oint_{\partial V}
\frac{\mathbf{M}\cdot\hat{\mathbf{n}}}{|\mathbf{r}-\mathbf{r}'|}\,\mathrm{d}A',
$$

the volume term becoming a surface term by the divergence theorem because
$\nabla'\cdot\mathbf{M} = 0$ for uniform $\mathbf{M}$. So the source is the
surface charge density $\sigma_m = \mathbf{M}\cdot\hat{\mathbf{n}}$.

**Apply it to a box with $\mathbf{M} = M\hat{\mathbf{z}}$** and half-extents
$h_x, h_y, h_z$. Only the faces with $\hat{\mathbf{n}} = \pm\hat{\mathbf{z}}$
carry charge: $\sigma_m = +M$ on the top, $-M$ on the bottom. Now compute the
box's quadrupole moment about its centre, $Q_{zz} = \oint\sigma_m(3z'^2 -
r'^2)\,\mathrm{d}A'$. On the top face $z' = h_z$ and $x',y'$ range over the
cross-section, so the integrand is $3h_z^2 - (x'^2+y'^2+h_z^2) = 2h_z^2 - x'^2 -
y'^2$, giving

$$Q_{zz}^\text{top} = M\,A\left[2h_z^2 -
\tfrac{1}{3}\left(h_x^2+h_y^2\right)\right],$$

and the bottom face has the same integrand (since $z'^2 = h_z^2$ there too) with
$\sigma_m = -M$, so it contributes **exactly the negative**. Hence

$$Q_{zz} = Q_{zz}^\text{top} + Q_{zz}^\text{bottom} = 0 .$$

**Measured check.** Numerically integrating $3z'^2-r'^2$ over both charged faces
of the demonstration's prism ($h_x = 80$, $h_y = 60$, $h_z = 50$ m) gives
$Q_{zz} = 0.0$ — exact cancellation to the precision of the integral.

**The consequence.** With the quadrupole absent, the leading non-dipole term on
the axis is the **octupole**, whose field falls as $r^{-5}$ against the dipole's
$r^{-3}$. The ratio therefore falls as $r^{-2}$, and the measured relative
difference fell with factors of 4.07, 4.05, 4.01 and 4.00 per doubling of
distance — a fitted exponent of 2.01, exactly as this derivation requires.
**Off-axis the cancellation does not occur**, the quadrupole survives, and the
relative error decays only as $r^{-1}$ — which is why the same demo's exponent is
geometry-dependent, as its own commentary says.

**Why this matters practically.** Depth and shape estimation from a magnetic
anomaly assume the dipole term. On-axis the error at $r = 4a_{\text{eff}}$ is
$1.3\times10^{-1}$ (13%), and the fall-off is fast enough that at
$r = 40a_{\text{eff}}$ it is $4.9\times10^{-4}$. The practical rule is
$r \gtrsim 10\,a$ for 1% accuracy, and the justification is now the vanishing
quadrupole rather than an assertion.

### 3.7 Depth-rule error propagation, derived

Depth estimates from half-widths are the most-used quantitative output of
potential-field interpretation, so their uncertainty deserves the same treatment
as any other measurement.

From $w_{1/2} = c\,d$ with $c$ a shape constant,

$$d = \frac{w_{1/2}}{c}
\qquad\Longrightarrow\qquad
\frac{\partial d}{\partial w_{1/2}} = \frac{1}{c},
\qquad
\frac{\partial d}{\partial c} = -\frac{w_{1/2}}{c^2} = -\frac{d}{c} .$$

**Two independent error sources, both first order in $d$:**

$$\frac{\delta d}{d} = \frac{\delta w}{w} - \frac{\delta c}{c}
\qquad\Longrightarrow\qquad
\left(\frac{\delta d}{d}\right)^2
= \left(\frac{\delta w}{w}\right)^2 + \left(\frac{\delta c}{c}\right)^2
\quad\text{(if independent)} .$$

**Numbers for the two standard shapes:**

| assumed shape | $c$ | depth for $w = 600$ m | $\partial d/\partial w$ |
|---|---|---|---|
| sphere | 1.532842 | 391.4 m | 0.6524 |
| 2-D line / cylinder | 2.000000 | 300.0 m | 0.5000 |

So a 10% error in the measured half-width produces a 10% depth error (0.65 m per
metre, or 0.50 for the cylinder) — straightforward and unremarkable. The
*shape* term is the dangerous one:

$$\frac{\delta c}{c}\bigg|_\text{sphere vs line} = \frac{2.000000 - 1.532842}
{1.532842} = 0.305 .$$

**A wrong shape assumption is worth a 30% depth error, three times a generous
10% width error, and it is systematic.** That is why the lesson insists on
reporting the assumed shape: the shape term dominates the error budget, and it
cannot be reduced by measuring the anomaly more carefully.

**The combined budget, stated as a procedure.** (1) Measure $w$ and quote its
uncertainty, including the effect of the sampling interval. (2) State the assumed
shape and, where the data permit, evaluate the depth for two shapes and report the
range. (3) Compute the ratio $w_{1/2}/w_{1/10}$ as a shape diagnostic
([05-01-03](../01-what-geophysics-measures/03-resolution-depth-tradeoff.md)) and
let it discriminate. (4) Report the depth as an interval with its dominant
uncertainty named. **A single depth number without its shape assumption is not a
result.**

### 3.8 Amplitude and width together: why one number is not a depth

There is a trap in using amplitude as a depth indicator, and its resolution
explains why interpretation uses the *shape* of an anomaly rather than its size.

From $A = Gm/d^2$,

$$d = \sqrt{\frac{Gm}{A}}
\qquad\Longrightarrow\qquad
\frac{\partial d}{\partial A} = -\frac{d}{2A},
\qquad\text{so a 10\% amplitude error gives a 5\% depth error}$$

— a *square-root* penalty, which sounds favourable. The catch is that $m$ is
unknown. Treating $A$ alone as a depth indicator therefore requires an *assumed*
mass, and an assumed mass is exactly what the survey was meant to determine:

$$\text{if } m \text{ is wrong by a factor } 2,\ \text{then }
d \text{ is wrong by a factor } \sqrt{2} = 1.41 .$$

**Use two observables instead.** A profile provides both a peak amplitude $A$ and
a half-width $w$. Two equations, two unknowns:

$$w = c\,d \quad\Longrightarrow\quad d = \frac{w}{c},
\qquad
A = \frac{Gm}{d^2} \quad\Longrightarrow\quad m = \frac{A\,d^2}{G} .$$

So the width determines the depth (given a shape) and the amplitude then
determines the mass — and the *consistency* of the two is a test of the shape
assumption. If the mass implied by the amplitude is geologically implausible
(a negative density contrast, or 10 kg/m³) the assumed shape is wrong.

**Worked arithmetic.** Take $w_{1/2} = 600$ m, $A = 0.5$ mGal, and test both
shapes:

| assumed shape | $c$ | $d = w/c$ | implied $m = Ad^2/G$ | implied radius at $\Delta\rho = 400$ kg/m³ |
|---|---|---|---|---|
| sphere | 1.532842 | 391.4 m | $1.148\times10^{10}$ kg | 190 m |
| 2-D line | 2.000000 | 300.0 m | $1.124\times10^{7}$ kg **per metre** | 94.6 m |

The 2-D quantity is computed from the *line* formula $A = 2G\lambda/d$, giving
$\lambda = Ad/2G = 1.124\times10^{7}$ kg m⁻¹ (not from the 3-D $m = Ad^2/G$,
which would mislabel a line density as a mass). Its implied radius,
$\sqrt{\lambda/\pi\Delta\rho} = 94.58$ m, is **half** the sphere's 189.8 m
(ratio $94.58/189.8 = 0.498$).

Both are self-consistent; they differ by 30% in depth and by a factor of two in
size. **The data have not chosen** — which is the non-uniqueness of
[05-01-04](../01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md)
appearing in the simplest possible interpretation, and the reason depth rules must
always be reported with their shape assumption.

**The one thing the two-observable system does constrain.** Because $d$ and $m$
trade off through $w$ and $A$ separately, the *combination* $A\,w^2 \propto
m\,c^2$ is well determined even when the shape is not. So a survey can determine
the excess mass robustly and the depth only up to the shape ambiguity — which is
often the honest answer: "the body has an excess mass of $7\times10^{9}$ to
$1.1\times10^{10}$ kg at between 300 and 390 m depth."

### 3.9 The slope-based depth rule, derived

The half-width rules require a peak. For a monotone anomaly — a step, a fault, a
region boundary — there is no half-width, and the depth must come from the *slope*
instead.

For the semi-infinite sheet of Section 3.5,

$$g_z(x) = 2G\sigma\left[\frac{\pi}{2}+\arctan\!\left(\frac{x}{d}\right)\right]
\qquad\Longrightarrow\qquad
\frac{\mathrm{d}g_z}{\mathrm{d}x} = \frac{2G\sigma\,d}{x^2+d^2} .$$

The gradient is **maximum at $x = 0$**, directly over the edge, with value

$$\left(\frac{\mathrm{d}g_z}{\mathrm{d}x}\right)_{\max} = \frac{2G\sigma}{d}
\qquad\Longrightarrow\qquad
\boxed{\;d = \frac{2G\sigma}{\left(\mathrm{d}g_z/\mathrm{d}x\right)_{\max}}\;}$$

Units: $[G\sigma/(\mathrm{m\,s^{-2}\,m^{-1}})] =
\mathrm{m^3kg^{-1}s^{-2}\cdot kg\,m^{-2}\cdot m\,s^{2}} = \mathrm{m}$ ✓.

**Physical interpretation.** The maximum gradient occurs where the observation
line crosses the edge, so this rule not only gives the depth but *locates the
edge* — the peak of the horizontal derivative. That is why horizontal-derivative
and tilt-angle maps are standard products in potential-field interpretation: they
convert a depth problem into a location problem, which is better conditioned.

**Worked arithmetic.** A dyke edge at depth 150 m with $\sigma = 400\cdot100 =
4\times10^{4}$ kg/m² (a 400 kg/m³ contrast over a 100 m thick sheet) gives

$$\left(\frac{\mathrm{d}g_z}{\mathrm{d}x}\right)_{\max}
= \frac{2(6.6743\times10^{-11})(4\times10^{4})}{150}
= 3.560\times10^{-8}\ \mathrm{s^{-2}} = 3.560\times10^{-3}\ \mathrm{mGal\,m^{-1}},$$

i.e. about 3.6 µGal per metre. Resolving that gradient over a 20 m station
interval requires a difference of 0.071 mGal — well within a relative
gravimeter's capability, which is why edge-location from gradients is routine.

**The assumption, and its size.** The rule assumes a *semi-infinite* sheet, i.e. a
step in density. A finite-width dyke's gradient has two peaks (one per edge),
which is diagnostic: **one gradient peak means a step, two mean a dyke**, and the
separation of the two peaks gives the width directly. Misreading a dyke's two
peaks as one broad step roughly doubles the inferred depth — a consequence of the
same shape ambiguity quantified in the depth-rule error budget above.

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

### 6.5 Extended worked example: apparent depth depends on the assumed shape

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
