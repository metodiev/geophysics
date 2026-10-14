# Exercises — 07-06-01 Solid Earth Tides and Their Gravity Signature

Attempt these before reading the
[solutions](./01-solid-earth-tides-solutions.md). The lesson is
[01 Solid Earth Tides](../01-solid-earth-tides.md). **All models and data in this
module are SYNTHETIC.**

Constants used throughout: $\omega = 7.2921150\times10^{-5}\
\mathrm{rad\,s^{-1}}$, sidereal month $= 27.321661\ \mathrm{d}$, tropical year
$= 365.2422\ \mathrm{d}$, $\mathrm{GM}_{\odot} = 1.32712440018\times10^{20}\
\mathrm{m^{3}\,s^{-2}}$, $\mathrm{GM}_{\text{Moon}} = 4.902800118\times10^{12}\
\mathrm{m^{3}\,s^{-2}}$, $R = 6371\ \mathrm{km}$,
$d_{\text{Moon}} = 3.844\times10^{8}\ \mathrm{m}$, $1\ \mathrm{AU} =
1.495978707\times10^{11}\ \mathrm{m}$, $h_2 = 0.6090$, $k_2 = 0.3040$.

## ★ Foundational

**★1.** Compute the ratio of the tidal forcing of the Sun to that of the Moon
from $\mathrm{GM}_b/d^{3}$, showing the arithmetic. Then state the ratio for a
hypothetical body with the Moon's mass at twice the Moon's distance.

**★2.** Compute the O1 frequency from $\omega$ and the Moon's mean motion, give
its period in hours, and compare with the sidereal day.

**★3.** Using $h_2 = 0.6078$ and $k_2 = 0.2990$ (an alternative stated set),
compute $\delta$ and state the percentage change in a predicted M2 amplitude
relative to $\delta = 1.1530$.

## ★★ Applied

**★★4.** Verify the identity behind S2: show, in cycles per mean solar day, that
$2(\omega - n_s) = 2$ exactly, using the relation between the solar and sidereal
rates. State in one sentence why this is a check on the rates rather than an
independent fact.

**★★5.** A record is 10 days long. Using the Rayleigh criterion, decide which of
the pairs (M2, S2), (K1, O1) and (M2, K2) can be separated, and state what a
least-squares fit will do if you ask it to separate a pair that cannot be.

**★★6.** A gravimeter at the equator records an M2 amplitude of
$83.87\ \mathrm{\mu Gal}$ in the synthetic model, whereas the analytic
"body in the equatorial plane" value is $95.11\ \mathrm{\mu Gal}$. Explain the
difference quantitatively, and state what additional information you would need
to predict the observed amplitude exactly.

## ★★★ Research-oriented

**★★★7.** Design a synthetic experiment that measures how a $10\%$ error in an
ocean-load model contaminates a fitted M2 amplitude at a coastal station.
Specify the synthetic body tide, the load tide, the noise, the analysis, the
diagnostic and the prediction. State what the same experiment cannot establish.

**★★★8.** The demonstration's model omits the Moon's orbital eccentricity and
the regression of its node. For each omission, state (i) which additional
frequencies it would introduce, and (ii) how large an amplitude error it would
cause in a fitted M2 amplitude from a 60-day record if the omitted effect were
$5\%$ of the lunar tide. A quantitative estimate, however rough, is required.
