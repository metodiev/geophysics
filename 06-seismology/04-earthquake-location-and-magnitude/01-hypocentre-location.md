---
id: 06-04-01
title: "Hypocentre Location: Arrival Times, Inversions and Error Ellipses"
level: advanced
prereqs: ["06-02-01", "06-02-02", "06-03-01", "18-01-02"]
tags: [seismology, hypocentre, location, least-squares, error-ellipse]
---

# Hypocentre Location: Arrival Times, Inversions and Error Ellipses

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the analytic Jacobian of the arrival time with respect to
   $(x, y, z, t_0)$ and **verify** it against a finite difference.
2. **Derive** the Gauss-Newton update from the linearised residual and explain
   why a nonlinear location problem is solved by a sequence of linear ones.
3. **Quantify** the depth/origin-time trade-off with the cosine between the two
   Jacobian columns, and explain why a single arrival cannot locate an event.
4. **Derive** the covariance matrix $\sigma_t^{2}(J^{T}J)^{-1}$ and the 95 per
   cent confidence ellipsoid, and **distinguish** a principal semi-axis from a
   marginal uncertainty.
5. **Compute** the derivative row for a given station by hand and check it
   against the demonstration.
6. **State** which assumptions produce the error ellipse, and which of them are
   false in every real catalogue.

## Prerequisites

- [06-02-01 Eikonal Equation, Rays and Fermat's Principle](../02-ray-theory-and-travel-times/01-eikonal-and-rays.md) —
  why a travel time is a function of source position at all.
- [06-02-02 Snell's Law, Layered Media and the Travel-Time Curve](../02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  the layered travel time used as the forward model in practice.
- [06-03-01 Faulting, Slip and the Elastic Rebound Cycle](../03-earthquake-sources/01-faulting-and-slip.md) —
  why the hypocentre is a quantity worth estimating.
- [18-01-02 Hadamard's Conditions: Existence, Uniqueness, Stability](../../18-inverse-problems/01-inverse-problem-foundations/02-hadamard-well-posedness.md) —
  the vocabulary of well-posedness used throughout.

## 1. Intuition: four numbers from a handful of times

An earthquake is reported as a **hypocentre** — a point $(x, y, z)$ — and an
**origin time** $t_0$. That is four numbers. What we measure is a set of arrival
times, one per station and per phase, and each arrival time is a *time*: a
scalar. The inversion is therefore the problem of extracting four numbers from
a vector of times through a nonlinear map.

Two facts make this harder and more interesting than it first appears.

- The map is **nonlinear**, because the travel time depends on the straight-line
  or ray distance between the trial hypocentre and the station, and a distance
  is a square root. Nonlinear least squares has no closed-form solution; it has
  an iteration.
- The geometry can be **degenerate**. If every station lies close together, or
  if there is only one, then a deeper event with an earlier origin time produces
  almost the same arrival times as a shallower one with a later origin time.
  The data cannot separate the two. This is not noise; it is a null direction of
  the problem, and it is the central honest difficulty of this lesson.

The demonstration prints both facts as numbers, and Section 3 derives them.

## 2. The forward problem and the residual

### 2.1 A tractable forward model

Real location uses a layered or three-dimensional velocity model. To keep the
algebra exact we work with a **homogeneous half-space** of velocity $v$, as the
demonstration does. The travel time from a trial hypocentre $\mathbf{m} =
(x, y, z)$ to a station at $(\xi_i, \eta_i, 0)$ is then

$$
T_i(\mathbf{m}) = \frac{1}{v}\sqrt{(\xi_i - x)^{2} + (\eta_i - y)^{2} + z^{2}}
\quad \mathrm{(s)} ,
\qquad z > 0 \ \text{down}.
$$

Including the origin time, the predicted arrival at station $i$ is $T_i + t_0$.
The **residual** is the difference between the observed and predicted arrival,

$$
r_i(\mathbf{m}, t_0) = T_i^{\text{obs}} - T_i(\mathbf{m}) - t_0 ,
$$

and the location is the parameter vector that minimises the sum of squares

$$
\Phi(\mathbf{m}, t_0) = \sum_i r_i^{2}
\qquad \text{(units: } \mathrm{s^{2}} \text{)} .
$$

That choice of objective is not innocent: it makes the solution a *least-squares*
estimate, which is the maximum-likelihood estimate only for Gaussian pick errors
with equal variance and no outliers. Section 5 states the rest.

### 2.2 Why the derivative can be written down exactly

Write $d_i = \sqrt{(\xi_i - x)^{2} + (\eta_i - y)^{2} + z^{2}}$ for the
source–station distance. Then $T_i = d_i / v$, and differentiating with respect
to the source coordinates gives, for example,

$$
\frac{\partial T_i}{\partial x}
= \frac{1}{v}\cdot\frac{-( \xi_i - x)}{d_i}
= -\frac{\xi_i - x}{v\, d_i} ,
\qquad
\frac{\partial T_i}{\partial z} = \frac{z}{v\, d_i} .
$$

Define the unit vector from the source to the station,
$\mathbf{u} = \big((\xi_i - x), (\eta_i - y), z\big) / d_i$. The row of
derivatives is

$$
\nabla T_i = \frac{1}{v}\big(-u_x, -u_y, +u_z\big) ,
\qquad
\frac{\partial T_i}{\partial t_0} = 1 .
$$

The physical reading is immediate: **the sensitivity of an arrival time to a
source displacement is the component of that displacement along the ray,
divided by the wave speed.** A station straight above the source sees only
depth; a station far to the north sees only north–south.

## 3. Derivations

### 3.1 From the linearisation to Gauss-Newton

Linearise the residual at the current model $\mathbf{p} = (\mathbf{m}, t_0)$
about a perturbation $\delta\mathbf{p}$:

$$
r_i(\mathbf{p} + \delta\mathbf{p}) \approx r_i(\mathbf{p})
+ \left.\frac{\partial r_i}{\partial \mathbf{p}}\right|_{\mathbf{p}} \delta\mathbf{p}
= r_i - J_{i}\delta\mathbf{p} ,
$$

because $r_i$ decreases when the predicted arrival increases, so
$\partial r_i / \partial p_j = -J_{ij}$ with $J_{ij} = \partial T_i/\partial p_j$
and $J_{i4} = 1$. Minimising $\|\mathbf{r} - J\delta\mathbf{p}\|^{2}$ gives the
normal equations

$$
J^{T}J\,\delta\mathbf{p} = J^{T}\mathbf{r} ,
\qquad
\delta\mathbf{p} = (J^{T}J)^{-1} J^{T}\mathbf{r} ,
$$

and the **Gauss-Newton** iteration is $\mathbf{p} \leftarrow \mathbf{p} +
\delta\mathbf{p}$. The iteration is the price of the nonlinearity: each step is
an exact linear least-squares problem, but the sequence is not guaranteed to
converge from an arbitrary start, and it can stop at a local minimum of $\Phi$.

*Regime of validity of the iteration.* Gauss-Newton converges quadratically
when the residual is small and the model is near the solution; it can diverge
when the starting hypocentre is far outside the network, which is why real
locators constrain the depth to a grid or a search interval.

### 3.2 The depth / origin-time trade-off, quantified

Take two columns of $J$: the depth column $\partial T_i/\partial z$ and the
origin-time column $\partial T_i/\partial t_0 = 1$ for every $i$. Their cosine is

$$
\cos\theta
= \frac{\sum_i \partial T_i/\partial z}
{\sqrt{\left(\sum_i \left(\partial T_i/\partial z\right)^{2}\right)\, N}} ,
$$

with $N$ the number of stations. Two limits are worth stating exactly.

- **One station.** $J$ is a single row, so its rank is 1 and three of the four
  parameter directions are null: any hypocentre along the ray to that station can
  reproduce the arrival by adjusting $t_0$. No error ellipse exists, only an
  unbounded family of solutions.
- **A tight array.** Every ray leaves the source almost vertically, so
  $u_z \approx 1$ for all $i$ and $\partial T_i/\partial z \approx 1/v$ for every
  station — a constant vector, proportional to the origin-time column. The
  cosine approaches 1 and the two parameters become nearly indistinguishable.

The **variance–covariance matrix** of the estimate makes this quantitative.
With independent pick errors of standard deviation $\sigma_t$,

$$
C = \sigma_t^{2}\,(J^{T}J)^{-1} ,
\qquad
\mathrm{corr}(z, t_0) = \frac{C_{34}}{\sqrt{C_{33}C_{44}}} .
$$

A correlation near $\pm 1$ means the data determine one combination of depth and
origin time and not the two separately.

### 3.3 The confidence ellipsoid

The quantity $(\mathbf{p} - \hat{\mathbf{p}})^{T} C^{-1}
(\mathbf{p} - \hat{\mathbf{p}})$ is, under the stated assumptions,
$\chi^{2}$-distributed with 4 degrees of freedom. The 95 per cent confidence
region is therefore the ellipsoid

$$
(\mathbf{p} - \hat{\mathbf{p}})^{T} C^{-1} (\mathbf{p} - \hat{\mathbf{p}})
\le \chi^{2}_{4}(0.95) = 9.4877 ,
$$

with semi-axes $\sqrt{9.4877\,\lambda_k}\,\mathbf{v}_k$, where $\lambda_k$ and
$\mathbf{v}_k$ are the eigenvalues and eigenvectors of $C$. The **longest
semi-axis is the direction in which the data are least informative** — that is
the whole interpretive content of the ellipsoid.

Two numbers are often confused, and the distinction matters:

- a **marginal** uncertainty is $\sqrt{C_{jj}}$ (or $1.96\sqrt{C_{jj}}$ for a 95
  per cent interval in one parameter), which ignores the correlation;
- a **principal semi-axis** is $\sqrt{9.4877\lambda_k}$, the extent of the joint
  region along its own axes, and it is always at least as long as the marginal.
  When depth and origin time are correlated, the longest principal axis can be
  much longer than either marginal.

## 4. Worked examples

All input values are those of `code/hypocentre_location_demo.py`: a homogeneous
half-space with $v = 6000\ \mathrm{m\,s^{-1}}$, pick uncertainty
$\sigma_t = 0.050\ \mathrm{s}$, a true hypocentre at
$(12.0, -8.0, 7.5)\ \mathrm{km}$ with $t_0 = 1.500\ \mathrm{s}$, and the
7-station array with the largest aperture (60 km). Every number quoted below is
printed by that script.

### Example 1 — one Jacobian row, by hand

Station 0 of the wide array is at $\xi_0 = -30\ \mathrm{km}$,
$\eta_0 = 52\ \mathrm{km}$. From the true hypocentre

$$
d_0 = \sqrt{(42)^{2} + (60)^{2} + (7.5)^{2}}\ \mathrm{km}
= \sqrt{5420.25}\ \mathrm{km} = 73.622\ \mathrm{km},
$$

$$
\frac{\partial T_0}{\partial x}
= -\frac{\xi_0 - x}{v\,d_0} = \frac{42\,000}{6000 \times 73\,622}
= 9.508\times10^{-5}\ \mathrm{s\,m^{-1}} ,
$$

$$
\frac{\partial T_0}{\partial z}
= \frac{z}{v\,d_0} = \frac{7500}{6000\times73\,622}
= 1.698\times10^{-5}\ \mathrm{s\,m^{-1}} .
$$

Both agree with the values the demonstration prints for station 0, and they show
the physical point directly: this station lies 60 km north and 42 km west of the
event, so it is far more sensitive to horizontal displacement than to depth. The
ratio is $\partial T/\partial x \div \partial T/\partial z = 5.6$.

### Example 2 — the trade-off in three configurations

The demonstration builds the same event with three networks and reports:

| array | $\cos(\partial T/\partial z,\ \partial T/\partial t_0)$ | rank | null dim | $\mathrm{cond}(J^{T}J)$ | $\mathrm{corr}(z,t_0)$ |
|---|---|---|---|---|---|
| 7 stations, aperture 60 km | 0.785764 | 4 | 0 | $6.536\times10^{8}$ | $-0.811661$ |
| 5 stations, aperture 4 km | 0.999824 | 3 | 1 | $\infty$ | — |
| 1 station | 1.000000 | 1 | 3 | $\infty$ | — |

Read the rows in order. A single arrival gives a rank-1 Jacobian, so three
parameter directions are entirely unconstrained and no corresponding uncertainty
can even be formed. Shrinking the array to 4 km removes the *exact* singularity
but not the *physical* one: the cosine rises to 0.999824, so depth and origin
time still trade almost perfectly. The wide array has the smallest cosine and
the smallest condition number, and even it leaves a strong correlation of
$-0.81$ between the two.

### Example 3 — the error ellipse, and two ways to misread it

For the wide array with $\sigma_t = 0.050\ \mathrm{s}$, the demonstration
computes $C = \sigma_t^{2}(J^{T}J)^{-1}$ and its eigen-decomposition. The 95 per
cent semi-axes are

| semi-axis | length | direction $(x, y, z, t_0)$ |
|---|---|---|
| 1 | $1488.2\ \mathrm{m}$ | $(+0.1360, +0.2826, -0.9495, +0.0001)$ |
| 2 | $911.9\ \mathrm{m}$ | $(-0.8244, -0.4993, -0.2667, +0.0000)$ |
| 3 | $518.5\ \mathrm{m}$ | $(-0.5495, +0.8190, +0.1650, +0.0001)$ |
| 4 | $0.0582\ \mathrm{s}$ | $(0.0000, -0.0001, +0.0001, +1.0000)$ |

The longest axis is almost entirely horizontal-and-depth with no origin-time
component: this array's worst-determined direction is source *geometry*, not
source *time*. The direction of that axis is defined only up to sign, so an
eigenvector and its negative are the same statement.

The two readings that are easy to get wrong:

- The diagonal of $C$ gives the **marginal** 1σ values
  $\sqrt{C_{xx}}, \sqrt{C_{yy}}, \sqrt{C_{zz}}, \sqrt{C_{t_0t_0}}$. For this array
  those are about $269\ \mathrm{m}$, $244\ \mathrm{m}$, $466\ \mathrm{m}$ and
  $0.0399\ \mathrm{s}$, so a naive "95 per cent depth error" of
  $1.96\times466 = 914\ \mathrm{m}$ is *shorter* than the longest principal
  semi-axis of $1488\ \mathrm{m}$, because the correlation between the two
  horizontal coordinates costs extra length in the joint region.
- The correlation $\mathrm{corr}(z, t_0) = -0.8117$ is the trade-off in one
  number. A negative sign means the two move in opposite senses: to keep the
  same arrivals, a deeper event must be given an *earlier* origin time. The
  single-station case has no such number, because there the trade-off is exact.

### Example 4 — Gauss-Newton from a bad start

Starting at $(20.0, 0.0, 15.0)\ \mathrm{km}$ with $t_0 = 0.000\ \mathrm{s}$, the
demonstration iterates:

| iter | $x$ (km) | $y$ (km) | $z$ (km) | $t_0$ (s) | rms residual (s) |
|---|---|---|---|---|---|
| 0 | 20.0000 | 0.0000 | 15.0000 | 0.0000 | $1.292\times10^{0}$ |
| 1 | 11.4002 | $-8.9204$ | 9.3651 | 1.7044 | $3.717\times10^{-1}$ |
| 2 | 12.0158 | $-7.9641$ | 7.5364 | 1.5100 | $1.104\times10^{-2}$ |
| 3 | 12.0000 | $-8.0000$ | 7.5001 | 1.5000 | $8.058\times10^{-6}$ |
| 4 | 12.0000 | $-8.0000$ | 7.5000 | 1.5000 | $1.485\times10^{-11}$ |

After four iterations the difference from the truth is of order $10^{-7}\ \mathrm{m}$
and $2\times10^{-11}\ \mathrm{s}$. On *exact* data Gauss-Newton converges to the
exact answer, and that is all this example claims: it tests the code and the
linearisation, not the Earth. The residual does not reach zero on real data, and
the size it settles at is the quantity that carries the information about model
error (lesson [02](02-velocity-model-dependence.md)).

## 5. Assumptions and regime of validity

The error ellipse is a statement about the *picks* under conditions that a real
catalogue does not satisfy. Each of the following assumptions is used by the
derivations above, and each is false in practice:

1. **Pick errors are Gaussian**, with a known standard deviation, and no
   outliers. Real picks include phase misidentifications, which are heavy-tailed
   and dominate the residual; one mis-picked phase can move a hypocentre by
   kilometres.
2. **Pick errors are independent between stations.** Shared phase, shared
   instrument class and shared picking software introduce correlation, which
   shrinks the apparent scatter in a way the formula cannot see.
3. **The velocity model is the true one.** Section 3.3 conditions on it
   completely; the ellipse is a statement about $(\mathbf{m}, t_0)$ *given* the
   model. Lesson [02](02-velocity-model-dependence.md) measures the size of the
   error this omission creates, and it is larger than the ellipse.
4. **The forward model is the right functional form.** A homogeneous half-space
   has no velocity gradient, so real depth estimates from it are biased.
5. **At least four independent constraints exist.** With fewer, $J^{T}J$ is
   singular and the operation $(J^{T}J)^{-1}$ in Section 3.1 does not exist; the
   demonstration avoids it by testing the rank first.
6. **The event lies in the region where the linearisation is valid.** Gauss-Newton
   refines a nearby solution; it does not find a global one.

## 6. The demonstration

`code/hypocentre_location_demo.py` reproduces every number in this lesson:

1. the Jacobian, analytic against a central finite difference — the worst
   difference over all entries is $3.327\times10^{-13}\ \mathrm{s\,m^{-1}}$, which
   is the discretisation error of the difference, not an error in either
   derivative;
2. the trade-off table of Example 2, including the rank and null dimension of
   each network;
3. the Gauss-Newton sequence of Example 4;
4. the 95 per cent ellipsoid of Example 3 and the two correlations.

Run it with

```bash
cd 06-seismology/04-earthquake-location-and-magnitude/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hypocentre_location_demo.py
```

The exercise set is
[`exercises/01-hypocentre-location-exercises.md`](exercises/01-hypocentre-location-exercises.md)
with worked solutions in
[`exercises/01-hypocentre-location-solutions.md`](exercises/01-hypocentre-location-solutions.md).

> All models and data in this module are **SYNTHETIC**. The velocity, the
> network, the event and the noise are teaching values, and no number here is a
> measurement or a published catalogue entry.

## Mastery checkpoint

Without notes:

1. Write the analytic derivative $\partial T_i/\partial x$ for the homogeneous
   half-space and state its units.
2. Explain why a single arrival gives a Jacobian of rank 1 out of 4.
3. State, with the correlation, what $\mathrm{corr}(z,t_0) = -0.81$ means
   physically.
4. Compute $1.96\sqrt{C_{zz}}$ for $\sqrt{C_{zz}} = 466\ \mathrm{m}$ and then
   explain why the longest 95 per cent semi-axis can still be $1488\ \mathrm{m}$.
5. Name one assumption in Section 5 that is false in every catalogue, and say
   which lesson measures its cost.

A worked check of (4) appears in the
[solutions](exercises/01-hypocentre-location-solutions.md).

## Common pitfalls

1. **Reporting an ellipse as an accuracy.** The ellipse measures the picks, not
   the Earth. A catalogue depth is conditional on a velocity model.
2. **Confusing a marginal uncertainty with a principal semi-axis.** They differ
   whenever the parameters are correlated, and the difference is usually the
   larger number.
3. **Assuming a tight array is better because the matrix is invertible.** The
   demonstration's 4 km array has rank 3 and a null direction; the wide array is
   the one that constrains depth.
4. **Treating convergence as validation.** Gauss-Newton converges on wrong
   models too; convergence says the arithmetic works, not that the answer is
   right.
5. **Using the residual as an error bar without units.** The rms residual is in
   seconds and the ellipse in metres; the conversion between them is $C$, and it
   is not a number.
6. **Ignoring outliers.** With uniform weights, one 1 s mis-pick has the same
   leverage as twenty good picks.

## Related modules

- [02 Dependence on the Velocity Model and Joint Inversion](02-velocity-model-dependence.md) —
  what the ellipse leaves out.
- [03 Relative Location: Master-Event, Double-Difference, HypoDD](03-relative-location.md) —
  how differencing removes the nuisance term.
- [06-02-04 Ray Tracing in Laterally Varying Media](../02-ray-theory-and-travel-times/04-ray-tracing.md) —
  the forward model when the half-space is not enough.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general theory
  of null spaces, damping and regularisation behind Section 3.
