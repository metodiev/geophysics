# Exercises — 01-13-02 Random Variables, PMFs, PDFs and CDFs

Attempt these closed-book before reading
[the solutions](./02-random-variables-solutions.md). The lesson is
[01-13-02](../02-random-variables.md).

Marking: ★ foundational, ★★ applied, ★★★ research-oriented.

For every continuous problem, state whether the quantity you have computed is a
probability or a density, and give its units.

---

## ★ Foundational

**★1.** A count of events per year has a Poisson distribution with $\lambda = 2.5$.

(a) Compute $P(N = k)$ for $k = 0, 1, 2, 3$ to six decimal places.
(b) Verify that the values you computed are consistent with the mean and variance
both being $2.5$.

**★2.** A waiting time in years has an exponential distribution with rate
$\lambda = 2$ per year.

(a) Give the density, its units, and the value of the density at $x = 0.5$ yr.
(b) Compute $P(X < 0.5)$ and $P(X > 1)$.
(c) Compute the median waiting time.

**★3.** A random variable has CDF $F(x) = 1 - e^{-x/3}$ for $x \ge 0$. Compute
$P(1 < X < 4)$ and $P(X > 6 \mid X > 3)$.

**★4.** A discrete random variable takes values $1, 2, 3$ with probabilities
$0.2, 0.5, 0.3$. Write the CDF as a table, and find the smallest $x$ with
$F(x) \ge 0.7$.

---

## ★★ Applied

**★★5.** Let $X$ be uniform on $(0, 2)$ and let $Y = X^{2}$.

(a) Derive the density of $Y$, including the jacobian factor, and state its support.
(b) Verify that your density integrates to one.
(c) Compute $P(Y > 1)$ two ways: from the density of $Y$ and directly from the
distribution of $X$.

**★★6.** Earthquake magnitudes above a completeness threshold are modelled as
exponential with rate $\lambda = 2.0$ per magnitude unit in natural logarithms, and
radiated energy scales as $Y = 10^{1.5M}$.

(a) Derive the tail exponent of $Y$.
(b) Compute the median of $Y$.
(c) Decide, with a one-line argument, whether $E[Y]$ exists.
(d) Compute $P(Y > 100)$.

**★★7.** A non-negative random variable has CDF $F(x) = x/(1+x)$ for $x \ge 0$.

(a) Verify that this is a valid CDF.
(b) Find the quantile function $F^{-1}(u)$.
(c) Explain, in one sentence, how you would generate $10^{6}$ samples from this
distribution.
(d) Compute the median.

**★★8.** A quantity follows a Weibull distribution with shape $k = 2$ and scale
$\lambda = 10$ in the parameterisation $F(x) = 1 - e^{-(x/\lambda)^{k}}$.

(a) Write down the hazard rate.
(b) Is the hazard increasing, constant or decreasing? What does that mean
physically?
(c) Compute $P(X > 12 \mid X > 10)$ and compare it with the memoryless value.

---

## ★★★ Research-oriented

**★★★9.** Let $\ln X \sim \mathcal{N}(\mu, \sigma^{2})$, so $X$ is lognormal.

(a) Derive the median, the mean and the mode of $X$ in terms of $\mu$ and $\sigma^{2}$,
stating the moment generating function you use.
(b) Show that mode $<$ median $<$ mean for every $\sigma > 0$.
(c) Compute the fraction of the distribution that lies below the mean for
$\sigma = 1$ by evaluating the standard normal CDF, and compare with the simulated
value $0.307670$ reported in the lesson.

**★★★10.** Generalise the magnitude-to-energy transformation: let
$M \sim \text{Exp}(\lambda)$ and $Y = 10^{aM}$ for a positive constant $a$.

(a) Derive the density of $Y$ and show that it is a Pareto density with tail exponent
$\alpha = \lambda/(a \ln 10)$.
(b) Show that the density integrates to one for every $\alpha > 0$, so normalisation
never fails.
(c) Determine the condition on $\lambda$ and $a$ for $E[Y]$ to exist, and reconcile
it with the value $\alpha = 0.6667$ quoted in the lesson for $a = 1.5$ and $b = 1$.
(d) Explain why the density's normalisation and the existence of its mean can fail
independently, in one or two sentences.
