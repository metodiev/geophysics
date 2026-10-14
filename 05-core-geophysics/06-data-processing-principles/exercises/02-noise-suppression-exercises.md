# Exercises — 05-06-02 Noise Suppression: Stacking, Filtering, Median, KL Transform

Attempt these **closed-book** before opening the
[solutions](./02-noise-suppression-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Reference results from the lesson's measurements. Stacking, measured SEM over 40 000
realisations: 0.99218, 0.70472, 0.50141, 0.35395, 0.25136, 0.12575 for
$N = 1,2,4,8,16,64$ against $\sigma/\sqrt{N}$ = 1, 0.70711, 0.5, 0.35355, 0.25,
0.125. Median filtering: RMS vs truth 0.00221, 0.00290, 0.01343, 0.03363 with peak
retained 95.32, 95.32, 82.02, 62.09 % for windows 3, 5, 7, 11. Band-pass: noise
0.30410 → 0.01169 (26.02× reduction), wavelet peak −5.53 %, true wavelet energy
retained 99.18 %. KL/SVD at S/N 1.48: error vs truth 73.20, 44.72, 32.78, 29.74,
38.07, 49.19, 68.19 % for ranks 1, 2, 3, 4, 6, 10, 24. Deconvolution: min
$\lvert\hat w\rvert = 9.363\times10^{-19}$, 62 of 257 bins below the double-precision
floor, max $\lvert1/\hat w\rvert = 1.068\times10^{18}$, 512 of 512 samples non-finite
on the naive inverse; Tikhonov gains 1107.1066 (λ = 1e−4) to 0.0022 (λ = 30) with
leakage 1.741970 to 0.000024.

---

## ★ Foundational

**★1.** Derive $\sigma_S = \sigma/\sqrt{N}$ for a stack of $N$ traces, stating the
assumption used at each step.

---

**★2.** State the noise structure each of the following suits: stacking, median
filtering, band-pass filtering, KL filtering.

---

**★3.** A stack of 36 traces has a noise level of 0.05 mGal. What was the
single-trace noise?

---

**★4.** Write the Tikhonov operator and state its behaviour for
$\lvert\hat w\rvert \gg \lambda$ and $\lvert\hat w\rvert \ll \lambda$.

---

**★5.** Explain in one sentence why deconvolution is ill-posed rather than merely
ill-conditioned.

---

## ★★ Applied

**★★6.** A deconvolution is applied with $\lambda = 0.01$. The measured operator
noise gain is 10.7210 and the data noise is 0.00189 mGal-equivalent.

(a) Predict the leakage.
(b) The measured leakage is 0.013232. Explain the difference.
(c) What $\lambda$ would bring the leakage down to the data noise, and what does the
recovery column of the lesson say that costs?

---

**★★7.** A 60-trace CMP gather has coherent ground-roll noise that is identical on
every trace, plus independent random noise of 1.0 amplitude and a signal of amplitude
1.0.

(a) What does stacking 60 traces do to the random noise?
(b) What does it do to the coherent ground roll?
(c) Using the KL results, would SVD filtering help? Justify with the measured
numbers.

---

**★★8.** A band-pass filtered section retains 99.18 % of a wavelet's energy but the
peak has dropped 5.53 %.

(a) Explain how both can be true.
(b) State which number matters for (i) amplitude interpretation, (ii) energy or power
analysis.
(c) State what a *rectangular* pass band does that a tapered one does not, and why
the lesson's example is nevertheless a good outcome.

---

**★★9.** A spike-removal step uses a window of 11 samples on data whose shortest
event is 6 samples wide.

(a) Using the measured peak-retention figures, estimate the amplitude error.
(b) What window would you choose, and what is the cost?
(c) What would you measure to confirm the choice on real data?

---

## ★★★ Research-oriented

**★★★10.** Measure the *wavelet-distortion* cost of deconvolution as a function of
the regularisation parameter: convolve the recovered model back with the wavelet and
compare the result with the input data. Report the residual as a function of
$\lambda$ and explain the shape of the curve in terms of the bias–variance
trade-off.

---

**★★★11.** Design an experiment that determines the rank at which KL filtering
should be truncated *without* knowing the truth, using only the data. Candidates
include an elbow criterion on the singular-value spectrum, a cross-validation over
traces, and a criterion based on the noise level estimated from a signal-free
window. Report which you would trust, and why.

---

**★★★12.** The lesson's Tikhonov table shows leakage falling with $\lambda$ and
recovery falling with $\lambda$: both columns move monotonically. Construct a
*criterion* that selects a single $\lambda$ for a given dataset, implement it, and
demonstrate it on the lesson's synthetic data. State the criterion's assumptions and
its failure mode.
