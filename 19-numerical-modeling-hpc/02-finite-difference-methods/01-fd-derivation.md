---
id: 19-02-01
title: "Deriving Finite-Difference Operators via Taylor Expansion"
level: advanced
prereqs: ["19-01-01", "19-01-02", "01-12-03"]
tags: [numerical-modelling, hpc, finite-difference, taylor-expansion, stencils, truncation-error]
---

# Deriving Finite-Difference Operators via Taylor Expansion

Every finite-difference stencil is the solution of a small linear system: the
*moment equations* that force the combination of neighbouring values to reproduce
a derivative. Once you can write that system you no longer need to remember
stencil tables, you can derive the operator you need for a non-uniform grid, a
boundary, or a staggered layout — and you can state its order before running
anything. This lesson derives operators from the moment equations, verifies the
exact truncation constants, and shows what one misplaced node costs. **All
models and data in this module are SYNTHETIC.** Every number quoted here is
printed by `code/fd_derivation_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the weights of a finite-difference stencil by solving the moment
   equations $\sum_i w_i \xi_i^{m} = m!\,\delta_{m,d}$ for a chosen node set.
2. **Determine** the order of a stencil as the index of the first moment that
   does not vanish, and **compute** the constant that multiplies $h^{p}$.
3. **Verify** a stencil by polynomial exactness: degree $\le p$ reproduced to
   round-off, degree $p+1$ left over with a measurable coefficient.
4. **Measure** the convergence order of one-sided, centred and fourth-order
   operators on a smooth function and **compare** with the Taylor prediction.
5. **Derive** a stencil for non-uniformly spaced nodes and **explain** why a
   uniform stencil applied to non-uniform nodes is not merely low order but
   inconsistent.
6. **Quantify** the error introduced by a grid-position error of a given
   fraction of $h$.

## Prerequisites

- [19-01-01 Discretisation: Grids, Nodes, Cells and Degrees of Freedom](../01-numerical-foundations/01-discretisation-concepts.md) —
  nodes, cells and degrees of freedom.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md) —
  truncation error and its measured order.
- [01-12-03 Numerical Differentiation and Finite-Difference Stencils](../../01-mathematics/12-numerical-methods/03-numerical-differentiation.md) —
  the same stencils in the mathematical-methods setting.

## 1. Intuition: a stencil is a small moment problem

Ask a combination $\sum_i w_i\,f(x+\xi_i h)$ to reproduce $f^{(d)}(x)$. Taylor
expand each term:

$$\sum_i w_i f(x+\xi_i h)
= \sum_{m\ge0}\frac{h^{m} f^{(m)}(x)}{m!}\sum_i w_i \xi_i^{m}.$$

The combination reproduces $f^{(d)}$ if the inner sums satisfy

$$\sum_i w_i\,\xi_i^{m} =
\begin{cases}
d! & m = d,\\
0   & m \ne d \ \text{for}\ m < n,
\end{cases}$$

where $n$ is the number of nodes. That is $n$ linear equations in $n$ unknowns —
a Vandermonde system — and it is solved once, symbolically or numerically, for
every stencil you will ever need. The *first* moment that cannot be forced to
zero, at $m = p+d$, sets the order $p$ and gives the leading error

$$\tau = \frac{h^{p}}{p!}\left(\frac{1}{d!}\sum_i w_i\xi_i^{p+d}\right)f^{(p+d)}(x)
\;\Longrightarrow\;
\frac{\tau}{h^{p}} = \frac{1}{p!}\sum_i w_i\xi_i^{p+d}\cdot\frac{f^{(p+d)}(x)}{d!}.$$

With $d$-derivative scaling the constant quoted in the tables below is
$C_p = \sum_i w_i\xi_i^{p+d}/(p+d)!$ times $(p+d)!/d!$; the demonstration reports
the raw moment divided by the factorial that makes the comparison with
$f^{(p)}(x)$ direct, and the measured numbers do the same.

## 2. Precise definitions

**Offsets $\xi_i$.** Node positions in units of $h$, measured from the point
where the derivative is wanted. A centred stencil has $\xi_i$ symmetric about
zero; a one-sided stencil has all $\xi_i \ge 0$ (or all $\le 0$).

**Order of accuracy.** The largest $p$ such that the stencil reproduces every
polynomial of degree $\le d+p-1$ exactly. Equivalently, the first non-vanishing
moment minus $d$.

**Consistency.** A stencil is consistent if the residual $\to 0$ as $h\to0$. A
set of weights derived for one node geometry and applied to another need not be
consistent at all (see §3.5).

## 3. Derivations

### 3.1 The standard stencils, derived rather than recalled

Solving the moment equations for the usual node sets gives the following
weights (all for a first-derivative operator unless marked; multiply by
$h^{-d}$):

| stencil | offsets | weights (× $h^{d}$) | order | $h^{p}$ coefficient |
|---|---|---|---|---|
| forward $u'$ | $0,1$ | $-1, +1$ | 1 | $+0.50000000$ |
| backward $u'$ | $-1,0$ | $-1, +1$ | 1 | $-0.50000000$ |
| central $u'$ | $-1,0,1$ | $-0.5, 0, +0.5$ | 2 | $+0.16666667$ |
| one-sided $u'$ | $0,1,2$ | $-1.5, +2, -0.5$ | 2 | $-0.33333333$ |
| central $u'$ | $-2..2$ | $+1/12, -2/3, 0, +2/3, -1/12$ | 4 | $-0.03333333$ |
| central $u'$ | $-3..3$ | $-1/60, +3/20, -3/4, 0,\dots$ | 6 | $+0.00714286$ |
| central $u''$ | $-1,0,1$ | $+1, -2, +1$ | 2 | $+0.08333333$ |
| central $u''$ | $-2..2$ | $-1/12, +4/3, -5/2, +4/3, -1/12$ | 4 | $-0.01111111$ |
| non-uniform $u'$ | $-1, 0.3, 1.7$ | $-0.569801, +0.384615, +0.185185$ | 2 | $+0.24833333$ |

The known constants appear as arithmetic: $1/6$, $-1/3$, $-1/30$, $1/12$,
$-1/90$ and $1/140$. The three-node one-sided formula is *second* order, which
is why a Neumann boundary condition implemented with three points does not drop
the global order (see
[19-02-03](03-fd-boundary-conditions.md)); the two-point one-sided formula does.

The non-uniform row deserves attention: with nodes at $-1$, $0.3$ and $1.7$ the
solution is still order two, because the moment equations were posed for those
positions. The offsets are no longer symmetric, so the weights are not, but
third-order moments vanish just as they would on a uniform grid. **Non-uniform
grids do not lose order; assuming uniformity on a non-uniform grid does.**

### 3.2 Polynomial exactness as a verification test

Apply the centred three-point first-derivative stencil to monomials at
$x = 0.7$ with $h = 0.1$:

| monomial | stencil value | exact derivative | difference |
|---|---|---|---|
| $x^{1}$ | 1.000000000000 | 1.000000000000 | $-2.220\times10^{-16}$ |
| $x^{2}$ | 1.400000000000 | 1.400000000000 | $-4.441\times10^{-16}$ |
| $x^{3}$ | 1.480000000000 | 1.470000000000 | $+1.000\times10^{-2}$ |
| $x^{4}$ | 1.400000000000 | 1.372000000000 | $+2.800\times10^{-2}$ |

Degree $\le 2$ is exact to round-off; degree 3 leaves a residual. Since the
first surviving moment of this stencil is at $m = 3$ with value $1$, the
predicted residual for $x^{3}$ is $h^{2}\cdot f'''/6 = h^{2}\cdot1$, and the
measurement reproduces it for three decades of $h$:

| $h$ | residual | residual$/h^{2}$ |
|---|---|---|
| 0.100 | $+1.0000000000\times10^{-2}$ | $+1.00000000$ |
| 0.010 | $+9.9999999999\times10^{-5}$ | $+1.00000000$ |
| 0.001 | $+9.9999999881\times10^{-7}$ | $+1.00000000$ |

This test is the fastest way to catch a transcription error in a stencil table:
a wrong weight breaks polynomial exactness immediately, whereas a convergence
study on a smooth function takes many runs and can hide the fault behind the
round-off floor.

### 3.3 Measured orders and constants on a smooth function

On $f = \sin$ at $x_0 = 0.3$ rad, with $h$ halved twice:

| stencil | $h = 0.1$ | $h = 0.05$ | $h = 0.025$ | order | exact coefficient | measured err$/h^{p}$ |
|---|---|---|---|---|---|---|
| forward $u'$ | $1.635513\times10^{-2}$ | $7.784473\times10^{-3}$ | $3.793321\times10^{-3}$ | 1.0711 | $-0.14776010$ | $0.15173285$ |
| central $u'$ | $1.591432\times10^{-3}$ | $3.980071\times10^{-4}$ | $9.951111\times10^{-5}$ | 1.9995 | $-0.15922275$ | $0.15921777$ |
| central 5-pt $u'$ | $3.180666\times10^{-6}$ | $1.989692\times10^{-7}$ | $1.243835\times10^{-8}$ | 3.9987 | $-0.03184455$ | $0.03184217$ |
| central $u''$ | $2.461848\times10^{-4}$ | $6.156158\times10^{-5}$ | $1.539136\times10^{-5}$ | 1.9996 | $0.02462668$ | $0.02462617$ |
| one-sided $u'$ | $3.099564\times10^{-3}$ | $7.861862\times10^{-4}$ | $1.978306\times10^{-4}$ | 1.9791 | $0.31844550$ | $0.31652903$ |

The central stencils agree with their predicted constants to five or six figures;
the one-sided and forward stencils are still approaching theirs, which is the
signature of a next term of the same order in the error (the forward stencil's
$O(h^{2})$ term is a fixed fraction of its $O(h)$ term, not a smaller power of
$h$). The measured order from three grids is $1.0711$ for a first-order stencil:
**three grids of a first-order scheme do not give exactly one**, and reporting
"order 1.07" is more honest than rounding to one.

### 3.4 A grid-position error is not a small error

Suppose the right-hand node of the centred three-point stencil actually sits at
$(1+\delta)h$ with $\delta = 0.1$, but the weights were derived for a uniform
grid. Then

$$\sum_i w_i = 0 \ \text{ fails}, \qquad
\text{average error} \to \frac{\delta}{2}f'(x_0) = 0.04776682,$$

a constant that does **not** vanish with $h$. The demonstration measures

| $h$ | error | ratio to previous |
|---|---|---|
| 0.1000 | $4.43634968\times10^{-2}$ | — |
| 0.0500 | $4.65275707\times10^{-2}$ | 0.953488 |
| 0.0250 | $4.72630191\times10^{-2}$ | 0.984439 |
| 0.0125 | $4.75438992\times10^{-2}$ | 0.994092 |

The error marches towards $0.04776682$ and stops. The scheme is *inconsistent*:
no amount of refinement recovers the derivative. If instead the weights are
solved for the true node positions $[-1, 0, 1.1]$, the scheme is consistent and
second order:

| $h$ | error | order | error$/h^{2}$ |
|---|---|---|---|
| 0.1000 | $-1.74912496\times10^{-3}$ | — | $-0.17491250$ |
| 0.0500 | $-4.37632531\times10^{-4}$ | 1.9988 | $-0.17505301$ |
| 0.0250 | $-1.09440680\times10^{-4}$ | 1.9996 | $-0.17510509$ |
| 0.0125 | $-2.73635271\times10^{-5}$ | 1.9998 | $-0.17512657$ |

against the predicted $c_3 f''' = -0.17514502$ with $c_3 = 1.1$. The contrast is
the lesson: the same geometry, two derivations, one usable scheme and one not.

## 4. Worked example: a first-derivative stencil for a stretched boundary layer

*A model needs $u'$ at the first node of a grid whose first three nodes are at
$x = 0$, $0.2h$ and $1.5h$ (a stretched boundary layer), to second order.*

1. Offsets from the evaluation point ($x_0$, the first node): $\xi = [0, 0.2, 1.5]$
   in units of $h$.
2. Moment equations: $w_1 + w_2 + w_3 = 0$; $0.2w_2 + 1.5w_3 = 1$;
   $0.04w_2 + 2.25w_3 = 0$.
3. Solve: from the third equation $w_2 = -56.25w_3$; substituting into the
   second, $0.2(-56.25w_3) + 1.5w_3 = 1$ gives
   $w_3 = 1/(-11.25 + 1.5) = -0.10256410$, hence $w_2 = 5.76923077$ and
   $w_1 = -(w_2+w_3) = -5.66666667$.
4. Order check: the first unforced moment is $m = 3$,
   $\sum w_i\xi_i^{3} = 5.76923077(0.008) - 0.10256410(3.375) = 0.04615385 -
   0.34615385 = -0.30000000$, so the error is $C h^{2}u'''$ with
   $C = -0.3/6 = -0.05$. To second order, as requested — with a constant three
   times smaller than the uniform three-point stencil's $1/6 \approx 0.167$,
   which is the usual reason stretching is used. (Verified numerically during
   preparation: the weights are $-5.66666667$, $+5.76923077$, $-0.10256410$, and
   the measured error$/h^{2}$ on $\sin$ at $x = 0.7$ walks from $0.03682$ to
   $0.03790$ towards the predicted $0.03824$.)
5. Verify by polynomial exactness as in §3.2 before using it in a solver.

## 5. Assumptions and regime of validity

1. **The function is smooth enough.** The moment argument needs $f$ to have
   $p+d$ derivatives at $x_0$. At a discontinuity the expansion fails and the
   order claimed is meaningless.
2. **The offsets are known exactly.** §3.4 quantifies the alternative; a grid
   generated from a coordinate transform is only as accurate as that transform.
3. **$h$ uniform in the expansion.** Non-uniform stencils are built by supplying
   the actual offsets, not by expanding about a nominal $h$.
4. **No round-off argument.** The moment analysis is exact arithmetic; in
   practice a stencil of order $p$ has a round-off floor that grows with the
   stencil width (see [19-02-02](02-fd-stencils.md)).
5. **One-sided stencils are less accurate for the same order.** The constants
   differ ($-1/3$ against $+1/6$ for the second-order first derivative), so
   boundary rows contribute an error several times larger than interior ones.
6. **The system must be well conditioned.** Nearly coincident nodes make the
   Vandermonde system ill-conditioned and the weights huge; a stretched grid
   with a ratio above about ten is a warning sign.

## 6. Python demonstration

`code/fd_derivation_demo.py` prints:

1. the weights, order and leading constant of nine stencils, solved from the
   moment equations;
2. the polynomial-exactness test, including the exact residual $h^{2}f'''/6$
   for $x^{3}$ over three decades of $h$;
3. measured convergence orders and error constants for five operators on
   $\sin$;
4. the misplaced-node experiment, in both the inconsistent and the
   re-derived consistent versions.

```bash
cd 19-numerical-modeling-hpc/02-finite-difference-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_derivation_demo.py
```

## Mastery checkpoint

Without notes:

> Derive a first-derivative stencil at the last node of a grid, using the three
> nodes at offsets $-2h$, $-h$ and $0$. **(a)** Write the three moment equations
> and solve for the weights. **(b)** State the order and compute the leading
> error constant in the form $C\,h^{2}f'''$. **(c)** Show by applying the stencil
> to $x^{3}$ that the constant is right. **(d)** Explain why a stencil derived
> for uniform nodes cannot be used at the first node of a stretched grid, with
> the size of the resulting error for a 10 % stretch.

The weights and constants are worked in
[`exercises/01-fd-derivation-solutions.md`](exercises/01-fd-derivation-solutions.md).

## Common pitfalls

1. **Recalling stencils instead of deriving them.** The moment equations take
   ten lines and work for any node set.
2. **Assuming the order is the number of nodes minus the derivative order.**
   True for distinct nodes, false as soon as the moment system is singular (for
   example two nodes at the same offset).
3. **Applying a uniform stencil to a stretched grid.** §3.4: the error does not
   vanish under refinement.
4. **Trusting a stencil proven only on smooth data.** Verify with polynomial
   exactness and the measured order before use.
5. **Ignoring the one-sided constants.** Boundary rows carry several times the
   interior truncation error, which is why stencils are re-derived for
   boundaries rather than borrowed.
6. **Assuming more nodes mean more accuracy.** Width increases the round-off
   floor even as it lowers the truncation term.

## Related modules

- [19-02-02 High-Order and Compact Stencils; Staggered Grids](02-fd-stencils.md) —
  what happens when the stencil is made wide, compact or staggered.
- [19-02-03 Boundary Conditions: Dirichlet, Neumann, Absorbing, PML](03-fd-boundary-conditions.md) —
  one-sided stencils where they matter most.
- [01-12-03 Numerical Differentiation and Finite-Difference Stencils](../../01-mathematics/12-numerical-methods/03-numerical-differentiation.md).
- [03-02-08 Replacing Loops: Vectorisation Patterns and Traps](../../03-scientific-computing/02-numpy/08-vectorisation-patterns.md) —
  implementing these operators efficiently.
- [Module 19-02 Finite-Difference Methods](README.md).

Exercises and worked solutions:
[`exercises/01-fd-derivation-exercises.md`](exercises/01-fd-derivation-exercises.md)
and
[`exercises/01-fd-derivation-solutions.md`](exercises/01-fd-derivation-solutions.md).
