# Module 04-03 — Geologic Time, Stratigraphy and Dating

**Stages:** beginner → advanced · **Prerequisites:** the plate-tectonics module
([04-02](../02-plate-tectonics/README.md)), which supplies the tectonic setting
that basins and stratigraphy develop in.

This module is about the one quantity in the geosciences that has no analogue in
the laboratory: **time**, in quantities so far outside human experience that the
words used for it are not descriptive but misleading. It is also about the
machinery that turns a rock into a number of years, and the assumptions that
machinery carries.

Two ideas organise everything here. The first is that **relative time is a
deductive system**: superposition, original horizontality, cross-cutting
relations, inclusions and faunal succession together constrain the order of
events, and the geological history is the set of orders consistent with all the
observations. That system needs no laboratory and no number, and it is the
foundation on which every absolute age is hung. The second is that **an absolute
age is a model-dependent interpretation, not a measurement**: what is measured is
a ratio of concentrations, and what is reported is that ratio converted into
years through a decay law, a closure assumption and a stated or fitted initial
condition. The lesson that treats dating
([03](./03-radiometric-dating.md)) refuses to present an age without those
attachments.

The decay law itself is not re-derived here. Radioactive decay, half-life, the
Bateman equations, the isochron equation and closure temperature are derived in
[02-09-02 Radioactive Decay, Half-Life and Dating](../../02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md),
and this module builds on that one rather than repeating it. What is added here
is the stratigraphic and geological use: what the systems date, how an age is
tied to a boundary in the time scale, and what a discordia, a mixing line and a
backstripped subsidence curve each assume.

## Learning objectives

By the end of this module you will be able to:

1. **Explain** why deep time is quantitatively unintuitive, and demonstrate it
   with the compression and ratio arithmetic that every popular graphic performs.
2. **Describe** the nested hierarchy of the geologic time scale, how a boundary
   is *defined* (a GSSP or a GSSA) as opposed to *numbered*, and why the
   hierarchy of names is stable while the ages attached to it are revised.
3. **Order** a sequence of geological events from field relations, and detect
   when a set of relations is internally inconsistent rather than picking the
   order that ignores the difficult observation.
4. **Distinguish** a date from a measurement, an isochron age from a model age,
   and state for any published age which of the two it is.
5. **Reconstruct** a concordia diagram, explain what a discordia chord's two
   intercepts mean, and use it to recover a crystallisation age and a
   disturbance age from one set of analyses.
6. **Quantify** the three assumptions that dominate a dating result: closed
   system, correct initial ratio, and closure temperature.
7. **Model** subsidence in a stretched lithosphere, separate the crustal-
   thinning from the thermal contribution, and explain why the familiar
   single-exponential subsidence law is an approximation.
8. **Backstrip** a stratigraphic column, decompact it, and report the tectonic
   subsidence with the sensitivity of the result to the porosity model it
   assumed.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [The Geologic Time Scale and Deep Time](./01-geologic-time-scale.md) | beginner | A boundary is defined at a physical reference point, not by an age; the chart assigns ages and has been revised repeatedly |
| 02 | [Stratigraphic Principles and Relative Dating](./02-stratigraphic-principles.md) | beginner | Relative dating is a constraint system, and an inconsistent set of field relations has no solution to be found |
| 03 | [Radiometric Dating Methods and Their Assumptions](./03-radiometric-dating.md) | advanced | A date is a model-dependent interpretation; the concordia is the internal test that makes U–Pb a system rather than a conversion |
| 04 | [Sedimentary Basins: Formation, Fill and Subsidence](./04-sedimentary-basins.md) | intermediate | A subsidence curve is a decomposition, and every term in it is a model with stated parameters |

Lesson 03 is the module's **mastery lesson**: if you can say, for any age, what
was measured, what was assumed, and what would falsify it, you have the skill the
rest of the folder assumes. Do not read it; work it with the demo open.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-geologic-time-scale.md`](./01-geologic-time-scale.md) … [`04-sedimentary-basins.md`](./04-sedimentary-basins.md) | The four lessons |
| [`exercises/01-geologic-time-scale-exercises.md`](./exercises/01-geologic-time-scale-exercises.md) … [`exercises/04-sedimentary-basins-exercises.md`](./exercises/04-sedimentary-basins-exercises.md) | Four problem sets, ★ to ★★★ |
| [`exercises/01-geologic-time-scale-solutions.md`](./exercises/01-geologic-time-scale-solutions.md) … [`exercises/04-sedimentary-basins-solutions.md`](./exercises/04-sedimentary-basins-solutions.md) | Full worked solutions with the numbers |
| [`code/01-deep_time_demo.py`](./code/01-deep_time_demo.py) | Compression, ratio arithmetic and interval uncertainty |
| [`code/02-stratigraphic_principles_demo.py`](./code/02-stratigraphic_principles_demo.py) | Field relations as a constraint system; graphic correlation |
| [`code/03-radiometric_dating_demo.py`](./code/03-radiometric_dating_demo.py) | Concordia, discordia, and the assumptions ledger |
| [`code/04-basins_subsidence_demo.py`](./code/04-basins_subsidence_demo.py) | Stretching, thermal subsidence, backstripping |
| [`code/*.py`](./code) | One runnable demo per lesson |

Every demo prints its own numbers and the lessons quote the real output. Run them
with the project environment, from inside `code/`:

```bash
cd 04-earth-science-geology/03-geologic-time-and-stratigraphy/code
.venv/bin/python 03-radiometric_dating_demo.py
```

## How this module treats numbers

Three rules apply to every page in this module, and they are the reason some
sentences are longer than they look.

**No boundary age of the geologic time scale is asserted.** The time scale is an
authoritative chart that has been revised repeatedly, and the ages on it belong
to a dated version of that chart. This module teaches the hierarchy and the
definition mechanism, shows the arithmetic that a chart supports, and requires
you to read the ages from the chart and cite the version. Where a number appears
in a demo it is labelled as a commonly tabulated value, with the instruction to
replace it.

**Decay constants and half-lives are tabulated values.** They differ between
compilations in their last digits, and every age computed from them inherits
that difference. When you quote an age, quote the compilation.

**Every synthetic input is labelled synthetic.** A demonstration that a method
recovers a value it was constructed with is a check on the method, not a
measurement of a rock, and the difference matters.

## Related lessons in other folders

- [02-09-02 Radioactive Decay, Half-Life and Dating](../../02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md)
  — the physics this module uses: the decay law, the isochron equation, closure
  temperature and the compilation problem in half-lives.
- [04-02 Plate Tectonics](../02-plate-tectonics/README.md) — the tectonic
  framework within which basins subside and sequences accumulate.
- [04-04 Structural Geology](../04-structural-geology/README.md) — the next
  module: how the rocks that record this time were deformed after they formed.
- [04-06-01 Source, Reservoir, Seal and Trap: The Petroleum System](../06-petroleum-and-mineral-systems/01-petroleum-system.md)
  — where basin subsidence modelling becomes an exploration tool.
- [13-07 Tectonics, Surface Processes and Climate Coupling](../../13-geodynamics-tectonics/07-geomorphology-tectonics-climate/README.md)
  — the feedback between the subsidence modelled here and the surface processes
  that fill the space it creates.
- [26-02-03 Physical Constants and Earth Parameters with Sources](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the exact/measured/nominal discipline that this module imposes on ages and
  decay constants.

## Common pitfalls across this module

1. **Reading a boundary age as a fact rather than as a chart entry.** The age
   belongs to the version of the chart, and it moves.
2. **Reporting a model age as an age.** If the initial ratio was assumed rather
   than fitted, say so, and state the assumed value.
3. **Treating a date as a measurement.** What was measured was a ratio of
   concentrations; the years came from a model.
4. **Solving a contradictory data set.** When the field relations have no
   consistent order, the output is "no consistent history", not an order.
5. **Fitting an isochron to a mixing line.** A line is not an age until the
   mixing hypothesis has been excluded.
6. **Comparing ages from different chronometers without their closure
   temperatures.** The disagreement is usually the measurement, not the error.
7. **Quoting a subsidence rate without the porosity model.** A backstripped
   curve without a sensitivity table has an unstated error bar, and it is usually
   larger than the signal.
8. **Using a linear time axis for deep time.** On a linear axis long enough to
   hold the age of the Earth, all of recorded history is thinner than a printed
   line.
