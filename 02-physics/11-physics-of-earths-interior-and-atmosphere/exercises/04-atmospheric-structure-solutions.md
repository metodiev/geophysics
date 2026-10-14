# Solutions — 02-11-04 Atmospheric Structure, Hydrostatic Balance and Lapse Rates

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Sea-level pressure and standard gravity are
> **exact**; the molar mass of air and $c_p$ are **nominal**; the standard
> atmosphere's layer structure is a **defined standard**.

---

## ★1 — Scale height

**(a)** $H(288.15\ \text{K}) = 287.058\times288.15/9.806\,65 = \mathbf{8\,435}$ m
$= 8.435$ km; $H(300\ \text{K}) = 287.058\times300/9.806\,65 = \mathbf{8\,782}$ m
$= 8.782$ km.

**(b)** $e$-folding: $H = 8.435$ km. Halving: $H\ln 2 = 8.435\times0.693\,15
= \mathbf{5.847}$ km.

**(c)** The mass below height $z$ in an isothermal atmosphere is
$1-e^{-z/H}$, so: $1-e^{-1} = 0.632$ (63 per cent) below $H$;
$1-e^{-2} = 0.865$ (86 per cent) below $2H$;
$1-e^{-3} = 0.950$ (95 per cent) below $3H = 25.3$ km.

**(d)** Because $H = RT/g$ requires an ideal gas, and water is essentially
incompressible. Its pressure gradient is $\rho g = 9.79$ kPa m⁻¹ and there is no
exponential scale height; the concept simply does not apply.

---

## ★2 — The dry adiabatic lapse rate

**(a)** For an adiabatic parcel $\mathrm{d}h = v\,\mathrm{d}P$, and for an ideal
gas $\mathrm{d}h = c_p\,\mathrm{d}T$, so $c_p\,\mathrm{d}T = v\,\mathrm{d}P$.
Hydrostatic balance in the environment gives
$\mathrm{d}P = -\rho g\,\mathrm{d}z$, and $v = 1/\rho$, so
$c_p\,\mathrm{d}T = -\rho g\,\mathrm{d}z/\rho = -g\,\mathrm{d}z$, hence
$\Gamma_d \equiv -\mathrm{d}T/\mathrm{d}z = g/c_p$ ✓.

**(b)** $\Gamma_d = 9.806\,65/1005 = \mathbf{9.758}$ K km⁻¹.

**(c)** $\dfrac{0.4}{1.4}\times\dfrac{9.806\,65}{287.058}
= 0.285\,714\times0.034\,163 = 9.761\times10^{-3}$ K m⁻¹ $= \mathbf{9.761}$
K km⁻¹. The 0.02 per cent difference from (b) is the difference between the
nominal $c_p = 1005$ and the value implied by $\gamma = 1.4$ and $R_{\text{air}}$.

**(d)** Adiabatic (no heat exchange), reversible (no dissipation), hydrostatic
equilibrium in the environment, ideal gas with constant $c_p$. In a cloud the
**adiabatic** assumption fails, because condensation releases latent heat into the
parcel; the correct rate is then the moist adiabatic lapse rate, which is shallower
and not constant.

---

## ★3 — Isothermal atmosphere

**(a)** $p = 101\,325\exp(-5500/8434.7) = 101\,325\times0.520\,86
= \mathbf{52\,787}$ Pa $= 527.9$ hPa.

**(b)** $z = H\ln 2 = \mathbf{5\,847}$ m $= 5.847$ km.

**(c)** Because the real troposphere is not isothermal — its temperature falls at
6.5 K km⁻¹, so the air at 5.5 km is colder (and therefore denser) than the
isothermal model assumes. A colder, denser column has a *steeper* pressure
gradient, so the real pressure at 5.5 km is lower than the isothermal value. The
correct standard-atmosphere value is obtained from the power law of ★5.

**(d)** Right: the isothermal solution has $p = p_0e^{-z/H}$, and the halving
height is $H\ln2 \approx 5.85$ km, close to 5.5 km. Wrong: the real atmosphere is
not isothermal, so the height at which the pressure actually halves is not
$H\ln2$; it is about 5.5 km in the standard troposphere, and it varies. The
statement is a good approximation with a false justification.

---

## ★4 — Potential temperature and stability

**(a)** $\theta = T(p_0/p)^{R/c_p}$ with $p_0 = 101\,325$ Pa: the temperature a
parcel would have if moved adiabatically to $p_0$.

**(b)** Along an adiabatic displacement $\mathrm{d}\theta = 0$, so the parcel's
$\theta$ is conserved. If $\mathrm{d}\theta/\mathrm{d}z>0$, a parcel displaced
upward arrives in an environment of *higher* $\theta$, i.e. the parcel is colder
and denser than its surroundings, and sinks back: stable. The comparison is
against the **dry adiabat**, since $\theta$ is defined by a dry adiabatic
displacement.

**(c)** $N^2 = \dfrac{g}{T}\left(\Gamma_d-\Gamma\right)$, where
$\Gamma = -\mathrm{d}T/\mathrm{d}z$. $N^2>0$: stable, oscillatory. $N^2 = 0$:
neutral, the parcel stays put. $N^2<0$: unstable, the parcel accelerates away and
convection follows.

**(d)** $N^2 = \dfrac{9.806\,65}{250}\times(9.758-12)\times10^{-3}
= 0.0392\times(-2.242\times10^{-3}) = \mathbf{-8.79\times10^{-5}}$ s⁻². Negative:
the layer is **unstable** and will overturn on the buoyancy timescale, which is
minutes for a layer a few hundred metres thick. Such a lapse rate is not observed
as a persistent state; it is the state that produces convection.

---

## ★★5 — The power law

**(a)** With $T = T_0+\Gamma'z$ and $\mathrm{d}T = \Gamma'\,\mathrm{d}z$,
substituting $\mathrm{d}z = \mathrm{d}T/\Gamma'$ into
$\mathrm{d}P/P = -g\,\mathrm{d}z/(R_{\text{air}}T)$ gives
$\mathrm{d}\ln P = -\dfrac{g}{R_{\text{air}}\Gamma'}\dfrac{\mathrm{d}T}{T}$, so
$\ln(P/P_0) = -\dfrac{g}{R_{\text{air}}\Gamma'}\ln(T/T_0)$ and
$P = P_0(T/T_0)^{-g/(R_{\text{air}}\Gamma')}$. Writing
$\Gamma = -\Gamma'$ gives $P = P_0(T/T_0)^{g/(R_{\text{air}}\Gamma)}$ ✓.

**(b)** $\dfrac{g}{R_{\text{air}}\Gamma} = \dfrac{9.806\,65}{287.058\times6.5\times10^{-3}}
= \dfrac{9.806\,65}{1.865\,88} = \mathbf{5.256}$.

**(c)** $T(5\ \text{km}) = 288.15-6.5\times5 = 255.65$ K, so
$p = 101\,325\times(255.65/288.15)^{5.256}
= 101\,325\times0.887\,21^{5.256}$. With
$\ln(0.887\,21) = -0.119\,65$ and $5.256\times(-0.119\,65) = -0.628\,89$,
$p = 101\,325\times0.533\,19 = \mathbf{54\,019}$ Pa. (The demo gives 54 020.5 Pa
at the grid point nearest 5 km.)

**(d)** The isothermal value at 5 km is 56 011 Pa, which is **3.7 per cent
higher**. The direction is as expected: a lapse rate makes the air aloft colder and
denser than an isothermal column would, so the pressure falls off *faster* with
height. A lapse rate always compresses the atmosphere more strongly than the
exponential.

---

## ★★6 — A dry-adiabatic troposphere

**(a)** $T(5\ \text{km}) = 288.15-9.758\times5 = \mathbf{239.36}$ K.

**(b)** Exponent $= 9.806\,65/(287.058\times9.758\times10^{-3}) = 3.501$, so
$p = 101\,325\times(239.36/288.15)^{3.501}
= 101\,325\times0.830\,75^{3.501}$. With $\ln(0.830\,75) = -0.185\,37$ and
$3.501\times(-0.185\,37) = -0.649\,00$,
$p = 101\,325\times0.522\,53 = \mathbf{52\,924}$ Pa.

**(c)** The standard atmosphere gives 54 019 Pa at the same height; the dry
adiabat gives 52 924 Pa, which is **2.0 per cent lower**. Again the direction
follows from the temperature: the dry adiabat is steeper, so the air at 5 km is
colder (239.4 K against 255.7 K), denser, and the column is more compressed.

**(d)** $N^2 = \dfrac{g}{T}(\Gamma_d-\Gamma_d) = \mathbf{0}$ exactly: **neutral**.
A dry-adiabatic layer is on the knife edge — any parcel displaced finds itself
exactly in equilibrium, neither returning nor accelerating, and in practice
convection proceeds on whatever small perturbation is present. This is why a
troposphere at the dry adiabat would be vigorously convective everywhere, and why
the real atmosphere, which has a source of heat (latent) that shallows the
operative lapse rate, sits at 6.5 K km⁻¹ instead.

---

## ★★7 — The standard atmosphere

**(a)** $T_0 = 288.15$ K, $p_0 = 101\,325$ Pa, and the lapse-rate breakpoints:

| Base height (km) | Lapse rate (K km⁻¹) |
|---|---|
| 0 | $-6.5$ |
| 11 | $0$ |
| 20 | $+1.0$ |
| 32 | $+2.8$ |
| 47 | $0$ |
| 51 | $-2.8$ |
| 71 | $-2.0$ |
| 84.852 | (end) |

**(b)** Layer by layer with equation (8) of the lesson:
$p(11\ \text{km}) = 101\,325\times(216.65/288.15)^{5.256} = \mathbf{22\,633}$ Pa;
$p(20\ \text{km}) = 22\,633\exp[-9.806\,65\times9000/(287.058\times216.65)]
= \mathbf{5\,475}$ Pa;
$p(32\ \text{km}) = 5\,475\times(228.65/216.65)^{9.806\,65/(287.058\times1.0\times10^{-3})}
= \mathbf{868}$ Pa. (The exponent for the $+1.0$ K km⁻¹ layer is
$9.80665/(287.058\times10^{-3}) = 34.16$.)

**(c)** Fractions of the surface pressure: $22\,633/101\,325 = \mathbf{22.3}$ per
cent at 11 km; $5\,475/101\,325 = \mathbf{5.40}$ per cent at 20 km;
$868/101\,325 = \mathbf{0.857}$ per cent at 32 km.

**(d)** Because the lapse rate in that layer is defined to be **zero** — the
11–20 km layer is isothermal in the standard atmosphere, at 216.65 K. This is the
standard's modelling of the lower stratosphere, where ozone absorption roughly
balances radiative cooling so that the temperature is nearly constant with height.

---

## ★★8 — The atmosphere's mass

**(a)** Integrating $\mathrm{d}P/\mathrm{d}z = -\rho g$ over the whole atmosphere
with constant $g$:
$\int_0^\infty \rho\,\mathrm{d}z = -\frac{1}{g}\int_{p_0}^{0}\mathrm{d}P
= p_0/g$. The mass is that column mass times the surface area:
$M_{\text{atm}} = 4\pi R^2p_0/g$ ✓.

**(b)** $M_{\text{atm}} = 4\pi(6.371\times10^6)^2\times101\,325/9.806\,65
= \mathbf{5.27\times10^{18}}$ kg. As a fraction of
$M_\oplus = 5.972\times10^{24}$ kg: $8.83\times10^{-7}$, i.e. about **one
millionth**.

**(c)** With $g = 3.71$ m s⁻²: $M_{\text{atm}} = 5.27\times10^{18}\times(9.806\,65/3.71)
= \mathbf{1.39\times10^{19}}$ kg. The mass is **larger**, because the same surface
pressure must be supported by more mass when gravity is weaker — the pressure is
the weight per unit area.

**(d)** The two assumptions are a spherical Earth and sea-level pressure applied
over the whole surface. The first is very accurate; the second biases the answer
**high**, because a large fraction of the land surface lies above sea level and
carries a lower surface pressure. So 5.27 × 10¹⁸ kg is an upper bound of a few per
cent, not a measurement.

---

## ★★★9 — Another planet's atmosphere

**(a)** $R_{\text{specific}} = R/M_{\text{CO}_2}
= 8.314\,462\,618\,153\,24/0.044\,01 = \mathbf{188.92}$ J kg⁻¹ K⁻¹.

**(b)** $H = 188.92\times210/3.71 = \mathbf{10\,694}$ m $= 10.69$ km.

**(c)** $\Gamma_d = g/c_p = 3.71/843 = 4.40\times10^{-3}$ K m⁻¹
$= \mathbf{4.40}$ K km⁻¹. The assumption is $c_p = 843$ J kg⁻¹ K⁻¹, a nominal
value for CO₂ near these temperatures; $c_p$ is temperature-dependent and the
value must be checked for the actual conditions.

**(d)** The Earth's $H$ at a comparable temperature is about 6.3 km at 216.65 K
and 8.4 km at 288.15 K. At 210 K the Earth's value would be
$287.058\times210/9.80665 = 6.15$ km, so the CO₂ atmosphere's 10.69 km is
**1.7 times larger**. From $H = RT/g$, the two reasons are the smaller $g$
(3.71 against 9.81, a factor of 2.64 in the numerator) partly offset by the larger
molar mass (a factor of 0.658 in $R_{\text{specific}}$): $2.64\times0.658 = 1.74$ ✓.

---

## ★★★10 — Stability through the real profile

**(a)** From the demo: $\theta = 288.15$ K at 0 km, 305.96 K at 5 km, 332.43 K at
11 km, 1897.03 K at 47 km.

**(b)**

| $z$ (km) | $N$ (s⁻¹) | Period (min) |
|---|---|---|
| 0 | 0.01053 | 9.9 |
| 5 | 0.01118 | 9.4 |
| 11 | 0.02102 | 5.0 |
| 47 | 0.01880 | 5.6 |

**(c)** Below the tropopause, $\Gamma = 6.5$ K km⁻¹ so
$\Gamma_d-\Gamma = 9.758-6.5 = 3.258$ K km⁻¹. Above it, $\Gamma = 0$ so
$\Gamma_d-\Gamma = 9.758$ K km⁻¹ — a factor of **3.0** larger. The factor in
$N^2$ is therefore 3.0, and the factor in $N$ is $\sqrt3 = 1.73$, close to the
observed 0.02102/0.01053 = 2.0 (the difference arising from the temperature, which
appears in the denominator and is smaller above the tropopause). So the doubling
is mostly the removal of the lapse rate, amplified slightly by the lower
temperature.

**(d)** Stability is measured against the **adiabatic** reference, not against
zero. $\theta$ rises monotonically through the whole troposphere — from 288.15 K at
the surface to 332.43 K at the tropopause — so a displaced parcel finds itself
colder than its environment and returns: the layer is stable, and the reason is
that 6.5 < 9.758.

---

## ★★★11 — Why the observed lapse rate is not the dry adiabat

**(a)** $9.758/6.5 = \mathbf{1.50}$: the dry adiabat is 50 per cent steeper.

**(b)** Rising saturated air condenses water, releasing latent heat inside the
parcel and warming it relative to a dry parcel that had done the same work. The
resulting *moist* adiabatic lapse rate is therefore shallower than the dry one, and
because the amount of water vapour the air can hold falls rapidly with
temperature (Clausius–Clapeyron), the moist rate depends on temperature and
pressure and is not a constant. It approaches the dry rate as the air dries.

**(c)** Radiative equilibrium — the balance of absorbed solar and emitted longwave
radiation — in a grey atmosphere requires a temperature profile that decreases
*faster* than the dry adiabat, i.e. it would be convectively unstable. The
atmosphere therefore convects until the profile is marginally stable against the
*moist* adiabat, and the observed profile is the outcome of that competition. The
two constraints bracket the observed value, which is why it lies between the moist
and the radiative-equilibrium rates.

**(d)** The mean profile is an average over tropical deep convection (which
follows a moist adiabat and produces a deep troposphere), mid-latitude baroclinic
eddies, and polar radiative cooling (which produces a shallow troposphere with a
low tropopause). The standard atmosphere's single lapse rate and single 11 km
tropopause are therefore a *mid-latitude climatological average*, and using them
at a particular place and season is an error of a few kilometres in the tropopause
height and a few K km⁻¹ in the lapse rate. That is why a forecast model carries
the actual profile, not the standard.

---

## ★★★12 — Verification of a hydrostatic integration

**(a)** The test is the tropospheric analytic solution
$p = p_0(T/T_0)^{g/(R\Gamma)}$, which is exact for a constant lapse rate. The demo
reports a relative difference of $3.21\times10^{-16}$ at 11 km.

**(b)** Because the integration scheme is *exact* for this differential equation:
within a constant-lapse segment, the scheme applies the closed-form step rather
than a finite-difference approximation, so the only error is floating-point
round-off, and $10^{-16}$ is the machine epsilon of double precision. In lesson
[01](../01-pressure-density-depth.md) §8, by contrast, the integrator is a
rectangle rule and the exact solutions are not reproduced by it; the correct
outcome there is a small but non-zero error of order $10^{-4}$, decreasing with the
step. The lesson is that the *expected* size of a verification discrepancy is set
by the scheme, not by a universal tolerance — a $10^{-4}$ error here would indicate
a bug, and a $10^{-16}$ error there would indicate the test was not testing
anything.

**(c)** A coding error that affects both the numerical integration and the analytic
comparison identically, because both call the same temperature function. For
example, an error in the lapse-rate table would produce a self-consistent
temperature profile in both, and the test would pass while the profile was wrong.
The way to catch it is to compare the computed temperatures at the breakpoints
against the standard atmosphere's tabulated values (288.15, 216.65, 228.65, 270.65
K), which the demo does by listing them.

**(d)** Sharing the temperature function makes the test a check of the *quadrature*
only, not of the temperature profile. Strengthening it requires an independent
source for the profile: either the standard's own tabulated $T(z)$ values, entered
separately, or a second, independently coded temperature routine. Only then does
the test verify the profile as well as the integration.
