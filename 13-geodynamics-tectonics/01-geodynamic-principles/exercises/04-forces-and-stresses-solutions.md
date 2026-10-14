# Solutions — 13-01-04 Driving Forces, Stress Fields and Intraplate Stress

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson:
[04 Driving Forces](../04-forces-and-stresses.md). Constants:
$g = 9.81\ \mathrm{m\,s^{-2}}$, $\rho_m = 3300\ \mathrm{kg\,m^{-3}}$,
$\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$, $T_m = 1300$ K,
$\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, $\rho_w = 1030\ \mathrm{kg\,m^{-3}}$,
$1\ \mathrm{Myr} = 3.1557\times10^{13}\ \mathrm{s}$.

---

## ★1 — Subsidence at other ages

The thermal subsidence is $s(t) = s(100\ \mathrm{Myr})\sqrt{t/100}$:

$$s(25) = 3593.8\sqrt{0.25} = 1796.9\ \mathrm{m},
\qquad
s(400) = 3593.8\sqrt{4} = 7187.6\ \mathrm{m} .$$

**Scaling:** $s\propto\sqrt{t}$, the signature of a boundary layer thickening as
$\sqrt{\kappa t}$. The 400 Myr value is not geological — a real plate is capped by
convection and a plate model flattens the curve — which is exactly why the
half-space law is a *young*-ocean approximation.

---

## ★2 — Ridge push at other ages

The anomaly is $\Delta\rho(y,t) = \rho_m\alpha T_m\,\mathrm{erfc}(y/2\sqrt{\kappa
t})$, so its characteristic depth scales as $\sqrt{t}$ and
$F_{RP} = g\int\zeta\Delta\rho\,\mathrm{d}\zeta \propto (\sqrt{t})^{2} = t$:

$$F_{RP}(25) = 4.11\times10^{12}\times0.25 = 1.028\times10^{12}\ \mathrm{N\,m^{-1}},$$

$$F_{RP}(50) = 4.11\times10^{12}\times0.50 = 2.055\times10^{12}\ \mathrm{N\,m^{-1}} .$$

**Linear**, not $\sqrt{t}$, and the reason is the extra factor of depth in the
first moment: the anomaly *amplitude* is fixed (it saturates at
$\rho_m\alpha T_m$) while the anomaly *extent* grows as $\sqrt{t}$, and the
moment weights extent by depth, giving one more factor of $\sqrt{t}$. A student
who expects all cooling-plate quantities to scale as $\sqrt{t}$ gets this wrong
by a factor of $\sqrt{t}$ — here a factor of 5 at 25 Myr.

---

## ★3 — Units of GPE

$$\mathrm{GPE} = g\int\zeta\rho\,\mathrm{d}\zeta :
\mathrm{m\,s^{-2}}\times\mathrm{m}\times\mathrm{kg\,m^{-3}}\times\mathrm{m}
= \mathrm{kg\,m^{-1}\,s^{-2}} = \mathrm{N\,m^{-1}} .$$

$\mathrm{N\,m^{-1}}$ is a force per unit length — the same unit as $V_0$, and the
same unit as every driving force in the inventory. ✔ The check is worth doing
because it is the reason driving forces are quoted *per unit length* and why
multiplying by a plate width (a "total force") invites three-orders-of-magnitude
errors.

---

## ★★4 — Slab pull for an 80 km slab

$$\int_0^{h}\Delta\rho\,\mathrm{d}y
= \int_0^{8\times10^{4}}\rho_m\alpha T_m\,\mathrm{erfc}\!\left(\frac{y}
{2\sqrt{\kappa t}}\right)\mathrm{d}y
= 6.4768\times10^{6}\ \mathrm{kg\,m^{-2}},$$

$$\langle\Delta\rho\rangle = \frac{6.4768\times10^{6}}{8\times10^{4}}
= 80.96\ \mathrm{kg\,m^{-3}},$$

$$F_{SP} = gL\int\Delta\rho\,\mathrm{d}y
= (9.81)(5\times10^{5})(6.4768\times10^{6})
= 3.1769\times10^{13}\ \mathrm{N\,m^{-1}} = 31.77\ \mathrm{TN\,m^{-1}} .$$

Compare with the same slab length for a 100 km slab. The lesson's integral is
$7.1423\times10^{6}\ \mathrm{kg\,m^{-2}}$ at $h = 100$ km, so
$F_{SP}(100\ \mathrm{km}, 500\ \mathrm{km}) = 35.03\ \mathrm{TN\,m^{-1}}$
(the lesson's 42.04 is for $L = 600$ km).

**Thickness dependence.** Cutting the thickness by 20% cuts the force by only
9.3%, a local exponent of

$$p = \frac{\ln(31.77/35.03)}{\ln(0.8)} = \frac{-0.0976}{-0.2231} = 0.44 .$$

The mean anomaly *rises* (from 71.42 to 80.96 kg m$^{-3}$) because the deeper,
warmer, less anomalous part of the slab has been removed. A slab is not a block:
its buoyancy, like its strength, lives in its cold top, and any argument that
treats slab pull as proportional to plate thickness overestimates the force from
thick, old plates.

---

## ★★5 — Plate speed for a lower viscosity

$$F_{\text{net}} = |F_{SP}| + |F_{RP}|
= 3.1769\times10^{13} + 4.11\times10^{12}
= 3.5880\times10^{13}\ \mathrm{N\,m^{-1}},$$

$$u = \frac{F_{\text{net}}d}{\eta L_p}
= \frac{(3.5880\times10^{13})(2\times10^{5})}{(5\times10^{20})(5\times10^{6})}
= 2.870\times10^{-9}\ \mathrm{m\,s^{-1}} = 90.6\ \mathrm{mm\,yr^{-1}} .$$

Compared with the lesson's 58.3 mm/yr at $\eta = 10^{21}$ Pa s, the speed changed
by a factor of $90.6/58.3 = 1.55$. It is *not* exactly the factor of 2 in
viscosity, because the driving force also changed (the 100 km slab became an
80 km one) and because the two changes move in opposite directions: viscosity fell
by 2 (speeding the plate by 2) while the force fell by 0.78 (slowing it by 0.78),
giving $2\times0.78 = 1.55$. ✔ Getting this arithmetic to close is a good
self-check that the balance has been assembled correctly.

---

## ★★6 — The closed form for the plateau GPE difference

**Assumptions.** (i) Airy isostasy, i.e. compensation at the Moho with a common
mantle density below; (ii) uniform crustal density $\rho_c$ and mantle density
$\rho_m$.

With $\zeta$ measured upward from a common compensation depth, the GPE per unit
area of a column with crustal thickness $h$ and elevation $e(h) = h(\rho_m -
\rho_c)/\rho_m$ above the reference datum is

$$\mathrm{GPE}(h) = g\left[\frac{\rho_m}{2}(t-h)^{2}
+ \frac{\rho_c}{2}\left(t^{2} - (t-h)^{2}\right)\right],
\qquad t = D + e(h) .$$

Expanding with $t = D + \Delta h/\rho_m$ and $\Delta = \rho_m-\rho_c$:

$$\mathrm{GPE}(h) = \frac{g\rho_m D^{2}}{2}
+ \frac{g h^{2}}{2}\,\Delta\left(1 - \frac{\Delta}{\rho_m}\right)
= \frac{g\rho_m D^{2}}{2} + \frac{g h^{2}}{2}\Delta\frac{\rho_c}{\rho_m} .$$

The $D$-dependent term is common to both columns and cancels on differencing:

$$\Delta\mathrm{GPE} = \frac{g}{2}\left(h_2^{2} - h_1^{2}\right)
(\rho_m - \rho_c)\frac{\rho_c}{\rho_m} . \qquad\checkmark$$

With $h_1 = 35$ km, $h_2 = 70$ km, $\rho_c = 2800$:

$$\Delta\mathrm{GPE} = \frac{9.81}{2}(4.9\times10^{9} - 1.225\times10^{9})(500)
\frac{2800}{3300} = 7.647\times10^{12}\ \mathrm{J\,m^{-2}},$$

matching the lesson's numerical double integral ($7.648\times10^{12}$) to
$1.3\times10^{-4}$. The cancellation of the $D$-term *is* the isostasy
condition, and it is the reason the answer is independent of the compensation
depth.

---

## ★★★7 — Uncertainty budget

Propagating independent fractional uncertainties:

| input | uncertainty | effect on $u$ |
|---|---|---|
| $\Delta\rho$ | 10% | 10% (linear) |
| slab length $L$ | 25% | 25% (linear, via $F_{SP}$) |
| plate length $L_p$ | — | (if uncertain, linear) |
| $\eta$ | 50% | 50% (linear, $u\propto1/\eta$) |
| channel thickness $d$ | 20% | 20% (linear) |

Since $u = (F_{SP}+F_{RP})d/(\eta L_p)$ is a product of powers, fractional errors
add in quadrature:

$$\frac{\sigma_u}{u} \approx \sqrt{0.10^{2} + 0.25^{2} + 0.50^{2} + 0.20^{2}}
= \sqrt{0.0100+0.0625+0.2500+0.0400} = \sqrt{0.3625} = 0.602 .$$

**Absolute plate speed: viscosity dominates**, contributing 69% of the variance.
**Relative speeds of two plates:** the shared factors $d$, $\eta$ and $L_p$
cancel, leaving the slab length (and the age, through $\Delta\rho$) as the only
discriminants. That is the quantitative reason the observed correlation of plate
speed with slab length is a robust result even though absolute speeds are not:
the correlation uses ratios in which the badly known viscosity has cancelled.

---

## ★★★8 — Critique of "the intraplate stress is 109 MPa"

*Model answer.* The 109 MPa figure is $\Delta\mathrm{GPE}/h_2$: an excess
gravitational potential energy per unit area divided by the thickness of the
layer that must carry it. That division is the step that turns a bound into an
apparent measurement. It assumes (i) that the excess GPE is supported uniformly
over the full 70 km of thickened crust, when in fact GPE anomalies are carried by
the *elastic* part of the lithosphere — measured elsewhere in this module to be a
few kilometres thick in bending, not tens; (ii) that nothing has relaxed; a
plateau is millions of years old, and viscous relaxation of the deepest, hottest
part of a lower crust reduces the deviatoric stress it supports; and (iii) that
the stress is horizontal and depth-independent, when the real field varies with
depth along the strength envelope.

The author should therefore write "an upper bound of 109 MPa on the
depth-averaged deviatoric stress in a 70 km crust, if the excess GPE were carried
uniformly". To make a stress estimate defensible requires a strength envelope
(at a stated geotherm and strain rate) to establish which depth interval can
actually maintain the stress, and either focal-mechanism inversions or geodetic
strain rates to test whether the region is deforming in the way the stress
implies. Without those, the number is a scaling estimate and should be labelled
as one.

---

## ★★★9 — Testing ridge push against slab pull

**Observable.** The velocities of several plates, expressed relative to a common
frame, together with their attached slab lengths and their ridge lengths.

**Model.** $u \propto (A\,S + B\,R)/\eta$, where $S$ is the slab length (scaled
from slab pull) and $R$ a ridge-length or ridge-distance proxy (scaled from ridge
push), with shared drag parameters. Estimate $A$ and $B$ (or their ratio) by
regression across plates.

**Signatures.** If slab pull dominates, the velocity should correlate with slab
length (and with the age of the subducting plate, through $\Delta\rho$) and be
largely independent of ridge length. If ridge push dominates, velocity should
correlate with ridge length or with the distance from the ridge, and a plate with
no slab (e.g. a purely spreading plate) should still move quickly.

**Principal confound.** The forces are not independent of the kinematics: ridge
push and slab pull both act along the plate, and the viscous drag is only crudely
represented by a single coefficient. A more serious confound is that slab length
and plate motion are causally entangled in the other direction — fast plates
subduct more slab — so a correlation between speed and slab length is not by
itself evidence of the force. The test becomes conclusive only with a kinematic
model that predicts slab lengths from the plate geometry independently of the
measured speeds, for example from a plate reconstruction over the past 50 Myr.
