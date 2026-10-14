# Module 17-08 — Remote Sensing Applications in Geophysics

**Stages:** advanced → research · **Prerequisites:** modules 17-01 and 17-02;
basic radiative transfer and statistics.

This module is the payoff of the folder: it takes the measurement chain built in
modules 17-01 to 17-07 and points it at five geophysical problems — mineral
alteration, geothermal heat, soil moisture, the cryosphere and disaster response.
Each lesson is organised around the same honest structure: a physical signal
exists, a sensor can see a proxy for it, an inversion turns the proxy into the
quantity of interest, and the inversion rests on assumptions that are larger than
the instrument's noise. The lessons therefore spend as much space on what the
method cannot do as on what it can.

The five problems are chosen because each one isolates a different failure mode
of inference, and together they cover the practical range. Mineral mapping shows
**degeneracy**: a band depth depends on abundance *and* grain size, so one number
answers two questions. Geothermal remote sensing shows **model dominance**: the
emissivity error exceeds the detector noise, so the detection limit is a
modelling limit. Soil moisture shows **validation**: the product estimates a
footprint mean and the reference measures a point, so the comparison, not the
retrieval, sets the error. The cryosphere shows **regime limits**: the snow-depth
signal saturates, the velocity signal is limited by pixel quantisation, and
permafrost settlement hides under a seasonal swing. Disaster response shows
**decision**: the map is a threshold with a cost structure, and its timeliness is
part of its value. Learning to recognise which failure mode is in play is the
transferable skill of the module.

All models and data in this module are **SYNTHETIC**. No real deposit, field,
glacier, snowpack, flood or mission is referred to, no site-specific number is
quoted, and every figure in every lesson is either printed by a demonstration in
this module or an exact SI constant stated with units.

## Learning objectives

By the end of this module you will be able to:

1. **Trace** a geophysical remote-sensing retrieval from radiance to the
   quantity of interest, and **name** the model at each step.
2. **Demonstrate** the degeneracy of a spectral index and **construct** the
   family of (abundance, grain-size) pairs that reproduce one measurement.
3. **Formulate** and solve a linear unmixing problem and **interpret** the
   condition number of a library as a separability limit.
4. **Invert** the Planck function, and **quantify** the emissivity error that
   dominates a land-surface temperature.
5. **Convert** a subsurface heat flux to a surface anomaly, and **compute** the
   detection limit against a stated emissivity and radiometric uncertainty.
6. **Trace** a soil-moisture retrieval and **compute** the vegetation-induced
   bias and the heterogeneity-limited validation error.
7. **Retrieve** snow depth from a saturating relation and **state** its regime
   of validity.
8. **Measure** a glacier surface velocity by feature tracking and **state** the
   pixel-quantised uncertainty.
9. **Separate** a seasonal cryospheric signal from a secular trend.
10. **Build** a threshold detector for a hazard, **compute** its confusion
    matrix, and **choose** a cost-weighted operating point.
11. **State** the assumed physical model behind any application product, and
    **report** the admitted error.
12. **Decide** whether a given geophysical application is within the regime of a
    remote-sensing method, and **justify** the decision with a number.

## Prerequisites

- [17-01-02 Reflectance, Emissivity and Spectral Signatures](../01-remote-sensing-physics/02-reflectance-and-emissivity.md)
  — the spectral quantities every application measures.
- [17-02-01 Multispectral Imaging, Band Ratios and Indices](../02-optical-and-thermal-remote-sensing/01-multispectral-imaging.md)
  — the indices mineral and cryosphere mapping build on.
- [05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)
  — the physical-property relations the retrievals invert.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Mineral and Alteration Mapping from Space](01-mineral-mapping-rs.md) | doctoral | A band depth is degenerate; a curved spectral error mimics a mineral |
| 02 | [Thermal Remote Sensing for Geothermal Systems](02-geothermal-rs.md) | doctoral | Radiance inverts to temperature; the emissivity sets the detection limit |
| 03 | [Soil Moisture Remote Sensing and Its Validation](03-soil-moisture-rs.md) | doctoral | Precision is not accuracy; a point cannot validate a footprint |
| 04 | [Cryosphere Remote Sensing: Ice, Snow and Permafrost](04-cryosphere-rs.md) | research | Every method has a regime; displacement is resolution-limited |
| 05 | [Remote Sensing for Disaster Response](05-disaster-response-rs.md) | doctoral | A map is a cost-weighted decision; latency is part of the measurement |

## Suggested path

**If you are new to applications:** lessons 01 and 03, which teach the two most
transferable skills — degeneracy and validation. Run both demonstrations.

**If you work on thermal or geothermal problems:** lesson 02 in full, then 04 §7
(the same seasonal-versus-secular problem).

**If you are preparing a research project:** read the "assumptions and regime of
validity" section of every lesson, then the ★★★ exercises of the lesson closest
to your problem. Each is a design specification that turns the honesty points
into an experiment.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-mineral-mapping-rs.md`](01-mineral-mapping-rs.md) | Lesson 01 |
| [`02-geothermal-rs.md`](02-geothermal-rs.md) | Lesson 02 |
| [`03-soil-moisture-rs.md`](03-soil-moisture-rs.md) | Lesson 03 |
| [`04-cryosphere-rs.md`](04-cryosphere-rs.md) | Lesson 04 |
| [`05-disaster-response-rs.md`](05-disaster-response-rs.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas, xarray and the geospatial stack:

```bash
cd 17-remote-sensing-gis/08-remote-sensing-applications-geophysics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mineral_mapping_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geothermal_rs_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python soil_moisture_rs_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cryosphere_rs_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python disaster_response_rs_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), reads and writes no files, and exits 0. They
require no network access.

## Mastery checkpoint

Complete this without notes:

> A study maps alteration with a single band-depth index. **(a)** State two
> physical causes that produce the same index, and one independent measurement
> that would separate them. **(b)** A thermal survey of the same area reports a
> $1.2\ \mathrm{K}$ anomaly; with $k = 2.0\ \mathrm{W\,m^{-1}\,K^{-1}}$ and
> $z = 20\ \mathrm{m}$, compute the implied heat flux and state the emissivity
> uncertainty that would match it. **(c)** A soil-moisture product with
> precision $0.002$ shows a bias of $0.04$ against point probes; state which
> term is the product's and which the comparison's. **(d)** A flood map is
> optimised for $F_1$; state one reason a response team might prefer a different
> threshold.

A worked version of (b)–(d) appears in the lesson-02, lesson-03 and lesson-05
solutions.

## Common pitfalls across this module

1. **Reading a proxy as the target quantity.** A dark pixel, a warm pixel and a
   dark radar return are all proxies.
2. **Confusing precision with accuracy.** A precise retrieval can be biased many
   times its scatter.
3. **Ignoring the regime of validity.** Saturation, resolution and melt all have
   hard limits.
4. **Validating a footprint product against a point.** It measures the
   comparison, not the product.
5. **Assuming a blackbody, a bare soil or a dry grain.** The model, not the
   detector, sets the limit.
6. **Choosing a threshold by $F_1$ alone.** In a response, misses and false
   alarms rarely cost the same.
7. **Reporting an application product without its model.** The assumption is
   part of the number.

## Related modules

- [17-01 Remote Sensing Physics](../01-remote-sensing-physics/README.md) and
  [17-02 Optical and Thermal Remote Sensing](../02-optical-and-thermal-remote-sensing/README.md)
  — the measurement chain these applications consume.
- [11-exploration-geophysics](../../11-exploration-geophysics/README.md) — the
  exploration decisions a mineral, geothermal or groundwater map informs.
- [18-inverse-problems](../../18-inverse-problems/README.md) — degeneracy,
  conditioning and regularisation in general form.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) —
  regression, validation and uncertainty quantification.
