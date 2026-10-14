---
id: 19-05-02
title: "Boundary Element Methods for Potential Fields"
level: research
prereqs: ["19-05-01", "19-02-06", "19-01-02"]
tags: [numerical-modelling, hpc, boundary-element, potential-fields, integral-equations, conditioning]
---

# Boundary Element Methods for Potential Fields

## Learning objectives

By the end of this lesson you will be able to:

1. **Assemble** the two boundary matrices $H$ and $G$ for constant panels,
   including the analytically integrable diagonal of $G$ and the vanishing
   diagonal of $H$.
2. **Derive** the free term of the boundary integral equation and **verify** it
   from the discrete row sums of $H$.
3. **Distinguish** the interior problem from the exterior problem and show, by a
   measured flux error, what happens when the sign of the free term is carried
   over unchanged.
4. **Measure** the convergence order of constant panels in the flux and in the
   reconstructed field, and explain why they are not second order.
5. **Compare**, on the same field and the same accuracy target, the unknowns a
   boundary method needs against those a volume grid needs — and report the case
   in which the volume grid wins.
6. **Quantify** the truncation error an exterior volume solve introduces, which
   the boundary method does not have.

## Prerequisites

- [19-05-01 Volume and Surface Integral Equations](01-integral-equations.md) —
  the representation, the outward normal, and the sign conventions fixed there.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md) —
  the refinement table used for every order quoted here.
- [19-02-06 FD for Diffusion, Laplace and Poisson Problems](../02-finite-difference-methods/06-fd-diffusion-and-potential.md) —
  the five-point operator used for the volume-grid comparison.

All models and data in this module are **SYNTHETIC**: the boundary is a chosen
disk of radius $10$ km and the test field is a chosen analytic harmonic function.
Nothing here is a measurement of the Earth, and no published boundary-element
benchmark is quoted.

## 1. The equation, and the free term

Let $u$ be harmonic in a domain $\Omega$ with boundary $\Gamma$, and let
$G(\mathbf{r}_0,\mathbf{r}') = -\frac{1}{2\pi}\ln|\mathbf{r}_0-\mathbf{r}'|$ be
the 2-D fundamental solution, satisfying $\nabla^{2}G = -\delta$. Green's second
identity,

$$\int_{\Omega}\left(u\nabla^{2}G - G\nabla^{2}u\right)\mathrm{d}A
= \oint_{\Gamma}\left(u\frac{\partial G}{\partial n'}
- G\frac{\partial u}{\partial n'}\right)\mathrm{d}l',$$

with $n'$ the **outward** normal, gives for a point $\mathbf{r}_0$ inside

$$u(\mathbf{r}_0) = -\oint_{\Gamma}u\frac{\partial G}{\partial n'}\,\mathrm{d}l'
+ \oint_{\Gamma}G\,q\,\mathrm{d}l', \qquad q \equiv \frac{\partial u}{\partial n'}.$$

Taking $\mathbf{r}_0$ to the boundary replaces $u(\mathbf{r}_0)$ by $c\,u$, with
$c = \tfrac12$ for a smooth boundary, and the discretised form is

$$\left(\tfrac12 I + H\right)\mathbf{u} = G\,\mathbf{q},
\qquad H_{ij} = \int_{\Gamma_j}\frac{\partial G}{\partial n'}\,\mathrm{d}l',
\qquad G_{ij} = \int_{\Gamma_j}G\,\mathrm{d}l'.$$

Two entries are analytic and worth knowing exactly:

- **$H_{ii} = 0$** for a straight panel, because $(\mathbf{r}'-\mathbf{r}_i)\cdot
  \mathbf{n}'_i = 0$ everywhere on the panel;
- $$G_{ii} = -\frac{1}{2\pi}L_i\left(\ln\frac{L_i}{2}-1\right)$$ for a panel of
  length $L_i$, from $\int_{0}^{L}\ln|t-\tfrac{L}{2}|\,\mathrm{d}t = L(\ln(L/2)-1)$.

The demonstration prints $G_{ii}$ for three resolutions of a circular boundary,
and the numbers carry the $\ln L$ growth that makes the diagonal dominant:

| $N$ panels | panel length $L$ (m) | $G_{ii}$ |
|---|---|---|
| 16 | 3901.806 | $-4083.6716$ |
| 64 | 981.353 | $-811.5155$ |
| 256 | 245.431 | $-148.8192$ |

**Worked check.** For $N = 16$, $L = 2\pi (10\,000)/16 = 3926.99$ m is the arc
length; the straight chord used by the discretisation is
$L = 2a\sin(\pi/N) = 20\,000\sin(11.25^{\circ}) = 3901.806$ m. Then

$$G_{ii} = -\frac{1}{2\pi}(3901.806)\left(\ln\frac{3901.806}{2}-1\right)
= -621.09\;(7.5761-1) = -4083.67,$$

matching the printed $-4083.6716$ to five figures. The lesson of the arithmetic
is that the self term is not small and not negligible: it dominates its row.

## 2. The free term, recovered from the row sums

A code that hard-codes $1/2$ has no evidence that $1/2$ is right. The discrete
row sums supply that evidence. For a smooth closed boundary the exact identity is

$$\sum_{j}H_{ij} = -\tfrac12,$$

which is the same information as the free term $+\tfrac12$ once the sign
convention of $G = -\frac{1}{2\pi}\ln r$ is fixed. Measured, with the panels as
built:

| $N$ | $\sum_j H_{ij}$ (row 0) | deviation from $-1/2$ | interior flux error |
|---|---|---|---|
| 8 | $-0.43750000$ | $6.250\times10^{-2}$ | $1.5362\times10^{-1}$ |
| 32 | $-0.48437500$ | $1.563\times10^{-2}$ | $4.4660\times10^{-2}$ |
| 64 | $-0.49218750$ | $7.813\times10^{-3}$ | $1.9318\times10^{-2}$ |
| 256 | $-0.49804687$ | $1.953\times10^{-3}$ | $4.1522\times10^{-3}$ |

The row sum converges to $-1/2$ **linearly**, and the flux error is of the same
order, within a factor of about two to three. That correlation is the useful
observation: the dominant error in a constant-panel flux is the error in the
free term, which is the chord-versus-arc error of the geometry.

Enforcing the identity exactly through

$$H_{ii} = -\frac12 - \sum_{j\neq i}H_{ij}$$

changes the flux error as follows (the same discretisation, one line of
assembly changed):

| $N$ | flux error, $H_{ii} = 0$ | flux error, row-sum diagonal |
|---|---|---|
| 16 | $1.036502\times10^{-1}$ | $3.985988\times10^{-2}$ |
| 32 | $4.465980\times10^{-2}$ | $1.314936\times10^{-2}$ |
| 64 | $1.931753\times10^{-2}$ | $3.654250\times10^{-3}$ |
| 128 | $8.776359\times10^{-3}$ | $9.587218\times10^{-4}$ |

The row-sum form is better by a factor of about $2.6$ to $9$, and its measured
order is closer to $2$ than to $1$. It is the standard "rigid-body" trick, and
here it is not folklore: the table is the evidence.

## 3. Interior convergence, measured

Test field: $u = (x^{3} - 3xz^{2})/a^{3} = (r/a)^{3}\cos 3\theta$ with
$a = 10$ km, harmonic everywhere, with exact interior normal derivative
$q = 3\cos(3\theta)/a$ on $r = a$ (maximum $|q| = 3.0\times10^{-4}\ \mathrm{m^{-1}}$).
The interior field is reconstructed at $512$ probe points on $r = 0.6a$:

| $N$ | $\max|q_{\text{BE}}-q_{\text{exact}}|/\max|q|$ | order | $\max|u_{\text{BE}}-u_{\text{exact}}|$ | order |
|---|---|---|---|---|
| 8 | $1.536234\times10^{-1}$ | — | $5.317799\times10^{-2}$ | — |
| 16 | $1.036502\times10^{-1}$ | 0.57 | $2.376444\times10^{-3}$ | 4.48 |
| 32 | $4.465980\times10^{-2}$ | 1.21 | $2.568230\times10^{-3}$ | $-0.11$ |
| 64 | $1.931753\times10^{-2}$ | 1.21 | $1.522122\times10^{-3}$ | 0.75 |
| 128 | $8.776359\times10^{-3}$ | 1.14 | $8.068233\times10^{-4}$ | 0.92 |
| 256 | $4.152242\times10^{-3}$ | 1.08 | $4.131929\times10^{-4}$ | 0.97 |

Two honest readings.

- The **flux** converges at about **first order**, not second. A constant flat
  panel represents both the arc and its normal to $O(h)$, and the normal enters
  $H$ and $G$ directly.
- The **reconstructed field** settles at first order too, *not* the second order
  a smoother argument might suggest. The reason is visible in the same table:
  the reconstruction uses
  $u(\mathbf{r}_0) = -\sum_jH_j u_j + \sum_jG_j q_j$, so an $O(h)$ error in $q$
  enters the answer through the single-layer kernel $G$. The field inherits the
  flux error. The single anomalous entry at $N = 16$ (order $4.48$) is a
  cancellation at one probe location, not a convergence rate, and the order
  settles to $0.9$–$1.0$ as the panels resolve the arc.

## 4. The exterior problem, and the sign of the free term

Apply the **same** Dirichlet data $u = \cos 3\theta$ to the **outside** of the
circle. The exact exterior flux is $q = -3\cos(3\theta)/a$: the same magnitude,
the opposite sign, because the outward normal of the exterior domain points
inward.

A single boundary integral equation does not know which side you meant. For an
exterior domain the outward normal is $-\mathbf{n}'$ relative to the disk, and
the derivation in Section 1 gives

$$\left(H - \tfrac12 I\right)\mathbf{u} = G\,\mathbf{q}_{\text{ext}},$$

i.e. the sign of the free term flips while $H$ and $G$ are unchanged. Measured:

| free term used | $\max$ relative error against the exterior solution |
|---|---|
| interior ($+\tfrac12$) | $2.0082\times10^{0}$ |
| exterior ($-\tfrac12$) | $6.8589\times10^{-3}$ |

The interior equation returns a flux wrong by $100\%$, exactly, because
$q_{\text{int}} = -q_{\text{ext}}$ for this data. Nothing in the assembly detects
this; the only symptom is a wrong answer. Reconstructing outside — using
$u(\mathbf{r}_0) = +\sum_j H_j u_j - \sum_j G_j q_j$, the opposite signs again —
recovers the decaying field at $r = 3a$ to $1.733\times10^{-4}$ against a maximum
value of $3.7037\times10^{-2}$.

## 5. Unknowns for the same accuracy: boundary against volume

This is the comparison that decides whether a boundary method is the right tool,
and it must be run on **the same field** to mean anything. Use
$u = \sin(x/a)\sinh(z/a)/\sinh(1)$, harmonic, and deliberately chosen so that the
five-point stencil does **not** annihilate it: a field the stencil solved exactly
would make the volume route look perfect and prove nothing. Errors are measured
inside $r < 0.9a$ for both routes.

| boundary panels $N$ | $\max|u_{\text{BE}}-u|$ |
|---|---|
| 8 | $9.9820\times10^{-3}$ |
| 32 | $2.3454\times10^{-3}$ |
| 64 | $1.1916\times10^{-3}$ |
| 128 | $5.9824\times10^{-4}$ |

| volume grid $n$ | unknowns | nonzeros | $\max|u_{\text{FD}}-u|$ | order |
|---|---|---|---|---|
| 16 | 256 | 1040 | $2.4547\times10^{-5}$ | — |
| 32 | 1024 | 4624 | $8.5138\times10^{-6}$ | 1.53 |
| 64 | 4096 | 19472 | $2.5028\times10^{-6}$ | 1.77 |
| 128 | 16384 | 79888 | $6.7720\times10^{-7}$ | 1.89 |
| 256 | 65536 | 323600 | $1.7607\times10^{-7}$ | 1.94 |

**The measured result does not favour the boundary method here.** In two
dimensions, for a smooth interior problem in a bounded domain, the volume grid
reaches $2.50\times10^{-6}$ with $4096$ unknowns while the boundary method needs
more than $128$ panels to reach $5.98\times10^{-4}$. Constant panels are simply a
lower-order discretisation than a five-point Laplacian on this field.

The boundary method's advantages are real but they are elsewhere, and each is
either measured below or is arithmetic:

- **Exterior domains need no truncation** (Section 6).
- **In three dimensions the unknowns scale with the surface, not the volume:**
  a grid with $128$ nodes per direction has $128^{3} = 2\,097\,152$ unknowns
  against $128^{2} = 16\,384$ boundary nodes. That is arithmetic, not a
  measurement, and it is the reason the method is used in 3-D and often not in
  2-D.
- **The operator is dense**, so the cost sits in the linear solve: for $N$ panels
  the matrix has $N^{2}$ entries against about $5n^{2}$ nonzeros for the grid on
  $n^{2}$ unknowns.

A lesson that reported only the third bullet and not the first table would be
hiding the measurement.

## 6. Truncation error: what an exterior volume solve pays

An exterior solve must place a boundary at some radius $R$ and impose a
condition there. For the decaying field $u = (a/r)^{3}\cos3\theta$ with $u = 0$ at
$R$, the exact solution of the truncated problem is

$$u_{R} = c\left(r^{3} - \frac{R^{6}}{r^{3}}\right)\frac{\cos3\theta}{a^{3}},
\qquad c = \frac{a^{6}}{a^{6}-R^{6}},$$

and the error inside the physical region is:

| $R/a$ | $\max$ error for $r \ge a$ |
|---|---|
| 2 | $1.2500\times10^{-1}$ |
| 4 | $1.5625\times10^{-2}$ |
| 10 | $1.0000\times10^{-3}$ |
| 100 | $1.0000\times10^{-6}$ |

The error falls as $(a/R)^{6}$, so it vanishes only as $R\to\infty$: at $R/a =
100$ it is still $10^{-6}$, which is far above the accuracy the boundary method
reaches at $r = 3a$ ($1.733\times10^{-4}$ with $128$ panels — and that number is
limited by the panels, not by a truncation choice). The boundary method has no
$R$ to choose, and therefore no truncation error to report.

## 7. Assumptions and regime of validity

1. **Laplace's equation, constant coefficients, 2-D.** The Green's function
   $-\frac{1}{2\pi}\ln r$ is a 2-D free-space kernel. Layered media, variable
   coefficients and 3-D each require their own kernel
   ([03 Numerical Green's Functions](03-greens-function-numerics.md)).
2. **Smooth closed boundary.** The free term $c = 1/2$ holds for a smooth
   boundary at a point where the boundary is straight in the discretised sense.
   A corner has a different $c$, and a code that ignores that produces a locally
   wrong flux.
3. **Constant panels.** The measured first-order flux convergence is a property
   of this choice. Linear or quadratic elements raise it, at the cost of a more
   elaborate assembly.
4. **Observation points away from the boundary.** The reconstruction integrals
   use the same kernels; near the boundary the near-singular quadrature degrades
   and the near-field accuracy is worse than the numbers in Section 3 suggest.
5. **A well-conditioned $G$.** Here the self term dominates and $G$ is easy to
   invert. That is not general: a thin body, or a low-frequency Helmholtz
   problem, produces a nearly singular $G$ and needs a different formulation.
6. **An analytic test field.** Every error quoted is against a field with a
   closed-form flux. In a real problem there is no such reference, which is why
   [19-07 Verification, Validation and Numerical Uncertainty](../07-verification-validation-uncertainty/README.md)
   exists.

## 8. A fully worked example

Boundary data $u = \cos3\theta$ on a circle of radius $a = 10\,000$ m, four
panels ($N = 4$) as a hand-sized case, in the sign convention of Section 1.

- Panel length: $L = 2a\sin(\pi/4) = 20\,000(0.7071) = 14\,142.1$ m; panel
  midpoints at $\theta = 45^{\circ}, 135^{\circ}, 225^{\circ}, 315^{\circ}$.
- Boundary data: $u = \cos(3\theta)$ gives
  $\cos135^{\circ} = -0.7071$, $\cos405^{\circ} = \cos45^{\circ} = 0.7071$, and
  the pair repeats with the same signs at $225^{\circ}$ and $315^{\circ}$.
- Exact flux: $q = 3\cos(3\theta)/a$, so
  $|q|_{\max} = 3/10\,000 = 3.0\times10^{-4}\ \mathrm{m^{-1}}$.
- $G_{ii} = -\frac{1}{2\pi}(14\,142.1)(\ln 7071.1 - 1)
  = -2250.8\,(8.8640-1) = -1.7695\times10^{4}$.

The measured $N = 8$ row is the smallest case the demonstration reports, and it
already shows the pattern: flux error $1.536234\times10^{-1}$ of $\max|q|$, i.e.
$4.6\times10^{-5}\ \mathrm{m^{-1}}$ in absolute terms, with the row sum at
$-0.4375$ rather than $-0.5$. Both numbers are large; both halve when the panel
count doubles. The convergence is slow, it is consistent, and the free-term
deficit explains most of it — which is what Section 2 measured by enforcing the
identity.

## 9. Python demonstration

`code/boundary_element_demo.py` builds the matrices, verifies the free term from
the row sums, measures interior convergence, runs the exterior problem with both
signs of the free term, compares unknown counts against a volume grid on the same
field, and quantifies the truncation error a volume solve would introduce.

```bash
cd 19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python boundary_element_demo.py
```

## 10. Exercises

Full sets with worked solutions are in
[`exercises/02-boundary-element-exercises.md`](./exercises/02-boundary-element-exercises.md)
and [`exercises/02-boundary-element-solutions.md`](./exercises/02-boundary-element-solutions.md).

- **★** Compute $G_{ii}$ for $N = 64$ from the printed chord length.
- **★** State why $H_{ii} = 0$ for a straight panel, in one sentence.
- **★★** From the row-sum table, show that the deviation falls linearly and
  estimate the constant in the deviation law.
- **★★** Explain, using the two tables of Section 5, why a boundary method is a
  3-D method and not a 2-D one.
- **★★★** Design a refinement study that decides whether the remaining flux
  error after the row-sum correction is a geometric (chord) effect or a
  quadrature effect, and state the observable that separates them.

## Mastery checkpoint

Without notes:

> A constant-panel boundary-element code on a circle of radius $10$ km reports
> $\sum_j H_{ij} = -0.48437500$ for one row, a flux error of
> $4.465980\times10^{-2}$ of $\max|q|$, and an exterior reconstruction at
> $r = 3a$ with error $1.733\times10^{-4}$. **(a)** How many panels does it have?
> **(b)** What sign of the free term was used, and what evidence supports your
> answer? **(c)** If the same field were solved by a five-point volume grid,
> state which route you would expect to need fewer unknowns and quote the
> measurement that decides it.

A worked version appears in the lesson-02
[solutions](./exercises/02-boundary-element-solutions.md).

## Common pitfalls

1. **Hard-coding the free term without checking it.** The row sums are free
   evidence; a code that never looks at them will not notice a
   chord-versus-arc deficit of a few per cent that shows up in every flux.
2. **Reusing the interior equation for an exterior problem.** The sign flip is
   not a detail — measured here as a $100\%$ error, silently.
3. **Quoting a boundary-method accuracy win in 2-D.** Section 5 measures the
   opposite; the win is in 3-D (surface against volume) and for unbounded
   domains.
4. **Reporting an order from two adjacent rows.** The $N = 16$ field-error entry
   in Section 3 shows an order of $4.48$; a rate read from two rows is a
   coincidence, and a rate read from four is a measurement.
5. **Forgetting that the reconstruction is an integral of the flux.** A
   first-order flux error propagates into the field; the potential is only
   second order if the flux is.
6. **Assuming the matrix is sparse.** It is dense by construction, and the
   comparison in Section 5 must be made on total work, not on unknowns alone.

## Related modules

- [01 Volume and Surface Integral Equations](01-integral-equations.md) — the
  representation and its conventions.
- [03 Numerical Green's Functions and Their Computation](03-greens-function-numerics.md) —
  the kernels a layered or screened medium requires.
- [04 Fast Multipole and Hierarchical Acceleration](04-fast-multipole.md) — what
  makes a dense boundary operator affordable.
- [19-03 Finite Element and Finite Volume Methods](../03-finite-element-and-volume/README.md) —
  the volume-based alternative whose discretisation variance is measured here.
- [19-06 High-Performance and Parallel Computing](../06-hpc-and-parallel-computing/README.md) —
  the dense solve as a performance problem.
