# Solutions — 08-04-04 MT Inversion: 1-D, 2-D and 3-D Approaches

> **Read after attempting the exercises.** The lesson is
> [04 MT Inversion](../04-mt-inversion.md).

---

## ★1 — Conductance

$$S = \frac{h}{\rho} = \frac{4000\ \mathrm{m}}{20\ \Omega\mathrm{m}}
= 200\ \mathrm{S}\ \left(\text{siemens}\right).$$

Units check: $\mathrm{m}/\left(\Omega\,\mathrm{m}\right) = \Omega^{-1} = \mathrm{S}$.

---

## ★2 — The trade-off

$$\text{misfit: } 0.15181 - 0.06268 = +0.08913 \left(+142\%\right), \qquad
\text{roughness: } 0.3383 - 1.0396 = -0.7013 \left(-67\%\right).$$

Moving from $\mu = 10^{-3}$ to $10^{-1}$ **paid** 142% more misfit and **bought**
a 67% smoother model. Whether that is a good trade depends on whether the extra
misfit takes the model above the noise level: the noise is 0.05885, and 0.15181 is
already 2.6 times it, so at $\mu = 10^{-1}$ the fit has been degraded beyond what
the data justify. The trade-off curve is only informative when read against the
noise level.

---

## ★3 — A static shift of 2

$$\rho_a \to s^{2}\rho_a = 4\,\rho_a, \qquad \phi \to \phi .$$

A fourfold increase in apparent resistivity with an unchanged phase — the shift
that the inversion of Section 5 absorbed into a top layer of $515.6\ \Omega$m
instead of $200\ \Omega$m.

---

## ★★4 — Is $\mu = 10^{-2}$ admitted?

Threshold: $1.10\times0.06087 = 0.066957$. The misfit at $\mu = 10^{-2}$ is
$0.07689 > 0.066957$, so **it is not admitted**: the criterion takes
$\mu = 10^{-3}$ (misfit 0.06268 $< 0.066957$) as the smoothest admissible model.
The purpose of the criterion is to stop the choice from being a matter of taste:
any model admitted by it fits the data to within 10% of the best achievable, and
among those the smoothest is preferred by an explicit, stated rule.

---

## ★★5 — Can the data discriminate the models?

| Model | Misfit | Misfit / noise |
|---|---|---|
| Truth: 20 $\Omega$m over 2 km | 0.06176 | 1.049 |
| 10 $\Omega$m over 1 km | 0.08415 | 1.430 |
| 40 $\Omega$m over 4 km | 0.11518 | 1.957 |

All three are within a factor of two of the noise level, and the differences
between them are of the same order as the noise itself. A formal test — for
instance an $F$-test on the misfit ratio — would be marginal at best, and with 48
data points and a 2% noise level the honest answer is **the data do not
discriminate**: the three models are members of one admissible family, differing
in thickness by a factor of four. What they share is the conductance, and that is
the quantity to report.

---

## ★★6 — Inverting amplitude alone

Once a static shift is present, the *amplitude* of the impedance at every period
is multiplied by the same unknown $s$, so $\rho_a$ is multiplied by $s^{2}$
**everywhere**. A reported top layer of $600\ \Omega$m could therefore be a true
$600/s^{2}\ \Omega$m for any $s$; a shift of 2 gives $150\ \Omega$m, and a shift of
0.5 gives $2400\ \Omega$m. The phase, being invariant, has a unique interpretation
in terms of structure.

Including the phase does not *remove* the ambiguity — it **confines** it: the
phase constrains the shape of the model (where the interfaces are, how the
conductivity varies) and the amplitude then fixes the scale up to $s^{2}$. What
remains is a single unknown per station, which is what a joint inversion with a
shift parameter addresses. Inverting the amplitude alone instead lets the whole
model absorb the shift, so both the scale and the shape come out wrong, as the
Section 5 table shows ($515.6$ and $519.3\ \Omega$m against true $200$ and $20$).

---

## ★★7 — Experiment design (specification)

**Period band.** Choose it from the physics: a $10\ \Omega$m layer at 2 km has a
skin depth equal to its depth at
$T = \pi\mu_0\sigma L^{2} = 3.9478\times10^{-6}\times0.1\times\left(2000\right)^{2}
= 1.58\ \mathrm{s}$, and a thin layer is sensed when $\delta$ spans roughly
$0.3$–$3$ times the layer thickness, i.e. periods from about $0.1$ s to $30$ s.

**Metric.** The misfit difference between two forward models — the true thin layer
and a thick layer of the same conductance — evaluated on a synthetic data set
generated from the thin one. The layer is *resolved* when that difference exceeds
the noise-inflated misfit, e.g. when
$\left\|\mathbf{d}_{\text{thin}}-\mathbf{d}_{\text{thick}}\right\| > 3\sigma_{\text{data}}$.

**Failure.** The discrimination fails when the noise level rises to the level of
the model difference. Since that difference grows with the *fourth* power of the
ratio of layer thickness to skin depth in the thin-sheet expansion, halving the
noise roughly halves the resolvable thickness — a strong, and useful, scaling.

---

## ★★8 — "What the data constrain" (model answer)

> The sounding constrains the **conductance** of the conductive interval to
> $97\pm10$ S, where the range spans the models admitted by the noise level and
> the choice of regularisation. The **depth interval** over which that conductance
> is distributed is bounded below by the shortest period (the top of the
> conductor) and above by the longest period; the inverted models place it between
> about 1.0 and 4.0 km, and the transition width is not resolved. The data do
> **not** determine the resistivity of the conductor (a factor of four range fits
> equally well), the sharpness of its boundaries, or anything beneath the depth
> reached by the longest period. The amplitude is subject to a static shift of
> unknown magnitude; the phase is not.

Every sentence in that paragraph is a statement the demonstration supports with a
number.
