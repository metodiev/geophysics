# Module 09-02 — DC Resistivity Methods

**Stages:** intermediate → research · **Prerequisites:** module 09-01 and
electrostatics (module 02-07); basic least squares (module 18-02).

This module builds the DC resistivity method from one equation to a complete
inversion, and it refuses to skip the step where most of the information is lost.
The measurement itself is simple — two electrodes inject current, two measure a
voltage, a geometric factor converts the ratio into an apparent resistivity — and
that simplicity is exactly why the interpretation is so often over-claimed. The
lessons make the loss explicit at every stage: the geometric factor is exact only
over a uniform half-space; a DC array's sensitivity is half spent on the
unresolvable surface step; a thin layer's thickness and resistivity trade almost
exactly; a sounding cannot separate one model from a family; and an inversion
adds a penalty term whose choice changes the picture while leaving the misfit
unchanged.

The forward model is built *before* anything is inverted, and it is verified
against an independent solution: the two-layer image series and the layered
Bessel-integral recurrence agree to twelve digits, the half-space limit is exact,
and reciprocity is exact. The sensitivity analysis then comes from the same
machinery — a Fréchet kernel verified against an exact layered computation, a
depth-of-investigation definition stated with its convention, and a null
direction identified with transverse-resistance equivalence. Every demo prints
the checks as well as the results, because a number without its check is an
assertion.

**All models and data in this module are SYNTHETIC.** The layered models,
arrays, currents, contact resistances, noise levels and starting models are
chosen teaching values. No site, instrument, survey or data set is used or
referred to.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the four-electrode geometric factor, **compute** it for any layout,
   and **quantify** the errors from contact resistance and electrode
   mislocation.
2. **Compute** geometric factors, signal levels and depth sensitivities for
   Wenner, Schlumberger, dipole-dipole, pole-dipole and pole-pole arrays, and
   **explain** why a DC array's cumulative sensitivity starts at $1/2$.
3. **Compute** sounding curves, explain the two equivalence relations, and
   **report** an admitted model family with a $\chi^{2}$ test instead of a single
   thickness.
4. **Distinguish** sounding from profiling, **compute** the lateral footprint of
   an array, and **quantify** the edge smearing it causes.
5. **Design** an ERT acquisition using the scaling law DOI $\propto a$, a signal
   budget against a stated noise floor, and a coverage curve.
6. **Implement** and **verify** a layered forward model, construct its Jacobian,
   and **interpret** the smallest singular vector as a physical equivalence.
7. **Invert** a sounding with smoothness, choose the trade-off parameter by a
   stated criterion, **report** a covariance, and **test** the result with
   multi-start and robust reweighting.
8. **Decide**, for a stated application, whether a survey can detect and whether
   it can resolve the target.

## Prerequisites

- [09-01 Electrical Properties of Earth Materials](../01-electrical-properties-of-earth/README.md) —
  what the method measures.
- [02-07 Electromagnetism and Electromagnetic Induction](../../02-physics/07-electromagnetism/README.md) —
  potentials, current density and superposition.
- [18-02 Linear Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/README.md) —
  least squares and SVD, used in lessons 06 and 07.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Resistivity Principle and the Four-Electrode Arrangement](01-resistivity-principle.md) | intermediate | One formula for $k$; four electrodes move the contact resistance out of the measurement path |
| 02 | [Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole](02-electrode-arrays.md) | advanced | Half of a DC array's sensitivity is a surface step; depth is linear in spacing and signal is cubic |
| 03 | [Apparent Resistivity and Geometric Factors](03-apparent-resistivity.md) | advanced | The data measure a transverse resistance or a longitudinal conductance, not a thickness |
| 04 | [Vertical Electrical Sounding vs Profiling](04-sounding-profiling.md) | advanced | Detection is easy and resolution is hard; a lateral contact is smeared over an aperture |
| 05 | [ERT Acquisition and Design](05-ert-tomography.md) | graduate | DOI scales with spacing, signal with $n^{-3}$; design is choosing where to spend sensitivity |
| 06 | [Forward Modelling Resistivity Data](06-resistivity-forward-modelling.md) | graduate | Two independent solutions must agree before anything is inverted; the null space is the physics |
| 07 | [Resistivity Inversion: Smoothness, Robustness, Constraints](07-resistivity-inversion.md) | research | The penalty chooses the picture; the covariance and the outliers are the report |
| 08 | [ERT Applications: Aquifers, Contamination, Landslides, Archaeology](08-ert-applications.md) | graduate | Detection, resolution and admitted families, worked for four archetypes |

## Suggested path

**If you are new to resistivity surveying:** lessons 01–03 in order, then 04.
Lesson 02 is where the depth/signal trade-off is quantified, and lesson 03 is
where the non-uniqueness first bites.

**If you already run surveys:** 02 §2–3 (the $1/2$ surface step and the DOI
convention), 03 §4–5 (equivalence against noise), and 05 (design numbers).

**If you are building an inversion:** 06 in full, then 07. The forward-model
verification of 06 §2–3 and the null-direction experiment of 06 §4–5 are the
prerequisites for trusting anything 07 produces.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-resistivity-principle.md`](01-resistivity-principle.md) | Lesson 01 |
| [`02-electrode-arrays.md`](02-electrode-arrays.md) | Lesson 02 |
| [`03-apparent-resistivity.md`](03-apparent-resistivity.md) | Lesson 03 |
| [`04-sounding-profiling.md`](04-sounding-profiling.md) | Lesson 04 |
| [`05-ert-tomography.md`](05-ert-tomography.md) | Lesson 05 |
| [`06-resistivity-forward-modelling.md`](06-resistivity-forward-modelling.md) | Lesson 06 |
| [`07-resistivity-inversion.md`](07-resistivity-inversion.md) | Lesson 07 |
| [`08-ert-applications.md`](08-ert-applications.md) | Lesson 08 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Eight runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 09-electrical-em-methods/02-dc-resistivity/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resistivity_principle_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python electrode_arrays_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python apparent_resistivity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sounding_profiling_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ert_tomography_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resistivity_forward_modelling_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resistivity_inversion_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ert_applications_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), imports no plotting library, and exits 0.
They require no network access. The two heaviest demos (electrode-array
sensitivity and the inversion) take about 10 and 20 seconds.

## Mastery checkpoint

Complete this without notes:

> A survey has 32 electrodes at 4 m spacing. **(a)** Compute $k$ for a Wenner
> array with $a = 8$ m and for a dipole-dipole array with $n = 3$, $a = 8$ m, and
> the signal ratio between them on $80\ \Omega\,\mathrm{m}$ ground at
> $I = 0.1$ A. **(b)** Using the scaling law, state the DOI of each and decide
> which is usable if the noise floor is 0.5 mV. **(c)** A thin resistive layer at
> 12 m has $T = 3000\ \Omega\,\mathrm{m^{2}}$. State what a sounding can and
> cannot determine about it, with a $\chi^{2}$ argument at 2% noise. **(d)** Name
> the two checks you would demand of the forward model before inverting.

A worked version of (a)–(c) appears in the lesson-03 and lesson-05
[solutions](exercises/05-ert-tomography-solutions.md).

## Common pitfalls across this module

1. **Quoting a depth of investigation without its convention.** With the surface
   step included, half a DC array's sensitivity sits at the surface.
2. **Reading an inverted section as the Earth.** It is one member of a family,
   selected by a penalty term.
3. **Confusing detection with resolution.** Lesson 04 and lesson 08 quantify the
   gap in the same models.
4. **Ignoring the signal budget.** $\Delta V \propto a^{-1}$ for a fixed $\rho_a$
   and $\propto n^{-3}$ for a dipole-dipole array: the deepest data are often
   below the noise.
5. **Inverting before verifying the forward model.** Two independent solutions
   agreeing to twelve digits is the minimum standard.

## Related modules

- [09-01 Electrical Properties of Earth Materials](../01-electrical-properties-of-earth/README.md) —
  the property relations behind every number here.
- [09-03 Induced Polarisation](../03-induced-polarisation/README.md) — the same
  acquisition with the time dimension added.
- [09-06 Borehole Electrical and EM Methods](../06-borehole-electrical/README.md) —
  the same physics from inside the ground.
- [09-07 EM Data Processing, QC and Uncertainty](../07-em-data-processing-and-qc/README.md) —
  noise, editing and error models.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general theory
  of the non-uniqueness this module demonstrates.
