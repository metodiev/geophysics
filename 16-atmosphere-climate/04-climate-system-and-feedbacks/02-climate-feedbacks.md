---
id: 16-04-02
title: "Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon"
level: doctoral
prereqs: ["16-04-01", "16-02-04", "16-02-06"]
tags: [atmosphere, climate, feedbacks, climate-sensitivity, ice-albedo, water-vapour, clouds, carbon-cycle]
---

# Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon

A change in the top-of-atmosphere energy budget is not a temperature change. It
is a *forcing* — an imbalance in watts per square metre — and the temperature
change is whatever restores balance. The baseline restoring mechanism is the
Planck response: a warmer body radiates more, at $4\sigma T^3$ per kelvin. Every
other process that changes the outgoing or incoming flux *because* the
temperature changed is a **feedback**, and the entire subject lives in one
algebraic identity:

$$N = F + \lambda\Delta T, \qquad \lambda = \lambda_0 + \sum_i \lambda_i,
\qquad \Delta T_\text{eq} = -\frac{F}{\lambda}.$$

The lesson is about the honesty required to use it. Each $\lambda_i$ is a
*derivative*, evaluated in one state, valid over the range where the underlying
process is linear. The water-vapour feedback can be tied to a physical law
(Clausius–Clapeyron) but not to a feedback parameter without an assumption about
relative humidity. The ice-albedo feedback produces genuinely non-linear
behaviour: two stable climates for one forcing. The cloud feedback's *sign* is
not settled by the physics in the accounting model, only by the assumed
sensitivities. And the carbon-cycle feedback is a feedback in *time* as well as
in temperature. So this lesson reports ranges with the assumptions attached, and
it shows quantitatively where the linear decomposition starts to fail: a
state-dependent feedback makes the linear estimate wrong by $2.75\%$ at the
reference forcing and by $6.37\%$ at twice it.

All models and data in this module are **SYNTHETIC**. Every feedback parameter,
range, albedo ramp and cloud coefficient below is a **chosen teaching value**;
none is quoted from any assessment report, and none should be read as an
estimate of the real Earth's feedbacks. What is transferable is the arithmetic
and the structure. Physical constants (Stefan–Boltzmann, latent heat of
vaporisation, the gas constant of water vapour) are standard constants.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Planck feedback parameter and **state** the sign convention
   under which it is negative.
2. **Compute** the equilibrium temperature change from a forcing and a set of
   feedback parameters, and **propagate** assumed ranges to a distribution with
   its median, spread and skew.
3. **Identify** which assumed feedback dominates the spread and explain why
   dominance is a property of the *range*, not of the mean.
4. **Demonstrate** quantitatively how a state-dependent feedback invalidates the
   linear decomposition, and **state** the criterion for acceptable error.
5. **Compute** the ice-albedo feedback parameter from an albedo ramp, and
   **explain** its multiple equilibria and the hysteresis loop, including the
   sense in which the loop width is an artefact of the parameters.
6. **Derive** the Clausius–Clapeyron rate $\mathrm{d}\ln e_s/\mathrm{d}T =
   L/(R_vT^2)$ and **explain** why it is not the water-vapour feedback parameter.
7. **Account** for the cloud feedback as the sum of a shortwave and a longwave
   term and **show** that its sign depends on the assumed sensitivities.
8. **Formulate** the carbon-cycle feedback with its concentration and
   climate parameters, and **compute** the airborne fraction with and without it.

## Prerequisites

- [16-04-01 Components of the Climate System and Their Timescales](../04-climate-system-and-feedbacks/01-climate-system-components.md) —
  heat capacities, relaxation times and the two-layer ocean.
- [16-02-04 Earth Energy Balance and Global Mean Temperature](../02-radiation-and-energy-balance/04-earth-energy-balance.md) —
  the top-of-atmosphere budget and the definition of a forcing.
- [16-02-06 Aerosols, Clouds and Their Radiative Effects](../02-radiation-and-energy-balance/06-aerosols-and-clouds-radiation.md) —
  the cloud radiative effects that Section 8 parameterises.

## 1. Intuition: a feedback is a derivative, not a process

Write the net downward top-of-atmosphere flux as $N(T; \mathbf{p})$ with
$\mathbf{p}$ a set of state parameters. A forcing changes the budget at fixed
$T$; a feedback changes it at fixed $\mathbf{p}$ through the dependence of
$T$ on the rest of the state. Expanding about the present climate,

$$N(T + \Delta T) = F + \underbrace{\left.\frac{\partial N}{\partial T}
\right|_{0}}_{\lambda}\,\Delta T + O(\Delta T^2),$$

so $\Delta T_\text{eq} = -F/\lambda$ to first order. Three consequences follow
immediately, and they are the reason this lesson is longer than the formula:

1. $\lambda$ is a derivative: it belongs to a state, and it changes when the
   state does.
2. $\partial N/\partial T$ includes every process that depends on $T$, whether
   or not anyone has measured it separately. The decomposition into named
   feedbacks is a *modelling* choice.
3. A positive $\lambda_i$ amplifies the response while a negative one damps it —
   but the sign of a feedback parameter has nothing to do with whether the
   underlying process is "good" or "bad". In this convention, stabilising means
   negative.

## 2. Definitions

| Symbol | Meaning | Convention |
|---|---|---|
| $F$ | Radiative forcing at fixed surface temperature | positive = warming |
| $N$ | Net downward top-of-atmosphere flux | positive = system gaining energy |
| $\lambda$ | $\partial N/\partial T$, total | W m⁻² K⁻¹ |
| $\lambda_0$ | Planck response, $4\partial(\sigma T^4)/\partial T$ | **negative** |
| $\lambda_i$ | A named feedback | positive = amplifying |
| $G$ | Gain, $-\lambda_i/\lambda$ for a single feedback | dimensionless |
| $F_{2\times}$ | Forcing from a doubling of CO₂ | chosen here as 3.7 W m⁻² |
| $\beta$ | Carbon-concentration uptake parameter | per unit excess |
| $\gamma$ | Carbon-climate uptake parameter | GtC K⁻¹ |

## 3. The Planck response

For a blackbody, $N = \sigma T^4$ at the top of the atmosphere, so

$$\lambda_0 = \frac{\mathrm{d}}{\mathrm{d}T}\left(\sigma T^4 -
\text{(absorption)}\right) \approx -4\sigma T^3,$$

where the minus sign follows the convention that $\lambda$ multiplies $\Delta T$
in $N = F + \lambda\Delta T$: a warmer body sends *more* energy out, which is a
*decrease* in net downward flux. At the chosen reference temperature $T = 288$ K,

$$\lambda_0 = -4(5.670374419\times10^{-8})(288)^3
= -5.418\ \mathrm{W\,m^{-2}K^{-1}},$$

and the Planck-only response to $F_{2\times} = 3.7\ \mathrm{W\,m^{-2}}$ is
$\Delta T = 3.7/5.418 = 0.68$ K. That is the number every feedback moves. The
Planck response operates everywhere, always, with no threshold and no
saturation, which is why it is the baseline rather than one feedback among many.

## 4. The additive decomposition, with its spread

The demonstration assumes, as **chosen ranges** (uniform), in W m⁻² K⁻¹:

| feedback | assumed range | mean | sd |
|---|---|---|---|
| water vapour + lapse rate | $[+0.8, +1.4]$ | 1.10 | 0.173 |
| surface albedo | $[+0.1, +0.5]$ | 0.30 | 0.115 |
| cloud | $[-0.4, +1.2]$ | 0.40 | 0.462 |
| carbon cycle | $[+0.0, +0.3]$ | 0.15 | 0.087 |

Summing with $\lambda_0 = -5.418$ gives a total $\lambda$ with mean $-3.470$,
standard deviation $0.514$, range $[-4.876, -2.069]$ W m⁻² K⁻¹. The implied
equilibrium temperature change $-\!F_{2\times}/\lambda$ is

| percentile | $\Delta T$ (K) |
|---|---|
| 5th | 0.862 |
| 25th | 0.955 |
| 50th | 1.066 |
| 75th | 1.206 |
| 95th | 1.401 |
| mean | 1.091 |

**Three things to read from this table, none of which requires the numbers to be
right.**

1. **The distribution is skewed.** The mean (1.091 K) lies above the median
   (1.066 K) and the 95th percentile is far from the median in absolute terms,
   because $\Delta T\propto1/\lambda$ and $\lambda$ can approach zero from below.
   A ratio of uncertain quantities has a long tail in the direction of the
   smaller denominator, and quoting a mean for such a quantity is a choice, not
   a summary.
2. **Spread is dominated by the widest assumed range.** The cloud term accounts
   for **80.7%** of the variance of the total, water vapour 11.4%, albedo 5.0%
   and carbon 2.9% — even though water vapour has the largest *mean*. Uncertainty
   is about ranges, not about magnitudes.
3. **The ranges are assumptions.** Change them and every number above changes
   without any physical insight being gained or lost. The value of the exercise
   is that it forces the assumptions to be written down where they can be
   argued with.

## 5. Where the linear decomposition fails

Take a single amplifying feedback whose parameter *strengthens* as the state
warms, $\lambda_c(\Delta T) = 0.80 + 0.15\,\Delta T$ W m⁻² K⁻¹ — a placeholder
for the real tendency of cloud and albedo feedbacks to change strength as the
state changes. The linear answer uses $\lambda_c(\Delta T = 0)$, while the exact
answer solves $F = \left[|\lambda_0| - \lambda_c(\Delta T)\right]\Delta T$
implicitly:

| $F$ (W m⁻²) | linear $\Delta T$ (K) | exact $\Delta T$ (K) | error | $\lambda_c$ at the exact $\Delta T$ |
|---|---|---|---|---|
| 0.5 | 0.108 | 0.109 | 0.35% | 0.816 |
| 1.0 | 0.217 | 0.218 | 0.71% | 0.833 |
| 2.0 | 0.433 | 0.439 | 1.45% | 0.866 |
| 3.7 | 0.801 | 0.823 | 2.75% | 0.923 |
| 6.0 | 1.299 | 1.359 | 4.62% | 1.004 |
| 8.0 | 1.732 | 1.843 | 6.37% | 1.076 |

At the reference forcing the linear answer is wrong by 2.75%, and at 8 W m⁻² by
6.37% (the sign is the same in every row: ignoring a *strengthening*
amplification underestimates the response). Both numbers are small enough that the linear framework is *useful*; both
are large enough that "the feedback parameter" must always be reported with the
state and the forcing range in which it was evaluated. The decomposition is a
Taylor expansion about the present climate. Applying it to a much warmer state
is not a conservative approximation; it is a different model with a different
answer.

## 6. Ice-albedo feedback

### 6.1 The feedback parameter

Let the planetary albedo be a ramp: $\alpha = 0.62$ below $-10\ ^\circ$C, $0.30$
above $+10\ ^\circ$C, and linear between. Then
$\mathrm{d}\alpha/\mathrm{d}T = -0.016\ \mathrm{K^{-1}}$, and

$$\lambda_\text{ice} = -\frac{S}{4}\frac{\mathrm{d}\alpha}{\mathrm{d}T}
= -(340.25)(-0.016) = +5.44\ \mathrm{W\,m^{-2}K^{-1}},$$

which is **larger in magnitude than the Planck response itself**. That is why
ice-albedo is not a small correction; but note the crucial qualifier: the ramp
exists only where the albedo is actually changing. Outside the band,
$\mathrm{d}\alpha/\mathrm{d}T = 0$ and the feedback parameter is zero. A single
number for "the ice-albedo feedback" is therefore only meaningful when the
transition band is specified.

### 6.2 Two climates for one forcing

The zero-dimensional model

$$C\frac{\mathrm{d}T}{\mathrm{d}t} = \frac{S}{4}\left[1-\alpha(T)\right]
- \left(A + BT\right), \qquad A = 203.3, \quad B = 2.09,$$

has closed-form equilibria, one per albedo regime. The demonstration finds:

| $S$ (W m⁻²) | equilibria (°C) | number |
|---|---|---|
| 1000 | $-51.82$ (ice) | 1 |
| 1200 | $-42.73$ (ice), $-5.99$ (ramp) | 2 |
| 1281 | $-39.05$ (ice), $-4.21$ (ramp) | 2 |
| 1361 | $-35.41$ (ice), $+16.69$ (ice-free), $-2.60$ (ramp) | 3 |
| 1500 | $-29.09$ (ice), $+28.33$ (ice-free), $-0.10$ (ramp) | 3 |
| 1700 | $-20.00$ (ice), $+45.07$ (ice-free), $+2.95$ (ramp) | 3 |
| 1920 | $-10.00$ (ice), $+63.49$ (ice-free), $+5.72$ (ramp) | 3 |
| 2100 | $+78.56$ (ice-free), $+7.65$ (ramp) | 2 |

The ice-free branch exists only for $S > 1281$ W m⁻², the ice-covered branch only
for $S < 1920\ \mathrm{W\,m^{-2}}$, and between those values there are **three**
equilibria. The middle one sits on the ramp and is unstable: its total feedback
parameter is $\lambda_\text{total} = -(S/4)\mathrm{d}\alpha/\mathrm{d}T - B
= +3.35\ \mathrm{W\,m^{-2}K^{-1}} > 0$, so a perturbation grows. The two outer
branches have $\lambda = -B < 0$ and are stable.

This is the structure — **bistability and hysteresis** — and it is a genuine
consequence of an amplifying feedback acting over a limited range. But the loop
width is 639 W m⁻², tens of per cent of the solar constant, so the model is
grossly overstating the effect: at 1920 W m⁻² the warm branch sits at
$+63\ ^\circ$C, far outside the range where a linear OLR law is meaningful. The
demonstration also shows the loop narrowing as the ramp widens:

| ramp width (°C) | $S$ at the ice-free limit | $S$ at the ice limit | loop width |
|---|---|---|---|
| 10 | 1221 | 2030 | 809 |
| 20 | 1281 | 1920 | 639 |
| 40 | 1401 | 1700 | 299 |

A wider (slower) transition weakens $\mathrm{d}\alpha/\mathrm{d}T$ and so narrows
the loop. **What is transferable is the structure; the numbers are artefacts of
$A$, $B$ and the ramp.**

## 7. Water vapour: a law, an assumption, and a feedback

### 7.1 The law

Clausius–Clapeyron, in its derivative form,

$$\frac{\mathrm{d}\ln e_s}{\mathrm{d}T} = \frac{L}{R_vT^2},$$

with $L = 2.5\times10^6$ J kg⁻¹ and $R_v = 461.5$ J kg⁻¹ K⁻¹:

| $T$ (K) | $T$ (°C) | $\mathrm{d}\ln e_s/\mathrm{d}T$ (K⁻¹) | % per K |
|---|---|---|---|
| 250 | $-23.1$ | 0.08667 | 8.67 |
| 273 | $-0.1$ | 0.07268 | 7.27 |
| 288 | $+14.9$ | 0.06531 | 6.53 |
| 300 | $+26.9$ | 0.06019 | 6.02 |
| 310 | $+36.9$ | 0.05637 | 5.64 |

The rate **falls** with temperature, because the same latent heat is divided by
a larger $T^2$. The familiar "7% per K" is the value near freezing and in the
mid-troposphere.

### 7.2 What the law is not

The rate above is a statement about *saturation*. To turn it into a feedback
parameter requires two more steps, each an assumption:

1. **A relative-humidity assumption.** Holding relative humidity fixed makes the
   vapour content rise at the Clausius–Clapeyron rate; holding specific humidity
   fixed makes the feedback zero.
2. **A radiative kernel.** The extra vapour must be mapped onto a change in
   outgoing longwave radiation, which requires a radiative transfer calculation
   or a linearised kernel.

Neither step is taken in this lesson, and the demonstration's water-vapour
feedback range in Section 4 is an assumption, not a derivation. The distinction
matters: the law is physics, the feedback parameter is a model output that
depends on how processes that are not resolved are represented.

## 8. Cloud feedback: two effects, either sign

The accounting model used here writes the cloud contribution to the net flux as

$$N_\text{cloud} = -f\alpha_c\frac{S}{4} + f\varepsilon_c\sigma T^4,$$

with $f$ the cloud fraction, $\alpha_c$ the cloud albedo (shortwave, cooling) and
$\varepsilon_c$ the longwave emissivity (warming). Differentiating at fixed
$S$, $T$,

$$\lambda_\text{cloud} = -\frac{S}{4}\left(\alpha_c\frac{\mathrm{d}f}
{\mathrm{d}T} + f\frac{\mathrm{d}\alpha_c}{\mathrm{d}T}\right)
+ \sigma T^4\left(\varepsilon_c\frac{\mathrm{d}f}{\mathrm{d}T}
+ f\frac{\mathrm{d}\varepsilon_c}{\mathrm{d}T}\right).$$

With $f = 0.60$, $\alpha_c = 0.40$, $\varepsilon_c = 0.80$, $S/4 = 340.25$ and
$\sigma T^4 = 390.1$ W m⁻², the demonstration evaluates seven defensible
combinations:

| $\mathrm{d}f/\mathrm{d}T$ | $\mathrm{d}\alpha_c/\mathrm{d}T$ | $\mathrm{d}\varepsilon_c/\mathrm{d}T$ | $\lambda_\text{cloud}$ | sign |
|---|---|---|---|---|
| $-0.005$ | 0.000 | 0.000 | $-0.880$ | negative |
| $-0.005$ | $-0.005$ | 0.000 | $+0.141$ | positive |
| $-0.005$ | 0.000 | $-0.005$ | $-2.050$ | negative |
| 0.000 | 0.000 | $+0.005$ | $+1.170$ | positive |
| $+0.005$ | $+0.010$ | 0.000 | $-1.162$ | negative |
| 0.000 | $-0.010$ | 0.000 | $+2.042$ | positive |
| $+0.005$ | 0.000 | $+0.010$ | $+3.221$ | positive |

The range is $[-2.05, +3.22]$ W m⁻² K⁻¹ and **the sign changes**. This is not a
failure of the physics: it is a correct statement that the net cloud feedback
depends on which of two competing effects dominates as the climate changes, and
that the accounting model accepts both possibilities. It is also the reason the
cloud term supplies 80.7% of the spread in Section 4.

## 9. Carbon-cycle feedback

The carbon cycle has both a temperature-independent and a temperature-dependent
uptake. Write the atmospheric excess as

$$\Delta C = \frac{E - \gamma\,\Delta T}{1 + \beta},$$

where $\beta$ is the uptake per unit excess (the *concentration–carbon*
feedback) and $\gamma$ the additional uptake per kelvin (the *climate–carbon*
feedback), with $\Delta T$ set by the logarithmic forcing
$F = F_{2\times}\ln(1 + \Delta C/C_0)/\ln 2$ divided by $|\lambda|$. With
$C_0 = 800$ GtC ($= 377$ ppm at the derived 2.124 GtC per ppm), $\beta = 1.00$,
$\gamma = 100$ GtC K⁻¹, $|\lambda| = 4.0$ W m⁻² K⁻¹ and $E = 1000$ GtC:

| case | $\Delta C$ (GtC) | ppm | airborne fraction | $F$ (W m⁻²) | $\Delta T$ (K) |
|---|---|---|---|---|---|
| without $\gamma$ | 500.0 | 612 | 0.500 | 2.592 | 0.648 |
| with $\gamma$ | 469.2 | 598 | 0.469 | 2.464 | 0.616 |

The feedback reduces the airborne fraction from 0.500 to 0.469 and the warming
from 0.648 K to 0.616 K — a difference of 0.032 K for the same emissions. Over
an assumed range $\gamma \in [0, 400]$ GtC K⁻¹ the warming spans 0.53–0.65 K.
Two structural points matter more than the numbers:

- The carbon feedback operates in **time** as well as in temperature: the ocean
  and land reservoirs adjust over decades to centuries (see
  [16-04-01](../04-climate-system-and-feedbacks/01-climate-system-components.md) §7),
  so a transient calculation shows a smaller effect than this equilibrium one.
- Its magnitude is set by $\beta$ and $\gamma$, both of which are
  parameterisations of unresolved processes, so the honest output is the range.

## 10. Assumptions and regime of validity

1. **Linearity in $\Delta T$.** Every decomposition here is a first-order
   expansion; Section 5 quantifies its error and shows it growing to 6.37% at
   8 W m⁻².
2. **Additivity.** Feedbacks are assumed to sum. That holds to the extent that
   the fluxes separate, which the same linearisation requires.
3. **A single state variable.** These models have one temperature. Anything that
   depends on the *pattern* of warming (the pattern effect) is invisible here.
4. **Constant coefficients.** $f$, $\alpha_c$, $\varepsilon_c$, $A$, $B$, $\beta$,
   $\gamma$ are all fixed. Their temperature dependence is the subject of
   Section 5, not of the models themselves.
5. **Chosen values everywhere.** No coefficient in this lesson is a measurement.
6. **Equilibrium.** Section 9 computes an equilibrium carbon budget; the real
   system is transient, and its transient response is smaller and slower.
7. **No ocean, no ice sheet, no biosphere dynamics** are included beyond the
   parameters listed.

## 11. Worked examples

### Example 1 — a feedback parameter and a response

$\lambda_0 = -5.418$, water vapour $+1.10$, albedo $+0.30$, cloud $+0.40$,
carbon $+0.15$ W m⁻² K⁻¹:

$$\lambda = -5.418 + 1.10 + 0.30 + 0.40 + 0.15 = -3.468\
\mathrm{W\,m^{-2}K^{-1}},$$

$$\Delta T_\text{eq} = -\frac{3.7}{-3.468} = 1.067\ \mathrm{K}.$$

The gain of the water-vapour feedback alone is
$G = 1.10/3.468 = 0.317$, i.e. it amplifies the response by about 32% relative
to the no-feedback case.

### Example 2 — the ice-albedo feedback parameter

With $S/4 = 340.25$ W m⁻² and $\mathrm{d}\alpha/\mathrm{d}T = -0.016$ K⁻¹:

$$\lambda_\text{ice} = -340.25\times(-0.016) = +5.44\
\mathrm{W\,m^{-2}K^{-1}},$$

so within the transition band the net $\lambda = \lambda_0 + \lambda_\text{ice}
= -5.418 + 5.44 = +0.02$ W m⁻² K⁻¹ — essentially zero. A state with
$\lambda \approx 0$ has no stable equilibrium temperature: this is exactly the
middle (unstable) branch of Section 6.2, at about $-2.6\ ^\circ$C for
$S = 1361$ W m⁻².

### Example 3 — the carbon feedback

Without $\gamma$: $\Delta C = 1000/2 = 500$ GtC. With $\gamma = 100$ and
$\Delta T = 0.616$ K: $\Delta C = (1000 - 61.6)/2 = 469.2$ GtC. The ppm values
come from $C_0 + \Delta C = 1269.2$ GtC divided by 2.124 GtC per ppm
$= 598$ ppm, and the forcing from
$F = 3.7\ln(1269.2/800)/\ln 2 = 3.7\times0.6660 = 2.464$ W m⁻², giving
$\Delta T = 2.464/4.0 = 0.616$ K. The iteration converges because
$\gamma\,\Delta T$ is small compared with $E$.

## 12. Python demonstration

[`code/climate_feedbacks_demo.py`](code/climate_feedbacks_demo.py) prints every
number above in seven labelled sections: the Planck response; the additive
decomposition with its Monte Carlo spread and variance shares; the linearity
error from a state-dependent feedback; the ice-albedo equilibria, hysteresis
loop and its sensitivity to the ramp; the Clausius-Clapeyron rate; the cloud
two-effect budget; and the carbon β–γ budget. It uses closed-form equilibrium
solutions rather than root-finding grids so that the whole script runs in a
fraction of a second; it needs no network and exits 0.

## 13. Exercises

Full sets with worked solutions are in
[`exercises/02-climate-feedbacks-exercises.md`](exercises/02-climate-feedbacks-exercises.md)
and
[`exercises/02-climate-feedbacks-solutions.md`](exercises/02-climate-feedbacks-solutions.md).

- **★** Compute $\lambda_0$ at $T = 270$ K and the Planck-only response to a
  2.0 W m⁻² forcing.
- **★** Compute $\mathrm{d}\ln e_s/\mathrm{d}T$ at 265 K and at 305 K and state
  the direction of the change with temperature.
- **★★** For assumed ranges water vapour $[0.9, 1.5]$, cloud $[-0.3, 1.0]$,
  albedo $[0.1, 0.4]$, carbon $[0.0, 0.2]$ (all W m⁻² K⁻¹), compute the total
  $\lambda$ at the midpoints and the equilibrium response to
  $F_{2\times} = 3.7$ W m⁻², then state which term you would most want to
  narrow first and why.
- **★★** Derive $\lambda_\text{ice} = -(S/4)\mathrm{d}\alpha/\mathrm{d}T$ and
  compute the albedo ramp slope for which $\lambda_0 + \lambda_\text{ice} = 0$
  at $S = 1361$ W m⁻².
- **★★★** The demonstration's hysteresis loop is 639 W m⁻² wide. Using the
  formula for the loop edges, determine how the width scales with
  $(1-\alpha_\text{ice})$, $(1-\alpha_\text{free})$ and the ramp half-width, and
  state what a *physical* ice-albedo model would have to include to narrow it.

## 14. Common mistakes

1. **Dropping the sign convention.** With $\lambda = \partial N/\partial T$,
   stabilising feedbacks are negative and $\Delta T = -F/\lambda$.
2. **Reporting a mean for a ratio.** Section 4's distribution is skewed; a mean
   is a choice.
3. **Treating the decomposition as exact.** Section 5 gives the error against
   forcing.
4. **Attributing the ice-albedo loop width to physics.** It is set by $A$, $B$
   and the assumed ramp.
5. **Calling Clausius–Clapeyron "the water-vapour feedback".** It is the
   saturation law; converting it requires a humidity assumption and a radiative
   kernel.
6. **Quoting a cloud feedback sign as settled.** Section 8 gives both signs from
   the same accounting model.
7. **Confusing $\beta$ with $\gamma$.** The first is concentration-driven, the
   second temperature-driven.
8. **Forgetting that feedbacks are derivatives of a state.** A single $\lambda$
   belongs to one climate.

## Mastery checkpoint

Complete this without notes.

> A model has $\lambda_0 = -5.418$ W m⁻² K⁻¹ and assumed feedbacks: water
> vapour $+1.2$, albedo $+0.35$, cloud $+0.5$, carbon $+0.2$ (all W m⁻² K⁻¹),
> with $F_{2\times} = 3.7$ W m⁻².
> **(a)** Compute the total $\lambda$ and the equilibrium temperature change.
> **(b)** Compute the gain of each feedback and state which one most amplifies
> the response.
> **(c)** The cloud feedback is uncertain over $[-0.4, +1.2]$. Recompute
> $\Delta T$ at both ends and state the implied range.
> **(d)** Explain in two sentences why the upper end of that range is not
> obtained by simply scaling the lower-end answer.
> **(e)** State one assumption that makes the whole calculation an idealisation,
> and one measurement that could in principle test it.

A worked version of (a)–(c) appears in the lesson-02
[solutions](exercises/02-climate-feedbacks-solutions.md).

## Common pitfalls

- **Adding gains instead of parameters.** Gains compose multiplicatively.
- **Forgetting that a feedback can change sign with state**, as the ice-albedo
  term does when it leaves its ramp.
- **Reporting $\lambda$ to three figures from ranges that span a factor of two.**
- **Treating the carbon feedback as instantaneous.** It acts over decades to
  centuries.
- **Assuming a single "climate sensitivity" number exists independent of the
  feedback definitions used to obtain it.**

## Related modules

- [01 Components of the Climate System and Their Timescales](01-climate-system-components.md) —
  the timescales that make the transient response differ from the equilibrium
  one.
- [03 Climate Sensitivity: Definitions and Estimation](03-climate-sensitivity.md) —
  how $\lambda$ and $F_{2\times}$ are combined into equilibrium and transient
  sensitivities, and how well each can be estimated.
- [05 The Carbon Cycle: Reservoirs, Fluxes and Perturbations](05-carbon-cycle.md) —
  the reservoirs and fluxes behind $\beta$ and $\gamma$.
- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  the radiative transfer that the feedback parameters summarise.
- [16-06 Palaeoclimate](../06-palaeoclimate/README.md) —
  the only empirical windows on feedbacks operating far from the present state.
- [18-05 Bayesian Inversion](../../18-inverse-problems/05-bayesian-inversion/README.md) —
  the machinery for turning uncertain ranges into a posterior distribution.
