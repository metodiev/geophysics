---
id: 09-01-05
title: "Temperature, Pressure and Frequency Dependence"
level: graduate
prereqs: ["09-01-03", "09-01-04", "01-09-02"]
tags: [electrical-methods, temperature, pressure, compaction, frequency-dependence, arrhenius, permafrost]
---

# Temperature, Pressure and Frequency Dependence

A resistivity is a number with a time stamp, a temperature and a depth attached,
and the three matter more than most textbooks admit. This lesson makes the
dependencies explicit and quantitative: an Arrhenius temperature law whose
implied linear coefficient is derived rather than quoted, a phase-change effect
that dwarfs the mobility effect, a compaction model that links porosity to
depth, and two frequency scales that differ by eight orders of magnitude and
mean completely different things.

**All models and data in this module are SYNTHETIC.** The activation energy, the
unfrozen-water model, the compaction law and the Debye parameters are chosen
teaching values. The Boltzmann constant and the permittivity of free space are
exact SI-defined constants.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the linear temperature coefficient implied by an Arrhenius law and
   evaluate it at a reference temperature.
2. **Quantify** where the linear approximation fails, and how that depends on
   the activation energy.
3. **Compute** the conductivity collapse produced by freezing with a stated
   unfrozen-water model.
4. **Compute** a porosity, formation-factor and conductivity profile from a
   compaction law, and convert depth to effective pressure.
5. **Distinguish** the charge-relaxation frequency from a polarisation
   relaxation frequency and compute both.
6. **Explain** why "DC" means two different things for a resistivity survey and
   for an IP measurement.
7. **State** which of these dependencies must be measured for a given survey.

## Prerequisites

- [09-01-03 Electrolytic, Electronic and Surface Conduction](03-conduction-mechanisms.md) —
  the conduction mechanisms that respond to temperature.
- [09-01-04 Clay Effects, CEC and Membrane Polarisation](04-clay-and-surface-conduction.md) —
  the relaxation whose frequency moves with temperature.
- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md) —
  the diffusive scale that makes charge relaxation fast.

## 1. Temperature: Arrhenius, and the coefficient it implies

Ionic conduction is a thermally activated process, so a reasonable model is

$$\sigma(T) = \sigma_\text{ref}\exp\left[-\frac{E_a}{k_B}
\left(\frac{1}{T} - \frac{1}{T_\text{ref}}\right)\right],$$

with $E_a$ the activation energy, $k_B = 8.617333262\times10^{-5}\
\mathrm{eV\,K^{-1}}$ and $T$ in kelvin. Expand about $T_\text{ref}$:

$$\sigma(T)\approx\sigma_\text{ref}\left[1 + \alpha\,(T - T_\text{ref})\right],
\qquad
\alpha = \frac{E_a}{k_BT_\text{ref}^2}.$$

The linear coefficient is therefore *not* a free parameter: it is fixed by the
activation energy. With the SYNTHETIC $E_a = 0.20\ \mathrm{eV}$ and
$T_\text{ref} = 25\ ^\circ\mathrm{C} = 298.15\ \mathrm{K}$ the demo prints
$\alpha = 0.026109\ \mathrm{K^{-1}}$ — about $2.6\%$ per kelvin.

| $T$ (°C) | 5 | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 |
|---|---|---|---|---|---|---|---|---|---|
| $\sigma$ ($\mathrm{S\,m^{-1}}$), Arrhenius | 0.057137 | 0.066207 | 0.076327 | 0.087567 | 0.100000 | 0.113700 | 0.145190 | 0.182618 | 0.226552 |
| linear form | 0.047782 | 0.060837 | 0.073891 | 0.086946 | 0.100000 | 0.113054 | 0.139163 | 0.165272 | 0.191381 |

The linearisation error reaches $-16.37\%$ at 5 °C and $-15.53\%$ at 60 °C. The
demo also shows how the coefficient scales:

| $E_a$ (eV) | 0.10 | 0.15 | 0.20 | 0.30 | 0.50 |
|---|---|---|---|---|---|
| $\alpha$ ($\mathrm{K^{-1}}$) | 0.013054 | 0.019582 | 0.026109 | 0.039163 | 0.065272 |
| $\sigma(60\,^\circ\mathrm{C})/\sigma(5\,^\circ\mathrm{C})$ | 1.991 | 2.810 | 3.965 | 7.896 | 31.306 |

So a survey that spans 55 K sees a factor 2 to 30 in conductivity depending on
the conduction mechanism — comparable to the whole catalogue range of
[09-01-01](01-resistivity-conductivity.md) over a *single* rock.

## 2. Freezing: phase change beats mobility

Below 0 °C not all the water is liquid. With a SYNTHETIC unfrozen-water model
$w(T) = [1 + (T_f - T)/\Delta T]^{-1}$ for $T < T_f = 0\ ^\circ\mathrm{C}$ and
$\Delta T = 1.0\ \mathrm{K}$, and $\sigma \propto \sigma_w(T)w(T)/F$ with
$F = \phi^{-2}$, $\phi = 0.25$:

| $T$ (°C) | 2 | 0 | $-0.5$ | $-1$ | $-2$ | $-5$ | $-10$ |
|---|---|---|---|---|---|---|---|
| $w(T)$ | 1.0000 | 1.0000 | 0.6667 | 0.5000 | 0.3333 | 0.1667 | 0.0909 |
| $\sigma$ ($\mathrm{S\,m^{-1}}$) | 0.003261 | 0.003065 | 0.002043 | 0.001533 | 0.001022 | 0.000511 | 0.000279 |
| $\rho$ ($\Omega\,\mathrm{m}$) | 306.70 | 326.24 | 489.36 | 652.48 | 978.72 | 1957.44 | 3588.65 |

The conductivity at $-10\ ^\circ\mathrm{C}$ is $11\times$ lower than at
$0\ ^\circ\mathrm{C}$, whereas 25 K of *warming* above zero gives only
$3.3\times$. A phase change is not a mobility effect, and a permafrost survey
that treats the two as one will get both the depth and the temperature wrong.

## 3. Pressure and compaction

Confining pressure reduces porosity, so it reduces resistivity through $F$ —
*unless* the pore water gets saltier with depth, which is the usual case in
sedimentary basins. Using the SYNTHETIC compaction law
$\phi(z) = \phi_0\exp(-z/z_c)$ with $\phi_0 = 0.40$, $z_c = 1500\ \mathrm{m}$,
Archie with $m = 2$ and $\sigma_w = 0.20\ \mathrm{S\,m^{-1}}$, and the effective
pressure $P_\text{eff} = (\rho_b - \rho_w)gz$ with $\rho_b = 2.30\times10^3$ and
$\rho_w = 1.00\times10^3\ \mathrm{kg\,m^{-3}}$:

| $z$ (m) | 0 | 100 | 250 | 500 | 1000 | 2000 | 3000 |
|---|---|---|---|---|---|---|---|
| $\phi$ | 0.4000 | 0.3742 | 0.3386 | 0.2866 | 0.2054 | 0.1054 | 0.0541 |
| $F = \phi^{-2}$ | 6.250 | 7.141 | 8.723 | 12.173 | 23.710 | 89.949 | 341.238 |
| $\sigma$ ($\mathrm{S\,m^{-1}}$) | 0.03200 | 0.02801 | 0.02293 | 0.01643 | 0.00844 | 0.00222 | 0.00059 |
| $\rho$ ($\Omega\,\mathrm{m}$) | 31.25 | 35.71 | 43.61 | 60.87 | 118.55 | 449.75 | 1706.19 |
| $P_\text{eff}$ (MPa) | 0 | 1.275 | 3.188 | 6.377 | 12.753 | 25.506 | 38.259 |

Porosity halves at $z = z_c\ln 2 = 1039.7\ \mathrm{m}$, which is an effective
pressure of $13.260\ \mathrm{MPa}$. Compaction alone makes the formation *more*
resistive with depth; a salinity increase opposes it, and which wins is a
question about the basin, not about Archie. The **effective** pressure is the
correct variable: two formations at the same depth but different pore pressure
have different porosities, which is why pore pressure matters for a resistivity
prediction.

## 4. Frequency: two scales, eight orders apart

Two relaxation processes are relevant, and they are not the same process.

**Charge relaxation.** Any charge imbalance in a conductor decays with the
Maxwell time $\tau_c = \varepsilon/\sigma$. With $\varepsilon_r = 10$ ($\varepsilon_0 = 8.8541878128\times10^{-12}\
\mathrm{F\,m^{-1}}$) and $\sigma = 0.10\ \mathrm{S\,m^{-1}}$:

$$\varepsilon = 10\times8.8541878128\times10^{-12} = 8.8542\times10^{-11}\
\mathrm{F\,m^{-1}}, \quad \tau_c = 8.8542\times10^{-10}\ \mathrm{s},$$

$$f_c = \frac{1}{2\pi\tau_c} = 1.7975\times10^{8}\ \mathrm{Hz}
\ (\approx 180\ \mathrm{MHz}).$$

Below that frequency the fields are diffusive and DC theory applies. Resistivity
frequencies are many decades below it, so **for a resistivity measurement, DC is
exactly right**.

**Polarisation relaxation.** The membrane polarisation of
[09-01-04](04-clay-and-surface-conduction.md) relaxes at $f_c = 1.0\ \mathrm{Hz}$
in the SYNTHETIC model here ($\tau = 0.15915\ \mathrm{s}$):

| $f$ (Hz) | 0.001 | 0.1 | 1 | 10 | 1000 | $10^{5}$ |
|---|---|---|---|---|---|---|
| $\lvert\sigma\rvert$ ($\mathrm{S\,m^{-1}}$) | 0.050000 | 0.050109 | 0.055227 | 0.059909 | 0.060000 | 0.060000 |
| phase (mrad) | 0.2000 | 19.7603 | 90.6599 | 16.5274 | 0.1667 | 0.0017 |

The same rock that is perfectly "DC" at 1 kHz is strongly dispersive at 1 Hz.
The ratio of the two scales is $1.8\times10^{8}$, and the practical consequence
is: **choose the frequency for the quantity you are measuring, and say which.**
Because $\tau$ is temperature-activated ($\tau = \tau_0 e^{E_a/k_BT}$), the
polarisation peak *moves* with temperature, which is why IP is used as a
permafrost and geothermal indicator
([09-03-04](../03-induced-polarisation/04-ip-applications.md)).

## 5. Worked example: a monitoring survey in a thermal plume

A synthetic monitoring target: a sand at $\phi = 0.30$ saturated with water of
$\sigma_w = 0.05\ \mathrm{S\,m^{-1}}$ at $10\ ^\circ\mathrm{C}$, in an aquifer
whose temperature rises to $40\ ^\circ\mathrm{C}$.

1. At 10 °C: $\sigma_w(10) = 0.05\times0.066207/0.066207$ — use
   $\sigma(10)/\sigma(25) = 0.66207$, so $\sigma_w = 0.033104\
   \mathrm{S\,m^{-1}}$.
2. At 40 °C: ratio $1.45190$, so $\sigma_w = 0.072595\ \mathrm{S\,m^{-1}}$.
3. $F = \phi^{-2} = 11.11$, so the bulk conductivity changes from
   $2.979\times10^{-3}$ to $6.534\times10^{-3}\ \mathrm{S\,m^{-1}}$ and the
   resistivity from $335.7$ to $153.1\ \Omega\,\mathrm{m}$.

A $30\ \mathrm{K}$ temperature rise produces the same resistivity change as a
factor-2.2 porosity change would. **A resistivity decrease in a monitoring
survey is not evidence of salinity until temperature is excluded**, and the
reverse is equally true.

## 6. Regime of validity

1. **Single activation energy.** Real conduction has a spectrum of barrier
   heights; the Arrhenius form is a local fit over the useful range.
2. **The linearisation is local.** It is good to a few per cent within about
   $\pm10\ \mathrm{K}$ of the reference temperature.
3. **The unfrozen-water model is synthetic.** Its shape (a sharp drop within a
   kelvin) is the qualitative behaviour to expect, not a calibrated curve.
4. **Compaction without cementation or mineral reaction.** At great depth the
   exponential law fails; diagenesis sets the porosity.
5. **Single relaxation time in the Debye model.** Real rocks need a distribution
   (Cole–Cole); the identity of Section 5 holds for the Debye case.
6. **No salinity change with depth.** Where salinity varies, the temperature
   and salinity effects must be modelled together — or the survey cannot
   separate them.

## 7. Mastery checkpoint

1. Derive $\alpha = E_a/(k_BT^2)$ and evaluate it at $0\ ^\circ\mathrm{C}$ and
   $50\ ^\circ\mathrm{C}$ for $E_a = 0.25\ \mathrm{eV}$. Explain the trend.
2. A sample measures $120\ \Omega\,\mathrm{m}$ at $18\ ^\circ\mathrm{C}$.
   Predict its resistivity at $2\ ^\circ\mathrm{C}$ with $E_a = 0.20\ \mathrm{eV}$
   and state one reason the prediction may fail.
3. Compute the porosity, $F$ and $\rho$ at 750 m in the model of Section 3.
4. Compute the charge-relaxation frequency for $\sigma = 0.005\
   \mathrm{S\,m^{-1}}$ and $\varepsilon_r = 15$, and compare it with the
   polarisation frequencies of Section 4.

## 8. Common pitfalls

1. **Quoting a temperature coefficient without an activation energy.** They are
   the same number (Section 1).
2. **Using the linear form far from the reference temperature.** The error is
   already 16% at 20 K.
3. **Ignoring freezing.** It is a factor-11 effect over 10 K.
4. **Confusing the two frequency scales.** They differ by $10^{8}$.
5. **Converting depth to porosity without effective pressure.** Depth is a proxy;
   pressure is the variable.
6. **Attributing a monitoring change to salinity alone.** Section 5 shows
   temperature alone can do it.

## 9. Related modules

- [09-01-03 Electrolytic, Electronic and Surface Conduction](03-conduction-mechanisms.md).
- [09-01-04 Clay Effects, CEC and Membrane Polarisation](04-clay-and-surface-conduction.md).
- [09-03 Induced Polarisation](../03-induced-polarisation/README.md) and
  [09-03-04 IP Applications](../03-induced-polarisation/04-ip-applications.md).
- [09-07 EM Data Processing, QC and Uncertainty](../07-em-data-processing-and-qc/README.md).
- [09-02 Resistivity Methods](../02-dc-resistivity/README.md) — the measurement
  whose interpretation depends on this lesson.

## 10. Demonstration and exercises

- [`code/temperature_and_pressure_effects_demo.py`](code/temperature_and_pressure_effects_demo.py)
  prints the Arrhenius table, the linearisation error, the freezing collapse,
  the compaction profile with effective pressure, and both frequency scales.
- [Exercises](exercises/05-temperature-and-pressure-effects-exercises.md) and
  [worked solutions](exercises/05-temperature-and-pressure-effects-solutions.md).
