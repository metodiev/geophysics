# Module 06 — Capstone Research Project

This module is a project *process*, not a subject: five lessons that take a research
study from a question to a defended result, each with the arithmetic that makes the step
checkable. The sequence is the one a real study follows, and each lesson's demo produces
an artefact the next lesson consumes.

## Lessons

| # | Lesson | The artefact it produces | Effort |
|---|--------|--------------------------|--------|
| [01](./01-capstone-design.md) | Designing an Original Research Study | a design brief with an effect size, a power calculation, a decision rule and a falsifier | 260 min |
| [02](./02-capstone-proposal.md) | Proposal, Literature Review and Methods Plan | a work breakdown with a critical path, a deadline probability and a risk-driven repair | 260 min |
| [03](./03-capstone-execution.md) | Data, Modelling and Uncertainty Analysis | a verified estimator, a statistical/systematic budget and a provenance log | 260 min |
| [04](./04-capstone-writeup.md) | Manuscript-Style Write-Up and Code Release | a result registry, an audited manuscript and a reproducible release | 260 min |
| [05](./05-capstone-defence.md) | Presentation, Defence and Peer Critique | a question-impact table, prepared answers and a peer critique | 240 min |

Each lesson has a companion pair under [`exercises/`](./exercises): a graded scaffold of
the lesson's quantitative step (★ recall, ★★ apply, ★★★ design/execute) and a worked
reference solution cross-checked against the demo's printed output.

## Demos

| Demo | What it prints |
|------|----------------|
| `capstone_design_demo.py` | minimum detectable effects and SNR for six candidate studies, a weighted screen, and rank stability under 500 perturbed weightings |
| `capstone_proposal_demo.py` | a 12-task PERT schedule, the critical path with per-task slack, Monte Carlo deadline probability, finish-date drivers, and two evaluated repairs |
| `capstone_execution_demo.py` | the headline number with a statistical/systematic split, first-order Sobol indices, an interval-coverage verification, and the value of improved precision |
| `capstone_writeup_demo.py` | a 10-entry result registry, a claim-by-claim recomputation with verdicts, derived-quantity and citation audits, and the defect summary |
| `capstone_defence_demo.py` | a question-by-question recomputation of the headline, swings in standard deviations, the dangerous questions, and the three numbers to know cold |

All demos are print-only, seeded with `np.random.default_rng(20261014)`, labelled
**SYNTHETIC**, use no network, write no files, exit 0, and run in at most about a second.

## How the five lessons chain

1. **Design** produces the numbers ($\Delta$, $\sigma$, $N$, SNR) that the proposal's
   schedule and the execution's budget inherit.
2. **Proposal** produces the plan and the dependency repair that protects the milestone
   the execution depends on: the synthetic validation.
3. **Execution** produces the verified estimator and the budget that the write-up must
   report without hiding the dominant assumption.
4. **Write-up** produces the registry and the audit, which is what the defence's
   question-impact table is computed from.
5. **Defence** produces the record of what the work survived, and the boundary statement
   of what it does not establish.

The single thread running through all five is the same discipline: **state the number,
state its uncertainty, and state what it depends on.** The design lesson measures
whether a number is detectable at all; the proposal lesson measures whether it will
exist in time; the execution lesson measures what it depends on; the write-up lesson
checks that the manuscript says exactly that; the defence lesson tests whether the
candidate can say it under questioning.

## How to study this module

1. Run each demo and read its output as the *artefact* of the lesson, not as an
   illustration: the schedule, the budget and the audit table are the deliverables.
2. Do the ★★ exercises: they reproduce the demo's key computations by hand, which is
   what makes the numbers yours rather than the demo's.
3. Do the ★★★ exercise with **your own** project — every one of them is written to be
   executed rather than described, and the sequence of five ★★★ items forms a complete
   capstone plan.
4. Keep the artefacts: the brief, the schedule, the registry, the audit and the
   question-impact table belong in the capstone repository, and each one is checked in
   the next lesson.

## Where this leads

This is the final module of the curriculum's project track. The technical depth it
assumes comes from the five doctoral projects of
[Module 05](../05-doctoral-projects/README.md), and the engineering practices from
[22 Data Engineering and Reproducibility](../../22-data-engineering-reproducibility/README.md).
After the defence, the natural continuation is the reproduction or extension of the
work by someone else — the exercise that
[25-05-05](../05-doctoral-projects/05-reproduce-published-result.md) practises on
another author's result.

## Prerequisites

The inference and numerical background of
[18 Inverse Problems](../../18-inverse-problems/README.md),
[21 Statistics, Bayesian Inference and Machine Learning](../../21-statistics-bayesian-ml/README.md)
and the reproducibility practices of
[22 Data Engineering and Reproducibility](../../22-data-engineering-reproducibility/README.md).
Python environment: `/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python`
(numpy, scipy, matplotlib, pandas, scikit-learn).
