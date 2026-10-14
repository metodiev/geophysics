---
id: 06-02-06
title: "Wavefront Tracking and the Fast Marching Method"
level: doctoral
prereqs: ["06-02-01", "06-02-04", "06-02-05", "01-12-03"]
tags: [seismology, eikonal-solver, fast-marching, fast-sweeping, wavefront, numerics]
---

# Wavefront Tracking and the Fast Marching Method

Ray tracing follows one path at a time, and it fails by returning *no path* —
behind a velocity drop, inside a shadow, or wherever the two-point problem has no
root. Solving the eikonal equation on a grid complements it by failing in the
opposite direction: it always returns a time, for every point, and that time is
the first arrival of *some* propagation mechanism. This lesson is about how those
grid solvers work, how accurately they work, and what the guarantee they provide
does and does not mean.

Two algorithms are implemented side by side in the demonstration. The **fast
marching method** accepts grid nodes in increasing order of travel time, in the
manner of Dijkstra's shortest-path algorithm, using the Godunov upwind
discretisation of $|\nabla T| = 1/v$. The **fast sweeping method** updates the
whole grid repeatedly in alternating directions — a Gauss–Seidel iteration on the
same stencil — and converges because information propagates one characteristic
direction per sweep. Both are first order, both use the same four-point stencil,
and comparing them is therefore a comparison of *orderings*, not of physics.

That last point is the honest difficulty of the lesson, and it is worth stating
plainly before any code runs: **agreement between two solvers that share a
discretisation is evidence about the discretisation.** The demonstration reports
that the two solvers agree with each other *exactly* in double precision and
disagree with the closed-form solution by tens of milliseconds. The shared error
is the real error, and no amount of iterating removes it — only refining the grid
does, and only at first order.

**All models and data in this module are SYNTHETIC.** The homogeneous medium and
the linear gradient used here are chosen teaching models, and no measured data
appears in this lesson. Every number below is printed by
`code/wavefront_tracking_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the eikonal equation as a boundary-value problem and **explain** why
   a selection principle (the viscosity solution) is needed before the problem is
   well posed.
2. **Derive** the Godunov upwind discretisation from the eikonal equation,
   including the two cases of the update formula and the reason for upwinding.
3. **Explain** why the fast marching method needs one pass over the grid while
   the fast sweeping method needs several, and **state** the causality argument
   each relies on.
4. **Measure** the convergence order of both solvers against a closed form and
   **interpret** the value (about 0.8 to 0.98 rather than a clean 1.0) in terms of
   where the error is concentrated.
5. **Compute** a Godunov update by hand and verify it against a solver result.
6. **Rank** discretisation error against velocity-model error for a stated model
   uncertainty, and **state** the grid spacing at which refining further stops
   paying.
7. **List** the classes of arrivals and media that a first-arrival grid solver
   cannot represent, and **name** the alternative for each.

## Prerequisites

- [01 Eikonal Equation, Rays and Fermat's Principle](01-eikonal-and-rays.md) —
  where $|\nabla T| = 1/v$ comes from and why it is a high-frequency limit.
- [04 Ray Tracing in Laterally Varying Media](04-ray-tracing.md) — the
  path-based alternative and its failure modes.
- [05 Shadow Zones, Triplications and the Low-Velocity Zone](05-shadow-zones.md) —
  the geometries that make first-arrival solvers necessary and insufficient.
- [01-12-03 Numerical Differentiation and Finite-Difference Stencils](../../01-mathematics/12-numerical-methods/03-numerical-differentiation.md)
  — the truncation-error machinery used throughout.

## 1. The eikonal equation as a boundary-value problem

For a point source at $\mathbf{x}_0$ the travel-time field satisfies

$$|\nabla T|^{2} = \frac{1}{v(\mathbf{x})^{2}}, \qquad T(\mathbf{x}_0) = 0,$$

which is a first-order nonlinear boundary-value problem. It is *not* well posed as
it stands. The equation is satisfied by every branch of a multi-valued arrival
time — the direct wave, each reflected wave, each triplicated arrival — and the
classical characteristic construction produces all of them at once. To get a
single-valued function, one more condition is needed.

The condition used by grid solvers is *viscosity*: solve
$|\nabla T| = 1/v + \varepsilon\nabla^{2}T$ and take the limit
$\varepsilon \to 0^{+}$. The limit exists, is unique among Lipschitz functions,
and equals the **first-arrival time**. Two consequences are worth carrying:

- a fast marching or fast sweeping solve returns the *first* arrival at each node,
  so a triplication is invisible to it — the later branches are still solutions of
  the equation, they are just not the viscosity solution;
- the limit is not a pointwise limit of smooth solutions: it is exactly the
  selection rule that discards kinks-and-branches in favour of the earliest
  arrival, and it is what makes a heap-based acceptance order legitimate.

## 2. The Godunov upwind discretisation

Discretise on a uniform grid of spacing $h$, and let $T_{i,j}$ be the unknown at
node $(i,j)$. The gradient is approximated by one-sided differences, choosing at
each node the direction from which information *arrives*, i.e. the smaller of the
two one-sided values. Write

$$a = \min\left(T_{i-1,j},\,T_{i+1,j}\right)
\quad\text{(the two neighbours along } x\text{)}, \qquad
b = \min\left(T_{i,j-1},\,T_{i,j+1}\right)
\quad\text{(along } z\text{)} .$$

The Godunov upwind scheme is then the solution of

$$\left(\max\left(T - a,\,0\right)\right)^{2} +
\left(\max\left(T - b,\,0\right)\right)^{2} = \left(\frac{h}{v_{i,j}}\right)^{2}
= f^{2}.$$

Solving for the larger root, with $a \le b$:

$$T = \begin{cases}
a + f, & a + f \le b \quad\text{(one-sided / axis-aligned information)},\\[2mm]
\dfrac{a + b + \sqrt{2f^{2} - (b-a)^{2}}}{2}, & \text{otherwise (diagonal)}.
\end{cases}$$

**Why upwind?** A centred difference would couple $T_{i,j}$ to neighbours whose
own values are larger, i.e. to information that has not yet arrived. The
$\max(\cdot,0)$ in the stencil removes exactly those contributions, which is what
makes the scheme monotone and therefore convergent to the viscosity solution. It
is also why the scheme is only first order: the true gradient to a diagonal
neighbour is resolved by two axis-aligned differences, and the resulting staircase
approximation of a diagonal front is a first-order object (Section 4).

## 3. Two ways to order the same update

### 3.1 Fast marching — accept nodes in increasing time

Every node is in one of three states: known (accepted), frontier (computed but
provisional), or untried. The algorithm repeatedly extracts the frontier node with
the smallest tentative time, accepts it permanently, and updates its four
neighbours with the Godunov formula above. This is Dijkstra's algorithm applied to
a continuous front.

The correctness argument is a causality argument: because the true first-arrival
time at a node cannot be smaller than the time at any node that reaches it, the
smallest frontier value *is* the true value, and it can never be improved later.
The demonstration's implementation therefore uses one min-heap of size
$\mathcal{O}(N)$ and performs one update per edge; each node is accepted exactly
once.

### 3.2 Fast sweeping — update everything, in alternating directions

The fast sweeping method performs Gauss–Seidel sweeps over the whole grid, each
sweep visiting the nodes in one of four orders (increasing/decreasing $i$,
increasing/decreasing $j$), applying the same Godunov update at every node, and
repeats until no node changes by more than a tolerance. Each sweep propagates
information correctly along the directions it visits, so four direction families
cover the four quadrant directions of the front.

The measured behaviour is better than the worst case: for both the homogeneous
model and the linear gradient the demonstration converges in **3 sweeps** at every
grid spacing tested. Sweeping is trivially parallel in parts, has no heap and no
priority queue, and is often the faster choice on structured grids; marching has
a stronger locality story and extends naturally to unstructured meshes.

### 3.3 What their agreement means

| $h$ (m) | sweeps | sweeping error (ms) | marching error (ms) | \|sweep − march\| (ms) |
|---|---|---|---|---|
| 100.0 | 3 | 44.144665 | 44.144665 | $0.000\times10^{0}$ |
| 50.0 | 3 | 25.445223 | 25.445223 | $0.000\times10^{0}$ |
| 25.0 | 3 | 14.435493 | 14.435493 | $0.000\times10^{0}$ |

for $v = 3500\ \mathrm{m\,s^{-1}}$ on a 10 km square with the source in a corner
and the exact solution $T = r/v$. The two solvers differ only in the *order* in
which the identical update is applied, and they agree to machine precision at
every node. Their common disagreement with the exact circle — 44.1 ms at
$h = 100$ m — is the discretisation error of the four-point stencil and nothing
else. **This is the correct way to read a solver-versus-solver comparison**, and
it is why the demonstration also carries closed forms.

## 4. Accuracy, measured

### 4.1 Convergence order

| model | $h = 100$ m | $h = 50$ m | $h = 25$ m | fitted order |
|---|---|---|---|---|
| homogeneous, $T = r/v$ | 44.145 ms | 25.445 ms | 14.435 ms | 0.806 |
| linear gradient, closed form | 52.549 ms | 26.665 ms | 13.431 ms | 0.984 |

Halving $h$ roughly halves the error. The fitted order is not exactly 1, and the
reason is visible in the error's distribution: the largest error lies in the first
few cells around the source, where the wavefront's curvature is largest and the
staircase approximation is worst. Refining the grid reduces that absolute error
at first order, but the *maximum* is dominated by the near-source region, so the
fitted slope comes out slightly below 1. Quoting "first order" as a slogan is
fine; measuring it is what tells you whether a result is limited by the stencil or
by a mistake.

### 4.2 Discretisation against model error

Accuracy against a closed form is only half the budget. The demonstration
perturbs the homogeneous model itself — 1.5 % rms relative velocity error with a
1 km correlation length, 30 realisations, same solver and grid — and measures the
travel time to the opposite corner of the 10 km square:

| quantity | value |
|---|---|
| exact time | 4.040610 s |
| solver time, unperturbed model | 4.084755 s (+44.145 ms) |
| solver time, perturbed models | $4.091120 \pm 24.401$ ms |
| model-error scatter ÷ discretisation error | 0.6 |

The two contributions are within a factor of two of each other. That is the
practical answer to *how fine should the grid be*: fine enough that the
discretisation error is no longer the largest term, and no finer. A grid refined
far below that point returns a travel time whose digits are precise and whose
value is no better, because the velocity field — not the solver — has become the
limiting input. The same conclusion was reached from the opposite direction in
[04](04-ray-tracing.md) Example 3, where a 1 % model error produced a 113 ms time
scatter against a 0.5 ms quadrature error.

## 5. What a first-arrival solver cannot do

1. **Later arrivals.** A triplication
   ([05](05-shadow-zones.md)) has several arrival times at one node; the viscosity
   solution selects the first. Representing the later branches requires either
   multi-arrival eikonal solvers or explicit ray tracing.
2. **Amplitudes.** The eikonal equation contains no amplitude information. A grid
   solver gives times; geometric amplitudes need the transport equation along each
   ray.
3. **Shadows and diffraction.** Inside a shadow, no ray exists, but the solver
   still returns a time for every node — the time of whatever path the
   discretisation found. In a shadow that number corresponds to no physical
   arrival, and it should not be interpreted as one.
4. **Anisotropy, without further work.** The isotropic form
   $|\nabla T| = 1/v$ presumes a scalar speed. In an anisotropic medium the
   slowness is a function of direction on the front normal, and the discretisation
   must be replaced by the appropriate (and considerably more delicate) factored
   or variational scheme.
5. **Media whose scale is below the grid.** A thin low-velocity layer thinner than
   a cell is either missed or smeared, and the resulting time is the time of an
   averaged medium. This is the hidden layer of
   [02](02-snell-and-layering.md) returning as a discretisation artefact rather
   than as a physical absence.

## 6. Worked examples

### Example 1 — one Godunov update by hand

Take $h = 100$ m, $v = 3500\ \mathrm{m\,s^{-1}}$, so
$f = h/v = 0.0285714$ s. Suppose in the two axis directions the smallest accepted
neighbour values are $a = 1.0$ ms and $b = 2.0$ ms.

1. Test the one-sided case: $a + f = 0.001000 + 0.0285714 = 0.0295714$ s, which
   is **greater** than $b = 0.002$ s, so the one-sided formula does not apply —
   information is arriving diagonally.
2. Discriminant: $2f^{2} - (b-a)^{2} = 2(0.0285714)^{2} - (0.001)^{2}
   = 1.632653\times10^{-3} - 1.0\times10^{-6} = 1.631653\times10^{-3}$;
   $\sqrt{\cdot} = 0.0403937$.
3. $T = \tfrac{1}{2}\left(a + b + \sqrt{\cdot}\right)
   = \tfrac{1}{2}(0.001 + 0.002 + 0.0403937) = 0.0216969$ s $= 21.697$ ms.

Two sanity constraints hold: the result exceeds both `a` and `b` (causality), and
it is less than $b + f = 30.571$ ms (a diagonal path is shorter in time than two
axis-aligned legs). Both are worth asserting in a solver implementation as
invariants.

### Example 2 — measuring the order instead of asserting it

From the homogeneous run, the errors at $h = 100$, $50$ and $25$ m are 44.145,
25.445 and 14.435 ms. Consecutive ratios are

$$\frac{44.145}{25.445} = 1.7349, \qquad \frac{25.445}{14.435} = 1.7627 ,$$

and since a factor-2 refinement multiplies a first-order error by $2^{p}$,
$p = \log_{2}(1.7349) = 0.795$ and $p = \log_{2}(1.7627) = 0.818$. The two
estimates bracket the fitted 0.806, and $2^{0.806} = 1.748$ reproduces the
observed ratios. **A convergence order is a measurement with a standard error,
not a property asserted from a textbook.**

### Example 3 — choosing a grid from the error budget

A study needs travel times good to 5 ms, in a medium whose velocity is uncertain
at the 1 % level over a 1 km correlation length. From Section 4.2, a 1.5 % velocity
error already produces a 24.4 ms time scatter on a 4.04 s path; scaling linearly,
1 % produces about 16 ms — larger than the 5 ms target. **No grid is fine enough
to meet the specification**, and the honest response is to report the target as
unattainable with the available velocity model rather than to refine until the
solver's own error is invisible. Working backwards: to reach 5 ms of model-induced
error the velocity would have to be known to about $0.3\%$, which is a statement
about the tomography that supplied it, not about the solver.

## 7. Assumptions and the regime of validity

1. **A single, isotropic, finite speed.** The schemes assume a well-defined local
   speed; $v = 0$ or $v \to \infty$ at a node breaks the update.
2. **A grid-resolved velocity field.** Features thinner than one cell are
   averaged, and (Section 5) the average may remove an arrival entirely.
3. **First arrivals only.** The viscosity solution is a selection, not a
   catalogue.
4. **Boundary conditions matter.** A free-surface-type boundary (a total
   reflection) must be encoded in the stencil; ignoring it makes the solver
   propagate energy through a boundary that reflects.
5. **Source singularity.** $T \sim r/v$ has a non-smooth point at the source, and
   the near-source cells dominate the maximum error (Section 4.1). A locally
   exact update near the source, or a fine local mesh, is the standard remedy.

## 8. Python demonstration

`code/wavefront_tracking_demo.py` prints three labelled sections with units:

1. **Homogeneous medium** — the two solvers against the analytic circle at three
   spacings, with sweep counts, errors, the machine-precision inter-solver
   agreement, and the fitted order.
2. **A linear gradient** — both solvers against the closed form
   $T = (1/g)\mathrm{arccosh}\left(1 + g^{2}(x^{2}+z^{2})/(2v_0(v_0+gz))\right)$,
   with the fitted order.
3. **Discretisation error against velocity-model error** — the error budget of
   Section 4.2.

```bash
cd 06-seismology/02-ray-theory-and-travel-times/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python wavefront_tracking_demo.py
```

## Mastery checkpoint

Complete this without notes:

> A solver uses $h = 50$ m and $v = 4000\ \mathrm{m\,s^{-1}}$. Two accepted
> neighbours give $a = 5.0$ ms and $b = 12.0$ ms along the two axes. **(a)** Decide
> which case of the Godunov update applies and justify it with the numbers.
> **(b)** Compute $T$ at the node. **(c)** State the two invariants you would
> assert in code. **(d)** The solver's error at $h = 50$ m is 20 ms and at
> $h = 25$ m it is 12 ms; estimate the convergence order. **(e)** Give two kinds
> of arrival or structure that this solver cannot represent, and say what a
> first-arrival time inside a shadow actually corresponds to.

A worked version of (a)–(c) appears in the lesson
[solutions](exercises/06-wavefront-tracking-solutions.md).

## Common pitfalls

1. **Reading inter-solver agreement as validation.** Two solvers sharing a stencil
   share its error; a closed form or a physical check is needed for more.
2. **Quoting "first order" without measuring it.** The fitted value here is 0.806
   to 0.984, and the deviation is informative about *where* the error lives.
3. **Refining the grid past the model error.** Once the velocity field dominates,
   smaller $h$ buys digits, not accuracy.
4. **Using a first-arrival time inside a shadow as if a ray existed.** The solver
   always returns a number; the number may correspond to no physical arrival.
5. **Forgetting the source singularity.** The largest error is in the first few
   cells; a global refinement is an expensive way to fix a local problem.
6. **Using the isotropic stencil for an anisotropic medium.** The whole structure
   of the discretisation changes.

## Related modules

- [01 Eikonal Equation, Rays and Fermat's Principle](01-eikonal-and-rays.md) —
  the same equation, derived and solved less carefully.
- [04 Ray Tracing in Laterally Varying Media](04-ray-tracing.md) — the path-based
  counterpart, and the settings in which it beats a grid.
- [05 Shadow Zones, Triplications and the Low-Velocity Zone](05-shadow-zones.md) —
  exactly the geometries that a first-arrival solver cannot represent.
- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the full wavefield, of which these solvers give the first arrival only.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — grids,
  stencils, convergence and performance in general.
- [01-12-03 Numerical Differentiation and Finite-Difference Stencils](../../01-mathematics/12-numerical-methods/03-numerical-differentiation.md) —
  the truncation-error analysis behind the measured orders.

## Exercises

Full sets with worked solutions are in
[`exercises/06-wavefront-tracking-exercises.md`](./exercises/06-wavefront-tracking-exercises.md)
and
[`exercises/06-wavefront-tracking-solutions.md`](./exercises/06-wavefront-tracking-solutions.md).
