# Solutions — 02-05-05 Convection, Radiation and Combined Heat Transfer

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — A convecting magma chamber

**(a)** $\mathrm{Ra} = \rho g\alpha\Delta T d^3/(\kappa\eta)
= 2600\times9.806\,65\times5\times10^{-5}\times300\times(2\times10^3)^3
/(10^{-6}\times10^4)$.
Numerator: $25497.3\times5\times10^{-5} = 1.274\,87$;
$1.274\,87\times300 = 382.46$; $382.46\times8\times10^9 = 3.0597\times10^{12}$.
Denominator: $10^{-2}$. So $\mathrm{Ra} = 3.06\times10^{14}$.

**(b)** $3.06\times10^{14}/10^3 = 3.06\times10^{11}$.

**(c)** $(3.06\times10^{14})^{1/3} = 6.738\times10^4$, so
$\mathrm{Nu} = 0.1\times6.738\times10^4 = \mathbf{6738}$.

**(d)** Convective, by eleven orders of magnitude. With $\eta = 10^8$ Pa s the
Rayleigh number falls to $3.06\times10^{10}$ — still seven orders above the
critical value, so the answer does not change. Only a viscosity near
$10^{14}$ Pa s, i.e. a solid-state crystal-mush rheology, would make the chamber
marginally stable.

---

## ★2 — Radiation at 500 K

**(a)** $F = 5.670\,374\,419\times10^{-8}\times500^4 = 3544.0$ W m⁻².
$h_{\text{rad}} = 4\sigma T^3 = 4\times5.670\,374\,419\times10^{-8}\times1.25
\times10^8 = 28.35$ W m⁻² K⁻¹.

**(b)** $F$ is the flux (W m⁻²); $h_{\text{rad}}$ is the linearised
heat-transfer coefficient (W m⁻² K⁻¹), the derivative of the flux with respect to
temperature.

**(c)** $28.35 > 15$ W m⁻² K⁻¹, so radiation dominates at 500 K — but only by a
factor of 1.9, which is why 500 K is roughly the crossover between the two modes
for a surface in air.

**(d)** Assumptions: (i) the emitter is a blackbody, i.e. it absorbs all incident
radiation at every wavelength, and (ii) it is optically thick and in local
thermodynamic equilibrium so that a temperature describes its emission. A real rock
surface has $\epsilon$ of 0.7–0.95 depending on mineralogy, roughness and
wavelength, so its flux is 5–30 per cent lower than $\sigma T^4$; and a surface
covered by an optically thin gas layer requires radiative transfer rather than a
surface flux.

---

## ★3 — Effective radiating temperature

**(a)** $T_e = \left(S(1-a)/(4\sigma)\right)^{1/4}$; the factor 4 is the ratio of
the sphere's surface area to its cross-sectional area.

**(b)** $a = 0.20$: absorbed $= 1361\times0.80/4 = 272.2$ W m⁻²,
$T_e = 263.22$ K. $a = 0.25$: 255.19 W m⁻², $T_e = 259.01$ K.
$a = 0.30$: 238.18 W m⁻², $T_e = 254.58$ K. $a = 0.35$: 221.16 W m⁻²,
$T_e = 249.90$ K.

**(c)** $259.01 - 249.90 = 9.11$ K for a 0.10 change in albedo.

**(d)** Because a 0.10 albedo change of 9.1 K corresponds to an absorbed-flux
change of 34 W m⁻², which is four hundred times the geothermal flux of
0.087 W m⁻². The sensitivity $\mathrm{d}T_e/\mathrm{d}S = T_e/(4S) = 0.0468$ K per
W m⁻² applies to both equivalently, but one of them can change by tens of
W m⁻² and the other by fractions of one.

---

## ★4 — Wien's law

**(a)** $b = hc/(xk_B)
= (6.626\,070\,15\times10^{-34}\times2.997\,924\,58\times10^8)
/(4.965\,114\times1.380\,649\times10^{-23})$.
Numerator $= 1.986\,446\times10^{-25}$; denominator $= 6.855\,25\times10^{-23}$;
$b = 2.897\,77\times10^{-3}$ m K.

**(b)** $1000$ K → $2.898\times10^{-6}$ m $= 2.898$ µm; 288 K →
$1.0062\times10^{-5}$ m $= 10.06$ µm; 5772 K → $5.020\times10^{-7}$ m
$= 502$ nm.

**(c)** 2.898 µm: near the boundary between near-infrared and thermal infrared.
10.06 µm: thermal infrared. 502 nm: visible (green).

**(d)** Because the Sun is 22 times hotter, and $\lambda_{\max}\propto1/T$, so the
Sun's peak is 20 times shorter in wavelength than the Earth's and the two spectra
overlap only in the wings. The consequence is that a gas can be simultaneously
transparent in the visible and opaque in the infrared — which is the greenhouse
effect, and which also means no single grey opacity can represent the atmosphere.

---

## ★★5 — Reading the demo

**(a)** Whole mantle Ra $5.920\times10^7$, Nu 38.97. Upper mantle
$3.629\times10^6$, 15.37. Water 1 m layer $1.369\times10^{11}$, 515.35. Lava lake
10 m $3.825\times10^9$, 156.38.

**(b)** $q_{\text{cond}} = 3.4483\times10^{-3}$ W m⁻²;
$q_{\text{conv}} = 1.3439\times10^{-1}$ W m⁻² $= 134.4$ mW m⁻².

**(c)** It is 1.5 times the observed mean. That is *agreement to within a factor of
2*, which is what a one-third-power scaling with an empirical prefactor and
order-of-magnitude inputs can deliver. Quoting it as "the mantle heat flow is
134 mW m⁻²" would be wrong on two counts: it is a model output, and the model's
inputs are nominal.

**(d)** (i) Temperature-dependent viscosity: the real mantle's $\eta$ varies by
orders of magnitude, which raises the effective exponent above 1/3 and changes the
prefactor. (ii) Internal heating: radioactive decay generates heat within the
convecting layer, which changes the boundary-layer structure and the scaling.
(iii) Phase transitions: the 410 and 660 absorb or release latent heat and change
the buoyancy, adding terms the Boussinesq system does not contain.

---

## ★★6 — Lava lake

**(a)** $\mathrm{Ra} = 2600\times9.806\,65\times5\times10^{-5}\times300
\times125/(10^{-6}\times100)$.
Numerator: $382.46\times125 = 47\,807$; denominator $10^{-4}$;
$\mathrm{Ra} = 4.78\times10^8$. $\mathrm{Nu} = 0.1\times(4.78\times10^8)^{1/3}
= 0.1\times781.9 = 78.2$.

**(b)** $q_{\text{cond}} = k\Delta T/d = 1.8\times300/5 = 108$ W m⁻²
(adopting $k = 1.8$ W m⁻¹ K⁻¹ for basaltic melt);
$q_{\text{conv}} = 78.2\times108 = 8.45\times10^3$ W m⁻².

**(c)** $\sigma T^4 = 5.670\,374\,419\times10^{-8}\times1400^4
= 2.178\times10^5$ W m⁻².

**(d)** Radiation 2.18 × 10⁵ > convection 8.45 × 10³ > conduction 1.08 × 10²
W m⁻². Radiation controls the lake's heat loss by a factor of 26 over convection,
which is why a lava lake's surface crusts only when the crust itself suppresses
radiation, and why the radiative cooling rate is the quantity that satellite
thermal monitoring measures.

---

## ★★7 — Groundwater and heat flow

**(a)** $\mathrm{Pe} = vL/\kappa$ with $v$ the fluid velocity, $L$ the length scale
over which the temperature changes, and $\kappa$ the thermal diffusivity of the
saturated medium. It measures advective transport relative to conductive.

**(b)** $v = \kappa/L = 1.157\times10^{-6}/2000 = 5.785\times10^{-10}$ m s⁻¹
$= 5.785\times10^{-10}\times3.155\,76\times10^7 = 1.826\times10^{-2}$ m yr⁻¹
$= 1.8$ cm yr⁻¹.

**(c)** $Pe = (0.05/3.155\,76\times10^7)\times2000/1.157\times10^{-6}
= 1.5847\times10^{-9}\times1.7286\times10^9 = 2.74$.

**(d)** Because advection *replaces* the conductive mechanism rather than adding to
it over the same path. The fluid carries enthalpy $\rho c_p v\Delta T$ per unit
area per unit time, which can be orders of magnitude larger than $k\Delta T/L$; the
rock's conductivity is unchanged, but the heat no longer has to pass through the
rock by conduction because it is being carried by the water filling the pores. In
a fault zone the relevant $k$ is not the bulk conductivity of the gouge but the
effective thermal conductivity of a medium being swept by fluid.

---

## ★★8 — Reading the demo

**(a)** $b = 2.897\,772\times10^{-3}$ m K.

**(b)** 3.651 cm yr⁻¹.

**(c)** Quote the velocity in **cm yr⁻¹**, because a hydrogeologist thinks in
groundwater velocities of that order and the comparison is immediate: "if your
water moves faster than a few centimetres a year, advection dominates over a
kilometre". Quoting $1.157\times10^{-9}$ m s⁻¹ would be technically correct and
communicatively useless.

**(d)** Because in the mantle there is no externally imposed velocity — the flow is
generated by the buoyancy itself, so $v$ is an output rather than an input. The
Rayleigh number is the correct criterion because it compares driving to damping
without needing a velocity, and it predicts whether convection begins at all.

---

## ★★9 — A cooling basalt surface

**(a)** $\sigma T^4 = 5.670\,374\,419\times10^{-8}\times1100^4
= 8.303\times10^4$ W m⁻².

**(b)** With $\epsilon = 0.9$: $7.473\times10^4$ W m⁻², a 10 per cent reduction.

**(c)** $h\Delta T = 12\times810 = 9.72\times10^3$ W m⁻².

**(d)** Radiation 8.30 × 10⁴ (89.5 per cent), convection 9.72 × 10³
(10.5 per cent), conduction through the flow negligible. At 600 K: radiation
$= 5.670\,374\,419\times10^{-8}\times600^4 = 7.35\times10^3$ W m⁻²; convection
$= 12\times310 = 3.72\times10^3$ W m⁻². Radiation still leads but only by a factor
of 2.0, so the ranking is preserved while the margin shrinks — and below about
500 K, convection and conduction take over.

---

## ★★★10 — Boundary-layer scaling

**(a)** Set the local Rayleigh number of the boundary layer equal to its critical
value: $\rho g\alpha\Delta T\delta^3/(\kappa\eta) \sim \mathrm{Ra}_c$. Then
$\delta^3 \sim \mathrm{Ra}_c\kappa\eta/(\rho g\alpha\Delta T)$. Since
$\mathrm{Ra} = \rho g\alpha\Delta T d^3/(\kappa\eta)$,
$\kappa\eta/(\rho g\alpha\Delta T) = d^3/\mathrm{Ra}$, so
$\delta^3 \sim \mathrm{Ra}_c d^3/\mathrm{Ra}$, i.e.
$\delta \sim d\left(\mathrm{Ra}_c/\mathrm{Ra}\right)^{1/3}
\propto d\,\mathrm{Ra}^{-1/3}$ for fixed $\mathrm{Ra}_c$.

**(b)** All the heat crosses the boundary layers by conduction, so
$q \sim k\Delta T/\delta$; the conductive baseline is $q_{\text{cond}} \sim
k\Delta T/d$; hence $\mathrm{Nu} = q/q_{\text{cond}} \sim d/\delta \sim
\mathrm{Ra}^{1/3}$, and the empirical prefactor is 0.1.

**(c)** $(5.920\times10^7)^{1/3} = 389.7$, so
$\delta = d\,\mathrm{Ra}^{-1/3} = 2.9\times10^6/389.7 = 7.44\times10^3$ m
$= 7.4$ km. Then $q_{\text{conv}} = k\Delta T/\delta
= 4\times2500/7.44\times10^3 = 1.344$ W m⁻² $= 134.4$ mW m⁻², which is exactly
the demo's value — as it must be, since the demo computed $\mathrm{Nu}k\Delta T/d$
and $d/\delta$ is the same ratio.

**(d)** Four assumptions and their failures:
1. *Constant viscosity.* The mantle's $\eta$ falls by orders of magnitude from the
   lithosphere to the deep mantle, so the cold, stiff upper boundary layer is much
   thicker than the scaling assumes. This makes the real flux **smaller** than
   predicted — the lithosphere is an effective lid.
2. *No internal heating.* The mantle generates a large fraction of its heat
   internally, which thickens the interior's effective thermal boundary layers and
   is associated with a different (lower-power) scaling. Makes the flux
   **smaller** for the same $\Delta T$ but also changes the temperature profile.
3. *No phase changes.* The 410 and 660 transitions release and absorb latent heat
   and add buoyancy terms; they locally flatten the adiabat and change the
   effective driving temperature. Direction **ambiguous** without a full model.
4. *Infinite Prandtl number and no inertia.* This one holds for the mantle, which
   is the approximation's success rather than its failure.

---

## ★★★11 — A one-layer atmosphere

**(a)** Radiative balance at the top: the planet absorbs $F$ and the atmosphere
emits $F$ to space at its own temperature $T_a$, so $\sigma T_a^4 = F$. At the
surface: the surface emits $\sigma T_s^4$ upward, receives $\sigma T_a^4$ back
from the atmosphere (emissivity 1 in the infrared, so the atmosphere emits both up
and down), and must balance: $\sigma T_s^4 = 2\sigma T_a^4$. Hence
$T_s^4 = 2T_a^4$ and $T_s = 2^{1/4}T_e$.

**(b)** $T_s = 2^{1/4}\times255 = 1.1892\times255 = 303.2$ K.

**(c)** Because the real atmosphere is not a single isothermal layer with unit
infrared emissivity. Its absorptivity varies strongly with wavelength and height,
so the effective radiating level is a weighted average over the emission spectrum
and only part of the surface's infrared emission is returned. The real greenhouse
warming over the $T_e = 255$ K baseline is 33 K rather than 48 K, which is a
measure of how much of the idealisation is wrong.

**(d)** Because a single grey emissivity would have to be the same in the visible
(where the atmosphere is nearly transparent) and in the infrared (where it is
strongly absorbing). A grey atmosphere with $\epsilon \approx 1$ in the infrared
would also block the incoming sunlight, and one with $\epsilon \approx 0$ in the
infrared would produce no greenhouse effect. Only a wavelength-dependent opacity
can be transparent to the short-wave and opaque to the long-wave, which is exactly
the physics identified by Wien's law in ★4.
