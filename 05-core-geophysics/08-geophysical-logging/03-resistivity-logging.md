---
id: 05-08-03
title: "Resistivity, Induction and Laterolog Tools"
level: advanced
prereqs: ["05-08-01", "09-01-01", "09-06-03"]
tags: [resistivity, induction, laterolog, skin-depth, invasion-correction, archie]
---

# Resistivity, Induction and Laterolog Tools

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the physical measurement each family of borehole resistivity tools
   makes — induction of eddy currents, focused electrode current, or pad contact —
   and the borehole conditions each requires.
2. **Compute** the quasi-static skin depth and state where the "503 √(ρ/f)" rule is
   exact and where it fails.
3. **Explain** why an induction tool responds to a conductivity average and a
   focused laterolog to a resistivity average, and quantify the difference on an
   invaded profile.
4. **Combine** a shallow and a deep reading into an invasion correction, and state
   the conditions under which the correction succeeds and fails.
5. **Convert** a saturation from $R_t$ for a stated $R_w$, temperature and Archie
   parameter set, and carry the uncertainty of each.
6. **Choose** between induction, laterolog and micro-resistivity for a stated
   borehole condition, and justify the choice from the physics.

## Prerequisites

- [05-08-01 The Borehole Environment and Invasion Profiles](./01-borehole-environment.md)
  — the invaded zone, $R_{xo}$, $R_t$ and the weighting-function formalism.
- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md)
  — the conductivity scale and the temperature dependence.
- [09-06-03 Downhole EM Logging and Induction Tools](../../09-electrical-em-methods/06-borehole-electrical/03-downhole-em-logging.md)
  — the EM theory of a borehole induction measurement.

## 1. Intuition: a current that goes where you send it, or one that goes where it likes

Two radically different ways of measuring formation resistivity:

- **Electrode tools (laterolog, micro-resistivity).** Current is injected through
  electrodes in contact with the hole and *focused* by guard electrodes so that it
  flows radially into the formation. The tool measures the voltage needed for a
  known current, hence a resistance, hence — via a geometric factor that depends
  on the *tool geometry* — a resistivity. They need a **conductive borehole fluid**
  to couple current into the formation, and they respond to the formation in
  series, so they are naturally **resistivity-averaging**.
- **Induction tools.** A transmitter coil carries an alternating current and
  induces eddy currents in the formation; a receiver coil measures the secondary
  field. No contact with the formation is needed, so induction works in an
  oil-based-mud, air-filled or empty hole. The induced eddy currents are
  proportional to *conductivity*, so the tool is naturally **conductivity-averaging**.

That single contrast — series-resistivity versus parallel-conductivity — explains
most of the disagreements between the two families over invaded, thinly bedded or
anisotropic intervals, and it is why a modern "triple-combo" runs both.

## 2. Precise definitions

### 2.1 Formation resistivity and conductivity

$$R = \frac{1}{\sigma}, \qquad [R] = \Omega\,\mathrm{m},\quad
[\sigma] = \mathrm{S\,m^{-1}}. \tag{1}$$

Field logs use Ω m for resistivity and often **mS m⁻¹** (or the historical
mmho m⁻¹, numerically identical) for conductivity. A conductivity log is not a
"resistivity log in different units" when averaging is involved, for the reason in
Section 3.3.

### 2.2 Apparent resistivity

$$\rho_a = K \frac{\Delta V}{I}, \tag{2}$$

with $K$ the tool's geometric factor (m). $\rho_a$ equals the true formation
resistivity only for a homogeneous medium; in a layered or invaded formation it is
a weighted average whose weighting is the tool's response function.

### 2.3 Skin depth

For a quasi-static field in a conductive non-magnetic medium, the amplitude decays
by $e^{-1}$ over

$$\delta = \sqrt{\frac{2\rho}{\mu_0\omega}}
\quad\Longrightarrow\quad
\delta \approx 503\sqrt{\frac{\rho}{f}} \ \text{m}
\quad (\rho\ \text{in}\ \Omega\,\mathrm{m},\ f\ \text{in Hz}). \tag{3}$$

### 2.4 Invasion parameters

- $R_{xo}$: flushed-zone resistivity (from a micro-resistivity or shallow pad tool).
- $R_t$: virgin-zone resistivity (from a deep tool).
- $d_i$: diameter of invasion, obtained from the $R_{xo}/R_t$ pair and a response
  model, or from an image log.

## 3. Derivations

### 3.1 The skin-depth rule, verified

Equation (3) is exact for the quasi-static limit. The demonstration tabulates it
against the closed form:

| $\rho$ (Ω m) | $f$ (Hz) | exact $\delta$ (m) | $503\sqrt{\rho/f}$ (m) | ratio |
|---|---|---|---|---|
| 1 | 100 | 50.329 | 50.300 | 0.9994 |
| 1 | 1000 | 15.915 | 15.906 | 0.9994 |
| 1 | 10 000 | 5.033 | 5.030 | 0.9994 |
| 10 | 100 | 159.155 | 159.063 | 0.9994 |
| 10 | 1000 | 50.329 | 50.300 | 0.9994 |
| 10 | 10 000 | 15.915 | 15.906 | 0.9994 |
| 100 | 100 | 503.292 | 503.000 | 0.9994 |
| 100 | 1000 | 159.155 | 159.063 | 0.9994 |
| 100 | 10 000 | 50.329 | 50.300 | 0.9994 |

The rule reproduces the exact expression to 0.06 per cent over three decades in
both variables, and the residual is the rounding of the constant 503 for the stated
units, not physics. **Use the rule, and always state the units it assumes.** The
practical content: at 10 kHz in a 10 Ω m formation the skin depth is 15.9 m, so an
induction tool's sensitivity is mediated by a volume metres across; at 100 Hz in the
same formation it is 159 m, which is why deep-reading induction tools use low
frequencies.

### 3.2 Two averaging rules, and the size of the difference

For a tool whose radial weighting is $w(r)$ (the demonstration uses
$w \propto e^{-(r-r_w)/L} r$ with stated $L$), define

$$\rho_{\text{avg}} = \frac{\int \rho\,w}{\int w},
\qquad
\frac{1}{\sigma_{\text{avg}}} = \frac{1}{\int \sigma w / \int w}. \tag{4}$$

On the demonstration's invaded profile ($R_t = 17.01$ Ω m,
$R_{xo} = 0.80$ Ω m, $r_i = 0.30$ m, a contrast of 21.3:1):

| Weighting length | $\rho_{\text{avg}}$ (Ω m) | $1/\sigma_{\text{avg}}$ (Ω m) | ratio |
|---|---|---|---|
| 0.15 m (shallow) | 8.50 | 1.46 | 5.81 |
| 1.50 m (deep) | 16.59 | 11.15 | 1.49 |

The two rules differ by a factor of **5.8** at the shallow weighting length and
**1.5** at the deep one, for the same formation. Neither is "the resistivity of the
rock": both are tool- and geometry-dependent averages. **Any comparison between an
induction log and a laterolog log over a contrast interval is a comparison of two
different averages**, which is why disagreement there is expected and is not
necessarily an error.

### 3.3 The invasion correction, and when it works

With two readings and a stated geometric-factor model, the step-profile
inversion of
[05-08-01 §3.5](./01-borehole-environment.md) gives the measured results:

| Case | $R_t$ recovered | $S_w$ recovered |
|---|---|---|
| True smooth diffusion profile | 40.35 Ω m ($-98.0$ %) | 2.816 |
| Genuine step profile | 1722.04 Ω m ($-13.9$ %) | 0.431 (true 0.400) |

The correction works when its geometry is right and fails when it is not, and the
failure is silent — it returns a number either way. Two lessons: (i) the
correction is a model, so state it; (ii) the conditioning matters, because the
deep tool's geometric factor here is 0.019, so a 1 per cent error in a reading
becomes roughly 15 per cent in $R_t$.

### 3.4 Saturation, and the direction of the invasion bias

$$S_w = \left(\frac{a R_w}{\phi^m R_t}\right)^{1/n}. \tag{5}$$

Measured on the demonstration's profile with true $S_w = 0.350$:

| Reading | $\rho_a$ (Ω m) | $S_w$ from equation (5) | error |
|---|---|---|---|
| deep (1.50 m weighting) | 11.15 | 0.4323 | $+23.5$ % |
| very deep (4.00 m) | 13.32 | 0.3954 | $+13.0$ % |

The bias is one-signed because the filtrate here is more conductive than the
formation: every tool that still sees filtrate under-estimates $R_t$ and
over-estimates $S_w$. With a resistive filtrate (oil-base mud) the sign reverses.
**The sign is a property of the mud–formation contrast, not a universal rule**,
and it must be worked out for each well.

### 3.5 Temperature and salinity

The same $R_w$ is a different number at a different temperature. Over a 2 km
interval a 20 °C change moves brine resistivity appreciably, and that change is
comparable with the contrast the interpretation is trying to resolve. Report $R_w$
at a stated reference temperature with the conversion used, and prefer a measured
produced-water sample to a catalogue value
([09-01-05](../../09-electrical-em-methods/01-electrical-properties-of-earth/05-temperature-and-pressure-effects.md)).

## 4. Worked examples

### 4.1 Choosing the tool from the borehole

**Problem.** A well is to be logged in an oil-based mud, with a 0.20 m hole and a
target interval of 20 Ω m formation at 2.5 km, over a 5 Ω m shale above.

*Reasoning.*

- **Oil-based mud:** electrode tools cannot couple current to the formation, so an
  **induction** tool is mandatory. Choosing a laterolog here returns noise.
- **Hole size:** a 0.20 m hole is favourable, since a larger hole increases the
  borehole signal in every tool.
- **Conductivity range:** 20 Ω m is a moderate resistivity, well inside induction's
  range; very resistive formations (thousands of Ω m) are where induction
  measurements become difficult, because the *secondary* field is small.
- **Invasion:** run a shallow-reading pad micro-resistivity as well, if the mud
  permits, because the $R_{xo}/R_t$ pair is the only direct invasion evidence.

Report the choice with the reason: physics first, then logistics.

### 4.2 Reading a thin bed between two resistive units

A 0.4 m shale of 3 Ω m sits between two 100 Ω m sands. Neither a shallow nor a deep
tool reads 3 Ω m, because both average over a metre. The laterolog reads closer to
the *series* average (biased high) and the induction to the *conductivity* average
(biased low), for the same reason as §3.2. Reporting "the shale is 20 Ω m" from
either tool is a statement about the tool, not the rock; the honest report says
which tool, what its vertical resolution is, and that the bed is below it.

### 4.3 A saturation with its uncertainty

$R_t = 20 \pm 2$ Ω m, $\phi = 0.22 \pm 0.02$, $a = 1$, $m = 2 \pm 0.2$,
$n = 2 \pm 0.2$, $R_w = 0.12 \pm 0.02$ Ω m. Equation (5) gives
$S_w = (0.12/(0.0484\times20))^{1/2} = 0.352$; a first-order propagation gives
$\delta S_w \approx S_w\left[\tfrac12(|\delta R_w/R_w| + |m\,\delta\phi/\phi| +
|m\delta R_t/R_t| + |\delta n/n \ln S_w^n|)\right] \approx 0.05$, so
$S_w = 0.35 \pm 0.05$. The dominant term is $\phi$ through $m$, which is why the
porosity log is the one to worry about — the same conclusion the full Monte Carlo
reaches in [05-08-07](./07-log-interpretation.md).

## 5. Assumptions

1. **A homogeneous medium for $\rho_a$ to equal $R$.** Otherwise it is an average
   (Section 3.2).
2. **Quasi-static fields for the skin-depth rule.** At very high frequency, or in
   very resistive media, propagation dominates and $\delta$ is a poor guide.
3. **Radial symmetry and a step invasion profile** for the correction of §3.3.
4. **Known $R_w$ at a known temperature.** Otherwise the saturation has an
   undiagnosed scale error.
5. **Non-magnetic formation** ($\mu_r \approx 1$) for equation (3); a few per cent
   of magnetite changes it.
6. **The borehole fluid conductivity is known**, because the borehole contributes
   to the signal in every electrode tool.
7. **Archie's law applies**, with stated $a$, $m$, $n$. In shaly sands it does not,
   and the model error dwarfs the statistical one.

## 6. Units and dimensional analysis

- $R$: Ω m. $\sigma$: S m⁻¹. mmho m⁻¹ = mS m⁻¹, numerically identical: a factor
  of confusion in old logs, not a factor of 1000.
- Equation (2): $K$ in m, $\Delta V$ in V, $I$ in A, so $K\Delta V/I$ is Ω m ✓.
- Equation (3): $\rho/f$ has units Ω m/Hz = (kg m³ s⁻³ A⁻²)/(s⁻¹) = kg m³ s⁻² A⁻²,
  whose square root times $\sqrt{\mu_0}$ … it is cleaner to check numerically
  against the exact expression, which the demonstration does to 0.06 per cent.
- Equation (5): dimensionless, provided $\phi$ is a fraction and $R_w$, $R_t$ share
  units. A $R_w$ in Ω m and $R_t$ in Ω m is required; mixing in Ω cm is a factor of
  100 in $S_w$ squared.
- Temperature: state the reference and the conversion. A resistivity "at reservoir
  temperature" without the temperature is not a number.

## 7. Python demonstration

`code/resistivity_demo.py` computes the skin depth, both averaging rules and the
saturation bias. Predict the averaging comparison before running it.

```python
w = np.exp(-(r - r[0]) / length) * r
w /= np.sum(w)
rho_avg = np.sum(rho * w)
sig_avg = np.sum((1.0 / rho) * w)
print(rho_avg, 1.0 / sig_avg)
```

Measured output, abridged:

```
rho (ohm m)  f (Hz)   exact delta (m)   503*sqrt(rho/f)   ratio
      10.0    1000      50.329          50.300            0.9994

SYNTHETIC Rt = 17.01 ohm m, Rxo = 0.80 ohm m, r_i = 0.30 m
resistivity contrast = 21.3 : 1
shallow-reading (weight length 0.15 m): rho_avg =     8.50 ohm m, 1/sig_avg =     1.46 ohm m, ratio   5.81
deep-reading   (weight length 1.50 m): rho_avg =    16.59 ohm m, 1/sig_avg =    11.15 ohm m, ratio   1.49

true Sw = 0.3500
deep reading      : Rt_app =    11.15 ohm m -> Sw_app = 0.4323 (+23.5 per cent)
very deep reading : Rt_app =    13.32 ohm m -> Sw_app = 0.3954 (+13.0 per cent)
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| The 503 rule matches the exact $\delta$ to 0.06 per cent | Check the units and use the rule, but state them |
| $\delta = 50.3$ m at 1 kHz in 10 Ω m | An induction tool's volume is tens of metres across, not decimetres |
| The averaging rules differ by 5.8× (shallow) and 1.5× (deep) | Induction and laterolog disagreement is expected, not an error |
| Uncorrected $S_w$ is 24 per cent high | The bias is one-signed and set by the mud–formation contrast |
| A deeper reading halves the bias | The direction to spend money is a deeper-reading tool |

> **Breaking exercise.** Set $R_{xo} < R_t$ (a resistive filtrate, as with an
> oil-base mud) and re-run. Predict the sign of the $S_w$ bias before running, then
> verify it and state the rule that governs the sign.

## 8. Exercises

[`exercises/03-resistivity-logging-exercises.md`](./exercises/03-resistivity-logging-exercises.md)
and
[`exercises/03-resistivity-logging-solutions.md`](./exercises/03-resistivity-logging-solutions.md).

### ★ Foundational

**★1.** State the physical measurement and the borehole-fluid requirement of (a)
induction, (b) a focused laterolog, (c) a pad micro-resistivity tool.

**★2.** Compute the skin depth at 20 kHz for 1, 10 and 100 Ω m, and state which
matters for a deep-reading tool.

**★3.** Convert 250 mS m⁻¹ to Ω m, and state the two common units a conductivity
log may be plotted in.

### ★★ Applied

**★★4.** Run `code/resistivity_demo.py`. Report both averaging rules for the
shallow and deep weightings and compute the ratio between them. Explain why a
21:1 contrast produces only a 1.5 difference at the deep weighting.

**★★5.** For $R_t = 50$ Ω m, $R_{xo} = 5$ Ω m, $\phi = 0.20$, $a = 1$, $m = 2$,
$n = 2$, $R_w = 0.1$ Ω m, compute the true $S_w$ and the $S_w$ from a deep reading
that is 20 per cent low.

**★★6.** At what temperature would a 0.1 Ω m water become 0.08 Ω m, given the
roughly linear temperature coefficient of ionic mobility? State the coefficient you
assume and its source.

### ★★★ Research-oriented

**★★★7.** Implement a two-dimensional (radial) forward model of a laterolog in an
invaded bed, using a stated current-focusing geometry, and compute the apparent
resistivity as a function of invasion radius. Compare with the two-reading
inversion of §3.3 and report where the inversion fails.

**★★★8.** Design a logging programme for a well in an oil-based mud over a
thinly bedded, anisotropic reservoir. Specify tools, acquisition parameters
(frequencies, spacings), the processing chain, and the interpretation workflow,
and state which of the measurements limits the final saturation uncertainty.

## 9. Common mistakes

1. **Running an electrode tool in a non-conductive mud.** The measurement does not
   exist; the log is noise.
2. **Comparing an induction and a laterolog value as if they measured the same
   quantity.** Section 3.2 quantifies the difference.
3. **Averaging resistivities when the physics averages conductivities.** A factor
   of 5.8 in the demonstration.
4. **Using table $R_w$ instead of a measured one**, and without a temperature
   reference.
5. **Quoting $\rho_a$ as $R_t$.** State the tool, the weighting and the invasion
   model.
6. **Ignoring the borehole's own contribution** in a large or washed-out hole.
7. **Applying an invasion correction without stating the geometry model.** It
   always returns a number.

## 10. Real-world applications

- **Reservoir saturation.** The input to volumetrics; its uncertainty propagates
  directly into reserves.
- **Thin-bed and low-resistivity pay.** Where induction and laterolog disagree most,
  and where the averaging question is worth real money.
- **Geothermal and groundwater.** Conductivity logs map salinity and clay content;
  the same averaging caveats apply
  ([14-03-01 Petrophysics for Hydrology](../../14-hydrology-hydrogeophysics/03-petrophysics-hydrology/README.md)).
- **CO₂ storage and monitoring.** Resistivity is the primary wireline monitor of
  saturation change, and the invasion correction is re-derived for each mud system.
- **Time-lapse logging.** Repeat passes detect invasion, which is the calibration
  for the whole shallow/deep workflow.

## 11. Further reading

- **Ellis, D. V. & Singer, J. M. (2007). *Well Logging for Earth Scientists*
  (2nd ed.). Springer.** Chapters 5–8. Level: intermediate to advanced. Induction
  and electrode tool physics, geometric factors and invasion correction.
- **Serra, O. (1984). *Fundamentals of Well-Log Interpretation*, Vol. 1.
  Elsevier.** Level: intermediate. Standard tool descriptions and correction charts.
- **Anderson, B. I. (2001). Modeling and inversion methods for the interpretation
  of resistivity logging tool response. *Surveys in Geophysics*, 22, 101–176.**
  Level: advanced. The rigorous account of the response functions used informally
  in §3.2.
- **Archie, G. E. (1942). The electrical resistivity log as an aid in determining
  some reservoir characteristics. *Transactions AIME*, 146, 54–62.** Level:
  intermediate. The empirical law of equation (5), still the starting point.
- **Schön, J. H. (2015). *Physical Properties of Rocks* (2nd ed.). Elsevier.**
  Level: advanced. The rock-physics basis for the conductivity models and their
  temperature and pressure dependence.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-04-07 Electrical Properties, Archie's Law and Clay Effects](../04-rock-physics/07-electrical-properties-rock.md)
  — why Archie fails in shaly sand, and what to use instead.
- [05-08-04 Density, Neutron and Sonic Porosity Logs](./04-porosity-logs.md)
  — the porosity input to equation (5).
- [05-08-07 Log Interpretation, Petrophysics and Uncertainty](./07-log-interpretation.md)
  — the full workflow, with the Monte Carlo that ranks these error sources.
- [09-06-03 Downhole EM Logging and Induction Tools](../../09-electrical-em-methods/06-borehole-electrical/03-downhole-em-logging.md)
  — the EM theory behind the induction measurement.
- [09-01-05 Temperature, Pressure and Frequency Dependence](../../09-electrical-em-methods/01-electrical-properties-of-earth/05-temperature-and-pressure-effects.md)
  — the $R_w$ temperature conversion used in §3.5.

## Self-assessment checklist

- [ ] I can state the three tool families' physics and their borehole requirements.
      (§1)
- [ ] I can compute and check a skin depth and say what it means for tool design.
      (§3.1)
- [ ] I can compute both averaging rules and explain the difference. (§3.2)
- [ ] I can perform an invasion correction and state when it fails. (§3.3)
- [ ] I can compute $S_w$ and determine the sign of the invasion bias. (§3.4)
- [ ] I can report $R_w$ with a temperature reference and its source. (§3.5)
- [ ] I can choose the right tool from a borehole description. (§4.1)
- [ ] I can run the demonstration and explain every printed number. (§7)
