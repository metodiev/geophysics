# Solutions — 14-02-01 ERT for Aquifer Characterisation and Salinity Mapping

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All sites are **SYNTHETIC**.

Lesson: [01 ERT for Aquifer Characterisation and Salinity Mapping](../01-ert-for-hydrology.md).

---

## ★1 — Reflection coefficient and limits

$$k = \frac{\rho_2 - \rho_1}{\rho_2 + \rho_1} = \frac{25 - 100}{25 + 100}
= \frac{-75}{125} = -0.600.$$

The negative sign says layer 2 is more conductive than layer 1, so $\rho_a$ falls
as the array widens.

**$a \to 0$:** the array samples only the near-surface, so
$\rho_a \to \rho_1 = 100\ \Omega$ m. (Verified in the demonstration: at
$a = 0.5$ m the series returns 120.0 for $\rho_1 = 120$.)

**$h \to 0$:** layer 1 disappears, the array sits on the half-space, and
$\rho_a \to \rho_2 = 25\ \Omega$ m. (Verified: the demonstration returns 5.0000 for
$\rho_2 = 5$.)

Both limits are properties of the series, not of the array geometry, so they are the
first two things to check when implementing a forward model.

---

## ★2 — Half-amplitude spacing and depth

Interpolate in $\log_{10}a$ between $(a = 8, y = 0.705)$ and $(a = 12, y = 0.454)$
for $y = 0.5$:
$$f = \frac{0.705 - 0.500}{0.705 - 0.454} = \frac{0.205}{0.251} = 0.8167,$$
$$\log_{10}a_{50} = \log_{10}8 + f(\log_{10}12 - \log_{10}8)
= 0.9031 + 0.8167(0.1761) = 1.0469,$$
$$a_{50} = 10^{1.0469} = 11.14\ \mathrm{m}.$$

$$h \approx \frac{a_{50}}{1.4} = \frac{11.14}{1.4} = 7.96\ \mathrm{m},$$
against a true $h = 8$ m: an error of $0.5\%$.

**Comment.** The rule works well here because the contrast is strong. It is an
empirical calibration of a *sensitivity* argument (the Wenner kernel's centroid is
near $a/2$, and the half-amplitude point falls at roughly $1.4h$), and it degrades
for weak contrasts — for which the whole depth band widens, as §3 of the lesson
measures.

---

## ★3 — Resistivity to salinity

$$\rho_w = \frac{\rho_{\text{bulk}}\,\phi^{m}}{a}
= 55 \times 0.30^{2} = 55 \times 0.09 = 4.95\ \Omega\,\mathrm{m},$$
$$\sigma_w = \frac{1}{4.95} = 0.2020\ \mathrm{S\,m^{-1}},$$
$$\mathrm{TDS} = \frac{\sigma_w}{0.15}\,\mathrm{g\,L^{-1}} \times 1000
= \frac{0.2020}{0.15} \times 1000 = 1347\ \mathrm{mg\,L^{-1}}.$$

Slightly brackish. Note the arithmetic chain and the two model-dependent links in
it: $m = 2$ (a model choice) and $0.15$ (a calibration).

---

## ★★4 — The porosity/cementation ambiguity

**Porosity, at $m = 2$, $\rho_{\text{bulk}} = 60\ \Omega$ m:** $\rho_w = 60\phi^{2}$
and $\mathrm{TDS} = (1/\rho_w)/0.15 \times 1000$.

| $\phi$ | $\rho_w$ ($\Omega$ m) | TDS (mg L$^{-1}$) |
|---|---|---|
| 0.25 | 3.75 | 1778 |
| 0.30 | 5.40 | 1235 |
| 0.35 | 7.35 | 907 |

**Cementation exponent, at $\phi = 0.30$:** $\rho_w = 60(0.30)^{m}$.

| $m$ | $\rho_w$ ($\Omega$ m) | TDS (mg L$^{-1}$) |
|---|---|---|
| 1.8 | 6.87 | 970 |
| 2.0 | 5.40 | 1235 |
| 2.2 | 4.24 | 1571 |

**Full range: 907 to 1778 mg L$^{-1}$** from porosity alone (a factor of 1.96), and
970 to 1571 mg L$^{-1}$ from the cementation exponent (a factor of 1.62). Both
together span roughly a factor of three.

**Which dominates.** Porosity does, but only mildly — the two are comparable, which
is itself the important result: assuming $m = 2$ without evidence is as damaging as
being unsure about porosity. The reason is that the two enter through the same
product $\phi^{m}$; **the data constrain $\phi^{m}\rho_w$, and every pair
$(\phi, m)$ that preserves it fits equally well.** This is the same degeneracy
analysed in
[09-01-02 Archie's Law](../../../09-electrical-em-methods/01-electrical-properties-of-earth/02-archies-law.md);
in a hydrogeophysical survey it is broken only by an independent porosity — from a
log, from seismic velocity, or from NMR.

---

## ★★5 — Time-lapse: salinity, temperature, saturation

**Baseline.** TDS $= 800\ \mathrm{mg\,L^{-1}}$:
$$\rho_w = \frac{1}{0.15 \times 0.8} = 8.333\ \Omega\,\mathrm{m}, \qquad
\rho_{\text{bulk}} = \frac{8.333}{0.28^{2}} = \frac{8.333}{0.0784}
= 106.3\ \Omega\,\mathrm{m}.$$

**A 9.1% drop** gives $\rho_{\text{bulk}} = 96.6\ \Omega$ m, hence
$$\rho_w = 96.6 \times 0.0784 = 7.575\ \Omega\,\mathrm{m}, \qquad
\sigma_w = 0.1320\ \mathrm{S\,m^{-1}}, \qquad
\mathrm{TDS} = \frac{0.1320}{0.15} \times 1000 = 880\ \mathrm{mg\,L^{-1}}.$$

So the salinity explanation is a **+10% rise** in TDS, i.e. 80 mg L$^{-1}$ of added
dissolved solids — a seawater fraction of about 4% from the mixing relation of
[14-01-05](../../01-hydrology-fundamentals/05-groundwater-chemistry.md).

**Temperature.** Water conductivity rises about 2% per $^\circ$C, so a 9.1% rise in
conductivity corresponds to
$$\Delta T = \frac{9.1}{2} = 4.55\ ^\circ\mathrm{C}.$$

**Could a falling water table do it?** No — and the sign is decisive.
$\rho_{\text{bulk}} \propto S_w^{-n}$ with $n = 2$, so *lowering* the saturation
**raises** the resistivity. Explaining the observed **drop** would require
$S_w > 1$, which is impossible. So a falling water table (or a falling water level
in the sampled zone) is excluded outright, whereas a *rising* water table could
contribute to the drop and must be checked. This kind of sign argument eliminates
whole classes of explanation before any modelling, and it is worth doing first.

**What it means in practice.** A 9.1% drop is explained equally well by +10% salinity
or by +4.6 $^\circ$C. A single ERT line cannot tell them apart; a piezometer with a
temperature logger and a chloride sample can, which is why the standard monitoring
design pairs the two.

---

## ★★6 — Spacing design for a 12 m target

**Coverage rule:** bracket the transition with spacings from about $0.25h$ to $5h$:
$$0.25 \times 12 = 3\ \mathrm{m}, \qquad 5 \times 12 = 60\ \mathrm{m}.$$

A practical Wenner list using standard cable take-outs, one per octave plus
intermediate points:
$$3,\ 4,\ 6,\ 8,\ 12,\ 16,\ 24,\ 32,\ 48,\ 60\ \mathrm{m}.$$

**Expected half-amplitude spacing:** $a_{50} \approx 1.4h = 16.8$ m, so the curve
should be near $0.5\rho_1$ at $a \approx 16$ m. Include a value either side
(12 and 24 m) so that the transition is bracketed rather than assumed.

**Two design cautions.** (i) The largest spacing sets the *depth of investigation*
but the smallest spacings are what fix the near-surface resistivity, which is a
nuisance parameter that the inversion will trade against the target; include at
least three spacings well above the target if the near-surface is heterogeneous.
(ii) A 60 m Wenner array needs 180 m of cable and a current electrode pair driven
60 m apart, which is often the practical limit on a coastal strip.

---

## ★★★7 — Detecting a thin saline layer

**Conductances.** Layer: $b/\rho = 1/2 = 0.5\ \mathrm{S}$.
Overburden: $20/40 = 0.5\ \mathrm{S}$.

**The two conductances are equal.** A surface measurement sees the *total*
conductance of the column, and the target contributes exactly as much as the
20 m of sand above it. That is the worst case for detection: the target doubles the
column conductance, so the *change* it produces is a factor-of-two change in a
quantity the data measure indirectly — detectable in principle, but only if the
overburden conductance is known to much better than a factor of two. In a real
survey the overburden resistivity is itself uncertain by tens of per cent, so the
thin layer is effectively **undetectable by a surface Wenner sounding** on the basis
of its conductance alone.

**A measurement strategy that could detect it.** Use a geometry whose sensitivity
is concentrated near 20 m depth rather than integrated over the whole column:

- **Larger spacings with dense coverage** (e.g. a 2-D ERT section with 5 m
  electrode spacing and 10–100 m separations), so that the layer's *inflection*
  appears in the shape of the curve rather than in its level. Sensitivity to a thin
  layer grows as the array's kernel concentrates near it — but the *shape* signal
  from a layer whose conductance equals the overburden's is weak, so this is a
  marginal improvement, not a solution.
- **Borehole or cross-hole measurements** — a downhole conductivity log through
  20 m measures the layer directly with no intervening ambiguity
  ([07 Borehole Geophysics](../07-borehole-hydrogeophysics.md)), or cross-hole ERT
  ([09-06-01 Cross-Hole Tomography](../../../09-electrical-em-methods/06-borehole-electrical/01-cross-hole-tomography.md))
  images it between two holes. Both remove the surface-integration problem.
- **A time-lapse target** if the layer's salinity changes (for example with
  pumping), since the difference removes the static overburden entirely.

**A strategy that definitely could not.** A single Wenner sounding, or a small
array ($a \le 5$ m) whose sensitivity never reaches 20 m: the layer contributes
essentially nothing to the response, and the inverted model will simply report the
average overburden resistivity. Scaling the same conclusion: **surface
resistivity cannot detect a conductive layer whose conductance is comparable to
the overburden's when the overburden itself is uncertain.**

**Arithmetic summary of the argument.**
$$\text{column conductance with layer} = \frac{20}{40} + \frac{1}{2}
= 1.00\ \mathrm{S},$$
$$\text{column conductance without layer} = 0.50\ \mathrm{S},$$
so the *detectable* quantity changes by a factor of 2 while the *nuisance*
parameter (overburden resistivity) is itself uncertain by a factor of about 1.4–2.
Detection requires the nuisance uncertainty to be several times smaller than the
target's contribution — here it is comparable, so the target is not separable.

---

## ★★★8 — Bootstrap uncertainty analysis

**Procedure.**

1. Fit the eight-point curve by least squares to obtain $(\hat\rho_2, \hat h)$ and
   the residual vector $r_i = (\rho_a^{\text{meas}} - \rho_a^{\text{pred}})/\sigma_i$.
2. Generate $B = 1000$ bootstrap datasets by resampling the residuals **with
   replacement** and adding them to the predicted curve:
   $\rho_a^{(b)}_i = \rho_a^{\text{pred}}_i + r_{j(i)}$ for random indices $j(i)$.
3. Refit each bootstrap dataset from the same starting model, keeping the
   starting model fixed so that the spread reflects the data and not the
   optimiser.
4. Report the **5th and 95th percentiles** of $\rho_2$ and of $h$ — a 90% interval
   — along with the number of realisations that failed to converge (which must be
   stated, because a failed fit is information).

**What the ranges will look like, and why.**

- The misfit surface is much flatter in the $\rho_2$ direction than in the $h$
  direction. In the lesson's depth scan, a 1 m error in $h$ costs 12.5% misfit
  while the best-fit $\rho_2$ changes by 22% (6.09 versus 5.00) to absorb it. So
  $h$ is the stiff direction and $\rho_2$ the soft one, and the bootstrap interval
  for $\rho_2$ will be **several times wider than the interval for $h$**, in
  agreement with the direct fit's errors ($+10.0\%$ in $\rho_2$ against $-2.1\%$ in
  $h$).
- Both intervals scale roughly linearly with the noise level: halving the noise
  halves the widths. Expect a 90% interval for $\rho_2$ of order $\pm10\%$ and for
  $h$ of order $\pm0.3$ m at 5% noise.
- The intervals will be **asymmetric**, because the sensitivity to $\rho_2$
  grows as $\rho_2 \to 0$ (the model becomes more conductive and the curve more
  extreme), so the negative side should be slightly wider.

**What the bootstrap will not capture.** Correlated or systematic error: a
mis-specified forward model (3-D structure under a 1-D inversion), an electrode
position error, a wrong $\rho_1$, or a biased Archie $m$ assumption. The bootstrap
redistributes the residuals it is given, so it estimates *random* uncertainty
only. Systematic model error must be estimated by inverting alternative models,
and stating that separately is the difference between a defensible uncertainty
statement and a misleading one.
