---
id: 14-02-01
title: "ERT for Aquifer Characterisation and Salinity Mapping"
level: graduate
prereqs: ["14-01-05", "14-01-02", "09-02-03"]
tags: [hydrogeophysics, ert, resistivity, salinity, archie, inversion]
---

# ERT for Aquifer Characterisation and Salinity Mapping

Electrical resistivity tomography is the standard tool for mapping salinity,
locating the water table in coarse sediments, and imaging the geometry of
conductive clay layers. Its appeal is that it measures a property the pore water
controls almost entirely, so the physical link from the measurement to the
hydrology is short. Its difficulty is that "almost entirely" is doing a lot of
work: the same bulk resistivity comes from salinity, porosity, clay content, and
saturation, and the DC inverse problem has a large near-null space, so a range of
models fits any dataset.

This lesson fixes the forward model, measures how well a sounding resolves depth,
and then chases the ambiguity in both directions — through the inverse problem
(what a sounding can and cannot determine) and through Archie's law (what a
resistivity means for salinity). The tools it needs — electrode arrays, geometric
factors, apparent resistivity, inversion — are derived in
[09-02 DC Resistivity](../../09-electrical-em-methods/02-dc-resistivity/README.md);
this lesson assumes them and concentrates on the hydrological interpretation.

**All models and data in this module are SYNTHETIC.** The site, its resistivities,
its salinities and the survey geometry are invented teaching values, and the
"measured" curve is the analytic response plus a stated noise level. No real site
or field dataset is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the apparent resistivity of a Wenner array over a two-layer earth
   and **verify** the forward model against its analytic limits.
2. **Measure** how well a sounding resolves the depth and resistivity of a second
   layer, and **explain** why resolution depends on the resistivity contrast rather
   than on array length alone.
3. **Invert** a noisy synthetic sounding and **report** the admitted range of
   models rather than a single answer.
4. **Convert** a bulk resistivity to a salinity through Archie's law and **quantify**
   the porosity ambiguity.
5. **Compute** the time-lapse response to a salinity change and **state** the three
   other changes that produce the same difference.
6. **Design** an ERT survey for a stated hydrological target, including the array,
   the spacing range and the tie to borehole control.

## Prerequisites

- [14-01-05 Groundwater Chemistry and Salinity](../01-hydrology-fundamentals/05-groundwater-chemistry.md)
  — TDS, chloride, seawater fraction and the water-conductivity calibration.
- [14-01-02 Aquifers, Porosity, Permeability and Storativity](../01-hydrology-fundamentals/02-aquifer-types-and-properties.md)
  — porosity and formation factor.
- [09-02-03 Apparent Resistivity](../../09-electrical-em-methods/02-dc-resistivity/03-apparent-resistivity.md)
  — the geometric factor and the definition of apparent resistivity.

---

## 1. Why resistivity sees water

A current flows through a saturated rock along the **pore water** and, where clay
coatings exist, along the **grain surfaces**. In a clean sand with fresh water the
first path dominates and Archie's law applies:

$$\rho_{\text{bulk}} = \frac{a\,\rho_w}{\phi^{m}S_w^{n}},$$

with $a \approx 1$, $m \approx 2$ (the cementation exponent) and $n \approx 2$ (the
saturation exponent). The consequences for hydrogeology are large:

- **Salinity dominates where the pore water is saline.** A seawater intrusion
  drops the bulk resistivity by one to two orders of magnitude, far more than any
  porosity change can, which is why ERT maps intrusion fronts so effectively.
- **Porosity matters as much as salinity for fresh water.** $\rho_b \propto \phi^{-2}$
  means a porosity change from 0.25 to 0.40 changes the resistivity by a factor of
  2.6 *at constant salinity*. In fresh-water settings this is usually the dominant
  ambiguity.
- **Clay breaks Archie.** Surface conduction adds a parallel path that lowers the
  resistivity at low salinity, so a clay-rich fresh-water unit can look like a
  clean brackish one.

## 2. The forward model used here

For a **Wenner array** (electrodes AMNB at equal spacing $a$) over two layers,
with layer 1 of resistivity $\rho_1$ above depth $h$ and a half-space $\rho_2$
below, the apparent resistivity is the exact series

$$\rho_a(a) = \rho_1\left[1 + 4\sum_{n=1}^{\infty}k^{n}
\left(\frac{1}{\sqrt{1 + (2nh/a)^{2}}}
- \frac{1}{\sqrt{4 + (2nh/a)^{2}}}\right)\right],
\qquad k = \frac{\rho_2 - \rho_1}{\rho_2 + \rho_1}.$$

Two limits must hold and the demonstration checks both:

- **$\rho_2 = \rho_1$** ($k = 0$): the series vanishes and
  $\rho_a = \rho_1$ exactly (measured: $120.000000\ \Omega$ m against
  $\rho_1 = 120$).
- **$h \to 0$**: the array sits on the half-space, and $\rho_a \to \rho_2$
  (measured: $5.0000\ \Omega$ m against $\rho_2 = 5$).

The series converges geometrically with ratio $\lvert k\rvert$; for the
synthetic contrast $\lvert k\rvert = 0.920$ and 400 terms give an error below
$10^{-12}\ \Omega$ m (verified against a 4000-term reference).

**Synthetic site** — an unsaturated sand over a saline aquifer, a typical coastal
intrusion geometry: $\rho_1 = 120\ \Omega$ m, $\rho_2 = 5\ \Omega$ m, $h = 8$ m:

| $a$ (m) | $\rho_a$ ($\Omega$ m) | $\rho_a/\rho_1$ |
|---|---|---|
| 2 | 118.90 | 0.991 |
| 4 | 112.53 | 0.938 |
| 8 | 84.63 | 0.705 |
| 12 | 54.49 | 0.454 |
| 16 | 33.12 | 0.276 |
| 24 | 13.27 | 0.111 |
| 32 | 7.50 | 0.063 |
| 40 | 5.88 | 0.049 |

The transition is centred near $a \approx 2h = 16$ m, where $\rho_a$ has fallen to
about $28\%$ of $\rho_1$. That is the working rule for choosing spacings: **spread
the array over roughly $0.25h$ to $5h$** to bracket the transition, and remember
that a Wenner spacing $a$ does not sample "depth $a/2$" — it samples a
sensitivity kernel centred near $a/2$ but extending much deeper.

## 3. What a sounding resolves, measured

For the strong contrast above, the demonstration scans trial depths and, at each,
finds the second-layer resistivity that best fits the synthetic curve:

| trial $h$ (m) | best $\rho_2$ ($\Omega$ m) | rms misfit |
|---|---|---|
| 4.0 | 7.89 | 44.6% |
| 6.0 | 6.92 | 24.4% |
| 7.0 | 6.09 | 12.5% |
| **8.0** | **5.00** | **0.00%** |
| 9.0 | 3.63 | 12.9% |
| 10.0 | 1.98 | 25.8% |
| 12.0 | 0.50 | 57.1% |
| 14.0 | 0.50 | 105.3% |

The misfit surface has a sharp minimum: a one-metre depth error already costs
12.5%, so this target is well resolved. Now repeat with a **weak contrast**
($\rho_1 = 50$, $\rho_2 = 20\ \Omega$ m, $k = -0.43$, same $h = 8$ m):

| trial $h$ (m) | best $\rho_2$ ($\Omega$ m) | rms misfit |
|---|---|---|
| 4.0 | 24.42 | 13.0% |
| 6.0 | 22.25 | 6.1% |
| 7.0 | 21.13 | 2.9% |
| **8.0** | **20.00** | **0.00%** |
| 9.0 | 18.85 | 2.7% |
| 10.0 | 17.68 | 5.1% |
| 12.0 | 15.26 | 9.4% |
| 14.0 | 12.71 | 13.0% |

At a 5% misfit threshold the weak-contrast sounding admits depths from 7 to 9 m
and resistivities from 21.1 to 18.9 — the depth is known only to about $\pm13\%$,
and only that well because the resistivity adjusts to compensate. **The deepest
lesson is that resolution is a function of contrast, not of array length.** A
saline layer against a resistive sand is a favourable ERT target; a
clay-versus-sand contrast of a factor of two is not, no matter how many electrodes
are deployed.

### 3.1 The inversion of a noisy curve

With 5% noise on eight spacings, a two-parameter least-squares fit (fixing
$\rho_1 = 120\ \Omega$ m) recovers $\rho_2 = 5.50\ \Omega$ m ($+10.0\%$) and
$h = 7.83$ m ($-2.1\%$), with an rms residual of 4.47% — consistent with the
injected noise, so the model is not being strained. The 10% error in $\rho_2$ is
the price of eight data points and a strong trade-off between $\rho_2$ and $h$:
the layer's influence is governed largely by its **conductance**, so a slightly
deeper and slightly less conductive layer fits almost as well.

**Reporting rule.** A conductivity model from ERT should be presented with (i) the
data error, (ii) the rms residual of the fit, and (iii) the admitted range of the
parameters, obtained by repeating the inversion from different starting models or
by profiling the misfit. A single number without (iii) is not a measurement.

## 4. From resistivity to salinity, and the porosity ambiguity

With the synthetic calibration $\sigma_w = 0.15 \times \mathrm{TDS}$ [g L$^{-1}$]
S m$^{-1}$ from
[14-01-05](../01-hydrology-fundamentals/05-groundwater-chemistry.md), a measured
$\rho_{\text{bulk}} = 40\ \Omega$ m inverts through Archie
($a = 1$, $m = 2$, $S_w = 1$) to:

| $\phi$ | $\rho_w$ ($\Omega$ m) | $\sigma_w$ (S m$^{-1}$) | TDS (mg L$^{-1}$) |
|---|---|---|---|
| 0.22 | 1.94 | 0.517 | 3444 |
| 0.25 | 2.50 | 0.400 | 2667 |
| 0.30 | 3.60 | 0.278 | 1852 |
| 0.35 | 4.90 | 0.204 | 1361 |
| 0.40 | 6.40 | 0.156 | 1042 |

**A factor of 1.8 in porosity spans a factor of 3.3 in inferred TDS** — from
drinking-water quality to unusable. The measurement alone cannot choose between a
tight formation with brackish water and a porous one with fresh water. Two
independent constraints are needed, and each is a standard part of a
hydrogeophysical survey:

1. **A porosity constraint** — a density, neutron or NMR log in a borehole on the
   profile (see [07 Borehole Geophysics](07-borehole-hydrogeophysics.md)), or an
   independent porosity from the seismic velocity
   ([03 Seismic Methods for Aquifer Geometry](03-seismic-hydrogeophysics.md)).
2. **A water sample** — which fixes the salinity directly and therefore calibrates
   the TDS–conductivity relation at that site.

With both, the inversion becomes a calibration problem instead of an ambiguity.
With neither, the honest statement is a *joint* constraint: "the product
$\phi^{2}\mathrm{TDS}$ is known to 10%".

## 5. Time-lapse, and what else changes the resistivity

A time-lapse difference is the most powerful use of ERT in hydrogeology, because
static heterogeneity cancels. With a synthetic baseline of $\phi = 0.28$ and
$\text{TDS} = 1000\ \mathrm{mg\,L^{-1}}$ in the aquifer:

| TDS (mg L$^{-1}$) | $\rho_w$ ($\Omega$ m) | $\rho_{\text{bulk}}$ ($\Omega$ m) | change |
|---|---|---|---|
| 1000 | 6.67 | 85.0 | – |
| 1100 | 6.06 | 77.3 | $-9.1\%$ |
| 1500 | 4.44 | 56.7 | $-33.3\%$ |
| 2000 | 3.33 | 42.5 | $-50.0\%$ |

A 10% salinity rise is a 9% resistivity drop: trivial to resolve against a
repeatability of 2–3%. The price is that **four different things** produce the same
difference, and a time-lapse survey without a control for them is uninterpretable:

1. **Salinity change** — the target.
2. **Saturation change** — a falling water table lowers $\rho_{\text{bulk}}$
   through $S_w^{-n}$; over a 1 m water-table change this can exceed the salinity
   signal.
3. **Temperature change** — water conductivity rises about 2% per $^\circ$C, so a
   5 $^\circ$C seasonal swing is a 10% signal on its own.
4. **Electrode and contact changes** — a shift in contact resistance or a
   re-positioned electrode mimics a subsurface change; reciprocal and repeat
   measurements expose it.

The control for (1)–(3) is a nest of piezometers with a logger: water level,
temperature and a chloride sample at each survey. That is why the standard
intrusion monitoring design is **ERT plus piezometers**, not ERT alone.

## 6. Python demonstration

`code/ert_for_hydrology_demo.py` prints all of the above with units. It:

1. computes the Wenner two-layer response over eight spacings and checks the
   $\rho_2 = \rho_1$, $h \to 0$ and $a \to 0$ limits;
2. scans trial depths for a strong and a weak contrast and reports the admitted
   depth band at a 5% misfit threshold;
3. inverts a 5%-noise synthetic sounding with `scipy.optimize.least_squares`,
   recovering $\rho_2 = 5.50\ \Omega$ m and $h = 7.83$ m with an rms residual of
   4.47%;
4. inverts a bulk resistivity to TDS over five porosities;
5. tabulates the time-lapse response to four salinities;
6. verifies the series truncation error against a 4000-term reference.

```bash
cd 14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ert_for_hydrology_demo.py
```

## 7. Assumptions and regime of validity

1. **The forward model is 1-D and two-layer.** Real aquifers are 3-D; a 1-D
   interpretation of a 2-D dataset introduces error that is largest where the
   layer dips or terminates. A dipping interface is a classic cause of an
   apparent depth that moves with array orientation.
2. **Isotropic resistivity.** Anisotropy of a layered sequence appears as a
   directional dependence; in ERT it can mimic a dipping layer.
3. **Archie's law applies** — clean granular rock, no clay, no metallic minerals,
   $S_w$ well above the percolation threshold. Clay-bearing units need a shaly-sand
   model (see [09-01-04 Clay and Surface Conduction](../../09-electrical-em-methods/01-electrical-properties-of-earth/04-clay-and-surface-conduction.md)).
4. **The array is not in a strong lateral contrast.** Electrodes near a
   road, a building foundation or a buried service see an anomalous field.
5. **Temperature is known.** A 2% per $^\circ$C dependence on water conductivity is
   comparable with the signals of interest.
6. **The noise model is correct.** ERT errors are better described by a
   proportional-plus-absolute model with reciprocal-error treatment than by a
   constant percentage; using the wrong model biases the inversion's apparent
   resolution.
7. **$a$ is not read as depth.** The spacing sets a sensitivity kernel's shape, not
   a depth; the median depth of investigation for a Wenner array is roughly
   $0.5a$ only under specific conditions, and it is a *sensitivity-weighted*
   quantity, not a resolution limit (see
   [09-02-04 Sounding and Profiling](../../09-electrical-em-methods/02-dc-resistivity/04-sounding-profiling.md)).

## Mastery checkpoint

A synthetic coastal profile has an unsaturated sand of $150\ \Omega$ m over a
saline aquifer of $4\ \Omega$ m at 12 m depth. A Wenner survey used spacings of 1,
2, 4, 8, 16 and 32 m.

**(a)** Estimate, from the rule of thumb, at which spacing the transition will be
centred, and state why the estimate is only approximate. **(b)** A colleague
reports the salinity from a bulk resistivity of $35\ \Omega$ m at 15 m depth as
"$2500\ \mathrm{mg\,L^{-1}}$ TDS" with $\phi = 0.30$. Compute what TDS the same
resistivity implies at $\phi = 0.25$ and 0.35, and state the honest way to report
the result. **(c)** A time-lapse survey shows the resistivity at 15 m falling by
8% between two seasons. List the four candidate causes and state the measurement
that discriminates each. **(d)** You have budget for one borehole: what would you
log in it and why?

## Common pitfalls

1. **Reading depth from spacing.** Sensitivity kernels overlap; the same $a$ samples
   a range of depths.
2. **Reporting a single salinity from a resistivity.** Porosity and clay change the
   answer by a factor of three or more.
3. **Interpreting a low resistivity as salinity without a clay check.** Surface
   conduction does the same thing.
4. **Assuming a strong contrast is hard to resolve.** It is the weak contrasts and
   the thin layers that are ambiguous, as the depth scan shows.
5. **Ignoring temperature.** 2% per $^\circ$C is the same order as an annual
   intrusion signal.
6. **Comparing two surveys with different electrode positions or acquisition.**
   The difference then includes the geometry change.
7. **Using a single-layer interpretation for a target that dips.** A dipping
   interface produces an apparent depth change with orientation.

## Related modules

- [09-02 DC Resistivity and ERT](../../09-electrical-em-methods/02-dc-resistivity/README.md) —
  arrays, geometric factors, forward modelling and inversion.
- [09-01-02 Archie's Law](../../09-electrical-em-methods/01-electrical-properties-of-earth/02-archies-law.md) —
  the law inverted in §4, with its own degeneracy analysis.
- [14-01-05 Groundwater Chemistry and Salinity](../01-hydrology-fundamentals/05-groundwater-chemistry.md) —
  where the TDS–conductivity calibration comes from.
- [02 EM and TDEM for Groundwater Exploration](02-em-for-hydrology.md) — the
  induction-based alternative, better where the target is deep or the surface is
  insulating.
- [05 Time-Lapse and Monitoring Hydrogeophysics](../05-hydrogeophysical-monitoring/README.md) —
  the full time-lapse design problem.
- [04 Contaminant and Environmental Geophysics](../04-contaminant-and-environmental/README.md) —
  intrusion and leachate applications.

## Code and exercises

- Demonstration: [`code/ert_for_hydrology_demo.py`](code/ert_for_hydrology_demo.py)
- Exercises: [`exercises/01-ert-for-hydrology-exercises.md`](exercises/01-ert-for-hydrology-exercises.md)
- Worked solutions: [`exercises/01-ert-for-hydrology-solutions.md`](exercises/01-ert-for-hydrology-solutions.md)
