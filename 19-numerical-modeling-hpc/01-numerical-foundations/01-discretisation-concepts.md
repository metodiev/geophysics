---
id: 19-01-01
title: "Discretisation: Grids, Nodes, Cells and Degrees of Freedom"
level: graduate
prereqs: ["01-12-07", "03-12-01", "03-02-07"]
tags: [numerical-modelling, hpc, discretisation, grids, degrees-of-freedom, staggering]
---

# Discretisation: Grids, Nodes, Cells and Degrees of Freedom

A continuous model has infinitely many unknowns. A computer can hold finitely
many numbers, so every simulation begins with a choice of *where* the unknowns
live and *how many* there are. That choice is not bookkeeping: it decides
whether a material contrast is represented exactly or with a 3 % flux error, how
much memory the run needs, how ill-conditioned the resulting linear system is,
and how large the discretisation error will be before a single line of physics
is evaluated.

This lesson builds the vocabulary — grid, node, cell, degree of freedom, node-
centred and cell-centred storage — and then quantifies each of those decisions
against a closed-form answer, so that the error of a discretisation is a
*number you can predict* rather than a surprise you discover. **All models and
data in this module are SYNTHETIC**: the grids, material contrasts and functions
below are chosen teaching values, not measurements. Every number quoted here is
printed by `code/discretisation_concepts_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Count** the degrees of freedom of a node-centred and a cell-centred
   discretisation in one, two and three dimensions, and the memory each needs.
2. **Convert** a resolution requirement expressed in points per wavelength (or
   cells per feature) into a grid spacing and a total unknown count.
3. **Derive** the face conductance of a material interface from the series
   argument, and explain why the harmonic mean is exact while the arithmetic
   mean is not.
4. **Predict** the discretisation error of the midpoint and trapezoid rules for
   a given integrand, including the exact constant, and confirm it numerically.
5. **Compare** a discrete norm with the continuous norm it approximates and
   state why an apparently convergent scheme can still be biased.
6. **Explain** why refinement improves accuracy and simultaneously worsens the
   conditioning of the linear system, and quantify both.

## Prerequisites

- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](../../01-mathematics/12-numerical-methods/07-pde-discretisation.md) —
  the words consistency, stability and convergence used throughout this folder.
- [03-12-01 A 1-D Finite-Difference Solver from Scratch](../../03-scientific-computing/12-numerical-simulation-python/01-finite-difference-1d.md) —
  a first grid and a first stencil in code.
- [03-02-07 Memory Layout, Strides and Cache-Aware Performance](../../03-scientific-computing/02-numpy/07-memory-performance.md) —
  how the numbers you count here are actually stored and traversed.

## 1. Intuition: a grid is a promise about what you cannot see

A grid is not a picture of the Earth. It is a promise: *between the points I
store, nothing varies that matters.* Everything else follows from how well that
promise holds.

Two quantities are being separated by the act of discretisation.

- The **field** is defined everywhere. A pressure wave has a value at every
  point of the water column.
- The **representation** is defined at finitely many places. The solver only
  ever knows those values.

When a material property changes between two stored values — a sandstone
overlying a shale, a water table, a Moho — the solver must decide what happens
*at the jump*. Nothing in the physics tells it: the answer depends on how the
unknowns were placed. Section 3.2 shows the size of that decision, and it is
larger than most beginners expect.

## 2. Precise definitions

**Domain.** The region $\Omega \subset \mathbb{R}^{d}$ in which the model
equation holds, $d = 1, 2$ or $3$.

**Grid (mesh).** A set of $N$ points $\{x_{i}\}_{i=1}^{N} \subset \bar\Omega$
together with the spacing rule that generated them. Uniform (regular) grids have
$x_{i} = x_{0} + (i-1)h$ with a single spacing $h$; curvilinear grids have
non-uniform spacing or non-orthogonal coordinates.

**Node.** A point at which an unknown is stored. In a **node-centred**
(collocated) scheme, node $i$ carries the field value $u_{i}\approx u(x_{i})$.

**Cell (control volume).** The region $[x_{i-1/2}, x_{i+1/2}]$ associated with a
cell centre $x_{i}$, where $x_{i\pm1/2}$ are the **cell faces**. In a
**cell-centred** scheme the unknown is the cell average $\bar u_{i}$, and the
faces are where differences are taken. Cell-centred schemes are also called
*staggered* when different fields live on different node sets — for example
pressure at cell centres and velocity at faces.

**Degree of freedom (DOF).** One scalar unknown the solver must determine. A
scalar field on a $N_x\times N_y$ grid has $N_x N_y$ DOF; a $d$-component vector
field has $d$ times as many. DOF is what determines memory and, with the
algorithm, run time.

**Discretisation error.** The difference between the exact solution of the
continuous problem and the exact solution of the discrete problem,
$e = u - u_h$. It is not the same as the *algebraic* error of an iterative
solver, and this folder keeps the two apart.

## 3. Derivations

### 3.1 Degrees of freedom and storage

For a uniform grid over a domain of length $L$ with $N$ cells per direction:
$h = L/N$, the number of cell centres per direction is $N$, and the number of
nodes is $N+1$. In $d$ dimensions the counts are $N^{d}$ and $(N+1)^{d}$. The
relative difference, $1 - (N/(N+1))^{d}$, is $3\,\%$ at $N = 100$ in 3-D, which
is exactly the size of the ambiguity that trips up conversions between the two
conventions.

The demonstration prints the counts for $L = 1$ km, $N = 100$ per direction,
with float64 storage ($8$ bytes per DOF):

| grid | per direction | DOF | float64 (MiB) |
|---|---|---|---|
| 1-D node-centred | 101 | 101 | 0.00 |
| 1-D cell-centred | 100 | 100 | 0.00 |
| 2-D node-centred | 101 | 10 201 | 0.08 |
| 2-D cell-centred | 100 | 10 000 | 0.08 |
| 3-D node-centred | 101 | 1 030 301 | 7.86 |
| 3-D cell-centred | 100 | 1 000 000 | 7.63 |

with $h = 0.010000$ km $= 10.000$ m in every case. A memory estimate is exact
arithmetic on the DOF count; it is one of the few numbers in a modelling project
that can be trusted before the code is written.

### 3.2 Storing a material contrast: why the harmonic mean is exact

Consider steady conduction through a column of length $L$ with conductivity
$\kappa(x)$ piecewise constant: $\kappa_1$ for $x < x_c$ and $\kappa_2$ for
$x > x_c$. The flux $q$ (W m$^{-2}$) is the same in both materials, and the
temperature drop across layer $i$ is $q\,t_i/\kappa_i$. Adding the drops,

$$q = \frac{\Delta T}{\dfrac{t_1}{\kappa_1} + \dfrac{t_2}{\kappa_2}},
\qquad
\kappa_{\text{eff}} = \frac{L}{\dfrac{t_1}{\kappa_1} + \dfrac{t_2}{\kappa_2}}.$$

This is the **series** (harmonic) combination. The demonstration chooses
$\kappa_1 = 1.00$, $\kappa_2 = 4.00\ \mathrm{W\,m^{-1}\,K^{-1}}$,
$x_c = 0.40$ km, $L = 1$ km, $\Delta T = 100$ K and obtains

$$\kappa_{\text{eff}} = 1.818182\ \mathrm{W\,m^{-1}\,K^{-1}},
\qquad q_{\text{exact}} = 181.818182\ \mathrm{W\,m^{-2}}.$$

Now discretise. In a cell-centred scheme the conductance between two adjacent
cell centres separated by $h$ is the series combination of two half-cells,

$$K_{\text{face}} = \frac{1}{\dfrac{h/2}{\kappa_A} + \dfrac{h/2}{\kappa_B}}
= \frac{2\kappa_A\kappa_B}{h(\kappa_A + \kappa_B)},$$

so the effective face conductivity is the **harmonic mean**
$2\kappa_A\kappa_B/(\kappa_A+\kappa_B) = 1.6000$ here. Using it, the computed
flux is

$$q_{cc} = 181.818182\ \mathrm{W\,m^{-2}},
\qquad \text{error} = -2.8\times 10^{-13}\ \%,\ \text{i.e. round-off}.$$

A node-centred scheme has no faces; the natural (and wrong) move is to average
the nodal conductivities onto them. The arithmetic mean of the same two cells is
$0.5(\kappa_1+\kappa_2) = 2.5000$, i.e. $56\,\%$ too large, and the computed
flux becomes

$$q_{nc} = 186.915888\ \mathrm{W\,m^{-2}},\qquad
\text{error} = +2.804\ \%.$$

The conclusion is structural, not numerical: a first-order-accurate scheme in
the interior can carry a *large, non-vanishing* error at a material interface if
the averaging rule is wrong. The error does not fall with refinement — refining
only narrows the badly averaged region. Cell-centred storage removes the
problem by construction, because the unknowns sit where the material properties
are defined and the faces sit where the fluxes are.

### 3.3 Discretisation error is predictable, not mysterious

The composite **midpoint** rule for $\int_a^b g\,\mathrm dx$ with $N$ cells of
width $h$ has the Euler–Maclaurin expansion

$$\int_a^b g\,\mathrm dx - h\sum_{i=0}^{N-1} g(x_{i+1/2})
= \frac{h^{2}}{24}\left[g'(b)-g'(a)\right] + O(h^{4}),
$$

and the **trapezoid** rule

$$\int_a^b g\,\mathrm dx - h\left[\tfrac12 g(a)+\sum_{i=1}^{N-1} g(x_i)
+\tfrac12 g(b)\right] = -\frac{h^{2}}{12}\left[g'(b)-g'(a)\right] + O(h^{4}).$$

For $g(x) = x^{2}$ on $[0,1]$ both corrections are *exact*, not merely leading:
$g'(1)-g'(0) = 2$, so

$$\text{midpoint error} = -\frac{h^{2}}{12},
\qquad
\text{trapezoid error} = +\frac{h^{2}}{6}.$$

The demonstration reports, for $N = 10$ ($h = 0.1$):

| rule | measured error | predicted constant |
|---|---|---|
| midpoint | $-8.333\times10^{-4}$ | $h^{2}/12 = 8.333\times10^{-4}$ |
| trapezoid | $+1.667\times10^{-3}$ | $h^{2}/6 = 1.667\times10^{-3}$ |

and the successive error ratio is exactly $4.000000$ at every refinement, which
is the signature of a second-order rule. The sign difference carries
information: the midpoint rule underestimates, the trapezoid rule overestimates,
and the two errors differ by a factor of exactly two for this integrand.

### 3.4 A discrete norm is not the norm you meant

A solver reports norms of the *grid function* it stores, not of the continuous
field. Take $f(x) = x^{2}$ on $[0,1]$. The continuous $L^{2}$ norm is

$$\|f\|_{2} = \sqrt{\int_{0}^{1}x^{4}\,\mathrm dx} = \sqrt{1/5}
= 0.4472135955,$$

while a cell-centred grid function is measured with
$\|f_h\|_{2} = \sqrt{h\sum_i f(x_{i+1/2})^{2}}$. That sum is the midpoint rule
for $\int_0^1 x^4\,\mathrm dx$, whose error is $h^{2}/24\,[g'(1)-g'(0)] = h^{2}/6$
with $g = x^{4}$. Propagating through the square root,

$$\|f_h\|_{2} - \|f\|_{2} \approx \frac{h^{2}}{2\cdot 6\,\|f\|_{2}}
= 0.1863390\,h^{2}.$$

Measured: $0.1864014$, $0.1863545$, $0.1863429$, $0.1863400$,
$0.1863391$ for $N = 10, 20, 40, 80, 320$. The prediction is reproduced to five
figures. The practical lesson is blunt: **when a solver reports a stable norm
while the physics is wrong, the norm is measuring a different object** — the
grid function, not the field.

### 3.5 Refinement improves accuracy and ruins conditioning

For the one-dimensional Dirichlet Laplacian matrix
$T = h^{-2}\,\mathrm{tridiag}(-1,2,-1)$ with $h = 1/(N+1)$ the eigenvalues are
known in closed form, $\lambda_k = 4h^{-2}\sin^{2}(k\pi h/2)$, so

$$\kappa(T) = \frac{\lambda_{\max}}{\lambda_{\min}}
= \frac{1+\cos(\pi h)}{1-\cos(\pi h)}
\;\sim\; \frac{4}{\pi^{2}h^{2}} \sim \frac{4(N+1)^{2}}{\pi^{2}}.$$

The demonstration compares `numpy.linalg.cond` with the closed form:

| $N$ | measured $\kappa$ | exact formula | $4/(\pi^{2}h^{2})$ |
|---|---|---|---|
| 15 | 103.0869 | 103.0869 | 103.7529 |
| 63 | 1659.3796 | 1659.3796 | 1660.0463 |
| 255 | 26 560.0737 | 26 560.0737 | 26 560.7404 |
| 1023 | 424 971.1792 | 424 971.1792 | 424 971.8458 |

Halving $h$ multiplies the truncation error by $1/4$ and the condition number by
$4$. A solver whose iteration count grows like $\sqrt{\kappa}$ (conjugate
gradients) therefore needs twice as many iterations when you refine — a
different cost law from the $2^{d}$-fold growth in unknowns.

## 4. Worked example: sizing a grid before writing code

*A 3-D acoustic simulation is required over a $10\ \mathrm{km}\times
10\ \mathrm{km}\times 4\ \mathrm{km}$ box. The shortest wavelength to resolve is
$40$ m, and 10 points per wavelength are wanted. The scheme is second order in
space, so the discretisation error is $C h^{2}$ with $C\approx 0.1$ in
dimensionless units.*

1. Spacing: $h = 40/10 = 4$ m.
2. Cells per direction: $N_x = 10\,000/4 = 2500$, $N_y = 2500$,
   $N_z = 4000/4 = 1000$.
3. DOF for one scalar field: $2500\times2500\times1000 = 6.25\times10^{9}$, i.e.
   $6.25$ billion unknowns.
4. Memory for one float64 field: $6.25\times10^{9}\times8$ bytes
   $= 5.0\times10^{10}$ bytes $= 46.6$ GiB. A second-order explicit scheme needs
   at least three field copies (current, previous, and one work array), so about
   $140$ GiB.
5. Discretisation error: $C h^{2} = 0.1\times16\ \mathrm{m^{2}}$ — with the model
   normalised to unit amplitude and unit length this is a relative error of
   order $1.6\times10^{-3}$ per wavelength of propagation, which is why 10 points
   per wavelength is the usual working minimum.
6. Conditioning: with $h$ small, $\kappa \sim 4/(\pi^{2}h^{2})$; in 3-D the
   five-point Laplacian has $\kappa \sim \pi^{-2}(3/h^{2})$ at leading order, so
   an iterative solve has to contend with a system whose condition number is of
   order $10^{4}$ at this spacing — and the iteration count will grow as $h$
   shrinks.

The interesting number is step 4: at this resolution the run is not limited by
physics or by floating-point precision but by memory, and the honest answer to
"can we model this?" is "*not on one machine*". Recognising that here, before
writing the solver, is the whole point of counting DOF.

## 5. Assumptions and regime of validity

1. **Uniform, axis-aligned grids.** All counts above assume a tensor-product
   grid. Curvilinear or unstructured grids change the DOF counts (you count
   cells, not nodes) and destroy the simple conditioning formulas.
2. **Cell averages as unknowns.** The claim that a cell-centred quantity is the
   exact cell average holds only to the order of the reconstruction; the
   harmonic-mean result of §3.2 is exact for *steady, one-dimensional,
   piecewise-constant* coefficients. In two and three dimensions the interface
   must be aligned with cell faces for the same exactness.
3. **The error constants are asymptotic.** The $h^{2}/12$ and $h^{2}/6$ results
   for $x^{2}$ are exact because the Euler–Maclaurin series truncates for that
   integrand. For general integrands they are leading-order only, and the next
   term is $O(h^{4})$.
4. **Conditioning formulas assume Dirichlet boundaries and the second
   difference operator.** A Neumann condition lowers $\kappa$; a variable
   coefficient raises it; a preconditioner changes the number that a solver
   actually sees.
5. **Memory estimates ignore overhead.** Sparse matrices, index arrays and
   halo/ghost cells add tens of per cent in practice; the DOF arithmetic is a
   lower bound, not a budget.

## 6. Python demonstration

`code/discretisation_concepts_demo.py` prints every number quoted above. It

1. tabulates DOF and float64 storage for 1-D, 2-D and 3-D node- and cell-centred
   grids;
2. solves the two-material column with a harmonic-mean face conductance and with
   an arithmetic node average, and compares both with the exact series flux;
3. shows that the midpoint and trapezoid errors for $x^{2}$ equal $h^{2}/12$ and
   $h^{2}/6$ exactly, with error ratio $4.000000$;
4. compares the discrete and continuous $L^{2}$ norms of the same function,
   recovering the predicted constant $0.1863390$;
5. reproduces the closed-form and asymptotic condition numbers of the discrete
   Laplacian.

```bash
cd 19-numerical-modeling-hpc/01-numerical-foundations/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python discretisation_concepts_demo.py
```

## Mastery checkpoint

Without notes:

> A 2-D domain of $20\ \mathrm{km}\times 20\ \mathrm{km}$ is to be modelled with
> 12 points per wavelength for waves of wavelength $150$ m, with two scalar
> fields stored. **(a)** Give $h$, $N$ per direction, the total DOF and the
> float64 memory for the two fields. **(b)** A conductivity contrast of
> $1:5$ is stored node-centred with arithmetic averaging of the faces: estimate
> the flux error. **(c)** State the two ways to remove that error. **(d)** If the
> grid is refined by a factor of two, state what happens to the discretisation
> error and to the condition number of the Laplacian.

Parts (a) and (b) are worked in
[`exercises/01-discretisation-concepts-solutions.md`](exercises/01-discretisation-concepts-solutions.md).

## Common pitfalls

1. **Confusing nodes with cells.** A factor $(1+1/N)^{d}$ is negligible at
   $N = 10^{4}$ and a $3\,\%$ error at $N = 100$ — the regime where teaching
   examples live.
2. **Averaging material properties arithmetically.** The measured
   $+2.804\,\%$ flux error above is a *structural* error that refinement does not
   remove.
3. **Reporting a discrete norm as a physical quantity.** Section 3.4 shows the
   $0.186\,h^{2}$ bias of a perfectly correct grid-function norm.
4. **Assuming that "second order" means "small".** The constant matters: $h^{2}$
   with $h = 4$ m is not small until the constant is known.
5. **Sizing a run by time alone.** At high resolution 3-D models are memory
   bound; counting DOF first is the cheapest experiment available.
6. **Treating $h$ as a free parameter.** $h$ is set by the shortest feature you
   claim to resolve; after that it is a constraint, not a choice.

## Related modules

- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](02-convergence-and-error.md) —
  what happens to the errors introduced here under refinement.
- [19-02-01 Deriving Finite-Difference Operators via Taylor Expansion](../02-finite-difference-methods/01-fd-derivation.md) —
  the stencils that live on these grids.
- [01-12-02 Interpolation, Splines and Approximation Theory](../../01-mathematics/12-numerical-methods/02-interpolation.md) —
  interpolation error as the origin of discretisation error.
- [18-01-04 Discretisation, Parameterisation and Model Choice](../../18-inverse-problems/01-inverse-problem-foundations/04-discretisation-reality.md) —
  the same choices viewed from the inverse side.
- [Module 19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md).

Exercises and worked solutions:
[`exercises/01-discretisation-concepts-exercises.md`](exercises/01-discretisation-concepts-exercises.md)
and
[`exercises/01-discretisation-concepts-solutions.md`](exercises/01-discretisation-concepts-solutions.md).
