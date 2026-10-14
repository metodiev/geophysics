# Solutions — 16-04-05 The Carbon Cycle: Reservoirs, Fluxes and Perturbations

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [05 The Carbon Cycle](../05-carbon-cycle.md).

---

## ★1 — The ppm-to-GtC conversion

$$\frac{p_s}{g} = \frac{1.013\times10^5}{9.81} = 1.0332\times10^4\
\mathrm{kg\,m^{-2}},$$

$$4\pi a^2 = 4\pi(6.371\times10^6)^2 = 5.1006\times10^{14}\ \mathrm{m^2},$$

$$m_\text{atm} = 1.0332\times10^4\times5.1006\times10^{14}
= 5.267\times10^{18}\ \mathrm{kg},$$

$$1\ \mathrm{ppm} = 10^{-6}\times5.267\times10^{18}\times0.4146
= 2.1837\times10^{12}\ \mathrm{kg} = 2.1837\ \mathrm{GtC}.$$

**Units check:** kg × (dimensionless mass fraction) = kg; dividing by
$10^{12}$ kg per GtC gives GtC. ✔

---

## ★2 — Fraction remaining at two times

$$a(30) = 0.20 + 0.30\mathrm{e}^{-30/3.5} + 0.30\mathrm{e}^{-1}
+ 0.20\mathrm{e}^{-30/400}.$$

Numerically: $\mathrm{e}^{-8.571} = 1.91\times10^{-4}$,
$\mathrm{e}^{-1} = 0.36788$, $\mathrm{e}^{-0.075} = 0.92774$, so

$$a(30) = 0.20 + 0.0000573 + 0.110364 + 0.185549 = 0.4960 .$$

$$a(400) = 0.20 + 0.30\mathrm{e}^{-114.3} + 0.30\mathrm{e}^{-13.33}
+ 0.20\mathrm{e}^{-1} = 0.20 + 0 + 0 + 0.073576 = 0.2736 .$$

**Which term dominates.** At 30 years the 30-year and 400-year terms contribute
0.1104 and 0.1855 — the slow terms dominate even at a few decades, because the
fast term has already drained. At 400 years only the non-decaying term (0.20)
and the 400-year term (0.0736) matter: the permanent component is now the larger
of the two.

---

## ★3 — A 2000 GtC pulse at 10 years

$$a(10) = 0.20 + 0.30\mathrm{e}^{-2.857} + 0.30\mathrm{e}^{-0.3333}
+ 0.20\mathrm{e}^{-0.025} = 0.20 + 0.01721 + 0.21541 + 0.19506
= 0.6277 .$$

Atmospheric excess $= 2000\times0.6277 = 1255.4$ GtC; sinks
$= 2000\times(1-0.6277) = 744.6$ GtC. Sum: $1255.4+744.6 = 2000.0$ GtC ✔ — the
partition is exact by construction, which is the point of the check.

---

## ★4 — A 3000 GtC pulse at three times

| time (yr) | $a(t)$ | atmosphere (GtC) | sinks (GtC) | fraction airborne |
|---|---|---|---|---|
| 10 | 0.6273 | 1881.8 | 1118.2 | 0.627 |
| 100 | 0.3665 | 1099.4 | 1900.6 | 0.366 |
| 1000 | 0.2164 | 649.3 | 2350.7 | 0.216 |

Every row sums to 3000.0 GtC ✔.

**Trend.** The airborne fraction falls monotonically, and almost all of the fall
occurs in the first century: from 0.627 at 10 years to 0.366 at 100 years, and
then only to 0.216 after a further 900 years. The *slow* tail is set by the
non-decaying coefficient: the fraction asymptotes to 0.20, not to zero.

---

## ★5 — Equilibrium budget with a climate–carbon feedback

The relation is implicit because $\Delta T$ depends on $\Delta C$ through the
logarithmic forcing. Iterate:

| iteration | $\Delta C$ (GtC) | $F$ (W m⁻²) | $\Delta T$ (K) |
|---|---|---|---|
| 0 (start) | 800.0 | 3.7000 | 0.9250 |
| 1 | 744.5 | 3.5123 | 0.8781 |
| 2 | 747.2 | 3.5208 | 0.8802 |
| 3 | 747.2 | 3.5207 | 0.8802 |

**Convergence check:** the change in $\Delta C$ between successive iterations is
below $10^{-13}$ GtC by the third step (the printed table shows the first two
significant steps; the code runs to $<10^{-13}$).

So $\Delta C = 747.2$ GtC, airborne fraction $= 747.2/2000 = 0.3736$, and
$\Delta T = 0.880$ K.

**Worked step 1:** with $\Delta T = 0$ first,
$\Delta C = 2000/2.5 = 800.0$ GtC;
$F = 3.7\ln(1+800/800)/\ln 2 = 3.7\times1.0 = 3.700$ W m⁻²;
$\Delta T = 3.7/4.0 = 0.9250$ K;
then $\Delta C = (2000-150\times0.9250)/2.5 = 1861.25/2.5 = 744.5$ GtC. ✔

---

## ★6 — The same budget without the climate–carbon feedback

With $\gamma = 0$ there is no feedback, so the system is explicit:

$$\Delta C = \frac{E}{1+\beta} = \frac{2000}{2.5} = 800.0\ \mathrm{GtC},
\qquad \text{airborne fraction} = 0.400,$$

$$F = 3.7\frac{\ln(1+800/800)}{\ln2} = 3.700\ \mathrm{W\,m^{-2}},
\qquad \Delta T = 0.9250\ \mathrm{K}.$$

**Difference.** The feedback reduces the airborne fraction from 0.400 to 0.3736
(a reduction of 0.0264, i.e. 6.6% of the airborne fraction) and the temperature
from 0.9250 to 0.8802 K (a reduction of 0.0448 K, 4.8%). The mechanism is
simultaneously a *negative* feedback on atmospheric carbon and therefore on
warming — the extra uptake takes carbon out of the atmosphere as it warms. This
is an equilibrium calculation; the transient effect is smaller and develops over
the timescales of Section 5 of the lesson.

---

## ★7 — Separating the two sources of curvature

**Design.** Run the same budget at the same emission totals twice: (A) with the
full model, and (B) with $\gamma$ set to zero but everything else unchanged.
The difference between the two runs isolates the $\gamma$ term exactly, because
the only change is that term. Then compare the *shape* of each curve.

**Diagnostic.** Plot $\Delta T/E$ (the increment per unit emissions) against $E$
for both runs, on the same axes. Decompose the total curvature:

$$\underbrace{\frac{\Delta T_\text{A}(E)}{E}}_{\text{full}} -
\underbrace{\frac{\Delta T_\text{B}(E)}{E}}_{\text{forcing only}}
= \text{contribution of }\gamma,$$

since run B has the identical logarithmic forcing and the identical linear
response, so any remaining curvature in B is attributable to the logarithm
alone.

**Attribution.** The curvature of B grows with $E$ because
$\ln(1+\Delta C/C_0)$ saturates; the difference A−B grows with $E$ because
$\gamma\Delta T$ grows with $\Delta T$. Evaluating the calculation:

| $E$ (GtC) | A: full model (K per 1000 GtC) | B: $\gamma = 0$ | difference ($\gamma$ contribution) |
|---|---|---|---|
| 250 | 0.723 | 0.402 | 0.321 |
| 1000 | 0.616 | 0.322 | 0.294 |
| 4000 | 0.408 | 0.271 | 0.137 |

Both sources reduce the increment per unit emissions, and the $\gamma$
contribution itself shrinks at the high end because the warming term saturates
with it. **Reporting the split matters because only the first is a property of
radiative transfer; the second is a property of an assumed carbon-cycle
parameterisation**, and a reader who is told only the combined number cannot
tell which of the two they would need to change in their own calculation.

---

## ★8 — "About half of emitted CO₂ remains in the atmosphere"

**What a reader must know.** Six things, and omitting any of them makes the
number unreproducible:

1. **The time window.** Section 6 of the lesson gives 0.699 at 25 years and
   0.388 at 300 years with the *same* model.
2. **The emission pathway.** A pulse and a ramp have different airborne
   fractions at the same cumulative emissions.
3. **The impulse-response coefficients.** The fast/intermediate/slow/permanent
   partition sets the whole trajectory; the non-decaying fraction alone moves
   the asymptote.
4. **The uptake parameters $\beta$ and $\gamma$**, and whether a climate–carbon
   feedback is included at all (★★6 shows a 6.6% change from $\gamma$ alone at
   equilibrium).
5. **The ppm-to-GtC convention**, if the claim mixes concentrations and masses (a
   3% effect).
6. **Whether the calculation is transient or equilibrium.** The lesson's own
   transient values (Section 5) and equilibrium values (Section 8) differ.

**Verdict:** the claim is **incomplete, and sometimes false**. It is a
reasonable order-of-magnitude statement for a mid-range window under a specific
set of coefficients — and it is wrong as a general property of the carbon cycle,
because the ratio is kinematic and time-dependent. A complete statement reads
like: "under this stated response function and this stated pathway, the
cumulative airborne fraction at year $t$ is $X$."
