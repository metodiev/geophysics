# Exercises — 11-03-01 Reflection Seismic in Exploration: From 2-D to 3-D

Attempt these before reading the
[solutions](./01-seismic-in-exploration-solutions.md). The lesson is
[01 Reflection Seismic in Exploration](../01-seismic-in-exploration.md). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A survey in a $3.40\ \mathrm{km\,s^{-1}}$ medium images 40 Hz data.
Compute the wavelength, the $\lambda/4$ limit and the period. Repeat for
$v = 2.60\ \mathrm{km\,s^{-1}}$ — a shallow, low-velocity section.

**★2.** Compute the first Fresnel zone radius at 1.5 km and at 3.0 km depth for
$\lambda = 85\ \mathrm{m}$. State the unit and show the square root's argument.

**★3.** A dipping event has 25° dip and the trace interval is 30 m. At what
frequency does it alias, for $v = 3.0\ \mathrm{km\,s^{-1}}$? Show the
dimensional check.

## ★★ Applied

**★★4.** A 3-D survey is designed with receivers every 25 m on lines spaced
250 m, with 9 receiver lines, maximum offsets $\pm2.5$ km inline and $\pm1.0$
km crossline; sources every 40 m on lines every 240 m; bin $25\times25$ m.
Compute $\sigma_s$, $\sigma_r$, the live traces per source $T$ (continuum and
discrete), the fold, and the expected random-noise gain. State why the
continuum and discrete answers differ.

**★★5.** Using the demonstration's side-swipe relation, compute the apparent
depth and the percentage error for a reflector at 1800 m depth that is 900 m
out of plane. If the true vertical resolution is 21 m, decide whether the
side-swipe error or the resolution limit dominates the interpretation, and
justify the answer with numbers.

**★★6.** A target is 18 m thick at 2.8 km depth in a 3.1 km/s rock. The deepest
useful frequency is 45 Hz. Decide whether the target is resolvable, and state
what acquisition change (if any) would make it so; if no change would, say so
and explain why.

## ★★★ Research-oriented

**★★★7.** Design an acquisition for a stated target of your own choosing
(state the depth, velocity, dip, target thickness and noise requirement).
Report: bin size from the alias relation, fold and its continuum-versus-discrete
values, the expected stacking gain, the Fresnel radius, and the one limit you
expect to bind first. Your answer must contain numbers that a reviewer could
check.

**★★★8.** Derive the trace-density expression for 3-D fold from the Jacobian of
the mapping $(s,r)\to(m,h)$, and state the condition under which the discrete
count and the continuum rule differ by more than 10%. Compute that condition
for the geometry of ★★4 and verify your prediction numerically by counting
midpoints (a short script is acceptable).
