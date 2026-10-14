---
id: 03-03-05
title: "scipy.signal: Filters, Windows and Spectral Estimation"
level: advanced
prereqs: ["03-03-01", "01-10-04", "01-10-05", "03-02-04"]
estimated_minutes: 90
tags: [signal-processing, filters, spectral-analysis, seismology, windows]
---

# scipy.signal: Filters, Windows and Spectral Estimation

A seismogram is a convolution of the Earth's response with a source wavelet,
recorded through an instrument, sampled, and contaminated with noise. Almost
every operation applied to it afterwards — filtering, spectral estimation,
deconvolution, attribute computation — is a statement about its spectrum, and
`scipy.signal` is where those statements are made.

This lesson covers four things that between them account for most of the
practical work:

1. **Filter design** — turning a specification ("40 Hz low-pass, at least
   30 dB down by 100 Hz") into coefficients.
2. **Filter application** — and the difference between a filter you can run
   in a processing loop and one you cannot, which is a difference in
   *causality*, not in quality.
3. **Windows** — the taper you multiply a finite record by, and the two
   errors (leakage, scalloping) it trades against resolution.
4. **Spectral estimation** — `spectrogram` and `welch`, and the one-line check
   that proves the normalisation is right.

The lesson's spine is a single synthetic seismogram whose reflectivity is
known, so that every latency, amplitude and residual reported below is
measurable. Run the demo before reading on:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/signal_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** a synthetic seismogram from a reflectivity series and a Ricker
   wavelet, and verify it against the reflectivity that generated it.
2. **Design** a Butterworth filter to a specification and **verify** the
   specification from its frequency response.
3. **Compute** the group delay of a filter and **measure** the latency it
   imposes on a trace, and explain why the two numbers differ.
4. **Compare** causal and zero-phase filtering in amplitude, latency and
   residual noise, and **prove** the non-causality of `filtfilt` with a
   truncation test.
5. **Choose** a window from its measured mainlobe width and sidelobe level, and
   **explain** leakage and scalloping loss.
6. **Read** a spectrogram knowing its time–frequency trade, and predict the
   bias it introduces on a swept-frequency signal.
7. **Verify** a PSD normalisation with Parseval's theorem in one line.

## Prerequisites

- [03-03-01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — §3.3 on the `numpy.fft` overlap.
- [01-10-04 The Discrete Fourier Transform](../../01-mathematics/10-fourier-analysis/04-discrete-fourier.md)
  — bins, the Nyquist frequency and the transform pair.
- [01-10-05 Windowing and Aliasing](../../01-mathematics/10-fourier-analysis/05-windowing-aliasing.md)
  — why a finite record has a finite spectral resolution.
- [03-02-04 Universal Functions, Reductions and Axis Semantics](../02-numpy/04-ufuncs-reductions.md)
  — the array operations the filter functions are built on.
- [01-11-05 The z-Transform](../../01-mathematics/11-complex-analysis/05-z-transform.md)
  — the pole–zero picture behind a digital filter's transfer function.

## 1. The synthetic seismogram

Every measurement below needs a reference, so the demo builds one. A
reflectivity series of nine picks — nine contrasts in acoustic impedance at
stated two-way times — is convolved with a Ricker wavelet of 32 Hz dominant
frequency, sampled at 500 Hz, and then contaminated with seeded Gaussian noise:

```
  1250 samples at dt = 2.0 ms (500 Hz); 9 reflectors, Ricker f = 32 Hz.
      two-way time (s)  reflectivity   trace at pick (rel. peak)
                 0.250          0.80                      0.8703
                 0.412         -0.45                     -0.4999
                 0.560          0.60                      0.6816
                 0.905          0.70                      0.7565
                 2.240         -0.35                     -0.3799
  clean trace RMS = 0.09894, added noise RMS = 0.01487 (15% of signal)
  measured SNR = 16.46 dB
```

The amplitudes at the picks are proportional to the reflection coefficients,
as convolution with a zero-phase wavelet requires, and the sign is preserved.
The 16.46 dB signal-to-noise ratio is the *measured* ratio of the two
variances, not the value requested, which is the habit to keep: a synthetic
test is only useful if its inputs are measured rather than assumed.

The Ricker wavelet is worth writing down, because its shape explains the
filter behaviour later:

$$w(t) = \left(1 - 2\pi^2 f^2 t^2\right) e^{-\pi^2 f^2 t^2} . \tag{1}$$

It is the second derivative of a Gaussian, has zero mean — so it does not
change the DC level of anything it is convolved with — and its amplitude
spectrum peaks at $f$ and falls off as $f^2 e^{-f^2}$ at high frequency. At
$f = 32$ Hz there is almost nothing above 100 Hz, which sets the scale against
which the filters of §2 are judged.

## 2. Filter design and verification

The standard specification for a low-pass filter has three numbers: a passband
edge, a stopband edge and an attenuation. `scipy.signal.butter` designs a
Butterworth filter, which is **maximally flat in the passband** — no ripple —
at the cost of a gentler transition than a Chebyshev or elliptic filter of the
same order.

```
     order  -3 dB point (Hz)   |H| at 40 Hz  |H| at 100 Hz (dB)  |H| at 200 Hz (dB)
         2           39.9933       0.707107              -18.14              -43.15
         4           39.9933       0.707107              -36.14              -86.30
         6           39.9933       0.707107              -54.21             -129.44
```

Three things to read off this table.

- **The cut-off is exact.** The −3 dB point is at 39.9933 Hz, which is
  40 Hz to the resolution of the response grid. This is the bilinear
  transform's frequency pre-warping at work: the design maps the digital
  frequency axis so that the requested edge lands exactly on −3 dB.
- **The stopband steepens by 6 dB per octave per order.** 18.14, 36.14 and
  54.21 dB at 100 Hz for orders 2, 4 and 6. The asymptotic Butterworth
  magnitude is $|H|^2 = 1/(1 + (f/f_c)^{2N})$, which is 6 dB per octave per
  order.
- **The numbers are *steeper* than $20N\log_{10}(100/40)$ predicts** — 16.0,
  31.8 and 47.8 dB — because warping maps 100 Hz to
  $\tan(\pi\cdot100/500)/\tan(\pi\cdot40/500) = 2.829$ times the cut-off
  rather than $100/40 = 2.5$. **A digital filter's response is not the
  analogue prototype's response re-labelled, and the difference is
  measurable.**

Verification is the part that matters. The demo calls `sosfreqz` and reads the
magnitude response, so the specification is checked against the object that
will actually be applied. A design that is never verified is a hope.

> **Design in second-order sections.** `butter(..., output='sos')` returns a
> list of biquad coefficients, and `sosfilt`/`sosfiltfilt` apply them in
> series. The `b, a` (transfer-function) form of a high-order filter loses
> precision in the polynomial coefficients and can produce a filter that
> diverges where the second-order-section form is stable. Use `sos` for
> anything above order 2.

## 3. Group delay: what a causal filter costs

A causal filter has a transfer function $H(f) = |H(f)|e^{i\phi(f)}$. The
magnitude is the design specification; the **phase** is the price. The group
delay,

$$\tau_g(f) = -\frac{1}{2\pi}\frac{d\phi}{df}, \tag{2}$$

is the time by which a narrowband packet centred on $f$ is delayed. The demo
computes it from the designed response:

```
    group delay at    5 Hz =  10.252 ms
    group delay at   10 Hz =  10.489 ms
    group delay at   20 Hz =  11.734 ms
    group delay at   32 Hz =  15.344 ms
    group delay at   40 Hz =  15.342 ms
```

and measures the latency of the whole trace by cross-correlating the filtered
trace against the noise-free one:

```
    sosfilt (causal)           lag =  12.000 ms  RMS error vs noise-free = 0.154089
    sosfiltfilt (zero-phase)   lag =   0.000 ms  RMS error vs noise-free = 0.044165
    unfiltered input           lag =   0.000 ms  RMS error vs noise-free = 0.014826
```

**The measured 12.00 ms is neither 10.25 nor 15.34 ms.** It is the
amplitude-weighted average of the group delay over the signal's spectrum: the
Ricker's energy is concentrated near 32 Hz, where the delay is largest, but
the trace also has low-frequency content where the delay is smallest. This is
the reason a latency quoted from a cross-correlation must always be
accompanied by the spectral content it was measured on, and why "the filter
delays the trace by 12 ms" is a statement about *this* trace rather than about
the filter.

The residual column is the second cost. Zero-phase filtering leaves 0.0442 of
RMS residual against the causal filter's 0.1541, because it filters twice and
so attenuates the noise in the passband twice. The unfiltered trace's 0.0148
is the smallest only because the added noise is white and fills the passband;
against narrowband noise, filtering would win.

### 3.1 The beginning and the end of the trace

At the start of the record the true trace is exactly zero — the Ricker wavelet
and the first reflector are both later — and the two filters behave
completely differently:

```
      sample        true      causal    zero-phase
           0     0.00000    -0.00002      -0.01102
           1     0.00000    -0.00015      -0.00911
           2     0.00000    -0.00050      -0.00746
           8     0.00000    -0.00604      -0.00730
          16     0.00000    -0.00918      -0.00858
```

The causal output at sample 0 is $-0.00002$, essentially zero, because a
causal filter cannot report energy from an event 250 ms in its future. The
zero-phase output is already $-0.01102$, **1.38% of the trace peak**, because
the backward pass carried the reply to later events back to the start of the
record. That is the fingerprint of a non-causal operation, and §5 turns it
into a measurement.

## 4. Windows, leakage and scalloping

Any operation on a finite record implicitly multiplies it by a rectangular
window, whose transform is a sinc-like function with sidelobes only 13.26 dB
down. Those sidelobes are **leakage**: a strong tone smears across the whole
spectrum. Multiplying by a taper before transforming suppresses the
sidelobes, and the cost is a wider mainlobe:

```
    window           -6 dB width (bins) null-to-null (bins)  first sidelobe (dB)
    boxcar                        0.605               2.000               -13.26
    hann                          1.000               4.000               -31.47
    hamming                       0.906               4.000               -42.62
    blackman                      1.148               6.000               -58.11
    kaiser(beta=8)                1.109               5.469               -58.69
    kaiser(beta=14)               1.438               9.133              -105.95
```

The measured first-sidelobe levels reproduce the textbook values — −13.26 dB
for a rectangle, −31.47 dB for Hann, −42.62 dB for Hamming — which is a check
that the widths and levels are being measured correctly. Two properties are
worth knowing beyond the table:

- **Hamming's first sidelobe is low but its far sidelobes fall off slowly**
  (about 20 dB per decade), so a strong out-of-band tone can still appear far
  away in the spectrum. Hann falls off faster (about 60 dB per decade) at the
  cost of a higher first sidelobe.
- **Kaiser offers a single knob.** $\beta$ sets the trade-off continuously;
  $\beta = 8$ matches Blackman's sidelobe level with a slightly narrower
  mainlobe, and $\beta = 14$ reaches −105.95 dB at the cost of a mainlobe
  2.4 times wider than Hann's. When you need to hit a specification rather
  than a name, use `kaiser_beta`/`kaiserord` to solve for $\beta$.

### 4.1 Amplitude recovery and scalloping loss

Dividing a windowed spectral peak by the **coherent gain** — the sum of the
window — recovers the tone's amplitude. Measured on a monochromatic signal
placed exactly on a bin and then half a bin off it:

```
    window            on-bin amplitude     error  half-bin amplitude  loss (dB)
    boxcar                    1.000000  2.22e-16            0.645881     -3.797
    hann                      1.000000  4.44e-16            0.848835     -1.424
    hamming                   1.000000  4.44e-16            0.818752     -1.737
    blackman                  1.000000  4.44e-16            0.881166     -1.099
    kaiser(beta=8)            1.000018  1.77e-05            0.872829     -1.181
```

Two results that between them dispose of most folklore:

- **On a bin, every window recovers the amplitude exactly** — to $4\times
  10^{-16}$ for the common ones. No window is more "accurate" than another
  once the coherent gain is divided out. The choice of window is about
  leakage, not about amplitude.
- **Half a bin off, the peak amplitude falls by 3.797 dB under a boxcar and
  only 1.424 dB under Hann.** This is **scalloping loss**: an off-bin tone's
  energy splits between two bins and the peak of the discrete spectrum
  understates it. The rectangular window has the worst scalloping loss of any
  window, and the flat-topped windows invented for calibration work exist
  purely to keep it under 0.1 dB.

The practical rule: **report the parameters of the window and the bin offset
whenever a spectral amplitude is quoted**, because a 3.8 dB error from
scalloping is larger than most of the effects being studied.

## 5. Why zero-phase filtering cannot run in real time

`filtfilt` (and `sosfiltfilt`) filters the record forwards, reverses it,
filters again, and reverses back. The composition of the forward filter with
its reverse has a real, non-negative transfer function: zero phase. The price
is that **the output at time $t$ depends on input at times greater than $t$**,
which is the definition of non-causality.

The demo proves it rather than asserting it, with a truncation test: filter
the full 2.5 s record, then filter only its first 1.0 s, and compare the two
answers over the part both runs share.

```
    filter                        max |difference|  at sample  time (s)
    sosfilt (causal)                     0.000e+00          0     0.000
    sosfiltfilt (zero-phase)             8.416e-03        499     0.998
```

The causal output is **bit-identical** — a difference of exactly zero — because
its value at time $t$ is a function of $x(t')$ for $t' \le t$ alone. The
zero-phase output differs by up to $8.4\times10^{-3}$, 1.05% of the trace peak,
and the first sample where the two differ by more than $10^{-9}$ is sample 347,
which is 153 samples before the truncation. That is the **look-ahead** the
backward pass requires at a 20 Hz cut-off.

So the trade is exact and quantitative:

| | Causality | Latency | Phase | Extra noise suppression |
|---|---|---|---|---|
| `sosfilt` | yes | group delay, 10–15 ms here | non-linear | 1× |
| `sosfiltfilt` | **no** | 0 | zero | 2× |

Zero-phase is the right choice when the whole record is available: a
reflection-seismic processing flow, a catalogue of past events, a lab
measurement, a reanalysis. It is the wrong choice — not worse, *invalid* —
when the answer is needed at the time the data arrive: an earthquake
early-warning filter, a shipboard real-time display, a feedback control loop.
A causal filter with a known few-millisecond delay is the only admissible
option there, and its phase distortion is the price of being allowed to
answer at all.

## 6. Spectral estimation: `spectrogram` and `welch`

The Fourier transform of a whole record gives the average spectrum over the
record. `spectrogram` gives the spectrum as a function of time, and the trade
is unavoidable: with `nperseg` samples per slice, the frequency resolution is
$f_s/\text{nperseg}$ and the time resolution is `nperseg`$\,\cdot\,dt$, and
their product is fixed.

On a linear chirp from 8 to 64 Hz over 2.56 s with 128-sample slices:

```
     time (s)  instantaneous f (Hz)   spectrogram peak (Hz)  error (Hz)
        0.256                13.600                  11.719      -1.881
        0.768                24.800                  23.438      -1.363
        1.280                36.000                  35.156      -0.844
        1.792                47.200                  46.875      -0.325
        2.304                58.400                  58.594       0.194
```

The frequency resolution is 3.906 Hz and the errors stay inside half a bin
(1.95 Hz) — but they are **systematically negative early and positive late**.
That is not noise and not a bug: each slice reports the average frequency over
its 0.256 s window, and a rising chirp spends most of that window below its
instantaneous frequency at the slice centre. The sign of the bias is a
prediction of the method, and seeing it in the output is the evidence that
the method is understood.

`welch` is the average of the periodograms of overlapping windowed segments —
a lower-variance, higher-bias estimate of the power spectral density. Its
normalisation is the thing to check, and Parseval's theorem is the check:

```
    sum(Pxx) * df = 0.582609
    var(x)        = 0.565053   (mean of x = 1.882e-03)
    ratio         = 1.031069  (+3.11%)
    The same test on a stationary white record gives 0.989781 (-1.02%)
```

The one-sided PSD integrates to the variance of the record to 3.1% for the
chirp and 1.0% for stationary noise. The residual is the price of averaging
windowed, overlapping segments — and it is smaller when the signal is
stationary, which is exactly Welch's assumption.

> **`sum(Pxx) * df ≈ var(x)` is the one-line test that catches the most common
> error in spectral analysis**: a factor-of-two mistake between one-sided and
> two-sided PSDs, or between amplitude and power spectra. Run it every time
> you use a new PSD routine.

## Worked code

The whole chain, from trace to filtered trace to spectrum, with the four
arguments that carry the choices:

```python
import numpy as np
from scipy import signal

fs = 500.0
t = np.arange(1250) / fs
x = ...                                    # the trace

# 1. design, in second-order sections, to a stated specification
sos = signal.butter(4, 40.0, btype="low", fs=fs, output="sos")

# 2. verify the specification before applying it
f, h = signal.sosfreqz(sos, worN=2 ** 14, fs=fs)
print("|H| at 100 Hz = %.2f dB" % (20 * np.log10(abs(np.interp(100.0, f, abs(h))))))

# 3. apply causally, or with zero phase -- decide which, and say why
y_causal = signal.sosfilt(sos, x)
y_zero = signal.sosfiltfilt(sos, x)

# 4. group delay: the price of causality, at the signal's dominant frequency
ph = np.unwrap(np.angle(signal.sosfreqz(sos, worN=2 ** 16, fs=fs)[1]))
fq = np.linspace(0.0, fs / 2, ph.size)
tau_g = -np.gradient(ph, fq) / (2 * np.pi)
print("group delay at 32 Hz = %.2f ms" % (1e3 * np.interp(32.0, fq, tau_g)))

# 5. a spectrogram whose resolution you chose deliberately
f_s, t_s, S = signal.spectrogram(x, fs=fs, window="hann",
                                 nperseg=128, noverlap=96, mode="magnitude")

# 6. a PSD whose normalisation you verified
f_w, Pxx = signal.welch(x, fs=fs, nperseg=512, noverlap=256, window="hann")
df = f_w[1] - f_w[0]
print("Parseval ratio = %.4f" % (Pxx.sum() * df / np.var(x)))
```

Step 2 and step 6 are the two that are usually skipped and should not be.

## Physical interpretation

A filter is a model of the recording system. The Butterworth low-pass of §2
is the standard stand-in for a geophone's or a hydrophone's response — an
instrument that passes the band of interest and rolls off outside it — and
the group delay of §3 is a real, measurable delay in a real acquisition
system. When a cross-hole tomographic arrival time is picked to 0.5 ms and the
anti-alias filter has a 12 ms group delay, the delay must be removed
before the travel time means anything; that removal is why
`scipy.signal.group_delay` exists as a function rather than a formula in a
textbook.

The window trade of §4 is the seismic resolution trade in a different
costume. The mainlobe width is the length of the wavelet you can distinguish,
and the sidelobe level is the "ringing" that leaks a strong reflector's energy
into the neighbouring trace — in map form, the acquisition footprint. A
processing sequence that tapers hard to remove the footprint also smears the
fault.

The causality test of §5 is the clearest case in this module of a
mathematical property with an engineering consequence. The forward–backward
filter is a non-causal operator; a non-causal operator needs the future; the
future is not available at run time. No amount of implementation effort
changes that, and the truncation test measures exactly how much future the
filter needs — 153 samples, 0.31 s, at a 20 Hz cut-off.

## Assumptions and limits

- **The Butterworth design assumes the sample rate is known and correct.**
  `fs` is not decoration: passing a normalised frequency where an `fs` is
  expected gives a filter at the wrong cut-off and no error.
- **`butter` in `b, a` form is numerically fragile above order 4–6.** Use
  `output='sos'` and the `sosfilt` family. (§2)
- **Group delay is a narrowband concept.** It describes the delay of a packet
  whose bandwidth is small compared with the filter's transition; applying it
  to a broadband arrival is an approximation, and §3 measures the size of the
  error (12 ms measured against 10.25 and 15.34 ms at the band edges).
- **`sosfiltfilt` assumes the record is long compared with the filter's
  impulse response.** Its default pad length is estimated from the filter
  order; a record of a few hundred samples filtered at 2 Hz will be dominated
  by edge effects.
- **`spectrogram` assumes the signal is stationary within each slice.** The
  systematic bias measured in §6 is the size of the error that assumption
  introduces for a chirp.
- **`welch` assumes stationarity across segments**, and returns a biased
  estimate whose bias is set by the window's mainlobe width. The Parseval test
  checks the *normalisation*, not the bias.
- **Power spectral density has units of power per hertz.** A "PSD"
  computed with `scaling='spectrum'` has units of power, and the two differ by
  a factor of the equivalent noise bandwidth. Mixing them up is the
  factor-of-two error that §6's test catches.

## Python demonstration

[`code/signal_demo.py`](./code/signal_demo.py) prints all the tables above.
The experiments that teach the most:

- Change the Butterworth order in §2 to 8 and re-verify with `sosfreqz`. The
  stopband improves and the group delay at 5 Hz grows; then compare the
  `b, a` form with the `sos` form of the same design and watch the
  transfer-function form oscillate.
- Move the filter's cut-off from 20 Hz to 5 Hz in §5 and re-measure the
  look-ahead. It grows roughly as $1/f_c$: a longer impulse response needs
  more future.
- Replace the Ricker wavelet with a zero-phase Klauder wavelet (a linear
  sweep's autocorrelation) and re-run §3. The residual after zero-phase
  filtering changes, and the cross-correlation lag of the causal filter
  moves, because the spectrum moved.
- Set `nperseg=64` in §6 and re-read the spectrogram table. The frequency
  errors become twice as large and the bias becomes more visible: that is the
  time–frequency trade being spent in one direction.
- Replace the white noise in §1 with narrowband noise (filter the noise with
  the same `sos`) and re-run the residual table. Now filtering *does* beat the
  unfiltered trace, and the comparison becomes the one you would make on real
  data.

## Common mistakes

- **Designing in `b, a` form for high orders.** Use `sos`. (§2)
- **Never verifying the response.** `sosfreqz` is one call; a design without a
  verification is a guess. (§2)
- **Filtering with `filtfilt` in a real-time pipeline.** Not worse — invalid.
  (§5)
- **Reporting a cross-correlation lag as "the filter's delay".** It is the
  delay of this trace through this filter; quote the spectrum it was measured
  on. (§3)
- **Using a boxcar window for a spectral estimate because "it does not distort
  the data".** It has the worst leakage and the worst scalloping loss of any
  window. (§4)
- **Comparing a spectral amplitude across two windows** without dividing by
  the coherent gain. On-bin amplitudes are identical across windows *after*
  the correction and differ by up to 30% before it. (§4.1)
- **Trusting a PSD's normalisation because the shape looks right.** Run the
  Parseval test. (§6)
- **Reading a spectrogram's peak frequency as the instantaneous frequency.**
  It is the window average, biased in a direction you can predict. (§6)
- **Assuming `filtfilt`'s output is "the filtered data".** It is the
  filtered data with a non-physical phase spectrum; deconvolution and
  inversion built on it inherit that.

## Real-world applications

- **Reflection seismics.** Band-pass filtering, spectral balancing and
  deconvolution are all statements about the trace's spectrum; the
  zero-phase assumption underpins wavelet estimation and the tie to well logs.
- **Earthquake early warning.** The filter is causal by necessity; the
  latency budget is a design constraint measured in the same milliseconds as
  §3.
- **Instrument response removal.** A seismometer's response is a filter, and
  its deconvolution requires the phase — which is why the response file is a
  full complex spectrum and not just a magnitude.
- **Ambient-noise tomography.** Cross-correlations of long noise records,
  combined with spectral whitening, produce the empirical Green's functions
  used for imaging; the windowing and normalisation choices of §4 and §6 are
  the standard processing parameters.
- **Tide and gravity analysis.** Tidal constituents are extracted by
  least-squares fitting in the frequency domain; leakage between constituents
  is a windowing problem, and the Rayleigh criterion is a mainlobe-width
  statement.
- **Potential-field filtering.** Upward continuation, derivative and
  matched-filter operations are all frequency-domain operators, and their
  design is the same design problem as §2 with a different specification.

## Further reading

- **Oppenheim, A. V., & Schafer, R. W. *Discrete-Time Signal Processing*
  (3rd ed., Pearson, 2010).** The definitive treatment of filter design,
  group delay, window functions and the discrete Fourier transform. Chapters
  5–7 and 10 are the ones this lesson uses. Level: advanced.
- **Kanasewich, E. R. *Time Sequence Analysis in Geophysics* (University of
  Alberta Press, 1981).** The classic geophysical treatment, with the
  filter design, windowing and spectral estimation conventions in the form
  the exploration industry uses them. Level: graduate.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** The seismological role of the source wavelet,
  the instrument response and the filtering that connects them. Level:
  graduate.
- **Shearer, P. M. *Introduction to Seismology* (3rd ed., Cambridge University
  Press, 2019).** Filtering and spectral analysis in the context of the
  observations they are applied to. Level: intermediate to graduate.
- **Harris, F. J. "On the use of windows for harmonic analysis with the
  discrete Fourier transform," *Proceedings of the IEEE*, 1978.** The
  reference table of window mainlobe widths and sidelobe levels that §4
  reproduces numerically. Level: advanced.
- **Proakis, J. G., & Manolakis, D. G. *Digital Signal Processing: Principles,
  Algorithms and Applications* (4th ed., Pearson, 2007).** A more
  accessible route to the same material than Oppenheim & Schafer. Level:
  intermediate.

> Note on citations: bibliographic details are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text;
> confirm editions and availability through your library before citing them
> yourself.

## Related lessons

- [01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — §3.3 on `numpy.fft` against `scipy.fft`.
- [04 scipy.interpolate](./04-interpolate.md) §5 — resampling, which is
  interpolation plus the anti-alias filter of §2.
- [06 scipy.sparse](./06-sparse.md) §5 — the implicit time step that a
  recursive filter's difference equation becomes in a full 3-D problem.
- [07 scipy.ndimage and scipy.linalg](./07-ndimage-linalg.md) §3 — 2-D
  filtering of grids, which is the same theory with a spatial kernel.
- [01-10-05 Windowing and Aliasing](../../01-mathematics/10-fourier-analysis/05-windowing-aliasing.md)
  — the mathematics behind §4.
- [01-11-05 The z-Transform](../../01-mathematics/11-complex-analysis/05-z-transform.md)
  — poles, zeros and the stability of a recursive filter.
- [20-signal-processing](../../20-signal-processing/README.md) — the folder
  that applies this material to seismic and other geophysical series.
- [06-seismology](../../06-seismology/README.md) — where the synthetic
  seismogram of §1 becomes a real record.

Exercises:
[`exercises/05-signal-exercises.md`](./exercises/05-signal-exercises.md)
and
[`exercises/05-signal-solutions.md`](./exercises/05-signal-solutions.md).

## Self-assessment checklist

- [ ] I can state the Ricker wavelet's formula and its spectrum's peak.
      (§1)
- [ ] I can design a Butterworth filter to a specification and verify the
      −3 dB point and one stopband value. (§2)
- [ ] I can explain the pre-warping that makes the digital cut-off exact.
      (§2)
- [ ] I can compute a group delay from a phase spectrum. (§3)
- [ ] I can measure a latency by cross-correlation and explain why it differs
      from the group delay. (§3)
- [ ] I can prove that `filtfilt` is non-causal, and state the look-ahead in
      samples. (§5)
- [ ] I can choose a window from its mainlobe width and sidelobe level. (§4)
- [ ] I can state the scalloping loss of a boxcar and of a Hann window. (§4.1)
- [ ] I can predict the sign of a spectrogram's frequency bias on a rising
      chirp. (§6)
- [ ] I can verify a PSD normalisation with Parseval's theorem. (§6)
