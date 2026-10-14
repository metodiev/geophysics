# Solutions — 02-02-01 Kinematics in One and Two Dimensions

> **Read this after attempting the exercises, not before.**
>
> Every number was computed. All values use
> $g = 9.82025\ \mathrm{m\,s^{-2}}$, derived from the defining $GM_\oplus$ and a
> nominal mean radius, and $1\ \mathrm{yr} = 3.1557\times10^{7}$ s.

---

## ★1 — Deriving the constant-acceleration relations

With $a = a_0$ constant,

$$v(t) = v_0 + \int_0^{t}a_0\,dt' = v_0 + a_0t, \qquad
x(t) = x_0 + \int_0^{t}v(t')\,dt' = x_0 + v_0t + \tfrac12a_0t^{2}.$$

Eliminating $t = (v-v_0)/a_0$ from the first and substituting into the second:

$$x - x_0 = \frac{v^{2}-v_0^{2}}{2a_0}
\quad\Longrightarrow\quad
v^{2} = v_0^{2} + 2a_0(x-x_0).$$

**The step that requires constant $a$** is the very first one: pulling $a$ out of
the integral. Everything downstream inherits that assumption, which is why
$v^{2} = v_0^{2}+2a\Delta x$ may not be applied across a segment where the
acceleration varies (a rocket, a body crossing the drag regime boundary).

---

## ★2 — Free fall from four heights

| $h$ (m) | $t = \sqrt{2h/g}$ (s) | $v = gt$ (m/s) |
|---|---|---|
| 10 | 1.427098 | 14.0145 |
| 100 | 4.512879 | 44.3176 |
| 400 | 9.025759 | 88.6352 |
| 1000 | 14.270977 | 140.1446 |

**Where constant $g$ errs by more than 0.01%.** The field is
$g(r) = GM/r^{2}$, so over a height $h$ the relative change is $2h/R$: this
exceeds $10^{-4}$ when $h > 5\times10^{-5}R = 0.32$ km. So the constant-$g$
assumption is *already* at the 0.01% level by a few hundred metres, which is fine
for a drop test but worth stating. Also note that drag, not the variation of $g$,
is the dominant error for any real dropped object — a 1000 m fall in air differs
from the vacuum time by far more than 0.01%.

---

## ★3 — Projectile ranges and apexes at three angles

| Launch angle | range $v_0^{2}\sin2\theta/g$ (m) | apex $v_0^{2}\sin^{2}\theta/2g$ (m) |
|---|---|---|
| 30° | 55.1173 | 7.9555 |
| 45° | 63.6440 | 15.9110 |
| 60° | 55.1173 | 23.8665 |

30° and 60° give the same range because $\sin2\theta$ is symmetric about 45°
($\sin60° = \sin120°$). The 60° launch reaches a **higher apex** (23.87 m against
7.96 m) because more of the initial speed is vertical; the range is the same
because the longer flight time of the steeper launch exactly compensates its
smaller horizontal speed. All of this assumes a flat Earth, no drag, and $g$
constant along the trajectory.

---

## ★4 — Unit conversions

| | Conversion | Result |
|---|---|---|
| (a) | $7\ \mathrm{cm\,yr^{-1}} = 70\ \mathrm{mm\,yr^{-1}}$; divide by $3.1557\times10^{7}$ s/yr | $2.218\times10^{-9}\ \mathrm{m\,s^{-1}}$ |
| (b) | multiply by $10^{3}$ mm/m and $3.1557\times10^{7}$ s/yr | $1.578\times10^{14}\ \mathrm{mm\,yr^{-1}}$ |
| (c) | $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ | $10^{-5}\ \mathrm{m\,s^{-2}}$ |

**Rate of motion versus rock property.** (a) is a *ground motion rate* — the
station, or the fault, is moving. (b) is a *rock property*: a seismic wave speed
is a material parameter of the medium, not a motion of the ground; confusing the
two is the most common category error in introductory seismology. (c) is an
acceleration — a quantity a *gravimeter measures*, related to the field, not to a
motion at all.

---

## ★★5 — Horizontal launch and the curvature it ignores

**(a)** Vertical motion is free fall from 100 m:
$t = \sqrt{2\times100/9.82025} = 4.512879$ s, and the horizontal distance is
$x = v_0t = 1000\times4.512879 = 4512.88$ m.

**(b)** The surface curves away by
$x^{2}/(2R) = (4512.88)^{2}/(2\times6.371\times10^{6}) = 1.598$ m.

**(c)** The flat-Earth error is 1.6 m over a 4.5 km range. That is 0.035% of the
range — comparable to the neglect of drag, and much larger than any curvature
effect that a 1 m accuracy requirement could tolerate. **The criterion should be
stated as a ratio**, e.g. "accept the flat-Earth approximation while
$x^{2}/(2R) \ll$ the height tolerance", and here it is not satisfied for a
metre-level application.

---

## ★★6 — Drag regime speeds

Drag equals gravity when $g = cv^{2}$:

| $c$ (m⁻¹) | $v_{\text{drag}} = \sqrt{g/c}$ (m/s) |
|---|---|
| $1\times10^{-3}$ | 99.10 |
| $2\times10^{-3}$ | 70.07 |

**Regime statement.** Below roughly $0.3\,v_{\text{drag}}$ (i.e. below about
30 m/s and 21 m/s for the two cases) the drag acceleration is under 10% of $g$,
so a vacuum ballistic calculation carries an error of that order in the speed
and somewhat less in the range. Above $v_{\text{drag}}$ a vacuum calculation is
qualitatively wrong: it predicts unlimited speed, where the real body approaches
a terminal speed. State the criterion as a speed, never as "for slow motion".

---

## ★★7 — A fitted rate, and how long a tectonic signal takes

**(a)** With $n = 365$, $\Delta t = 1/365$ yr and $\sigma = 0.01$ m,

$$\sigma_v = \sigma\sqrt{\frac{12}{n(n^{2}-1)}}\frac{1}{\Delta t}
= 0.01\times\sqrt{\frac{12}{365(365^{2}-1)}}\times\frac{1}{1/365}
= 1.8132\times10^{-3}\ \mathrm{m\,yr^{-1}} = \mathbf{1.81\ mm\,yr^{-1}}.$$

**(b)** $n = 730$: $0.6411$ mm/yr. $n = 1095$: $0.3489$ mm/yr.
(The scaling is close to $n^{-3/2}$, as the module states.)

**(c)** For a 2σ detection of a 2 mm/yr signal, the 1σ rate uncertainty must be
below 1 mm/yr, which happens between 1 and 2 years of daily data: interpolating
the $n^{-3/2}$ law, $n \approx 365\times(1.8132/1.0)^{2/3} = 545$ days. So
**about 1.5 years** of daily data, in the ideal white-noise case.

**(d)** The formula assumes **independent (white) noise** with a known constant
variance. Real GNSS series contain common-mode error shared between nearby
stations, coloured noise (random-walk and flicker components) and offsets from
equipment changes; all of these inflate the rate uncertainty, typically by a
factor of several. The remedy is a network solution and a realistic noise model
(see [02-01-02](../../01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)),
not more of the same data.

---

## ★★8 — Borehole drop

**(a)** $t_{\text{vac}} = \sqrt{2\times400/9.82025} = 9.025759$ s and
$v = gt = 88.6352\ \mathrm{m\,s^{-1}}$.

**(b)** With $c = 2\times10^{-3}\ \mathrm{m^{-1}}$ the module's demonstration
integrates the quadratic-drag equations and obtains **10.2635 s**, longer than
the vacuum time by **+1.2377 s** (13.7%). Quoting the demonstration is legitimate
provided you say so; the number is reproducible by integrating
$\dot v = -g - cv^{2}$ numerically.

**(c)** The crew should use the **drag** value, because the instrument has to
travel in air. Note also that the difference is measured, not modelled, if the
probe's mass and cross-section are known: a timing residual of 1.24 s against the
vacuum prediction is a measurement of $c$ (see ★★★9).

---

## ★★★9 — Designing a drop-calibration experiment

**(a)** With downward-positive $z$ and quadratic drag,
$\dot v = -g - c\,v^{2}$ (equivalently, with $z$ downward,
$\ddot z = g - c\dot z^{2}$). Written in terms of $\tau = t\sqrt{gc}$ and
$u = v\sqrt{c/g}$ (or simply by inspection), the motion depends on two
dimensionless quantities:

$$T\sqrt{gc} = f(\text{initial condition}), \qquad
\frac{v_0}{\sqrt{g/c}} = \frac{v_0}{v_{\text{drag}}},$$

i.e. a **dimensionless time** built from $c$ and $g$, and a **speed ratio** to
the terminal speed. The penetration distance adds $cL$ as a third parameter.

**(b)** To determine $c$ you need (i) a measured total time $T$ with known
precision, (ii) either the impact speed or a second timing at a known depth
(photogates or accelerometer records), and (iii) the release conditions. With
1 ms timing on a 9–10 s fall the fractional timing precision is $10^{-4}$, which
propagates to a similar fractional precision on $c$ once gravity is subtracted;
the dominant error is the release mechanism, not the clock.

**(c)** A **systematic timing offset** (release delay, trigger threshold, clock
bias) shifts the measured time by the *same* amount regardless of the probe's
mass, cross-section or drop depth, and it does not change with $c$. A genuine
**drag** effect grows with $v^{2}$, hence with depth and with $1/m$, and it
disappears if the air is pumped out. So the discriminator is a *parameter sweep*:
vary the depth and the probe's mass/cross-section and see whether the timing
residual scales as the predicted function of $v_{\text{drag}}$ or stays constant.
An experiment that quotes a single drop has not separated the two at all.

---

## ★★★10 — Differentiating a noisy series

**(a)** $\dot x \approx (x_{i+1}-x_i)/\Delta t$. With independent noises of
variance $\sigma^{2}$ each, the difference has variance $2\sigma^{2}$
(variances add for a difference of independent variables), so the derivative's
noise has standard deviation $\sqrt{2}\sigma/\Delta t$. It is *amplified* as
$\Delta t$ shrinks — which is the opposite of the behaviour of a time average.

**(b)**

| $\Delta t$ | noise in $\dot x$ |
|---|---|
| 1 day | $\sqrt{2}(0.01)/(86400)\times3.1557\times10^{7}\times10^{3} = \mathbf{5165\ mm\,yr^{-1}}$ |
| 30 days | $\mathbf{172.2\ mm\,yr^{-1}}$ |

**(c)** Compare with the fitted-slope uncertainty of ★★7: 1.81 mm/yr for a year of
daily data. The two-point difference with a 1-day baseline is worse by a factor
of $5165/1.81 = 2850$. The reason is structural: the least-squares slope uses the
*whole* time span (an effective lever arm of order the series length), while the
two-point difference uses only one interval. This is why geodetic velocities are
always fitted, never differenced.

**(d)** The two-point difference is the right tool when the signal is not
well modelled by a constant rate over the whole series — detecting an
**offset** (an equipment change or an earthquake), locating a transient, or
constructing a **high-frequency** measure such as a seismic or tilt rate where
the noise is not white and the bandwidth matters more than the precision. In
those cases the amplification is acceptable because the signal of interest
occupies the same band as the derivative.
