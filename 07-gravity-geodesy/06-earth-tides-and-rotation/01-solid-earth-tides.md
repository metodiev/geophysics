---
id: 07-06-01
title: "Solid Earth Tides and Their Gravity Signature"
level: graduate
prereqs: ["07-01-02", "02-02-07", "02-04-04"]
tags: [gravity, geodesy, earth-tides, love-numbers, time-series]
---

# Solid Earth Tides and Their Gravity Signature

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the tidal potential from the difference between the acceleration
   of a mass element and that of the Earth's centre, and **explain** why the
   degree-1 term is removed.
2. **Derive** the degree-2 tidal acceleration at the Earth's surface and
   **compute** the solar-to-lunar ratio from $\mathrm{GM}_b/d^{3}$ alone.
3. **Derive** the frequencies of the principal tidal constituents as integer
   combinations of three rates, and **check** that S2 comes out as exactly
   $12.0000\ \mathrm{h}$.
4. **Compute** the gravity-tide amplitude factor
   $\delta = 1 + h_2 - \tfrac{3}{2}k_2$ and state what each term represents
   physically.
5. **Verify** the equilibrium latitude laws $\propto\cos^{2}\varphi$
   (semidiurnal) and $\propto\sin 2\varphi$ (diurnal) by harmonic analysis of a
   synthetic record.
6. **Measure** how the residual of a harmonic fit falls as constituents are
   added, and **state** the criterion that decides which constituents must be
   included.
7. **State** which parts of a tidal prediction are physics, which are Earth
   parameters, and which are oceanographic.

## Prerequisites

- [07-01-02 Gravitational Potential, Equipotentials and the Geoid](../01-gravity-fundamentals/02-gravity-potential.md) —
  the multipole expansion and Laplace's equation.
- [02-02-07 Central Forces](../../02-physics/02-classical-mechanics/07-central-forces.md) —
  orbital motion, used for the ephemeris and the removal of the degree-1 term.
- [02-04-04 Elastic Moduli](../../02-physics/04-elasticity-and-continuum-mechanics/04-elastic-moduli.md) —
  why the solid Earth deforms, and what a Love number summarises.

> **All models and data in this module are SYNTHETIC.** The ephemeris below is a
> deliberately simplified teaching model (circular orbits, fixed node, no
> ellipticity); the amplitudes it produces are properties of that model, not of
> the Earth. The Love numbers used are *rounded standard elastic-Earth
> parameters*, not measurements made here.

## 1. What a tide is

Place a mass element at the Earth's surface, at position $\mathbf{r}$ relative
to the Earth's centre, and a perturbing body of mass $M_b$ at
$\mathbf{d}$ from the centre. Both the element and the centre are attracted by
the body, but not equally, because they are at different distances. The
element's acceleration relative to the Earth's centre is

$$\mathbf{a}_{\text{tidal}} = -GM_b\frac{\mathbf{r}-\mathbf{d}}{|\mathbf{r}-\mathbf{d}|^{3}}
+ GM_b\frac{\mathbf{d}}{d^{3}} ,$$

where the second term is the centre's acceleration. This *difference of two
accelerations* is the entire phenomenon. It is what raises a water tide, what
strains the rock, and what a gravimeter measures.

Expanding in $r/d$ (with $r \ll d$) and keeping the leading terms gives a
potential

$$V(\mathbf{r}) = \frac{GM_b}{d}\sum_{n=2}^{\infty}\left(\frac{r}{d}\right)^{n}
P_n(\cos\psi), \qquad \cos\psi = \hat{\mathbf{r}}\cdot\hat{\mathbf{d}} ,$$

where $\psi$ is the geocentric angle between the station and the body. **The sum
starts at $n = 2$** because the $n = 0$ term is a constant (irrelevant to a
difference) and the $n = 1$ term is exactly cancelled by the centre's
acceleration — the $n = 1$ term describes a rigid translation of the whole
Earth toward the body, which produces no tidal effect. Both statements can be
checked by expanding $\mathbf{a}_{\text{tidal}}$ in Legendre polynomials.

Degree 2 dominates. The relative size of degree $n+1$ to degree $n$ is of order
$r/d$: for the Moon $6371/384400 = 1.66\%$ and for the Sun
$6371/(1.496\times10^{8}) = 0.0043\%$. The demonstration's model includes only
degree 2, and that omission is a $1.7\%$ effect for the Moon — larger than many
of the constituents one fits in practice, which is why production tide
algorithms carry degree 3 and even degree 4.

## 2. The degree-2 tide, and the solar/lunar ratio

With $P_2(x) = \tfrac{1}{2}(3x^{2}-1)$, the degree-2 tidal potential and the
radial acceleration it produces are

$$V_2 = \frac{GM_b\,r^{2}}{d^{3}}P_2(\cos\psi),
\qquad
\frac{\partial V_2}{\partial r} = \frac{2GM_b\,r}{d^{3}}P_2(\cos\psi) .$$

At the Earth's surface $r = R$ the scale of the tidal acceleration is
$2GM_bR/d^{3}$, which depends on the body only through $\mathrm{GM}_b/d^{3}$:

| body | $\mathrm{GM}_b R/d^{3}$ (per unit $P_2$) | $2\mathrm{GM}_bR/d^{3}$ |
|---|---|---|
| Moon | $5.499227\times10^{-7}$ | $1.099845\times10^{-6}\ \mathrm{m\,s^{-2}}$ |
| Sun | $2.525475\times10^{-7}$ | $5.050949\times10^{-7}\ \mathrm{m\,s^{-2}}$ |

*Worked example 1 (the ratio).* With $\mathrm{GM}_{\odot} =
1.32712440018\times10^{20}$, $\mathrm{GM}_{\text{Moon}} =
4.902800118\times10^{12}\ \mathrm{m^{3}\,s^{-2}}$,
$d_{\odot} = 1.495978707\times10^{11}$ (one astronomical unit by definition) and
$d_{\text{Moon}} = 3.844\times10^{8}\ \mathrm{m}$,

$$\frac{(\mathrm{GM}/d^{3})_{\odot}}{(\mathrm{GM}/d^{3})_{\text{Moon}}}
= \frac{1.32712440018\times10^{20}/(1.495978707\times10^{11})^{3}}
{4.902800118\times10^{12}/(3.844\times10^{8})^{3}}
= \frac{3.9643\times10^{-14}}{8.6323\times10^{-14}} = 0.4592 .$$

The solar tide is $46\%$ of the lunar tide — not because the Sun is weaker
(it is $2.7\times10^{7}$ times more massive) but because the $d^{-3}$ dependence
penalises the huge distance. That is why spring and neap tides differ by only a
factor of about $2$ rather than by orders of magnitude.

## 3. Constituent frequencies, derived rather than memorised

Write $\omega$ for the Earth's rotation rate, $n_m = 2\pi/(\text{sidereal
month})$ for the Moon's mean motion and $n_s = 2\pi/(\text{tropical year})$ for
the Sun's. For a circular orbit, the potential is built from products of
rotation phases and orbital phases, so every frequency in the record is an
**integer combination** of the three rates. The named constituents are simply
labels for the small frequencies that matter:

| name | combination | frequency (rad/s) | period |
|---|---|---|---|
| M2 | $2\omega - 2n_m$ | $1.40518901\times10^{-4}$ | 12.4206 h |
| S2 | $2\omega - 2n_s$ | $1.45444087\times10^{-4}$ | 12.0000 h |
| K2 | $2\omega$ | $1.45842300\times10^{-4}$ | 11.9672 h |
| O1 | $\omega - 2n_m$ | $6.75977509\times10^{-5}$ | 25.8193 h |
| K1 | $\omega$ | $7.29211500\times10^{-5}$ | 23.9345 h |
| P1 | $\omega - n_s - n_m$ | $7.00603441\times10^{-5}$ | 24.9118 h |
| Mf | $2n_m$ | $5.32339905\times10^{-6}$ | 13.6608 d |
| Mm | $n_m$ | $2.66169953\times10^{-6}$ | 27.3217 d |
| Ssa | $2n_s$ | $3.98212759\times10^{-7}$ | 182.6211 d |

The rates used are $\omega = 7.2921150\times10^{-5}\ \mathrm{rad\,s^{-1}}$,
a sidereal month of $27.321661\ \mathrm{d}$ and a tropical year of
$365.2422\ \mathrm{d}$ — three numbers generate the whole table.

*Worked example 2 (why S2 is exactly 12 hours).* In cycles per mean solar day,
$\omega = 1.0027379$ and $n_s = 1/365.2422 = 0.0027379$, so

$$2(\omega - n_s) = 2(1.0027379 - 0.0027379) = 2.0000000\ \mathrm{cycles/day}
\;\Longrightarrow\; T = \frac{24}{2} = 12.0000\ \mathrm{h}.$$

The cancellation is not a coincidence: the difference between the solar and
sidereal rotation rates *is* the Sun's mean motion, by definition. Computing this
from the rates with no further input is a check that the rates are mutually
consistent — and it is the reason a solar semidiurnal tide keeps exact clock
time while the lunar one drifts by about 50 minutes a day.

## 4. The gravity-tide factor

A gravimeter does not measure the tidal potential; it measures the change in
gravitational acceleration, and that has three parts:

1. the **direct** attraction of the body, $2GM_bR/d^{3}\,P_2$, which also
   changes the equipotential;
2. the **deformation** of the solid Earth, which moves the station radially by
   $u_r = h_2 V_2/g$ and therefore changes $g$ by $h_2$ times the direct effect;
3. the **redistribution of mass** inside the deformed Earth, which produces an
   additional potential $k_2V_2$.

Collecting the three effects at degree 2 gives the classical gravity-tide factor

$$\delta = 1 + h_2 - \frac{3}{2}k_2 ,$$

where the $3/2$ arises because the extra potential changes the radial derivative
of the potential at the surface with a factor of $3$ relative to the direct
term and the other $1/2$ is the ratio of the $P_2$ angular factors. With the
standard rounded elastic values $h_2 = 0.6090$ and $k_2 = 0.3040$,

$$\delta = 1 + 0.6090 - 1.5(0.3040) = 1.1530 .$$

So the observed solid-Earth tide is about $15\%$ larger than the geometrical one.
**This is the one place where an Earth model enters a tidal prediction**, and it
enters linearly: a $1\%$ error in $h_2$ is a $0.5\%$ error in $\delta$.

*Worked example 3 (the equatorial amplitude).* At the equator with a body
overhead, the semidiurnal part of $P_2$ has amplitude $3/4$ (from
$P_2 = \tfrac14 + \tfrac34\cos2H\cos^{2}\varphi + \ldots$), so

$$|\delta g|_{M2} = \tfrac{3}{4}\times\frac{2GM_{\text{Moon}}R}{d^{3}}\times\delta
= 0.75 \times 1.099845\times10^{-6} \times 1.1530
= 9.5109\times10^{-7}\ \mathrm{m\,s^{-2}} = 95.11\ \mathrm{\mu Gal},$$

where $1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$. That is the scale of
the signal a relative gravimeter must remove before it can see anything else:
**a microgravity target is of order $10\ \mathrm{\mu Gal}$, so the tide is about
ten times the largest anomaly a microgravity survey hunts for, and it must be
removed to better than a per cent.**

The $95.11\ \mathrm{\mu Gal}$ figure assumes the body in the equatorial plane.
The demonstration's synthetic Moon reaches a declination of
$23.44 + 5.15 = 28.58^\circ$, and its fitted equatorial M2 amplitude is
$83.8668\ \mathrm{\mu Gal}$, i.e. $88.18\%$ of the analytic value: the missing
factor is $\cos^{2}\delta$ averaged over the orbit. **Geometry, not
discrepancy** — and it is why a tidal amplitude quoted without the body's
declination is not a prediction.

## 5. Latitude laws, and how to check a tidal analysis

From $P_2$ alone, the semidiurnal amplitude must vary as $\cos^{2}\varphi$ and the
diurnal as $\sin 2\varphi$. The demonstration checks these by harmonic analysis
of a synthetic 60-day record at five latitudes:

| latitude | M2 measured ($\mathrm{\mu Gal}$) | $A_0\cos^{2}\varphi$ | ratio | K1 measured | $B_{45}\sin2\varphi$ | ratio |
|---|---|---|---|---|---|---|
| $0^\circ$ | 83.8668 | 83.8668 | 1.0000 | 0.0016 | 0.0000 | — |
| $30^\circ$ | 62.8953 | 62.9001 | 0.9999 | 43.8678 | 43.8683 | 1.0000 |
| $45^\circ$ | 41.9279 | 41.9334 | 0.9999 | 50.6547 | 50.6547 | 1.0000 |
| $60^\circ$ | 20.9620 | 20.9667 | 0.9998 | 43.8686 | 43.8683 | 1.0000 |
| $89^\circ$ | 0.0256 | 0.0255 | 1.0020 | 1.7679 | 1.7678 | 1.0000 |

Every ratio is unity to four decimals. The tiny departure at $89^\circ$ is a
tiny-amplitude numerical effect, not physics. **The law is exact because it is a
property of $P_2$, not of the Earth** — which is exactly why deviations from it
are informative: a measured departure from $\cos^{2}\varphi$ at a coastal station
is ocean loading, and a departure at an inland station is lateral structure or
instrument error.

## 6. What a harmonic fit can and cannot establish

Fitting a sum of cosines and sines at chosen frequencies to a record leaves a
residual, and the residual measures **the part of the spectrum the chosen list
does not contain**:

| constituents fitted | residual rms |
|---|---|
| 4 (M2, S2, K1, O1) | $8.2156\ \mathrm{\mu Gal}$ |
| 9 (adds K2, P1, Mf, Mm, Ssa) | $6.6232\ \mathrm{\mu Gal}$ |
| all 74 frequencies of the form $m\omega + kn_m + ln_s$, $m\in\{0,1,2\}$, $|k|,|l|\le2$ | $6.1\times10^{-11}\ \mathrm{\mu Gal}$ |

The last row is round-off, and it says something important: in a synthetic model
whose physics is known, the residual is a statement about the *analysis*, not
about the Earth. In a real record the same three-way distinction applies:

- a constituent **above** the noise must be included, or it aliases into the
  others (the four-constituent fit shifted S2 from $20.11$ to
  $23.72\ \mathrm{\mu Gal}$ — a $18\%$ error in an oceanographically important
  quantity, purely from an incomplete list);
- a constituent **below** the noise cannot be estimated, and including it only
  costs degrees of freedom;
- the **Rayleigh criterion** fixes how long a record must be to separate two
  frequencies: in cycles per day, M2 and S2 differ by
  $2(n_m-n_s)\times86400/2\pi = 0.0677\ \mathrm{c\,d^{-1}}$ (the $2\pi$ matters:
  a rate in $\mathrm{rad\,s^{-1}}$ is not a frequency in cycles per day), so
  $1/0.0677 = 14.8$ days are required. The demonstration's 60-day record is
  comfortable for every constituent it fits.

## 7. Assumptions and regime of validity

1. **Point-mass bodies on circular orbits.** The real Moon's orbit is eccentric
   and its node regresses; these produce the *elliptic* and *nodal* modulations,
   which this model does not contain and which real analyses must include. The
   demonstration's absence of them is a feature of the teaching model, not an
   approximation to reality.
2. **Degree 2 only.** Degree 3 is of order $R/d = 1.7\%$ for the Moon and is
   omitted here; production algorithms include it.
3. **Elastic, spherically symmetric, non-rotating Earth response.** $h_2$ and
   $k_2$ summarise it; the real Earth is aspherical, and the response has small
   latitude and frequency dependences.
4. **No ocean load.** The oceans redistribute the tidal potential and produce a
   load tide that can reach $10$–$20\%$ of the body tide at coastal stations.
   **This is the largest term omitted here**, and it is not small.
5. **No atmosphere, no core resonance.** The fluid core reduces the effective
   $k_2$ slightly, and the free core nutation produces a frequency-dependent
   resonance near the diurnal band.
6. **Equilibrium tide.** The solid Earth responds nearly in equilibrium; the
   ocean does not, which is precisely why the ocean tide needs a hydrodynamic
   model and the body tide does not.

## 8. Python demonstration

`code/solid_earth_tides_demo.py` prints, with units:

1. **Derived frequencies** for nine named constituents from three rates, with S2
   coming out at exactly $12.0000\ \mathrm{h}$ as a consistency check.
2. **The degree-2 acceleration** for the Moon and Sun and their ratio $0.4592$.
3. **The gravity-tide factor** $\delta = 1.1530$ and the equatorial M2 amplitude
   $95.11\ \mathrm{\mu Gal}$.
4. **A synthetic 60-day record** at $5$-minute sampling (rms
   $60.71\ \mathrm{\mu Gal}$, range $-147.3$ to $+92.5\ \mathrm{\mu Gal}$) from a
   simplified ephemeris.
5. **Harmonic analyses** with 4, 9 and all 74 constituents, showing the residual
   collapsing from $8.22\ \mathrm{\mu Gal}$ to round-off.
6. **The latitude laws**, verified to four decimals.

Print-only, fixed seed, no network, runs in under a second.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-solid-earth-tides-exercises.md`](./exercises/01-solid-earth-tides-exercises.md)
and
[`exercises/01-solid-earth-tides-solutions.md`](./exercises/01-solid-earth-tides-solutions.md).

- **★** Derive the Moon/Sun tidal ratio from $\mathrm{GM}/d^{3}$ with the numbers
  given, and state the ratio for a body at twice the Moon's distance with the
  same mass.
- **★** Compute the O1 period from $\omega$ and $n_m$ and convert it to hours.
- **★★** Compute $\delta$ for $h_2 = 0.6078$, $k_2 = 0.2990$ and state the change
  in the predicted M2 amplitude.
- **★★** A record is 10 days long. Which pairs among M2, S2, K1, O1 can be
  separated by the Rayleigh criterion?
- **★★★** Design a synthetic experiment that measures how much a $10\%$ error in
  the ocean-load model contaminates a fitted M2 amplitude at a coastal station.

## 10. Mastery checkpoint

Do this without notes:

> A synthetic gravimeter at $45^\circ$N records 60 days of data. **(a)** Compute
> the frequency and period of M2 from $\omega$ and the sidereal month, and state
> the required record length to separate M2 from S2. **(b)** Compute the
> gravity-tide factor $\delta$ for $h_2 = 0.6090$, $k_2 = 0.3040$ and say what
> the physical meaning of each term is. **(c)** Predict the M2 amplitude at
> $45^\circ$N given the equatorial value $95.11\ \mathrm{\mu Gal}$ (including
> $\delta$) and compare with the measured $41.93\ \mathrm{\mu Gal}$.
> **(d)** The 4-constituent fit gave S2 $= 23.72\ \mathrm{\mu Gal}$ and the
> 9-constituent fit $20.11$: explain the difference and state which you would
> report. **(e)** Name the largest physical effect omitted from the model.

*Answers.* **(a)** $\omega = 7.2921150\times10^{-5}$,
$n_m = 2\pi/(27.321661\ \mathrm{d}) = 2.6617\times10^{-6}\ \mathrm{rad\,s^{-1}}$,
so $\omega_{M2} = 2\omega - 2n_m = 1.405189\times10^{-4}\ \mathrm{rad\,s^{-1}}$
and $T = 2\pi/\omega_{M2} = 44714\ \mathrm{s} = 12.4206\ \mathrm{h}$. The M2–S2
frequency difference is $2(n_m - n_s) = 0.0677\ \mathrm{cycles\,day^{-1}}$
(converting the radian rate with the $2\pi$), so the Rayleigh criterion requires
about $1/0.0677 = 14.8$ days — which the 60-day record satisfies.
**(b)** $\delta = 1 + h_2 - \tfrac32k_2 = 1 + 0.6090 - 0.4560 = 1.1530$: the
$1$ is the direct attraction, $h_2$ the radial displacement of the station
(taller station, smaller $g$), $-\tfrac32k_2$ the mass redistribution inside the
deformed Earth. **(c)** The latitude ratio is what the law predicts:
$83.8668\cos^{2}45^\circ = 41.9334\ \mathrm{\mu Gal}$ against the measured
$41.9279$ — a ratio of $0.9999$. The *absolute* amplitude carries a second
geometric factor, the body's declination: the analytic $95.11\ \mathrm{\mu Gal}$
assumes the body in the equatorial plane, the synthetic Moon reaches
$28.58^\circ$ declination, and the fitted equatorial M2 is
$83.8668\ \mathrm{\mu Gal} = 88.18\%$ of the analytic value. Quote both factors
or neither. **(d)** The four-constituent fit leaks the omitted
constituents into S2; report the longer list and state which constituents were
included, since S2 moves by $18\%$. **(e)** The ocean load tide, which can reach
$10$–$20\%$ of the body tide at coastal sites.

## 11. Common pitfalls

1. **Forgetting the gravity-tide factor.** Predicting the geometry rather than
   $1.15$ times the geometry is a $15\%$ error.
2. **Treating the body tide as the observed tide.** At coastal stations the
   ocean load is comparable to the departures one is trying to measure.
3. **Fitting a short constituent list and believing the amplitudes.** The
   demonstration's S2 moved by $18\%$ when five constituents were added.
4. **Ignoring the Rayleigh criterion.** A record shorter than $1/\Delta f$
   cannot separate two constituents, and the least-squares fit will return two
   numbers anyway.
5. **Assuming the Love numbers are exact.** They are an Earth model, and a $1\%$
   error in $h_2$ is $0.5\%$ in $\delta$.
6. **Confusing the equilibrium tide with a dynamic one.** The solid Earth is
   close to equilibrium; the ocean is not.

## 12. Real-world applications

- **Precise gravimetry and microgravity.** The tide must be removed to the
  microGal level; it is $10^{5}$ times a typical target anomaly.
- **Geodesy.** Tidal displacements (up to $\sim30\ \mathrm{cm}$ radially) enter
  GNSS and levelling reductions; see
  [07-04-03](../04-geodesy-reference-frames/03-gnss-positioning.md).
- **Tidal gravity as an Earth probe.** The amplitude and phase departures from
  the equilibrium tide constrain the ocean load, the anelasticity of the mantle
  and core resonances.
- **Tidal triggering.** Small stress changes modulate seismicity and volcanic
  activity; the same potential is the input.

## 13. Further reading

- **Torge, W. & Müller, J., *Geodesy*** — the classical treatment of tidal
  potential, Love numbers and the gravity factor.
- **Heiskanen, W. A. & Moritz, H., *Physical Geodesy*** — the potential
  expansions used throughout.
- **Stacey, F. D. & Davis, P. M., *Physics of the Earth*** — the elastic and
  anelastic Earth response, and the Earth's rotation.
- **Lambeck, K., *The Earth's Variable Rotation*** — tides as a torque on the
  rotation, and the connection to the next lesson.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Editions and years are omitted
> because they differ between printings.

## 14. Related lessons

- [02 Tidal Corrections in Precise Measurements](02-tidal-corrections.md) —
  how the tide is removed from a survey, and what the removal assumes.
- [03 Earth Rotation, Polar Motion, LOD and Excitation](03-earth-rotation.md) —
  the same potential as a torque on the Earth's rotation.
- [04 Post-Glacial Rebound: Viscosity and Ice History Inference](04-post-glacial-rebound.md) —
  the other large solid-Earth signal that must be removed from gravity.
- [07-05-01 GRACE and GRACE-FO](../05-satellite-gravimetry/01-grace-gracefo.md) —
  why the solid-Earth tide appears in the background models of a satellite
  solution.

## 15. Related modules

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — the
  potential and the reference field.
- [07-05 Satellite Gravimetry](../05-satellite-gravimetry/README.md) — where
  tides are one item in a long list of background models.
- [02 Physics](../../02-physics/README.md) — central forces and elasticity.
- [26-reference-library](../../26-reference-library/README.md) — symbols, units
  and constants used without re-derivation.

## 16. Self-assessment checklist

- [ ] I can derive the tidal potential and explain the absence of degree 1.
- [ ] I can compute the solar/lunar tidal ratio from $\mathrm{GM}/d^{3}$.
- [ ] I can derive constituent frequencies from three rates and check S2.
- [ ] I can compute $\delta$ and say what each term means.
- [ ] I can predict the M2 and K1 latitude dependence and check a fit against it.
- [ ] I can explain why a harmonic residual measures the constituent list.
- [ ] I can name the largest omitted physical effect and its size.
