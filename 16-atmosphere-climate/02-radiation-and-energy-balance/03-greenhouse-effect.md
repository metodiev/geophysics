---
id: 16-02-03
title: "The Greenhouse Effect: Physics, Not Rhetoric"
level: intermediate
prereqs: ["16-02-01", "16-02-02", "16-01-04"]
tags: [atmosphere, climate, greenhouse-effect, radiative-forcing, planck-response, saturation]
---

# The Greenhouse Effect: Physics, Not Rhetoric

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the greenhouse effect as an *emission-level* statement rather than a
   "trapping" statement, and **explain** why the two differ physically.
2. **Compute** the effective radiating temperature from a stated albedo and
   **compare** it with a stated surface temperature, distinguishing what is
   measured from what is modelled.
3. **Derive** the downwelling infrared flux a surface must receive to be in
   radiative balance at a given temperature, and **explain** why that flux is the
   direct observable of the greenhouse effect.
4. **Fit** a one-layer model to a surface temperature, and **state** why a good fit
   with one free parameter carries no explanatory power.
5. **Derive** the Planck response $4\sigma T^3$ and **compute** the
   no-feedback temperature change for an imposed forcing.
6. **Model** band saturation with an explicit line shape and **measure** the
   transition of the absorption deficit from linear to square-root scaling.
7. **Classify** statements about the greenhouse effect as measured, modelled or
   inferred, and **identify** the counterfactual assumptions each requires.

## Prerequisites

- [01 Solar and Terrestrial Radiation, Blackbody Laws](01-solar-and-terrestrial-radiation.md) —
  Planck, Wien, Stefan–Boltzmann, the factor four and the two spectra.
- [02 Radiative Transfer in the Atmosphere](02-radiative-transfer-atmosphere.md) —
  optical depth, the Schwarzschild equation, the one-layer model and the emission
  level.
- [16-01-04 Moisture, Humidity Variables and Cloud Formation](../01-atmospheric-structure-and-thermodynamics/04-moisture-and-clouds.md) —
  why water vapour is a radiatively active gas at all.

## 1. Intuition: it is not a blanket, and it does not trap anything

Three statements are commonly made about the greenhouse effect, and all three are
wrong in a way that matters.

1. **"The atmosphere traps heat."** It does not. At equilibrium the outgoing
   longwave flux at the top of the atmosphere equals the absorbed solar flux
   *whatever* the composition is; that is energy conservation and no opacity can
   change it. What opacity changes is the **temperature of the level from which the
   escaping radiation last came**. The planet must radiate at $T_e$; the surface
   must therefore be warmer than $T_e$ if the radiating level is above it.
2. **"Greenhouse gases act like a blanket."** A blanket suppresses convective and
   conductive loss. Greenhouse gases do not touch conduction; they exchange
   radiation, in both directions, at their own temperature. By Kirchhoff's law an
   absorber is an emitter, so the atmosphere does not block the outgoing flux — it
   *replaces* it with emission from colder air.
3. **"The effect is a theory."** It is not a hypothesis awaiting confirmation: the
   downwelling infrared it predicts is measured at the surface, and the
   spectrally resolved outgoing radiation shows the absorption structure it
   requires. What *is* uncertain — severely — is how the effect changes as
   composition changes, because that requires feedbacks and a counterfactual.

The clean way to state the physics is therefore:

> **A planet with an infrared-absorbing atmosphere radiates to space from a level
> above its surface. Because temperature falls with height in the troposphere, that
> level is colder than the surface. To balance the absorbed sunlight, the surface
> must be warmer than the effective radiating temperature by exactly the amount
> needed to raise the temperature at the emission level back to $T_e$.**

Everything in this lesson is either a derivation of that sentence or a
quantification of how much of it is measured, how much is modelled, and how much is
inferred.

## 2. Precise definitions

### 2.1 The three temperatures

| symbol | name | status |
|---|---|---|
| $T_e = ((1-a)S/(4\sigma))^{1/4}$ | effective radiating temperature | **model output** given a chosen albedo |
| $T_s$ | surface temperature | **measured** in reality; a chosen input here |
| $T_s - T_e$ | the greenhouse increment | **inferred**; a difference of the two |

With the standard solar constant $S = 1361\ \mathrm{W\,m^{-2}}$, a chosen albedo
$a = 0.30$ and an illustrative surface temperature of $T_s = 288.00\ \mathrm{K}$
(chosen input, not an assertion about the real Earth):

$$F = \frac{S(1-a)}{4} = 238.175\ \mathrm{W\,m^{-2}}, \qquad
T_e = \left(\frac{F}{\sigma}\right)^{1/4} = 254.578\ \mathrm{K} = -18.57\
\mathrm{^\circ C},$$

$$T_s - T_e = 33.42\ \mathrm{K}.$$

**An important caution repeated from
[01](01-solar-and-terrestrial-radiation.md):** $254.578\ \mathrm{K}$ is not "the
temperature the Earth would have without a greenhouse effect". It is the
temperature of a blackbody that absorbs $238.175\ \mathrm{W\,m^{-2}}$ and radiates
uniformly — a model. A world with the greenhouse gases removed but everything else
held fixed is a different model; a world with the atmosphere removed entirely is a
different planet, with a different albedo. **The counterfactual has to be
specified before the number means anything.**

### 2.2 Radiative forcing

A **radiative forcing** $\Delta F$ is the change in net radiative flux at some
level (conventionally the top of the atmosphere, or the tropopause) caused by a
change in composition, with everything else held fixed — including the temperature.
It has units $\mathrm{W\,m^{-2}}$ and it is a *model output* conditional on the
spectroscopic input and on the "everything else held fixed" convention. Two
different conventions (instantaneous, stratosphere-adjusted) give different
numbers for the same composition change; the difference is itself a modelling
statement.

### 2.3 The Planck response

If the whole planet warms by $\mathrm{d}T$ at constant composition, its emitted
flux rises by

$$\lambda_0 \equiv \frac{\mathrm{d}F}{\mathrm{d}T} = 4\sigma T^3
\qquad (\mathrm{W\,m^{-2}\,K^{-1}}).$$

This is the **Planck response**: the negative feedback that would stabilise the
planet with no other feedbacks at all. Every other feedback in
[16-04-02](../04-climate-system-and-feedbacks/02-climate-feedbacks.md) is measured
*relative to* it, which is why it must be computed rather than quoted.

## 3. Derivations

### 3.1 The energy budget of a surface that is warmer than $T_e$

A black surface at $T_s$ emits $\sigma T_s^4$ upward. In the model of this lesson
the surface absorbs all of the incident sunlight, $F$, and it must also receive a
downwelling infrared flux $D$ from the atmosphere. Balance:

$$\sigma T_s^4 = F + D
\;\;\Longrightarrow\;\;
D = \sigma T_s^4 - F .$$

With $T_s = 288.00\ \mathrm{K}$: $\sigma T_s^4 = 390.11\ \mathrm{W\,m^{-2}}$, so

$$D = 390.11 - 238.175 = 151.93\ \mathrm{W\,m^{-2}},$$

$$\frac{\sigma T_s^4}{F} = 1.638.$$

**So the surface radiates $64\%$ more than the planet absorbs, and the difference
comes back as infrared from the sky.** This is the greenhouse effect in its most
directly observable form: a pyrgeometer pointing at a clear sky measures a
downwelling flux of order $10^{2}\ \mathrm{W\,m^{-2}}$, not zero. Nothing in this
calculation is controversial, and nothing in it depends on the surface being warmed
*by* that flux — energy is conserved on both sides of it.

### 3.2 A one-layer fit, and why it explains nothing

The exact one-layer result of [02 §3.3](02-radiative-transfer-atmosphere.md) is
$\sigma T_s^4 = 2F/(2-\varepsilon)$. Solve it for the emissivity that reproduces
$T_s = 288.00\ \mathrm{K}$:

$$\varepsilon = 2 - \frac{2F}{\sigma T_s^4}
= 2 - \frac{2\times238.175}{390.11} = 2 - 1.22108 = 0.77892 .$$

| $\varepsilon$ | $T_s$ (K) | $T_s - T_e$ (K) |
|---|---|---|
| 0.0000 | 254.578 | 0.000 |
| 0.2500 | 263.220 | 8.642 |
| 0.5000 | 273.562 | 18.984 |
| 0.7500 | 286.320 | 31.741 |
| **0.7789** | **288.000** | **33.422** |
| 0.9000 | 295.618 | 41.040 |
| 1.0000 | 302.746 | 48.168 |

**One free parameter is enough.** That is the reason the fit is worthless as
explanation: the model has two inputs (the albedo, which sets $F$, and the
emissivity) and it is being asked to reproduce one number. A model with as many
parameters as targets cannot be falsified by those targets. Compare
[02 §3.7](02-radiative-transfer-atmosphere.md): a grey model matched to the
broadband flux gets the *sensitivity* to added absorber wrong by a factor of about
$2.4$, and the outgoing *spectrum* wrong in shape. The one-layer fit is a
convenient closure, not a theory.

### 3.3 The Planck response

Differentiate $F = \sigma T^4$:

$$\lambda_0 = 4\sigma T^3, \qquad
\lambda_0(T_e = 254.578\ \mathrm{K}) = 3.7423\ \mathrm{W\,m^{-2}\,K^{-1}},\
\qquad
\lambda_0(288\ \mathrm{K}) = 5.4181\ \mathrm{W\,m^{-2}\,K^{-1}} .$$

An imposed forcing $\Delta F$ therefore produces, with no feedbacks,

$$\Delta T_0 = \frac{\Delta F}{\lambda_0}:$$

| $\Delta F$ (W m⁻²) | $\Delta T_0$ (K) |
|---|---|
| 0.5 | 0.134 |
| 1.0 | 0.267 |
| 2.0 | 0.534 |
| 4.0 | 1.069 |

**Two things this does and does not say.** It does say that the conversion from
flux to temperature is arithmetically trivial *once the forcing is known*, and that
the coefficient is not a free parameter — it follows from $\sigma$ and $T_e$. It
does not say anything about the forcing from any particular change in composition:
that requires the spectroscopic absorption coefficients and the integration of
[02](02-radiative-transfer-atmosphere.md), and the resulting number is a
measurement-plus-model product. And it is emphatically *not* a climate
sensitivity: the real response includes water-vapour, lapse-rate, cloud, surface
albedo and carbon-cycle feedbacks
([16-04-02](../04-climate-system-and-feedbacks/02-climate-feedbacks.md)).

### 3.4 Band saturation, from the line shape

The reason the marginal effect of adding a greenhouse gas declines with the amount
already present is *not* that the greenhouse effect weakens; it is that the
**absorption lines saturate**. Take a single line with a Lorentz shape,

$$k(\nu) = \frac{S\,\alpha}{\pi\left[(\nu-\nu_0)^2 + \alpha^2\right]},$$

with $S$ the model line strength and $\alpha$ the model half-width, and define the
absorption deficit of the outgoing flux in a band relative to a transparent
atmosphere:

$$D(W) = \int \left[1 - e^{-k(\nu)W}\right] B_\nu(T_s)\,\mathrm{d}\nu .$$

With **explicitly synthetic** parameters ($\nu_0$ corresponding to a
$15\ \mu\mathrm{m}$ centre, $\alpha = 5.0\times10^{2}\ \mathrm{m^{-1}}$, and $S$
chosen so that the line-centre absorption coefficient times $W = 1$ equals $1.0$ —
these are model choices, not the parameters of any real line), the demonstration
measures:

| $W$ (relative) | $D$ (W m⁻²) | local slope $\mathrm{d}\ln D/\mathrm{d}\ln W$ |
|---|---|---|
| 0.001 | 0.006343 | — |
| 0.01 | 0.063284 | 0.9946 |
| 0.1 | 0.618697 | 0.9515 |
| 1 | 5.061772 | 0.7684 |
| 10 | 21.293201 | 0.5420 |
| 100 | 61.415418 | 0.3951 |
| 1000 | 131.334237 | — |

The band's total blackbody flux at $288\ \mathrm{K}$ over the modelled wavelength
range is $158.17\ \mathrm{W\,m^{-2}}$, so at $W = 1000$ the line absorbs $83\%$ of
it.

**Read the slopes.** At small $W$ the slope is $1.00$: the medium is thin and
doubling the absorber doubles the absorbed flux. As the line core saturates the
slope passes through $1/2$ (the *strong-line* regime, where only the wings grow and
their area grows as the square root of the amount), and it falls below $1/2$ once
even the wings saturate. **An approximately logarithmic dependence of forcing on
amount follows directly from this**, and it is a property of the line shape, not of
the greenhouse effect in general.

The corollary that matters for physics rather than arithmetic: **the marginal
greenhouse effect of an absorber is largest where the spectrum is not already
saturated.** That is why the weak bands and the edges of the atmospheric window
carry disproportionate weight, and why a broadband (grey) emissivity cannot
represent the response.

### 3.5 What a one-layer model gets wrong about sensitivity

Differentiating the exact one-layer result gives

$$\frac{\mathrm{d}T_s}{\mathrm{d}\varepsilon}
= \frac{T_s}{4(2-\varepsilon)},
\qquad
\frac{1}{T_s}\frac{\mathrm{d}T_s}{\mathrm{d}\varepsilon}
= \frac{1}{4(2-\varepsilon)}:$$

| $\varepsilon$ | $T_s$ (K) | $\mathrm{d}T_s/\mathrm{d}\varepsilon$ (K) | fractional per unit $\varepsilon$ |
|---|---|---|---|
| 0.30 | 265.135 | 38.990 | 0.14706 |
| 0.50 | 273.562 | 45.594 | 0.16667 |
| 0.7789 | 288.000 | 58.964 | 0.20474 |
| 0.85 | 292.351 | 63.555 | 0.21739 |
| 0.95 | 299.076 | 71.209 | 0.23810 |

**The fractional response grows with emissivity — this model does not saturate.**
That is a genuine property of the one-layer idealisation: with a single layer, the
atmosphere is either transparent or opaque, and there is no partially saturated
regime to flatten the response. The real saturation of §3.4 lives in the *spectrum*
and cannot be represented by a broadband emissivity. **Claiming that the one-layer
model demonstrates saturation — or, equally, that it demonstrates its absence — is
the commonest misuse of this model.** What it demonstrates is a monotone response
with a magnitude set by one fitted parameter.

## 4. Physical interpretation

- **The surface energy budget is not the planetary budget.** The surface emits
  $390\ \mathrm{W\,m^{-2}}$ while the planet absorbs $238\ \mathrm{W\,m^{-2}}$;
  the atmosphere supplies the difference. The surface is *not* in radiative balance
  with space, and any argument that treats it as such is wrong by construction.
- **The greenhouse effect is a temperature-offset statement.** Replace "traps heat"
  with "raises the height from which the planet radiates". Every quantitative
  consequence follows from the lapse rate and the opacity, as in
  [02 §3.6](02-radiative-transfer-atmosphere.md).
- **Water vapour dominates by mass and by effect, and it is a feedback, not a
  forcing.** Its concentration is set by temperature through Clausius–Clapeyron
  ([16-01-04](../01-atmospheric-structure-and-thermodynamics/04-moisture-and-clouds.md)),
  so it responds to a change instead of causing one; that distinction is the
  subject of the water-vapour feedback.
- **Saturation means diminishing returns, not no returns.** The measured slope
  falling from 1 to 0.4 means the effect per unit absorber shrinks, not vanishes.
- **The observable is the spectrum.** A single broadband flux can be reproduced by
  many compositions; the *spectral* distribution of the outgoing radiation, and its
  change, cannot.

## 5. Worked numerical examples

**Example 1 — the downwelling infrared flux.**

$$\sigma T_s^4 = 5.670374419\times10^{-8}\times288.00^4
= 5.670374419\times10^{-8}\times6.879707136\times10^{9}
= 390.11\ \mathrm{W\,m^{-2}},$$

$$D = 390.11 - 238.175 = 151.93\ \mathrm{W\,m^{-2}}.$$

The surface must therefore receive $152\ \mathrm{W\,m^{-2}}$ of infrared from the
sky to sit at $288\ \mathrm{K}$ with no other energy source. If instead the
downwelling flux were zero, the balance $\sigma T_s^4 = F$ would give
$T_s = T_e = 254.578\ \mathrm{K}$ — the airless-blackbody case. **That pair of
numbers, $288.00$ and $254.578\ \mathrm{K}$, is the entire quantitative content of
the "33 K" statement, and both are model quantities.** The observation that
supports it is the measured downwelling flux, not either temperature.

**Example 2 — the Planck response, and a forcing.**

$$\lambda_0 = 4\sigma T_e^3 = \frac{4F}{T_e}
= \frac{4\times238.175}{254.578} = 3.7423\ \mathrm{W\,m^{-2}\,K^{-1}},$$

using the identity $\sigma T^4 = F$ at the effective temperature, which makes the
arithmetic a one-liner and is also the cleanest check on the formula. For an
imposed $\Delta F = 2.0\ \mathrm{W\,m^{-2}}$:

$$\Delta T_0 = \frac{2.0}{3.7423} = 0.534\ \mathrm{K}.$$

**The honest reading.** This is what a blackbody in radiative balance does, and it
is *not* a prediction of the response to any real forcing. A real forcing of
$2\ \mathrm{W\,m^{-2}}$ would produce a different temperature change because
feedbacks act; whether the feedbacks amplify or damp, and by how much, is a
modelling question with a published literature and a large uncertainty, and it is
not answered here.

**Example 3 — saturation in numbers.**

From §3.4, going from $W = 0.01$ to $W = 0.1$ — a tenfold increase — raises the
deficit from $0.0633$ to $0.6187\ \mathrm{W\,m^{-2}}$, a factor of $9.78$: nearly
linear. Going from $W = 10$ to $W = 100$ raises it from $21.29$ to
$61.42\ \mathrm{W\,m^{-2}}$, a factor of only $2.88$ for the same tenfold increase.
**A factor of $3.4$ less effect for the same multiplicative change in absorber.**
That difference is the saturation, and it is the reason that the *first* addition
of a greenhouse gas to an atmosphere does much more than the tenth.

## 6. Assumptions and regime of validity

| Assumption | Where used | What breaks it |
|---|---|---|
| Blackbody surface | §§3.1–3.2 | Real surfaces have $\varepsilon \approx 0.9$–$1.0$ in the infrared; a slightly smaller $\varepsilon$ slightly weakens the estimate |
| All solar absorption at the surface | §3.1 | A real atmosphere absorbs about a quarter of the solar beam before it reaches the surface; the surface's own budget then differs |
| No convection, no latent heat | the surface budget | Convection and evaporation carry a large share of the surface energy; the radiative-only budget overstates the surface temperature, which is why §3.5's one-layer fit needs a fitted parameter rather than an ab initio one |
| Cloud-free | everything | Clouds both reflect sunlight and absorb infrared; their net effect is opposite in sign in the two bands and is the largest single structural uncertainty |
| Constant lapse rate | the emission-level picture | Inversions reverse it locally; the concept of a single emission level is a centroid, not a boundary |
| Constant relative humidity | nowhere in this lesson, but everywhere downstream | The water-vapour feedback requires it, and it is an inference from models and observations; it does not follow from Clausius–Clapeyron |
| "Everything else held fixed" for a forcing | §2.2 | The convention must be stated, and the stratospheric adjustment included, or the number is not comparable with any other |
| Lorentz line shape | §3.4 | Real lines have Voigt shapes and pressure/temperature dependence; the *scaling* measured here is robust, the magnitudes are not |

**Climate-claim discipline, stated as a table.** This lesson's material falls into
three categories, and conflating them is the error the lesson exists to prevent:

| statement | status | what it requires |
|---|---|---|
| The outgoing spectral radiance shows absorption features | **measured** | a spectrometer and its calibration |
| The surface receives a downwelling infrared flux | **measured** | a pyrgeometer and its calibration |
| $T_e = 254.578\ \mathrm{K}$ for $a = 0.30$ | **modelled** | the blackbody laws and a chosen albedo |
| The one-layer emissivity that fits a surface temperature | **modelled** | one fitted parameter |
| "The greenhouse effect is 33 K" | **inferred** | a specified counterfactual and a chosen albedo |
| The radiative forcing of a composition change | **modelled + measured** | measured line parameters, a computed band integral, a stated convention |
| The temperature response to a forcing | **modelled + inferred** | feedbacks, a climate model, and an evaluation exercise |

**Only the first two rows are observations.** Everything else is a computation
whose inputs must be stated.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| Flux density | $F$ | $\mathrm{W\,m^{-2}}$ | |
| Effective radiating temperature | $T_e$ | K | $(F/\sigma)^{1/4}$ ✔ |
| Downwelling infrared | $D$ | $\mathrm{W\,m^{-2}}$ | $\sigma T_s^4 - F$ ✔ |
| Emissivity | $\varepsilon$ | dimensionless | $[0,1]$ |
| Planck response | $\lambda_0$ | $\mathrm{W\,m^{-2}\,K^{-1}}$ | $4\sigma T^3$ ✔ |
| Radiative forcing | $\Delta F$ | $\mathrm{W\,m^{-2}}$ | |
| Absorption coefficient | $k$ | $\mathrm{m^{-1}}$ | product $kW$ dimensionless ✔ |
| Line strength | $S$ | $\mathrm{m^{-2}}$ | $S\alpha/\pi/\Delta\nu^2 \to \mathrm{m^{-1}}$ ✔ |

The check that catches a factor-of-four error: $F = \sigma T^4$ and
$\lambda_0 = 4\sigma T^3$, so $\lambda_0 = 4F/T$; at $T_e = 254.578\ \mathrm{K}$
with $F = 238.175\ \mathrm{W\,m^{-2}}$ this gives
$4\times238.175/254.578 = 3.742\ \mathrm{W\,m^{-2}\,K^{-1}}$ ✔.

## 8. Python demonstration

[`code/greenhouse_effect_demo.py`](code/greenhouse_effect_demo.py) prints every
number quoted above. It:

1. computes $F$, $T_e$, the illustrative $T_s$ and the increment $33.42\
   \mathrm{K}$;
2. computes the required downwelling infrared flux, $151.93\ \mathrm{W\,m^{-2}}$,
   and the ratio $\sigma T_s^4/F = 1.638$;
3. fits the one-layer emissivity to the illustrative surface temperature
   ($\varepsilon = 0.77892$) and tabulates $T_s(\varepsilon)$;
4. computes $\mathrm{d}T_s/\mathrm{d}\varepsilon$ and shows that the *fractional*
   response grows — the one-layer model does not saturate;
5. computes the Planck response $4\sigma T^3$ at four temperatures and the
   no-feedback temperature change for four forcings;
6. measures the absorption deficit of an **explicitly synthetic** Lorentz line as
   a function of column amount and reports the local logarithmic slope, showing the
   transition from $1.00$ through $0.54$ to $0.40$;
7. prints a measured/modelled/inferred classification of eight statements, and the
   counterfactual warning of §1.

```bash
cd 16-atmosphere-climate/02-radiation-and-energy-balance/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python greenhouse_effect_demo.py
```

## 9. Exercises

Graded problems with worked solutions:
[`exercises/03-greenhouse-effect-exercises.md`](exercises/03-greenhouse-effect-exercises.md)
and
[`exercises/03-greenhouse-effect-solutions.md`](exercises/03-greenhouse-effect-solutions.md).

## Mastery checkpoint

Without notes:

> A planet has $S = 1100\ \mathrm{W\,m^{-2}}$ at its orbital distance and
> $a = 0.25$, and its surface sits at $285\ \mathrm{K}$. **(a)** Compute $F$,
> $T_e$ and the increment, stating which are model outputs. **(b)** Compute the
> downwelling infrared flux the surface must receive, and the ratio
> $\sigma T_s^4/F$. **(c)** Fit the one-layer emissivity and state in one sentence
> what the fit does and does not show. **(d)** Compute the Planck response and the
> no-feedback temperature change for a forcing of $1.5\ \mathrm{W\,m^{-2}}$.
> **(e)** For a synthetic Lorentz line with $\alpha = 2\times10^{2}\ \mathrm{m^{-1}}$
> and a line-centre absorption coefficient times the reference column equal to
> $0.5$, state (without computing) whether the logarithmic slope of the absorption
> deficit at that column is nearer $1$ or nearer $1/2$, and why. **(f)** List every
> quantity in (a)–(d) that is an observation, and every one that is a computation.

## Common pitfalls

1. **Saying the atmosphere traps heat.** It exchanges radiation and changes the
   level from which the planet radiates; the outgoing flux at equilibrium is
   unchanged.
2. **Treating $254.578\ \mathrm{K}$ as an observation or as "the temperature
   without the greenhouse effect".** It is a blackbody model with a chosen albedo,
   and the counterfactual must be specified.
3. **Claiming a one-layer fit explains the greenhouse effect.** One fitted
   parameter reproducing one number explains nothing, and the same model gets the
   spectrum and the sensitivity badly wrong.
4. **Quoting a no-feedback $\Delta T$ as a climate sensitivity.** Feedbacks are
   omitted by construction; the number is a reference, not a prediction.
5. **Assuming the one-layer model shows saturation.** It does not; its fractional
   response grows monotonically. Saturation lives in the line shapes.
6. **Treating a forcing as a measured quantity.** It depends on a stated
   convention and on measured line parameters, and different conventions give
   different numbers.
7. **Confusing a change in water vapour with a forcing.** Water vapour responds to
   temperature; that makes it a feedback.
8. **Assuming the surface is in radiative balance with space.** It is not; the
   emission level is.

## Related modules

- [01 Solar and Terrestrial Radiation, Blackbody Laws](01-solar-and-terrestrial-radiation.md) —
  the two spectra and the factor four on which everything here rests.
- [02 Radiative Transfer in the Atmosphere](02-radiative-transfer-atmosphere.md) —
  the transfer equations and the emission level used throughout.
- [04 Earth Energy Balance and Global Mean Temperature](04-earth-energy-balance.md) —
  the observational budget, including the non-radiative terms omitted in §6.
- [05 Zero- and One-Dimensional Energy Balance Models](05-energy-balance-models.md) —
  where the fitted emissivity of §3.2 is replaced by physics.
- [06 Aerosols, Clouds and Their Radiative Effects](06-aerosols-and-clouds-radiation.md) —
  the scatterers whose omission is the largest structural uncertainty here.
- [16-01-04 Moisture, Humidity Variables and Cloud Formation](../01-atmospheric-structure-and-thermodynamics/04-moisture-and-clouds.md) —
  why water vapour's concentration follows temperature.
- [16-04-02 Feedbacks: Water Vapour, Ice-Albedo, Cloud, Carbon](../04-climate-system-and-feedbacks/02-climate-feedbacks.md) —
  what turns a Planck response into a climate sensitivity.
