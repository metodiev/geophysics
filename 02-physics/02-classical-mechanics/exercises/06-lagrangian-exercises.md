# Exercises — 02-02-06 Lagrangian and Hamiltonian Formulations

Attempt these **closed-book** before opening the
[solutions](06-lagrangian-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Use $g = 9.82025\ \mathrm{m\,s^{-2}}$ unless stated otherwise. State a regime of
validity with every numerical answer in ★★ and ★★★.

---

## ★ Foundational

**★1.** For each Lagrangian, obtain the Euler–Lagrange equation and interpret it:
(a) $L = \tfrac12m\dot x^{2} - \tfrac12kx^{2}$;
(b) $L = \tfrac12ml^{2}\dot\theta^{2} + mgl\cos\theta$;
(c) $L = \tfrac12m\dot x^{2} - mgx$.

---

**★2.** For the pendulum of ★1(b) with $l = 1$ m: (a) state the small-angle
period; (b) compute the exact period at 10° and the error of the small-angle form;
(c) state the angle at which the error reaches 1%.

---

**★3.** Identify the cyclic coordinates and the conserved quantities:
(a) a free particle, $L = \tfrac12m(\dot x^{2}+\dot y^{2}+\dot z^{2})$;
(b) a particle in a central potential, $L = \tfrac12m(\dot r^{2}+r^{2}\dot\theta^{2})
- V(r)$;
(c) the pendulum of ★1(b) written with $\theta$ measured from the vertical.

---

**★4.** Perform the Legendre transform for a particle in a plane in polar
coordinates: (a) write $L$; (b) compute $p_r$ and $p_\theta$; (c) construct $H$
and show that it equals $T+V$; (d) identify which generalised momentum is the
angular momentum.

---

## ★★ Applied

**★★5.** A bead of mass 0.1 kg slides on a frictionless hoop of radius 0.5 m
rotating at constant $\omega$ about its vertical diameter.
(a) Write $L$ and the effective potential. (b) Compute the critical
$\omega_c = \sqrt{g/R}$. (c) Compute the equilibrium angle at $\omega = 8$ rad/s
from $\cos\theta^{\ast} = g/(\omega^{2}R)$. (d) State what happens to the
equilibrium as $\omega$ falls below $\omega_c$ and identify the type of
bifurcation.

---

**★★6.** Two equal masses $m = 1$ kg are connected by springs: each is attached
to a wall by a spring of stiffness $k = 4\ \mathrm{N\,m^{-1}}$, and they are
joined to each other by a spring of stiffness $k_c = 1\ \mathrm{N\,m^{-1}}$.
(a) Write $L$ in the two displacements. (b) Obtain the two normal-mode
frequencies. (c) Describe the motion of each mode. (d) State the general
principle that determines the number of modes.

---

**★★7.** The effective potential for a particle of mass $m$ and angular momentum
$l$ in a potential $V(r)$ is
$V_{\text{eff}} = l^{2}/(2mr^{2}) + V(r)$ with $V = -\alpha/r$.
(a) Find the radius of the circular orbit. (b) Show that it is stable by
computing $V_{\text{eff}}''$. (c) Compute the small-oscillation frequency about
the minimum and compare it with the orbital frequency. (d) State what the
coincidence (or lack of it) implies about the closure of the orbit.

---

**★★8.** (a) Integrate the harmonic oscillator with explicit Euler, implicit
Euler and leapfrog at $\Delta t = 0.1$ for 2000 steps and state which keeps the
energy bounded. (b) Explain in one sentence why the symplectic scheme behaves
differently. (c) State one geophysical integration where this choice matters.

---

## ★★★ Research-oriented

**★★★9.** Derive the one-dimensional elastic wave equation from a Lagrangian
density.

(a) Write the kinetic and strain energy densities for a rod of density $\rho$ and
Young's modulus $E$, with displacement field $u(x,t)$.
(b) Write $\mathcal{L}$ and the action, and vary it to obtain the equation of
motion.
(c) Show that the wave speed is $\sqrt{E/\rho}$.
(d) State which physical assumptions entered (linearity, locality, isotropy) and
one way each could fail in rock.

---

**★★★10.** A geodetic satellite is integrated for 10 years with (i) a
fourth-order Runge–Kutta scheme at a small step and (ii) a symplectic
(leapfrog) scheme at the same step.

(a) State which conserves the orbital energy in the *bounded* sense and why,
referring to the structure the scheme preserves.
(b) Explain why the RK4 scheme can have a smaller error over one orbit while
being worse over 10 years.
(c) State what diagnostic you would plot to demonstrate the difference, and what
you expect to see in each case.
