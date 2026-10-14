# Exercises — 14-02-03 Seismic Methods for Aquifer Geometry

Attempt these before reading the
[solutions](./03-seismic-hydrogeophysics-solutions.md). The lesson is
[03 Seismic Methods for Aquifer Geometry](../03-seismic-hydrogeophysics.md). All
models are **SYNTHETIC**.

Use
$R = (Z_2-Z_1)/(Z_2+Z_1)$ with $Z = \rho v_p$;
$d = v\,\mathrm{TWT}/2$;
$x_{\text{cross}} = 2h\sqrt{(v_2+v_1)/(v_2-v_1)}$;
$t_i = 2h\sqrt{v_2^{2}-v_1^{2}}/(v_1v_2)$; $\lambda = v/f$.

## ★ Foundational

**★1.** Compute the reflection coefficient at a water table where the unsaturated
zone has $v_p = 900\ \mathrm{m\,s^{-1}}$, $\rho = 1800\ \mathrm{kg\,m^{-3}}$ and
the saturated aquifer has $v_p = 1700\ \mathrm{m\,s^{-1}}$,
$\rho = 2050\ \mathrm{kg\,m^{-3}}$. State the polarity convention for a positive
$R$.

**★2.** Compute the wavelength and the quarter-wavelength resolution limit for a
100 Hz source in a medium of $v_p = 1500\ \mathrm{m\,s^{-1}}$.

**★3.** Compute the refraction crossover distance for a saturated layer at 8 m
depth with a dry cover of $500\ \mathrm{m\,s^{-1}}$ over a saturated layer of
$1500\ \mathrm{m\,s^{-1}}$.

## ★★ Applied

**★★4.** Using the lesson's tuning table (60 Hz, $v_p^{\text{sat}} = 1650\
\mathrm{m\,s^{-1}}$, peak response 0.183 at 0.5 m, 0.361 at 1.0 m, 0.853 at 2.0 m,
1.409 at 6.0 m, 1.000 at and above 20 m), estimate the thickness that gives (i) half
the tuning peak, (ii) response equal to 20% of the thick-layer value, and (iii) the
thinnest aquifer whose thickness can be read from travel time. State the
interpolation you used and its justification.

**★★5.** A three-layer synthetic structure has $v_1 = 400\ \mathrm{m\,s^{-1}}$ over
the top 2 m, $v_2 = 1200\ \mathrm{m\,s^{-1}}$, and $v_3 = 2000\
\mathrm{m\,s^{-1}}$ below. Derive the maximum thickness of layer 2 for which its
refracted arrival is never the first arrival anywhere on the array, evaluate it, and
state the spread length at which the layer becomes visible.

**★★6.** A two-way time of 30 ms is picked to a marker. Compute the depth error
introduced by using $1500\ \mathrm{m\,s^{-1}}$ instead of the correct
$1800\ \mathrm{m\,s^{-1}}$, and state in one sentence why the error is not a
"small" one in an aquifer context.

## ★★★ Research-oriented

**★★★7.** Design a combined seismic, GPR and borehole programme to map a 3 m thick
aquifer at 15 m depth to $\pm 0.5$ m and to report its water content to $\pm 0.02$.
Give the arithmetic of each choice (spread length, source frequency, GPR antenna
frequency, number of boreholes), an error budget for the depth, and state precisely
which measurement breaks the time-to-depth circularity and which does not.

**★★★8.** Write a verification *and* validation plan for (a) a reflection modelling
code and (b) the $v_p(S_w)$ relation used to interpret it. For (a), include an
analytic check, a tuning-curve check and a convergence measurement. For (b), state
what would be required to establish the relation empirically, why a code test
cannot do it, and what the consequence is for any hydrological interpretation that
depends on it. Finish by ranking seismic, ERT and GPR for (i) resolving the water
table, (ii) resolving a clay layer's base, and (iii) measuring water content, with
one number in support of each ranking.
