# Exercises — 15-03-01 Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems

Attempt these before reading the
[solutions](./01-mid-ocean-ridges-solutions.md). The lesson is
[01 Mid-Ocean Ridges](../01-mid-ocean-ridges.md). All models and data are
**SYNTHETIC** teaching values; the material constants used are those stated in
the lesson and printed by `code/mid_ocean_ridges_demo.py`.

## ★ Foundational

**★1.** Compute the depth of the seafloor for crust of age 1, 4, 9, 16 and
25 Myr using $d=2500+373.2\sqrt{t}$ (metres, $t$ in Myr). State the depth
difference between 4 and 9 Myr and explain in one sentence why the subsidence
between equal age increments shrinks.

**★2.** Using $q=kT_m/\sqrt{\pi\kappa t}$ with $kT_m=4320$ and
$\pi\kappa=3.1416\times10^{-6}$, compute $q$ at 1, 4, 16 and 64 Ma, and verify
that each quadrupling of age halves $q$ (equivalently, each doubling divides it by
$\sqrt{2}$). Give the answer in $\mathrm{mW\,m^{-2}}$.

**★3.** State the unit of permeability and convert $5\times10^{-15}\ \mathrm{m^2}$
to millidarcies using $1\ \mathrm{mD}=9.869\times10^{-16}\ \mathrm{m^2}$.

## ★★ Applied

**★★4.** A ridge has a half-spreading rate of $3\ \mathrm{cm\,yr^{-1}}$. At what
distance from the axis is the crust 5 Myr old? Use the $600\ ^\circ\mathrm{C}$
erf solution of the lesson to compute the depth of the brittle–ductile transition
there, and state how the answer changes if the half-rate is $9\ \mathrm{cm\,yr^{-1}}$.

**★★5.** The demonstration reports $\mathrm{Ra}=50.5$ at $k=10^{-14}\ \mathrm{m^2}$
for $H=1000\ \mathrm{m}$, $\Delta T=200\ \mathrm{K}$, $\mu=2\times10^{-4}\ \mathrm{Pa\,s}$.
Recompute $\mathrm{Ra}$ for $\mu=5\times10^{-4}\ \mathrm{Pa\,s}$ (a colder-fluid
value) and for $\Delta T=400\ \mathrm{K}$, and state which of the two changes
moves the system across the onset threshold.

**★★6.** Using the lesson's heat-budget numbers
($\int_0^{10\,\mathrm{Ma}}q\,\mathrm{d}t=8.659\times10^{13}\ \mathrm{J\,m^{-2}}$,
$\rho=1030\ \mathrm{kg\,m^{-3}}$, $c_p=5000\ \mathrm{J\,kg^{-1}\,K^{-1}}$),
compute the required water volume per square metre for $\Delta T=350\ \mathrm{K}$
and $f=0.30$, then for $f=0.10$. Convert the first to an average Darcy flux in
$\mathrm{mm\,yr^{-1}}$ and state the assumption that makes it an average rather
than a local flux.

## ★★★ Research-oriented

**★★★7.** The lesson's subsidence coefficient $373.2\ \mathrm{m\,(Myr)^{-1/2}}$
comes from $\alpha_v=3\times10^{-5}\ \mathrm{K^{-1}}$, $T_m=1350\ \mathrm{K}$,
$\kappa=10^{-6}\ \mathrm{m^2\,s^{-1}}$, $\rho_m=3300$ and $\rho_w=1030$. Construct
the error budget: find the fractional change in $a$ produced by a 10% change in
each of the five constants in turn, rank them, and state which two an analyst
must fix before the others can be tested against data. Explain why the ranking
itself is a model result and not a measurement.

**★★★8.** Design a synthetic experiment that separates "the young-crust heat-flow
deficit is caused by hydrothermal circulation" from "the deficit is caused by a
crustal thermal conductivity lower than $3.2\ \mathrm{W\,m^{-1}\,K^{-1}}$". State
the observable you would measure, the prediction of each hypothesis, the
discriminating measurement, the noise level you would need, and the specific
model assumption that would still be untested after your experiment. A
specification that could not be executed is a failed answer.
