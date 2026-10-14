---
id: 10-06-01
title: "Time-Lapse Near-Surface Geophysics"
level: doctoral
prereqs: ["05-02-03", "05-05-05", "10-05-05", "10-06-02"]
tags: [near-surface, time-lapse, monitoring, coda-interferometry, repeatability]
---

# Time-Lapse Near-Surface Geophysics

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** repeatability as an NRMS between independent baseline repeats, and
   **compute** it from a noise level.
2. **Derive** the resolution of a relative velocity change from a travel-time
   measurement, and **compute** the threshold for stated path lengths, velocities
   and picking errors.
3. **Derive** the stretching estimator of coda-wave interferometry from the
   least-squares misfit, and **state** its precision in terms of the noise and the
   coda's time-derivative energy.
4. **Quantify** the environmental aliasing between a target change and a
   temperature or moisture change, and **state** the two standard defences.
5. **Show**, with a computed rejection rate, that separating a distributed change
   from a localised one is governed by the *depth coverage* of the path set rather
   than by picking accuracy.
6. **State** the difference between a 4-D difference, a 4-D ratio and a 4-D
   inversion, and what each assumes about repeatability.

## Prerequisites

- [05-02-03 Noise and Drift](../../05-core-geophysics/02-geophysical-fields-and-observables/03-noise-and-drift.md) —
  random versus systematic error.
- [05-05-05 Quality Control](../../05-core-geophysics/05-survey-design-and-acquisition/05-quality-control.md) —
  repeatability as an acquisition design quantity.
- [10-05-05 Integrating Near-Surface Methods](../05-other-near-surface-methods/05-multi-method-nearsurface.md) —
  the sensitivity-vector reasoning this lesson applies to time rather than to
  method.
- [10-06-02 Monitoring Dams, Embankments and Foundations](02-geotechnical-monitoring.md) —
  the geotechnical application of what is derived here.

> All models and data in this module are **SYNTHETIC**. The velocities, path
> lengths, noise levels, environmental sensitivities, coda lengths and change
> magnitudes below are chosen teaching values, not measurements and not site
> parameters.

## 1. Intuition: the second measurement is the hard one

A static survey asks *what is there*. A monitoring survey asks *what changed*, and
the difficulty is that the answer is a small difference of two large numbers. The
signal of interest — a wetting front, a thaw, a piezometric change, an injected
fluid — produces changes of a few tenths of a per cent in the observables, while
the survey itself changes between epochs for reasons that have nothing to do with
the target: source and receiver coupling, water content in the very shallow soil,
temperature, and instrument drift.

Three quantities therefore have to be separated, and the whole practice of
time-lapse geophysics is about keeping them apart:

- the **repeatability** (how different are two measurements of the *same* state?),
- the **change** (how different are the two states?),
- the **environmental change** (how much of the difference is caused by
  temperature, moisture or coupling rather than by the target?).

A detection is claimed only when the change exceeds the repeatability in a way
that the third term cannot explain. This lesson derives each of the three, and
then shows with numbers that the last one is usually the one that decides.

## 2. Precise definitions

**Baseline and monitor.** The baseline is the first state, measured with enough
repeats to *measure* its own repeatability; the monitor is the later state,
measured with the same geometry.

**NRMS.** The normalised RMS difference between two traces (or two data sets),

$$\mathrm{NRMS}(a,b) = \frac{\sqrt{\mathrm{mean}\,[(a-b)^2]}}
{\sqrt{\mathrm{mean}\,[((a+b)/2)^2]}} \times 100\% .$$

It is dimension-free, insensitive to an overall scale, and is the standard
repeatability metric of the seismic industry.

**4-D difference and 4-D ratio.** The difference $\Delta d = d_2 - d_1$ is the
natural observable for a property that adds (arrival time); the ratio
$d_2/d_1$ is natural for a property that scales (amplitude, velocity). Neither is
an inversion: both compare the same bin of the same geometry, so both assume that
the geometry and the coupling are unchanged.

**4-D inversion.** An inversion in which the model is parameterised *twice* — a
baseline model and a change — with a coupling term (often a norm on the change)
and a shared structure. It is the honest way to handle the case where the baseline
is itself uncertain.

**Relative velocity change** $\delta v/v$. For a monitoring survey the target is
usually a *relative* change; the absolute velocity may be poorly known and does
not need to be.

**Coda-wave interferometry.** Using the *tail* of the record, where energy has
scattered many times, as a long yardstick: a spatially uniform velocity change
stretches the whole coda in time, and the stretch factor is the velocity change.
The estimator is described in Section 3.3.

## 3. Derivations

### 3.1 Repeatability as a function of the noise level

If two repeats differ only by independent noise of RMS $\sigma$ on a signal of RMS
$S$, then

$$a - b = \text{noise}_2 - \text{noise}_1, \qquad
\mathrm{mean}[(a-b)^2] = 2\sigma^2,$$

so

$$\mathrm{NRMS} = \frac{\sqrt{2}\,\sigma}{S}\times 100\%
\approx 1.41\,\frac{\sigma}{S}\times 100\%.$$

The demonstration measures exactly this: a 5% noise level gives NRMS $7.34\%$,
about $1.47$ times the noise, and a 10% noise level gives $14.04\%$. **NRMS is a
property of the acquisition, not of the target**, which is why two surveys can have
the same target and wildly different detection thresholds.

### 3.2 The resolution of a velocity change from a travel time

For a path with local velocity $v(l)$, the travel time is $t = \int \mathrm dl/v$,
so a velocity change $\delta v(l)$ produces

$$\delta t = -\int \frac{\delta v(l)}{v(l)^2}\,\mathrm dl .$$

For a *uniform* relative change $\delta v/v = \epsilon$ over the whole path,

$$\delta t = -\epsilon\, t \qquad\Longrightarrow\qquad
\epsilon = -\frac{\delta t}{t}.$$

The resolution of $\epsilon$ is therefore

$$\sigma_\epsilon = \frac{\sigma_t}{t},$$

a ratio of the picking error to the *total* travel time — so long paths in slow
media are the most sensitive. The demonstration tabulates it:

| path (m) | $v$ (m/s) | $t$ (ms) | $\sigma_\epsilon$ for $\sigma_t = 0.5\ \mathrm{ms}$ |
|---|---|---|---|
| 10 | 400 | 25.00 | 2.00% |
| 20 | 400 | 50.00 | 1.00% |
| 20 | 1500 | 13.33 | 3.75% |
| 50 | 1500 | 33.33 | 1.50% |

Two per cent on a 10 m path in a 400 m/s medium is the practical floor for a
picking-based survey. Everything that follows is about doing better than this
floor without better picks.

### 3.3 Coda-wave interferometry: estimator and precision

Let the baseline coda be $f(t)$ and the monitor coda be the same waveform
stretched by the factor $(1+\epsilon)^{-1}$ and contaminated by noise, so that the
model is $g(t) \approx f(t(1+\epsilon))$. The estimator of $\epsilon$ minimises

$$\chi^2(\epsilon) = \sum_i \left[f(t_i) - g\big(t_i(1+\epsilon)\big)\right]^2 .$$

Expanding $g(t(1+\epsilon)) \approx g(t) + \epsilon t\,g'(t)$ around
$\epsilon = 0$:

$$\chi^2(\epsilon) \approx \chi^2(0) - 2\epsilon \sum_i
(f-g)(t_i)\,t_i g'(t_i) + \epsilon^2 \sum_i \big[t_i g'(t_i)\big]^2,$$

so the minimiser is

$$\hat\epsilon = \frac{\sum_i (f-g)(t_i)\,t_i g'(t_i)}
{\sum_i \left[t_i g'(t_i)\right]^2},$$

and, with the residual dominated by independent noise of RMS $\sigma_n$,

$$\boxed{\;\sigma_\epsilon = \frac{\sigma_n}{\sqrt{\sum_i \left[t_i\,g'(t_i)\right]^2}}\;}.$$

The denominator is the **time-derivative energy of the coda weighted by time**, and
it is what makes the method powerful: a coda with a dominant frequency $\omega$ and
a duration $T$ has $\sum (t g')^2 \sim \omega^2 T^3$, so

$$\sigma_\epsilon \sim \frac{\sigma_n}{\omega\,T^{3/2}} .$$

**Longer and higher-frequency coda is exponentially better than longer picking
practice.** The demonstration measures both trends:

| noise | measured scatter | CRB prediction |
|---|---|---|
| 20% | $0.057\times10^{-4}$ | $0.037\times10^{-4}$ |
| 50% | $0.170\times10^{-4}$ | $0.092\times10^{-4}$ |
| 100% | $0.364\times10^{-4}$ | $0.184\times10^{-4}$ |

(in units of $\delta v/v$, so $1\times10^{-4}$ is $0.01$ percentage points) and, at
20% noise, a coda of $1$, $2$ and $4\ \mathrm{s}$ gives scatters of $0.355$, $0.121$
and $0.058\times10^{-4}$. The measured scatter exceeds the Cramér–Rao prediction by
a factor of about **1.9** where it is well above the search-grid step, because the
estimator resamples by linear interpolation: the bound is optimistic, and reporting
it as an achieved precision would be an overclaim. Even so, both are two orders of
magnitude finer than the $2\%$ picking threshold of Section 3.2.

### 3.4 Distributed versus localised change: a coverage problem

Write the observable as a vector $\mathbf d$ of per-path travel-time changes and
the two hypotheses as the sensitivity vectors

$$\mathbf s_A = \mathbf t \quad\text{(a uniform change scales with path time)},$$
$$\mathbf s_B = \left(h_i^{(1)}/v_1\right)_i \quad
\text{(only the top layer changes)},$$

where $h_i^{(1)}$ is the length of path $i$ in the top layer. A data set of $n$
paths has $n$ numbers; each hypothesis has one free amplitude; so the hypotheses
are separable only insofar as $\mathbf s_A$ and $\mathbf s_B$ are **not parallel**.
Measured, for the teaching model and a 5% top-layer change with a $0.5\ \mathrm{ms}$
picking error:

| path set | correlation of $\mathbf s_A,\mathbf s_B$ | rejection of the wrong hypothesis |
|---|---|---|
| three deep paths (one depth range) | $+1.0000$ | $4.3\%$ (the false-positive rate) |
| shallow, mid and deep paths | $-0.8611$ | $19.3\%$ |

So depth coverage creates the *possibility* of separation — the wrong hypothesis is
never rejected when the paths are parallel — but the *decision* still needs the
signature difference to exceed the noise. The demonstration computes the
requirement: with a $0.5\ \mathrm{ms}$ picking error a decisive rejection at 95%
needs a top-layer change of $11.0\%$, not the $5\%$ used. **Coverage and
signal-to-noise are two different budgets, and a monitoring design has to spend
both.**

### 3.5 Environmental aliasing

Any process that changes the near surface between epochs is aliased with the
target. With a teaching sensitivity $\mathrm dv/\mathrm dT = -0.5\
\mathrm{m\,s^{-1}\,K^{-1}}$ at $v = 400\ \mathrm{m\,s^{-1}}$:

| $\Delta T$ (K) | $\delta v/v$ | $\delta t$ on a 20 m path ($t = 50\ \mathrm{ms}$) |
|---|---|---|
| 1 | $-0.125\%$ | $0.062\ \mathrm{ms}$ |
| 2 | $-0.250\%$ | $0.125\ \mathrm{ms}$ |
| 5 | $-0.625\%$ | $0.313\ \mathrm{ms}$ |
| 10 | $-1.250\%$ | $0.625\ \mathrm{ms}$ |

A seasonal swing of a few kelvin therefore produces changes of the same order as
the target — and *larger* than the coda method's precision, so the coda does not
solve this problem; it makes the aliasing more visible. The two standard defences
are (i) a **reference site** whose target does not change, measured with the same
instrument and geometry, and subtracted, and (ii) an **independent measurement of
the confounding variable** (temperature, moisture, piezometric level) used as a
regression covariate. Neither removes the aliasing where the target and the
confounder respond at the same depth and frequency; that case has to be designed
around.

## 4. Physical interpretation

**Repeatability is a design quantity.** Because NRMS scales with noise, it is set
by coupling, source stability and geometry control, and it can be improved by
spending survey time. It is *not* improved by better processing, which usually
correlates the noise between epochs and thereby *understates* the true
repeatability.

**The coda is a distributed sensor.** A picking-based measurement uses one
arrival; a coda measurement uses the whole scattered record, whose energy has
sampled a large volume. That is why the precision improves with coda length
($0.355 \to 0.058\times10^{-4}$ from 1 s to 4 s here) and why coda methods can
detect changes two orders of magnitude below the picking threshold. The price is
that the coda measurement is *not localised*: it reports an average velocity
change over the volume the coda sampled, and separating depths requires the
sensitivity-vector analysis of Section 3.4 (see also
[06-07 Ambient Noise and Interferometry](../../06-seismology/07-ambient-noise-and-interferometry/README.md)).

**A 4-D difference is not a 4-D inversion.** Subtracting two images produces a
difference image in which any baseline error appears as a change. Where the
baseline is uncertain, the difference must be inverted jointly with the baseline;
otherwise the "change" is a map of the baseline's own artefacts.

**The third state counts.** Monitoring designs are usually decided by the ratio of
the expected change to the repeatability. When those are comparable, the cheapest
improvement is often a third epoch, not a new method: a three-epoch series can be
fitted for a linear trend and its residual, which separates a slow environmental
drift from a step change in the target.

## 5. Worked examples

### Example 1 — Is a 0.4% velocity change detectable?

A 20 m path in a $400\ \mathrm{m\,s^{-1}}$ medium gives $t = 50.00\ \mathrm{ms}$.
With a picking error of $0.5\ \mathrm{ms}$, $\sigma_\epsilon = 0.5/50 = 1.0\%$:
the $0.4\%$ change is **not** detectable by picking. The same change shifts the
arrival by

$$\delta t = \epsilon t = 0.004 \times 50 = 0.2\ \mathrm{ms},$$

which is a factor of $2.5$ below the pick.

### Example 2 — The same change by coda stretching

The coda estimator at 20% noise reaches a scatter of $0.057\times10^{-4}$, i.e.
$5.7\times10^{-6}$ — a factor of $700$ finer than $0.4\%$. The 0.4% change is
therefore detected with an enormous margin, **provided** the coda is available
(the record must contain a scattered tail) and provided the change is spatially
uniform enough that a single stretch describes it. If the change is confined to
one layer, the coda stretches non-uniformly and the single-stretch estimator
returns an average whose interpretation needs Section 3.4.

### Example 3 — A decisive test of a localised change

For the mixed-depth path set with a $0.5\ \mathrm{ms}$ picking error, the
noiseless $\chi^2$ of the *wrong* hypothesis at unit amplitude is $497$
(demonstration). Since $\chi^2$ scales as the square of the change amplitude, a
rejection at the 95% point ($\chi^2 = 5.99$ for two degrees of freedom) requires

$$\epsilon_{\text{needed}} = \sqrt{\frac{5.99}{497}} = 0.110,$$

i.e. an $11.0\%$ top-layer change — not the $5\%$ assumed. Two ways to buy the
margin: reduce the picking error by a factor of four (to $0.125\ \mathrm{ms}$), or
add a fourth path whose top-layer share is very different from the existing three
(which changes $\chi^2_{\text{unit}}$ rather than the noise).

### Example 4 — Correcting for temperature

Suppose the target is a $0.5\%$ velocity change in a layer and the survey spans a
$4\ \mathrm{K}$ seasonal change, which by Section 3.5 contributes $0.50\%$ if it
acts uniformly. The raw change is then $1.00\%$ and the target is a factor of two
error. With a reference site that sees the same $4\ \mathrm{K}$ but no target
change, the correction subtracts $0.50\%$ and leaves the target — *if* the
reference's sensitivity is the same. The residual error is the difference of the
two sensitivities times $4\ \mathrm{K}$, which is the quantity a reference-site
design has to bound, not the temperature itself.

## 6. Assumptions and regime of validity

1. **Repeatable geometry.** Sources and receivers at the same positions to a small
   fraction of the shortest wavelength; a repositioning error of a tenth of a
   wavelength is a change of the same size as many targets.
2. **Repeatable coupling.** Ground contact, planting depth and instrument gain must
   be reproduced, or the observed change is coupling. This is the commonest cause
   of a spurious 4-D anomaly in the very shallow section.
3. **A spatially coherent change for the stretch estimator.** A single stretch
   factor describes a *uniform* relative velocity change. Depth-dependent changes
   produce depth-dependent stretching and require either a layered stretching model
   or a 4-D inversion.
4. **Noise is stationary between epochs.** If the noise level itself changes (a
   wetter surface, a noisier site), the repeatability measured on the baseline
   understates the error of the difference.
5. **The confounders are measured.** Temperature, moisture and water level change
   with the target unless they are recorded; unmeasured confounders cannot be
   corrected statistically.
6. **Independence of the error terms.** A shared systematic error (a mis-calibrated
   instrument, a mis-located station) correlates the epochs and does not cancel in
   the difference; it *grows* in a ratio.
7. **The target is not the baseline.** A large enough change invalidates the
   linearisation $\delta t = -\epsilon t$ and the single-stretch model; repeat the
   baseline when the change exceeds a stated fraction (a few per cent is the usual
   trigger).

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| repeatability | NRMS | % | $\sqrt{2}\sigma/S$ |
| travel time | $t$ | s | $\int\mathrm dl/v$ |
| picking error | $\sigma_t$ | s | |
| relative velocity change | $\epsilon = \delta v/v$ | dimensionless | $-\delta t/t$ |
| stretch factor | $1+\epsilon$ | dimensionless | applied to the time axis |
| coda derivative energy | $\sum(t g')^2$ | (trace$^2$) | sets $\sigma_\epsilon$ |
| environmental sensitivity | $\mathrm dv/\mathrm dT$ | $\mathrm{m\,s^{-1}\,K^{-1}}$ | site property |

Checks worth doing: $\epsilon$ must be dimensionless, so a travel-time change in
milliseconds must be divided by a travel time in milliseconds; and $\sigma_\epsilon$
from the coda formula must be dimensionless, so the noise and the derivative energy
must be in the same amplitude units.

## 8. Python demonstration

`code/time_lapse_demo.py` implements the whole chain and prints labelled results
with units. It:

1. measures NRMS against noise level ($0.70\%$ at 0.5% noise up to $14.04\%$ at
   10%) and confirms the $\sqrt{2}$ factor;
2. tabulates the $\epsilon$ resolution for four path/velocity combinations
   ($1.00\%$ for a 20 m path at $400\ \mathrm{m\,s^{-1}}$);
3. implements the stretching estimator with a coarse-to-fine search, measures its
   bias and scatter against noise and against coda length
   ($0.355 \to 0.058\times10^{-4}$ from 1 s to 4 s at 20% noise), and compares with
   the Cramér–Rao prediction, which it exceeds by a factor of $1.9$;
4. tabulates the environmental aliasing for temperature changes of 1–10 K;
5. computes the rejection rate of a *wrong* change hypothesis for two path sets
   ($4.3\%$ versus $19.3\%$) and derives the change amplitude needed for a
   decisive rejection ($11.0\%$).

The demonstration is print-only, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network, and runs in about two seconds.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-time-lapse-nearsurface-exercises.md`](./exercises/01-time-lapse-nearsurface-exercises.md)
and
[`exercises/01-time-lapse-nearsurface-solutions.md`](./exercises/01-time-lapse-nearsurface-solutions.md).

- **★** Two repeats give NRMS $3.0\%$. What noise level does that imply, and what
  is the smallest velocity change detectable by a $0.5\ \mathrm{ms}$ pick on a
  $40\ \mathrm{ms}$ path?
- **★★** Compute the coda-precision ratio between a 1 s and a 4 s coda from the
  measured values, and compare with the $T^{3/2}$ prediction.
- **★★** A monitoring survey over 6 months spans a $6\ \mathrm{K}$ temperature
  change. Using the teaching sensitivity, compute the aliased $\delta v/v$ and
  state whether a $0.3\%$ target change is measurable without a reference site.
- **★★★** Design a four-path monitoring layout that would reject the localised
  change hypothesis with a $0.25\ \mathrm{ms}$ pick, and state the amplitude you
  could then detect.

## Mastery checkpoint
Complete this without notes:

> A monitoring experiment has a 20 m path in a $400\ \mathrm{m\,s^{-1}}$ medium, a
> coda of 3 s, a picking error of $0.4\ \mathrm{ms}$ and a noise level of 15%.
> **(a)** Compute the picking-based $\epsilon$ resolution. **(b)** Estimate the
> coda-based resolution using the measured scalings, and state the assumption that
> makes the comparison legitimate. **(c)** State the NRMS you expect between two
> baseline repeats and what it implies about the detection threshold. **(d)** A
> $3\ \mathrm{K}$ temperature change occurs between the epochs: compute its
> aliased $\delta v/v$ and say whether your answer to (b) survives. **(e)** State
> the design change that would separate the target from the temperature.

A worked version of (a)–(c) appears in the exercise solutions.

## Common pitfalls
1. **Reporting a change without a repeatability.** Without an NRMS or a repeated
   baseline, a 4-D anomaly cannot be distinguished from noise.
2. **Using the baseline repeat noise as the error of the difference.** If the
   monitor's noise differs (wetter ground, noisier site), the error is larger.
3. **Assuming the coda measurement is localised.** It is an average over the
   sampled volume until a sensitivity analysis says otherwise.
4. **Treating a 4-D difference as an inversion.** Baseline artefacts appear as
   changes.
5. **Ignoring the environment.** Temperature and moisture changes of the same order
   as the target are the normal case in the shallow subsurface, not the exception.
6. **Repeating the baseline for too long.** Once the change exceeds a few per cent,
   the linearisation behind $-\delta t/t$ and the single stretch fails; a new
   baseline is required.
7. **Quoting the Cramér–Rao bound as achieved precision.** The demonstration
   measures a factor of $1.9$ between the two.
8. **Designing for signal-to-noise only.** Coverage — the diversity of depth
   sensitivities — decides whether a distributed change can be separated from a
   localised one at all.

## Related modules
- [10-06-02 Monitoring Dams, Embankments and Foundations](02-geotechnical-monitoring.md) —
  the application that motivates most shallow monitoring.
- [10-06-03 Monitoring Contaminant Transport with Geophysics](03-contaminant-monitoring.md) —
  the other application, with a designed change rather than a natural one.
- [10-05-05 Integrating Near-Surface Methods](../05-other-near-surface-methods/05-multi-method-nearsurface.md) —
  sensitivity vectors in method space; this lesson does the same in time.
- [06-07 Ambient Noise and Seismic Interferometry](../../06-seismology/07-ambient-noise-and-interferometry/README.md) —
  the same coda interferometry at regional scale, and the source of most of the
  methodology.
- [14-05 Time-Lapse and Monitoring Hydrogeophysics](../../14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/README.md) —
  the hydrological interpretation of a monitored change.
