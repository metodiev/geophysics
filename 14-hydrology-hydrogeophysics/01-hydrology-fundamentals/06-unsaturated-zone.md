---
id: 14-01-06
title: "The Unsaturated Zone, Infiltration and Soil Moisture"
level: advanced
prereqs: ["14-01-03", "14-01-02", "02-06-05"]
tags: [hydrology, hydrogeophysics, unsaturated-zone, infiltration, soil-moisture, richards-equation, gpr, van-genuchten]
---

# The Unsaturated Zone, Infiltration and Soil Moisture

Between the ground surface and the water table, water is held at *negative*
pressure by capillarity, and the hydraulic conductivity falls by orders of
magnitude within a metre. This is the **unsaturated zone** (the vadose zone), and
it is where recharge is created, where contaminants are delayed, and where
geophysics — chiefly GPR and time-lapse ERT — measures water content directly
rather than inferring it.

The physics is harder than in the saturated zone in one specific way: the
conductivity is a **function of the state** you are solving for. Darcy's law
survives, but the flow equation becomes nonlinear, and every quantity in it is a
constitutive relation (a *retention curve* and a *conductivity function*) rather
than a constant. This lesson builds both, applies them to infiltration, and
verifies a numerical solution against a water budget.

**All models and data in this module are SYNTHETIC.** The soil, its retention
parameters, the wetting-front suction and the rainfall rates below are invented
teaching values. Physical constants and model end members are stated with units
where used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** water content from pressure head with the van Genuchten retention
   curve and **invert** it, and **state** the meaning of each parameter.
2. **Compute** unsaturated conductivity with the Mualem relation and **quantify**
   its collapse — orders of magnitude over one metre of suction.
3. **Compute** field capacity, wilting point and available water capacity, and
   **explain** why the first two are conventions rather than soil constants.
4. **Apply** the Green–Ampt model to ponded infiltration, **derive** the ponding
   time for a rainfall rate, and locate the transition at $r = K_s$.
5. **Solve** the Richards equation numerically under a rainfall flux and
   **verify** the solution with a water budget that closes to round-off.
6. **Compare** a diffuse-front numerical solution with a sharp-front
   approximation and **quantify** the definitional difference between two
   definitions of "the front".
7. **Convert** water content to permittivity with a mixing model, **compute** a
   GPR velocity, and **quantify** the sensitivity of the inversion to the assumed
   porosity.

## Prerequisites

- [14-01-03 Hydraulic Head, Darcy's Law and Groundwater Flow](03-hydraulic-head-darcy.md)
  — Darcy's law, head, and the saturated flow equation.
- [14-01-02 Aquifers, Porosity, Permeability and Storativity](02-aquifer-types-and-properties.md)
  — porosity, effective porosity and specific yield, all of which have an
  unsaturated counterpart here.
- [02-06-05 Flow in Porous Media](../../02-physics/06-fluid-mechanics/05-porous-media-flow.md)
  — the viscous-flow origin of Darcy's law, which continues to hold here.

---

## 1. Intuition: a conductivity that depends on the answer

Above the water table the pore water is under suction. Three consequences follow,
and they are the whole lesson:

1. **Pressure head is negative.** $h < 0$, measured in metres of water, and it is
   the suction that holds water against gravity. It is also why the head formula
   of [03](03-hydraulic-head-darcy.md) still gives a number above the water table
   but that number is not a potential for regional flow.
2. **Water fills only part of the pore space.** The water content $\theta$
   (volume of water per unit bulk volume) is less than the porosity $n$, and the
   remainder is air at (nearly) atmospheric pressure.
3. **Conductivity collapses.** Water moves only through the water-filled pores, and
   in a fine pore the film is thin, so $K$ falls by **orders of magnitude** within
   a metre of suction. In the synthetic soil below, $K$ spans
   $10^{-5}$ to $10^{-15}\ \mathrm{m\,s^{-1}}$ as $\theta$ falls from 0.42 to 0.07.

The third point is why the unsaturated zone controls recharge timing: near the
surface, wet soil conducts; dry soil does not, so the wetting front advances
slowly and most rainfall events are absorbed without reaching the water table.

## 2. Defining the two constitutive relations

### 2.1 The retention curve

The **van Genuchten** form gives water content as a function of pressure head
$h \le 0$:

$$\theta(h) = \theta_r + \frac{\theta_s - \theta_r}
{\left[1 + (\alpha \lvert h\rvert)^{n}\right]^{m}},
\qquad m = 1 - \frac{1}{n},$$

with $\theta_s$ the saturated water content ($= n$ if the soil is air-free at
saturation), $\theta_r$ a residual content at which liquid water ceases to be
connected, $\alpha$ [m$^{-1}$] a scale that sets the air-entry suction
($\lvert h_{\text{ae}}\rvert \sim 1/\alpha$) and $n$ a shape parameter.

Note that $\theta_r$ is a **model parameter, not a measurement**: no soil has a
discrete residual content, and $K \to 0$ continuously. $\theta_r$ exists so that
the closed form can represent a curve that flattens.

**Synthetic soil:** $\theta_s = 0.42$, $\theta_r = 0.06$, $\alpha = 3.0\
\mathrm{m^{-1}}$, $n = 1.6$ (so $m = 0.375$), $K_s = 1.0 \times 10^{-5}\
\mathrm{m\,s^{-1}} = 36\ \mathrm{mm\,h^{-1}}$.

| $h$ (m) | $h$ (kPa) | $\theta$ | effective saturation $S_e$ |
|---|---|---|---|
| $-0.05$ | $-0.5$ | 0.4137 | 0.9826 |
| $-0.10$ | $-1.0$ | 0.4021 | 0.9503 |
| $-0.30$ | $-2.9$ | 0.3461 | 0.7948 |
| $-1.00$ | $-9.8$ | 0.2354 | 0.4873 |
| $-3.30$ | $-32.4$ | 0.1501 | 0.2503 |
| $-10.0$ | $-98.1$ | 0.1067 | 0.1297 |
| $-150$ | $-1471$ | 0.0692 | 0.0256 |

with $S_e = (\theta - \theta_r)/(\theta_s - \theta_r)$. Limits check: $\theta(0) =
0.4200 = \theta_s$ exactly, and $\theta(-10^{4}\ \mathrm{m}) = 0.06074 \to
\theta_r$. The **inverse** relation is what a numerical model needs most often:

$$\lvert h(\theta)\rvert = \frac{1}{\alpha}\left(S_e^{-1/m} - 1\right)^{1/n}.$$

### 2.2 The conductivity function

The **Mualem–van Genuchten** model gives

$$K(\theta) = K_s\,S_e^{1/2}\left[1 - \left(1 - S_e^{1/m}\right)^{m}\right]^{2}.$$

The two exponents are not free: $S_e^{1/2}$ is a tortuosity factor and the bracket
is the integral of the pore-size distribution. For the synthetic soil:

| $h$ (m) | $S_e$ | $K$ (m s$^{-1}$) | $K/K_s$ |
|---|---|---|---|
| $-0.05$ | 0.9826 | $4.65 \times 10^{-6}$ | $4.7 \times 10^{-1}$ |
| $-0.10$ | 0.9503 | $2.83 \times 10^{-6}$ | $2.8 \times 10^{-1}$ |
| $-0.30$ | 0.7948 | $5.75 \times 10^{-7}$ | $5.8 \times 10^{-2}$ |
| $-1.00$ | 0.4873 | $2.34 \times 10^{-8}$ | $2.3 \times 10^{-3}$ |
| $-3.30$ | 0.2503 | $4.43 \times 10^{-10}$ | $4.4 \times 10^{-5}$ |
| $-10.0$ | 0.1297 | $9.45 \times 10^{-12}$ | $9.5 \times 10^{-7}$ |
| $-150$ | 0.0256 | $7.27 \times 10^{-16}$ | $7.3 \times 10^{-11}$ |

$K$ falls by **ten orders of magnitude** over 150 m of suction, and by more than
four orders of magnitude between the water table and the wilting point. Note also
that $K(\theta_s) = K_s$ exactly — a useful unit test of any implementation.

### 2.3 Field capacity, wilting point, available water

| Quantity | Suction convention | Value for the synthetic soil |
|---|---|---|
| field capacity $\theta_{fc}$ | $h = -3.3$ m ($-33$ kPa) | 0.1501 |
| wilting point $\theta_{wp}$ | $h = -150$ m ($-1.5$ MPa) | 0.0692 |
| available water capacity | $\theta_{fc} - \theta_{wp}$ | 0.0809 m$^3$ m$^{-3}$ |

Available water $= 0.0809\ \mathrm{m^3\,m^{-3}} = 80.9\ \mathrm{mm}$ per metre of
soil, i.e. 24.3 mm over a 0.3 m root zone, 40.5 mm over 0.5 m, 161.8 mm over 2 m.

Both conventions are **operational definitions, not soil constants**: field
capacity is "the water content after two days of drainage" (a hydraulic process
with a timescale), and the wilting point is a plant response that depends on the
crop (a biological process). A soil's available water is therefore
0.08 for a shallow-rooted crop and different for a deep-rooted one — the same soil,
two answers.

## 3. Infiltration: the Green–Ampt model

Green–Ampt idealises the wetting front as a **sharp step** at depth $L_f$, with
water content jumping from $\theta_i$ ahead to $\theta_s$ behind. Darcy's law
applied across the wetted zone, with the suction $\psi_f$ at the front, gives

$$\boxed{\;f = K_s\left(1 + \frac{\psi_f\,\Delta\theta}{F}\right),
\qquad \Delta\theta = \theta_s - \theta_i,}$$

where $F$ is the cumulative infiltration and $f = \mathrm{d}F/\mathrm{d}t$.
Separating and integrating with $F = 0$ at $t = 0$:

$$F - \psi_f\Delta\theta\,\ln\left(1 + \frac{F}{\psi_f\Delta\theta}\right) = K_s t.$$

With $\theta_i = 0.15$ (so $\Delta\theta = 0.27$) and a stated
$\psi_f = 0.20$ m:

| $t$ (min) | $F$ (mm) | $f$ (mm h$^{-1}$) | front depth $F/\Delta\theta$ (m) |
|---|---|---|---|
| 1 | 8.45 | 265.9 | 0.031 |
| 5 | 20.05 | 132.9 | 0.074 |
| 15 | 37.44 | 87.9 | 0.139 |
| 30 | 56.82 | 70.2 | 0.210 |
| 60 | 88.34 | 58.0 | 0.327 |
| 180 | 189.28 | 46.3 | 0.701 |

Two limits worth memorising: $f \to K_s$ as $F \to \infty$ (the suction term
becomes negligible and infiltration is limited by the saturated conductivity), and
$f \to \infty$ as $F \to 0$ (the initial wetting front is driven by suction alone).

### 3.1 Ponding time under rainfall

If rainfall arrives at rate $r$, ponding begins when the infiltration capacity has
fallen to $r$. Inverting the Green–Ampt relation gives the **Mein–Larson ponding
time**

$$t_p = \frac{K_s\,\psi_f\,\Delta\theta}{r\,(r - K_s)}, \qquad r > K_s,$$

and $t_p = \infty$ for $r \le K_s$: **rain at or below the saturated conductivity
never ponds.** For the synthetic soil ($K_s = 36$ mm h$^{-1}$):

| $r$ (mm h$^{-1}$) | $r/K_s$ | $t_p$ |
|---|---|---|
| 18 | 0.50 | never |
| 36 | 1.00 | never |
| 54 | 1.50 | 120 min |
| 108 | 3.00 | 15.0 min |
| 360 | 10.0 | 1.0 min |

The $\sim 1/r^{2}$ decay for $r \gg K_s$ is one of the most useful field rules in
hydrology: **doubling the rainfall intensity cuts the time to ponding by about
four**, and therefore quadruples the fraction of the event that becomes surface
runoff.

## 4. The Richards equation

Green–Ampt is an approximation. The governing equation is Richards' equation,
which is Darcy's law plus mass conservation with $\theta(h)$ as the state relation:

$$C(h)\frac{\partial h}{\partial t}
= \frac{\partial}{\partial z}\left[K(h)\left(\frac{\partial h}{\partial z} - 1\right)\right],
\qquad C(h) = \frac{\mathrm{d}\theta}{\mathrm{d}h},$$

with $z$ measured downwards and the $-1$ from gravity. Equivalently, in the
**mixed form** used for numerical work (which conserves mass far better),

$$\frac{\partial \theta}{\partial t}
= -\frac{\partial q}{\partial z},
\qquad q = -K(h)\left(\frac{\partial h}{\partial z} - 1\right).$$

Nonlinearity is the whole difficulty: $K$ depends on $h$, $C$ depends on $h$, and
both vary by orders of magnitude across the front.

### 4.1 A numerical solution, and its verification

The demonstration solves the mixed form with a conservative finite-volume explicit
scheme on a $0.8$ m column, driven by a rainfall flux $r = 5\
\mathrm{mm\,h^{-1}} = 1.389 \times 10^{-6}\ \mathrm{m\,s^{-1}}$ (so
$r/K_s = 0.139 < 1$ and the surface never saturates).

**Verification 1 — the water budget.** Over $t = 6$ h the applied water is
$rt = 30.00$ mm. The model reports storage $29.991$ mm and drainage
$0.0095$ mm, with **zero** water clipped above saturation and a closure error of
$8.3 \times 10^{-11}$ mm — round-off. The budget is exact because the scheme is
finite-volume; an error here would indicate a genuine bug, so this is a
verification of the code, not a restatement of the model.

**Verification 2 — grid independence.** The same run at 101, 201 and 401 nodes
($\Delta z = 8$, 4 and 2 mm) gives storage $29.991$ mm in every case and drainage
$0.0095$ mm in every case, to the printed precision. Grid convergence at this
level is expected for a diffusive problem solved to steady conditions and
confirms that the front is resolved.

**Verification 3 — the long-time limit.** With a constant flux $r < K_s$ and free
drainage, the profile must approach a steady state in which $K(\theta) = r$
everywhere (the "unit-gradient" state). Inverting the Mualem relation gives
$\theta \to 0.3792$ for $r = 1.389 \times 10^{-6}\ \mathrm{m\,s^{-1}}$. The
computed surface water content after 6 h is 0.3580 and rising
($K/r = 0.564$ at the surface, i.e. still short of the asymptote) — consistent
with a profile still relaxing towards the limit at a rate governed by
$C/K \sim$ hours.

**What the solution looks like after 6 h:**

| depth (m) | $\theta$ | $h$ (m) | $K$ (m s$^{-1}$) | $K/r$ |
|---|---|---|---|---|
| 0.00 | 0.3580 | $-0.2561$ | $7.83 \times 10^{-7}$ | 0.564 |
| 0.05 | 0.3439 | $-0.3085$ | $5.43 \times 10^{-7}$ | 0.391 |
| 0.10 | 0.3188 | $-0.4132$ | $2.81 \times 10^{-7}$ | 0.202 |
| 0.15 | 0.2677 | $-0.7074$ | $6.67 \times 10^{-8}$ | 0.048 |
| 0.25 | 0.1500 | $-3.3075$ | $4.39 \times 10^{-10}$ | 0.000 |
| 0.80 | 0.1500 | $-3.3075$ | $4.39 \times 10^{-10}$ | 0.000 |

Ahead of the front, $K(\theta_i)/r = 3.2 \times 10^{-4}$: essentially no water
reaches dry soil under a small flux, which is why the front stays sharp even
though the profile behind it is graded.

### 4.2 "The front" is a definition

After 6 h the **50%-crossing** of the profile sits at **0.136 m**. The
sharp-front position implied by the stored water is
$F/\Delta\theta = 0.029990/0.27 = 0.111$ m, and that is also the Green–Ampt
prediction $rt/\Delta\theta = 0.111$ m. The two differ by **25 mm (about 20%)**
purely because the profile is diffuse: a $50\%$ crossing is always deeper than the
equivalent sharp front. **Which definition is "the front" is a choice, and it must
be stated**, because it is exactly the sort of definitional discrepancy that
becomes a spurious "model error" in a comparison.

## 5. The geophysical link: permittivity and GPR

Water has a relative permittivity of about 81 against 4.5 for soil minerals and 1
for air, so the bulk permittivity is a strong, nearly linear function of water
content. The **complex refractive index model** (CRIM) makes the mixture rule
linear in $\sqrt{\varepsilon}$:

$$\sqrt{\varepsilon_{\text{eff}}}
= (1 - \phi)\sqrt{\varepsilon_s} + \theta\sqrt{\varepsilon_w}
+ (\phi - \theta)\sqrt{\varepsilon_a},$$

and in the low-loss regime the radar velocity is
$v = c/\sqrt{\varepsilon_{\text{eff}}}$. With $\varepsilon_s = 4.5$,
$\varepsilon_w = 81$, $\varepsilon_a = 1$, $\phi = 0.42$ and
$c = 0.299792458\ \mathrm{m\,ns^{-1}}$:

| $\theta$ | $\varepsilon_{\text{eff}}$ | $v$ (m ns$^{-1}$) | two-way time over 1 m (ns) |
|---|---|---|---|
| 0.05 | 4.204 | 0.1462 | 13.68 |
| 0.10 | 6.004 | 0.1223 | 16.35 |
| 0.20 | 10.565 | 0.0922 | 21.68 |
| 0.30 | 16.405 | 0.0740 | 27.02 |
| 0.42 | 25.104 | 0.0598 | 33.43 |

The sensitivity near $\theta = 0.155$ is $\mathrm{d}\varepsilon/\mathrm{d}\theta =
46.2$, so **a one-percentage-point change in water content changes the
permittivity by 0.46 (5.5%)** — far above the repeatability of a modern GPR
velocity analysis, which is why GPR is the standard tool for soil moisture.

**The inversion is remarkably robust to the porosity assumption.** Inverting
$\varepsilon_{\text{eff}} = 12.0$ with three assumed porosities:

| assumed $\phi$ | inferred $\theta$ |
|---|---|
| 0.36 | 0.2183 |
| 0.42 | 0.2267 |
| 0.48 | 0.2351 |

A six-point error in porosity moves the inferred water content by only about
0.01, because the mineral and air end members have similar permittivities and
partly cancel. Compare this with
[05 Groundwater Chemistry](05-groundwater-chemistry.md), where the same porosity
error changes an inferred salinity by a factor of four. **The lesson generalises:
the sensitivity of an inversion to a nuisance parameter depends on the contrast
between that parameter's end members, not on the parameter's importance in
general.**

## 6. Python demonstration

`code/unsaturated_zone_demo.py` prints all of the above with units. It:

1. tabulates $\theta(h)$ and $K(\theta)$ and checks the limits $\theta(0) =
   \theta_s$ and $K(\theta_s) = K_s$ (exact to $10^{-16}$ relative);
2. computes field capacity, wilting point and available water over four root-zone
   depths;
3. solves the Green–Ampt equation by Newton iteration and tabulates $F$, $f$ and
   the front depth, then computes ponding times for five rainfall rates;
4. solves the Richards equation by a conservative finite-volume scheme at three
   grid resolutions, closing the water budget to $8.3 \times 10^{-11}$ mm;
5. verifies the same explicit time-stepping machinery against the analytic
   $\mathrm{erfc}$ solution of the linear diffusion equation
   (maximum error $8.3 \times 10^{-6}$, i.e. $3.1 \times 10^{-5}$ of the step);
6. converts $\theta$ to $\varepsilon$ with CRIM, computes GPR velocities and
   two-way times, and inverts for $\theta$ under three assumed porosities.

```bash
cd 14-hydrology-hydrogeophysics/01-hydrology-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python unsaturated_zone_demo.py
```

Runtime is about 7 s, dominated by the three Richards runs.

## 7. Assumptions and regime of validity

1. **Rigid, isothermal, single-phase-flow soil.** No swelling clays, no
   preferential flow, no temperature-driven vapour transport, no freezing.
   Frozen ground and shrink–swell clays each break the model completely.
2. **Hysteresis is neglected.** Wetting and drying retention curves differ; the
   van Genuchten curve used here is single-valued, which introduces errors
   during wetting–drying cycles of order the hysteresis loop width (several
   hundredths of a water-content unit).
3. **The retention curve is a fitted closed form.** $\theta_r$ has no physical
   existence; $\alpha$ and $n$ are correlated in fitting, so a family of
   $(\alpha, n)$ pairs describes the same data (the same non-uniqueness pattern as
   everywhere else in this module).
4. **The conductivity function is a model.** Mualem's integral assumes a
   specific pore-size distribution shape and a bundle-of-capillaries geometry; the
   $K_s$ used is a matric-potential-free value, so it differs from a field
   infiltration measurement.
5. **Green–Ampt assumes a sharp front with $\theta_s$ behind it.** The
   demonstration measures the resulting overstatement of both stored water and
   front depth relative to a diffuse-front solution, so $\psi_f$ must be treated
   as a **calibration parameter**, not a measured suction.
6. **The flux-driven solution requires $r \le K_s$.** Above that, ponding occurs,
   the surface becomes a head boundary, and rainfall excess becomes runoff — the
   regime covered by §3.1 rather than by the numerical solution here.
7. **CRIM assumes a three-phase mixture with no clay-bound water and no
   frequency dependence.** Clay-bound water has a much lower permittivity than
   free water, so a mineral-specific calibration is needed for clay-rich soils.
8. **The $\mathrm{erfc}$ verification uses a linear diffusion equation**, which
   is NOT Richards' equation. It tests the time-stepper and the boundary
   treatment, not the retention model — a distinction the demonstration states
   explicitly.

## Mastery checkpoint

A synthetic silt loam has $\theta_s = 0.46$, $\theta_r = 0.10$, $\alpha =
1.2\ \mathrm{m^{-1}}$, $n = 1.5$, $K_s = 2.0 \times 10^{-6}\ \mathrm{m\,s^{-1}}$,
and an initial water content $\theta_i = 0.22$.

**(a)** Compute $\theta$ at $h = -0.5$ and $-5$ m, and $K$ at those water
contents. **(b)** Compute the available water capacity between $h = -3.3$ and
$-150$ m in mm per metre. **(c)** Compute the ponding time for rainfall at 12 and
at $24\ \mathrm{mm\,h^{-1}}$, and state whether either ponds. **(d)** With
$\psi_f = 0.25$ m, compute $F$ and $f$ at $t = 30$ min of ponded infiltration.
**(e)** Compute the CRIM permittivity and GPR velocity at $\varepsilon$-inferred
$\theta = 0.25$, and the two-way travel time through a 0.5 m layer. **(f)** The
same soil is tilled, raising $\alpha$ to $2.4\ \mathrm{m^{-1}}$ and $\theta_s$ to
0.50 with $\theta_r$ unchanged. What happens to the available water capacity and
to the ponding time for a 24 mm h$^{-1}$ rain? Explain in one sentence which
change a farmer would care about more.

## Common pitfalls

1. **Reporting $K$ without stating $\theta$ or $h$.** An unsaturated conductivity is
   meaningless without the state at which it applies.
2. **Treating $\theta_r$ as a measurement.** It is a fitting parameter; the curve
   only becomes flat.
3. **Using field capacity and wilting point as soil constants.** Both are
   conventions; the crop and the drainage time decide.
4. **Assuming Green–Ampt's $\psi_f$ is the wetting-front suction of the retention
   curve.** It is a calibration; the two can differ by an order of magnitude.
5. **Comparing front positions from different definitions.** A 20% discrepancy
   appeared in this lesson between two definitions of the same front.
6. **Forgetting that ponding occurs at $r = K_s$, not at some fixed rainfall
   rate.** The threshold is a property of the soil.
7. **Assuming that impermeable-looking dry soil stops infiltration.** It does not
   stop it; it slows it by orders of magnitude and delays it, which matters for
   the recharge timescale rather than for the total.
8. **Applying a saturated-zone Archie relation to the unsaturated zone** without a
   water-content term (see [05](05-groundwater-chemistry.md) §7 and
   [module 14-02](../02-hydrogeophysics-methods/README.md)).

## Related modules

- [03 Hydraulic Head, Darcy's Law and Groundwater Flow](03-hydraulic-head-darcy.md)
  — the saturated limit of this lesson.
- [04 Well Hydraulics and Pumping Tests](04-well-hydraulics.md) — the delayed-yield
  behaviour that the unsaturated zone causes in an unconfined aquifer.
- [01 The Hydrologic Cycle and Water Balance](01-hydrologic-cycle.md) — the recharge
  term that this lesson determines.
- [04 GPR for Soil Moisture and the Water Table](../02-hydrogeophysics-methods/04-gpr-for-soil-moisture.md)
  — the field realisation of the permittivity link in §5.
- [10-gpr-near-surface/01-gpr-principles](../../10-gpr-near-surface/01-gpr-principles/README.md)
  — the electromagnetic theory behind CRIM and the radar velocity.

## Code and exercises

- Demonstration: [`code/unsaturated_zone_demo.py`](code/unsaturated_zone_demo.py)
- Exercises: [`exercises/06-unsaturated-zone-exercises.md`](exercises/06-unsaturated-zone-exercises.md)
- Worked solutions: [`exercises/06-unsaturated-zone-solutions.md`](exercises/06-unsaturated-zone-solutions.md)
