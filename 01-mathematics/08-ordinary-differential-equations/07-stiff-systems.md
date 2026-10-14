---
id: 01-08-07
title: "Stiff Systems and Numerical Stability Challenges"
level: advanced
prereqs: ["01-08-01", "01-08-04"]
estimated_minutes: 90
tags: [stiff-systems, implicit-methods, a-stability, numerical-instability, diffusion]
---

# Stiff Systems and Numerical Stability Challenges

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** stiffness quantitatively — a large ratio of the fastest to the
   slowest timescale in a system — and explain why the definition is about
   *timescales*, not about non-linearity or about difficulty.
2. **Derive** the explicit Euler stability limit $h\lambda<2$ and explain why
   an implicit method removes it.
3. **Compute** stability functions $R(z)$ for explicit Euler, implicit Euler
   and the trapezoidal rule, and decide A-stability and L-stability from them.
4. **Estimate** the stiffness ratio of a diffusion problem as $O(N^2)$ from the
   discrete Laplacian's largest eigenvalue, and predict the explicit step limit
   $\Delta t\le \Delta x^2/(2\kappa)$.
5. **Explain** why implicit methods need a linear or non-linear solve per step,
   what Newton iteration costs, and when that cost is worth paying.
6. **Recognise** stiff systems in geophysics — thermal and chemical diffusion,
   magma and reaction kinetics, EM diffusion, and any multi-timescale coupling —
   and choose a method accordingly.

## Prerequisites

- [01 First-Order ODEs: Separation of Variables and Integrating Factors](./01-first-order-odes.md) —
  the model problem $y' = -\lambda y$ and the Euler method.
- [04 Systems of ODEs, Phase Portraits and Stability](./04-systems-of-odes.md) —
  the eigenvalue spectrum that defines the timescales.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../05-single-variable-calculus/04-taylor-series.md) —
  the Taylor expansions used to derive every stability function below.

## 1. Intuition: when the step size is set by a mode you do not care about

Suppose a system contains two processes: one that relaxes in microseconds and
one that evolves over days. You are interested in the days. An explicit method
must resolve the microseconds anyway, because it is unstable otherwise — so you
take $10^{11}$ steps to simulate one day of physics you could have modelled
with a hundred. That is stiffness, and it is not a pathology but the normal
condition of every diffusion and reaction problem in geophysics.

The engineering response is a family of methods that are stable for *any* step
size. They achieve this by solving an equation for the next state rather than
extrapolating to it, which costs a linear or non-linear solve per step. **The
trade is: one solve per step instead of a million steps.** This lesson makes
that trade quantitative.

Geophysical examples of stiff systems, all of which recur below:

| System | Fast timescale | Slow timescale of interest |
|---|---|---|
| Heat conduction on a fine grid | $\Delta x^2/\kappa$ | $L^2/(\pi^2\kappa)$ |
| Chemical or magma kinetics | a fast reaction rate | the cooling or crystallisation time |
| EM diffusion in a conductor | $\mu\sigma\Delta x^2$ | the survey's latest gate |
| Coupled atmosphere/ocean box | surface equilibration | deep-ocean adjustment |
| Mantle relaxation with a low-viscosity channel | channel relaxation | post-glacial rebound |

The mathematical content of all of them is the eigenvalue ratio of the
linearised system: **stiffness is a spectral property.**

## 2. Definitions

### 2.1 The test equation and the stiffness ratio

Everything follows from the model problem

$$y' = -\lambda y, \qquad \lambda>0,$$

whose solution decays with timescale $1/\lambda$. For a *system*
$\dot{\mathbf{y}} = A\mathbf{y}$, the relevant quantity is the spectrum of $A$,
and the system is called **stiff** if

$$S = \frac{\max_i|\operatorname{Re}\lambda_i|}{\min_i|\operatorname{Re}\lambda_i|}
\;=\; \frac{\tau_{\text{slow}}}{\tau_{\text{fast}}} \gg 1 .$$

For a non-linear system the same definition applies locally, using the
eigenvalues of the Jacobian $\partial\mathbf{f}/\partial\mathbf{y}$ evaluated on
the solution.

Three clarifications, because the word is used loosely in practice:

- **Stiffness is not non-linearity.** A linear problem can be arbitrarily stiff
  (Section 3.3 is linear).
- **Stiffness is not instability of the physical system.** All the modes above
  are decaying; the physics is perfectly stable, and only the *numerical*
  method is at risk.
- **Stiffness is a statement about timescales of interest.** A problem is stiff
  when the fastest timescale present is far shorter than the interval you need
  to simulate — a statement that includes the user, not only the equations.

### 2.2 Explicit and implicit Euler

**Explicit (forward) Euler:**

$$y_{n+1} = y_n + h\,f(t_n,y_n).$$

**Implicit (backward) Euler:**

$$y_{n+1} = y_n + h\,f(t_{n+1},y_{n+1}).$$

For the model problem these are $y_{n+1} = (1-h\lambda)y_n$ and
$y_{n+1} = y_n/(1+h\lambda)$, so the **amplification factors** are

$$R_{\text{exp}}(z) = 1+z, \qquad R_{\text{imp}}(z) = \frac{1}{1-z},
\qquad z = -h\lambda .$$

A method is **absolutely stable** at a given $z$ if $|R(z)|\le1$; its
**stability region** is the set of $z$ where that holds. The method is
**A-stable** if the stability region contains the whole left half plane — which
is exactly the set of decaying modes, so an A-stable method never amplifies
any physical decay, at any step size.

### 2.3 L-stability and why A-stability is not enough

A-stability permits $|R(z)|\to1$ as $z\to-\infty$. A method is **L-stable** if
$R(z)\to0$ as $z\to-\infty$: it does not merely avoid amplifying a very fast
mode, it annihilates it. This distinction decides whether a fast transient is
damped or rings, and Section 3.3 shows the difference quantitatively.

## 3. Derivations, step by step

### 3.1 The explicit stability limit

Impose $|1-h\lambda|\le1$:

$$-1 \le 1-h\lambda \le 1
\;\Longrightarrow\; 0 \le h\lambda \le 2 .$$

So explicit Euler is stable for the model problem exactly while
$h\lambda<2$, i.e. while the step is less than twice the fastest timescale. The
demonstration uses $\lambda = 100$ and integrates to $t=1$:

| method | $h$ | $h\lambda$ | $y(1)$ | stable? |
|---|---|---|---|---|
| explicit Euler | 0.020 | 2.0 | $1.000000\times10^{0}$ | yes (on the boundary) |
| explicit Euler | 0.022 | 2.2 | $-3.657\times10^{3}$ | no |
| explicit Euler | 0.019 | 1.9 | $-3.757\times10^{-3}$ | yes |
| explicit Euler | 0.010 | 1.0 | $0.000000\times10^{0}$ | yes |
| implicit Euler | 0.0200 | 2.0 | $1.393\times10^{-24}$ | yes |
| implicit Euler | 0.0100 | 1.0 | $7.889\times10^{-31}$ | yes |
| implicit Euler | 0.0001 | 0.01 | $6.113\times10^{-44}$ | yes |

Three readings, each worth stating explicitly:

1. **The boundary case is exactly on the boundary.** At $h\lambda = 2$ the
   amplification is $R = -1$: the solution oscillates with constant magnitude
   and never decays, so $y(1) = 1.000000$ rather than the exact
   $e^{-100} = 3.72\times10^{-44}$. Stable in the technical sense, useless in
   practice.
2. **Just past the boundary the method explodes.** At $h\lambda = 2.2$ the
   amplification is $-1.2$, so $|y|$ grows by $1.2$ per step over 45 steps, and
   the sign alternates. The output $-3.657\times10^{3}$ grows without bound.
3. **Implicit Euler is stable everywhere, and accurate at small $h$.** At
   $h\lambda = 0.01$ it reproduces the exact answer to three figures.

Note also what happens to the *error* at $h\lambda = 2$: the exact answer is
$10^{-44}$ and the numerical answer is 1. **A converged-looking solution can be
completely wrong in magnitude.** Stability analysis is not a luxury; it is the
first question to ask.

### 3.2 Stability functions, compared

The demonstration tabulates $R(z)$ against $\exp(z)$ for the three methods:

| $z=-h\lambda$ | $\exp(z)$ | explicit Euler | implicit Euler | trapezoidal |
|---|---|---|---|---|
| $-0.1$ | $9.048\times10^{-1}$ | $9.000\times10^{-1}$ | $9.091\times10^{-1}$ | $9.048\times10^{-1}$ |
| $-1.0$ | $3.679\times10^{-1}$ | $0$ | $5.000\times10^{-1}$ | $3.333\times10^{-1}$ |
| $-2.0$ | $1.353\times10^{-1}$ | $-1.000$ | $3.333\times10^{-1}$ | $0$ |
| $-2.1$ | $1.225\times10^{-1}$ | $-1.100$ | $3.226\times10^{-1}$ | $-2.439\times10^{-2}$ |
| $-10.0$ | $4.540\times10^{-5}$ | $-9.000$ | $9.091\times10^{-2}$ | $-6.667\times10^{-1}$ |
| $-1000.0$ | $\approx0$ | $-999.0$ | $9.990\times10^{-4}$ | $-9.960\times10^{-1}$ |

The trapezoidal rule (Crank–Nicolson) is
$R_{\text{trap}}(z) = (1+z/2)/(1-z/2)$, obtained by averaging the explicit and
implicit right-hand sides. Its accuracy is clearly the best at moderate $z$ —
at $z = -0.1$ it gives $0.904762$ against $\exp(-0.1) = 0.904837$, an error two
orders smaller than implicit Euler's. But its behaviour at large negative $z$ is
the trap:

$$\lim_{z\to-\infty}R_{\text{imp}}(z) = 0, \qquad
\lim_{z\to-\infty}R_{\text{trap}}(z) = -1 .$$

The demonstration prints $R(-10^{3}) = +9.99\times10^{-4}$ for implicit Euler
and $-0.996008$ for the trapezoidal rule, and $R(-10^{6}) = +10^{-6}$ and
$-0.999996$ respectively. **Both are A-stable; only one is L-stable.**

### 3.3 What L-stability buys: the ringing demonstration

Now make the consequence visible. Take $\lambda = 1000$, $h = 1$ so that
$h\lambda = 1000$, and step the model problem with both A-stable methods:

| step | $t$ | trapezoidal | implicit Euler | exact |
|---|---|---|---|---|
| 1 | 1 | $-9.960080\times10^{-1}$ | $9.990010\times10^{-4}$ | $\approx0$ |
| 2 | 2 | $9.920319\times10^{-1}$ | $9.980030\times10^{-7}$ | $\approx0$ |
| 5 | 5 | $-9.801986\times10^{-1}$ | $9.950150\times10^{-16}$ | $\approx0$ |
| 10 | 10 | $9.607894\times10^{-1}$ | $9.900548\times10^{-31}$ | $\approx0$ |
| 50 | 50 | $8.187305\times10^{-1}$ | $9.513\times10^{-151}$ | $\approx0$ |
| 100 | 100 | $6.703197\times10^{-1}$ | $9.049\times10^{-301}$ | $\approx0$ |

The exact solution at $t=100$ is $\exp(-10^5)$, which is zero to every double
precision digit. Implicit Euler is at $9\times10^{-301}$; the trapezoidal rule
is at $0.67$ and still alternating in sign. **A-stability prevented blow-up but
did not damp the fast mode, so the numerical solution is dominated by a
transient that physics has already forgotten.**

This is not a defect of the trapezoidal rule in general — it is second-order
accurate and excellent for wave problems. It is a defect *for stiff problems
where the fast mode must be damped*, and it is why backward Euler and the
backward-difference formulas are the default for diffusion and kinetics. The
diagnostic is a one-line computation of $R(z)$ at large negative $z$.

### 3.4 The stiffness of a diffusion problem, computed

Discretise $u_t = \kappa u_{xx}$ on $(0,L)$ with $N$ interior nodes at spacing
$\Delta x = L/(N+1)$ and the three-point stencil. The semi-discrete system is

$$\dot u_i = \frac{\kappa}{\Delta x^2}\left(u_{i-1}-2u_i+u_{i+1}\right),$$

which is $\dot{\mathbf{u}} = A\mathbf{u}$ with $A$ the (scaled) discrete
Laplacian. Its eigenvalues are

$$\lambda_k = -\frac{4\kappa}{\Delta x^2}\sin^2\!\left(\frac{k\pi\Delta x}{2L}\right),
\qquad k = 1,\dots,N,$$

so the extreme eigenvalues are

$$|\lambda|_{\max}\approx\frac{4\kappa}{\Delta x^2}, \qquad
|\lambda|_{\min} = \frac{4\kappa}{\Delta x^2}\sin^2\!\left(\frac{\pi\Delta x}{2L}\right)
\approx \frac{\kappa\pi^2}{L^2}.$$

Two conclusions follow immediately:

- **Explicit step limit:** $h \le 2/|\lambda|_{\max} \approx \Delta x^2/(2\kappa)$ —
  the step must scale with the *square* of the grid spacing, so refining the
  grid by 2 costs a factor of 4 in run time.
- **Stiffness ratio:** $S \approx (4/\pi^2)N^2 \approx 0.405\,N^2$ — quadratic in
  the number of grid points. **Refining a diffusion grid makes the problem
  stiffer, without limit.**

The demonstration uses $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$, $L=1$ m and
$N=200$ interior nodes ($\Delta x = 4.975\times10^{-3}$ m) and prints

$$|\lambda|_{\max} = 1.616040\times10^{-1}\ \mathrm{s^{-1}}, \qquad
|\lambda|_{\min} = 9.869604\times10^{-6}\ \mathrm{s^{-1}}, \qquad
S = 1.6374\times10^{4},$$

against the predicted $N^2/\pi^2 = 4052.8$ — the *ratio* of the two computed
values is $1.6374\times10^{4}$, which is larger than $N^2/\pi^2$ because the
smallest eigenvalue is not quite $\kappa\pi^2/L^2$ on a coarse grid. The
explicit limit is

$$h \le \frac{2}{1.616\times10^{-1}} = 12.3759\ \mathrm{s},$$

while the physical decay time is $L^2/(\pi^2\kappa) = 1.0132\times10^{5}$ s,
i.e. **1.17 days**. Covering one decay time explicitly therefore needs about
**8187 steps**, and this is for a one-dimensional problem with only 200 nodes.
In three dimensions with a million nodes the same argument gives a step limit
in the microseconds.

The demonstration then runs four schemes for the same physical time:

| scheme | $\Delta t$ (s) | max $u$ | min $u$ | verdict |
|---|---|---|---|---|
| explicit Euler | 12.376 | $8.876\times10^{-1}$ | $9.950\times10^{-3}$ | ok (on the limit) |
| explicit Euler | 13.614 | $2.241\times10^{10}$ | $-2.251\times10^{10}$ | **FAILED** |
| implicit Euler | 5000.000 | $3.094\times10^{-1}$ | $4.832\times10^{-3}$ | ok |
| Crank–Nicolson | 5000.000 | $3.069\times10^{-1}$ | $4.720\times10^{-3}$ | ok |

**Twenty implicit steps replace 8187 explicit ones**, and the implicit steps are
larger than the physical shortest timescale by a factor of 300. That is the
entire justification for implicit methods in geophysical modelling.

Two honest caveats. First, the implicit and Crank–Nicolson profiles after 20
steps of 5000 s differ by about 1 % because the step is far larger than any
accuracy requirement; stability bought speed, not accuracy. Second, the
Crank–Nicolson run stays physically admissible here because the initial
condition (a tent) is not sharp, but a *step* initial condition with such a
large step would overshoot below zero. **Accuracy and stability are separate
questions and neither implies the other.**

### 3.5 How the cost scales with refinement

The 1-D numbers above understate the problem, because they hold the node count
fixed. Increase the resolution of a fixed domain and the cost per physical decay
time grows as

$$\text{steps}\times\text{nodes} \;\propto\; \Delta x^{-2}\times\Delta x^{-d}
= \Delta x^{-(2+d)},$$

where $d$ is the spatial dimension. The demonstration tabulates both cases:

**2-D aquifer**, $D = 10\ \mathrm{m^{2}\,s^{-1}}$, $L = 4000$ m, so
$\lambda_{\min} = 2D\pi^{2}/L^{2} = 1.2337\times10^{-5}\ \mathrm{s^{-1}}$
(decay time 0.938 d):

| $\Delta x$ (m) | nodes | steps per $\tau$ | node-updates per $\tau$ | ratio |
|---|---|---|---|---|
| 100 | 1 600 | 162 | $2.594\times10^{5}$ | — |
| 25 | 25 600 | 2 594 | $6.640\times10^{7}$ | 256.0 |
| 6.25 | 409 600 | 41 501 | $1.700\times10^{10}$ | 256.0 |

**3-D thermal problem**, $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$,
$L = 1000$ m, so $\lambda_{\min} = 3\kappa\pi^{2}/L^{2}
= 2.9609\times10^{-11}\ \mathrm{s^{-1}}$ (decay time $3.38\times10^{10}$ s):

| $\Delta x$ (m) | nodes | steps per $\tau$ | node-updates per $\tau$ | ratio |
|---|---|---|---|---|
| 20 | $1.25\times10^{5}$ | 507 | $6.333\times10^{7}$ | — |
| 10 | $1.00\times10^{6}$ | 2 026 | $2.026\times10^{9}$ | 32.0 |
| 5 | $8.00\times10^{6}$ | 8 106 | $6.485\times10^{10}$ | 32.0 |
| 2.5 | $6.40\times10^{7}$ | 32 423 | $2.075\times10^{12}$ | 32.0 |

Every ratio is exactly the predicted power: $4^{4} = 256$ in two dimensions and
$2^{5} = 32$ in three. **In three dimensions, halving the grid spacing makes an
explicit diffusion run 32 times more expensive per unit of physical time.** That
single number is the strongest argument for implicit methods in geophysical
modelling, and it costs five minutes to compute — Section 7 of the companion
script does exactly that, and
[19-02-04 Explicit vs Implicit Time Stepping](../../19-numerical-modeling-hpc/02-finite-difference-methods/04-fd-time-stepping.md)
is where the resulting code architecture is discussed.

### 3.6 Reaction kinetics: the same structure without a grid

Diffusion is not the only source of stiff spectra. Consider the linear chain

$$\dot y_1 = -k_fy_1, \qquad \dot y_2 = k_fy_1 - k_sy_2,$$

with $k_f = 10^{6}\ \mathrm{s^{-1}}$ and $k_s = 1\ \mathrm{s^{-1}}$, so the
stiffness ratio is $10^{6}$. Physically this is a fast-responding intermediate
(a dissolved species buffered by a mineral, or a melt in local equilibrium with
crystals) feeding a slow reservoir. The exact solution is

$$y_1 = e^{-k_ft}, \qquad
y_2 = \frac{k_f\left(e^{-k_st} - e^{-k_ft}\right)}{k_f-k_s},$$

so $y_2(1) = 0.367879809051$. The demonstration integrates over $[0,1]$:

| method | $h$ | steps | $y_2(1)$ | relative error |
|---|---|---|---|---|
| explicit | $10^{-6}$ | 1 000 000 | 0.3678796251 | $5.0\times10^{-7}$ |
| explicit | $4\times10^{-6}$ | 250 000 | — | diverged |
| implicit | 0.1 | 10 | 0.3855436750 | $4.8\times10^{-2}$ |
| implicit | 0.01 | 100 | 0.3697115820 | $5.0\times10^{-3}$ |
| implicit | 0.001 | 1000 | 0.3680636724 | $5.0\times10^{-4}$ |

Read the last three rows for the accuracy story: the error falls by a factor of
ten when $h$ is divided by ten, which is **first-order convergence**, exactly as
the method's order promises. Read the first two rows for the stability story:
explicit Euler needs $h<2/k_f = 2\times10^{-6}$ s and fails at
$4\times10^{-6}$ s even though the timescale of interest is one second.

**Notice that the implicit error is an accuracy error, not a stability error.**
This is the distinction the lesson is built on: after the stability constraint is
removed, the remaining question is the ordinary truncation-error question, and
it is answered by a convergence study.

### 3.7 Nonlinear stiffness, Newton's method and conservation

Real kinetics are non-linear. The demonstration solves the **Robertson**
chemical-kinetics test problem, the standard benchmark for stiff solvers:

$$\dot y_1 = -k_1y_1 + k_3y_2y_3, \qquad
\dot y_2 = k_1y_1 - k_3y_2y_3 - k_2y_2^2, \qquad
\dot y_3 = k_2y_2^2,$$

with the published rate constants $k_1 = 0.04$, $k_2 = 3\times10^{7}$ and
$k_3 = 10^{4}$ (quoted as the standard values; every number computed from them
is produced by the script). The initial condition is $(1,0,0)$, and
$y_1+y_2+y_3$ is conserved.

Implicit Euler requires solving $\mathbf{G}(\mathbf{y}) = \mathbf{y}-\mathbf{y}_n
- h\mathbf{f}(\mathbf{y}) = 0$ at each step. Newton's method needs the Jacobian

$$\frac{\partial\mathbf{f}}{\partial\mathbf{y}} =
\begin{pmatrix}
-k_1 & k_3y_3 & k_3y_2\\
k_1 & -k_3y_3-2k_2y_2 & -k_3y_2\\
0 & 2k_2y_2 & 0
\end{pmatrix},$$

and each Newton step is a $3\times3$ linear solve (Cramer's rule in the script).
Results at $t = 40$:

| scheme | $h$ | $y_1(40)$ | $y_2(40)$ | $y_3(40)$ | $y_1+y_2+y_3$ |
|---|---|---|---|---|---|
| explicit Euler | 0.01 | FAILED | — | — | — |
| explicit Euler | 0.1 | FAILED | — | — | — |
| implicit + Newton | 0.01 | 0.715861987 | $9.1869\times10^{-6}$ | 0.284128826 | 1.000000000 |
| implicit + Newton | 0.1 | 0.716174955 | $9.1991\times10^{-6}$ | 0.283815846 | 1.000000000 |

Newton converges in an average of 2.88 iterations at $h = 0.01$ (worst case 9)
and 3.09 at $h = 0.1$ (worst case 13). The two step sizes, differing by a factor
of ten, give $y_1(40)$ values differing by $4.4\times10^{-4}$ relative — the
accuracy of a first-order method. **Mass is conserved to the Newton tolerance,
which is a property of the implicit formulation: the update satisfies the
discrete equation exactly once Newton has converged.**

Explicit Euler fails at both steps. The reason is in the Jacobian: the fast
eigenvalue scale is set by $-k_3y_3-2k_2y_2$, of order $10^{3}$–$10^{4}$, while
the slow dynamics evolve on a timescale of order $1/k_1 = 25$. The gap between
the step a method needs for *stability* and the step its *accuracy* needs is
the definition of stiffness, and Robertson is the canonical illustration.

## 4. Physical interpretation

**The stiff modes are usually the physically uninteresting ones.** In the
diffusion problem they are the grid-scale oscillations; in the kinetics problem
they are the fast equilibrium of an intermediate species; in EM diffusion they
are the earliest-time response. They must be *damped*, not resolved — which is
precisely what L-stable methods do and what A-stable-but-not-L-stable methods
fail to do.

**Cost accounting.** An implicit step costs one Jacobian evaluation, one
factorisation and a few Newton iterations; for a $N$-node one-dimensional
problem with a tridiagonal matrix that is $O(N)$ operations, and in three
dimensions a sparse solve is $O(N)$ to $O(N^{1.5})$ with a good ordering.
Compare that with $N^2$ extra explicit steps in one dimension. **Implicit wins
in one dimension, wins by more in two and three, and the margin grows as the
grid is refined** — which is why every production diffusion and geodynamic code
is implicit or semi-implicit.

**Semi-implicit and operator-splitting schemes.** Many geophysical codes treat
only the stiff part implicitly and the rest explicitly (IMEX schemes), or split
the operator into a linear stiff part and a non-linear smooth part. The
stability limit is then set by the *explicit* part, so the splitting must be
chosen with the spectrum in mind: putting the wrong term on the explicit side
reintroduces the very constraint the implicit treatment was meant to remove.

**Stiffness is a property of the model, not just of a discretisation.** A
chemical system with a fast reversible reaction is stiff even before any grid
exists. But discretising an elliptic or parabolic operator manufactures
stiffness out of nothing, and that manufactured stiffness is the most common
form in geophysics: the gradient of the operators of
[01-09-02](../09-partial-differential-equations/02-heat-equation.md) is what
sets the timescale ratio.

**What to watch for.** A run that produces a solution of the right magnitude
but with grid-scale oscillations is the classic signature of a method at the
edge of its stability limit. A run that needs a step far smaller than the
features you are interested in is the classic signature of stiffness. Both are
diagnosed before, not after, by computing the spectrum.

## 5. Python demonstration

The companion script is
[`code/stiff_systems_demo.py`](./code/stiff_systems_demo.py), standard library
only.

| Section | Claim being tested | Observed result |
|---|---|---|
| 1 | The explicit wall is at $h\lambda = 2$ | $h\lambda=1.9$ stable, $h\lambda=2.2$ gives $-3.657\times10^{3}$ |
| 2 | A-stability and L-stability differ | $R(-\infty) = 0$ for implicit Euler, $-1$ for the trapezoidal rule |
| 3 | Ringing from an A-stable method | at $t=100$: trapezoidal $6.7\times10^{-1}$, implicit Euler $9\times10^{-301}$ |
| 4 | Diffusion stiffness is $O(N^2)$ | $|\lambda|_{\max} = 1.616\times10^{-1}$, $S = 1.637\times10^{4}$; explicit limit 12.376 s vs 8187 steps per decay time |
| 4 | Implicit steps survive where explicit fails | 20 steps of 5000 s succeed; 13.614 s explicit diverges |
| 5 | Two-timescale kinetics | explicit needs $h<2\times10^{-6}$ s; implicit at $h=0.1$ in 10 steps |
| 6 | Robertson with Newton | mass conserved to $1.000000000$; Newton average 2.9 iterations; explicit fails |
| 7 | Cost scales as $\Delta x^{-(2+d)}$ | 2-D ratios $256 = 4^{4}$; 3-D ratios $32 = 2^{5}$ |
| 8 | The audit comes before the code | the checklist: $\lambda_{\max}$, $\lambda_{\min}$, their ratio, the step limit |

Section 4 is the one to reproduce by hand. Compute $4\kappa/\Delta x^2$,
$\kappa\pi^2/L^2$, their ratio and $2/(4\kappa/\Delta x^2)$, and check them
against the printed values. Then decide, for your own grid, whether an explicit
scheme is even conceivable; this is a five-minute calculation that regularly
saves a week of failed runs. Section 7 does the same thing for the
refinement question, and its two tables (one for two dimensions, one for three)
are the numbers behind Section 3.5.

> **Breaking exercise.** In Section 4, change $N$ from 200 to 400 and predict
> the new explicit step limit and the number of explicit steps needed per decay
> time before running. Check the factor against the predicted $1/N^2$ scaling.
> Then use Section 7's formula to predict the change in the *total* cost per
> decay time, which is a different and larger factor.

## 6. Exercises

Attempt these closed-book. See
[`exercises/07-stiff-systems-exercises.md`](./exercises/07-stiff-systems-exercises.md)
and the worked
[`exercises/07-stiff-systems-solutions.md`](./exercises/07-stiff-systems-solutions.md).

## 7. Common mistakes

1. **Believing that a small enough step is always the answer.** For stiff
   problems the required step is set by the fastest mode even when that mode is
   irrelevant, and the cost can be prohibitive.
2. **Choosing a method by its order alone.** The trapezoidal rule is second
   order and implicit Euler is first order, but on a stiff problem with a
   transient to damp, the first-order L-stable method can give a better answer.
   Order is an accuracy statement, not a stability one.
3. **Assuming A-stable means safe.** Section 3.3 is the counterexample: the
   ringing is $O(1)$ and never decays.
4. **Getting the sign of the damping term wrong in an IMEX split.** Put the
   stiff term on the implicit side; a sign error turns damping into growth.
5. **Forgetting that implicit methods need a solve.** The cost per step is not
   the function evaluation; it is the Jacobian, the factorisation and the
   Newton iterations, and for a non-linear problem convergence is not
   automatic.
6. **Using a loose Newton tolerance and interpreting the error as truncation
   error.** An unconverged Newton iteration adds an error that scales with the
   tolerance and does not shrink with $h$.
7. **Diagnosing stiffness from a plot.** Compute the eigenvalues, or at
   minimum compare the step you need with the timescales you care about.
8. **Assuming the physical problem is unstable because the code is.** Decaying
   modes cannot blow up; a growing numerical solution is a statement about the
   method.

## 8. Real-world applications

- **Thermal modelling of the crust and mantle.** Conduction on a fine grid is
  stiff by construction; every production code is implicit or uses a
  semi-implicit scheme. See
  [19-02-04 Explicit vs Implicit Time Stepping and Stability Limits](../../19-numerical-modeling-hpc/02-finite-difference-methods/04-fd-time-stepping.md)
  and [19-02-06 FD for Diffusion, Laplace and Poisson Problems](../../19-numerical-modeling-hpc/02-finite-difference-methods/06-fd-diffusion-and-potential.md).
- **Magma dynamics and crystallisation kinetics.** Crystal growth and
  melt–crystal equilibrium have reaction rates orders of magnitude faster than
  the cooling rate, so the coupled system is stiff and needs implicit or
  operator-split treatment. See
  [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md).
- **Chemical kinetics in reactive transport.** The Robertson problem of
  Section 3.7 is the prototype for reactive-transport models in aquifers and
  hydrothermal systems.
- **Electromagnetic diffusion.** The same parabolic operator appears in
  time-domain EM, where $\mu\sigma$ replaces $1/\kappa$; the step limit and the
  stiffness ratio have the same form. See
  [19-08-03 Simulating EM Diffusion in Conductive Media](../../19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/03-simulate-em-diffusion.md).
- **Post-glacial rebound and viscoelastic relaxation.** A low-viscosity
  asthenosphere and a high-viscosity lower mantle put a factor of $10^{4}$ or
  more between the fast and slow relaxation times. See
  [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md).
- **Coupled climate and carbon-cycle models.** The atmosphere–ocean–ice
  system is stiff because the surface equilibrates in months and the deep ocean
  in centuries.
- **Numerical software choice.** The distinction made here is exactly the one
  that separates the non-stiff solvers from the stiff solvers in general-purpose
  libraries, and picking the wrong family is a common cause of very slow runs
  with no error message.

## 9. Further reading

- **Hairer, E., & Wanner, G. *Solving Ordinary Differential Equations II: Stiff
  and Differential-Algebraic Problems.* Springer.** The definitive reference for
  stiff methods: stability theory, order barriers, stiffly accurate methods,
  BDF and implicit Runge–Kutta schemes. Level: graduate to doctoral.
- **Hairer, E., Nørsett, S. P., & Wanner, G. *Solving Ordinary Differential
  Equations I: Nonstiff Problems.* Springer.** The companion volume: the parts
  of the theory (order conditions, embedded error estimates) that the stiff
  volume assumes. Level: graduate.
- **Butcher, J. C. *Numerical Methods for Ordinary Differential Equations.*
  Wiley.** Stability functions, order conditions, and the general theory of
  Runge–Kutta methods, done rigorously. Level: advanced to graduate.
- **Gear, C. W. *Numerical Initial Value Problems in Ordinary Differential
  Equations.* Prentice Hall.** The classical account of BDF methods and
  stiffness, including the original definition of stiff stability. Level:
  graduate.
- **Trefethen, L. N., & Bau, D. *Numerical Linear Algebra.* SIAM.** Lectures 34
  and 37 on stability of ODE solvers, written with unusual clarity. Level:
  advanced.
- **LeVeque, R. J. *Finite Difference Methods for Ordinary and Partial
  Differential Equations.* SIAM.** The link from the model problem to
  grid-based diffusion, including the eigenvalue analysis of Section 3.4.
  Level: advanced.
- **Wanner, G., & Hairer, E. *Solving Ordinary Differential Equations* and the
  associated test-set literature.** The Robertson problem and the standard stiff
  test problems have a long published history as benchmarks; consult the
  numerical-analysis literature for reference solutions rather than trusting a
  single code.
- **Turcotte, D. L., & Schubert, G. *Geodynamics.* Cambridge University
  Press.** The relaxation-time analysis of viscoelastic and thermal problems,
  which is where the stiffness ratios in Section 8 come from.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted
> text, and you should confirm current editions and availability through your
> library before citing them yourself.

## 10. Related lessons

- [01 First-Order ODEs: Separation of Variables and Integrating Factors](./01-first-order-odes.md) —
  the model problem and the Euler method used throughout.
- [04 Systems of ODEs, Phase Portraits and Stability](./04-systems-of-odes.md) —
  where the eigenvalue spectrum that defines stiffness is computed.
- [06 Green's Functions and Impulse Response](./06-green-functions.md) —
  the continuum of relaxation times that makes a diffusion kernel stiff.
- [01-09-02 The Diffusion/Heat Equation](../09-partial-differential-equations/02-heat-equation.md) —
  the operator whose discretisation manufactures the stiffness analysed here.
- [01-12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md) —
  the wider family of numerical methods, of which this lesson covers one
  decisive case.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — the
  production setting: finite differences, implicit solves and performance.
- [19-02-04 Explicit vs Implicit Time Stepping and Stability Limits](../../19-numerical-modeling-hpc/02-finite-difference-methods/04-fd-time-stepping.md) —
  the same trade-off in the language of modelling codes.
- [19-08-03 Simulating EM Diffusion in Conductive Media](../../19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/03-simulate-em-diffusion.md) —
  stiffness with $\mu\sigma$ in place of $1/\kappa$.

## Self-assessment checklist

- [ ] I can define the stiffness ratio and compute it from a spectrum. (2.1)
- [ ] I can derive the explicit Euler limit $h\lambda<2$ and explain the
      boundary case. (3.1)
- [ ] I can compute $R(z)$ for explicit Euler, implicit Euler and the
      trapezoidal rule, and decide A-stability and L-stability. (3.2)
- [ ] I can demonstrate the ringing of an A-stable but not L-stable method.
      (3.3)
- [ ] I can estimate $\lambda_{\max}$ for a discrete Laplacian and predict the
      explicit step limit and the step count per physical decay time. (3.4)
- [ ] I can explain why refining a diffusion grid makes the problem stiffer.
      (3.4)
- [ ] I can write the Newton iteration for an implicit step of a non-linear
      system and say what each piece costs. (3.6)
- [ ] I can separate a stability error from an accuracy error in observed
      results. (3.5, Section 7.2)
