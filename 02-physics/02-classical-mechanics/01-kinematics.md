---
id: 02-02-01
title: "Kinematics in One and Two Dimensions"
level: beginner
prereqs: ["02-01-01", "02-01-02"]
estimated_minutes: 90
tags: [kinematics, projectile-motion, drag, velocity, gnss]
---

# Kinematics in One and Two Dimensions

## Learning objectives

By the end of this lesson you will be able to:

1. **Differentiate** position to obtain velocity and acceleration, and integrate
   back, stating the initial conditions you used.
2. **Derive** the constant-acceleration relations and the vacuum projectile
   results (range, apex, flight time) from those integrals, without quoting
   them.
3. **Explain** why the horizontal and vertical motions of a projectile are
   independent, and what that independence requires of the force law.
4. **Estimate** the regime of validity of each kinematic result you use:
   flat-Earth, constant-$g$, no-drag — with a computed error at a stated
   distance or speed.
5. **Fit** a velocity from a noisy position series, and state the uncertainty of
   the fitted rate.

## Prerequisites

- [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](../01-measurement-and-physical-reasoning/01-physical-quantities.md) —
  the units of velocity and acceleration, and the conversion between km/s and
  mm/yr.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](../01-measurement-and-physical-reasoning/02-measurement-uncertainty.md) —
  needed for §3.6, where a velocity is fitted to noisy positions.

## 1. Intuition: kinematics is description without explanation

Kinematics answers "where, how fast, and in which direction" without asking
*why*. That is not a weakness; it is the division of labour that makes both
halves of mechanics tractable. In geophysics the kinematic vocabulary is
everywhere:

| Statement | The kinematic content |
|---|---|
| "the Pacific plate moves northwest at 7 cm/yr" | a velocity vector, measured from GNSS or magnetic isochrons |
| "the P wave arrived 12 s after the origin time" | an average speed over a known path |
| "the station subsided 3 mm/yr" | a fitted rate from noisy position series |
| "the rockfall reached 30 m/s before impact" | an instantaneous speed, inferred from energy |
| "the Moon recedes at 2 cm/yr" | a measured rate, from lunar laser ranging |

Notice that the first, third and fifth of these are *rates fitted to data*: the
physics enters only through what the fit is allowed to assume. Kinematics is
therefore also where the most common quantitative mistakes in geophysics live —
using an average speed as if it were instantaneous, quoting a rate without its
uncertainty, or fitting a straight line to a curve.

## 2. Precise definitions

### 2.1 Position, displacement, velocity, acceleration

Take a fixed reference frame with origin $O$. The **position** of a particle is
$\mathbf{r}(t)$; the **displacement** over an interval is
$\Delta\mathbf{r} = \mathbf{r}(t_2) - \mathbf{r}(t_1)$.

**Average velocity** is displacement over elapsed time,
$\bar{\mathbf{v}} = \Delta\mathbf{r}/\Delta t$; **instantaneous velocity** is the
derivative

$$\mathbf{v}(t) = \frac{d\mathbf{r}}{dt}
= \lim_{\Delta t\to0}\frac{\Delta\mathbf{r}}{\Delta t},$$

and **acceleration** is $\mathbf{a} = d\mathbf{v}/dt = d^{2}\mathbf{r}/dt^{2}$.

Three distinctions that matter in practice:

1. **Speed is not velocity.** Speed is $|\mathbf{v}|$, a non-negative scalar. A
   velocity always carries a direction, and in geophysics that direction is
   usually the point of the measurement (a plate motion is not characterised by
   7 cm/yr alone).
2. **Average is not instantaneous.** An average over 10 Ma of plate motion
   smooths over earthquakes; an instantaneous GNSS rate includes the
   post-seismic transient of the last event.
3. **A reference frame must be named.** "The station rose 2 mm/yr" is
   incomplete without the frame: is the frame the geocentre, the regional
   network average, or a nearby bedrock benchmark?

### 2.2 The choice of coordinates, and why 1-D is not a toy

Almost every useful geophysical kinematic problem reduces to one dimension by
choosing the axis along the motion (a borehole drop, a ray along a straight
path, a plate motion projected onto its direction of travel). The 1-D relations
below therefore carry most of the load; the 2-D case enters for projectiles,
where the horizontal and vertical components decouple.

## 3. Step-by-step derivations

### 3.1 Constant acceleration, by integration

Let $\mathbf{a}$ be constant. Then

$$\mathbf{v}(t) = \mathbf{v}_0 + \int_0^t \mathbf{a}\,dt'
= \mathbf{v}_0 + \mathbf{a}t,$$

$$\mathbf{r}(t) = \mathbf{r}_0 + \int_0^t \mathbf{v}(t')\,dt'
= \mathbf{r}_0 + \mathbf{v}_0t + \tfrac12\mathbf{a}t^{2}.$$

These two are the definitions integrated once and twice, and they are valid
**only for constant** $\mathbf{a}$. Eliminating $t$ between them gives the
third relation,

$$v^{2} = v_0^{2} + 2\,\mathbf{a}\cdot\Delta\mathbf{r},$$

which is useful when time is not observed — exactly the case in seismology,
where arrival times give distances rather than elapsed times.

### 3.2 The vacuum projectile

Choose $x$ horizontal and $z$ vertical, so $\mathbf{a} = (0,-g)$ with $g$
constant. Then the components are independent:

$$x(t) = x_0 + v_{x0}t, \qquad z(t) = z_0 + v_{z0}t - \tfrac12gt^{2}.$$

For launch and landing at the same height $z_0$, the flight time is found from
$z(t) = z_0$:

$$t_{\text{flight}} = \frac{2v_{z0}}{g},$$

the apex is at $t_{\text{apex}} = v_{z0}/g$, and the range is

$$R = v_{x0}t_{\text{flight}} = \frac{2v_0^{2}\sin\theta\cos\theta}{g}
= \frac{v_0^{2}\sin 2\theta}{g},$$

maximised at $\theta = 45°$. Checking with the lesson's demonstration for
$v_0 = 20\ \mathrm{m\,s^{-1}}$, $\theta = 35°$ and
$g = 9.82025\ \mathrm{m\,s^{-2}}$:

$$R = \frac{(20)^{2}\sin 70°}{9.82025} = 38.2757\ \mathrm{m},$$

matching the integrated value to all printed digits, and the apex height is

$$h_{\text{apex}} = \frac{v_{z0}^{2}}{2g}
= \frac{(20\sin35°)^{2}}{2\times9.82025} = 6.7002\ \mathrm{m}.$$

### 3.3 Why the components are independent — and when they are not

The decoupling in §3.2 is not a property of projectiles; it is a property of
**separable forces**. Newton's second law in components is

$$m\ddot{x} = F_x, \qquad m\ddot{z} = F_z,$$

and these are independent equations *only if* $F_x$ does not depend on $z$ or
$\dot z$ (and vice versa). Gravity near the surface depends on neither, so the
motion separates, and Galileo's observation follows: **the time to fall is
independent of the horizontal speed**.

Air resistance breaks the independence, because the drag magnitude depends on
the *total* speed $\sqrt{v_x^{2}+v_z^{2}}$. That is why the demonstration's drag
runs must be integrated rather than solved component-wise. It is worth noting
that the *sign* of the effect is predictable without integrating: drag removes
range monotonically, and the demonstration measures it — 94.1%, 86.6% and 76.8%
of the vacuum range for drag coefficients 0.002, 0.005 and 0.010 m⁻¹.

### 3.4 Linear drag, in closed form

For a body falling under gravity with a drag force proportional to velocity
(Stokes regime), $m\dot v = -mg - bv$, i.e. $\dot v = -g - kv$ with $k = b/m$.
This is linear and separates:

$$\int_0^{v}\frac{dv'}{g+kv'} = -\int_0^{t}dt'
\;\Longrightarrow\;
v(t) = -\frac{g}{k}\left(1-e^{-kt}\right),$$

so the **terminal velocity** is $v_t = g/k$ and the approach is exponential with
time constant $\tau = 1/k$. In the demonstration, $k = 0.2\ \mathrm{s^{-1}}$
gives $v_t = 49.1013\ \mathrm{m\,s^{-1}}$, and after 20 s of fall the exact and
integrated values agree to all six printed digits
($-48.201932\ \mathrm{m\,s^{-1}}$, i.e. 98.17% of terminal).

**This is the first place in the folder where an approximation reveals itself
through its error.** Terminal velocity exists because drag grows with speed; a
"constant acceleration" model has no terminal velocity at all, and using it for
a body falling for many time constants is simply the wrong model — not an
inaccurate version of the right one.

### 3.5 Quadratic drag: no closed form, so integrate and measure

For high Reynolds numbers the drag is quadratic: $\dot{\mathbf{v}} =
\mathbf{g} - c\,|\mathbf{v}|\,\mathbf{v}$, with $c = \rho C_dA/(2m)$. There is no
elementary closed-form solution for the trajectory, so the demonstration
integrates it. For a 400 m borehole drop with $c = 0.002\ \mathrm{m^{-1}}$ the
fall takes 10.2635 s against the vacuum 9.0258 s: a **+1.24 s** difference, i.e.
13.7% longer.

The practical reading: in a drop-calibration test the vacuum time is a *lower
bound* on the elapsed time, and the difference is a measurement of the drag
coefficient, not an error to be ignored.

### 3.6 Estimating a velocity from noisy positions

Suppose a station position is measured $n$ times at times $t_i = i\Delta t$, each
with independent white noise of standard deviation $\sigma$, and you fit a
straight line $x(t) = a + vt$. The least-squares slope has variance

$$\sigma_v^{2} = \frac{\sigma^{2}}{\sum_i(t_i-\bar{t})^{2}}
= \frac{12\sigma^{2}}{n(n^{2}-1)\Delta t^{2}}.$$

Evaluating with $\sigma = 1$ cm (a daily GNSS position, SYNTHETIC) and
$\Delta t = 1$ day:

| Span | $n$ | $\sigma_v$ |
|---|---|---|
| 1 month | 30 | 77.0 mm/yr |
| 6 months | 180 | 5.24 mm/yr |
| 1 year | 365 | 1.81 mm/yr |
| 3 years | 1095 | 0.35 mm/yr |

The lesson is a scaling law in plain sight: the rate uncertainty falls roughly
as $n^{-3/2}$, i.e. as $(\text{span})^{-3/2}$. This single line explains why
geodetic velocity fields require multi-year series, why campaign-mode GPS with
three occupations is nearly useless for velocities, and why a 1 mm/yr tectonic
signal needs years of daily data. Note also that the assumption of *white* noise
is what makes the formula this simple; real GNSS position series contain
common-mode and coloured noise, which inflate the rate uncertainty
([02-01-02](../01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)).

## 4. Physical interpretation

### 4.1 What the kinematic quantities mean physically

- **Velocity** is a vector; in a rock it is a *material* property at the scale of
  the wave (seismic velocity), while for a station it is a *motion* of the
  ground. The same word, different referents — always check which.
- **Acceleration** is what a gravimeter measures, and it is the quantity in
  Newton's second law. Displacement is what GNSS measures; velocity and
  acceleration are *derived* from it by differentiation, which amplifies noise
  as frequency increases (differentiating a position twice multiplies white
  noise by $\omega$ and $\omega^{2}$ respectively). This is why strong-motion
  accelerometers measure acceleration directly, and why integrating
  accelerograms to displacement accumulates drift.
- **Averaging time matters.** A plate velocity averaged over 10 Ma and a GNSS
  velocity over 5 yr can differ by the elastic strain accumulation, which is
  precisely the signal earthquake-cycle studies want.

### 4.2 Sign conventions

Two conventions coexist and both must be stated:

| Convention | Positive vertical | Used by |
|---|---|---|
| depth-positive | downward | seismology, borehole data |
| height-positive | upward | geodesy, GNSS, surveying |

A "2 mm/yr uplift" in a geodetic paper and a "2 mm/yr in the depth coordinate"
in a seismological one are the *same* physical motion of the ground. Getting the
sign wrong is a factor of −1 error that no dimensional check can catch.

## 5. Assumptions and regime of validity

Each result of §3 carries its own regime, and each can be quantified:

1. **Constant $g$**: valid while the height change is small compared with the
   Earth's radius. From [02-01-01](../01-measurement-and-physical-reasoning/01-physical-quantities.md),
   the vertical gradient at the surface is $2GM/R^{3} = 3.08\times10^{-6}\ \mathrm{s^{-2}}$,
   so over 1 km the change in $g$ is $3.1\times10^{-3}\ \mathrm{m\,s^{-2}}$,
   i.e. 0.03%.
2. **Flat Earth**: approximating the surface as a plane. For a horizontal range
   $x$ the surface curves away by $x^{2}/(2R)$: 7.8 m at 10 km, **785 m at
   100 km**, and $7.8\times10^{4}$ m at 1000 km. The corresponding reduction in
   $g$ at the landing point is 0.025% at 100 km. So the flat-Earth projectile
   formula is good to a part in $10^{3}$ at 100 km and must not be used for
   intercontinental ballistic contexts — or for anything that leaves the
   troposphere.
3. **No drag**: valid only when the drag force is small against gravity. Compare
   $c v^{2}$ with $g$: with the demonstration's $c = 0.002\ \mathrm{m^{-1}}$ the
   two are equal at $v = \sqrt{g/c} = 70\ \mathrm{m\,s^{-1}}$. **State it as a
   speed, not as a hand-wave.**
4. **Point particle**: no rotation, no deformation, no spin. A spinning ball
   acquires a Magnus force, and a long falling object has a different drag.
5. **Non-relativistic**: $v/c = 1.7\times10^{-5}$ for a 5 km/s P wave, so
   relativistic kinematics are irrelevant for seismic wave *speeds*; they are
   not irrelevant for GNSS clock and orbit modelling.
6. **Instantaneous position vs material point**: for a deforming body the
   material velocity is $\mathbf{v}(\mathbf{x}(t),t)$, not
   $\partial_t\mathbf{x}$ with $\mathbf{x}$ fixed — the distinction between
   material and partial derivatives, which returns in
   [02-04-02](../04-elasticity-and-continuum-mechanics/02-strain.md).

## 6. Units and dimensional analysis

Kinematic quantities in geophysics are expressed in an unusually wide range of
units, and all of them are decimal powers of SI:

| Quantity | Unit | In SI |
|---|---|---|
| ground motion velocity | mm/yr | $3.17\times10^{-11}\ \mathrm{m\,s^{-1}}$ |
| seismic wave speed | km/s | $10^{3}\ \mathrm{m\,s^{-1}}$ |
| borehole flow | m/d | $1.16\times10^{-5}\ \mathrm{m\,s^{-1}}$ |
| acceleration (gravity) | mGal | $10^{-5}\ \mathrm{m\,s^{-2}}$ |

The conversion $1\ \mathrm{mm\,yr^{-1}} = 3.1688\times10^{-11}\ \mathrm{m\,s^{-1}}$
is worth memorising, because it converts every geodetic rate into SI in one
step. Dimensionally, all kinematic relations must satisfy $[v] = LT^{-1}$ and
$a = LT^{-2}$: check that $v^{2} = 2gh$ has $L^{2}T^{-2}$ on both sides, and
that $\sqrt{2h/g}$ has $T$, before trusting either.

## 7. Python demonstration

The script integrates projectile motion and measures (a) the equality of fall
times for dropped and thrown bodies, (b) the convergence order of two
integrators and the way a *measurement* can hide it, (c) linear drag against its
closed form, (d) quadratic drag's range reduction, and (e) a 400 m borehole
drop.

Full listing: [`code/kinematics_demo.py`](./code/kinematics_demo.py).

Two excerpts. The integrator, which lands exactly on the requested final time so
that the comparison is not contaminated by a fractional last step:

```python
def rk4(vx0, vy0, dt, t_end, drag=None):
    """Classical fourth-order Runge-Kutta on the same state, same landing."""
    n = max(1, round(t_end / dt))
    h = t_end / n
    state = [0.0, 0.0, vx0, vy0]                    # x, y, vx, vy
```

and the drag term, which is what breaks the horizontal/vertical independence:

```python
        def drag(v, c=c):
            speed = math.hypot(*v)
            return (-c * speed * v[0], -c * speed * v[1])
```

Observed output (Python 3.14.4, standard library only):

```text

========================================================================
1. Free fall and a horizontal projection: the same fall time
========================================================================
  g at R = 6371 km              : 9.820250 m/s^2
  fall from 100 m             : t = 4.512879 s, impact speed = 44.3176 m/s
  dropped      : y = -100.000000 m, horizontal distance =   0.0000 m, vy = -44.3176 m/s
  thrown at 5 m/s: y = -100.000000 m, horizontal distance =  22.5644 m, vy = -44.3176 m/s
  thrown at 20 m/s: y = -100.000000 m, horizontal distance =  90.2576 m, vy = -44.3176 m/s
  analytic horizontal distance for 20 m/s = 90.2576 m

========================================================================
2. Vacuum projectile: range, apex, and integrator order
========================================================================
  v0 = 20.0 m/s at 35.0 deg
  range (exact)  = 38.275709 m, apex time = 1.168150 s, apex height = 6.700235 m
  range integrated until the trajectory lands, relative error:
      dt      Euler     ratio       RK4       ratio
   0.100  4.240e-02      ---  4.187e-04      ---
   0.010  4.276e-03     9.92  4.275e-06    97.95
   0.001  4.280e-04     9.99  3.851e-08   111.00
  Euler falls by ~10 per decade -> first order, as expected.
  RK4 falls by ~100, i.e. second order, NOT fourth: the limiting
  error is the linear interpolation of the landing time, not the
  integrator.  Measure the integrator separately, at a fixed time:
      dt      Euler error   ratio     RK4 error      ratio   (height at t = 1.0 s, exact 6.561403483 m)
   0.1000  4.910e-01      ---  2.665e-15     ---
   0.0100  4.910e-02    10.00  2.220e-14    0.12
   0.0010  4.910e-03    10.00  5.240e-14    0.42
   0.0001  4.910e-04    10.00  1.424e-12    0.04
  Euler is cleanly first order.  RK4 sits at round-off (~1e-14) and
  gets *worse* as dt shrinks, because it is exact for polynomials of
  degree <= 4 and the whole trajectory here is quadratic: what is
  left is floating-point noise, which grows with the step count.
  To see RK4's fourth order, use a problem with no polynomial
  solution -- quadratic drag, compared against a fine reference:
      dt      Euler error   ratio     RK4 error      ratio
   0.1000  2.073e-01      ---  1.383e-07     ---
   0.0100  2.045e-02    10.14  1.392e-11 9937.23
   0.0010  2.042e-03    10.01  1.332e-13  104.51
  (Reference = RK4 at dt = 1e-5.)  Now the orders appear: ~10 per
  decade for Euler (first order) and ~10^4 for RK4 (fourth order),
  until the RK4 residual itself reaches its round-off floor near
  1e-12 for velocities of order 10 m/s and flattens.  A measured
  convergence order is a property of the whole pipeline: a
  low-order component (the landing interpolation) or an exactly
  integrable test problem can each hide the true order.

========================================================================
3. Linear drag: exact solution versus integration
========================================================================
  linear drag a = -g - k v, k = 0.2 1/s
  terminal velocity = g/k = 49.1013 m/s
  after 20 s of fall: RK4 vy = -48.201932 m/s, exact = -48.201932 m/s
  (the body was launched from rest, so this is a vertical drop)
  fraction of terminal speed reached in 20 s = 0.981684

========================================================================
4. Quadratic drag: range reduction, measured
========================================================================
  vacuum range at 45 deg = 40.732159 m
  c = 0.0020 m^-1: range =   38.320 m (94.08% of the vacuum value)
  c = 0.0050 m^-1: range =   35.275 m (86.60% of the vacuum value)
  c = 0.0100 m^-1: range =   31.299 m (76.84% of the vacuum value)

========================================================================
5. A borehole drop: how long to fall 400 m?
========================================================================
  vacuum free fall from rest: t = 9.0258 s
  with quadratic drag c = 0.002 m^-1: t = 10.2635 s (difference +1.2377 s)
  The sign and size of the difference is what a calibration drop
  test measures; the vacuum time is an upper bound on the speed and
  a lower bound on the time.
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| dropped, 5 m/s and 20 m/s all reach $y = -100.000000$ m in the same time, with $v_y = -44.3176$ m/s | horizontal and vertical motion decouple exactly in vacuum |
| Euler's landing-range error falls ~10 per decade, RK4's ~100 | first and second order: the *second* order is the interpolation of the landing time, not the integrator |
| at a fixed time, RK4 sits at 1e-14 while Euler is cleanly first order | the trajectory here is a quadratic polynomial, which RK4 integrates exactly |
| quadratic drag: 94.1%, 86.6%, 76.8% of vacuum range for $c = 0.002, 0.005, 0.010\ \mathrm{m^{-1}}$ | drag error is monotone and measurable; the vacuum formula is an upper bound on range |
| 400 m drop: 9.0258 s (vacuum) versus 10.2635 s (drag) | a 13.7% timing difference that a calibration test can measure |

> **Breaking exercise.** In §1 of the script, set the horizontal speed to
> 2 km/s and predict the landing distance before running; it is of order
> $v\sqrt{2h/g} = 9$ km. Then ask what the flat-Earth error would be at that
> range using $x^{2}/(2R)$: about 6 m. Compare with the distance and decide
> whether the flat-Earth model is adequate.

## 8. Common mistakes

1. **Using an average speed where an instantaneous one is meant.** A 10 Ma plate
   average includes millions of years of quiescence and a few earthquakes.
2. **Quoting a rate without an uncertainty, or with the wrong one.** The
   $n^{-3/2}$ law of §3.6 is the difference between a detection and a hope.
3. **Mixing depth-positive and height-positive vertical coordinates.** The sign
   is not checkable by dimensions.
4. **Assuming component independence in the presence of drag.** Drag depends on
   the total speed; the equations do not separate.
5. **Applying the vacuum projectile range formula outside its regime.** The
   curvature error is 785 m at 100 km range; drag matters above about
   70 m/s in the demonstration's parameters.
6. **Differentiating a noisy position series twice** and treating the result as
   an acceleration. Differentiation amplifies high-frequency noise.
7. **Forgetting that $v^{2} = v_0^{2}+2a\Delta x$ requires constant $a$.**
   Apply it to a variable-acceleration segment and the error is not small.
8. **Reporting speed as velocity.** In geodesy the direction is often the
   scientific content (a rotation pole, a strain axis).

## 9. Real-world applications

1. **Plate motion from GNSS.** Positions differentiated over years; the $n^{-3/2}$
   scaling sets the duration of every velocity-field campaign.
2. **Seismic travel-time interpretation.** The average speed over a raypath is
   what a travel-time curve gives; turning that into a depth-dependent velocity
   is a kinematic inverse problem ([06-seismology](../../06-seismology/README.md)).
3. **Borehole and drop tests.** A dropped tool's arrival time measures
   $g$ and drag; the demo's 1.24 s difference is the observable.
4. **Rockfall and avalanche runout.** Energy-based estimates of impact speed are
   kinematic inferences; the drag regime determines whether they hold.
5. **Seismic source dynamics.** The far-field ground velocity pulse is a
   kinematic observation from which source parameters are inferred; the
   double-couple has zero net momentum, so the *pulse*, not the momentum, is
   what is measured ([02-02-04](./04-momentum.md)).
6. **Satellite orbit determination.** Position and velocity are integrated
   forward from a state vector; the "kinematics" here is the two-body and
   perturbation problem of [02-02-07](./07-central-forces.md).

## 10. Further reading

- **Kleppner, D., & Kolenkow, R. J. *An Introduction to Mechanics* (2nd ed.).**
  Chapters 1–3: the kinematic derivations of §3 done with unusual care about the
  assumptions. Level: beginner to intermediate.
- **Feynman, R. P., Leighton, R. B., & Sands, M. *The Feynman Lectures on
  Physics*, Vol. I, Chapters 8–10.** The kinematics of free fall and the
  Galileo argument; the treatment of the independence of components is the
  classic one. Level: beginner.
- **Taylor, J. R. *Classical Mechanics*.** Chapter 2 covers projectile motion
  with and without drag, including the linear-drag closed form of §3.4.
  Level: intermediate.
- **Segall, P. *Earthquake and Volcano Deformation*.** Chapter 1–2: how GNSS
  position series become velocity and strain fields, with the noise and
  duration issues of §3.6. Level: graduate.
- **Hofmann-Wellenhof, B., Lichtenegger, H., & Wasle, E. *GNSS — Global
  Navigation Satellite Systems.* ** For the frame and clock conventions behind
  any geodetic velocity. Level: intermediate.
- **Molnar, P., & Stock, J. M. papers on plate-motion frames.** For the
  difference between geological and geodetic rates, and why the reference frame
  must be named. Level: graduate.

> Citation note: bibliographic details are given so you can locate the works;
> this repository does not reproduce copyrighted text.

## 11. Related lessons

- [02-02-02 Newton's Laws and Free-Body Analysis](./02-newtons-laws.md) — where
  the *cause* of the acceleration is supplied.
- [02-02-03 Work, Energy, Power and Conservative Forces](./03-work-energy.md) —
  the energy route to speeds, which avoids integrating the equation of motion.
- [02-01-03 Scaling Laws, Similarity and Dimensional Reasoning](../01-measurement-and-physical-reasoning/03-scaling-laws.md) —
  the $n^{-3/2}$ scaling of §3.6 is one more example of the same reasoning.
- [02-03-04 Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity](../03-oscillations-and-waves/04-wave-basics.md) —
  where speeds belong to waves rather than particles.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — where geodetic
  positions and their rates are the primary data.

## Exercises

Attempt the graded problems in
[`exercises/01-kinematics-exercises.md`](./exercises/01-kinematics-exercises.md),
then compare with
[`exercises/01-kinematics-solutions.md`](./exercises/01-kinematics-solutions.md).

## Self-assessment checklist

- [ ] I can derive $v = v_0+at$, $x = x_0+v_0t+\tfrac12at^{2}$ and
      $v^{2} = v_0^{2}+2a\Delta x$ by integration, and say what each assumes.
      (Section 3.1)
- [ ] I can derive the vacuum projectile range and identify the launch angle
      that maximises it. (Section 3.2)
- [ ] I can state the condition under which horizontal and vertical motion
      decouple, and give an example where it fails. (Section 3.3)
- [ ] I can solve the linear-drag equation and quote its terminal velocity and
      time constant. (Section 3.4)
- [ ] I can give the drag speed at which drag equals gravity for a stated drag
      coefficient, and use it as a regime boundary. (Section 5.3)
- [ ] I can compute the flat-Earth error $x^{2}/(2R)$ at a stated range and
      decide whether the approximation is usable. (Section 5.2)
- [ ] I can derive and apply the $n^{-3/2}$ scaling of a fitted rate.
      (Section 3.6)
- [ ] I can name the vertical sign convention in a figure or dataset before
      interpreting its rates. (Section 4.2)
