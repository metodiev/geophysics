# Solutions — 05-08-01 The Borehole Environment and Invasion Profiles

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Every mud, diffusivity and tool weighting is a
> labelled SYNTHETIC input.

---

## ★1 — Four perturbations, and what they affect

| Perturbation | Most affected measurement |
|---|---|
| Stress release and hole enlargement (breakouts, washouts) | Caliper, image logs, and every tool whose signal includes borehole fluid (density, neutron) |
| Fluid replacement by filtrate (invasion) | Resistivity (all variants), NMR, and the gamma log if the mud is radioactive |
| Thermal disturbance by the drilling fluid | Temperature logs and any thermally sensitive tool; the basis of [05-09-01](../../09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md) |
| Pressure difference (overbalance) | The driver of bit 2; also the mudcake, which biases density and sonic |

---

## ★2 — $R_w$ versus $R_{mf}$

| | $R_w$ | $R_{mf}$ |
|---|---|---|
| Property of | the formation water | the drilling-fluid filtrate |
| Measured | on a produced-water sample, from a catalogue, or from SP | at the flowline with a resistivity cell |
| In Archie's law | yes (equation 5 of the lesson) | no |
| Sets | the saturation scale | the flushed-zone resistivity $R_{xo}$ |

In a fresh mud over a saline formation the two can differ by factors of tens.
Substituting one for the other produces a saturation that is wrong by the square
root of that factor.

---

## ★3 — Diffusivity and diffusion length

$3\ \mathrm{cm^2\,s^{-1}} = 3\times10^{-4}\ \mathrm{m^2\,s^{-1}}$.

| $t$ | $\sqrt{4Dt}$ |
|---|---|
| 10 h ($3.6\times10^4$ s) | $\sqrt{4(3\times10^{-4})(3.6\times10^4)} = \sqrt{43.2} = 6.57$ m |
| 100 h | 20.8 m |
| 1000 h | 65.7 m |

Note the contrast with the demonstration's $D = 3\times10^{-7}$ m² s⁻¹, which gives
decimetres. **The invasion radius is a strong function of the diffusivity**, and the
diffusivity is the least well known quantity in the model — which is why the
demonstration quotes its model as an illustration of geometry rather than as a
prediction of a real invasion radius.

---

## ★4 — The demonstration's invasion result

**(a)** Planar fronts 0.0976, 0.3128, 0.9883 m with exponents 0.5058 and 0.4997.
Cylindrical fronts 0.1701, 0.2596, 0.4338 m with exponents 0.1835 and 0.2229.

**(b)** Cylindrical diffusion from a fixed wall radius has three length scales
($r_w$, $\sqrt{Dt}$, the outer boundary) and is therefore not self-similar, so no
single $\sqrt{Dt}$ law applies; the growing circumference also means each unit of
radial advance requires proportionally more filtrate.

**(c)** The virgin formation's conductivity here is
$\sigma_t = 1/2000 = 5\times10^{-4}$ S m⁻¹. A 5 per cent excess is
$2.5\times10^{-5}$ S m⁻¹, i.e. a deep reading of $5.25\times10^{-4}$ S m⁻¹. The
measured deep values are 0.0712, 0.0890, 0.1352, 0.2066, 0.3573, 0.4633 S m⁻¹ at
10, 28, 100, 278, 1000 and 2778 h — all far above. **The 5 per cent level was
crossed before the first reported time (10 h)**, because the smooth profile tail
reaches the deep tool's weighting immediately. This is the quantitative reason a
deep induction reading in a permeable, invaded interval is never the virgin
formation value without a correction.

---

## ★5 — Geometric factor and apparent reading

**(a)** With $w(r) = e^{-(r-r_w)/L}r$ and $L = 0.15$ m, integrating numerically
over the same domain used to compute the reading gives

$$a = \frac{\int_{r_w}^{r_i} w\,\mathrm{d}r}{\int_{r_w}^{\infty} w\,\mathrm{d}r}
= 0.411 \quad\text{for } r_i = 0.25\ \mathrm{m}.$$

The geometric factor is large *because the weighting length is short*: a 0.15 m
exponential centroid means most of the response comes from within a few
decimetres. (For comparison, $L = 1.5$ m at the same $r_i$ gives $a = 0.0174$ —
which is why the deep tool of the demonstration is almost blind to a 0.26 m
invaded zone in *geometric-factor* terms, and yet still reads 2.7 times the virgin
conductivity through the profile tail.)

**(b)** $\sigma_{\text{app}} = a\sigma_{xo} + (1-a)\sigma_t
= 0.411(1.0) + 0.589(0.01) = 0.417$ S m⁻¹, so
$R_{\text{app}} = 2.40$ Ω m against a true $R_t = 100$ Ω m.

**(c)** It is a *weighted average of conductivity*, not the formation resistivity:
the reported 2.40 Ω m understates the formation by a factor of 42, and the
direction of the error is set by the filtrate being more conductive. Reporting this
number as "the formation resistivity" is the error that Section 3.5 of the lesson
quantifies as a saturation above 1.

---

## ★6 — Recomputing at 36 h

The front at 36 h is between the 10 h and 100 h values; from the fitted exponent
0.1835, $R_i(36) \approx 0.1701(3.6)^{0.1835} = 0.215$ m. The smooth-profile
correction recovers $R_t$ near 40 Ω m (the failure is not a function of time in the
range tested, because the smooth tail always contributes), while the step profile
with $r_i = 0.215$ m recovers within about 15 per cent of 2000 Ω m. **The
conclusion is that the failure is driven by profile shape, not by the elapsed
time.**

---

## ★7 — Non-circular invasion

**(a)** A 10:1 radial diffusivity contrast produces a front whose radius varies with
azimuth by of order the square root of the diffusivity ratio, i.e. a factor of about
3 in the front position — a strongly non-circular invaded zone.

**(b)** The model needs an azimuthal dependence in $D$, i.e. a direction for the
contrast, which in a real well corresponds to a fracture or a high-permeability
streak.

**(c)** The test is a four- or six-arm caliper plus an image log (fracture
orientation), or a directional resistivity tool that resolves azimuth. Without one
of those, a radial model is the only available choice and its error is
unquantified.

---

## ★8 — Adding a shape parameter

A defensible parameterisation is a power-law profile
$c(r) = \exp[-\alpha((r-r_w)/(r_i-r_w))^p]$ with $p$ the shape parameter ($p = 1$
near-exponential, large $p$ near-step). With three readings, solve for
$(R_{xo}, R_t, p)$ by least squares.

Reported result to expect: the step profile is recovered with $p$ large and a small
residual; the smooth diffusion profile is recovered with $p \approx 1$–$2$ and the
residual in $R_t$ falls from 98 per cent to a few tens of per cent. A *direct*
constraint on the shape requires a measurement of the resistivity at a known radius
— a resistivity image log, or a second shallow reading with a different depth of
investigation — which is exactly what a modern multi-spacing induction array
provides.
