# Exercises — 02-06-01 Fluid Statics, Pressure and Buoyancy

Attempt these **closed-book** before opening the
[solutions](./01-fluid-statics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to [`../code/fluid_statics_demo.py`](../code/fluid_statics_demo.py)
require you to run it and report its actual output. Use $g = 9.81\
\mathrm{m\,s^{-2}}$ and state the density you assume.

---

## ★ Foundational

**★1.** A crustal column has uniform density $\rho = 2650\ \mathrm{kg\,m^{-3}}$.

(a) Compute the pressure gradient in MPa km⁻¹.
(b) Compute the pressure at 1, 5, 10, 20 and 30 km depth, ignoring the
atmospheric term.
(c) Express the pressure at 10 km as a head of water of density
$1000\ \mathrm{kg\,m^{-3}}$.
(d) State what assumption is being made about pore pressure if these are taken
to be the pressures *inside* a saturated rock.

---

**★2.** Seawater has $\rho_w = 1025\ \mathrm{kg\,m^{-3}}$.

(a) Compute the hydrostatic pressure at 100 m, 1 km, 4 km and 11 km.
(b) Compute the depth at which the pressure is exactly 100 MPa.
(c) The rule of thumb "1 MPa per 100 m" — by what percentage does it err for
seawater, and for fresh water?
(d) Why does the answer to (c) not depend on latitude?

---

**★3.** An iceberg of density $917\ \mathrm{kg\,m^{-3}}$ floats in seawater of
density $1030\ \mathrm{kg\,m^{-3}}$.

(a) Compute the submerged fraction.
(b) A basalt magma of density $2500\ \mathrm{kg\,m^{-3}}$ sits in crust of
density $2700\ \mathrm{kg\,m^{-3}}$. Compute the net buoyancy force per unit
volume and state its direction.
(c) Compute the buoyancy pressure produced by a 2 km column of that magma.
(d) Explain in one sentence why the answer to (a) does not depend on $g$.

---

**★4.** Airy isostasy with $\rho_c = 2750$ and $\rho_m = 3300\
\mathrm{kg\,m^{-3}}$.

(a) Compute the root thickness needed to support a 2 km plateau.
(b) Compute the amplification factor $r/h$.
(c) Verify by hand that the pressure at 60 km depth under the plateau equals the
pressure at 60 km under the reference column.
(d) State the two assumptions that make this a *model* rather than a law.

---

## ★★ Applied

**★★5.** A three-layer crust is: sediment $0$–$2$ km, $\rho = 2200$; upper crust
$2$–$15$ km, $\rho = 2650$; lower crust $15$–$35$ km, $\rho = 2900\
\mathrm{kg\,m^{-3}}$.

(a) Compute the pressure at the base of each layer.
(b) Compute the pressure at 35 km using a single density of
$2700\ \mathrm{kg\,m^{-3}}$ and compare.
(c) Compute the pressure at 35 km using the *average* density of the column and
show that it agrees with (a).
(d) State which of (a) and (b) is the model and which is the measurement-driven
answer.

---

**★★6.** Run [`../code/fluid_statics_demo.py`](../code/fluid_statics_demo.py).

(a) Report the worst finite-difference residual in section 1 and the number of
interior samples used.
(b) Report the layered and single-density pressures at 35 km and their relative
difference.
(c) Report the density required by the Pratt model for a 5 km plateau at
compensation depth 30 km, and the density deficit.
(d) Report the net force per unit volume for the dense block in section 2 and
explain the sign.

---

**★★7.** A magma of density $2500\ \mathrm{kg\,m^{-3}}$ fills a vertical
conduit to 5 km depth in crust of density $2700\ \mathrm{kg\,m^{-3}}$.

(a) Compute the buoyancy pressure at the base of the column.
(b) The host rock has a tensile strength of 5 MPa. Does the buoyancy pressure
exceed it?
(c) The conduit has radius 1 m and the magma viscosity is $100\
\mathrm{Pa\,s}$. Using the Poiseuille result $Q = \pi \Delta p\,a^4/(8\mu L)$
from lesson 03, estimate the volume flux driven by the full buoyancy pressure
over the 5 km length, and the mean velocity.
(d) Explain why your answer to (c) is an over-estimate of the actual ascent
rate, naming at least two effects neglected.

---

**★★8.** Consider a 1 km plateau on crust of density $2750\
\mathrm{kg\,m^{-3}}$ over mantle of density $3300\ \mathrm{kg\,m^{-3}}$.

(a) Compute the Airy root.
(b) Compute the Pratt density needed at compensation depth $D = 40$ km, and the
density deficit.
(c) Show that *both* models predict the same pressure at 60 km depth, and hence
that surface gravity alone cannot distinguish them.
(d) Name one independent observation that does distinguish them and say what it
measures.

---

## ★★★ Research-oriented

**★★★9.** Consider a self-gravitating sphere of uniform density $\rho$ and
radius $R$. Newton's theorem gives the enclosed mass at radius $r$ as
$M(r) = \tfrac43\pi r^3\rho$.

(a) Show that the gravitational acceleration inside is $g(r) = \tfrac43\pi G\rho
r$, directed inwards.
(b) Integrate $\partial p/\partial r = -\rho g(r)$ from $p(R) = 0$ to obtain
$p(r) = \tfrac23\pi G\rho^2 (R^2-r^2)$.
(c) Evaluate the central pressure for $\rho = 5514\ \mathrm{kg\,m^{-3}}$ and
$R = 6371$ km, using $G = 6.674\,30\times10^{-11}\
\mathrm{m^3\,kg^{-1}\,s^{-2}}$ (CODATA, as distributed by NIST; handbook Sec. 2).
(d) The real Earth's central pressure is larger, about 364 GPa from the
Preliminary Reference Earth Model (Dziewonski & Anderson, 1981; cited in the
handbook, Sec. 6). Explain why the constant-density model underestimates it,
using no equations.

---

**★★★10.** An unconfined aquifer is a permeable layer whose top is the water
table. A piezometer at a site measures the water table at 50 m below ground
level.

(a) Assuming hydrostatic conditions with fresh water, compute the pressure at
100 m and at 200 m below ground level.
(b) The measured pressure at 200 m is 9 per cent *lower* than your answer to
(a). Compute the implied pressure head and describe what physical situation
produces it.
(c) Water cannot sustain more than about one atmosphere of tension before it
cavitates. Taking the vapour pressure of water at 20 °C as 2.3 kPa (nominal),
compute the lowest absolute pressure the water at 200 m can reach and express it
as a gauge pressure. State why the fluid cavitates below it.
(d) Explain why the hydrostatic assumption is the appropriate default and how a
measured departure from it is interpreted in
[14-hydrology-hydrogeophysics](../../../14-hydrology-hydrogeophysics/README.md).
