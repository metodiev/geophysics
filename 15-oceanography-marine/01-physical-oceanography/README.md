# Module 15-01 — Physical Oceanography

**Stages:** intermediate → research · **Prerequisites:** modules 02-06 (fluid
mechanics), 02-05 (thermodynamics) and 02-03 (waves and dispersion); comfort with
least-squares fitting and with units.

> **All models and data in this module are SYNTHETIC.** Every equation-of-state
> coefficient, wind-stress field, box-model parameter, stratification profile,
> tidal amplitude and oscillator coefficient in these lessons is a chosen
> teaching value, printed by a demonstration in `code/`. No tide gauge, mooring,
> cruise, satellite product, reanalysis or published measurement is reproduced.
> Physical constants ($g$, $\Omega$, $G$, $\rho_{\text{air}}$, $c_p$, $L_v$) and
> conventional astronomical values (the M2 period) are stated with units and are
> used as standard constants.

Physical oceanography is a subject in which almost nothing that matters is
measured directly. Density — the variable that drives every current — is computed
from temperature, salinity and pressure through an equation of state whose
coefficients are themselves fitted. Transports of tens of Sverdrups are inferred
from a balance of terms. Mixing rates are obtained from a measured dissipation
divided by a stratification and multiplied by a mixing efficiency that no
measurement determines. Sea-level trends contain the vertical motion of the
land the gauge is bolted to.

That is not a defect; it is the subject. This module is organised around the
consequence: **every number in these lessons is either printed by a
demonstration, or an exact standard constant, and every inference is stated as an
inference.** Where a model has a trade-off, the module quantifies it rather than
asserting it: 4.5 °C of cooling per g kg$^{-1}$ of salinity in the density
sensitivity, a factor 3.1 of spurious stability from using in-situ density, a
factor 60 variation of $N$ over 1.5 km, a fold in the freshwater forcing at
$0.0586\ \mathrm{(g\,kg^{-1})\,yr^{-1}}$ in a two-box model, a factor 2.6 spread
in the thermocline response between two coupled oscillators with the same period.
A caveat without a size is not a caveat.

The third discipline of the module is that **model and measurement are kept
apart in writing**. A two-box model can have two stable states; the real ocean's
threshold is not in those boxes. A recharge oscillator can be tuned to a
four-year period; that period is an input, not a prediction. Where a lesson
crosses from one to the other, it says so in the sentence where the crossing
happens.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** density from a stated equation of state, derive $\alpha$ and
   $\beta$, and **quantify** the error of a linear equation of state over a
   stated range.
2. **Explain** why in-situ density may not be differenced for a stability test,
   and **compute** the spurious $N^{2}$ that results when it is.
3. **Derive** the Ekman transport, the Sverdrup balance and the western-boundary
   scales from the depth-integrated momentum and vorticity equations, and
   **evaluate** each with units.
4. **Formulate** a two-box buoyancy-driven model, **find all** of its steady
   states, and **locate** a saddle-node bifurcation numerically.
5. **Derive** the internal-wave dispersion relation, **solve** the vertical-mode
   eigenproblem for a structured $N(z)$, and **compute** a characteristic slope
   and criticality.
6. **Set up** harmonic analysis as least squares, **diagnose** a nearly singular
   design from its condition number, and **compute** an alias frequency.
7. **Derive** the eigenvalues of a two-variable coupled oscillator and
   **distinguish** its deterministic period from the peak of its forced response.

## Prerequisites

- [02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) —
  continuity, momentum, vorticity and the closure problem.
- [02-05 Thermodynamics](../../02-physics/05-thermodynamics/README.md) —
  heat conduction and the diffusion equation used for the thermocline.
- [02-03 Oscillations and Waves](../../02-physics/03-oscillations-and-waves/README.md) —
  dispersion relations, superposition and interference.
- [02-08 Potential Theory](../../02-physics/08-potential-theory/README.md) —
  the Legendre expansion behind the tidal potential.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Seawater Properties: Temperature, Salinity, Density](01-seawater-properties.md) | intermediate | Density is computed, not measured; compression dominates the vertical gradient, and cabbeling is invisible to a linear equation of state |
| 02 | [Wind-Driven Circulation, Ekman Transport and Gyres](02-wind-driven-circulation.md) | advanced | Transport is perpendicular to the wind and independent of the viscosity; the gyre's return flow is a western boundary layer |
| 03 | [Thermohaline Circulation and Deep Water Formation](03-thermohaline-circulation.md) | doctoral | A prescribed freshwater flux gives a circulation more than one stable state, and a fold whose position is a property of the model |
| 04 | [Internal Waves, Tides and Mixing](04-internal-waves-and-tides.md) | doctoral | The ocean's interior is a moving, anisotropic medium; the diffusivity everyone uses is a closure, not a measurement |
| 05 | [Sea Level, Tides and Harmonic Analysis](05-sea-level-and-tides.md) | advanced | Harmonic analysis is least squares on a designed matrix, and the design's conditioning is the answer to "how long a record do I need?" |
| 06 | [Ocean-Atmosphere Coupling and ENSO](06-ocean-atmosphere-coupling.md) | doctoral | A coupled mode is a property of the pair; a broad spectral peak estimated from a finite record scatters by 11 % |

## Suggested path

**If you are new to the ocean:** lessons 01, 02, 05 in order, running each
demonstration and checking the printed numbers against your own hand
calculations. Lesson 01 supplies the equation of state that everything else
consumes; lesson 05 is the only lesson built around a measurement technique you
could operate yourself.

**If you already know the classical balances:** read 01 §3 (why potential
density), then 03 and 04 — the two lessons where the difficulty is a closure
rather than an algebra, and where the module's honesty conventions are most
visible.

**If you are preparing a research project:** 03 §3–5 (multiple equilibria and the
trace identity), 04 §4–7 (modes, criticality, the Osborn closure) and the ★★★
exercises in each companion set, which are written as measurement designs rather
than as algebra.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-seawater-properties.md`](01-seawater-properties.md) | Lesson 01 |
| [`02-wind-driven-circulation.md`](02-wind-driven-circulation.md) | Lesson 02 |
| [`03-thermohaline-circulation.md`](03-thermohaline-circulation.md) | Lesson 03 |
| [`04-internal-waves-and-tides.md`](04-internal-waves-and-tides.md) | Lesson 04 |
| [`05-sea-level-and-tides.md`](05-sea-level-and-tides.md) | Lesson 05 |
| [`06-ocean-atmosphere-coupling.md`](06-ocean-atmosphere-coupling.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations, one per lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 15-oceanography-marine/01-physical-oceanography/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seawater_properties_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python wind_driven_circulation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermohaline_circulation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python internal_waves_tides_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sea_level_tides_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ocean_atmosphere_coupling_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0. They
are print-only — no plots are produced — so the output can be compared line by
line with the tables in the lessons. All six run in under ten seconds in total;
the thermohaline demo is the slowest at about six seconds.

## Mastery checkpoint

Complete this without notes:

> A synthetic station has surface water at $T = 22\ ^\circ$C,
> $S = 35.80\ \mathrm{g\,kg^{-1}}$ and 1000 m water at $T = 6\ ^\circ$C,
> $S = 35.00\ \mathrm{g\,kg^{-1}}$, over a column where the wind stress is
> $0.10\ \mathrm{N\,m^{-2}}$ eastward at $30^\circ$N. **(a)** Compute $\sigma_t$ at
> both levels and $N^{2}$ from the pair, stating your sign convention. **(b)**
> Compute the meridional Ekman transport and its direction. **(c)** Compute
> $\mathrm{curl}_z\tau$ for a zonal stress $\tau_x(y) = 0.10\cos(\pi y/3000\
> \mathrm{km})$ at $y = 750\ \mathrm{km}$ and the resulting Sverdrup transport.
> **(d)** State one number that quantifies the cost of using in-situ rather than
> potential density, and one that quantifies a linear equation of state's error.

Worked versions of (a)–(c) appear in the lesson-01 and lesson-02 solutions
([01](exercises/01-seawater-properties-solutions.md),
[02](exercises/02-wind-driven-circulation-solutions.md)).

## Common pitfalls across this module

1. **Differencing in-situ density for stability.** The compression term is
   $1.77\,\%$ of the density at 4000 m — larger than any $T$ or $S$ contrast —
   and it inflates the apparent stability by a factor 3.1 in the lesson's example.
2. **Writing $N^{2}$ with the sign from height coordinates.** With $z$ positive
   downward, $N^{2} = +(g/\rho_0)\partial\rho_\theta/\partial z$.
3. **Quoting a depth, or a transport, without its assumption.** Every one of
   these lessons produces conditional answers: a depth depends on a velocity, a
   heat transport on a temperature contrast, a diffusivity on a mixing
   efficiency, a period on an imposed coefficient.
4. **Treating a closure as a property.** $A_v$, $A_H$, $\kappa$ and $\Gamma$ are
   parameterisations. Where a result depends on one, the dependence is stated.
5. **Reading a spectral peak as an eigenfrequency.** Section 6 of lesson 06
   measures the difference (at most $1.5\,\%$ here) and the scatter of a
   finite-record estimate ($\pm11\,\%$), and reports both.
6. **Exporting a model's threshold to the ocean.** The freshwater threshold of
   lesson 03 is a property of chosen coefficients; only the *structure* — the
   fold and its hysteresis — transfers.
7. **Sampling a tide once a day.** M2 aliases to 14.77 days, which is
   indistinguishable from the genuine spring–neap cycle.

## Related modules

- [Module 15-02 Marine Geophysical Methods](../02-marine-geophysics-methods/README.md) —
  the instruments that measure the ocean's depth, its sub-surface structure and
  its gravity field, sharing the sound-speed and resolution logic of lesson 04.
- [Module 15-03 Seafloor Tectonics and Structure](../03-seafloor-tectonics/README.md) —
  what lies beneath the water column this module describes.
- [Module 15-06 Sea Level Change and Marine Records](../06-sea-level-change-marine/README.md) —
  the trend, the datum and the land motion that lesson 05 deliberately leaves alone.
- [02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) —
  the continuum equations these lessons apply.
- [06-02 Ray Theory and Travel Times](../../06-seismology/02-ray-theory-and-travel-times/README.md) —
  the same slowness geometry, used on seismic rather than internal waves.
- [13-02 Mantle Convection](../../13-geodynamics-tectonics/02-mantle-convection/README.md) —
  buoyancy against diffusion in a fluid 3000 times more viscous.
