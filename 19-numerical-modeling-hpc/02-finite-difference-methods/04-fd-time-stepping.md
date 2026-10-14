---
id: 19-02-04
title: "Explicit vs Implicit Time Stepping and Stability Limits"
level: doctoral
prereqs: ["19-02-01", "19-01-03", "19-02-03"]
tags: [numerical-modelling, hpc, time-stepping, cfl, implicit, stiffness]
---

# Explicit vs Implicit Time Stepping and Stability Limits

The space discretisation sets the truncation error; the time discretisation sets
the step size, and the step size sets the run time. This lesson measures the
stability limits of the explicit schemes for diffusion and for the wave
equation, shows what an implicit scheme does about them, and separates the two
questions that are routinely confused: **stability** (does the error grow?) and
**accuracy** (is the answer right?). It closes with the count that decides most
production runs — how many steps each choice needs, and what each step costs.
**All models and data in this module are SYNTHETIC.** Every number quoted here is
printed by `code/fd_time_stepping_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the stability limit $r \le 1/2$ of the explicit (FTCS) diffusion
   scheme from the amplification factor and **measure** the growth per step of
   the highest mode on both sides of it.
2. **Measure** the order of accuracy in time of three schemes against the *exact
   solution of the space-discretised problem*, so that the spatial error is
   excluded from the measurement.
3. **Explain** why the explicit step limit scales as $h^{2}/(2\alpha d)$ and
   **compute** the step count a three-dimensional refinement implies.
4. **Derive** the CFL limit $C \le 1$ of the explicit wave scheme and
   **measure** the growth rate beyond it against the closed form.
5. **Distinguish** unconditional stability from accuracy by marching a
   trapezoidal scheme far beyond its CFL and measuring both the bounded
   amplitude and the growing error.
6. **Choose** between explicit and implicit time stepping for a stated accuracy
   target, using step counts and work per step rather than habit.

## Prerequisites

- [19-02-01 Deriving Finite-Difference Operators via Taylor Expansion](01-fd-derivation.md) —
  the spatial operators whose eigenvalues drive the stability limits.
- [19-01-03 Consistency, Stability and the Lax Equivalence Theorem](../01-numerical-foundations/03-consistency-stability.md) —
  the amplification-factor analysis used throughout.
- [19-02-03 Boundary Conditions: Dirichlet, Neumann, Absorbing, PML](03-fd-boundary-conditions.md) —
  the boundary treatment a time-stepping scheme has to live with.

## 1. Intuition: two limits, two philosophies

Diffusion and waves have opposite behaviours, and the schemes follow.

- **Parabolic (diffusion).** The solution of the semi-discrete system has modes
  decaying like $e^{-4\alpha\sin^{2}(\theta/2)t/h^{2}}$; the fastest mode decays
  in a time $\sim h^{2}/(4\alpha)$. An explicit scheme must resolve that decay,
  so $dt \propto h^{2}$. Refining the grid in three dimensions costs $n^{2}$ steps
  on top of $n^{3}$ unknowns.
- **Hyperbolic (waves).** Information travels at speed $c$, and an explicit
  scheme may not let it cross more than one cell per step: $dt \le h/c$, i.e.
  $dt \propto h$. Refinement costs $n$ steps on $n^{3}$ unknowns, which is
  cheaper per unknown than diffusion but still fast to grow.

Implicit schemes remove the *stability* limit by solving a linear system at each
step. They do not remove the *accuracy* limit, and they do not make a stiff
problem cheap: a stiff system still needs many steps for accuracy at the
timescale you care about — the point of implicit methods is that the steps you
need are set by accuracy, not by the grid.

## 2. Precise definitions

**Diffusion number.** $r = \alpha\,dt/h^{2}$ for $u_t = \alpha u_{xx}$.

**Courant number.** $C = c\,dt/h$ for hyperbolic equations.

**FTCS.** Forward time, centred space: $u_i^{n+1} = u_i^{n} + r(u_{i+1} - 2u_i
+ u_{i-1})$, amplification $G = 1 - 4r\sin^{2}(\theta/2)$.

**Backward Euler (BE).** $(1 - dt\,\alpha\nabla^{2})u^{n+1} = u^{n}$;
$G = 1/(1 + 4r\sin^{2}(\theta/2))$, unconditionally stable, first order in $dt$.

**Crank–Nicolson (CN).** $(1 - \tfrac{dt}{2}\alpha\nabla^{2})u^{n+1}
= (1 + \tfrac{dt}{2}\alpha\nabla^{2})u^{n}$;
$G = (1-2r\sin^{2})/(1+2r\sin^{2})$, unconditionally stable, second order in $dt$.

**Leapfrog for waves.** $u^{n+1} = 2u^{n} - u^{n-1} + C^{2}(u_{i+1} - 2u_i +
u_{i-1})$, amplification roots of $G^{2} - 2bG + 1 = 0$ with
$b = 1 - 2C^{2}\sin^{2}(\theta/2)$.

**Trapezoidal (average-acceleration, Newmark $\beta = 1/4$).** The implicit
counterpart of leapfrog,

$$u^{n+1} - 2u^{n} + u^{n-1}
= \frac{C^{2}}{4}\nabla^{2}\!\left(u^{n+1} + 2u^{n} + u^{n-1}\right),$$

whose amplification satisfies $|G| = 1$ for every $C$ and every mode.

## 3. Derivations

### 3.1 The explicit diffusion limit, measured

For the highest grid mode ($\theta = \pi$) the FTCS amplification is exactly
$G = 1 - 4r$, so the condition $|G|\le1$ gives $0 \le r \le 1/2$. The
demonstration starts the checkerboard mode on a periodic grid and measures the
growth per step over 200 steps:

| $r$ | $\lvert 1-4r\rvert$ predicted | measured growth/step | amplitude after 200 |
|---|---|---|---|
| 0.250 | 0.00000000 | 0.00000000 | $0.000000\times10^{0}$ |
| 0.490 | 0.96000000 | 0.96000000 | $2.846077\times10^{-4}$ |
| 0.500 | 1.00000000 | 1.00000000 | $1.000000\times10^{0}$ |
| 0.501 | 1.00400000 | 1.00400000 | $2.221992\times10^{0}$ |
| 0.550 | 1.20000000 | 1.20000000 | $6.858817\times10^{15}$ |
| 0.750 | 2.00000000 | 2.00000000 | $1.606938\times10^{60}$ |

Agreement is exact because the checkerboard *is* an eigenmode on a periodic grid —
a detail worth remembering: measuring a stability limit on a mode that is not an
eigenmode gives a number contaminated by beating between modes. Two entries
deserve notice. At $r = 1/4$ the mode is annihilated in one step ($G = 0$). At
$r = 1/2$, the classical limit, the mode is **exactly neutral**: it neither grows
nor decays, which is stability at the boundary and one reason $r = 0.5$ is a poor
working value — the highest mode of the data never disappears.

### 3.2 Orders of accuracy in time, isolated from space

To measure a time order you must remove the spatial error. The clean way is to
compare against the exact solution of the *space-discretised* problem, obtained
from the eigen-decomposition of the discrete Laplacian,
$u_{\text{exact}}(t) = V e^{\Lambda t} V^{\mathsf T} u_0$. With $n = 64$ interior
nodes on $(0,1)$ and a Dirichlet cosine start, the semi-discrete eigenvalues are
known, so this is exact. The measured $L^{2}$ errors:

| scheme | $dt$ range | finest-4 errors | observed order |
|---|---|---|---|
| FTCS explicit | $1.2\times10^{-4} \to 1.5\times10^{-5}$ | $1.541\times10^{-4}$, $7.702\times10^{-5}$, $3.850\times10^{-5}$, $1.925\times10^{-5}$ | 1.0000 |
| backward Euler | $10^{-2} \to 1.25\times10^{-3}$ | $1.233\times10^{-2}$, $6.287\times10^{-3}$, $3.175\times10^{-3}$, $1.596\times10^{-3}$ | 0.9926 |
| Crank–Nicolson | $10^{-2} \to 1.25\times10^{-3}$ | $2.113\times10^{-4}$, $5.278\times10^{-5}$, $1.319\times10^{-5}$, $3.298\times10^{-6}$ | 2.0001 |

(Each row halves its own $dt$ four times; the errors are listed from the largest
to the smallest step. FTCS is restricted to $dt\le1.2\times10^{-4}$ because at
$h = 0.0154$ m its stability limit is $0.5h^{2}/\alpha = 1.183\times10^{-4}$ s,
while the implicit schemes are shown at steps a hundred times larger — the
observed order is dimensionless and comparable across the rows.) Two conclusions:
the order is a property of the time discretisation alone, and an implicit scheme
is *not* more accurate per step — at $dt = 10^{-2}$ backward Euler's error is
$58$ times Crank–Nicolson's.

### 3.3 The cost of the explicit limit

The limit $dt \le h^{2}/(2\alpha d)$ in $d$ dimensions gives, for $h = 1/100$ m
and $\alpha = 1\ \mathrm{m^{2}\,s^{-1}}$:

| dimension | $dt_{\max}$ (s) | steps to reach $t = 1$ s |
|---|---|---|
| 1-D | $5.000\times10^{-5}$ | 20 000 |
| 2-D | $2.500\times10^{-5}$ | 40 000 |
| 3-D | $1.667\times10^{-5}$ | 60 000 |

For the working grid of §3.2 ($n = 64$, $h = 0.01538$ m) the explicit step is
$1.18\times10^{-4}$ s, so reaching $T = 0.1$ s takes $845$ steps against $10$
backward-Euler steps at $dt = 10^{-2}$ — an $85\times$ difference in step count.
Each implicit step costs a linear solve (tridiagonal in 1-D, banded in 2-D/3-D),
so the break-even is a function of the solver, the bandwidth and the parallel
efficiency: on a cache-friendly band matrix the implicit scheme usually wins; on
a short-vector accelerator with many independent right-hand sides, `spsolve` per
step can erase the advantage entirely. That calculation is
[19-06](../06-hpc-and-parallel-computing/README.md) territory, but the step
counts above are what feed it.

### 3.4 The wave CFL limit and its growth rate

For the leapfrog wave scheme, $G^{2} - 2bG + 1 = 0$ with
$b = 1 - 2C^{2}\sin^{2}(\theta/2)$. At $\theta = \pi$, $b = 1 - 2C^{2}$, so:

- $|b|\le1$ (i.e. $C\le1$) gives complex roots with $|G| = 1$: neutral;
- $C>1$ gives real roots, the larger of which is
  $|G| = \lvert b\rvert + \sqrt{b^{2}-1}$.

Starting in the pure eigenmode and measuring over 200 steps:

| $C$ | predicted $\lvert G\rvert$ | measured growth/step |
|---|---|---|
| 0.90 | 1.00000000 | 1.00000000 |
| 0.95 | 1.00000000 | 1.00000000 |
| 1.00 | 1.00000000 | 1.00000000 |
| 1.02 | 1.49083493 | 1.49083493 |
| 1.05 | 1.87732804 | 1.87732804 |
| 1.10 | 2.42816665 | 2.42816665 |

The limit is exactly one, and beyond it the growth is predicted in closed form —
which is what makes an unstable run *diagnosable* rather than merely broken. A
run whose measured growth is $1.88$ per step is a wave scheme at $C = 1.05$; a
run whose measured growth is $1.004$ is a diffusion scheme at $r = 0.501$. The
rate is a fingerprint.

### 3.5 Unconditional stability is not accuracy

The trapezoidal scheme has $|G| = 1$ for every $C$ and every mode: substituting
$b' = 1 - 2C^{2}\sin^{2}(\theta/2)$ into the discretisation gives a quadratic
with discriminant $-16C^{2}\sin^{2}(\theta/2)\le0$ and roots of modulus one.
Marching the same problem at five Courant numbers for $T = 0.5$ s:

| $C$ | amplitude ratio after 1000 steps | $L^{2}$ error against exact |
|---|---|---|
| 0.50 | 1.0000030253 | $1.097007\times10^{-2}$ |
| 1.00 | 0.9999999234 | $2.193949\times10^{-2}$ |
| 2.00 | 0.9999992979 | $4.359996\times10^{-2}$ |
| 5.00 | 0.9999762988 | $1.063203\times10^{-1}$ |
| 10.00 | 0.9999237054 | $2.031935\times10^{-1}$ |

The amplitude column is bounded at every $C$ — that is unconditional stability,
measured. The error column grows linearly in $C$: the scheme is stable and
useless above $C\approx2$ for this problem. **Stability buys the absence of
blow-up, never accuracy.** An implicit scheme's step size is set by the same
dispersion and truncation analysis as an explicit one; what changes is that the
*stability* constraint no longer sits underneath it.

## 4. Worked example: choosing a time step for a coupled diffusion problem

*A 2-D thermal model has $\alpha = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, a grid with
$h = 50$ m, and must run to $t = 10^{6}$ s. Compare an explicit and a
Crank–Nicolson march.*

1. Explicit limit: $dt \le h^{2}/(2\alpha d) = 2500/(2\times10^{-6}\times2)
   = 6.25\times10^{8}$ s — the limit is *not binding* here; the physical time is
   the binding constraint.
2. That is the interesting case: with $h$ large and $\alpha$ small, the explicit
   scheme is stable at huge steps and the real constraint is resolving the
   solution of interest. Choose $dt$ from the timescale you care about, say
   $dt = 10^{5}$ s, giving 10 steps to $10^{6}$ s.
3. Verification: at $dt = 10^{5}$ s and $h = 50$ m, $r = \alpha dt/h^{2} =
   0.04$, well inside the limit; but the truncation error in time is $O(dt)$ for
   FTCS, so run the same case with $dt = 10^{4}$ s and confirm the change in the
   answer is below your tolerance before believing the coarse run.
4. If the tolerance is not met, switch to Crank–Nicolson ($O(dt^{2})$) rather
   than refining the grid: the time error is what dominates in a
   diffusion-limited problem, and CN costs one tridiagonal solve per step.
5. Sanity check the diffusion number in three dimensions if the model is 3-D:
   the same $h$ and $\alpha$ give a limit only $(2/3)$ as large, because
   $dt_{\max}\propto1/d$.

## 5. Assumptions and regime of validity

1. **Constant coefficients and a uniform grid.** The limits $r\le1/2$ and
   $C\le1$ are for those cases. Variable coefficients keep the same form with
   the *maximum* diffusivity or speed, so heterogeneity makes the limit more
   restrictive, never less.
2. **Eigenmode measurements need eigenmodes.** The checkerboard on a periodic
   grid and the constructed leapfrog eigenmode are exact eigenvectors; general
   initial data give unreadable growth rates because two roots beat against each
   other.
3. **The order measured excludes the spatial error by construction.** Any other
   comparison (against a continuum solution at fixed $h$) mixes the two, and the
   smaller of the two errors hides the larger.
4. **Unconditional stability means "for this linear problem".** Nonlinear terms
   and variable boundary conditions can still destabilise an A-stable scheme;
   the linear analysis is a necessary condition.
5. **Round-off is not modelled.** At $C = 1$ the leapfrog scheme is neutral and
   accumulates round-off linearly in $n$; over $10^{5}$ steps this can dominate a
   small-amplitude solution.
6. **Implicit cost is not constant.** The step-count advantage of §3.3 is
   meaningless without the per-step work: a direct banded solve, an iterative
   solve and a preconditioned solve differ by orders of magnitude, and the
   comparison must be made for the actual solver.

## 6. Python demonstration

`code/fd_time_stepping_demo.py` prints:

1. the measured FTCS growth on both sides of $r = 1/2$, with the annihilating
   and neutral cases identified;
2. time-accuracy orders 1, 1 and 2 for FTCS, backward Euler and Crank–Nicolson
   measured against the exact semi-discrete solution;
3. the step counts implied by $dt_{\max} = h^{2}/(2\alpha d)$ and the
   explicit-versus-implicit step comparison;
4. the leapfrog CFL limit with measured growth rates matching
   $\lvert b\rvert+\sqrt{b^{2}-1}$;
5. the trapezoidal scheme's bounded amplitude and growing error up to $C = 10$.

```bash
cd 19-numerical-modeling-hpc/02-finite-difference-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_time_stepping_demo.py
```

## Mastery checkpoint

Without notes:

> A 3-D wave model with $c_{\max} = 4000\ \mathrm{m\,s^{-1}}$ runs on a grid with
> $h = 20$ m and is refined to $h = 10$ m. **(a)** Compute the explicit step limit
> before and after refinement and the change in step count for a fixed physical
> time. **(b)** State what an implicit scheme changes about that count and what
> it costs per step. **(c)** For a diffusion problem with the same $h$ and
> $\alpha = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, decide whether the explicit limit
> or the physical timescale binds, and justify with a number. **(d)** Explain why
> a run that is stable can still be wrong, with the measurement that
> demonstrates it.

Part (d) is worked in
[`exercises/04-fd-time-stepping-solutions.md`](exercises/04-fd-time-stepping-solutions.md).

## Common pitfalls

1. **Confusing stability with accuracy.** §3.5: amplitude ratio $0.9999$ and an
   error of $20\,\%$ in the same run.
2. **Working at the stability limit.** At $r = 1/2$ or $C = 1$ the highest mode
   is neutral; noise at the grid scale never leaves.
3. **Measuring growth from a generic initial condition.** Use an eigenmode, or
   you measure beating.
4. **Refining the grid to fix a time-stepping error.** The two errors are
   independent; identify which one dominates before spending anything.
5. **Assuming an implicit scheme needs fewer steps for accuracy.** It needs
   fewer steps for *stability*; accuracy sets its own step count.
6. **Ignoring the dimension factor.** $dt_{\max} \propto 1/d$; a 3-D run is
   three times more expensive per unknown than the same code in 1-D.

## Related modules

- [19-02-05 Finite-Difference Acoustic and Elastic Wave Propagation](05-fd-wave-propagation.md) —
  the CFL limit in practice, in two dimensions with absorbing boundaries.
- [19-02-06 FD for Diffusion, Laplace and Poisson Problems](06-fd-diffusion-and-potential.md) —
  what happens when the diffusion problem is solved in steady state instead.
- [19-06 High-Performance and Parallel Computing](../06-hpc-and-parallel-computing/README.md) —
  the cost model that decides explicit versus implicit.
- [01-12-06 Numerical ODE Solvers: Euler, Runge-Kutta, Implicit and Adaptive](../../01-mathematics/12-numerical-methods/06-ode-solvers.md).
- [Module 19-02 Finite-Difference Methods](README.md).

Exercises and worked solutions:
[`exercises/04-fd-time-stepping-exercises.md`](exercises/04-fd-time-stepping-exercises.md)
and
[`exercises/04-fd-time-stepping-solutions.md`](exercises/04-fd-time-stepping-solutions.md).
