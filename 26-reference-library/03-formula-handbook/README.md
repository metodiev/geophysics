# Module 26-03 — Formula Handbook

**Stages:** intermediate → graduate · **Prerequisites:** none (lookup resource)

Seven formula sheets, one per subject area. They are compact by design: a table
of formulas, the conditions attached to each, and — for every sheet — a small
print-only script that evaluates a few of the entries so that the algebra in the
sheet is checked against arithmetic rather than trusted.

The organising rule of this module is that **a formula without its assumptions is
a trap**. Every row carries either an explicit condition or a note on the regime
in which it holds: isotropic versus anisotropic, small-strain, far-field,
diffusive versus propagative, geostrophic. Where a constant is conventionally
quoted in two different ways (the free-air gradient, for instance), the sheet
gives both values and explains the difference instead of choosing one silently.

The worked examples in each sheet quote numbers printed by the corresponding
script in `code/`. They are **SYNTHETIC** in the sense that the inputs are
chosen test values, not measurements; each script prints a provenance banner that
says so.

## Lessons

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Formula Sheet: Mathematics and Calculus](./01-formulas-mathematics.md) | intermediate | Series have radii of convergence; quadrature and difference schemes have orders |
| 02 | [Formula Sheet: Linear Algebra, SVD and Numerics](./02-formulas-linear-algebra-numerics.md) | advanced | A formula can be exact and numerically useless: conditioning, rank and stability |
| 03 | [Formula Sheet: Waves, Elasticity and Seismology](./03-formulas-waves-seismology.md) | advanced | Two independent elastic constants; ray parameter; amplitude versus energy reflection |
| 04 | [Formula Sheet: Gravity, Magnetics and Potential Theory](./04-formulas-potential-fields.md) | advanced | Shape formulas are model-dependent; reductions need a stated density |
| 05 | [Formula Sheet: Electromagnetics and Electrical Methods](./05-formulas-em-electrical.md) | advanced | Diffusion versus propagation; apparent resistivity is not a material property |
| 06 | [Formula Sheet: Inverse Theory and Statistics](./06-formulas-inverse-statistics.md) | advanced | Resolution and variance trade off; $\chi^{2}/\text{dof}$ is evidence about your errors |
| 07 | [Formula Sheet: Atmosphere, Radiation and Ocean](./07-formulas-atmosphere-ocean.md) | graduate | Every balance has a small parameter; radiation laws are geometric |

## How to use this module

1. Find the formula in the sheet for the subject.
2. Read the **conditions** column before evaluating anything.
3. If the entry has a worked example, run the script and compare your own
   arithmetic with the printed values — this catches unit and convention slips
   that reading cannot.
4. For anything being published, take constants from the responsible body's
   current release rather than from this sheet (see
   [26-02-03](../02-symbols-and-units/03-constant-handbook.md)).

## Verification scripts

| Script | Checks | Runtime |
|---|---|---|
| [`code/formulas_mathematics_demo.py`](./code/formulas_mathematics_demo.py) | quadrature orders, difference errors, series truncation, $\nabla^{2}(1/r)$ | < 1 s |
| [`code/formulas_linear_algebra_demo.py`](./code/formulas_linear_algebra_demo.py) | SVD and condition number, three least-squares routes, damping trade-off, eigen invariants | < 1 s |
| [`code/formulas_waves_seismology_demo.py`](./code/formulas_waves_seismology_demo.py) | moduli conversion with back-substitution, Snell, impedance, NMO, dispersion, $M_w$ | < 1 s |
| [`code/formulas_potential_fields_demo.py`](./code/formulas_potential_fields_demo.py) | Bouguer slab, both free-air gradients, sphere anomaly, continuation, dipole $1/r^{3}$ | < 1 s |
| [`code/formulas_em_electrical_demo.py`](./code/formulas_em_electrical_demo.py) | skin depth, MT half-space identity, array factors, GPR, sphere $\tau$, loop field | < 1 s |
| [`code/formulas_inverse_statistics_demo.py`](./code/formulas_inverse_statistics_demo.py) | weighted mean, covariance propagation, damping, Monte Carlo, resolution matrix | < 2 s |
| [`code/formulas_atmosphere_ocean_demo.py`](./code/formulas_atmosphere_ocean_demo.py) | potential temperature, Coriolis, geostrophy, radiation, optical depth | < 1 s |

All seven are print-only, use `np.random.default_rng(20261014)` wherever a
random number is needed, write no files and exit 0.

## How to run the verification scripts

```bash
.venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_mathematics_demo.py
.venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_linear_algebra_demo.py
.venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_waves_seismology_demo.py
.venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_potential_fields_demo.py
.venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_em_electrical_demo.py
.venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_inverse_statistics_demo.py
.venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_atmosphere_ocean_demo.py
```

## Mastery checkpoint

This module has no checkpoint — it is a reference. The skill it supports is
**checking a formula's conditions before using it**, and running a two-minute
numerical check of any formula whose sign or factor you are unsure of.

## Common pitfalls across this module

1. **Dropped conditions.** Using a small-offset, small-angle or small-strain
   formula outside its regime is the single most common error in every sheet.
2. **Amplitude versus energy.** Reflection coefficients quoted as amplitudes and
   as energies differ by a square; check which convention a source uses.
3. **Conventions.** Fourier signs, $z$-positive directions and magnetic field
   symbols differ between subfields; each sheet states this repository's choice.
4. **Numerical naivety.** The normal equations, downward continuation and
   undamped inversion are all correct and all unstable; prefer the stable
   formulations given in the sheets.
5. **Quoting a constant from a formula sheet.** Free-air gradients, sound speed
   and equation-of-state coefficients are all sources of silent bias; use the
   responsible body's release.

## Related modules

- [26-01 Glossary of Geophysical Terms](../01-glossary/README.md) — the words these formulas name.
- [26-02 Symbols, Units and Conventions](../02-symbols-and-units/README.md) — symbols, units, constants and dimensional checks.
- [26-04 Annotated Textbook Bibliography](../04-textbook-bibliography/README.md) — where each of these derivations is done properly.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the taught treatment behind sheet 06.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — discretisation, stability and solver detail behind sheet 02.
