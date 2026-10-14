# Exercises — 21-06-05 ML-Based Denoising of Geophysical Signals

Attempt these before reading the
[solutions](./05-denoising-ml-solutions.md). The lesson is
[05 Denoising](../05-denoising-ml.md). All decibels are **SYNTHETIC** values
printed by [`code/denoising_ml_demo.py`](../code/denoising_ml_demo.py).

Measured SNR (dB) on 40 test traces:

| noise ratio | input | BP 30 Hz | BP 40 Hz | BP 60 Hz | BP 80 Hz | learned |
|---|---|---|---|---|---|---|
| 0.3 | $+10.18$ | $+2.45$ | $+6.17$ | $+12.72$ | $+12.14$ | $+12.07$ |
| 0.6 | $+4.15$ | $+1.92$ | $+4.72$ | $+7.17$ | $+6.07$ | $+5.96$ |

Additional measured quantities: a 30 Hz Ricker keeps **0.797** of its energy
below 40 Hz, **0.951** below 50 Hz and **0.993** below 60 Hz; white noise keeps
the fraction $f/f_{N}$ of its energy below a corner $f$, with the Nyquist
frequency $f_N = 125$ Hz. Sampling rate 250 Hz, trace length 1 000 samples,
dictionary rank 16 on patches of length 32.

## ★ Foundational

**★1.** Compute the change in SNR (in dB) delivered by every method at both noise
levels, and convert the 30 Hz band-pass result at noise 0.3 into a factor
by which the *error energy* increased relative to no processing.

**★2.** Using the measured signal-energy fractions and the white-noise fraction
$f/f_N$, predict the post-band-pass error energy and hence the SNR at noise 0.3
for the 40 Hz and 60 Hz corners. Compare with the measured values and state the
origin of any residual discrepancy.

**★3.** Compute the mean SNR over the two noise levels for the learned dictionary
and for the best band-pass, and state which method has the smaller spread between
the two noise levels. Express both spreads in dB.

## ★★ Applied

**★★4.** The dictionary is an orthonormal rank-16 basis on patches of length 32,
and it captures 0.999819 of the signal variance. Predict the SNR a projector onto
that basis would deliver at noise 0.3 if white noise retained the fraction
$K/L$ of its variance, and compare with the measured $+12.07$ dB. List the three
mechanisms that account for the difference.

**★★5.** Design the mismatched-dictionary experiment as a sweep: dictionaries
trained at 20, 25, 30, 35 and 40 Hz, applied to the same 30 Hz test traces. State
the metric, the plot, the predicted shape of the curve and the single number you
would quote from it.

**★★6.** The mean SNR is reported over 40 test traces. State the two sources of
sampling error in that mean — over traces and over patches — and explain which
one a bootstrap must resample if patches overlap with stride 8 on a length-32
window.

## ★★★ Research-oriented

**★★★7.** Design the experiment that decides whether the learned denoiser helps
a phase picker. State the metric pair, the control, the sizing, and the result
pattern that would show the denoiser helps the SNR but hurts the picking.

**★★★8.** In the field there is no clean reference trace. Specify three
substitutes for the clean reference, state what each can and cannot establish,
and say which one you would accept for a claim about *amplitude fidelity*.

**★★★9.** Design the experiment that detects amplitude distortion, i.e. that the
denoiser changes relative reflection amplitudes. Define the metric, the synthetic
truth needed, the confound with noise removal, and the sizing.
