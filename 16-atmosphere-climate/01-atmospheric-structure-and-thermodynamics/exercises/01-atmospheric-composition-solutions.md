# Solutions — 16-01-01 Atmospheric Composition and Vertical Structure

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; where a problem admits more than one defensible route it is said so. All
> models are **SYNTHETIC** teaching values.

Lesson: [01 Atmospheric Composition](../01-atmospheric-composition.md).

---

## ★1 — Mean molar mass of a three-species mixture

$$M_d = 0.79(28.0134) + 0.20(31.9988) + 0.01(39.9480)
= 22.130586 + 6.399760 + 0.399480 .$$

| term | value | unit |
|---|---|---|
| $0.79\,M_{\mathrm{N_2}}$ | 22.130586 | g mol⁻¹ |
| $0.20\,M_{\mathrm{O_2}}$ | 6.399760 | g mol⁻¹ |
| $0.01\,M_{\mathrm{Ar}}$ | 0.399480 | g mol⁻¹ |
| $M_d$ | **28.929826** | g mol⁻¹ |

$$R_d = \frac{R^{*}}{M_d} = \frac{8.314462618}{2.8929826\times10^{-2}}
= 287.401\ \mathrm{J\,kg^{-1}\,K^{-1}} .$$

The crude model differs from the lesson's ten-species value ($287.041$) by
$0.13\%$: composition details matter at the level of the third figure for $R_d$.

---

## ★2 — Specific heats and a Mayer check

$$c_p = \frac{\gamma}{\gamma-1}R_d = \frac{1.4}{0.4}(287.401) = 1005.90\
\mathrm{J\,kg^{-1}\,K^{-1}},$$
$$c_v = \frac{R_d}{\gamma-1} = \frac{287.401}{0.4} = 718.50\
\mathrm{J\,kg^{-1}\,K^{-1}}.$$

Mayer: $c_p - c_v = 1005.90 - 718.50 = 287.40 \approx R_d = 287.401$ ✔
(the residual is rounding in the printed figures).

Heat at constant pressure: $Q = m c_p \Delta T = 10 \times 1005.90 \times 5
= 5.0295\times10^{4}\ \mathrm{J} \approx 50.3\ \mathrm{kJ}$.

*Note.* At constant *volume* the same $\Delta T$ needs
$m c_v \Delta T = 35.9\ \mathrm{kJ}$; the difference, $14.4\ \mathrm{kJ}$, is the
work the parcel does expanding against the environment. That is the first law in
one line, and it is the physics behind the adiabatic lapse rate in
[03](../03-thermodynamic-processes.md).

---

## ★3 — Scale height

$$H(250\ \mathrm{K}) = \frac{287.401 \times 250}{9.80665} = 7326.7\ \mathrm{m}
= 7.327\ \mathrm{km},$$
$$H(300\ \mathrm{K}) = \frac{287.401 \times 300}{9.80665} = 8792.0\ \mathrm{m}
= 8.792\ \mathrm{km}.$$

Meaning: $H$ is the height over which the pressure of an *isothermal* atmosphere
falls by a factor $e$, because $p/p_0 = e^{-z/H}$. Warmer air has a larger scale
height — it is more expanded — so the pressure falls more slowly with height, and
the same pressure level sits higher.

---

## ★4 — Isothermal pressure ratios at $288\ \mathrm{K}$

$H(288\ \mathrm{K}) = 287.401 \times 288 / 9.80665 = 8440.3\ \mathrm{m}$.

$$p/p_0\,(2\ \mathrm{km}) = e^{-2000/8440.3} = e^{-0.236957} = 0.789025,$$
$$p/p_0\,(7\ \mathrm{km}) = e^{-7000/8440.3} = e^{-0.829350} = 0.436333 .$$

So the isothermal model puts $789\ \mathrm{hPa}$ at $2\ \mathrm{km}$ and
$442\ \mathrm{hPa}$ at $7\ \mathrm{km}$ (using $p_0 = 1013.25\ \mathrm{hPa}$).

---

## ★5 — Polytropic solution and a drier atmosphere

From $\mathrm{d}p/p = -(g/R_d)\,\mathrm{d}z/(T_0-\Gamma z)$, with
$u = T_0 - \Gamma z$ and $\mathrm{d}u = -\Gamma\,\mathrm{d}z$:

$$\ln\frac{p}{p_0} = -\frac{g}{R_d}\int_0^z\frac{\mathrm{d}z'}{T_0-\Gamma z'}
= \frac{g}{R_d\Gamma}\ln\frac{T_0-\Gamma z}{T_0},$$

so $p = p_0\left(T/T_0\right)^{g/(R_d\Gamma)}$, with
$T = 288.15 - 5\Gamma$ at $z = 5\ \mathrm{km}$.

| $\Gamma$ (K km⁻¹) | $T/T_0$ | exponent $g/(R_d\Gamma)$ | $p/p_0$ |
|---|---|---|---|
| 6.5 | 0.887212 | 5.2495 | 0.533541 |
| 9.8 | 0.829950 | 3.4818 | 0.522580 |

The larger lapse rate (9.8 K km⁻¹) gives the smaller pressure at $5\ \mathrm{km}$:
it corresponds to the **drier** atmosphere, because a parcel that does not
condense follows the dry adiabat and cools faster with height, so the air aloft is
colder, denser, and the pressure falls off faster. Moisture makes the lapse rate
*smaller* than the dry value, not larger
([04](../04-moisture-and-clouds.md)).

---

## ★6 — Column mass at a mountain site

(a) Above the site:
$m/A = p/g = 84200/9.80665 = 8586.0\ \mathrm{kg\,m^{-2}}$.

(b) Ratio to the standard column:
$8586.0/10332.27 = 0.830989$.

(c) Fraction of the total mass *below* the site:
$1 - 84200/101325 = 1 - 0.830989 = 0.169011$, i.e. **16.9%**.

Assumptions: (i) **hydrostatic balance** — the surface pressure measures the
weight of the whole column above it; (ii) the column is taken along the local
vertical at the same $g$, and the comparison uses the same standard $p_0$ for the
whole planet. Neither assumption is that the atmosphere is isothermal — this
calculation uses only mass and gravity. Note too that the result is *not* a
statement about altitude alone: $842\ \mathrm{hPa}$ is a pressure, and the
16.9% is the share of the *standard* column mass that happens to lie below that
pressure.

---

## ★7 — Virtual temperature

With $p = p_d + e$ and $\rho = \rho_d + \rho_v = p_d/(R_d T) + e/(R_v T)$,

$$\rho = \frac{p - e}{R_d T} + \frac{e}{R_v T}
= \frac{p}{R_d T}\left[1 - \frac{e}{p}\left(1 - \frac{R_d}{R_v}\right)\right]
= \frac{p}{R_d T}\left[1 - \frac{e}{p}(1-\varepsilon)\right].$$

Requiring $\rho = p/(R_d T_v)$ gives
$T_v = T\big/\big[1-(e/p)(1-\varepsilon)\big]$.

For small $q$, $e/p \approx q/\varepsilon$ (since
$q = \varepsilon e/(p-(1-\varepsilon)e) \approx \varepsilon e/p$), so

$$T_v \approx T\left[1 + \frac{q}{\varepsilon}(1-\varepsilon)\right]
= T\left[1 + q\left(\frac{1}{\varepsilon}-1\right)\right]
= T(1 + 0.608\,q),$$

using $1/0.622 - 1 = 0.6077 \approx 0.608$.

*Numerical:* $T_v = 280(1+0.608\times0.008) = 280(1.004864) = 281.362\ \mathrm{K}$.

$$\rho_{\text{true}} = \frac{85000}{287.041 \times 281.362} = 1.05247\
\mathrm{kg\,m^{-3}}, \quad
\rho_{\text{ignoring moisture}} = \frac{85000}{287.041 \times 280}
= 1.05759\ \mathrm{kg\,m^{-3}}.$$

Relative error $= 1.05759/1.05247 - 1 = +4.84\times10^{-3}$, i.e. **$+0.484\%$**:
ignoring moisture *over*estimates the density (equivalently, under-estimates the
virtual temperature).

---

## ★8 — Thermal speeds and why aerosols are different

$$v_{\text{rms}} = \sqrt{\frac{3k_B T}{m}}, \qquad T = 288.15\ \mathrm{K},
\quad k_B = 1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}.$$

| species | $M$ (g mol⁻¹) | $m$ (kg) | $v_{\text{rms}}$ (m s⁻¹) |
|---|---|---|---|
| N₂ | 28.0134 | $4.6517\times10^{-26}$ | 506.53 |
| H₂O | 18.0153 | $2.9915\times10^{-26}$ | 631.64 |
| CO₂ | 44.0095 | $7.3079\times10^{-26}$ | 404.12 |

(A molecular mass is $M\times10^{-3}/N_A$ with
$N_A = 6.02214076\times10^{23}\ \mathrm{mol^{-1}}$.)

The N₂ value reproduces the demonstration's $506.5\ \mathrm{m\,s^{-1}}$, which is
the check that the calculation is the same one.

*Aerosol particles, by contrast.* Take a spherical water droplet of diameter
$1\ \mathrm{\mu m}$ and density $1000\ \mathrm{kg\,m^{-3}}$ (stated assumptions):
$m = (\pi/6)(10^{-6})^3(1000) = 5.236\times10^{-16}\ \mathrm{kg}$, i.e.
$1.13\times10^{10}$ times the mass of an N₂ molecule. The same formula would give
$v_{\text{rms}} = 4.77\times10^{-3}\ \mathrm{m\,s^{-1}}$ — for practical purposes
zero. Aerosols do not have a molecular thermal speed; they are advected by the
wind, diffused only very slowly by Brownian motion, and settle under gravity. That
is why they are described by a *size distribution* and *optical* properties rather
than by a velocity distribution, and why
[16-02-06](../../02-radiation-and-energy-balance/06-aerosols-and-clouds-radiation.md)
treats them collectively.

---

## ★9 — Model-based specification (no unique answer)

A defensible specification must fix six things.

1. **Data generator.** $T(z) = 288.15 - 6.5 z$ (z in km) plus a
   *height-correlated* perturbation, e.g. a sinusoid of amplitude $A$ and
   wavelength $\lambda$ plus white noise of rms $\sigma$. The lesson's model is
   the $A=\sigma=0$ case, so the generator must include a departure or the
   comparison is trivial. Correlated (not white) noise is essential: a white-noise
   perturbation averages out under column integration and would flatter the
   piecewise model.
2. **Predictor set.** (i) isothermal at $T_0$; (ii) single polytropic with
   $\Gamma = 6.5\ \mathrm{K\,km^{-1}}$; (iii) piecewise integration of the
   generated $T(z)$ with RK4.
3. **Metric.** RMS pressure error in hPa over $0 < z \le 15\ \mathrm{km}$
   (or the maximum absolute error, with the choice stated). Better: both, since a
   small RMS can hide a large bias aloft.
4. **Baseline.** The forward integration of the *same* generator with RK4 is the
   reference; the comparison between (i) and (ii) must be made against it, not
   against each other.
5. **Expected ranking.** (iii) beats (i) and (ii) at every amplitude, because it
   contains the true $T(z)$ up to noise. Between (i) and (ii): the isothermal
   model has a *biased* error growing upward (measured in the lesson as $10.2\%$
   at $8\ \mathrm{km}$), so (ii) wins for any $\Gamma$ near $6.5\
   \mathrm{K\,km^{-1}}$, while (i) can win if the generator is nearly isothermal
   ($A$ small and a mean lapse rate below about $2\ \mathrm{K\,km^{-1}}$), because
   (ii) then imposes a lapse rate the data does not have.
6. **The measurement that reverses the ranking.** A *cold-tropopause* test:
   compare the heights of the minimum in the generated $T(z)$ with the $T = 0\
   \mathrm{K}$ extrapolation of the fitted lapse rate. A single-$\Gamma$ model
   eventually predicts a negative absolute temperature, and the height at which
   it does is a diagnostic of how far a constant-lapse-rate assumption can be
   trusted. That check is a *measurement of the model's own breakdown*, which is
   the point.

---

## ★10 — Error budget for the atmospheric mass

$M = p_0 A/g$ is "exact" only as *bookkeeping*: it is the integral of hydrostatic
balance, so it is exact for the actual pressure and gravity fields. The uncertainty
splits as follows.

- **Definitional part.** $p_0 = 101325\ \mathrm{Pa}$ and $g = 9.80665\
  \mathrm{m\,s^{-2}}$ are definitions of the standard atmosphere. Together they
  fix the reference column $10332.27\ \mathrm{kg\,m^{-2}}$ with no uncertainty
  attached — but they describe a *hypothetical* atmosphere.
- **Geometric part.** $A = 4\pi R_E^2$ uses a mean radius; a $0.1\%$ error in
  $R_E$ is a $0.2\%$ error in $A$ (radius enters squared). Terrain contributes at
  the level of its mean height, $\sim 0.8\ \mathrm{km}$ out of $6371\ \mathrm{km}$,
  i.e. $0.03\%$ in $A$ — smaller than it feels.
- **Physical part.** The real global-mean surface pressure differs from
  $101325\ \mathrm{Pa}$ in the third figure and varies with weather by $\pm3\%$
  locally. The column mass over any particular site is therefore a *time-varying,
  site-specific* quantity.
- **Gravity part.** $g$ varies by $\sim 0.5\%$ with latitude (the equatorial
  bulge) and by $\sim 0.03\%$ from surface height. Using a single $g$ in
  $p_0/g$ mixes two effects, since the same $p_0$ at the equator and the pole
  corresponds to different column masses.

**Conclusion.** The physical part dominates: the honest statement is
"$5.27\times10^{18}\ \mathrm{kg}$ for the standard atmosphere", with the physical
uncertainty of the real global mean an order of magnitude larger than the
definitional precision. The definitional part is not an uncertainty at all; it is
a convention.

---

## ★11 — The CO₂ sensitivity of $R_d$

Repeating §3.1 with the lesson's ten-species table, changing
$x_{\mathrm{CO_2}}$ from $4.20\times10^{-4}$ to $1.00\times10^{-3}$ and
re-normalising:

$$M_d(420\ \mathrm{ppm}) = 28.966098\ \mathrm{g\,mol^{-1}}, \quad
M_d(1000\ \mathrm{ppm}) = 28.974818\ \mathrm{g\,mol^{-1}},$$

$$\Delta M_d = +8.72\times10^{-3}\ \mathrm{g\,mol^{-1}},
\qquad \frac{\Delta M_d}{M_d} = +3.01\times10^{-4}.$$

$$R_d(420) = 287.041\ \mathrm{J\,kg^{-1}\,K^{-1}}, \quad
R_d(1000) = 286.955\ \mathrm{J\,kg^{-1}\,K^{-1}},$$

i.e. $R_d$ **falls** by $0.086\ \mathrm{J\,kg^{-1}\,K^{-1}}$ ($-0.030\%$), because
the replacement molecule is heavier than the mean.

**Why a negligible effect can be central.**

A change of $3\times10^{-4}$ in $R_d$ shifts a computed temperature by
$0.03\%$ (about $0.09\ \mathrm{K}$ at $288\ \mathrm{K}$) if pressure and density
are held fixed — below the level at which any weather model could care. The
radiative effect works differently: it is not a change in a *bulk* property
averaged over all molecules, but a change in the *number of absorbers* at
specific wavelengths where almost nothing else absorbs. Averaging over the
mixture dilutes a trace gas; spectral selectivity concentrates it. The same
molecule can therefore be dynamically irrelevant and radiatively decisive, and
the two statements are not in conflict.

The radiative side is quantified from measured absorption spectra in
[16-02-02](../../02-radiation-and-energy-balance/02-radiative-transfer-atmosphere.md);
this module does not assert a radiative number here, only the mass arithmetic
above.
