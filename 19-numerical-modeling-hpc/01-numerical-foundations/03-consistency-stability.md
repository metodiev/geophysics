---
id: 19-01-03
title: "Consistency, Stability and the Lax Equivalence Theorem"
level: research
prereqs: ["19-01-02", "01-12-07", "03-12-02"]
tags: [numerical-modelling, hpc, consistency, stability, von-neumann, lax-equivalence]
---

# Consistency, Stability and the Lax Equivalence Theorem

Consistency says the scheme approximates the right equation. Stability says the
error does not grow. Together, for a linear well-posed problem, they imply
convergence — and that is the only reason a convergence study is worth running,
because it tells you in advance what to check when a run produces garbage. This
lesson derives the equivalence, then *measures* both halves: the truncation
residual that vanishes as the grid is refined, and the amplification factor that
either stays below one or grows at a rate predicted in closed form. **All models
and data in this module are SYNTHETIC.** Every number quoted here is printed by
`code/consistency_stability_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the local truncation error of the upwind scheme by applying it to
   the exact solution, and **identify** the diffusive correction it implies.
2. **Perform** a von Neumann analysis for a one-step scheme: insert a Fourier
   mode, obtain the amplification factor $G(\theta)$, and **solve** the
   stability inequality.
3. **Measure** the growth per step of an exact eigenmode and **compare** it with
   the analytic $|G|$, including the CFL $= 1$ case that is exactly neutral.
4. **State** the Lax equivalence theorem, sketch its proof, and **explain** the
   two hypotheses it needs.
5. **Produce** a convergent run and a divergent run of the same scheme and
   **measure** both rates: order one for the converged refinement, $|G|^{n}$ for
   the unstable one.
6. **Recognise** a consistent but unconditionally unstable scheme, and predict
   the number of steps to blow-up.

## Prerequisites

- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](02-convergence-and-error.md) —
  the truncation residual and the observed order used throughout.
- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](../../01-mathematics/12-numerical-methods/07-pde-discretisation.md) —
  the classical statement of the theorem and the von Neumann test.
- [03-12-02 Numerical Stability, CFL Conditions and Convergence Testing](../../03-scientific-computing/12-numerical-simulation-python/02-stability-and-cfl.md) —
  the same analysis implemented and instrumented in Python.

## 1. Intuition: three words that must not be confused

Take a scheme that is a good approximation of the right equation on every
individual step. Run it for a thousand steps. Two things can happen.

- Each step's residual, $O(h^{p})$, is added to the solution. If the scheme
  **amplifies** nothing, the total error after $T/dt$ steps is
  $(T/dt)\,O(h^{p}) = O(h^{p-1})$. Not convergent — but the *amplification* is
  exactly what converts local order into global order, and a stable scheme
  provides the missing factor of $h$.
- If the scheme does amplify some mode by a factor slightly above one, that
  factor compounds. A growth of $0.3\,\%$ per step over $200$ steps is a factor
  $1.8$; over $2000$ steps, $400$. Garbage that doubles per hundred steps looks
  like a solution for the first hundred.

Stability is therefore not a refinement of consistency; it is an independent
property, and neither implies the other. A scheme can be stable and
inconsistent (converging to the wrong equation) or consistent and unstable
(diverging from the right one). The Lax equivalence theorem says that together
they are enough.

## 2. Precise definitions

Let $u_t + a u_x = 0$ with $a > 0$ on a periodic domain, and let $U_j^n$ denote
the numerical approximation at $x_j = jh$, $t_n = n\,dt$.

**Upwind scheme.** The one-sided space difference follows the direction the
information comes from:

$$U_j^{n+1} = U_j^{n} - C\left(U_j^{n} - U_{j-1}^{n}\right),
\qquad C \equiv \frac{a\,dt}{h}.$$

$C$ is the **Courant number**. It is dimensionless, and every stability
statement below is a statement about it.

**Fourier mode.** Write $U_j^n = G^{n}e^{\mathrm i\theta j}$ with
$\theta = kh \in [-\pi,\pi]$. Substituting gives the **amplification factor**

$$G(\theta) = 1 - C\left(1 - e^{-\mathrm i\theta}\right).$$

**Von Neumann stability.** A scheme is von Neumann stable if
$|G(\theta)| \le 1$ for every $\theta$ and every $dt\le dt_{\max}$, i.e. the
error does not grow in the discrete $L^{2}$ norm. (For constant-coefficient
one-step schemes on a periodic domain this agrees with the general definition of
stability; with variable coefficients or boundaries it is necessary but not
sufficient.)

**Consistency.** With $\tau$ the residual obtained by applying the scheme to the
exact solution, the scheme is consistent of order $p$ if
$\|\tau\| = O(h^{p})$ as $h\to0$ along the refinement path.

**Convergence.** $\|U^n - u(\cdot,t_n)\| \to 0$ as $h\to0$, uniformly for
$0 \le t_n \le T$.

## 3. Derivations

### 3.1 Consistency of the upwind scheme

Apply the scheme to the exact solution $u = \sin\!\big(2\pi(x-t)\big)$ of
$u_t + u_x = 0$ with $a = 1$ on $[0,1]$ and define

$$R(x,t) = \frac{u(x,t+dt)-u(x,t)}{dt}
        + a\,\frac{u(x,t)-u(x-h,t)}{h}.$$

Expand in $dt$ and $h$. Since $u_{tt} = a^{2}u_{xx}$ along the characteristics,

$$R = \tfrac{1}{2}dt\,a^{2}u_{xx} - \tfrac{1}{2}a h\,u_{xx} + O(dt^{2},h^{2})
  = \frac{a h}{2}\left(C-1\right)u_{xx} + O(dt^{2},h^{2}).$$

At fixed $C$ the residual is $O(h)$ — the scheme is consistent, first order —
and $R/h$ approaches the finite limit $\tfrac{a}{2}(1-C)\,4\pi^{2}
\sin(2\pi(x-t))$. With $x_0 = 0.15$, $t_0 = 0.30$, $C = 0.5$ the limit is
$-7.98467769$ and the demonstration measures

| $h$ (m) | $dt$ (s) | $R$ (1/s) | $R/h$ | $(R/h - \text{limit})/h$ |
|---|---|---|---|---|
| 0.05000 | 0.02500 | $-4.38790754\times10^{-1}$ | $-8.77581508$ | $-15.8227$ |
| 0.02500 | 0.01250 | $-2.10272406\times10^{-1}$ | $-8.41089623$ | $-17.0487$ |
| 0.01250 | 0.00625 | $-1.02565270\times10^{-1}$ | $-8.20522161$ | $-17.6435$ |
| 0.00625 | 0.00313 | $-5.06048598\times10^{-2}$ | $-8.09677756$ | $-17.9360$ |
| 0.00313 | 0.00156 | $-2.51286894\times10^{-2}$ | $-8.04118062$ | $-18.0809$ |

The last column is drifting towards a constant, which is the signature of an
$O(h)$ approach to the limit. The structure of the residual is more informative
than its size: it is proportional to $u_{xx}$ and vanishes at $C = 1$. The
upwind scheme is a diffusion-like perturbation of advection, and at $C = 1$ the
perturbation disappears — which is exactly the case that will turn out to be
exact.

### 3.2 Von Neumann stability of the upwind scheme

With $z = e^{-\mathrm i\theta}$,

$$|G|^{2} = G\,G^{*} = 1 - 2C(1-C)(1-\cos\theta).$$

Because $1-\cos\theta \ge 0$, the condition $|G|\le1$ for all $\theta$ is

$$C(1-C) \ge 0 \qquad\Longleftrightarrow\qquad 0 \le C \le 1,$$

the classical CFL condition for upwind. For $C>1$ the most amplified mode is
$\theta = \pi$, where $\sin\theta = 0$ and

$$|G(\pi)| = |1-2C| \quad\Longrightarrow\quad
|G(\pi)|^{2} = 1 + 4C(C-1).$$

The demonstration starts each run in a *pure eigenmode* of amplitude
$10^{-6}$ — a state constructed so that only one root of the amplification
quadratic is present — and measures the growth per step:

| $C$ | $\theta/\pi$ | predicted $\lvert G\rvert$ | steps | measured growth/step |
|---|---|---|---|---|
| 0.50 | 0.50 | 0.70710678 | 20 | 0.70710678 |
| 0.50 | 1.00 | 0.00000000 | 1 | removed in one step |
| 0.90 | 1.00 | 0.80000000 | 20 | 0.80000000 |
| 1.00 | 0.50 | 1.00000000 | 20 | 1.00000000 |
| 1.00 | 1.00 | 1.00000000 | 20 | 1.00000000 |
| 1.20 | 1.00 | 1.40000000 | 200 | 1.40000000 |
| 1.50 | 1.00 | 2.00000000 | 200 | 2.00000000 |

Everything agrees to eight digits. Two entries deserve comment. At $C = 0.5$
and $\theta = \pi$, $G = 1 - 0.5(1-(-1)) = 0$: the scheme **annihilates** the
highest grid mode in a single step, and the measured relative amplitude after
one step is round-off ($4.0\times10^{-15}$). And at $C = 1$ the amplification is
exactly one for every mode — the boundary of stability, not a defect.

### 3.3 The Lax equivalence theorem

**Theorem (Lax, 1956).** Let $L_h$ be a consistent discretisation of a
well-posed linear initial-value problem. Then $L_h$ is convergent if and only if
it is stable.

**Proof sketch (the direction that matters).** Write one step as
$U^{n+1} = S\,U^{n} + dt\,\tau^{n}$, where $S$ is the update operator and
$\tau^{n}$ is the residual of §3.1 evaluated at the current (exact) state.
Subtract the same identity written for the exact solution:

$$e^{n+1} = S\,e^{n} + dt\,\tau^{n}
\qquad\Longrightarrow\qquad
e^{n} = \sum_{k=0}^{n-1} S^{n-1-k}\,dt\,\tau^{k}.$$

Stability says $\|S^{m}\|\le K$ for all $m$ with $m\,dt \le T$. Then

$$\|e^{n}\| \le K\,dt\sum_{k=0}^{n-1}\|\tau^{k}\|
             \le K\,T\,\max_k\|\tau^{k}\| = O(h^{p}),$$

because $n\,dt = T$. Consistency supplies the $O(h^{p})$ and stability supplies
the $K$ that stops the sum from accumulating. The converse direction — an
unstable scheme cannot converge — is the contrapositive: unbounded growth of
$\|S^{m}\|$ makes the same inequality impossible for *any* perturbation, and a
grid of finite precision always provides one.

Two hypotheses are doing real work: **linearity** (so that errors superpose) and
**well-posedness** of the continuous problem (so that a bounded scheme is
approximating something that has a unique solution).

### 3.4 Watching the theorem operate

**Stable and consistent: convergence at the order of the truncation error.**
Refining with $C = 0.5$ fixed, from the exact solution of the teaching problem,
the $L^{\infty}$ error at $t = 2$ s is

| $h$ (m) | steps | $L^{\infty}$ error | observed order |
|---|---|---|---|
| 0.05000 | 80 | $6.288118\times10^{-1}$ | — |
| 0.02500 | 160 | $3.898121\times10^{-1}$ | 0.689849 |
| 0.01250 | 320 | $2.187058\times10^{-1}$ | 0.833787 |
| 0.00625 | 640 | $1.160705\times10^{-1}$ | 0.913990 |
| 0.00313 | 1280 | $5.982196\times10^{-2}$ | 0.956254 |

The order approaches one from below, which is what a first-order scheme looks
like when the $O(h^{2})$ term is still present: $0.69, 0.83, 0.91, 0.96$. A
study that stopped after two grids would report $0.69$ and conclude something
was wrong.

**Stable only at the boundary: exactness at $C = 1$.** With $C = 1$ the update
becomes $U_j^{n+1} = U_{j-1}^{n}$, a shift by exactly one cell per step, and the
solution is exact for any initial data. After 100 steps the measured
$L^{\infty}$ error is $7.772\times10^{-16}$, i.e. round-off. This is the single
most useful sanity check in the whole lesson: if a code that claims to be
second-order is asked for $C = 1$ and does *not* reproduce a pure shift, the
stencil or the update order is wrong, and no convergence study is needed to
find out.

**Consistent and unstable: divergence at a predicted rate.** Running the same
scheme at $C = 1.2$ for 200 steps gives a predicted growth
$|G|^{200} = 1.681\times10^{+29}$ with $|G| = 1.40000000$ and a measured growth
of $1.681\times10^{29}$ from an initial $10^{-6}$. Unstable runs do not merely
fail; they fail at a rate you can compute in advance, which is how an unstable
run is diagnosed rather than discovered.

### 3.5 A consistent scheme that is unconditionally unstable

Replace the one-sided space difference by the centred one and keep forward
Euler in time:

$$U_j^{n+1} = U_j^{n} - \frac{C}{2}\left(U_{j+1}^{n}-U_{j-1}^{n}\right),
\qquad G = 1 - \mathrm i C\sin\theta.$$

The truncation error is now $O(h^{2})$ — this is a *more accurate* approximation
of the same equation — but

$$|G|^{2} = 1 + C^{2}\sin^{2}\theta > 1
\qquad\text{for every }\theta \ne 0,\pi.$$

The scheme is unconditionally unstable, and the demonstration confirms the
predicted rate at $\theta = \pi/2$:

| $C$ | predicted $\lvert G\rvert$ | measured growth/step | steps to grow $10^{6}\times$ |
|---|---|---|---|
| 0.25 | 1.03077641 | 1.03077641 | 455.8 |
| 0.50 | 1.11803399 | 1.11803399 | 123.8 |
| 1.00 | 1.41421356 | 1.41421356 | 39.9 |

A quarter Courant number buys five hundred steps before the error is a million
times larger — long enough to publish a paper if nobody checks. Higher spatial
order without stability is a trap, and the trap has a computable depth.

## 4. Worked example: diagnosing a run that produced nonsense

*A colleague's 1-D advection run with 400 cells explodes after about 60 steps.
The scheme is upwind, $a = 2\ \mathrm{m/s}$, $h = 5$ m, $dt = 0.02$ s, and the
initial condition contains a component at the grid scale.*

1. Courant number: $C = a\,dt/h = 2\times0.02/5 = 0.008$ — stable, so the
   explosion is *not* a CFL violation.
2. Highest mode growth: $|G(\pi)|^{2} = 1 + 4C(C-1) = 1 + 4(0.008)(-0.992)
   = 0.968$. The mode decays by $1.6\,\%$ per step. Nothing in the scheme can
   blow up.
3. Therefore the instability is elsewhere: look for a second, differently
   discretised term. A common cause is a source or boundary term updated
   *explicitly with the wrong sign* or a term differencing in the downwind
   direction. Downwind differencing of the same term has
   $|G|^{2} = 1 + 2C(1+C)(1-\cos\theta) > 1$ — the growth rate of an instability
   is itself a fingerprint, and the measured growth identifies which term is at
   fault.
4. Confirm with §3.2's eigenmode test: start the run in a single mode and measure
   the growth per step. If it does not match the prediction for the scheme you
   *think* you implemented, the implemented scheme is different from the
   intended one.

## 5. Assumptions and regime of validity

1. **Linear, constant coefficients, periodic.** The von Neumann test as
   performed here applies to that class exactly. For variable coefficients,
   boundaries and nonlinearity, $|G|\le1$ is necessary but not sufficient; a
   boundary can inject a growing mode with every interior mode neutral.
2. **One-step schemes.** Multi-step schemes such as leapfrog have a
   *matrix* amplification and can suffer defective roots: $|G|\le1$ for both
   roots while the solution still grows linearly (see
   [19-01-04](04-numerical-dispersion-diffusion.md) for the spurious root).
3. **The exact solution used is the exact solution of the teaching problem.**
   With a manufactured or measured initial condition instead, the residual
   contains its own error and the measured consistency order measures the data,
   not the scheme.
4. **Fixed Courant number.** Consistency was established along $dt \propto h$
   with $C$ constant. Refining $h$ alone while holding $dt$ changes the limit and
   the order.
5. **Round-off is not modelled.** The theorem's $K$ is a property of exact
   arithmetic; in floating point every unstable mode is eventually excited by
   round-off, which is why the initial perturbation amplitude in these
   experiments is $10^{-6}$ rather than zero: the experiment needs a mode to
   amplify.

## 6. Python demonstration

`code/consistency_stability_demo.py` prints every number quoted above:

1. the residual of the scheme applied to the exact solution, against its Taylor
   limit, with the difference falling like $h$;
2. measured growth per step of exact eigenmodes against $|G|$ from
   $G = 1 - C(1-e^{-\mathrm i\theta})$, including the annihilation at
   $(C,\theta) = (0.5,\pi)$ and the neutral boundary at $C = 1$;
3. a refinement study of the stable scheme (order approaching one), the
   divergence of the unstable one at $|G|^{200}$, and the exact-shift result at
   $C = 1$;
4. the unconditionally unstable centred scheme with its predicted growth and
   blow-up step count.

```bash
cd 19-numerical-modeling-hpc/01-numerical-foundations/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python consistency_stability_demo.py
```

## Mastery checkpoint

Without notes:

> A scheme for $u_t + a u_x = 0$ has $G(\theta) = 1 - C(1-\cos\theta)
> - \mathrm i C\sin\theta$ with $C = 1.4$. **(a)** Compute $|G(\pi)|$ and state
> how many steps it takes the highest mode to grow by $10^{12}$. **(b)** Is the
> scheme consistent? Justify with the truncation residual. **(c)** State what
> Lax equivalence concludes and what it does *not* conclude from these two
> facts about the finest grid you can afford. **(d)** Suggest one cheap
> modification that restores stability and state its cost.

The arithmetic for (a) and the discussion of (c) are in
[`exercises/03-consistency-stability-solutions.md`](exercises/03-consistency-stability-solutions.md).

## Common pitfalls

1. **Believing that higher order implies stability.** §3.5 is second-order
   consistent and unconditionally unstable.
2. **Checking stability on the wrong mode.** For upwind the least stable mode is
   $\theta = \pi$; for centred differences it is $\theta = \pi/2$. The
   demonstration reports which, because a stability scan over the wrong mode
   returns "stable" for an unstable scheme.
3. **Measuring growth from a general initial condition.** Robustness requires a
   pure eigenmode; with a general start the two roots of a multi-step scheme
   beat against each other and the growth rate is unreadable.
4. **Confusing neutral with accurate.** At $C = 1$ the scheme is exact and at
   $C = 1/2$ the highest mode is annihilated; neither fact transfers to other
   Courant numbers.
5. **Treating the CFL condition as a numerical detail.** It is the discrete
   statement of the domain of dependence: information may not travel more than
   one cell per step.
6. **Stopping the convergence study too early.** The observed orders
   $0.69 \to 0.96$ show what a two-grid study would have concluded.

## Related modules

- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](04-numerical-dispersion-diffusion.md) —
  what a stable scheme still gets wrong.
- [19-02-04 Explicit vs Implicit Time Stepping and Stability Limits](../02-finite-difference-methods/04-fd-time-stepping.md) —
  the same analysis for diffusion and for the wave equation with implicit
  alternatives.
- [20-02 Fourier and Spectral Analysis](../../20-signal-processing/02-fourier-and-spectral-analysis/README.md) —
  the Fourier tools used by the von Neumann test.
- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](../../01-mathematics/12-numerical-methods/07-pde-discretisation.md).
- [Module 19-01 Numerical Foundations for Simulation](README.md).

Exercises and worked solutions:
[`exercises/03-consistency-stability-exercises.md`](exercises/03-consistency-stability-exercises.md)
and
[`exercises/03-consistency-stability-solutions.md`](exercises/03-consistency-stability-solutions.md).
