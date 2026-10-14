# Exercises — 20-05-01 Stochastic Processes, Stationarity and Ergodicity

Attempt these before reading the
[solutions](./01-stochastic-processes-solutions.md). The lesson is
[01 Stochastic Processes](../01-stochastic-processes.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** An AR(1) process has $\varphi = 0.80$, driving-noise standard deviation
$\sigma_w = 1.0$ and sampling interval $\Delta t = 0.25\ \mathrm{s}$. Compute
$\sigma^{2}$, $\sigma$, $\rho_k$ for $k = 3$, the integrated time
$\tau_{\text{int}}$ and the $1/e$ decay time $\tau_{1/e}$. State the unit of
each.

**★2.** For the process of ★1 with a record length $T = 2000\ \mathrm{s}$,
compute $N_{\text{eff}}$, the standard error of the mean, and the naive value
$\sigma/\sqrt{N}$. By what factor does the naive value understate the error?

**★3.** A record from a generator reports a split-half mean difference of
$0.35$ and a split-half variance difference of $1.2$. The ensemble scatter of
each is $0.2$ and $0.3$ respectively. Which of the two statistics shows
non-stationarity, and on what basis?

## ★★ Applied

**★★4.** Starting from
$\operatorname{Var}(\bar x) = \frac{1}{N^{2}}\sum_{n,m}C(n-m)$, derive
$\operatorname{Var}(\bar x) \approx \sigma^{2}\tau_{\text{int}}/T$ and show that
for a continuous process with $C(\tau) = \sigma^{2}e^{-|\tau|/\tau_c}$ the
integrated time is $\tau_{\text{int}} = 2\tau_c$.

**★★5.** Design a measurement that would distinguish a stationary-and-ergodic
process from the random-offset process of §6 of the lesson. State the statistic,
the prediction for each case, and the number of realisations needed so the two
predictions differ by more than $5\sigma$.

**★★6.** The demonstration measures the scatter of the time average of the
AR(1) process over its ensemble as $0.1019$. Invert
$\operatorname{Var}(\bar x) = \sigma^{2}/N_{\text{eff}}$ to infer $N_{\text{eff}}$
from that measurement, and compare it with the value predicted from
$\tau_{\text{int}}$. Express the difference as a percentage and explain its sign.

## ★★★ Research-oriented

**★★★7.** Specify a Monte Carlo experiment that measures the bias of the sample
variance estimator $\hat\sigma^{2} = \frac{1}{N-1}\sum(x_n-\bar x)^{2}$ as a
function of $\varphi$, for $T/\tau_{\text{int}}$ fixed. State the metric, the
expected sign of the bias, and how you would separate the bias from the
estimator's scatter. A specification that could not be executed is a failed
answer.

**★★★8.** For exact $1/f$ noise the sum $\sum_k\rho_k$ does not converge and
$\tau_{\text{int}}$ is undefined. Propose a finite-band definition of an
effective sample count, state how it depends on the record length, and describe
the experiment that would confirm the dependence.
