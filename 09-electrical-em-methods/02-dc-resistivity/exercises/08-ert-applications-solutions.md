# Solutions — 09-02-08 ERT Applications: Aquifers, Contamination, Landslides, Archaeology

> **Read after attempting the exercises.** Lesson:
> [08 ERT Applications](../08-ert-applications.md).

---

## ★1 — Saline intrusion minimum

$\rho_a$ minimum $= 42.40\ \Omega\,\mathrm{m}$ at $a = 20$ m, in a model whose
layer values are $80\ \Omega\,\mathrm{m}$ (0–4 m), $3\ \Omega\,\mathrm{m}$
(4–24 m) and $60\ \Omega\,\mathrm{m}$ (below). The minimum is *not* at the
layer value: the array at 20 m still averages the overburden, which is why
$\rho_a$ remains 14 times the layer resistivity.

---

## ★2 — Uncertainty factor

Range 4.0–13.0 m about a true 10.0 m is a factor $13.0/4.0 = 3.25$ end to end,
or $\pm$ a factor 1.9 about the mid-point of the logs
($\sqrt{4\times13} = 7.21$).

---

## ★3 — Anomaly and sign

Resistive wall:
$(87.64-60)/60 = +46.1\%$.
Conductive pit: $(52-60)/60 = -13.3\%$.

Both are detectable at 2% noise; the *sign* distinguishes a resistive wall from
a conductive feature, and the amplitude difference (46% against 13%) reflects the
fact that a resistive body has a much larger contrast requirement to produce a
given anomaly in a conductive host.

---

## ★4 — Required depth separation

The patterns at 5 m and 18 m differ by (at least) the difference of their
amplitudes, roughly $3.81\% - 2.12\% = 1.69\%$ in the worst case. The
demonstration measured $\chi^{2} = 0.1$ for a 5 m separation, so
$\chi^{2}\propto(\text{separation})^{p}$ with $p$ unknown. Using
$\chi^{2}\propto(\Delta d)^{4}$ (the natural scaling when the pattern difference
is a second difference of a smooth function):

$$1.0 = 0.1\left(\frac{\Delta d}{5}\right)^{4}
\Rightarrow \frac{\Delta d}{5} = 10^{1/4} = 1.778
\Rightarrow \Delta d \approx 8.9\ \mathrm{m}.$$

With the more conservative $\chi^{2}\propto(\Delta d)^{2}$:
$\Delta d = 5\sqrt{10} = 15.8$ m. So the depth resolution at 10–18 m depth is
between about 9 and 16 m — **of the same order as the depth itself**. Either
way, the conclusion of the lesson stands: at this separation and noise level a
change at 8 m and a change at 12 m cannot be told apart.

---

## ★5 — A 1 m target at 12 m

- Spacing for depth: $a = 12/1.787 = 6.7$ m.
- Footprint: $2.51a = 16.8$ m.

The target is 1 m and the footprint is 16.8 m: **a factor 17 too coarse.** The
conclusion is that a slip surface cannot be *resolved* at 12 m depth by any
surface array of this kind; the survey can locate where the *bulk* moisture
content changes, which may (indirectly) mark the surface's position, but the
report must not claim metre-scale resolution. The only honest options are to
detect the surface's effect on a thicker volume, or to use a borehole method
(module 09-06).

---

## ★6 — A 4×4 m grid for archaeology

Along one line, dipole-dipole with $n = 1..3$: 4 electrodes give
$\text{count}(n=1) = 4-5+1 = 0$ — **the line is too short** for even $n = 1$
with a 4-electrode array. So a 4×4 m grid cannot support dipole-dipole at all.

What it can support is a single quadrupole configuration (two current, two
potential electrodes) or a Wenner array with $a = 1$ m, whose DOI is about 0.52 m
(2.60 m at $a = 5$ m, scaled by 1/5). The wall at 1 m depth is at about twice the
Wenner DOI, so it would be **marginal at best**, and the footprint at 1 m depth
would be about 3.6 m wide (18.2 m at $a = 5$ m, scaled) — wider than the survey
grid. The archaeological conclusion: a 0.5 m wall at 1 m depth needs a *sub-metre*
electrode spacing, i.e. a 0.5 m spacing and a line of at least 8–10 electrodes,
together with a small current because the voltages are large
($\Delta V = \rho I/k$ with $k = 2\pi\times0.5 = 3.14$ m, so a 1 mA current on
60 $\Omega\,\mathrm{m}$ soil already gives 19 mV).

---

## ★7 — Monitoring a landfill liner at 6 m

1. **Array and spacing.** Dipole-dipole, $n = 1..6$, $a = 3.4$ m
   ($= 6/1.787$), aperture 27 m.
2. **Current and stacking.** $|k| = 1055.58\times3.4 = 3589$ m;
   $\Delta V = \rho I/|k|$ with the *conductive* leachate case $\rho \approx 20\
   \Omega\,\mathrm{m}$ gives $0.0056I$ V, i.e. 0.56 mV at $I = 0.1$ A — just at a
   0.5 mV floor. Use $I = 0.5$ A (2.8 mV) and 16-fold stacking (effective noise
   0.125 mV), giving a comfortable margin.
3. **Required detection.** A 10% change in a 1 m layer at 6 m: from the
   lesson's Section 3 pattern magnitudes, a 20% change in a 3 m layer at 5 m
   gives 3.81%; scaling by the ratio of layer thicknesses and change magnitudes
   gives about $3.81\%\times(1/3)\times(0.5) = 0.64\%$ — well below a 2% noise
   floor on a *single* measurement. Averaging many measurements that share the
   target's sensitivity (say 20) reduces the noise by $\sqrt{20} = 4.5$, to
   0.44%: the change becomes marginally detectable. **The design must therefore
   rely on averaging, and the reported detection limit must be the averaged
   one.**
4. **Most likely false positive.** Seasonality: soil moisture and temperature
   both change a shallow, conductive layer by more than 10%
   ([09-01-05](../../01-electrical-properties-of-earth/05-temperature-and-pressure-effects.md)
   gives 2.6% per kelvin). A winter-to-summer difference can produce a
   spurious "leak".
5. **Test.** Install a temperature/soil-moisture reference station and a
   *control* line away from the landfill. Re-occupy the control line each epoch:
   if the control shows the same change, the anomaly is seasonal, not a leak.

---

## ★8 — A third explanation: temperature

From [09-01-05](../../01-electrical-properties-of-earth/05-temperature-and-pressure-effects.md),
$\alpha = 2.61\%$ per kelvin for $E_a = 0.20$ eV. To produce $-40\%$ in
resistivity (i.e. $+67\%$ in conductivity) requires

$$\Delta T = \frac{\ln(1.67)}{0.026109} = \frac{0.5129}{0.026109}
= 19.6\ \mathrm{K}.$$

That is large but entirely possible in a thermal plume, an artificial recharge
scheme, or a seasonal ground-water temperature cycle at shallow depth. So:

| explanation | size required | independent measurement |
|---|---|---|
| water-table rise | ~10 m rise (from the lesson's arithmetic, a 3 m rise gives only 8%) | water level in a piezometer |
| salinity change | factor ~2 in $\rho_w$ | water sample, EC log |
| temperature | $+19.6$ K | thermistor string or fibre-optic DTS |

The measurement that separates all three is a **multi-parameter borehole
observation** (water level, EC, temperature) at one location inside the anomaly
footprint. With it, the resistivity anomaly becomes an *interpolation* between
measurements rather than an inference; without it, all three explanations remain
live and must be reported as such.
