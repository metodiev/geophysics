# Solutions — 18-03-07 Regularisation of Nonlinear Problems

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted as printed.

Lesson: [07 Regularisation of Nonlinear Problems](../07-nonlinear-regularization.md).
All models are **SYNTHETIC**.

---

## ★1 — Three Gauss–Newton iterations

$F(u) = e^{-u}$, $d = 0.5$, $u^\star = \ln 2 = 0.693147$.

| iteration | $u$ | $F(u)$ | $F-d$ | $J = -e^{-u}$ | $\delta = -J^{\mathsf T}(F-d)/(J^{\mathsf T}J)$ | error |
|---|---|---|---|---|---|---|
| 0 | 0.000000 | 1.000000 | $+0.500000$ | $-1.000000$ | $+0.500000$ | $0.693147$ |
| 1 | 0.500000 | 0.606531 | $+0.106531$ | $-0.606531$ | $+0.175639$ | $0.193147$ |
| 2 | 0.675639 | 0.508831 | $+0.008831$ | $-0.508831$ | $+0.017355$ | $0.017508$ |
| 3 | 0.692995 | 0.500076 | $+0.000076$ | $-0.500076$ | $+0.000152$ | $0.000152$ |

For one parameter the Gauss–Newton equation reduces to
$\delta = -(F-d)/J$, which is what the table evaluates.

Error ratios: $0.693147 \to 0.193147 \to 0.017508 \to 0.000152$, i.e.
$0.279$, $0.0906$, $0.00868$ — **collapsing towards zero**, the signature of
superlinear convergence for an undamped step with a zero-residual solution.

---

## ★2 — The optimal difference step

$$h^\star \approx \epsilon^{1/3} = (2.2\times10^{-16})^{1/3} = 6.04\times10^{-6}.$$

The measured optimum is $h = 10^{-5}\ \mathrm{km}$ with deviation
$1.073\times10^{-8}$, and the neighbouring values
($h = 10^{-4}$: $8.920\times10^{-7}$; $h = 10^{-6}$: $4.974\times10^{-8}$) bracket
it. The estimate $6\times10^{-6}$ and the measured $10^{-5}$ agree to a factor of
$1.7$ — which is as much as the $O(1)$ constant in the estimate can promise. The
deviation at the optimum, $1.1\times10^{-8}$, is far smaller than the
$8.9\times10^{-3}$ at $h = 10^{-2}$: **choosing the step badly costs five orders
of magnitude in Jacobian accuracy.**

---

## ★3 — The damped, penalised system

$$\left(J_k^{\mathsf T}J_k + (\alpha+\lambda)I\right)\delta
= -\left(J_k^{\mathsf T}r_k + \alpha u_k\right),
\qquad r_k = d - F(u_k),\ u_{k+1} = u_k+\delta .$$

- $\lambda$ is the **damping** (Levenberg–Marquardt): it makes the step shorter
  and more like steepest descent when the linearisation is unreliable.
- $\alpha$ is the **regularisation parameter**: it encodes the prior and changes
  the estimator, not just the path to it.
- $u_k$ is the **linearisation point**: the step is only valid in a neighbourhood
  of it, and both $\alpha$ and the start determine which neighbourhood the
  iteration visits.

$\lambda$ does not appear in the objective and $\alpha$ does; conflating them is
the most common error in reporting a nonlinear inversion.

---

## ★★4 — Convergence from the step norms

**Order: linear.** A ratio that settles at a constant below one (here about
$0.30$–$0.31$ over iterations 12–15) is linear convergence. Over ten further
iterations the step norm — and, near the solution, the error — falls by
$0.3^{10} = 5.9\times10^{-6}$.

A quadratic method has $e_{k+1} \approx C e_k^2$, so the *ratio* $e_{k+1}/e_k
\approx Ce_k$ falls in proportion to the remaining error: as $e_k\to0$ the ratio
collapses. The measured ratios are flat, which is the fingerprint of the damping:
Levenberg–Marquardt trades the convergence order for a guaranteed decrease in the
objective.

---

## ★★5 — The depth–density error split

$$\Delta\text{depth} = 0.29739-0.27381 = +0.02358\ (+8.6\%),$$
$$\Delta\text{density} = 0.15912-0.31140 = -0.15228\ (-48.9\%).$$

Raising $\alpha$ from $10^{-10}$ to $10^{-6}$ makes the densities **much** more
accurate and the depths slightly worse. The mechanism is the trade-off: depth and
density trade off against each other in the gravity kernel, so a prior that
shrinkages amplitudes (which is what a magnitude penalty does) suppresses the
noise-driven density oscillations and makes the depth estimate, which is inflated
when the densities are wrong, slightly more conservative. The whole-vector error
improves ($0.29821 \to 0.21997$) even though one block degrades. **A single
"model error" number hides which parameter group the prior helped and which it
hurt**, and it is the reason inversion reports should quote per-block errors.

---

## ★★6 — The equivalence class at the noise level

$$n\sigma^2 = 3.7127\times10^{-5}, \qquad
\text{data term} = 2.302913\times10^{-5} = 0.620\,n\sigma^2,$$

$$\text{admissible extra data term} = (1-0.620)\,n\sigma^2
= 0.380\times3.7127\times10^{-5} = 1.410\times10^{-5}.$$

Moving along $v_{-5}$ by the measured step raises the data term until
$\chi^2/(n\sigma^2) = 1.000$ exactly (the demonstration prints $1.000$), with a
depth change of up to $0.6479\ \mathrm{km}$.

**Is the alternative rejectable?** No: by construction its misfit equals the
noise level, so it is exactly as consistent with the data as the reported
solution. The two models differ by $0.65\ \mathrm{km}$ in depth against a ridge
amplitude of $2.2\ \mathrm{km}$ — a 29% change in the very quantity the survey
was meant to measure, at no cost in goodness of fit. This is the measured content
of "the solution is not unique".

---

## ★★★7 — IRLS weights

The smoothed penalty is $\phi(Dz) = \sqrt{(Dz)_k^2+\epsilon}$ per component, with

$$\frac{\mathrm d}{\mathrm d(Dz)_k}\sqrt{(Dz)_k^2+\epsilon}
= \frac{(Dz)_k}{\sqrt{(Dz)_k^2+\epsilon}}
= \frac{(Dz)_k}{1/w_k}
\;\Rightarrow\; w_k = \frac{1}{\sqrt{(Dz)_k^2+\epsilon}} .$$

So the smoothed penalty's gradient is exactly $w_k(Dz)_k$, i.e. a weighted
least-squares gradient with weights $w_k$. **As $\epsilon\to0$**: for
$(Dz)_k \ne 0$ the weight tends to $1/|(Dz)_k|$ and the penalty tends to
$|(Dz)_k|$; for $(Dz)_k = 0$ the weight tends to $1/\sqrt\epsilon \to \infty$,
which is the discrete expression of the fact that the subdifferential of
$|\cdot|$ at zero is the whole interval $[-1,1]$ — an infinite set of
subgradients. A finite $\epsilon$ replaces that set with a very steep but finite
slope, which is why the algorithm drives small differences to *exactly* zero
rather than merely small (the measured $\max|Dz| = 0.0000$ at every $\alpha$
in the demonstration).

---

## ★★★8 — Error split versus penalty operator

**Design.** Four penalties on the same nonlinear problem, same data, same start,
each at its own oracle $\alpha$:

1. $\Omega = \|u\|^2$ (magnitude, both blocks) — the demonstration's case;
2. $\Omega = \|Dz\|^2$ (depth roughness only);
3. $\Omega = \|Da\|^2$ (density roughness only);
4. $\Omega = \|Dz\|^2 + \|Da\|^2$.

**Statistic.** The pair $\big(\text{rel. error in depths},\ \text{rel. error in
densities}\big)$ at each penalty's best achievable total error, plus the total.

**Predictions.**

- Magnitude only (1): shrinks both blocks towards zero → density error falls,
  depth error rises (the measured pattern of ★★5).
- Depth roughness only (2): the depth profile must become smooth, which is
  approximately true here (a Gaussian ridge), so the depth error should fall; the
  densities absorb the remaining misfit and their error should rise.
- Density roughness only (3): the density profile is already constant, so the
  penalty is nearly inactive; the depths should absorb the misfit and the depth
  error should behave much as unregularised.
- Both (4): intermediate, with the total error no better than the best of the
  single-block penalties unless one prior is genuinely right.

**Falsification.** If the depth error is *insensitive* to which block is
penalised, then the two blocks are not traded off in this geometry, and the
premise that $\alpha$ controls the split would be wrong. The measured change
between $\alpha = 10^{-10}$ and $10^{-6}$ (+8.6% depths, −48.9% densities) is
evidence against that outcome, but the experiment is what settles it for the
other three penalties.
