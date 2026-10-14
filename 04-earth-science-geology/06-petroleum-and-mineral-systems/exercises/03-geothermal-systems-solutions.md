# Solutions — 04-06-03 Geothermal Systems, Heat Flow and Resource Assessment

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values computed here are labelled as such.

The **heat in place** is computed. Recovery factors and capacities are stated
symbolically only, and are never given a numerical value.

---

## ★1 — Heat flow and geotherm

**(a)** $q = k\,\mathrm{d}T/\mathrm{d}z = 3.0 \times 35\times10^{-3}
= 0.105$ W m⁻² $= 105$ mW m⁻².

**(b)** $T(2000) = 10 + 35\times10^{-3}(2000) = 80\ ^\circ$C.

**(c)** $q = 2.0 \times 35\times10^{-3} = 70$ mW m⁻². The **gradient** is the
better controlled input, because a temperature log measures it over hundreds of
metres; the **conductivity** is usually determined from a limited set of cores or
from a log with sparse core calibration, and it varies with lithology and
saturation.

**(d)** Because the heat flow is not measured anywhere: it is the *product* of a
measured gradient and a measured (or inferred) conductivity, each with its own
spatial variability, so the map inherits the errors of both and they do not
cancel.

---

## ★2 — A geotherm with a source term

**(a)** $T = 10 + \dfrac{(60\times10^{-3})(4000)}{2.5} = 10 + 96 = 106.0\ ^\circ$C.

**(b)** Add $\dfrac{A z^{2}}{2k} = \dfrac{(3\times10^{-6})(1.6\times10^{7})}{5.0}
= 9.6$ K, giving 115.6 °C.

**(c)** 9.6 K, which is 8.3 per cent of the 116 °C above the surface — and it is
much larger than the uncertainty of a careful temperature measurement.

**(d)** The source term is quadratic in depth while the conductive term is linear,
so at 1 km it contributes $0.64$ K and at 4 km it contributes $9.6$ K: a factor of
15 for a factor of four in depth. Negligible near the surface, first-order at the
base of a heat-flow section.

---

## ★3 — Skin depth

**(a)** $\delta = 503\sqrt{\rho T} = 503\sqrt{20 \times 10} = 503(14.14) =
7113$ m.

**(b)** At 100 s: $\delta = 503\sqrt{2000} = 503(44.72) = 22\,494$ m.

**(c)** $5\times10^{3} = 503\sqrt{\rho T}$ gives
$\rho T = (5000/503)^{2} = 98.8$ Ω m s, so e.g. 1 Ω m at 98.8 s.

**(d)** The method measures **electrical conductivity** as a function of depth
(equivalently, the depth to conductivity contrasts). It does **not** measure
temperature: a conductive zone may be a clay cap caused by past alteration rather
than a hot reservoir, and a resistive zone may be dry rather than hot.

---

## ★★4 — Rayleigh number and regime

**(a)** With $k_\mathrm{perm} = 10^{-13}$ m², $H = 1500$ m, $\Delta T = 120$ K:

$$\mathrm{Ra} = \frac{(10^{-13})(10^{6})(4186)(9.81)(5\times10^{-4})(120)(1500)}
{(2.5\times10^{-4})(2.0)} = 739.2 .$$

**(b)** $\mathrm{Ra}_c = 4\pi^{2} = 39.48$, so
$\mathrm{Ra}/\mathrm{Ra}_c = 18.7$: the layer is **well above critical** and
convection is expected.

**(c)** Since $\mathrm{Ra} \propto H$ at fixed $\Delta T$, the critical thickness is
$1500/18.72 = 80.1$ m.

**(d)** The two weakest inputs are the **permeability** and the **viscosity**;
$\mathrm{Ra} \propto k_\mathrm{perm}/\mu$. To drop below critical from 18.7
requires a factor of 19 change. The viscosity of water cannot increase 19-fold
over any plausible temperature range, but the permeability *can* easily be a
factor of 19 lower — permeability varies by many orders of magnitude between
formations. The conclusion is therefore **robust against the viscosity and not at
all robust against the permeability**, which is why a Rayleigh calculation is a
screening exercise and not a prediction.

---

## ★★5 — Heat in place, and the engineering boundary

**(a)** $Q = \rho c V\Delta T = (2700)(900)(5\times10^{9})(150)
= 1.8225\times10^{18}$ J $= 1822.5$ PJ.

**(b)** $Q_\mathrm{rec} = R\,Q$, with $R$ dimensionless. The units of $R$ are those
of a fraction, and its value is an engineering assumption.

**(c)** $Q$ is **linear in both** the volume and the temperature excess, so
doubling either doubles $Q$. There is no larger effect per unit of relative
change — the sensitivity is unity in each, which is the reason a volumetric
estimate is never better than its two inputs.

**(d)** The recovery factor depends on the reservoir permeability and its spatial
connectivity, the well pattern and the flow rate that the wells actually deliver,
the reinjection temperature, the project lifetime, and the economics of all of
those. None of these is a measurement of the rock.

---

## ★★6 — Reading an apparent resistivity

**(a)** 0.01 s: 5.00 Ω m; 1 s: 11.16 Ω m; 100 s: 220.82 Ω m; 10 000 s:
457.94 Ω m.

**(b)** $11.16/5 = 2.23$ times the cap resistivity; $457.94/500 = 0.916$, i.e.
8.4 per cent below the basement resistivity.

**(c)** Because 11.16 Ω m is a weighted average of a conductive cap and a
resistive basement, dominated by the cap. Reading it as the reservoir would
conclude that the reservoir is about 11 Ω m — a conductor — when its true
resistivity is 500 Ω m, an error of a factor of 45.

**(d)** A thicker cap puts the transition at **longer** periods, because the
diffusive depth scale grows as $\sqrt{\rho T}$: to reach the same depth through
more conductive material requires a longer period. The practical consequence is
that the period range needed for a survey is set by the cap, not by the target,
and cannot be copied between fields.

---

## ★★★7 — Reading the demonstration

Quoted output from `geothermal_systems_demo.py`:

**(a)** $k = 2.5$, 25 K km⁻¹: 62.50 mW m⁻²; $k = 1.5$, 40 K km⁻¹: 60.00;
$k = 3.5$, 20 K km⁻¹: 70.00.

**(b)** At 1 km: 35.0 without the source, 35.4 with. At 2 km: 60.0 and 61.6.
At 3 km: 85.0 and 88.6. At 5 km: 135.0 and 145.0.

**(c)** 500 m/50 K: $\mathrm{Ra} = 10.27$, ratio 0.260, conductive.
1000 m/100 K: 41.06, ratio 1.040, convecting. 1000 m/50 K: 20.53, ratio 0.520.
2000 m/150 K: 123.19, ratio 3.121. 3000 m/200 K: 246.39, ratio 6.241.

**(d)** 1 km³, 100 K: 243.000 PJ; 10 km³, 150 K: 3645.000 PJ; 100 km³, 200 K:
48 600.000 PJ. Power: 2.1 and 4.2 MW_th at 10 kg s⁻¹; 10.5 and 20.9 at 50;
41.9 and 83.7 MW_th at 200 kg s⁻¹.

**(e)** 1 Ω m: 503.3 m at 1 s, 1591.5 at 10 s, 5032.9 at 100 s. 10 Ω m: 1591.5,
5032.9, 15915.5. 1000 Ω m: 15915.5, 50 329.2, 159 154.9.

**(f)** Half-space 100 Ω m: exactly 100.00 Ω m at every period. 500 m cap over
500 Ω m: 5.00, 4.15, 11.16, 66.01, 220.82, 379.71, 457.94 Ω m at 0.01, 0.1, 1,
10, 100, 1000 and 10 000 s. Cap over 50 Ω m: 5.00, 4.44, 8.47, 23.84, 38.93,
46.16, 48.75 Ω m.

**(g)** At 0.5 km: 2.00, 6.00, 12.00 K for +10, +30, +60 mW m⁻². At 1 km: 4.00,
12.00, 24.00. At 2 km: 8.00, 24.00, 48.00. At 3 km: 12.00, 36.00, 72.00 K.

**(h)** The heat flow, the conductive geotherm, the Rayleigh number, the skin
depth, the Cagniard apparent resistivity, the heat in place and the temperature
excess are **derived formulas** evaluated here. The convection criterion and the
linear phase-boundary treatment of the hydrate-like intersection problems are
**parameterisations**, and the Rayleigh conclusion in particular rests on assumed
permeability and viscosity. The mass flow rates, temperature contrasts and any
recovery factor used in a real assessment are **engineering inputs**, and the
demo deliberately leaves the recovery factor symbolic.

---

## ★★★8 — Interpretation and its limits

**(a)** A straight log over 2 km with a constant gradient implies **steady-state
conduction** through a column of uniform conductivity. Two processes that can
produce the same appearance without conduction being the mechanism:

1. **Advection at a rate that happens to give a linear profile.** Groundwater flow
   can impose a linear temperature–depth relation over an interval.
2. **A coincidental compensation**: a conductivity that increases with depth while
   the flux decreases (for example through a change in the radiogenic production)
   can also give a nearly straight log.

Both are distinguished by measuring the conductivity profile itself: a linear log
with a *varying* conductivity is not a conductive steady state, and the departure
is the diagnostic.

**(b)** The correct statement: "the MT data are consistent with a conductive layer
at about 1 km depth, which is likely to be a clay-rich alteration zone." The
conductor is a *conductivity* feature, and it may be a cap or an alteration halo
rather than a reservoir. The additional measurement that tests it is a
**temperature gradient** in a slim hole through the interval: if the layer is a
caprock, the gradient above it is steep and the interval below it is nearly
isothermal; a conductive mudstone with no heat source would show neither.

**(c)** A recovery factor is not observable by any physical method because it is
not a property of the rock at all: it is a statement about how much of the
contained energy a particular engineering design can extract under a particular
set of economic conditions, over a stated lifetime, with a stated reinjection
temperature. No survey can measure it, and no survey can falsify it. What a
geophysical study contributes is the **volume**, the **temperature**, the
**permeability structure** and the **geometry of the caprock** — the quantities
on which the recovery factor then operates.

**(d)** A 20 mW m⁻², 50 km-wide heat-flow anomaly: three possible causes, one of
them not thermal.

1. **A crustal heat source at depth**, such as a buried radiogenic granite. The
   discriminating observation is the *shape* of the anomaly and its correlation
   with the mapped geology: a broad anomaly matching the granite outline, with the
   gradient anomaly increasing with depth.
2. **A shallow convective system** redistributing heat laterally, which would show
   a locally disturbed gradient and, usually, a coincident conductivity anomaly
   from hydrothermal alteration. Discriminating observation: the MT/EM response
   and a local steepening of the gradient in the cap.
3. **Not thermal at all — a systematic error in the conductivity model.** A
   regionally consistent error in the assumed or measured conductivity, for
   example from a lithology that is systematically mis-assigned, reproduces a
   smooth broad anomaly with no geological correlation. Discriminating
   observation: a fresh set of conductivity measurements on cores from the
   anomaly, and a check of whether the anomaly boundary cuts across geology or
   follows it.
