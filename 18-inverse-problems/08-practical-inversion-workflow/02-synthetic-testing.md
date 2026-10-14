---
id: 18-08-02
title: "Synthetic Testing, Checkerboards and Recovery Tests"
level: research
prereqs: ["18-08-01", "18-02-05"]
tags: [inverse-problems, workflow, checkerboard-test, resolution, point-spread-function]
---

# Synthetic Testing, Checkerboards and Recovery Tests

> All models and data in this module are **SYNTHETIC**. The blur-and-subsample
> operator and every pattern below are chosen teaching ingredients; no number is
> a measurement of the Earth.

## Learning objectives

By the end of this lesson you will be able to:

1. **Design** a synthetic experiment that measures the resolution of a stated
   inversion, and **state** what the experiment fixes and what it varies.
2. **Compute** a recovery curve — recovered amplitude versus pattern
   wavelength — and **read** the resolution length from it.
3. **Explain** the alignment trap: a single checkerboard gives an amplitude at
   one alignment, and a badly shifted pattern can be nearly invisible.
4. **Derive** and **interpret** the point-spread function as a row of the model
   resolution matrix, and **measure** its width and sidelobes.
5. **Distinguish** detection from resolution and **state** which one a
   checkerboard test measures.
6. **State** the two ways a checkerboard test is misused: as a picture rather
   than a curve, and as a proof of resolution rather than a measurement of it.

## Prerequisites

- [18-08-01 Setting Up a Solvable Inverse Problem](01-problem-setup.md) —
  resolution, effective parameters, the grid choice.
- [18-02-05 Resolution and Information Matrices in Interpretation](../02-linear-inverse-problems/05-resolution-matrices.md) —
  the resolution matrix this lesson samples.

## 1. What a synthetic test is for

A synthetic test answers one question: *for this operator, this noise level and
this regularisation, how faithfully would a known model be recovered?* It is
therefore a property of the **experiment plus processing**, not of the Earth.

The experiment fixes the operator $G$, the noise $\sigma$, the regularisation
$P_0$, and the truth $\mathbf{m}_{\text{true}}$; it varies the truth over a family
of patterns. The output is a curve or a number, never a picture. A picture of a
recovered checkerboard is an illustration of a curve that should have been
plotted.

## 2. Worked example: the recovery curve

`code/synthetic_testing_demo.py` uses a $24\times24$ grid, a Gaussian blur of
$\sigma = 1.4$ cells, subsampling every second cell (144 data), $1\%$ noise and a
Laplacian smoothness weight $0.05$. Checkerboards
$m_{ij}\propto\cos(2\pi x_i/P)\cos(2\pi y_j/P)$ of unit amplitude are pushed
through the experiment and inverted; the recovered amplitude is the projection of
the recovered model onto the pattern.

| period (cells) | 2 | 3 | 4 | 6 | 8 | 12 | 16 |
|---|---|---|---|---|---|---|---|
| recovered amplitude | 0.0012 | 0.0045 | 0.5680 | 0.9332 | 0.9875 | 0.9983 | 1.0004 |

Recovery falls below one half between a period of 3 and 4 cells. That is the
**resolution length** of this experiment for one-sided (positive) recovery:
patterns finer than it return with a fraction of their true amplitude, so an
inversion image showing a strong short-wavelength feature would be producing it
from the noise or from the prior, not from the data.

## 3. The alignment trap

A single checkerboard gives a number at one alignment. Shifting the pattern by
half a cell (a quarter of the period for $P=4$) changes the answer dramatically:

| shift (cells) | 0.0 | 0.5 | 1.0 | 1.5 | 2.0 |
|---|---|---|---|---|---|
| recovered amplitude | 0.5683 | 0.0951 | 0.0009 | 0.2276 | 0.5691 |

At a shift of one cell the pattern sits on a **null direction** of the operator:
the true signal leaves almost no trace in the data, so the recovery collapses to
0.0009. That is not a loss of resolution; it is the pattern being invisible to
this experiment. Two practical consequences:

- **Run several shifts, or a suite of patterns**, and report the *worst*
  recovery. A single well-aligned checkerboard flatters the result.
- **A poor recovery does not prove the region is unresolvable**, and a good
  recovery does not prove it is resolved for every pattern. The curve, with its
  minimum over alignment, is the measurement.

## 4. The point-spread function

The cleanest single number is the point-spread function, obtained from a row of
the model resolution matrix. Passing a unit spike through the experiment and
inverting gives the recovered peak, and the demo reports:

| quantity | value |
|---|---|
| recovered peak of a true unit spike | 0.3222 |
| cells above half the recovered peak | 5 |
| PSF half-width (cells) | 3 |
| most negative sidelobe | $-0.0531$ |
| $\operatorname{diag}R$ at the centre cell | 0.3222 |

Two facts follow. The recovered peak is one third of the true amplitude: the
inversion cannot return a spike, and any workflow that reports one is
over-recovering. The negative sidelobes are produced by the smoothness prior —
they are an artifact of the processing, not a structure, and any negative lobe in
an inversion image must be tested against the PSF before it is interpreted.

## 5. Detection is not resolution

A checkerboard test measures **resolution**. Detection is a different question: a
thin body can raise the data above the noise (detected) long after its shape is
unresolvable. If the aim is "is there a body here", do a detection test (add the
body, ask whether the residual exceeds the noise); if the aim is "what shape is
it", do a recovery test. Reporting one as the other is the commonest overclaim in
this area.

## 6. Numeric demonstration

```bash
cd 18-inverse-problems/08-practical-inversion-workflow/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python synthetic_testing_demo.py
```

Four sections: the spike/PSF; the recovery curve; the alignment sweep; the PSF
numbers. Print-only, seeded, exits 0 in well under a second.

## 7. Assumptions and regime of validity

1. **The test's operator must be the inversion's operator.** A checkerboard run
   with a different wavelet, grid or weighting measures nothing about the final
   model.
2. **The noise level must be the final one.** Resolution measured at 1% noise
   says nothing about a 10% data set.
3. **The regularisation must be the production one.** A different $\lambda$
   changes the curve and the PSF width.
4. **Amplitude recovery is one-sided.** Some patterns recover with amplitude
   above 1 (here 1.0004 at $P=16$) because the smoothness prior redistributes
   energy between patterns; the curve should be read for its shape, not its last
   digit.
5. **The truth family matters.** Checkerboards probe periodic structure; a
   layered or blocky target needs its own patterns (spikes, steps, random
   models) in addition.

## Mastery checkpoint

Without notes: **(a)** State the three quantities a synthetic test fixes before
it varies the truth. **(b)** From the recovery table, state the resolution length
and the period at which a *detection* claim could still be made. **(c)** Explain
the null-direction collapse at a shift of one cell using the operator's
subsampling. **(d)** Given a PSF of half-width 3 cells and a recovered image
showing a 1-cell anomaly, state what you would report.

## Common pitfalls

1. **Showing the recovered checkerboard as a picture.** Report the curve; the
   picture hides the alignment question.
2. **One alignment.** The worst recovery is the honest number.
3. **Reading a good checkerboard as proof of resolution.** It is a measurement
   for those patterns at that noise level.
4. **Confusing detection with resolution.** Section 5.
5. **Running the test with a different regularisation than production.** The
   result then describes an experiment you did not perform.

## Related modules

- [Setting Up a Solvable Inverse Problem](01-problem-setup.md).
- [Assessing a Model: Resolution, Artifacts, Alternatives](03-model-assessment.md).
- [Reporting Inversion Results Responsibly](04-reporting-inversion.md).
- [18-02-05 Resolution and Information Matrices in Interpretation](../02-linear-inverse-problems/05-resolution-matrices.md).

Code: [`code/synthetic_testing_demo.py`](code/synthetic_testing_demo.py).
Exercises: [`exercises/02-synthetic-testing-exercises.md`](exercises/02-synthetic-testing-exercises.md).
