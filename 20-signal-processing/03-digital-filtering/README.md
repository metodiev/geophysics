# Module 20-03 — Digital Filtering

**Stages:** advanced → research · **Prerequisites:** modules 20-01 and 20-02;
basic Python and SciPy.

Every geophysical record is filtered, usually several times, and each filter is a
decision about which frequencies are signal and which are interference. This
module is about making that decision explicitly and measuring its consequences.
It starts with the two design families — finite impulse response filters, whose
phase can be made exactly linear, and infinite impulse response filters, which buy
sharpness with feedback and pay for it in phase — and then moves to the questions
that decide real processing: which filter for which contaminant, what the phase
cost of a causal filter does to a wavelet, how to adapt a filter to unknown
interference, and how an array adds a second dimension in which to separate
events.

The organising tension is **efficiency against fidelity**. An IIR filter meets a
specification with roughly a tenth of the coefficients of an FIR filter, but its
group delay varies across the band, so it disperses the waveform. A zero-phase
implementation removes the dispersion and doubles the magnitude roll-off and the
effective order. A causal filter is realisable in real time but distorts; a
non-causal one is honest about the waveform but needs the whole record. Each
lesson states which of these it is trading and measures the size of the trade,
rather than asserting that one choice is correct.

Two results are worth carrying out of the module. First, the *window* controls a
windowed design's stopband floor and the *order* controls its transition width;
these are independent knobs, and the module measures both. Second, array filtering
is limited by acquisition: an event steeper than the spatial Nyquist aliases onto
an apparent dip that can be exactly the signal dip, and the demo retains 94.9% of
such an event through a filter designed to reject it. No processing step can
recover the information that a too-coarse trace spacing never recorded.

All models and data in this module are SYNTHETIC. The specifications,
wavelets, traces and gathers are chosen teaching objects, not measurements from
any instrument or survey.

## Learning objectives

By the end of this module you will be able to:

1. **Design** an FIR filter by the window method, by Parks-McClellan and by least
   squares, and **state** which error norm each one minimises.
2. **Design** a Butterworth, Chebyshev or elliptic IIR filter for a stated
   specification, and **verify** its order, stability and group-delay variation by
   measurement.
3. **Choose** an ordered filter chain for a contaminated record, and **quantify**
   the signal-to-noise ratio recovered with an explicitly stated metric.
4. **Predict** the alias frequency produced by decimation and **explain** why the
   anti-alias filter cannot be omitted.
5. **Measure** the group delay of a filter, and **explain** when zero-phase
   filtering is required and what it costs.
6. **Configure** an adaptive noise canceller or line enhancer, and **diagnose**
   convergence-versus-misadjustment behaviour from the data.
7. **Design** an f-k fan filter, **measure** its pass and reject performance, and
   **state** the aliasing condition that limits it.

## Prerequisites

- [20-01 Linear Time-Invariant Systems and Impulse Response](../01-signals-and-systems/02-lti-systems.md) —
  the systems this module designs filters for.
- [20-02 Practical DFT/FFT: Normalisation, Units and Pitfalls](../02-fourier-and-spectral-analysis/01-dft-fft-practice.md) —
  how the spectra that motivate a filter are computed.
- [03-03-05 SciPy for Scientific Computing](../../03-scientific-computing/03-scipy/05-signal.md) —
  the `scipy.signal` routines used throughout the demos.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [FIR Filter Design: Windows, Parks-McClellan, Least Squares](01-fir-filters.md) | graduate | Window sets the stopband floor, order sets the transition width; symmetric coefficients give exactly linear phase |
| 02 | [IIR Filter Design: Butterworth, Chebyshev, Elliptic](02-iir-filters.md) | graduate | Ripple in either band buys order; no causal IIR filter has linear phase |
| 03 | [Filter Selection for Geophysical Data](03-filter-applications.md) | advanced | Read the spectrum, then order the chain; a metric can mislead |
| 04 | [Phase Response, Zero-Phase Filtering and Distortion](04-phase-and-zero-phase.md) | doctoral | A causal IIR disperses the wavelet; `filtfilt` gives $\|H\|^2$, zero phase |
| 05 | [Adaptive Filtering and Noise Cancellation](05-adaptive-filtering.md) | research | Let the data set the coefficients; the reference channel is the assumption |
| 06 | [Multichannel and Array Filtering (f-k, Radon)](06-multichannel-filtering.md) | research | Linear events are lines in f-k; aliasing can forge the signal dip |

## Suggested path

**If you are new to digital filtering:** lessons 01 → 02 → 03, running each
demonstration. Lesson 03 is where the design choices in 01 and 02 become a
processing decision.

**If you already design filters:** read 04 §3 (why a causal IIR cannot be linear
phase), then 05 and 06 — the two cases where a fixed filter is the wrong tool.

**If you are preparing a research project:** 04 in full, 05 §3.3 (what breaks a
noise canceller), and 06 §4.2 (the aliasing counter-example), plus the exercises
at ★★★ level.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-fir-filters.md`](01-fir-filters.md) | Lesson 01 |
| [`02-iir-filters.md`](02-iir-filters.md) | Lesson 02 |
| [`03-filter-applications.md`](03-filter-applications.md) | Lesson 03 |
| [`04-phase-and-zero-phase.md`](04-phase-and-zero-phase.md) | Lesson 04 |
| [`05-adaptive-filtering.md`](05-adaptive-filtering.md) | Lesson 05 |
| [`06-multichannel-filtering.md`](06-multichannel-filtering.md) | Lesson 06 |
| [`code/`](code) | Six runnable demonstrations, one per lesson |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and Matplotlib:

```bash
cd 20-signal-processing/03-digital-filtering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fir_filters_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python iir_filters_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python filter_applications_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python phase_zero_phase_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python adaptive_filtering_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multichannel_filtering_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access, completes in well
under a second, and exits 0.

## Mastery checkpoint

Complete this without notes:

> A 500 Hz-sampled shot record carries a 40 Hz reflection, 8 Hz ground roll, a
> 50 Hz power line and its 150 Hz harmonic, and must be decimated to 125 Hz.
> **(a)** Order the filter chain and justify each stage. **(b)** Compute the alias
> frequency of the 150 Hz harmonic if the anti-alias stage were omitted.
> **(c)** Choose a design family for the band-pass and state the phase
> consequence. **(d)** State the group delay of a 121-tap linear-phase version in
> samples and in milliseconds. **(e)** Explain, using the f-k picture, whether the
> ground roll could instead be removed by an array filter, and what acquisition
> change would be needed if it were spatially aliased.

A worked version of (a)–(d) appears in the lesson-03 and lesson-04
[solutions](exercises/03-filter-applications-solutions.md).

## Common pitfalls across this module

1. **Judging a filter by its stopband alone.** Ripple in the passband destroys
   amplitudes that reflection-coefficient and AVO work depends on.
2. **Trusting a rule of thumb instead of measuring.** `kaiserord` is accurate for
   the window it was derived for; the demo's 31-tap row is 40 dB away from the
   estimate because the order is too small.
3. **Ignoring the delay of a causal filter.** A linear-phase FIR delays by
   $(N-1)/2$ samples; an IIR delays different frequencies differently.
4. **Decimating without an anti-alias filter.** A 150 Hz tone becomes a 25 Hz
   tone, indistinguishable from signal.
5. **Taking a spikier or quieter output as proof of success.** Always state the
   metric and check it against a prediction.
6. **Trusting array filtering on aliased data.** The demo passes an aliased event
   with 94.9% of its energy intact.

## Related modules

- [20-01 Signals and Systems](../01-signals-and-systems/README.md) — the
  convolution and transfer-function background.
- [20-02 Fourier and Spectral Analysis](../02-fourier-and-spectral-analysis/README.md) —
  the spectral tools used to choose a band.
- [20-04 Deconvolution and Inverse Filtering](../04-deconvolution-and-inverse-filtering/README.md) —
  the inverse problem that filtering sets up.
- [20-05 Noise and Random Signals](../05-noise-and-random-signals/README.md) — the
  statistical description of the interference these filters remove.
- [20-06 Polarisation and Array Processing](../06-polarisation-and-array-processing/README.md) —
  the estimation counterpart of f-k filtering.
- [06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md) —
  the processing sequence in which these filters are used.
