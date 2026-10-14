# Solutions — 18-07-04 Sequential vs Simultaneous Inversion

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC**.

Lesson: [04 Sequential vs Simultaneous Inversion](../04-sequential-vs-simultaneous.md).

---

## ★1 — Precisions

$$P_{\text{joint}} = P_a + P_b + P_0,\qquad
P^{(1)} = P_b + P_0,\qquad P^{(2)} = P_a + P^{(1)} .$$

$P_a$ and $P_b$ are the data information matrices
($G_i^{T}C_i^{-1}G_i$); $P_0$ is the prior precision.

---

## ★2 — Substitution

$$P^{(2)} = P_a + P^{(1)} = P_a + \left(P_b + P_0\right) = P_a + P_b + P_0
= P_{\text{joint}} .$$

Assumptions: (i) the two data error vectors are **independent** (so the
information matrices add), and (ii) both stages act on the **same** model vector,
so the stage-1 posterior can serve as a prior for the same unknowns.

---

## ★3 — Risk reduction

From $G_1$ alone: $(6.0483 - 0.7777)/6.0483 = 87.1\%$.
From $G_2$ alone: $(1.3060 - 0.7777)/1.3060 = 40.5\%$.

The weak data set benefits far more from being combined, which is the expected
pattern: the joint posterior is limited by whichever directions remain poorly
informed by both.

---

## ★4 — Round-off amplification

Double precision carries about $1.6\times10^{-16}$ relative error. Amplification
through the normal equations of a matrix with condition number $\kappa$ scales
roughly as $\kappa$ (and as $\kappa^2$ for the normal-equation route), so with
$\kappa = 3.098\times10^3$ expect errors of order

$$1.6\times10^{-16}\times3.1\times10^{3} \approx 5\times10^{-13},$$

or up to $\sim\!10^{-9}$–$10^{-10}$ if the squared condition number is the
relevant amplification. The observed $3.2$–$4.4\times10^{-10}$ is consistent
with the squared-conditioning estimate, so both orderings agree to the precision
the linear algebra permits. Reporting them as "identical" is justified only with
this estimate attached.

---

## ★5 — Crossing point and calibration target

The ratio rms/$\sigma$ is 0.50, 0.70, 0.97, 1.47 at $\alpha = 1,2,4,10$; it
crosses 1 between $\alpha = 4$ and $\alpha = 10$, near $\alpha \approx 4.2$.

For a perfectly calibrated Gaussian estimator, the *rms* error equals the
reported standard deviation, so the target ratio is **1.0**. (For the mean
absolute error the target would be $\sqrt{2/\pi}\approx0.80$.) At $\alpha=1$ the
workflow is over-conservative by this measure (ratio 0.50, intervals twice as
wide as needed); by $\alpha = 10$ it is over-confident (ratio 1.47).

---

## ★6 — Misfit and noise level

If the stated noise were under-estimated by a factor $f$, every chi would be
under-stated by the same factor. The frozen-stage chi of 2.346 corresponds to a
true ratio of $2.346/f$. For the frozen stage to look acceptable ($\chi\approx1$)
one would need $f \approx 2.35$, i.e. a noise level 2.35 times larger than
stated — which is exactly the rationalisation a careless analyst reaches for when
the residual is unpleasant.

The point of stating the noise first is that this rationalisation becomes
visible: either the noise was wrong from the start (a documented change) or the
model is missing something. Fixing the noise after seeing the residual makes the
chi test unfalsifiable.

---

## ★7 — Order dependence for a nonlinear problem

Workflow: stage A inverts data set 1 for a smooth background; stage B inverts
data set 2 for a perturbation, linearised about stage A's model.

Demonstration: run A→B and B→A on the same data from the same synthetic truth,
with both stages using the same convergence criterion, and report

$$\Delta = \frac{\left\|\mathbf{m}_{A\to B} - \mathbf{m}_{B\to A}\right\|}
{\left\|\mathbf{m}_{A\to B}\right\|}$$

together with the final misfit of each ordering. Order dependence is established
if $\Delta$ exceeds the round-off estimate of ★4 by orders of magnitude.

Control: repeat with a linear forward model on the same grids and show
$\Delta$ collapses to round-off — that isolates nonlinearity as the cause.

Decision rule: choose the ordering whose *final* misfit is lower **and** whose
result is stable under a small change in the starting model; if the two orderings
give different answers with comparable misfits, report both as admissible models
rather than selecting one.

---

## ★8 — Bias from a frozen geometry

Write the geometry parameters $\mathbf{h} = \mathbf{h}_0 + \delta\mathbf{h}$ and
the properties $\mathbf{m}$. Data set 2 is $G_2(\mathbf{h})\mathbf{m}$. The joint
solution solves for both; the frozen workflow fixes $\mathbf{h} = \hat{\mathbf{h}}$
from stage 1. To first order in $\delta\mathbf{h}$,

$$G_2(\mathbf{h})\mathbf{m} \approx G_2(\mathbf{h}_0)\mathbf{m}
+ J_h\,\delta\mathbf{h}\,\mathbf{m}, \qquad
J_h = \frac{\partial G_2}{\partial\mathbf{h}} ,$$

so freezing the geometry leaves a residual $J_h\,\delta\mathbf{h}\,\mathbf{m}$
that the property inversion must absorb. The induced bias is

$$\delta\mathbf{m} \approx -\left(G_2^{T}C_2^{-1}G_2\right)^{-1}
G_2^{T}C_2^{-1}J_h\,\delta\mathbf{h}\,\mathbf{m},$$

i.e. the inverse operator acting on the geometry-error term. The quantity to
report alongside the properties is the norm of this term divided by the data
noise — the propagated geometry error expressed in the second data set's chi
units — together with the posterior covariance of $\hat{\mathbf{h}}$ from
stage 1.
