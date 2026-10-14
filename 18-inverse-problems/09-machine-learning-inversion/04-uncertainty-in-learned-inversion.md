---
id: 18-09-04
title: "Uncertainty in Learned Inversion: Pitfalls and Calibration"
level: research
prereqs: ["18-09-01", "18-06-01"]
tags: [inverse-problems, machine-learning, uncertainty, calibration, ensembles]
---

# Uncertainty in Learned Inversion: Pitfalls and Calibration

> All models and data in this module are **SYNTHETIC**. The ensembles, the
> training distribution and the noise level are chosen teaching ingredients; no
> number below is a measurement of the Earth. Training is deliberately tiny
> (five small networks) and finishes in well under a second.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** aleatory, epistemic and structural uncertainty in a learned
   inverse, and **state** which one an ensemble of networks measures.
2. **Measure** calibration as empirical coverage of nominal intervals, and
   **state** the two directions of miscalibration.
3. **Compute** the ratio of realised error to reported uncertainty and **use** it
   as a one-number diagnostic.
4. **Measure** how coverage collapses under distribution shift while the reported
   uncertainty barely moves.
5. **State** why ensemble disagreement is a lower bound on ignorance, and
   **construct** a case in which every ensemble member agrees and is wrong.
6. **Design** a calibration report: nominal versus empirical coverage, in and out
   of distribution, with the shift family named.

## Prerequisites

- [18-09-01 Learned Inversion: Direct and Iterative Networks](01-learned-inversion.md) —
  the distributional argument.
- [18-06-01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](../06-uncertainty-quantification/01-uncertainty-taxonomy.md) —
  the vocabulary used throughout.

## 1. Three uncertainties in a learned inverse

- **Aleatory.** The measurement noise $\boldsymbol{\epsilon}$. It is in the data
  generation, and it is the only component a conventional inversion models
  properly.
- **Epistemic.** Ignorance of the model, given the data. A conventional inversion
  reports it as a posterior covariance; a learned inverse has to learn it.
- **Structural.** Ignorance of the relationship itself — the forward operator, the
  training distribution, the network family. Neither a posterior nor an ensemble
  measures this reliably, and it is the dominant term outside the training
  distribution.

An ensemble $\{f_{\theta_e}\}_{e=1}^{E}$ trained on resampled data measures
**disagreement among members**. That corresponds to epistemic uncertainty *within
the training distribution*, and to nothing else.

## 2. Worked example: miscalibration in distribution

`code/uncertainty_in_learned_demo.py` trains five small networks
($30\to24\tanh\to20$) on bootstrap resamples of a 2000-model synthetic training
set, and evaluates 600 test models.

| quantity | value |
|---|---|
| in-distribution ensemble MSE | $3.505\times10^{-3}$ |
| mean ensemble $\sigma$ | 0.0105 |
| mean $|\text{error}|$ | 0.0451 |
| error/$\sigma$ | 4.32 |
| coverage, $\pm1\sigma$ (nominal 68.3%) | 15.3% |
| coverage, $\pm2\sigma$ (nominal 95.4%) | 30.3% |

The ensemble is badly **under-dispersed**: its spread reaches only a fraction of
the realised error, so its intervals cover far less than they advertise. A
deliberately tiny ensemble is not calibrated, and there is no reason to expect one
to be. For comparison, a linear posterior with a smoothness prior on the same
problem has mean $\sigma = 0.3095$ and $\pm2\sigma$ coverage of **100%** — the
opposite failure, over-coverage, because its prior is conservative.

Both numbers are failures of a different sign. Both must be measured; neither can
be assumed.

## 3. Under distribution shift the error bars do not follow

| test set | mean error | mean $\sigma$ | error/$\sigma$ | coverage $\pm2\sigma$ |
|---|---|---|---|---|
| in-distribution | 0.0451 | 0.0105 | 4.32 | 30.3% |
| 8 sine modes | 0.1202 | 0.0111 | 10.78 | 11.8% |
| isolated spike | 0.1165 | 0.0086 | 13.63 | 13.4% |

The mean error grows by a factor of 2.7 while the ensemble spread stays at
$\approx0.01$. The ratio error/$\sigma$ worsens by a factor of 2.5–3.2, and the
coverage falls further. **An ensemble measures disagreement among its members;
when every member has learned the same wrong thing, they agree.** Disagreement is
a lower bound on ignorance, not a measure of it.

## 4. Confident and wrong, in one number

Fraction of model cells whose error exceeds the ensemble's own $\pm2\sigma$ band:

| test set | fraction outside | nominal |
|---|---|---|
| in-distribution | 69.65% | 4.6% |
| spike test set | 85.97% | 4.6% |

In distribution, the ensemble is wrong by more than its own 2-sigma band in
69.65% of cells, i.e. 15.2 times the rate it advertises; on the spike family the
factor is $85.97/4.6 = 18.7$. Reporting the ensemble sigma without this
measurement is reporting a number that has not been shown to mean anything.

The single most useful diagnostic in this lesson is the ratio error/$\sigma$: it
is computable without a truth if a held-out data set with known noise exists, and
it immediately reveals a factor-of-four miscalibration.

## 5. What to report for a learned inverse

1. **Held-out error**, in-distribution, with the test distribution named.
2. **Calibration table**: nominal versus empirical coverage for at least
   $\pm1\sigma$ and $\pm2\sigma$.
3. **The shift family and the same table on it**, so the reader can see the
   degradation rather than being told about it.
4. **The ensemble construction** (size, resampling scheme, seeds) and the training
   distribution's specification.
5. **The ratio error/$\sigma$**, if a held-out set with known noise is available.

A learned inverse reported without items 1–4 is not a measurement; it is a
demonstration.

## 6. Numeric demonstration

```bash
cd 18-inverse-problems/09-machine-learning-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python uncertainty_in_learned_demo.py
```

Four sections: the ensemble and the linear reference; in-distribution
calibration; the shift table; the fraction outside the advertised band.
Print-only, seeded, exits 0 in under a second.

## 7. Assumptions and regime of validity

1. **The ensemble is a lower bound.** Correlated errors among members are
   invisible; a systematic bias afflicting all members is not measured at all.
2. **Calibration is distribution-specific.** A calibration measured on one family
   says nothing about another; report the family.
3. **The linear reference is not a gold standard.** It over-covers here because
   its prior is conservative; calibration is a property of the pair
   (estimator, test distribution).
4. **Bootstrap resampling is one ensemble scheme.** Deep ensembles, dropout
   ensembles and quantile regression produce different spreads, all requiring the
   same coverage test.
5. **Coverage requires many test models.** With 600 test models and 20 cells, the
   standard error on a coverage estimate near 30% is about
   $\sqrt{0.3\cdot0.7/(600\cdot20)}\approx0.4\%$, adequate here, but small test
   sets cannot support calibration claims.

## Mastery checkpoint

Without notes: **(a)** Classify three uncertainties of a learned inverse and state
which one an ensemble measures. **(b)** Given mean error 0.0451 and mean $\sigma$
0.0105, compute the ratio and state the calibration failure in one sentence.
**(c)** Compute the factor by which the in-distribution coverage falls short of
nominal at $\pm2\sigma$. **(d)** Explain why a distribution-shift test is required
even when the in-distribution calibration is good.

## Common pitfalls

1. **Reporting ensemble sigma as a posterior standard deviation.** It is a spread
   of members, and here it is four times too small.
2. **Testing calibration only in distribution.** Section 3.
3. **Assuming a well-calibrated small ensemble exists.** Calibration must be
   measured, and re-measured after any change of distribution or architecture.
4. **Confusing aleatory with epistemic uncertainty.** The noise floor is not the
   ignorance of the model.
5. **Treating agreement as validation.** Section 3's last sentence.

## Related modules

- [Learned Inversion: Direct and Iterative Networks](01-learned-inversion.md).
- [Generative Priors: GANs, VAEs, Diffusion Models](03-generative-models-inversion.md).
- [18-06-01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](../06-uncertainty-quantification/01-uncertainty-taxonomy.md).
- [18-06-02 Monte Carlo Propagation and Its Convergence](../06-uncertainty-quantification/02-monte-carlo-uq.md).

Code: [`code/uncertainty_in_learned_demo.py`](code/uncertainty_in_learned_demo.py).
Exercises: [`exercises/04-uncertainty-in-learned-inversion-exercises.md`](exercises/04-uncertainty-in-learned-inversion-exercises.md).
