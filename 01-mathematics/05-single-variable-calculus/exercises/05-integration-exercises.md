# Exercises — 01-05-05 Integration Techniques and Definite Integrals

Attempt these **closed-book** before opening the
[solutions](./05-integration-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Evaluate:

(a) $\displaystyle\int_0^{2}\left(3x^{2}-2x\right)dx$
(b) $\displaystyle\int_1^{e}\frac{dx}{x}$
(c) $\displaystyle\int_0^{1}xe^{-x}\,dx$
(d) $\displaystyle\int\frac{dz}{z^{2}+4}$

---

**★2.** For each result in ★1, check it by (i) differentiating the antiderivative and
(ii) checking the units of the integrand times the differential against the units of
the answer.

---

## ★★ Applied

**★★3.** A sediment column has porosity $\phi(z) = 0.55\,e^{-z/800}$ (SYNTHETIC),
grain density $2650\ \mathrm{kg\,m^{-3}}$ and pore-fluid density
$1030\ \mathrm{kg\,m^{-3}}$.

(a) Derive the mass per unit area to depth $H$ in closed form.
(b) Evaluate it for $H = 2000$ m.
(c) Compute the relative error of the trapezoid rule with $n = 10$ and with
$n = 20$, and state the ratio between them.
(d) Use the trapezoid error formula to find the $\xi$ in $(0,H)$ that would make the
error formula exact for $n = 10$, and confirm that it lies in the interval.

---

**★★4.** A spherical body of radius 500 m has a density contrast of
$+250\ \mathrm{kg\,m^{-3}}$ with its surroundings.

(a) Write the excess mass as an integral with the correct differential and evaluate
it.
(b) The gravity anomaly of this body is measured 2 km above its centre. State, using
the language of the mean-value discussion in the lesson, why the data constrain the
excess mass but not the density contrast.
(c) Compute $I/(MR^{2})$ for this body if the density were uniform over the sphere
(it is a uniform sphere, so the answer is a number you know). Explain why this
quantity is useless for a body of this size and shape, and useful for a planet.

---

## ★★★ Research-oriented

**★★★5.** A layer has thermal conductivity that decreases with depth,
$k(z) = k_0(1 - \beta z)$ with $z$ measured downward and $\beta > 0$ small.

(a) Show that a *constant* upward heat flux $q$ implies the geotherm

$$T(z) = T_0 - \frac{q}{k_0\beta}\ln(1-\beta z),$$

and verify that it satisfies $q = k(z)\,dT/dz$.
(b) Find the depth at which the temperature has risen by 100 K for
$k_0 = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$, $\beta = 0.01\ \mathrm{km^{-1}}$, and compare
with the constant-conductivity result for the same $q$.
(c) Explain in one sentence which physical assumption is doing the work in the
comparison.

---

**★★★6.** The mean value theorem for integrals says that for continuous $f$ there is
a $c \in [a,b]$ with $\int_a^b f = f(c)(b-a)$.

(a) For the linear geotherm $T(z) = T_0 + \Gamma z$, find $c$ and show it is the
midpoint.
(b) For a geotherm with curvature, $T(z) = T_0 + \Gamma z - \Delta e^{-z/\lambda}$,
find the mean over $[0,H]$ and show that it is *not* $(T(0)+T(H))/2$.
(c) Compute both for $T_0 = 10$ °C, $\Gamma = 25\ \mathrm{K\,km^{-1}}$,
$\Delta = 5$ °C, $\lambda = 500$ m, $H = 3$ km, and state the difference. Then explain
why a single measured heat flux at the surface cannot distinguish the two geotherms.

---

## Extension ideas

- Derive the error constant of the midpoint rule for $\int_0^H T(z)\,dz$ with the
  linear geotherm and confirm that the rule is exact for it.
- Write a program that integrates the compaction density profile with Simpson's rule
  and reports the number of panels required for a relative error below $10^{-10}$.
  Compare with the trapezoid requirement.
- Evaluate $\int_0^{R}4\pi\rho r^{2}\,dr$ for a two-layer Earth model (core 3480 km at
  11000 kg/m³, mantle to 6371 km at 4400 kg/m³) and compare the mass with the closed
  form $M = \frac{4}{3}\pi\left(\rho_c r_c^{3} + \rho_m(R^{3}-r_c^{3})\right)$.
