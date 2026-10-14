---
id: 14-04-01
title: "Contaminant Plumes and Their Geophysical Signature"
level: doctoral
prereqs: ["14-01-03", "14-01-05", "14-03-02", "09-02-05"]
tags: [hydrology, hydrogeophysics, contaminant, plume, advection-dispersion, retardation, tracer, time-lapse]
---

# Contaminant Plumes and Their Geophysical Signature

> **All models and data in this module are SYNTHETIC.** The tracer in this lesson
> is a generic, idealised ionic solute described in arbitrary concentration units
> (CU). No real contaminant, site, spill, licence or regulated threshold is used
> or implied anywhere in this module.

A geophysical survey never detects a contaminant. It detects a *bulk property* —
electrical conductivity, permittivity, density, elastic modulus — and the
contaminant is inferred from the property change. This lesson makes that chain
explicit and then attacks it: the transport model that predicts where the
contaminant is, the petrophysical model that converts its concentration into a
property change, the survey model that converts the property change into a
measurement, and the noise level that decides whether the measurement means
anything.

The result is a set of three numerically separate statements, and conflating them
is the central error of the subject. "The plume is 140 m long" is a transport
result. "The plume lowers the resistivity by a factor of three" is a
petrophysical result. "The anomaly is detectable above 2% noise" is a
measurement result. Each has its own assumptions and its own error, and only the
first is about the contaminant.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the one-dimensional advection–dispersion equation from a mass
   balance, and **state** the meaning and units of $v$, $D$, $\alpha_L$ and $R$.
2. **Compute** the retardation factor from a distribution coefficient and a bulk
   density, and **explain** why it delays every arrival time by the same factor.
3. **Evaluate** the step-release solution and **extract** the front position and
   the 10–90% transition width, and **state** how each scales with time.
4. **Convert** a tracer concentration to a pore-fluid conductivity, then to a
   bulk resistivity, and **state** each model assumption in the chain.
5. **Compute** a detection threshold from a stated measurement noise, and
   **explain** why the threshold scales with the background conductivity.
6. **Distinguish** a static interpretation from a time-lapse one, and **justify**
   which the survey design should target.
7. **List** the physical mechanisms that produce a conductive anomaly without a
   contaminant, and **name** the independent constraint that separates each.

## Prerequisites

- [14-01-03 Hydraulic Head, Darcy's Law and Groundwater Flow](../01-hydrology-fundamentals/03-hydraulic-head-darcy.md) —
  the velocity field the plume is advected by.
- [14-01-05 Groundwater Chemistry and Salinity](../01-hydrology-fundamentals/05-groundwater-chemistry.md) —
  total dissolved solids and the conductivity of natural waters.
- [14-03-02 Archie's Law and Saturation Estimation](../03-petrophysics-hydrology/02-archie-and-saturation.md) —
  the pore-fluid-to-bulk conductivity conversion used in Section 6.
- [09-02-05 ERT Tomography](../../09-electrical-em-methods/02-dc-resistivity/05-ert-tomography.md) —
  the measurement that produces the resistivity distribution.

## 1. Intuition: three separate models, in a chain

Every contaminant-geophysics interpretation is a composition of three models.

$$
\underbrace{C(\mathbf x, t)}_{\text{transport}}
\;\xrightarrow{\text{petrophysics}}\;
\underbrace{\sigma(\mathbf x)}_{\text{property}}
\;\xrightarrow{\text{survey}}\;
\underbrace{d}_{\text{data}} .
$$

The chain is read right-to-left in practice: measure $d$, invert to $\sigma$,
invert to $C$. Both inversions are non-unique, and the errors multiply. A
practitioner who reports a concentration map from an ERT section has quietly
assumed a transport model, a mixing law, a porosity, a clay content and a
saturation — and the last two of those are usually not measured at all.

The saving grace is that the *archetypal* signatures are large. A saline or ionic
solute changes the pore-fluid conductivity by orders of magnitude, and that
contrast is independent of the rock. A non-aqueous liquid phase changes
resistivity, permittivity and density in a quite different combination, which is
why multi-method surveys work: each method sees a different term of the same
change.

## 2. Definitions and the transport model

**Concentration** $C$ (this module uses arbitrary CU; the physics is unchanged
for $\mathrm{mg\,L^{-1}}$ or $\mathrm{mol\,m^{-3}}$).

**Seepage velocity** $v$ ($\mathrm{m\,day^{-1}}$): the mean velocity of the water
in the pores, related to the Darcy flux $q$ by $v = q/\theta$ with $\theta$ the
effective (mobile) porosity.

**Longitudinal dispersivity** $\alpha_L$ (m): a length scale of the pore-scale
mixing, so that the mechanical dispersion coefficient is

$$
D = \alpha_L v + D^{*}, \qquad D \approx \alpha_L v \ \text{ in an aquifer},
$$

with $D^{*}$ the molecular diffusion coefficient (usually negligible away from
the source and in the transverse direction).

**Retardation factor.** For a solute that partitions onto the solid phase with a
distribution coefficient $K_d$,

$$
R = 1 + \frac{\rho_b K_d}{\theta}, \qquad
v_\text{solute} = \frac{v}{R}.
$$

$R$ appears as a divisor on every velocity, so **every arrival time is multiplied
by $R$**. Retardation delays; it does not spread, and it does not remove mass.

**Transport equation.** Conservation of solute mass in a one-dimensional column
with no source gives

$$
\frac{\partial C}{\partial t} + \frac{v}{R}\frac{\partial C}{\partial x}
= \frac{D}{R}\frac{\partial^{2}C}{\partial x^{2}} .
$$

## 3. Derivation of the transport equation and its solution

**Mass balance.** In a slice of thickness $\delta x$ and unit cross-section the
flux is $qC - D\theta\,\partial C/\partial x$ (advective plus dispersive), and the
solute mass per unit volume is $\theta C + \rho_b C_s$ with
$C_s = K_d C$. Dividing the conservation statement
$\partial(\theta C + \rho_b K_d C)/\partial t = -\partial(\text{flux})/\partial x$
by $\theta$ gives the equation in Section 2, with $R$ dividing both transport
terms and $D = \alpha_L v$.

**Step-release solution.** For a semi-infinite column at $C = 0$ with $C = C_0$
imposed at $x = 0$ from $t = 0$ onward, the solution is the Ogata–Banks form

$$
C(x,t) = \frac{C_0}{2}\left[
\operatorname{erfc}\!\left(\frac{x - v_s t}{2\sqrt{D_s t}}\right)
+ \exp\!\left(\frac{v_s x}{D_s}\right)
\operatorname{erfc}\!\left(\frac{x + v_s t}{2\sqrt{D_s t}}\right)\right],
$$

with $v_s = v/R$ and $D_s = D/R$. For all but the earliest times the second term
is negligible and the profile is a single complementary error function, i.e. a
smoothed step whose centre advects at $v_s$ and whose width grows as $\sqrt t$.

**Front and width.** The 50% point is at $x_f = v_s t$. A complementary error
function profile has its 10% and 90% points at $\mp 1.2816$ standard deviations
of the equivalent normal, so

$$
w_{10\text{–}90} = 2.563\,\sqrt{2 D_s t} .
$$

## 4. The archetypal signature: what a tracer changes

Geophysical methods respond to different terms of the same physical change:

| Change | Term affected | Typical method |
|---|---|---|
| ionic solute raises pore-fluid conductivity | bulk electrical conductivity | ERT, EM induction, TDEM |
| non-aqueous liquid replaces water | conductivity down, permittivity up or down, density down | ERT + GPR |
| temperature change | conductivity and density | ERT + distributed temperature |
| gas generation replaces water | saturation, so resistivity up and velocity down | ERT + seismic |
| redox front at the plume edge | streaming and electrochemical potential | self-potential |

The **ionic-solute** case is the archetype used in this lesson because it is the
simplest chain with the largest and most transferable contrast. The others are
treated in the following lessons as their own archetypes, because a
resistivity-only survey confuses them all.

## 5. Worked example 1 — front position and transition width

**Problem.** A synthetic aquifer has $v = 0.050\ \mathrm{m\,day^{-1}}$,
$\theta = 0.30$, $\rho_b = 1855\ \mathrm{kg\,m^{-3}}$ (i.e. a grain density of
$2650\ \mathrm{kg\,m^{-3}}$ at $\theta = 0.30$),
$K_d = 0.05\ \mathrm{mL\,g^{-1}}$ and $\alpha_L = 1.0\ \mathrm{m}$. Compute $R$,
the solute velocity, $D$, the front position at 3650 days and the 10–90% width
then.

**Solution.**

$$
R = 1 + \frac{\rho_b K_d}{\theta}
= 1 + \frac{1.855 \times 0.05}{0.30} = 1 + 0.3092 = 1.3092 .
$$

(With $\rho_b$ converted to $1.855\ \mathrm{g\,cm^{-3}}$, the product
$\rho_b K_d$ has units of $\mathrm{cm^{3}}$ per $\mathrm{cm^{3}}$, i.e. it is
dimensionless before dividing by $\theta$ — the units check that $K_d$ must be in
$\mathrm{mL\,g^{-1}}$ when $\rho_b$ is in $\mathrm{g\,cm^{-3}}$.)

$$
v_s = \frac{v}{R} = \frac{0.050}{1.3092} = 0.0382\ \mathrm{m\,day^{-1}},
$$

$$
D_s = \frac{\alpha_L v}{R} = \frac{1.0\times0.050}{1.3092}
= 0.03819\ \mathrm{m^{2}\,day^{-1}}.
$$

At $t = 3650$ days (10.0 years):

$$
x_f = v_s t = 0.0382\times3650 = 139.4\ \mathrm{m},
$$

$$
w_{10\text{–}90} = 2.563\sqrt{2\times0.03819\times3650}
= 2.563\times16.70 = 42.8\ \mathrm{m}.
$$

All four numbers are printed by
[`code/contaminant_plumes_demo.py`](./code/contaminant_plumes_demo.py). Note what
the widths do: $13.5\ \mathrm{m}$ at 1 year, $23.4\ \mathrm{m}$ at 3 years,
$42.8\ \mathrm{m}$ at 10 years — a $\sqrt t$ growth against a linear front, so
the *relative* sharpness improves with age. A young plume is wide compared with
its travel distance ($13.5\ \mathrm{m}$ of transition after $13.9\ \mathrm{m}$ of
travel); an old one is sharp (43 m after 139 m).

## 6. Worked example 2 — from concentration to anomaly

**Problem.** Using the synthetic linear model
$\sigma_w = 0.050 + 1.0\times10^{-4}C\ \mathrm{S\,m^{-1}}$ (with $C$ in CU) and
Archie with $a = 1$, $m = 2$, $S_w = 1$, $\phi = 0.30$, compute the bulk
resistivity at $C = 0$, at $C = 1000$ CU, and at the source concentration. State
each assumption.

**Solution.** The bulk conductivity is
$\sigma_b = \phi^{m}\sigma_w/a = 0.09\,\sigma_w$, and $\rho_b = 1/\sigma_b$.

| $C$ (CU) | $\sigma_w$ ($\mathrm{S\,m^{-1}}$) | $\sigma_b$ ($\mathrm{S\,m^{-1}}$) | $\rho_b$ ($\Omega\,\mathrm{m}$) |
|---|---|---|---|
| 0 | 0.0500 | 0.004500 | 222.22 |
| 50 | 0.0550 | 0.004950 | 202.02 |
| 100 | 0.0600 | 0.005400 | 185.19 |
| 250 | 0.0750 | 0.006750 | 148.15 |
| 500 | 0.1000 | 0.009000 | 111.11 |
| 1000 | 0.1500 | 0.013500 | 74.07 |

So the plume lowers the bulk resistivity from $222.2$ to $74.1\
\Omega\,\mathrm{m}$ — **a factor of 3.00**.

**The assumptions, in the order they matter.** (i) The rock is clay-free, so
there is no parallel conduction path (lesson 02 §8). (ii) $\phi = 0.30$ is known
and constant; a $\pm 0.01$ error moves $\sigma_b$ by $\mp 7\%$. (iii) The rock is
fully saturated. (iv) The concentration-to-conductivity relation is linear with
a stated slope; real relations are non-linear, temperature-dependent and
ion-specific. Every one of these is a model choice, and none of them is measured
by the resistivity survey.

## 7. Detection: the smallest change the noise allows

The measured quantity is the apparent resistivity, with a stated repeatability.
The demonstration takes $2\%$ (one sigma) and computes the smallest concentration
that moves the bulk resistivity by one and two sigma. Since
$\rho_b \propto 1/\sigma_w$ and the background is $\sigma_{w0} = 0.050\
\mathrm{S\,m^{-1}}$:

$$
\frac{\Delta\rho}{\rho} = \frac{\Delta\sigma_w}{\sigma_w}
= \frac{\beta C}{\sigma_{w0} + \beta C}
\;\;\Longrightarrow\;\;
C_\text{min} = \frac{\varepsilon\,\sigma_{w0}}{\beta(1-\varepsilon)},
\quad \varepsilon = \frac{\Delta\rho}{\rho} .
$$

With $\beta = 1.0\times10^{-4}\ \mathrm{S\,m^{-1}}$ per CU:

| threshold | $\Delta\rho/\rho$ | required $\Delta\sigma_w/\sigma_w$ | $C_\text{min}$ | fraction of source |
|---|---|---|---|---|
| 1 sigma | 0.020 | 2.0% | 10.2 CU | 1.02% |
| 2 sigma | 0.040 | 4.0% | 20.8 CU | 2.08% |

**Two consequences that generalise.**

1. The detectable concentration is proportional to the *background*
   conductivity. In a fresh aquifer ($\sigma_{w0}$ small) the method sees a tiny
   tracer concentration; in a brackish one it is blind until the tracer dominates.
   This is the single most useful rule for screening a site for feasibility.
2. The threshold is a *concentration*, not a mass. A small plume of a strong
   electrolyte and a large plume of a weak one can be equally visible, and
   equally invisible, so the detection map is not a mass map.

## 8. Time-lapse as the estimator, not the static image

The demonstration's last table follows one sensor at $x = 50\ \mathrm{m}$:

| $t$ (days) | $C$ (CU) | $\rho$ ($\Omega\,\mathrm{m}$) | change |
|---|---|---|---|
| 365 | 0.0 | 222.22 | $-0.00\%$ |
| 1095 | 211.9 | 156.07 | $-29.77\%$ |
| 1825 | 962.1 | 75.99 | $-65.80\%$ |
| 2555 | 999.8 | 74.08 | $-66.66\%$ |
| 3650 | 1000.0 | 74.07 | $-66.67\%$ |

The front reaches the sensor at $t = 50/v_s = 1309$ days. Before that the signal
is **absent, not small** — and this is precisely why time-lapse acquisition is
the right design and why the *schedule* matters as much as the array. A
monitoring network that samples only after arrival cannot constrain $v_s$; the
only part of the record that contains information about the transport parameters
is the rising limb between 1095 and 1825 days.

Differencing two surveys also removes every static error — array geometry,
electrode position, background geology — while the random component adds in
quadrature, a $41\%$ penalty on noise for a large gain in systematic error
elimination. The quantitative test is the ratio of systematic to random error in
a single survey: differencing wins when that ratio exceeds $\sqrt{2}$.

## 9. Assumptions and regime of validity

**Transport.** (i) One-dimensional, uniform, steady flow; the seepage velocity
must be known *independently* of the plume. (ii) Constant $\alpha_L$; real
dispersivity grows with travel distance because it averages over heterogeneities,
so a plume that has crossed scale boundaries is not fitted by a single $\alpha_L$.
(iii) Local equilibrium sorption with a linear isotherm; a rate-limited or
non-linear isotherm changes the shape, not just the speed. (iv) No degradation,
no density-driven flow, no multiphase flow — a dense non-aqueous liquid phase
sinks, a light one floats, and neither obeys this equation. (v) A step release;
a finite-duration release superimposes two steps and, for short releases, never
reaches $C_0$.

**Petrophysics.** As Section 6: a clean matrix, a known and uniform porosity,
full saturation, and a stated concentration-to-conductivity relation.

**Measurement.** The bulk resistivity must be inverted from apparent resistivity
with a model; the inversion's smoothness means a sharp plume edge is smeared, and
the width after inversion is not comparable with $w_{10\text{–}90}$ without a
resolution analysis.

## 10. Non-uniqueness: what else makes a conductive anomaly

| mechanism | size of the bulk resistivity change | independent constraint |
|---|---|---|
| clay-rich rock with fresh water | $2$–$3\times$ lower | natural gamma, cation exchange capacity, NMR bound fluid |
| brackish water intrusion | up to $80\times$ lower | coastal setting; fluid samples |
| metallic conductor (a body, not a solute) | orders of magnitude | very low resistivity with a strong induced-polarisation phase |
| increased water saturation | $2$–$3\times$ lower | sampling shows no change in pore-fluid conductivity |
| higher porosity | $1.5$–$2\times$ lower | an independent porosity measurement |

The last two rows are the ones that matter in practice. A measured resistivity is
a statement about the **product** $\phi^{m}\sigma_w$; every mechanism that raises
either factor produces the same observation, and the transport model is only one
of five. An environmental interpretation must name at least one independent
constraint, or it is a hypothesis dressed as a measurement.

## 11. Python demonstration

[`code/contaminant_plumes_demo.py`](./code/contaminant_plumes_demo.py) prints the
transport parameters and $R$, profiles at three times, the front and width
scaling, the retardation table, the conductivity and resistivity conversion, the
detection thresholds, the time-lapse table and the reference numbers used above.

```bash
cd 14-hydrology-hydrogeophysics/04-contaminant-and-environmental/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python contaminant_plumes_demo.py
```

## 12. Exercises

Graded problems are in
[`exercises/01-contaminant-plumes-exercises.md`](./exercises/01-contaminant-plumes-exercises.md)
with worked solutions in
[`exercises/01-contaminant-plumes-solutions.md`](./exercises/01-contaminant-plumes-solutions.md).

## Mastery checkpoint

Answer without notes.

> An idealised ionic tracer enters a synthetic aquifer with
> $\theta = 0.30$, $\rho_b = 1855\ \mathrm{kg\,m^{-3}}$,
> $v = 0.050\ \mathrm{m\,day^{-1}}$, $\alpha_L = 1.0\ \mathrm{m}$ and
> $K_d = 0.20\ \mathrm{mL\,g^{-1}}$. **(a)** Compute $R$ and the solute velocity.
> **(b)** Compute the front position and the 10–90% width after 3 years, and say
> which of them grew faster. **(c)** The pore fluid has
> $\sigma_{w0} = 0.05\ \mathrm{S\,m^{-1}}$ at the background and the tracer adds
> $1.0\times10^{-4}\ \mathrm{S\,m^{-1}}$ per CU; with $\phi = 0.30$, $m = 2$,
> compute the bulk resistivity at the background and at $C = 500$ CU.
> **(d)** With a $2\%$ one-sigma survey noise, compute the detection threshold and
> explain why it changes if the background is ten times more conductive.
> **(e)** Name two mechanisms other than the tracer that would produce the same
> resistivity drop, and the measurement that distinguishes each.

## Common pitfalls

1. **Reporting a concentration from a resistivity without the chain.** Write the
   three models out; if you cannot, you have not made a measurement.
2. **Using the Darcy flux as the seepage velocity.** They differ by $\theta$.
3. **Forgetting $R$ in the arrival time.** Retardation multiplies every time by
   the same factor, and it is easy to fit $v$ when you have actually fitted
   $v/R$.
4. **Assuming a constant dispersivity over a long travel distance.** Real
   dispersivity grows with scale, so a single $\alpha_L$ fits one plume length.
5. **Comparing an inverted, smoothed plume edge with a modelled sharp one.** The
   inversion sets its own length scale.
6. **Sampling only after the front has arrived.** The information is in the
   rising limb.
7. **Forgetting that the detection threshold scales with the background
   conductivity.** A feasibility screen must use the site's own background.

## Related modules

- [02 Landfill Investigation and Leachate Mapping](02-landfill-investigation.md) —
  the same chain with a different anatomy and a layered-earth forward model.
- [03 Seawater Intrusion and Coastal Aquifer Monitoring](03-saline-intrusion.md) —
  the largest-contrast case, and the density-driven physics that transport alone
  misses.
- [04 Acid Mine Drainage and Mining Environmental Geophysics](04-acid-mine-drainage.md) —
  where the tracer is generated by a reaction rather than released.
- [05 Permafrost Monitoring with Geophysics](05-permafrost-monitoring.md) — a
  phase change rather than a solute.
- [Module 14-05 Time-Lapse and Monitoring Hydrogeophysics](../05-hydrogeophysical-monitoring/README.md) —
  the systematic treatment of differencing and repeatability.
- [Module 09-02 DC Resistivity and ERT](../../09-electrical-em-methods/02-dc-resistivity/README.md) —
  the acquisition and inversion whose resolution limits Section 9 refers to.
