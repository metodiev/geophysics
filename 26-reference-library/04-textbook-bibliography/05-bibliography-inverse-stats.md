---
id: 26-04-05
title: "Annotated Bibliography: Inverse Theory, Statistics and ML"
level: doctoral
prereqs: []
estimated_minutes: 30
tags: [reference, bibliography, inverse-theory, statistics, machine-learning]
---

# Annotated Bibliography: Inverse Theory, Statistics and ML

Inverse theory, statistics and machine learning are three literatures that
describe the same problem — inference from noisy, incomplete data — in three
vocabularies. This page lists the works worth owning in each, and says where the
vocabularies translate.

## How to use this page

Grouped by role: inverse theory for geophysics, general Bayesian inference,
classical statistics, and machine learning. The translation table at the end
maps the three vocabularies, which is the fastest way to read across them.

**Honesty statement about citations.** All works below are real. Journal volumes
and page numbers are omitted rather than guessed; verify them before citing. Two
widely used texts are legitimately available free from their authors' websites —
that does not remove the need to cite the printed edition.

*Provenance:* bibliographic reference only. No copyrighted text is reproduced.

## Inverse theory for geophysics

| Work | Level | Use it for | Not for |
|---|---|---|---|
| **Menke**, *Geophysical Data Analysis: Discrete Inverse Theory* (Academic Press; editions vary, 4th ed. published 2018) | advanced | The clearest entry point: least squares, the generalised inverse, resolution and covariance, with worked problems | Non-linear and Bayesian framing beyond an introduction |
| **Tarantola**, *Inverse Problem Theory and Methods for Model Parameter Estimation* (SIAM; 2005) | research | The canonical Bayesian formulation: probability densities over models, the null space, sampling, and honest treatment of uncertainty. Legitimately available as a free PDF from the author's site | A first course; the mathematics is dense |
| **Aster, Borchers & Thurber**, *Parameter Estimation and Inverse Problems* (Elsevier/Academic Press; 3rd ed. 2018) | advanced | The most usable textbook of the three: linear and non-linear inversion, Tikhonov methods, the L-curve, with computational exercises | Advanced Bayesian computation |
| **Parker**, *Geophysical Inverse Theory* (Princeton University Press; 1994) | research | Rigorous treatment of the continuous (Backus–Gilbert) inverse problem, resolving kernels and trade-offs | Implementation guidance |
| **Zhdanov**, *Inverse Theory and Applications in Geophysics* (Elsevier; 2nd ed. 2015) | advanced | Inversion as practised in EM and potential-field work, including regularisation families | A statistical viewpoint |
| **Sen & Stoffa**, *Global Optimization Methods in Geophysical Inversion* (Cambridge University Press; 2nd ed. 2013) | advanced | Simulated annealing, genetic algorithms, neighbourhood algorithms and their use when the misfit is non-convex | Gradient-based efficiency |
| **Hansen**, *Rank-Deficient and Discrete Ill-Posed Problems* (SIAM; 1998) | research | The numerical core of regularisation: parameter-choice methods and their failure modes | Geophysical interpretation |
| **Engl, Hanke & Neubauer**, *Regularization of Inverse Problems* (Kluwer; 1996) | research | Functional-analytic regularisation theory, for when the question is which family is consistent | Practical recipe selection |
| **Tikhonov & Arsenin**, *Solutions of Ill-Posed Problems* (Winston; 1977) | research | The origin of the regularisation idea | Modern notation or computation |

## Statistical inference and Bayesian computation

| Work | Level | Use it for | Not for |
|---|---|---|---|
| **Gelman, Carlin, Stern, Dunson, Vehtari & Rubin**, *Bayesian Data Analysis* (CRC Press; 3rd ed. 2013) | graduate | The standard applied Bayesian reference: hierarchical models, computation, model checking, and the discipline of posterior predictive checks | Geophysical notation |
| **MacKay**, *Information Theory, Inference, and Learning Algorithms* (Cambridge University Press; 2003) | advanced | The clearest account of the unity of inference and compression, with an honest discussion of Occam factors. Legitimately free online | Cookbook implementation |
| **Sivia & Skilling**, *Data Analysis: A Bayesian Tutorial* (Oxford University Press; 2nd ed. 2006) | intermediate | A short, physical introduction to Bayesian reasoning for scientists | Large-scale computation |
| **Robert & Casella**, *Monte Carlo Statistical Methods* (Springer; 2nd ed. 2004) | research | The theory and practice of MCMC, importance sampling and convergence diagnostics | A first exposure to statistics |
| **Efron & Tibshirani**, *An Introduction to the Bootstrap* (Chapman & Hall; 1993) | advanced | Resampling for error bars and confidence intervals without distributional assumptions; also the reason block resampling is needed for correlated data | Spatial statistics as such |
| **Kaipio & Somersalo**, *Statistical and Computational Inverse Problems* (Springer; 2005) | research | The Bayesian inverse-problem formulation with approximation-error modelling — directly relevant to discretisation choices | Elementary statistics |
| **Casella & Berger**, *Statistical Inference* (Duxbury; 2nd ed. 2002) | intermediate | The classical foundation: estimators, sufficiency, hypothesis testing, intervals | Bayesian computation |
| **Taylor**, *An Introduction to Error Analysis* (University Science Books; 2nd ed. 1997) | beginner–intermediate | Error propagation, significant figures and least squares, taught with unusual care | Advanced inference |
| **Bevington & Robinson**, *Data Reduction and Error Analysis for the Physical Sciences* (McGraw-Hill; 3rd ed. 2003, reissued by Waveland) | intermediate | Fitting, covariance and goodness-of-fit as a laboratory physicist needs them | Bayesian methods |
| **Wilks**, *Statistical Methods in the Atmospheric Sciences* (Academic Press/Elsevier; 3rd ed. 2011) | advanced | Hypothesis testing and multivariate methods with the worked examples a geoscientist can recognise | Spatial geostatistics |
| **von Storch & Zwiers**, *Statistical Analysis in Climate Research* (Cambridge University Press; 1999) | advanced | Spectral analysis, empirical orthogonal functions and significance testing for climate series | Sedimentary or geodetic data |

## Machine learning and data-driven modelling

| Work | Level | Use it for | Not for |
|---|---|---|---|
| **Bishop**, *Pattern Recognition and Machine Learning* (Springer; 2006) | advanced | Regression, classification, graphical models and approximate inference with a Bayesian framing | Deep architectures developed after its publication |
| **Hastie, Tibshirani & Friedman**, *The Elements of Statistical Learning* (Springer; 2nd ed. 2009) | advanced | The classical statistical-learning toolkit and, importantly, its bias–variance and model-selection reasoning | Deep learning |
| **Goodfellow, Bengio & Courville**, *Deep Learning* (MIT Press; 2016) | advanced | The conceptual and algorithmic reference for neural networks, including the optimisation and regularisation chapters that matter in practice | Statistical inference on small datasets |
| **Murphy**, *Probabilistic Machine Learning: An Introduction* (MIT Press; 2022) | advanced | A modern, unified probabilistic treatment; a good successor to Bishop. Legitimately free online with the printed edition | Geoscience-specific examples |
| **Rasmussen & Williams**, *Gaussian Processes for Machine Learning* (MIT Press; 2006) | research | Kernels, marginal likelihood and uncertainty quantification — the closest ML relative of kriging. Legitimately free online | Large-scale deep models |
| **Brunton & Kutz**, *Data-Driven Science and Engineering* (Cambridge University Press; 2nd ed. 2022) | advanced | SVD, sparse regression (SINDy), dynamic mode decomposition and neural networks for physical systems | Classical statistics |
| **Chollet**, *Deep Learning with Python* (Manning; editions vary) | intermediate | Implementation-oriented learning with a well-regarded framework | Theory or validation methodology |
| **Géron**, *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow* (O'Reilly; editions vary) | intermediate | Practical end-to-end workflows, including the data-splitting discipline that geoscientists most often skip | Statistical inference |

## Translating between the three vocabularies

| Inverse theory | Bayesian statistics | Machine learning |
|---|---|---|
| Model parameters $m$ | Parameters $\theta$ | Weights |
| Data $d$ | Observations $y$ | Features, targets |
| Misfit function | Negative log-likelihood | Loss function |
| Damping $\alpha\lVert Lm\rVert^{2}$ | Prior (usually Gaussian) | Regularisation / weight decay |
| Resolution matrix | Posterior covariance structure | Effective number of parameters |
| Linearised uncertainty | Laplace approximation | Hessian / Fisher information |
| Bootstrap or jackknife | Resampling posterior | Cross-validation, ensembling |
| Model selection | Evidence, Bayes factors | Validation error, information criteria |

## Which one to read, by need

| If you need to… | Start with |
|---|---|
| Invert a dataset for the first time | Menke, then Aster et al. |
| Justify an uncertainty statement | Tarantola, then Gelman et al. |
| Choose a damping parameter defensibly | Hansen |
| Model a non-convex misfit | Sen & Stoffa |
| Apply an ML model to geophysical data with honest error bars | Murphy or Rasmussen & Williams, plus the validation discipline in Hastie et al. |

## Assumptions and regime of validity

- Levels and recommendations are this repository's opinion.
- Machine-learning texts written for computer-vision benchmarks assume data
  volumes that most geophysical problems do not have; the *validation* chapters
  transfer, the architecture chapters often do not.
- Free online availability is noted only where it is a documented property of the
  work; verify from the publisher or the author's page.

## Related pages

- [Annotated Bibliography: Mathematics and Numerical Methods](./01-bibliography-mathematics.md)
- [Formula Sheet: Inverse Theory and Statistics](../03-formula-handbook/06-formulas-inverse-statistics.md)
- [18-inverse-problems folder overview](../../18-inverse-problems/README.md)
- [21-statistics-bayesian-ml folder overview](../../21-statistics-bayesian-ml/README.md)
