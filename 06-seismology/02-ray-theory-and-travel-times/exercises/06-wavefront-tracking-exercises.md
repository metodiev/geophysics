# Exercises — 06-02-06 Wavefront Tracking and the Fast Marching Method

Attempt these before reading the
[solutions](./06-wavefront-tracking-solutions.md). The lesson is
[06 Wavefront Tracking and the Fast Marching Method](../06-wavefront-tracking.md).
All models are **SYNTHETIC** teaching values. Numbers marked "from the demo" are
printed by `code/wavefront_tracking_demo.py`.

## ★ Foundational

**★1.** A grid has spacing $h = 200$ m and the local speed is
$v = 4000\ \mathrm{m\,s^{-1}}$. Compute $f = h/v$ and state its unit and its
meaning.

**★2.** At a node, the smallest accepted neighbour values along the two axes are
$a = 5.0$ ms and $b = 12.0$ ms, with $h = 50$ m and
$v = 4000\ \mathrm{m\,s^{-1}}$. Decide which case of the Godunov update applies,
justify the decision numerically, and compute $T$ at the node.

**★3.** State two invariants the Godunov update must satisfy, and verify both for
the value computed in ★2.

## ★★ Applied

**★★4.** From the demo, the marching errors on the homogeneous model are
44.144665, 25.445223 and 14.435493 ms at $h = 100, 50, 25$ m. Compute the two
consecutive order estimates, their mean, and compare with the printed fitted
order. Explain in one sentence why the order is slightly below 1.

**★★5.** The demo reports a model-error scatter of 24.401 ms for a 1.5 % velocity
error and a discretisation error of 44.145 ms at $h = 100$ m. State which term
dominates, compute the grid spacing (assuming first-order convergence and a
factor-2 refinement) at which the discretisation error would fall to one quarter
of the model term, and say whether that refinement is worth doing.

**★★6.** The two solvers agree to $0.000\times10^{0}$ ms at every grid spacing
tested, while both disagree with the analytic solution by tens of milliseconds.
Explain why the *exact* inter-solver agreement is expected, not fortunate, and
what the pair of results therefore does and does not validate.

## ★★★ Research-oriented

**★★★7.** Design an experiment that would let a first-arrival solver detect the
presence (not the times) of a triplication. Specify the model, the quantities you
would compute at each node, the diagnostic you would apply to the resulting field,
and the outcome that would prove the *first-arrival* field alone cannot see the
later branches. A design that cannot be executed is a failed answer.

**★★★8.** Consider the node diagonally adjacent to the source on a uniform grid of
spacing $h$ in a homogeneous medium of speed $v$. Compute the exact travel time
and the value the Godunov scheme produces there, and show that the relative error
is $1/\sqrt{2} + 1/2 - 1 = 20.71\%$, independent of $h$ and of $v$. Explain why
this makes the *maximum relative* error of the scheme stop improving under
refinement, and state the practical remedy.
