---
id: 23-06-01
title: "Sample Preparation, Coring and Drying Protocols"
level: advanced
prereqs: ["23-01-03", "05-04-01"]
estimated_minutes: 95
tags: [laboratory, sampling, coring, porosity, preparation, uncertainty]
---

# Sample Preparation, Coring and Drying Protocols

## Learning objectives

By the end of this lesson you will be able to:

1. **Choose** a plug or specimen geometry from the measurement it will feed, and
   **compute** the bias an end effect contributes.
2. **State** a drying stopping criterion that is independent of the clock, and
   **compute** the mass change per 24 h that meets it.
3. **Compute** porosity by three routes — caliper, immersion and grain density — and
   **state** what each route assumes.
4. **Compute** the residual air saturation left by a given evacuation pressure, and
   **state** how it biases a water-saturation measurement.
5. **Compute** the standard error of a porosity mean and the number of plugs a stated
   precision requires.
6. **State** which preparation choices are irreversible, and why they must be decided
   before the core is cut.

All masses, dimensions, densities and pressures here are **SYNTHETIC** teaching values
combined with the standard relations quoted in the text (Boyle's law, the mass and
volume definitions of density and porosity, the standard error of a mean). No
laboratory standard, commercial procedure or measured rock property is reproduced.

## Prerequisites

- [23-01-03 Field Notebooks, Metadata and Data Provenance](../01-field-safety-and-planning/03-field-notebooks.md) —
  the record that makes a sample's history auditable.
- [05-04-01 Porosity, Density and Velocity Relationships](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  the petrophysical definitions used throughout this module.

## 1. Intuition: preparation decides what the measurement can mean

A laboratory measurement is a statement about a **specimen**, and the specimen is
produced by choices that are hard to reverse: how the core was cut, what it was cut
with, how it was cleaned, how it was dried, how it was saturated. Those choices set a
floor on what the downstream measurement can say:

- A plug that is too short for its diameter returns a velocity biased by its ends.
- A plug dried with a fixed oven time returns a water content that depends on its
  clay fraction rather than on the protocol.
- A plug with residual air after "saturation" returns a porosity low by the air
  fraction, and no downstream arithmetic can put the water back.
- A plug whose surface roughness inflates its caliper volume returns a porosity high by
  the roughness fraction.

The remedy is the same in every case: **choose the specimen geometry and the protocol
from the precision the measurement needs**, write the tolerances down before cutting,
and record the deviations that actually happened. Preparation errors are systematic, not
random, so they do not average out with more specimens.

## 2. Geometry: the aspect ratio and the end effect

A specimen's measured property is a property of the specimen *plus its ends*. For a
velocity measurement the common model is an apparent length excess proportional to the
diameter, which makes the velocity bias proportional to the inverse aspect ratio. With a
synthetic excess of $0.10\,D$:

| L/D | Length (mm) for D = 38.10 mm | Length excess | Velocity bias at 4.5 km/s |
|---|---|---|---|
| 1.0 | 38.10 | 10.00 % | 450.0 m/s |
| 1.5 | 57.15 | 6.67 % | 300.0 m/s |
| 2.0 | 76.20 | 5.00 % | 225.0 m/s |
| 2.5 | 95.25 | 4.00 % | 180.0 m/s |
| 3.0 | 114.30 | 3.33 % | 150.0 m/s |

The consequences that matter for planning:

1. **The bias is a percentage of the property, not an absolute offset**, so a longer plug
   is not automatically better for a slower rock: what matters is the bias compared with
   the *between-sample* variability of the study.
2. **The correction is not free.** The excess length can be estimated by measuring two
   plugs of the same material with different lengths, which costs a specimen — the
   standard reason a pilot series is cut before the main one.
3. **The tolerable bias must be stated with the precision target**, e.g. "1 % of velocity
   at 4.5 km/s is 45 m/s, which is smaller than the 1.2 % between-plug scatter, so
   L/D ≥ 2.5 suffices and L/D ≥ 3 is not worth the core".
4. **Ends are also surfaces.** Parallel end faces, flatness and cleanliness matter more
   than length once the ratio is adequate, because a non-parallel face is a *variable*
   bias rather than a fixed one.

## 3. Drying: a criterion instead of a clock

Drying removes the water that occupies pore space; the mass approaches an asymptote
exponentially. With a synthetic $6$ h time constant, starting from $215.90$ g wet and
$200.80$ g dry (water 15.10 g, 6.99 % of wet mass):

| Hours | Mass (g) | Change vs 24 h earlier |
|---|---|---|
| 24 | 201.077 | −7.3822 % |
| 48 | 200.805 | −0.1352 % |
| 72 | 200.800 | −0.0025 % |
| 96 | 200.800 | −0.0000 % |

So a criterion of "less than 0.01 % of dry mass change per 24 h" is first met at 72 h,
and the criterion, not a fixed time, is the protocol. Three reasons:

1. **The time constant is a property of the sample.** A clay-rich or microporous plug has
   a much longer one; a fixed 24 h oven leaves it wet, and the mass error enters every
   subsequent mass-based quantity.
2. **The criterion is a *measurement*, and it can be falsified.** If two successive 24 h
   weighings differ by more than the balance resolution, the sample is not dry; that
   statement can be checked by anyone with the record.
3. **Temperature is itself a compromise.** Higher temperature shortens the drying but
   drives off structural water and alters clays — an irreversible change. The
   temperature must therefore be chosen from what the sample contains and stated.

Also record the balance resolution and the tolerance used: a criterion of 0.01 %
measured on a balance with 0.001 g resolution on a 200 g sample is a difference of
0.02 g, which is 20 counts — adequate. The same criterion on a 0.01 g balance would be
2 counts, i.e. noise, and the sample would appear to dry when it had not.

## 4. Density and porosity: three routes, three assumptions

With dry, saturated and immersed masses of $200.80$, $219.70$ and $126.39$ g, a caliper
cylinder of $38.10$ mm diameter and $83.0$ mm length, and a chosen grain density of
$2.65$ g/cm³:

| Route | Bulk volume | Porosity |
|---|---|---|
| caliper ($\pi d^2 L/4$) | 94.628 cm³ | 20.01 % |
| Archimedes immersion | 93.497 cm³ | 20.26 % |
| grain density, no bulk volume | — | 19.92 % |

with the pore water volume $18.938$ cm³ and the caliper volume $1.0121$ times the
immersion volume ($+1.21$ %). The three routes differ by 0.34 porosity points, which is
the size of the effect that preparation and assumptions contribute — and it is *smaller*
than the between-plug scatter of most studies, which is the only reason any of them is
acceptable.

Each route assumes something different:

1. **Caliper**: the specimen is a right circular cylinder. Surface roughness makes the
   measured volume an envelope, which *overstates* the bulk volume and *understates*
   porosity — the +1.21 % volume here is a −1.20 % porosity bias.
2. **Immersion (Archimedes)**: the specimen is fully saturated and the immersed mass
   has no adhering water film. A wet film inflates both the bulk volume estimate and the
   apparent pore volume, and the two partially cancel — which is why the immersion route
   is the usual reference.
3. **Grain density**: the grain density is known, and no bulk volume is needed. It is the
   only route available for a friable or irregular specimen, and it transfers the entire
   burden onto a *different* measurement — the grain density, usually by pycnometry.

The porosity is then

$$\phi = \frac{V_{\text{pore}}}{V_{\text{bulk}}}
= 1 - \frac{\rho_b}{\rho_g}, \qquad \rho_b = \frac{m_{\text{dry}}}{V_{\text{bulk}}} ,$$

and the second form is the one to reach for when a bulk density is already known, because
it needs no pore volume at all.

## 5. Saturation: the residual gas that survives the vacuum

If the pore space is initially air-filled at atmospheric pressure and is then evacuated,
the air that remains is compressed into the volume of the pore space itself:

$$S_{\text{air}} = \frac{p_{\text{vac}}}{p_{\text{atm}}} ,$$

| Evacuation (Pa) | Residual air (cm³) | $S_{\text{air}}$ |
|---|---|---|
| 100 000 | 18.6923 | 0.9869 |
| 10 000 | 1.8692 | 0.0987 |
| 1 000 | 0.1869 | 0.0099 |
| 100 | 0.0187 | 0.0010 |
| 10 | 0.0019 | 0.0001 |

So a 10 kPa vacuum leaves 9.87 % of the pore space air-filled and **the measured water
saturation is low by that amount** — a 9.9 % relative error on a porosity of 20 %, i.e.
2 porosity points. Three practical consequences:

1. **The evacuation pressure is a specification, not a nicety.** A rough pump leaves
   percent-level air; a good vacuum leaves 0.1 %.
2. **The saturation method must match the measurement.** Low-field techniques can be
   calibrated against the saturating fluid by mass *saturation* differences, which
   avoids the residual-air problem entirely.
3. **The residual air is a systematic error and it is invisible in the dataset.** Every
   specimen made the same way is wrong by the same amount, so the reproducibility is
   excellent and the accuracy is not. Only an independent check — a gravimetric porosity
   from a second route — reveals it.

## 6. Sample size: how many specimens the statement needs

The between-specimen scatter, not the instrument, sets the precision of a reported mean:
with a synthetic between-plug standard deviation of $1.20$ porosity points,

$$\mathrm{se}(\bar\phi) = \frac{s}{\sqrt{n}} ,$$

| $n$ | $\mathrm{se}$ | 95 % half-width | Simulated $\mathrm{se}$ |
|---|---|---|---|
| 3 | 0.6928 | 1.3579 | 0.6834 |
| 5 | 0.5367 | 1.0518 | 0.5487 |
| 8 | 0.4243 | 0.8316 | 0.4166 |
| 12 | 0.3464 | 0.6790 | 0.3489 |
| 20 | 0.2683 | 0.5259 | 0.2695 |
| 40 | 0.1897 | 0.3719 | 0.1908 |

The $\sqrt{n}$ law is the whole story: **halving the half-width costs four times the
specimens**, and 40 plugs give 0.19 points where 12 gave 0.35. The simulated column,
from a seeded normal draw, agrees with the analytic one — which is the cheap way to
check a sampling plan before cutting rock. And the corollary that matters when rock is
scarce: it is usually better to report a mean with an honest uncertainty from 5 plugs
than to cut 20 plugs from a heterogeneous interval and report a mean that describes a
mixture.

## 7. Assumptions and regime of validity

1. **The specimen represents the interval.** Every route above measures a cm-scale
   object; the extrapolation to a formation is a separate claim, usually the weakest one
   in the chain.
2. **Water is the only volatile.** Drying also removes loosely bound water and can alter
   clays, so the "dry mass" is a protocol-defined quantity, not a material constant.
3. **The saturating fluid fully replaces the air.** This is what the $S_{\text{air}}$
   table above tests, and it can fail in microporous or oil-wet samples.
4. **Immersion does not change the specimen.** Swelling clays, dissolution and
   salt-leaching all violate it, and all are common.
5. **The geometry is measurable to the required precision.** A caliper resolution of
   0.01 mm on a 38.10 mm plug is 0.03 % in diameter, hence 0.05 % in volume; the same
   resolution on a 10 mm plug is 0.2 %.
6. **The scatter is random.** Preparation-generated scatter (a badly cut plug) is not, and
   an outlier test that removes it is a *judgement*, which belongs in the record.

## 8. The honest summary

- Preparation choices are systematic: they shift every specimen, so more specimens do not
  remove them.
- A $0.10\,D$ end effect costs 5.00 % of velocity at L/D = 2 — 225 m/s at 4.5 km/s — and
  3.33 % at L/D = 3.
- Drying is controlled by a mass criterion per 24 h, first met at 72 h here with
  $\tau = 6$ h; a fixed oven time is not a protocol.
- Porosity by caliper, immersion and grain density gave 20.01 %, 20.26 % and 19.92 %:
  differences of 0.34 points, each with a different assumption.
- A 10 kPa vacuum leaves 9.87 % of the pore space air-filled; the porosity is low by 2
  points and the dataset will not show it.
- The standard error falls as $1/\sqrt{n}$: 0.54 points at $n = 5$, 0.27 at $n = 20$.
- Record the tolerances before cutting, and record the deviations after.

## 9. Python demonstration

[`code/sample_preparation_demo.py`](./code/sample_preparation_demo.py) prints every
number quoted above: the end-effect table, the drying curve against a per-24 h
criterion, the three porosity routes with their volumes, the residual-air table against
evacuation pressure, and the standard error of a mean with a seeded simulation check.

```bash
cd 23-field-methods-instruments/06-laboratory-measurements/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sample_preparation_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/01-sample-preparation-exercises.md`](./exercises/01-sample-preparation-exercises.md)
and
[`exercises/01-sample-preparation-solutions.md`](./exercises/01-sample-preparation-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A plug has D = 25.0 mm. Compute the velocity bias at L/D = 2 and L/D = 3 for a
   synthetic end effect of $0.10\,D$.
2. A wet sample is 118.40 g and its dry mass is 110.20 g. Compute the water content as a
   percentage of wet and of dry mass.
3. Compute the porosity of a plug with a dry mass of 110.20 g, a saturated mass of
   120.05 g, an immersed mass of 68.30 g and $\rho_w = 0.998$ g/cm³.
4. Compute the residual air fraction after evacuation to 2 kPa.
5. State how many specimens are needed to halve the standard error of a mean.

## 12. Common pitfalls

1. **Choosing a geometry after cutting the core.** Aspect ratio is not recoverable.
2. **A fixed oven time.** It works until the sample is clay-rich.
3. **Quoting a porosity without its route.** The three routes disagree by tens of
   hundredths of a point and by what they assume.
4. **Trusting a vacuum gauge instead of the mass check.** The saturation must be verified
   gravimetrically.
5. **Ignoring surface roughness.** It biases a caliper volume, and it is not random.
6. **Cutting more samples to beat a systematic error.** It cannot.
7. **Reporting a mean without the specimen count.** The precision of the statement is a
   function of $n$.

## 13. Where this is used

- Rock-physics programmes, where velocity, resistivity, permeability and thermal
  properties are all measured on the same plugs — see
  [02 Ultrasonic Velocity Measurement and Pressure Dependence](02-ultrasonic-velocity.md).
- Core analysis in reservoir and geothermal work, where the porosity and permeability of
  an interval are the deliverable.
- Low-field nuclear-magnetic-resonance and dielectric calibrations, whose saturation
  protocol is the source of most of their systematic error.
- Any inter-laboratory comparison, where the *preparation* differs as much as the
  instrument — see
  [08 Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md).

## 14. Related lessons

- [03 Laboratory Density, Porosity and Permeability Measurement](03-density-porosity-lab.md) —
  the measurements this preparation serves.
- [02 Ultrasonic Velocity Measurement and Pressure Dependence](02-ultrasonic-velocity.md) —
  the geometry-sensitive measurement used as the example here.
- [05 Magnetic Laboratory Measurements](05-magnetic-lab-measurements.md) —
  where specimen size and holder background enter the same way.
- [08 Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md) —
  how these systematic errors are reported.

## 15. Self-assessment checklist

- [ ] I can choose a geometry from a precision target and compute the end-effect bias.
- [ ] I can state and check a drying criterion.
- [ ] I can compute porosity by three routes and name each assumption.
- [ ] I can compute a residual air saturation from an evacuation pressure.
- [ ] I can compute a standard error and the specimen count a precision needs.
- [ ] I can say which preparation choices are irreversible.
