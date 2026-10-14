# Solutions — 21-06-01 ML for Seismic Detection, Picking and Classification

> Read after attempting. Lesson:
> [01 Seismic ML](../01-seismic-ml.md). All rates are **SYNTHETIC** values
> printed by
> [`code/seismic_ml_demo.py`](../code/seismic_ml_demo.py).

---

## ★1 — Raw feature values

Using $x = 10^{\log_{10}x}$:

| Feature | noise raw | event raw | relative separation |
|---|---|---|---|
| STA/LTA ratio (dimensionless) | $10^{0.289} = 1.945$ | $10^{0.394} = 2.477$ | $+27.4\%$ |
| kurtosis (dimensionless) | $10^{0.461} = 2.890$ | $10^{0.538} = 3.455$ | $+19.6\%$ |
| 4–12 Hz / 0.5–2 Hz energy ratio | $10^{0.671} = 4.688$ | $10^{0.935} = 8.611$ | $+83.7\%$ |
| peak/RMS (dimensionless) | $2.903$ | $3.412$ | $+17.5\%$ |

The **band-energy ratio** separates the classes best in relative terms
($+83.7\%$), which is why its standardised coefficient ($+1.10$) is the largest
of the four. Note that the peak/RMS ratio is the *worst* single feature here even
though it is the statistic most often quoted in the field: it uses only the
largest sample, while the band ratio integrates the whole window.

---

## ★2 — Precision at three priors

$$P = \frac{\mathrm{TPR}\,\pi}
{\mathrm{TPR}\,\pi + \mathrm{FPR}\,(1-\pi)} .$$

**$\pi = 0.5$** (the demonstration's own balance):

- trigger at ratio 2.0: $0.880/(0.880+0.390) = 0.693$;
- learned at the 5% budget: $0.560/(0.560+0.040) = 0.933$.

**$\pi = 10^{-3}$:**

- trigger at ratio 2.0:
  $0.880\times10^{-3} / (0.880\times10^{-3} + 0.390\times0.999) = 8.80\times10^{-4}/
  3.9049\times10^{-1} = 2.254\times10^{-3}$;
- learned at the 5% budget: $5.60\times10^{-4} / 4.0520\times10^{-2} =
  1.382\times10^{-2}$.

**$\pi = 10^{-5}$:**

- trigger at ratio 2.0: $8.80\times10^{-6} / 0.39000 = 2.256\times10^{-5}$ —
  **one correct trigger per about 44 300 triggers**;
- learned at the 5% budget: $5.60\times10^{-6} / 0.04000 = 1.400\times10^{-4}$ —
  **one correct trigger per about 7 140 triggers**.

The 7.7-fold FPR reduction buys a 6.2-fold precision gain at a fixed TPR ratio;
the absolute numbers are still hopeless, which is why a detector's output is
never treated as a catalogue without association, coincidence and location
steps.

---

## ★3 — How many events is that?

$$\mathrm{SE}(p) = \sqrt{\frac{p(1-p)}{n}}
= \sqrt{\frac{0.770 \times 0.230}{100}} = \sqrt{1.771\times10^{-3}} = 0.0421 .$$

One event is $0.01$ of the TPR, so the reported $0.770$ itself has a granularity
of $0.01$ and a sampling error of $0.042$. A difference of $0.030$ between two
training runs is $0.7$ standard errors: **not resolvable**. Any claim about a
two-event difference in TPR at this test size is a claim about the seed.

---

## ★4 — The precision identity

Let $n_1$ be the number of event windows and $n_0$ the number of noise windows,
with $\pi = n_1/(n_0+n_1)$. Then

$$\mathrm{TP} = \mathrm{TPR}\,n_1, \qquad \mathrm{FP} = \mathrm{FPR}\,n_0,$$
$$P = \frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FP}}
= \frac{\mathrm{TPR}\,n_1}{\mathrm{TPR}\,n_1 + \mathrm{FPR}\,n_0}
= \frac{\mathrm{TPR}\,\pi}{\mathrm{TPR}\,\pi + \mathrm{FPR}\,(1-\pi)} .$$

For $\pi \ll 1$ the two terms $\mathrm{FPR}(1-\pi)$ and $\mathrm{FPR}$ differ by
a relative $10^{-3}$ at most, so

$$P \approx \frac{\mathrm{TPR}}{\mathrm{FPR}}\,\pi .$$

Check at $\pi = 10^{-3}$: for the trigger, $\mathrm{TPR}/\mathrm{FPR} = 0.880/0.390
= 2.256$, giving $2.256\times10^{-3}$ against the exact $2.254\times10^{-3}$
($+0.1\%$). For the learned classifier,
$0.560/0.040 = 14.0$, giving $1.400\times10^{-2}$ against the exact
$1.382\times10^{-2}$ ($+1.3\%$). The approximation is excellent while
$\mathrm{TPR}\,\pi \ll \mathrm{FPR}$.

---

## ★5 — A comparison protocol that can fail

**Held-out unit.** Stations, not windows. Split the network into contiguous
station groups (or by campaign), train on all groups but one, test on the held
one, and repeat. Windows from the same station are correlated through site
response, so a window-level split leaks.

**Metrics.** At a budget fixed *in advance* (say 1% FPR calibrated on training
noise only), report for each held-out group the TPR and the FPR, plus the
event prior. Add the precision at the field prior, since that is what a user
experiences.

**Test.** The comparison is **paired**: both detectors see exactly the same
windows, so their outcomes are correlated. For a fixed threshold, use McNemar's
test on the discordant windows (the windows where the two detectors disagree) —
that is the paired test for two classifiers on one test set. Aggregate over
stations with a paired signed-rank test on the per-station TPR differences. Do
*not* compare two independent binomial proportions: that discards the pairing
and loses most of the power, and it is the standard error of the difference that
decides significance, not the two marginal errors.

**Reported uncertainty.** A bootstrap that resamples *events* (not windows), so
that all windows of one event move together.

---

## ★6 — Predicting the STA/LTA ratio

For a short window of $n_s = 20$ samples and a long window of $n_l = 160$ samples
at $\Delta t = 0.01\ \mathrm{s}$, with the wavelet entirely inside both windows,

$$\rho \approx \frac{\sigma^2 + E_w/(n_s\Delta t)}
{\sigma^2 + E_w/(n_l\Delta t)} .$$

With $A = 3\sigma$, $f = 8\ \mathrm{Hz}$ and $E_w = 0.30A^2/f$,

$$E_w = 0.30 \times \frac{9\sigma^2}{8\ \mathrm{Hz}} = 0.3375\,\sigma^2\,\mathrm{s},
\qquad
\frac{E_w}{\sigma^2\Delta t} = 33.75\ \text{sample}.$$

$$\rho \approx \frac{1 + 33.75/20}{1 + 33.75/160}
= \frac{2.6875}{1.2109} = 2.219 .$$

The measured median is $2.477$, i.e. $12\%$ higher. The model treats the wavelet
energy as uniform across the short window, ignores the exact shape of
$E_w/f$ for a Ricker (the closed form is $3/(8\pi f)$ times the peak squared, not
$0.30/f$), and ignores the fluctuation of the noise average itself — the last of
which is why the *measured* statistic is a maximum over a noisy ratio, not a
ratio of expectations. Two lessons follow: the ratio of a *peak* statistic to its
median value differs by $O(10\%)$, and the STA/LTA ratio is not the peak-to-RMS
ratio — both windows contain the event, which caps $\rho$ far below $A/\sigma$.

---

## ★★★7 — The gain-versus-SNR experiment

**Design.** Sweep peak-to-RMS $\in \{2, 3, 4, 6, 8\}$. For each value, draw
$R = 100$ independent window populations of the same size as the demonstration
(600 windows, 400 train / 200 test, 100 test events). For each population,
compute
$$\Delta \mathrm{TPR} = \mathrm{TPR}_{\mathrm{ml}}(5\%) -
\mathrm{TPR}_{\mathrm{trig}}(5\%),$$
with both thresholds calibrated on that population's *training* noise windows so
that the budget is 5% by construction.

**Metric.** Report $\overline{\Delta\mathrm{TPR}} \pm \mathrm{SE}$ against
peak-to-RMS, where $\mathrm{SE} = \mathrm{sd}(\Delta\mathrm{TPR})/\sqrt{R}$.

**Sizing.** At fixed budget the per-realisation $\Delta\mathrm{TPR}$ has a
standard deviation of order $0.05$ (each TPR is a proportion on 100 events).
To resolve a change of $0.02$ in the mean you need
$\mathrm{SE} \le 0.02/3 = 0.0067$, i.e.
$R \ge (0.05/0.0067)^2 \approx 56$. Use **$R = 100$** per point; that gives
$\mathrm{SE} \approx 0.005$ and a $3\sigma$ resolution of $0.015$.

**Seed policy.** One `np.random.default_rng(20261014)`; derive one child seed per
(SNR, realisation) pair so that the *same* populations are reused across
detectors (paired) and the SNR points are independent.

**Confound to hold constant.** The classifier sees the trigger ratio as one of
its four features, so at high peak-to-RMS the trigger saturates first and the
measured gain conflates "more features" with "the trigger being at its ceiling".
Fix the feature set, the training-set size and the wavelet frequency across the
sweep, and additionally report the gain of a classifier trained *without* the
trigger ratio to separate the two effects.

---

## ★★★8 — Cascading two stages

With independence, the two-stage detector has

$$\mathrm{FPR}_{\mathrm{tot}} = 0.390 \times 0.140 = 0.0546, \qquad
\mathrm{TPR}_{\mathrm{tot}} = 0.880 \times 0.770 = 0.678 .$$

That is close to the single-stage learned classifier at a 5% budget
(0.040, 0.560): the cascade spends 5.5% instead of 4.0% of noise to keep 0.678
instead of 0.560 of events. For a low-prior application with a fixed alarm
budget, the cascade is one legitimate way to buy TPR — but not a free one, and it
costs a second model to maintain.

**Why independence fails.** The classifier's features *include* the STA/LTA
ratio, so both stages fail on the same windows: a noise burst that fools the
ratio usually fools the classifier too. The true joint FPR is then larger than
$0.0546/0.0546$ predicted by the product, and the joint TPR is larger than the
product as well, because the classifier's errors are a subset of the trigger's.

**Measurement.** On the same held-out windows, build the $2\times2$ table of the
two decisions and compare the observed $\mathrm{FPR}_{\mathrm{tot}}$ with the
independence prediction $0.0546$; report the phi coefficient (or Yule's $Q$)
between the two binary decisions. A strongly positive association is the failure
signature, and the observed joint rates are the only honest summary of the
cascade.

---

## ★★★9 — Mislabelled training windows

**Direction.** Mislabelling 5% of *event* windows as noise removes the hardest,
lowest-peak-to-RMS positives from the training set. The fitted boundary becomes
more conservative, so:

1. the AUC **decreases** slightly — the removed events were the ones the model
   most needed in order to rank weak events above noise;
2. the TPR at a fixed 5% budget **decreases** by more than the AUC does, because
   the budget fixes the FPR and the boundary then retreats from the weak-event
   region.

The AUC is a global ranking average dominated by the many easy pairs, which is
why it barely moves; the fixed-budget TPR is a local property of the boundary,
which is why it moves first. This is the same asymmetry that makes AUC a poor
proxy for a deployed detector.

**Experiment.** (i) Choose the 5% at random among event windows whose
peak-to-RMS lies in the *lowest* quartile, so that the corruption is not
detectable by a simple amplitude filter. (ii) Retrain, and evaluate AUC and
TPR-at-5%-budget on a *clean* held-out set whose labels are untouched.
(iii) Repeat over 20 training seeds and report the mean and standard error of
both changes. (iv) Run the mirror corruption — 5% of *noise* windows labelled as
events — to confirm that the two corruptions move the metrics in opposite
directions, which is the evidence that the effect is caused by the label and not
by the retraining noise.
