# Exercises — 16-03-01 Global Circulation: Hadley, Ferrel, Polar Cells, Jets

Attempt these before reading the
[solutions](./01-global-circulation-solutions.md). The lesson is
[01 Global Circulation](../01-global-circulation.md). All models are
**SYNTHETIC** teaching values; use $\Omega = 7.292115\times10^{-5}\
\mathrm{rad\,s^{-1}}$, $a = 6.371\times10^6$ m, $g = 9.81\ \mathrm{m\,s^{-2}}$.

## ★ Foundational

**★1.** Compute $f = 2\Omega\sin\phi$ and the inertial period $2\pi/|f|$ at
$20^\circ$ and $70^\circ$. State the inertial period in hours.

**★2.** For a flow of speed $U = 15\ \mathrm{m\,s^{-1}}$ and horizontal scale
$L = 2\times10^6$ m, compute the Rossby number at $20^\circ$ and at $70^\circ$.
Which of the two is rotation-dominated, by the $\mathrm{Ro}<0.1$ criterion?

**★3.** Evaluate the angular-momentum-conserving wind
$u_M = \Omega a\sin^2\phi/\cos\phi$ at $\phi = 5^\circ$, $15^\circ$ and
$40^\circ$. State the unit and explain in one sentence why $u_M$ cannot be
believed at $40^\circ$.

## ★★ Applied

**★★4.** Derive $\mathrm{d}M/\mathrm{d}t = -a\cos\phi\,u/\tau$ from the zonal
momentum equation
$\partial_t u + (v/a)\partial_\phi u - (f + u\tan\phi/a)v = -u/\tau$,
showing explicitly how the Coriolis and curvature terms cancel. State what
$\mathrm{d}M/\mathrm{d}t$ reduces to when $\tau\to\infty$.

**★★5.** Use the quartic approximation
$\theta_t(\phi)-\theta_t(0) \approx -\theta_0\Omega^2a^2\phi^4/(gH)$ with
$\theta_0 = 300$ K and $H = 10$ km.
**(a)** Evaluate the drop at $10^\circ$, $20^\circ$ and $30^\circ$.
**(b)** Find the latitude at which the quartic form is in error by $5\%$
relative to the full bracket
$C(\ln\cos\phi + \sin^2\phi/2)$, with $C = 4\theta_0\Omega^2a^2/(gH)$.

**★★6.** A midlatitude jet of $U = 20\ \mathrm{m\,s^{-1}}$ occupies a column of
depth $10$ km and density $1.0\ \mathrm{kg\,m^{-3}}$, spun down by Rayleigh
friction on a $5$-day timescale. The Ferrel cell's surface branch is
$v = -1\ \mathrm{m\,s^{-1}}$ at $45^\circ$.
**(a)** Compute the friction drag per unit area.
**(b)** Compute the Coriolis torque per unit area.
**(c)** Compute the eddy momentum flux convergence required to maintain the jet,
and state its sign meaning.

## ★★★ Research-oriented

**★★★7.** Section 5 matches the conserved profile to a chosen equilibrium
profile. Instead of tuning $\Delta\theta_e$, suppose the equilibrium tropopause
potential temperature is itself uncertain by $20$ K over the tropics and the
tropopause height by $2$ km. Propagate both uncertainties to the cell-edge
latitude, state the resulting admitted range, and explain why the range is
narrower than the $10.9^\circ$–$22.6^\circ$ span of the demonstration's table.

**★★★8.** Section 6 computes the transport *required* by a prescribed net TOA
flux. Design a calculation that would partition that transport between a mean
meridional circulation and eddies using only quantities this lesson defines,
state the closure you must add, and say precisely what would have to be measured
to test it. A specification that could not be executed is a failed answer.
