# Exercises — 02-03-05 Deriving the Wave Equation from Continuum Physics

Attempt these **closed-book** before opening the
[solutions](./05-wave-equation-derivation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/wave_equation_derivation_demo.py`](../code/wave_equation_derivation_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** A steel string of linear density $\mu = 0.020\ \mathrm{kg\,m^{-1}}$ is
under tension $T = 80$ N.

(a) Compute the transverse wave speed.
(b) Compute the wavelength of a 440 Hz wave on it.
(c) State which assumption of the derivation would fail first if the tension were
raised to 8000 N, and why.

---

**★2.** Derive the bar speed $\sqrt{E/\rho}$ from scratch, stating the two
assumptions.

(a) For a granite-like rock with $E = 73.6$ GPa and $\rho = 2700\
\mathrm{kg\,m^{-3}}$, compute $c_{\text{bar}}$.
(b) For the same rock with $\lambda = 25$ GPa and $\mu = 30$ GPa, compute $v_p$.
(c) Compute the ratio $v_p/c_{\text{bar}}$ and identify it as $\sqrt{M/E}$.
(d) Explain in two sentences why lateral inertia raises the speed.

---

**★3.** For $u_{tt} = c^2u_{xx}$ with $c = 2500$ m s⁻¹, domain
$x\in[0,3000]$ m and source width 60 m:

(a) What is the largest $\Delta x$ that resolves the source with at least 10
points per width?
(b) What is the largest $\Delta t$ for stability at that $\Delta x$?
(c) How many time steps are needed to reach $t = 0.5$ s?
(d) If the cost were reduced by doubling $\Delta x$ and keeping $\Delta t$ at the
new stability limit, what happens to the number of steps and to the error?

---

**★4.** Write down d'Alembert's solution for a string released from rest with
initial displacement $\phi(x) = e^{-x^2}$.

(a) Give the solution explicitly.
(b) Describe what you see at $t = 0$, at $t = 0.5$ and at $t = 2$ (in units where
$c = 1$).
(c) State the domain of dependence of the point $x = 0$ at $t = 1$.
(d) Explain why the maximum amplitude at large $t$ is half the initial maximum.

---

## ★★ Applied

**★★5.** Starting from conservation of momentum and mass for a fluid, derive
equation (8) of the lesson,
$\frac{1}{K}p_{tt} = \nabla\cdot\left(\frac{1}{\rho}\nabla p\right)$.

(a) Show that for constant $\rho$ it reduces to $p_{tt} = c^2\nabla^2p$ with
$c = \sqrt{K/\rho}$.
(b) Show that for a variable density the divergence form is the correct one, and
state what goes wrong if the constant-$\rho$ form is used across a density
contrast.
(c) For water with $K = 2.2$ GPa, $\rho = 1000\ \mathrm{kg\,m^{-3}}$ and for air
with $K = 1.42\times10^5$ Pa, $\rho = 1.225\ \mathrm{kg\,m^{-3}}$, compute both
sound speeds and comment on the ratio.

---

**★★6.** The demo's lattice section reports
$\omega = c(2/a)\sin(ka/2)$, $v_{\text{ph}} = c\sin(ka/2)/(ka/2)$ and
$v_g = c\cos(ka/2)$.

(a) Verify all three from the dispersion relation.
(b) Show that $v_{\text{ph}}v_g \le c^2$ with equality only as $ka\to0$.
(c) Compute the largest $ka$ at which $v_{\text{ph}}$ exceeds $0.99c$, and state
the corresponding number of grid points per wavelength.
(d) State the practical rule this gives for how many points per wavelength a
finite-difference wave simulation needs, and compare with the usual
"10 points per wavelength" rule of thumb.

---

**★★7.** Run the convergence study in the demo.

(a) Report the measured orders and state the code's demonstrated convergence.
(b) Explain why the error decreases by a factor of four when $\Delta x$ is halved
at fixed Courant number, even though $\Delta t$ is also halved.
(c) Extrapolate: what $\Delta x$ would be needed for a maximum error below
$10^{-9}$?
(d) State the cost of that improvement in time steps and in memory.

---

**★★8.** Run the stability study.

(a) Report the measured growth factor at $r = 1.05$ and $r = 1.20$ and compare
with $\left|2r^2-1\right| + \sqrt{(2r^2-1)^2-1}$.
(b) Explain why the observed value is slightly *below* the theoretical one.
(c) Show that at $r = 1$ the scheme is exact for this initial data and give the
one-sentence reason.
(d) For a 3-D simulation with the same stencil, state the stability limit and
compute the maximum $\Delta t$ for $\Delta x = 5$ m and $c = 3000$ m s⁻¹.
Compare with the 1-D value.

---

## ★★★ Research-oriented

**★★★9.** A layered medium has $c(x)$ varying with depth.

(a) Write the divergence-form wave equation $\rho u_{tt} =
\partial_x(\mu u_x)$ for a transversely varying medium and show that it reduces
to $u_{tt} = c^2u_{xx} + \ldots$ with an extra term proportional to the gradient
of the impedance.
(b) Show that the *impedance* $Z = \rho c$ is the quantity that should be
averaged (harmonically) at a discontinuity of properties, and explain why the
arithmetic average is wrong.
(c) Modify the demo's layered solver from the reflection lesson
([`../code/reflection_refraction_demo.py`](../code/reflection_refraction_demo.py))
to use the arithmetic average instead, and report the measured reflection
coefficient and its error compared with the theory
$R = (Z_1-Z_2)/(Z_1+Z_2)$.
(d) State the general lesson about averaging material properties in numerical
schemes.

---

**★★★10.** Choose a physical system *outside* this module — a stretched
membrane, a shallow-water channel, a transmission line, a plasma — and derive its
wave equation.

(a) Show that it has the form $u_{tt} = c^2\nabla^2u$ (or a close analogue with a
lower-order term) and identify the stiffness and inertia.
(b) Compute a numerical speed for representative parameters and check it against
a published value or a textbook estimate, citing the source.
(c) State which of the seven assumptions in §5 of the lesson that system
violates, and what observable consequence the violation has.
(d) Write a program that solves the system's wave equation with the explicit
scheme of this lesson, measures the numerical convergence order and reports the
Courant limit. State your measured values.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
