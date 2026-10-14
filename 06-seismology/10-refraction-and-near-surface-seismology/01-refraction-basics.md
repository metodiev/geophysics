---
id: 06-10-01
title: "Refraction Survey Geometry and Travel-Time Interpretation"
level: intermediate
prereqs: ["06-01-02", "06-02-02"]
tags: [seismology, near-surface, refraction, head-wave, travel-time, survey-design]
---

# Refraction Survey Geometry and Travel-Time Interpretation

> **All models and data in this module are SYNTHETIC.** The velocities, depths,
> spreads and picking errors used here are chosen teaching values. No field
> survey, site, borehole or catalogue is referred to, and no number is quoted
> from a published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the critical angle from Snell's law and show that a critically
   refracted ray carries the horizontal slowness $p = 1/v_2$ exactly.
2. **Derive** the head-wave travel-time equation
   $t(x) = x/v_2 + 2h\cos i_c/v_1$ from the ray geometry, and obtain the
   intercept time and crossover distance in closed form.
3. **Compute** the intercept time, the crossover distance and the first-arrival
   branch for a two-layer model, and **state** the units of every quantity.
4. **Explain** why the crossover must fall inside the spread for the refractor to
   be interpreted at all.
5. **Check** the closed form against an independent ray and wavefront
   computation, and **state** what each check does and does not validate.
6. **Demonstrate** that a two-layer interpretation of a three-layer
   first-arrival curve can be exact and wrong at the same time, and **quantify**
   the depth error (the blind zone).

## Prerequisites

- [06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation](../01-elastic-wave-propagation/02-p-and-s-waves.md) —
  the body waves whose speeds enter every formula here.
- [06-02-02 Snell's Law, Layered Media and the Travel-Time Curve](../02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  the ray parameter as a conserved quantity, and the travel-time curve.
- [03-10 ObsPy and Seismic Data](../../03-scientific-computing/10-obspy-and-seismic-data/README.md) —
  reading and picking arrival times, which is where every number below comes
  from in practice.

## 1. Intuition: a line of receivers and the first thing that arrives

Put a source on the ground and a line of receivers along the surface. At each
receiver, record the first motion that arrives and note its time. You now have a
function $t(x)$, the **travel-time curve** of the first arrivals, and the entire
method of this lesson is the attempt to read a layered structure out of its
slope.

Two things can arrive first at a horizontal offset $x$:

- the **direct wave**, travelling along the surface in the top layer at speed
  $v_1$: $t = x/v_1$;
- the **head wave** (also called the critically refracted wave, or simply the
  refraction): a wave that dives to an interface, runs along it at the speed of
  the layer below, and returns to the surface.

The head wave starts later than the direct wave — it has further to travel — but
its slope on a $t(x)$ plot is $1/v_2 < 1/v_1$, so its line is *steeper* in time
per metre only until it overtakes. Past the **crossover distance** the head wave
is the first arrival, and that transition is what the interpreter reads.

There is one thing the method can never see, and it is worth stating at the
outset because every later lesson in this module is a reaction to it. A
first-arrival time is a time, and the ray that produces it has avoided
everything that is slower than its own path. A **low-velocity layer** between two
faster ones slows every arrival down and yet never appears as a separate branch.
It is genuinely invisible to first arrivals, not merely hard to invert, and
Section 6 measures exactly what that costs.

## 2. Precise definitions

### 2.1 The critical angle

For two homogeneous layers in welded contact, Snell's law makes the horizontal
slowness

$$p = \frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}
\qquad (\mathrm{s\,m^{-1}})$$

the same on both sides of the interface. Setting $\theta_2 = 90^\circ$ gives the
**critical angle**

$$\sin i_c = \frac{v_1}{v_2}, \qquad
\cos i_c = \sqrt{1 - \frac{v_1^{2}}{v_2^{2}}}
= \frac{\sqrt{v_2^{2} - v_1^{2}}}{v_2}.$$

At and beyond this incidence angle no energy is transmitted into the lower
medium as a body wave; the transmitted wave becomes a disturbance that travels
along the interface, and it is that disturbance which radiates back into the
upper layer.

**The critical ray has $p = 1/v_2$ exactly.** The demonstration prints
$p = \sin i_c/v_1 = 5.55556\times10^{-4}\ \mathrm{s\,m^{-1}}$ and
$1/v_2 = 5.55556\times10^{-4}\ \mathrm{s\,m^{-1}}$ for
$v_1 = 500\ \mathrm{m\,s^{-1}}$, $v_2 = 1800\ \mathrm{m\,s^{-1}}$. This is the
slowest horizontal slowness the lower medium can carry: no ray in it can be more
horizontal.

### 2.2 Head-wave travel time

If the interface is at depth $h$ beneath a flat surface, the ray leaves the
source at the critical angle, travels along the interface, and returns to the
surface at the critical angle. Its travel time is

$$\boxed{\;t(x) = \frac{x}{v_2} + t_i, \qquad
t_i = \frac{2h\cos i_c}{v_1}
= \frac{2h\sqrt{v_2^{2}-v_1^{2}}}{v_1 v_2}.\;}$$

$t_i$ is the **intercept time**: the time at which the head-wave branch, extended
back to $x = 0$, would start. It is not the time of any physical arrival at the
source, and one of the commonest errors in hand interpretation is to treat it as
if it were.

### 2.3 Crossover distance

The direct and head branches cross where $x/v_1 = x/v_2 + t_i$, so

$$\boxed{\;x_c = \frac{t_i v_1 v_2}{v_2 - v_1}
= 2h\sqrt{\frac{v_2+v_1}{v_2-v_1}}.\;}$$

The second form follows from the first by substituting $t_i$, and it is worth
deriving once because it shows the whole design trade. A **weak contrast**
$v_2 \to v_1$ sends $x_c \to \infty$: the two branches become parallel lines, and
the offsets needed to separate them grow without bound. This is the subject of
Lesson 06's survey design, and the reason a refraction survey is expensive
precisely where the velocity change is small.

### 2.4 Apparent velocity

The slope of a branch on the $t(x)$ plot is the **apparent velocity**

$$v_{\text{app}} = \left(\frac{\mathrm{d}t}{\mathrm{d}x}\right)^{-1}
\qquad (\mathrm{m\,s^{-1}}),$$

which equals the true layer velocity only when the interface and the surface are
horizontal and the line is perpendicular to the structure. A dipping interface
gives one apparent velocity in the forward direction and a different one in the
reverse direction — which is why surveys are shot from both ends, and why
Lesson 02 exists.

## 3. Derivations

### 3.1 From the ray geometry to $t(x)$

Let the ray leave the source at angle $i_c$ from the vertical. Each of the two
diagonal legs has length $h/\cos i_c$ travelled at speed $v_1$, and its horizontal
projection is $h\tan i_c$. The horizontal length of the middle leg is therefore
$x - 2h\tan i_c$, travelled at speed $v_2$. Adding the three parts,

$$t(x) = \frac{2h}{v_1\cos i_c}
+ \frac{x - 2h\tan i_c}{v_2}.$$

Now collect the constant terms and use $\sin i_c = v_1/v_2$:

$$\frac{2h}{v_1\cos i_c} - \frac{2h\tan i_c}{v_2}
= \frac{2h}{v_1\cos i_c}\left(1 - \sin^{2} i_c\right)
= \frac{2h\cos^{2} i_c}{v_1\cos i_c}
= \frac{2h\cos i_c}{v_1},$$

which is $t_i$. The identity $\sin i_c = v_1/v_2$ is what collapses the two
constant terms into one, and it is the only non-obvious step.

*Numerical check (SYNTHETIC).* $v_1 = 500\ \mathrm{m\,s^{-1}}$,
$v_2 = 1800\ \mathrm{m\,s^{-1}}$, $h = 10\ \mathrm{m}$:
$\cos i_c = 0.960645062$ and $\tan i_c = 0.289157367$, so
$2h/(v_1\cos i_c) = 41.63867\ \mathrm{ms}$ and
$2h\tan i_c/v_2 = 3.21286\ \mathrm{ms}$; their difference is
$38.42581\ \mathrm{ms}$. The demonstration prints
$t_i = 38.425814\ \mathrm{ms}$ from both algebraic routes — the delay-time form and
$2h\sqrt{v_2^{2}-v_1^{2}}/(v_1 v_2)$ — which is the same number.

### 3.2 Crossover, three ways

With $t_i = 38.425814\ \mathrm{ms}$,

$$x_c = \frac{t_i v_1 v_2}{v_2-v_1}
= \frac{0.038425814 \times 500 \times 1800}{1300}
= 26.6025\ \mathrm{m},$$

and the closed form gives
$2h\sqrt{(v_2+v_1)/(v_2-v_1)} = 20\sqrt{2300/1300} = 26.6025\ \mathrm{m}$. The
demonstration reports that these two are equal to $1.34\times10^{-16}$ in
relative terms, and that a numerical root find on a $0.1\ \mathrm{mm}$ grid
locates the crossing at $26.602400\ \mathrm{m}$, a relative difference of
$3.27\times10^{-6}$ — the grid resolution, not a discrepancy.

### 3.3 The travel-time curve

| $x$ (m) | $t_{\text{direct}}$ (ms) | $t_{\text{head}}$ (ms) | first arrival |
|---|---|---|---|
| 5 | 10.0000 | 41.2036 | direct |
| 10 | 20.0000 | 43.9814 | direct |
| 20 | 40.0000 | 49.5369 | direct |
| 26.6 | 53.2000 | 53.2036 | direct |
| 40 | 80.0000 | 60.6480 | head |
| 60 | 120.0000 | 71.7591 | head |
| 100 | 200.0000 | 93.9814 | head |
| 150 | 300.0000 | 121.7591 | head |

Note the structure of the numbers. The direct branch has slope
$1/v_1 = 2\ \mathrm{ms\,m^{-1}}$; the head branch has slope
$1/v_2 = 0.5556\ \mathrm{ms\,m^{-1}}$; the head branch starts $38.4\ \mathrm{ms}$
late and never catches up until $26.6\ \mathrm{m}$. Inverting the pair of slopes
gives $v_1$ and $v_2$; inverting the intercept gives $h$ **given $v_1$ and
$v_2$**. There is no third equation, and that is the whole information content of
a two-layer refraction line.

## 4. Survey geometry

The standard in-line refraction spread has one shot at each end of a line of
receivers. The two shots give the **forward** and **reverse** travel-time curves,
whose difference is what allows a dipping interface to be separated from a
horizontal one. The quantities an interpreter needs are:

| Quantity | Symbol | Meaning |
|---|---|---|
| spread length | $L$ | source-to-farthest-receiver distance |
| offset | $x$ | source-to-receiver distance |
| near / far offset | $x_{\min}, x_{\max}$ | the sampled range |
| receiver spacing | $\Delta x$ | sets the shortest resolvable structure |
| forward / reverse branch | $t_f(x), t_r(x)$ | shot at either end |

Design rules that follow directly from Section 3:

1. **The crossover must lie inside the spread**, ideally with the far offset at
   three times $x_c$, so that the far branch has a well-determined slope. If
   $x_{\max} < x_c$ the refractor is not seen at all: the record shows one line
   with slope $1/v_1$ and nothing else is recoverable.
2. **The near offsets must sample the direct branch.** Without picks on
   $x/v_1$ there is no independent measurement of $v_1$, and Section 6 shows that
   $v_1$ is the parameter the depth is most sensitive to.
3. **The receiver spacing sets the shortest interface feature** that can appear
   in the interpretation, since every depth estimate belongs to one receiver
   position.
4. **The source must be strong enough to give a first-motion pick** at the far
   offset; the amplitude of the head wave decays with offset faster than that of
   the direct wave.

## 5. Verification: is the closed form right?

A closed form can be verified in two independent ways, and the demonstration
does both.

**Ray minimisation (Fermat).** The head-wave time is computed by numerically
minimising the travel-time functional over the two knee points of the ray,
without ever using the closed form. The worst relative difference over five
offsets from 30 to 160 m is $4.354\times10^{-14}$ — floating-point stopping
tolerance. This validates the algebra of Section 3.1.

**Discretised eikonal (shortest-path) solver.** A grid-based wavefront solver is
given the velocity stack and the source, and returns first-arrival times with no
assumption about rays at all. Its refinement parameter is the *number of
directions* in which a path may continue:

| directions | max $|\Delta t|$ (ms) | max relative difference |
|---|---|---|
| 16 | 0.7400 | $1.220\times10^{-2}$ |
| 32 | 0.1048 | $1.727\times10^{-3}$ |
| 48 | 0.0275 | $4.528\times10^{-4}$ |
| 96 | 0.0275 | $4.528\times10^{-4}$ |
| 144 | 0.0104 | $1.715\times10^{-4}$ |
| 176 | 0.0104 | $1.715\times10^{-4}$ |

The residual is **angular quantisation**, not grid spacing: a ray at
$73.87^\circ$ from the horizontal must be built from the available
$71.57^\circ$ and $75.96^\circ$ steps, and the error falls by roughly a factor of
three per refinement step. The plateau between 48 and 96 directions is the same
two neighbouring directions bounding the ray until a better pair becomes
available. A shortest-path solver must therefore be refined in *directions*, and
reporting a residual without saying which parameter was refined reports nothing.

What the second check does and does not prove matters. It validates the closed
form against a method that does not share its assumptions about the ray family.
It does not validate the choice of a layered model, and it says nothing about
whether the first arrival at a given offset is a head wave or a direct wave —
that is decided by the model, in both computations.

## 6. The blind zone: a two-layer answer that is exact and wrong

Take the SYNTHETIC three-layer model:

| layer | velocity (m/s) | thickness (m) |
|---|---|---|
| 1 | 500 | 8.0 |
| 2 | **250** | 8.0 |
| 3 | 1800 | half-space |

The exact first-arrival time is the delay-time sum of the two overlying layers,

$$t(x) = \frac{x}{v_3} + \left[\frac{h_1\cos\theta_1}{v_1}
+ \frac{h_2\cos\theta_2}{v_2}\right],$$

with $\theta_1 = \arcsin(v_1/v_3) = 16.1276^\circ$ and
$\theta_2 = \arcsin(v_2/v_3) = 7.9836^\circ$. The bracket is
$15.370326\ \mathrm{ms} + 31.689855\ \mathrm{ms} = 94.120362\ \mathrm{ms}$.

Now interpret that curve as if it were two layers. The fitted model is
$500\ \mathrm{m\,s^{-1}}$ over $1800\ \mathrm{m\,s^{-1}}$ with

$$h = \frac{t_i v_1 v_3}{2\sqrt{v_3^{2}-v_1^{2}}}
= \frac{0.094120362 \times 500 \times 1800}{2\sqrt{1800^{2}-500^{2}}}
= 24.494045\ \mathrm{m},$$

against a true depth of $16.0\ \mathrm{m}$ to the top of the $1800\
\mathrm{m\,s^{-1}}$ layer: an error of $+8.494\ \mathrm{m}$, or $+53.1\%$.

The reason this is not merely a bad inversion is the residual. Fitting the
two-layer model to the true first arrivals over offsets of 20–200 m (91 traces)
leaves a maximum residual of $0.000\ \mathrm{s}$ and an RMS of $0.000\ \mathrm{s}$:
**the observed curve is a two-layer curve to numerical precision**. There is no
residual of any size to reveal the $250\ \mathrm{m\,s^{-1}}$ layer, because no
first-arrival ray spends any time in it. The independent eikonal check reproduces
the same travel times to $0.01514\ \mathrm{ms}$ at worst, so the forward
computation is not in question.

Two consequences, both quantitative:

- **The blind layer is blind, not noisy.** More receivers, better picks or a
  better inversion cannot recover it. The information is absent.
- **There is a blind *window*, not just a blind layer.** With a 100 m spread the
  basal $1800\ \mathrm{m\,s^{-1}}$ refractor stays visible only while the blind
  layer is thinner than $14.352\ \mathrm{m}$. Thicker than that, the refractor
  also disappears, and the record shows a single line at $500\ \mathrm{m\,s^{-1}}$
  — two layers lost to one.

The remedy is never a better refraction interpretation. It is a different
measurement: a borehole that physically enters the layer, or a surface-wave
sounding that senses the low-velocity material directly (Lesson 04).

## 7. Worked example

**Problem.** A two-layer model has $v_1 = 500\ \mathrm{m\,s^{-1}}$,
$v_2 = 1800\ \mathrm{m\,s^{-1}}$, $h = 10\ \mathrm{m}$. A 120 m spread with 2 m
receiver spacing is shot from both ends. (a) Compute $i_c$, $t_i$ and $x_c$.
(b) Predict the first-arrival time at $x = 60\ \mathrm{m}$. (c) State which
picks constrain the depth, and which constrain the velocities.

**(a)** $\sin i_c = 500/1800 = 0.277778$, so $i_c = 16.1276^\circ = 0.281480\
\mathrm{rad}$ and $\cos i_c = 0.960645$.

$$t_i = \frac{2 \times 10 \times 0.960645}{500} = 0.0384258\ \mathrm{s}
= 38.4258\ \mathrm{ms},$$
$$x_c = 2 \times 10\sqrt{\frac{1800+500}{1800-500}} = 26.6025\ \mathrm{m}.$$

**(b)** At $x = 60\ \mathrm{m} > x_c$ the head wave arrives first:
$t = 60/1800 + 0.0384258 = 0.0333333 + 0.0384258 = 0.0717591\ \mathrm{s}
= 71.7591\ \mathrm{ms}$, matching the demonstration's table. The direct wave
would have arrived at $120\ \mathrm{ms}$, an order-of-magnitude difference in
first-motion time that is why refraction is a workhorse method.

**(c)** The two *slopes* give $v_1$ and $v_2$; they say nothing about depth. The
*intercept* gives $h$ and it does so only because $v_1$ and $v_2$ are already
assumed. In the demonstration's flat-model round trip, feeding exact travel
times back through the inversion returns $v_1 = 500.000000\
\mathrm{m\,s^{-1}}$, $v_2 = 1800.000000\ \mathrm{m\,s^{-1}}$ and
$h = 10.000000\ \mathrm{m}$ with relative errors of $2.27\times10^{-16}$,
$3.79\times10^{-16}$ and $1.07\times10^{-15}$. With exact times the round trip
closes to floating point; **all of the difficulty in Lesson 02 comes from the
picking error that this experiment has set to zero.**

## 8. Assumptions and regime of validity

1. **Two homogeneous isotropic layers in welded contact.** Lateral velocity
   change within a layer, or a gradational interface, breaks the interpretation;
   Section 6 shows what an unrecognised third layer does, and Lesson 02
   quantifies a lateral change.
2. **Plane interfaces and a flat free surface.** Dip makes the forward and
   reverse apparent velocities unequal (a diagnostic, not a nuisance); topography
   must be recorded and used, because a refraction time maps to a depth *below the
   receiver*, not below a datum.
3. **Velocity increasing with depth.** Otherwise no head wave exists from the
   deeper interface at all: **the method cannot detect a slow layer beneath a
   fast one**, and it cannot detect one between two fast ones either (Section 6).
4. **Each layer thick enough to produce a distinct branch.** A layer thinner than
   roughly a quarter of the dominant wavelength does not appear as a separate
   break in slope (Lesson 06 quantifies this with numbers).
5. **The first arrival is the head wave**, not a guided wave in a thin layer, a
   diffracted arrival, or an air wave. At very short offsets an air wave
   ($\approx 340\ \mathrm{m\,s^{-1}}$) can arrive first and be mistaken for
   ground motion; it is identified by its compressional polarisation and its
   speed, which is a standard constant of the atmosphere.
6. **Sources and receivers on the same line and offsets known to centimetres.**
   The depth error is linear in an offset error, so a survey with sloppy
   geometry has a depth bias that no processing removes.
7. **Picking error is the dominant random error**; it is quantified in Lesson 02
   and is the reason the demonstration's round trip closes but a real one does
   not.

## Mastery checkpoint

Do this without notes, using $v_1 = 600\ \mathrm{m\,s^{-1}}$,
$v_2 = 2400\ \mathrm{m\,s^{-1}}$, $h = 12\ \mathrm{m}$ (SYNTHETIC values).

**(a)** Compute $\sin i_c$, $\cos i_c$, the intercept time and the crossover
distance, with units.
**(b)** Predict the first-arrival time at $x = 50\ \mathrm{m}$ and state which
branch it is.
**(c)** A survey of total length $L$ has its farthest offset at $L$. What is the
minimum $L$ that puts a crossover at one third of the spread for this model, and
what is the deepest interface such a spread could see if the contrast were only
$1.2$?
**(d)** A colleague reports that the residual of their two-layer fit is
$0.000\ \mathrm{s}$ and concludes that the site has exactly two layers. Give the
one-sentence rebuttal, with a number from Section 6.
**(e)** Explain why a head wave cannot exist for $p > 1/v_2$.

A worked version appears in the
[solutions](exercises/01-refraction-basics-solutions.md).

## Common pitfalls

1. **Reading the intercept time as an arrival time.** $t_i$ is an extrapolation
   to $x = 0$; no wave arrives at the source at that time.
2. **Quoting a depth without its velocity assumption.** The depth is derived from
   the intercept *given* $v_1$ and $v_2$; change $v_1$ by $20\%$ and the depth
   changes by roughly the same amount (Lesson 02 measures this sensitivity as
   $1.067$ in logarithmic terms).
3. **Using apparent velocities as layer velocities.** Only with a horizontal
   interface and a perpendicular line do they coincide; dip makes them differ in
   a way that depends on the shooting direction.
4. **Mixing $\mathrm{s\,m^{-1}}$ and $\mathrm{s\,km^{-1}}$.** In near-surface work
   the ray parameter is of order $10^{-4}$–$10^{-3}\ \mathrm{s\,m^{-1}}$; in
   crustal work it is quoted in $\mathrm{s\,km^{-1}}$. A unit slip changes $p$ by
   a factor of $10^{3}$.
5. **Believing a zero residual.** A three-layer model with a low-velocity middle
   layer is fitted exactly by a two-layer model (Section 6), so a perfect fit is
   not evidence that the model is right.
6. **Forgetting the air wave.** It is fast enough to be the first arrival at short
   offsets in many field settings and is not a ground arrival at all.
7. **Designing a spread that stops before the crossover.** Nothing below the
   deepest crossing branch is recovered, and no amount of inversion recovers it.

## Related modules

- [02 Delay-Time (Plus-Minus) Methods and Depth Estimation](02-plus-minus-method.md) —
  the same two-layer equations rewritten so that depth is computed receiver by
  receiver, with the error propagation that makes them useful.
- [03 Refraction Tomography and First-Arrival Inversion](03-tomography-refraction.md) —
  what to do when the two-layer assumption is not good enough, and what remains
  impossible.
- [06-01-06 Interface Waves, Head Waves and the Total Wavefield](../01-elastic-wave-propagation/06-interface-waves.md) —
  why the head wave exists at all, and how it differs from a Stoneley or
  Scholte interface wave.
- [06-02-03 The tau-p Transform and Intercept Time](../02-ray-theory-and-travel-times/03-tau-p.md) —
  the intercept time as a slowness-domain observable, which is the systematic
  version of Section 2.2.
- [10-04-03 Near-Surface Refraction for Static Corrections](../../10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/03-refraction-static.md) —
  the same interpretation used to build the statics of a reflection survey.

## Code and exercises

The demonstration for this lesson is
[`code/refraction_basics_demo.py`](code/refraction_basics_demo.py):

```bash
cd 06-seismology/10-refraction-and-near-surface-seismology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python refraction_basics_demo.py
```

It prints every number quoted in this lesson, with units, and exits 0.

Graded exercises are in
[`exercises/01-refraction-basics-exercises.md`](exercises/01-refraction-basics-exercises.md)
with worked solutions in
[`exercises/01-refraction-basics-solutions.md`](exercises/01-refraction-basics-solutions.md).
Module overview and the full lesson map: [`README.md`](README.md).
