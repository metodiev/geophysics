# Module 05-09 — Geothermal and Heat-Flow Methods

**Stages:** advanced → graduate · **Prerequisites:**
[02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
for the governing equation and the diffusion timescales, and
[05-08-02 Natural Gamma and Spectral Gamma Logging](../08-geophysical-logging/02-gamma-logging.md)
for the radiogenic heat production that enters every geotherm.

This module is about the one geophysical quantity that is a **product of two
measurements**:

$$q = k\,\frac{\mathrm{d}T}{\mathrm{d}z},$$

thermal conductivity times the vertical temperature gradient. Everything awkward
about the subject follows from that structure. Both factors are measured
separately; both have their own systematic errors; and the temperature factor is
measured in a hole that **drilling has just disturbed**.

Two disciplines run through the module:

- **Get the sign convention and the vertical coordinate fixed before any number is
  written.** With depth positive downward, $\mathrm{d}T/\mathrm{d}z > 0$ and heat
  flows upward; the reported heat flow is the upward magnitude,
  $q = +k\,\mathrm{d}T/\mathrm{d}z$. This is the single commonest error in the
  topic, and it is a convention error rather than a physics error.
- **Distinguish clearly what is measured from what is assumed.** The module's
  demonstrations compute every number they quote. Where a quantity is a literature
  *range* it is given as a range; where it is a chosen parameter it is labelled
  SYNTHETIC; and the one place where a remembered constant appears — the critical
  Rayleigh numbers — is a place where the demonstration **re-derives** them
  numerically and reports the agreement.

## Learning objectives

By the end of this module you will be able to:

1. **State** the sign convention, derive $q = k\,\mathrm{d}T/\mathrm{d}z$, and use
   flux continuity across a conductivity contrast as the primary check on a
   heat-flow profile.
2. **Quantify** the drilling disturbance with a line-source relaxation model and
   state the heat-flow bias at a given elapsed time.
3. **Demonstrate** the non-uniqueness of a ground-surface-temperature
   reconstruction, and report a family of histories rather than one curve.
4. **Distinguish** conductivity from diffusivity, and derive both mixing orders for
   a layered rock without interchanging them.
5. **Recover** a conductivity by a steady-state and by a transient method, with the
   fitting window and the error sources stated.
6. **Build** a geothermal exploration argument that separates heat, fluid and
   permeability, and state which of the three the geophysics does not measure.

## Lesson map

| # | Lesson | Core content |
|---|---|---|
| 01 | [Measuring Terrestrial Heat Flow](./01-heat-flow-measurement.md) | The sign convention, flux continuity measured across a 2:1 conductivity contrast (gradient halves, flux identical), the drilling disturbance (41.67 per cent bias at 1 h, 0.69 per cent at 5 days), and two GST histories that differ by 0.06 K at 300 m and 0.003 K at 500 m — a measured demonstration of non-uniqueness. |
| 02 | [Thermal Conductivity Measurement and Corrections](./02-thermal-conductivity.md) | Conductivity versus diffusivity; the series (harmonic, 2.4138) and parallel (arithmetic, 2.7600) means measured on one stack, with anisotropy growing faster than contrast (3.03 for 10:1); divided-bar and needle-probe recovery, including the 22.5 per cent bias from a badly chosen fitting window. |
| 03 | [Geothermal Exploration Geophysics](./03-geothermal-exploration.md) | Heat, fluid and permeability as three separate requirements; the clay-cap model; heat in place computed and explicitly not treated as a resource; geotherms with the radiogenic partition measured; and the critical Rayleigh numbers **re-derived numerically** — free-slip 657.5110 against $27\pi^4/4 = 657.5114$, rigid 1707.7616 against the reference 1707.762. |

## What every lesson enforces

- **The convention is stated before the first equation.** Depth positive downward;
  $q$ the upward magnitude; conductivity orientation named.
- **Every quoted number is computed by a script in `code/`**, with its grid size,
  sample count or convergence order reported instead of a wall-clock time.
- **Every parameter that is not measured is labelled SYNTHETIC**, with its value
  shown, and where a quantity is only known as a range the range is given.
- **The one remembered constant pair is re-derived** and the caveat about the
  numerical method's own limits is stated rather than hidden.

## How to run the demonstrations

All scripts run offline under the repository virtual environment, use `numpy` and
`scipy` only, print labelled results with units, exit 0, and use
`np.random.default_rng(seed)` where randomness is involved.

```bash
cd 05-core-geophysics/09-geothermal-and-heat-flow-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python heatflow_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermal_cond_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geothermal_demo.py
```

| Script | What it measures |
|---|---|
| `heatflow_demo.py` | Flux continuity across a conductivity contrast; the line-source disturbance decay and the resulting heat-flow bias versus elapsed time; two GST histories propagated to the present day |
| `thermal_cond_demo.py` | Both mixing means and the geometric mean on one layer stack; anisotropy versus contrast; a divided bar with its thermometry error budget; needle-probe fits over five windows |
| `geothermal_demo.py` | The critical Rayleigh numbers by Chebyshev collocation with row-replacement boundary conditions, minimised over wavenumber (free-slip and rigid); geotherms with a radiogenic source and the mantle partition; a Nusselt scaling with its chosen coefficient flagged |

## Exercises and solutions

Every lesson has an exercise set and a solution set under [`exercises/`](./exercises/),
graded ★ foundational, ★★ applied and ★★★ research-oriented, with solutions quoting
the demonstrations' measured numbers.

| Lesson | Exercises | Solutions |
|---|---|---|
| 01 | [`exercises/01-heat-flow-measurement-exercises.md`](./exercises/01-heat-flow-measurement-exercises.md) | [`exercises/01-heat-flow-measurement-solutions.md`](./exercises/01-heat-flow-measurement-solutions.md) |
| 02 | [`exercises/02-thermal-conductivity-exercises.md`](./exercises/02-thermal-conductivity-exercises.md) | [`exercises/02-thermal-conductivity-solutions.md`](./exercises/02-thermal-conductivity-solutions.md) |
| 03 | [`exercises/03-geothermal-exploration-exercises.md`](./exercises/03-geothermal-exploration-exercises.md) | [`exercises/03-geothermal-exploration-solutions.md`](./exercises/03-geothermal-exploration-solutions.md) |

## Where this module sits

It closes folder 05 by taking the borehole measurements of
[05-08 Geophysical Logging](../08-geophysical-logging/README.md) — temperature,
gamma spectrometry for heat production — and turning them into a geophysical
quantity with its own measurement discipline. It follows
[05-07 Interpretation and Integration](../07-interpretation-and-integration/README.md)
for the uncertainty-reporting framework, and it hands off to
[12-03 Geotherms and the Heat Budget](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/README.md)
for the global picture, to
[11-04 Geothermal Exploration Geophysics](../../11-exploration-geophysics/04-geothermal-exploration-geophysics/README.md)
for the exploration methods in detail, and to
[13-02 Mantle Convection](../../13-geodynamics-tectonics/02-mantle-convection/README.md)
for the convective physics whose critical numbers are re-derived here.

## Self-assessment for the module

- [ ] I can state the sign convention and write $q$ for either choice of the
      direction of $z$.
- [ ] I can check a heat-flow profile for flux continuity and identify the
      conductivity error that breaks it.
- [ ] I can compute the drilling disturbance and the heat-flow bias it causes.
- [ ] I can demonstrate the non-uniqueness of a GST reconstruction and report a
      family of histories.
- [ ] I can derive both mixing orders and say which is which, without hesitating.
- [ ] I can recover a conductivity by two methods and state each method's error
      budget.
- [ ] I can build a geothermal exploration argument that does not confuse heat with
      permeability.
- [ ] I can state exactly which numbers in my answer are measured, which are
      assumed, and which are scaling estimates.
