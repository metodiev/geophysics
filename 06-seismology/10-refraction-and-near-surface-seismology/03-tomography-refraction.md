---
id: 06-10-03
title: "Refraction Tomography and First-Arrival Inversion"
level: graduate
prereqs: ["06-10-02", "06-06-01"]
tags: [seismology, near-surface, refraction, tomography, inversion, coverage]
---

# Refraction Tomography and First-Arrival Inversion

> **All models and data in this module are SYNTHETIC.** The velocity grids, the
> source and receiver geometry, the inversion grid, the damping and the picking
> noise are chosen teaching values. The forward solver is a numerical eikonal
> solver on those synthetic models; no field data set is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the first-arrival forward problem as a path integral of slowness and
   **discretise** it into the matrix equation $\mathbf{A}\mathbf{s} = \mathbf{t}$.
2. **Derive** the Fréchet derivative
   $\partial t_i/\partial s_j = $ (ray length in cell $j$) from Fermat's
   principle, and **explain** why the inversion must be iterated.
3. **State** why a starting model containing a velocity gradient is required for
   diving rays to exist at all.
4. **Formulate** the damped least-squares update, and **interpret** the damping as
   a prior that pins cells the data do not reach.
5. **Quantify** coverage, and **show** that the cells changed least are the cells
   with the least coverage.
6. **Distinguish** what refraction tomography fixes from what it cannot: a
   lateral gradient or a dipping interface is recoverable, a low-velocity layer is
   not.
7. **Estimate** the depth of investigation from the spread length and the velocity
   contrast, and **state** the assumption that makes the estimate valid.

## Prerequisites

- [02 Delay-Time (Plus-Minus) Methods and Depth Estimation](02-plus-minus-method.md) —
  the layered interpretation that this lesson generalises, and its error
  propagation.
- [06-06-01 The Tomography Principle: Data as Path Integrals](../06-seismic-tomography/01-tomography-principle.md) —
  the same forward problem at crustal and mantle scales.
- [06-02-04 Ray Tracing in Laterally Varying Media](../02-ray-theory-and-travel-times/04-ray-tracing.md) —
  how the ray paths that appear in $\mathbf{A}$ are obtained.
- [03-10 ObsPy and Seismic Data](../../03-scientific-computing/10-obspy-and-seismic-data/README.md) —
  the picking machinery behind the right-hand side.

## 1. Intuition: why replace three numbers with a grid

Lesson 02 delivers a velocity and a depth profile, and it does so under two
assumptions that a real near-surface site violates constantly: a laterally
constant overburden velocity, and a single refractor with an infinite velocity
contrast below it. Both fail in the same way — the picks still arrive, and the
interpretation still returns numbers, but the numbers describe a model that does
not exist.

Refraction tomography keeps the same data — first-arrival times on a line — and
replaces the layered model with a grid of velocities. The forward problem becomes
"trace a ray through this grid and add up the time", the inverse problem becomes
"adjust the grid until the predicted times match the picks", and the price is that
the model is now described by many more unknowns than the data constrain. What
the method buys is real: a lateral velocity change, a dipping refractor, and a
velocity gradient are all representable. What it does not buy is information that
was never in the data, and this lesson is largely about the difference.

The honest difficulty is stated once and then measured: **first arrivals sample
only the fastest path from source to receiver, so a tomographic inversion of first
arrivals recovers a *fast* structure and is blind to anything a first arrival
cannot reach.** Every figure in Sections 5–8 is a version of that sentence.

## 2. Precise definitions

| Term | Meaning in this lesson |
|---|---|
| forward grid | nodes at which the numerical eikonal solver propagates times, $1\ \mathrm{m}$ here |
| inversion grid | cells over which slowness is constant, $5\ \mathrm{m}$ here ($20 \times 6 = 120$ unknowns) |
| starting model | the model the first iteration linearises about |
| residual | $\mathbf{t}_{\text{obs}} - \mathbf{t}_{\text{pred}}$ |
| coverage | number of ray segments passing through a cell |
| damping | the $\lambda$ in $(\mathbf{A}^{\mathsf T}\mathbf{A} + \lambda\mathbf{I})$ |
| box constraint | hard bounds on the admissible velocity |

The forward and inversion grids are deliberately different. The solver needs a
fine grid to reproduce curved and dipping paths; the inversion needs a coarse one
so that most cells are crossed by rays, because unknowns with no rays cannot be
estimated at all.

## 3. Derivations

### 3.1 The forward problem

In a smooth medium the first-arrival time from a source $S$ to a receiver $R$ is
the travel time along the ray that minimises it:

$$t_{SR} = \int_{\Gamma_{SR}} \frac{1}{v(\mathbf{x})}\,\mathrm{d}l
= \int_{\Gamma_{SR}} s(\mathbf{x})\,\mathrm{d}l,$$

with $s = 1/v$ the **slowness**. Discretising the model into cells $j$ of constant
slowness gives

$$t_i = \sum_j A_{ij} s_j, \qquad
A_{ij} = \text{length of ray } i \text{ inside cell } j
\quad (\text{units: m}).$$

The matrix $\mathbf{A}$ has units of length, the model is in
$\mathrm{s\,m^{-1}}$, and the product is a time — the dimensional check that
catches most coding errors in a travel-time inversion.

### 3.2 The Fréchet derivative, and why iteration is unavoidable

Perturb the model and ask how $t_i$ changes. Two things change: the slowness along
the path, and the path itself:

$$\delta t_i = \int_{\Gamma_i}\delta s\,\mathrm{d}l
+ \int_{\Gamma_i} s\,\delta(\mathrm{d}l).$$

**Fermat's principle kills the second term to first order.** The ray path is
stationary in travel time, so a first-order change in the path produces a
*second-order* change in $t_i$; the path perturbation is therefore not part of the
first-order derivative. Hence

$$\boxed{\;\frac{\partial t_i}{\partial s_j} = A_{ij},\;}$$

and the linearised inverse problem is $\mathbf{A}\,\delta\mathbf{s} =
\delta\mathbf{t}$ *around the current model*. The matrix $\mathbf{A}$ depends on
$\mathbf{s}$, so the system must be re-linearised and the rays re-traced after
every update. This is the standard Gauss–Newton structure, and the reason a
single-pass inversion of a strongly heterogeneous model is not merely inaccurate
but undefined.

### 3.3 Damped least squares

$\mathbf{A}$ has 120 columns in the demonstration and 126 rows, but its rank
depends on which cells contain rays. Solve instead the regularised problem

$$\min_{\delta\mathbf{s}}\;\left\|\mathbf{A}\,\delta\mathbf{s}
- \delta\mathbf{t}\right\|^{2} + \lambda\left\|\delta\mathbf{s}\right\|^{2},
\qquad
(\mathbf{A}^{\mathsf T}\mathbf{A} + \lambda\mathbf{I})\,\delta\mathbf{s}
= \mathbf{A}^{\mathsf T}\delta\mathbf{t}.$$

Two properties matter:

- **the damping is a prior.** The penalty is on the *perturbation*, so a cell with
  no rays ($\mathbf{A}$ column zero, hence a zero diagonal entry) is left at its
  starting value. "Unconstrained" in practice means "equal to the guess";
- **the damping is not free.** The resolution matrix
  $\mathbf{R} = (\mathbf{A}^{\mathsf T}\mathbf{A} +
  \lambda\mathbf{I})^{-1}\mathbf{A}^{\mathsf T}\mathbf{A}$
  equals the identity only when $\lambda = 0$ and the system is full rank. With
  $\lambda > 0$ each cell's estimate is a weighted average of its neighbours, so
  the recovered model is *smoother than the truth by construction* — which is what
  Section 5 measures as interface smearing.

The demonstration uses $\lambda = 15$, 12 Gauss–Newton iterations, LSQR for the
inner solve, a starting model with a vertical gradient from $400$ to
$1900\ \mathrm{m\,s^{-1}}$, and a hard box constraint
$150 \le v \le 4000\ \mathrm{m\,s^{-1}}$. The box constraint is not cosmetic:
without it the unconstrained step drives slowness in zero-coverage cells negative,
and a negative slowness is a negative edge weight, at which point the shortest-path
forward solver is no longer solving anything physical.

### 3.4 Why the starting model must have a gradient

A ray in a homogeneous medium is a straight line. In a layered model with a
horizontal interface the first arrival at moderate offset bends only at the
interface, and for a *smooth* model with no gradient a ray launched from the
surface has no reason to leave it: the shortest path is along the surface. The
starting model therefore needs a velocity that increases with depth, so that rays
dive, sample depth, and populate the sensitivity matrix. The demonstration states
this explicitly: *a vertical gradient is needed so that rays dive at all*. A
tomographic inversion whose first iteration produces a $\mathbf{A}$ with no
sensitivity below the first cell cannot recover structure below the first cell in
any later iteration either.

## 4. The reference case: two flat layers

The demonstration's first experiment is the case Lesson 01 solved in closed form,
inverted instead on a grid: 600 m/s above 10 m, 1800 m/s below, four sources at
0, 25, 50 and 75 m, receivers every 2 m out to 100 m, 126 source–receiver pairs,
and SYNTHETIC Gaussian picking noise of $\sigma = 0.5\ \mathrm{ms}$ (realised RMS
$0.4473\ \mathrm{ms}$).

| iteration | RMS residual (ms) |
|---|---|
| 1 | 15.0693 |
| 2 | 10.4561 |
| 3 | 3.9462 |
| 4 | 1.7796 |
| 5 | 1.3931 |
| 6 | 1.0981 |
| 7 | 1.1365 |
| 8 | 0.9290 |
| 9 | 0.8365 |
| 10 | 0.8043 |
| 11 | 0.7440 |
| 12 | 0.7208 |

Two readings. The residual falls by a factor of 21 in twelve iterations — the
linearisation is working — and it **stops at $0.7208\ \mathrm{ms}$, which is
$1.6\times$ the noise level rather than equal to it.** A residual above the noise
floor is the ordinary signature of model error: the damped inversion cannot
reproduce the sharp interface, so it cannot fit the data to the noise level.

Recovered row means, against truth:

| depth (m) | recovered (m/s) | true (m/s) |
|---|---|---|
| 0–5 | 534.7 | 600 |
| 5–10 | 860.2 | 600 |
| 10–15 | 1107.6 | 1800 |
| 15–20 | 1756.6 | 1800 |
| 20–25 | 1805.5 | 1800 |
| 25–30 | 1999.2 | 1800 |

The rows **where the rays actually run along the refractor** — 15–20 m and
20–25 m — come back at 1757 and 1806 m/s, within 2.4% of the truth. The apparent
failure in rows 0–2 is not a failure of resolution in depth: the cells are 5 m
wide and the interface sits exactly on a cell boundary, so within one cell width
the assignment of velocity to cell is genuinely ambiguous. Only $62.5\%$ of cells
contain at least one ray at all. And the deepest row, $1999.2\ \mathrm{m\,s^{-1}}$,
is 11% *too fast*: everything below the deepest ray is whatever the damping left
there, and the damping's job is not to be right.

## 5. The blind zone, measured

Now put a $250\ \mathrm{m\,s^{-1}}$ layer between 5 and 10 m, with
$600\ \mathrm{m\,s^{-1}}$ above it and $1800\ \mathrm{m\,s^{-1}}$ below. Rays cross
it, so the data are certainly affected: the layer delays every arrival by about
$7.83\ \mathrm{ms}$ on average — many times the $0.5\ \mathrm{ms}$ noise.

The inversion returns

| depth (m) | recovered (m/s) | true (m/s) |
|---|---|---|
| 0–5 | 559.0 | 600 |
| 5–10 | **728.8** | **250** |
| 10–15 | 851.4 | 1800 |
| 15–20 | 1174.7 | 1800 |
| 20–25 | 1592.0 | 1800 |
| 25–30 | 1821.7 | 1800 |

Row 5–10 m comes back at $728.8\ \mathrm{m\,s^{-1}}$ where the truth is
$250\ \mathrm{m\,s^{-1}}$ — a factor of $2.92$. The layer is not mis-resolved; it is
**replaced by more of the layer above it**, a substitution that fits the observed
delay almost as well because delay time depends on thickness/velocity and a thick
fast layer can mimic a thin slow one. The two-layer equivalent depth computed from
the exact intercept time makes the same mistake with one number:
$17.60\ \mathrm{m}$ instead of the true $10.0\ \mathrm{m}$ to the top of the
$1800\ \mathrm{m\,s^{-1}}$ layer, a $76\%$ error.

This is the blind zone of Lesson 01, unchanged by the upgrade from three unknowns
to 120. Tomography refines the refractor's depth; it does not make the low-velocity
layer invertible, because the *data* do not contain it as a separate arrival.

## 6. A velocity inversion: the layer no ray enters

Reverse the layering — $1800\ \mathrm{m\,s^{-1}}$ in the top 5 m over
$400\ \mathrm{m\,s^{-1}}$ below. Now measure the ray coverage of the *true* model:

| depth (m) | mean ray segments per cell | cells with no ray |
|---|---|---|
| 0–5 | 51.8 | 0 of 20 |
| 5–10 | 0.0 | 20 of 20 |
| 10–15 | 0.0 | 20 of 20 |
| 15–20 | 0.0 | 20 of 20 |
| 20–25 | 0.0 | 20 of 20 |
| 25–30 | 0.0 | 20 of 20 |

Not one ray enters the slow layer. The first arrival is always the direct wave in
the fast surface layer, so the deeper cells have zero coverage and zero columns of
$\mathbf{A}$. The inversion's residual sequence and final coverage say the same
thing quantitatively: the RMS residual falls from $39.0404\ \mathrm{ms}$ to
$1.4543\ \mathrm{ms}$ and then *stops*, because the best possible fit of a model
whose rays stay in the top layer to data generated by such a model is the
direct-wave branch itself. Final coverage: $51.7\%$ of cells. **The inversion
cannot report a slow layer beneath a fast one, and the data cannot even ask the
question** — the residual floor is not a numerical artefact but the statement that
the model class and the data agree.

The remedy is a different wave: a surface-wave method that senses the slow material
through its dispersion (Lesson 04), or a borehole that enters it.

## 7. Depth of investigation against spread length

The two-layer crossover relation from Lesson 01,
$x_c = 2h\sqrt{(v_2+v_1)/(v_2-v_1)}$, inverts to the maximum depth sampled by a
spread of length $L$ if the crossover is placed at the end of the spread:

$$h_{\max} = \frac{L}{2}\sqrt{\frac{v_2-v_1}{v_2+v_1}}.$$

The demonstration compares this estimate with the deepest row that the inversion's
rays actually reached with mean coverage above one half:

| $L$ (m) | $h_{\max}$ formula (m) | deepest row with mean coverage $> 0.5$ |
|---|---|---|
| 30 | 10.61 | 5.0 |
| 50 | 17.68 | 20.0 |
| 80 | 28.28 | 30.0 |
| 100 | 35.36 | 30.0 |

The formula is a *two-layer* estimate and the model here is not one (the starting
model has a gradient plus a fast surface layer), so the two columns agree only in
order of magnitude. That discrepancy is the honest content of the table: a design
formula derived from a layered model constrains a tomographic survey only to within
a factor of about two, while the robust statement — **the deepest sampled row grows
with the spread, and everything below it is unconstrained regardless of the
algorithm** — holds exactly.

## 8. Coverage is the whole story

Rank the 120 cells of Section 4 by the size of the change the inversion made, and
split the ranking into the most-changed twenty and the least-changed twenty:

| group | mean ray segments per cell |
|---|---|
| 20 most-changed cells | 23.00 |
| 20 least-changed cells | 1.35 |

The update is proportional to ray coverage, which is what a damped least-squares
step must do, and it means that **a tomographic image without its coverage map is
half a result.** Two inversions of the same data with different damping produce
different pictures in low-coverage cells and identical pictures where coverage is
good; only the coverage tells you which pixels to believe.

## 9. Assumptions and regime of validity

1. **First arrivals only.** Guided waves, reflections, surface waves and
   diffractions contain structure that first arrivals cannot see, and ignoring them
   is what makes the blind zone permanent (Section 5).
2. **The high-frequency (ray) approximation.** Cells smaller than about a quarter
   wavelength do not produce a distinct arrival; the inversion will still fill them
   with numbers (Lesson 06 gives the wavelengths).
3. **An isotropic, smoothly varying medium at the inversion scale.** Sharp
   interfaces are represented only through smearing over one to two cells, which is
   why the interface in Section 4 is spread over 5–15 m.
4. **The eikonal forward solver is adequate.** Its error is angular quantisation and
   it is a *first-arrival* solver: it returns the fastest route and never a later,
   slower arrival (Lesson 01 verifies the quantisation error directly).
5. **The damping is a statement about the answer.** $\lambda = 15$ was chosen, not
   derived; a different value gives a different model with a nearly identical
   residual, which is another face of non-uniqueness.
6. **Noise is Gaussian, additive and independent between picks.** Real pick errors
   are correlated between adjacent receivers, which inflates the apparent resolution
   of the inversion.
7. **Coverage is reported and interpreted.** Without it, a recovered model is an
   assertion about where the rays went, and the damping determines the answer in the
   cells where they did not go.

## Mastery checkpoint

Use the demonstration's geometry (four sources at 0, 25, 50 and 75 m; receivers
every 2 m to 100 m; 5 m cubic cells to 30 m depth).

**(a)** Write the forward problem for one source–receiver pair as a path integral,
and state the units of $\mathbf{A}$, $\mathbf{s}$ and $\mathbf{t}$.
**(b)** Explain in two sentences why Fermat's principle makes
$\partial t_i/\partial s_j$ equal to the ray length in cell $j$ rather than
something involving the path perturbation.
**(c)** A cell has zero ray coverage. What value does the damped inversion return
for it, and why is that not an estimate of the ground?
**(d)** For $v_1 = 1000\ \mathrm{m\,s^{-1}}$, $v_2 = 3000\ \mathrm{m\,s^{-1}}$,
what spread length is needed to sample a target $25\ \mathrm{m}$ deep using
$h_{\max} = (L/2)\sqrt{(v_2-v_1)/(v_2+v_1)}$, and what is the assumption that makes
this a *lower* bound on the true requirement?
**(e)** The reference inversion stops at $0.7208\ \mathrm{ms}$ RMS against a noise
level of $0.4473\ \mathrm{ms}$. Give two distinct reasons the residual cannot reach
the noise level, one from the damping and one from the grid.

A worked version is in the
[solutions](exercises/03-tomography-refraction-solutions.md).

## Common pitfalls

1. **Reporting the model without the coverage.** The two are one result; the cells
   the inversion changed least are the cells with the fewest rays (23.00 versus
   1.35 segments in Section 8).
2. **Reading the smeared interface as a gradational one.** A 5 m interface smeared
   over 10 m is an artefact of the cell size and the damping, not a measurement of a
   transition zone.
3. **Trusting a falling residual as convergence to the truth.** The residual stops
   above the noise floor because of model error, and a *lower* residual can be
   achieved by over-fitting correlated picks.
4. **Starting from a homogeneous model.** Without a gradient, rays do not dive, the
   sensitivity matrix has no deep entries, and no later iteration can repair it.
5. **Believing that more unknowns means more resolution.** The 120-cell model has
   the same 126 travel times as the layered model has parameters in the dozens; the
   extra detail is damping, not information.
6. **Expecting first arrivals to find a low-velocity layer.** They cannot, and the
   residual will not warn you.
7. **Choosing $\lambda$ by taste.** State it, and state what the answer looks like at
   a second value.

## Related modules

- [02 Delay-Time (Plus-Minus) Methods and Depth Estimation](02-plus-minus-method.md) —
  the layered interpretation whose failure motivates the grid.
- [01 Refraction Survey Geometry and Travel-Time Interpretation](01-refraction-basics.md) —
  the blind zone, the crossover and the spread design used in Section 7.
- [06-06-02 Travel-Time Tomography: Parametrisation and Inversion](../06-seismic-tomography/02-travel-time-tomography.md) —
  the same machinery at lithospheric scale, where the same coverage problem appears
  as a poorly sampled mantle.
- [06-06-03 Resolution, Null Space and Model Covariance](../06-seismic-tomography/03-resolution-and-nullspace.md) —
  the formal treatment of $\mathbf{R}$, the null space and model covariance.
- [18-inverse-problems](../../18-inverse-problems/README.md) — regularisation, the
  trade-off curve and the interpretation of a regularised solution.

## Code and exercises

The demonstration is
[`code/refraction_tomography_demo.py`](code/refraction_tomography_demo.py):

```bash
cd 06-seismology/10-refraction-and-near-surface-seismology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python refraction_tomography_demo.py
```

It prints every number quoted here, with units, and exits 0.

Exercises:
[`exercises/03-tomography-refraction-exercises.md`](exercises/03-tomography-refraction-exercises.md);
solutions:
[`exercises/03-tomography-refraction-solutions.md`](exercises/03-tomography-refraction-solutions.md).
Module overview: [`README.md`](README.md).
