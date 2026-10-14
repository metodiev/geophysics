---
id: 18-05-05
title: "Hamiltonian Monte Carlo and Modern Samplers"
level: research
prereqs: ["18-05-04", "18-04-02"]
tags: [inverse-problems, bayesian, uncertainty-quantification, hmc, nuts, gradients, preconditioning]
---

# Hamiltonian Monte Carlo and Modern Samplers

All models in this module are **SYNTHETIC**. Both targets used here are Gaussians
whose moments are known exactly, so each sampler can be scored against the truth.
Every number quoted is printed by [`code/hmc_demo.py`](./code/hmc_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Hamiltonian formulation of a target density, including the
   auxiliary momentum, and **explain** why volume preservation and energy
   conservation make it a valid proposal.
2. **Implement** the leapfrog (velocity Verlet) integrator and **measure** its
   second-order energy error over a fixed trajectory duration.
3. **Explain** why the Metropolis step is still required even though the dynamics
   conserve energy exactly in continuous time.
4. **Choose** a trajectory length from a measured efficiency curve rather than
   from a rule of thumb, and state what the adaptive NUTS criterion replaces.
5. **Measure** the improvement obtained from preconditioning with a
   covariance-matched mass matrix, and state the practical problem of estimating
   that covariance.
6. **Compare** HMC against random-walk Metropolis at equal numbers of gradient
   evaluations, and state when the comparison is not favourable.
7. **State** the assumptions a gradient-based sampler needs, and the failure mode
   when the gradient is discontinuous, noisy or unavailable.

## Prerequisites

- [18-05-04 Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs](04-mcmc.md)
  — acceptance ratios, autocorrelation time and effective sample size.
- [18-04-02 Gradient, Gauss-Newton and Full Newton Methods](../04-nonlinear-inversion/02-gradient-and-newton.md)
  — gradients and Hessians of a misfit, and the adjoint construction of a
  gradient for a large forward model.
- [03-03-03 Optimisation in SciPy](../../03-scientific-computing/03-scipy/03-optimize.md)
  — the numerical machinery underneath a gradient evaluation.

## 1. Intuition: replace guessing by simulation

A random-walk proposal knows nothing about the target. It steps in a random
direction, and the acceptance test tells it afterwards whether that was a good
idea. In a correlated or stiff target, most directions are bad, and the measured
autocorrelation time of
[04](04-mcmc.md) grows accordingly.

Hamiltonian Monte Carlo removes the guessing. It uses the gradient of the log
density to follow the target rather than to test it, by simulating a classical
mechanical system whose potential energy is the negative log density. Momentum
carries the state across the space along level sets of the density, so a single
proposal can travel a long way while staying in a high-probability region.

The physical analogy is exact enough to be useful. Picture a ball rolling on a
hillside whose height is $-\ln p(m\mid d)$: the ball is slow in deep valleys
(high probability) and fast on the slopes. The kinetic energy gives it a way to
cross a saddle; the potential energy pulls it back. A random walk cannot cross a
saddle efficiently because it must climb one step at a time; a single
Hamiltonian trajectory conserves the total energy and does it in one move.

## 2. The Hamiltonian formulation

Augment the model $m$ with a fictitious momentum $p \sim \mathcal{N}(0,M)$ and
define

$$
H(m,p) = U(m) + K(p),
\qquad
U(m) = -\ln p(m\mid d),
\qquad
K(p) = \tfrac12 p^{\top}M^{-1}p .
$$

The joint density $\exp[-H(m,p)]$ has $m$ marginal
$\propto \exp[-U(m)]$ — the posterior, up to the constant that MCMC never needs —
and a Gaussian momentum marginal. The equations of motion are

$$
\frac{\mathrm{d}m}{\mathrm{d}t} = \frac{\partial H}{\partial p} = M^{-1}p,
\qquad
\frac{\mathrm{d}p}{\mathrm{d}t} = -\frac{\partial H}{\partial m} = \nabla U(m).
$$

Two properties matter, and both are provable in one line.

**Energy conservation.** Along a solution, $\mathrm{d}H/\mathrm{d}t =
(\partial H/\partial m)\dot m + (\partial H/\partial p)\dot p = \dot p^{\top}\dot
m - \dot m^{\top}\dot p = 0$. A trajectory therefore stays on a level set of $H$,
which in the joint space is a level set of the *joint density*. All parts of a
trajectory are equally probable.

**Volume preservation.** The vector field is divergence-free: $\partial \dot
m/\partial m + \partial \dot p/\partial p = 0$ because
$\dot m = M^{-1}p$ does not depend on $m$ and $\dot p = \nabla U(m)$ does not
depend on $p$. The flow therefore preserves phase-space volume, so no
Jacobian correction appears in the acceptance ratio. This is the property that
makes Hamiltonian proposals *reversible and volume-preserving*, which is what
detailed balance requires.

## 3. The leapfrog integrator, and its measured error

Continuous-time conservation is of no use to a computer. Discretise with one
leapfrog step of size $\varepsilon$, from $(m,p)$:

$$
p \leftarrow p - \tfrac{\varepsilon}{2}\nabla U(m),
\qquad
m \leftarrow m + \varepsilon M^{-1}p,
\qquad
p \leftarrow p - \tfrac{\varepsilon}{2}\nabla U(m).
$$

The scheme is *symplectic*, so it conserves a perturbed Hamiltonian
$\tilde H = H + \mathcal{O}(\varepsilon^2)$ rather than $H$ itself, and it is
*reversible*, which is what lets the Metropolis test correct it. It is also
second order, and the demonstration measures that claim rather than asserting it.
Holding the trajectory duration at $T = 1$ so that only $\varepsilon$ changes, and
linking the number of steps by $L = T/\varepsilon$, it reports the mean energy
error $|\Delta H|$ over $400$ random initial conditions:

| $\varepsilon$ | $L$ | mean $\lvert\Delta H\rvert$ | ratio to the previous row |
|---|---|---|---|
| 0.50000 | 2 | $1.086\times10^{0}$ | — |
| 0.25000 | 4 | $3.864\times10^{-2}$ | 28.11 |
| 0.12500 | 8 | $3.304\times10^{-3}$ | 11.69 |
| 0.06250 | 16 | $5.959\times10^{-4}$ | 5.54 |
| 0.03125 | 32 | $1.282\times10^{-4}$ | 4.65 |

The ratio approaches $4$ as $\varepsilon$ falls, which is the signature of second
order; the measured log-log slope over this range is $-3.21$, steeper than the
asymptotic $-2$ because the largest steps are far from the asymptotic regime. The
honest statement is that the error is $\mathcal{O}(\varepsilon^2)$ *asymptotically*
and that the demo's largest steps are not in that regime. A fitted slope quoted as
if it were the asymptotic exponent would be a misreading.

**Why the Metropolis step is still needed.** The numerical trajectory conserves
$\tilde H$, not $H$, so $H$ changes by $\mathcal{O}(\varepsilon^2)$ and the
proposal $\exp[-H(m',p')]$ is not exactly $\exp[-H(m,p)]$. Accepting the proposal
with probability $\min(1, e^{-\Delta H})$ removes that bias exactly, converting a
slightly wrong dynamics into a slightly inefficient exact sampler. Without it,
the sampler would systematically drift.

## 4. The HMC algorithm

Given a current state $m$:

1. Draw $p_0 \sim \mathcal{N}(0,M)$.
2. Integrate the leapfrog scheme for $L$ steps with step size $\varepsilon$,
   obtaining $(m',p')$.
3. Accept $m'$ with probability $\min(1, e^{-\Delta H})$, where
   $\Delta H = H(m',p') - H(m,p_0)$.
4. Discard the momentum (and, for exact reversibility in the derivation, negate
   it; negating is irrelevant to the sampled $m$, since the momentum is
   symmetric).

The negation matters for the *proof* — it is what makes the leapfrog map exactly
reversible in the augmented space — and not for the output. The demonstration
implements the negated form and notes this in the code.

## 5. Trajectory length: measured, not guessed

With $\varepsilon = 0.25$ fixed, the demonstration sweeps $L$ on the
correlated 2-D target:

| $L$ | acceptance | $\tau$ | ESS of 3000 draws | ESS per gradient evaluation |
|---|---|---|---|---|
| 1 | 0.960 | 92.1 | 33 | 0.0081 |
| 2 | 0.950 | 31.6 | 95 | 0.0119 |
| 5 | 0.961 | 3.7 | 809 | 0.0404 |
| **10** | **0.948** | **1.0** | **3000** | **0.0750** |
| 20 | 0.970 | 1.0 | 3000 | 0.0375 |
| 40 | 0.955 | 4.7 | 641 | 0.0040 |

Each iteration costs $L$ gradient evaluations, so the raw ESS is the wrong
currency. The last column is the honest score, and it peaks at $L = 10$: at
$L = 40$ the path is so long that it curls back and the state returns near where
it started, so the extra gradients are wasted. This is the phenomenon that the
**No-U-Turn Sampler** automates: NUTS doubles and then reverses the trajectory
until continuing would reduce the distance between the ends, so the path length is
chosen per iteration from the geometry rather than fixed in advance. The step
size in that scheme is set by dual averaging during warm-up to a target
acceptance probability, and both are frozen before the sampling phase.

Notice also that the acceptance rate is almost constant across the table
($0.948$ to $0.970$) while the ESS varies by a factor of $90$. Acceptance and
information are, once again, different things.

## 6. Preconditioning, measured

The mass matrix $M$ is not a free parameter but a choice of metric. If the target
is anisotropic, a single step size cannot serve both a narrow and a wide
direction, and the efficiency collapses. The demonstration makes this quantitative
with a second SYNTHETIC target,

$$
C_B = \begin{bmatrix}1&9\\9&100\end{bmatrix},
\qquad
\text{eigenvalues } (0.188,\ 100.812),
\qquad
\text{condition number } 535,
$$

and scans the step size for each choice of mass matrix, at $L = 10$, reporting
the best ESS per gradient evaluation:

| mass matrix | best $\varepsilon$ | best ESS of 6000 draws | ESS per gradient |
|---|---|---|---|
| $M = I$ | 0.010 | 52 | 0.00087 |
| $M = \operatorname{diag}(\operatorname{Var})$ | 0.100 | 5000 | 0.08333 |
| $M = C_B^{-1}$ | 0.050 | 5000 | 0.08333 |

A covariance-matched mass matrix is worth a factor of about $96$ here. The
message is not that a diagonal mass matrix is as good as the inverse covariance in
general — on this target the correlation structure happens to be mild enough that
the diagonal already suffices — but that **the metric is the important knob, and
the step size is a consequence of it**.

Two practical cautions. First, $C_B$ is known in this synthetic example; in a real
inversion it must be estimated, typically from a short pilot run or from a
Laplace approximation at the posterior mode, and the estimate must then be
**frozen**: continuing to adapt the metric during sampling breaks the
stationarity that every diagnostic in [04](04-mcmc.md) depends on. Second, when
the parameter count is large, a dense mass matrix is itself expensive; the usual
compromise is a diagonal or low-rank-plus-diagonal preconditioner built from the
inverse Hessian of the misfit.

## 7. HMC versus random walk, costed honestly

The comparison must charge HMC for its gradients. On the same target, with
$n = 8000$ iterations:

| sampler | acceptance | $\tau$ | ESS | likelihood evaluations | ESS per evaluation |
|---|---|---|---|---|---|
| HMC, $\varepsilon = 0.25$, $L = 10$ | 0.953 | 1.0 | 7000 | $80\,000$ | 0.08750 |
| RWM, step 1.5 | 0.199 | 24.5 | 285 | $8\,000$ | 0.03567 |

The ratio is $2.45$ in favour of HMC. That is a real but modest gain, and it is
modest precisely because this target is easy: a 2-D Gaussian with correlation
$0.9$ is exactly the kind of target a tuned random walk handles. On a stiff,
high-dimensional target the gap is much larger, because the random walk's
autocorrelation time grows with the condition number while HMC's grows far more
slowly. The correct conclusion from the table is *not* "HMC is $2.45$ times
better"; it is **"on a Gaussian target in two dimensions, with a tuned step, the
gradient buys a factor of a few — so measure the target before paying for
gradients"**.

## 8. What "modern sampler" adds

Four developments sit between the textbook HMC above and a production sampler.

1. **NUTS** — adaptive trajectory length, removing $L$ from the user's
   responsibility and handling the curl-back problem of Section 5 automatically.
2. **Dual averaging for $\varepsilon$** — a stochastic optimisation that drives the
   average acceptance probability to a target during warm-up.
3. **Windowed metric adaptation** — a sequence of warm-up windows in which the
   metric is estimated, then fixed.
4. **Divergence diagnostics** — when the leapfrog error exceeds a threshold the
   trajectory is abandoned, and each such event is recorded. A nonzero divergence
   count is the sampler's own report that the posterior has a region it cannot
   integrate through: a funnel, a hard constraint, or a non-identified direction.
   This is the most useful single diagnostic a modern sampler emits, because it
   localises the difficulty instead of merely reporting inefficiency.

An entirely different family replaces sampling by optimisation of an approximate
density. **Variational inference** fits a tractable $q(m)$ to $p(m\mid d)$ by
maximising the evidence lower bound, and is orders of magnitude faster, at the
price of a bias that is hard to quantify: it reports the width of $q$, not of
$p$. For decision-making under uncertainty, where interval widths drive the
decision, that substitution must be justified case by case. See
[21-03-05 Variational Inference](../../21-statistics-bayesian-ml/03-bayesian-inference/05-variational-inference.md).

## 9. Worked example: energy error to step size

For a Gaussian target with covariance $C$ and mass matrix $M = C^{-1}$, the
leapfrog map acts on each normal mode independently with an effective frequency
$\omega = 1$ in the whitened coordinates. Over a trajectory duration $T$, the
energy error of a symplectic integrator of order $2$ behaves as

$$
\lvert\Delta H\rvert \sim c\,\varepsilon^{2}\,\omega^{3}T
$$

for a coefficient $c$ of order $1$ that depends on the phase of the trajectory.
Solving for the step size that keeps the error below a threshold $\eta$ gives
$\varepsilon \lesssim \sqrt{\eta/(c\omega^3T)}$, which is how a target acceptance
probability is translated into a step size in practice.

Check against the measurement: at $\varepsilon = 0.03125$, $T = 1$ and
$\omega = 1$ the measured mean error is $1.282\times10^{-4}$, so
$c \approx 1.282\times10^{-4}/0.03125^{2} = 0.13$. The empirical coefficient is
indeed of order $0.1$–$1$, and the scaling reproduces the observed ratios
$28.11 / 11.69 / 5.54 / 4.65 \to 4$. The linear-in-$T$ factor is why a longer
trajectory needs a smaller step for the same error, and why the two cannot be
tuned independently.

## 10. Regime of validity

1. **The gradient must exist and be correct.** A finite-difference gradient costs
   $M$ extra forward solves per iteration and usually destroys the advantage. A
   reverse-mode (adjoint) gradient costs a small constant multiple of one forward
   solve and is the basis of large-scale HMC in geophysics.
2. **The density must be differentiable.** Hard bounds are handled by
   transformations (log, logit, spherical) or by a soft penalty; the choice
   changes the sampled measure and must be stated. See
   [18-03-06 Constraints](../03-regularization/06-constraints.md).
3. **Discontinuous or noisy likelihoods break the integrator.** A finite-element
   solver with a mesh-adaptation step, or a likelihood estimated by simulation,
   produces a gradient that does not correspond to the potential, and the
   acceptance rate collapses in a way that no step-size tuning fixes.
4. **The metric must be frozen before sampling.** Adaptation during the sampling
   phase invalidates the diagnostics.
5. **Divergences are evidence, not noise.** A nonzero divergence count means the
   posterior has structure the integrator cannot traverse; report it.
6. **Cost accounting must be explicit.** Report gradient evaluations, not
   iterations, and give ESS per forward solve.

## 11. Demonstration and exercises

[`code/hmc_demo.py`](./code/hmc_demo.py) implements the leapfrog integrator, the
energy-error study, the trajectory-length sweep, the preconditioning comparison
and split $\hat R$ over four chains, prints all tables above with units, and
exits $0$ in about four seconds. Exercises and solutions:
[`exercises/05-hmc-and-modern-samplers-exercises.md`](./exercises/05-hmc-and-modern-samplers-exercises.md),
[`exercises/05-hmc-and-modern-samplers-solutions.md`](./exercises/05-hmc-and-modern-samplers-solutions.md).

## Mastery checkpoint

**(a)** Show that the leapfrog map is exactly reversible: applying it with $+\varepsilon$
then $-\varepsilon$ returns the initial state.
**(b)** For the measured coefficient $c \approx 0.13$ and $T = 1$, estimate the
step size that keeps the mean energy error below $0.01$.
**(c)** A run reports acceptance $0.98$, $\hat R = 1.001$, and a divergence count
of $14$. State the likely cause and the fix.
**(d)** Explain in two sentences why adapting the mass matrix during production
sampling invalidates $\hat R$.

## Common pitfalls

1. **Assuming energy conservation makes the Metropolis step redundant.** The
   integrator conserves $\tilde H$, not $H$.
2. **Tuning the step size and the trajectory length independently.** They trade
   off, as Section 9 shows.
3. **Judging the sampler by acceptance rate.** The measured table spans $0.948$ to
   $0.970$ while the ESS changes by a factor of $90$.
4. **Using a finite-difference gradient in a large problem.** The cost scales with
   the parameter count and erases the advantage.
5. **Ignoring divergence counts.** They localise the failure and are cheap.
6. **Adapting the metric forever.** It makes the chain non-stationary.
7. **Pretending variational inference is sampling.** It reports the width of a
   chosen approximation.

## Further reading

- **Neal, R. M. (2011). MCMC using Hamiltonian dynamics. In *Handbook of Markov
  Chain Monte Carlo*, Chapman & Hall/CRC, 113–162.** Level: research. The
  standard derivation, including the volume-preservation argument used in
  Section 2.
- **Hoffman, M. D., & Gelman, A. (2014). The No-U-Turn Sampler: adaptively setting
  path lengths in Hamiltonian Monte Carlo. *Journal of Machine Learning Research*,
  15, 1593–1623.** Level: research. The adaptive trajectory length of Section 5.
- **Betancourt, M. (2017). A conceptual introduction to Hamiltonian Monte Carlo.
  *arXiv:1701.02434*.** Level: research. The geometric picture behind the metric
  and divergence diagnostics.
- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: research. The adjoint construction of the gradient
  that makes large-scale HMC feasible in geophysics.

## Related modules

- [04 Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs](04-mcmc.md).
- [06 Posterior Summaries](06-posterior-summary.md) — what to do with the draws.
- [18-04-02 Gradient, Gauss-Newton and Full Newton Methods](../04-nonlinear-inversion/02-gradient-and-newton.md)
  — the gradient and Hessian machinery.
- [18-04-03 Conjugate Gradient and Large-Scale Inversion](../04-nonlinear-inversion/03-conjugate-gradient-inverse.md)
  — matrix-free operators, the same tools an adjoint gradient needs.
- [18-09-04 Uncertainty in Learned Inversion: Pitfalls and Calibration](../09-machine-learning-inversion/04-uncertainty-in-learned-inversion.md)
  — where surrogate gradients enter and where they fail.
- [21-03-05 Variational Inference](../../21-statistics-bayesian-ml/03-bayesian-inference/05-variational-inference.md)
  — the fast approximate alternative of Section 8.
