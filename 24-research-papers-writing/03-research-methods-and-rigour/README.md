# Module 24-03 — Research Methods and Scientific Rigour

**Stages:** advanced → research · **Prerequisites:** modules
[24-01](../01-reading-research-literature/README.md) and
[24-02](../02-scientific-writing/README.md); the design lesson leans on
[21-08-01 Experimental Design](../../21-statistics-bayesian-ml/08-causal-inference-and-design/01-experimental-design.md).

This module is about the part of research that happens before and around the
writing: choosing a question that can be answered, stating hypotheses that forbid
something, committing to a design in numbers, keeping the analysis reproducible,
reviewing and being reviewed, and getting attribution right. Its organising idea is
that **rigour is a set of quantities, not a tone**. A question's specificity, a
design's power, the error rate that flexibility induces, the tolerance of a
reproducibility claim, the spread of a review panel and the dilution of an author
list are all measurable, and each lesson measures one of them.

The module's thread is the cost of ambiguity, in four places. A vague question is
consistent with many studies, and the unmade choices become someone's work later. A
hypothesis tested after seeing the data has already spent its error rate. A design
without a stated sample size cannot say what it will conclude. And a review panel's
score is partly a property of the panel, which is why a decision threshold and a
reviewer list both need stating. Each lesson reports the number rather than the
warning, because the number can be argued with.

Every quantitative result in this module is **SYNTHETIC**: questions are modelled as
binary content elements, experiments are simulated from the normal model, the
review panel and contribution matrices are generated, and the text-similarity
demonstration operates on a generated word sequence. No dataset, review record,
proposal or published paper is analysed. Where a lesson refers to a published
convention — the ICMJE authorship criteria, the CRediT contribution roles, the
Spearman-Brown relation, Bonferroni correction — it does so as a stated definition
and names the source in the text without reproducing it.

## Learning objectives

By the end of this module you will be able to:

1. **State** a research question with quantity, comparison and scope, and **compute**
   how many studies it is consistent with.
2. **Write** $H_0$, $H_1$ and a falsifier for a hypothesis, and **compute** the
   error rate that unstated analysis choices induce.
3. **Fix** a design in three numbers, **compute** the implied sample size, and
   **measure** what confounding and attenuation do to the estimate.
4. **Make** a reproducibility claim with a tolerance, **compute** a content digest,
   and **measure** the propagation of a parameter or environment change to the
   reported digits.
5. **Compute** an intraclass correlation for a review panel and **state** what
   aggregation and normalisation can and cannot fix.
6. **Choose** a similarity threshold with both of its error rates and **apply** a
   stated authorship criterion to a contribution matrix.
7. **Distinguish** plagiarism, self-plagiarism, redundant publication and
   insufficient attribution, and **name** each one's remedy.
8. **Assemble** the artefacts that make a project checkable: pre-registration,
   provenance block, contribution statement, and data and code availability.

## Prerequisites

- [24-01-03 Critiquing Methods, Data and Inference](../01-reading-research-literature/03-critiquing-methods.md) —
  the axes this module builds studies to satisfy.
- [24-02-03 Writing Methods Sections That Can Be Reproduced](../02-scientific-writing/03-writing-methods.md) —
  where the design's decisions are reported.
- [24-02-07 Self-Editing, Revision and Response to Reviewers](../02-scientific-writing/07-editing-and-revision.md) —
  the response side of peer review.
- [02-01-02 Measurement Uncertainty](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md) —
  what an error bar asserts.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Formulating Answerable Research Questions](01-research-questions.md) | advanced | $26.8\%$ of questions are fully specified; the mean question fits $3.7$ candidate designs; two raters agree at $\kappa = 0.45$ |
| 02 | [Hypotheses, Falsifiability and Testing in Earth Science](02-hypothesis-and-falsifiability.md) | doctoral | $64$ defensible choices turn a null result significant $96\%$ of the time; $20$ tests give a $64.2\%$ family-wise error rate |
| 03 | [Designing Observational, Experimental and Modelling Studies](03-study-design.md) | research | Power is bought quadratically; a $0.60$ confounder loading yields a slope of $+0.36$ from a true zero; reliability $0.6$ attenuates a slope to $0.60$ |
| 04 | [Reproducible Research Practice End to End](04-reproducible-research-practice.md) | research | A $1\%$ parameter change moves every reported value at four significant digits; one environment difference breaks some of them |
| 05 | [Peer Review: How to Do It Well and Receive It Well](05-peer-review-practice.md) | research | ICC $= 0.59$; within-proposal range $1.35$ points; normalisation changes $15\%$ of deciles and no reviewer level |
| 06 | [Research Ethics, Plagiarism, Authorship and Integrity](06-research-ethics.md) | graduate | Shingle similarity falls to $0.059$ where cosine stays at $0.908$; one gift author dilutes credit exactly as much as the loosest rule |

## Suggested path

**If you are planning a project:** 01 → 02 → 03, in that order. Write the question,
then the hypotheses and falsifiers, then the three numbers. Each step constrains the
next, and doing them in this order prevents the design from being chosen by what is
convenient.

**If you are finishing a project:** 04 → 03 §3–4. Write the reproducibility claim
and build the provenance block before you write the paper; the attenuation and
confounding checks are the two the discussion will have to address.

**If you are reviewing manuscripts:** 05 → 01 §4. The four-part report structure and
the question-answerability test are what make a review both useful and defensible.

**If you supervise or teach:** 02 §6 (the pre-analysis plan) and 06 §4 (the five
checkable practices) are the two artefacts worth requiring of students, because both
are records rather than promises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-research-questions.md`](01-research-questions.md) | Lesson 01 |
| [`02-hypothesis-and-falsifiability.md`](02-hypothesis-and-falsifiability.md) | Lesson 02 |
| [`03-study-design.md`](03-study-design.md) | Lesson 03 |
| [`04-reproducible-research-practice.md`](04-reproducible-research-practice.md) | Lesson 04 |
| [`05-peer-review-practice.md`](05-peer-review-practice.md) | Lesson 05 |
| [`06-research-ethics.md`](06-research-ethics.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/research_questions_demo.py`](code/research_questions_demo.py) | Element rates, candidate-design counts, two-rater $\kappa$, false-start cost |
| [`code/hypothesis_and_falsifiability_demo.py`](code/hypothesis_and_falsifiability_demo.py) | Null calibration, power versus effect size, flexibility error rate, multiplicity |
| [`code/study_design_demo.py`](code/study_design_demo.py) | Power curve, confounding with and without adjustment, attenuation table, the three design numbers |
| [`code/reproducible_research_practice_demo.py`](code/reproducible_research_practice_demo.py) | Result digest, determinism, parameter and environment propagation to the reported digits |
| [`code/peer_review_practice_demo.py`](code/peer_review_practice_demo.py) | Panel spread, variance decomposition and ICC, panel composition effect, normalisation |
| [`code/research_ethics_demo.py`](code/research_ethics_demo.py) | Two similarity measures versus paraphrase level, authorship thresholds, credit dilution |

## How to run the demos

```bash
cd 24-research-papers-writing/03-research-methods-and-rigour/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python research_questions_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hypothesis_and_falsifiability_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python study_design_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproducible_research_practice_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python peer_review_practice_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python research_ethics_demo.py
```

All six scripts are print-only, read no files, use no network, and run in well under
a second.

## Mastery checkpoint

1. Write your research question, mark its four elements, and state the design it
   implies.
2. Write $H_0$, $H_1$ and a falsifier, and count the analysis choices you have made
   since receiving the data; compute $1 - 0.95^{k}$.
3. Compute the sample size for your design at $80\%$ and $90\%$ power, and list the
   confounders you will measure.
4. Write the reproducibility claim, compute a digest, and list the inputs it covers.
5. Write a four-part review of a paper you have read this month.
6. Write your authorship criterion and a contribution statement for a current
   paper.

## Common pitfalls across this module

1. **Choosing the sample size from availability.** State the power the available
   resources buy, and the effect they can detect.
2. **Testing after seeing the data.** The flexibility table quantifies why the order
   matters.
3. **Claiming reproducibility without a tolerance.** The claim cannot fail, so it
   cannot be tested.
4. **Reporting four significant digits with unspecified parameters.** The
   demonstration shows a $1\%$ change moving every value.
5. **Treating an ICC as a validation.** Consistency is not correctness.
6. **Treating a similarity score as a finding.** It selects pairs to read.
7. **Deciding authorship at submission.** The record should be built as the work
   happens.
8. **Quoting these synthetic numbers as field norms.** Every table describes a
   teaching generator.

## Related modules

- [24-01 Reading the Research Literature](../01-reading-research-literature/README.md) —
  the reader's version of the critique this module builds studies to satisfy.
- [24-02 Scientific Writing](../02-scientific-writing/README.md) — where these
  decisions are reported.
- [24-04 Presentation and Science Communication](../04-presentation-and-communication/README.md) —
  presenting the result and its uncertainty to different audiences.
- [24-05 Theses, Proposals and Career Documents](../05-thesis-and-proposals/README.md) —
  proposing the work this module designs.
- [22-02 Reproducible Research Workflows](../../22-data-engineering-reproducibility/02-reproducible-workflows/README.md) —
  the tooling behind lesson 04.
- [21-08 Causal Inference and Experimental Design](../../21-statistics-bayesian-ml/08-causal-inference-and-design/README.md) —
  the statistical foundations of lesson 03.
