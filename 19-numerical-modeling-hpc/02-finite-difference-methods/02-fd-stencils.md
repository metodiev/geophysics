---
id: 19-02-02
title: "High-Order and Compact Stencils; Staggered Grids"
level: doctoral
prereqs: ["19-02-01", "19-01-04", "03-02-07"]
tags: [numerical-modelling, hpc, high-order, compact-schemes, staggered-grids, dispersion]
---

# High-Order and Compact Stencils; Staggered Grids

Ten points per wavelength is not a law of nature; it is the price of a
second-order stencil. This lesson compares the three ways of paying less —
wider explicit stencils, compact (Padé) schemes that solve a narrow band system,
and staggered grids that place each unknown where it is differentiated — and
measures what each buys in resolving power, error constant and operator
bandwidth. **All models and data in this module are SYNTHETIC.** Every number
quoted here is printed by `code/fd_stencils_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Measure** the order of explicit central stencils of order 2, 4, 6 and 8 and
   **explain** why the highest-order stencil reaches the round-off floor first.
2. **Compute** the dispersion symbol of a stencil and **express** its resolution
   as the number of points per wavelength needed for a stated phase error.
3. **Derive** the two-point staggered derivative and **show** that its truncation
   coefficient is $h^{2}/24$ against $h^{2}/6$ for the centred stencil — a factor
   of four at equal order.
4. **Formulate** a compact scheme as a tridiagonal system, **solve** it, and
   **compare** its error and bandwidth with an explicit stencil of the same
   order.
5. **Quantify** the resolution-versus-width trade-off and **choose** a scheme for
   a stated accuracy target.
6. **Verify** the conservation property of a staggered leapfrog update by
   measuring the drift of the discrete energy over thousands of steps.

## Prerequisites

- [19-02-01 Deriving Finite-Difference Operators via Taylor Expansion](01-fd-derivation.md) —
  the moment equations used to derive every stencil here.
- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](../01-numerical-foundations/04-numerical-dispersion-diffusion.md) —
  the dispersion language used throughout.
- [03-02-07 Memory Layout, Strides and Cache-Aware Performance](../../03-scientific-computing/02-numpy/07-memory-performance.md) —
  why operator bandwidth is a performance quantity, not a formality.

## 1. Intuition: three currencies

Accuracy in a wave model can be bought with three currencies.

- **Width.** Use more nodes per derivative. Explicit stencils of order $2p$ use
  $2p+1$ nodes, all of which must be loaded from memory at every point.
- **Coupling.** Solve a small band system for the derivative at every node: a
  *compact* scheme. The stencil is narrow, the linear algebra is wider, and the
  resolution per node is much better.
- **Placement.** Store each field where it is needed instead of interpolating.
  A staggered grid differentiates velocity at the pressure node using the two
  adjacent velocities, giving second-order accuracy with two points and, for the
  leapfrog update, an exactly conserved discrete energy.

Each currency has a measurable exchange rate. This lesson measures all three.

## 2. Precise definitions

**Explicit central stencil of order $2p$.** Weights $w_i$ on nodes
$\xi = -p,\dots,p$ with the moment equations of
[19-02-01](01-fd-derivation.md) satisfied for $m \le 2p$ and $m$ odd below
$2p+1$.

**Dispersion symbol.** For a mode $e^{\mathrm ikx}$ the stencil returns
$\mathrm i k\,S(\theta)$ with $\theta = kh$ and

$$S(\theta) = \frac{1}{\theta}\sum_{i} w_i\sin(i\theta),\qquad
\text{p=2: } \frac{\sin\theta}{\theta},\qquad
\text{p=4: } \frac{8\sin\theta-\sin2\theta}{6\theta}.$$

$S = 1$ means the derivative is exact; $|1-S|$ is the relative phase error of
that mode.

**Staggered (cell-centred) derivative.** With $u$ known at cell centres and its
derivative wanted at the faces,
$g_{i+1/2} = (u_{i+1}-u_i)/h$, a two-point formula:

$$g_{i+1/2} = u'(x_{i+1/2}) + \frac{h^{2}}{24}u'''(x_{i+1/2}) + O(h^{4}),
\qquad S(\theta) = \frac{\sin(\theta/2)}{\theta/2}.$$

**Compact (Padé) scheme.** The derivative is defined implicitly,

$$\alpha\,g_{i-1} + g_i + \alpha\,g_{i+1}
= a\,\frac{u_{i+1}-u_{i-1}}{2h} + b\,\frac{u_{i+2}-u_{i-2}}{4h},$$

with $(\alpha,a,b) = (1/4, 3/2, 0)$ fourth order and
$(\alpha,a,b) = (1/3, 14/9, 1/9)$ sixth order. Its symbol is

$$S(\theta) = \frac{a\sin\theta + \tfrac{b}{2}\sin2\theta}
{\theta\left(1 + 2\alpha\cos\theta\right)}.$$

Solving for $g$ costs one tridiagonal (or pentadiagonal) solve per right-hand
side; on a periodic grid the matrix is circulant and $3n$ or $5n$ non-zeros.

## 3. Derivations

### 3.1 Explicit stencils: order and its floor

On a periodic grid of $n$ cells covering $[0,2\pi)$ the demonstration applies
each stencil to $\sin$ and halves $h$:

| order | $n = 100$ | $n = 200$ | $n = 400$ | $n = 800$ | observed order |
|---|---|---|---|---|---|
| 2 | $6.578438\times10^{-4}$ | $1.644853\times10^{-4}$ | $4.112284\times10^{-5}$ | $1.028081\times10^{-5}$ | 2.0000 |
| 4 | $5.192710\times10^{-7}$ | $3.246589\times10^{-8}$ | $2.029302\times10^{-9}$ | $1.268399\times10^{-10}$ | 3.9999 |
| 6 | $4.391573\times10^{-10}$ | $6.875056\times10^{-12}$ | $1.201261\times10^{-13}$ | $9.692247\times10^{-14}$ | 5.9972 → floor |
| 8 | $3.880229\times10^{-13}$ | $2.198242\times10^{-14}$ | $5.706546\times10^{-14}$ | $1.054712\times10^{-13}$ | 4.1417 → floor |

Each stencil reaches its design order until its error meets the round-off floor,
and the higher the order the sooner that happens: the sixth-order stencil is
already at the floor by $n = 400$, where its truncation error would be
$\sim10^{-16}$. The practical implication is that a high-order stencil is useful
only if the grid is coarse enough for its truncation term to sit above the
arithmetic noise of the *whole* computation.

### 3.2 Dispersion: the numbers behind "ten points per wavelength"

The symbol $S(\theta)$ for all seven schemes, with $\theta = 2\pi/\mathrm{PPW}$:

| PPW | p=2 | p=4 | p=6 | p=8 | staggered 2 | Padé 4 | Padé 6 |
|---|---|---|---|---|---|---|---|
| 4 | 0.6366198 | 0.8488264 | 0.9337090 | 0.9700873 | 0.9003163 | 0.9549297 | 0.9902974 |
| 6 | 0.8269933 | 0.9648256 | 0.9923920 | 0.9982991 | 0.9549297 | 0.9923920 | 0.9992836 |
| 8 | 0.9003163 | 0.9882152 | 0.9985132 | 0.9998058 | 0.9744954 | 0.9977253 | 0.9998797 |
| 16 | 0.9744954 | 0.9992217 | 0.9999746 | 0.9999991 | 0.9935869 | 0.9998654 | 0.9999982 |
| 32 | 0.9935869 | 0.9999507 | 0.9999996 | 1.0000000 | 0.9983944 | 0.9999917 | 1.0000000 |

At PPW $=8$ the second-order stencil has a $9.97\,\%$ phase error and the
staggered two-point stencil has $2.55\,\%$: the same nominal order, a factor
$3.908$ in error against the exact coefficient ratio

$$\frac{h^{2}/6}{h^{2}/24} = 4.000.$$

The residual (3.908 against 4.000) is the $O(\theta^{4})$ term, and the
demonstration prints both numbers side by side so that the asymptotic ratio is
never mistaken for an identity.

### 3.3 Resolving power and what it costs

Solving $|1-S| = 1\,\%$ for each scheme gives the points per wavelength needed
for a one-per-cent phase error, and multiplying by the stencil width gives a
crude work-per-wavelength proxy:

| scheme | PPW for 1 % | stencil width | PPW × width |
|---|---|---|---|
| explicit p=2 | 25.612 | 3 | 76.8 |
| explicit p=4 | 8.348 | 5 | 41.7 |
| explicit p=6 | 5.712 | 7 | 40.0 |
| explicit p=8 | 4.695 | 9 | 42.3 |
| staggered 2 | 12.806 | 2 | 25.6 |
| Padé 4 | 5.628 | 3 | 16.9 |
| Padé 6 | 3.982 | 5 | 19.9 |

Three readings of the same table. Explicit schemes above order four stop
improving their *total* work per wavelength, because the width grows as fast as
the resolution improves. Staggering halves the cost of a second-order scheme for
free. Compact schemes are the cheapest in this accounting, at the price of a
tridiagonal or pentadiagonal solve per right-hand side — a price that is
favourable on a cache-friendly band matrix and hostile on a GPU with many
independent right-hand sides.

### 3.4 The compact scheme, solved and measured

For the fourth-order family ($\alpha = 1/4$, $a = 3/2$) the demonstration solves
the circulant system on periodic grids with $\sin$ as the data:

| $n$ | $h$ | compact max error | observed order | explicit p=4 error |
|---|---|---|---|---|
| 128 | 0.049087 | $3.226501\times10^{-8}$ | — | $1.934790\times10^{-7}$ |
| 256 | 0.024544 | $2.016130\times10^{-9}$ | 4.0003 | $1.209504\times10^{-8}$ |
| 512 | 0.012272 | $1.260049\times10^{-10}$ | 4.0000 | $7.559839\times10^{-10}$ |
| 1024 | 0.006136 | $7.946532\times10^{-12}$ | 3.9870 | $4.729328\times10^{-11}$ |

Six times smaller error than the explicit five-point stencil at the same $h$,
with a tridiagonal matrix (3072 non-zeros at $n = 1024$) instead of the explicit
stencil's five diagonals (5120 non-zeros) — cheaper *and* more accurate here,
because the band solve replaces the wide stencil. The measured order is 4.0000
until round-off appears in the last row.

### 3.5 Staggered grids and a conserved energy

For the one-dimensional velocity–stress system
$v_t = -\tfrac1\rho p_x$, $p_t = -\rho c^{2}v_x$ the staggered leapfrog update

$$v_{i+1/2}^{n+1/2} = v_{i+1/2}^{n-1/2} - \frac{dt}{\rho h}\big(p_{i+1}^{n}-p_{i}^{n}\big),
\qquad
p_i^{n+1} = p_i^{n} - \frac{dt\,\rho c^{2}}{h}\big(v_{i+1/2}^{n+1/2}-v_{i-1/2}^{n+1/2}\big)$$

is the standard Virieux-style scheme: second order, two points per derivative,
and the discrete energy

$$E^{n+1/2} = \tfrac12\sum_i\left(\rho\,v_i^{2} + \frac{p_i^{2}}{\rho c^{2}}\right)$$

is conserved to round-off. The demonstration runs the equivalent second-order
wave equation, $u^{n+1} = 2u^{n}-u^{n-1}+C^{2}(u_{i+1}-2u_i+u_{i-1})$, for 5000
steps at $C = 0.5$ with 400 cells and tracks the discrete energy

$$E = \tfrac12\sum_i\left[\left(\frac{u^{n+1}_i-u^{n}_i}{dt}\right)^{2}
+ \left(\frac{u_{i+1}-u_i}{h}\right)^{2}\right]:$$

| step | relative change in $E$ |
|---|---|
| 0 | $0.000\times10^{0}$ |
| 1000 | $-2.341\times10^{-10}$ |
| 2000 | $-7.335\times10^{-12}$ |
| 3000 | $-2.268\times10^{-10}$ |
| 4000 | $-1.469\times10^{-11}$ |
| 5000 | $-2.195\times10^{-10}$ |

The drift is a round-off walk with no systematic direction, which is what
"symplectic" means operationally: the discrete quadratic form is invariant in
exact arithmetic. For contrast, a first-order scheme on the same grid does not
conserve energy at all — the upwind scheme of
[19-01-03](../01-numerical-foundations/03-consistency-stability.md) removes the
highest grid mode entirely in one step at $C = 1/2$.

## 4. Worked example: choosing a scheme for a 0.2 % phase-error target

*A 2-D acoustic survey tolerates a 0.2 % phase error and must run on the coarsest
grid that achieves it.*

1. For a second-order central stencil, $1 - S = \theta^{2}/6$ with
   $\theta = 2\pi/\mathrm{PPW}$, so $1-S = 6.58/\mathrm{PPW}^{2}$. PPW for a
   $0.2\,\%$ error: $\sqrt{6.58/0.002} = 57.4$.
2. For the fourth-order stencil $1-S = \theta^{4}/30$, i.e.
   $51.95/\mathrm{PPW}^{4}$, so PPW $= (51.95/0.002)^{1/4} = 12.7$. (Sanity
   check against the measured table: at PPW $=8$ the formula gives
   $51.95/4096 = 1.27\,\%$ against the measured $1.18\,\%$ — the $O(\theta^{6})$
   term is already visible at that resolution.)
3. Compact fourth-order: from its measured column, $1\,\%$ needs
   $5.628$ points, so $A = 0.01\times5.628^{4} = 10.0$ and
   PPW $= (10.0/0.002)^{1/4} = 8.4$.
4. Cost in two dimensions: at PPW $= 57.4$ a $1000\lambda$ domain needs
   $5.74\times10^{4}$ cells per direction, i.e. $3.3\times10^{9}$ unknowns,
   against $1.27\times10^{4}$ cells and $1.6\times10^{8}$ unknowns for the
   fourth-order stencil — a factor $20.4$ fewer, bought with a five-point
   stencil instead of a three-point one.
5. Verify with the measured dispersion table rather than trusting the fits: the
   fitted laws are asymptotic, and the compact scheme's fitted coefficient is
   not comparable with the explicit one at these resolutions.

## 5. Assumptions and regime of validity

1. **Periodic, uniform, constant-coefficient tests.** The symbols and the exact
   weight tables assume it; boundaries and variable coefficients need the
   boundary-row treatment of [19-02-03](03-fd-boundary-conditions.md).
2. **Round-off ignored, then acknowledged.** The order measurements are
   trustworthy only while truncation dominates; every table above says where it
   stops being true.
3. **The dispersion symbol describes plane waves.** A point source excites all
   directions, so the two-dimensional anisotropy of
   [19-01-04](../01-numerical-foundations/04-numerical-dispersion-diffusion.md)
   applies on top of the one-dimensional numbers given here.
4. **Compact schemes need a solve.** The bandwidth numbers above are non-zeros,
   not arithmetic operations; a tridiagonal solve costs a forward and backward
   sweep and parallelises over the band, which is why it suits CPUs and
   penalises short-vector accelerators.
5. **Staggered conservation is for the leapfrog update.** The energy invariant
   belongs to the specific time discretisation; an implicit or Runge–Kutta time
   step with the same staggered space differencing has no such invariant.
6. **Width is not accuracy.** A 9-point stencil has a larger round-off floor
   than a 5-point one; the high-order advantage is real only in the regime where
   the truncation term dominates.

## 6. Python demonstration

`code/fd_stencils_demo.py` prints:

1. measured orders 2, 4, 6, 8 and the round-off floor of each;
2. the dispersion table for seven schemes and the measured staggered/centred
   coefficient ratio 3.908 against the exact 4.000;
3. resolving power in points per wavelength with the width product;
4. the compact fourth-order solve, its order 4.0000 and its non-zero count
   against the explicit stencil;
5. the energy drift of the leapfrog update over 5000 steps.

```bash
cd 19-numerical-modeling-hpc/02-finite-difference-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_stencils_demo.py
```

## Mastery checkpoint

Without notes:

> A wave model must keep the phase error of its shortest wavelength below
> $0.5\,\%$. **(a)** Compute the points per wavelength needed by a second-order
> explicit stencil and by a fourth-order explicit stencil, using the measured
> dispersion table. **(b)** Repeat for the staggered two-point derivative and
> state why it beats the centred stencil of the same order. **(c)** Explain what
> the compact fourth-order scheme changes about the *linear algebra* of the
> problem, and give its measured advantage in non-zeros at $n = 1024$.
> **(d)** State one situation in which you would not choose the compact scheme.

Parts (a)–(c) are worked in
[`exercises/02-fd-stencils-solutions.md`](exercises/02-fd-stencils-solutions.md).

## Common pitfalls

1. **Believing that high order always wins.** Width and round-off grow with
   order; §3.1 shows the higher-order stencil reaching its floor first.
2. **Quoting "ten points per wavelength" without the scheme and the Courant
   number.** It is a statement about a specific stencil and a specific error
   level.
3. **Mistaking the asymptotic coefficient ratio for a measured ratio.** 3.908
   against 4.000 is the honest pair.
4. **Forgetting that a staggered grid needs staggered material properties.**
   Density is needed at the faces, where the velocity is stored; averaging it
   there re-introduces the error the staggering was meant to remove.
5. **Assuming a compact scheme costs more.** At equal accuracy it can cost
   less — but it does couple all nodes, which changes parallel efficiency.
6. **Assuming an energy invariant transfers.** The conservation of §3.5 belongs
   to the leapfrog update in the staggered variables.

## Related modules

- [19-02-05 Finite-Difference Acoustic and Elastic Wave Propagation](05-fd-wave-propagation.md) —
  the staggered scheme in a two-dimensional elastic setting.
- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](../01-numerical-foundations/04-numerical-dispersion-diffusion.md) —
  the anisotropy the compact scheme of the next module reduces.
- [04-spectral-and-pseudospectral](../04-spectral-and-pseudospectral/README.md) —
  the limit case where resolving power is bought with global basis functions.
- [03-02-08 Replacing Loops: Vectorisation Patterns and Traps](../../03-scientific-computing/02-numpy/08-vectorisation-patterns.md).
- [Module 19-02 Finite-Difference Methods](README.md).

Exercises and worked solutions:
[`exercises/02-fd-stencils-exercises.md`](exercises/02-fd-stencils-exercises.md)
and
[`exercises/02-fd-stencils-solutions.md`](exercises/02-fd-stencils-solutions.md).
