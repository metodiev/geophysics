---
id: 06-04-03
title: "Relative Location: Master-Event, Double-Difference, HypoDD"
level: graduate
prereqs: ["06-04-01", "06-04-02", "06-02-02"]
tags: [seismology, relative-location, double-difference, cross-correlation, earthquake-cluster]
---

# Relative Location: Master-Event, Double-Difference, HypoDD

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the differential-time equation for a pair of events at one
   station and show that the station delay cancels exactly.
2. **Derive** the classic double-difference residual, in which the station term
   and the path error are both removed by differencing residuals across events.
3. **Quantify** the improvement in cluster geometry obtained from a directly
   measured time difference, and **explain** why differencing two independent
   picks does not by itself improve anything.
4. **Derive** why a uniform velocity error survives in an absolute location but
   almost cancels in a relative one, and state the conditions under which the
   cancellation is incomplete.
5. **Compute** the bias that a station-delay pattern imposes on an absolute
   location as a projection, and check the prediction against measurement.
6. **State** precisely what relative location cannot deliver, and why the
   reported improvement is in precision rather than in accuracy.

## Prerequisites

- [01 Hypocentre Location: Arrival Times, Inversions and Error Ellipses](01-hypocentre-location.md) —
  the Jacobian, the residual and the normal equations.
- [02 Dependence on the Velocity Model and Joint Inversion](02-velocity-model-dependence.md) —
  the uniform-scaling theorem used in Section 3.4.
- [06-02-02 Snell's Law, Layered Media and the Travel-Time Curve](../02-ray-theory-and-travel-times/02-snell-and-layering.md).

## 1. Intuition: subtract before you invert

Absolute location fails in a way that has nothing to do with pick noise. A
seismic station has a **site delay**: the last few kilometres of the path pass
through weathered rock and sediment whose velocity is unknown, and every arrival
at that station is late or early by the same amount. That delay is a signal in
the data and an unmodelled nuisance in the inversion, and an absolute locator
absorbs it into position. The demonstration measures this and finds a bias of
$(+867, -210, +810)\ \mathrm{m}$ from a delay pattern whose mean is only
$-8.95\ \mathrm{ms}$ and whose standard deviation is $95.9\ \mathrm{ms}$.

Relative location attacks that directly. If two events are close enough that
their rays to a given station are nearly the same, then the station delay is the
*same unknown* in both arrivals and **cancels in the difference**. The same is
true of a systematic velocity error along the path. What does *not* cancel is
whatever differs between the two paths: the geometry, and the measurement error
in the difference itself.

The honest difficulty of this lesson is contained in the previous sentence, and
it is not the one most introductions emphasise. Differencing removes the
nuisance term — but if the difference is formed by subtracting two independently
picked times, the pick noise doubles and the depth/origin-time trade-off
survives, and the cluster geometry can end up no better than before. What buys
the improvement is measuring the *difference* directly, by cross-correlation of
similar waveforms, at a precision one or two orders of magnitude better than a
pick. The demonstration measures all three variants.

## 2. The equations

### 2.1 Absolute location, with a station term written down

Let event $j$ be recorded at station $i$ at time

$$
t_{ij}^{\text{obs}} = \tau_i + t_{0j} + T_{ij}(\mathbf{e}_j) ,
$$

where $\tau_i$ is the unknown station delay, $t_{0j}$ the origin time and
$T_{ij}$ the travel time from event $j$ to station $i$ in the chosen model.
An absolute locator solves for $(\mathbf{e}_j, t_{0j})$ and treats $\tau_i$ as if
it were zero. Because $\tau_i$ is common to every event, it cannot be averaged
away by locating more events: it biases all of them together.

### 2.2 The differential-time equation

For a master event $0$ at the same station,

$$
t_{ij}^{\text{obs}} - t_{i0}^{\text{obs}}
= \big(t_{0j} - t_{00}\big) + \big(T_{ij}(\mathbf{e}_j) - T_{i0}(\mathbf{e}_0)\big)
= \Delta t_{0j} + \Delta T_{ij} ,
$$

and $\tau_i$ is gone. The unknowns for event $j$ are its offset from the master
and the difference of origin times: four parameters, exactly as before, but with
the station term excluded from the model instead of absorbed into the geometry.

### 2.3 The double difference

The master-event form still assumes the master's own location is right. The
double-difference form removes that assumption by working with pairs of events
at pairs of stations. Define the residual of the observed differential time

$$
r_{ij} = \Delta t_{ij}^{\text{obs}} - \Delta T_{ij}^{\text{pred}} ,
$$

and form the **double difference** of two such residuals, for events $j$ and $k$
at the same station $i$:

$$
\mathrm{DD}_{ijk} = r_{ij} - r_{ik} .
$$

Substituting the model of Section 2.1 shows what this removes:

$$
r_{ij} = \tau_i + \delta t_{0j} + \delta T_{ij} ,
\qquad
r_{ik} = \tau_i + \delta t_{0k} + \delta T_{ik} ,
$$

so

$$
\mathrm{DD}_{ijk} = \delta t_{0j} - \delta t_{0k} + \delta T_{ij} - \delta T_{ik} ,
$$

with no $\tau_i$ at all: the station term cancels **without being estimated**.
This is why double-difference location (the family of codes usually called
HypoDD) works on dense clusters with poor stations, and why the same trick
removes a uniform velocity error to first order as well.

## 3. Derivations

### 3.1 The linear system

Linearising about current positions, the predicted differential time for a small
offset $\delta\mathbf{e}_j$ is

$$
\Delta T_{ij} \approx \Delta T_{ij}^{(0)}
+ \frac{\partial T_{ij}}{\partial \mathbf{e}_j}\cdot\delta\mathbf{e}_j
- \frac{\partial T_{i0}}{\partial \mathbf{e}_0}\cdot\delta\mathbf{e}_0 .
$$

With a homogeneous medium the derivative is the one of lesson
[01](01-hypocentre-location.md), $\nabla T = (-u_x, -u_y, +u_z)/v$ with
$\mathbf{u}$ the unit vector from source to station. Stacking all pairs gives a
large sparse linear system solved by damped least squares. The damping matters:
clusters that are small compared with the station distance have a strong
depth/origin-time trade-off for each *pair*, so an undamped solution can move
events by kilometres along that direction while barely changing the residual.

### 3.2 The improvement factor comes from the measurement, not the subtraction

Let the pick error have standard deviation $\sigma_{\text{pick}}$. A differential
time formed from two picks has error, if the errors are independent,

$$
\sigma_{\Delta}
= \sqrt{\sigma_{\text{pick}}^{2} + \sigma_{\text{pick}}^{2}}
= \sqrt{2}\,\sigma_{\text{pick}} ,
$$

so differencing *increases* the noise by 41 per cent. A cross-correlation of two
similar waveforms, by contrast, measures the delay between them with precision
$\sigma_{\text{dd}}$ set by the signal-to-noise ratio and the bandwidth rather
than by the absolute timing of either arrival, and it can be far smaller than
$\sigma_{\text{pick}}$.

Because a location error scales with the noise of whatever times are used, the
improvement in cluster geometry is approximately the ratio

$$
\frac{\text{error with picks}}{\text{error with cross-correlation}}
\approx \frac{\sqrt{2}\,\sigma_{\text{pick}}}{\sqrt{2}\,\sigma_{\text{dd}}}
= \frac{\sigma_{\text{pick}}}{\sigma_{\text{dd}}} .
$$

In the demonstration this ratio is $20\ \mathrm{ms}/2\ \mathrm{ms} = 10$, and the
measured improvement is a factor of 24 on the cluster geometry — the same order,
with the difference coming from how the noise propagates through the
depth/origin-time trade-off.

### 3.3 Why the station term cancels, and why the velocity error mostly does

For two events separated by a small vector $\delta\mathbf{e}$, the travel-time
difference is

$$
\Delta T_{i} \approx \nabla T_i \cdot \delta\mathbf{e} ,
$$

so a *station-independent* error in $\nabla T_i$ — a wrong velocity along the
path — multiplies the same small quantity in both the absolute and the relative
problem. In the absolute problem the error is $\nabla T_i \cdot \delta\mathbf{e}$
with $\delta\mathbf{e}$ of the size of the *source–station* geometry, which is
kilometres; in the relative problem it is the same operator applied to the
*event separation*, which is hundreds of metres. That is the whole reason
relative locations are robust: the error term is proportional to the event
separation, not to the event–station distance.

Formally, with a uniformly scaled model the predicted travel time becomes
$T/s$ (lesson [02](02-velocity-model-dependence.md) Section 3.1). The
differential time becomes $\Delta T/s$, so

$$
\delta(\Delta T) = \Delta T\left(\frac{1}{s} - 1\right) \approx -\Delta d\,
\Delta T ,
$$

which is *first order in the differential travel time* — a small number when the
two events are close — whereas in the absolute problem the corresponding error
is first order in the total travel time, which is large. The cancellation is
therefore not exact; it is a cancellation of the leading term, and its residual
grows with event separation, with depth, and with any horizontal gradient.

## 4. Worked examples

All numbers are printed by `code/relative_location_demo.py`. Its synthetic
experiment uses $v = 3500\ \mathrm{m\,s^{-1}}$, 8 stations spanning 12.0 by
11.0 km, a master event at $(4.00, -2.00, 7.00)\ \mathrm{km}$, nine further events
scattered about it with $\sigma = 400\ \mathrm{m}$ in each coordinate,
$\sigma_{\text{pick}} = 20\ \mathrm{ms}$, and a per-station delay drawn once with
$\sigma_{\text{station}} = 100\ \mathrm{ms}$.

### Example 1 — the bias a station delay imposes on an absolute location

Each event located independently against the noisy picks gives 3-D errors from
$454$ to $2122\ \mathrm{m}$; after removing the mean, the scatter is
$692.5\ \mathrm{m}$ horizontally and $1083.7\ \mathrm{m}$ in depth. The mean
error, common to every event, is

$$
(\delta x, \delta y, \delta z) = (+867.2, -210.0, +810.0)\ \mathrm{m} .
$$

That bias is predictable rather than mysterious. Solve the linearised problem
for the position shift that best reproduces the delay pattern itself:

$$
J\,\delta\mathbf{m} \approx \boldsymbol{\tau}
\quad\Longrightarrow\quad
\delta\mathbf{m} = (+869.7, -266.1, +1016.5)\ \mathrm{m},
\quad \delta t_0 = -0.322\ \mathrm{s},
$$

with $J$ the absolute-location Jacobian at the master. The prediction matches the
measured bias to a few tens of metres, and it shows that the *mean* of the
delays is nearly irrelevant — only $-8.95\ \mathrm{ms}$ — while their *pattern*
moves the event by nearly a kilometre. Every absolute location in this
experiment is wrong in the same direction, and no amount of averaging over the
cluster fixes it.

### Example 2 — three ways to get the cluster geometry

Measure the cluster geometry three ways, all on the same synthetic arrivals, and
compare each offset with the true offset from the master:

| method | rms offset error (m) | max error (m) |
|---|---|---|
| absolute locations, offsets taken | 1594.3 | 2333.5 |
| relative, difference of two picks | 1870.2 | 2777.7 |
| relative, measured difference | 78.2 | 191.1 |

Read the rows in order, because the middle row is the warning, and read it
carefully. Taking offsets against a master already removes any error common to
the cluster, so the bias of Example 1 is absent from the first **and** the second
row: the difference between them is not the bias. Differencing two independent
picks doubles the timing noise ($20\ \mathrm{ms}$ each become about
$28\ \mathrm{ms}$), and the pairwise depth/origin-time trade-off is strong for
events that nearly coincide, so the middle row is *worse* than the row above it:
$1870\ \mathrm{m}$ against $1594\ \mathrm{m}$. Measuring the difference directly
improves on both by a factor of

$$
\frac{1870.2}{78.2} = 23.9 ,
$$

which is the number to remember: relative location is worth precisely as much as
the precision with which the *difference* is measured.

### Example 3 — the same experiment with a 3 per cent velocity error

Locating everything with $v = 3395\ \mathrm{m\,s^{-1}}$, 3 per cent too slow:

| quantity | correct velocity | 3 % low |
|---|---|---|
| absolute depth bias, mean (m) | 810.0 | 1208.0 |
| absolute 3-D scatter after bias removal (m) | 476.5 | 491.3 |
| relative rms error, pick differences (m) | 1870.2 | 1924.0 |
| relative rms error, measured differences (m) | 78.2 | 67.5 |

The absolute depth bias grows by $398\ \mathrm{m}$ — a 49 per cent increase —
while the relative error with measured differences is unchanged within the
scatter of a single realisation ($78.2$ to $67.5\ \mathrm{m}$). The 3 per cent
velocity error is real, it is much larger than any realistic model error, and
the relative solution does not see it, because the error is nearly common to the
two events that share almost the same ray paths. That is the entire reason
double-difference catalogues exist.

### Example 4 — the expected improvement, from the noise levels

Sections 3.2 and 3.3 predict an improvement of order
$\sigma_{\text{pick}}/\sigma_{\text{dd}} = 20/2 = 10$ on the geometry.
The measured factor is 24. The two are the same order of magnitude and not
equal, which is the honest outcome: the noise does not propagate into the
geometry with unit gain, because the depth/origin-time trade-off partly converts
timing error into a direction the geometry is less sensitive to. Quoting the
ratio as "about ten to twenty times" is defensible; quoting "24" as a law is not.

## 5. Assumptions and regime of validity

1. **The two events are close enough that their rays coincide.** Formally, the
   cancellation of $\tau_i$ is exact for any pair (because $\tau_i$ is
   station-specific), but the cancellation of *velocity* error and of anything
   else path-dependent requires a small separation. A 10 km cluster on a 12 km
   aperture is outside this regime.
2. **The waveforms are similar enough to cross-correlate.** For events of very
   different size or mechanism, the correlation degrades and the measured
   difference is biased toward zero.
3. **Station delays are truly station-specific.** The cancellation fails when
   the "station term" is really a source-side or path term that varies between
   events — for example two events at different depths, whose last kilometre
   passes through different material.
4. **The reference (master) location is right.** All relative locations are
   differences from it, so a wrong master shifts the whole cluster and the
   demonstration's offset comparison is measured relative to the master's own
   estimate.
5. **The relative geometry is not guaranteed better.** Example 2 shows it can be
   worse. The method is a technique, not a cure.
6. **The linearisation is about small offsets.** Relative location is a
   refinement of an existing catalogue, not a standalone locator.

## 6. What relative location cannot do

Relative locations are differences, and every property of a difference that is
common to all its terms is invisible to it:

- a wrong master shifts the whole cluster;
- a wrong regional velocity shifts the whole cluster;
- a wrong reference station delay shifts the whole cluster.

So the improvement demonstrated in Example 2 is an improvement in the
**precision of the geometry**, not in the accuracy of where the cluster sits on
the Earth. A double-difference catalogue should therefore always be reported
with the absolute reference it was tied to — and that reference carries all of
the problems of absolute location from lessons
[01](01-hypocentre-location.md) and [02](02-velocity-model-dependence.md).

## 7. The demonstration

```bash
cd 06-seismology/04-earthquake-location-and-magnitude/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python relative_location_demo.py
```

It builds the synthetic cluster, locates every event absolutely by Gauss-Newton,
then relatively against the master, then repeats both with a 3 per cent velocity
error, and prints the projection of the delay pattern onto the model space.

Exercises:
[`exercises/03-relative-location-exercises.md`](exercises/03-relative-location-exercises.md)
and
[`exercises/03-relative-location-solutions.md`](exercises/03-relative-location-solutions.md).

> All models and data in this module are **SYNTHETIC**. The events, the network,
> the delays and the noise are teaching values; no real earthquake, station or
> catalogue is used.

## Mastery checkpoint

Without notes:

1. Write the differential-time equation and circle the term that cancels.
2. Derive $\sigma_{\Delta} = \sqrt{2}\sigma_{\text{pick}}$ and state the
   consequence for a location computed from differenced picks.
3. Explain why a uniform velocity error affects a relative location far less
   than an absolute one, using the event separation rather than hand-waving.
4. State the three things a relative location cannot detect, and what must
   therefore accompany a relative catalogue.
5. Given $\sigma_{\text{pick}} = 20\ \mathrm{ms}$ and
   $\sigma_{\text{dd}} = 1\ \mathrm{ms}$, predict the order of the improvement in
   cluster geometry.

## Common pitfalls

1. **Believing differencing alone improves the catalogue.** It removes the bias
   and can leave the geometry worse.
2. **Cross-correlating dissimilar events.** The measured delay is then biased
   toward zero, which compresses the cluster and invents a tight geometry.
3. **Reporting relative depths as absolute depths.** The reference is the
   master, and the master came from an absolute location.
4. **Ignoring the linearisation limits.** Relative location refines; it does not
   locate from scratch.
5. **Forgetting the separation limit.** The cancellation of velocity error is a
   leading-order statement whose residual grows with event separation.
6. **Quoting an improvement factor without the noise levels.** The factor is a
   ratio of precisions, and it means nothing without them.

## Related modules

- [01 Hypocentre Location: Arrival Times, Inversions and Error Ellipses](01-hypocentre-location.md).
- [02 Dependence on the Velocity Model and Joint Inversion](02-velocity-model-dependence.md).
- [06-12 Induced and Triggered Seismicity](../12-induced-and-triggered-seismicity/README.md) —
  where millimetre-to-metre relative accuracy is the whole measurement.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the rank and damping questions of Section 3.1.
