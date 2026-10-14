# Exercises — 24-03-04 Reproducible Research Practice End to End

Attempt these before reading the
[solutions](./04-reproducible-research-practice-solutions.md). The lesson is
[04 Reproducible Research Practice](../04-reproducible-research-practice.md). All
numbers are **SYNTHETIC**.

## ★ Foundational

**★1.** State a reproducibility claim for a table of six numbers reported to four
significant digits, naming the four inputs the claim depends on.

**★2.** A pipeline produces the same six numbers on two runs from a clean checkout.
State what that establishes and what it does not.

**★3.** Compute a digest of the tuple $(1.0, 2.50, 3.125)$ after rounding to three
significant digits, and state why the digest is taken after rounding rather than
before.

## ★★ Applied

**★4.** Changing the window length by $1\%$ changes the reported digits of all six
results, with a largest relative change of $0.095\%$. Explain why a change of
$0.095\%$ can still alter the fourth significant digit, using a concrete value.

**★5.** A single environment difference of relative size $10^{-4}$ changes the
digits of $4$ of $6$ results in one run and $2$ of $6$ in another. Explain why the
count is not stable and what that implies for a claim of exact reproduction.

**★6.** A paper reports four significant digits. Compute how many parameters the
Methods section must specify in full for the claim to be supportable, given that
each unstated parameter has a plausible $1\%$ range and every parameter affects
every reported value.

## ★★★ Research-oriented

**★★★7.** Design a reproducibility check for a paper in your subfield: what you
would request, the order in which you would attempt reproduction, the tolerance you
would set, and what you would conclude from each of the three outcomes (exact
agreement, agreement within tolerance, disagreement).

**★★★8.** Specify a study that estimates the fraction of published results in a
subfield that are reproducible at two significant digits. State the sampling, the
outcome definition, the effort model (how many person-days per paper), and the two
ways the estimate is biased upward.
