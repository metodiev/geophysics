---
id: 19-08-05
title: "Running a Simple Climate Model"
level: research
prereqs: ["19-07-02", "19-07-03", "16-02-05"]
tags: [numerical-modelling, verification, climate-model, energy-balance, feedback, calibration]
---

# Running a Simple Climate Model

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the zero-dimensional energy-balance equilibrium temperature and the
   one-layer grey-atmosphere surface temperature.
2. **Verify** a time-integrated relaxation against the exact exponential decay and
   **measure** the time constant against the analytic $C/B$.
3. **Verify** a one-dimensional diffusive energy-balance solver against a
   manufactured solution and **measure** its order.
4. **Compute** the equilibria of a model with an ice-albedo feedback and
   **demonstrate** that the number of equilibria changes with the solar constant.
5. **Explain** why a simple climate model is calibrated rather than validated, and
   **state** precisely what claim about an unused observable would be defensible.
6. **State** which physical processes a model of this class cannot represent, and
   what a model higher in the hierarchy would add.

## Prerequisites

- [19-07-02 Solution Verification](../07-verification-validation-uncertainty/02-solution-verification.md)
  and [19-07-03 Model Validation](../07-verification-validation-uncertainty/03-model-validation.md)
  — the two standards applied to a model whose parameters are chosen.
- [16-02-05 Zero- and One-Dimensional Energy Balance Models](../../16-atmosphere-climate/02-radiation-and-energy-balance/05-energy-balance-models.md)
  — the climate-science treatment of the same models.

All models in this module are **SYNTHETIC teaching models**. The solar constant
and the Stefan-Boltzmann constant are standard physical constants and are used as
anchors; every albedo, heat capacity, feedback parameter, threshold and forcing
below is a **chosen** value, and no model result here is claimed to describe the
real climate.

## 1. Intuition: the simplest model that can be wrong in an interesting way

The zero-dimensional energy-balance model says that a planet absorbs solar
radiation over its cross-section and radiates over its whole surface:

$$(1-\alpha)\frac{S_0}{4} = \sigma T^{4}.$$

One line, one unknown, and a closed-form answer. Its value is not accuracy — it is
that every ingredient is visible. You can see that the factor $4$ is geometry, that
$\alpha$ is a *chosen* albedo, that $T$ is an *effective* radiating temperature
rather than a surface temperature, and that the greenhouse effect has been left
out. Adding a single absorbing layer introduces the greenhouse effect in the same
transparent way, and it immediately shows why one layer cannot work: the emissivity
needed to reach a realistic surface temperature is not the emissivity of anything
real.

That transparency is the point of a simple climate model, and it is also the reason
such a model cannot be validated. Its parameters are calibrated to reproduce a
target, its feedbacks are functions invented to behave plausibly, and the model has
no independent record to be tested against in this course. **What can be
established rigorously is everything about its numerical behaviour**: the exact
equilibria, the exact relaxation time, the order of a discretisation, and the
structure of its multiple steady states. The demonstration does exactly that, and
then states plainly what it has not established.

The last theme is non-uniqueness, which appears here as *multiple equilibria*: with
an ice-albedo feedback the same solar constant can support a snowball state, an
intermediate state and a warm state, and the set of states changes discontinuously
as the solar constant varies. A model that reports "the equilibrium temperature"
without reporting which branch it converged to has reported one of several answers.

## 2. Definitions

**Energy-balance model (EBM).** A model in which the only physics is a radiative
balance, possibly with a diffusive transport term representing heat transport by
atmosphere and ocean.

**Effective radiating temperature $T_e$.** The temperature of a black body emitting
the absorbed flux: $T_e = ((1-\alpha)S_0/4\sigma)^{1/4}$.

**Grey atmosphere.** A single layer that absorbs and emits a fraction $\varepsilon$
of radiation, transparent everywhere else.

**Feedback parameter $B$.** The coefficient in the linearised outgoing-radiation
relation $F_{\text{out}} = A + BT$; the equilibrium response to a forcing
$\Delta F$ is $\Delta T = \Delta F/B$.

**Ice-albedo feedback.** A temperature-dependent albedo with a high value when cold
(ice) and a low value when warm (open water), which makes the radiative balance
nonlinear and multivalued.

**Calibration versus evaluation.** Fitting parameters to a target record and then
reporting agreement with that record is calibration; comparison with an *unused*
observable is evaluation and is the strongest claim such a model can earn.

## 3. Derivations

### 3.1 Zero-dimensional equilibrium

Balance absorbed solar flux against emitted radiation with the geometry factor $1/4$
(the absorbed flux is spread over $4\pi R^2$ while the intercepting area is
$\pi R^2$):

$$T = \left(\frac{(1-\alpha)S_0}{4\sigma}\right)^{1/4}.$$

With $S_0 = 1361$ W m$^{-2}$ and $\alpha = 0.30$ this is $254.6$ K, and the outgoing
flux is $\sigma T^{4} = 238.2$ W m$^{-2}$ by construction — the model cannot
contradict itself.

### 3.2 One layer, and why it is not the atmosphere

A single grey layer at temperature $T_a$ absorbs all the surface radiation
(fraction $\varepsilon$) and emits $\varepsilon\sigma T_a^{4}$ upward and the same
downward. At equilibrium the layer's flux balance and the surface balance give

$$T_s = T_e\left(\frac{2}{2-\varepsilon}\right)^{1/4}.$$

For $\varepsilon = 1$ the surface is $T_e\,2^{1/4} = 302.8$ K; for the $\varepsilon$
that reproduces $288$ K it is $0.779$. That number is a *calibration*: it is what
the single layer must be to mimic many absorbing layers, and it is not the
emissivity of any gas.

### 3.3 Relaxation time

For $C\,\mathrm{d}T/\mathrm{d}t = F - BT$, the departure from equilibrium decays as
$e^{-t/\tau}$ with $\tau = C/B$ exactly. The demonstration measures $\tau$ by
time-integrating and fitting, which verifies the integrator against the analytic
solution and gives the physical statement: **an equilibrium statement is only
meaningful once the run is long compared with $C/B$.**

### 3.4 The one-dimensional diffusive model

Adding diffusive transport with a coefficient $D$ that vanishes at the poles (no
flux through the pole in a latitude coordinate $y = \sin(\text{latitude})$):

$$D\frac{\mathrm{d}}{\mathrm{d}y}\left[(1-y^{2})\frac{\mathrm{d}T}{\mathrm{d}y}\right]
+ Q(y) - \left(A + BT\right) = 0 .$$

For a verification test one manufactures $T(y) = 1 + 0.5y^{2}$ and solves for the
source:

$$Q(y) = A + BT_m - D(1 - 3y^{2}),$$

which is exact. Substituting back gives a *discrete* residual of order $h^{2}$, and
the measured order is the code's.

### 3.5 Multiple equilibria

With a smooth ice-albedo feedback $\alpha(T)$ the balance
$(1-\alpha(T))S_0/4 = \sigma T^{4}$ is a nonlinear algebraic equation. Its roots
are the equilibria, and the sign of the residual tells you which way the
temperature would move. Because a cold state has a high albedo and therefore a
lower equilibrium temperature, the equation can have **three** roots: two stable
(snowball and warm) and one unstable between them. Changing $S_0$ moves the roots
and can destroy a pair of them — the mechanism behind the hysteresis that Section 5
measures and that makes the answer depend on the path, not only on the parameters.

## 4. Assumptions and regime of validity

1. **Radiative equilibrium only, or radiative plus diffusive transport.** No
   dynamics, no clouds as a prognostic field, no carbon cycle, no ocean heat
   uptake structure.
2. **A grey atmosphere.** Real absorption is spectrally selective; the
   single-layer model's $\varepsilon$ is an effective parameter, not a gas property.
3. **A chosen albedo function.** The threshold and width of the ice-albedo
   transition determine the hysteresis, and they are parameters.
4. **A chosen heat capacity.** $C$ controls the transient and the timescale, and
   it is chosen to be large enough to be plausible, not measured.
5. **A linearised feedback.** $F_{\text{out}} = A + BT$ is a local linearisation
   of the outgoing radiation; it fails for large departures from the calibration
   state.
6. **What is not established.** Anything about the real climate. A model of this
   class can be verified against its own arithmetic, and it can be *evaluated*
   against an unused observable once someone measures one; it cannot be validated
   by the data it was tuned to
   ([16-05-03 Model Evaluation, Skill and Benchmarking](../../16-atmosphere-climate/05-climate-models/03-model-evaluation.md)).

## 5. Measured evidence

The demonstration `code/simulate_climate_model_demo.py` runs in about $0.3$ s.

### 5.1 Exact zero-dimensional equilibria

Standard constants $S_0 = 1361$ W m$^{-2}$, $\sigma = 5.670374419\times10^{-8}$
W m$^{-2}$K$^{-4}$; chosen albedos:

| albedo | equilibrium $T$ (K) | outgoing flux (W m$^{-2}$) |
|---:|---:|---:|
| 0.10 | 271.09 | 306.2 |
| 0.30 | 254.58 | 238.2 |
| 0.62 | 218.52 | 129.3 |

### 5.2 The one-layer grey atmosphere

$T_e = 254.58$ K at $\alpha = 0.30$:

| $\varepsilon$ | surface $T$ (K) |
|---:|---:|
| 0.00 | 254.58 |
| 0.50 | 273.56 |
| 0.77 | 287.48 |
| 0.90 | 295.62 |
| 1.00 | 302.75 |

The emissivity that reproduces $288$ K is $0.7790$. **A single layer needs an
emissivity of $0.78$ to be a stand-in for the real atmosphere, and that number is
the model's calibration, not a measurement.**

### 5.3 Relaxation against the exact time constant

$C = 1.0\times10^{8}$ J m$^{-2}$K$^{-1}$ and $B = 1.2$ W m$^{-2}$K$^{-1}$ (both
chosen): the exact time constant is $C/B = 8.3333\times10^{7}$ s $= 2.641$ years,
and the time-integrated fit gives $8.3321\times10^{7}$ s, $0.015$ per cent from the
analytic value. The integrator is verified; the timescale is a property of two
chosen parameters.

### 5.4 The one-dimensional model against a manufactured solution

| $N$ | $\Delta y$ | max error | order |
|---:|---:|---:|---:|
| 16 | 0.12500 | $1.6032\times10^{-3}$ | — |
| 32 | 0.06250 | $4.1633\times10^{-4}$ | 1.945 |
| 64 | 0.03125 | $1.0681\times10^{-4}$ | 1.963 |
| 128 | 0.01562 | $2.7205\times10^{-5}$ | 1.973 |
| 256 | 0.00781 | $6.8978\times10^{-6}$ | 1.980 |

The measured orders approach the design order $2$ from below, the residual being
the higher-order term of a variable-coefficient stencil. This is the *only* way to
know the order: no observational record can tell you whether a discretisation is
second order.

### 5.5 Multiple equilibria and hysteresis

Chosen albedo transition: from $0.62$ (cold) to $0.30$ (warm), centred on $250$ K
with width $2$ K. At $S_0 = 1361$ W m$^{-2}$ the model has **three** equilibria:

| $T$ (K) | albedo | residual (W m$^{-2}$) |
|---:|---:|---:|
| 218.52 | 0.6200 | $0.0$ |
| 251.89 | 0.3291 | $8.5\times10^{-14}$ |
| 254.56 | 0.3002 | $-2.8\times10^{-14}$ |

As the solar constant falls the upper pair merges and disappears:

| $S_0$ (W m$^{-2}$) | number of equilibria | temperatures (K) |
|---:|---:|---|
| 1440 | 3 | 221.6, 251.0, 258.2 |
| 1361 | 3 | 218.5, 251.9, 254.6 |
| 1300 | 1 | 216.0 |
| 1250 | 1 | 213.9 |
| 1200 | 1 | 211.7 |
| 1000 | 1 | 202.3 |

Scanning $1$ W m$^{-2}$ at a time, the last solar constant with three equilibria
lies between $1337$ and $1338$ W m$^{-2}$. **One equation, three answers, and a
discontinuous change in the number of answers** — which is the honest form of the
statement that a simple climate model's equilibrium is not a single number.

### 5.6 What calibration does to a sensitivity

$\Delta T = \Delta F/B$ with a chosen forcing $\Delta F = 3.0$ W m$^{-2}$:

| $B$ (W m$^{-2}$K$^{-1}$) | $\Delta T$ (K) |
|---:|---:|
| 1.0 | 3.000 |
| 1.2 | 2.500 |
| 1.4 | 2.143 |
| 2.0 | 1.500 |

A $40$ per cent change in the feedback parameter moves the answer by $40$ per
cent. Both $\Delta F$ and $B$ are inputs; neither is measured here; and the model
has no observational record against which to check them. **An equilibrium
temperature from a zero-dimensional model is an arithmetic consequence of its
parameters.**

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| solar constant | $S_0$ | W m$^{-2}$ | $1361$ |
| Stefan-Boltzmann constant | $\sigma$ | W m$^{-2}$K$^{-4}$ | $5.670374419\times10^{-8}$ |
| albedo | $\alpha$ | dimensionless | 0 to 1 |
| temperature | $T$ | K | |
| heat capacity | $C$ | J m$^{-2}$K$^{-1}$ | chosen |
| feedback parameter | $B$ | W m$^{-2}$K$^{-1}$ | chosen |
| time constant | $\tau = C/B$ | s | J m$^{-2}$K$^{-1}$ / (W m$^{-2}$K$^{-1}$) |
| diffusivity | $D$ | W m$^{-2}$K$^{-1}$ | chosen |
| forcing | $\Delta F$ | W m$^{-2}$ | chosen |

The unit check that matters most: $C/B$ must come out in seconds, which it does
because a joule per watt is a second. If a time constant comes out in years
directly, a year-to-second conversion has been assumed rather than performed.

## 7. Worked examples

### Example 1 — the effective temperature by hand

With $\alpha = 0.30$ and $S_0 = 1361$ W m$^{-2}$:

$$\frac{(1-\alpha)S_0}{4} = \frac{0.70\times1361}{4} = 238.175\ \mathrm{W\,m^{-2}},$$

$$T = \left(\frac{238.175}{5.670374419\times10^{-8}}\right)^{1/4}
= \left(4.2003\times10^{9}\right)^{1/4} = 254.58\ \mathrm{K}.$$

The fourth root is worth doing once by two square roots: $\sqrt{4.2003\times10^{9}}
= 6.4809\times10^{4}$, $\sqrt{6.4809\times10^{4}} = 254.58$ ✓.

### Example 2 — the emissivity that reproduces 288 K

Solving $288 = T_e(2/(2-\varepsilon))^{1/4}$ for $\varepsilon$:

$$\frac{2}{2-\varepsilon} = \left(\frac{288}{254.58}\right)^{4} = 1.6379
\;\Longrightarrow\; 2-\varepsilon = 1.2211 \;\Longrightarrow\; \varepsilon = 0.7789 .$$

The demonstration's numerical search gives $0.7790$: agreement to $10^{-4}$ in
$\varepsilon$, which is the check that the search is doing what the algebra says. It
also illustrates the general point of a hand calculation beside a numerical one —
the algebra fixes the value, and the code reproduces it.

### Example 3 — the relaxation time in years

$$C/B = \frac{1.0\times10^{8}}{1.2} = 8.3333\times10^{7}\ \mathrm{s}
= \frac{8.3333\times10^{7}}{3.15576\times10^{7}} = 2.641\ \mathrm{years}.$$

A simulation of this model must run for tens of years of model time before its
temperature is an equilibrium statement, and the demonstration's forced-ODE test
runs for $6\tau$ to make the fit reliable. **The cost of an equilibrium claim is set
by $C/B$, not by the time step.**

### Example 4 — a statement about a simple climate model

> The model is a one-dimensional energy balance with a diffusive transport term, a
> linearised outgoing-radiation relation with chosen $A$ and $B$, and a chosen
> ice-albedo transition. Its discretisation is second order in $\Delta y$ (measured
> orders $1.95$ to $1.98$, Section 5.4); its time integration reproduces the exact
> $C/B$ to $0.015$ per cent (Section 5.3); its equilibria are computed to machine
> precision (Section 5.5). Its parameters are calibrated, not measured, and the
> model has not been evaluated against any observational record in this course. No
> statement about the Earth's climate is made or supported.

## 8. Python demonstration

```bash
cd 19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulate_climate_model_demo.py
```

Print-only, no file output, no network, exits 0.

## 9. Exercises

[`exercises/05-simulate-climate-model-exercises.md`](exercises/05-simulate-climate-model-exercises.md)
and
[`exercises/05-simulate-climate-model-solutions.md`](exercises/05-simulate-climate-model-solutions.md)
include computing equilibria, designing a manufactured solution that tests the
transport term, and writing the strongest defensible claim for a calibrated model.

## 10. Applications

- **Model hierarchies.** Energy-balance models are the bottom of the ladder whose
  top is a coupled Earth-system model; what they are good for is explaining
  mechanisms, and what they are not good for is prediction
  ([16-05-01 Model Hierarchy](../../16-atmosphere-climate/05-climate-models/01-climate-model-hierarchy.md)).
- **Conceptual mechanisms.** Ice-albedo hysteresis, snowball states and feedback
  amplification are all demonstrable in one line of algebra.
- **Calibration practice.** The model is a clean example of a system whose
  parameters are tuned to targets, and of the resulting limits on what agreement
  means ([16-04-03 Climate Sensitivity](../../16-atmosphere-climate/04-climate-system-and-feedbacks/03-climate-sensitivity.md)).
- **Teaching verification.** The same three tests — exact equilibrium, exact
  relaxation, manufactured solution — apply to any energy-balance code.

## 11. Further study

- [16-02-05](../../16-atmosphere-climate/02-radiation-and-energy-balance/05-energy-balance-models.md),
  [16-04-03](../../16-atmosphere-climate/04-climate-system-and-feedbacks/03-climate-sensitivity.md),
  [16-05-03](../../16-atmosphere-climate/05-climate-models/03-model-evaluation.md).
- [19-07-02](../07-verification-validation-uncertainty/02-solution-verification.md) and
  [19-07-03](../07-verification-validation-uncertainty/03-model-validation.md).
- [21-09-02 Honest Reporting of Uncertainty and Limitations](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/02-reporting-uncertainty-ethics.md).

## Mastery checkpoint

Without notes:

> A zero-dimensional energy-balance model has $S_0 = 1361$ W m$^{-2}$ and a chosen
> albedo of $0.30$. **(a)** Compute the equilibrium temperature and the outgoing
> flux. **(b)** Add a single grey layer with $\varepsilon = 0.8$ and compute the
> surface temperature; state what $\varepsilon$ would be needed for $288$ K and why
> that value is not a physical property. **(c)** The model is integrated with
> $C = 1\times10^{8}$ J m$^{-2}$K$^{-1}$ and $B = 1.3$ W m$^{-2}$K$^{-1}$: compute
> the time constant in years and state how long a run must be to support an
> equilibrium claim. **(d)** With an ice-albedo feedback the model has three
> equilibria at this solar constant; state which one a simulation started from a
> uniform $280$ K would find, and why the answer depends on the starting state.

Worked answers appear in
[`exercises/05-simulate-climate-model-solutions.md`](exercises/05-simulate-climate-model-solutions.md).

## Common pitfalls

1. **Reporting the effective temperature as a surface temperature.** It is the
   temperature of the outgoing radiation, not of the ground.
2. **Treating a fitted emissivity as a measurement.** The single-layer
   $\varepsilon = 0.78$ is a calibration for many absorbing layers.
3. **Quoting an equilibrium without stating the branch.** With feedbacks the
   equilibrium is one of several.
4. **Running shorter than the relaxation time.** An equilibrium claim needs
   $t \gg C/B$.
5. **Reading a sensitivity as a prediction.** $\Delta T = \Delta F/B$ is arithmetic
   on two chosen inputs.
6. **Describing a calibrated model as validated.** Only comparison with an unused
   observable earns the word
   ([19-07-03](../07-verification-validation-uncertainty/03-model-validation.md)).

## Related modules

- [19-08 Geophysical Simulation Case Studies](README.md) — the module that contains
  this lesson.
- [19-07 Verification, Validation and Numerical Uncertainty](../07-verification-validation-uncertainty/README.md).
- [16-atmosphere-climate](../../16-atmosphere-climate/README.md) — the climate
  science this model is a caricature of.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) — honest
  reporting of uncertainty.

## Self-assessment checklist

- [ ] I can derive the zero-dimensional equilibrium and the one-layer temperature.
- [ ] I can verify a relaxation integrator against $C/B$.
- [ ] I can write down and solve a manufactured solution for the transport term.
- [ ] I can find the equilibria of a model with an ice-albedo feedback.
- [ ] I can explain hysteresis and why it makes the answer path-dependent.
- [ ] I can state what a calibrated model may and may not claim.
