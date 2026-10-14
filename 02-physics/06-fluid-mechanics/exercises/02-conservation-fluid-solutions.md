# Solutions — 02-06-02 Continuity and Momentum Equations; Navier-Stokes

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Viscosities and densities are the nominal
> values stated in the exercise.

---

## ★1 — Continuity and acceleration

**(a)** $\nabla\cdot\mathbf{u} = \partial_x(ax) + \partial_y(-ay) = a - a =
\mathbf{0}$. The flow is incompressible everywhere, for any $a$: this is the
classic **stagnation-point (or hyperbolic) flow**, with inflow along one axis
and outflow along the other.

**(b)** Equation (8) gives $\dfrac{1}{\rho}\dfrac{\mathrm{D}\rho}{\mathrm{D}t} =
-\nabla\cdot\mathbf{u} = 0$, so a uniform density stays uniform. This is how an
incompressible field can still stretch a parcel: it stretches in one direction
and compresses in the other.

**(c)** $\mathrm{D}\mathbf{u}/\mathrm{D}t = u\,\partial_x\mathbf{u} +
v\,\partial_y\mathbf{u} = ax\,(a,0,0) + (-ay)\,(0,-a,0) = (a^2x,\;a^2y,\;0)$.
The acceleration points **away from the origin** in both directions: this is a
pure straining flow with no rotation.

**(d)** $a>0$ is a flow converging along $y$ and diverging along $x$ (as
computed: the acceleration is outward in both). A geophysical example of
divergence at a large scale is a mantle upwelling beneath a rift; of convergence,
a subduction zone where surface material is consumed. The sign alone gives the
topology, not the direction of gravity-driven flow.

---

## ★2 — Material versus local derivative

**(a)** $\partial T/\partial t = 2$ K s⁻¹ and
$\mathbf{u}\cdot\nabla T = 1\times5 = 5$ K s⁻¹.

**(b)** $\mathrm{D}T/\mathrm{D}t = 5 + 2 = \mathbf{7}$ K s⁻¹.

**(c)** With $T = 20 + 5(x-t)$: $\partial T/\partial t = -5$ K s⁻¹,
$\mathbf{u}\cdot\nabla T = +5$ K s⁻¹, so $\mathrm{D}T/\mathrm{D}t = 0$.

**(d)** In (b) the parcel is both carried into a warmer place (5 K s⁻¹) and the
field itself is warming (2 K s⁻¹), so a parcel warms by 7 K s⁻¹. In (c) the
pattern translates at exactly the fluid speed: the field at a fixed point
cools at 5 K s⁻¹ and the parcel is advected into warmer fluid at exactly
5 K s⁻¹, so the parcel experiences **no change at all**. Case (c) is a *steady
solution* of the advection equation, and it makes the point of the section: a
field can change rapidly in time at a fixed point while changing not at all for
the fluid — and vice versa.

---

## ★3 — Plane Poiseuille flow

**(a)** $u_{\text{max}} = \dfrac{Gh^2}{8\mu} =
\dfrac{5\times10^3\times(2\times10^{-3})^2}{8\times10^{-3}} = \mathbf{2.5\
\mathrm{m\,s^{-1}}}$, and
$u_{\text{mean}} = \dfrac{Gh^2}{12\mu} = 1.667\ \mathrm{m\,s^{-1}}$.

**(b)** $Q = h\,u_{\text{mean}} = 2\times10^{-3}\times1.667 =
\mathbf{3.33\times10^{-3}\ \mathrm{m^2\,s^{-1}}}$ per unit width.

**(c)** $u = \dfrac{G}{2\mu}(hy - y^2)$, so
$\mathrm{d}u/\mathrm{d}y = \dfrac{G}{2\mu}(h-2y)$ and
$\mathrm{d}^2u/\mathrm{d}y^2 = -\dfrac{G}{\mu}$, hence
$\mu\,\mathrm{d}^2u/\mathrm{d}y^2 = -G$, which equals $-\mathrm{d}p/\mathrm{d}x$
by the definition of $G$. Verified.

**(d)** A circular pipe of radius $a$ has $Q = \pi G a^4/(8\mu)$ and
$u_{\text{max}} = Ga^2/(4\mu)$; a slot has $Q = G h^3/(12\mu)$ per unit width
and $u_{\text{max}} = Gh^2/(8\mu)$. The ratio of mean to maximum is $1/2$ for the
pipe and $2/3$ for the slot, so *the same maximum* at the same length scale gives
$4/3$ times the mean velocity in a slot. Using a pipe formula for a fracture is
therefore a 33 per cent error on the mean velocity — and fractures in rock are
slots, not pipes.

---

## ★4 — Reynolds numbers

| Case | $Re$ | Dominant term | Entitled approximation |
|---|---|---|---|
| (a) fracture, $U = 0.05$ m s⁻¹, $L = 5$ mm | $1000\times0.05\times5\times10^{-3}/10^{-3} = 250$ | both matter; viscous sets the profile | Lubrication (lubrication-thin-film) approximation; *not* Stokes |
| (b) air past a 1 m object | $1.2\times10\times1/1.8\times10^{-5} = 6.7\times10^{5}$ | inertia | Euler away from the surface plus a boundary layer; turbulence is inevitable |
| (c) magma, $U = 0.01$ m s⁻¹, $L = 2$ m | $2500\times0.01\times2/100 = 0.5$ | viscous | Stokes (creeping) flow |

The contrast between (a) and (c) at velocities within a factor of five of each
other is the whole content of the Reynolds number: the *material* (through
$\mu/\rho$) and the *scale* (through $L$) matter as much as the speed.

---

## ★★5 — Nondimensionalisation

**(a)** Substitute $\mathbf{u} = U\mathbf{u}^*$, $x = Lx^*$, $p = \rho U^2 p^*$.
Then $\nabla = \nabla^*/L$ and $\mathbf{u}\cdot\nabla = (U/L)\mathbf{u}^*\cdot
\nabla^*$, and the viscous term is $\mu U\nabla^{*2}\mathbf{u}^*/L^2$. Dividing
the whole equation by $\rho U^2/L$:

$$\mathbf{u}^*\cdot\nabla^*\mathbf{u}^* = -\nabla^*p^* +
\frac{\mu}{\rho UL}\nabla^{*2}\mathbf{u}^* + \frac{gL}{U^2}\hat{g},
\qquad Re = \frac{\rho UL}{\mu}, \quad Fr = \frac{U}{\sqrt{gL}}.$$

**(b)** $Re = 1000\times1\times10/10^{-3} = \mathbf{10^{7}}$; using the depth
scale $h = 1$ m for the Froude number, $Fr = 1/\sqrt{9.81} = \mathbf{0.319}$.

**(c)** $1/Re = 10^{-7}$: the viscous term is negligible *for the interior*.
$1/Fr^2 = U^2/(gL) = 1/98.1 = 1.02\times10^{-2}$, which is small but two orders
of magnitude larger than $1/Re$; gravity cannot be dropped, because it is the
term that sets the free surface and the pressure profile. The correct statement
is: drop viscosity in the interior, retain gravity everywhere, and restore
viscosity in a boundary layer of thickness $\delta \sim L/\sqrt{Re}$.

**(d)** The Froude number decides: $Fr = 0.319 < 1$ is **subcritical**
(tranquil) flow, in which a surface disturbance can propagate upstream. The
threshold is $Fr = 1$, corresponding to a Froude number built on the water depth,
not on an arbitrary length.

---

## ★★6 — Reading the demo

**(a)** Worst residual $1.565\times10^{-7}\ \mathrm{Pa\,m^{-1}}$, against
$\mu\,\mathrm{d}^2u/\mathrm{d}y^2 = -10^4$ and $-\mathrm{d}p/\mathrm{d}x = +10^4$
Pa m⁻¹. The residual is twelve orders of magnitude below the terms, i.e. at the
round-off of the finite-difference formula.

**(b)** Numeric $Q = 8.333333\times10^{-4}$ m² s⁻¹; analytic $h u_{\text{mean}} =
8.333333\times10^{-4}$ m² s⁻¹; relative error $1.25\times10^{-11}$.

**(c)** Mantle: inertia/viscous $= 3.3\times10^{-21}$, verdict "Stokes (drop
inertia)". Ocean western boundary current: $1.025\times10^{11}$, verdict "Euler
(drop viscosity)". The two verdicts are 31 orders of magnitude apart, which is
why one module can contain both the mantle and the atmosphere without
inconsistency.

**(d)** The fracture row gives inertia/viscous $= 10$. That is $Re = 10$ based on
the aperture. Darcy's law is generally trusted while the pore-scale Reynolds
number is below roughly $1$–$10$, so this case sits **at the limit** and a
careful calculation would not rely on Darcy. A second calculation makes the point
sharper: the appropriate model for an open fracture is the cubic law from
Poiseuille flow (lesson 05), which is exact for a smooth parallel-plate fracture
and remains laminar to $Re$ of order $10^3$; inertia appears as a correction long
before the flow becomes turbulent. Darcy's law, by contrast, is a
*porous-medium* statement and should not be applied to a single open conduit at
all.

---

## ★★7 — Boussinesq validity

**(a)** $\alpha\Delta T = 3\times10^{-5}\times2500 = \mathbf{0.075}$.
**(b)** $2\times10^{-4}\times25 = \mathbf{5\times10^{-3}}$.
**(c)** $10^{-3}\times300 = \mathbf{0.3}$.

Ranked: lake (0.005), mantle (0.075), hydrothermal system (0.3). The
Boussinesq approximation is excellent for the lake, good for the mantle and
**not valid** for the hydrothermal system, where a 30 per cent density change
means the flow is strongly compressible in the dynamical sense and variable
density must be retained throughout. In such systems one solves the equations
with a full equation of state — the physics of
[02-05-07 Phase Equilibria](../../05-thermodynamics/07-phase-equilibria.md).

---

## ★★8 — Stokes settling

**(a)** $w = \dfrac{2\times1650\times9.81\times(10^{-4})^2}{9\times10^{-3}} =
\mathbf{3.597\times10^{-2}\ \mathrm{m\,s^{-1}}}$.

**(b)** $Re = \dfrac{1000\times3.597\times10^{-2}\times2\times10^{-4}}{10^{-3}} =
\mathbf{7.19}$. The law is **not** self-consistent: it was derived by dropping
inertia, and $Re \approx 7$ means inertia is not negligible. The true settling
speed is lower than the Stokes prediction.

**(c)** For $a = 10^{-5}$ m, $w = 3.597\times10^{-4}\ \mathrm{m\,s^{-1}}$ and
$Re = 7.19\times10^{-3}$. Self-consistent.

**(d)** The demo prints exactly these numbers: $w = 3.597\times10^{-2}$ m s⁻¹
with $Re = 7.194$ for the $0.1$ mm grain, and $w = 3.597\times10^{-4}$
m s⁻¹ with $Re = 7.194\times10^{-3}$ for the $0.01$ mm grain. There is no
discrepancy to reconcile: the two agree because $w \propto a^2$ and $Re \propto
w a \propto a^3$, so a tenfold reduction in radius reduces $Re$ by $10^3$ — from
7.19 to $7.19\times10^{-3}$. This factor-of-1000 sensitivity is why sand
(0.1 mm) settles outside the Stokes regime while silt and clay settle well
inside it, and why the Stokes settling law must always be accompanied by its
Reynolds-number self-check.

---

## ★★★9 — The vorticity equation

**(a)** Take the curl of (4) with $\rho$ constant and $\mathbf{g}$ conservative
(a gradient, hence curl-free):

$$\frac{\partial\boldsymbol{\omega}}{\partial t} +
\nabla\times(\mathbf{u}\cdot\nabla\mathbf{u}) = -\nabla\times(\nabla p/\rho) +
\nu\nabla^2\boldsymbol{\omega}.$$

The pressure term vanishes because the curl of a gradient is zero (for constant
density). Using the vector identity
$\mathbf{u}\cdot\nabla\mathbf{u} = \nabla(\tfrac12u^2) -
\mathbf{u}\times\boldsymbol{\omega}$ and taking the curl (the first term is a
gradient and vanishes):

$$\nabla\times(\mathbf{u}\cdot\nabla\mathbf{u}) =
-(\mathbf{u}\cdot\nabla)\boldsymbol{\omega} +
(\boldsymbol{\omega}\cdot\nabla)\mathbf{u} +
\boldsymbol{\omega}(\nabla\cdot\mathbf{u}),$$

and the last term vanishes by incompressibility. Collecting:

$$\boxed{\;\frac{\partial\boldsymbol{\omega}}{\partial t} +
(\mathbf{u}\cdot\nabla)\boldsymbol{\omega} =
(\boldsymbol{\omega}\cdot\nabla)\mathbf{u} +
\nu\nabla^2\boldsymbol{\omega}\;}$$

**(b)** The **vortex-stretching** term is $(\boldsymbol{\omega}\cdot\nabla)
\mathbf{u}$: the rate at which a vortex tube is stretched by the velocity
gradient, which amplifies vorticity by conservation of angular momentum. It
requires a velocity gradient **along** the vorticity direction — that is, three
dimensionality.

**(c)** In two-dimensional flow $\mathbf{u} = (u(x,y), v(x,y), 0)$ and
$\boldsymbol{\omega} = (0,0,\omega_z)$. Then
$(\boldsymbol{\omega}\cdot\nabla)\mathbf{u} = \omega_z\,\partial_z\mathbf{u} =
\mathbf{0}$, because nothing depends on $z$.

**(d)** With no stretching, vorticity in two dimensions is merely advected and
diffused; there is no mechanism to concentrate it into ever-smaller structures,
so enstrophy cascades *upgrade* to large scales (inverse cascade) rather than
downscale to dissipation. A purely two-dimensional model of the atmosphere
therefore cannot produce the small-scale intermittency of real turbulence, which
is why large-eddy and cloud-resolving models must be three-dimensional while
quasi-geostrophic models — which are formally two-dimensional — are used only
for the balanced, large-scale flow they were designed for.

---

## ★★★10 — Hydrostatic validity in a plume

**(a)** $w^2/L_z = 1^2/10^3 = 10^{-3}\ \mathrm{m\,s^{-2}}$.

**(b)** Ratio to gravity: $10^{-3}/9.81 = \mathbf{1.0\times10^{-4}}$.

**(c)** The vertical momentum equation is
$\rho\,\mathrm{D}w/\mathrm{D}t = -\partial_z p - \rho g$. The hydrostatic
approximation drops the left-hand side, so the fractional error in the vertical
pressure gradient is
$\dfrac{|\rho\,\mathrm{D}w/\mathrm{D}t|}{|\rho g|} \sim \dfrac{w^2/L_z}{g}$,
which is (b).

**(d)** $w^2/L_z = 30^2/10^4 = 0.09\ \mathrm{m\,s^{-2}}$; the ratio is
$0.09/9.81 = \mathbf{9.2\times10^{-3}}$, about **1 per cent**. A 1 per cent error
in the vertical pressure gradient sounds harmless but acts on the *pressure
perturbation* that drives the flow, not on the total pressure: the perturbation
is itself of order $\rho w^2$, so the relative error in the perturbation is of
order 1. This is why thunderstorm-scale models must be **non-hydrostatic**: the
check is not against $g$ but against the dynamically relevant pressure
perturbation. The same reasoning, with a different scale, decides whether an
ocean model may be hydrostatic.
