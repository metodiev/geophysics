---
id: 22-01-04
title: "Documentation, Docstrings and READMEs That Work"
level: intermediate
prereqs: ["22-01-01", "03-01-04"]
estimated_minutes: 40
tags: [documentation, docstrings, readme, maintenance, software-engineering]
---

# Documentation, Docstrings and READMEs That Work

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** the four jobs documentation does — orientation, reference,
   task, explanation — and **assign** each to the right artefact.
2. **Write** a docstring that states units, parameter shapes, the return value
   and the failure modes, in a form a reader can execute.
3. **Structure** a project README so a stranger can install, run and cite the
   code without reading the source.
4. **Measure** documentation decay with a signature-drift model, and **explain**
   why coverage and accuracy are different quantities.
5. **Quantify** what an executed-example (doctest) suite buys, and **state** what
   it does not cover.
6. **Document** the reproducibility-critical facts — environment, seed, data
   version, decision — that a reader needs to reproduce a result.

Documentation is a human artefact and its decay is modelled here, not measured:
the numbers in this lesson come from a **SYNTHETIC** simulation of a 120-function
API over eight releases, with chosen change and update rates. No repository was
parsed and no survey is quoted.

## Prerequisites

- [22-01-01 Designing Software for Scientific Research](./01-software-design-science.md) —
  the interfaces that documentation has to describe.
- [03-01-04 Functions and Modules](../../03-scientific-computing/01-python-fundamentals/04-functions-modules.md) —
  signatures, arguments and return values.

## 1. Intuition: documentation is written for the second user

The first user of any research code is its author, who holds the whole context:
which axis is which, which year the instrument was recalibrated, what the fit
excluded. The second user holds none of it, and the second user is the one who
decides whether the result is credible. Documentation is the transfer of the
context that the code cannot encode by itself.

That framing decides priorities: a beautiful docstring on a private helper is
worth less than three lines in the README saying which command produced the
figure in the paper. Documentation is part of the deliverable, and its decay is a
measurable process rather than a moral failure.

## 2. The four jobs, and the four artefacts

| Job | Reader question | Artefact |
|---|---|---|
| Orientation | "What is this and how do I start?" | `README.md` |
| Reference | "What exactly does this function take and return?" | docstrings / generated API docs |
| Task | "How do I do *this specific thing*?" | a short guide or a worked example |
| Explanation | "Why is the algorithm this way?" | a design note, comment or paper section |

Conflating them produces the two classic failures: a README that explains the
physics instead of how to run the code, and docstrings that describe the physics
instead of the parameter's unit. Each artefact has one audience and one job; if a
paragraph in the README is answering "why", it belongs in a design note.

## 3. Docstrings that state the contract

A docstring is the function's contract. For scientific code, four items are
non-negotiable and one is strongly recommended:

1. **What it computes**, in one sentence, in domain language.
2. **Units of every parameter and of the return value.** A bare `dt` is a defect;
   `dt : float, sampling interval in seconds` is not.
3. **Shape and dtype** of array arguments and results, including axis
   conventions, for anything with more than one dimension.
4. **Failure modes** — what it raises, and what it returns for empty or
   single-sample input.
5. **One executable example** (see §5) with a value a reader can check.

```python
def strain_rate(data, dt):
    """Return the time derivative of `data` along axis 0.

    Parameters
    ----------
    data : ndarray, shape (n_samples, ...)
        Array sampled at a constant interval along axis 0.
    dt : float
        Sampling interval in seconds. Must be non-zero.

    Returns
    -------
    ndarray, shape (n_samples - 1, ...)
        Forward difference in data units per second.

    Raises
    ------
    ValueError
        If `dt` is zero or `data` has fewer than two samples.

    Examples
    --------
    >>> strain_rate(np.array([0.0, 2.0, 6.0]), 2.0)
    array([1., 2.])
    """
```

The example is the part that makes the rest checkable. It is also the part most
often omitted, which is why §5 treats it as a test rather than as prose.

## 4. The README as the entry point

A README is read by four different people: someone deciding whether to use the
code, someone trying to run it, someone trying to cite it, and someone (often the
author, a year later) trying to remember what it was for. The order that serves
all four is fixed:

1. **One sentence** saying what the code does.
2. **Status**: is this maintained, archived, or a paper's frozen release?
3. **Install**: the exact commands, including the environment file.
4. **Quickstart**: the shortest command that produces a meaningful output.
5. **Data**: provenance, access route, size, and the version used.
6. **How to cite**: the citation file or the paper, with the version.
7. **Licence**, by name.
8. **What is not here**: known limitations, excluded cases, the parts that are
   research code rather than production code.

Items 5, 6 and 8 are the ones that separate scientific software from product
software. A README that omits the data version cannot support a reproduction, and
one that omits limitations invites a reader to trust more than the author does.

## 5. Documentation rot, and what decays

Documentation does not become wrong because it was wrong; it becomes wrong
because the **code changed underneath it**. The demonstration models exactly that:
120 public functions start at 70.8 % coverage (85 of 120), each release changes
15 % of signatures, four functions are added, and each changed signature has a
55 % chance of a matching documentation update. The **SYNTHETIC** results:

| Release | Functions | Documented | Stale | Accurate |
|---|---|---|---|---|
| 1 | 124 | 69.4 % | 4.8 % | 64.5 % |
| 2 | 128 | 68.0 % | 9.4 % | 58.6 % |
| 4 | 136 | 65.4 % | 17.6 % | 47.8 % |
| 5 | 140 | 64.3 % | 20.7 % | 43.6 % |
| 6 | 144 | 63.9 % | 23.6 % | 40.3 % |
| 8 | 152 | 64.5 % | 21.1 % | 43.4 % |

Two things are worth noticing. First, **coverage is nearly flat** (69.4 % → 64.5
%) while **accuracy falls** from 64.5 % to 43.4 %: counting documented functions
would have reported success throughout. Second, the model has a **long-run
limit**, and the eight releases are still in the transient on the way to it. At
each release a fraction $P(1-u) = 0.15 \times 0.45 = 0.0675$ of documented
functions becomes stale, while a fraction $P u = 0.15 \times 0.55 = 0.0825$ of
stale functions is healed by an update. Setting the flows equal gives the
steady-state ratio

$$\frac{S}{D} = \frac{1-u}{u} = \frac{0.45}{0.55} = 0.818,$$

so the model's destination is **81.8 % of documented functions stale**, which at
the modelled coverage is 52.8 % of all functions. The apparent plateau at 21–23 %
in releases 6–8 is not an equilibrium; it is the transient, and the wobble is
sampling noise. The general lesson is stark: an update rate $u$ below one half
gives a documentation set that becomes *mostly wrong*, no matter how much is
written at the start.

The metric to report is therefore *accurate* documentation, and the only way to
keep it honest is to make the documentation executable.

## 6. Executed examples: the only self-checking documentation

If an example runs as a test, a signature change breaks the test instead of
silently invalidating the example. With a runner that catches a stale signature
with probability 0.70 per release, the demonstration's residual staleness at
release 8 falls from **21.1 % to 6.3 %**, avoiding **14.7 percentage points** of
stale documentation. The arithmetic is transparent:

$$\text{residual} = \text{stale} \times (1 - p_{\text{catch}}) = 0.211 \times
0.30 = 0.063.$$

The demonstrated example in §3 — `strain_rate(np.array([0.0, 2.0, 6.0]), 2.0)`
returning `array([1., 2.])` — tests the unit, the shape and the convention in
three lines. What executed examples **cannot** cover is a convention that changed
while the example still passes: a switch from a forward to a central difference
needs a different example, and no runner detects an example never written.

## 7. The cost of staleness, and how to state it

The demonstration estimates the reader cost with an explicitly labelled model:
32 of the 152 functions are documented and stale at release 8, each consulted
stale function is assumed to waste 12 reader-minutes, and 10 % of them are
consulted before the error is noticed. That gives

$$32 \times 12\ \text{min} \times 0.10 = 38\ \text{min} \approx 0.6\ \text{h}$$

per team pass through the API. Report it as a model output with its assumptions
attached: staleness recurs at every pass, and the cost is paid by the reader least
equipped to notice it — the newcomer.

## 8. Documenting reproducibility, not just the interface

Four facts belong in the documentation even though they are not part of any
signature:

1. **Environment**: the file (`environment.yml`, `requirements.txt`, a container
   digest) that produced the result, with a date.
2. **Seed**: which generator, which seed, and where randomness enters; a result
   that depends on an unrecorded seed is not reproducible.
3. **Data version**: an identifier (DOI, archive hash, query date) and the
   processing steps applied to it.
4. **Decisions**: why a threshold, a window or a filter was chosen, written where
   the parameter is set, because no amount of code reading recovers that fact.

Items 1–3 are the subject of
[22-02 Reproducible Research Workflows](../02-reproducible-workflows/README.md);
recording them in one place at the top of the repository is what makes that module
feasible.

## 9. Worked example: auditing a README

A repository's README contains: a two-paragraph history of the research group, an
installation section that says "install the requirements", a usage section
showing an internal function call, no licence, no citation, no data provenance,
and no mention of limitations. Scored against §4 it fails seven of the eight
items: there is no one-sentence purpose (a reader cannot decide whether to
invest), no status (a 2016 script looks maintained), no quickstart (the reader
must read the source to run anything), no data provenance (the result cannot be
reproduced), no citation (the software cannot be cited), no licence (reuse is
legally undefined) and no limitations (the reader trusts more than the author
does); only the installation section is partly present, and it pins no version.

The cheapest repair is not "write more": it is to add five lines — purpose,
quickstart command, data DOI, citation and licence — because those five lines
convert the repository from an archive into an instrument.

## Assumptions and regime of validity

1. **Signature drift is the decay mechanism.** The model assumes documentation
   goes stale when signatures change; documentation also decays through changed
   *conventions* and changed *physics*, which no signature check detects.
2. **Uniform change probability.** In a real project the same 15 % function is
   edited every release while most are untouched; clustering makes staleness more
   concentrated and the mean less informative.
3. **A fixed catch probability.** An example runner catches whatever its examples
   exercise, which is not a uniform 70 % of signature changes.
4. **Reader cost is a chosen constant, and the model is silent on correctness
   when written.** The 12 reader-minutes and the 10 % consultation fraction are
   teaching values; and nothing here detects documentation that was wrong from
   the start, which is what a coverage count hides most completely.

## The honest summary

Documentation is the interface between the code and the stranger who must judge
it, and it decays by a mechanism you can measure: signature change without a
matching update. In the synthetic API, coverage stays near 64–69 % across eight
releases while *accurate* documentation falls from 64.5 % to 43.4 % and stale
documentation rises to 21.1 % on the way to the model's long-run limit of 81.8 %
of documented functions; adding an executed-example suite cuts residual staleness
to 6.3 %, a saving of 14.7 percentage points, at the cost of writing one
runnable example per function. The practical rules that follow are: write for
the second user, state units in every parameter, keep one artefact per job, put
the reproducibility facts (environment, seed, data version, decision) where a
reader will find them, and make documentation executable so that decay announces
itself as a failing test rather than as a wrong result.

## Python demonstration

[`code/documentation_demo.py`](./code/documentation_demo.py) simulates the
120-function API with `np.random.default_rng(20261014)` and prints, under four
numbered banners:

1. the starting coverage: 85 documented of 120 (70.8 %);
2. the eight-release table of coverage, staleness and accuracy;
3. the effect of a 70 %-effective example runner (21.1 % → 6.3 %);
4. the reader-cost model, with every assumption printed alongside the result.

```bash
cd 22-data-engineering-reproducibility/01-research-software-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python documentation_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/04-documentation-exercises.md`](./exercises/04-documentation-exercises.md)
and
[`exercises/04-documentation-solutions.md`](./exercises/04-documentation-solutions.md).

## Mastery checkpoint

Without notes: the demonstration reports 152 functions at release 8, 64.5 %
documented and 21.1 % stale.

1. Compute the number of documented functions and the number of stale functions,
   and check that the "accurate" percentage is their difference as a fraction of
   the total.
2. The team adds a rule that every changed signature must be updated. State the
   new steady-state staleness in the model's terms, and explain why it does not
   reach zero in practice.
3. Name the four reproducibility facts from §8 for a result that depends on a
   random subsample of a downloaded catalogue.
4. A reviewer says "coverage is 64 %, so documentation is fine". State the two
   measurements that answer them.

## Common pitfalls

1. **Reporting coverage instead of accuracy.** In the demonstration coverage is
   nearly flat while accuracy falls by 21 percentage points.
2. **Documentation that describes the implementation.** "Loops over the samples"
   is not a contract; state the input, the output and the units.
3. **Missing units.** The single most common defect in scientific docstrings, and
   the one a reader cannot recover from the code.
4. **Examples that cannot run.** An example not executed by CI is prose with a
   syntax error waiting to happen.
5. **Documenting only what exists.** A README must state what the code does
   *not* handle; silence is read as support.
6. **Writing documentation last.** The context that makes it cheap is the context
   you have while writing the code, not a month later.

## Where this is used

- **Publishing software with a paper** — the README and the executable examples
  are what a referee checks: see
  [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md).
- **Long-lived instrument codes and student handover** — the quickstart command
  and the decision record are what get a newcomer working on real data instead of
  on setup, and what keep a parameter's reason alive across staff turnover.

## Related lessons

- [22-01-05 Licensing, Citation and Software Credit](./05-licensing-and-citation.md) —
  the two README sections that make reuse legal and credit possible.
- [22-01-03 Code Review and Collaborative Development](./03-code-review.md) —
  where documentation defects are caught before they cost a reader.
- [22-07-04 Benchmarking, Performance Tracking and Documentation Tests](../07-software-testing-quality/04-benchmarking-and-docs.md) —
  the machinery that executes examples and docs.
- [22-02-01 The Reproducibility Problem in the Computational Sciences](../02-reproducible-workflows/01-reproducibility-crisis.md) —
  why the four facts of §8 decide whether a result can be reproduced.

## Self-assessment checklist

- [ ] I can name the four documentation jobs and their artefacts.
- [ ] I can write a docstring with units, shapes, failure modes and an example.
- [ ] I can order a README so a stranger can run the code.
- [ ] I can explain why coverage and accuracy diverge.
- [ ] I can compute what an executed-example suite changes.
- [ ] I can list the four reproducibility facts for a given result.
