---
id: 20-02-03
title: "Window Functions and Spectral Leakage Control"
level: advanced
prereqs: ["20-02-01", "20-02-02", "01-10-05"]
tags: [signal-processing, windows, leakage, enbw, scalloping, kaiser]
---

# Window Functions and Spectral Leakage Control

Truncating a record is multiplying it by a rectangular window, and multiplication
in time is convolution in frequency: every spectral feature is smeared by the
rectangular window's kernel, whose sidelobes decay slowly and reach only
$-13\ \mathrm{dB}$. Windowing replaces that kernel with a better one, and the
price is always paid in resolution. This lesson tabulates the metrics that make
the choice explicit, derives the exact equivalent noise bandwidth of the
cosine-sum windows, and measures the resolution, leakage and amplitude-accuracy
consequences of each choice.

**All models and data in this module are SYNTHETIC.** Every metric below is
computed from the window that `scipy.signal.windows` builds, by zero-padded DTFT,
so each number is reproducible rather than quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define and compute** the five metrics that decide a window: coherent gain,
   equivalent noise bandwidth (ENBW), highest sidelobe level, sidelobe decay, and
   scalloping loss.
2. **Derive** the ENBW of a cosine-sum window and **verify** the classical values
   $1.5$ (Hann), $1.3628$ (Hamming) and $1.7269$ (Blackman).
3. **Explain** why the resolution of two tones is set by the main lobe, and
   **measure** the separation at which the dip reaches $-3\ \mathrm{dB}$.
4. **Quantify** the leakage-limited detection of a weak tone beside a strong one,
   and convert a measured leakage floor into the weakest detectable amplitude.
5. **Use** the Kaiser family's single parameter to move along the
   sidelobe-versus-ENBW trade, and **state** the value that meets a specification.
6. **Choose** between a resolving window and a flat-top window for amplitude
   measurement, and **state** the cost of each.
7. **Report** a spectral estimate with the window, the ENBW and the scalloping
   loss, so that it can be reproduced.

## Prerequisites

- [20-02-01 Practical DFT/FFT](01-dft-fft-practice.md) — leakage, scalloping and
  the Dirichlet kernel.
- [20-02-02 Spectral Estimation](02-spectral-estimation.md) — the bias that the
  window shape controls.
- [01-10-05 Sampling, Aliasing, Leakage and Windowing](../../01-mathematics/10-fourier-analysis/05-windowing-aliasing.md) —
  the mathematical treatment of truncation.

## 1. Intuition: a window is a spectral kernel you chose

A finite record is a longer signal times a taper. In the frequency domain the
measured spectrum is the true spectrum **convolved with the taper's transform**.
Choosing a window is therefore choosing the kernel: how wide the main lobe is
(resolution) and how fast the sidelobes decay (leakage, and hence how far a
strong feature spoils a weak one nearby).

Three statements worth holding on to:

- **The main lobe costs resolution; the sidelobes cost dynamic range.**
- **A window cannot reduce leakage to zero, only redistribute it.** Truncation is
  the cause; the window shapes the effect.
- **Nothing is free.** Every window except the rectangular one multiplies the
  spectrum's variance by the ratio ENBW/(window's coherent gain)². The
  rectangular window has the best variance and the worst leakage, and no window
  beats it on both.

## 2. The metrics, defined

For a window $w[n]$ of length $N$ with transform $W(f) = \sum_n w[n]e^{-i2\pi fn}$:

| metric | definition | what it controls |
|---|---|---|
| coherent gain | $\frac1N\sum_n w[n]$ | the loss on a coherent (on-bin) tone |
| ENBW | $\displaystyle N\frac{\sum_n w^{2}[n]}{\left(\sum_n w[n]\right)^{2}}$ (in bins) | the variance penalty and the noise bandwidth |
| highest sidelobe | $\max_{\lvert f\rvert > f_{\text{null}}}\lvert W(f)/W(0)\rvert$ | the worst-case leakage from a strong tone |
| sidelobe decay | the envelope slope beyond the near sidelobes | how fast leakage dies with distance |
| scalloping loss | $\min_{0\le\delta\le1/2}\lvert W(\delta)/W(0)\rvert$ | the worst-case amplitude error for an off-bin tone |
| worst-case process loss | coherent gain $\times$ scalloping | the total amplitude error, before any correction |

**Why the ENBW is the variance currency.** For white noise, a windowed
periodogram bin has

$$\operatorname{Var} = \frac{S^{2}}{N}\cdot\text{ENBW}(\text{in bins}),$$

so a window with $\mathrm{ENBW} = 1.5$ costs $50\%$ more variance than the
rectangular window. Every improvement in leakage is bought with that factor, and
stating ENBW is how the price is declared.

## 3. The measured metric table

Measured at $N = 1024$ by zero-padded DTFT (`NPAD` $= 2^{18}$), bandwidths in
bins of $1/N$:

| window | coherent gain | ENBW (bins) | highest sidelobe (dB) | sidelobe at 10 bins (dB) | scalloping (dB) | 3 dB BW (bins) | 6 dB BW (bins) |
|---|---|---|---|---|---|---|---|
| rectangular | 1.000000 | 1.0000 | $-13.26$ | $-29.49$ | $-3.92$ | 0.438 | 0.609 |
| Hann | 0.500000 | 1.5000 | $-31.47$ | $-68.47$ | $-1.42$ | 0.719 | 1.000 |
| Hamming | 0.540000 | 1.3628 | $-42.67$ | $-46.66$ | $-1.75$ | 0.656 | 0.906 |
| Blackman | 0.420000 | 1.7268 | $-58.11$ | $-76.38$ | $-1.10$ | 0.828 | 1.156 |
| Kaiser $\beta = 8.6$ | 0.420800 | 1.7214 | $-63.26$ | $-78.83$ | $-1.11$ | 0.812 | 1.141 |
| flat-top | 0.215579 | 3.7702 | $-93.01$ | $-103.04$ | $-0.01$ | 1.859 | 2.297 |

Worst-case process loss (coherent gain × scalloping):

| window | process loss | dB |
|---|---|---|
| rectangular | 0.636620 | $-3.92$ |
| Hann | 0.424413 | $-7.44$ |
| Hamming | 0.441390 | $-7.10$ |
| Blackman | 0.370088 | $-8.63$ |
| Kaiser $\beta = 8.6$ | 0.370352 | $-8.63$ |
| flat-top | 0.215336 | $-13.34$ |

Read the table as three separate trades:

- **Hamming versus Hann.** Hamming has a lower first sidelobe ($-42.7$ against
  $-31.5\ \mathrm{dB}$) and a *smaller* ENBW, yet at 10 bins it is **worse**
  ($-46.7$ against $-68.5\ \mathrm{dB}$). Hann's sidelobes decay quickly because
  the window and its first derivative are continuous at the ends; Hamming's do not
  because the window is discontinuous ($0.08$ at the edges). A single "highest
  sidelobe" figure therefore does not describe leakage at a distance, which is
  precisely the regime that matters for a weak tone far from a strong one.
- **Blackman and Kaiser 8.6.** Both suppress the first sidelobe below
  $-58\ \mathrm{dB}$ and hold $-77$ to $-79\ \mathrm{dB}$ at 10 bins, at an ENBW
  cost of $1.72$ bins (against $1.36$ for Hamming).
- **Flat-top.** Scalloping $-0.01\ \mathrm{dB}$ — an amplitude can be read off a
  bin with $0.1\%$ accuracy — at an ENBW of $3.77$ bins and a process loss of
  $-13.34\ \mathrm{dB}$. It is a measurement instrument, not a resolving one.

## 4. Deriving the ENBW of a cosine-sum window

Write the Hann window as

$$w[n] = 0.5 - 0.5\cos\frac{2\pi n}{N}, \qquad n = 0,\dots,N-1 .$$

Its transform is a sum of the transforms of the three terms, i.e. a Dirichlet
kernel centred at $f = 0$ with two half-weight kernels at $f = \pm1$ bin:

$$W(f) = 0.5\,D(f) + 0.25\,D(f - 1) + 0.25\,D(f + 1),
\qquad D(f) = \frac{\sin(\pi f)}{\sin(\pi f/N)}\times N/N .$$

For the ENBW, use the Parseval pair in the time domain instead — it is exact and
shorter. With $\sum_n w[n] = N/2$ for Hann and

$$\sum_{n=0}^{N-1}\left(0.5-0.5\cos\frac{2\pi n}{N}\right)^{2}
= 0.25N + 0.125N = 0.375N,$$

$$\mathrm{ENBW} = N\frac{0.375N}{(0.5N)^{2}} = \frac{0.375}{0.25} = 1.5\ \text{exact}.$$

For Hamming $w = 0.54 - 0.46\cos(2\pi n/N)$:
$\sum w = 0.54N$, $\sum w^{2} = (0.54^{2} + 0.46^{2}/2)N = (0.2916+0.1058)N
= 0.3974N$, so

$$\mathrm{ENBW} = \frac{0.3974}{0.54^{2}} = 1.36283\ \text{exact},$$

against the measured $1.362826$ — agreement to seven digits, the residual being
the periodic (`sym=False`) window's one-sample difference. Blackman,
$a_0 - a_1\cos + a_2\cos2$ with $a = (0.42, 0.5, 0.08)$, gives

$$\mathrm{ENBW} = \frac{0.42^{2} + 0.5^{2}/2 + 0.08^{2}/2}{0.42^{2}}
= \frac{0.1764+0.125+0.0032}{0.1764} = 1.72676,$$

measured $1.726757$. The general rule for a cosine-sum window
$\sum_k a_k\cos(2\pi kn/N)$ is

$$\mathrm{ENBW} = \frac{\sum_k a_k^{2}/c_k}{\left(\sum_k a_k\right)^{2}}
\quad\text{with } c_0 = 1,\ c_k = 2 \text{ for } k\ge1 .$$

## 5. Resolution: measured on two tones

Resolution is a property of the **main lobe**. For two equal tones with random
relative phase, the phase-averaged spectrum is
$\lvert W(f-f_1)\rvert^{2} + \lvert W(f-f_2)\rvert^{2}$ — an exact construction
that removes the beat that makes an in-phase two-tone test phase-dependent.
Measuring the dip between the peaks:

| window | smallest separation with a $-3\ \mathrm{dB}$ dip | dip at a 2-bin separation |
|---|---|---|
| rectangular | 1.10 bins | deep |
| Hamming | 1.60 bins | $-8.81\ \mathrm{dB}$ |
| Hann | 1.75 bins | $-6.02\ \mathrm{dB}$ |
| Blackman | 2.00 bins | $-3.15\ \mathrm{dB}$ |
| Kaiser $\beta = 8.6$ | 2.00 bins | $-3.22\ \mathrm{dB}$ |
| flat-top | not reached below 4 bins | $-2.24\ \mathrm{dB}$ |

The ordering is the ordering of the 3-dB bandwidth column of Section 3
($0.438 < 0.656 < 0.719 < 0.828 < 0.812 < 1.859$ bins), with the Kaiser value
slightly out of order because its main lobe is not exactly scaled by ENBW. Two
consequences:

- **A resolution claim must name the window.** "0.1 Hz resolution" from a
  1024-sample record means different things for a rectangular and a Blackman
  window: the first resolves tones 1.1 bins apart, the second needs 2.0.
- **The rectangular window is not automatically wrong.** When the data are
  periodic in the record length and the tones are on bins, it is optimal — least
  variance, no process loss. It is only when the record is *not* periodic that its
  slow sidelobe decay does damage
  ([20-02-01 §8](01-dft-fft-practice.md)).

## 6. Leakage-limited detection, quantified

A strong off-bin tone at $20.0488\ \mathrm{Hz}$ (amplitude 1) in a 1024-sample
record, with the leakage envelope measured 20 bins away at $22.002\ \mathrm{Hz}$:

| window | leakage at the probe, relative to the peak | amplitude ratio (weak/strong) for a 3 dB detection |
|---|---|---|
| rectangular | $-35.9\ \mathrm{dB}$ | $2.27\times10^{-2}$ |
| Hann | $-88.9\ \mathrm{dB}$ | $5.06\times10^{-5}$ |
| Hamming | $-53.3\ \mathrm{dB}$ | $3.05\times10^{-3}$ |
| Blackman | $-96.5\ \mathrm{dB}$ | $2.11\times10^{-5}$ |
| Kaiser $\beta = 8.6$ | $-85.0\ \mathrm{dB}$ | $7.97\times10^{-5}$ |
| flat-top | $-94.3\ \mathrm{dB}$ | $2.72\times10^{-5}$ |

The "amplitude ratio" column is $\sqrt{2\times10^{\text{floor}/10}}$: the weak
tone's own peak must exceed twice the leakage power (a 3 dB margin), and the
amplitude ratio is the square root of that power ratio. Two orders of magnitude of
detectability separate the rectangular window from Blackman at the same
frequency — a factor of $1000$ in detectable amplitude — which is why the choice of
window is a detection decision, not a cosmetic one.

**A cross-check that keeps the table honest.** The Hamming window's measured
floor at 20 bins ($-53.3\ \mathrm{dB}$) is *worse* than Hann's ($-88.9\
\mathrm{dB}$) despite Hamming having the lower first sidelobe: the first sidelobe
is not where the leakage is at 20 bins. Any table that lists only one sidelobe
number invites exactly this mistake.

## 7. The Kaiser family: one parameter, one trade

Kaiser windows are $\propto I_0(\beta\sqrt{1-(2n/(N-1)-1)^{2}})$ with a single
shape parameter $\beta$; $\beta = 0$ is the rectangular window and larger $\beta$
trades ENBW for sidelobe suppression. Measured:

| $\beta$ | ENBW (bins) | highest sidelobe (dB) | scalloping (dB) | coherent gain |
|---|---|---|---|---|
| 0.0 | 1.0000 | $-13.26$ | $-3.92$ | 1.0000 |
| 3.0 | 1.1366 | $-23.73$ | $-2.50$ | 0.6842 |
| 6.0 | 1.4668 | $-43.80$ | $-1.51$ | 0.5000 |
| 8.6 | 1.7214 | $-63.26$ | $-1.11$ | 0.4208 |
| 12.0 | 2.0092 | $-89.89$ | $-0.82$ | 0.3579 |
| 16.0 | 2.3033 | $-122.16$ | $-0.63$ | 0.3108 |

The trade is monotone and measurable, and it is the reason the Kaiser family is
the default in filter design
([20-03-01](../03-digital-filtering/01-fir-filters.md)): a specification is
usually stated as "at least $X\ \mathrm{dB}$ of stopband attenuation", which fixes
$\beta$, and then the transition band fixes the length.
`scipy.signal.kaiserord` inverts that mapping.

**Worked inversion.** A specification asks for $-60\ \mathrm{dB}$ sidelobes.
From the table, $\beta = 8.6$ gives $-63.3\ \mathrm{dB}$ and $\beta = 6.0$ gives
$-43.8\ \mathrm{dB}$: interpolating, $\beta \approx 8.3$ meets it, at an ENBW of
about $1.70$ bins — a $70\%$ variance penalty over the rectangular window, and
about a $40\%$ wider main lobe than Hann. Those are the numbers to quote when the
request is "just window it".

## 8. Worked examples

### Example 1 — is a peak real?

A periodogram of a 4096-sample record at $f_s = 250\ \mathrm{Hz}$ (a
$16.4\ \mathrm{s}$ record, $\Delta f = 0.061\ \mathrm{Hz}$) shows a peak at
$12.5\ \mathrm{Hz}$ that is 4 times the local level, with a rectangular window.
Neighbouring bins are at 2.1 and 1.8 times the local level.

- With a rectangular window the leakage from a strong component 20 bins away is
  only $-35.9\ \mathrm{dB}$ *if* the strong component is a clean off-bin tone; a
  4-to-1 ratio over neighbours is well inside the plausible leakage pattern of a
  single strong tone elsewhere in the band.
- The check that settles it: recompute with Hann. Measured leakage at 20 bins
  falls from $-35.9$ to $-88.9\ \mathrm{dB}$, a factor of $5\times10^{5}$ in
  power. A genuine spectral feature survives a change of window essentially
  unchanged; leakage does not.
- Report the result with the window, the ENBW (so the variance is stated) and
  the scalloping loss (so the amplitude uncertainty is stated).

### Example 2 — reading an amplitude from a bin

A synthetic calibration tone of true amplitude $1.000$ happens to fall half a bin
off. Reading the amplitude at the nearest DFT bin, $2\max\lvert X\rvert/\sum w$:

| offset (bins) | rectangular | Hann | flat-top |
|---|---|---|---|
| 0.00 | 1.000000 | 1.0000 | 1.000000 |
| 0.25 | 0.899626 | 0.9603 | 1.000263 |
| 0.50 | 0.636940 | 0.8488 | 0.998876 |

The rectangular window under-reads by $36\%$ in the worst case (the exact factor
$2/\pi = 0.636620$), Hann by $15\%$, and the flat-top by $0.11\%$. **If the
measurement is an amplitude, use a flat-top; if it is a detection or a
separation, use a resolving window.** The cost of the flat-top is visible in the
same table: its ENBW is $3.77$ bins, so its variance is $3.77\times$ the
rectangular window's and its resolution (Section 5) is worse than $4$ bins.

### Example 3 — the coherent gain as a calibration factor

A Hann-windowed amplitude spectrum must be divided by the coherent gain
$0.5$ before it means anything: a full-scale on-bin tone of amplitude 1 gives a
windowed peak of $0.5$ before correction, and $0.5$ is not a property of the
signal. The correction is exact for an on-bin tone and only approximate for an
off-bin one, where the scalloping factor multiplies it — which is why
"amplitude spectrum" without a stated window, coherent-gain correction and
scalloping budget is uninterpretable.

## 9. Units and dimensional analysis

| quantity | unit | check |
|---|---|---|
| coherent gain | dimensionless | mean of the window |
| ENBW | bins (equivalently Hz after multiplying by $\Delta f$) | a ratio of moments |
| highest sidelobe, scalloping | dB (a ratio) | $20\log_{10}$ of an amplitude ratio |
| process loss | dimensionless | a product of two dimensionless factors |
| resolution | Hz | main-lobe width × $\Delta f$ |

The ENBW is the only one that must be converted: an ENBW of $1.5$ bins at
$\Delta f = 0.061\ \mathrm{Hz}$ is $0.0915\ \mathrm{Hz}$ of noise bandwidth, and a
noise level quoted per bin is a different number from one quoted per hertz.
Convert and state which you mean.

## 10. Python demonstration

`code/windowing_advanced_demo.py` is print-only, single-process, uses `numpy`
and `scipy.signal`, and runs in under a second. It:

1. measures the seven metrics for six windows, including the sidelobe level at
   10 bins as a robust proxy for the decay rate;
2. checks the measured ENBW against the exact cosine-sum formula;
3. measures the leakage floor beside a strong off-bin tone and converts it to the
   weakest detectable amplitude;
4. measures the resolution of two equal tones by the phase-averaged dip;
5. sweeps the Kaiser $\beta$;
6. reads amplitudes at the nearest bin for an on-bin, quarter-bin and half-bin
   tone with three windows.

```bash
cd 20-signal-processing/02-fourier-and-spectral-analysis/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python windowing_advanced_demo.py
```

## 11. Assumptions and regime of validity

1. **The window is applied to the whole record or to each segment.** A window and
   Welch segmentation interact: the segment length must span several periods of
   the lowest frequency of interest, or the window *attenuates the signal* rather
   than shaping the kernel.
2. **The sidelobe tables assume a single dominant tone.** With many comparable
   components, leakage adds incoherently and the effective floor rises;
   the measured table is a best case.
3. **A window cannot recover resolution lost to truncation.** It can trade
   resolution for dynamic range, nothing more; only a longer record adds
   resolution.
4. **The main-lobe width scales as $1/N$ in bins, i.e. is constant in hertz** for
   a fixed window shape and duration. Doubling the record length halves the
   resolution in hertz at fixed ENBW.
5. **Overlap in Welch estimation must scale with the window.** A Hann window's
   effective overlap is 50–75 %; a Blackman window needs more, because its ends
   taper harder and more data are discarded.
6. **Scalloping corrections assume a single, well-separated tone.** With two
   tones within a main lobe, the peak is neither tone's amplitude.
7. **`sym=True` versus `sym=False` matters at the $10^{-3}$ level** in ENBW (the
   measured $1.362826$ against the exact $1.36283$) and matters absolutely when a
   window is used as a filter kernel, where the periodic version is the correct
   one ([20-03-01](../03-digital-filtering/01-fir-filters.md)).

## 12. Exercises

- [`exercises/03-windowing-advanced-exercises.md`](./exercises/03-windowing-advanced-exercises.md)
- [`exercises/03-windowing-advanced-solutions.md`](./exercises/03-windowing-advanced-solutions.md)

## 13. Common pitfalls

1. **Choosing a window by its first sidelobe alone.** Hamming's first sidelobe is
   $11\ \mathrm{dB}$ lower than Hann's, yet at 10 bins it leaks $22\ \mathrm{dB}$
   more.
2. **Forgetting the coherent gain.** A Hann-windowed amplitude is half the true
   amplitude until corrected.
3. **Quoting an amplitude from a single bin.** The worst-case scalloping loss is
   $-3.92\ \mathrm{dB}$ (rectangular) and $-1.42\ \mathrm{dB}$ (Hann).
4. **Claiming resolution without naming the window.** The measured
   $-3\ \mathrm{dB}$ two-tone separation ranges from 1.10 to more than 4 bins
   across the table.
5. **Using a flat-top to detect and a rectangular to measure.** The two windows
   have opposite strengths, as Examples 1 and 2 show.
6. **Assuming that windowing removes leakage.** It redistributes it; a
   $+60\ \mathrm{dB}$ tone still contaminates nearby bins, just with a floor of
   $-100\ \mathrm{dB}$ instead of $-13$.
7. **Forgetting ENBW when comparing noise levels.** Levels differ by the ENBW
   ratio, $1.5$ for Hann and $3.77$ for flat-top.

## 14. Mastery checkpoint

Without notes:

**(a)** Define ENBW in words and in a formula, and say what it costs.
**(b)** A record of 8192 samples at $f_s = 512\ \mathrm{Hz}$ is windowed with
Blackman. Give $\Delta f$, the 3-dB resolution in hertz, and the ENBW in hertz.
**(c)** Derive the ENBW of a Hann window from its definition and check it
numerically.
**(d)** Two tones of equal amplitude 3 bins apart must be separated with at least
a $10\ \mathrm{dB}$ dip. Which of the windows in the measured table can do it?
State the criterion you used.
**(e)** A strong tone 15 bins from a weak one must allow the weak tone at
$-60\ \mathrm{dB}$ to be detected. From the leakage floor table, which windows
qualify?
**(f)** An amplitude must be measured to $1\%$ for a tone at an unknown bin
offset. Which window, and what does it cost in resolution and variance?

Answers for (b), (d) and (f) are in the
[solutions](./exercises/03-windowing-advanced-solutions.md).

## 15. Related modules

- [20-02-01 Practical DFT/FFT](01-dft-fft-practice.md) — the Dirichlet kernel
  that a rectangular window produces, and the scalloping loss.
- [20-02-02 Spectral Estimation](02-spectral-estimation.md) — where ENBW enters
  the variance of a Welch or multitaper estimate.
- [20-02-05 Time–Frequency Analysis](05-time-frequency.md) — windows as
  time–frequency atoms, where their length is the free parameter.
- [20-03 Digital Filtering](../03-digital-filtering/README.md) — the same windows
  used as FIR filter designs, with the Kaiser parameter fixing the stopband.
- [01-10 Fourier Analysis and Spectral Methods](../../01-mathematics/10-fourier-analysis/README.md) —
  the underlying transform theory.
