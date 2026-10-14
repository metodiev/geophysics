---
id: 16-06-01
title: "Palaeoclimate Proxies: Ice Cores, Sediments, Isotopes"
level: doctoral
prereqs: ["16-02-03", "15-01-01", "16-04-05"]
tags: [atmosphere, climate, palaeoclimate, proxies, isotopes, fractionation, calibration]
---

# Palaeoclimate Proxies: Ice Cores, Sediments, Isotopes

> All models and data in this module are **SYNTHETIC**. Every number below was
> printed by
> [`code/paleoclimate_proxies_demo.py`](code/paleoclimate_proxies_demo.py). The
> fractionation factor is a chosen function of temperature, not a measured
> calibration, and no ice-core record, sediment record or published slope is
> quoted. The physical constants used in the saturation expression are standard
> and are stated in the code.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a palaeoclimate proxy and a proxy system model, and **state** the
   three links (climate → proxy formation → measurement) that a calibration must
   bridge.
2. **Write** the $\delta$ notation for a stable-isotope ratio and **convert**
   between a ratio and a $\delta$ value.
3. **Derive** the Rayleigh distillation equations for the remaining vapour and
   the instantaneous condensate under equilibrium fractionation.
4. **Link** the remaining vapour fraction to temperature through a
   Clausius-Clapeyron saturation curve and **measure** the resulting
   $\mathrm{d}\delta/\mathrm{d}T$.
5. **Quantify** how much the inferred temperature moves when the fractionation
   parameterisation changes — the structural uncertainty of the calibration.
6. **Demonstrate** the degeneracy between source composition and condensation
   temperature for a single measured $\delta$.
7. **State** why a proxy calibration is a model with a domain of validity, not
   an instrument reading.

## Prerequisites

- [16-02-03 The Greenhouse Effect: Physics, Not Rhetoric](../02-radiation-and-energy-balance/03-greenhouse-effect.md) —
  radiative driving of the temperature a proxy responds to.
- [15-01-01 Seawater Properties](../../15-oceanography-marine/01-physical-oceanography/01-seawater-properties.md) —
  the ocean reservoir that exchanges with the atmosphere.
- [16-04-05 The Carbon Cycle: Reservoirs, Fluxes and Perturbations](../04-climate-system-and-feedbacks/05-carbon-cycle.md) —
  the reservoir framework used for any geochemical tracer.

## 1. Intuition: a proxy is a physical process

A thermometer measures temperature. A proxy records a *physical or biological
process* that is sensitive to climate, and the climate signal must be recovered
through a model of that process. Three links sit between the climate variable
you want and the number you measure:

1. **Climate → environment.** Temperature, precipitation, humidity, sea-ice
   cover and seasonality control the local environment.
2. **Environment → archive.** The environment controls how the archive forms:
   snow compaction, isotopic distillation, carbonate precipitation, biological
   growth, sediment deposition.
3. **Archive → measurement.** Extraction, instrumental analysis and age
   modelling turn that into a number with an uncertainty.

A **proxy system model** is an explicit statement of links 1 and 2, and the
calibration is the inversion of that model. Where the calibration is empirical
rather than physical, it is a regression, and it inherits a regression's
assumptions — including the assumption that the modern relationship held in the
past. That assumption is the central weakness of palaeoclimatology, and this
lesson quantifies two of its consequences.

The archives used most widely are ice cores (air bubbles, water isotopes, dust,
chemistry), marine and lake sediments (foraminiferal isotopes and trace-element
ratios, alkenone unsaturation, pollen, organic biomarkers), speleothems
(growth-rate and isotope records), corals (density and trace elements) and
borehole temperature profiles. Each has a different proxy system model and a
different dominant uncertainty. Naming them is easy; quantifying the uncertainty
in each is the research programme.

## 2. Definitions

- **Proxy.** A measurable property of an archive that responds to climate.
- **Calibration.** The mapping from proxy value to climate variable, fitted using
  modern observations or, failing that, laboratory experiments and theory.
- **Transfer function.** A specific calibrated mapping (often linear),
  transportable between sites only under stated assumptions.
- **Fractionation factor.** For two reservoirs $A$ and $B$,
  $\alpha_{A-B} = R_A/R_B$ where $R$ is the ratio of the heavy to the light
  isotope. For water, $\alpha>1$ means the condensate is enriched in the heavy
  isotope relative to the vapour.
- **$\delta$ notation.** For a ratio $R$ relative to a standard $R_{\text{std}}$:
  $$\delta = \left(\frac{R}{R_{\text{std}}}-1\right)\times 1000\ \text{per mil}.$$
- **Rayleigh distillation.** The evolution of an isotope ratio as a reservoir is
  progressively removed, with the product isolated from the residue.

## 3. Derivation: Rayleigh distillation

### 3.1 The vapour

Let $R$ be the isotope ratio of the vapour, and let a fraction
$\mathrm{d}f$ of the vapour condense and be immediately removed. In an
infinitesimal step the vapour loses $\alpha R\,\mathrm{d}f$ of heavy isotope
while losing $\mathrm{d}f$ of total water, so

$$\frac{\mathrm{d}R}{R} = (\alpha-1)\,\frac{\mathrm{d}f}{f}
\quad\Longrightarrow\quad
R = R_0 f^{\alpha-1},$$

where $f$ is the fraction of the original vapour still airborne and $R_0$ is its
initial ratio. In $\delta$ notation, using
$R = (\delta+1000)/1000$ exactly:

$$\boxed{\;\delta_v = (\delta_0 + 1000)\,f^{\alpha-1} - 1000.\;}$$

### 3.2 The instantaneous condensate

Because the condensate is in equilibrium with the vapour at every step, it
fractionates by $\alpha$:

$$\boxed{\;\delta_c = \alpha\,(R_0 f^{\alpha-1})/R_{\text{std}} - 1000
= \alpha(\delta_0+1000)f^{\alpha-1} - 1000.\;}$$

With $\delta_0 = -12.0$ per mil and $\alpha(280\ \mathrm{K}) = 1.00953$ (the
demonstration's chosen synthetic value), the demonstration prints:

| $f$ | $\delta$ vapour (per mil) | $\delta$ condensate (per mil) |
|---|---|---|
| 1.00 | $-12.000$ | $-2.583$ |
| 0.80 | $-14.099$ | $-4.702$ |
| 0.60 | $-16.799$ | $-7.427$ |
| 0.40 | $-20.591$ | $-11.256$ |
| 0.20 | $-27.041$ | $-17.767$ |
| 0.10 | $-33.448$ | $-24.235$ |

Both reservoirs become more negative as the heavy isotope is preferentially
removed. That monotone trend is the physical reason a cold site records a more
negative isotope value — and the reason the trend is a *process*, not a
thermometer.

### 3.3 From $f$ to temperature

A cooling saturated parcel loses moisture according to the saturation mixing
ratio, so the remaining fraction tracks the Clausius-Clapeyron curve,

$$q_s(T) \propto \exp\!\left[-\frac{L}{R_v}
\left(\frac{1}{T}-\frac{1}{T_{\text{ref}}}\right)\right],
\qquad
f(T) = \frac{q_s(T)}{q_s(T_{\text{start}})},$$

with $L = 2.501\times10^{6}\ \mathrm{J\,kg^{-1}}$ and
$R_v = 461.5\ \mathrm{J\,kg^{-1}\,K^{-1}}$ (both standard constants, stated in
the code). Substituting $f(T)$ into the Rayleigh expression makes
$\delta_c$ a function of $T$ alone for a fixed initial state and a fixed
$\alpha(T)$.

## 4. Measurement: the slope of the calibration

Cooling a synthetic parcel from $292.0\ \mathrm{K}$ to $250.0\ \mathrm{K}$ drives
$f$ from $1.000$ to $0.044$ and $\delta_c$ from $-3.341$ to $-36.773$ per mil:

| $T$ (K) | $T$ (°C) | $f$ | $\delta$ condensate (per mil) |
|---|---|---|---|
| 292.0 | 18.85 | 1.000 | $-3.341$ |
| 283.6 | 10.41 | 0.575 | $-7.925$ |
| 275.1 | 1.97 | 0.320 | $-13.403$ |
| 266.7 | $-6.48$ | 0.172 | $-19.939$ |
| 258.2 | $-14.92$ | 0.088 | $-27.734$ |
| 250.0 | $-23.15$ | 0.044 | $-36.773$ |

A least-squares line through these points has slope
$0.7863\ \text{per mil per K}$, i.e. about
$-0.786\ \text{per mil}$ per kelvin of cooling. Two features of that number
matter:

- It is a **slope of a model**, not a constant of nature. It depends on
  $\alpha(T)$, on the condensation path (whether the condensate is removed
  immediately, as assumed, or retained), and on $\delta_0$.
- The relation is **nonlinear**: the discrete table shows $\delta$ falling
  $-4.58$, $-5.48$, $-6.54$, $-7.80$ and $-9.04$ per mil across successive
  equal temperature steps. A linear calibration therefore fits some temperature
  range well and others badly, which is why published calibrations are stated
  with the range over which they were fitted.

## 5. Structural uncertainty of the calibration

Change only the fractionation parameterisation, from
$\alpha = 1 + 0.0090(T_{\text{ref}}/T)^{2}$ to
$\alpha = 1 + 0.0130(T_{\text{ref}}/T)^{2}$, and refit:

| parameterisation | slope (per mil per K) |
|---|---|
| A ($0.0090$) | $0.7863$ |
| B ($0.0130$) | $1.1329$ |
| ratio B/A | $1.4407$ |

Now invert a single measured value, $\delta = -25.0$ per mil:

| parameterisation | implied $T$ (°C) |
|---|---|
| A | $-11.49$ |
| B | $-6.42$ |
| disagreement | $5.07\ \mathrm{K}$ |

Both calibrations are internally consistent, and they differ by five kelvin on
the same measurement. This is **structural uncertainty**: it comes from the
fractionation physics, and no quantity of additional samples of the *same*
proxy removes it. It can only be reduced by an independent constraint on
$\alpha(T)$ — laboratory experiments, or a site where temperature is known
independently.

## 6. Non-uniqueness: source against temperature

Hold the measured condensate at $\delta = -30.0$ per mil and solve for the
combination of source composition $\delta_0$ and implied temperature, using the
parcel's final fraction $f = 0.044$:

| $\delta_0$ (per mil) | required $\alpha$ | implied $T$ (K) | implied $T$ (°C) |
|---|---|---|---|
| $-8.0$ | 1.01056 | 265.98 | $-7.17$ |
| $-10.0$ | 1.00961 | 278.79 | $+5.64$ |
| $-12.0$ | 1.00866 | 293.69 | $+20.54$ |
| $-14.0$ | 1.00771 | 311.31 | $+38.16$ |
| $-16.0$ | 1.00676 | 332.60 | $+59.45$ |

The spread is $66.62\ \mathrm{K}$ over $8$ per mil of source uncertainty, i.e.
about $8.33\ \mathrm{K}$ of implied temperature per per mil of source
composition — in this synthetic model. A single $\delta$ value therefore
constrains a *curve* in $(\delta_0, T)$ space, not a temperature. In practice the
source composition is constrained by the modern hydrological cycle and by the
spatial pattern of many sites; characterising that constraint is the difference
between a defensible reconstruction and a curve-drawing exercise. The structure
of the problem is exactly the underdetermined inverse problem of
[18-01 Foundations of Inverse Problems](../../18-inverse-problems/01-inverse-problem-foundations/README.md).

## 7. Worked example: reading a number honestly

*Problem.* A synthetic ice core yields a layer with $\delta = -25.0$ per mil
under parameterisation A. Quote the implied temperature with its uncertainty.

*Solution.*

1. From the fitted line under A, slope $0.7863$ per mil per K, the implied
   temperature is $-11.49\ \mathrm{{}^{\circ}C}$ (demonstration output).
2. Under parameterisation B it is $-6.42\ \mathrm{{}^{\circ}C}$.
3. The structural spread is $5.07\ \mathrm{K}$.
4. A defensible statement is therefore: "$-11.5\ \mathrm{{}^{\circ}C}$
   $\pm\,5.1\ \mathrm{K}$ from the fractionation parameterisation alone, under
   the assumption that the source composition is known and that the condensate
   was removed immediately."

*Interpretation.* The dominant term in the uncertainty is not noise; it is the
model of fractionation. Quoting only the regression's standard error would
understate the uncertainty by an order of magnitude, and — worse — it would be
an uncertainty of the wrong kind, because structural error does not shrink with
more samples.

## 8. Assumptions and regime of validity

1. **Equilibrium fractionation.** Every condensation step is assumed to reach
   isotopic equilibrium. Kinetic (non-equilibrium) effects during rapid
   deposition, and post-depositional exchange in the snowpack, violate this.
2. **Immediate removal of condensate.** The Rayleigh derivation assumes the
   condensate leaves the parcel at once. Retaining it gives a different
   (closed-system) trajectory, with a different slope.
3. **A single source region and composition.** $\delta_0$ is held fixed. In
   reality the moisture source, its temperature and its trajectory vary, and
   the trajectory mixture changes with climate.
4. **Temperature controls $f$.** The moisture budget is assumed to be
   temperature-driven; circulation changes that alter moisture transport break
   the link.
5. **A smooth, sampled climate.** Extremes and seasonality are averaged; an
   annual-layer proxy records a seasonal-weighted signal, not an annual mean.
6. **Age models.** Every palaeoclimate record carries an age uncertainty,
   frequently larger than the proxy's own. It is a separate error term and must
   not be folded into the calibration.
7. **Domain of validity.** A calibration fitted over a stated temperature range
   has no guarantee outside it.

## 9. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| isotope ratio | $R$ | 1 | heavy/light |
| $\delta$ | | per mil ($10^{-3}$) | $1000(R/R_{\text{std}}-1)$ |
| fractionation factor | $\alpha$ | 1 | ratio of ratios |
| temperature | $T$ | K | |
| latent heat | $L$ | $\mathrm{J\,kg^{-1}}$ | |
| gas constant for water vapour | $R_v$ | $\mathrm{J\,kg^{-1}\,K^{-1}}$ | $L/R_v$ is in K |
| calibration slope | | per mil per K | per mil has no unit |

The exponent in $f^{\alpha-1}$ must be dimensionless, and it is: $\alpha$ is a
ratio. The exponent in the Clausius-Clapeyron expression must also be
dimensionless: $L/R_v$ is a temperature, and multiplying by
$(1/T - 1/T_{\text{ref}})$, which has units $\mathrm{K^{-1}}$, gives a pure
number. Checking this catches the commonest code error in this calculation, a
missing or spurious factor of $1000$ from mixing $R$ and $\delta$.

## 10. Python demonstration

[`code/paleoclimate_proxies_demo.py`](code/paleoclimate_proxies_demo.py):

1. tabulates vapour and condensate $\delta$ against the remaining fraction under
   Rayleigh distillation at fixed temperature;
2. links $f$ to temperature with a Clausius-Clapeyron saturation curve, and fits
   the resulting calibration slope;
3. refits under a second fractionation parameterisation and reports the implied
   temperature difference for one measured value;
4. solves for the $(\delta_0, T)$ pairs consistent with a single measured $\delta$
   and reports the spread.

It is print-only, seeded with `np.random.default_rng(20261014)`, uses the
standard constants $L$ and $R_v$ from the code, and exits 0.

## 11. Exercises

See [`exercises/01-paleoclimate-proxies-exercises.md`](exercises/01-paleoclimate-proxies-exercises.md)
and [`exercises/01-paleoclimate-proxies-solutions.md`](exercises/01-paleoclimate-proxies-solutions.md).

## Mastery checkpoint

> **(a)** With $\delta_0 = -12.0$ per mil, $\alpha = 1.00953$, compute
> $\delta_v$ and $\delta_c$ at $f = 0.5$ by hand and compare with the
> demonstration's table (interpolating between $f = 0.6$ and $f = 0.4$).
> **(b)** State why $\delta_c - \delta_v = (\alpha-1)(\delta_v + 1000)$ and
> evaluate the difference at $f = 0.1$.
> **(c)** The calibration slope is $0.7863$ per mil per K under A and $1.1329$
> under B. For an inferred temperature of $-15\ \mathrm{{}^{\circ}C}$, compute
> the two implied $\delta$ values and the difference between them.
> **(d)** A colleague reports a temperature from a single isotope value with no
> uncertainty. List, in order of magnitude, the two uncertainties they have
> omitted.

## Common pitfalls

1. **Treating a proxy as a thermometer.** Every proxy is a process; the
   calibration is a model of it.
2. **Quoting a regression standard error as the total uncertainty.** Structural
   uncertainty of the calibration dominates, and it is not random.
3. **Ignoring the source composition.** One $\delta$ constrains a curve; the
   demonstration measures an $8.33\ \mathrm{K}$ per per mil sensitivity.
4. **Assuming a linear calibration over a whole range.** Section 4 shows the
   relation bending even over tens of kelvin.
5. **Forgetting the age model.** Dating uncertainty is usually not the smallest
   term.
6. **Transporting a calibration to a different climate regime.** The
   calibration assumes its own environment; the assumption is testable only with
   independent information.

## Related modules

- [16-06 Palaeoclimate](README.md).
- [16-06-02 Model-Data Comparison in Palaeoclimate](02-paleoclimate-model-data.md) —
  what to do with these proxies once their uncertainties are characterised.
- [16-04-05 The Carbon Cycle](../04-climate-system-and-feedbacks/05-carbon-cycle.md) —
  the reservoir framework behind isotope budgeting.
- [15-06 Sea Level Change and Marine Records](../../15-oceanography-marine/06-sea-level-change-marine/README.md) —
  marine archives of the same climate history.
- [18-01 Foundations of Inverse Problems](../../18-inverse-problems/01-inverse-problem-foundations/README.md) —
  underdetermination and null space, which Section 6 exhibits concretely.
