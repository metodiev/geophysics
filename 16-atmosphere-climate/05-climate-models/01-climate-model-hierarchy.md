---
id: 16-05-01
title: "Model Hierarchy: EBMs, EMICs, GCMs, ESMs"
level: graduate
prereqs: ["16-02-05", "16-04-01", "16-04-03"]
tags: [atmosphere, climate, climate-models, energy-balance, model-hierarchy, parameterisation]
---

# Model Hierarchy: EBMs, EMICs, GCMs, ESMs

> All models and data in this module are **SYNTHETIC**. The numbers quoted in
> this lesson were printed by
> [`code/climate_model_hierarchy_demo.py`](code/climate_model_hierarchy_demo.py),
> which you can run yourself; the parameters are teaching choices, not fitted
> values and not observations.

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** a climate model by the state variables it carries and the
   processes it resolves, rather than by its name.
2. **Derive** the effective radiating temperature of a planet from an absorbed
   shortwave flux and the Stefan-Boltzmann law, and **state** why it is a
   diagnostic definition rather than a surface temperature.
3. **Derive** the equilibrium temperature and the relaxation time of a
   zero-dimensional energy-balance model with a linear outgoing-longwave law.
4. **Construct** a one-dimensional (latitudinally resolved) energy-balance model
   with a diffusion closure, and **verify** that it conserves the global mean
   against the zero-dimensional result.
5. **Quantify** what each level of the hierarchy can and cannot constrain, and
   **identify** the closure each level introduces.
6. **Explain** why a trivial model is still useful: it isolates one mechanism
   whose response can be checked independently.
7. **State** the structural uncertainty that survives in even the simplest
   level of the hierarchy.

## Prerequisites

- [16-02-05 Zero- and One-Dimensional Energy Balance Models](../02-radiation-and-energy-balance/05-energy-balance-models.md) —
  the energy-balance idea and the linear outgoing-longwave parameterisation.
- [16-04-01 Components of the Climate System and Their Timescales](../04-climate-system-and-feedbacks/01-climate-system-components.md) —
  which reservoirs respond on which timescales.
- [16-04-03 Climate Sensitivity: Definitions and Estimation](../04-climate-system-and-feedbacks/03-climate-sensitivity.md) —
  the equilibrium response per unit forcing, used here as a model parameter.

## 1. Intuition: a hierarchy, not a ladder

Climate science is often described as if it had one goal model and a set of
toy predecessors. It is more useful to think of a **hierarchy**: a set of
models, each of which answers a different question exactly, and none of which
answers every question. The right level is the one whose missing physics does
not matter for the question being asked.

Three practical reasons make the hierarchy the organising principle of this
module rather than a historical footnote:

- **A simple model can be checked.** The global mean of a one-dimensional model
  must equal the zero-dimensional answer when the transport operator conserves
  area. That is a test that a full model cannot pass, because a full model has
  no closed-form answer to compare against. Simple models are how we verify
  that our *reasoning* is consistent.
- **Mechanisms are isolated.** If you want to know how much a step in the solar
  constant changes the global mean, a one-dimensional model will tell you the
  diffusive part of the answer without clouds confusing the attribution.
- **Cost buys coverage.** Cheap models can be run thousands of times — for
  calibration, for ensembles, for exploring uncertainty. That is the subject of
  [06 Emulators and Surrogate Models](06-emulation-and-surrogates.md).

The price of simplicity is always the same: a closure. A closure is a
replacement for physics the model does not carry (Section 5).

## 2. Precise definitions: classifying by state and closure

A model is defined by its **prognostic state** (what it carries forward in
time), its **resolved processes**, and its **closures** (the empirical or
parametric rules that stand in for unresolved processes).

| Level | Example class | Prognostic state | Direction of the budget considered | Principal closure |
|---|---|---|---|---|
| 0-D blackbody | diagnostic | none | global, top-of-atmosphere | none (definition) |
| 0-D EBM | EBM | $T(t)$, one number | global | $F_{\text{out}}=A+BT$ |
| 1-D EBM | EBM | $T(x,t)$, $x=\sin\varphi$ | latitude | diffusivity $D$ |
| 2-D/3-D dynamics | EMIC, GCM | $T,\mathbf{u},q,\ldots$ | spherical | diffusive/eddy, cloud, convection |
| Earth system | ESM | the above $+$ carbon, ice, chemistry | spherical | biogeochemistry, ice flow |

The abbreviations are conventional: **EBM** energy-balance model, **EMIC**
Earth-system model of intermediate complexity, **GCM** general circulation model,
**ESM** Earth-system model. The names matter much less than the table. Two
models with the same name from different centres may differ in state variables,
so *classify by state and closure, not by label*.

A useful heuristic: a model can resolve features larger than roughly four of its
grid spacings. Everything smaller is sub-grid and must be closed. As resolution
increases, the closed part shrinks — it never disappears
(see [02 GCMs, Resolution and Parameterisation](02-gcms-and-parameterisation.md)).

## 3. The zero-dimensional model, derived in three steps

### 3.1 Absorption and the effective radiating temperature

Let $S$ be the total solar irradiance (the solar constant, taken here as the
standard value $S = 1361\ \mathrm{W\,m^{-2}}$) and $\alpha$ the planetary
albedo. A sphere intercepts $\pi R^{2}$ of the beam and radiates from $4\pi
R^{2}$, so the absorbed flux per unit area is

$$F_{\text{abs}} = \frac{S(1-\alpha)}{4}.$$

Requiring a blackbody to emit exactly this,

$$\sigma T_{\text{eff}}^{4} = F_{\text{abs}}
\qquad\Longrightarrow\qquad
T_{\text{eff}} = \left[\frac{S(1-\alpha)}{4\sigma}\right]^{1/4},$$

with $\sigma = 5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$. With
$\alpha = 0.30$ the demonstration prints

$$F_{\text{abs}} = 238.17\ \mathrm{W\,m^{-2}},\qquad
T_{\text{eff}} = 254.58\ \mathrm{K} = -18.57\ \mathrm{{}^{\circ}C}.$$

This is **not** a surface temperature. It is the emission temperature that a
blackbody would need in order to balance the absorbed flux. It is a definition,
and it is exact given $S$ and $\alpha$.

### 3.2 A linear outgoing-longwave law

The next step replaces the blackbody by a *parameterisation* of what the
top-of-atmosphere actually emits:

$$F_{\text{out}} = A + B\,T,$$

with $A$ and $B$ constants. In the demonstration $A = 210\
\mathrm{W\,m^{-2}}$ and $B = 2.0\ \mathrm{W\,m^{-2}\,K^{-1}}$, chosen so that the
model reproduces a plausible global mean; these are **teaching values**, not
fitted measurements. The $A$ term is what makes the model "warm": a blackbody at
$T_{\text{eff}}$ emits $238.17\ \mathrm{W\,m^{-2}}$, whereas $A+BT$ at
$T = 14.09\ \mathrm{{}^{\circ}C}$ also emits $210 + 2.0\times14.09 = 238.17\
\mathrm{W\,m^{-2}}$. The difference between the two temperatures,
$14.09 - (-18.57) = 32.66\ \mathrm{K}$ in this model, is the model's *implied*
greenhouse warming. It is a consequence of the chosen $A$, not a measurement.

### 3.3 Equilibrium and timescale

With a heat capacity $C$ per unit area,

$$C\frac{\mathrm{d}T}{\mathrm{d}t}
= \frac{S(1-\alpha)}{4} - A - BT
\qquad\Longrightarrow\qquad
T(t) = T_{0} + (T(0)-T_{0})e^{-t/\tau},$$

$$T_{0} = \frac{F_{\text{abs}}-A}{B},\qquad \tau = \frac{C}{B}.$$

The demonstration prints $T_{0} = 14.09\ \mathrm{{}^{\circ}C}$ and, taking
$C = 5.0\ \mathrm{W\,yr\,m^{-2}\,K^{-1}}$, a relaxation time
$\tau = 2.50\ \mathrm{yr}$. The two numbers measure different things: $T_{0}$ is
the equilibrium, $\tau$ is how long the system remembers a perturbation. A step
forcing $F$ produces an equilibrium warming $F/B = 1.85\ \mathrm{K}$ for
$F = 3.7\ \mathrm{W\,m^{-2}}$.

The quantity $1/B$ is the feedback parameter and $F/B$ is the equilibrium
response, exactly the
[climate sensitivity](../04-climate-system-and-feedbacks/03-climate-sensitivity.md)
of this model. Because $B$ is a closure coefficient, the sensitivity is a
property of the closure; the hierarchy does not remove that dependence.

## 4. One dimension: latitude and a diffusion closure

### 4.1 The equation

Let $x = \sin\varphi$ (so area is uniform in $x$) and let $T(x,t)$ be the zonal
mean temperature. The budget becomes

$$C\frac{\partial T}{\partial t}
= D\frac{\partial}{\partial x}\left[(1-x^{2})\frac{\partial T}{\partial x}\right]
+ Q_{0}\,S(x)\bigl(1-\alpha\bigr) - A - BT,$$

where $Q_{0} = S/4$, $S(x)$ is a synthetic insolation shape of unit mean and
$D$ is a diffusivity with units $\mathrm{W\,m^{-2}\,K^{-1}}$. The factor
$(1-x^{2})$ makes the transport operator regular at the poles and gives zero
heat flux through them.

### 4.2 The conservation check

Integrate the transport term over $x\in[-1,1]$:

$$\int_{-1}^{1}\frac{\partial}{\partial x}\left[(1-x^{2})\frac{\partial T}{\partial x}\right]\mathrm{d}x
= \left[(1-x^{2})\frac{\partial T}{\partial x}\right]_{-1}^{+1} = 0,$$

since $(1-x^{2})=0$ at both ends. **Transport redistributes heat; it cannot
create or destroy it.** Therefore the area-weighted global mean of the 1-D
steady state must equal the 0-D equilibrium for the same albedo. The
demonstration finds

$$14.088\ \mathrm{{}^{\circ}C}\ \text{(1-D)}\quad\text{versus}\quad
14.087\ \mathrm{{}^{\circ}C}\ \text{(0-D)},\qquad \text{difference } +0.0000\
\mathrm{K}.$$

This is the kind of check that a full model cannot perform, and it is the main
reason to keep the simple level in the toolbox.

With $D = 0.6\ \mathrm{W\,m^{-2}\,K^{-1}}$ and a synthetic insolation shape, the
steady state is $27.71\ \mathrm{{}^{\circ}C}$ at the equator and
$-14.67\ \mathrm{{}^{\circ}C}$ at the pole, an equator-minus-pole contrast of
$42.38\ \mathrm{K}$. Only the *contrast* is new information relative to the 0-D
model; the mean is not.

### 4.3 A feedback on top

Adding a step-function ice albedo — $0.30$ where $T > -10\
\mathrm{{}^{\circ}C}$, $0.62$ elsewhere — gives $11.0\%$ of the latitude points
ice-covered and lowers the global mean to $11.24\ \mathrm{{}^{\circ}C}$,
i.e. by $2.84\ \mathrm{K}$ relative to the no-feedback run. That is the
ice-albedo feedback acting at the level of a global mean. The size of the effect
is set by the *chosen* threshold and albedo contrast; see
[03 Abrupt Climate Change and Tipping Elements](../06-palaeoclimate/03-abrupt-climate-change.md)
for what happens when that feedback is strong enough to create several
equilibria.

## 5. What each level adds, and what it hides

| Level | New state | New closure | Question it can answer |
|---|---|---|---|
| 0-D blackbody | — | none | how much flux must be emitted |
| 0-D EBM | $T$ | $A$, $B$ | global mean and response time |
| 1-D EBM | $T(x)$ | $D$ | pole–equator contrast |
| GCM/ESM | $\mathbf{u},q,T(x,y,z)$ | convection, cloud, boundary layer, microphysics | regional structure, storms, circulation |

Three of these deserve emphasis:

- **Diffusion is a closure.** The 1-D model does not simulate eddies; it assumes
  that their net effect is down-gradient transport with a constant
  coefficient. Real heat transport is not Fickian at these scales, and $D$
  is not a property of the atmosphere.
- **The $A$ and $B$ coefficients are closures.** They encode the greenhouse
  effect, water-vapour feedback and cloud response in two numbers.
- **Parameterised processes disagree between models.** The disagreement is not
  an implementation bug; it is the structural uncertainty of the closure
  (see [05 CMIP, Model Intercomparison and Ensemble Design](05-coupled-model-intercomparison.md)).

## 6. Worked example: three numbers from the 0-D model

*Given* $S = 1361\ \mathrm{W\,m^{-2}}$, $\alpha = 0.30$,
$A = 210\ \mathrm{W\,m^{-2}}$, $B = 2.0\ \mathrm{W\,m^{-2}\,K^{-1}}$,
$C = 5.0\ \mathrm{W\,yr\,m^{-2}\,K^{-1}}$, and a step forcing
$F = 3.7\ \mathrm{W\,m^{-2}}$:

1. $F_{\text{abs}} = 1361(1-0.30)/4 = 238.17\ \mathrm{W\,m^{-2}}$.
2. $T_{\text{eff}} = (238.17/5.670374419\times10^{-8})^{1/4}
   = 254.58\ \mathrm{K} = -18.57\ \mathrm{{}^{\circ}C}$.
3. $T_{0} = (238.17-210)/2.0 = 14.09\ \mathrm{{}^{\circ}C}$.
4. $\tau = C/B = 5.0/2.0 = 2.50\ \mathrm{yr}$, and $F/B = 1.85\ \mathrm{K}$.

*Interpretation.* If the analyst changes $B$ from $2.0$ to
$2.5\ \mathrm{W\,m^{-2}\,K^{-1}}$ — that is, strengthens the restoring — the
equilibrium warming from the same forcing falls from $1.85$ to $1.48\
\mathrm{K}$, a $20\%$ reduction, while $T_{0}$ changes to
$(238.17-210)/2.5 = 11.27\ \mathrm{{}^{\circ}C}$. Both changes come from a
coefficient that is a closure. This is the honest statement of the hierarchy:
even the simplest reliable model has one number that is chosen, and its output
is conditional on it.

## 7. Assumptions and regime of validity

1. **Global and annual mean.** The 0-D model has no geography, no seasons and
   no diurnal cycle. It is valid for questions phrased as global means over
   periods long compared with the relaxation time.
2. **Linear outgoing longwave radiation.** $F_{\text{out}} = A+BT$ is a
   linearisation; it is accurate over the small range of $T$ the model is used
   for, and fails for large excursions (Section 4.3 already shows one).
3. **A single, constant heat capacity.** The $C$ used here is an effective
   mixed-layer value. The real system has a fast atmosphere-plus-mixed-layer
   component and a slow ocean, so a single exponential is an approximation.
4. **Fixed albedo, or a prescribed albedo rule.** $\alpha$ is not predicted; it
   is given. A cloud change is therefore invisible unless it is written into the
   albedo rule.
5. **No dynamics.** There is no circulation in the 0-D model, hence no
   advection of heat, moisture or momentum. The 1-D model adds a diffusion
   closure, not dynamics.
6. **Diagnostic versus prognostic temperature.** $T_{\text{eff}}$ is diagnostic;
   $T$ in the EBM is prognostic. Conflating them is the commonest error with
   this model (Section 9).

## 8. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| irradiance | $S$ | $\mathrm{W\,m^{-2}}$ | |
| absorbed flux | $F_{\text{abs}}$ | $\mathrm{W\,m^{-2}}$ | $S(1-\alpha)/4$, dimensionless factor |
| OLR coefficients | $A$, $B$ | $\mathrm{W\,m^{-2}}$, $\mathrm{W\,m^{-2}\,K^{-1}}$ | $A+BT$ is a flux |
| heat capacity | $C$ | $\mathrm{W\,yr\,m^{-2}\,K^{-1}}$ | so $C/B$ is in years |
| diffusivity | $D$ | $\mathrm{W\,m^{-2}\,K^{-1}}$ | so $D\,\partial_{x}[(1-x^{2})\partial_{x}T]$ is a flux |

The last row is worth checking explicitly: $(1-x^{2})$ is dimensionless, each
$\partial_{x}$ carries the unit of $x^{-1}$ (dimensionless, since $x=\sin\varphi$),
so the operator returns kelvin, and $D$ supplies the flux unit.

## 9. Python demonstration

[`code/climate_model_hierarchy_demo.py`](code/climate_model_hierarchy_demo.py)
performs the whole calculation and prints labelled results with units. It:

1. computes $T_{\text{eff}}$ from the absorbed flux and prints every constant;
2. solves the 0-D EBM for $T_{0}$, $\tau$ and the step response;
3. time-steps the 1-D EBM to steady state with an implicit scheme, prints the
   latitude profile and verifies the global-mean conservation against the 0-D
   answer to round-off;
4. repeats the 1-D run with the ice-albedo feedback and reports the change in
   global mean and the ice-covered fraction;
5. prints the hierarchy table so the assumptions are visible next to the
   numbers.

The demonstration is print-only, uses the fixed seed
`np.random.default_rng(20261014)`, and takes well under a second.

## 10. Exercises

Full problem sets with worked solutions are in
[`exercises/01-climate-model-hierarchy-exercises.md`](exercises/01-climate-model-hierarchy-exercises.md)
and [`exercises/01-climate-model-hierarchy-solutions.md`](exercises/01-climate-model-hierarchy-solutions.md).
The exercises ask you to redo the derivations with different coefficients, to
show that the conservation check is exact, and to design a hierarchy study.

## Mastery checkpoint

Complete this without notes.

> A planet has $S = 1361\ \mathrm{W\,m^{-2}}$, $\alpha = 0.30$. Its atmosphere is
> represented by $F_{\text{out}} = A+BT$ with $A = 210\
> \mathrm{W\,m^{-2}}$, $B = 2.0\ \mathrm{W\,m^{-2}\,K^{-1}}$.
> **(a)** Compute $T_{\text{eff}}$ and the EBM equilibrium $T_{0}$, and state in
> one sentence why they differ.
> **(b)** With $C = 5.0\ \mathrm{W\,yr\,m^{-2}\,K^{-1}}$, compute $\tau$ and the
> time to reach $90\%$ of the equilibrium response to a step forcing.
> **(c)** A 1-D version of the same model reports a global mean $0.4\
> \mathrm{K}$ *lower* than your $T_{0}$. Give two possible reasons and say which
> is a numerical error and which is physics.
> **(d)** State one question the 0-D model can answer and one it cannot.

## Common pitfalls

1. **Reporting $T_{\text{eff}}$ as a surface temperature.** It is the emission
   temperature of a blackbody; the model's surface temperature is $T_{0}$.
   Confusing them makes the "greenhouse effect" look like a fudge rather than a
   consequence of $A$ and $B$.
2. **Treating $A$ and $B$ as measured constants.** They are closures. A model
   with different values has a different sensitivity.
3. **Assuming transport changes the global mean.** It cannot. If a 1-D run does
   not conserve the global mean, either the boundary treatment is wrong or the
   time step has not converged.
4. **Reading a hierarchy as a progression towards "the truth".** A GCM is not a
   more correct EBM; it answers different questions at a different cost.
5. **Forgetting that resolution does not remove closures.** A finer grid moves
   the closure boundary; it does not delete the closure.

## Related modules

- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  where the absorbed flux and the greenhouse effect are derived properly.
- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  the sensitivity this model parameterises.
- [16-06 Palaeoclimate](../06-palaeoclimate/README.md) — the same models used
  against proxy records.
- [19-01 Numerical Foundations for Simulation](../../19-numerical-modeling-hpc/01-numerical-foundations/README.md) —
  discretisation, convergence and stability, which the 1-D solve assumes.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  the systematic treatment of the structural uncertainty raised here.
