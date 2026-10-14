# Module 10-03 — GPR Applications

**Stages:** advanced → research · **Prerequisites:** modules 10-01 and 10-02;
basic electromagnetism and signal processing.

**All models and data in this module are SYNTHETIC.** No field site, survey,
target, instrument, glacier, road or planetary radar measurement is used. The
material permittivities, thicknesses, moisture profiles, ionospheric densities and
detection thresholds are chosen teaching values, stated as such wherever they
appear. The only numbers that are not chosen are physical constants
($c = 0.299792458\ \mathrm{m\,ns^{-1}}$,
$Z_0 = 376.730313668\ \Omega$,
$\varepsilon_0 = 8.8541878128\times10^{-12}\ \mathrm{F\,m^{-1}}$), the standard
permittivity of liquid water ($80.1$ at $20\ ^\circ\mathrm{C}$) and the standard
permittivity and density of cold ice ($3.17$,
$917\ \mathrm{kg\,m^{-3}}$).

This module takes the same instrument through five applications and asks the same
question in each of them: **what does a two-way time and an amplitude actually
constrain, and what is left to a model?** The answer is different in each case,
and the difference is the content of the module. In hydrogeology the measurement
is a *moisture* measurement and the model is a mixing law, so the unknown porosity
enters every number. In glaciology the permittivity is known to a few per cent, so
the thickness is nearly a measurement — and the firn at the top of the column,
whose density is not known, is what a careless survey gets wrong. In archaeology
and utility mapping the target is usually a discrete scatterer, so geometry is
almost everything and the *aperture* of the profile decides the depth. In pavement
and concrete inspection the geometry is perfect and the permittivity is measured on
site with a metal plate, which makes it the most quantitative routine application
— and the thin-layer problem, in which one amplitude belongs to four different
thicknesses, is the sharpest illustration of non-uniqueness in the folder. In
planetary sounding every difficulty appears at once, with the surface itself as
the strongest competing reflector.

Two organising commitments run through the five lessons. The first is that **a
depth is always conditional on a velocity** and a moisture content on a porosity;
the lessons print the sensitivity of every reported number to its assumption rather
than appending a caveat. The second is that **non-uniqueness is quantified, not
deplored**: a graded water table is priced in dB, a thin layer in millimetres of
ambiguous thickness, a planetary depth in an eleven-per-cent spread between two
models that fit the same two observations exactly.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** a soil's permittivity, speed and wavelength from its porosity and
   water content with a volumetric mixing model, and **quantify** the error an
   unknown porosity injects into the moisture inversion.
2. **Compute** the reflection coefficient of a wetting front, **show** that a
   graded contact of one wavelength removes most of the echo amplitude, and
   **explain** why contrast and transition thickness trade against each other.
3. **Convert** two-way times to depths in a layered column, and **report** the
   depth error that a single shallow velocity produces.
4. **Compute** the permittivity and speed of firn from its density, **derive** the
   constant-offset property of a firn correction, and **state** the conditions
   under which it cancels in a thickness but not in an absolute depth.
5. **Use** a surface echo as an absolute amplitude reference, and **convert** a
   calibrated bed amplitude into a reflection coefficient and a bed material.
6. **Derive** the diffraction hyperbola and its fitted form, and **quantify** how
   the aperture of a profile couples the recovered velocity to the recovered
   depth.
7. **Derive** the Rayleigh $a^3 f^2$ amplitude scaling, and **compute** the
   dynamic range that a target-size change demands.
8. **Derive** the exact three-layer slab response, **verify** it against the
   half-space limit, and **demonstrate** that a single amplitude belongs to
   several thicknesses.
9. **Derive** the metal plate calibration and **propagate** an amplitude error into
   a thickness error for a pavement layer.
10. **Compute** orbital range resolution, the Fresnel footprint, the
    clutter-equivalent off-nadir distance and the ionospheric group delay, and
    **decide** whether attenuation or clutter limits a sounding.

## Prerequisites

- [10-01 GPR Principles](../01-gpr-principles/README.md) — the low-loss speed,
  the reflection coefficient, the loss tangent, the resolution limits and the
  depth of investigation.
- [10-02 GPR Acquisition and Processing](../02-gpr-acquisition-and-processing/README.md)
  — survey design, gain, filtering, migration and velocity analysis.
- [02-07 Electromagnetism](../../02-physics/07-electromagnetism/README.md) — the
  Maxwell equations and plane waves in dielectrics and plasmas.
- [09-01 Electrical Properties of the Earth](../../09-electrical-em-methods/01-electrical-properties-of-earth/README.md)
  — conductivity, Archie's law and the pore-fluid control of the loss tangent.
- [03-01 Scientific Computing](../../03-scientific-computing/README.md) — NumPy
  and SciPy, which every demonstration uses.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [GPR for Soil Moisture, Water Table and Aquifer Structure](01-gpr-hydrogeology.md) | doctoral | The permittivity is a mixture property: moisture needs a porosity, and a depth needs a velocity profile |
| 02 | [GPR for Glacier Thickness and Internal Stratigraphy](02-gpr-glaciology.md) | doctoral | Ice is the easy medium and firn is the hard one; a firn correction cancels in a thickness but not in a depth |
| 03 | [GPR in Archaeology, Forensics and Buried Utilities](03-gpr-archaeology-forensics.md) | advanced | The hyperbola is geometry, the amplitude is contrast, and a short aperture makes velocity and depth one number |
| 04 | [GPR for Pavements, Concrete and Infrastructure Inspection](04-gpr-roads-concrete.md) | advanced | A metal plate converts an assumed permittivity into a measured one; below $\lambda/4$ an amplitude is not a thickness |
| 05 | [Planetary GPR: MARSIS, SHARAD and Lunar Radar](05-gpr-planetary.md) | research | The surface is the competitor; range resolution, clutter geometry and the ionosphere fix what a sounding can claim |

## Suggested path

**If you are new to the applications:** lessons 01 and 03 in order, running each
demonstration. Lesson 01 is where the moisture/porosity ambiguity appears; lesson
03 is where the velocity/depth coupling appears.

**If you work in engineering or infrastructure:** lesson 04 first (the calibration
and thin-layer results are the ones that reach a report), then 03 for the
hyperbola geometry and 01 for the moisture problem.

**If you work in glaciology or planetary science:** 02 then 05, in that order —
05 reuses 02's low-loss layer physics and adds the geometry and plasma that make
orbital sounding a different problem.

**If you are preparing a research project:** 01 §3.3–3.4 (the mixing-model and
graded-contact non-uniqueness), 04 §3.3 (the ill-posed thin-layer inversion),
05 §3.3–3.5 (clutter and dispersion), plus the exercises at ★★★ level.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-gpr-hydrogeology.md`](01-gpr-hydrogeology.md) | Lesson 01 |
| [`02-gpr-glaciology.md`](02-gpr-glaciology.md) | Lesson 02 |
| [`03-gpr-archaeology-forensics.md`](03-gpr-archaeology-forensics.md) | Lesson 03 |
| [`04-gpr-roads-concrete.md`](04-gpr-roads-concrete.md) | Lesson 04 |
| [`05-gpr-planetary.md`](05-gpr-planetary.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and Matplotlib:

```bash
cd 10-gpr-near-surface/03-gpr-applications/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_hydrogeology_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_glaciology_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_archaeology_forensics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_roads_concrete_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_planetary_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits $0$.
They are print-only: no figures are produced and no file is written.

| Demo | Lesson | What it computes |
|---|---|---|
| `gpr_hydrogeology_demo.py` | 01 | CRIM moisture and speed, the porosity sensitivity, a layered depth-conversion error, the graded-contact Born sum verified against the analytic sinc, exact versus low-loss attenuation, and a depth budget |
| `gpr_glaciology_demo.py` | 02 | firn density to permittivity, the depth conversion against assumed permittivity, bed coefficients referenced to the surface echo, $\lambda/4$ resolution, an Arrhenius absorption table, exact two-layer hyperbola fits, and isochrone thicknesses |
| `gpr_archaeology_forensics_demo.py` | 03 | a Monte Carlo hyperbola fit at two apertures, target reflection coefficients, the Rayleigh $a^3$ table, Fresnel radii, Kirchhoff migration at three velocities, and the linear velocity-to-depth error |
| `gpr_roads_concrete_demo.py` | 04 | thickness against assumed permittivity, the metal plate inversion with an exact round trip, the exact three-layer slab response with its $h \to 0$ check and its amplitude ambiguity, rebar cover from a Monte Carlo, multiples, and a thickness budget |
| `gpr_planetary_demo.py` | 05 | range resolution against bandwidth, the Fresnel footprint at orbital altitude, clutter geometry, two models with one observation, the plasma frequency and the ionospheric delay by two routes, and the attenuation-versus-clutter comparison |

## Mastery checkpoint

Complete this without notes. All values are SYNTHETIC.

> A $250\ \mathrm{MHz}$ survey crosses a dry sand profile of porosity $0.35$,
> measuring $\varepsilon_r = 8.0$ above a contact and $\varepsilon_r = 21.0$ below
> it, with the contact at a two-way time of $25.0\ \mathrm{ns}$. **(a)** Compute
> the water content in both layers from a CRIM mixing model with grain
> permittivity $5.0$, and the saturations. **(b)** Compute the reflection
> coefficient at the contact and express it in dB. **(c)** Convert the
> $25.0\ \mathrm{ns}$ to a depth using the upper-layer velocity, state the
> assumption that makes this the answer, and compute the depth error if the true
> upper-layer permittivity is $10\%$ lower. **(d)** A $1.5\ \mathrm{GHz}$ metal
> plate survey of a nearby pavement gives a surface reflection of $R_s = -0.36$ and
> a base reflection at $1.40\ \mathrm{ns}$; compute the permittivity and the layer
> thickness. **(e)** State, in one sentence each, the single assumption that most
> limits (a), (c) and (d).

The method for (a)–(c) is Sections 3.3–3.5 of lesson 01 and for (d) Section 3.2 of
lesson 04; each answer is a substitution into one of those formulas, and the
sensitivities quoted in the lessons ($\partial\theta/\partial\phi = 0.155$,
$\mathrm{d}h/h = -\mathrm{d}\varepsilon_r/(2\varepsilon_r)$) give the error terms
without any new algebra.

## Common pitfalls across this module

1. **Converting a time to a depth with one velocity.** The demonstration profiles
   show $+69.6\%$ and $+26.6\%$ errors from exactly this, and neither is visible
   in the section (lessons 01, 02).
2. **Reading an amplitude as a thickness or a material.** Below $\lambda/4$ one
   amplitude belongs to $12$, $30$, $50$ and $51\ \mathrm{mm}$; a graded
   water-table contact of a quarter wavelength loses $70\%$ of its echo
   (lessons 01, 04).
3. **Assuming the permittivity.** It is $37\%$ of a $70\ \mathrm{mm}$ layer's
   thickness in the plausible asphalt range; the metal plate exists because of
   that (lesson 04).
4. **Using a short aperture to fit a hyperbola.** Velocity and depth come out
   correlated at $+0.999$, and the depth inherits the velocity error in full
   (lesson 03).
5. **Treating the surface echo as clutter.** It is the one absolutely calibrated
   amplitude in the scene — the reference for a glacier bed and the calibration
   for a pavement (lessons 02, 04).
6. **Quoting a penetration or resolution figure without its regime.** Cold ice at
   $-40$ and $-5\ ^\circ\mathrm{C}$ differ by $57\times$ in absorption; a
   $1\ \mathrm{MHz}$ band resolves $84\ \mathrm{m}$ in ice (lessons 02, 05).
7. **Trusting a delay as proof of depth.** A subsurface echo at $100\ \mathrm{m}$
   and a surface echo from $10\ \mathrm{km}$ off nadir arrive at the same time
   (lesson 05).

## Related modules

- [10-01 GPR Principles](../01-gpr-principles/README.md) — the physics this module
  applies.
- [10-02 GPR Acquisition and Processing](../02-gpr-acquisition-and-processing/README.md)
  — how the data these lessons interpret are collected and processed.
- [10-04 Near-Surface Seismic and Geotechnical Methods](../04-near-surface-seismic-and-geotechnical/README.md)
  — the complementary measurement: seismic stiffness where GPR gives moisture,
  and the borehole ground truth both methods need.
- [10-05 Other Near-Surface Methods](../05-other-near-surface-methods/README.md) —
  EMI conductivity covers the salinity that defeats GPR; surface waves cover the
  stiffness that GPR cannot see.
- [10-06 Near-Surface Monitoring and Time-Lapse](../06-nearsurface-monitoring/README.md)
  — repeating any of these surveys to watch a process rather than a state.
- [11 Exploration Geophysics](../../11-exploration-geophysics/README.md) — the
  same methods at the scale of a basin rather than a site.
- [14 Hydrology and Hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md)
  — the hydrological and contaminant questions the moisture measurement serves.
