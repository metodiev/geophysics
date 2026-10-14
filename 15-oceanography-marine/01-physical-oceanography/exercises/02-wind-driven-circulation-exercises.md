# Exercises — 15-01-02 Wind-Driven Circulation, Ekman Transport and Gyres

Attempt these before reading the
[solutions](./02-wind-driven-circulation-solutions.md). The lesson is
[02 Wind-Driven Circulation](../02-wind-driven-circulation.md). All models are
**SYNTHETIC** teaching values.

Constants: $\Omega = 7.292115\times10^{-5}\ \mathrm{s^{-1}}$,
$R = 6.371\times10^{6}\ \mathrm{m}$, $\rho = 1025\ \mathrm{kg\,m^{-3}}$,
$1^\circ$ of latitude $= 111.19\ \mathrm{km}$, $1\ \mathrm{Sv} = 10^{6}\
\mathrm{m^{3}\,s^{-1}}$.

## ★ Foundational

**★1.** Compute $f = 2\Omega\sin\phi$ and $\beta = 2\Omega\cos\phi/R$ at
$25^\circ$S. Give the units, and state the sign of each. What is the inertial
period there?

**★2.** A wind stress of $\tau = 0.15\ \mathrm{N\,m^{-2}}$ blows eastward at
$35^\circ$N. Compute the depth-integrated Ekman transport in
$\mathrm{m^{2}\,s^{-1}}$, state its direction, and give the transport across a
$500\ \mathrm{km}$ stretch of coast in Sv.

**★3.** Show by dimensional analysis that $\tau/(\rho f)$ has units of
$\mathrm{m^{2}\,s^{-1}}$ and explain in one sentence what "depth-integrated"
means.

## ★★ Applied

**★★4.** Take the synthetic wind of the lesson,
$\tau_x(y) = \tau_0\cos(\pi y/L)$ with $\tau_0 = 0.10\ \mathrm{N\,m^{-2}}$,
$L = 3000\ \mathrm{km}$, $\tau_y = 0$. (a) Write $\mathrm{curl}_z\boldsymbol{\tau}$
and evaluate it at $y = 750\ \mathrm{km}$. (b) Compute the Sverdrup transport at
that latitude using $\beta$ at $30^\circ$N. (c) Convert to a transport across a
$5000\ \mathrm{km}$ basin, in Sv. (d) State the latitude at which the interior
flow reverses and say why.

**★★5.** Using the curl of ★★4(a) and $f = 7.292\times10^{-5}\ \mathrm{s^{-1}}$,
compute the Ekman pumping velocity $w_E = \mathrm{curl}_z(\boldsymbol{\tau}/\rho
f)$ in $\mathrm{m\,s^{-1}}$ and in $\mathrm{m\,yr^{-1}}$. State the sign and
whether the thermocline is displaced upward or downward.

**★★6.** At $45^\circ$N with $A_v = 0.010\ \mathrm{m^{2}\,s^{-1}}$ the lesson
gives $D = 13.93\ \mathrm{m}$ and $V_0 = 0.0961\ \mathrm{m\,s^{-1}}$. (a) Compute
$D$ and $V_0$ for $A_v = 0.040\ \mathrm{m^{2}\,s^{-1}}$. (b) Compute the Ekman
transport in both cases and comment on which quantity is robust.

**★★7.** The lesson measures a $\beta$-plane error of
$2.286\times10^{-6}\ \mathrm{s^{-1}}$ over $\pm1500\ \mathrm{km}$ about
$30^\circ$N. Compute the corresponding error over $\pm2500\ \mathrm{km}$ and
express it as a percentage of $f_0$ and as a percentage error in Ekman
transport.

## ★★★ Research-oriented

**★★★8.** Design an observational test of the Sverdrup balance in a synthetic
basin of your choosing. State (a) the quantity you would measure and how,
(b) the quantity you would infer, (c) the error budget, and (d) which term of
the balance you expect to be violated first at the basin's eastern margin.
Justify (d) with a number. A specification that could not be executed is a
failed answer.

**★★★9.** The western-boundary width is $\delta = r/\beta$ (Stommel) or
$\delta = (A_H/\beta)^{1/3}$ (Munk), while the interior transport is independent
of both $r$ and $A_H$. Write a short argument explaining *why* the vorticity
budget constrains the interior but not the boundary layer, and state one
observable that would discriminate between the two closures.
