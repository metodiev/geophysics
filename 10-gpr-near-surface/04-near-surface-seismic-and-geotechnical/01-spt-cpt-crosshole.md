---
id: 10-04-01
title: "Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole"
level: advanced
prereqs: ["06-01-02", "06-10-01", "10-01-01"]
tags: [gpr, near-surface, geotechnical, spt, cpt, cross-hole, down-hole, shear-wave-velocity]
---

# Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole

**All models and data in this module are SYNTHETIC.** The blow counts, cone
resistances, unit weights, layer velocities and pick errors below are chosen
teaching values. No borehole, site or test result is described from measurement.
Physical constants and adopted conventions (the 60% reference energy ratio, the
100 kPa reference stress, the standard cone net-area ratio) are labelled as such.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the energy-ratio and overburden corrections that turn a measured
   blow count $N$ into $(N_1)_{60}$, and **explain** why the two corrections act
   in opposite directions.
2. **Compute** the net cone resistance, the friction ratio and a soil
   behaviour-type index from cone data, and **state** what an index is and is not.
3. **Derive** the interval-velocity relation $v = (r_2-r_1)/(t_2-t_1)$ from the
   straight-ray assumption, and **show** that it fails when the ray crosses a
   velocity increase.
4. **Distinguish** the same-depth cross-hole configuration, which measures a layer
   velocity directly, from the fixed-source configuration, which does not.
5. **Quantify** how a constant trigger delay and a random trigger jitter affect a
   down-hole interval velocity differently, and **state** which intervals are
   least reliable and why.
6. **Convert** a shear-wave velocity to a small-strain modulus with
   $G_{\max} = \rho V_s^2$, and **explain** why an index parameter and a modulus
   are not interchangeable.
7. **State** the depth and geometry conditions under which a borehole velocity
   measurement is a layer property rather than an average over the ray path.

## Prerequisites

- [06-01-02 P and S Waves](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md)
  — the shear modulus, the shear-wave speed and their relation.
- [06-10-01 Refraction Survey Geometry and Travel-Time Interpretation](../../06-seismology/10-refraction-and-near-surface-seismology/01-refraction-basics.md)
  — travel-time geometry, the crossover distance and first arrivals.
- [10-01-01 GPR Physics: EM Pulses, Dielectric Permittivity and Reflection](../01-gpr-principles/01-gpr-physics.md)
  — a complementary near-surface measurement, and the amplitude/calibration
  discipline this lesson reuses for velocity.

## 1. Intuition: four tests, four different measurements

A geotechnical site investigation answers engineering questions — how much will
this settle, will it liquefy, how strong is it — using four measurements that are
often quoted as if they were the same number:

- the **standard penetration test (SPT)**, a blow count: a *penetration
  resistance* under dynamic loading;
- the **cone penetration test (CPT)**, a quasi-static tip resistance and sleeve
  friction: also a *penetration resistance*, but measured continuously and under
  different drainage conditions;
- the **cross-hole** seismic test, a travel time between two boreholes: a *shear
  velocity*, hence a small-strain stiffness;
- the **down-hole** test, a travel time from a surface source to a borehole
  receiver: also a shear velocity, with different geometry and different errors.

The first two are **index** measurements: they depend on density, stress state,
cementation, grain shape and drainage in ways that cannot be separated by the
measurement itself, so any conversion to a design parameter is an empirical
correlation with scatter. The second two are **physical**: a travel time and a
geometry give a velocity, and $\rho V_s^2$ is a modulus exactly. The engineering
deliverable is usually built from all four, and the honest report says which
number came from which kind of measurement.

This lesson is about that split, and about the geometry conditions that decide
whether a "velocity" is a layer property or an average. It ends with the arithmetic
of the one thing every borehole seismic survey has to get right: the time
reference.

## 2. Precise definitions

| Quantity | Symbol | Meaning | Unit |
|---|---|---|---|
| blow count | $N$ | blows per 300 mm in the SPT | — |
| energy ratio | $ER$ | hammer energy reaching the sampler | % |
| corrected count | $N_{60}$ | $N\,ER/60$ | — |
| overburden correction | $C_N$ | $\sqrt{p_a/\sigma'_v}$ | — |
| normalised count | $(N_1)_{60}$ | $N_{60}C_N$ | — |
| cone resistance | $q_c$ | measured tip resistance | MPa |
| net cone resistance | $q_t$ | $q_c + (1-a)u_2$ | MPa |
| friction ratio | $R_f$ | $f_s/q_t \times 100$ | % |
| behaviour index | $I_c$ | soil-behaviour-type index | — |
| shear velocity | $V_s$ | from a travel time and a path length | m/s |
| small-strain modulus | $G_{\max}$ | $\rho V_s^2$ | Pa |

$p_a = 100\ \mathrm{kPa}$ is the reference stress and $60\%$ is the reference
energy ratio: **both are conventions**, and $C_N$ as written is the
Liao–Whitman-style square-root form, not a unique physical law.

## 3. Derivations

### 3.1 SPT corrections

A hammer delivering energy $ER$ (a percentage of the theoretical free-fall
energy) drives the sampler further than a 60%-energy hammer would, so the
*measured* count is smaller and must be scaled up to the reference:

$$N_{60} = N\,\frac{ER}{60}.$$

The penetration resistance also depends on the confining stress: the same sand at
greater depth is stiffer for reasons that have nothing to do with its relative
density. The standard correction normalises to an effective stress of
$100\ \mathrm{kPa}$:

$$C_N = \sqrt{\frac{p_a}{\sigma'_v}}, \qquad
(N_1)_{60} = N_{60}\,C_N.$$

*Measured table* (SYNTHETIC profile, water table at $2.0\ \mathrm{m}$,
$\gamma = 18$ and $20\ \mathrm{kN\,m^{-3}}$, $ER = 72\%$ so
$ER/60 = 1.20$):

| $z$ (m) | $\sigma_v$ (kPa) | $\sigma'_v$ (kPa) | $N$ | $N_{60}$ | $C_N$ | $(N_1)_{60}$ |
|---|---|---|---|---|---|---|
| $1.5$ | $27.0$ | $27.0$ | $5$ | $6.0$ | $1.92$ | $11.5$ |
| $3.0$ | $56.0$ | $46.2$ | $8$ | $9.6$ | $1.47$ | $14.1$ |
| $4.5$ | $86.0$ | $61.5$ | $13$ | $15.6$ | $1.28$ | $19.9$ |
| $6.0$ | $116.0$ | $76.8$ | $17$ | $20.4$ | $1.14$ | $23.3$ |
| $7.5$ | $146.0$ | $92.0$ | $21$ | $25.2$ | $1.04$ | $26.3$ |
| $9.0$ | $176.0$ | $107.3$ | $26$ | $31.2$ | $0.97$ | $30.1$ |

Read the two corrections against each other. The energy ratio multiplies every
count by $1.20$; the overburden correction *divides* the deep ones by up to
$1/0.97$. The net effect on the profile is a smoothing of the increase with depth:
the raw counts rise by a factor of $5.2$ from $1.5$ to $9\ \mathrm{m}$, and the
normalised counts by $2.6$. **An uncorrected $N$ is neither a penetration
resistance nor a density.**

### 3.2 CPT indices

The cone measures tip resistance $q_c$, sleeve friction $f_s$ and pore pressure
$u_2$. The net area of the cone's shoulder means the pore pressure at the tip acts
over a small area, so the *net* resistance is

$$q_t = q_c + (1-a)u_2,$$

with $a \approx 0.8$ the net area ratio for a standard cone (a convention). Two
dimensionless groups follow:

$$R_f = \frac{f_s}{q_t}\times100\ (\%),
\qquad
Q = \frac{q_t-\sigma_v}{\sigma'_v},
\qquad
F = \frac{f_s}{q_t-\sigma_v}\times100\ (\%),
$$

and the soil behaviour type index

$$I_c = \sqrt{(3.47-\log_{10}Q)^{2} + (1.22+\log_{10}F)^{2}}.$$

*Measured table* (SYNTHETIC):

| $z$ (m) | $q_c$ (MPa) | $q_t$ (MPa) | $R_f$ (%) | $Q$ | $F$ | $I_c$ | behaviour type |
|---|---|---|---|---|---|---|---|
| $1.5$ | $3.20$ | $3.203$ | $0.87$ | $117.6$ | $0.88$ | $1.82$ | sand |
| $3.0$ | $5.10$ | $5.106$ | $0.70$ | $109.3$ | $0.71$ | $1.79$ | sand |
| $4.5$ | $8.40$ | $8.409$ | $0.52$ | $135.4$ | $0.53$ | $1.64$ | sand |
| $6.0$ | $11.20$ | $11.212$ | $0.46$ | $144.6$ | $0.47$ | $1.58$ | sand |
| $9.0$ | $15.60$ | $15.618$ | $0.45$ | $143.9$ | $0.45$ | $1.58$ | sand |
| $12.0$ | $1.80$ | $1.828$ | $4.92$ | $11.5$ | $5.65$ | $3.11$ | clayey silt |

The sharp change at $12\ \mathrm{m}$ is the whole point of the index: a factor of
nine in tip resistance and a factor of eleven in friction ratio, which classify as
a different material. Note also how small the net-area correction is here
($3.203$ against $3.20$): it matters in soft, high-$u_2$ ground, not in sand.

**An index is not a stiffness.** $I_c$ and $V_s$ are correlated in practice, and
the correlation is empirical and site-specific. Anything derived from $I_c$
inherits its scatter; anything derived from $V_s$ inherits only the measurement
error of a travel time and a path length.

### 3.3 Cross-hole: the interval-velocity formula and its assumption

In a cross-hole survey a source in one borehole and receivers in another record
the first arrival. If the medium were homogeneous, the path would be a straight
line of length $r = \sqrt{L^2 + \Delta z^2}$ ($L$ the borehole separation,
$\Delta z$ the depth difference), so between two receivers

$$t_2 - t_1 = \frac{r_2-r_1}{v}
\;\Longrightarrow\;
v = \frac{r_2-r_1}{t_2-t_1}.$$

**That is the entire derivation, and its assumption is the whole story.** In a
layered medium the first arrival is *refracted*: it bends along interfaces, and
whenever the ray crosses a velocity increase it spends more of its path in the
faster material. The measured $t_2-t_1$ is then smaller than the straight-ray
prediction, and the formula returns a velocity that is too high — or, at a large
enough contrast, unphysical.

*Measured table* (SYNTHETIC $V_s$ model $180$, $260$, $420$,
$600\ \mathrm{m\,s^{-1}}$ in four layers, $L = 4.0\ \mathrm{m}$, source at
$1.0\ \mathrm{m}$): the exact first-arrival times, computed by solving Snell's law
for the ray parameter, are

| $z_r$ (m) | range (m) | exact $t$ (ms) | $\Delta t$ (ms) | $v$ by the formula (m/s) | true $V_s$ (m/s) |
|---|---|---|---|---|---|
| $2.0$ | $4.123$ | $22.906$ | $0.684$ | $180.0$ | $180.0$ |
| $3.0$ | $4.472$ | $20.002$ | $-2.904$ | $-120.2$ | $260.0$ |
| $4.0$ | $5.000$ | $21.621$ | $1.620$ | $325.9$ | $260.0$ |
| $7.0$ | $7.211$ | $27.632$ | $0.978$ | $825.8$ | $420.0$ |
| $11.0$ | $10.770$ | $34.299$ | $1.230$ | $749.3$ | $600.0$ |

The arrival at $3.0\ \mathrm{m}$ is **earlier** than at $2.0\ \mathrm{m}$: the ray
to the deeper receiver dives into the faster second layer. The formula then
returns $-120.2\ \mathrm{m\,s^{-1}}$ — a negative shear velocity, which is the
loudest possible statement that the straight-ray assumption has failed. The
correct treatment is a refraction-corrected (Snell) inversion or a layered model;
the straight-ray formula is valid only when the path crosses no velocity increase,
which is precisely what a site investigation cannot assume.

### 3.4 Cross-hole: the geometry that does work

If the source and the receiver are at the **same depth**, the path is horizontal
inside one layer and

$$v = \frac{L}{t}.$$

*Measured table* (same model): $z = 1\ \mathrm{m} \rightarrow t = 22.222\
\mathrm{ms} \rightarrow v = 180.0\ \mathrm{m\,s^{-1}}$;
$z = 3\ \mathrm{m} \rightarrow v = 260.0$; $z = 7\ \mathrm{m} \rightarrow 420.0$;
$z = 11\ \mathrm{m} \rightarrow 600.0$ — the true layer velocities, exactly. The
price is operational: it requires a source that can be lowered to the same depth as
a receiver, or strings of sources and receivers in both holes, rather than a single
surface source.

A caveat that must be stated with the method: the direct horizontal path is the
first arrival only if no *diving* ray through a faster layer arrives earlier. In
extreme contrasts the picked first break may not be the direct wave at all, and
the check is reciprocity and consistency between source-receiver depth pairs.

### 3.5 Down-hole: what cancels and what does not

A down-hole survey has a source at (or near) the surface and receivers at
increasing depth in one borehole. The interval velocity again uses
$v = (r_2-r_1)/(t_2-t_1)$ with $r_i$ the source–receiver distances, and two error
terms behave completely differently:

- **a constant trigger delay $\delta t_0$** appears in both $t_1$ and $t_2$ and
  **cancels exactly** in the difference;
- **a random trigger jitter** does not cancel, and its relative effect on an
  interval velocity is $\delta(\Delta t)/\Delta t$ — largest where $\Delta t$ is
  smallest, i.e. in the fastest intervals and wherever the receiver spacing is
  short.

*Measured table* (SYNTHETIC, receivers every $2\ \mathrm{m}$ from $1$ to
$13\ \mathrm{m}$, true interval velocities computed by Snell's law):

| case | interval velocities (m/s) |
|---|---|
| exact | $-212.6$, $302.5$, $418.5$, $502.2$, $567.9$, $670.1$ |
| $+1\ \mathrm{ms}$ constant offset | $-212.6$, $302.5$, $418.5$, $502.2$, $567.9$, $670.1$ (identical) |
| $1\ \mathrm{ms}$ random jitter | $-148.5$, $310.9$, $568.1$, $358.3$, $868.4$, $696.8$ |

The constant-offset row reproduces the exact row to the printed precision — a
direct demonstration of the cancellation. The jitter row scatters by tens of per
cent, and it scatters *more* as the interval gets faster. The negative first value
is the same refraction artefact as Section 3.3, not a timing error.

**Consequence for practice.** A down-hole survey's accuracy is bought with a
repeatable trigger and a long receiver spacing, not with more receivers: doubling
$\Delta z$ halves the relative effect of a fixed timing error.

## 4. Physical interpretation

- **Index versus physical measurement.** $N$ and $q_c$ are *responses* of a
  complex system; $V_s$ is a physical property of the medium. A design number
  derived from the first is a correlation; from the second it is a modulus times a
  strain-dependent factor (the next lesson).
- **Geometry decides whether a velocity is a layer property.** The same ground
  gives $180.0\ \mathrm{m\,s^{-1}}$ from a same-depth cross-hole pair and
  $-120.2$ from a straight-ray interpretation of a deeper receiver. The medium did
  not change; the assumption did.
- **Time reference is a first-class error source, but only in its random part.** A
  constant delay is invisible in interval velocities and fatal to absolute depths;
  jitter is fatal to the fastest intervals. Two different mitigations.
- **A ratio is not a correlation.** The SYNTHETIC profiles give
  $(N_1)_{60}/V_s = 0.0765$ and $0.0554\ \mathrm{s\,m^{-1}}$ at two depths; a
  transfer function fitted to a population is a different object from a ratio
  computed at one point, and it must be quoted with its scatter.

## 5. Worked examples

### Example 1 — from blow counts to a normalised count

At $z = 6.0\ \mathrm{m}$ in the SYNTHETIC profile: $\sigma_v = 116.0$ kPa
($18 \times 2 + 20 \times 4$), $u = 9.81 \times 4 = 39.2$ kPa, so
$\sigma'_v = 116.0-39.2 = 76.8$ kPa.

1. $C_N = \sqrt{100/76.8} = \sqrt{1.3021} = 1.141$.
2. $N_{60} = 17 \times 72/60 = 20.4$.
3. $(N_1)_{60} = 20.4 \times 1.141 = 23.3$ (the demonstration prints $23.3$).

Had the hammer energy not been measured, the same count would have been reported as
$N = 17$ — $27\%$ low against $(N_1)_{60} = 23.3$.

### Example 2 — cross-hole, both configurations

Same SYNTHETIC model, $V_s = 260\ \mathrm{m\,s^{-1}}$ in $2$–$6\ \mathrm{m}$.

1. **Same-depth pair at $z = 3\ \mathrm{m}$** with $L = 4.0\ \mathrm{m}$:
   $v = 4.0/t = 4.0/0.015385 = 260.0\ \mathrm{m\,s^{-1}}$ — exact.
2. **Fixed source at $z_s = 1\ \mathrm{m}$**, receivers at $2$ and
   $3\ \mathrm{m}$: $r_1 = 4.123\ \mathrm{m}$, $r_2 = 4.472\ \mathrm{m}$,
   $t_1 = 22.906\ \mathrm{ms}$, $t_2 = 20.002\ \mathrm{ms}$. The difference is
   negative because the second arrival dove into the faster layer, so the formula
   returns $-120.2\ \mathrm{m\,s^{-1}}$.
3. **The fix.** Either invert with Snell's law for a layered model (the correct
   route), or place the receivers so that the paths remain inside the target layer
   — the same-depth configuration, whose $260.0\ \mathrm{m\,s^{-1}}$ needs no
   refraction correction at all.

### Example 3 — a modulus from a velocity, and its status

The same layer, with SYNTHETIC $\rho = 1900\ \mathrm{kg\,m^{-3}}$:

$$G_{\max} = \rho V_s^2 = 1900 \times 260^2 = 1.284\times10^{8}\ \mathrm{Pa}
= 128.4\ \mathrm{MPa},$$

$$E = 2G(1+\nu) = 2(128.4)(1.30) = 333.9\ \mathrm{MPa}\quad (\nu = 0.30).$$

The demonstration prints exactly these numbers. Two statements about them:

- $G_{\max} = \rho V_s^2$ is **exact** for a linear isotropic elastic medium — no
  correlation, no fit, and its uncertainty is the uncertainty of $\rho$ and $V_s$
  (typically $2$–$5\%$ in each).
- $G_{\max}$ is the modulus at **infinitesimal** strain. It is not the modulus that
  a footing at working load will see; that is the subject of the next lesson, where
  the same layer gives a settlement that differs by a factor of $2.9$ depending on
  which modulus is used.

## 6. Assumptions and regime of validity

1. **The SPT corrections are conventions.** $ER/60$ and $C_N = \sqrt{p_a/\sigma'_v}$
   are two of several accepted forms; the numbers they produce are comparable only
   if the conventions are stated.
2. **Hydrostatic pore pressure** for $\sigma'_v$. Over- or under-pressure changes
   $C_N$ and every normalised index built on it.
3. **A straight ray for the interval-velocity formula.** Valid only where the path
   crosses no velocity increase; the demonstration's negative velocity is the
   counter-example.
4. **A horizontally layered medium** for the two-layer interpretation of the
   weathering and for the layer labels in the velocity tables. A dipping or
   laterally variable profile makes every interval velocity an *apparent* one.
5. **A repeatable source and a stable receiver coupling.** Both are part of the
   time measurement, and the review of a borehole survey should always ask how they
   were verified (reciprocity, a repeat shot, a known-depth check).
6. **A point source and receiver.** A finite-length receiver averages over its own
   length, which is one more reason not to expect a layer velocity from a short
   interval.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| stress | $\sigma_v,\sigma'_v$ | kPa | $\mathrm{kN\,m^{-3}}\times\mathrm{m}$ |
| blow count | $N$, $N_{60}$, $(N_1)_{60}$ | — | dimensionless |
| tip resistance | $q_c, q_t$ | MPa | force/area |
| friction ratio | $R_f$ | % | ratio $\times 100$ |
| velocity | $V_s$ | $\mathrm{m\,s^{-1}}$ | length/time |
| modulus | $G, E$ | Pa | $\mathrm{kg\,m^{-3}}\times(\mathrm{m\,s^{-1}})^2$ |
| time | $t$ | ms | travel time in borehole seismic |

The unit of the index expression is worth checking once: $Q$ and $F$ are
dimensionless (stress ratios), so their logarithms are dimensionless and $I_c$ is a
pure number. If a computation of $I_c$ carries a unit, a stress was divided by a
stress incorrectly.

## 8. Python demonstration

[`code/spt_cpt_crosshole_demo.py`](code/spt_cpt_crosshole_demo.py) prints every
number quoted above:

1. the SPT correction table, with the two corrections shown acting in opposite
   directions;
2. the CPT table: net resistance, friction ratio and behaviour-type index, with
   the classification band printed for each row;
3. cross-hole in two geometries — the same-depth configuration recovering the
   layer velocities exactly, and the fixed-source configuration producing a
   negative interval velocity from the straight-ray formula;
4. down-hole interval velocities with a constant trigger offset (which reproduces
   the exact row) and with random jitter (which scatters by tens of per cent);
5. $G_{\max}$ and $E$ for each layer, and the $(N_1)_{60}/V_s$ ratio, with the
   statement that a ratio is not a correlation.

The exact arrival times are computed by solving Snell's law for the ray parameter
with a scan, not by calling a ray-tracing library, so the check is independent of
any package. The demo is print-only, uses the fixed seed `20261014`, and exits $0$.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-spt-cpt-crosshole-exercises.md`](exercises/01-spt-cpt-crosshole-exercises.md)
and
[`exercises/01-spt-cpt-crosshole-solutions.md`](exercises/01-spt-cpt-crosshole-solutions.md).

- **★** Compute $(N_1)_{60}$ for $N = 12$, $ER = 55\%$, $z = 5\ \mathrm{m}$ in a
  profile with $\sigma'_v = 70\ \mathrm{kPa}$.
- **★★** Two cross-hole receivers at the same depth $3\ \mathrm{m}$ in boreholes
  $5.0\ \mathrm{m}$ apart give $t = 19.2\ \mathrm{ms}$. Compute $V_s$ and
  $G_{\max}$ for $\rho = 1950\ \mathrm{kg\,m^{-3}}$, and state the two assumptions.
- **★★★** Design a borehole seismic programme that determines an interval velocity
  to $5\%$ in a $180\ \mathrm{m\,s^{-1}}$ layer with a $0.2\ \mathrm{ms}$ timing
  resolution, choosing the geometry, the receiver spacing and the timing strategy,
  and stating what would invalidate it.

## 10. Further reading

- **Robertson, P. K. (1990). Soil classification using the cone penetration test.
  *Canadian Geotechnical Journal*, 27.** Level: research. The origin of the
  behaviour-type index used in Section 3.2.
- **Liao, S. S. C., & Whitman, R. V. (1986). Overburden correction factors for SPT
  in sand. *Journal of Geotechnical Engineering*, 112.** Level: research. The
  overburden correction of Section 3.1.
- **Youd, T. L., et al. (2001). Liquefaction resistance of soils: summary report
  from the 1996 NCEER and 1998 NCEER/NSF workshops. *Journal of Geotechnical and
  Geoenvironmental Engineering*, 127.** Level: research/reference. The simplified
  procedure quantified in the next lesson, and the standard statement of what a
  corrected penetration index is for.
- **ASTM/ISO test standards for the SPT, CPT and cross-hole methods.** Level:
  reference. The procedural definitions of $N$, $q_c$ and the trigger reference
  used throughout this lesson; consult the current edition of the relevant standard
  rather than a second-hand description.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes. All values are SYNTHETIC.

> A borehole site has $\gamma = 18\ \mathrm{kN\,m^{-3}}$ above and
> $20\ \mathrm{kN\,m^{-3}}$ below a $2.5\ \mathrm{m}$ water table. At
> $z = 5.0\ \mathrm{m}$ an SPT with $ER = 65\%$ gives $N = 11$, and a cone gives
> $q_c = 6.0\ \mathrm{MPa}$, $f_s = 40\ \mathrm{kPa}$, $u_2 = 50\ \mathrm{kPa}$.
> **(a)** Compute $\sigma_v$, $\sigma'_v$, $N_{60}$ and $(N_1)_{60}$.
> **(b)** Compute $q_t$, $R_f$, $Q$ and $F$, and comment on the size of the net
> area correction. **(c)** A down-hole survey uses receivers at $2\ \mathrm{m}$
> spacing with a $0.2\ \mathrm{ms}$ pick precision and a $0.5\ \mathrm{ms}$ random
> trigger jitter. Compute the velocity uncertainty in a $200\
\mathrm{m\,s^{-1}}$ interval and in a $600\ \mathrm{m\,s^{-1}}$ interval, and state
> which is worse. **(d)** The same layer gives $V_s = 240\ \mathrm{m\,s^{-1}}$ from
> a same-depth cross-hole pair and $310\ \mathrm{m\,s^{-1}}$ from the straight-ray
> formula on a fixed-source pair. Explain the difference in one sentence.
> **(e)** Compute $G_{\max}$ for $V_s = 240\ \mathrm{m\,s^{-1}}$,
> $\rho = 1900\ \mathrm{kg\,m^{-3}}$, and state why it is not yet a design
> modulus.

Worked versions of (a)–(c) appear in the
[solutions](exercises/01-spt-cpt-crosshole-solutions.md).

## Common pitfalls

1. **Reporting an uncorrected $N$.** The energy-ratio and overburden corrections
   act in opposite directions and together change the profile by a factor of two.
2. **Treating an index as a stiffness.** $I_c$ and $V_s$ are different
   measurements; a transfer function between them is an empirical fit.
3. **Applying the straight-ray interval formula in layered ground.** The
   demonstration returns $-120.2\ \mathrm{m\,s^{-1}}$ — a velocity that cannot
   exist.
4. **Assuming a constant trigger delay matters.** It cancels in an interval
   velocity, exactly; the random part is the problem.
5. **Expecting a short receiver spacing to improve resolution.** With a fixed
   timing error, the shortest interval has the worst velocity error.
6. **Using $G_{\max}$ as a design modulus.** It is the infinitesimal-strain value;
   the next lesson measures the factor.

## Related modules

- [10-04 Near-Surface Seismic and Geotechnical Methods](./README.md) — the module
  these methods belong to.
- [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md)
  — refraction geometry and the surface-wave route to a $V_s$ profile, which is the
  non-invasive alternative to a borehole.
- [06-01 Elastic Wave Propagation](../../06-seismology/01-elastic-wave-propagation/README.md)
  — why $\rho V_s^2$ is a modulus and what a Poisson's ratio does to $E$.
- [23-02 Seismic Instruments and Fieldwork](../../23-field-methods-instruments/02-seismic-instruments-and-fieldwork/README.md)
  — the hardware, timing and field-quality-control side of a borehole survey.
- [11-06 Geotechnical and Engineering Exploration](../../11-exploration-geophysics/06-geotechnical-and-engineering/README.md)
  — the same measurements scaled up to dams, tunnels and large foundations.

## Code and exercises

| Path | Contents |
|---|---|
| [`code/spt_cpt_crosshole_demo.py`](code/spt_cpt_crosshole_demo.py) | The five computations of Section 8 |
| [`exercises/01-spt-cpt-crosshole-exercises.md`](exercises/01-spt-cpt-crosshole-exercises.md) | Graded problems |
| [`exercises/01-spt-cpt-crosshole-solutions.md`](exercises/01-spt-cpt-crosshole-solutions.md) | Worked solutions |

```bash
cd 10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spt_cpt_crosshole_demo.py
```
