---
id: 17-08-04
title: "Cryosphere Remote Sensing: Ice, Snow and Permafrost"
level: research
prereqs: ["17-02-01", "17-02-05", "17-03-02"]
tags: [remote-sensing, earth-observation, cryosphere, snow, glaciers, permafrost, feature-tracking]
---

# Cryosphere Remote Sensing: Ice, Snow and Permafrost

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** that a cryospheric product (albedo, snow depth, glacier velocity,
   thaw subsidence) is an inference, and **name** the model each one rests on.
2. **Compute** a synthetic snow albedo as a function of grain size and impurity,
   and **state** why one channel cannot separate the two causes of darkening.
3. **Retrieve** snow depth from a synthetic brightness-temperature difference,
   **demonstrate** the saturation of the relation, and **quantify** the error
   from an uncorrected forest.
4. **Measure** a displacement between two synthetic images by
   cross-correlation, **convert** it to a surface velocity, and **state** the
   uncertainty floor set by pixel quantisation.
5. **Distinguish** a seasonal thaw signal from a secular subsidence trend in a
   synthetic displacement series.
6. **State** which cryospheric signals are direct measurements and which are
   proxies.
7. **Report** a cryospheric product with the model, the saturation range and the
   resolution that produced it.

## Prerequisites

- [17-02-01 Multispectral Imaging, Band Ratios and Indices](../02-optical-and-thermal-remote-sensing/01-multispectral-imaging.md)
  — the optical indices used for snow and ice.
- [17-02-05 Change Detection and Time-Series Analysis](../02-optical-and-thermal-remote-sensing/05-change-detection.md)
  — change detection, the basis of feature tracking.
- [17-03-02 InSAR: Interferometric Phase and Deformation Measurement](../03-radar-remote-sensing/02-insar.md)
  — the radar measurement of displacement used for subsidence.

> All models and data in this module are **SYNTHETIC**. The albedo model, the
> depth relation, the imagery and the subsidence series below are chosen
> teaching values, not measurements of any real glacier, snowpack or permafrost
> site. No site, glacier or region is named.

## 1. One folder, four different inferences

"Cryosphere remote sensing" is not one method but several, bound by a common
difficulty: the surface is cold, bright, often in darkness, and changing. Each
product is an inference through its own model.

- **Snow albedo** is an inference from reflectance; darkening has more than one
  cause.
- **Snow depth** is an inference from a microwave signal that *saturates*.
- **Glacier velocity** is a *displacement measurement*, precise to a fraction of
  a pixel, and dominated by its resolution.
- **Permafrost thaw** is a *subsidence* signal buried under a large seasonal
  cycle.

The honest thread is that each method has a **regime** — a range of values where
it works — and outside that regime the product is either biased or
uninformative, often without any visible failure.

## 2. Definitions

- **Broadband albedo**: the fraction of incident solar energy reflected,
  dimensionless, in $[0, 1]$.
- **Grain size**: the effective optical grain diameter of snow ($\mu$m);
  larger grains absorb more and appear darker.
- **Brightness-temperature difference** $\Delta T_B = T_B(19\ \mathrm{GHz}) -
  T_B(37\ \mathrm{GHz})$: a passive-microwave proxy for snow depth.
- **Feature tracking**: measuring displacement by the shift that best aligns a
  patch between two images.
- **Subsidence**: downward surface displacement, e.g. from thawing ground ice.

## 3. Derivations

### 3.1 The saturation scale

The depth relation reaches a fraction $1 - e^{-\mathrm{SD}/45}$ of its
asymptotic value, so its characteristic scale is $45\ \mathrm{cm}$. Three useful
values follow from that single constant: at $\mathrm{SD} = 45\ \mathrm{cm}$ the
signal is $1 - e^{-1} = 63\%$ of maximum; at $90\ \mathrm{cm}$ it is $1 - e^{-2}
= 86\%$; and at $135\ \mathrm{cm}$ it is $1 - e^{-3} = 95\%$. Beyond roughly two
to three times the scale length the signal barely changes with depth, so the
*retrieval* — which divides the signal by a fixed coefficient — becomes
insensitive and its absolute bias grows without bound. The scale length is thus
the honest upper bound on the useful range: state it, rather than expecting a
single coefficient to work at all depths.

### 3.2 Snow albedo

A synthetic broadband albedo model that captures the two effects is

$$
\alpha(g, s) = 0.99 - 0.22\left(1 - e^{-g/250}\right) - 0.35\,s,
$$

with grain size $g$ in micrometres and impurity fraction $s$ (dimensionless).
Albedo falls with both; the first term dominates for clean snow, the second for
dirty snow.

### 3.3 Snow depth from a microwave difference

The passive-microwave depth relation is empirical and saturating:

$$
\mathrm{SD} = c\,\Delta T_B, \qquad
\Delta T_B(\mathrm{SD}) = 6.0\left(1 - e^{-\mathrm{SD}/45}\right)(1 - 0.6 f),
$$

where $f$ is forest fraction and the retrieved depth uses a *fixed* coefficient
$c$ fitted to the shallow-snow regime.

### 3.4 Displacement by cross-correlation

Given two images $I_1$ and $I_2$ separated by time $\Delta t$, the displacement
is the shift $\mathbf{d}$ maximising the cross-correlation. With pixel size
$p$ (m) and interval $\Delta t$ (days), the surface speed is

$$
v = \frac{\lVert \mathbf{d}\rVert\,p}{\Delta t}\times 365.25
\qquad [\mathrm{m\,yr^{-1}}].
$$

### 3.5 Uncertainty of a correlation displacement

The displacement is found on an integer-pixel grid, so each component carries an
uncertainty of about $\pm 0.5$ pixel. Because the speed is proportional to the
displacement magnitude, the relative uncertainty is

$$
\frac{\delta v}{v} = \frac{0.5\ \text{px}}{\lVert \mathbf{d} \rVert},
$$

so the *smaller* the displacement in pixels, the *larger* the relative error.
For the worked case $\lVert \mathbf{d} \rVert = 3.606$ px this is
$0.5/3.606 = 0.139$, i.e. $13.9\%$ — the figure used in §6. Sub-pixel
refinement (fitting a parabola to the correlation peak, or an interpolation of
the image) reduces the uncertainty toward $\pm 0.1$ pixel, and it is the
standard remedy when the motion is small. It does not help when the images lack
texture: there the peak is ill-defined rather than merely quantised, and the
error is set by texture, not by pixel size.

## 4. Worked example 1 — albedo and snow depth

From [`code/cryosphere_rs_demo.py`](code/cryosphere_rs_demo.py):

| Grain ($\mu$m) | Clean albedo | With 5% impurity |
|---|---|---|
| 50 | 0.950 | 0.933 |
| 100 | 0.917 | 0.900 |
| 200 | 0.869 | 0.851 |
| 500 | 0.800 | 0.782 |
| 1000 | 0.774 | 0.757 |

Clean albedo falls from $0.950$ at fine grain to $0.774$ at coarse grain — a
drop of $0.176$. But adding $5\%$ impurity at *fine* grain ($0.933$) is nearly
the same as *growing* the grain to $100\ \mu$m ($0.917$): the two causes of
darkening are comparable. A single broadband channel cannot separate "old,
coarse snow" from "dirty snow", and the two have very different melt
implications. That separation needs spectral shape, not a single albedo.

## 5. Snow depth: saturation and forest

With the fixed coefficient $c = 7.5\ \mathrm{cm\,K^{-1}}$:

| True SD (cm) | $\Delta T_B$ (K) | Retrieved (cm) | Bias (cm) |
|---|---|---|---|
| 5 | 0.631 | 4.7 | $-0.3$ |
| 15 | 1.701 | 12.8 | $-2.2$ |
| 40 | 3.533 | 26.5 | $-13.5$ |
| 80 | 4.986 | 37.4 | $-42.6$ |
| 150 | 5.786 | 43.4 | $-106.6$ |

The retrieval is nearly unbiased for shallow snow and increasingly wrong for deep
snow: at $150\ \mathrm{cm}$ it returns $43\ \mathrm{cm}$, a gross underestimate.
The relation *saturates* — past roughly half a metre the microwave signal barely
grows — so no coefficient recovers deep snow from this single difference.

Forest compounds the error:

| Forest fraction | $\Delta T_B$ for 40 cm (K) | Retrieved (cm) |
|---|---|---|
| 0.00 | 3.533 | 26.5 |
| 0.25 | 3.003 | 22.5 |
| 0.50 | 2.473 | 18.5 |

A forest absorbs and re-emits the microwave signal, so forested snow reads as
*thin* snow — the same direction as saturation, and easily mistaken for it. The
honest report states the saturation limit and the forest fraction; a "snow depth
map" without them is not interpretable above a few tens of centimetres.

## 6. Glacier velocity by feature tracking

Two synthetic images ($128\times128$ pixels) separated by $30$ days, with a true
displacement of $(2, 3)$ pixels, are correlated. The recovery is exact —
$(2, 3)$ pixels — and with a pixel size of $10\ \mathrm{m}$,

$$
\lVert \mathbf{d} \rVert = \sqrt{2^{2}+3^{2}} = 3.606\ \text{px}
= 36.1\ \mathrm{m}, \qquad
v = \frac{36.1}{30}\times 365.25 = 439.0\ \mathrm{m\,yr^{-1}}.
$$

The uncertainty is set by pixel quantisation: $\pm 0.5$ pixel is

$$
\pm 0.5\times 10\ \mathrm{m} = \pm 5\ \mathrm{m} \quad\Rightarrow\quad
\pm 60.9\ \mathrm{m\,yr^{-1}},
$$

a $13.9\%$ uncertainty on the recovered speed. Two design lessons follow. The
measurement is *geometric and exact* for the displacement it finds, so its
accuracy is limited by the *image* (resolution, texture, registration), not by
spectroscopy. And a faster glacier, moving more pixels per interval, has a
smaller *relative* uncertainty — its resolution is better. Feature tracking is
therefore most reliable where the motion is large.

## 7. Seasonal signal against a secular trend

A subsidence series at $12$-day revisit over five years, with a seasonal thaw of
amplitude $5.00\ \mathrm{cm}$, a secular settlement of $1.0\ \mathrm{cm/yr}$ and
$0.73\ \mathrm{cm}$ measurement noise, has a measured half-range of
$7.70\ \mathrm{cm}$ and a total range of $15.41\ \mathrm{cm}$. The secular
signal ($1\ \mathrm{cm/yr}$, so $5\ \mathrm{cm}$ over the record) is *smaller
than the seasonal swing*, so a single displacement map cannot separate them. The
separation requires fitting a seasonal term and a trend simultaneously — the
same machinery as [17-07-04](../07-earth-observation-data/04-time-series-satellite.md).
Reporting "the ground dropped $8\ \mathrm{cm}$" from one map conflates thaw with
settlement; the honest statement separates the periodic and the secular parts.

## 8. Assumptions and regime of validity

1. **Snow albedo is broadband and Lambertian.** Real snow is forward-scattering
   and anisotropic; a nadir albedo is an approximation.
2. **Snow depth is below the saturation limit.** The retrieval is usable to a
   few tens of centimetres; beyond that it is a lower bound.
3. **The microwave signal is snow-only.** Forest, wet snow and liquid water all
   confound it; wet snow in particular destroys the signal.
4. **Feature tracking measures horizontal surface motion.** Vertical change,
   melt or a change of texture between images breaks the assumption of a rigid
   translation.
5. **The correlation peak is unique.** Repetitive patterns (crevasses, regular
   ridges) can produce a wrong peak.
6. **Subsidence noise is stationary.** A change in the radar or processing
   within the series creates a spurious step.

## 9. Worked example 2 — a snow-depth budget

A snowpack is reported at $60\ \mathrm{cm}$ from the microwave difference.
The saturation table says the signal for $60\ \mathrm{cm}$ is
$\Delta T_B = 6.0(1 - e^{-60/45}) = 4.42\ \mathrm{K}$, so the retrieval returns
$7.5 \times 4.42 = 33.2\ \mathrm{cm}$ — a bias of $-26.8\ \mathrm{cm}$. With a
forest fraction of $0.25$ the signal becomes $3.76\ \mathrm{K}$ and the retrieved
depth $28.2\ \mathrm{cm}$, a further bias of $-5.0\ \mathrm{cm}$. Two model
errors act in the same direction, and the honest report states a depth of "at
least $33\ \mathrm{cm}$" with the forest and saturation caveats, rather than a
point value it cannot support.

## Mastery checkpoint

Complete this without notes.

> Two images taken $24$ days apart show a surface displacement of $4$ pixels,
> with a pixel size of $15\ \mathrm{m}$. **(a)** Compute the speed in
> $\mathrm{m\,yr^{-1}}$. **(b)** Compute the $\pm1\sigma$-style uncertainty from
> $\pm 0.5$ pixel and express it as a percentage. **(c)** State the sign of the
> snow-depth bias introduced by saturation and by forest, and explain why the
> two are confusable. **(d)** A single displacement map shows an $8\ \mathrm{cm}$
> drop; state why it cannot be called permafrost settlement.

A worked version appears in the
[solutions](exercises/04-cryosphere-rs-solutions.md).

## Common pitfalls

1. **Reading a snow-depth map beyond the saturation limit.** It is a lower
   bound there.
2. **Ignoring forest.** Forested snow reads thin.
3. **Confusing grain growth with impurity.** One albedo cannot separate them.
4. **Quoting a velocity without its pixel uncertainty.** The floor is a fraction
   of a pixel.
5. **Trusting a correlation peak in a repeating texture.** It can be wrong by a
   full period.
6. **Calling a seasonal drop "settlement".** Separate the periodic from the
   secular.
7. **Assuming wet snow behaves like dry.** Liquid water destroys the microwave
   signal.

## Related modules

- [17-02-01 Multispectral Imaging, Band Ratios and Indices](../02-optical-and-thermal-remote-sensing/01-multispectral-imaging.md)
  — the optical indices behind snow and ice mapping.
- [17-03-02 InSAR](../03-radar-remote-sensing/02-insar.md) and
  [17-03-03 InSAR Time Series](../03-radar-remote-sensing/03-insar-time-series.md)
  — the precise displacement measurement used for subsidence.
- [17-07-04 Satellite Time Series and Trend Analysis](../07-earth-observation-data/04-time-series-satellite.md)
  — separating season from trend.
- [15-06-03 Ice-Sheet Marine Margins](../../15-oceanography-marine/06-sea-level-change-marine/03-ice-sheet-marine-margins.md)
  — why cryospheric change matters.

## Materials

- Demonstration: [`code/cryosphere_rs_demo.py`](code/cryosphere_rs_demo.py)
  — albedo, snow depth, feature-tracking velocity and subsidence.
- Exercises: [`exercises/04-cryosphere-rs-exercises.md`](exercises/04-cryosphere-rs-exercises.md)
  with [solutions](exercises/04-cryosphere-rs-solutions.md).
