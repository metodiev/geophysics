# Exercises — 01-13-03 Expectation, Variance and Moments

Attempt these closed-book before reading
[the solutions](./03-expectation-variance-solutions.md). The lesson is
[01-13-03](../03-expectation-variance.md).

Marking: ★ foundational, ★★ applied, ★★★ research-oriented.

Carry units through every answer. State explicitly when a result depends on an
independence assumption.

---

## ★ Foundational

**★1.** A discrete random variable takes values $0, 1, 2$ with probabilities
$0.5, 0.3, 0.2$. Compute $E[X]$, $E[X^{2}]$ and $\operatorname{Var}(X)$.

**★2.** For $X \sim \text{Exp}(\lambda)$, state $E[X]$, $\operatorname{Var}(X)$ and
$E[X^{2}]$, and verify that $E[X^{2}] - (E[X])^{2}$ reproduces the variance.

**★3.** Given $\operatorname{Var}(X) = 4$, compute $\operatorname{Var}(3X - 2)$ and
the standard deviation of $3X - 2$.

**★4.** Independent measurements have standard deviations $\sigma_1 = 0.1$ and
$\sigma_2 = 0.2$. Compute the standard deviation of $Y = 2X_1 + 3X_2$.

---

## ★★ Applied

**★★5.** A joint distribution is given by $P(X = 0, Y = 0) = 0.4$,
$P(X = 0, Y = 1) = 0.1$, $P(X = 1, Y = 0) = 0.2$, $P(X = 1, Y = 1) = 0.3$.
Compute $E[X]$, $E[Y]$, $E[XY]$, $\operatorname{Cov}(X,Y)$ and the correlation
coefficient. Then compute $\operatorname{Var}(X + Y)$ directly from its definition
and check it against $\operatorname{Var}X + \operatorname{Var}Y + 2\operatorname{Cov}$.

**★★6.** Repeated readings of an anomaly have single-reading standard deviation
$0.5$ mGal.

(a) How many readings give a standard error of $0.02$ mGal?
(b) Now suppose every reading shares a calibration error with standard deviation
$0.08$ mGal. What is the smallest achievable standard error of the mean? Find the
number of readings at which the noise contribution has fallen to the same size as
the calibration contribution, and state in one sentence what further readings buy
after that point.

**★★7.** Each reading is $X_i = \mu + B + \varepsilon_i$ with shared bias variance
$\sigma_B^{2} = 0.04\ \mathrm{mGal^{2}}$ and reading-noise variance
$\sigma_\varepsilon^{2} = 0.64\ \mathrm{mGal^{2}}$. Compute the standard error of
the mean for $n = 64$ readings, and compare it with the value a careless analyst
would report from the noise term alone.

**★★8.** Two quantities each have standard deviation $2$ and correlation
$\rho = 0.7$. Compute the standard deviation of their difference. Explain in one
sentence why the answer is smaller than $\sqrt{8}$.

---

## ★★★ Research-oriented

**★★★9.** Let $X_1, \dots, X_n$ be identically distributed with variance
$\sigma^{2}$ and constant pairwise correlation $\rho$.

(a) Derive $\operatorname{Var}(\bar X) = \dfrac{\sigma^{2}}{n}
\left[1 + (n-1)\rho\right]$.
(b) Find the limit as $n \to \infty$ and interpret it.
(c) Define the effective sample size $n_{\text{eff}}$ as the number of independent
observations with the same variance as $\bar X$, and compute it for $n = 100$,
$\rho = 0.05$ with $\sigma = 0.2$.
(d) State the practical consequence for a survey whose stations are correlated over
a length of about ten stations.

**★★★10.** Let $X \sim \text{Uniform}(a, b)$ with $0 < a < b$.

(a) Compute $E[1/X]$ by integration.
(b) Compute $1/E[X]$.
(c) Show that $E[1/X] > 1/E[X]$, and identify the inequality from which this
follows.
(d) Evaluate both for $a = 1$, $b = 3$ and state the relative size of the Jensen
gap.
