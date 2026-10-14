---
id: 16-01-04
title: "Moisture, Humidity Variables and Cloud Formation"
level: advanced
prereqs: ["16-01-01", "16-01-03", "02-05-07"]
tags: [atmosphere, climate, moisture, humidity, clausius-clapeyron, clouds, cape, latent-heat]
---

# Moisture, Humidity Variables and Cloud Formation

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Clausius–Clapeyron relation for the saturation vapour pressure
   and **compute** its relative sensitivity $L_v/(R_vT^2)$, showing that
   saturation vapour pressure rises about $6.5\%$ per kelvin at $288\ \mathrm{K}$.
2. **Convert** between vapour pressure $e$, mixing ratio $w$, specific humidity
   $q$, relative humidity and dewpoint, and **state which of them is conserved**
   in which process.
3. **Compute** the lifting condensation level exactly, and **quantify** the error
   of the $125\ \mathrm{m\,K^{-1}}$ rule of thumb.
4. **Derive** the saturated (moist) adiabatic lapse rate and **show** that it
   approaches the dry adiabat as $w_s \to 0$ — an independent check on the formula.
5. **Explain** why moist static energy is conserved only to first order in the
   buoyancy, and **identify** the exactly conserved quantity instead.
6. **Compute** a lifting condensation level, level of free convection, level of
   neutral buoyancy and CAPE for a parcel, and **state** every assumption that
   makes CAPE an upper bound.
7. **Distinguish** what is measured (temperature, humidity, pressure), what is
   modelled (the parcel path) and what is inferred (CAPE, the cloud base).

## Prerequisites

- [01 Atmospheric Composition and Vertical Structure](01-atmospheric-composition.md) —
  $R_d$, $R_v$ and the virtual temperature.
- [03 Adiabatic Processes, Lapse Rates and Stability](03-thermodynamic-processes.md) —
  the dry adiabat, $\theta$ and the buoyancy frequency.
- [02-05-07 Phase Equilibria](../../02-physics/05-thermodynamics/07-phase-equilibria.md) —
  latent heat and the Clapeyron equation in its general form.

The general thermodynamics of phase changes is in
[02-05 Thermodynamics and Heat Transfer](../../02-physics/05-thermodynamics/README.md)
and is not repeated; this lesson specialises it to the vapour–liquid equilibrium of
water in air.

> **All models and data in this module are SYNTHETIC.** The surface state, the
> relative humidity and the environmental lapse rate below are chosen inputs of a
> teaching model. The constants used (latent heat, reference vapour pressure, gas
> constants) are standard constants and are identified as such.

## 1. Intuition: one number per kelvin, and everything that follows from it

Water vapour is a trace gas — a few grams per kilogram — and it dominates the
atmosphere's energy budget anyway. The reason is a single thermodynamic fact:

$$\frac{1}{e_s}\frac{\mathrm{d}e_s}{\mathrm{d}T} = \frac{L_v}{R_vT^2}
= \frac{2.501\times10^6}{461.5 \times 288.15^2} = 6.53\times10^{-2}\ \mathrm{K^{-1}}.$$

Warm air can hold **$6.5\%$ more water vapour per kelvin**. That one number drives
the following chain, which is the subject of this lesson:

- **Cloud formation.** Lift a parcel and it cools adiabatically. Because
  $e_s$ falls steeply with temperature, a modest ascent (a few hundred metres in
  a humid boundary layer) brings the parcel to saturation. The height at which
  that happens is the **lifting condensation level**, the physical cloud base.
  In the model below, a surface with $T = 288.15\ \mathrm{K}$ and $80\%$ relative
  humidity reaches saturation at $424.5\ \mathrm{m}$.
- **A different lapse rate.** Once saturated, condensation releases latent heat and
  the parcel cools more slowly: at $288.15\ \mathrm{K}$ and $1013\ \mathrm{hPa}$
  the saturated lapse rate is $4.71\ \mathrm{K\,km^{-1}}$ against the dry
  $9.76\ \mathrm{K\,km^{-1}}$. That is why the *observed* tropospheric lapse rate is
  $6.5\ \mathrm{K\,km^{-1}}$ and not the dry adiabat
  ([03](03-thermodynamic-processes.md)).
- **Convection.** The extra buoyancy from latent heat is what lets a moist parcel
  reach the tropopause. In the model, raising the surface relative humidity from
  $0.70$ to $0.90$ turns a convectively dead sounding into one with
  $352\ \mathrm{J\,kg^{-1}}$ of CAPE.
- **Sensitivity to warming.** If the temperature rises and relative humidity stays
  the same, the water-vapour content rises at $6.5\%\ \mathrm{K^{-1}}$. That is a
  *physical* consequence of Clausius–Clapeyron, and it is the largest single
  amplifier in the climate system — but the *assumption that relative humidity
  stays the same* is a modelling statement, and it is examined in
  [16-04-02](../04-climate-system-and-feedbacks/02-climate-feedbacks.md). Keep the
  two apart: the $6.5\%$ is thermodynamics; the constancy of relative humidity is
  an inference from models and observations.

## 2. Precise definitions

### 2.1 Humidity variables

For water vapour of partial pressure $e$ in air of total pressure $p$, with
$\varepsilon \equiv R_d/R_v = M_w/M_d = 0.622$:

$$w = \frac{m_v}{m_d} = \frac{\varepsilon e}{p - e}
\qquad\text{(mixing ratio, kg kg}^{-1}),$$

$$q = \frac{m_v}{m_v+m_d} = \frac{w}{1+w}
\qquad\text{(specific humidity, kg kg}^{-1}),$$

$$\mathrm{RH} = \frac{e}{e_s(T)},
\qquad T_d \text{ such that } e_s(T_d) = e
\qquad\text{(dewpoint)}.$$

The distinction $w$ versus $q$ is small ($w - q = w^2/(1+w)$, i.e.
$7.2\times10^{-5}\ \mathrm{kg\,kg^{-1}}$ at $w = 8.5\ \mathrm{g\,kg^{-1}}$) but it
is not always negligible, and they are conserved in slightly different processes.

### 2.2 Saturation vapour pressure

Clausius–Clapeyron, integrated over a constant latent heat:

$$e_s(T) = e_{s0}\exp\left[\frac{L_v}{R_v}\left(\frac{1}{T_0} - \frac{1}{T}\right)\right],
\qquad e_{s0} = 611.2\ \mathrm{Pa},\; T_0 = 273.15\ \mathrm{K},$$

with $L_v = 2.501\times10^{6}\ \mathrm{J\,kg^{-1}}$. The formula is an
*approximation* — $L_v$ falls with temperature, and the reference state $e_{s0}$ is
a measured value — but it is accurate to a few per cent over the range of the
troposphere, which is why it is used everywhere.

### 2.3 Condensation levels and convective energy

- **Lifting condensation level (LCL).** The height at which an unsaturated parcel
  lifted adiabatically first becomes saturated. This is the cloud base for
  convective clouds.
- **Level of free convection (LFC).** The height above which the parcel is warmer
  than its environment, so it accelerates.
- **Level of neutral buoyancy (LNB).** The height above which it is colder again.
- **CAPE.** The integral of the buoyancy between the LFC and the LNB:

$$\mathrm{CAPE} = \int_{z_{\mathrm{LFC}}}^{z_{\mathrm{LNB}}}
g\,\frac{T_p(z) - T_e(z)}{T_e(z)}\,\mathrm{d}z \qquad (\mathrm{J\,kg^{-1}}).$$

$\mathrm{CAPE}$ is an energy per unit mass; $\sqrt{2\,\mathrm{CAPE}}$ is the
speed a ballistically converted parcel could reach, and it is an **upper bound**
(§6).

### 2.4 Moist static energy, and one warning

$$h_m \equiv c_p T + gz + L_v q .$$

It is the standard conserved tracer for moist convection, and it is **not exactly
conserved** for a parcel embedded in an environment of a different temperature.
Section 3.5 derives the exact statement:

$$\frac{\mathrm{d}h_m}{\mathrm{d}z} = -\text{buoyancy}
= g\left(1 - \frac{T_p}{T_e}\right),$$

which is zero only to first order in the buoyancy perturbation. The exactly
conserved quantity is the entropy, equivalently $\theta$ while the parcel is dry.
Reporting a moist static energy budget without this caveat is one of the most
common overclaims in the subject.

## 3. Derivations

### 3.1 The Clausius–Clapeyron relation

The Clapeyron equation for a phase equilibrium with specific volumes
$v_v \gg v_l$ and treating the vapour as ideal:

$$\frac{\mathrm{d}e_s}{\mathrm{d}T} = \frac{L_v}{T(v_v - v_l)}
\approx \frac{L_v}{T v_v} = \frac{L_v e_s}{R_v T^2},$$

using $v_v = R_vT/e_s$. Separating variables and integrating from
$(T_0, e_{s0})$ to $(T, e_s)$:

$$\int \frac{\mathrm{d}e_s}{e_s} = \int\frac{L_v}{R_v}\frac{\mathrm{d}T}{T^2}
\;\Longrightarrow\;
\ln\frac{e_s}{e_{s0}} = \frac{L_v}{R_v}\left(\frac{1}{T_0}-\frac{1}{T}\right),$$

which is the formula of §2.2. The relative sensitivity follows immediately:

$$\frac{1}{e_s}\frac{\mathrm{d}e_s}{\mathrm{d}T} = \frac{L_v}{R_vT^2}.$$

The demonstration evaluates it from $263$ to $303\ \mathrm{K}$:

| $T$ (K) | $e_s$ (hPa) | $\mathrm{d}e_s/\mathrm{d}T$ (hPa K⁻¹) | relative (%/K) |
|---|---|---|---|
| 263.15 | 2.8757 | 0.2251 | 7.826 |
| 273.15 | 6.1120 | 0.4439 | 7.263 |
| 283.15 | 12.3165 | 0.8325 | 6.759 |
| 288.15 | 17.1680 | 1.1205 | 6.527 |
| 293.15 | 23.6609 | 1.4921 | 6.306 |
| 303.15 | 43.5380 | 2.5674 | 5.897 |

$e_s$ nearly **doubles** between $283$ and $303\ \mathrm{K}$ (from $12.3$ to
$43.5\ \mathrm{hPa}$) while the temperature rises only $7\%$: the exponential is
the whole story.

### 3.2 Saturation mixing ratio and the dewpoint

Combining $w = \varepsilon e/(p-e)$ with $e = e_s(T)$:

$$w_s(T,p) = \frac{\varepsilon\,e_s(T)}{p - e_s(T)}
\;\approx\; \varepsilon\frac{e_s(T)}{p}$$

(the approximation in the last step is the one that appears inside the standard
moist-lapse-rate formula, and §3.5 measures its cost: about
$e_s/p = 1.3\%$ here). The dewpoint inverts the same relation:

$$T_d = \left[\frac{1}{T_0} - \frac{R_v}{L_v}\ln\frac{e}{e_{s0}}\right]^{-1}.$$

For the model surface state, $T = 288.15\ \mathrm{K}$, $p = 101325\ \mathrm{Pa}$,
$\mathrm{RH} = 0.80$: $e = 1373.44\ \mathrm{Pa}$,
$w = 8.547\ \mathrm{g\,kg^{-1}}$, $q = 8.474\ \mathrm{g\,kg^{-1}}$,
$T_d = 284.771\ \mathrm{K}$ ($11.62\ \mathrm{^\circ C}$), a dewpoint depression of
$3.379\ \mathrm{K}$.

**What is conserved.** Lifting an unsaturated parcel conserves $w$ (mass of
vapour per mass of dry air) exactly; it also conserves $q$ to the extent that
mass is neither added nor removed, but $w$ is the better variable because dry air
is the conserved carrier. **Relative humidity is not conserved** — it rises as the
parcel cools, which is the entire mechanism of cloud formation.

### 3.3 The lifting condensation level

The LCL is the height at which, following the dry adiabat upward,

$$w_s\bigl(T_p(z),\,p_e(z)\bigr) = w,$$

with $T_p(z) = \theta_p\,(p_e(z)/p_0)^{R_d/c_p}$ by $\theta$ conservation
([03 §3.2](03-thermodynamic-processes.md)) and $p_e$ the environmental pressure.
This is a one-dimensional root-finding problem — the demonstration solves it by
$60$ bisection steps, giving $z_L = 424.5\ \mathrm{m}$ and
$T_L = 284.017\ \mathrm{K}$ for the model state.

**The rule of thumb.** Linearising both sides about the surface gives

$$z_L \approx \frac{T - T_d}{\Gamma_d - \mathrm{d}T_d/\mathrm{d}z} \approx
\frac{T - T_d}{8\ \mathrm{K\,km^{-1}}}
\;\Longrightarrow\; z_L \approx 125\,\frac{\mathrm{m}}{\mathrm{K}}\,(T - T_d),$$

because the dewpoint falls with height at about $1.8\ \mathrm{K\,km^{-1}}$ against
the dry adiabat's $9.76$, leaving a closure rate near $8\ \mathrm{K\,km^{-1}}$.
For the model state the rule gives $422\ \mathrm{m}$ against the exact
$424.5\ \mathrm{m}$: **$+0.50\%$**, or $2.1\ \mathrm{m}$. The rule is a
linearisation, not a law; its error grows with the dewpoint depression and with
the height of the LCL. The divergence between the two is also a reminder that
"the cloud base" is a *diagnostic of a parcel model*, not a measured quantity —
what is measured is the temperature and humidity profile.

### 3.4 The saturated adiabatic lapse rate

Let $w_s$ decrease as the parcel rises; condensation releases $L_v\,\mathrm{d}w_s$
per unit mass. The first law for the parcel, with the environment's pressure
gradient $\mathrm{d}p/\mathrm{d}z = -\rho_e g$, is

$$c_p\frac{\mathrm{d}T}{\mathrm{d}z} + \frac{\rho_e}{\rho_p}g
= -L_v\frac{\mathrm{d}w_s}{\mathrm{d}z}.$$

Using $\mathrm{d}\ln w_s = \mathrm{d}\ln e_s - \mathrm{d}\ln p$ (the approximation
of §3.2), $\mathrm{d}\ln e_s/\mathrm{d}z = (L_v/(R_vT^2))\,\mathrm{d}T/\mathrm{d}z$
and $\mathrm{d}\ln p/\mathrm{d}z = -g/(R_dT_e)$, and keeping only the
$\rho_e = \rho_p$ case for clarity:

$$\boxed{\;\Gamma_m = \frac{g}{c_p}\,
\frac{1 + \dfrac{L_v w_s}{R_d T}}
{1 + \dfrac{L_v^2 w_s}{c_p R_v T^2}}\;}$$

**Two limits worth checking.** As $w_s \to 0$ (cold air) the two denominators
$\to 1$ and $\Gamma_m \to \Gamma_d$; the demonstration measures the ratio
$0.9968$ at $193.15\ \mathrm{K}$ and $100\ \mathrm{hPa}$, where
$w_s = 10.3\ \mathrm{mg\,kg^{-1}}$. As $w_s$ grows, $\Gamma_m$ falls:

| $T$ (K) | $p$ (hPa) | $w_s$ (g kg⁻¹) | $\Gamma_m$ (K km⁻¹) | $\Gamma_m/\Gamma_d$ |
|---|---|---|---|---|
| 303.15 | 1013 | 27.925 | 3.451 | 0.354 |
| 293.15 | 1013 | 14.871 | 4.221 | 0.432 |
| 288.15 | 1013 | 10.720 | 4.714 | 0.483 |
| 283.15 | 900 | 8.630 | 5.038 | 0.516 |
| 273.15 | 800 | 4.788 | 6.031 | 0.618 |
| 253.15 | 600 | 1.324 | 7.981 | 0.818 |
| 233.15 | 400 | 0.316 | 9.158 | 0.938 |

So a warm saturated parcel cools at **less than half** the dry rate. This is the
quantitative answer to the question posed in
[03](03-thermodynamic-processes.md): the observed $6.5\ \mathrm{K\,km^{-1}}$ is
neither the dry adiabat nor the near-surface saturated adiabat, but a
condensation-weighted average of the two, modified further by radiation
([16-02-02](../02-radiation-and-energy-balance/02-radiative-transfer-atmosphere.md)).

### 3.5 What is conserved, exactly

Integrating the model parcel through the environment and following
$h_m = c_pT + gz + L_vw$ gives a drift of **$+2104\ \mathrm{J\,kg^{-1}}$ over
$12\ \mathrm{km}$**, while $-\int \text{buoyancy}\,\mathrm{d}z = +2256\
\mathrm{J\,kg^{-1}}$: the two agree to $6.7\%$, which is the quadrature error of
the trapezoidal integral of a strongly curved profile. This confirms the identity

$$\frac{\mathrm{d}h_m}{\mathrm{d}z}
= \left(c_p\frac{\mathrm{d}T_p}{\mathrm{d}z} + g\right) + L_v\frac{\mathrm{d}w_s}{\mathrm{d}z}
= g\left(1 - \frac{\rho_e}{\rho_p}\right)
= g\left(1 - \frac{T_p}{T_e}\right) = -\text{buoyancy},$$

because the first law at $z$ reads
$c_p\,\mathrm{d}T_p/\mathrm{d}z + (\rho_e/\rho_p)g = -L_v\,\mathrm{d}w_s/\mathrm{d}z$.
**Moist static energy is conserved only when $T_p \approx T_e$.** Meanwhile
$\theta$ below the LCL is conserved *exactly*: the demonstration measures a span of
$1.1\times10^{-13}\ \mathrm{K}$ over the $425$ levels beneath the LCL, i.e. machine
precision.

### 3.6 The approximation inside $\Gamma_m$, located numerically

The derivation of §3.4 replaced $w_s = \varepsilon e_s/(p-e_s)$ by
$\varepsilon e_s/p$. Feeding the *same* approximation to both sides of the first
law at $z = 475\ \mathrm{m}$ (just above the LCL, where the saturated and dry
branches meet with a kink):

$$c_p\frac{\mathrm{d}T}{\mathrm{d}z} + \frac{\rho_e}{\rho_p}g
= 4.672393\ \mathrm{J\,kg^{-1}\,m^{-1}},$$

$$-L_v\frac{\mathrm{d}w_s}{\mathrm{d}z}\Big|_{\text{approx}} = 4.672393\
\mathrm{J\,kg^{-1}\,m^{-1}}, \qquad \text{residual } 3.6\times10^{-15},$$

$$-L_v\frac{\mathrm{d}w_s}{\mathrm{d}z}\Big|_{\text{exact}} = 4.735695\
\mathrm{J\,kg^{-1}\,m^{-1}}, \qquad \text{residual } -6.3\times10^{-2}.$$

The fractional residual of the exact version is
$0.01355$, and $e_s/p = 0.01340$ at that level. **The algebra is exact under its
own approximation, and the residual measures that approximation.**

## 4. Physical interpretation

- **The exponential is the mechanism.** Because $e_s$ grows exponentially with
  $T$, small height changes produce large changes in relative humidity. That is
  why cloud base sits at a few hundred metres and not at kilometres.
- **Saturation is a threshold, and thresholds make sharp features.** The LCL, the
  cloud base and the LFC all exist because a smooth cooling intersects a steeply
  rising capacity curve. The features are sharp in the model; in reality
  entrainment and mixing round them off.
- **Latent heat is an amplifier.** One gram per kilogram of condensate releases
  $2.501\ \mathrm{kJ\,kg^{-1}}$, and lifting $1\ \mathrm{kg}$ of air $1\ \mathrm{km}$
  costs only $9.81\ \mathrm{kJ\,kg^{-1}}$: condensate pays for about
  $0.26\ \mathrm{km}$ of ascent per gram per kilogram. Absorb the whole
  $8.5\ \mathrm{g\,kg^{-1}}$ of the model surface moisture and you can lift a
  parcel several kilometres — which is why moist convection reaches the
  tropopause.
- **CAPE is a moisture diagnostic, not a temperature one.** The demonstration
  changes nothing in the environment and finds no convection at
  $\mathrm{RH} = 0.70$, $87.5\ \mathrm{J\,kg^{-1}}$ at $0.80$, and
  $352\ \mathrm{J\,kg^{-1}}$ at $0.90$. Forecasting convection is therefore a
  humidity-forecasting problem, which is harder than a temperature-forecasting
  problem.
- **Cloud base is measurable, cloud depth is inferred.** A ceilometer measures the
  base; the LNB and the CAPE are computed from a *model of a parcel*, so they
  inherit every one of the idealisations in §6.

## 5. Worked numerical examples

**Example 1 — from relative humidity to dewpoint.**

Model state: $T = 288.15\ \mathrm{K}$, $p = 101325\ \mathrm{Pa}$, $\mathrm{RH} =
0.80$.

$$e_s(288.15) = 611.2\exp\left[\frac{2.501\times10^{6}}{461.5}
\left(\frac{1}{273.15}-\frac{1}{288.15}\right)\right] = 1716.80\ \mathrm{Pa},$$

$$e = 0.80 \times 1716.80 = 1373.44\ \mathrm{Pa},$$

$$w = \frac{0.622 \times 1373.44}{101325 - 1373.44} = \frac{854.28}{99951.6}
= 8.547\times10^{-3}\ \mathrm{kg\,kg^{-1}},$$

$$T_d = \left[\frac{1}{273.15} - \frac{461.5}{2.501\times10^{6}}
\ln\frac{1373.44}{611.2}\right]^{-1}
= \left[3.6610\times10^{-3} - 1.8451\times10^{-4}\times0.8090\right]^{-1}
= 284.771\ \mathrm{K}.$$

Check: $e_s(284.771) = 1373.4\ \mathrm{Pa} \approx e$ ✔. Dewpoint depression
$288.15-284.771 = 3.379\ \mathrm{K}$, and the rule of thumb gives
$125\times3.379 = 422\ \mathrm{m}$ against the exact $424.5\ \mathrm{m}$.

**Example 2 — the saturated lapse rate at two temperatures.**

At $T = 288.15\ \mathrm{K}$, $p = 1013.25\ \mathrm{hPa}$:
$w_s = 10.720\ \mathrm{g\,kg^{-1}}$,
$A = L_vw_s/(R_dT) = 2.501\times10^{6}\times0.010720/82710 = 0.3242$,
$B = L_v^2w_s/(c_pR_vT^2) = 1.7422$.

$$\Gamma_m = \frac{9.7614}{1}\times\frac{1.3242}{2.7422}
= 4.714\ \mathrm{K\,km^{-1}}.$$

At $T = 233.15\ \mathrm{K}$, $p = 400\ \mathrm{hPa}$:
$w_s = 0.316\ \mathrm{g\,kg^{-1}}$,
$A = 2.501\times10^{6}\times3.161\times10^{-4}/(287.041\times233.15) = 0.01181$,
$B = L_v^2w_s/(c_pR_vT^2) = 0.07846$:

$$\Gamma_m = 9.7614\times\frac{1.01181}{1.07846} = 9.158\ \mathrm{K\,km^{-1}}.$$

The ratio to $\Gamma_d$ moves from $0.483$ to $0.938$ — the same formula, two very
different atmospheres, and the direction of the change is what a cold upper
troposphere requires.

**Example 3 — CAPE and its moisture sensitivity.**

Environment: $\Gamma = 6.5\ \mathrm{K\,km^{-1}}$ to $11\ \mathrm{km}$, isothermal
above. Surface $T = 288.15\ \mathrm{K}$. Varying only the surface relative
humidity:

| RH | $w$ (g kg⁻¹) | LCL (m) | LFC (m) | LNB (m) | CAPE (J kg⁻¹) | $\sqrt{2\,\mathrm{CAPE}}$ (m s⁻¹) |
|---|---|---|---|---|---|---|
| 0.60 | 6.39 | 956 | — | — | — | — |
| 0.70 | 7.47 | 674 | — | — | — | — |
| 0.80 | 8.55 | 425 | 1541 | 5172 | 87.5 | 13.23 |
| 0.85 | 9.09 | 311 | 1025 | 5861 | 204.7 | 20.23 |
| 0.90 | 9.63 | 202 | 624 | 6437 | 352.1 | 26.54 |

At $\mathrm{RH} = 0.80$ the maximum buoyancy is $0.0363\ \mathrm{m\,s^{-2}}$, about
$0.4\%$ of $g$. These numbers are **upper bounds**: the parcel is assumed
undiluted, frictionless and unloaded. Real updraughts entrain environmental air,
which dilutes $\theta$ and $w$ and reduces CAPE substantially; that gap is exactly
what convective parameterisation has to model
([16-05-02](../05-climate-models/02-gcms-and-parameterisation.md)).

## 6. Assumptions and regime of validity

| Assumption | Where used | What breaks it |
|---|---|---|
| Constant $L_v = 2.501\times10^{6}\ \mathrm{J\,kg^{-1}}$ | Clausius–Clapeyron, $\Gamma_m$ | $L_v$ falls by about $2.4\ \mathrm{kJ\,kg^{-1}}$ per kelvin; over the tropospheric range this shifts $e_s$ by a few per cent |
| Reference state $e_{s0} = 611.2\ \mathrm{Pa}$ at $273.15\ \mathrm{K}$ | every $e_s$ value | It is a measured constant; the formula's absolute accuracy is $\sim1\%$ |
| Plane water surface; no curvature or solute effect | $e_s$ | Cloud droplets need supersaturation of order $1\%$ to nucleate; the Köhler correction is essential for cloud microphysics and is not in this model |
| Ideal gas for vapour | $w$, $T_v$ | Excellent below $50\ \mathrm{km}$ |
| $w_s \approx \varepsilon e_s/p$ | derivation of $\Gamma_m$ | Measured here as a $1.3\%$ residual in the energy identity (§3.6) |
| Unsaturated: $w$ conserved | LCL | Mixing with environment; also any condensation below the computed LCL, which happens on aerosol |
| Parcel keeps the environment's pressure | whole parcel model | Fails at the few-hPa level in violent updraughts |
| No entrainment | CAPE, LFC, LNB | The dominant error; real CAPE is smaller, often by a factor of two or more |
| No loading by condensate | CAPE | Precipitation-sized condensate adds weight and reduces buoyancy |
| No ice phase | $L_v$ only | Above the freezing level, freezing releases $L_f$ and the "moist" adiabat becomes the "saturated" one including ice; this module does not treat it |
| Static environment | LFC/LNB | Moving storms, wind shear and cold pools all change the answer |

**Climate-claim discipline.** Three statements of very different epistemic status
appear in this lesson's subject matter, and they must not be conflated:

1. *Clausius–Clapeyron* — physics, exact to the ideal-gas and constant-$L_v$
   approximations. Water-vapour capacity rises at about $6.5\%\ \mathrm{K^{-1}}$
   near the surface.
2. *Relative humidity stays roughly constant as the atmosphere warms* — an
   **inference** from observations and models, with uncertainties that are
   quantified in [16-04-02](../04-climate-system-and-feedbacks/02-climate-feedbacks.md).
   It is not implied by (1).
3. *Convective precipitation intensity increases* — a **modelled** consequence of
   (1) and (2), conditional on the parameterisation of convection itself, and one
   of the largest structural uncertainties in climate projection.

This module supplies only (1) and the machinery to compute the parcel diagnostics.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| Vapour pressure | $e, e_s$ | Pa | |
| Mixing ratio, specific humidity | $w, q$ | kg kg⁻¹ | often g kg⁻¹ |
| Relative humidity | RH | dimensionless | 0–1 |
| Dewpoint | $T_d$ | K | |
| Latent heat (specific) | $L_v$ | J kg⁻¹ | |
| $L_v/(R_vT^2)$ | | K⁻¹ | $(\mathrm{J\,kg^{-1}})/((\mathrm{J\,kg^{-1}\,K^{-1}})\mathrm{K^2})$ ✔ |
| Saturated lapse rate | $\Gamma_m$ | K m⁻¹ | |
| CAPE | | J kg⁻¹ = m² s⁻² | $\sqrt{2\,\mathrm{CAPE}}$ is m s⁻¹ ✔ |
| Moist static energy | $h_m$ | J kg⁻¹ | $c_pT$ ✔, $gz$ ✔, $L_vq$ ✔ |

The unit check that catches most errors: $L_v w_s/(R_d T)$ must be **dimensionless**
(it is a ratio of two specific energies divided by a temperature times a gas
constant, i.e. $\mathrm{J\,kg^{-1}}/\mathrm{J\,kg^{-1}}$), while $L_v^2w_s/(c_pR_vT^2)$
is also dimensionless. If either comes out with units, a gas constant has been
misplaced.

## 8. Python demonstration

[`code/moisture_and_clouds_demo.py`](code/moisture_and_clouds_demo.py) prints every
number above. It:

1. tabulates $e_s(T)$ and the Clausius–Clapeyron relative sensitivity;
2. converts a surface state between all the humidity variables, with two
   round-trip checks;
3. finds the LCL by $60$ bisection steps and compares it with the
   $125\ \mathrm{m\,K^{-1}}$ rule;
4. tabulates $\Gamma_m$ over seven states and checks the dry limit at
   $193\ \mathrm{K}$ and $213\ \mathrm{K}$;
5. integrates the moist adiabat $12\ \mathrm{km}$ upward with the environment's
   pressure gradient, verifies the exact conservation of $\theta$ below the LCL
   ($1.1\times10^{-13}\ \mathrm{K}$), shows that $h_m$ is *not* conserved and that
   its drift equals $-\int\text{buoyancy}\,\mathrm{d}z$, and locates the
   $w_s \approx \varepsilon e_s/p$ approximation by evaluating the first-law
   identity with both derivatives;
6. tabulates CAPE, LFC and LNB against surface relative humidity from $0.60$ to
   $0.90$;
7. converts condensation to latent heat and to kilometres of lift.

```bash
cd 16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python moisture_and_clouds_demo.py
```

## 9. Exercises

Graded problems with worked solutions:
[`exercises/04-moisture-and-clouds-exercises.md`](exercises/04-moisture-and-clouds-exercises.md)
and
[`exercises/04-moisture-and-clouds-solutions.md`](exercises/04-moisture-and-clouds-solutions.md).

## Mastery checkpoint

Without notes:

> A surface state has $T = 295\ \mathrm{K}$, $p = 1000\ \mathrm{hPa}$ and
> $\mathrm{RH} = 0.65$. **(a)** Compute $e_s$, $e$, the mixing ratio and the
> dewpoint. **(b)** Compute the LCL height two ways: exactly, and with the
> $125\ \mathrm{m\,K^{-1}}$ rule; state the difference. **(c)** Compute
> $\Gamma_m$ at the LCL and compare it with $\Gamma_d$. **(d)** State which of
> $w$, $q$, $\theta$, RH and $h_m$ is conserved between the surface and the LCL,
> and which is not, with one sentence of justification each. **(e)** Name two
> assumptions that make a CAPE computed for this parcel an upper bound.

## Common pitfalls

1. **Confusing mixing ratio with specific humidity.** They differ by
   $w^2/(1+w)$; at $20\ \mathrm{g\,kg^{-1}}$ that is $0.4\ \mathrm{g\,kg^{-1}}$,
   which is larger than many effects this folder later discusses.
2. **Treating relative humidity as conserved.** It is not: it rises as a parcel
   cools, which is why clouds form.
3. **Using $e_s(T)$ for $e$ when computing the LCL.** The parcel's vapour pressure
   falls as it rises and its pressure falls; the conserved quantity is $w$, and the
   balance is $w_s(T_p,p_e) = w$.
4. **Quoting the $125\ \mathrm{m\,K^{-1}}$ rule as physics.** It is a
   linearisation; measured error here $0.50\%$, and it grows.
5. **Applying the dry adiabat to a saturated parcel.** The error reaches a factor
   of two in $\Gamma$.
6. **Assuming moist static energy is exactly conserved.** The demonstration
   measures a $2104\ \mathrm{J\,kg^{-1}}$ drift; it equals
   $-\int\text{buoyancy}\,\mathrm{d}z$.
7. **Treating CAPE as an observation.** It is a model output conditional on an
   undiluted, frictionless, unloaded parcel; models disagree about it *because*
   the approximation fails differently.
8. **Extrapolating the $6.5\%\ \mathrm{K^{-1}}$ Clausius–Clapeyron sensitivity into
   a statement about precipitation.** It is one link in a chain of three
   (§6), two of which are modelled.
9. **Forgetting the ice phase above the freezing level.** Real convection above
   $0\ \mathrm{^\circ C}$ involves freezing and sublimation, which this lesson
   does not model.

## Related modules

- [01 Atmospheric Composition and Vertical Structure](01-atmospheric-composition.md) —
  $R_v$, the virtual temperature and the reason moist air is light.
- [02 Hydrostatic Balance and Pressure-Height Relations](02-hydrostatic-balance.md) —
  the pressure field the parcel is lifted through.
- [03 Adiabatic Processes, Lapse Rates and Stability](03-thermodynamic-processes.md) —
  the dry adiabat and $\theta$, the exactly conserved quantity below the LCL.
- [05 Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind](05-atmospheric-dynamics-basics.md) —
  what the condensation does once the flow is three-dimensional.
- [02-05-07 Phase Equilibria](../../02-physics/05-thermodynamics/07-phase-equilibria.md) —
  the Clapeyron equation in general.
- [01-12-01 Root Finding](../../01-mathematics/12-numerical-methods/01-root-finding.md) —
  the bisection method used for the LCL.
- [16-02-06 Aerosols, Clouds and Their Radiative Effects](../02-radiation-and-energy-balance/06-aerosols-and-clouds-radiation.md) —
  what the clouds formed here do to radiation.
- [16-03-03 Cyclones, Fronts and Severe Weather Dynamics](../03-atmospheric-circulation/03-storms-and-fronts.md) —
  where CAPE is consumed.
