---
id: 23-06-03
title: "Laboratory Density, Porosity and Permeability Measurement"
level: advanced
prereqs: ["23-06-01", "05-04-01"]
estimated_minutes: 105
tags: [laboratory, density, porosity, permeability, pycnometry, uncertainty]
---

# Laboratory Density, Porosity and Permeability Measurement

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a bulk density from a coated-immersion measurement and **state** why
   the coating must be corrected.
2. **Compute** a grain volume from a Boyle's-law pycnometer, and **compute** the
   sensitivity of the result to the pressure transducer.
3. **Compute** porosity from a grain volume and a bulk volume, and **recognise** the
   algebraic identity of the two forms.
4. **Fit** the Klinkenberg correction to gas-permeability measurements and **report**
   the liquid-equivalent value.
5. **Compute** a permeability from a steady-state flow test and **identify** the
   dominant term in its uncertainty.
6. **Recognise** non-Darcy flow and **state** how a valid test range is demonstrated.

All masses, volumes, pressures and permeabilities here are **SYNTHETIC** teaching values
combined with the standard relations quoted in the text (the mass and volume definitions
of density, Boyle's law, Darcy's law, the Klinkenberg correction, first-order error
propagation). No instrument specification or measured rock property is reproduced.

## Prerequisites

- [01 Sample Preparation, Coring and Drying Protocols](01-sample-preparation.md) —
  the masses, volumes and saturation protocol this lesson assumes.
- [05-04-01 Porosity, Density and Velocity Relationships](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  where these properties are used.

## 1. Intuition: three measurement routes, one unknown too many

Porosity needs a pore volume and a bulk volume; density needs a mass and a volume;
permeability needs a flow, a pressure difference and a geometry. In each case one
quantity must be obtained *indirectly*, and each indirect route brings its own assumption:

| Property | Direct measurement | Indirect measurement | The assumption it brings |
|---|---|---|---|
| Bulk density | mass | bulk volume by immersion, caliper or gamma attenuation | the displaced volume is the solid + void volume |
| Grain density | mass | grain volume by pycnometry or immersion | the gas or fluid reaches every connected pore |
| Porosity | — | pore volume and bulk volume, or the two densities | the two volumes describe the same specimen |
| Permeability | — | a flow rate and a pressure difference, or a transient decay | the flow is laminar, single-phase and Darcy |

The lesson's design rule follows: **measure the property by two routes whose assumptions
differ, and compare.** If the two agree, both assumptions were probably satisfied; if they
disagree, the difference is the measurement's honest uncertainty — and it is almost always
larger than the repeatability of either route alone.

## 2. Bulk density by coated immersion

For a friable specimen a coating (paraffin, wax or a resin film) holds the sample
together and protects the pore fluid from the bath. The coating's volume must then be
subtracted, because it displaces water too:

$$V_{\text{bulk}} = \frac{m_{\text{coated}} - m_{\text{coated,imm}}}{\rho_w}
- \frac{m_{\text{coated}} - m_{\text{dry}}}{\rho_{\text{par}}}.$$

With $m_{\text{dry}} = 176.600$ g, $m_{\text{coated}} = 176.915$ g,
$m_{\text{coated,imm}} = 99.939$ g, $\rho_w = 0.998$ and
$\rho_{\text{par}} = 0.900$ g/cm³:

| Quantity | Value |
|---|---|
| film volume | 0.3500 cm³ |
| coated bulk volume | 77.1303 cm³ |
| corrected bulk volume | 76.7803 cm³ |
| film as a fraction of the coated volume | 0.45 % |
| **bulk density** | **2.3001 g/cm³** |
| density if the film were ignored | 2.2896 g/cm³ (−0.454 %) |

The film is 0.45 % of the volume and ignoring it costs 0.45 % of density — small, but
**systematic and one-signed**: it makes every coated specimen appear less dense. The
correction also cuts the other way for a different reason: the coating seals the surface
pores, so a coated measurement *excludes* the surface porosity that an uncoated one
includes. The two routes therefore differ by the surface porosity plus the film error,
which is why the coated route is used only when the sample would otherwise disintegrate.

## 3. Grain volume by gas pycnometry

A helium pycnometer measures the *solid* volume by Boyle's law. With a cell volume
$V_c$, an expansion volume $V_e$, an initial gauge pressure $p_1$ and a final pressure
$p_2$ after expansion into the cell containing the specimen,

$$V_{\text{solid}} = V_c - V_e\left(\frac{p_1}{p_2} - 1\right) ,$$

and the sensitivity to the final pressure is

$$\frac{\mathrm{d}V_{\text{solid}}}{\mathrm{d}p_2} = \frac{V_e p_1}{p_2^{2}} .$$

For $V_c = 100.00$ cm³, $V_e = 50.00$ cm³, $p_1 = 100.0$ kPa gauge and
$m_{\text{dry}} = 176.600$ g:

| $p_2$ (kPa) | $V_{\text{solid}}$ (cm³) | $\mathrm{d}V/\mathrm{d}p_2$ (cm³/kPa) | Grain density (g/cm³) |
|---|---|---|---|
| 90.0 | 94.4444 | 0.6173 | 1.8699 |
| 70.0 | 78.5714 | 1.0204 | 2.2476 |
| 60.0 | 66.6667 | 1.3889 | 2.6490 |
| 50.0 | 50.0000 | 2.0000 | 3.5320 |
| 40.0 | 25.0000 | 3.1250 | 7.0640 |

Three things to notice. **The sensitivity degrades as $p_2$ falls**: at 60 kPa a 0.5 kPa
transducer error moves the solid volume by 0.6944 cm³, i.e. **1.042 %**, and the grain
density the other way — so the operating point is chosen where the expansion ratio is
large but the final pressure is still well above the transducer's noise. **The resolution
comes from the expansion ratio, not the absolute volumes**: as $p_2 \to p_1$ the
instrument measures nothing ($V_{\text{solid}} \to V_c$). And **a leak or a thermal drift
looks exactly like a wrong grain volume**, so the two-standard calibration before and
after each batch is the only defence — without it a pycnometer drift is
indistinguishable from a mineralogical change.

Helium is used because its molecule is small enough to enter the connected pore space
quickly and does not adsorb strongly at room temperature; the *connected* qualifier
matters, since isolated porosity is invisible to this method and is one of the standard
differences between a pycnometry porosity and a total porosity from a saturation method.

## 4. Porosity from the two volumes

Combining the routes of §2 and §3 on the same material gives the grain density and the
porosity:

$$\rho_g = \frac{m_{\text{dry}}}{V_{\text{grain}}} = \frac{176.600}{66.6667}
= 2.6490\ \mathrm{g/cm^{3}},$$

$$\phi = 1 - \frac{V_{\text{grain}}}{V_{\text{bulk}}}
= 1 - \frac{66.6667}{76.7803} = 0.131721 = 13.1721\ \% ,$$

and, from the two densities,

$$1 - \frac{\rho_b}{\rho_g} = 1 - \frac{2.3001}{2.6490} = 13.1721\ \% ,$$

in agreement to $1.1\times10^{-14}$ percentage points — i.e. to floating-point precision.
**That identity is the point of the exercise.** The two forms are algebraically the same
statement, so a disagreement between them is an arithmetic or unit error, not a property
of the rock. The quantity that can disagree is the *input* pair (a pore volume from
saturation against a grain volume from pycnometry), and it disagrees by the isolated
porosity, the residual air, and the surface-film error of §2.

A useful order-of-magnitude check to carry in the head: filling this specimen's pore space
takes $0.131721 \times 76.7803 \times 0.998 = 10.09$ g of water — the number that must
appear as a mass gain in a saturation experiment, and the number that makes a "20 g mass
gain" immediately suspicious.

## 5. Gas permeability and the Klinkenberg correction

A gas flowing through a porous medium slips along the pore walls, so the measured
permeability is higher than the liquid-equivalent value and depends on the mean pressure.
The Klinkenberg relation is

$$K_{\text{gas}} = K_L\left(1 + \frac{b}{\bar p}\right) ,$$

a **straight line in $1/\bar p$** with intercept $K_L$ and slope $K_L b$. With a synthetic
$K_L = 1.00$ mD and $b = 0.80$ MPa:

| Mean pressure (MPa) | $K_{\text{gas}}$ (mD) | $1/\bar p$ (1/MPa) |
|---|---|---|
| 0.50 | 2.6000 | 2.0000 |
| 1.00 | 1.8000 | 1.0000 |
| 2.00 | 1.4000 | 0.5000 |
| 4.00 | 1.2000 | 0.2500 |

A least-squares fit of $K_{\text{gas}}$ against $1/\bar p$ recovers
$K_L = 1.0000$ mD and $b = 0.8000$ MPa exactly, because the synthetic data are exactly
linear — a useful check that the fitting code is right, but not a check of the *physics*.

Two conclusions that matter in practice. **The low-pressure measurement is not the
permeability**: the 0.5 MPa point is 2.60× the liquid-equivalent value, so a single-point
gas measurement reported as "the permeability" is wrong by a factor that depends on the
pressure, the pore size and the gas. And **the extrapolation is to $1/\bar p = 0$, which is
never measured**, so it amplifies the uncertainty of the lowest-pressure point: the design
rule is to measure at four or more mean pressures spanning a decade, check the linearity
and report the intercept's uncertainty — not to measure at two pressures and draw a line.

## 6. Steady-state liquid permeability and its uncertainty

Darcy's law in the form used by a core-flood apparatus is

$$Q = \frac{K A \Delta p}{\mu L} \qquad\Longrightarrow\qquad
K = \frac{Q \mu L}{A \Delta p} ,$$

with $Q$ the volumetric flow rate, $A$ the cross-sectional area, $L$ the specimen length,
$\Delta p$ the differential pressure and $\mu$ the fluid viscosity. For
$A = 11.40$ cm², $L = 80.0$ mm, $\Delta p = 0.20$ MPa and $\mu = 1.000$ mPa·s (water):

$$Q = \frac{(1.0\times10^{-15})(1.14\times10^{-3})(2.0\times10^{5})}
{(1.0\times10^{-3})(0.080)} = 2.850\times10^{-9}\ \mathrm{m^{3}/s}
= 2.850\ \mathrm{mm^{3}/s} = 0.2462\ \mathrm{L/day} ,$$

i.e. less than a quarter of a litre per day for a 1.013 mD specimen — the reason a
steady-state test on a tight rock takes hours and why transient methods exist.

The uncertainty budget, with the relative uncertainties a typical apparatus reports:

| Term | Relative | Variance share |
|---|---|---|
| flow rate | 1.0 % | 18.87 % |
| length | 0.1 % | 0.19 % |
| area | 0.2 % | 0.75 % |
| **differential pressure** | **2.0 %** | **75.47 %** |
| viscosity | 0.5 % | 4.72 % |
| **combined** | **2.302 %** | 100 % |

**The differential pressure dominates**, at three-quarters of the variance, so the
improvement to make is a better pressure measurement — not a better balance, and not a
better caliper. This is the recurring pattern of the module: the dominant term is the one
that was not measured most carefully, and it is usually a *differential* quantity.

The third check the apparatus must pass is the **validity of Darcy's law**. Adding an
inertial term, $\Delta p = aQ + bQ^{2}$:

| $Q$ (mm³/s) | $\Delta p$ (MPa) | Apparent $K$ (mD) | Fall |
|---|---|---|---|
| 2.8500 | 0.2020 | 1.0032 | 0.00 % |
| 5.7000 | 0.4080 | 0.9934 | 0.98 % |
| 14.2500 | 1.0500 | 0.9650 | 3.81 % |
| 28.5000 | 2.2000 | 0.9211 | 8.18 % |
| 57.0000 | 4.8000 | 0.8444 | 15.83 % |

so an apparent permeability that falls 15.83 % over a 20× range of rate is a statement
about the *flow*, not about the rock. A steady-state result is only a rock property if
$K$ is shown to be independent of $Q$ over the range used, and "shown" means a table like
this one in the report.

## 7. Assumptions and regime of validity

1. **The specimen is a right cylinder.** Both the bulk volume and $A$ and $L$ depend on
   it; the previous lesson's roughness and end-effect discussion applies exactly here.
2. **The pycnometer gas reaches every connected pore.** Isolated pores are invisible, so a
   pycnometry porosity is a *connected* porosity, and it is a lower bound on the total.
3. **The displaced fluid does not enter the pores.** A coating seals them, an uncoated
   immersion floods them; the two routes differ by the surface porosity and must be
   labelled.
4. **Darcy flow is laminar, single phase and isothermal.** Gas flow additionally requires
   the Klinkenberg correction; high rates require the inertial check; clays require a
   controlled salinity and a check for swelling.
5. **The viscosity is known.** It depends on temperature (about 2 % per °C for water) and
   on salinity, so a 5 °C temperature drift is a 10 % permeability error — and the
   temperature is rarely the term the report mentions.
6. **The specimen does not change during the test.** Fines migration, clay swelling and
   dissolution all change $K$ while the test runs, and the repeated measurement at the
   first rate at the end of the sequence is the standard control.

## 8. The honest summary

- Every route to porosity or density has one indirect quantity and therefore one
  assumption: name it.
- A paraffin film of 0.3500 cm³ on a 77.1303 cm³ specimen costs 0.45 % of bulk density if
  ignored, and the error is systematic.
- A helium pycnometer at $p_2 = 60$ kPa gives 66.6667 cm³ and a grain density of
  2.6490 g/cm³; a 0.5 kPa pressure error is 1.042 % of the volume.
- Porosity by the two routes is 13.1721 % either way — they are the same statement, so a
  disagreement is an error, not a rock property.
- Using the same material and the same masses, the specimen's pore space holds 10.09 g of
  water: a useful, checkable number.
- A 0.5 MPa gas measurement is 2.60× the liquid-equivalent permeability of 1.00 mD; the
  correction is fitted as a line in $1/\bar p$ and the intercept is the result.
- The differential pressure dominates the permeability budget at 75.47 % of the variance;
  the combined uncertainty is 2.302 %.
- An apparent permeability that falls 15.83 % over a 20× rate range is a flow result, not
  a rock result.

## 9. Python demonstration

[`code/density_porosity_lab_demo.py`](./code/density_porosity_lab_demo.py) prints every
number quoted above: the coated-immersion density with and without the film correction,
the pycnometry sensitivity table, the porosity by both routes with their difference, the
Klinkenberg table with a least-squares recovery of $K_L$ and $b$, and the steady-state
budget with the non-Darcy demonstration.

```bash
cd 23-field-methods-instruments/06-laboratory-measurements/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python density_porosity_lab_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/03-density-porosity-lab-exercises.md`](./exercises/03-density-porosity-lab-exercises.md)
and
[`exercises/03-density-porosity-lab-solutions.md`](./exercises/03-density-porosity-lab-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A specimen has $m_{\text{dry}} = 145.20$ g, $m_{\text{coated}} = 145.65$ g and
   $m_{\text{coated,imm}} = 83.10$ g, with $\rho_{\text{par}} = 0.90$ and
   $\rho_w = 0.998$ g/cm³. Compute the film volume, the corrected bulk volume and the bulk
   density.
2. A pycnometer with $V_c = 80$ cm³ and $V_e = 40$ cm³ runs from 120 kPa to 75 kPa.
   Compute $V_{\text{solid}}$ and $\mathrm{d}V/\mathrm{d}p_2$.
3. With a grain volume of 52.0 cm³ and a bulk volume of 65.0 cm³, compute the porosity
   and the grain density for $m_{\text{dry}} = 137.8$ g.
4. Gas permeability is 3.2 mD at a mean pressure of 0.4 MPa and 1.6 mD at 1.6 MPa. Fit
   $K_L$ and $b$.
5. State which term dominates a steady-state permeability budget when the flow rate is
   known to 0.5 % and the pressure drop to 3 %.

## 12. Common pitfalls

1. **Ignoring the coating.** It biases every specimen the same way.
2. **Running the pycnometer where the sensitivity is poor.** The expansion ratio is the
   resolution.
3. **Reporting a pycnometry porosity as a total porosity.** It is the connected porosity.
4. **Reporting a single-pressure gas permeability.** Multiply by the correction or say so.
5. **Fitting the Klinkenberg line through two points.** The intercept is an extrapolation;
   use four or more and check the linearity.
6. **Assuming Darcy's law over an unverified rate range.** Show $K$ versus $Q$.
7. **Forgetting the temperature.** Viscosity moves about 2 % per °C for water.

## 13. Where this is used

- Core analysis for reservoir, geothermal and storage projects, where porosity and
  permeability of an interval are the deliverable.
- Rock-physics programmes, where the density and porosity tie the velocities to the
  mineralogy and the fluids — see
  [02 Ultrasonic Velocity Measurement and Pressure Dependence](02-ultrasonic-velocity.md).
- Flow and transport modelling, where $K$ and $\phi$ are the two parameters that set the
  transport, and their uncertainties must be propagated — see
  [08 Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md).
- Any inter-laboratory comparison, where the difference between laboratories is usually
  the protocol rather than the instrument.

## 14. Related lessons

- [01 Sample Preparation, Coring and Drying Protocols](01-sample-preparation.md) —
  the masses and volumes every route here depends on.
- [02 Ultrasonic Velocity Measurement and Pressure Dependence](02-ultrasonic-velocity.md) —
  the same specimens measured dynamically.
- [04 Laboratory Resistivity, IP and Dielectric Measurements](04-electrical-lab-measurements.md) —
  the electrical properties that also depend on the pore geometry.
- [08 Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md) —
  how these budgets are combined and reported.

## 15. Self-assessment checklist

- [ ] I can compute a coated-immersion bulk density with the film correction.
- [ ] I can compute a pycnometer grain volume and its sensitivity.
- [ ] I can compute porosity by two routes and recognise the identity.
- [ ] I can fit a Klinkenberg correction and report the intercept.
- [ ] I can compute a steady-state permeability and its uncertainty budget.
- [ ] I can demonstrate that a test was run in the Darcy range.
