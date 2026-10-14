---
id: 06-06-07
title: "Resolving Discrepancies Between Tomographic Models"
level: research
prereqs: ["06-06-03", "06-06-06"]
tags: [seismology, tomography, model-comparison, resolution, uncertainty]
---

# Resolving Discrepancies Between Tomographic Models

All models and data in this module are **SYNTHETIC**. Every number below is
printed by `code/tomography_controversies_demo.py`: a
$16\ \mathrm{km}\times5.5\ \mathrm{km}$ region discretised into $16\times12=192$
cells, a homogeneous $3000\ \mathrm{m\,s^{-1}}$ reference, two acquisitions — a
crossing one (144 rays) and a one-sided one (100 rays) — straight rays, and 5 ms
travel-time noise.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** the three causes of a model discrepancy: data coverage,
   regularisation and measurement noise, and **test** them separately.
2. **Compute** the mutual correlation of two models and **show** that it
   concentrates where the ray coverage is good.
3. **Demonstrate** a large discrepancy produced by a change of damping alone,
   with no change in the data whatsoever.
4. **Quantify** what combining two data sets buys: agreement or accuracy, and
   which one.
5. **Build** a vote map for an ensemble of models and **decide** which parts of
   an image it licenses you to interpret.
6. **Write** a comparison protocol that a reader could reproduce.

## Prerequisites

- [03 Resolution, Null Space and Model Covariance](03-resolution-and-nullspace.md) —
  the machinery that explains the discrepancies.
- [06 Global Mantle Tomography](06-global-mantle-tomography.md) — the global
  version of the same problem.
- [18-02 Linear Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/README.md) —
  the general theory of well- and ill-posed comparisons.

## 1. Three causes, three tests

When two tomographic models of the same region disagree, the disagreement comes
from one of three places, and each can be tested in isolation:

| cause | how to test it | what the demonstration measures |
|---|---|---|
| **coverage** — different ray geometries | correlate the models as a function of local ray count | worst-covered quarter: correlation 0.050; best-covered quarter: 0.447 |
| **regularisation** — same data, different damping | invert the same data twice with two stated dampings | correlation 0.416, difference 57 per cent of the true anomaly |
| **noise** — different realisations, same geometry | invert several noise realisations and build an ensemble | sign agreement 0.966 across 30 models |

Only the first is about the Earth. The second and third are about the
inversions, and in the demonstration each of them alone is enough to produce a
disagreement comparable to the anomaly being studied.

## 2. Two models of one Earth

Inverting two different ray sets from the *same* synthetic Earth:

| quantity | value |
|---|---|
| crossing acquisition | 144 rays, 0 cells without a ray, model rms $2.6038\times10^{-2}$ |
| one-sided acquisition | 100 rays, 76 cells without a ray, model rms $2.2112\times10^{-2}$ |
| correlation of the two models | $+0.699$ |
| rms difference between them | $1.4195\times10^{-2}$ |
| rms of the true anomaly | $3.1227\times10^{-2}$ |
| difference as a fraction of the model | 0.455 |
| correlation of each with the truth | $+0.180$, $+0.214$ |

Both inversions are correct implementations operating on real (synthetic) data
from one Earth. They agree at the level a reader would call "similar" and differ
by 46 per cent of the anomaly's rms. Note also the last row: at this geometry
even the *best possible* answer is only weakly correlated with the true anomaly,
because rank 141 of 192 leaves most of the truth unreachable. A discrepancy map
must therefore be read against the resolution of both models, not against zero.

## 3. Where the models agree

Split the cells by how many rays cross them (crossing acquisition) and correlate
the two models within each subset:

| subset | correlation | rms difference | cells |
|---|---|---|---|
| worst-covered quarter (1-11 rays) | 0.050 | $1.3669\times10^{-2}$ | 45 |
| best-covered quarter (20-30 rays) | 0.447 | $7.6380\times10^{-3}$ | 38 |
| all cells | 0.663 | $1.0182\times10^{-2}$ | 192 |

Disagreement is not uniform: it concentrates exactly where the coverage is poor.
This converts a vague question — "why do the models differ?" — into a computable
one: is the difference, in that cell, larger than the resolution there? If it is
not, the difference is not evidence of anything except the two null spaces.

## 4. Amplitudes are a choice

Using one dataset, one code and one true Earth, sweeping only the damping:

| $\lambda/\lVert G\rVert$ | misfit (s) | recovered rms | fraction of truth | correlation with truth |
|---|---|---|---|---|
| $10^{-3}$ | $1.019\times10^{-5}$ | $2.6271\times10^{-2}$ | 0.841 | 0.250 |
| $10^{-2}$ | $2.987\times10^{-4}$ | $2.6096\times10^{-2}$ | 0.836 | 0.225 |
| $3\times10^{-2}$ | $1.732\times10^{-3}$ | $2.5699\times10^{-2}$ | 0.823 | 0.206 |
| $10^{-1}$ | $1.395\times10^{-2}$ | $2.3086\times10^{-2}$ | 0.739 | 0.175 |
| $3\times10^{-1}$ | $6.602\times10^{-2}$ | $1.3372\times10^{-2}$ | 0.428 | 0.143 |

The recovered amplitude spans a factor of two, and the correlation with the truth
falls as damping rises. The best any inversion of these rays could do correlated
with the truth at only $+0.251$, so the low correlation numbers are a statement
about the geometry (most of the anomaly is in the null space), not about the
choice of damping. The amplitude, however, *is* the choice: two papers that quote
"a 1.5 per cent anomaly" and "a 0.7 per cent anomaly" for the same region may be
looking at the same data with different damping.

## 5. Disagreement with no data difference at all

The same 144 travel times, the same code, two dampings
($\lambda = 10^{-2}\lVert G\rVert$ and $3\times10^{-1}\lVert G\rVert$):

| quantity | value |
|---|---|
| rms of the two models | $2.0886\times10^{-2}$, $9.6783\times10^{-3}$ |
| correlation between them | $+0.416$ |
| rms difference | $1.3151\times10^{-2}$, i.e. 57 per cent of the true anomaly's rms |
| correlation with the truth | $+0.195$, $+0.227$ |

Nothing differs except one number in the inversion. A discrepancy of this size
need not be evidence about the Earth at all. This is the honest core of the
"tomography controversy" literature: untangling the inversion from the Earth is
the work, and it requires the parameters, not just the figures.

## 6. What combining data buys

Two ray sets, inverted separately and jointly:

| quantity | value |
|---|---|
| correlation of the two separate models | $+0.717$ |
| rms difference of the two separate models | $1.4171\times10^{-2}$ |
| correlation of the joint model with the crossing model | $+0.934$ |
| rms difference of the joint model against the crossing model | $2.2054\times10^{-3}$ |
| rms error against the truth: crossing alone | $1.37\times10^{-2}$ |
| rms error against the truth: one-sided alone | $1.66\times10^{-2}$ |
| rms error against the truth: joint | $1.37\times10^{-2}$ |

Combining the data sets **collapses the disagreement** — the same inversion run
on the union of the two ray sets agrees with itself far better than the two
separate inversions agreed — while **barely changing the error against the
truth**. A joint inversion does not conjure up missing angular coverage; what it
removes is the part of the model that was unconstrained in one geometry and
arbitrary in the other. Agreement and accuracy are different quantities, and
combining data improves one of them. A reader who wants accuracy must add rays
that sample the disputed region from new directions.

## 7. Voting maps, and what they license

Build 30 models from the same rays and the same Earth: five damping values times
six noise realisations. For each cell, record the fraction of models that agree
on the sign of the anomaly:

| subset | mean agreement | worst cell | cells |
|---|---|---|---|
| best-covered quarter | 0.982 | 0.867 | 38 |
| worst-covered quarter | 0.961 | 0.800 | 45 |
| all cells | 0.966 | 0.667 | 192 |

The **sign** is the robust part of a tomographic image: 96.6 per cent of models
agree on it overall, and still 96.1 per cent in the worst-covered quarter, while
their amplitudes differ by factors of two and their mutual correlations range
from 0.4 to 0.9. A vote map is therefore the cheapest honest summary of an
ensemble: quote the sign where essentially everything agrees, and quote the
ensemble, with amplitudes, where it does not.

**Worked example — reading a discrepancy map.** A colleague's model differs from
yours by $+1$ per cent in a cell that your resolution matrix shows to have
$|R_{kk}| = 0.25$ and a point spread of three cells. Your model's own $1\sigma$
error there is 0.9 per cent and the displacement direction is largely along a
null-space vector. The honest report is: "the two models differ by 1 per cent in
a cell where neither resolves the sign of the anomaly better than 25 per cent,
so the difference is not attributable to structure; new rays crossing that cell
at a second angle are the test." The dishonest one is to add the difference to a
table of "mantle anomalies".

## 8. Assumptions and regime of validity

1. **Both models are minimum-norm or similarly regularised.** If one model uses a
   prior and the other does not, the difference includes the prior and the
   comparison must be made in the data space instead.
2. **The parametrisations are comparable.** Comparing a $16\times12$ cell model
   with a spherical-harmonic expansion requires projecting both into a common
   space — and the projection itself is a filter (lesson 06-06-06).
3. **The noise model is stated.** The ensemble of section 7 uses Gaussian noise;
   correlated errors would produce correlated model errors and a vote map that is
   too optimistic.
4. **A common reference model.** Differences in $v_0$ appear as differences in
   the perturbation, so both models must be referred to the same one.
5. **The "truth" is available only in synthetic tests.** Every quantitative
   statement about accuracy in this lesson is possible because the answer is
   known. With real data, the achievable statements are about *agreement* and
   about *resolution*, not about truth — and a paper that presents the first as
   the second has overclaimed.

## 9. Demonstration

[`code/tomography_controversies_demo.py`](code/tomography_controversies_demo.py)
produces every table above. Exercises:
[`exercises/07-tomography-controversies-exercises.md`](exercises/07-tomography-controversies-exercises.md),
solutions:
[`exercises/07-tomography-controversies-solutions.md`](exercises/07-tomography-controversies-solutions.md).

## Mastery checkpoint

> Two published models of a region disagree by 2 per cent in a $50\times50$ km
> cell. Your model's resolution there is $|R_{kk}| = 0.3$ with a 100 km point
> spread; the cell is crossed by 4 of your rays and 30 of theirs. **(a)** List the
> three candidate causes in order of how likely they are here, with the test that
> would settle each. **(b)** State what you would report if the disagreement
> survives all three tests. **(c)** Design the experiment that would actually
> break the tie, and state its cost in ray count. **(d)** Explain why a high
> correlation between two models is not evidence that either is right.

## Common pitfalls

1. **Reading agreement as accuracy.** Combining data sets raised the mutual
   correlation to 0.934 while leaving the error against the truth unchanged.
2. **Blaming the data when the damping is the difference.** One number, 57 per
   cent of the anomaly.
3. **Comparing amplitudes without damping.** A factor of two is available for
   free.
4. **Comparing models at different degrees.** A low-degree model aliases
   high-degree structure into its band.
5. **Summarising an ensemble by its mean.** The sign is robust and the amplitude
   is not; a mean amplitude is a number no model contains.
6. **Treating a vote map as a probability.** It is a frequency within the
   ensemble, and the ensemble is defined by the assumptions that generated it.

## Related modules

- [03 Resolution, Null Space and Model Covariance](03-resolution-and-nullspace.md).
- [06 Global Mantle Tomography](06-global-mantle-tomography.md).
- [06-07 Ambient Noise and Interferometry](../07-ambient-noise-and-interferometry/README.md) —
  an independent data type that samples the same region with different kernels.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  how to turn an ensemble into a defensible interval.
- [18-07 Joint and Multi-Physics Inversion](../../18-inverse-problems/07-joint-and-multi-physics-inversion/README.md) —
  the systematic treatment of section 6.
