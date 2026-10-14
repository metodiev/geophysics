---
id: 18-01-01
title: "Forward vs Inverse Problems and the Practical Asymmetry"
level: advanced
prereqs: ["05-03-01", "01-07-02", "03-02-01"]
tags: [inverse-problems, forward-problems, ill-posedness, conditioning, gravity]
---

# Forward vs Inverse Problems and the Practical Asymmetry

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the forward and inverse problems for a geophysical experiment, and
   **identify** which of the two the physics hands you directly.
2. **Write** the discretised linear model $\mathbf{d} = G\mathbf{m} + \mathbf{e}$
   and **explain** the role of each symbol, including the units of $G$.
3. **Demonstrate numerically** that the forward map attenuates model differences
   while the inverse map amplifies data errors.
4. **Quantify** the amplification with the condition number $\kappa(G)$ and with
   a measured error gain, and **explain** why the gain is constant in the noise
   level for a linear problem.
5. **Compute** the data-error budget required for a stated model accuracy for a
   given survey geometry.
6. **Explain** why difficulty belongs to the experiment (the kernel and the
   sampling), not to the physics, using a scale-invariance argument.
7. **Distinguish** the practical asymmetry of cost and existence from the
   mathematical asymmetry of well-posedness.

## Prerequisites

- [05-03-01 The Forward Problem: From Model to Data](../../05-core-geophysics/03-forward-modelling-principles/01-forward-problem.md) —
  the map from a subsurface model to a predicted measurement.
- [01-07-02 Matrices, Matrix Multiplication and Linear Maps](../../01-mathematics/07-linear-algebra/02-matrices-and-operations.md) —
  matrices as linear maps between vector spaces.
- [03-02-05 Linear Algebra with numpy.linalg](../../03-scientific-computing/02-numpy/05-linear-algebra-numpy.md) —
  building kernels and solving with arrays, which is how every number below was made.

## 1. Two questions, one map

Every quantitative geophysical measurement can be written as a map from a
description of the Earth to a set of numbers a sensor records. Call the
description the **model** $\mathbf{m}$ and the numbers the **data** $\mathbf{d}$.
The map is the **forward operator**:

$$\mathbf{d} = F(\mathbf{m}).$$

Two questions can be asked of this single object, and they are not symmetric:

- the **forward problem**: given $\mathbf{m}$, compute $\mathbf{d}$;
- the **inverse problem**: given $\mathbf{d}$, find the $\mathbf{m}$ that
  produced it.

The forward problem is what a physical theory gives you. Gravity, elasticity,
electromagnetism and heat conduction are all stated as forward relations. The
inverse problem is what an interpreter actually wants: a picture of the
subsurface. The practical asymmetry is that the forward problem is usually easy
and stable, while the inverse problem is usually hard and unstable — and nothing
in the forward calculation warns you of this.

This module is about that asymmetry. Later modules in folder 18 deal with
regularisation, nonlinear optimisation, Bayesian inference and uncertainty
quantification; this lesson fixes the vocabulary and measures the phenomenon.

All models and data in this module are **SYNTHETIC**.

## 2. The linear model and its notation

Most of this module works with a **linear**, **discretised** forward operator:

$$\boxed{\;\mathbf{d} = G\,\mathbf{m} + \mathbf{e},\qquad
\mathbf{d}\in\mathbb{R}^{N},\quad \mathbf{m}\in\mathbb{R}^{M},\quad
G\in\mathbb{R}^{N\times M}.}$$

- $M$ is the number of **model parameters**; they are discrete by construction.
  A continuous Earth is a limit we never actually compute with
  (see [18-01-04](04-discretisation-reality.md)).
- $N$ is the number of **data**; it is also discrete.
- $\mathbf{e}$ is the data error, including measurement noise, theory error and
  the representation error of the discretisation.
- $G$ carries the physics. Its entries are **sensitivity coefficients**
  $\partial d_i/\partial m_j$, so each entry has the units of
  (data unit) per (model unit). Getting those units right is the single most
  effective check on a forward code.

For the demonstration in this lesson, the model is a set of point masses and the
data are surface gravity readings. The kernel is exact textbook physics: the
vertical gravity of a point mass $M$ at horizontal offset $x$ and depth $z$ is

$$g_z(x,z) = \frac{G_N M z}{(x^{2}+z^{2})^{3/2}},$$

with the gravitational constant
$G_N = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ (2018 CODATA) and
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ exactly, by definition. The
kernel entry is therefore

$$G_{ik} = \frac{G_N z_k}{\left(x_i^{2}+z_k^{2}\right)^{3/2}}
\quad \left[\frac{\mathrm{mGal}}{\mathrm{kg}}\right],$$

and $G$ is linear in the masses by superposition, which is exact for point
masses.

## 3. The forward direction is stable, and silent about the inverse

The demonstration `code/forward_and_inverse_demo.py` uses four masses

$$\mathbf{m} = (1.0,\;1.4,\;0.8,\;1.2)\times10^{10}\ \mathrm{kg}$$

at depths $1,2,3,4\ \mathrm{km}$, recorded at 25 stations from $-12$ to
$+12\ \mathrm{km}$. The forward data span

$$3.8\times10^{-4}\ \mathrm{mGal}
\;\le\; d_i \;\le\; 0.10104\ \mathrm{mGal},
\qquad \max_i|d_i| = 0.10104\ \mathrm{mGal}.$$

Now perturb the model by $1\%$ in norm:

$$\frac{\lVert\delta\mathbf{m}\rVert}{\lVert\mathbf{m}\rVert} = 0.010000,
\qquad
\frac{\lVert\delta\mathbf{d}\rVert}{\lVert\mathbf{d}\rVert} = 0.001904,$$

so the **forward gain** is $0.001904/0.010000 = 0.1904$. The forward map does not
merely fail to magnify model differences: it *attenuates* them by a factor of
five. If you only ever ran the forward calculation, you would conclude that
gravity is a well-behaved and forgiving measurement.

The reason is visible in the column norms of $G$, which measure how strongly a
unit mass at each depth moves the whole data set:

| depth (km) | $\lVert G_{\cdot k}\rVert$ (mGal/kg) | anomaly of $10^{10}$ kg (mGal) |
|---|---|---|
| 1.0 | $7.5174\times10^{-12}$ | 0.07517 |
| 2.0 | $2.5618\times10^{-12}$ | 0.02562 |
| 3.0 | $1.3940\times10^{-12}$ | 0.01394 |
| 4.0 | $9.0512\times10^{-13}$ | 0.00905 |

Sensitivity falls by a factor $8.3$ between 1 km and 4 km, and the *shape* of the
anomaly barely changes: the correlation between adjacent columns is $0.913789$
between the 1 km and 2 km masses, $0.974901$ between 2 km and 3 km, and
$0.987897$ between 3 km and 4 km. Two masses one kilometre apart in depth produce
nearly the same surface anomaly. The forward map therefore *compresses* the
model space: distinct models become nearly indistinguishable data.

## 4. The inverse direction amplifies

Compression in one direction is expansion in the other. The singular values of
the kernel are

$$\sigma = (8.0002\times10^{-12},\;1.3355\times10^{-12},\;
2.2256\times10^{-13},\;2.2035\times10^{-14})\ \mathrm{mGal\,kg^{-1}},$$

so

$$\kappa(G) = \frac{\sigma_{\max}}{\sigma_{\min}} = 3.6307\times10^{2}.$$

The smallest singular vector is

$$\mathbf{v}_{\min} = (0.015,\;-0.243,\;0.758,\;-0.605),$$

a pattern that adds mass to the 3 km and 4 km levels and removes it from the
2 km level. That combination changes the surface gravity least of all four
directions a unit-length model can take.

The demonstration then recovers the masses from noisy data, 200 noise
realisations per row, with noise drawn as white noise whose rms is a stated
fraction of the peak anomaly:

| noise rms (% of peak $\lvert d\rvert$) | mean model error | 90th percentile | gain |
|---|---|---|---|
| 0.01 | 1.80% | 3.53% | 179.6 |
| 0.03 | 4.84% | 9.11% | 161.2 |
| 0.10 | 16.67% | 32.26% | 166.7 |
| 0.30 | 49.63% | 92.84% | 165.4 |
| 1.00 | 169.55% | 351.37% | 169.5 |

Read the table twice. First, a **$0.1\%$ data error produces a $16.7\%$ model
error**: the inverse map multiplies by about $167$. Second, the **gain is
constant** across two orders of magnitude of noise. That is the signature of a
linear problem: the error transfer is exactly proportional, and the constant of
proportionality is a property of the operator and the design, not of the noise.

If you want the model to $10\%$, you must therefore deliver data to
$10/166.5 = 0.060\%$ of the peak anomaly, that is
$6.070\times10^{-5}\ \mathrm{mGal}$ rms. That number was computed in the
demonstration; it is a measurement requirement imposed by the geometry, and it
appears nowhere in a forward calculation.

## 5. Fully worked example: the budget arithmetic

Take the numbers above and redo them by hand.

*(a) Data.* The rms noise at $0.1\%$ of the peak anomaly is
$0.001\times0.10104 = 1.0104\times10^{-4}\ \mathrm{mGal}$.

*(b) Model error.* The measured gain is $166.5$, so the expected model error is

$$\frac{\lVert\delta\mathbf{m}\rVert}{\lVert\mathbf{m}\rVert}
\;\approx\; 166.5\times\frac{1.0104\times10^{-4}}{0.10104}
\;=\;166.5\times10^{-3} = 0.1665,$$

i.e. $16.7\%$, which is the number in the table. The apparent cancellation of
$0.10104$ is not a coincidence: the gain was *defined* with the noise expressed
as a fraction of the peak, so the budget has the same form.

*(c) Invert the budget.* For a $10\%$ model error,

$$\text{noise fraction} = \frac{0.10}{166.5} = 6.0\times10^{-4} = 0.060\%,
\qquad
\text{noise rms} = 6.0\times10^{-4}\times0.10104
= 6.07\times10^{-5}\ \mathrm{mGal}.$$

*(d) Sanity check against the singular values.* The bound implied by the SVD is

$$\frac{\lVert\delta\mathbf{m}\rVert}{\lVert\mathbf{m}\rVert}
\le \kappa(G)\,\frac{\lVert\delta\mathbf{d}\rVert}{\lVert\mathbf{d}\rVert}
= 363\times10^{-3} = 0.363,$$

i.e. $36\%$ worst case. The measured mean of $16.7\%$ is inside that bound by
roughly a factor of two, as expected for noise spread over all singular
directions rather than concentrated in the worst one. Use $\kappa(G)$ to state a
worst case, and a measured gain to state an expectation. Both are honest; mixing
them up is not.

## 6. Why the asymmetry is *practical* as well as mathematical

Four differences matter in daily work, and only the first is a statement about
mathematics.

1. **A guarantee.** The forward problem always has a solution: evaluate $F$. The
   inverse problem may have none (no model reproduces the data), many (the data
   do not constrain every model parameter), or a unique solution that is
   destroyed by noise. Lesson [18-01-02](02-hadamard-well-posedness.md) tests
   each failure mode numerically.
2. **Cost.** One forward evaluation is one matrix-vector product, $O(NM)$ work.
   Solving the inverse problem the direct way requires factorising $G$, roughly
   $O(NM^{2}+M^{3})$ work — in this example $MN = 100$ versus a few thousand
   floating-point operations, which sounds trivial, but the same ratio becomes
   decisive in three dimensions.
3. **Nonlinearity does not rescue the inverse.** A nonlinear forward problem is
   still evaluated in one pass per model, while its inverse needs an iterative
   sequence of linearised inverses
   ([18-04-01](../04-nonlinear-inversion/01-local-linearization.md)), each of
   which inherits the amplification above.
4. **The asymmetry is invisible in the forward direction.** The forward map of a
   *perfectly behaved* physical law is smooth, bounded and cheap; the difficulty
   appears only when you look at its inverse.

## 7. Difficulty is a property of the experiment

The same physics can be easy or hard depending on how — and where — you sample
the model. The gravitational kernel depends on $x$ and $z$ only through the
ratio $x/z$. Halve every depth and halve the station spread and the kernel is
unchanged entry by entry, so the demonstration measures the *identical*
condition number:

$$\kappa(G_{\text{halved}}) = 3.6307\times10^{2}
= \kappa(G_{\text{original}}).$$

That is a scale-invariance of the gravity problem: shallow and deep surveys are
governed by the same number, namely the ratio of survey spread to target depth.

Move the same four masses to depths $5,10,15,20\ \mathrm{km}$ while keeping the
$\pm12\ \mathrm{km}$ spread and the picture changes:

$$\kappa(G_{\text{deep}}) = 1.9838\times10^{3},
\qquad \text{measured gain} = 417.6 .$$

Identical masses, identical stations, identical physics — and a $2.6$ times worse
error amplification. Resolution and depth trade off against each other
([05-01-03](../../05-core-geophysics/01-what-geophysics-measures/03-resolution-depth-tradeoff.md)),
and the condition number is one honest way to make that trade-off quantitative
before any field work is done.

## 8. Assumptions and regime of validity

Every number above rests on statements you must be prepared to defend.

- **Exact kernel.** The forward operator is the closed-form point-mass formula.
  Real surveys add terrain, regional fields, instrument drift and unknown
  density–depth coupling, none of which is modelled here.
- **Linear in the parameters.** True for masses, false for the geometry of a
  body. Depth and shape enter nonlinearly
  ([05-03-02](../../05-core-geophysics/03-forward-modelling-principles/02-analytical-solutions.md)).
- **Known, fixed parameterisation.** The four depths are chosen, not estimated.
  Lesson [18-01-04](04-discretisation-reality.md) shows what changes when they
  are not.
- **White, zero-mean noise.** The gain table uses independent Gaussian errors.
  Correlated errors behave differently and are treated in
  [18-02-06](../02-linear-inverse-problems/06-weighting-and-covariance.md).
- **Least squares as the estimator.** The recovery used the least-squares
  solution. Had the norm of the model been penalised instead, the numbers would
  change; that choice is the subject of module
  [18-03](../03-regularization/README.md).
- **A single noise metric.** All percentages are relative to the *peak* anomaly.
  Relative to $\lVert\mathbf{d}\rVert$ the numbers differ by a factor
  $\lVert\mathbf{d}\rVert/(\sqrt{N}\max|d_i|)$, so always state the metric.

## 9. Running the demonstration

The demonstration for this lesson is [`code/forward_and_inverse_demo.py`](code/forward_and_inverse_demo.py) — print-only, no network access, fixed seed
`np.random.default_rng(20261014)`.

```bash
cd 18-inverse-problems/01-inverse-problem-foundations/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python forward_and_inverse_demo.py
```

The script prints each of the tables quoted above, with units, using a fixed seed
(`np.random.default_rng(20261014)`). It takes well under a second and needs no
network. Companion exercises with worked solutions are in
[`exercises/01-forward-and-inverse-exercises.md`](exercises/01-forward-and-inverse-exercises.md).

## Mastery checkpoint

Without notes:

> A gravity survey has $\kappa(G) = 3.63\times10^{2}$ and a measured error gain
> of $167$ for a four-parameter model. **(a)** State the worst-case model error
> for a $0.2\%$ data error and the expected mean model error, and explain why
> they differ. **(b)** The target is a $5\%$ model error: what data precision is
> required, in percent of the peak anomaly? **(c)** A colleague doubles all
> depths and all station offsets, then reports that the conditioning got worse.
> Is that right? **(d)** Give one reason why a nonlinear forward problem does
> not remove the difficulty.

A worked version of (a)–(c) is in
[`exercises/01-forward-and-inverse-solutions.md`](exercises/01-forward-and-inverse-solutions.md).

## Common pitfalls

1. **Judging the inverse by the forward.** A smooth, cheap, always-defined
   forward map tells you nothing about the stability of its inverse.
2. **Quoting a model error without a noise metric.** Percent of peak anomaly,
   percent of $\lVert\mathbf{d}\rVert$ and absolute mGal are different numbers.
3. **Confusing the bound with the expectation.** $\kappa(G)$ gives a worst case;
   the measured gain gives a mean. State which one you are using.
4. **Assuming more stations always help.** It is the *design* — spread relative
   to depth — that controls the condition number, as the scale-invariance check
   shows.
5. **Treating amplification as a bug.** It is a property of the experiment and
   can be predicted before acquisition.

## Related modules

- [18-01-02 Hadamard's Conditions](02-hadamard-well-posedness.md) — the three
  failure modes of the inverse problem, tested one by one.
- [18-01-03 Null Space and Non-Uniqueness](03-null-space.md) — where the missing
  model directions come from.
- [18-02-01 Overdetermined Problems and Least Squares](../02-linear-inverse-problems/01-overdetermined.md) —
  the estimator used in this lesson, derived properly.
- [05-03-01 The Forward Problem](../../05-core-geophysics/03-forward-modelling-principles/01-forward-problem.md) —
  the same map from the modelling side.
- [05-01-04 Non-Uniqueness of Geophysical Models](../../05-core-geophysics/01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md) —
  the qualitative statement this module makes quantitative.
