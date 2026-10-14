# Solutions — 05-08-07 Log Interpretation, Petrophysics and Uncertainty

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — The five stages and one constant each

| Stage | Constant |
|---|---|
| Data preparation | The environmental-correction set and its version |
| Shale volume | The gamma-ray baselines and the index relation (e.g. 0.33 and the exponent 2) |
| Porosity | Matrix density and fluid density (2650 and 1000 kg m⁻³ here) |
| Saturation | $a$, $m$, $n$ (1, 2, 2 here) and $R_w$ (0.12 Ω m at 65 °C here) |
| Summation | Net-to-gross cut-offs (a $V_{\\mathrm{sh}}$ or porosity threshold) |

---

## ★2 — MD to TVD

$$\\mathrm{TVD} = \\mathrm{MD}\\cos(\\text{inclination}) = 2500\\cos 25°
= 2500(0.9063) = 2266\\ \\mathrm{m}.$$

The 234 m difference is 9 per cent — larger than most of the uncertainties
discussed in this lesson, and entirely a depth-scale error.

---

## ★3 — Cement bond versus flow

A **cement bond log** measures the acoustic response of the casing–cement–formation
system, and establishes whether cement is bonded over an interval — with the
caveat that a micro-annulus, a fast formation or gas-cut cement can mimic a bad
bond. A **flow log** measures movement (spinner, temperature, pressure, density,
capacitance) and establishes which intervals flow and roughly how much. The first is
about isolation, the second about production; neither is about rock properties.

---

## ★4 — The demonstration's saturation

**(a)** Point estimate $S_w = 0.477$; 90 per cent interval $[0.307, 0.721]$;
hydrocarbon saturation $0.279$–$0.693$.

**(b)** With $m = 1.8$: $\\phi_{\\text{eff}}^m = 0.171^{1.8} = 0.0404$ (against
$0.171^2 = 0.0292$), so $S_w = (0.15/(0.0404\\times18))^{1/2} =
(0.2063)^{1/2} = 0.454$. (Using $R_w = 0.12$ and $m = 2$ gives
$(0.12/0.526)^{1/2} = 0.478$; both changes together give about 0.427 with
$R_w = 0.15$ and $m = 1.8$.)

**(c)** The $m$ change moves $S_w$ by about $-5$ to $-11$ per cent depending on
$R_w$, while the $R_w$ change alone moves it by about $+12$ per cent. Both matter,
and the ranking in the demonstration is set by the *perturbation widths* assumed
(10 per cent on $m$, 20 per cent on $R_w$), not by the sensitivities alone — which
is exactly why the assumed widths must be reported.

---

## ★5 — Depth-matching residuals

| Bed (m) | Fractional error at 0.35 m misfit |
|---|---|
| 0.5 | 70 % |
| 1.0 | 35 % |
| 3.0 | 12 % |
| 10.0 | 3.5 % |

The thinly bedded, thinly net-pay intervals are affected most, which is
unfortunate because they are frequently the most valuable. Depth matching is
therefore a first-order step for thin-bed interpretation and a second-order one for
thick reservoirs.

---

## ★6 — Volumetric uncertainty

Hydrocarbon volume is proportional to the product
$\\text{NTG}\\times\\phi\\times(1-S_w)$, so relative uncertainties add in
quadrature:

$$\\frac{\\delta V}{V} = \\sqrt{\\left(\\frac{0.06}{0.42}\\right)^2
+ \\left(\\frac{0.021}{0.171}\\right)^2 + \\left(\\frac{0.207}{0.523}\\right)^2}
= \\sqrt{0.0204 + 0.0151 + 0.1567} = \\sqrt{0.1922} = 0.438 .$$

**44 per cent**, dominated by the saturation term (which contributes 82 per cent of
the variance). Buying a better porosity log changes the answer by 3 per cent
relative; constraining $m$ and $R_w$ changes it by tens of per cent. This is the
quantitative version of the lesson's conclusion.

---

## ★7 — A synthetic-well workflow test

Method: fix mineralogy, porosity and fluid by layer; derive saturated moduli with
Gassmann; convert to velocity with a stated model; forward-model the logs; then run
the workflow. Report $S_w$ error for three categories of layer:

| Layer type | Expected $S_w$ error | Dominant cause |
|---|---|---|
| All assumptions hold | $\\approx 0$ (percent-level) | Numerical and reading precision |
| Wrong mineralogy (dolomite read as quartz) | Tens of per cent | Porosity wrong by 30–90 per cent, entering through $\\phi^m$ |
| Shaly rock with Archie | Large and one-signed (too high) | Clay conduction adds a parallel conductivity path that Archie does not model |

**Ranking:** the shaly-rock error is usually largest, then the mineralogy error,
then everything else. The result to take away is that both dominant terms are
*model* errors, and neither is reduced by better logs.

---

## ★8 — Halving the saturation uncertainty

The dominant term is $m$ (cementation exponent), contributing about 43 per cent of
the one-at-a-time spread. To halve the interval:

1. **Measure $m$ on core** in the same lithology and at the same confining pressure,
   using a formation-factor ($F$–$\\phi$) measurement. This is the direct route and
   it typically reduces $m$'s uncertainty from 10 per cent to 2–3 per cent.
2. **Measure $R_w$ from a produced-water sample** at reservoir temperature, which
   reduces its contribution to a few per cent.
3. **Constrain mineralogy** from $P_\\mathrm{e}$ plus core, which reduces the
   matrix-density term.

**Cost:** a few core plugs with a formation-factor measurement, one produced-water
sample, and a routine $P_\\mathrm{e}$ analysis — modest compared with a logging
programme, which is the point.

**Residual uncertainty** after all three: the structural question of whether Archie
applies at all, plus the small remaining statistical terms. That residual is not
quantifiable from these logs.

**What would prove the programme unnecessary:** a demonstrative test that the
current $m$ and $R_w$ are correct — for example, a well in the same formation where
core-derived $m$ and core-calibrated saturation agree with the log-derived values
to within the target uncertainty. If such a well exists, cite it and carry its
result; if it does not, the core programme is the cheapest available reduction in
uncertainty.
