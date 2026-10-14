---
id: 11-03-05
title: "Geophysics for Unconventional Reservoirs"
level: doctoral
prereqs: ["11-03-03", "05-04-05", "06-12-01", "05-08-05"]
tags: [exploration-geophysics, unconventional, anisotropy, microseismic, brittleness]
---

# Geophysics for Unconventional Reservoirs

**All models and data in this module are SYNTHETIC.** The rock properties,
fracture parameters, source magnitudes and acquisition geometries below are
chosen teaching values. No well, play, company or published field measurement is
described.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** Young's modulus and Poisson's ratio from $v_p$, $v_s$, $\rho$, and
   **explain** why a brittleness index is a convention rather than a property.
2. **Show** that two common brittleness indices rank a set of rocks differently,
   and **state** what must accompany any brittleness number.
3. **Derive** the exact VTI phase-velocity expression, **compute** the Thomsen
   parameters from a stiffness matrix and **explain** why recovering them from
   velocities tests algebra rather than geology.
4. **Quantify** the depth bias from ignoring $\delta$, and the shear-wave
   splitting produced by fracture-induced (HTI) anisotropy.
5. **Compute** seismic moment, magnitude, slip and rupture area for a
   microseismic event, and **state** what the scaling does not determine.
6. **Budget** the detection range of a monitoring array and **explain** why
   detectability and resolution pull in opposite directions.
7. **Quantify** the location error of a monitoring geometry and the systematic
   bias introduced by a velocity-model error.
8. **Compute** the pore-pressure change needed to trigger slip on a fracture,
   and **explain** why the result depends on quantities no surface survey
   measures.

## Prerequisites

- [11-03-03 Reservoir Characterisation and Property Prediction](03-reservoir-characterisation.md) —
  the rock-physics chain and the Bayesian view of prediction.
- [05-04-05 Anisotropy in Rocks: Causes and Magnitudes](../../05-core-geophysics/04-rock-physics/05-anisotropy-rock.md) —
  the physical origins of the anisotropy used here.
- [06-12-01 Causes of Induced Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/01-induced-seismicity-causes.md) —
  the seismicity that monitoring is designed to observe.
- [05-08-05 Borehole Imaging, Dipmeter and Fracture Detection](../../05-core-geophysics/08-geophysical-logging/05-imaging-logs.md) —
  the borehole measurement that calibrates every surface fracture attribute.

## 1. What changes when the reservoir is "unconventional"

In a conventional play the exploration question is *where is the trap*, and the
geophysical answer is a structure and a fluid indicator
([11-03-01](01-seismic-in-exploration.md), [11-03-03](03-reservoir-characterisation.md)).
In an unconventional play the rock is present almost everywhere in a fairway,
and the questions become:

1. **Will it produce when stimulated?** This is a question about rock mechanics
   (brittleness, stress state) and about the fracture network.
2. **Where is the organic richness?** A source-rock property, only weakly
   related to a geophysical observable.
3. **How do we watch what the stimulation does?** Microseismic and
   fibre-optic monitoring.

Geophysics contributes **proxies** to all three, and the professional standard is
to name them as such. No surface method measures permeability, kerogen content,
or the closure stress on a natural fracture. What follows computes the proxies,
their sensitivities, and — in every section — their failure modes.

## 2. Elastic moduli and brittleness

From $v_p$, $v_s$ and $\rho$ (all in SI), the isotropic elastic constants follow
exactly:

$$E = \rho v_s^{2}\,\frac{3v_p^{2}-4v_s^{2}}{v_p^{2}-v_s^{2}},
\qquad
\nu = \frac{v_p^{2}-2v_s^{2}}{2\left(v_p^{2}-v_s^{2}\right)} .$$

The demonstration evaluates four chosen lithologies:

| lithology | $v_p$ (m/s) | $v_s$ (m/s) | $\rho$ (kg/m³) | $E$ (GPa) | $\nu$ |
|---|---|---|---|---|---|
| brittle carbonate | 6200 | 3400 | 2700 | 80.2 | 0.285 |
| shale (clay rich) | 3200 | 1750 | 2450 | 19.3 | 0.287 |
| organic-rich shale | 2900 | 1600 | 2350 | 15.4 | 0.281 |
| tight sandstone | 4600 | 2800 | 2600 | 49.2 | 0.206 |

A **brittleness index** normalises these against stated endpoints. Two of the
many conventions in use:

$$\text{BI}_E = \frac{E - E_{\min}}{E_{\max}-E_{\min}},
\qquad
\text{BI}_\nu = \frac{\nu_{\max}-\nu}{\nu_{\max}-\nu_{\min}} .$$

With the endpoints taken from the four rocks listed (a stated, reproducible
choice; the demonstration prints them), the results are:

| lithology | BI$_E$ | BI$_\nu$ |
|---|---|---|
| brittle carbonate | 1.00 | 0.02 |
| tight sandstone | 0.52 | 1.00 |
| shale (clay rich) | 0.06 | 0.00 |
| organic-rich shale | 0.00 | 0.07 |

**Ranked by $\text{BI}_E$: carbonate, sandstone, shale, organic shale. Ranked by
$\text{BI}_\nu$: sandstone, organic shale, carbonate, shale.** The two
conventions disagree at the top, and not marginally. The reason is physics: a
stiff rock ($E$ large) can still have a high Poisson's ratio, and it is
$\nu$ — the ratio of lateral to axial strain — that governs whether the rock
dilates or compacts under a stress change. Neither index is *the* brittleness;
both are proxies for a complex failure process, and both inherit the calibration
set they were normalised on.

The practical rule: **publish the moduli, the index formula and the endpoints.**
A brittleness map without them cannot be reproduced, compared, or corrected.

## 3. Anisotropy: the two mechanisms that matter

### 3.1 VTI: vertical transverse isotropy, and the exact phase velocities

A transversely isotropic medium with a vertical symmetry axis is described by
five independent stiffnesses $(C_{11}, C_{33}, C_{13}, C_{44}, C_{66})$ and three
Thomsen parameters:

$$\varepsilon = \frac{C_{11}-C_{33}}{2C_{33}}, \qquad
\delta = \frac{(C_{13}+C_{44})^2-(C_{33}-C_{44})^2}{2C_{33}(C_{33}-C_{44})},
\qquad
\gamma = \frac{C_{66}-C_{44}}{2C_{44}} .$$

The exact phase velocities at angle $\theta$ from the symmetry axis are

$$\rho v_{p,\text{SV}}^{2} = \tfrac12\left[
C_{11}\sin^{2}\theta + C_{33}\cos^{2}\theta + C_{44}
\pm \mathcal{D}\right],$$

$$\mathcal{D}^{2} = \left[\left(C_{11}-C_{44}\right)\sin^{2}\theta -
\left(C_{33}-C_{44}\right)\cos^{2}\theta\right]^{2}
+ 4\left(C_{13}+C_{44}\right)^{2}\sin^{2}\theta\cos^{2}\theta,$$

$$\rho v_{SH}^{2} = C_{66}\sin^{2}\theta + C_{44}\cos^{2}\theta .$$

The demonstration builds a synthetic shale-like medium from
$v_p = 3.20\ \mathrm{km\,s^{-1}}$, $v_s = 1.80\ \mathrm{km\,s^{-1}}$,
$\rho = 2450\ \mathrm{kg\,m^{-3}}$ and chosen
$\varepsilon = 0.20,\ \delta = 0.10,\ \gamma = 0.15$:

| angle (°) | $v_p$ (km/s) | $v_{SV}$ (km/s) | $v_{SH}$ (km/s) |
|---|---|---|---|
| 0 | 3.200 | 1.800 | 1.800 |
| 30 | 3.304 | 1.895 | 1.866 |
| 45 | 3.446 | 1.912 | 1.930 |
| 60 | 3.611 | 1.875 | 1.992 |
| 90 | 3.786 | 1.800 | 2.052 |

Recovering the parameters from the velocities at 0° and 90° returns
$\varepsilon = 0.2000$ and $\gamma = 0.1500$ — **exactly**, because the
definitions *are* those two limits. This is worth stating plainly: a
forward-model-versus-definition check verifies algebra, not geology. The genuine
test is whether a measured $\varepsilon$ can be predicted from an independent
measurement (mineralogy, layering, fractures).

**What ignoring $\delta$ costs.** The NMO velocity in a VTI medium is
$v_{\text{nmo}} = v_{p,v}\sqrt{1+2\delta}$, so using the vertical velocity
instead biases every converted depth by
$\sqrt{1+2\delta} = 1.095$, i.e. **9.5%** here. At 3 km that is 285 m. This is
the same class of error as the velocity error of
[11-03-06 §3](06-borehole-and-integration.md), and it is *systematic in depth
and organised by the layering*, so it cannot be averaged out.

### 3.2 HTI: fractures, and shear-wave splitting

A single set of aligned vertical fractures makes a medium with a horizontal
symmetry axis (HTI). At vertical incidence the two shear modes split: the one
polarised along the fractures travels at $v_{\text{fast}}$ and the one across
them at $v_{\text{slow}}$. In terms of the same stiffnesses,

$$v_{\text{fast}} = \sqrt{C_{66}/\rho}, \qquad
v_{\text{slow}} = \sqrt{C_{44}/\rho}, \qquad
\gamma = \frac{C_{66}-C_{44}}{2C_{44}} = \frac{v_{\text{fast}}^2-v_{\text{slow}}^2}
{2v_{\text{slow}}^2}.$$

The demonstration uses $v_s = 3.00\ \mathrm{km\,s^{-1}}$ and reports:

| $\gamma$ | $v_{\text{fast}}$ (km/s) | split | $\Delta t$ 50 m | $\Delta t$ 100 m | $\Delta t$ 200 m |
|---|---|---|---|---|---|
| 0.02 | 3.059 | 2.0% | 0.324 ms | 0.647 ms | 1.295 ms |
| 0.05 | 3.146 | 4.9% | 0.776 ms | 1.551 ms | 3.102 ms |
| 0.10 | 3.286 | 9.5% | 1.452 ms | 2.904 ms | 5.809 ms |

Two things must be said carefully.

- **The measurement is a product, not a fracture property.** The splitting time
  is the path integral of the shear anisotropy. It constrains fracture
  **orientation** and an integrated intensity. It does not measure aperture,
  connectivity, or permeability. A densely fractured impermeable rock and a
  sparsely fractured permeable one can produce the same splitting.
- **The first-order form is biased high.** $\Delta t \approx
  \gamma d/v_s$ gives 1.667 ms for $\gamma = 0.05$, $d = 100$ m, against the
  exact 1.551 ms — 7% high. For quantitative work, use the exact expression
  above.

## 4. Microseismics: source scaling

For a circular rupture of radius $a$ with a static stress drop $\Delta\sigma$ the
seismic moment is

$$M_0 = \frac{16}{7}\,\Delta\sigma\,a^{3},
\qquad
M_w = \frac{2}{3}\left(\log_{10}M_0 - 9.1\right) \quad (M_0 \text{ in N m}),$$

and the mean slip follows from the moment's definition $M_0 = \mu A \bar{u}$ with
$A = \pi a^{2}$. The demonstration uses $\mu = 20$ GPa and
$\Delta\sigma = 1$ MPa:

| radius $a$ (m) | area (m²) | $M_0$ (N m) | $M_w$ | mean slip (mm) |
|---|---|---|---|---|
| 10 | 314.2 | $2.286\times10^{9}$ | 0.17 | 0.364 |
| 20 | 1256.6 | $1.829\times10^{10}$ | 0.77 | 0.728 |
| 50 | 7854.0 | $2.857\times10^{11}$ | 1.57 | 1.819 |
| 100 | 31415.9 | $2.286\times10^{12}$ | 2.17 | 3.638 |

So a 100 m rupture with a 1 MPa stress drop is $M_w = 2.2$, with millimetres of
slip. Microseismicity is small because the ruptures are small, not because the
rock is weak. The inverse statement is the one that matters for interpretation:
**a located event gives a rupture size and a slip only through an assumed
stress drop**, which is not measured. Two interpretations of the same event
cloud can differ in released moment by an order of magnitude.

## 5. Detection: the amplitude budget

A working model of far-field amplitude is geometric spreading times absorption:

$$A(r) = \frac{A_0}{r}\exp\left(-\frac{\pi f r}{Q v}\right).$$

With $f = 20$ Hz, $v = 3.0\ \mathrm{km\,s^{-1}}$, $Q = 100$ and $A_0 = 1$:

| distance (m) | $1/r$ | absorption | product | loss (%) |
|---|---|---|---|---|
| 250 | $4.00\times10^{-3}$ | 0.9490 | $3.80\times10^{-3}$ | 5.1 |
| 500 | $2.00\times10^{-3}$ | 0.9006 | $1.80\times10^{-3}$ | 9.9 |
| 1000 | $1.00\times10^{-3}$ | 0.8110 | $8.11\times10^{-4}$ | 18.9 |
| 2000 | $5.00\times10^{-4}$ | 0.6578 | $3.29\times10^{-4}$ | 34.2 |
| 4000 | $2.50\times10^{-4}$ | 0.4327 | $1.08\times10^{-4}$ | 56.7 |

The **detection radius** for a relative noise floor of $10^{-3}$:

| $Q$ | $A_0$ | detection radius (m) |
|---|---|---|
| 50 | 1.0 | 740 |
| 100 | 1.0 | 840 |
| 200 | 1.0 | 910 |
| 100 | 3.0 | 1990 |

At these ranges **geometric spreading dominates**: between $Q = 50$ and
$Q = 200$ the radius moves only from 740 to 910 m, while tripling the source
amplitude moves it to 1990 m. Two consequences for survey design:

1. Detection range is a **budget** — array geometry, noise floor and event size
   — not a property of the event.
2. **Raising frequency to improve location precision shortens the detection
   range**, and absorption is the mechanism. There is no free lunch between the
   two, which is why real monitoring networks combine deep sensors close to the
   reservoir with surface stations
   ([23-02-07 Distributed Acoustic Sensing and Nodal Systems](../../23-field-methods-instruments/02-seismic-instruments-and-fieldwork/07-das-and-nodal-systems.md)).

## 6. Location: geometry first, misfit never

Location uncertainty is dominated by **geometry**, and the demonstration makes
that explicit. With a 2 ms pick error, $v = 3.0\ \mathrm{km\,s^{-1}}$, a known
origin time of 0.35 s and 100 realisations:

| geometry | error (m) | depth error (m) | travel-time residual (ms) |
|---|---|---|---|
| 16 surface stations, 4 km aperture | 20 | 18 | 1.33 |
| 4 symmetric surface corners | 1827 | 1827 | 0.77 |
| 12-level downhole array, origin time unknown | 449 | 138 | 1.68 |
| 12-level downhole array, origin time known | 535 | 5 | 1.77 |

Every row fits the picks to within the pick error — the residual column proves
it — and the locations differ by two orders of magnitude. The reasons are
geometric:

- a wide surface array with many stations separates depth from origin time;
- four stations at the corners of a square symmetric about the epicentre make
  every travel time equal, so depth and origin time are **degenerate**;
- a single vertical array gives excellent depth but poor horizontal control,
  because it is nearly one-dimensional;
- knowing the origin time (from a calibration shot) buys depth control that no
  amount of picking precision can buy otherwise.

The corollary for interpretation is that a microseismic "cloud" is a set of
locations **with these error bars**, and any statement about cloud dimensions,
growth rate or azimuthal coverage must carry them.

## 7. Why the rock fails: stress, pressure and permeability

Slip on a pre-existing, cohesionless fracture obeys a Coulomb condition. With
normal stress $\sigma_n$, resolved shear stress $\tau$, pore pressure $P$ and
friction coefficient $\mu_f$:

$$\tau \ge \mu_f\left(\sigma_n - P\right)
\qquad\Longrightarrow\qquad
P \ge \sigma_n - \frac{\tau}{\mu_f}.$$

The demonstration's table (a negative answer means the fracture is already
critically stressed):

| $\sigma_n$ (MPa) | $\tau/\sigma_n$ | $\mu_f = 0.4$ | $\mu_f = 0.6$ | $\mu_f = 0.8$ |
|---|---|---|---|---|
| 40 | 0.50 | already critical | 6.7 MPa | 15.0 MPa |
| 40 | 0.65 | already critical | already critical | 7.5 MPa |
| 60 | 0.65 | already critical | already critical | 11.2 MPa |

The stress ratio $\tau/\sigma_n$ is what decides: at 0.65, a fracture in a
$\mu_f = 0.6$ stress state is within a few MPa of failure before any injection.
This is why induced seismicity is governed by the **pre-existing stress field
and fracture orientation**, and why a geophysical survey that maps structure and
fracture intensity still cannot predict which faults will slip. The traffic-light
protocol is a response framework, not a prediction
([06-12-04](../../06-seismology/12-induced-and-triggered-seismicity/04-monitoring-and-mitigation.md)).

## 8. Worked examples

### Example 1 — from logs to brittleness

A log interval gives $v_p = 4.30\ \mathrm{km\,s^{-1}}$,
$v_s = 2.55\ \mathrm{km\,s^{-1}}$, $\rho = 2550\ \mathrm{kg\,m^{-3}}$.

1. $v_p^2 = 1.849\times10^{7}$, $v_s^2 = 6.5025\times10^{6}$,
   $3v_p^2-4v_s^2 = 5.547\times10^{7}-2.601\times10^{7} = 2.946\times10^{7}$.
2. $E = 2550\times6.5025\times10^{6}\times2.946\times10^{7}/(1.199\times10^{7})
   = 4.08\times10^{10}\ \mathrm{Pa} = 40.8$ GPa.
3. $\nu = (1.849-1.3005)\times10^{7}/(2\times1.199\times10^{7}) = 0.229$.
4. With the demonstration's endpoints ($E$: 15.4–80.2 GPa; $\nu$: 0.206–0.287):
   $\text{BI}_E = (40.8-15.4)/64.8 = 0.39$ and
   $\text{BI}_\nu = (0.287-0.229)/0.081 = 0.72$.

Two numbers, two answers, both defensible. Report both and the endpoints.

### Example 2 — a shear-wave splitting budget

Target interval 120 m thick, expected $\gamma = 0.04$,
$v_s = 2.8\ \mathrm{km\,s^{-1}}$.

- Exact: $v_{\text{fast}} = 2.8\sqrt{1.08} = 2.910\ \mathrm{km\,s^{-1}}$, so
  $\Delta t = 120\left(1/2800 - 1/2910\right)
  = 120\left(3.5714\times10^{-4} - 3.4364\times10^{-4}\right)
  = 1.618\times10^{-3}\ \mathrm{s} = 1.62$ ms.
- First-order: $\gamma d/v_s = 0.04\times120/2800 = 1.714$ ms, which is
  **5.9% high** — the same direction and the same order as the demonstration's
  7% for $\gamma = 0.05$.

So the splitting is 1.6 ms across a 120 m interval. Whether that is measurable
depends entirely on the data: a 1 ms sampling interval cannot resolve it, and a
broadband downhole receiver at 250 Hz sampling can. The splitting time is not
the deliverable; the *interpretable* quantity is the anisotropy, and it comes
with the path-length assumption.

### Example 3 — the pressure to trigger

At $\sigma_n = 50$ MPa, $\tau = 27$ MPa, $\mu_f = 0.6$:
$P \ge 50 - 27/0.6 = 50 - 45 = 5$ MPa. A 5 MPa injection-driven pressure change
at the fracture is enough. If the same fracture had $\tau = 33$ MPa,
$P \ge 50 - 55 = -5$ MPa: it is already sliding, and the seismicity is a
response to whatever perturbation occurs. **The difference between "needs
5 MPa" and "already critical" is a 20% difference in the resolved shear
stress** — which is exactly the quantity that cannot be measured from the
surface.

## 9. Assumptions and regime of validity

1. **Isotropy in §2.** $E$ and $\nu$ from $v_p, v_s, \rho$ are isotropic
   constants; in a shale with $\varepsilon = 0.20$ they are apparent values that
   depend on the measurement direction (usually vertical log). The brittleness
   index inherits the direction.
2. **Brittleness conventions are arbitrary.** Endpoints, formula and index
   choice change the ranking (§2).
3. **Thomsen parameters are weak-anisotropy parameterisations.** The exact phase
   velocities above are exact for a VTI stiffness matrix, but mapping
   $\varepsilon,\delta,\gamma$ to mineralogy or fracture density requires a
   model (Hudson, Schoenberg, Backus) with its own assumptions.
4. **Splitting measures a product.** Orientation is robust; intensity is
   degenerate with path length and fracture compliance.
5. **Moment scaling assumes a circular crack and a uniform stress drop.** Real
   ruptures are irregular, and stress drop is not measurable from a single
   station.
6. **The amplitude model is a point-source, single-frequency, isotropic-radiation
   approximation.** Radiation patterns, directivity and site effects all modify
   amplitudes by factors comparable to the range differences computed above.
7. **Location assumes a known homogeneous velocity.** The demonstration's
   velocity-error experiment (in the companion demo, §10) shows the resulting
   bias is systematic and does not average out.
8. **Coulomb failure assumes a cohesionless, planar, well-oriented fracture.**
   Cohesion, asperities, poroelastic stress changes and fault-zone damage all
   change the threshold.

## 10. Python demonstration

`code/unconventional_geophysics_demo.py` prints:

1. the modulus and brittleness table with both indices and their rankings;
2. exact VTI phase velocities from a stiffness matrix, the recovered Thomsen
   parameters, and the $\sqrt{1+2\delta}$ depth bias;
3. the HTI splitting table with the first-order comparison;
4. moment, magnitude, area and slip for four rupture radii;
5. the amplitude budget with distance, and detection radii for four $Q$/amplitude
   combinations;
6. location error, depth error and residual for four acquisition geometries;
7. the Coulomb table of required pore pressure.

It is print-only, seeded with `np.random.default_rng(20261014)` and exits 0.

## 11. Exercises

- [`exercises/05-unconventional-geophysics-exercises.md`](exercises/05-unconventional-geophysics-exercises.md)
- [`exercises/05-unconventional-geophysics-solutions.md`](exercises/05-unconventional-geophysics-solutions.md)

## Mastery checkpoint

> A shale interval has $v_p = 3.60\ \mathrm{km\,s^{-1}}$,
> $v_s = 1.95\ \mathrm{km\,s^{-1}}$, $\rho = 2500\ \mathrm{kg\,m^{-3}}$ and
> measured $\delta = 0.12$. **(a)** Compute $E$ and $\nu$. **(b)** Compute both
> brittleness indices with the endpoints used in this lesson and state whether
> they agree in rank with the tight sandstone of §2. **(c)** Compute the depth
> bias at 2.5 km from ignoring $\delta$. **(d)** A shear-wave splitting of
> 2.0 ms is measured over a 150 m interval with $v_s = 2.0\ \mathrm{km\,s^{-1}}$:
> compute $\gamma$ exactly and state what it does and does not tell you about the
> fractures.

## Common pitfalls

1. **Quoting a brittleness index without its formula and endpoints.**
2. **Treating $E$ and $\nu$ from a vertical log as rock constants in an
   anisotropic shale.**
3. **Reading a splitting time as a fracture density.** It is an integrated
   product.
4. **Interpreting a microseismic cloud as a flow path.** It maps where rock
   slipped, in an assumed velocity model, with the error bars of §6.
5. **Predicting which fault will slip.** The governing quantities are the
   in-situ stress and fracture orientation.
6. **Assuming more sensors help.** Detection range, resolution and geometry
   each constrain different things; the budget must be computed.

## Related modules

- [11-03-03 Reservoir Characterisation and Property Prediction](03-reservoir-characterisation.md) —
  the elastic-property chain this lesson extends.
- [05-04-05 Anisotropy in Rocks: Causes and Magnitudes](../../05-core-geophysics/04-rock-physics/05-anisotropy-rock.md) —
  where $\varepsilon$, $\delta$ and $\gamma$ come from physically.
- [06-12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md) —
  mechanism, pore-pressure diffusion and mitigation.
- [11-03-06 Integrating Borehole Data with Seismic](06-borehole-and-integration.md) —
  where the anisotropic velocity model comes from.
- [11-04-03 Microseismic Monitoring of Geothermal Fields](../04-geothermal-exploration-geophysics/03-microseismic-geothermal.md) —
  the same monitoring physics applied to a different resource.

## Further reading

- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press. Level: textbook. Elastic
  moduli, anisotropy and their measurement.
- Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press. Level: textbook. Seismic anisotropy and shear-wave
  propagation.
- Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists. Level: reference. Anisotropy in processing and imaging.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.
