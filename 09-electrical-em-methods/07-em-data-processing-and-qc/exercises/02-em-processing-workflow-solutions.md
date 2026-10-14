# Solutions — 09-07-02 EM Processing Workflow and Data Editing

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All models are **SYNTHETIC**.

Lesson: [02 EM Processing Workflow and Data Editing](../02-em-processing-workflow.md).

---

## ★1 — Signal and timescale at five gates

$V = (t+t_0)^{-2.5}$ with $t_0 = 1.00\times10^{-4}$ s;
timescale $= (t+t_0)/p = (t+t_0)/2.5$; rule: filter length $\ll$ timescale,
taken here as at most one tenth of it.

| $t$ | $V$ | timescale $(t+t_0)/p$ | filter length from the rule |
|---|---|---|---|
| 0.10 ms | $1.7678\times10^{9}$ | 80.0 $\mu$s | $\le8\ \mu$s |
| 0.30 ms | $3.1250\times10^{8}$ | 160.0 $\mu$s | $\le16\ \mu$s |
| 1.00 ms | $2.4918\times10^{7}$ | 440.0 $\mu$s | $\le44\ \mu$s |
| 6.00 ms | $3.4409\times10^{5}$ | 2440.0 $\mu$s | $\le244\ \mu$s |
| 20.0 ms | $1.7459\times10^{4}$ | 8040.0 $\mu$s | $\le804\ \mu$s |

The timescale grows linearly in $t$, so a filter that is harmless late is
destructive early: one filter length cannot be defended for the whole record.
This is why window-by-window processing (or a time-varying filter) exists.

---

## ★2 — A small offset at late times

$2\%$ of the first sample is $0.02\times1.0000\times10^{10} =
2.000\times10^{8}$. The last sample of the demonstration's 40 ms record is
$3.106\times10^{3}$, so the offset is

$$\frac{2.000\times10^{8}}{3.106\times10^{3}} = 6.44\times10^{4}$$

times the signal at the end of the record — 64,400 times larger than the
quantity being measured. An interpreter who reads only the late gates therefore
reads the *offset*, not the formation, unless the drift has been removed. This is
the quantitative form of the statement that the offset is "invisible early and
fatal late".

---

## ★3 — A detector for additive, constant noise

With additive constant noise the natural statistic is the **absolute** residual

$$r_i = x_i - \operatorname{med}(x_{i-k/2..i+k/2}),
\qquad \text{flag if } |r_i| > c\cdot1.4826\,\mathrm{MAD}(r).$$

The relative residual of the lesson divides by the running median, which is
correct when the noise is multiplicative (so that the noise scale is set by the
signal) and **wrong** here: late in the record the median approaches the constant
offset, the denominator becomes noise-dominated and small, and the relative
residual is inflated for ordinary samples — a flood of false positives. The
choice of statistic must follow the noise model, and the noise model must be
stated.

---

## ★4 — Where the false positives are

With a global scale, 481 samples are flagged at $k=3$ against 6 true spikes. The
false positives concentrate at early times, where the decay changes by up to
$\sim50\%$ per sample and a running median of three samples therefore differs
substantially from the sample it is centred on: the **signal's curvature looks
exactly like a spike** to a median-based detector. Only a few of the flags lie in
the last three quarters of the record.

A **local** scale reduces the count (481 → 249 at $k=3$, 557 → 156 at $k=5$)
because the residual distribution is not stationary: the relative noise level
falls by orders of magnitude along the record, so a single MAD over the whole
record is dominated by the quiet late samples and sets a threshold far below the
normal residual amplitude early on. Estimating the MAD in a sliding window makes
the threshold follow the local noise.

---

## ★5 — Choosing a drift window

The latest usable gate is 6 ms. From the table, a window must extend well beyond
6 ms for the residual signal in it to be negligible compared with the drift. The
measured options:

| window (ms) | mean gate error | fitted exponent |
|---|---|---|
| 30–40 | 1.93% | 2.4328 |
| 20–40 | 2.48% | 2.4494 |
| 10–40 | 4.92% | 2.5158 |
| 4–40 | 16.03% | 2.9032 |

**Chosen window: 30–40 ms**, with a mean gate error of 1.93% (against an ideal
2.4126 exponent, the recovered 2.4328 is within 0.8%).

**Assumption:** that the signal is negligible compared with the drift inside
30–40 ms — justified here because the drift there is 644 times the signal.
**Falsification test:** fit the drift model in two disjoint windows (e.g. 30–35
and 35–40 ms) and compare the fitted slopes; if the two disagree by more than the
noise on the fit, the model is absorbing signal or the drift is not linear. The
residual criterion alone cannot detect this, because absorbing signal *reduces*
the residual.

---

## ★6 — Largest defensible filter length

Timescale at $t = 0.3$ ms is 160.0 $\mu$s and one sample is 19.54 $\mu$s, so the
largest filter is $m = 160/19.54 = 8.2$, i.e. $m = 7$ (odd, centred).

Measured boundary: the demonstration gives a gate-1 bias of $+7.6655\%$ at $m=9$
and $+33.0756\%$ at $m=17$, so the rule ($m\le7$) lands just inside the
$7\%$ regime. The rule is therefore not conservative by a comfortable margin: it
marks the boundary between "a few per cent" and "tens of per cent", and an
analyst who needs $1\%$ accuracy at the first gate must use $m\le3$, not $m\le7$.

---

## ★7 — A reproducible processing log

Model answer. Each line names the estimator, the parameter, the measured noise
reduction, the measured bias on the ideal record and the rejected alternatives.

| step | estimator | parameter | measured noise reduction | measured bias (ideal record) | rejected |
|---|---|---|---|---|---|
| 1 | band limiting / window | 40 ms record, 2048 samples | — | — | shorter record: no quiet window for the drift fit |
| 2 | relative-residual despiker | $k=5$, $c=6$, **local** MAD (window $\pm200$) | removes 6/6 spikes | mean gate error 1.03% | global MAD: 557 flags vs 156 (3.6× more false positives); $k=9$: more of the curved early record replaced |
| 3 | linear drift fit, subtracted | window 30–40 ms | not applicable | mean gate error 1.93% | 10–40 ms: 4.92% error; 4–40 ms: 16.03%; 0–40 ms: fits the signal, exponent undefined |
| 4 | centred moving average | $m=9$ | suppression ×4.681 ($\sqrt{m} = 3.000$) | gate-1 $+7.67\%$, gate-6 $+0.03\%$ | $m=17$: gate-1 bias 33.1%; $m=3$: suppression only 1.7× |
| 5 | arithmetic mean of repeats | $N=40$ | measured reduction 5.80 vs $\sqrt{N}=6.33$ | n/a (unbiased under stationarity) | median: pays a $\sqrt{\pi/2}$ efficiency penalty on clean data |
| 6 | 3-sigma clip, median-based scale | per gate | removes 3/40 contaminated repeats; error bar 0.345% → 0.368% | bias falls from $+1.75\%$ to $-0.004\%$ | clipping at 2.5σ: rejects clean samples, no accuracy gain |

The log is reproducible when another analyst can run the same steps in the same
order with the same parameters and obtain the same tables. The rejected
alternatives are not decoration: they are the evidence that the choices were
made against measurements.

---

## ★8 — Separating a poor receiver from a drifting instrument

Model answer. The two failure modes have different signatures in the *repeat*
structure and in the *record* structure.

**Statistic 1 — repeat scatter versus gate.** Compute the standard error of the
mean at each gate from the repeats. A receiver-limited record shows an error bar
that scales as $1/\sqrt{N}$ and is largest at late gates where the signal is
small in absolute terms. A drift-limited record shows a *bias* that is the same
in every repeat (so the standard error is small) and that grows systematically
with gate index.

**Statistic 2 — the two-block test.** Split the $N$ repeats into a first half and
a second half and compare their means at each gate. A drifting instrument shows a
difference between halves that is much larger than the combined standard error
and that is *monotone in gate index*; a noisy receiver shows a difference
consistent with the standard error and with no gate trend.

**Decision rule:** if |block difference| > 3 × (combined standard error) and the
difference is monotone in gate index over at least four consecutive gates,
diagnose drift; otherwise diagnose receiver noise. The monotonicity requirement
is what makes the test a drift test rather than a multiple-comparison generator.
The diagnostic is executable on any data set with several repeats and a gate
sequence.
