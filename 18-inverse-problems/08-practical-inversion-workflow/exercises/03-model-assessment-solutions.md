# Solutions — 18-08-03 Assessing a Model: Resolution, Artifacts, Alternatives

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC**.

Lesson: [03 Assessing a Model: Resolution, Artifacts, Alternatives](../03-model-assessment.md).

---

## ★1 — The five items

| item | quantity |
|---|---|
| misfit | chi per datum against the stated noise |
| complexity | $\operatorname{tr}R$ effective parameters out of $n$ |
| resolution | PSF half-width (position-dependent) |
| admissibility | perturbation signature and posterior norm |
| alternatives | 95% admitted range per position |

---

## ★2 — Width of a 95% Gaussian range

$$P(|\Delta| < 2\sigma) = 0.9545 ,$$

so the range is **$4\sigma$ wide** (from $-2\sigma$ to $+2\sigma$) for a
Gaussian posterior. Assumption: the posterior is approximately Gaussian — true
for a linear operator with Gaussian errors; an approximation otherwise.

---

## ★3 — Resolution at 6.25 km

PSF half-width: 4.00 km. A 0.5-km feature is eight times narrower than the
resolution length, so it **cannot be resolved**; the perturbation table confirms
this with a signature of 0.212$\sigma$ (not required) at that width.

---

## ★4 — Criteria in disagreement

Data-signature criterion: $0.953 < 1$, so the feature is **not required** (just
below the threshold). Posterior-norm criterion: $0.587 < 1$, so the feature is
**admissible** (within about one posterior standard deviation per cell).

They agree here, and that is the typical pattern for a feature just below
resolution. If they disagreed — signature above 1 but posterior norm far above 1,
or vice versa — the correct action is to check which model is being compared:
the posterior norm is computed with the same $C$ used to produce the model, so a
mismatch usually means the reported covariance does not correspond to the
inversion that produced the model (a different weight, or a nonlinear solution
linearised elsewhere).

---

## ★5 — Spread ratio and the edge

$$\frac{0.5468}{0.3402} = 1.61 .$$

Two reasons the deep edge is worse: (i) **no observation sits over it** — the
observations occupy $z\in[1,19]$ km and the cell at 19.75 km is outside their
range, so no kernel has its maximum there; (ii) the kernel sensitivity decreases
with depth from the near-surface peak in this experiment, so the data
information available at the edge is smaller than in the interior.

---

## ★6 — Is the 6.25 km claim supported?

The claim is "0.30" (presumably a contrast of 0.30 in the model units). The model
value is 0.3884 with a 95% admitted range (0.2094, 0.5674), a width of 0.3580.

The admitted range **does** contain 0.30, so the value is not contradicted. But
the range is *wider than the claim*: the data admit anything from 0.21 to 0.57 at
that depth, so the claim of a specific value is not supported — only the claim of
a value in that interval is.

Rewrite: "the model is $0.39\pm0.18$ (95% admitted range 0.21–0.57) at 6.25 km;
the data require a positive contrast there but do not determine its size to
better than about a factor of two."

---

## ★7 — Assessment without a linear resolution matrix

- **Misfit:** chi per datum at the MAP model. Cheap (one forward run).
- **Complexity:** effective parameters estimated from the Hessian at the MAP
  (eigenvalue spectrum of the Gauss–Newton operator) or, for sampling methods,
  from the number of well-constrained principal directions. Moderate cost.
- **Resolution:** replace the PSF with a *nonlinear* spike test: perturb the true
  (or reference) model, re-invert from several starting models, and measure the
  spread of the recovered feature position and amplitude. Cost: one inversion per
  spike, and the result depends on the starting ensemble, so report the range.
- **Admissibility:** re-invert with the feature added and removed from the
  starting model; a feature is required only if the misfit degrades beyond the
  noise in both cases. Cost: two inversions per feature.
- **Alternatives:** sample the posterior (MCMC or a trans-dimensional sampler)
  and tabulate marginal ranges; cost is the dominant one and should be quoted
  (thousands of forward solves).

---

## ★8 — When the posterior norm misleads

Construction: a nonlinear operator whose curvature varies strongly with the
model. Take a resistivity problem with an exponential sensitivity: at the
linearisation point the posterior covariance $C$ is very tight in one direction,
so the posterior norm of a perturbation in that direction is > 1 and it is
declared inadmissible. If the nonlinear forward response saturates, however, the
data may be almost unchanged by that perturbation — the perturbation is
consistent with the data even though the linearised posterior rejects it.

Detection: compute the *actual* data change by forward-modelling the perturbed
model (the signature criterion, which is exact for any model) and compare it with
the linearised prediction. A large disagreement between the two is the signal
that the posterior norm is unreliable, and the remedy is a nonlinear sampling of
the alternatives rather than the linear $C$.
