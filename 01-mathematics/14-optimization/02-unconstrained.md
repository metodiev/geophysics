---
id: 01-14-02
title: "Unconstrained Minimisation: Gradient, Newton, Quasi-Newton"
level: advanced
prereqs: ["01-14-01", "01-07-06", "01-07-10"]
estimated_minutes: 90
tags: [optimization, gradient-descent, newton-method, quasi-newton]
---

# Unconstrained Minimisation: Gradient, Newton, Quasi-Newton

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the steepest-descent, Newton and BFGS steps from the local
   quadratic model, and say what each one assumes about the objective.
2. **Explain** why the iteration count of steepest descent on a quadratic grows
   in proportion to the condition number, and predict that count from
   $\kappa$ and the target tolerance.
3. **Measure** a convergence rate from an error sequence, and compare the
   measured rate with the bound $(\kappa - 1)/(\kappa + 1)$.
4. **Choose** between a damped Newton step, a line search, and a
   Levenberg–Marquardt interpolation, and justify the choice from the curvature.
5. **Implement** BFGS with a line search using only the standard library, and
   state its cost in gradient evaluations relative to Newton.
6. **Recognise** that a finite-difference gradient limits the achievable model
   accuracy, and estimate that limit.

## Prerequisites

[01-14-01 Convexity, Stationarity and Optimality Conditions](./01-convexity.md)
for the optimality conditions and curvature language, and
[01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md)
for the spectral radius reasoning that the convergence analysis uses.

## 1. Intuition: the engine inside every inversion code

A linear inversion solves a linear system. A *nonlinear* inversion cannot: there
is no system to solve, only a misfit to reduce. What every such code does is
choose a direction and a step length, repeatedly, until the gradient is small.
The vocabulary of this lesson — steepest descent, Newton, quasi-Newton, line
search, damping — is the vocabulary of the "solve" step in
[01-18 Inverse Problems](../../18-inverse-problems/README.md), and the difference
between them is entirely a matter of how much curvature information they use.

Three sentences summarise the trade:

- **Steepest descent** uses only the gradient. Each step is cheap and the
  iteration count is proportional to the condition number — three orders of
  magnitude of conditioning costs three orders of magnitude of iterations.
- **Newton** uses the Hessian. On a quadratic it converges in one step and on
  anything smooth it converges quadratically near the solution, but one step
  costs a linear solve and the undamped step can leave the basin entirely.
- **Quasi-Newton** builds an approximation to the Hessian out of the gradients
  it has already computed. It converges superlinearly in practice at roughly the
  cost per step of steepest descent. That is why it is the default in production
  inversion codes, and why it is the method you should be able to implement.

The single most important number in the lesson is the ratio of the objective's
largest to smallest curvature, $\kappa$. Everything else is bookkeeping.

## 2. Precise definitions

### 2.1 The local quadratic model

About a point $m$, a twice-differentiable objective has the model

$$q(p) = f(m) + g^{\mathsf{T}}p + \tfrac12 p^{\mathsf{T}} H p,
\qquad g = \nabla f(m),\ H = \nabla^{2} f(m). \tag{2.1}$$

Every method in this lesson differs only in how it uses $(g, H)$ in (2.1).

### 2.2 The three step directions

**Steepest descent.** Minimise the *linear* model under a constraint on the step
length; the answer is the negative gradient,

$$p_{\text{sd}} = -g. \tag{2.2}$$

Equivalently: the direction of greatest decrease per unit Euclidean length.

**Newton.** Minimise the quadratic model (2.1) exactly:

$$p_{\text{N}} = -H^{-1} g. \tag{2.3}$$

For an exactly quadratic objective with $H \succ 0$ this reaches the minimiser in
one step; otherwise it is a local model and the step may be too long.

**Quasi-Newton (BFGS).** Replace $H^{-1}$ by a matrix $B_k$ updated from the
gradient differences $s_k = m_{k+1} - m_k$ and $y_k = g_{k+1} - g_k$ so that
$B_k y_k = s_k$ holds — a secant condition, which is the least a matrix can do to
imitate the Hessian inverse. The BFGS update of $B \approx H^{-1}$ is

$$B_{k+1} = \left(I - \rho_k s_k y_k^{\mathsf{T}}\right) B_k
\left(I - \rho_k y_k s_k^{\mathsf{T}}\right)
+ \rho_k s_k s_k^{\mathsf{T}}, \qquad \rho_k = \frac{1}{y_k^{\mathsf{T}} s_k}.
\tag{2.4}$$

When $y_k^{\mathsf{T}} s_k > 0$ the update preserves positive definiteness, so
the implied curvature model stays legitimate.

### 2.3 Step length, line search and damping

The *step* is $\alpha p$ with $\alpha$ chosen to guarantee progress. The Armijo
condition is

$$f(m + \alpha p) \le f(m) + c_1 \alpha\, g^{\mathsf{T}}p,
\qquad c_1 = 10^{-4}, \tag{2.5}$$

enforced by halving $\alpha$ until it holds. For a Newton step, the cheapest
repair when $H$ is inaccurate is to add a multiple of the identity, the
**Levenberg–Marquardt** modification:

$$p_{\text{LM}}(\lambda) = -(H + \lambda I)^{-1} g, \tag{2.6}$$

which interpolates between the Newton step ($\lambda \to 0$) and a scaled
steepest-descent step ($\lambda \to \infty$). The name matters because (2.6) is
also the standard regularisation of nonlinear least squares in
[01-14-04](./04-least-squares.md).

### 2.4 Convergence orders

Let $e_k = \|m_k - m^{*}\|$. The iteration is **linearly convergent** with rate
$r$ if $e_{k+1} \le r e_k$ asymptotically, **superlinearly** if
$e_{k+1}/e_k \to 0$, and **quadratically** if $e_{k+1} \le C e_k^{2}$. The
practical test for quadratic convergence is that the ratio
$e_{k+1}/e_k^{2}$ settles to a constant — which, as Section 4.5 shows, is
different from the ratio being small.

## 3. Derivations

### 3.1 Steepest descent and the condition number

Take the quadratic $f(m) = \tfrac12(m - m^{*})^{\mathsf{T}} A (m - m^{*})$ with
$A$ symmetric positive definite, eigenvalues $\mu = \lambda_{\min}$ and
$L = \lambda_{\max}$, $\kappa = L/\mu$. Write the error as $e_k = m_k - m^{*}$.
Then $g_k = A e_k$ and the fixed-step iteration $m_{k+1} = m_k - \alpha g_k$
gives

$$e_{k+1} = (I - \alpha A) e_k. \tag{3.1}$$

The error is amplified independently in each eigen-direction by the factor
$1 - \alpha\lambda_i$. Two consequences follow immediately:

1. **Stability:** $|1 - \alpha\lambda_i| < 1$ for all $i$ requires
   $0 < \alpha < 2/L$. A step size above $2/L$ diverges, which is why the safe
   choice $\alpha = 1/L$ appears in every textbook.
2. **Rate:** with the optimal $\alpha = 2/(L + \mu)$ the worst-case factor is
   $(L - \mu)/(L + \mu) = (\kappa - 1)/(\kappa + 1)$.

To reach a relative tolerance $\varepsilon$ the iteration needs approximately

$$k \approx \frac{\ln(1/\varepsilon)}{\ln\bigl((\kappa+1)/(\kappa-1)\bigr)}
\approx \frac{\kappa}{2}\ln\frac{1}{\varepsilon}, \tag{3.2}$$

using $\ln\bigl((\kappa+1)/(\kappa-1)\bigr) \approx 2/\kappa$ for large $\kappa$.
Equation (3.2) is the central quantitative statement of the lesson: **cost is
proportional to the condition number**, so a problem with $\kappa = 10^{4}$ costs
ten thousand times a perfectly conditioned one. Section 4.2 measures the
constant $9.2$ in $k \approx 9.2\kappa$ for $\varepsilon = 10^{-8}$, matching
$\ln(10^{8})/2 = 9.21$.

### 3.2 Newton is exact on a quadratic, and quadratically convergent in general

Expand the gradient about $m_k$:

$$g(m^{*}) = 0 = g_k + H_k (m^{*} - m_k) + O(\|e_k\|^{2}).$$

Ignoring the remainder gives the Newton step (2.3), whence
$m_{k+1} - m^{*} = O(\|e_k\|^{2})$ — quadratic convergence, and exact convergence
in one step when the remainder vanishes, i.e. for a quadratic. The same
expansion shows the failure mode: if $H_k$ is indefinite, the step goes towards a
saddle, and if $H_k$ is inaccurate where the curvature changes sign the step can
be arbitrarily long. Section 4.4 exhibits an objective where the undamped Newton
iteration diverges to $|x| \approx 7\times10^{2}$ in eight steps.

### 3.3 Why BFGS terminates in $n$ steps on a quadratic

For a quadratic, $y_k = A s_k$, and the secant condition $B y_k = s_k$ becomes
$B A s_k = s_k$. After $k$ independent steps the update (2.4) reproduces the
action of $A^{-1}$ on the $k$-dimensional span of the $s_j$; hence after $n$ steps
$B = A^{-1}$ exactly and the next step lands on the minimiser. This is a finite
termination property, not an asymptotic rate, and it explains why BFGS takes
exactly $n = 2$ iterations on the two-parameter quadratic of Section 4.1.

### 3.4 Finite-difference gradients

If a code supplies gradients by central differences with step $h$, each component
carries an error of two contributions:

- truncation, $O(h^{2} f''')$;
- round-off, $O(\epsilon_{\text{mach}} |f| / h)$,

so the total is minimised near $h \sim \epsilon^{1/3}$. The consequence is
concrete: a residual gradient error $\delta g$ perturbs the solution of a
least-squares problem by roughly $\|A^{-1}\| \delta g$, and in a decentred model
this can be the dominant error. Section 4.6 measures the effect.

## 4. Numerical results

All numbers below are from
[`code/unconstrained_demo.py`](./code/unconstrained_demo.py), which implements
Gaussian elimination, the Rosenbrock function, Armijo backtracking, BFGS and the
Levenberg damped Newton step with the standard library alone.

### 4.1 A quadratic: rates and iteration counts

With $f(m) = \tfrac12(m - m^{*})^{\mathsf{T}}A(m-m^{*})$, $A = Q
\operatorname{diag}(1,\kappa)Q^{\mathsf{T}}$ and $m^{*} = (1,-2)$:

| $\kappa$ | step | iterations | $\|m - m^{*}\|$ | measured rate | bound $(\kappa-1)/(\kappa+1)$ |
|---|---|---|---|---|---|
| $10$ | $1/L$ | $127$ | $2.069\times10^{-7}$ | $0.9000$ | $0.8182$ |
| $10$ | $2/(L+\mu)$ | $92$ | $2.146\times10^{-8}$ | $0.8182$ | $0.8182$ |
| $100$ | $1/L$ | $1095$ | $2.226\times10^{-6}$ | $0.9900$ | $0.9802$ |
| $100$ | $2/(L+\mu)$ | $922$ | $2.192\times10^{-8}$ | $0.9802$ | $0.9802$ |
| $1000$ | $1/L$ | $8696$ | $2.231\times10^{-5}$ | $0.9990$ | $0.9980$ |
| $1000$ | $2/(L+\mu)$ | $9211$ | $2.233\times10^{-8}$ | $0.9980$ | $0.9980$ |

Two observations worth dwelling on. First, with the optimal step the *measured*
rate equals the bound to four decimal places — the geometric mean of successive
gradient-norm ratios is $0.8182$, $0.9802$, $0.9980$ for the three condition
numbers. Second, at $\kappa = 1000$ the safe step $1/L$ takes *fewer* iterations
than the theoretically optimal step but leaves an error $10^{3}$ times larger:
the stopping test is on the gradient, and a slower final rate with a smaller
per-iteration contraction produces a different relation between iterations and
accuracy. Reporting one without the other is meaningless.

The cost law (3.2) is visible in the iterations-per-condition-number column:

| $\kappa$ | iterations | iterations/$\kappa$ |
|---|---|---|
| $10$ | $92$ | $9.20$ |
| $100$ | $922$ | $9.22$ |
| $1000$ | $9211$ | $9.21$ |
| $10000$ | $92104$ | $9.21$ |

For a quadratic, **Newton converges in one iteration** ($\|m - m^{*}\| =
2.220\times10^{-16}$) at the cost of two gradient evaluations, and BFGS in
$n = 2$ iterations with $12$ gradient evaluations — the finite-termination
property of Section 3.3, paid for in line-search evaluations.

### 4.2 Rosenbrock: where the methods separate

Starting from $(-1.2, 1.0)$ with the tolerance $\|\nabla f\| \le 10^{-8}\|g_0\|$:

| method | iterations | final error | gradient evaluations |
|---|---|---|---|
| steepest descent, $\alpha = 10^{-3}$ | $29\,960$ | $5.830\times10^{-6}$ | $29\,961$ |
| steepest descent, $\alpha = 5\times10^{-4}$ | $59\,934$ | $5.830\times10^{-6}$ | $59\,935$ |
| Newton with Armijo line search | $21$ | $1.351\times10^{-10}$ | $29$ |
| BFGS with Armijo line search | $34$ | $1.086\times10^{-8}$ | $54$ |

The fixed-step results also illustrate a subtlety: halving the step size doubled
the iterations *and left the final error unchanged*, because the run stopped on
the gradient test rather than on the error. Newton reached the tolerance in $21$
iterations using only $29$ gradient evaluations; BFGS took $34$ iterations and
$54$ evaluations. BFGS's advantage is not iteration count here — the Hessian of
Rosenbrock is two-by-two and cheap — it is that BFGS never needed the Hessian,
which in a $10^{5}$-parameter inversion is the difference between a feasible
method and an infeasible one.

### 4.3 Newton without a line search: an excursion and a divergence

Undamped Newton on Rosenbrock from $(-1.2, 1.0)$ does not fail outright, but it
takes a violent detour:

| iteration | $x$ | $y$ | $f$ |
|---|---|---|---|
| 0 | $-1.200000$ | $1.000000$ | $2.420000\times10^{1}$ |
| 1 | $-1.175281$ | $1.380674$ | $4.731884\times10^{0}$ |
| 2 | $0.763115$ | $-3.175034$ | $1.411845\times10^{3}$ |
| 3 | $0.763430$ | $0.582825$ | $5.596552\times10^{-2}$ |

The objective jumps by a factor of $300$ at step 2 before the method recovers to
$f = 3.433\times10^{-20}$ in six iterations. A single unlucky step is survivable
here; on a larger problem with a 50-digit-scaled parameter range it is not.

The divergence example is cleaner. For $f(x) = \log(1 + x^{2})$ — non-convex for
$|x| > 1$, minimised at $x = 0$ — undamped Newton from $x = 2$ produces

$$2.0 \to 5.333 \to 11.055 \to 22.293 \to 44.676 \to 89.397 \to 178.816
\to 357.643 \to 715.292,$$

doubling every step, because the Newton step is proportional to $1/f''$ and
$f''$ changes sign in the non-convex region. The repair is one line: damp the
Hessian so that the step remains a descent direction, and add a backtracking line
search. With $h_{\text{damped}} = f''$ when $f'' > 10^{-6}$ and $|f''| + 1$
otherwise, plus Armijo backtracking, the same iteration converges to
$x = 7.971\times10^{-19}$.

### 4.4 Levenberg damping: the interpolation in action

On Rosenbrock from $(-1.2, 1)$:

| $\lambda$ | iterations | evaluations | final error |
|---|---|---|---|
| $0$ | $21$ | $29$ | $1.351\times10^{-10}$ |
| $10^{-4}$ | $21$ | $29$ | $1.999\times10^{-9}$ |
| $10^{-2}$ | $20$ | $28$ | $2.125\times10^{-6}$ |
| $1$ | $49$ | $53$ | $5.140\times10^{-6}$ |
| $10^{2}$ | $3009$ | $3010$ | $5.816\times10^{-6}$ |

Small damping is nearly free; large damping is a scaled steepest descent and
pays the condition-number price. Two of the rows also show the honest side of
damping: with $\lambda = 1$ and $10^{2}$ the method stops with an error
$10^{4}$–$10^{5}$ times worse than undamped Newton, because a converged *model*
requires the damping to be reduced near the solution.

### 4.5 Measuring quadratic convergence properly

For $f(x) = e^{x} - 3x$ (minimiser $x^{*} = \ln 3 = 1.098612$) the Newton errors
are

$$1.099,\ 0.9014,\ 0.3074,\ 4.275\times10^{-2},\ 9.011\times10^{-4},\
4.059\times10^{-7},$$

with ratios $e_{k+1}/e_k^{2} = 0.7468,\ 0.3783,\ 0.4525,\ 0.4930,\ 0.4999$ —
settling to a constant near $1/2$. That is what quadratic convergence looks like
when it is measured rather than asserted. On Rosenbrock the same test is *not*
clean: the last five gradient norms from the undamped run are
$1.371\times10^{3}, 4.731\times10^{-1}, 2.503\times10^{1}, 8.609\times10^{-6},
8.286\times10^{-9}$, which are not a constant squared ratio because early
iterations include an *increase*. Quoting a convergence order over a run that
contains a non-monotone step is dishonest; quote it over the asymptotic tail.

### 4.6 Finite-difference gradients, and what they cost

Two regimes, both measured.

**On a quadratic, central differences are exact.** The gradient errors are pure
round-off and *grow* as $h$ shrinks: $6.963\times10^{-13}$ at $h = 10^{-2}$,
$3.482\times10^{-11}$ at $10^{-4}$, $1.553\times10^{-8}$ at $10^{-6}$,
$6.524\times10^{-7}$ at $10^{-8}$. The descent converges to the same model
($\|m - m^{*}\| = 2.192\times10^{-8}$ in $922$ iterations) in every case,
because the stopping test is relative to $\|g_0\|$, which is far above the
difference noise.

**On Rosenbrock, truncation is present and the error has an interior minimum**:
$4.000\times10^{-2}$, $4.000\times10^{-6}$, $3.786\times10^{-9}$,
$7.069\times10^{-7}$ for $h = 10^{-2}, 10^{-4}, 10^{-6}, 10^{-8}$. The best step
here is $h = 10^{-6}$, giving a gradient accurate to $3.8\times10^{-9}$; pushing
to $10^{-8}$ makes it *worse*, because round-off now dominates. This U-shape is
the practical warning: **an optimiser can never converge more precisely than the
gradient it was given.**

### 4.7 Scaling and preconditioning

| problem | $\kappa$ | iterations |
|---|---|---|
| $A = \operatorname{diag}(1, 10^{4})$ | $10\,000$ | $92\,104$ |
| $DAD$ with $D = \operatorname{diag}(1/\sqrt{A_{ii}})$ | $1$ | $1$ |
| $A = Q\operatorname{diag}(1,10^{4})Q^{\mathsf{T}}$ (rotated) | $10\,000$ | $92\,104$ |
| $DAD$ on the rotated problem | $7500.5$ | $69\,083$ |

Diagonal scaling annihilates the cost for the axis-aligned problem — the
preconditioned matrix is the identity — and buys only a factor of $1.33$ on the
rotated problem. The lesson is precise: **preconditioning works when it reduces
the spectral spread, and a diagonal scaling of a rotated operator does not.**
The geophysical practice of choosing model parameters of comparable sensitivity
is exactly the axis-aligned case, and it is free.

## 5. Physical interpretation

**The gradient is the sensitivity of the data to the model.** Each steepest-descent
step moves every parameter in proportion to how strongly it affects the misfit,
which is why the trajectory of steepest descent on an inversion looks like the
sensitivity distribution. Steepest descent spends most of its steps re-shrinking
the well-resolved directions while crawling along the poorly resolved ones — the
spatial behaviour of "slow directions are slow".

**The Newton step is a full resolution analysis.** Solving $H p = -g$ uses the
relative curvature of every parameter combination. In a linearised inversion $H =
G^{\mathsf{T}}G$, so the Newton step is exactly the normal-equation solve, and
the conditioning of $G^{\mathsf{T}}G$ is the conditioning of the iteration — the
bridge to [01-07-05](../07-linear-algebra/05-determinants-inverses.md).

**A line search is a statement about the validity of the local model.** Halving
$\alpha$ until $f$ decreases is the cheapest possible response to a bad Hessian;
it costs evaluations and nothing else. In production, the number of line-search
halvings is a diagnostic: a run that always needs many halvings has a Hessian
that is wrong by a lot, and a run that never needs any is either well behaved or
has a bug.

**Damping is not a kludge.** Adding $\lambda I$ does three things at once:
it makes the step a descent direction, it bounds the step length, and it is
equivalent to Tikhonov regularisation of the normal equations. That equivalence —
Levenberg–Marquardt and Tikhonov regularisation are the same algebra — is
developed in [01-16 Functional Analysis](../16-functional-analysis/README.md) and
is why the same parameter appears as "damping" in seismic packages and
"regularisation weight" in inverse-theory texts.

## 6. Assumptions and regime of validity

1. **Smoothness.** Newton and BFGS assume two continuous derivatives. A kinked
   objective — an L1 misfit, a travel time computed by picking, a
   maximum-likelihood misfit with discrete data — breaks both and requires the
   subgradient methods of [01-14-07](./07-linear-programming.md).
2. **Positive definiteness for the safe step bounds.** The stability condition
   $\alpha < 2/L$ is derived for $H \succ 0$. Where curvature changes sign, no
   fixed step is safe (Section 4.3).
3. **Conditioning.** Equation (3.2) governs everything. A run that "does not
   converge" is usually a run whose condition number exceeds its iteration
   budget, not a run whose gradient is wrong.
4. **Gradient accuracy.** A finite-difference gradient imposes a floor on the
   achievable misfit and on the final model accuracy (Section 4.6). Adjoint
   gradients ([01-07-10](../07-linear-algebra/10-matrix-calculus.md)) remove the
   floor at the cost of writing adjoint code.
5. **Scaling.** Iteration counts are stated in the parameterisation used.
   Re-scaling the parameters changes $\kappa$ and therefore the cost; it does not
   change the mathematics.
6. **Rounding.** With $\kappa \gtrsim 10^{8}$ in double precision, the computed
   gradient itself becomes unreliable — the same wall
   [01-14-04](./04-least-squares.md) hits when forming $G^{\mathsf{T}}G$.

## 7. Python demonstration

The companion script is
[`code/unconstrained_demo.py`](./code/unconstrained_demo.py), with nine
sections. It prints tables; run it and predict each number first.

| Section | Measured | Interpretation |
|---|---|---|
| 1, rates | measured rate equals $(\kappa-1)/(\kappa+1)$: $0.8182$, $0.9802$, $0.9980$ | the bound is attained by the optimal fixed step |
| 2, cost law | $92$, $922$, $9211$, $92104$ iterations for $\kappa = 10, 10^{2}, 10^{3}, 10^{4}$ | cost is linear in $\kappa$, from (3.2) |
| 3, exactness | Newton $1$ iteration, error $2.220\times10^{-16}$; BFGS $2$ iterations | finite termination on a quadratic |
| 4, Rosenbrock | steepest descent $59\,934$ iterations against Newton's $21$ | curvature information buys three orders of magnitude |
| 5, failures | Rosenbrock excursion to $f = 1.41\times10^{3}$; $\log(1+x^{2})$ doubling to $715.3$ | unguarded Newton has no safety property |
| 6, damping | $\lambda = 0$: $21$ iterations; $\lambda = 10^{2}$: $3009$ | damping trades speed for robustness |
| 7, order | ratios $0.7468, 0.3783, 0.4525, 0.4930, 0.4999$ | quadratic convergence, measured |
| 8, differences | best gradient error $3.8\times10^{-9}$ at $h = 10^{-6}$; worse at $10^{-8}$ | truncation against round-off |
| 9, scaling | $92\,104 \to 1$ iterations by diagonal preconditioning | preconditioning changes the spectrum or does nothing |

> **Breaking exercise.** Take the quadratic of Section 1 with $\kappa = 10^{4}$
> and change the stopping test from $\|\nabla f\| \le 10^{-8}\|g_0\|$ to
> $\|m - m^{*}\| \le 10^{-8}$. Predict which method's iteration count moves most,
> and why. Then run it. The point is that a convergence criterion is a
> *specification*, and different criteria measure different things.

## 8. Exercises

Full set and worked solutions:
[`exercises/02-unconstrained-exercises.md`](./exercises/02-unconstrained-exercises.md)
and [`exercises/02-unconstrained-solutions.md`](./exercises/02-unconstrained-solutions.md).
Four to start with:

**★1.** Derive the stability bound $\alpha < 2/L$ for steepest descent on a
quadratic from (3.1), and state what happens at $\alpha = 2/L$ exactly.

**★2.** Write out one BFGS update by hand for $n = 1$ and confirm that it
reproduces $1/f''$ at the second step.

**★★3.** A two-parameter misfit has Hessian eigenvalues $0.01$ and $1.0$. How
many steepest-descent iterations does (3.2) predict to reach
$\varepsilon = 10^{-6}$? Compare with the measured count in
[`code/unconstrained_demo.py`](./code/unconstrained_demo.py) Section 2.

**★★4.** For a finite-difference gradient with a relative evaluation error
$\epsilon$, derive the optimal $h$ and the resulting gradient accuracy, and check
your prediction against the Rosenbrock numbers in Section 4.6.

## 9. Common mistakes

1. **Using a fixed step size above $2/L$.** The iteration diverges; the failure
   is arithmetic, not physical.
2. **Trusting Newton without a guard.** Section 4.3's divergence is one line of
   code away in any code that computes a Hessian.
3. **Reporting an iteration count without the tolerance and the criterion.**
   Section 4.1 shows two runs on the same problem differing by a factor of
   $10^{3}$ in final accuracy at comparable cost.
4. **Believing that BFGS always beats steepest descent per iteration.** BFGS
   *always* uses fewer iterations; per unit of wall-clock time the comparison
   depends on what a gradient costs.
5. **Forgetting to reset or recondition $B$.** After an indefinite-curvature
   region BFGS's $B$ can become non-positive-definite; standard implementations
   test $y^{\mathsf{T}}s$ and reset when it is not positive.
6. **Quoting a convergence order over a non-monotone run.** Section 4.5's
   Rosenbrock sequence contains an increase; only the tail is asymptotic.
7. **Using $1/L$ when the optimal step is available.** On a quadratic, $1/L$
   costs $40\%$ more iterations and leaves $100\times$ the error (Table 4.1).
8. **Expecting convergence beyond the gradient's accuracy.** Section 4.6 sets the
   floor.

## 10. Real-world applications

- **Travel-time tomography.** Linearised inversions use a conjugate-gradient or
  LSQR solver, which is a preconditioned steepest descent; the "iteration" in the
  paper is exactly the $k$ of this lesson, and the condition number of the ray
  matrix is the thing to report.
- **Full-waveform inversion.** L-BFGS on the adjoint gradient is the industry
  default; it is a limited-memory BFGS chosen precisely because storing a
  $10^{9}$-entry Hessian is impossible.
- **Gravity and magnetic inversion.** Gauss–Newton with Levenberg damping
  ([01-14-04](./04-least-squares.md)) dominates, and the damping schedule is the
  practical art.
- **Geodetic network adjustment.** Newton's method on the normal equations, with
  the same conditioning analysis as
  [01-07-05](../07-linear-algebra/05-determinants-inverses.md).
- **Machine learning.** Stochastic gradient descent is steepest descent with a
  noisy, subsampled gradient; Adam and its relatives are diagonal
  preconditioners — the same Section 4.7 idea with an adaptive diagonal.

## 11. Further reading

- **Nocedal, J., & Wright, S. J. *Numerical Optimization* (2nd ed.). Springer.**
  Chapters 2–3 and 6–7. Level: graduate. The definitive account of line searches,
  BFGS and superlinear convergence.
- **Dennis, J. E., & Schnabel, R. B. *Numerical Methods for Unconstrained
  Optimization and Nonlinear Equations*. SIAM Classics.** Level: advanced.
  Convergence-rate theory done carefully, with the failure modes.
- **Luenberger, D. G., & Ye, Y. *Linear and Nonlinear Programming* (4th ed.).
  Springer.** Level: graduate. The convex case in full, with the duality that
  [01-14-03](./03-constrained.md) uses.
- **Kelley, C. T. *Iterative Methods for Optimization*. SIAM.** Level:
  advanced. Short, practical, and honest about what breaks.
- **Tarantola, A. *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: graduate. The same methods in the geophysical
  setting, with the misfit defined by data uncertainty.

> Note on citations: bibliographic details above are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text, and you
> should confirm editions and current availability through your library before
> citing them yourself.

## 12. Self-assessment checklist

- [ ] I can derive the steepest-descent stability bound and the rate
      $(\kappa-1)/(\kappa+1)$.
- [ ] I can estimate an iteration count from $\kappa$ and a tolerance and check it
      against a measured run.
- [ ] I can explain why Newton is exact on a quadratic and only locally reliable
      otherwise.
- [ ] I can write the BFGS update and say what the secant condition enforces.
- [ ] I can implement a backtracking line search and say what it protects
      against.
- [ ] I can choose a damping schedule and justify it from the curvature.
- [ ] I can measure a convergence order from an error sequence and state its
      regime of validity.
- [ ] I can estimate the gradient accuracy a finite-difference scheme delivers
      and the resulting limit on model accuracy.

## 13. Related lessons

- [01-14-01 Convexity, Stationarity and Optimality Conditions](./01-convexity.md) —
  the curvature language this lesson iterates with.
- [01-14-03 Constrained Optimisation and Lagrange Multipliers](./03-constrained.md) —
  what changes when the step must stay inside a feasible set.
- [01-14-04 Linear and Nonlinear Least Squares](./04-least-squares.md) —
  Gauss–Newton, the special case where the curvature is approximately
  $J^{\mathsf{T}}J$.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md) —
  spectral radius and the convergence of fixed-point iterations.
- [01-07-10 Matrix Calculus and Sensitivity Derivatives](../07-linear-algebra/10-matrix-calculus.md) —
  where adjoint gradients come from.
- [01-18 Inverse Problems](../../18-inverse-problems/README.md) — the same
  iteration as the solve step of a nonlinear inversion.
