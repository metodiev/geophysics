---
id: 21-06-03
title: "ML for Magnitude Estimation and Source Characterisation"
level: research
prereqs: ["21-06-01", "21-01-04", "06-04-04"]
estimated_minutes: 60
tags: [machine-learning, seismology, magnitude, regression, teaching]
---

# ML for Magnitude Estimation and Source Characterisation

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** what a magnitude estimator measures — a functional of the
   ground motion — from what it claims to report — a source size, and state
   where the two diverge.
2. **Derive** a simple attenuation-law estimator and **identify** its irreducible
   error as the amplitude scatter of the generating law.
3. **Compute** the standard error of a magnitude estimate from amplitude,
   distance and period scatter, and **state** the resulting magnitude
   uncertainty in magnitude units.
4. **Compare** a hand-written estimator with a trained regressor on a random
   split, and **explain** why a small gain reflects an extra observation rather
   than a better law.
5. **Measure** the extrapolation failure of a trained regressor outside its
   training magnitude range and **state** the deployment rule it implies.
6. **Evaluate** claims of source characterisation (focal mechanism, stress drop,
   moment) against the fact that the "ground truth" label is itself a model
   output.
7. **Specify** the reporting requirements for a magnitude model: units, scatter,
   bias as a function of magnitude, training range, and the reference catalogue.

All amplitudes, periods, magnitudes and residuals below are **SYNTHETIC**,
produced by
[`code/magnitude_and_source_ml_demo.py`](./code/magnitude_and_source_ml_demo.py).
No catalogue, station correction or published magnitude is read or quoted.

## Prerequisites

- [21-06-01 ML for Seismic Detection, Picking and Classification](./01-seismic-ml.md) —
  the upstream detector whose operating point selects which events get a
  magnitude at all.
- [21-01-04 Linear, Multiple and Robust Regression](../../21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md) —
  the estimators and diagnostics used here.
- [06-04-04 Magnitude Scales: Local, Body, Surface, Duration, Moment](../../06-seismology/04-earthquake-location-and-magnitude/04-magnitude-scales.md) —
  what the different magnitude scales measure, and why they disagree.
- [06-04-05 Magnitude Saturation and Why Moment Magnitude Is Preferred](../../06-seismology/04-earthquake-location-and-magnitude/05-magnitude-saturation.md) —
  the regime in which any amplitude-based estimator fails by construction.

## 1. Intuition: a magnitude is a functional of a recording

A magnitude is not a property of the earthquake alone. It is a **specified
functional of the ground motion**, chosen so that its value is roughly stable
across instruments, distances and regions. Local magnitude, for instance, is
essentially $\log_{10}$ of a peak amplitude with a distance correction. Two
consequences follow immediately:

- Any estimator of magnitude can only be as good as the information in the
  recording it uses. If the amplitude scatter of the physical law is
  $\sigma_{\log A} = 0.15$ in $\log_{10}$ units, then no estimator that uses only
  the amplitude can do better than $0.15$ magnitude units — and that is exactly
  what the demonstration measures.
- A learned model can *use more observations* than the classical formula (for
  example a period, which correlates with source size) and thereby reduce the
  scatter. That is a genuine improvement, but it is not "learning the physics":
  the physics was already exact in the generator.

Keeping these two claims apart is the whole of this lesson.

## 2. The synthetic measurement set

The generator draws 400 events with magnitude $M$ uniform on $[2.0, 5.0]$ and
hypocentral distance $R$ log-uniform from 5.0 km to 99.8 km. It then applies

$$\log_{10} A = M - \log_{10}\!\left(\frac{R}{10\ \mathrm{km}}\right)
+ \log_{10} A_{\mathrm{ref}} + \mathcal{N}(0, \sigma_{\log A}^2),$$

with $A$ in counts, $\log_{10}A_{\mathrm{ref}} = -1.0$ and
$\sigma_{\log A} = 0.15$; and

$$\log_{10} T = \log_{10}(0.4 + 0.1\,M) + \mathcal{N}(0, 0.05^2),$$

with the dominant period $T$ in seconds. The scatter is **multiplicative in
amplitude**, which in logarithmic units is additive and Gaussian — the standard
working model behind every magnitude residual.

Because the law is exact up to that scatter, inverting it gives

$$\hat M = \log_{10} A + \log_{10}\!\left(\frac{R}{10\ \mathrm{km}}\right)
- \log_{10} A_{\mathrm{ref}},$$

which recovers $M$ exactly when the scatter is zero. Its full-sample error here
is $0.145$ magnitude units — the irreducible amplitude scatter, recovered.

## 3. Measured performance on a random split

Splitting 400 events into 280 training and 120 held-out events and fitting a
ridge regression on three standardised features ($\log_{10}A$, $\log_{10}R$,
$\log_{10}T$) gives standardised coefficients

$$\text{intercept} = 3.519, \qquad
\log_{10}A: +0.904, \qquad
\log_{10}R: +0.353, \qquad
\log_{10}T: +0.031,$$

and the held-out errors

| Estimator | RMSE (magnitude units) | bias | scatter |
|---|---|---|---|
| hand-written inverse of the law | $0.141$ | $-0.005$ | $0.141$ |
| learned ridge regression | $0.137$ | $-0.008$ | $0.138$ |

The learned model gains $+0.004$ magnitude units of RMSE. Ten of those
coefficients are informative: the fitted $\log_{10}A$ coefficient is $+0.904$
rather than $1.0$, because the model shrinks the amplitude term when a correlated
feature is present, and the $\log_{10}T$ coefficient is only $+0.031$ because $T$
adds little once $A$ and $R$ are known in this generator. The model **rediscovered
the attenuation law**; it did not improve on it. Where a learned model performs
markedly better than a hand-written formula in the literature, the usual reason
is that the hand-written formula was missing something real — a site term, a
path term, a second phase — and not that the physics was unknown.

## 4. The extrapolation failure, measured

Now train only on events with $M \le 3.6$ (212 events) and test on the 188 events
with $M > 3.6$:

| Estimator | RMSE (magnitude units) | bias | scatter |
|---|---|---|---|
| hand-written inverse of the law | $0.145$ | $+0.006$ | $0.145$ |
| learned ridge regression | $0.179$ | $-0.113$ | $0.140$ |

The RMSE ratio learned/hand-written is $1.238$, and the learned estimator's mean
error in the top bin is $-0.113$ magnitude units. The mechanism is visible in the
scatter column: the scatter is unchanged ($0.140$ versus $0.145$) but a
systematic offset appears. A regressor fitted on a restricted range compresses
its predictions towards that range's centre — the classic shrinkage of regression
under range restriction — so it reports large events as smaller than they are.
The hand-written formula contains the correct functional form, so it keeps
working outside the training range; the learned model does not.

This is not an argument against learned magnitude models. It is the deployment
rule they come with: **a magnitude model must be validated over the magnitude
range it will be used on, and a model trained on $M\le3.6$ must not be pointed at
$M=6$** — which is exactly the range where magnitude is most consequential.

## 5. Source characterisation: what changes

Estimating *size* is a regression problem with a continuous target. Source
characterisation usually means something else — a focal mechanism, a moment
tensor, a stress drop, a rupture duration — and it brings three extra
difficulties.

1. **The target is a model output, not an observation.** A moment-tensor solution
   is the result of an inversion with its own data weighting and errors, so a
   network trained to reproduce it learns that inversion's bias as much as the
   Earth. Circularity is the default failure mode: if the labels come from
   waveform inversion, the model has learned the invertor.
2. **The mapping is not one-to-one.** Two different source geometries can produce
   nearly identical waveforms at a single station; the amplitude-only information
   that a magnitude problem enjoys is not available, and single-station focal
   mechanisms are unidentifiable without an assumption.
3. **The error metric is not a difference.** Focal mechanisms are compared by
   angular difference (Kagan angle), not by subtraction; stress drop is compared
   in log space because it spans orders of magnitude. A model that "wins" on RMSE
   in linear units may be worse in the metric that matters.

A defensible characterisation study therefore reports the reference inversion,
the angular or logarithmic metric, the station and azimuthal coverage, and — for
any claim about physics — a synthetic test in which the truth is known.

## 6. Reporting a magnitude model

The minimum set for a reproducible claim:

| Item | Example for this demonstration |
|---|---|
| training and test magnitude range | $M \in [2.0, 5.0]$, split at $3.6$ |
| distance range | $5.0$–$99.8\ \mathrm{km}$ |
| units | magnitude units for RMSE and bias; counts and s for inputs |
| reference | the generator's own magnitude, an exact number |
| residual distribution | bias and scatter per magnitude bin, not one RMSE |
| the amplitude scatter | $0.15$ in $\log_{10}$ units, the irreducible floor |

The last row is the one most often omitted. Without a stated irreducible floor it
is impossible for a reader to tell whether a model with RMSE $0.137$ is at the
information limit or leaving $0.10$ on the table.

## 7. Assumptions and regime of validity

1. **A single, distance-independent attenuation exponent.** Real path effects
   vary with region, depth and frequency.
2. **No site term.** Every station has its own amplification; a model trained
   across stations absorbs the mean site effect and hides the spread.
3. **No saturation.** Amplitude-based scales saturate above about
   $M\approx6.5$ ([06-04-05](../../06-seismology/04-earthquake-location-and-magnitude/05-magnitude-saturation.md));
   nothing in this generator models that.
4. **Gaussian errors in $\log_{10}A$.** Real magnitude residuals are
   heavy-tailed, because some records are contaminated.
5. **The true magnitude is known exactly.** In the demonstration it is the
   generator's number. In reality the reference catalogue magnitude is itself an
   estimate, so a measured bias is a bias *relative to the reference*, and two
   magnitude scales disagreeing by $0.2$ units can both be internally consistent.

## The honest summary

On an exactly known attenuation law with $0.15$ magnitude units of amplitude
scatter, a hand-written inverse reaches RMSE $0.141$ and a learned regressor
$0.137$ on a random split: the gain is $0.004$, and the model has recovered the
law rather than discovered anything. Restricted to $M\le3.6$ and asked to predict
$M>3.6$, the learned regressor's RMSE rises to $0.179$ with a $-0.113$ bias while
the hand-written estimator holds at $0.145$: a range-restricted model fails
outside its range even when the underlying law is available to it. Source
characterisation is harder still, because its labels are model outputs and
circularity, not variance, is the dominant error. The numbers here are properties
of this generator; the requirements — state the training range, the units, the
irreducible scatter and the bias per bin — are general.

## Python demonstration

[`code/magnitude_and_source_ml_demo.py`](./code/magnitude_and_source_ml_demo.py)
prints every number quoted above. It:

1. prints the generator's parameters and the exact-law check that recovers the
   amplitude scatter ($0.145$ on the full sample);
2. fits a ridge regression on a random 70/30 split and prints the coefficients,
   the hand-written RMSE and the learned RMSE;
3. retrains on $M \le 3.6$ and reports both estimators on $M > 3.6$, with the
   RMSE ratio and the bias in the top bin;
4. prints the two structural warnings — that a small gain means the law was
   rediscovered, and that a range-restricted model must not be extrapolated —
   under a `SYNTHETIC` provenance line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/06-ml-in-geophysics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnitude_and_source_ml_demo.py
```

It runs in under 0.1 s (closed-form linear algebra only), reads no files, uses no
network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/03-magnitude-and-source-ml-exercises.md`](./exercises/03-magnitude-and-source-ml-exercises.md)
and [`exercises/03-magnitude-and-source-ml-solutions.md`](./exercises/03-magnitude-and-source-ml-solutions.md).

## Mastery checkpoint

Without notes:

1. The generator's amplitude scatter is $0.15$ in $\log_{10}$ units. State the
   smallest RMSE any estimator that never sees $T$ can achieve, and compare it
   with the measured $0.141$.
2. A model reports RMSE $0.137$ against a hand-written formula's $0.141$. State
   the two questions you must ask before calling this an improvement.
3. The extrapolation experiment gives RMSE $0.179$ and bias $-0.113$ for the
   learned model, with unchanged scatter. Explain the mechanism in two sentences.
4. Your colleague trains a moment-tensor predictor on inversion labels and
   reports a mean Kagan angle of $20°$ against those labels. State the
   circularity and the test that would break it.
5. Write the four-line methods paragraph that would make the $0.137$ number
   reproducible.

## Common pitfalls

1. **Calling a $0.004$ gain a discovery.** The physics was exact; the gain came
   from an extra observation.
2. **Reporting one RMSE over a wide magnitude range.** Bias varies with
   magnitude, and the top bin is where it hurts.
3. **Extrapolating a learned magnitude model.** Measured RMSE inflation is
   $1.238\times$ with a $-0.113$ bias just one magnitude unit past the training
   range.
4. **Treating inversion labels as ground truth.** A model trained on another
   model's output inherits its errors and its choices.
5. **Quoting magnitude to two decimals.** With scatter around $0.14$ magnitude
   units, the second decimal is not information.
6. **Ignoring saturation.** No amplitude-based estimator survives $M \gtrsim 6.5$
   without an explicit corner.

## Where this is used

- **Routine catalogue production**, where a fixed magnitude estimator sets the
  shape of the frequency–magnitude distribution used in hazard analysis
  ([06-11-01](../../06-seismology/11-earthquake-statistics-and-hazard/01-gutenberg-richter.md)).
- **Rapid response and tsunami warning**, where a fast, slightly biased magnitude
  is worth more than a slow, accurate one — provided the bias is documented.
- **Induced-seismicity reporting**, where traffic-light protocols are defined in
  magnitude units and a scale change can move an event across a legal threshold.
- **Discrimination of explosions from earthquakes**, where the source
  characterisation problem is genuinely multi-parameter and labels are scarce.
- **Ground-motion prediction**, where a magnitude error of $0.1$ units maps into
  a variance contribution that must be accounted for explicitly
  ([06-11-05](../../06-seismology/11-earthquake-statistics-and-hazard/05-ground-motion-models.md)).

## Related lessons

- [21-06-01 ML for Seismic Detection, Picking and Classification](./01-seismic-ml.md) —
  the detector that decides which events receive a magnitude.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](./09-ml-pitfalls-geophysics.md) —
  the general extrapolation failure measured here in magnitude units.
- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](../04-machine-learning-fundamentals/02-bias-variance.md) —
  the shrinkage mechanism behind the range-restricted bias.
- [18-05-01 Bayesian Inversion: The Formulation](../../18-inverse-problems/05-bayesian-inversion/01-bayes-inverse-formulation.md) —
  the framework in which a data-derived magnitude becomes a posterior with a
  stated uncertainty.
- [06-04-05 Magnitude Saturation and Why Moment Magnitude Is Preferred](../../06-seismology/04-earthquake-location-and-magnitude/05-magnitude-saturation.md) —
  the physics that limits the amplitude-based approach.

## Self-assessment checklist

- [ ] I can write the attenuation law and invert it by hand.
- [ ] I can identify the irreducible scatter of a magnitude estimator.
- [ ] I can explain why a small learned gain means the law was rediscovered.
- [ ] I can explain the shrinkage mechanism of range-restricted regression.
- [ ] I can state the deployment rule that follows from the extrapolation test.
- [ ] I can name the three difficulties of source characterisation beyond size.
- [ ] I can list the four numbers a magnitude-model report must contain.
