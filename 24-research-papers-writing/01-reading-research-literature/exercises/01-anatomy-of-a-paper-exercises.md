# Exercises — 24-01-01 Anatomy of a Research Paper

Attempt these before reading the
[solutions](./01-anatomy-of-a-paper-solutions.md). The lesson is
[01 Anatomy of a Research Paper](../01-anatomy-of-a-paper.md). All models and
numbers are **SYNTHETIC** teaching values; the corpus parameters are those of the
accompanying demonstration.

## ★ Foundational

**★1.** A manuscript is $6400$ words long. The IMRaD body is $0.78$ of that, and
the sectional shares are $20.1\%$, $29.6\%$, $24.1\%$ and $26.2\%$ for
Introduction, Methods, Results and Discussion. Compute each section's word count
to the nearest $10$ words and check that the shares sum to $100\%$.

**★2.** In the demonstration corpus the Discussion holds $17.6$ references in
$1333$ words, and the Methods holds $6.8$ references in $1487$ words. Compute the
reference density of each in references per $1000$ words. Then state why both
differ from the reported median densities of $10.82$ and $4.81$.

**★3.** The corpus has a mean Discussion/Introduction word ratio of
$3.403 \pm 10.643$ and $62.7\%$ of papers have a longer Discussion than
Introduction. Explain why a mean ratio above $3$ is compatible with a large
minority below $1$, and name the statistic you would report instead.

## ★★ Applied

**★★4.** Using the means and standard deviations from the demonstration corpus,
treat the Introduction length $985 \pm 719$ words and the Discussion length
$1333 \pm 862$ words as two quantities and compute the mean and standard
deviation of their difference under the assumption of independence. Compare your
standard deviation with the measured $1091$ words and explain the sign of the
difference.

**★★5.** The generator draws manuscript length from a lognormal distribution
with median $6200$ words and log-scale standard deviation $\sigma = 0.34$. Compute
the theoretical mean, the standard error of the sample mean for $N = 400$ papers,
and decide whether the measured mean of $6387$ words is consistent with the
generator.

**★★6.** The demonstration reports that the Introduction and Discussion hold
$69.5\%$ of the citations in $46.5\%$ of the body words. Compute the ratio of the
citation share to the word share, and state what that ratio means physically.
Then compute the number of references the demonstration's median density implies
for a Methods section of $1487$ words.

## ★★★ Research-oriented

**★★★7.** Design a corpus study on $20$ papers from your own subfield that
measures sectional word shares and reference densities. State the metric, the
sampling rule, the confounds you must control (at minimum: article type, journal
policy, review-versus-research), and how you would separate author practice from
journal formatting rules. A design that could not be executed is a failed answer.

**★★★8.** The citation-share model of the demonstration assigns references to
*sectional word counts*, never to *claims*. Specify a study that would test
whether the references in an Introduction actually support the sentences that
carry them. State the unit of analysis, the sample size, the coding protocol for
"supports", the agreement statistic to be used, and the confound that
self-citation introduces.
