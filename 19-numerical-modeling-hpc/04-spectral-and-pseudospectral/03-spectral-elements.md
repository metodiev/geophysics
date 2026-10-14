---
id: 19-04-03
title: "Spectral Element Methods and Their Geophysical Use"
level: research
prereqs: ["19-03-02", "19-04-01", "19-01-04"]
tags: [numerical-modelling, spectral-elements, gll, diagonal-mass, stability, numerical-modelling]
---

# Spectral Element Methods and Their Geophysical Use

**All models and data in this module are SYNTHETIC.** The meshes, orders and
manufactured solution are chosen teaching models; every number is printed by
[`code/spectral_elements_demo.py`](./code/spectral_elements_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** Gauss-Lobatto-Legendre (GLL) nodes and weights and **verify** the
   degree of polynomial exactness the rule delivers.
2. **Derive** why the GLL quadrature of the mass matrix is diagonal, and
   **measure** the off-diagonal residual.
3. **State** the two different errors a spectral element carries — the quadrature
   (lumping) error and the discretisation error — and **separate** them by
   measurement.
4. **Measure** exponential $p$-convergence and algebraic $h$-convergence for the
   same discretisation and **explain** when each refinement is the right tool.
5. **Measure** how the largest eigenvalue of the discrete operator depends on the
   polynomial order and on the element size, and **derive** the explicit
   time-step limit that follows.
6. **Explain** why a spectral-element code is the standard choice for
   wave propagation on a heterogeneous, geometrically complex Earth.
7. **State** what a diagonal mass matrix buys and what it costs, with the measured
   numbers.

## Prerequisites

- [19-03-02 Element Types, Shape Functions and Quadrature](../03-finite-element-and-volume/02-fem-element-types.md) —
  Lagrange elements, quadrature policy and the conditioning of node sets, all of
  which this lesson reuses.
- [19-04-01 Spectral Methods: Basis Choice and Exponential Convergence](01-spectral-methods.md) —
  why a global high-order basis converges exponentially.
- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](../01-numerical-foundations/04-numerical-dispersion-diffusion.md) —
  the finite-order error a spectral element is designed to avoid.

## 1. The hybrid idea

A spectral method on a single global basis cannot represent a geometrically
complex domain, and it cannot localise refinement where the solution varies
quickly. A finite element can do both, but its accuracy improves only
algebraically in $h$. A **spectral element** takes both: partition the domain
into elements (as FEM does), and inside each element use a high-order polynomial
basis at specially chosen nodes (as a spectral method does).

The choice of nodes is not free. It is **Gauss-Lobatto-Legendre** nodes — the
endpoints plus the roots of $P_p'$ — and the reason is measured in Section 3.
The resulting method is sometimes called $p$-type, sometimes "high-order
(hp)", and in seismology it is the basis of production codes for wave
propagation in heterogeneous media.

## 2. GLL quadrature: what it integrates exactly

With $p+1$ GLL nodes on $[-1,1]$ the quadrature is exact for polynomials of
degree up to $2p-1$, one degree less than Gauss-Legendre with the same number of
nodes. The endpoints are included, which is what allows continuity between
elements, and the price is that single degree. The demonstration measures:

| $p$ | $\sum_j w_j - 2$ | error at degree $2p-1$ | error at degree $2p$ |
|---|---|---|---|
| 2 | $2.2\times10^{-16}$ | $0.0\times10^{0}$ | $2.667\times10^{-1}$ |
| 4 | $2.2\times10^{-16}$ | $1.4\times10^{-17}$ | $1.451\times10^{-2}$ |
| 6 | $0.0\times10^{0}$ | $6.9\times10^{-18}$ | $8.611\times10^{-4}$ |
| 8 | $4.4\times10^{-16}$ | $6.9\times10^{-18}$ | $5.237\times10^{-5}$ |
| 12 | $2.2\times10^{-16}$ | $3.5\times10^{-18}$ | $1.988\times10^{-7}$ |

The weights sum to 2 exactly and the exactness column is round-off; the first
failing degree is non-zero by construction, and it is the degree at which an
element's *mass* integrand sits — which is why the lumping error of Section 3 is
not an accident.

## 3. The diagonal mass matrix, measured

Evaluate the mass integral with the element's own nodes and weights:

$$\tilde{M}_{ij} = \sum_{q=0}^{p} w_q\,\varphi_i(x_q)\,\varphi_j(x_q)
= \delta_{ij}\,w_i, \tag{3.1}$$

because the Lagrange basis satisfies $\varphi_i(x_q) = \delta_{iq}$. This is
exact algebra, and it makes the mass matrix diagonal **by construction** — no
lumping approximation is involved in the identity, only in the integral it
replaces. Measured against the exact mass matrix computed with a high-order Gauss
rule:

| $p$ | max off-diagonal (GLL) | $\max|\operatorname{diag}(\tilde{M}) - \operatorname{diag}(M_{\rm exact})|$ |
|---|---|---|
| 2 | $0.000\times10^{0}$ | $2.667\times10^{-1}$ |
| 4 | $0.000\times10^{0}$ | $7.901\times10^{-2}$ |
| 6 | $0.000\times10^{0}$ | $3.751\times10^{-2}$ |
| 8 | $0.000\times10^{0}$ | $2.185\times10^{-2}$ |

Two columns, two entirely different statements. The first is a property of the
quadrature and the basis: exactly zero, at every order. The second is the price:
the diagonal entries differ from the true integrals, and the difference decays
only slowly with $p$ ($2.7\times10^{-1}$ at $p=2$ to $2.2\times10^{-2}$ at $p=8$
— a factor 12 over a factor 4 in $p$).

**This is the central trade of the method.** A diagonal mass matrix turns an
implicit step into an explicit one (no linear solve for the mass operator), which
is decisive for time-domain wave propagation. The price is a quadrature error
that is $O(10^{-1})$ at low order and falls only algebraically. It is a
*modelling choice*, and a code that silently makes it has decided something the
user should know about.

## 4. Two convergence modes, measured

### 4.1 p-refinement at fixed element size

Two elements spanning $(0,1)$, exact $u = \sin(\pi x)$:

| $p$ | ndof | $\mathrm{L}^2$ error | ratio to previous $p$ | $\mathrm{H}^1$ error |
|---|---|---|---|---|
| 2 | 5 | $1.791\times10^{-2}$ | — | $2.068\times10^{-1}$ |
| 3 | 7 | $1.464\times10^{-3}$ | $1.223\times10^{1}$ | $2.675\times10^{-2}$ |
| 4 | 9 | $1.076\times10^{-4}$ | $1.361\times10^{1}$ | $2.637\times10^{-3}$ |
| 6 | 13 | $3.781\times10^{-7}$ | $2.846\times10^{2}$ | $1.369\times10^{-5}$ |
| 8 | 17 | $7.961\times10^{-10}$ | $4.749\times10^{2}$ | $3.796\times10^{-8}$ |
| 10 | 21 | $1.106\times10^{-12}$ | $7.196\times10^{2}$ | $6.535\times10^{-11}$ |
| 12 | 25 | $3.145\times10^{-15}$ | $3.518\times10^{2}$ | $7.981\times10^{-14}$ |

The error falls by two to three orders of magnitude per increment of $p$, and the
$\mathrm{H}^1$ error tracks it down to $8\times10^{-14}$ at $p = 12$ — the
round-off floor of the assembly. **The refinement stops because the arithmetic
stops, not because the method stops.** Nothing improves past $p=12$ on this
mesh, and a table that continues to $p=20$ would report noise.

### 4.2 h-refinement at fixed order

The same discretisation with $p = 4$ and the mesh refined:

| $n_{\rm elem}$ | ndof | $\mathrm{L}^2$ error | order | $\mathrm{H}^1$ error | order |
|---|---|---|---|---|---|
| 2 | 9 | $1.076\times10^{-4}$ | — | $2.637\times10^{-3}$ | — |
| 4 | 17 | $3.374\times10^{-6}$ | 4.995 | $1.670\times10^{-4}$ | 3.981 |
| 8 | 33 | $1.055\times10^{-7}$ | 4.999 | $1.047\times10^{-5}$ | 3.995 |
| 16 | 65 | $3.299\times10^{-9}$ | 5.000 | $6.549\times10^{-7}$ | 3.999 |
| 32 | 129 | $1.031\times10^{-10}$ | 5.000 | $4.094\times10^{-8}$ | 4.000 |

Orders 5 and 4 per halving of $h$ — the $p+1$ and $p$ of any order-$p$ Galerkin
method. So a spectral element refines in $h$ exactly like a finite element of the
same order, and the extra ingredient is Section 4.1's behaviour in $p$.

The practical rule: **use $p$ when the solution is smooth inside each element,
and $h$ when it is not** — at an interface, a discontinuity, a strongly varying
coefficient, or where the geometry forces small elements. The two are
complementary, and the $(h,p)$ pair is chosen per element in an $hp$ code.

### 4.3 A note on measuring the error norm

The demonstration integrates the error with a Gauss rule of order $p+6$ rather
than with the element's own GLL rule. This is not pedantry: the GLL rule
under-integrates the error integrand (degree $2p$ against exactness $2p-1$), and
using it inflates the apparent convergence order. The effect was large enough to
be visible in this very demonstration during its development — the $p=4$
h-refinement appeared to converge at order 6 rather than 5 until the error norm
was computed accurately. **The error norm is part of the experiment.**

## 5. The eigenvalue spectrum, measured, and the timestep it dictates

For explicit time integration of a wave equation, the stable step is set by the
extreme eigenvalue of the generalised problem $Kv = \lambda Mv$:
$\Delta t \le 2/\sqrt{\lambda_{\max}}$. Both matrices are built with the
element's own GLL rule, as a spectral element code does. Measured at $h = 0.5$:

| $p$ | $\lambda_{\max}$ | $\Delta t$ limit (s) | $p^4/h^2$ model |
|---|---|---|---|
| 2 | 81.7359 | 0.221220 | 64.0 |
| 4 | 766.9212 | 0.072220 | 1024.0 |
| 6 | 3245.7555 | 0.035105 | 5184.0 |
| 8 | 9397.6063 | 0.020631 | 16384.0 |
| 10 | 21780.0650 | 0.013552 | 40000.0 |

Fitted exponent in $p$ over $p = 2\dots10$: **3.469**. Note that the commonly
quoted $p^4$ model *overpredicts* at low order (81.7 measured against 64.0 at
$p=2$, then 766.9 against 1024.0 at $p=4$) — the measured exponent is what a
stability estimate should use, and it is between $p^3$ and $p^4$ over this range.
Measured against element size at $p=4$:

| $n_{\rm elem}$ | $h$ | $\lambda_{\max}$ | $\Delta t$ limit (s) | $1/h^2$ model |
|---|---|---|---|---|
| 2 | 0.5000 | 766.9212 | 0.072220 | 4.0 |
| 4 | 0.2500 | 3128.3967 | 0.035758 | 16.0 |
| 8 | 0.1250 | 12586.0871 | 0.017827 | 64.0 |
| 16 | 0.0625 | 50419.9128 | 0.008907 | 256.0 |
| 32 | 0.0312 | 201755.9886 | 0.004453 | 1024.0 |

Fitted exponent in $1/h$: **2.009** — the familiar $h^{-2}$, and the timestep
limit falls by $\sqrt{2}$ per refinement ($0.0722 \to 0.0358 \to 0.0178$, a factor
2.02 per halving).

Put together, the two measurements give the design trade of a spectral-element
wave solver in one sentence. Raising $p$ improved the $\mathrm{L}^2$ error by
factors of $1.2\times10^{1}$, $1.4\times10^{1}$, $2.8\times10^{2}$, $4.7\times10^{2}$
and $7.2\times10^{2}$ in Section 4.1 while shrinking the timestep like
$p^{-1.73}$ (the square root of the measured $p^{3.469}$). Refining $h$ improved
the error like $h^{5}$ while shrinking the timestep like $h^{-1}$. Both refinement
directions buy accuracy by making the problem stiffer, and the choice between them
is a comparison of those two measured behaviours on the actual solution.

## 6. A fully worked resolution-and-stability estimate

A spectral-element model uses elements of size $h = 0.5$ in dimensionless units
and order $p = 4$, and the run must be characterised by a timestep and a
resolution statement. Using only the measured quantities of Section 5:

1. **Stability.** At $p=4$, $h=0.5$ the measured $\lambda_{\max} = 766.9212$, so
   an explicit scheme requires $\Delta t \le 2/\sqrt{766.9212} = 0.072220$.
2. **Refinement.** Go to $h = 0.25$ at $p=4$: the measured exponent 2.009 gives
   $\lambda_{\max} = 766.9212\times2^{2.009} = 3.08\times10^{3}$, and the timestep
   limit falls to $2/\sqrt{3.08\times10^{3}} = 0.0360$ — the measured
   $3128.3967$ and $0.035758$. The prediction reproduces the measurement to three
   digits from two numbers, which is the whole reason for measuring exponents.
3. **Order instead of size.** Go to $p = 8$ at $h = 0.5$: the measured exponent
   3.469 gives $\lambda_{\max} = 766.9212\times(8/4)^{3.469} = 8.46\times10^{3}$
   against the measured $9.40\times10^{3}$ — 10% low, because a single power law
   is an approximation over a factor 2 in $p$. The timestep limit is
   $2/\sqrt{9.40\times10^{3}} = 0.020631$, i.e. 3.5 times smaller.
4. **What this lesson does *not* provide: a resolution criterion.** Stability and
   resolution are different constraints. The resolution limit is the frequency at
   which the scheme's numerical phase speed departs from the physical one by more
   than an allowed tolerance, and it can only be obtained from a dispersion
   analysis of the specific scheme — the subject of lesson
   [01-04](../01-numerical-foundations/04-numerical-dispersion-diffusion.md). The
   honest position is that this lesson supplies the stability half of the
   characterisation and refers the resolution half elsewhere, rather than quoting
   a nodes-per-wavelength rule of thumb that was not measured here.
5. **Cost.** Doubling $p$ costs a factor 3.5 in timesteps and gains the accuracy
   factors measured in Section 4.1. Whether that is a bargain depends on the
   quantity of interest, and the two numbers belong in the same sentence.

## 7. Assumptions and regime of validity

1. **Affine, Cartesian elements and a constant coefficient.** The measured
   exponents are for that case; a distorted element introduces a Jacobian that
   varies inside the element, and a strongly varying coefficient raises
   $\lambda_{\max}$.
2. **Node parity.** Odd/even effects in the eigenvalue and in the error are
   visible in the tables ($p=2 \to 4 \to 6$ ratios differ from $p=3 \to 4$);
   quoting a single exponent over all $p$ hides them.
3. **GLL quadrature of both matrices.** The diagonal mass identity (3.1) holds
   only if the quadrature nodes *are* the interpolation nodes. With Gauss nodes
   the mass matrix is dense, and the measured lumping error of Section 3 does not
   apply.
4. **Explicit time integration for the $\Delta t$ statement.** An implicit scheme
   trades the stability limit for a linear solve per step, and the
   preconditioning problem of lesson
   [19-03-03](../03-finite-element-and-volume/03-fem-assembly.md), Section 6, returns.
5. **Round-off floors every convergence table.** $p$-refinement stops at
   $3.1\times10^{-15}$; nothing above that is measurable in double precision.
6. **One-dimensional deduction.** The two- and three-dimensional statements of
   the timestep limit carry an extra factor from the dimension (a sum over
   directions) that must be measured rather than assumed.

## 8. Mastery checkpoint

Complete this without notes.

> A spectral-element wave model uses $p = 6$ on elements of size $h = 0.5$ in
> dimensionless units.
>
> **(a)** State the exactness degree of the $p=6$ GLL rule on one element.
> **(b)** State, with the measured value from this lesson, the largest generalised
> eigenvalue at $p=6$, $h=0.5$ and the explicit timestep limit it implies.
> **(c)** You double $p$ to 12 and halve $h$ to 0.25. Using the measured
> exponents 3.469 in $p$ and 2.009 in $1/h$, predict the new $\lambda_{\max}$ and
> the new timestep limit.
> **(d)** Explain the difference between the off-diagonal column and the diagonal
> column of the table in Section 3, and state which of them is a modelling choice.
> **(e)** The code reports an $\mathrm{L}^2$ error that stopped improving at
> $p = 12$. State the reason and one way to know it is the reason.

A worked version appears with the
[exercises](exercises/03-spectral-elements-exercises.md).

## 9. Common pitfalls

1. **Confusing the two errors.** The off-diagonal mass error is exactly zero; the
   diagonal error is $2.7\times10^{-1}$ at $p=2$. Reporting "the mass matrix is
   exact" conflates them.
2. **Believing a diagonal mass is free.** It is a quadrature choice with a
   measured price that falls only algebraically in $p$.
3. **Continuing a $p$ table past the floor.** Measured: nothing improves beyond
   $1.1\times10^{-12}$ at $p=10$ and $3.1\times10^{-15}$ at $p=12$.
4. **Measuring the error with the element's own rule.** The under-integrated error
   norm inflated the apparent $h$-order from 5 to 6 in this demonstration's own
   development.
5. **Using a quoted $p^4$ stability scaling without checking.** The measured
   exponent here is 3.469, and the $p^4$ model overpredicts at $p=2$ and $p=4$.
6. **Choosing $p$ where $h$ is needed.** At an interface or a sharp coefficient
   contrast the solution is not smooth inside the element, and $p$-refinement
   buys much less; the measured exponential rate is a statement about smooth $u$.
7. **Reporting only the stability limit or only the resolution limit.** They are
   independent constraints on the same run.

## 10. Related modules

- [19-04-04 Spherical Harmonic Modelling of Global Fields](04-spherical-harmonics-modelling.md) —
  the same high-order idea on a sphere, where elements are rarely used at all.
- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](../01-numerical-foundations/04-numerical-dispersion-diffusion.md) —
  the resolution limit referenced in Section 6.
- [19-08-01 Simulating a 2-D/3-D Seismic Wavefield](../08-geophysical-simulation-case-studies/01-simulate-seismic-wavefield.md) —
  the production problem spectral elements were developed for.
- [19-06-02 Shared-Memory Parallelism: OpenMP and Threading](../06-hpc-and-parallel-computing/02-shared-memory-parallelism.md) —
  why the diagonal mass matters for parallel efficiency.
- [03-12-04 Verification vs Validation: Benchmarks and Convergence Tests](../../03-scientific-computing/12-numerical-simulation-python/04-verification-and-validation.md) —
  the convergence-study practice used in Section 4.

## Materials

- Demonstration: [`code/spectral_elements_demo.py`](./code/spectral_elements_demo.py).
- Exercises: [`exercises/03-spectral-elements-exercises.md`](./exercises/03-spectral-elements-exercises.md)
  with worked [solutions](./exercises/03-spectral-elements-solutions.md).
