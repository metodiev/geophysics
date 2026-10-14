# Solutions — 02-02-08 Rigid-Body Dynamics, Precession and the Earth's Rotation

> **Read this after attempting the exercises, not before.**
>
> All arithmetic was computed. $\omega_\oplus = 7.292\,115\times10^{-5}$ rad s⁻¹,
> $a = 6\,378\,137$ m, $1/f = 298.257\,223\,563$; the sidereal year (365.256 d) and
> the obliquity (23.439°) are **nominal** inputs flagged as such.

---

## ★1 — Euler's equations

**(a)** $I_1\dot\omega_1 = (I_2-I_3)\omega_2\omega_3 + \tau_1$, and cyclically. The
terms $(I_2-I_3)\omega_2\omega_3$ are **kinematic**, not forces: they arise because
the body frame rotates, so a constant $\mathbf{L}$ in space has time-varying
components in the body frame. Physically they express the exchange of angular
momentum among the three principal axes of an asymmetric body — which is why an
asymmetric top wobbles even with no torque at all.

**(b)** With $I_1 = I_2 = A$ and $I_3 = C$:
$$A\dot\omega_1 = -(C-A)\omega_2\omega_3, \qquad
A\dot\omega_2 = +(C-A)\omega_3\omega_1, \qquad C\dot\omega_3 = 0.$$
So $\omega_3$ is constant and $(\omega_1,\omega_2)$ performs a rotation at rate
$\Omega = \omega_3(C-A)/A$.

**(c)** The equations are exact for a rigid body: no small-angle or slow-rotation
approximation is made anywhere. For the Earth, "rigid" fails because the mantle
deforms elastically under the tidal and centrifugal potentials, the fluid outer
core rotates partially independently, and mass redistributes (atmosphere, oceans,
ice). Each is a modelled correction with a measured input (lesson 08 §3.6).

---

## ★2 — Symmetric top

**(a)** $C\dot\omega_3 = 0$ gives $\omega_3 = 3$ rad s⁻¹ **constant** — it is an
exact consequence of the equations, not an approximation.

**(b)** $\Omega = \omega_3(C-A)/A = 3\times(1.5-1)/1 = \mathbf{1.5\ rad\,s^{-1}}$,
period $2\pi/\Omega = \mathbf{4.1888\ s}$. The lesson's integration reproduces
4.188790 s against the closed form 4.188790 s (relative difference
$4.9\times10^{-8}$, which is the integrator's error).

**(c)** This is the mechanism of the Earth's **free wobble**: a rotation axis
tilted slightly away from the symmetry axis executes a circular precession about
it, with a period fixed by $H = (C-A)/A$ and $\omega$. The rigid-body version is
the Eulerian free precession; the observed version (the Chandler wobble) is longer
because of elasticity and the fluid core.

---

## ★3 — The Earth's dynamical ellipticity

**(a)** $f = 1/298.257\,223\,563 = 3.352\,810\,6\times10^{-3}$, so
$b = a(1-f) = \mathbf{6\,356\,752.314\ m}$.

**(b)** $H = \dfrac{a^{2}-b^{2}}{a^{2}+b^{2}} = \dfrac{4.066\,063\,9\times10^{13} -
4.041\,237\,7\times10^{13}}{4.066\,063\,9\times10^{13}+4.041\,237\,7\times10^{13}}
= \mathbf{3.3584\times10^{-3}}$.

**(c)** $T_{\text{free}} = \dfrac{2\pi}{\omega H}
= \dfrac{2\pi}{7.292\,115\times10^{-5}\times3.3584\times10^{-3}}
= 2.5656\times10^{7}\ \mathrm{s} = \mathbf{296.945\ days}$.

**What this is:** a *model* value from two defining shape parameters, the defining
rotation rate and the assumption of uniform density. The real Earth's $H$ is
smaller (central condensation) and its free period longer; the observed value must
come from IERS.

---

## ★4 — Invariants of the torque-free asymmetric top

The two invariants are

$$|\mathbf{L}|^{2} = I_1^{2}\omega_1^{2}+I_2^{2}\omega_2^{2}+I_3^{2}\omega_3^{2},
\qquad
T_{\text{rot}} = \tfrac12\left(I_1\omega_1^{2}+I_2\omega_2^{2}+I_3\omega_3^{2}\right).$$

The components $\omega_i$ are *not* conserved because the three equations couple
them: energy and angular momentum can flow from one axis to another (through the
$(I_j-I_k)\omega_j\omega_k$ terms), but the two quadratic combinations cannot
change. The body frame itself is rotating, so "$\omega_1$ changes" is a statement
about the body frame, not about the physics — which is why the invariants, being
frame-independent, are the right things to check.

---

## ★★5 — Solar-only forced precession

**(a)** $n = 2\pi/(365.256\times86\,400) = 1.990\,988\,6\times10^{-7}$ rad s⁻¹, so
$\omega/n = 7.292\,115\times10^{-5}/1.990\,988\,6\times10^{-7}
= \mathbf{366.2560}$ — the number of sidereal days in a year (rounded), which is
also the reason the sidereal and solar days differ.

**(b)**
$$\frac{d\psi}{dt} = \tfrac32\frac{n^{2}}{\omega}H\cos\varepsilon
= 1.5\times\frac{(1.990\,99\times10^{-7})^{2}}{7.292\,115\times10^{-5}}
\times3.3584\times10^{-3}\times\cos23.439° = \mathbf{2.5125\times10^{-12}\ rad\,s^{-1}}.$$
In astronomers' units:
$2.5125\times10^{-12}\times3.1557\times10^{7}\times206\,264.81
= \mathbf{16.3543\ arcsec\,yr^{-1}}$.

**(c)** $T_{\text{prec}} = 2\pi/(2.5125\times10^{-12}\ \mathrm{rad\,s^{-1}})
= 2.5007\times10^{12}$ s $= \mathbf{7.9245\times10^{4}\ years}$ for the **solar
torque alone**.

**(d)** Missing: (i) the **lunar** torque, which dominates the total (the Moon is
far closer, and the torque scales with $m/d^{3}$); (ii) the correction from using
$C$ rather than $A$ in the denominator (a relative error of order $H \approx
3\times10^{-3}$); (iii) the real obliquity and orbit eccentricity (periodic terms,
i.e. nutation rather than precession); and (iv) the Earth's elastic and fluid
response, which modifies the effective $H$.

---

## ★★6 — Sensitivity to $H$

**(a)**

| $H$ | $d\psi/dt$ (rad s⁻¹) | (arcsec yr⁻¹) | $T_{\text{prec}}$ (yr) |
|---|---|---|---|
| 0.00335843 | $2.5125\times10^{-12}$ | 16.3543 | 79 244 |
| 0.0033 | $2.4688\times10^{-12}$ | 16.0697 | 80 647 |
| 0.0032 | $2.3940\times10^{-12}$ | 15.5828 | 83 167 |
| 0.0030 | $2.2444\times10^{-12}$ | 14.6088 | 88 712 |

**(b)** The period scales exactly as $1/H$: $79\,244\times(0.00335843/0.0030)
= 88\,712$ ✓, and similarly for the other rows. This is because $H$ enters the
rate linearly and the rate is the reciprocal of the period — a *one-parameter*
scaling law, which is why the sensitivity table is so compact.

**(c)** The astronomical inputs ($n$, $\varepsilon$) describe *external* bodies and
are known from celestial mechanics to high precision. So if the precession rate is
measured, the only unknown in the relation is $H = (C-A)/A$ — a property of the
Earth's *internal* mass distribution. The measurement is therefore an interior
probe, and the sense in which it is a probe is exactly the sense in which the
formula is invertible. (With the real, non-rigid Earth there is a second unknown —
the elastic/fluid response — which is why the *nutation* spectrum is used as well:
the two observables separate $H$ from the response.)

---

## ★★7 — Asymmetric top

**(a)** $|\mathbf{L}|^{2} = (1\times1)^{2}+(1.5\times0.2)^{2}+(2\times3)^{2}
= 1+0.09+36 = \mathbf{37.09}$ (units kg² m⁴ s⁻² with the given inertias);
$T_{\text{rot}} = \tfrac12(1\times1+1.5\times0.04+2\times9)
= \tfrac12(1+0.06+18) = \mathbf{9.53}$.

**(b)** Integrate Euler's equations with a fixed small step (the lesson uses RK4 at
$\Delta t = 10^{-4}$ for 10 s) and print the relative change in both invariants
at the end. The lesson's measured drift is $1.149\times10^{-15}$ for
$|\mathbf{L}|^{2}$ and $1.118\times10^{-15}$ for $T_{\text{rot}}$ — round-off, as
expected, since RK4's truncation error on this problem is far below that. A useful
extra check: refine $\Delta t$ and confirm the drift falls.

**(c)** The **polhode** is the closed curve traced by the tip of $\boldsymbol{\omega}$
*in the body frame*: the intersection of the kinetic-energy ellipsoid
$\tfrac12\mathbf{I}\boldsymbol{\omega}\cdot\boldsymbol{\omega} = T_{\text{rot}}$
with the angular-momentum sphere $|\mathbf{I}\boldsymbol{\omega}| = |\mathbf{L}|$.
It is confined because $\boldsymbol{\omega}$ must satisfy *both* constraints
simultaneously, and two algebraic constraints in a three-dimensional space leave a
one-dimensional curve. The lesson measures the polhode's recurrence: $\omega_3$ has
maxima at 1.7402, 3.5792, 5.4183 and 7.2573 s, a period of 1.839 s.

---

## ★★8 — Classification

| Observable | Driver |
|---|---|
| (a) axis direction in space, secular | lunisolar torque on the equatorial bulge (precession) |
| (b) axis direction in space, periodic | the same torque with the inclined, precessing lunar orbit (nutation) |
| (c) axis direction moving in the body | mass redistribution (ice, water, atmosphere) exciting the free wobble (polar motion) |
| (d) rotation rate changing by fractions of a ms per year | angular-momentum exchange: secular tidal transfer; decadal core–mantle coupling; seasonal atmosphere |

The four are separate measurements with separate mechanisms; "the Earth's rotation
changed" is not a statement until one of them is named.

---

## ★★★9 — Why the observed free period is longer

**(a)** Three effects, each with a distinct mechanism:

1. **Elastic yielding.** The body deforms under the centrifugal and tidal
   potentials, and the deformation follows the wobble. The response reduces the
   effective restoring torque (the body "gives" slightly instead of restoring
   fully), which lengthens the period.
2. **A fluid outer core.** The core does not rotate with the mantle; part of the
   angular momentum is carried by a fluid that is only weakly coupled to the
   mantle, so the mantle's restoring torque is smaller and the effective $H$ is
   smaller.
3. **Central condensation of mass.** A real Earth has less mass at large radii
   than the uniform spheroid, hence a smaller $H$; since $T = 2\pi/(\omega H)$,
   the period is longer.

**(b)** The restoring torque for a given wobble angle is proportional to $C-A$,
i.e. to $H$; the angular momentum to be restored is proportional to $C \approx A$.
So the precession rate $\propto H$ and the period $\propto 1/H$: less oblateness,
weaker restoring torque, slower wobble.

**(c)** The observed free-wobble period must be determined from the Earth-orientation
series — a time series of polar motion, fitted for its dominant resonant period —
published by IERS and revised as the series lengthen and as the excitation model
improves. A textbook value is inadequate for a modern study because the series are
reprocessed, the excitation (atmosphere plus oceans) must be modelled to isolate
the resonance, and the uncertainties are quoted with the series rather than with
the number.

**(d)** A pure rigid body with any dissipation would have its free wobble damped
on a timescale short compared with the age of the Earth — the observed
$Q$ of the wobble implies damping over decades to centuries. Since the wobble is
observed *now*, it must be **continually excited**: by atmospheric and oceanic
angular-momentum changes, by earthquakes, and by other mass redistributions. The
persistence of the wobble is therefore a statement about the excitation budget,
not about the absence of dissipation — one of the classic results of
20th-century Earth rotation research.

---

## ★★★10 — Designing a nutation test

**(a)** The nutation amplitudes depend on: (i) the **torque** terms, from the
solar and lunar positions and moments — known to high accuracy from celestial
mechanics; (ii) the **dynamical ellipticity** $H$, i.e. the whole-Earth mass
distribution; (iii) the **elastic response**, through Love numbers describing the
deformation under the tidal potential; and (iv) the **fluid core**, through its
moment of inertia, its coupling to the mantle, and the Free Core Nutation. Items
(ii)–(iv) are the unknowns; (i) is essentially given.

**(b)** You need long, precise **space-geodetic Earth-orientation series** —
VLBI nutation estimates, with GNSS and satellite laser ranging contributing —
covering many years (to separate the 18.6-year term and the secular precession),
with amplitudes determined at the level of tens of microarcseconds or better, plus
a model of the atmospheric and oceanic contributions so that the solid-Earth
amplitude can be isolated. State the required precision as a *number tied to the
series you use*, and take it from the IERS product documentation rather than from
memory.

**(c)** The **periods** of the forced nutations are set by the astronomical
forcing (the Moon's node regression, the Sun's annual motion), so they carry no
information about the Earth's interior. The **amplitudes** are set by the Earth's
response to a known torque, and so they are the diagnostic. This is a general
principle: in a forced oscillator, frequency comes from the forcing, amplitude and
phase from the system.

**(d)** A **systematic error that could mimic a core-inertia change** is an error
in the assumed ellipticity of the *mantle and crust alone* — i.e. in $H$ — since
both $H$ and the core's inertia enter the same amplitudes. They can be separated
because they enter with different frequency dependence: the core's effect is
largest near the Free Core Nutation resonance (nearly diurnal), while the
ellipticity affects the long-period terms. So the test is to fit the *frequency
dependence* of the amplitude residuals, not the amplitude of a single term; a
single-term fit cannot distinguish them at all.
