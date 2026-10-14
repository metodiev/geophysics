---
id: 13-01-02
title: "Rheology: Elastic, Viscous, Plastic and Power-Law Creep"
level: doctoral
prereqs: ["13-01-01", "02-04-07", "01-08-07"]
tags: [geodynamics, tectonophysics, rheology, creep, viscosity, maxwell, brittle-ductile]
---

# Rheology: Elastic, Viscous, Plastic and Power-Law Creep

> All models and data in this module are **SYNTHETIC**. The flow laws and
> strengths below use chosen teaching constants, not laboratory measurements, and
> every number quoted here is printed by `code/rheology_of_earth_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Maxwell relaxation time from the series combination of an
   elastic and a viscous element, and **interpret** the Deborah number as the
   statement of which behaviour a given observation time sees.
2. **Write** a power-law creep law $\dot\varepsilon = A\sigma^{n}e^{-E/RT}$ and
   **derive** its effective viscosity, including the sign and magnitude of the
   stress dependence.
3. **Measure** the stress exponent from synthetic laboratory-style data and
   **quantify** how well $n$ is resolved compared with the prefactor $A$.
4. **Compute** the Arrhenius sensitivity of viscosity to temperature and
   **explain** why a few hundred kelvin produces orders of magnitude.
5. **Locate** the brittle–ductile transition by combining a frictional strength
   envelope with a creep law, and **state** how it moves with the geotherm.
6. **Predict** postseismic stress relaxation from the Maxwell time and **state**
   the observational signature that distinguishes viscous from elastic response.
7. **Explain** why "the viscosity of the mantle" is not a material property but a
   statement about a stress, a temperature and a mechanism.

## Prerequisites

- [13-01-01 Momentum, Mass and Energy Balances in the Solid Earth](01-momentum-mass-energy.md) —
  where $\eta$ enters the equations of motion.
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md) —
  the rheological models this lesson uses quantitatively.
- [01-08-07 Stiff Systems and Numerical Stability Challenges](../../01-mathematics/08-ordinary-differential-equations/07-stiff-systems.md) —
  why the exponentially stiff temperature dependence matters numerically.
- [04-01-02 Lithosphere, Asthenosphere and the Rheological Definition](../../04-earth-science-geology/01-earth-structure/02-lithosphere-asthenosphere.md) —
  the geological labels that this lesson makes mechanical.

## 1. Intuition: one material, four laws, chosen by timescale and stress

Ask four geophysicists what the mantle is and you may get four answers: seismic
waves see an elastic solid, postglacial rebound sees a fluid of
$10^{21}\ \mathrm{Pa\,s}$, the upper crust fails on faults as a brittle solid,
and a laboratory creep experiment sees a material whose viscosity depends on the
stress raised to the 3.5th power. All four are correct; they differ in the
timescale and the stress at which the material is interrogated.

The organising idea is to stop asking "what is the rheology?" and start asking
"over what time and at what stress?". Two controls do most of the organising:

- **The Deborah number** $De = t_{\text{relax}}/t_{\text{obs}}$ separates elastic
  from viscous response: the same material is elastic when you look quickly and
  viscous when you look slowly.
- **The stress** separates linear (Newtonian) from nonlinear (power-law) creep:
  the same material creeps linearly when weakly loaded and nonlinearly when
  strongly loaded.

Everything else — the temperature dependence, the pore pressure, the grain
size, the water content — modulates the coefficients. The honest conclusion,
stated up front because it is the intellectual content of the lesson, is that
**a single number called "the viscosity of the mantle" does not exist**. What
exists is a law, and a legal range of values for its parameters.

## 2. Definitions and constitutive laws

### 2.1 The Maxwell model

Put an elastic spring of shear modulus $\mu$ in series with a viscous dashpot
of viscosity $\eta$. The total strain rate is the sum of the elastic part
$\dot\sigma/\mu$ and the viscous part $\sigma/\eta$:

$$\dot\varepsilon = \frac{\dot\sigma}{\mu} + \frac{\sigma}{\eta} .$$

Hold the strain fixed ($\dot\varepsilon = 0$) and integrate: stress relaxes as
$\sigma(t) = \sigma_0 e^{-t/t_M}$ with the **Maxwell relaxation time**

$$\boxed{\;t_M = \frac{\eta}{\mu}\;}.$$

Take $\mu = 70\ \mathrm{GPa}$ (SYNTHETIC) and the measured values follow:

| $\eta$ (Pa s) | $t_M$ (s) | $t_M$ (yr) | typical material |
|---|---|---|---|
| $10^{18}$ | $1.429\times10^{7}$ | 0.453 | low-viscosity shear zone |
| $10^{19}$ | $1.429\times10^{8}$ | 4.527 | asthenosphere |
| $10^{20}$ | $1.429\times10^{9}$ | 45.27 | weak lower crust |
| $10^{21}$ | $1.429\times10^{10}$ | 452.7 | upper mantle |
| $10^{22}$ | $1.429\times10^{11}$ | 4527 | continental mantle |

### 2.2 The Deborah number

The Deborah number compares that memory time with the observation time:

$$De = \frac{t_M}{t_{\text{obs}}} .$$

Measured: for $\eta = 10^{19}$ Pa s, $De = 1.43\times10^{8}$ at a 1 s seismic
period, $4.53$ at 1 yr and $4.53\times10^{-4}$ at 10 kyr. For
$\eta = 10^{21}$ Pa s the same numbers are $1.43\times10^{10}$, $4.53\times10^{2}$
and $4.53\times10^{-2}$.

The interpretation is not "solid or liquid" but "$De \ll 1$: the material has
forgotten its elastic strain, so treat it as a viscous fluid; $De \gg 1$: treat
it as elastic". The asthenosphere is elastic to a seismic wave and viscous to
postglacial rebound — the deepest sense in which both labels are right.

### 2.3 Power-law (dislocation) creep

At high temperature and stress, deformation is controlled by dislocation motion
and follows

$$\dot\varepsilon = A\,\sigma^{n}\,\exp\!\left(-\frac{E}{RT}\right),$$

with stress exponent $n\approx3$–$3.5$, activation energy $E$, and a prefactor
$A$ that hides grain size, water fugacity, oxygen fugacity and crystal
chemistry. The **effective viscosity** for simple shear is defined by
$\eta_{\text{eff}} = \sigma/(2\dot\varepsilon)$, so that

$$\eta_{\text{eff}} = \frac{e^{E/RT}}{2A\,\sigma^{\,n-1}} .$$

Three consequences, all measured below:

- $\eta_{\text{eff}}$ *falls* as stress rises (shear-thinning) because
  $n-1>0$: on a log–log plot the slope is $-(n-1)$.
- $\eta_{\text{eff}}$ depends *exponentially* on temperature. A small change in
  temperature is a large change in viscosity.
- $\eta_{\text{eff}}$ is not a constant even at fixed temperature and stress: it
  is a bookkeeping device for a nonlinear law, and it must be recomputed at every
  iteration in a numerical model.

### 2.4 Diffusion creep and brittleness

At low stress and small grain size, diffusion creep dominates and is
**Newtonian** ($n=1$), with its own activation energy. At low temperature and
high stress, the material does not creep at all: it fails. Coulomb friction with
pore pressure gives the brittle strength

$$\sigma_b = \mu_f\,(1-\lambda_p)\,\rho g z ,$$

where $\mu_f$ is the friction coefficient and $\lambda_p$ the ratio of pore
pressure to lithostatic pressure (the Hubbert–Rubey construction). The
**brittle–ductile transition** is the depth where $\sigma_b$ meets the creep
strength; below it the rock creeps instead of failing.

## 3. Derivations

### 3.1 The effective viscosity of a power law

Inverting $\dot\varepsilon = A\sigma^n e^{-E/RT}$ for the stress and inserting
the definition $\eta_{\text{eff}} = \sigma/(2\dot\varepsilon)$:

$$\sigma = \left[\frac{\dot\varepsilon\,e^{E/RT}}{A}\right]^{1/n},
\qquad
\eta_{\text{eff}} = \frac{1}{2}\left(\frac{1}{A}\right)^{1/n}
\dot\varepsilon^{\,1/n-1} e^{\,E/(nRT)} .$$

Two equivalent forms are worth memorising, because different papers use
different independent variables:

- **Stress-controlled:** $\eta_{\text{eff}} \propto \sigma^{1-n}e^{E/RT}$ —
  slope $-(n-1)$ in a log–log plot against stress.
- **Strain-rate-controlled:** $\eta_{\text{eff}} \propto \dot\varepsilon^{1/n-1}
  e^{E/(nRT)}$ — slope $(1-n)/n$ against strain rate.

For $n=3.5$, the two slopes are $-2.5$ and $-0.714$. They are not the same
number, and confusing them is the most common quantitative error in this
subject.

### 3.2 Temperature sensitivity

Differentiating $\ln\eta_{\text{eff}} = E/(nRT) + \text{const}$ with respect to
$T$:

$$\frac{\partial \ln \eta_{\text{eff}}}{\partial T} = -\frac{E}{nRT^{2}},
\qquad
\frac{\eta(T_1)}{\eta(T_2)} = \exp\!\left[\frac{E}{nR}\left(\frac{1}{T_1}
-\frac{1}{T_2}\right)\right] .$$

The stiffness here is the reason a mantle-convection model must be implicit, and
the reason a stagnant lid forms: the surface layer is not merely a bit stronger
but orders of magnitude stronger than the interior, so it does not participate
in the flow.

### 3.3 Brittle–ductile transition

Setting $\sigma_b = \sigma_{\text{ductile}}$ and solving for $z$ requires the
geotherm $T(z)$; there is no closed form for a general geotherm, but the
condition is monotone and a bisection converges in a few dozen evaluations. That
is what the demonstration does, and the result is sensitive to both the
geotherm and the flow-law parameters — which is exactly why published
brittle–ductile transition depths are quoted with their assumed geotherm.

## 4. Worked examples

### Example 1 — effective viscosity and its stress sensitivity

SYNTHETIC olivine-like law: $n = 3.5$, $E = 350\ \mathrm{kJ\,mol^{-1}}$,
$A = 2.0\times10^{-28}\ \mathrm{Pa^{-n}\,s^{-1}}$, at $T = 1600$ K. Using
$R = 8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}$:

$$e^{E/RT} = e^{350000/(8.314\times1600)} = e^{26.31} = 2.67\times10^{11}.$$

| $\sigma$ (MPa) | $\dot\varepsilon$ (s$^{-1}$) | $\eta_{\text{eff}}$ (Pa s) |
|---|---|---|
| 1 | $7.4867\times10^{-19}$ | $6.6785\times10^{23}$ |
| 10 | $2.3675\times10^{-15}$ | $2.1119\times10^{21}$ |
| 100 | $7.4867\times10^{-12}$ | $6.6785\times10^{18}$ |

A factor of 100 in stress changes viscosity by a factor of $10^{5}$, and the
measured log–log slope is $-2.5000$ against the predicted $1-n = -2.5$. A
hundredfold change in stress producing a hundred-thousandfold change in
viscosity is the single most important quantitative fact in mantle dynamics: it
is what allows a plate to be effectively rigid while the asthenosphere beneath
it flows.

### Example 2 — temperature

Same law, $\sigma = 10$ MPa:

| $T$ (K) | $\eta_{\text{eff}}$ (Pa s) |
|---|---|
| 1500 | $1.2203\times10^{22}$ |
| 1600 | $2.1119\times10^{21}$ |
| 1700 | $4.4928\times10^{20}$ |

Measured ratios: $\eta(1500)/\eta(1600) = 5.778$,
$\eta(1600)/\eta(1700) = 4.701$, and $\eta(1200)/\eta(1600) = 6.440\times10^{3}$.
**A 400 K difference is worth nearly four orders of magnitude in viscosity.** Any
argument that treats mantle viscosity as a constant is therefore an argument
about a narrow temperature range, or it is wrong.

### Example 3 — the diffusion/dislocation crossover

With a SYNTHETIC Newtonian law ($n=1$, $E=250$ kJ/mol,
$A=10^{-13}\ \mathrm{Pa^{-1}\,s^{-1}}$) and the dislocation law above, both at
$T = 1600$ K, the strain rates cross at

$$\sigma_{\text{cross}} = 1.5329\times10^{7}\ \mathrm{Pa} = 15.33\ \mathrm{MPa},
\qquad \eta = 7.2598\times10^{20}\ \mathrm{Pa\,s}.$$

Below that stress diffusion creep (Newtonian, grain-size sensitive) dominates;
above it dislocation creep does. The crossover stress therefore defines what "a
typical mantle stress" means rheologically, and it is also why laboratory
experiments must span a wide stress range: a single-stress experiment cannot
separate the two mechanisms.

## 5. The strength envelope and the brittle–ductile transition

Combining §2.4 with §2.3 for a SYNTHETIC geotherm (20 K/km in the crust, 12 K/km
below 35 km) and a reference strain rate of $10^{-15}\ \mathrm{s^{-1}}$:

| depth (km) | brittle strength (MPa) |
|---|---|
| 2 | 26.0 |
| 5 | 64.9 |
| 10 | 129.8 |
| 20 | 259.6 |
| 35 (mantle $\rho$) | 535.4 |
| 60 | 917.8 |
| 90 | 1376.7 |

The measured crossing depths are

| geotherm (K/km) | crustal BDT (km) | mantle BDT (km) |
|---|---|---|
| 10 | 21.63 | 69.45 |
| 20 | 11.76 | 37.28 |
| 30 | 8.23 | 26.38 |

The structure to take away: frictional strength grows linearly with depth
(pressure), creep strength falls exponentially with temperature. Their crossing
therefore moves sharply with the geotherm — a factor of three in the crust and a
factor of 2.6 in the mantle across the range tested. Everything that follows in
[13-01-03](03-lithospheric-strength.md) and
[13-01-04](04-forces-and-stresses.md) depends on where that crossing sits.

Two subtleties worth stating explicitly:

1. At any instant, *whichever* mechanism is weaker is the one operating. This is
   a **minimum** rule, not a sum: it is why a strength envelope is drawn as the
   lower of two curves.
2. The envelope is only meaningful at a specified strain rate. Lower the
   reference rate and the ductile branch strengthens: an envelope computed at
   $10^{-15}$ s$^{-1}$ describes a mountain belt, not a seismic wave.

## 6. Transient and postseismic behaviour

The Maxwell model predicts relaxation of a stress step:

$$\frac{\sigma(t)}{\sigma_0} = e^{-t/t_M},
\qquad
\text{fraction relaxed} = 1 - e^{-t/t_M}.$$

Measured:

| $\eta$ (Pa s) | $t_M$ (yr) | relaxed after 1 yr | relaxed after 10 yr |
|---|---|---|---|
| $10^{18}$ | 0.453 | 89.02% | 100.00% |
| $10^{19}$ | 4.527 | 19.82% | 89.02% |
| $10^{20}$ | 45.27 | 2.18% | 19.82% |

The discriminating power of an observation is therefore not in the existence of
relaxation but in its *rate*: a year of postseismic geodetic data separates
$10^{18}$ from $10^{20}$ Pa s by almost the entire range of the table, while it
would struggle to distinguish $10^{21}$ from $10^{22}$. This is the physical basis
of postseismic viscosity inference, treated systematically in
[13-04-03](../04-tectonophysics-deformation/03-postseismic-viscoelastic.md).

## 7. Inverting a creep law: what is resolvable?

A synthetic experiment with 12 data points at $10^{6}$–$10^{8}$ Pa and 5%
log-normal noise recovers the stress exponent as

$$n_{\text{fit}} = 3.486 \quad (\text{true } n = 3.5),
\qquad \text{rms misfit in }\log_{10}\dot\varepsilon = 0.0604 .$$

The exponent is well resolved because it is a *slope*: noise in the amplitude
partially cancels when differencing neighbouring points. The prefactor $A$ is
not, because it trades off against $E$ and against the absolute temperature,
which is itself uncertain. Inverting a creep law from laboratory data is a
joint-inversion problem with a strong parameter degeneracy, and the honest output
is a correlated region in $(A, n, E)$ space — the subject of
[18-01-01](../../18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md).

## 8. Assumptions and regime of validity

| assumption | consequence if violated |
|---|---|
| $\mu$ is temperature- and pressure-independent | affects $t_M$ only weakly; $\mu$ varies far less than $\eta$ |
| single mechanism active | the crossover stress decides which; both may operate together |
| steady-state creep | transient (primary) creep matters immediately after a stress step |
| homogeneous stress | localisation means the stress is not what the average implies |
| isothermal flow law | strain heating can localise shear (see [13-01-01 §6](01-momentum-mass-energy.md)) |
| no damage/weakening | real faults weaken dramatically with slip |
| $\eta_{\text{eff}}$ isotropic | anisotropy and crystallographic preferred orientation are neglected |

The most consequential of these is the **steady-state** assumption. A power law
has no memory, so a real rock cannot have the response to a stress step that the
Maxwell model shows *and* a stress-dependent steady viscosity: those are two
different idealisations. Combining them — a linear Maxwell element in series with
a nonlinear dashpot — is the standard upper-mantle rheological model, and it is a
model, not a measurement.

## 9. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| stress | $\sigma$ | Pa | |
| strain rate | $\dot\varepsilon$ | s$^{-1}$ | |
| viscosity | $\eta$ | Pa s | $[\sigma/\dot\varepsilon]$ |
| activation energy | $E$ | J mol$^{-1}$ | $[RT]$ |
| gas constant | $R$ | J mol$^{-1}$ K$^{-1}$ | $8.314$ (standard) |
| prefactor | $A$ | Pa$^{-n}$ s$^{-1}$ | $[\sigma^{-n}\dot\varepsilon]$ |
| effective viscosity | $\eta_{\text{eff}}$ | Pa s | see §3.1 |

The prefactor's units depend on $n$. If you tabulate $A$ without $n$ you have
lost the ability to check a single calculation — a frequent source of error in
copied flow laws.

## 10. The demonstration

`code/rheology_of_earth_demo.py` prints every number above:

```bash
cd 13-geodynamics-tectonics/01-geodynamic-principles/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rheology_of_earth_demo.py
```

It computes the Maxwell times and Deborah numbers, the stress and temperature
dependence, the diffusion/dislocation crossover by bisection, the brittle
strength profile and the brittle–ductile transition by bisection, the
postseismic relaxation table, and the lab-style inversion with noise. Fixed seed,
print-only, no network, exits 0.

Exercises:
[`exercises/02-rheology-of-earth-exercises.md`](exercises/02-rheology-of-earth-exercises.md)
and
[`exercises/02-rheology-of-earth-solutions.md`](exercises/02-rheology-of-earth-solutions.md).

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC dislocation-creep law has $n = 3$, $E = 300\ \mathrm{kJ\,mol^{-1}}$,
> $A = 10^{-24}\ \mathrm{Pa^{-3}\,s^{-1}}$, and $\mu = 70$ GPa.
> **(a)** Compute $\eta_{\text{eff}}$ at $\sigma = 20$ MPa and $T = 1500$ K.
> **(b)** Compute the Maxwell time for that viscosity and state the Deborah number
> for a 2 yr observation. **(c)** Compute $\eta_{\text{eff}}$ at $T = 1600$ K and
> give the ratio. **(d)** State which of the two figures — the stress or the
> temperature — is better constrained by a laboratory experiment, and why.

A worked version appears in the
[solutions](exercises/02-rheology-of-earth-solutions.md).

## Common pitfalls

1. **Reporting a viscosity without a stress and a temperature.** Both are part of
   the value; $\eta_{\text{eff}}$ is not a material constant.
2. **Mixing the two power-law slopes.** $-(n-1)$ against stress, $(1-n)/n$
   against strain rate.
3. **Using $\eta = \sigma/\dot\varepsilon$ instead of $\sigma/(2\dot\varepsilon)$.**
   The factor 2 is a convention (engineering shear strain vs tensor strain) and
   must be applied consistently.
4. **Sloppy units of $A$.** Tabulate $(A, n)$ together and check
   $A\sigma^{n}$ for a strain rate.
5. **Treating the brittle–ductile transition as a rock property.** It moves with
   the geotherm, the strain rate and the pore pressure.
6. **Reading a postseismic time series with one viscosity.** The transient part
   of the response and the geometry of the viscoelastic body both matter; one
   relaxation time fits a whole family of models.
7. **Forgetting that both mechanisms are active.** Real rock deforms by whichever
   is weaker at that instant; summing them is also defensible, ignoring one is
   not.

## Related modules

- [13-01-01 Momentum, Mass and Energy Balances in the Solid Earth](01-momentum-mass-energy.md) —
  where $\eta$ appears in the equations of motion.
- [13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure](03-lithospheric-strength.md) —
  integrating a strength envelope to get a single number.
- [13-01-04 Driving Forces, Stress Fields and Intraplate Stress](04-forces-and-stresses.md) —
  what the stresses actually are.
- [13-02-01 Rayleigh-Benard Convection Applied to the Mantle](../02-mantle-convection/01-rayleigh-benard-mantle.md) —
  how a temperature-dependent viscosity changes convection.
- [02-04-08 Rock Failure, Fracture and Rate-State Friction](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md) —
  what happens past the brittle limit.
