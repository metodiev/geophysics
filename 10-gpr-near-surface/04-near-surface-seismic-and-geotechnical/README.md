# Module 10-04 — Near-Surface Seismic and Geotechnical Methods

**Stages:** advanced → graduate · **Prerequisites:** modules 06-01 and 06-02;
basic geotechnical engineering concepts.

**All models and data in this module are SYNTHETIC.** No borehole, site, survey,
foundation or earthquake is described from measurement. The blow counts, cone
resistances, unit weights, velocity profiles, weathering depths, elevations,
datums, timing errors, shaking parameters and uncertainties are chosen teaching
values. The empirical relations that appear as relations (the liquefaction
screening procedure, the modulus-reduction form, the SPT and cone corrections, the
code site-class boundaries) are attributed in the lessons and labelled as
conventions or fits, and the numbers they produce here come from SYNTHETIC inputs.
The only non-chosen numbers are physical constants
($g = 9.80665\ \mathrm{m\,s^{-2}}$ is a defined value, and the SI and standard
material constants are quoted as such).

This module is about the geotechnical **deliverable**, not about re-deriving
seismic theory. The refraction geometry, the surface-wave dispersion relation and
the site-response calculation already live in
[06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md);
what is added here is the chain from a measurement to a number an engineer will
build on — a shear-velocity profile for foundation design, a small-strain and an
operational stiffness, a code site class, a settlement estimate, a liquefaction
screening result, and a static correction that is good enough to image with. Each
link in that chain has its own status: some are exact algebra, some are conventions,
and some are empirical fits with scatter that has to be carried into the answer.

The organising question is therefore the one this whole folder asks, in engineering
clothes: **what is exact, what is a convention, and what is a correlation?** The
answers are unusually clear-cut here, and the lessons make them explicit. A shear
velocity from a travel time and a geometry is physical; $\rho V_s^2$ is exact given
$\rho$; $E = 2G(1+\nu)$ is exact given $\nu$; the modulus reduction at a design
strain is a modelled curve; a code site class is a decision boundary; a
liquefaction factor of safety is a screening index from an empirical resistance
curve. Mixing those categories is how a defensible measurement becomes an
indefensible prediction.

Three quantitative themes run through the module. First, **the geometry decides
what a velocity means**: the same ground gives $260\ \mathrm{m\,s^{-1}}$ from a
same-depth cross-hole pair and a *negative* interval velocity from a straight-ray
interpretation of a deeper receiver, because a diving ray through a faster layer
arrives early. Second, **the strain level decides the stiffness**: using
$G_{\max}$ where an operational modulus is required under-predicts settlement by a
factor of three to four. Third, **the near surface decides the image**: a wrong
weathering velocity of $10\%$ leaves the statics almost right and the weathering
depth $11\%$ wrong, so the error is silent in the product that is checked and loud
in the structure that is interpreted.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** the SPT corrections that turn a measured blow count into
   $(N_1)_{60}$, and **explain** why an index parameter and a stiffness are not
   interchangeable.
2. **Compute** net cone resistance, friction ratio and a soil behaviour-type index,
   and **state** the conventions the numbers depend on.
3. **Derive** the interval-velocity relation from the straight-ray assumption and
   **demonstrate** its failure where a ray crosses a velocity increase, including
   the unphysical negative velocity it can return.
4. **Quantify** the different effects of a constant trigger delay and a random
   trigger jitter on a borehole interval velocity, and **choose** a geometry and a
   receiver spacing that meet a stated accuracy.
5. **Construct** a shear-velocity profile from measurements with different
   resolutions, **compute** the $V_{S30}$ and the class it implies, and **report**
   the interval rather than a value.
6. **Convert** a velocity profile into $G_{\max}$ and into an operational modulus at
   a design strain, and **compute** the settlement each implies.
7. **Derive** the cyclic stress ratio from a peak shear-stress ratio, **compute**
   factors of safety against liquefaction by two routes, and **report** the
   probability rather than the point value.
8. **Compute** a weathering depth and a datum static, and **quantify** which error
   produces a structure error and which produces a resolution loss.
9. **Derive** the stack response to systematic and random statics, **prove** the
   one-dimensional null space of the surface-consistent decomposition, and
   **state** what must be measured outside the reflection data.

## Prerequisites

- [06-01 Elastic Wave Propagation](../../06-seismology/01-elastic-wave-propagation/README.md)
  — the shear modulus, the shear speed and Poisson's ratio.
- [06-02 Ray Theory and Travel Times](../../06-seismology/02-ray-theory-and-travel-times/README.md)
  — Snell's law, head waves and travel-time curves.
- [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md)
  — the refraction, MASW and site-characterisation theory this module applies.
- [10-01 GPR Principles](../01-gpr-principles/README.md) — the complementary
  shallow measurement, and the calibration discipline reused here for velocity.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole](01-spt-cpt-crosshole.md) | advanced | An index is not a stiffness, and geometry decides whether a travel time gives a layer velocity |
| 02 | [Shear-Wave Velocity Modelling and Site Classification](02-shear-wave-velocity-modelling.md) | graduate | A profile is a construction; stiffness is exact, the operational modulus is a strain choice, and screening is probabilistic |
| 03 | [Near-Surface Refraction for Static Corrections](03-refraction-static.md) | graduate | A static error is a structure error; the depth is far more sensitive to the weathering velocity than the static is |

## Suggested path

**If you are new to geotechnical geophysics:** lesson 01 first — the four
measurements and what each one actually constrains — then 02, which builds the
engineering numbers on top of them.

**If you work in site investigation or foundation design:** 02 §3.3–3.5 (modulus
reduction, settlement and liquefaction screening) is the core; read 01 §3.3–3.5 for
the geometry and timing errors that decide whether the input velocity is right.

**If you work in seismic processing:** lesson 03, and 01 §3.5 for the timing
discipline that a statics solution depends on. The statics lesson is deliberately
about the error budget rather than about deriving refraction depths, which is
[06-10-02](../../06-seismology/10-refraction-and-near-surface-seismology/02-plus-minus-method.md)'s
subject.

**If you are preparing a research project:** 01 §3.3 (the straight-ray failure),
02 §3.5 and the two-route disagreement, 03 §3.4–3.5 (the null space and the
structure trade), plus the exercises at ★★★ level.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-spt-cpt-crosshole.md`](01-spt-cpt-crosshole.md) | Lesson 01 |
| [`02-shear-wave-velocity-modelling.md`](02-shear-wave-velocity-modelling.md) | Lesson 02 |
| [`03-refraction-static.md`](03-refraction-static.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and Matplotlib:

```bash
cd 10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spt_cpt_crosshole_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python shear_wave_velocity_modelling_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python refraction_static_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits $0$.
They are print-only: no figures are produced and no file is written.

| Demo | Lesson | What it computes |
|---|---|---|
| `spt_cpt_crosshole_demo.py` | 01 | SPT energy-ratio and overburden corrections, cone indices, cross-hole exact arrival times and the straight-ray interval velocity in two geometries, down-hole interval velocities with a constant offset and with jitter, $G_{\max}$ and $E$ |
| `shear_wave_velocity_modelling_demo.py` | 02 | three profiles and the $V_{S30}$ each implies, site classes and margins, $G_{\max}$ and modulus reduction, two settlements, the liquefaction screening table by two routes, and two Monte Carlos (class probability and factor-of-safety distribution) |
| `refraction_static_demo.py` | 03 | the weathering depth and its sensitivity, datum statics for a line, the analytic stack response verified against a direct spectral stack, the surface-consistent null space, and the depth-error versus static-error comparison |

## Mastery checkpoint

Complete this without notes. All values are SYNTHETIC.

> A site is a $12\ \mathrm{m}$ sand profile over a stiff layer, water table at
> $3.0\ \mathrm{m}$, $\gamma = 18\ \mathrm{kN\,m^{-3}}$ above and
> $20\ \mathrm{kN\,m^{-3}}$ below. An SPT at $6.0\ \mathrm{m}$ gives $N = 14$ with
> $ER = 60\%$; a same-depth cross-hole pair $5.0\ \mathrm{m}$ apart at $6.0\
\mathrm{m}$ gives a first arrival at $12.5\ \mathrm{ms}$; and a refraction survey
finds $v_w = 600\ \mathrm{m\,s^{-1}}$ over $v_r = 2000\ \mathrm{m\,s^{-1}}$ with an
intercept time of $14.0\ \mathrm{ms}$. **(a)** Compute $\sigma_v$, $\sigma'_v$,
$N_{60}$, $(N_1)_{60}$ at $6.0\ \mathrm{m}$. **(b)** Compute $V_s$ from the
cross-hole pair, $G_{\max}$ for $\rho = 1900\ \mathrm{kg\,m^{-3}}$, and the
operational modulus at $\gamma = 10^{-3}$ with $\tau_{\max} = 45\ \mathrm{kPa}$.
**(c)** Compute the weathering depth from the intercept time, and the depth if
$v_w$ were really $660\ \mathrm{m\,s^{-1}}$. **(d)** State which of the three
numbers in (b) belongs in a settlement calculation at working load, and which in a
dynamic-response calculation. **(e)** State the single assumption that most limits
(a), (b) and (c), one each.

The methods are Sections 3.1–3.5 of lesson 01, Sections 3.1–3.4 of lesson 02 and
Section 3.1 of lesson 03; each answer is a substitution into one of those formulas,
and the sensitivities quoted in the lessons ($G \propto V_s^2$,
$\mathrm{d}z/\mathrm{d}v_w = 7.2\times10^{-3}\ \mathrm{m}$ per m/s at these
velocities) give the error terms without any new algebra.

## Common pitfalls across this module

1. **Reporting an index as a property.** A blow count and a cone resistance are
   responses; a shear velocity is a property. Correlations between them are
   empirical and carry the scatter (lessons 01, 02).
2. **Applying the straight-ray interval formula in layered ground.** It returns
   $-120.2\ \mathrm{m\,s^{-1}}$ in the demonstration's model (lesson 01).
3. **Blaming the trigger for everything.** A constant trigger delay cancels exactly
   in an interval velocity; only the random part matters (lesson 01).
4. **Averaging velocities arithmetically.** $V_{S30}$ is $30/\sum(h/V_s)$, and the
   slow layers dominate it (lesson 02).
5. **Quoting one $V_{S30}$.** Three defensible constructions of one site differ by
   $28.5\%$ and fall in different code classes (lesson 02).
6. **Using $G_{\max}$ as the design modulus.** The settlement differs by a factor of
   $2.9$ to $4.2$ at working strain (lesson 02).
7. **Reporting a factor of safety without its distribution.** $0.96 \pm 0.39$,
   $P(FS<1) = 0.64$ (lesson 02).
8. **Trusting the stack to reveal a statics error.** A $10\%$ weathering-velocity
   error costs $11.5\%$ of the weathering depth and $0.02\%$ of the $40\ \mathrm{Hz}$
   amplitude (lesson 03).

## Related modules

- [10-01 GPR Principles](../01-gpr-principles/README.md) and
  [10-03 GPR Applications](../03-gpr-applications/README.md) — the electromagnetic
  near-surface measurement that gives moisture where this module gives stiffness.
- [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md)
  — the refraction, MASW and site-response theory that this module turns into
  deliverables.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md)
  — where the shaking parameters of a liquefaction screening come from, and with
  what probability.
- [10-05 Other Near-Surface Methods](../05-other-near-surface-methods/README.md) —
  EMI, surface waves, thermal and nuclear methods, and how to combine them.
- [10-06 Near-Surface Monitoring and Time-Lapse](../06-nearsurface-monitoring/README.md)
  — repeating these measurements to watch a dam, an embankment or a foundation.
- [11-06 Geotechnical and Engineering Exploration](../../11-exploration-geophysics/06-geotechnical-and-engineering/README.md)
  — the same methods at the scale of tunnels, dams and large foundations.
