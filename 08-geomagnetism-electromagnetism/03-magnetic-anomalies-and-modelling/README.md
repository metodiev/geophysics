# Module 08-03 — Magnetic Anomalies and Modelling

**Stages:** advanced → doctoral · **Prerequisites:** modules 08-01 and 08-02;
the dipole field from 02-07.

This module turns a measured total-field anomaly into a statement about rock. It
is built around one honest difficulty: an anomaly's amplitude is a *product* of a
magnetisation and a depth, and neither factor can be recovered from the amplitude
alone. Every lesson either derives that trade-off or shows how more data narrows
it — and every lesson states which of the two it is doing. Along the way the
module takes the two approximations that practitioners actually use — the single
dipole and the induced-magnetisation assumption — and measures their errors
rather than asserting them. The measured failures are large: a factor of fifteen
in the near field, and a factor of eleven in susceptibility when remanence is
ignored.

The second organising idea is that a magnetic map is not a picture of the
subsurface. What an instrument records is a **projection** of a vector field on
the direction of the main field, so the same body produces a positive, a
displaced or a negative anomaly depending on the field's inclination and on a
remanence the survey never measured. Reduction to the pole is the standard
response, and it is presented here as an *assumption* with a cost — a noise gain
that grows without bound as the inclination approaches zero — rather than as a
correction.

The third is that inversion does not solve the problem, it exposes it. The final
lessons show a null space of dimension 127 in a problem with 168 parameters and 41
data, construct a model change of 156% that the data cannot see, and state what a
report must therefore contain. All models and data in this module are
**SYNTHETIC**: no station, survey, observatory or published anomaly is used, and
every number quoted in a lesson is printed by a demonstration in `code/`.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the dipole field of a magnetised body and the total-field anomaly as
   a projection, and **state** the range over which the projection may be
   linearised.
2. **Compute** induced and remanent magnetisations, their vector sum and the
   Koenigsberger ratio, and **quantify** the error made by assuming induced
   magnetisation.
3. **Derive** the reduction-to-the-pole filter from the Poisson relation,
   **verify** it numerically, and **quantify** its noise cost at low latitude.
4. **Build** a forward model of a magnetised body by two independent routes,
   **verify** each against an exact solution, and **measure** where the dipole
   approximation fails.
5. **Apply** Euler and Werner deconvolution, the half-width rule and the spectral
   method, and **state** the model each assumes and the error each makes.
6. **Assemble** a magnetic inverse problem, **interpret** its singular-value
   spectrum and null space, and **solve** it with regularisation and a positivity
   constraint.
7. **Design** a mineral, UXO or archaeological survey from the target's moment,
   the required detection depth, the sensor noise and the anomaly half-width.

## Prerequisites

- [08-01 The Earth's Magnetic Field](../01-earth-magnetic-field/README.md) —
  the main field, its inclination, secular variation and rock magnetism.
- [08-02 Magnetic Instruments and Surveys](../02-magnetic-instruments-and-surveys/README.md) —
  how the nanotesla is measured and how surveys are designed and levelled.
- [02-07-02 Magnetostatics](../../02-physics/07-electromagnetism/02-magnetostatics.md) —
  the magnetic dipole and the scalar potential.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Magnetic Anomaly Physics and Remanent vs Induced Magnetisation](01-magnetic-anomaly-basics.md) | advanced | $\Delta T = \hat f\cdot\mathbf{B}_a$ is a projection; depth and moment trade exactly as $z^{-3}$ |
| 02 | [Koenigsberger Ratio and Remanence Dominance](02-koenigsberger-and-remanence.md) | graduate | $\mathbf{M} = \mathbf{M}_i+\mathbf{M}_r$; an induced-only interpretation inflates $\chi$ by 11.6 in the demonstration |
| 03 | [Reduction to the Pole and Equator](03-reduction-to-pole.md) | graduate | $k^{2}/\hat{\mathcal{O}}_m\hat{\mathcal{O}}_f$; identity at the pole, unbounded at low latitude |
| 04 | [Forward Modelling Magnetic Bodies](04-magnetic-forward-modelling.md) | graduate | Charge and dipole routes verified against an exact solution; the dipole form fails by 15× near a body |
| 05 | [Depth Estimation: Werner, Euler, Peters and Spectral Methods](05-magnetic-depth-estimation.md) | doctoral | Four estimators, four models; the structural index moves the answer by tens of per cent |
| 06 | [Magnetic Inversion and Its Non-Uniqueness](06-magnetic-inversion.md) | doctoral | Rank 41, nullity 127; a 156% model change invisible in the data |
| 07 | [Applications: Mineral Exploration, UXO, Archaeology](07-magnetic-uses.md) | advanced | Detectability is a ratio; moment buys range as its cube root |

## Suggested path

**If you are new to magnetic methods:** lessons 01, 04 and 07 in order, running
each demonstration. Lesson 04 is where the approximations reveal their size.

**If you already know the dipole formula:** start at 02 (remanence), then 03 (what
to do about it) and 06 (what the data can actually determine).

**If you are preparing a research project:** 03 §5–6 (the low-latitude cost), 05
and 06 in full, plus the ★★★ exercises of every lesson.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-magnetic-anomaly-basics.md`](01-magnetic-anomaly-basics.md) | Lesson 01 |
| [`02-koenigsberger-and-remanence.md`](02-koenigsberger-and-remanence.md) | Lesson 02 |
| [`03-reduction-to-pole.md`](03-reduction-to-pole.md) | Lesson 03 |
| [`04-magnetic-forward-modelling.md`](04-magnetic-forward-modelling.md) | Lesson 04 |
| [`05-magnetic-depth-estimation.md`](05-magnetic-depth-estimation.md) | Lesson 05 |
| [`06-magnetic-inversion.md`](06-magnetic-inversion.md) | Lesson 06 |
| [`07-magnetic-uses.md`](07-magnetic-uses.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

All models and data in this module are **SYNTHETIC**.

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_anomaly_basics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python koenigsberger_and_remanence_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reduction_to_pole_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_forward_modelling_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_depth_estimation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_inversion_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_uses_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), is print-only and exits 0. No network access
is required.

## Mastery checkpoint

Complete this without notes:

> A **synthetic** survey records a 120 nT anomaly over a body at low magnetic
> latitude ($I = 20^\circ$), displaced 1.5 km from the mapped surface expression.
> **(a)** State what the displacement implies for the magnetisation direction and
> compute the $3\sin^{2}I - 1$ factor. **(b)** Decide whether RTP is usable at this
> latitude, using the noise-gain table and a stated noise level. **(c)** Assuming
> induced magnetisation, compute the moment required at 1.5 km depth, and state
> the volume needed at $M = 3$ A m$^{-1}$. **(d)** If the rock has $Q = 4$ with
> remanence across the field, state how your answer to (c) changes and by roughly
> how much. **(e)** State two independent measurements that would settle the
> magnetisation direction, and what each requires.

A worked version of parts (a)–(d) appears in the lesson-02 and lesson-03
solutions.

## Common pitfalls across this module

1. **Quoting a depth without a magnetisation, or a magnetisation without a
   depth.** They are exchanged at the rate of $z^{3}$.
2. **Using the dipole formula near a body.** Measured error in the demonstration:
   a factor of 15 over the centre of a shallow prism.
3. **Assuming induced magnetisation.** $Q$ exceeds unity in many rocks, and the
   induced-only interpretation inflates the susceptibility by an order of
   magnitude in the demonstration.
4. **Treating RTP as a correction.** It assumes a magnetisation direction and
   multiplies noise by a gain that grows without bound at low latitude.
5. **Tuning the structural index until the map looks right.** It is the model,
   and it moves the depth by tens of per cent.
6. **Reporting one inverted model as the Earth.** The null space has dimension
   $n_{\text{model}}-n_{\text{data}}$; report the family.

## Related modules

- [08-01 The Earth's Magnetic Field](../01-earth-magnetic-field/README.md) — where
  the field, its inclination and rock magnetism come from.
- [08-04 Electromagnetic Induction in the Earth](../04-electromagnetic-induction/README.md) —
  the other half of the folder: conductivity instead of magnetisation.
- [05-03 Forward Modelling Principles](../../05-core-geophysics/03-forward-modelling-principles/README.md) —
  the discipline of building and validating a forward model, applied here.
- [18-01 Foundations of Inverse Problems](../../18-inverse-problems/01-inverse-problem-foundations/README.md) —
  the general theory of the non-uniqueness exposed in lesson 06.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) —
  susceptibility and remanence as measurable rock properties.
