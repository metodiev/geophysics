---
id: 16-03-01
title: "Global Circulation: Hadley, Ferrel, Polar Cells, Jets"
level: advanced
prereqs: ["16-01-02", "16-01-05", "02-06-07"]
tags: [atmosphere, climate, circulation, hadley-cell, angular-momentum, thermal-wind, eddies]
---

# Global Circulation: Hadley, Ferrel, Polar Cells, Jets

The atmosphere is heated most strongly where the Sun is overhead and loses heat
to space most strongly near the poles. A circulation that moved heat poleward
would remove both extremes, and one exists: the tropical **Hadley cells** rising
at the equator, the **Ferrel cells** in midlatitudes, and the shallow **polar
cells**. The textbook zonal-mean picture of three cells per hemisphere, with
subtropical and polar-front **jets** between them, is a description of the
*zonal mean* — and the zonal mean is not a closed system.

This lesson builds the circulation from two constraints that can be written on
one line each: **angular momentum conservation** and **thermal wind**. Together
they predict something surprising and checkable — that the tropical
tropopause potential temperature is *flat* out to roughly twenty degrees of
latitude, because the conservation law is quartic rather than quadratic in
latitude. They also predict a subtropical jet of $134\ \mathrm{m\,s^{-1}}$ at
$30^\circ$, about twice what the midlatitude momentum budget of Section 7 can
sustain. That discrepancy is the whole of Section 7, and its resolution is not a
fudge factor but a statement about what a zonal-mean theory can contain.

All models and data in this module are **SYNTHETIC**. The temperature profiles,
flux profiles and velocity scales below are chosen teaching values, printed by
[`code/global_circulation_demo.py`](code/global_circulation_demo.py), not
measurements. Earth's rotation rate, radius and gravity are standard constants.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Coriolis parameter $f = 2\Omega\sin\phi$ and the inertial
   period, and **classify** five flows by their Rossby number $\mathrm{Ro} =
   U/(fL)$.
2. **Derive** the angular-momentum-conserving zonal wind
   $u = \Omega a \sin^2\phi/\cos\phi$ by showing that multiplying the zonal
   momentum equation by $a\cos\phi$ cancels the Coriolis and curvature terms
   exactly.
3. **Explain** why conservation cannot hold to the pole, and what that implies
   about where the Hadley cell must end.
4. **Derive** the tropical tropopause potential-temperature plateau from thermal
   wind plus conservation, including the quartic $\phi^4$ structure, and
   **verify** the closed form against a numerical integral.
5. **Estimate** the Hadley-cell edge by matching to a chosen radiative
   equilibrium, and **report it as a range** with the assumptions that set its
   width.
6. **Compute** the poleward heat transport implied by a prescribed net
   top-of-atmosphere flux, and state the closure needed to turn it into a
   velocity.
7. **Quantify** why a thermally indirect Ferrel cell cannot maintain the
   midlatitude jet, and estimate the eddy momentum flux convergence required.

## Prerequisites

- [16-01-02 Hydrostatic Balance and Pressure-Height Relations](../01-atmospheric-structure-and-thermodynamics/02-hydrostatic-balance.md) —
  the hydrostatic relation used to convert pressure gradients into depth
  gradients.
- [16-01-05 Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind](../01-atmospheric-structure-and-thermodynamics/05-atmospheric-dynamics-basics.md) —
  geostrophy and thermal wind, which this lesson extends to a non-geostrophic
  tropical circulation.
- [02-06-07 Geophysical Fluids](../../02-physics/06-fluid-mechanics/07-geophysical-fluids.md) —
  rotating-fluid kinematics: the Coriolis parameter, the Rossby number and
  Ekman transport, which are *used* here and derived there.

## 1. Intuition: why the tropics cannot be in geostrophic balance

Geostrophic balance requires a Coriolis force to balance the pressure gradient.
The Coriolis parameter is

$$f = 2\Omega\sin\phi, \qquad \Omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}},
$$

and it **vanishes at the equator**. A balance that is proportional to $f$ cannot
hold where $f$ is zero, and near the equator it is weak. The relevant measure is
the Rossby number, the ratio of the advective acceleration to the Coriolis
acceleration for a flow of speed $U$ and horizontal scale $L$:

$$\mathrm{Ro} = \frac{U}{fL}.$$

The demonstration prints, with a fixed $\Omega$:

| latitude | $f$ (s⁻¹) | inertial period (h) |
|---|---|---|
| $0^\circ$ | $0$ | infinite |
| $15^\circ$ | $3.77468\times10^{-5}$ | 46.238 |
| $30^\circ$ | $7.29211\times10^{-5}$ | 23.934 |
| $45^\circ$ | $1.03126\times10^{-4}$ | 16.924 |
| $60^\circ$ | $1.26303\times10^{-4}$ | 13.819 |
| $75^\circ$ | $1.40873\times10^{-4}$ | 12.389 |

and the corresponding classification:

| flow | $U$ (m s⁻¹) | $L$ (m) | $\mathrm{Ro}$ | regime |
|---|---|---|---|---|
| tropical Hadley cell | 20 | $3\times10^6$ | 0.177 | marginally rotational |
| midlatitude surface cyclone | 15 | $1\times10^6$ | 0.145 | rotation-dominated |
| midlatitude jet stream | 40 | $3\times10^6$ | 0.129 | rotation-dominated |
| tornado | 100 | $3\times10^2$ | 3555.7 | advection-dominated |
| bathtub drain | 0.1 | 0.5 | 1939.4 | advection-dominated |

The tropical cell sits at $\mathrm{Ro}\approx0.18$: not small, not large. That
single fact is the reason this lesson has a section on angular momentum
conservation and a section on eddies, and why neither alone answers the
question.

## 2. Definitions

| Symbol | Meaning | Unit |
|---|---|---|
| $\phi$ | latitude | rad (or deg) |
| $a$ | Earth mean radius, $6.371\times10^6$ | m |
| $\Omega$ | rotation rate, $7.292115\times10^{-5}$ | rad s⁻¹ |
| $u$ | zonal (eastward) wind | m s⁻¹ |
| $v$ | meridional (northward) wind | m s⁻¹ |
| $M$ | specific angular momentum | m² s⁻¹ |
| $\theta$ | potential temperature | K |

The **specific angular momentum** of air moving zonally with speed $u$ is

$$M = \underbrace{\Omega a^2\cos^2\phi}_{\text{planetary}}
      + \underbrace{u\,a\cos\phi}_{\text{relative}},$$

the moment of the total velocity about the rotation axis, per unit mass. The
planetary part is the contribution of the Earth's own rotation; the relative
part is the contribution of the wind.

## 3. Angular momentum conservation: the Hadley cell's constraint

### 3.1 The conservation law

Write the zonal momentum equation for an axisymmetric flow (no dependence on
longitude), with Rayleigh friction $-u/\tau$ and no zonal pressure gradient:

$$\frac{\partial u}{\partial t} + \frac{v}{a}\frac{\partial u}{\partial\phi}
- \left(f + \frac{u\tan\phi}{a}\right)v = -\frac{u}{\tau}.$$

Multiply by $a\cos\phi$ and use
$\partial M/\partial t = a\cos\phi\,\partial u/\partial t$ together with

$$\frac{\partial M}{\partial\phi} = -2\Omega a^2\sin\phi\cos\phi
- u a\sin\phi + a\cos\phi\frac{\partial u}{\partial\phi},$$

so that

$$\frac{v}{a}\frac{\partial M}{\partial\phi}
= -a\cos\phi\left(f + \frac{u\tan\phi}{a}\right)v
+ v\cos\phi\frac{\partial u}{\partial\phi}.$$

Adding the two identities **cancels the Coriolis and curvature terms exactly**:

$$\boxed{\;\frac{\mathrm{d}M}{\mathrm{d}t} = -\frac{a\cos\phi}{\tau}\,u\;}$$

That is the whole derivation. In the absence of friction the relative part of the
angular momentum is not separately conserved — the *total* $M$ is, and the
planetary part converts into wind as air moves meridionally.

### 3.2 The conserved-wind profile

Integrate $\mathrm{d}M/\mathrm{d}t = 0$ from the equator, where the air starts
at rest ($u = 0$) and hence $M = \Omega a^2$:

$$\Omega a^2 = \Omega a^2\cos^2\phi + u\,a\cos\phi
\quad\Longrightarrow\quad
\boxed{\;u_M(\phi) = \frac{\Omega a\sin^2\phi}{\cos\phi}.\;}$$

The demonstration evaluates this and checks conservation directly:

| $\phi$ | $u_M$ (m s⁻¹) | $M$ (m² s⁻¹) | $M/(\Omega a^2) - 1$ |
|---|---|---|---|
| $0^\circ$ | 0.00 | $2.959843\times10^9$ | $0$ |
| $10^\circ$ | 14.22 | $2.959843\times10^9$ | $0$ |
| $20^\circ$ | 57.83 | $2.959843\times10^9$ | $0$ |
| $30^\circ$ | 134.11 | $2.959843\times10^9$ | $2.2\times10^{-16}$ |
| $45^\circ$ | 328.51 | $2.959843\times10^9$ | $0$ |
| $60^\circ$ | 696.87 | $2.959843\times10^9$ | $2.2\times10^{-16}$ |
| $75^\circ$ | 1674.76 | $2.959843\times10^9$ | $0$ |

The residual column is round-off ($\sim10^{-16}$), which is what a correct
conservation law looks like in double precision. The velocity scale is
$\Omega a = 464.6\ \mathrm{m\,s^{-1}}$.

Two things are wrong with $u_M$ as a description of the atmosphere, and both are
informative:

1. $u(30^\circ) = 134.1\ \mathrm{m\,s^{-1}}$ is about **twice** a real
   subtropical jet. Conservation without friction over-predicts.
2. $u_M$ **diverges** as $\phi\to90^\circ$ because $\cos\phi\to0$. Angular
   momentum conservation cannot hold anywhere near the pole; something must
   break it, and what breaks it is exactly the eddy mixing that also fixes (1).

### 3.3 There is no free lunch

The Hadley cell cannot reach the pole: if it did, the air would have to acquire
$\Omega a\sin^2\phi/\cos\phi$, which is unphysical. In fact the cell stops where
the flow's *temperature* would fall below what radiation can supply — the
matching problem of Section 5. Poleward of that edge the flow is no longer
angular-momentum conserving, and the circulation changes character.

## 4. Thermal wind and the tropical tropopause plateau

### 4.1 Thermal wind

Geostrophy, $f u = -(1/\rho)\,\partial p/\partial y$, combined with hydrostatic
balance gives the **thermal wind relation**. In potential-temperature form, with
$\theta_0$ a reference value,

$$\frac{\partial u}{\partial z} = -\frac{g}{f\theta_0}\frac{\partial\theta}{\partial y},
\qquad y = a\phi .$$

*Read it physically:* a meridional temperature gradient is the same thing as a
vertical shear of the zonal wind. If the poleward side is colder
($\partial\theta/\partial y<0$ in the northern hemisphere), the westerly wind
increases with height.

### 4.2 The plateau

Now impose the tropical idealisation used by Held–Hou-type theories:

1. the surface potential temperature is **uniform across the tropics** (deep
   convection mixes it horizontally);
2. the surface zonal wind is **zero** (friction), and the tropopause wind is
   $u_M(\phi)$;
3. the shear is distributed linearly in $z$, so the depth average of
   $\partial\theta/\partial y$ is $(1/2)\,\partial\theta_t/\partial y$ with
   $\theta_t$ the tropopause value.

Integrating the thermal wind relation over $0\le z\le H$ then gives

$$\frac{\partial\theta_t}{\partial y}
= -\frac{2f\theta_0}{gH}\,u_M(\phi).$$

Substitute $u_M$ and $f = 2\Omega\sin\phi$ and integrate meridionally, using
$\int \sin^3\phi/\cos\phi\,\mathrm{d}\phi
= -\ln\cos\phi-\tfrac{1}{2}\sin^2\phi$:

$$\boxed{\;\theta_t(\phi) - \theta_t(0)
= \frac{4\theta_0\Omega^2a^2}{gH}\left(\ln\cos\phi + \frac{\sin^2\phi}{2}\right).\;}$$

The bracket is the point of the section. Expanding for small $\phi$,

$$\ln\cos\phi + \frac{\sin^2\phi}{2} = -\frac{\phi^4}{4} + O(\phi^6),$$

so

$$\theta_t(\phi) - \theta_t(0) \approx -\frac{\theta_0\Omega^2a^2}{gH}\,\phi^4.$$

**The tropical tropopause is flat to leading order.** Not quadratic — quartic.
No radiative transfer has entered: this is a kinematic consequence of angular
momentum conservation, and it is the reason a "flat tropical tropopause" is a
diagnostic of the tropical circulation rather than of tropical radiation.

The demonstration computes $C = 4\theta_0\Omega^2a^2/(gH) = 2640.2$ K for
$H = 10$ km and $\theta_0 = 300$ K, and prints

| $\phi$ | $\theta_t-\theta_t(0)$ (K) | $-30\sin^2\phi$ (K) |
|---|---|---|
| $5^\circ$ | $-0.04$ | $-0.23$ |
| $10^\circ$ | $-0.61$ | $-0.90$ |
| $15^\circ$ | $-3.10$ | $-2.01$ |
| $20^\circ$ | $-9.80$ | $-3.51$ |
| $25^\circ$ | $-23.95$ | $-5.36$ |
| $30^\circ$ | $-49.74$ | $-7.50$ |
| $35^\circ$ | $-92.38$ | $-9.87$ |
| $40^\circ$ | $-158.22$ | $-12.40$ |

The second column is flat to within about $1$ K out to $15^\circ$ and within
$10$ K out to $20^\circ$, then plunges: $50$ K colder by $30^\circ$. A
quadratic profile with the same $30$ K equator-to-pole contrast is shown for
comparison and behaves completely differently. **The plateau exists, and its
width is set by how long the $\phi^4$ term stays small.**

The demonstration also verifies the closed form against a direct numerical
integration of $\partial\theta_t/\partial y$: the largest discrepancy over
$10^\circ$–$40^\circ$ is $4.1\times10^{-9}$ K. That check tests the algebra, not
the physics. The physics rests on assumptions (1)–(3), which are exactly what
Section 8 lists as the regime of validity.

## 5. Where does the Hadley cell end? A range, not a number

The cell must end where the conserved temperature profile meets the
radiative-equilibrium profile. Take the equilibrium tropopause potential
temperature to be

$$\theta_e(\phi) = \theta_t(0) - \Delta\theta_e\sin^2\phi,$$

a chosen profile with a contrast $\Delta\theta_e$. The edge $\phi_H$ solves
$\theta_t(\phi_H) = \theta_e(\phi_H)$. Using the quartic approximation,

$$-\frac{C}{4}\phi_H^4 = -\Delta\theta_e\phi_H^2
\quad\Longrightarrow\quad
\phi_H \approx \sqrt{\frac{4\Delta\theta_e}{C}}
= \sqrt{\frac{\Delta\theta_e\,gH}{\theta_0\Omega^2a^2}}.$$

The demonstration solves the full equation on a fine grid over a matrix of
assumptions:

| $\Delta\theta_e$ (K) | $H=8$ km | $H=10$ km | $H=12$ km |
|---|---|---|---|
| 30 | $10.9^\circ$ | $12.1^\circ$ | $13.3^\circ$ |
| 50 | $14.0^\circ$ | $15.6^\circ$ | $17.0^\circ$ |
| 70 | $16.5^\circ$ | $18.3^\circ$ | $20.0^\circ$ |
| 90 | $18.6^\circ$ | $20.7^\circ$ | $22.6^\circ$ |

Every one of those twelve entries is defensible, and they span
$10.9^\circ$–$22.6^\circ$: a factor of $2.1$. **The matching argument locates
the cell edge but does not pin it.** Note the two sensitivities are opposite:
a stronger equilibrium contrast pushes the edge poleward, a deeper tropopause
pulls it equatorward, so they partly cancel and the width of the admitted range
is the honest answer. A single cell-edge latitude quoted from this model would
be an overclaim, and the lesson will not quote one.

## 6. What the circulation must carry

Fix the problem from the other end: prescribe the net top-of-atmosphere flux
$N(\phi) = A - B\sin^2\phi$ and ask how much heat the circulation must move. The
profile used in the demonstration is $N = 40 - 120\sin^2\phi\
\mathrm{W\,m^{-2}}$, chosen so that the area-weighted global mean is exactly
zero (a planet in balance).

The poleward transport across latitude $\phi$ is the deficit of the polar cap:

$$T(\phi) = 2\pi a^2\int_\phi^{\pi/2}\left[-N(\phi')\right]\cos\phi'\,
\mathrm{d}\phi'.$$

With $B = 3A$ this integrates analytically. Since
$-N = A(3\sin^2\phi' - 1)$, setting $x = \sin\phi$ gives

$$T(\phi) = 2\pi a^2 A\int_{x}^{1}(3u^2-1)\,\mathrm{d}u
= 2\pi a^2 A\left[u^3-u\right]_{x}^{1}
= 2\pi a^2 A\, x\,(1-x^2),$$

which is $80\pi a^2\sin\phi\,(1-\sin^2\phi)$ for $A = 40\
\mathrm{W\,m^{-2}}$.

The demonstration prints

| $\phi$ | $T$ (PW) | $\bar v$ if a mean cell carried it all (m s⁻¹) |
|---|---|---|
| $0^\circ$ | 0.000 | 0.000 |
| $15^\circ$ | 2.463 | 0.604 |
| $30^\circ$ | 3.825 | 1.047 |
| $45^\circ$ | 3.607 | 1.209 |
| $60^\circ$ | 2.209 | 1.047 |
| $75^\circ$ | 0.660 | 0.604 |

The peak requirement is $3.825\ \mathrm{PW}$ at $30^\circ$. The $\bar v$ column
comes from the crude closure
$\bar v = T/(2\pi a\cos\phi\,\rho c_p\,\Delta\theta\,H)$ with $\rho = 0.7\
\mathrm{kg\,m^{-3}}$, $\Delta\theta = 15$ K and $H = 10$ km — **chosen**, not
measured. It is printed so that its dependence on those three numbers is
visible: change $\Delta\theta$ to 10 K and every velocity rises by 50%. The
transport of a few PW is robust because it comes only from the flux profile and
the geometry; the velocity is not.

## 7. Ferrel and polar cells: why eddies are not optional

Midlatitudes are different in kind, not merely in strength. The Ferrel cell
turns over the "wrong" way — **thermally indirect**: it transports heat
equatorward in the mean, which cannot be driven by the meridional heating
contrast. Its existence must be paid for, and the currency is eddy momentum.

Consider the midlatitude jet as a column of depth $H = 10$ km and density
$\rho = 1.0\ \mathrm{kg\,m^{-3}}$, with $U = 20\ \mathrm{m\,s^{-1}}$, spun down
by Rayleigh friction on a $5$-day timescale. Then

$$\text{friction drag} = \rho H U/\tau = \frac{1.0\times10^4\times20}{
5\times86400} = 0.463\ \mathrm{N\,m^{-2}}.$$

The Ferrel cell's surface branch is equatorward, $v\approx -1\ \mathrm{m\,s^{-1}}$
at $45^\circ$ where $f = 1.031\times10^{-4}\ \mathrm{s^{-1}}$, so it exerts

$$\text{Coriolis torque} = \rho H f v = 10^4\times1.031\times10^{-4}\times(-1)
= -1.031\ \mathrm{N\,m^{-2}},$$

which **decelerates** the jet (the same sign as friction). The budget therefore
requires an eddy momentum flux convergence of

$$0.463 - (-1.031) = 1.49\ \mathrm{N\,m^{-2}}$$

to keep the jet in place. That number — order $1\ \mathrm{N\,m^{-2}}$, with the
mean cell working *against* the jet — is the quantitative content of "the Ferrel
cell is eddy-driven". Eddies are not a correction to the zonal-mean picture;
they are what maintains it, and the same eddies break the angular momentum
conservation that Section 3 assumed, which is why the real subtropical jet is
weaker than $u_M$.

The polar cell, by contrast, is a weak, largely thermally direct overturning
driven by radiative cooling at high latitude, whose poleward branch carries the
residual heat transport of Section 6 at $60^\circ$–$75^\circ$ in the table
above. It is shallow and slow, and it exists because the polar cap's radiative
deficit must be supplied from lower latitudes.

## 8. Assumptions and regime of validity

The results of this lesson hold only where their assumptions do. State them
every time:

1. **Axisymmetry.** Section 3 assumes no variation with longitude. Real
   eddies violate it; that is precisely the failure quantified in Section 7.
2. **Small friction.** $u_M$ is the $\tau\to\infty$ limit. With a 5-day
   spin-down time, a jet cannot be maintained at $134\ \mathrm{m\,s^{-1}}$ by
   any forcing considered here.
3. **Uniform tropical surface potential temperature and zero surface wind.**
   Both are approximations valid in the deep tropics and poor outside them.
4. **Linear-in-height shear** (the factor 2 in Section 4.2). A different shear
   profile changes the coefficient of the plateau; the $\phi^4$ structure
   survives, the constant does not.
5. **No radiative transfer in Section 4.** That is a feature: the plateau is
   kinematic. It is also a limitation: nothing in it fixes $\theta_t(0)$.
6. **The matching of Section 5 is a matching, not a solution.** It uses a
   chosen $\theta_e(\phi)$; the range in the table is the price of that choice.
7. **The transport of Section 6 is a budget, not a model.** It says what must
   be carried, never who carries it.

## 9. Worked examples

### Example 1 — the conserved wind at $15^\circ$ and the plateau depth

$u_M(15^\circ) = \Omega a\sin^2 15^\circ/\cos 15^\circ
= 464.6\times0.066987/0.965926 = 32.2\ \mathrm{m\,s^{-1}}$.

Plateau: $\ln\cos15^\circ = -0.034670$,
$\sin^2 15^\circ/2 = 0.033494$, bracket $= -0.001176$, so

$$\theta_t - \theta_t(0) = 2640.2\times(-0.001176) = -3.10\ \mathrm{K}.$$

Cross-check with the quartic form:
$-\theta_0\Omega^2a^2\phi^4/(gH)
= -(300)(5.3177\times10^{-9})(4.059\times10^{13})(0.2618)^4/(9.81\times10^4)
= -3.10$ K, identical to two decimals. At $30^\circ$ the quartic form gives
$-49.62$ K against the exact $-49.74$ K, an error of $0.24\%$: the quartic is
an excellent approximation over the whole plateau and fails only where the
profile itself has already plunged.

### Example 2 — a required transport

Using Section 6 at $45^\circ$: $x = \sin45^\circ = 0.707107$,
$1-x^2 = 0.5$, so $T = 80\pi a^2\times0.707107\times0.5
= 80\pi\times4.059\times10^{13}\times0.353553 = 3.607\times10^{15}$ W
$= 3.607$ PW, matching the demonstration's third row.

If the atmosphere carried this with a mean cell of $\Delta\theta = 15$ K through
$H = 10$ km at density $0.7\ \mathrm{kg\,m^{-3}}$,
$\bar v = 3.607\times10^{15}/(2\pi\times6.371\times10^6\times0.7071\times0.7
\times1004\times15\times10^4) = 1.209\ \mathrm{m\,s^{-1}}$.

### Example 3 — the cell edge from the scaling

$\phi_H \approx \sqrt{\Delta\theta_e gH/(\theta_0\Omega^2a^2)}$ with
$\Delta\theta_e = 50$ K, $H = 10$ km:

$$\phi_H = \sqrt{\frac{50\times9.81\times10^4}
{300\times5.3177\times10^{-9}\times4.059\times10^{13}}}
= \sqrt{0.07575} = 0.2752\ \mathrm{rad} = 15.8^\circ,$$

against $15.6^\circ$ from the full solution in the table. The scaling is
accurate to a few per cent at these parameters and is the right way to see the
$\sqrt{\Delta\theta_e H}$ dependence: quadrupling the contrast only doubles the
cell width.

## 10. Python demonstration

[`code/global_circulation_demo.py`](code/global_circulation_demo.py) prints every
number used above, in seven labelled sections: the Coriolis parameter and
inertial period; five Rossby numbers; the conserved wind profile with its
round-off-level conservation check; the plateau profile, its comparison with a
quadratic profile, and the closed-form-versus-numerical verification; the
cell-edge table; the transport budget with its stated closure; and the Ferrel
cell momentum budget. It runs in under a second, needs no network, and exits 0.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/01-global-circulation-exercises.md`](exercises/01-global-circulation-exercises.md)
and
[`exercises/01-global-circulation-solutions.md`](exercises/01-global-circulation-solutions.md).

- **★** Compute $f$ and the inertial period at $20^\circ$ and $70^\circ$, and
  the Rossby number of a $10\ \mathrm{m\,s^{-1}}$ flow of scale $2\times10^6$ m
  at each latitude. Which is rotation-dominated?
- **★★** Derive $\mathrm{d}M/\mathrm{d}t = -a\cos\phi\,u/\tau$ from the zonal
  momentum equation, showing where the curvature term goes.
- **★★** Show that the exponent in $\theta_t(\phi)-\theta_t(0)$ is quartic and
  find the latitude at which the quartic form is in error by 5%.
- **★★★** Repeat Section 7's momentum budget with $v = -3\
  \mathrm{m\,s^{-1}}$ and a 2-day friction timescale, and state what happens to
  the required eddy flux convergence. Then explain why an axisymmetric theory
  cannot produce that flux.

## 12. Common mistakes

1. **Reading $u_M$ as a prediction.** It is an upper bound that ignores
   friction and eddies. Quoting $134\ \mathrm{m\,s^{-1}}$ for the subtropical
   jet is quoting an assumption.
2. **Treating the three-cell picture as a closed system.** The Ferrel cell is
   thermally indirect; eddies supply its momentum. Suppress the eddies and the
   cells change place and strength.
3. **Assuming geostrophy near the equator.** $f\to0$ there and the balance
   fails; the equatorial circulation is qualitatively different.
4. **Quoting a single cell-edge latitude.** Section 5's table spans a factor of
   2.1 across assumptions that are all defensible.
5. **Confusing what must be carried with what carries it.** The transport in
   Section 6 is a requirement; the partition between the mean circulation,
   eddies and the ocean is a modelling choice.
6. **Forgetting that the plateau's exponent came from conservation.** If the
   flow were not angular-momentum conserving, the flat tropical tropopause
   would not follow, and no amount of radiation physics would supply it.

## Mastery checkpoint

Complete this without notes.

> A zonal-mean model gives a tropical tropospheric wind
> $u_M(20^\circ) = 57.8\ \mathrm{m\,s^{-1}}$ at the tropopause and
> $u = 0$ at the surface, with a $10$ km deep tropopause and a uniform tropical
> surface potential temperature. **(a)** State the specific angular momentum of
> air at $20^\circ$ that this wind corresponds to, and check that it equals the
> equatorial value $\Omega a^2$ to three significant figures. **(b)** Use the
> thermal-wind relation to estimate the meridional potential-temperature
> gradient at the tropopause. **(c)** Give the tropopause potential-temperature
> drop at $20^\circ$ two ways: from the quartic form and from the full bracket.
> **(d)** Explain in one sentence why a bigger equilibrium contrast gives a wider
> cell while a deeper tropopause gives a narrower one. **(e)** State one
> measurement that would distinguish an angular-momentum-conserving tropical
> circulation from a frictionally controlled one.

A worked version of (a)–(c) appears in the lesson-01
[solutions](exercises/01-global-circulation-solutions.md).

## Common pitfalls

- **Watching the wrong residual.** "Conservation holds" must be checked as
  $|M/M_\text{eq} - 1|\sim10^{-16}$; a test that passes at $10^{-2}$ has not
  tested conservation.
- **Mixing latitude conventions.** $y = a\phi$ requires $\phi$ in radians; the
  demonstration works in degrees at the interface and converts everywhere else.
- **Using a quadratic picture for the plateau.** The whole signature is that
  the exponent is 4; a $\sin^2$ fit will "confirm" the wrong theory.
- **Quoting a $\bar v$ from Section 6 without its closure.**
- **Treating the Ferrel cell as a heat engine.** It is a momentum sink.

## Related modules

- [02 Monsoons, Regional Circulation and Teleconnections](02-monsoons-and-regional.md) —
  what happens when the zonal symmetry of this lesson is replaced by a
  land–sea contrast.
- [03 Cyclones, Fronts and Severe Weather Dynamics](03-storms-and-fronts.md) —
  the eddies of Section 7, treated as growing disturbances rather than as
  bookkeeping.
- [04 Atmospheric Waves: Rossby, Kelvin, Gravity Waves](04-atmospheric-waves.md) —
  the wave dynamics behind the eddy fluxes.
- [16-01 Atmospheric Structure and Thermodynamics](../01-atmospheric-structure-and-thermodynamics/README.md) —
  the thermodynamic framework this circulation acts on.
- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  where the flux profile of Section 6 comes from.
- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  what changing the circulation does to global temperature.
- [02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) —
  the rotating-fluid mechanics used here.
- [15-01 Physical Oceanography](../../15-oceanography-marine/01-physical-oceanography/README.md) —
  the ocean's half of the same transport problem.
