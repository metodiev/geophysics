# Module 09-04 — Self-Potential and Related Methods

**Stages:** advanced → graduate · **Prerequisites:** module 09-01; the potential
theory of folder 02.

This module is about the only measurement in the folder that injects no current.
A self-potential survey reads the natural voltage between two electrodes, and that
voltage is the surface expression of currents generated inside the ground by
chemistry or by moving water. The organising chain is therefore
**mechanism → current distribution → surface potential**, and the module works
along it: lesson 01 derives the two source mechanisms and the potential field of a
buried current distribution, lesson 02 applies both to seepage, dams, landfills
and mineralisation and measures the detection limits, and lesson 03 turns the same
potential theory around and injects a current into a known body
(mise-à-la-masse), comparing it with a surface array and with an induced
polarisation measurement.

Two honest difficulties run through all three lessons. First, **SP measures a
current, not a property**: the same anomaly shape can arise from a redox cell, a
seepage path or a conductivity contrast, and separating them needs additional
information. Second, **a potential field constrains a family, not a body**: the
width of an anomaly sets a depth only once the source geometry is assumed, and the
lesson measures the admitted ridge of (depth, length, current) triples for a
single profile, with a correlation of $+0.854$ between depth and length.

The third thread is **the reference**. SP is measured between two electrodes, so a
drifting reference contributes to the data; the module measures which trends bias
the answer (asymmetric ones) and which do not (symmetric ones are orthogonal to a
symmetric anomaly), and it states the levelling function as part of the model.

**All models and data in this module are SYNTHETIC.** No real fluid, mineral, ore
body, dam, landfill or instrument is modelled, and no field value is quoted.
Physical constants are standard values with units stated.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the Helmholtz-Smoluchowski electrokinetic coupling coefficient and
   **compute** the head a stated SP anomaly requires.
2. **Compute** Nernst cell potentials from standard reduction potentials and
   **derive** the membrane (diffusion) potential against transference number.
3. **Derive** the half-space potential of a buried electrode and of a buried
   current dipole by the image method, and **verify** the two profile-width rules.
4. **Measure** a matched-filter detection limit for an SP anomaly and **explain**
   the measured $\text{depth}^{3/2}$ law.
5. **Report** a depth from a profile with its admitted range, its source family
   and its model dependence.
6. **Derive** the conducting-sphere response, **verify** its boundary conditions,
   and **explain** why the amplitude saturates in conductivity contrast.
7. **Compare** a mise-à-la-masse measurement with a surface array and with an IP
   measurement, and **state** what each constrains.

## Prerequisites

- [09-01 Electrical Properties of Earth Materials](../01-electrical-properties-of-earth/README.md) —
  conductivity and surface chemistry.
- [02-07-01 Electrostatics, Coulomb's Law and Electric Potential](../../02-physics/07-electromagnetism/01-electrostatics.md) —
  the potential theory used throughout.
- [09-03 IP Acquisition, Chargeability and Phase Units](../03-induced-polarisation/03-ip-acquisition.md) —
  the electrode and noise environment shared with SP.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Sources of Self-Potential: Electrokinetic, Electrochemical](01-self-potential-sources.md) | graduate | Two mechanisms, one field; width gives depth only with a geometry assumed |
| 02 | [SP for Seepage, Dams, Landfills and Mineralisation](02-sp-applications.md) | advanced | Detection is a matched filter; the admitted set is a ridge; asymmetric drift biases |
| 03 | [Mise-a-la-Masse and Induced Polarisation Mapping](03-mise-a-la-masse.md) | graduate | Energising a body: the amplitude saturates in contrast and measures geometry |

## Suggested path

**If you are new to SP:** lesson 01 in full, then lesson 02's §3.2 (detection)
and §3.5 (drift), running both demonstrations.

**If you use SP in the field:** 01 §3.5 (cross-check the width rules), 02 §3.4
(source type versus parameters) and 02 §3.5 (levelling).

**If you are preparing a research project:** 03 §3.4–3.6 (the distance–contrast
degeneracy and the model's failure when the source is inside the body), plus the
★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-self-potential-sources.md`](01-self-potential-sources.md) | Lesson 01 |
| [`02-sp-applications.md`](02-sp-applications.md) | Lesson 02 |
| [`03-mise-a-la-masse.md`](03-mise-a-la-masse.md) | Lesson 03 |
| [`code/`](code) | Three runnable demonstrations |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |

## How to run the demos

```bash
cd 09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python self_potential_sources_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sp_applications_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mise_a_la_masse_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), exits 0, and opens no plot window.

## Mastery checkpoint

Complete this without notes:

> **(a)** With $\varepsilon_r = 80.1$, $\zeta = -20$ mV, $\eta = 10^{-3}$ Pa s and
> $\sigma = 0.01$ S/m, compute $\partial V/\partial h$ in mV per metre of head and
> the head needed for a $10$ mV anomaly. **(b)** A single-lobe anomaly has
> FWHM $= 120$ m: compute the depth it implies under the point-source and compact
> dipole rules, and state the ratio. **(c)** For a buried electrode of $1$ A at
> $50$ m depth in a $50\ \Omega$ m half-space, compute the potential directly above
> it. **(d)** State what happened to the modelled anomaly as the source was moved
> towards a body's centre, and what model replaces the sphere model there.

Worked versions appear in the lesson
[solutions](exercises/01-self-potential-sources-solutions.md) and in
`solutions` for lesson 03.

## Common pitfalls across this module

1. **Reporting an absolute SP value.** The measurement is between two electrodes;
   the reference and the levelling are part of the data.
2. **Converting a width to a depth without a geometry.** The two standard rules
   differ by a factor $2.26$.
3. **Quoting one depth from a fitted profile.** The admitted set is a ridge with
   a measured correlation of $+0.854$.
4. **Levelling with a function that can absorb the anomaly.** A one-sided ramp
   moved the recovered current by $+4.6\%$ in the measured test.
5. **Reading a mise-à-la-masse anomaly as a conductivity.** The response
   saturates in contrast and measures geometry.
6. **Using a polarised-sphere model with the electrode inside the body.** The
   modelled anomaly diverges by four orders of magnitude; that geometry needs an
   equipotential-body model.

## Related modules

- [09-01 Electrical Properties of Earth Materials](../01-electrical-properties-of-earth/README.md)
- [09-02 DC Resistivity Methods](../02-dc-resistivity/README.md) — the active
  counterpart of the passive measurement.
- [09-03 Induced Polarisation](../03-induced-polarisation/README.md) — the
  polarisation measurement that survives a saturated conductivity contrast.
- [09-05 Applied Electromagnetic Methods](../05-em-methods-applications/README.md) —
  the inductive measurements over the same targets.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the framework for
  the ridge and the degeneracy measured here.
