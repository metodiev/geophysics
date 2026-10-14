# Solutions — 02-05-03 Second Law, Entropy and Irreversibility

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — The same energy at two temperatures

**(a)** $\Delta S = Q/T$: at 350 K, $10^6/350 = 2857.1$ J K⁻¹; at 1200 K,
$10^6/1200 = 833.3$ J K⁻¹.

**(b)** The 350 K delivery. Its entropy change is 3.43 times larger, and entropy
change is the quantity that measures how much the energy has been degraded: energy
delivered at low temperature is further from a state that can do work.

**(c)** A reversible engine between 350 K and 280 K converts
$\eta = 1 - 280/350 = 0.2000$ of the heat, i.e. $W_{\max} = 0.2\times10^6
= 2\times10^5$ J.

**(d)** Because only the fraction $1 - T_c/T_h$ of the heat can be converted; the
rest must be rejected to the cold reservoir, and the second law forbids
converting it all.

---

## ★2 — Entropy production in conduction

**(a)** $\sigma = q(1/T_c - 1/T_h) = 0.060\times(1/280 - 1/1200)
= 0.060\times(3.5714\times10^{-3} - 8.3333\times10^{-4})
= 0.060\times2.7381\times10^{-3} = 1.643\times10^{-4}$ W m⁻² K⁻¹.

**(b)** At 800 K: $0.060\times(3.5714\times10^{-3} - 1.25\times10^{-3})
= 0.060\times2.3214\times10^{-3} = 1.393\times10^{-4}$ W m⁻² K⁻¹. *Smaller*
than (a), because the temperature drop is smaller for the same flux.

**(c)** With the heat flowing from 280 K to 1200 K the expression becomes
$q(1/T_h - 1/T_c) = -1.643\times10^{-4}$ W m⁻² K⁻¹, negative. A negative entropy
production is impossible for an isolated system, which is the formal statement
that the reversed process cannot occur: heat does not flow from cold to hot.

**(d)** $1.643\times10^{-4}\times5.10\times10^{14}
= 8.38\times10^{10}$ W K⁻¹ globally.

---

## ★3 — Carnot efficiency for a geothermal plant

**(a)** $1 - 293.15/453.15 = 0.3531$.

**(b)** $0.09/0.3531 = 25.5$ per cent of the bound.

**(c)** $1 - 278.15/453.15 = 0.3862$, a gain of 3.3 percentage points, i.e. a 9.4
per cent relative improvement in the ceiling. Cooling the sink far below ambient
requires refrigeration, which consumes work; the net gain is usually negative
unless a natural cold sink (a river, deep seawater, or a cold climate) is
available. So it is achievable only where such a sink exists.

**(d)** Because Carnot assumes infinitely slow, reversible heat transfer through
zero temperature difference in the exchangers, which carries zero flux. Any device
that transfers heat at a finite rate does so through a finite temperature
difference (equation (4) of the lesson), and that difference is entropy production
which no engineering can remove.

---

## ★4 — Entropy of fusion

**(a)** $\Delta s_{\text{fus}} = L/T = 4\times10^5/1500 = 266.7$
J kg⁻¹ K⁻¹.

**(b)** $\Delta s = c_p\ln(1500/300) = 840\times1.6094 = 1351.9$
J kg⁻¹ K⁻¹.

**(c)** Ratio $= 266.7/1351.9 = 0.197$. Approximately one fifth of the entropy
change associated with the whole cooling history occurs at the crystallisation
front, which is therefore where 20 per cent of the *irreversibility* is
concentrated while the front is active. That is why crystallisation is
entropy-limited and proceeds at essentially constant temperature.

**(d)** Because energy and entropy weight the same process by different factors:
the latent heat carries a factor $1/T_m$ while the sensible heat carries
$\ln(T_2/T_1)$. The energy fraction was 28.4 per cent (lesson 02-05-01), while the
entropy fraction is 19.7 per cent; neither can be read off the other.

---

## ★★5 — Reading the demo

**(a)** $1.890\,570\times10^{-4}$ (1600/283),
$1.484\,320\times10^{-4}$ (800/283),
$5.541\,924\times10^{-5}$ (373/283), and exactly $0$ (1600/1600), all in
W m⁻² K⁻¹.

**(b)** Because $1/T_c - 1/T_h = 0$ when the two temperatures are equal; the
production vanishes, and so does the flux that could carry it. A finite flux at
zero temperature difference would require infinite conductivity.

**(c)** With $T_c = 283$ K the bracket $1/T_c - 1/T_h$ is
$3.5336\times10^{-3} - 6.25\times10^{-4} = 2.9086\times10^{-3}$ K⁻¹ at
$T_h = 1600$ K, and $3.5336\times10^{-3} - 1.25\times10^{-3}
= 2.2836\times10^{-3}$ K⁻¹ at $T_h = 800$ K. The ratio is
$2.9086/2.2836 = 1.274$, which is exactly the ratio of the two tabulated values
($1.8906/1.4843 = 1.274$). **The steeper temperature drop produces 27 per cent
more entropy for the same flux.**

**(d)** That either the temperature gradient is mis-signed, or the flux has an
advective component, or the system is not in a steady state and is storing
entropy. In a laboratory measurement it almost always means the heat flux is being
estimated from a thermal-conductivity model that is wrong rather than measured.

---

## ★★6 — Entropy production in the lithosphere

**(a)** Start from
$\rho\,\partial s/\partial t + \nabla\cdot(\mathbf q/T) = \sigma$ with
$\mathbf q = -k\nabla T$. Then
$\nabla\cdot(\mathbf q/T) = \nabla\cdot\mathbf q/T + \mathbf q\cdot\nabla(1/T)
= \nabla\cdot\mathbf q/T - \mathbf q\cdot\nabla T/T^2$. Substituting
$\mathbf q = -k\nabla T$ and using the energy equation
$\rho c_p\partial T/\partial t = -\nabla\cdot\mathbf q$ gives
$\rho T\,\partial s/\partial t = \rho c_p\partial T/\partial t$, so all terms
cancel except

$$\sigma = k\frac{|\nabla T|^2}{T^2} .$$

**(b)** With $|\nabla T| = G$ and $T = T_0 + Gz$,

$$\Sigma = \int_0^H kG^2\frac{\mathrm{d}z}{(T_0+Gz)^2}
= kG^2\cdot\frac{1}{G}\left(\frac{1}{T_0}-\frac{1}{T_H}\right)
= kG\left(\frac{1}{T_0}-\frac{1}{T_H}\right) .$$

**(c)** $G = (1200-280)/80\,000 = 0.0115$ K m⁻¹ $= 11.5$ K km⁻¹.
$\Sigma = 3.0\times0.0115\times(1/280 - 1/1200)
= 0.0345\times(3.5714\times10^{-3} - 8.3333\times10^{-4})
= 0.0345\times2.7381\times10^{-3} = 9.446\times10^{-5}$ W m⁻² K⁻¹.
Globally $9.446\times10^{-5}\times5.10\times10^{14}
= 4.82\times10^{10}$ W K⁻¹.

**(d)** Because $\sigma$ is quadratic in the gradient while the flux is linear in
it. Doubling $G$ doubles the flux but quadruples the production. A given amount of
heat delivered through a steep gradient therefore costs more than four times as
much entropy as the same heat delivered through a shallow one — which is why
lithospheric conduction, with its tens of kelvin per kilometre, is a more
profligate entropy producer per unit of heat than mantle convection is.

---

## ★★7 — District heating

**(a)** $1 - 313.15/363.15 = 0.1378$.

**(b)** The exergy relative to a 278.15 K (5 °C) ambient is
$\dot E = \dot Q(1 - T_0/\bar T)$, with $\bar T$ a mean delivery temperature.
Taking the supply temperature 363.15 K as the upper bound,
$\dot E = 20\times(1 - 278.15/363.15) = 20\times0.2340 = 4.68$ MW. Taking the
arithmetic mean of supply and return (75 °C = 348.15 K),
$\dot E = 20\times(1 - 278.15/348.15) = 20\times0.2011 = 4.02$ MW. Quote one of
these and say which temperature you used; the difference is 14 per cent and it
matters.

**(c)** Because the *product* is heat at a temperature useful for space heating,
not work. The second law values heat by its temperature, and 60–90 °C is exactly
the temperature a building needs, so almost all of the delivered energy is used
at the right quality. Its low Carnot efficiency is irrelevant when the desired
output is heat rather than work.

**(d)** Electricity at 8 per cent efficiency from 20 MW thermal gives 1.6 MWe,
which is worth more per unit of energy but delivers only a fraction of the heat.
The trade-off is quality versus quantity: district heating uses nearly all the
energy at low quality, electricity uses a small fraction at high quality. The
correct choice depends on the relative prices of heat and power, which is an
economic question informed by, but not answered by, the second law.

---

## ★★8 — Secular cooling

**(a)** $\dot S = \dot Q(1/T_s - 1/T_i)$.

**(b)** $31\times10^{12}\times(1/283 - 1/1600)
= 3.1\times10^{13}\times(3.5336\times10^{-3} - 6.25\times10^{-4})
= 3.1\times10^{13}\times2.9086\times10^{-3} = 9.02\times10^{10}$ W K⁻¹.

**(c)** Conduction: $3.9\times10^{10}$ W K⁻¹. Secular cooling:
$9.0\times10^{10}$ W K⁻¹ — comparable, about 2.3 times larger. Radiation:
$4.56\times10^{14}$ W K⁻¹ — 5000 times larger than either.

**(d)** None of the three is a clean upper bound, because they are not all the
same kind of quantity. The radiative figure is the entropy *exported* by
irreversible degradation of solar photons, which dominates the planet's
irreversibility. Interior conduction and secular cooling are the solid Earth's
internal production, and their sum (≈1.3 × 10¹¹ W K⁻¹) is the correct figure for
"the solid Earth's entropy production". They are comparable to one another; both
are four orders below the radiative figure. Comparing them directly is legitimate
as long as it is stated that they are different *processes*, not competing
estimates of one quantity.

---

## ★★9 — Heat pump

**(a)** COP $= \dot Q_{\text{out}}/\dot W = 4/1 = 4.0$.

**(b)** COP$_{\max} = T_h/(T_h - T_c) = 313.15/(313.15 - 278.15) = 8.95$.

**(c)** Two checks. *First law:* the ground supplies
$\dot Q_c = \dot Q_h - \dot W = 4 - 1 = 3$ kW, and $3 + 1 = 4$ kW arrives in the
house ✓. *Second law:* the entropy delivered to the house is
$\dot Q_h/T_h = 4000/313.15 = 12.77$ W K⁻¹ and the entropy removed from the
ground loop is $\dot Q_c/T_c = 3000/278.15 = 10.79$ W K⁻¹. The difference,
$12.77 - 10.79 = 1.98$ W K⁻¹, is supplied by the entropy associated with the work
input and by the irreversibility of the compressor. Equivalently, the realised
COP of 4.0 is well below the Carnot value of 8.95 that a reversible device would
achieve, so the second law is satisfied with room to spare.

**(d)** COP above Carnot would mean pumping more heat uphill than the minimum work
requires, i.e. more energy transferred than the entropy books allow. Since the
Carnot COP corresponds to a reversible device, exceeding it means negative entropy
production in the universe — a perpetual-motion machine of the second kind.

---

## ★★★10 — Viscous dissipation in the mantle

**(a)** $\tau_{ij}$ has units Pa = J m⁻³ and $\dot\varepsilon_{ij}$ has units s⁻¹,
so $\tau\dot\varepsilon$ is J m⁻³ s⁻¹, a power per unit volume ✓. Dividing by
$T$ (K) gives J m⁻³ s⁻¹ K⁻¹ = W m⁻³ K⁻¹, an entropy production per unit volume
per unit time ✓.

**(b)** $\sigma_{\text{vis}} = 10^6\times10^{-15}/2000 = 5\times10^{-10}$ W m⁻³ K⁻¹.

**(c)** Globally: $5\times10^{-10}\times8.889\times10^{20}
= 4.44\times10^{11}$ W K⁻¹. Both this and the conductive figure from lesson §2.3
($3.9\times10^{10}$ W K⁻¹) are already *global* rates, so they are directly
comparable: the mantle's viscous dissipation produces about **11 times** as much
entropy as the entire lithospheric conduction, and about $10^{-3}$ of the
radiation budget ($4.56\times10^{14}$ W K⁻¹).

**(d)** The mechanical power dissipated is
$\int\sigma_{\text{vis}}T\,\mathrm{d}V = 4.44\times10^{11}\times2000
= 8.9\times10^{14}$ W $= 0.89$ TW. Against a total surface heat loss of ~46 TW
that is about 2 per cent, so viscous dissipation is a small but not negligible
term in the mantle's energy budget. Its ratio to the total flux is indeed of the
same order as the ratio of viscous to total energy transport, which is the
self-consistency the question asks for. **The uncertainty is large**: both the
mean stress (order of magnitude) and the strain rate (two orders) are nominal
values for a mantle whose viscosity varies by orders of magnitude with depth and
temperature, and the entropy-production integral weights the hot, low-viscosity
regions far more heavily than the cold ones. A defensible answer is
$10^{11}$–$10^{12}$ W K⁻¹, i.e. an order of magnitude with the assumption stated.

---

## ★★★11 — Reversibility and its limits

**(a)** The two limits are (i) infinitesimal temperature differences in every heat
exchanger, so that all heat transfer is reversible, and (ii) infinitesimal
resistance to flow, so that no viscous dissipation occurs. Neither is available to
a geothermal plant: (i) would require exchangers of infinite area and a flow rate
that carried no heat, and (ii) would require an infinite wellbore. Both are the
classic "infinite time or infinite size" limits of reversible thermodynamics.

**(b)** Carnot for 1600 K and 283 K gives $\eta = 1 - 283/1600 = 0.8231$. A claim
of 0.90 exceeds the bound. In entropy terms: extracting $Q$ at 1600 K removes
$Q/1600$ from the hot reservoir; rejecting the unavoidable $0.1Q$ at 283 K adds
$0.1Q/283$; the work output $0.9Q$ must be accompanied by zero entropy change. The
hot reservoir loses $Q/1600 = 6.25\times10^{-4}Q$; the cold gains
$0.1Q/283 = 3.53\times10^{-4}Q$. Net entropy change
$= 3.53\times10^{-4}Q - 6.25\times10^{-4}Q = -2.72\times10^{-4}Q < 0$ for
$Q > 0$: a decrease in total entropy, which the second law forbids.

**(c)** The error is conflating "generates heat" with "generates energy". Viscous
dissipation converts *mechanical* energy into heat, and the mechanical energy
came from the gravitational potential energy released by sinking material, which
in turn came from the thermal buoyancy produced by the mantle's own cooling. It is
a redistribution, not a source. The first law allows it — dissipation is a
conversion, not a creation — and the second law requires that at each conversion
the total entropy rises, which is why the process is not a cycle that returns the
mantle to its original state with more energy. The correct accounting is:
convection transports heat from the interior to the surface, dissipating a small
fraction (exercise 10 gives about 2 per cent) as it goes, while the interior cools
because the surface flux exceeds the internal generation.

**(d)** The fraction is set by the temperature *contrast* across which the
transport occurs, relative to the absolute temperature. Mantle convection moves
heat across a contrast of order 1000 K at a mean temperature of order 2000 K, so
the fractional entropy production is of order $\Delta T/T \sim 0.5$ per unit of
heat moved. The radiation budget moves the same energy across a contrast of
5772 − 255 = 5517 K at a mean of order 250 K, so its fractional production is of
order $\Delta T/T \sim 20$ per unit of heat — forty times larger. The general rule
is that a process loses quality in proportion to the fractional temperature drop
it spans, which is why a hot source and a cold sink is the most irreversible
configuration available.
