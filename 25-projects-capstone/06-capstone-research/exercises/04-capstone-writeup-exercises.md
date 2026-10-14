# Exercises — 25-06-04 Capstone: Manuscript-Style Write-Up and Code Release

Attempt these before reading the
[solutions](./04-capstone-writeup-solutions.md). The lesson is
[04 Capstone Write-Up](../04-capstone-writeup.md); all numbers are **SYNTHETIC** and
printed by [`code/capstone_writeup_demo.py`](../code/capstone_writeup_demo.py):

| Quantity | Value |
|---|---|
| registry | 10 values with units and provenance |
| claims audited | 12; 7 pass; 5 flagged (42%); 11 of 12 carry a registry reference (92%) |
| flags | wrong $z$ (3.29 against 3.922), variance share reported as 71% (true 63.94%), arithmetic slip (92% against 86.54%), untraceable claim, miscited figure |
| derived checks | quadrature $\sqrt{1.198^2+1.600^2} = 1.999$ km against $2.001$ km; Sobol indices sum to 0.991 |
| registry values | `H_mean` 35.04 km; `H_sd` 2.001; `H_sd_stat` 1.198; `H_sd_sys` 1.600; `S_k` 0.474; `S_t` 0.356; `n_accepted` 45; `n_requested` 52; `t_ps` 4.3493 s; `n_sched` 20000 |

## ★ Foundational

**★1.** State what every registry entry must carry and why each field is necessary for
the audit. Give the entry for the 95% interval of the headline number.

**★2.** Recompute the four derived quantities in the flags: the 95% interval with
$z = 1.96$ and with $z = 1.645$, the systematic share of the variance, and the
percentage of stations accepted. State which of the manuscript's values are right.

**★3.** Explain why "the systematic term is 71% of the variance" and "the systematic
term is 64% of the variance" can both look plausible, and what the 71% actually is
($1.600/2.001$).

## ★★ Applied

**★★4.** Classify each of the five flags into one of the four defect classes, and state
for each whether it would be caught by (a) reading the manuscript, (b) checking the
abstract against the results, (c) recomputing from the registry.

**★★5.** The citation audit reports that all three listed figures are never cited in the
claim list, and that one cited figure does not exist. Explain what each of the two
problems does to a referee's reading, and state which is the more serious.

**★★6.** The audit reports the quadrature check as $1.999$ km against a sampled
$2.001$ km. Compute the relative difference, state what the difference would look like
if the model were nonlinear, and explain why this check is worth automating.

**★★7.** Design the claim list for the abstract of a capstone manuscript in your field:
six sentences, each with its quantitative claim, its registry identifier(s) and the
Results item it restates. Then state which of the six you would expect an audit to flag
if the manuscript had been written from memory.

**★★8.** State what a code release must contain for a reader to reproduce this headline
number from scratch, and identify the one element whose absence would make the rest
useless. Justify the choice.

## ★★★ Research-oriented

**★★★9.** Write (a) the audit script's specification and (b) the release checklist for
your own capstone. The audit specification must state: how the registry is generated
from the analysis, the checks performed (value, derivation, quadrature, unit conversion,
tracing, citation), the tolerance policy for rounding at quoted precision, and how the
audit is run in continuous integration so that a stale registry fails the build. The
release checklist must cover environment, data statement, one-command reproduction,
tests, licence, citation and limitations. Then state the one failure mode your
specification does **not** catch, and what would catch it instead. A specification that
audits the manuscript against itself is a failed answer.
