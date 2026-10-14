# Solutions — 02-05-02 First Law, Work and Energy Balances

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

Sign convention used throughout: $\mathrm{d}U = \delta Q - \delta W$, with
$\delta Q > 0$ into the system, $\delta W > 0$ done by the system.

---

## ★1 — A two-step cycle

**(a)** Step 1: $\Delta U = 2.0 - 1.2 = +0.8$ MJ. Step 2:
$\Delta U = -0.5 - 0.8 = -1.3$ MJ.

**(b)** Cycle total $= 0.8 - 1.3 = -0.5$ MJ. For a *closed cycle* returning to
the initial state it must be **zero**; this pair of steps is therefore not a
closed cycle but a net decrease of internal energy by 0.5 MJ. The net work done
(1.2 + 0.8 = 2.0 MJ) exceeds the net heat absorbed (2.0 − 0.5 = 1.5 MJ) by
exactly 0.5 MJ, which is the correct and consistent reading.

**(c)** Adopting $\mathrm{d}U = \delta Q + \delta W$ would flip the sign of every
$W$ term and turn step 1 into $\Delta U = +3.2$ MJ and step 2 into
$\Delta U = +0.3$ MJ. The *physics* is unchanged; only the bookkeeping differs.
This is why every calculation must state its convention — a reader who assumes the
other one will find an inconsistency that is not there.

---

## ★2 — The mantle adiabat

**(a)** $\mathrm{d}T/\mathrm{d}P = \alpha T/(\rho c_p)
= (3\times10^{-5}\times1500)/(3300\times1250)
= 0.045/4.125\times10^6 = 1.0909\times10^{-8}$ K Pa⁻¹ $= 10.91$ K GPa⁻¹.

**(b)** With $\rho g = 3300\times9.806\,65 = 32\,362$ Pa m⁻¹ $= 3.2362\times10^{-5}$
GPa m⁻¹, $\mathrm{d}T/\mathrm{d}z = 10.91\times3.2362\times10^{-5}
= 3.531\times10^{-4}$ K m⁻¹ $= 0.353$ K km⁻¹.

**(c)** $\Delta P = \rho g\times50\times10^3 = 1.618\times10^9$ Pa
$= 1.618$ GPa, so $\Delta T = 10.91\times1.618 = 17.7$ K.

**(d)** No. Adiabatic descent at these rates heats the mantle by only ~18 K per
50 km, and the process is *reversible for the parcel* — the parcel would cool by
the same amount on the way back up. A plume is a parcel that was already hotter
than its surroundings, so its excess temperature is carried, not generated.
Adiabatic heating can only redistribute the existing temperature field along a
gradient; it cannot create a 200–300 K anomaly relative to an adiabatically
stratified reference.

---

## ★3 — Geothermal plant balance

**(a)** $\dot Q = \dot m c_p\Delta T = 80\times4186\times140
= 4.689\times10^7$ W $= 46.89$ MW thermal.

**(b)** Electrical $= 0.11\times46.89 = 5.16$ MW. Rejected
$= 46.89 - 5.16 = 41.73$ MW.

**(c)** $5.16 + 41.73 = 46.89$ MW, equal to the input ✓. The first law closes for
any $\eta$.

**(d)** Carnot: $1 - 313.15/453.15 = 0.3089$. The realised efficiency is
$0.11/0.3089 = 35.6$ per cent of the bound. The gap is irreversibility —
finite-rate heat exchangers, turbine losses, wellbore pressure drop, and the
reservoir's own depressurisation — not missing energy.

---

## ★4 — $H$ or $U$?

(i) **$U$.** A closed parcel exchanges no mass, so the $pV$ term is irrelevant
and $\mathrm{d}U = \delta Q - p\,\mathrm{d}V$ is the direct statement.

(ii) **$H$.** A flowing wellbore has fluid entering and leaving, and the
flow-work $pV$ must be accounted for; the steady-flow equation
$\dot m(h_2-h_1) = \dot Q$ is the natural form.

(iii) **$U$.** At constant volume $\delta W = 0$, so all the heat goes into
internal energy and $H$ would add a spurious pressure term.

---

## ★★5 — Reading the demo

**(a)** Mantle: 11.6364 K GPa⁻¹ and 0.3766 K km⁻¹. Crust: 2.9630 K GPa⁻¹ and
0.0785 K km⁻¹. Outer core: 5.1948 K GPa⁻¹ and 0.5604 K km⁻¹.

**(b)** 9.7579 K km⁻¹.

**(c)** For a gas $\alpha = 1/T$ exactly, so equation (6) collapses to $g/c_p$,
which is $\sim 9.76\times10^{-3}$ K m⁻¹ — nearly 26 times the mantle value. For a
solid, $\alpha T$ is small: at 1600 K, $\alpha T = 0.048$, so the effective
"thermal expansion per kelvin" is only 4.8 per cent, against 100 per cent for an
ideal gas.

**(d)** Because $\alpha$ for crustal rock is smaller than for mantle rock
($8\times10^{-6}$ against $3\times10^{-5}$) and the density is lower while $c_p$
is lower as well; the combination $\alpha/c_p$ falls faster than $T$ rises. The
result is physically important: the crustal adiabat is so small that it is
irrelevant, and a crustal temperature profile is set by conduction alone.

---

## ★★6 — Hydrothermal circulation

**(a)** $\dot Q = 50\times4186\times60 = 1.256\times10^7$ W $= 12.56$ MW.

**(b)** $\Delta h = c_p\Delta T = 4186\times(-30) = -1.256\times10^5$ J kg⁻¹;
total $\dot m\Delta h = 50\times(-1.256\times10^5) = -6.28\times10^6$ W
$= -6.28$ MW.

**(c)** The water gains 12.56 MW in the aquifer and loses 6.28 MW on the recharge
leg. The difference, 6.28 MW, is the net heat delivered to the surface by the
circulating fluid — half the aquifer's thermal throughput is spent reheating the
recharge water that came down cold. This is why the *net* heat output of a
hydrothermal system is much smaller than its internal circulation rate.

**(d)** The recharge leg is neither: it is dominated by *advection* of the fluid
with heat exchange to the wall rock, i.e. the Péclet regime of lesson 02-05-05
§3.7. Whether that matters depends on the flow rate: the descent takes a time
$L/v$, and if $L^2/\kappa \ll L/v$ the water equilibrates with the rock, which is
exactly what makes the recharge leg's temperature change conductive in effect.

---

## ★★7 — Plant sizing

**(a)** $1 - 298.15/493.15 = 0.3954$.

**(b)** At 40 per cent of Carnot, $\eta = 0.1582$, so thermal
$= 12/0.1582 = 75.9$ MW. At 60 per cent, $\eta = 0.2372$, thermal
$= 12/0.2372 = 50.6$ MW.

**(c)** $\dot m = \dot Q/(c_p\Delta T) = 75.9\times10^6/(4186\times160)
= 113.3$ kg s⁻¹; and $50.6\times10^6/(4186\times160) = 75.6$ kg s⁻¹.

**(d)** It governs the number of wells and the well spacing, which is usually the
dominant capital cost. A 33 per cent reduction in required flow is a 33 per cent
reduction in well count, which is why heat-exchanger and turbine optimisation
justifies its cost even though it does not change the resource.

---

## ★★8 — Magma energy budget

**(a)** $\rho c_p\Delta T = 2900\times840\times1200 = 2.923\times10^9$ J m⁻³.

**(b)** $\rho L = 2900\times4\times10^5 = 1.16\times10^9$ J m⁻³.

**(c)** With $A_{\text{latent}} = \rho L\,\partial f/\partial t$ and
$\partial f/\partial t = (\partial f/\partial T)(\partial T/\partial t)$, the heat
equation becomes

$$\rho\left(c_p + L\frac{\partial f}{\partial T}\right)\frac{\partial T}{\partial t}
= \nabla\cdot(k\nabla T) ,$$

which must be applied over the **liquidus-to-solidus interval** — the range of
temperature in which $f$ changes. Outside it $\partial f/\partial T = 0$ and the
ordinary equation applies.

**(d)** Because latent heat is not a flux into or out of the domain; it is an
internal redistribution. A model that omits it still has $\dot Q_{\text{in}}
- \dot Q_{\text{out}} = \mathrm{d}U/\mathrm{d}t$ satisfied by the *sensible* energy
bookkeeping. The error appears as a wrong $\mathrm{d}T/\mathrm{d}t$: the model
cools too fast through the crystallisation interval, so it "balances" while
violating the physics. Energy audits detect missing fluxes; they do not detect
misassigned state functions, which is why the physics must be checked separately.

---

## ★★9 — Exponentially distributed heat generation

**(a)** $k\,\mathrm{d}^2T/\mathrm{d}z^2 = -A_0e^{-z/h}$.

**(b)** Integrating once:
$\mathrm{d}T/\mathrm{d}z = (A_0h/k)e^{-z/h} + C$. With
$\mathrm{d}T/\mathrm{d}z = q_0/k$ at $z = 0$,
$C = (q_0 - A_0h)/k$, so

$$\frac{\mathrm{d}T}{\mathrm{d}z}
= \frac{A_0h}{k}e^{-z/h} + \frac{q_0 - A_0h}{k} .$$

**(c)** As $z\gg h$, $\mathrm{d}T/\mathrm{d}z \to (q_0 - A_0h)/k$, a constant, so
the geotherm becomes linear with a heat flow $q_0 - A_0h$: the **mantle heat
flow**, i.e. the surface heat flow less all the heat generated in the radiogenic
layer.

**(d)** $A_0h = 1.5\times10^{-6}\times1.2\times10^4 = 1.8\times10^{-2}$ W m⁻²
$= 18$ mW m⁻². For a surface heat flow of 65 mW m⁻² that is 28 per cent of it.

---

## ★★★10 — The adiabat through a phase transition

**(a)** The first law for a parcel with no external heat exchange but with an
internal latent term is $\mathrm{d}h = v\,\mathrm{d}P - \ell\,\mathrm{d}f$, where
$\ell$ is the specific latent heat and $f$ the transformed fraction. Writing
$\mathrm{d}h = c_p\,\mathrm{d}T + v(1-\alpha T)\,\mathrm{d}P$ and eliminating
$\mathrm{d}P$ with the lithostatic relation gives, over the transition interval
$\Delta T$ with total transformed fraction $f$,

$$c_p^{\text{eff}} = c_p + \frac{\ell f}{\Delta T} .$$

**(b)** $c_p^{\text{eff}}/c_p = 1 + \ell f/(c_p\Delta T)
= 1 + (3\times10^4\times1)/(1250\times20) = 1 + 1.2 = 2.2$.

**(c)** The adiabatic gradient $\mathrm{d}T/\mathrm{d}z = \alpha Tg/c_p^{\text{eff}}$
is *reduced* by the factor 2.2, so the adiabat becomes **flatter** — the transition
acts as a thermal buffer, exactly as latent heat does in a crystallising magma.

**(d)** A flatter segment in the temperature profile is a segment where temperature
changes little with depth, so the seismic velocity change with depth is also
suppressed — the discontinuity appears as a *gradual* velocity increase rather
than a step, even though the mineralogy changes abruptly. The observed velocity
gradient across the transition is therefore a joint constraint on the Clapeyron
slope (which sets the depth of the transition) and on the latent heat (which sets
the flatness). The accompanying signature is a comparison of the seismically
inferred discontinuity sharpness with the mineral physics: a sharp boundary in
mineralogy with a broad velocity ramp is itself evidence for a large latent heat.

---

## ★★★11 — Flashing in a separator

**(a)** For steady adiabatic flow with no shaft work, the energy equation
$\dot m(h_2-h_1) = \dot Q - \dot W_s$ gives $h_2 = h_1$: **throttling is
isenthalpic**. The temperature still changes because $h$ depends on both $T$ and
$P$: along $h = $ const, $\mathrm{d}T = -(\partial h/\partial P)_T/(\partial h/
\partial T)_P\,\mathrm{d}P$, whose sign is set by the sign of the Joule–Thomson
coefficient. For a condensing vapour the coefficient is negative, so pressure
reduction cools the fluid.

**(b)** The fluid's enthalpy is unchanged across the throttle, but the *form* of
the energy changes. At the lower pressure, the saturated vapour enthalpy $h_g$ and
saturated liquid enthalpy $h_f$ have both fallen, and a fraction $x$ of the mass
must vaporise to keep the mixture enthalpy at its original value. The energy comes
from the sensible heat of the remaining liquid, not from any external source —
which is why the liquid cools and the separator outlet is at the lower saturation
temperature.

**(c)** Using the standard steam-table relation

$$x = \frac{h_{f,1} - h_{f,2}}{h_{g,2} - h_{f,2}} ,$$

adopt from a published steam table (state which, with its edition, and cite it):
$h_{f}$ at 200 °C, $h_f$ and $h_g$ at 150 °C. Substituting the adopted values
gives $x$ of order 0.1–0.2 for this temperature drop. **The numerical answer
depends entirely on the table used, so it is not quoted here**: this problem
requires you to obtain the table from your library, record the edition, and show
your arithmetic. What is not negotiable is the structure — the separator produces
steam without adding heat, which surprises people until they see (b).

**(d)** Two assumptions: (i) the throttle is adiabatic, which fails when the
separator and pipework lose heat to their surroundings (typically a few per cent
of the enthalpy); (ii) the fluid is pure water, which fails for a geothermal brine
whose dissolved solids change the saturation enthalpies and can cause scaling.
Both errors are second-order in the flashed fraction but first-order in plant
performance, which is why the assumed steam-table values must be recorded rather
than remembered.
