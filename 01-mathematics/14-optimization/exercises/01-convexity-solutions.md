# Solutions — 01-14-01 Convexity, Stationarity and Optimality Conditions

> **Read this after attempting the exercises, not before.**
>
> Numeric answers were computed and verified with
> [`../code/convexity_demo.py`](../code/convexity_demo.py) or by hand from exact
> algebra. Where a number comes from the script, the section is named.

---

## ★1 — The chord inequality for a quadratic

With $f(m) = \tfrac12 m^{\mathsf{T}}Am - b^{\mathsf{T}}m$, $A = A^{\mathsf{T}}
\succ 0$, substitute $m_\theta = \theta x + (1-\theta)y$:

$$f(m_\theta) = \tfrac12 m_\theta^{\mathsf{T}}Am_\theta - b^{\mathsf{T}}m_\theta .$$

Write $u = x - y$ so that $m_\theta = y + \theta u$. Then

$$f(m_\theta) = f(y) + \theta\left(u^{\mathsf{T}}Ay - b^{\mathsf{T}}u\right)
+ \tfrac12\theta^{2}u^{\mathsf{T}}Au,$$

and the chord is

$$\theta f(x) + (1-\theta)f(y) = f(y) + \theta\left(f(x) - f(y)\right)
= f(y) + \theta\left(u^{\mathsf{T}}Ay + \tfrac12u^{\mathsf{T}}Au - b^{\mathsf{T}}u\right),$$

using $x = y + u$ to expand $f(x) - f(y)$. Subtracting,

$$f(m_\theta) - \left[\theta f(x) + (1-\theta)f(y)\right]
= -\tfrac12\theta(1-\theta)\,u^{\mathsf{T}}Au \le 0,$$

because $u^{\mathsf{T}}Au > 0$ for $u \ne 0$ (positive definiteness). Inequality
(2.1) therefore holds for every $x, y$ and $\theta \in [0,1]$, and it is strict for
$0 < \theta < 1$: $f$ is strictly convex.

**Minimiser.** $\nabla f = Am - b = 0$ gives $m^{*} = A^{-1}b$, unique because
$A$ is nonsingular. The same conclusion follows from strict convexity.

**Remark.** The proof used only the sign of $u^{\mathsf{T}}Au$. Weakening
$A \succ 0$ to $A \succeq 0$ loses strict convexity and, as ★3 shows, uniqueness
with it.

---

## ★2 — Gradient and Hessian of a least-squares misfit

In components, $\phi = \tfrac12\sum_i\left(\sum_j G_{ij}m_j - d_i\right)^{2}$.
Differentiate with respect to $m_k$:

$$\frac{\partial\phi}{\partial m_k} = \sum_i \Bigl(\sum_j G_{ij}m_j - d_i\Bigr)G_{ik}
= \left[G^{\mathsf{T}}(Gm - d)\right]_k .$$

So $\nabla\phi = G^{\mathsf{T}}(Gm-d) = -G^{\mathsf{T}}r$ with
$r = Gm - d$. Differentiating once more,

$$\frac{\partial^{2}\phi}{\partial m_k\partial m_l} = \sum_i G_{ik}G_{il}
= (G^{\mathsf{T}}G)_{kl}, \qquad \nabla^{2}\phi = G^{\mathsf{T}}G,$$

independent of $m$: the misfit is an exact quadratic.

**Uniqueness.** $\nabla\phi = 0$ is the normal equation $G^{\mathsf{T}}Gm =
G^{\mathsf{T}}d$, which has a *unique* solution if and only if $G$ has full
column rank (equivalently, $\operatorname{null}(G) = \{0\}$, equivalently
$G^{\mathsf{T}}G \succ 0$). If a null vector $n \ne 0$ exists, then
$\phi(m + \alpha n) = \phi(m)$ for every $\alpha$, and the minimiser is a set.

---

## ★3 — Two rays through one cell

**(a)** The kernel is $G = \begin{bmatrix}1&1\\1&1\end{bmatrix}$ and the normal
equations read $2(m_1 + m_2) = 0.04$, so the solution set is

$$\{m : m_1 + m_2 = 0.02\} = \{(0.02,0) + \alpha(1,-1) : \alpha \in \mathbb{R}\}.$$

Every such model gives $Gm = (0.02, 0.02)^{\mathsf{T}} = d$ exactly.

**(b)** The misfit is $\phi = \tfrac12\|Gm - d\|^{2} = 0$ for **every** $\alpha$.
This is the flat-valley case of the lesson: not merely stationary, but exactly
constant along $n = (1,-1)$. The companion script's Section 4 prints the same
behaviour for a three-cell version, with misfits of $7.7\times10^{-34}$ at
$\alpha \ne 0$ — round-off around the true zero.

**(c)** $G^{\mathsf{T}}G = \begin{bmatrix}2&2\\2&2\end{bmatrix}$ has eigenvalues
$(4, 0)$. The objective is convex (the Hessian is positive semi-definite) but not
*strictly* convex, so a minimiser exists and is not unique. Both facts are the
same fact.

**Interpretation.** The two rays carry identical information: whatever the data
say, they say it twice. The sum $m_1 + m_2$ is determined; the difference is not,
and no algorithm can determine it.

---

## ★4 — Basins of a cycle-skipped misfit

**(a)** From `convexity_demo.py` Section 6, the local minima on
$[1.5, 8.0]$ km/s and their misfits are

| $v$ (km/s) | misfit |
|---|---|
| $1.73680$ | $2.502116$ |
| $2.18970$ | $2.997575$ |
| $3.00000$ | $0.000000$ |
| $4.76230$ | $2.997575$ |

The minimum at $v = 3.0$ km/s is the true velocity, and it is the global minimum
with misfit $0$.

**(b)** Damped descent started at $v = 5.0$ km/s converges to

$$v = 4.76233\ \mathrm{km/s}, \qquad \text{misfit} = 2.997575,$$

which is the local minimum at $4.76230$ — the returned model is wrong by
$59$ per cent in velocity, and the residual is finite and unremarkable.

**(c)** The misfit is a sum of $1 - \cos(2\pi\,\Delta t/T)$ terms; an arrival-time
error of a whole number of periods produces the same value, so models separated
by one period in a wrapped observable are indistinguishable. Starting above
$4$ km/s places the search in the basin of the aliased minimum.

---

## ★5 — A stationary point that is not a minimum

**(a)** $f(x,y) = x^{2} - y^{2}$, so $\nabla f = (2x, -2y)$ and
$\nabla f(0,0) = (0,0)$.

**(b)** The Hessian is constant, $\nabla^{2}f = \operatorname{diag}(2,-2)$; the
demonstration uses the scaled version $\operatorname{diag}(1,-1)$, whose
eigenvalues are $(-1, +1)$.

**(c)** The **first-order necessary condition** is satisfied. The **second-order
necessary condition** fails, because the Hessian has a negative eigenvalue and is
therefore not positive semi-definite. The point is a saddle: it is a minimum along
$x$ and a maximum along $y$.

**Consequence.** A local descent started exactly at the origin has zero gradient
and stops, reporting convergence to something that is not a minimum. That is why
the lesson insists on pairing the gradient test with a curvature test, and it is
why the demonstration's Newton run on $f(m) = m^{4}-2m^{2}+0.3m$ from
$m = 0$ converged to $m = 0.07542916$ with $f'' = -3.931725$ — a maximum, found
with the same criterion that found the two minima.

---

## ★6 — Closure properties of convex functions

**(a) Non-negative combinations.** Let $f, g$ be convex on a convex set $C$ and
let $\alpha, \beta \ge 0$. For $x, y \in C$ and $\theta \in [0,1]$, convexity of
$f$ and $g$ gives
$f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y)$ and likewise for
$g$. Multiplying the first by $\alpha$, the second by $\beta$ and adding,

$$(\alpha f + \beta g)\bigl(\theta x + (1-\theta)y\bigr) \le
\theta(\alpha f + \beta g)(x) + (1-\theta)(\alpha f+\beta g)(y).$$

No differentiability is needed; $\alpha,\beta \ge 0$ is essential (a negative
multiple of a convex function is concave).

**(b) Composition with an increasing convex function.** Let $f$ be convex and
$h$ convex and non-decreasing. By the chord inequality for $f$,
$f_\theta := f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y) =: \bar
f_\theta$. Since $h$ is non-decreasing, $h(f_\theta) \le h(\bar f_\theta)$, and
by convexity of $h$, $h(\bar f_\theta) \le \theta h(f(x)) + (1-\theta)h(f(y))$.
Chaining the two inequalities gives

$$h\bigl(f(\theta x + (1-\theta)y)\bigr) \le \theta\,h(f(x)) + (1-\theta)\,h(f(y)).$$

Monotonicity of $h$ is essential and is what makes this different from (a).

**Consequence for a weighted misfit.** The weighted least-squares objective
$\sum_i w_i r_i^{2}$ with all $w_i > 0$ is a non-negative combination of the
convex functions $r_i^{2}$, so it is convex by (a) — and strictly convex whenever
the weighted kernel $W^{1/2}G$ has full column rank. Positive weights therefore
cannot destroy uniqueness; they can only change the geometry.

**Where (b) applies.** A misfit built as $h(\text{residual energy})$ with $h$ convex
and increasing — for example a Huber-type penalty applied to the misfit value, or
an exponential-of-misfit likelihood term — inherits convexity of the inner term
only if the inner term is convex *and* the composition respects the monotonicity
direction. An often-missed case is the reverse: $\log$ of a misfit energy is
*concave*, not convex, which is why log-misfit objectives can be multi-modal even
when the underlying misfit is not.

---

## ★7 — A critique of a reported convergence

The report gives a final gradient norm of $10^{-9}$ and a misfit of $0.8$ where
the data variance suggests $0.1$ is attainable. A structured critique:

**What the quoted numbers do establish.** $\|\nabla\phi\| \le 10^{-9}$ is the
first-order necessary condition: the reported model is a stationary point of the
objective to that accuracy. Nothing more. In particular it does not establish
that the point is a minimum (a saddle or maximum also has a vanishing gradient),
nor that it is the global minimum, nor that the model is near the truth.

**What they do not address.** Three separate questions: (i) curvature — is
$\nabla^{2}\phi$ positive definite there, and what is its smallest eigenvalue?
(ii) basin membership — did the run start in the basin of the global minimum?
(iii) model error — the misfit is $8$ times the expected noise level, so either
the noise estimate, the forward model, or the parameterisation is wrong.

**The test to run next.** The cheapest informative test is a curvature and
conditioning check: compute the smallest eigenvalue of $\nabla^{2}\phi$ at the
reported model, or, if the engine is Gauss–Newton, the singular values of $J$.
Two outcomes:

- **Smallest eigenvalue positive and not tiny** (say $\lambda_{\min}/\lambda_{\max}
  > 10^{-8}$): the model is a genuine, well-determined local minimum, and the
  misfit excess must be explained by the forward model or the noise estimate.
- **Near-zero or negative eigenvalue**: the run has stopped on a flat or
  indefinite direction, and "converged" means only that the solver could not
  make progress. The remedy is a different starting model or a global search,
  not a tighter tolerance.

**Measured support.** In this module, the five-ray cross-hole misfit of
`convexity_demo.py` Section 2 has $\lambda_{\min} = 1.1\times10^{-4}$ against
$\lambda_{\max} = 5.397682$ — a ratio of $2\times10^{-5}$ — while the gradient at
the minimiser is $1.9\times10^{-16}$. A run reporting only the gradient would look
perfectly converged; the eigenvalue tells you that one model direction is
constrained by the data $4\times10^{4}$ times more weakly than the best-determined
one, which is the number that should accompany the "converged" claim.
