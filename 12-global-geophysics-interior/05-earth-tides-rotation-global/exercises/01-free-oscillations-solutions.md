# Solutions — 12-05-01 Free Oscillations of the Earth (Normal Modes)

> Read after attempting the
> [exercises](./01-free-oscillations-exercises.md). Lesson:
> [01 Free Oscillations of the Earth](../01-free-oscillations.md). Numbers
> computed. All models **SYNTHETIC**.

---

## ★1 — The radial equation and the $j_1$ solution

$$\frac{\mathrm{d}}{\mathrm{d}r}\left[(\lambda+2\mu)U' + \frac{2\lambda U}{r}\right]
+ \frac{4\mu}{r}\left(U' - \frac{U}{r}\right) = -\rho\omega^{2}U .$$

With constant moduli the left-hand side is
$(\lambda+2\mu)\left(U'' + \frac{2}{r}U' - \frac{2}{r^{2}}U\right)$ — the
three terms cancel pairwise into the operator with $l(l+1) = 2$, i.e. $l = 1$.
Substituting $U = j_1(kr)$ uses the spherical Bessel equation

$$x^{2}j_1'' + 2xj_1' + (x^{2} - 2)j_1 = 0
\;\Longrightarrow\;
j_1'' + \frac{2}{x}j_1' - \frac{2}{x^{2}}j_1 = -k^{2}j_1,$$

and the equation is satisfied with $k^{2} = \rho\omega^{2}/(\lambda+2\mu)$.

---

## ★2 — Fundamental period for $\alpha = 10$ km/s

$$\omega_0 = \frac{x_0\alpha}{R},\qquad
T_0 = \frac{2\pi R}{x_0\alpha}
= \frac{2\pi\times6.371\times10^{6}}{2.60263\times10.0\times10^{3}}.$$

Numerator: $4.0030\times10^{7}$ m. Denominator: $2.60263\times10^{4}$ m s⁻¹.

$$T_0 = 1.5381\times10^{3}\ \mathrm{s} = 25.63\ \mathrm{min}.$$

Units: m/(m s⁻¹) = s ✔. Note that a faster sphere has a *shorter* period, as
$T \propto 1/\alpha$ requires.

---

## ★3 — Boundary conditions

$$U(0) = 0 \quad\text{(regularity: the displacement cannot diverge at the centre)},$$
$$(\lambda+2\mu)U'(R) + \frac{2\lambda U(R)}{R} = 0 \quad\text{(free surface)}.$$

The second is a traction condition because a free surface is defined by the
absence of force, and force is traction — not displacement. This is why the first
eigenvalue of the radial problem is $x_0 = 2.60263$ rather than the $\pi$ that a
displacement-node argument would give.

---

## ★★4 — Convergence order and extrapolation

Ratios:

$$\frac{2.48\times10^{-5}}{6.58\times10^{-6}} = 3.77,\qquad
\frac{6.58\times10^{-6}}{1.69\times10^{-6}} = 3.89.$$

A second-order scheme doubles the spacing when $n$ halves, so the error should
change by $2^{2} = 4$; the observed ratios approaching 4 identify the scheme as
second-order, with the 3.77 at coarse resolution reflecting the interface
handling.

Prediction at $n = 800$: $1.69\times10^{-6}/3.9 \approx 4.3\times10^{-7}$, which
the demonstration's trend (ratio 3.77–3.89) supports to within about 10%.

---

## ★★5 — Scaling to a smaller, faster model

$$T \propto \frac{R}{\alpha}\;\Longrightarrow\;
\frac{T_{\text{new}}}{T_0} = \frac{0.97R}{1.02\alpha}\frac{\alpha}{R}
= \frac{0.97}{1.02} = 0.9510,$$

$$T_{\text{new}} = 0.9510\times32.0431 = 30.474\ \mathrm{min}.$$

The two changes partly cancel: a 3% smaller body and a 2% faster one move the
period in the same direction (both shorten it), and their *product* is what
appears — this is the degeneracy that
[12-06 Geodetic Constraints on the Interior](../../06-geodesy-constraints-interior/README.md)
exists to break.

---

## ★★6 — Sensitivity of a period to a deep perturbation

Using $\delta\ln T \approx -f\,\delta\ln\alpha$ with the kernel fraction
$f = 0.172$:

$$\left|\frac{\delta T}{T}\right| \approx 0.172\times0.02 = 0.0034
= 0.34\%,$$

i.e. about $0.07$ min on a 21.27-min period.

**Assumption.** That the mode's sensitivity to a perturbation in that region is
proportional to the fraction of its kinetic energy there. That is the right
first-order structure of the problem (the kernel is an energy-weighted average),
but the *sign* is opposite to the perturbation: a slower region lengthens the
period.

**Upper or lower bound?** It is neither: it is an estimate whose error is the
difference between the true sensitivity kernel and the energy fraction. For a
localised perturbation the two can differ by a factor of a few, so the estimate
should be quoted with a factor-of-two caveat and checked against a perturbed
model run.

---

## ★★★7 — Separating $R$ from $\alpha$

**Observable 1: a mode period.** Gives a constraint on $R/\alpha$ for a kernel
that weights the region where the mode's energy sits. Two modes with different
kernels give two different weighted averages, hence information about the *shape*
of the profile, not just its ratio — but both still scale with $R$.

**Observable 2: a mass or moment-of-inertia constraint.** The total mass
$M = \int4\pi\rho r^{2}\,\mathrm{d}r$ and the polar moment of inertia
$C = \int\tfrac{8}{3}\pi\rho r^{4}\,\mathrm{d}r$ are absolute quantities with no
$\alpha$ in them, so they fix the radial scale and the density distribution. With
$M$, $C$ and the mass-weighted moment $J_2$ from gravity, the *size* of the body
is determined independently of any seismic speed.

**Observable 3 (optional): a normal-mode period *plus* a travel time.** A travel
time gives $\int\mathrm{d}r/\alpha(r)$ along a path with a different weighting;
combining it with a period removes part of the degeneracy without a density
constraint.

The defensible answer names the degeneracy explicitly and shows which observable
breaks each leg of it.

---

## ★★★8 — Why self-gravitation matters for the gravest modes

**The extra term.** A displacement that moves mass changes the gravitational
potential; the resulting force,
$-\rho\nabla\phi'$, must be added to the elastic restoring force, and $\phi'$
satisfies Poisson's equation coupled to the displacement (the "sixth-order"
system in place of the fourth-order elastic one). The restoring force is then a
sum of an elastic part and a buoyancy-like gravitational part.

**Why the density distribution enters.** The gravitational part of the restoring
force depends on $\rho$, on $g(r)$ and on how the displaced mass redistributes —
none of which appear in the purely elastic problem. For the gravest spheroidal
modes of a planet, these two contributions are comparable (which is why the
long-period "football" mode is at the wrong period by tens of per cent if
self-gravitation is omitted). Radial modes are affected much less, because the
spherically symmetric redistribution of mass leaves the external field unchanged.

**What carries unique density information.** The splitting of a mode into a
multiplet, and the free-wobble frequency, both depend on the equatorial and polar
moments of inertia — quantities a body-wave travel time cannot sense at all. This
is precisely why
[12-06 Geodetic Constraints on the Interior](../../06-geodesy-constraints-interior/README.md)
treats the moment of inertia, the figure and the nutation parameters as the
density observables of global geophysics.

---

## What a good answer looks like

Every period came with its model, every convergence claim came with its error
ratios, and no sensitivity estimate was presented without stating whether it was
a bound or an estimate.
