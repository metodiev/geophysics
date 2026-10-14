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

## Extended worked example: the kernel as a matrix, and what its columns mean

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
