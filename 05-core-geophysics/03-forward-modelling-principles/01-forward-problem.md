---
id: 05-03-01
title: "The Forward Problem: From Model to Data"
level: intermediate
prereqs: ["05-02-01"]
tags: [forward-problem, model-space, data-space, kernel, well-posedness]
---

# The Forward Problem: From Model to Data

## Learning objectives

1. **State** the forward problem formally as a map from model space to data
   space, and name its components.
2. **Distinguish** the forward problem (unique and usually well-posed) from the
   inverse problem (non-unique).
3. **Write** a forward operator for gravity as an integral and discretise it.
4. **Explain** what a kernel is and why its smoothness controls everything.
5. **Verify** a forward code against an independent method before trusting it.

## Prerequisites

- [05-02-01 Scalar and Vector Fields](../02-geophysical-fields-and-observables/01-scalar-vs-vector-fields.md)
- [01-07-02 Matrices and Operations](../../01-mathematics/07-linear-algebra/02-matrices-and-operations.md)

## 1. Intuition

Forward modelling is the easy direction: given the rock, predict the reading.
It is easy because nature integrates, and integration is a smoothing, stable
operation. Inverting — recovering rock from readings — is hard because
integration destroys information.

Forward modelling is nevertheless where all interpretation starts, because you
cannot assess a model without knowing what data it predicts.

## 2. Formal statement

Let $\mathbf{m} \in \mathcal{M}$ be a model (a function or a vector of
parameters) and $\mathbf{d} \in \mathcal{D}$ the data.

$$F: \mathcal{M} \to \mathcal{D}, \qquad \mathbf{d} = F[\mathbf{m}] + \boldsymbol{\eta},$$

with $\boldsymbol{\eta}$ the noise. For a **linear** problem,

$$\mathbf{d} = \mathbf{G}\mathbf{m} + \boldsymbol{\eta}, \qquad
G_{ij} = K(\text{observation } i,\ \text{cell } j).$$

**Model space** $\mathcal{M}$: what you parameterise — a density distribution, a
set of layer thicknesses, a mesh of conductivities.

**Data space** $\mathcal{D}$: the vector of observations, with units.

**Kernel**: the sensitivity of one datum to one model cell. It carries all the
physics and all the geometry.

## 3. Derivation: the gravity forward operator

For a density distribution $\Delta\rho(\mathbf{r}')$, the vertical attraction at
$\mathbf{r}$ is

$$g_z(\mathbf{r}) = G\int_V \frac{\Delta\rho(\mathbf{r}')\,(z-z')}
{|\mathbf{r}-\mathbf{r}'|^3}\,dV'.$$

Discretising $V$ into cells of volume $\Delta V_j$ with constant density
$m_j = \Delta\rho_j$:

$$d_i = g_z(\mathbf{r}_i) = G\sum_j \frac{(z_i-z_j)}{|\mathbf{r}_i-\mathbf{r}_j|^3}
\Delta V_j\, m_j \implies G_{ij} = G\,\Delta V_j
\frac{z_i-z_j}{|\mathbf{r}_i-\mathbf{r}_j|^3}.$$

Dimension check: $[G] = \mathrm{m^3kg^{-1}s^{-2}}$, $[\Delta V] = \mathrm{m^3}$,
$\mathrm{m/m^3}$, so $[G_{ij}] = \mathrm{m^3s^{-2}kg^{-1}}$ and
$G_{ij}m_j$ has $\mathrm{m\,s^{-2}}$. ✓

**The kernel is smooth and positive-definite in the wrong way**: two adjacent
cells have almost identical columns of $\mathbf{G}$, so $\mathbf{G}$ is severely
ill-conditioned. This is the mathematical face of non-uniqueness
([05-03-... see 05-01-04](../01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md)).

### 3.1 From a volume integral to a matrix, with its error

The kernel matrix does not appear from nowhere. It is the midpoint rule applied
to a volume integral, and knowing that tells you both where the error comes from
and how to reduce it.

Write the exact forward operator for a sheet-like source as a convolution
(derived in [05-01-04](../01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md)):

$$g_z(x_i) = \int \frac{2G\,d}{\left(x_i-x'\right)^2+d^2}\,\sigma(x')\,\mathrm{d}x' .$$

Partition the model into $n_s$ cells of width $\Delta x$ centred at $x_j$ and
approximate the integral by a sum:

$$g_z(x_i) \;\approx\; \sum_{j=1}^{n_s}
\underbrace{\frac{2G\,d\,\Delta x}{\left(x_i-x_j\right)^2+d^2}}_{G_{ij}}\,
\sigma(x_j)
\qquad\Longrightarrow\qquad \mathbf{d} = \mathbf{G}\boldsymbol{\sigma} .$$

**The error of this approximation.** The midpoint rule on a smooth integrand has
local error $(h^2/24)f''(\xi)$, so the operator error is $O(\Delta x^2)$ — until
the cell becomes comparable to $d$, at which point the integrand's variation
across a cell is no longer small and the expansion fails.

**Measured convergence.** Summing the Gaussian-sheet forward model on grids of
increasing $n_s$ and comparing with a 200 001-point reference:

| $n_s$ | relative difference from the reference |
|---|---|
| 50 | $1.195\times10^{-3}$ |
| 100 | $4.640\times10^{-7}$ |
| 200 | $6.670\times10^{-12}$ |
| 400 | $6.670\times10^{-12}$ |
| 800 | $6.670\times10^{-12}$ |

The convergence is far faster than $\Delta x^2$ because the integrand here is
analytically smooth (a Gaussian) and the kernel is broad relative to the cell:
the effective rule behaves like a high-order quadrature. **The floor at
$6.67\times10^{-12}$ is not discretisation error** — it is the difference between
the normalisation used for the reference mass (trapezoid) and for the sampled
model (rectangle sum). Reporting the floor and its cause matters: someone
refining the grid further would otherwise conclude that the code had stalled.

**Choice of discretisation, and the cost.** Halving $\Delta x$ doubles $n_s$ and
therefore quadruples the size of $\mathbf{G}$ (which is $n_o\times n_s$). For a
3-D model the cost grows as $\Delta x^{-3}$ for assembly and as
$\Delta x^{-2}$ or worse for a solve. Discretisation is therefore a *trade
against accuracy and conditioning simultaneously*, and Section 3.2 shows the
conditioning gets worse, not better.

### 3.2 Why the matrix is ill-conditioned: the angle between two columns

The condition number of $\mathbf{G}$ is large because its columns are nearly
parallel. Make that quantitative.

Column $j$ is the anomaly produced by unit density in cell $j$. Two adjacent
cells differ only in the position of a narrow source at the same depth, so their
patterns differ by a small amount. The cosine of the angle between them
measures the degeneracy. Measured for the demonstration's geometry
($n_o = 120$ observations, $n_s = 400$ cells over 12 km, depth 300 m):

| $\Delta x/d$ | $\cos\theta$ | $1-\cos\theta$ | angle (deg) |
|---|---|---|---|
| 0.404 | 0.960786102 | $3.92\times10^{-2}$ | 16.10 |
| 0.201 | 0.989999927 | $1.00\times10^{-2}$ | 8.11 |
| **0.100** | **0.997493645** | $2.51\times10^{-3}$ | **4.06** |
| 0.050 | 0.999373783 | $6.26\times10^{-4}$ | 2.03 |

The pattern is exact and worth stating as a scaling law:

$$1-\cos\theta \;\approx\; 0.25\left(\frac{\Delta x}{d}\right)^{2},
\qquad\Longrightarrow\qquad
\theta \;\approx\; 0.707\,\frac{\Delta x}{d}\ \text{rad}
\;=\; 40.5\,\frac{\Delta x}{d}\ \text{degrees},$$

verified to better than 1% for $\Delta x/d \le 0.2$ (the constant is 0.25 to
within 4% even at the coarsest row).

**Physical interpretation.** The angle between columns is the *information
content* of a cell: at $\Delta x/d = 0.1$ two neighbouring cells are
indistinguishable to within $4°$ of pattern space, which is why the data cannot
separate them. Making cells finer $\propto\Delta x$ makes them *more*
indistinguishable, quadratically — **refinement increases resolution in the sense
of parameterisation while decreasing it in the sense of conditioning.**

**Depth, measured.** The same construction at 1200 m depth gives
$\cos\theta = 0.999842581$ for $\Delta x/d = 0.0251$, and the condition number of
the $120\times400$ operator rises as

| depth (m) | $\operatorname{cond}(\mathbf{G})$ |
|---|---|
| 50 | $3.33$ |
| 100 | $15.6$ |
| 300 | $7.62\times10^{3}$ |
| 600 | $8.11\times10^{7}$ |
| 1200 | $8.27\times10^{15}$ |

a rise of twelve orders of magnitude across a factor of 24 in depth.

### 3.3 Why depth hurts so much: homogeneity of the kernel

The kernel is homogeneous in depth. Collect factors of $d$:

$$G_{ij} = 2G\,d\,\Delta x\cdot\frac{1}{\left(x_i-x_j\right)^2+d^2}
= \frac{2G\,\Delta x}{d}\cdot\frac{1}{1+
\left(\dfrac{x_i-x_j}{d}\right)^{2}} .$$

So the kernel is (i) an amplitude factor $2G\Delta x/d$ and (ii) a shape function
of the dimensionless variable $(x_i-x_j)/d$ alone. Two consequences follow:

- **Amplitude** falls as $d^{-1}$, so deep sources produce weak data;
- **Shape** broadens as $d$, so at large $d$ every row of $\mathbf{G}$ is a slow,
  smooth function and the rows become nearly parallel — which is the
  ill-conditioning of Section 3.2, now seen from the row side.

The combination is why the *signal-to-noise* problem and the
*conditioning* problem both worsen with depth, and why regularisation becomes
unavoidable rather than optional.

### 3.4 The resolution matrix, derived and measured

Section 3.2 measured how nearly parallel the columns of $\mathbf{G}$ are. The
*consequence* for an inversion is captured by one object: the resolution matrix

$$\mathbf{R} \equiv \mathbf{G}^{+}\mathbf{G},$$

where $\mathbf{G}^{+}$ is the Moore–Penrose pseudoinverse. For an estimate
$\hat{\mathbf{m}} = \mathbf{G}^{+}\mathbf{d}$ of a true model
$\mathbf{d} = \mathbf{G}\mathbf{m}$ (noise-free),

$$\hat{\mathbf{m}} = \mathbf{G}^{+}\mathbf{G}\mathbf{m} = \mathbf{R}\mathbf{m}
\ \Longrightarrow\
\hat m_i = \sum_j R_{ij}m_j .$$

So **row $i$ of $\mathbf{R}$ is the averaging kernel for cell $i$**: it says how
much of each true cell leaks into the estimate of cell $i$. Its properties are
diagnostic:

- $R_{ii} = 1$ and $R_{ij} = 0$ for $j \ne i$ means perfect resolution;
- $\sum_j R_{ij} = 1$ (a row sums to one if the operator is unbiased in the mean);
- a *broad* row means the estimate is a smeared average rather than a local value.

**Measured** for the demonstration's geometry ($n_o = 120$, $n_s = 400$,
$\Delta x \approx 30$ m, depth 300 m), at the central cell:

| quantity | measured value |
|---|---|
| diagonal $R_{ii}$ | **0.2834** |
| row sum $\sum_j R_{ij}$ | 3.53 cells $= 106$ m |
| largest off-diagonal $\lvert R_{ij}\rvert$, $j\ne i$ | 0.9304 |

**Read the numbers.** The inversion recovers **28% of the true value of the
central cell** and distributes the remaining 72% over its neighbours: the leading
off-diagonal element carries 93% of the cell's own value. The resolution width is
3.53 cells = 106 m, or **$0.35\,d$** — narrow compared with the anomaly
half-width ($1.53d$), because the inversion is *exploiting* the data's smoothness
to localise better than the raw anomaly width. That is the precise sense in which
linear inversion beats visual inspection, and the resolution matrix is how much
better it is.

**Why this belongs in the forward-modelling module.** $\mathbf{R}$ depends only on
$\mathbf{G}$ and on the inverse operator's parameterisation — not on the data.
It is therefore a property of the *survey design and discretisation*, computable
before any measurements exist, which makes it the right tool for planning. A
target that requires $R_{ii} > 0.5$ needs a shallower body, a larger contrast, or
a coarser model parameterisation than a target that tolerates 0.28.

### 3.5 Nonlinear problems, and what changes

Everything above assumed $\mathbf{d} = \mathbf{G}\mathbf{m}$. For a nonlinear
forward operator the structure survives *locally* and only locally.

Expand $F$ about a reference model $\mathbf{m}_0$:

$$F[\mathbf{m}_0+\delta\mathbf{m}] \approx F[\mathbf{m}_0]
+ \mathbf{J}\,\delta\mathbf{m}, \qquad
J_{ij} = \frac{\partial F_i}{\partial m_j}\bigg|_{\mathbf{m}_0},$$

so the Jacobian plays the role of $\mathbf{G}$ for *perturbations*. Everything the
lesson derived about $\mathbf{G}$ then applies to $\mathbf{J}$ at that reference
model — conditioning, near-parallel columns, null space — with two additions:

- the null space is now *local*, so it moves as the model moves, and a model can
  be well constrained in one region of model space and poorly constrained in
  another;
- the misfit surface is curved, so the linearised step must be damped and
  iterated, which is where the machinery of
  [18-04-01](../../18-inverse-problems/04-nonlinear-inversion/01-local-linearization.md)
  begins.

**Where nonlinearity enters geophysics.** Gravity in density is exactly linear.
Magnetics in magnetisation is linear only if demagnetisation is neglected
([05-03-03](./03-superposition.md)). Resistivity is linear in *potential* but
nonlinear in *conductivity*, so the Jacobian must be computed by solving the
linear problem for each parameter perturbation. Seismic travel-time tomography is
nonlinear because the raypaths depend on the velocity field being estimated — the
operator itself is model-dependent, which is the strongest form of the
difficulty.

**The practical diagnostic.** Compare the misfit for a linear step at two step
sizes. If halving the step halves the misfit, the problem is locally linear and a
Gauss–Newton step is adequate. If it does not, the curvature is significant and
damping is required. **That test — cheap, and rarely performed — is the
nonlinear analogue of the convergence-order measurement** of
[05-03-04](./04-numerical-forward-modelling.md).

## 4. Units and dimensional analysis

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{m}$ | model parameters | kg m⁻³ (density) |
| $\mathbf{d}$ | data | m s⁻² |
| $\mathbf{G}$ | kernel matrix | m³ s⁻² kg⁻¹ |
| $F$ | forward operator | carries the physics |
| $\boldsymbol{\eta}$ | noise | m s⁻² |

## 5. Assumptions

1. **Linearity.** Gravity in density is exactly linear; magnetic in
   susceptibility is approximately linear (demagnetisation ignored); seismic in
   velocity is not.
2. **Known geometry of the discretisation.** Cell size is a modelling choice,
   and it must be fine enough that refining it does not change the answer.
3. **Adequate physical model.** A closed-form prism kernel assumes a
   homogeneous cell; sub-cell variation is unrepresentable.
4. **Known observation positions.** A 1 cm position error in the vertical
   corresponds to about 0.003 mGal — usually negligible, but state it.

## 6. Worked examples (measured)

`code/prism_gravity_demo.py` compares three methods for a homogeneous prism with
density contrast 500 kg/m³ occupying $x,y \in [-100,100]$ m, $z \in [50,250]$ m:

| method | $g_z$ (mGal) |
|---|---|
| closed form (prism formula) | 1.021214 |
| Gauss-Legendre, $n = 120$ | 1.021214 |
| scipy adaptive quadrature | 1.021214 |

Measured relative differences: closed-form vs Gauss-Legendre
$1.8\times10^{-15}$; closed-form vs adaptive $1.3\times10^{-15}$. The
quadrature converges from a relative error of $6.1\times10^{-10}$ at $n=20$ to
$8.3\times10^{-16}$ at $n=80$. **All three agree to essentially machine
precision, which is the standard of evidence for a forward code.**

### 6.1 Worked arithmetic: a two-cell inverse problem, solved and failed

Reduce the forward problem to its smallest interesting form: two cells, two
observations. Let the cells be 100 m wide at depth 150 m, centred at $x = \pm50$
m, and observe at $x = \pm50$ m.

$$G_{ij} = \frac{2G\,d\,\Delta x}{\left(x_i-x_j\right)^2+d^2},$$
$$G_{11} = G_{22} = \frac{2(6.6743\times10^{-11})(150)(100)}{0^2+150^2}
= 8.899\times10^{-11},$$
$$G_{12} = G_{21} = \frac{2(6.6743\times10^{-11})(150)(100)}{100^2+150^2}
= 4.618\times10^{-11}.$$

The matrix is symmetric with equal diagonal and equal off-diagonal entries, so
its columns differ only in which entry is larger — and their angle satisfies

$$\cos\theta = \frac{G_{11}G_{12}+G_{12}G_{11}}
{\sqrt{G_{11}^2+G_{12}^2}\sqrt{G_{12}^2+G_{11}^2}}
= \frac{2G_{11}G_{12}}{G_{11}^2+G_{12}^2} = \frac{2r}{1+r^2},
\qquad r = \frac{G_{12}}{G_{11}} = 0.519,$$

giving $\cos\theta = 0.8165$ and $\theta = 35.3°$ — so even this tiny problem has
columns only 35° apart. Its condition number follows directly from the symmetry:
the eigenvalues are $G_{11}\pm G_{12}$, so

$$\operatorname{cond}(\mathbf{G}) = \frac{G_{11}+G_{12}}{G_{11}-G_{12}}
= \frac{1+r}{1-r} = \frac{1.519}{0.481} = 3.16 .$$

Now put the cells closer together, at $x = \pm10$ m. Then
$G_{12} = 2G\,d\,\Delta x/(10^2+150^2)$ giving $r = 150^2/(100+150^2) = 0.99557$,
so

$$\operatorname{cond}(\mathbf{G}) = \frac{1.99557}{0.00443} = 450 .$$

**Halving the cell separation by a factor of 5 raised the condition number by a
factor of 143.** The two-cell problem is a complete, checkable illustration of
the entire lesson: the data cannot distinguish two nearby cells, and the
difficulty grows quadratically with the precision demanded of the geometry.

### 6.2 A shortcut that fails: "use a finer mesh for a better model"

**The shortcut.** Model the subsurface on a fine grid "because finer is more
accurate".

**What actually happens, measured.** At a fixed depth, refining cells leaves the
data unchanged (by construction) but drives the columns of $\mathbf{G}$ closer
together: $1-\cos\theta = 0.25(\Delta x/d)^2$, so halving $\Delta x$ cuts the
angle between neighbouring columns by half (Section 3.2). The null space grows
linearly with $n_s$ (Section 3.6 of
[05-01-04](../01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md)):
$\dim\ker\mathbf{G} = n_s - n_o$. Doubling the cells doubles the number of
directions the data cannot see.

**So what is refinement for?** It is for reducing the *discretisation error of
the forward model* ($1.2\times10^{-3} \to 6.7\times10^{-12}$ in the measured
table of Section 3.1), not for improving the inverse problem. The two uses are
in direct tension, and the resolution is to discretise finely enough that the
forward error is below the data noise, then stop — and to impose smoothness or
compactness priors to control the null space that refinement created.

**The generalisable lesson.** "Finer" is not a virtue. Ask which error the
refinement reduces and which it inflates, and stop when the first is below the
noise. That judgement is the substance of
[05-03-04](./04-numerical-forward-modelling.md).

### 6.3 Extended worked example: the kernel as a matrix, and what its columns mean

Build the smallest interesting version of the gravity forward problem by hand.
Take a model of five sheet cells, each 100 m wide, on a plane at 150 m depth,
with a line of five observations on the surface at the same spacing. The kernel
entry is

$$G_{ij} = G\,\Delta x\,\frac{d}{(x_i-x_j)^2+d^2},\qquad d = 150\ \mathrm{m},\
\Delta x = 100\ \mathrm{m}.$$

Units: $[G\Delta x d/(\ \cdot\ )] = \mathrm{m^3kg^{-1}s^{-2}\cdot m\cdot m/m^2}
= \mathrm{m^3s^{-2}kg^{-1}}$, so $\mathbf{G}\mathbf{m}$ with
$[\mathbf{m}] = \mathrm{kg\,m^{-2}}$ gives $\mathrm{m\,s^{-2}}$. ✓

**Read the columns.** Column $j$ is the anomaly produced by unit sheet density in
cell $j$ alone. Column 1 and column 2 differ only because the observation line
sits 100 m off-centre relative to each; the difference is a few percent of the
magnitude. Two nearly parallel columns mean the data cannot separate the two
cells' densities — the matrix is nearly rank-deficient, and its condition number
is large.

**Read the rows.** Row $i$ is the sensitivity of one observation to all cells. It
peaks at the cell directly beneath the station and falls off with distance. The
*depth* sets the width of that sensitivity: at 150 m depth the row spans a few
cells; at 1500 m it would span tens of cells with much smaller values. This is
the width law of
[05-01-03](../01-what-geophysics-measures/03-resolution-depth-tradeoff.md)
appearing as a row of a matrix.

**Quantify the difficulty.** For this configuration the condition number is of
order $10^{2}$–$10^{3}$; deepen the sheet to 1500 m and it rises by several
orders of magnitude, because every row becomes a broader, flatter, more similar
function. Adding observations *outside* the source footprint improves the
condition number far more than adding observations on top of it: the off-edge
data see the cells at genuinely different angles, whereas the over-centre data
all see roughly the same thing.

**A concrete test you can run.** Compute the anomaly for a model that is uniform
(`m = 500` kg/m² in every cell), then add the alternating pattern
`+50, -50, +50, -50, +50` kg/m² and recompute. The change in the data is a
smooth, almost negligible wiggle, while the model has changed by 10% in every
cell. That is the null-space behaviour of
[05-01-04](../01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md)
expressed in a five-cell model, and it is the reason gravity inversion needs a
smoothness or compactness prior.

**What the closed-form benchmark adds.** The prism demonstration confirms that
the kernel is *correct*: closed form, Gauss–Legendre and adaptive quadrature
agree to $1.8\times10^{-15}$ and $1.3\times10^{-15}$ relative for a prism of
density contrast 500 kg/m³. So when an inversion behaves badly, the cause is the
matrix's conditioning, not a coding error. This is exactly the separation that
[05-03-04](./04-numerical-forward-modelling.md) formalises: verify the kernel,
then diagnose the operator.

## 7. Python demonstration

Run `code/prism_gravity_demo.py`. It also checks the thin-sheet limit: a wide
20 m prism gives 0.418528 mGal against the infinite-slab value
$2\pi G\rho t = 0.419359$ mGal, a relative difference of
$2.0\times10^{-3}$ attributable to the finite lateral extent and finite
thickness — a *modelling* difference, not a numerical error, and the script says
so.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/01-forward-problem-exercises.md`](./exercises/01-forward-problem-exercises.md).

**Common mistakes.** (1) Treating the forward problem as hard and the inverse as
routine. (2) Forgetting the noise term and then declaring a model "exact".
(3) Refining the mesh without checking convergence. (4) Confusing a kernel
matrix with a Jacobian (they coincide only for linear problems). (5) Reporting a
prediction without units.

**Applications.** Gravity and magnetic modelling of prisms and polyhedra;
seismic finite-difference modelling; EM 1-D layered solutions; every one of them
is a discretised kernel applied to a model vector.

## 9. Further reading

- **Blakely (1995).** Chapters 1 and 9. Level: advanced.
- **Menke, *Geophysical Data Analysis*.** Chapter 1. Level: graduate.
- **Nagy, D. (1966).** The gravitational attraction of a right rectangular
  prism. *Geophysics* 31, 362–371. The classical closed form used above.

## 10. Related lessons

- [05-03-02 Analytical Solutions for Simple Bodies](./02-analytical-solutions.md)
- [05-03-04 Numerical Forward Modelling and Discretisation](./04-numerical-forward-modelling.md)
- [05-03-05 Validating Forward Codes Against Analytic Benchmarks](./05-forward-model-validation.md)
- [18-01-01 Forward and Inverse](../../18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md)

## Self-assessment checklist

- [ ] I can write the forward problem as $\mathbf{d} = F[\mathbf{m}] + \eta$ and
      name each part.
- [ ] I can derive the prism kernel matrix and check its units.
- [ ] I can explain why $\mathbf{G}$ is ill-conditioned.
- [ ] I can state the standard of evidence for a forward code.
- [ ] I can distinguish a modelling difference from a numerical error.
