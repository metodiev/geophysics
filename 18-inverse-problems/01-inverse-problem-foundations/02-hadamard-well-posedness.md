---
id: 18-01-02
title: "Hadamard's Conditions: Existence, Uniqueness, Stability"
level: graduate
prereqs: ["18-01-01", "01-16-05", "01-16-03"]
tags: [inverse-problems, hadamard, well-posedness, ill-posedness, stability, uniqueness]
---

# Hadamard's Conditions: Existence, Uniqueness, Stability

## Learning objectives

By the end of this lesson you will be able to:

1. **State** Hadamard's three conditions for a well-posed problem and
   **distinguish** which of them fails in a given geophysical setting.
2. **Test existence numerically** by measuring the least-squares misfit against
   the noise level, and **decide** whether a misfit floor is a model failure or
   a noise realisation.
3. **Construct** an exactly non-unique layered gravity problem, derive its
   $11$-dimensional null space, and **verify** that two different models produce
   bit-identical data.
4. **Repair** non-uniqueness by adding independent measurements, and **count**
   how many are needed.
5. **Explain** why a discretised version of an ill-posed problem always has a
   bounded inverse, and **demonstrate** the growth of $\kappa(G)$ under
   refinement.
6. **Reproduce** Hadamard's differentiation example and **identify** the
   $h^{-1}$ noise amplification as the stability failure.
7. **State** a declared tolerance whenever you report a numerical rank, and
   explain what the tolerance means for the model.

## Prerequisites

- [18-01-01 Forward vs Inverse Problems](01-forward-and-inverse.md) — the map,
  the notation and the measured error amplification.
- [01-16-05 Ill-Posedness in the Sense of Hadamard](../../01-mathematics/16-functional-analysis/05-ill-posedness.md) —
  the mathematical statement in function spaces.
- [01-16-03 Linear Operators, Adjoints and Compactness](../../01-mathematics/16-functional-analysis/03-operators.md) —
  why compact operators have unbounded inverses.

## 1. The definition, and why it is a checklist

Hadamard called a problem **well posed** when, for every admissible data set,

1. **Existence** — a solution exists;
2. **Uniqueness** — the solution is unique;
3. **Stability** — the solution depends continuously on the data.

If any fails, the problem is **ill posed**. The definition is a checklist, and
the value of a checklist is that you can test items one at a time. This lesson
does exactly that, using a single physical model — the gravity of a horizontally
layered Earth — so that the failures cannot be attributed to "different physics".

The physical facts used, both exact:

- a set of point masses superposes: $\mathbf{d} = G\mathbf{m}$ with the kernel of
  [18-01-01](01-forward-and-inverse.md);
- an infinite horizontal **slab** of density $\rho$ and thickness $h$ produces,
  at a point outside it,
  $g = \pm 2\pi G_N \rho h$, with the sign positive when the slab lies below the
  sensor. The constant $2\pi G_N = 4.194\times10^{-5}\ \mathrm{mGal}$ per
  $(\mathrm{kg\,m^{-3}})$ per metre, equivalently the familiar
  $0.0419\ \mathrm{mGal\,m^{-1}}$ per $\mathrm{g\,cm^{-3}}$.

All models and data in this module are **SYNTHETIC**.

## 2. Existence: data outside the range of the operator

**Existence** fails when the observed data have structure that no model in your
parameterisation can reproduce. The demonstration makes this concrete: the true
source is two masses at depths $8$ and $12\ \mathrm{km}$, while the model space
consists of three masses at $1$, $2$ and $3\ \mathrm{km}$. Twenty-one stations
span $\pm10\ \mathrm{km}$ and the data carry white noise with rms $0.113\%$ of
the peak anomaly.

Measured:

$$\lVert\mathbf{d}_{\text{obs}}\rVert = 5.106535\times10^{-3}\ \mathrm{mGal},
\qquad
\text{best misfit} = 1.537876\times10^{-3}\ \mathrm{mGal},$$

so the relative misfit is $30.116\%$ — and, against the noise,

$$\frac{\lVert\mathbf{d}_{\text{obs}}-G\mathbf{m}_{\text{LS}}\rVert}
{\lVert\mathbf{e}\rVert} = 182.3 .$$

A misfit $182$ times the noise is not a noise realisation. No model in this
parameterisation fits these data, so **the inverse problem has no solution** in
the strict sense: the observed vector is not in $\operatorname{range}(G)$.

Two lessons about the diagnostic:

- the true test is a **comparison**, misfit against the stated noise level, not
  an absolute threshold. A misfit is "large" only relative to the error you claim
  the data have;
- existence failures are *parameterisation* failures. Here they are informative:
  the data are telling you that a shallow-only model is inadequate, which is a
  physical conclusion worth having.

The constructive remedy is to enlarge the model space — and, as the next section
shows, that immediately creates the opposite problem.

## 3. Uniqueness: an exact null space in a layered Earth

Now take a model space that is *large*: twelve horizontal layers of $h = 1\ \mathrm{km}$
each, with densities $\rho_k$ in $\mathrm{kg\,m^{-3}}$. Suppose the only datum is
the surface gravity anomaly of the stack. Summing slabs:

$$d = 2\pi G_N h \sum_{k=1}^{12}\rho_k
= c\sum_{k=1}^{12}\rho_k,\qquad c = 0.04193586\
\frac{\mathrm{mGal}}{\mathrm{kg\,m^{-3}}}.$$

Every row of $G$ is the same constant, so $G$ is $1\times12$ of rank $1$. The
null space is

$$\mathcal{N}(G) = \left\{\mathbf{n}:\ \sum_k n_k = 0\right\},
\qquad \dim\mathcal{N}(G) = 12 - 1 = 11,$$

and the data determine **only** the total mass per unit area
$\sum_k \rho_k h$. Pick

$$\mathbf{m}_1 = (100,100,\dots,100),\qquad
\mathbf{n} = 50\,(+1,-1,+1,-1,\dots,+1,-1),\qquad
\mathbf{m}_2 = \mathbf{m}_1 + \mathbf{n}.$$

Because $\sum n_k = 0$ exactly (the alternation cancels in floating point too),
the demonstration reports

$$g(\mathbf{m}_1) = g(\mathbf{m}_2) = 50.323036\ \mathrm{mGal},
\qquad g(\mathbf{m}_1)-g(\mathbf{m}_2) = 0.000\times10^{0}\ \mathrm{mGal},$$

$$\frac{\lVert\mathbf{m}_2-\mathbf{m}_1\rVert}{\lVert\mathbf{m}_1\rVert} = 0.5000,
\qquad \max_k|m_{2,k}-m_{1,k}| = 50\ \mathrm{kg\,m^{-3}}.$$

Two density models that differ by $50\ \mathrm{kg\,m^{-3}}$ in *every* layer
produce bit-identical data. This is not an approximation: the failure of
uniqueness is exact, and it is the reason a gravity profile alone can never give a
unique density-versus-depth structure.

### 3.1 Repairing it, and counting the price

A borehole gravimeter changes the geometry. A sensor at depth $d$ sees a layer
below it pull downward and a layer above it pull upward, so its row of $G$ is
$+c$ or $-c$ depending on whether the layer centre is deeper or shallower than the
sensor (this sign convention is the standard slab result, stated here explicitly).
Stacking the surface reading with $n$ borehole levels gives a matrix whose
measured rank and null-space dimension are:

| borehole levels | data rows | rank | null-space dimension |
|---|---|---|---|
| 0 | 1 | 1 | 11 |
| 1 | 2 | 2 | 10 |
| 3 | 4 | 4 | 8 |
| 5 | 6 | 6 | 6 |
| 8 | 9 | 9 | 3 |
| 11 | 12 | 12 | 0 |

Each new independent level buys exactly one dimension, and **twelve independent
measurements are needed for twelve layers**. With all twelve, and noise at $0.1\%$
of the peak datum, the recovered profile has a mean error of $0.809\%$ (worst of
200 realisations: $1.393\%$).

That last number is the point of the whole exercise. Non-uniqueness is not
"always infinite"; it is a *counting* result. Each independent datum gives one
constraint, each model parameter costs one, and what remains unconstrained is the
difference. It is also a *design* result: the fix is a different measurement, not
a better algorithm.

## 4. Stability, part 1: why a discrete problem is never ill posed

A discretised operator maps $\mathbb{R}^{M}$ to $\mathbb{R}^{N}$; its
pseudo-inverse is bounded whenever the truncation tolerance is fixed, so **every
finite matrix problem satisfies Hadamard's stability condition** once you have
declared a tolerance. Ill-posedness is a statement about the *continuum* problem
that the matrices approximate, and it reveals itself as a growth of the
condition number under refinement. The demonstration refines a stack of masses
inside a fixed $4\ \mathrm{km}$ interval:

| cells $M$ | cell size (km) | $\sigma_{\max}$ | $\sigma_{\min}$ | $\kappa(G)$ | $\varepsilon\,\sigma_{\max}$ |
|---|---|---|---|---|---|
| 4 | 1.000 | $1.5062\times10^{-12}$ | $8.6089\times10^{-16}$ | $1.7496\times10^{3}$ | $3.3\times10^{-28}$ |
| 8 | 0.500 | $2.1534\times10^{-12}$ | $2.6469\times10^{-20}$ | $8.1355\times10^{7}$ | $4.8\times10^{-28}$ |
| 16 | 0.250 | $3.0540\times10^{-12}$ | $4.1191\times10^{-33}$ | $7.4143\times10^{20}$ | $6.8\times10^{-28}$ |
| 32 | 0.125 | $4.3221\times10^{-12}$ | $5.1804\times10^{-38}$ | $8.3432\times10^{25}$ | $9.6\times10^{-28}$ |
| 64 | 0.062 | $6.1135\times10^{-12}$ | $1.5579\times10^{-34}$ | $3.9241\times10^{22}$ | $1.4\times10^{-27}$ |

The condition number grows by three to five orders of magnitude per refinement —
and then, at $M = 64$, it *stops growing* and even falls. That is not a
mathematical plateau: $\sigma_{\min}$ has fallen below
$\varepsilon\sigma_{\max} = 1.4\times10^{-27}$, where $\varepsilon$ is the
double-precision unit roundoff, so the printed value is rounding noise. The
correct reading is:

> the discrete problem's inverse is bounded, the bound is $\kappa(G)$, and the
> bound degrades without limit as the discretisation approaches the continuum.

## 5. Stability, part 2: Hadamard's own example

Hadamard's canonical illustration of instability is differentiation of noisy data.
The demonstration differentiates $f(t)=\sin t$ at $t = 1$ with a central
difference,

$$f'(1)\approx\frac{f(1+h)-f(1-h)}{2h},\qquad f'(1) = \cos 1 = 0.5403023,$$

adding a fixed sample error of $\pm10^{-6}$:

| $h$ | measured $\lvert f'-\cos 1\rvert$ | truncation $\cos(1)h^{2}/6$ | noise $\sim 10^{-6}/h$ |
|---|---|---|---|
| $10^{-1}$ | $8.994\times10^{-4}$ | $9.005\times10^{-4}$ | $1.000\times10^{-5}$ |
| $3\times10^{-2}$ | $8.379\times10^{-5}$ | $8.105\times10^{-5}$ | $3.333\times10^{-5}$ |
| $10^{-2}$ | $1.425\times10^{-5}$ | $9.005\times10^{-6}$ | $1.000\times10^{-4}$ |
| $3\times10^{-3}$ | $8.106\times10^{-5}$ | $8.105\times10^{-7}$ | $3.333\times10^{-4}$ |
| $10^{-3}$ | $2.945\times10^{-4}$ | $9.005\times10^{-8}$ | $1.000\times10^{-3}$ |
| $3\times10^{-4}$ | $2.137\times10^{-3}$ | $8.105\times10^{-9}$ | $3.333\times10^{-3}$ |

For large $h$ the error is the *method's* bias, falling as $h^{2}$. Below
$h\approx10^{-2}$ the noise term $10^{-6}/h$ dominates and the total error
**grows** as $h$ shrinks. There is a minimum in between; setting the two
contributions equal, $\cos(1)h^{2}/6 = \varepsilon/h$, gives
$h_{\text{opt}} = (6\varepsilon/\cos 1)^{1/3} \approx 0.022$, consistent with the
measured minimum between $10^{-2}$ and $3\times10^{-2}$.

This is the stability failure in its purest form: the inverse operator
$\mathrm{d}/\mathrm{d}t$ is unbounded, so no Lipschitz constant
$L$ with $\lVert\delta f'\rVert\le L\lVert\delta f\rVert$ exists. Refining the
sampling — the obvious response to a "resolution" problem — makes the answer
*worse*.

## 6. Fully worked example: reading a rank table

The demonstration also builds eight masses at depths
$5.00 + 0.05k\ \mathrm{km}$, $k = 0,\dots,7$ (50 m apart), observed at 21
stations, and asks for the rank at three tolerances. Relative singular values:

$$1,\ 1.187\times10^{-2},\ 1.179\times10^{-4},\ 1.022\times10^{-6},\
7.852\times10^{-9},\ 5.302\times10^{-11},\ 3.083\times10^{-13},\
1.315\times10^{-15}.$$

*(a)* At relative tolerance $\tau = 10^{-6}$, four singular values exceed
$\tau$, so $\operatorname{rank} = 4$ and $\dim\mathcal{N}(G) = 8-4 = 4$.

*(b)* At $\tau = 10^{-10}$, five exceed it: rank $5$, null space $3$.

*(c)* At $\tau = 10^{-12}$, six exceed it: rank $6$, null space $2$.

Three tolerances, three answers, all correct. The reason is physical: because the
kernel is smooth, the singular values decay without a gap, so there is no natural
place to say "these directions are constrained and those are not". The tolerance
*is* the answer to "how well do I claim to know my data": a relative tolerance of
$\tau$ says that a data direction carrying less than $\tau$ of the largest
singular value is indistinguishable from noise. Reporting a rank without a
tolerance is reporting an opinion as a fact.

## 7. Assumptions and regime of validity

- **Point masses and slabs.** The two test problems use exact closed-form kernels.
  Terrain, regional trends and non-layered structure are absent.
- **Known noise model.** Existence is judged by comparing misfit with a stated
  noise rms. If the noise level is unknown, the same number is uninterpretable;
  estimating it is a separate problem
  ([18-02-06](../02-linear-inverse-problems/06-weighting-and-covariance.md)).
- **The slab sign convention.** Borehole rows assume the standard convention
  stated in §3.1. Change the convention and the signs change; the ranks do not.
- **A declared truncation tolerance.** Every rank and pseudo-inverse here is
  tolerance-dependent, as §6 makes explicit.
- **Double precision.** The refinement table is limited by
  $\varepsilon\approx2.2\times10^{-16}$ at $M = 64$; a higher-precision
  arithmetic would extend the growth by a few more refinements but would not
  change the conclusion.
- **Gaussian, additive, independent errors.** Used for the noise in §3.1; other
  error models change the numbers, not the structure.

## 8. Running the demonstration

The demonstration for this lesson is [`code/hadamard_well_posedness_demo.py`](code/hadamard_well_posedness_demo.py) — print-only, no network access, fixed seed
`np.random.default_rng(20261014)`.

```bash
cd 18-inverse-problems/01-inverse-problem-foundations/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hadamard_well_posedness_demo.py
```

It prints each of the tables above with units, seeded by
`np.random.default_rng(20261014)`, in well under a second with no network access.
Companion problems are in
[`exercises/02-hadamard-well-posedness-exercises.md`](exercises/02-hadamard-well-posedness-exercises.md).

## Mastery checkpoint

Without notes:

> **(a)** Name the three Hadamard conditions and the failure mode each one
> describes, with one geophysical example each. **(b)** A model with 12 layers is
> constrained by 5 independent gravity readings. How large is the null space, and
> what is the *guaranteed* content of the answer? **(c)** A colleague refines the
> model grid from 16 to 32 cells and reports that $\kappa(G)$ grew by five orders
> of magnitude, "so the code has a bug". Correct the claim. **(d)** Why does the
> differentiation example get worse as $h\to0$, and what would you do instead?

Worked solutions to (a)–(d) are in
[`exercises/02-hadamard-well-posedness-solutions.md`](exercises/02-hadamard-well-posedness-solutions.md).

## Common pitfalls

1. **Judging existence with an absolute threshold.** Compare the misfit with the
   stated noise level, never with "small".
2. **Treating a misfit floor as a code failure.** It may be an honest statement
   that the parameterisation cannot express the data.
3. **Believing that more parameters remove non-uniqueness.** More parameters
   *create* null space unless the data grow too.
4. **Reporting "the null space" of a discretised operator.** Report the tolerance
   with it, or report the singular-value spectrum instead.
5. **Fixing an instability by refining.** Refinement makes $\kappa$ worse; the
   remedy is regularisation ([18-03](../03-regularization/README.md)) or better
   data.
6. **Forgetting that uniqueness is a counting result.** Each independent datum
   buys one constraint; every model parameter spends one.

## Related modules

- [18-01-01 Forward vs Inverse Problems](01-forward-and-inverse.md) — the
  amplification that stability failure produces.
- [18-01-03 Null Space and Non-Uniqueness](03-null-space.md) — the equivalence
  class, quantified parameter by parameter.
- [18-02-04 SVD Analysis](../02-linear-inverse-problems/04-svd-analysis-inverse.md) —
  the singular-value machinery used throughout this lesson.
- [01-16-05 Ill-Posedness in the Sense of Hadamard](../../01-mathematics/16-functional-analysis/05-ill-posedness.md) —
  the same conditions in infinite-dimensional spaces.
- [06-06-03 Resolution, Null Space and Model Covariance](../../06-seismology/06-seismic-tomography/03-resolution-and-nullspace.md) —
  the same analysis applied to a real tomographic geometry.
