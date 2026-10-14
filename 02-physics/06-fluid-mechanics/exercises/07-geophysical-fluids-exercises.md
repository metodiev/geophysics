# Exercises — 02-06-07 Rotating Fluids, Coriolis Effect and Geostrophic Balance

Attempt these **closed-book** before opening the
[solutions](./07-geophysical-fluids-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/rotating_fluids_demo.py`](../code/rotating_fluids_demo.py) require you
to run it and report its actual output. Use $\Omega = 7.292\,115\times10^{-5}$
rad s⁻¹ (the WGS 84 defining value), $g = 9.81\ \mathrm{m\,s^{-2}}$ and, where a
water density is needed, $\rho = 1025\ \mathrm{kg\,m^{-3}}$ (nominal).

---

## ★ Foundational

**★1.** Coriolis parameter and inertial period.

(a) Compute $f$ at latitudes 0°, 30°, 45°, 60° and 90°.
(b) Compute the inertial period $2\pi/f$ at each of those latitudes.
(c) State what happens to both at the equator and why geostrophic balance is
then undefined.
(d) Compute the planetary vorticity $2\Omega$ and compare it with $f$ at 45°.

---

**★2.** Compute the Rossby number $Ro = U/(fL)$ and classify each flow as
rotation-dominated, intermediate or advection-dominated:

(a) a bathtub drain, $U = 0.1\ \mathrm{m\,s^{-1}}$, $L = 0.5$ m, 45°;
(b) a river, $U = 1\ \mathrm{m\,s^{-1}}$, $L = 1000$ m, 45°;
(c) a coastal current, $U = 0.3\ \mathrm{m\,s^{-1}}$, $L = 10$ km, 45°;
(d) an ocean gyre, $U = 0.1\ \mathrm{m\,s^{-1}}$, $L = 1000$ km, 35°;
(e) a weather system, $U = 10\ \mathrm{m\,s^{-1}}$, $L = 1000$ km, 45°.

---

**★3.** Geostrophic conversion at 45°.

(a) A sea-surface slope of $10^{-6}$ (10 cm per 100 km) — compute the
geostrophic speed.
(b) What slope is needed for a 0.1 m s⁻¹ current?
(c) Repeat (a) and (b) at 30° and at 60°, and state how the required slope varies
with latitude.
(d) State which sign of slope gives which direction of current in the northern
hemisphere, and why a sign error here is a sign error in the gyre.

---

**★4.** Ekman parameters.

(a) Compute the Ekman depth $\delta_E = \sqrt{2\nu/f}$ at 45° for
$\nu = 10^{-2}$ and $10^{-1}$ m² s⁻¹.
(b) Compute the Ekman transport per unit length for a wind stress of
$0.1\ \mathrm{N\,m^{-2}}$ at 45°.
(c) State why the transport does not depend on $\nu$ but the depth does.
(d) State the direction of the transport relative to the wind in each hemisphere.

---

## ★★ Applied

**★★5.** Thermal wind at 45°, with $\alpha = 2\times10^{-4}$ K⁻¹.

(a) Compute $\partial u/\partial z$ for a northward temperature increase of 2 K
per 100 km.
(b) Compute the velocity difference across 500 m and across 1000 m.
(c) Repeat at 30° and state the latitude dependence.
(d) State why the thermal-wind relation cannot be applied at the equator, and
name the approximation that replaces it.

---

**★★6.** Run
[`../code/rotating_fluids_demo.py`](../code/rotating_fluids_demo.py).

(a) Report $f$ and the inertial period at 45° and at the equator.
(b) Report $Ro$ for the bathtub, the coastal current and the ocean gyre.
(c) Report the geostrophic speed for a $10^{-6}$ slope at 45° and the slope
required for 0.1 m s⁻¹.
(d) Report the Ekman depth at 45° for $\nu = 0.1$ m² s⁻¹ and the Ekman transport
for $\tau = 0.1\ \mathrm{N\,m^{-2}}$.
(e) Report the internal Rossby radius for $N = 10^{-2}$ s⁻¹, $H = 1$ km at 45°.

---

**★★7.** The internal Rossby radius $L_R = NH/|f|$.

(a) Compute $L_R$ for $N = 10^{-2}$ s⁻¹, $H = 1000$ m at 45°, and at 30°, and at
60°.
(b) Compute $L_R$ for the same $N$ and $H = 8000$ m at 60°.
(c) State what $L_R$ means for the eddy scale of the ocean and for the grid
spacing of a balanced numerical model.
(d) State what happens to $L_R$ at the equator and what that implies for
equatorial dynamics.

---

**★★8.** The bathtub question, quantitatively.

(a) Compute $Ro$ for $U = 0.1\ \mathrm{m\,s^{-1}}$, $L = 0.5$ m at 45°.
(b) Compute the ratio of the drain time (60 s) to the inertial period.
(c) Compute the basin size $L$ for which $Ro = 1$ at $U = 0.1\
\mathrm{m\,s^{-1}}$ at 45°.
(d) Using (c), explain why the claim "bathwater drains one way in the northern
hemisphere and the other way in the southern" is quantitatively false, and state
what does determine the vortex sense.

---

## ★★★ Research-oriented

**★★★9.** Potential vorticity.

(a) For a shallow homogeneous layer of depth $H(x,y,t)$ with depth-averaged
velocity $\mathbf{u}$, start from the depth-averaged continuity equation
$\partial H/\partial t + \nabla\cdot(H\mathbf{u}) = 0$ and the depth-averaged
vorticity equation, and show that
$\mathrm{D}/\mathrm{D}t\left[(\zeta+f)/H\right] = 0$ in the absence of friction
and vortex stretching by other means.
(b) A column of fluid at rest at 30° latitude is moved northwards to 45° without
changing its depth. Compute the relative vorticity it acquires and the rotation
sense.
(c) Repeat with the depth halved instead (no change in latitude). Compute the
relative vorticity.
(d) State one geophysical phenomenon that each of (b) and (c) explains, and state
the two conditions in which the conservation law fails.

---

**★★★10.** Rotating convection and the outer core.

(a) Rotating convection is characterised by the Ekman number
$Ek = \nu/(\Omega d^2)$ and the modified Rayleigh number
$Ra_\Omega = Ra\,Ek$ (or by the convective Rossby number
$Ro_c = (Ra/(Pr\,Ta))^{1/2}$). For the outer core take $\nu = 10^{-6}$ m² s⁻¹
(liquid metal), $d = 2.26\times10^6$ m, $\Omega = 7.292\times10^{-5}$ s⁻¹. Compute
$Ek$.
(b) For the mantle of lesson 06, compute $Ek = \nu/(\Omega d^2)$ using
$\nu = 3.03\times10^{17}$ m² s⁻¹ and $d = 2.891\times10^6$ m. Compare with (a).
(c) Explain why the outer core's small Ekman number implies columnar flow aligned
with the rotation axis, and name the theorem that states it.
(d) State two observational consequences of rotation-dominated convection in the
outer core, and explain why a mantle-convection model and a geodynamo model
require different equations even though both solve the same Boussinesq momentum
balance.
