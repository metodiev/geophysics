# Module 21-09 — Ethical and Responsible Quantitative Practice

**Stages:** graduate → research · **Prerequisites:** modules 21-01, 21-07 and
21-08; a completed analysis to reflect on.

This module is about the obligations that come with producing a quantitative
result: reporting multiplicity honestly, stating an uncertainty that reflects the
whole measurement chain, and governing the data themselves. It is a short module
because it does not introduce new mathematics — every method used here has appeared
earlier — and a necessary one because the mathematics is where these failures hide.

The organising idea is that **a reported number carries claims that are not in the
number.** A $p$-value cannot reveal how many hypotheses were tested. An interval of
$\pm0.31$ mm cannot reveal a systematic offset shared by every observation. A
correctly anonymised count release cannot reveal whether anyone consented to it.
Each lesson makes one of these invisible claims measurable — the family-wise error
rate, the coverage of an interval, the disclosure risk and utility of a release —
and then states clearly what the measurement still cannot decide.

All models, data and numbers in this module are **SYNTHETIC**. Every demonstration
generates its own statistics, measurements or survey, seeds
`np.random.default_rng(20261014)`, prints labelled results with units, and reads
nothing from disk or network. No study, data set, institution, community or site is
described, and the governance frameworks named in lesson 03 are discussed at the
level of principle only: their details vary and must be checked against current
published guidance and against the requirements of the specific data holders
involved.

## Learning objectives

By the end of this module you will be able to:

1. Compute the family-wise error rate for $m$ tests and apply Bonferroni and
   Benjamini-Hochberg corrections, stating which error rate each controls.
2. Measure the power and false-discovery trade of both procedures when some
   hypotheses are true.
3. Quantify the inflation of the error rate and of the reported effect produced by
   optional stopping.
4. Separate statistical from systematic uncertainty, combine them, and choose the
   number of significant figures the combination supports.
5. Measure the coverage of a nominal interval under a correct model, an unmodelled
   systematic and a post-hoc selection, and explain why the reported number cannot
   distinguish them.
6. Write a limitations paragraph that names the quantity affected, the direction of
   the effect and, where possible, its size.
7. Compute disclosure risk and utility for an aggregated spatial release, and
   measure the cost of a $k$-anonymity threshold.
8. State which questions about a data release only an agreement with the data
   holders can answer, and list the elements such an agreement should contain.

## Prerequisites

- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../01-statistics-in-practice/03-resampling.md) —
  the Monte Carlo measurement of every rate in this module.
- [21-07-03 Statistical Spectral Analysis and Significance Testing](../07-time-series-and-forecasting/03-spectral-analysis-statistical.md) —
  multiplicity in a spectral setting, and the same arithmetic as lesson 01.
- [21-08-02 Causal Inference Methods and Counterfactuals](../08-causal-inference-and-design/02-causal-inference-methods.md) —
  the identification limits a limitations paragraph must name.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../04-machine-learning-fundamentals/03-model-assessment.md) —
  selection effects inside a modelling workflow.
- [23-01-03 Field Notebooks, Metadata and Data Provenance](../../23-field-methods-instruments/01-field-safety-and-planning/03-field-notebooks.md) —
  the provenance practice that makes a release auditable.
- [22-01-05 Licensing, Citation and Software Credit (CITATION.cff)](../../22-data-engineering-reproducibility/01-research-software-engineering/05-licensing-and-citation.md) —
  licensing as the technical expression of a data agreement.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Statistical Reproducibility, p-Hacking and Multiple Comparisons](01-reproducibility-statistical.md) | graduate | Twenty null tests reach $p < 0.05$ in $0.6280$ of experiments; optional stopping triples the level and returns $0.3724\sigma$ from a true zero |
| 02 | [Honest Reporting of Uncertainty and Limitations](02-reporting-uncertainty-ethics.md) | doctoral | Three protocols, one stated uncertainty of $\pm0.31$ mm, coverages of $0.9511$, $0.2837$ and $0.4533$ |
| 03 | [Data Ethics, Indigenous Data Sovereignty and Geoscience](03-data-ethics-geoscience.md) | research | Coarsening dominates suppression; $k = 10$ at 1 km retains $1.2\%$ of records, at 2 km retains $67.6\%$ |

## Suggested path

**If you have just finished an analysis:** lesson 01 first — count your tests and
state your stopping rule — then lesson 02 to write the uncertainty section.

**If you are supervising a project:** lessons 01 and 02, then the ★★★ exercises,
each of which specifies an audit or a pre-analysis plan that can be applied to a
draft.

**If you are planning a data release:** lesson 03, preceded by lesson 02 for the
reporting obligations that accompany it, and followed by the licensing practice in
[22-01-05](../../22-data-engineering-reproducibility/01-research-software-engineering/05-licensing-and-citation.md).

**If you are preparing a publication:** lesson 01 §4 (which decisions create hidden
multiplicity) and lesson 02 §4 (what a published row looks like under each
protocol) are the two sections most likely to change what you write.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-reproducibility-statistical.md`](01-reproducibility-statistical.md) | Lesson 01 — multiplicity, corrections and stopping |
| [`02-reporting-uncertainty-ethics.md`](02-reporting-uncertainty-ethics.md) | Lesson 02 — uncertainty budgets and honest reporting |
| [`03-data-ethics-geoscience.md`](03-data-ethics-geoscience.md) | Lesson 03 — disclosure risk, governance and sovereignty |
| [`exercises/`](exercises) | Graded exercises and worked solutions for all three lessons |
| [`code/`](code) | Three runnable demonstrations, one per lesson |

| Script | What it prints |
|---|---|
| [`code/reproducibility_statistical_demo.py`](code/reproducibility_statistical_demo.py) | Family-wise rates for no correction, Bonferroni and BH; power and FDR with true effects; the optional-stopping inflation and its effect-size artefact |
| [`code/reporting_uncertainty_ethics_demo.py`](code/reporting_uncertainty_ethics_demo.py) | Coverage, mean reported value and bias for three reporting protocols; the combined uncertainty and the significant-figure consequence |
| [`code/data_ethics_geoscience_demo.py`](code/data_ethics_geoscience_demo.py) | Occupancy, singleton cells, and the suppression-versus-retention table across cell sizes and $k$ |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproducibility_statistical_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reporting_uncertainty_ethics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_ethics_geoscience_demo.py
```

Every demonstration is print-only: no plots, no files, no network. Each seeds
`np.random.default_rng(20261014)`, prints labelled results with units under a
numbered-section banner, prints a `SYNTHETIC` provenance line, and exits 0. The
slowest is `reproducibility_statistical_demo.py` at about 0.9 s; the others take
under 0.4 s.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A paper reports a significant relationship at $p = 0.01$ with a stated uncertainty
> of $\pm 0.2$ units, from a survey whose data are released as a 1 km grid of
> household counts. **(a)** The methods mention 60 stations, four time windows and
> three processing variants. Compute the effective number of tests, the corrected
> threshold, and state whether $p = 0.01$ survives. **(b)** The record was extended
> until the correlation stabilised; state the additional inflation this introduces
> and the measured factor for a five-look design. **(c)** Their uncertainty budget
> contains only the internal scatter of ten observations, and an intercomparison
> suggests a $0.5$-unit scale offset; compute the combined uncertainty and restate
> the value to the correct number of significant figures. **(d)** Their 1 km release
> shows cells of one household, and a second release at 2 km is planned; state the
> disclosure risk, the control their current plan lacks, and the question their
> privacy metric cannot answer.
>
> Worked versions of (a)–(d) appear in the ★★★ exercises of lessons 01, 02 and 03.

## Common pitfalls across this module

1. **Reporting a selected result as if it were pre-specified.** Twenty null tests
   reach significance in $0.6280$ of experiments, and the maximum of five processing
   variants sits $0.35$ units above the truth — more than its own interval's
   half-width.
2. **Quoting the statistical error as the uncertainty.** A $0.40$ mm systematic
   against a $0.158$ mm statistical error understates the budget by a factor of
   $2.72$ and drops the interval's coverage to $0.2837$.
3. **Stopping when the result is significant.** The nominal $0.05$ becomes $0.1485$,
   and the reported effect is $0.3724\sigma$ when the truth is zero.
4. **Reporting more digits than the uncertainty supports.** The last digit of
   $10.00 \pm 0.31$ mm implies a precision the measurement chain cannot deliver.
5. **Treating a privacy metric as a governance decision.** Singleton counts and
   $k$-anonymity inform a release plan; consent, authority, sensitive locations and
   benefit-sharing are answered by agreement.
6. **Applying suppression release by release.** Overlapping releases can be
   differenced to recover suppressed counts.

## Related modules

- [21-01 Statistics in Geophysical Practice](../01-statistics-in-practice/README.md) —
  the estimators and tests whose reporting this module constrains.
- [21-07 Time-Series Modelling and Forecasting](../07-time-series-and-forecasting/README.md) —
  calibration and multiplicity in a temporal setting.
- [21-08 Causal Inference and Experimental Design](../08-causal-inference-and-design/README.md) —
  the identification limits that a limitations paragraph must state.
- [21-06 Machine Learning in Geophysics](../06-ml-in-geophysics/README.md) —
  leakage, shift and selection in the modelling workflow.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md) —
  the tooling that makes a reproducible claim checkable.
- [23-field-methods-instruments](../../23-field-methods-instruments/README.md) —
  the fieldwork practice that produces the provenance a release depends on.
