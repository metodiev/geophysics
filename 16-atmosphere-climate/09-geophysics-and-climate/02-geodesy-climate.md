---
id: 16-09-02
title: "Geodesy for Sea Level, Ice Mass and Water Storage"
level: research
prereqs: ["07-05-05", "16-09-01", "21-01-06"]
tags: [atmosphere, climate, geodesy, sea-level, grace, vertical-land-motion, gia]
---

# Geodesy for Sea Level, Ice Mass and Water Storage

> **All models and data in this module are SYNTHETIC.** The budget components,
> vertical land motion, GIA correction and noise in `code/geodesy_climate_demo.py`
> are chosen teaching values in mm/yr. No real tide gauge, satellite mission,
> gravity solution, GIA model or published rate is used.

Geodesy supplies the climate discussion with its most policy-relevant number —
how fast the ocean surface is rising and where the water is coming from — and it
does so through a **budget**: a statement that the observed change equals the sum
of its components, within a stated uncertainty. The budget's logic is simple
arithmetic and its difficulty is entirely in the corrections:

$$\underbrace{\text{total sea-level change}}_{\text{altimetry, tide gauges}}
= \underbrace{\text{mass change}}_{\text{gravimetry, ice and land water}}
+ \underbrace{\text{steric change}}_{\text{ocean density, temperature and salinity}}.$$

Every term on the right is a measurement or a model, and each carries a
correction — glacial isostatic adjustment (GIA) for the gravity term, vertical
land motion for the gauges, reference-frame conventions for altimetry — whose
*uncertainty* enters the budget as directly as the data do. This lesson builds the
budget quantitatively and shows, with measured numbers, that the correction
uncertainties are not second-order: a $0.25\ \mathrm{mm\,yr^{-1}}$ uncertainty in
a GIA correction drove $8\%$ of the total budget variance in the demonstration,
and an unmeasured land motion of $1.50\ \mathrm{mm\,yr^{-1}}$ biased a gauge trend
by half the signal.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the sea-level budget and **state** which observable supplies each
   term.
2. **Compute** closure of a synthetic budget and **judge** closure against the
   stated uncertainty rather than against zero.
3. **Explain** why a tide gauge measures relative sea level, and **quantify** the
   bias an unmeasured vertical land motion produces.
4. **Explain** what a GIA correction is, how it enters the mass term, and how its
   uncertainty propagates into the budget.
5. **Compute** the record length required for a trend to exceed twice its standard
   error, and **explain** why the trend's standard error falls as $n^{-3/2}$.
6. **Distinguish** measured, corrected and assumed quantities in a geodetic
   climate product.
7. **Design** a validation that would test whether an apparent mass change is
   signal or correction artefact.

## Prerequisites

- [07-05-05 Applications: Groundwater Depletion, Ice Loss, Sea Level](../../07-gravity-geodesy/05-satellite-gravimetry/05-grace-applications.md) —
  the gravity products and their errors.
- [16-09-01 Seismic and Geodetic Monitoring of Cryosphere Change](01-seismic-monitoring-climate.md) —
  the seismic-side observable of the same ice.
- [12-06-01 Spatial and Directional Statistics in Earth Science](../../21-statistics-bayesian-ml/01-statistics-in-practice/06-spatial-statistics-geo.md) —
  spatial weighting, leakage and the statistics of gridded changes.

## 1. The budget, and what each term is

| Term | Measured by | Main correction |
|---|---|---|
| Total sea-surface height | satellite altimetry | reference frame, geocentre, instrument drift |
| Total local water level | tide gauges | vertical land motion |
| Mass (ice sheets, glaciers, land water) | satellite and repeat gravimetry | GIA, leakage and filtering |
| Steric (thermal + haline) | ocean temperature and salinity | the observation network's own bias |
| Terrestrial water storage | satellite gravimetry, wells | GIA, leakage, anthropogenic abstractions |

The budget is an equation, so a closure residual is informative only when compared
with its uncertainty. The demonstration builds a $30$-year synthetic planet with
a total trend of $3.30\ \mathrm{mm\,yr^{-1}}$, a mass component of
$1.90\ \mathrm{mm\,yr^{-1}}$, a steric component of $1.30\ \mathrm{mm\,yr^{-1}}$
(note $1.90+1.30 = 3.20 \ne 3.30$, so the synthetic budget has a built-in
$0.10\ \mathrm{mm\,yr^{-1}}$ defect), annual noise of $25\ \mathrm{mm}$ with AR(1)
persistence $\varphi = 0.70$, and fits each component by least squares:

| component | truth | fitted trend | standard error |
|---|---|---|---|
| total | 3.30 | 3.888 | 0.598 |
| mass | 1.90 | 1.721 | 0.353 |
| steric | 1.30 | 1.882 | 0.372 |

$$\text{residual} = 3.888 - 1.721 - 1.882 = +0.285\ \mathrm{mm\,yr^{-1}},
\qquad \sigma_{\text{residual}} = \sqrt{0.598^{2}+0.353^{2}+0.372^{2}}
= 0.788\ \mathrm{mm\,yr^{-1}},$$

so the residual is $+0.36\sigma$. **The budget closes**: the residual is small
relative to what the data can resolve, and the built-in defect is not detectable
at this noise level. The converse lesson is equally important — a budget with
$0.1\ \mathrm{mm\,yr^{-1}}$ of closure but an unstated uncertainty of
$0.8\ \mathrm{mm\,yr^{-1}}$ has not demonstrated anything about closure; it has
demonstrated that it cannot test it.

## 2. Tide gauges measure relative sea level

A tide gauge measures water level relative to **the land it stands on**. If the
land moves vertically, the record does too, and the vertical motion is a
tectonic, isostatic, sediment-compaction or groundwater-extraction signal, not a
sea-level signal. The demonstration gives the site a synthetic vertical land
motion of $-1.50\ \mathrm{mm\,yr^{-1}}$ (subsidence) and compares the
"absolute" series with the gauge series:

| quantity | trend (mm/yr) |
|---|---|
| absolute (satellite-like) | $+3.004 \pm 0.397$ |
| relative (tide gauge) | $+4.504 \pm 0.397$ |
| difference | $+1.500$ |

If the analyst assumes zero land motion, the gauge trend is wrong by
$1.50\ \mathrm{mm\,yr^{-1}}$, which is **$50\%$ of the absolute trend**. The
correction is not small and it is not optional: the land motion must be measured
(GNSS, absolute gravimetry, repeat levelling) or the gauge trend must be reported
as relative and labelled as such. This is why any sea-level trend from a single
gauge is a joint statement about the ocean and the coast.

## 3. Corrections are not measurements

The mass term requires a **GIA correction**: the solid Earth is still responding
to the removal of ice loads from earlier millennia, so the gravity field changes
for reasons unrelated to present-day mass loss. The correction is a *model*
output — a viscoelastic Earth model forced by a deglaciation history — and its
uncertainty is the model's uncertainty.

The demonstration applies a synthetic live GIA correction of
$+0.60\ \mathrm{mm\,yr^{-1}}$ to the mass component, with an assumed uncertainty
of $0.25\ \mathrm{mm\,yr^{-1}}$:

| quantity | value (mm/yr) |
|---|---|
| mass trend before correction | $+1.721 \pm 0.353$ |
| mass trend after correction | $+1.828 \pm 0.440$ |
| budget residual uncertainty incl. GIA term | $0.867$ |

The GIA uncertainty contributes $0.25^{2}/0.867^{2} = 8\%$ of the budget's
variance. Three structural points follow, and they generalise to every correction
in this field:

1. **A correction moves the answer by its size.** Here $+0.60\ \mathrm{mm\,yr^{-1}}$
   on the mass term is a $35\%$ change in it.
2. **A correction widens the uncertainty by at least its assumed error.** The
   post-correction uncertainty is larger than the pre-correction one.
3. **The assumed error is itself a choice.** A more confident GIA model produces a
   smaller quoted uncertainty without producing a better measurement; the budget's
   stated precision is therefore partly an assertion.

## 4. How long is long enough?

A trend is only as good as its standard error, and for a persistence-dominated
series that error falls fast. Simulating $200$ realisations per record length with
the demonstration's synthetic noise ($25\ \mathrm{mm}$ annual sd,
$\varphi = 0.70$) and a $3.30\ \mathrm{mm\,yr^{-1}}$ trend:

| $n$ (yr) | mean SE of trend (mm/yr) | trend/SE | detectable at $2\sigma$? |
|---|---|---|---|
| 10 | 1.734 | 1.90 | no |
| 15 | 1.047 | 3.15 | yes |
| 20 | 0.739 | 4.46 | yes |
| 25 | 0.559 | 5.90 | yes |
| 30 | 0.434 | 7.61 | yes |
| 60 | 0.170 | 19.44 | yes |

Two readings. First, **a decade is not a climate record for this variable**: at
$n = 10$ the trend is only $1.9$ times its own standard error and establishes
nothing, while by $15$ years it exceeds three. Second, the standard error falls
roughly as $n^{-3/2}$ (from $10$ to $30$ years it falls by a factor $4.0$, close
to $3^{1.5} = 5.2$), much faster than the $1/\sqrt{n}$ of a mean, because a trend
is estimated from the *shape* of the series over time rather than from its
average. Lengthening a record therefore buys trend precision unusually quickly —
which is why the century-scale tide-gauge records matter so much.

## 5. Separating ice, land water and ocean

The mass term lumps together ice-sheet loss, glacier loss and terrestrial water
storage change, and separating them is a modelling exercise, not a measurement:

- **Spatial patterns differ.** Ice-mass change is concentrated at ice-sheet
  margins; groundwater depletion is concentrated over managed aquifers. A gravity
  solution's spatial resolution, its filtering and its **leakage** between regions
  determine whether the separation is possible at all (see
  [07-05-04 Mass Concentration Solutions, Leakage and Filtering](../../07-gravity-geodesy/05-satellite-gravimetry/04-mascons-and-leakage.md)).
- **GIA is regional.** Two regions with the same present-day mass change but
  different deglaciation histories need different corrections.
- **The ocean floor is not measured.** Steric change is inferred from temperature
  and salinity observations whose coverage is uneven, so its uncertainty is
  largest where the observations are sparse — typically the same places where the
  budget residual is largest.

The honest form of a separation statement is conditional: *"given the GIA model,
the leakage correction and the filtering, the ice contribution is $X$ and the
terrestrial-water contribution is $Y$; the alternative partitioning permitted by
the model spread is $Z$."*

## 6. Assumptions and regime of validity

1. **Linearity.** The budget is written as a sum of independent terms; a
   non-linear interaction (for example, meltwater changing the steric term) breaks
   the additivity silently.
2. **The corrections are correct up to their stated uncertainty.** GIA and land
   motion are the dominant systematic terms, and both are modelled or measured
   with independent error.
3. **No unmodelled trend in the observing system.** Altimeter drift, gauge
   datum changes and changes in the gravity mission's processing all enter as
   spurious trends.
4. **The record is long enough for the noise model.** The standard errors quoted
   are only as good as the assumed persistence; a record containing one large
   volcanic or ENSO event has an effective sample size far below its length.
5. **The regions are separable.** Leakage between adjacent mass-change regions is
   a modelling choice, and its uncertainty is usually the largest term in a
   regional attribution.
6. **The reference frame is stable and stated.** A sea-level rate is meaningless
   without the frame it is measured in.

## 7. Python demonstration

[`code/geodesy_climate_demo.py`](code/geodesy_climate_demo.py) builds the
synthetic budget and runs the analysis, printing labelled results in mm/yr. It:

1. constructs the total, mass and steric series with stated truths and noise, and
   measures the closure residual against its uncertainty;
2. compares an absolute series with a tide-gauge series affected by synthetic land
   motion and measures the bias;
3. applies a GIA correction and propagates its uncertainty into the budget;
4. measures the record length required for the trend to exceed twice its standard
   error;
5. states what is measured, corrected and assumed.

Every number in this lesson is printed by that demonstration.

## Mastery checkpoint

> The demonstration's synthetic planet has a total trend of
> $3.30\ \mathrm{mm\,yr^{-1}}$, a mass component of $1.90$ and a steric component
> of $1.30$, with a built-in $0.10\ \mathrm{mm\,yr^{-1}}$ budget defect, and a
> synthetic GIA correction of $+0.60\ \mathrm{mm\,yr^{-1}}$.
>
> **(a)** Write the budget equation and identify which term each observable
> supplies.
> **(b)** The fitted components give a residual of $+0.285\
> \mathrm{mm\,yr^{-1}}$ with $\sigma = 0.788\ \mathrm{mm\,yr^{-1}}$. Decide
> whether the budget closes, and explain your criterion in one sentence.
> **(c)** A gauge sits on land subsiding at $-1.50\ \mathrm{mm\,yr^{-1}}$ and the
> analyst assumes zero land motion. Compute the error in the gauge trend and
> express it as a fraction of the $3.00\ \mathrm{mm\,yr^{-1}}$ absolute trend.
> **(d)** The GIA correction is $+0.60$ with an assumed uncertainty of
> $0.25\ \mathrm{mm\,yr^{-1}}$. Compute its contribution to the budget variance
> and explain why a smaller assumed uncertainty would not improve the measurement.
> **(e)** From the table, state the shortest record in which a
> $3.30\ \mathrm{mm\,yr^{-1}}$ trend exceeds twice its standard error, and explain
> why the trend's standard error falls as $n^{-3/2}$.

## Common pitfalls

1. **Judging closure against zero.** The residual is judged against its
   uncertainty ($+0.36\sigma$ here).
2. **Calling a tide-gauge trend a sea-level trend.** It is relative to the land.
3. **Treating a correction as a measurement.** GIA and land motion are model or
   measurement with their own errors.
4. **Forgetting to widen the uncertainty after a correction.** The post-correction
   interval is wider, not narrower.
5. **Quoting a gravity-based regional attribution without its leakage and GIA
   uncertainty.** Those are frequently the largest terms.
6. **Reporting a trend from a decade of data.** At $n = 10$ the ratio was $1.90$.
7. **Assuming a shorter record suffices because the trend is "large".** The
   standard error, not the trend, decides.

## Related modules

- [16-09-01 Seismic and Geodetic Monitoring of Cryosphere Change](01-seismic-monitoring-climate.md) —
  the seismic state variable that complements the mass constraint.
- [16-09-05 Climate–Geohazard Interactions (Sea Level, Permafrost, Slopes)](05-climate-geohazards.md) —
  where a sea-level trend becomes a coastal hazard.
- [16-09-03 Borehole Temperature Records of Past Climate](03-geothermal-climate-records.md) —
  the thermal history of the same land surface.
- [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md) —
  the gravity products and error models behind the mass term.
- [12-06 Geodesy Constraints on the Interior](../../12-global-geophysics-interior/06-geodesy-constraints-interior/README.md) —
  reference frames, the geocentre and the rotation terms.
- [16-08-03 Homogenisation, Bias Adjustment and Uncertainty](../08-climate-observation-and-data/03-climate-data-homogenisation.md) —
  the same discipline of separating an observing-system change from a signal.

## Self-assessment checklist

- [ ] I can write the budget and name the observable behind each term.
- [ ] I can compute a closure residual and compare it with its uncertainty.
- [ ] I can explain and quantify the tide-gauge land-motion bias.
- [ ] I can propagate a GIA correction uncertainty into a budget.
- [ ] I can compute a trend's standard error and the record length it requires.
- [ ] I can distinguish measured, corrected and assumed in a geodetic product.
