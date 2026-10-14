---
id: 25-04-02
title: "Project: 1-D and 2-D Magnetotelluric Inversion"
level: graduate
prereqs: ["25-03-02", "08-04-02", "09-02-07", "18-04-02"]
estimated_minutes: 210
tags: [projects, magnetotellurics, inversion, non-uniqueness, 2d, teaching]
---

# Project: 1-D and 2-D Magnetotelluric Inversion

## Learning objectives

By the end of this project you will be able to:

1. **Compute** the 1-D MT response of a layered earth with the impedance
   recursion, and **state** the skin-depth scaling.
2. **Invert** the response for layer resistivities under a roughness penalty, and
   **show** that the penalty, not the data, chooses among the accepted models.
3. **Measure** the width of the equivalence class along a physically motivated
   parameter direction, rather than assuming the textbook trade-off.
4. **Demonstrate** that a frequency-independent galvanic distortion is
   unabsorbable by a 1-D model, and **use** the resulting misfit as a diagnostic.
5. **State** what a 2-D inversion adds, and what the TE/TM mode split does to the
   inverse problem.
6. **Report** an MT inversion with its penalty, its misfit per datum, its class
   width and the dimensionality evidence.
7. **Diagnose** the three failure modes of a 1-D MT interpretation: a distortion
   absorbed into resistivity, a static shift misread as structure, and a
   penalty chosen to produce a desired answer.

All responses in this project are **SYNTHETIC**: computed from chosen layered
models with chosen noise by
[`code/mt_inversion_demo.py`](./code/mt_inversion_demo.py). No field site, no
published sounding and no EMAP dataset is used.

## Prerequisites

- [25-03-02 Project: ERT Inversion with Resolution Assessment](../03-advanced-projects/02-ert-inversion-project.md) —
  the same equivalence-and-resolution discipline for a diffusive method.
- [09-02-07 Resistivity Inversion: Smoothness, Robustness, Constraints](../../09-electrical-em-methods/02-dc-resistivity/07-resistivity-inversion.md) —
  the regularised inversion being applied.
- [08-04-02 Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/02-magnetotellurics.md) —
  the impedance tensor, its modes and the physical basis of the measurement.
- [18-04-02 Gradient, Gauss-Newton and Full Newton Methods](../../18-inverse-problems/04-nonlinear-inversion/02-gradient-and-newton.md) —
  the non-linear solver and its convergence criteria.

## 1. The question

*What does a magnetotelluric sounding determine, and what does a two-dimensional
Earth do to a one-dimensional interpretation?*

MT is the deepest-penetrating electromagnetic method and the most deceptive to
interpret in one dimension, for two structural reasons. First, its inverse problem
is non-linear and non-unique in a way that is *penalty-dependent*: the
demonstration's models change by a factor of 18 in places between two
regularisation parameters that both fit the data at a $\chi^{2}$ of about $0.8$ per
datum. Second, a **galvanic distortion** — a frequency-independent complex factor
imposed by nearby 2-D or 3-D structure — cannot be absorbed by any 1-D model at
all, and the demonstration measures a misfit of $916$ where $1$ is expected.

## 2. The data

**Synthetic sounding (SYNTHETIC).** A 30-layer model with 20 m to 300 km
thicknesses and resistivities of $100\ \Omega\,\mathrm{m}$ above 300 m,
$5\ \Omega\,\mathrm{m}$ from 300 to 3000 m and $1000\ \Omega\,\mathrm{m}$ below,
computed at 20 frequencies from $0.001$ to $100\ \mathrm{Hz}$ with $2\%$ noise on
$\log_{10}\rho_a$ and $1°$ on phase. The response falls from
$217.429\ \Omega\,\mathrm{m}$ at 0.001 Hz to $5.913\ \Omega\,\mathrm{m}$ at
0.43 Hz and rises again to $81.844\ \Omega\,\mathrm{m}$ at 100 Hz — the conductor
first, then the resistive basement. The skin depth in a
$100\ \Omega\,\mathrm{m}$ half-space is $5.0\ \mathrm{km}$ at 1 Hz.

**Provenance.** SYNTHETIC. The profile is a chosen three-part structure; the
"distortion" of §6 is a chosen complex factor applied to the response, not a
computed 2-D solution.

## 3. The project specification

**Steps.**

1. Implement the impedance recursion from the bottom of a layered model and verify
   it against the half-space result $Z = \sqrt{i\omega\mu_0\rho}$.
2. Compute apparent resistivity and phase and tabulate the response over the
   frequency band.
3. Invert for 30 log-resistivities with a first-difference roughness penalty at
   three values of the penalty, and report the misfit and the model spread.
4. Measure the width of the class along a chosen parameter direction (here the
   conductor's thickness with its conductance held fixed) by evaluating the misfit
   of a family of models against the *same* observed data.
5. Apply a frequency-independent complex distortion and invert; report the misfit
   and state what the misfit establishes.
6. Write the report: response, inversion, penalty, class width, dimensionality
   evidence and what the data do not determine.

**Deliverable.** The response table, three inverted models with their misfits, the
class-width measurement and the distortion test.

**Success criterion.** The penalty is stated and its effect measured; the class
width is measured along a stated direction; the distortion is diagnosed from the
misfit, not from the recovered structure.

## 4. The forward problem

For a stack of layers the impedance is built from the bottom upward:
$Z_N = \sqrt{i\omega\mu_0\rho_N}$ in the half-space, and

$$Z_k = Z_k^{\text{layer}}\,
\frac{Z_{k+1} + Z_k^{\text{layer}}\tanh(k_k h_k)}
     {Z_k^{\text{layer}} + Z_{k+1}\tanh(k_k h_k)},
\qquad
Z_k^{\text{layer}} = \sqrt{i\omega\mu_0\rho_k},
\qquad
k_k = \sqrt{i\omega\mu_0/\rho_k},$$

from which $\rho_a = |Z_1|^{2}/(\omega\mu_0)$ and
$\phi = \arctan(\operatorname{Im}Z_1/\operatorname{Re}Z_1)$. The **skin depth**
$\delta = \sqrt{2\rho/(\omega\mu_0)}$ sets the depth sampled by a frequency, so the
sounding's depth range is fixed by its frequency band: $5.0\ \mathrm{km}$ at 1 Hz
in $100\ \Omega\,\mathrm{m}$ rock, and a factor of $\sqrt{10}$ deeper at 0.01 Hz
for the same resistivity.

## 5. The penalty is part of the answer

| $\alpha$ | $\chi^{2}$ per datum | model rms ($\log_{10}\rho$) | roughness |
|---|---|---|---|
| 0.02 | 0.7150 | 0.7699 | 19.7972 |
| 0.20 | 0.7366 | 0.5134 | 7.0924 |
| 2.00 | 0.8033 | 0.4252 | 2.6710 |

All three fit the data at about the noise level, and the models differ by up to
$1.259$ in $\log_{10}\rho$ — a factor of **18.2**. The misfit is nearly flat
between them because the roughness penalty suppresses structure the data cannot
distinguish from noise. **The report must therefore state the penalty used**, since
$\alpha$ is selecting among an accepted family, not resolving it. This is the same
statement as module 25-03's regularisation discussion, with MT's sharper
consequence: a factor of 18 in a subsurface resistivity, chosen by a parameter the
reader cannot see unless it is printed.

## 6. Equivalence, measured rather than assumed

Textbooks describe an **S-equivalence** for a thin conducting layer: only its
conductance $h/\rho$ is determined, so $h$ and $\rho$ trade. Whether a given
conductor is in that limit is a measurement. Holding the conductance at
$540\ \mathrm{S}$ and varying the thickness:

| thickness (m) | $\rho$ ($\Omega\,\mathrm{m}$) | conductance (S) | $\chi^{2}$ | verdict |
|---|---|---|---|---|
| 600 | 1.11 | 540 | 106.644 | rejected |
| 1350 | 2.50 | 540 | 50.361 | rejected |
| 2700 | 5.00 | 540 | 1.121 | accepted |
| 5400 | 10.00 | 540 | 42.755 | rejected |
| 10800 | 20.00 | 540 | 179.027 | rejected |

Only the true thickness fits, and a 25-point scan from 1500 to 5000 m accepts a
class narrower than the scan step. **The S-equivalence does not hold here**, and the
reason is physical: the conductor is 2700 m thick while the skin depth at the
frequencies that sense it is about $2.05\ \mathrm{km}$ at 0.3 Hz, so the depth to
the *base* of the conductor is sensed and the conductance is not the only
constraint. The equivalence is a **thin-layer limit**, and this layer is not thin.

The lesson generalises: the width of an inverse problem's equivalence class is a
property of the specific model and data, and the fastest way to be wrong is to
quote a textbook degeneracy in place of a measurement. Note also that the class
width *along this direction* is narrow while the class across *penalties* is wide
(§5): the two are different classes and both belong in the report.

## 7. Two-dimensional structure, and the distortion test

A nearby 2-D or 3-D body imposes a **galvanic distortion** on the field: a
frequency-independent complex factor $D = |D|e^{i\phi_D}$ multiplying the regional
impedance, produced by charge accumulation at conductivity boundaries. Applying
$|D| = 1.25$ and $\phi_D = 8°$ and inverting with a 1-D model gives

$$\chi^{2} = 916.0 \quad\text{against an expected } 1.0,$$

with a model rms error of $4.4084$ in $\log_{10}\rho$. **The 1-D model cannot fit
the data at all**, because no layered structure produces a constant complex factor
across the band: the amplitude bias alone would be
$\log_{10}(1.25^{2}) = +0.194$ decade in apparent resistivity, but the $8°$ phase
offset has no layered equivalent.

Two consequences for practice:

1. **The misfit is the diagnostic.** A 1-D inversion that will not converge to
   $\chi^{2} \approx 1$ is evidence of dimensionality, not of an unrepresentable
   fine structure.
2. **A 2-D inversion is not a bigger 1-D inversion.** In two dimensions the
   response splits into **TE** (electric field parallel to strike) and **TM**
   (magnetic field parallel to strike) modes with different sensitivities: the TM
   mode is strongly affected by galvanic charges at lateral boundaries, the TE
   mode much less. The joint inversion of both modes is what resolves lateral
   structure, and the TE–TM discrepancy in the data — the **mode split** — is the
   standard dimensionality indicator to check *before* choosing a model
   parameterisation.

## 8. Assumptions and regime of validity

1. **Plane-wave source.** MT assumes a uniform, horizontal source field; at
   periods long enough for the source field to vary spatially (the auroral
   electrojet at high latitude) the assumption fails and produces a spurious
   resistivity.
2. **A layered or 2-D earth.** Distortion and mode splitting are the evidence when
   it is not.
3. **Isotropic resistivity.** Anisotropy in a layered sequence is
   indistinguishable in a 1-D sounding from a different thickness.
4. **A correct noise model.** $\chi^{2}$ is only meaningful with defensible
   uncertainties, which MT estimation produces through robust processing; the
   robust errors are themselves estimates.
5. **A converged, adequately penalised inversion.** A penalty chosen so that the
   model "looks geological" is a prior, and must be reported as one.

## The honest summary

This project's result is a warning with numbers. The 1-D response of a
30-layer model with a 2700 m conductor at $5\ \Omega\,\mathrm{m}$ is inverted with a
roughness penalty at three values, all fitting at $\chi^{2} \approx 0.7$–$0.8$ per
datum while the models differ by a factor of 18.2; the conductor's thickness is
nevertheless constrained to better than the 1.05 scan step, because the S-equivalence
is a thin-layer limit this conductor is not in; and a frequency-independent
distortion of amplitude 1.25 and phase $8°$ produces a misfit of 916 where 1 is
expected, which is the diagnostic that sends the interpreter to two or three
dimensions. The transferable practice is to report the penalty, to measure the
class width along the direction you care about, and to treat an unfittable 1-D
response as evidence about dimensionality rather than about resolution.

## Python demonstration

[`code/mt_inversion_demo.py`](./code/mt_inversion_demo.py) prints every number
quoted above. It:

1. computes the layered response and prints it at five frequencies with the 1 Hz
   skin depth;
2. inverts at three penalties, printing the misfit, the model error and the
   roughness, and the factor-18 model spread;
3. measures the class width along the fixed-conductance direction, printing the
   accepted and rejected thicknesses and the fine-scan result;
4. applies the galvanic distortion, inverts, and prints the misfit that diagnoses
   it.

Run it with the project virtual environment:

```bash
cd 25-projects-capstone/04-graduate-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_inversion_demo.py
```

The script prints only, writes no files, uses no network and exits 0. It runs in
under three seconds (SciPy's `least_squares` on a 30-parameter problem).

## Exercises

Graded problems and worked solutions are in
[`exercises/02-mt-1d-2d-inversion-exercises.md`](./exercises/02-mt-1d-2d-inversion-exercises.md)
and
[`exercises/02-mt-1d-2d-inversion-solutions.md`](./exercises/02-mt-1d-2d-inversion-solutions.md).
The ★★★ item asks you to design a dimensionality test, not to rerun the inversion.

## Mastery checkpoint

Without notes:

1. Write the impedance recursion and state the skin-depth formula.
2. State why a roughness penalty makes the inversion's answer depend on a
   parameter the data do not determine.
3. A 1-D inversion of a real sounding converges to $\chi^{2} = 40$ per datum with
   a reasonable-looking model. State the diagnosis and the next step.
4. Explain in two sentences why the amplitude of a galvanic distortion biases the
   apparent resistivity but its phase cannot be absorbed.

## Common pitfalls

1. **Reporting a model without its penalty.** A factor of 18 lies between two
   defensible choices.
2. **Quoting the S-equivalence as a fact about the data.** It is a thin-layer
   limit, and here it fails.
3. **Absorbing a distortion into a resistivity.** The amplitude part looks like
   structure; the phase part refuses to fit.
4. **Inverting TE and TM as if they were one dataset.** Their sensitivities differ,
   and the split is the dimensionality test.
5. **Treating robust error bars as exact.** They are estimates, and $\chi^{2}$
   inherits their uncertainty.

## Where this is used

MT is used for geothermal and mineral exploration, for crustal and lithospheric
imaging, and for monitoring. The dimensionality discipline of §7 is what
distinguishes a defensible 2-D section from a one-dimensional cartoon, and it is
the same question the receiver-function and surface-wave projects address in the
seismic domain ([25-04-06](./06-receiver-function-project.md)). In professional
practice the TE–TM split and the distortion decomposition are the first two items
in an MT interpretation report, and an inversion that will not reach unit misfit is
returned before its model is interpreted.

## Related lessons

- [09-02-03 Apparent Resistivity and Geometric Factors](../../09-electrical-em-methods/02-dc-resistivity/03-apparent-resistivity.md) —
  the DC analogue of the apparent-resistivity concept used here.
- [08-04-04 MT Inversion: 1-D, 2-D and 3-D Approaches](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/04-mt-inversion.md) —
  the inversion frameworks this project applies, including the mode split.
- [09-05-01 TEM Sounding for Aquifers and Mineral Targets](../../09-electrical-em-methods/05-em-methods-applications/01-tem-sounding.md) —
  a controlled-source method with the same diffusive physics and a better-defined
  source.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the formal statement of §6.
- [25-03-06 Project: Gravity Inversion with Uncertainty Quantification](../03-advanced-projects/06-gravity-inversion-uq.md) —
  the same equivalence-class measurement in a linear problem.

## Self-assessment checklist

- [ ] I can implement the MT impedance recursion and check it on a half-space.
- [ ] I can compute a skin depth and state the depth range of a band.
- [ ] I can invert with a roughness penalty and report the penalty's effect.
- [ ] I can measure a class width along a stated parameter direction.
- [ ] I can diagnose a galvanic distortion from the misfit.
- [ ] I can name the three failure modes of §8 and the test for each.
