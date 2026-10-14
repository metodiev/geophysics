# Solutions — 11-05-02 EM and ERT for Groundwater Mapping

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson: [02 EM and ERT for Groundwater Mapping](../02-em-and-ert-groundwater.md).

---

## ★1 — Geometric factors

**(a) Wenner:** $K = 2\pi a = 2\pi(5) = 31.42\ \mathrm{m}$.

**(b) Schlumberger:**

$$ K = \frac{\pi(L^{2}-MN^{2}/4)}{MN}
= \frac{\pi(900 - 6.25)}{5} = \frac{\pi(893.75)}{5} = 561.6\ \mathrm{m}. $$

$$ \rho_a = KR = 561.6 \times 0.42 = 235.9\ \Omega\,\mathrm{m}. $$

**Note.** The Schlumberger $K$ is $\approx 18$ times the Wenner $K$ here because
the current electrodes are far apart while the potential pair is close: the
array is much more sensitive to the deep, current-carrying volume.

---

## ★2 — Skin depth

$$ \delta = 503.29\sqrt{\rho/f}\ \mathrm{m}, \qquad
\rho = 50\ \Omega\,\mathrm{m}: $$

$$ \delta(1\ \mathrm{Hz}) = 503.29\sqrt{50} = 3558.8\ \mathrm{m}, $$
$$ \delta(10\ \mathrm{Hz}) = 503.29\sqrt{5} = 1125.4\ \mathrm{m}, $$
$$ \delta(100\ \mathrm{Hz}) = 503.29\sqrt{0.5} = 355.9\ \mathrm{m}. $$

Units: $[\rho] = \Omega\,\mathrm{m}$, $[f] = \mathrm{s^{-1}}$,
$[\mu_0] = \mathrm{H\,m^{-1}} = \mathrm{kg\,m\,A^{-2}\,s^{-2}}$, so
$\sqrt{\rho/(\omega\mu_0)}$ has units of metres. ✔

---

## ★3 — The two-layer series and its truncation

$k = (10-50)/(10+50) = -2/3$. With $h_1 = 8\ \mathrm{m}$ and $L = 10\
\mathrm{m}$, $(2nh_1/L) = 1.6n$.

| $n$ | term $k^{n}/(1+(1.6n)^{2})^{3/2}$ | partial $\rho_a$ ($\Omega$m) |
|---|---|---|
| 1 | $-0.099258$ | 40.07 |
| 2 | $+0.011795$ | 41.25 |
| 3 | $-0.002513$ | 41.00 |
| 6 | — | 41.060 |
| 400 (converged) | — | 41.057 |

Varying the upper limit from $n = 6$ to $n = 400$ moves the result by
$0.003\ \Omega\,\mathrm{m}$ ($< 0.01\%$) here, while at
$L = 20\ \mathrm{m}$ the same truncation moves it by $0.02\
\Omega\,\mathrm{m}$ on a $23.6\ \Omega\,\mathrm{m}$ value ($0.1\%$). Truncation error is
largest where the curve is steep, i.e. where the sounding crosses the layer.

---

## ★4 — Conductance equivalence

$$ S = \sigma h = 0.2 \times 5 = 1.0\ \mathrm{S}. $$

For $\sigma' = 0.5\ \mathrm{S\,m^{-1}}$ the equivalent thickness is

$$ h' = S/\sigma' = 1.0/0.5 = 2.0\ \mathrm{m}. $$

A sounding cannot distinguish them because, when the layer is thin compared with
its depth and with the array spacing, current crossing the layer spreads
laterally in proportion to the sheet conductance $\sigma h$; the individual
$\sigma$ and $h$ enter only through that product to first order. Only when the
spacing is comparable to the thickness — i.e. when the array can resolve the
layer's own geometry — do the two separate.

---

## ★5 — Why long spacings fix the depth

In

$$ \rho_a(L) = \rho_1\left[1 + 2\sum_{n\ge1}
\frac{k^{n}}{\left(1+(2nh_1/L)^{2}\right)^{3/2}}\right], $$

each term depends on the ratio $2nh_1/L$. For **large** $L$ the ratio is small,
the denominator approaches 1, and the series sums to
$\rho_1(1+k)/(1-k) = \rho_2$: the large-spacing response is controlled by
$\rho_2$ almost independently of $h_1$, so $\rho_2$ is fixed by the tail and
$h_1$ is fixed by *where* the curve turns — which requires those large spacings
to be present. For **short** spacings, $2h_1/L$ is large, the terms are tiny and
the curve sits near $\rho_1$: the layer is nearly invisible, so $h_1$ and
$\rho_2$ trade off along the equivalence direction. This is exactly what the
admitted-set table reports.

---

## ★6 — The alternative model along the least-determined direction

The direction is $(d\ln\rho_2, d\ln h_1) = (+0.449, -0.894)$. A $10\%$ increase
in $\rho_2$ is $d\ln\rho_2 = \ln(1.10) = 0.0953$. Moving along the direction by
a scale factor $s$ means

$$ d\ln h_1 = \frac{-0.894}{0.449}\times 0.0953 = -0.1898. $$

$$ h_1' = 7\,e^{-0.1898} = 7 \times 0.8271 = 5.79\ \mathrm{m}. $$

So the equally acceptable model is $\rho_2 \approx 13.2\
\Omega\,\mathrm{m}$, $h_1 \approx 5.8\ \mathrm{m}$ — the product
$\rho_2 h_1 = 84\ \Omega\,\mathrm{m^{2}}$ in the first model becomes
$76.4\ \Omega\,\mathrm{m^{2}}$, i.e. nearly unchanged (the residual change is the
second-order curvature the linearisation ignores). Reporting only the first
model would understate the depth uncertainty by about $17\%$.

---

## ★7 — Siting the borehole (specification)

**Target.** Resistive sand to about $40\ \mathrm{m}$, conductor (aquifer or clay)
from about $40$ to $60\ \mathrm{m}$.

**Largest $AB/2$.** The lesson's sensitivity analysis puts the peak sensitivity
to a boundary near $L/2$ and the $10\%$ sensitivity at about $1.9L$. To place the
peak at $50\ \mathrm{m}$, use $AB/2_{\max} \approx 100\ \mathrm{m}$ (peak near
$40$-$50\ \mathrm{m}$), consistent with the printed $41.4\ \mathrm{m}$ peak at
$AB/2 = 100\ \mathrm{m}$.

**$MN$ schedule.** Start at $MN = 2\ \mathrm{m}$ for the short spacings
($MN \ll L$ keeps $K \approx \pi L^{2}/MN$ valid), and increase $MN$ in
logarithmic steps so the measured voltage stays above the instrument noise floor;
the Schlumberger approximation degrades once $MN$ approaches $L/5$.

**Noise target.** Below $2\%$ relative, because the admitted-set demonstration
shows a $3\%$ noise level already widens a two-layer depth to
$7.4$-$9.5\ \mathrm{m}$ when the acquisition range is short.

**Number of soundings.** At least one per $20\ \mathrm{m}$ along the line, then
infill where the parameter trade-off is worst; better, a 2-D ERT profile so that
lateral change is modelled rather than aliased into layer thickness.

**Report.** If the inversion admits a family, report the family: a depth range
and the corresponding conductance range, with the noise level, the array
geometry and the regularisation weight that produced it. A single depth would be
a choice presented as a measurement.

---

## ★8 — ERT and FDEM disagreeing

**Physical causes.**
1. **Different weighting.** DC senses the conductor by current channelling
   through it; EM senses it by induction, and the two weight the same volume
   differently — a thin conductor is relatively more visible to EM.
2. **Anisotropy.** A dipping or fractured conductor has directional
   conductivity; the array geometries sample direction differently.
3. **Induced polarisation.** A polarisable clay or sulphide changes the DC
   voltage with a phase lag but appears mainly as conductivity to FDEM.

**Processing causes.**
1. **Calibration.** FDEM requires a zero-level (bucking) calibration; an offset
   changes apparent conductivity almost uniformly.
2. **Inversion regularisation.** Different smoothing weights produce different
   images from the same data.
3. **Layering assumption.** A 1-D interpretation of a 2-D or 3-D body biases
   each method by a different factor.

**Separating the leading candidate.** Log one borehole through the anomaly with
a conductivity log and a water sample. If the logged conductivity matches the
EM-derived value and both differ from the DC-derived value, the cause is a DC
weighting or IP effect; if it matches the DC value, the FDEM calibration or
inversion is at fault; if it matches neither, the layering assumption is.

---

## Worked mastery checkpoint

**(a) Geometric factor** at $AB/2 = 50\ \mathrm{m}$, $MN = 2\ \mathrm{m}$:

$$ K = \frac{\pi(L^{2}-MN^{2}/4)}{MN}
= \frac{\pi(2500 - 1)}{2} = 3925.8\ \mathrm{m}. $$

**(b) Why the late spacings fix only the conductance.** In the series
$\rho_a = \rho_1[1 + 2\sum k^{n}/(1+(2nh_1/L)^{2})^{3/2}]$, each term depends on
$2nh_1/L$. For large $L$ the denominator approaches 1 and the sum collapses to
$\rho_1(1+k)/(1-k) = \rho_2$: the late curve measures the deep conductor's
resistivity and barely depends on the cap thickness. The *position* of the
transition (which spacings are "late") is what carries the thickness, and it is
constrained only when the spacing range straddles the transition.

**(c) Skin depth** at $\rho = 20\ \Omega\,\mathrm{m}$, $f = 100\ \mathrm{Hz}$:

$$ \delta = 503.29\sqrt{20/100} = 503.29(0.4472) = 225.1\ \mathrm{m}. $$

The comparison is only qualitative. With $AB/2 = 150\ \mathrm{m}$ the DC
sounding is *most* sensitive near $L/2 \approx 75\ \mathrm{m}$ (the lesson's
sensitivity calculation) with a $10\%$ sensitivity level near $1.9L \approx
285\ \mathrm{m}$; the $100\ \mathrm{Hz}$ EM field has a skin depth of $225\
\mathrm{m}$ but its response integrates over the whole diffusive volume. The two
probe overlapping but different volumes and weight them differently, so they are
complementary rather than interchangeable.

**(d) The two pieces of information that would most reduce the ambiguity:** a
borehole with a resistivity log (to anchor the layer boundaries and resistivity
absolutely) and a wider spacing range or a second method (a seismic porosity, or
an EM sounding) to constrain the layer thickness independently of its
resistivity.
