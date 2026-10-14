# Module 21-06 — Machine Learning in Geophysics

**Stages:** research · **Prerequisites:** modules 21-01, 21-04; a working
knowledge of the geophysical method being learned.

This module is where the machine-learning toolkit built in 21-04 and 21-05 meets
real geophysical tasks. Each lesson takes one task — detection, phase picking,
magnitude estimation, facies prediction, denoising, prospectivity mapping,
downscaling, land-cover classification — states what its label actually is, and
then *measures* one thing on synthetic data whose truth is known: an operating
point, a pick bias, an extrapolation failure, a validation inflation.

The organising idea is that **in geophysics the label, the split and the
distribution are the modelling decisions, and the architecture is the least
important choice.** Every lesson therefore reports the same four things: the
definition of the target, the split that matches the deployment geometry, the
per-class or per-range breakdown of the error, and the mechanism behind the
failure that the aggregate metric hides. Lesson 09 collects the four general
failure modes — spurious correlation, non-stationarity, extrapolation and
selection leakage — that the earlier lessons meet in their specific settings.

All models, data and numbers in this module are **SYNTHETIC**. Each demonstration
generates its own series, grids or traces, seeds `np.random.default_rng(20261014)`,
prints labelled results with units, and reads no data from disk or network. No
measured value, catalogue, spectrum or published accuracy figure is quoted
anywhere; where a real-world quantity is mentioned, it is described as varying by
source and to be checked.

## Learning objectives

By the end of this module you will be able to:

1. State the target and the label of a geophysical learning task precisely enough
   that the achievable precision and the failure modes follow from the definition.
2. Report a detector as a (threshold, false-positive rate, true-positive rate)
   triple at a stated event prior, and refuse to substitute an AUC for it.
3. Recognise a label-convention artefact — such as the $-0.180$ s pick bias of a
   window-classification picker — and choose a target that removes it.
4. Choose an evaluation split that matches the deployment question: event-,
   station-, bed-, block- or regime-disjoint, and say what each one tests.
5. Read a confusion matrix and report per-class recall whenever the class
   proportions are unbalanced, which in stratigraphy and land cover they always are.
6. Measure the cost of a distribution shift — a radiometric offset, a regime change,
   a mismatched training distribution — and state what no amount of extra data
   from the training distribution can repair.
7. Bound a model's fitted range and refuse to extrapolate a learned regressor
   outside it, quantifying the penalty when you must.
8. Put every data-dependent step inside the cross-validation fold, and report the
   lower, noisier, honest score that results.

## Prerequisites

- [21-04-01 ML Taxonomy: Supervised, Unsupervised, Reinforcement](../04-machine-learning-fundamentals/01-ml-taxonomy.md) —
  the task families used throughout.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../04-machine-learning-fundamentals/03-model-assessment.md) —
  the split discipline every lesson applies.
- [21-04-05 Decision Trees, Random Forests and Gradient Boosting](../04-machine-learning-fundamentals/05-trees-and-ensembles.md) —
  the model family used as a second classifier in lessons 04 and 08.
- [21-05-02 Convolutional Networks for Seismic and Image Data](../05-deep-learning/02-cnns.md) —
  the architectures behind the pickers of lesson 02.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md) —
  the statistics of every noise model in this module.
- [05-08-07 Log Interpretation, Petrophysics and Uncertainty](../../05-core-geophysics/08-geophysical-logging/07-log-interpretation.md) —
  the physical meaning of the logs classified in lesson 04.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [ML for Seismic Detection, Picking and Classification](01-seismic-ml.md) | research | Four features and a logistic regression double the TPR at a 5% false-positive budget; the AUC says nothing about it |
| 02 | [Deep-Learning Phase Picking: SeisBench and Beyond](02-phase-picking-ml.md) | research | Window labels give a $-0.180$ s pick bias; the regime, not the method, decides the ranking of two pickers |
| 03 | [ML for Magnitude Estimation and Source Characterisation](03-magnitude-and-source-ml.md) | research | A learned regressor recovers the attenuation law, then errs by $0.113$ magnitude units one unit outside its training range |
| 04 | [Facies and Lithology Prediction from Well Logs](04-facies-and-lithology.md) | research | Overall accuracy stays at 0.96 across three splits while deep-sand recall is 0.60 |
| 05 | [ML-Based Denoising of Geophysical Signals](05-denoising-ml.md) | research | A band-pass corner at the wavelet's frequency makes the trace 5.9× worse; a mismatched dictionary costs 1.61 dB silently |
| 06 | [ML for Mineral Prospectivity Mapping](06-mineral-prospectivity-ml.md) | research | The negative sampling design moves the AUC by 0.111; the fold design by at most 0.026 |
| 07 | [ML for Climate Downscaling and Emulation](07-climate-ml.md) | research | A $3.32$ K warming costs 16% RMSE; a change of lapse-rate regime costs $3.2\times$ |
| 08 | [ML for Remote Sensing Classification](08-remote-sensing-ml.md) | research | Dropping half the spectrum costs 0.309 kappa; a $0.02$ reflectance offset costs 0.084 and raises no error |
| 09 | [Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](09-ml-pitfalls-geophysics.md) | research | 38% of independent random-walk pairs correlate above 0.5; pre-split feature selection manufactures $R^2 = 0.602$ from nothing |

## Suggested path

**If you are new to applied ML in geophysics:** lessons 01, 04 and 09. Lesson 01
builds the operating-point vocabulary, lesson 04 shows the imbalance trap, and
lesson 09 collects the four failure modes.

**If you are building a picking or detection pipeline:** lessons 01, 02 and 05, in
that order. Lesson 02's label-convention bias and lesson 05's downstream-metric
argument are the two results most often missing from the papers.

**If you work with maps or grids:** lessons 06, 07 and 08. The three lessons share
one structure — a transfer that is invisible in the training statistics — and
lesson 06 supplies the spatial-block validation that the other two assume.

**If you are preparing a research project:** lesson 09 plus the ★★★ exercises of
every lesson; each specifies an experiment you can run on your own data, including
the sizing needed to resolve the effect you are claiming.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-seismic-ml.md`](01-seismic-ml.md) | Lesson 01 — detection, picking and classification |
| [`02-phase-picking-ml.md`](02-phase-picking-ml.md) | Lesson 02 — deep-learning phase picking |
| [`03-magnitude-and-source-ml.md`](03-magnitude-and-source-ml.md) | Lesson 03 — magnitude and source characterisation |
| [`04-facies-and-lithology.md`](04-facies-and-lithology.md) | Lesson 04 — facies from well logs |
| [`05-denoising-ml.md`](05-denoising-ml.md) | Lesson 05 — learned denoising |
| [`06-mineral-prospectivity-ml.md`](06-mineral-prospectivity-ml.md) | Lesson 06 — prospectivity mapping |
| [`07-climate-ml.md`](07-climate-ml.md) | Lesson 07 — downscaling and emulation |
| [`08-remote-sensing-ml.md`](08-remote-sensing-ml.md) | Lesson 08 — land-cover classification |
| [`09-ml-pitfalls-geophysics.md`](09-ml-pitfalls-geophysics.md) | Lesson 09 — the four failure modes |
| [`exercises/`](exercises) | Graded exercises and worked solutions for all nine lessons |
| [`code/`](code) | Nine runnable demonstrations, one per lesson |

| Script | What it prints |
|---|---|
| [`code/seismic_ml_demo.py`](code/seismic_ml_demo.py) | Feature medians, STA/LTA operating points, logistic-regression coefficients, AUC and two false-positive budgets |
| [`code/phase_picking_ml_demo.py`](code/phase_picking_ml_demo.py) | Pick bias, MAE, scatter and tolerance fractions for two pickers at two signal-to-noise ratios |
| [`code/magnitude_and_source_ml_demo.py`](code/magnitude_and_source_ml_demo.py) | Attenuation-law check, ridge coefficients, and the random-split versus extrapolation error |
| [`code/facies_and_lithology_demo.py`](code/facies_and_lithology_demo.py) | Bed count, depth-dependent proportions, three splits, and the per-class recall table |
| [`code/denoising_ml_demo.py`](code/denoising_ml_demo.py) | Patch count, captured variance, and a band-pass-versus-dictionary SNR table with a mismatch penalty |
| [`code/mineral_prospectivity_ml_demo.py`](code/mineral_prospectivity_ml_demo.py) | Two negative designs × two fold designs, and the top-10% targeting efficiency |
| [`code/climate_ml_demo.py`](code/climate_ml_demo.py) | Fitted lapse rate and a 3 × 4 RMSE/bias table over four evaluation blocks |
| [`code/remote_sensing_ml_demo.py`](code/remote_sensing_ml_demo.py) | Overall accuracy, kappa and per-class recall for four configurations |
| [`code/ml_pitfalls_geophysics_demo.py`](code/ml_pitfalls_geophysics_demo.py) | Random-walk correlation rates, shift inflation, polynomial extrapolation error, and the selection leak |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, pandas and
scikit-learn:

```bash
cd 21-statistics-bayesian-ml/06-ml-in-geophysics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_ml_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python phase_picking_ml_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnitude_and_source_ml_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python facies_and_lithology_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python denoising_ml_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mineral_prospectivity_ml_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_ml_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python remote_sensing_ml_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ml_pitfalls_geophysics_demo.py
```

Every demonstration is print-only: no plots, no files, no network. Each seeds
`np.random.default_rng(20261014)`, prints labelled results with units under a
numbered-section banner, prints a `SYNTHETIC` provenance line, and exits 0. The
slowest is `seismic_ml_demo.py` at about 3.5 s, almost all of it the scikit-learn
import; the rest take under 2 s.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A team reports a detector, a picker, a magnitude model and a facies model for a
> new network. **(a)** The detector is described by an AUC of 0.93. State the three
> numbers you need instead and why the AUC cannot give them. **(b)** The picker is
> described as 0.90 accurate with no tolerance; state the two numbers that would
> make the claim meaningful and explain how the demonstration's learned picker
> could be reported as either 0.345 or 0.740 accurate. **(c)** The magnitude model
> was trained on $M \le 3.6$ and is to be applied locally down to $M = 2$; state
> the validation you would require and the measured penalty for the analogous
> extrapolation. **(d)** The facies model reports overall accuracy 0.96 on a
> section that is 89% shale; state which class to interrogate, the metric to ask
> for, and the recall you would expect to see if the model were failing.
>
> Worked versions of (a)–(d) appear in the ★★★ exercises of lessons 01, 02, 03 and
> 04 respectively.

## Common pitfalls across this module

1. **Reporting an aggregate metric for an unbalanced or shifted problem.** The
   measured accuracies of 0.96 for facies (with 0.60 sand recall), 0.95 for land
   cover (with 0.354 water recall in one configuration) and 0.62 for prospectivity
   (with a targeting uplift of 1.16×) all hide the failure the study was about.
2. **Validating with a split that does not match the deployment geometry.** A
   random split hides the regime change (lesson 07), the radiometric offset
   (lesson 08) and the label-defining feature (lesson 06).
3. **Assuming a learned model inherits a physical law.** Lesson 03's regressor
   recovered the attenuation law to $0.004$ magnitude units and then failed by
   $0.113$ outside its training range.
4. **Comparing a learned method with an untuned classical baseline.** The band-pass
   corner moves the denoising result by more than 10 dB (lesson 05), and the
   negative sampling moves the prospectivity AUC by 0.111 (lesson 06).
5. **Treating the training distribution as a detail.** A mismatched dictionary
   costs 1.61 dB and raises no error; a $0.02$ reflectance offset costs 0.084 kappa
   and appears in no training statistic.
6. **Doing any data-dependent step before the split.** Selection leakage
   manufactured $R^2 = 0.602$ from pure noise (lesson 09).

## Related modules

- [21-01 Statistics in Geophysical Practice](../01-statistics-in-practice/README.md) —
  the estimators, tests and regression machinery that every lesson here builds on.
- [21-04 Machine Learning Fundamentals](../04-machine-learning-fundamentals/README.md) —
  bias–variance, cross-validation, regularisation and trees, which this module
  applies.
- [21-05 Deep Learning](../05-deep-learning/README.md) —
  the architectures behind the pickers and denoisers of lessons 02 and 05.
- [21-07 Time-Series Modelling and Forecasting](../07-time-series-and-forecasting/README.md) —
  the temporal models that formalise the non-stationarity met in lesson 09.
- [21-09 Ethical and Responsible Quantitative Practice](../09-ethical-and-responsible-analytics/README.md) —
  the reproducibility and reporting standards that the measurements here demand.
- [20-signal-processing](../../20-signal-processing/README.md) —
  the classical baselines every learned method must be compared against.
- [17-remote-sensing-gis](../../17-remote-sensing-gis/README.md) —
  the geospatial practice behind lessons 06, 07 and 08.
