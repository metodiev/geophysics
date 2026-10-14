# Exercises — 01-13-04 Common Distributions and Their Earth-Science Roles

Attempt these closed-book before reading
[the solutions](./04-distributions-solutions.md). The lesson is
[01-13-04](../04-distributions.md).

Marking: ★ foundational, ★★ applied, ★★★ research-oriented.

For each distribution you identify, name the **mechanism** that produces it as well
as the family.

---

## ★ Foundational

**★1.** Name the distribution family you would use, and say why, for each of the
following:

(a) the error in a levelling traverse accumulated from many small independent
sources;
(b) the time between successive earthquakes in a catalogue with a constant
recurrence rate;
(c) the permeability of a sandstone whose value is the product of grain size,
sorting and cementation factors;
(d) the length of rock fragments produced by repeated crushing;
(e) the largest flood in each of forty years at one gauging station.

**★2.** Events occur at a constant rate of $4$ per year. Compute the probability of
$0$, of at least $1$, and of exactly $3$ events in a year.

**★3.** The mean waiting time between events is $0.25$ yr under a Poisson process.
Write down the rate, and compute the probability that the next gap exceeds one year.

**★4.** For a lognormal variable with $\ln X \sim \mathcal{N}(0,1)$, compute the
median, the mean and the mode, and the fraction of the distribution lying above the
mean.

---

## ★★ Applied

**★★5.** The five largest values in a sample above a threshold of $20$ are
$100, 50, 40, 30, 20$. Estimate the tail exponent with the Hill estimator and state
the estimate to four significant figures.

**★★6.** For an exponential$(1)$ parent, consider the maximum $M_n$ of $n = 100$
observations.

(a) Compute $P(M_n \le 5)$ exactly.
(b) Using the shifted variable $y = 5 - \ln n$, compute the Gumbel approximation
$\exp\left(-e^{-y}\right)$ and compare it with (a). Explain in one sentence why the
shift $\ln n$ appears.

**★★7.** A Pareto variable has tail exponent $\alpha = 3$ and lower limit
$x_{\min} = 2$. Compute its mean and variance, and state which is the highest moment
that exists.

**★★8.** A tail exponent is estimated as $\hat\alpha = 2.4$ from the largest $5\%$
of a sample of $20\,000$ values spanning a range that the analyst believes is only
partially within the power-law regime. State two reasons the estimate may be biased,
and say what diagnostic would reveal the problem.

---

## ★★★ Research-oriented

**★★★9.** Derive the Poisson PMF as the limit of the binomial distribution with
$n$ trials of success probability $p = \lambda T/n$ as $n \to \infty$, stating at
each step which approximation is used. Then state one physical assumption of the
Poisson process that the derivation makes explicit.

**★★★10.** For i.i.d. $\text{Exp}(1)$ variables, derive the limit law of the
standardised maximum:

(a) write $P(M_n \le x) = (1-e^{-x})^{n}$;
(b) substitute $x = y + \ln n$ and expand $\ln(1-e^{-x})$ for large $n$;
(c) identify the limit and its mean, and say what the shift $\ln n$ represents
physically.

**★★★11.** (a) Show that if $X_1, \dots, X_k$ are independent lognormal variables —
so $\ln X_i \sim \mathcal{N}(\mu_i, \sigma_i^{2})$ — then their product is lognormal,
and give its parameters.
(b) Use (a) to explain in three sentences why the arithmetic mean of a permeability
field is not the parameter a flow calculation should use, and name the summary that
should be used instead.

**★★★12.** A colleague reports a power-law fit to a dataset of $5000$ observations
with $\hat\alpha = 1.8$, estimated from the largest $10\%$ of the sample, and uses it
to extrapolate a once-in-a-thousand-year event.

(a) State which moments of the fitted model exist.
(b) Explain what happens to a sample mean of this variable as the sample grows.
(c) Explain why the extrapolation is more sensitive to the assumed tail form than to
the estimated exponent.
(d) State what you would require before accepting the extrapolation.
