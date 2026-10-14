# Solutions — 02-01-04 Conservation Laws as the Engine of Physical Modelling

> **Read this after attempting the exercises, not before.**
>
> Arithmetic was computed. Where a number is measured rather than derived — the
> observed rates of Earth rotation change, for example — that is stated instead
> of quoted, because the lesson's rule is that a measured quantity must carry its
> provenance.

---

## ★1 — Conservation or balance

| | Classification | Source term |
|---|---|---|
| (a) mass in a closed aquifer | **conservation** in the closed system | none (internal redistribution only) |
| (b) entropy in an irreversible process | **balance** | $\sigma \ge 0$: entropy production, the second law |
| (c) energy with a radiogenic source | **balance** | $H$ (W m⁻³), production |
| (d) electric charge | **conservation** | none (no charge creation) |
| (e) Earth's momentum during an earthquake | **balance** *for the Earth alone* (external torques and the Moon's action); **conservation** for the Earth–Moon system | external torque; internal sources cancel |

**(e)** is the one that requires care. A double-couple seismic source contributes
zero net force and zero net torque, so it does not change the Earth's total
momentum. What it *does* redistribute is internal momentum, and if it changes
$I$ (by displacing mass) it changes $\omega$ at fixed $L$.

---

## ★2 — The master balance equation and term dimensions

$$\frac{\partial\phi}{\partial t} + \nabla\cdot\mathbf{J} = \sigma.$$

| Quantity | $[\phi]$ | $[\partial_t\phi]$ | $[\nabla\cdot\mathbf{J}]$ ($=\mathbf{J}$ per length) | $[\sigma]$ |
|---|---|---|---|---|
| mass | $\mathrm{M\,L^{-3}}$ | $\mathrm{M\,L^{-3}T^{-1}}$ | $(\mathrm{M\,L^{-2}T^{-1}})/\mathrm{L} = \mathrm{M\,L^{-3}T^{-1}}$ | 0 |
| energy (heat) | $\mathrm{M\,L^{-1}T^{-2}}$ | $\mathrm{M\,L^{-1}T^{-3}}$ | $(\mathrm{M\,T^{-3}})/\mathrm{L} = \mathrm{M\,L^{-1}T^{-3}}$ | $\mathrm{M\,L^{-1}T^{-3}}$ (W m⁻³) |
| charge | $\mathrm{I\,T\,L^{-3}}$ | $\mathrm{I\,L^{-3}}$ | $(\mathrm{I\,L^{-2}})/\mathrm{L} = \mathrm{I\,L^{-3}}$ | 0 |

(The energy density here is written as an energy per unit volume,
$\mathrm{J\,m^{-3}} = \mathrm{M\,L^{-1}T^{-2}}$, consistent with
$\rho cT$.) All three terms match in every row, which is the check.

---

## ★3 — Collisions

**(a)** $p = 4(2) + 1(-3) = 5$ kg m/s;
$\mathrm{KE} = \tfrac12(4)(4) + \tfrac12(1)(9) = 8 + 4.5 = 12.5$ J.

**(b)** Elastic 1-D:
$$v_1 = \frac{(m_1-m_2)u_1 + 2m_2u_2}{m_1+m_2}
= \frac{3(2) + 2(-3)}{5} = 0,$$
$$v_2 = \frac{(m_2-m_1)u_2 + 2m_1u_1}{m_1+m_2}
= \frac{(-3)(-3) + 2(4)(2)}{5} = \frac{9+16}{5} = 5\ \mathrm{m\,s^{-1}}.$$
Check: $p = 0 + 5 = 5$ ✓; $\mathrm{KE} = 0 + \tfrac12(1)(25) = 12.5$ J ✓.
**Both conserved.** (Note the elegant special case: the 4 kg block is stopped and
the 1 kg block leaves with five times the speed — because the collisions were
chosen so the momentum transfer is complete.)

**(c)** Inelastic: $v = p/(m_1+m_2) = 1$ m/s;
$\mathrm{KE} = \tfrac12(5)(1) = 2.5$ J. Loss $= 12.5 - 2.5 = 10.0$ J, i.e.
**80%**. Momentum is still exactly 5 kg m/s. In an inelastic collision, checking
energy conservation is checking the wrong law; the missing energy appears as
heat, sound and permanent deformation.

---

## ★4 — Flux form versus advective form

**(a)** The flux form conserves the total because each interior face flux enters
one cell's update with $+$ and its neighbour's with $-$; summing the updates
cancels every flux pairwise
(see ★8). The advective form discretises $\mathbf{v}\cdot\nabla\rho$, which is
algebraically equivalent in the continuum but carries no such discrete identity;
so the total drifts by an amount set by the scheme and $\Delta t$.

**(b)** $3.1\times10^{-16}$ is double-precision round-off: the identity holds
exactly in exact arithmetic, and the observed value is the accumulation of
floating-point rounding. $1.5\times10^{-1}$ — a 15% mass error after 1000 steps —
is a property of the discretisation, not of the computer; it would remain finite
in exact arithmetic, and it grows roughly linearly with the number of steps.

**(c)** No. Conservation and accuracy are independent properties. Upwind flux-form
advection conserves mass exactly while being only first-order accurate, so it
diffuses the profile strongly. Conversely, a high-order scheme can be accurate
and slightly non-conservative. A conservation check is a *necessary* test that
catches a whole class of bugs, not a sufficient test of correctness.

---

## ★★5 — Momentum in a two-body system

**(a)** $m_1 = GM_\oplus/G = 3.986\,004\,418\times10^{14}/6.674\,30\times10^{-11}
= 5.9722\times10^{24}$ kg (this is exactly how the Earth's mass in the constant
handbook is obtained — and it inherits $G$'s 2.2 × 10⁻⁵ relative uncertainty).

Circular speed (relative motion, two-body):
$$v = \sqrt{\frac{G(m_1+m_2)}{r}}
= \sqrt{\frac{6.674\,30\times10^{-11}\times5.9722\times10^{24}}{10^{7}}}
= 6318.8\ \mathrm{m\,s^{-1}}.$$

Period (Kepler's third law):
$$T = 2\pi\sqrt{\frac{r^{3}}{G(m_1+m_2)}} = 2\pi\sqrt{\frac{10^{21}}
{3.986\times10^{14}}} = 9943.7\ \mathrm{s} = 2.76\ \mathrm{h}.$$

**(b)** Both bodies feel the *same* force magnitude with opposite signs
($\mathbf{F}_{12} = -\mathbf{F}_{21}$), so
$m_1\Delta\mathbf{v}_1 = -m_2\Delta\mathbf{v}_2$ step by step. The increments
cancel pairwise in the sum, exactly as the flux increments do in ★8: this is
Newton's third law expressed as a discrete identity.

**(c)** Yes, momentum is conserved. The residual must be normalised by the
*scale of the terms* — here $m_2v = 6.319\times10^{25}$ kg m/s — giving
$1.2\times10^{11}/6.3\times10^{25} = 1.9\times10^{-15}$, i.e. round-off. The
lesson's demonstration reports $3.3\times10^{-15}$ for the same quantity.
Normalising by the initial total (which can be zero by symmetry) or by zero is
the error this part is designed to catch.

---

## ★★6 — Rotational bookkeeping

**(a)** Uniform sphere: $I = \tfrac25MR^{2}
= 0.4\times5.972\times10^{24}\times(6.371\times10^{6})^{2}
= 9.6963\times10^{37}\ \mathrm{kg\,m^{2}}$.
$$L = I\omega = 7.0707\times10^{33}\ \mathrm{kg\,m^{2}\,s^{-1}},\qquad
E = \tfrac12I\omega^{2} = 2.5780\times10^{29}\ \mathrm{J}.$$

**(b)** Two-layer model: $I = 8.4699\times10^{37}$ kg m²,
$I/(MR^{2}) = 0.3465$;
$$L = 6.1764\times10^{33}\ \mathrm{kg\,m^{2}\,s^{-1}},\qquad
E = 2.2519\times10^{29}\ \mathrm{J}.$$
Both $L$ and $E$ are 13% smaller than the uniform-sphere values, entirely
because the centrally condensed mass distribution has a smaller moment of
inertia. This is why an accurate $I$ — and hence satellite gravity — is needed
before the Earth's angular momentum budget can be closed.

**(c)** A 1 ms increase in the length of the day changes the rate by
$$\Delta\omega = -\omega\,\frac{\Delta T}{T}
= -7.292\,115\times10^{-5}\times\frac{10^{-3}}{86\,400}
= -8.440\times10^{-13}\ \mathrm{rad\,s^{-1}}.$$
Then
$$\Delta L = I\Delta\omega = -7.149\times10^{25}\ \mathrm{kg\,m^{2}\,s^{-1}},
\qquad
\Delta E = I\omega\,\Delta\omega = -5.213\times10^{21}\ \mathrm{J}.$$
The fractional change is $|\Delta L|/L = 1.16\times10^{-8}$.

**(d)** The claim is wrong twice over. First, the energy does not *radiate*: the
mechanism that slows the Earth is tidal friction, which converts rotational
energy to heat in the oceans and solid Earth, and only a tiny fraction
(of order $10^{-5}M_0$, see ★10) goes into seismic radiation. Second, a *seismic*
budget is the wrong accounting frame entirely: the relevant comparison is
tidal dissipation against the $5.2\times10^{21}$ J, and any statement about
whether the numbers balance requires the measured tidal dissipation rate, which
must be taken from the literature rather than inferred from this exercise.

---

## ★★7 — The heat equation from an energy balance

Start from
$$\frac{\partial(\rho cT)}{\partial t} + \nabla\cdot\mathbf{q} = H,
\qquad \mathbf{q} = -k\nabla T.$$
Substituting the constitutive law gives
$$\frac{\partial(\rho cT)}{\partial t} = \nabla\cdot(k\nabla T) + H.$$
Dividing by the constant $\rho c$:
$$\frac{\partial T}{\partial t} = \kappa\nabla^{2}T + \frac{H}{\rho c},
\qquad \kappa = \frac{k}{\rho c}.$$

**(a)** The two assumptions: (i) $\rho$ and $c$ are constant in time and space
(the general form keeps $\rho c$ inside the time derivative); (ii) the medium is
rigid or moves slowly enough that the advective energy flux
$\rho cT\mathbf{v}$ is negligible compared with conduction — the Péclet-number
assumption.

**(b)** Dimensions with $\rho c$ in $\mathrm{M\,L^{-1}T^{-2}K^{-1}}$:

| Term | Dimension |
|---|---|
| $\rho c\,\partial_tT$ | $(\mathrm{M\,L^{-1}T^{-2}K^{-1}})(\mathrm{K\,T^{-1}}) = \mathrm{M\,L^{-1}T^{-3}}$ |
| $\nabla\cdot(k\nabla T)$ | $(\mathrm{M\,L\,T^{-3}K^{-1}})(\mathrm{K\,L^{-2}}) = \mathrm{M\,L^{-1}T^{-3}}$ |
| $H$ | $\mathrm{W\,m^{-3}} = \mathrm{M\,L^{-1}T^{-3}}$ |

All three terms match: a power per unit volume.

**(c)** With no conduction, $\Delta T = H\Delta t/(\rho c)
= 10^{-6}\times3.1557\times10^{7}/2.16\times10^{6}
= 1.46\times10^{-5}$ K. One year of radiogenic heating of an insulated rock
raises its temperature by 15 µK — which is why the geotherm is a *steady-state*
balance between production and conduction, not an accumulation.

---

## ★★8 — The telescoping identity

**(a)** With cell averages $\rho_i$ on a periodic grid and face fluxes $F_i$
(between cells $i-1$ and $i$):
$$\rho_i^{n+1} = \rho_i^{n} - \frac{\Delta t}{\Delta x}\left(F_i - F_{i-1}\right).$$

**(b)** Sum over $i = 0,\dots,N-1$:
$$\sum_i \rho_i^{n+1} = \sum_i \rho_i^{n}
- \frac{\Delta t}{\Delta x}\left(\sum_i F_i - \sum_i F_{i-1}\right).$$
Because the grid is periodic, $\sum_i F_{i-1} = \sum_i F_i$ (the same set of
fluxes, reindexed), so the bracket vanishes identically and
$\sum_i\rho_i^{n+1} = \sum_i\rho_i^{n}$.

**(c)** The proof uses periodicity only to assert that the index shift
$i \mapsto i-1$ permutes the same flux list. With a **closed (no-flux)**
boundary, the fluxes at the two outermost faces are set to zero, and the same
cancellation happens for all interior faces while the boundary terms contribute
nothing — so the total is still conserved. With a **prescribed flux** at the
boundary (an open system), the total changes by exactly the boundary flux times
$\Delta t$: the conservation statement becomes a balance statement, with the
boundary flux as the source term. That is the discrete version of §2.2 of the
lesson.

---

## ★★★9 — Conservation is not sufficiency

**(a) Newton's shell theorem.** For a spherically symmetric mass distribution,
(i) the external gravitational field is identical to that of a point mass with
the same total mass at the centre, and (ii) the field inside a uniform spherical
*sail* of matter is zero.

**(b)** A spherical shell's contribution to the external field is exactly zero
(point (i) with a shell of mass $m$ at the same radius, and point (ii) applied
to the interior of a shell), while its mass is $m>0$. So mass can be added in a
sheaf of concentric shells without changing the external field at all.

**(c)** Take any two density profiles that agree in *total mass*, for example:
(i) a uniform sphere of radius $R$ and density $\rho_0$; (ii) an equal-mass
point sphere plus a set of concentric uniform shells chosen so that the
equal-mass condition is preserved. Both are spherically symmetric with equal $M$,
so by the shell theorem their external fields are identical —
$g_r = -GM/r^{2}$ for all $r \ge R$. The degeneracy is **exact** because the
shell theorem is an identity, not an approximation: the extra shells' fields
cancel identically at every external point, and no precision in the external data
can detect them. (Adding *rotational flattening* or an equatorial bulge breaks
spherical symmetry and therefore the argument — which is exactly how the
non-uniqueness of potential-field inversion is bounded in practice.)

**(d)** A measurement sensitive to the interior specifically: (i) the *internal*
field, sampled by a satellite in a low orbit through the shell (or, for the
Earth, seismic travel times and normal modes that sample the density profile);
(ii) the moment of inertia, from the precession or from the $C_{20}$ gravity
coefficient combined with the rotation rate. External gravity alone is not
enough — which is the physical content of the null space of the gravity inverse
problem ([01-06-08](../../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)).

---

## ★★★10 — Seismic moment and radiated energy

**(a)** $M_0 = \mu A D = 3\times10^{10}\times5\times10^{7}\times0.5
= 7.5\times10^{17}\ \mathrm{N\,m}$.

**(b)** $E_s = (\Delta\sigma/2\mu)M_0 = (3\times10^{6}/6\times10^{10})
\times7.5\times10^{17} = 5\times10^{-5}\times7.5\times10^{17}
= 3.75\times10^{13}$ J.

**(c)** Two separate errors:

1. **Category error in the energy.** Tidal dissipation removes rotational
   energy as heat, not as seismic radiation. The seismic energy is roughly
   $10^{-5}$ of the moment, and the moment is itself not the tidal energy; the
   two budgets are not interchangeable.
2. **Missing the angular-momentum bookkeeping.** A change in rotational energy
   at fixed $I$ comes with a change in $L$ of $I\Delta\omega$, which must appear
   in the Moon's orbit. Subtracting $E_s$ from $I\omega^{2}/2$ while leaving $L$
   unspecified violates conservation of angular momentum. Unlike energy,
   *total* angular momentum is conserved; energy is not, because dissipation is
   precisely the mechanism.

**(d)** An explosion is a purely volumetric (isotropic) source. Its force system
is a set of outward point forces distributed over a sphere; by symmetry their
vector sum is zero at every instant, so the net force — and hence the net
linear momentum injected — is exactly zero. It still radiates: the *radiated
field* is generated by the time-varying stress and volume change, and the
far-field displacement depends on the divergence-free part of the source for
S waves and the volumetric part for P waves. Zero net momentum does not mean
zero radiation; it means the Earth's centre of mass is undisturbed. This is why
explosions and earthquakes have characteristically different radiation patterns
and why moment-tensor inversions separate the isotropic from the deviatoric
parts.

---

## Self-assessment: have you actually learned this?

- [ ] I can write a balance law in integral and differential form and identify
      the source term.
- [ ] I can derive the continuity equation and explain the role of each step.
- [ ] I can explain why flux-form schemes conserve exactly and demonstrate the
      telescoping algebra.
- [ ] I can compute the momentum and energy bookkeeping of a collision and say
      which law is the right check.
- [ ] I can compute $I$, $L$ and the rotational energy change for a given
      change in the length of the day, and normalise a residual correctly.
- [ ] I can argue from the shell theorem why external fields cannot determine the
      interior distribution uniquely.
