---
id: 11-06-01
title: "Site Investigation: Objectives and Method Selection"
level: advanced
prereqs: ["11-01-02", "06-10-05", "10-04-02"]
tags: [exploration-geophysics, geotechnical, site-investigation, vs30, settlement, microgravity, value-of-information]
---

# Site Investigation: Objectives and Method Selection

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** a measured shear-wave velocity into a small-strain shear modulus
   and an elastic modulus, and **state** the assumption behind each conversion.
2. **Compute** a vs30 value from a layered velocity profile and **show** how
   truncating the profile or missing a surface layer changes it.
3. **Derive** the elastic settlement of a uniformly loaded flexible circular
   footing from the Boussinesq solution and **compute** its sensitivity to a
   shear-velocity error.
4. **Derive** the gravity anomaly of a buried sphere and **compute** the depth
   limit of a microgravity survey for a stated void size and noise level.
5. **Select** a geophysical method for a stated geotechnical objective and
   **justify** the choice with a resolution or detection number.
6. **Compute** the value of information of a survey against a stated prior and
   explain why a survey can destroy value.

## Prerequisites

- [11-01-02 Targeting Strategy and Method Selection](../01-exploration-workflow/02-targeting-and-strategy.md)
  — the general logic this lesson applies to the built environment.
- [06-10-05 Seismic Methods for Site Characterisation](../../06-seismology/10-refraction-and-near-surface-seismology/05-seismic-hazards-site.md)
  — the acquisition that produces the velocities used here.
- [10-04-02 Shear-Wave Velocity Modelling](../../10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/02-shear-wave-velocity-modelling.md)
  — how a $v_s$ profile is measured and modelled.
- [18-06-06 Decision Under Uncertainty](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md)
  — the expected-cost framework of Section 3.5.

> All models and data in this module are **SYNTHETIC**. No real site, borehole,
> footing or survey is used, and no code requirement or design value is quoted.

## 1. Intuition: the product is a ground model, not a section

A geotechnical investigation exists to answer a design question: *can this
structure be built here, and what has to be done first?* The engineering answer
takes the form of a **ground model** — a description of the soil and rock
sequence, its engineering properties, and the uncertainty on both. The ground
model has two parts that must not be confused:

- the **factual** part: what was measured, where, and with what uncertainty
  (borehole logs, velocity profiles, density, water levels);
- the **interpretive** part: what the investigator believes lies between and
  beyond the measurements (boundaries, a karst cavity, a fault, a designed
  parameter).

Geophysics is efficient at the factual part over large volumes and useless at
replacing the interpretive judgement. The worst outcome is not a missing
measurement; it is an interpretive model reported as though it were measured.
This lesson derives the links from the geophysical observables to the
engineering quantities, and then treats method selection as an economic decision.

## 2. Precise definitions

### 2.1 The geotechnical quantities

| Quantity | Meaning | Typical unit |
|---|---|---|
| $v_s$, $v_p$ | Shear and compressional wave speed | $\mathrm{m\,s^{-1}}$ |
| $v_{s30}$ | Travel-time average $v_s$ over the top 30 m | $\mathrm{m\,s^{-1}}$ |
| $G_{\max}$ | Small-strain shear modulus | Pa, MPa |
| $E$ | Young's modulus | Pa, MPa |
| $\nu$ | Poisson's ratio | dimensionless |
| $q$ | Applied footing pressure | kPa |
| $s$ | Settlement | mm |

$v_{s30}$ is defined as a **travel-time** (harmonic) average, not an arithmetic
one:

$$ v_{s30} = \frac{30\ \mathrm{m}}
{\displaystyle\sum_i \frac{h_i}{v_{s,i}} }, $$

with $h_i$ the thickness of layer $i$ within the top 30 m. Because it is defined
by a time, a slow layer dominates it.

### 2.2 Small-strain versus operational moduli

A seismic measurement is made at strains of order $10^{-6}$ or less. A footing
works at strains of order $10^{-4}$ to $10^{-2}$, where the modulus is smaller,
sometimes by a factor of several. The ratio is a **strain-dependent modulus
reduction** and is a soil property, not a correction factor. Any design
calculation that uses $G_{\max}$ directly overestimates the stiffness, and this
lesson states its reduction factor explicitly rather than hiding it.

### 2.3 Objectives and observables

Method selection starts from the objective, not from the instrument. Typical
objectives and the observable that answers each:

| Objective | Observable | Method |
|---|---|---|
| Depth to bedrock / rippability | $v_p$ contrast | seismic refraction, MASW |
| Stiffness profile for settlement | $v_s(z)$ | MASW, downhole, cross-hole |
| Void or cavity detection | density contrast | microgravity, GPR, ERT |
| Water level and saturated thickness | $v_p$ step, $\sigma$ | refraction, ERT |
| Fill thickness and buried obstructions | dielectric and conductive contrasts | GPR, EM |
| Contaminated ground | conductivity | ERT, EM |

## 3. Derivations

### 3.1 From $v_s$ to stiffness

The shear modulus of an elastic medium is defined by $\mu = \rho v_s^{2}$;
because a seismic shear wave is measured in this regime, the measured quantity
**is** $G_{\max}$:

$$ \boxed{\;G_{\max} = \rho v_s^{2}\;}. $$

For an isotropic linear elastic solid,

$$ E = 2G(1+\nu), $$

so with $\rho = 2000\ \mathrm{kg\,m^{-3}}$ and $\nu = 0.30$ (a stated teaching
value):

| Material | $v_s$ (m/s) | $G$ (MPa) | $E$ (MPa) |
|---|---|---|---|
| soft soil | 150 | 40.5 | 105 |
| stiff soil | 300 | 171.0 | 445 |
| dense sand / gravel | 500 | 500.0 | 1300 |
| weathered rock | 900 | 1782.0 | 4633 |
| competent rock | 2000 | 10000.0 | 26000 |

The table is printed by the demonstration. Note the consequences: a factor of
$3.3$ in $v_s$ is a factor of $11$ in $G$, and the geophysical measurement
therefore discriminates stiffness far better than velocity.

### 3.2 The Boussinesq settlement of a circular footing

For a point load $Q$ on the surface of a homogeneous elastic half-space, the
Boussinesq solution gives a surface deflection that falls as $1/r$. Integrating a
uniform pressure $q$ over a circular area of radius $R$ gives the settlement at
the centre of a **flexible** loaded area:

$$ s = \frac{2qR(1-\nu^{2})}{E}. $$

The derivation is the integral of $q\,\mathrm{d}A\,(1-\nu^{2})/(\pi E r)$ over the
disc; the factor $2$ arises from the $1/r$ kernel. The result is proportional to
$R$ and to $q$, and inversely proportional to $E$ — and since $E \propto v_s^{2}$,

$$ s \propto v_s^{-2}. $$

**This is the reason a velocity error matters so much.** With the demonstration's
stated values ($q = 200\ \mathrm{kPa}$, $R = 2.5\ \mathrm{m}$, $\nu = 0.30$,
$\rho = 2000\ \mathrm{kg\,m^{-3}}$, and an operational modulus
$E_{\text{op}} = 0.30\,E_{\max}$):

| $v_s$ (m/s) | $E_{\text{op}}$ (MPa) | settlement (mm) |
|---|---|---|
| 250 | 97.5 | 9.3 |
| 400 | 249.6 | 3.6 |
| 600 | 561.6 | 1.6 |

and a $\pm20\%$ error in $v_s$ moves the settlement by $+56\%$ / $-31\%$.

### 3.3 The gravity anomaly of a buried sphere

A homogeneous sphere produces, outside itself, exactly the field of a point mass
at its centre (Newton's theorem), so for a density contrast $\Delta\rho$, radius
$R$ and centre depth $z$:

$$ g_z(x) = \frac{G M z}{(x^{2}+z^{2})^{3/2}},
\qquad M = \frac{4}{3}\pi R^{3}\Delta\rho. $$

Directly above the centre the anomaly is
$g_z(0) = \frac{4}{3}\pi G \Delta\rho R^{3}/z^{2}$. For an air-filled void
$\Delta\rho = -\rho_{\text{rock}}$; with $\rho_{\text{rock}} = 2500\
\mathrm{kg\,m^{-3}}$ the demonstration prints (in $\mu\mathrm{Gal}$):

| Void radius | $z = 5$ m | $z = 10$ m | $z = 15$ m | $z = 20$ m |
|---|---|---|---|---|
| 1 m | $-2.80$ | $-0.70$ | $-0.31$ | $-0.17$ |
| 2 m | $-22.37$ | $-5.59$ | $-2.49$ | $-1.40$ |
| 3 m | $-75.48$ | $-18.87$ | $-8.39$ | $-4.72$ |

Against a $5\ \mu\mathrm{Gal}$ survey noise, the depth limits are $3.7$,
$10.6$ and $19.4\ \mathrm{m}$ for the three radii. The anomaly scales as
$R^{3}/z^{2}$, so the depth limit scales as $R^{3/2}$ — to double the depth you
must multiply the *volume* by $2^{3} = 8$, not the radius by 2.

### 3.4 Why a sphere model matters even when the target is not a sphere

A cavity is rarely a sphere, and the sphere model is used because it is *the
least optimistic* simple shape: for equal volume and depth, a flat-topped cavity
produces a similar or larger anomaly, and an elongated one a smaller peak at the
same volume. A depth limit from a sphere model is therefore a defensible lower
bound when the shape is unknown — provided the density contrast and the noise are
stated. What the model cannot do is convert a measured anomaly into a unique
depth: the anomaly amplitude is degenerate in $(R, z, \Delta\rho)$, exactly as in
the potential-field inverse problems of
[folder 07](../../07-gravity-geodesy/README.md).

### 3.5 Value of information

Let $p$ be the prior probability of the hazard (a void, a buried obstruction, a
soft pocket), $\mathrm{TPR}$ the probability that it produces a detectable
anomaly, and $\mathrm{FPR}$ the probability that it does not. A decision has to
be made. Two branches:

- **No survey.** Take the risk: expected cost $= p\,H$, with $H$ the cost of a hit
  (repair, redesign, accident).
- **Survey, then act on the result.** Pay the survey cost $c$, take a protective
  measure at cost $P$ whenever an anomaly appears, and bear the residual hit
  probability $p(1-\mathrm{TPR})$:

$$ \mathbb{E}[\text{cost}]_{\text{survey}} = c
+ P\bigl[p\,\mathrm{TPR} + (1-p)\,\mathrm{FPR}\bigr]
+ H\,p\,(1-\mathrm{TPR}). $$

The **value of information** is the difference. With the demonstration's stated
values ($p = 0.10$, $\mathrm{TPR} = 0.85$, $\mathrm{FPR} = 0.20$, $c = 15$,
$P = 100$, $H = 400$ — arbitrary synthetic cost units):

$$ \mathbb{E}[\text{no survey}] = 0.10(400) = 40, $$
$$ \mathbb{E}[\text{survey}] = 15 + 100(0.265) + 400(0.015) = 47.5, $$
$$ \text{VOI} = -7.5 \quad (\text{the survey destroys value}). $$

At $p = 0.30$ the VOI is $+47.5$, and at $p = 0.60$ it is $+130.0$. Three
conclusions, all matter-of-fact:

1. A survey is not automatically worth doing; it is worth doing when the prior
   risk and the consequence are large enough.
2. The survey **never removes the risk** — the residual miss term stays.
3. The decision rule must be stated before the survey, or the survey will be
   reported as a set of anomalies rather than as a decision aid.

## 4. Worked examples

### Example 1 — stiffness and settlement for a proposed footing

A MASW profile gives $v_{s30} = 300\ \mathrm{m\,s^{-1}}$ over a
$\rho = 1900\ \mathrm{kg\,m^{-3}}$ profile.

$$ G_{\max} = 1900 \times 300^{2} = 1.71\times10^{8}\ \mathrm{Pa}
= 171\ \mathrm{MPa}, $$
$$ E_{\max} = 2(171)(1.30) = 444.6\ \mathrm{MPa}, \qquad
E_{\text{op}} = 0.30(444.6) = 133.4\ \mathrm{MPa}. $$

For $q = 200\ \mathrm{kPa}$, $R = 2.5\ \mathrm{m}$, $\nu = 0.30$:

$$ s = \frac{2(200\times10^{3})(2.5)(1-0.09)}{133.4\times10^{6}}
= \frac{9.1\times10^{5}}{1.334\times10^{8}} = 6.8\times10^{-3}\ \mathrm{m}
= 6.8\ \mathrm{mm}. $$

Now suppose the true operational modulus is half that (a softer response than the
0.30 reduction factor assumed): $s = 13.7\ \mathrm{mm}$. The *modulus reduction
factor* is a larger source of error than the seismic measurement — which is
exactly why it must be stated.

### Example 2 — vs30 is a profile statement, not a site constant

For the synthetic profile of the demonstration ($160\ \mathrm{m\,s^{-1}}$ to
$3\ \mathrm{m}$, $240$ to $8\ \mathrm{m}$, $380$ to $20\ \mathrm{m}$, $600$ to
$40\ \mathrm{m}$):

$$ v_{s30} = \frac{30}{3/160 + 5/240 + 12/380 + 10/600} = 341.6\
\mathrm{m\,s^{-1}}. $$

If the survey stops at 20 m and the 20-30 m interval is assigned the
$380\ \mathrm{m\,s^{-1}}$ of the layer above, $v_{s30}$ becomes
$421.6\ \mathrm{m\,s^{-1}}$ — a $23\%$ change from the interpretation alone.
Adding a 5 m stiff fill at $400\ \mathrm{m\,s^{-1}}$ at the surface changes it to
$326.1\ \mathrm{m\,s^{-1}}$. Neither change touched the ground.

### Example 3 — the void detection limit

A microgravity survey resolves $5\ \mu\mathrm{Gal}$. For a $2\ \mathrm{m}$ radius
void in $2500\ \mathrm{kg\,m^{-3}}$ rock:

$$ g_z(0) = \frac{4}{3}\pi G (2500) \frac{2^{3}}{z^{2}}
= \frac{5.5924\times10^{-6}}{z^{2}}\ \mathrm{m\,s^{-2}}
= \frac{559.2}{z^{2}}\ \mu\mathrm{Gal}, $$

using $1\ \mu\mathrm{Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$. Setting
$g_z = 5\ \mu\mathrm{Gal}$ gives $z^{2} = 559.2/5 = 111.8$, so
$z = 10.6\ \mathrm{m}$ — matching the demonstration. A $1\ \mathrm{m}$ void
reaches the same limit at $3.7\ \mathrm{m}$; a $3\ \mathrm{m}$ void at
$19.4\ \mathrm{m}$.

## 5. Assumptions and regime of validity

1. **Elasticity.** The stiffness relations assume a linear elastic, isotropic
   medium. Soils are non-linear and often anisotropic; the moduli derived here
   are the small-strain, isotropic-equivalent ones.
2. **Strain level.** $G_{\max}$ is not the operational modulus; a reduction
   factor (stated, calibrated, or measured) is required, and it dominates many
   settlements.
3. **Boussinesq settlement** assumes a homogeneous half-space, a flexible load,
   and no layering. A stiff layer at shallow depth reduces the settlement well
   below the homogeneous prediction; a soft layer beneath increases it. Where a
   layering is known, it must be modelled, not averaged.
4. **Sphere gravity model** assumes a compact body, a known density contrast, and
   a survey noise that is *regional* rather than instrumental — the residual
   after removing the regional field usually dominates.
5. **Independence in the information model.** $\mathrm{TPR}$ and $\mathrm{FPR}$
   are stated as fixed numbers; if the anomaly criterion is tuned after looking
   at the data, they are not.

## 6. Python demonstration

`code/site_investigation_demo.py` prints:

1. $G_{\max}$ and $E$ for a table of materials;
2. $v_{s30}$ for a full profile, a truncated profile and a profile with a
   surface fill;
3. the elastic settlement of a footing and its sensitivity to a $v_s$ error;
4. the microgravity anomaly of voids of three radii at four depths, with the
   $5\ \mu\mathrm{Gal}$ depth limit;
5. the value-of-information calculation for four priors.

```bash
cd 11-exploration-geophysics/06-geotechnical-and-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python site_investigation_demo.py
```

Companions:
[`exercises/01-site-investigation-exercises.md`](./exercises/01-site-investigation-exercises.md)
and
[`exercises/01-site-investigation-solutions.md`](./exercises/01-site-investigation-solutions.md).

## Common pitfalls

1. **Reporting a section instead of a ground model.** A resistivity image is not
   a design parameter; the ground model states what was measured and what was
   inferred.
2. **Using $G_{\max}$ as the design modulus.** The strain reduction is usually
   larger than the measurement error.
3. **Quoting $v_{s30}$ without the profile.** It is defined by a travel time and
   changes with truncation and with a missing surface layer.
4. **Treating a microgravity anomaly as a cavity.** Amplitude is degenerate in
   radius, depth and density contrast; the shape of the profile and an
   independent constraint are needed.
5. **Commissioning a survey without a decision rule.** A survey with no
   pre-stated action is a cost with no information content.

## Mastery checkpoint

Complete this without notes:

> A site has a MASW profile of $220\ \mathrm{m\,s^{-1}}$ to $6\ \mathrm{m}$ over
> $480\ \mathrm{m\,s^{-1}}$ below, with $\rho = 1900\
> \mathrm{kg\,m^{-3}}$. **(a)** Compute $G_{\max}$, $E_{\max}$ and the elastic
> settlement of a $R = 2\ \mathrm{m}$, $q = 150\ \mathrm{kPa}$ flexible circular
> footing using a stated operational reduction factor. **(b)** Compute $v_{s30}$
> for the profile. **(c)** A $1.5\ \mathrm{m}$ radius void is suspected at
> $8\ \mathrm{m}$ depth in $2500\ \mathrm{kg\,m^{-3}}$ rock; compute its
> microgravity anomaly and state whether a $5\ \mu\mathrm{Gal}$ survey can see it.
> **(d)** State whether the survey is worth doing for a prior void probability of
> $0.05$ and a hit cost twenty times the survey cost, and show the arithmetic.

A worked version of (a)-(c) is in the lesson-06-01
[solutions](./exercises/01-site-investigation-solutions.md).

## Related modules

- [11-06-02 Geophysics for Tunnels, Dams and Foundations](./02-tunnelling-and-dams.md)
  — the same objectives on large structures.
- [11-06-03 Buried Objects, UXO Detection and Clearance](./03-buried-objects-uxo.md)
  — detection limits and false alarms for small targets.
- [11-06-04 Landfill, Waste and Brownfield Site Assessment](./04-landfill-and-waste.md)
  — the contaminated-ground case, with its own base-rate problem.
- [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md)
  and [10-04 Near-Surface Seismic and Geotechnical Methods](../../10-gpr-near-surface/04-near-surface-seismic-and-geotechnical/01-spt-cpt-crosshole.md).
- [07-03 Gravity Anomalies and Modelling](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/01-anomaly-interpretation.md)
  — the microgravity model in full.

## Self-assessment checklist

- [ ] I can convert $v_s$ to $G_{\max}$ and $E$, and state the strain caveat.
- [ ] I can compute $v_{s30}$ and explain its sensitivity to truncation.
- [ ] I can derive $s = 2qR(1-\nu^{2})/E$ and use it.
- [ ] I can compute a sphere gravity anomaly and a detection limit.
- [ ] I can select a method for a stated objective with a number as justification.
- [ ] I can compute a value of information and say when it is negative.
