# Exercises — 02-01-04 Conservation Laws as the Engine of Physical Modelling

Attempt these **closed-book** before opening the
[solutions](./04-conservation-laws-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Use $G = 6.674\,30\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$,
$GM_\oplus = 3.986\,004\,418\times10^{14}\ \mathrm{m^3\,s^{-2}}$ (defining),
$\omega = 7.292\,115\times10^{-5}$ rad s⁻¹ (defining) and
$R_\oplus = 6371$ km (nominal).

---

## ★ Foundational

**★1.** For each quantity, say whether it obeys a *conservation law* or a
*balance law* in the stated system, and give the source term if there is one:
(a) mass in a closed aquifer; (b) entropy in an irreversible process;
(c) energy in a system with a radiogenic heat source; (d) electric charge;
(e) linear momentum of the Earth alone, during an earthquake.

---

**★2.** Write the master balance equation and, for each of mass, energy
(heat) and electric charge, state the dimension of every term. Confirm all three
terms of each equation have the same dimension.

---

**★3.** Blocks of $m_1 = 4$ kg and $m_2 = 1$ kg move on a frictionless line with
$u_1 = +2$ m/s and $u_2 = -3$ m/s.

(a) Compute the total momentum and kinetic energy.
(b) For a perfectly elastic collision, compute $v_1$ and $v_2$ and verify both
conservation laws.
(c) For a perfectly inelastic collision, compute the common velocity, the
kinetic energy, and the energy lost as a fraction.

---

**★4.** A 1-D advection problem is discretised two ways: in flux (upwind) form
and in advective (centred-difference) form. (a) Explain which one conserves the
total exactly and why. (b) The flux form's relative mass drift after 1000 steps
is $3.1\times10^{-16}$ and the advective form's is $1.5\times10^{-1}$. Interpret
both numbers. (c) Does the flux form's conservation imply accuracy? Explain.

---

## ★★ Applied

**★★5.** Two bodies attract gravitationally with $m_1 = GM_\oplus/G$ and
$m_2 = 10^{22}$ kg, separated by $10^{7}$ m, with $m_1$ initially at rest and
$m_2$ moving perpendicular to the separation at the circular speed.

(a) Compute $m_1$, the circular speed, and the orbital period from Kepler's third
law.
(b) Explain why the total momentum is constant, in terms of the accelerations.
(c) If your computation reports a residual of $1.2\times10^{11}$ kg m/s against a
momentum scale of $6.3\times10^{25}$ kg m/s, is momentum conserved? Justify your
normalisation.

---

**★★6.** (a) Compute the moment of inertia of a uniform sphere of mass
$M = 5.972\times10^{24}$ kg and radius $R = 6371$ km, and its angular momentum
and rotational energy at $\omega = 7.292\,115\times10^{-5}$ rad s⁻¹.
(b) Repeat with a two-layer model value $I = 8.4699\times10^{37}$ kg m².
(c) For the two-layer model, compute the change in angular momentum and in
rotational energy when the length of the day increases by exactly 1 ms.
(d) A student claims this energy "is radiated as seismic energy". Critique the
claim in two sentences.

---

**★★7.** Derive the heat equation $\rho c\,\partial_tT =
\nabla\cdot(k\nabla T) + H$ from the energy balance
$\partial_t(\rho cT) + \nabla\cdot\mathbf{q} = H$ with $\mathbf{q} = -k\nabla T$.
(a) State the two assumptions. (b) Write the dimension of every term of the final
equation and verify homogeneity. (c) For $\rho c = 2.16\times10^{6}\
\mathrm{J\,m^{-3}K^{-1}}$, evaluate the temperature change in one year produced
by $H = 10^{-6}\ \mathrm{W\,m^{-3}}$ with no conduction.

---

**★★8.** Prove that a flux-form finite-volume update on a periodic 1-D grid
conserves the cell-average sum exactly. (a) Write the update. (b) Sum over all
cells and show the telescoping. (c) State where the proof uses periodicity, and
what changes with a closed (no-flux) boundary.

---

## ★★★ Research-oriented

**★★★9.** Conservation laws are necessary but not sufficient for a unique
model. (a) State Newton's shell theorem. (b) Explain why a uniform spherical
shell adds nothing to the external field but does add mass. (c) Construct two
spherically symmetric mass distributions with the same total mass that produce
identical external fields, and explain why the degeneracy is exact rather than
approximate. (d) Say what extra measurement breaks the degeneracy.

---

**★★★10.** The seismic moment is defined by $M_0 = \mu A D$. (a) Compute $M_0$
for $\mu = 3\times10^{10}$ Pa, $A = 5\times10^{7}$ m² and $D = 0.5$ m.
(b) Using $E_s = (\Delta\sigma/2\mu)M_0$ with $\Delta\sigma = 3\times10^{6}$ Pa,
compute $E_s$. (c) A student adds $E_s$ to the Earth's rotational energy budget
as if it were a direct subtraction from $I\omega^{2}/2$. Explain two separate
things wrong with that procedure. (d) Explain why an explosion source radiates
seismic waves but injects zero net linear momentum.
