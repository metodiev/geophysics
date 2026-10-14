---
id: 01-12-02
title: "Interpolation, Splines and Approximation Theory"
level: intermediate
prereqs: ["01-02-04", "01-05-04", "01-07-03"]
estimated_minutes: 90
tags: [numerical-methods, interpolation, splines, runge-phenomenon]
---

# Interpolation, Splines and Approximation Theory

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the interpolation problem precisely, and distinguish interpolation
   from approximation and from extrapolation.
2. **Construct** an interpolating polynomial in the Lagrange and Newton forms,
   and explain why they are the same polynomial computed in different bases.
3. **Explain** the Runge phenomenon in terms of the node distribution, and use
   Chebyshev nodes to remove it.
4. **Derive** the error formula for polynomial interpolation and the moment
   equations of a cubic spline.
5. **Measure** the convergence order of linear, natural-spline and clamped-spline
   interpolation, and state which window each order describes.
6. **Choose** an interpolant for irregularly sampled field data or a well log,
   including the cases where the smooth interpolant must be rejected.

## Prerequisites

[01-02-04 Polynomials and Roots](../02-algebra/04-polynomials-roots.md) — the
object being constructed. [01-05-04 Taylor Series](../05-single-variable-calculus/04-taylor-series.md)
— the machinery of the error term. [01-07-03 Linear Systems, Gaussian
Elimination and LU Factorisation](../07-linear-algebra/03-systems-and-elimination.md)
— because the spline equations are a tridiagonal system.

## 1. Intuition: filling the gaps is inventing structure

You measure a gravity profile every 500 m along a line, or a well log every
0.15 m of depth. You want values in between. The honest statement of the problem
is uncomfortable: **interpolation does not recover what you did not measure; it
invents a rule for what lies between and then fills it in.** The only thing that
makes it legitimate is that the rule can be justified — by smoothness of the
underlying field, by the physics that produced the samples, or at least by the
absence of oscillation between them.

Three regimes must be distinguished, because they have completely different
epistemics:

- **Interpolation** passes exactly through the data. Every datum is treated as
  true, which is only defensible when the samples really are accurate.
- **Approximation** (or smoothing, or regression) deliberately misses the data,
  trading a small systematic error for immunity to noise. This is the correct
  choice for most measured field data, and it is the subject of
  [01-12-05](./05-linear-solvers.md) and [21 Statistics](../../21-statistics-bayesian-ml/README.md)
  rather than of this lesson.
- **Extrapolation** goes outside the sampled range. Nothing in interpolating
  theory justifies it, and the error grows without bound even for an exact
  polynomial fit. A gravity profile sampled to 5 km tells you nothing about 10 km
  by interpolation alone; a different model, or a different dataset, is required.

The geophysical interest is that the choice of interpolant changes the answer, and
the change is not always small. The demonstration below shows a unit step
interpolated by a cubic spline overshooting to 1.107 — an 11% error — and dipping
to $-0.1306$. A monotone porosity log extrapolated that way can return negative
porosity.

## 2. Precise definitions

### 2.1 Interpolating polynomial, existence and uniqueness

Given $n+1$ distinct nodes $x_0<x_1<\dots<x_n$ with values $y_i$, the
**interpolating polynomial** $p$ of degree at most $n$ satisfies $p(x_i)=y_i$.
It exists and is unique: the Vandermonde system is nonsingular, and if two such
polynomials existed their difference would be a degree-$\le n$ polynomial with
$n+1$ roots.

### 2.2 Two bases for the same polynomial

The **Lagrange form** writes $p$ as a combination of cardinal polynomials,

$$p(x) = \sum_{i=0}^{n} y_i\,\ell_i(x), \qquad
\ell_i(x) = \prod_{\substack{j=0\\j\ne i}}^{n}\frac{x-x_j}{x_i-x_j},$$

where $\ell_i(x_j)=\delta_{ij}$. The **Newton form** uses divided differences,

$$p(x) = \sum_{i=0}^{n} a_i \prod_{j=0}^{i-1}(x-x_j),$$

with $a_i$ the divided differences constructed recursively as
$a_i^{(j)} = (a_i^{(j-1)} - a_{i-1}^{(j-1)})/(x_i - x_{i-j})$. Both represent the
same polynomial; the demonstrated difference between them is $7.1\times10^{-15}$
on 41 points, i.e. round-off. What differs is the *stability*: adding a node to
the Newton form costs one new coefficient and leaves the others unchanged, while
the Lagrange form must be rebuilt entirely.

### 2.3 Splines

A **cubic spline** on the node set is a piecewise cubic that is twice
continuously differentiable across every interior node. A spline of the class
$C^2$ has exactly enough free parameters to impose the interpolation conditions
plus $C^2$ continuity, leaving two degrees of freedom that the **end conditions**
consume:

- the **natural** conditions $s''(x_0)=s''(x_n)=0$;
- the **clamped** (complete) conditions $s'(x_0)$ and $s'(x_n)$ given.

These are not interchangeable, and the demonstration measures that they produce
max-norm orders of 2 and 4 respectively on the same data.

## 3. Derivations

### 3.1 The interpolation error

Let $p_n$ interpolate $f\in C^{n+1}$ at $x_0,\dots,x_n$. For $x$ not a node,
consider $F(t) = f(t)-p_n(t) - \lambda\omega(t)$ with
$\omega(t)=\prod_{j}(t-x_j)$ and $\lambda$ chosen so that $F(x)=0$. Then $F$ has
$n+2$ zeros and, applying Rolle's theorem $n+1$ times, $F^{(n+1)}$ has one zero
$\xi$ at which $f^{(n+1)}(\xi) - \lambda(n+1)! = 0$. Hence

$$f(x)-p_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{j=0}^{n}(x-x_j) .$$

Two things follow, and they are the whole content of the Runge phenomenon.

1. The error is the product of a *function factor* and a *node factor*
   $\omega(x)$.
2. Increasing $n$ helps the function factor (because $(n+1)!$ grows) but can
   destroy the node factor, since $\max|\omega|$ depends entirely on where the
   nodes are placed.

### 3.2 Runge's phenomenon as a node-distribution problem

For $f(x)=1/(1+25x^2)$ on $[-1,1]$, the derivatives grow like $25^n$ near the
origin (the function has poles at $x=\pm \mathrm{i}/5$), while $\omega$ for
equally spaced nodes is largest near the ends — the two effects combine in the
worst possible way, and the interpolant oscillates violently near $\pm1$. The
demonstration measures the max error on a 401-point grid:

| $n$ | equispaced nodes | Chebyshev nodes |
|---|---|---|
| 4 | $4.38\times10^{-1}$ | $4.60\times10^{-1}$ |
| 8 | $1.05$ | $2.05\times10^{-1}$ |
| 12 | $3.66$ | $8.43\times10^{-2}$ |
| 16 | $14.4$ | $3.67\times10^{-2}$ |
| 20 | $59.8$ | $1.77\times10^{-2}$ |
| 24 | $257$ | $8.17\times10^{-3}$ |

The equispaced error *grows by a factor of about 4.3 for every four extra nodes*
— adding data makes the answer worse. The reason is that equispaced nodes make
$\max|\omega|$ grow like $2^{n-1}/(n+1)$ for large $n$, and the derivative growth
outruns the factorial. The Chebyshev nodes

$$x_j = -\cos\!\left(\frac{j\pi}{n}\right), \qquad j=0,\dots,n,$$

place nodes densely at the ends, where $\omega$ would otherwise be large, and
minimise $\max|\omega|$ over all node sets of size $n+1$ (their $\omega$ is a
scaled Chebyshev polynomial of degree $n+1$, with all extrema equal in modulus to
$2^{-n}$). The product then behaves, the error falls monotonically, and
interpolating polynomials of high degree become usable.

The practical lesson is not "use Chebyshev nodes for field data" — you cannot
choose where a gravity reading was taken — but that **equispaced high-degree
polynomial interpolation is a trap**, and that when the node distribution cannot
be controlled, splines or local methods must be used.

### 3.3 The spline moment equations

Write the spline in terms of its second derivatives $M_i = s''(x_i)$, which vary
linearly across each interval $[x_i,x_{i+1}]$ with $h_i = x_{i+1}-x_i$. Requiring
$C^1$ continuity of $s'$ at each interior node gives, for $i=1,\dots,n-1$,

$$h_{i-1}M_{i-1} + 2(h_{i-1}+h_i)M_i + h_iM_{i+1}
= 6\left(\frac{y_{i+1}-y_i}{h_i} - \frac{y_i-y_{i-1}}{h_{i-1}}\right).$$

This is a symmetric, strictly diagonally dominant tridiagonal system, so it has a
unique solution and is solved in $O(n)$ operations by the Thomas algorithm
([01-12-05](./05-linear-solvers.md)). The natural condition sets $M_0=M_n=0$ and
leaves an $(n-1)\times(n-1)$ system; the clamped condition appends two equations
involving the given end slopes and leaves an $(n+1)\times(n+1)$ system.

### 3.4 Why natural and clamped splines have different global orders

The interior discretisation is exact to $O(h^4)$ in both cases. The difference is
entirely in the *boundary* treatment:

- The **clamped** conditions impose the true derivatives, so the error is
  $O(h^4)$ uniformly.
- The **natural** conditions impose $s''=0$ at the ends, which is a statement
  about the function — and a false one unless $f''(x_0)=f''(x_n)=0$. The
  resulting error is $O(h^2)$ near each end, in a layer that does not shrink in
  units of $h$, and that boundary layer controls the max norm.

The demonstration measures exactly this: on $f=\mathrm{e}^x$ the max-norm orders
are linear 2.00, natural 2.00 and clamped 4.00; and for the natural spline
measured on the interior window $[0.25,0.75]$ the order is 4.00 while the same
fit measured over the whole interval stays at 2.00.

| nodes | natural spline, max error on $[0.25,0.75]$ | order | max error on $[0,1]$ | order |
|---|---|---|---|---|
| 16 | $2.614\times10^{-6}$ | – | $5.200\times10^{-4}$ | – |
| 32 | $5.880\times10^{-9}$ | 8.80 | $1.300\times10^{-4}$ | 2.00 |
| 64 | $3.249\times10^{-10}$ | 4.18 | $3.251\times10^{-5}$ | 2.00 |
| 128 | $2.039\times10^{-11}$ | 3.99 | $8.129\times10^{-6}$ | 2.00 |
| 512 | $7.905\times10^{-14}$ | 4.00 | $5.080\times10^{-7}$ | 2.00 |

Note the pre-asymptotic orders 8.80 and 4.18 at the coarse end: the boundary
layer has not yet separated from the window, and an order quoted from those two
rows alone would be wrong. **An order is a statement about a window and a range
of $h$, not about an interpolant in the abstract.**

## 4. Physical interpretation

- **Gravity and magnetic profiles.** The field above a body is analytic in the
  half-space above it, so it is as smooth as any interpolant could wish. But the
  *samples* are not: they carry reading error and terrain effects. Interpolating
  them exactly transfers the noise into oscillations; approximating them is the
  physically defensible choice.
- **Well logs.** Logs are sampled densely in depth (0.15 m is typical), so
  interpolation between samples is a small extrapolation and a spline is
  appropriate. But porosity, saturation and clay volume are bounded quantities,
  and an interpolant that overshoots out of range describes an impossible rock.
  The measured overshoot of 0.107 on a unit step is the size of the problem.
- **Travel-time tables in seismology.** A velocity model published on a coarse
  depth grid is interpolated at every ray step. A spline is standard, and the
  $O(h^4)$ interior order is why: the interpolation error must not exceed the
  accuracy of the travel-time pick, and picks are good to a few milliseconds
  over hundreds of kilometres.
- **Gridding and mapping.** Regularising scattered data onto a grid is
  interpolation in two dimensions, where the node-distribution problem becomes a
  triangulation problem. Unstructured meshes and kriging are the two answers;
  both are outside this lesson, but the reasoning is the same.

## 5. Assumptions and regime of validity

| Interpolant | Best order | Requires | Reject when |
|---|---|---|---|
| Linear | $O(h^2)$, exact on lines | nothing beyond the data | the field has curvature you need to resolve |
| Polynomial (equispaced) | none, in general | very smooth $f$, small $n$ | $n\gtrsim 10$ — Runge phenomena take over |
| Polynomial (Chebyshev) | geometric for analytic $f$ | control of node placement | the samples are noisy, or nodes are fixed |
| Cubic spline, natural | $O(h^4)$ interior, $O(h^2)$ global | $f\in C^4$ | the end behaviour of $f$ is unknown *and* the whole interval is used |
| Cubic spline, clamped | $O(h^4)$ global | end slopes known to $O(h^4)$ | the end slopes are guesses |

Three caveats must be stated alongside any of these orders.

1. **Smoothness.** All of the orders above assume the function is $C^4$, and the
   polynomial error formula assumes $C^{n+1}$. Logs with bed boundaries are
   piecewise smooth at best, and at a boundary no interpolant has an order at all.
2. **Noise.** Interpolation passes through the data, so a $1\sigma$ noise level
   becomes a bias of the same size in the interpolant — and a derivative of the
   interpolant is far worse, as [01-12-03](./03-numerical-differentiation.md)
   shows.
3. **Extrapolation.** Every order quoted above is for the interpolated interval.
   Outside it, the error of a cubic spline grows like the cube of the distance
   from the nearest node, and nothing constrains it.

## 6. Python demonstration

The script `code/interpolation.py` builds the Lagrange and Newton forms, the
Runge comparison, and both spline variants, and measures all of the orders quoted
above. Selected output:

```text
  max |Lagrange - Newton| on 41 points = 7.105e-15
  They are algebraically identical; the difference is round-off.

  f(x) = 1/(1 + 25 x^2) on [-1, 1], max error on a 401-point grid
     n         uniform       Chebyshev
    12       3.663e+00       8.430e-02
    20       5.979e+01       1.772e-02
    24       2.570e+02       8.166e-03

  f(x) = exp(x) on [0, 1]; max error over 20 points per interval
   nodes         h      linear     natural     clamped                orders
       8    0.1250   4.989e-03   2.077e-03   1.690e-06
      16    0.0625   1.287e-03   5.200e-04   1.069e-07    1.96  2.00  3.98
      32    0.0312   3.267e-04   1.300e-04   6.716e-09    1.98  2.00  3.99
      64    0.0156   8.231e-05   3.251e-05   4.209e-10    1.99  2.00  4.00
     256    0.0039   5.175e-06   2.032e-06   1.647e-12    2.00  2.00  4.00

  data at depths 0, 0.25, 0.5, 0.75, 1.0: [0.0, 0.0, 1.0, 1.0, 1.0]
  spline maximum      = 1.107290 at x = 0.596
  overshoot above the largest datum (1.0) = 0.107290
  undershoot below the smallest datum (0.0) = -0.130590
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Lagrange and Newton agree to $7\times10^{-15}$ | the basis is a numerical choice, not a mathematical one |
| Runge error grows with $n$ on equispaced nodes | "more data" is not a convergence strategy when nodes are fixed |
| Chebyshev error falls monotonically | controlling node placement is what makes high order usable |
| linear 2.00, natural 2.00, clamped 4.00 | the *boundary condition*, not the stencil, sets the global order |
| natural spline interior order 4.00, global 2.00 | quote an order with the window it was measured on |
| spline overshoot of 0.107 on a unit step | bounded physical quantities need shape-preserving schemes |

> **Breaking exercise.** In `report_spline_orders`, replace `math.exp` with
> `lambda x: math.sin(math.pi * x)`, for which $f''(0)=f''(1)=0$. Predict, before
> running, whether the natural spline will now reach order 4 globally. Then run
> it and explain the result from the boundary conditions.

## 7. Common mistakes

1. **Believing the interpolation error is controlled by the number of points.**
   It is controlled by the product $\max|\omega(x)|$, which for equispaced nodes
   *grows* with $n$. See the table in §3.2.
2. **Quoting a spline order without saying which spline.** "Cubic splines are
   fourth order" is true for the clamped spline and false in the max norm for the
   natural one. The measured numbers are 4.00 and 2.00.
3. **Quoting an order from a non-asymptotic range.** The natural-spline interior
   order measures 8.80 and 4.18 before settling at 4.00. Orders must be taken
   from the regime where they are stable.
4. **Extrapolating.** No interpolant has an extrapolation error bound. The
   tendency to extrapolate a gravity profile "just a little beyond the last
   station" is the most common misuse of everything in this lesson.
5. **Using an interpolant where an approximation is needed.** Passing exactly
   through noisy data injects the noise into every derived quantity. If the
   samples have errors, fit rather than interpolate.
6. **Forgetting that a spline is a *global* construct.** Changing one datum
   changes the entire spline through the moment equations, unlike a local
   (Hermite or monotone) scheme. For very long logs this is a performance issue
   as well as a modelling one.
7. **Assuming smoothness across a boundary.** A well log crossing a facies change
   is piecewise smooth; the interpolation error at the boundary is dominated by
   the jump, not by $h^4$.

## 8. Real-world applications

- **Gravity and magnetic survey processing.** Profiles and grids are interpolated
  onto common stations before filtering or upward continuation. Choosing a spline
  rather than linear interpolation changes the computed vertical gradient at the
  level of several per cent, and that gradient is what an interpretation reads.
- **Wireline log analysis.** Sonic, density and neutron logs are sampled at
  different depths and must be placed on a common grid. A spline is standard;
  monotone interpolation is required for volume fractions, and this is a
  real constraint in petrophysics, not a detail.
- **Seismic velocity models.** Published models are coarsely sampled in depth;
  every ray tracer interpolates them thousands of times per event. An $O(h^4)$
  interior error against a millisecond-level pick accuracy is what makes the
  interpolation invisible in the result.
- **Bathymetry and topography.** Gridded products such as
  [NOAA ETOPO global relief](https://www.ngdc.noaa.gov/mgg/global/) are built by
  interpolating and merging heterogeneous sources, and the interpolation choice
  determines the apparent roughness of the seafloor at scales below the source
  resolution.
- **GNSS and tide-gauge time series.** Irregular sampling in time is regularised
  by interpolation before spectral analysis; the interpolation kernel is a
  filter, and an interpolant that overshoots introduces spectral leakage that the
  analysis will then attribute to the Earth. See
  [10 Fourier Analysis](../10-fourier-analysis/README.md).

## 9. Further reading

- **de Boor, C. (2001). *A Practical Guide to Splines* (revised ed.). Springer.**
  Level: graduate. The definitive treatment, including the error theory that
  distinguishes the natural and clamped cases.
- **Hall, C. A., & Meyer, W. W. (1976). Optimal error bounds for cubic spline
  interpolation. *Journal of Approximation Theory*, 16(2), 105–122.** Level:
  graduate. The origin of the interior-versus-boundary order distinction used in
  §3.4.
- **Trefethen, L. N. (2013). *Approximation Theory and Approximation Practice*.
  SIAM.** Level: graduate. Chebyshev interpolation done properly, with the
  barycentric formula that supersedes the naive Lagrange evaluation used here for
  clarity.
- **Berrut, J.-P., & Trefethen, L. N. (2004). Barycentric Lagrange interpolation.
  *SIAM Review*, 46(3), 501–517.** Level: graduate. The paper to read before
  implementing polynomial interpolation in production: it explains why the
  barycentric form is stable and the Lagrange form is not.
- **Isaaks, E. H., & Srivastava, R. M. (1989). *An Introduction to Applied
  Geostatistics*. Oxford University Press.** Level: intermediate to graduate.
  The geostatistical alternative to deterministic interpolation: kriging as
  optimal approximation rather than exact interpolation.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 10. Exercises

Full statements and difficulty grading are in
[`exercises/02-interpolation-exercises.md`](./exercises/02-interpolation-exercises.md),
with worked solutions in
[`exercises/02-interpolation-solutions.md`](./exercises/02-interpolation-solutions.md).

**★1.** Write the Lagrange cardinal polynomials for the three nodes $0,1,3$ and
evaluate the interpolant at $x=2$ for $y=(1,2,0)$.

**★2.** Construct the divided-difference table for the same data and evaluate the
Newton form at $x=2$. Confirm the two agree.

**★3.** Show that $\max_{[-1,1]}|\omega(x)|$ for equispaced nodes at $n=2$ is
$2/(3\sqrt3)$ and compute the error bound for $f=\mathrm{e}^x$ on $[-1,1]$.

**★4.** A well log has values 0.19, 0.21, 0.22 at depths 1000, 1001, 1002 m.
Estimate the value at 1001.4 m by linear interpolation and state the size of the
curvature error if the second derivative is $2\times10^{-4}\ \mathrm{m^{-1}}$.

**★★5.** Derive the tridiagonal moment system of §3.3 from the $C^1$ continuity
condition, showing each step.

**★★6.** For the natural spline on nodes $0,1,2,3$ with $y=(0,1,1,0)$, solve for
the moments and evaluate the spline at $x=1.5$. State the value of $s''$ at the
ends and comment.

**★★7.** Explain, using the error formula, why the Runge function's equispaced
interpolation error grows roughly by a constant factor per node, and estimate
that factor from the table in §3.2.

**★★8.** A gravity profile is sampled at $x=0,100,\dots,1000$ m. You need a
value at $x=1500$ m. Write a short paragraph stating what you would do, and why
the sentence "I will use a cubic spline" is not an answer.

**★★★9.** Construct a data set of 20 equispaced samples of
$f(x)=1/(1+25x^2)$ with 1% relative noise, and compare the max interpolation
error obtained by (a) an interpolating polynomial, (b) a cubic spline, (c) a
degree-6 least-squares fit. Report the measured errors, and explain why the
ranking is the opposite of the noise-free case.

**★★★10.** A published map of a gravity field is described as "interpolated with
a bicubic spline from a 5 km grid". Write a critique: what can be inferred from
the map at 1 km scale, what cannot, and what diagnostic would reveal whether
overshoot has produced spurious anomalies?

## 11. Self-assessment checklist

- [ ] I can state the interpolation error formula and identify the function
      factor and the node factor.
- [ ] I can explain the Runge phenomenon in one paragraph without referring to
      the Runge function specifically.
- [ ] I can write the Chebyshev node formula and say what it optimises.
- [ ] I can derive the spline moment equations from the continuity conditions.
- [ ] I can state the natural and clamped end conditions and the global order
      each produces, with the measured numbers.
- [ ] I can explain why an order must be quoted with a window and an $h$ range.
- [ ] I can give two physical quantities for which a spline overshoot is not
      acceptable, and name the alternative.

## Related lessons

- [01-12-01 Root Finding: Bisection, Newton, Secant and Robust Hybrids](./01-root-finding.md)
  — what to do with the interpolant once you have one; also the source of the
  tabulated functions this lesson cautions about.
- [01-12-03 Numerical Differentiation and Finite-Difference Stencils](./03-numerical-differentiation.md)
  — why differentiating an interpolant is worse than the interpolation error
  alone suggests.
- [01-12-04 Numerical Integration: Trapezoid, Simpson, Gauss Quadrature](./04-numerical-integration.md)
  — the same node-placement question, asked about quadrature weights instead of
  interpolants.
- [01-07-03 Linear Systems, Gaussian Elimination and LU Factorisation](../07-linear-algebra/03-systems-and-elimination.md)
  — the tridiagonal solve at the centre of every spline.
- [10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md) —
  interpolation as a filter, and the spectral consequences of choosing a kernel.
- [17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md) — the same
  problem in its data-science setting, with resampling and geostatistics.
