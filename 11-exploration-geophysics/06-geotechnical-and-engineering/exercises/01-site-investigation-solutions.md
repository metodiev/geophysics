# Solutions — 11-06-01 Site Investigation: Objectives and Method Selection

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson: [01 Site Investigation](../01-site-investigation.md).

---

## ★1 — Velocity to stiffness

$$ G_{\max} = \rho v_s^{2} = 1800 \times 250^{2}
= 1.125\times10^{8}\ \mathrm{Pa} = 112.5\ \mathrm{MPa}, $$
$$ E = 2G(1+\nu) = 2(112.5)(1.30) = 292.5\ \mathrm{MPa}. $$

Units: $[\rho v_s^{2}] = \mathrm{kg\,m^{-3}}\cdot\mathrm{m^{2}\,s^{-2}}
= \mathrm{kg\,m^{-1}\,s^{-2}} = \mathrm{Pa}$. ✔

---

## ★2 — vs30

$$ t = \frac{5}{200} + \frac{25}{500} = 0.025 + 0.050 = 0.075\ \mathrm{s}, $$
$$ v_{s30} = \frac{30}{0.075} = 400.0\ \mathrm{m\,s^{-1}}. $$

The slow 5 m layer contributes one third of the travel time: the harmonic
average is dominated by the slow material, which is the point of defining it by
time rather than by thickness.

---

## ★3 — Void anomaly

$$ g_z(0) = \frac{4}{3}\pi G \Delta\rho \frac{R^{3}}{z^{2}}
= \frac{4}{3}\pi(6.6743\times10^{-11})(2600)\frac{1.5^{3}}{6^{2}}, $$

$$ = 2.7962\times10^{-10} \times 2600 \times \frac{3.375}{36}
= 2.7962\times10^{-10} \times 243.75 = 6.815\times10^{-8}\ \mathrm{m\,s^{-2}}
= 6.81\ \mu\mathrm{Gal}. $$

---

## ★4 — Settlement and its velocity sensitivity

$$ G_{\max} = 1800(400)^{2} = 2.88\times10^{8}\ \mathrm{Pa}, \qquad
E_{\max} = 2(288)(1.3) = 748.8\ \mathrm{MPa}, $$
$$ E_{\text{op}} = 0.35(748.8) = 262.1\ \mathrm{MPa}. $$

$$ s = \frac{2qR(1-\nu^{2})}{E_{\text{op}}}
= \frac{2(150\times10^{3})(2.0)(0.91)}{262.1\times10^{6}}
= \frac{5.46\times10^{5}}{2.621\times10^{8}} = 2.08\times10^{-3}\ \mathrm{m}
= 2.1\ \mathrm{mm}. $$

With $v_s$ $15\%$ lower everywhere, $E$ falls as $v_s^{2}$, i.e. by a factor
$0.85^{2} = 0.7225$, and the settlement rises by $1/0.7225 = 1.384$:

$$ s = 2.08 \times 1.384 = 2.88\ \mathrm{mm} \quad (+38.4\%). $$

A $15\%$ velocity error is a $38\%$ settlement error: the inverse-square
dependence propagates every velocity uncertainty as twice its relative size.

---

## ★5 — Radius required at 12 m

$$ g_z(0) = \frac{4}{3}\pi G \rho \frac{R^{3}}{z^{2}} = 5\times10^{-8}\
\mathrm{m\,s^{-2}} $$

$$ R^{3} = \frac{5\times10^{-8} z^{2}}{\frac{4}{3}\pi G \rho}
= \frac{5\times10^{-8}(144)}{2.7962\times10^{-10}(2500)}
= \frac{7.2\times10^{-6}}{6.9905\times10^{-7}} = 10.30\ \mathrm{m^{3}}, $$

$$ R = 2.18\ \mathrm{m}. $$

**Assumption.** The sphere is compact, its density contrast is the full rock
density (an empty void), and the anomaly is measured on the profile peak with the
regional field removed. A flat cavity of the same volume would produce a
comparable or larger anomaly; an elongated one a smaller peak.

---

## ★6 — Value of information

$$ \mathrm{P(\text{anomaly})} = p\,\mathrm{TPR} + (1-p)\mathrm{FPR}
= 0.20(0.90) + 0.80(0.25) = 0.18 + 0.20 = 0.38, $$
$$ \mathrm{P(\text{void and no anomaly})} = p(1-\mathrm{TPR}) = 0.02. $$

$$ \mathbb{E}[\text{no survey}] = p\,H = 0.20(40c) = 8.0c, $$
$$ \mathbb{E}[\text{survey}] = c + 0.38(8c) + 0.02(40c)
= c + 3.04c + 0.80c = 4.84c. $$

$$ \text{VOI} = 8.0c - 4.84c = +3.16c \quad (\text{survey}). $$

The survey pays: it removes $3.16$ survey-costs of expected loss. Note the
arithmetic also shows what would flip the decision — a lower prior, a cheaper
protective measure, or a survey with a worse $\mathrm{FPR}$.

---

## ★7 — Method suite for a karstic hospital site (specification)

**(i) Cavity detection to 15 m.** Microgravity, with a station spacing of a few
metres and a $5\ \mu\mathrm{Gal}$ target. From the lesson, a $2\ \mathrm{m}$
void is detectable to $10.6\ \mathrm{m}$ and a $3\ \mathrm{m}$ void to
$19.4\ \mathrm{m}$ in $2500\ \mathrm{kg\,m^{-3}}$ rock, so the survey can reach
15 m for voids of $\ge 2.5\ \mathrm{m}$ radius. Complement with GPR for the
shallow, electrically resistive part and ERT for clay-filled cavities, which
microgravity sees only weakly (a clay-filled void has a small density contrast).
**Failure mode:** an undetected regional gradient, or a cavity filled with
water-saturated sediment (near-zero density contrast).

**(ii) Bedrock depth.** Seismic refraction, using the $v_p$ contrast between
weathered cover and limestone, with the crossover-distance relation. Expect
$\pm10$-$15\%$ depth uncertainty where the velocity contrast is below 2 (the
lesson-05-03 sensitivity table). **Failure mode:** a velocity inversion (a slow
weathered zone beneath a faster layer), which refraction cannot see.

**(iii) Stiffness profile.** MASW, with a spread long enough to sample the
$\lambda/3$ depths of interest. For a settlement calculation the profile's
uncertainty must be propagated, because the settlement goes as $v_s^{-2}$.
**Failure mode:** a high-impedance surface layer (a road, a foundation) that
traps high-frequency energy and truncates the dispersion curve.

---

## ★8 — Choosing a threshold, and overstating the VOI

Moving the detection threshold trades $\mathrm{TPR}$ against $\mathrm{FPR}$: a
low threshold detects more (higher $\mathrm{TPR}$) and flags more
non-hazards (higher $\mathrm{FPR}$); a high threshold does the reverse. The set
of achievable $(\mathrm{FPR}, \mathrm{TPR})$ pairs is the **ROC curve**, and a
decision-maker should choose the point that minimises the expected cost of
Section 3.5, i.e. that maximises

$$ \mathrm{VOI}(\theta) = pH - \left[c + P\,p_{\text{anom}}(\theta)
+ H\,p(1-\mathrm{TPR}(\theta))\right], $$

where $\theta$ is the threshold. Because the survey cost $c$ and the
protective-measure cost $P$ enter, the optimal threshold is **not** the one that
maximises detection: it depends on the consequences.

**How the VOI can be overstated accidentally.**

1. **Choosing the threshold after seeing which anomalies correspond to known
   hazards.** That tunes $\mathrm{TPR}$ and $\mathrm{FPR}$ on the same data used
   to compute the VOI, so both are optimistic.
2. **Treating $\mathrm{FPR}$ as if false alarms were free.** Each false alarm may
   trigger a protective measure $P$; if $P$ is omitted from the model, the survey
   looks better than it is.
3. **Forgetting that $\mathrm{TPR}$ applies to the detectable population.** A
   detection model calibrated on large, shallow targets overstates $\mathrm{TPR}$
   for small, deep ones, and the miss term $H\,p(1-\mathrm{TPR})$ is the term
   that grows.

---

## Worked mastery checkpoint

**(a) Stiffness and settlement.** The profile is $220\ \mathrm{m\,s^{-1}}$ to
$6\ \mathrm{m}$ over $480\ \mathrm{m\,s^{-1}}$, with
$\rho = 1900\ \mathrm{kg\,m^{-3}}$. Using the travel-time average as the
representative velocity over 30 m:

$$ v_{s30} = \frac{30\ \mathrm{m}}{\dfrac{6}{220}+\dfrac{24}{480}}
= \frac{30}{0.027273+0.050} = 388.2\ \mathrm{m\,s^{-1}}, $$

$$ G_{\max} = 1900(388.2)^{2} = 2.864\times10^{8}\ \mathrm{Pa}
= 286.4\ \mathrm{MPa}, $$
$$ E_{\max} = 2(286.4)(1.30) = 744.6\ \mathrm{MPa}. $$

With a stated operational reduction factor of $0.30$,
$E_{\text{op}} = 223.4\ \mathrm{MPa}$, and for $q = 150\ \mathrm{kPa}$,
$R = 2.0\ \mathrm{m}$, $\nu = 0.30$:

$$ s = \frac{2(150\times10^{3})(2.0)(0.91)}{223.4\times10^{6}} = 2.44\
\mathrm{mm}. $$

**(b) $v_{s30} = 388.2\ \mathrm{m\,s^{-1}}$** (the same calculation).

**(c) Void anomaly.** $R = 1.5\ \mathrm{m}$ at $z = 8\ \mathrm{m}$ in
$2500\ \mathrm{kg\,m^{-3}}$ rock:

$$ g_z(0) = \frac{4}{3}\pi G(2500)\frac{1.5^{3}}{8^{2}}
= \frac{2.7962\times10^{-10}(2500)(3.375)}{64}
= 3.69\times10^{-8}\ \mathrm{m\,s^{-2}} = 3.69\ \mu\mathrm{Gal}. $$

This is **below** a $5\ \mu\mathrm{Gal}$ noise floor: the survey would not see
this void at that depth and noise level. Solving
$g_z(0) = 5\ \mu\mathrm{Gal}$ for the depth gives the limit for this radius:

$$ z = \sqrt{\frac{2.3593\times10^{-6}}{5\times10^{-8}}} = 6.87\ \mathrm{m}, $$

so the void would be detectable only if it were shallower than about 6.9 m.

**(d) Value of information** with $p = 0.05$, survey cost $c$, protective measure
$8c$, hit cost $20c$, $\mathrm{TPR} = 0.85$, $\mathrm{FPR} = 0.20$:

$$ \mathbb{E}[\text{no survey}] = 0.05(20c) = 1.00c, $$
$$ P(\text{anomaly}) = 0.05(0.85) + 0.95(0.20) = 0.2325, \qquad
\text{miss} = 0.05(0.15) = 0.0075, $$
$$ \mathbb{E}[\text{survey}] = c + 8c(0.2325) + 20c(0.0075)
= c + 1.86c + 0.15c = 3.01c, $$
$$ \mathrm{VOI} = 1.00c - 3.01c = -2.01c. $$

**Do not survey.** At a 5% prior the protective measure costs more than the risk
it mitigates. Note also that if the survey is skipped, the residual risk
$p\,H = 1.0c$ remains and must be accepted consciously.
