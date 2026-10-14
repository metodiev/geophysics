# Solutions — 18-05-05 Hamiltonian Monte Carlo and Modern Samplers

> Read after attempting the exercises. Numbers were computed, not estimated.
> Lesson: [05 Hamiltonian Monte Carlo and Modern Samplers](../05-hmc-and-modern-samplers.md).

---

## ★1 — Reversibility of the leapfrog map

One step with step size $\varepsilon$ takes $(m,p)$ to

$$
p' = p - \tfrac{\varepsilon}{2}\nabla U(m),\quad
m' = m + \varepsilon M^{-1}p',\quad
p'' = p' - \tfrac{\varepsilon}{2}\nabla U(m').
$$

Now apply a step with $-\varepsilon$ starting from $(m',p'')$:

$$
\tilde p = p'' + \tfrac{\varepsilon}{2}\nabla U(m')
= p' - \tfrac{\varepsilon}{2}\nabla U(m') + \tfrac{\varepsilon}{2}\nabla U(m')
= p',
$$

$$
\tilde m = m' - \varepsilon M^{-1}\tilde p = m' - \varepsilon M^{-1}p' = m,
$$

$$
\tilde{\tilde p} = \tilde p + \tfrac{\varepsilon}{2}\nabla U(\tilde m)
= p' + \tfrac{\varepsilon}{2}\nabla U(m) = p .
$$

So the map with $+\varepsilon$ followed by the map with $-\varepsilon$ is the
identity. This exact reversibility is what makes the Metropolis acceptance rule
valid for the numerical trajectory; it holds because each kick uses the gradient at
the *updated* position, which is the same point in both directions.

---

## ★2 — Step size for a target energy error

$$
\lvert\Delta H\rvert \approx c\,\varepsilon^{2}T = 0.13\,\varepsilon^{2}(1)
\ \le\ 0.01
\ \Rightarrow\
\varepsilon \le \sqrt{\frac{0.01}{0.13}} = 0.27735 .
$$

So a step of about $0.28$ (in units where the effective frequency is one) satisfies
the bound. Note the square root: the error is second order, so a four-fold
reduction in error costs only a factor of two in step size.

---

## ★3 — Why no Jacobian

1. **Energy conservation**, $\mathrm{d}H/\mathrm{d}t = 0$, so the proposal is
   symmetric in probability between the endpoints.
2. **Phase-space volume preservation** (the flow is divergence-free because
   $\dot m = M^{-1}p$ is independent of $m$ and $\dot p = \nabla U(m)$ is
   independent of $p$), so the proposal density and its reverse have equal
   Jacobians and cancel.

---

## ★★4 — Effective exponents

| $\varepsilon$ | mean $\lvert\Delta H\rvert$ | ratio | exponent $\ln(\text{ratio})/\ln 2$ |
|---|---|---|---|
| 0.50000 | $1.086\times10^{0}$ | — | — |
| 0.25000 | $3.864\times10^{-2}$ | 28.11 | 4.813 |
| 0.12500 | $3.304\times10^{-3}$ | 11.69 | 3.547 |
| 0.06250 | $5.959\times10^{-4}$ | 5.54 | 2.470 |
| 0.03125 | $1.282\times10^{-4}$ | 4.65 | 2.217 |

The exponent falls monotonically toward the asymptotic value $2$. Only the last
two rows are close to it, and even the final row has not reached $2$. A single
least-squares slope over the whole range gives $-3.21$ (the demonstration's
measured value), which *understates* the true order: the large-step rows inflate
it. The defensible statement is "second order asymptotically, verified by the
trend toward an exponent of $2$", not "the measured exponent is $-3.21$".

---

## ★★5 — ESS per gradient evaluation

| $L$ | ESS (3000 draws) | ESS per gradient |
|---|---|---|
| 5 | 809 | 0.0404 |
| 10 | 3000 | 0.0750 |
| 20 | 3000 | 0.0375 |

The ESS per gradient rises from $L=5$ to $L=10$ and then falls by half at
$L=20$: doubling the trajectory length does not double the decorrelation, because
the path begins to curl back and returns near its starting point. The measured
optimum here is $L = 10$, at $0.0750$ per gradient. In practice this optimum is
target-specific and is chosen adaptively (the NUTS criterion) rather than by
scanning.

---

## ★★6 — Preconditioning factor

$$
\frac{0.08333}{0.00087} = 95.8 .
$$

A covariance-matched mass matrix buys a factor of about $96$ in ESS per gradient
evaluation on this target, whose condition number is $535$. The factor is
target-specific because it measures how badly a single step size serves both the
narrow and the wide eigendirection: on a target with condition number near $1$ the
identity mass matrix is already adequate, and on one with condition number $10^{4}$
even a diagonal mass matrix is insufficient.

---

## ★★7 — High acceptance, nonzero divergences

**Likely cause.** The posterior has a region the leapfrog integrator cannot
traverse — a funnel (a scale parameter that shrinks with another parameter), a
near-discontinuity in the likelihood, or a poorly identified direction with
extreme curvature. The step size is small enough that ordinary moves are accepted,
while a few trajectories enter the difficult region and produce enormous
$\lvert\Delta H\rvert$.

**Fix.** Reparameterise (non-centred parameterisation, log or logit transforms,
whitening by a covariance estimate), then re-run. A change of metric alone may
help but does not remove a genuine funnel.

**Why the acceptance rate hides it.** Acceptance is an average over the whole run.
Fourteen divergences out of tens of thousands of iterations leave the average
essentially unchanged, while the draws they produce are biased because the
algorithm never reached the region and instead reported a trajectory that had
wandered. Divergences are the only diagnostic that localises this failure.

---

## ★★8 — A gradient check

- **Test quantity:** the directional derivative along a random unit vector $v$,
  compared between the adjoint gradient and a central finite difference:
  $g_{\text{fd}} = [f(m+hv) - f(m-hv)]/(2h)$ against $g_{\text{adj}} = v^{\top}\nabla f$.
- **Perturbation sizes:** $h \in \{10^{-3}, 10^{-4}, 10^{-5}, 10^{-6}\}$ times a
  characteristic parameter scale, so that the truncation error $\mathcal{O}(h^2)$
  and the round-off error $\mathcal{O}(\epsilon/h)$ are both visible.
- **Expected scaling:** the relative error should fall as $h^2$ and then rise as
  $h$ decreases, with a minimum near $h \sim \epsilon^{1/3}$. The check is
  reproducible because both branches are deterministic.
- **Threshold:** accept when the relative difference at the best $h$ is below
  $10^{-5}$; a mismatch at all $h$ indicates a genuine error in the adjoint, a
  mismatch only at small $h$ indicates a noisy forward solver.

**What a pass does not tell you:** it does not verify that the forward model is
correct, that the misfit is the intended one, or that the gradient is continuous
away from the tested point. A correct adjoint of a wrong forward model passes
every time.
