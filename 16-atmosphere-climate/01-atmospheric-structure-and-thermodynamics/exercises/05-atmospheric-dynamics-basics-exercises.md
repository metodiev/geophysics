# Exercises — 16-01-05 Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind

Attempt these before reading the
[solutions](./05-atmospheric-dynamics-basics-solutions.md). The lesson is
[05 Atmospheric Dynamics](../05-atmospheric-dynamics-basics.md). Use
$\Omega = 7.2921150\times10^{-5}\ \mathrm{rad\,s^{-1}}$,
$g = 9.80665\ \mathrm{m\,s^{-2}}$ and
$R_d = 287.041\ \mathrm{J\,kg^{-1}\,K^{-1}}$. All models are **SYNTHETIC**.

## ★ Foundational

**★1.** Compute $f = 2\Omega\sin\phi$ at $20^\circ$, $45^\circ$ and $60^\circ$,
and for each compute $1/f$ and $2\pi/f$ in hours. State in one sentence the
difference in meaning between the two timescales.

**★2.** At $45^\circ\mathrm{N}$ with $\rho = 1.2\ \mathrm{kg\,m^{-3}}$, compute the
geostrophic wind for a pressure gradient of $2\ \mathrm{hPa}$ per $200\ \mathrm{km}$
directed northward (pressure rising to the north). Give the magnitude, the sign of
$u_g$, and the compass direction.

**★3.** Compute the Rossby number for $U = 15\ \mathrm{m\,s^{-1}}$ and
$L = 800\ \mathrm{km}$ at $45^\circ$ and at $15^\circ$, and state for each whether
the geostrophic approximation is adequate.

**★4.** Compute the thermal-wind shear $\partial u_g/\partial z$ for
$\partial T/\partial y = +2\ \mathrm{K}$ per $100\ \mathrm{km}$ at $30^\circ$ with
$T = 290\ \mathrm{K}$, and state whether the westerly increases or decreases with
height. Explain in one sentence why the tropics differ from the mid-latitudes.

## ★★ Applied

**★★5.** Derive geostrophic balance from the horizontal momentum equation by scale
analysis, showing explicitly that the ratio of the acceleration to the Coriolis term
is $\mathrm{Ro}$. Then write the gradient-wind balance for a circular vortex,
$u^2/R + fu = fu_g$, solve it for $u$ as a function of $R$ and $u_g$, and evaluate
it for $u_g = 10\ \mathrm{m\,s^{-1}}$ at $45^\circ$ with $\mathrm{Ro} = 0.2$.

**★★6.** Derive the thermal wind relation in both pressure coordinates
($\partial u_g/\partial p$) and height coordinates
($\partial u_g/\partial z$), stating each step and each assumption used. Show that
$(g/T)\,\mathrm{d}z = -R_d\,\mathrm{d}\ln p$ and explain what that identity implies
about the independence of the thermal-wind integral from geostrophic balance.

**★★7.** For a pure inertial oscillation with $U = 10\ \mathrm{m\,s^{-1}}$ at
$45^\circ$, compute the period, the radius of the circle in the hodograph, and the
actual distance the air travels in one period. Then explain why the speed is
constant and why the path is a circle rather than a spiral.

**★★8.** A jet has a westerly wind of $10\ \mathrm{m\,s^{-1}}$ at
$850\ \mathrm{hPa}$ and $45\ \mathrm{m\,s^{-1}}$ at $300\ \mathrm{hPa}$
(geometric thickness $7.71\ \mathrm{km}$). Infer the layer-mean meridional
temperature gradient at $T = 265\ \mathrm{K}$, in $\mathrm{K}$ per $100\ \mathrm{km}$,
and state its sign. State the two assumptions that dominate the uncertainty in your
answer.

## ★★★ Research-oriented

**★★★9.** Design an observational test of geostrophic balance at synoptic scales.
Specify: the wind measurement you would use and why it is independent of the
pressure analysis, the metric (rms vector difference normalised by the
geostrophic wind speed, and the angle between the observed and geostrophic winds),
the expected departure in the free troposphere versus the boundary layer, and two
confounders that would produce an apparent failure of the balance without any real
failure. State what result would falsify the approximation at $\mathrm{Ro} \ll 1$.

**★★★10.** In §3.5 and Example 3 the lesson argues that the thermal-wind integral
is a consistency check rather than an independent test. Construct a genuinely
independent test of the thermal-wind relation that does *not* rely on
differentiating a pressure or geopotential field — for example using a measured
temperature gradient, a measured wind shear, and an independent constraint from
mass continuity. State clearly which quantity is measured and which is inferred,
and what the test would detect that the consistency check cannot.

**★★★11.** Design a numerical experiment that measures the period of a pure
inertial oscillation as a function of the time step $\Delta t$ for a fourth-order
Runge–Kutta scheme, at latitudes from $10^\circ$ to $80^\circ$. Predict the
scaling of the period error with $\Delta t$ *before* running it, predict how the
error depends on latitude, and state what would falsify your prediction. Note that
the measured quantity here is a numerical artefact, so say explicitly what the
experiment is *for*.
