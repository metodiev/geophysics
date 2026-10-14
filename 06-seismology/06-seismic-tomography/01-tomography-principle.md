---
id: 06-06-01
title: "The Tomography Principle: Data as Path Integrals"
level: graduate
prereqs: ["06-02-02", "03-02-05"]
tags: [seismology, tomography, path-integrals, inverse-problems, resolution]
---

# The Tomography Principle: Data as Path Integrals

All models and data in this module are **SYNTHETIC**. No real survey, station,
catalogue or published Earth model is used anywhere, and every number quoted
below is printed by the demonstration named in the text.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the travel-time datum as a path integral of slowness and **show**
   that its first-order perturbation is a linear functional of the slowness
   perturbation along the reference ray.
2. **Construct** the discrete Jacobian $G$ of a two-dimensional travel-time
   experiment and **state** the units of every factor in it.
3. **Quantify** the error introduced by fixing the rays, and **explain** why the
   same quantity can be made as small as required by iteration.
4. **Define** the null space of a tomographic problem and **exhibit** two models
   that fit the same data to machine precision.
5. **Measure** how the answer changes when the angular range of the rays
   changes at fixed data count.
6. **Interpret** the resolution matrix $R$ as a smearing operator, and **explain**
   why quoting a single resolution length is not reproducible.
7. **Choose** a damping rule by a stated criterion and **report** the model error
   it costs.

## Prerequisites

- [06-02-02 Snell's Law and Layered Media](../02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  the ray parameter and why rays are the characteristics of the eikonal.
- [06-02-04 Ray Tracing](../02-ray-theory-and-travel-times/04-ray-tracing.md) —
  how a path is found in a heterogeneous medium.
- [03-02-05 Linear Algebra with NumPy](../../03-scientific-computing/02-numpy/05-linear-algebra-numpy.md) —
  the singular-value decomposition used throughout.
- [18-01-01 Forward and Inverse Problems](../../18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md) —
  the vocabulary of well-posedness that this lesson makes concrete.

## 1. The one idea, and why it is not an imaging trick

Tomography is usually introduced as "many rays through a body reconstruct its
interior". That description hides the only thing that matters. A travel time is
not a sample of the Earth; it is an **average of slowness along a path**, and the
path depends on the Earth. Everything difficult about tomography follows from
those two clauses: the datum is an integral, not a point measurement, and the
operator that maps a model to data is nonlinear because the path moves.

Write the arrival time of a phase between source $\mathbf{x}_s$ and receiver
$\mathbf{x}_r$ as

$$
T \;=\; \int_{\Gamma} \frac{\mathrm{d}s}{v(\mathbf{x})}
\;=\; \int_{\Gamma} u(\mathbf{x})\,\mathrm{d}s
\tag{1}
$$

with $u = 1/v$ the **slowness** and $\Gamma$ the ray, the path of stationary
travel time (Fermat's principle). Equation (1) is exact for any medium in which
the ray exists. The measured quantity is usually a *perturbation* of a travel
time relative to a reference model,

$$
\delta T \;=\; T_{\text{observed}} - T_0 ,
\tag{2}
$$

and $T_0$ comes from a reference model that is itself an assumption — normally a
one-dimensional average, and normally not the true Earth.

## 2. Linearisation, and what it silently assumes

Let $u = u_0 + \delta u$ and keep the ray fixed at the reference path $\Gamma_0$.
Then (1) gives **exactly**

$$
\delta T^{\text{lin}} \;=\; \int_{\Gamma_0} \delta u\,\mathrm{d}s ,
\tag{3}
$$

because the integrand is linear in $u$. Two distinct approximations are hidden
in the step from (2) to (3), and they are of different kinds.

- **Path error.** The true ray through the perturbed medium is not $\Gamma_0$.
  Fermat's principle saves us: $T$ is stationary with respect to path
  perturbations, so a path error of order $\epsilon$ changes $T$ only at order
  $\epsilon^2$. Lesson 06-06-02 measures this: displacing a ray's mid-point by
  70 m — the true bending in that model — costs **$0.486$ ms on a $5.071$ s
  travel time**.
- **Parametrisation error.** If the model is written as a *velocity*
  perturbation, $v = v_0(1+p)$, then
  $T - T_0 = -\int (\mathrm{d}s/v_0)\,p/(1+p)$, and the first-order
  approximation to that is nonlinear-to-linear. The remainder is
  $+\int (\mathrm{d}s/v_0)\,p^2/(1+p)$.

Both errors shrink as the square of the anomaly. In the demonstration for this
lesson (`code/tomography_demo.py`), a $10\ \mathrm{km}\times 5\ \mathrm{km}$
cross-hole model with 8 per cent velocity anomalies gives

| quantity | value |
|---|---|
| datum $\delta T$ range | $-0.1050$ to $-0.0317\ \mathrm{s}$ |
| rms datum | $6.7096\times10^{-2}\ \mathrm{s}$ |
| max $|$exact $-$ linear$|$ | $6.7691\times10^{-3}\ \mathrm{s}$ |
| rms $|$exact $-$ linear$|$ | $4.0653\times10^{-3}\ \mathrm{s}$ |
| rms error / rms datum | $0.0606$ (6.06 per cent) |

So the linearisation is wrong at the **6 per cent** level for 8 per cent
anomalies. That is small enough for a first iteration and too large to ignore;
it is why travel-time tomography is always described as a sequence of linear
steps, each with its own rays and its own Jacobian.

## 3. The discrete problem

Discretise the region into $N_c$ cells and assume a constant slowness
perturbation $m_j$ in cell $j$. Equation (3) becomes

$$
d_i \;=\; \sum_{j=1}^{N_c} G_{ij} m_j , \qquad
G_{ij} \;=\; \ell_{ij}, \quad \text{(length of ray } i \text{ in cell } j).
\tag{4}
$$

Read the units off (4): $\ell_{ij}$ is in metres and $m_j$ is a slowness
perturbation in $\mathrm{s\,m^{-1}}$, so every entry of $G$ — and hence every
datum — is in seconds. In the demonstration, over a $10\times10$ cell grid with
144 rays, $G$ has 1888 non-zero entries out of 14400, i.e. **13.11 per cent**,
and the mean reference travel time is $2.453\ \mathrm{s}$ (range 2.400 to
2.661 s).

The system is underdetermined whenever $N_c$ exceeds the number of independent
data, and it is *also* effectively underdetermined when the rays fail to cross
some cells at all. In the demonstration, the wide-aperture acquisition has a
mean of 18.9 rays per cell and **no unlit cell**, while the narrow-aperture
acquisition — with the *same 144 rays* — leaves **30 of 100 cells** with no ray.

## 4. Two models, one dataset

The cleanest statement of non-uniqueness needs no statistics. Take the
singular-value decomposition $G = U S V^{\mathsf T}$ and pick any right singular
vector $\mathbf{v}$ with singular value exactly zero: $G\mathbf{v} = 0$. Then
$\mathbf{m}$ and $\mathbf{m} + \alpha\mathbf{v}$ produce **identical** data for
every $\alpha$. In the demonstration:

| quantity | value |
|---|---|
| rank of $G$ (1e-9 relative tolerance) | 89 of 100 |
| null-space dimension | 11 |
| condition number | $8.509\times10^{1}$ |
| $\lVert G\mathbf{m}_1 - \mathbf{d}\rVert$ | $7.4\times10^{-16}$ |
| $\lVert G\mathbf{m}_2 - \mathbf{d}\rVert$ | $7.5\times10^{-16}$ |
| rms$(\mathbf{m}_2-\mathbf{m}_1)$ / rms$(\mathbf{m}_{\text{true}})$ | $0.500$ |
| cell carrying the largest component of $\mathbf{v}$ | $(x = 4.5,\ z = 4.8)\ \mathrm{km}$, crossed by 3 rays |

The two models differ by half the model norm while fitting the data to
$10^{-15}$ of the data norm. This is not a solver failure and it does not go
away with a better method: the data contain zero information about the
component along $\mathbf{v}$. Every published tomographic model is a projection
of the truth onto a data-defined subspace plus an explicit or implicit choice in
the null space, and that choice is a scientific decision.

### Worked example — how much resolution does 144 rays buy?

Take the $10\times10$ grid, $N_c = 100$ and $N_d = 144$ rays. A naive count
suggests "more data than parameters", so a unique answer. The rank measurement
says otherwise: **rank 89**. Compute the shortfall in two ways.

1. *Counting parameters.* $100 - 89 = 11$ null directions. One of them is
   exhibited above: a smooth, grid-spanning perturbation with a 0.5 relative
   difference when added to the least-squares solution.
2. *Counting the missing geometry.* The transverse (vertical) structure is
   sampled only by the angular range of the rays: with the narrow-aperture
   acquisition the same 144 rays leave 30 cells unlit, and the recovered rms
   model error rises from $9.7394\times10^{-3}$ to $1.8133\times10^{-2}$ in
   $v/v_0$ while the variance explained falls from 0.907 to 0.677.

The lesson of the arithmetic is that the useful question is never "how many
equations", but "how many *independent* equations, and with what angle range".

## 5. How the answer depends on the geometry

The demonstration runs two acquisitions that differ **only** in the depth range
of the receivers, so both have 144 rays, the same sources, the same true model
and the same inversion:

| | wide aperture | narrow aperture |
|---|---|---|
| rays per cell (min / median / max) | 3 / 22 / 33 | 0 / 18 / 72 |
| cells with no ray | 0 | 30 |
| data misfit | $2.214\times10^{-4}\ \mathrm{s}$ | $2.875\times10^{-4}\ \mathrm{s}$ |
| shallow anomaly recovered | $+73.7$ per cent | $+71.9$ per cent |
| deep anomaly recovered | $+75.2$ per cent | $+38.6$ per cent |
| rms model error ($v/v_0$) | $9.74\times10^{-3}$ | $1.81\times10^{-2}$ |
| variance explained $R^2$ | 0.907 | 0.677 |
| point-spread $x/z$ ratio of one cell | 1.88 | 2.83 |

Both datasets are fitted to a misfit far below any plausible noise level, and
both produce an image. One of them is twice as good, and the difference is
decided entirely by the range of ray angles crossing the interior. This is why
"we inverted the data" is not a statement about resolution, and why the
resolution test belongs in the paper next to the image.

## 6. The resolution matrix

For damped least squares with damping $\lambda$,

$$
\mathbf{m}(\lambda) = \underbrace{(G^{\mathsf T}G + \lambda^2 I)^{-1}G^{\mathsf T}}_{A(\lambda)}\mathbf{d},
\qquad
R(\lambda) = A(\lambda)G ,
\tag{5}
$$

so that the noise-free estimate is $R(\lambda)\mathbf{m}_{\text{true}}$. The
matrix $R$ is the answer to "what does the inversion do to the truth": its
columns are the images of single cells (point-spread functions), its diagonal
says how much of each cell's estimate is its own, and its rows say which other
cells contribute.

In the demonstration at $\lambda = 10^{-2}\lambda_{\max}$:

| cell | $|R_{kk}|$ | row sum | spread (x, z) | off-diagonal weight |
|---|---|---|---|---|
| $x=2.5$, $z=1.2$ km | 0.882 | 1.041 | 2.37 km, 1.41 km | $+0.160$ |
| corner $x=0.5$, $z=0.2$ km | 0.822 | 0.827 | 3.18 km, 1.93 km | $+0.005$ |

Row sums away from one are exactly the statement that the inversion does not
conserve the amplitude of a cell: some of every cell's estimate comes from
elsewhere. The spread is anisotropic — 2.4 km in $x$ against 1.4 km in $z$ —
because the rays of this survey are mostly horizontal.

## 7. Resolution against variance, and the choice of damping

$R$ measures bias. Noise measures the other half. With data covariance
$\sigma^2 I$, the model covariance is $\sigma^2 A A^{\mathsf T}$, and the
demonstration measures the trade-off directly at $\sigma = 0.02\ \mathrm{s}$:

| $\lambda/\lambda_{\max}$ | $\lVert R-I\rVert_F/\sqrt{n}$ | min row sum | rms bias | rms std dev | total rms error |
|---|---|---|---|---|---|
| $10^{-4}$ | 0.3317 | 0.8294 | $8.62\times10^{-3}$ | $1.476\times10^{-1}$ | $1.479\times10^{-1}$ |
| $10^{-2}$ | 0.3467 | 0.8256 | $8.86\times10^{-3}$ | $1.127\times10^{-1}$ | $1.131\times10^{-1}$ |
| $10^{-1}$ | 0.6346 | 0.7115 | $1.17\times10^{-2}$ | $1.960\times10^{-2}$ | $2.282\times10^{-2}$ |
| $3\times10^{-1}$ | 0.8011 | 0.5503 | $1.37\times10^{-2}$ | $6.638\times10^{-3}$ | $1.519\times10^{-2}$ |
| $10^{0}$ | 0.9493 | 0.1264 | $2.19\times10^{-2}$ | $1.266\times10^{-3}$ | $2.197\times10^{-2}$ |

(all in $\mathrm{s\,m^{-1}}$; the row-space model rms for comparison is
$3.1911\times10^{-2}\ \mathrm{s\,m^{-1}}$). The standard deviation falls by two
orders of magnitude as damping rises while the bias grows; the combined error
has a minimum at an intermediate damping, here $3\times10^{-1}$. The
demonstration also compares three automatic parameter-choice rules against the
best achievable error and finds:

| rule | $\sigma = 0.002$ s | $\sigma = 0.02$ s |
|---|---|---|
| L-curve | $1.32\times$ optimum | $9.19\times$ optimum |
| GCV | $1.19\times$ | $6.64\times$ |
| discrepancy principle | $1.03\times$ | $1.00\times$ |

The ranking is problem dependent and it is not the point. The point is that the
same data and the same code produce answers a factor of nine apart in model
error depending on a rule that the analyst chooses, and none of the rules knows
the answer. A tomographic image is not reproducible without the damping rule,
the data misfit actually achieved, and the assumed noise level.

## 8. Assumptions and regime of validity

1. **Ray theory.** The datum is a path integral along a ray. This fails where
   the wavelength is comparable to the structure (diffraction, scattering) and
   in the shadow of strong heterogeneity. The remedy is finite-frequency
   sensitivity kernels (lesson 06-06-05).
2. **First-order perturbation.** Valid for anomalies small compared with the
   background over the relevant length scale; measured at 6 per cent of the
   datum for 8 per cent anomalies in this model.
3. **Fixed rays.** Justified by Fermat stationarity, which makes the neglected
   term second order in the path error; measured at 0.486 ms in lesson 06-06-02.
4. **Constant slowness per cell.** The parametrisation sets the smallest
   structure the answer can contain. A feature smaller than a cell cannot exist
   in the model, and refining the grid does not create it (lesson 06-06-02
   measures the penalty).
5. **Known source and receiver positions and times.** Location errors, clock
   errors and origin-time errors project into the model, usually as long-
   wavelength artefacts; the classic trade-off between velocity and hypocentre
   depth belongs to lesson 06-04-02.
6. **The reference model is part of the answer.** Changing $v_0$ changes the
   rays, the Jacobian, and the neglected second-order term, so the perturbation
   is defined with respect to something that must be stated.

## 9. Exercises, demonstration and where to go next

The runnable demonstration is
[`code/tomography_demo.py`](code/tomography_demo.py) — five measured sections:
the forward problem and its linearisation error, the null space made explicit,
the aperture experiment, the resolution-variance trade-off, and three
parameter-choice rules. Graded exercises with worked solutions are in
[`exercises/01-tomography-principle-exercises.md`](exercises/01-tomography-principle-exercises.md)
and
[`exercises/01-tomography-principle-solutions.md`](exercises/01-tomography-principle-solutions.md).

## Mastery checkpoint

Complete this without notes.

> A cross-hole survey over $10\ \mathrm{km}\times5\ \mathrm{km}$ is discretised
> into $10\times10$ cells and recorded with 144 rays, giving a Jacobian of rank
> 89. **(a)** State the dimension of the null space and write down one null-space
> vector in words. **(b)** Explain why adding a second dataset with the same 144
> rays but a different angular range can improve the image even though the number
> of data is unchanged. **(c)** Given that a $+8$ per cent velocity anomaly
> changes the datum by about $0.067\ \mathrm{s}$ rms, estimate the size of the
> neglected second-order term for a $+4$ per cent anomaly and justify the scaling
> you used. **(d)** State two numbers that a published tomographic image must
> report for you to be able to reproduce it.

## Common pitfalls

1. **Treating the datum as a point sample.** A travel time is an average along
   a path; two different structures can give the same average, and the average
   moves when the structure changes.
2. **Counting equations instead of independent equations.** 144 rays gave rank
   89, not 100, on a 100-parameter grid.
3. **Quoting "the resolution" as a number.** Resolution is a matrix with a
   direction: 2.4 km in $x$ and 1.4 km in $z$ for the same cell here.
4. **Choosing the damping by taste.** The same data gave model errors differing
   by a factor of nine under three standard rules.
5. **Forgetting the units of the Jacobian.** Lengths in metres divided by a
   velocity give seconds; a slowness perturbation is $\mathrm{s\,m^{-1}}$, and a
   velocity perturbation converted to slowness is $-\delta v/v_0^2$ to first
   order.
6. **Believing a small data misfit.** Every row of the aperture experiment fits
   the data; the images differ by a factor of two in error.

## Related modules

- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  the ray family this module differentiates.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  the same inversion machinery applied to amplitude and $t^*$.
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) — the
  same inverse problem with a controlled source and a much denser geometry.
- [18-01 Foundations of Inverse Problems](../../18-inverse-problems/01-inverse-problem-foundations/README.md) —
  well-posedness, null space and discretisation in general form.
- [18-02 Linear Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/README.md) —
  the singular-value analysis used here.
