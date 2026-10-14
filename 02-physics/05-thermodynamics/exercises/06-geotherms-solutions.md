# Solutions — 02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. All values are nominal unless stated.

---

## ★1 — Derivation

**(a)** The steady heat equation with $z$ downward and
$A(z) = A_0e^{-z/h}$ is $k\,\mathrm{d}^2T/\mathrm{d}z^2 = -A_0e^{-z/h}$.
Integrating once:
$\mathrm{d}T/\mathrm{d}z = (A_0h/k)e^{-z/h} + C$. Imposing
$\mathrm{d}T/\mathrm{d}z = q_0/k$ at $z = 0$ (because the upward flux is
$k\,\mathrm{d}T/\mathrm{d}z$ with $z$ downward) gives
$C = (q_0 - A_0h)/k$.

**(b)** Integrating again with $T(0) = T_0$:

$$T(z) = T_0 + \frac{q_0 - A_0h}{k}z
+ \frac{A_0h^2}{k}\left(1 - e^{-z/h}\right) .$$

**(c)** $q(z) = k\,\mathrm{d}T/\mathrm{d}z
= q_0 - A_0h\left(1 - e^{-z/h}\right)$, and as $z\gg h$ this tends to
$q_0 - A_0h$, the **mantle heat flow**.

**(d)** Since $\int_0^\infty A\,\mathrm{d}z = A_0h$, the surface heat flow is the
mantle flux plus the entire crustal radiogenic production. The assumption is
**steady, one-dimensional conduction**: in steady 1-D, none of the internal
production can flow downward, because there is no downward channel.

---

## ★2 — A specific geotherm

**(a)** $q_{\text{mantle}} = q_0 - A_0h = 0.055 - 1.0\times10^{-6}\times10^4
= 0.055 - 0.010 = 0.045$ W m⁻² $= 45$ mW m⁻².

**(b)** $0.010/0.055 = 18.2$ per cent.

**(c)** $T(35\ \mathrm{km}) = 283.15
+ (0.055-0.010)\times35\,000/2.5
+ (1.0\times10^{-6}\times10^8/2.5)(1-e^{-3.5})$.
Second term: $0.045\times14\,000 = 630.0$ K. Third:
$40\times(1-0.030\,197) = 40\times0.969\,803 = 38.79$ K. So
$T = 283.15+630.0+38.79 = 951.9$ K $= 678.8$ °C.

**(d)** $\bar G = (951.9-283.15)/35 = 19.11$ K km⁻¹.

---

## ★3 — The deeper gradient

**(a)** $T(50\ \mathrm{km}) = 283.15 + 0.045\times20\,000
+ 40(1-e^{-5}) = 283.15+900.0+40\times0.993\,262 = 283.15+900.0+39.73
= 1222.9$ K $= 949.7$ °C.

**(b)** $G_{35-50} = (1222.9-951.9)/15 = 18.07$ K km⁻¹, against 19.11 K km⁻¹ over
0–35 km.

**(c)** Because the exponentially distributed source is concentrated near the
surface. Its contribution to the gradient decays as $e^{-z/h}$, so by 35 km
(3.5 scale heights) it is essentially exhausted, and the gradient approaches its
asymptotic value $(q_0 - A_0h)/k = 0.045/2.5 = 0.018$ K m⁻¹ $= 18.0$ K km⁻¹.

**(d)** Well below the scale depth $h$ — the third term of the solution has
saturated by about $3h = 30$ km, beyond which the geotherm is linear with the
mantle gradient. That is why the deeper geotherm is a straight line, and why a
crustal geotherm's shape is a direct diagnostic of where the radiogenic elements
are concentrated.

---

## ★4 — Half-space cooling

**(a)** $q(t) = k\Delta T/\sqrt{\pi\kappa t}$, $d(t) = 2\sqrt{\kappa t}$.

**(b)** $\kappa = 3.2/(3300\times1250) = 7.7576\times10^{-7}$ m² s⁻¹.
At 10 Ma ($t = 3.1558\times10^{14}$ s):
$q = 3.2\times1300/\sqrt{\pi\times7.7576\times10^{-7}\times3.1558\times10^{14}}
= 4160/\sqrt{7.6905\times10^8} = 4160/27\,732 = 0.1500$ W m⁻²
$= 150.0$ mW m⁻²; $d = 2\sqrt{7.7576\times10^{-7}\times3.1558\times10^{14}}
= 2\times15\,646 = 31\,293$ m $= 31.3$ km.
At 40 Ma: 75.0 mW m⁻² and 62.6 km. At 70 Ma: 56.7 mW m⁻² and 82.8 km.

**(c)** $q\sqrt t = k\Delta T/\sqrt{\pi\kappa} = 4160/1.5611\times10^{-3}
= 2.665\times10^6$ W m⁻² s$^{1/2}$, constant to the digits carried.

**(d)** At **10 Ma** the model overpredicts, because hydrothermal circulation removes
heat advectively through the young, fractured crust. At **40 Ma** the model is
close to observation. At **70 Ma** the model begins to underpredict, because the
thermal boundary layer has approached the base of a finite plate and the
$t^{-1/2}$ law must give way to a plate model in which heat flow flattens.

---

## ★★5 — Reading the demo

**(a)**

| Province | $q_0$ | $q_m$ | radiogenic % | $T$@20 km | $T$@50 km |
|---|---|---|---|---|---|
| Craton | 40.0 | 30.0 | 25.0 | 284.6 °C | 649.7 °C |
| Stable platform | 60.0 | 50.0 | 16.7 | 444.6 °C | 1049.7 °C |
| Extensional basin | 85.0 | 75.0 | 11.8 | 644.6 °C | 1549.7 °C |

**(b)** By the 1300 °C criterion: 104.2, 62.5 and 41.7 km. By adiabat
intersection (potential temperature 1550 K): 105.8, 62.6 and 41.5 km.

**(c)** Because $A_0h$ is the same in all three rows (10 mW m⁻²) while $q_0$
differs, so $A_0h/q_0$ is largest where $q_0$ is smallest. A cold province has a
proportionally larger self-heating contribution.

**(d)** Because they exceed the peridotite solidus: 1250, 2050 and 3050 °C at
100 km, and 1850, 3050 and 4550 °C at 150 km. A mantle that conducted would be
molten, so the conductive geotherm must be abandoned at the lithosphere base. The
columns are the *argument for convection*, not a temperature prediction.

---

## ★★6 — Global heat loss

**(a)** $\bar q = 0.29\times65 + 0.71\times100 = 18.85 + 71.0 = 89.85$ mW m⁻².
$\dot Q = 0.089\,85\times5.10\times10^{14} = 4.582\times10^{13}$ W
$= 45.8$ TW.

**(b)** 75 mW m⁻²: $0.075\times5.10\times10^{14} = 3.825\times10^{13}$ W
$= 38.3$ TW. 95 mW m⁻²: $4.845\times10^{13}$ W $= 48.5$ TW.

**(c)** The answer moves by ±10 per cent for a ±10 mW m⁻² change in the mean,
which is itself within the province-to-province range. So a statement of the form
"the Earth loses X TW" is defensible to two significant figures only if the mean
heat flow is stated; otherwise it is an order-of-magnitude statement.

**(d)** Because a drill hole measures the local gradient and conductivity at one
place, over a depth range of a few kilometres, in a province whose heat flow may
differ from the global mean by a factor of two. The global mean is a spatial
integral of a heterogeneous field — a statistic, not an observation.

---

## ★★7 — Radiogenic inventory

**(a)** $A V = 1.0\times10^{-6}\times1.479\times10^{14}\times35\times10^3
= 1.0\times10^{-6}\times5.1765\times10^{18} = 5.18\times10^{12}$ W $= 5.18$ TW.

**(b)** $1.0\times10^{-8}\times8.889\times10^{20} = 8.889\times10^{12}$ W
$= 8.89$ TW.

**(c)** Doubling both: continental $10.35$ TW, mantle $17.78$ TW. The continental
term rises by 5.18 TW (35 per cent of the original total of 14.57 TW) and the
mantle term by 8.89 TW (61 per cent). **The mantle dominates the sensitivity.**

**(d)** The mantle, because its composition is inferred indirectly — from the
composition of mid-ocean-ridge basalt and from chondritic or primitive-mantle
models — whereas the continental crust can be sampled directly in outcrop. A
factor of two in the mantle's heat production is a serious possibility; a factor
of two in the average continental crustal value is less likely but not excluded.

---

## ★★8 — Secular cooling

**(a)** $45 - 14.6 = 30.4$ TW.

**(b)** $\mathrm{d}T/\mathrm{d}t = 30.4\times10^{12}/(4.0\times10^{24}\times1250)
= 3.04\times10^{13}/5.0\times10^{27} = 6.08\times10^{-15}$ K s⁻¹.
Multiply by $3.155\,76\times10^7$ s yr⁻¹ and by $10^9$:
$6.08\times10^{-15}\times3.1558\times10^{16} = 192$ K per 10⁹ yr.

**(c)** With production 20 TW the deficit is 25 TW and the rate is
$25/30.4\times192 = 158$ K per 10⁹ yr, i.e. 18 per cent lower.

**(d)** (i) Part of the surface loss is balanced by cooling of the core and by
latent heat released as the inner core grows (lesson 02-05-07 §4.4 gives ~1.9 TW
for an adopted growth rate), not by mantle cooling. (ii) The mantle's heat
production is very likely higher than the adopted 0.01 µW m⁻³, in which case the
deficit is smaller. Both corrections push the answer down.

---

## ★★9 — Reading the demo

**(a)** Deficit 31.25 TW.

**(b)** $6.2439\times10^{-15}$ K s⁻¹ $= 197.0$ K per 10⁹ yr.

**(c)** The mantle heat production (0.01 µW m⁻³) dominates, because it contributes
8.89 TW of the 14.57 TW total. Halving it to 0.005 µW m⁻³ reduces the
production to 10.13 TW and raises the deficit to 35.7 TW, a 14 per cent increase
in the deficit and hence in the cooling rate (to 225 K per 10⁹ yr). Halving the
*continental* value instead changes the deficit by only 8 per cent.

**(d)** Because the inputs are nominal concentrations applied to model volumes,
the residual is a difference of two uncertain numbers, and part of the loss is
borne by the core. A single number would imply a precision that does not exist;
"a deficit of order 30 TW, implying cooling of order 10² K per 10⁹ yr for the
stated inventory" is both accurate and useful.

---

## ★★★10 — A geotherm for a chosen setting

This is an open problem; the following is the shape of a defensible answer.
Take an **extensional basin**.

**(a)** Inputs: (i) **transport** — steady 1-D conduction, valid only to the
lithosphere base; (ii) **source** — exponentially distributed crustal production
with $A_0 = 1.0$ µW m⁻³ and $h = 10$ km, plus a mantle contribution; (iii)
**boundary conditions** — $T_0 = 283.15$ K, $q_0 = 85$ mW m⁻² (a nominal
extensional value), and an adiabatic mantle at depth.

**(b)** $q_{\text{mantle}} = 75$ mW m⁻² (11.8 per cent radiogenic). From the
demo's table, $T(20\ \mathrm{km}) = 644.6$ °C and $T(50\ \mathrm{km}) = 1549.7$ °C;
the Moho at 30 km is between them, at
283.15 + 0.075\times30\,000/2.5 + 40(1-e^{-3}) = 1221.2 K = **948 °C**. The lithosphere base is 41.7 km
by the 1300 °C criterion. Note that the Moho temperature is below the lithosphere
base temperature here, which is a consistency check: the crust has not reached the
convective regime.

**(c)** The value that cannot be defended from a verified source is $q_0 = 85$
mW m⁻² *for this basin*: it is a nominal extensional-province value, not a
measurement at a named site. Equally, $A_0$ and $h$ are nominal. **Both should be
stated as such**, and the answer should say that a real study replaces them with
the basin's own heat-flow and geochemical data.

**(d)** Two falsifying observations: (i) a measured heat-flow profile that is
non-linear below 5 km — which would indicate advective transport by groundwater
(lesson 02-05-05 §3.7) rather than the pure conduction assumed; and (ii) a
measured Moho temperature from mantle xenolith thermobarometry that differs from
the computed value by more than the combined uncertainty, which would falsify
either $q_0$ or the source distribution.

---

## ★★★11 — The budget as an inverse problem

**(a)** $\dot Q_{\text{loss}}$ is **measured** (a spatial integral of heat-flow
measurements, each corrected). $\dot Q_{\text{rad}}$ is **computed from an
assumed composition** applied to a model volume — the volumes come from seismology
and are reasonably well known, the concentrations do not. $\dot Q_{\text{cool}}$
is **defined as the residual** and is therefore neither measured nor independently
computed.

**(b)** Because it is obtained by subtraction, it inherits the error of both terms
and has no independent observational content. If the assumed radiogenic inventory
were exactly equal to the true production, the residual would be the true cooling;
if the assumption is wrong, the residual is a mixture of cooling and inventory
error, and the two cannot be separated from surface data alone.

**(c)** **Geoneutrino detection** converts the radiogenic term from an assumption
to a measurement, because the antineutrinos emitted by ²³⁸U and ²³²Th decay
escape the Earth and can be counted. The current uncertainty on that measurement
is limited by counting statistics and by the signal from the crust and the nearby
reactor background; **the specific percentage is not quoted here** because it
changes with each published result and this repository has not verified a value.

**(d)** A residual that is 68 per cent of the largest term is not a result; it is
the difference of two numbers of comparable size, and drawing a conclusion from it
requires the assumptions to be carried explicitly. Reporting the assumptions lets
a reader test the sensitivity themselves, which is the only honest way to present
a quantity dominated by an unverified input. The value of the analysis is the
*structure* — the demonstration that surface loss exceeds internal production, and
by roughly a factor of three — not the two-digit cooling rate that the structure
implies.
