# Exercises — 22-07-01 Test Strategy for Numerical and Data Code

Attempt these before reading the
[solutions](./01-test-strategy-science-solutions.md). The lesson is
[01 Test Strategy for Numerical and Data Code](../01-test-strategy-science.md).
Numbers refer to the **SYNTHETIC** model of `code/test_strategy_science_demo.py`.

## ★ Foundational

**★1.** List the five kinds of claim a test can make about a numerical or data result, and
give one example of each for a gravity-inversion code.

**★2.** Using the lesson's cost table, compute the expected cost per defect for a third
strategy with discovery fractions 40 % unit, 30 % integration, 20 % acceptance, 10 % field,
and state whether it is better or worse than the "strong unit suite".

**★3.** State why line coverage can never be higher than a suite's defect-detection rate,
and what the gap between the two is called in the lesson's model.

## ★★ Applied

**★★4.** A function computes a gradient by a central difference with step $h$.

(a) State which error term dominates at $h = 10^{-2}$ and which at $h = 10^{-12}$.
(b) State the $h$ that minimises the total error for a central difference, and the
resulting error order, given that the truncation error is $O(h^2)$ and the round-off error
is $O(\varepsilon/h)$. (c) State the tolerance you would assert at the optimum for a
quantity of magnitude 1, and the one you would assert at $h = 10^{-12}$.

**★★5.** A suite has 4 000 lines, 92 % line coverage and 150 tests. One test file contains
40 assertions that check only that a function returns without raising.

(a) State the effect on the kill rate for statement-deletion mutants and explain why.
(b) State the two changes that would move the kill rate, using the lesson's per-class
table. (c) State what you would *not* do, and why.

**★★6.** A colleague proposes to raise the assertion tolerance from $10^{-9}$ to
$10^{-4}$ because the suite fails on a different machine.

(a) State the two possible causes of the cross-machine failure and how to distinguish them.
(b) State what the looser tolerance would stop detecting, with an example error class.
(c) State the change that keeps both the suite and its detection power.

## ★★★ Research-oriented

**★★★7.** Design the test suite for a new numerical kernel that solves a 1-D diffusion
equation on a variable-coefficient grid.

State: three exact assertions, two property tests, one metamorphic relation, one
convergence test, one golden regression test with its tolerance justification, and the one
defect class your suite cannot detect. Justify the tolerance of the golden value by
reference to a measured round-off floor.

**★★★8.** A group's suite has 97 % coverage, 3 000 passing tests, and a bug that reached a
publication.

Design the post-mortem analysis: how you would establish whether the code path was
executed, whether it was asserted on, whether the class of defect was present in the
mutation set, and what you would change in the suite. State the two outcomes of the
analysis and the different actions each implies.

**★★★9.** A reviewer argues that property-based and metamorphic tests are unnecessary
because "regression goldens catch everything".

Analyse the claim: state which defect classes goldens catch well, which they cannot catch,
why a golden cannot distinguish a correct refactor from a wrong one, and the platform or
dependency change that turns a golden suite into an alarm generator. State the evidence you
would produce to settle the argument in one afternoon.
