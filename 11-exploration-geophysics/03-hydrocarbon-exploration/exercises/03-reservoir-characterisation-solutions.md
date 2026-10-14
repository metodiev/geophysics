# Solutions — 11-03-03 Reservoir Characterisation and Property Prediction

> **Read after attempting the exercises.** Numbers were computed with the
> relations of the lesson, not estimated. Where two answers are defensible it is
> said so.

Lesson: [03 Reservoir Characterisation and Property Prediction](../03-reservoir-characterisation.md).

---

## ★1 — A complete fluid substitution, step by step

$$K_{\text{dry}} = 36.6\left(1-\frac{0.22}{0.40}\right) = 36.6\times0.45
= 16.47\ \mathrm{GPa},$$
$$\mu_{\text{dry}} = 45.0\times0.45 = 20.25\ \mathrm{GPa},$$
$$\rho = 0.78\times2650 + 0.22\times1000 = 2067 + 220
= 2287\ \mathrm{kg\,m^{-3}}.$$

Gassmann:

$$\left(1-\frac{K_{\text{dry}}}{K_m}\right)^{2} = (1-0.45)^{2} = 0.3025,$$
$$\frac{\phi}{K_{\text{fl}}} = \frac{0.22}{2.2} = 0.100000, \qquad
\frac{1-\phi}{K_m} = \frac{0.78}{36.6} = 0.021311, \qquad
\frac{K_{\text{dry}}}{K_m^{2}} = \frac{16.47}{1339.56} = 0.012295,$$
$$\text{denominator} = 0.100000 + 0.021311 - 0.012295 = 0.109016,$$
$$K_{\text{sat}} = 16.47 + \frac{0.3025}{0.109016} = 16.47 + 2.775
= 19.245\ \mathrm{GPa}.$$

Velocities:

$$v_p = \sqrt{\frac{(19.245 + \tfrac43\times20.25)\times10^{9}}{2287}}
= \sqrt{\frac{46.245\times10^{9}}{2287}} = 4496.8\ \mathrm{m\,s^{-1}},$$
$$v_s = \sqrt{\frac{20.25\times10^{9}}{2287}} = 2975.6\ \mathrm{m\,s^{-1}},$$
$$\text{AI} = 2287\times4496.8 = 1.0284\times10^{7}
= 10.28\ \mathrm{MRayl}, \qquad \frac{v_p}{v_s} = 1.511 .$$

(These reproduce the lesson's brine-sand row at $\phi = 0.22$.)

---

## ★2 — Fluid mixing

Wood's equation (harmonic mean of the fluid moduli) and arithmetic density
mixing:

$$\frac{1}{K_{\text{fl}}} = \frac{0.3}{2.2} + \frac{0.7}{0.02}
= 0.136364 + 35.000 = 35.1364
\qquad\Longrightarrow\qquad K_{\text{fl}} = 0.028460\ \mathrm{GPa},$$
$$\rho_{\text{fl}} = 0.3\times1000 + 0.7\times200 = 440\ \mathrm{kg\,m^{-3}} .$$

Wood's equation is a *model* of a fine, uniform mixture: it assumes the two
fluids are mixed at a scale finer than the wavelength and that they share the
same pressure. **Patchy** saturation (gas patches larger than the pore scale)
gives a stiffer effective fluid, and therefore a smaller gas effect.

---

## ★3 — Impedance units

SI: $\mathrm{kg\,m^{-2}\,s^{-1}}$ (equivalently Pa·s/m). MRayl $= 10^{6}$ of it.

$$Z = 9.7\times10^{6}\ \mathrm{kg\,m^{-2}\,s^{-1}} = 9.70\ \mathrm{MRayl}.$$

---

## ★★4 — Gas substitution

$$K_{\text{fl}} = 0.028460\ \mathrm{GPa}, \qquad
\rho_{\text{fl}} = 440\ \mathrm{kg\,m^{-3}},$$
$$\rho = 0.78\times2650 + 0.22\times440 = 2067 + 96.8
= 2163.8\ \mathrm{kg\,m^{-3}},$$
$$\frac{\phi}{K_{\text{fl}}} = \frac{0.22}{0.028460} = 7.7302, \qquad
\text{denominator} = 7.7302 + 0.021311 - 0.012295 = 7.7392,$$
$$K_{\text{sat}} = 16.47 + \frac{0.3025}{7.7392} = 16.47 + 0.0391
= 16.509\ \mathrm{GPa},$$
$$v_p = \sqrt{\frac{(16.509+27.000)\times10^{9}}{2163.8}} = 4484.2\
\mathrm{m\,s^{-1}}, \qquad
v_s = \sqrt{\frac{20.25\times10^{9}}{2163.8}} = 3059.2\ \mathrm{m\,s^{-1}},$$
$$\text{AI} = 2163.8\times4484.2 = 9.703\times10^{6} = 9.70\ \mathrm{MRayl}.$$

Change in impedance: $(9.703-10.284)/10.284 = -5.65\%$.

**Decomposition.** $v_p$ changed from 4496.8 to 4484.2 m/s, i.e. $-0.28\%$;
$\rho$ changed by $-5.39\%$. The impedance change is essentially the density
change:

$$-5.65\% \approx -0.28\% - 5.39\% .$$

Gas is a **density** anomaly in this model, which is why density information
(long offsets) is decisive, and why a $v_p$-only estimate can miss a pay sand
entirely. Note also $v_s$ *rose* by 2.8% — Gassmann leaves the shear modulus
unchanged, so $v_s$ rises only because the density fell, which is the origin of
the $v_p/v_s$ drop.

---

## ★★5 — Joint separation

$$d_1 = \frac{|\Delta \text{AI}|}{\sigma_{\text{AI}}}
= \frac{0.6}{0.5} = 1.20,$$

$$d_2 = \sqrt{\left(\frac{0.6}{0.5}\right)^{2}
+ \left(\frac{0.045}{0.045}\right)^{2}}
= \sqrt{1.44 + 1.00} = 1.56 .$$

The second attribute improves the separation from 1.20 to 1.56 standard
deviations — a real improvement of 30%, and still a weak discriminant: at 1.56σ
the error rates are high and the base rate dominates the posterior (lesson §5).
**Meaning for classification:** no method can make a 1.56σ problem separable;
the honest options are more data (a well), a better prior, or accepting and
quantifying the error rate.

---

## ★★6 — Net-to-gross averaging

Sand properties (from ★4, brine case): $v_p = 4695\ \mathrm{m\,s^{-1}}$ (at
$\phi = 0.20$), $\rho = 2200\ \mathrm{kg\,m^{-3}}$; shale:
$2800\ \mathrm{m\,s^{-1}}$, $2450\ \mathrm{kg\,m^{-3}}$.

$$\rho_{\text{cell}} = 0.6\times2200 + 0.4\times2450 = 1320 + 980
= 2300\ \mathrm{kg\,m^{-3}},$$
$$v_{\text{cell}} = \frac{1}{\dfrac{0.6}{4695} + \dfrac{0.4}{2800}}
= \frac{1}{1.2779\times10^{-4} + 1.4286\times10^{-4}}
= \frac{1}{2.7065\times10^{-4}} = 3694.8\ \mathrm{m\,s^{-1}},$$
$$\text{AI}_{\text{cell}} = 2300\times3694.8 = 8.498\times10^{6}
= 8.50\ \mathrm{MRayl}.$$

**Which average is exact.** The **density** average (arithmetic) is exact: mass
per unit volume is additive. The transit-time average is exact for the
*two-way time through the cell* — travel times add, so $1/v$ averages
volume-fraction-weighted, which is why the harmonic form appears. The *product*
$\rho_{\text{cell}}v_{\text{cell}}$ is only approximately the amplitude-relevant
impedance; the rigorous long-wavelength construction for a layered cell is
Backus averaging, which also produces anisotropy (lesson [11-03-06](../06-borehole-and-integration.md)).

---

## ★★★7 — Posterior and threshold

$$P(\text{pay}\mid x) = \frac{\Lambda p}{\Lambda p + (1-p)}, \qquad \Lambda = 12 .$$

| prior $p$ | $\Lambda p$ | $1-p$ | posterior |
|---|---|---|---|
| 0.50 | 6.00 | 0.50 | 0.923 |
| 0.20 | 2.40 | 0.80 | 0.750 |
| 0.05 | 0.60 | 0.95 | 0.387 |
| 0.02 | 0.24 | 0.98 | 0.197 |

**Threshold.** Call it a prospect if the expected value of drilling exceeds the
cost of not drilling. With dry-hole cost 1 and discovery return 8, drilling is
worth it when

$$P\times8 - (1-P)\times1 > 0
\qquad\Longleftrightarrow\qquad
P > \frac{1}{9} = 0.111 .$$

So the decision threshold is $P > 0.111$, not 0.5, and the answer is:

1. at the prospect's own base rate $p = 0.04$ (or 0.02), the posterior **0.33**
   (or 0.20) exceeds 0.111 — drill, if the likelihood ratio is really 12;
2. but the whole answer is sensitive to the prior and the likelihood ratio: at
   $p = 0.02$ the posterior is 0.197, and a likelihood ratio of 5 would give
   0.093 — below the threshold. **The decision is a bet on the prior and the
   attribute quality, not on the anomaly alone**, which is the content of
   [11-01-03](../../01-exploration-workflow/03-cost-benefit.md) and the
   reason a sensitivity table belongs in the report.

---

## ★★★8 — A worked ambiguity

**Method.** Take the lesson's model: $K_m = 36.6$, $\mu_m = 45.0$ GPa,
$\phi_c = 0.40$, brine $K = 2.2$, $\rho = 1000$, gas $K = 0.02$,
$\rho = 200$. Scan $\phi \in [0.10, 0.35]$ in steps of 0.001 and
$S_g \in [0, 1]$ in steps of 0.01, compute AI and $v_p/v_s$ at every node, and
select the pairs within 0.5% of a target AI.

**Result.** With the target taken as the $\phi = 0.25$, $S_g = 0.50$ sand
($\text{AI} = 8.807$ MRayl, $v_p/v_s = 1.4664$), the scan returns **250 nodes**
within 0.5% of the target impedance, spanning $\phi = 0.244$–$0.269$ and
$S_g = 0.00$–$0.94$:

| pair | $\phi$ | $S_g$ | AI (MRayl) | $v_p/v_s$ |
|---|---|---|---|---|
| gas-rich, low porosity | 0.244 | 0.94 | 8.82 | 1.466 |
| brine-filled, high porosity | 0.269 | 0.00 | 8.79 | 1.542 |

The two $v_p/v_s$ values differ by **5.2%** — larger than the 2% asked for, and
larger than a 3% attribute noise, so this pair is in fact separable, but only
just, and only with a $v_p/v_s$ estimate good to a few per cent.

**Tolerance.** 0.5% in impedance, well inside typical attribute noise (3–5%), so
the ambiguity in impedance is not an artefact of the search tolerance.

**What you would write.** *The cell's impedance is consistent with a
brine-filled sand at slightly lower porosity and with a 70%-gas sand at slightly
higher porosity; the two differ by 2.5% in $v_p/v_s$, which is comparable to the
attribute noise. Therefore the data constrain the impedance but not the fluid
uniquely; the interpretation should report the admitted range of $(S_g,\phi)$
and the measurement that would resolve it (a well, or a lower-noise
$v_p/v_s$ estimate from long-offset data).* That is a complete, checkable, and
honest answer — and it is more useful than a single number.
