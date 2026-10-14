# Exercises — 01-10-03 Convolution, Filtering and the Convolution Theorem

Attempt these **closed-book** before opening the
[solutions](./03-convolution-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Compute the discrete convolution $y = x * h$ by hand.

(a) $x = [1, 2, 3]$, $h = [1, 1]$
(b) $x = [1, 0, -1]$, $h = [1, 2, 1]$
(c) $x = [2, 2, 2, 2]$, $h = [\tfrac12, \tfrac12]$

For each, state the output length and explain what the filter does.

---

**★2.** A filter has impulse response $h = [\tfrac14, \tfrac12, \tfrac14]$.

(a) Show that its transfer function is real and non-negative at every frequency,
and write it in the form $\cos^2(\pi f\,dt)$.
(b) State whether this filter has spectral zeros, and where.
(c) Compare it with the 3-point boxcar $[\tfrac13,\tfrac13,\tfrac13]$ at
$f = 1/(4\,dt)$.

---

**★3.** State the convolution theorem for the convention used in this module,
and use it to write the transform of $h_1 * h_2 * h_3$ in terms of the individual
transforms. Explain in one sentence why this matters for cascaded instruments.

---

**★4.** A signal of 1000 samples is convolved with a filter of 201 samples
using an FFT with no padding.

(a) How long is the true linear convolution?
(b) How much of it is folded back into the record?
(c) State the minimum FFT length that avoids the problem.

---

## ★★ Applied

**★★5.** A moving average of $M$ samples is applied to a seismic trace with
white noise of RMS 12 µV and a signal of RMS 400 µV in the passband.

(a) Derive the transfer function of the moving average.
(b) Compute the output signal amplitude and the output noise RMS for $M = 16$, in
both cases evaluated *at frequencies where* $\lvert H\rvert \approx 1$.
(c) State the improvement in signal-to-noise ratio.
(d) A colleague reports a factor-of-16 improvement. Where is the error, and what
does the correct factor depend on?

---

**★★6.** The 5-point boxcar filter of the lesson has $\lvert H(50\ \mathrm{Hz})\rvert
= 2.6\times10^{-4}$ with $dt = 4$ ms, and its first exact zero is at
$f = 1/(5\,dt) = 50$ Hz.

(a) Explain why the measured value is not exactly zero.
(b) A subsequent processing step divides the spectrum by $\lvert H(f)\rvert$ over
the band 0–125 Hz. State what happens at 50 Hz and at 100 Hz (the second zero, if
you judge it to be one), and whether regularisation can help.
(c) Suggest a filter of the same length with no zeros and state the trade-off.

---

**★★7.** A seismometer has transfer function
$H(f) = 1/(1 + 2\pi i f\tau)$ with $\tau = 0.5$ s, as in the lesson.

(a) Compute $\lvert H\rvert$ and the phase at 0.1, 1 and 10 Hz.
(b) A ground motion of amplitude 1 mm at 1 Hz is recorded. What is the recorded
amplitude, and what fraction of the true amplitude must be restored?
(c) The noise above 20 Hz is white. Compute the noise gain at 20 Hz from the
naive inverse $1/H$, and compare it with the gain at 1 Hz.
(d) State the water level that would bound the gain to 100 at all frequencies,
using $\lvert H\rvert/(\lvert H\rvert^2+\epsilon^2)$.

---

**★★8.** A synthetic trace is $y = h * x + n$, where $h$ is a 20-sample
zero-phase wavelet with unit DC gain, $x$ is a spike series of amplitude 1, and
$n$ is noise of RMS 0.01 (1% of a unit-amplitude spike).

(a) With the noise absent, state the RMS error of the naive inverse.
(b) With the noise present, explain in two sentences why the naive inverse
performs badly.
(c) The lesson's table gives the best water level at $\epsilon = 10^{-2}$ for a
0.81% noise-to-signal ratio. If the noise were 0.1%, would you expect the optimal
$\epsilon$ to be larger or smaller? Justify your answer from the form of the
regularised division.

---

## ★★★ Research-oriented

**★★★9.** The lesson measures the noise gain of a regularised deconvolution:

| noise RMS | naive error | regularised error ($\epsilon = 10^{-2}$) |
|---|---|---|
| $10^{-4}$ | 0.012000 | 0.015299 |
| $10^{-3}$ | 0.120002 | 0.023347 |
| $10^{-2}$ | 1.200019 | 0.177893 |
| $3\times10^{-2}$ | 3.600057 | 0.531946 |

(a) Show that the naive error scales linearly with the noise level, and confirm
this from the table.
(b) The regularised error flattens as the noise grows: compute the ratio of the
regularised errors at $10^{-2}$ and $3\times10^{-2}$ and explain the value.
(c) At which noise level do the two methods cross? Estimate from the table.
(d) Using the supplied script
[`code/convolution_demo.py`](../code/convolution_demo.py), find the optimal water
level for noise RMS $3\times10^{-2}$ by scanning $\epsilon$. Report the best
$\epsilon$ and the resulting error, and compare with the value at
$\epsilon = 10^{-2}$.
(e) State the rule of thumb relating the optimal $\epsilon$ to the noise level
that your numbers support.

---

**★★★10.** A "brick-wall" band-pass filter keeps wavenumbers in
$[k_1, k_2]$ exactly and rejects everything else.

(a) Write its transfer function.
(b) Its impulse response is the difference of two sincs. Show that the
impulse response decays as $1/t$ for large $t$.
(c) Explain why a filter with a $1/t$ impulse response applied to a *short* record
is equivalent to a very long operator shared between the record and the padding.
(d) The Gibbs overshoot is 8.949% of a jump for a single edge. For a band-pass
with two edges, would you expect the overshoot at a step to be larger or smaller
than for a low-pass alone? Justify your reasoning in one paragraph, and say how
you would test it numerically with the supplied script.
