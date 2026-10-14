# Module 20-04 — Deconvolution and Inverse Filtering

**Stages:** doctoral → research · **Prerequisites:** modules 20-01, 20-02 and
20-03; comfort with least squares.

This module is about undoing a convolution, and about why that is not the same as
dividing. The convolutional model says that a recorded trace is the Earth's
reflectivity convolved with a source wavelet, plus noise. Inverting it would be a
division if the wavelet's spectrum were bounded away from zero; but a wavelet is
band-limited, so the division amplifies noise without bound wherever the wavelet
is weak. The whole module is built around that single defect and the two honest
responses to it: measure the noise and regularise to match it, or abandon the
explicit wavelet and invert the trace's statistics instead.

The four lessons follow that split. Lesson 01 sets up the inverse problem, exposes
its conditioning, and derives the water-level (Tikhonov) solution, measuring the
three-way trade of resolution, noise gain and forward-model bias. Lesson 02 takes
the statistical route — spiking and predictive deconvolution from the trace
autocorrelation by the Levinson recursion — which needs no known wavelet but does
need a minimum-phase one, and measures what happens when that assumption holds and
when it fails. Lesson 03 derives the Wiener filter from least squares, verifies the
orthogonality condition numerically, and shows that the optimal filter is the
same regularised inverse in the frequency domain. Lesson 04 returns to the noise:
where in the spectrum it enters, how much resolution it actually costs, and why
prewhitening suppresses almost none of the signal.

The recurring measurement is the *forward residual*: convolve the recovered
reflectivity back with the wavelet and compare with the input. It is the one
diagnostic that is available without knowing the answer, and its growth with the
regularisation parameter is the bias you paid. All models and data in this module
are **SYNTHETIC**; no field record, well log or published wavelet is used.

## Learning objectives

By the end of this module you will be able to:

1. **Write** the convolutional model, **derive** the inverse filter, and
   **compute** the operator's condition number over its usable band.
2. **Derive** the damped inverse from regularised least squares, and **state** the
   resolution, noise-gain and bias trade it controls.
3. **Choose** a water level from a measured noise-to-signal ratio and **verify**
   that choice against an oracle sweep.
4. **Derive** the prediction-error filter from the Yule-Walker equations and
   **solve** them with the Levinson recursion.
5. **Measure** the spikiness gain of a spiking operator against a known
   reflectivity, and **explain** the role of the minimum-phase assumption.
6. **Configure** predictive deconvolution with a prediction gap and **show** that a
   mismatched gap does not suppress the multiple.
7. **Derive** the Wiener-Hopf normal equations, **solve** them, and **verify**
   optimality by orthogonality.
8. **Quantify** where deconvolution noise enters the spectrum and **decide** how
   much resolution the noise allows.

## Prerequisites

- [20-01-03 Convolution, Correlation and Filtering](../01-signals-and-systems/03-convolution-and-filters.md) —
  the convolution theorem used in every derivation.
- [20-03-01 FIR Filter Design: Windows, Parks-McClellan, Least Squares](../03-digital-filtering/01-fir-filters.md) —
  the operator-design and least-squares background.
- [20-03-04 Phase Response, Zero-Phase Filtering and Distortion](../03-digital-filtering/04-phase-and-zero-phase.md) —
  why the wavelet's phase decides whether a causal inverse exists.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md) —
  the general theory of the stabiliser used here.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Deconvolution: Concept, Ill-Posedness and Stabilisation](01-deconvolution-concept.md) | doctoral | The inverse is a division by a quantity that vanishes; the water level is a noise model |
| 02 | [Spiking (Predictive) Deconvolution and Wavelet Estimation](02-spiking-deconvolution.md) | research | Invert the statistics, not the wavelet — if the wavelet is minimum phase |
| 03 | [Wiener Filtering and Least-Squares Inverse Filters](03-wiener-filtering.md) | research | The best filter of a given length; orthogonality is the check |
| 04 | [Deconvolution in the Presence of Noise](04-deconvolution-noise.md) | research | The noise, not the wavelet, sets the resolution |

## Suggested path

**If you are new to deconvolution:** lessons 01 → 04 in order, running each
demonstration. Lesson 04 is where the numbers from 01 become a decision.

**If you know the convolutional model:** read 01 §3 and §5 (conditioning and the
NSR rule), then 03 §3.4 (the two derivations are the same filter).

**If you are preparing a research project:** 02 in full (the minimum-phase
assumption and its failure), 03 §3.2–3.3 (design delay and orthogonality), and 04
§3.4–3.5 (prewhitening and the resolution ceiling), plus the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-deconvolution-concept.md`](01-deconvolution-concept.md) | Lesson 01 |
| [`02-spiking-deconvolution.md`](02-spiking-deconvolution.md) | Lesson 02 |
| [`03-wiener-filtering.md`](03-wiener-filtering.md) | Lesson 03 |
| [`04-deconvolution-noise.md`](04-deconvolution-noise.md) | Lesson 04 |
| [`code/`](code) | Four runnable demonstrations, one per lesson |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |

## How to run the demos

```bash
cd 20-signal-processing/04-deconvolution-and-inverse-filtering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python deconvolution_concept_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spiking_deconvolution_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python wiener_filtering_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python deconvolution_noise_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access, completes in well
under a second, and exits 0.

## Mastery checkpoint

Complete this without notes:

> A trace has a known wavelet with usable band 5–80 Hz and a noise-to-signal power
> ratio of $4\times10^{-3}$. **(a)** Explain in one sentence why the inverse is
> ill-posed. **(b)** Compute a water level and state the rule. **(c)** State the
> three quantities that move in opposite directions as the water level changes.
> **(d)** State whether a spiking deconvolution could avoid the water level, and
> the assumption it would require. **(e)** Explain where the deconvolution noise
> lands in the spectrum, and why prewhitening costs so little resolution.

A worked version appears in the lesson-01 and lesson-04
[solutions](exercises/01-deconvolution-concept-solutions.md).

## Common pitfalls across this module

1. **Reporting a spikier result as a better result.** The naive inverse's error is
   $10^{13}$; spiky is not the same as correct.
2. **Tuning the water level by eye.** It is a noise model: estimate the noise and
   set it.
3. **Assuming a minimum-phase wavelet.** The autocorrelation carries no phase
   information; test the assumption against something independent.
4. **Setting the prediction gap from intuition.** Measure the multiple period from
   the autocorrelation.
5. **Confusing detection with estimation.** The matched filter maximises peak SNR;
   the Wiener filter minimises reconstruction error.
6. **Hoping for resolution the noise does not allow.** Past the noise floor, more
   resolution is less information.

## Related modules

- [20-03 Digital Filtering](../03-digital-filtering/README.md) — the filtering
  that precedes deconvolution and sets its noise.
- [20-05 Noise and Random Signals](../05-noise-and-random-signals/README.md) — the
  statistics that spiking deconvolution inverts.
- [20-07 Inverse Methods in Signal Processing](../07-inversion-in-signal-processing/README.md) —
  the sparse and L1 route to spikiness.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the systematic
  treatment of ill-posedness and regularisation.
- [06-08 Receiver Functions and Crustal Structure](../../06-seismology/08-receiver-functions-and-crustal-structure/README.md) —
  water-level deconvolution and its resolution trade in a crustal setting.
- [06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md) —
  deconvolution as one step of a processing flow.
