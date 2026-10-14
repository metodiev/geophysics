---
id: 10-06-03
title: "Monitoring Contaminant Transport with Geophysics"
level: doctoral
prereqs: ["05-02-03", "10-05-05", "10-06-01", "14-04-01"]
tags: [near-surface, monitoring, contaminant-transport, advection-dispersion, ert]
---

# Monitoring Contaminant Transport with Geophysics

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the one-dimensional advection-dispersion solution for a step and for
   a finite release, and **verify** the analytic solution against a numerical
   scheme.
2. **Compute** the arrival time and the passage duration of a plume at a monitoring
   point from the Darcy flux, the effective porosity and the dispersivity.
3. **Show** that the conductivity of a plume is a mixture of the plume, the
   background and the calibration, and **quantify** which error dominates for a
   strong and for a weak plume.
4. **Compute** the survey interval beyond which the plume peak is systematically
   missed, and **state** why that error is a bias rather than a noise.
5. **Compute** the detection probability (power) of a single survey for a stated
   plume strength and measurement noise.
6. **State** what a geophysical monitoring programme can and cannot deliver for a
   contaminated site, and **name** the measurements that supply the rest.

## Prerequisites

- [05-02-03 Noise and Drift](../../05-core-geophysics/02-geophysical-fields-and-observables/03-noise-and-drift.md) —
  random versus systematic error.
- [10-05-05 Integrating Near-Surface Methods](../05-other-near-surface-methods/05-multi-method-nearsurface.md) —
  the petrophysical chain from a property to a state variable.
- [10-06-01 Time-Lapse Near-Surface Geophysics](01-time-lapse-nearsurface.md) —
  repeatability, thresholds and the ambiguity of change hypotheses.
- [14-04-01 Contaminant Plumes](../../14-hydrology-hydrogeophysics/04-contaminant-and-environmental/01-contaminant-plumes.md) —
  the hydrogeology of the target.

> All models and data in this module are **SYNTHETIC**. The velocities,
> dispersivities, concentrations, calibrations, noise levels and survey intervals
> below are chosen teaching values, not measurements, not calibrations and not
> site parameters.

## 1. Intuition: a designed change that moves

Monitoring a contaminant plume differs from monitoring an embankment in one
decisive way: **the change is expected, it is moving, and its physics is known.**
The relevant partial differential equation — advection and dispersion in
groundwater — is the same one used in every hydrogeology text, and its solution
gives the arrival time and the passage duration at a point. That means the
geophysical survey is not looking for an unknown anomaly; it is **sampling a
process**, and a survey design is a question about sampling theory: how often must
you look, and how small a change must you resolve, to reconstruct the passing
plume rather than a random subset of its history.

Three difficulties are worth stating before the derivation, because each is
quantitative and each is measured in the demonstration.

- **Conductivity is a mixture.** A conductivity map depends on the plume, the
  background and the calibration (and on the pore-water chemistry through
  $\sigma_w$). Only a change is measured robustly; the concentration requires
  assumptions that geophysics cannot test.
- **Aliasing is a bias, not a noise.** Sampling more slowly than the passage
  averages the plume down. The result is not scattered around the truth; it is
  systematically smaller, and it looks perfectly smooth and plausible.
- **Detectability is a power calculation.** At the detection threshold the false
  negative rate is 50% by construction, so any claim of "no plume" must be
  accompanied by the smallest plume that the survey could have seen.

## 2. Precise definitions

**Darcy flux and pore velocity.** The Darcy flux $q$ (m/day) is the volumetric
flow per unit area of aquifer. The **pore-water velocity** is
$v = q/n_e$, with $n_e$ the effective (connected) porosity. Advective transport
is transported at $v$, not at $q$ — a factor of two to five in an unconsolidated
aquifer, and the commonest factor-of-several error in plume prediction.

**Longitudinal dispersivity and dispersion coefficient.** Mechanical spreading is
parameterised as $D = \alpha_L v$, with $\alpha_L$ the longitudinal dispersivity in
metres. In the field $\alpha_L$ grows with the scale of observation, which is why
it is the least predictable parameter in any transport prediction.

**Peclet number.** $\mathrm{Pe} = vL/D = L/\alpha_L$ compares advection to
dispersion over a length $L$. For a release of duration $T$ the controlling
dimensionless group is $vT/\alpha_L$: advection dominates when the release is long
compared with the dispersivity, and diffusion dominates for a short release.

**Retardation.** A sorbing contaminant travels at $v/R$ with $R$ the retardation
factor; geophysics sees the conductivity change, which is affected by sorption
only through the water movement. **The geophysical image is of the water, not of
the contaminant.**

**Detection power.** The probability of rejecting the null hypothesis when the
effect is present, $1-\beta$. At the threshold that gives a 5% false-positive rate
the power is 50%; a survey that *could* see the plume in half the trials will
report "no change" in the other half.

## 3. Derivations and measurements

### 3.1 Advection-dispersion and its analytic solutions

For one-dimensional transport with a constant velocity and dispersion coefficient,

$$\frac{\partial C}{\partial t} = D\frac{\partial^2 C}{\partial x^2}
- v\frac{\partial C}{\partial x},$$

with $D = \alpha_L v$. For a step input $C(0,t) = C_0$ on a semi-infinite domain
the solution is

$$C(x,t) = \frac{C_0}{2}\left[\mathrm{erfc}\!\left(\frac{x-vt}{2\sqrt{Dt}}\right)
+ e^{v x/D}\,\mathrm{erfc}\!\left(\frac{x+vt}{2\sqrt{Dt}}\right)\right],$$

and a release of finite duration $T$ is the difference of two step solutions,

$$C_{\text{slug}}(x,t) = C_{\text{step}}(x,t) - C_{\text{step}}(x,t-T),$$

which is the superposition principle applied to the same Green's function. The
demonstration verifies the step solution against an explicit finite-difference
solution of the partial differential equation on a $4001$-node grid over
$120\ \mathrm{m}$: the **maximum difference over $0$–$70\ \mathrm{m}$ is
$0.0001$** and the RMS difference $4\times10^{-5}$, at $t = 60$ days and with the
front at $60\ \mathrm{m}$. The comparison is restricted to $0$–$70\ \mathrm{m}$
because the outlet node is an artificial zero.

### 3.2 Arrival time and passage duration

The centre of a slug travels at the pore velocity, so it reaches the monitoring
point at

$$t_{\text{arr}} = \frac{x}{v} = \frac{x\,n_e}{q},$$

and the spreading grows as $\sqrt{D t}$, giving a passage whose duration is roughly

$$\Delta t_{\text{passage}} \approx T + \frac{2\sqrt{2Dt_{\text{arr}}}}{v}
= T + \frac{2\sqrt{2\alpha_L x/v}}{v}.$$

With the teaching values $q = 0.30\ \mathrm{m/day}$, $n_e = 0.30$ (so
$v = 1.00\ \mathrm{m/day}$), $\alpha_L = 0.50\ \mathrm{m}$ and
$x = 12\ \mathrm{m}$: $t_{\text{arr}} = 12.00$ days and the passage lasts about
$12.3$ days for a five-day release. The demonstration's measured peak is
$C = 0.5685$ at $t = 13.40$ days — later than $x/v$ because the release has finite
duration and dispersion skews the peak. **The design quantity is the passage
duration, not the arrival time**, because it is the duration that sets the
required survey interval.

### 3.3 Conductivity as a mixture

Write the measured conductivity as

$$\sigma = \sigma_{\text{bg}} + k\,C,$$

with $k$ the site calibration. Inverting for $C$ requires **both** $\sigma_{\text{bg}}$
and $k$, and the demonstration measures the consequence:

| true $C$ | rise (mS/m) | error from $k-27\%$ | error from $k+27\%$ | error from $\sigma_{\text{bg}}+3\ \mathrm{mS\,m^{-1}}$ |
|---|---|---|---|---|
| 0.85 | 127.50 | $+37.0\%$ | $-21.3\%$ | $-2.4\%$ |
| 0.13 | 19.50 | $+37.0\%$ | $-21.3\%$ | $-15.4\%$ |

Read the table as a statement about **which error dominates**: for a strong plume
the calibration error is the only one that matters, and for a weak plume a
background error of a few millisiemens per metre is nearly as damaging as a 27%
calibration error. This is not a statement about inversion quality but about
arithmetic: the concentration is a *difference divided by a scale*, so both terms
must be known to the accuracy demanded of the result.

### 3.4 Sampling-interval aliasing

Let the survey interval be $\Delta t$. The sampled peak is
$\max_j C(t_j)$ with $t_j = j\Delta t$, so the fraction of the true peak that is
seen depends only on the ratio of $\Delta t$ to the passage duration. Measured, for
the teaching plume:

| interval (days) | fraction of the true peak |
|---|---|
| 1.0 | $99.3\%$ |
| 2.0 | $98.5\%$ |
| 5.0 | $90.2\%$ |
| 10.0 | $54.2\%$ |
| 20.0 | $26.7\%$ |
| 30.0 | $0.5\%$ |

Two lessons follow. First, the *bias* is enormous well before the plume is missed
altogether: a 10-day interval halves the peak. Second, the under-estimate is
**systematic and plausible**: the sampled series is smooth and monotone, so no
statistical test applied to it will reveal that the peak was missed. The defence is
to state the sampling theorem in the design — the interval must be a fraction of the
passage duration — and to run one dense survey (a single day or a week) to
calibrate the passage duration of the site.

### 3.5 Detection power and the meaning of "no plume"

At a detection threshold set for a 5% false-positive rate, the power against a
plume of strength $s$ (in units of the noise) is

$$\text{power}(s) = 1 - \Phi(z_{0.95} - s),$$

so $\text{power}(2.0) = 0.50$: a plume whose conductivity rise equals twice the
noise is found half the time. The demonstration tabulates the power for the
teaching noise of $2\ \mathrm{mS\,m^{-1}}$:

| rise (mS/m) | detected at $2\sigma$? | power |
|---|---|---|
| 2.0 | no | $84.1\%$ |
| 4.0 | no | $50.0\%$ |
| 6.0 | yes | $15.9\%$ |
| 10.0 | yes | $0.13\%$ |
| 20.0 | yes | $\approx 0$ |

(the "power" column is the probability of *missing* the plume, so it is the
false-negative rate; it falls from $84\%$ to nearly zero as the plume strengthens).
The practical consequence: **a monitoring report must state the smallest plume it
could have detected**, otherwise "no change" is indistinguishable from "the survey
was too coarse".

## 4. Physical interpretation

**Geophysics sees the plume's electrical shadow, not the contaminant.** A
conductivity change follows the *water* and its dissolved ions. A plume of a
non-conductive contaminant (a light hydrocarbon, for example) may show little or
no conductivity change, while a plume of brine lights up strongly. The method's
sensitivity is therefore to the ionic content, and the petrophysical relation for
that is site-specific
([10-05-05](../05-other-near-surface-methods/05-multi-method-nearsurface.md)).

**The most defensible deliverable is a change map with an error bar.** Absolute
concentrations require a calibration that must be established by sampling;
relative changes between epochs cancel the background and much of the calibration
error, and they are what a monitoring programme is really for.

**Transport prediction and monitoring design are the same calculation.** Arrival
time and passage duration come from $q$, $n_e$ and $\alpha_L$; the required
interval comes from the passage duration; the required sensitivity comes from the
concentration that must be detected. Writing this chain down before the survey
converts a monitoring programme from a series of measurements into a test with a
stated power.

**What the hydrogeologist must supply.** $n_e$, $\alpha_L$, $R$ and the source
history. None of them is a geophysical measurement, and each one enters
multiplicatively: a factor-of-two error in $n_e$ is a factor-of-two error in the
arrival time, whatever the resolution of the survey.

**The companion measurements.** A water sample for the calibration $k$ and the
pore-water conductivity; a background station for $\sigma_{\text{bg}}$; and a
piezometer network for the head gradient that sets $q$. Geophysics is the part of
the monitoring programme that can see a *volume*, and it is not a substitute for a
sample at a point.

## 5. Worked examples

### Example 1 — Arrival time and passage duration

With $q = 0.30\ \mathrm{m/day}$, $n_e = 0.30$:

$$v = \frac{q}{n_e} = \frac{0.30}{0.30} = 1.00\ \mathrm{m/day}, \qquad
t_{\text{arr}} = \frac{12.0}{1.00} = 12.0\ \mathrm{days},$$
$$D = \alpha_L v = 0.50(1.00) = 0.50\ \mathrm{m^2/day}, \qquad
\Delta t_{\text{passage}} = 5.0 + \frac{2\sqrt{2(0.50)(12.0)}}{1.00}
= 5.0 + 6.9 = 11.9\ \mathrm{days},$$

against the measured peak time of $13.40$ days and passage of about $12.3$ days.
The design conclusion: an interval of $1$–$2$ days samples the passage adequately,
and $10$ days does not.

### Example 2 — The peak a 10-day survey reports

From the aliasing table, a 10-day interval sees $54.2\%$ of the peak. If the
calibration says the true peak rise is $127.5\ \mathrm{mS\,m^{-1}}$, the survey
reports $69.1\ \mathrm{mS\,m^{-1}}$ — a factor of $1.85$ under. Because the
under-estimate is systematic, the *shape* of the reported time series still looks
like a plausible plume passing; only the design information (the passage duration)
reveals the loss. Repeating the survey more often is the only fix, and the fix is
cheap compared with the cost of a wrong remediation decision.

### Example 3 — Which error dominates for a weak plume

Take a plume producing a rise of $19.5\ \mathrm{mS\,m^{-1}}$ (true $C = 0.13$,
$k = 0.15\ \mathrm{S\,m^{-1}}$ per unit). The measured errors are:

- calibration $27\%$ low: $C$ inferred $37.0\%$ high;
- calibration $27\%$ high: $C$ inferred $21.3\%$ low;
- background $3\ \mathrm{mS\,m^{-1}}$ high: $C$ inferred $15.4\%$ low.

Now the background error is comparable with the calibration error, because the
plume's rise ($19.5$) is no longer much larger than the background uncertainty
($3$). The practical rule: **the ratio of the plume's conductivity rise to the
background uncertainty decides whether a calibration campaign can be skipped** —
and for a weak plume it cannot.

### Example 4 — Power and the null result

A survey with $2\ \mathrm{mS\,m^{-1}}$ noise finds no change. Using the power table,
the survey could have detected a $4\ \mathrm{mS\,m^{-1}}$ rise only half the time
and a $2\ \mathrm{mS\,m^{-1}}$ rise $16\%$ of the time (that is, its
false-negative rate at 2 mS/m is $84\%$). Reporting "no plume" therefore means
"no plume with a conductivity rise above about $6\ \mathrm{mS\,m^{-1}}$", and the
number belongs in the report. Without it, the result is not a measurement.

## 6. Assumptions and regime of validity

1. **One-dimensional, homogeneous transport.** Real plumes are three-dimensional
   and heterogeneous; $\alpha_L$ fitted from a 1-D model absorbs the heterogeneity
   of the site, which is exactly why $\alpha_L$ is scale-dependent and why the
   passage duration is uncertain by a factor of two or more.
2. **A conservative (non-sorbing) tracer.** Sorption multiplies the travel time by
   $R$; geophysics sees the water, so a sorbing contaminant moves slower than the
   conductivity change suggests.
3. **A stable calibration $k$.** The relation between concentration and
   conductivity depends on the ionic composition of the contaminant, which changes
   as the plume ages and mixes. A calibration from the source zone does not
   necessarily apply at the front.
4. **A known background that does not drift.** Seasonal water-table and salinity
   changes move $\sigma_{\text{bg}}$; a background station is the only defence.
5. **Linear superposition of conductivities.** The relation between concentration
   and conductivity is linear only in dilute solutions; at high ionic strength the
   relation curves, and the inferred concentrations are biased low or high
   depending on which side of the curve the sample sits.
6. **A stationary water table during the survey.** A falling or rising water table
   changes the conductivity by changing saturation, which is indistinguishable from
   a concentration change without a head measurement.
7. **Sampling interval shorter than the passage.** Otherwise the peak is missed by
   construction, and the error does not appear in any statistical summary.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| Darcy flux | $q$ | $\mathrm{m\,day^{-1}}$ | volumetric flow per unit area |
| effective porosity | $n_e$ | dimensionless | $0<n_e<1$ |
| pore velocity | $v$ | $\mathrm{m\,day^{-1}}$ | $q/n_e$ |
| dispersivity | $\alpha_L$ | m | |
| dispersion coefficient | $D$ | $\mathrm{m^2\,day^{-1}}$ | $\alpha_L v$ |
| concentration | $C$ | $\mathrm{kg\,m^{-3}}$ or normalised | |
| calibration | $k$ | $\mathrm{S\,m^{-1}}$ per unit $C$ | |
| survey interval | $\Delta t$ | day | compare with the passage duration |

The check that catches the commonest error: the argument of every error function
must be dimensionless, so $x$, $v t$ and $\sqrt{Dt}$ must be in the same length
unit. Mixing metres with kilometres in $D$ while keeping days gives a
dimensionally consistent but numerically wrong plume — the same trap as the
$\mathrm{cm^2\,g^{-1}}$ versus $\mathrm{m^2\,kg^{-1}}$ trap in
[10-05-04](../05-other-near-surface-methods/04-nuclear-and-radiometric-nearsurface.md).

## 8. Python demonstration

`code/contaminant_monitoring_demo.py` implements the whole chain and prints
labelled results with units. It:

1. solves the advection-dispersion equation by finite differences on a 4001-node
   grid over 120 m and verifies the analytic step solution (maximum difference
   $0.0001$, RMS $4\times10^{-5}$ over 0–70 m);
2. computes the slug plume at a monitoring point ($12\ \mathrm{m}$ downstream) and
   reports the measured peak $C = 0.5685$ at $13.40$ days and a passage of about
   $12.3$ days for a five-day release;
3. quantifies the confounding of the calibration and the background for a strong
   and a weak plume;
4. measures the aliasing of the peak for survey intervals from 1 to 30 days
   ($99.3\%$ down to $0.5\%$);
5. tabulates the detection power (false-negative rate) against the plume's
   conductivity rise for a $2\ \mathrm{mS\,m^{-1}}$ noise level.

The demonstration is print-only, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network, and runs in about a second.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-contaminant-monitoring-exercises.md`](./exercises/03-contaminant-monitoring-exercises.md)
and
[`exercises/03-contaminant-monitoring-solutions.md`](./exercises/03-contaminant-monitoring-solutions.md).

- **★** Compute the pore velocity, arrival time and dispersion coefficient for
  $q = 0.15\ \mathrm{m/day}$, $n_e = 0.25$, $x = 20\ \mathrm{m}$,
  $\alpha_L = 1.0\ \mathrm{m}$.
- **★** From the aliasing table, state the interval that retains 90% of the peak
  and the interval that reduces it by half.
- **★★** A weak plume gives a $20\ \mathrm{mS\,m^{-1}}$ rise with a $2\ \mathrm{mS\,m^{-1}}$
  noise level. Compute the detection power and the smallest rise the survey could
  claim to have detected.
- **★★** Quantify the error in the inferred concentration for a $25\%$ calibration
  error and a $2\ \mathrm{mS\,m^{-1}}$ background error, for a plume rise of
  $20\ \mathrm{mS\,m^{-1}}$.
- **★★★** Design a monitoring programme for a plume expected to pass a compliance
  well over six months, stating the survey interval, the detection claim, the
  calibration measurements, and the falsification test.

## Mastery checkpoint
Complete this without notes:

> A plume is released for 10 days into an aquifer with $q = 0.20\ \mathrm{m/day}$,
> $n_e = 0.25$, $\alpha_L = 1.0\ \mathrm{m}$. A monitoring line lies $25\ \mathrm{m}$
> downstream and the conductivity noise is $2\ \mathrm{mS\,m^{-1}}$ with a
> calibration of $0.12\ \mathrm{S\,m^{-1}}$ per unit concentration.
> **(a)** Compute the pore velocity, the arrival time and the passage duration.
> **(b)** State the survey interval you would choose and why. **(c)** Compute the
> conductivity rise for a plume peak of $C = 0.5$ and the detection power against
> the noise. **(d)** State what additional measurements are needed before the
> result can be reported as a concentration. **(e)** Name two processes that would
> make the plume arrive later than your prediction.

A worked version of (a)–(c) appears in the exercise solutions.

## Common pitfalls
1. **Using the Darcy flux as the transport velocity.** The plume moves at
   $q/n_e$; using $q$ under-predicts the arrival time by the porosity factor.
2. **Designing the survey interval from the arrival time.** It is the *passage*
   duration that sets the interval.
3. **Reporting a concentration without a calibration and a background.** The
   conductivity is a mixture; two of its three terms are site properties.
4. **Treating an aliased peak as a small plume.** The under-estimate is systematic
   and invisible in the time series.
5. **Reporting "no plume" without a detection limit.** At the threshold the
   false-negative rate is 50%.
6. **Assuming the calibration transfers from the source zone to the front.** The
   ionic composition changes as the plume ages.
7. **Ignoring the water table.** Saturation and concentration both change the
   conductivity.
8. **Forgetting retardation.** Geophysics monitors the water; a sorbing
   contaminant lags behind it.

## Related modules
- [10-06-01 Time-Lapse Near-Surface Geophysics](01-time-lapse-nearsurface.md) —
  repeatability, environmental aliasing and detection thresholds.
- [10-06-02 Monitoring Dams, Embankments and Foundations](02-geotechnical-monitoring.md) —
  the same machines applied to a change that is *not* designed.
- [10-05-05 Integrating Near-Surface Methods](../05-other-near-surface-methods/05-multi-method-nearsurface.md) —
  the petrophysical chain from conductivity to water content and salinity.
- [14-04 Contaminant and Environmental Geophysics](../../14-hydrology-hydrogeophysics/04-contaminant-and-environmental/README.md) —
  landfills, saline intrusion and acid mine drainage.
- [14-05 Time-Lapse and Monitoring Hydrogeophysics](../../14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/README.md) —
  the hydrological side of the same programme.
