# Solutions — 20-05-02 Autocorrelation, Power Spectral Density and Wiener-Khinchin

> Read after attempting. Numbers computed. Lesson:
> [02 Autocorrelation and PSD](../02-autocorrelation-spectra.md).

---

## ★1 — The frequency grid

$$\mathrm{d}f = \frac{f_s}{N} = \frac{64}{2048} = 0.03125\ \mathrm{Hz},
\qquad f_N = \frac{f_s}{2} = 32\ \mathrm{Hz}.$$

A one-sided PSD from `numpy.fft.rfft` has $N/2 + 1 = 1025$ values, from
$f = 0$ to $f = 32\ \mathrm{Hz}$ inclusive.

---

## ★2 — A factor-of-two error

The integral of the one-sided PSD must equal the variance. Getting $5.00$ for a
variance of $2.50$ means the PSD is a factor of two too large. The usual cause is
applying the fold $S_1 = 2S_2$ *and* treating the result as if it were still
two-sided — i.e. counting the negative frequencies twice. Either divide the
computed spectrum by two, or return to the two-sided convention and integrate
over $-f_N$ to $+f_N$. The corrected one-sided integral must be $2.50$.

---

## ★3 — The periodogram ratio

For Gaussian white noise, $\operatorname{std}/\operatorname{mean} \to 1$ at
every frequency. A reported $5\%$ standard error is therefore wrong by a factor
of 20.

Doubling the record length **changes nothing** about that ratio. The number of
frequency bins doubles and each bin remains exponential with mean equal to its
standard deviation. Only averaging over bins, segments or realisations reduces
the ratio.

---

## ★4 — Conflicting requirements

Standard error $15\%$ needs $1/\sqrt{K_{\text{eff}}} \le 0.15$, i.e.
$K_{\text{eff}} \ge 44.4$.

Resolution $1\ \mathrm{Hz}$ with a Hann window needs
$2f_s/N_{\text{seg}} < 1$, i.e. $N_{\text{seg}} > 2(100)/1 = 200$ samples. Try
$N_{\text{seg}} = 256$. With 50% overlap,

$$K_{\text{nominal}} = \frac{2N}{N_{\text{seg}}} - 1 = \frac{2(8192)}{256} - 1
= 63, \qquad K_{\text{eff}} \approx \frac{63}{2} = 31.5,$$

so $\text{SE} \approx 1/\sqrt{31.5} = 17.8\%$ — short of the target.

Try $N_{\text{seg}} = 192$: resolution $2(100)/192 = 1.04\ \mathrm{Hz}$, which
misses $1\ \mathrm{Hz}$; and
$K_{\text{nominal}} = 2(8192)/192 - 1 = 84.3$, $K_{\text{eff}} \approx 42$,
$\text{SE} \approx 15.4\%$.

**Conclusion.** The two requirements conflict on this record. The best
compromise is $N_{\text{seg}} = 256$ with 50% overlap, giving $1.00\ \mathrm{Hz}$
resolution and a $17.8\%$ standard error, and reporting the shortfall; or a
multitaper estimator, which reaches a given variance with a wider effective
resolution. Do not report both targets as met.

---

## ★5 — Why the ratio is one

For a white Gaussian record of $N$ samples, $X_k = \sum_n x_n e^{-i2\pi kn/N}$ is
a complex Gaussian with

$$\operatorname{Var}(\operatorname{Re}X_k) =
\operatorname{Var}(\operatorname{Im}X_k) = \frac{N\sigma^{2}}{2}.$$

The modulus squared $|X_k|^{2} = (\operatorname{Re}X_k)^{2} +
(\operatorname{Im}X_k)^{2}$ is then a sum of two squared Gaussians of equal
variance, i.e. an exponential random variable with

$$\mathbb{E}|X_k|^{2} = N\sigma^{2}, \qquad
\operatorname{Var}(|X_k|^{2}) = (N\sigma^{2})^{2} .$$

Since $\hat S \propto |X_k|^{2}$ by a fixed constant, the ratio of standard
deviation to mean is $N\sigma^{2}/(N\sigma^{2}) = 1$, independent of $N$.

---

## ★6 — Resolving two Hann-window lines

$$2f_s/N_{\text{seg}} < 4\ \mathrm{Hz}
\;\Longrightarrow\;
N_{\text{seg}} > \frac{2f_s}{4} = \frac{2(200)}{4} = 100 .$$

The smallest practical power-of-two segment is $N_{\text{seg}} = 128$ samples,
giving a nominal resolution of $2(200)/128 = 3.125\ \mathrm{Hz}$, comfortably
below the $4\ \mathrm{Hz}$ separation. At $N_{\text{seg}} = 64$ the resolution
would be $6.25\ \mathrm{Hz}$ and the lines would merge.

---

## ★★★7 — Measuring the bias from a Hann window

**Design.** Synthesise a record containing one narrow line plus white noise at a
known level. Analyse it with a Hann window at
$N_{\text{seg}} \in \{64, 128, 256, 512, 1024, 2048\}$, with 50% overlap, and for
each compute the PSD on a fixed frequency grid. Repeat over $M = 500$ noise
realisations.

**Metric.** For each segment length, take the ensemble-mean PSD and report

$$\text{bias}(N_{\text{seg}}) = \frac{\bar S_{\text{Welch}}(f_0)}
{S_{\text{true}}(f_0)} - 1
\quad\text{and}\quad
\text{line width} = \text{FWHM of the mean peak}.$$

**Expected direction.** A Hann window broadens the line by roughly a factor of
two relative to a rectangular window, so as $N_{\text{seg}}$ *decreases* the mean
peak height at the line's centre falls (the line's energy is spread over bins
wider than $\mathrm{d}f$) while the level away from the line rises from leakage.
The bias is therefore **negative at the peak** and **positive in the wings**.

**Separating bias from variance.** The bias is the deviation of the
*ensemble-mean* spectrum from the truth; the variance is the scatter of a single
realisation around that mean. Compute both: report
$\text{bias} \pm \operatorname{std}(S)/\sqrt{M}$ for the mean, and
$\operatorname{std}(S)/\operatorname{mean}(S)$ for the single-realisation
scatter. A bias is only claimed when it exceeds three times its own standard
error. This is the difference between "the estimator is wrong" and "the estimator
is noisy", and confusing them is the usual failure in this kind of study.

---

## ★★★8 — Equivalence and its tolerance

**(a)** From §3.1 of the lesson, $|X_k|^{2} = N\sum_m \hat C(m)
e^{-i2\pi km/N}$ with $\hat C$ the **biased** sample autocovariance (the divisor
$N$, not $N-k$). The periodogram is exactly that expression multiplied by
$2\Delta t/(f_s N) = 2\Delta t^2$. They are not two estimators of the same
quantity that agree approximately; they are the same sum with the same
arithmetic, evaluated by two different FFTs.

**(b)** Both routes end in a floating-point computation whose error is a
relative error of order the machine epsilon, $\varepsilon \approx
2.2\times10^{-16}$ for doubles. A sum of $N$ terms accumulates of order
$\sqrt{N}\,\varepsilon$ if the rounding is random, here
$\sqrt{8192}\times2.2\times10^{-16} \approx 2\times10^{-14}$ as a pessimistic
bound; the measured $9.7\times10^{-17}$ is better because the comparison is
between two well-conditioned sums. A residual of $10^{-30}$ would require more
than double precision, so $10^{-16}$ is exactly the right order to expect — it is
the statement "the two are equal to machine precision", not "the two differ".

**Extending to $N = 10^{7}$.** The error grows slowly (at worst as $\sqrt N$)
while the two computations also require different algorithms — the direct
transform of a $10^{7}$-lag autocovariance is unrealistic, so the comparison
would have to be made on a subsampled lag range, and the tolerance would have to
be stated in terms of the accumulated error: something like
$10\,\sqrt{N}\,\varepsilon$ rather than a fixed absolute number. Choosing the
tolerance before knowing the conditioning is what makes this the dangerous step.
