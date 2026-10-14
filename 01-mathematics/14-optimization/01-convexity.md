---
id: 01-14-01
title: "Convexity, Stationarity and Optimality Conditions"
level: advanced
prereqs: ["01-06-01", "01-07-07", "01-07-10"]
estimated_minutes: 90
tags: [optimization, convexity, optimality, inverse-problems]
---

# Convexity, Stationarity and Optimality Conditions

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the definitions of a convex set, a convex function and a strictly
   convex function, and test a given function against them using the chord
   (Jensen) inequality and the curvature condition.
2. **Derive** the first-order and second-order optimality conditions from a
   Taylor expansion, and explain why the first-order condition alone certifies
   nothing about the type of a critical point.
3. **Prove** that for a convex objective every local minimiser is a global
   minimiser, and use the proof to say exactly what a non-convex objective
   forfeits.
4. **Read** a Hessian spectrum as curvature: positive definite means a unique
   answer, positive semi-definite with a zero eigenvalue means an answer that is
   not unique, and an indefinite Hessian means a saddle or a maximum.
5. **Recognise** that a null space of the forward operator and a flat direction
   of the misfit are the same statement, and that both are the mathematical
   origin of inversion non-uniqueness.
6. **Identify**, in a geophysical misfit, the mechanism (phase wrapping, layer
   swapping, sign ambiguity) that destroys convexity, and predict how many
   basins the objective will have.

## Prerequisites

[01-06-01 Partial Derivatives](../06-multivariable-calculus/01-partial-derivatives.md)
for gradients and Hessians,
[01-07-07 Orthogonality, Projections and Least Squares](../07-linear-algebra/07-orthogonality.md)
for the normal equations and positive definiteness, and
[01-07-10 Matrix Calculus and Sensitivity Derivatives](../07-linear-algebra/10-matrix-calculus.md)
for the derivative identities used at $\nabla_m$ signs everywhere below.

## 1. Intuition: optimisation is inversion wearing different clothes

Almost every geophysical inversion is stated as a minimisation. Given data $d$
and a forward operator $G$, the question "which Earth model explains these data"
is turned into "which model makes the misfit smallest":

$$\phi(m) = \tfrac12\|G m - d\|^{2}, \qquad m^{*} = \arg\min_m \phi(m).$$

Nothing in that sentence guarantees that $m^{*}$ deserves the name. If $\phi$ is
**convex**, the minimiser exists, and if it is *strictly* convex there is exactly
one of it: the data determine the model completely within the chosen
parameterisation, and a search that finds *any* minimum has found *the* answer.
If $\phi$ is **non-convex**, the objective may have several local minima with
different misfit values, a continuum of equally good models, or both — and the
number you report becomes a statement about where your search started rather
than about the Earth.

This lesson builds the vocabulary that makes those statements precise. It is
placed here, at the start of the module, because everything that follows — the
descent methods of [01-14-02](./02-unconstrained.md), the bounds
of [01-14-03](./03-constrained.md), the least-squares algebra of
[01-14-04](./04-least-squares.md), the global searches of
[01-14-05](./05-global-optimization.md) — is a response to one of
the two cases. Convexity is not a technicality about algorithms; it is the
mathematical content of the sentence "this inverse problem has an answer".

The inverse-problems module takes the same story from the other end:
[01-18 Inverse Problems](../../18-inverse-problems/README.md) treats
non-uniqueness as a property of the operator, here it is a property of the
objective, and the two are the same statement expressed in different languages.
Lesson [01-07-04 Rank, Null Space and Solvability](../07-linear-algebra/04-rank-and-nullspace.md)
is the bridge: a null-space vector $n$ with $Gn = 0$ leaves the misfit unchanged.

## 2. Precise definitions

### 2.1 Convex sets

A set $C \subseteq \mathbb{R}^{n}$ is **convex** if for every $x, y \in C$ and
every $\theta \in [0, 1]$,

$$\theta x + (1 - \theta) y \in C.$$

Geometrically: the segment joining any two points of the set stays inside it. A
box $[\ell_1, u_1] \times \dots \times [\ell_n, u_n]$ — the parameter bounds a
practitioner typically imposes, densities between 2.0 and 3.2 g cm⁻³, say — is
convex. So is any affine subspace $\{m : Cm = d\}$, which is the form an equality
constraint takes. A *union* of two boxes is usually not convex, and that
distinction is exactly what makes the difference between bounded inversion and
multi-modal inversion.

### 2.2 Convex functions

A function $f : C \to \mathbb{R}$ on a convex set is **convex** if, for all
$x, y \in C$ and $\theta \in [0, 1]$,

$$f(\theta x + (1 - \theta)y) \le \theta f(x) + (1 - \theta) f(y). \tag{2.1}$$

This is the **chord inequality**: the graph lies below the chord. It is
**strictly convex** if the inequality is strict whenever $x \ne y$ and
$\theta \in (0, 1)$.

Two equivalent tests are used constantly.

**First-order test.** If $f$ is differentiable, convexity is equivalent to

$$f(y) \ge f(x) + \nabla f(x)^{\mathsf{T}}(y - x) \quad \text{for all } x, y \in C.
\tag{2.2}$$

The tangent plane is a global underestimate. In optimisation language, (2.2) is
what makes a local model trustworthy everywhere, and its absence is why
Gauss–Newton can take a violent step
([01-14-04](./04-least-squares.md), Section 5).

**Second-order test.** If $f$ is twice differentiable, convexity is equivalent to
the Hessian being positive semi-definite everywhere:

$$\nabla^{2} f(x) \succeq 0 \quad \text{for all } x \in C. \tag{2.3}$$

Strict convexity follows from $\nabla^{2} f(x) \succ 0$.

### 2.3 Jensen's inequality

For convex $f$ and a random variable $X$ with finite mean,

$$\mathbb{E}[f(X)] \ge f(\mathbb{E}[X]). \tag{2.4}$$

Equation (2.4) is (2.1) applied repeatedly, and it is the reason averaging a
nonlinear function and evaluating it at the average differ. For a concave
function the inequality reverses, which is a convenient numerical test: the sign
of the gap identifies the curvature.

### 2.4 Optimality conditions

Let $f$ be differentiable on an open set containing $m^{*}$.

*First-order necessary condition.* If $m^{*}$ is a local minimiser then

$$\nabla f(m^{*}) = 0, \qquad G^{\mathsf{T}} G m^{*} = G^{\mathsf{T}} d
\quad \text{for } f(m) = \tfrac12\|Gm - d\|^{2}. \tag{2.5}$$

*Second-order necessary condition.* If $m^{*}$ is a local minimiser then
$\nabla^{2} f(m^{*}) \succeq 0$.

*Second-order sufficient condition.* If $\nabla f(m^{*}) = 0$ and
$\nabla^{2} f(m^{*}) \succ 0$, then $m^{*}$ is a strict local minimiser.

The asymmetry in that list is the point of Section 3.3: a zero gradient is
necessary, never sufficient, and the curvature is what decides the type of the
critical point.

### 2.5 Convexity and uniqueness

**Theorem.** If $f$ is convex on the convex set $C$, every local minimiser is a
global minimiser. If $f$ is strictly convex, the global minimiser is unique.

*Proof.* Let $m^{*}$ be a local minimiser and suppose, for contradiction, that
some $y \in C$ has $f(y) < f(m^{*})$. For $\theta \in (0, 1]$ the point
$m^{*} + \theta(y - m^{*})$ is in $C$ by convexity, and (2.1) gives

$$f\bigl(m^{*} + \theta(y - m^{*})\bigr)
\le (1 - \theta)f(m^{*}) + \theta f(y)
= f(m^{*}) + \theta\bigl(f(y) - f(m^{*})\bigr) < f(m^{*}).$$

For arbitrarily small $\theta > 0$ this contradicts local minimality. The strict
case follows because equality in (2.1) for $f(x) = f(y)$ with $x \ne y$ would
require the strict inequality to fail. $\square$

The proof deserves to be read twice: it uses *only* the chord inequality. Every
guarantee in optimisation that does not assume convexity is a guarantee about
local behaviour, and the practical consequence is the possibility of two
different "answers" from two different starting models.

## 3. Step-by-step derivations

### 3.1 The first-order condition from Taylor's theorem

Expand $f$ about $m$ along a direction $p$ with step $\alpha$:

$$f(m + \alpha p) = f(m) + \alpha\, \nabla f(m)^{\mathsf{T}} p
+ \tfrac{1}{2}\alpha^{2} p^{\mathsf{T}} \nabla^{2} f(m) p
+ O(\alpha^{3}).$$

If $m$ is a local minimiser and $\nabla f(m)^{\mathsf{T}} p < 0$, then for
sufficiently small $\alpha$ the linear term dominates and $f(m + \alpha p) <
f(m)$; the same argument with $-p$ excludes $\nabla f(m)^{\mathsf{T}}p > 0$.
Since $p$ is arbitrary, $\nabla f(m) = 0$. This is a one-line derivation that
students often memorise as a fact; deriving it once makes clear that it says
nothing about the *size* of the curvature term, hence nothing about the type of
critical point.

### 3.2 Curvature of a least-squares misfit

For $\phi(m) = \tfrac12\|Gm - d\|^{2}$,

$$\nabla \phi(m) = G^{\mathsf{T}}(Gm - d), \qquad
\nabla^{2} \phi(m) = G^{\mathsf{T}} G .$$

The Hessian does not depend on $m$, so a linear least-squares misfit is exactly
a quadratic with curvature $G^{\mathsf{T}}G$: convex always, strictly convex
exactly when $G$ has full column rank. That is the sense in which linear
inversion is "easy": the difficulty is not convexity but conditioning, and
[01-07-05](../07-linear-algebra/05-determinants-inverses.md) already told us
what conditioning costs in digits.

### 3.3 A saddle satisfies the first-order condition

Take $f(x, y) = x^{2} - y^{2}$. Then $\nabla f(0,0) = (0, 0)$ — the first-order
condition holds — but the Hessian is
$\operatorname{diag}(2, -2)$, with eigenvalues $(-1, +1)$ for the scaled version
$\operatorname{diag}(1,-1)$ used in the demonstration. The point is a saddle.
Stationarity alone certifies nothing. In a geophysical context the saddle is not
exotic: it sits between two basins of a two-parameter model and is precisely
where a badly designed search stalls.

### 3.4 The misfit is flat wherever the null space is non-trivial

Let $n$ be a null vector, $Gn = 0$, and let $m$ be any model. Then

$$\phi(m + \alpha n) = \tfrac12\|Gm + \alpha Gn - d\|^{2} = \phi(m)
\quad \text{for every } \alpha.$$

The objective is *constant* along $n$, not merely stationary. This is the
mathematical origin of inversion non-uniqueness, and it is a stronger statement
than "the gradient vanishes at the minimum": the whole line of models is
equally good, and no amount of care in the minimiser will pick one of them
without extra information. Lesson
[01-07-04](../07-linear-algebra/04-rank-and-nullspace.md) derives the null
space; this lesson shows what it does to the objective function.

### 3.5 Where convexity is lost

A nonlinear forward operator $F(m)$ with misfit $\phi(m) = \tfrac12\|F(m) -
d\|^{2}$ has Hessian

$$\nabla^{2} \phi = J^{\mathsf{T}} J + \sum_i r_i \nabla^{2} F_i(m),
\qquad r = F(m) - d ,$$

where $J$ is the Jacobian. The first term is always positive semi-definite. The
second can be indefinite, and its size grows with the residuals: **far from the
solution, where the residuals are large, the misfit can be non-convex even when
it is convex near the solution.** This is why a Gauss–Newton iteration that
starts badly misbehaves (Section 5 of
[01-14-04](./04-least-squares.md)) and why continuation
strategies — start with a smoothed, nearly convex objective, then sharpen it —
are standard practice in seismic inversion.

## 4. Numerical results

Everything quoted below comes from
[`code/convexity_demo.py`](./code/convexity_demo.py). Run it and check the
numbers.

### 4.1 The chord test

| Function | Largest chord violation | Verdict |
|---|---|---|
| $x^{2}$ on $[-2,2]$ | $0.000\times10^{0}$ | convex |
| $e^{x}$ on $[-1,1]$ | $0.000\times10^{0}$ | convex |
| $\cosh x$ on $[-1,1]$ | $0.000\times10^{0}$ | convex |
| $1 - \cos x$ on $[-1.5,1.5]$ | $0.000\times10^{0}$ | convex |
| $1 - \cos x$ on $[-3,3]$ | $2.027\times10^{-1}$ | not convex |
| $x^{4} - 3x^{2}$ on $[-2,2]$ | $2.250\times10^{0}$ | not convex |
| $\sin x$ on $[0,\pi]$ | $1.000\times10^{0}$ | not convex |

The $1-\cos x$ pair is the instructive one: the *same function* is convex on
$[-\pi/2, \pi/2]$ and non-convex outside it, because
$(1-\cos x)'' = \cos x$ changes sign at $\pm\pi/2$. The demonstration's cosine
misfit in Section 6 lives on exactly this behaviour. Jensen's inequality gives
the same information numerically: for $X \sim U[0,1]$, $\mathbb{E}[X^{2}] =
0.333333$ against $(\mathbb{E}X)^{2} = 0.250000$, a gap of $+0.083333$; for
$-x^{2}$ the gap is $-0.083333$, the sign flagging concavity.

A caveat the demonstration states: sampling a grid of chords can *falsify*
convexity but never proves it, since the inequality must hold for all pairs. The
sampled test is a diagnostic; the analytic second-derivative test is the proof.

### 4.2 Curvature of a five-ray cross-hole kernel

A SYNTHETIC five-ray, three-cell travel-time problem with residuals
$d = (0.0310, 0.0296, 0.0620, 0.0300, 0.0460)$ s gives

$$G^{\mathsf{T}}G \;\text{eigenvalues} = (5.397682,\ 1.892608,\ 0.000110),
\qquad \kappa = 49\,014.29 .$$

All three are positive, so the misfit is strictly convex and the model is
unique — but the smallest eigenvalue is $1.1\times10^{-4}$, four orders of
magnitude below the largest. The consequence is not non-uniqueness but
*uncertainty*: the associated model direction is determined to about
$1/\sqrt{1.1\times10^{-4}}$ of the precision of the others. Convexity gives
uniqueness; it does not give precision. At the minimiser the demonstration
reports $\|\nabla\phi(m^{*})\| = 1.948\times10^{-16}$ — the first-order
condition satisfied to round-off, and the strongest numerical statement one can
make about a stationary point.

The chord test applied along a random direction of that same misfit is violated
by at most $2.220\times10^{-16}$, i.e. not at all: the objective is an exact
quadratic and the test finds only round-off.

### 4.3 A non-convex misfit and where descent lands

For $f(m) = m^{4} - 2m^{2} + 0.3m$ (a layer thickness in km) a fine grid finds
two local minima,

| $m$ (km) | $f(m)$ | $f''(m)$ |
|---|---|---|
| $-1.035600$ | $-1.30542848$ | $+8.869608$ |
| $+0.960100$ | $-0.70585351$ | $+7.061504$ |

and Newton's method from three starting models locates three different critical
points: $m = -1.03557871$ (minimum, $f'' = +8.869079$), $m = 0.07542916$ (a
**maximum**, $f'' = -3.931725$), and $m = 0.96014956$ (minimum, $f'' =
+7.062646$). The middle case is the honest lesson of the section: a second-order
method converges to whatever critical point is in reach, and without a curvature
check you would report a maximum as a model. The depth of the two minima differs
by a factor of $1.85$, so the choice between them is not a detail.

### 4.4 Non-uniqueness as a flat valley

With a kernel whose first two columns are identical ($Gn = 0$ for
$n = (1,-1,0)$), the demonstration evaluates the misfit at
$m_0 + \alpha n$ for $\alpha \in \{-2,-1,0,1,2\}$:

| $\alpha$ | model (s/km) | misfit |
|---|---|---|
| $-2.0$ | $(-1.9700, +2.0000, +0.0620)$ | $7.704\times10^{-34}$ |
| $-1.0$ | $(-0.9700, +1.0000, +0.0620)$ | $7.704\times10^{-34}$ |
| $0.0$ | $(+0.0300, +0.0000, +0.0620)$ | $0.000\times10^{0}$ |
| $+1.0$ | $(+1.0300, -1.0000, +0.0620)$ | $7.704\times10^{-34}$ |
| $+2.0$ | $(+2.0300, -2.0000, +0.0620)$ | $3.775\times10^{-32}$ |

The misfit is constant to round-off while the model norm ranges from $0.069$ to
$2.85$ s/km — a factor of 41. The eigenvalues of $G^{\mathsf{T}}G$ for this
kernel are $(0.000000, 1.000000, 4.000000)$: one zero, so the objective is convex
but *not* strictly convex, and the minimiser exists but is not unique. Rank
deficiency and objective flatness are one phenomenon.

### 4.5 The same geometry in a real-style seismic misfit

A two-parameter cycle-skipped misfit built from arrival times
$t = x/v_1 + x^{2}/(4v_2)$ at offsets $x = 1,2,3,4$ km, with the phase wrapped
every $0.5$ s, has four local minima on $v \in [1.5, 8.0]$ km/s:

| $v$ (km/s) | misfit |
|---|---|
| $1.73680$ | $2.502116$ |
| $2.18970$ | $2.997575$ |
| $3.00000$ | $0.000000$ (the true velocity) |
| $4.76230$ | $2.997575$ |

Damped descent from $v = 5.0$ km/s converges to $v = 4.76233$ km/s with misfit
$2.997575$ — a local minimum whose misfit is *three times* the value at the
truth. This is the archetypal seismic-inversion failure mode: the algorithm
converged, the residual is finite and unremarkable, and the model is wrong. The
misfit's four basins are the direct consequence of the cosine's periodicity,
which is the same mechanism as the $1-\cos x$ transition to non-convexity in
Section 4.1.

## 5. Physical interpretation

**Convexity is the statement that the data contain one answer.** For a linear
problem convexity is automatic and adds nothing; what matters there is
conditioning. For a nonlinear problem convexity is a real, often false,
assumption, and the honest framing is: *the misfit is convex on the part of
model space your starting model can reach.*

**Curvature is resolution.** The Hessian of the misfit is, up to a factor, the
inverse of the model covariance. A direction with small curvature is one the data
barely constrain; a direction with zero curvature is one they do not constrain
at all. Reading eigenvalues is therefore not a numerical formality — it is how
you answer "which part of this model is the data actually testing?", the same
question the singular-value decomposition answers for linear problems in
[01-07-08](../07-linear-algebra/08-svd.md).

**Non-uniqueness comes in two flavours, and they are distinguishable.** A null
space gives a *connected, flat* valley of equally good models: the objective
cannot choose. Multiple basins give *separated* minima of different misfit
values: the objective prefers one, but a local search may not find it. Theory
distinguishes them (rank deficiency versus non-convexity); practice distinguishes
them by running a local search from several starts and looking at whether the
misfit values agree.

**Smoothing changes the geometry, not the physics.** Many operational codes
minimise a smoothed misfit and then sharpen it, because a smoothed objective is
closer to convex. That is legitimate — it is a continuation method — but it is a
statement about the *objective*, and the resulting model is a minimum of the
objective you actually minimised.

## 6. Assumptions and regime of validity

1. **Convexity is a property of your objective, not of the Earth.** Re-parameterise
   the model and the geometry can change: minimising over $\ln v$ instead of $v$
   turns some non-convex travel-time misfits into convex ones, and vice versa.
   Say which parameterisation you are claiming convexity in.
2. **The second-order sufficient condition is local.** Even with
   $\nabla^{2}\phi \succ 0$ at a point, the objective may be non-convex far away.
   Nothing about the Hessian at $m^{*}$ constrains what happens at another
   starting model.
3. **Numerical curvature is not analytic curvature.** The smallest eigenvalue of
   the five-ray kernel is $1.1\times10^{-4}$ in double precision. If the problem
   were larger or more weakly constrained, that eigenvalue would fall below
   $\epsilon_{\text{mach}}\lambda_{\max}$ and the computed Hessian would lose it
   altogether — the same failure mode that
   [01-14-04](./04-least-squares.md) demonstrates for $G^{\mathsf{T}}G$.
4. **Round-off changes the answer in a flat valley.** Where curvature is
   $\sim10^{-34}$ (Section 4.4), the "minimiser" is whatever the arithmetic
   happens to produce. Reporting it to eight figures is a misuse of the model,
   not a property of the data.
5. **The chord test only falsifies.** A sampled chord test cannot establish
   convexity; use it to find counterexamples, and prove with derivatives.
6. **Bounds and equalities change nothing here.** Constrained versions of these
   conditions require the KKT framework of
   [01-14-03](./03-constrained.md); the curvature conditions
   below

are stated on the active set, and the unconstrained statements above are the
special case where no constraint is active.

## 7. Python demonstration

The companion script is
[`code/convexity_demo.py`](./code/convexity_demo.py). It uses only the Python
standard library: the Jacobi eigensolver and the Gaussian elimination are
written out, so the script is a self-contained reference implementation.

| Section | Measured | Interpretation |
|---|---|---|
| 1, chord test | violations $0$ for $x^{2}$ and $\cosh x$; $2.03\times10^{-1}$ for $1-\cos x$ on $[-3,3]$ | the same function can be convex on one interval and not on another |
| 1, Jensen | gap $+0.083333$ for $x^{2}$, $-0.083333$ for $-x^{2}$ | the sign of the gap identifies the curvature |
| 2, spectrum | eigenvalues of $G^{\mathsf{T}}G$: $5.397682$, $1.892608$, $0.000110$ | strictly convex, condition number $49\,014.29$ |
| 2, stationarity | $\|\nabla\phi(m^{*})\| = 1.948\times10^{-16}$ | first-order condition satisfied to round-off |
| 2, chord in 3-D | maximum violation $2.220\times10^{-16}$ | an exact quadratic is convex, as theory requires |
| 3, grid | two minima: $f(-1.0356) = -1.30542848$, $f(0.9601) = -0.70585351$ | objective values differ by $1.85\times$ |
| 3, Newton | three starts, three critical points, one a maximum ($f'' = -3.931725$) | stationarity must be paired with a curvature check |
| 4, flat valley | identical misfit ($7.7\times10^{-34}$) for five models | a null vector makes the objective exactly flat |
| 5, saddle | Hessian eigenvalues $(-1, +1)$ at a stationary point | first-order condition holds, minimum it is not |
| 6, seismic | four local minima; descent from $5.0$ reaches $4.76233$ km/s, misfit $2.997575$ | convergence is not correctness |

> **Breaking exercise.** In Section 6, change the period from $0.5$ s to $2.0$ s
> and predict, before running: (a) whether the number of local minima falls, (b)
> whether the misfit at $v = 3.0$ km/s is still zero, and (c) whether descent
> from $5.0$ km/s now reaches the truth. Then run it. The answer to (c) is the
> one that matters in practice: the geometry of the misfit is a property of the
> data's frequency content.

## 8. Exercises

Full set and worked solutions:
[`exercises/01-convexity-exercises.md`](./exercises/01-convexity-exercises.md)
and
[`exercises/01-convexity-solutions.md`](./exercises/01-convexity-solutions.md).
Four to start with:

**★1.** Show by direct substitution that $f(m) = \tfrac12 m^{\mathsf{T}}A m -
b^{\mathsf{T}}m$ with $A$ symmetric positive definite satisfies the chord
inequality, and identify its minimiser.

**★2.** For $\phi(m) = \tfrac12\|Gm - d\|^{2}$, derive $\nabla\phi$ and
$\nabla^{2}\phi$, and state precisely when the minimiser is unique.

**★★3.** A two-cell kernel has columns $g_1 = (1, 0)^{\mathsf{T}}$ and
$g_2 = (1, 0)^{\mathsf{T}}$. Write down every model fitting the data
$d = (0.02, 0.02)^{\mathsf{T}}$ exactly, and state the misfit at each.

**★★4.** Construct a one-parameter misfit with exactly three local minima,
compute them, and say what data-acquisition change would remove one of them.

## 9. Common mistakes

1. **Reporting a stationary point as a model.** Section 4.3 converged to a
   maximum with $f'' = -3.93$; the check costs one line and is routinely skipped.
2. **Confusing convexity with conditioning.** The five-ray kernel is strictly
   convex with $\kappa = 49\,014$; unique does not mean precise.
3. **Reading "the solver converged" as "the model is right".** The cycle-skipped
   example converged to a misfit three times the global minimum.
4. **Testing convexity numerically and calling it proved.** A chord test over a
   grid of samples can only falsify.
5. **Assuming that a linear problem is automatically easy.** Linear least squares
   is convex and can still be numerically singular
   ([01-14-04](./04-least-squares.md), Section 2).
6. **Forgetting that the parameterisation is yours.** Convexity statements are
   relative to the variables chosen.
7. **Ignoring the scale of the smallest eigenvalue.** A curvature of
   $10^{-34}$ is not a small number, it is a statement that the direction is
   unconstrained by the data at double precision.

## 10. Real-world applications

- **Travel-time tomography.** The misfit is convex in slowness for fixed ray
  paths; updating the ray paths with the model makes it mildly non-convex, which
  is why tomographic codes iterate between ray tracing and inversion.
- **Full-waveform inversion.** Cycle skipping is the cosine effect of Section 4.5
  operating on waveforms. The entire low-frequency-acquisition debate in the
  seismic industry is a debate about the geometry of the misfit.
- **MT and potential-field inversion.** Nonlinear in layer thicknesses and
  conductivities; the sign and thickness ambiguities are genuine null-space
  directions, and the standard remedy is to fix a subset of parameters (an
  equal-constraint problem) rather than to search harder.
- **Reservoir history matching.** Convex in the linearised (gradient) problem and
  strongly non-convex in the nonlinear one, which is why ensemble methods and
  multiple starting models dominate practice.
- **Machine-learning training.** The loss surfaces of neural networks are
  non-convex; the same saddle, plateau and basin vocabulary applies, and the same
  distinction between a critical point and a minimum.

## 11. Further reading

- **Nocedal, J., & Wright, S. J. *Numerical Optimization* (2nd ed.). Springer.**
  Chapters 2–3. Level: graduate. The standard treatment of optimality
  conditions; Chapter 3 covers the convex case in full rigour.
- **Boyd, S., & Vandenberghe, L. *Convex Optimization*. Cambridge University
  Press.** Chapters 2–5. Level: graduate. The reference for convex sets,
  functions, duality and the practical meaning of the conditions used here.
  Available from the authors' university page.
- **Rockafellar, R. T. *Convex Analysis*. Princeton University Press.** Level:
  research. The rigorous source, including convexity without differentiability.
- **Tarantola, A. *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: graduate. Inversion as minimisation, with the
  misfit function and its curvature as the central objects.
- **Aster, R. C., Borchers, B., & Thurber, C. H. *Parameter Estimation and
  Inverse Problems.* Academic Press.** Level: intermediate to advanced. The
  geophysical framing of convexity, uniqueness and resolution.

> Note on citations: bibliographic details above are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text, and you
> should confirm editions and current availability through your library before
> citing them yourself.

## 12. Self-assessment checklist

- [ ] I can state the chord inequality and the first- and second-order convexity
      tests, and say which is easiest to check in practice.
- [ ] I can derive the first-order optimality condition from a Taylor expansion
      and explain why it does not classify a critical point.
- [ ] I can prove that for a convex objective every local minimum is global.
- [ ] I can read a Hessian spectrum and translate it into uniqueness, uncertainty
      or a saddle.
- [ ] I can explain why a null vector makes the misfit exactly constant along a
      line, and connect that to inversion non-uniqueness.
- [ ] I can construct a non-convex geophysical misfit and predict the number of
      basins from the data's periodicity.
- [ ] I can distinguish "unique but ill-conditioned" from "non-unique", with
      numbers for both.

## 13. Related lessons

- [01-14-02 Unconstrained Minimisation](./02-unconstrained.md) —
  what to do once you know the geometry: gradient, Newton and quasi-Newton.
- [01-14-03 Constrained Optimisation and Lagrange Multipliers](./03-constrained.md) —
  optimality conditions when the model is restricted to a feasible set.
- [01-14-04 Linear and Nonlinear Least Squares](./04-least-squares.md) —
  the convex misfit that geophysics uses most, and its conditioning.
- [01-14-05 Global Optimisation](./05-global-optimization.md) —
  what to do when the objective has several basins.
- [01-07-04 Rank, Null Space and Solvability](../07-linear-algebra/04-rank-and-nullspace.md) —
  the null space whose objective counterpart is Section 4.4.
- [01-07-05 Determinants, Inverses and Matrix Conditioning](../07-linear-algebra/05-determinants-inverses.md) —
  why uniqueness and precision are different questions.
- [01-18 Inverse Problems](../../18-inverse-problems/README.md) — non-uniqueness
  stated as a property of the operator rather than of the misfit.
