# Module 18-09 — Machine Learning Approaches to Inversion

**Stages:** research · **Prerequisites:** modules 18-01 to 18-04; module 18-08.

This module treats neural networks, physics-informed networks and generative
models as what they are in inverse problems: **learned surrogates and learned
priors**. The single honest statement that organises it is that a network is a
function of the data, the operator and the distribution it was trained on. It
creates no information. Where it appears to beat a conventional inversion, the
gain is traceable to a learned prior, and where it fails, the failure is a
distribution shift — usually silent, because the network's output remains
smooth, bounded and plausible.

The module therefore measures rather than asserts. In-distribution it compares a
small network against a tuned Tikhonov inversion and finds the network 1.6 times
better in rms, for the stated reason that the training ensemble lives in a
three-dimensional subspace. Out of distribution the same network's error grows by
a factor of 7–12 while the physics-based inversion degrades by 1.8–4.6, so the
network becomes the worse method. Generated priors are measured by comparing
their in-family and out-of-family behaviour, including the fraction of recovered
energy forced into the learned subspace — about 95% even when the truth has only
1.7% of its energy there. Uncertainty estimates are measured by coverage: an
ensemble that advertises 95% coverage delivers 30% in distribution and 13% under
shift.

All models and data in this module are **SYNTHETIC**. The operators, ensembles,
networks and noise levels are chosen teaching ingredients, no dataset is real,
and no number is quoted from a published study. Training in every demonstration is
deliberately tiny — one hidden layer, a few hundred to a few thousand steps, well
under twenty seconds — so that the measurements can be reproduced in the time it
takes to read the lesson.

## Learning objectives

By the end of this module you will be able to:

1. **Write** the empirical-risk objective of a learned inverse and **identify**
   where the prior distribution enters.
2. **Measure** in-distribution and out-of-distribution error for a learned
   inverse and for a physics-based inversion on the same data.
3. **Explain** why a learned inverse can outperform a Tikhonov inversion
   in-distribution without containing information the operator lacks.
4. **Formulate** a physics-informed loss, compute a PDE residual through a
   network, and **state** when the method is a conventional collocation solver in
   a different basis.
5. **Measure** the failure of a physics-informed fit under a mis-specified
   equation, and **state** why no internal diagnostic detects it.
6. **Construct** a generative prior and **quantify** both its in-family gain and
   the fraction of recovered energy it forces into its own subspace.
7. **Measure** the calibration of a learned uncertainty by coverage, in and out of
   distribution, and **report** the diagnostic ratio error/$\sigma$.

## Prerequisites

- [18-02-01 Overdetermined Problems and Least Squares](../02-linear-inverse-problems/01-overdetermined.md).
- [18-04-01 Local Linearisation, Jacobians and Iteration](../04-nonlinear-inversion/01-local-linearization.md).
- [18-05-03 Priors: Informative, Reference and Their Influence](../05-bayesian-inversion/03-priors.md).
- [18-06-01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](../06-uncertainty-quantification/01-uncertainty-taxonomy.md).
- [18-08-03 Assessing a Model: Resolution, Artifacts, Alternatives](../08-practical-inversion-workflow/03-model-assessment.md).

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Learned Inversion: Direct and Iterative Networks](01-learned-inversion.md) | research | The advantage is the learned prior; the failure is silent and measured by error ratios |
| 02 | [Physics-Informed Neural Networks](02-physics-informed-networks.md) | research | The equation replaces the data; a wrong equation is undetectable internally |
| 03 | [Generative Priors: GANs, VAEs, Diffusion Models](03-generative-models-inversion.md) | research | A prior fills the null space; 95% of the answer is forced into the learned subspace |
| 04 | [Uncertainty in Learned Inversion: Pitfalls and Calibration](04-uncertainty-in-learned-inversion.md) | research | An ensemble measures disagreement, not ignorance; 95% advertised, 30% delivered |

## Suggested path

**If you are new to machine learning in inversion:** lessons 01 → 04 in order.
Lesson 01 sets the frame; lesson 04 supplies the only honest way to report a
learned uncertainty.

**If you come from machine learning:** read 01 §1 for the distributional argument,
02 §4–5 for the mis-specification failure, and 04 §1–3 for the calibration
vocabulary.

**If you are preparing a research project:** 03 §3–4 (the null space and the
subspace projection), 04 §4 (the confident-and-wrong measurement), and the ★★★
exercises of 02–04.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-learned-inversion.md`](01-learned-inversion.md) | Lesson 01 |
| [`02-physics-informed-networks.md`](02-physics-informed-networks.md) | Lesson 02 |
| [`03-generative-models-inversion.md`](03-generative-models-inversion.md) | Lesson 03 |
| [`04-uncertainty-in-learned-inversion.md`](04-uncertainty-in-learned-inversion.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy. No deep-learning framework is required: the networks are small enough to
train in NumPy.

```bash
cd 18-inverse-problems/09-machine-learning-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python learned_inversion_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python physics_informed_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python generative_priors_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python uncertainty_in_learned_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access and exits 0. The
slowest (the physics-informed fit) runs in about two seconds.

## Mastery checkpoint

Complete this without notes:

> A network inverts your data with an in-distribution held-out rms error of
> 0.0593, and a tuned Tikhonov inversion achieves 0.0964. **(a)** State where the
> network's advantage comes from and name the two assumptions it needs. **(b)**
> On eight-mode models the network's error becomes 0.0262 and the linear
> inversion's 0.0169; state which method you deploy for a target known to be
> outside the training ensemble, and why. **(c)** An ensemble reports a mean
> $\sigma$ of 0.0105 against a realised mean error of 0.0451; compute the ratio,
> state the calibration failure, and say what must be measured before the
> uncertainty can be quoted. **(d)** Name the one internal diagnostic that detects
> a mis-specified equation in a physics-informed fit — or state honestly that
> there is none.

A worked version of (a)–(c) appears in the lesson-01 and lesson-04
[solutions](exercises/01-learned-inversion-solutions.md).

## Common pitfalls across this module

1. **Reporting in-distribution performance as if it were general.**
2. **Treating a plausible-looking output as a validated one.** Learned inverses
   fail silently.
3. **Quoting ensemble spread as a posterior standard deviation.**
4. **Assuming a physics-informed fit validates the physics.**
5. **Comparing against an untuned conventional baseline.**
6. **Forgetting that every demonstration here is SYNTHETIC**, and that a
   distribution learned from synthetic models encodes the choices of whoever
   generated them.

## Related modules

- [07 Joint and Multi-Physics Inversion](../07-joint-and-multi-physics-inversion/README.md) —
  the classical route to combining information.
- [08 Practical Inversion Workflow](../08-practical-inversion-workflow/README.md) —
  the assessment and reporting discipline this module inherits.
- [05 Bayesian Inversion and Inference](../05-bayesian-inversion/README.md) —
  the posterior framework a learned prior plugs into.
- [06 Uncertainty Quantification](../06-uncertainty-quantification/README.md).
- [21 Statistics, Bayesian Inference and Machine Learning](../../21-statistics-bayesian-ml/README.md) —
  the statistical background for calibration and ensembles.
