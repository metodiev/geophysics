# Solutions — 02-06-01 Fluid Statics, Pressure and Buoyancy

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. All densities are the nominal values stated in
> the exercise, not measurements of a particular rock or water mass.

---

## ★1 — Hydrostatic gradient in the crust

**(a)** $\rho g = 2650\times9.81 = 2.5997\times10^4\ \mathrm{Pa\,m^{-1}} =
0.0260\ \mathrm{MPa\,m^{-1}} = 26.00\ \mathrm{MPa\,km^{-1}}$.

**(b)**

| Depth (km) | $p$ (MPa) |
|---|---|
| 1 | 26.00 |
| 5 | 129.98 |
| 10 | 259.97 |
| 20 | 519.93 |
| 30 | 779.90 |

**(c)** $h = p/(\rho_w g) = 2.5997\times10^8/(1000\times9.81) = 2.65\times10^4$
m, i.e. **26.5 km of fresh water**. The head is larger than the depth because
water is less dense than rock.

**(d)** The assumption is that the pore fluid is connected to the surface and
that its pressure is the hydrostatic pressure of a continuous column. That is
the *hydrostatic* pore-pressure case. It fails where a layer is sealed, and the
resulting *overpressure* is the subject of
[05 Flow in Porous Media](../05-porous-media-flow.md) and of induced
seismicity ([06-seismology/12](../../../06-seismology/12-induced-and-triggered-seismicity/README.md)).

---

## ★2 — Ocean pressure

**(a)** $p = \rho_w g z$ with $\rho_w = 1025\ \mathrm{kg\,m^{-3}}$:

| Depth | $p$ (MPa) |
|---|---|
| 100 m | 1.006 |
| 1 km | 10.055 |
| 4 km | 40.221 |
| 11 km | 110.608 |

The demo reports 40.417 MPa at 4 km for $\rho_w = 1030$; the difference is
entirely the density choice, which is the point of part (c).

**(b)** $z = 10^8/(1025\times9.81) = 9.945$ km.

**(c)** 100 m of seawater gives $1.0055$ MPa, so the rule of thumb errs **high by
0.55 per cent**; for fresh water it gives $0.981$ MPa, erring **low by 1.9 per
cent**. The rule is a serviceable mental estimate and a bad calculation.

**(d)** The pressure at a given depth depends on the local density and the local
$g$. $g$ varies with latitude by about 0.5 per cent, so the rule's accuracy is
no better than that in any case; but the reason the *percentage error* is
latitude-independent is that the rule is a statement about $\rho g$ per unit
depth, and the error is $(\rho g/10^4 - 1)$, which contains no latitude.

---

## ★3 — Buoyancy

**(a)** Submerged fraction $= \rho_{\text{ice}}/\rho_w = 917/1030 =
0.8903$. About 89 per cent below the waterline; the familiar "nine-tenths" is
right to a per cent.

**(b)** $(\rho_{\text{crust}}-\rho_{\text{magma}})g = (2700-2500)\times9.81 =
1962\ \mathrm{N\,m^{-3}}$, directed **upwards**. This is a force per unit volume;
multiply by the volume to get a force.

**(c)** $1962\ \mathrm{Pa\,m^{-1}}\times2000\ \mathrm{m} = 3.924$ MPa.

**(d)** Because floating is a *balance*, not a force: $m_{\text{body}}g =
m_{\text{displaced}}g$ and $g$ cancels from both sides. The submerged fraction
is a density ratio, hence dimensionless and independent of $g$. This is also why
the same argument works on another planet.

---

## ★4 — Airy isostasy

**(a)** $r = \dfrac{\rho_c}{\rho_m-\rho_c}h =
\dfrac{2750}{3300-2750}\times2\ \mathrm{km} = 5.0\times2 = \mathbf{10\ km}$.

**(b)** Amplification $r/h = 5.0$.

**(c)** At 60 km under the plateau: crust from 0 to 60 km is 2 km of topography
plus 28 km of "normal" crust plus the 30 km root:
$p = 2750\times9.81\times2\times10^3 + 2750\times9.81\times28\times10^3 +
3300\times9.81\times30\times10^3 = 53.96 + 755.37 + 971.19 = 1780.5$ MPa.
Under the reference column: 30 km of crust plus 30 km of mantle gives
$2750\times9.81\times30\times10^3 + 3300\times9.81\times30\times10^3 = 809.3 +
971.2 = 1780.5$ MPa. The two agree exactly — as they must, because the root
thickness was *derived* from that equality. The residual tests arithmetic, not
physics.

**(d)** (i) That the load is supported entirely by buoyancy, i.e. that the
lithosphere has no elastic strength (valid for loads broad compared with the
flexural wavelength); (ii) that the compensation is local and at a single depth,
i.e. that the density structure is known. Real compensation is partial, and
flexure supports part of a narrow load. Both assumptions are the subject of
[02-04 Elasticity](../../04-elasticity-and-continuum-mechanics/README.md) and
[07-gravity-geodesy](../../../07-gravity-geodesy/README.md).

---

## ★★5 — Layered pressure profile

**(a)** Integrating layer by layer:

| Layer | Top (km) | Base (km) | $\rho$ | $p_{\text{top}}$ (MPa) | $p_{\text{base}}$ (MPa) |
|---|---|---|---|---|---|
| sediment | 0 | 2 | 2200 | 0.000 | 43.164 |
| upper crust | 2 | 15 | 2650 | 43.164 | 381.119 |
| lower crust | 15 | 35 | 2900 | 381.119 | 950.099 |

**(b)** Single density $2700$: $p = 2700\times9.81\times35\times10^3 =
927.045$ MPa.

**(c)** Column-average density $\bar\rho = (2200\times2 + 2650\times13 +
2900\times20)/35 = 2767.14\ \mathrm{kg\,m^{-3}}$, giving $p = 2767.14\times9.81
\times35\times10^3 = 950.099$ MPa, identical to (a). A single-density model is
therefore *exact* provided the density used is the column average — which is the
reason the error in (b) is a statement about the choice of 2700, not about the
physics.

**(a)/(b)/(c) all agree with the demo output to the digits shown.**

**(d)** (a) is the computed profile; (b) is a model whose error is 2.49 per cent
at 35 km. The measurement that resolves the ambiguity is a density log or a
gravity survey; neither is contained in the hydrostatic assumption.

---

## ★★6 — Reading the demo

**(a)** Worst finite-difference residual over **695 interior samples**:
$2.183\times10^{-8}\ \mathrm{Pa\,m^{-1}}$. That is round-off at the sampling
step, and it confirms that the discrete integration and the discrete
differentiation are consistent.

**(b)** Layered $p(35\ \mathrm{km}) = 950.098$ MPa; single density
$2700\ \mathrm{kg\,m^{-3}}$ gives $927.045$ MPa; relative difference
$+2.49$ per cent. Every digit of the layered answer is produced by the
integration in part (a); nothing new was assumed.

**(c)** For $h = 5$ km at $D = 30$ km, $\rho = \rho_0 D/(D+h) = 2700\times30/35
= 2314.3\ \mathrm{kg\,m^{-3}}$, a deficit of **385.7 kg m⁻³**. That is a large
anomaly: compensating a plateau by density requires a much stronger lateral
variation than compensating it by a root.

**(d)** The dense block gives $(2700-3000)\times9.81 = -2943\
\mathrm{N\,m^{-3}}$: negative, i.e. a net downward force. The sign is produced
automatically by the density *difference*; adding a minus sign "because it
sinks" would double-count it.

---

## ★★7 — Magma ascent

**(a)** $(2700-2500)\times9.81\times5000 = \mathbf{9.81\ MPa}$.

**(b)** Yes: 9.81 MPa exceeds 5 MPa. So a 5 km column of this magma can, on
buoyancy alone, exceed the tensile strength of the host rock — which is
precisely why dykes propagate as tensile fractures. Note how sensitive the
conclusion is to the assumed densities: at a contrast of $100\
\mathrm{kg\,m^{-3}}$ the pressure is halved.

**(c)** With $\Delta p = 9.81$ MPa, $a = 1$ m, $\mu = 100$ Pa s, $L = 5000$ m:

$$Q = \frac{\pi\Delta p\,a^4}{8\mu L} = \frac{\pi\times9.81\times10^6\times1}
{8\times100\times5000} = 7.70\ \mathrm{m^3\,s^{-1}},$$

and the mean velocity is $Q/(\pi a^2) = 2.45\ \mathrm{m\,s^{-1}}$.

**(d)** It is an over-estimate because: (i) as the dyke opens, the driving
overpressure is spent partly on elastic deformation of the walls, not on flow;
(ii) magma cools and crystallises, raising the effective viscosity and finally
arresting the flow; (iii) a dyke is a narrow slot, not a circular pipe, and its
walls are not smooth; (iv) the conduit is not full of a single-phase liquid —
volatiles exsolve and the flow becomes two-phase. Observed dyke propagation
rates are far below the laminar-pipe estimate, which is why every dyke-propagation
model solves a coupled elasticity–flow problem rather than Poiseuille's law
alone.

---

## ★★8 — Isostasy is non-unique

**(a)** $r = 2750\times1000/(3300-2750) = 5000$ m = **5 km**.

**(b)** $\rho = \rho_0 D/(D+h) = 2750\times40/41 = 2682.9\
\mathrm{kg\,m^{-3}}$, a deficit of **67.1 kg m⁻³**.

**(c)** Airy at 60 km: crust 1 km (the topography) plus 29 km of normal crust
plus the 34 km root above 60 km, then 25 km of mantle:
$2750g(1+29)\times10^3 + 3300g\times34\times10^3$
$= 2750\times9.81\times30\times10^3 + 3300\times9.81\times34\times10^3
= 809.3 + 1100.7 = 1910.0$ MPa.
Pratt at 60 km: 40 km of reduced-density crust (2682.9), then 20 km of mantle:
$2682.9\times9.81\times40\times10^3 + 3300\times9.81\times20\times10^3 =
1052.8 + 647.5 = 1700.3$ MPa.
These are **not** equal, which is the real lesson: the two models are
constructed to give equal pressure at their own compensation depth, and the
pressures differ away from it. Interpreting gravity therefore requires choosing
a compensation depth as well as a model.

**(d)** One independent discriminator is **seismology**: a crustal root shows a
deepened Moho, which is measured by receiver functions or wide-angle refraction,
whereas a Pratt anomaly has a flat Moho. A second is the **geoid**, whose
wavelength dependence distinguishes root from density compensation. This is the
central theme of [07-gravity-geodesy](../../../07-gravity-geodesy/README.md).

---

## ★★★9 — Central pressure of a uniform sphere

**(a)** By Newton's shell theorem the mass outside radius $r$ exerts no net
force at $r$, so only $M(r) = \tfrac43\pi r^3\rho$ matters:

$$g(r) = \frac{GM(r)}{r^2} = \frac{4}{3}\pi G\rho\,r .$$

**(b)** Hydrostatic balance $\mathrm{d}p/\mathrm{d}r = -\rho g(r)$ gives

$$p(r) = \int_r^R \rho g(r')\,\mathrm{d}r' = \frac{4}{3}\pi G\rho^2
\int_r^R r'\,\mathrm{d}r' = \frac{2}{3}\pi G\rho^2(R^2-r^2).$$

**(c)** $p(0) = \tfrac23\pi\times6.674\,30\times10^{-11}\times(5514)^2
\times(6.371\times10^6)^2 = 1.725\times10^{11}$ Pa $= \mathbf{172.5\ GPa}$
using the handbook's nominal mean density and mean radius.

**(d)** The real Earth's central pressure is larger because the density is not
uniform: it increases with depth under self-compression, so the material near
the centre is heavier and the weight of the overlying column is larger than the
uniform case. The preliminary reference Earth model gives about 364 GPa
(Dziewonski & Anderson, 1981), a factor of about 2.1 above the constant-density
estimate. That factor is a measure of how much the Earth is compressed by its
own gravity — which is exactly the physics of
[02-11 Physics of the Earth's Interior](../../11-physics-of-earths-interior-and-atmosphere/README.md).

---

## ★★★10 — Aquifer pressures and tension

**(a)** Depth below the water table is $100-50 = 50$ m and $200-50 = 150$ m.

$$p(100) = 1000\times9.81\times50 = 0.4905\ \mathrm{MPa}, \qquad
p(200) = 1000\times9.81\times150 = 1.4715\ \mathrm{MPa}.$$

**(b)** 9 per cent lower is $p = 0.91\times1.4715 = 1.339$ MPa. The pressure head
is $p/(\rho g) = 136.5$ m, so the hydraulic head relative to ground level is
$-200+136.5 = -63.5$ m, against $-50$ m at the water table. The head falls by
13.5 m over 150 m of descent: the flow is **downwards**, i.e. the site is a
recharge area, or the piezometer is screened in a layer of lower head than the
overlying one (a downward-hydraulic-gradient situation). Either way, the
departure from hydrostatic is the *signal*, and it is what a water-balance study
actually uses.

**(c)** Water cavitates when its absolute pressure falls to the vapour pressure.
With $p_{\text{vap}} = 2.3$ kPa at 20 °C and $p_{\text{atm}} = 101.3$ kPa,

$$p_{\text{gauge,min}} = p_{\text{vap}} - p_{\text{atm}} = 2.3\times10^3 -
1.013\times10^5 = -9.9\times10^4\ \mathrm{Pa} \approx -99\ \mathrm{kPa}.$$

That is about $-10$ m of water head. Below this the water cannot remain a
continuous liquid: a vapour cavity opens, the liquid separates from the
measuring point, and the pressure the instrument reads is no longer the pressure
of the fluid. This is why suction measurements in the vadose zone are made with
tensiometers whose range is limited to roughly one atmosphere, and why
section-05 pore-pressure arguments never invoke unbounded tension.

**(d)** Hydrostatic is the default because it is what a connected column of
static fluid does, with no free parameters, and because recharge and discharge
over most of an aquifer are slow enough that the acceleration term is negligible
(lesson 02 quantifies this). A measured departure is interpreted as a *vertical
gradient of head*, hence as vertical flow, and the magnitude of the departure is
what a groundwater-flow model is calibrated against — see
[14-hydrology-hydrogeophysics](../../../14-hydrology-hydrogeophysics/README.md).
