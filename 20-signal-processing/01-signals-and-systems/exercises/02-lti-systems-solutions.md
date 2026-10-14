# Solutions — 20-01-02 Linear Time-Invariant Systems and Impulse Response

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All models are **SYNTHETIC**.

Lesson: [02 LTI Systems](../02-lti-systems.md).

---

## ★1 — Classification

| system | linear? | time-invariant? | impulse response |
|---|---|---|---|
| (a) $y[n] = 3x[n]-x[n-1]$ | yes | yes | $h = [3,\,-1]$ |
| (b) $y[n] = x^{2}[n]$ | **no** | yes | not defined (system is not LTI) |
| (c) $y[n] = x[n/2]$ (even $n$) | yes | **no** | not defined |
| (d) $y[n] = n\,x[n]$ | yes | **no** | not defined |
| (e) $y[n] = 0.5y[n-1]+x[n]$ | yes | yes | $h[n] = 0.5^{n}u[n]$ |

**(b)** fails linearity: $x_1 = [1]$, $x_2 = [1]$, $a = b = 1$ give
$\mathcal H\{x_1+x_2\} = 4$ but $\mathcal H\{x_1\}+\mathcal H\{x_2\} = 2$.

**(c)** fails time-invariance: shift the input by one sample and the output does
not shift — it changes shape, because the decimator keeps a different phase of
the input.

**(d)** fails time-invariance: shifting the input shifts the multiplier too,
since $n$ is tied to absolute time.

**Note.** Using a time-varying system does not make it wrong; it means an impulse
response measured at one time does not describe the system at another.

---

## ★2 — Hand convolution and the sum check

$x = [2,-1,3]$ on $n = 0,1,2$; $h = [1, 0.5]$ on $n = 0,1$:

$$y[0] = 2, \quad y[1] = 2(0.5) + (-1) = 0, \quad
y[2] = -0.5 + 3 = 2.5, \quad y[3] = 3(0.5) = 1.5 .$$

So $y = [2, 0, 2.5, 1.5]$, length $3+2-1 = 4$.

Check: $\sum y = 6.0$ and $(\sum x)(\sum h) = 4 \times 1.5 = 6.0$. ✔

---

## ★3 — One-pole system with $a = 0.7$

$$h[n] = 0.7^{\,n}u[n], \qquad
\sum_{n=0}^{\infty}\lvert h[n]\rvert = \frac{1}{1-0.7} = 3.333333,$$

finite, so the system is BIBO-stable. DC gain $= 3.333333$.

Step response at $n = 5$: $s[n] = (1-0.7^{\,n+1})/(1-0.7)$, so

$$s[5] = \frac{1-0.7^{6}}{0.3} = \frac{1-0.117649}{0.3} = 2.941170 .$$

Equivalently $s[5] = 1-0.7^{6}$ normalised by the DC gain:
$1.0 - 0.117649 = 0.882351$ of the final value.

---

## ★4 — A five-tap FIR

$h = [1, 0.8, 0.6, 0.4, 0.2]$.

**(a) DC gain** $= \sum h = 3.0$ exactly.

**(b) Step response** (running sum) $= [1.0,\ 1.8,\ 2.4,\ 2.8,\ 3.0]$, after which
it equals the DC gain.

**(c) Group delay.** For a symmetric FIR of odd length $M$, the phase is exactly
linear and $\tau_g = (M-1)/2 = 2$ samples. **This $h$ is not symmetric** — its
centroid delay is
$\left(\sum_n n\,h[n]\right)/\left(\sum_n h[n]\right) = 4.0/3.0 = 1.333333$
samples — so its phase is *not* linear and a single group-delay number is
misleading. The correct statement is that $\tau_g(\omega)$ varies with frequency.

**(d)** $x = [1,1,1,1,1]$:

$$h * x = [1.0,\ 1.8,\ 2.4,\ 2.8,\ 3.0,\ 2.0,\ 1.2,\ 0.6,\ 0.2],$$

length $5+5-1 = 9$. The two checks: the entries after the first five are the
*reversed* cumulative sums $3.0-1.0 = 2.0$, $2.0-0.8 = 1.2$, $1.2-0.6 = 0.6$,
$0.6-0.4 = 0.2$, $0.2-0.2 = 0$; and $\sum y = 15.0 = (\sum x)(\sum h) = 5\times3$.
✔

**Unit note.** Sampled at $1\ \mathrm{kHz}$, $\tau_g = 2$ samples $= 2\ \mathrm{ms}$
for the symmetric case, and the centroid delay $1.333$ samples
$= 1.333\ \mathrm{ms}$.

---

## ★5 — Linearity forces $\mathcal H\{0\} = 0$, and why $\lvert x\rvert$ fails

Set $a = 1$, $b = -1$ and any $x$ in (L):

$$\mathcal H\{0\} = \mathcal H\{x - x\} = \mathcal H\{x\} - \mathcal H\{x\} = 0 .$$

**Sensor offset.** A sensor reporting $2.5\ \mathrm{V}$ at zero input is affine,
$y = \mathcal H\{x\} + 2.5$, and fails (L) immediately. Physically the offset is
usually additive and stable, so the fix is to estimate it (with the input
blocked) and subtract it before any superposition-based processing. Doing this
is not optional bookkeeping: an unremoved offset propagates through every later
stage, and a zero-phase filter will smear it across the record.

**$y = \lvert x\rvert$ is not linear.** Take $x_1 = [1,-2]$ and $x_2 = [-1,-2]$
with $a = b = 1$:

$$\lvert x_1 + x_2\rvert = [0, 4], \qquad
\lvert x_1\rvert + \lvert x_2\rvert = [2, 4].$$

The two differ at $n=0$, so (L) fails. (It is time-invariant, so it is a
candidate LTI system that fails only one axiom — a useful reminder that the two
axioms are independent.)

---

## ★6 — Cascade by associativity

$h_1[n] = 0.5^{n}u[n]$, $h_2 = [1,\,-0.25]$.

$$h_c[n] = \sum_k h_1[k]h_2[n-k]
= h_1[n] - 0.25\,h_1[n-1].$$

For $n = 0$: $h_c[0] = 1$. For $n \ge 1$:
$h_c[n] = 0.5^{n} - 0.25\cdot0.5^{\,n-1} = 0.5^{\,n-1}(0.5-0.25)
= 0.25\cdot0.5^{\,n-1} = 0.5^{\,n+1}$. Hence

$$h_c = [1,\ 0.25,\ 0.125,\ 0.0625,\ 0.03125,\ \dots]
= \delta[n] + 0.5^{\,n+1}u[n-1].$$

**DC gain of the cascade** $= (\sum h_1)(\sum h_2)
= \dfrac{1}{1-0.5}\,(1-0.25) = 2\times0.75 = 1.5$ exactly.

**Which is which.**

| | $H(e^{i0})$ | $H(e^{i\pi})$ | character |
|---|---|---|---|
| $h_1$ (one-pole) | $2.000$ | $1/(1+0.5) = 0.667$ | low-pass: passes DC, attenuates Nyquist |
| $h_2 = [1,-0.25]$ | $0.750$ | $1.250$ | high-pass: attenuates DC, boosts Nyquist |

Computing the truncated sums numerically gives $1.9921875$ and $0.6640625$ for
$h_1$ (8 terms) and $0.75$, $1.25$ for $h_2$, confirming the table and showing
that the truncation is the only error.

---

## ★7 — Drifting gain versus non-LTI (specification)

**Input.** A repeatable broadband test signal, not ambient noise: either a
pseudo-random binary sequence injected at the sensor, or a known synthetic
sweep, repeated many times across a full daily temperature cycle.

**Design.** Repeat the identical input at intervals short compared with the
thermal time constant.

**Statistic.** Recover $H(f,t)$ for each repeat and track (i) the *shape*
$H(f,t)/H(0,t)$ and (ii) the *scalar* gain $H(0,t)$. Use a coherence-based
estimator ([20-02-04](../../02-fourier-and-spectral-analysis/04-cross-spectra-coherence.md))
so that the resolution of the statistic in frequency is stated.

**Signatures.**

- *LTI with drifting gain*: shape is constant to within the estimator's
  resolution; the scalar gain correlates with temperature at the stated
  $0.05\%\,\mathrm{K^{-1}}$, which over $\pm2.5\ \mathrm{K}$ is a
  $\pm0.125\%$ effect — detectable only if the gain estimate is resolved better
  than that, so the required precision sets the number of repeats.
- *Not LTI*: the shape changes with time or amplitude, the residual after a
  time-varying scalar correction is structured, and the response to a
  large-amplitude repeat differs from the small-amplitude one.

**Resolution requirement.** The measurement must resolve $0.1\%$ in gain to see
the drift at all. With $K$ independent repeats the gain uncertainty falls as
$1/\sqrt{K}$, so state $K$ rather than hoping.

**If drift is supported.** Split the record into intervals short compared with
the thermal time constant, deconvolve each with its own gain, and record the
gain series as part of the metadata. Do not apply one calibration to the whole
record.

---

## ★8 — Onset delay versus centroid delay

Use a single-pole causal low-pass with $a = 0.9$:
$h[n] = 0.9^{\,n}u[n]$.

- **Onset delay:** the first non-zero output sample occurs at the same index as
  the input impulse, so the onset delay is $0$ samples.
- **Centroid delay:**

$$\frac{\sum_n n\,h[n]}{\sum_n h[n]}
= \frac{0.9/(1-0.9)^{2}}{1/(1-0.9)}
= \frac{90}{10} = 9.0 \ \text{samples}.$$

The two differ by 9 samples — far more than one sample, and the sign is
positive (the centroid lags the onset).

**What a first-break picker measures.** A picker detects the *first* sample at
which the signal exceeds a threshold above the noise, i.e. an onset-like
statistic. On a causally low-pass-filtered record the onset is preserved but the
waveform is stretched, so the pick lands near the true onset and the bias is
small — provided the threshold is set from the noise level, not from a fixed
fraction of the peak.

**Bias direction and size.** If instead the arrival time is estimated from the
peak or the centroid of the envelope, the estimate is biased *late* by the
centroid delay of the wavelet — up to 9 samples in this example, i.e.
$9\Delta t$ in seconds. For a $200\ \mathrm{Hz}$ channel that is $45\ \mathrm{ms}$;
for a $10^{-4}\ \mathrm{s}$-sampled record it is negligible. The magnitude
scales with the filter's pole radius (its "ringing time"), so it must be
re-reported whenever the processing chain's low-pass corner changes. Cross-correlation
(pick the peak of the cross-correlogram) measures the centroid, not the onset,
for asymmetric wavelets.


---

## Mastery checkpoint answers

**(c)** $x = [2,-1,3]$, $h = [1,0.5]$:

$$y[0] = 2,\quad y[1] = 2(0.5) - 1 = 0,\quad
y[2] = -0.5 + 3 = 2.5,\quad y[3] = 1.5,$$

so $y = [2,\,0,\,2.5,\,1.5]$ and the sum check reads
$\sum y = 6.0 = (2-1+3)(1+0.5) = 4 \times 1.5$ ✔.

**(d)** For $y[n] = 0.8\,y[n-1] + x[n]$:

- $h[n] = 0.8^{n}u[n]$;
- $\sum_n \lvert h[n]\rvert = 1/(1-0.8) = 5.000000$ (finite, so BIBO-stable);
- DC gain $= 5.000000$;
- $10\%$–$90\%$ rise time of the step response: the normalised step is
  $1-0.8^{\,n+1}$, so $10\%$ occurs at
  $n+1 = \ln 0.9/\ln 0.8 = 0.4722$ and $90\%$ at
  $n+1 = \ln 0.1/\ln 0.8 = 10.319$, giving a rise time of
  $10.319-0.472 = 9.85$ samples. As a check, the time constant is
  $-1/\ln 0.8 = 4.481$ samples and $2.197\tau = 9.85$ ✔.
