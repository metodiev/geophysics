---
id: 21-06-05
title: "ML-Based Denoising of Geophysical Signals"
level: research
prereqs: ["21-06-01", "21-05-05", "20-05-04"]
estimated_minutes: 60
tags: [machine-learning, denoising, signal-processing, dictionary-learning, teaching]
---

# ML-Based Denoising of Geophysical Signals

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** signal-to-noise ratio in dB for a synthetic trace and **compute**
   the improvement a denoiser delivers, distinguishing signal preserved from
   noise removed.
2. **Explain** why a band-pass and a learned dictionary remove noise for
   different reasons, and **predict** which one survives a change of wavelet.
3. **Construct** a dictionary denoiser from the principal components of clean
   training patches and **state** what its training data must contain.
4. **Measure** the effect of a badly chosen band-pass corner frequency and
   **explain** why removing signal energy can make the SNR worse than no
   processing at all.
5. **Quantify** the penalty of a mismatched training distribution and **state**
   the reporting requirement it implies.
6. **Distinguish** denoising for display from denoising as a preconditioning
   step, and **explain** why the second must be validated through the downstream
   task rather than through the SNR.
7. **Specify** the report of a denoiser: training distribution, metric and its
   units, the input SNR, the noise model, and the downstream metric it is
   supposed to improve.

Every trace and every decibel below is **SYNTHETIC**, produced by
[`code/denoising_ml_demo.py`](./code/denoising_ml_demo.py). No field record, no
published signal-to-noise improvement and no noise model taken from a
measurement is used.

## Prerequisites

- [21-06-01 ML for Seismic Detection, Picking and Classification](./01-seismic-ml.md) —
  the feature and operating-point vocabulary.
- [21-05-05 Autoencoders for Compression and Denoising](../../21-statistics-bayesian-ml/05-deep-learning/05-autoencoders.md) —
  the deep-learning version of the dictionary projection used here.
- [20-05-04 Noise Reduction Strategies in Practice](../../20-signal-processing/05-noise-and-random-signals/04-noise-reduction.md) —
  the classical toolbox this lesson benchmarks against.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md) —
  why "trained on clean data" is a strong assumption, not a detail.

## 1. Intuition: two ways to remove noise

Every denoiser must decide *what a signal looks like*, and the decision is where
the noise it removes comes from.

- A **band-pass** asserts that the signal lives in a frequency band. It keeps
  that band exactly and deletes everything else. It is blind to the waveform's
  shape and it needs no training data, but if any signal energy lies outside the
  band, that energy is deleted with the noise.
- A **learned dictionary** asserts that the signal can be written as a short
  combination of basis patterns seen during training. It keeps anything that
  resembles those patterns and projects everything else onto them. It preserves
  waveform shape that spans many frequencies — and it fails silently when the
  deployment signal differs from the training signal.

Both are projections. The measurement that separates them is not which one wins
on one example, but *how each one behaves when the assumption is violated*.

## 2. The synthetic traces

| Property | Value |
|---|---|
| trace length | 1 000 samples at 250 Hz (4.0 s) |
| clean training traces | 200 |
| clean test traces | 40 |
| wavelet | 30 Hz Ricker, Normalised |
| reflectivity | 40 spikes, Laplace amplitudes, same statistics in train and test |
| noise | Gaussian, white, 0.3 or 0.6 times the clean RMS |
| input SNR (measured) | $+10.18$ dB (0.3); $+4.15$ dB (0.6) |
| clean RMS | 0.0980 (arbitrary units — the simulation is unit-free) |

The two noise levels are quoted as **ratios**, so the nominal input SNR is
$20\log_{10}(1/r) = +10.46$ dB and $+4.44$ dB. The measured values in the table
are lower by 0.3 dB because a finite realisation's RMS is not exactly its nominal
value — a reminder to state whether an SNR is nominal or measured.

Signal-to-noise ratio is defined here as

$$\mathrm{SNR} = 20\log_{10}\frac{\lVert \text{clean}\rVert}
{\lVert \text{estimate} - \text{clean}\rVert}\ \text{[dB]},$$

that is, the ratio of the *whole* clean signal to the *whole* error, which
includes both the noise left behind and the signal that was destroyed.

## 3. The dictionary, and what it was trained on

The dictionary is built from 24 400 Hann-tapered patches of 32 samples (stride
8) taken from the 200 clean training traces. Its 16 leading principal components
capture $0.999819$ of the patch variance: within this generator, a 30 Hz
Ricker wavelet is almost perfectly described by 16 shapes.

Denoising is an overlap–add projection: each noisy patch is projected onto the
dictionary with a small ridge penalty, and the reconstructions are averaged with
Hann-squared weights. The penalty matters: with a rank-16 basis in a 32-sample
space, the projector already discards half the dimensions, and the ridge keeps
the remaining coefficients from chasing noise.

A second dictionary is trained the same way on traces built from **20 Hz**
wavelets, and is applied to the same 30 Hz test traces. That is the whole
experiment of §5.

## 4. Measured SNR, including a badly chosen band-pass corner

| noise ratio | input | BP 30 Hz | BP 40 Hz | BP 60 Hz | BP 80 Hz | learned |
|---|---|---|---|---|---|---|
| 0.3 | $+10.18$ | $+2.45$ | $+6.17$ | $+12.72$ | $+12.14$ | $+12.07$ |
| 0.6 | $+4.15$ | $+1.92$ | $+4.72$ | $+7.17$ | $+6.07$ | $+5.96$ |

Three results, each with a mechanism:

1. **A band-pass corner at the wavelet's own frequency is a disaster.** At 30 Hz
   the output SNR is $+2.45$ dB against an input of $+10.18$ dB: the processing
   makes the trace *seven times worse* in error energy. A 30 Hz Ricker has a
   broad spectrum whose high-frequency lobe carries a large fraction of its
   energy; cutting at 30 Hz deletes more signal than noise.
2. **The best corner beats the learned dictionary slightly** ($+12.72$ versus
   $+12.07$ dB at the low noise level), and it does so without any training data.
   A well-tuned classical filter is a strong baseline, and a denoising paper that
   does not report it has not shown that learning was necessary.
3. **The learned dictionary degrades faster with noise** ($+12.07 \rightarrow
   +5.96$ dB as the noise ratio doubles, a loss of 6.1 dB, against 5.6 dB for the
   60 Hz band-pass). Both methods are dominated by the noise level, not by the
   method.

The correct conclusion is not "filters are as good as learning". It is that the
**corner frequency is a modelling choice with a first-order effect**, and that
any learned method must be compared against the filter with its parameter tuned
on the same data.

## 5. The mismatched dictionary

| noise ratio | matched dictionary | trained on 20 Hz | penalty |
|---|---|---|---|
| 0.3 | $+12.06$ dB | $+10.45$ dB | $1.61$ dB |
| 0.6 | $+6.05$ dB | $+5.36$ dB | $0.69$ dB |

A dictionary trained on the wrong wavelet still improves the trace: the 20 Hz
patterns overlap the 30 Hz ones enough to capture a useful part of the signal.
The failure is therefore **partial and silent** — no error, no warning, just a
worse answer — and it is largest exactly where the SNR is highest, because at
low SNR the noise dominates the error and the mismatch is masked.

Two consequences for practice:

1. A denoiser must be reported together with the distribution it was trained on
   (wavelet type, frequency content, amplitude statistics, noise model,
   acquisition geometry). "Trained on seismic data" is not a description.
2. The mismatch test — train on a *deliberately wrong* distribution and report
   the penalty — is cheap, and it is the only thing that tells a reader how
   fragile the result is.

## 6. Denoising for display versus denoising for a downstream task

SNR is a proxy. What consumers need is:

| Consumer | Metric that matters | What a high SNR can hide |
|---|---|---|
| interpreter's display | continuity, no dimming | amplitude distortion that changes relative amplitudes |
| automatic picker | pick bias, pick scatter ([21-06-02](./02-phase-picking-ml.md)) | a wavelet distortion that shifts the onset |
| amplitude-versus-offset work | amplitude fidelity | a projection that flattens the amplitude trend |
| inversion | misfit and model error | removal of the weak signal the inversion needs |

A learned dictionary removes whatever does not lie in its 16-dimensional
subspace, and weak reflections in directions the dictionary does not span are
signal. The rule that follows is: **validate the denoiser through the downstream
task, not through the SNR**, and report both. The demonstration's clean-trace
reference is a luxury that no field data set provides; a correspondingly honest
field report substitutes a synthetic truth, a repeat-shoot comparison, or a
well-log-derived forward model.

## 7. Assumptions and regime of validity

1. **The noise is white and stationary.** Real seismic and geodetic noise is
   coloured and its spectrum changes with time of day and weather; the optimal
   corner moves with it.
2. **Training data are clean.** Clean traces come from other traces assumed
   clean, from synthetics, or from noise-free windows — each of which carries an
   assumption that this demonstration does not test.
3. **The signal statistics are stationary across the survey.** A dictionary
   trained in one area migrates imperfectly, as §5 measures.
4. **The patches are independent.** Overlapping patches are strongly
   correlated; the projector is therefore applied to correlated inputs, which
   changes the bias–variance balance but not the qualitative conclusions.
5. **SNR is the objective.** Every number here is an SNR in decibels in the
   unit-free simulation. A real study must state the amplitude units and whether
   the ratio is of RMS, of peak, or of energy.

## The honest summary

On synthetic 30 Hz traces at an input SNR of $+10.18$ dB, a 16-atom dictionary
trained on 200 clean traces reaches $+12.07$ dB while a 60 Hz band-pass reaches
$+12.72$ dB and a 30 Hz band-pass reaches $+2.45$ dB — worse than doing nothing.
A dictionary trained on 20 Hz wavelets instead of 30 Hz loses $1.61$ dB and
raises no error. The three transferable conclusions are: the classical baseline
must be tuned and reported; the corner frequency is a first-order modelling
choice that can destroy the signal; and a learned denoiser's performance is a
property of its training distribution, so the mismatch penalty belongs in the
report alongside the headline number. The decibels themselves belong to this
generator.

## Python demonstration

[`code/denoising_ml_demo.py`](./code/denoising_ml_demo.py) prints every number
quoted above. It:

1. generates 200 clean training traces and 40 clean test traces and prints the
   nominal input SNR for both noise ratios, noting the measured values;
2. builds a 16-atom dictionary by eigendecomposition of the clean patch Gram
   matrix, prints the patch count and the captured variance, and builds a
   mismatched dictionary on 20 Hz wavelets;
3. prints the measured SNR for both noise levels and five methods (input, four
   band-pass corners, learned dictionary);
4. repeats the measurement with the mismatched dictionary and prints the
   penalty, followed by the structural warnings and a `SYNTHETIC` line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/06-ml-in-geophysics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python denoising_ml_demo.py
```

It runs in under 1 s, reads no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/05-denoising-ml-exercises.md`](./exercises/05-denoising-ml-exercises.md)
and [`exercises/05-denoising-ml-solutions.md`](./exercises/05-denoising-ml-solutions.md).

## Mastery checkpoint

Without notes:

1. State why the 30 Hz band-pass is worse than no processing, and compute the
   error-energy factor it represents.
2. The learned dictionary reaches $+12.07$ dB and the best band-pass $+12.72$ dB.
   Write the two sentences that should appear next in a methods section.
3. A mismatched dictionary costs $1.61$ dB at the low noise level and $0.69$ dB
   at the high one. Explain why the penalty shrinks with more noise.
4. A colleague reports a denoiser with $+14$ dB SNR improvement and no baseline.
   State the three numbers you would ask for.

## Common pitfalls

1. **Comparing a learned denoiser with an untuned filter.** The corner frequency
   moves the result by more than 10 dB here.
2. **Assuming more processing means less error.** The 30 Hz band-pass increases
   the error energy by a factor of about 6.
3. **Reporting SNR without the input SNR or the units.** An improvement of 2 dB
   means different things at $+4$ dB and at $+20$ dB.
4. **Omitting the training distribution.** The mismatch penalty is silent and
   measurable.
5. **Validating a preconditioning step on the SNR alone.** The downstream task
   defines success.
6. **Claiming generality from one noise level.** Both methods lose 5–6 dB when
   the noise doubles.

## Where this is used

- **Seismic preprocessing**, where denoising precedes picking, amplitude analysis
  and inversion — each with its own fidelity requirement.
- **Microseismic and induced-seismicity monitoring**, where the target events are
  weak enough that the denoiser's bias is a fraction of the signal.
- **Geodetic and gravity time series**, where coloured noise and a slow signal
  make the choice of band a scientific decision rather than a cosmetic one.
- **Ground-penetrating radar and near-surface data**, where clutter is
  non-Gaussian and a learned prior trained on synthetics is the usual starting
  point.

## Related lessons

- [21-06-01 ML for Seismic Detection, Picking and Classification](./01-seismic-ml.md) —
  the detection step that a denoiser usually serves.
- [21-06-02 Deep-Learning Phase Picking: SeisBench and Beyond](./02-phase-picking-ml.md) —
  the picker whose bias a denoiser can create.
- [21-05-05 Autoencoders for Compression and Denoising](../05-deep-learning/05-autoencoders.md) —
  the same projection idea with a learned nonlinear encoder.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](./09-ml-pitfalls-geophysics.md) —
  the distribution-shift framework behind §5.
- [20-05-04 Noise Reduction Strategies in Practice](../../20-signal-processing/05-noise-and-random-signals/04-noise-reduction.md) —
  the classical baselines every learned denoiser should beat.

## Self-assessment checklist

- [ ] I can compute an SNR in dB and say whether it is nominal or measured.
- [ ] I can explain how a band-pass and a dictionary each decide what is signal.
- [ ] I can build a dictionary from clean patches and state what it assumes.
- [ ] I can predict the effect of a band-pass corner set at the wavelet's
      frequency.
- [ ] I can design a mismatch test and interpret its penalty.
- [ ] I can name the downstream consumers whose metrics outrank the SNR.
