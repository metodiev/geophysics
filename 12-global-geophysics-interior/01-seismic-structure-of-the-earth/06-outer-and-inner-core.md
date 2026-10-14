---
id: 12-01-06
title: "Outer Core, Inner Core Anisotropy and Rotation"
level: research
prereqs: ["12-01-01", "12-01-05", "06-01-02", "06-02-02"]
tags: [global-geophysics, earth-interior, outer-core, inner-core, anisotropy, rotation, differential-times]
---

# Outer Core, Inner Core Anisotropy and Rotation

> **All models and data in this module are SYNTHETIC.** Velocities, densities,
> anisotropy parameters, heterogeneity amplitudes and rotation rates used here are
> chosen teaching values. No seismogram, station, catalogue or published
> measurement is used. The ICB radius (1221.5 km) and the core velocities are the
> chosen values carried through from lesson 01.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the vertical travel time through the outer and inner core from a
   radial velocity profile, and **explain** why the correct average is harmonic.
2. **Derive** the inner core's elastic moduli and Poisson's ratio from $v_p$, $v_s$
   and $\rho$, and **state** what $K/G \approx 8.6$ says about the material.
3. **Derive** the first-order differential travel time produced by hexagonal
   anisotropy, $\delta t = -\int A(r)\cos^{2}\xi\,\mathrm{d}l/v$, and **compute** it
   for paths of different depth penetration.
4. **Compute** the shear-wave splitting implied by a given S anisotropy, and
   **compare** the P and S anisotropy requirements for a stated observation.
5. **Compute** the secular travel-time change produced by a rotating lateral
   heterogeneity, and **invert** a measured rate for a rotation rate conditional on
   the heterogeneity amplitude.
6. **Explain** why the heterogeneity, the anisotropy and the rotation form a coupled
   inverse problem, and **construct** the degeneracy families that connect them.
7. **State** which quantities in this lesson are measured and which are modelled.

## Prerequisites

- [12-01-01 PREM, IASP91 and Reference Earth Models](01-prem-and-reference-models.md) —
  the radial model and the ray parameter.
- [12-01-05 Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite](05-core-mantle-boundary.md) —
  what happens at the *upper* boundary of the outer core.
- [06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md) —
  polarisation, which is what splitting measures.
- [06-02-02 Snell's Law, Layered Media and the Travel-Time Curve](../../06-seismology/02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  the ray parameter in a sphere.

## 1. The core as a laboratory

Three facts about the core are established by seismology alone, and each one comes
from a *different kind* of measurement:

| fact | how it is established |
|---|---|
| the outer core is liquid | S waves do not propagate through it (no S impedance) |
| the inner core is solid | P waves transmit through it, and it supports shear |
| the inner core is anisotropic | travel times depend on the direction the path travels |

The first two are binary conclusions from the *existence* of phases; the third is a
quantitative inference from *differences between* travel times. This lesson is
mostly about the third, because it is where the assumptions and the degeneracies
live.

Two structural numbers frame everything. The demonstration's SYNTHETIC core
profiles are

- outer core: $v_p$ from 8.06 km s$^{-1}$ at the CMB to 10.29 km s$^{-1}$ at the
  ICB, $\rho$ from 9.90 to 12.17 g cm$^{-3}$, $v_s = 0$;
- inner core: $v_p$ from 11.03 to 11.26 km s$^{-1}$, $v_s$ from 3.50 to
  3.67 km s$^{-1}$, $\rho$ from 12.76 to 13.09 g cm$^{-3}$.

## 2. Radial travel times and the harmonic average

For a radial path ($p = 0$) the ray integrals of
[lesson 01](01-prem-and-reference-models.md) collapse to
$T = \int \mathrm{d}r/v(r)$, and the demonstration integrates them:

| path | length (km) | $T$ (s) | implied mean $v_p$ (km s$^{-1}$) |
|---|---|---|---|
| CMB → ICB (outer core) | 2258.5 | **247.381** | length/time = 9.1297 |
| centre → ICB (inner core) | 1221.5 | **109.605** | length/time = 11.1446 |

Both are *one-way* times. Two remarks:

- The implied mean is the **harmonic** mean. The arithmetic mean of the outer-core
  endpoints is $(8.06+10.29)/2 = 9.175\ \mathrm{km\,s^{-1}}$, which is 0.5 % larger
  than the harmonic mean 9.130 — hence a travel time from an arithmetic average is
  systematically short. The same trap as in lesson 01.
- The inner core's mean $v_p$ of 11.1446 km s$^{-1}$ is the number seismic
  tomography and mineral physics must reproduce when they ask what the inner core is
  made of ([12-02-04](../02-composition-and-mineral-physics/04-core-composition.md)).

## 3. The ICB as a boundary, and what it makes the inner core

The normal-incidence P reflection coefficient at the ICB follows from the
impedances. Just above the ICB (outer core, using the bottom-of-outer-core values)
$Z = 12.17 \times 10.29 = 125.23$; just below (inner core)
$Z = 12.76 \times 11.03 = 140.74$:

$$R = \frac{140.74 - 125.23}{140.74 + 125.23} = \frac{15.51}{265.97} = +0.0583,$$

a 5.8 % P reflection — small, but an order of magnitude larger than the 2 %
reflection at the CMB (lesson 05), which is why the ICB is a visible reflector in
long-period stacks and why PKiKP exists as a distinct phase.

The inner core's *solidity* is then a statement about elasticity. From
$G = \rho v_s^2$ and $K = \rho\left(v_p^2 - \tfrac{4}{3}v_s^2\right)$ at the ICB:

$$G = 12.76 \times 3.50^{2} = 156.3\ \mathrm{GPa}, \qquad
K = 12.76 \times \left(11.03^{2} - \tfrac{4}{3}\times 3.50^{2}\right)
= 1344\ \mathrm{GPa},$$

so $K/G = 8.60$ and

$$\nu = \frac{v_p^{2} - 2v_s^{2}}{2\left(v_p^{2} - v_s^{2}\right)}
= \frac{121.66 - 24.50}{2\left(121.66 - 12.25\right)} = 0.4440.$$

Poisson's ratio of 0.44 is *very* high — the mantle sits at 0.25–0.28, and a value
near 0.5 means the material resists compression far more than shear. In words: the
inner core is a **soft solid**, nearly rigid in compression and easily sheared. That
is a strong mineralogical statement, and it is one of the reasons the light-element
content of the core is an open question (lesson
[12-02-04](../02-composition-and-mineral-physics/04-core-composition.md)).

## 4. Inner-core anisotropy

### 4.1 The measurement

If the inner core is elastically anisotropic with a symmetry axis along the rotation
axis, a path whose direction makes an angle $\xi$ with that axis travels at

$$v(\xi) = v_\text{iso}\left(1 + A(r)\cos^{2}\xi\right),$$

with $A(r)$ the fractional anisotropy (positive for a fast axis). The travel time
difference between a path at angle $\xi$ and an isotropic path follows to first
order from $\delta t = -\int \delta v\, \mathrm{d}l / v^{2}$:

$$\boxed{\;\delta t = -A\cos^{2}\xi \int_\text{inner core} A(r)\,
\frac{\mathrm{d}l}{v}\;}$$

(the inner $A$ inside the integral is the radial shape, the outer one the magnitude).
The sign is what the physics requires: a *faster* path gives a *negative*
differential. And Fermat's principle is why this first-order form is legitimate: the
change in the *path* is a second-order contribution to the time, so only the
velocity change along the reference path matters.

### 4.2 Computed differentials

With $A_0 = 3.0\ \%$ and a taper from a quarter of full strength at the ICB to full
strength below 400 km depth, the demonstration integrates along paths of different
ray parameter:

| $p$ (s rad$^{-1}$) | $r_{tp}$ (km) | inner-core path length (km) | leg time (s) | mean taper | $\delta t$ (s) |
|---|---|---|---|---|---|
| 10.0 | 112.4 | 2431.7 | 218.257 | 0.843 | **−5.521** |
| 30.0 | 335.9 | 2344.3 | 210.688 | 0.830 | −5.245 |
| 50.0 | 557.7 | 2165.1 | 194.936 | 0.794 | −4.645 |
| 70.0 | 777.9 | 1872.2 | 168.925 | 0.695 | −3.520 |
| 90.0 | 996.5 | 1401.4 | 126.736 | 0.401 | −1.525 |
| 105.0 | 1159.4 | 761.7 | 69.011 | 0.273 | −0.566 |

Three structural facts to read off:

1. **The differential is a few seconds** — and it is the *whole* measurement. There
   is no way to measure the anisotropy of a single direction; only differences are
   observable.
2. **It grows with the length of the inner-core leg** (218 s of leg at $p = 10$
   against 69 s at $p = 105$), because $\delta t \propto \int A\,\mathrm{d}l/v$. A
   study with only shallow-penetrating paths sees a much weaker signal.
3. **The mean taper falls for shallow paths** (0.843 → 0.273), because shallow
   paths spend their time in whatever weak-anisotropy skin the model has. This is
   why a *radially varying* anisotropy and a *constant* one can produce the same
   data set with different magnitudes — a degeneracy inside the anisotropy problem
   itself.

### 4.3 The ensemble problem

Because $\delta t \propto \cos^{2}\xi$, the *reported* anisotropy depends on the
directions a study happens to sample. For an isotropic distribution of ray
directions, $\langle\cos^{2}\xi\rangle = 1/3$, so the same material would appear
three times less anisotropic than an axial-only data set would suggest. Real
studies do not usually adopt the convention
$v = v_\text{iso}\left[1 + A\left(\cos^{2}\xi - \tfrac13\right)\right]$, which makes
$v_\text{iso}$ the directionally averaged velocity — and when they do not, the
"isotropic velocity" in a paper is not the same quantity as in the next paper. **A
quoted anisotropy is a quoted geometry as well as a quoted material property.**

## 5. Shear-wave splitting

A hexagonal medium splits an S wave into two polarisations with different speeds.
The demonstration's SYNTHETIC parametrisation is
$v_{s1,s2} = v_s(1 \pm B\cos^{2}\xi)$, so with $B = 1\ \%$ the two polarisations
differ by $2B = 2\ \%$ along an axial path. The two-way S travel time through the
inner core is

$$T_s = 2\int_0^{R_{ICB}} \frac{\mathrm{d}r}{v_s(r)} = 681.578\ \mathrm{s},$$

so the splitting is

$$\delta t_S = 2B\,T_s = 0.02 \times 681.578 = 13.632\ \mathrm{s}$$

for $B = 0.01$. Inverting for the $B$ implied by a measured splitting:

| observed splitting (s) | implied $B$ (%) |
|---|---|
| 0.5 | 0.037 |
| 1.0 | 0.073 |
| 2.0 | 0.147 |
| 4.0 | 0.293 |

The point of this table is the **size**: a *modest* observed splitting corresponds to
a *very small* S anisotropy once the long S travel time through the inner core is
accounted for. The P anisotropy and the S anisotropy are therefore separate
measurements, and **their ratio is the diagnostic**. A mechanism that aligns
crystals produces both in a fixed proportion set by the mineral's elastic tensor; a
mechanism based on alignment, melt or texture produces a different ratio. Quoting
one without the other leaves the mechanism undetermined — which is exactly the state
of the discussion about what makes the inner core anisotropic.

## 6. Inner-core rotation

### 6.1 The mechanism and the geometry

If the inner core is laterally heterogeneous and rotates relative to the mantle, a
fixed seismic path samples a changing piece of structure, so its travel time drifts.
The demonstration models this with a $\cos(2\phi)$ heterogeneity of amplitude 0.5 %
in the equatorial plane, tapered over the outer 200 km of the inner core, and uses a
path in the *equatorial* plane so that $\cos^{2}\xi = 0$ and the P anisotropy is
inert by construction.

Geometry: a straight chord at perpendicular distance 921.5 km from the axis has a
half-length 801.8 km, an inner-core leg length of **1603.6 km**, and a one-way
travel time of **144.910 s**.

### 6.2 The signal

| rotation of the pattern (deg) | travel-time change (s) |
|---|---|
| 0 | 0.0000 |
| 30 | −0.1831 |
| 60 | −0.5492 |
| 90 | −0.7323 |
| 120 | −0.5492 |
| 150 | −0.1831 |
| 180 | 0.0000 |

Two features matter:

- **The signal is periodic in 180°.** A $\cos(2\phi)$ pattern is invariant under a
  half turn, so the observed curve cannot distinguish a fast rotation from a slow
  one without additional information about the pattern's *orientation history*.
- **The observed rate depends on the orientation.** Scanning the pattern's phase,
  the travel-time change per degree of rotation runs from 0 (when the pattern is
  symmetric about the path) to a maximum of **−0.01278 s per degree**. A measured
  *zero* secular change therefore does not mean no rotation: it may mean the
  pattern is currently symmetric about the path.

### 6.3 The rate

| assumed rotation rate (°/yr) | predicted change (s/yr) |
|---|---|
| 0.05 | −0.0006 |
| 0.10 | −0.0013 |
| 0.50 | −0.0064 |
| 1.00 | −0.0128 |
| 2.00 | −0.0256 |

and inverting a hypothetical measured 0.020 s/yr:

| heterogeneity amplitude (%) | implied rotation rate (°/yr) |
|---|---|
| 0.1 | 7.83 |
| 0.25 | 3.13 |
| 0.5 | 1.57 |
| 1.0 | 0.78 |
| 2.0 | 0.39 |

**The rate is not measured.** What is measured is the product
$\omega \times H$ (rotation rate times heterogeneity amplitude). The inversion above
is a division, and the divisor is not a data product. This is the single most
important thing to understand about inner-core rotation claims.

## 7. The coupled inverse problem

Collect the three degeneracies:

| quantity | what the data constrain | what breaks it |
|---|---|---|
| P anisotropy $A$ | $A \times$ (leg time) $\times$ (mean taper) | paths of different penetration depth |
| S anisotropy $B$ | $B \times T_s$ (a long lever) | a measurement of $T_s$, which needs the S velocity |
| rotation $\omega$ | $\omega \times H$ × orientation | an independent $H$, or a longer time series covering the 180° cycle |
| heterogeneity $H$ | its *pattern* through the time dependence | an independent model of the inner core's lateral structure |

And one more, which is the reason this is described as a coupled problem rather
than three separate ones: because the *same* anisotropy that makes an axial path
fast also makes its turning depth shallower, and the inner-core leg time is very
sensitive to the turning depth, a change in $A$ changes not just the velocity along
the path but the length of the path in the inner core. In the demonstration, a 3 %
axial velocity change moves the turning radius of a shallow-penetrating ray by
about 10 km, which by itself changes the inner-core leg time by tens of seconds. A
naive "$\delta t$ = anisotropy × leg time" argument therefore over- or under-states
the effect depending on which paths are used — which is exactly why the
first-order integral of Section 4.1 (evaluated along the *reference* path) is the
right formulation, and why full-waveform and ray-tracing studies are used when the
anisotropy is large.

A further degeneracy is worth naming: **anisotropy and heterogeneity both produce
azimuth-dependent travel times.** An anisotropic inner core and a heterogeneous one
are distinguished by their *symmetry* (anisotropy is symmetric about the axis and
180°-periodic in azimuth; a specific heterogeneity is not) and by their *time
dependence*. Distinguishing them requires broad azimuthal coverage, not more data
of the same kind.

## 8. Assumptions and regime of validity

1. **Hexagonal symmetry with the axis along the rotation axis.** If the symmetry
   axis is tilted (as some studies require), the simple $\cos^{2}\xi$ form is
   replaced by a five-parameter expansion and the differential times pick up
   azimuthal dependence with a 90° period.
2. **First-order perturbation.** $\delta t = -\int A\cos^{2}\xi\,\mathrm{d}l/v$ is
   linear in the perturbation, valid for $A \lesssim$ a few per cent. Path changes
   are second order by Fermat's principle, but the *turning-depth* sensitivity of a
   shallow inner-core path is large enough that this deserves checking numerically
   for each geometry.
3. **A known reference inner-core velocity.** Everything scales with $\int
   \mathrm{d}l/v$, so a 2 % velocity error is a 2 % error on the anisotropy.
4. **The taper is assumed.** The radial shape of the anisotropy is not measured
   independently; it trades off against the magnitude, as Section 4.2 shows.
5. **A lateral heterogeneity with an assumed pattern.** The rotation inference uses
   $\cos(2\phi)$, a chosen shape. A different pattern gives a different
   $\mathrm{d}(\delta t)/\mathrm{d}\phi$.
6. **No differential rotation of the outer core.** A rotating inner core implies
   torques through the outer core; the dynamical consistency of any claimed rate is
   a separate question.
7. **The inner core is solid, not partly molten.** Phase existence arguments are
   strong but not infinitely sharp.

## 9. Worked examples

### Example 1 — the outer-core vertical time and the right average

From the endpoints alone, the outer-core vertical time is *not*
$2258.5/9.175 = 246.16\ \mathrm{s}$ using the arithmetic mean. The demonstration's
integral gives $247.381\ \mathrm{s}$. The difference is

$$247.381 - 246.16 = 1.22\ \mathrm{s},$$

i.e. **0.5 %** — the size of the anomaly signals this module is built around. The
harmonic mean of the endpoints is
$2/(1/8.06 + 1/10.29) = 9.0395\ \mathrm{km\,s^{-1}}$, giving
$2258.5/9.0395 = 249.85\ \mathrm{s}$, which *over*-estimates by 2.5 s because the
velocity profile is linear in $r$ rather than harmonic. The exact value lies between
the arithmetic and harmonic estimates: the correct average is the one defined by
$\int \mathrm{d}r/v$, which no single-number summary reproduces exactly for a thick
shell. **Integrate; do not average.**

### Example 2 — a differential time from the formula

For $p = 10\ \mathrm{s\,rad^{-1}}$, the demonstration gives an inner-core leg time of
218.257 s and a taper-weighted mean of 0.843. Then

$$\delta t = -A \times \langle A_\text{taper}\rangle \times T_\text{leg}
= -0.030 \times 0.843 \times 218.257 = -5.521\ \mathrm{s},$$

matching the printed value exactly (the printed column *is* this product). Inverting:
a measured axial–equatorial differential of $-2.0$ s on such a path implies
$A_0 = 2.0/(0.843 \times 218.257) = 1.09\ \%$. **The anisotropy is
(measured differential)/(leg time × taper)**, so an error in the leg time — i.e. in
the inner-core velocity model — is a proportional error in the anisotropy.

### Example 3 — from a measured rate to a rotation rate and back

A study measures a secular change of 0.020 s/yr on an equatorial path. Using the
demonstration's sensitivity of $-0.01278$ s per degree:

$$\omega = \frac{0.020}{0.01278} = 1.57\ \mathrm{^\circ\,yr^{-1}},$$

**conditional on a heterogeneity amplitude of 0.5 %**. If the same study had assumed
0.25 %, the answer would be 3.13 °/yr. The honest report is a one-parameter family:
$\omega H = 0.0079\ \mathrm{\%\,^\circ\,yr^{-1}}$ (the product $\omega \times H$
equals 1.57 × 0.5). Any paper that reports a rate without an explicit statement of
the heterogeneity amplitude used to get it has hidden the assumption inside a
number.

## 10. Python demonstration

`code/outer_and_inner_core_demo.py` builds the core profiles, integrates the radial
travel times, forms the ICB reflection coefficient and the elastic moduli, computes
the inner-core leg lengths and the first-order anisotropy differential for a range of
penetration depths, evaluates the S splitting, models a rotating lateral
heterogeneity and its travel-time signature (including the orientation scan), and
assembles the degeneracy tables. It prints labelled results with units and runs in
under 0.1 s:

```bash
cd 12-global-geophysics-interior/01-seismic-structure-of-the-earth/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python outer_and_inner_core_demo.py
```

## 11. Exercises

Full sets with worked solutions are in
[`exercises/06-outer-and-inner-core-exercises.md`](exercises/06-outer-and-inner-core-exercises.md)
and
[`exercises/06-outer-and-inner-core-solutions.md`](exercises/06-outer-and-inner-core-solutions.md).

- **★** Integrate a radial travel time and compare with an arithmetic-mean estimate.
- **★★** Compute the anisotropy implied by a differential time on a stated path.
- **★★** Compute the splitting implied by an S anisotropy and the ratio to a P
  anisotropy.
- **★★★** Design a data set that separates rotation from heterogeneity and from
  anisotropy, with a predicted resolution.

## Mastery checkpoint

Without notes:

> An equatorial-path study reports a differential travel time of $-1.8\ \mathrm{s}$
> between two paths whose inner-core leg times are 190 s and 95 s, mean taper
> factors 0.80 and 0.35 respectively, and a secular change of $0.015\ \mathrm{s\,yr^{-1}}$
> with a heterogeneity amplitude assumed to be 0.4 %.
> **(a)** Compute the P anisotropy implied by each path separately and say whether
> they agree.
> **(b)** Compute the rotation rate for the stated heterogeneity, and the rate implied
> if the heterogeneity were 0.2 %.
> **(c)** State why (a) and (b) are not independent.
> **(d)** State what would have to be measured to make each answer unconditional.

A worked version appears in the lesson-06
[solutions](exercises/06-outer-and-inner-core-solutions.md).

## Common pitfalls

1. **Treating the rotation rate as measured.** Only $\omega H$ is measured; the rest
   is a division.
2. **Forgetting the 180° periodicity.** A $\cos(2\phi)$ pattern gives a zero secular
   rate at two orientations out of every half turn.
3. **Quoting an anisotropy without saying which directions the data sample.** The
   ensemble average of $\cos^{2}\xi$ is 1/3; the reported value depends on it.
4. **Assuming a taper.** The radial shape of the anisotropy trades off against its
   magnitude.
5. **Using an arithmetic mean velocity** either in the core or along a path.
6. **Confusing $A$ and $B$.** The P and S anisotropies are different measurements
   with different physical implications, and their ratio is the informative quantity.
7. **Assuming the symmetry axis is the rotation axis.** If it is tilted, the
   differential times acquire a 90° azimuthal dependence that a simple model will
   misinterpret as heterogeneity.

## Related modules

- [01 PREM, IASP91 and Reference Earth Models](01-prem-and-reference-models.md) —
  the ray integrals reused here.
- [05 Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite](05-core-mantle-boundary.md) —
  the upper boundary of this region, and the total-reflection argument for S.
- [12-02-04 Core Composition, Light Elements and the Geodynamo](../02-composition-and-mineral-physics/04-core-composition.md) —
  what the velocities and the $K/G$ ratio imply about composition.
- [06-01-08 Anisotropic Propagation](../../06-seismology/01-elastic-wave-propagation/08-anisotropic-propagation.md) —
  the general theory of hexagonal symmetry and splitting.
- [12-04-03 Palaeomagnetic Record and Reversal Frequency](../04-geomagnetism-and-core/03-palaeomagnetic-record.md) —
  the record that constrains the core's thermal history, and hence its solidification.

## Self-assessment checklist

- [ ] I can integrate a radial travel time and explain the harmonic mean.
- [ ] I can compute $G$, $K$ and $\nu$ from $v_p$, $v_s$ and $\rho$.
- [ ] I can derive the first-order differential time from a velocity perturbation.
- [ ] I can compute a differential for a stated path geometry.
- [ ] I can compute an S splitting and state the implied $B$.
- [ ] I can compute the travel-time signature of a rotating heterogeneity.
- [ ] I can invert a measured rate for $\omega$ and state the assumption.
- [ ] I can write the three degeneracy relations from memory.
