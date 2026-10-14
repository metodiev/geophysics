---
id: 07-01-06
title: "Isostasy: Pratt, Airy and Flexural Models"
level: graduate
prereqs: ["07-01-04", "02-04-03", "02-08-04"]
tags: [gravity, geodesy, isostasy, airy, pratt, flexure, lithosphere, compensation]
---

# Isostasy: Pratt, Airy and Flexural Models

**All models and data in this module are SYNTHETIC.** Densities, elastic
constants, compensation depths, topography and station geometry are chosen
teaching values. No mountain belt, dataset or published value is reproduced. The
only exact quantity used is $G = 6.67430\times10^{-11}\
\mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ together with
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Airy root $t = h\rho_{c}/\left(\rho_{m}-\rho_{c}\right)$ from
   hydrostatic balance of columns, and **state** the assumption that makes it local.
2. **Show** that the Airy model is constructed so that the thin-slab isostatic
   anomaly of a perfectly compensated plateau vanishes identically, and
   **compute** the Bouguer anomaly it predicts.
3. **Measure** how much the finite lateral extent of a real root changes that
   cancellation, and **explain** why the "isostatic anomaly" is a residual against
   a hypothesis.
4. **Derive** the Pratt column model $\rho(h) = \rho_{0}D/(D+h)$ and **quantify**
   how much the predicted isostatic anomaly depends on which model is chosen.
5. **Derive** the flexural response of an elastic plate to a sinusoidal load, and
   **compute** the compensation fraction as a function of load wavelength and
   elastic thickness.
6. **State** the non-uniqueness of $\left(\Delta\rho, t\right)$ from gravity alone
   and **quantify** the thickness error produced by a wrong density contrast.
7. **Decide**, for a stated data set and question, which isostatic model is
   adequate, and **state** what would falsify that choice.

## Prerequisites

- [07-01-04 Gravity Reductions](04-gravity-reduction.md)
  — the slab and free-air corrections, and the definition of the Bouguer anomaly.
- [02-04-03 Constitutive Laws](../../02-physics/04-elasticity-and-continuum-mechanics/03-constitutive-laws.md)
  — the elastic moduli entering the flexural rigidity.
- [02-08-04 Poisson's Equation](../../02-physics/08-potential-theory/04-poisson-equation.md)
  — the integral form of the potential used for slab and cylinder attractions.

## 1. The problem isostasy answers

Mountains have roots. That statement sounds like an observation; in fact it is an
inference, and isostasy is the family of models that makes it quantitative. The
question is what supports topography: if a plateau of height $h$ were simply rock
piled on the surface with nothing below it, its mass would produce a large positive
Bouguer anomaly, and observed mountain belts do not have one. Something must
compensate, and there are only three ways to do it:

| mechanism | what varies | model |
|---|---|---|
| a low-density root thickens the crust | thickness | Airy |
| the crust itself is less dense under high terrain | density | Pratt |
| the lithosphere bends and spreads the compensation laterally | rigidity | flexure |

All three predict a **deficit** of mass under topography. What they disagree about
is *how much*, *where*, and *how deep*, and the gravity anomaly differs between them
by tens of milligal. The honest statement to carry through this lesson: the
isostatic correction is a **model-based reduction**, so the residual it produces is
evidence about the model as much as about the rocks.

## 2. The Airy model

### 2.1 Derivation

Consider two vertical columns of unit cross-section reaching to a common
compensation depth: one under a plateau of height $h$ with crustal density
$\rho_{c}$ and mantle density $\rho_{m}$ below the crust, one under the adjacent
plain with crust of normal thickness. Requiring equal pressure at the depth of
compensation gives

$$\rho_{c}\,h = \left(\rho_{m}-\rho_{c}\right)t
\qquad\Longrightarrow\qquad
\boxed{\;t = \frac{\rho_{c}}{\rho_{m}-\rho_{c}}\,h\;}$$

**Numerical values (SYNTHETIC: $\rho_{c} = 2670$, $\rho_{m} = 3270\
\mathrm{kg\,m^{-3}}$):**

| $h$ (km) | root $t$ (km) | deficit $\left(\rho_{m}-\rho_{c}\right)t$ ($\mathrm{kg\,m^{-2}}$) | predicted Bouguer anomaly (mGal) |
|---|---|---|---|
| 0.5 | 2.225 | $1\,335\,000$ | $-55.984$ |
| 1.0 | 4.450 | $2\,670\,000$ | $-111.969$ |
| 2.0 | 8.900 | $5\,340\,000$ | $-223.938$ |
| 3.0 | 13.350 | $8\,010\,000$ | $-335.906$ |
| 5.0 | 22.250 | $13\,350\,000$ | $-559.844$ |

The predicted Bouguer anomaly is $-2\pi G\rho_{c}h$: at $h = 3\ \mathrm{km}$ it is
$-335.906\ \mathrm{mGal}$, and the deficit $\left(\rho_{m}-\rho_{c}\right)t =
8\,010\,000\ \mathrm{kg\,m^{-2}}$ equals $\rho_{c}h = 8\,010\,000\
\mathrm{kg\,m^{-2}}$ **exactly**, because that is how $t$ was defined.

### 2.2 Why the isostatic anomaly is identically zero in the thin-slab approximation

Assemble the effects for a plateau of height $h$:

- the topography's slab contributes $+2\pi G\rho_{c}h$ to the observed value;
- the root's deficit contributes $-2\pi G\left(\rho_{m}-\rho_{c}\right)t$;
- the free-air term removes $-\mathrm{d}\gamma/\mathrm{d}h \cdot h$, which cancels
  the normal-gravity change with height;
- the Bouguer reduction subtracts $2\pi G\rho_{c}h$.

Adding them: the slab terms cancel, and what remains is
$-2\pi G\left(\rho_{m}-\rho_{c}\right)t = -2\pi G\rho_{c}h$. Restoring the
compensation (the isostatic correction) adds $+2\pi G\left(\rho_{m}-\rho_{c}\right)t$
back, giving an isostatic anomaly of **exactly zero**. This is not a coincidence or
a success of the method: it is arithmetic, imposed by the definition of $t$. The
Airy model *cannot* fail to explain a region it was tuned to explain. Any nonzero
isostatic anomaly therefore signals either a departure from local Airy
compensation, or the failure of the infinite-plate approximation used to compute
it — and the next subsection measures the second effect.

### 2.3 The price of the infinite-plate approximation

The slab result assumes the root extends infinitely. The attraction at the centre
of the top face of a cylindrical root of thickness $t$ and radius $R$ is, exactly,

$$g_{\text{root}} = 2\pi G\,\Delta\rho\left[t + R - \sqrt{R^{2}+t^{2}}\right],
\qquad \Delta\rho = \rho_{m}-\rho_{c},$$

so the isostatic anomaly becomes the **unexplained** part

$$\Delta g_{\text{iso}} = 2\pi G\,\Delta\rho\left[\sqrt{R^{2}+t^{2}} - R\right].$$

**Measured (SYNTHETIC, $R = 100\ \mathrm{km}$):**

| $h$ (km) | $t$ (km) | exact root (mGal) | slab root (mGal) | residual (mGal) | residual as % of slab |
|---|---|---|---|---|---|
| 1.0 | 4.450 | 109.479 | 111.969 | 2.490 | 2.2% |
| 3.0 | 13.350 | 313.584 | 335.906 | 22.323 | 6.6% |
| 5.0 | 22.250 | 498.313 | 559.844 | 61.530 | 11.0% |

For a $3\ \mathrm{km}$ plateau with a $100\ \mathrm{km}$-wide root the residual is
$22.3\ \mathrm{mGal}$ — the same order as real isostatic anomalies that are
interpreted as geological signal. The lesson: **an isostatic anomaly of a few tens
of milligal can be produced entirely by the geometry of the computation**, with no
geological information in it. Widening $R$ reduces the residual (it is the same
functional form as the terrain correction of lesson
[04](04-gravity-reduction.md)), so the extent of the assumed root must be stated
with any isostatic anomaly.

## 3. The Pratt model

Pratt (1855) proposed the complementary answer: the crust does not thicken under
topography; it thins, or becomes less dense, so that every column has the same
mass above a fixed **compensation depth** $D$. Writing the density of a column of
height $D+h$ as $\rho(h)$ and requiring equal mass per unit area,

$$\rho(h)\left(D+h\right) = \rho_{0}D
\qquad\Longrightarrow\qquad
\boxed{\;\rho(h) = \frac{\rho_{0}D}{D+h}\;}$$

The deficit per unit area relative to the reference column is

$$D\left(\rho_{0}-\rho(h)\right) = \frac{D\,\rho_{0}\,h}{D+h}
= \rho_{0}h\left(1 - \frac{h}{D+h}\right)
= \rho_{0}h\left(\frac{D}{D+h}\right).$$

**Numerical values (SYNTHETIC: $\rho_{0} = 2670\ \mathrm{kg\,m^{-3}}$,
$D = 30\ \mathrm{km}$):**

| $h$ (km) | $\rho(h)$ ($\mathrm{kg\,m^{-3}}$) | Pratt deficit | Airy deficit | difference |
|---|---|---|---|---|
| 0.5 | 2626.2 | $1\,313\,115$ | $1\,335\,000$ | $-1.64\%$ |
| 1.0 | 2583.9 | $2\,583\,871$ | $2\,670\,000$ | $-3.23\%$ |
| 2.0 | 2503.1 | $5\,006\,250$ | $5\,340\,000$ | $-6.25\%$ |
| 3.0 | 2427.3 | $7\,281\,818$ | $8\,010\,000$ | $-9.09\%$ |
| 5.0 | 2288.6 | $11\,442\,857$ | $13\,350\,000$ | $-14.29\%$ |

**The model dependence, measured.** For $h = 3\ \mathrm{km}$ the Pratt deficit is
short of the Airy deficit by $728\,182\ \mathrm{kg\,m^{-2}}$, which as a slab effect
is $30.54\ \mathrm{mGal}$ of uncancelled gravity signal. So **choosing Pratt instead
of Airy changes the predicted isostatic anomaly by about $30\ \mathrm{mGal}$** for
the same topography and the same densities — comparable to the finite-geometry
effect of Section 2.3, and again with no geological information in it.

The two models are also not equally plausible everywhere. Airy's local root is a
good description where the lithosphere is weak (young, hot, actively deforming);
Pratt's density variation is closer to the truth where the crust is strong and the
compensation is achieved by lateral density changes at depth. In detail, the truth
is a combination, and the whole point of a *flexural* model is to compute it rather
than choose it.

## 4. Flexure: an elastic plate

### 4.1 The governing equation

A thin elastic plate of flexural rigidity $D$ floating on a denser substrate
deflects under a load $q(x)$ according to

$$D\,\frac{\mathrm{d}^{4}w}{\mathrm{d}x^{4}} + \Delta\rho\,g\,w = q(x),
\qquad
D = \frac{E\,T_{e}^{3}}{12\left(1-\nu^{2}\right)},$$

where $T_{e}$ is the **elastic thickness**, $E$ Young's modulus, $\nu$ Poisson's
ratio, and $\Delta\rho$ the density contrast between the material displaced and the
material filling the deflection.

**Numerical values (SYNTHETIC: $E = 7.0\times10^{10}\ \mathrm{Pa}$,
$\nu = 0.25$, $T_{e} = 25\ \mathrm{km}$, $\Delta\rho = 600\
\mathrm{kg\,m^{-3}}$):**

$$D = 9.7222\times10^{22}\ \mathrm{N\,m},$$

$$\alpha = \left(\frac{D}{\Delta\rho\,g}\right)^{1/4} = 63.751\ \mathrm{km}
\qquad\text{(the flexural parameter).}$$

### 4.2 The sinusoidal-load solution

For a load $q(x) = q_{0}\cos kx$ with $k = 2\pi/\lambda$, the solution is
$w(x) = w_{0}\cos kx$ with

$$w_{0} = \frac{q_{0}}{Dk^{4} + \Delta\rho\,g}
\qquad\Longrightarrow\qquad
\frac{w_{0}}{w_{\text{Airy}}} = \frac{1}{1 + \left(2\pi/\lambda\right)^{4}\alpha^{4}},$$

where $w_{\text{Airy}} = q_{0}/\left(\Delta\rho g\right)$ is what a purely local
compensation of the same load would produce. With $q_{0} = \rho_{c}gh$ and
$h = 1\ \mathrm{km}$, $w_{\text{Airy}} = 4.450\ \mathrm{km}$ — the same root as the
Airy formula, as it must be.

**Measured:**

| $\lambda$ (km) | $\lambda/\alpha$ | deflection $w$ (km) | fraction of the Airy root |
|---|---|---|---|
| 50 | 0.78 | 0.001 | 0.0002 |
| 100 | 1.57 | 0.017 | 0.0039 |
| 200 | 3.14 | 0.260 | 0.0585 |
| 400 | 6.27 | 2.219 | 0.4986 |
| 800 | 12.55 | 4.187 | 0.9409 |
| 1600 | 25.10 | 4.433 | 0.9961 |

The transition from regional to local support occurs at
$\lambda = 2\pi\alpha = 400.6\ \mathrm{km}$, exactly as the formula's structure
requires: at that wavelength the plate has deflected half as much as local
compensation would demand. **A short load is carried by the plate and produces
almost no root; a long load is compensated almost locally.** A single "depth of
compensation" is therefore a wavelength-dependent statement, not a property of a
mountain belt.

### 4.3 The three models on one station

SYNTHETIC station on a plateau $h = 2000\ \mathrm{m}$, load width
$\lambda = 300\ \mathrm{km}$, same densities and plate:

| model | predicted root | Bouguer anomaly (mGal) | unexplained residue (mGal) |
|---|---|---|---|
| no support | 0.000 km | $+223.938$ | $+223.938$ |
| Airy (infinite slab) | 8.900 km | $-223.938$ | $0.000$ |
| flexure ($T_{e} = 25\ \mathrm{km}$) | 2.130 km | $-53.597$ | $-170.341$ |

Read the last two columns carefully. The **Bouguer anomaly** is what a survey
would measure; the **residue** is the part that each model leaves unexplained. The
Airy model explains everything by construction; the flexural model, with these
parameters, explains only a quarter of the compensation and would leave a
$-170\ \mathrm{mGal}$ anomaly to be interpreted. Adopting the wrong model is not a
small bookkeeping error: it changes the anomaly from "nothing to explain" to "a
large unexplained signal".

## 5. Worked example — from topography to a predicted anomaly and back

**Forward.** A SYNTHETIC plateau of height $h = 1500\ \mathrm{m}$,
$\rho_{c} = 2670$, $\rho_{m} = 3270\ \mathrm{kg\,m^{-3}}$.

1. Root: $t = 1500 \times 2670/(3270-2670) = 1500 \times 4.45 = 6675\
   \mathrm{m} = 6.675\ \mathrm{km}$.
2. Deficit: $\left(\rho_{m}-\rho_{c}\right)t = 600 \times 6675 =
   4.005\times10^{6}\ \mathrm{kg\,m^{-2}}$.
3. Predicted Bouguer anomaly: $-2\pi G\Delta\rho t \times 10^{5} =
   -0.04193 \times 600 \times 6675/1000 = -167.95\ \mathrm{mGal}$ (using
   $2\pi G = 4.1930\times10^{-10}$ and converting to mGal).
4. Equivalent check: $-2\pi G\rho_{c}h = -0.111969 \times 1500 =
   -167.95\ \mathrm{mGal}$. ✔

**Inverse, and its non-uniqueness.** Suppose a survey measures
$-167.9\ \mathrm{mGal}$ over that plateau and the topography is known. The product
$\Delta\rho\,t = 4.005\times10^{6}\ \mathrm{kg\,m^{-2}}$ follows, but not the pair
separately:

| assumed $\Delta\rho$ ($\mathrm{kg\,m^{-3}}$) | required $t$ (km) |
|---|---|
| 300 | 13.350 |
| 600 | 6.675 |
| 900 | 4.450 |

A $500\ \mathrm{kg\,m^{-3}}$ contrast — plausible in a warm, partly serpentinised
or underplated setting — gives $t = 8.010\ \mathrm{km}$ instead of $6.675\
\mathrm{km}$: a **$1.335\ \mathrm{km}$ ($20\%$) difference in crustal thickness from
identical data**. Gravity alone cannot choose. Seismic receiver functions,
refraction, or a density measurement on mantle-derived material can, which is why
isostatic studies are almost always joint studies.

## 6. Assumptions and regime of validity

1. **Local (Airy) or uniform-density (Pratt) compensation.** Both are end-member
   hypotheses. Real lithosphere is elastic to some degree, so the truth is closer
   to flexure; the end members are useful because they bracket the answer.
2. **Uniform densities.** $\rho_{c}$, $\rho_{m}$ and $\Delta\rho$ are averages whose
   lateral and vertical variation is usually larger than the anomaly being
   interpreted.
3. **Steady state.** Isostasy is a statement of equilibrium. A region in active
   uplift or rebound is out of equilibrium by construction, and its isostatic
   anomaly is a *measurement of that disequilibrium* — a feature, not a nuisance
   (module [06](../06-earth-tides-and-rotation/README.md), lesson 4).
4. **Compensation at a single depth.** Pratt's $D$ and Airy's compensation depth
   are model parameters, not measured horizons.
5. **Thin-plate elasticity and small deflection.** The flexural equation assumes
   deflections small compared with $T_{e}$ and no in-plane loads. For large
   deflections and for loads near a plate boundary the boundary conditions
   dominate, and the simple sinusoidal solution does not apply.
6. **Infinite lateral extent for the slab form.** Measured in Section 2.3: the
   finite geometry changes the residual by tens of milligals.
7. **Rigidity is a state, not a constant.** $T_{e}$ is a rheological parameter that
   depends on temperature and loading history; it may differ between loads in the
   same region.
8. **The residual is a difference of models.** Nothing in this lesson is a direct
   measurement of the compensation.

## 7. Python demonstration

`code/isostasy_demo.py` computes and prints, with units:

1. the Airy root and the predicted Bouguer anomaly for five topographic heights,
   with the exact cancellation of the thin-slab isostatic anomaly;
2. the finite-cylinder root: exact versus slab attraction and the residual
   ($2.490$, $22.323$ and $61.530\ \mathrm{mGal}$ for $h = 1$, $3$ and $5\
   \mathrm{km}$, i.e. $2.2\%$, $6.6\%$ and $11.0\%$ of the compensation);
3. the Pratt column densities and the $30.54\ \mathrm{mGal}$ model dependence at
   $h = 3\ \mathrm{km}$;
4. the flexural rigidity $9.7222\times10^{22}\ \mathrm{N\,m}$, flexural parameter
   $63.751\ \mathrm{km}$, the compensation fraction versus load wavelength and the
   transition at $400.6\ \mathrm{km}$;
5. the three-model comparison on one station;
6. the $\left(\Delta\rho,t\right)$ trade-off table.

Exercises and solutions:
[`exercises/06-isostasy-exercises.md`](exercises/06-isostasy-exercises.md),
[`exercises/06-isostasy-solutions.md`](exercises/06-isostasy-solutions.md).

## Mastery checkpoint

Answer without notes.

> A SYNTHETIC plateau is $2.5\ \mathrm{km}$ high with $\rho_{c} = 2700$ and
> $\rho_{m} = 3300\ \mathrm{kg\,m^{-3}}$. **(a)** Compute the Airy root. **(b)**
> Compute the predicted Bouguer anomaly of a perfectly compensated plateau.
> **(c)** State what the isostatic anomaly of that plateau would be under the
> infinite-slab model and one sentence on why. **(d)** A root of that thickness
> but only $R = 120\ \mathrm{km}$ wide is a cylinder: compute the unexplained
> residual. **(e)** State what the residual would be interpreted as if the
> analysis omitted the geometry.

A worked version of (a)–(d) is in the
[solutions](exercises/06-isostasy-solutions.md).

## Common pitfalls

1. **Treating an isostatic anomaly as a measurement.** It is a residual against a
   model with free parameters, so it inherits their ambiguity.
2. **Forgetting the geometry.** Section 2.3 measures a $22.3\ \mathrm{mGal}$
   residual from finite extent alone, for a root that is "perfectly compensated".
3. **Quoting a crustal thickness without the density contrast.** The
   $\left(\Delta\rho,t\right)$ trade-off is the physics (Section 5).
4. **Assuming the compensation depth is known.** $D$, the Airy compensation depth
   and $T_{e}$ are all model parameters; a fit to them must report their
   correlation, which is typically strong.
5. **Using one isostatic model everywhere.** The appropriate model depends on the
   load wavelength relative to $2\pi\alpha$, and that is a computed number.
6. **Applying Airy's local model to a short-wavelength load.** Section 4.2 shows
   that a $50\ \mathrm{km}$ load produces a root $0.02\%$ of the Airy value — the
   end member is not merely imprecise there, it is wrong by orders of magnitude.
7. **Ignoring the geoid.** The same mass distributions produce both a gravity
   anomaly and a geoid undulation, and the geoid is far more sensitive to deep
   compensation. A model that fits the anomaly and misses the geoid is not
   finished (module [07](../07-geoid-and-height-modern/README.md)).

## Related modules

- [Module 01 — Gravity Fundamentals](README.md) — this module; lesson
  [04](04-gravity-reduction.md) supplies the Bouguer and terrain corrections used
  here, and lesson [02](02-gravity-potential.md) the geoid connection.
- [13-06-01 Isostasy and Flexure Modelling](../../13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md) —
  the geodynamic treatment, with the full plate-boundary mathematics.
- [12-06 Geodesy Constraints on the Interior](../../12-global-geophysics-interior/06-geodesy-constraints-interior/README.md) —
  what moments of inertia add to the compensation problem.
- [Module 07 — The Geoid and Modern Height Determination](../07-geoid-and-height-modern/README.md) —
  where the long-wavelength consequences of compensation appear.
- [04-02 Height Systems](../04-geodesy-reference-frames/02-height-systems.md) —
  why a plateau's height itself depends on the gravity field.
