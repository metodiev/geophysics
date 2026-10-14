# 21 — Statistics, Bayesian Inference and Machine Learning

**Stages:** intermediate → research

Every quantity in geophysics is an estimate, and this folder is about the machinery
that turns a measurement into an estimate and an estimate into a defensible
statement. The tools are familiar — a mean, a variogram, a posterior, a loss
function — and the difficulty is never in the formula. It is in knowing what the
formula assumes, what it silently replaces, and how large the resulting error is.
The organising principle is therefore **stated assumptions with measured
consequences**: each method here is introduced with the assumption that licenses
it and a demonstration that quantifies what happens when the assumption fails. A
number is produced for the failure, not a warning. Ten spikes moved a sample mean
by $+7.3\ \%$ where the median moved by $+0.6\ \%$; a Gaussian and a lognormal fitted
to the same sample disagreed by a factor of $325$ about a tail probability; a
$100\ \mathrm m$ block mean carried only $33\ \%$ of the point variance it was
reported to summarise; a model comparison returned a tie at $0.17\sigma$; mean-field
variational inference reported $44.5\ \%$ of the true posterior standard deviation,
and exactly $\sqrt{1-\rho^{2}}$ was the reason. Each of those numbers is what the
assumption costs, and none of them is visible in the fitted model's output.

The second theme is that **validation is where an analysis is won or lost**, and
that the failure is usually quantitative rather than qualitative. A pipeline that
selected its features on the full data beat an honest one by $40.8\ \%$ on data with
**no signal at all**. A single hold-out came out $43\ \%$ below the cross-validated
error. A missing Jacobian in a sampler shifted an estimate by $3.3\ \%$, and no
convergence diagnostic noticed. $19\,000$ correlated MCMC draws were worth $3918$
independent ones. These are the errors that survive peer review, because the
model, the code and the plots are all correct; only the number is wrong, and only
a comparison against a properly blocked or properly resampled baseline exposes it.
This folder treats that baseline as part of the result rather than as an appendix:
every demonstration prints the comparison that makes its headline number
interpretable, including when that comparison is unflattering — a frozen
representation scored $0.9133$ against $0.9600$ for the raw features, and the
lesson reports it as the negative result it is.

The third theme is **honesty about provenance.** All data in this folder are
**SYNTHETIC**. Every demonstration generates its data from stated parameters,
implements its methods from scratch with NumPy and SciPy, prints the numbers the
lessons quote, seeds with `np.random.default_rng(20261014)`, needs no network,
creates no files and produces no plots. That choice is itself part of the
curriculum: a number whose generating process is written down can be checked, and
the habit of asking "where did this number come from?" is the habit the folder
exists to build. No demonstration here is evidence about a real formation,
network or hazard; each is evidence about a method.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Summarise** data with measures whose breakdown point and efficiency you can
   state, and **detect** the observations that decide the answer.
2. **Choose** a probability model from the data's support and tail behaviour, and
   **state** the tail risk the choice carries.
3. **Estimate** uncertainty by resampling, **state** what the resampling scheme
   assumes, and **report** intervals that respect the data's structure.
4. **Model** spatial continuity, **fit** and validate a variogram, and
   **interpolate** with kriging weights whose properties you can verify.
5. **Quantify** a posterior and **separate** the three sources of its uncertainty —
   the prior, the likelihood and the computation.
6. **Diagnose** an MCMC or variational fit, and **state** what the diagnostics can
   and cannot detect.
7. **Validate** a learner against honest baselines, **choose** a metric that matches
   the decision, and **identify** leakage before it inflates a score.
8. **Justify** a deep architecture as a statement about the data's structure, and
   **measure** the assumption it makes rather than asserting it.
9. **Report** an uncertainty, a search and a limitation as part of a result, in the
   form a reader can reproduce.

## Modules

| # | Module | Topics | Why it matters |
|---|---|---|---|
| 01 | [Statistics in Geophysical Practice](./01-statistics-in-practice/README.md) | Robust and descriptive measures; probability-model selection; bootstrap, jackknife and permutation tests; linear, multiple and robust regression; nonparametric methods and kernel density estimation; spatial and directional statistics; extreme value theory | The estimation vocabulary and the robustness machinery every later module assumes; the mean, the interval and the $p$-value are each given a failure mode here |
| 02 | [Geostatistics](./02-geostatistics/README.md) | Regionalised variables and support; variograms, covariance and model fitting; kriging (simple, ordinary, universal, indicator); conditional simulation; geostatistics combined with inversion | Spatial continuity made quantitative, with the support and the kriging variance treated as part of the result rather than as decoration |
| 03 | [Bayesian Inference](./03-bayesian-inference/README.md) | The Bayesian paradigm and subjective probability; conjugate priors; hierarchical models and exchangeability; MCMC in practice; variational inference; the Bayesian workflow | Where uncertainty is represented rather than bounded, and where the sampler and the diagnostic become objects of study in their own right |
| 04 | [Machine Learning Fundamentals](./04-machine-learning-fundamentals/README.md) | The supervised/unsupervised/reinforcement taxonomy; bias-variance; cross-validation, metrics and leakage; regularisation; trees and ensembles; feature engineering; PCA, ICA and manifolds; clustering | The discipline that decides whether a predictor is any good; leakage and metric choice are the two failures it exists to prevent |
| 05 | [Deep Learning](./05-deep-learning/README.md) | Feedforward networks and backpropagation; convolution; recurrences and gates; attention and transformers; autoencoders; generative models; self-supervised learning | Architectures as structural assumptions, each priced: $160$ parameters against $16\,793\,600$, a $40$-step dependence at $1.48\ \%$ of its gradient, attention overtaking a recurrence exactly at $T = d$ |
| 06 | [Machine Learning in Geophysics](./06-ml-in-geophysics/README.md) | Seismic detection, picking and classification; deep-learning phase picking; magnitude estimation and source characterisation; facies and lithology from well logs; denoising; mineral prospectivity; climate downscaling and emulation; remote sensing; the pitfalls of spurious correlation, non-stationarity and extrapolation | The applied end: where the methods of modules 04 and 05 meet real Earth data, and where their assumptions are tested by acquisition, geology and scale |
| 07 | [Time-Series Modelling and Forecasting](./07-time-series-and-forecasting/README.md) | AR, MA and ARIMA models; state-space models and Kalman filtering; statistical spectral analysis and significance testing; forecast evaluation, skill scores and calibration; point processes and seismicity rates | Sequential data with dependence built into the model, and the place where forecast skill is defined rigorously enough to be believed |
| 08 | [Causal Inference and Experimental Design](./08-causal-inference-and-design/README.md) | Experimental and survey design for Earth studies; causal inference methods and counterfactuals; attribution in climate and hazard science | The step beyond prediction: what a design or an attribution study can and cannot establish about a cause |
| 09 | [Ethical and Responsible Quantitative Practice](./09-ethical-and-responsible-analytics/README.md) | Statistical reproducibility, $p$-hacking and multiple comparisons; honest reporting of uncertainty and limitations; data ethics, Indigenous data sovereignty and geoscience | The professional standard the rest of the folder is held to: a reproducible analysis, an honest interval, and data used with consent and credit |

## The dependency spine

`01 → 02 → 03` is the statistical spine: summarise and resample, then model space,
then model uncertainty. `04 → 05 → 06` is the learning spine: validate a learner,
scale the model class, apply it. `07` depends on `01` and `03` — a state-space model
is a Bayesian model over time and its forecast intervals are conditional
distributions. `08` depends on `01` and `04`, because identification needs both an
estimator and a design. `09` depends on everything, because it is about how the
results of all the others are reported.

The two spines meet in several places, and the lessons link across rather than
duplicating: kriging is regression with a covariance (02 ↔ 04), a prior is a
regulariser (03 ↔ 04), the ELBO is a training loss (03 ↔ 05), and a variational
autoencoder is a Bayesian model with a neural likelihood (05 ↔ 03).

## Which modules do you actually need?

- **Analysing a survey or a monitoring record?** 01 in full, then 02 for anything
  spatially continuous, then 07 if the record is long.
- **Fitting a predictor?** 04 in full before anything in 05 or 06; leakage and
  metric choice invalidate more applied results than model choice does.
- **Reporting an uncertainty?** 01, 03 and the first two lessons of 09.
- **Reading a machine-learning paper?** 04 lessons 02 and 03, then the relevant
  architecture in 05, then the matching application in 06.
- **Working with spatial data and few samples?** 02 lessons 02–04 and 03 lesson 03:
  the variogram, the simulation and partial pooling are the three tools that make
  small samples defensible.

## Suggested paths

**The statistical path:** 01 → 02 → 03 → 07 → 08 → 09. Slow, and the right order
for a researcher who needs defensible uncertainty statements rather than
predictions.

**The machine-learning path:** 01 (lessons 03 and 05) → 04 → 05 → 06 → 09. The
applied route, with module 09 read last but before anything is published.

**The applied-geophysics path:** 01 (lesson 01) → 02 → 04 (lesson 03) → 06 → 09.
For a practitioner who already fits models and needs spatial honesty and
validation discipline.

**The uncertainty-quantification path:** 01 (lessons 03 and 07) → 02 (lessons 03
and 04) → 03 → 07 (lesson 02) → 09 (lesson 02). Extreme values, kriging variance,
posteriors and forecast calibration, in that order.

## Mastery checkpoint for the folder

A report claims a mean porosity from $40$ wells with a standard error of $\pm 0.05$
units, a kriged map of the same property, a trained classifier for a lithology, and
a statement that the property "increased significantly since 2015".

1. **The mean:** the wells are $100\ \mathrm m$-scale measurements used to describe a
   reservoir-scale volume. State what the support does to the variance and what the
   standard error becomes when it is respected.
2. **The map:** state the two diagnostics the variogram needs and the property the
   kriging weights must satisfy.
3. **The classifier:** state the split, the metric and the specific leakage modes
   you would check before believing the accuracy.
4. **The trend:** state what a $p$-value on a spatially correlated series measures
   when the correlations are ignored, and what replaces it.
5. **The report:** state the three things about provenance, uncertainty and search
   that must accompany the numbers for the analysis to be reproducible.

Worked versions appear as ★★★ exercises across modules 02, 04, 07 and 09.

## Conventions used throughout

- **All data are SYNTHETIC.** Generated from the stated parameters, seeded with
  `np.random.default_rng(20261014)`. No demonstration reads a file or the network.
- **Every quoted number is printed by a demonstration.** The lesson text and the
  demo output agree; either can be used to check the other.
- **Levels.** `intermediate`, `advanced`, `graduate`, `doctoral` and `research`
  describe the prerequisite background, not the importance of the lesson. The
  levels rise across the folder: statistics and spatial modelling start at
  `intermediate`/`graduate`, the Bayesian and deep-learning modules are
  `doctoral`/`research`, and the applied and ethical modules are `research`.
- **Companions.** Each lesson has an exercise set and a worked solution set under
  `exercises/`, graded ★ through ★★★; the ★★★ problems are research designs and
  are expected to be specified to the point of being executable.
- **Estimates carry their comparison.** A metric appears with the baseline that
  makes it interpretable — a mean with a median, a hold-out with a cross-validated
  error, a probe with the raw-feature score.

## A caution about numbers in this folder

Every number here is an artefact of a synthetic generating process described in the
lesson that quotes it. The magnitudes are chosen to be realistic in scale and in
sign — a $3.3\ \%$ sampler bias, a $33\ \%$ loss of point variance under blocking, a
$104\,960\times$ parameter saving — but none of them is a measurement of a real
formation, survey, network or hazard, and none should be cited as one. What
transfers is the **mechanism**: the reason a missing Jacobian biases an estimate,
why a block mean has a smaller variance than the points it averages, why weight
sharing is cheap. Use the numbers to calibrate intuition, and the mechanisms to
design the check on your own data.

## How to use the code

Each module has a `code/` directory of print-only demonstrations and each lesson
names the one that produces its numbers. Run them with the project virtual
environment:

```bash
cd 21-statistics-bayesian-ml/01-statistics-in-practice/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python descriptive_statistics_demo.py
```

Replace the module directory and the script name with the pair given in the
lesson's "Python demonstration" section. Every script prints labelled sections,
exits 0, and runs in seconds; the longest demonstrations use a few seconds of
full-batch training and nothing more.

## Where this folder sits

- **[01 Mathematics](../01-mathematics/README.md)** — probability, linear algebra,
  estimation theory and optimisation are the prerequisites; module 21-01 assumes
  the estimation material directly.
- **[18 Inverse Problems](../18-inverse-problems/README.md)** — inference as
  optimisation under constraints; geostatistics and Bayes both reappear there as
  priors.
- **[19 Numerical Modeling and HPC](../19-numerical-modeling-hpc/README.md)** — the
  linear algebra and the sampling algorithms that make the posteriors and the
  kriging systems computable.
- **[20 Signal Processing and Time-Series Analysis](../20-signal-processing/README.md)** —
  the deterministic and spectral view of the same records this folder models
  probabilistically; the two are complementary and cross-linked.
- **[22 Data Engineering and Reproducibility](../22-data-engineering-reproducibility/01-research-software-engineering/README.md)** — research
  software engineering, reproducible workflows and data formats: where the data and
  the pipeline that produces these numbers come from.
- **[23 Field Methods and Instruments](../23-field-methods-instruments/01-field-safety-and-planning/README.md)** —
  planning, acquisition and instrumentation: the measurement that produces the
  numbers, and the acquisition effects that become biases once modelled.
- **[24 Research Papers and Scientific Writing](../24-research-papers-writing/README.md)** —
  how the results of this folder are reported, with module 21-09 as the statistical
  half of that standard.
