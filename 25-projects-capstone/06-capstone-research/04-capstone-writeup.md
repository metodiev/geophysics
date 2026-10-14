---
id: 25-06-04
title: "Capstone: Manuscript-Style Write-Up and Code Release"
level: research
prereqs: ["25-06-03", "22-01-04", "22-01-05", "22-03-02"]
estimated_minutes: 260
tags: [capstone, writing, code-release, reproducibility, research]
---

# Capstone: Manuscript-Style Write-Up and Code Release

## Learning objectives

By the end of this lesson you will be able to:

1. **Audit** every quantitative claim in a manuscript against the analysis that
   produced it, by recomputation rather than by rereading.
2. **Build** a result registry in which each number has a unit and a provenance, and
   **trace** every claim in the text to an entry.
3. **Classify** the defects an audit finds: wrong derivation, wrong quantity, rounding
   or arithmetic slip, untraceable claim, miscited artefact.
4. **Write** a manuscript with the section structure and the *claim–evidence* pairing
   that a referee expects, and with the uncertainty reported in the form the execution
   phase produced.
5. **Package** a code release that lets a reader reproduce the headline number:
   environment, data statement, tests, licence, citation, and a repository structure.
6. **State** what is and is not reproducible from the release, and why.
7. **Sequence** the work so that the audit runs before the submission, not after the
   review.

## Prerequisites

- [25-06-03 Capstone: Data, Modelling and Uncertainty Analysis](./03-capstone-execution.md) —
  the numbers, the budget and the provenance log this lesson reports.
- [22-01-04 Writing Documentation for Research Code](../../22-data-engineering-reproducibility/01-research-software-engineering/04-documentation.md) —
  the documentation the release must contain.
- [22-01-05 Licensing and Citation](../../22-data-engineering-reproducibility/01-research-software-engineering/05-licensing-and-citation.md) —
  the legal and citation side of a release.
- [22-03-02 Trade-offs in Scientific Data Formats](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/02-format-design-tradeoffs.md) —
  how the results are stored so that the audit can be run.

## 1. The question

*Does the manuscript say what the analysis found, exactly, and can someone else check
it?*

The demonstration is an audit, not an essay: 12 quantitative claims from a synthetic
capstone manuscript are recomputed from a 10-entry result registry and compared.

| outcome | count |
|---|---|
| claims checked | 12 |
| passed | 7 |
| flagged | 5 (42%) |
| claims carrying a registry reference | 11 of 12 (92%) |
| flags stable under rounding at the quoted precision | all five |

The five flags cover the four defect classes a write-up can contain — and **not one of
them is detectable by reading the manuscript**:

| flag | class |
|---|---|
| "95% interval of $\pm 3.29$ km (using $z = 1.645$)" | wrong derivation (the registry gives $3.922$) |
| "the systematic term is 71% of the variance" | wrong quantity (a standard-deviation ratio reported as a variance share; the registry gives $63.94\%$) |
| "45 of 52 stations passed QC (92%)" | arithmetic slip (the count gives $86.54\%$) |
| "the budget exceeds 2400 m at 95%" | untraceable claim (no registry entry) |
| "H = 35 km (see figure_04_resolution)" | miscited artefact (the figure list has `figure_01_map`, `figure_02_budget`, `figure_03_schedule`) |

Five defects in twelve claims is not an unusually bad manuscript; it is a normal one
before the audit.

## 2. The result registry

The registry is a table produced by the analysis — not maintained by hand — in which
every number that will appear in the text has an identifier, a value, a unit, and a
provenance:

| id | value | unit | provenance |
|---|---|---|---|
| `H_mean` | 35.04 | km | `capstone_execution`: mean of 40 000 budget draws |
| `H_sd` | 2.001 | km | `capstone_execution`: standard deviation of the budget |
| `H_sd_stat` | 1.198 | km | the statistical part of the budget |
| `H_sd_sys` | 1.600 | km | the systematic part of the budget |
| `S_k` | 0.474 | — | first-order Sobol index of $V_p/V_s$ |
| `S_t` | 0.356 | — | first-order Sobol index of $t$ |
| `n_accepted` | 45 | count | `fetch_waveforms`: stations passing QC |
| `n_requested` | 52 | count | stations requested |
| `t_ps` | 4.3493 | s | `hk_grid`: Ps delay at the reference station |
| `n_sched` | 20 000 | count | `capstone_proposal`: Monte Carlo schedules |

Three rules make the registry work:

1. **Write it from the analysis, not from the manuscript.** A registry typed from the
   text audits the text against itself.
2. **Store units and precision with the value.** The four flags above include one
   unit-independent error (a variance share) and one precision error ($z = 1.645$); both
   become visible only when the derivation is recomputed from identified values.
3. **Every derived quantity is computed, not quoted.** The 95% interval is
   $1.959964\,\sigma$, the percentage is $100\,\sigma_\text{sys}^2/\sigma^2$, the
   percentage of stations is $100\,n_\text{accepted}/n_\text{requested}$. Writing the
   formula in the audit script is what catches the wrong $z$ and the
   standard-deviation-ratio-as-variance-share.

**Derived-quantity checks that are worth automating** for any capstone: the quadrature
of the components against the total (the demo's $1.999$ km against $2.001$ km — a
$0.1\%$ agreement that confirms both the arithmetic and the linearity claim); the sum of
the sensitivity indices against unity ($0.991$ here, so the manuscript must state the
$0.9\%$ interaction remainder); and every unit conversion between the abstract, the
tables and the figures (kilometres in the figures, metres in the abstract).

## 3. Manuscript structure and the claim–evidence pairing

A capstone manuscript is a journal article with a narrower claim. The structure that
referees expect, with the element each section must contain:

| section | content | the thing that is usually missing |
|---|---|---|
| Abstract | question, method, headline number **with its uncertainty**, verdict | the uncertainty, or the assumption the number depends on |
| Introduction | the gap (from the literature review), the question, the contribution | the gap stated as a missing number rather than as a shortage of attention |
| Data | source, query, filters, count, noise estimate and its source | the count after filtering, and how the noise was estimated |
| Methods | estimator, forward model, the parameters that are *not* determined by the data with their tested values | the list of decisions |
| Results | the number, the verification, the sensitivity, the figures | the verification, which belongs in the results |
| Discussion | comparison with the literature in its own uncertainty units, assumptions, limitations | the comparison's uncertainty basis |
| Conclusion | what is established, what is not, next step | the "what is not" |
| Data and code statement | where the data came from and the release identifier | a DOI or a commit, not "available on request" |

**The claim–evidence rule.** Every quantitative sentence in the Abstract and the
Conclusions must be a restatement of a Results item. Write the Results first, then the
Abstract last, and check the pairing by reading the Abstract sentence by sentence with
the Results in front of you — a five-minute task that catches the commonest error in
student manuscripts, the optimistic abstract written from memory. The audit of §1 is
the mechanical version of that task, and it also catches the numerical defects the
pairing check cannot see.

**Reporting uncertainty.** The rule from [25-06-03](./03-capstone-execution.md):
quote the budget, not the statistical term alone. In this manuscript the honest sentence
is *"$H = 35.0 \pm 2.0$ km (total budget, of which 1.6 km is systematic and dominated
by the assumed $V_p/V_s = 1.75 \pm 0.03$)"* — not *"$35.04 \pm 1.20$ km"*, which is the
uncertainty of a quantity that does not exist.

## 4. The code release

A release is defined by what a reader can do with it, not by what it contains. The
minimum that lets someone reproduce the headline number:

1. **Repository structure**: `data/` (or a download script), `src/`, `scripts/` for the
   numbered steps, `results/` for the registry and figures, `tests/`, `README.md`,
   `LICENSE`, `CITATION.cff`.
2. **Environment**: a lock file (or container) that pins every package, plus the
   interpreter version; the README states the command that recreates it.
3. **Data statement**: the exact queries, the filters, the access date, the hashes, and
   for large or licensable data a `download.py` with the same parameters — the
   largest single barrier to reproduction and the easiest to solve while writing.
4. **One-command reproduction**: a task or Makefile target that runs the numbered
   scripts in order and writes `results/registry.json`; the audit of §1 then runs
   against the *fresh* registry.
5. **Tests**: the verification checks of [25-06-03](./03-capstone-execution.md) —
   the analytic check, the synthetic recovery, and at least one unit test that fails if
   a constant is changed. Tests are what make the release checkable rather than
   readable.
6. **Licence and citation**: code and data may need different licences; `CITATION.cff`
   carries the title, authors, version and DOI of the *release*, which is what a
   reader cites.
7. **Limitations section**: what the release does not reproduce (a proprietary dataset,
   a manual picking step, a cluster-only inversion) with the mitigation — a small
   synthetic example that exercises the same code path.

**What the release is for.** Not primarily for other scientists: for *the author*, six
months later, and for the referee who asks for the number in a different unit. A release
that cannot be run by its author after a break is not a release.

## 5. Sequencing

The write-up is not the last phase; it is a phase that overlaps the execution:

1. **Write the Methods and Data sections while executing** — while the decisions are
   fresh and their provenance is in front of you, not reconstructed afterwards.
2. **Write the Results as the registry fills**, with one results paragraph per
   headline number.
3. **Freeze the analysis** ([25-06-03](./03-capstone-execution.md)), run the registry
   generator, then the audit.
4. **Fix every flag before submission.** Each flag is either a text correction or, more
   seriously, an analysis correction — and the second kind changes the Results, which
   invalidates the draft downstream of it. That is the reason the audit precedes the
   final read.
5. **Write the Abstract last**, by copying from Results.
6. **Release the code at the freeze commit**, tag it, mint the DOI, and put the
   identifier in the data statement.

## 6. Failure modes

1. **Numbers typed from memory or from an earlier run.** The registry exists to make
   this impossible; the audit exists to catch it when it happens anyway.
2. **The abstract written first.** It will contain the optimistic version of the result
   and the wrong uncertainty.
3. **A 95% interval computed with $z = 1.645$**, or a variance share divided by a
   standard deviation: both are *derivation* errors, invisible without recomputation.
4. **Statistical-only uncertainty** in the abstract, hiding an assumption-dominated
   budget.
5. **Data "available on request"** with no query, no filters and no hash — the release
   that cannot be checked.
6. **A code release without tests**, so a reader cannot tell whether it works.
7. **An audit run after the review**, which converts a five-minute fix into a revision.

## 7. Rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Result registry | 20% | generated by code, with units and provenance for every number |
| Audit | 25% | every quantitative claim recomputed; flags classified and fixed |
| Structure and claim–evidence pairing | 20% | every abstract claim traceable to a Results item |
| Uncertainty reporting | 15% | total budget with the statistical/systematic split and the dominant assumption |
| Code release | 20% | environment, data statement, one-command reproduction, tests, licence, citation, limitations |

## 8. The honest summary

The product of the write-up phase is a manuscript whose numbers have been recomputed
and a release that regenerates them. The audit of the demonstration's 12 claims found
5 defects — a wrong $z$, a ratio reported as a variance share, an arithmetic slip, an
untraceable claim and a miscited figure — none of which a careful reader would catch,
and all of which the registry plus a ten-line recomputation caught immediately. The
transferable results are that a number in a manuscript is a claim about a computation
and must be audited as one, that the honest uncertainty is the budget rather than the
statistical term, and that a release is defined by what a reader can re-run rather than
by what it contains.

## Python demonstration

[`code/capstone_writeup_demo.py`](./code/capstone_writeup_demo.py) prints every number
above: the registry, the claim-by-claim recomputation with verdicts, the derived-quantity
checks, the citation audit, the defect summary, and a rounding-robustness table showing
which flags are stable at the quoted precision and which are marginal rounding
questions.

```bash
cd 25-projects-capstone/06-capstone-research/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python capstone_writeup_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, no network, no files, no
plots, exits 0, runs in about $0.1$ s.

## Exercises

Graded problems and worked solutions are in
[`exercises/04-capstone-writeup-exercises.md`](./exercises/04-capstone-writeup-exercises.md)
and
[`exercises/04-capstone-writeup-solutions.md`](./exercises/04-capstone-writeup-solutions.md).
The ★★★ item asks you to write the audit and the release checklist for your own
manuscript, with the registry generated from your own analysis.

## Mastery checkpoint

Without notes:

1. State the five things every registry entry must carry.
2. Name the four defect classes an audit finds, with an example of each.
3. Compute a 95% interval and a variance share from a mean, an sd and two component sds.
4. State the claim–evidence rule and the order in which the sections are written.
5. List the seven parts of a code release and state what a reader can do with each.

## Common pitfalls

1. A registry typed from the manuscript.
2. Auditing only the numbers you remember writing.
3. Quoting a statistical-only uncertainty.
4. Releasing code without the data download parameters.
5. Treating the audit as proofreading, when it is a verification of the analysis.

## Where this is used

This lesson produces the two artefacts the [defence](./05-capstone-defence.md) examines:
the manuscript and the release. The audit script is reusable in every subsequent
project — a version of it belongs in the template repository from which capstone
projects start — and the release is what makes the work citable and checkable rather
than merely reported.

## Related lessons

- [22-01-04 Writing Documentation for Research Code](../../22-data-engineering-reproducibility/01-research-software-engineering/04-documentation.md) —
  the README and API documentation standards for the release.
- [22-02-04 Notebooks versus Pipelines](../../22-data-engineering-reproducibility/02-reproducible-workflows/04-notebooks-vs-pipelines.md) —
  why the numbered-script structure is easier to audit than a notebook.
- [25-05-05 Project: Reproducing a Published Result](../05-doctoral-projects/05-reproduce-published-result.md) —
  the reader's side of this lesson.
- [25-06-05 Capstone: Presentation, Defence and Peer Critique](./05-capstone-defence.md) —
  defending the audited numbers.

## Self-assessment checklist

- [ ] I can generate a result registry from my analysis.
- [ ] I can audit every quantitative claim by recomputation.
- [ ] I can classify and fix each defect class.
- [ ] I can trace every abstract claim to a Results item.
- [ ] I can report uncertainty as the total budget with its split.
- [ ] I can release code that reproduces my headline number in one command.
