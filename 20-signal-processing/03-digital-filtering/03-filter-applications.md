---
id: 20-03-03
title: "Filter Selection for Geophysical Data"
level: advanced
prereqs: ["20-03-01", "20-03-02", "20-02-01"]
tags: [signal-processing, filtering, notch, bandpass, aliasing, decimation, snr, ground-roll]
---

# Filter Selection for Geophysical Data

## Learning objectives

By the end of this lesson you will be able to:

1. **Measure** the frequency content of a contaminated record and **identify**
   which bands carry signal and which carry interference.
2. **Choose** an ordered filter sequence — notch, band-pass, anti-alias — and
   **justify** the order from the spectrum.
3. **Derive** the alias frequency produced by decimation and **predict** it exactly
   from the sample rates.
4. **Quantify** the signal-to-noise ratio recovered by a filter chain, and
   **state** the metric used.
5. **Explain** why a metric can improve or worsen for reasons that have nothing to
   do with the filter, and **detect** that case.
6. **Design** a notch with a specified $-3$ dB bandwidth and place it so the
   signal band is untouched.

## Prerequisites

- [20-03-01 FIR Filter Design: Windows, Parks-McClellan, Least Squares](01-fir-filters.md) —
  the filters used here.
- [20-03-02 IIR Filter Design: Butterworth, Chebyshev, Elliptic](02-iir-filters.md) —
  the Butterworth band-pass and the IIR notch.
- [20-02-01 Practical DFT/FFT: Normalisation, Units and Pitfalls](../02-fourier-and-spectral-analysis/01-dft-fft-practice.md) —
  the spectrum used to choose the band.

## 1. Intuition: filtering is a decision, then a design

A recorded geophysical trace is a sum of things nobody separated at the
instrument: the signal of interest, a low-frequency surface wave, cultural
interference at fixed frequencies, and broadband noise. Filtering is the act of
declaring which of those you are willing to keep and which you are willing to
lose. That declaration should be made from a *measured spectrum*, not from habit.

In the synthetic record used throughout this lesson ($f_s = 500$ Hz, 8 s), the
measured band energies are:

| band (Hz) | fraction of total power (dB) |
|---|---|
| 0–5 | $-26.19$ |
| 5–15 | $-2.86$ |
| 15–30 | $-20.21$ |
| 30–60 | $-5.09$ |
| 60–90 | $-17.46$ |
| 90–250 | $-8.41$ |

The 5–15 Hz band is the ground roll, the 30–60 Hz band is the signal (a 45 Hz
Ricker wavelet train), and the 90–250 Hz band carries the 150 Hz power-line
harmonic plus broadband noise. **The bands overlap.** The 50 Hz line sits inside
the signal band, and the signal is broadband enough to touch the ground-roll
band's tail. That is why a single filter cannot separate them and a *sequence* is
needed.

All models and data in this module are SYNTHETIC. The record is built from
chosen components, not measured from a real survey or instrument.

## 2. Definitions

### 2.1 The signal-to-noise metric

Any filter comparison requires an explicit metric. Throughout this lesson the
**crude signal-to-noise ratio** is

$$\mathrm{SNR} = 10\log_{10}\frac{P_{30\text{--}60}}{P_{0\text{--}20}+P_{80\text{--}250}}
\quad\text{(dB)},$$

where $P_{a\text{--}b}$ is the power of the record in the band $a$–$b$ Hz. The
numerator is the band the signal occupies; the denominator is everything
attributed to interference. Because the 50 Hz line lies *inside* the numerator
band, this metric can be fooled — and watching it get fooled is the point of §4.

### 2.2 Notch quality factor

An IIR notch at $f_0$ is specified by its quality factor $Q$. The $-3$ dB
bandwidth is

$$B = \frac{f_0}{Q}.$$

For $f_0 = 50$ Hz and $Q = 30$, $B = 1.67$ Hz: narrow enough that the signal at
25–40 Hz is untouched.

### 2.3 Aliasing

If a continuous signal is sampled at $f_s$, every frequency $f$ is indistinguishable
from $f \pm k f_s$. If a record is decimated by an integer factor $D$, the new
sample rate is $f_s' = f_s/D$ and everything above $f_s'/2$ folds back:

$$f_{\text{alias}} = \left|f - k f_s'\right| \quad\text{for the integer } k
\text{ that puts the result in } [0, f_s'/2].$$

## 3. Derivations

### 3.1 Why filter before decimating

Decimation keeps every $D$-th sample. In the frequency domain that is a
compression of the spectrum by $D$: content at $f$ moves to $f \bmod f_s'$. The
new Nyquist is $f_s'/2$, so any energy between $f_s'/2$ and the old Nyquist lands
inside the new band, where it is **indistinguishable from genuine low-frequency
signal**. There is no post-hoc fix: once folded, the two are the same numbers.

The demo makes this exact rather than rhetorical. A pure 150 Hz tone sampled at
500 Hz, decimated by $D = 4$ to $f_s' = 125$ Hz, has predicted alias

$$f_{\text{alias}} = |150 - 125| = 25\ \text{Hz}.$$

The measured dominant frequency of the decimated record is **25.0 Hz**, with rms
0.707. With an 8th-order Butterworth anti-alias lowpass at $0.8\,f_s'/2 = 50$ Hz
applied first, the residual rms falls to **0.0033** and the dominant frequency is
no longer the tone. The anti-alias filter is not optional.

### 3.2 Why notch first

The 50 Hz line lies inside the signal band. A band-pass at 25–70 Hz passes it
along with the signal; a notch removes it with a 1.67 Hz-wide hole. So the order
is: notch the narrowband lines (they are few and known), then band-pass the
broadband content (the ground roll and the high-frequency noise), then anti-alias
and decimate if the record is to be reduced.

### 3.3 Why the anti-alias cutoff sits below the new Nyquist

It is tempting to place the anti-alias lowpass exactly at $f_s'/2$. That leaves no
transition band: a real filter reaches its specified attenuation only some distance
into the stopband, and any content in that transition interval folds. The demo
places the cutoff at $0.8\,f_s'/2 = 50$ Hz for $f_s' = 125$ Hz, which leaves
$62.5 - 50 = 12.5$ Hz for the roll-off to reach full attenuation before the fold
begins.

The cost is signal: everything between 50 and 62.5 Hz is attenuated more than
necessary, even though it would have been representable after decimation. The
trade is quantified by the filter's transition width. For an 8th-order Butterworth
the roll-off is $6M = 48$ dB per octave, so from 50 Hz to 62.5 Hz (a ratio of 1.25,
or 0.32 of an octave) the attenuation increases by about
$48 \times 0.32 = 15$ dB. That is rarely enough on its own; the demo's measured
residual rms of $0.0033$ at the end of the chain reflects the combined action of
the band-pass (which had already removed the 150 Hz tone) and the anti-alias stage.

The practical rule is the one the demo uses: **set the anti-alias cutoff at about
0.8 of the new Nyquist and choose the order so the stopband attenuation is reached
by the new Nyquist.** Both numbers are design inputs; neither can be defaulted.

## 4. The measurement, and how it can mislead



The demo applies the chain to the synthetic record and reports the crude SNR:

| stage | crude SNR (dB) |
|---|---|
| raw record | $-3.36$ |
| after notching 50 and 150 Hz | $-15.57$ |
| after notching **and** 25–70 Hz band-pass | $+21.65$ |

The middle row falls by 12 dB, and the reason is worth pausing on. The 50 Hz line
was *inside* the numerator band $P_{30\text{--}60}$, so it had been inflating the
apparent signal. Removing the line removes that inflation, and the metric reveals
how much of the "signal band" was interference. **The honest comparison is the
raw record against the fully filtered one: $-3.36 \to +21.65$ dB, a 25 dB
improvement.** The lesson is general: when a processing step makes a metric worse,
check whether the metric was measuring what you thought.

The band-resolved measurements tell the same story without the ambiguity:

| band (Hz) | raw (dB of total) | after notch | after notch + band-pass |
|---|---|---|---|
| 5–15 (ground roll) | $-2.86$ | — | $-28.13$ |
| 45–55 (50 Hz line) | $-5.27$ | $-21.00$ | — |
| 145–155 (150 Hz line) | $-12.40$ | $-26.09$ | — |
| 30–60 (signal) | $-5.09$ | — | $-1.63$ |

The notch removes 15.74 dB from the 45–55 Hz band and 13.69 dB from the 145–155 Hz
band; the band-pass removes 25 dB from the ground-roll band while keeping the
signal band as the dominant part of the record ($-1.63$ dB of the total power).

## 5. Worked example (SYNTHETIC)

A 1000 Hz-sampled seismic channel carries a 60 Hz reflection signal, a 12 Hz
ground roll, a 50 Hz power line, and must be decimated to 250 Hz.

1. **Decimation factor**: $D = 1000/250 = 4$. New Nyquist $= 125$ Hz.
2. **Anti-alias edge**: use a lowpass at $0.8 \times 125 = 100$ Hz. Choose order 8
   Butterworth. At 250 Hz and above (which would alias into 0–125 Hz) the
   attenuation is far beyond the $-$60 dB the demo achieved with a comparable
   design.
3. **Notch**: the 50 Hz line. Set $Q = 30$ so the $-3$ dB width is
   $50/30 = 1.67$ Hz. The notch removes 50 Hz without touching 60 Hz.
4. **Order of operations**: notch (narrowband, removes the line that the band-pass
   cannot reach), then lowpass (broadband anti-alias), then decimate by 4.
5. **Check the sign of the alias**: a 50 Hz line is *below* the new Nyquist
   (125 Hz), so it survives decimation unchanged at 50 Hz; it does not alias.
   A 300 Hz component would alias to $|300 - 2\times250| = 200$ Hz — still above
   125 Hz, so it would alias again to $|200-250| = 50$ Hz, exactly on top of the
   line. This is why the anti-alias stage must come before decimation and must
   remove everything above 125 Hz, not just the first alias zone.

Step 5 is the part that practice hides: aliasing is many-to-one, so a component
far above Nyquist can land on a frequency you care about after one or more folds.

## 6. Assumptions and regime of validity

1. **The interference is stationary or slowly varying.** A notch at 50 Hz assumes
   the line is at 50 Hz; mains frequency drifts, and a fixed notch widens the hole
   needed.
2. **The signal and interference bands are separable in frequency.** When they
   overlap (as the 50 Hz line overlaps the signal band here) only a notch, or a
   method that uses another dimension (f-k, polarisation, adaptive), can separate
   them — see [06](06-multichannel-filtering.md) and
   [05](05-adaptive-filtering.md).
3. **The filter is applied to a stationary window.** A filter designed for one
   band applied to a record whose content changes in time will over- or
   under-filter parts of it.
4. **Phase is handled.** A causal band-pass shifts the record by its group delay;
   the demo uses `filtfilt` (zero-phase) throughout, which doubles the effective
   order. If you use a causal filter, correct the timing before picking arrivals.
5. **The sample rate is high enough to begin with.** Filtering cannot recover
   content above the original Nyquist; it can only avoid adding new aliases.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| sample rate | $f_s$ | Hz | samples s$^{-1}$ |
| band edges | $f$ | Hz | |
| decimation factor | $D$ | dimensionless | $f_s' = f_s/D$ |
| alias frequency | $f_{\text{alias}}$ | Hz | $\|f - k f_s'\|$ |
| notch $Q$ | $Q$ | dimensionless | $f_0/B$ |
| bandwidth | $B$ | Hz | $f_0/Q$ |
| power ratio | SNR | dB | $10\log_{10}(P/P)$ |

The dimensional check that catches most mistakes is the alias formula: both $f$
and $k f_s'$ are in Hz, and the result must land in $[0, f_s'/2]$. If your alias
frequency is negative, take the absolute value; if it is above $f_s'/2$, you chose
the wrong $k$.

## 8. Python demonstration

`code/filter_applications_demo.py` builds the synthetic record, measures its band
energies, applies the notch and band-pass chain, and demonstrates the decimation
alias exactly. It is self-contained, seeded with
`np.random.default_rng(20261014)`, and exits 0. Run it with the command in the
[module README](README.md).

What to look for:

1. **section 2** — the band table; note the overlap between signal and
   interference bands.
2. **section 3** — the notch removes 15.74 dB from the 45–55 Hz band and nothing
   from the signal.
3. **section 4** — the crude SNR falls after notching, then rises after
   band-passing; read the explanation before concluding anything.
4. **section 5** — the 150 Hz tone becomes a 25.0 Hz tone with no anti-alias
   filter, and essentially vanishes with one.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-filter-applications-exercises.md`](exercises/03-filter-applications-exercises.md)
and
[`exercises/03-filter-applications-solutions.md`](exercises/03-filter-applications-solutions.md).

- **★** Compute the alias frequency of a 220 Hz tone decimated from 1000 Hz to
  200 Hz.
- **★★** Given the band table of §1, justify the order notch → band-pass →
  anti-alias → decimate in terms of where each contaminant lives.
- **★★** A colleague reports that notching *reduced* the SNR. Explain how the
  metric could produce that result and propose a metric that does not.
- **★★★** Design a chain that removes a 50 Hz line whose frequency drifts by
  $\pm 0.5$ Hz, and state the resolution cost.

## Mastery checkpoint

Complete this without notes:

> A 2000 Hz-sampled record contains a 90 Hz reflection signal, a 15 Hz ground
> roll, a 50 Hz line and its 100 Hz and 200 Hz harmonics, and must be decimated to
> 500 Hz. **(a)** Compute the new Nyquist and name the lowest frequency above it
> that would alias onto the 90 Hz signal. **(b)** State the ordered filter chain
> and the purpose of each stage. **(c)** Choose a notch $Q$ so the 90 Hz signal
> is untouched, and compute the resulting bandwidth. **(d)** Explain whether
> the 100 Hz harmonic aliases onto anything after decimation. **(e)** State the
> one assumption that would break the whole chain.

A worked version appears in the
[solutions](exercises/03-filter-applications-solutions.md).

## Common pitfalls

1. **Decimating without an anti-alias filter.** The demo's 150 Hz tone becomes a
   25 Hz tone. There is no way to tell it apart from signal afterwards.
2. **Band-passing before notching.** A band-pass passes the line that lies inside
   the band; notch first.
3. **Trusting one metric.** The crude SNR improved 25 dB overall but *fell* in the
   middle of the chain for a good reason.
4. **Forgetting the filter's delay.** A causal band-pass shifts picks; use
   zero-phase filtering or correct the shift.
5. **Choosing a notch by feel.** State $Q$ and the resulting bandwidth
   ($B = f_0/Q$), and check that the signal band lies outside it.

## Related modules

- [20-03-04 Phase Response, Zero-Phase Filtering and Distortion](04-phase-and-zero-phase.md) —
  the phase cost of the filters used here.
- [20-03-04 Deconvolution in the Presence of Noise](../04-deconvolution-and-inverse-filtering/04-deconvolution-noise.md) —
  what the noise left after filtering does to deconvolution.
- [20-05-04 Noise Reduction Strategies in Practice](../05-noise-and-random-signals/04-noise-reduction.md) —
  the wider menu of noise-reduction methods.
- [03-10-05 Preprocessing: Detrend, Taper, Filter, Decimate](../../03-scientific-computing/10-obspy-and-seismic-data/05-filtering-detrending.md) —
  the same operations in ObsPy.
- [06-09-02 Reflection Processing Flow: Deconvolution, NMO, Stack, Migration](../../06-seismology/09-reflection-seismology/02-processing-flow.md) —
  where filtering sits in a processing sequence.
