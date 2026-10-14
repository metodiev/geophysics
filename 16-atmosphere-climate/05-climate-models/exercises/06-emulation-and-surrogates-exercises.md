# Exercises — 16-05-06 Emulators and Surrogate Models for Climate

Attempt these before reading the
[solutions](./06-emulation-and-surrogates-solutions.md). Lesson:
[06 Emulators and Surrogate Models](../06-emulation-and-surrogates.md). All
models and data are **SYNTHETIC**. The demonstration is
[`../code/emulation_and_surrogates_demo.py`](../code/emulation_and_surrogates_demo.py).

## ★ Foundational

**★1.** Write the Gaussian-process predictive mean and variance conditional on a
single training point $(x_1, y_1)$ with RBF kernel amplitude $\sigma_f^{2}$,
length scale $\ell$ and noise $\sigma_n^{2}$. Evaluate both at $x = x_1$ and as
$|x-x_1|\to\infty$.

**★2.** The demonstration reports an emulator RMSE of $0.0830\ \mathrm{K}$ inside
the training range and $3.2512\ \mathrm{K}$ outside. Compute the ratio and state
in one sentence what it measures.

**★3.** The linear surrogate $\Delta T = F/0.8$ gives $7.5000\ \mathrm{K}$ at
$F = 6.0\ \mathrm{W\,m^{-2}}$ where the model gives $4.3290\ \mathrm{K}$. Compute
the absolute and relative error.

## ★★ Applied

**★4.** With amplitude $\sigma_f = 1.0\ \mathrm{K}$ and length scale
$\ell = 2.0\ \mathrm{W\,m^{-2}}$, compute the prior covariance between two inputs
separated by $4.0\ \mathrm{W\,m^{-2}}$, and state what fraction of the prior
variance that is.

**★5.** The demonstration's step-response emulator has a mean absolute error of
$0.6944\ \mathrm{K}$ in the unsampled window and a mean stated standard deviation
of $0.0605\ \mathrm{K}$. Compute the width of the nominal $95\%$ interval and
express the actual error as a multiple of it.

**★6.** You may add five training points to a design that has no points within
$0.6\ \mathrm{W\,m^{-2}}$ of a known transition at $F = 4.0\ \mathrm{W\,m^{-2}}$.
State where you would place them and what you would expect to change in (i) the
RMSE away from the transition and (ii) the error-to-uncertainty ratio there.

## ★★★ Research-oriented

**★★★7.** Compare a Gaussian-process emulator with a fitted cubic polynomial as
surrogates for the nonlinear response of the demonstration. State which you would
trust for interpolation, which for extrapolation, and what you would report
alongside each prediction.

**★★★8.** A study uses an emulator to project warming and reports the emulator's
predictive standard deviation as the uncertainty of the projection. Write a
critique identifying the quantities that are missing, and state what would have
to be true for the reported uncertainty to be the total uncertainty.
