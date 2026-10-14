# Exercises — 16-05-04 Downscaling: Statistical and Dynamical

Attempt these before reading the [solutions](./04-downscaling-solutions.md).
Lesson: [04 Downscaling](../04-downscaling.md). All models and data are
**SYNTHETIC**. The demonstration's numbers are reproduced by
[`../code/downscaling_demo.py`](../code/downscaling_demo.py).

## ★ Foundational

**★1.** A coarse box has mean elevation $h_c = 0.30\ \mathrm{km}$ and mean
temperature $T_c = 288.0\ \mathrm{K}$. Downscale to two fine points at
$0.05\ \mathrm{km}$ and $0.90\ \mathrm{km}$ using
$\Gamma = 6.0\ \mathrm{K\,km^{-1}}$.

**★2.** State the unit of every term in
$T_{\text{lapse}} = T_c + \Gamma(h_c-h_f)$ and check that the equation is
dimensionally consistent.

**★3.** A downscaling repeats the coarse box mean at every fine point inside the
box. Explain in one sentence why this cannot add within-box structure no matter
how it is post-processed.

## ★★ Applied

**★★4.** The demonstration reports a total fine-scale variance of
$6.3487\ \mathrm{K^{2}}$ and a residual variance after the lapse correction of
$0.0697\ \mathrm{K^{2}}$. Compute the fraction of the *total* fine-scale variance
removed by the correction, and compare it with the reported fraction of the
*raw residual* variance removed ($0.9538$).

**★★5.** A statistical downscaling is fitted in a training period as
$T_f = a + b\,T_c$, and in the target period the true relationship is
$T_f = a' + b'\,T_c$ with $a'$ chosen so that the two relations agree at the
training-period mean $\bar T_c$ (so $a' = a + (b-b')\bar T_c$). Derive the mean
bias of the downscaled product over the target period and state the condition
under which it vanishes.

**★★6.** The demonstration's hybrid method (coarse $T$ plus fine orography) has a
fitted orography coefficient of $-6.880\ \mathrm{K\,km^{-1}}$ against a true
$-6.500\ \mathrm{K\,km^{-1}}$, and an RMSE of $0.294\ \mathrm{K}$ against the
analytic lapse method's $0.229\ \mathrm{K}$. Explain why a method that recovers
approximately the right physics can be beaten by one that knows the physics
exactly.

## ★★★ Research-oriented

**★★★7.** Design an evaluation that would detect non-stationarity in a
statistically downscaled product *without* knowing the truth in the target
period. State the diagnostic, the data it needs, and what it can and cannot
conclude.

**★★★8.** Design a hybrid downscaling that combines a dynamical simulation with a
statistical correction of its residual. State what each component is expected to
supply, and how you would test that the statistical correction has not simply
absorbed the dynamical model's errors.
