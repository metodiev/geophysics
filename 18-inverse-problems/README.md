# 18 — Inverse Problems, Optimization and Uncertainty Quantification

**Stages:** advanced → research

Geophysics does not measure the Earth; it measures responses, and infers the
Earth from them. That inference is never unique. The organising principle of this
folder is therefore the one that every other folder's honesty depends on:
**geophysical inversion is ill-posed, so the data do not determine the model, and
every solution is a choice** — of parametrisation, of regularisation, of prior.
A null space is not a defect to be removed by a cleverer solver; it is the
statement of what the measurement cannot see, and it is the first thing a
responsible inversion reports.

The central failure mode this folder exists to prevent is the model that arrives
without its uncertainty: a picture, a depth, a contrast, and no statement of what
else would have fitted the data equally well. That failure is not exotic. It is
the *default* outcome of an inversion, because a solver always returns something
and a regularised objective always has a minimiser. A model reported without its
null space and its admitted range is a claim the data may not support, and there
is no way for a reader to tell the difference from the figure alone.

A second difficulty runs through the folder and is stated here once, plainly:
**more machinery is not more information.** A second data set, a coupling term, a
rock-physics relation, a neural network and a learned prior each change the
answer by adding an assumption. Some of those assumptions are well founded and
some are not, and the only way to know which is to measure the effect: rank and
resolution for a joint operator, misfit for a coupling weight, out-of-distribution
error for a learned inverse, coverage for a reported uncertainty. Every
demonstration in this folder is built so that the measurement can be made and the
number printed.

A third theme follows from the first two and is deliberately repeated across the
modules: **the misfit is not the objective.** The model with the smallest misfit
can be the furthest from the truth, because the residual has a noise floor and
the model has a resolution limit. Choosing the regularisation weight from a stated
noise level (the discrepancy principle), reporting the admitted range, and
testing a claim against an independent datum are the practices that turn an
inversion result into a measurement. They are also the practices most often
omitted.

Four distinctions recur often enough to state once:

- **Resolution, detection and identification.** A feature can raise a residual
  (detected) long after its shape is unresolvable, and can be resolved long
  before its cause is identifiable. Reporting one as another is the commonest
  overclaim in this subject, and several lessons measure the difference with
  numbers.
- **Data, model and choice.** The measurements are data; the operator and the
  prior are models; the grid, the weight and the parametrisation are choices.
  A report in which these are not labelled cannot be audited.
- **Aleatory, epistemic and structural uncertainty.** Noise, ignorance and
  mis-specification behave differently. A posterior covariance models the first
  two, an ensemble measures a lower bound on the second, and neither reliably
  captures the third.
- **In-distribution and out-of-distribution.** Every learned or tuned component
  has a domain of validity. Outside it, performance does not degrade gracefully;
  it fails, and it usually fails silently.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Distinguish** forward from inverse problems, and **state** the practical
   asymmetry that makes the inverse direction hard.
2. **Test** a problem against Hadamard's conditions and **identify** which
   condition a given data set violates.
3. **Compute** the null space of a linear inverse problem and **report** the
   equivalence class of models that fit the data equally well.
4. **Derive** and apply the generalised inverse, least-squares, minimum-norm and
   SVD solutions, and **read** resolution and information matrices quantitatively.
5. **Choose** a regularisation and its weight from a stated noise level, and
   **state** the bias each choice imports.
6. **Linearise** a nonlinear problem, compute Jacobians, and **diagnose**
   convergence and local minima rather than assuming a good solution.
7. **Formulate** an inverse problem in Bayesian terms, sample the posterior, and
   **summarise** it with marginals, credible intervals and correlations.
8. **Propagate** uncertainty through a forward model and **report** the
   uncertainty of the prediction rather than of the model alone.
9. **Justify** a joint or multi-physics inversion by the complementary
   sensitivities of the operators involved, and **measure** the gain and the bias
   the coupling introduces.
10. **Set up**, **test** and **assess** an inversion workflow, and **report** a
    model with its resolution, its admitted range and its misfit.
11. **Evaluate** a learned inverse as a surrogate or a prior, and **measure** its
    out-of-distribution failure and the calibration of its uncertainty rather
    than claiming robustness.
12. **Write** an interpretation in which every number is labelled measured,
    modelled or chosen, and every claim is accompanied by the observation that
    would falsify it.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Foundations of Inverse Problems](./01-inverse-problem-foundations/README.md) | Forward versus inverse, well-posedness, null space and equivalence classes, discretisation and parameterisation, model and data spaces | The vocabulary every later module assumes; read it before anything else |
| 02 | [Linear Inverse Problems](./02-linear-inverse-problems/README.md) | Least squares, minimum-norm solutions, the generalised inverse, SVD analysis, resolution and information matrices, weighting and covariance | The exact solutions that nonlinear iteration reduces to, and the source of the resolution language |
| 03 | [Regularisation and Stabilisation](./03-regularization/README.md) | Tikhonov, parameter choice, sparsity, total variation, constraints, nonlinear regularisation | The machinery that makes an ill-posed problem answerable, and the bias it buys |
| 04 | [Nonlinear Inversion and Optimisation](./04-nonlinear-inversion/README.md) | Local linearisation, Gauss–Newton, conjugate gradients, global search, annealing, multi-start, convergence diagnosis | Almost every real forward model is nonlinear; this is how the linear theory is used in practice |
| 05 | [Bayesian Inversion and Inference](./05-bayesian-inversion/README.md) | Bayes' theorem, likelihoods, priors, MCMC, Hamiltonian samplers, posterior summaries, evidence, trans-dimensional sampling | Uncertainty as a distribution rather than an error bar, and the framework learned priors plug into |
| 06 | [Uncertainty Quantification](./06-uncertainty-quantification/README.md) | Taxonomy of uncertainty, Monte Carlo propagation, sensitivity analysis, surrogates, visualisation, decisions and value of information | Turns a posterior into a decision input, and makes the uncertainty of a prediction explicit |
| 07 | [Joint and Multi-Physics Inversion](./07-joint-and-multi-physics-inversion/README.md) | Complementary sensitivities, structural and petrophysical coupling, sequential versus simultaneous, weighting and over-coupling pitfalls | Where two measurements constrain what neither constrains alone, and where coupling manufactures structure |
| 08 | [Practical Inversion Workflow](./08-practical-inversion-workflow/README.md) | Problem setup, synthetic testing and checkerboards, model assessment, responsible reporting | The procedural spine: what to do before and after the solver runs |
| 09 | [Machine Learning Approaches to Inversion](./09-machine-learning-inversion/README.md) | Learned and iterative inverses, physics-informed networks, generative priors, calibration and out-of-distribution failure | A learned surrogate or prior, measured honestly: it creates no information, and it fails silently outside its training distribution |

## The dependency spine

```text
18-01 Foundations ──┬──> 18-02 Linear ──────┬──> 18-03 Regularisation ──┬──> 18-04 Nonlinear ──┬──> 18-05 Bayesian ──┬──> 18-06 UQ ──> 18-07 Joint
   (well-posedness,  │   (exact solutions,  │    (Tikhonov, sparsity,    │   (Gauss-Newton,    │   (MCMC, priors,   │
    null space,      │    SVD, resolution)  │     parameter choice)      │    global search)   │    posteriors)     ├──> 18-08 Workflow ──┐
    parametrisation) │                     │                            │                     │                    │                      │
                     │                     │                            │                     │                    └──> 18-09 ML ─────────┤
                     │                     │                            │                     │                                           v
                     └─────────────────────┴────────────────────────────┴─────────────────────┴─── all of it feeds applications ──> (05-core-geophysics,
                                                                                                        (07-gravity-geodesy, 09-electrical-em-methods,
                                                                                                         11-exploration-geophysics, 12-global-geophysics,
                                                                                                         14-hydrology-hydrogeophysics, 19-numerical-modeling-hpc)
```

Four rules of thumb follow:

1. **A null space before a method.** No module here starts with an algorithm.
   Every one starts by asking what the data determine and what they leave free;
   the choice of method follows from that answer.
2. **A noise level before a weight.** Every regularisation weight is a statement
   about the data error. If the noise level is not stated first, the weight is a
   choice that cannot be audited.
3. **A truth before a claim.** Synthetic tests with known models are how
   resolution, artifacts and failure modes are measured. Without them, an
   interpretation has no denominator.
4. **An uncertainty before a decision.** A model without an admitted range cannot
   support a decision, because the decision depends on what else was possible.
   Modules 06, 08 and the applied folders in 11 convert the model into a decision
   input; do not use a model downstream before that conversion.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand why inversion is hard | 01 |
| Solve a linear inverse problem and report resolution | 01, 02 |
| Stabilise an unstable solution | 01, 02, 03 |
| Invert a nonlinear forward model | 01–04 |
| Quantify uncertainty in a model | 01, 02, 05 (then 06) |
| Propagate uncertainty into a prediction or decision | 05, 06 |
| Combine two or more data sets | 02, 03, 07 |
| Run and report an inversion project end to end | 01–04, 08 |
| Use a neural network as a surrogate or prior | 01–04, 08, 09 |
| Critically review someone else's inversion | 01, 02, 03, 08 |

## Suggested paths

**If you are new to inverse problems:** read
[18-01-01 Forward vs Inverse Problems and the Practical Asymmetry](./01-inverse-problem-foundations/01-forward-and-inverse.md),
then [18-02-01 Overdetermined Problems and Least Squares](./02-linear-inverse-problems/01-overdetermined.md)
and [18-02-02 Underdetermined Problems and Minimum-Norm Solutions](./02-linear-inverse-problems/02-underdetermined.md),
running the demos. Do not skip module 02 to reach the Bayesian material: the
posterior in module 05 is the same linear algebra with a distribution attached.

**If you come from the physics-side folders:** read
[18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](./01-inverse-problem-foundations/03-null-space.md)
and [18-02-04 SVD Analysis: Model Resolution and Data Importance](./02-linear-inverse-problems/04-svd-analysis-inverse.md)
first, then [18-08-03 Assessing a Model: Resolution, Artifacts, Alternatives](./08-practical-inversion-workflow/03-model-assessment.md).
The unfamiliar content will be the interpretation, not the mathematics.

**If you already run inversions:** read
[18-08-04 Reporting Inversion Results Responsibly](./08-practical-inversion-workflow/04-reporting-inversion.md)
first, then [18-07-05 Pitfalls: Inconsistent Physics, Weighting, Over-Coupling](./07-joint-and-multi-physics-inversion/05-joint-inversion-pitfalls.md).
Both are audits of practice rather than introductions.

**If you are preparing a research project:** read the "assumptions and regime of
validity" section of every lesson in your target module, plus
[18-06-01 Taxonomy of Uncertainty](./06-uncertainty-quantification/01-uncertainty-taxonomy.md),
[18-09-04 Uncertainty in Learned Inversion: Pitfalls and Calibration](./09-machine-learning-inversion/04-uncertainty-in-learned-inversion.md)
and the ★★★ exercises of 07–09. Each is a worked example of stating what a data
set does *not* determine.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **For a one-dimensional inverse problem of your choice, a complete inversion
> report from synthetic data.** Build a forward operator, choose a stated noise
> level, and invert. Then: **(a)** compute the singular-value spectrum and state
> the rank at a stated cut and the dimension of the null space; **(b)** state the
> regularisation and its weight, and justify the weight from the noise level, not
> from the truth; **(c)** report the model with its per-position admitted range
> and its resolution length, and name the positions where the admitted range
> exceeds the claimed structure; **(d)** run one synthetic recovery test and
> report the curve, not the picture; **(e)** for every number in (a)–(d), label it
> **measured**, **modelled** or **chosen**; and **(f)** name the single additional
> observation that would most reduce the largest remaining uncertainty, and state
> the decision it would change.

The point of the checkpoint is the accounting, not the digits: a defensible
inversion is one in which every number carries its label, every model carries its
null space, and every claim carries the observation that would falsify it. A
worked version of (a)–(c) appears in the module 08 exercises; the structure is the
same for any problem.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $\mathbf{m}$ | model vector (the unknowns) | varies |
| $\mathbf{d}$ | data vector (the measurements) | varies |
| $G$, $\mathbf{g}(\mathbf{m})$ | forward operator; forward function | — |
| $\mathbf{d} = G\mathbf{m} + \boldsymbol{\epsilon}$ | linear forward model with noise | — |
| $n$, $p$ | number of model parameters; number of observations | — |
| $C_d$ | data error covariance | $(\text{data unit})^2$ |
| $C_m$, $C_{\text{post}}$ | prior and posterior model covariance | $(\text{model unit})^2$ |
| $R = C\,G^{T}C_d^{-1}G$ | model resolution matrix | dimensionless |
| $\operatorname{diag}R$, $\operatorname{tr}R$ | resolution per parameter; effective parameter count | dimensionless |
| $N$ | null-space matrix ($GN = 0$); dimension $\operatorname{nullity}$ | dimensionless |
| $\lambda$, $\alpha$, $w$ | regularisation or coupling weights | task-dependent |
| $P_0$ | prior or regularisation precision matrix | $(\text{model unit})^{-2}$ |
| $\chi$ | misfit per datum, in units of the stated noise | dimensionless |
| $\sigma$ | standard deviation of a datum or a parameter | data or model unit |
| $\mathrm{MSE}$, $\mathrm{rmse}$ | mean squared error; its square root | $(\text{model unit})^2$, model unit |
| $\mathrm{L2}$ | root-mean-square norm of a function or field | model unit |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md).

## A caution about numbers in this folder

Every model, operator, ensemble, network and uncertainty quoted in this folder is
a **teaching value**. The demonstrations are sized to run in seconds, the noises
and weights are chosen to make a trade-off visible, and the "truths" are
synthetic models constructed for the lesson. **Unless a lesson explicitly says
otherwise, all models and data in this folder are SYNTHETIC.**

Where a lesson gives a number it is either (a) printed by a demonstration in that
lesson's `code/` directory, which you can run, or (b) an exact standard constant
or exact mathematical result (for example
$\mathbb{E}|X|/\sigma = \sqrt{2/\pi}$ for a Gaussian, or the determinant of a
$2\times2$ matrix). No number is presented with the authority of a measurement of
the Earth, a real survey, a real well or a real rock-physics compilation.

The machine-learning modules deserve a second caution. A network's performance is
a statement about its training distribution, and every demonstration there states
that distribution explicitly. Trained on synthetic models, a network has learned
*synthetic* geology, and its out-of-distribution failure — measured, not asserted
— is the lesson's point rather than an inconvenience. The demonstrations' training
is kept deliberately tiny (one hidden layer, a few hundred to a few thousand
steps, under twenty seconds) so that the claims can be checked in the time it
takes to read the lesson, and a claim that cannot be checked in that time is not
made.

Every demonstration is reproducible from the code in its module's `code/`
directory, is print-only (no figures, no `plt.show()`), uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access and exits 0.

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 18-inverse-problems/02-linear-inverse-problems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python svd_analysis_demo.py
```

The demonstrations fall into four kinds, and it is worth knowing which you are
reading. Some **derive and verify a formula** against an independent route (the
normal equations against SVD, a PDE residual against an exact solution, a
spectral ratio against an analytic transfer function). Some **measure a
trade-off** (regularisation weight against misfit and model error, coupling weight
against structural agreement, ensemble spread against realised error). Some
**measure a non-uniqueness** (the equivalence curve of a single datum, the null
space of a rank-deficient operator, the subspace a generative prior forces the
answer into). And some **measure a failure** (out-of-distribution error, coverage
under shift, bias from a mis-specified relation, the frozen-stage residual). If a
demonstration reports a number, that number is either printed by the code you are
running or is a stated standard constant.

The repository-wide quality gate, which checks structure, frontmatter, links and
LaTeX, is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

Inverse problems sit between the mathematical and computational foundations and
every measurement-driven application. It assumes the linear algebra and calculus
of [01-mathematics](../01-mathematics/README.md), the forward physics of
[02-physics](../02-physics/README.md) and the numerical practice of
[03-scientific-computing](../03-scientific-computing/README.md), and it supplies
the interpretation framework that the applied folders use: potential fields
([07-gravity-geodesy](../07-gravity-geodesy/README.md)), magnetics and
electromagnetics ([08-geomagnetism-electromagnetism](../08-geomagnetism-electromagnetism/README.md)),
electrical methods ([09-electrical-em-methods](../09-electrical-em-methods/README.md)),
seismology ([06-seismology](../06-seismology/README.md)) and exploration
([11-exploration-geophysics](../11-exploration-geophysics/README.md)) all state
their results in this folder's language of resolution, null space and admitted
range. It depends on
[21-statistics-bayesian-ml](../21-statistics-bayesian-ml/README.md) for its
probability and machine-learning foundations, hands its numerical heavy lifting to
[19-numerical-modeling-hpc](../19-numerical-modeling-hpc/README.md), and supplies
[25-projects-capstone](../25-projects-capstone/README.md) with the template for a
complete, uncertainty-aware study.

The skill this folder teaches, stated as plainly as possible, is the ability to
say what a measurement does **not** determine — and to report that alongside what
it does.
