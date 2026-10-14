---
id: 13-07-03
title: "Tectonic-Climate Feedbacks on Geological Timescales"
level: research
prereqs: ["13-07-01", "16-04-01", "12-03-01"]
tags: [geodynamics, tectonophysics, climate-feedback, carbon-cycle, weathering, timescales]
---

# Tectonic-Climate Feedbacks on Geological Timescales

> **All models and data in this module are SYNTHETIC.** The fluxes are in chosen
> units of $10^{12}$ mol C per year and every parameter below is a teaching
> value; no published carbon-cycle model is reproduced or quoted. Every number is
> printed by
> [`code/tectonics_climate_feedback_demo.py`](code/tectonics_climate_feedback_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** a zero-dimensional carbonate–silicate box model with a
   weathering sink that depends on the carbon reservoir and on temperature, and
   **find** its steady state.
2. **Derive** the steady-state sensitivity
   $\mathrm{d}\ln N/\mathrm{d}\ln F_{\text{out}} = 1/(a+\beta S/\ln 2)$ and
   **verify** it against an exact steady-state calculation.
3. **Measure** the thermostat gain: how much the temperature dependence of
   weathering reduces the steady-state warming from a change in outgassing.
4. **Derive** the equilibration time $\tau = 1/(a+\beta S/\ln 2)$ in units of the
   reservoir residence time, and **measure** it from an integration.
5. **Demonstrate** that the present-day state alone constrains no parameter, and
   **quantify** how far the inferred palaeo-outgassing diverges between parameter
   sets.
6. **Compute** the climate response to a tectonic forcing scenario and **state**
   which part of the answer is robust and which is not.
7. **Distinguish** a feedback explanation from a forcing explanation for a
   palaeoclimate trend, and name the data that would separate them.

## Prerequisites

- [13-07-01 Erosion, Uplift and Thermochronology](01-erosion-and-uplift.md) —
  the erosion rates that the weathering flux responds to.
- [16-04-01 The Climate System and Its Feedbacks](../../16-atmosphere-climate/04-climate-system-and-feedbacks/README.md) —
  climate sensitivity and feedback language.
- [12-03-01 Radiogenic Heat and the Global Heat Budget](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md) —
  where the tectonic carbon source comes from.
- [16-06 Palaeoclimate](../../16-atmosphere-climate/06-palaeoclimate/README.md) —
  the records a model like this is compared with.

## 1. One equation and one honest difficulty

Over million-year timescales the carbon cycle has a single dominant stabilising
feedback: silicate weathering consumes CO$_2$, its rate increases with
temperature and with runoff, and a warmer world therefore removes CO$_2$ faster.
The balance against volcanic and metamorphic outgassing sets the long-term
CO$_2$ level, and hence the climate, over the timescale on which tectonics
operates.

The honest difficulty is not the physics but the accounting. The present-day
state provides one number; the model has several parameters; and the parameter
combinations that fit today's state disagree about the past by factors of
several. This lesson makes that concrete with the smallest model that shows it.

## 2. The model

State: $N$, the atmosphere–ocean carbon reservoir, in units of
$10^{12}$ mol C. Weathering is an outflux and outgassing an influx:

$$\frac{\mathrm{d}N}{\mathrm{d}t} = F_{\text{out}} - F_w, \qquad
F_w = u\left(\frac{N}{N_0}\right)^{a}e^{\beta(T-T_0)}, \qquad
T = T_0 + S\log_2\!\frac{N}{N_0},$$

where $u$ is a weathering efficiency (the tectonic knob: more fresh rock exposed
means a larger $u$ at the same climate), $a$ is the reservoir exponent, $\beta$
the temperature sensitivity of weathering and $S$ the climate sensitivity in
kelvin per doubling. Chosen reference values: $N_0 = 1$, $T_0 = 15$ °C,
$S = 3$ K per doubling, $a = 0.30$, $\beta = 0.06\ \mathrm{K^{-1}}$,
$F_{\text{out},0} = 1.0$; the reference CO$_2$ is labelled 400 ppmv as a chosen
reference, not a measurement.

The steady states, measured:

| $F_{\text{out}}$ ($10^{12}$ mol C/yr) | $N$ steady | pCO$_2$ (ppmv) | $T$ (°C) |
|---|---|---|---|
| 0.50 | 0.2898 | 115.9 | 9.64 |
| 1.00 | 1.0000 | 400.0 | 15.00 |
| 2.00 | 3.4503 | 1380.1 | 20.36 |
| 4.00 | 11.9045 | 4761.8 | 25.72 |

A factor of four in outgassing gives 5.72 K of warming for 1.8 doublings of
CO$_2$ — a *much* smaller change than the climate sensitivity alone would
predict, and the reduction is the thermostat.

## 3. Derivation: the thermostat gain

Differentiate the steady-state balance $F_{\text{out}} = u(N/N_0)^ae^{\beta(T-T_0)}$
with respect to $F_{\text{out}}$ at fixed $u$, using
$\mathrm{d}T = (S/\ln 2)\,\mathrm{d}\ln N$:

$$\frac{\mathrm{d}\ln N}{\mathrm{d}\ln F_{\text{out}}} = \frac{1}{a + \beta S/\ln 2}.$$

The parameter combination $a + \beta S/\ln 2$ is the *total* sensitivity of the
sink, and the temperature term is the feedback. Measured for the reference set:

| quantity | value |
|---|---|
| $a$ | 0.300 |
| $\beta S/\ln 2$ | 0.260 |
| $a + \beta S/\ln 2$ | 0.560 |
| exponent $1/(a+\beta S/\ln 2)$ | 1.786 |
| exponent without the feedback, $1/a$ | 3.333 |
| multiplier $3.333/1.786$ | 1.866 |

So the feedback reduces the CO$_2$ response to a change in outgassing by a factor
of 1.87 in the exponent. The steady-state temperature change for a doubling of
outgassing, with and without the temperature dependence:

| case | $N$ steady | $T$ (°C) | change from 15 °C |
|---|---|---|---|
| full model ($\beta = 0.06$) | 3.4503 | 20.360 | 5.360 K |
| no temperature feedback ($\beta = 0$) | 10.0794 | 25.000 | 10.000 K |

and the closed form checks against the exact steady states in the small-
perturbation limit:

| change in $F_{\text{out}}$ | closed form (K) | exact steady states (K) |
|---|---|---|
| $+1\%$ | 0.0766 | 0.0769 |
| $+10\%$ | 0.711 | 0.737 |

The agreement is 0.4% at 1% and 3.5% at 10%: the closed form is the small-signal
limit, and the discrepancy at 10% is the curvature of the logarithmic CO$_2$
sensitivity. A feedback statement is a *linearisation*, and its regime must be
stated with it.

## 4. The equilibration time

Linearising the box model about the steady state gives exponential relaxation
with

$$\tau = \frac{1}{a+\beta S/\ln 2}\ \ \text{in units of}\ \ t^* = \frac{N_0}{F_{\text{out}}},$$

measured as $\tau = 1.7867\,t^*$. The demonstration integrates a 5% perturbation
and reads the decay rate off successive samples: the measured $\tau = 1.79464\,t^*$
against the closed form $1.78672\,t^*$, a 0.4% agreement. A 50% perturbation gives
$\tau = 1.90550\,t^*$ — 7% smaller — because the flux law is not linear in $N$,
so the linearised $\tau$ is a small-signal quantity and the discrepancy is the
size of that effect at 50%.

The physical value follows from the units. With chosen (not measured) inputs of
$3.0\times10^{18}$ mol C in the surface reservoir and outgassing of
$1.2\times10^{13}$ mol C/yr, $t^* = 2.5\times10^{5}$ yr and
$\tau = 4.47\times10^{5}$ yr — a few hundred thousand years. This matters for the
interpretation of the tectonic signal: a 10 Myr mountain-building ramp lasts
20 times longer than the equilibration time, so the climate *records* the
tectonic forcing essentially instantaneously, and the observed CO$_2$ history is a
smoothed but faithful image of it. That conclusion is contingent on the
parameters: a larger reservoir or a weaker weathering law lengthens $\tau$ and
restores a lag.

## 5. Worked example: the present state constrains nothing

*Problem.* Three parameter sets are chosen. All three reproduce the present-day
state ($N = N_0$, $T = 15$ °C) for the same outgassing, because the weathering
law is normalised so that $F_w(N_0)$ equals the reference outgassing. What do
they disagree about?

1. **The response to a doubling of outgassing** (measured):

| $a$ | $\beta$ (K$^{-1}$) | $a+\beta S/\ln 2$ | $T$ after doubling (°C) | $\Delta T$ (K) |
|---|---|---|---|---|
| 0.05 | 0.050 | 0.266 | 26.261 | 11.261 |
| 0.30 | 0.060 | 0.560 | 20.360 | 5.360 |
| 0.80 | 0.200 | 1.666 | 16.801 | 1.801 |

A factor of **6.3** between the first and last row, on the same present-day
state.

2. **The outgassing required to explain a given past temperature** (measured,
   by inverting each parameter set):

| target $T$ (°C) | set 1 | set 2 | set 3 | spread |
|---|---|---|---|---|
| 17.0 | 1.131 | 1.295 | 2.159 | $\times1.91$ |
| 19.0 | 1.279 | 1.677 | 4.662 | $\times3.64$ |
| 21.0 | 1.447 | 2.173 | 10.065 | $\times6.96$ |

*Answer.* The three sets are indistinguishable today and differ by up to a factor
of seven in the outgassing they require for a warm past. The degeneracy grows
with the size of the excursion, because the parameter that matters is the *slope*
of the sink law and the excursion probes how non-linear it is. What breaks it is
an independent constraint on the sink: a laboratory or field determination of the
weathering law, a record of the outgassing history, or a proxy that responds to
the reservoir rather than to temperature. A better thermometer does not help —
the degeneracy is between parameters, not between data points.

3. **A tectonic scenario.** A weathering-efficiency ramp from $u = 1.0$ to
   $u = 2.0$ over 10 Myr — the exposure of fresh rock by mountain building —
   cools the model by (measured): 11.261 K for set 1, 5.360 K for set 2 and
   1.801 K for set 3. The same scenario, a factor of 6.3 in the answer.

The robust statement is directional and conditional: *more weathering means less
CO$_2$ and a cooler climate, by an amount that depends on the weathering law*.
A prediction of "2 to 4 °C of cooling from Cenozoic mountain building" is not
wrong, but it is a statement about a parameter choice, and it should be reported
as one.

## 6. Assumptions and regime of validity

1. **A single well-mixed reservoir with fixed atmospheric–ocean partitioning.**
   The ocean's buffering chemistry is the largest omitted process and it changes
   both the timescale and the sensitivity.
2. **No organic carbon, no carbonate weathering, no reverse weathering.** Each is
   a separate sink with its own temperature dependence.
3. **The weathering law's form is assumed.** The exponents $a$ and $\beta$ are
   not measured here; they are the parameters the lesson shows are
   underconstrained.
4. **Climate is a function of CO$_2$ alone.** No palaeogeography, no solar
   evolution, no ice albedo — each of which is a competing explanation for the
   same trend.
5. **Outgassing is a free parameter.** The tectonic *forcing* is not modelled; it
   is prescribed, so the degeneracy between forcing and feedback remains.
6. **Timescales above about $10^{5}$ yr only.** The model has no ocean
   circulation, no biological pump and no short-term variability, so it cannot
   address anything faster than its own equilibration time.

## Mastery checkpoint

Without notes:

1. Write the box model, state each term's physical meaning and find its steady
   state for $F_{\text{out}} = 2F_{\text{out},0}$ with $a = 0.4$, $\beta = 0.05$,
   $S = 3$ K per doubling.
2. Derive $\mathrm{d}\ln N/\mathrm{d}\ln F_{\text{out}} = 1/(a+\beta S/\ln 2)$ and
   evaluate it for those parameters.
3. Explain in two sentences why the thermostat reduces the climate response to a
   change in outgassing, and state what it does *not* reduce.
4. Compute $\tau$ in units of $t^*$ for those parameters, and convert to years
   for $N_0 = 4\times10^{18}$ mol C and $F_{\text{out}} = 10^{13}$ mol C/yr.
5. Given two parameter sets that both fit today's state, explain why a better
   temperature record cannot distinguish them, and name one measurement that
   could.
6. State the Cenozoic cooling question in the form "which observation would
   discriminate between the uplift hypothesis and the climate-feedback
   hypothesis", and say what such an observation would have to look like.

## Common pitfalls

1. **Treating the model's parameters as measured.** The demonstration's three
   sets differ by a factor of 6.3 in their response while agreeing today.
2. **Reporting a feedback result without its regime.** The closed form is a
   small-signal linearisation; it errs by 3.5% at a 10% perturbation here.
3. **Confusing climate sensitivity with the steady-state sensitivity.**
   $S = 3$ K per doubling is not the response to a doubling of outgassing
   (measured here: 5.36 K for the full model with $\beta = 0.06$).
4. **Assuming the climate tracks the forcing without checking $\tau$.** That is a
   calculation, not an assumption.
5. **Attributing a palaeoclimate trend to tectonics without an outgassing
   history.** The forcing and the feedback are degenerate in the same way.
6. **Forgetting that weathering itself needs a supply of fresh rock.** The
   tectonic and climatic controls on $u$ are coupled, and treating $u$ as a
   prescribed ramp is a simplification, not a result.

## Related modules

- [13-07-01 Erosion, Uplift and Thermochronology](01-erosion-and-uplift.md) —
  the erosion rates that set the weathering supply.
- [13-07-02 River Profiles, Steepness Indices and Uplift Inference](02-river-profile-tectonics.md) —
  the uplift history that drives the scenario.
- [16-06 Palaeoclimate](../../16-atmosphere-climate/06-palaeoclimate/README.md) —
  the records such models are compared with.
- [16-04 Climate System and Feedbacks](../../16-atmosphere-climate/04-climate-system-and-feedbacks/README.md) —
  feedback language and climate sensitivity.
- [18-07 Joint and Multi-Physics Inversion](../../18-inverse-problems/07-joint-and-multi-physics-inversion/README.md) —
  combining observables to break a parameter degeneracy.

Companion exercises:
[`exercises/03-tectonics-climate-feedback-exercises.md`](exercises/03-tectonics-climate-feedback-exercises.md)
and
[`exercises/03-tectonics-climate-feedback-solutions.md`](exercises/03-tectonics-climate-feedback-solutions.md).
Run the demonstration with

```bash
cd 13-geodynamics-tectonics/07-geomorphology-tectonics-climate/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tectonics_climate_feedback_demo.py
```
