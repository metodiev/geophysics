# Exercises — 02-04-01 Stress: Traction, Cauchy Stress Tensor and Equilibrium

Attempt these **closed-book** before opening the
[solutions](./01-stress-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/stress_demo.py`](../code/stress_demo.py) require
you to run it and report its actual output. Use the compression-positive
convention throughout and state it in your answers.

---

## ★ Foundational

**★1.** A stress state (MPa, compression positive) is
$\sigma_{11} = 50$, $\sigma_{22} = 20$, $\sigma_{33} = 10$, $\sigma_{12} = -15$,
all other components zero.

(a) Compute the traction on the plane with normal $\hat{n} = (1,0,0)$ and on
$\hat{n} = (1,1,0)/\sqrt2$.
(b) Compute the normal and shear components of each traction.
(c) Verify that the traction on $-\hat{n}$ is the negative of that on $\hat{n}$.
(d) State which plane carries the greater shear traction.

---

**★2.** For the same tensor:

(a) Compute the three invariants.
(b) Compute the principal stresses by solving the characteristic cubic.
(c) Identify the principal directions (the in-plane rotation angle is enough).
(d) Compute the maximum shear stress over all planes.

---

**★3.** Show that the traction on a plane whose normal makes an angle $\theta$ with
the greatest principal stress has normal stress
$\sigma_n = ((\sigma_1+\sigma_3)/2) + ((\sigma_1-\sigma_3)/2)\cos2\theta$ for a
2-D state with $\sigma_2 = (\sigma_1+\sigma_3)/2$.

(a) Derive the expression.
(b) Derive the corresponding expression for the shear stress $\tau$.
(c) Show that the maximum of $\tau$ occurs at $\theta = 45^\circ$ and equals
$(\sigma_1-\sigma_3)/2$.
(d) State what the "$\sigma_2 = (\sigma_1+\sigma_3)/2$" restriction does to the
result and why it matters for 3-D states.

---

**★4.** Compute the lithostatic and effective stress at 1, 5, 10, 20 and 30 km for
$\rho = 2650\ \mathrm{kg\,m^{-3}}$, $g = 9.81\ \mathrm{m\,s^{-2}}$, and hydrostatic
pore pressure with $\rho_w = 1030\ \mathrm{kg\,m^{-3}}$.

(a) Tabulate the total and effective vertical stresses.
(b) Compute the effective-stress gradient.
(c) Repeat the calculation for an overpressured case with $p_f$ equal to 60 per
cent of the lithostatic stress, and state the effect on the effective gradient.
(d) State which assumption in (c) is a model and how it would be measured in
practice.

---

## ★★ Applied

**★★5.** Run the demo and use its printed stress tensor.

(a) Report the three principal stresses and the three invariants from both routes.
(b) Report the measured residual shear on the principal planes and state what it
demonstrates.
(c) Report the mean stress, $J_2$ and the von Mises stress.
(d) Compute by hand the ratio of the deviatoric magnitude to the mean stress and
state what the ratio implies about the state's proximity to failure.

---

**★★6.** A borehole is drilled in a stress field with
$\sigma_v = 25$ MPa km⁻¹ depth, $\sigma_H = 1.5\sigma_v$ and
$\sigma_h = 0.8\sigma_v$, with hydrostatic pore pressure
($\rho_w = 1000\ \mathrm{kg\,m^{-3}}$).

(a) Write out the effective stress tensor at 3 km depth, choosing coordinates with
$x$ along $\sigma_H$, $y$ along $\sigma_h$ and $z$ vertical.
(b) Determine which of $\sigma_1$, $\sigma_2$, $\sigma_3$ is vertical and hence
which Anderson regime applies.
(c) Compute the maximum shear stress on any plane.
(d) State which plane in the borehole wall would be most likely to fail in shear
and why (a qualitative answer in terms of the stress concentration is enough).

---

**★★7.** Run the demo's Mohr-circle section.

(a) Report the circle centre, radius and the maximum deviation measured.
(b) Verify by hand that the eight tabulated $(\sigma_n,\tau)$ pairs lie on the
circle.
(c) Report the maximum shear stress measured over the scanned planes and compare
with $(\sigma_1-\sigma_3)/2$.
(d) Explain why the shear stress on the plane at 45° is 40 MPa rather than the
50 MPa maximum, given the angle dependence derived in ★3.

---

**★★8.** A stress state is measured as
$\sigma_{11} = 80$, $\sigma_{22} = 60$, $\sigma_{33} = 40$, $\sigma_{12} = 10$,
$\sigma_{13} = -5$, $\sigma_{23} = 8$ MPa.

(a) Compute all three invariants.
(b) Compute the three principal stresses numerically (a program is acceptable).
(c) Report the invariants computed from the eigenvalues and compare.
(d) Compute the decomposition into isotropic and deviatoric parts and report
$\sigma_{\text{vM}}$.

---

## ★★★ Research-oriented

**★★★9.** A horizontal layer of rock at depth $z$ is loaded by a vertical stress
and confined laterally so that no lateral strain occurs (uniaxial strain).

(a) Using an isotropic elastic constitutive law (lesson 02-04-03), show that the
lateral stress is $\sigma_h = \frac{\nu}{1-\nu}\sigma_v$.
(b) For $\nu = 0.25$ and a lithostatic vertical stress, compute the lateral
stresses at 1, 5 and 10 km.
(c) Compute the deviatoric stress tensor and $J_2$ at each depth, and state
whether $J_2$ grows linearly with depth.
(d) Explain the geophysical significance: which regime (in the Anderson
classification) does this state correspond to, and what would it take to change
it?

---

**★★★10.** Stress in a sphere under its own gravity.

(a) Show that the gravitational acceleration inside a uniform sphere of density
$\rho$ at radius $r$ is $g(r) = \frac{4}{3}\pi G\rho r$.
(b) Solve the equilibrium equation in spherical symmetry for the pressure, and show
that $p(r) = \frac{2}{3}\pi G\rho^2(R^2-r^2)$.
(c) Evaluate the central pressure for $\rho = 5510\ \mathrm{kg\,m^{-3}}$ and
$R = 6.371\times10^6$ m and compare with the actual central pressure of the Earth
(about 364 GPa) — explain the sign and magnitude of the discrepancy in terms of the
constant-density assumption.
(d) State which additional physics (self-compression, composition) is required for
a realistic Earth model, and name one reference model that provides it (with a
citation you have verified).

Report measured values only if you verify them numerically, and state which of
your results are analytic.
