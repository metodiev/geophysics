# Exercises — 21-06-07 ML for Climate Downscaling and Emulation

Attempt these before reading the
[solutions](./07-climate-ml-solutions.md). The lesson is
[07 Climate ML](../07-climate-ml.md). All numbers are **SYNTHETIC**, printed by
[`code/climate_ml_demo.py`](../code/climate_ml_demo.py).

Setup to use: coarse 6 × 6, fine 18 × 18 (3 × 3 per coarse cell), 200 monthly
means, elevation 0–927 m, lapse rate 6.5 K/km west of $x = 0.5$ and 3.0 K/km
east of it, fine noise 0.15 K. Fitting uses the west half and months 1–150
(24 300 fine-cell-months). Mean coarse temperature 13.88 K (months 1–150) and
17.20 K (months 151–200).

RMSE in K (mean error in parentheses):

| method | in-sample | later period | other region | both shifts |
|---|---|---|---|---|
| bilinear interpolation | 1.169 (+0.160) | 1.186 (−0.296) | 0.754 (+0.158) | 0.781 (−0.296) |
| linear emulator | 0.166 (−0.000) | 0.193 (+0.036) | 0.558 (−0.001) | 0.564 (+0.037) |
| quadratic emulator | 0.160 (−0.000) | 0.277 (+0.096) | 0.556 (−0.001) | 0.597 (+0.097) |

Linear coefficients: intercept $-2.21876$, $T_c$ $+1.14830$, $\Delta z$
$-0.00647$ K/m.

## ★ Foundational

**★1.** Convert the fitted elevation coefficient into K/km and compare it with
the true western lapse rate. State the percentage error and explain why this
check is possible in a synthetic study and rarely in a real one.

**★2.** Compute the RMSE ratio between the other-region block and the in-sample
block for each of the three methods, and the ratio between the later-period block
and the in-sample block. State which transfer each ratio isolates.

**★3.** The fine noise is 0.15 K. For each method and each block, compute the
ratio of the RMSE to that floor and state which blocks are at the floor.

## ★★ Applied

**★★4.** The error in the east is not a bias: the mean error is $-0.001$ K while
the RMSE is 0.558 K. Derive the expected error for a cell with elevation anomaly
$\Delta z$ when the model applies a lapse rate $\Gamma_w = 6.5$ K/km where the
truth is $\Gamma_e = 3.0$ K/km, and compute the RMSE this predicts for a domain
whose elevation anomalies have a standard deviation of 120 m. Compare with the
measured 0.558 K.

**★★5.** Design the experiment that separates "the emulator extrapolates badly in
temperature" from "the emulator is over-parameterised". State the families, the
splits, the metric and the result pattern for each hypothesis.

**★★6.** Compute what fraction of a 3.32 K warming the training range already
covers, using the range of monthly coarse temperatures in months 1–150 versus
months 151–200. On that basis, explain why the temporal block is a modest
extrapolation rather than a severe one.

## ★★★ Research-oriented

**★★★7.** Design a study that would detect a regime-dependent lapse rate in real
data without knowing it is there. State the diagnostic, the data needed, the
confound with elevation-dependent biases in the input product, and the result
that would show the regime rather than the noise.

**★★★8.** Specify the downscaling validation protocol for a study whose
deployment target is a *future* period in a *new* region. State the blocks, the
metrics, the reference data, and the honest statement of what the protocol cannot
establish.

**★★★9.** You must report a single headline number for a downscaling model. State
which number you would choose, the three quantities you would print beside it,
and why a reader cannot interpret the headline without them.
