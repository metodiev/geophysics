# Exercises — 21-01-04 Linear, Multiple and Robust Regression

Attempt these before reading the
[solutions](./04-regression-solutions.md). The lesson is
[04 Regression](../04-regression.md). All fits are **SYNTHETIC**; numbers quoted
from the demonstration reproduce its output.

## ★ Foundational

**★1.** The clean OLS fit of the demonstration's gravity profile has
$\hat\beta_1 = 0.4989\ \mathrm{mGal/km}$ with standard error $0.0034$, $n = 100$,
$p = 2$, $\mathrm{RSS}$ implied by $s^{2} = 0.944\ \mathrm{mGal^{2}}$. Compute
the $t$ statistic for $\beta_1 = 0.5\ \mathrm{mGal/km}$ and the $95\ \%$
confidence interval for the slope.

**★2.** A multiple regression has a predictor whose auxiliary regression gives
$R_j^{2} = 0.99734$. Compute the VIF and by what factor it inflates the standard
error of $\hat\beta_j$. The demonstration measured VIF $= 375.5$; convert it the
same way and compare with the observed standard-error ratio of
$0.682/0.032$.

**★3.** For the demonstration's design ($x = 0,\dots,99$ plus $x = 120$, total
$n = 101$), show that the leverage of the added point is
$h_{ii} = 1/n + (x_i-\bar x)^{2}/\sum_j (x_j-\bar x)^{2}$ and evaluate it. Is it
above the $2p/n$ rule of thumb?

## ★★ Applied

**★★4.** Derive the normal equations by differentiating
$J(\beta) = (y-X\beta)^{\mathsf T}(y-X\beta)$ with respect to $\beta$ and
setting the gradient to zero. State the single condition on $X$ needed for the
solution to be unique.

**★★5.** For an observation with leverage $h_{ii} = 0.0651$, residual
$r_i = -4.9\ \mathrm{mGal}$ and $s^{2} = 0.944$, with $p = 2$, compute Cook's
distance and compare it with the threshold $4/n = 0.0396$. Would your next step
change if the point were a genuine measurement at a real station?

**★★6.** The Huber loss with $c = 1.345$ gives weights
$w_i = \min(|u_i|, c)/|u_i|$ where $u_i = r_i/s$. Compute the weights for
$u = 0.5$, $u = 1.345$ and $u = 3.0$, and show that they reduce continuously to
the least-squares value at $u = 0$.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that measures the **breakdown** behaviour of
OLS and of Huber regression as a function of the fraction of contaminated
points, using the demonstration's design. State the metric, the contamination
placement, the replicate count, and the prediction for the slope error at
$f = 0$, $0.1$ and $0.4$.

**★★★8.** Design a **cross-validated** comparison of OLS, Huber and a
least-absolute-deviations fit on a regression problem with heavy-tailed errors.
State the splitting scheme, the loss, the metric, and the way you would detect
that the robust methods are *worse* rather than better. A specification that
could not be executed is a failed answer.
