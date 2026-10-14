# Exercises — 14-02-07 Borehole Geophysics for Aquifer Characterisation

Attempt these before reading the
[solutions](./07-borehole-hydrogeophysics-solutions.md). The lesson is
[07 Borehole Geophysics for Aquifer Characterisation](../07-borehole-hydrogeophysics.md).
Every log, unit, calibration and test below is **SYNTHETIC**.

Constants and models to use:
$\rho_{\text{matrix}} = 2650$, $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$,
$\rho_w g/\mu = 9.79 \times 10^{6}\ \mathrm{m^{-1}\,s^{-1}}$ (converts $k$ in
m² to m s$^{-1}$),
$V_{\text{clay}} = (\mathrm{GR} - 30)/150$,
$\phi = (\rho_{\text{matrix}} - \rho_b)/(\rho_{\text{matrix}} - \rho_w)$,
$\mathrm{Sw} = [R_w/(\phi^{m}R_t)]^{1/n}$ with $m = n = 2$,
$k_{\text{SDR}} = C\phi^{4}T_2^{2}$ with $C = 4.0 \times 10^{-9}\ \mathrm{m^2\,s^{-3}}$,
$K = Q\ln(R/r_w)/(2\pi L\Delta h)$ (constant-head packer test), and
$z^{*} = k_{\text{th}}/(\rho_w c_w v_z)$ with $k_{\text{th}} = 2.0\ \mathrm{W\,m^{-1}\,K^{-1}}$
and $\rho_w c_w = 4.18 \times 10^{6}\ \mathrm{J\,m^{-3}\,K^{-1}}$.

## ★ Foundational

**★1.** A gamma log reads 45, 60 and 190 API in three units. Compute the clay volume
of each, state which is the most likely confining layer, and explain what the third
value means physically.

**★2.** Density logs give $\rho_b = 2130$, 2200 and 2450 kg m$^{-3}$. Compute the
three porosities and state which unit has the most pore volume.

**★3.** The NMR $T_2$ values are 85, 18 and 4 ms in the same three units. Using the
porosities from ★2, compute the SDR permeabilities in m d$^{-1}$ and state which
interval you would screen.

## ★★ Applied

**★★4.** The resistivity log reads 220, 95 and 18 $\Omega$ m with a water resistivity
of 5 $\Omega$ m, fixed by a sample. Compute the three water saturations from Archie
and explain, in terms of the physics of clay, why the third value is not a true
saturation and why its appearance is still diagnostic.

**★★5.** A constant-head packer test gives $Q = 0.08\ \mathrm{L\,s^{-1}}$ at
$\Delta h = 10$ m over $L = 3$ m, with $r_w = 75$ mm and an assumed
$R = 50$ m. Compute $K$ in m s$^{-1}$ and m d$^{-1}$, then recompute for $R = 10$ m
and $R = 200$ m. State the fractional error made by using the wrong radius of
influence and say what that implies for reporting the result.

**★★6.** A temperature log reads $T_0 = 12.0$ °C at the water table with a
background geothermal gradient of $0.025$ °C m$^{-1}$. Compute $z^{*}$ for a
downward Darcy velocity of $2 \times 10^{-8}$ m s$^{-1}$ (in m d$^{-1}$ too), the
temperature at 20 m and 50 m, and the gradient at 20 m. State how the log's
sensitivity compares with the gradient at zero flow.

## ★★★ Research-oriented

**★★★7.** A cross-hole programme must monitor both a water-content change and a
salinity change in a 12 m inter-borehole interval. Using the lesson's tables (a water
content change from 0.10 to 0.30 changes the velocity from 0.1160 to 0.0716 m ns$^{-1}$
and the travel time from 103.5 to 167.5 ns; a 5 000 mg L$^{-1}$ brine has
$\sigma_w = 0.75$ S m$^{-1}$ and 102.3 dB m$^{-1}$ attenuation at 50 MHz), compute the
percentage changes each effect produces in travel time and in amplitude, and state
which parameter each of the two measurements determines. Then explain why cross-hole
*radar* fails for salinity and name the two method families that work instead.

**★★★8.** The demonstration verifies the density-porosity inversion exactly
(2122.0 kg m$^{-3}$ → $\phi = 0.3200000000$), checks the temperature solution against
its ODE (relative residual $7.3 \times 10^{-7}$, limited by the second-order
difference) and checks that flowmeter increments are non-negative and sum to the
pumped rate (1.0%). State what each check verifies and what none of them can verify.
Then design a **validation** of the whole interpretation, naming the measurement and
what it would catch that the three checks cannot.
