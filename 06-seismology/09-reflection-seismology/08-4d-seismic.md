---
id: 06-09-08
title: "Time-Lapse (4-D) Seismic and Reservoir Monitoring"
level: doctoral
prereqs: ["06-09-05", "06-09-07"]
tags: [seismology, reflection-seismology, 4d-seismic, monitoring, repeatability]
---

# Time-Lapse (4-D) Seismic and Reservoir Monitoring

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the 4-D signal as the difference between a baseline and a monitor
   survey, and explain why its *interpretation* requires a rock-physics link.
2. **Derive** the NRMS repeatability metric and explain what it measures and what
   it hides.
3. **Compute** the detection threshold of a 4-D change given the
   non-repeatable noise, including the $\sqrt{2}$ factor for independent errors.
4. **Use** the spatial localisation of a 4-D anomaly as a discriminator against
   noise.
5. **State** how a change in saturation or pressure maps to a seismic change via
   Gassmann's equation, and why the mapping is non-unique.
6. **Design** a 4-D feasibility study and state its assumptions.

## Prerequisites

- [05 AVO/AVA Analysis and Its Assumptions](05-amplitude-vs-offset.md) — fluid
  substitution and AVA.
- [07 Seismic Attributes and Quantitative Interpretation](07-seismic-attributes.md) —
  detection versus resolution.

## 1. Intuition: subtracting two images to see change

A 4-D survey is a controlled experiment: image the same subsurface twice, under
different production conditions, and subtract. What remains — the 4-D signal —
should be the change in the reservoir. Everything else is error.

The whole difficulty is that "everything else" is usually much larger than the
change. Seismic acquisition is never perfectly repeatable: source signatures
drift, receiver positions differ, the near-surface changes with weather, and the
noise is different every shot. The art of 4-D seismic is to make the
non-repeatable part of the difference small enough that the repeatable part —
production — is visible. That is an engineering problem with a measurable metric
(NRMS) and a physical detection threshold.

All numbers here are **SYNTHETIC**.

## 2. Precise definitions

### 2.1 The 4-D difference and NRMS

Let $b(t)$ be the baseline trace and $m(t)$ the monitor trace. The **NRMS**
(normalised root-mean-square) difference is

$$\text{NRMS} = \frac{\sqrt{\left\langle (m-b)^{2}\right\rangle}}
{\tfrac{1}{2}\left(\sqrt{\langle b^{2}\rangle}+\sqrt{\langle m^{2}\rangle}\right)}
\times 100\%,$$

where $\langle\cdot\rangle$ denotes a time average over a stated window. A lower
NRMS means better repeatability.

### 2.2 Detection threshold

If the non-repeatable noise in each survey has rms $\sigma$ and the two surveys'
noise is independent, the difference has rms $\sqrt{2}\,\sigma$. A 4-D anomaly is
**detected** when its amplitude exceeds a stated multiple (conventionally 3) of
that difference noise:

$$|m-b|_{\text{peak}} > 3\sqrt{2}\,\sigma.$$

### 2.3 4-D rock physics

A change in saturation or pressure alters $K_{\text{sat}}$ and $\rho$ (and hence
$v_p$, $v_s$) through Gassmann's equation
([05 §3.2](05-amplitude-vs-offset.md)), which in turn alters the impedance
contrast and the reflection amplitude.

## 3. Derivations

### 3.1 Why NRMS uses a symmetric denominator

The difference $m-b$ has zero mean and a magnitude that scales with the overall
amplitude level. Dividing by the *average* of the two traces' rms values makes
NRMS independent of the absolute amplitude scale, so it can be compared between
surveys, wells and vintages. Dividing by only one survey's rms would make the
metric asymmetric and biased when the two surveys have different gains.

### 3.2 The $\sqrt{2}$ factor

Let $b = s + n_b$ and $m = s' + n_m$, with $n_b,n_m$ independent zero-mean noise
of variance $\sigma^{2}$ and $s,s'$ the (different) signals. Then

$$m - b = (s'-s) + (n_m - n_b),$$
$$\operatorname{Var}(n_m-n_b) = \operatorname{Var}(n_m)+\operatorname{Var}(n_b)
= 2\sigma^{2}.$$

So the difference noise is $\sqrt{2}\sigma$. **This is why 4-D acquisition invests
in repeatability rather than in signal strength**: the noise enters the difference
amplified by $\sqrt{2}$, and the signal is the (usually small) difference of two
large numbers.

### 3.3 The 4-D signal and its detection, measured

The demonstration builds two SYNTHETIC zero-offset traces from a two-interface
model (cap / reservoir / basement) and changes the reservoir velocity by $+6\%$:

| | baseline | monitor |
|---|---|---|
| reservoir $v_p$ | $3000\ \mathrm{m\,s^{-1}}$ | $3180\ \mathrm{m\,s^{-1}}$ |
| $R$ at reservoir top | $+0.0386$ | $+0.0676$ |
| $R$ at reservoir base | $+0.1356$ | $+0.1069$ |
| NRMS (noiseless) | — | **51.74%** |

The NRMS of 51.74% is enormous because the 4-D signal is itself very large in
this deliberately exaggerated example — a $75\%$ relative change in the top
reflection coefficient. Real 4-D signals are typically a small fraction of this;
the demonstration's value is chosen to be visible.

Detection, measured inside the reservoir window (signal peak $0.06247$):

| noise rms | measured 4-D peak | threshold $3\sqrt{2}\sigma$ | detected |
|---|---|---|---|
| 0.000 | 0.06247 | 0.00000 | yes |
| 0.001 | 0.05903 | 0.00424 | yes |
| 0.003 | 0.05877 | 0.01273 | yes |
| 0.005 | 0.06176 | 0.02121 | yes |
| 0.010 | 0.07437 | 0.04243 | yes |
| 0.020 | 0.08015 | 0.08485 | **no** |
| 0.030 | 0.08266 | 0.12728 | **no** |
| 0.050 | 0.17864 | 0.21213 | **no** |

The transition happens between $\sigma = 0.010$ and $\sigma = 0.020$: the 4-D
signal is $0.062$ and the threshold reaches it once
$3\sqrt{2}\sigma \approx 0.062$, i.e. $\sigma \approx 0.0146$. **The feasibility
of a 4-D survey is therefore a calculation, not an opinion** — and it can be done
before any data are acquired.

### 3.4 Spatial localisation: the discriminator

Amplitude alone cannot always distinguish a 4-D anomaly from noise. Space can.
The demonstration (with $\sigma = 0.003$) measures the difference rms in two
windows:

| window | difference rms |
|---|---|
| inside the reservoir window | 0.02543 |
| outside the reservoir window | 0.00420 |
| ratio inside/outside | **5.94** |

A genuine 4-D change is **localised** at the reservoir: the ratio is far from 1.
Independent noise is spread evenly, so its ratio approaches 1. **The spatial
pattern, not the peak amplitude alone, is what makes a 4-D anomaly
interpretable**, and any 4-D study should report the anomaly's geometry.

### 3.5 Non-uniqueness of the 4-D inversion

A 4-D amplitude change can be caused by a saturation change, a pressure change, a
temperature change, or a combination, and the mapping from each to the seismic
response is porous-rock physics that is itself uncertain. The AVO degeneracy of
lesson 05 applies directly: a 4-D amplitude difference constrains a combination
of elastic changes, not a unique physical cause. The defensible 4-D statement is
usually "the difference is consistent with a $X$–$Y\%$ saturation change under
the assumed rock-physics model", with the model stated.

### 3.6 Repeatability metrics beyond NRMS

NRMS is necessary but not sufficient, and several complementary metrics are used
in practice:

- **Predictability**: how much of the monitor trace can be predicted from the
  baseline by a short matching filter. A high predictability with a *low* NRMS
  means the difference is mostly a stable time/phase shift, not random noise.
- **Time-shift** (from the matching filter): a systematic time shift between
  surveys can come from a velocity change in the overburden (real, and often
  interesting) or from acquisition differences (artefact). It must be diagnosed,
  not merely corrected.
- **Amplitude matching scalar**: a systematic gain difference indicates a source
  or receiver problem, not a reservoir change.

The distinction that matters is between the **4-D noise** (the random,
unpredictable part of the difference) and **systematic** differences (shifts,
gains), which are reproducible and can be modelled or removed. The demonstration
adds *independent random* noise, so it is measuring the best case; real data
usually have a systematic component that behaves differently and is often
larger.

### 3.7 The threshold is a decision, not a constant

Using $3\sigma$ as the detection threshold is a convention, not a law. It
corresponds to a low false-positive rate under a Gaussian assumption, and it
should be stated explicitly because the *interpretation* changes with it:

*Worked check.* With $\sigma = 0.02$ and an expected 4-D signal of $0.05$:

- $3\sqrt{2}\sigma = 0.0849$: not detected;
- $2\sqrt{2}\sigma = 0.0566$: not detected;
- $1\sqrt{2}\sigma = 0.0283$: detected, but at a confidence at which random noise
  alone would produce many false anomalies.

A study that reports "detected" without the threshold is unfalsifiable. **State
the threshold, the estimated noise, and the window.** With those three numbers,
a reviewer can repeat the calculation and reach the same conclusion — which is
the definition of a reproducible 4-D result.

## 4. Physical interpretation

- **4-D is a difference experiment**, so the noise of both surveys enters, and
  the signal is a small difference of large numbers.
- **Repeatability is the currency.** Every processing choice in 4-D is judged by
  whether it lowers NRMS without removing signal.
- **Detection is a threshold, resolution a limit, and localisation a
  discriminator.** All three matter; none alone suffices.
- **The rock physics is the interpreter.** The seismic measures an elastic
  change; converting it to saturation or pressure requires Gassmann plus an
  assumed model, with the attendant non-uniqueness.

## 5. Assumptions

1. **The two surveys image the same Earth except for the production change.**
   Any real change in acquisition geometry, overburden, or near-surface breaks
   this.
2. **Independent noise** for the $\sqrt{2}$ factor; correlated noise (e.g. a
   repeating source artefact) does not add in quadrature and is worse.
3. **The production change dominates the 4-D difference** in the window of
   interest.
4. **A rock-physics model** linking saturation/pressure to $(v_p,v_s,\rho)$, with
   its own uncertainty.
5. **Consistent processing.** Independent processing of the two surveys injects
   artificial differences.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| NRMS | % (or dimensionless) | ratio of rms values |
| $\sigma$ | amplitude | |
| threshold $3\sqrt{2}\sigma$ | amplitude | |
| 4-D signal | amplitude | |
| inside/outside ratio | dimensionless | |

NRMS is independent of absolute amplitude scale by construction; a "50% NRMS" means
the difference rms is half the average trace rms, whatever the units.

## 7. Worked examples

### Example 1 — NRMS of two noisy copies

Two surveys are nominally identical, each with signal rms 1.0 and independent
noise rms 0.1. Then the difference rms is $0.1\sqrt{2} = 0.1414$, and

$$\text{NRMS} = \frac{0.1414}{1.0}\times100\% = 14.1\%.$$

So an NRMS of ~14% corresponds to a per-survey noise of ~10% — a useful
rule-of-thumb conversion between the two numbers, valid when the noise is
independent and the signal is unchanged.

### Example 2 — the feasibility calculation

A proposed 4-D survey has an expected noise rms of $\sigma = 0.02$ of the trace
rms. The predicted 4-D signal from the reservoir model is 0.05 of the trace rms.
Threshold: $3\sqrt{2}(0.02) = 0.0849$. Since $0.05 < 0.0849$, the survey is
**infeasible as designed** — and this is known before acquiring anything. Options:
improve repeatability (lower $\sigma$), a stronger expected signal (a different
production scenario), or accept a lower confidence (use $2\sigma$: threshold
$0.0566$, still above 0.05).

### Example 3 — why localisation saves a marginal survey

In Example 2, with a $3\sigma$ threshold the peak fails. But if the difference
inside the reservoir window is 0.05 while outside it is 0.02, the inside/outside
ratio is 2.5 — spatially anomalous. Combined with a physical expectation of where
the change should be, that pattern can still be interpretable, whereas an equal
difference everywhere would not be. **Report the pattern, not just the peak.**

## 8. Python demonstration

`code/four_d_demo.py`:

1. builds baseline and monitor traces and reports the reflection-coefficient
   changes ($+0.0386\to+0.0676$ at the top, $+0.1356\to+0.1069$ at the base);
2. computes NRMS (51.74% for the noiseless 4-D signal in this exaggerated
   example);
3. adds independent noise and finds the detection transition between
   $\sigma=0.010$ (detected) and $\sigma=0.020$ (not detected) against the
   $3\sqrt{2}\sigma$ threshold;
4. measures the inside/outside difference-rms ratio (5.94) as the localisation
   discriminator, and states the NRMS normalisation caveat.

## 9. Exercises

Full sets are in
[`exercises/08-4d-seismic-exercises.md`](./exercises/08-4d-seismic-exercises.md)
and
[`exercises/08-4d-seismic-solutions.md`](./exercises/08-4d-seismic-solutions.md).

- **★** Compute NRMS for a difference rms of 0.05 and average trace rms of 0.40.
- **★★** Derive the $\sqrt{2}$ factor and state the assumption it needs.
- **★★** Given $\sigma = 0.015$ and an expected 4-D signal of 0.06, decide
  feasibility against a $3\sigma$ threshold.
- **★★★** Design a 4-D QC plan: list the metrics, the windows, and the decision
  each metric supports.

## 10. Common mistakes

1. **Reporting a 4-D anomaly without its noise floor.** An amplitude is not a
   detection.
2. **Using NRMS in a window where the signal is near zero.** The denominator
   vanishes and NRMS becomes meaningless; quote difference rms instead.
3. **Processing the two surveys independently.** Any inconsistent step becomes a
   fake 4-D signal.
4. **Attributing a 4-D anomaly to saturation alone.** Pressure, temperature and
   rock-physics uncertainty all contribute, and the mapping is non-unique.
5. **Ignoring the geometry of the anomaly.** Localisation is often the strongest
   discriminator against noise.

## 11. Real-world applications

- **Reservoir surveillance.** 4-D seismic detects unswept oil, gas-cap expansion
  and water-front movement, and is a standard tool for well placement.
- **CO$_2$ storage monitoring.** The 4-D signal tracks the plume; regulatory
  monitoring requires quantified detection limits, exactly the calculation of
  Section 3.3.
- **Geothermal and gas-storage reservoirs.** Pressure and saturation changes in
  the working fluid produce detectable 4-D signals when the rock physics is
  favourable.
- **Repeatability engineering.** Permanent reservoir monitoring (PRM) with buried
  cables exists specifically to lower $\sigma$, because the feasibility
  calculation rewards it directly.

## 12. Further reading

- **Lumley, D. E. (2001). Time-lapse seismic reservoir monitoring. *Geophysics*,
  66(1), 50–53.** Level: research. A concise overview of the method and its
  requirements.
- **Johnston, D. H. (2013). Practical applications of time-lapse seismic data.
  *SEG Distinguished Instructor Short Course*.** Level: intermediate to
  advanced. Practical 4-D work.
- **Mavko, G., Mukerji, T., & Dvorkin, J. (2009). *The Rock Physics Handbook*
  (2nd ed.). Cambridge University Press.** Level: advanced. The rock physics
  behind 4-D modelling.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related lessons

- [05 AVO/AVA Analysis and Its Assumptions](05-amplitude-vs-offset.md) — the
  fluid-substitution machinery.
- [07 Seismic Attributes and Quantitative Interpretation](07-seismic-attributes.md) —
  detection versus resolution.
- [09 Structural and Stratigraphic Interpretation](09-interpretation-reflection.md) —
  where the 4-D result is placed in a geological model.

## 14. Self-assessment checklist

- [ ] I can define NRMS and explain its symmetric denominator.
- [ ] I can derive the $\sqrt{2}$ factor for difference noise.
- [ ] I can compute a detection threshold and decide feasibility before acquisition.
- [ ] I can use inside/outside localisation as a discriminator.
- [ ] I can explain the non-uniqueness of the saturation/pressure attribution.
- [ ] I can list three processing requirements for a valid 4-D comparison.
