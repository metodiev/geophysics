# Exercises — 02-06-03 Viscous Flow, Reynolds Number and Boundary Layers

Attempt these **closed-book** before opening the
[solutions](./03-viscous-flow-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/viscous_flow_demo.py`](../code/viscous_flow_demo.py)
require you to run it and report its actual output. Take water as
$\rho = 1000\ \mathrm{kg\,m^{-3}}$, $\mu = 10^{-3}$ Pa s, $\nu = 10^{-6}$
m² s⁻¹ unless told otherwise.

---

## ★ Foundational

**★1.** Couette flow between plates 1 mm apart, the upper plate moving at
$0.1\ \mathrm{m\,s^{-1}}$, no pressure gradient.

(a) Write the velocity profile and compute the velocity at mid-gap.
(b) Compute the shear stress everywhere in the gap and state why it is uniform.
(c) Compute the shear rate.
(d) State which quantity a rotational viscometer measures and how it is
converted to $\mu$.

---

**★2.** A fracture has aperture $b = 0.5$ mm and is subject to a pressure
gradient $G = 10^4\ \mathrm{Pa\,m^{-1}}$, with water.

(a) Compute the flow rate per unit width from the cubic law.
(b) Compute the equivalent permeability $k = b^2/12$ in m² and in darcy (1
darcy $= 0.9869\times10^{-12}$ m²).
(c) Compute $u_{\text{mean}}$, $u_{\text{max}}$ and the Reynolds number based on
the aperture.
(d) Compute the total discharge for a fracture 10 m wide.

---

**★3.** A borehole of radius 0.05 m and length 100 m carries water driven by a
head loss of 1 m.

(a) Compute the pressure difference.
(b) Compute the volume flow rate from Hagen–Poiseuille.
(c) Compute the mean velocity and the Reynolds number based on the diameter.
(d) Compute the laminar friction factor $64/Re$ and state whether it is
applicable.

---

**★4.** Water flows at $0.1\ \mathrm{m\,s^{-1}}$ along a flat plate, and you
consider the boundary layer at $x = 10$ m.

(a) Compute $Re_x$.
(b) Compute the laminar Blasius thickness.
(c) Compute the turbulent thickness $\delta \approx 0.37x\,Re_x^{-1/5}$.
(d) State which of (b) and (c) applies and by what factor you would be wrong if
you quoted the other.

---

## ★★ Applied

**★★5.** The cubic law is $q \propto b^3$.

(a) Compute the ratio of flow rates for apertures of 1 mm and 0.5 mm at the same
gradient.
(b) Compute the ratio of flow rates for apertures of 1 mm and 2 mm.
(c) Explain in one sentence why this makes crustal permeability so variable.
(d) A fracture closes by 20 per cent under a stress change. Compute the change in
flow rate.

---

**★★6.** Run [`../code/viscous_flow_demo.py`](../code/viscous_flow_demo.py).

(a) Report the Reynolds number of the 1 mm fracture and of the 0.1 m borehole at
$U = 0.1\ \mathrm{m\,s^{-1}}$, and the regime printed for each.
(b) Report the cubic-law flow rate, the quadrature flow rate and the relative
error.
(c) Report the equivalent permeability in m² and in units of $10^3$ darcy.
(d) Report the borehole mean velocity and Reynolds number, and explain in two
sentences why the laminar result must not be used.

---

**★★7.** Stokes settling of a quartz sphere of radius 0.25 mm in water.

(a) Compute the settling velocity from $w = 2\Delta\rho\,g a^2/(9\mu)$.
(b) Compute the Reynolds number based on the diameter and state whether the law
is self-consistent.
(c) State what correction is needed and in which direction the true velocity
differs from your answer.
(d) Repeat (a) and (b) for a radius of 0.05 mm and state the conclusion.

---

**★★8.** A single fracture in a rock mass has a visible (mechanical) aperture
of 1.0 mm. A flow test with a pressure gradient of $10^4\ \mathrm{Pa\,m^{-1}}$
measures a flow rate of $2.08\times10^{-4}\ \mathrm{m^2\,s^{-1}}$ per unit
width.

(a) Invert the cubic law to find the hydraulic aperture
$b_h = (12\mu q/G)^{1/3}$.
(b) Compare it with the mechanical aperture and compute the ratio.
(c) Explain physically why the hydraulic aperture is smaller, using the idea of
aperture variability.
(d) State which of the two apertures should be used in a flow model and why.

---

## ★★★ Research-oriented

**★★★9.** Consider flow in a thin film between two nearly parallel surfaces
separated by a gap $h(x)$ that varies slowly in $x$, so that
$\partial h/\partial x \sim h/L \ll 1$.

(a) By scaling $\partial p/\partial x \sim \mu\partial^2u/\partial y^2$, show
that the transverse pressure gradient is smaller than the streamwise one by a
factor of order $(h/L)^2$, and hence that $p = p(x)$ to leading order.
(b) Derive Reynolds' lubrication equation
$\dfrac{\partial}{\partial x}\left(\dfrac{h^3}{12\mu}\dfrac{\partial
p}{\partial x}\right) = 0$ for steady incompressible flow with no-slip walls.
(c) For constant $h$ recover the cubic law and identify the regime of validity
in terms of $h/L$.
(d) State one geophysical situation in which $h/L$ is *not* small, and what goes
wrong there.

---

**★★★10.** In a sand of grain diameter $d = 0.2$ mm and porosity $\phi = 0.2$,
Darcy's law is claimed to hold.

(a) For specific discharges $q = 10^{-5}$, $10^{-4}$, $10^{-3}$ and
$10^{-2}\ \mathrm{m\,s^{-1}}$, compute the pore-scale Reynolds number
$Re_p = \rho q d/\mu$ (this module's convention, equation (10) of lesson 05),
and also report the pore velocity $v = q/\phi$ for reference.
(b) State the specific discharge at which $Re_p = 1$.
(c) Convert that discharge into metres per day and compare it with typical
groundwater velocities of order 0.1–1 m per day.
(d) Explain, with the numbers, why Darcy's law is robust in hydrogeology but
fails near a gravel-packed well or a large karst conduit.
