# Exercises — 02-06-02 Continuity and Momentum Equations; Navier-Stokes

Attempt these **closed-book** before opening the
[solutions](./02-conservation-fluid-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/navier_stokes_demo.py`](../code/navier_stokes_demo.py)
require you to run it and report its actual output. Take water as
$\rho = 1000\ \mathrm{kg\,m^{-3}}$, $\mu = 10^{-3}$ Pa s unless told otherwise.

---

## ★ Foundational

**★1.** A velocity field is $\mathbf{u} = (ax,\; -ay,\; 0)$ with $a$ a constant.

(a) Compute $\nabla\cdot\mathbf{u}$ and state whether the flow is
incompressible.
(b) Compute the material derivative of the density if the density is initially
uniform, using equation (8).
(c) Compute the acceleration field $\mathrm{D}\mathbf{u}/\mathrm{D}t$ by
differentiating directly.
(d) State what the sign of $a$ does to the flow and give a geophysical example
of each sign.

---

**★2.** The temperature field is $T(x,t) = 20 + 5x + 2t$ (K, $x$ in metres) and
the velocity is $\mathbf{u} = (1,0,0)$ m s⁻¹.

(a) Compute $\partial T/\partial t$ and $\mathbf{u}\cdot\nabla T$ separately.
(b) Compute $\mathrm{D}T/\mathrm{D}t$.
(c) A second field is $T = 20 + 5(x - t)$ with the same velocity. Compute both
terms and the material derivative.
(d) Explain the difference between (b) and (c) in words, relating it to why a
steady flow can still heat a parcel.

---

**★3.** Plane Poiseuille flow between plates a distance $h$ apart is
$u(y) = \dfrac{G}{2\mu}y(h-y)$ with $G = -\mathrm{d}p/\mathrm{d}x$.

(a) For $h = 2$ mm, $G = 5\times10^3\ \mathrm{Pa\,m^{-1}}$ and water, compute
$u_{\text{max}}$ and $u_{\text{mean}}$.
(b) Compute the volume flow rate per unit width.
(c) Verify $\mu\,\mathrm{d}^2u/\mathrm{d}y^2 = -G$ by differentiating twice.
(d) State why this flow is not the same as flow in a circular pipe, and give the
factor that differs.

---

**★4.** Compute the Reynolds number and state which term of the momentum
equation dominates:

(a) water at $0.05\ \mathrm{m\,s^{-1}}$ in a fracture of aperture 5 mm;
(b) air at $10\ \mathrm{m\,s^{-1}}$ past an object of size 1 m
($\rho = 1.2\ \mathrm{kg\,m^{-3}}$, $\mu = 1.8\times10^{-5}$ Pa s);
(c) basaltic magma at $0.01\ \mathrm{m\,s^{-1}}$ in a dyke of width 2 m
($\rho = 2500\ \mathrm{kg\,m^{-3}}$, $\mu = 100$ Pa s).
(d) For each, name the approximation you would be entitled to make.

---

## ★★ Applied

**★★5.** Starting from the steady incompressible momentum equation with a body
force, scale with $L$, $U$, $\rho U^2$:

(a) Show that the equation becomes
$\mathbf{u}^*\cdot\nabla^*\mathbf{u}^* = -\nabla^*p^* +
\frac{1}{Re}\nabla^{*2}\mathbf{u}^* + \frac{1}{Fr^2}\hat{g}$, and define $Re$ and
$Fr$.
(b) Compute $Re$ and $Fr$ for a river with $U = 1\ \mathrm{m\,s^{-1}}$,
$L = 10$ m, depth scale $h = 1$ m.
(c) Show that dropping the viscous term is justified and that dropping gravity
is not.
(d) State the dimensionless group whose magnitude decides whether the flow is
subcritical or supercritical, and compute it for part (b).

---

**★★6.** Run [`../code/navier_stokes_demo.py`](../code/navier_stokes_demo.py).

(a) Report the worst x-momentum residual and the size of the terms it is
compared against.
(b) Report the measured and analytic flow rates and their relative error.
(c) Report the inertia/viscous ratio for the mantle and for the ocean western
boundary current, and the verdict printed for each.
(d) For the "groundwater in a fracture" row, report the ratio and state whether
Darcy's law could be used there, justifying your answer with a second
calculation.

---

**★★7.** The Boussinesq approximation requires $\alpha\Delta T \ll 1$.

(a) Compute $\alpha\Delta T$ for the mantle with $\alpha = 3\times10^{-5}$
K⁻¹ and $\Delta T = 2500$ K.
(b) Compute it for a lake with $\alpha = 2\times10^{-4}$ K⁻¹ and
$\Delta T = 25$ K.
(c) Compute it for a hydrothermal system with $\Delta T = 300$ K and
$\alpha = 10^{-3}$ K⁻¹.
(d) Rank the three cases by validity of the Boussinesq approximation and state
what replaces it in the worst case.

---

**★★8.** Stokes' law for the settling speed of a sphere is
$w = \dfrac{2(\rho_s-\rho_f)ga^2}{9\mu}$.

(a) For a quartz grain of radius $0.1$ mm in water, compute $w$.
(b) Compute the Reynolds number $Re = \rho_f w (2a)/\mu$ and state whether the
law is self-consistent.
(c) Repeat for a radius of $0.01$ mm.
(d) Report the demo's values for the same two cases and reconcile any
difference. (The demo uses $\rho_s = 2650\ \mathrm{kg\,m^{-3}}$ and defines $Re$
with the diameter.)

---

## ★★★ Research-oriented

**★★★9.** Take the curl of the incompressible Navier–Stokes equation with
constant viscosity and a conservative body force.

(a) Show that the vorticity $\boldsymbol{\omega} = \nabla\times\mathbf{u}$
satisfies
$\dfrac{\partial\boldsymbol{\omega}}{\partial t} +
(\mathbf{u}\cdot\nabla)\boldsymbol{\omega} =
(\boldsymbol{\omega}\cdot\nabla)\mathbf{u} + \nu\nabla^2\boldsymbol{\omega}$.
(b) Identify the term responsible for vortex stretching and state in what kind
of flow it can generate vorticity.
(c) Show that in two-dimensional flow the stretching term vanishes identically.
(d) Explain, in two sentences, why (c) is the reason two-dimensional turbulence
behaves so differently from three-dimensional turbulence, and what that implies
for a "two-dimensional" model of the atmosphere.

---

**★★★10.** A convective plume in the atmosphere rises with a vertical velocity
$w = 1\ \mathrm{m\,s^{-1}}$ over a vertical scale $L_z = 1$ km.

(a) Estimate the vertical acceleration scale $w^2/L_z$.
(b) Compare it with $g$ and compute the ratio.
(c) Show from the vertical momentum equation that the fractional error in the
hydrostatic approximation is of order $w^2/(gL_z)$.
(d) A thunderstorm updraught reaches $30\ \mathrm{m\,s^{-1}}$ over 10 km.
Compute the ratio for that case and state whether the hydrostatic approximation
remains defensible.
