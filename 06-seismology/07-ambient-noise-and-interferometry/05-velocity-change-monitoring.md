---
id: 06-07-05
title: "Monitoring Velocity Changes with Coda-Wave Interferometry"
level: research
prereqs: ["06-07-03", "06-07-04"]
tags: [seismology, ambient-noise, coda, dv-v, monitoring, uncertainty]
---

# Monitoring Velocity Changes with Coda-Wave Interferometry

**All models and data in this module are SYNTHETIC.** The scattering model, the
noise level and the velocity changes are chosen teaching values, and every
number below is printed by
[`code/velocity_change_monitoring_demo.py`](code/velocity_change_monitoring_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** $\delta t/t = -\delta v/v$ from the travel-time integral and
   **explain** why the coda, not the direct arrival, is the preferred
   observable.
2. **Formulate** the stretching estimator, **derive** its first-order condition
   and **explain** that it returns a sensitivity-weighted average of the local
   changes.
3. **Measure** a $0.2\%$ change to better than $50\ \mathrm{ppm}$ from a
   synthetic coda and **decompose** the residual bias.
4. **Quantify** the dependence of the apparent $\delta v/v$ on the lapse-time
   window, for a uniform and for a shallow-only change.
5. **Measure** the precision of the estimator as a function of frequency band
   and of the number of averaged windows, and **state** the scaling that each
   follows.
6. **State** the four independent ways a measured $\delta v/v$ can be wrong, and
   the test for each.

## Prerequisites

- [06-07-03 Ambient-Noise Tomography and Monitoring](03-noise-tomography.md) —
  the tomographic inversion whose epoch-to-epoch difference is the map form of
  this measurement.
- [06-07-04 Autocorrelation and Body-Wave Microseismics](04-autocorrelation.md) —
  where the coda of a noise record comes from.

---

## 1. Why the coda, and why it stretches

Take a wave that leaves a station, is scattered $n$ times, and returns after
lapse time $t$. Its travel time is a path integral of slowness:

$$t = \int_{\text{path}}\frac{ds}{v(s)} .$$

If the medium's velocity changes everywhere by the same fractional amount
$\delta v/v$, every element of every path changes by the same fraction, so

$$\boxed{\;\frac{\delta t}{t} = -\frac{\delta v}{v}.\;}$$

A velocity *increase* (positive $\delta v/v$) makes arrivals **early**
($\delta t<0$). Two consequences make the coda the preferred observable.

- **Amplification with lapse time.** A given fractional velocity change produces
  a time shift proportional to $t$. At $t = 21\ \mathrm{s}$ a change of
  $2000\ \mathrm{ppm} = 0.2\%$ shifts the arrival by

$$\delta t = -t\frac{\delta v}{v} = -21.0\times 0.0020
= -0.0420\ \mathrm{s} = -42.0\ \mathrm{ms},$$

  which is measurable with a $50\ \mathrm{ms}$ sampling interval only because
  the shift is estimated by correlation, not by picking. The demonstration
  measures $-42.33\ \mathrm{ms}$ for that arrival against a model of $-42.0\
  \mathrm{ms}$, and $-5.66\ \mathrm{ms}$ at $t = 3.0\ \mathrm{s}$ against a model
  of $-6.00\ \mathrm{ms}$.
- **Averaging over many paths.** The coda contains hundreds of scattered
  arrivals with different paths, so the estimate averages over the medium rather
  than sampling one ray.

The cost of using the coda is the mirror image of the benefit: the average is
over **unknown** paths, so a measured $\delta v/v$ is a sensitivity-weighted
average whose weighting depends on the coda's scattering — an interpretation
problem, not a measurement problem.

## 2. The stretching estimator

Let $x_{\text{ref}}(t)$ be a reference coda and $x_{\text{per}}(t)$ a later one.
Define the stretched reference

$$y_{\varepsilon}(t) = x_{\text{ref}}\big(t(1+\varepsilon)\big),$$

i.e. the reference compressed by a factor $1+\varepsilon$ in time. The estimator
is the $\varepsilon$ that minimises the windowed misfit

$$\hat{\varepsilon} = \arg\min_{\varepsilon}
\int_{t_1}^{t_2}\Big[x_{\text{per}}(t) - x_{\text{ref}}\big(t(1+\varepsilon)\big)\Big]^{2}dt .$$

To see what it estimates, expand to first order. Write
$x_{\text{ref}}(t(1+\varepsilon)) \approx x_{\text{ref}}(t)
+ \varepsilon\,t\,\dot{x}_{\text{ref}}(t)$ and let
$x_{\text{per}} = x_{\text{ref}} + \delta x$. Then

$$\hat{\varepsilon} = \frac{-\displaystyle\int_{t_1}^{t_2} t\,\dot{x}\,\delta x\,dt}
{\displaystyle\int_{t_1}^{t_2} \big(t\,\dot{x}\big)^{2}dt},$$

so $\hat\varepsilon$ is the **weighted average** of the local time shifts
$-\delta x/\dot x$ divided by $t$, weighted by $\dot x^{2}$: the estimate is
dominated by the parts of the window where the waveform changes fastest, i.e.
where there is signal. That is both the estimator's strength (it automatically
ignores flat, noisy stretches) and its weakness (the implicit weighting is not
the physical sensitivity kernel you would choose).

**Sign conventions are a classic source of sign errors.** In this lesson a
positive $\hat\varepsilon$ means the medium sped up. The demonstration's search
grid runs from $-1.00\%$ to $+1.00\%$ and reports $\hat\varepsilon$, so the
measured value can be compared directly with the imposed change.

## 3. The measurement, and what its bias is

The demonstration builds a synthetic coda from 58 scattered arrivals between
$1.0\ \mathrm{s}$ and $29.5\ \mathrm{s}$, generated as Ricker wavelets
($f_0 = 2.0\ \mathrm{Hz}$) scaled by random coefficients, records at
$20\ \mathrm{Hz}$, and adds noise at $20\%$ of the coda rms. The perturbed
record is generated **physically**: every arrival time is divided by
$1+\delta v/v$ with $\delta v/v = +0.2000\%$, while the wavelet keeps its shape.
The estimator, by contrast, stretches the whole trace.

| quantity | value |
|---|---|
| true $\delta v/v$ | $+0.2000\%$ ($+2000\ \mathrm{ppm}$) |
| measured $\delta v/v$ | $+0.1957\%$ ($+1957\ \mathrm{ppm}$) |
| error | $-43\ \mathrm{ppm}$ ($-2.15\%$ of the change) |
| residual at the minimum | $0.00537$ |
| noise rms inside the window | $0.00383$ |

The $43\ \mathrm{ppm}$ bias is **not** noise, and it is not a fitting artefact of
the grid: refining the grid by parabolic interpolation changes the answer in the
third decimal. It is the **stretching approximation**. The operator
$x_{\text{ref}}(t(1+\varepsilon))$ stretches the wavelet as well as the arrival
pattern, whereas a velocity change moves the arrivals without changing the
source wavelet. The mismatch is second order in
$\varepsilon\times(\text{bandwidth}\times\text{window})$, which is why it is
small here ($2\%$ of the change) and why it grows with longer lapse windows and
broader bands. A careful study either corrects for it or quotes it as a
systematic.

## 4. The apparent change depends on the window

The most important honesty point in this lesson is that $\delta v/v$ is
**not a single number for a record**: it is a window-dependent average.

*Uniform change* (every arrival moves by the same factor):

| window (s) | measured $\delta v/v$ (ppm) | error (ppm) |
|---|---|---|
| 2-10 | $+2319$ | $+319$ |
| 10-18 | $+2034$ | $+34$ |
| 18-29 | $+1808$ | $-192$ |

All three windows see the true change to within a few hundred ppm, but the
spread ($+2319$ to $+1808$) is an order of magnitude larger than the
single-window standard error in §5 ($\approx51\ \mathrm{ppm}$ at these
parameters). The spread is therefore *systematic in the window*: the early
window has fewer arrivals and the late window a weaker signal-to-noise ratio,
and neither effect is captured by a naive uncertainty.

*Shallow-only change* (only arrivals before $8\ \mathrm{s}$ move):

| window (s) | measured $\delta v/v$ (ppm) |
|---|---|
| 2-10 | $+1546$ |
| 10-18 | $-23$ |
| 18-29 | $-226$ |

An early window is dominated by arrivals that have spent their time in the
shallow structure and reports a large apparent change; a late window is
dominated by arrivals that have penetrated deeper and reports essentially
nothing. The same data, two different answers, both correct — and neither is
"the" $\delta v/v$ of the medium. The phrase "we measured $\delta v/v$" is
incomplete without the window, the band and the reference model.

## 5. Precision: what one measurement can resolve

Forty independent noise realisations per band, both records band-passed before
stretching:

| band (Hz) | centre period (s) | std of $\delta v/v$ (ppm) | resolution scale (s) |
|---|---|---|---|
| 0.5-1.0 | 1.414 | 349 | 1.000 |
| 1.0-2.0 | 0.707 | 64 | 0.500 |
| 2.0-4.0 | 0.354 | 38 | 0.250 |
| 4.0-8.0 | 0.177 | 19 | 0.125 |

The scatter falls monotonically as the band moves to shorter periods — by
factors of $5.5$, $1.7$ and $2.0$ between successive bands, i.e. faster than the
factor $2$ per band that a naive $1/f$ argument would give. The reason is
visible in the last column: a shorter period packs more cycles into the same
window, so a given fractional time shift produces a larger phase change at the
estimator. The physical price is also visible in the same column: the resolution
scale $1/f_{\max}$ shrinks, so the method's *sensitivity* is to progressively
shallower and more heterogeneous structure. This is not a free lunch; it is the
standard trade of a frequency-dependent depth kernel.

**Scaling argument.** For an arrival measured with signal-to-noise ratio
$\rho$ at frequency $f$, the timing precision is of order
$\sigma_t \approx 1/(2\pi f\rho)$, and since $\delta v/v = \delta t/t$ over a
window of characteristic lapse time $t$,

$$\sigma_{v} \approx \frac{1}{2\pi f\,t\,\rho}.$$

**Worked numeric example (fully worked, using the measured table).** Invert the
formula to obtain the *implied* signal-to-noise ratio of each band, with
$t = 17\ \mathrm{s}$ (the 5-29 s window) and the band centre frequency
$f = 1/\sqrt{f_1f_2}$:

| band (Hz) | $f$ (Hz) | $\sigma_v$ (ppm) | implied $\rho = 1/(2\pi f t \sigma_v)$ |
|---|---|---|---|
| 0.5-1.0 | 0.707 | 349 | $1/(2\pi\times0.707\times17\times3.49\times10^{-4}) = 37.9$ |
| 1.0-2.0 | 1.414 | 64 | $1/(2\pi\times1.414\times17\times6.4\times10^{-5}) = 103.5$ |
| 2.0-4.0 | 2.828 | 38 | $1/(2\pi\times2.828\times17\times3.8\times10^{-5}) = 87.1$ |
| 4.0-8.0 | 5.657 | 19 | $1/(2\pi\times5.657\times17\times1.9\times10^{-5}) = 87.1$ |

The implied signal-to-noise ratio is roughly constant at $\rho\approx88$ for the
three higher bands — which is the statement that the formula's shape is right —
and drops to $38$ in the lowest band, because a $0.7\ \mathrm{Hz}$ wave has only
about $12$ cycles in a $17\ \mathrm{s}$ window while a $5.7\ \mathrm{Hz}$ wave has
about $96$. **A formula that ignores the number of cycles in the window
over-predicts the precision at long period**, and the $38$-versus-$88$ ratio is
the size of that error here.

## 6. Precision: what averaging buys

Averaging $N$ independent realisations and measuring the scatter of the mean
over 20 repetitions:

| $N$ | std of the mean (ppm) |
|---|---|
| 1 | 51 |
| 2 | 34 |
| 4 | 19 |
| 8 | 21 |
| 16 | 11 |

A straight-line fit in log-log coordinates gives

$$\frac{d\log_{10}(\text{std})}{d\log_{10}N} = -0.526$$

against the $-0.500$ of the $\sqrt{N}$ law; the deviation is within the sampling
error of a 20-repetition estimate. Averaging *independent* measurements is the
only honest way to buy precision, and the independence must be verified: two
"realisations" that share the same noise (or the same source field) do not
average down, which is exactly the shortfall measured in lessons 02 and 04
($-0.471$ and $-0.454$).

## 7. The four ways a $\delta v/v$ measurement is wrong

1. **Source change mistaken for a medium change.** A change in the noise source
   distribution between epochs changes the retrieved phase (lesson 01 §6: a
   $45^\circ$ sector moves the coherence magnitude from $0.184$ to $0.929$ and
   rotates its phase), and it can produce a travel-time change of either sign.
   *Test:* compare the retrieval **amplitudes** between epochs; a source change
   alters both amplitude and time, a deep medium change alters the times first.
2. **Window and band dependence.** §4 shows a systematic spread of
   $\pm300\ \mathrm{ppm}$ between windows for a uniform change and a
   sign-changing apparent value for a shallow change. *Test:* measure the change
   in several windows and report the profile, not the single number.
3. **Common-mode non-tectonic forcing.** Pressure, temperature and pore-fluid
   changes affect all stations; thermoelastic strain in the uppermost metres is
   a standard contaminant. *Test:* correlate the measured $\delta v/v$ with
   independent pressure and temperature records; a common seasonal signal that
   correlates with weather is not a tectonic signal.
4. **The sensitivity kernel is assumed, not measured.** Converting
   $\delta v/v$ into a depth-localised change requires a model of where the coda
   sampled. *Test:* the frequency dependence of §5 is a proxy — if the measured
   $\delta v/v$ does not change between bands, either the change is uniform or
   the coda is not sampling what the model claims.

None of these four is detectable from the $\delta v/v$ time series alone. That
is the honest core of this lesson: the measurement is precise (§5, §6) and
ambiguous (§7) at the same time, and only the *combination* of times,
amplitudes, multiple windows, multiple bands and independent forcing records
resolves which of the four is at work.

## 8. Assumptions and regime of validity

1. **The coda is a fixed set of arrivals.** If the medium changes enough to move
   scatterers (not just to change their velocity), the stretching model fails
   and the estimator returns a biased or unstable value. Small strains
   ($\lesssim10^{-5}$) are usually in the velocity-only regime.
2. **The change is small compared with the wavelet.** The first-order expansion
   of §2 requires $\varepsilon\,t \ll$ wavelet width; with $t = 26\ \mathrm{s}$
   and a $0.5\ \mathrm{s}$ wavelet the linear regime ends near
   $\varepsilon \approx 0.02$, i.e. $2\%$ — two orders of magnitude above the
   changes this lesson measures, so the approximation is safe here and should be
   checked elsewhere.
3. **A reference coda exists and is stable.** Usually a stack of many months is
   used; a reference that is itself perturbed contaminates every epoch.
4. **The noise level is known.** The precision of §5 scales inversely with the
   signal-to-noise ratio, and the residual at the misfit minimum (here
   $0.00537$ against a noise rms of $0.00383$) is one diagnostic that the fit is
   signal-dominated.
5. **The clock and the instrument are stable** to better than the timing
   precision being claimed. At $19\ \mathrm{ppm}$ over a $17\ \mathrm{s}$ window
   the required timing stability is
   $19\times10^{-6}\times17 = 3.2\times10^{-4}\ \mathrm{s} = 0.32\ \mathrm{ms}$,
   which is a real instrument requirement, not a formality.

## Mastery checkpoint

> **(a)** A velocity increase of $0.05\%$ occurs. Compute the time shift at
> $t = 4\ \mathrm{s}$ and at $t = 24\ \mathrm{s}$. **(b)** Your sampling interval
> is $20\ \mathrm{ms}$: which of the two shifts can be picked directly, and why
> does the answer not limit the method? **(c)** Using the measured frequency
> dependence, would you expect the $0.05\%$ change to be detected more
> confidently in the $4$-$8\ \mathrm{Hz}$ band or in the $0.5$-$1\ \mathrm{Hz}$
> band, and what is the trade? **(d)** The measured $\delta v/v$ is
> $+1500\ \mathrm{ppm}$ for the 2-10 s window and $-100\ \mathrm{ppm}$ for the
> 18-29 s window. Give the most likely physical situation and one alternative
> explanation you cannot exclude. **(e)** How many independent windows are
> needed to reach $10\ \mathrm{ppm}$ precision if one window gives
> $50\ \mathrm{ppm}$?

## Common pitfalls

1. **Quoting a single $\delta v/v$ without its window and band.** §4 is the
   demonstration: the number moves by hundreds of ppm between windows.
2. **Reading an apparent change as depth-localised.** The coda's sensitivity is
   a model quantity, not a measurement.
3. **Assuming the source field is stationary between epochs.** This is the
   single most common false positive in the literature of this method, and it is
   testable with amplitudes.
4. **Averaging non-independent realisations.** The measured exponents
   ($-0.471$, $-0.454$, $-0.526$) are the diagnostics; a value far from $-0.5$
   means the samples are correlated or the noise is not stationary.
5. **Forgetting the sign convention.** A positive $\delta v/v$ means faster
   material and earlier arrivals. Sign errors survive review far too often.

## Related modules

- [06-07-03 Ambient-Noise Tomography and Monitoring](03-noise-tomography.md).
- [06-07-04 Autocorrelation and Body-Wave Microseismics](04-autocorrelation.md).
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  the intrinsic-loss mechanisms behind velocity changes in fluids and cracks.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  turning a scatter into a quoted uncertainty.
- [21-03 Bayesian Inference](../../21-statistics-bayesian-ml/03-bayesian-inference/README.md) —
  detecting a change against a noisy baseline.

## Code and exercises

- Demonstration:
  [`code/velocity_change_monitoring_demo.py`](code/velocity_change_monitoring_demo.py).
- Exercises:
  [`exercises/05-velocity-change-monitoring-exercises.md`](exercises/05-velocity-change-monitoring-exercises.md)
  with worked [solutions](exercises/05-velocity-change-monitoring-solutions.md).
