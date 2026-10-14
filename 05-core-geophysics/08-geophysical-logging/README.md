# Module 05-08 — Geophysical Logging

**Stages:** advanced → graduate · **Prerequisites:**
[05-07-04 Ground Truthing: Boreholes, Outcrop and Drill Core](../07-interpretation-and-integration/04-ground-truthing.md)
for the role a borehole plays in testing a geophysical model, and
[05-04-01 Porosity, Density and Velocity Relationships](../04-rock-physics/01-porosity-density-velocity.md)
for the rock-physics relations that connect a log reading to a rock property.

This module is about the measurement whose "field" is a **depth profile** rather
than a map. Everything changes when the observation point is inside the medium:

- **The borehole is part of the measurement.** A hole drilled, filled with fluid and
  held at a pressure different from the pore pressure perturbs the rock it is
  measuring. Invasion, hole enlargement, mudcake, temperature and stress release are
  not corrections applied at the end; they are the physics.
- **The volume of investigation is decimetres.** A log samples a cylinder of order
  metres along the hole and a few decimetres into the formation, which is four
  orders of magnitude smaller than what a surface survey resolves. This is the
  module's central scale statement.
- **No log measures a rock property.** Each measures a field — a count rate, a
  density, a slowness, a conductivity, a relaxation time — and the conversion to
  porosity, saturation or lithology is a model with named constants.

The module therefore repeats one discipline in seven forms: state the physical
measurement, state the volume of investigation, state the units, state the model and
its constants, and state the uncertainty.

## Learning objectives

By the end of this module you will be able to:

1. **Describe** the borehole environment and solve the invasion problem, including
   why the front is *not* $\sqrt{t}$ in a cylindrical hole.
2. **State** what each of the gamma, density, neutron, sonic, resistivity, NMR and
   imaging measurements physically is, and its volume of investigation.
3. **Apply** the environmental corrections, and say what each corrects and what
   happens if it is omitted.
4. **Forward-model** a synthetic well from rock physics, invert it, and identify
   which recovered parameters are measurement and which are assumption.
5. **Tie** a well to seismic, including the velocity-to-depth relation and its
   dominant error.
6. **Produce** a petrophysical interpretation with a Monte Carlo uncertainty budget
   and a ranked list of what to fix first.

## Lesson map

| # | Lesson | Core content |
|---|---|---|
| 01 | [The Borehole Environment and Invasion Profiles](./01-borehole-environment.md) | Drilling disturbance, overbalance and mudcake, radial invasion solved numerically (planar exponent 0.500 validated; cylindrical 0.18–0.22 measured), tool weighting functions, the six environmental corrections, $R_w$ versus $R_{mf}$, and the invasion correction that works on a step profile and fails on a smooth one. |
| 02 | [Natural Gamma and Spectral Gamma Logging](./02-gamma-logging.md) | The volume of investigation derived ($d_{90} = 2.303\lambda$: 23 cm for $\lambda = 10$ cm), thin-bed attenuation measured (0.5 m bed loses 53.5 per cent), and radiogenic heat production **derived** from isotope abundance, half-life and decay energy, checked against the conventional coefficients (3.7–8.2 per cent). |
| 03 | [Resistivity, Induction and Laterolog Tools](./03-resistivity-logging.md) | Induction versus electrode physics, skin depth verified against the exact expression, conductivity-versus-resistivity averaging (5.8× difference at shallow weighting), and the saturation bias from invasion (+23.5 per cent, one-signed). |
| 04 | [Density, Neutron and Sonic Porosity Logs](./04-porosity-logs.md) | The four porosity measurements and why none is a porosity; density and neutron forward models with the gas effect derived; the slowness-to-time identity verified numerically; matrix and fluid assumption errors measured ($-86$ per cent and $+11$ per cent). |
| 05 | [Borehole Imaging, Dipmeter and Fracture Detection](./05-imaging-logs.md) | Dip and azimuth from the sinusoid (exact fit), the azimuthal aliasing rule $|m - P\,\mathrm{round}(m/P)|$ verified row by row, hole-deviation correction (one true dip spans 8.0°–52.0° in relative dip), fracture aperture as a calibration (1.7× spread). |
| 06 | [Vertical Seismic Profiling and Check Shots](./06-seismic-while-drilling.md) | Time–depth integration, interval velocities from check-shot differences with their precision argument, the 5 per cent-to-100 m depth error at 2 km, VSP geometry and the direct arrival (542 ms later at 250 m for a 1200 m offset). |
| 07 | [Log Interpretation, Petrophysics and Uncertainty](./07-log-interpretation.md) | The five-stage workflow with every constant named, a Monte Carlo budget ($S_w$ 90 per cent interval [0.307, 0.721] against a point estimate of 0.477, dominated by $m$), depth matching and the three depth scales, cement bond and flow logging, and four things logging cannot determine. |

## What every lesson enforces

- **Physical measurement first, name second.** No lesson says "the density log
  measures density" without stating that it measures Compton-scattered gamma
  attenuation.
- **Volume of investigation for every tool**, because tool specifications vary by
  manufacturer and vintage and are not quoted as universal.
- **Every parameter that is not measured is labelled SYNTHETIC**, with its value.
  Where a range is used, a range is given.
- **Every inversion is demonstrated forward-then-inverse** on a model whose answer
  is known, including a case where the inversion fails.

## How to run the demonstrations

All scripts run offline under the repository virtual environment, use `numpy` and
`scipy` only, print labelled results with units, exit 0, and use
`np.random.default_rng(seed)` where a random draw is involved. No wall-clock
timings are reported; grid sizes, sample counts, iteration counts and measured
convergence orders are given instead.

```bash
cd 05-core-geophysics/08-geophysical-logging/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python borehole_env_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gamma_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resistivity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python porosity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python imaging_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python vsp_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python petrophysics_demo.py
```

| Script | What it measures |
|---|---|
| `borehole_env_demo.py` | Crank–Nicolson radial diffusion validated on plane geometry (exponents 0.5058 and 0.4997) and applied to a borehole (0.1835 and 0.2229); shallow/deep tool ratios; the invasion correction succeeding on a step profile (8 per cent in $S_w$) and failing on a smooth one ($-98$ per cent in $R_t$) |
| `gamma_demo.py` | Volume of investigation; thin-bed attenuation for five thicknesses; specific heat production derived from decay data and compared with the conventional coefficients |
| `resistivity_demo.py` | Skin depth against the exact expression (0.06 per cent); both averaging rules on one invaded profile; the $S_w$ bias from invasion |
| `porosity_demo.py` | A five-layer synthetic well forward-modelled and inverted for three porosity logs; the gas crossover; the wrong-matrix cost; the slowness-to-time integral verified |
| `imaging_demo.py` | Sinusoid dip and azimuth; the azimuthal aliasing table with its folded-order column; the deviation correction; three aperture calibrations on one trace |
| `vsp_demo.py` | A layered time–depth model; check-shot interval velocities; the depth error from a wrong average velocity; straight-ray direct arrivals for an offset source |
| `petrophysics_demo.py` | The five-stage workflow at one depth; a 200 000-sample Monte Carlo of $S_w$; a ranked one-at-a-time budget |

## Exercises and solutions

Every lesson has an exercise set and a solution set under [`exercises/`](./exercises/),
graded ★ foundational, ★★ applied and ★★★ research-oriented, with the solutions
quoting the demonstrations' measured numbers.

| Lesson | Exercises | Solutions |
|---|---|---|
| 01 | [`exercises/01-borehole-environment-exercises.md`](./exercises/01-borehole-environment-exercises.md) | [`exercises/01-borehole-environment-solutions.md`](./exercises/01-borehole-environment-solutions.md) |
| 02 | [`exercises/02-gamma-logging-exercises.md`](./exercises/02-gamma-logging-exercises.md) | [`exercises/02-gamma-logging-solutions.md`](./exercises/02-gamma-logging-solutions.md) |
| 03 | [`exercises/03-resistivity-logging-exercises.md`](./exercises/03-resistivity-logging-exercises.md) | [`exercises/03-resistivity-logging-solutions.md`](./exercises/03-resistivity-logging-solutions.md) |
| 04 | [`exercises/04-porosity-logs-exercises.md`](./exercises/04-porosity-logs-exercises.md) | [`exercises/04-porosity-logs-solutions.md`](./exercises/04-porosity-logs-solutions.md) |
| 05 | [`exercises/05-imaging-logs-exercises.md`](./exercises/05-imaging-logs-exercises.md) | [`exercises/05-imaging-logs-solutions.md`](./exercises/05-imaging-logs-solutions.md) |
| 06 | [`exercises/06-seismic-while-drilling-exercises.md`](./exercises/06-seismic-while-drilling-exercises.md) | [`exercises/06-seismic-while-drilling-solutions.md`](./exercises/06-seismic-while-drilling-solutions.md) |
| 07 | [`exercises/07-log-interpretation-exercises.md`](./exercises/07-log-interpretation-exercises.md) | [`exercises/07-log-interpretation-solutions.md`](./exercises/07-log-interpretation-solutions.md) |

## Where this module sits

It follows [05-07 Interpretation and Integration](../07-interpretation-and-integration/README.md),
which establishes that a borehole is a validation experiment, and it supplies the
downhole measurements that module 07 uses as its ground truth. It precedes
[05-09 Geothermal and Heat-Flow Methods](../09-geothermal-and-heat-flow-methods/README.md),
which takes the radiogenic heat production of lesson 02 and the temperature
disturbance of lesson 01 as two of its inputs, and it feeds the petrophysical
content of [14-hydrology-hydrogeophysics/03-petrophysics-hydrology](../../14-hydrology-hydrogeophysics/03-petrophysics-hydrology/README.md)
and the completions work in
[11-exploration-geophysics](../../11-exploration-geophysics/README.md).

## Self-assessment for the module

- [ ] I can describe the borehole environment and say why invasion is not a
      $\sqrt{t}$ process in a hole.
- [ ] I can state the physical measurement, the volume of investigation and the
      limitations of each of the seven log families.
- [ ] I can apply each environmental correction and say what it corrects.
- [ ] I can build a synthetic log from rock physics and invert it, and I can name
      the case where the inversion fails.
- [ ] I can tie a well to seismic and state the dominant error in the tie.
- [ ] I can report a saturation as an interval with a ranked cause.
- [ ] I can name four things logging cannot determine, and say what would.
