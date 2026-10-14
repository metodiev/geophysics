# Solutions — 06-02-06 Wavefront Tracking and the Fast Marching Method

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand; where a problem admits more than one defensible answer it is said so.

Lesson: [06 Wavefront Tracking and the Fast Marching Method](../06-wavefront-tracking.md).

---

## ★1 — The grid-time scale

$$f = \frac{h}{v} = \frac{200}{4000} = 0.050000\ \mathrm{s}.$$

Unit: $\mathrm{m}/(\mathrm{m\,s^{-1}}) = \mathrm{s}$. Meaning: $f$ is the time for
the front to cross one cell along an axis, i.e. the natural unit of the discrete
update — the quantity the eikonal equation compares against
$(\max(T-a,0))^{2} + (\max(T-b,0))^{2}$ in the stencil.

---

## ★2 — Which case applies

$$f = \frac{h}{v} = \frac{50}{4000} = 0.012500\ \mathrm{s} = 12.500\ \mathrm{ms}.$$

One-sided test: $a + f = 5.0 + 12.5 = 17.5$ ms, which is **greater** than
$b = 12.0$ ms, so the one-sided formula does not apply. Information is arriving
diagonally, and the quadratic case is used:

$$2f^{2} - (b-a)^{2} = 2(0.0125)^{2} - (0.007)^{2}
= 3.125\times10^{-4} - 4.9\times10^{-5} = 2.635\times10^{-4},$$
$$\sqrt{2.635\times10^{-4}} = 0.0162327\ \mathrm{s},$$
$$T = \tfrac{1}{2}\left(a + b + \sqrt{\cdot}\right)
= \tfrac{1}{2}(0.005 + 0.012 + 0.0162327) = 0.0166164\ \mathrm{s}
= 16.616\ \mathrm{ms}.$$

Had $b$ instead been 20.0 ms, the one-sided case would apply and
$T = a + f = 17.5$ ms.

---

## ★3 — Invariants

1. **Causality:** $T$ must exceed both $a$ and $b$. Here
   $16.616 > 12.0 > 5.0$ ms ✔.
2. **Diagonal bound:** a diagonal path is not slower than two axis-aligned legs,
   so $T \le \min(a,b) + f\sqrt{2}$; with $a = 5.0$ ms and
   $f\sqrt{2} = 17.68$ ms that upper bound is 22.68 ms, and
   $16.616 \le 22.68$ ✔. (A simpler, also valid, statement is $T < b + f$.)

Both are worth asserting in code: a violation means the upwind selection has been
implemented inconsistently with the quadratic, and the failure is otherwise silent.

---

## ★4 — Order from the printed errors

| pair | ratio | $p = \log_2$(ratio) |
|---|---|---|
| 44.144665 / 25.445223 | 1.734890 | 0.794844 |
| 25.445223 / 14.435493 | 1.762685 | 0.817774 |

Mean: $(0.794844 + 0.817774)/2 = 0.806309$, which matches the printed fitted
order of 0.806.

Why slightly below 1: the largest error sits in the first cells around the
source, where the front is most curved; the maximum-error norm is dominated by
that localised contribution, so refining $h$ reduces it at a rate slightly worse
than the ideal first order over the range measured.

---

## ★5 — Refining past the model error

- Discretisation error at $h = 100$ m: 44.145 ms.
- Model-error scatter: 24.401 ms.
- The discretisation error dominates by a factor $44.145/24.401 = 1.81$.

To bring the discretisation error to one quarter of the model term, i.e. to
$24.401/4 = 6.100$ ms, from 44.145 ms at first order in $h$:

$$h_{\text{new}} = h_{\text{old}}\frac{6.100}{44.145} = 100 \times 0.13819
= 13.8\ \mathrm{m}.$$

That is a factor of about 7.2 in spacing, hence about $7.2^{2} \approx 52$ times
as many nodes in two dimensions, for a total error that falls only from
$\sqrt{44.1^{2} + 24.4^{2}} = 50.4$ ms to
$\sqrt{6.1^{2} + 24.4^{2}} = 25.2$ ms — a factor of two. **Whether it is worth
doing depends on the purpose**: for a study whose requirement is 5 ms, no grid
achieves it (the model term alone is 24.4 ms); for one whose requirement is 50 ms,
the current grid already passes. Refining to satisfy a 25 ms requirement is a
reasonable engineering choice, but it must be stated as being about the *total*
error budget, not about the solver alone.

---

## ★6 — Why the two solvers agree exactly

Within a single node's update both algorithms apply *the same* Godunov formula,
and both terminate only when every node satisfies the same discrete equations. A
monotone upwind discretisation of the eikonal equation has a unique discrete
solution satisfying the boundary condition $T(\mathbf{x}_0) = 0$; therefore the
order in which the equations were solved cannot affect the answer, and any
difference is attributable only to floating-point summation order at the last bit.
The demonstration's $0.000\times10^{0}$ ms is therefore *expected*, not fortunate.

What the pair of results validates:

- **Yes:** the implementation of the update (a bug in the stencil would show up as
  a difference), and the convergence machinery of both algorithms (heap ordering
  versus sweeping order).
- **No:** the physics or the discretisation. Both solvers share the four-point
  stencil; their common 44 ms disagreement with the analytic circle is the
  discretisation error, and it can only be assessed against a solution obtained
  another way — a closed form, as in the lesson, or a much finer independent
  computation.

---

## ★7 — Detecting a triplication with a first-arrival field

- **Model.** A layered or gradient model with a velocity inversion deep enough to
  fold the travel-time curve, e.g. a fast lid over a low-velocity zone over a
  faster half space, all thicknesses at least ten cells.
- **Quantities.** Two fields over the grid: (i) the first-arrival time
  $T(\mathbf{x})$ from the solver, and (ii) its discrete ray-parameter field,
  obtained by central differences of $T$ along the surface,
  $p = \mathrm{d}T/\mathrm{d}X$.
- **Diagnostic.** A fold in the *full* travel-time curve appears in the
  first-arrival field as a **discontinuity in the gradient** of $T$ along the
  surface: the first-arrival curve switches branch with a kink (and often a
  *decrease* in $\mathrm{d}T/\mathrm{d}X$ in the fold's shadow side). Tabulate
  $\mathrm{d}T/\mathrm{d}X$ against offset and look for a jump; alternatively,
  count sign changes in the second derivative.
- **Outcome proving the first-arrival field is insufficient.** The kink locates the
  branch switch but reports *one* time at every offset. Comparing with a
  multi-arrival computation for the same model — or with the engine used in
  Lesson 05, which returns 5–7 arrivals in a triplication region — shows that at
  the kink offset the first-arrival field carries exactly one of the 5–7 times.
  The number of arrivals missing is the measure of what the viscosity solution
  discards, and it cannot be recovered from $T(\mathbf{x})$ alone.

---

## ★8 — The near-source error, exactly

Let the source be node $(0,0)$ with $T = 0$, and consider node $(1,1)$ at
distance $h\sqrt{2}$.

- **Exact:** $T_{\text{ex}} = h\sqrt{2}/v$.
- **Scheme:** both axial neighbours are at $T = h/v$ (they are reached along the
  axes, where the scheme is exact), so with $f = h/v$ we have $a = b = h/v$ and
  the quadratic reduces to $2(T - f)^{2} = f^{2}$, giving
  $T_{\text{scheme}} = f + f/\sqrt{2} = (h/v)(1 + 1/\sqrt{2})$.

The relative error is therefore

$$\frac{T_{\text{scheme}}}{T_{\text{ex}}}
= \frac{1 + 1/\sqrt{2}}{\sqrt{2}}
= \frac{1}{\sqrt{2}} + \frac{1}{2} = 1.207107 ,$$

i.e. **20.71 %**, with no $h$ and no $v$ in the expression.

Why the maximum *relative* error stops improving: the error at this node is a
fixed fraction of a travel time that itself scales with $h$, so it is invariant
under refinement. Averaged over the whole grid the error does fall at first order
(the measured fitted order of about 0.8–1.0), and the *maximum absolute* error
falls too, but the maximum *relative* error never improves on the near-source
ring — which is exactly why the demonstration's homogeneous run prints the same
$1.208\times10^{-1}$ maximum relative error at every grid spacing. That printed
value is measured over the interior of the grid, which excludes the first three
rows and columns, so it is the *next-worst* ring; the node computed here lies
inside the excluded one and is worse.

**Practical remedy.** Do not refine globally; fix the source. Either initialise a
small patch around the source analytically ($T = r/v$ for the first ring of
nodes), or use a locally exact update there. This is the standard treatment of the
source singularity in eikonal solvers.
