---
id: 06-06-05
title: "The Adjoint Method for Efficient Sensitivity Computation"
level: research
prereqs: ["06-06-04", "18-04-02"]
tags: [seismology, adjoint, sensitivity-kernels, gradient, finite-frequency]
---

# The Adjoint Method for Efficient Sensitivity Computation

All models and data in this module are **SYNTHETIC**. Every number below is
printed by `code/adjoint_methods_demo.py`: 300 nodes at 10 m spacing, a Ricker
source of 18 Hz injected at node 2 (20 m below the free surface),
$\Delta t = 2.857$ ms, a starting model of 2000 / 2400 / 2800 m/s with
interfaces at 0.8 and 2.0 km, a target model 150 m deeper and up to
100 m/s faster, and a least-squares misfit over 0.45-1.30 s.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the adjoint equation from a Lagrangian for a time-stepping scheme,
   and **show** that the adjoint field is obtained by integrating the same
   scheme backwards in time with the data residual as a source.
2. **Assemble** the discrete wave operator as a matrix and **explain** why the
   adjoint must be the exact transpose of the scheme that produced the data.
3. **Verify** an adjoint implementation by the dot-product test and by
   comparison with finite differences, and **state** what each test does and does
   not establish.
4. **Compute** the cost of a gradient by both routes and **explain** why the
   adjoint cost is independent of the number of parameters.
5. **Interpret** a sensitivity kernel, **measure** its width against the
   frequency band, and **state** in what sense it is not a ray.
6. **Judge** how far from the current model a linearised gradient can be
   trusted, using measured curvature.

## Prerequisites

- [04 Full-Waveform Inversion](04-full-waveform-inversion.md) — the misfit whose
  gradient this lesson computes.
- [18-04-02 Gradient and Newton Methods](../../18-inverse-problems/04-nonlinear-inversion/02-gradient-and-newton.md) —
  what a gradient is used for.
- [03-02-05 Linear Algebra with NumPy](../../03-scientific-computing/02-numpy/05-linear-algebra-numpy.md) —
  matrix transposes and adjoints.

## 1. Why the brute-force gradient is unusable

The misfit of lesson 06-06-04 is

$$
J(\mathbf{m}) = \tfrac{1}{2}\sum_r\int\bigl[u_r(t;\mathbf{m})-d_r(t)\bigr]^2\,\mathrm{d}t .
\tag{1}
$$

The definition of $\partial J/\partial m_i$ is a finite difference, and in the
demonstration it costs two forward solves per parameter:

| | value |
|---|---|
| parameters sampled | 12 of 300 |
| forward solves | 24 |
| sampled gradient values ($\mathrm{s^{-2}}$) | $+0.000$, $-1.08\times10^{-3}$, $-1.08\times10^{-3}$, $+1.00$, $\dots$ |

For a real model — $10^6$ to $10^8$ parameters — this is not a slow method, it is
an impossible one. Note carefully what the finite difference is *not*: it is not
wrong. It is the reference against which an adjoint implementation must be
checked.

## 2. The adjoint, derived once

Write the scheme of lesson 06-06-04 as a linear recursion in the state vector
$\mathbf{u}^n$,

$$
\mathbf{u}^{n+1} = A(\boldsymbol\theta)\,\mathbf{u}^{n} - B\,\mathbf{u}^{n-1}
+ \mathbf{s}^n ,
\qquad B = P D ,
\tag{2}
$$

where $\boldsymbol\theta_i = (c_i\Delta t/\Delta x)^2$ are the parameters, $D$ is
the boundary damping and $P$ zeroes the free-surface row. Introduce the adjoint
field $\boldsymbol\lambda^n = \partial J/\partial \mathbf{u}^n$. Differentiating
the Lagrangian with respect to $\mathbf{u}^k$ and requiring it to vanish:

$$
\boldsymbol\lambda^{k} = A^{\mathsf T}\boldsymbol\lambda^{k+1}
- B^{\mathsf T}\boldsymbol\lambda^{k+2} + \mathbf{r}^k ,
\qquad \mathbf{r}^k = \mathbf{u}^k - \mathbf{d}^k \ \text{at the receivers}.
\tag{3}
$$

Equation (3) is the *same* stencil, run backwards in time, with the data residual
injected where the receiver is. The gradient then follows from
$\partial \mathbf{u}^{n+1}/\partial\theta_i = B\,\partial A/\partial\theta_i\,\mathbf{u}^n$:

$$
\boxed{\;
\frac{\partial J}{\partial\theta_i}
= \sum_n \bigl(B^{\mathsf T}\boldsymbol\lambda^{n+1}\bigr)_i
\bigl(\Delta\mathbf{u}^n\bigr)_i ,
\qquad
(\Delta\mathbf{u})_i = u_{i+1} - 2u_i + u_{i-1} .
\;} \tag{4}
$$

Two properties of (4) deserve emphasis.

- **The cost is two propagations**, one forward (storing the field) and one
  backward, whatever the number of parameters.
- **The transpose must be exact.** $B^{\mathsf T}$, $A^{\mathsf T}$, the damping
  factors, the free-surface row and the source insertion all have to match the
  scheme that produced the data. If they do not, the gradient is simply wrong,
  and it is wrong in a way that no amount of line searching will fix.

## 3. Verifying the adjoint

Two tests, and they are different tests.

**The dot-product test.** For a random model perturbation $\delta\mathbf{m}$ and
a random data-space vector $\mathbf{w}$, the identity
$\langle J\delta\mathbf{m}, \mathbf{w}\rangle
= \langle \delta\mathbf{m}, J^{\mathsf T}\mathbf{w}\rangle$ must hold, where
$J$ here is the *linearised forward operator* applied to a perturbation. It
compares two different numerical experiments and needs no true model. Measured:

| quantity | value |
|---|---|
| $\langle J\delta\mathbf{m},\mathbf{w}\rangle$ | $+6.07460951\times10^{-1}$ |
| $\langle \delta\mathbf{m}, J^{\mathsf T}\mathbf{w}\rangle$ | $+6.07460951\times10^{-1}$ |
| ratio | $1.0000000000$ |

**The gradient test.** Compare (4) with central differences at the sampled
parameters:

| quantity | value |
|---|---|
| median relative difference | $5.584\times10^{-10}$ |
| worst relative difference | $2.361\times10^{-6}$ |
| cosine similarity | $1.0000000000$ |
| matrix form of the scheme against the stencil form | $7.15\times10^{-15}$ relative amplitude |

The dot-product test establishes that the adjoint is the transpose of the
operator; the gradient test establishes that the misfit derivative is right. An
implementation can pass one and fail the other — in this demonstration an earlier
version passed neither until the free-surface row of the operator was included in
the gradient accumulation, which is the kind of detail that these tests exist to
catch. Reporting "we use the adjoint method" without reporting such a test is
reporting an intention.

## 4. Cost

| parameters | brute-force solves | adjoint solves | speed-up |
|---|---|---|---|
| 4 | 8 | 2 | $4\times$ |
| 16 | 32 | 2 | $16\times$ |
| 64 | 128 | 2 | $64\times$ |
| 256 | 512 | 2 | $256\times$ |

The demonstration also measures the real cost on this problem: the adjoint
gradient took **0.02 s**, the same order as one forward solve. The ratio is the
number of parameters divided by two, and it is the only reason operational
waveform inversion exists.

### Worked example — sizing a gradient computation

Take a realistic global problem: $n = 5\times10^{5}$ parameters (say a
$200\times100$ by 25-layer model) and 200 sources, each requiring one forward
solve per evaluation, at 1 s per solve on a cluster node.

- **Finite differences:** two solves per parameter,
  $2n = 10^{6}$ solves, i.e. $10^{6}$ s $\approx$ **11.6 days** for a single
  gradient — and the same again for the next iteration.
- **Adjoint:** two solves per source, $2\times200 = 400$ solves, i.e. **400 s**
  — under seven minutes, independent of $n$.

The speed-up is $n/2 = 2.5\times10^{5}$. This is not a constant-factor
improvement in an algorithm: it is the difference between an infeasible
computation and a routine one, and it is the reason the adjoint method, not finite
differences, defines what a waveform inversion can iterate on. Note also the two
costs that the count above ignores: the backward pass needs the forward field
history (40 TB in the estimate of exercise 8) and the number of *iterations* is
set by the reliability limit of §6, not by the gradient cost.


## 5. The kernel is not a ray

Take a *travel-time* measurement: the misfit
$J = \tfrac12 \Delta t^2$ where $\Delta t$ is the lag that best aligns synthetic
and observed traces in a window. Its derivative with respect to the model is a
**sensitivity kernel** $K(\mathbf{x}) = \partial J/\partial m(\mathbf{x})$: the
answer to "where does this measurement look?". Measured on the demonstration
problem, band-passing both traces:

| band (Hz) | kernel width (m) | local wavelength (m) | width / wavelength |
|---|---|---|---|
| 16 | 120 | 125 | 0.96 |
| 32 | 60 | 62 | 0.97 |

The kernel is **about one wavelength wide and halves when the band doubles**: it
is a property of the frequency, not of the model grid. In one dimension the
sensitivity is spread along the whole path inside that envelope, and the kernel
has positive and negative lobes. In two and three dimensions the same
construction produces the ring-shaped ("banana-doughnut") kernel, whose
travel-time sensitivity **vanishes on the geometric ray**. That structure is not
reproduced by a one-dimensional model and is not claimed here; what this
measurement does show is the general point that a finite-frequency measurement
sees a volume, and a ray is only the zero-width limit of that volume.

Two practical consequences:

1. Ray-based tomography and finite-frequency tomography are not the same
   inverse problem. They have different kernels, hence different null spaces,
   hence different answers from the same data — which is one reason two
   published models of the same region can differ without either being wrong in
   the arithmetic.
2. A kernel that is wider than the structure being sought sets the resolution
   directly: no regularisation can recover what the kernel does not sample.

## 6. Reliability: how far does the gradient point?

A gradient is a *local* statement. The demonstration takes one steepest-descent
step of size $f$ times the model rms along $-\mathbf{g}$ and compares the change
the linear model predicts with the change that occurs:

| $f$ | predicted $\Delta J$ | actual $\Delta J$ | ratio | $\cos(\mathbf{g}_{\text{new}},\mathbf{g}_{\text{old}})$ |
|---|---|---|---|---|
| $10^{-4}$ | $-2.12321\times10^{-2}$ | $-2.12008\times10^{-2}$ | 0.9985 | 1.000000 |
| $10^{-3}$ | $-2.12321\times10^{-1}$ | $-2.09182\times10^{-1}$ | 0.9852 | 0.999959 |
| $10^{-2}$ | $-2.12321\times10^{0}$ | $-1.80065\times10^{0}$ | 0.8481 | 0.991390 |
| $5\times10^{-2}$ | $-1.06161\times10^{1}$ | $-1.48173\times10^{0}$ | 0.1396 | $-0.842338$ |
| $2\times10^{-1}$ | $-4.24643\times10^{1}$ | $+2.05206\times10^{2}$ | $-4.8324$ | $-0.951436$ |

At $f = 10^{-2}$ the misfit still falls, but 15 per cent less than predicted; by
$f = 5\times10^{-2}$ the gradient has rotated to a *negative* cosine with itself
and the step no longer descends in the direction the linear model promised; at
$f = 2\times10^{-1}$ the misfit *increases*. Curvature of this magnitude is what
cycle skipping is made of, and it is why the safe step length is a modelling
decision tied to the band and to the starting error, not a number to be tuned
until the inversion "looks right".

## 7. Assumptions and regime of validity

1. **A differentiable misfit.** Equation (3) assumes $J$ is differentiable in
   the field; hard data windows, $L^1$ norms and picked arrivals need care.
2. **The discrete adjoint, not the continuous one.** Equation (4) is the
   transpose of the *scheme*, including its damping and boundary rows. The
   continuous adjoint gives the same answer only in the limit of a converged
   discretisation.
3. **Linearisation about the current model.** Section 6 measures the radius of
   validity: a step of $10^{-3}$ of the model rms is safe here,
   $5\times10^{-2}$ is not.
4. **A recorded field, not a picked time.** For travel-time measurements the
   kernel requires the measurement itself to be differentiable — which is why
   cross-correlation and instantaneous-phase measurements are used instead of
   picks.
5. **Storage.** The backward propagation needs the forward field at every step: a
   memory-versus-recomputation decision (checkpointing) that is invisible in the
   equations and dominant in the implementation.
6. **One source at a time.** The cost argument is per source; a realistic
   inversion sums (4) over sources and receivers, and the practical cost is
   proportional to the number of forward problems.

## 8. Demonstration

[`code/adjoint_methods_demo.py`](code/adjoint_methods_demo.py): the brute-force
gradient, the adjoint gradient with both verification tests, the cost table, the
kernel widths against the band, and the step-length study. Exercises:
[`exercises/05-adjoint-methods-exercises.md`](exercises/05-adjoint-methods-exercises.md),
solutions:
[`exercises/05-adjoint-methods-solutions.md`](exercises/05-adjoint-methods-solutions.md).

## Mastery checkpoint

> A waveform inversion has $5\times10^{5}$ parameters and 200 sources.
> **(a)** Estimate the number of forward solves a finite-difference gradient
> needs, and compare with the adjoint route. **(b)** Your adjoint gradient agrees
> with finite differences at 10 randomly chosen parameters but the inversion
> diverges. Name the test you have not run and say what it checks. **(c)** The
> kernel of a 15 s surface-wave measurement is one wavelength wide; a colleague
> claims 50 km resolution at 100 s period in a 4.0 km/s medium. Compute the
> wavelength and comment. **(d)** State two reasons why a step of 0.2 times the
> model rms is a bad idea here, using measured numbers.

## Common pitfalls

1. **Deriving the adjoint on paper and not testing it.** The median agreement
   here was $6\times10^{-10}$ and the worst $2\times10^{-6}$ — a test that would
   have caught every intermediate mistake made while writing it.
2. **Forgetting a boundary or damping row.** The free-surface row alone moved the
   gradient error from $\sim10^{-9}$ to a factor of 1.44 at the affected cells.
3. **Treating the gradient as global.** Measured: the cosine between successive
   gradients becomes negative at a step of 5 per cent of the model rms.
4. **Confusing the kernel with the ray.** The ray is the zero-frequency limit of
   the kernel; using it where the wavelength matters changes the answer.
5. **Ignoring memory.** The backward pass needs the whole forward field history;
   checkpointing is part of the method, not an optimisation.
6. **Reporting "the adjoint method" as a result.** The method is a way of
   computing a derivative; the reliability questions of lesson 06-06-04 are
   unchanged by it.

## Related modules

- [04 Full-Waveform Inversion](04-full-waveform-inversion.md).
- [18-04 Nonlinear Inversion and Optimisation](../../18-inverse-problems/04-nonlinear-inversion/README.md) —
  what to do with the gradient once you have it.
- [18-09 Machine Learning Approaches to Inversion](../../18-inverse-problems/09-machine-learning-inversion/README.md) —
  physics-informed networks use the same adjoint machinery.
- [03-12 Building Numerical Simulation Code in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md) —
  verification practice for the schemes being differentiated.
