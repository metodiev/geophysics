---
id: 14-02-06
title: "Microgravity and Satellite Gravity for Water Storage Change"
level: doctoral
prereqs: ["14-02-05", "14-01-01", "07-03-06"]
tags: [hydrogeophysics, microgravity, satellite-gravimetry, grace, storage-change, bouguer-slab, leakage]
---

# Microgravity and Satellite Gravity for Water Storage Change

Gravity measures mass. Water has mass, so a change in stored water changes gravity
— and unlike every other method in this module, the measurement does not care
whether the water is in pores or in a fracture, fresh or saline, mobile or bound.
That is a powerful simplification, and it is also the limitation: **gravity
cannot tell water from anything else of the same mass**, and it cannot tell
storage from water level.

This lesson develops both ends of the scale range. Microgravity (a few tens of
metres of resolution, repeatability of a few µGal) measures storage change at a
site. Satellite gravimetry (hundreds of kilometres of resolution, tens of mm of
equivalent water height) measures it over whole basins. The physics is the same
in both cases; what differs is the noise, the corrections, and the leakage.

The instrument-level detail — meters, drifts, tidal corrections, survey
procedures — is in
[07-02 Gravity Instruments and Surveys](../../07-gravity-geodesy/02-gravity-instruments-and-surveys/README.md)
and the satellite mission context in
[07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md).

**All models and data in this module are SYNTHETIC.** The loads, basins, noise
levels and synthetic Stokes coefficients below are invented teaching values. The
physical constants used (G, the mean Earth radius and density, the load Love
number of degree 2, the free-air gradient) are stated with their values.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Bouguer-slab relation $\Delta g = 2\pi G\rho\,\Delta h$ and
   **convert** a gravity change into a mass per unit area.
2. **Compute** the storage change a stated instrument repeatability resolves, and
   **state** why a gravity change cannot separate a water-table change from a
   saturation change.
3. **Build** a microgravity correction budget and **identify** which terms exceed
   the signal.
4. **Convert** a Stokes coefficient to equivalent water height and **state** the
   precision required of the gravity field.
5. **Compute** a mass change from an equivalent water height over a basin.
6. **Quantify** the degree truncation (leakage) of a compact basin load and
   **explain** why a basin-scale mass balance must state its filter.
7. **Verify** the slab approximation against the disk integral and the equivalent
   water height against its linearity properties.

## Prerequisites

- [14-02-05 Surface NMR for Direct Water Detection](05-nmr-for-groundwater.md) —
  the other method that measures water directly, by a completely different
  physics.
- [14-01-01 The Hydrologic Cycle and Water Balance](../01-hydrology-fundamentals/01-hydrologic-cycle.md)
  — the storage-change term that gravity measures rather than infers.
- [07-03-06 Microgravity Applications](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/06-microgravity-applications.md)
  — the survey practice and anomaly interpretation this lesson quantifies.

---

## 1. The Bouguer slab: gravity per metre of water

A laterally extensive layer of density $\rho$ and thickness $\Delta h$ produces a
vertical gravity change

$$\Delta g = 2\pi G\rho\,\Delta h, \qquad
G = 6.67430 \times 10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}.$$

For water ($\rho_w = 1000\ \mathrm{kg\,m^{-3}}$):

$$2\pi G\rho_w = 4.1936 \times 10^{-7}\ \mathrm{m\,s^{-2}}\ \text{per metre}
= 41.94\ \mathrm{\mu Gal}\ \text{per metre of water}$$

(using $1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$).

| water-table change (m) | $\Delta g$ (µGal) |
|---|---|
| 0.05 | 2.10 |
| 0.10 | 4.19 |
| 0.25 | 10.48 |
| 0.50 | 20.97 |
| 1.00 | 41.94 |
| 2.00 | 83.87 |
| 5.00 | 209.7 |

A metre of water table is 42 µGal — twenty times a good repeatability. That single
number is the reason microgravity works as a storage gauge.

**Why the infinite slab is the right first model.** A *finite* disk of radius $R$
at depth $z$ produces
$g_z = 2\pi G\rho\,[1 - z/\sqrt{z^2 + R^2}]$, which tends to the slab value as
$R/z \to \infty$ — verified in the demonstration (at $R = 1$ km and $z = 100$ m the
disk gives only 37.76 µGal against the slab's 41.94, an 11% deficit).
In hydrogeology the water-table change is usually much wider than it is deep, so
the slab is the natural model, and the demonstration measures exactly how wide
"wide" must be: at $R/z = 400$ the disk gives 41.52 µGal against the slab's 41.94
(a 1% deficit).

## 2. What microgravity resolves in storage terms

Since $\Delta g = 2\pi G\Delta m$ with $\Delta m$ the mass change per unit area,

$$\Delta m = \frac{\Delta g}{2\pi G}
= \Delta g\,[\mathrm{\mu Gal}] \times
\frac{10^{-8}}{4.1936 \times 10^{-10}}\ \mathrm{kg\,m^{-2}}
\approx 23.85\,\Delta g\,[\mathrm{\mu Gal}]\ \mathrm{kg\,m^{-2}}.$$

| repeatability (µGal) | equivalent water-table change (m) | equivalent storage (mm of water) |
|---|---|---|
| 3 | 0.072 | 71.5 |
| 5 | 0.119 | 119.2 |
| 10 | 0.238 | 238.5 |
| 20 | 0.477 | 476.9 |

A 5 µGal repeatability resolves about 120 mm of water-table change, or 12 mm of
storage at a specific yield of 0.10. That is comparable with a good satellite
product — but delivered at metre-scale spatial resolution, which is why
microgravity survives in the satellite era.

**The ambiguity that no amount of precision removes.** Gravity measures mass, not
level. A 1 m water-table rise (41.94 µGal) and a saturation increase of 0.10 over
5 m of soil at $n = 0.30$ (6.29 µGal) are the *same kind of measurement*: the
second is 15% of the first, i.e. it mimics 0.15 m of water-table movement, which is
larger than the 0.12 m detection limit. So a gravity change must always be
accompanied by water levels and, where the unsaturated zone matters, by soil
moisture. **A gravity-only storage claim is an assumption in disguise.**

## 3. The correction budget

| effect | magnitude (µGal) | equivalent water-table change (m) |
|---|---|---|
| solid-Earth tide (range) | 100 | 2.39 |
| ocean tide loading | 10 | 0.24 |
| instrument drift, 1 day | 20 | 0.48 |
| barometric, 10 hPa (at $-3$ nGal Pa$^{-1}$) | 3.0 | 0.07 |
| 1 cm height error | 3.1 | 0.07 |

Every figure is larger than or comparable with the storage signal of §2, except the
barometric term. Two are worth deriving rather than quoting:

- **The free-air gradient** is $2g/a = 2(9.81)/6.371 \times 10^{6}
  = 3.0796 \times 10^{-6}\ \mathrm{s^{-2}}$, i.e.
  $307.96\ \mathrm{\mu Gal\,m^{-1}} = 3.080\ \mathrm{\mu Gal\,cm^{-1}}$.
  (The normal-gravity free-air coefficient used in surveying — 0.3086 mGal/m =
  3.086 µGal/cm — is the ellipsoidal equivalent; the difference is a convention,
  not an error.) **A 1 cm levelling error is 3.1 µGal, i.e. 7.3% of a 1 m
  water-table change**, which is why height control at the centimetre level is
  mandatory and why it is the most common failure of a microgravity programme.
- **The barometric term** follows from an admittance of about
  $-3\ \mathrm{nGal\,Pa^{-1}}$: 10 hPa = 1000 Pa gives 3.0 µGal.

The tide and the drift are 2–25 times the signal being measured, so they are
modelled and removed rather than assumed small. Every one of these numbers is a
*model* magnitude in this synthetic budget; in practice each is computed from the
site's latitude, the survey's timing and the local pressure record.

## 4. Equivalent water height from a Stokes coefficient

A time-variable gravity field is expressed as changes in the normalized Stokes
coefficients $\Delta C_{lm}, \Delta S_{lm}$. A surface mass load is converted to an
**equivalent water height** through the degree-dependent relation

$$\mathrm{EWH}(\theta,\varphi) = \frac{a\,\rho_{\text{ave}}}{3\rho_w}
\sum_{l=2}^{l_{\max}}\frac{2l+1}{1+k_l}
\sum_{m=0}^{l}\bar{P}_{lm}(\cos\theta)
\left[\Delta C_{lm}\cos m\varphi + \Delta S_{lm}\sin m\varphi\right],$$

with $a = 6.371 \times 10^{6}$ m the mean Earth radius,
$\rho_{\text{ave}} = 5517\ \mathrm{kg\,m^{-3}}$ the mean Earth density,
$\rho_w = 1000\ \mathrm{kg\,m^{-3}}$, $k_l$ the elastic load Love numbers, and
$\bar{P}_{lm}(1) = \sqrt{5}$ for $l = 2$, $m = 0$ (normalized associated Legendre).

For the degree-2 zonal term at the pole,

$$\mathrm{EWH} = \frac{a\,\rho_{\text{ave}}\,5}{3\rho_w(1+k_2)}\sqrt{5}\,
\Delta C_{20}
= 1.8713 \times 10^{8}\ \mathrm{m}\ \times \Delta C_{20},$$

with $k_2 = -0.30$:

| $\Delta C_{20}$ | EWH at the pole (mm) |
|---|---|
| $1.0 \times 10^{-12}$ | 0.187 |
| $1.0 \times 10^{-11}$ | 1.871 |
| $1.0 \times 10^{-10}$ | 18.71 |
| $3.0 \times 10^{-10}$ | 56.14 |
| $1.0 \times 10^{-9}$ | 187.1 |

Three consequences: the geodetic coefficients that matter are of order
$10^{-11}$–$10^{-10}$; the **degree-1 terms must be removed** (they contain the
geocentre motion, which is not a surface load); and $k_2 < 1$ means the elastic
Earth's own deformation *amplifies* the observed gravity effect of the load, so
ignoring $k_l$ understates the water by 30% at degree 2.

## 5. Mass change over a basin, and leakage

From EWH to mass is arithmetic: $\Delta M = \rho_w \times \mathrm{EWH} \times
\text{area}$. A 20 mm EWH change over 200 000 km² is

$$\Delta M = 1000 \times 0.020 \times 2 \times 10^{11}
= 4.0 \times 10^{12}\ \mathrm{kg} = 4.0\ \mathrm{km^{3}}\ \text{of water}.$$

That is the annual water demand of a city of several million people, which is why
satellite gravimetry matters for water management: it measures storage change at
the scale at which the decisions are made.

**Leakage is the price.** A compact load has a harmonic spectrum that extends to
high degree, so a product truncated at $l_{\max}$ captures only part of it. For a
uniform disk load of angular radius $\theta_0$, the demonstration computes the
degree variance captured by truncation:

| $\theta_0$ (deg) | disk radius (km) | fraction below $l = 10$ | $l = 20$ | $l = 40$ |
|---|---|---|---|---|
| 1.0 | 111 | 10.6% | 22.2% | 44.1% |
| 2.0 | 222 | 19.5% | 39.8% | 72.1% |
| 5.0 | 556 | 47.2% | 81.7% | 97.7% |
| 10.0 | 1112 | 81.6% | 97.1% | 99.2% |

A basin of 100 km radius has only 10.6% of its degree-variance below degree 10: a
product truncated at degree 10 recovers a *tenth* of its signal, and the deficit
appears as "leakage" from outside the basin in a regional solution. This is why
**every basin-scale mass balance from satellite gravimetry must state the filter,
the truncation degree and the leakage correction**, and why a mass balance that
closes to 10% without them is a coincidence rather than a result.

## 6. Python demonstration

`code/gravity_for_groundwater_demo.py` prints all of the above with units. It:

1. computes the Bouguer-slab coefficient (41.94 µGal per metre of water) and a
   table of water-table changes;
2. converts repeatability into resolvable storage (5 µGal → 119 mm of water-table
   change) and quantifies the water-level-versus-saturation ambiguity (a
   saturation change of 0.10 over 5 m mimics 0.15 m of water-table movement);
3. builds the correction budget, derives the free-air gradient from $2g/a$
   (3.080 µGal/cm) and states the ellipsoidal convention, and shows that a 1 cm
   height error is 7.3% of a 1 m water-table change;
4. converts a Stokes coefficient to equivalent water height
   (1.8713 × 10⁸ m per unit $\Delta C_{20}$) and tabulates the required precision;
5. computes a mass change (4.0 km³ for 20 mm over 200 000 km²) and the
   degree-truncation table for four disk radii;
6. verifies the slab against the disk integral (37.76 → 41.94 µGal as $R$ grows),
   the linearity of EWH in $\Delta C_{20}$ (exactly 2) and in $(1+k_l)$ (exactly 2),
   and the structure of the general-degree formula (ratio 2.415 for $l = 4$ against
   $l = 2$).

```bash
cd 14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_for_groundwater_demo.py
```

## 7. Assumptions and regime of validity

1. **The slab is infinite and of uniform density.** A local storage change with a
   lateral extent comparable to its depth cannot be treated as a slab, and the
   demonstration measures the resulting error (at $R/z = 10$ the disk gives 37.8
   against the slab's 41.9 µGal, an 11% deficit). At $R/z \gtrsim 100$ the
   approximation is good to 1%.
2. **The mass change is water of density $\rho_w$.** A mixed change (water plus
   gas, or water plus a temperature change) needs a stated density model; a
   gravity change in a thermally varying aquifer is not purely hydrological.
3. **Density is uniform in depth.** A water-table rise replaces air with water in
   the drained zone, so the *effective* density of the change is $\rho_w S_y$, not
   $\rho_w$, if only part of the pore space fills. The demonstration's slab uses
   the full water density, so a specific-yield correction must be applied when
   interpreting a saturation change above the water table.
4. **The load Love numbers are elastic.** $k_l$ for an elastic Earth is standard;
   a viscous response matters for long-period (century-scale) loads and for the
   present-day response to past ice loads, which must be modelled separately.
5. **Degree-1 terms are removed.** Their inclusion misattributes geocentre motion
   to water.
6. **The atmosphere is removed.** Atmospheric mass varies by more than the
   hydrological signal at some locations and must be subtracted with a consistent
   (usually non-inverted barometer) convention.
7. **Glacial isostatic adjustment and other solid-Earth signals are modelled, not
   measured.** Any trend estimate must state how they were removed, since they are
   of the same size as a real depletion trend in some regions.
8. **The truncation and filter are stated.** As §5 makes quantitative, a basin
   mass balance is not reproducible without them.

## Mastery checkpoint

A synthetic microgravity monitoring network covers a 4 km × 4 km area over an
unconfined aquifer with $S_y = 0.12$. Surveys are repeated twice a year with a
5 µGal repeatability; the network is levelled to a shared benchmark.

**(a)** Compute the gravity change for a 1 m water-table decline. **(b)** Compute
the mass change per unit area and the storage change in mm of water, with the
specific-yield correction. **(c)** Compute the smallest storage change the network
can resolve at 1σ and state the corresponding water-table change. **(d)** The area
also shows a 0.05 increase in saturation over the top 3 m of the unsaturated zone
at $\phi = 0.35$. Compute the gravity effect and compare it with (a). **(e)** The
co-located satellite product reports a 15 mm EWH decline over 0.5° cells
(≈ 55 km). Explain in two sentences why this is consistent or inconsistent with
your microgravity result, and name the two corrections that decide the answer.
**(f)** Compute the height error that would produce a 10 µGal error and state the
survey consequence.

## Common pitfalls

1. **Quoting a storage change from gravity without water levels.** The saturation
   ambiguity is a real, measured equivalence (0.15 m of water-table movement).
2. **Ignoring the height reference.** A centimetre is 3.1 µGal; that is routine
   levelling error and 7% of a metre of water.
3. **Treating tidal and drift corrections as cosmetic.** They exceed the signal.
4. **Applying the slab coefficient to a load whose lateral extent is comparable
   with its depth.** The demonstration's disk check quantifies the error.
5. **Forgetting the specific yield.** A saturation change above the water table
   has an effective density of $\rho_w S_y$, not $\rho_w$.
6. **Reporting an EWH change without the filter and truncation degree.** A
   basin-scale number is not reproducible without them.
7. **Comparing microgravity and satellite numbers without matching their
   footprints.** One is metres, the other tens of kilometres.
8. **Ignoring GIA and atmospheric correction in a trend.** Both can be the same
   size as the hydrological signal.

## Related modules

- [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md)
  and [07-05-05 GRACE Applications](../../07-gravity-geodesy/05-satellite-gravimetry/05-grace-applications.md) —
  the mission detail and application practice.
- [07-03-06 Microgravity Applications](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/06-microgravity-applications.md) —
  field survey practice and anomaly interpretation.
- [07-03-07 Time-Variable Gravity](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/07-time-variable-gravity.md) —
  the repeat-survey framework.
- [14-01-01 The Hydrologic Cycle and Water Balance](../01-hydrology-fundamentals/01-hydrologic-cycle.md) —
  the term gravity measures independently.
- [03 Saline Intrusion and Coastal Aquifer Monitoring](../04-contaminant-and-environmental/03-saline-intrusion.md) —
  a complementary measurement that is sensitive to the water's *chemistry* rather
  than its mass.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) — trend
  estimation and its uncertainty, which is where most published storage-trend
  disagreements arise.

## Code and exercises

- Demonstration: [`code/gravity_for_groundwater_demo.py`](code/gravity_for_groundwater_demo.py)
- Exercises: [`exercises/06-gravity-for-groundwater-exercises.md`](exercises/06-gravity-for-groundwater-exercises.md)
- Worked solutions: [`exercises/06-gravity-for-groundwater-solutions.md`](exercises/06-gravity-for-groundwater-solutions.md)
