# Solutions — 01-10-03 Convolution, Filtering and the Convolution Theorem

> **Read this after attempting the exercises, not before.**
>
> All arithmetic below was computed. Values quoted from the supplied script are
> the values it printed.

---

## ★1 — Three discrete convolutions

**(a)** $x = [1,2,3]$, $h = [1,1]$:
$y = [1, 2+1, 3+2, 3] = \boxed{[1,3,5,3]}$, length $3+2-1 = 4$. The filter is a
two-point running sum: it does not preserve amplitude ($\lvert H(0)\rvert = 2$),
so it is a smoother with a gain of 2 at DC. At $f = 1/(2\,dt)$ its response is
$1 + e^{-i\pi} = 0$: a two-point boxcar is a *high-pass* filter in disguise as a
smoother.

**(b)** $x = [1,0,-1]$, $h = [1,2,1]$:
$y = [1, 2+0, 1+0-1, 0-2, -1] = \boxed{[1,2,0,-2,-1]}$, length 5. This is the
differentiating pair $[1,-1]$ *convolved* with the smoothing pair $[1,1]$:
smooth then difference. The output peaks are ±2, which is $\lvert H\rvert$ at the
input's dominant frequency $(1+2e^{-i\omega dt}+e^{-2i\omega dt})$.

**(c)** $x = [2,2,2,2]$, $h = [\tfrac12,\tfrac12]$:
$y = [1,2,2,2,1]$, $\boxed{[1,2,2,2,1]}$, length 5. A constant input gives a
constant output of 2 in the interior, with half-amplitude at the two ends: the
end samples are the "wrap-around" that a circular convolution would fold back to
the other end. This is the smallest possible illustration of why padding
matters.

---

## ★2 — The [1/4, 1/2, 1/4] filter

**(a)** With $\omega = 2\pi f$,

$$H(f) = \tfrac14 + \tfrac12e^{-i\omega dt} + \tfrac14e^{-2i\omega dt}
= e^{-i\omega dt}\left(\tfrac14e^{i\omega dt} + \tfrac12 + \tfrac14e^{-i\omega dt}\right)
= e^{-i\omega dt}\left(\tfrac12 + \tfrac12\cos\omega dt\right).$$

Since $1+\cos\theta = 2\cos^2(\theta/2)$,

$$H(f) = e^{-i\omega dt}\cos^2(\pi f\,dt).$$

This is real and non-negative apart from the linear phase ramp $e^{-i\omega dt}$,
which is the shift of one sample — the filter is symmetric about its centre
sample.

**(b)** It has exactly one zero, at $\cos(\pi f\,dt) = 0$, i.e.

$$f = \frac{1}{2\,dt},$$

the Nyquist frequency of the sampling. So this "smoother" annihilates the
Nyquist component of the data — a real and usually unwanted property.

**(c)** At $f = 1/(4\,dt)$:

$$\text{triangular: } \cos^2(\tfrac{\pi}{4}) = 0.5, \qquad
\text{boxcar 3: } \frac{\sin(3\pi/4)}{3\sin(\pi/4)} = \frac{0.7071}{3\times0.7071}
= 0.3333 .$$

So the tapered filter passes 50% at this frequency while the flat one passes 33%.
The taper is *less* aggressive at moderate frequencies and *more* aggressive at
Nyquist, where the boxcar passes $1/3$ and the tapered filter passes zero. **The
taper moves the rejection from the middle of the band to the very top of it**,
which is why it is preferred when the top of the band is noise.

---

## ★3 — The convolution theorem

$$\mathcal F\{x * h\} = X(f)\,H(f).$$

For a chain,

$$\mathcal F\{h_1*h_2*h_3\} = H_1(f)H_2(f)H_3(f),$$

by applying the theorem twice (associativity in the time domain becoming
multiplication in the frequency domain).

**Why it matters for cascaded instruments:** the transfer functions multiply, so
an amplitude-versus-frequency budget can be assembled by multiplying curves, and
a chain of instruments can be replaced by a single equivalent operator without
ever computing the intermediate time series. It also means that a *zero* in any
one factor is a zero in the product — a single notch anywhere in the chain
destroys that frequency irrecoverably, no matter how good the other elements are.

---

## ★4 — Padding arithmetic

**(a)** $N_x + N_h - 1 = 1000 + 201 - 1 = \boxed{1200}$ samples.

**(b)** The FFT length is 1000, so the 200 samples beyond 1000 are folded back to
the start of the record: samples 1000–1199 are added to samples 0–199. That is
$\boxed{200}$ samples of contamination — the entire length of the filter minus
one, which is the same statement as (a).

**(c)** The FFT length must be at least $N_x+N_h-1 = 1200$; since power-of-two
lengths are convenient, use $\boxed{2048}$.

---

## ★★5 — Noise averaging

**(a)** The moving average of $M$ samples has

$$h[n] = \frac{1}{M}\ \text{for } n = 0,\ldots,M-1, \qquad
H(f) = \frac{1}{M}\sum_{n=0}^{M-1}e^{-2\pi ifn\,dt}
= e^{-i\pi f(M-1)dt}\frac{\sin(\pi fM\,dt)}{M\sin(\pi f\,dt)} .$$

The magnitude is the Dirichlet kernel; it equals 1 at $f = 0$ and falls to its
first zero at $f = 1/(M\,dt)$.

**(b)** For a signal well inside the passband, $\lvert H\rvert \approx 1$:

$$A_{\text{out}} \approx 400\ \mu\mathrm{V}.$$

For white noise, the output variance is
$\sigma_{\text{in}}^2\sum_n h[n]^2 = \sigma_{\text{in}}^2 \cdot M \cdot (1/M)^2
= \sigma_{\text{in}}^2/M$, so

$$\sigma_{\text{out}} = \frac{12}{\sqrt{16}} = 3\ \mu\mathrm{V}.$$

**(c)** The signal-to-noise ratio goes from $400/12 = 33.3$ to $400/3 = 133.3$:
an improvement of $\sqrt{16} = \boxed{4}$.

**(d)** The colleague has confused the reduction in *power* (a factor $M = 16$)
with the reduction in *amplitude* (a factor $\sqrt{M} = 4$). The correct factor
depends on the noise spectrum: $1/\sqrt{M}$ holds only if the noise is white
across the passband of the average. If the noise is concentrated at low
frequency, where $\lvert H\rvert \approx 1$, averaging does almost nothing; if it
is concentrated near the first spectral zero of the filter, the noise is
attenuated far more than $1/\sqrt{M}$ — and so is whatever signal lives there.

---

## ★★6 — Zeros, and what happens when you divide by them

**(a)** The measured $2.6\times10^{-4}$ (rather than exactly zero) is a
combination of three effects: the filter is applied to a *finite* record whose
spectrum has been sampled at bin frequencies that do not coincide exactly with
50 Hz; round-off in the FFT accumulates; and the impulse response in the demo is
zero-padded, which slightly changes the effective filter. The lesson's own
analysis of the boxcar's zeros showed that when the sampled pulse contains
exactly $M$ samples of spacing $dt$ with $M\,dt = T$, the discrete sum cancels
*exactly* at $f = n/T$. The residual here is what remains when those conditions
are only approximately met.

**(b)** Dividing by $\lvert H(f)\rvert$:

- At 50 Hz the gain is $1/2.6\times10^{-4} \approx 3850$, so the noise at that
  frequency is amplified nearly four thousandfold. If the true $\lvert H\rvert$
  were exactly zero, the data there would contain no information at all and the
  division would be $0/0$ — amplifying pure round-off.
- At 100 Hz the boxcar's response is exactly zero ($f = 2/(M\,dt) = 100$ Hz),
  so **the information is destroyed**, not merely attenuated. No regularisation
  can recover it, because there is nothing to recover; the best a regularised
  inverse can do is decline to amplify, which is a silent admission that the
  band around 100 Hz has been lost.

**(c)** A filter of the same length with no zeros: replace the boxcar with a
Gaussian of matched width (the lesson's 9-point Gaussian has no zeros and its
response at 50 Hz is 0.16764, at 62.5 Hz 0.06262). The trade-off is that the
Gaussian rolls off earlier in the passband — 0.32110 at 40 Hz against 0.22656 for
the boxcar — so it attenuates wanted signal at moderate frequencies in exchange
for being invertible. Which is better depends on whether the data are to be
merely viewed or subsequently inverted.

---

## ★★7 — Instrument response and its inverse

**(a)** With $\lvert H\rvert = 1/\sqrt{1+(2\pi f\tau)^2}$ and phase
$-\arctan(2\pi f\tau)$, $\tau = 0.5$ s:

| $f$ (Hz) | $2\pi f\tau$ | $\lvert H\rvert$ | $1/\lvert H\rvert$ | phase (°) |
|---|---|---|---|---|
| 0.1 | 0.3142 | 0.954028 | 1.0482 | $-17.441$ |
| 1 | 3.1416 | 0.303314 | 3.2969 | $-72.343$ |
| 10 | 31.416 | 0.031815 | 31.4318 | $-88.177$ |
| (20) | 62.832 | 0.015913 | 62.8398 | $-89.088$ |

**(b)** The recorded amplitude at 1 Hz is
$1\,\mathrm{mm}\times0.303314 = \boxed{0.3033\ \mathrm{mm}}$, and the fraction to
be restored by the inverse is $1/0.303314 = 329.7\%$ of the recorded value (a
factor of 3.297).

**(c)** The naive inverse $\hat X = Y/H$ multiplies the noise by $1/\lvert H\rvert$:

$$\text{gain at 20 Hz} = 62.8398, \qquad \text{gain at 1 Hz} = 3.2969,$$

a ratio of about 19. So white noise becomes strongly coloured by the inverse —
the noise at 20 Hz is amplified 19 times more than the noise at 1 Hz. Absent a
prior on the noise's own spectrum, this is why instrument-corrected traces can
look far noisier than the raw ones without any error having been made.

**(d)** The gain function of the regularised inverse,
$g(\lvert H\rvert) = \lvert H\rvert/(\lvert H\rvert^2+\epsilon^2)$, has its maximum
at $\lvert H\rvert = \epsilon$, where $g = 1/(2\epsilon)$. Bounding the gain by
100 therefore requires

$$\frac{1}{2\epsilon} = 100 \qquad\Longrightarrow\qquad \epsilon = 0.005 .$$

Check: with $\epsilon = 0.005$, at the worst frequency present if the band ends
at 50 Hz ($\lvert H\rvert = 0.006366$),
$g = 0.006366/(0.006366^2+0.005^2) = 97.15 \le 100$ ✓. Because the bound
$1/(2\epsilon)$ is attained wherever $\lvert H\rvert$ passes through $\epsilon$,
the choice is independent of the band once $\epsilon$ exceeds the minimum
$\lvert H\rvert$ in the band — a useful simplification.

---

## ★★8 — Naive versus regularised deconvolution

**(a)** With no noise the system $Y = HX$ is exactly invertible on the padded
grid (provided $H$ has no zeros there), so the RMS error is round-off: the
lesson's equivalent test with a longer response closed at
$1.8\times10^{-15}$.

**(b)** Naive division multiplies every frequency by $1/H(f)$. Where
$\lvert H\rvert$ is small — the top of the band, and any notch — the noise
component there is multiplied by a large number, and the result is a recovered
signal whose error is dominated by a handful of high-frequency bins. The
information at those frequencies was attenuated below the noise in $y$, so the
division is amplifying noise, not recovering signal.

**(c)** **Smaller.** The regularised division
$\overline{H}Y/(\lvert H\rvert^2+\epsilon^2)$ behaves as $1/H$ where
$\lvert H\rvert \gg \epsilon$ and rolls off where $\lvert H\rvert \ll \epsilon$.
The roll-off is needed only where the noise has swamped the signal, i.e. where
$\lvert H\rvert$ has fallen by the noise-to-signal ratio. With a tenfold smaller
noise, that crossover moves to a tenfold smaller $\lvert H\rvert$, so the optimal
$\epsilon$ is smaller — approximately in proportion, or even faster, as the
lesson's own scan shows (optimal $\epsilon$ from $10^{-2}$ at noise $10^{-3}$ to
$3\times10^{-2}$ at noise $10^{-2}$).

---

## ★★★9 — How the two inverses scale with noise

**(a)** The naive error is $\lVert (Y_{\text{noise}})/H\rVert$, linear in the
noise realisation. From the table:

| noise ratio (to $10^{-4}$) | 1 | 10 | 100 | 300 |
|---|---|---|---|---|
| naive error | 0.012000 | 0.120002 | 1.200019 | 3.600057 |
| error ratio | 1 | 10.0 | 100.0 | 300.0 |

The ratios reproduce the noise ratios exactly — linear scaling confirmed to four
figures.

**(b)** $0.531946/0.177893 = 2.99$. A threefold increase in the noise gives a
threefold increase in the regularised error *at these levels*, so here the
regularised error is also linear in the noise — the regularisation is no longer
the dominant term. The sublinear part of the table is at the *other* end: from
noise $10^{-4}$ to $10^{-3}$ (a factor of 10) the error grows only from 0.015299
to 0.023347, a factor of 1.53, because at those levels the error is dominated by
the bias introduced by $\epsilon = 10^{-2}$ rather than by the noise itself. The
sublinearity appears **where the regularisation is the limiting factor**, and
disappears once the noise term dominates.

**(c)** At noise $10^{-4}$ the naive error (0.012000) is smaller than the
regularised error (0.015299); at $10^{-3}$ the order is reversed. Because the
naive error is exactly proportional to the noise, it crosses the regularised
error between the two rows:

$$120\times\sigma = 0.0153 \quad(\text{taking the regularised value as a floor})
\;\Longrightarrow\; \sigma \approx 1.3\times10^{-4}.$$

So the cross-over is at about $1.3\times10^{-4}$ — between the two lowest rows,
as the data show.

**(d)** Using [`code/convolution_demo.py`](../code/convolution_demo.py) and
scanning the water level at noise RMS $3\times10^{-2}$:

| $\epsilon$ | RMS error |
|---|---|
| 0.000 | 3.600057 |
| 0.001 | 3.403419 |
| 0.003 | 2.368828 |
| 0.010 | 0.531946 |
| 0.030 | 0.081618 |
| **0.050** | **0.059730** |
| 0.100 | 0.060062 |
| 0.200 | 0.061320 |
| 0.300 | 0.061605 |
| 1.000 | 0.061823 |

The best value in this scan is $\epsilon = 0.05$ with an RMS error of 0.059730,
against 0.531946 at $\epsilon = 0.01$ — a factor of 8.9 poorer. Note that the
error surface is flat for $\epsilon \ge 0.05$: over-regularising is much less
damaging than under-regularising, which is a useful asymmetry in practice.

**(e)** The optimal water level **tracks the noise level but not in proportion**.
From the lesson and this scan: noise $10^{-3}$ → optimal $\epsilon \approx 10^{-2}$
(ten times the noise); noise $10^{-2}$ → optimal $\epsilon \approx 3\times10^{-2}$
(three times); noise $3\times10^{-2}$ → optimal $\epsilon \approx 0.05$ (1.7
times). The ratio falls as the noise grows, so no single multiplier is safe. The
defensible rule is: *estimate the noise, scan $\epsilon$ over a decade either
side, and report both the value chosen and the sensitivity of the result to it* —
which is exactly the language of an inverse-problem result rather than a
processing recipe.

---

## ★★★10 — Brick-wall band-pass

**(a)** With $k$ in cycles per unit length and a symmetric two-sided band,

$$H(k) = \begin{cases}1, & k_1 \le \lvert k\rvert \le k_2,\\ 0, & \text{otherwise.}\end{cases}$$

**(b)** For a symmetric band the impulse response is

$$h(t) = \int_{-k_2}^{-k_1}e^{2\pi ikt}dk + \int_{k_1}^{k_2}e^{2\pi ikt}dk
= 2\int_{k_1}^{k_2}\cos(2\pi kt)\,dk
= \frac{\sin(2\pi k_2t) - \sin(2\pi k_1t)}{\pi t}.$$

For large $t$ the numerator is bounded by 2 and the denominator grows as $t$, so

$$\lvert h(t)\rvert \le \frac{2}{\pi\lvert t\rvert}
\qquad\Longrightarrow\qquad h(t) = O(1/t).$$

Each edge contributes one sinc-like $1/t$ term; the low-wavenumber edge does
*not* cancel the high-wavenumber one, because the two have different periods.

**(c)** A $1/t$ decay is extremely slow: to represent the operator to a relative
accuracy $\eta$ you need $\lvert t\rvert \sim 2/(\pi\eta)$ samples. At
$\eta = 10^{-3}$ that is about 640 samples *on each side* of the output sample —
so a "local" band-pass that appears to require a 100-sample operator is really a
700-sample operator, and when applied to a 1000-sample record through the DFT you
are implicitly assuming that the other 400 samples are whatever the periodic
extension says they are (usually a repeat of the record's start, or zeros). The
apparent locality is an artefact; the operation is global. This is why, in
practice, a sharp band-pass is always accompanied by tapering or padding, and why
its edges generate artefacts far into the record.

**(d)** Expect a *larger* overshoot than 8.949% of the step, but less than the
worst-case sum of the two edges' overshoots (about 17.9%). The reasoning: each
edge of the band produces its own ringing pattern at a jump, with the 8.949%
Gibbs overshoot relative to the jump. The patterns have different periods — the
low edge's ringing oscillates slowly, the high edge's rapidly — and they add with
a relative phase that depends on the position of the step relative to the record
and on the band edges. Where they add in phase the total approaches the sum;
where they oppose it can be smaller. A single number is therefore not
defensible; you would have to test.

To test it numerically with the supplied script: replace the brick-wall low-pass
mask in Section 4 with a mask that keeps $\lvert k\rvert$ between $k_1$ and
$k_2$, apply it to the periodic square wave, and measure the overshoot with the
same plateau-referenced statistic the script already uses for the low-pass. Do it
for several choices of $(k_1,k_2)$ and for two different positions of the jump,
and report the range rather than a single figure. Reporting the range is the
honest outcome: the answer is a property of the filter *and* of where the
discontinuity falls, not of the filter alone.
