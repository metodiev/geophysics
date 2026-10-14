# Solutions — 11-01-02 Targeting Strategy and Method Selection

> **Read after attempting the exercises.** Numbers below were computed, not
> estimated. All models and parameters are **SYNTHETIC** teaching values.

Lesson: [02 Targeting Strategy](../02-targeting-and-strategy.md).

---

## ★1 — Sphere mass and gravity anomaly

$$V = \frac{4}{3}\pi (120)^{3} = 7.2382\times10^{6}\ \mathrm{m^{3}}, \qquad
M = V\Delta\rho = 7.2382\times10^{6} \times 350 = 2.5334\times10^{9}\ \mathrm{kg}.$$

$$\Delta g = \frac{GM}{z^{2}}
= \frac{6.67430\times10^{-11} \times 2.5334\times10^{9}}{250^{2}}
= \frac{0.169091}{6.25\times10^{4}} = 2.7055\times10^{-6}\ \mathrm{m\,s^{-2}}
= 0.2706\ \mathrm{mGal}.$$

**Same mass in a cube:** the anomaly is unchanged. Outside a spherically
symmetric body the field is that of a point mass; a cube of the same mass and the
same centroid produces nearly the same anomaly directly above the centre (exactly
the same in the far field $z \gg$ body size). This is why gravity cannot
distinguish shape from mass at depth.

---

## ★2 — Magnetic dipole anomaly

$$\frac{B_0}{\mu_0} = \frac{48\times10^{-6}}{4\pi\times10^{-7}}
= 38.197\ \mathrm{A\,m^{-1}},$$

$$m = \kappa \frac{B_0}{\mu_0} V = 0.03 \times 38.197 \times 7.2382\times10^{6}
= 8.2942\times10^{6}\ \mathrm{A\,m^{2}},$$

$$\Delta B = \frac{\mu_0}{4\pi}\frac{2m}{z^{3}}
= 10^{-7} \times \frac{2(8.2942\times10^{6})}{1.5625\times10^{7}}
= 1.0617\times10^{-7}\ \mathrm{T} = 106.2\ \mathrm{nT}.$$

Equivalently $\Delta B = \kappa B_0 V/(2\pi z^{3})$.

---

## ★3 — Skin depth

$$\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}},
\qquad \sigma = \frac{1}{80} = 0.0125\ \mathrm{S\,m^{-1}}.$$

- $f = 50\ \mathrm{Hz}$: $\omega\mu_0\sigma = 314.159 \times 1.25664\times10^{-6}
  \times 0.0125 = 4.9332\times10^{-6}$, so $\delta = \sqrt{4.0542\times10^{5}}
  = 636.7\ \mathrm{m}$.
- $f = 200\ \mathrm{Hz}$: $\delta = 636.7/\sqrt{4} = 318.4\ \mathrm{m}$.
- $f = 800\ \mathrm{Hz}$: $\delta = 636.7/\sqrt{16} = 159.2\ \mathrm{m}$.

Since $\delta \propto f^{-1/2}$, multiplying the frequency by four divides the
skin depth by two.

---

## ★4 — Radiometric attenuation

$$\mu = \frac{\mu}{\rho}\rho = 0.06 \times 1.5 = 0.09\ \mathrm{cm^{-1}},
\qquad \mathrm{HVL} = \frac{\ln 2}{0.09} = 7.70\ \mathrm{cm}.$$

Transmitted fraction across $25\ \mathrm{cm}$:
$e^{-0.09\times25} = e^{-2.25} = 0.1054$, i.e. **10.5%**. About $89.5\%$ of the
signal from beneath the cover is lost, which is why a thin transported cover
hides bedrock radioelement patterns.

---

## ★5 — A self-similar pair: which anomaly is invariant?

**Magnetics.** $\Delta B \propto V/z^{3} = Rb^{3}/z^{3}$ where $Rb$ is the radius.
With $R/z = 0.5$ for both bodies the ratio $(R/z)^{3}$ is identical, so

$$\Delta B_A = \frac{0.02 \times 50\times10^{-6} \times \frac{4}{3}\pi(80)^{3}}
{2\pi(160)^{3}} = 83.33\ \mathrm{nT},$$
$$\Delta B_B = \frac{0.02 \times 50\times10^{-6} \times \frac{4}{3}\pi(160)^{3}}
{2\pi(320)^{3}} = 83.33\ \mathrm{nT}.$$

**Gravity.** $\Delta g \propto \Delta\rho R^{3}/z^{2} = \Delta\rho R (R/z)^{2}$, so at
fixed $R/z$ the anomaly scales with the absolute radius:

$$\Delta g_A = 0.16774\ \mathrm{mGal}, \qquad \Delta g_B = 0.33549\ \mathrm{mGal},
\qquad \frac{\Delta g_B}{\Delta g_A} = 2.00 = \frac{R_B}{R_A}.$$

**Which is invariant:** the magnetic anomaly amplitude, because it depends only on
the dimensionless ratio $R/z$ (and on the contrasts). The gravity amplitude is
*not* invariant: it depends on absolute size at fixed shape. **Consequence for the
inverse problem:** one gravity amplitude and one depth cannot separate radius from
density contrast — a doubling of radius can be offset by a halving of
$\Delta\rho$ — and at large depth the shape information disappears entirely
(lesson §2.1: the formula tends to the point-mass limit). Magnetics does not have
that particular ambiguity but inherits the same problem in the $(R,z)$ pair for a
fixed amplitude.

---

## ★6 — The crossover depth

With radius $100\ \mathrm{m}$, $\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$,
$\kappa = 0.02$, $B_0 = 52\ \mathrm{\mu T}$, noise $0.03$ mGal and $0.3$ nT:

$$\Delta g(z) = 0.20968\left(\frac{200}{z}\right)^{2}\ \mathrm{mGal},
\qquad \Delta B(z) = 86.667\left(\frac{200}{z}\right)^{3}\ \mathrm{nT}.$$

$$d'_g(z) = 6.9893\left(\frac{200}{z}\right)^{2}, \qquad
d'_m(z) = 288.89\left(\frac{200}{z}\right)^{3}.$$

Setting $d'_g = d'_m$:

$$6.9893 = 288.89\left(\frac{200}{z}\right)
\;\Longrightarrow\; \frac{200}{z} = 0.024194
\;\Longrightarrow\; z = 8267\ \mathrm{m}.$$

**Answer: $z \approx 8270\ \mathrm{m}$.** Such a depth always exists when both
contrasts are non-zero, because $d'_g \propto z^{-2}$ and $d'_m \propto z^{-3}$
while the *noise* terms are constants; a ratio that grows as $z$ must pass
through 1. If either contrast were zero, one of the ratios would be identically
zero and there would be no crossover — one method would simply never work.

---

## ★7 — Optimal frequency depends on the target

Model: index $= (a/z)^{3} e^{-2z/\delta_{\text{host}}}
\frac{\omega\tau}{\sqrt{1+(\omega\tau)^{2}}}$ with
$\tau = \mu_0\sigma a^{2}/\pi^{2}$ and $\delta$ from the $100\ \Omega\,\mathrm{m}$
host.

**Case (i)** $a = 150\ \mathrm{m}$, $\rho = 1\ \Omega\,\mathrm{m}$:
$\sigma = 1\ \mathrm{S\,m^{-1}}$, $\tau = 2.865\ \mathrm{ms}$, corner
$1/(2\pi\tau) = 55.6\ \mathrm{Hz}$.

| $f$ (Hz) | 10 | 30 | 100 | 500 |
|---|---|---|---|---|
| index (×10³) | 15.19 | 30.91 | 33.17 | 8.64 |

Maximum at $\approx 60\ \mathrm{Hz}$.

**Case (ii)** $a = 50\ \mathrm{m}$, $\rho = 1\ \Omega\,\mathrm{m}$:
$\tau = \mu_0\sigma a^{2}/\pi^{2} = 0.3183\ \mathrm{ms}$, corner
$500\ \mathrm{Hz}$.

| $f$ (Hz) | 10 | 30 | 100 | 500 |
|---|---|---|---|---|
| index (×10⁴) | 0.635 | 1.443 | 2.756 | 2.277 |

Maximum at $\approx 210\ \mathrm{Hz}$.

**Both optima** sit at roughly $1$–$1.5\times$ the frequency that makes
$\omega\tau \approx 1$, and the index is an order of magnitude smaller for the
smaller target at the same depth. **The practical difficulty:** the optimum
depends on $\tau \propto \sigma a^{2}$, which is exactly the quantity the survey is
trying to determine. Choosing a single frequency presumes the answer. This is why
broadband (time-domain or multi-frequency) systems are used: they sample the decay
curve instead of committing to one induction number.

---

## ★8 — A stricter threshold costs detection depth

Magnetics on T1 (radius $150\ \mathrm{m}$, $\kappa = 0.001$, $B_0 = 50\
\mathrm{\mu T}$): $\Delta B(z) = 4.1667(300/z)^{3}$ nT and noise $0.2$ nT, so
$d'(z) = 20.833(300/z)^{3}$.

The condition $P_d = 0.5$ means $d' = Q^{-1}(P_{fa})$:

- $P_{fa} = 0.05$: $Q^{-1} = 1.64485$, $(300/z)^{3} = 0.078953$, $z = 699.3\
  \mathrm{m}$.
- $P_{fa} = 0.01$: $Q^{-1} = 2.32635$, $(300/z)^{3} = 0.111645$, $z = 623.0\
  \mathrm{m}$.

**Detection depth falls from 699 m to 623 m — a 11% reduction (76 m) — for a
five-fold reduction in false alarms.** The consequence for a specification:
"depth of detection" is meaningless without both $P_d$ and $P_{fa}$. Tightening
the false-alarm rate to reduce wasted follow-up drilling directly reduces the
depth reach, and a survey tender that quotes only one of the two numbers is not
comparable with another.

---

## ★9 — A targeting strategy (model answer)

**Target model:** sphere, $R$ between $100$ and $150\ \mathrm{m}$, centre at
$z = 450\ \mathrm{m}$, $\Delta\rho = 250\ \mathrm{kg\,m^{-3}}$, $\kappa = 0.03$ SI,
$\rho_t = 5\ \Omega\,\mathrm{m}$ in a $300\ \Omega\,\mathrm{m}$ host,
$B_0 \approx 50\ \mathrm{\mu T}$.

**Predicted anomalies.** Using the lesson's formulas with $R = 125\ \mathrm{m}$:

- gravity: $\frac{4}{3}\pi G(250)(1.953\times10^{6})/450^{2}
  = 6.74\times10^{-7}\ \mathrm{m\,s^{-2}} = 0.067\ \mathrm{mGal}$;
- magnetics: $\kappa B_0 V/(2\pi z^{3}) = 0.03\times50\times10^{-6}\times
  8.181\times10^{6}/(2\pi\times9.1125\times10^{7}) = 2.14\times10^{-8}$ T
  $= 21.4\ \mathrm{nT}$;
- EM: $\delta_{\text{host}}$ at $100\ \mathrm{Hz} = \sqrt{2/(2\pi\!\cdot\!100
  \cdot\!\mu_0/300)} = 872\ \mathrm{m}$, geometric factor
  $(125/450)^{3} = 0.02143$, induction factor from
  $\tau = \mu_0(1/5)(125)^{2}/\pi^{2} = 0.397\ \mathrm{ms}$ gives
  $\omega\tau = 0.249$, so the index $\approx 0.02143\,e^{-1.032}(0.242)
  = 1.85\times10^{-3}$.

**Noise to assume:** airborne magnetics $0.3$ nT (levelling and diurnal residual
dominate over sensor noise), ground gravity $0.02$ mGal after Bouguer and
levelling, airborne EM with a stated noise floor of $0.02$ in the
secondary/primary ratio. These are the SYNTHETIC values used in the lesson's
spirit, and they must be *measured* on a repeat line before being believed.

**Expected $P_d$** at $P_{fa} = 0.05$: gravity $d' = 0.067/0.02 = 3.37 \to
P_d \approx 0.96$;
magnetics $d' = 21.4/0.3 = 71.4 \to P_d \approx 1.00$; EM
$d' = 1.85\times10^{-3}/0.02 = 0.093 \to P_d = 0.06$ (i.e.
no better than the false-alarm rate).

**Strategy.** (1) Airborne magnetics over the whole area first: cheapest, and the
magnetic contrast is the strongest signal. (2) Ground gravity over the magnetic
anomaly only, to test whether the source is dense as well as magnetic — the two
together separate a magnetic-dense body from a magnetic-non-dense one. (3) EM only
with a target-specific frequency computed from the *assumed* $\tau$, or with a
time-domain system, and only over the coincident anomaly. Decision rule: go to
drilling only where the magnetic and gravity anomalies coincide within the
positioning uncertainty.

**Cheapest falsifying measurement:** the magnetic anomaly amplitude. If the
measured amplitude is an order of magnitude below $21\ \mathrm{nT}$, either
$\kappa$ or the volume is wrong, and the target model is dead for the price of one
airborne survey.

---

## ★10 — Where the EM index breaks down

**(a) Target thinner than its skin depth.** The index assumes a single
geometric coupling $(a/z)^{3}$ and a single induction number, i.e. a body with one
well-defined $\tau$. For a thin sheet (thickness $t \ll a$) the relevant scale is
$t$, and the response depends on the conductivity-thickness product $\sigma t$,
not on $\sigma$ and $t$ separately. **Observable that reveals it:** the decay
curve stays exponential-like but its time constant scales with $\sigma t a^{2}$
rather than $\sigma a^{2}$, so two very different sheets fit equally well — the
same $\sigma$–$a$ ambiguity in a re-scaled form.

**(b) Conductive host.** When the host's own response is comparable to the
target's, the measured secondary field is a sum, and the index's
$\exp(-2z/\delta)$ treatment of the host as a pure attenuator is wrong: the host
also *generates* a response that can be larger than the target's. **Observable:**
at a "target-free" part of the survey, the response does not fall to the noise
floor and decays with the same time constant as the target; and the target's
apparent $\tau$ shortens with distance from the transmitter.

**(c) Internally varying conductivity.** A body with a conductive shell around a
resistive core has a sum of exponentials, not one. **Observable:** the decay curve
in log-linear coordinates is not a straight line; a two-exponential fit reduces
the residual by far more than the extra parameter justifies in noise terms, and
the apparent $\tau$ varies with the late-time window chosen.

---

## ★11 — Correlated evidence is not twice the evidence

Prior $P(D) = 0.10$. Each test: sensitivity $P(+|D) = 0.9$, specificity
$P(-|\text{no }D) = 0.9$, hence $P(+|\text{no }D) = 0.1$.

**(a) Independent.** $P(++|D) = 0.81$; $P(++|\text{no }D) = 0.01$.

$$P(D\mid ++) = \frac{0.81 \times 0.10}{0.81 \times 0.10 + 0.01 \times 0.90}
= \frac{0.081}{0.081 + 0.009} = 0.900 .$$

**(b) Perfectly correlated (behaves as one test).**

$$P(D\mid +) = \frac{0.9 \times 0.10}{0.9 \times 0.10 + 0.1 \times 0.90}
= \frac{0.09}{0.09+0.09} = 0.500 .$$

**The $\rho = 0.8$ case lies strictly between 0.500 and 0.900.** Correlation alone
does not determine it: the joint distribution $P(++,D)$ is fixed only by all four
joint probabilities $P(r_1,r_2|D)$ and $P(r_1,r_2|\text{no }D)$, and a single
correlation coefficient is consistent with a whole family of them (for instance
two tests that repeat the same measurement, versus one good test plus one noisy
copy, both have high $\rho$ but different joints). **Consequence:** the marginal
value of the second method must be assessed with a joint noise model — a shared
forward model, shared cultural noise, shared geology — not with a correlation
coefficient. Pretending independence when two methods see the same property is
the single commonest way multi-method value is overstated, and it is why
[11-02-07](../../02-mineral-exploration/07-multi-method-targeting.md) insists on
naming *which* property each layer measures.
