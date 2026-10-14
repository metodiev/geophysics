# Solutions — 04-06-04 Aquifer Types and Groundwater Occurrence

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values computed here are labelled as such.

Note which quantity is which type of property: $K$ is **rock plus fluid**,
$S_s$ and $S_y$ are **rock plus fluid** (storage), and the specific capacity is a
property of the **well and the aquifer together**.

---

## ★1 — Darcy's law and transmissivity

**(a)** $Q = K\,i\,A = (2\times10^{-4})(5\times10^{-4})(500) =
5.0\times10^{-5}$ m³ s⁻¹.

**(b)** $5.0\times10^{-5} \times 86400 = 4.32$ m³ day⁻¹.

**(c)** $T = Kb = (2\times10^{-4})(20) = 4.0\times10^{-3}$ m² s⁻¹
$= 345.6$ m² day⁻¹.

**(d)** Yes. $K = k\rho_w g/\mu$, and $\mu$ falls by a factor of about two between
10 °C and 25 °C, so a warmer aquifer conducts more water through the same rock.
Hydraulic conductivity is therefore temperature dependent, which is why a cold
aquifer and a hot one of identical rock behave differently.

---

## ★2 — Storage regimes

**(a)** $S = S_s b = (2\times10^{-6})(40) = 8.0\times10^{-5}$.

**(b)** $S_y/S = 0.20/8.0\times10^{-5} = 2500$.

**(c)** Confined: $8.0\times10^{-5} \times 10^{6}\ \text{m}^2 \times 1\ \text{m}
= 80$ m³. Unconfined: $0.20 \times 10^{6} \times 1 = 2\times10^{5}$ m³.

**(d)** The **confined** aquifer shows the much larger head decline for the same
volume of water removed, because $S$ is three orders of magnitude smaller: one
metre of head change releases only 80 m³ from a square kilometre, against
$2\times10^{5}$ m³ in the unconfined case. That is why a confined aquifer can be
pumped hard with a dramatic fall in water level while very little water is
actually being removed from storage — the two are decoupled, and the drawdown is
not a measure of the resource.

---

## ★3 — Archie's law

**(a)** $F = a/\phi^{m} = 1/0.25^{2} = 16$.

**(b)** $\rho_0 = F\rho_w = 16 \times 8 = 128$ Ω m.

**(c)** $\rho_t = \rho_0/S_w^{n} = 128/0.25 = 512$ Ω m.

**(d)** The **saturation exponent $n$ and the cementation exponent $m$** are the
weak points, but the most often violated assumption is the **clay-free condition**:
a shaly sand contains conductive clay that lowers the resistivity independently of
the water, and applying a clean-sand Archie relation to it overestimates the water
saturation systematically. The second most common is the assumption that the rock
is fully water-wet and that the water resistivity is known.

---

## ★★4 — Theis drawdown

**(a)** $u = \dfrac{r^{2}S}{4Tt} = \dfrac{(150)^{2}(2\times10^{-4})}
{4(0.02)(2 \times 86400)} = 3.255\times10^{-4}$.

**(b)** $W(u) = E_1(3.255\times10^{-4}) = 7.4532$.

**(c)** $s = \dfrac{Q}{4\pi T}W = \dfrac{0.06}{4\pi(0.02)}(7.4532)
= 0.23874(7.4532) = 1.779$ m.

**(d)** At 20 days, $u = 3.255\times10^{-5}$ and $W = 9.7555$, so
$s = 2.329$ m; the ratio is $1.309$. A **tenfold** increase in pumping time
increases the drawdown by 31 per cent, because the growth is logarithmic.

---

## ★★5 — Recharge from water-table fluctuation

**(a)** $R = 0.12 \times 1.2/1 = 0.144$ m yr⁻¹ $= 144$ mm yr⁻¹.

**(b)** $S_y = 0.06$: 72 mm yr⁻¹. $S_y = 0.24$: 288 mm yr⁻¹.

**(c)** Because $R \propto S_y$ exactly, and $S_y$ is estimated from grain size or
from a pumping test with an uncertainty of a factor of two or worse. The method
converts a well-measured head change into a poorly constrained water volume, so it
is a consistency check on a water balance rather than an independent measurement.

**(d)** The method fails where (i) the water table is pumped or drained by a river
during the rise, so the rise is not the recharge signal; and (ii) the aquifer is
confined, or the water table is shallow enough that evapotranspiration or surface
sealing removes part of the recharge before it reaches the table.

---

## ★★6 — CRIM and the water-table reflector

**(a)** $\sqrt{\varepsilon} = 0.25\sqrt{81} + 0.75\sqrt{5}
= 2.25 + 1.6771 = 3.9271$, so $\varepsilon = 15.42$.

**(b)** $v = c/\sqrt{\varepsilon} = 2.99792458\times10^{8}/3.9271
= 7.634\times10^{7}$ m s⁻¹ $= 0.0763$ m/ns.

**(c)** At $\theta = 0.05$:
$\sqrt{\varepsilon} = 0.05(9) + 0.75(2.23607) + 0.20(1)
= 0.45 + 1.67705 + 0.20 = 2.32705$, so $\varepsilon = 5.415$ and
$v = 1.288\times10^{8}$ m s⁻¹ $= 0.1288$ m/ns.

**(d)** $R = (2.32705 - 3.9271)/(2.32705 + 3.9271) = -0.2558$. The water table is a
strong reflector because the *contrast in $\sqrt{\varepsilon}$* is large: water has
$\varepsilon_r \approx 81$ against 1 for air, so adding even a few per cent of water
by volume changes the radar velocity substantially. Note that $R$ is negative, and
that the absolute reflection is about 26 per cent of amplitude — comparable with a
strong lithological boundary.

---

## ★★★7 — Reading the demonstration

Quoted output from `groundwater_aquifers_demo.py`:

**(a)** $K = 10^{-5}$, $b = 10$: 1.73 m³ day⁻¹, $T = 8.6$ m² day⁻¹.
$K = 10^{-4}$, $b = 20$: 17.28, 172.8. $K = 10^{-3}$, $b = 5$: 172.80, 432.0.
$K = 10^{-2}$, $b = 30$: 1728.00, 25 920.0.

**(b)** $S_s = 1.8443\times10^{-6}$ m⁻¹; storativities
$1.8443\times10^{-5}$ (10 m), $9.2214\times10^{-5}$ (50 m),
$3.6886\times10^{-4}$ (200 m); $S_y/S = 1627$ for the 50 m case.

**(c)** Specific capacity at 0.15 m radius after 1 day: $T = 0.005$ m² s⁻¹,
$S = 10^{-4}$: $s = 15.822$ m, 273.0 m³ day⁻¹ per metre. $T = 0.010$:
$s = 8.187$ m, 527.7. $T = 0.050$: $s = 1.765$ m, 2447.0. $T = 0.010$,
$S = 10^{-3}$: $s = 7.270$ m, 594.2.

**(d)** $E_1(1) = 0.2193839344$, matching the reference to ten figures.
Drawdown at 50, 100 and 500 m: 2.648, 2.097, 0.844 m at 0.1 d; 3.564, 3.012,
1.734 at 1 d; 4.480, 3.928, 2.648 at 10 d; 5.396, 4.845, 3.564 at 100 d;
6.312, 5.761, 4.480 m at 1000 d.

**(e)** $R = 0.1 \times 0.8 = 80.0$ mm yr⁻¹; 40.0 mm yr⁻¹ at $S_y = 0.05$ and
160.0 mm yr⁻¹ at $S_y = 0.20$.

**(f)** Formation factor and saturated resistivity: 6.25/62.5 (0.40), 11.11/111.1
(0.30), 25.00/250.0 (0.20), 100.00/1000.0 (0.10), 400.00/4000.0 (0.05) Ω m.
Partial saturation at $\phi = 0.30$: 111.11, 173.61, 444.44, 1234.57 Ω m at
$S_w = 1.0$, 0.8, 0.5, 0.3.

**(g)** CRIM with $\phi = 0.30$: $\varepsilon = 18.19$, $v = 0.0703$ m/ns and
111.1 Ω m at $S_w = 1.0$; 14.33, 0.0792, 173.6 at 0.8; 9.40, 0.0978, 444.4 at
0.5; 5.50, 0.1278, 2777.8 at 0.2. Reflection coefficient between
$S_w = 0.2$ and $S_w = 1.0$: $R = -0.2904$.

**(h)** The Darcy flow, the storativities, the Theis drawdown, the CRIM
permittivity, the radar velocity and the reflection coefficient are **derived from
physical relations**. Archie's formation factor and the partial-saturation
relation are **empirical fits** whose exponents are lithology dependent. The
specific yield, the porosity, the densities and the end-member permittivities are
**model inputs and nominal ranges**, and the radius-of-influence convention and the
Rouse-like threshold bands elsewhere in this module are **conventions** rather
than physics.

---

## ★★★8 — Interpretation and its limits

**(a)** A 200 Ω m unit at 30 m depth could be:

1. **A clean, saturated sand aquifer.** Discriminating measurement: a borehole
   with a gamma and a resistivity log, which gives the clay content and the
   porosity, or a pumping test for the yield.
2. **A dry or unsaturated sand.** Discriminating measurement: GPR, whose velocity
   is controlled by water content and not by salinity — a dry sand and a freshwater
   sand have similar resistivities but very different permittivities.
3. **A resistive bedrock (granite, or a cemented horizon).** Discriminating
   measurement: seismic refraction or surface-wave analysis, which measure the
   velocity and stiffness and separate a loose sediment from a rock.

**(b)** The exploration problem differs because the *geometry of the permeability*
differs even when the bulk transmissivity does not. In the alluvial sand, the
permeability is distributed through the whole volume, so a survey that maps the
sand body maps the aquifer; the property carrying the signal is resistivity (and
permittivity). In the fractured granite, the permeability is concentrated in a
network of apertures occupying a fraction of a per cent of the volume, so the
aquifer is a *structure* and not a body; the signal carriers are the **fracture
orientation** (through azimuthal resistivity or seismic anisotropy) and the
**weathering profile**, and the drilling target is an intersection rather than a
layer.

**(c)** The anomaly is nearly independent of rock type because the conductivity
contrast is in the **pore fluid**: seawater has a conductivity of order
$3$ S m⁻¹ against $0.03$–$0.1$ S m⁻¹ for fresh water, so the bulk resistivity of
*any* saturated sediment changes by two orders of magnitude when its pore fluid
changes from fresh to saline. The property actually measured is the bulk
**electrical conductivity** of the saturated formation, which is dominated by the
pore-fluid conductivity and only modulated by porosity through the formation
factor.

**(d)** Three reasons a 100 mm yr⁻¹ discrepancy could arise:

1. **$S_y$ is wrong.** If the true specific yield is 0.08 rather than 0.12, the
   fluctuation method gives 100 rather than 144 mm yr⁻¹ and the gap closes.
2. **The catchment balance assumes no change in storage.** The balance term
   $\Delta S$ is usually the residual, so an unmeasured change in groundwater
   storage — or in soil moisture — appears as an error in recharge.
3. **A component of the balance is mis-attributed.** Inter-catchment groundwater
   flow, or a surface-water outflow that is not gauged, changes the balance without
   changing the recharge.

The one that is testable with geophysics is (2): **time-lapse gravity or
time-lapse ERT** measures the change in stored water directly, which converts the
storage term from an assumption into a measurement.
