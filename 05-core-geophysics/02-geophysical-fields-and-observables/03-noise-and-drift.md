---
id: 05-02-03
title: "Noise, Drift, Tides and Instrument Bias in Field Data"
level: advanced
prereqs: ["05-02-02"]
tags: [noise, drift, tides, instrument-bias, qc]
---

# Noise, Drift, Tides and Instrument Bias in Field Data

## Learning objectives

1. **Separate** four distinct error sources — random readout noise, instrument
   drift, Earth tides, and bias — and explain how each is recognised in data.
2. **Apply** base-station repeat tying and state what it can and cannot remove.
3. **Quantify** a noise budget and decide how much of it a survey can tolerate.
4. **Explain** why a bias is undetectable by repetition within one survey.
5. **Design** a QC loop that would reveal each error source.

## Prerequisites

- [05-02-02 Units and Conventions](./02-field-measurement-units.md)

## 1. Intuition

A field reading is a difference between what the instrument now reads and what
it read at a reference station. Everything that changes between the two
moments — the instrument's own elastic creep, the Earth's body tide, the
operator's handling — is folded into that difference. Correction is possible
only because the unwanted signals have different *structure* from the target:
drift is slow and monotonic, tides are periodic and predictable, noise is
uncorrelated, and bias is constant.

## 2. Precise definitions

**Random noise (precision).** Short-period, uncorrelated scatter. Reduced by
averaging: $\sigma_\text{mean} = \sigma/\sqrt{N}$ for $N$ independent samples.

**Drift.** A slow, usually monotonic change in the instrument's zero, caused by
elastic creep in a spring, thermal expansion, or electronic offset. Removed by
re-occupying a base station and assuming linearity between occupations.

**Tide.** The time-variable component of the gravity field caused by the
relative motion of Sun, Moon and Earth (and the solid-Earth response). It is
*predictable* from an ephemeris and is a signal, not noise — it must be modelled
and removed.

**Bias (accuracy).** A constant offset or scale error. Repetition within the
survey cannot detect it, because every station shares it. Only an absolute
reference (a calibration range, an absolute gravimeter, a known station)
reveals it.

**Tie.** The operation of re-occupying a station, allowing drift to be
interpolated.

## 3. Derivation: what base-station tying removes

Model the reading at station $i$ at time $t_i$ as

$$r_i = g_i + \beta(t_i) + \tau(t_i) + \epsilon_i,$$

where $g_i$ is the true gravity, $\beta$ the drift, $\tau$ the tide and
$\epsilon_i$ the random noise. Repeat the base at times $t_a$ and $t_b$, with
true value $g_b$ known:

$$\beta(t_b) - \beta(t_a) = [r_b(t_b)-r_a(t_a)] - [\tau(t_b)-\tau(t_a)] -
(\epsilon_b-\epsilon_a).$$

Interpolating linearly gives $\hat\beta(t)$ for all $t$, and

$$\hat g_i = r_i - \hat\beta(t_i) - \tau(t_i) = g_i + (\beta-\hat\beta)(t_i) +
(\epsilon_i - \text{interpolated noise}).$$

The residual contains the *non-linearity* of the drift plus a noise contribution
that is $(1+\text{weight})$ times the individual noise. Units: everything in
mGal. Dimensional check is trivial here; the useful check is *magnitude* — is
$\beta-\hat\beta$ smaller than the target anomaly?

## 4. Units and magnitudes

| Source | Typical magnitude | Time signature | Removable? |
|---|---|---|---|
| Readout noise | 0.005–0.05 mGal (relative gravimeter) | white | by averaging |
| Drift | 0.01–0.1 mGal per hour, up to mGal/hour in bad conditions | monotonic | by tying (if linear) |
| Earth tide | up to ~0.2–0.3 mGal peak-to-peak | periodic, ~12.42 h and 24 h | by model |
| Bias (scale) | up to 0.1% of the reading | constant | only by calibration |
| Magnetic diurnal variation | tens of nT | periodic + irregular | by base/repeat or model |

These magnitudes are *ranges*, and they depend strongly on instrument,
latitude, and conditions; use them to plan, not to conclude. The demonstration
below uses stated synthetic values.

## 5. Assumptions

1. **Drift is linear between ties.** Poorly satisfied if the instrument is
   moved, warmed, or handled roughly.
2. **The tide model is correct to better than the target.** Modern models are,
   but the *ocean loading* term requires a local model.
3. **The base station is stable.** A monument that moves is a bias.
4. **Random noise is independent.** Correlated noise (e.g. microseism) averages
   less efficiently than $\sqrt{N}$.
5. **Repetition measures precision, not accuracy.** This is the assumption
   most often violated in practice.

## 6. Worked examples (measured)

Using the module demonstration with stated synthetic inputs (target 4 mGal
Gaussian, drift 0.05 mGal/h, tide amplitude 0.15 mGal, noise $\sigma = 0.02$
mGal, relief ±8 m, Bouguer density 2400 kg/m³):

- **Raw** readings depart from the target by 0.2324 mGal RMS, with a largest
  single error of 0.3623 mGal. The contamination exceeds the target.
- **After removing drift and the tide model** the RMS departure is 0.0212 mGal
  — but note this is *not* the noise floor, because the elevation effect is
  still present in both the data and the comparison.
- **After the free-air and Bouguer corrections** the residual is 0.0212 mGal
  against a stated $\sigma = 0.02$ mGal: the corrections removed exactly what
  the model put in.

The demonstration notes explicitly that it removed drift *exactly*, which is
optimistic; real residual drift of 0.01–0.05 mGal over a survey is routine.

## 7. Python demonstration

`code/noise_reduction_demo.py` builds the survey, applies each correction, and
prints the effect of each. Predict the raw RMS error before running. Then
modify the script to make the drift *non-linear* (add a quadratic term) and
observe how much residual survives base-station tying — that is the honest
measure of a tie's power.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/03-noise-and-drift-exercises.md`](./exercises/03-noise-and-drift-exercises.md).

**Common mistakes.** (1) Averaging $N$ samples and claiming $\sqrt{N}$ noise
reduction when the noise is correlated. (2) Forgetting the tide is a *signal* to
be modelled, not noise. (3) Confusing precision with accuracy. (4) Tying only at
the start and end of a long day. (5) Ignoring ocean-loading in coastal surveys.

**Applications.** Microgravity monitoring of volcanoes and aquifers needs
tidal and drift control at the 0.005 mGal level; magnetic base stations serve
the same role for diurnal variation; repeat surveys for 4-D need *accuracy*
reproducibility, which is a calibration problem.

## Extended worked example: reading a residual plot

The demonstration's synthetic survey provides a worked case in the order a field
geophysicist would actually reason.

**Step 1 — look at the raw spread.** The raw readings depart from the known
target by 0.2324 mGal RMS with a largest single error of 0.3623 mGal. Since the
target amplitude is 4.0 mGal, the contamination is about 6% of the signal — not
fatal for a large target, but fatal for a subtle one. **The first number to
compute is always this ratio**, because it decides whether the target is
reachable at all.

**Step 2 — ask which contaminant has which structure.** Over a 4-hour loop the
drift reaches $0.05\times4 = 0.20$ mGal — a slow trend across the whole survey.
The tide, with 0.15 mGal amplitude and a 12.42 h period, changes smoothly and
predictably within the loop. The readout noise, $\sigma = 0.02$ mGal, is
uncorrelated station to station. Three different signatures; three different
treatments.

**Step 3 — remove what you can model.** Subtracting the exact drift and the tide
model leaves 0.0212 mGal RMS, which is the elevation effect plus noise. The
residual is *not* yet the noise floor: the terrain terms are still in the data
*and* absent from the comparison, so they appear as residual. This is a subtle
and common misreading — checking a processing step against a model that omits
one of the terms in the data.

**Step 4 — apply the corrections, then re-check.** After the free-air and
Bouguer corrections the residual is still 0.0212 mGal, now equal to the stated
noise $\sigma = 0.02$ mGal. The peak recovered anomaly is 3.9995 mGal against a
true 4.0000 mGal — a 0.01% error, i.e. at the noise level. All three
corrections did exactly what the forward model required.

**Step 5 — ask what the residual would have told you if it had been larger.**
A residual larger than the noise has two possible causes: a real feature, or a
mis-specified correction. The demonstration shows the second explicitly: with
$\rho_B = 3000$ kg/m³ instead of 2400, the peak anomaly shifts by $+0.157$ mGal
— 3.9% of the target, well above the noise. **From the data alone you cannot
tell which cause is operative**; you must test the corrections independently
(e.g. a Nettleton density profile, or a repeat survey with a different
correction set).

**Step 6 — state what was assumed.** The demonstration removed drift *exactly*,
using the known drift function. Real ties estimate it, and residual drift of
0.01–0.05 mGal is routine. Reporting a synthetic residual of 0.0212 mGal without
that caveat would overstate the achievable precision by a factor of two or more.

## 9. Further reading

- **Telford, Geldart & Sheriff (1990).** Chapter 2. Level: intermediate.
- **Longman, I. M. (1959). Formulas for computing the tidal accelerations due
  to the Moon and the Sun.** *JGR* 64, 2351–2355. The classical tidal
  formulation.
- **Milsom & Eriksen, *Field Geophysics*.** Level: intermediate. Practical
  drift and tie procedure.

## 10. Related lessons

- [05-02-04 Reduction of Observations to Anomalies](./04-reduction-of-observations.md)
- [05-01-05 Choosing a Method](../01-what-geophysics-measures/05-choosing-a-method.md)
- [07-01-05 Gravity Units and Instruments](../../07-gravity-geodesy/01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md)

## Self-assessment checklist

- [ ] I can list the four error sources and their time signatures.
- [ ] I can derive what base-station tying removes and what it leaves.
- [ ] I can explain why repetition does not detect bias.
- [ ] I can state typical magnitudes as ranges, not values.
- [ ] I can design a QC loop for each source.
