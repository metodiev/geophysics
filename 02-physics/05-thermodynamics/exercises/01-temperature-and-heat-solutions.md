# Solutions — 02-05-01 Temperature, Heat, Internal Energy and Specific Heat

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. All rock properties are nominal.

---

## ★1 — Heating a cubic metre of granite

**(a)** $Q = \rho c_p V \Delta T = 2700 \times 790 \times 1 \times 100
= 2.133\times10^8$ J.

**(b)** $2.133\times10^8/3.6\times10^6 = 59.25$ kWh.

**(c)** $t = Q/P = 2.133\times10^8/5000 = 4.266\times10^4$ s $= 11.85$ h.

**(d)** It is **energy**. Part (c) required assuming (i) no losses, so 100 per
cent conversion of electrical energy into stored heat, and (ii) uniform
temperature throughout the block — which is itself false, because the block's own
thermal diffusion time at $L = 1$ m is $L^2/\kappa \approx 1.2$ Ms ≈ 14 days
(lesson 02-05-04). Heating it in 12 hours therefore gives a strong internal
temperature gradient, and "the block is warmed by 100 K" would not be true
uniformly. This mismatch between the heating time and the diffusion time is the
single most common error in storage calculations.

---

## ★2 — Saturated sandstone

**(a)** $\rho = (1-\phi)\rho_{\min} + \phi\rho_w = 0.8\times2650 + 0.2\times1000
= 2120 + 200 = 2320$ kg m⁻³.

**(b)** Volumetric mixing of heat capacity:
$\rho c_p = (1-\phi)\rho_{\min}c_{\min} + \phi\rho_w c_w
= 0.8\times2650\times790 + 0.2\times1000\times4186
= 1.6748\times10^6 + 8.372\times10^5 = 2.512\times10^6$ J m⁻³ K⁻¹.

**(c)** Dry: $0.8\times2650\times790 = 1.6748\times10^6$ J m⁻³ K⁻¹.

**(d)** Ratio $= 2.512/1.6748 = 1.500$. The density ratio is
$2320/2120 = 1.094$, which is much smaller. Heat capacity is *mass* times
*specific heat capacity*, and water's specific heat capacity is 5.3 times the
mineral's, so the water contributes $8.372\times10^5$ J m⁻³ K⁻¹ from 8 per cent
of the mass. The bulk density is a poor guide to the bulk heat capacity whenever
the phases differ in $c_p$.

---

## ★3 — $c_p$ versus $c_v$ for basalt

**(a)** $c_p - c_v = \alpha^2TK_T/\rho
= (2\times10^{-5})^2\times300\times45\times10^9/2900
= 4\times10^{-10}\times300\times4.5\times10^{10}/2900 = 1.862$ J kg⁻¹ K⁻¹.

**(b)** $1.862/840 = 2.2\times10^{-3}$, i.e. 0.22 per cent.

**(c)** The demonstration's Dulong–Petit values are 1238 (MgO), 1242 (MgSiO₃) and
1245 (SiO₂) J kg⁻¹ K⁻¹, all close to the nominal *mantle* value of ~1250, while a
room-temperature measurement of granite is ~790. The discrepancy is not an error:
Dulong–Petit is the high-temperature limit and is attained only above the Debye
temperature, which is 300–500 K for these minerals. At 300 K not all modes are
excited, so the measured value is lower. The correct statement is that
Dulong–Petit explains mantle heat capacities and *not* room-temperature crustal
ones.

---

## ★4 — Sensible and latent heat

**(a)** $\rho c_p\Delta T = 2750\times900\times1100 = 2.7225\times10^9$ J m⁻³.

**(b)** $\rho L = 2750\times3.5\times10^5 = 9.625\times10^8$ J m⁻³.

**(c)** $9.625/(27.225+9.625) = 26.1$ per cent.

**(d)** Because it is released at essentially constant temperature, it controls
the *duration* for which the body stays hot, and therefore the duration of
hydrothermal circulation, contact metamorphism and any ore-forming fluid flow
around the intrusion. A 26 per cent energy share can dominate the thermal history
because it is delivered at the highest temperature the system reaches.

---

## ★5 — Dulong–Petit for forsterite

$c_v = 3nR/M$ with $n = 7$ and $M = 0.14069$ kg mol⁻¹:

$$c_v = \frac{3\times7\times8.314\,462\,618}{0.14069}
= \frac{174.604}{0.14069} = 1241.0\ \mathrm{J\,kg^{-1}\,K^{-1}} .$$

That is within 0.7 per cent of the nominal mantle value, as expected: the
Dulong–Petit limit is $3R$ per atom, and forsterite has 20.1 g of mass per atom,
essentially the same as every other rock-forming silicate.

The comparison is expected to hold at temperatures well above the Debye
temperature, i.e. in the mantle. At 100 K the lattice modes are not fully excited
and $c_v$ is far below the limit, tending to zero as $T^3$.

---

## ★6 — Reading the demo

**(a)** $4.0832\times10^{18}$ J for a 1 km³ body, of which
$1.1600\times10^{18}$ J is latent.

**(b)** $1.2939\times10^8$ kW-years $= 129.39$ GW-years, using
1 kW-year $= 1000\ \mathrm{W}\times3.155\,76\times10^7\ \mathrm{s}
= 3.1558\times10^{10}$ J.

**(c)** $4.0832\times10^{18}/(10^4\times3.155\,76\times10^7)
= 4.0832\times10^{18}/3.155\,76\times10^{11} = 1.294\times10^7$ W
$= 12.9$ MW.

**(d)** The stored energy is a property of the magma; the power is a property of
the *path* the heat takes to escape. The same body cooling in 10⁴ yr or 10⁶ yr
delivers 12.9 MW or 0.129 MW with identical stored energy. The path is the
subject of lesson 02-05-04.

---

## ★7 — Aquifer thermal store

**(a)** $V = 10^6\ \mathrm{m^2}\times50\ \mathrm{m} = 5\times10^7$ m³.
$Q = \rho c_p V\Delta T = 2.512\times10^6\times5\times10^7\times10
= 1.256\times10^{15}$ J.

**(b)** $1.256\times10^{15}/3.6\times10^6 = 3.489\times10^8$ kWh
$= 348.9$ GWh.

**(c)** One house takes $5\ \mathrm{kW}\times8\ \mathrm{h} = 40$ kWh per day, and
over 100 days 4000 kWh $= 4\times10^3$ kWh. Number of houses
$= 3.489\times10^8/4\times10^3 = 8.72\times10^4$, i.e. about $8.7\times10^4$
houses.

**(d)** The dominant uncertainties are: (i) the recovery factor — not all the
stored heat can be recovered before the store cools below the usable
temperature, and typical values are well below 1; (ii) whether the rock is
actually saturated and whether the pore water participates thermally at the
cycling rate (frequency matters, as in lesson 02-04-04 §3.4); (iii) the thermal
losses to the confining layers, which are an $L^2/\kappa$ question with
$L = 50$ m — about 68 yr, so losses are significant over a 100-day cycle only
through the top and bottom few metres.

---

## ★8 — The crystallisation plateau

**(a)** $(\rho c_p)_{\text{eff}} = \rho c_p + \rho L/\Delta T_{\text{xtal}}$.

**(b)** $\rho c_p = 2.475\times10^6$ J m⁻³ K⁻¹ and
$\rho L = 9.625\times10^8$ J m⁻³.
For 200 K: $\rho L/200 = 4.8125\times10^6$, so
$(\rho c_p)_{\text{eff}} = 7.288\times10^6$ and the factor is **2.94**.
For 50 K: $\rho L/50 = 1.925\times10^7$, so
$(\rho c_p)_{\text{eff}} = 2.173\times10^7$ and the factor is **8.78**.

**(c)** The same latent heat is released over a smaller temperature interval, so
the heat per kelvin of cooling rises as $1/\Delta T_{\text{xtal}}$. A narrow
interval means the body absorbs almost no sensible heat while releasing the whole
latent budget, and the temperature barely moves.

**(d)** Because real crystallisation is not a single temperature: the liquidus and
solidus are separated by tens to hundreds of kelvin, the melt composition changes
continuously along the path, and the latent heat is released progressively. The
result is a *steepened* segment of the cooling curve rather than a perfectly flat
one, and the exact shape requires a thermodynamic crystallisation model, not a
single $L$.

---

## ★9 — Uncertainty in the heat content

**(a)** Assuming independence,

$$\frac{\delta Q}{Q}
= \sqrt{\left(\frac{\delta\rho}{\rho}\right)^2
+ \left(\frac{\delta c_p}{c_p}\right)^2
+ \left(\frac{\delta V}{V}\right)^2
+ \left(\frac{\delta\Delta T}{\Delta T}\right)^2} .$$

**(b)** $\sqrt{0.03^2+0.10^2+0.15^2+0.02^2}
= \sqrt{9\times10^{-4}+10^{-2}+2.25\times10^{-2}+4\times10^{-4}}
= \sqrt{3.38\times10^{-2}} = 0.1838$, i.e. **18.4 per cent**.

**(c)** The volume term dominates (15 per cent), then $c_p$ (10 per cent). The
improvement that matters most is a better *volume* estimate — a denser survey or
a better geometric model — not a better laboratory heat capacity. Note that this
is the reverse of the intuitive answer, which is usually "measure the rock
better".

---

## ★★★10 — Debye low-temperature limit

**(a)** $12\pi^4/5 = 12\times97.40909/5 = 1168.91/5 = 233.78$ ✓.

**(b)** With $n = 7$, $R = 8.314\,462\,618$ J mol⁻¹ K⁻¹, $\Theta_D = 500$ K and
$T = 50$ K:

$$c_v = 233.78\times7\times8.314\,462\,618\times(0.1)^3
= 233.78\times58.201\times10^{-3} = 13.60\ \mathrm{J\,mol^{-1}\,K^{-1}} ,$$

i.e. $13.60/0.14069 = 96.7$ J kg⁻¹ K⁻¹.

**(c)** At $T = \Theta_D/20 = 25$ K the factor $(T/\Theta_D)^3$ is eight times
smaller: $c_v = 13.60/8 = 1.700$ J mol⁻¹ K⁻¹ $= 12.1$ J kg⁻¹ K⁻¹. The ratio of
the two values is exactly 8, which verifies the $T^3$ scaling.

**(d)** A single Debye temperature assumes one characteristic vibrational
spectrum. Forsterite has 28 atoms in the primitive cell, hence 84 phonon branches
with a wide range of frequencies, from acoustic modes with low $\Theta_D$ to
high-frequency optic modes with much larger effective $\Theta_D$. There is no
single $\Theta_D$ that fits the whole temperature range: a value fitted above
100 K underestimates $c_v$ below 50 K, and vice versa. A real measurement would
show a $c_v$ that follows a $T^3$ law only at very low temperature, then rises
more slowly than a single-$T^3$ extrapolation would predict. **No numerical
measured value is quoted here**, because none has been verified from a source in
this repository.

---

## ★★★11 — Cooling-curve budget of a sill

**(a)** Per unit area of a 100 m sill, the mass column is
$\rho\times100\ \mathrm{m} = 2.75\times10^5$ kg m⁻². Sensible heat over 1100 K:
$2.75\times10^5\times900\times1100 = 2.7225\times10^{11}$ J m⁻². Latent:
$2.75\times10^5\times3.5\times10^5 = 9.625\times10^{10}$ J m⁻². Total
$= 3.685\times10^{11}$ J m⁻².

**(b)** At 100 W m⁻² from **both** faces the removal rate is 200 W m⁻², so
$t = 3.685\times10^{11}/200 = 1.843\times10^9$ s $= 58.4$ yr.

**(c)** The latent part is 26.1 per cent of the total (★4(c)), so the plateau
occupies $0.261\times58.4 = 15.3$ yr *if* the latent heat were spread uniformly.
But it is released inside a 100 K interval, so the plateau is the interval in
which the body is crystallising, and the fraction of the cooling *time* is the
latent share by construction of the constant-flux assumption: 26 per cent of the
time is spent releasing latent heat, i.e. **15.3 yr**, against 43.1 yr of sensible
cooling.

**(d)** The most severe assumption is the constant 100 W m⁻² flux at both faces.
As the sill cools, the gradient driving the flux falls, so the flux decreases and
the cooling slows dramatically — the Fourier number problem of lesson 02-05-04.
The real cooling curve therefore has a long tail, and the time to reach the
ambient temperature is closer to $L^2/\kappa$ (≈ 27 400 yr for $L = 1$ km scaled
to 100 m as ≈ 274 yr) than to the 58 yr computed here. The latent plateau, by
contrast, is *at* the temperature where the magma is, when the flux is still
large, so it is shorter than the constant-flux estimate suggests. Both corrections
push in the same direction: a shorter plateau on a much longer total cooling
curve.
