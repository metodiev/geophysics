# Exercises — 06-02-01 Eikonal Equation, Rays and Fermat's Principle

Attempt these before reading the
[solutions](./01-eikonal-and-rays-solutions.md). The lesson is
[01 Eikonal Equation, Rays and Fermat's Principle](../01-eikonal-and-rays.md).
All models are **SYNTHETIC** teaching values. Numbers marked "from the demo" are
printed by `code/eikonal_and_rays_demo.py`.

## ★ Foundational

**★1.** A homogeneous medium has $v = 3000\ \mathrm{m\,s^{-1}}$ and a point
source at the origin. Write $T(x,z)$, compute $T$ at $(4.0, 3.0)$ km, verify
$|\nabla T| = 1/v$ analytically, and state the unit of $|\nabla T|$.

**★2.** For $v(z) = 2500 + 0.8z$ (with $z$ in metres and $v$ in
$\mathrm{m\,s^{-1}}$), compute the dimensionless validity group
$\varepsilon = f^{-1}\,|\mathrm{d}v/\mathrm{d}z|$ at $f = 20$ Hz and at
$f = 5$ Hz. State in one sentence, for each, whether a ray description is
defensible.

**★3.** Using the closed form
$T = (1/g)\,\mathrm{arccosh}\left(1 + g^{2}(x^{2}+z^{2})/(2v_0(v_0+gz))\right)$
with $v_0 = 2000\ \mathrm{m\,s^{-1}}$ and $g = 0.50\ \mathrm{s^{-1}}$, evaluate
$T(3000, 0)$ and $T(0,0)$. State the unit and explain why $T(0,0)$ must vanish.

## ★★ Applied

**★★4.** Derive the eikonal equation and the transport equation from the
trial solution $u = A(\mathbf{x})e^{i\omega(T(\mathbf{x}) - t)}$. Name the two
terms that are dropped, and state which of them carries the information that
ray theory does not provide.

**★★5.** The demonstration reports fast-marching errors of 91.645060, 53.556648,
30.732574 and 17.370528 ms at $h = 200, 100, 50, 25$ m. Compute the three
consecutive order estimates $p_k = \log_2(e_k/e_{k+1})$ and their mean, and
compare with the printed fitted order of 0.800.

**★★6.** A receiver $8485.281$ m from a source in a homogeneous
$v = 3000\ \mathrm{m\,s^{-1}}$ medium records an arrival picked with
$\sigma_t = 5.0$ ms at an exact time of $2.828427$ s. Compute the distance
scatter from the pick alone, and the distance shift produced by a 0.5 %
velocity error at fixed time. Report the ratio. Say which of the two the eikonal
solver supplies.

## ★★★ Research-oriented

**★★★7.** Fermat's principle. For the gradient of ★3, consider the family of
two-segment paths from $(0,0)$ to $(6000, 3000)$ m that passes through a
way-point at depth 1500 m and horizontal position $6000a$ for $0 \le a \le 1$.
Evaluate $T(a)$ at $a = 0$, $0.2$, $0.5$ and $1.0$, locate the minimum
numerically, and compare the minimum with (i) the straight-chord time
$2.502678$ s and (ii) the ray time $2.390587$ s from the closed form. State what
the comparison proves about stationarity and about what a broken line can
represent.

**★★★8.** Design an experiment that would *measure* the failure of ray theory in
a layered model. Specify the model (a synthetic stack with one low-velocity
layer), the two independent predictions (closed-form branches, and a grid
eikonal solve), the quantity you would compare, and the outcome that would
falsify the claim that a grid solver misses shallow-angle arrivals. A
specification that could not be executed is a failed answer.
