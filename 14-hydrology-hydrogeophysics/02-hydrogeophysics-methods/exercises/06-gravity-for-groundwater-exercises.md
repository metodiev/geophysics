# Exercises — 14-02-06 Microgravity and Satellite Gravity for Water Storage Change

Attempt these before reading the
[solutions](./06-gravity-for-groundwater-solutions.md). The lesson is
[06 Microgravity and Satellite Gravity for Water Storage Change](../06-gravity-for-groundwater.md).
Every model, network and storage figure below is **SYNTHETIC**.

Use $G = 6.67430 \times 10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$,
$\rho_w = 1000\ \mathrm{kg\,m^{-3}}$, so
$\Delta g = 2\pi G \rho_w \Delta h = 41.94\ \mathrm{\mu Gal}$ per metre of water
column and $\Delta g = 2\pi G \Delta m$ with
$2\pi G = 4.1936 \times 10^{-10}\ \mathrm{m\,s^{-2}}$ per kg m$^{-2}$; and
$1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$.

## ★ Foundational

**★1.** An unconfined aquifer has $S_y = 0.12$. Compute the gravity change for a
1 m water-table **decline**, and compute the storage change in mm of water. Explain
in one sentence why the answer is not 41.94 µGal.

**★2.** A relative gravimeter is repeatable to 5 µGal. Compute the equivalent water
column in mm, and the water-table change this corresponds to for $S_y = 0.12$ and
for $S_y = 1$ (a confined aquifer's head change, no drainage).

**★3.** A time-variable gravity solution gives $\Delta C_{20} = 2 \times 10^{-10}$.
Using the lesson's coefficient (EWH $= 1.8713 \times 10^{8}$ m per unit
$\Delta C_{20}$ at the pole), compute the equivalent water height in mm, and the
mass change over 200 000 km².

## ★★ Applied

**★★4.** A gravity station's height is known to only 1 cm. Compute the induced
gravity error, express it as a percentage of the signal in ★1, and state the height
control required to keep the height error below 10% of that signal.

**★★5.** A microgravity survey records a storage loss of 52.5 mm of water
(2.20 µGal). **(i)** Compute the water-table decline this implies for
$S_y = 0.12$. **(ii)** Compute the gravity change produced by a saturation decrease
of 0.05 over 3 m of soil with $\phi = 0.35$, and the water-table decline it mimics.
**(iii)** Comment on the ambiguity and name two measurements that break it.

**★★6.** For a compact basin load, the fraction of the load's degree-variance
captured below $l_{\max}$ is 19.5% / 39.8% / 72.1% for $l_{\max} = 10/20/40$ at a
disk radius of 2°, and 81.6% / 97.1% / 99.2% at 10°. Compute the missing fraction in
each case, state which radius is worst affected, and explain in three sentences why
this appears as leakage in a regional mascon solution rather than as a small error at
the basin centre.

## ★★★ Research-oriented

**★★★7.** A monitoring network covers 4 km × 4 km over an unconfined aquifer with
$S_y = 0.12$. The requirement is to detect a 0.25 m annual water-table change at two
standard deviations. Compute the required per-survey repeatability and the number of
repeat occupations needed from a 5 µGal instrument (noise falls as $1/\sqrt{N}$),
then state whether the requirement is achievable and what you would change. Include
the transfer error from levelling in your argument.

**★★★8.** The demonstration verifies three things: the disk integral's convergence to
the Bouguer slab (37.76 → 41.93 µGal as $R$ grows from 1 km to 100 000 km), exact
linearity of the equivalent-water-height formula in $\Delta C_{20}$ and in
$(1 + k_l)$, and the structure of the general-degree formula (the $l = 4$/ $l = 2$
ratio 2.415). State what each test verifies and what none of them can verify. Then
design one **validation** for the same code — an independent measurement or
independent physical law — and say what it would catch that the three verifications
cannot.
