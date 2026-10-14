# Exercises — 21-07-02 State-Space Models and Kalman Filtering

Attempt these before reading the
[solutions](./02-state-space-solutions.md). The lesson is
[02 State Space](../02-state-space.md). All numbers are **SYNTHETIC**, printed by
[`code/state_space_demo.py`](../code/state_space_demo.py).

Model: $x_t = x_{t-1} + \eta_t$ with $q = 0.020\ (\text{unit})^2$ per epoch;
$y_t = x_t + \varepsilon_t$ with $r = 1.000\ (\text{unit})^2$; $n = 1000$;
$P_0 = 10\ (\text{unit})^2$.

Measured: RMSE raw $0.9792$, filtered $0.3757$, sample mean $1.4565$, improvement
$0.616$; $K_{\mathrm{ss}} = 0.1318$, first-epoch gain $0.9093$; log-likelihood
$-1473.2$; coverage $0.9410$. Mis-specified cases: $q$ 100× too large → gain
$0.7321$, RMSE $0.7488$, likelihood $-1781.6$; $q$ 100× too small → gain
$0.0140$, RMSE $0.7694$, likelihood $-1675.5$.

## ★ Foundational

**★1.** Run two epochs of the recursion by hand from $x_0^{+} = 0$,
$P_0^{+} = 10$, using $y_1 = 2.0$ and $y_2 = -0.5$. Report $x_1^{+}$, $P_1^{+}$,
$K_1$, $x_2^{+}$, $P_2^{+}$, $K_2$ and the two innovations.

**★2.** Compute $K_{\mathrm{ss}}$ from the closed form for $q/r = 0.02$ and for
$q/r = 1$, and state what each value means for how much of an innovation the
filter accepts.

**★3.** Compute the fractional improvements of the filtered state over the raw
measurement and over the sample mean, and state in one sentence why the sample
mean does so badly.

## ★★ Applied

**★★4.** Derive $K_{\mathrm{ss}} = (-q+\sqrt{q^2+4qr})/(2r)$ from the fixed-point
conditions, and show that $K \to 1$ as $q/r \to \infty$ and $K \to \sqrt{q/r}$ as
$q/r \to 0$.

**★★5.** Design the experiment that estimates $q$ and $r$ from the data by maximum
likelihood. State the parameterisation, the optimiser, the reported uncertainty of
each variance, and the diagnostic that would show the local-level model is
inadequate.

**★★6.** The demonstration reports an interval coverage of $0.9410$. Design the
experiment that would establish whether that deficit from $0.9500$ is real, and
state the sizing.

## ★★★ Research-oriented

**★★★7.** Design a study that separates instrument noise from real deformation in
a geodetic series using a local linear trend model. State the state vector, the
observation equation, the parameters to be estimated, the identifiability problem,
and the measurement that resolves it.

**★★★8.** Design the experiment that measures the cost of ignoring correlated
observation errors in the filter. State the generating process, the filter used,
the metrics, and the predicted direction of the failure for a positive
correlation.

**★★★9.** A published filtered series is quoted from its first epoch. Specify the
analysis needed to decide whether the first 20 epochs should be reported at all,
including the statistic, the threshold and the remedy.
