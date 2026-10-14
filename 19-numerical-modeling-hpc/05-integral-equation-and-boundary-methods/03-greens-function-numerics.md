---
id: 19-05-03
title: "Numerical Green's Functions and Their Computation"
level: research
prereqs: ["19-05-01", "19-01-02", "19-02-06"]
tags: [numerical-modelling, hpc, green-functions, poisson-solver, spectral-methods, singularity]
---

# Numerical Green's Functions and Their Computation

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the one-dimensional Dirichlet Green's function from the discrete
   operator and explain why the discrete solution is exact for this operator.
2. **Show**, by measurement, how the representation of the singular source — at a
   node, distributed linearly, or lumped to the nearest node — decides whether the
   error is roundoff or first order.
3. **Compute** a screened Green's function on a periodic grid two independent
   ways and check that they agree to roundoff.
4. **Measure** the lattice-versus-continuum error of the screened kernel and
   identify the regime in which periodic images, not the grid, dominate.
5. **Quantify** the additive constant of a 2-D Laplace Green's function and show
   how it depends on the domain size.
6. **State** which comparison is meaningful near a singularity and which is not.

## Prerequisites

- [19-05-01 Volume and Surface Integral Equations](01-integral-equations.md) —
  the Green's function as the kernel of an integral representation.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md) —
  the only evidence of order used here is a measured table.
- [19-02-06 FD for Diffusion, Laplace and Poisson Problems](../02-finite-difference-methods/06-fd-diffusion-and-potential.md) —
  the discrete operators whose inverse is computed.

All models and data in this module are **SYNTHETIC**: the domains, grid spacings
and screen parameters are chosen teaching values, and the "reference" is always
either an exact closed form or a second, independent discretisation.

## 1. Why a Green's function is not free

The Green's function of an operator is the field of a unit point source. It is
the kernel of every integral representation in
[01 Volume and Surface Integral Equations](01-integral-equations.md), and in
practice it is almost never the free-space formula. Three things force a
numerical construction:

- **the medium is not free space** — layering, screening, anisotropy;
- **the domain is bounded or periodic** — the kernel then depends on the box;
- **the operator is not Laplace's** — elastic, electromagnetic and diffusive
  operators each have their own kernel, and several have no closed form.

This lesson builds kernels the way a code does, by inverting the **discrete**
operator, and then asks the only question worth asking: what is the relation
between the discrete kernel and the continuous one, and where does that relation
break down?

## 2. The one-dimensional case, solved exactly

On $0<x<1$ with $u(0) = u(1) = 0$, the Green's function of $-u''$ is the tent
function

$$G(x;x_0) = \frac{x_{<}(L - x_{>})}{L}, \qquad L = 1 .$$

Evaluate it at the nodes $x_i = ih$, $i = 1,\dots,n$, $h = 1/(n+1)$. The second
difference of the tent at the source node is
$(G_{i_0+1} - 2G_{i_0} + G_{i_0-1}) = -h$, so

$$-\frac{G_{i_0+1} - 2G_{i_0} + G_{i_0-1}}{h^{2}} = \frac{1}{h},$$

which is exactly the discrete equation for a unit source. The consequence is a
statement worth pausing on: **the discrete solution is the continuum solution**,
at every node, for this operator and this source placement.

Measured, with the source at a node and $n$ interior nodes:

| $n$ | $\max|G_{\text{discrete}}-G_{\text{analytic}}|$ |
|---|---|
| 15 | $2.776\times10^{-17}$ |
| 31 | $6.106\times10^{-16}$ |
| 63 | $1.971\times10^{-15}$ |
| 127 | $1.499\times10^{-15}$ |

The residual is roundoff, and it grows with the size of the tridiagonal solve
because more arithmetic is performed; it is not a discretisation error. A second,
independent solve (a dense $\mathtt{numpy.linalg.solve}$ on the same system)
agrees with the banded solve to $5.551\times10^{-17}$.

**Why is this not the general case?** Because the exact kernel happens to lie in
the discrete space. For the 1-D Laplace operator the space of functions that are
linear between nodes is closed under the operator, and the tent is in it. Change
the operator — add a screen, use a different stencil, go to 2-D — and the exact
kernel is no longer representable, and an $O(h^{2})$ error appears.

## 3. Representing a point source: three placements, three behaviours

An important practical question is how the delta function enters the right-hand
side. Take $x_0 = 0.5$ with an even $n$, so the source falls **between** nodes,
and compare:

| $n$ | $h$ | linear (hat) distribution | lumped on nearest node | lumped error$/h$ |
|---|---|---|---|---|
| 8 | 1/9 | $4.163\times10^{-17}$ | $2.469\times10^{-2}$ | 0.2222 |
| 32 | 1/33 | $6.661\times10^{-16}$ | $7.346\times10^{-3}$ | 0.2424 |
| 128 | 1/129 | $3.358\times10^{-15}$ | $1.923\times10^{-3}$ | 0.2481 |
| 512 | 1/513 | $9.770\times10^{-15}$ | $4.864\times10^{-4}$ | 0.2495 |

- **Linear (hat) distribution** — putting the mass $(1-w)/h$ on the node below
  and $w/h$ on the node above, with $w$ the fractional offset — reproduces the
  analytic tent to roundoff. The discrete source is the exact weak form of the
  delta for this operator.
- **Lumping** all the mass onto the nearest node costs a **first-order** error of
  about $0.25\,h$, and the ratio column shows it converging to a constant. This
  is a *modelling* error, not a solver error, and it is invisible in a residual
  check: the lumped system is solved exactly, it just solves a slightly different
  problem.

The lesson transfers directly to 2-D and 3-D codes: how a point source is
inserted into a grid decides the accuracy of the kernel, and the fix is a
consistent (integrated) source, not a finer grid.

## 4. A screened kernel on a periodic grid, two independent routes

Now take the operator $\nabla^{2} - \kappa^{2}$ on an $n\times n$ periodic grid
with spacing $h$ and invert it for a unit source carrying the cell mass
$1/h^{2}$. The FFT route uses the **exact symbol of the five-point stencil**,

$$\lambda(\mathbf{k}) = \frac{2}{h^{2}}\left(2 - \cos k_x h -
\cos k_y h\right) + \kappa^{2}, \qquad \hat{G} = 1/\lambda,$$

so the FFT result is the exact inverse of the same matrix a sparse direct solve
would invert. Measured, a box of $L = 64$ km, $\kappa = 1\ \mathrm{km^{-1}}$:

| $n$ | $\max|G_{\text{fft}} - G_{\text{sparse}}|$ | $\max|G|$ |
|---|---|---|
| 64 | $5.551\times10^{-17}$ | $2.540\times10^{-1}$ |
| 128 | $1.388\times10^{-16}$ | $3.769\times10^{-1}$ |
| 256 | $3.331\times10^{-16}$ | $4.932\times10^{-1}$ |

Two entirely different algorithms, agreeing to roundoff, which is what a solver
cross-check should look like.

### 4.1 Lattice against continuum, at fixed physical distance

The continuum kernel of $\nabla^{2}-\kappa^{2}$ in **two** dimensions is
$K_{0}(\kappa r)/(2\pi)$ — the modified Bessel function, not the 3-D
$\mathrm{e}^{-\kappa r}/(4\pi r)$, and the difference is a common and expensive
mistake. Since only *differences* of the kernel are physically measured, compare
$G_{\text{lat}}(r_1) - G_{\text{lat}}(r_2)$ with the continuum difference at
$r_1 = 8$ km and $r_2 = 24$ km:

| $n$ | $h$ (km) | lattice difference | $K_0$ difference | relative error | order |
|---|---|---|---|---|---|
| 64 | 1.0000 | $3.02551942\times10^{-5}$ | $2.33115352\times10^{-5}$ | $2.979\times10^{-1}$ | — |
| 128 | 0.5000 | $2.49723339\times10^{-5}$ | $2.33115352\times10^{-5}$ | $7.124\times10^{-2}$ | 2.06 |
| 256 | 0.2500 | $2.37226941\times10^{-5}$ | $2.33115352\times10^{-5}$ | $1.764\times10^{-2}$ | 2.01 |
| 512 | 0.1250 | $2.34140785\times10^{-5}$ | $2.33115352\times10^{-5}$ | $4.399\times10^{-3}$ | 2.00 |

The error falls by four for each halving of $h$: second order, the order of the
five-point Laplacian itself. Working with differences is what makes this possible
— the kernel's additive constant, which is large and grid-dependent (Section 5),
cancels.

### 4.2 Which error dominates depends on $\kappa L$

Compare the lattice value at $r = 8$ km with two models, at $n = 256$:

| $\kappa$ ($\mathrm{km^{-1}}$) | $\kappa L$ | lattice value | error vs single kernel | error vs 7×7 image sum |
|---|---|---|---|---|
| 1.00 | 64.0 | $2.37226957\times10^{-5}$ | $1.764\times10^{-2}$ | $1.764\times10^{-2}$ |
| 0.05 | 3.2 | $2.00897196\times10^{-1}$ | $1.326\times10^{-1}$ | $5.994\times10^{-5}$ |

At $\kappa L = 64$ the images are suppressed by $\mathrm{e}^{-32}$ and the only
error left is the $O(h^{2})$ discretisation. At $\kappa L = 3.2$ the single
kernel is wrong by $13\%$ and a $7\times7$ sum over images explains the value to
$6\times10^{-5}$. **A kernel on a periodic grid is a sum over images; whether the
images matter is a question of $\kappa L$, not of grid spacing.** This is the
quantitative form of the sentence "the Green's function depends on the domain".

## 5. The 2-D Laplace kernel and its additive constant

Set $\kappa = 0$. The $\mathbf{k} = 0$ mode of the symbol vanishes, the system is
singular, and the solution is fixed only up to a constant. Removing that mode
(equivalently, requiring the kernel to have zero mean) fixes the constant — and
the constant is then a property of the box.

Close to the source, $r \ll L$, the free-space logarithm is the right comparison.
With distances fixed in **cells** (so the source stays resolved as $h\to0$):

| $n$ | $h$ | $G(8h) - G(32h)$ | $-\frac{1}{2\pi}\ln\frac{1}{4}$ | relative error | order |
|---|---|---|---|---|---|
| 64 | 1.0000 | $0.15409015$ | $0.22063560$ | $3.016\times10^{-1}$ | — |
| 256 | 0.2500 | $0.21714498$ | $0.22063560$ | $1.582\times10^{-2}$ | 2.10 |
| 512 | 0.1250 | $0.21992013$ | $0.22063560$ | $3.243\times10^{-3}$ | 2.29 |
| 1024 | 0.0625 | $0.22060856$ | $0.22063560$ | $1.226\times10^{-4}$ | 4.73 |

At fixed **physical** distances comparable with the box, however, refining does
**not** help:

| $n$ | $h$ | $G(8\,\text{km}) - G(24\,\text{km})$ | $-\frac{1}{2\pi}\ln\frac{1}{3}$ | relative error | order |
|---|---|---|---|---|---|
| 64 | 1.0000 | $0.14130916$ | $0.17484958$ | $1.918\times10^{-1}$ | — |
| 1024 | 0.0625 | $0.14111790$ | $0.17484958$ | $1.929\times10^{-1}$ | $-0.00$ |

The error is pinned at $19.3\%$: the 2-D Laplace field does not decay, so every
periodic image contributes, and the free-space logarithm is simply the wrong
model at $r \sim L/3$. That is not a discretisation error and no refinement
removes it.

**The additive constant, measured.** With the zero mode removed,
$G(1\ \mathrm{km})$ for boxes of increasing size:

| $L$ (km) | $G(1\ \mathrm{km})$ | increment per doubling | $\frac{1}{2\pi}\ln 2$ |
|---|---|---|---|
| 16 | $0.233675$ | — | 0.11032 |
| 32 | $0.343268$ | $0.10959$ | 0.11032 |
| 64 | $0.453442$ | $0.11017$ | 0.11032 |
| 128 | $0.563877$ | $0.11043$ | 0.11032 |

The increment converges to $\frac{1}{2\pi}\ln 2 = 0.110318$, which identifies the
constant as containing $-\frac{1}{2\pi}\ln L$. A 2-D Laplace Green's function on
a bounded or periodic domain is defined only **relative to a reference length**;
a potential from a net-zero source distribution is unaffected, a single-source
potential is not.

## 6. Assumptions and regime of validity

1. **Two dimensions, constant coefficients.** The log kernel, $K_0$ and the
   $\ln L$ constant are 2-D statements. In 3-D the screened kernel is
   $\mathrm{e}^{-\kappa r}/(4\pi r)$ and the sum over images decays as
   $1/r$ rather than logarithmically.
2. **The symbol equals the stencil.** The FFT route is the exact inverse of the
   five-point matrix only because the symbol in Section 4 is the stencil's
   symbol. Using the continuum $k^{2}$ in place of
   $\frac{2}{h^{2}}(2-\cos k_xh-\cos k_yh)$ gives a different operator, and the
   "cross-check" would fail for a real reason.
3. **Source mass $1/h^{2}$.** The discrete source represents a cell mass, not a
   unit point value. Getting this wrong scales the whole kernel by $h^{2}$ and
   produces a convergence study that appears to have order $2$ for the wrong
   reason.
4. **Periodic images.** The kernel is the image sum. It is usable as a
   free-space kernel only when $\kappa L$ is large; the boundary in the measured
   table is around $\kappa L \gtrsim 10$ for $1\%$ accuracy.
5. **Away from the source.** Pointwise comparison near $r = 0$ is meaningless for
   a discrete kernel; only cell-averaged (integrated) quantities converge.
   Section 3 showed the size of the effect for a lumped source.
6. **A fixed convention for the singular mode.** With $\kappa = 0$ the constant
   must be fixed by a convention that is stated, because every absolute value
   depends on it.

## 7. A fully worked example

Take the 1-D problem with $n = 32$ interior nodes, $h = 1/33$, and the source at
$x_0 = 0.5$, which falls between the nodes $x_{16} = 16/33 = 0.48485$ and
$x_{17} = 17/33 = 0.51515$.

- The fractional offset is $w = (0.5 - 0.48485)/h = 0.5$, so the **linear**
  distribution puts $(1-w)/h = 0.5/h$ on the lower node and $0.5/h$ on the upper.
- The analytic value at the source location is
  $G(0.5;0.5) = 0.5(1-0.5)/1 = 0.25$.
- Measured error of the linear distribution: $6.661\times10^{-16}$, which is
  $0.0000000000000006661$ — roundoff, and nothing else.
- Measured error of the lumped distribution: $7.346\times10^{-3}$, which is
  $0.2424\,h$ with $h = 1/33 = 0.030303$. A $0.7\%$ error in a kernel that will
  be multiplied by source strengths and summed over thousands of cells is not a
  small error, and it does not shrink at second order.

The two errors differ by thirteen orders of magnitude, they come from the same
operator, and the only difference is where the delta was put.

## 8. Python demonstration

`code/greens_function_numerics_demo.py` measures everything quoted above: the
1-D exactness and the three source placements, the FFT-versus-sparse
cross-checks, the lattice-versus-continuum orders, the image-dominated regime,
the Laplace zero mode, and the box-dependent constant against $\frac{1}{2\pi}\ln2$.

```bash
cd 19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python greens_function_numerics_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-greens-function-numerics-exercises.md`](./exercises/03-greens-function-numerics-exercises.md)
and [`exercises/03-greens-function-numerics-solutions.md`](./exercises/03-greens-function-numerics-solutions.md).

- **★** Evaluate the tent function at $n = 4$ nodes for $x_0 = 0.5$ and show that
  it satisfies the discrete equation with source $1/h$.
- **★** Compute $G_{ii}$-style self terms: $\int_0^L \ln|t - L/2|\,\mathrm{d}t$
  for $L = 1$ and check the sign.
- **★★** Show from the lumped-source table that the error is $0.25h$ and explain
  where the factor comes from.
- **★★** For $\kappa = 0.05\ \mathrm{km^{-1}}$ and $L = 64$ km, estimate how many
  image terms are needed for $1\%$ accuracy and check it against the measured
  image-sum error.
- **★★★** Design a test that distinguishes an error caused by a wrong source
  mass from one caused by a wrong symbol, using only refinement tables.

## Mastery checkpoint

Without notes:

> A screened kernel is computed on a periodic $256^{2}$ grid with
> $L = 64$ km and $\kappa = 1\ \mathrm{km^{-1}}$, and the FFT value at $r = 8$ km
> is compared with $K_0(\kappa r)/(2\pi)$ and with a $7\times7$ image sum.
> **(a)** State which comparison is meaningful here and what the measured error
> is in each case. **(b)** State what happens to both errors if $\kappa$ is
> reduced to $0.05\ \mathrm{km^{-1}}$ and why. **(c)** Explain why the additive
> constant of the kernel never appears in these comparisons, and what it does
> depend on.

A worked version appears in the lesson-03
[solutions](./exercises/03-greens-function-numerics-solutions.md).

## Common pitfalls

1. **Using the 3-D Yukawa kernel in 2-D.** The 2-D screened kernel is
   $K_0(\kappa r)/(2\pi)$; the error this makes is not small and not a
   discretisation error.
2. **Forgetting the cell mass.** A discrete source of unit value rather than
   $1/h^{2}$ scales the kernel by $h^{2}$, which makes refinement studies look
   well-behaved while the kernel is wrong by orders of magnitude.
3. **Comparing point values near the source.** The discrete kernel is finite
   where the continuum kernel diverges; only differences and cell averages
   converge.
4. **Assuming images are negligible.** For a weakly screened or unscreened
   operator they are not, and the free-space kernel is then the wrong model
   rather than an inaccurate one.
5. **Refining when the error is a domain effect.** The $19.3\%$ error at
   $r \sim L/3$ does not move with $h$, and a refinement study that expects it to
   will conclude the wrong thing about the code.
6. **Leaving the singular mode to chance.** With $\kappa = 0$ the constant must
   be fixed deliberately and stated, or two implementations will disagree by a
   constant and neither will be wrong.

## Related modules

- [01 Volume and Surface Integral Equations](01-integral-equations.md) —
  the representation these kernels evaluate.
- [02 Boundary Element Methods for Potential Fields](02-boundary-element.md) —
  where the free-space kernel is assembled into a dense operator.
- [04 Fast Multipole and Hierarchical Acceleration](04-fast-multipole.md) —
  evaluating kernels of this kind in linear time.
- [19-04 Spectral and Pseudospectral Methods](../04-spectral-and-pseudospectral/README.md) —
  the FFT route used here, generalised.
- [19-08 Geophysical Simulation Case Studies](../08-geophysical-simulation-case-studies/README.md) —
  kernels used inside full simulations.
