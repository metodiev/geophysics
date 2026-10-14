---
id: 00-01-05
title: "Research Milestones from Beginner to Independent Investigator"
level: beginner
prereqs: ["00-01-01"]
estimated_minutes: 40
tags: [study-method, research, milestones, careers]
---

# Research Milestones from Beginner to Independent Investigator

## Learning objectives

- Explain what distinguishes a research *milestone* from a stage checkpoint:
  milestones are artefacts that other people can examine.
- List the six milestones that carry a learner from reproducing textbook results
  to designing an original study.
- Write a milestone for your own work in the form "artefact + evidence +
  external check".
- Recognise the transitions where learners most often stall, and what to do at
  each.

## Prerequisites

[The Six Stages and Their Mastery Checkpoints](./02-six-stages.md) defines the
stages; this lesson defines the *research artefacts* that mark movement through
them. Read [How to Learn Geophysics](./01-how-to-learn-geophysics.md) first if
you have not.

## 1. A milestone is an artefact, not a feeling

A stage checkpoint says what you should be able to do. A milestone says what you
should have **made**, and how someone else can tell that you made it.

The difference matters because the failure mode of self-directed study is a
gradual drift into believing you can do things you have never done. Milestones
are immune to that, provided they satisfy three conditions:

1. **Artefact.** There is a thing: a script, a figure, a notebook, a report, a
   manuscript, a dataset, a review.
2. **Evidence.** The artefact records what was done, with what data, and with
   what assumptions — not only the final number.
3. **External check.** Someone or something outside you can test it: a benchmark
   with a known answer, a published figure to reproduce, a colleague who reads
   the code, a reviewer who reads the manuscript.

An example of a bad milestone: "understand seismic tomography". An example of a
good one: "reproduce a published tomographic resolution test on synthetic data,
recover the input anomaly from at least two different damping choices, and write
two pages stating which features the data constrain and which they do not."

## 2. The six research milestones

The milestones below are cumulative. They are not tied to a calendar; they are
tied to evidence.

### M1 — Reproduce a textbook result from first principles

**Artefact:** a derivation written from memory and a script that computes the
same quantity numerically.
**Evidence:** the analytic and numerical results agree to the expected order.
**External check:** a known closed-form solution, or a textbook figure whose
values you can read off and compare.
**Typical curriculum point:** the intermediate stage, e.g. the wave-equation
checkpoint in [02-physics/03-oscillations-and-waves](../../02-physics/03-oscillations-and-waves/README.md).

This milestone proves you can *derive* and *verify*. Many learners can do one of
the two.

### M2 — Reproduce a published figure from a paper

**Artefact:** code that regenerates a figure from a published study, using the
paper's stated method and parameters.
**Evidence:** you state every parameter, including those the paper omits, and you
say so when you had to choose a value yourself.
**External check:** visual and quantitative comparison with the published figure.
**Typical curriculum point:** late advanced to graduate; see
[24-research-papers-writing/01-reading-research-literature](../../24-research-papers-writing/01-reading-research-literature/README.md).

M2 is where you discover that papers routinely underspecify their methods. That
discovery is the point of the milestone.

### M3 — Process real open data end to end

**Artefact:** a documented pipeline from a real archive to a defensible result.
**Evidence:** provenance (which archive, which version, which query), quality
control decisions, and a stated uncertainty.
**External check:** the result is within the range the published literature
expects for that region or dataset — or you explain why not.
**Typical curriculum point:** graduate; the data archives in
[26-reference-library/05-open-datasets-catalogue](../../26-reference-library/05-open-datasets-catalogue/README.md)
and the methods in [05-core-geophysics/06-data-processing-principles](../../05-core-geophysics/06-data-processing-principles/README.md).

### M4 — Invert data with an explicitly justified regularisation

**Artefact:** an inversion with a regularisation parameter chosen by a stated
criterion, plus a resolution or posterior analysis.
**Evidence:** the criterion (discrepancy principle, L-curve, cross-validation,
or a Bayesian posterior), the noise model it assumes, and the resulting
trade-off.
**External check:** synthetic data with a known answer, and a demonstration that
the recovered model degrades gracefully as noise increases.
**Typical curriculum point:** advanced to graduate; the natural home is
[18-inverse-problems](../../18-inverse-problems/README.md), with numerics from
[19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md).

This is the milestone that separates "I can run an inversion" from "I know what
my inversion means".

### M5 — Reproduce and critique a published result

**Artefact:** a reproduction plus a written critique: which assumptions bind,
how sensitive the conclusion is to them, and where the reported uncertainty is
incomplete.
**Evidence:** sensitivity tests, not opinions.
**External check:** a specialist can read the critique and identify what would
change the original conclusion.
**Typical curriculum point:** doctoral; see
[24-research-papers-writing/03-research-methods-and-rigour](../../24-research-papers-writing/03-research-methods-and-rigour/README.md).

### M6 — Design, execute, and communicate an original study

**Artefact:** a manuscript-style report with reproducible code, data provenance,
stated limitations, and a response to critical questioning.
**Evidence:** the whole chain — question, method, data, analysis, uncertainty,
limitations, and what would falsify the main claim.
**External check:** peer review, a thesis defence, or a seminar where
specialists attempt to break the argument.
**Typical curriculum point:** research professional; see
[25-projects-capstone/06-capstone-research](../../25-projects-capstone/06-capstone-research/README.md).

M6 also includes the *reviewer* role. Being able to write a substantive review of
another study is part of independent practice, and it is a milestone in its own
right because it requires all of M1–M5.

## 3. Milestones mapped to stages

| Stage | Milestone available | The skill it certifies |
|---|---|---|
| Beginner | none strictly required; build the habits in [study habits](./04-study-habits.md) | Units, plots, vocabulary, first scripts |
| Intermediate | M1 | Derive and verify |
| Advanced | M1 in a second domain, plus the numerical half of M4 | Implement and validate |
| Graduate | M2, M3, M4 | Reproduce, process, invert honestly |
| Doctoral | M5 | Critically appraise |
| Research professional | M6 | Originate, publish, review |

The mapping is deliberately not one-to-one: M1 recurs in every new domain, and a
researcher at M6 still produces M1-level artefacts when entering a new field.

## 4. How to write a milestone for yourself

Use this template. Fill in all four lines; an incomplete template is not a
milestone.

```text
ARTEFACT:   What I will produce (file, figure, report, dataset).
EVIDENCE:   What the artefact must record (data source, parameters, assumptions).
CHECK:      How someone else can test it (benchmark, published figure, reviewer).
WRONG-IF:   What result would show I have not achieved it.
```

Two examples:

```text
ARTEFACT:   A script that computes receiver functions for ten IRIS
            broadband stations and a stacked radial section.
EVIDENCE:   Station codes, time windows, filter corners, and the
            deconvolution water level, all recorded in a config file.
CHECK:      Compare the Moho depth I obtain with published values for the
            same region and state the difference.
WRONG-IF:   The stacked section shows no coherent conversion, or the
            result changes qualitatively when the water level moves within
            its plausible range.
```

```text
ARTEFACT:   An inversion of synthetic gravity data for a dipping interface,
            with an L-curve and a resolution test.
EVIDENCE:   Noise level, discretisation, regularisation operator, and the
            criterion used to select the damping.
CHECK:      A colleague regenerates the figure from the config alone.
WRONG-IF:   The recovered model is qualitatively different for two damping
            values that both satisfy the discrepancy criterion.
```

The `WRONG-IF` line is the one people omit, and it is the one that prevents the
milestone from becoming a box-ticking exercise.

## 5. Worked plan: from beginner to a first independent study

This is an illustrative *sequence*, not a schedule. Actual durations depend on
prior background and available time; treat the ordering as the content.

**Phase 1 — Foundations with visible output.** Work through
[01-mathematics](../../01-mathematics/README.md) and
[03-scientific-computing](../../03-scientific-computing/README.md) in parallel
with [04-earth-science-geology](../../04-earth-science-geology/README.md), and
[05-core-geophysics](../../05-core-geophysics/README.md) as soon as the first
two allow it. Milestone in view: M1 in two different domains. Output: a small
public repository of derivations and verified scripts.

**Phase 2 — One domain to working depth.** Choose a track from
[domain tracks](../02-curriculum-map/03-domain-tracks.md). In geophysics, a
common first choice is seismology or potential fields, because both have open
data archives and well-documented toolkits. Milestones in view: M1 and the
beginning of M2.

**Phase 3 — Real data.** Move to M3. This phase is where most learners discover
that "the data" is not a file but a query, a version, a licence, and a set of
station or survey metadata. Expect to spend more time on provenance and quality
control than on inversion, and record it as it happens.

**Phase 4 — Inference with honesty.** M4. Learn to state what the data do *not*
constrain. This is the single most transferable skill in the whole curriculum,
because it is what distinguishes a defensible result from a plausible one.

**Phase 5 — Critique and origin.** M5 and M6. Read recent papers in your area
critically; reproduce one; then design something small and original — a new
region, a new dataset, a method comparison, a sensitivity study. Originality at
this scale is not a new theory; it is a question nobody has answered with the
data you can access.

## 6. Self-review rubric for your own artefacts

Before claiming a milestone, answer these ten questions in writing. They are
adapted from the reproducibility concerns discussed in the further reading.

1. Can someone else obtain the data from the information you provided?
2. Are all processing parameters stated, including those that "obviously" had
   one value?
3. Is there a test that would fail if the code were wrong?
4. Have you checked the result against an analytic or published case?
5. What is the dominant source of uncertainty: measurement, model assumption, or
   parameter choice?
6. Which conclusion would change if that dominant uncertainty were doubled?
7. What did you *not* model, and how would that bias the result?
8. Are the figures regenerated by code, or hand-assembled?
9. If a reviewer asked for the raw numbers behind the main figure, could you
   produce them in one command?
10. What would falsify the main claim?

A "no" to any of items 1–4 or 9 means the artefact is not yet a milestone.

## 7. Where learners stall, and why

| Transition | Common stall | What usually helps |
|---|---|---|
| Beginner → intermediate | "I can follow lessons but cannot start problems" | Apply heuristics H2 and H8 from [study habits](./04-study-habits.md); estimate first, simplify the problem |
| Intermediate → advanced | Deriving is fine, implementing is not | Verified implementation: always reproduce a known case before a new one |
| Advanced → graduate | Running inversions without interrogating them | Require a resolution test for every inversion, without exception |
| Graduate → doctoral | Producing results but not questions | Read the limitations sections of ten recent papers; the questions are there |
| Doctoral → research professional | Finishing but not publishing | Attend to [24-research-papers-writing](../../24-research-papers-writing/README.md); treat writing as part of the method, not an afterthought |

## 8. Research integrity as a milestone component

Two milestones have integrity requirements that are not optional:

- **M3** requires data provenance and licence awareness. Data services and
  archives publish their own terms of use; record them, and cite the data
  provider as well as the archive, as the repository-level guidance in
  [CURRICULUM.md](../../CURRICULUM.md) and the root [README](../../README.md)
  also state.
- **M6** requires that reproduction be possible: code, environment, and
  parameter records. Professional societies publish authorship and ethics
  policies; read at least one before you submit your first manuscript, and
  follow your target journal's data-availability policy.

One habit covers most of this: **write your methods section while you work, not
afterwards.** If you cannot state a parameter, you did not record it, and the
milestone is not complete.

## Common mistakes

1. **Milestones without artefacts.** "I understand tomography" is not a
   milestone; a reproduction with a resolution test is.
2. **Skipping M2.** Reproducing one published figure is the cheapest way to learn
   how methods are actually reported, and how much is left unsaid.
3. **Treating M3 as a data-wrangling nuisance.** Provenance and quality control
   *are* the work; the inversion is often the short part.
4. **Claiming M4 without a resolution test.** An inversion figure without a
   resolution analysis does not say what the data constrain.
5. **Waiting for a perfect question before starting M6.** Original work begins
   with a small, answerable question and available data.
6. **Neglecting the reviewer milestone.** Reviewing others' work is the fastest
   way to raise the standard of your own.

## Real-world applications

- **Job applications and interviews.** Employers in geophysics ask for artefacts:
  a processed dataset, a modelling result, a tool you have written. The milestone
  template is exactly how such work is described in an interview.
- **Progression reviews and thesis committees.** Progress decisions are made on
  evidence of produced work, not on hours logged.
- **Publication and peer review.** M6 is the milestone most closely aligned with
  what journals require: a reproducible method, a stated uncertainty, and a claim
  that can be tested.

## Further reading

- Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers,
  C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., &
  Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature
  Human Behaviour*, 1, 0021. — A concise statement of the reproducibility
  practices that the milestone rubric in section 6 operationalises.
- Nosek, B. A., Alter, G., Banks, G. C., Borsboom, D., Bowman, S. D., Breckler,
  S. J., et al. (2015). Promoting an open research culture. *Science*,
  348(6242), 1422–1425. — The TOP guidelines; useful for deciding what to
  release alongside a result.
- Ioannidis, J. P. A. (2005). Why most published research findings are false.
  *PLoS Medicine*, 2(8), e124. — Read it for the reasoning about bias and
  uncertainty, and note that its quantitative claims are contested; the
  methodological argument stands independently.
- Booth, W. C., Colomb, G. G., Williams, J. M., Bizup, J., & FitzGerald, W. T.
  (2016). *The Craft of Research* (4th ed.). University of Chicago Press. — On
  turning a broad interest into an answerable research question.
  These are bibliographic records; confirm availability through your library or a
  DOI resolver before citing them yourself.

## Related lessons

- [The Six Stages and Their Mastery Checkpoints](./02-six-stages.md)
- [Deliberate Practice, Spaced Repetition and Problem-Solving Habits](./04-study-habits.md)
- [Domain Tracks: Seismology, Potential Fields, EM, Climate, Near-Surface](../02-curriculum-map/03-domain-tracks.md)
- [Batch Workflow for Adding Lessons and Projects](../03-how-to-use-this-repo/04-contribution-workflow.md)
