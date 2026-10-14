# Exercises — 01-13-09 Error and Uncertainty Propagation (Analytic and Monte Carlo)

Attempt these closed-book before reading
[the solutions](./09-error-propagation-solutions.md). The lesson is
[01-13-09](../09-error-propagation.md).

Marking: ★ foundational, ★★ applied, ★★★ research-oriented.

State at every step whether you are adding variances or standard deviations, and
whether the inputs are independent.

---

## ★ Foundational

**★1.** Three independent lengths are $100 \pm 1$ m, $200 \pm 2$ m and $50 \pm 0.5$ m.
Compute the total and its standard deviation.

**★2.** A ratio of two independent quantities has relative standard uncertainties of
$1\%$ and $2\%$. Compute the relative standard uncertainty of the ratio.

**★3.** A quantity is cubed, and the input has a relative standard uncertainty of
$2\%$. Compute the relative standard uncertainty of the cube.

**★4.** A velocity is computed as $v = d/T$ with $d = 100 \pm 1$ m and
$T = 10 \pm 0.05$ s, independently measured. Compute $v$, its relative standard
uncertainty, and its standard uncertainty in m/s.

---

## ★★ Applied

**★★5.** Two quantities each have standard deviation $2$ and correlation $\rho = 0.6$.
Compute the standard deviation of their difference. Then compute it for $\rho = -0.6$
and explain both results in one sentence each.

**★★6.** A quantity is $g = ab/c$ with relative standard uncertainties $1\%$, $3\%$ and
$2\%$ in $a$, $b$ and $c$, all independent. Compute the relative standard uncertainty
of $g$, identify the dominant contribution, and state how much the total would fall if
the dominant uncertainty were halved.

**★★7.** A Monte Carlo ensemble estimates a standard deviation. How many draws are
needed for the Monte Carlo standard error of that estimate to be $1\%$ of the value?
State the formula you use and its assumption.

**★★8.** For $Y = (r/r_0)^{3}$ with $r$ lognormal and relative standard deviation
$s = 0.1$, compute the exact relative standard deviation of $Y$ and compare it with the
first-order value $3s$. State the direction of the discrepancy.

---

## ★★★ Research-oriented

**★★★9.** Derive the first-order propagation formula

$$\operatorname{Var}\bigl(g(\mathbf{X})\bigr) \approx
\sum_{i}\left(\frac{\partial g}{\partial x_i}\right)^{2}\sigma_i^{2}
+ 2\sum_{i<j}\frac{\partial g}{\partial x_i}\frac{\partial g}{\partial x_j}
\sigma_{ij}$$

from a Taylor expansion, stating the three assumptions used. Write the result in
matrix form.

**★★★10.** Let $r$ be lognormal with median $r_0$ and relative standard deviation $s$,
so $\ln r \sim \mathcal{N}(\ln r_0, \sigma_L^{2})$ with
$\sigma_L^{2} = \ln(1+s^{2})$.

(a) Show that $(r_0/r)^{p} = e^{-pZ}$ with $Z \sim \mathcal{N}(0, \sigma_L^{2})$.
(b) Derive $E[(r_0/r)^{p}]$ and $\operatorname{sd}[(r_0/r)^{p}]$ exactly.
(c) Evaluate the relative standard deviation for $p = 3$ and $s = 0.5$, and compare
with $3s$.
(d) Explain in two sentences why the linearised budget is optimistic for this function,
and why that direction of error is the dangerous one.

**★★★11.** A shared systematic error affects every reading in a survey.

(a) Show that if two readings each consist of an independent part with variance
$\sigma_i^{2}$ and a shared part with variance $\sigma_B^{2}$, then
$\operatorname{Var}(X_2 - X_1) = 2\sigma_i^{2}$.
(b) Show that $\operatorname{Var}(X_1 + X_2) = 2\sigma_i^{2} + 4\sigma_B^{2}$.
(c) Explain in three sentences why the difference of two nearby measurements can be
far more informative than either measurement, and what must be argued physically
before the formula in (a) may be used.
