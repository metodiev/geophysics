---
id: 07-03-04
title: "Gravity Inversion and Its Severe Non-Uniqueness"
level: doctoral
prereqs: ["07-03-03", "18-01-03"]
tags: [gravity, geodesy, inversion, non-uniqueness, regularisation]
---

# Gravity Inversion and Its Severe Non-Uniqueness

All models and data in this module are SYNTHETIC. The target block, the station
spacing and the noise level used below are chosen teaching values.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** a discretised gravity inverse problem as
   $\mathbf{d} = \mathbf{A}\mathbf{m}$ and **state** what each vector means with
   units.
2. **Implement** non-negative least squares with a smoothness penalty and
   **read** the misfit-versus-regularisation trade-off table.
3. **Demonstrate** two structurally different models that fit the same data
   equally well, and **explain** why the data cannot choose between them.
4. **Compute** the model resolution matrix and **interpret** its diagonal as a
   depth-dependent visibility.
5. **Construct** an exact annihilator for a single-wavelength data set and
   **state** the mass ambiguity it implies.
6. **Report** an admitted set of models rather than a best-fit model, and
   **explain** how the survey aperture sets its width.
7. **Explain** why non-uniqueness in gravity is not a numerical artefact.

## Prerequisites

- [03 Forward Modelling in 2-D and 3-D](03-forward-modelling-2d3d.md) — how
  $\mathbf{A}$ is built.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the general theory of what a null space is.

## 1. The problem, and why it is not a numerical accident

Gravity inversion asks for a density distribution whose predicted anomaly matches
an observed one. The data are finite in number and sampled on a 2-D surface; the
unknown is a 3-D continuum. Even in the ideal case of exact, noise-free data on a
complete surface, the answer is not unique: the classic result is that **any
density distribution can be altered by adding a suitable distribution confined to
the observation surface, or by adding any mass distribution external to the
observation domain, without changing the measured field at all.**

The practical consequence is not "inversion is useless" but "inversion is
selection". Regularisation, depth weighting, sparsity and bounds are all choices
that break the ambiguity; they are assumptions about the Earth, and they should
be reported as such.

## 2. Formulation

Parameterise the subsurface into $p$ cells of known density contrast and write

$$\mathbf{d} = \mathbf{A}\mathbf{m} + \mathbf{e}, \qquad
\mathbf{d}\in\mathbb{R}^{n},\;
\mathbf{m}\in\mathbb{R}^{p},\;
\mathbf{A}\in\mathbb{R}^{n\times p},$$

with $d_i$ in $\mathrm{m\,s^{-2}}$, $m_j$ in $\mathrm{kg\,m^{-3}}$ and
$A_{ij}$ in $\mathrm{m\,s^{-2}}$ per $\mathrm{kg\,m^{-3}}$. The demonstration's
problem has $n = 61$ stations at $100\ \mathrm{m}$ spacing over $6\ \mathrm{km}$
and $p = 246$ cells (41 columns $\times$ 6 depth layers from $100\ \mathrm{m}$ to
$6.4\ \mathrm{km}$): **four parameters for every datum.**

The synthetic truth is a 2-D block from $-800\ \mathrm{m}$ to $+800\ \mathrm{m}$
in $x$, from $200\ \mathrm{m}$ to $1200\ \mathrm{m}$ in depth, with
$\Delta\rho = 400\ \mathrm{kg\,m^{-3}}$, giving a peak anomaly of
$9.4791\ \mathrm{mGal}$; $0.02\ \mathrm{mGal}$ rms noise is added.

### 2.1 The regularised objective

Minimise

$$\Phi(\mathbf{m}) =
\left\|\mathbf{A}\mathbf{m}-\mathbf{d}\right\|^{2}
+ \alpha\left\|\mathbf{D}\mathbf{m}\right\|^{2},
\qquad \mathbf{m}\ge 0,$$

where $\mathbf{D}$ is a first-difference operator in $x$ and in depth (445 rows
here) and $\alpha$ sets the trade-off. Non-negativity is imposed because a
negative mass can only be an artefact of a density *contrast* being expressed
relative to a reference, and because it is the cheapest available physical
constraint.

## 3. The trade-off, measured

| $\alpha$ | rms misfit (mGal) | mass per unit length ($\mathrm{kg\,m^{-1}}$) | mass centre depth (m) |
|---|---|---|---|
| $10^{-6}$ | 0.0109 | $5.877\times10^{8}$ | 229.5 |
| $10^{-5}$ | 0.0115 | $5.972\times10^{8}$ | 297.6 |
| $10^{-4}$ | 0.0139 | $6.362\times10^{8}$ | 643.2 |
| $10^{-3}$ | 0.0277 | $6.495\times10^{8}$ | 736.7 |
| $10^{-2}$ | 0.3857 | $7.224\times10^{8}$ | 1093.4 |
| $10^{-1}$ | 1.9455 | $1.101\times10^{9}$ | 3020.0 |

Two features matter. First, the misfit floor is $0.0109\ \mathrm{mGal}$ — *below*
the $0.02\ \mathrm{mGal}$ noise: the inversion is fitting noise, which is the
signature of over-parameterisation. Second, the depth of the recovered mass moves
by a factor of **13** (230 m to 3020 m) across the table while the misfit changes
by a factor of 180. The table is a statement about the penalty, not about the
Earth.

## 4. Two models, one data set

Take $\alpha = 10^{-5}$ and compare with the truth:

| model | rms misfit (mGal) | mass centre depth (m) | mass per unit length ($\mathrm{kg\,m^{-1}}$) |
|---|---|---|---|
| true block | 0.0205 (it *is* the noise) | 700.0 | $6.400\times10^{8}$ |
| inverted | 0.0115 | 297.6 | $5.972\times10^{8}$ |

The inverted model fits **better** than the truth, and places its mass at less
than half the true depth. Nothing in the data rejects it. This is the
non-uniqueness of §1, measured on a small problem where the answer is known.
Reporting the inverted model without the truth comparison would be reporting an
artefact of the regularisation.

## 5. Resolution: what the data can and cannot see

For a linear, regularised problem the model resolution matrix is

$$\mathbf{R} = \left(\mathbf{A}^{\mathsf{T}}\mathbf{A}
+ \alpha\mathbf{D}^{\mathsf{T}}\mathbf{D}\right)^{-1}
\mathbf{A}^{\mathsf{T}}\mathbf{A},$$

and $\mathrm{diag}(\mathbf{R})$ measures how much of each parameter the data
determine. Averaged over the 41 columns of each layer:

| layer depth (m) | mean $\mathrm{diag}(\mathbf{R})$ | reading |
|---|---|---|
| 100–200 | 0.5446 | well resolved |
| 200–400 | 0.3812 | weakly resolved |
| 400–800 | 0.1090 | weakly resolved |
| 800–1600 | 0.0423 | essentially invisible |
| 1600–3200 | 0.0248 | essentially invisible |
| 3200–6400 | 0.0174 | essentially invisible |

The trace is $45.9$ for $246$ parameters and $61$ data. Two general statements
follow. **The number of resolvable parameters cannot exceed the number of
independent data**, whatever the grid resolution; and **resolution decays roughly
as depth$^{-2}$**, because the kernel weakens and broadens with depth. A
depth-weighted penalty (multiplying cell $j$ by $z_j^{\beta}$) is therefore not a
cosmetic choice: it is the statement of how much structure at each depth you are
willing to invent.

## 6. An exact annihilator

Consider a thin sheet at depth $h$ with surface density
$\sigma(x) = \sigma_0\cos kx$. Its vertical gravity is

$$g_z(x) = 2\pi G\sigma_0\cos(kx)\,e^{-kh}$$

(a result obtained by Fourier transforming the line-mass kernel
$2Ghz/(x^{2}+h^{2})$; the demonstration verifies the discrete sum against this
analytic kernel to a relative difference of $10^{-4}$, which is the quadrature
error of the discrete sheet).

Now take **two** such sheets: $\sigma_1$ at $h_1 = 800\ \mathrm{m}$ and
$\sigma_2 = -\sigma_1 e^{k(h_2-h_1)}$ at $h_2 = 1600\ \mathrm{m}$, with
$k = 2\pi/1000\ \mathrm{m^{-1}}$. Their sum is

$$2\pi G\cos(kx)\left[\sigma_1e^{-kh_1} + \sigma_2e^{-kh_2}\right] = 0$$

**identically, at every $x$**. The demonstration measures the residual of the
sum: it is $1.2\%$ of the individual signal in discrete sums whose own accuracy is
$10^{-4}$, i.e. pure quadrature error amplified by near-cancellation; in the
continuum the cancellation is exact. With $h_2-h_1 = 800\ \mathrm{m}$ the
required amplitude ratio is $e^{k\Delta h} = 152.4$: **the deeper sheet carries
152 times the mass of the shallower one, and the data see nothing.**

For a single-wavelength data set this is an exact null-space direction. For
broadband data it is only approximate — which is why real inversions show a
*valley* of acceptable models rather than a flat direction.

## 7. The admitted set, and what sets it

Fix the shape to a point mass, keep the mass free, and accept every depth whose
best-fitting model has rms misfit below the stated noise ($0.02\ \mathrm{mGal}$).
The true body is $2.0\times10^{11}\ \mathrm{kg}$ at $1000\ \mathrm{m}$.

| aperture (m) | stations | admitted depth (m) | admitted mass (kg) | mass factor |
|---|---|---|---|---|
| 500 | 21 | 805–1462 | $1.32\times10^{11}$–$4.20\times10^{11}$ | 3.19 |
| 1000 | 41 | 919–1099 | $1.72\times10^{11}$–$2.38\times10^{11}$ | 1.38 |
| 2000 | 81 | 956–1050 | $1.86\times10^{11}$–$2.16\times10^{11}$ | 1.16 |
| 8000 | 321 | 938–1071 | $1.81\times10^{11}$–$2.21\times10^{11}$ | 1.22 |

Two conclusions, both measurable. **The aperture, not the number of
observations, sets the resolution**: an aperture comparable to the source depth
admits a depth range of a factor $1.8$ and a mass range of $3.2$. And **even a
wide aperture leaves a $22\%$ mass range** once the noise is honest. Reporting
the best-fit depth alone hides both.

## 8. Worked example

*Invert a $0.30\ \mathrm{mGal}$ residual anomaly with a $4\ \mathrm{km}$
aperture and $0.02\ \mathrm{mGal}$ noise.*

1. Fit the point-mass shape: $M = g z^{2}/G$. With
   $g = 0.30\ \mathrm{mGal} = 3.0\times10^{-6}\ \mathrm{m\,s^{-2}}$ and
   $z = 1000\ \mathrm{m}$,
   $$M = \frac{3.0\times10^{-6}\times10^{6}}{6.67430\times10^{-11}}
   = 4.49\times10^{10}\ \mathrm{kg}.$$
2. From the aperture table, a $4\ \mathrm{km}$-wide aperture at that depth admits
   roughly $\pm7\%$ in depth ($z$ between about $940$ and $1070\ \mathrm{m}$),
   i.e. $\pm15\%$ in depth from the shape alone at half the aperture.
3. Propagate to mass: $M \propto z^{2}$ at fixed peak, so a $+15\%$ depth error
   is $+32\%$ in mass; the table's mass factor $1.16$–$1.22$ is the
   noise-limited version of the same statement.
4. If the body could be a dyke instead of a point mass, add the shape ambiguity
   of [01 §3.6](01-anomaly-interpretation.md): another $30\%$ in depth.
5. **Report:** "a compact body of $2$–$6\times10^{10}\ \mathrm{kg}$ at
   $800$–$1500\ \mathrm{m}$ depth, assuming a compact shape; deeper and larger if
   the body is extended." That sentence is the deliverable; the model grid is
   not.

## 9. Assumptions and regime of validity

1. **Linear physics and a fixed parameterisation.** Both are choices; changing
   the cell grid changes the answer, as §3 shows.
2. **Known noise level.** The admitted set is only meaningful relative to a
   stated noise; without it, *every* model with a smaller misfit is "acceptable".
3. **Density contrast relative to a reference.** Only contrasts are recoverable
   from gravity alone.
4. **2-D geometry** in this demonstration; the null-space structure is richer in
   3-D, not poorer.
5. **No independent constraints.** Bounds, petrophysics, boreholes and other
   geophysical data remove null-space components; they do not merely "improve"
   the model.
6. **Non-negativity is itself an assumption**, and one that can be wrong: a
   low-density body inside a dense one requires a negative contrast.

## 10. Physical interpretation

- The kernel decays and broadens with depth, so deep structure leaves a smooth
  imprint that shallow structure can mimic. That is the whole content of the
  resolution matrix.
- A null space exists because gravity measures a *projection*, and projections
  have kernels. Only additional physics — a different measurement, a
  petrophysical relation, a borehole — can supply the missing components.
- Regularisation is a prior. Choosing it by eye, or by whatever value makes the
  picture look geological, is choosing a prior by taste; the L-curve and
  discrepancy principle of
  [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](../../18-inverse-problems/03-regularization/03-parameter-choice.md)
  exist to make the choice explicit.

## 11. Python demonstration

`code/inversion_gravity_demo.py` prints:

1. the synthetic data set and its statistics;
2. the $\alpha$ trade-off table with mass and mass-centre depth;
3. the truth-versus-inversion comparison, both within the noise;
4. the resolution matrix diagonal per depth layer and $\mathrm{trace}(\mathbf{R})$;
5. the exact annihilator, its discrete residual and the mass ratio it implies;
6. the aperture study, with admitted depth and mass ranges.

Every number in this lesson is from that output; the script is print-only, uses
`np.random.default_rng(20261014)` and exits 0.

## 12. Exercises

See
[`exercises/04-inversion-gravity-exercises.md`](./exercises/04-inversion-gravity-exercises.md)
and
[`exercises/04-inversion-gravity-solutions.md`](./exercises/04-inversion-gravity-solutions.md).

- **★** Write $\mathbf{d} = \mathbf{A}\mathbf{m}$ for three stations and two
  cells, and state the units of every entry.
- **★** State two distinct density distributions that produce no field outside
  their own surface.
- **★★** From the $\alpha$ table, choose a regularisation for a survey whose
  noise is $0.02\ \mathrm{mGal}$ and justify it against the honesty of the
  misfit.
- **★★** Compute $\mathrm{trace}(\mathbf{R})$ for the demonstration and explain
  why it must be less than $n = 61$.
- **★★★** Derive the annihilator condition for two sheets at depths $h_1, h_2$
  and show that the required amplitude ratio grows exponentially with
  $(h_2-h_1)$.

## Mastery checkpoint

Without notes:

> A $0.30\ \mathrm{mGal}$ anomaly is modelled by a point mass or by a finite
> dyke. The survey has a $4\ \mathrm{km}$ aperture and $0.02\ \mathrm{mGal}$
> noise.

**(a)** Give the mass for a $1\ \mathrm{km}$-deep point mass.
**(b)** Give the admitted depth range from the aperture table.
**(c)** Give the resulting admitted mass range.
**(d)** State one additional measurement that would collapse the range, and one
sentence of warning about reporting only the best-fit model.

## Common pitfalls

1. **Reporting a best-fit model as an answer.** The admitted set is the answer.
2. **Choosing $\alpha$ to make the picture look right.** State the criterion.
3. **Reading a misfit below the noise as success.** It is a symptom.
4. **Forgetting that resolution is depth-dependent.** A sharp feature at depth
   is usually an artefact of the penalty, not a discovery.
5. **Ignoring the aperture.** Width of coverage, not count of stations, sets the
   admitted set.
6. **Believing a "unique" solution because the matrix was invertible.** The
   inverse exists because a penalty was added.

## 13. Applications

- **Basin depth and shape.** Gravity inversions for sediment thickness are
  routinely regularised and depth-weighted; the resolution table is what the
  interpreter should attach to them.
- **Orebody mass estimation.** Excess mass is better constrained than shape, and
  is often all the data support.
- **Subsurface storage and cavity detection.** As in
  [06](06-microgravity-applications.md), the honest product is a depth range.
- **Joint inversion.** Adding a second data type removes null-space components;
  see
  [18-07-01 Why Joint Inversion: Complementary Sensitivities](../../18-inverse-problems/07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md).

## Related modules

- [03 Forward Modelling in 2-D and 3-D](03-forward-modelling-2d3d.md).
- [05 Derivatives, Upward/Downward Continuation and Euler Deconvolution](05-derivatives-and-filters.md) —
  the deterministic, non-inverse way to estimate depth.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md).
- [18-02-05 Resolution and Information Matrices in Interpretation](../../18-inverse-problems/02-linear-inverse-problems/05-resolution-matrices.md).
- [21-01-02 Choosing Probability Models for Earth Data](../../21-statistics-bayesian-ml/01-statistics-in-practice/02-probability-models-earth.md) —
  likelihoods for the admitted set.

## 14. Self-assessment checklist

- [ ] I can write a gravity inverse problem and its units.
- [ ] I can implement NNLS with a smoothness penalty.
- [ ] I can interpret a misfit-versus-$\alpha$ table honestly.
- [ ] I can compute and read a resolution matrix.
- [ ] I can construct a two-sheet annihilator and state its mass ratio.
- [ ] I can report an admitted set from an aperture table.
