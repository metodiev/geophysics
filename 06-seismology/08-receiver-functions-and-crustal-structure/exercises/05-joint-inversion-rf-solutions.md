# Solutions — 06-08-05 Joint Inversion of Receiver Functions and Surface Waves

> Read after attempting. Lesson: [05 Joint Inversion](../05-joint-inversion-rf.md).

---

## ★1 — Objective value

$$\chi^{2}_{t} = \left(\frac{0.05}{0.05}\right)^{2} = 1.00,$$
$$\chi^{2}_{c} = \left(\frac{0.02}{0.02}\right)^{2} +
\left(\frac{-0.03}{0.02}\right)^{2} = 1.00 + 2.25 = 3.25,$$
$$\chi^{2} = 4.25.$$

---

## ★2 — Why divide by the uncertainty

Without normalisation, a time residual in seconds would be added to a velocity
residual in km/s — a dimensionally meaningless sum whose minimum depends on the
arbitrary sizes of the units. Dividing by each data set's uncertainty converts
every residual into "how many standard deviations off", which is dimensionless
and comparable. It also gives each measurement its proper weight: a precise
measurement constrains more than an imprecise one.

---

## ★3 — Asymptotic limits

**Right-hand side as $\omega\to0$:** the layer term
$\omega H\sqrt{b_1^{-2}-c^{-2}}\to0$, so $\tan(\cdot)\to0$, and the relation
requires the right-hand side to vanish too. The right-hand side is
$\dfrac{\mu_2\sqrt{c^{-2}-b_2^{-2}}}{\mu_1\sqrt{b_1^{-2}-c^{-2}}}$; it vanishes
when $c\to b_2$ (numerator zero). So $c\to b_2$: the long-period limit samples
the half-space. Numerical check in the demonstration: $c = 4.4917$ at
$T = 200\ \mathrm{s}$ against $b_2 = 4.5000$, a $0.18\%$ difference.

**As $\omega\to\infty$:** the layer term oscillates rapidly unless
$\sqrt{b_1^{-2}-c^{-2}}\to0$, i.e. $c\to b_1$, which makes the tangent argument
finite and the right-hand side large. So the short-period limit is $c\to b_1$.
Numerical check: $c = 3.6648$ at $T = 1\ \mathrm{s}$ against $b_1 = 3.6501$, a
$0.4\%$ difference.

---

## ★4 — Reading the three admitted ranges

- **16 km (receiver function alone):** the observables determine only a
  combination of $H$ and $k$; along the ridge, any $H$ in the grid is admissible
  with a compensating $k$. The receiver function is *detecting* structure but not
  *resolving* the split between thickness and velocity ratio.
- **2 km (dispersion alone):** the phase-velocity curve across eight periods
  determines $b_1$ and $H$ jointly well enough to bound $H$ to a few kilometres.
- **1 km (joint):** intersecting the two constraints bounds $H$ to the grid
  step.

The **dispersion** does the constraining in the joint fit; the receiver function
is what makes the depth *interpretable as a conversion depth* rather than merely
a layer thickness. Reporting all three is essential, because it shows which
measurement carries the information.

---

## ★5 — Halving $\sigma_c$

The dispersion residuals double in standardised units, so the dispersion term
dominates $\chi^{2}$ and the joint minimum is essentially the dispersion-only
minimum: the receiver function barely influences the answer. What must be
reported: the $\chi^{2}$ contribution of each data set, the admitted range for
each weighting tried, and the statement that the receiver function's independent
constraint is small at that weighting. If the answer changes materially with the
weighting, the data do not determine it.

---

## ★6 — Testing near-orthogonality of null directions

Compute, for a candidate model, the Hessian (or Fisher information) matrix of each
objective in $(H,k)$, then the null direction of each (the eigenvector of the
smallest eigenvalue). The quantity to compute is the angle $\theta$ between the
two null directions, or equivalently the condition number of the summed Hessian
relative to the better-conditioned single-objective Hessian.

$$\cos\theta \approx \frac{\mathbf{n}_1\cdot\mathbf{n}_2}
{\lVert\mathbf{n}_1\rVert\,\lVert\mathbf{n}_2\rVert}.$$

If $|\cos\theta|\to1$ (null directions parallel), the joint Hessian remains nearly
singular and joint inversion cannot help — the two data sets are redundant. If
$|\cos\theta|\to0$, they are complementary. In the demonstration's single-layer
model the two trade-offs are close to orthogonal, which is why the joint range
(1 km) is far smaller than either alone (16 km and 2 km).

---

## ★7 — Two-layer crust

For a two-layer crust the model space gains parameters (two thicknesses, two
velocity ratios) and the receiver function gains extra conversions and multiples,
some of which are degenerate with each other. The dispersion curve also becomes
more sensitive to the layering.

**Prediction:** the joint objective will sharpen the total crustal thickness, but a
trade-off between the thicknesses of the two layers can persist if the deeper
contrast is weak: moving material across the intra-crustal interface changes the
dispersion only slightly while the Ps times can be matched by a compensating
velocity-ratio change. **Residual non-uniqueness:** the depth of the intra-crustal
interface and the velocities within it remain coupled; adding dispersion does not
guarantee their separation. The honest output is a set of two-layer models with
equal fit, not a single profile.
