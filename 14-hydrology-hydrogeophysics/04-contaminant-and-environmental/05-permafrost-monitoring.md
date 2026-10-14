---
id: 14-04-05
title: "Permafrost Monitoring with Geophysics"
level: research
prereqs: ["14-04-01", "14-03-02", "14-03-03", "04-05-02", "10-03-02"]
tags: [hydrology, hydrogeophysics, permafrost, active-layer, stefan-problem, resistivity, gassmann, monitoring, remote-sensing]
---

# Permafrost Monitoring with Geophysics

> **All models and data in this module are SYNTHETIC.** The soil properties,
> thermal conductivity, water content, pore-fluid conductivities and dry-frame
> moduli are chosen teaching values. The only standard constants used are the
> latent heat of fusion of water ($334\ \mathrm{kJ\,kg^{-1}}$), the bulk modulus
> and density of ice, and the moduli and densities of water and air.

Permafrost monitoring is the environmental geophysics problem with the largest
property contrast available — a phase change can raise the resistivity of a soil
by two orders of magnitude — and the most misleading interpretation, because the
quantity that matters to engineers and climate models is a *temperature* or an
*ice content*, and geophysics measures neither directly. What it measures is the
conductivity of the unfrozen water and the elastic properties of the
ice-cemented frame.

This lesson keeps the two chains separate. The **thermal chain** (Stefan problem)
predicts how deep the thaw front goes from a surface temperature history. The
**property chain** (Archie for conductivity, Gassmann plus a cementation bracket
for velocity) converts ice content into a measurement. And the **inverse
problem** — recovering ice content from a survey — is shown to be ambiguous in
a way that can be quantified and must be reported.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Stefan thaw-depth solution $X = \sqrt{2k\Delta T t/L_v}$ from
   an energy balance, and **verify** it against that balance numerically.
2. **State** the degree-day form and **explain** its single assumption and its
   failure mode.
3. **Compute** how the thaw depth scales with surface temperature, thermal
   conductivity and water content, and **explain** why two of the three are
   indistinguishable to a geophysical survey.
4. **Convert** an unfrozen water fraction to a bulk resistivity, and **state**
   the model assumptions.
5. **Apply** Gassmann fluid substitution with ice as the pore phase, and
   **explain** why it provides a lower bound rather than a prediction.
6. **Quantify** the cementation bracket that the fluid-substitution calculation
   omits, and **state** what calibration it requires.
7. **Design** a fixed-depth monitoring sensor as a binary crossing detector, and
   **compute** the depth resolution implied by the survey interval.
8. **Show** that the salinity confound moves both frozen and thawed resistivities
   together, and **state** what trade-off must then be reported.

## Prerequisites

- [14-04-01 Contaminant Plumes and Their Geophysical Signature](01-contaminant-plumes.md) —
  the property chain and the time-lapse argument.
- [14-03-02 Archie's Law and Saturation Estimation](../03-petrophysics-hydrology/02-archie-and-saturation.md) —
  the conductivity model used with the unfrozen fraction as $S_w$.
- [14-03-03 Seismic Velocity vs Saturation and Gassmann](../03-petrophysics-hydrology/03-seismic-velocity-saturation.md) —
  fluid substitution, the Wood/Hill limits and the dry-frame requirement.
- [04-05-02 Glacial Landforms](../../04-earth-science-geology/05-geomorphology-and-quaternary/02-glacial-landforms.md) —
  the ground ice and patterned ground this lesson monitors.
- [10-03-02 GPR Glaciology](../../10-gpr-near-surface/03-gpr-applications/02-gpr-glaciology.md) —
  the complementary method for ice-rich ground.

## 1. Intuition: a phase change with latent heat

Freezing a soil is not like cooling it. Water releases $334\
\mathrm{kJ\,kg^{-1}}$ when it turns to ice, which is enough to raise the
temperature of the same mass of water by $80\ \mathrm{K}$. Nearly all of the
energy budget of a freezing front therefore goes into the *latent* term, and that
single fact produces the characteristic $\sqrt{t}$ behaviour of the active layer:
the front advances quickly at first, when it is shallow and the thermal gradient
across it is steep, and then slows without limit.

Geophysics sees the phase change because the two phases are electrically and
elastically different. Ice is a solid with a very low electrical conductivity and
a bulk modulus of $9\ \mathrm{GPa}$, so the *unfrozen* water is the only
conducting phase in the pore space and the *frozen* pore content is a stiff
inclusion. The first effect is large and simple; the second is where the physics
becomes model-dependent.

## 2. The Stefan problem

**Derivation.** Let a freezing (or thawing) front be at depth $X(t)$ below a
surface held at a temperature $\Delta T$ colder (or warmer) than the phase
change. The heat flux conducted to the front is $q = k\Delta T/X$, so the energy
supplied per unit area over a time $\mathrm{d}t$ is
$k\Delta T\,\mathrm{d}t/X$. That energy is absorbed as latent heat,

$$
k\frac{\Delta T}{X}\,\mathrm{d}t = L_v\,\mathrm{d}X,
\qquad L_v \equiv \theta\,\rho_w\,L_f ,
$$

where $\theta$ is the volumetric water content and $L_f =
334\times10^{3}\ \mathrm{J\,kg^{-1}}$ is the latent heat of fusion of water.
Separating variables, $X\,\mathrm{d}X = (k\Delta T/L_v)\,\mathrm{d}t$, and
integrating from $X = 0$ at $t = 0$:

$$
\boxed{\;X(t) = \sqrt{\frac{2k\,\Delta T\,t}{L_v}}
= \sqrt{\frac{2k\,\Delta T\,t}{\theta\,\rho_w\,L_f}}\;}
$$

**Verification.** Substituting back, the *time-integrated* conducted energy per
unit area is $\int_0^t k\Delta T/X(\tau)\,\mathrm{d}\tau = 2k\Delta T t/X(t)$ —
the factor $2$ is the integral of $1/\sqrt{\tau}$ — and the latent energy absorbed
is $L_v X(t)$. The demonstration evaluates both for
$\Delta T = 10\ \mathrm{K}$, $t = 100$ days, $k = 2.0\
\mathrm{W\,m^{-1}\,K^{-1}}$, $\theta = 0.30$:

$$
L_v = 0.30\times1000\times334\times10^{3} = 1.0020\times10^{8}\
\mathrm{J\,m^{-3}},
$$

$$
X = \sqrt{\frac{2\times2.0\times10\times100\times86400}{1.0020\times10^{8}}}
= 1.8572\ \mathrm{m},
$$

and both energies come out as $1.8609\times10^{8}\ \mathrm{J\,m^{-2}}$, a ratio
of $1.0000000000$. **The balance closes exactly, which is the check that the
solution and the bookkeeping are the same statement.**

**Degree days.** Because the solution depends on $\Delta T$ and $t$ only through
their product, one can replace them by a single "thawing degree-day" sum:

$$
X = \sqrt{\frac{2k\,\mathrm{DDT}\times 86400}{L_v}} , \qquad
\mathrm{DDT} = \sum \Delta T_i\,\Delta t_i \ \ (\mathrm{K\,day}).
$$

The demonstration confirms the equivalence numerically: $100$ days at $10\
\mathrm{K}$ and $200$ days at $5\ \mathrm{K}$ both give $X = 1.857\ \mathrm{m}$
(degree-days of $1000$ in both cases). The method's assumption is that the
surface temperature history can be reduced to a sum, which fails when the
temperature passes through freezing repeatedly, when snow insulates transiently,
or when the soil is not at its water-holding capacity.

## 3. Worked example 1 — thaw depth and its scaling

**Problem.** Compute the thaw depth at 30, 60, 90, 120 and 200 days for the model
above, and compute the sensitivities to $\Delta T$, $k$ and $\theta$.

**Solution.** From $X = 1.8572\sqrt{t/100}$ (with $t$ in days):

| $t$ (days) | 30 | 60 | 90 | 120 | 200 |
|---|---|---|---|---|---|
| $X$ (m) | 1.017 | 1.439 | 1.762 | 2.034 | 2.626 |

The demonstration's sensitivity table:

| varied | values | $X$ at 100 days (m) |
|---|---|---|
| $\Delta T$ | 5, 10, 20 K | 1.313, 1.857, 2.626 |
| $\theta$ | 0.15, 0.30, 0.45 | 2.626, 1.857, 1.516 |
| $k$ | 1.0, 2.0, 4.0 $\mathrm{W\,m^{-1}\,K^{-1}}$ | 1.313, 1.857, 2.626 |

Two exact statements fall out of the formula: doubling $\Delta T$ multiplies $X$
by $\sqrt2 = 1.414$, and halving $\theta$ does the same. Quadrupling the season
length only doubles the thaw depth. **Because $X$ depends on $\Delta T$, $k$ and
$\theta$ only through their product in the numerator, a measured thaw-depth
change cannot be attributed to any one of them by the geophysics alone** — which
is the first honest limitation of the whole method.

## 4. Resistivity and the unfrozen water fraction

In frozen ground the conducting phase is the *unfrozen* water; the ice is part of
the matrix for electrical purposes. Archie's law therefore applies with
$S_w = $ the unfrozen fraction:

$$
\sigma_b = \frac{\phi^{m}S_w^{n}\sigma_w}{a}, \qquad
\rho_b = \frac{a}{\phi^{m}S_w^{n}\sigma_w} .
$$

With $\sigma_w = 0.050\ \mathrm{S\,m^{-1}}$ (i.e. $\rho_w = 20\
\Omega\,\mathrm{m}$), $\phi = 0.30$, $a = 1$, $m = n = 2$:

| unfrozen fraction | 1.00 | 0.50 | 0.20 | 0.10 | 0.05 | 0.02 |
|---|---|---|---|---|---|---|
| $\rho_b$ ($\Omega$ m) | 222.2 | 888.9 | 5555.6 | 22 222.2 | 88 888.9 | 555 555.6 |
| ratio to thawed | 1.0 | 4.0 | 25.0 | 100.0 | 400.0 | 2500.0 |

A reduction of the unfrozen fraction from $1.00$ to $0.10$ raises the bulk
resistivity by a factor of **100**. That is the reason resistivity is the
workhorse of permafrost monitoring: the contrast is enormous, and it is monotone
in the quantity that thermal models need — the unfrozen water content, not the
temperature.

Note the model limitation, which must be stated every time: the ice fraction
enters *only* through $S_w$, so the relation cannot distinguish "less unfrozen
water because it is colder" from "less unfrozen water because the total water
content is lower". A survey measures $S_w$, not ice content, without an
independent porosity or total-water measurement.

## 5. Velocity: what Gassmann explains and what it does not

The temptation is to treat ice as a pore fluid and apply Gassmann fluid
substitution. The demonstration does exactly that for a synthetic soil with
$\phi = 0.30$, $K_\text{dry} = 5.0\ \mathrm{GPa}$, $\mu_\text{dry} = 4.0\
\mathrm{GPa}$:

| pore phase | $K_\text{sat}$ (GPa) | $\rho$ ($\mathrm{kg\,m^{-3}}$) | $V_p$ (km/s) | $V_s$ (km/s) |
|---|---|---|---|---|
| air | 5.0002 | 1855.4 | 2.3600 | 1.4683 |
| water | 9.8800 | 2155.0 | 2.6570 | 1.3624 |
| ice | 20.1577 | 2130.1 | 3.4593 | 1.3703 |

The predicted water-to-ice velocity shift is $802.4\ \mathrm{m\,s^{-1}}$, and it
is a **lower bound**: Gassmann treats the pore phase as a fluid and sets
$\mu_\text{sat} = \mu_\text{dry}$, so it cannot see the *cementation* that ice
actually provides when it grows between grains. The demonstration prints an
illustrative bracket in which $\mu$ rises on freezing by factors of one, two and
four:

| $\mu$ on freezing (GPa) | 4.0 | 8.0 | 16.0 |
|---|---|---|---|
| $V_p$ (ice) (km/s) | 3.4593 | 3.8041 | 4.4134 |
| $V_s$ (ice) (km/s) | 1.3703 | 1.9380 | 2.7407 |

The spread is larger than the fluid-substitution effect itself, and it is
controlled by a coefficient — the cementation factor — that must be calibrated
from local data. **A velocity-derived ice content is therefore a bracket, never a
number.** The useful measurement is $V_s$, because it is the quantity that
responds to cementation and is nearly independent of the pore fluid's modulus;
a $V_p$-only interpretation cannot separate ice content from frame stiffness.

## 6. Monitoring design: a fixed sensor is a crossing detector

Consider a seasonal cycle with $\Delta T = 12\ \mathrm{K}$ over $120$ days, which
gives a maximum thaw depth of $2.229\ \mathrm{m}$, and a sensor at $2.0\
\mathrm{m}$:

| day | $X$ (m) | state at 2.0 m | $\rho$ at the sensor ($\Omega$ m) |
|---|---|---|---|
| 60 | 1.576 | frozen | 22 222.2 |
| 90 | 1.930 | frozen | 22 222.2 |
| 100 | 2.034 | thawed | 222.2 |
| 120 | 2.229 | thawed | 222.2 |

The front reaches $2.0\ \mathrm{m}$ at $t = 96.6$ days (by inverting
$X(t) = 2.0\ \mathrm{m}$). The front moves at
$\mathrm{d}X/\mathrm{d}t = X/(2t) = 0.01035\ \mathrm{m\,day^{-1}}$ there, so a
weekly survey dates the crossing to about $7.2\ \mathrm{cm}$ — $3.6\%$ of the
sensor depth — and the resistivity flip is a factor of $100$, far above any
survey noise.

The honest reading is that **a fixed sensor is a precise but binary
instrument**: it dates the crossing of a known depth, and it does not profile the
profile. A thaw-depth curve requires either an array of sensors at several depths
or a tomographic inversion with its own resolution analysis, and the two give
different errors that must not be conflated.

## 7. The salinity confound

The frozen/thawed resistivity ratio in this model is exactly $S_w^{-n} = 100$,
**independent of the pore-fluid conductivity**:

| $\sigma_w$ ($\mathrm{S\,m^{-1}}$) | 0.05 | 0.20 | 0.50 | 1.00 |
|---|---|---|---|---|
| $\rho$ frozen ($\Omega$ m) | 22 222.2 | 5555.6 | 2222.2 | 1111.1 |
| $\rho$ thawed ($\Omega$ m) | 222.2 | 55.6 | 22.2 | 11.1 |
| ratio | 100.00 | 100.00 | 100.00 | 100.00 |

So salinity does *not* destroy the frozen/thawed contrast; it translates both
resistivities by the same factor. That is a genuinely useful result: a monitoring
programme that tracks the *ratio* at a fixed site is robust to a changing
salinisation. What salinity does destroy is the ability to separate unfrozen
water content from salinity in a *single* survey, because a brackish, partly
frozen layer and a fresher, more thawed layer have the same resistivity. Report
the two as a trade-off; do not choose.

## 8. Assumptions and regime of validity

**Thermal.** (i) A single moving front with a step surface temperature: no
multi-year thermal memory, no snow-cover insolation, no latent-heat release from
a finite temperature interval. (ii) Constant and uniform $k$, $\theta$ and
$\rho$: in reality the thermal conductivity of frozen ground is roughly twice
that of thawed ground, which changes the effective $k$ as the front passes.
(iii) No advective heat transport by groundwater, which dominates in coarse,
permeable substrates and makes the active layer far deeper than Stefan predicts.

**Property.** (i) The unfrozen water content is the only conducting phase and it
has the stated $\sigma_w$; in a clay-rich soil there is also surface conduction
(Archie fails). (ii) $\phi$ and $m$ are known and uniform; a $10\%$ porosity error
is a $21\%$ resistivity error at $m = 2$. (iii) Ice is an insulator, which is an
excellent approximation below a few tens of hertz but degrades at high frequency
and near the freezing point, where a liquid-like premelted film makes the ice
weakly conducting.

**Elastic.** (i) Gassmann's own assumptions (isotropic, homogeneous,
low-frequency, known dry frame), all of which are strained by a partially frozen
soil. (ii) The cementation bracket is illustrative; a real calibration measures
$V_p$ and $V_s$ in frozen and thawed states on representative samples at the
*seismic* frequency band, not the ultrasonic one.

## 9. Python demonstration

[`code/permafrost_monitoring_demo.py`](./code/permafrost_monitoring_demo.py)
prints the Stefan solution with the energy-balance check, the time and degree-day
tables, the three sensitivity blocks, the resistivity-versus-unfrozen-fraction
table, the fluid-substitution and cementation-bracket velocity tables, the
monitoring scenario with its crossing date and depth resolution, and the salinity
table.

```bash
cd 14-hydrology-hydrogeophysics/04-contaminant-and-environmental/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python permafrost_monitoring_demo.py
```

## 10. Exercises

Graded problems are in
[`exercises/05-permafrost-monitoring-exercises.md`](./exercises/05-permafrost-monitoring-exercises.md)
with worked solutions in
[`exercises/05-permafrost-monitoring-solutions.md`](./exercises/05-permafrost-monitoring-solutions.md).

## Mastery checkpoint

Answer without notes.

> **(a)** Derive the Stefan solution and state the energy balance that verifies
> it. **(b)** Compute the thaw depth for $\Delta T = 8\ \mathrm{K}$, $90$ days,
> $k = 1.5\ \mathrm{W\,m^{-1}\,K^{-1}}$, $\theta = 0.35$. **(c)** By what factor
> does the depth change if the water content doubles, and why is that bad news
> for attributing a depth change to warming? **(d)** With $\phi = 0.30$,
> $m = n = 2$ and $\rho_w = 25\ \Omega\,\mathrm{m}$, compute the bulk resistivity
> at unfrozen fractions of $1.0$ and $0.10$. **(e)** Explain why Gassmann's
> ice-substitution answer is a lower bound, and state the measurement that
> constrains the missing term. **(f)** A site's pore water becomes twice as
> saline. State what happens to the frozen/thawed resistivity ratio and what
> happens to a single-survey interpretation, and how you would report it.

## Common pitfalls

1. **Attributing a thaw-depth change to warming.** $\Delta T$, $k$ and $\theta$
   are not separable by geophysics.
2. **Reporting ice content from $S_w$.** The survey measures the unfrozen
   fraction of the pore water, not the total ice.
3. **Using Gassmann's ice substitution as a prediction.** It is a lower bound;
   cementation dominates in ice-rich ground.
4. **Calibrating cementation at ultrasonic frequency and applying it to seismic
   data.** The dispersive regime differs.
5. **Ignoring surface conduction in clay-rich frozen ground.** Archie fails
   exactly where permafrost is often silty.
6. **Treating a fixed sensor as a profiler.** It is a crossing detector.
7. **Choosing between ice content and salinity instead of reporting the
   trade-off.** Both fit one resistivity.

## Related modules

- [01 Contaminant Plumes and Their Geophysical Signature](01-contaminant-plumes.md).
- [03 Seawater Intrusion and Coastal Aquifer Monitoring](03-saline-intrusion.md) —
  the salinity end of the same ambiguity.
- [04 Acid Mine Drainage and Mining Environmental Geophysics](04-acid-mine-drainage.md).
- [Module 14-03 Petrophysical Relations for Saturated Media](../03-petrophysics-hydrology/README.md) —
  Archie and Gassmann in full.
- [Module 14-05 Time-Lapse and Monitoring Hydrogeophysics](../05-hydrogeophysical-monitoring/README.md) —
  the differencing and repeatability discipline this lesson assumes.
- [10-03-02 GPR Glaciology](../../10-gpr-near-surface/03-gpr-applications/02-gpr-glaciology.md) —
  the complementary radar method for ice-rich ground.
- [Module 16-atmosphere-climate](../../16-atmosphere-climate/README.md) —
  the surface-temperature forcing that drives the Stefan solution.
