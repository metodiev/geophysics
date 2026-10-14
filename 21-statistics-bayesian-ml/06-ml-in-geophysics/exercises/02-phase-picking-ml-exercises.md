# Exercises — 21-06-02 Deep-Learning Phase Picking: SeisBench and Beyond

Attempt these before reading the
[solutions](./02-phase-picking-ml-solutions.md). The lesson is
[02 Phase Picking](../02-phase-picking-ml.md). All numbers are **SYNTHETIC**
values printed by
[`code/phase_picking_ml_demo.py`](../code/phase_picking_ml_demo.py).

Measured on 200 test records (true pick at 1.50 s):

| Statistic | 10 dB STA/LTA | 10 dB learned | 4 dB STA/LTA | 4 dB learned |
|---|---|---|---|---|
| bias | $+0.002\ \mathrm{s}$ | $-0.180\ \mathrm{s}$ | $+0.061\ \mathrm{s}$ | $+0.029\ \mathrm{s}$ |
| MAE | $0.342\ \mathrm{s}$ | $0.568\ \mathrm{s}$ | $0.927\ \mathrm{s}$ | $0.917\ \mathrm{s}$ |
| scatter (1 s.d.) | $0.635\ \mathrm{s}$ | $0.777\ \mathrm{s}$ | $1.062\ \mathrm{s}$ | $1.040\ \mathrm{s}$ |
| within $\pm0.05\ \mathrm{s}$ | $0.475$ | $0.090$ | $0.060$ | $0.045$ |
| within $\pm0.10\ \mathrm{s}$ | $0.740$ | $0.345$ | $0.180$ | $0.135$ |

## ★ Foundational

**★1.** Convert every error above into samples at 100 Hz sampling, and give the
count of test records inside $\pm0.05\ \mathrm{s}$ for the two 10 dB pickers.
Compute the ratio MAE/scatter for all four columns and state what a value below
1 means.

**★2.** The learned picker's label window is 20 samples wide and starts at the
true onset. Express the measured 10 dB bias in samples, compare it with the
window width and with half the window width, and state in one sentence what that
comparison implies about the maximum precision the label convention allows.

**★3.** Compute, for each signal-to-noise level, the difference in MAE between
the two pickers as a percentage of the smaller value. State at which level the
comparison discriminates the two methods and at which it does not.

## ★★ Applied

**★★4.** Assume the residuals of the 10 dB STA/LTA picker are Gaussian with the
measured bias and scatter. Predict the fraction inside $\pm0.05\ \mathrm{s}$ and
compare it with the measured 0.475. Then fit a two-component mixture — a
"good-pick" component concentrated within $\pm0.05\ \mathrm{s}$ and a
"gross-error" component spread over the tail — and estimate the weight of the
good component. State what the failure of the Gaussian model tells you about the
residual distribution.

**★★5.** Design an experiment that separates the label-window bias from the
waveform-limited bias, sweeping the label window width
$W \in \{10, 20, 40\}$ samples. State the metric, the plots, the prediction under
the hypothesis "bias scales with $W$", and the prediction under the competing
hypothesis "bias is set by the wavelet half-width".

**★★6.** The event is a symmetric wavelet. Explain, using the concept of
near-indistinguishable half-windows, why the measured 10 dB bias
($-18$ samples) exceeds half the label window (10 samples), and state what added
information would be needed to remove the ambiguity.

## ★★★ Research-oriented

**★★★7.** You switch the reference picker to offset regression on the same
features and records. Specify the experiment that measures whether the bias
disappears, including the target definition, the loss, the metric and the sample
size needed to resolve a residual bias of $0.01\ \mathrm{s}$ at 10 dB.

**★★★8.** Design the transfer test for a pretrained picker applied to a new
network. Name the strata, the metrics, the reference labels, the split, and the
one result that would justify *not* deploying it. State what the test cannot
establish.

**★★★9.** A tolerance fraction of $0.475$ is measured from 200 records. Give
its binomial standard error, and compute how many records are needed to state
the same fraction to $\pm0.005$. Then state why a binomial interval is *too
narrow* for picks that share a common event and a common noise field, and what
resampling unit you would use instead.
