# Exercises — 20-01-03 Convolution, Correlation and Filtering

Attempt these before reading the
[solutions](./03-convolution-and-filters-solutions.md). The lesson is
[03 Convolution, Correlation and Filtering](../03-convolution-and-filters.md).
**All models and data in this module are SYNTHETIC** teaching examples.

## ★ Foundational

**★1.** Convolve $x = [3, -1, 2]$ with $h = [1, 2]$ by hand. Give the output
length and verify the sum rule.

**★2.** A synthetic trace is white noise of $\sigma = 1.5$ plus a rectangular
pulse of amplitude $2$ lasting 32 samples. Write down the matched filter, compute
the attainable peak-to-rms gain, and express it in decibels.

**★3.** For $N = 64$ input samples and a kernel of $M = 7$, state the output
length for `full`, `same` and `valid`, and the indices of the input that are
affected when the FFT length is only 64 instead of $N+M-1$.

## ★★ Applied

**★★4.** Two identical Gaussian pulses of standard deviation $\sigma = 2$
samples are separated by $d$ samples in a noise-free synthetic trace.
Derive the condition on $d$ for the pair to appear as two resolved peaks
*(a)* in the raw trace and *(b)* after matched filtering, and evaluate both
numbers. State which criterion you used and why it is a convention rather than a
law of nature.

**★★5.** For a 5-point moving average, compute $\lvert H\rvert$ at
$\omega = 2\pi/5$, at $0.9\times2\pi/5$ and at $1.1\times2\pi/5$, and express
each in dB. Confirm the exact null algebraically. What does the result imply
about using a moving average to remove a sinusoid whose period is not an integer
number of samples?

**★★6.** A cross-correlation peak is used to estimate the delay between two
synthetic channels. The correlogram peak value is $r = 0.42$ times
$\lVert x\rVert\lVert y\rVert$, and the dominant frequency of the wavelet is
$12\ \mathrm{Hz}$ with a sample interval of $2\ \mathrm{ms}$. Estimate the delay
uncertainty from $\sigma_\tau \approx 1/(2\pi f_{\text{dom}}
\sqrt{\mathrm{SNR}})$, stating how you converted the correlation coefficient into
an SNR and why the answer is an order-of-magnitude guide rather than a
measurement.

## ★★★ Research-oriented

**★★★7.** Design a delay-estimation experiment between two synthetic channels
that must detect a $0.2$-sample delay at a confidence level you state. Include:
the input signal (bandwidth and duration), the estimator, the sub-sample
interpolation, the uncertainty formula, the null distribution (how you generate
it without assuming a delay exists), and the number of independent repeats
needed. Then specify the single experiment that would falsify your claimed
resolution.

**★★★8.** You inherit a convolution routine that produces a result 20 % too
large in rms and has a maximum error of 0.92 at the record ends. List, in the
order you would test them, the four hypotheses (reversal, padding, mode, length)
and give the *specific* diagnostic number from this lesson that identifies each
one. Then state which of the four properties of convolution would have caught
the bug in a unit test, and write that one-line test as pseudocode.
