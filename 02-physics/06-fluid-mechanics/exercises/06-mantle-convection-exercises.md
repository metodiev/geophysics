# Exercises — 02-06-06 Mantle Convection and Rayleigh-Benard Instability

Attempt these **closed-book** before opening the
[solutions](./06-mantle-convection-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/mantle_convection_demo.py`](../code/mantle_convection_demo.py) require
you to run it and report its actual output. Use $g = 9.81\
\mathrm{m\,s^{-2}}$ unless told otherwise.

---

## ★ Foundational

**★1.** Compute the Rayleigh number for each of the following, showing every
factor:

(a) the mantle: $\rho = 3300$, $\alpha = 3\times10^{-5}$, $\Delta T = 2500$,
$d = 2.891\times10^6$, $\kappa = 10^{-6}$, $\eta = 10^{21}$ (SI units).
(b) a water tank: $\rho = 1000$, $\alpha = 2\times10^{-4}$, $\Delta T = 20$,
$d = 1$, $\kappa = 1.4\times10^{-7}$, $\eta = 10^{-3}$.
(c) a magma chamber of $d = 10^3$ m with $\rho = 2500$, $\alpha = 3\times10^{-5}$,
$\Delta T = 100$, $\kappa = 10^{-6}$, $\eta = 10^{3}$.
(d) State which of the three is most supercritical, using $Ra_c = 657.5$ as the
stress-free reference.

---

**★2.** Derive the marginal-stability condition for stress-free boundaries.

(a) State the boundary conditions on $W$ and show that $W = \sin(n\pi z)$
satisfies them.
(b) Show that the eigenvalue condition is
$Ra = (n^2\pi^2+a^2)^3/a^2$.
(c) Show that the minimum over $a$ occurs at $a_c = \pi/\sqrt2$ for $n = 1$.
(d) Evaluate $Ra_c = 27\pi^4/4$ numerically.

---

**★3.** The critical wavenumber is $a_c = \pi/\sqrt2 \approx 2.221$.

(a) Compute the corresponding aspect ratio $\lambda_c/d = 2\pi/a_c$.
(b) State in words what this predicts about the shape of convection cells at
onset.
(c) Repeat for rigid boundaries with $a_c \approx 3.117$ and compare.
(d) State why the aspect ratio is a *prediction* and the critical Rayleigh number
is a *threshold*.

---

**★4.** Boundary-layer scalings.

(a) Compute $\delta = d\,Ra^{-1/3}$ for the mantle with $Ra = 5.87\times10^7$
and $d = 2.891\times10^6$ m.
(b) Compute the local Rayleigh number of that layer and explain the answer.
(c) Compute $\delta_c = d(Ra_c/Ra)^{1/3}$ with $Ra_c = 657.51$ and state how it
differs from (a) and why.
(d) State which definition of "thermal boundary layer" you would use to compare
with a seismic estimate of the lithospheric thickness, and why.

---

## ★★ Applied

**★★5.** The mantle's Prandtl number.

(a) Compute $\nu = \eta/\rho$ for the mantle with $\eta = 10^{21}$ Pa s and
$\rho = 3300\ \mathrm{kg\,m^{-3}}$.
(b) Compute $Pr = \nu/\kappa$ with $\kappa = 10^{-6}$ m² s⁻¹.
(c) Compute the momentum diffusion time $d^2/\nu$ and the thermal diffusion time
$d^2/\kappa$ for $d = 2.891\times10^6$ m.
(d) Explain, in two sentences, why the enormous Prandtl number is exactly what
makes the Stokes approximation safe for the mantle — and why it also means the
mantle has no turbulent cascade.

---

**★★6.** Run
[`../code/mantle_convection_demo.py`](../code/mantle_convection_demo.py).

(a) Report the numerator, the denominator and $Ra$, and $\log_{10}Ra$.
(b) Report the ternary-search minimum, the analytic $\pi/\sqrt2$ and
$27\pi^4/4$, and state what the agreement demonstrates.
(c) Report the free-slip finite-difference values at $N = 20$, 40, 80 and the
error trend.
(d) Report the rigid-boundary values at $N = 40$ and 60, and the classical value
they approach.
(e) Report $Ra_\delta$ for $\delta = d\,Ra^{-1/3}$ and state why it is an
identity, not a result.

---

**★★7.** Nusselt number and heat flow.

(a) Compute $Nu = 0.1\,Ra^{1/3}$ for the mantle.
(b) Compute the implied surface heat flow with $k = 2.5\ \mathrm{W\,m^{-1}K^{-1}}$,
$\Delta T = 2500$ K and $d = 2.891\times10^6$ m.
(c) Compare with the handbook values of about 65 mW m⁻² (continental) and
100 mW m⁻² (oceanic).
(d) State which part of the $Nu$ relation is a scaling law and which is an
empirical coefficient, and what that means for the credibility of (b).

---

**★★8.** Sensitivity to viscosity. Recompute $Ra$, $\delta = d\,Ra^{-1/3}$,
$Nu$ and the velocity scale $u = (\kappa/d)Ra^{2/3}$ for
$\eta = 10^{19}$, $10^{20}$, $10^{21}$ and $10^{22}$ Pa s, with all other
inputs at their nominal values.

(a) Tabulate the four cases.
(b) State the powers of $\eta$ in each quantity.
(c) Convert $u$ to cm per year and compare with observed plate speeds of order
1–10 cm yr⁻¹.
(d) State which of the four cases gives the best agreement and what that implies
about the effective viscosity of the convecting mantle.

---

## ★★★ Research-oriented

**★★★9.** The Rayleigh number is often read as a ratio of timescales.

(a) Show that $Ra = \tau_{\text{diffusion}}/\tau_{\text{buoyancy}}$ with
$\tau_{\text{diffusion}} = d^2/\kappa$ and
$\tau_{\text{buoyancy}} = \eta/(\rho g\alpha\Delta T\,d)$.
(b) Compute both timescales for the mantle and verify the ratio equals your
answer to ★1(a).
(c) Show that the physical meaning of $Ra_c \sim 10^3$ is that convection starts
only when the buoyancy timescale is about a thousand times *shorter* than the
diffusion timescale.
(d) Simulate the same reasoning for a 1 m thick layer of the same material and
state whether it would convect on any timescale of interest.

---

**★★★10.** The mantle's viscosity is temperature-dependent, roughly
$\eta(T) = \eta_0\exp[E_a/(R_gT)]$ with an activation energy $E_a$ and gas constant
$R_g$ (see [02-04-07](../../04-elasticity-and-continuum-mechanics/07-viscoelasticity.md)).

(a) Taking $\eta_0$ such that $\eta = 10^{21}$ Pa s at $T = 1800$ K, and using
$R_g = 8.314\ \mathrm{J\,mol^{-1}K^{-1}}$, compute the ratio
$\eta(1500\ \mathrm{K})/\eta(2500\ \mathrm{K})$ for
$E_a = 3\times10^5\ \mathrm{J\,mol^{-1}}$.
(b) Describe qualitatively what such a viscosity contrast does to the planform of
convection.
(c) Explain why the *global* Rayleigh number is then no longer a single control
parameter, and what replaces it.
(d) Name two observations that a constant-viscosity Rayleigh–Bénard model cannot
reproduce and a variable-viscosity model can.
