# Exercises — 21-07-01 AR, MA, ARIMA and Their Interpretation

Attempt these before reading the
[solutions](./01-arima-models-solutions.md). The lesson is
[01 ARIMA Models](../01-arima-models.md). All numbers are **SYNTHETIC**, printed
by [`code/arima_models_demo.py`](../code/arima_models_demo.py).

Measured quantities: $n = 4000$, innovation standard deviation $1.0$;
$\hat\rho_1 = +0.7106$, $\hat\rho_2 = +0.5066$ for the AR(1); $\hat\rho_1 =
+0.4028$ for the MA(1); $\hat\rho_1 = +0.7565$, $\hat\rho_2 = +0.4521$ for the
ARMA(1,1); one-step-ahead MSE $0.9913$, mean-prediction MSE $2.0019$; random-walk
$\rho_1 = +0.996$ with first-difference $\rho_1 = +0.005$.

## ★ Foundational

**★1.** Using $\hat\varphi = \hat\rho_1 = 0.7106$, compute $\sigma^2$,
$\sigma$, $\rho_3$, the integrated correlation time $\tau_{\text{int}}$ and the
$1/e$ decay lag. State the unit of each.

**★2.** Compute the one-step-ahead prediction standard error for the AR(1)
process, the theoretical $R^2$ of the one-step forecast, and the theoretical
variance reduction relative to predicting the sample mean. Compare with the
measured $0.9913$, $2.0019$ and variance reduction $0.5048$.

**★3.** Classify each of the following ACF patterns as AR, MA or non-stationary,
with one clause of justification: (a) $\rho_k$ decaying geometrically from
$0.996$ and no decay to zero over the record; (b) $\rho_1 = 0.40$, then $0.013$,
$0.013$, $0.011$; (c) $\rho_k = 0.75 \times 0.65^{k-1}$ for $k \ge 1$;
(d) $\rho_k$ decaying geometrically from $\rho_1 = 0.71$ with $\rho_2 = 0.51$.

## ★★ Applied

**★★4.** Derive $\sigma^2 = \sigma_w^2/(1-\varphi^2)$ and $\rho_k =
\varphi^{|k|}$ from the AR(1) recursion by taking variances and then covariances
with $x_{t-k}$. State the stationarity condition used at each step.

**★★5.** The MA(1) moment equation is $\rho_1 = \theta/(1+\theta^2)$. Show that
the two roots multiply to 1, verify that with $\hat\theta = 0.5058$, and state
precisely what the invertibility convention asserts and what it does not.

**★★6.** Show that $\text{ARMA}(1,1)$ satisfies $\rho_k = \varphi\rho_{k-1}$ for
$k \ge 2$, write down $\rho_1$ in terms of $\varphi$ and $\theta$, and state the
two conditions under which the moment estimator fails.

## ★★★ Research-oriented

**★★★7.** Design the Monte Carlo experiment that measures the finite-sample bias
and standard error of the Yule-Walker AR(1) estimator for $\varphi = 0.7$ at
$n = 100, 200, 400, 1000, 4000$. State the number of realisations needed to
resolve the bias to $\pm 0.005$, and the prediction for the sign of the bias and
its dependence on $n$.

**★★★8.** Design the experiment that separates "the moment estimator is fragile"
from "the model is wrong". State the estimator, the data-generating process, the
metric, the sizing, and the result pattern that would distinguish the two.

**★★★9.** Design a test that distinguishes an AR(1) from an ARMA(1,1) using only
the sample autocorrelations. State the statistic, its null distribution, the
measured value for the ARMA series here, and the sample size needed to detect the
difference at three standard errors.
