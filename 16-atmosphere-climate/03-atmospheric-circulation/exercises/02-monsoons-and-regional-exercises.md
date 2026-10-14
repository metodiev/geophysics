# Exercises — 16-03-02 Monsoons, Regional Circulation and Teleconnections

Attempt these before reading the
[solutions](./02-monsoons-and-regional-solutions.md). The lesson is
[02 Monsoons, Regional Circulation and Teleconnections](../02-monsoons-and-regional.md).
All models are **SYNTHETIC** teaching values; use
$\Omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}}$,
$a = 6.371\times10^6$ m, and the lesson's forcing
$F_0 = 40\ \mathrm{W\,m^{-2}}$, $\lambda = 5.42\ \mathrm{W\,m^{-2}K^{-1}}$,
period 365 days.

## ★ Foundational

**★1.** A surface has effective heat capacity
$C = 5\times10^7\ \mathrm{J\,m^{-2}K^{-1}}$. Compute $C\omega$ (with
$\omega = 2\pi/(365\ \text{days})$), the amplitude of the annual temperature
cycle and the phase lag in days and in degrees.

**★2.** Compute the hydrostatic surface-pressure change for a uniform column
warming of $\Delta T = 3$ K with $p_s = 1.013\times10^5$ Pa and $T = 300$ K.
Give the answer in Pa and hPa, and state one reason the real value would be
smaller in magnitude.

**★3.** At $45^\circ$ with $U = 15\ \mathrm{m\,s^{-1}}$, compute $\beta$,
$K_s = \sqrt{\beta/U}$ and the stationary wavelength $2\pi/K_s$. Give units.

## ★★ Applied

**★★4.** Derive $\omega = \sqrt{b^2-a^2}$ and $\tau = \arccos(a/b)/\omega$
from the neutral conditions $a = b\cos\omega\tau$ and
$\omega = b\sin\omega\tau$. Then evaluate both for
$a = 0.004\ \mathrm{d^{-1}}$ and $b = 0.02\ \mathrm{d^{-1}}$, giving the period
in months and the delay in months.

**★★5.** A zonal wind stress of $\tau = 0.05\ \mathrm{N\,m^{-2}}$ tilts the
equatorial thermocline by 243.9 m over a 15 000 km basin.
**(a)** Show that a 50% increase in stress deepens the tilt by exactly 50%, and
give the new tilt.
**(b)** State the two assumptions in
$g'\,\partial h/\partial x = \tau/(\rho_0 H)$ that you used, and what would
change if the layer depth $H$ were 50 m instead of 150 m.

**★★6.** On a synthetic 40-year annual record with lag-1 autocorrelation
$\phi = 0.6$, a study reports $r = 0.42$. Using the lesson's AR(1) null
(5% threshold $\lvert r\rvert = 0.432$) and the white-noise threshold
$2/\sqrt{n}$:
**(a)** compute the white-noise threshold;
**(b)** state whether $r = 0.42$ passes each test;
**(c)** explain in two sentences why the thresholds differ.

## ★★★ Research-oriented

**★★★7.** A colleague argues that because the delayed oscillator reproduces a
4-year ENSO period, ENSO must be a delayed oscillator. Construct the strongest
version of the counter-argument using only quantities in this lesson, including
at least one that the model does *not* predict, and state one observation that
would discriminate between a delayed oscillator and an alternative mechanism.

**★★★8.** Design a study to test whether a regional monsoon anomaly is caused
by a remote teleconnection. Specify the index definitions, the null model, the
lag structure, the number of degrees of freedom you would claim, and the
evidence that would distinguish a true teleconnection from a common external
driver. A specification that could not be executed is a failed answer.
