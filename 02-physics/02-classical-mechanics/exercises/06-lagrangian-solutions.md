# Solutions — 02-02-06 Lagrangian and Hamiltonian Formulations

> **Read this after attempting the exercises, not before.**
>
> Numbers computed with $g = 9.82025\ \mathrm{m\,s^{-2}}$.

---

## ★1 — Euler–Lagrange for three Lagrangians

**(a)** $L = \tfrac12m\dot x^{2} - \tfrac12kx^{2}$:
$\partial L/\partial\dot x = m\dot x$, $\partial L/\partial x = -kx$, so

$$m\ddot x = -kx:$$

a harmonic oscillator with $\omega = \sqrt{k/m}$.

**(b)** $L = \tfrac12ml^{2}\dot\theta^{2} + mgl\cos\theta$:
$\partial L/\partial\dot\theta = ml^{2}\dot\theta$,
$\partial L/\partial\theta = -mgl\sin\theta$, so

$$\ddot\theta = -\frac{g}{l}\sin\theta:$$

the nonlinear pendulum. Note the sign convention: with $\theta$ from the
downward vertical, $V = -mgl\cos\theta$ and the *potential energy* is negative at
the bottom — a reminder that $L = T - V$ and that the zero of $V$ is a choice.

**(c)** $L = \tfrac12m\dot x^{2} - mgx$:
$m\ddot x = -mg$, i.e. free fall with $g$ positive upward. Setting $x$ upward
makes the equation read $\ddot x = -g$, which is the sign convention of a
height-positive coordinate system.

---

## ★2 — Pendulum at 10° with $l = 1$ m

**(a)** $T_0 = 2\pi\sqrt{l/g} = \mathbf{2.005019\ s}$.

**(b)** Exact: $T = 4\sqrt{l/g}\,K(\sin^{2}5°) = \mathbf{2.008843\ s}$, so the
small-angle form is low by
$(2.008843-2.005019)/2.008843 = \mathbf{0.1904\%}$.

**(c)** The 1% boundary: solving the exact period numerically, the error is
0.9208% at 22°, **1.006% at 23°**, 1.0956% at 24°. So **about 23°** is the 1%
limit. (The two-term series
$1+\theta^{2}/16+11\theta^{4}/3072$ crosses 1% at
$\theta = 0.4$ rad $= 22.9°$, in agreement.)

---

## ★3 — Cyclic coordinates

**(a)** All three coordinates are cyclic: $p_x$, $p_y$, $p_z$ are conserved — the
three components of linear momentum. The symmetry is translational invariance
(homogeneity of space).

**(b)** Only $\theta$ is cyclic: $p_\theta = mr^{2}\dot\theta = l$ is conserved —
angular momentum. The symmetry is rotational invariance. Note that $r$ is *not*
cyclic even though the potential depends on it alone in a specific way; the
conservation of energy (not of $p_r$) is what constrains the radial motion.

**(c)** Neither $\theta$ nor $\dot\theta$ is absent from $L$, so there is no
cyclic coordinate — but $L$ has no explicit time dependence, so the
**Hamiltonian** is conserved. This is the important distinction: a cyclic
coordinate gives a momentum, absence of explicit time dependence gives energy.

---

## ★4 — Legendre transform in polar coordinates

**(a)** $L = \tfrac12m(\dot r^{2} + r^{2}\dot\theta^{2}) - V(r,\theta)$.

**(b)** $p_r = \partial L/\partial\dot r = m\dot r$;
$p_\theta = \partial L/\partial\dot\theta = mr^{2}\dot\theta$.

**(c)** $H = p_r\dot r + p_\theta\dot\theta - L
= \frac{p_r^{2}}{2m} + \frac{p_\theta^{2}}{2mr^{2}} + V(r,\theta)$.

Since the kinetic energy was quadratic in the velocities, $H = T + V$: the total
energy.

**(d)** $p_\theta = mr^{2}\dot\theta$ **is** the angular momentum about the origin
(units kg m² s⁻¹), while $p_r = m\dot r$ is an ordinary linear momentum. This is
the point of §6 of the lesson: generalised momentum carries the units of its
coordinate, so the *units* tell you which conserved quantity you are looking at.

---

## ★★5 — Bead on a rotating hoop

**(a)** With $\theta$ from the bottom,
$$L = \tfrac12mR^{2}\dot\theta^{2} + \tfrac12mR^{2}\omega^{2}\sin^{2}\theta
- mgR(1-\cos\theta),$$
so
$$V_{\text{eff}}(\theta) = mgR(1-\cos\theta)
- \tfrac12mR^{2}\omega^{2}\sin^{2}\theta.$$

**(b)** $\omega_c = \sqrt{g/R} = \sqrt{9.82025/0.5} = \mathbf{4.4318\ rad\,s^{-1}}$.

**(c)** $\cos\theta^{\ast} = g/(\omega^{2}R) = 9.82025/(64\times0.5) = 0.30688$,
so $\theta^{\ast} = \arccos(0.30688) = \mathbf{72.1285°}$. (The lesson's
demonstration, which minimises $V_{\text{eff}}$ numerically at a 0.009° grid
spacing, found 72.129° at this $\omega$ — agreement to the grid.)

**(d)** As $\omega$ falls below $\omega_c$, $\cos\theta^{\ast} > 1$ has no
solution, the only equilibrium is $\theta = 0$, and it becomes the global
minimum. The tilted equilibria are born in a **pitchfork bifurcation** at
$\omega = \omega_c$: two symmetric branches appear, one on each side, out of a
single symmetric state. This is a canonical symmetry-breaking bifurcation, and it
appears whenever a symmetric state loses stability to a symmetric pair.

---

## ★★6 — Two coupled oscillators

**(a)** With displacements $x_1, x_2$ from equilibrium,
$$L = \tfrac12m(\dot x_1^{2}+\dot x_2^{2})
- \tfrac12k(x_1^{2}+x_2^{2}) - \tfrac12k_c(x_2-x_1)^{2}.$$

**(b)** The equations are
$m\ddot x_1 = -kx_1 + k_c(x_2-x_1)$ and
$m\ddot x_2 = -kx_2 - k_c(x_2-x_1)$. Adding and subtracting:

$$m(\ddot x_1+\ddot x_2) = -k(x_1+x_2), \qquad
m(\ddot x_1-\ddot x_2) = -(k+2k_c)(x_1-x_2),$$

so the normal-mode frequencies are

$$\omega_1 = \sqrt{\frac{k}{m}} = \sqrt{4/1} = \mathbf{2.000\ rad\,s^{-1}},
\qquad
\omega_2 = \sqrt{\frac{k+2k_c}{m}} = \sqrt{6/1} = \mathbf{2.449\ rad\,s^{-1}}.$$

**(c)** Mode 1: $x_1 = x_2$ — the two masses move **together**, the coupling
spring never stretches, and the coupling stiffness is invisible (hence
$\omega_1$ is unchanged by $k_c$). Mode 2: $x_1 = -x_2$ — the masses move in
**opposition**, the coupling spring is stretched twice as much, and the effective
stiffness is $k+2k_c$.

**(d)** A system with $n$ degrees of freedom has exactly $n$ normal modes. Here
$n = 2$. The count is a rank statement (the mass and stiffness matrices are
$n\times n$), and it is why the normal-mode structure of a continuum — a
seismogram, the Earth's free oscillations — is indexed by an integer triplet.

---

## ★★7 — Effective potential for $V = -\alpha/r$

**(a)** $V_{\text{eff}}' = -l^{2}/(mr^{3}) + \alpha/r^{2} = 0$ gives
$r_0 = l^{2}/(m\alpha)$. With $\alpha = m = l = 1$ (SI-compatible round numbers):
$r_0 = \mathbf{1.0}$.

**(b)** $V_{\text{eff}}'' = 3l^{2}/(mr^{4}) - 2\alpha/r^{3}$. At $r_0$, using
$l^{2}/(mr_0) = \alpha$:

$$V_{\text{eff}}''(r_0) = \frac{3l^{2}}{mr_0^{4}} - \frac{2\alpha}{r_0^{3}}
= \frac{1}{r_0^{3}}\left(\frac{3l^{2}}{mr_0} - 2\alpha\right)
= \frac{\alpha}{r_0^{3}} > 0,$$

so the extremum is a **minimum**: the circular orbit is stable. (Beware the common
error of computing only the first term: $3l^{2}/(mr_0^{4})$ alone is *not*
$V_{\text{eff}}''$.)

**(c)** The small-oscillation frequency is
$\omega_r = \sqrt{V_{\text{eff}}''(r_0)/m} = \sqrt{\alpha/(mr_0^{3})}$.
With the round numbers, $\omega_r = \sqrt{1} = 1$ rad s⁻¹. The orbital frequency is
$\omega_{\text{orb}} = l/(mr_0^{2}) = 1$ rad s⁻¹. **They are equal.**

**(d)** The equality is special to the inverse-square law: for $V \propto r^{n}$
with $n = -1$, the radial and angular frequencies coincide, so a perturbed orbit
returns to its starting point after one radial oscillation — the orbit **closes**
into an ellipse and does not precess. This is Bertrand's theorem in action. For
any other power, $\omega_r/\omega_{\text{orb}} \ne 1$ and the orbit is a
precessing rosette; the $J_2$ oblateness of the Earth does exactly this to
satellite orbits, which is why the apsidal precession rate is a measured
observable ([02-02-07](../07-central-forces.md) §4.2).

---

## ★★8 — Integrator behaviour

**(a)** The lesson's demonstration gives, for the harmonic oscillator integrated to
$t = 200$ with the exact energy 0.5:

| $\Delta t$ | explicit Euler | implicit Euler | leapfrog |
|---|---|---|---|
| 0.1 | $2.196\times10^{8}$ | 0.000000 | 0.499140 |
| 0.01 | 3.694159 | 0.067674 | 0.499990 |
| 0.001 | 0.610701 | 0.409365 | 0.500000 |

Only **leapfrog** keeps the energy bounded; explicit Euler pumps energy in
without limit and implicit Euler bleeds it away.

**(b)** Leapfrog is **symplectic**: its one-step map preserves the same
symplectic form (phase-space area) as the exact flow, and a symplectic map has a
modified conserved quantity (a "shadow" Hamiltonian) close to the true energy, so
the computed energy oscillates in a bounded band instead of drifting.

**(c)** Any long-time Hamiltonian integration: orbit propagation for GNSS or a
geodesy satellite, molecular dynamics of a mantle mineral at high pressure, or
long-time integrations of a seismic wavefield where the total energy must not
drift over millions of steps.

---

## ★★★9 — The elastic wave equation from a Lagrangian density

**(a)** Let $u(x,t)$ be the axial displacement of a rod of density $\rho$,
cross-section $A$ and Young's modulus $E$. The kinetic energy density (per unit
volume) is

$$\mathcal{T} = \tfrac12\rho\dot u^{2},$$

and the strain energy density for a linearly elastic rod with strain
$\varepsilon = \partial u/\partial x$ is

$$\mathcal{V} = \tfrac12E\varepsilon^{2} = \tfrac12E\left(\frac{\partial u}{\partial x}\right)^{2}.$$

**(b)** The Lagrangian density and action are

$$\mathcal{L} = \tfrac12\rho\dot u^{2} - \tfrac12E\left(\frac{\partial u}{\partial x}\right)^{2},
\qquad
S = \int\!\!\int\mathcal{L}\,dx\,dt.$$

Varying with $\delta u$ vanishing at the boundary and integrating by parts in both
variables:

$$\delta S = \int\!\!\int\left[-\rho\ddot u + E\,\frac{\partial^{2}u}{\partial x^{2}}\right]\delta u\,dx\,dt = 0
\;\Longrightarrow\;
\rho\frac{\partial^{2}u}{\partial t^{2}} = E\frac{\partial^{2}u}{\partial x^{2}}.$$

**(c)** This is the wave equation with $c^{2} = E/\rho$, so
$c = \sqrt{E/\rho}$ — the bar-speed formula. Dimensionally
$\sqrt{(\mathrm{M\,L^{-1}T^{-2}})/(\mathrm{M\,L^{-3}})} = \mathrm{L\,T^{-1}}$ ✓.

**(d)** Assumptions: **linearity** (strain energy quadratic in strain, i.e. small
strain — it fails as the rock approaches failure, and it fails for a
stress–strain curve with hysteresis even at small strain, which is anelasticity);
**locality** (the energy at a point depends only on the strain at that point,
which fails at high frequency when the wavelength approaches the grain or
fracture scale, giving dispersion); **isotropy and homogeneity** (fails in
bedded or fractured rock, giving anisotropy and the P/S discrepancy used in
exploration seismology); and **no dissipation** (fails in all real rock, which is
why $Q$ exists as a separate parameter). Each of these is the subject of
[02-04 Elasticity](../../04-elasticity-and-continuum-mechanics/README.md) and
[02-03-10 Attenuation](../../03-oscillations-and-waves/10-attenuation.md).

---

## ★★★10 — Ten-year orbit integration

**(a)** The **symplectic (leapfrog)** scheme conserves the orbital energy in the
bounded sense, because it preserves the symplectic structure of the Hamiltonian
flow (the phase-space area) and therefore has a nearby conserved "shadow"
Hamiltonian. RK4 preserves no such structure, so although its local error is
smaller, it can accumulate secularly in the energy and the semi-major axis.

**(b)** Over one orbit RK4's truncation error is typically orders of magnitude
smaller than leapfrog's, so any single-orbit comparison favours RK4. Over years
the error *type* matters more than its size: RK4's energy error grows
(secularly or randomly, depending on the problem), while leapfrog's oscillates
within a band fixed by the step size. A satellite's orbit is determined by its
energy and its angular momentum, so a drifting energy is a drifting semi-major
axis — exactly the quantity the mission measures.

**(c)** Plot the **relative energy error** $[E(t)-E(0)]/E(0)$ (or the osculating
semi-major axis, or the total angular momentum) against time over the ten years.
Expectation: for RK4, a trend — small at first, growing systematically (or a
random walk, depending on the perturbation model); for leapfrog, bounded
oscillations with no trend, at a level set by the step size. The second
diagnostic is a convergence check: halving $\Delta t$ should shrink the leapfrog
band, and should shrink the RK4 error only if the step is small enough that
truncation, rather than structure, dominates.
