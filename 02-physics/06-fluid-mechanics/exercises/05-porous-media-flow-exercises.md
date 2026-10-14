# Exercises — 02-06-05 Flow in Porous Media: Darcy's Law and Permeability

Attempt these **closed-book** before opening the
[solutions](./05-porous-media-flow-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/darcy_flow_demo.py`](../code/darcy_flow_demo.py)
require you to run it and report its actual output. Take water as
$\rho = 1000\ \mathrm{kg\,m^{-3}}$, $\mu = 10^{-3}$ Pa s, $g = 9.81\
\mathrm{m\,s^{-2}}$, and use the Darcy-velocity convention
$Re_p = \rho q d/\mu$ throughout (state it if you deviate).

---

## ★ Foundational

**★1.** A sandstone has intrinsic permeability $k = 10^{-13}$ m².

(a) Compute the hydraulic conductivity $K$ for water.
(b) Express it in m per day.
(c) Compute $K$ for an oil of density $800\ \mathrm{kg\,m^{-3}}$ and viscosity
$5\times10^{-3}$ Pa s.
(d) Compute the ratio $K_{\text{water}}/K_{\text{oil}}$ and state whether the
permeability differs between the two cases.

---

**★2.** A porous medium is modelled as a bundle of tubes of radius $10\ \mu$m
with porosity $\phi = 0.2$.

(a) Compute $k = \phi r^2/8$.
(b) Compute $K$ for water.
(c) For a hydraulic gradient of 0.01, compute the specific discharge and the pore
velocity.
(d) State the two ways in which this model is an idealisation of a real rock.

---

**★3.** A fracture has aperture 0.5 mm.

(a) Compute $k = b^2/12$ in m² and in darcy.
(b) Compute $K$ for water.
(c) Compute the specific discharge at unit hydraulic gradient and compare it with
$u_{\text{mean}}$ from the cubic law of lesson 03.
(d) Explain why the agreement in (c) is a consistency check and not a
coincidence.

---

**★4.** A confined aquifer has $K = 10^{-5}\ \mathrm{m\,s^{-1}}$, thickness
$D = 50$ m and porosity 0.25.

(a) Compute the transmissivity $T$.
(b) For a hydraulic gradient of $10^{-3}$, compute the specific discharge, the
total discharge across a 10 km front, and the pore velocity.
(c) Compute the travel time of a particle over 1 km.
(d) State which of these numbers a contaminant's arrival time depends on.

---

## ★★ Applied

**★★5.** A well is pumped in a confined aquifer with $T = 10^{-3}$ m² s⁻¹. Two
observation wells at $r_1 = 0.1$ m (the well radius) and $r_2 = 1000$ m show a
head difference of 10 m.

(a) Compute the discharge $Q$ from the Thiem solution.
(b) Express it in m³ per day.
(c) Compute the head gradient at $r = 1$ m and at $r = 100$ m.
(d) State two reasons the Thiem solution is an approximation rather than a
prediction of a real well.

---

**★★6.** Run [`../code/darcy_flow_demo.py`](../code/darcy_flow_demo.py).

(a) Report the numerical and formula permeabilities of the tube bundle and their
relative difference.
(b) Report $K$ in m per day for silty sand and for a 1 mm open fracture, and the
ratio.
(c) Report the Thiem discharge and the relative difference from the numerical
radial integration.
(d) Report $Re_p$ for the sand aquifer, the gravel aquifer and the 1 mm fracture
at $q = 10^{-2}$ m s⁻¹, and state which are inside the Darcy range.

---

**★★7.** A rock has $k = 10^{-15}$ m² and specific storage
$S_s = 10^{-5}\ \mathrm{m^{-1}}$.

(a) Compute the hydraulic diffusivity $\kappa_h$.
(b) Compute the diffusion length $\sqrt{\kappa_h t}$ for $t = 1$ day, 1 year and
100 years.
(c) Compute how long a pressure front takes to travel 1 km.
(d) Repeat (a)–(c) for $k = 10^{-14}$ m² and state the ratio of the two 1 km
times.

---

**★★8.** Darcy's law is claimed valid while $Re_p \lesssim 1$–$10$, with
$Re_p = \rho q d/\mu$.

(a) Compute the specific discharge at $Re_p = 1$ for $d = 0.2$ mm (sand),
$d = 10$ mm (gravel) and $d = 0.5$ m (a karst conduit).
(b) Express each in metres per day.
(c) Compare with typical groundwater specific discharges of
$10^{-6}$–$10^{-5}$ m s⁻¹, and state the conclusion for each medium.
(d) Explain why the *grain* scale, and not the aquifer thickness, is the correct
length in $Re_p$.

---

## ★★★ Research-oriented

**★★★9.** Derive the pore-pressure diffusion equation.

(a) Start from Darcy's law and conservation of mass for a fluid of density $\rho$
in a deforming porous medium:
$\partial(\phi\rho)/\partial t + \nabla\cdot(\rho\mathbf{q}) = 0$.
(b) Linearise with $\mathrm{d}\rho/\rho = c_f\,\mathrm{d}p$ and
$\mathrm{d}\phi/\phi = c_m\,\mathrm{d}p$, take the head-gradient form of Darcy's
law ($\mathbf{q} = -K\nabla h$ with $h = p/(\rho g)$ for a constant-density
fluid), and show that the pressure obeys
$\partial p/\partial t = \kappa_h\nabla^2 p$. State clearly the approximation you
make about the relative size of $\nabla p$ and $\rho\mathbf{g}$.
(c) Identify $S_s = \rho g(\phi c_f + c_m)$ and show
$\kappa_h = k\rho g/(\mu S_s)$.
(d) State the physical meaning of $c_f$ and $c_m$, and which dominates in a stiff
rock and in a soft soil.

---

**★★★10.** A wastewater injection well raises the pore pressure by $\Delta p = 1$
MPa at a fault 300 m away.

(a) Taking a friction coefficient $\mu_f = 0.6$ and assuming the shear traction
on the fault is unchanged, compute the Coulomb failure-function change per unit
pore-pressure change, and evaluate it.
(b) Compare it with a typical earthquake stress drop of order 1–10 MPa and state
whether the change is significant.
(c) Using $k = 10^{-15}$ m² and $S_s = 10^{-5}$ m⁻¹, compute the time for the
pressure front to reach 300 m, and repeat for $k = 10^{-14}$ m².
(d) Explain, using (c), why the distance over which injection can trigger
seismicity is inherently a range, and name the two quantities that control it.
