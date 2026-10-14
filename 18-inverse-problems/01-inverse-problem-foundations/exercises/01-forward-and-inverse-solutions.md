# Solutions — 18-01-01 Forward vs Inverse Problems and the Practical Asymmetry

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Lesson: [01 Forward vs Inverse Problems](../01-forward-and-inverse.md).

---

## ★1 — Shapes and units

$M = 4$ model parameters, $N = 25$ data, so $G$ is $25\times4$. Each entry is a
sensitivity $\partial d_i/\partial m_k$, hence the unit is
$\mathrm{mGal\,kg^{-1}}$ — data unit per model unit. (Equivalently
$10^{-5}\ \mathrm{m\,s^{-2}\,kg^{-1}}$.)

---

## ★2 — Forward gain

(a) $0.001904/0.010000 = 0.1904$.

(b) Gravity of a finite body is a smooth, decaying function of distance, so
distinct source configurations separated by small distances produce almost the
same surface field: the operator averages rather than differentiates, and its
norm is below $1$ in these normalised units.

---

## ★3 — Sensitivity ratio and anomalies

Ratio: $7.5174\times10^{-12} / 9.0512\times10^{-13} = 8.305$.

Anomalies: multiply each column norm by $10^{10}\ \mathrm{kg}$:

- $1\ \mathrm{km}$: $7.5174\times10^{-12}\times10^{10} = 0.07517\ \mathrm{mGal}$
- $2\ \mathrm{km}$: $0.02562\ \mathrm{mGal}$
- $3\ \mathrm{km}$: $0.01394\ \mathrm{mGal}$
- $4\ \mathrm{km}$: $0.00905\ \mathrm{mGal}$

---

## ★4 — Bound versus expectation

(a) Worst case: $0.002\times363 = 0.726$, i.e. about $73\%$.

(b) Expected: $0.002\times166.5 = 0.333$, i.e. about $33\%$.

The factor is $73/33 = 2.2$. The $\kappa$ bound assumes all the error is
concentrated in the smallest singular direction; white noise spreads its energy
over all directions, so the mean is smaller. Use $\kappa$ for the worst case,
the measured gain for a planning estimate.

---

## ★5 — Required precision for a 5% model error

Noise fraction $= 0.05/166.5 = 3.0\times10^{-4} = 0.030\%$ of peak.

$$3.0\times10^{-4}\times0.10104 = 3.03\times10^{-5}\ \mathrm{mGal}\ \text{rms}.$$

An instrument with $5\times10^{-5}\ \mathrm{mGal}$ rms is a factor
$5/3.03 = 1.65$ noisier, so the model error would be
$5\times10^{-5}/0.10104\times166.5 = 0.0824$, i.e. about $8.2\%$ — short of the
target. Either improve the instrument by a factor $1.65$ or change the geometry
(which changes the gain).

---

## ★6 — Evaluating the proposal

The kernel depends on $x$ and $z$ only through $x/z$; scaling all depths and all
offsets together leaves $G$ unchanged entry by entry, and the demonstration
measured the *identical* condition number $3.6307\times10^{2}$ for the halved
survey. Halving the station *spacing* at fixed spread does not change the
ratio of spread to depth, so it mostly adds redundant (nearly collinear) rows: the
condition number of $G$ barely moves, while $\lVert G\rVert$ grows and the
orthogonal complement dimension falls. The proposal buys a smaller misfit floor,
not better model recovery. Improvement has to come from a different *kind* of
measurement — for example the borehole levels of
[18-01-02](../02-hadamard-well-posedness.md) — or from a deeper *spread* relative
to the target depth.

---

## ★7 — Experiment design (specification)

**Geometry.** Four density levels cannot be resolved by surface gravity with a
low condition number; the honest specification is a *layered* survey with
borehole gravity:

- target: four levels spanning $2.5$–$4.0\ \mathrm{km}$;
- surface readings on a profile of at least $4$ times the shallowest target depth
  (spread $\pm12\ \mathrm{km}$ for a $3\ \mathrm{km}$ target), so that
  $x/z \in [-4,4]$ is sampled;
- borehole gravimeter levels at the four level mid-points, giving four rows with
  distinct sign patterns (the slab convention of
  [18-01-02 §3.1](../02-hadamard-well-posedness.md)).

**Predicted conditioning.** By scale invariance, the surface-only conditioning for
this depth range is the same as at $1$–$4\ \mathrm{km}$ with a $\pm12\ \mathrm{km}$
spread, i.e. $\kappa \approx 3.6\times10^{2}$, gain $\approx 1.7\times10^{2}$.
Adding four independent borehole rows raises the rank by four and should reduce the
gain by roughly an order of magnitude.

**Pre-survey check.** Build $G$ from the *planned* geometry and compute
(i) the singular spectrum, (ii) the numerical rank at the expected data-precision
tolerance (here $0.05\%$ of peak $\Rightarrow$ relative tolerance
$5\times10^{-4}$), (iii) the number of singular values above that tolerance versus
the four parameters you intend to report. If the count is below four, the design
cannot deliver the deliverable — change it before spending money.

---

## ★8 — Why the gain is constant

For $\mathbf{d} = G\mathbf{m}_{\text{true}} + \mathbf{e}$ with an unbiased
estimator $\hat{\mathbf{m}} = G^{+}\mathbf{d}$,

$$\hat{\mathbf{m}} - \mathbf{m}
= G^{+}\mathbf{e},\qquad
\lVert G^{+}\mathbf{e}\rVert \le \sigma_{\min}^{-1}\lVert\mathbf{e}\rVert .$$

Scaling $\mathbf{e}$ by a factor $c$ scales the error by exactly $c$: the
*normalised* gain $\lVert G^{+}\mathbf{e}\rVert\sigma_{\min}/\lVert\mathbf{e}\rVert$
is independent of the scale of $\mathbf{e}$. Noise realisations differ only in the
random direction of $\mathbf{e}$ relative to the singular vectors, which averages
out over realisations.

Two mechanisms that break constancy:

1. **A regularised (e.g. damped) estimator.** The filter factors
   $\sigma/(\sigma^{2}+\alpha^{2})$ suppress small singular directions, so the
   effective gain *falls* as the noise grows if $\alpha$ is chosen from the noise
   level — which is precisely why discrepancy-based methods exist
   ([18-03-03](../../03-regularization/03-parameter-choice.md)).
2. **A nonlinear or clipped step.** Non-negativity constraints, bound constraints
   or explicit truncation of the model make the estimator nonlinear: large noise
   realisations are projected back, so the gain *saturates* (grows sublinearly)
   as the noise level rises.
