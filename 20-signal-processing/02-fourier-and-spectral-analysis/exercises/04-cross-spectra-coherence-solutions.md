# Solutions — 20-02-04 Cross-Spectra, Coherence and Phase Estimation

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All models are **SYNTHETIC**.

Lesson: [04 Cross-Spectra, Coherence and Phase Estimation](../04-cross-spectra-coherence.md).

---

## ★1 — The magnitude-squared coherence

$$\gamma^{2}(f) = \frac{\lvert S_{yx}(f)\rvert^{2}}{S_{xx}(f)\,S_{yy}(f)}
= \frac{\lvert\hat S_{yx}(f)\rvert^{2}}{\hat S_{xx}(f)\,\hat S_{yy}(f)}
\quad\text{when estimated},$$

where $S_{yx}$ is the cross-spectrum and $S_{xx}$, $S_{yy}$ the auto-spectra.

- **Range:** $0 \le \gamma^{2} \le 1$, by the Cauchy–Schwarz inequality applied to
  the two spectra — equality at 1 only for a perfectly linearly related pair.
- **Units:** dimensionless. The numerator carries
  $(\text{unit}_x)^{2}(\text{unit}_y)^{2}\,\mathrm{Hz^{-2}}$ and the denominator
  the same, so units cancel whether the two channels share units or not. That is
  why coherence is a convenient diagnostic across sensor types (m/s against V, for
  instance), while the transfer function is not.

---

## ★2 — Coherence and SNR

$$\gamma^{2} = \frac{\mathrm{SNR}}{1+\mathrm{SNR}}
\;\Longrightarrow\;
\mathrm{SNR} = \frac{\gamma^{2}}{1-\gamma^{2}}
= \frac{0.64}{0.36} = 1.7778 \;\Rightarrow\; 10\log_{10}1.7778 = 2.50\ \mathrm{dB}.$$

For an output SNR of 20 dB, $\mathrm{SNR} = 10^{2} = 100$:

$$\gamma^{2} = \frac{100}{101} = 0.990099 .$$

**The point of the table:**

| $\gamma^{2}$ | 0.2 | 0.5 | 0.8 | 0.9 | 0.99 | 0.999 |
|---|---|---|---|---|---|---|
| SNR (dB) | $-6.0$ | 0.0 | 6.0 | 9.5 | 20.0 | 30.0 |

Coherence compresses a $36\ \mathrm{dB}$ range of SNR into $[0.2,0.999]$, which is
why "coherence 0.9" is not "90 % good" but "$9.5\ \mathrm{dB}$ of SNR". Stating
the SNR is almost always more informative.

---

## ★3 — Delay from the phase slope

$$\tau = -\frac{\mathrm d\arg S_{yx}}{\mathrm d\omega}
= -(-0.19) = +0.19\ \text{samples}.$$

In seconds: $0.19\times\Delta t = 0.19/100 = 0.0019\ \mathrm{s} = 1.9\
\mathrm{ms}$.

**Convention.** The positive sign together with the lesson's verified relation
$\arg S_{yx} = -\omega\tau$ means the cross-spectrum was formed as
`scipy.signal.csd(x, y)` — the *first* argument is the leading (input) channel, and
`csd(y, x)` would give $+0.19$ per rad/sample and a delay of $-0.19$ under the
same formula. Always state which argument is the input and verify with a known
delay, because a sign flip is invisible in the magnitude and doubles the apparent
delay error in a two-way experiment.

---

## ★4 — Bias, correction and significance at $K = 16$, $\hat\gamma^{2} = 0.7$

**(a) Bias term.**

$$\frac{(1-\gamma^{2})^{2}}{K} = \frac{(1-0.7)^{2}}{16} = \frac{0.09}{16} = 0.005625 .$$

**(b) Bias-corrected value.**

$$\hat\gamma^{2}_{\text{corr}} = \frac{\hat\gamma^{2}K - 1}{K-1}
= \frac{0.7\times16 - 1}{15} = \frac{10.2}{15} = 0.6800 .$$

**(c) Significance threshold at $\alpha = 0.05$.**

$$c = 1 - \alpha^{1/(K-1)} = 1 - 0.05^{1/15} = 1 - 0.8190 = 0.1810 .$$

**Verdict.** $0.70$ is far above the threshold $0.181$, and the corrected value
$0.680$ is also far above it: the detection survives the correction comfortably.
The correction matters only when $\hat\gamma^{2}$ is comparable with $1/K$; here
it is a $2\%$ adjustment, and reporting it is a matter of discipline rather than
necessity. Contrast Example 1 of the lesson, where $K = 8$ and
$\hat\gamma^{2} = 0.35$ put the corrected value *below* the threshold.

---

## ★5 — Predicted transfer-function error at $K = 25$

$$\frac{\operatorname{std}\lvert\hat H\rvert}{\lvert H\rvert}
\approx\sqrt{\frac{1-\gamma^{2}}{\gamma^{2}K}} .$$

| $\gamma^{2}$ | 0.95 | 0.8 | 0.5 | 0.2 |
|---|---|---|---|---|
| relative error | 0.0459 | 0.1000 | 0.2000 | 0.4000 |
| SNR (dB) | 12.8 | 6.0 | 0.0 | $-6.0$ |

**Refusal threshold for a $10\%$ requirement.** Setting
$\sqrt{(1-\gamma^{2})/(25\gamma^{2})} = 0.10$ gives
$(1-\gamma^{2})/\gamma^{2} = 0.25$, i.e. $\gamma^{2} = 1/1.25 = 0.8$. So report
$\hat H$ only where $\hat\gamma^{2} \ge 0.8$ — but use the *bias-corrected*
coherence for the test, since with $K = 25$ the bias term is
$(1-\gamma^{2})^{2}/K = 0.04/25 = 0.0016$, small enough to ignore here.

**The scaling to quote.** Requiring $10\%$ accuracy at $K = 25$ needs a coherence
of $0.8$; halving the error requires quadrupling the coherence-to-noise ratio or
the number of averages. Since $K$ and $\gamma^{2}/(1-\gamma^{2})$ enter the
expression symmetrically, the two are interchangeable currencies — which is the
practical answer to "should I record longer or find a quieter site?".

---

## ★6 — Searching 100 bins

**(a) Naive use of the per-bin threshold.** A per-bin false-alarm probability
$\alpha = 0.05$ over $M = 100$ *independent* bins gives a family-wise probability

$$1-(1-\alpha)^{M} = 1 - 0.95^{100} = 1 - 0.00592 = 0.994 .$$

So a "significant" result is essentially guaranteed somewhere in the band whether
or not any relationship exists. The lesson's measured realisation of this effect:
with $K = 7$ the single-bin threshold $0.393$ was exceeded by the maximum over 31
bins in $100\%$ of 400 trials ($1-0.95^{31} = 0.796$ predicted).

**(b) Bonferroni correction.** Use $\alpha' = \alpha/M = 0.05/100 = 0.0005$ per
bin. For $K = 50$:

$$c_{\text{naive}} = 1 - 0.05^{1/49} = 0.059306, \qquad
c_{\text{Bonferroni}} = 1 - 0.0005^{1/49} = 0.143688 .$$

The threshold nearly triples. Bonferroni is conservative when the bins are
correlated (they always are, since adjacent bins share window energy), so the
*plan* should state the window's ENBW and count independent bins as
$M_{\text{eff}} \approx \text{bandwidth}/(\mathrm{ENBW}\times\Delta f)$, and
report the threshold for that count.

**The general rule.** A threshold is a property of the *search*, not of the
frequency. "Coherence 0.15 is significant" is meaningless without "at one
pre-selected frequency" or "as the maximum of a 100-bin search, with a
Bonferroni threshold of 0.144".

---

## ★7 — Designing a 0.02-sample delay measurement at 5 Hz

**Target.** $\sigma_\tau = 0.02$ samples at $f_{\text{dom}} = 5\ \mathrm{Hz}$.

**Naive scaling.** $\sigma_\tau \approx 1/(2\pi f_{\text{dom}}\sqrt{\mathrm{SNR}})$
gives $\sqrt{\mathrm{SNR}} = 1/(2\pi\cdot5\cdot0.02) = 1.5915$, i.e.
$\mathrm{SNR} = 2.53$ (4.0 dB) and $\gamma^{2} = \mathrm{SNR}/(1+\mathrm{SNR})
= 0.717$.

**Measured correction.** The lesson measured this prediction to be a factor
2.9 **optimistic** at 20 dB output SNR ($0.0046$ measured against $0.0016$
predicted). Applying the factor: to *achieve* $0.02$ you need the prediction to be
$\approx 0.02/2.9 = 0.0069$, i.e.

$$\sqrt{\mathrm{SNR}} = \frac{1}{2\pi\cdot5\cdot0.0069} = 4.61
\;\Rightarrow\; \mathrm{SNR} = 21.3\ (13.3\ \mathrm{dB})
\;\Rightarrow\; \gamma^{2} \ge 0.955 .$$

**Design.**

| element | choice | why |
|---|---|---|
| band | 4–6 Hz (or 2–8 Hz if dispersion is negligible) | $f_{\text{dom}}$ near 5 Hz; narrow enough that the phase ramp is linear |
| segment length | $\ge 10$ periods of the lowest frequency, i.e. $L \ge 10 f_s/f_{\min}$ | otherwise the phase estimate at the low edge is meaningless |
| number of segments | $K \ge 30$ (50 % overlap) | gives $\mathrm{dof} \approx 60$ and a usable $\gamma^{2}$ threshold ($\approx 0.095$) |
| required coherence | $\gamma^{2} \gtrsim 0.96$ in the band | from the corrected scaling above |
| estimator | phase slope of `csd(x, y)` over the band, weighted by $\gamma^{4}$, phase unwrapped | weights the informative bins |
| repeats | $R = (s/(0.02/\sqrt{?}))^2$ — concretely, run the estimator on independent realisations and stop when the standard error of the mean reaches $0.02$; with a per-realisation scatter of $s$ samples, $R \approx (s/0.02)^{2}$ | variance, not bias, is what repeats fix |

**Where the design is bias-limited.** If the two channels have different
antialias filters or different group delays (a real possibility with two
instruments), the phase slope contains a *systematic* offset that more repeats do
not remove. The measurement that reveals it: **swap the roles of the channels**
(`csd(y, x)` instead of `csd(x, y)`) with the same physical setup. A pure
propagation delay changes sign; an instrumental offset does not. Report both
numbers.

---

## ★8 — Three independent problems with the reported coherence

The claim: coherence 0.45 between two channels at $0.02\ \mathrm{Hz}$ from a
**single** cross-spectrum over a **50-second** record.

**Problem 1 — no averaging, so the estimate has 2 degrees of freedom and a bias
of 1.** With a single un-averaged cross-spectrum ($K = 1$ in the lesson's
notation, since the estimate is one complex number), the bias term is
$(1-\gamma^{2})^{2}/K = 1$ for incoherent signals — the estimate is
*uninformative*: any value in $[0,1]$ is consistent with no relationship. The
lesson's measured values at the smallest $K$ tested ($K = 7$) already show
$0.1481$ from unrelated signals, and the trend is $1/K$ all the way down to
$K = 1$, where the expected value is 1 regardless of the truth. The reported
$0.45$ therefore carries no evidence at all as computed.

**Problem 2 — the record is shorter than one period of the frequency quoted.**
$0.02\ \mathrm{Hz}$ has a period of $50\ \mathrm{s}$, and the record *is*
$50\ \mathrm{s}$: exactly one cycle, and depending on phase alignment possibly
less. The lesson's rule is that a segment must contain several (5–10) periods of
the lowest frequency analysed. At $10$ periods the record would need to be
$500\ \mathrm{s}$; the estimate at $0.02\ \mathrm{Hz}$ from a $50\ \mathrm{s}$
record is dominated by leakage from the mean and the trend, and any linear
detrending step would remove the component. The number $0.45$ at that frequency
is a property of the window and the record length, not of the channels.

**Problem 3 — no threshold, and no stated search.** Even if the analysis had been
done with averaging, quoting a coherence without the threshold leaves it
unfalsifiable: with $K = 8$ averages the $5\%$ threshold is
$1-0.05^{1/7} = 0.348$, so $0.45$ would be marginal; with $K = 4$ it is
$1-0.05^{1/3} = 0.632$, so $0.45$ would be *below* threshold; and if the value
was the largest over a band of, say, 50 bins, the family-wise probability of
exceeding the per-bin threshold is $1-0.95^{50} = 0.923$.

**The minimal defensible analysis.**

1. Extend the record to at least $500\ \mathrm{s}$ (10 periods at
   $0.02\ \mathrm{Hz}$), or move the analysis to a frequency the record can
   support — state which.
2. Segment the record into $K \ge 16$ half-overlapping segments of at least
   $10$ periods each (so $K = 16$ segments of 10 periods needs
   $16\times500\times0.5 \approx 4000\ \mathrm{s}$ of data, which is the honest
   price).
3. Report $\hat\gamma^{2}$, $K$, the bias-corrected value, the threshold
   $1-0.05^{1/(K-1)}$, and — if a band was searched — the Bonferroni-corrected
   threshold.
4. Report the phase and, if a delay is claimed, the delay with its uncertainty
   from the measured scaling (not from the optimistic formula).

Only then does "coherence 0.45" become a statement that another analyst can test.


---

## Mastery checkpoint answers

**(b)** $\hat\gamma^{2} = 0.7$, $K = 16$: bias term
$(1-0.7)^{2}/16 = 0.005625$; corrected value
$(0.7\times16-1)/15 = 0.680000$; significance threshold at $\alpha = 0.05$ is
$1-0.05^{1/15} = 0.1810$. The detection survives comfortably.

**(c)** The predicted relative error of the transfer function is

$$\sqrt{\frac{1-\gamma^{2}}{\gamma^{2}K}} = \sqrt{\frac{0.3}{0.7\times16}}
= \sqrt{0.026786} = 0.163663,$$

i.e. $16\%$ at that frequency.

**(d)** Testing whether *any* frequency in a 100-bin band is significant requires a
threshold corrected for the search: either the per-bin level
$\alpha' = \alpha/M$ (Bonferroni; for $K = 50$ the threshold rises from the naive
$0.0593$ to $0.1437$), or a statement of the family-wise rate. Using the naive
per-bin threshold over 100 bins gives a family-wise false-alarm probability of
$1-(1-0.05)^{100} = 0.9941$ — a "detection" is essentially guaranteed. Note also
that the bins are correlated through the window, so the *effective* number of
independent bins must be counted from the ENBW, not from the array length.
