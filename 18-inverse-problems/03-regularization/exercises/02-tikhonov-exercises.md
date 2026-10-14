# Exercises — 18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off

Attempt these before reading the
[solutions](./02-tikhonov-solutions.md). The lesson is
[02 Tikhonov Regularisation and the Smoothing Trade-Off](../02-tikhonov.md).
All models are **SYNTHETIC**. The problem is in standard form: kernel divided by
$\sigma_1$, data divided by $\sigma_1\|m_{\mathrm{true}}\|$, so
$\hat\sigma_1 = 1$, $\hat\sigma_{64} = 8.599\times10^{-7}$ and the noise is
$\hat\sigma_e = 1.0169\times10^{-3}$ per datum.

## ★ Foundational

**★1.** Compute the filter factor $f_i$ at $\alpha = 10^{-4}$ for
$\hat\sigma_i = 10^{-2}$, $10^{-3}$ and $10^{-4}$. State which component is
closest to the crossover and what $\sum_i f_i$ means.

**★2.** For the same problem at $\alpha = 10^{-3}$, the demonstration lists 16
filter factors above $0.5$ and $\sum f_i = 16.009$. Explain in one paragraph why
those two numbers are close but not equal.

**★3.** Write the normal equations for $\|Km-d\|^2 + \alpha\|Lm\|^2$ with a
general $L$ and show that $m_\alpha$ is linear in $d$.

## ★★ Applied

**★★4.** Derive $\mathrm{d}\mathbb E\|m_\alpha-m_{\mathrm{true}}\|^2/\mathrm{d}\alpha$
and show that the optimum satisfies
$\sum_i f_i^2(1-f_i)x_i^2/\sigma_i^2 = \sigma_e^2\sum_i f_i^3/\sigma_i^4$.
Evaluate both sides numerically at $\alpha = 10^{-3}$ using
$f_i = \hat\sigma_i^2/(\hat\sigma_i^2+10^{-3})$ and the tabulated values
$x_1 = 8.118\times10^{-1}$, $x_3 = 5.582\times10^{-1}$,
$x_5 = 1.679\times10^{-1}$, $x_7 = 3.503\times10^{-2}$, and note that the sums
run over all 64 components.

**★★5.** At the oracle $\alpha = 5.623\times10^{-3}$ the demonstration reports
bias$^2 = 1.133\times10^{-4}$ and variance $= 4.089\times10^{-4}$. Compute the
predicted relative model error and compare it with the measured
$0.02269$. Then compute the same quantities at $\alpha = 10^{-6}$ (bias$^2 =
8.782\times10^{-9}$, variance $= 2.272$) and explain the sign of the change.

**★★6.** The $L=I$ solution at its best $\alpha$ has a point-spread spread of
$213\ \mathrm{m}$ and error $0.02220$; the $L=D$ solution has $305\ \mathrm{m}$
and $0.01175$. A colleague reports the $L=D$ result as "twice as accurate".
Write two sentences that state what is accurate, what was given up, and why the
comparison requires the same synthetic truth.

## ★★★ Research-oriented

**★★★7.** The variance formula assumes white noise. Derive the general
expression $\sum_{ij}f_if_j\,\mathrm{Cov}(e_i,e_j)/(\sigma_i\sigma_j)$ and show
that for a stationary noise process with spectrum $S_e(\omega)$ along a profile
it becomes an integral against $S_e$. State what the demonstration's correlated
noise experiment would have to measure for the optimum to be recomputed.

**★★★8.** Design a synthetic experiment that measures how the bias-to-variance
ratio at the optimum depends on the fitted degree of ill-posedness $q$
($q = 1.64$, $3.24$, $6.34$ from the depth control in lesson 01). Give the
statistic, the design, and the predicted direction of the effect.
