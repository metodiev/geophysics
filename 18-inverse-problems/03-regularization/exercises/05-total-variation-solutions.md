# Solutions — 18-03-05 Total Variation and Edge-Preserving Inversion

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted as printed.

Lesson: [05 Total Variation and Edge-Preserving Inversion](../05-total-variation.md).
All models are **SYNTHETIC**.

---

## ★1 — Two-sample step at $\alpha = 0.3$

Assume $x_2 > x_1$, so $\partial|x_2-x_1|/\partial x_2 = +1$ and
$\partial/\partial x_1 = -1$. Stationarity:

$$x_1 - \alpha = 0 \;\Rightarrow\; x_1 = 0.3, \qquad
(x_2-1)+\alpha = 0 \;\Rightarrow\; x_2 = 0.7 .$$

The assumption $x_2 > x_1$ holds since $0.7 > 0.3$. The recovered step is
$0.7-0.3 = 0.4 = 1-2\alpha$, against a true step of $1.0$: TV shrank it by
$2\alpha = 0.6$, i.e. by $60\%$.

**Check.** Objective at $(0.3,0.7)$:
$\tfrac12(0.09+0.09) + 0.3(0.4) = 0.09+0.12 = 0.21$. Objective at the
unregularised $(0,1)$: $0+0.3 = 0.3$. Objective at the constant $(0.5,0.5)$:
$0.25+0 = 0.25$. The computed point is the best of the three, as it must be.

---

## ★2 — Annihilation thresholds

$$\alpha^\star = h/2: \quad h = 3.90 \Rightarrow \alpha^\star = 1.95, \qquad
h = 0.60 \Rightarrow \alpha^\star = 0.30 .$$

A single $\alpha$ therefore treats the two contrasts very differently: at
$\alpha = 1.95$ the strong layer is exactly annihilated while the weak one
vanished long before, at $\alpha = 0.30$ — a factor of $6.5$ earlier. **TV is not
scale-free in the model**: a survey with both weak and strong contrasts cannot be
tuned by one parameter without deciding which of the two to preserve. The
demonstration's chosen $\alpha = 3.2\times10^{-2}$ is far below both thresholds,
which is why all recovered amplitudes are within $1\%$ — but the same mechanism
still shrinks the weak contrasts more, in relative terms, than the strong ones.

---

## ★3 — The ADMM $z$-update

$$z^{k+1} = \mathrm{soft}\left(Dm^{k+1}+u^k,\ \alpha/\rho\right).$$

The **threshold** is $\alpha/\rho$: it carries the penalty weight $\alpha$ and is
inversely proportional to the augmented-Lagrangian parameter $\rho$. The
**penalty weight** in the original problem is $\alpha$; $\rho$ is an algorithmic
parameter that does not change the minimiser but changes the conditioning and the
convergence rate. Confusing the two is a common source of "the result depends on
$\rho$" confusion — it does not, once the iteration has converged, and the
demonstration's primal/dual residuals are what certify that it has.

---

## ★★4 — Edge widths as fractions of the source depth

| objective | width (m) | width / 1500 m |
|---|---|---|
| Tikhonov $L=I$ | 960 | 0.64 |
| Tikhonov $L=D$ | 1006 | 0.67 |
| TV | 325 | 0.22 |

The source depth sets the intrinsic resolution: two cells closer than roughly the
depth produce nearly indistinguishable data, so a quadratic penalty — which must
spread a step over a distance determined by the spectrum — produces transitions
of order the depth, as measured ($0.64$–$0.67$). TV produces a transition
**three times narrower than the resolution the data can support**. That is
possible only because the prior supplies the missing information: the model is
*declared* piecewise constant, so a 325 m transition is not evidence of
resolution but an artefact of the assumption. If the assumption is wrong, the
narrow transition is wrong by the same amount it is sharp.

---

## ★★5 — Can the residual select the penalty?

| model | objective | res$^2/(n\sigma^2)$ at best $\alpha$ |
|---|---|---|
| blocky | Tikhonov $L=I$ | 0.659 |
| blocky | Tikhonov $L=D$ | 0.660 |
| blocky | TV | 0.878 |
| ramp | Tikhonov $L=I$ | 1.475 |
| ramp | Tikhonov $L=D$ | 0.940 |
| ramp | TV | 0.751 |

All six values lie within a factor of $1.5$ of $1.0$, i.e. every penalty can fit
the data to the noise level. Meanwhile the model errors differ by a factor of
$13.6$ on the blocky model and $4.6$ on the ramp. **The residual cannot select the
penalty**: it is a test of the fit, and all three priors are capable of a fit
consistent with the noise. The residual is necessary — a value far from $1$
falsifies the combination of penalty and parameter (as TV at
$\alpha = 10^{1}$ on the ramp does, with ratio $103$) — but it is not sufficient
to choose the prior.

---

## ★★6 — Which penalty is right for the ramp?

$$\frac{0.02608}{0.00570} = 4.58 .$$

First-order Tikhonov's error is $4.6$ times smaller than TV's on a model that is
a smooth ramp, and it achieves that with **zero** spurious jumps. TV's prior —
piecewise constancy — is false for a ramp, so its steps are artefacts and its
error is larger. **The "right" penalty is the one whose prior matches the Earth**,
and on a ramp that is the smoothness penalty. The measurement is symmetric with
Section 3 of the lesson, where the same two penalties swap places by a factor of
$13.6$ on a blocky model.

---

## ★★★7 — Why the sweep is cheap

The augmented-Lagrangian $m$-update is

$$m^{k+1} = \left(K^{\mathsf T}K+\rho D^{\mathsf T}D\right)^{-1}
\left(K^{\mathsf T}d + \rho D^{\mathsf T}(z^k-u^k)\right).$$

The matrix $K^{\mathsf T}K+\rho D^{\mathsf T}D$ contains $\rho$ but **not**
$\alpha$: $\alpha$ acts only through the soft threshold in the $z$-update. So for
a fixed $\rho$ the matrix can be factorised once (a Cholesky factorisation of a
$100\times100$ banded matrix here) and every subsequent $m$-update is two
triangular solves.

**Cost implication.** A 37-point $\alpha$ sweep costs one factorisation plus
$37\times(\text{iterations})\times(\text{two solves})$. Solving each $\alpha$
from scratch would repeat the factorisation 37 times. For problems where the
factorisation dominates (large $n$, dense $K$), the saving is a factor of order
the number of $\alpha$ values; for the demonstration's small banded system the
saving is smaller but the same structure holds. Note the limitation: this reuse
requires a **fixed** $\rho$; adaptive-$\rho$ schemes lose the saving and must
justify the change.

---

## ★★★8 — Distinguishing real steps from created steps

**Statistic.** The step count $N(\sigma)$ — the number of adjacent-cell
differences exceeding $3\times$ the largest *true-looking* smooth variation — as
a function of the noise level $\sigma$, at a fixed $\alpha$ and a fixed model
grid.

**Design.** Use the ramp model (no steps) and a blocky model with known steps;
generate 50 realisations at each of four noise levels
($0.05\%$, $0.5\%$, $5\%$, $20\%$ of the peak anomaly); solve TV at the
$\alpha$ chosen by the discrepancy principle for each realisation; record
$N(\sigma)$ and the amplitudes of the counted steps.

**Expected behaviour.**

- *Created steps:* $N$ **grows** with the noise level (more noise, more steps),
  and each counted step's amplitude scales with the noise level.
- *Real steps:* $N$ is **invariant** to the noise level (it equals the number of
  true interfaces, or saturates there) and each amplitude is invariant.

**Discrimination.** A monotone increase of $N$ with $\sigma$ falsifies the claim
that the steps are real. The known-truth blocky model calibrates the statistic
before it is applied to a field data set, which is the honest order of
operations.
