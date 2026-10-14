# Solutions — 15-03-01 Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems

> **Read after attempting the exercises.** Numbers were computed with the
> constants of the lesson; where a problem has more than one defensible answer
> that is said so. Lesson: [01 Mid-Ocean Ridges](../01-mid-ocean-ridges.md).

## ★ Foundational

## ★1 — Depth versus age

$d=2500+373.2\sqrt{t}$ with $t$ in Myr:

| $t$ (Myr) | $\sqrt{t}$ | $d$ (m) |
|---|---|---|
| 1 | 1.000 | 2873 |
| 4 | 2.000 | 3246 |
| 9 | 3.000 | 3620 |
| 16 | 4.000 | 3993 |
| 25 | 5.000 | 4366 |

Depth difference 4→9 Myr: $3620-3246=374\ \mathrm{m}$. The subsidence between
equal age increments shrinks because it is proportional to
$\sqrt{t_2}-\sqrt{t_1}$, and the square root flattens: the same 5 Myr buys
374 m at 4→9 Myr but only 190 m at 16→25 Myr ($4366-3993$).

## ★2 — Heat flow versus age

$q = 4320/\sqrt{3.1416\times10^{-6}\,t}$ with $t$ in seconds; converting the age
to Myr, $t=3.15576\times10^{13}\,t_{\mathrm{Myr}}$, so

$$q\,[\mathrm{mW\,m^{-2}}]=\frac{4320\times10^{3}}{\sqrt{3.1416\times10^{-6}\times3.15576\times10^{13}\,t_{\mathrm{Myr}}}}
=\frac{433.9}{\sqrt{t_{\mathrm{Myr}}}} .$$

| $t$ (Myr) | $q$ (mW/m²) |
|---|---|
| 1 | 433.9 |
| 4 | 216.9 |
| 16 | 108.5 |
| 64 | 54.2 |

Each quadrupling of age (1→4→16→64) halves $q$, because
$1/\sqrt{4}=0.5000$; each doubling divides $q$ by $\sqrt{2}=0.7071$, so
$q(2\ \mathrm{Myr})=433.9\times0.7071=306.8\ \mathrm{mW\,m^{-2}}$. The value
$433.9\ \mathrm{mW\,m^{-2}}$ at 1 Ma is the lesson's
$0.4339\ \mathrm{W\,m^{-2}}$ and the $1372\ \mathrm{mW\,m^{-2}}$ printed by the
demonstration is the same formula at 0.1 Ma. ✔

## ★3 — Permeability units

Permeability has units of area, $\mathrm{m^2}$.
$5\times10^{-15}/9.869\times10^{-16}=5.07\ \mathrm{mD}$.

## ★★ Applied

## ★4 — Distance, age and the brittle–ductile transition

Age: $t=x/u$, so $x=u\,t=0.03\ \mathrm{m\,yr^{-1}}\times5\times10^{6}\ \mathrm{yr}
=1.5\times10^{5}\ \mathrm{m}=150\ \mathrm{km}$.

$z_{600}=0.83362\sqrt{\kappa t}$ with
$t=5\times10^{6}\times3.15576\times10^{7}=1.578\times10^{14}\ \mathrm{s}$:

$$\kappa t = 10^{-6}\times1.578\times10^{14}=1.578\times10^{8},\quad
\sqrt{\kappa t}=12\,562\ \mathrm{m},$$
$$z_{600}=0.83362\times12\,562=10\,472\ \mathrm{m}.$$

This is *larger* than the crustal thickness (~6 km), which means the whole crust
at 150 km from a slow ridge stays cooler than $600\ ^\circ\mathrm{C}$: the model
predicts brittle behaviour to the Moho. At that distance from the axis the
half-space assumption is no longer a good description of a ridge flank (the plate
is not being fed heat from below and radiogenic heating is not negligible), so
the number should be read as an upper bound on the brittle-layer thickness. At
$9\ \mathrm{cm\,yr^{-1}}$ the crust reaches
5 Myr at 450 km, and the age at a *fixed* 150 km distance becomes 1.67 Myr, giving
$\sqrt{\kappa t}=7\,258\ \mathrm{m}$ and $z_{600}=6050\ \mathrm{m}$: the
transition is at the base of the crust instead of far below it. The physical
statement is that the brittle layer thins both with distance from the axis and
with increasing spreading rate.

## ★5 — Changing $\mu$ and $\Delta T$

$\mathrm{Ra}\propto\Delta T/\mu$; the base case is $50.5$.

- $\mu=5\times10^{-4}\ \mathrm{Pa\,s}$: $\mathrm{Ra}=50.5\times(2/5)=20.2$,
  below $\mathrm{Ra}_c=39.478$ → conductive.
- $\Delta T=400\ \mathrm{K}$: $\mathrm{Ra}=50.5\times2=101.0$, above onset →
  convecting, $\mathrm{Ra}/\mathrm{Ra}_c=2.56$.

The viscosity change moves the system out of convection, the temperature change
deeper into it. Since $\mathrm{Ra}\propto\Delta T/\mu$ and both changes have the
same fractional size (a factor 2.5 versus a factor 2), the ranking is
$\Delta T$ (×2) then $\mu$ (÷2.5), so the viscosity change is the larger lever
per unit fractional change.

## ★6 — Heat budget to water volume

Per square metre:
$V=f\times8.659\times10^{13}/(1030\times5000\times350)
=f\times4.802\times10^{4}\ \mathrm{m^3\,m^{-2}}$.

- $f=0.30$: $V=1.441\times10^{4}\ \mathrm{m^3\,m^{-2}}$, a column of 14 412 m
  (the demonstration's value — the algebra and the code agree).
- $f=0.10$: $V=4.802\times10^{3}\ \mathrm{m^3\,m^{-2}}$, a column of 4802 m.

Average Darcy flux: $V/t_1$ with $t_1=10\ \mathrm{Myr}=3.15576\times10^{14}\ \mathrm{s}$:

$$1.441\times10^{4}/3.15576\times10^{14}
=4.567\times10^{-11}\ \mathrm{m\,s^{-1}},$$

$$\times10^{3}\ \mathrm{mm\,m^{-1}}\times3.15576\times10^{7}\ \mathrm{s\,yr^{-1}}
=1.44\ \mathrm{mm\,yr^{-1}}.$$

It is an *average* because the integration has already destroyed all information
about where and when the flow happened: real circulation is focused along faults
and vents, and a local flux can exceed the mean by orders of magnitude. The
conversion to a local flux is not possible from a heat budget alone.

## ★★★ Research-oriented

## ★7 — Error budget for $a$

$a=\dfrac{\rho_m}{\rho_m-\rho_w}\alpha_vT_m2\sqrt{\kappa/\pi}$
(dropping the unit conversion to Myr, which is a constant). Sensitivities to a
+10% change:

| constant | role | $\delta a/a$ for $+10\%$ | sign |
|---|---|---|---|
| $\alpha_v$ | linear | $+10\%$ | + |
| $T_m$ | linear | $+10\%$ | + |
| $\kappa$ | $\sqrt{\kappa}$ | $+(1.1)^{1/2}-1=+4.9\%$ | + |
| $\rho_w$ | $\rho_m/(\rho_m-\rho_w)$ | $1.522843/1.453744-1=+4.8\%$ | + |
| $\rho_m$ | $\rho_m/(\rho_m-\rho_w)$ | $1.396154/1.453744-1=-4.0\%$ | − |

Ranking: $T_m=\alpha_v>\kappa>\rho_w>\rho_m$. The two constants to fix first are
$T_m$ and $\alpha_v$: each moves $a$ one-for-one with its own error. $\rho_m$ is
the least important because it appears in a ratio close to 1 whose numerator and
denominator both change.

The ranking is a model result, not a measurement: it is the sensitivity of
$a(\text{model})$ to its parameters, computed by differentiating the formula. It
says nothing about how well $T_m$ or $\alpha_v$ are known, which is a separate
(and in $\alpha_v$'s case, difficult) question. A sensitivity analysis constrains
the *interpretation* of a measurement; it does not substitute for the
measurement.

## ★8 — Separating hydrothermal advection from a low conductivity

**Observable:** the surface heat flow $q_{\text{obs}}(t)$ as a function of crustal
age, together with the *depth* at which the conductive gradient is measured
(probe penetration and the temperature profile above it, not just the gradient).

**Prediction of H1 (hydrothermal circulation):** the deficit is confined to young,
permeable crust and disappears as alteration seals the crust; the *shape* of the
deficit is an increasing function of permeability and is spatially patchy at
scales of kilometres; the conductive gradient at depth is normal while the
surface flow is low, so the profile is non-linear (concave) with depth.

**Prediction of H2 (low $k$):** the deficit is uniform in age, spatially smooth,
and the measured gradient is linear with depth; $q_{\text{obs}}/q_{\text{model}}$
is constant.

**Discriminating measurement:** a temperature profile to several hundred metres
below the seafloor in a sedimented young-crust location. H1 predicts a
depth-dependent gradient (heat is being mined from the section, not just
conducted through it); H2 predicts a single gradient all the way, with a lower
value of $k$ inferred. A second discriminator is age dependence at fixed
sediment cover.

**Noise level:** the two hypotheses differ by tens of percent in $k$ and by a
factor of order two in curvature over 100–300 m of penetration; a temperature
resolution of a few millikelvin over metre-scale probes, and a gradient
determined to better than 5%, is adequate. The limiting error is not the
thermometry but the thermal-conductivity measurement on the recovered core, which
must be better than 5% to distinguish the models.

**What remains untested:** the partitioning between *focused* and *distributed*
flow. Even a perfectly measured deficit cannot tell whether the missing heat left
through a few vents or through the whole ridge flank, because the budget
integrates over both. That partition requires direct flux measurements at vents
and a tracer budget in the water column — an independent experiment.
