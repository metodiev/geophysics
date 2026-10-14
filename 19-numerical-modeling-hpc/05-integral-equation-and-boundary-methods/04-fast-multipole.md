---
id: 19-05-04
title: "Fast Multipole and Hierarchical Acceleration"
level: research
prereqs: ["19-05-01", "19-05-03", "19-01-02"]
tags: [numerical-modelling, hpc, fast-multipole, tree-code, hierarchical, scaling, potential-fields]
---

# Fast Multipole and Hierarchical Acceleration

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the far-field Taylor expansion of a $1/r$ kernel about a node
   centre, and define the node moments it requires.
2. **State** an admissibility criterion and explain what it bounds.
3. **Measure** the geometric convergence of a single node's expansion in the
   number of moments, and connect the rate to the half-width-to-distance ratio.
4. **Measure** the accuracy of a complete tree code against a direct sum, and
   report the trade between the opening angle and the interaction count.
5. **Count** interactions exactly and explain why the measured wall-clock speedup
   of a Python tree code against a vectorised direct sum is **not** the count
   ratio.
6. **Explain** how the same structure turns a dense boundary operator into a
   linear-cost one.

## Prerequisites

- [19-05-01 Volume and Surface Integral Equations](01-integral-equations.md) —
  where the dense $N\times M$ sum comes from, and the measured multipole decay
  that motivates this lesson.
- [19-05-03 Numerical Green's Functions and Their Computation](03-greens-function-numerics.md) —
  the kernels being summed.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md) —
  the measurement discipline used for every rate here.

All models and data in this module are **SYNTHETIC**: source positions, receiver
lines and strengths are chosen teaching values. There is no measured dataset, no
published benchmark and no hardware model name anywhere in this lesson.

## 1. The problem: a dense sum

Every integral representation in this module ends in the same arithmetic,

$$\phi(y_i) = \sum_{j=1}^{N_{\text{src}}} \frac{q_j}{|\mathbf{y}_i -
\mathbf{x}_j|}, \qquad i = 1,\dots,N_{\text{rec}} .$$

For $N$ sources and $N$ receivers the count is $N^{2}$: the demonstration's
$N = 3200$ case would be $10\,240\,000$ pair evaluations, and a 3-D problem with
$10^{7}$ sources is out of reach. The fix is not a faster machine but a different
question: **can a group of sources be replaced by a few numbers?**

## 2. Moments and the far-field expansion

Consider a node containing particles at positions $x_j = c + \delta_j$, and a
target at $y$ that is far compared with the node's half-width $s$. With
$D = |y - c|$ and $u = y - c$, each term of the kernel expands as

$$\frac{1}{|y - x_j|} = \frac{1}{|u - \delta_j|},$$

and since $\max_j|\delta_j| = s < D$, a geometric series is available whose
coefficients depend on the source distribution only through the **moments**

$$M_k = \sum_{j} q_j\,\delta_j^{\,k}.$$

Two sign cases arise and they matter (see Section 7): if the node lies to the
**right** of the target, $|u - \delta| = (y - c) - \delta$ when $y > c$, and the
series is $\sum_k M_k/D^{k+1}$. If the node lies to the **left**, the kernel is
$1/(D + \delta)$ and the series alternates: $\sum_k (-1)^{k}M_k/D^{k+1}$. A tree
code that uses one form for both cases is wrong by the reflection parity, and it
is wrong silently.

For the demonstration's 400 sources the root node has

$$M_0 = +4.04726574\times10^{2},\quad M_1 = -3.28017101\times10^{0},\quad
M_2 = +3.30569802\times10^{1},\quad M_3 = -7.35363148\times10^{-1},$$

in units of strength and of km$^{k}$ respectively. $M_0$ is the node's total
strength, $M_1$ its dipole, $M_2$ its quadrupole: the same hierarchy that
Section 7 of [01 Volume and Surface Integral Equations](01-integral-equations.md)
measured decaying as $R^{-2}$ in the residual of a single rectangle's field.

## 3. How fast does one node's expansion converge?

Evaluating one node (all 400 sources) at $y = 2.5$ km, where the exact sum is
$205.6370151508\ \mathrm{km^{-1}}$:

| $p$ (terms kept) | relative error |
|---|---|
| 1 (monopole) | $1.663\times10^{-2}$ |
| 2 | $2.061\times10^{-2}$ |
| 3 | $5.571\times10^{-4}$ |
| 4 | $7.800\times10^{-4}$ |
| 6 | $3.537\times10^{-5}$ |
| 8 | $1.743\times10^{-6}$ |
| 10 | $9.005\times10^{-8}$ |

The arithmetic of the first row is worth doing by hand:

$$\frac{M_0}{|y - c|} = \frac{404.726574}{2.001436} = 202.2180799309,$$

against the exact $205.6370151508$ — an error of $1.66\%$ from the monopole
alone. Each additional pair of terms buys about two orders of magnitude, at a
rate set by $s/d = 0.2470$: the truncation error behaves like $(s/d)^{p+1}$.

Note the **non-monotonicity** at $p = 2$, where the error is slightly larger than
at $p = 1$. This is not an implementation artefact: $M_1/M_0 = -8\times10^{-3}$
in units of km, so the dipole term is small and can move the estimate away from
the exact value before the quadrupole corrects it. An error table that is not
monotone is information about the source distribution, and a lesson that reports
only $p \ge 3$ hides it.

## 4. A tree code, and what the admissibility test buys

The algorithm: sort the sources, build a binary hierarchy by splitting, and for
each target either

- accept a node as **far** if $|y - c| > \theta s$, and use its $p$ moments; or
- descend, and if a leaf is not acceptable, sum its particles **directly**.

$\theta$ is the opening angle. The demonstration's results, on a synthetic
receiver line at $[2,3]$ km well separated from the source line at $[0,1]$ km
(400 sources, 400 receivers, $\theta = 2.0$):

| $p$ | max relative error | far-field nodes | particles far | particles direct |
|---|---|---|---|---|
| 1 | $4.208\times10^{-2}$ | 400 | 160000 | 0 |
| 3 | $3.187\times10^{-3}$ | 400 | 160000 | 0 |
| 6 | $2.249\times10^{-4}$ | 400 | 160000 | 0 |
| 10 | $1.835\times10^{-6}$ | 400 | 160000 | 0 |

One node per target: the entire source line is far from every receiver, so the
work falls from $160\,000$ pair evaluations to $400$ node evaluations. That is
the ideal case, and it is fair to show it first because it isolates the accuracy
question from the counting question.

The realistic case puts the receivers **on the source line**, so no target is
outside the root node and the walk must descend:

| $p$ | max relative error | far-field nodes | direct particles | self terms skipped |
|---|---|---|---|---|
| 1 | $3.819\times10^{-2}$ | 2851 | 9063 | 400 |
| 3 | $5.613\times10^{-3}$ | 2851 | 9063 | 400 |
| 6 | $8.973\times10^{-4}$ | 2851 | 9063 | 400 |
| 8 | $1.804\times10^{-4}$ | 2851 | 9063 | 400 |

with a tree depth of $5$ and $32$ leaves ($16$ particles each). The direct work
is now real — about $9\,000$ particle pairs — and the accuracy knob still works.

The opening angle, at $p = 6$:

| $\theta$ | max relative error | far-field nodes | direct particles |
|---|---|---|---|
| 1.0 | $3.418\times10^{-1}$ | 1996 | 4699 |
| 1.5 | $6.867\times10^{-3}$ | 2432 | 6820 |
| 2.0 | $8.973\times10^{-4}$ | 2851 | 9063 |
| 3.0 | $8.135\times10^{-5}$ | 3695 | 13494 |
| 5.0 | $1.975\times10^{-6}$ | 4680 | 22054 |

A **larger** $\theta$ makes the far test stricter, which is why accuracy improves
and direct work grows. Both knobs trade accuracy for the interaction count, and
both counts are exact integers, not estimates.

## 5. The count scaling, and why the measured speedup is not it

Self-potential geometry, $p = 6$, $\theta = 1.5$:

| $n$ | direct pairs | tree far-field nodes | tree direct particles | $t_{\text{direct}}$ | $t_{\text{tree}}$ | measured ratio |
|---|---|---|---|---|---|---|
| 200 | $4.0\times10^{4}$ | 924 | 3355 | 0.04 ms | 2.21 ms | 0.02× |
| 400 | $1.6\times10^{5}$ | 2422 | 6851 | 0.34 ms | 5.12 ms | 0.07× |
| 800 | $6.4\times10^{5}$ | 6035 | 13660 | 0.57 ms | 11.89 ms | 0.05× |
| 1600 | $2.56\times10^{6}$ | 14429 | 27552 | 2.89 ms | 25.71 ms | 0.11× |
| 3200 | $1.024\times10^{7}$ | 33636 | 55066 | 9.14 ms | 57.00 ms | 0.16× |

Read the counts and the times separately, because they say different things.

- The **counts** show the algorithm: direct work grows as $n^{2}$ while the tree's
  far-field node count grows about linearly and its direct-particle count stays a
  small multiple of $n$.
- The **times** show this implementation: the direct sum is one vectorised numpy
  expression while the tree walks Python objects one node at a time. The measured
  ratio is below $1$ at **every** size tested, rising only from $0.02$ to $0.16$.

A lesson that reported the count ratio as a speedup would be reporting an
intention. The honest statement is: *the asymptotic advantage is in the counts;
whether a particular implementation realises it depends on the constant factor of
the near-field and traversal work, and here, in pure Python, it does not at any
size tested.*

## 6. Assumptions and regime of validity

1. **A kernel with a decaying multipole expansion.** The expansion requires
   $s < D$ and a smooth kernel away from the source. A Green's function with a
   strong layering response has a longer-range tail and needs more than $p$ terms
   or a different expansion.
2. **Well-separated groups.** The admissibility test is what makes the series
   converge; a target inside a node's span must be handled directly, and the
   count of such interactions is what sets the near-field constant.
3. **Point sources on a line, 1-D geometry, kernel $1/r$.** The measured orders
   are properties of this geometry. Three dimensions adds the translation
   operators of the full fast multipole method and changes the constants, not the
   structure.
4. **A monotone error is not promised.** Section 3 measured a non-monotone $p$
   sequence; a convergence claim must be made over a range of $p$, not between
   two adjacent values.
5. **Accuracy is not the only requirement.** A tree code's error must be
   *controllable* — the same run with more moments must be more accurate — and it
   must be *reproducible*: the traversal order affects the summation order and
   therefore the last bits, which is the subject of
   [19-06-07 Reproducibility and Provenance in HPC Workflows](../06-hpc-and-parallel-computing/07-reproducible-hpc.md).
6. **Parallelism is not free.** Distributing the sources changes the tree, and
   the far-field/near-field split must be rebuilt; the load balance of a tree is
   a separate problem — see
   [19-06-05 Domain Decomposition and Load Balancing](../06-hpc-and-parallel-computing/05-domain-decomposition.md).

## 7. A fully worked example: the alternating sign

Take a node with centre $c = 0.498564$ km and half-width $s = 0.494405$ km, and
two targets: $y = 2.5$ km (to the right of the node) and $y = -1.5$ km (to the
left). The node's span is $[0.004159, 0.992969]$ km, so both targets are outside
it and $|y - c| = 2.001436$ km in the first case and $1.998564$ km in the second.

- **Right of the node:** $|y - x_j| = (y - c) - \delta_j$, so
  $1/|y-x_j| = (1/D)\sum_k(\delta_j/D)^{k}$ and
  $\phi = \sum_k M_k/D^{k+1}$ with **all signs positive**.
  Monopole: $M_0/D = 404.726574/2.001436 = 202.218080$, error $1.66\%$.
- **Left of the node:** $|y - x_j| = (c - y) + \delta_j = D + \delta_j$, so
  $1/|y-x_j| = (1/D)\sum_k(-\delta_j/D)^{k}$ and
  $\phi = \sum_k (-1)^{k}M_k/D^{k+1}$: **alternating signs**.

For the symmetric source distribution used here $M_1 = -3.28$ and $M_2 = 33.06$,
so ignoring the alternation at $p = 2$ produces a dipole term of the wrong sign,
and at $p = 3$ a quadrupole term of the wrong sign. The error is not a small
perturbation; it is a reflection error, and it is the reason a tree code must
branch on which side of the node the target lies — a case the demonstration's
own first version got wrong, and which the direct-sum comparison caught
immediately because the error was $O(1)$ rather than $O((s/d)^{p})$.

The general lesson: **the check that catches a wrong expansion is an independent
direct evaluation, not a self-consistency test.** A tree code is self-consistent
under almost any sign convention.

## 8. Python demonstration

`code/fast_multipole_demo.py` builds the moments, measures the single-node
convergence in $p$, runs the tree code in both geometries, sweeps the opening
angle, counts every interaction exactly, and times the direct and tree routes at
five sizes with the small-problem and implementation caveat printed alongside the
numbers.

```bash
cd 19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fast_multipole_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/04-fast-multipole-exercises.md`](./exercises/04-fast-multipole-exercises.md)
and [`exercises/04-fast-multipole-solutions.md`](./exercises/04-fast-multipole-solutions.md).

- **★** Verify the monopole arithmetic $M_0/|y-c|$ for $y = 2.5$ km.
- **★** State the admissibility criterion and explain what $s/d$ bounds.
- **★★** From the single-node error table, estimate the error at $p = 12$ and
  state the assumption behind the estimate.
- **★★** Using the count table, estimate the size at which a compiled tree would
  break even against a vectorised direct sum, and say what extra information the
  estimate needs.
- **★★★** Design a numerical experiment that determines whether an error of
  $O(1)$ in a tree code comes from the sign convention in the expansion or from a
  wrong admissibility test, and state the observable that distinguishes them.

## Mastery checkpoint

Without notes:

> A tree code returns a potential whose maximum relative error against a direct
> sum is $1\times10^{-3}$ with $\theta = 2$ and $p = 6$. **(a)** State whether
> raising $\theta$ or raising $p$ should be used to improve it, and what each
> costs. **(b)** The same code on a receiver line far from all sources reports
> $400$ far-field nodes and $0$ direct particles for $400$ receivers; explain why
> the count is so small. **(c)** The measured wall-clock ratio against a
> vectorised direct sum is $0.16$ at $n = 3200$. Explain what that number does and
> does not say about the algorithm.

A worked version appears in the lesson-04
[solutions](./exercises/04-fast-multipole-solutions.md).

## Common pitfalls

1. **Applying one sign convention on both sides of a node.** The kernel is
   $1/|y-x|$, so the series alternates when the node lies to the left; the error
   this produces is $O(1)$, not $O((s/d)^{p})$.
2. **Reading a speedup from interaction counts.** Counts show an algorithm; times
   show an implementation. They agreed nowhere in the measured table.
3. **Comparing against the previous $p$.** The measured $p = 2$ row is worse than
   $p = 1$; a rate needs a range.
4. **Forgetting the self term.** With receivers at the sources, one term per
   target is infinite and must be excluded deliberately; the demonstration counts
   $400$ skipped self terms at $n = 400$.
5. **Assuming the near field is negligible.** Direct particles stayed between
   $4.7\times10^{3}$ and $2.2\times10^{4}$ in the $\theta$ sweep: the near field
   is the constant factor that decides whether the method pays at a given size.
6. **Treating the opening angle as a tuning knob with no cost.** Every increase
   of $\theta$ that improves accuracy raises the direct work, and the table shows
   both columns moving together.

## Related modules

- [01 Volume and Surface Integral Equations](01-integral-equations.md) — the
  dense sum and the multipole decay that motivates acceleration.
- [02 Boundary Element Methods for Potential Fields](02-boundary-element.md) —
  the dense operator that a hierarchical method makes affordable.
- [03 Numerical Green's Functions and Their Computation](03-greens-function-numerics.md) —
  the kernels being expanded.
- [19-06 High-Performance and Parallel Computing](../06-hpc-and-parallel-computing/README.md) —
  the implementation question this lesson deliberately separates from the
  algorithm.
- [19-08 Geophysical Simulation Case Studies](../08-geophysical-simulation-case-studies/README.md) —
  where dense sums of this form appear in production simulations.
