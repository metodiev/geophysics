# Solutions — 09-05-04 EM for Geothermal Systems and Permafrost

> **Read after attempting.** Lesson:
> [04 EM for Geothermal Systems and Permafrost](../04-em-geothermal-permafrost.md).

---

## ★1 — Conductivity at $60$ °C

$T = 333.15$ K. $\frac{1}{298.15} - \frac{1}{333.15} = 3.3540\times10^{-3} -
3.0017\times10^{-3} = 3.523\times10^{-4}$ K⁻¹. $E_a/R = 2.0\times10^{4}/8.314463
= 2405.4$ K. Exponent: $2405.4\times3.523\times10^{-4} = 0.8474$. So

$$\sigma = 0.03\,e^{0.8474} = 0.03\times2.333 = 0.0700\ \mathrm{S/m},
\qquad \rho = 14.3\ \Omega\,\mathrm{m}.$$

---

## ★2 — Largest response for a $5$ m layer

From the table the $5$ m row reads $0.8790$ ($10$ Hz), $0.8734$ ($100$ Hz),
$0.8637$ ($1000$ Hz) and $0.8504$ ($10$ kHz): the largest *change* is at the
highest frequency, $10$ kHz, where the layer is a $14.96\%$ reduction in $|H_s|$.
The response change grows with frequency for a thin layer because a thin resistor
must be sampled by a short diffusion length.

---

## ★3 — Two mechanisms, one channel

Both heating and thawing change the *same* quantity, the pore-fluid (or ice)
contribution to conductivity, so a single conductivity measurement cannot say
which happened; separating them requires temperature, hydrological or seasonal
information that the EM measurement does not contain.

---

## ★4 — Relative sensitivity

$$\ln\sigma = \ln\sigma_{25} + \frac{E_a}{R}
\left(\frac{1}{298.15} - \frac{1}{T}\right)
\;\Longrightarrow\;
\frac{\mathrm{d}\ln\sigma}{\mathrm{d}T} = \frac{E_a}{R\,T^{2}},$$

since $\mathrm{d}(-1/T)/\mathrm{d}T = 1/T^{2}$. With $E_a/R = 1804.1$ K:

- at $50$ °C ($323.15$ K): $1804.1/1.0443\times10^{5} = 1.728\times10^{-2}$ K⁻¹,
  i.e. about $1.7\%$ per kelvin;
- at $250$ °C ($523.15$ K): $1804.1/2.7369\times10^{5} = 6.592\times10^{-3}$ K⁻¹,
  i.e. about $0.66\%$ per kelvin.

The relative sensitivity falls as $T^{-2}$, so the same temperature change is
harder to detect in a hot rock — the opposite of the naive expectation and a
direct consequence of the Arrhenius form.

---

## ★5 — Thinnest detectable layer

The $2$ m entry at $100$ Hz is $0.9708$, a $2.92\%$ change; the threshold is $1\%$,
so the detection limit is below $2$ m. Extrapolating linearly towards zero
thickness (the response change is nearly proportional to thickness for thin
layers), $1\%$ is reached at
$t \approx 2.0 \times 1.0/2.92 = 0.68$ m.

That is the **detection** limit. The **resolution** limit — how well the
thickness can be determined — is set by the noise level and the curvature of the
response with thickness: from the table, $20$ m gives $0.4202$ and $40$ m gives
$0.2201$ at $100$ Hz, so a $20\%$ response uncertainty corresponds to a thickness
uncertainty of order $5$ m in that range. Detection and resolution differ by
about a factor of seven here.

---

## ★6 — The cap saturation

At $100$ Hz the ratios are $47.59$ ($10$ m), $118.74$ ($50$ m), $126.31$
($100$ m) and $126.10$ ($200$ m). From $100$ m to $200$ m the response *changes by
$-0.17\%$*, i.e. the two are indistinguishable at any realistic noise level: once
the cap is thicker than about three diffusion depths, the induced currents are
already excluded from the layer and everything below it, so the response is
saturated. An inversion that reports a cap thickness in that regime is reporting
a lower bound, not a measurement, and the honest output is "cap thickness greater
than about $100$ m".

---

## ★7 — A monitored $2\%$ change at $100$ °C

A $2\%$ change in $|H_s|$ corresponds to a $1\%$ change in conductivity in the
linear regime. At $100$ °C the relative sensitivity is $1.2957\times10^{-2}$ K⁻¹
(printed), so

$$\Delta T = \frac{0.01}{0.012957} = 0.77\ \mathrm{K}.$$

With $E_a$ uncertain by a factor two, the sensitivity scales with $E_a$ (it is
linear in it), so $\Delta T$ ranges over $0.39$–$1.55$ K. **The model uncertainty
dominates the measurement by a factor of four**, which is why a monitoring
programme pairs EM with temperature observation where any is available.

---

## ★8 — A $1$ K monitoring design (specification)

**Band.** From the lesson's tables, sensitivity to a warm shallow section is
best at frequencies whose diffusion depth matches the section of interest; for a
$0.05$ S/m section and a target at tens of metres, $100$–$1000$ Hz is the useful
band, and the demonstration's frozen-layer table shows the response change growing
with frequency for a thin feature.

**Repeat interval.** A $1$ K change at $20$ °C corresponds to a $2.0\%$
conductivity change (from $E_a/RT^{2} = 0.0210$ K⁻¹ at $20$ °C), i.e. a $4.0\%$
response change in the quadratic? No — in the linear regime a $2\%$ conductivity
change gives a $2\%$ response change. With a $1\%$ noise level that is a
$2\sigma$ detection, so a repeatability of $1\%$ is the design target; two to
three repeats per station per epoch are needed to reach it.

**Statistic.** The mean response difference between epochs, tested by a paired
$t$-test against the repeat scatter, with the same survey geometry and the same
coil heights in both epochs. A single-epoch difference with an unstated geometry
change is not evidence.

**Assumption accepted.** The Arrhenius model with $E_a = 15$ kJ/mol and a
temperature-independent $\sigma_{25}$. If the change is due to soil-moisture or
salinity change instead, the same response would be produced with no temperature
change at all — which is the reason the design includes a hydrological record.
