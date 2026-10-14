# Solutions — 02-05-07 Thermodynamic Phase Equilibria and Mantle Mineralogy

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Pressures at the CMB, ICB and centre are adopted
> model values; slopes and deep temperatures are nominal.

---

## ★1 — A melting transition

**(a)** $\Delta S = L/T_m = 6\times10^5/2000 = 300$ J kg⁻¹ K⁻¹.

**(b)** $\mathrm{d}P/\mathrm{d}T = \Delta S/\Delta V
= 300/3\times10^{-6} = 1.0\times10^8$ Pa K⁻¹ $= 100$ MPa K⁻¹.
$\mathrm{d}T/\mathrm{d}P = 1/(1.0\times10^8) = 1.0\times10^{-8}$ K Pa⁻¹
$= \mathbf{10}$ K GPa⁻¹.

**(c)** $\Delta V > 0$ means the liquid occupies more volume than the solid — the
usual case, because melting destroys long-range order. With $\Delta S > 0$ as well,
$\mathrm{d}T/\mathrm{d}P = \Delta V/\Delta S > 0$: pressure raises the melting
temperature, because the denser (solid) phase is favoured by pressure and must be
heated further to melt.

**(d)** With $\Delta V < 0$ — as for ice — the sign flips and pressure *lowers* the
melting temperature, by the same formula.

---

## ★2 — Ice

**(a)** $\Delta v = 1/\rho_{\text{water}} - 1/\rho_{\text{ice}}
= 1/1000 - 1/917 = 1.0\times10^{-3} - 1.090\,51\times10^{-3}
= -9.0513\times10^{-5}$ m³ kg⁻¹.

**(b)** $\Delta s = 3.34\times10^5/273.15 = 1222.77$ J kg⁻¹ K⁻¹;
$\mathrm{d}T/\mathrm{d}P = \Delta v/\Delta s = -9.0513\times10^{-5}/1222.77
= -7.402\times10^{-8}$ K Pa⁻¹ $= \mathbf{-0.0740}$ K MPa⁻¹.

**(c)** The measured pressure-melting rate of ice is about −0.074 K MPa⁻¹
(equivalently, about 0.74 K per 100 bar). The agreement is exact to the digits
computed, which is the point: the formula reproduces a measured number from two
other measured numbers with no fitting.

**(d)** Because for almost every silicate — and for water's own vapour transition —
the liquid is *less* dense than the solid, so $\Delta v > 0$ and pressure raises
the melting point. Ice is the exception, not the rule, and the sign of
$\mathrm{d}T/\mathrm{d}P$ is decided entirely by the sign of $\Delta v$.

---

## ★3 — Entropy change of the 410 km transition

**(a)** From $\gamma = \mathrm{d}P/\mathrm{d}T = \Delta S/\Delta V$,
$\Delta S = \gamma\Delta V = 2.5\times10^6 \times (-0.5\times10^{-6})
= \mathbf{-1.25}$ J mol⁻¹ K⁻¹.

**(b)** $L = T\Delta S = 1900\times(-1.25) = -2375$ J mol⁻¹, i.e. the
*high-pressure* side releases 2.4 kJ mol⁻¹ on transforming.

**(c)** A negative $\Delta S$ means the product phase has *lower* entropy — fewer or
less accessible microscopic states. That is the expected behaviour for a
transition to a more closely packed structure with higher cation coordination,
fewer structural vacancies and a stiffer, higher-frequency vibrational spectrum. So
the sign is not merely permitted; it is what a crystallographic expectation
predicts.

**(d)** Because both quantities in $\Delta S = \gamma\Delta V$ come from
independent measurements: $\gamma$ from the seismically observed depth change of
the boundary with temperature (or from laboratory bracketing), and $\Delta V$ from
density or unit-cell measurements. Nothing was assumed to obtain the sign; the
sign is a *consequence*, and that is what makes this a consistency check rather
than a fit.

---

## ★4 — Pressure at 410 km

$P = \rho g z = 3400\times9.806\,65\times4.10\times10^5 = 1.3670\times10^{10}$ Pa
$= \mathbf{13.67}$ GPa.

The commonly quoted 13.5 GPa is 1.3 per cent lower. The estimate is imperfect
because (i) the density is not constant with depth — it increases from ~3300 to
~3800 kg m⁻³ across the upper mantle; (ii) $g$ decreases with depth as the mantle
above loses its gravitational pull, from 9.81 to about 9.8 m s⁻² at 410 km; and
(iii) the phase boundary lies at the pressure where the *geotherm* crosses the
equilibrium curve, not at a fixed depth. The calculation's purpose is to establish
that the transition sits at a pressure of order 10 GPa, which is what the mineral
physics requires; it is not a substitute for PREM.

---

## ★★5 — Depth shifts

**(a)** $\Delta z = \gamma\Delta T/(\rho g)$.

**(b)** $\Delta z = 3\times10^6\times200/(3400\times9.806\,65)
= 6\times10^8/33\,342.6 = 1.7995\times10^4$ m $= \mathbf{+18.0}$ km for
$+200$ K, and $-\mathbf{18.0}$ km for $-200$ K.

**(c)** $\Delta z = -3\times10^6\times200/(4000\times9.9)
= -6\times10^8/39\,600 = -1.5152\times10^4$ m $= \mathbf{-15.2}$ km for
$+200$ K, and $+15.2$ km for $-200$ K.

**(d)** For the same $+200$ K anomaly the 410 deepens by 18.0 km and the 660
shallows by 15.2 km, so the transition zone *thickens* by 33.2 km. In a cold slab
the reverse happens and the transition zone thins. A seismologist would measure
the arrival times of converted phases (P-to-S from the 410 and the 660) and invert
them for the two boundary depths; the difference of the two depths is the
measurement, and it is more robust than either depth alone because the shallow
crustal and station corrections cancel to first order.

---

## ★★6 — The core adiabat

**(a)** $\mathrm{d}T/\mathrm{d}P|_{\text{ad}} = \alpha T/(\rho c_p)$.

**(b)** $1.2\times10^{-5}\times4500 = 0.054$;
$11\,500\times700 = 8.05\times10^6$;
$\mathrm{d}T/\mathrm{d}P = 0.054/8.05\times10^6 = 6.7081\times10^{-9}$ K Pa⁻¹
$= \mathbf{6.708}$ K GPa⁻¹.

**(c)** $\Delta P = 329 - 135 = 194$ GPa, so
$\Delta T = 6.708\times194 = \mathbf{1301}$ K.

**(d)** A stably stratified layer conducts heat instead of convecting it, and its
temperature gradient would be set by the heat flux and conductivity rather than by
the adiabat — in the extreme, a layer could be nearly isothermal, making its
gradient much smaller than 6.7 K GPa⁻¹. That matters because the inner core's
solidity depends on the comparison between the *local* gradient and the melting
curve: a smaller gradient means the adiabat falls further below the melting curve
at depth and the inner core is *more* strongly favoured. It also means the ICB
temperature inferred from an assumed adiabat would be wrong, which propagates into
every estimate of the core's thermal history and of the power available to the
dynamo.

---

## ★★7 — The required melting slope

**(a)** The adiabat reaches
$T_{\text{ad}}(P_{\text{ICB}}) = 4000 + 1301 = 5301$ K. Requiring
$T_m(P_{\text{ICB}}) = T_{\text{ad}}(P_{\text{ICB}})$ with
$T_m(P_{\text{CMB}}) = 3600$ K:

$$s_m = \frac{5301 - 3600}{194} = \mathbf{8.770}\ \mathrm{K\,GPa^{-1}} .$$

**(b)** Against $s_{\text{ad}} = 6.708$ K GPa⁻¹, the ratio is 1.307.

**(c)** The inner core exists if and only if $s_m > s_{\text{ad}}$: only then does
the melting curve gain on the adiabat as pressure rises, so that descending
material crosses from the liquid side to the solid side. If $s_m < s_{\text{ad}}$
the inner core would be molten all the way to the centre, however cold the CMB is.

**(d)** It constrains the *difference* between the melting slope and the adiabatic
slope, and therefore the combination $\Delta V_{\text{melt}}/\Delta S_{\text{melt}}$
of the core material against $\alpha/(\rho c_p)$. Since the latter is calculable
from the core's equation of state, the existence and radius of the inner core
become a constraint on the melting properties and the light-element content of the
outer core — which is why the inner core is central to core-composition debates
rather than a curiosity.

---

## ★★8 — Reading the demo

**(a)** Adiabatic slope 5.590 K GPa⁻¹; required melting slope 7.652 K GPa⁻¹;
ratio 1.369.

**(b)**

| Location | $P$ (GPa) | $T_{\text{ad}}$ (K) | $T_m$ (K) | $T_m - T_{\text{ad}}$ (K) | State |
|---|---|---|---|---|---|
| CMB | 135.0 | 4000.0 | 3600.0 | −400.0 | liquid |
| Mid outer core | 232.0 | 4542.2 | 4342.2 | −200.0 | liquid |
| ICB | 329.0 | 5084.5 | 5084.5 | 0.0 | boundary |
| Centre | 364.0 | 5280.1 | 5352.3 | +72.2 | solid |

**(c)** $5280.1 - 4000.0 = \mathbf{1280}$ K.

**(d)** The margin is only 72 K. Since the individual uncertainties on the CMB
temperature, the adiabatic slope and the melting slope are each comparable to or
larger than 72 K, the *numbers* in the table are not defensible. What is
defensible is the ordering: $s_m > s_{\text{ad}}$, which is required for a solid
inner core to exist at all, and which the observation of a solid inner core
therefore establishes. The honest way to report the table is as an illustration of
a mechanism, with the margin itself quoted as evidence that the mechanism is only
just satisfied.

---

## ★★9 — Decompression melting

**(a)** Lithostatic gradient $\rho g = 0.0324$ GPa km⁻¹ (33 MPa km⁻¹); mantle
adiabat 0.4 K km⁻¹; dry peridotite solidus 110–135 K GPa⁻¹, i.e.
$110\times0.0324 = 3.56$ to $135\times0.0324 = 4.37$ K km⁻¹.

**(b)** Because the criterion is whether the adiabat, followed upward, *crosses*
the solidus. That depends only on which is steeper: the solidus rises with depth
about ten times faster than the adiabat, so a rising parcel gains ~4 K of
solidus temperature per kilometre of ascent while losing only 0.4 K of its own, and
the gap closes at a rate of ~3.6 K km⁻¹. Absolute values set *where* the crossing
is; the relative slope decides *whether* it happens at all.

**(c)** The model requires

$$T_s(65\ \mathrm{km}) = 1573 + 0.4\times65 = \mathbf{1599}\ \mathrm{K}
\quad\text{at}\quad P = 0.0324\times65 = \mathbf{2.11}\ \mathrm{GPa} .$$

**(d)** Because melting is a comparison of the parcel's temperature with the
solidus *at the same pressure*, not with its own starting temperature. Along the
adiabat the parcel cools by 0.4 K per kilometre of ascent (~26 K over 65 km), while
the solidus at that pressure falls by ~4 K km⁻¹ (~260 K). The parcel's temperature
falls, but the temperature at which it would melt falls ten times faster, so it
passes from subsolidus to super-solidus. This is why melting correlates with
upwelling rate and potential temperature rather than with the absolute
temperature of the mantle.

---

## ★★★10 — Latent heat of inner-core growth

**(a)** $V = \frac43\pi r^3 = \frac43\pi(1.221\times10^6)^3
= 7.6249\times10^{18}$ m³; $M = \rho V = 12\,800\times7.6249\times10^{18}
= 9.7599\times10^{22}$ kg.

**(b)** With $L = 2.5\times10^5$ J kg⁻¹,
$Q = LM = 2.4\times10^{28}$ J approximately (the demo prints
2.4400 × 10²⁸ J). With an adopted $T = 5200$ K,
$\Delta S = Q/T = 4.6923\times10^{24}$ J K⁻¹. **Both $L$ and $T$ are nominal**, so
this is an order-of-magnitude figure.

**(c)** $\mathrm{d}M/\mathrm{d}t = 4\pi r^2\rho v$ with $v = 0.5$ mm yr⁻¹
$= 1.5844\times10^{-11}$ m s⁻¹:
$4\pi\times1.4908\times10^{12}\times12\,800\times1.5844\times10^{-11}
= 3.7994\times10^6$ kg s⁻¹, so $P = L\,\mathrm{d}M/\mathrm{d}t
= 9.50\times10^{11}$ W $= \mathbf{0.95}$ TW. For 1.0 mm yr⁻¹ the values double to
$\mathrm{d}M/\mathrm{d}t = 7.599\times10^6$ kg s⁻¹ and $P = \mathbf{1.90}$ TW.

**(d)** The growth rate is not observable directly because the inner core is
buried under 2900 km of liquid iron and its growth is ~1 mm yr⁻¹ — five orders of
magnitude below any resolvable change over a human lifetime. It is constrained
indirectly by: (i) matching the observed present-day geomagnetic field and its
secular variation with dynamo models, which require a specified buoyancy flux;
(ii) matching the observed CMB heat flux and the mantle's thermal evolution;
(iii) the seismic structure of the inner core, including the depth extent of
anisotropy and any layering; and (iv) matching the palaeomagnetic record of
geomagnetic behaviour. Every one of those is model-dependent, which is why
published growth rates span roughly 0.3–1.5 mm yr⁻¹ and the resulting power spans
roughly 0.5–3 TW. **No single value should be quoted as measured.**

---

## ★★★11 — Phase rule and disequilibrium

**(a)** $F = C - P + 2$, where $C$ is the number of independent components, $P$ the
number of phases present, and the 2 accounts for the two intensive variables that
must be specified independently (conventionally $P$ and $T$) for a system with no
other work coordinates. $F$ is the number of remaining degrees of freedom — the
number of additional intensive variables that must be fixed to pin the state down.

**(b)** The system CaO–MgO–Al₂O₃–SiO₂ has $C = 4$. At a point where
$(Mg,Fe)_2SiO_4$ (treated as one component's phase) and melt coexist, $P = 2$, so
$F = 4 - 2 + 2 = 4$. In the mantle, $P$ and $T$ are imposed by the geotherm, which
uses two of the four; the remaining two are the compositions of the two phases.
That is why the composition of a melt in equilibrium with olivine is *not* free
but is fixed once $P$ and $T$ are given — which is the thermodynamic basis of
geothermobarometry.

**(c)** Because of the Clapeyron slopes. The 410 has a slope of ±2–3 MPa K⁻¹, so
across a boundary width of a few kilometres the equilibrium temperature varies by
tens of kelvin — a narrow, sharp transition that seismology resolves as a
discontinuity. The 520 km feature has a slope near zero, which means that over a
considerable depth range the equilibrium pressure is almost independent of
temperature, so small temperature and composition variations smear the transition
over tens of kilometres. A near-zero Clapeyron slope produces a diffuse
discontinuity; the seismically observed diffuseness of the 520 is therefore itself
evidence for a small slope.

**(d)** A phase transition requires nucleation and growth, and at low temperature
the cation diffusion needed to restructure the lattice is extremely slow. If the
slab descends faster than the transition can proceed — i.e. if the descent time is
shorter than the relaxation time of the transformation — olivine can persist as a
metastable phase well below its equilibrium depth. The relaxation time is
thermally activated, so cold slabs are the most likely hosts. The seismic
signature would be a *missing* or greatly weakened 410 km discontinuity inside the
slab, with the transformation instead appearing deeper and spread over a larger
depth interval than in the surrounding mantle. The accompanying velocity anomaly
also depends on the densities and elastic moduli of the two phases at those
conditions, and **this repository does not assert a sign for it**; the robust,
model-independent statement is the depressed and weakened discontinuity itself.
Detecting it requires resolving a boundary at 400–500 km depth inside a
subduction zone, where the slab is only tens of kilometres thick.

---

## ★★★12 — A thermodynamic consistency check

**(a)** Coexistence requires $\mu_\alpha(P,T) = \mu_\beta(P,T)$. Differentiating
along the coexistence curve and using
$\mathrm{d}\mu = -\bar s\,\mathrm{d}T + \bar v\,\mathrm{d}P$ for each phase gives
$-\bar s_\alpha\mathrm{d}T + \bar v_\alpha\mathrm{d}P
= -\bar s_\beta\mathrm{d}T + \bar v_\beta\mathrm{d}P$, hence
$\mathrm{d}P/\mathrm{d}T = \Delta S/\Delta V$.

**(b)** With $\gamma > 0$ and $\Delta V < 0$,
$\Delta S = \gamma\Delta V < 0$. For a densification this is physically plausible:
the denser phase generally has higher coordination, a stiffer and higher-frequency
vibrational spectrum, and fewer configurational states, all of which reduce
entropy. A positive $\Delta S$ with $\Delta V < 0$ would require the denser phase
to be *more* disordered, which is possible but needs a specific structural reason
(a disordering transition, or a decomposition into two phases — which is exactly
the case at 660 km).

**(c)** $\Delta S = \gamma\Delta V$, so at fixed $\gamma$ a factor of 2 in
$\Delta V$ is a factor of 2 in $\Delta S$ (and hence in the latent heat). What
would settle it is a direct measurement of the volume change: either unit-cell
volume measurements of both phases at the relevant pressure from a diamond-anvil
cell, or a density measurement precise enough to resolve the two phases. Neither
is easy at 13.5 GPa, which is why the factor-of-two possibility is real.

**(d)** The depth is measured by seismology to a few kilometres, whereas the slope
requires knowing the temperature change as well as the depth change — and the
temperature change inside the mantle is inferred, not measured, to within tens of
kelvin. So converting an observed depth anomaly into a temperature anomaly
requires dividing by a slope that is uncertain by tens of per cent, which makes
the inferred temperature uncertain by at least that much. The consequence for
practice is that a discontinuity depth should be reported as a depth anomaly in
kilometres, with the temperature interpretation offered separately and with the
slope's uncertainty propagated. Quoting "the mantle here is 150 K hotter" from a
7 km 410 anomaly without stating the slope and its uncertainty would be a
two-digit answer resting on a one-digit number.
