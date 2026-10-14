# Solutions — 04-06-01 Source, Reservoir, Seal and Trap

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

The kinetic model is a **parameterisation** and the seal and impedance numbers are
**model results**; every rate below carries its coefficient. No reserve, recovery
factor or production volume is stated.

---

## ★1 — Geotherm and the window as a depth interval

**(a)** $T = 15 + 30\times10^{-3} \times 3000 = 15 + 90 = 105\ ^\circ$C.

**(b)** $z_{60} = (60-15)/30\times10^{-3} = 1500$ m;
$z_{120} = (120-15)/30\times10^{-3} = 3500$ m. The window spans 1.5 to 3.5 km.

**(c)** At 20 K km⁻¹: $z_{60} = 45/0.020 = 2250$ m and
$z_{120} = 105/0.020 = 5250$ m.

**(d)** The window is defined by the temperature range over which the generation
reactions proceed at a useful rate, and temperature is encountered at whatever
depth the local gradient puts it: a shallower gradient places the same window
deeper.

---

## ★2 — Arrhenius conversion

**(a)** $k = 10^{13}\exp[-2.0\times10^{5}/(8.314 \times 383.15)]
= 5.428\times10^{-15}$ s⁻¹.

**(b)** $t = -\ln(0.9)/k = 0.105361/5.428\times10^{-15}
= 1.941\times10^{13}$ s $= 6.151\times10^{5}$ yr.

**(c)** At 90 °C, $k = 1.710\times10^{-16}$ s⁻¹ and
$t = 1.952\times10^{7}$ yr; the ratio is **31.7** for a 20 K decrease.

**(d)** Kerogen is a mixture, so generation is a *set* of parallel reactions with
a distribution of activation energies, and the reactions are not first order in a
single species. The correct use of this model is to demonstrate the temperature
and heating-rate dependence, not to predict a maturity from one rate constant.

---

## ★3 — Compaction, porosity and density

**(a)** $\phi = 0.45\exp(-1500/2500) = 0.45\exp(-0.6) = 0.45(0.5488) = 0.2470$.

**(b)** $\rho = (0.2470)(1030) + (0.7530)(2650) = 254.4 + 1995.5 =
2249.9$ kg m⁻³.

**(c)** At 3000 m: $\phi = 0.45\exp(-1.2) = 0.1355$ and
$\rho = 139.6 + 2290.8 = 2430.4$ kg m⁻³.

**(d)** The **shallow** interval has the larger rate of change: the exponential
has its steepest slope at the surface. Between the surface and 1500 m the density
rises from 1921 to 2249.9 kg m⁻³, a change of about 330; between 1500 m and
3000 m it rises by only 180 kg m⁻³. This is why a
velocity or density trend fitted over a deep interval extrapolates badly upward,
and why a time–depth conversion is least reliable in the shallow section.

---

## ★★4 — Seal capacity

**(a)** $P_c = 2\sigma/r = 2(0.025)/(0.5\times10^{-6}) =
1.00\times10^{5}$ Pa.

**(b)** $\Delta\rho = 1050 - 200 = 850$ kg m⁻³, so
$h = 1.00\times10^{5}/(850 \times 9.81) = 11.99$ m.

**(c)** $\Delta\rho = 1050 - 750 = 300$ kg m⁻³, so
$h = 1.00\times10^{5}/(300 \times 9.81) = 33.98$ m.

**(d)** The **pore-throat radius**, to the first power: $h \propto 1/r$. Halving
$r$ doubles the capacity, and $r$ is the least well known of the four inputs
because a real seal has a *distribution* of throat radii.

---

## ★★5 — Impedance and the bright spot

**(a)** $Z_\mathrm{shale} = 2450 \times 3200 = 7.840\times10^{6}$ kg m⁻² s⁻¹.

**(b)** $Z_\mathrm{brine} = 2150 \times 2800 = 6.020\times10^{6}$; so
$R = (6.020 - 7.840)/(6.020 + 7.840) = -0.1313$.

**(c)** $Z_\mathrm{gas} = 2000 \times 2500 = 5.000\times10^{6}$; so
$R = (5.000 - 7.840)/(5.000 + 7.840) = -0.2212$.

**(d)** Amplitude ratio $= 0.2212/0.1313 = 1.685$. Both are **negative**, so both
are troughs at the top of the reservoir on a normal-polarity section: the fluid
changes the *amplitude* by a factor of 1.7 and not the polarity. A polarity
reversal therefore indicates a *harder* unit above the reservoir, not a fluid.

---

## ★★6 — Effective stress and overpressure

**(a)** $\sigma_v = 2400 \times 9.81 \times 3000 = 7.063\times10^{7}$ Pa
$= 70.63$ MPa. $p = 1030 \times 9.81 \times 3000 = 3.031\times10^{7}$ Pa
$= 30.31$ MPa.

**(b)** $\sigma_v' = 70.63 - 30.31 = 40.32$ MPa.

**(c)** At 1.5 times hydrostatic, $p = 45.47$ MPa and
$\sigma_v' = 70.63 - 45.47 = 25.16$ MPa.

**(d)** The reduction is $100(40.32 - 25.16)/40.32 = 37.6$ per cent. Because
compaction, porosity, velocity and permeability are all functions of *effective*
stress rather than depth, a velocity–depth trend calibrated in a normally
pressured well overpredicts the velocity (and hence the depth) in an
overpressured compartment by a large margin. This is the standard route by which
a depth conversion goes wrong in a subsalt or deep-water setting.

---

## ★★★7 — Reading the demonstration

Quoted output from `petroleum_system_demo.py`:

**(a)** $20$ K km⁻¹: 2.500 to 5.500 km; $25$ K km⁻¹: 2.000 to 4.400 km;
$40$ K km⁻¹: 1.250 to 2.750 km.

**(b)** 60 °C: $k = 4.391\times10^{-19}$ s⁻¹, $t = 7.603\times10^{9}$ yr;
100 °C: $k = 1.009\times10^{-15}$ s⁻¹, $t = 3.308\times10^{6}$ yr;
180 °C: $k = 8.840\times10^{-11}$ s⁻¹, $t = 3.777\times10^{1}$ yr.

**(c)** 1 K Myr⁻¹: 97.1 °C; 3: 103.2; 10: 110.2; 30: 116.9 °C.

**(d)** At 500 m: $\phi = 0.3894$, $\rho = 2019.2$ kg m⁻³, $\sigma_v = 9.49$ MPa,
$\sigma_v' = 4.44$ MPa. At 4 km: $\phi = 0.0677$, $\rho = 2540.4$ kg m⁻³,
$\sigma_v = 90.34$ MPa, $\sigma_v' = 49.92$ MPa.

**(e)** 1 km: one-way 0.490 s, TWT 0.980 s; 4 km: one-way 1.196 s, TWT 2.392 s.

**(f)** Gas: $\Delta\rho = 830$ kg m⁻³, $P_c = 3.000\times10^{5}$ Pa,
$h_{\max} = 36.84$ m. Oil: $\Delta\rho = 230$ kg m⁻³, $P_c = 2.500\times10^{5}$ Pa,
$h_{\max} = 110.80$ m. Sensitivity: 147.38 m at $r = 0.05$ µm, 73.69 at 0.10,
36.84 at 0.20 and 7.37 m at 1.00 µm.

**(g)** Shale over brine sand $R = -0.0153$; over gas sand $R = -0.1326$; over
limestone $R = +0.2540$. Amplitude ratio gas/brine $= 8.66$.

**(h)** $100$ km² × 50 m: $4.836\times10^{11}$ kg $= 0.484$ Gt;
$1000$ km² × 100 m: $9.672\times10^{12}$ kg $= 9.672$ Gt.

**(i)** The geotherm depths, the Athy porosity and density, the stress integrals,
the travel times, the capillary pressures and column heights, the impedances and
the reflection coefficients, and the organic-carbon mass are **computed from
derived relations**. The kinetic conversion times rest on a **parameterisation**
(the single-reaction model with a chosen $E_a$ and $A$), and would change with a
different scheme. The porosities at the surface, the density and velocity trends,
the interfacial tensions, the throat radius and the rock properties would have to
come from **measurement** in a real study; every other number is conditional on
them.

---

## ★★★8 — Interpretation and its limits

**(a)** Two mechanisms for a bright amplitude without a commercial accumulation:

1. **Fizz gas.** A small free-gas saturation (< 10 per cent) collapses the fluid
   modulus and lowers $v_P$ almost as much as a full gas charge would (see
   [04-06-05](./05-unconventional-resources-solutions.md)), so the impedance
   anomaly saturates at low saturation. Discriminating observation: a shear
   measurement or a $v_P/v_S$ analysis, which is far less sensitive to a small gas
   fraction.
2. **A lithology or tuning effect.** A tight, low-velocity unit, or a thin
   reservoir near the tuning thickness, produces an amplitude anomaly with no
   fluid involved. Discriminating observation: well control at the location, or an
   amplitude-versus-offset behaviour that separates a fluid effect from a
   lithology effect.

**(b)** The conversion is a time–temperature integral, so the temperature at
which a fixed conversion is reached rises with the heating rate. A rapidly
subsiding margin passes through each temperature quickly and therefore needs a
higher temperature — a greater depth — to reach the same maturity. A play mapped
by present-day depth alone will therefore mis-rank two areas with different
subsidence histories: the "deeper" one is not necessarily the more mature.

**(c)** A single entry pressure is inadequate because the capacity is inversely
proportional to the pore-throat radius and a real seal contains a *distribution*
of throat radii, from micrometres to tens of nanometres. An appropriate
presentation is a distribution of capacities (equivalently of column heights),
usually summarised by a range or by a percentile exceedance curve, with the
measurement method stated.

**(d)** In order of expected magnitude:

1. **The closure geometry converted to depth**, which depends on the velocity
   model used for time-to-depth conversion. This is the largest and it is a
   geophysical-modelling uncertainty.
2. **The fluid saturation and net-to-gross**, which determine how much of the
   pore volume is hydrocarbon. The amplitude anomaly constrains this only weakly
   because of the fizz-gas non-uniqueness.
3. **The recovery factor**, which is **not geophysical at all**: it is an
   engineering and economic quantity that depends on permeability, completion
   design, well spacing, price and regulation.

A volume estimate is therefore a *conditional* statement, and the condition is
usually stated last and matters most.
