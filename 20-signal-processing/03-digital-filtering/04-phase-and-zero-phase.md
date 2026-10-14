---
id: 20-03-04
title: "Phase Response, Zero-Phase Filtering and Distortion"
level: doctoral
prereqs: ["20-03-02", "20-03-03", "20-01-04"]
tags: [signal-processing, filtering, phase, group-delay, zero-phase, filtfilt, distortion, dispersion]
---

# Phase Response, Zero-Phase Filtering and Distortion

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the group delay from the phase response and **state** the condition
   for a filter to be dispersionless.
2. **Prove** that a causal stable IIR filter cannot have exactly linear phase, and
   **quantify** the resulting delay variation by measurement.
3. **Measure** the peak shift and the envelope asymmetry a causal filter imposes
   on a wavelet, and **separate** them from any amplitude change.
4. **Explain** forward-backward (`filtfilt`) filtering as the cascade
   $H(e^{i\omega})H(e^{-i\omega}) = |H|^2$, and **derive** both its zero phase and
   its doubled magnitude cost.
5. **Choose** between causal and zero-phase filtering from a stated requirement on
   the waveform, and **state** what each one costs.
6. **Predict** the residual phase of a small-mismatch forward-backward filter.

## Prerequisites

- [20-03-02 IIR Filter Design: Butterworth, Chebyshev, Elliptic](02-iir-filters.md) —
  the causal filters whose phase is measured here.
- [20-03-03 Filter Selection for Geophysical Data](03-filter-applications.md) —
  the practical filtering chain that uses these results.
- [20-01-04 Transfer Functions, Poles and Zeros](../01-signals-and-systems/04-transfer-functions.md) —
  the rational response and its pole-zero picture.

## 1. Intuition: the phase is half the filter

A filter is a complex number at every frequency. Magnitude tells you *how much*
of each frequency survives; phase tells you *when* it arrives. Seismic
interpretation cares about both: a first-break time, a converted-phase polarity, a
reflection coefficient sign or an AVO gradient are all encoded in arrival time and
waveform shape, not only in amplitude.

A causal filter must produce its output after its input, so it necessarily
delays. The question is whether it delays *all* frequencies equally. An FIR filter
with symmetric coefficients does, to the last bit. A causal IIR filter does not:
its group delay grows toward the cutoff, so a broadband wavelet is smeared. That
smearing is dispersion, and it is a phase artefact — the amplitude spectrum is
unchanged.

All models and data in this module are SYNTHETIC. The wavelets and filters
are chosen teaching objects.

## 2. Definitions

### 2.1 Phase and group delay

Write $H(e^{i\omega}) = |H(\omega)|e^{i\phi(\omega)}$. The **phase delay** at
$\omega$ is $-\phi(\omega)/\omega$ (the time a pure sinusoid is shifted); the
**group delay** is

$$\tau_g(\omega) = -\frac{\mathrm{d}\phi(\omega)}{\mathrm{d}\omega},$$

the delay of a narrow band around $\omega$. They coincide only when $\phi$ is
linear.

### 2.2 Phase classes

- **Linear phase**: $\phi(\omega) = -\omega\tau_0 + \pi m$, so $\tau_g = \tau_0$
  constant. Realised exactly by a symmetric (or antisymmetric) FIR filter.
- **Zero phase**: $\phi(\omega) = 0$, so $\tau_g = 0$. Not realisable causally;
  realisable only by non-causal (offline, forward-backward) processing.
- **Minimum phase**: all zeros inside the unit circle; the phase is the smallest
  possible for a given magnitude.
- **Non-linear phase**: everything else; $\tau_g$ depends on $\omega$.

### 2.3 Causality

A causal filter's impulse response vanishes for $n<0$. For a rational transfer
function, causality plus stability means every pole lies strictly inside the unit
circle.

## 3. Derivations

### 3.1 Why a causal IIR filter cannot be linear phase

Suppose $H(z)$ were causal, stable and linear phase. Linear phase requires the
zero set to be symmetric under $z \to 1/z^{*}$ (a zero at $z_0$ paired with one at
$1/z_0^{*}$). But stability requires all poles strictly inside the unit circle,
and a causal filter cannot have poles outside it. A linear-phase rational filter
therefore needs its poles to be symmetric in pairs $z_p, 1/z_p^{*}$ — which puts
at least one pole of each pair outside the unit circle, contradicting causality
and stability. Hence no causal, stable, rational filter has exactly linear phase
unless it is FIR. This is the reason the measured group delay of the demo's
Butterworth swings by several samples while the FIR's is flat to $10^{-12}$.

### 3.2 Forward-backward filtering

Filter forward, reverse the output, filter again, and reverse back. In the
frequency domain the reverse of a sequence conjugates its transform, so the total
operation is

$$H_{\text{ff}}(e^{i\omega}) = H(e^{i\omega})\,H^{*}(e^{i\omega})
= \left|H(e^{i\omega})\right|^2.$$

Two consequences follow immediately and exactly:

- the phase of $H_{\text{ff}}$ is zero, because a positive real number has zero
  phase: **the output is zero-phase**;
- the magnitude is squared, so a filter giving $-3$ dB at cutoff applied
  forward-backward gives $-6$ dB, and one giving $-21.97$ dB gives $-43.94$ dB.

The demo measures exactly this: at 20, 40, 60 and 90 Hz the causal response is
$-0.00$, $-0.03$, $-3.01$ and $-21.97$ dB, and the squared (forward-backward)
response is $-0.00$, $-0.06$, $-6.02$ and $-43.94$ dB. **Zero phase is bought by
doubling the magnitude roll-off**: `filtfilt` with order $n$ behaves like
a causal filter of order $2n$.

### 3.3 Cascaded group delays add

The phase of a product is the sum of phases, so group delays add:
$\tau_g^{(1\cdot 2)} = \tau_g^{(1)} + \tau_g^{(2)}$. Forward-backward filtering is
a cascade of $H$ and $H^{*}$; their group delays are equal and opposite at every
frequency, so the sum is zero at every frequency. That is the mechanism, and it is
why the cancellation is exact and not merely approximate.

## 4. The measurement

The demo's causal filter is a 6th-order Butterworth lowpass at $f_c = 60$ Hz with
$f_s = 1000$ Hz. Its measured passband group delay is $11.5538 \pm 1.3905$ samples
(two standard deviations of the variation), rising monotonically:

| frequency (Hz) | group delay (samples) |
|---|---|
| 5 | 10.155 |
| 20 | 10.610 |
| 40 | 12.915 |
| 55 | 17.395 |

The 101-tap Hamming FIR at the same cutoff has a measured passband group delay of
$50.0000 \pm 2.45\times10^{-12}$ samples — the exact $(101-1)/2$. **One filter
delays every frequency by 50 samples; the other delays 5 Hz by 10.2 samples and
55 Hz by 17.4 samples.** The second one disperses.

The effect on a wavelet is quantified in three numbers. A 35 Hz Ricker wavelet
peaking at sample 1000 becomes, after causal filtering:

- peak at sample **1011** — an 11-sample (11.00 ms) shift, close to the
  $11.99$-sample group delay measured at 35 Hz;
- **envelope asymmetry $|\text{skew}|$ growing from 0.0092 to 0.0233** — a
  two-and-a-half-fold increase, i.e. the wavelet is no longer symmetric;
- zero-phase `filtfilt` restores the peak to sample **1000** (shift $+0$) and
  reduces the asymmetry to 0.0076, close to the input's 0.0092.

The asymmetry figure is the important one. A peak shift can be corrected by
subtracting a constant; skew cannot be corrected by shifting, because different
frequencies within the wavelet have been delayed by different amounts. A causal
filter has changed the wavelet's shape, and shape is signal.

## 5. Worked example (SYNTHETIC)

A 500 Hz-sampled trace must be low-passed at 80 Hz and then used to pick a
first-break time to within 2 ms.

1. **Causal option**: a 6th-order Butterworth at 80 Hz. Its group delay near DC is
   about 10 samples $= 10/500 = 20$ ms, and it varies by several samples across
   the band. A first-break at 20 Hz and a reflection wavelet centred at 60 Hz
   would be shifted by *different* amounts, so a single time correction is not
   enough. This option fails the 2 ms requirement.
2. **Zero-phase option**: apply `filtfilt` with the same filter. The peak shift
   becomes 0 samples, so the requirement is met trivially. The cost is the doubled
   roll-off: the response at 120 Hz becomes approximately $-2\times 21.9 = -43.8$
   dB instead of $-21.9$ dB, which is *better* attenuation and therefore usually
   welcome.
3. **The real cost of zero-phase filtering** is that it is non-causal: it requires
   the whole record, so it cannot be used in real time, and it smears energy
   *before* the first arrival (from the reverse pass) where a causal filter would
   not. For a first-break pick at the very start of a record, that pre-arrival
   smearing can be worse than a phase shift. The fix is to pad the record or to
   accept the causal filter and correct only the group delay.
4. **A concrete check**: after `filtfilt` the effective order is 12. For an
   order-12 Butterworth the numerical conditioning in direct form starts to
   matter in single precision; use `sos` (second-order sections) or scale
   coefficients down.

The example shows the decision rule: **if the waveform's shape or relative timing
matters, use zero phase; if the filter must be causal or real-time, use a causal
filter and correct its group delay, accepting the dispersion.**

## 6. Assumptions and regime of validity

1. **The filter is time-invariant.** Zero-phase filtering cancels the phase of a
   *fixed* filter. If the filter adapts with time
   ([05](05-adaptive-filtering.md)), the cancellation is only approximate.
2. **The record is long compared with the filter's effective length.** `filtfilt`
   pads the ends; a record barely longer than the filter has edge transients.
3. **The phase of the input is meaningful.** If the input is a stacked,
   zero-phase-processed section, applying a *causal* filter reintroduces a phase
   that a previous step removed.
4. **Amplitude preservation is not required.** Squaring $|H|$ is harmless when you
   want more attenuation, harmful when you need a flat passband: a 1 dB ripple
   becomes 2 dB.
5. **The group-delay measurement bandwidth is adequate.** A numerical derivative of
   an unwrapped phase is only as good as the frequency grid; the demo uses 8192
   points to keep the derivative smooth.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| phase | $\phi$ | rad | unwrap before differentiating |
| group delay | $\tau_g$ | samples | $\mathrm{d}\phi/\mathrm{d}\omega$, (rad)/(rad/sample) |
| group delay | — | s | $\tau_g/f_s$ |
| magnitude | $\|H\|$ | dimensionless | or dB via $20\log_{10}$ |
| power gain | $\|H\|^2$ | dimensionless | twice the dB |

The trap is the last row: squaring a magnitude doubles its value in **dB**, not
its ratio. $-3.01$ dB becomes $-6.02$ dB, and the *amplitude* ratio falls from
0.707 to 0.500, a factor of two, not four.

## 8. Python demonstration

`code/phase_zero_phase_demo.py` measures the group delay of a linear-phase FIR
and a causal IIR, the peak shift and envelope asymmetry they impose on a wavelet,
the zero-phase restoration by `filtfilt`, and the doubling of the magnitude
response in dB. It is self-contained, seeded with
`np.random.default_rng(20261014)`, and exits 0.

What to look for:

1. **section 1** — group delay constant to $10^{-12}$ for FIR, varying by
   1.4 samples for IIR.
2. **section 2** — the 11-sample peak shift and the 2.5× asymmetry growth.
3. **section 3** — `filtfilt` returns the peak to its original sample and the
   asymmetry to near its input value.
4. **section 4** — $|H|^2$ in dB is exactly twice $|H|$ in dB: $-3.01 \to -6.02$,
   $-21.97 \to -43.94$.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/04-phase-and-zero-phase-exercises.md`](exercises/04-phase-and-zero-phase-exercises.md)
and
[`exercises/04-phase-and-zero-phase-solutions.md`](exercises/04-phase-and-zero-phase-solutions.md).

- **★** Compute the group delay in milliseconds of a 201-tap linear-phase FIR at
  $f_s = 400$ Hz.
- **★★** From the group-delay table of §4, estimate the differential delay between
  a 10 Hz and a 55 Hz component.
- **★★** Show that `filtfilt` with a 1 dB-ripple filter produces a 2 dB-ripple
  output, and explain the consequence for an amplitude study.
- **★★★** A forward-backward filter uses two *different* filters $H_1$ and $H_2$.
  Derive the residual phase and show that it vanishes only if $|H_1| = |H_2|$ or
  the phases cancel.

## Mastery checkpoint

Complete this without notes:

> A 1 Hz Ricker wavelet at 40 Hz on a 1000 Hz-sampled trace is passed through a
> causal 4th-order Butterworth lowpass at 50 Hz. **(a)** State whether the output
> magnitude at 40 Hz changes much, and why the waveform still looks different.
> **(b)** Predict the sign of the peak shift (earlier or later) and explain.
> **(c)** State what `filtfilt` with the same filter would do to the peak position
> and to the attenuation at 80 Hz. **(d)** Give the effective order of the
> `filtfilt` result. **(e)** State one situation in which you would prefer the
> causal filter despite the distortion.

A worked version appears in the
[solutions](exercises/04-phase-and-zero-phase-solutions.md).

## Common pitfalls

1. **Correcting a phase problem with a time shift.** A constant shift fixes a
   linear phase; dispersion needs a phase correction or zero-phase filtering.
2. **Assuming `filtfilt` is free.** It doubles the magnitude roll-off and the
   effective order, and it smears energy before the first arrival.
3. **Measuring group delay on a coarse frequency grid.** The numerical derivative
   of an unwrapped phase needs a fine grid; the demo uses 8192 points.
4. **Reading asymmetry off the raw wavelet.** A two-sided wavelet has zero mean, so
   the raw third moment is undefined-ish; use the analytic envelope, as the demo
   does.
5. **Applying a causal filter to data that was previously zero-phased.** You
   reintroduce exactly the distortion the earlier processing removed.

## Related modules

- [20-03-02 IIR Filter Design: Butterworth, Chebyshev, Elliptic](02-iir-filters.md) —
  the origin of the non-linear phase measured here.
- [20-03-01 FIR Filter Design: Windows, Parks-McClellan, Least Squares](01-fir-filters.md) —
  the exactly-linear-phase alternative.
- [20-03-03 Filter Selection for Geophysical Data](03-filter-applications.md) —
  the chain in which these filters are used.
- [20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation](../04-deconvolution-and-inverse-filtering/01-deconvolution-concept.md) —
  why the deconvolution operator also has a phase, and why that phase matters for
  spiking.
- [01-10-06 Hilbert Transform, Analytic Signal and Instantaneous Phase](../../01-mathematics/10-fourier-analysis/06-hilbert-transform.md) —
  the envelope and instantaneous-phase tools used to measure asymmetry.
- [06-08-01 Receiver Functions: Deconvolution and Ps Conversions](../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md) —
  a method whose delay measurements are destroyed by unknown phase.
