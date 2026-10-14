# Solutions — 09-05-05 EM for Contaminant Plumes, Salinity and Leachate

> **Read after attempting.** Lesson:
> [05 EM for Contaminant Plumes, Salinity and Leachate](../05-em-environmental.md).

---

## ★1 — Bulk conductivity at $25$ mol/m³

$$\sigma_w = 0.0126 \times 25 = 0.315\ \mathrm{S/m},
\qquad
\sigma_{\text{bulk}} = \frac{0.315}{6.617} + 0.0020
= 0.04760 + 0.0020 = 0.0496\ \mathrm{S/m},$$

i.e. $\rho = 20.2\ \Omega$ m. The surface term is $4.0\%$ of the total here,
against $51.2\%$ at $c = 1$ mol/m³: at $25$ mol/m³ the pore fluid dominates.

---

## ★2 — Response change

From the table, $c = 200$ mol/m³ at $t = 10$ m gives $0.9397$, a change of
$-6.03\%$ from the background. That is above a $5\%$ threshold and well above a
$1\%$ threshold, so the layer would be detected at either noise level for this
geometry.

---

## ★3 — Same concentration, different soil

Because the pore geometry enters twice: through the formation factor, which
divides the fluid conductivity, and through the surface-conduction term, which
adds to it. A clay has a small $F$-equivalent (more, and more tortuous, water
paths) and a large surface term, so the same pore fluid yields a different, and
more surface-dominated, bulk conductivity.

---

## ★4 — Crossover concentration

Setting the two contributions equal:

$$\frac{\Lambda c}{F} = \sigma_s
\;\Longrightarrow\;
c = \frac{\sigma_s F}{\Lambda}
= \frac{0.005 \times 10}{0.0126} = 3.97\ \mathrm{mol/m^3}.$$

Below about $4$ mol/m³ of this assumed ion, a conductivity measurement on that
soil is mapping surface chemistry rather than contamination. This is the
quantitative form of the standard caution that a conductivity map of a clay-rich
site may contain no plume information at all.

---

## ★5 — Conductance required for a $5\%$ response

From the table: $0.0645$ S ($2$ m), $0.1260$ S ($5$ m), $0.2292$ S ($10$ m) and
$0.4350$ S ($20$ m). The conductance required is **not constant** — it grows with
thickness because a thicker layer is farther from the surface of the responding
volume in the thin-layer limit and because the background section differs. Its
value roughly triples as the thickness goes from $2$ to $20$ m, i.e. it grows as
$t^{0.63}$.

For a $1\%$ threshold the required conductance falls by a factor of about five
(a $5\%$ response needs five times the conductance of a $1\%$ response only if
the response is linear in conductance, which the measured near-linearity of the
plume response supports). So the numbers above should be divided by about five.

---

## ★6 — Thicknesses consistent with "$10$ mol/m³"

From the threshold table, $10$ mol/m³ is below the $5\%$-detection concentration
at every tabulated thickness ($15.89$, $12.19$, $10.99$ and $10.37$ mol/m³ for
$2$, $5$, $10$ and $20$ m). So the claim "$10$ mol/m³" as a *detected plume* is
consistent with a thickness of about $20$ m or more at a $5\%$ threshold, and with
a thin layer only if the threshold is better than $5\%$. Reporting the
concentration without the thickness is reporting a member of a family
inconsistent with the stated detection level for small thicknesses — which is
exactly the error this lesson's equivalence warning addresses.

---

## ★7 — Survey design (specification)

**Band.** The measured response grows with conductance and is largest at the
lower frequencies tested; a loop at $100$ Hz with a $20$ m separation gives
$6$–$13\%$ changes for the stronger plumes in the table. The design band is
therefore $100$–$1000$ Hz, with the choice fixed by the depth of the plume
($10$ m) and the requirement that the diffusion depth of the window reaches it.

**Station spacing.** At least five to eight stations across the anomaly: for a
$5$ m thick plume at $10$ m depth the lateral extent is unknown, so an initial
line at $10$ m spacing, refined to $5$ m over the anomaly, is appropriate.

**Repeat policy.** Repeat one third of the stations within the same day, measure
one base station every hour, and level to it; the target detectability of $3\%$
requires a repeatability of better than $1\%$, which is a stated design
requirement rather than an instrument specification.

**Statistic.** A paired comparison of the anomaly amplitude against the local
background, with the equivalence band converted into an admitted range of
concentration–thickness pairs: report both the range (e.g. "$c = 12$–$16$ mol/m³
for $t = 2$–$5$ m") and the conductance it implies ($0.06$–$0.13$ S).

---

## ★8 — Which omissions matter

- **Plume geometry (three-dimensional):** changes the **detectability**. A
  three-dimensional body of finite lateral extent produces a smaller anomaly than
  the layered model for the same conductivity and thickness, because current can
  flow around it; the one-dimensional result is an upper bound.
- **Concentration gradient:** changes the **interpretation**, not primarily the
  detectability. The measured response integrates the conductance within its
  kernel, so a smooth gradient is seen as an average conductance — the datum
  remains as detectable, but the reported concentration refers to an average over
  the kernel and not to any sampled point.
- **Temperature effect:** changes both. A temperature contrast changes the pore
  fluid's conductivity independently of its chemistry, so it alters the
  detectability of a given concentration *and* changes the interpretation,
  because the petrophysical conversion from conductivity to concentration assumed
  a temperature.

**Reason for the split.** Detectability depends on the *total conductance* inside
the response kernel and on whether that conductance is spatially extended or
compact; interpretation depends on the *mapping* from the measured average to the
target quantity, and it is that mapping which geometry, gradients and temperature
distort.
