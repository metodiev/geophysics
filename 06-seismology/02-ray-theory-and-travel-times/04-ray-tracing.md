---
id: 06-02-04
title: "Ray Tracing in Laterally Varying Media"
level: graduate
prereqs: ["06-02-01", "06-02-02", "06-02-03", "01-04-03"]
tags: [seismology, ray-tracing, shooting, travel-time, numerics, uncertainty]
---

# Ray Tracing in Laterally Varying Media

A travel-time curve is a table. A **ray tracer** is what turns a velocity model
into that table: given $v(\mathbf{x})$ and two points, it finds the path along
which the travel time is stationary and reports the time. Everything in the two
previous lessons was analytic because the medium was one-dimensional. This lesson
is about the step to models that vary in two or three dimensions, and about what
is gained and what is quietly lost when that step is taken.

Two formulations are standard. In **shooting**, the ray equations are integrated
forward from a source with an assumed take-off direction, and the take-off is
adjusted until the ray reaches the receiver — a root-finding problem wrapped
around an initial-value problem. In **bending**, the path is perturbed directly
until the travel-time functional is stationary — a variational problem solved by
relaxation. The demonstration uses shooting, twice: against an independent
travel-time engine on the standard `iasp91` reference model, and against a
closed-form solution on a synthetic gradient.

The honest difficulty is that the two-point problem stops having a unique answer
as soon as the medium is not one-dimensional. Where the travel-time curve folds,
several distinct rays reach the same receiver, and "the" travel time is not
defined until the branches are labelled. A tracer that returns the first arrival
is not wrong; it is answering a narrower question than the one the interpreter
asked. Section 5 states that limit precisely, and
[05 Shadow Zones, Triplications and the Low-Velocity Zone](05-shadow-zones.md)
measures it.

**All models and data in this module are SYNTHETIC.** The gradient
$v = 2000 + 0.50z\ \mathrm{m\,s^{-1}}$ is a chosen teaching model. The comparison
in Section 4 uses the standard `iasp91` reference model that ships with ObsPy, a
named reference model rather than measured data from this repository. Every
number below is printed by `code/ray_tracing_demo.py`; none is quoted from a
publication.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the ray equations in the form
   $\mathrm{d}/\mathrm{d}s\left(v^{-1}\mathrm{d}\mathbf{x}/\mathrm{d}s\right) =
   \nabla\!\left(v^{-1}\right)$ and **state** the two equivalent formulations
   (shooting and bending).
2. **Set up** the two-point problem as a root-finding problem in the take-off
   angle or ray parameter, and **explain** why a bracketing search is needed
   rather than Newton's method alone.
3. **Integrate** the spherical ray equations in radius and **compare** the result
   with an independent travel-time engine, reporting both the distance and time
   errors and where the agreement degrades.
4. **Show** that in a linear gradient the rays are exactly circular arcs, and
   **use** that closed form to validate a numerical tracer.
5. **Quantify** how a stated velocity-model error propagates into travel time and
   arrival distance, and **explain** why a 1 % velocity error produces about a
   2 % travel-time change at fixed ray parameter.
6. **Identify** the situations in which a shooting tracer returns a misleading
   single answer — folds, shadow zones, lateral heterogeneity — and **name** the
   remedy for each.

## Prerequisites

- [01 Eikonal Equation, Rays and Fermat's Principle](01-eikonal-and-rays.md) —
  the ray equations derived here are solved numerically.
- [02 Snell's Law, Layered Media and the Travel-Time Curve](02-snell-and-layering.md)
  — the reference case against which a tracer is validated.
- [03 The tau-p Transform and Intercept Time](03-tau-p.md) — the slowness
  integrals a tracer is computing.
- [01-04-03 Cartesian, Cylindrical and Spherical Coordinates](../../01-mathematics/04-geometry-and-coordinates/03-cartesian-spherical.md)
  — the spherical radius and path coordinates used throughout.

## 1. The ray equations, and two ways to solve them

For a medium with speed $v(\mathbf{x})$, the ray equation derived in
[01](01-eikonal-and-rays.md) is

$$\frac{\mathrm{d}}{\mathrm{d}s}\!\left(\frac{1}{v}\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}s}\right)
= \nabla\!\left(\frac{1}{v}\right),
\qquad
\frac{\mathrm{d}T}{\mathrm{d}s} = \frac{1}{v},$$

where $s$ is arc length. In a spherically symmetric Earth it is convenient to
work in $(r, \Delta)$ — radius and angular distance — where the conserved
quantity is $p = r\sin i/v$. With the turning radius $r_t$ defined by
$v(r_t) = r_t/p$ (the point at which the ray is horizontal, $\sin i = 1$), the
distance and the time are the two quadratures

$$\Delta(p) = 2\int_{r_t}^{R}\frac{p\;\mathrm{d}r}{r^{2}\sqrt{v(r)^{-2} - p^{2}/r^{2}}},
\qquad
T(p) = 2\int_{r_t}^{R}\frac{\mathrm{d}r}{v(r)^{2}\sqrt{v(r)^{-2} - p^{2}/r^{2}}},$$

with $R$ the source radius. These are exactly the one-dimensional integrals of
[03](03-tau-p.md), written in spherical coordinates; the demonstration evaluates
them by quadrature with an endpoint substitution that removes the integrable
square-root singularity at $r_t$.

**Shooting.** Choose $p$ (equivalently a take-off angle), integrate to get
$\Delta(p)$, compare with the target distance $\Delta^{\ast}$, and iterate on $p$.
Each evaluation is an initial-value problem; the iteration is a root-finding
problem. The difficulty is that $\Delta(p)$ is not monotone in general, so
bracketing is essential and the *number of roots in the bracket* is a physical
question, not a numerical one.

**Bending.** Discretise the path $\mathbf{x}_k$ and minimise
$T = \sum_k |\mathbf{x}_{k+1} - \mathbf{x}_k|/v$ subject to fixed endpoints, by
gradient descent or a conjugate-gradient scheme. Bending needs no root-finding
and handles multi-pathing more gracefully, but its cost grows with the number of
path nodes and it can converge to a local minimum — which is the same branch
ambiguity in another costume.

## 2. Why a linear gradient is the ideal test bed

For $v(z) = v_0 + Gz$ the rays are exactly circles whose centre lies at the level
where the extrapolated velocity would vanish, $z_c = -v_0/G$, and whose radius
follows from the take-off angle $i_0$ (measured from the vertical at the
surface):

$$R = \frac{v_0}{G\sin i_0}, \qquad \theta_0 = \arcsin(p v_0),
\qquad
X = 2R\cos\theta_0, \qquad z_t = R - \frac{v_0}{G},$$

with the total travel time

$$T = \frac{2}{G}\,\ln\frac{1}{\tan(\theta_0/2)} .$$

These are the closed forms used as the reference solution in Section 3. Because
every quantity is known analytically, the numerical tracer can be validated
against them *without* an independent software package — which is the strongest
form of validation available to a numerical method.

## 3. Validating a tracer

### 3.1 Against a closed form

The demonstration integrates the *flat* gradient problem with
$v_0 = 2000\ \mathrm{m\,s^{-1}}$, $G = 0.50\ \mathrm{s^{-1}}$ at four take-off
angles and compares the numerical path with the circular arc it should lie on:

| take-off $i_0$ | $p$ (s m⁻¹) | $X$ (km) | $T$ (s) | arc radius (km) | max deviation from arc (m) |
|---|---|---|---|---|---|
| 10.0° | $8.682409\times10^{-5}$ | 45.367 | 9.7447 | 23.035 | 1.851 |
| 20.0° | $1.710101\times10^{-4}$ | 21.978 | 6.9414 | 11.695 | 0.839 |
| 30.0° | $2.500000\times10^{-4}$ | 13.855 | 5.2676 | 8.000 | 0.500 |
| 45.0° | $3.535534\times10^{-4}$ | 7.999 | 3.5253 | 5.657 | 0.271 |

The numerical path lies on the analytic circle to sub-metre accuracy on offsets
of tens of kilometres, and the error shrinks as the quadrature spacing
effectively tightens. That is the check that the *equations being integrated are
the right equations*.

### 3.2 Against an independent engine

The same tracer, run on the `iasp91` reference model (sampled at 1444 depths
from 0 to 2886 km, $v_p$ from 5.800 to 13.690 $\mathrm{km\,s^{-1}}$), is compared
with the travel-time engine that accompanies ObsPy. The tracer is given the
engine's own ray parameter for a $P$ arrival at each distance and asked where and
when the ray surfaces:

| target Δ | $T$ from engine (s) | $p$ from engine (s rad⁻¹) | Δ from tracer | $T$ from tracer (s) |
|---|---|---|---|---|
| 30° | 370.2639 | 506.819320 | 29.967060° | 370.0524 |
| 45° | 496.9685 | 456.127860 | 44.993290° | 496.9802 |
| 60° | 608.2804 | 393.950163 | 59.996164° | 608.3122 |
| 75° | 703.2422 | 331.134570 | 75.004026° | 703.3190 |
| 90° | 781.3348 | 265.802096 | 90.163307° | 782.1434 |

From $45^\circ$ to $75^\circ$ the distance is reproduced to better than
$0.007^\circ$ and the time to better than 0.08 s, on times of 500–700 s — a
relative agreement of about $10^{-4}$. At $90^\circ$ the ray turns close to the
core–mantle boundary, where the model velocity drops from 13.6906 to
$8.0140\ \mathrm{km\,s^{-1}}$ within a few kilometres of depth and below the
tabulated window the quadrature has no turning point to resolve; the distance
error becomes $0.163^\circ$ and the time error 0.81 s. **The failure is located
and explained rather than averaged away**, and it is the same mechanism
(undersampling a sharp velocity drop) that produces the shadow zone of
[05](05-shadow-zones.md).

Two independent implementations of the same theory agreeing to $10^{-4}$ is
evidence about both; disagreement localised at the CMB is evidence about the
*discretisation*, which is the more useful kind.

## 4. Worked examples

### Example 1 — the arc geometry by hand, for the 30° ray

Take $v_0 = 2000\ \mathrm{m\,s^{-1}}$, $G = 0.50\ \mathrm{s^{-1}}$, $i_0 = 30^\circ$.

1. Ray parameter: $p = \sin i_0 / v_0 = 0.5/2000 = 2.500000\times10^{-4}\
   \mathrm{s\,m^{-1}}$ ✔ matches the table.
2. Arc radius: $R = v_0/(G\sin i_0) = 2000/(0.5 \times 0.5) = 8000$ m
   $= 8.000$ km ✔.
3. Turning depth: $z_t = R - v_0/G = 8000 - 4000 = 4000$ m $= 4.000$ km ✔ (also
   $(1/p - v_0)/G = (4000 - 2000)/0.5 = 4000$ m).
4. Offset: $X = 2R\cos\theta_0 = 2(8.000)(0.866025) = 13.856$ km ✔ (the
   quadrature gives 13.855 km, a difference of 1 m in 13.9 km).
5. Travel time: $T = (2/G)\ln\!\left[1/\tan(\theta_0/2)\right]
   = 4\ln(1/\tan 15^\circ) = 4(1.316958) = 5.2678$ s ✔ (quadrature: 5.2676 s).

The demonstration checks the same two quantities against the closed form
directly and reports agreement of 0.5000 ms in time and 2.0006 m in distance, so
the hand calculation above and the code agree to the precision printed.

### Example 2 — the two-point problem, solved

Suppose a receiver sits at $X = 10.000$ km on the same gradient, and we want the
first-arrival ray parameter and time. For this model the offset has the exact
form $X = (2v_0/G)\cot i_0 = 8000\cot i_0$ m, which is monotone decreasing, so
the two-point problem has exactly one solution here and it can be written down:

$$\cot i_0 = \frac{GX}{2v_0} = 1.25
\quad\Longrightarrow\quad
i_0 = 38.6598^\circ,
\qquad
p = \frac{\sin i_0}{v_0} = 3.123475\times10^{-4}\ \mathrm{s\,m^{-1}},$$
$$T = \frac{2}{G}\ln\frac{1}{\tan(i_0/2)}
= 4\ln\frac{1}{\tan 19.3299^\circ} = 4.1904\ \mathrm{s}.$$

The same answer by bracketing: at $i_0 = 30^\circ$, $X = 13.856$ km; at
$i_0 = 45^\circ$, $X = 7.999$ km. Linear interpolation in $i_0$ between these
bracketing rows gives $30^\circ + 15^\circ(3.856/5.857) = 39.88^\circ$, within
$1.2^\circ$ of the exact $38.66^\circ$ — which is why a *bracketing* search is
the first move and refinement is only the second: the bracket does most of the
work, and the refinement exists to make the answer honest rather than to make it
correct. Note also what made this example easy: $\cot i_0$ is monotone, so there
is one root. In a medium that varies laterally, that is precisely what is no
longer guaranteed (Section 5).

### Example 3 — what a velocity error does to the answer

The demonstration perturbs the gradient with a random field of 1 % rms relative
velocity error and 2 km correlation length and re-traces a fixed ray parameter
($p = 2.500000\times10^{-4}\ \mathrm{s\,m^{-1}}$, take-off $30^\circ$, nominal
turning depth 4.000 km) over 200 realisations. The quadrature's own error is
0.5000 ms in time, so anything larger is model error:

| quantity | mean ± 1σ | relative |
|---|---|---|
| travel time | $5.2759 \pm 113.162$ ms | 2.15 % of 5.2673 s |
| arrival offset | $13.8826 \pm 344.06$ m | 2.48 % of 13.8544 km |

Notice two things. First, the scatter is *larger* than the input error: at fixed
ray parameter a 1 % velocity change alters both the slowness along the path and
the depth at which the ray turns, and the two effects add rather than cancel.
Second, the mean time is $+8.614$ ms above the unperturbed value — a small
convexity bias, since $T$ is a convex function of the velocity perturbation.

The physical consequence is the central trade-off of travel-time work: a travel
time is a *sensitive* average of slowness along the path, and a *poor* locator of
where the anomaly is. A faster column anywhere the ray reaches gives a similar
time change, and separating the possibilities is exactly what tomography does
with many crossing paths — see
[06-06 Seismic Tomography](../06-seismic-tomography/README.md).

## 5. Laterally varying media: what changes, and what breaks

Nothing in the ray equations requires one-dimensionality. With
$v = v(x, z)$, the same equation

$$\frac{\mathrm{d}}{\mathrm{d}s}\!\left(\frac{1}{v}\frac{\mathrm{d}\mathbf{x}}{\mathrm{d}s}\right)
= \nabla\!\left(\frac{1}{v}\right)$$

applies, now with a genuinely two-component right-hand side. What changes is not
the physics but the *bookkeeping*:

1. **$p$ is no longer conserved.** A ray crossing a horizontal gradient changes
   its horizontal slowness, so the ray parameter is a label for the source
   direction, not an invariant. This is why the $\tau$-$p$ construction of
   [03](03-tau-p.md) is a one-dimensional tool.
2. **The number of solutions changes.** Lateral variation focuses and defocuses,
   and can create or destroy additional arrivals at a fixed receiver; the tracer
   must be asked for *all* arrivals, which means a bracketing search over
   take-off angle that records every root, not just the first.
3. **The first-arrival answer becomes incomplete.** A shooting tracer that stops
   at the first root returns a correct travel time for one arrival and says
   nothing about the others. Where the curve triplicates, the interpreter needs
   all three branches; where the ray family vanishes, the tracer returns nothing
   at all and the observed energy is diffracted.
4. **Grid methods replace rays for robustness.** Because rays can be trapped,
   shadowed or multi-pathed, production work in two and three dimensions often
   solves the eikonal equation on a grid instead, trading ray-branch resolution
   for unconditional existence of a first-arrival time.
   [06 Wavefront Tracking and the Fast Marching Method](06-wavefront-tracking.md)
   implements two such solvers and compares them.

**A note on the demonstration's scope.** `ray_tracing_demo.py` traces
one-dimensional (spherically symmetric) models and a laterally homogeneous
gradient; it does not include lateral heterogeneity. That limitation is stated
here rather than implied, because the *validated* part of a tracer is the
integration machinery, and the machinery is the same in 2-D — what differs is the
bookkeeping of items 1–4 above, which the demonstration's Sections 1–3 do not
exercise.

## 6. Assumptions and the regime of validity

1. **Ray theory.** Everything rests on the high-frequency reduction of
   [01](01-eikonal-and-rays.md): $\varepsilon = f^{-1}|\mathrm{d}v/\mathrm{d}z|
   \ll 1$. A tracer will happily return a number for a model in which rays are
   not a valid description.
2. **A smooth enough model.** The quadrature assumes $v(r)$ is well sampled. At
   the core–mantle boundary in the demonstration's own comparison, that
   assumption fails visibly (Section 3.2).
3. **A single arrival, unless the tracer is asked for more.** The two-point
   problem is not single-valued in general; the tracer's answer is a choice.
4. **First arrivals only, for grid solvers.** Where a ray is missing, a grid
   solver still returns a time — for a different, non-geometric propagation path.
5. **Isotropy and no attenuation.** Anisotropy changes the slowness surface;
   attenuation changes the amplitude and, at the level of ray theory, nothing
   about the time.
6. **The velocity model is the input, and it is uncertain.** Example 3 is the
   quantification: the model error dominated the numerical error in every
   realisation.

## 7. Python demonstration

`code/ray_tracing_demo.py` prints three labelled sections with units:

1. **One-dimensional shooting against an independent engine** — the table of
   Section 3.2, with the CMB degradation named and explained.
2. **A linear gradient against a closed form** — the arc table of Section 3.1,
   including each arc's radius and the maximum deviation of the numerical path
   from it.
3. **What a 1 % velocity error does to a turning ray** — the Monte Carlo of
   Example 3.

```bash
cd 06-seismology/02-ray-theory-and-travel-times/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ray_tracing_demo.py
```

## Mastery checkpoint

Complete this without notes:

> A gradient model has $v_0 = 2500\ \mathrm{m\,s^{-1}}$, $G = 0.60\
> \mathrm{s^{-1}}$. **(a)** Compute the ray parameter and arc radius for a
> take-off angle of $30^\circ$. **(b)** Compute the turning depth and offset.
> **(c)** Compute the travel time with the closed form. **(d)** A colleague
> changes the take-off angle to $45^\circ$ and reports a smaller offset; state
> whether that is expected and why. **(e)** Explain in two sentences why a tracer
> that returns only the first arrival can be *correct and still misleading*.

A worked version of (a)–(c) appears in the lesson
[solutions](exercises/04-ray-tracing-solutions.md).

## Common pitfalls

1. **Asserting Newton's method.** Solving $\Delta(p) = \Delta^{\ast}$ by Newton's
   method alone fails exactly where multi-pathing begins; bracket first, then
   refine, and count the roots in the bracket.
2. **Validating a tracer only against itself.** Agreement between two
   implementations that share a discretisation is evidence about the
   discretisation; a closed form or an independent engine is needed for more.
3. **Reporting a ray parameter as an invariant in a laterally varying medium.**
   It is conserved only for $v = v(z)$ (or $v = v(r)$).
4. **Believing the numerical error is the error.** In Example 3 the
   discretisation contributed 0.5 ms and the model contributed 113 ms.
5. **Ignoring where the agreement degrades.** A tracer that is good to $10^{-4}$
   at $75^\circ$ and to $10^{-3}$ at $90^\circ$ is a tracer with a known failure
   region, and the failure region is informative.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the wave physics the ray equations approximate.
- [01 Eikonal Equation, Rays and Fermat's Principle](01-eikonal-and-rays.md),
  [02 Snell's Law, Layered Media and the Travel-Time Curve](02-snell-and-layering.md),
  [03 The tau-p Transform and Intercept Time](03-tau-p.md) — the theory being
  integrated numerically here.
- [05 Shadow Zones, Triplications and the Low-Velocity Zone](05-shadow-zones.md) —
  what happens at the failure regions identified in Section 3.2.
- [06 Wavefront Tracking and the Fast Marching Method](06-wavefront-tracking.md) —
  the robust alternative in two and three dimensions.
- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) — where many ray
  paths are combined to localise what a single path cannot.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  discretisation, quadrature and error control in general.

## Exercises

Full sets with worked solutions are in
[`exercises/04-ray-tracing-exercises.md`](./exercises/04-ray-tracing-exercises.md)
and
[`exercises/04-ray-tracing-solutions.md`](./exercises/04-ray-tracing-solutions.md).
