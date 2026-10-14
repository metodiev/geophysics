---
id: 06-06-02
title: "Travel-Time Tomography: Parametrisation and Inversion"
level: doctoral
prereqs: ["06-06-01", "18-02-02"]
tags: [seismology, tomography, parametrisation, regularisation, iterative-solvers]
---

# Travel-Time Tomography: Parametrisation and Inversion

All models and data in this module are **SYNTHETIC**. Every number below is
printed by `code/travel_time_tomography_demo.py`, whose setup is a
$16\ \mathrm{km}\times5.5\ \mathrm{km}$ cross-hole survey in a homogeneous
$3000\ \mathrm{m\,s^{-1}}$ reference medium with 10 sources and 14 receivers
(140 rays).

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** the three decisions that make up a parametrisation — basis,
   cell size and regularity — and **state** what each one forbids in the answer.
2. **Build** the Jacobian for a cell basis and for a bilinear node basis, and
   **measure** the sparsity and conditioning difference between them.
3. **Solve** a damped least-squares problem both directly and with
   conjugate-gradient least squares, and **compare** them in matrix-vector
   products and in wall time.
4. **Demonstrate** that refining the grid past the resolution of the data
   increases the model error while decreasing the data misfit, and **explain**
   the mechanism with the null-space fraction.
5. **Choose** a regularisation operator and **quantify** what it does to the
   model error and to the roughness of the answer.
6. **Measure** the two sources of nonlinearity — the parametrisation and the ray
   paths — and **decide** how many iterations are needed for a stated accuracy.

## Prerequisites

- [01 The Tomography Principle](01-tomography-principle.md) — the path integral,
  the Jacobian and the null space.
- [18-02-02 Underdetermined Problems](../../18-inverse-problems/02-linear-inverse-problems/02-underdetermined.md) —
  minimum-norm solutions and why they are a choice.
- [03-02-05 Linear Algebra with NumPy](../../03-scientific-computing/02-numpy/05-linear-algebra-numpy.md) —
  the decompositions used here.

## 1. A parametrisation is three decisions, not one

Tomographic papers describe the model as "a $16\times12$ grid". That single
phrase hides three separate choices, each of which changes the answer:

1. **The basis.** Piecewise-constant cells, or linear/bilinear interpolation
   between nodes, or splines, or spherical harmonics. The basis fixes what a
   model *can* look like: a cell basis cannot represent a gradient inside a cell,
   a node basis cannot represent a discontinuity.
2. **The support.** Cell size, node spacing, layer thickness. This sets the
   smallest structure that can exist in the answer and, less obviously, how many
   parameters the null space contains.
3. **The regularisation.** What is penalised — amplitude, roughness, distance
   from a prior — and by how much.

Only the third is usually reported. The demonstration measures the first two.

## 2. Two bases for the same rays

For each ray $i$ and each basis function $\phi_j$, the Jacobian entry is

$$
G_{ij} \;=\; \int_{\Gamma_i} \phi_j(\mathbf{x}(s))\,\mathrm{d}s
\tag{1}
$$

divided by the reference velocity, because the datum is a *time*. With a
piecewise-constant cell basis, $\phi_j$ is an indicator and the entry is just the
ray length inside one cell. With a bilinear node basis, each sample point on the
ray contributes to four nodes, so the matrix is about four times denser.

Measured on the same 140 rays:

| | cells $16\times12$ | nodes $17\times13$ |
|---|---|---|
| parameters | 192 | 221 |
| non-zeros in $G$ | 2819 (10.49 per cent) | 5921 (19.14 per cent) |
| non-zeros per ray | 20.1 (max 27) | 42.3 (max 56) |
| rank | 136 of 140 | 140 of 140 |
| condition number | $2.887\times10^{2}$ | $7.054\times10^{3}$ |

The node basis is smoother and better conditioned in rank terms, but its
condition number is 24 times worse: neighbouring parameters are almost the same
function, so the inversion has to disentangle them with data that cannot. Both
matrices describe the same physics; the choice is a statement about what the
Earth is allowed to look like, and it must be stated.

## 3. Solving it: direct or iterative?

Damped least squares solves

$$
\min_{\mathbf{m}} \lVert G\mathbf{m} - \mathbf{d}\rVert_2^2
+ \lambda^2 \lVert L\mathbf{m}\rVert_2^2 ,
\tag{2}
$$

which for $L = I$ is the normal-equation system
$(G^{\mathsf T}G + \lambda^2 I)\mathbf{m} = G^{\mathsf T}\mathbf{d}$. On a
$192$-parameter problem the direct solve costs milliseconds. On a real problem
$G$ is sparse, enormous, and never formed: conjugate-gradient least squares
(CGLS) applies $G$ and $G^{\mathsf T}$ and never factorises anything.

Measured on the demonstration problem (140 data, 192 parameters,
$\lambda = 3\times10^{-2}\lVert G\rVert$):

| CGLS iterations | matrix-vector products | misfit (s) | wall time (s) | $\lVert\mathbf{m}-\mathbf{m}_{\text{direct}}\rVert$ |
|---|---|---|---|---|
| 2 | 4 | $6.7792\times10^{-3}$ | 0.00003 | $3.28\times10^{-3}$ |
| 5 | 10 | $2.1686\times10^{-3}$ | 0.00005 | $9.52\times10^{-4}$ |
| 10 | 20 | $1.4846\times10^{-3}$ | 0.00009 | $1.65\times10^{-4}$ |
| 20 | 40 | $1.4694\times10^{-3}$ | 0.00017 | $6.30\times10^{-6}$ |
| 50 | 100 | $1.4694\times10^{-3}$ | 0.00043 | $2.12\times10^{-10}$ |

The direct solve reached misfit $1.4694\times10^{-3}\ \mathrm{s}$ in
$0.0002\ \mathrm{s}$; CGLS reached the same answer to five significant figures
in 20 iterations. The practical lesson is that the *iteration count is now part
of the model definition*: an inversion stopped at 5 iterations is a different
model from one stopped at 50, and the stopping rule has to be reported exactly
as the damping is.

## 4. The grid is a hypothesis

Fix the data (140 rays, one smooth 5 per cent anomaly, noise
$\sigma = 5\ \mathrm{ms}$, 40 noise realisations). For each grid, choose the
damping that just reaches the statistically acceptable misfit
$\sqrt{N}\sigma = 5.9161\times10^{-2}\ \mathrm{s}$, and measure the model error.

| grid | parameters | data/param | $\lambda/\lVert G\rVert$ | misfit (s) | model error | row-space error | null fraction |
|---|---|---|---|---|---|---|---|
| $8\times6$ | 48 | 2.92 | $5.61\times10^{-1}$ | $5.638\times10^{-2}$ | $1.6292\times10^{-2}$ | $7.171\times10^{-3}$ | 0.519 |
| $16\times12$ | 192 | 0.73 | $8.41\times10^{-1}$ | $5.561\times10^{-2}$ | $1.8668\times10^{-2}$ | $1.135\times10^{-2}$ | 0.526 |
| $24\times18$ | 432 | 0.32 | $8.41\times10^{-1}$ | $5.564\times10^{-2}$ | $1.8991\times10^{-2}$ | $1.115\times10^{-2}$ | 0.546 |
| $32\times24$ | 768 | 0.18 | $8.91\times10^{-1}$ | $5.884\times10^{-2}$ | $1.9810\times10^{-2}$ | $1.083\times10^{-2}$ | 0.589 |

The model error is rms$(\hat v/v_0 - v_{\text{true}}/v_0)$; the true anomaly has
rms $0.028$. Three things are worth reading off this table.

- **Every row fits the data equally well.** The misfit cannot choose between them.
- **Refinement makes the image worse**, monotonically, from $1.63\times10^{-2}$ to
  $1.98\times10^{-2}$.
- **The mechanism is the null space**, whose share of the true anomaly grows from
  0.519 to 0.589 as cells are added that no ray constrains. The part of the
  anomaly that *is* recoverable (the row-space error) does not blow up: it stays
  between $7\times10^{-3}$ and $1.1\times10^{-2}$.

A finer grid is therefore not a better grid. The honest choice is the coarsest
grid that does not visibly bias the answer, and the sensitivity of the answer to
the grid must be shown — with a known-model test, not asserted.

### Worked example — why the data cannot choose the grid

Compare the $16\times12$ and $32\times24$ rows of the table. The data fit
improves from $5.561\times10^{-2}$ to $5.884\times10^{-2}$ s — that is, it gets
*0.6 per cent worse*, and both values are statistically identical given the
stated 5 ms noise — while the model error grows from $1.8668\times10^{-2}$ to
$1.9810\times10^{-2}$, i.e. **6.1 per cent worse**. The null fraction rises from
0.526 to 0.589 in the same step. So the finer grid costs 6 per cent of model
accuracy and buys 0.6 per cent of misfit, and the misfit is the only quantity an
automated parameter-choice rule can see. A factor-of-ten mismatch between the two
sensitivities is the quantitative reason that "the inversion converged" is not an
argument about the model.


## 5. What "regularisation" does to the answer

Two operators, tuned so that both reach the same data misfit
$\sqrt{N}\sigma$:

| operator | $\lambda/\lVert G\rVert$ | misfit (s) | model error | $\lVert L\mathbf{m}\rVert$ (1/s) | $\lVert L\mathbf{m}\rVert/\lVert L\mathbf{m}_{\text{true}}\rVert$ |
|---|---|---|---|---|---|
| identity | $2.384\times10^{-1}$ | $5.8457\times10^{-2}$ | $1.9277\times10^{-2}$ | $9.833\times10^{-2}$ | 1.257 |
| first differences (+5 per cent identity) | $4.317\times10^{0}$ | $5.7113\times10^{-2}$ | $1.8008\times10^{-2}$ | $9.650\times10^{-4}$ | 0.012 |

Matched by data misfit, the smoother answer is both closer to the truth
($1.80\times10^{-2}$ against $1.93\times10^{-2}$) and 100 times less rough than
the truth, while the minimum-norm answer is rougher than the truth. Sweeping the
roughness damping from $10^{-3}$ to $3\times10^{-1}$ moves the model error from
$1.68\times10^{-2}$ to $1.49\times10^{-2}$ and the roughness ratio from 3.23 to
0.17: the operator is a prior statement about the Earth, and it changes the
numbers in the image by tens of per cent.

A practical detail that is easy to get wrong: a pure first-difference operator
does **not** penalise a constant model, because constants are in its null space.
In the demonstration the augmented operator (differences stacked with 5 per cent
of the identity) had to be used before the data misfit could be made to rise at
all as damping increased. A pure difference operator plus unconstrained data is
a recipe for an arbitrary mean level in the image.

## 6. Two nonlinearities, measured

### 6.1 Ray paths: Fermat makes the error second order

Take a 15.6 km ray, force its path through a mid-point displaced by $d$ in $z$,
and integrate the exact travel time through the 2-D model:

| $d$ (km) | $T(d) - T(0)$ (ms) |
|---|---|
| 0.25 | $+2.595$ |
| 0.50 | $+11.315$ |
| 1.00 | $+45.101$ |

Doubling the displacement multiplies the penalty by 4.36 and then by 4.00: the
travel-time penalty is quadratic in the path error. The minimum over $d$ sits at
$d = -0.070\ \mathrm{km}$, i.e. the true ray is 70 m away from the straight line,
and using the straight line costs only **$0.486$ ms on $5.071$ s**. That is why
the fixed-path Jacobian is a good approximation even when the rays bend, and why
the neglected path term is not the thing that limits travel-time tomography.

### 6.2 Parametrisation: what iteration buys

Parametrise velocity as $v = v_0(1+p)$. The datum is
$T - T_0 = -\int (\mathrm{d}s/v_0)\,p/(1+p)$, which is nonlinear in $p$.
Starting from $p = 0$ and re-linearising about the current estimate:

| iteration | data residual rms (s) | error vs truth | error vs recoverable part |
|---|---|---|---|
| 0 | $1.2607\times10^{-1}$ | $2.8157\times10^{-2}$ | $2.3506\times10^{-2}$ |
| 1 | $2.9922\times10^{-3}$ | $1.4842\times10^{-2}$ | $7.7718\times10^{-4}$ |
| 2 | $2.1312\times10^{-6}$ | $1.4822\times10^{-2}$ | $7.1833\times10^{-4}$ |
| 3 | $2.1591\times10^{-7}$ | $1.4822\times10^{-2}$ | $7.1760\times10^{-4}$ |
| 4 | $5.9279\times10^{-8}$ | $1.4822\times10^{-2}$ | $7.1751\times10^{-4}$ |

One step recovers the recoverable part of the anomaly to 3.3 per cent of its rms
($7.77\times10^{-4}$ against $2.35\times10^{-2}$); the second step multiplies the
data residual by $1/1400$. Everything left after that is the part of the anomaly
the ray geometry cannot see. **The residual after convergence measures
resolution, not iteration quality.**

## 7. Assumptions and regime of validity

1. **Straight rays** in the reference medium. Exactly right only for a
   homogeneous reference; the error introduced is second order (section 6.1).
2. **Small perturbations**, $\lvert p\rvert \ll 1$. Measured: 8 per cent
   anomalies give a 6 per cent error on the datum (lesson 06-06-01) and require
   two iterations.
3. **A known reference velocity.** Section 4 shows that refinement without a
   reference is not refinement; the reference and the grid together define what
   "the anomaly" means.
4. **Gaussian, independent, zero-mean travel-time errors** with known $\sigma$.
   Real picks have correlated errors (picking operator, event location, station
   corrections) which inflate the effective $\sigma$ and bias the model.
5. **Consistent acquisition.** Sources and receivers are assumed known and
   correctly timed; a 5 ms timing error is a systematic datum error at the same
   scale as the noise used here.

## 8. Demonstration

[`code/travel_time_tomography_demo.py`](code/travel_time_tomography_demo.py)
produces every table above: the two bases, the two solvers, the grid sweep with
its null-space fraction, the two regularisation operators, the Fermat
measurement and the Newton iteration. Exercises and worked solutions:
[`exercises/02-travel-time-tomography-exercises.md`](exercises/02-travel-time-tomography-exercises.md)
and
[`exercises/02-travel-time-tomography-solutions.md`](exercises/02-travel-time-tomography-solutions.md).

## Mastery checkpoint

> A 200-parameter cell model is inverted from 300 travel times with 5 ms noise.
> The $20\times10$ grid gives a model error of $1.9\times10^{-2}$; the
> $40\times20$ grid gives $2.4\times10^{-2}$ with a smaller misfit. **(a)** Give
> the most likely explanation in one sentence. **(b)** Name the diagnostic that
> confirms it. **(c)** State the damping, the misfit and the grid that must
> accompany a published version of this image. **(d)** Estimate the number of
> re-linearisation steps needed if the anomalies are 15 per cent, and justify it
> from the $p^2$ scaling.

## Common pitfalls

1. **Refining the grid to "get more detail".** Measured: it adds null-space
   parameters and worsens the image.
2. **Reporting a misfit without the noise level.** A misfit of $5.6\times10^{-2}$
   s is excellent for 5 ms noise on 140 data and terrible for 0.5 ms noise.
3. **Using a pure first-difference operator.** Constants are unpenalised, so the
   mean of the model is set by noise.
4. **Stopping an iterative solver by iteration count without saying so.** The
   iteration count is part of the model.
5. **Iterating until the residual is "small".** After convergence the residual
   is dominated by damping bias and by the null space, not by unmodelled
   nonlinearity.
6. **Believing that Fermat's principle excuses everything.** It excuses path
   errors at second order; it does not excuse a wrong reference model, which
   changes the datum at first order.

## Related modules

- [06-06-01 The Tomography Principle](01-tomography-principle.md).
- [06-06-03 Resolution, Null Space and Model Covariance](03-resolution-and-nullspace.md) —
  the quantification of the null-space effects seen here.
- [18-03 Regularisation and Stabilisation](../../18-inverse-problems/03-regularization/README.md) —
  the general theory of the operators used in section 5.
- [18-04 Nonlinear Inversion and Optimisation](../../18-inverse-problems/04-nonlinear-inversion/README.md) —
  the iteration of section 6.2 in general form.
- [06-13 Planetary and Exploration Seismology](../13-planetary-and-exploration-seismology/README.md) —
  tomographic problems with far fewer rays than parameters.
