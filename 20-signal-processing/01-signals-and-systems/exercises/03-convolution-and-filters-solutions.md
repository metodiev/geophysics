# Solutions — 20-01-03 Convolution, Correlation and Filtering

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All models are **SYNTHETIC**.

Lesson: [03 Convolution, Correlation and Filtering](../03-convolution-and-filters.md).

---

## ★1 — Hand convolution

$y = x * h$ with $x = [3,-1,2]$ on $n=0,1,2$ and $h = [1,2]$ on $n=0,1$:

$$y[0] = 3, \quad y[1] = 3(2) + (-1)(1) = 5, \quad
y[2] = (-1)(2) + 2(1) = 0, \quad y[3] = 2(2) = 4 .$$

$$y = [3,\ 5,\ 0,\ 4], \qquad L = 3 + 2 - 1 = 4 .$$

Sum rule: $\sum y = 12 = (3-1+2)(1+2) = 4\times3$. ✔

---

## ★2 — Matched filter for a rectangular pulse

Matched filter: $h[n] = s[-n]$, i.e. a rectangle of 32 unit samples (the
time-reversed rectangle is itself). The attainable peak-to-rms gain is

$$G = \frac{\lVert s\rVert}{\sigma}
= \frac{2\sqrt{32}}{1.5} = \frac{11.313708}{1.5} = 7.542472 .$$

In decibels: $20\log_{10}7.542472 = 17.550\ \mathrm{dB}$.

Sanity check on the scaling: the peak of the matched-filter output is
$\lVert s\rVert^{2} = 128$, the output noise rms is
$\sigma\lVert s\rVert = 1.5\times11.313708 = 16.970563$, and their ratio is
$7.542472$, as above. Pulses of amplitude $2$ therefore remain detectable
(peak-to-rms $> 5$, i.e. $>14\ \mathrm{dB}$) but a change of the pulse length to
8 samples would reduce the gain to $2\sqrt8/1.5 = 3.771$.

---

## ★3 — Output lengths and wrap-around

- `full`: $N + M - 1 = 64 + 7 - 1 = 70$ samples.
- `same`: 64 samples — the first and last $(M-1)/2 = 3$ samples of the `full`
  output are discarded.
- `valid`: $N - M + 1 = 58$ samples — only where the kernel fully overlapped.

With an FFT length of 64 instead of 70, the six samples of the convolution that
would have extended beyond index 63 wrap around and are added to indices
$0..5$. All 64 output samples are therefore wrong, not just the ends: the
wrap-around term has *maximum* effect at the beginning and decays through the
record, but the demonstration measured that for a 40-sample input and a 5-point
kernel the wrap-around rms was **50.3 %** of the output rms, with the error
spread over the entire array. The correct statement of the rule is
$N_{\text{FFT}} \ge N + M - 1$, and padding beyond it (to a power of two, for
speed) never hurts.

---

## ★4 — Resolving two Gaussian pulses

**(a) Raw trace.** A sum of two Gaussians of equal width $\sigma$ and separation
$d$ has three extrema when $d > 2\sigma$ and one when $d < 2\sigma$: the midpoint
switches from a local maximum to a saddle at $d = 2\sigma$. So the pair is
resolved for

$$d > 2\sigma = 4\ \text{samples}.$$

**(b) After matched filtering.** The matched filter convolves the trace with a
Gaussian of the same width, so each peak broadens to
$\sigma' = \sqrt{\sigma^{2}+\sigma^{2}} = \sigma\sqrt2 = 2.828$ samples, and the
condition becomes

$$d > 2\sigma' = 4\sqrt2 = 5.657\ \text{samples}.$$

**Which criterion, and why it is a convention.** The $2\sigma$ rule is the
separation at which the *sum* of the two shapes loses its saddle point; it is the
mathematical statement "the union is no longer bimodal". It is a convention
because (i) real data carry noise, so the practical limit depends on SNR; (ii)
the Rayleigh criterion (a dip of a stated depth between the peaks) is an
alternative and gives a different number; and (iii) the eye and a peak-picker
disagree near the threshold. Whenever you quote a resolution, quote the criterion
and the SNR at which it holds.

---

## ★5 — Moving-average gain near a null

$$H(e^{i\omega}) = \frac{1}{5}e^{-i\omega\cdot2}
\frac{\sin(5\omega/2)}{\sin(\omega/2)} .$$

| $\omega$ | $\lvert H\rvert$ | dB |
|---|---|---|
| $2\pi/5 = 1.256637$ | $8.3\times10^{-17}$ | (exact zero) |
| $0.9\times2\pi/5 = 1.130973$ | $0.115342$ | $-18.760$ |
| $1.1\times2\pi/5 = 1.382301$ | $0.096958$ | $-20.268$ |

**Algebraic confirmation of the null.** At $\omega = 2\pi k/M$,
$H = \frac1M\sum_{n=0}^{M-1}e^{-i2\pi kn/M} = \frac1M
\frac{1-e^{-i2\pi k}}{1-e^{-i2\pi k/M}} = 0$ for $k = 1,\dots,M-1$, because the
sum of the $M$-th roots of unity vanishes and the denominator is non-zero.

**Implication.** The null is only $\sim -19$ to $-20\ \mathrm{dB}$ when the
interference frequency is 10 % away from it — a factor of $\sim 10$ in amplitude,
not the factor of $10^{8}$ implied by "zero". A moving average removes a periodic
interference only when the interference period is an integer number of samples
*and* the record length is a whole number of periods. Otherwise you have a mild
notch, and the honest statement is "attenuated by about $20\ \mathrm{dB}$", not
"removed".

---

## ★6 — Delay uncertainty from a correlation coefficient

**Conversion to SNR.** For a measurement in which the signal amplitude is
$A_{\text{s}}$ and the noise standard deviation is $\sigma$, the normalised
correlation coefficient is $\rho = A_{\text{s}}/\sqrt{A_{\text{s}}^{2}+
\sigma^{2}}$, so

$$\mathrm{SNR} = \frac{A_{\text{s}}^{2}}{\sigma^{2}}
= \frac{\rho^{2}}{1-\rho^{2}} = \frac{0.42^{2}}{1-0.42^{2}} = 0.2144 .$$

**Propagating to the delay.** With
$f_{\text{dom}} = 12\ \mathrm{Hz}$,

$$\sigma_\tau \approx \frac{1}{2\pi f_{\text{dom}}\sqrt{\mathrm{SNR}}}
= \frac{1}{2\pi\cdot12\cdot\sqrt{0.2144}}
= \frac{1}{75.398\times0.4630} = 0.028645\ \mathrm{s} = 28.6\ \mathrm{ms}.$$

**Why it is only a guide.** (i) The formula is the Cramér–Rao bound for a
time-delay estimate of a *known* narrow-band signal; a real wavelet is not
narrow-band, and the bound degrades as the bandwidth shrinks from that
assumption. (ii) It assumes the two channels' noises are independent and equal;
correlated noise biases the estimate towards zero delay. (iii) The coefficient
itself is estimated with uncertainty, so $\rho = 0.42$ has an error bar that
propagates non-linearly through $\rho^{2}/(1-\rho^{2})$. The legitimate use is
scaling: it says the uncertainty is tens of milliseconds, and that doubling the
SNR would reduce it by $\sqrt2$. To *measure* the uncertainty, resample the
estimate — a bootstrap over record segments or over independent event repeats.

---

## ★7 — Designing a 0.2-sample delay experiment (specification)

**Target.** Detect $\Delta = 0.2$ samples ($= 0.4\ \mathrm{ms}$ at
$2\ \mathrm{ms}$ sampling) with a stated $5\sigma$ confidence, i.e. a detected
shift of at least $5\sigma_\tau$ in the measured lag.

**Input signal.** Must be broadband: a synthetic sweep from $5$ to $40\
\mathrm{Hz}$ over $20\ \mathrm{s}$, or band-limited white noise. A pure tone is
unusable — its autocorrelation is periodic, so the correlogram has many equal
peaks and the lag is ambiguous.

**Estimator.** Cross-correlation of the two channels with zero-mean, unit-variance
normalisation; locate the peak; **interpolate** the peak with a parabola through
the three samples around it. The parabola interpolation is where sub-sample
resolution comes from: without it the resolution floor is one sample and the
target is unreachable by construction.

**Uncertainty.** Bootstrap: divide the record into $K$ independent segments of
at least $10/f_{\text{min}}$ seconds each, estimate the lag on each, and use the
standard error of the $K$ estimates. State $K$ and the segment length.

**Null distribution.** Generate it by *shifting one channel circularly by a
random non-integer number of samples*, re-running the whole estimator, and
repeating. Circular shifting preserves the spectrum exactly, so the null contains
no spurious delay; simply adding noise does not test the estimator's bias.

**Repeats needed.** If the target is $0.2$ samples and the per-estimate standard
error is $s$, the required number of independent repeats is
$K = (5s/0.2)^{2}$; compute $s$ from a pilot and report $K$. If $K$ exceeds what
the data allow, the honest answer is that the target is not reachable with this
record, and the specification should say so rather than round up.

**Falsification.** Inject a *known* delay of $0.2$ samples and run the estimator
blind. If the estimator returns zero beyond the stated uncertainty, the claimed
resolution is falsified. Do this for several delays including 0.

---

## ★8 — Debugging a convolution routine

Order of tests, with the diagnostic number that identifies each hypothesis:

| # | hypothesis | diagnostic | expected if the hypothesis is right |
|---|---|---|---|
| 1 | **missing reversal** (used correlation) | compare the two arrays directly | they differ by a reflection — the bug only shows on asymmetric inputs, so test with an asymmetric $h$ |
| 2 | **insufficient padding** (circular convolution) | `max|y_fft - y_direct|` on the interior | a maximum error of order the signal, not of order $10^{-15}$; the demonstration's version of this mistake gave a wrap-around rms that was **50.3 %** of the output rms, with a maximum of $0.943834$ |
| 3 | **wrong mode** | output length and the position of a known feature | `same` removes the $(M-1)/2$ delay and trims both ends; a pulse injected at sample 60 appeared at 58 |
| 4 | **off-by-one in the output length** | $L$ versus $N+M-1$, then the sum rule | the sum rule fails unless the missing samples happen to be zero |

**The property that catches it in a unit test:** the **sum rule**,
$\sum(x*h) = (\sum x)(\sum h)$. It is exact, one line, and fails for truncation,
wrong length and missed samples — though not for a reversal (the sum is
unchanged) and not for padding errors that preserve the total.

**Pseudocode:**

```text
assert isclose(sum(convolve(x, h)) , sum(x) * sum(h))            # sum rule
assert len(convolve(x, h, 'full')) == len(x) + len(h) - 1        # length
assert isclose(convolve(x, h, 'full')[k], sum(x[i]*h[k-i] ...))  # one sample, by hand
# and once, with an asymmetric h, to catch the reversal:
assert not isclose(convolve(x, h), correlate(x, h[::-1]) * 0 + correlate(x, h))
```

Better still, add an FFT-versus-direct comparison for a small case
($N \le 64$), with a tolerance of $10^{-12}$ relative — that single test catches
reversal, padding, mode and length errors together, at the cost of one extra
line.


---

## Mastery checkpoint answers

**(a)** $x = [1,2,-1]$, $h = [2,0.5]$:

$$y = [2,\; 4.5,\; -1,\; -0.5], \qquad L = 3+2-1 = 4,$$
$$\sum y = 5.0 = (1+2-1)(2+0.5) = 2 \times 2.5 \; ✔ .$$

**(b)** The DFT implements a *circular* convolution of the transform length. With
a 1024-point transform, the 1999 samples of the true linear convolution wrap: the
last $1999-1024 = 975$ samples are added to the first 975. The fix is to
zero-pad both sequences to at least $N+M-1 = 1999$ (2048 for a power of two).

**(c)** $\lVert s\rVert = 3\sqrt{25} = 15$, $\sigma = 2$, so the attainable
peak-to-rms gain is $7.5$ ($17.5\ \mathrm{dB}$). For the Gaussian pulse of unit
peak and sample norm $4.10$ the gain is $4.10/2 = 2.05$ — the shape, not the
filter, sets the ceiling.

**(d)** The correlation peak sits at lag 227 measured from the template's first
sample, and the template's origin (its centre) is at index 10, so the feature is at
sample $227+10 = 237$.

**(e)** An 8-point moving average has exact nulls at $\omega = 2\pi k/8$ for
$k = 1,2,3$, i.e. $\pi/4$, $\pi/2$ and $3\pi/4\ \mathrm{rad}$. The gain at
Nyquist is $(1/8)\sum(-1)^{n} = 0$ because $M$ is **even** — an even-length
average annihilates the Nyquist component, whereas an odd-length one leaves
$1/M = 0.2$ (measured for $M = 5$). That is the one place where the parity of $M$
changes the answer.
