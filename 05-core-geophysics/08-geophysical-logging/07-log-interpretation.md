---
id: 05-08-07
title: "Log Interpretation, Petrophysics and Uncertainty"
level: graduate
prereqs: ["05-08-03", "05-08-04", "18-06-02"]
tags: [petrophysics, saturation, shale-volume, uncertainty, depth-matching, cement-bond, uncertainty-budget]
---

# Log Interpretation, Petrophysics and Uncertainty

## Learning objectives

By the end of this lesson you will be able to:

1. **Execute** the standard petrophysical workflow — shale volume, porosity,
   saturation — and state every constant it contains.
2. **Build** a Monte Carlo uncertainty budget for a saturation, rank its
   contributions, and identify which measurement to improve.
3. **Explain** the depth datum problem: why measured depth, true vertical depth and
   seismic two-way time are three different scales, and why logs from the same well
   can be misaligned.
4. **Verify** an interpretation on a synthetic well built from rock physics, and
   state which errors are measurement and which are assumptions.
5. **Describe** the coverage measurements — cement bond and fluid flow — and what
   each establishes.
6. **Write** a petrophysical result with a stated uncertainty, a stated model set
   and an explicit statement of what was not determined.

## Prerequisites

- [05-08-03 Resistivity, Induction and Laterolog Tools](./03-resistivity-logging.md)
  — the saturation relation and its inputs.
- [05-08-04 Density, Neutron and Sonic Porosity Logs](./04-porosity-logs.md)
  — the porosity inputs and the synthetic-well inversion.
- [18-06-02 Monte Carlo Propagation and Its Convergence](../../18-inverse-problems/06-uncertainty-quantification/02-monte-carlo-uq.md)
  — the propagation machinery used in Section 3.

## 1. Intuition: a petrophysical answer is a model with a variance

The workflow is a chain of empirical relations, each with constants chosen by the
analyst:

$$\text{log readings} \longrightarrow V_{\mathrm{sh}} \longrightarrow \phi
\longrightarrow S_w \longrightarrow \text{hydrocarbon volume}.$$

Every arrow is a model. Every constant — baselines, matrix density, fluid
properties, $a$, $m$, $n$, $R_w$ — is an analyst decision, frequently borrowed from
another well or a catalogue. The chain is therefore not a measurement; it is a
*calculation whose error budget is dominated by its inputs, not by its data*.

This lesson's demonstration makes that precise. A single depth in a synthetic well
gives $S_w = 0.477$ as a point estimate, but a Monte Carlo over the parameters —
each perturbed by a plausible amount — gives a 90 per cent interval of
$[0.307, 0.721]$ for $S_w$, i.e. a hydrocarbon saturation anywhere between 0.28 and
0.69. The log readings contribute almost none of that spread.

The second theme is **depth**. Every log is indexed in measured depth along the
hole; every seismic section is in two-way time; every map is in true vertical
depth. A petrophysical interpretation that does not state which scale it is on
cannot be compared with anything.

## 2. Precise definitions

### 2.1 The standard workflow

1. **Data preparation.** Depth match, splice runs, apply environmental corrections
   of [05-08-01 §2.4](./01-borehole-environment.md), and quality-control the
   caliper and the tension.
2. **Shale volume.** From the gamma-ray index with a stated relation, or from a
   density–neutron separation in shaly intervals.
3. **Porosity.** From density, neutron, sonic, NMR, or a combination, with the
   matrix and fluid identified from $P_e$, a crossplot, or core.
4. **Saturation.** Archie in clean formations; a shaly-sand model where clay
   conduction matters (see
   [05-04-07 Electrical Properties, Archie's Law and Clay Effects](../04-rock-physics/07-electrical-properties-rock.md)).
5. **Summation.** Net-to-gross, net pay, and the volumetric product — with the
   uncertainty carried through, not dropped at the end.

### 2.2 Depth scales

| Scale | Definition | Source |
|---|---|---|
| Measured depth (MD) | Distance along the borehole | Drill pipe, wireline depth counter |
| True vertical depth (TVD) | Vertical projection of MD | Deviation survey |
| Two-way time (TWT) | Seismic travel time | Check shot, VSP, sonic integral |

Conversion MD → TVD uses the deviation survey; TVD → TWT uses the velocity model.
Both conversions have their own errors, and both are systematic.

### 2.3 Depth matching

**Depth matching** is the alignment of two logs of the same well, usually by
cross-correlating a common feature (typically the gamma-ray log run in both
passes). It is needed because:

- different runs have different depth-measurement systems (wireline tension,
  cable stretch, tool length);
- a tool may be run in a different hole condition;
- logging-while-drilling depth is measured by drill-pipe length, which differs
  systematically from wireline depth.

The residual misalignment after matching is the *depth-matching uncertainty*, and
it is usually of order decimetres — comparable with the bed thicknesses being
interpreted, which is exactly why it matters.

### 2.4 Coverage measurements

- **Cement bond log (CBL/VDL).** An acoustic measurement of the amplitude of the
  casing signal and of the waveform, used to assess whether cement is bonded to
  casing and to formation. It is *qualitative* in the sense that a good bond is
  unambiguous but a poor reading can arise from micro-annulus, fast formation, or
  gas-cut cement as well as from absent cement.
- **Production/flow logging.** Spinner, temperature, pressure, density and
  capacitance measurements, run to determine which intervals flow and how much.
  It measures *movement*, not rock.
- **Noise and tracer logs.** Further flow diagnostics.

The honest statement about coverage logging is that it establishes a *borehole-scale*
fact (bond over this interval; inflow at this depth) and that these facts are the
strongest available constraints on completions and on connectivity — but they are
still measurements in a single well.

## 3. Derivations

### 3.1 The workflow computed, with every constant named

At one depth, with SYNTHETIC readings GR = 62 API, baselines 22 and 110 API,
$\rho_b = 2320$ kg m⁻³, $R_t = 18$ Ω m, and matrix and fluid densities 2650 and
1000 kg m⁻³:

$$I_{\mathrm{GR}} = \frac{62-22}{110-22} = 0.455, \qquad
V_{\mathrm{sh}} = 0.33\left(2^{2I_{\mathrm{GR}}}-1\right) = 0.290, \tag{1}$$

$$\phi = \frac{2650-2320}{2650-1000} = 0.200, \qquad
\phi_{\text{eff}} = \phi - 0.10\,V_{\mathrm{sh}} = 0.171, \tag{2}$$

$$S_w = \left(\frac{aR_w}{\phi_{\text{eff}}^m R_t}\right)^{1/n}
= \left(\frac{1\times0.12}{0.171^2\times18}\right)^{1/2} = 0.477 . \tag{3}$$

The constants `0.33`, the `0.10` shale-porosity factor, `1`, `2`, `2`, `0.12`, and
the baselines are all *choices*. Equations (1)–(3) are the entire calculation, and
each constant is a place where the answer can move.

### 3.2 A Monte Carlo budget

Perturb each constant by a stated amount and sample:

| Input | 1σ perturbation | $\Delta S_w$ (one at a time) |
|---|---|---|
| $m$ | $\pm10$ % | $+0.169$ |
| $\rho_{\mathrm{ma}}$ | $\pm40$ kg m⁻³ | $-0.110$ |
| $R_w$ | $\pm20$ % | $+0.096$ |
| $n$ | $\pm10$ % | $+0.071$ |
| $a$ | $\pm10$ % | $+0.048$ |

Sampling all of them simultaneously, 200 000 draws:

$$\text{percentiles}_{5,25,50,75,95}(S_w) = 0.307,\ 0.399,\ 0.474,\ 0.562,\ 0.721,
\tag{4}$$

with a 90 per cent interval width of 0.414 and a hydrocarbon saturation range of
0.279 to 0.693.

**Three conclusions, in order of importance:**

1. **The dominant term is $m$, the cementation exponent**, then the matrix density.
   Neither is a log reading. Buying a better density log would not narrow the
   answer; measuring the mineralogy and constraining $m$ from core would.
2. **The point estimate sits where both the low and the high tails are large** — the
   distribution is asymmetric, so a symmetric "±" is the wrong summary. Quote
   percentiles.
3. **This is model uncertainty for the assumed relations.** It says nothing about
   whether Archie's law applies to this rock. That is structural uncertainty and it
   is larger (Section 4.3).

### 3.3 Depth matching, quantified

Two logs of the same well, matched by cross-correlation of their gamma-ray traces,
typically align to a fraction of a metre. Take the residual misalignment as 0.2 m
and consider what it does to:

- a **3 m bed**: a 7 per cent error in its thickness, hence in the net-to-gross;
- a **1 m bed**: 20 per cent;
- a **stress orientation** from a breakout: a shift of 0.2 m is usually harmless
  unless the breakout is short;
- a **seismic tie**: 0.2 m at 3000 m s⁻¹ is 0.13 ms two-way, negligible compared
  with the velocity error of §3.4 of the previous lesson.

So depth matching matters in proportion to how thin the features are — which is
exactly the regime where the interpretation is most valuable.

### 3.4 Verification on a synthetic well

The safest way to build confidence in an interpretation chain is to run it on data
whose answer you know. The demonstration of
[05-08-04 §4.1](./04-porosity-logs.md) provides a layer model with known
mineralogy, porosity and fluid, and the chain of §3.1 recovers the porosity
*exactly* wherever every assumption happens to match, and fails exactly where one
does not:

- water-bearing quartz layers: recovery exact;
- the gas layer: density porosity 0.303 and neutron 0.073 against a true 0.20;
- the dolomite–oil layer: $-86$ per cent with a quartz assumption, $+11$ per cent
  with the correct matrix but a water assumption.

**A synthetic-well test is therefore a test of the *assumptions*, not of the
data.** Any chain that passes it has correct arithmetic and can still be wrong on
real rock.

## 4. Worked examples

### 4.1 Reporting a saturation

> "Net reservoir 1042–1068 m MD (TVD 1015–1040 m at 8° deviation). Mean effective
> porosity 0.171 ± 0.021 (1σ, from density with the matrix identified as quartz
> from $P_e$). Water saturation 0.474, 90 per cent interval [0.307, 0.721], from
> Archie with $a = 1$, $m = 2.0 \pm 0.2$, $n = 2.0 \pm 0.2$ and
> $R_w = 0.12 \pm 0.02$ Ω m at 65 °C. The dominant term in the uncertainty is $m$;
> a core $m$ would narrow the interval substantially. Archie's applicability to the
> shaly intervals (Vsh > 0.35) has not been tested and those intervals are
> excluded."

Every clause is either a number with a unit and an uncertainty, a stated model, or
a stated non-determination. This is the required form.

### 4.2 A cement bond that is not a cement bond

A CBL reads high amplitude (poor bond) over an interval with excellent cement, as
proved by a subsequent pressure test. The cause: a micro-annulus — a thin fluid
film between cement and casing produced by thermal contraction after setting. The
log is not wrong; the *inference* from amplitude to "no cement" is wrong, because
the measurement cannot distinguish a micro-annulus from absent cement. The
resolution requires a second measurement (a radial or segmented bond tool, or a
pressure test) — the transverse-sensitivity principle of
[05-07-03](../07-interpretation-and-integration/03-multi-method-integration.md),
applied to completions.

### 4.3 What the whole module cannot tell you

Four quantities that no logging programme determines, however complete:

1. **Permeability** at reservoir scale. Logs give proxies (NMR, Stoneley); the
   measurement is a flow test or a pressure transient.
2. **Connectivity** between wells. A single well cannot measure it.
3. **Saturation in the uninvaded, unswept rock** in the presence of unknown
   wettability. Archie's parameters are saturation-dependent in ways a log cannot
   resolve.
4. **Whether the model applies.** Every relation in Section 3.1 is empirical; the
   log cannot test its own model. Only core, a second method, or production data
   can.

## 5. Assumptions

1. **The depth scales are reconciled and stated.** §2.2, §3.3.
2. **Environmental corrections are applied and identified.**
3. **The matrix and fluid are identified**, not assumed.
4. **Each empirical relation applies to this rock**, with its constants stated.
5. **The logs are of the same well, the same intervals and the same conditions**, or
   the differences are accounted for.
6. **Uncertainties are independent** for the Monte Carlo of §3.2. Correlated inputs
   change the answer, usually by making it worse.
7. **The uncertainty reported is model uncertainty for the stated relations.** It is
   not a confidence interval on the Earth.

## 6. Units and dimensional analysis

- Every constant in §3.1 carries a unit or is dimensionless; write them down.
  $R_w$ in Ω m at a stated temperature; $\rho$ in kg m⁻³ or g cm⁻³ but consistently.
- Porosity as a fraction or as porosity units; a "porosity of 20" is ambiguous and
  a "porosity of 20 per cent" is not.
- $V_{\mathrm{sh}}$ is dimensionless and bounded $[0,1]$; a computed value outside
  that range is a statement that the baselines are wrong, not a number to clip
  silently.
- Depth: always label MD or TVD. A net-to-gross from an MD-thick interval in a
  deviated well is wrong by $\cos(\text{inclination})$.
- Uncertainty: dimensionless relative values or absolute in the quantity's unit;
  quote percentiles, and say which.
- A volumetric product is m³ (or acre-ft); a saturation is dimensionless. Mixing
  them in a spreadsheet is a common and expensive error.

## 7. Python demonstration

`code/petrophysics_demo.py` runs the workflow, the Monte Carlo and the ranked
budget.

```python
sw_s = np.clip((a_s * rw_s / (phi_eff_s ** m_s * rt)) ** (1.0 / n_s), 0.0, 1.0)
q = np.percentile(sw_s, [5, 25, 50, 75, 95])
```

Measured output, abridged:

```
I_GR = 0.455 -> Vsh = 0.290
total density porosity = 0.200; shale-corrected effective porosity = 0.171
Archie Sw = 0.477  (so hydrocarbon saturation = 0.523)

samples = 200000
Sw percentiles 5/25/50/75/95 = 0.307 / 0.399 / 0.474 / 0.562 / 0.721
90 per cent interval width  = 0.414
hydrocarbon saturation range at 90 per cent = 0.279 to 0.693

ranked contribution to the variance of Sw (one-at-a-time, others fixed):
  m  (+/-10 per cent)        delta Sw = +0.169
  rho_ma (+/-40 kg/m^3)      delta Sw = -0.110
  Rw (+/-20 per cent)        delta Sw = +0.096
  n  (+/-10 per cent)        delta Sw = +0.071
  a  (+/-10 per cent)        delta Sw = +0.048
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| $S_w = 0.477$ as a point estimate | The number a report usually contains |
| 90 per cent interval $[0.307, 0.721]$ | The number it must contain instead |
| $m$ is the largest single contributor | Measure the mineralogy and $m$ from core, not the log |
| The distribution is asymmetric | Quote percentiles, not "±" |
| The Monte Carlo assumes the relations | Structural uncertainty is outside it, and larger |

> **Breaking exercise.** Set the $m$ perturbation to zero and re-run. Predict the
> new 90 per cent interval width from the one-at-a-time entries, then check whether
> simple quadrature overestimates or underestimates it, and explain why.

## 8. Exercises

[`exercises/07-log-interpretation-exercises.md`](./exercises/07-log-interpretation-exercises.md)
and
[`exercises/07-log-interpretation-solutions.md`](./exercises/07-log-interpretation-solutions.md).

### ★ Foundational

**★1.** List the five stages of the standard workflow and name one constant each
contains.

**★2.** Convert an MD of 2500 m at 25° deviation to TVD.

**★3.** State the difference between a cement bond log and a flow log, and what
each establishes.

### ★★ Applied

**★★4.** Run `code/petrophysics_demo.py` and recompute $S_w$ with $m = 1.8$ and
$R_w = 0.15$ Ω m. Report the new point estimate and the interval.

**★★5.** Two logs are depth-matched with a residual 0.35 m misfit. Compute the
fractional thickness error for beds of 0.5, 1, 3 and 10 m and state which
interpretation is affected.

**★★6.** For a net-to-gross of $0.42 \pm 0.06$, mean porosity $0.171 \pm 0.021$ and
hydrocarbon saturation $0.523 \pm 0.207$ (the 90 per cent half-interval from §3.2,
treated as 1σ for the exercise), compute the volumetric uncertainty by first-order
propagation and state the dominant term.

### ★★★ Research-oriented

**★★★7.** Build a complete synthetic well from rock physics (Gassmann plus a
velocity-porosity model), forward-model all logs, and run the whole workflow
including depth matching and environmental corrections. Report the error in $S_w$
that the workflow produces for layers where (a) all assumptions hold, (b) the
mineralogy is wrong, (c) the rock is shaly and Archie is used anyway. Rank the
three.

**★★★8.** Design a data-acquisition programme that would halve the saturation
uncertainty of §3.2. State what is measured, how it constrains the dominant term,
what it costs in principle, and what residual uncertainty remains. Then state the
observation that would prove your programme unnecessary.

## 9. Common mistakes

1. **Quoting a saturation with no uncertainty.** §3.2 shows the point estimate is
   one point in a factor-of-two interval.
2. **Assuming the matrix.** The dominant error in the demonstration.
3. **Using a catalogue $R_w$** without a temperature reference or a sample.
4. **Clipping $V_{\mathrm{sh}}$ outside $[0,1]$ silently** instead of revisiting the
   baselines.
5. **Mixing MD and TVD** in a net-to-gross or a volumetric.
6. **Treating a Monte Carlo as a validation.** It quantifies the relations you
   assumed; it cannot test them.
7. **Reporting a cement bond as "no cement"** without considering micro-annulus,
   fast formation or gas-cut cement.
8. **Dropping the uncertainty before the volumetric.** The error propagates into
   every number downstream.

## 10. Real-world applications

- **Reserves and volumetrics.** Every term carries an uncertainty; the discipline
  of Section 3 is what makes the final number defensible.
- **Reservoir simulation input.** Porosity, net-to-gross and saturation
  distributions with their uncertainty, not single values.
- **Completions.** Cement bond and flow logs decide perforation and isolation
  strategy; their limitations (micro-annulus) have direct safety and cost
  consequences.
- **Geothermal and hydrogeological wells.** The same workflow, with the addition of
  temperature and the temperature dependence of the fluids.
- **Regulatory and storage projects.** Where a stated uncertainty and a stated
  model set are requirements, not best practice.

## 11. Further reading

- **Ellis, D. V. & Singer, J. M. (2007). *Well Logging for Earth Scientists*
  (2nd ed.). Springer.** Chapters 1–4 and 18–19. Level: intermediate to advanced.
  The environment, corrections and the cement-bond and production measurements.
- **Serra, O. (1984, 1986). *Fundamentals of Well-Log Interpretation*, Vols 1–2.
  Elsevier.** Level: intermediate. The complete classical workflow.
- **Worthington, P. F. (1985). The evolution of shaly-sand concepts in reservoir
  evaluation. *The Log Analyst*, 26(1), 23–36.** Level: advanced. Why Archie fails
  and what the alternatives assume.
- **BIPM (2008). *Evaluation of Measurement Data — Guide to the Expression of
  Uncertainty in Measurement*.** Level: reference. The uncertainty vocabulary of
  §3.2, including why an asymmetric distribution should not be summarised by a
  symmetric interval.
- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Chapters 1–3. Level: graduate. Why a parameter estimate
  without its posterior is not an estimate.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-07-05 Reporting Geophysical Results with Honest Uncertainty](../07-interpretation-and-integration/05-reporting-results.md)
  — the reporting discipline this lesson applies to petrophysics.
- [05-08-06 Vertical Seismic Profiling and Check Shots](./06-seismic-while-drilling.md)
  — the time scale that the depth scales of §2.2 must reconcile with.
- [05-09-01 Measuring Terrestrial Heat Flow](../09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md)
  — the thermal application of the same workflow.
- [18-06-06 Decision-Making Under Uncertainty and Value of Information](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md)
  — what the interval is for.
- [05-04-03 Gassmann Fluid Substitution and Saturation Effects](../04-rock-physics/03-gassmann-fluid-substitution.md)
  — the rock physics behind the fluid terms.

## Self-assessment checklist

- [ ] I can execute the five-stage workflow and name every constant in it. (§2.1,
      §3.1)
- [ ] I can build and read a Monte Carlo budget and rank the terms. (§3.2)
- [ ] I can explain the three depth scales and quantify a depth-matching error.
      (§2.2–2.3, §3.3)
- [ ] I can verify a workflow on a synthetic well and say what that verifies.
      (§3.4)
- [ ] I can describe a cement bond and a flow measurement and their limits. (§2.4,
      §4.2)
- [ ] I can write a petrophysical result with units, uncertainties, models and
      non-determinations. (§4.1)
- [ ] I can name four quantities the module cannot determine. (§4.3)
- [ ] I can run the demonstration and explain every printed number. (§7)
