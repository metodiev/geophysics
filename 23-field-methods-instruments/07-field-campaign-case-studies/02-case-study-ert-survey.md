---
id: 23-07-02
title: "Case Study: An ERT Survey from Design to Report"
level: research
prereqs: ["23-04-01", "23-07-01", "18-03-01"]
estimated_minutes: 115
tags: [case-study, ert, resistivity, survey-design, inversion, qc]
---

# Case Study: An ERT Survey from Design to Report

## Learning objectives

By the end of this lesson you will be able to:

1. **Turn** a target depth and a required lateral resolution into a line length, an
   electrode count and a spacing, and **state** which parameter buys which.
2. **Compute** the number of configurations a protocol uses and the fraction of the
   configuration space it represents.
3. **Compute** the injected current from a voltage-limited transmitter and a contact
   resistance, and the signal that arrives at the potential pair.
4. **Choose** a stack count from the noise the survey must beat, and **state** the time it
   costs.
5. **Decide** the model mesh from the data count, and **state** what the resolution claim
   then means.
6. **Design** the QC that runs during acquisition and the error model the inversion will use.
7. **Write** the result so that a reader can tell what the survey resolved and what it did not.

All numbers here are **SYNTHETIC** teaching values combined with the standard relations
quoted in the text (depth of investigation against spread, configuration counting, contact
resistance and Ohm's law, the $\sqrt{N}$ stacking law, the over/under-determination of an
inversion). No real survey, instrument, vendor figure or measured dataset is reproduced.

## Prerequisites

- [23-04-01 ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity](../04-electrical-em-fieldwork/01-ert-fieldwork.md) —
  the field procedure and its geometry arithmetic.
- [23-07-01 Case Study: Deploying a Temporary Seismic Array](01-case-study-seismic-array.md) —
  the same design-to-report sequence for a different method.
- [18-03-01 Why Regularisation Is Justified](../../18-inverse-problems/03-regularization/01-why-regularize.md) —
  the inversion machinery the data feed.

## 1. The requirement

A synthetic near-surface survey must **map a 20 m deep feature with a lateral resolution of a
few metres**, over a line of a few hundred metres. As in the array case study, the requirement
names a depth and a resolution, and those two numbers separate cleanly into two design
parameters: the **spread** of the largest configuration and the **electrode spacing**.

## 2. Geometry: depth is bought with length, resolution with electrode count

With the modelling choice that the depth of investigation is about a fifth of the largest
spread, $L_{\max} \ge 5 \times 20 = 100$ m:

| Electrodes | Spacing | Line | $L_{\max}$ | DOI | Lateral sample |
|---|---|---|---|---|---|
| 21 | 5.0 m | 100.0 m | 100.0 m | 20.0 m | 5.0 m |
| 48 | 5.0 m | 235.0 m | 235.0 m | 47.0 m | 5.0 m |
| 48 | 2.5 m | 117.5 m | 117.5 m | 23.5 m | 2.5 m |
| 64 | 5.0 m | 315.0 m | 315.0 m | 63.0 m | 5.0 m |
| **64** | **2.0 m** | **126.0 m** | **126.0 m** | **25.2 m** | **2.0 m** |

The **64-electrode line at 2 m spacing** is the design chosen: it reaches 25.2 m (a 26 %
margin on the target), and its lateral sampling is 2.0 m — enough for a "few metres" claim.
The 21-electrode line just reaches the target and cannot resolve anything smaller than 5 m;
the 64 at 5 m reaches 63 m, three times deeper than needed, at the cost of the lateral
sampling the requirement asked for.

Two cautions that belong in the design note:

1. **The DOI constant is a modelling choice, not a law.** Values between roughly 0.15 and 0.25
   of the spread appear in practice, and the honest plan quotes the constant, the rule's
   source and a sensitivity check — a 25 % change in the constant is 5 m of depth here.
2. **More electrodes is not always more information.** Each configuration has its own
   sensitivity pattern, and configurations that duplicate coverage at the same depth add data
   volume without adding resolution. The protocol, not the electrode count, is the design.

## 3. Configurations: what fraction of the space is used

With 64 electrodes there are $\binom{64}{4} = 635\,376$ possible four-electrode
configurations, and of those a standard skip-1 protocol (α, β and γ patterns at skip levels
$n = 1\ldots21$) uses 1 953, i.e. **0.31 %**. The acquisition uses a 1 080-measurement subset
chosen for depth coverage. Two consequences:

1. **The 0.31 % is the reason ERT is practical.** A multichannel system switching through a
   protocol is fast precisely because the space is enormous and almost all of it is redundant;
   the design question is which small subset carries the depth and resolution information.
2. **The deepest levels carry the fewest configurations**, and the count falls linearly with
   the skip level:

| Skip level $n$ | $a$ | Spread | DOI | Count |
|---|---|---|---|---|
| 1 | 2.0 m | 6.0 m | 1.2 m | 183 |
| 3 | 6.0 m | 18.0 m | 3.6 m | 165 |
| 6 | 12.0 m | 36.0 m | 7.2 m | 138 |
| 9 | 18.0 m | 54.0 m | 10.8 m | 111 |
| 12 | 24.0 m | 72.0 m | 14.4 m | 84 |
| 21 | 42.0 m | 126.0 m | 25.2 m | 3 |

So the deepest level that reaches the target rests on **three measurements**. That number
belongs in the report: it is the reason the deepest part of the model is smooth, and it is
visible to the reader before any inversion is run.

## 4. Contact resistance, current, and the signal

For a homogeneous half-space with resistivity $\rho$ and a Wenner configuration of spacing
$a$, the transfer resistance is $\rho/(2\pi a)$, so the potential-pair voltage is

$$V = I\,\frac{\rho}{2\pi a} , \qquad I = \frac{V_{\text{tx}}}{2R_c + R_{\text{ground}}} ,$$

and with a 100 V transmitter, $\rho = 50$ Ω·m and $a = 10$ m:

| Contact each | $I$ | $V_{\text{pair}}$ | $V$/noise |
|---|---|---|---|
| 500 Ω | 50.00 mA | 39.789 mV | 198.9 |
| 2 000 Ω | 20.00 mA | 15.915 mV | 79.6 |
| 5 000 Ω | 9.09 mA | 7.234 mV | 36.2 |
| 20 000 Ω | 2.44 mA | 1.941 mV | 9.7 |

with a synthetic 0.2 mV per-measurement noise. Three points:

1. **The contact resistance acts as a signal attenuator**, and it is the *deepest* levels that
   suffer most, because their transfer resistance is smallest ($\rho/2\pi a$ falls as $a$
   grows). A survey that is comfortable at 5 m spacing can be starved at 42 m spacing with the
   same electrodes.
2. **A 20 kΩ contact still gives a factor 10 signal-to-noise**, so it is *not* a failure — but
   it becomes one after the noise model, the stacking and the inversion's tolerance are
   applied.
3. **The remedy order matters**: improve the contact (water, bentonite, deeper electrodes)
   before increasing the stack count, because the stack costs time linearly while the contact
   improvement costs only the installation.

## 5. Stacking: buying noise with time

Noise falls as $\sqrt{N}$ while time rises as $N$:

| Stacks | Seconds per measurement | Time for 1 080 | Relative noise |
|---|---|---|---|
| 1 | 0.60 | 10.8 min | 1.0000 |
| 4 | 2.40 | 43.2 min | 0.5000 |
| 16 | 9.60 | 172.8 min | 0.2500 |
| 64 | 38.40 | 691.2 min | 0.1250 |

So 4 stacks cost 43.2 min of acquisition and buy a factor 2; 64 stacks cost 11.5 hours and buy
a factor 8. **The design rule is to fix the required signal-to-noise from the inversion's
error model, then take the smallest stack count that delivers it** — and here the starting
point is the reciprocal check, which measures the achievable repeatability directly rather
than assuming it.

## 6. The model, the error model and the honest resolution

The inversion needs a mesh, and the mesh has to be defensible:

| Model cells | Data | Cells/data | Status |
|---|---|---|---|
| 100 | 1 080 | 0.09 | over-determined |
| 500 | 1 080 | 0.46 | over-determined |
| 1 080 | 1 080 | 1.00 | at the limit |
| 2 000 | 1 080 | 1.85 | under-determined |
| 10 000 | 1 080 | 9.26 | under-determined |

So a mesh finer than about 500 cells is claiming resolution the data cannot support, and the
reported resolution is then a property of the smoothing, not of the survey. The two standard
defences are a coarse mesh with regularization (which makes the resolution *stated* rather than
hidden) and a resolution analysis that reports, for each part of the model, how well the data
constrain it.

The error model is the other half. A linear model
$\varepsilon = 0.005\lvert V\rvert + 0.2$ mV, with a 5 % reciprocal tolerance, is defensible
and checkable: the synthetic reciprocal errors have zero mean and a standard deviation of
0.789 %, and no datum falls outside the 5 % tolerance — so the error model is conservative,
which is the correct direction to err. If the reciprocal error distribution is not roughly
zero-mean, the *measurement* is biased (a leakage to ground, an electrode in a bad contact, a
cable swap) and no inversion fixes it.

## 7. From data to report

The report's structure follows the design, and each section answers a question the design
already asked:

1. **Requirement and design** (§1–§2): the target, the constant used for the DOI, the line and
   the spacing, and the margin.
2. **Acquisition** (§3–§5): the protocol, its configuration count, the contact resistances
   achieved, the injected currents, the stack count and the total time.
3. **QC**: the reciprocal error distribution with its mean and standard deviation, the number
   of data rejected and why, the repeat measurements at a fixed configuration, and the
   comparison of the two ends of the line (where an electrode in the wrong place shows up as a
   systematic asymmetry).
4. **Inversion**: the mesh, the regularization, the error model, the achieved misfit, and the
   **resolution claim** — for which parts of the model the data constrain the value and for
   which they constrain only a smoothed average.
5. **Interpretation**, with the features that are *not* resolved stated as such: the deepest
   level rests on three measurements, so a thin resistor at the target depth is not resolvable,
   and saying so is part of the result.

## 8. Assumptions and regime of validity

1. **The ground is two-dimensional along the line.** A three-dimensional feature (a small
   tank, a pipe end, a localized plume) is imaged as a smeared body in a 2-D inversion.
2. **The DOI constant applies.** It is a rule of thumb whose constant varies with the array
   and the ground; the plan quotes it, and the interpretation does not lean on it.
3. **The contact resistances are stable through the line.** They change with moisture and
   temperature, so a line acquired over a day has a varying transfer function; the reciprocal
   check is what detects it.
4. **The error model covers the real noise.** It must include, not just random noise, the
   effects of electrode positioning, cable leakage and telluric drift.
5. **The inversion's smoothing is disclosed.** A smooth model is not a statement that the
   ground is smooth; it is a statement that the data do not require it to be rough.
6. **The geometry is measured.** Electrode positions from a tape and a GPS, recorded with the
   line, because the geometric factor is the first thing a reviewer will question.

## 9. The honest summary

- Depth is bought with the largest spread, resolution with the electrode spacing: 64 electrodes
  at 2 m gave a 25.2 m DOI and a 2.0 m lateral sample, where 21 at 5 m gave 20 m of depth and
  5 m of sampling.
- Of $\binom{64}{4} = 635\,376$ possible configurations the protocol uses 1 953 (0.31 %) and
  the acquisition 1 080; the deepest level that reaches the target rests on **three**.
- A 2 000 Ω contact gave 20.00 mA and 15.915 mV at the pair; a 20 000 Ω contact still gave a
  factor 9.7 signal-to-noise, and the deepest levels suffer first.
- Stacking is $\sqrt{N}$ for $N$ times the time: 4 stacks cost 43.2 min and buy a factor 2.
- A mesh finer than ~500 cells is under-determined; the resolution claim is then about the
  smoothing, not the data.
- The reciprocal error distribution (mean, standard deviation, rejections) is the QC that makes
  the error model checkable, and the deepest level's three measurements belong in the report.

## 10. Python demonstration

[`code/case_study_ert_survey_demo.py`](./code/case_study_ert_survey_demo.py) prints every
number quoted above: the geometry table, the configuration counts by skip level, the contact
and current table, the stacking cost, and the model/data ratio with a seeded reciprocal-error
check.

```bash
cd 23-field-methods-instruments/07-field-campaign-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_ert_survey_demo.py
```

## 11. Exercises

Worked problem sets are in
[`exercises/02-case-study-ert-survey-exercises.md`](./exercises/02-case-study-ert-survey-exercises.md)
and
[`exercises/02-case-study-ert-survey-solutions.md`](./exercises/02-case-study-ert-survey-solutions.md).

## 12. Mastery checkpoint

Without notes:

1. A target depth of 30 m with $\mathrm{DOI} = L_{\max}/5$. Compute the minimum spread, then
   the line length and the DOI for 48 electrodes at 4 m spacing.
2. Compute the number of possible configurations for 32 electrodes and the count of a
   skip-1 α/β/γ protocol with $n = 1\ldots10$.
3. With $\rho = 30$ Ω·m, $a = 20$ m, a 200 V transmitter and 3 kΩ per contact, compute the
   current, the pair voltage and the signal-to-noise for a 0.3 mV noise level.
4. Compute the time for 2 000 measurements at 5 stacks of 0.5 s, and the noise factor it buys.
5. For 2 000 data and a 5 000-cell mesh, state whether the problem is over- or
   under-determined and what that implies for the resolution claim.

## 13. Common pitfalls

1. **Choosing the electrode spacing for depth.** The spread sets the depth; the spacing sets
   the sampling.
2. **Assuming a DOI constant without stating it.** It varies with the array and the ground.
3. **Ignoring the deepest levels' data count.** Three measurements cannot support a sharp
   interface.
4. **Buying noise with stacks when the contact is the problem.** Fix the contact first.
5. **Inverting on a mesh finer than the data support.** The smoothing becomes the result.
6. **A QC that reports only the mean error.** The distribution and the sign matter.
7. **Reporting a smooth model as a smooth subsurface.** State the resolution.

## 14. Where this is used

- Near-surface, environmental, geotechnical and archaeological surveys — see
  [23-04-01 ERT Fieldwork](../04-electrical-em-fieldwork/01-ert-fieldwork.md).
- Time-lapse monitoring, where the resolution claim must be made per *difference* rather than
  per absolute model.
- Any inversion-based survey whose credibility rests on a resolution statement rather than on
  a picture — see
  [18-03-01 Why Regularisation Is Justified](../../18-inverse-problems/03-regularization/01-why-regularize.md).

## 15. Related lessons

- [01 Case Study: Deploying a Temporary Seismic Array](01-case-study-seismic-array.md) —
  the same design sequence for an array.
- [03 Case Study: A Magnetotelluric Campaign](03-case-study-mt-campaign.md) —
  where recording time rather than stacking is the currency.
- [23-04-05 Borehole Logging Operations and Tool Calibration](../04-electrical-em-fieldwork/05-borehole-fieldwork.md) —
  the depth control that a borehole check gives an ERT model.
- [23-07-04 Case Study: A Marine Geophysical Cruise](04-case-study-marine-cruise.md) —
  the marine analogue, where the geometry is set by the vessel.

## 16. Self-assessment checklist

- [ ] I can turn a depth and a resolution into a spread, a count and a spacing.
- [ ] I can count configurations and state the fraction of the space used.
- [ ] I can compute the current and pair voltage from a contact resistance.
- [ ] I can choose a stack count from a noise target.
- [ ] I can decide a mesh from the data count.
- [ ] I can design the QC and the error model.
- [ ] I can state what the survey does not resolve.
