---
id: 14-06-02
title: "Groundwater-Surface Water Interaction"
level: research
prereqs: ["14-06-01", "14-01-03", "14-01-05"]
tags: [hydrology, hydrogeophysics, groundwater-surface-water, temperature, seepage, tracer-dilution, streambed]
---

# Groundwater-Surface Water Interaction

**All models and data in this module are SYNTHETIC.** There is no real stream,
aquifer, piezometer, temperature probe or tracer injection in this lesson. The
reach is an idealised one-dimensional column, every parameter is a chosen
teaching value, and all numbers come from
[`code/groundwater_surface_water_demo.py`](./code/groundwater_surface_water_demo.py).
No site is named and no published measurement is quoted.

The exchange between a stream and the aquifer beneath it is the place where
hydrology, hydrogeology and hydrogeophysics meet most directly, because it is
where the water changes compartment. The exchange controls streamflow in dry
periods, the temperature and chemistry of the stream, the fate of nutrients and
contaminants in the hyporheic zone, and the legal question of how much of a
pumping licence is captured from a river. It is also one of the hardest things to
measure, because it is a flux through a boundary that is metres wide and
hundreds of metres long, and the natural fluctuations that make it interesting —
a storm, a diurnal temperature cycle, a pumping cycle — are the same fluctuations
that make it hard to isolate.

This lesson works through the four measurements that are actually available at a
reach — a piezometer pair, a temperature profile, a salt-dilution gauging, and a
resistivity section — and derives what each one *measures*, with units. The
result is a reconciliation table in which the entries are not interchangeable:
some are Darcy velocities, one is a seepage velocity, one is a discharge, and one
is a resistivity contrast. Turning any of them into another requires an effective
porosity or a petrophysical link, and neither of those is among the measurements.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a reach-scale exchange flux from a piezometer pair, with the sign
   convention stated and the dependence on the assumed conductivity quantified.
2. **Derive** the one-dimensional periodic solution for temperature in a
   saturated porous medium with vertical flow, and **define** the conductive skin
   depth.
3. **Show** that the phase lag of the diurnal signal determines only the
   *magnitude* of the seepage velocity while the amplitude ratio determines its
   *sign*, and **quantify** both inversions.
4. **Demonstrate** that a layered streambed breaks a homogeneous inversion, and
   use the inconsistency between the amplitude and phase estimates as a
   diagnostic of model error.
5. **Compute** a stream discharge from a salt-dilution gauging, and **show** the
   error introduced by truncating the integration window.
6. **Compute** the apparent-resistivity signature of a losing reach against a
   stated noise level, and **state** what a resistivity contrast does and does
   not say about the flux.
7. **Reconcile** Darcy, temperature-derived and dilution estimates by stating,
   for each, what it measures and what assumption carries it.

## Prerequisites

- [14-06-01 Integrated Catchment Characterisation](01-catchment-characterisation.md)
  — the water balance and the hydrograph separation that the exchange feeds.
- [14-01-03 Hydraulic Head, Darcy's Law and Groundwater Flow](../01-hydrology-fundamentals/03-hydraulic-head-darcy.md)
  — Darcy's law and the head gradient.
- [14-01-05 Groundwater Chemistry and Salinity](../01-hydrology-fundamentals/05-groundwater-chemistry.md)
  — the conductivity–concentration link used in the dilution method.
- [14-04-03 Seawater Intrusion and Coastal Aquifer Monitoring](../04-contaminant-and-environmental/03-saline-intrusion.md)
  — the salinity mapping that the resistivity contrast depends on.
- [10-03-01 GPR for Soil Moisture, Water Table and Aquifer Structure](../../10-gpr-near-surface/03-gpr-applications/01-gpr-hydrogeology.md)
  — a complementary shallow method for the same streambed.

## 1. What "exchange" means, and why it is a flux

Take a stream flowing over an aquifer, and define the depth $z$ positive
downward from the streambed surface. The vertical specific discharge (Darcy
flux) across the bed is

$$q_z = -K\frac{\partial h}{\partial z}
\qquad (\mathrm{m\,d^{-1}}),$$

positive downward. Two sign conventions matter and must be stated once:

- $q_z > 0$ means water leaves the stream: a **losing** reach. The aquifer
  recharges, the streambed drains, and the hyporheic zone is oxygenated.
- $q_z < 0$ means water enters the stream: a **gaining** reach. The streambed is
  saturated, upward, and the stream is fed by storage.

For the demonstration's SYNTHETIC reach ($K = 2.5\ \mathrm{m\,d^{-1}}$,
piezometers 8.0 m apart, and a head difference
$\Delta h = h_{\text{stream}} - h_{\text{aquifer}}$):

| season | $\Delta h$ (m) | $q_z$ (m/d) | seepage $v = q_z/n_e$ (m/d) | exchange (m³ d⁻¹ per m) |
|---|---|---|---|---|
| gaining | $-0.32$ | $-0.1000$ | $-0.4000$ | $-0.2000$ |
| losing | $+0.10$ | $+0.0312$ | $+0.1250$ | $+0.0625$ |

with $n_e = 0.25$ used for the conversion (Section 7). The reach reverses
direction seasonally, and the magnitude of the gaining flux is **3.2 times** the
losing flux. The sign of a reach-scale exchange is a robust measurement — it is
a head difference of centimetres and the conductivity cannot change it. The
magnitude is not: it is linear in $K$, and $K$ was not measured by the two
piezometers.

Note also the units of the "exchange" column: multiplying $q_z$ by the reach
length in metres gives m³ d⁻¹ per metre of stream width, which is what a water
balance needs. A reach-scale budget uses $q_z \times L_{\text{reach}} \times
W_{\text{stream}}$, and both $L$ and $W$ are usually the largest uncertainties in
it.

## 2. Stream temperature as a tracer

The reason temperature is so useful is that the stream imposes a large, periodic
boundary condition on the bed — a diurnal cycle of several kelvin, and a seasonal
cycle of tens of kelvin — and the subsurface responds to it in a way that depends
on how fast water is moving. Advection carries the signal downward faster than
conduction; upwelling flow pushes a constant deep temperature toward the surface
and suppresses the signal.

With $\kappa$ the thermal diffusivity of the saturated medium, $v$ the seepage
velocity positive downward and a surface temperature $T(0,t) = \bar{T} +
A\cos\omega t$, the periodic solution of

$$\kappa\frac{\partial^2 T}{\partial z^2}
- v\frac{\partial T}{\partial z}
= \frac{\partial T}{\partial t}$$

that decays with depth is $T = A\,\mathrm{e}^{\mathrm{i}\omega t}\mathrm{e}^{\lambda z}$
with

$$\lambda = a - b, \qquad
a = \frac{v}{2\kappa}, \qquad
b = \sqrt{a^2 + \frac{\mathrm{i}\omega}{\kappa}}.$$

Separating real and imaginary parts gives the two measurable quantities over a
depth separation $L$:

$$\boxed{\;\text{ratio} = \exp\!\left[-\left(\operatorname{Re} b - a\right)L\right],
\qquad
\text{lag} = \left(\operatorname{Im} b\right)L .\;}$$

Three consequences follow directly, and they are the whole of the method.

- **The phase lag is even in $v$**: $\operatorname{Im} b$ depends on $a^2$, so
  $+v$ and $-v$ give the same lag. The phase therefore measures $|v|$ and
  *cannot* give the direction of flow.
- **The amplitude ratio is asymmetric in $v$**: $\operatorname{Re} b - a$ decreases as
  $v$ increases, so the ratio is strictly increasing in $v$, upwelling flow
  attenuating the signal more than downwelling flow at the same speed. The
  amplitude ratio gives the sign — and, being monotone, a unique magnitude too.
- **The conductive skin depth** $d = \sqrt{2\kappa/\omega}$ is the depth over
  which a purely conductive signal decays by $1/\mathrm{e}$. For
  $\kappa = 1.0\times10^{-6}\ \mathrm{m^2\,s^{-1}}$ (a stated SYNTHETIC value for
  a saturated sand) and a diurnal period,

$$d = \sqrt{\frac{2\times10^{-6}}{7.272\times10^{-5}}}
= \sqrt{0.02750} = 0.1658\ \mathrm{m}.$$

The demonstration places probes at $z_1 = 0.15$ m and $z_2 = 0.30$ m, chosen so
that the separation is comparable to the skin depth: much shallower and the
signal is insensitive to flow, much deeper and the diurnal amplitude is lost.

### 2.1 The homogeneous-bed response

Solving the equation numerically on a fine grid (and verifying against the
analytic $\lambda$ above) gives, for $A = 4.0$ K:

| $v$ (m/d) | ratio $A(z_2)/A(z_1)$ | phase lag (h) | inverted $v$ from ratio (m/d) |
|---|---|---|---|
| $-0.80$ | 0.1754 | 2.9875 | $-0.800$ |
| $-0.40$ | 0.2765 | 3.3295 | $-0.400$ |
| $-0.10$ | 0.3704 | 3.4462 | $-0.0999$ |
| $0.00$ | 0.4048 | 3.4542 | $+0.0001$ |
| $+0.10$ | 0.4406 | 3.4462 | $+0.1001$ |
| $+0.40$ | 0.5537 | 3.3295 | $+0.400$ |
| $+0.80$ | 0.7036 | 2.9875 | $+0.7999$ |

The amplitude inversion returns the true velocity in every row — the mapping is
monotone. The phase column is symmetric: $+0.40$ and $-0.40$ m/d both give
3.3295 h, equal to $2\times10^{-13}$ h, and the phase inversion returns
$\pm0.401$ m/d. **A study that reports only a phase-derived velocity has measured
a speed, not an exchange direction**, and in a stream context that is the
difference between a gaining and a losing reach.

## 3. A layered bed, and the value of an inconsistency

The homogeneous solution above assumes one $\kappa$. Real streambeds are layered —
sand, silt, an organic mat — and the silt layer is both finer and less conductive
of heat. The demonstration adds a SYNTHETIC silt layer from 0.08 to 0.18 m with
$\kappa = 4.0\times10^{-7}\ \mathrm{m^2\,s^{-1}}$, and retains the true
$v = -0.40$ m/d (upward, the gaining reach of Section 1):

| bed model | ratio | lag (h) |
|---|---|---|
| homogeneous truth | 0.2765 | 3.3295 |
| layered truth | 0.1918 | 3.9893 |

Now invert with the homogeneous model:

- From the **amplitude ratio**: the homogeneous inversion returns
  $v = -0.7268$ m/d, an error of $+82\%$ — the right sign, the wrong size.
- From the **phase lag**: **there is no solution at all.** The largest lag any
  homogeneous bed can produce at this separation is 3.4549 h (at $v = 0$, where
  the lag is maximal), and the layered bed shows 3.9893 h. The homogeneous model
  is rejected outright by the data.

The second result is the useful one. **A model that cannot fit the data is more
informative than a model that fits it well**: the failure tells you that the
assumption is wrong, and it tells you which assumption — and if the study had
reported only the amplitude-derived velocity, it would have published
$-0.73\ \mathrm{m\,d^{-1}}$ with no warning that anything was amiss. The remedy
is either to include the layering in the model (a thermal-conductivity log or a
core is needed) or to use a probe pair that straddles a single layer.

## 4. Salt-dilution gauging: a discharge, not a velocity

Where the stream is turbulent and well mixed, the discharge can be measured by
injecting a known mass of salt and integrating the conductance rise:

$$Q = \frac{M}{\int_0^{t_{\max}} \Delta C(t)\,\mathrm{d}t}.$$

The method is exact for a conservative tracer with complete mixing, and it is
attractive because it measures the *stream* discharge rather than a point flux.
The demonstration's SYNTHETIC injection of $M = 2.00$ kg gives a conductance
curve (a Gaussian peak plus a slow tail) and:

| integration limit (s) | $\int \Delta C\,\mathrm{d}t$ (kg s m⁻³) | $Q$ (m³/s) | error |
|---|---|---|---|
| 1500 | 23177.14 | $8.63\times10^{-5}$ | $+7.39\%$ |
| 1800 | 23641.18 | $8.46\times10^{-5}$ | $+5.28\%$ |
| 2400 | 24273.30 | $8.24\times10^{-5}$ | $+2.54\%$ |
| 3600 | 24889.25 | $8.04\times10^{-5}$ | $0.00\%$ |

The injected mass is exact; the *integral* is not. Cutting the record 900 s after
the peak over-estimates the discharge by 5.3%, because the tail still carries
tracer. Reporting a dilution discharge therefore requires the integration window,
the sampling interval and the tail treatment — and at a losing reach, part of the
injected tracer may leave the stream entirely, so the method measures the
*stream*, not the exchange.

## 5. The resistivity signature, and what it does not say

A losing reach builds a saturated, lower-resistivity zone beneath the bed; a
gaining reach drains it. Using the two-layer Wenner series of
[14-05-01 §3](../05-hydrogeophysical-monitoring/01-time-lapse-ert.md) with a
saturated zone of $60\ \Omega\,\mathrm{m}$ under a dry bed of
$300\ \Omega\,\mathrm{m}$, and $2\%$ relative noise:

| $h$ (m) | best spacing (m) | $\rho_a$ ($\Omega$ m) | ratio | detections |
|---|---|---|---|---|
| 0.5 | 0.5 | 77.7 | 0.2589 | 37.1 sd |
| 1.0 | 0.5 | 63.4 | 0.2114 | 39.4 sd |
| 2.0 | 0.5 | 60.5 | 0.2016 | 39.9 sd |

At a fixed spacing of 1.0 m the apparent resistivity is 300.0 (dry bed), 115.8,
77.7 and 63.4 $\Omega$ m for $h = 0.5, 1.0, 2.0$ m. The contrast is large and
easily detected, and the spacing that detects it best is the shortest one —
which is the same lesson as in the time-lapse ERT lesson.

What the section *does not* give is a flux. The resistivity contrast is produced
by saturation and by pore-water conductivity, which are the same two quantities
that 14-05-01 showed to be inseparable from a resistivity measurement alone; and
even a correctly inverted saturation profile gives a *state*, not a *rate*.
Turning it into a flux needs the Archie link, the porosity, and an assumption
about how long the wetting has persisted — three assumptions to produce the one
number the hydrologist asked for.

## 6. Reconciliation: four methods, four quantities

| method | measures | gaining reach | losing reach | assumption that carries it |
|---|---|---|---|---|
| piezometer pair (Darcy) | $q_z$ (m d⁻¹) | $-0.1000$ | $+0.0312$ | $K$ of the bed |
| diurnal temperature | $v$ (m d⁻¹) | $-0.4000$ | $+0.1250$ | homogeneous, steady flow |
| salt dilution | $Q$ (m³ s⁻¹) | see Section 4 | see Section 4 | complete mixing |
| ERT | ratio $\rho$ | not resolvable | 0.2000 | Archie and a porosity |

The consistency check is the porosity link,

$$q_z = n_e v,
\qquad -0.1000 = 0.25 \times (-0.4000), \qquad +0.0312 = 0.25 \times (+0.1250),$$

which is exact here **because the two columns were built from the same numbers**.
With field data they agree only if $K$, $n_e$ and the *structure* of the
temperature model are all right, and none of these four methods measures the
others' assumptions. The honest reporting form is the table above with its last
column filled in — a list of numbers *and* a list of what each one needs to be
believed.

## 7. Assumptions and regime of validity

1. **Vertical, one-dimensional flow through a homogeneous bed.** Lateral
   hyporheic flow, bedforms and a sloping water table all break this; the
   temperature method then measures an effective velocity along a path that is
   not the one in the equation.
2. **Steady flow over the timescale of the signal.** For a diurnal signal, the
   flow must be steady for about a day; for a seasonal signal, for months. A
   pumping cycle violates this, and the amplitude and phase then disagree in
   exactly the way Section 3 describes — with a physical instead of a structural
   cause.
3. **Conduction is the only non-advective transport.** Thermal dispersivity and
   free convection in coarse gravel are neglected.
4. **The thermal properties are known.** $\kappa$ and the heat capacity of the
   saturated medium enter both $a$ and $b$; a 20% error in $\kappa$ is a
   comparable error in the inferred velocity, in the opposite direction to the
   one produced by a wrong porosity.
5. **The streambed temperature is a single sinusoid of known amplitude.** In
   reality the surface signal is the stream temperature, which varies with
   shading, inflow and air temperature; the amplitude must be measured at the
   interface, not in the air.
6. **Darcy's law applies at the bed scale.** In gravel with high flow rates the
   Forchheimer correction becomes relevant; at the other extreme, fine silt can
   make the bed a "disconnected" boundary on the timescale of the stream's
   fluctuations, in which case the exchange flux is controlled by the bed
   conductance rather than by the aquifer's head.
7. **Dilution gauging requires complete mixing.** A reach with pools, dead zones
   or tributary inflows fails the assumption; the tracer recovery is the test.

The regime of best validity is a sand-bed, single-layer, low-gradient reach with
a hydraulic gradient that is stable over days, an instrumented temperature
profile, and an independent measurement of the bed's thermal conductivity. The
regime of worst validity is a pool-riffle sequence on a gravel bed with a pumping
well nearby, where every one of the assumptions above fails and the methods
disagree — and the disagreement is the measurement.

## 8. Worked examples

### Example 1 — the skin depth and a probe spacing

For a diurnal period, $\omega = 2\pi/86400 = 7.272\times10^{-5}\ \mathrm{s^{-1}}$.
With $\kappa = 1.0\times10^{-6}\ \mathrm{m^2\,s^{-1}}$:

$$d = \sqrt{\frac{2\kappa}{\omega}}
= \sqrt{\frac{2.0\times10^{-6}}{7.272\times10^{-5}}}
= \sqrt{0.02750} = 0.16584\ \mathrm{m}.$$

A probe pair at 0.15 m and 0.30 m spans $L = 0.15\ \mathrm{m} = 0.905d$. With no
flow, $\operatorname{Re}b = \operatorname{Im}b = \sqrt{\omega/2\kappa} = 6.030$ per
metre, so the ratio is

$$\exp(-6.030 \times 0.15) = \mathrm{e}^{-0.9045} = 0.4048$$

and the lag is $6.030 \times 0.15 = 0.9045$ rad, i.e.
$0.9045/7.272\times10^{-5}/3600 = 3.4542$ h. Both match the $v = 0$ row of the
table. **The correct probe separation is one that keeps the ratio in a measurable
range (roughly 0.2–0.8) and the lag larger than the sampling error**: closer than
$0.3d$ and both quantities are too close to 1 and 0 respectively.

### Example 2 — inverting the two observables by hand

Take $v = +0.40\ \mathrm{m\,d^{-1}} = 4.630\times10^{-6}\ \mathrm{m\,s^{-1}}$
(downward). Then

$$a = \frac{v}{2\kappa} = \frac{4.630\times10^{-6}}{2.0\times10^{-6}}
= 2.3150\ \mathrm{m^{-1}},$$

$$b = \sqrt{a^2 + \frac{\mathrm{i}\omega}{\kappa}}
= \sqrt{5.359 + 72.72\,\mathrm{i}} ,$$

and using $|5.359 + 72.72\mathrm{i}| = 72.917$ and
$\arg = 1.49725$ rad:

$$b = \sqrt{72.917}\,\mathrm{e}^{\mathrm{i}(1.49725/2)}
= 8.5392\,\mathrm{e}^{\mathrm{i}0.74863}
= 6.2583 + 5.8105\,\mathrm{i}.$$

Hence

$$\text{ratio} = \exp\!\left[-(6.2583 - 2.3150)(0.15)\right]
= \mathrm{e}^{-0.59150} = 0.5537,$$

$$\text{lag} = 5.8105 \times 0.15 = 0.87158\ \mathrm{rad}
= 3.3295\ \mathrm{h},$$

both matching the $+0.40$ row. Now repeat with $v = -0.40$: $a = -2.3150$, and

$$\operatorname{Re}b - a = 6.2583 + 2.3150 = 8.5733,
\qquad \text{ratio} = \mathrm{e}^{-1.2860} = 0.2765,$$

while $\operatorname{Im}b$ is unchanged at 5.8105, so the lag is again 3.3295 h.
**This is the arithmetic behind the entire asymmetry argument**: the amplitude
changes by a factor 2.0 between $+0.40$ and $-0.40$ m/d, and the phase does not
change at all.

### Example 3 — a dilution gauging by hand

The demonstration's full-window integral is
$\int \Delta C\,\mathrm{d}t = 24889.25\ \mathrm{kg\,s\,m^{-3}}$ for
$M = 2.00$ kg, so

$$Q = \frac{2.00}{24889.25} = 8.036\times10^{-5}\ \mathrm{m^3\,s^{-1}}.$$

Truncating at 1800 s gives $\int = 23641.18$ and

$$Q' = \frac{2.00}{23641.18} = 8.460\times10^{-5}\ \mathrm{m^3\,s^{-1}},
\qquad \frac{Q'}{Q} = 1.0528,$$

a $+5.3\%$ error for omitting 47 s of tail at the far end of a 3600 s record.

## 9. The demonstration

[`code/groundwater_surface_water_demo.py`](./code/groundwater_surface_water_demo.py)
prints every number above in six labelled sections: the piezometer-pair flux with
its seasonal reversal; the homogeneous temperature response and the phase
symmetry; the layered-bed inversion with the admissible-velocity scan,
including a hypothetical inconsistent pair of readings; the
salt-dilution gauging; the resistivity signature; and the reconciliation table.
It is print-only, uses a fixed seed (`np.random.default_rng(20261014)`), needs no
network, and exits 0 in about two seconds.

## Exercises

Full sets with worked solutions are in
[`exercises/02-groundwater-surface-water-exercises.md`](./exercises/02-groundwater-surface-water-exercises.md) and
[`exercises/02-groundwater-surface-water-solutions.md`](./exercises/02-groundwater-surface-water-solutions.md). The three
tiers are ★ foundational, ★★ applied and ★★★ research-oriented; every problem is
answerable from this lesson and the demonstration that accompanies it.

## Mastery checkpoint

Without notes, using $\kappa = 1.0\times10^{-6}\ \mathrm{m^2\,s^{-1}}$,
$\omega = 7.272\times10^{-5}\ \mathrm{s^{-1}}$ and probes at 0.15 m and 0.30 m:

> **(a)** Compute the conductive skin depth and state whether the probe
> separation is well chosen. **(b)** A profile gives an amplitude ratio of 0.4048
> and a phase lag of 3.4542 h. Compute the seepage velocity from each and explain
> why they agree here. **(c)** The same reach gives a ratio of 0.3500 and a lag of
> 3.2000 h. Scan the two observables for the velocities they imply (the
> demonstration prints $-0.161$ m/d and $\pm0.578$ m/d) and state which
> conclusion is defensible.
> **(d)** A piezometer pair 8 m apart with $K = 2.5$ m/d reads a head difference
> of $+0.06$ m (stream above aquifer). Compute $q_z$ and the seepage velocity for
> $n_e = 0.25$, and say whether it agrees with (c). **(e)** Name the one
> assumption that, if wrong, would make both (a)–(d) wrong in the same direction.

The arithmetic is Section 8; (e) is Section 7.

## Common pitfalls

1. **Reporting a temperature-derived velocity without the sign convention or the
   phase/amplitude distinction.** The phase cannot give the direction.
2. **Assuming a homogeneous bed.** A silt layer produced an $+82\%$ velocity
   error in the demonstration, and an outright rejection by the phase.
3. **Choosing probe depths by convenience.** The separation must be comparable to
   the skin depth for the frequency used.
4. **Quoting a dilution discharge without its integration window.** A 47 s
   truncation cost 5.3%.
5. **Turning a resistivity contrast into a flux.** It is a state, and the
   saturation–salinity ambiguity of 14-05-01 applies.
6. **Mixing Darcy and seepage velocities.** They differ by $n_e$, which none of
   the four methods measured.
7. **Assuming a "disconnected" reach behaves like a connected one.** The
   time-dependence is different and the head difference alone becomes
   insufficient.

## Related modules

- [14-06-01 Integrated Catchment Characterisation](01-catchment-characterisation.md)
  — the catchment-scale budget the reach exchange feeds.
- [14-06-03 Water Resource Assessment and Sustainable Yield](03-water-resource-assessment.md)
  — the capture of streamflow by pumping, computed from the same geometry.
- [14-01-03 Hydraulic Head, Darcy's Law and Groundwater Flow](../01-hydrology-fundamentals/03-hydraulic-head-darcy.md)
  — the flow law used throughout.
- [14-05-01 Time-Lapse ERT for Infiltration and Transport](../05-hydrogeophysical-monitoring/01-time-lapse-ert.md)
  — the resistivity series reused in Section 5.
- [10-03 GPR Applications](../../10-gpr-near-surface/03-gpr-applications/README.md) —
  a complementary method for the shallow streambed.

## Self-assessment checklist

- [ ] I can compute a reach exchange flux and state its sign convention.
- [ ] I can derive the periodic temperature solution and the skin depth.
- [ ] I can explain why the phase gives $|v|$ and the amplitude the sign.
- [ ] I can invert both observables and read an inconsistency as model error.
- [ ] I can compute a dilution discharge and its window error.
- [ ] I can state what an ERT contrast does and does not say about the flux.
- [ ] I can fill in the reconciliation table for any reach I survey.
