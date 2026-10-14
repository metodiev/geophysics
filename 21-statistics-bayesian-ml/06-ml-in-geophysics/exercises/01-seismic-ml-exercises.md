# Exercises — 21-06-01 ML for Seismic Detection, Picking and Classification

Attempt these before reading the
[solutions](./01-seismic-ml-solutions.md). The lesson is
[01 Seismic ML](../01-seismic-ml.md). Every rate below is a **SYNTHETIC**
teaching value printed by
[`code/seismic_ml_demo.py`](../code/seismic_ml_demo.py).

The demonstration's held-out measurements, needed for several items:

| Detector | Operating point | test FPR | test TPR |
|---|---|---|---|
| STA/LTA | fixed ratio 2.0 | 0.390 | 0.880 |
| STA/LTA | ratio 2.66 (5% training budget) | 0.090 | 0.280 |
| logistic regression | probability 0.5 | 0.140 | 0.770 |
| logistic regression | score 0.773 (5% budget) | 0.040 | 0.560 |
| logistic regression | score 0.886 (1% budget) | 0.020 | 0.340 |

The test set holds 200 windows, 100 of them containing an event.

## ★ Foundational

**★1.** The feature medians are quoted as $\log_{10}$ values: noise
$+0.289$, event $+0.394$ for the STA/LTA ratio; $+0.461$, $+0.538$ for the
kurtosis; $+0.671$, $+0.935$ for the band-energy ratio. Convert all six to the
raw values, state the unit of each, and say which feature has the largest
relative separation between the two classes.

**★2.** Using the table above, compute the precision at an event prior of 0.5,
0.001 and $10^{-5}$ for the STA/LTA trigger at ratio 2.0 and for the learned
classifier at the 5% budget. Present the results as "one correct trigger per
$N$ triggers" at the smallest prior.

**★3.** The learned classifier's TPR at probability 0.5 is $0.770$ on 100
events. Compute the binomial standard error of that proportion, and state
whether the difference between $0.770$ and the $0.740$ you would obtain from a
second training run on the same window count is resolvable.

## ★★ Applied

**★★4.** Derive the precision identity
$P = \mathrm{TPR} \cdot \pi / (\mathrm{TPR}\cdot\pi + \mathrm{FPR}\cdot(1-\pi))$
from the definitions of TPR, FPR and Bayes' rule. Then show algebraically that
at small $\pi$ the precision is approximately
$(\mathrm{TPR}/\mathrm{FPR})\,\pi$, and check the approximation against your
★2 numbers at $\pi = 10^{-3}$.

**★★5.** You must compare two detectors on a real network. Specify the split
(which unit is held out), the metrics, and a test that decides whether the
difference in TPR at a fixed false-positive budget is real. State explicitly
what makes the test paired rather than independent.

**★★6.** The STA/LTA ratio at the event can be estimated analytically. Take a
short window of $n_s = 20$ samples and a long window of $n_l = 160$ samples at
100 Hz, noise variance $\sigma^2$, and a wavelet whose total energy is
$E_w = 0.30\,A^2/f$ with peak amplitude $A$. Using $A = 3\sigma$ and
$f = 8\ \mathrm{Hz}$, predict the peak ratio and compare it with the measured
median of $2.477$.

## ★★★ Research-oriented

**★★★7.** Design a Monte Carlo experiment that measures how the TPR gain of
the learned classifier over the trigger at a 5% false-positive budget depends on
the event peak-to-RMS ratio. Fix the metric, the number of realisations needed
so that the gain is resolved to $\pm 0.02$, the seed policy, and the confound
that must be held constant. A specification you could not execute is a failed
answer.

**★★★8.** A station triggers $N_{\mathrm{trig}}$ times per day with the
classical trigger alone. Add the learned classifier as a second stage and
compute the combined FPR and TPR, stating the independence assumption you used.
Estimate how the assumption fails for two detectors built on *the same* four
features, and propose a measurement that would detect the failure.

**★★★9.** A training set has 5% of its event windows mislabelled as noise.
Predict the direction of the change in (i) the AUC and (ii) the TPR at a 5%
budget, and specify the experiment that would measure both, including how you
would construct the mislabelling so that it is not trivially detectable.
