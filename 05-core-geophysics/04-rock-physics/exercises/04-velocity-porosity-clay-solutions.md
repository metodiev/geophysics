# Solutions — 05-04-04 Velocity–Porosity–Clay Models

> Numbers marked *verified* were computed.

---

## ★1

Wyllie: $1/V_p = \phi/V_\text{fl} + (1-\phi)/V_\text{ma}$ — terms s/m, so the
reciprocal is m/s. ✓
Raymer: $V_p = (1-\phi)^2V_\text{ma} + \phi V_\text{fl}$ — both terms m/s. ✓

---

## ★2

$t = t_\text{ma}+t_\text{fl}$ with path lengths $(1-\phi)L$ and $\phi L$ in
series. Assumption: series (layered) path geometry, so the wave traverses matrix
and fluid sequentially. Real rocks do not satisfy this, especially for the fluid,
which is confined.

---

## ★3

(1) It is a third phase with its own moduli, occupying pore space and reducing
effective porosity. (2) It is compliant, lowering the frame modulus beyond its
volume fraction alone. (3) It conducts and holds bound water, changing the
effective fluid and the electrical response.

---

## ★★4 *(verified)*

$\phi = 0.10$: Wyllie $1/V = 0.10/1500 + 0.90/4500 = 6.6667\times10^{-5}+
2.0\times10^{-4} = 2.6667\times10^{-4}$, $V = 3750.0$ m/s.
Raymer: $0.81(4500)+0.10(1500) = 3645+150 = 3795.0$ m/s. Difference $-1.2\%$
(Wyllie lower).
$\phi = 0.35$: Wyllie $1/V = 2.3333\times10^{-4}+0.65/4500 = 2.3333\times10^{-4}
+1.4444\times10^{-4} = 3.7778\times10^{-4}$, $V = 2647.1$ m/s.
Raymer: $0.4225(4500)+0.35(1500) = 1901.25+525 = 2426.25$ m/s. Difference
$+8.3\%$ (Wyllie higher). Divergence is largest at high porosity.

---

## ★★5 *(verified)*

$V_\text{ma}=4500$: $1/V = 1.3333\times10^{-4}+1.7778\times10^{-4}
= 3.1111\times10^{-4}$, $V = 3214.3$ m/s.
$V_\text{ma}=4300$: $1/V = 1.3333\times10^{-4}+0.8/4300 = 1.3333\times10^{-4}
+1.8605\times10^{-4} = 3.1938\times10^{-4}$, $V = 3131.1$ m/s.
Change $= -83.2$ m/s ($-2.6\%$). The Wyllie–Raymer difference at
$\phi = 0.20$ is $3214.3-3180.0 = 34.3$ m/s ($1.1\%$). **The input-modulus
uncertainty is 2.4 times the model-choice difference** — picking between the two
relations matters less than knowing the matrix velocity.

---

## ★★6 *(verified)*

Wyllie at $\phi = 0.30$: $1/V = 2.0\times10^{-4}+0.7/4500
= 2.0\times10^{-4}+1.5556\times10^{-4} = 3.5556\times10^{-4}$,
$V = 2812.5$ m/s. Misfit $= (2600-2812.5)/2812.5 = -7.56\%$.
Raymer: $0.49(4500)+0.30(1500) = 2205+450 = 2655$ m/s. Misfit
$= (2600-2655)/2655 = -2.07\%$.
Both are negative (the rock is slower than predicted). The likely cause is clay
or a compliant mineral assemblage lowering the frame modulus, since a fluid
effect alone would act through $V_\text{fl}$, which is already set to 1500 m/s.

---

## ★★7

Because the relation is a *model* with fitted exponents and an assumed
lithology, and it is many-to-one: a given velocity is consistent with a range of
porosities depending on the clay content, the mineralogy and the saturation.
Inverting it yields a porosity *conditional on* the model and its inputs, with
an uncertainty at least as large as the residual scatter of the original fit.
Reporting it as a measurement overstates what is known.

---

## ★★★8

A three-phase model replaces the single $V_\text{ma}$ with
$V_\text{ma}^\text{eff}$ from a weighted average of quartz and clay moduli
(using an appropriate averaging scheme — Voigt, Reuss or HS, each an assumption),
and reduces effective porosity by the clay-bound water volume.

Expected: the two-phase models overpredict velocity increasingly with clay
content, exceeding 5% for typical shaly sands at moderate clay volume fractions
of order 10–20%. The calibration required is a set of core measurements of $V_p$
with independent porosity, clay content and saturation, from which the effective
moduli are fitted; the model is then only defensible within that dataset's range.

---

## ★★★9

Wyllie with $\phi = 0.15$: $1/V = 1.0\times10^{-4}+0.85/4500
= 1.0\times10^{-4}+1.8889\times10^{-4} = 2.8889\times10^{-4}$,
$V = 3461.5$ m/s.

Perturbations: $\delta V_\text{ma} = \pm4\% = \pm180$ m/s changes
$0.85/4500$ to $0.85/4680 = 1.8162\times10^{-4}$ or $0.85/4320
= 1.9676\times10^{-4}$, giving $V = 3552.6$ or 3375.5 m/s, i.e. $\pm2.6\%$.
$\delta V_\text{fl} = \pm3\%$ changes $0.15/1500 = 1.0\times10^{-4}$ by
$\pm3\%$, i.e. $\pm0.3\%$ of the $V_p$ slowness — about $\pm0.1\%$ in $V_p$.
$\delta\phi = \pm0.02$ changes $V$ by roughly $\pm1.2\%$.

Dominant term: $V_\text{ma}$ (±2.6%), then $\phi$ (±1.2%), then
$V_\text{fl}$ (±0.1%). At $\phi = 0.30$ the ordering is similar in structure but
$V_\text{fl}$ gains weight.

Conclusion: a 3% velocity anomaly is **borderline** at $\phi = 0.15$ — larger
than each single uncertainty but comparable to the combined uncertainty — so it
cannot be interpreted as a real anomaly without first reducing the
$V_\text{ma}$ uncertainty. At $\phi = 0.30$ the combined uncertainty is smaller
relative to the anomaly, but only if the matrix mineralogy is known.
