# Exercises — 16-01-02 Hydrostatic Balance and Pressure-Height Relations

Attempt these before reading the
[solutions](./02-hydrostatic-balance-solutions.md). The lesson is
[02 Hydrostatic Balance](../02-hydrostatic-balance.md). Use
$R_d = 287.041\ \mathrm{J\,kg^{-1}\,K^{-1}}$ and
$g_0 = 9.80665\ \mathrm{m\,s^{-2}}$ throughout; all models are **SYNTHETIC**.

## ★ Foundational

**★1.** Compute the thickness sensitivity coefficient
$K = (R_d/g_0)\ln(p_1/p_2)$ for the layers $1000\text{–}850\ \mathrm{hPa}$,
$850\text{–}700\ \mathrm{hPa}$ and $500\text{–}200\ \mathrm{hPa}$, in
$\mathrm{m\,K^{-1}}$. State the units of the logarithm.

**★2.** A layer between $1000$ and $850\ \mathrm{hPa}$ has a mean temperature of
$285\ \mathrm{K}$. Compute its thickness. Then compute the thickness if the mean
temperature were $283\ \mathrm{K}$, and state the difference in metres.

**★3.** A synthetic radiosonde reports a $1000\text{–}500\ \mathrm{hPa}$ thickness
of $5400\ \mathrm{m}$. Compute the layer-mean temperature in kelvin and in degrees
Celsius.

**★4.** Compute the geopotential height $Z$ corresponding to geometric heights of
$3$, $8$ and $15\ \mathrm{km}$ using $Z = zR_E/(R_E+z)$ with
$R_E = 6.371\times10^{6}\ \mathrm{m}$, and state $Z-z$ in metres for each.

## ★★ Applied

**★5.** Derive $\partial \Phi/\partial p = -1/\rho$ from hydrostatic balance and
the definition of geopotential, showing each step. Then, for the layer of ★2 (take
its bottom at $z = 111\ \mathrm{m}$ and its top at the bottom plus the geometric
thickness), compute the geometric thickness and the geopotential thickness, and
state the difference in metres and as a percentage of the layer.

**★6.** For the $1000\text{–}850\ \mathrm{hPa}$ layer of ★1, a temperature sensor
has a $+0.4\ \mathrm{K}$ bias (it reads warm). Compute the thickness error it
produces. Then compute the temperature error to which a fixed thickness
uncertainty of $5\ \mathrm{m}$ corresponds in that layer and in the
$500\text{–}200\ \mathrm{hPa}$ layer, and comment on which layer is more
sensitive to bias *in metres* and which *in kelvin*.

**★7.** Show that the fractional thickness error equals the fractional
temperature error, $\delta(\Delta Z)/\Delta Z = \delta\bar T/\bar T$, by
differentiating the hypsometric equation at fixed pressure levels. Use it to
predict the fractional thickness error for a $2\ \mathrm{K}$ error on a
$270\ \mathrm{K}$ layer, then verify your prediction numerically.

**★8.** A pressure measurement has an absolute accuracy of $0.5\ \mathrm{hPa}$.
Convert that to a column-mass accuracy in $\mathrm{kg\,m^{-2}}$, and to a height
accuracy at sea level using the isothermal model with $T = 288.15\ \mathrm{K}$
and scale height $H = 8.4342\ \mathrm{km}$ (take
$\mathrm{d}Z = H\,\mathrm{d}p/p$).

## ★★★ Research-oriented

**★★★9.** Hydrostatic balance fails by a fraction $|a_z|/g$. Construct an error
budget for a synthetic sounding taken in a strong updraught $(a_z = 0.2\
\mathrm{m\,s^{-2}})$ and in a quiescent column $(a_z = 10^{-5}\
\mathrm{m\,s^{-2}})$, and compare the non-hydrostatic pressure error with (i) the
sensor accuracy of ★8 and (ii) the temperature-induced thickness error of ★6.
State the scale at which non-hydrostatic effects become the *dominant* term in
the pressure measurement, and the measurement that would detect them.

**★★★10.** The hypsometric equation is exact for $\bar T$ *as defined*, yet
different organisations report slightly different layer temperatures from the
same radiosonde. Enumerate at least four distinct causes, classify each as
physical, definitional, or numerical, and say which of them could be resolved by
better instruments and which cannot in principle. Do not invent values; argue
from the structure of the equation.

**★★★11.** You are asked to design a satellite-based thickness measurement that
must detect a $0.5\ \mathrm{K}$ change in a $1000\text{–}500\ \mathrm{hPa}$ layer
mean over ten years. Specify: (a) the required thickness accuracy in metres,
(b) two independent error sources that scale differently with averaging time, and
(c) one confounder that a static (non-time-varying) correction cannot remove.
State your assumptions explicitly, and do not assert any instrument performance
figure you cannot derive from the constants given.
