# Solutions — 02-06-07 Rotating Fluids, Coriolis Effect and Geostrophic Balance

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. $\Omega = 7.292\,115\times10^{-5}$ rad s⁻¹ is
> the WGS 84 defining value (handbook Sec. 3.1); it is exact by agreement.

---

## ★1 — Coriolis parameter and inertial period

**(a)–(b)** $f = 2\Omega\sin\phi$, $T_i = 2\pi/f$:

| Latitude | $f$ (s⁻¹) | $T_i$ (h) |
|---|---|---|
| 0° | 0 | infinite |
| 30° | $7.292\times10^{-5}$ | 23.934 |
| 45° | $1.031\times10^{-4}$ | 16.924 |
| 60° | $1.263\times10^{-4}$ | 13.819 |
| 90° | $1.458\times10^{-4}$ | 11.967 |

**(c)** At the equator $\sin\phi = 0$, so $f = 0$ and the inertial period
diverges. Geostrophic balance $f\hat{z}\times\mathbf{u} = -\nabla p/\rho$ cannot
be solved for $\mathbf{u}$ when $f = 0$: the balance degenerates, the required
pressure gradient for any given current is zero, and the Rossby number is
infinite for any finite flow. Equatorial dynamics is instead governed by
equatorial wave theory, in which the *variation* of $f$ with latitude plays the
central role.

**(d)** $2\Omega = 1.45842\times10^{-4}$ s⁻¹; at 45°, $f = 0.7071\times2\Omega$,
i.e. $1.031\times10^{-4}$ s⁻¹. The planetary vorticity is the maximum possible
value of $f$, attained at the poles.

---

## ★2 — Rossby numbers

| Flow | $L$ (m) | $U$ (m s⁻¹) | $\phi$ | $f$ (s⁻¹) | $Ro$ | Regime |
|---|---|---|---|---|---|---|
| (a) bathtub | 0.5 | 0.1 | 45° | $1.031\times10^{-4}$ | $1.94\times10^{3}$ | advection-dominated |
| (b) river | 1000 | 1 | 45° | $1.031\times10^{-4}$ | 9.70 | advection-dominated |
| (c) coastal current | $10^{4}$ | 0.3 | 45° | $1.031\times10^{-4}$ | 0.291 | intermediate |
| (d) ocean gyre | $10^{6}$ | 0.1 | 35° | $8.365\times10^{-5}$ | $1.20\times10^{-3}$ | rotation-dominated |
| (e) weather system | $10^{6}$ | 10 | 45° | $1.031\times10^{-4}$ | $9.70\times10^{-2}$ | rotation-dominated |

The range is six orders of magnitude. Note that the river is *not* a
rotating-fluid problem even at $L = 1$ km, while the weather system at the same
length scale and a hundred times the speed *is* — because $U$ and $L$ appear
together in $Ro$, so a slow, wide flow is more rotation-dominated than a fast,
narrow one.

---

## ★3 — Geostrophic conversions at 45°

**(a)** $u = -(g/f)\,\partial\eta/\partial y = -(9.81/1.031\times10^{-4})\times
10^{-6} = \mathbf{-0.0951\ m\,s^{-1}} = -9.51$ cm s⁻¹. The negative sign means
the current is westward for a surface rising northward (in the northern
hemisphere).

**(b)** $\partial\eta/\partial y = -fu/g = -1.031\times10^{-4}\times0.1/9.81 =
-1.051\times10^{-6}$, i.e. a **10.5 cm drop over 100 km**.

**(c)**

| Latitude | $g/f$ (m² s⁻¹) | $u$ for slope $10^{-6}$ (cm s⁻¹) | slope for 0.1 m s⁻¹ (cm per 100 km) |
|---|---|---|---|
| 30° | $1.345\times10^{5}$ | $-13.45$ | 7.43 |
| 45° | $9.513\times10^{4}$ | $-9.51$ | 10.51 |
| 60° | $7.767\times10^{4}$ | $-7.77$ | 12.87 |

The required slope is proportional to $f$, i.e. to $\sin\phi$: **the same current
requires a larger sea-surface slope at higher latitude.** This is why the dynamic
topography of the ocean has a strong latitudinal structure even where the
currents are similar.

**(d)** With $u = -(g/f)\partial\eta/\partial y$, a slope rising *northward*
($\partial\eta/\partial y > 0$) gives a *westward* current, and vice versa. Since
$f$ changes sign between hemispheres but the pressure gradient does not, the same
slope drives opposite currents in the two hemispheres — and a sign error flips
the circulation of the entire gyre, which is the classic way an ocean model is
found to have its Coriolis term incorrectly coded.

---

## ★4 — Ekman parameters

**(a)** $\delta_E = \sqrt{2\nu/|f|}$ at 45° ($f = 1.031\times10^{-4}$ s⁻¹):
for $\nu = 10^{-2}$ m² s⁻¹, $\delta_E = \mathbf{13.93\ m}$; for
$\nu = 10^{-1}$ m² s⁻¹, $\delta_E = \mathbf{44.04\ m}$.

**(b)** $M_E = \tau/(\rho f) = 0.1/(1025\times1.031\times10^{-4}) =
\mathbf{0.946\ m^2\,s^{-1}} = 8.17\times10^{4}$ m² per day**.

**(c)** The transport follows from integrating the Coriolis balance over the layer
and imposing that the stress vanish at the base: the viscosity determines *how*
the stress is distributed vertically (and hence the layer thickness), but its
integral is fixed by the surface stress and the Coriolis parameter alone. This is
why the transport is the robust prediction and the depth is the model-dependent
one.

**(d)** To the **right** of the wind in the northern hemisphere, to the **left**
in the southern hemisphere. This is the direct consequence of the sign of $f$ in
equation (8).

---

## ★★5 — Thermal wind at 45°

**(a)** With $\alpha = 2\times10^{-4}$ K⁻¹ and a northward temperature increase
of $2$ K per 100 km ($\partial T/\partial y = 2\times10^{-5}$ K m⁻¹):

$$\frac{\partial u}{\partial z} = \frac{g\alpha}{f}\frac{\partial T}{\partial y}
= \frac{9.81\times2\times10^{-4}}{1.031\times10^{-4}}\times2\times10^{-5} =
\mathbf{3.81\times10^{-4}\ s^{-1}}.$$

**(b)** Across 500 m: $3.81\times10^{-4}\times500 = \mathbf{0.190\ m\,s^{-1}}$;
across 1000 m: $\mathbf{0.381\ m\,s^{-1}}$.

**(c)** At 30° ($f = 7.292\times10^{-5}$), the shear is
$3.81\times10^{-4}\times(1.031/0.7292) = \mathbf{5.38\times10^{-4}\ s^{-1}}$ and
the 500 m difference is 0.269 m s⁻¹. The shear is **inversely proportional to
$f$**, i.e. larger at low latitude for the same temperature gradient.

**(d)** At the equator $f = 0$, so the thermal-wind relation predicts infinite
shear and is meaningless. What replaces it is the **equatorial thermal-wind
balance**, in which the vertical shear is related to the *second* derivative of
the pressure field in the meridional direction, and the relevant wave dynamics is
the equatorial wave guide. Applying the mid-latitude relation at the equator is a
regime error, not a small inaccuracy.

---

## ★★6 — Reading the demo

**(a)** At 45°: $f = 1.03126\times10^{-4}$ s⁻¹, inertial period 16.924 h. At the
equator: $f = 0$, period "infinite".

**(b)** Bathtub $Ro = 1.939\times10^{3}$; coastal current $Ro = 2.909\times10^{-1}$;
ocean gyre $Ro = 1.195\times10^{-3}$.

**(c)** For a $10^{-6}$ slope at 45°, $u_g = -9.513$ cm s⁻¹ (the demo prints
$-0.0951$ m s⁻¹). The slope required for 0.1 m s⁻¹ is $-1.051\times10^{-6}$, i.e.
10.51 cm per 100 km.

**(d)** $\delta_E = 44.04$ m for $\nu = 0.1$ m² s⁻¹; $M_E = 0.946$ m² s⁻¹
(81 737.5 m² per day) for $\tau = 0.1$ N m⁻².

**(e)** $L_R = N H/|f| = 10^{-2}\times1000/1.031\times10^{-4} =
\mathbf{97.0\ km}$.

---

## ★★7 — The Rossby radius of deformation

**(a)** $L_R = NH/|f|$ with $N = 10^{-2}$ s⁻¹, $H = 1000$ m:

| Latitude | $f$ (s⁻¹) | $L_R$ (km) |
|---|---|---|
| 30° | $7.292\times10^{-5}$ | 137.1 |
| 45° | $1.031\times10^{-4}$ | 97.0 |
| 60° | $1.263\times10^{-4}$ | 79.2 |

**(b)** $H = 8000$ m at 60°: $L_R = 10^{-2}\times8000/1.263\times10^{-4} =
\mathbf{633.4\ km}$.

**(c)** $L_R$ is the scale of the largest eddies that can exist in geostrophic
balance, and therefore the natural scale of ocean mesoscale eddies and of
atmospheric synoptic systems. A balanced numerical model must resolve scales of
order $L_R$ or smaller to represent eddy dynamics; a grid coarser than $L_R$
cannot, and must parameterise the eddies. This is why ocean climate models with
100 km grids need an eddy parameterisation, and why eddy-resolving models run at
1–10 km.

**(d)** At the equator $f \to 0$ and $L_R \to \infty$ (for fixed $N$, $H$): there
is no finite scale below which balanced dynamics applies, so **there is no
geostrophic eddy regime at the equator**. The equatorial dynamics is instead
wave-dominated, with the equatorial Rossby radius
$L_{eq} = \sqrt{NH/\beta}$ replacing $NH/f$ as the relevant scale — a genuinely
different theory, not a limiting case of the mid-latitude one.

---

## ★★8 — The bathtub

**(a)** $Ro = U/(fL) = 0.1/(1.031\times10^{-4}\times0.5) =
\mathbf{1.94\times10^{3}}$. Equivalently, from the accelerations,
$fU/(U^2/L) = 5.16\times10^{-4}$ — the ratio of the Coriolis to the advective
acceleration, which is $1/Ro$, i.e. $5.2\times10^{-4}$.

**(b)** $60\ \mathrm{s}/(2\pi/f) = 60/60\,927 = \mathbf{9.85\times10^{-4}}$. The
basin empties **about a thousand times faster** than the Earth can organise a
rotating flow in it.

**(c)** For $Ro = 1$: $L = U/f = 0.1/1.031\times10^{-4} = \mathbf{970\ m}$. A
basin would have to be nearly a kilometre across, with a 0.1 m s⁻¹ flow, before
rotation began to matter at all.

**(d)** The mechanism requires $Ro \lesssim 1$; a bathtub is at $Ro \sim 2\times
10^{3}$ and would have to be 970 m across on the same flow. The claim is false by
three orders of magnitude in $Ro$ and three in the timescale ratio. What
determines the vortex sense is the **residual angular momentum of the water when
the plug is pulled** — the swirl acquired during filling, the asymmetry of the
basin and of the drain — plus the requirement that angular momentum be conserved
as the water converges. Careful experiments that eliminate the residual swirl
(by waiting many drain times, or by symmetric filling) find no reproducible
Coriolis-driven rotation at laboratory scale, which is the experimental
confirmation of the estimate above.

---

## ★★★9 — Potential vorticity

**(a)** The depth-averaged continuity equation is
$\partial H/\partial t + \nabla\cdot(H\mathbf{u}) = 0$. In two dimensions, take
the $z$-component of the curl of the shallow-water momentum equation; the
pressure-gradient term vanishes (it is a gradient) and, neglecting friction and
other sources, the result is the vorticity equation
$\mathrm{D}(\zeta+f)/\mathrm{D}t = -(\zeta+f)\nabla\cdot\mathbf{u}$. Using
continuity to write $\nabla\cdot\mathbf{u} = -\dfrac{1}{H}\dfrac{\mathrm{D}H}
{\mathrm{D}t}$ and substituting:

$$\frac{\mathrm{D}(\zeta+f)}{\mathrm{D}t} = \frac{\zeta+f}{H}
\frac{\mathrm{D}H}{\mathrm{D}t}
\;\Longrightarrow\;
\frac{\mathrm{D}}{\mathrm{D}t}\left[\frac{\zeta+f}{H}\right] = 0.$$

**(b)** With $H$ constant, $\zeta + f$ is constant. Moving northwards changes $f$
by $\Delta f = f_{45}-f_{30} = 1.031\times10^{-4} - 7.292\times10^{-5} =
+3.02\times10^{-5}$ s⁻¹, so the column acquires
$\zeta = -\Delta f = \mathbf{-3.02\times10^{-5}\ s^{-1}}$: **negative, i.e.
anticyclonic (clockwise) in the northern hemisphere.**

**(c)** With $f$ constant and $H$ halved, $(\zeta+f)/(H/2) = f/H$ gives
$\zeta + f = f/2$, so
$\zeta = -f/2 = \mathbf{-5.16\times10^{-5}\ s^{-1}}$: again **anticyclonic**, by
squashing the column.

**(d)** Case (b) is the mechanism of the $\beta$-effect: a column displaced
northwards or southwards changes its relative vorticity, which provides the
restoring force for **Rossby waves** and underlies the Sverdrup balance and
western-boundary-current intensification. Case (c) is **topographic steering and
vortex stretching by Ekman pumping**: squashing a water column (downwelling,
Ekman pumping) generates anticyclonic vorticity, and stretching it (upwelling,
Ekman suction) generates cyclonic vorticity — which is why wind-driven
upwelling regions are associated with cyclonic vorticity and eddy generation.
The two conditions under which the conservation law fails are **friction** (most
importantly in Ekman layers, where PV is produced or destroyed) and **diabatic
heating or density change** (buoyancy sources), together with non-conservative
body forces. In the real ocean the interior approximately conserves PV, and the
boundary layers are precisely where it does not — which is where the energy is
exchanged and the circulation is closed.

---

## ★★★10 — Rotating convection and the outer core

**(a)** $Ek = \dfrac{\nu}{\Omega d^2} =
\dfrac{10^{-6}}{7.292\,115\times10^{-5}\times(2.26\times10^6)^2} =
\dfrac{10^{-6}}{3.725\times10^{8}} = \mathbf{2.68\times10^{-15}}$.

**(b)** $Ek = \dfrac{3.03\times10^{17}}{7.292\,115\times10^{-5}\times
(2.891\times10^6)^2} = \dfrac{3.03\times10^{17}}{6.095\times10^{8}} =
\mathbf{5.0\times10^{8}}$.

**(c)** $Ek = 2.7\times10^{-15}$ means viscous effects are fifteen orders of
magnitude smaller than rotational effects: the fluid is effectively inviscid with
respect to rotation. In the limit $Ek \to 0$ (equivalently $Ro \to 0$) the
leading-order balance is geostrophic, and its curl gives the
**Taylor–Proudman theorem**, $\partial\mathbf{u}/\partial z = 0$: the flow is
invariant along the rotation axis and organises itself into columns. In a sphere
the columns are tangent cylinders coaxial with the rotation axis, and in the outer
core these are the structures that the geomagnetic secular variation is
interpreted in terms of.

**(d)** Two observational consequences: (i) the **alignment of the geomagnetic
field** with the rotation axis over geological time, which is the signature of
columnar, rotation-dominated convection rather than isotropic convection; and
(ii) the **tangent-cylinder structure of the secular variation** — the
concentration of geomagnetic field changes in patterns consistent with flow
constrained to cylinders coaxial with the rotation axis. Both follow from the
Taylor–Proudman constraint, not from any assumption about the field geometry.

A mantle-convection model and a geodynamo model need different equations even
though both start from the same Boussinesq momentum balance, because the
*retained terms* are different. The mantle has $Ek \sim 10^{8}$ — rotation is
utterly negligible, and the balance is between buoyancy and viscous stress, with
a temperature-dependent viscosity and a free surface. The outer core has
$Ek \sim 10^{-15}$: rotation dominates, the Coriolis term is the leading balance,
and — critically — the fluid is an **electrical conductor**, so the Lorentz force
$\mathbf{J}\times\mathbf{B}$ appears in the momentum equation and the induction
equation must be solved alongside it. Two systems with the same starting equation
can have entirely different physics depending on which terms survive; recognising
this is the central skill of this module, and the reason the "which terms do you
drop, and what does it cost?" table of lesson 02 is the frame for everything
that follows.
