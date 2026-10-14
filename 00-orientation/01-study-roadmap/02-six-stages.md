---
id: 00-01-02
title: "The Six Stages and Their Mastery Checkpoints"
level: beginner
prereqs: ["00-01-01"]
estimated_minutes: 40
tags: [study-method, curriculum, assessment]
---

# The Six Stages and Their Mastery Checkpoints

## Learning objectives

- State the entry requirement, scope, and mastery checkpoint for each of the six
  stages.
- Explain why a *demonstrated artefact* is a better checkpoint than a feeling of
  familiarity.
- Identify which stage a given task belongs to by inspecting the task itself.

## Prerequisites

[How to Learn Geophysics](./01-how-to-learn-geophysics.md).

## 1. Why stages need checkpoints

A curriculum without checkpoints degrades into a reading list. The problem is
that self-assessment of understanding is unreliable: learners who understand
least are often the most confident, because they cannot yet see what a correct
solution requires. The remedy is to make each checkpoint an **externally
checkable artefact** — something a competent colleague could inspect and judge.

> A checkpoint is well-formed if a stranger could mark it pass/fail without
> asking you how you felt about it.

"I understand Fourier analysis" fails that test. "I can take an arbitrary
time series, compute its power spectrum with correct units, and explain the
frequency resolution and the noise floor" passes it.

## 2. The six stages

### Stage 1 — Beginner

- **Entry:** arithmetic, basic algebra. No programming assumed.
- **Scope:** what geophysics measures; units and dimensional analysis; reading a
  map; plotting data; the vocabulary of the field.
- **Checkpoint:** *Working independently, you convert a real geophysical
  observation into SI units, plot it with correctly labelled axes, and state in
  one paragraph what physical property it is sensitive to and why.*
- **Curriculum entry:** [01-mathematics](../../01-mathematics/README.md) from
  the start, [03-scientific-computing](../../03-scientific-computing/README.md)
  in parallel.

### Stage 2 — Intermediate

- **Entry:** single-variable calculus; basic Python; one introductory physics
  course.
- **Scope:** derivatives and integrals as physical tools; the wave equation;
  simple forward models; Fourier ideas; least squares.
- **Checkpoint:** *You derive the 1-D wave equation from a stretched string,
  implement a stable finite-difference solution, verify it against the analytic
  solution, and measure the observed convergence order.*
- **Typical modules:** [01-05](../../01-mathematics/05-single-variable-calculus/README.md),
  [01-07](../../01-mathematics/07-linear-algebra/README.md),
  [02-03](../../02-physics/03-oscillations-and-waves/README.md),
  [03-12](../../03-scientific-computing/12-numerical-simulation-python/README.md).

### Stage 3 — Advanced

- **Entry:** multivariable calculus; ODEs; linear algebra; NumPy proficiency.
- **Scope:** PDEs; vector calculus; elasticity; potential theory; grid-based
  forward modelling; linear inversion with regularisation.
- **Checkpoint:** *You implement a 2-D finite-difference forward model for a
  scalar wave or a potential field, validate it against an analytic benchmark,
  and invert synthetic data with an explicitly chosen regularisation parameter
  justified by an L-curve or discrepancy argument.*
- **Typical modules:** [01-06](../../01-mathematics/06-multivariable-calculus/README.md),
  [01-09](../../01-mathematics/09-partial-differential-equations/README.md),
  [02-04](../../02-physics/04-elasticity-and-continuum-mechanics/README.md),
  [18-inverse-problems](../../18-inverse-problems/README.md).

### Stage 4 — Graduate

- **Entry:** vector calculus; complex analysis; statistics; scientific software
  practice (version control, tests, reproducible environments).
- **Scope:** full processing pipelines on real data; Bayesian inference;
  resolution and uncertainty analysis; HPC fundamentals.
- **Checkpoint:** *You take a real open dataset end to end — download, quality
  control, process, invert, and report — producing a result with a stated
  uncertainty and an explicit statement of what the data do not constrain.*
- **Typical modules:** [06-seismology](../../06-seismology/README.md),
  [18-05](../../18-inverse-problems/05-bayesian-inversion/README.md),
  [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md).

### Stage 5 — Doctoral

- **Entry:** a domain specialisation; inverse theory; numerical methods.
- **Scope:** research-grade problems; novel method development; critical
  appraisal of published work.
- **Checkpoint:** *You reproduce a published result from its stated methods,
  then critique it: which assumptions bind, how sensitive the conclusion is to
  them, and where the reported uncertainty is incomplete.*
- **Typical modules:** [06-06 tomography](../../06-seismology/06-seismic-tomography/README.md),
  [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md),
  [25-05 doctoral projects](../../25-projects-capstone/05-doctoral-projects/README.md).

### Stage 6 — Research professional

- **Entry:** independent research capability across theory, data, and computing.
- **Scope:** designing studies; obtaining and managing data; leading
  interpretation; publishing; reviewing others' work.
- **Checkpoint:** *You design and execute an original study, write it up in
  manuscript form with reproducible code and data provenance, defend it under
  expert questioning, and provide a substantive peer review of another study.*
- **Typical modules:** [24-research-papers-writing](../../24-research-papers-writing/README.md),
  [25-06 capstone](../../25-projects-capstone/06-capstone-research/README.md).

## 3. Stages are not folders

A frequent misreading: the numbered folders are *topic* groupings, not stage
groupings. Folder 06 (seismology) contains beginner material (what a seismogram
looks like) and research material (trans-dimensional Bayesian source inversion).
**Difficulty is tracked per lesson** in its frontmatter, and the level marker
appears in [CURRICULUM.md](../../CURRICULUM.md).

This means you can be at Stage 4 in seismology and Stage 1 in geodynamics, and
that is normal. Research geophysicists are specialists who remain beginners
outside their area.

## 4. Progressing without fooling yourself

Three practical rules:

1. **Checkpoint before moving on.** Attempt the checkpoint artefact; do not
   merely decide you could do it.
2. **Interleave.** When moving to a new stage, spend ~20% of study time
   revisiting earlier material. Retention decays without it (see
   [study habits](./04-study-habits.md)).
3. **Expect the plateau.** Skill acquisition is not linear. Plateaus usually
   mean the task has become too easy to force adaptation, not that you have
   reached your limit. Increase difficulty or change task type.

## Common mistakes

1. **Confusing folder number with difficulty.** Folder 20 is not "harder" than
   folder 06.
2. **Declaring a checkpoint passed without an artefact.** This is the failure
   mode the entire checkpoint system exists to prevent.
3. **Skipping the foundations because they feel easy.** Most stalled learners
   are stuck on a missing foundation, not on a hard current topic.
4. **Studying only in your specialisation.** Cross-domain transfer is where
   original research often begins — joint inversion, for instance, sits exactly
   between two domains.

## Real-world applications

Postgraduate progression, professional accreditation, and job interviews all use
checkpoint-style assessment: you are asked to *do* something, not to describe
having learned it. Practising with artefact-based checkpoints is direct
preparation for a qualifying exam, a thesis defence, and a technical interview.

## Further reading

- Bloom, B. S. (Ed.) (1956). *Taxonomy of Educational Objectives: The
  Classification of Educational Goals. Handbook I: Cognitive Domain.*
  Longmans, Green. — The origin of the objectives taxonomy used to tag lesson
  objectives in this repository.
- Anderson, L. W., & Krathwohl, D. R. (Eds.) (2001). *A Taxonomy for Learning,
  Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational
  Objectives.* Longman. — The revised taxonomy, which distinguishes "remember"
  from "create" and is why lesson objectives here use verbs of application.
- Biggs, J., & Tang, C. (2011). *Teaching for Quality Learning at University*
  (4th ed.). Open University Press. — Constructive alignment: objectives,
  activities, and assessment must point at the same thing.

## Related lessons

- [How to Learn Geophysics: A Method, Not a Reading List](./01-how-to-learn-geophysics.md)
- [Diagnostic Self-Assessment and Placement Quiz](./03-self-assessment.md)
- [Research Milestones from Beginner to Independent Investigator](./05-milestones.md)
