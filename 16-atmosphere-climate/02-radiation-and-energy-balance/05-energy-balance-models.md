---
id: 16-02-05
title: "Zero- and One-Dimensional Energy Balance Models"
level: graduate
prereqs: ["16-02-04", "16-02-02", "01-09-02"]
tags: [atmosphere, climate, energy-balance-model, feedback, diffusion, hysteresis, radiative-convective]
---

# Zero- and One-Dimensional Energy Balance Models

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the zero-dimensional energy balance model, **solve** it for the
   equilibrium temperature, and **derive** its relaxation time $C/\lambda$ from a
   heat capacity and a feedback parameter.
2. **Measure** the relaxation time by integrating the ODE and **explain** the
   residual difference from $C/\lambda$ in terms of the model's nonlinearity.
3. **Derive** the annual-mean insolation from the daily formula and **verify** that
   its area-weighted mean reproduces the geometric factor four.
4. **Write** the one-dimensional energy balance model with a diffusion
   parameterisation, **discretise** it as a finite-volume problem, and **prove**
   that its area-weighted mean temperature equals the zero-dimensional solution
   when the model is linear.
5. **Compute** the transport implied by the diffusion parameterisation and the
   transport required by the energy budget, and **explain** why their agreement is
   a consistency check rather than an independent test.
6. **Demonstrate** the ice-albedo bifurcation and hysteresis, and **state** which
   features are robust and which are artefacts of the chosen albedo function.
7. **Explain** why a purely radiative profile is unphysical and **quantify** the
   non-radiative flux that convective adjustment must carry.

## Prerequisites

- [04 Earth Energy Balance and Global Mean Temperature](04-earth-energy-balance.md) —
  the budgets these models solve, and the degeneracy they must break.
- [02 Radiative Transfer in the Atmosphere](02-radiative-transfer-atmosphere.md) —
  the grey radiative-equilibrium profiles used in §3.5.
- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md) —
  the diffusion operator and its boundary conditions.

> **All models and data in this module are SYNTHETIC.** $\sigma$, the solar
> constant and the water properties are standard constants. The reference
> temperature for the OLR linearisation, the diffusion coefficient, the mixed-layer
> depth, the albedo values and the ice threshold are **chosen inputs**, printed by
> the demonstration. No fitted OLR coefficient, published parameterisation or
> measured model output is used.

## 1. Intuition: the smallest model that can be wrong in an interesting way

An energy balance model (EBM) keeps the energy budget of
[04](04-earth-energy-balance.md) and throws away almost everything else. The
zero-dimensional version has one equation and one unknown:

$$C\frac{\mathrm{d}T}{\mathrm{d}t} = \frac{S(1-a)}{4} - \sigma T^4 .$$

It is *wrong* in almost every particular — it has no atmosphere, no geography, no
seasons and no dynamics — and yet it answers questions that a full model answers
only at vastly greater cost: How long does the system take to respond (the
relaxation time $C/\lambda = 1.69$ years for the model's $50\ \mathrm{m}$ mixed
layer)? How does the equilibrium temperature depend on a forcing (linearly, with
coefficient $1/\lambda$)? Is the response reversible?

Two extensions make it much more informative, and this lesson builds both.

**Geography.** Replace the single temperature by a latitude-dependent field $T(\phi)$
and represent the transport of energy by a diffusion term. That makes the model
*one-dimensional*, and it immediately produces a real result: the tropics warm
relative to the pole, and the model's own transport can be compared with the
transport the budget requires. The demonstration finds a peak transport of
$2.64\ \mathrm{PW}$ at $38.1^\circ$ for its chosen parameters.

**Nonlinearity.** Make the albedo depend on temperature (ice is bright) and the
model acquires *multiple equilibria*. The demonstration exhibits a hysteresis loop
between $S/S_0 = 1.30$ and about $1.55$: inside that range, whether the planet is
icy or not depends on where it started.

A third extension — **convective adjustment** — is what makes an EBM able to
reproduce a realistic surface temperature at all, and §3.5 quantifies why: the
grey radiative-equilibrium profile of [02](02-radiative-transfer-atmosphere.md)
puts the surface at $335\ \mathrm{K}$ for an optical depth of 4, which would require
the surface to export $324\ \mathrm{W\,m^{-2}}$ non-radiatively — more than the
planet absorbs. Convection is not a refinement of a radiative model; it is what
prevents the radiative model from being absurd.

## 2. Precise definitions

### 2.1 The zero-dimensional model and the feedback parameter

$$C\frac{\mathrm{d}T}{\mathrm{d}t} = F - \mathrm{OLR}(T),
\qquad F = \frac{S(1-a)}{4},$$

where $C$ is the **heat capacity per unit area** ($\mathrm{J\,m^{-2}\,K^{-1}}$).
Linearise the outgoing longwave radiation about a reference temperature $T_0$ (a
Taylor expansion, not a fit):

$$\mathrm{OLR}(T) = \sigma T_0^4 + 4\sigma T_0^3(T - T_0)
= A + BT,$$

$$A \equiv \sigma T_0^4 - 4\sigma T_0^3T_0 = -719.273\ \mathrm{W\,m^{-2}},
\qquad
B \equiv 4\sigma T_0^3 = 3.7609\ \mathrm{W\,m^{-2}\,K^{-1}}$$

at $T_0 = 255\ \mathrm{K}$. $B$ is the **feedback parameter** of the Planck response
([03 §3.3](03-greenhouse-effect.md)); the **relaxation time** of the linearised
model is

$$\tau \equiv \frac{C}{B} .$$

### 2.2 The one-dimensional model and the diffusion parameterisation

$$C\frac{\partial T}{\partial t} = Q(\phi)\left[1-a(\phi,T)\right] - \mathrm{OLR}(T)
+ D\frac{\partial}{\partial x}\left[(1-x^2)\frac{\partial T}{\partial x}\right],
\qquad x \equiv \sin\phi,$$

where $Q(\phi)$ is the annual-mean top-of-atmosphere insolation and $D$
($\mathrm{W\,m^{-2}\,K^{-1}}$) is a **chosen** diffusion coefficient. The operator
$(1-x^2)\partial_x$ is the spherical divergence of a downgradient flux in
$x$-coordinates, and $x$ is the natural coordinate because the area element is
$\cos\phi\,\mathrm{d}\phi = \mathrm{d}x$.

### 2.3 Ice-albedo feedback

$$a(\phi,T) = \begin{cases} a_{\text{warm}} & T \ge T_{\text{ice}} \\
a_{\text{ice}} & T < T_{\text{ice}}\end{cases}$$

This is a **positive** feedback: a colder surface is a brighter surface, which
absorbs less sunlight, which makes it colder. A positive feedback does not have to
destabilise anything — but it makes multiple equilibria possible.

### 2.4 Convective adjustment

A rule that resets any layer whose lapse rate exceeds the adiabatic value to the
adiabatic value, conserving energy, and then recomputes the radiative balance. The
result is a **radiative–convective equilibrium**. The rule is a modelling choice;
what is *not* a choice is that some such rule is needed (§3.5).

## 3. Derivations

### 3.1 The zero-dimensional model: equilibrium, relaxation, response

**Equilibrium.** Setting $\mathrm{d}T/\mathrm{d}t = 0$:

$$\sigma T_{\text{eq}}^4 = F
\;\Longrightarrow\;
T_{\text{eq}} = \left(\frac{S(1-a)}{4\sigma}\right)^{1/4}
= 254.578\ \mathrm{K} \quad (a = 0.30).$$

**Heat capacity.** For a mixed layer of depth $h$ of water,

$$C = \rho c_p h = 1000 \times 4000 \times 50 = 2.000\times10^{8}\
\mathrm{J\,m^{-2}\,K^{-1}}.$$

**Relaxation time.**

$$\tau = \frac{C}{4\sigma T_{\text{eq}}^3} = \frac{2.000\times10^{8}}{3.7423}
= 5.3444\times10^{7}\ \mathrm{s} = 1.69\ \mathrm{years}.$$

The demonstration integrates the ODE from $250\ \mathrm{K}$ and measures an
e-folding time of $5.4364\times10^{7}\ \mathrm{s} = 1.72\ \mathrm{years}$, i.e.
$+1.72\%$ longer than $\tau$. The difference is **not** numerical: $\tau$ is
evaluated with $4\sigma T^3$ at the equilibrium temperature, while along the
trajectory the feedback parameter is smaller (colder air radiates less per kelvin),
so the approach is slower. That is the model's nonlinearity showing up exactly
where the linearisation is stretched furthest.

**Linear response to a forcing.** Adding a forcing $\Delta F$ and linearising about
equilibrium:

$$C\frac{\mathrm{d}(\delta T)}{\mathrm{d}t} = \Delta F - B\,\delta T
\;\Longrightarrow\;
\delta T(\infty) = \frac{\Delta F}{B} .$$

**Note what $C$ does not do.** It appears only in the transient; the equilibrium
temperature is independent of it. That is the algebraic content of "a forcing is
not a temperature".

### 3.2 Annual-mean insolation, and a check on the factor four

Average the daily-mean formula of
[01 §3.5](01-solar-and-terrestrial-radiation.md) over a year, taking
$\sin\delta(t) = \sin\varepsilon\sin(2\pi t/\text{year})$:

$$Q(\phi) = \frac{1}{T_{\text{year}}}\int_0^{T_{\text{year}}}
\frac{S}{\pi}\left[h_0\sin\phi\sin\delta + \cos\phi\cos\delta\sin h_0\right]
\mathrm{d}t .$$

The demonstration evaluates this numerically and finds

| latitude | $Q$ (W m⁻²) |
|---|---|
| 0° | 415.54 |
| 45° | 307.46 |
| 90° | 172.33 |

**The check.** Because the area element is $\cos\phi\,\mathrm{d}\phi$, the
area-weighted mean is
$\int_0^{\pi/2}Q\cos\phi\,\mathrm{d}\phi / \int_0^{\pi/2}\cos\phi\,\mathrm{d}\phi
= \int_0^1 Q\,\mathrm{d}x$, which computes to $340.2490\ \mathrm{W\,m^{-2}}$
against $S/4 = 340.2500$. **Agreement to $0.0003\%$**: the latitude-dependent
insolation formula, integrated over the sphere, reproduces the geometric factor
four. That is a genuine check on both, and it is why $S/4$ is safe in a global
budget.

### 3.3 The one-dimensional model: discretisation and an exact property

**Finite-volume discretisation.** With $f(x) \equiv 1-x^2$ and a uniform grid in
$x$ of spacing $\Delta x$,

$$\frac{\partial}{\partial x}\left[f\frac{\partial T}{\partial x}\right]_i
\approx \frac{f_{i+1/2}(T_{i+1}-T_i) - f_{i-1/2}(T_i-T_{i-1})}{\Delta x^2},$$

with $f_{i\pm1/2} = 1 - \left(\frac{x_i+x_{i\pm1}}{2}\right)^2$. The boundary
conditions are **not imposed but arise**:

- at the equator, $f_{-1/2}$ multiplies the *symmetric* difference and is set to
  zero because $\partial T/\partial x = 0$ there by symmetry;
- at the pole, $f_{n-1/2} = 1 - 1^2 = 0$ automatically.

With the OLR linearised, the steady state is a **linear** system:

$$D\frac{\partial}{\partial x}\left[f\frac{\partial T}{\partial x}\right]
- BT = A - Q(x)\left[1-a\right],$$

which is solved exactly in the demonstration.

**The exact property.** Sum the discrete equations over all $i$. The diffusion
terms telescope and vanish (both boundary fluxes are zero), leaving

$$\sum_i\left(-BT_i - A + Q_i(1-a_i)\right) = 0
\;\Longrightarrow\;
\langle T\rangle = \frac{\langle Q(1-a)\rangle - A}{B},$$

where $\langle\cdot\rangle$ denotes the *uniform* average over the $x$ grid — which
is exactly the area-weighted average over the sphere. The demonstration confirms it
to $1.1\times10^{-10}\ \mathrm{K}$: $\langle T\rangle = 254.531378\ \mathrm{K}$.

$$\boxed{\;\text{For a linear EBM with energy-conserving transport, the
area-weighted mean temperature equals the zero-dimensional equilibrium exactly.}\;}$$

**The lesson in that identity.** *Redistributing* energy changes the pattern and not
the mean. A one-dimensional model with a fixed albedo therefore **cannot** change
the global mean temperature, however strong its transport is: the demonstration
confirms $\langle T\rangle = 254.531\ \mathrm{K}$ for $D = 0.3$, $0.6$, $1.2$ and
$2.4\ \mathrm{W\,m^{-2}\,K^{-1}}$, while the pole-to-equator contrast falls from
$31.7\ \mathrm{K}$ to $9.8\ \mathrm{K}$. Global-mean change requires either a
change in the forcing, a change in the *nonlinearity*, or a change in the
distribution that feeds back on the mean — which is exactly what §3.4 supplies.

### 3.4 The ice-albedo feedback: bifurcation and hysteresis

The dependence of $a$ on $T$ makes the steady-state problem nonlinear, and it is
solved by fixed-point iteration. The demonstration scans the solar constant:

| $S/S_0$ | ice edge (from ice-free) | equator $T$ (K) | pole $T$ (K) | mean (K) |
|---|---|---|---|---|
| 1.20 | frozen | 237.38 | 221.72 | 232.47 |
| 1.30 | frozen | 241.23 | 224.25 | 235.91 |
| 1.35 | $33.7^\circ$ | 280.55 | 232.66 | 262.72 |
| 1.40 | $45.8^\circ$ | 287.59 | 238.23 | 271.67 |
| 1.50 | $62.7^\circ$ | 296.74 | 249.08 | 283.27 |
| 1.60 | ice free | 304.56 | 266.08 | 292.50 |
| 1.80 | ice free | 318.72 | 275.43 | 305.16 |

and then compares the ice-free and frozen starting points at the same $S$:

| $S/S_0$ | from ice-free | from frozen |
|---|---|---|
| 1.30 | frozen | frozen |
| 1.40 | $45.8^\circ$ | frozen |
| 1.50 | $62.7^\circ$ | frozen |
| 1.60 | ice free | frozen |
| 1.80 | ice free | frozen |
| 2.00 | ice free | ice free |
| 2.50 | ice free | ice free |

**Read the second table.** Between $S/S_0 = 1.30$ and somewhere in
$(1.80, 2.00)$ **both branches exist**: the state depends on the history, not only
on the forcing. That is **hysteresis**, and it is the classic demonstration that a
nonlinear EBM supports multiple equilibria. Note also the *discontinuity* in the
first table — between $S/S_0 = 1.30$ and $1.35$ the mean temperature jumps by
$27\ \mathrm{K}$ — which is a **bifurcation**: the ice-free and frozen branches are
separate solutions and the system switches between them. The loop is closed when
the frozen branch becomes unstable and the planet jumps *up* to the ice-free state
between $1.80$ and $2.00$; the scan does not locate the upper bifurcation
precisely, and a bisection on the ice edge would be the way to do it.

**Three honest caveats, all of them model choices.**

1. This model needs a solar constant between about $30\%$ and $95\%$ **above** the
   standard value for the hysteresis loop to appear at all, because the OLR
   linearisation about $255\ \mathrm{K}$ and the chosen diffusion coefficient are
   not calibrated to the real Earth. **What the demonstration establishes is the
   structure of the bifurcation, not the location of any real threshold.**
2. The albedo is a **step** function. A smoother dependence on temperature narrows
   the hysteresis and eventually removes it, so the existence and width of the loop
   are properties of the *shape* of $a(T)$, not of the physics alone.
3. The frozen branch is a solution of a one-dimensional diffusive model with no
   ocean heat transport, no ice dynamics, no clouds and no seasonal cycle.

**Why the feedback can do this at all.** A positive feedback amplifies a
perturbation. Amplification alone does not create multiple equilibria — a linear
positive feedback just rescales the response — but combined with a *threshold* it
does. That is the general structure: threshold plus positive feedback gives
hysteresis, and the threshold here is the freezing point.

### 3.5 Why a radiative-only profile cannot be the answer

From [02 §3.5](02-radiative-transfer-atmosphere.md), the grey radiative-equilibrium
surface temperature rises with total infrared optical depth. Compare each with an
illustrative $288\ \mathrm{K}$ surface:

| radiative model | $T_s$ (K) | $\sigma T_s^4$ (W m⁻²) | excess over $288\ \mathrm{K}$ (W m⁻²) |
|---|---|---|---|
| one grey layer, $\varepsilon = 1$ | 302.746 | 476.35 | 86.24 |
| grey, $\tau_s = 4$ | 335.043 | 714.52 | 324.41 |
| grey, $\tau_s = 8$ | 380.681 | 1190.85 | 800.74 |

For $\tau_s = 4$ the surface would have to export $324\ \mathrm{W\,m^{-2}}$
non-radiatively — **more than the planet absorbs** ($238\ \mathrm{W\,m^{-2}}$),
which is impossible, since convection and evaporation carry energy *from* the
surface to the atmosphere and the atmosphere's own capacity to receive it is
bounded by what it can radiate. The excess is the **diagnostic of the failure**,
exactly as the sign test of [04 §3.3](04-earth-energy-balance.md) was.

**Convective adjustment.** The physical reason is that the radiative-equilibrium
lapse rate is steeper than adiabatic, so the profile is unstable
([16-01-03 §3.3](../01-atmospheric-structure-and-thermodynamics/03-thermodynamic-processes.md)).
The remedy is to impose

$$\Gamma = \min\left(\Gamma_{\text{rad}}, \Gamma_{\text{ad}}\right)$$

in the convecting region, conserving energy, and to recompute the radiative
balance — iterating until both hold. The surface temperature is then set by the
radiative balance at the *top* of the convecting layer, not at the surface. **The
rule is a modelling choice; needing a rule is not.**

### 3.6 The transport implied and the transport required

The diffusion parameterisation implies a transport

$$H_{\text{diff}}(\phi) = -2\pi R_E^2\,D\,(1-x^2)\frac{\mathrm{d}T}{\mathrm{d}x},$$

while the budget requires

$$H_{\text{budget}}(\phi) = -2\pi R_E^2\int_x^{1}N(x')\,\mathrm{d}x',
\qquad N = Q(1-a) - \mathrm{OLR}.$$

In steady state these are the same expression by construction — the diffusion term
*is* the divergence of the transport — so comparing them is a **consistency check
on the discretisation, not an independent test**. The demonstration finds
$H_{\text{diff}} - H_{\text{budget}}$ never exceeding $0.0565\ \mathrm{PW}$, i.e.
$2.1\%$ of the $2.64\ \mathrm{PW}$ peak, and identifies the residual as the
first-order-accurate numerical gradient used for $\mathrm{d}T/\mathrm{d}x$ rather
than any physical inconsistency. The peak occurs at $38.1^\circ$.

**Why the check is still worth doing.** A discretisation that is *inconsistent* —
for instance one that does not conserve energy on the grid — would fail this
comparison, and the failure would be invisible in the temperature field. The check
is cheap and it tests the code, not the physics; saying which is which is the
point.

## 4. Physical interpretation

- **The zero-dimensional model is a null hypothesis.** It has no atmosphere, no
  geography and no dynamics, so any phenomenon it fails to reproduce is a
  *diagnosis* of what the missing ingredient does. That is its value.
- **The heat capacity sets the clock, not the destination.** $C$ determines how
  long the system takes to reach equilibrium and nothing else.
- **Distribution and mean are independent in a linear model.** §3.3 proves it, and
  it is a strong statement: no amount of redistribution by itself warms a planet.
  Warming a planet's mean requires changing its energy balance.
- **Nonlinearity is what makes geography matter for the mean.** The ice-albedo
  feedback couples the distribution to the mean, and that is why it produces
  bifurcations.
- **Multiple equilibria are a property of the model family, not a prediction.**
  The hysteresis is robust as a *mechanism*; its location and width are set by
  chosen functions, as §3.4 says.
- **Convective adjustment is where the physics is hidden.** Everything an EBM says
  about the surface temperature depends on it, and it is a rule rather than a
  derivation. That is the honest summary of the model hierarchy of
  [05 Climate Models](../05-climate-models/README.md).

## 5. Worked numerical examples

**Example 1 — equilibrium, relaxation and a step forcing.**

With $F = 238.175\ \mathrm{W\,m^{-2}}$, $T_{\text{eq}} = 254.578\ \mathrm{K}$,
$C = 2.000\times10^{8}\ \mathrm{J\,m^{-2}\,K^{-1}}$ and $B = 3.7423\
\mathrm{W\,m^{-2}\,K^{-1}}$:

$$\tau = C/B = 5.3444\times10^{7}\ \mathrm{s} = 1.69\ \mathrm{yr}.$$

A step forcing of $\Delta F = 3.0\ \mathrm{W\,m^{-2}}$ produces
$\delta T(\infty) = 3.0/3.7423 = 0.802\ \mathrm{K}$, reached with time constant
$\tau$: after one year the response is
$0.802(1-e^{-1/1.69}) = 0.802\times0.4465 = 0.358\ \mathrm{K}$, i.e. $45\%$ of the
way. **That ratio is the whole reason the ocean matters**: a forcing and a
temperature are not interchangeable until the system has had several $\tau$.

**Example 2 — the mean-temperature identity, verified.**

| $D$ (W m⁻² K⁻¹) | equator (K) | pole (K) | contrast (K) | mean (K) |
|---|---|---|---|---|
| 0.3 | 264.405 | 232.686 | 31.719 | 254.531 |
| 0.6 | 262.068 | 238.017 | 24.052 | 254.531 |
| 1.2 | 259.634 | 243.434 | 16.200 | 254.531 |
| 2.4 | 257.628 | 247.829 | 9.799 | 254.531 |

A **fourfold** change in the diffusion coefficient changes the contrast by a factor
of $3.2$ and the mean by **nothing** ($254.531\ \mathrm{K}$ in every row, matching
$(\langle Q(1-a)\rangle - A)/B$ to $10^{-10}$). The tropics change most, because
the metric factor $(1-x^2)$ is largest there: the diffusion carries more energy per
unit gradient near the equator than near the pole.

**Example 3 — the hysteresis width.**

Between $S/S_0 = 1.30$ (frozen from both starting points) and somewhere in
$(1.80, 2.00)$ (ice-free from both, with $1.80$ still giving a frozen state from a
cold start and $2.00$ not), the two branches coexist. At $S/S_0 = 1.40$ the
ice-free branch has an ice edge at $45.8^\circ$ and a global mean of
$271.67\ \mathrm{K}$, while the frozen branch has a global mean of
$239.34\ \mathrm{K}$. **The two equilibria at the same forcing differ by
$32\ \mathrm{K}$ in the global mean** — larger than any greenhouse-gas-driven
change discussed elsewhere in this module, and produced by a change in
*reflectivity*. The comparison is between model states, not between two real
climates, and the width of the loop is a property of the chosen albedo function
(§3.4). It is also the reason the existence of a *mechanism* must be separated from
the magnitude of its effect: the mechanism is general, the $32\ \mathrm{K}$ is not.

## 6. Assumptions and regime of validity

| Assumption | Where used | What breaks it |
|---|---|---|
| Single temperature | the zero-dimensional model | There is no such temperature; the global mean is an average of a field with a large variance |
| Mixing depth 50 m | $C$ | The ocean's effective heat capacity depends on the timescale; for long times the deep ocean participates and $C$ grows |
| OLR linearised about one temperature | $A$, $B$ | The linearisation is excellent for small perturbations about $T_0$ and poor for tens of kelvin; the $1.72\%$ relaxation-time residual measures the beginning of that failure |
| OLR a function of $T$ alone | the 1-D model | Real OLR depends on humidity, clouds and the vertical profile, not only on the surface temperature |
| Diffusion parameterisation of transport | the 1-D model | Real transport is by atmospheric eddies and ocean circulation, not by downgradient diffusion; the parameterisation is chosen to get the *pattern* roughly right, not derived |
| $D$ constant | all of §3.3 | The transport efficiency varies with season and with the jet position |
| Step-function albedo | §3.4 | Ice margins are diffuse; a smooth albedo weakens and eventually destroys the hysteresis |
| No ocean heat transport | §3.4 | The ocean carries a large share of the poleward transport and has a different geometry |
| No seasonal cycle | everything | Seasonal ice, the seasonal cycle of insolation and the storage of heat in the ocean all change the thresholds |
| No dynamics, no clouds | everything | Clouds set much of the albedo and are not independent of temperature |
| Convective adjustment as a rule | §3.5 | The rule's details (what is conserved, over what depth) change the answer by more than the radiative physics does |

**Climate-claim discipline.** These models are *explanatory*, not predictive, and
three distinctions should be kept:

1. **A model result is not a prediction.** "The ice-free and frozen branches
   coexist for $S/S_0 \in (1.30, 1.55)$" is a statement about this model with these
   functions. The *mechanism* — threshold plus positive feedback gives hysteresis —
   is general.
2. **An EBM cannot be validated against a temperature alone.** It has enough
   freedom to match a global mean temperature with many parameter choices
   ([04 §3.3](04-earth-energy-balance.md) showed the degeneracy in a simpler case).
   Validation requires the *pattern* (the pole-to-equator contrast, the seasonal
   cycle) and that is where an EBM starts to fail.
3. **The model hierarchy is a ladder of excuses, and each rung must name its own.**
   The zero-dimensional model names no geography; the one-dimensional model names
   a diffusion coefficient; the radiative–convective model names a convective
   adjustment. Naming them is what makes the ladder useful.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| Heat capacity per area | $C$ | $\mathrm{J\,m^{-2}\,K^{-1}}$ | $\rho c_p h$: $(\mathrm{kg\,m^{-3}})(\mathrm{J\,kg^{-1}\,K^{-1}})(\mathrm{m})$ ✔ |
| Feedback parameter | $B$ | $\mathrm{W\,m^{-2}\,K^{-1}}$ | $4\sigma T^3$ ✔ |
| Relaxation time | $\tau = C/B$ | s | $\mathrm{J\,m^{-2}\,K^{-1}}/(\mathrm{W\,m^{-2}\,K^{-1}})$ ✔ |
| Diffusion coefficient | $D$ | $\mathrm{W\,m^{-2}\,K^{-1}}$ | same unit as $B$; the operator $(1-x^2)\partial_x\partial_x$ is dimensionless in $x$ |
| Transport | $H(\phi)$ | W | $(\mathrm{W\,m^{-2}\,K^{-1}})(\mathrm{K})(\mathrm{m^2})$ ✔ |
| Insolation | $Q(\phi)$ | $\mathrm{W\,m^{-2}}$ | annual mean of a daily mean |

Two checks: the ratio $D/B$ is a *length-squared-free* timescale only if the
operator is dimensionless, which it is in $x$ (not in $\phi$ or in metres — a
common source of silent factor errors when the coordinate is changed); and any
transport must come out in watts.

## 8. Python demonstration

[`code/energy_balance_models_demo.py`](code/energy_balance_models_demo.py) prints
every number quoted above. It:

1. solves the zero-dimensional model, computes $C$, $B$ and $\tau$, integrates the
   ODE and measures the e-folding time ($1.72\%$ above $\tau$, and explains why);
2. computes the annual-mean insolation from the daily formula on a grid uniform in
   $x = \sin\phi$, and verifies that its area-weighted mean is $S/4$ to
   $0.0003\%$;
3. solves the steady one-dimensional model exactly as a linear finite-volume
   system, verifies the mean-temperature identity to $10^{-10}\ \mathrm{K}$, and
   tabulates the equator–pole contrast for four diffusion coefficients;
4. computes the transport two ways and identifies the residual as a numerical
   gradient error;
5. scans the solar constant for the ice-albedo bifurcation, runs the hysteresis
   loop from both starting states, and states its three caveats;
6. quantifies the non-radiative flux a radiative-only profile would need, and
   explains convective adjustment.

```bash
cd 16-atmosphere-climate/02-radiation-and-energy-balance/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python energy_balance_models_demo.py
```

## 9. Exercises

Graded problems with worked solutions:
[`exercises/05-energy-balance-models-exercises.md`](exercises/05-energy-balance-models-exercises.md)
and
[`exercises/05-energy-balance-models-solutions.md`](exercises/05-energy-balance-models-solutions.md).

## Mastery checkpoint

Without notes:

> A zero-dimensional EBM has $S = 1361\ \mathrm{W\,m^{-2}}$, $a = 0.30$, a mixed
> layer of $80\ \mathrm{m}$ and the OLR linearised about $T_0 = 250\ \mathrm{K}$.
> **(a)** Compute $F$, the equilibrium temperature (both by solving the full
> $\sigma T^4$ balance and by the linearised relation), and state why they differ.
> **(b)** Compute $C$, $B$ and $\tau$, and the temperature change after two years
> for a step forcing of $4\ \mathrm{W\,m^{-2}}$. **(c)** State in one sentence what
> would change if the mixed layer were $40\ \mathrm{m}$ instead of $80\ \mathrm{m}$.
> **(d)** A one-dimensional version of the model has a transport that changes the
> equator-pole contrast from $30\ \mathrm{K}$ to $15\ \mathrm{K}$ with no change in
> $D$'s global-mean effect; state what happens to the global mean temperature and
> justify your answer with the identity of §3.3. **(e)** Name two mechanisms that
> would break that identity, and state for each whether it is a model choice or a
> physical fact.

## Common pitfalls

1. **Treating the EBM's equilibrium temperature as a prediction.** It is the
   temperature of a model with a chosen albedo and no atmosphere.
2. **Forgetting that $C$ sets only the timescale.** A larger heat capacity does not
   change the equilibrium, only the time taken to reach it.
3. **Expecting transport to change the global mean.** In a linear model it cannot,
   and §3.3 proves it. Global-mean change needs a forcing or a nonlinearity.
4. **Imposing the pole boundary condition explicitly.** The metric factor
   $1-x^2$ makes the pole flux vanish automatically; imposing something extra
   introduces an error.
5. **Believing the hysteresis width is a physical number.** It is a property of the
   chosen albedo function, and §3.4 says so.
6. **Calling the transport comparison an independent test.** It is a consistency
   check on the discretisation; the two quantities are the same by construction.
7. **Using the OLR linearisation far from $T_0$.** It is a Taylor expansion; the
   $1.72\%$ relaxation-time residual is where it starts to hurt.
8. **Replacing convective adjustment with nothing.** Without it the model's surface
   temperature is hundreds of kelvin: the required non-radiative flux exceeds the
   absorbed sunlight.

## Related modules

- [04 Earth Energy Balance and Global Mean Temperature](04-earth-energy-balance.md) —
  the budgets these models discretise, and the degeneracy they must break.
- [02 Radiative Transfer in the Atmosphere](02-radiative-transfer-atmosphere.md) —
  the grey radiative-equilibrium profiles of §3.5.
- [03 The Greenhouse Effect: Physics, Not Rhetoric](03-greenhouse-effect.md) —
  the feedback parameter $B$ and the forcing conventions.
- [06 Aerosols, Clouds and Their Radiative Effects](06-aerosols-and-clouds-radiation.md) —
  the scattering that the albedo parameter guesses at.
- [01 Solar and Terrestrial Radiation, Blackbody Laws](01-solar-and-terrestrial-radiation.md) —
  the daily-mean insolation formula averaged in §3.2.
- [16-01-03 Adiabatic Processes, Lapse Rates and Stability](../01-atmospheric-structure-and-thermodynamics/03-thermodynamic-processes.md) —
  the adiabatic lapse rate used by the convective adjustment.
- [01-09-02 The Diffusion/Heat Equation and Diffusive Timescales](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md) —
  the diffusion operator and its boundary conditions.
- [16-05 Climate Models and Simulation](../05-climate-models/README.md) —
  where the model hierarchy continues.
