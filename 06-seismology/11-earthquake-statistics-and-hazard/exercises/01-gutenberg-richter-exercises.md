# Exercises — 06-11-01 Gutenberg-Richter, b-Value and Magnitude of Completeness

Attempt these before reading the
[solutions](./01-gutenberg-richter-solutions.md). The lesson is
[01 Gutenberg-Richter](../01-gutenberg-richter.md). All models and data in this
module are **SYNTHETIC**; the numbers below are chosen teaching values.

## ★ Foundational

**★1.** A synthetic catalogue has $N = 400$ events above $M_c = 2.0$, on a $0.1$
reporting grid, with mean reported magnitude $\bar m = 2.4821$. Compute the
Aki-Utsu estimate $\hat b$ and its standard error. State the unit of $b$.

**★2.** For $N = 250$ events above $M_c = 1.5$ with $b = 0.95$, compute the
expected largest event $M_c + \log_{10}N/b$, and the probability that the catalogue
contains no event above $M\,5.0$.

**★3.** Convert $M\,5.6$ to seismic moment (N m) and radiated energy (J), using
$\log_{10}M_0 = 1.5M + 9.1$ and $\log_{10}E = 1.5M + 4.8$. By what factor does the
energy change per magnitude unit?

## ★★ Applied

**★★4.** The demonstration's complete catalogue has $\bar m = 1.3817$ with
$N = 5000$ and $M_c = 1.0$ (grid $0.1$). (a) Reproduce $\hat b$ at $M_c = 1.0$.
(b) Reproduce $\hat b$ at $M_c = 0.5$. (c) Explain, without further arithmetic, why
the demonstration's table shows a large negative bias for $M_c$ assumed too low
and only a small positive bias for $M_c$ assumed too high.

**★★5.** In the detection-limited catalogue of the demonstration, maximum
curvature returns $M_c = 1.00$ with $N = 15206$ and $\hat b = 0.8662$, while the
99%-detection level $M = 2.00$ gives $N = 1851$ and $\hat b = 0.9935$. Compute the
standard error of each estimate and decide which of the two is consistent with
$b = 1.00$. State the conclusion in one sentence.

**★★6.** A study wants to detect a 10% difference in $b$ between two regions at
the 2-s.e. level. Assuming the statistical error dominates, how many events above
$M_c$ are needed in *each* region?

## ★★★ Research-oriented

**★★★7.** Derive the distribution of the largest event,
$P(M_{\max} < m) = \exp[-N\,10^{-b(m-M_c)}]$, and invert it to obtain the 5th and
95th percentiles as functions of $N$ and $b$. Evaluate both for $N = 5000$,
$M_c = 1.0$, $b = 1.0$ and compare with the demonstration's observed largest event.
State one consequence for "maximum magnitude" estimates from catalogues.

**★★★8.** Design an experiment that measures the b-value error caused by the
magnitude-binning convention. State the metric, the two catalogue constructions to
be compared, the predicted outcome with its derivation, and the control that makes
the comparison fair. A specification that could not be executed is a failed answer.
