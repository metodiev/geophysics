---
id: 25-01-01
title: "Project: Units, Conversions and First Scientific Plots"
level: beginner
prereqs: ["01-01-03", "03-05-01", "03-05-02", "05-02-02"]
estimated_minutes: 90
tags: [projects, units, dimensional-analysis, plotting, teaching]
---

# Project: Units, Conversions and First Scientific Plots

## Learning objectives

By the end of this project you will be able to:

1. **Convert** a field-sheet table of geophysical measurements to SI units and
   **state** the factor and the target unit for each row.
2. **Derive** the free-air gradient $2g/R$ and the Bouguer slab gradient
   $2\pi G\rho$, and **compute** both in mGal per metre.
3. **Check** an expression dimensionally and **reject** a formula whose two sides
   do not carry the same unit.
4. **Produce** a first scientific figure that carries axis units, an uncertainty
   and a caption consistent with the plotted range.
5. **Diagnose** the three classic beginner errors — a mixed unit system, a
   forgotten factor of $10^{3}$, and a bare number with no unit — from the
   numbers alone.
6. **Grade** your own conversion table against a stated rubric and **justify**
   each mark with a measurement from the table.

All values used in this project are **SYNTHETIC**. They are typed into
[`code/units_and_plotting_demo.py`](./code/units_and_plotting_demo.py) as
teaching numbers; no instrument was read, no archive was queried and no
published measurement is quoted.

## Prerequisites

- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md) —
  the factor table and the dimensional-homogeneity rule used throughout.
- [03-05-01 Matplotlib Figure/Axes Model and Anatomy of a Plot](../../03-scientific-computing/05-plotting-and-visualisation/01-matplotlib-basics.md) —
  the figure anatomy a first plot must respect.
- [03-05-02 Line, Scatter and Error-Bar Plots with Correct Uncertainty](../../03-scientific-computing/05-plotting-and-visualisation/02-line-scatter-plots.md) —
  how an uncertainty gets drawn rather than described.
- [05-02-02 Units and Conventions for Gravity, Magnetic and EM Fields](../../05-core-geophysics/02-geophysical-fields-and-observables/02-field-measurement-units.md) —
  the field conventions (mGal, nT) that this project converts to SI.

## 1. The question

*Can you take a field sheet written in the units people actually use — mGal,
nT, g/cm³, km/s — turn it into SI, and defend every number on it?*

This is deliberately the first project of the folder, because almost every later
one fails in the same way when it fails at all: a quantity is compared with
another quantity in different units, or a formula is applied to a number whose
unit was assumed rather than checked. A conversion table is small enough to
finish in an afternoon and unforgiving enough to expose the habit.

The geophysical motivation is concrete. Gravity is reported in **mGal**
($1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$), the magnetic field in
**nanotesla**, densities in **g cm⁻³**, seismic velocities in **km s⁻¹**. The
SI system wants m s⁻², T, kg m⁻³ and m s⁻¹. The factors are $10^{5}$, $10^{9}$,
$10^{3}$ and $10^{3}$ — large enough that a slip does not look like a slip, it
looks like a discovery.

## 2. The data (SYNTHETIC)

The project uses a six-row teaching table, in the units a field sheet would use:

| quantity | value | unit |
|---|---|---|
| gravity anomaly | 32.5 | mGal |
| target depth | 2.4 | km |
| rock density | 2.67 | g/cm³ |
| seismic velocity | 5.80 | km/s |
| total magnetic field | 48 000 | nT |
| station spacing | 250 | m |

Converted to SI by the demonstration, the same rows become
$3.25\times10^{-4}\ \mathrm{m\,s^{-2}}$, $2400\ \mathrm{m}$,
$2670\ \mathrm{kg\,m^{-3}}$, $5800\ \mathrm{m\,s^{-1}}$,
$4.8\times10^{-5}\ \mathrm{T}$ and $250\ \mathrm{m}$.

**Provenance.** These are chosen teaching values. They are in the range a real
survey would produce, but they are **not** measured, and nothing in this project
depends on their exact size — only on the conversion carrying the right unit.

## 3. The project specification

**Steps.**

1. Write the conversion table with four columns: quantity, field value and unit,
   SI value, SI unit. Fill it by hand first, then check it against the script.
2. Compute the two gravity gradients of §4 and express them in mGal per metre.
3. Take one derived quantity that combines two rows — a time, a ratio, a mass —
   and check its unit by hand before computing it.
4. Produce one figure: a 120-station profile with depth on the vertical axis.
   Label both axes with units and state the uncertainty in the caption.
5. Write a five-line "unit audit" stating, for each number you report, the unit
   and how it was obtained.

**Deliverable.** A conversion table, a figure, and the unit audit.

**Success criterion.** Every reported number carries a unit; every conversion
factor is stated; the figure's axes are labelled and its caption's range matches
the plotted range; the derived quantity's unit follows from the units of its
inputs. A number without a unit is a failure, not a formatting issue.

## 4. Worked example: the two gradients

Both corrections are derivatives of a gravity formula with respect to height, so
both come out in acceleration per length.

The **free-air gradient** differentiates $g = GM/R^{2}$ with respect to $R$:

$$\frac{\mathrm{d}g}{\mathrm{d}R} = -\frac{2GM}{R^{3}} = -\frac{2g}{R}.$$

With $g = 9.8203\ \mathrm{m\,s^{-2}}$ and $R = 6.371\times10^{6}\ \mathrm{m}$,

$$\left|\frac{2g}{R}\right| = \frac{2 \times 9.8203}{6.371\times10^{6}}
= 3.0828\times10^{-6}\ \mathrm{m\,s^{-2}}\ \text{per m}
= 0.3083\ \mathrm{mGal\,m^{-1}}.$$

The **Bouguer slab** term for an infinite horizontal slab of density $\rho$ is

$$2\pi G \rho = 2\pi \times 6.67430\times10^{-11} \times 2670
= 1.1197\times10^{-6}\ \mathrm{m\,s^{-2}}\ \text{per m}
= 0.1120\ \mathrm{mGal\,m^{-1}}.$$

Their ratio is $2.7533$, dimensionless, and it is the reason the two corrections
are always quoted together: for a fixed density the free-air term is larger, and
whether you apply it depends on the measurement height, not on the station.

## 5. Dimensional checking as a habit

The check is mechanical. Write the unit of each input, substitute, and cancel.

- The anomaly ratio has unit $\mathrm{m\,s^{-2}} / \mathrm{m\,s^{-2}}$, so it is
  dimensionless: $3.250\times10^{-4} / 9.8203 = 33.095$ parts per million.
- A length divided by a speed has unit $\mathrm{m} / (\mathrm{m\,s^{-1}})$,
  which is a time: $2400\ \mathrm{m} / 5800\ \mathrm{m\,s^{-1}} = 0.4138\ \mathrm{s}$.
- A formula such as $v = \sqrt{g\,h}$ has unit
  $\sqrt{(\mathrm{m\,s^{-2}})(\mathrm{m})} = \mathrm{m\,s^{-1}}$ — a speed, as
  required.

If the two sides of an equation do not carry the same unit, the equation is
wrong, and no amount of arithmetic will fix it. This is the single cheapest test
available and it catches the majority of beginner errors in later projects.

## 6. What the first figure must carry

The demonstration's synthetic profile has 120 stations at 250 m spacing, so the
horizontal axis runs from $0$ to $29.75\ \mathrm{km}$. The depths have mean
$2392.6\ \mathrm{m}$, standard deviation $57.1\ \mathrm{m}$, range
$2257.2$–$2516.8\ \mathrm{m}$, and a standard error of the mean of $5.21\ \mathrm{m}$.

A figure is honest when:

1. **both axes carry a unit** — "$x$ (km)", "$y$ (m)", not "$x$", "$y$";
2. **the vertical axis is inverted** if it shows depth, and the caption says so;
3. **the uncertainty is drawn** — an error bar, a band, or an explicit
   $\pm$ value in the caption;
4. **the axis limits match the caption** — quoting a range the axes do not show
   is the most common caption defect;
5. **the vertical exaggeration is stated** if the two axes have different units
   per centimetre, because a profile is almost never at true scale.

## 7. Failure modes and how to detect them

1. **Mixed unit systems.** A correction computed in mGal added to an anomaly
   computed in m s⁻². *Detect:* convert every term to one system before adding,
   and print the unit of each intermediate.
2. **Lost factor of $10^{3}$.** g/cm³ used as kg/m³ (off by $10^{3}$), or km used
   as m (off by $10^{3}$). *Detect:* compare the converted value's order of
   magnitude with the expected range — a rock density of 2.67 kg m⁻³ is air.
3. **Bare numbers.** "The anomaly is 32.5" without a unit. *Detect:* read the
   table aloud; if any row is unitless and should not be, it fails.
4. **Dimensionless quantities given a unit.** A ratio of two accelerations is not
   in mGal. *Detect:* cancel the units symbolically before reporting.
5. **A figure whose caption and axes disagree.** *Detect:* read the caption back
   against the plotted limits printed by the script.

## 8. Rubric

| Criterion | 4 — exemplary | 3 — competent | 2 — developing | 1 — incomplete |
|---|---|---|---|---|
| Conversions | All six rows correct, factors stated | One minor slip | Two or more slips | Units mixed |
| Derived gradients | Both derived and in mGal/m | Computed, derivation missing | One wrong | Both wrong |
| Dimensional check | Applied to every derived quantity | Applied once | Mentioned | Absent |
| Figure | Units, uncertainty, inverted depth axis, matching caption | Units and uncertainty | Units only | No units |
| Unit audit | Every number labelled with its source | Most labelled | Some | Absent |

## 9. Assumptions and regime of validity

1. **The gradients are linearised.** $0.3083\ \mathrm{mGal\,m^{-1}}$ is the
   first-order free-air term; it is adequate for height differences of hundreds
   of metres, not for kilometres.
2. **The slab is infinite.** The Bouguer term neglects terrain; on a ridge or in
   a valley the terrain correction is not optional.
3. **$g = 9.8203\ \mathrm{m\,s^{-2}}$ is a spherical-Earth value.** The real
   surface value varies with latitude by about $0.05\ \mathrm{m\,s^{-2}}$; the
   gradient varies by far less, which is why one gradient suffices here.
4. **The synthetic profile is stationary.** Its scatter is drawn from one
   distribution, so the standard error of the mean is meaningful. A profile with
   a trend would need the trend removed first.
5. **A labelled figure is not a correct figure.** Units and error bars are
   necessary and not sufficient; §5 of later projects is where plausibility is
   argued.

## The honest summary

Unit conversion is the cheapest possible check on a quantitative claim and it
catches a class of error that no domain expertise repairs. The deliverable — a
conversion table, two gradients in mGal per metre, and a labelled figure — is
small, and the pass condition is strict: every number carries a unit, every
factor is stated, and the figure's caption matches its axes. The numbers quoted
here belong to synthetic teaching values and constrain nothing about the Earth;
what transfers to real work is the arithmetic of the two gradients
($0.3083\ \mathrm{mGal\,m^{-1}}$ free-air, $0.1120\ \mathrm{mGal\,m^{-1}}$
Bouguer at $2670\ \mathrm{kg\,m^{-3}}$) and the habit of dimensional checking.

## Python demonstration

[`code/units_and_plotting_demo.py`](./code/units_and_plotting_demo.py) prints
every number quoted above. It:

1. converts the six-row field table to SI, printing the factor and the unit;
2. derives and prints the free-air and Bouguer gradients in both m s⁻² m⁻¹ and
   mGal m⁻¹, with their dimensionless ratio $2.7533$;
3. performs the two dimensional checks (the anomaly ratio of $33.095$ ppm and the
   travel time of $0.4138\ \mathrm{s}$);
4. prints the summary statistics a first figure must carry for a 120-station
   synthetic profile.

Run it with the project virtual environment:

```bash
cd 25-projects-capstone/01-beginner-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python units_and_plotting_demo.py
```

The script prints only, writes no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/01-units-and-plotting-exercises.md`](./exercises/01-units-and-plotting-exercises.md)
and
[`exercises/01-units-and-plotting-solutions.md`](./exercises/01-units-and-plotting-solutions.md).
The ★★★ item asks you to design a unit-hygiene procedure for a whole survey, not
to repeat the table.

## Mastery checkpoint

Without notes:

1. Convert $1.5\ \mathrm{mGal}$ to m s⁻², and $2.8\times10^{-5}\ \mathrm{T}$ to nT.
2. State the free-air gradient in mGal m⁻¹ and say, in one sentence, what
   measurement it corrects for.
3. A colleague reports an anomaly of $32.5$ with no unit, and a density of
   $2.67\ \mathrm{kg\,m^{-3}}$. Name the error in each.
4. Your figure shows depth from 2250 m to 2520 m but the caption says
   "2257–2517 m". Which is the defect, and why does it matter?

## Common pitfalls

1. **Reporting a dimensionless ratio with a unit.** $33.095$ ppm is
   dimensionless; writing "$33.095$ mGal" confuses the ratio with the anomaly.
2. **Assuming a conversion factor instead of writing it down.** The factor
   $10^{5}$ for mGal is memorably *large*, which is exactly why a slip is
   invisible in the result.
3. **Plotting depth increasing upwards.** A depth axis that is not inverted
   misleads every reader who knows the convention.
4. **Quoting a gradient without its density.** $0.3083\ \mathrm{mGal\,m^{-1}}$
   is the free-air value; the Bouguer value depends on $\rho$.

## Where this is used

Every subsequent project in this folder inherits this lesson's outputs. The
conversion table pattern reappears in
[25-01-03](./03-gravity-of-earths-layers.md) for shell masses and in
[25-02-02](../02-intermediate-projects/02-simple-gravity-model.md) for anomaly
amplitudes; the figure checklist is enforced again in
[25-01-02](./02-earthquake-map.md) for a map and in
[25-02-03](../02-intermediate-projects/03-fourier-analysis-signals.md) for a
spectrum. In professional practice the same table is the first page of a survey
report, because a unit error found there costs minutes and a unit error found
after modelling costs a field campaign.

## Related lessons

- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md) —
  the factor table this project applies.
- [05-02-02 Units and Conventions for Gravity, Magnetic and EM Fields](../../05-core-geophysics/02-geophysical-fields-and-observables/02-field-measurement-units.md) —
  why the field conventions exist at all.
- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md) —
  the full reduction chain the two gradients below belong to.
- [25-01-03 Computing Gravity Through a Layered Earth](./03-gravity-of-earths-layers.md) —
  the next project, which uses these gradients on a layered model.

## Self-assessment checklist

- [ ] I can convert all six field units to SI from memory and state the factor.
- [ ] I can derive the free-air gradient from $g = GM/R^{2}$.
- [ ] I can compute the Bouguer slab gradient for a given density.
- [ ] I can check any formula dimensionally before trusting its output.
- [ ] I can produce a figure whose axes, caption and uncertainty agree.
- [ ] I can name the five failure modes of §7 and the test for each.
