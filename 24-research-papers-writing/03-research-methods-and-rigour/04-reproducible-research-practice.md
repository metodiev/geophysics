---
id: 24-03-04
title: "Reproducible Research Practice End to End"
level: research
prereqs: ["24-03-03", "22-02-01"]
estimated_minutes: 60
tags: [research, reproducibility, version-control, digests, workflows, provenance]
---

# Reproducible Research Practice End to End

Reproducibility is not a virtue a project has or lacks; it is a property of a
specific claim under a specific tolerance. This lesson makes that precise with a
**content digest**: a hash of the published numbers, so that two runs either agree
or do not, and a claim of "the same result" becomes a test rather than a memory.
It then measures what a changed parameter and a changed environment do to the
digest, and states the one thing a workflow cannot promise.

The organising idea is that **a result is a function of its inputs, and the inputs
are a longer list than the paper suggests**. Code, parameters, seed, library
versions, hardware and rounding convention all enter. A digest over a tuple of
those inputs is the cheapest way to make the list explicit, and the demonstration
shows a $1\%$ change in any single parameter breaking a four-significant-digit
agreement on every reported quantity.

> **Data provenance.** All numbers are **SYNTHETIC**. The pipeline is a small
> arithmetic surrogate; no files are written, nothing is downloaded, and no
> external data are read. The environment-perturbation size is a chosen value that
> stands in for real differences between library and hardware versions.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** reproducibility for a specific claim and **state** the tolerance at
   which the claim is made.
2. **Compute** a content digest of a result table and **use** it to test whether
   two runs agree.
3. **Enumerate** the inputs a digest must cover: code, parameters, seed,
   environment and rounding.
4. **Measure** how a parameter change and an environment change propagate to the
   reported digits.
5. **Design** a project structure in which a single command regenerates every
   reported number, and **state** what that command cannot guarantee.
6. **Report** provenance for a published result in a form a reader can check.

## Prerequisites

- [24-03-03 Designing Observational, Experimental and Modelling Studies](03-study-design.md) —
  the decisions the workflow must record.
- [22-02-01 The Reproducibility Crisis](../../22-data-engineering-reproducibility/02-reproducible-workflows/01-reproducibility-crisis.md) —
  the empirical background for these practices.

## 1. Reproducibility is a claim with a tolerance

Write the claim in a form that can fail:

> Given the archived code, the pinned environment and the parameter file, the
> reported quantities in Table 2 are reproduced to four significant digits.

Every clause matters. "Reproduced" without "to four significant digits" is not a
claim: it is a mood. The tolerance sets the work: four digits requires pinned
environment and fixed seeds; two digits survives most environment variation; one
digit survives almost everything.

Three levels are worth separating explicitly:

| Level | Meaning | Requires |
|---|---|---|
| Repeatability | Same author, same machine, same session | Nothing beyond the session |
| Reproducibility | Independent person, archived inputs, same outputs | Code, data, parameters, environment |
| Replicability | Independent data, same question | A documented method, not the code |

## 2. Digests: making agreement testable

The demonstration computes a SHA-256 digest over the rounded result vector:

$$d = \operatorname{SHA256}\!\left(\text{round}(y,\ 4\ \text{sig. digits})\right)
= \texttt{ec3ee4ed297050a7}\ldots \ (64\ \text{hex characters}).$$

Two properties make this useful:

- **It is sensitive.** Changing the RNG seed changes the reported digits and
  therefore the digest (demonstration: run at seed $20261014$ gives
  `ec3ee4ed297050a7...`, seed $20261015$ gives a different digest).
- **It is insensitive to irrelevant differences.** Because the digest is taken
  after rounding to the claimed precision, a difference below the tolerance does
  not change it. This is deliberate: the digest must encode the *claim*, not the
  bytes.

A digest is not a proof of correctness. Two runs can agree because both are wrong
in the same way, which is why an independent implementation matters more than an
identical rerun. What the digest does is make "we reproduced it" checkable, which
is the part that is otherwise unverifiable.

## 3. What a changed parameter does

In the demonstration every parameter of the chain influences every reported
quantity. Changing one parameter by $1\%$ of its value:

| Parameter changed by $1\%$ | Results changing digits | Largest relative change |
|---|---|---|
| high-cut corner | $6$ of $6$ | $0.142\%$ |
| taper length | $6$ of $6$ | $0.190\%$ |
| window length | $6$ of $6$ | $0.095\%$ |
| velocity step | $6$ of $6$ | $0.138\%$ |
| damping factor | $6$ of $6$ | $0.063\%$ |
| elevation correction | $6$ of $6$ | $0.298\%$ |

Every reported quantity moves, which is the arithmetic behind the constraint in
[24-02-03 Writing Methods Sections That Can Be Reproduced](../02-scientific-writing/03-writing-methods.md):
a $1\%$ uncertainty in an unstated parameter is enough to destroy agreement at four
significant digits. Reporting to four digits is therefore a commitment to a fully
specified parameter set, and a paper that reports four digits without one is making
a claim it cannot support.

## 4. What a changed environment does

One environment-induced difference — a different library version, a different
BLAS, a different compiler flag — is modelled here at relative size $10^{-4}$. Its
effect on the reported digits:

| Accumulated differences | Results still identical at $4$ digits |
|---|---|
| $0$ | $6$ of $6$ |
| $1$ | $2$ of $6$ |
| $4$ | $1$ of $6$ |
| $25$ | $1$ of $6$ |
| $100$ | $1$ of $6$ |

Two honest readings follow. First, a single difference of this size already breaks
four-digit agreement for some results. Second, the count does not fall
monotonically with the number of differences: whether a digit flips depends on
where the value sits relative to a rounding boundary, not on the perturbation size
alone. So "we cannot reproduce the last digit" is usually not evidence of an
error, and "we reproduced everything exactly" says as much about the rounding
convention as about the arithmetic.

## 5. The project structure that makes this possible

A layout that supports the claim:

```
project/
  README.md            # what it is, how to run it, what it produces
  environment.yml      # pinned environment
  data/raw/            # immutable inputs, never edited
  data/derived/        # regenerated, never edited by hand
  src/                 # library code, importable, tested
  scripts/             # numbered entry points: 01_..., 02_...
  params/
    baseline.yaml      # every parameter, with units and a comment
  outputs/
    figures/
    tables/
  make.sh              # runs 01..N in order and writes a digest file
```

Three properties matter: **one command** regenerates everything; **no hand-edited
derived files**; and **every reported number is written by a script**, so the
paper's table and the code cannot drift apart. The tooling is covered in
[22-02-03 Workflow Managers](../../22-data-engineering-reproducibility/02-reproducible-workflows/03-workflow-managers.md)
and the packaging in
[22-02-02 Environment Pinning](../../22-data-engineering-reproducibility/02-reproducible-workflows/02-environment-pinning.md).

## 6. Reporting provenance

The Methods section needs a short provenance block, not a manual:

- the repository location and the version or commit;
- the environment file name;
- the parameter file name;
- the command that reproduces the table;
- the seed or seeds;
- the tolerance of the reproducibility claim.

Six lines. Every one of them is checkable by a reader, and together they convert
"the analysis is available on request" into a claim with a test.

## Assumptions and regime of validity

1. **The pipeline is a surrogate.** Real computations involve solvers, iterative
   convergence and parallel reductions, whose reproducibility behaviour is richer
   than a weighted sum; the arithmetic of a digest and a tolerance is the same.
2. **The perturbation size $10^{-4}$ is chosen.** Real differences between
   environment versions range from exactly zero (bit-identical) to far larger
   (changed default and algorithm choices).
3. **A digest does not establish correctness.** It establishes agreement between
   two runs of one implementation.
4. **Rounding to a tolerance is a choice with consequences.** Reporting more digits
   makes the claim stronger and harder to meet; the choice belongs in the paper.
5. **Pinning is finite.** Containers pin the environment, not the hardware; a claim
   of bit-identical output across architectures is not usually supportable.

## The honest summary

A digest makes reproducibility testable, and the measurements are blunt: any single
parameter changed by $1\%$ moves every reported quantity at four significant
digits, and one environment difference of relative size $10^{-4}$ breaks the
agreement for some of them. The practical conclusion is to state the tolerance, pin
the environment, and report fewer digits when the claim cannot be met.

## Python demonstration

[`code/reproducible_research_practice_demo.py`](./code/reproducible_research_practice_demo.py)
prints four labelled sections: the result table with its SHA-256 digest; the
determinism check across runs and seeds; the effect of a $1\%$ parameter change on
the reported digits; and the effect of accumulated environment differences.

```bash
cd 24-research-papers-writing/03-research-methods-and-rigour/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproducible_research_practice_demo.py
```

## Exercises

Problems are in
[`exercises/04-reproducible-research-practice-exercises.md`](./exercises/04-reproducible-research-practice-exercises.md),
worked answers in
[`exercises/04-reproducible-research-practice-solutions.md`](./exercises/04-reproducible-research-practice-solutions.md).

## Mastery checkpoint

For a project you have finished or nearly finished:

1. Write the reproducibility claim with a tolerance.
2. Compute a digest of your main result table and record it.
3. Run your pipeline twice from a clean checkout; compare digests.
4. List every input not covered by your digest: seeds, versions, hardware, rounding.
5. Write the six-line provenance block for your Methods section.
6. State which of the three levels (repeatability, reproducibility, replicability)
   you can actually support, and how you know.

## Common pitfalls

1. **Claiming reproducibility with no tolerance.** The claim cannot be checked.
2. **Digesting before rounding.** Then the digest fails for reasons that do not
   matter.
3. **Hand-editing derived files.** The pipeline no longer regenerates what the
   paper contains.
4. **Seeds set in one script and not another.** Reproducibility is per output.
5. **Treating an identical rerun as independent validation.** It is not; an
   independent implementation is.
6. **Reporting four digits with unstated parameters.** The digits overstate the
   evidence; see
   [24-02-03 Writing Methods Sections That Can Be Reproduced](../02-scientific-writing/03-writing-methods.md).

## Where this is used

- **Every paper with a computed table:** the digest and the provenance block belong
  in the supplement.
- **Data and code release:** the repository is the artefact that makes the claim
  checkable; see
  [24-06-01 Publishing Data and Code Alongside Papers](../06-reproducible-publication/01-data-publication.md).
- **Group practice:** a shared layout and one-command pipeline converts
  reproducibility from heroics into habit.
- **Reviewing:** asking for the digest and the command is a fast, fair referee
  request; see [05 Peer Review Practice](05-peer-review-practice.md).

## Related lessons

- [24-06-03 Interactive Publications and Notebooks as Articles](../06-reproducible-publication/03-notebooks-as-publications.md) —
  the notebook-specific hazards of hidden state.
- [22-02-05 Data Versioning](../../22-data-engineering-reproducibility/02-reproducible-workflows/05-data-versioning.md) —
  how the inputs are pinned.
- [22-07-03 Regression Testing Data](../../22-data-engineering-reproducibility/07-software-testing-quality/03-regression-testing-data.md) —
  the tests that catch a silent change in a pipeline.
- [24-01-03 Critiquing Methods, Data and Inference](../01-reading-research-literature/03-critiquing-methods.md) —
  the audit a reader performs when the artefacts are missing.

## Self-assessment checklist

- [ ] I can write a reproducibility claim with a tolerance.
- [ ] I can compute and compare content digests.
- [ ] I can list the inputs a digest must cover.
- [ ] I can measure parameter and environment propagation to the reported digits.
- [ ] I can structure a project so one command regenerates everything.
- [ ] I can write a six-line provenance block.
