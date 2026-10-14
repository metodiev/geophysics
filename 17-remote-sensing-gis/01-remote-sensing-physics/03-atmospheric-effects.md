---
id: 17-01-03
title: "Atmospheric Attenuation, Scattering and Correction"
level: graduate
prereqs: ["17-01-02", "16-02-02"]
tags: [remote-sensing, gis, atmosphere, radiative-transfer, atmospheric-correction, scattering]
---

# Atmospheric Attenuation, Scattering and Correction

The atmosphere is not a filter sitting between the surface and the sensor. It is
a participating medium: it absorbs, it scatters, and it emits. A sensor at the
top of the atmosphere therefore records three contributions that must be
separated before any surface property can be claimed:

1. radiation scattered or emitted by the atmosphere into the sensor's line of
   sight, which never reached the surface (**path radiance**);
2. radiation from the surface, attenuated on its way down and again on its way
   up (**transmittance**);
3. in the thermal region, radiation emitted by the atmosphere downward,
   reflected by the surface, and attenuated upward (**reflected sky**).

This lesson builds the equations that separate those terms, then measures what
happens when each is mishandled. The results are blunt. In the synthetic
example below, ignoring path radiance overestimates surface reflectance by
$+39.2\%$; a $10\%$ error in the estimated path radiance still leaves a $+3.9\%$
reflectance error; and a $10\%$ error in the optical depth becomes a $+5.5\%$
reflectance error because the correction is multiplicative along both legs.
Neglecting the thermal atmosphere entirely costs a few kelvin, but the individual
atmospheric terms are each worth about $11\%$–$15\%$ of the radiance and partly
cancel — so an uncorrected retrieval can look accurate for the wrong reason.

The lesson's honesty point is that atmospheric correction is an **inversion with
its own uncertainty budget**, not a preprocessing step. The corrected reflectance
is a number with an error bar that the correction's inputs set, and reporting one
without the other is the central overclaim of applied optical remote sensing.

All models and data in this module are **SYNTHETIC**. The atmosphere here is a
teaching model: a vertical optical depth split into a Rayleigh-like and an
aerosol-like component with an Ångström exponent, plus an isothermal emitting
layer. No measured optical depth, aerosol product or instrument is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Beer-Lambert law and the plane-parallel air mass, and **state**
   where the plane-parallel approximation fails.
2. **Derive** the Schwarzschild radiative-transfer equation and **solve** it for
   an isothermal layer.
3. **Separate** path radiance, transmittance and surface reflectance in a
   measured signal, and **quantify** the reflectance error from ignoring each.
4. **Derive** the Ångström exponent estimator and **explain** why it is exact for
   a power law and biased otherwise.
5. **Propagate** an optical-depth uncertainty to a reflectance uncertainty by
   linearisation and by Monte Carlo, and **explain** why the noise carries a
   small positive bias.
6. **Write** the thermal radiative-transfer equation including the reflected-sky
   term, and **compute** the temperature bias when terms are neglected.
7. **State** the assumptions of each correction and design a dark-object
   calibration with a stated uncertainty.

## Prerequisites

- [17-01-02 Reflectance, Emissivity and Spectral Signatures](02-reflectance-and-emissivity.md)
  — the Lambertian relation and Kirchhoff's law used throughout.
- [16-02-02 Radiative Transfer in the Atmosphere](../../16-atmosphere-climate/02-radiation-and-energy-balance/02-radiative-transfer-atmosphere.md)
  — the radiative-transfer equation and the atmospheric energy balance.

---

## 1. Intuition: three signals in one measurement

Point a radiometer at a dark lake from a hill on a hazy day. The radiance you
record is larger than the lake's reflected radiance, and the excess comes from
light scattered by the air between you and the lake. Now point the same
radiometer at a bright snowfield. The recorded radiance is *smaller* than the
snowfield's reflected radiance, because the atmosphere absorbed part of what left
the snow. The same atmosphere added to one measurement and subtracted from the
other, and the sign of the net effect depends on how bright the target is.

That is why the correction cannot be a single multiplicative scale factor. The
sensor radiance is

$$L_{\rm sensor} = L_{\rm path}
+ \underbrace{T_\uparrow}_{\text{up leg}}\;
\frac{\rho}{\pi}\,\underbrace{E_{\rm sun}T_\downarrow}_{\text{down leg}},
$$

an additive term plus a multiplicative one. Subtracting the additive term and
dividing by the multiplicative one are two different operations, and each has its
own error.

For a dark target the additive term dominates (it is *all* of the signal), so a
dark-object calibration is the natural way to estimate it. For a bright target the
multiplicative term dominates, so the optical depth matters more. Any correction
scheme must therefore be validated across the *contrast* of the scene, not at a
single target.

## 2. Precise definitions and units

### 2.1 Attenuation quantities

| Quantity | Symbol | Unit | Definition |
|---|---|---|---|
| extinction coefficient | $\kappa_\lambda$ | m⁻¹ | absorption + scattering per unit path length |
| vertical optical depth | $\tau_\lambda$ | dimensionless | $\int_0^{z_{\rm TOA}}\kappa_\lambda\,\mathrm{d}z$ |
| transmittance | $T_\lambda$ | dimensionless | $e^{-\tau_\lambda}$ for a vertical path |
| air mass | $m(\theta)$ | dimensionless | slant path length / vertical path length |
| path radiance | $L_{\rm path}$ | W m⁻² sr⁻¹ m⁻¹ | atmospheric radiance reaching the sensor |
| single-scattering albedo | $\omega_0$ | dimensionless | scattering / extinction |
| Ångström exponent | $\alpha$ | dimensionless | exponent in $\tau_{\rm aer}\propto\lambda^{-\alpha}$ |

### 2.2 Two scattering regimes

- **Rayleigh scattering** (molecules, particle radius $\ll \lambda$):
  $\tau \propto \lambda^{-4}$. Strong in the blue and the ultraviolet, weak in
  the infrared.
- **Mie/aerosol scattering** (particles comparable to $\lambda$): nearly
  wavelength-independent, often parameterised as $\tau_{\rm aer}(\lambda) =
  \tau_{\rm aer}(\lambda_0)(\lambda/\lambda_0)^{-\alpha}$ with $\alpha$ of order
  unity.

In the synthetic atmosphere of this lesson, $\tau_{\rm Ray}(0.55\,\mathrm{\mu m})
= 0.10$, $\tau_{\rm aer}(0.55\,\mathrm{\mu m}) = 0.15$ and $\alpha = 1.30$; the
two contributions are equal at $0.4733\ \mathrm{\mu m}$, so the molecular term
dominates in the blue and the aerosol term in the red — the usual situation.

## 3. Derivations

### 3.1 Beer-Lambert law and the air mass

For a beam crossing a slab with extinction $\kappa_\lambda$ and no emission,

$$\frac{\mathrm{d}L_\lambda}{L_\lambda} = -\kappa_\lambda\,\mathrm{d}s
\;\Longrightarrow\;
L_\lambda(s) = L_\lambda(0)\exp\!\left(-\int_0^{s}\kappa_\lambda\,\mathrm{d}s'\right)
= L_\lambda(0)e^{-\tau_\lambda(s)}.$$

A beam at zenith angle $\theta$ crosses a path a factor $m$ longer than the
vertical, so with a horizontally uniform atmosphere

$$\tau_{\rm slant} = \tau_{\rm vert}\,m,\qquad
m(\theta) = \sec\theta = \frac{1}{\cos\theta}\quad(\text{plane-parallel}).$$

*Numerical check.* With $\tau_{\rm vert}(0.55\,\mathrm{\mu m}) = 0.250$:

| $\theta$ | $m$ | $\tau_{\rm slant}$ | $T$ |
|---|---|---|---|
| $0°$ | 1.000 | 0.250 | 0.7788 |
| $45°$ | 1.414 | 0.354 | 0.7022 |
| $60°$ | 2.000 | 0.500 | 0.6065 |
| $75°$ | 3.864 | 0.966 | 0.3806 |
| $85°$ | 11.474 | 2.868 | 0.0568 |

The plane-parallel law diverges at the horizon as $\sec\theta\to\infty$, which is
unphysical: a real atmosphere is curved, the path length saturates, and above
roughly $80°$ a curved model or a table (relative optical mass) must be used.
**This is the first place where a correction fails, and it fails worst exactly
where satellite footprints are most oblique.**

### 3.2 The Schwarzschild equation and an isothermal layer

Include emission. With $\mathrm{d}\tau = -\kappa\,\mathrm{d}s$ measured downward
from the sensor, the radiance change along the line of sight is

$$\frac{\mathrm{d}L_\lambda}{\mathrm{d}\tau_\lambda} = -L_\lambda + B_\lambda(T),
\qquad\text{(the Schwarzschild equation)},$$

where $B_\lambda(T)$ is the Planck function of the local temperature and we have
ignored scattering. Integrating from the surface ($\tau = \tau_{\rm tot}$) to the
sensor ($\tau = 0$) with transmittance as the integrating factor:

$$L_\lambda(0) = L_\lambda(\tau_{\rm tot})e^{-\tau_{\rm tot}}
+ \int_0^{\tau_{\rm tot}} B_\lambda(T(\tau))e^{-\tau}\,\mathrm{d}\tau .$$

For an **isothermal** layer at temperature $T_a$ the integral is elementary:

$$L_\lambda(0) = L_{0}e^{-\tau_{\rm tot}} + B_\lambda(T_a)\left(1-e^{-\tau_{\rm tot}}\right).$$

*Numerical check (thermal).* At $10.8\ \mathrm{\mu m}$ with
$\tau_{\rm atm} = 0.85$, $\varepsilon = 0.95$, $T_s = 300\ \mathrm{K}$ and an
isothermal layer at $280\ \mathrm{K}$, the demonstration computes the radiance
budget:

| Term | Value (W m⁻² sr⁻¹ m⁻¹) | Share of sensor radiance |
|---|---|---|
| surface emission, $\varepsilon B(T_s)$ | $9.1859\times10^{6}$ | $100.29\%$ |
| reflected sky, $\tau(1-\varepsilon)B(T_a)$ | $2.9828\times10^{5}$ | $3.26\%$ |
| reduction of the surface term by $\tau$ | $-1.3779\times10^{6}$ | $-15.04\%$ |
| atmospheric up, $(1-\tau)B(T_a)$ | $1.0528\times10^{6}$ | $11.49\%$ |
| **sensor radiance** | $9.1591\times10^{6}$ | $100\%$ |

Inverting this radiance under four different assumed forward models gives:

| Assumed model | Retrieved $T$ (K) | Bias (K) |
|---|---|---|
| blackbody surface, no atmosphere | 296.422 | $-3.58$ |
| emissivity known, no atmosphere | 299.805 | $-0.20$ |
| $\tau$ and up term modelled, reflected sky ignored | 302.523 | $+2.52$ |
| full radiative transfer | 300.000 | $0.00$ |

The second row is the lesson of the thermal case. **The two largest atmospheric
effects — the $+11.5\%$ up term and the $-15.0\%$ transmittance factor — nearly
cancel**, so neglecting the atmosphere entirely looks almost correct here while
the individual errors are each worth several kelvin. A retrieval that is right
for the wrong reason will fail as soon as the atmosphere, surface temperature or
emissivity changes; the reflected-sky term alone is worth $+2.52\ \mathrm{K}$
when omitted (row 3).

### 3.3 Retrieving surface reflectance

Model the surface as Lambertian. Then the surface radiance is $\rho E/\pi$ with
$E$ the irradiance reaching it, and the sensor sees

$$L = L_{\rm path} + \frac{\rho}{\pi}E_{\rm sun}T_\downarrow T_\uparrow
\;\Longrightarrow\;
\boxed{\;\rho = \frac{\pi\left(L - L_{\rm path}\right)}
{E_{\rm sun}\,T_\downarrow T_\uparrow}\;.}$$

Three operations, three error sources, and the demonstration separates them:

- **Path radiance ignored** ($L_{\rm path}=0$): with
  $L_{\rm path} = 17.4587$, $L = 62.0365$, $T_\downarrow T_\uparrow = 0.5835$ and
  $E_{\rm sun} = 800\ \mathrm{W\,m^{-2}\,{\mu m}^{-1}}$, the true
  $\rho = 0.300$ is retrieved as $\rho = 0.4175$ — a $+39.2\%$ error.
- **Path radiance estimated from a dark object and $10\%$ too low**: retrieval
  gives $0.3117$, a $+3.9\%$ error. A good dark-object estimate is therefore
  worth more than a perfect transmittance.
- **Transmittance wrong**: see Section 3.4.

The retrieved value with the full correction is $0.3000$ — the arithmetic closes,
which is a check on the algebra, not on the atmosphere.

### 3.4 Sensitivity to the optical depth

Differentiate the boxed relation at fixed $L$ with respect to a common scaling
error in $\tau$ on both legs. Since $T_\downarrow T_\uparrow =
\exp[-\tau(m_\downarrow+m_\uparrow)]$,

$$\frac{\partial \ln\rho}{\partial \tau}
= -(m_\downarrow+m_\uparrow)
\;\Longrightarrow\;
\frac{\delta\rho}{\rho} \approx
-(m_\downarrow+m_\uparrow)\,\delta\tau .$$

With $m_\downarrow = \sec 30° = 1.1547$ and $m_\uparrow = 1$,
$m_{\rm round} = 2.1547$, so $\delta\tau = +0.025$ (a $10\%$ error on
$\tau = 0.250$) gives

$$\frac{\delta\rho}{\rho}
\approx -2.1547\times0.025 = -0.0539
\;\Longrightarrow\;
\rho \text{ retrieved } 5.5\% \textit{ too high}$$

(because the assumed transmittance was too small, so the data are divided by too
little). The demonstration measures $+5.53\%$, in exact agreement with the
first-order prediction $\exp(0.0539)-1$. **An optical-depth error is amplified by
the round-trip air mass, which is always greater than 2.**

### 3.5 The Ångström exponent

Parameterise the aerosol optical depth as a power law
$\tau_{\rm aer}(\lambda) = \tau_0(\lambda/\lambda_0)^{-\alpha}$. Taking the ratio
at two wavelengths and solving,

$$\boxed{\;\alpha = -\frac{\ln\!\left[\tau_{\rm aer}(\lambda_1)
\big/\tau_{\rm aer}(\lambda_2)\right]}
{\ln(\lambda_1/\lambda_2)}\;}.$$

The demonstration recovers $\alpha = 1.3000$ from either of the pairs
$(0.45,0.55)$ and $(0.55,0.65)\ \mathrm{\mu m}$, because the synthetic aerosol
*is* a pure power law. That exactness is the point: the estimator is algebraically
exact for the model, so any disagreement in a real retrieval measures departure
from the power law (or an error in one of the two optical depths), not a flaw in
the formula. The estimator is also very sensitive to errors at two wavelengths:
$\delta\alpha \approx \delta\tau/\tau / \ln(\lambda_2/\lambda_1)$, and
$\ln(0.65/0.55) = 0.167$, so a $1\%$ relative error in the ratio becomes
$\delta\alpha \approx 0.06$.

### 3.6 Convexity: why correction noise is biased

Even a *centred* uncertainty in $\tau$ biases the *mean* retrieved reflectance,
because the correction is a convex exponential. With
$\ln(\rho_{\rm ret}/\rho_{\rm true}) = \tau m_{\rm round} u$ and
$u\sim N(0,\sigma_u^2)$,

$$\mathbb{E}\!\left[\frac{\rho_{\rm ret}}{\rho_{\rm true}}\right]
= \exp\!\left(\tfrac{1}{2}\left(\tau m_{\rm round}\sigma_u\right)^{2}\right) > 1 .$$

The logical spread is
$\sigma_{\ln\rho} = \tau m_{\rm round}\sigma_u$. The demonstration's
$20\,000$-draw experiment returns $\rho = 0.3003 \pm 0.0161$, i.e. a relative
spread of $5.37\%$ against the predicted $5.39\%$, and a bias of
$+0.09\%\pm0.038\%$ against the predicted $+0.145\%$ — consistent within the
Monte Carlo standard error. **Averaging many uncertain atmospheric corrections
does not converge to the truth; it converges to the truth times a small positive
factor.**

## 4. Physical interpretation

- **Additive and multiplicative errors act on different targets.** A dark object
  is dominated by $L_{\rm path}$; a bright object by $T_\downarrow T_\uparrow$.
  Validate a correction on both ends of the contrast range.
- **The correction grows with air mass.** A scene acquired at $60°$ solar zenith
  needs a larger correction than the same scene at $30°$, which is why
  multi-temporal products must be corrected per acquisition, not with one
  coefficient.
- **Blue bands are the hardest.** In the synthetic atmosphere the Rayleigh share
  of the optical depth is $0.61$ at $0.40\ \mathrm{\mu m}$ and $0.12$ at
  $1.00\ \mathrm{\mu m}$, so a small absolute error in the aerosol term is a
  larger relative error in the blue.
- **The thermal atmosphere both adds and subtracts.** The up term adds
  $(1-\tau)B(T_a)$ ($+11.49\%$ of the sensor radiance in the demonstration); the
  transmittance factor removes $15.04\%$ of the surface term; and the
  reflected-sky term adds $\tau(1-\varepsilon)B(T_a)$ ($+3.26\%$). The two large
  terms nearly cancel, which is exactly why an uncorrected retrieval can look
  accurate ($-0.20\ \mathrm{K}$ in the demonstration) while being built on two
  errors worth several kelvin each.
- **Correction is an inversion.** It has a forward model, parameters, a
  residual and an uncertainty, exactly like the inversions in
  [18-inverse-problems](../../18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md).

## 5. Assumptions and regime of validity

1. **Horizontal homogeneity.** Air mass and optical depth are computed for a
   uniform atmosphere. Clouds, plumes and gradients break this outright.
2. **Plane-parallel geometry.** Valid to roughly $70°$–$80°$ zenith; a curved
   atmosphere is required beyond that.
3. **No multiple scattering** in the retrieval used here (single-scattering-like
   path radiance, and Schwarzschild without a scattering source). Multiple
   scattering matters at high optical depth and in the blue.
4. **Lambertian surface** for $\rho = \pi(L-L_{\rm path})/(E T_\downarrow
   T_\uparrow)$. A non-Lambertian surface needs a BRDF correction, and
   [17-01-02](02-reflectance-and-emissivity.md) measures how large that error is.
5. **Known illumination.** The direct-beam form assumes the surface irradiance is
   delivered by the direct beam times $T_\downarrow$; the diffuse fraction must
   be added separately.
6. **Known single-scattering albedo and phase function** for $L_{\rm path}$. In
   practice these are modelled, and that model is the dominant error in an
   operational correction.
7. **Local thermodynamic equilibrium and an isothermal layer** for the thermal
   solve. A real profile requires integrating $B(T(\tau))e^{-\tau}$ numerically.
8. **The synthetic parameter values are chosen teaching values.** The optical
   depths, Ångström exponent, layer temperature and single-scattering albedo are
   parameters of the demonstration, not atmospheric measurements.

## 6. Units and dimensional analysis

| Expression | Unit arithmetic | Result |
|---|---|---|
| $\tau = \int\kappa\,\mathrm{d}z$ | $\mathrm{m^{-1}}\cdot\mathrm{m}$ | dimensionless |
| $T = e^{-\tau}$ | dimensionless | dimensionless |
| $m = \sec\theta$ | m/m | dimensionless |
| $\rho = \pi(L-L_{\rm path})/(E T^2)$ | $\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}/\mathrm{W\,m^{-2}\,m^{-1}}$ | sr⁻¹·… → dimensionless when the $\pi$ is included |
| $\alpha = -\ln(\tau_1/\tau_2)/\ln(\lambda_1/\lambda_2)$ | $\ln(\cdot)/\ln(\cdot)$ | dimensionless |
| $(1-\tau)B(T_a)$ | $1\cdot\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$ | radiance |

The reflectance row is worth doing carefully. The Lambertian relation is
$L = \rho E/\pi$, so $\pi L/E = \rho$ and the result must be dimensionless. A
shortcut that produces a steradian instead means a factor of $\pi$ has been
misplaced: the $\pi$ is not a unit conversion but the solid-angle integral of the
hemisphere (derived in [17-01-02](02-reflectance-and-emissivity.md), Section 3.1).

## 7. Worked examples

### Example 1 — air mass and round-trip transmittance

Sun at $60°$ zenith, sensor at nadir, $\tau_{\rm vert} = 0.250$.

1. $m_\downarrow = \sec 60° = 2.000$, so $\tau_\downarrow = 0.500$ and
   $T_\downarrow = e^{-0.500} = 0.6065$.
2. $m_\uparrow = \sec 0° = 1.000$, so $T_\uparrow = e^{-0.250} = 0.7788$.
3. Round trip: $T_\downarrow T_\uparrow = 0.4724$.

Moving the sensor to a $60°$ view angle gives $T_\uparrow = 0.6065$ and a round
trip of $0.3679$ — a further $22\%$ loss. **View geometry is a first-order
radiometric variable, not a detail.**

### Example 2 — the cost of a bad path radiance

Using the demonstration's numbers, $L = 62.0365$, $T_\downarrow T_\uparrow =
0.5835$, $E_{\rm sun} = 800$:

$$\rho_{\rm full} = \frac{\pi\left(62.0365 - 17.4587\right)}{800\times0.5835}
= \frac{\pi\times44.5778}{466.8} = 0.3000,$$
$$\rho_{\rm no\ path} = \frac{\pi\times62.0365}{466.8} = 0.4175
\quad(+39.2\%),$$
$$\rho_{\rm dark\ 10\%\ low} = \frac{\pi\left(62.0365 - 15.7128\right)}{466.8}
= 0.3117\quad(+3.9\%).$$

A $10\%$ error in the *estimated* path radiance costs $3.9\%$ of reflectance;
ignoring it entirely costs $39\%$. The lesson is that the additive term must be
estimated, not assumed away.

### Example 3 — optical-depth error and its convexity bias

With $\tau = 0.250$, $m_{\rm round} = 2.1547$:

| $\delta\tau$ | predicted $\delta\rho/\rho$ | measured |
|---|---|---|
| $-20\%$ | $-10.2\%$ | $-10.21\%$ |
| $-10\%$ | $-5.4\%$ | $-5.24\%$ |
| $+10\%$ | $+5.5\%$ | $+5.53\%$ |
| $+20\%$ | $+11.4\%$ | $+11.38\%$ |

For a *random* $\tau$ error with $10\%$ standard deviation, the retrieved
reflectance spreads by $5.37\%$ and carries a small positive bias of order
$+0.1\%$: the exponential correction is convex, so its noise does not average
away.

### Example 4 — the thermal cancellation

Reading $L = 9.1591\times10^{6}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$ at
$10.8\ \mathrm{\mu m}$ as a blackbody surface temperature with no atmosphere
gives $296.42\ \mathrm{K}$ against a true surface of $300\ \mathrm{K}$: a bias of
$-3.58\ \mathrm{K}$. But with the emissivity known, the same "no-atmosphere"
retrieval returns $299.805\ \mathrm{K}$, only $-0.20\ \mathrm{K}$ from truth —
because the $+11.49\%$ atmospheric up term and the $-15.04\%$ transmittance
reduction nearly cancel. Omit only the reflected-sky term while modelling the
rest and the retrieval is $+2.52\ \mathrm{K}$ *too high*.

Since $\lambda k_BT^{2}/(hc) = 67.6\ \mathrm{K}$ at this wavelength
([17-01-02](02-reflectance-and-emissivity.md)), a $2.5\ \mathrm{K}$ bias
corresponds to about a $3.7\%$ error in the effective emissivity — the same order
as the emissivity uncertainty itself. **In the thermal infrared, atmospheric and
emissivity errors are comparable in size, they partly cancel, and they must be
solved together. A retrieval that is accurate for the wrong reason is a
coincidence that will not survive a change of atmosphere.**

## 8. Python demonstration

`code/atmospheric_correction_demo.py` prints, with units:

1. transmittance versus zenith angle for $\tau_{\rm vert}(0.55\,\mathrm{\mu m})
   = 0.250$, from $0.7788$ at nadir to $0.0568$ at $85°$;
2. round-trip transmittances for four sun/view geometry pairs
   ($0.5835$ down to $0.3679$);
3. the Ångström exponent, recovered as $1.3000$ from two wavelength pairs;
4. the path-radiance budget ($44.58$ surface, $17.46$ path, $62.04$ total in
   $\mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}$) and the three retrievals
   ($0.3000$, $0.4175$, $0.3117$);
5. the $±20\%$ optical-depth sensitivity table;
6. a $20\,000$-draw Monte Carlo ($\rho = 0.3003\pm0.0161$, spread $5.37\%$,
   bias $+0.09\%\pm0.038\%$ against a predicted $+0.145\%$);
7. the Rayleigh/aerosol split from $0.40$ to $1.00\ \mathrm{\mu m}$ and the
   equal-contribution wavelength $0.4733\ \mathrm{\mu m}$;
8. the thermal term budget and the four retrieved temperatures
   ($296.422$, $299.805$, $302.523$, $300.000\ \mathrm{K}$) showing the
   near-cancellation of the atmospheric terms.

Everything is generated in code; there is no file input and no network access.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-atmospheric-effects-exercises.md`](./exercises/03-atmospheric-effects-exercises.md)
and
[`exercises/03-atmospheric-effects-solutions.md`](./exercises/03-atmospheric-effects-solutions.md).

- **★** Compute $T$ for $\tau_{\rm vert} = 0.35$ at $\theta = 0°,45°,70°$.
- **★** Compute the round-trip transmittance for sun $45°$, view $30°$.
- **★★** Derive the reflectance-sensitivity relation and evaluate it for
  $\delta\tau/\tau = 5\%$.
- **★★** Estimate how large an Ångström exponent error a $2\%$ relative error in
  a two-wavelength optical-depth ratio produces.
- **★★★** Design a dark-object calibration and state its uncertainty and the
  reflectance it delivers at $+5\%$ and $+20\%$ error levels.

## Mastery checkpoint

Without notes: $\tau_{\rm vert}(0.55\,\mathrm{\mu m}) = 0.30$, sun at $40°$
zenith, view nadir, $E_{\rm sun} = 900\ \mathrm{W\,m^{-2}\,\mu m^{-1}}$,
$L = 55\ \mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}$,
$L_{\rm path} = 14\ \mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}$. **(a)** Compute
the round-trip transmittance. **(b)** Retrieve the surface reflectance. **(c)**
Compute the reflectance error if $L_{\rm path}$ is ignored. **(d)** State which
error source dominates and why.

## 10. Common pitfalls

1. **Dividing by transmittance without subtracting path radiance.** The
   $+39.2\%$ error in Section 3.3 is the size of this mistake.
2. **Using one correction coefficient for a whole time series.** Air mass and
   aerosol change between acquisitions.
3. **Applying the plane-parallel air mass at high zenith angles.** At $85°$ it
   predicts $T = 0.0568$; a curved atmosphere saturates well above that.
4. **Treating the correction as exact.** The Monte Carlo gives a $5.37\%$
   reflectance spread for a $10\%$ optical-depth uncertainty.
5. **Forgetting the reflected-sky term in the thermal infrared.** Omitting it
   while modelling the rest biases the retrieval $+2.52\ \mathrm{K}$ too high here.
6. **Assuming correction noise averages out** in a temporal composite. The
   exponential makes the noise positively biased at about the $0.1\%$ level here,
   and larger for larger uncertainties.
7. **Quoting a reflectance validation against a single bright target.** The
   additive and multiplicative errors trade places with target brightness.

## 11. Real-world applications

- **Multi-temporal composites.** Every composite of atmospherically corrected
  reflectance inherits a bias unless each acquisition's correction is
  consistent; Section 3.6 is the mechanism.
- **Ocean colour.** Over dark water the signal is almost entirely path radiance,
  which is why ocean-colour correction is the most demanding branch of the
  subject.
- **Thermal monitoring.** Land-surface-temperature products must model the
  atmosphere and the emissivity together (Section 7, Example 4), which is why
  they ship retrieval uncertainty layers.
- **Aerosol retrieval.** Running the correction backwards — assuming the surface
  and solving for $\tau$ — is one of the standard ways aerosol optical depth is
  estimated from space, with the Ångström exponent from two bands.
- **Validation networks.** Ground reflectance measurements are used to validate
  atmospheric correction, and their uncertainty sets the achievable accuracy of
  the product.

## 12. Further reading

- *Physical Principles of Remote Sensing* (Rees) — atmospheric transmission and
  correction in a single notation.
- *Radiative Transfer* (Chandrasekhar) — the Schwarzschild equation and its
  solutions.
- [16-02-02 Radiative Transfer in the Atmosphere](../../16-atmosphere-climate/02-radiation-and-energy-balance/02-radiative-transfer-atmosphere.md)
  — the atmospheric energy balance and profile.
- [02-10-03 Radiative Transfer, Blackbody Radiation and Kirchhoff's Law](../../02-physics/10-optics-and-photometry/03-radiative-transfer.md)
  — the radiative-transfer equation and its plane-parallel solutions.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related modules

- [01 The Electromagnetic Spectrum and Sensing Windows](01-em-spectrum-remote-sensing.md) —
  which wavelengths reach the surface at all.
- [02 Reflectance, Emissivity and Spectral Signatures](02-reflectance-and-emissivity.md) —
  the surface model this lesson corrects toward.
- [04 Spatial, Spectral, Temporal and Radiometric Resolution](04-resolution-concepts.md) —
  the noise floor below which correction errors stop mattering.
- [17-02-05 Change Detection and Time-Series Analysis](../02-optical-and-thermal-remote-sensing/05-change-detection.md) —
  why inconsistent corrections create spurious trends.
- [18-inverse-problems](../../18-inverse-problems/03-regularization/01-why-regularize.md)
  — the general treatment of a correction as a regularised inversion.

## 14. Self-assessment checklist

- [ ] I can compute a slant optical depth and transmittance from a zenith angle.
- [ ] I can solve the Schwarzschild equation for an isothermal layer.
- [ ] I can retrieve a reflectance and name the three error sources.
- [ ] I can derive the Ångström exponent and state its sensitivity.
- [ ] I can linearise a retrieval's sensitivity to an optical-depth error.
- [ ] I can explain why correction noise has a positive bias.
- [ ] I can write the thermal radiative-transfer equation with the reflected-sky term.
