---
id: 15-06-01
title: "Palaeo Sea Level Reconstruction from Marine Records"
level: research
prereqs: ["15-03-04", "15-02-04", "07-06-04", "16-06-01"]
tags: [oceanography, marine-geophysics, sea-level-change, palaeoclimate, isotopes]
---

# Palaeo Sea Level Reconstruction from Marine Records

> **All models and data in this module are SYNTHETIC.** The isotope model, the
> records and the age models are teaching models with the stated model constants.
> No real core, site, terrace, speleothem or published record is referenced, and no
> number is quoted from a published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the carbonate δ¹⁸O signal as the sum of an ice-volume term and a
   temperature term, with both coefficients stated and justified in magnitude.
2. **Demonstrate** that one isotope value cannot give a sea level, and **compute**
   the sea-level error per kelvin of temperature error.
3. **Compute** an ice-volume equivalent sea level from an ice volume, and the
   Gt-per-millimetre conversion used in the modern budget.
4. **Propagate** an age-model error into a sea-level rate and **show** that the
   chronology, not the depth measurement, limits the rate.
5. **Quantify** the glacial-isostatic-adjustment correction and its error, and
   **state** why a local sea level is not a eustatic one.
6. **Distinguish** measured quantities (isotope ratios, radiometric ages, depths)
   from modelled ones (temperature, sea level, ice volume, GIA) in a published
   sea-level curve.
7. **State** the two independent measurements that would break the isotope
   non-uniqueness, and why one of them is still not enough on its own.

## Prerequisites

- [15-03-04 Fracture Zones, Transform Faults and Oceanic Anomalies](../03-seafloor-tectonics/04-fracture-zones.md) —
  the age framework and magnetic timescale of marine records.
- [15-02-04 Sub-Bottom Profiling and Chirp Systems](../02-marine-geophysics-methods/04-sub-bottom-profiling.md) —
  the stratigraphic imaging that locates the horizons.
- [07-06-04 Post-Glacial Rebound](../../07-gravity-geodesy/06-earth-tides-and-rotation/04-post-glacial-rebound.md) —
  the glacial-isostatic adjustment that has to be removed.
- [16-06-01 Palaeoclimate Proxies](../../16-atmosphere-climate/06-palaeoclimate/01-paleoclimate-proxies.md) —
  the general proxy framework.

## 1. Intuition: an isotope ratio that measures two things at once

The oxygen-isotope ratio in foraminiferal calcite is the workhorse proxy for
palaeo sea level, and it works because two processes load the same signal onto it.
When ice sheets grow, the ocean's remaining water becomes isotopically heavier,
and the calcite that forms from it is heavier by a proportional amount. When the
water cools, the fractionation between water and calcite changes, and the calcite
becomes heavier again. Both effects push δ¹⁸O in the same direction during a
glacial, and they are **not separable in a single measurement**.

That single sentence contains everything that makes this subject difficult. The
conversion of δ¹⁸O to sea level requires a temperature, the temperature has its own
error, and the sea-level sensitivity to that error is **22 m per kelvin** in the
model here — larger than most of the changes being studied. Every published
δ¹⁸O-based sea-level curve is therefore accompanied by an independent temperature
estimate, and every honest statement of the result carries both uncertainties.

Two more terms must be removed before a *local* sea-level record becomes a
*eustatic* one: the age model (a rate is a difference over time, and time comes
from radiometric dating with its own error) and the glacial-isostatic adjustment
(the solid Earth and the geoid both respond to the ice and water loads, by tens of
metres near former ice sheets). Both are models, and both are large.

## 2. Precise definitions

**δ¹⁸O**: the per-mil deviation of the ¹⁸O/¹⁶O ratio of a sample from a standard,
$\delta^{18}\mathrm{O}=10^{3}(R_{\text{sample}}/R_{\text{standard}}-1)$.

**Ice-volume effect**: the change in the ocean's δ¹⁸O caused by the preferential
removal of ¹⁶O into ice, quantified here by an ice-volume coefficient in
‰ per metre of sea level.

**Vital effect and fractionation slope**: the temperature dependence of the
calcite–water fractionation, a model coefficient of the order of
$0.2\ \text{‰}\,^\circ\mathrm{C}^{-1}$.

**Ice-volume equivalent sea level (ESL)**: the global mean sea-level change
produced by a given mass of ice, ignoring all redistribution.

**GIA (glacial isostatic adjustment)**: the viscoelastic and gravitational response
of the Earth to changes in ice and water loads, which moves both the land and the
geoid.

**Age model**: the mapping from depth in a core to age, built from dated horizons
and an assumption about accumulation between them.

## 3. Derivations and measurements

### 3.1 The forward isotope model

Write the carbonate signal as

$$\delta^{18}\mathrm{O}_{\text{carb}}
=\underbrace{\delta^{18}\mathrm{O}_{\text{sw}}}_{\text{ice volume}}
+\underbrace{0.22\,(T_0-T)}_{\text{temperature}},\qquad
\delta^{18}\mathrm{O}_{\text{sw}}=\delta_0-0.010\,SL_m ,$$

with $T_0=15\ ^\circ\mathrm{C}$ a reference temperature. Both coefficients are
model values of the standard magnitude: $0.010\ \text{‰}\,\mathrm{m}^{-1}$ means
that 100 m of sea-level fall raises the ocean's δ¹⁸O by 1‰, and
$0.22\ \text{‰}\,\mathrm{K}^{-1}$ is the calcite–water fractionation slope. The
demonstration's forward table:

| $SL$ (m) | $T$ (°C) | δ¹⁸O_sw | δ¹⁸O_carb (‰) |
|---|---|---|---|
| 0 | 15 | 0.000 | 0.000 |
| −40 | 13 | 0.400 | 0.840 |
| −80 | 10 | 0.800 | 1.900 |
| −120 | 8 | 1.200 | 2.740 |
| −120 | 12 | 1.200 | 1.860 |

The last two rows are the whole problem: **the same 120 m of sea-level fall
produces 2.740‰ or 1.860‰ depending only on the temperature**.

### 3.2 The inversion and its non-uniqueness

Solving for sea level at an assumed temperature,

$$SL_m=\frac{\delta^{18}\mathrm{O}_{\text{carb}}-0.22(T_0-T)}{0.010} .$$

For a measured 1.60‰:

| assumed $T$ (°C) | implied $SL$ (m) |
|---|---|
| 15 | −160 |
| 14 | −138 |
| 13 | −116 |
| 12 | −94 |
| 10 | −50 |
| 8 | −6 |

$$\frac{\mathrm{d}(SL)}{\mathrm{d}T}=-\frac{0.22}{0.010}=-22\
\mathrm{m\,K^{-1}} .$$

**A 1 K temperature error is a 22 m sea-level error.** That number is the reason
this lesson exists: the proxy's sensitivity to the quantity nobody measures is an
order of magnitude larger than the palaeoceanographic signals (a few metres to
tens of metres per millennium) that the records are used to resolve.

Note also what the table's extremes show: because the temperature and ice-volume
terms have similar magnitudes, a 7 K uncertainty in temperature moves the inferred
sea level over **150 m**. The inversion is only meaningful when the temperature is
independently constrained, and even then it is the *correlation* between the
temperature error and the age model that dominates the final uncertainty.

### 3.3 Ice-volume equivalent sea level

For an ice volume $V$ melted into the ocean,

$$SL=\frac{\rho_{\text{ice}}V}{\rho_{\text{sw}}A_{\text{ocean}}}
=\frac{917}{1025\times3.61\times10^{14}}V=2.478\times10^{-15}\,V ,$$

so $1\times10^{15}\ \mathrm{m^3}$ of ice is 2.48 m of global sea level and
$20\times10^{15}\ \mathrm{m^3}$ is 49.56 m. In mass terms, one millimetre of
global mean sea level is

$$1\ \mathrm{mm}=\rho_wA_{\text{ocean}}\times10^{-3}
=1000\times3.61\times10^{14}\times10^{-3}=3.61\times10^{14}\ \mathrm{kg}
=361\ \mathrm{Gt},$$

the standard conversion of the modern sea-level budget. **These are the two
numbers that connect an ice volume to a sea level, and both are exact given the
constants** — the model content is entirely in the ice volume itself, which is
always a reconstruction.

### 3.4 Chronology

A rate is a difference over a time interval, so

$$\text{rate}=\frac{\Delta h}{\Delta t},\qquad
\frac{\sigma_{\text{rate}}}{\text{rate}}=\frac{\sigma_{\Delta t}}{\Delta t} .$$

For a 60 m rise between horizons dated at 20 and 10 ka, the rate is 6.00 mm/yr;
with ±1 ka on each age, $\sigma_{\Delta t}=\sqrt2$ ka = 1.41 ka, giving

$$\sigma_{\text{rate}}=6.00\times\frac{1.41}{10}=0.85\ \mathrm{mm\,yr^{-1}}
\quad(14\%).$$

**The chronology, not the depth measurement, limits the rate.** The
demonstration's table (10, 9, 9, 8 ka durations for the same 60 m) shows the rate
ranging from 6.00 to 7.50 mm/yr for age assignments that are all within the dating
error — a 25% spread produced entirely by the age model.

### 3.5 The GIA correction

GIA changes both the land surface and the geoid, and its size depends entirely on
location:

| site character | model GIA correction | fraction of a 120 m signal |
|---|---|---|
| near a former ice sheet | 80 m | 67% |
| intermediate | 20 m | 17% |
| far field, stable | 5 m | 4% |

The consequences are worth stating plainly. **A local sea-level record is not a
eustatic one** until the GIA term is removed. Near a former ice sheet the
correction is two-thirds of the signal, so an error of 10% *of the correction* is
an 8 m error in the answer — larger than the millennial-scale changes the record is
being used to resolve. And the correction depends on a viscoelastic Earth model,
a deglaciation history and a sea-level equation: three models, none of which the
record itself constrains.

## 4. Physical interpretation

- **The proxy measures a sum.** Ice volume and temperature; the sum is measured,
  the parts are modelled.
- **The sensitivity is asymmetric.** 1 K of temperature error is 22 m of sea
  level, while 1 m of sea level is 0.01‰ of isotope — a signal far below the
  analytical precision. The reconstruction is limited at the *temperature* end.
- **The two coefficients are calibration constants.** They come from laboratory
  fractionation work and from records where an independent sea level exists, so
  they carry that record's assumptions into every subsequent reconstruction.
- **Time is as uncertain as state.** A 14% rate uncertainty from ±1 ka ages, on a
  record whose depth resolution is centimetres, is a statement about geochronology.
- **The local-to-eustatic step is a model step.** It is where most published
  disagreements between sea-level curves come from, and it is unavoidable.
- **Ice-volume reconstructions inherit the same structure**: an ice volume is
  inferred from a sea level (or from a GIA-corrected one), so the ESL conversion
  is arithmetic on a model output, not a measurement of ice.

## 5. Assumptions and regime of validity

1. **A two-term isotope model.** Species-dependent vital effects, salinity
   effects, diagenesis and changes in the isotopic composition of the source water
   are ignored; each is a known complication.
2. **Constant calibration coefficients.** The ice-volume coefficient depends on the
   isotopic composition of the ice sheets, which varied; the fractionation slope is
   linearised.
3. **A single temperature proxy with an independent error.** Mg/Ca and alkenone
   proxies have calibration errors of 1–2 K themselves, i.e. 22–44 m of sea level.
4. **Ice-volume equivalent sea level ignores redistribution.** It is a mass
   conversion only, and it says nothing about where the water goes (§4 of
   [15-06-02](02-sea-level-rise-observation.md)).
5. **An age model built from dated horizons.** Between dates the accumulation rate
   is assumed; hiatuses, bioturbation and reworking all violate it, and the
   assumed rate is not testable with the same data.
6. **A GIA model with a stated Earth structure and deglaciation history.** Its
   uncertainty is largest where the correction is largest, and it correlates with
   the ice history being reconstructed — a circularity that is difficult to avoid.
7. **Local sea level is a depth measurement with its own datum problem.** Terraces,
   cores and speleothems each carry a different (and different-sized) facies and
   datum uncertainty, and none of them is a sea surface.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| δ¹⁸O | — | ‰ (per mil) | ratio × 10³ |
| ice-volume coefficient | — | ‰ m⁻¹ | 0.010 |
| fractionation slope | — | ‰ K⁻¹ | 0.22, sign convention matters |
| sea-level sensitivity | — | m K⁻¹ | coefficient ratio, 22 |
| ice volume | $V$ | m³ | |
| sea-level equivalent | — | m | $\rho_iV/(\rho_wA)$ |
| mass per millimetre | — | Gt | 361 |
| rate | — | mm/yr | |
| age | — | ka | converted to yr before use |

The check that catches the commonest sign error: during a glacial, δ¹⁸O_carb
becomes **more positive**, sea level **falls**, and temperature **falls**. Writing
the temperature term as $0.22(T-T_0)$ reverses its sign and doubles the error
rather than cancelling it.

## 7. Worked examples

All numbers are printed by `code/paleo_sea_level_demo.py`.

### Example 1 — the two contributions

For $SL=-80$ m and $T=10\ ^\circ\mathrm{C}$:
$\delta^{18}\mathrm{O}_{\text{sw}}=0.010\times80=0.800$‰ and the temperature term
$0.22\times(15-10)=1.100$‰, giving 1.900‰. The temperature contribution is
$1.100/0.800=138\%$ of the ice-volume one at these values: **at a 5 K cooling the
temperature term dominates the ice-volume term**, which is why a glacial δ¹⁸O
maximum does not mean an exceptionally large ice volume on its own.

### Example 2 — the inversion

With 1.60‰ and $T=14\ ^\circ\mathrm{C}$: $SL=-138.0$ m; with
$T=12\ ^\circ\mathrm{C}$: $SL=-94.0$ m. The difference of 44 m comes from 2 K.

### Example 3 — the conversions

1 mm of global sea level $=\rho_wA_{\text{ocean}}\times10^{-3}=361$ Gt;
$20\times10^{15}\ \mathrm{m^3}$ of ice $=49.56$ m of sea level.

### Example 4 — the rate and its chronology

60 m over 10 ka $=6.00$ mm/yr; with ±1 ka at each end,
$\sigma_{\text{rate}}=0.85$ mm/yr (14%).

### Example 5 — the GIA term

Near a former ice sheet, an 80 m correction against a 120 m signal means the
correction is 67% of the measured value; a 10% error in the correction is 8 m.

## 8. Python demonstration

`code/paleo_sea_level_demo.py` prints, with units:

1. the forward isotope table and the two coefficients;
2. the inversion table, the 22 m K⁻¹ sensitivity and the uncertainty ridge;
3. the ice-volume equivalent sea level and the 361 Gt mm⁻¹ conversion;
4. the rate-versus-chronology table and the GIA table;
5. the worked-example values of Section 7.

```bash
cd 15-oceanography-marine/06-sea-level-change-marine/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python paleo_sea_level_demo.py
```

## 9. Exercises

[`exercises/01-paleo-sea-level-exercises.md`](./exercises/01-paleo-sea-level-exercises.md)
and
[`exercises/01-paleo-sea-level-solutions.md`](./exercises/01-paleo-sea-level-solutions.md).

## 10. Real-world applications

- **Sea-level targets for coastal planning.** Palaeo records provide the only data
  on rates during rapid deglaciation, and those rates are used as analogues.
- **Ice-sheet history.** The sea-level record is the main independent constraint on
  past ice volume ([15-06-03](03-ice-sheet-marine-margins.md)).
- **GIA model validation.** Modern geodetic data and palaeo records constrain the
  same Earth model
  ([07-06-04](../../07-gravity-geodesy/06-earth-tides-and-rotation/04-post-glacial-rebound.md)).
- **Chronostratigraphy.** The same age models serve the stratigraphic and
  archaeological records.
- **Carbon-cycle and ocean-circulation studies.** δ¹⁸O is used for both
  temperature and ice volume, and the ambiguity of §3.2 propagates into them.

## 11. Further reading

- **Emiliani, C., "Pleistocene temperatures", *Journal of Geology*.** Level:
  research (historical). The paper that established the isotope record as a
  palaeoclimate archive.
- **Huybers, P., & Curry, W., "Links between annual, Milankovitch and continuum
  temperature variability", *Nature*.** Level: research. The covariation of
  temperature and isotope signals and what it implies.
- **Lambeck, K., Rouby, H., Purcell, A., Sun, Y., & Sambridge, M., "Sea level and
  global ice-volume changes during the last glacial cycle", *PNAS*.** Level:
  research. A GIA-constrained sea-level reconstruction and its error budget.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint
- [ ] I can write the two-term isotope model with its coefficients.
- [ ] I can invert a value at an assumed temperature and state the sensitivity.
- [ ] I can compute an ice-volume equivalent sea level and the Gt mm⁻¹ conversion.
- [ ] I can propagate an age error into a rate.
- [ ] I can state the size of the GIA correction and why a local level is not
      eustatic.
- [ ] I can name what is measured and what is modelled in a sea-level curve.
## Common pitfalls
1. **Reading δ¹⁸O as sea level.** It is a sum of two terms; the temperature one
   can dominate.
2. **Quoting a sea-level curve without its temperature assumption.** The
   sensitivity is 22 m K⁻¹.
3. **Treating ESL as a local sea level.** It is a global mass conversion.
4. **Quoting a rate to three figures from a 1 ka age model.** The chronology sets
   the precision.
5. **Applying a single GIA correction to records from different settings.**
   It ranges from metres to tens of metres.
6. **Using a species without a calibration.** Vital effects differ between species
   and between size fractions.
7. **Forgetting that the ice-volume coefficient depends on ice composition.** The
   ice sheets are not identical in δ¹⁸O, and they change through time.

## Related modules
- [15-06-02 Observing Modern Sea Level Rise: Altimetry, Tide Gauges, GRACE](02-sea-level-rise-observation.md) —
  the instrumental half of the same problem.
- [15-06-03 Ice Sheet Marine Margins and Stability](03-ice-sheet-marine-margins.md) —
  the ice dynamics behind the volume changes.
- [15-02-04 Sub-Bottom Profiling and Chirp Systems](../02-marine-geophysics-methods/04-sub-bottom-profiling.md) —
  the stratigraphy that provides the horizons.
- [07-06-04 Post-Glacial Rebound](../../07-gravity-geodesy/06-earth-tides-and-rotation/04-post-glacial-rebound.md) —
  the GIA theory in full.
- [16-06-01 Palaeoclimate Proxies](../../16-atmosphere-climate/06-palaeoclimate/01-paleoclimate-proxies.md) —
  the proxy framework and its pitfalls.
- [04-05-04 Quaternary Climate](../../04-earth-science-geology/05-geomorphology-and-quaternary/04-quaternary-climate.md) —
  the geological context.
