# Solutions — 20-04-02 Spiking (Predictive) Deconvolution and Wavelet Estimation

> **Read after attempting the exercises.** Lesson:
> [02 Spiking Deconvolution](../02-spiking-deconvolution.md).

---

## ★1 — Order-2 Yule-Walker

$$\begin{pmatrix} r[0] & r[1] \\ r[1] & r[0] \end{pmatrix}
\begin{pmatrix} a_1 \\ a_2 \end{pmatrix}
= \begin{pmatrix} r[1] \\ r[2] \end{pmatrix}.$$

Solving by substitution: from the first row $a_1 = (r[1] - r[1]a_2)/r[0]$. Rather
than substituting, use Cramer's rule:

$$a_1 = \frac{r[1]r[0] - r[1]r[2]}{r[0]^2 - r[1]^2},\qquad
a_2 = \frac{r[0]r[2] - r[1]^2}{r[0]^2 - r[1]^2}.$$

The prediction-error filter is $a = [1, -a_1, -a_2]$.

---

## ★2 — Kurtosis

$$\mathrm{kurt}(x) = \frac{\mathbb{E}[(x-\bar x)^4]}
{\left(\mathbb{E}[(x-\bar x)^2]\right)^2}.$$

For a Gaussian the fourth central moment is $3\sigma^4$ and the squared variance is
$\sigma^4$, so $\mathrm{kurt} = 3$. A sparse spike train has a much larger value
(66.1 in the demo's reflectivity).

---

## ★3 — Prediction gap

The gap $\alpha$ is the lag at which the filter predicts, i.e. the repetition
period of the feature to be removed. It should be set to the measured **multiple
period**, converted from seconds to samples ($\alpha = T/\Delta t$), and it should
exceed the wavelet length so that the operator predicts the periodicity rather
than the wavelet itself.

---

## ★★4 — Operator length for a 30-sample wavelet

From the lesson's table, kurtosis and correlation peak at the *shortest* operators
(63.7 and 0.9924 at length 2) and decline after about 20 samples (62.4 and 0.9775
at 40; 60.4 and 0.9597 at 80). For a 30-sample wavelet the correct choice is
**$p \approx 30$** — long enough to whiten the wavelet, no longer. Expect kurtosis
close to 62 and correlation close to 0.98, with the noise gain near 2.

Making the operator much longer than the wavelet costs accuracy (kurtosis 60.4 and
correlation 0.9597 at $p = 80$) because the extra coefficients fit the noise in the
estimated autocorrelation.

---

## ★★5 — Why a zero-phase wavelet cannot be spiked causally

A zero-phase wavelet is symmetric about $n = 0$, so its inverse is also symmetric
about $n = 0$ — it has coefficients at negative lags and is **non-causal**. A
causal FIR operator can only use $x[n], x[n-1], \dots$, i.e. positive lags, so it
cannot realise that inverse. When the Levinson recursion is applied anyway, it
finds the minimum-energy predictor, which suppresses the trace rather than
inverting it; the resulting output is a phase-distorted, near-zero-correlation
image of the reflectivity.

There is no fix from the autocorrelation alone, because the autocorrelation of a
zero-phase wavelet is *identical* to that of its minimum-phase counterpart: the
autocorrelation discards phase, so it cannot tell you which one you have.

---

## ★★6 — Suppression factors

$$\text{suppression} = \frac{\rho_{\text{input}}}{\rho_{\text{output}}}$$

- gap = period: $0.4613/0.0436 = 10.6\times$ — the multiple is suppressed.
- gap = half period: $0.4613/0.3896 = 1.18\times$ — essentially nothing.
- gap = 2 × period: $0.4613/0.3975 = 1.16\times$ — essentially nothing.

**Design conclusion**: the gap must match the measured period. The difference
between the right and wrong gap is a factor of nine in suppression, so a guessed
gap is not a small error — it is the difference between working and not working.
Measure the period from the peak of the trace autocorrelation.

---

## ★★★7 — Minimum-phase spectral factorisation

Let $S(\omega) \ge 0$ be a power spectrum with $\log S$ integrable (the
Paley-Wiener condition). Write $\log S(\omega) = \sum_n c_n e^{-i\omega n}$ (the
cepstrum) and define the **minimum-phase cepstrum** by folding the acausal part to
zero:

$$c^{+}_n = \begin{cases} c_0, & n = 0,\\ 2c_n, & n > 0,\\ 0, & n < 0.\end{cases}$$

Then $W_{\min}(\omega) = \exp\!\left(\sum_n c^{+}_n e^{-i\omega n}\right)$ satisfies
$|W_{\min}|^2 = S$, and since the exponent's transform has no acausal part, the
result is causal and minimum phase. Uniqueness follows because any other solution
differs from $W_{\min}$ by an all-pass factor, which is non-minimum-phase (it adds
the same magnitude but extra phase).

**Why it matters**: the spiking operator is $1/W_{\min}$. Because $W_{\min}$ has all
its zeros inside the unit circle, its reciprocal is causal and stable — a realisable
filter. Without the minimum-phase choice, $|W|^2 = S$ has infinitely many solutions
and only one of them yields a causal stable inverse. Spectral factorisation is
therefore what turns "invert the autocorrelation" from an underdetermined statement
into a well-defined algorithm.

---

## ★★★8 — Robust predictive deconvolution

With a period varying by $\pm10\%$ — say $T = 120 \pm 12$ ms — a single gap of
120 ms misses the extremes by up to 12 ms.

**Option 1 — widen the operator.** Keep the gap at 120 ms but extend $p$ so the
filter's prediction window spans the variation. Cost: a longer operator fits noise
(§4 of the lesson) and whitens more of the band than necessary; the spikiness gain
falls.

**Option 2 — apply several gaps and sum.** Design three or more operators with
gaps at 108, 120 and 132 ms and apply them in cascade. Cost: each pass
re-introduces its own operator bias, and the effective operator is the product of
the three, which is longer and noisier than any one; it also risks over-whitening.

**Option 3 — window the operator design.** Estimate the period per window (a
sliding autocorrelation), design a gap per window, and apply the filters
window by window. Cost: the period estimate needs several periods of data, so the
temporal resolution of the gap estimate is limited to that window length; and
discontinuities between windows can appear unless the operators are interpolated.

The cheapest robust method in practice is **option 1 with a modest $p$**, because
the multiple's autocorrelation peak is broad anyway: a $\pm10\%$ period spread
corresponds to a correlation width that a 40–60 ms operator already covers.