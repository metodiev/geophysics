# Exercises — 21-01-01 Descriptive Statistics, Robust Measures and Outliers

Attempt these before reading the
[solutions](./01-descriptive-statistics-solutions.md). The lesson is
[01 Descriptive Statistics](../01-descriptive-statistics.md). All data are
**SYNTHETIC** teaching values; where a question quotes a number from the
demonstration, that number is reproduced exactly.

## ★ Foundational

**★1.** A porosity sample of seven values is
$\{4.1,\,5.2,\,4.8,\,5.0,\,5.3,\,4.9,\,120.0\}$ in per cent. Compute (a) the
mean, (b) the median, (c) the $1$-of-$7$ trimmed mean. State the unit and, for
each, whether it is a location estimate of the mean or of the median.

**★2.** For the same sample compute the standard deviation with $n-1$ in the
denominator and the MAD, then rescale each to a Gaussian scale (divide the IQR
by $1.349$ and the MAD by $0.6745$). By what factor do the two estimates of
$\sigma$ disagree?

**★3.** The demonstration's clean sample has mean $49.012\ \%$, median
$49.060\ \%$ and standard deviation $9.866\ \%$ with $n = 200$. Compute the
standard error of the mean and state whether the median's departure from $50\ \%$
is consistent with sampling error at one standard error.

## ★★ Applied

**★★4.** Derive the exact shift of the sample mean produced by replacing $k$
values $x_1,\dots,x_k$ with a constant $c$, and use it to verify the
demonstration's $+7.325\ \%$ for $k = 10$, $c = 200\ \%$, $n = 200$. Then derive
the corresponding statement for the median and explain why no formula with the
magnitudes of $c$ appears.

**★★5.** The demonstration reports that one value at $2000\ \%$ raises the
standard deviation to $138.55\ \%$ and that the classical $z$-score then finds
only $1$ of the $5$ planted spikes. Compute the classical $z$-score of a spike at
$120\ \%$ in a clean sample with mean $50\ \%$ and standard deviation $10\ \%$,
and again after the single $2000\ \%$ value is added, and show that the threshold
$3.5$ is crossed in the first case but not the second.

**★★6.** The demonstration measures $\mathrm{sd}(\bar x) = 0.7267\ \%$ and
$\mathrm{sd}(\tilde x) = 0.8886\ \%$ on clean Gaussian data with $\sigma = 10\ \%$
and $n = 200$. Compute the theoretical values $\sigma/\sqrt n$ and
$\sqrt{\pi/2}\,\sigma/\sqrt n$, and express the discrepancy of each as a
percentage. State which discrepancy should be smaller and why.

## ★★★ Research-oriented

**★★★7.** Specify a Monte-Carlo experiment that measures the *efficiency* of a
$10\ \%$ trimmed mean relative to the mean and the median, as a function of the
contamination fraction $f \in [0, 0.4]$ and the outlier magnitude. State the
metric, the number of ensembles needed to resolve a $2\ \%$ efficiency
difference, and the prediction at $f = 0$. An experiment that could not be
executed is a failed answer.

**★★★8.** A laboratory reports assay values in which, unknown to the analyst, a
$2\ \%$ fraction of samples are contaminated by a systematic dilution. Design the
diagnostic that would reveal this, state which summary statistics it moves and by
how much (in units of the clean standard deviation), and state what the test
cannot conclude. Give a specification, not a general discussion.
