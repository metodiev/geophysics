---
id: 23-06-04
title: "Laboratory Resistivity, IP and Dielectric Measurements"
level: research
prereqs: ["23-06-03", "05-04-07"]
estimated_minutes: 110
tags: [laboratory, resistivity, induced-polarization, dielectric, sample-holder, uncertainty]
---

# Laboratory Resistivity, IP and Dielectric Measurements

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the error a contact impedance produces in a two-electrode measurement, and
   **state** why a four-electrode array removes it.
2. **Compute** a geometric factor and the resistivity error a spacing error produces.
3. **Evaluate** a Cole-Cole complex resistivity, its phase spectrum and its percent
   frequency effect.
4. **Convert** an impedance measurement into a complex permittivity, and **locate** the
   relaxation and loss-tangent peaks.
5. **Build** an uncertainty budget for a laboratory resistivity and **identify** the
   dominant term.
6. **State** which electrical quantities are robust and which are dominated by the
   specimen's preparation.

All resistivities, permittivities, relaxation parameters and contact resistances here are
**SYNTHETIC** teaching values combined with the standard relations quoted in the text (the
geometric factor of a sample holder, the four-electrode measurement, the Cole-Cole
relaxation model, the Debye relaxation, the loss tangent). No instrument specification or
measured rock property is reproduced.

## Prerequisites

- [03 Laboratory Density, Porosity and Permeability Measurement](03-density-porosity-lab.md) —
  the porosity and saturation state an electrical measurement depends on.
- [05-04-07 Electrical Properties, Archie's Law and Clay Effects](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md) —
  what the measured resistivity is used to infer.

## 1. Intuition: the specimen holder is part of the measurement

A laboratory electrical measurement places a rock between electrodes, so **two more
interfaces exist than in a field survey**, and they are the interfaces with the largest
and least reproducible impedance in the chain: the rock–electrode contact. Three
consequences organize the whole lesson:

1. **The contact impedance must be excluded, not calibrated.** A two-electrode
   measurement adds both contacts to the specimen's resistance; a four-electrode
   measurement drives current through the outer pair and senses the voltage on the inner
   pair, through which no current flows, so the contacts cancel.
2. **The geometry is the accuracy limit.** Resistivity is proportional to the ratio of a
   length to an area, both measured with a caliper on a specimen whose surfaces are not
   perfect planes.
3. **The pore fluid sets the value.** Resistivity is a property of the rock *and* its
   fluid, so the salinity, the saturation and the temperature — each of which changes the
   value by percent per unit — must be measured with the electrical quantity and reported
   with it.

A fourth, subtler point runs through the lesson: **a resistivity is a function of
frequency**, and so is a permittivity. A single number is only meaningful with the
frequency (or the frequency band) at which it was measured.

## 2. Two electrodes or four: the contact impedance

The specimen's resistance follows from its geometry:

$$R = \frac{\rho L}{A} ,$$

so for $\rho = 50$ Ω·m, $A = 11.40$ cm² and $L = 80.0$ mm the specimen resistance is
$R = 3508.77$ Ω. A two-electrode measurement sees $R + 2R_c$, hence an apparent resistivity

$$\rho_{\text{app}} = \rho\left(1 + \frac{2R_c}{R}\right) :$$

| Contact resistance (each) | Apparent ρ | Error |
|---|---|---|
| 0 | 50.00 Ω·m | 0.00 % |
| 100 Ω | 52.85 Ω·m | +5.70 % |
| 500 Ω | 64.25 Ω·m | +28.50 % |
| 1000 Ω | 78.50 Ω·m | +57.00 % |
| 5000 Ω | 192.50 Ω·m | +285.00 % |

Three lessons from this table:

1. **The error scales as $R_c/R$**, so it is worst for a *conductive* (small-ρ) specimen —
   the opposite of the intuition that a conductive sample is easy to measure.
2. **The contact resistance is not a constant.** It depends on the electrode material, the
   surface finish, the contact pressure, the pore-fluid salinity and time (polarization),
   so it cannot be subtracted as a fixed number. A two-electrode measurement of a resistive
   specimen can be usable; of a conductive one it usually is not.
3. **The four-electrode array removes the contacts from the *measurement* but not from the
   *circuit*.** The current electrodes still need contact, because current must enter the
   specimen; what the array removes is the contact impedance in the *sensing* loop, where
   the input impedance of the voltmeter is many orders of magnitude larger.

## 3. Geometric factor and spacing error

With the four-electrode array the resistivity is

$$\rho = K\frac{\Delta V}{I}, \qquad K = \frac{A}{L} ,$$

so for this holder $K = A/L = 14.25$ mm. The measurement is therefore *linearly*
sensitive to the separation of the potential electrodes:

| Effective sense separation | Apparent ρ | Error |
|---|---|---|
| 78.0 mm | 48.750 Ω·m | −2.50 % |
| 79.0 mm | 49.375 Ω·m | −1.25 % |
| 79.5 mm | 49.688 Ω·m | −0.62 % |
| 80.0 mm | 50.000 Ω·m | 0.00 % |
| 80.5 mm | 50.313 Ω·m | +0.63 % |
| 81.0 mm | 50.625 Ω·m | +1.25 % |
| 82.0 mm | 51.250 Ω·m | +2.50 % |

So a 0.5 mm error in the sense spacing costs 0.63 % and a 2 mm error costs 2.50 % —
comparable to or larger than the voltmeter's contribution (0.5 % in §5). The practical
rules: measure the spacing with a caliper and record it, fix the sense electrodes by a
machined dimension rather than by hand, and check the *sign* of discrepancies — a batch
that is systematically 2.5 % low suggests a bookkeeping error, not a rock.

## 4. Induced polarization: a Cole-Cole spectrum

Induced polarization is the frequency dependence of resistivity, and the standard
phenomenological model is the Cole-Cole complex resistivity:

$$\rho(\omega) = \rho_0\left[1 - m\left(1 - \frac{1}{1 + (i\omega\tau)^{c}}\right)\right] ,$$

with $\rho_0$ the DC resistivity, $m$ the chargeability, $\tau$ the relaxation time and
$c$ a broadening exponent ($c = 1$ is a single Debye relaxation, smaller values a broader
distribution). For $\rho_0 = 50$ Ω·m, $m = 0.30$, $\tau = 1.0$ s and $c = 0.50$:

| Frequency | $\lvert\rho\rvert$ | Phase |
|---|---|---|
| 0.01 Hz | 47.4962 Ω·m | −39.505 mrad |
| 0.10 Hz | 43.6213 Ω·m | −70.162 mrad |
| 1.00 Hz | 38.9182 Ω·m | −63.132 mrad |
| 10.0 Hz | 36.3375 Ω·m | −30.837 mrad |
| 100 Hz | 35.4248 Ω·m | −11.290 mrad |

with the peak of the imaginary part at $1/(2\pi\tau) = 0.1592$ Hz and a percent frequency
effect from 0.1 to 10 Hz of **16.6976 %**.

Four observations that generalise:

1. **Report the phase, not just the magnitude.** The phase is dimensionless, it does not
   depend on $\rho_0$ or on the geometric factor, and it is far less affected by contact
   impedance than the magnitude — because a resistive contact adds a real term, which
   shifts the magnitude but leaves a phase measurement almost intact.
2. **The phase peaks near the relaxation frequency and vanishes at both ends**, so a
   two-frequency survey has to bracket $\tau$; a single-frequency measurement of IP is a
   measurement of whatever happens to be at that frequency.
3. **Two parameters are weakly constrained by a narrow band.** Inverting $m$, $\tau$ and
   $c$ from a decade of data gives large correlated uncertainties, which is why the
   reported quantities should be *observables* (the phase at each frequency, the PFE)
   rather than only the fitted model parameters.
4. **The IP response requires a polarizable interface**, so it grows with clay content,
   sulfide content and the surface area of the pore network — and it *falls* with
   saturation when the conducting phase is disconnected, so the saturation state must be
   reported with the IP number.

## 5. Dielectric measurements: from impedance to permittivity

A dielectric measurement is the same electrical measurement taken at higher frequency and
interpreted as a capacitance. The empty-holder capacitance is $C_0 = \varepsilon_0 A/L$;
with $A = 11.40$ cm² and $L = 80.0$ mm, $C_0 = 0.1262$ pF. The complex permittivity follows
from the measured impedance,

$$\varepsilon^{*}(\omega) = \frac{1}{i\omega C_0 Z(\omega)} ,$$

and a single Debye relaxation with $\varepsilon_s = 20$, $\varepsilon_\infty = 5$ and
$\tau = 1.0$ µs gives

| Frequency | $\varepsilon'$ | $\varepsilon''$ | $\tan\delta$ | $\lvert Z\rvert$ |
|---|---|---|---|---|
| 1 kHz | 19.9994 | 0.0942 | 0.0047 | 63.07 MΩ |
| 10 kHz | 19.9410 | 0.9388 | 0.0471 | 6.319 MΩ |
| 100 kHz | 15.7544 | 6.7572 | 0.4289 | 735.8 kΩ |
| 1 MHz | 5.3706 | 2.3283 | 0.4335 | 215.5 kΩ |
| 10 MHz | 5.0038 | 0.2387 | 0.0477 | 25.18 kΩ |

Two peaks, at different frequencies, and confusing them is a common error:

- $\varepsilon''$ peaks at $1/(2\pi\tau) = 159.155$ kHz;
- $\tan\delta = \varepsilon''/\varepsilon'$ peaks at
  $\sqrt{\varepsilon_s/\varepsilon_\infty}/(2\pi\tau) = 318.310$ kHz, where its value is
  $(\varepsilon_s-\varepsilon_\infty)/(2\sqrt{\varepsilon_s\varepsilon_\infty}) = 0.7500$.

The practical consequences: a "dielectric constant" quoted without a frequency is
meaningless in the relaxation band (here $\varepsilon'$ moves from 19.9994 to 5.0038 across
four decades); the imaginary part and the loss tangent are *different* observables with
different peaks; and the impedance spans four orders of magnitude across the same range,
which is why the instrument's range and its cable capacitance become part of the
calibration. Water's own relaxation lies in the GHz range, so a rock's low-frequency
permittivity is dominated by *bound* water and mineral surfaces — it cannot be predicted
from porosity alone.

## 6. The uncertainty budget, and what dominates

With synthetic relative uncertainties and the terms combined in quadrature:

| Term | Relative | Variance share |
|---|---|---|
| voltage | 0.5 % | 4.50 % |
| current | 0.5 % | 4.50 % |
| length | 0.1 % | 0.18 % |
| area | 0.2 % | 0.72 % |
| temperature (2 %/°C) | 1.0 % | 18.02 % |
| **pore-fluid salinity** | **2.0 %** | **72.07 %** |
| **combined** | **2.356 %** | 100 % |

**The pore fluid dominates at 72 % of the variance**, and the instrument is almost
irrelevant. A 5 % salinity error produces a 5.6 % resistivity error:

| Salinity offset | Apparent ρ |
|---|---|
| −5 % | 55.556 Ω·m |
| −2 % | 52.083 Ω·m |
| 0 % | 50.000 Ω·m |
| +2 % | 48.077 Ω·m |
| +5 % | 45.455 Ω·m |

The design consequences are therefore not about the voltmeter:

1. **Measure and report the pore-fluid conductivity, the saturation and the temperature**
   with every specimen, and convert the fluid conductivity to a *reference* temperature —
   otherwise the scatter between specimens is a scatter between fluids.
2. **Keep the saturation protocol identical** across the batch (see
   [01 Sample Preparation](01-sample-preparation.md)): a residual-air fraction of a few
   percent moves the resistivity by more than the instrument's whole contribution.
3. **Check the holder with a reference specimen** of known resistivity at the start and end
   of each session, which detects the changes (electrode polarization, cable capacitance,
   temperature) that the two-electrode arithmetic cannot predict.

## 7. Assumptions and regime of validity

1. **The specimen is a uniform right cylinder.** Layering, fractures and vugs make the
   measured value a geometric average that is not the matrix resistivity.
2. **The current distribution is uniform.** Four-electrode holders approximate this with a
   guard ring or with sense electrodes well inside the current path; without that, the
   "geometric factor" is a fitted number, not a computed one.
3. **The contacts are stable and non-polarizing.** Steel electrodes polarize; the
   conventional defence is a non-polarizing (reversible) electrode pair and a measurement
   time short compared with the polarization build-up.
4. **The saturation is uniform and known.** Resistivity depends on the *distribution* of
   the fluid as well as its amount, so a partial saturation produced by drying is not
   equivalent to one produced by drainage.
5. **The temperature is stable and measured.** Fluid conductivity moves about 2 % per °C,
   and the specimen's own temperature may lag the bath's.
6. **The model is not the rock.** $m$, $\tau$ and $c$ are fitting parameters of a
   phenomenological model; two processes with the same fitted $\tau$ can have entirely
   different physical origins.

## 8. The honest summary

- The contacts, not the voltmeter, are the first problem: 500 Ω per contact on a 3508.77 Ω
  specimen is a 28.50 % apparent-resistivity error in a two-electrode measurement, and the
  four-electrode array is what removes it.
- The geometric factor is $A/L = 14.25$ mm here; a 0.5 mm spacing error is 0.63 % and a
  2 mm error 2.50 %.
- The Cole-Cole phase peaks near $1/(2\pi\tau) = 0.1592$ Hz and the PFE from 0.1 to 10 Hz is
  16.6976 %; the phase is the robust observable.
- $\varepsilon''$ peaks at 159.155 kHz but $\tan\delta$ peaks at 318.310 kHz with the value
  0.7500 — different observables, different peaks.
- The pore fluid dominates the resistivity budget at 72.07 % of the variance; the combined
  uncertainty is 2.356 % and a 5 % salinity error is 5.6 % of resistivity.
- Every electrical number needs its frequency, its saturation, its fluid and its
  temperature to mean anything.

## 9. Python demonstration

[`code/electrical_lab_demo.py`](./code/electrical_lab_demo.py) prints every number quoted
above: the contact-impedance table, the geometric factor with a spacing-error table, the
Cole-Cole spectrum with the phase and the PFE, the Debye permittivity spectrum with both
peaks, and the uncertainty budget with the salinity sensitivity.

```bash
cd 23-field-methods-instruments/06-laboratory-measurements/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python electrical_lab_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/04-electrical-lab-measurements-exercises.md`](./exercises/04-electrical-lab-measurements-exercises.md)
and
[`exercises/04-electrical-lab-measurements-solutions.md`](./exercises/04-electrical-lab-measurements-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A specimen has $\rho = 5$ Ω·m, $A = 10.0$ cm² and $L = 50.0$ mm. Compute its resistance
   and the apparent resistivity a 200 Ω contact would produce in a two-electrode
   measurement.
2. Compute the geometric factor for $A = 10.0$ cm² and $L = 50.0$ mm, and the spacing error
   that would produce a 1 % resistivity error.
3. For a Cole-Cole model with $\tau = 0.5$ s, compute the frequency of the imaginary-part
   peak.
4. For a Debye relaxation with $\varepsilon_s = 30$, $\varepsilon_\infty = 6$ and
   $\tau = 2$ µs, compute the two peak frequencies and the value of $\tan\delta$ at its
   peak.
5. State the two quantities you would report with a laboratory resistivity and why.

## 12. Common pitfalls

1. **Making a two-electrode measurement on a conductive specimen.** The error is largest
   exactly where it is least expected.
2. **Reporting the spacing from the drawing rather than the caliper.** A 0.5 mm error is
   0.63 %.
3. **Quoting a resistivity without the fluid, the saturation or the temperature.** The
   fluid term dominates the budget.
4. **Reporting only fitted Cole-Cole parameters.** The observables are the defensible
   numbers.
5. **Confusing the $\varepsilon''$ peak with the $\tan\delta$ peak.** They differ by
   $\sqrt{\varepsilon_s/\varepsilon_\infty}$.
6. **Ignoring the holder's own capacitance and the cable.** They enter at high frequency.
7. **Assuming a calibration transfers between sessions.** Electrodes polarize and
   contacts change; the reference specimen is the control.

## 13. Where this is used

- Rock-physics programmes linking resistivity and IP to saturation, clay content and
  texture — see
  [05-04-07 Electrical Properties, Archie's Law and Clay Effects](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md).
- Petrophysical calibration for field and borehole measurements, where the laboratory value
  is the reference.
- Near-surface and environmental work, where the laboratory is used to interpret a field
  resistivity model.
- Any measurement of a rock property in a holder: the contact, geometry and fluid problems
  recur in ultrasonic, thermal and mechanical measurements alike.

## 14. Related lessons

- [01 Sample Preparation, Coring and Drying Protocols](01-sample-preparation.md) —
  the saturation state this measurement depends on above all.
- [03 Laboratory Density, Porosity and Permeability Measurement](03-density-porosity-lab.md) —
  the porosity that sets the fluid-dominated resistivity.
- [05 Laboratory Magnetic Susceptibility and Remanence](05-magnetic-lab-measurements.md) —
  another measurement where the specimen holder is part of the result.
- [08 Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md) —
  how the budget here is reported.

## 15. Self-assessment checklist

- [ ] I can compute the two-electrode error from a contact resistance.
- [ ] I can compute a geometric factor and a spacing-error sensitivity.
- [ ] I can evaluate a Cole-Cole response and its PFE.
- [ ] I can convert an impedance to a complex permittivity and locate both peaks.
- [ ] I can build an electrical uncertainty budget and name the dominant term.
- [ ] I can state what must be reported with every electrical number.
