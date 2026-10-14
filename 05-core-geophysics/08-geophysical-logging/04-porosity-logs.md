---
id: 05-08-04
title: "Density, Neutron and Sonic Porosity Logs"
level: graduate
prereqs: ["05-04-01", "05-08-02", "02-09-05"]
tags: [density-log, neutron-porosity, sonic-log, photoelectric-factor, nmr, gas-effect, inversion]
---

# Density, Neutron and Sonic Porosity Logs

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what each porosity tool physically measures — Compton scattering for
   density, hydrogen moderation for the neutron, elastic slowness for the sonic,
   and proton relaxation for NMR — and why none of them measures porosity.
2. **Derive** the density-porosity relation from a volume balance, including the
   electron-density and photoelectric corrections, and state its assumptions.
3. **Explain** why the neutron log is *not* a unique porosity measurement, using
   the hydrogen index, and derive the gas effect on the density–neutron pair.
4. **Derive** the sonic time-average relation and prove numerically that a
   *slowness* log integrates to a travel time, then state the consequence for a
   well tie.
5. **Forward-model** a synthetic density, neutron and sonic log from a layer
   model and **invert** it, recovering porosity in the favourable case and
   demonstrating the failure in the unfavourable one.
6. **Choose** which porosity answer to believe when the three logs disagree, and
   state the assumption each choice rests on.

## Prerequisites

- [05-04-01 Porosity, Density and Velocity Relationships](../04-rock-physics/01-porosity-density-velocity.md)
  — the volume-balance relations used throughout.
- [05-08-02 Natural Gamma and Spectral Gamma Logging](./02-gamma-logging.md)
  — the nuclear measurements that do not irradiate the formation, for contrast.
- [02-09-05 Neutron Interactions and Borehole Nuclear Measurements](../../02-physics/09-radiation-and-atomic-physics/05-neutron-interaction.md)
  — moderation, the hydrogen index and the capture processes.

## 1. Intuition: four tools, four different averages, none of them "porosity"

Porosity is a geometric quantity: the fraction of a rock's volume that is not
solid. It cannot be measured from a borehole directly, because a borehole sees only
fields. Each porosity tool measures a *different* consequence of porosity:

| Log | Physical measurement | Why porosity changes it |
|---|---|---|
| Density | Attenuation of Compton-scattered gamma rays | Pore fluid is lighter than the matrix, so bulk density falls |
| Neutron | Moderation of fast neutrons to thermal energies | Hydrogen in the pore fluid does the moderating |
| Sonic | Travel time of an elastic wave | Pores lower the elastic moduli and the velocity |
| NMR | Relaxation of proton spins in the pore fluid | The fluid's protons relax, and the *amount* and *pore size* set the signal |

Each is an *apparent* porosity that equals the true one only under stated
assumptions. The four assumptions differ, so the four answers differ, and the
differences are the interpretation. A density–neutron crossover is not an error; it
is a hydrocarbon indicator. A sonic log reading high porosity where the density
reads low is a lithology statement. The skill is knowing which disagreement means
what.

## 2. Precise definitions

### 2.1 Density and electron-density index

The tool measures the electron density through Compton scattering and reports a
**bulk density** $\rho_b$ referred to a limestone calibration. The
**electron-density index** and the **photoelectric factor** come from the same
measurement's low-energy channels:

$$\rho_e = \frac{Z}{A}\rho_b, \qquad
P_e \propto \left(\frac{Z}{10}\right)^{3.6}. \tag{1}$$

$P_e$ separates quartz, calcite, dolomite, anhydrite and heavy minerals, which is
why the density log is usually run with a $P_e$ curve and why the pair
$(P_e, \rho_b)$ identifies mineralogy.

### 2.2 Neutron porosity and the hydrogen index

A neutron tool reports a **porosity**, but what it measures is the formation's
hydrogen content:

$$HI = \frac{\text{hydrogen atoms per unit volume in the material}}
{\text{hydrogen atoms per unit volume in fresh water}}. \tag{2}$$

Apparent neutron porosity $\phi_N$ is then approximately a hydrogen-index
measurement calibrated in a limestone–water reference.

### 2.3 Sonic slowness

The tool measures the transit time per unit length, $\Delta t$ in µs m⁻¹, of a
compressional wave along the wall. It is a *slowness*, and Section 3.4 shows why
that matters.

### 2.4 NMR porosity and T₂

Nuclear magnetic resonance measures the signal from hydrogen nuclei in the pore
fluid and its decay rate, characterised by the transverse relaxation time $T_2$.
Signal amplitude gives a **porosity**, and the $T_2$ distribution separates
**bound** from **movable** fluid.

## 3. Derivations

### 3.1 Density porosity, and its assumptions

Volume balance over a unit volume: $\phi$ of fluid and $1-\phi$ of matrix,

$$\rho_b = \phi\rho_f + (1-\phi)\rho_{\mathrm{ma}}
\quad\Longrightarrow\quad
\phi_D = \frac{\rho_{\mathrm{ma}} - \rho_b}{\rho_{\mathrm{ma}} - \rho_f}. \tag{3}$$

Three assumptions: a **known matrix density**, a **known fluid density**, and no
other phases. Section 4.1 quantifies the matrix error and shows it dominates.

### 3.2 The gas effect, derived

The demonstration's synthetic gas has $\rho_f = 150$ kg m⁻³ and $HI = 0.35$
against water's 1000 kg m⁻³ and 1.00. At a true porosity of 0.20 in quartz:

$$\phi_D = \frac{2650 - 2150}{2650 - 1000} = 0.303, \tag{4}$$

whereas the neutron log, read as if the fluid were water,

$$\phi_N = \frac{HI_{\text{measured}} - HI_{\mathrm{ma}}}{HI_f - HI_{\mathrm{ma}}}
= \frac{0.20(0.35)}{1.00 - (-0.02)} = 0.069\ \text{to}\ 0.073 . \tag{5}$$

The measured apparent crossover is $-0.230$ porosity units. **The two logs are
wrong in opposite directions, and their difference is the reliable signal.** This
is why density and neutron are always run together over prospective intervals.

### 3.3 Matrix identification from the crossplot

Plotting $\phi_D$ against $\phi_N$ places each mineral on a fixed point, and the
measured pair moves along a line between the mineral point and the fluid point.
The position along that line gives porosity and the direction identifies the
mineralogy. The demonstration measures the cost of getting the mineral wrong, for
a dolomite–oil layer at $\phi = 0.12$:

| Assumed matrix | $\rho_{\mathrm{ma}}$ (kg m⁻³) | $\phi_D$ | error |
|---|---|---|---|
| quartz | 2650 | 0.017 | $-85.7$ % |
| calcite | 2710 | 0.052 | $-56.9$ % |
| dolomite (correct) | 2870 | 0.133 | $+10.7$ % |

Even the *correct* matrix gives $+10.7$ per cent because the fluid was oil, not
water — a second, independent assumption error of the same size as the first.
**Two assumptions, two errors, and they are not separable from the log alone.**

### 3.4 Why a slowness integrates to a time

This is the property that makes the sonic log the well-tie log. Travel time is the
integral of slowness along a path:

$$t(z) = \int_0^z \frac{\mathrm{d}z'}{v(z')} = \int_0^z \Delta t(z')\,\mathrm{d}z'
\quad\Longrightarrow\quad
t_{2}(z) = 2\sum_i \Delta t_i\,\Delta z_i \tag{6}$$

for a vertical path. The demonstration verifies it numerically on the synthetic
well: integrating a 2 cm-sampled slowness log over 1000–1050 m gives a one-way time
of **0.013563 s**, i.e. **27.127 ms** two-way. The identity is exact, so the sonic
log *is* a time–depth curve sampled along the hole.

Its failure mode is equally exact: missing or washed-out intervals. Replacing 1 m
of quartz at 0.15 porosity (248 µs m⁻¹) by 1 m of quartz at 0.30 porosity
(313 µs m⁻¹) changes the two-way time by **0.066 ms**, which at typical velocities
is tens of metres of depth. A tie built on a log with a washed-out zone in it has
that error in it, and the error is invisible in the tie.

### 3.5 The sonic time-average relation, and its limits

Wyllie's relation is

$$\Delta t = \phi\,\Delta t_f + (1-\phi)\,\Delta t_{\mathrm{ma}}
\quad\Longrightarrow\quad
\phi_S = \frac{\Delta t - \Delta t_{\mathrm{ma}}}
{\Delta t_f - \Delta t_{\mathrm{ma}}}, \tag{7}$$

which is *identical in form* to equation (3) with slowness replacing density. That
formal identity is why both relations share the same assumptions and the same
failures: unconsolidated sands, gas, fractures and clay all violate them, and
Raymer–Hunt–Gardner or a rock-physics model is used instead
([05-04-04 Velocity-Porosity-Clay Models and Empirical Relations](../04-rock-physics/04-velocity-porosity-clay.md)).

### 3.6 NMR: the measurement that is closest to porosity

The amplitude of the NMR signal is proportional to the number of hydrogen nuclei in
the *fluid*, so — unlike the neutron log — the matrix contributes nothing and the
matrix-lithology assumption largely disappears. The limitations are different:

- **Very short $T_2$** in clay-bound water and heavy oil lies below the tool's
  minimum echo spacing and is invisible, so NMR *under-reads* clay-rich porosity.
- **Gas** has a low hydrogen index and a long $T_2$; polarisation and diffusion
  effects make it non-trivial.
- **The tool reads a sensitive volume** near the wall, so invasion and hole
  geometry matter exactly as in Section 3 of the previous lessons.

So NMR removes one large assumption and introduces three smaller ones. It is the
most *robust* porosity measurement in the common case, and it is not a reference
standard.

## 4. Worked examples

### 4.1 Forward model and inversion of a synthetic well

The demonstration's layer model (all SYNTHETIC) and its forward responses:

| Layer (m) | Matrix | Fluid | $\phi$ | $\rho_b$ (kg m⁻³) | $\phi_N$ | $\Delta t$ (µs m⁻¹) |
|---|---|---|---|---|---|---|
| 1000–1010 | quartz | water | 0.30 | 2155 | 0.286 | 313.4 |
| 1010–1020 | quartz | water | 0.15 | 2402 | 0.133 | 247.7 |
| 1020–1030 | calcite | water | 0.10 | 2539 | 0.100 | 202.4 |
| 1030–1040 | quartz | gas | 0.20 | 2150 | 0.054 | 375.6 |
| 1040–1050 | dolomite | oil | 0.12 | 2622 | 0.132 | 217.0 |

Inverting each with a quartz-matrix, water-fluid assumption recovers the porosity
**exactly** in the four layers where that assumption is true, and can be checked
against the values above. This is the point of a forward-and-invert exercise: it
calibrates the machinery, not the rock. Every error in the rest of this lesson
comes from an assumption, never from the arithmetic.

### 4.2 The gas layer, in detail

Measured for the gas layer: $\phi_{\text{true}} = 0.20$, density-derived
$\phi_D = 0.303$, neutron-derived $\phi_N = 0.073$, crossover $-0.230$. The
*arithmetic mean* of the two, a common shortcut, gives 0.188 — within 6 per cent of
truth, which is why the shortcut survives — but it is a coincidence of this
contrast and this hydrogen index. The defensible procedure is to solve the
two-log system with the fluid properties as unknowns, which requires a third
measurement (NMR, or a pressure–volume–temperature model of the fluid).

### 4.3 Which answer to believe

| Situation | Preferred porosity | Why |
|---|---|---|
| Clean, water-bearing, known mineralogy | Any of the three | They agree; use the arithmetic mean and report the spread |
| Gas-bearing | NMR, or a two-log solve | Density and neutron are biased in opposite directions |
| Shaly | NMR, or density with a clay correction | Neutron and sonic both see clay-bound water |
| Unconsolidated | Density, or NMR | Wyllie fails; velocity is not matrix-controlled |
| Heavy oil or bitumen | Density | NMR $T_2$ is too short to see the fluid |
| Fractured | NMR *plus* an image log | The fracture porosity is a separate quantity |

The table is a decision aid, not a rule: in each row the reason given is the
assumption the preferred tool does *not* need.

## 5. Assumptions

1. **Known matrix density and mineralogy.** Dominant error source (§3.3).
2. **Known fluid density and hydrogen index.** The gas effect (§3.2).
3. **A two-phase (matrix + fluid) volume balance.** Pyrite, siderite, coal and
   heavy minerals break it.
4. **The tool's volume of investigation is representative.** A thin bed or an
   invaded zone is not.
5. **Wyllie's relation (or a stated alternative) for the sonic.** Fails in
   unconsolidated and gas-bearing rock.
6. **The borehole is in gauge and the mud is known.** All the corrections of
   [05-08-01 §2.4](./01-borehole-environment.md).
7. **NMR's $T_2$ window covers the fluid**, which it does not for clay-bound water
   and heavy oil.

## 6. Units and dimensional analysis

- $\rho_b$: kg m⁻³ (logs in g cm⁻³; 2650 kg m⁻³ = 2.65 g cm⁻³). Mixing the two is
  a factor of 1000 in the fluid term and produces absurd porosities.
- $\Delta t$: µs m⁻¹, sometimes µs ft⁻¹. **1 µs ft⁻¹ = 3.281 µs m⁻¹**; a
  conversion error here is a factor of 3.3 in the integrated time and therefore in
  the tie depth.
- Equation (6): µs m⁻¹ × m = µs ✓. Summing a log sampled in µs ft⁻¹ while
  integrating in metres is the single most common tie error.
- $HI$: dimensionless, referenced to fresh water = 1.
- $P_e$: barns per electron, dimensionless in the log's convention; the reference
  values are mineral properties, not universal constants.
- $\phi_D$, $\phi_N$, $\phi_S$: fractions; report as fractions or as porosity units
  and say which (0.15 = 15 p.u.).

## 7. Python demonstration

`code/porosity_demo.py` builds the layer model, forward-models three logs, inverts
them, and verifies the slowness-to-time identity.

```python
rho = phi * f["rho"] + (1.0 - phi) * m["rho"]          # density forward
phi_n = phi * f["hi"] + (1.0 - phi) * m["hi"]          # neutron forward
dt = phi * f["dt"] + (1.0 - phi) * m["dt"]             # sonic forward
phi_d = (rho - mq["rho"]) / (wf["rho"] - mq["rho"])    # density inverse
```

Measured output, abridged:

```
true porosity = 0.20, fluid = gas
density-derived porosity, water assumed = 0.303
neutron-derived porosity, water assumed = 0.073
apparent crossover = -0.230 porosity units
true hydrogen index of the fluid = 0.35 (water = 1.00)

true layer: dolomite with oil, phi = 0.12
  density porosity assuming quartz    (rho_ma =   2650):   0.017  (  -85.7 per cent)
  density porosity assuming calcite   (rho_ma =   2710):   0.052  (  -56.9 per cent)
  density porosity assuming dolomite  (rho_ma =   2870):   0.133  (  +10.7 per cent)

one-way time from the log   = 0.013563 s
two-way time from the log   = 0.027127 s
effect of substituting 1 m of quartz at 0.30 porosity (313 us/m)
for 1 m of quartz at 0.15 porosity (248 us/m): -0.066 ms two-way
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Water-bearing layers invert exactly | The machinery is verified; every later error is an assumption |
| Gas: $\phi_D = 0.303$ against $\phi_N = 0.073$, truth 0.20 | The two logs err in opposite directions; the crossover is the signal |
| A wrong matrix is $-86$ per cent and a wrong fluid is $+11$ per cent | Two assumptions, both large, neither separable from one log |
| The slowness integral is exact | A sonic log *is* a time–depth curve |
| A 1 m washed-out interval costs 0.066 ms | Tens of metres of tie error, invisible in the tie |

> **Breaking exercise.** Change the gas hydrogen index to 0.60 and re-run. Predict
> the new crossover before running, then check it. Then state at what hydrogen
> index the density and neutron porosities would agree, and why that must exist.

## 8. Exercises

[`exercises/04-porosity-logs-exercises.md`](./exercises/04-porosity-logs-exercises.md)
and
[`exercises/04-porosity-logs-solutions.md`](./exercises/04-porosity-logs-solutions.md).

### ★ Foundational

**★1.** State what each of the four tools physically measures and one assumption
each requires.

**★2.** Compute $\phi_D$ for $\rho_b = 2450$ kg m⁻³ with quartz matrix and (a)
water, (b) oil of 800 kg m⁻³.

**★3.** Convert $\Delta t = 100$ µs ft⁻¹ to µs m⁻¹ and compute the two-way time
over a 1000 m vertical interval at that constant slowness.

### ★★ Applied

**★★4.** Run `code/porosity_demo.py` and report the crossover for hydrogen
indices of 0.2, 0.35 and 0.6 at a true porosity of 0.20.

**★★5.** For a limestone layer with 8 per cent porosity containing water, compute
the density, neutron and sonic readings from the demonstration's parameters, then
invert them with a dolomite assumption and report the errors.

**★★6.** A sonic log has a 2 m washed-out interval where the tool read the mud's
slowness. Estimate the two-way time error, convert it to depth at 3000 m s⁻¹, and
state how you would detect it from the log alone.

### ★★★ Research-oriented

**★★★7.** Implement a two-log (density–neutron) solve for porosity and fluid
hydrogen index simultaneously, assuming a known matrix, and report the condition
number of the system as a function of the true fluid hydrogen index. Identify the
hydrogen index at which the inversion becomes ill-conditioned and explain why.

**★★★8.** Build a complete synthetic well from a rock-physics model (Gassmann
fluid substitution plus Wyllie or Raymer for velocity), forward-model all four logs
including a 1 m bed and an invaded zone, then run the full interpretation chain of
[05-08-07](./07-log-interpretation.md) and report where it fails and by how much.

## 9. Common mistakes

1. **Calling any of these a porosity measurement.** Each is an apparent porosity
   under a stated assumption.
2. **Assuming a matrix.** Identify it, from $P_e$, a crossplot, or core.
3. **Reading a gas zone with water properties** and reporting a porosity 50 per
   cent wrong in each direction.
4. **Using $\Delta t$ in µs ft⁻¹ in a metres integral.** A factor of 3.3.
5. **Treating the density–neutron crossover as an error** rather than as the
   signal.
6. **Trusting a sonic in an unconsolidated sand.** Wyllie fails; the velocity is
   not matrix-controlled.
7. **Trusting NMR for clay-bound water.** It is below the echo-spacing floor.

## 10. Real-world applications

- **Reservoir volumetrics.** Porosity is the first term in a hydrocarbon volume
  calculation, and its uncertainty propagates linearly.
- **Well ties.** The sonic log's integral is the tie, and a washed-out interval is
  a tie error of tens of metres (§3.4).
- **Geomechanics.** Sonic velocities give the elastic moduli used for the
  mechanical earth model
  ([02-04-04 Young's Modulus, Poisson's Ratio and the Elastic Constants](../../02-physics/04-elasticity-and-continuum-mechanics/04-elastic-moduli.md)).
- **Gas hydrate and unconventional reservoirs.** Where density–neutron separation
  is the primary identification tool.
- **Geothermal wells.** Porosity and matrix identification control the thermal
  conductivity estimate used in the heat-flow model.

## 11. Further reading

- **Ellis, D. V. & Singer, J. M. (2007). *Well Logging for Earth Scientists*
  (2nd ed.). Springer.** Chapters 9–15. Level: intermediate to advanced. Density,
  neutron, sonic and NMR tool physics and interpretation.
- **Schlumberger (1989). *Log Interpretation Principles/Applications*.** Level:
  intermediate. The classical description of the crossplot method and the gas
  effect.
- **Kenyon, W. E. (1997). Petrophysical principles of applications of NMR
  logging. *The Log Analyst*, 38(2), 21–43.** Level: advanced. The $T_2$ physics
  and its petrophysical limits.
- **Mavko, G., Mukerji, T. & Dvorkin, J. (2009). *The Rock Physics Handbook*
  (2nd ed.). Cambridge University Press.** Level: advanced. The rock-physics
  relations of §3.5 and the alternatives to Wyllie.
- **Wyllie, M. R. J., Gregory, A. R. & Gardner, L. W. (1956). Elastic wave
  velocities in heterogeneous and porous media. *Geophysics*, 21(1), 41–70.**
  Level: advanced. The origin of equation (7) and of its limitations.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-08-03 Resistivity, Induction and Laterolog Tools](./03-resistivity-logging.md)
  — the saturation that consumes this porosity.
- [05-08-05 Borehole Imaging, Dipmeter and Fracture Detection](./05-imaging-logs.md)
  — the fractured-porosity case of §4.3.
- [05-08-07 Log Interpretation, Petrophysics and Uncertainty](./07-log-interpretation.md)
  — the workflow and its Monte Carlo.
- [05-04-03 Gassmann Fluid Substitution and Saturation Effects](../04-rock-physics/03-gassmann-fluid-substitution.md)
  — the fluid-substitution route that a two-log solve approximates.
- [02-09-05 Neutron Interactions and Borehole Nuclear Measurements](../../02-physics/09-radiation-and-atomic-physics/05-neutron-interaction.md)
  — the neutron physics in full.

## Self-assessment checklist

- [ ] I can state what each tool measures and its principal assumption. (§1, §2)
- [ ] I can derive density porosity and propagate a matrix error. (§3.1, §3.3)
- [ ] I can derive the gas effect from the hydrogen index. (§3.2)
- [ ] I can explain and verify numerically why a slowness integrates to a time.
      (§3.4)
- [ ] I can forward-model and invert a synthetic well and say which errors are
      assumptions. (§4.1)
- [ ] I can choose the right porosity answer for a stated situation with a reason.
      (§4.3)
- [ ] I can convert between µs ft⁻¹ and µs m⁻¹ and say why it matters. (§6)
- [ ] I can run the demonstration and explain every printed number. (§7)
