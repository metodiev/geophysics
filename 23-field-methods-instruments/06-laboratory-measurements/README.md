# Module 23-06 — Laboratory Measurements on Rocks and Fluids

**Stages:** advanced → research · **Prerequisites:** modules 23-01, 23-05;
[05-04-01 Porosity, Density and Velocity Relationships](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md).

This module is about the half of geophysics that happens indoors: the specimen in a holder,
the load frame, the pycnometer, the calorimeter. It follows one specimen through the whole
laboratory sequence — **preparation** (§1), then the properties measured on it:
**ultrasonic velocity** (§2), **density, porosity and permeability** (§3), **electrical
properties** (§4), **magnetic properties** (§5), **thermal properties** (§6), **rock
mechanics** (§7) — and closes with the **uncertainty budget** (§8) that makes all of the
numbers defensible together.

The organising idea is that **each measurement has one indirect quantity and therefore one
assumption, and the assumption is where the error lives**. Porosity needs a bulk volume that
a caliper overstates by the surface roughness (20.01 % against 20.26 % by immersion); a
velocity needs a transducer delay that, ignored, costs 22 % at a 40 mm plug; a permeability
needs a Klinkenberg extrapolation to a pressure that is never measured (a 0.5 MPa
single-point value is 2.60× the liquid-equivalent one); a resistivity needs a contact
impedance that a two-electrode measurement adds in full (a 500 Ω contact is +28.50 %); a
susceptibility needs a $4\pi$ and a normalization (a factor of 12.57 and the density); a
thermal conductivity needs a contact resistance that hides in the temperature drop; a
strength needs the machine's compliance (a 5000 kN/mm frame reads a 34.999 GPa rock as
31.850 GPa).

The second theme is **the difference**: derived properties hinge on the *difference* of two
measurements, and a difference amplifies relative error. The mass difference dominates the
porosity budget at 76.34 % of the variance; the differential pressure dominates the
permeability budget at 75.47 %; the net travel time dominates the velocity budget at 0.1125 %
against 0.0250 % for the length; the pore fluid dominates the resistivity budget at 72.07 %.
In every case the dominant term is the one that was *not* measured most carefully, and in
every case it is visible in the budget before any specimen is cut.

The third theme is **what a laboratory value can and cannot be used for**: a plug is not a
rock mass (a 10× larger specimen is 37 % weaker), a dry specimen is not a saturated one, a
laboratory temperature is not the in-situ temperature, and a laboratory magnetic measurement
at one amplitude is not the field susceptibility. Every lesson states that limit explicitly,
because the alternative — a number transferred without its conditions — is the commonest way
laboratory data are misused.

All numbers in this module are **SYNTHETIC**, combined with the standard relations stated in
each lesson (Boyle's law, Darcy's law, the Klinkenberg correction, the geometric factor of a
sample holder, the Cole-Cole and Debye relaxations, the log-Gaussian IRM law, the S-ratio,
Fourier's law in a divided bar, the error-function surface-step solution, mixing laws, linear
elasticity, Mohr-Coulomb, Byerlee's law, the GUM-style uncertainty combination, the
$E_n$ score). No laboratory standard, certificate, instrument specification, manufacturer
figure or measured rock property is used or reproduced.

## Learning objectives

By the end of this module you will be able to:

1. **Choose** a specimen geometry and a preparation protocol from the precision the
   measurement needs, and **compute** the end-effect and drying biases.
2. **Compute** a velocity with its transducer delay, its elastic moduli and its
   pressure dependence, and **build** its uncertainty budget.
3. **Compute** density, porosity and permeability by their alternative routes, and
   **recognise** the algebraic identities that must hold.
4. **Compute** the errors that contacts, spacings and pore fluids produce in electrical
   measurements, and **interpret** a Cole-Cole and a Debye spectrum.
5. **Convert** between magnetic units and normalizations, and **interpret** the ratios that
   separate concentration from grain size.
6. **Compute** thermal conductivity, diffusivity and effusivity, and **integrate** a
   temperature-dependent conductivity over a geotherm.
7. **Fit** a Mohr-Coulomb criterion, **apply** Byerlee's law and **compute** the rate and
   size effects on strength.
8. **Build** an uncertainty budget, **identify** its dominant term and **report** the result
   with defensible significant digits.
9. **State** the limits that no laboratory measurement removes: the specimen's scale, its
   saturation, its stress state and its temperature.

## Prerequisites

- [23-01-03 Field Notebooks, Metadata and Data Provenance](../01-field-safety-and-planning/03-field-notebooks.md) —
  the record that makes a specimen's history auditable.
- [23-05-04 Calibration, Testing and Traceability](../05-instrumentation-and-electronics/04-calibration-and-testing.md) —
  the calibration budget and traceability chain the laboratory budgets start from.
- [05-04-01 Porosity, Density and Velocity Relationships](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  the petrophysical relations these measurements feed.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Sample Preparation, Coring and Drying Protocols](01-sample-preparation.md) | advanced | A $0.10\,D$ end effect is 5.00 % of velocity at L/D = 2; a 10 kPa vacuum leaves 9.87 % residual air; the three porosity routes differed by 0.34 points |
| 02 | [Ultrasonic Velocity Measurement and Pressure Dependence](02-ultrasonic-velocity.md) | research | Ignoring a 2.5 µs delay cost 22 %; $K$ moved 1.6 % per 1 % of $V_S$; the timing term dominated the budget 0.1125 % against 0.0250 % |
| 03 | [Laboratory Density, Porosity and Permeability Measurement](03-density-porosity-lab.md) | advanced | A pycnometer at $p_2 = 60$ kPa gave 66.6667 cm³ and 2.6490 g/cm³; porosity was 13.1721 % by both routes; a 0.5 MPa gas value was 2.60× the liquid-equivalent one |
| 04 | [Laboratory Resistivity, IP and Dielectric Measurements](04-electrical-lab-measurements.md) | research | A 500 Ω contact was +28.50 % in a two-electrode measurement; the PFE was 16.6976 %; the pore fluid was 72.07 % of the variance |
| 05 | [Laboratory Magnetic Susceptibility and Remanence (IRM, ARM)](05-magnetic-lab-measurements.md) | research | Omitting the $4\pi$ is 12.57×; the same specimen gave 0.9524 and 0.1667 of $\kappa_0$ at 10 and 1000 A/m; a 0.50 cm³ holder is +100 % on a 0.50 cm³ chip |
| 06 | [Thermal Conductivity, Diffusivity and Specific Heat](06-thermal-lab-measurements.md) | research | A 1 K error on a 6 K drop is 17 %; ignoring $K(T)$ cost 2.45 % of heat flow; the mixing models spanned 51.20 % |
| 07 | [Rock Mechanics Testing: Strength, Friction, Fracture](07-rock-mechanics-lab.md) | research | A 5000 kN/mm frame read 31.850 GPa for a 34.999 GPa rock; reactivation needed $\sigma_1/\sigma_3 \approx 12.3$; a 10× size change was 37 % weaker |
| 08 | [Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md) | research | The certificate was 70.56 % of the variance; the mass difference 76.34 %; $E_n$ tests the budgets as much as the values |

## Suggested path

**If you are preparing core for a measurement programme:** 01, then the lesson for the first
property you will measure — 02 for velocity, 03 for density and permeability, 04 for
resistivity, 05 for magnetics, 06 for thermal, 07 for strength.

**If you are designing an apparatus or a holder:** 01 §2–§3 for geometry, then the relevant
property lesson; every one of them has a contact-or-holder section, and they are the same
argument in different units.

**If you are writing up a dataset:** 08 first for the reporting rules, then each property
lesson's budget section to assemble the terms.

**If you are comparing with a field measurement:** each lesson's "what cannot be supported"
paragraph, and §8 for the $E_n$ machinery that turns the comparison into a defensible
statement.

**If you are reviewing someone else's laboratory data:** check the conditions list in each
lesson's assumptions section against what the dataset actually states; the missing one is
usually the saturation or the temperature.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-sample-preparation.md`](01-sample-preparation.md) | Lesson 01 |
| [`02-ultrasonic-velocity.md`](02-ultrasonic-velocity.md) | Lesson 02 |
| [`03-density-porosity-lab.md`](03-density-porosity-lab.md) | Lesson 03 |
| [`04-electrical-lab-measurements.md`](04-electrical-lab-measurements.md) | Lesson 04 |
| [`05-magnetic-lab-measurements.md`](05-magnetic-lab-measurements.md) | Lesson 05 |
| [`06-thermal-lab-measurements.md`](06-thermal-lab-measurements.md) | Lesson 06 |
| [`07-rock-mechanics-lab.md`](07-rock-mechanics-lab.md) | Lesson 07 |
| [`08-lab-data-uncertainty.md`](08-lab-data-uncertainty.md) | Lesson 08 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Eight runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/sample_preparation_demo.py`](code/sample_preparation_demo.py) | End-effect bias, drying criterion, three porosity routes, residual-air saturation, standard error of a mean |
| [`code/ultrasonic_velocity_demo.py`](code/ultrasonic_velocity_demo.py) | Travel time and delay, wavelength criterion, elastic moduli, pressure dependence, uncertainty budget |
| [`code/density_porosity_lab_demo.py`](code/density_porosity_lab_demo.py) | Coated-immersion density, pycnometry sensitivity, porosity by both routes, Klinkenberg fit, non-Darcy range |
| [`code/electrical_lab_demo.py`](code/electrical_lab_demo.py) | Contact impedance, geometric factor, Cole-Cole spectrum, Debye permittivity, salinity-dominated budget |
| [`code/magnetic_lab_demo.py`](code/magnetic_lab_demo.py) | Unit conversions, field dependence, IRM acquisition and S-ratio, ARM ratios, holder background |
| [`code/thermal_lab_demo.py`](code/thermal_lab_demo.py) | Divided-bar conductivity, $K(T)$ integration, $c_p$–$\alpha$–$e$, surface-step penetration, mixing laws |
| [`code/rock_mechanics_demo.py`](code/rock_mechanics_demo.py) | Moduli and machine compliance, Mohr-Coulomb fit, Byerlee reactivation, brittleness, rate and size effects |
| [`code/lab_uncertainty_demo.py`](code/lab_uncertainty_demo.py) | Type A + B budget, effective degrees of freedom, propagated porosity, reporting, $E_n$ scores, variance components |

## How to run the demos

Use the project virtual environment:

```bash
cd 23-field-methods-instruments/06-laboratory-measurements/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sample_preparation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ultrasonic_velocity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python density_porosity_lab_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python electrical_lab_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_lab_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermal_lab_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rock_mechanics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python lab_uncertainty_demo.py
```

Each demo prints labelled results under numbered section banners, starts from
`np.random.default_rng(20261014)` wherever randomness is used, uses no network and no file
I/O, prints a `SYNTHETIC` provenance line and exits 0. All eight run in under 0.2 s.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A 60 cm core of tight sandstone is available, and you must publish porosity, permeability,
> $V_P$, $V_S$ and thermal conductivity for 10 plugs, each with a defensible uncertainty, plus
> the reactive potential of the rock at 1.5 km depth. **(a)** Write the preparation protocol:
> plug geometry with the arithmetic that justifies it, the drying criterion, the saturation
> procedure with the residual-air calculation, and the specimens each property will use.
> **(b)** For each property, name the dominant uncertainty term and its arithmetic, and state
> which properties are preparation-limited rather than instrument-limited. **(c)** Compute the
> heat capacity term you need and whether you need it at all. **(d)** Assemble the thermal
> conductivity budget and state whether a 5 % target is met. **(e)** Fit Mohr-Coulomb from
> three triaxial tests and compute the reactivation ratio for $\mu = 0.6$ at the in-situ
> effective stress. **(f)** State the three things a reader of your data table cannot recover
> from the numbers alone.

## Common pitfalls across this module

1. **Cutting the specimen before writing the precision target.** Geometry, drying and
   saturation are irreversible.
2. **Quoting a property without its conditions.** Saturation, temperature, stress, fluid and
   frequency change every one of the properties in this module.
3. **Missing the indirect quantity.** Every route here has one, and it carries the
   assumption.
4. **Reporting only the repeatability.** The dominant term is usually a systematic one, and it
   is rarely the repeat.
5. **Using a difference without noticing.** Differences amplify relative errors, and they
   dominate most of the budgets here.
6. **Confusing a derived quantity with a measured one.** $\alpha$, $e$, the elastic moduli,
   $K_L$, the S-ratio and the porosity from densities are all combinations.
7. **Transferring a laboratory value without its scale.** A plug is not a rock mass, a dry
   specimen is not a saturated one, and a laboratory field is not the Earth's field.
8. **A budget with no dominant term identified.** The effort then goes to the wrong
   measurement.
9. **An $E_n$ far below 1 treated as excellence.** It is often an overstated budget.

## Related modules

- [23-05 Instrumentation and Electronics for Geophysics](../05-instrumentation-and-electronics/README.md) —
  the instruments, their calibration and the traceability chain.
- [23-03 Gravity and Magnetic Fieldwork](../03-gravity-magnetic-fieldwork/README.md) —
  the field magnetic measurements the laboratory susceptibilities serve.
- [23-04 Electrical and EM Fieldwork](../04-electrical-em-fieldwork/README.md) —
  the field electrical measurements the laboratory resistivities calibrate.
- [23-07 Field Campaign Case Studies](../07-field-campaign-case-studies/README.md) —
  the campaigns that combine field and laboratory data.
- [05 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md) —
  the relations these measured properties are used in.
