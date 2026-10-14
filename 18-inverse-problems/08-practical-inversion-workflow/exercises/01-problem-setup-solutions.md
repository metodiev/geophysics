# Solutions — 18-08-01 Setting Up a Solvable Inverse Problem

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC**.

Lesson: [01 Setting Up a Solvable Inverse Problem](../01-problem-setup.md).

---

## ★1 — Effective parameters and the data count

$\operatorname{tr}R$ is 6.28 (12 cells), 6.46 (20), 6.72 (40), 6.98 (80) — all
above 6, and $5.80$ for the 6-cell grid just below it.

$\operatorname{tr}R \le \operatorname{rank}G \le \min(p, n) = 12$ here: the
effective number of parameters cannot exceed the number of independent
observations, because each parameter beyond that would have to be inferred from
information that does not exist.

---

## ★2 — Threshold for a parameter

$\|G_{:,j}\|\big/\sigma = 0.45/1.0 = 0.45 < 1$: the cell moves the data by less
than the noise, so it is **not** a parameter of the problem — it is a choice of
grid (or, more precisely, a smooth interpolation between cells that are).

For the answer to become yes, either the noise must fall (to below $\sigma =
0.45$, an instrument or stacking question), the cell must be thicker (a coarser
grid), or the sensitivity must rise (a different geometry or a larger property
contrast).

---

## ★3 — Resolution entries

$$R = C\,G^{T}C_d^{-1}G,\qquad R_{jj}\in[0,1].$$

- $R_{jj} = 0.95$: cell $j$ is recovered, 95% of it appears at cell $j$ and 5%
  leaks to neighbours.
- $R_{jj} = 0.31$: cell $j$ is mostly a weighted average of its neighbours; the
  recovered value at $j$ is only 31% "local".
- $\operatorname{tr}R = 4.94$ for a 40-cell model: the data support about five
  independent parameters, so a 40-number model is about eight times
  over-parametrised.

---

## ★4 — Chi below 1

chi per datum is the rms residual divided by the stated $\sigma$. A model
smoother than the truth leaves a residual that can be *smaller* than $\sigma$ on
average: the smoothness penalty acts as extra information, so the fit is
"better than the noise" in the sense that the model does not chase the noise
realisation. chi = 0.424 means the residual is 42% of the stated noise, i.e. the
model is under-fitting (also called over-smoothing).

Report the 12-cell model: it recovers the truth to 0.6921 rms, which is small
relative to the model's own scale, and its chi near 1 says the fit is
consistent with the noise. The caveat: 12 cells is a modelling choice made for
this synthetic example; on real data the grid would be chosen from the
sensitivity table, and the resolution width (more than one cell) would be
reported with the model.

---

## ★5 — An 80-cell grid for a 0.5-km layer

From the table, at 80 cells the cell size is 0.25 km and one cell moves the data
by $0.4507$, i.e. 0.5 times the noise. A single 0.5-km layer spans two such
cells, giving a combined signature of order
$\sqrt{0.4507^2+0.4507^2}\approx0.64$ — still below the noise, so the layer
cannot be resolved by this experiment.

Legitimate uses of the fine grid: (i) making the regularisation isotropic in
physical units so the model is not biased by grid geometry; (ii) providing a
discretisation in which the admitted range can be computed and reported; (iii)
matching a grid required by an external constraint. None of these is a claim
that the fine structure is resolved.

---

## ★6 — Growth of the condition number

Numerical consequences: (i) the normal equations must be solved with a
factorisation that tolerates conditioning (QR or SVD rather than forming
$G^{T}G$), and (ii) any iterative solver needs more iterations and a tighter
tolerance, and round-off amplification grows roughly with the condition number
(here from $\sim2\times10^{2}$ to $\sim4\times10^{3}$).

Interpretive consequence: the model is increasingly determined by the
regularisation rather than by the data; $\operatorname{diag}R$ falls, and the
admitted range widens. A resolved-looking picture on a grid with condition
number $10^{3}$ and $\min\operatorname{diag}R = 0.072$ is mostly smoothing.

---

## ★7 — Resolving a low-velocity layer

Specification: (i) data — a refraction spread long enough that rays turn below
the layer, with first-arrival (or full-waveform) picks at, say, 24 receivers
with $\sigma = 2$ ms; (ii) parameterisation — three layers (above, the
low-velocity layer, below) with depths and velocities, $n = 6$; (iii) the
demonstration quantity — $\operatorname{diag}R$ for the low-velocity layer's
thickness and $\|G_{:,j}\|/\sigma$ for that parameter, reported as a number.

If the layer's signature is below the noise, the honest recommendation is a
different experiment (a wider spread, a borehole, or a different method), not a
finer grid: a hidden low-velocity layer is invisible to first arrivals because
refracted energy from below arrives first regardless of what sits between.

---

## ★8 — Priors and rank

Rank as computed here is defined by a threshold on the *regularised* operator:
adding $P_0$ raises every singular value, so with a threshold on the
*unregularised* operator the rank is prior-independent, but the resolution
matrix and $\operatorname{tr}R$ are not.

Case in point on the demonstration's data: with a weak smoothness the effective
parameter count is much larger and most diagonals stay small; with a strong
smoothness a few low-order directions are resolved almost exactly while the rest
are driven towards zero. Both are correct answers to "how many parameters are
resolved", for two different priors. The count of resolved parameters is
therefore a statement about the pair (data, prior), never about the data alone.
