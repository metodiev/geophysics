# Solutions — 12-01-06 Outer Core, Inner Core Anisotropy and Rotation

Worked solutions for
[06-outer-and-inner-core-exercises.md](./06-outer-and-inner-core-exercises.md). The
lesson is
[06 Outer Core, Inner Core Anisotropy and Rotation](../06-outer-and-inner-core.md).
All models are **SYNTHETIC**.

---

## ★ Foundational

### ★1 — The three estimates of a vertical travel time

**(a) Exact.** With $v$ linear in $r$, $\int_0^L \mathrm{d}x/v = L\ln(v_2/v_1)/(v_2-v_1)$:

$$T = \frac{2258.5}{10.40-8.20}\ln\frac{10.40}{8.20}
= 1026.591 \times 0.237672 = 243.992\ \mathrm{s}.$$

**(b) Arithmetic mean.**
$\bar{v}_\text{arith} = 9.30$ km s$^{-1}$ →
$T = 2258.5/9.30 = 242.849\ \mathrm{s}$.

**(c) Harmonic mean.**
$v_h = 2/(1/8.20 + 1/10.40) = 9.1699$ km s$^{-1}$ →
$T = 2258.5/9.1699 = 246.295\ \mathrm{s}$.

**Which is closest, and why neither is exact.** The harmonic estimate (246.295 s)
is the closest of the two simple ones, but it *overshoots* by 2.3 s (0.9 %) while
the arithmetic estimate undershoots by 1.14 s. The reason is that the correct
average for a *linear gradient* is neither: it is the **logarithmic mean**,

$$\bar{v}_\text{log} = \frac{v_2-v_1}{\ln(v_2/v_1)} = \frac{2.20}{0.237672}
= 9.2565\ \mathrm{km\,s^{-1}},$$

which gives $2258.5/9.2565 = 243.992\ \mathrm{s}$ — exact by construction, because
$T = L/\bar{v}_\text{log}$ is just the integral rewritten. The three means satisfy
$v_h < v_\text{log} < \bar{v}_\text{arith}$, which is why the harmonic estimate gives
the *larger* time. **The practical rule: integrate; any single-number average is an
approximation whose error you should be able to state.**

### ★2 — Elastic moduli and Poisson's ratio of an inner core

$$G = \rho v_s^{2} = 12.90 \times 10^{3} \times 3.55^{2}\times10^{6}
= 1.626\times10^{11}\ \mathrm{Pa} = 162.6\ \mathrm{GPa},$$
$$K = \rho\left(v_p^{2} - \tfrac{4}{3}v_s^{2}\right)
= 12.90\times10^{3}\left(11.15^{2} - \tfrac43 \times 3.55^{2}\right)\times10^{6}
= 1387\ \mathrm{GPa},$$
$$\frac{K}{G} = \frac{1387}{162.6} = 8.53,\qquad
\nu = \frac{11.15^{2} - 2\times3.55^{2}}{2\left(11.15^{2}-3.55^{2}\right)}
= \frac{124.32 - 25.21}{2(124.32-12.60)} = 0.4436.$$

(The unit conversion: $\rho$ in kg m$^{-3}$ and $v$ in m s$^{-1}$ give Pa, so
$\mathrm{g\,cm^{-3}}\times(\mathrm{km\,s^{-1}})^{2}$ needs $\times10^{3}$
from the density and $\times10^{6}$ from the squared velocity.)

**Implication.** A Poisson's ratio of 0.44 with $K/G = 8.5$ describes a *soft*
solid: it is nearly incompressible and easily sheared. For comparison, the mantle's
0.25–0.28 corresponds to $K/G \approx 1.7$–2.1. The inner core's high value is a
strong constraint on its composition — it cannot be a simple dense metal in its
usual crystalline state at those conditions without help from light elements or from
a different crystal structure.

### ★3 — The ICB reflection coefficient

$$Z_\text{oc} = 12.17 \times 10.29 = 125.23, \qquad
Z_\text{ic} = 12.76 \times 11.03 = 140.74,$$
$$R = \frac{140.74 - 125.23}{140.74 + 125.23} = \frac{15.51}{265.97} = +0.0583.$$

**Units.** $Z = \rho v$ carries $\mathrm{g\,cm^{-3}\,km\,s^{-1}}$. In the ratio, the
numerator and denominator are both sums of impedances in the same units, so the units
cancel identically — which is why any *consistent* system works. What does *not*
work is mixing systems between the two impedances (e.g. computing $Z_\text{oc}$ in
$\mathrm{kg\,m^{-3}\,m\,s^{-1}}$ and $Z_\text{ic}$ in
$\mathrm{g\,cm^{-3}\,km\,s^{-1}}$): the ratio would then be wrong by a factor of
$10^{6}$. A useful habit is to quote impedances in
$\mathrm{kg\,m^{-3}\,m\,s^{-1}}$ (Mrayl) or to state the system once.

---

## ★★ Applied

### ★★4 — Anisotropy from a differential time

Invert $\delta t = -A\,\langle A_\text{taper}\rangle\, T_\text{leg}$:

$$A = \frac{|\delta t|}{\langle A_\text{taper}\rangle\,T_\text{leg}}
= \frac{3.375}{0.75 \times 180.0}
= \frac{3.375}{135.0} = 0.0250.$$

So **$A = 2.50\ \%$**. Note the structure of the answer: the numerator is the
measurement, the denominator is *entirely model* (the leg time depends on the
inner-core velocity profile, and the taper on an assumed radial shape). A quoted
anisotropy is therefore a ratio of one measured number to two modelled ones; this
exercise's answer is exact only for the assumed model.

### ★★5 — Splitting and the P/S ratio

**(a)** With $B = 0.005$:

$$\delta t_S = 2B\,T_s = 2 \times 0.005 \times 681.578 = 6.816\ \mathrm{s}.$$

**(b)** For a measured 3.0 s:

$$B = \frac{\delta t_S}{2T_s} = \frac{3.0}{2 \times 681.578} = 2.20\times10^{-3},$$

i.e. **$B = 0.220\ \%$**.

**(c)** With $A = 2\ \%$ and $B = 0.22\ \%$,

$$\frac{A}{B} = \frac{2.0}{0.22} = 9.1.$$

**Why the ratio is the informative quantity.** A single anisotropy value cannot
distinguish between candidate mechanisms, because different mechanisms predict
different *combinations* of $A$ and $B$ for a given degree of alignment. The
elastic tensor of a hexagonal crystal gives a fixed $A/B$ ratio for perfect
alignment; partial alignment scales both together; a mechanism based on melt
pockets or on a different crystal structure changes the ratio. So the pair $(A,B)$
is the measurement, and $A/B$ is the diagnostic. Reporting only one of them leaves
the mechanism unconstrained no matter how precise the value is.

### ★★6 — The rotation rate and the family it belongs to

$$\omega = \frac{\dot{\delta t}}{\left|\mathrm{d}(\delta t)/\mathrm{d}\phi\right|
\times (H/H_\text{ref})}$$

with the demonstration's reference $H_\text{ref} = 0.5\ \%$ and sensitivity
$0.01278$ s per degree. Since the signal scales linearly with $H$, a study assuming
$H = 0.3\ \%$ has an effective sensitivity of
$0.01278 \times 0.6 = 0.007668$ s/deg, so

$$\omega(0.3\ \%) = \frac{0.030}{0.007668} = 3.91\ \mathrm{^\circ\,yr^{-1}},$$
$$\omega(0.6\ \%) = \frac{0.030}{0.015336} = 1.96\ \mathrm{^\circ\,yr^{-1}}.$$

**The family the data determine** is the product

$$\omega \times H = 3.91 \times 0.3 = 1.17\
\mathrm{^\circ\,yr^{-1}\,\% } = 1.96 \times 0.6,$$

i.e. any pair on the hyperbola $\omega H = 1.17$. Reporting "1.96 °/yr" without
"for an assumed 0.6 % heterogeneity" is reporting a point on a curve as if it were a
measurement.

### ★★7 — Splitting from a layer rather than the whole inner core

If the anisotropy is confined to a 200 km thick layer with
$v_s = 3.52\ \mathrm{km\,s^{-1}}$, the two-way S time in that layer is
$2 \times 200/3.52 = 113.6$ s, so

$$B_\text{layer} = \frac{1.5}{2 \times 113.6} = 6.6\times10^{-3},$$

i.e. **0.66 %**. Compare with the whole-inner-core interpretation
($B = 1.5/1363 = 0.11\ \%$): confining the same splitting to a thin layer requires an
anisotropy **six times larger**. The interpretation therefore changes not the
measurement but the *magnitude* of the material property by a factor of six, and the
two possibilities (a weakly anisotropic whole inner core, or a strongly anisotropic
thin layer) make completely different statements about mineral alignment. This is a
sharp instance of the general rule: **splitting measures an integral, and turning an
integral into a material property requires assuming where the material is.**

---

## ★★★ Research-oriented

### ★★★8 — The ensemble average and its bias

For an isotropic distribution of **directions** on the sphere, the mean of
$\cos^{2}\xi$ follows from isotropy of the second moment:
$\langle\cos^{2}\xi\rangle = \langle n_z^{2}\rangle = 1/3$, because
$\langle n_x^2+n_y^2+n_z^2\rangle = 1$ and the three components have equal means by
symmetry. (This is the same argument that gives $\langle\cos^{2}\theta\rangle = 1/3$
for a randomly oriented axis.)

Consequences: if the underlying relation is
$v = v_\text{iso}(1 + A\cos^{2}\xi)$, then a data set with an isotropic direction
mix measures an *average* effect of $A/3$ — so a reported "$A$" from such a set
would be three times smaller than the true $A$ unless the study corrects for it. Two
concrete biases:

1. **An equatorial-only study of PKIKP.** Paths near the equator sample
   $\xi \approx 90°$, so $\cos^{2}\xi \approx 0$: the study measures *nothing* about
   $A$, and any nonzero result is heterogeneity or noise. The bias is total
   (a factor of zero relative to an axial study).
2. **A study restricted to one distance range.** Because the turning radius maps to
   a range of $\xi$ along the path, restricting distances restricts the sampled
   $\xi$. For a data set sampling $\langle\cos^{2}\xi\rangle = 0.15$ instead of the
   global 1/3, the inferred anisotropy is $0.15/(1/3) = 0.45$ times the value a
   globally distributed study would infer — a factor of 2.2 bias from coverage alone.

Both biases are *quantifiable in advance* from the ray geometry, which means a study
can state its effective $\langle\cos^{2}\xi\rangle$ and thus make its anisotropy
comparable with another study's. Very few do.

### ★★★9 — The geometry change and Fermat's principle

**The size of the geometry change.** For a fixed ray parameter, switching on the
anisotropy changes the velocity by $A$, so the turning radius changes by
$\delta r_{tp} \approx A\,r_{tp}$ (to keep $r/v = p$ with $v \to v(1+A)$). For a
demonstration-like shallow-penetrating path with $r_{tp} = 1159$ km and
$A = 0.03$, that is $\delta r_{tp} \approx 35$ km.

**The change in leg time from the geometry alone.** The inner-core leg time is
extremely sensitive to the turning radius for shallow paths, because the path becomes
nearly horizontal: in the demonstration, a 10 km change in $r_{tp}$ near
$r_{tp} \approx 1100$ km changes the leg time by about 25 s. A 35 km change is
therefore worth $\sim$90 s of leg time — *larger* than the anisotropy signal itself
(5.5 s)!

**Why the first-order formula is nevertheless correct.** Fermat's principle states
that the travel time is stationary with respect to *path* perturbations about the
true ray. The 90 s leg-time change is *not* additional signal: it is compensated,
almost exactly, by the change in the outer-core part of the same ray, because the
*ray parameter is held fixed* and the total travel time at fixed $p$ depends only on
the slowness perturbation integrated along the reference path — to first order in
$A$. The correct statement is therefore:

$$\delta t\big|_{\text{fixed }p} = -\int A(r)\cos^{2}\xi\,\frac{\mathrm{d}l}{v}
+ O(A^{2}),$$

and the $O(A^{2})$ term is set by the *curvature* of the travel-time function with
respect to the path. Numerically, the demonstration's full calculation (allowing the
turning radius to move) and the first-order integral agreed to better than 0.1 s on
the paths tested.

### ★★★10 — Separating rotation, heterogeneity and anisotropy

**Observables.**

1. **Differential travel times at fixed ray parameter** between paths with different
   $\cos^{2}\xi$ (axial vs equatorial): the anisotropy signal, $A$-only.
2. **Absolute travel times (or differentials against a reference) on equatorial
   paths** repeated over years: the rotation signal, because equatorial paths have
   $\cos^{2}\xi = 0$ by construction and are therefore anisotropy-blind.
3. **The same paths at several azimuths**: the heterogeneity signal, because a
   rotating pattern produces a *systematic* drift in one azimuthal sense, while
   static heterogeneity is azimuth-dependent but time-independent.
4. **Absolute PKIKP travel times**, which measure the mean inner-core velocity and
   therefore the *magnitude* scale that all three effects are divided by.

**Coverage.** Azimuthally: at least four well-separated azimuths, so that a
$\cos(2\phi)$ pattern's phase can be fitted rather than assumed. Temporally: a
baseline covering of order half the expected rotation period at the target rate —
for 1 °/yr that is 90 years, which is why the rotation literature is limited by
*time*, not by data volume; shorter baselines constrain only the *product*
$\omega H$. Polar: paths with a range of $\cos^{2}\xi$ from 0 to 1 to separate $A$
from the taper shape.

**Forward model.** Ray tracing in a spherically symmetric inner core with
(a) a hexagonal anisotropy $A(r)\cos^{2}\xi$ along the rotation axis, and
(b) a lateral slowness perturbation $H\,f(r)\cos(2(\phi - \omega t))$, fitted jointly
to all the observables above. The unknown vector is $(A_0, \text{taper shape},
H, \phi_0, \omega)$.

**Predicted resolution.** With $N$ independent measurements each of precision
$\sigma$, the rotation rate's uncertainty is
$\sigma_\omega \approx \sigma/(N^{1/2}\,|\mathrm{d}(\delta t)/\mathrm{d}\phi|)$.
Using the demonstration's $|\mathrm{d}(\delta t)/\mathrm{d}\phi| = 0.01278$
s/deg at $H = 0.5\ \%$ and a realistic picking precision of $\sigma = 0.01$ s for
differential times, 100 independent measurements give
$\sigma_\omega \approx 0.01/(10 \times 0.01278) = 0.078\ \mathrm{^\circ\,yr^{-1}}$
**for $H = 0.5\ \%$**, scaling as $1/H$: at $H = 0.1\ \%$ the same data give
$0.39\ \mathrm{^\circ\,yr^{-1}}$. That is the whole point — the rotation rate is
resolved *only* in proportion to the assumed heterogeneity, so the design priority is
an independent constraint on $H$, not more measurements of the same kind.

---

## Mastery checkpoint — worked version

> Differential time $-1.8$ s; two paths with leg times 190 s and 95 s and mean taper
> factors 0.80 and 0.35; secular change $0.015\ \mathrm{s\,yr^{-1}}$ with
> $H$ assumed to be 0.4 %.

**(a) The anisotropy implied by each path.**

$$A_1 = \frac{1.8}{0.80 \times 190} = \frac{1.8}{152.0} = 0.01184
\;(1.18\ \%),$$
$$A_2 = \frac{1.8}{0.35 \times 95} = \frac{1.8}{33.25} = 0.05414
\;(5.41\ \%).$$

They **disagree by a factor of 4.6**. A single differential of $-1.8$ s is a
different statement depending on which path produced it, and the two paths cannot
both be described by the same $A$. The likely explanations, in order of
plausibility: (i) the two "paths" are actually different phases or the picks are
contaminated, since a factor of 4.6 exceeds any reasonable modelling error;
(ii) the radial shape (taper) is wrong, so the weights 0.80 and 0.35 are wrong;
(iii) the leg times are wrong, which would need a 4.6× error in the inner-core
velocity model — implausible. **This is precisely why anisotropy studies fit many
paths simultaneously rather than inverting one differential at a time.**

**(b) Rotation rate.** With the demonstrated sensitivity
$\mathrm{d}(\delta t)/\mathrm{d}\phi = -0.01278$ s/deg at $H_\text{ref} = 0.5\ \%$,
the sensitivity at 0.4 % is $0.01278 \times 0.8 = 0.010224$ s/deg, so

$$\omega(0.4\ \%) = \frac{0.015}{0.010224} = 1.47\ \mathrm{^\circ\,yr^{-1}},
\qquad
\omega(0.2\ \%) = \frac{0.015}{0.005112} = 2.93\ \mathrm{^\circ\,yr^{-1}}.$$

The data determine the product $\omega H = 1.47 \times 0.4 = 0.588\ (1.17$ at
0.2 %); the rate itself is the product divided by a modelled number.

**(c) Why (a) and (b) are not independent.** Both are calibrated by the *same*
inner-core path geometry: the differential times that give $A$ and the secular change
that gives $\omega H$ are both integrals of the form
$\int(\text{perturbation})\,\mathrm{d}l/v$ along inner-core legs. An error in the
inner-core velocity model rescales both; an error in the assumed taper shape
redistributes both; and the anisotropy itself changes the turning radii of the
rotation-sensitive paths, which changes their sensitivity to the rotating pattern.
So a joint inversion is required, and the joint uncertainties are larger than either
single-parameter inversion suggests.

**(d) What would make each answer unconditional.**

- For **(a)**: an independent constraint on the radial shape of the anisotropy — for
  example a dense set of paths spanning the full inner-core depth range, fitted
  simultaneously for $A_0$ *and* the taper, with the covariances reported. Even then,
  a constant-$A$ model and a taper model can fit the same data with different
  magnitudes, so the honest output is a family.
- For **(b)**: an independent estimate of the heterogeneity amplitude and pattern,
  from a different observable (e.g. a laterally varying travel-time anomaly mapped at
  a single epoch), plus long enough a time series to observe the 180° periodicity
  rather than a single slope. Until then, the answer is
  $\omega H = 0.588$, not $\omega = 1.47$.

**Condition for adequacy of the first-order formula.** The second-order term is of
order $A^{2}\,r_{tp}^{2}\,\partial^{2}T/\partial r_{tp}^{2}$. Because
$\partial^{2}T/\partial r_{tp}^{2}$ grows without bound as the path grazes a
discontinuity — here the ICB, where $v$ jumps — the first-order formula is safe for
$A \lesssim$ a few per cent on ordinary paths, but a study using grazing paths must
verify it numerically. That verification is one line of code: recompute the travel
time with the anisotropic velocity *and* the anisotropic turning radius, and compare
with the first-order integral. The demonstration does exactly this, and finds
agreement to better than 0.1 s on the paths tested.
