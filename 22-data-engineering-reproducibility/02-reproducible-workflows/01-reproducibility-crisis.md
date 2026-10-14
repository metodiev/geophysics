---
id: 22-02-01
title: "The Reproducibility Problem in the Computational Sciences"
level: intermediate
prereqs: ["22-01-03", "22-01-04"]
estimated_minutes: 45
tags: [reproducibility, statistics, power, multiplicity, research-practice]
---

# The Reproducibility Problem in the Computational Sciences

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** repeatability, reproducibility and replicability, and **classify** a
   given failure into the right category.
2. **Compute** the power of a test for a stated effect size and sample size, and
   **explain** why the replication rate of a significant result is the power and
   not one.
3. **Quantify** the winner's curse: how much a significance filter inflates the
   reported effect size.
4. **Compute** the false discovery proportion when many hypotheses are tested at
   an uncorrected level, and **state** the two inputs it depends on.
5. **Match** a reproducibility remedy to the failure it removes, and **say** for
   each remedy what it does not fix.
6. **Diagnose** an irreproducible result from its documentation alone.

Every number in this lesson is **SYNTHETIC**: studies are simulated from chosen
effect sizes, sample sizes and a unit noise level. No replication rate, effect
size or meta-analytic result from the literature is quoted or implied.

## Prerequisites

- [22-01-03 Code Review and Collaborative Development](../01-research-software-engineering/03-code-review.md) —
  the practice that catches the failures this lesson classifies.
- [22-01-04 Documentation, Docstrings and READMEs That Work](../01-research-software-engineering/04-documentation.md) —
  where the environment, seed and data facts are recorded.

## 1. Intuition: three words that are not synonyms

Reproducibility discussions go wrong immediately because three distinct claims
share one word. The widely used convention in computing is:

| Term | Team | Setup | What it establishes |
|---|---|---|---|
| **Repeatable** | same | same | the result was not a one-off accident of this run |
| **Reproducible** | different | same | the result is a property of the code and data, not of the person |
| **Replicable** | different | different | the result is a property of the world |

Repeatability is a claim about your own pipeline on your own machine; it fails
when a seed is unrecorded. Reproducibility is the claim a paper makes when it
publishes code and data; it fails when the environment is unpinned. Replicability
is a claim about nature, and no amount of software engineering can establish it —
which is why the statistical part of this lesson exists at all.

## 2. The failure taxonomy

A result fails to reproduce for one of six reasons, and each has a different
remedy:

1. **The data are gone or ambiguous.** "The catalogue from 2019" resolves to no
   particular file. Remedy: versioned data with an identifier
   ([22-02-05](05-data-versioning.md)).
2. **The code is gone.** A figure exists; the script that drew it does not.
   Remedy: the artefact and the analysis in one citable release
   ([22-01-05](../01-research-software-engineering/05-licensing-and-citation.md)).
3. **The environment drifted.** The code runs, the numbers differ. Remedy: pinned
   environments and containers ([22-02-02](02-environment-pinning.md),
   [22-02-06](06-containers-reproducibility.md)).
4. **The steps were manual.** Three commands, two edits and one spreadsheet.
   Remedy: a workflow definition
   ([22-02-03](03-workflow-managers.md)).
5. **The randomness was not controlled.** A seed is unrecorded or a run depends
   on thread interleaving. Remedy: explicit generators and recorded seeds
   ([22-01-03](../01-research-software-engineering/03-code-review.md) §7).
6. **The claim exceeds the evidence.** The pipeline reproduces perfectly and the
   conclusion is still not supported, because of power, selection or
   multiplicity. Remedy: §4 of this lesson, and honest reporting.

Only the last category survives a perfect software pipeline. That is the point of
this lesson's measurements: reproducibility engineering is necessary and not
sufficient.

## 3. Power, and why a significant result often does not replicate

A two-sided test at level $\alpha$ compares $\hat\delta$ with
$z_{1-\alpha/2}\,\sigma/\sqrt{n}$. Its **power** for a true effect $\delta$ is

$$\text{power} = \Phi\!\left(\frac{\delta\sqrt{n}}{\sigma} -
z_{1-\alpha/2}\right), \qquad
z_{1-0.025} = 1.959964, \quad \Phi = \text{standard normal CDF}.$$

With the demonstration's SYNTHETIC model ($\sigma = 1$ data unit,
$\alpha = 0.05$):

| Effect (in $\sigma$) | $n = 10$ | $n = 30$ | $n = 100$ | $n = 300$ |
|---|---|---|---|---|
| 0.2 | 0.092 | 0.194 | 0.516 | 0.934 |
| 0.5 | 0.352 | 0.782 | 0.999 | 1.000 |
| 0.8 | 0.716 | 0.992 | 1.000 | 1.000 |
| 1.0 | 0.885 | 1.000 | 1.000 | 1.000 |

Inverting the relation gives the sample size for 80 % power:
$n = 31.4 \to 32$ for $\delta = 0.5$, and $n = 196.2 \to 197$ for
$\delta = 0.2$. An effect of a fifth of the noise requires roughly six times the
sample of an effect of half the noise — the arithmetic behind the familiar
complaint that small effects need large studies.

**The replication arithmetic.** If the effect is exactly the same in the
replication, then the probability that a significant original study is significant
again is

$$P(\text{replicate} \mid \text{significant}) = \text{power},$$

not one. The demonstration's Monte Carlo confirms it row by row:

| $n$ | Effect | Power | Significant | Replicates at $n$ | Replicates at $2n$ |
|---|---|---|---|---|---|
| 30 | 0.3 | 0.376 | 7466 | 0.374 | 0.634 |
| 30 | 0.5 | 0.782 | 15707 | 0.781 | 0.972 |
| 30 | 0.8 | 0.992 | 19853 | 0.993 | 1.000 |
| 10 | 1.0 | 0.885 | 17709 | 0.886 | 0.994 |

So a literature in which the typical study has 50 % power has a *correct*
expected replication rate of about 50 %, and reporting that figure as a scandal
misreads the statistics. When the true effect itself varies between studies, the
measured rate falls further: with effects drawn with a standard deviation of half
the effect size at the same power of 0.782, the demonstration measures a
replication rate of **0.687**.

## 4. Winner's curse and multiplicity

**Winner's curse.** Selecting on significance selects the studies whose noise
happened to be favourable, so the reported effect is biased upwards. The
demonstration measures the mean $|\hat\delta|$ among significant studies for three
cases:

| True effect | $n$ | Mean reported effect | Reported / true |
|---|---|---|---|
| 0.2 | 100 | 0.277 | 1.387 |
| 0.5 | 30 | 0.568 | 1.137 |
| 0.8 | 30 | 0.802 | 1.003 |

The inflation is worst where the power is lowest — 39 % at 52 % power — and
vanishes where the power is near one. This is not fraud and not bias in the
estimator: $\hat\delta$ is unbiased *unconditionally*, and the conditioning is
the whole problem. It is also the reason a follow-up study of a just-significant
effect usually finds a smaller one: the replication is not measuring a smaller
world, it is measuring the same world without the selection.

**Multiplicity.** Testing 20 hypotheses at $\alpha = 0.05$ each gives, for purely
null effects, an expected
$20 \times 0.05 = 1$ significant result and a high chance of at least one. The
demonstration's SYNTHETIC run with 10 % of hypotheses truly non-zero reports:

| True effect size | Mean significant tests | Mean false discovery proportion | $P(\ge 1$ false positive$)$ |
|---|---|---|---|
| 0.0 | 0.98 | 0.899 | 0.594 |
| 0.5 | 1.07 | 0.853 | 0.610 |

With no correction, about **90 % of the reported discoveries are false** whenever
the true effects are small relative to the noise: the family-wise error rate is
59–61 % while the nominal per-test rate is 5 %. The false discovery proportion
depends on only two things — the per-test level and the fraction of hypotheses
that are truly non-zero — which is why a result cannot be judged without knowing
how many hypotheses were searched.

## 5. Remedy versus failure, honestly

| Failure | Remedy | What the remedy does **not** fix |
|---|---|---|
| Data ambiguity | versioned data + identifier | a wrong processing choice |
| Missing code | release with the analysis | a bug in that code |
| Environment drift | pinning + container + lock file | CPU-dependent floating point |
| Manual steps | workflow definition | a wrong step, now automated |
| Uncontrolled randomness | recorded seed | a seed that is irrelevant because the result is unstable |
| Claim exceeds evidence | power, correction, selection reporting | a bad measurement |

The last column is the one that matters in practice. Each remedy removes one
failure mode and is silent about the others; a group that pins its environment
and still tests 40 hypotheses has improved its engineering and not its inference.

## 6. Worked example: diagnosing a failed reproduction

A reader reports that they cannot reproduce a published correlation of 0.31. The
authors' repository contains one notebook, a `requirements.txt` with no versions,
and a data path pointing at a personal directory. Work through §2:

1. **Data ambiguity (yes).** The path is personal; no archive identifier is cited,
   so the version of the catalogue is unknown.
2. **Missing code (partly).** The notebook exists but the file that produced its
   intermediate input does not.
3. **Environment drift (yes).** Unpinned requirements over a three-year interval
   will resolve to a different set; the demonstration's 40 dependencies with a
   mean of 6.2 admissible releases each give $10^{30.9}$ admissible
   combinations, and the chance that an unpinned install reproduces another is
   $10^{-30.9}$.
4. **Manual steps (unknown).** The notebook's outputs correspond to one of
   $913\,584$ valid cell orders in the demonstration's 14-cell model; nothing
   records which one ran.
5. **Randomness (unknown).** No seed is mentioned.
6. **Claim (testable).** With 0.31 reported, ask for the sample size and the
   number of hypotheses. If the study has $n = 25$ and the corpus has an enormous
   correlation, the reported value is plausibly a winner's-curse draw.

The diagnosis tells you which remedies to ask for, and in which order: the data
identifier first, because without it nothing downstream can be checked.

## Assumptions and regime of validity

1. **Normal-approximation testing.** Power and the winner's-curse figures assume
   a z-test with known unit variance; $t$-tests shift the numbers slightly at
   small $n$ and change none of the conclusions.
2. **A single pre-specified test.** The multiplicity section is about a search
   over 20 hypotheses; sequential testing, optional stopping and model selection
   inflate error rates by different mechanisms with different corrections.
3. **The replication uses the true effect.** Where the effect is exactly the same
   in both studies the replication rate equals the power; heterogeneity lowers it
   (measured 0.687 at 0.782 power here).
4. **A chosen prior on true effects.** The false discovery proportion depends on
   the fraction of tested hypotheses that are truly non-zero (10 % here); that
   fraction is never known in a real study, which is why the FDP is reported as a
   function of it.
5. **No claim about the real literature.** Nothing here estimates the actual
   replication rate of any field; the numbers are properties of the simulated
   model with the stated parameters.

## The honest summary

Reproducibility is three different claims, and the failure taxonomy splits into
artefact problems (data, code, environment, manual steps, randomness) and
inference problems (power, selection, multiplicity). The artefact problems are
solved by engineering, and this module's later lessons measure the solutions. The
inference problems are not: a significant result replicates with probability
equal to the study's power — 0.374 at 37.6 % power in the demonstration's model,
0.781 at 78.2 % — and a significance filter inflates the reported effect by 39 %
when the power is near one half. Testing 20 hypotheses at an uncorrected 5 %
produces a mean false discovery proportion of 0.899 when the effects are null.
The most useful habit this lesson can install is to ask, of any reported result:
what is the power, how many hypotheses were searched, and which version of the
data — because those three questions decide whether the number can mean what it
appears to mean.

## Python demonstration

[`code/reproducibility_crisis_demo.py`](./code/reproducibility_crisis_demo.py)
prints, with `np.random.default_rng(20261014)` and 20 000 simulated studies per
row:

1. the power table and the sample sizes for 80 % power (32 for $\delta = 0.5$,
   197 for $\delta = 0.2$);
2. the conditional replication rates at one and two times the sample size, plus
   the heterogeneous-effect case (0.687 against 0.782);
3. the winner's-curse inflation table (worst case 1.387);
4. the multiplicity result: mean false discovery proportion 0.899 and
   family-wise error 0.594 for null effects.

```bash
cd 22-data-engineering-reproducibility/02-reproducible-workflows/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproducibility_crisis_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/01-reproducibility-crisis-exercises.md`](./exercises/01-reproducibility-crisis-exercises.md)
and
[`exercises/01-reproducibility-crisis-solutions.md`](./exercises/01-reproducibility-crisis-solutions.md).

## Mastery checkpoint

Without notes: a study reports a correlation significant at $p = 0.03$ with
$n = 28$, and the authors state that they tested "the main relationship".

1. Compute the power for an effect of 0.5 of the noise at $n = 28$ using the
   lesson's formula, and state the expected replication rate.
2. State the two facts about the search that the methods section must report
   before the $p$-value can be interpreted.
3. Name the artefact failures you would check first, and give the order.
4. A colleague says "our pipeline reproduces exactly, so the result is solid".
   State the failure category that the reproduction does not address.

## Common pitfalls

1. **Using "reproducible" for all three claims.** Repeatability, reproducibility
   and replicability need different evidence.
2. **Treating a 50 % replication rate as misconduct.** It is the arithmetic of
   50 % power.
3. **Quoting a post-selection effect size.** The mean reported effect in the
   demonstration's low-power case is 1.387 times the true one.
4. **Reporting a $p$-value without the number of hypotheses.** The false
   discovery proportion depends on it; 20 uncorrected tests give a mean FDP of
   0.899 in the null case.
5. **Assuming better software fixes inference.** A perfectly reproducible
   pipeline can produce a winner's-curse estimate.
6. **Omitting the seed and the data version.** Both are required for
   repeatability and neither is implied by publishing the code.

## Where this is used

- **Referee reports and editorial checks** — the questions in §6 are what a
  data-availability policy is meant to make answerable.
- **Reproducibility badges and artefact evaluation** — a badge asserts a specific
  claim from §1, not all three.
- **Group practice** — the failure taxonomy is a checklist for a project's
  handover documentation.
- **Statistical review of your own work** — power and multiplicity calculations
  belong in the analysis plan, not in the response to a reviewer:
  see [21-08 Causal Inference and Design](../../21-statistics-bayesian-ml/08-causal-inference-and-design/README.md).

## Related lessons

- [22-02-02 Pinning Environments and Managing Dependencies](./02-environment-pinning.md) —
  the remedy for environment drift, measured.
- [22-02-03 Workflow Managers: Snakemake, Make, Dask, Prefect](./03-workflow-managers.md) —
  the remedy for manual steps.
- [22-02-04 Notebooks vs Pipelines: Choosing the Right Tool](./04-notebooks-vs-pipelines.md) —
  what the notebook's execution order does to repeatability.
- [22-02-05 Data Versioning and Provenance Tracking](./05-data-versioning.md) —
  the remedy for ambiguous data.
- [22-02-06 Containers for Computational Reproducibility](./06-containers-reproducibility.md) —
  the remedy for environment drift at the level of the whole machine.

## Self-assessment checklist

- [ ] I can distinguish repeatability, reproducibility and replicability.
- [ ] I can classify a failure into the six categories.
- [ ] I can compute power and the sample size for a target power.
- [ ] I can state why the replication rate of a significant result is the power.
- [ ] I can quantify the winner's curse for a given power.
- [ ] I can compute a false discovery proportion from the level and the prior.
