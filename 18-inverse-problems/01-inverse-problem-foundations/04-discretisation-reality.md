---
id: 18-01-04
title: "Discretisation, Parameterisation and Model Choice"
level: doctoral
prereqs: ["18-01-03", "18-01-02", "05-03-04"]
tags: [inverse-problems, discretisation, parameterisation, model-choice, regularisation, gravity]
---

# Discretisation, Parameterisation and Model Choice

## Learning objectives

By the end of this lesson you will be able to:

1. **Separate** three distinct errors — measurement error, representation
   (discretisation) error and the choice of estimator — and **assign** each to a
   stage of the workflow.
2. **Measure** the convergence order of a block-averaged parameterisation and
   **explain** why a smooth Earth represented by blocks converges as $h^{2}$.
3. **Demonstrate** that the same data support several parameterisations whose
   reported physical values differ, and **quantify** the difference.
4. **Compute** the effective rank of a finely parameterised operator at a declared
   tolerance, and **predict** the failure of the untruncated pseudo-inverse.
5. **Construct** the equivalence class at fixed parameterisation by sampling the
   null space, and **report** the spread of a physically meaningful quantity.
6. **Justify** regularisation as a model choice rather than a preprocessing step,
   and **report** the damping with the misfit it produced.
7. **Decide** whether a basis can represent a given Earth at all, using the
   representation error of an exactly representable test model.

## Prerequisites

- [18-01-03 Null Space and Non-Uniqueness](03-null-space.md) — equivalence classes
  and the tolerance dependence of rank.
- [18-01-02 Hadamard's Conditions](02-hadamard-well-posedness.md) — existence,
  uniqueness and the rank table.
- [05-03-04 Numerical Forward Modelling and Discretisation](../../05-core-geophysics/03-forward-modelling-principles/04-numerical-forward-modelling.md) —
  how a forward code turns a continuum model into numbers.

## 1. Three errors that are usually conflated

An inversion result is the product of three separate approximations:

| error | where it enters | how to reduce it |
|---|---|---|
| measurement / theory error | the data vector $\mathbf{d}$ | better instruments, better physics |
| **representation error** | the parameterisation of the model | a more appropriate basis |
| **estimator bias** | the estimator you chose | report it; regularise knowingly |

Textbook treatments discuss the first; this lesson is about the second and third,
which are the ones an interpreter controls and usually does not report. The key
claim, demonstrated below, is that **the model you choose and the basis you frame
it in set an error floor that no amount of data can remove**, and that when the
parameterisation is finer than the data can constrain, the estimator's selection
rule decides the answer.

Throughout, the physical setting is a horizontally layered Earth observed by
gravity: the surface reading plus borehole readings at depth. The slab formula of
[18-01-02](02-hadamard-well-posedness.md) is exact, so all inaccuracy discussed
here is representation or estimator inaccuracy, not physics error.

All models and data in this module are **SYNTHETIC**. The "true" profile is a
chosen teaching function,

$$\rho(z) = 2700 + 30\,z + 120\exp\!\left[-\left(\frac{z-6}{1.2}\right)^{2}\right]
\quad \mathrm{kg\,m^{-3}},\qquad z\in[0,10]\ \mathrm{km},$$

and the sensors sit at depths $0,1,2,4,6,8,10\ \mathrm{km}$: seven readings. All
models, data and noise are synthetic.

## 2. Representation error has a measurable order

Suppose the model space is $M$ equal blocks and each block carries the true
*average* density over its interval — the best any block model can do. Predict the
data with the block kernel and compare with data computed from a fine reference
quadrature:

$$e(M) = \frac{\lVert G_M\mathbf{m}_M - \mathbf{d}_{\text{ref}}\rVert}
{\lVert\mathbf{d}_{\text{ref}}\rVert}.$$

| $M$ | block size (km) | $e(M)$ |
|---|---|---|
| 2 | 5.0000 | $5.550\times10^{-3}$ |
| 4 | 2.5000 | $1.887\times10^{-3}$ |
| 8 | 1.2500 | $5.041\times10^{-4}$ |
| 16 | 0.6250 | $1.302\times10^{-4}$ |
| 32 | 0.3125 | $2.224\times10^{-5}$ |
| 64 | 0.1562 | $7.506\times10^{-6}$ |

Halving the block size reduces the error by about four, and a least-squares fit of
$\log e$ against $\log h$ over the last five refinements gives a **measured order
of $2.045$**. The reason is elementary: block-averaging a smooth function is a
midpoint-type quadrature, whose error is $O(h^{2})$. Two consequences follow
immediately, and both are quantitative:

- the error is real — $0.55\%$ at $5\ \mathrm{km}$ blocks for this profile;
- it is controllable, and the block size needed for a target accuracy can be
  computed rather than guessed. To reach $0.1\%$ you need to halve the block size
  roughly $(5.55/1)^{1/2}\approx2.4$ times from the first row, i.e. blocks near
  $2\ \mathrm{km}$.

## 3. The same data, five parameterisations

Now fix the data once — the seven exact readings plus white noise of rms
$2.5499\ \mathrm{mGal}$, which is $0.211\%$ of the peak reading — and fit five
parameterisations with the min-norm rule:

| $M$ | data misfit | model error | $\rho$ at $z=5\ \mathrm{km}$ | $\lVert\mathbf{m}\rVert$ |
|---|---|---|---|---|
| 3 | 0.2241% | 0.9999% | 2946.4 | 4977.5 |
| 4 | 0.3218% | 0.6334% | 2913.8 | 5747.9 |
| 5 | 0.1676% | 0.8773% | 2960.4 | 6428.6 |
| 7 | 0.0434% | 1.6433% | 3017.9 | 7604.2 |
| 20 | 0.0434% | 1.3618% | 2960.4 | 12849.4 |

The truth at $5\ \mathrm{km}$ is $2909.9\ \mathrm{kg\,m^{-3}}$. Read the table as
three separate facts.

1. **Misfit saturates.** From $M = 7$ onwards the misfit sits at $0.0434\%$ and no
   longer falls. The reason is structural, not numerical: although there are seven
   readings, they carry only **six independent numbers**. The sensor at
   $10\ \mathrm{km}$ sits at the bottom of the layer stack and sees the whole stack
   from below, so its reading is the exact negative of the surface reading:
   $\pm1205.87553\ \mathrm{mGal}$. The numerical rank of the $7\times2000$
   reference kernel is $6$, not $7$. A redundant measurement is invisible in a
   station table and obvious in a singular-value spectrum.
2. **Misfit is not monotone** either ($0.3218\%$ at $M=4$, $0.1676\%$ at $M=5$):
   with min-norm selection, a coarser model can miss the noise direction that a
   finer one fits.
3. **Model error is worst in the middle.** The $7$-parameter model fits the data
   best and sits *furthest* from the truth ($1.6433\%$) among the first four
   rows, because the extra freedom is spent on null-space structure chosen by the
   norm, not by physics. The reported value at $5\ \mathrm{km}$ moves by
   $104\ \mathrm{kg\,m^{-3}}$ between $M=4$ and $M=7$ and by about
   $100\ \mathrm{kg\,m^{-3}}$ overall — a $3.5\%$ change in a quantity an
   interpreter would quote as a number.

So the choice of $M$ is a *modelling* decision with a measurable effect on the
answer. There is no $M$ that is "just resolution".

## 4. Beyond the data: effective rank and the failure of the plain inverse

Push the parameterisation to $M = 100$ blocks and the operator becomes
$7\times100$. The singular values of the square-ish part are

$$\sigma_1 = 8.136166\times10^{-2},\qquad
\sigma_7 = 3.949768\times10^{-17},\qquad
\frac{\sigma_7}{\sigma_1} = 4.855\times10^{-16}.$$

This is where the tolerance discussion of
[18-01-02 §6](02-hadamard-well-posedness.md) becomes practical. The matrix is
**full rank on paper** ($7$ singular values, all non-zero) and **rank $6$ in
fact** at a relative tolerance of $10^{-10}$, because $\sigma_7/\sigma_1$ is at
double precision. The effective null space has $94$ dimensions: $93$ exactly null
directions plus the numerically empty seventh.

What happens if you ignore this? The demonstration divides by all seven singular
values and reports

$$\lVert\mathbf{m}\rVert = 2.469\times10^{16}\ \mathrm{kg\,m^{-3}},
\qquad \rho(5\ \mathrm{km}) = -7.357\times10^{12}\ \mathrm{kg\,m^{-3}},$$

numbers with no physical meaning whatsoever. One singular value at machine
precision has multiplied the noise by $\sim10^{15}$. With the tolerance enforced,
`np.linalg.pinv` — whose default `rcond` is
$\max(M,N)\varepsilon = 2.2\times10^{-14}$ — returns

$$\lVert\mathbf{m}\rVert = 28732.1\ \mathrm{kg\,m^{-3}},
\qquad \rho(5\ \mathrm{km}) = 2960.4\ \mathrm{kg\,m^{-3}},$$

and the misfit is the same $0.0434\%$ as the untruncated answer *appeared* to
achieve. The tolerance is not a numerical detail; it is the boundary of the
question you are answering.

## 5. The equivalence class at fixed parameterisation

Truncating at rank $6$ leaves a $93$-dimensional null space. Sample $300$ models
of the form $\mathbf{m}_0 + Z\mathbf{w}$ with $\lVert\mathbf{w}\rVert = 5\%$ of
$\lVert\mathbf{m}_0\rVert$, and measure three things:

| quantity | value |
|---|---|
| min-norm fit | $0.0434\%$ of $\lVert\mathbf{d}\rVert$ |
| worst fit over the 300 samples | $0.0434\%$ |
| $\lVert\mathbf{m}\rVert$ for every sample | $28768.0\ \mathrm{kg\,m^{-3}}$ |
| $\rho(5\ \mathrm{km})$ across the sample | $[2620.4,\ 3200.8]\ \mathrm{kg\,m^{-3}}$ |
| spread of $\rho(5\ \mathrm{km})$ | $580.5\ \mathrm{kg\,m^{-3}}$ |

Three hundred models, the *same* fit, the *same* model norm — because the
perturbations are orthogonal to $\mathbf{m}_0$ and of fixed length — and a
$580\ \mathrm{kg\,m^{-3}}$ spread in the density at $5\ \mathrm{km}$, which is
$20\%$ of the true value $2909.9$. This is the concrete form of the statement
"the data do not determine the vertical density distribution": not an assertion,
but a measured spread over an explicitly constructed family.

## 6. Regularisation is a model choice

Apply Tikhonov damping, which replaces the filter factors $1/\sigma_i$ by
$\sigma_i/(\sigma_i^{2}+\alpha^{2})$, and sweep $\alpha$:

| $\alpha$ | data misfit | model error | $\rho$ at $5\ \mathrm{km}$ | roughness |
|---|---|---|---|---|
| $0$ (truncated min-norm) | 0.0434% | 1.5037% | 2960.4 | 33.29 |
| $10^{-4}$ | 0.0434% | 1.5038% | 2960.4 | 33.29 |
| $10^{-3}$ | 0.0483% | 1.5169% | 2960.3 | 33.47 |
| $10^{-2}$ | 1.9486% | 4.9405% | 2947.2 | 63.09 |
| $3\times10^{-2}$ | 13.1057% | 20.6076% | 2785.9 | 151.25 |
| $10^{-1}$ | 60.6370% | 63.7827% | 1334.7 | 100.06 |

The reported density at $5\ \mathrm{km}$ moves from $2960.4$ to
$2785.9\ \mathrm{kg\,m^{-3}}$ between $\alpha = 0$ and $\alpha = 3\times10^{-2}$
— a change of $175\ \mathrm{kg\,m^{-3}}$ — and by $\alpha = 10^{-1}$ the model is
over-smoothed and has drifted to $1334.7$. A workflow that records only "the
inversion result" has recorded one point on this curve without saying which.
Report $\alpha$ and the misfit it produced; module
[18-03](../03-regularization/README.md) develops the trade-off properly, and
[18-08-04](../08-practical-inversion-workflow/04-reporting-inversion.md) covers
reporting.

## 7. A basis is a physical assumption

Representation error depends on the *basis*, not only on the number of
parameters. Take a truth that is exactly linear,
$\rho_{\text{lin}}(z) = 2700+30z\ \mathrm{kg\,m^{-3}}$, and compare two bases with
the same node spacing:

| $M$ (blocks or intervals) | block-basis data error | linear-basis data error |
|---|---|---|
| 4 | $1.675\times10^{-3}$ | $2.746\times10^{-16}$ |
| 8 | $3.876\times10^{-4}$ | $7.661\times10^{-16}$ |
| 16 | $1.047\times10^{-4}$ | $4.675\times10^{-16}$ |
| 32 | $2.423\times10^{-5}$ | $1.209\times10^{-15}$ |

The block basis has an $O(h^{2})$ error even though the truth is a straight line;
the linear basis represents it *exactly*, to machine precision, at every
resolution. Parameterising in blocks asserts that the Earth is piecewise uniform,
and that assertion produces a bias which converges away only as $h^{2}$. Rules of
thumb:

- if a basis can represent the truth, use it — the representation error is then
  zero and the parameterisation costs nothing;
- if it cannot, you have *chosen* an error floor; state it;
- comparing a block model to a smooth Earth (as in §3) mixes representation error
  with estimator bias, which is why §3 reports both misfit and model error.

## 8. Fully worked example: the tolerance arithmetic of §4

*(a) Relative singular value.* $\sigma_7/\sigma_1 = 3.949768\times10^{-17} /
8.136166\times10^{-2} = 4.855\times10^{-16}$. Since double precision carries
$\varepsilon = 2.220\times10^{-16}$, this direction is one unit in the last place
above zero: it carries no information.

*(b) Amplification.* Dividing the data by $\sigma_7$ multiplies any error in the
corresponding data direction by $1/3.949768\times10^{-17} = 2.532\times10^{16}$.
A data error of $10^{-3}\ \mathrm{mGal}$ in that direction would become a model
error of $2.5\times10^{13}\ \mathrm{kg\,m^{-3}}$, which is what the reported
$-7.357\times10^{12}$ reflects.

*(c) The truncated answer.* Keeping six directions, $\lVert\mathbf{m}\rVert$
drops from $2.469\times10^{16}$ to $2.873\times10^{4}$ — a factor
$8.6\times10^{11}$ — with the misfit unchanged at $0.0434\%$ of
$\lVert\mathbf{d}\rVert$. **The data cannot tell the difference between the
meaningless answer and the usable one.** Only the tolerance can.

## 9. Assumptions and regime of validity

- **A layered (1-D) model.** The slab kernel is exact for horizontal layering.
  Three-dimensional structure changes the kernel and the resolution, not the
  logic.
- **Tikhonov damping as the estimator family.** The trade-off table is specific to
  $L_{2}$ damping; an $L_{1}$ or total-variation choice gives different numbers
  ([18-03-04](../03-regularization/04-sparsity.md)).
- **White Gaussian noise at $0.211\%$ of peak.** The specific misfit values are
  noise-realisation-dependent; the *structure* of the tables is not.
- **Fixed sensor depths.** Depths are presumed exact. Depth uncertainty is a
  nonlinear problem ([18-04-01](../04-nonlinear-inversion/01-local-linearization.md)).
- **A single noise realisation in §3 and §6.** The tables are one realisation each,
  so column-to-column differences of a few per cent are not significant; the
  orders of magnitude are.
- **Refinement of one parameterisation family.** The $h^{2}$ result is for
  block-averaging; a different rule (e.g. endpoint sampling) would have a
  different order.

## 10. Running the demonstration

The demonstration for this lesson is [`code/discretisation_reality_demo.py`](code/discretisation_reality_demo.py) — print-only, no network access, fixed seed
`np.random.default_rng(20261014)`.

```bash
cd 18-inverse-problems/01-inverse-problem-foundations/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python discretisation_reality_demo.py
```

The script prints all seven tables with units, uses
`np.random.default_rng(20261014)`, and finishes in well under a second. Companion
problems are in
[`exercises/04-discretisation-reality-exercises.md`](exercises/04-discretisation-reality-exercises.md).

## Mastery checkpoint

Without notes:

> A layered gravity experiment has seven readings and a $100$-block
> parameterisation. **(a)** The numerical rank is $6$: give two independent
> reasons why seven readings do not give seven constraints. **(b)** Explain what
> happens to the min-norm solution if you divide by all seven singular values, and
> how you would detect it without looking at the model. **(c)** You must report
> $\rho$ at $5\ \mathrm{km}$ with an honest uncertainty. Describe the three
> numbers you must quote. **(d)** A reviewer asks why your blocks are $2\ \mathrm{km}$
> thick. Answer with a representation-error argument.

Worked solutions are in
[`exercises/04-discretisation-reality-solutions.md`](exercises/04-discretisation-reality-solutions.md).

## Common pitfalls

1. **Treating $M$ as a knob rather than an assumption.** It changes the reported
   answer by per-cent amounts in this example.
2. **Reporting a misfit without reporting the independent-data count.** Redundant
   readings make a misfit floor look like a model success.
3. **Using an untruncated pseudo-inverse.** A single machine-precision singular
   value destroys the solution.
4. **Quoting a physical value from an underdetermined inversion as if it were
   determined.** Show the spread over the equivalence class instead.
5. **Hiding the damping parameter.** $\alpha$ is a modelling choice; the answer
   depends on it measurably.
6. **Assuming a finer grid resolves more.** It resolves more *of the estimator's
   preference*, not more of the Earth.

## Related modules

- [18-01-03 Null Space and Non-Uniqueness](03-null-space.md) — equivalence classes
  and resolved combinations.
- [18-01-05 Model Space and Data Space](05-model-space-data-space.md) — projection
  language for the same facts.
- [18-03-02 Tikhonov Regularisation](../03-regularization/02-tikhonov.md) — the
  trade-off of §6 developed fully.
- [19-07-02 Solution Verification and Discretisation Error](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/02-solution-verification.md) —
  the same measured-order discipline applied to forward solvers.
- [05-03-04 Numerical Forward Modelling and Discretisation](../../05-core-geophysics/03-forward-modelling-principles/04-numerical-forward-modelling.md) —
  discretisation from the modelling side.
