---
id: 07-03-03
title: "Forward Modelling in 2-D and 3-D"
level: graduate
prereqs: ["07-03-02"]
tags: [gravity, geodesy, forward-modelling, prisms, discretisation]
---

# Forward Modelling in 2-D and 3-D

All models and data in this module are SYNTHETIC. The prisms, densities, stations
and voxel sizes used below are chosen teaching values.

## Learning objectives

By the end of this lesson you will be able to:

1. **Implement** the closed-form vertical-gravity anomaly of a rectangular prism
   and **verify** it against a numerical triple integral.
2. **Use** superposition to build an arbitrary 3-D density model from prisms.
3. **Demonstrate** the far-field limit in which a prism becomes a point mass, and
   the long-strike limit in which it becomes the 2-D formula.
4. **Measure** the discretisation error introduced by voxelising a smooth body
   and **separate** the volume error from the shape error.
5. **Explain** why a model with more cells is not automatically a better model.
6. **Construct** the design matrix of a forward problem and state its
   dimensions and units.
7. **State** the regimes in which 2-D modelling is adequate and where it fails.

## Prerequisites

- [02 Analytical Formulas for Sphere, Cylinder, Sheet and Dyke](02-simple-body-formulas.md) —
  the 2-D closed forms and the limits used as tests here.

## 1. From formulas to models

A real target is not a sphere, and it is not a cylinder. It is a body with a
complicated shape, a density that varies inside it, and a top that does not
coincide with the topography. The universal escape from this difficulty is
**superposition**: divide the body into many simple volumes, use a closed form
for each, add. Gravity is linear in the density, so subdivision is not an
approximation at all — it is a change of parameterisation, and it is exact as
long as the simple volumes tile the body.

The only price is that the parameters are now the densities of many small cells,
and that is the beginning of the non-uniqueness treated in
[04](04-inversion-gravity.md). Forward modelling is the safe half of the problem:
fix the geometry, compute the anomaly, compare.

## 2. The rectangular prism

For a prism with corners $(x_1,x_2)\times(y_1,y_2)\times(z_1,z_2)$, $z$ measured
downward from the observation point, the vertical attraction of a homogeneous
body is (summing over the eight corners with alternating signs)

$$
g_z = G\Delta\rho\sum_{i=1}^{2}\sum_{j=1}^{2}\sum_{k=1}^{2}
(-1)^{\,i+j+k}\left[
x_i\ln\!\left(y_j+r_{ijk}\right) + y_j\ln\!\left(x_i+r_{ijk}\right)
- z_k\arctan\frac{x_i y_j}{z_k r_{ijk}}
\right],
$$

with $r_{ijk} = \sqrt{x_i^{2}+y_j^{2}+z_k^{2}}$ and the coordinates measured from
the observation point to each face. The demonstration evaluates it and compares
with a Gauss-Legendre quadrature of

$$g_z = G\Delta\rho\iiint \frac{z'}{\left|\mathbf{r}'\right|^{3}}\,\mathrm{d}V,
$$

obtaining differences of $10^{-20}$ to $10^{-18}\ \mathrm{m\,s^{-2}}$ for a
$400\ \mathrm{m}\times800\ \mathrm{m}\times650\ \mathrm{m}$ prism with
$\Delta\rho = 400\ \mathrm{kg\,m^{-3}}$ (peak value $2.22642\ \mathrm{mGal}$ at
$x = -400\ \mathrm{m}$). That agreement is the verification; without it, a sign
error in the eight-term sum is almost invisible, because the formula still
returns plausible numbers.

## 3. Superposition

Because $g_z$ is linear in $\Delta\rho$, the anomaly of a set of prisms is the
sum of their anomalies — including prisms with **negative** density contrast,
which is how a low-density body inside a denser one is modelled. The
demonstration sums two prisms, one positive and one negative, and prints the
individual contributions and the total at thirteen stations. At $x = 0$ the
positive prism gives $0.92806\ \mathrm{mGal}$, the negative prism
$-0.71450\ \mathrm{mGal}$ and the total $0.21355\ \mathrm{mGal}$: the observable
is a small difference of large numbers, which is exactly why the *correctness*
of each term matters more than the smoothness of the total.

A second demonstration of linearity: halving the density of the first prism
halves every ordinate of its anomaly exactly (the table prints both), so no
part of the profile shape can separate density from volume. The depth enters
only through the shape of the kernel, and only for extended bodies.

## 4. Limits as tests

1. **Prism → point mass.** At $200\ \mathrm{km}$ the demonstration's prism and
   its equivalent point mass agree to a ratio of $0.999859$; at $500\ \mathrm{km}$
   to $0.996869$. The residual is the finite size of the prism relative to the
   distance, and it falls as (size/distance)$^{2}$.
2. **Prism → 2-D rectangle.** For a strike half-length $L$, the prism's anomaly
   approaches the 2-D value as $L$ grows:

| strike length (m) | $g_{3D}/g_{2D}$ at $x=0$ |
|---|---|
| $2\times10^{3}$ | 0.8517 |
| $2\times10^{4}$ | 0.9980 |
| $2\times10^{5}$ | 0.99998 |
| $2\times10^{6}$ | 1.00000 |

   At $x=-600\ \mathrm{m}$ the same ratios are $0.89934$, $0.99873$, $0.99999$,
   $1.00000$. The lesson is quantitative: a strike length ten times the depth
   buys about $0.2\%$, a hundred times buys $0.002\%$.
3. **Sphere → stack of prisms.** Voxelising a sphere of $R=500\ \mathrm{m}$ at
   $1200\ \mathrm{m}$ depth with cubes of side $h$ and comparing with the
   analytic sphere gives the discretisation error directly (next section).

## 5. Discretisation error, measured

| voxel (m) | cells | volume error (%) | rms error, naive (mGal) | rms error, mass-matched (mGal) | mass-matched / peak (%) |
|---|---|---|---|---|---|
| 400 | 7 | $-14.44$ | 0.06223 | 0.00804 | 0.828 |
| 250 | 32 | $-4.51$ | 0.01983 | 0.00154 | 0.159 |
| 150 | 171 | $+10.22$ | 0.04815 | 0.00135 | 0.139 |
| 100 | 552 | $+5.42$ | 0.02506 | 0.00007 | 0.007 |
| 60 | 2469 | $+1.85$ | 0.00874 | 0.00028 | 0.029 |

The analytic peak is $0.97049\ \mathrm{mGal}$. Two lessons hide in this table.

- **The naive error is dominated by volume.** Cube voxels over- or under-count
  the body's volume, and the misfit tracks that volume error, not the cell size:
  the $10.22\%$ volume excess at $150\ \mathrm{m}$ voxels produces a *larger*
  error than the $4.51\%$ deficit at $250\ \mathrm{m}$ voxels. Discretisation
  error is not monotone in cell size unless the discrete model conserves mass.
- **Once mass-matched, the error collapses** — from $0.83\%$ of the peak at
  $400\ \mathrm{m}$ voxels to below $0.2\%$ at $100$–$250\ \mathrm{m}$ — but it
  still is not perfectly monotone, because the cube grid shifts relative to the
  sphere as the voxel size changes.

The practical rule: **check the volume of your discretised model** before
blaming the formula, and report the error relative to the peak, not in absolute
mGal, so the reader can judge it against the noise.

## 6. Worked example

*A prism $1\ \mathrm{km}\times2\ \mathrm{km}$ in plan, from $200\ \mathrm{m}$ to
$1.5\ \mathrm{km}$ depth, with $\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$, observed
above its centre.*

1. Half-widths $x_1 = -500\ \mathrm{m}$, $x_2 = +500\ \mathrm{m}$,
   $y_1 = -1000\ \mathrm{m}$, $y_2 = +1000\ \mathrm{m}$.
2. Because the observation is above the centre, the eight corner terms pair up.
   For the nearest corner $(x,y,z) = (500,1000,200)$ the distance is
   $r = \sqrt{500^{2}+1000^{2}+200^{2}} = 1135.8\ \mathrm{m}$; the corner terms
   are the logs and arctangents of this lesson's formula.
3. Evaluating the closed form gives $g_z = 5.0047\ \mathrm{mGal}$
   ($5.0047\times10^{-5}\ \mathrm{m\,s^{-2}}$). The infinite-slab value for the
   same thickness $1300\ \mathrm{m}$ is $16.3550\ \mathrm{mGal}$, so the finite
   body reaches only $30.6\%$ of the slab value: at this depth-to-width ratio the
   slab is a poor shorthand, unlike the $2\ \mathrm{km}$-wide, $200\ \mathrm{m}$
   thick body of §4 which reaches $99.96\%$.
4. Moving $500\ \mathrm{m}$ along the strike direction reduces the anomaly to
   $3.5505\ \mathrm{mGal}$, a $29\%$ drop — the smooth fall-off in the strike
   direction is what makes the strike length matter for a 2-D interpretation.
5. **Check with a limit:** raise the prism's top to the surface and widen it; the
   result must approach the slab. The demonstration performs exactly this test
   in the 2-D case; the 3-D case behaves the same way.

## 7. A verification checklist for any forward-model implementation

A prism implementation that produces plausible numbers is not verified. Run these
five checks in order; each catches a different class of error.

| check | what it catches | criterion |
|---|---|---|
| quadrature agreement | sign and algebra errors in the eight-term sum | relative difference $<10^{-8}$ |
| far-field point mass | missing or duplicated factors | ratio $\to1$ as $r/\text{size}\to\infty$; $0.99986$ at $200\ \mathrm{km}$ in the demonstration |
| long-strike 2-D limit | the factor of two between 2-D and 3-D kernels | ratio $\to1$ with strike length; $0.998$ at $10\times$ depth |
| superposition | linearity and sign handling of negative contrasts | sum of parts equals the whole to round-off |
| volume of the discretised model | voxel bookkeeping | discrete volume matches the analytic volume before any anomaly comparison |

The last row is the one most often skipped and the one that dominates the error,
as the voxelisation table shows: a $10.22\%$ volume excess produced a larger
anomaly error than a $4.51\%$ deficit, so the error tracked the volume mistake
rather than the cell size. **Compute the volume first; compare anomalies second.**

## 8. Assumptions and regime of validity

1. **Constant density inside each prism.** Gradients require subdivision.
2. **Planar top and bottom faces**, vertical sides. Dipping interfaces need
   polyhedral or voxel models.
3. **Exact arithmetic on the formula**, but **finite precision on the
   model**: the accuracy of the answer is the accuracy of the geometry, not of
   the algorithm.
4. **Observations outside the body.** The formula is singular inside the mass.
5. **No self-gravitation, no isostatic response.** The forward model computes the
   attraction of a *given* density; it does not predict the density.
6. **2-D validity:** strike length $\gtrsim10\times$ the depth for $0.2\%$
   accuracy, per the table above.

## 9. What the design matrix looks like

Gathering all stations and all cells,

$$\mathbf{d} = \mathbf{A}\,\mathbf{m}, \qquad A_{ij} = g_z^{(j)}\!\left(\text{unit density}\right)\!\left(\mathbf{x}_i\right),$$

with $\mathbf{d}$ a vector of $n$ anomalies in $\mathrm{m\,s^{-2}}$ and
$\mathbf{m}$ a vector of $p$ cell densities in $\mathrm{kg\,m^{-3}}$. The
demonstration's inversion in [04](04-inversion-gravity.md) uses
$n = 61$, $p = 246$: **more parameters than data**, so the forward model alone
does not determine the model. That ratio, not the formula, is what limits
interpretation.

## 10. Python demonstration

`code/forward_modelling_2d3d_demo.py` prints:

1. the prism closed form against a triple quadrature;
2. the far-field comparison with a point mass;
3. the long-strike table against the 2-D formula;
4. the voxelisation study with volume error, naive error and mass-matched error;
5. a two-prism superposition table with the density-halving check.

Every number in this lesson is from that output, with units printed, and the
script exits 0.

## 11. Exercises

See
[`exercises/03-forward-modelling-2d3d-exercises.md`](./exercises/03-forward-modelling-2d3d-exercises.md)
and
[`exercises/03-forward-modelling-2d3d-solutions.md`](./exercises/03-forward-modelling-2d3d-solutions.md).

- **★** State the number of closed-form terms in the prism sum and explain the
  alternating sign.
- **★** Verify by dimensional analysis that each bracket term in the prism
  formula is a length.
- **★★** For a strike half-length $L$, estimate the relative error of the 2-D
  approximation and compare with the demonstration's table at $L = 10^4\
  \mathrm{m}$.
- **★★** Show that halving $\Delta\rho$ halves $g_z$ and that changing $z$ does
  not, for an extended body.
- **★★★** Design a voxelisation of a dipping slab that conserves mass exactly
  and estimate the residual shape error at $100\ \mathrm{m}$ voxels.

## Mastery checkpoint

Without notes:

> A survey over a buried prism ($2\ \mathrm{km}$ strike, $600\ \mathrm{m}$ wide,
> $150\!-\!900\ \mathrm{m}$ deep, $\Delta\rho = 250\ \mathrm{kg\,m^{-3}}$) gives
> a peak anomaly of $1.62\ \mathrm{mGal}$.

**(a)** Write the forward operator and its units.
**(b)** Decide whether a 2-D interpretation is acceptable for this body, using
the strike-length table.
**(c)** Predict the anomaly at $500\ \mathrm{m}$ offset in the strike direction
and state why it is smaller than the cross-strike value.
**(d)** You discretise the body into $100\ \mathrm{m}$ cubes; state two checks
you would run before believing the result.

## Common pitfalls

1. **Sign errors in the eight-term sum.** Only a quadrature check exposes them.
2. **Voxel models that do not conserve volume.** The error then tracks the
   volume error, as measured above.
3. **Reporting absolute error instead of error relative to the peak.**
4. **Using a 2-D code on a short-strike body.** The demonstration's ratio is
   $0.85$ at a $2\ \mathrm{km}$ strike — a $15\%$ error.
5. **Believing more cells means better.** More cells mean more freedom; the data
   count has not changed.
6. **Forgetting that superposition includes negative density contrasts.**

## 12. Applications

- **Basin and salt modelling.** Prisms with negative contrast model salt and
  low-density fill.
- **Reservoir and orebody geometry.** Forward models test geological
  hypotheses against observed anomalies.
- **Inversion as repeated forward modelling.** Every gradient-based inversion in
  [04](04-inversion-gravity.md) needs $\mathbf{A}$ and $\mathbf{A}^{\mathsf{T}}$,
  both built from this lesson's formulas.
- **Joint interpretation.** The same prism machinery supplies the kernel for
  magnetic forward modelling, since both are potential fields
  ([02-08-06 Uniqueness Theorems and Boundary Conditions](../../02-physics/08-potential-theory/06-uniqueness-theorems.md)).

## Related modules

- [02 Analytical Formulas for Sphere, Cylinder, Sheet and Dyke](02-simple-body-formulas.md).
- [04 Gravity Inversion and Its Severe Non-Uniqueness](04-inversion-gravity.md).
- [18-01-04 Discretisation, Parameterisation and Model Choice](../../18-inverse-problems/01-inverse-problem-foundations/04-discretisation-reality.md) —
  the general consequences of turning a body into cells.
- [12-01-04 Verification vs Validation: Benchmarks and Convergence Tests](../../03-scientific-computing/12-numerical-simulation-python/04-verification-and-validation.md).

## 13. Self-assessment checklist

- [ ] I can implement the prism formula and verify it by quadrature.
- [ ] I can build a model from prisms with positive and negative contrasts.
- [ ] I can state and use the point-mass and 2-D limits.
- [ ] I can measure a voxelisation error and separate volume from shape error.
- [ ] I can write a design matrix and state its dimensions.
- [ ] I can decide when a 2-D interpretation is legitimate.
