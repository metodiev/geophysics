# Solutions — 01-14-02 Unconstrained Minimisation: Gradient, Newton, Quasi-Newton

> **Read this after attempting the exercises, not before.**
>
> Iteration counts and errors quoted as "measured" come from
> [`../code/unconstrained_demo.py`](../code/unconstrained_demo.py), run on this
> machine with Python's binary64 floats. Different hardware can change the last
> digit or two of a reported error, never a reported iteration count unless the
> run stops at a tolerance boundary.

---

## ★1 — Stability and rate of fixed-step steepest descent

With $e_k = m_k - m^{*}$ and $g_k = \nabla f(m_k) = Ae_k$, the update
$m_{k+1} = m_k - \alpha g_k$ gives

$$e_{k+1} = e_k - \alpha Ae_k = (I - \alpha A)e_k .$$

**(a) Convergence.** Since $A$ is symmetric, diagonalise it: in the eigenbasis
the $i$-th component is multiplied by $1 - \alpha\lambda_i$. Convergence for
every component requires $|1 - \alpha\lambda_i| < 1$, i.e.
$0 < \alpha\lambda_i < 2$ for all $i$, which with $\mu \le \lambda_i \le L$ is

$$0 < \alpha < \frac{2}{L}.$$

At $\alpha = 2/L$ the component along the largest eigenvalue has multiplier
$-1$: it neither decays nor grows, and round-off accumulates without bound. That
is the observed behaviour of a descent that "oscillates forever" on a stiff
problem.

**(b) Best fixed step.** Taking $\alpha = 2/(L+\mu)$ equalises the two extreme
multipliers, $1 - \alpha\mu = -(1 - \alpha L)$, so both are $\pm(\kappa-1)/(\kappa+1)$
in magnitude. The worst-case contraction per iteration is therefore

$$r = \frac{\kappa - 1}{\kappa + 1}, \qquad \kappa = \frac{L}{\mu}.$$

Values: $\kappa = 10 \Rightarrow r = 0.8182$; $\kappa = 100 \Rightarrow 0.9802$;
$\kappa = 1000 \Rightarrow 0.9980$. The demonstration measures these rates
directly (Section 1) as $0.8182$, $0.9802$, $0.9980$ — a three-way agreement to
four decimals, which is as good as a rate measurement gets.

---

## ★2 — BFGS in one dimension

For $n = 1$ the update (2.4) with scalars $s, y$ and $\rho = 1/(ys)$ reads

$$B^{+} = \left(1 - \rho s y\right)B\left(1 - \rho y s\right) + \rho s^{2}
= B\left(1 - \rho s y\right)^{2} + \rho\, s^{2}.$$

Since $\rho s y = 1$ by definition, the first term vanishes and

$$B^{+} = \rho s^{2} = \frac{s^{2}}{sy} = \frac{s}{y}.$$

**Interpretation.** $s/y = \Delta x/\Delta g$ is the reciprocal of the secant
slope of the gradient, i.e. the finite-difference approximation to $1/f''(x)$
centred on the two iterates. In one dimension BFGS therefore reconstructs the
curvature exactly whenever $f$ is quadratic (for which $y = f''s$ identically), so
the next step is a Newton step and the iteration terminates at the minimiser. This
is the $n = 1$ instance of the finite-termination property proved in the lesson's
Section 3.3: BFGS on a quadratic reaches the solution in $n$ steps, which the
demonstration confirms on a two-parameter quadratic ($2$ iterations, final error
$4.818\times10^{-10}$ against Newton's $1$ iteration and $2.220\times10^{-16}$).

---

## ★★3 — Predicting steepest-descent iterations

**(a)** With $\kappa = 100$ and $\varepsilon = 10^{-8}$,

$$k \approx \frac{\kappa}{2}\ln\frac{1}{\varepsilon}
= \frac{100}{2}\times 18.4207 = 921.0 .$$

**(b)** The measured count with the optimal step $\alpha = 2/(L+\mu)$ is **922**
(`unconstrained_demo.py` Section 2, $\kappa = 100$). Agreement to one iteration
out of 922 — $0.1$ per cent — because the derivation's approximation
$\ln((\kappa+1)/(\kappa-1)) \approx 2/\kappa$ is accurate to
$O(\kappa^{-2})$, and because the stopping test is satisfied at the first
iterate *after* the error passes the threshold rather than exactly at it.

The same formula predicts $k = 9210$ at $\kappa = 1000$; the measurement gives
$9211$. For the record, the safe step $\alpha = 1/L$ is not optimal and gives
$8696$, $1095$ and $127$ iterations at $\kappa = 1000, 100, 10$ — but with final
errors $2.2\times10^{-5}$, $2.2\times10^{-6}$ and $2.1\times10^{-7}$, i.e. a
hundred times worse than the optimal step. **Iteration count and final accuracy
must always be quoted together.**

---

## ★★4 — The best step for a central difference

**(a)** The central difference of a smooth $f$ has

$$\text{truncation} \approx \frac{h^{2}}{6}|f'''|, \qquad
\text{round-off} \approx \frac{\epsilon\,|f|}{2h},$$

where $\epsilon$ is the relative error of an evaluation. The total
$T(h) = C_1h^{2} + C_2\epsilon/h$ is minimised at

$$\frac{dT}{dh} = 2C_1h - \frac{C_2\epsilon}{h^{2}} = 0
\quad\Longrightarrow\quad
h^{*} = \left(\frac{C_2\epsilon}{2C_1}\right)^{1/3} \sim \epsilon^{1/3},$$

with $T(h^{*}) \sim \epsilon^{2/3}$.

**(b)** For $\epsilon = 2.2\times10^{-16}$, $h^{*} \sim 6.0\times10^{-6}$ and
$T \sim \epsilon^{2/3} = 3.6\times10^{-11}$. The measured Rosenbrock gradient
errors are

| $h$ | max gradient error |
|---|---|
| $10^{-2}$ | $4.000\times10^{-2}$ |
| $10^{-4}$ | $4.000\times10^{-6}$ |
| $10^{-6}$ | $3.786\times10^{-9}$ |
| $10^{-8}$ | $7.069\times10^{-7}$ |

The minimum of the measured curve is indeed near $h^{*}$ — between $10^{-6}$ and
$10^{-4}$, with $10^{-6}$ the best of the four tested — and the observed
skipping of the predicted $3.6\times10^{-11}$ is explained by the size of the
coefficients $C_1, C_2$: the prediction gives the *scaling* of $h^{*}$ and
$T(h^{*})$, not the constants, and the coefficients here are not exactly
$1/6$ and $1/2$.

The important qualitative fact stands: the error is *not* monotone in $h$. Making
the step smaller eventually makes the gradient worse, and an optimiser cannot
converge more accurately than the gradient it is given. The contrast with the
quadratic test in the same section is instructive: for a quadratic the central
difference is exact, so there is no truncation term at all and the measured error
grows monotonically as $h$ falls from $10^{-2}$ ($6.963\times10^{-13}$) to
$10^{-8}$ ($6.524\times10^{-7}$).

---

## ★★5 — The Newton step and indefinite curvature

**Derivation.** Expand the gradient about $m_k$:

$$0 = \nabla f(m^{*}) = \nabla f(m_k) + \nabla^{2}f(m_k)(m^{*} - m_k)
+ O(\|m^{*}-m_k\|^{2}),$$

so the Newton step $p = -\nabla^{2}f(m_k)^{-1}\nabla f(m_k)$ makes the *linear
model of the gradient* vanish. For a quadratic the remainder is exactly zero,
which is why one step suffices.

**Indefinite Hessian.** If $H$ has a negative eigenvalue, the step moves in the
direction of *increasing* $f$ along that eigendirection: $p = -H^{-1}g$ has
$p^{\mathsf{T}}g = -g^{\mathsf{T}}H^{-1}g > 0$ when $H^{-1}$ has a negative
eigenvalue. The step is not a descent direction, and the length
$\|H^{-1}g\|$ can be arbitrarily large as $H$ approaches singularity. This is
exactly the divergence mechanism of ★★6.

---

## ★★6 — Where undamped Newton diverges

For $f(x) = \log(1+x^{2})$, $f'(x) = 2x/(1+x^{2})$ and
$f''(x) = 2(1-x^{2})/(1+x^{2})^{2}$, so

$$x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}
= x_k - \frac{x_k(1+x_k^{2})}{1 - x_k^{2}}
= \frac{-2x_k^{3}}{1-x_k^{2}} .$$

**(a)** From $x_0 = 2$:

| $k$ | $x_k$ | $f'(x_k)$ | $f(x_k)$ |
|---|---|---|---|
| 0 | $2.000000\times10^{0}$ | $8.000000\times10^{-1}$ | $1.609438\times10^{0}$ |
| 1 | $5.333333\times10^{0}$ | $3.622642\times10^{-1}$ | $3.382505\times10^{0}$ |
| 2 | $1.105533\times10^{1}$ | $1.794400\times10^{-1}$ | $4.813974\times10^{0}$ |
| 3 | $2.229306\times10^{1}$ | $8.953386\times10^{-2}$ | $6.210561\times10^{0}$ |
| 4 | $4.467602\times10^{1}$ | $4.474433\times10^{-2}$ | $7.599375\times10^{0}$ |

**(b)** The iterates roughly double each step ($|x_{k+1}/x_k| \to 2$ as
$x_k \to \infty$, since $-2x^{3}/(1-x^{2}) \to 2x$). The objective is
*increasing* steadily: the method is walking uphill and away from the solution at
$x = 0$. The assumption that fails is the validity of the local quadratic model:
$f$ is non-convex for $|x| > 1$, so $f''(x) < 0$ there and the step points in the
direction of increasing $f$. In the demonstration the same table reaches
$x_4 = 44.676$ and continues to $x_8 = 715.292$.

**(c) Repair.** Damp the Hessian so that the step is a descent direction —
$h_{\text{damped}} = f''$ where $f'' > 0$ and $|f''| + 1$ otherwise — and add an
Armijo backtracking line search (2.5). With that modification the demonstration
converges to $x = 7.971\times10^{-19}$, i.e. to the minimiser, from the same
starting point. The general principle: a Newton step needs either a positive
definite curvature model or a guard that bounds its length.

---

## ★★7 — Why BFGS rather than DFP

**The short answer.** Both updates satisfy the secant condition and both preserve
positive definiteness, but BFGS's implied *direct* Hessian approximation is the
one that behaves better in practice: the BFGS update is less prone to the
"information loss" that makes DFP produce poor curvature estimates when steps are
large, and it has superior self-correcting properties under inexact line searches
— which is what large-scale codes use. Textbooks typically cite practical
performance and the BFGS update's better behaviour with scaling rather than a
single theorem.

**An experiment that would distinguish them.** Controlled variables: the
objective (Rosenbrock), the starting point $(-1.2, 1)$, the line-search
parameters ($c_1 = 10^{-4}$, halving), the stopping test
($\|\nabla f\| \le 10^{-8}\|\nabla f_0\|$), the arithmetic (binary64), and the
number of runs $R$ per method — a stochastic comparison with $R = 1$ is
meaningless, and $R \ge 20$ is the minimum for a claim about a *distribution* of
iteration counts rather than a single sample.

Measured quantities: iterations and gradient evaluations per run, reported as
medians with the full range, plus the final error. A single run cannot distinguish
the methods; the experiment must fail on the *worst* runs, which is where the
updates differ.

**Why the design is what it is.** The demonstrable difference between quasi-Newton
methods is not the median behaviour on a well-scaled two-parameter problem — both
will take tens of iterations — but the tail: the largest iteration count out of
$R$ runs from a perturbed start. That is the quantity to report, and it is
comparable across methods only if the line search and stopping rule are
identical, because those dominate the iteration count otherwise.

---

## ★★8 — Separating three contributions to the iteration count

**Design.** Hold fixed: the objective, the starting model, the outer stopping
tolerance, and the random seed. Vary one factor at a time:

| Factor | How to vary it | Observable that isolates it |
|---|---|---|
| (i) conditioning | multiply the model parameters by a scaling $s$ and invert; equivalently change the Hessian's spectral spread from $10^{2}$ to $10^{4}$ to $10^{6}$ | iteration count should grow roughly *linearly* in $\kappa$, as the lesson's Table of $92, 922, 9211, 92104$ for $\kappa = 10, 10^{2}, 10^{3}, 10^{4}$ |
| (ii) gradient accuracy | supply the same gradient twice: once analytically, once by central differences at a chosen $h$ | the *achievable* final misfit changes, but the iteration count changes only slightly; the signature is a floor on the misfit, not extra iterations |
| (iii) tolerance | change the inner CG tolerance from $10^{-4}$ to $10^{-8}$ | iteration count grows logarithmically in $1/\varepsilon$ if the inner solve is the bottleneck, and stays flat if it is not |

**Diagnosis.** If the count tracks $\kappa$ linearly, the outer problem's
conditioning is the cost. If it responds to $h$ in the gradient, the finite
difference is the limit. If it responds strongly to (iii) while (i) and (ii) are
fixed, the inner solver's tolerance is the cost. Because the three responses have
different functional forms — linear in $\kappa$, a *floor* rather than a count for
$h$, logarithmic in the tolerance — a well-designed sweep separates them without
needing a model of the interaction.

**Measured anchor from the module.** Section 4.6 of the lesson shows the
finite-difference contribution is not extra iterations but a floor on the
achievable model error; Section 4.7 shows the conditioning contribution is
linear in $\kappa$ and disappears entirely when the preconditioner removes the
spectral spread. Those two observations are exactly what the design above is
built to separate.
