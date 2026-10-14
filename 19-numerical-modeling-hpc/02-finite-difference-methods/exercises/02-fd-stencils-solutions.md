# Solutions — 19-02-02 High-Order and Compact Stencils; Staggered Grids

> **Read after attempting the exercises.** Demonstration values are quoted where
> they apply; arithmetic is shown.

Lesson: [02 FD Stencils](../02-fd-stencils.md).

---

## ★1 — Fourth-order centred stencil

Weights $(1, -8, 0, 8, -1)/12$ on offsets $(-2,-1,0,1,2)$, divided by $h$.
Leading term: $-\dfrac{h^{4}}{30}f^{(5)}$ — the fourth-order symbol is
$S(\theta) = (8\sin\theta - \sin2\theta)/(6\theta)$, so
$1-S = \theta^{4}/30 + O(\theta^{6})$.

---

## ★2 — Staggered derivative

$$g_{i+1/2} = \frac{u_{i+1}-u_i}{h}, \qquad
g = u' + \frac{h^{2}}{24}u''' + O(h^{4}), \qquad
S(\theta) = \frac{\sin(\theta/2)}{\theta/2}.$$

Expanding: $1 - S = \theta^{2}/24 + O(\theta^{4})$, so the ratio of constants to
the centred second-order stencil's $\theta^{2}/6$ is

$$\frac{1/24}{1/6} = \frac14.$$

Measured at PPW $= 8$: $2.550\times10^{-2}$ against $9.968\times10^{-2}$, ratio
$3.908$ — the asymptotic $4.000$ modified by the $O(\theta^{4})$ term.

---

## ★3 — Resolving power

The resolving power of a scheme is the number of grid points per wavelength
needed to keep a stated phase error, here $1\,\%$. Measured: second-order
explicit $25.612$ points per wavelength; staggered two-point $12.806$.

---

## ★4 — Cheapest sufficient scheme at PPW $= 10$

Measured dispersion at $\mathrm{PPW} = 10$ (computed from the symbols):
explicit p=2 gives $0.935489$ (a $6.45\,\%$ error — insufficient); explicit p=4
gives $0.995043$ ($0.50\,\%$ — sufficient but marginal); staggered 2 gives
$0.983632$ ($1.64\,\%$ — insufficient); Padé 4 gives $0.999093$ ($0.09\,\%$ —
sufficient with a large margin).

So the choice is between explicit p=4 (width 5) and Padé 4 (width 3). Using the
measured one-per-cent thresholds (8.348 and 5.628 points), both satisfy the
target at PPW $=10$; the compact scheme does so with a factor
$8.348/5.628 = 1.48$ more margin at the same stated resolution and a narrower
stencil, at the cost of a tridiagonal solve. **Cheapest** therefore depends on
the hardware: on a CPU with a banded solver the compact scheme wins by the
work-per-wavelength proxy ($16.9$ against $41.7$); with many right-hand sides per
step on a GPU, the explicit stencil's independence usually wins.

---

## ★5 — Compact against explicit

Error ratio at $n = 256$:
$1.210\times10^{-8}/2.016\times10^{-9} = 6.00$.

Non-zeros per row at $n = 1024$: compact (tridiagonal) $3$; explicit five-point
$5$. The measured totals are $3072$ against $5120$ — the compact scheme is both
more accurate ($6\times$) and sparser ($1.67\times$ fewer non-zeros) on this
problem, because the band solve replaces the wide stencil.

---

## ★6 — Energy conservation against annihilation

**Staggered leapfrog.** For the two-level update the amplification roots satisfy
$G^{2} - 2bG + 1 = 0$ with $b = 1-2C^{2}\sin^{2}(\theta/2)$. For
$C\le1$ the discriminant is negative, so the roots are complex conjugates with
$|G_1G_2| = 1$ and $|G_1| = |G_2| = 1$: every mode is neutral, so the discrete
quadratic form $\frac12\sum[((u^{n+1}-u^n)/dt)^{2}+((u_{i+1}-u_i)/h)^{2}]$ is
invariant and the measured drift is round-off
($\sim2\times10^{-10}$ over 5000 steps, with no systematic sign).

**Upwind.** For $u_t + au_x = 0$,
$|G|^{2} = 1-2C(1-C)(1-\cos\theta)$. At $\theta = \pi$ and $C = 1/2$,
$|G|^{2} = 1-2(0.25)(2) = 0$: the mode is annihilated in a single step, so
energy is *removed* rather than redistributed. The mechanism differs in kind:
leapfrog's neutrality comes from a symmetric operator and a symplectic time
step; upwind's damping comes from an asymmetric spatial difference that mimics
diffusion.

---

## ★7 — A 3-D elastic model at four points per wavelength

**Scheme.** A staggered-grid velocity–stress formulation (Virieux) with a
fourth-order spatial stencil applied to the staggered derivative
$S(\theta) = \sin(\theta/2)/(\theta/2)$-type differences, or the standard
2-4 scheme (second order in time, fourth order in space).

**Resolving power.** The measured overlap between the one-dimensional tables and
the 3-D requirement: the staggered derivative's error is $1-\theta^{2}/24$, which
at $\mathrm{PPW} = 4$ ($\theta = \pi/2$) is $1-0.1028 = 0.897$ — a $10\,\%$
error, above the $2\,\%$ target. The fourth-order staggered family reaches
$2\,\%$ at about $\mathrm{PPW} = 6$. Conclusion: at four points per wavelength
with the *fourth-order* staggered stencil (error $\sim\theta^{4}/1920$,
$\approx0.3\,\%$ at PPW $= 4$ for the interior symbol), the target is met;
with a second-order stencil it is not. **State the stencil order with the
resolution** — "four points per wavelength" alone does not determine the error.

**Boundaries and memory.** Memory is the binding constraint: three velocity
components plus six stresses per cell is nine fields. For a $400^{3}$ grid this
is $9\times6.4\times10^{7}\times8$ bytes $= 4.6$ GB per copy, so three copies
(leapfrog needs two time levels plus a work array) exceed $13$ GB. A memory-first
design reduces the grid, not the stencil order.

**Verification.** (i) A one-dimensional staggered test against the exact
impedance reflection coefficient, as in the lesson's measured table, to calibrate
amplitudes. (ii) The dispersion relation measured along the axis and the
diagonal against the stencil's own prediction. (iii) A homogeneous half-space
run with the analytical free-surface reflection to check the boundary
implementation. Fail any of the three and the model is not ready for geology.

---

## ★8 — Nine-point Laplacian in a 3-D EM solver

**Case for.** Anisotropy of $0.027\,\%$ against $1.30\,\%$ at PPW $=8$ means the
*modelling error* falls by a factor $49$ at the same grid. In a frequency-domain
solve the cost is dominated by the linear algebra, and the same grid with a
$49\times$ smaller modelling error is equivalent to refining by about
$\sqrt{49} = 7$ in each direction — i.e. $343\times$ more unknowns — to achieve
the same accuracy with the five-point operator. No bandwidth argument survives
that comparison.

**Case against.** The nine-point operator raises the number of non-zeros per row
from $7$ in 3-D (the standard seven-point stencil) to $27$ for the full
nine-point family extended to three dimensions (or $19$ for the
nineteen-point variant), a factor $2.7$–$3.9$ in the matrix and in the cost of
each matrix-vector product. If the solver is already at the memory limit, that
factor is decisive.

**Resolution.** Compare at *equal accuracy*: the question is not "which stencil
is sparser" but "which grid reaches the target with the smaller product of
unknowns and non-zeros per row". Using the measured anisotropy numbers, the
five-point scheme needs about seven times finer resolution in each direction for
the same angular error, which changes the unknown count by $343\times$ against a
$4\times$ bandwidth penalty — so the nine-point operator wins unless the angular
error is not the binding error term. Check that first: if the source bandwidth
or the conductivity contrast dominates, neither stencil's anisotropy matters.
