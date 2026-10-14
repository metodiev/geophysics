---
id: 16-01-03
title: "Adiabatic Processes, Lapse Rates and Stability"
level: advanced
prereqs: ["16-01-01", "16-01-02", "02-05-02"]
tags: [atmosphere, climate, adiabatic, lapse-rate, potential-temperature, stability, buoyancy]
---

# Adiabatic Processes, Lapse Rates and Stability

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the dry adiabatic lapse rate $\Gamma_d = g/c_p$ from the first law
   applied to a parcel in hydrostatic balance, and **explain** why it contains no
   temperature or pressure.
2. **Derive** potential temperature $\theta = T(p_0/p)^{R_d/c_p}$ and **show**
   analytically and numerically that it is conserved on a dry adiabat.
3. **Relate** the vertical gradient of $\theta$ to the difference between the
   environmental and adiabatic lapse rates,
   $\mathrm{d}\theta/\mathrm{d}z = \theta(\Gamma_d-\Gamma)/T$.
4. **Derive** the buoyancy frequency $N^2 = (g/T)(\Gamma_d-\Gamma)$ from the
   vertical momentum equation, and **classify** an environment as stable, neutral
   or unstable from a lapse rate.
5. **Verify** the linear prediction $2\pi/N$ against a full nonlinear parcel
   integration, and **state** the amplitude regime in which they agree.
6. **Apply** conservation of dry static energy $c_p T + gz$ and of entropy
   $s = c_p\ln\theta$ to a lifted parcel.
7. **Distinguish** the dry adiabat from the observed mean tropospheric lapse rate
   and **state** which physics is missing.

## Prerequisites

- [01 Atmospheric Composition and Vertical Structure](01-atmospheric-composition.md) —
  $c_p$, $c_v$, $R_d$ and $\gamma$, derived from composition.
- [02 Hydrostatic Balance and Pressure-Height Relations](02-hydrostatic-balance.md) —
  the pressure–height relation used for the parcel's environment.
- [02-05-02 First Law, Work and Energy Balances](../../02-physics/05-thermodynamics/02-first-law.md) —
  the sign conventions and the difference between $c_p$ and $c_v$ paths.

## 1. Intuition: the atmosphere is stable because air cools when it rises

Push a balloon of air upward. It expands, because the pressure around it falls. In
expanding it does work on its surroundings, and if that work is not replaced by
heat the parcel's internal energy falls — so its temperature falls. That single
chain of reasoning gives the most important number in meteorology:

$$\Gamma_d = \frac{g}{c_p} = \frac{9.80665}{1004.64} = 9.7614\times10^{-3}\
\mathrm{K\,m^{-1}} = 9.7614\ \mathrm{K\,km^{-1}}.$$

Now compare that with the observed mean tropospheric lapse rate, about
$6.5\ \mathrm{K\,km^{-1}}$. The atmosphere cools *more slowly* with height than a
rising parcel would. That is the whole explanation of stratification: a parcel
lifted from the surface arrives at $1\ \mathrm{km}$ at $278.445\ \mathrm{K}$ while
its environment is at $281.650\ \mathrm{K}$, so it is **$3.205\ \mathrm{K}$
colder** and heavier than its surroundings, and sinks back. The troposphere
resists vertical motion; it is *statically stable*. Convection happens only where
something makes the actual lapse rate steeper than the adiabatic one, and
invariably that something is the release of latent heat (Section 6 and
[04](04-moisture-and-clouds.md)).

(The naive "cool by $\Gamma_d$ per kilometre" would give $278.389\ \mathrm{K}$;
the $0.056\ \mathrm{K}$ difference is the pressure-equilibrium subtlety explained
in §3.4, and it is a useful warning that the parcel is not simply a thermometer
carried up a dry adiabat.)

The gap between $6.5$ and $9.7614\ \mathrm{K\,km^{-1}}$ is not a detail. It is the
difference between a stably stratified atmosphere and a convecting one, and its
size sets the frequency at which a displaced parcel oscillates back, $N \approx
0.011\ \mathrm{s^{-1}}$, a period of about **$561\ \mathrm{s}$** at
$255\ \mathrm{K}$ (Section 3.4). That number appears in gravity-wave dynamics
([16-03-04](../03-atmospheric-circulation/04-atmospheric-waves.md)), in the
interpretation of radiosonde soundings, and in every stability index used in
forecasting.

## 2. Precise definitions

### 2.1 The parcel and the adiabatic assumption

A **parcel** is an imaginary blob of air, large enough to contain many molecules
and small enough that its boundaries are well defined, which is assumed to

- move without exchanging mass with its environment,
- exchange no heat with its environment ($\delta q = 0$),
- adjust its pressure instantaneously to that of its surroundings.

The first two are the **adiabatic** assumptions; the third is the *pressure
equilibrium* assumption and is the one that makes the mathematics local. Their
validity is examined in Section 6.

### 2.2 Lapse rate

$$\Gamma \equiv -\frac{\partial T}{\partial z}
\qquad \text{(positive when temperature decreases upward).}$$

Two lapse rates matter: the *environmental* $\Gamma$ (whatever the sounding says)
and the *parcel's* $\Gamma_d$ (set by adiabatic ascent).

### 2.3 Potential temperature

$$\boxed{\;\theta \equiv T\left(\frac{p_0}{p}\right)^{R_d/c_p},
\qquad p_0 = 1000\ \mathrm{hPa}\;}$$

The reference pressure $p_0$ is a **convention**: $\theta$ is the temperature a
parcel would have if it were brought adiabatically to $1000\ \mathrm{hPa}$. With
$R_d/c_p = 0.285715$, the model's surface air has

$$\theta = 288.150 \times \left(\frac{1000}{1013.250}\right)^{0.285715}
= 288.150 \times 0.996245 = 287.068\ \mathrm{K}.$$

Because $p_0$ is arbitrary, the *value* of $\theta$ is arbitrary up to a constant
factor; only differences and gradients of $\theta$ are physical. This is worth
saying out loud, because comparisons of $\theta$ between papers with different
reference pressures are otherwise meaningless.

### 2.4 Static stability and the buoyancy frequency

An environment is **statically stable** if a displaced parcel experiences a
restoring force, **neutral** if it does not, and **unstable** if the displacement
grows. The quantitative measure is the **buoyancy (Brunt–Väisälä) frequency**

$$N^2 \equiv \frac{g}{\theta}\frac{\mathrm{d}\theta}{\mathrm{d}z},$$

positive in a stable environment. For $\mathrm{d}\theta/\mathrm{d}z > 0$ the
air is stably stratified; $\mathrm{d}\theta/\mathrm{d}z < 0$ is unstable.

## 3. Derivations

### 3.1 The dry adiabatic lapse rate

The first law for a unit mass of air, in the form that uses enthalpy, is

$$\delta q = c_p\,\mathrm{d}T - \frac{1}{\rho}\,\mathrm{d}p .$$

This is the same law as $\delta q = c_v\,\mathrm{d}T + p\,\mathrm{d}(1/\rho)$; the
$c_p$ form is the convenient one because the parcel stays in pressure equilibrium
with its environment
([02-05-02](../../02-physics/05-thermodynamics/02-first-law.md)).

Adiabatic means $\delta q = 0$:

$$c_p\,\mathrm{d}T = \frac{1}{\rho}\,\mathrm{d}p .$$

The parcel's pressure follows its environment, so hydrostatic balance applies
([02 §3.1](02-hydrostatic-balance.md)):

$$\frac{\mathrm{d}p}{\mathrm{d}z} = -\rho g .$$

Substituting:

$$c_p\frac{\mathrm{d}T}{\mathrm{d}z} = \frac{1}{\rho}(-\rho g) = -g
\qquad\Longrightarrow\qquad
\boxed{\;\Gamma_d = \frac{g}{c_p}\;}$$

**Properties worth noting.** $\Gamma_d$ contains neither $T$ nor $p$: a dry
adiabat is a straight line in $T$–$z$, and $9.76\ \mathrm{K\,km^{-1}}$ is the same
at the surface and at $10\ \mathrm{km}$. It also depends on composition only
through $c_p$, so a hypothetical atmosphere of pure CO₂ would have a different
$\Gamma_d$: with $c_p$ higher for a triatomic gas, the lapse rate would be
*smaller*, and the atmosphere stiffer.

### 3.2 Conservation of potential temperature

Logarithmically differentiate $\theta = T(p_0/p)^{R_d/c_p}$ and use the
hydrostatic relation:

$$\frac{\mathrm{d}\ln\theta}{\mathrm{d}z}
= \frac{1}{T}\frac{\mathrm{d}T}{\mathrm{d}z}
- \frac{R_d}{c_p}\frac{1}{p}\frac{\mathrm{d}p}{\mathrm{d}z}
= \frac{1}{T}\left(-\Gamma\right)
+ \frac{R_d}{c_p}\frac{g}{R_d T},$$

where the last term uses $(1/p)\,\mathrm{d}p/\mathrm{d}z = -g/(R_d T)$. Therefore

$$\boxed{\;\frac{\mathrm{d}\ln\theta}{\mathrm{d}z}
= \frac{\Gamma_d - \Gamma}{T}\;}
\qquad\text{and, multiplying by }\theta,\qquad
\frac{\mathrm{d}\theta}{\mathrm{d}z} = \frac{\theta}{T}\left(\Gamma_d - \Gamma\right).$$

Setting $\Gamma = \Gamma_d$ gives $\mathrm{d}\theta/\mathrm{d}z = 0$: **a dry
adiabat is a line of constant $\theta$**. The demonstration verifies this by
integrating a dry adiabat $16\ \mathrm{km}$ upward: $\theta$ stays constant to
$7.8\times10^{-7}\ \mathrm{K}$, the residual being the truncation error of the
midpoint rule with $\mathrm{d}z = 1\ \mathrm{m}$ and not a physical drift.

### 3.3 From $\Gamma$ to $N^2$

Combining the definitions of §2.4 and the result of §3.2:

$$N^2 = \frac{g}{\theta}\frac{\mathrm{d}\theta}{\mathrm{d}z}
= \frac{g}{T}\left(\Gamma_d - \Gamma\right).$$

This is the key formula of the lesson:

- $\Gamma < \Gamma_d \Rightarrow N^2 > 0$: **stable**, and a displaced parcel
  oscillates at frequency $N$.
- $\Gamma = \Gamma_d \Rightarrow N^2 = 0$: **neutral**.
- $\Gamma > \Gamma_d \Rightarrow N^2 < 0$: **unstable**, displacement grows
  exponentially at rate $|N|$.

Note the two appearances of $g$: one in $\Gamma_d = g/c_p$, one in the prefactor
$g/T$. They do not cancel, and the reason is physical — one sets how fast a parcel
cools, the other how strong the buoyancy force is for a given temperature excess.

### 3.4 Buoyancy and the vertical momentum equation

For a parcel displaced upward by $\zeta$ from an equilibrium level, the only force
is buoyancy, which for a small temperature difference is

$$\ddot\zeta = g\,\frac{T_p - T_e}{T_e}
= g\,\frac{\theta_p - \theta_e}{\theta_e}.$$

Since the parcel conserves $\theta$ and the environment has
$\theta_e = \theta_e(0) + (\mathrm{d}\theta_e/\mathrm{d}z)\zeta$,

$$\theta_p - \theta_e = -\frac{\mathrm{d}\theta_e}{\mathrm{d}z}\zeta
\qquad\Longrightarrow\qquad
\ddot\zeta = -\frac{g}{\theta_e}\frac{\mathrm{d}\theta_e}{\mathrm{d}z}\,\zeta
= -N^2\zeta .$$

So the "adiabatic" oscillation is a harmonic oscillator with frequency $N$, and the
demonstration measures its period from a full nonlinear integration and compares
it with $2\pi/N$: at $288.15\ \mathrm{K}$ and $\Gamma = 6.5\ \mathrm{K\,km^{-1}}$
the prediction is $596.39\ \mathrm{s}$ and the measurement is $596.40\ \mathrm{s}$
($+0.002\%$). Agreement that good is possible because the amplitude is small
($200\ \mathrm{m}$, so the fractional temperature differences are $\sim10^{-3}$)
and because the environment is linear by construction.

**The pressure-equilibrium subtlety.** A parcel does not carry its own pressure
field; it takes the environment's. Combining $c_p\,\mathrm{d}T = (1/\rho_p)\,
\mathrm{d}p$ with the *environment's* gradient $\mathrm{d}p/\mathrm{d}z = -\rho_e g$
gives

$$\frac{\mathrm{d}T_p}{\mathrm{d}z} = -\frac{g}{c_p}\frac{\rho_e}{\rho_p}
= -\Gamma_d\,\frac{T_p}{T_e},$$

so the parcel's lapse rate is *slightly less* than $\Gamma_d$ once it is colder
than its environment. **The exact statement is the conservation of $\theta$**, and
the parcel's temperature at height $z$ is

$$T_p(z) = \theta_p\left(\frac{p_e(z)}{p_0}\right)^{R_d/c_p},$$

with $p_e$ the environment pressure. At $1\ \mathrm{km}$ in the $\Gamma = 6.5\
\mathrm{K\,km^{-1}}$ environment this gives
$T_p = 287.068(898.741/1000)^{0.285715} = 278.445\ \mathrm{K}$, whereas
$T_0 - \Gamma_d z = 278.389\ \mathrm{K}$: a difference of $0.056\ \mathrm{K}$,
which is larger than the $0.002\%$ agreement above and therefore matters.

### 3.5 Dry static energy and entropy

Two conserved quantities are used for a dry adiabat, and one of them needs a
caveat.

$$h \equiv c_p T + g z \quad \text{(dry static energy, J kg}^{-1})$$

is conserved **for the adiabat considered as its own hydrostatic profile**, because
then $\mathrm{d}h/\mathrm{d}z = c_p(-\Gamma_d) + g = 0$. Numerically the
demonstration finds $h = 289.487\ \mathrm{kJ\,kg^{-1}}$ at every level to within
$1.1\times10^{-7}\ \mathrm{J\,kg^{-1}}$.

**The caveat, stated because it is easy to get wrong.** A parcel moving through an
environment of a *different* temperature takes the environment's pressure
gradient, $\mathrm{d}p/\mathrm{d}z = -\rho_e g$, not its own. The first law then
gives

$$\frac{\mathrm{d}}{\mathrm{d}z}\left(c_p T_p + gz\right)
= -\frac{\rho_e}{\rho_p}g + g
= g\left(1 - \frac{T_p}{T_e}\right)
= -\text{buoyancy},$$

so $c_p T + gz$ is **not** conserved for an embedded parcel — it changes at exactly
the rate that the buoyancy force does work. What *is* exactly conserved is
$\theta$ (equivalently the entropy), as §3.2 shows; dry static energy is a
first-order-in-buoyancy approximation to the same idea. The distinction is
measured and quantified in
[04 §5](04-moisture-and-clouds.md), where the same identity for a moist parcel
shows that moist static energy is likewise conserved only to first order.

For entropy, $\mathrm{d}s = c_p\,\mathrm{d}\ln\theta$ for an ideal gas, so
conservation of $\theta$ is exactly conservation of $s$:

$$\Delta s = c_p\ln\frac{\theta_1}{\theta_0}.$$

Along the integrated adiabat this is $-2.7\times10^{-6}\
\mathrm{J\,kg^{-1}\,K^{-1}}$ — zero to the precision of the integration — whereas
adding $500\ \mathrm{J\,kg^{-1}}$ of heat at $T = 131.97\ \mathrm{K}$ raises $s$ by
$500/131.97 = 3.789\ \mathrm{J\,kg^{-1}\,K^{-1}}$. **The distinction between
"conserved up to numerical noise" and "changed by a measurable amount" is the
whole content of irreversibility**, and it is why latent heating
([04](04-moisture-and-clouds.md)) and radiation
([16-02-02](../02-radiation-and-energy-balance/02-radiative-transfer-atmosphere.md))
cannot be represented by an adiabatic model.

## 4. Physical interpretation

- **Stability is a comparison, not a property of the air.** Nothing about a
  thermometer reading at one height tells you whether the atmosphere is stable;
  only the *gradient* does.
- **$\theta$ is the natural vertical coordinate for a stable atmosphere.** Because
  it increases upward monotonically, it can be inverted to give $z(\theta)$; that
  is why isentropic analysis is standard. Where $\mathrm{d}\theta/\mathrm{d}z$
  changes sign, the coordinate folds and the analysis must change variables.
- **$N$ is the stiffness of the atmosphere.** Large $N$ means strong restoring
  force, fast oscillations and a short vertical wavelength for internal gravity
  waves ($\lambda_z = 2\pi U/N$). Small $N$ means nearly neutral stratification
  and easy vertical mixing.
- **The troposphere is stably stratified on average, convectively active locally.**
  A mean lapse of $6.5\ \mathrm{K\,km^{-1}}$ is far from neutral, but the
  day-to-day, place-to-place variation spans the neutral value and beyond: the
  superadiabatic layers of a hot afternoon boundary layer and of a tropical
  convective tower are precisely the cases where $\Gamma > \Gamma_d$.
- **Why the observed lapse rate is not the dry adiabatic one.** Two reasons, in
  order of importance: (i) **latent heat release** when water vapour condenses,
  which makes the effective moist lapse rate smaller than $\Gamma_d$ (quantified
  in [04](04-moisture-and-clouds.md)); (ii) **radiative heating and cooling**
  distributed through the column, which moves the profile toward a radiative
  equilibrium rather than an adiabatic one
  ([16-02-02](../02-radiation-and-energy-balance/02-radiative-transfer-atmosphere.md)).
  A dry-adiabatic troposphere is what a perfectly dry, convecting atmosphere would
  look like — a useful limit, not a description.
- **The stability of the surface layer is not the stability of the troposphere.**
  Radiation creates strong superadiabatic layers within centimetres of a hot
  surface while the layer above remains stable; the *relevant* depth must always
  be stated with the lapse rate.

## 5. Worked numerical examples

**Example 1 — the dry adiabat as a $T$–$p$ relation.**

A parcel leaves the surface at $T = 288.150\ \mathrm{K}$ with
$\theta = 287.068\ \mathrm{K}$. Along its own hydrostatic column the adiabat is
$p = p_0(\theta/T)^{c_p/R_d}$, i.e. a straight line in $T$–$z$ with slope
$-\Gamma_d$; the demonstration integrates it and finds, at $2\ \mathrm{km}$,

$$T = 288.150 - 9.7614\times2 = 268.627\ \mathrm{K}, \qquad
p = 792.642\ \mathrm{hPa}.$$

The analytic check uses the exponent $c_p/R_d = 3.5$ (not the $5.2561$ of the
$6.5\ \mathrm{K\,km^{-1}}$ profile):

$$p = 1013.250\left(\frac{268.627}{288.150}\right)^{3.5}
= 1013.250 \times 0.932249^{3.5} = 792.68\ \mathrm{hPa},$$

agreeing with the integrated value to $0.04\ \mathrm{hPa}$, which is the midpoint
rule's truncation error. The consistency check is that $\theta$ is recovered:

$$\theta = 268.627\left(\frac{1000}{792.642}\right)^{0.285715}
= 268.627 \times 1.068673 = 287.07\ \mathrm{K}.\;\checkmark$$

**Example 2 — is the layer stable, and by how much?**

Environment: $\Gamma = 6.5\ \mathrm{K\,km^{-1}}$, surface $\theta = 287.068\
\mathrm{K}$. At $1\ \mathrm{km}$ the environment is at $281.650\ \mathrm{K}$ and
$898.741\ \mathrm{hPa}$ ([01 §3.3](01-atmospheric-composition.md)), so

$$\theta_e = 281.650\left(\frac{1000}{898.741}\right)^{0.285715}
= 281.650 \times 1.030976 = 290.374\ \mathrm{K}.$$

A parcel lifted from the surface conserves its $\theta_p = 287.068\ \mathrm{K}$,
so $\theta_p - \theta_e = -3.306\ \mathrm{K}$: **the parcel is colder than its
environment in potential temperature**. Its actual temperature, from
$T_p = \theta_p(p_e/p_0)^{R_d/c_p}$, is
$287.068 \times 0.898741^{0.285715} = 278.445\ \mathrm{K}$, so the conventional
temperature difference is $-3.205\ \mathrm{K}$. The two differences are related
by the same factor: $\Delta\theta = \Delta T\,(p_0/p_e)^{R_d/c_p}$, i.e.
$-3.205 \times 1.030976 = -3.305\ \mathrm{K}$. ✔ No lifting energy is available;
the layer is stable.

From $\mathrm{d}\theta/\mathrm{d}z = (\theta/T)(\Gamma_d-\Gamma)$ and
$\Gamma_d - \Gamma = 3.2614\ \mathrm{K\,km^{-1}}$, using the surface temperature,

$$N^2 = \frac{g}{T}(\Gamma_d-\Gamma) = \frac{9.80665 \times 3.2614\times10^{-3}}
{288.15} = 1.1099\times10^{-4}\ \mathrm{s^{-2}},$$

$$N = 0.01054\ \mathrm{s^{-1}}, \qquad \frac{2\pi}{N} = 596.4\ \mathrm{s}.$$

At a mid-tropospheric $255\ \mathrm{K}$ the same algebra gives
$N^2 = 1.2542\times10^{-4}$, $N = 0.01120\ \mathrm{s^{-1}}$ and a period of
$561.0\ \mathrm{s}$ — a $6\%$ change from the surface value, purely because $T$
enters the prefactor $g/T$.

**Example 3 — a superadiabatic layer, and the buoyancy work.**

Take $\Gamma = 10.5\ \mathrm{K\,km^{-1}}$, steeper than adiabatic. Then

$$N^2 = \frac{9.80665}{288.15}\left(9.7614 - 10.5\right)\times10^{-3}
= -2.841\times10^{-5}\ \mathrm{s^{-2}}, \qquad |N| = 0.005014\ \mathrm{s^{-1}},
$$

an e-folding time of $199.4\ \mathrm{s}$. The demonstration integrates the full
nonlinear buoyancy force from rest and measures a logarithmic growth rate of
$0.004923\ \mathrm{s^{-1}}$ ($-1.8\%$): the discrepancy is *not* physics but the
signature of a release from rest, $z\propto\cosh(Nt)$, whose logarithmic slope
$N\tanh(Nt)$ lies below $N$ for all finite $t$.

The energy budget makes the same point. Integrating the buoyancy
$g(T_p-T_e)/T_e$ over the path, with $T_p$ from $\theta$ conservation, gives the
work that must be done *on* each kilogram of air to lift it $1\ \mathrm{km}$:

| environment | work on the parcel per kg | $T_p - T_e$ at $1\ \mathrm{km}$ |
|---|---|---|
| $\Gamma = 6.5\ \mathrm{K\,km^{-1}}$ (stable) | $+55.7\ \mathrm{J\,kg^{-1}}$ | $-3.206\ \mathrm{K}$ |
| $\Gamma = 8.5\ \mathrm{K\,km^{-1}}$ (weakly stable) | $+21.7\ \mathrm{J\,kg^{-1}}$ | $-1.240\ \mathrm{K}$ |
| $\Gamma = 10.5\ \mathrm{K\,km^{-1}}$ (unstable) | $-12.7\ \mathrm{J\,kg^{-1}}$ | $+0.726\ \mathrm{K}$ |

Negative work means the buoyancy force *does* work on the parcel, which is
therefore accelerating; the number is a one-dimensional analogue of convective
available potential energy, and its smallness ($12.7\ \mathrm{J\,kg^{-1}}$) is
exactly why dry convection is weak compared with moist convection. The latent heat
released by condensing $10\ \mathrm{g\,kg^{-1}}$ of water vapour is
$L_v \times 0.010 = 2.501\times10^{6} \times 0.010 = 2.5\times10^{4}\
\mathrm{J\,kg^{-1}}$ — three orders of magnitude more, which is why the real
troposphere convects where the dry one would not
([04](04-moisture-and-clouds.md)).

## 6. Assumptions and regime of validity

| Assumption | Where used | What breaks it |
|---|---|---|
| Adiabatic ($\delta q = 0$) | $\Gamma_d = g/c_p$, $\theta$ conservation | Radiation acts on hours–days, condensation on minutes: both are non-adiabatic. The dry adiabat is a *shorter-time* idealisation than it looks |
| Parcel stays in pressure equilibrium | the whole derivation | Fails when the vertical scale of the displacement approaches the scale over which the environment adjusts; for a thunderstorm updraught the pressure perturbation is a few $\mathrm{hPa}$ |
| No mixing with the environment | $\theta$ and $h$ conservation | Entrainment is the single largest error in real convective calculations; it dilutes $\theta$ and reduces buoyancy |
| Implicitly dry | $\Gamma_d$, all of §3 | Condensation caps the parcel's cooling at the *moist* adiabat, which for a warm moist boundary layer is closer to $4\text{–}6\ \mathrm{K\,km^{-1}}$; derived in [04](04-moisture-and-clouds.md) |
| Fixed $c_p$ | $\Gamma_d$ | $c_p$ varies by a few parts in $10^4$ with humidity and to three figures with temperature; irrelevant here, relevant for precision thermodynamics |
| Linear buoyancy (small $\Delta T$) | $\ddot\zeta = -N^2\zeta$ | At large amplitude the exact $g(T_p-T_e)/T_e$ is nonlinear; the demonstration's $0.002\%$ agreement is a statement about a $200\ \mathrm{m}$ amplitude, and it degrades quadratically with amplitude |
| Environment linear in $z$ | Examples 2 and 3 | Real soundings have inversions; then $N$ is a function of height and $2\pi/N$ is only a local period |

**A climate-claim caution.** Nothing in this lesson is a measurement of the
climate. Static stability is one of the quantities that *changes* when the
atmosphere warms, and the sign and size of that change are model-dependent: the
stratification can stabilise (warmer surface, similar tropopause) while the
convective available energy changes in the opposite direction. Those statements
require the radiative physics of [16-02](../02-radiation-and-energy-balance/README.md)
and the model evaluation of [16-05](../05-climate-models/README.md); this lesson
supplies only the diagnostic $N^2$ and the parcel logic.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| Lapse rate | $\Gamma, \Gamma_d$ | K m⁻¹ | often quoted in K km⁻¹ |
| $\Gamma_d = g/c_p$ | | K m⁻¹ | $(\mathrm{m\,s^{-2}})/(\mathrm{m^2\,s^{-2}\,K^{-1}})$ ✔ |
| Potential temperature | $\theta$ | K | $(p_0/p)$ dimensionless |
| Buoyancy frequency | $N$ | s⁻¹ | $\sqrt{(\mathrm{m\,s^{-2}})(\mathrm{K\,m^{-1}})/\mathrm{K}}$ ✔ |
| Period | $2\pi/N$ | s | |
| Dry static energy | $c_p T + gz$ | J kg⁻¹ | |
| Entropy change | $c_p\ln\theta$ | J kg⁻¹ K⁻¹ | |

The exponent $R_d/c_p = 0.285715$ is dimensionless and is the only exponent in the
definition of $\theta$; writing $c_p/R_d$ by mistake changes $\theta$ by a factor
of about $1.07$ at $500\ \mathrm{hPa}$ and would be caught immediately by the
check that $\theta \to T$ as $p \to 1000\ \mathrm{hPa}$.

## 8. Python demonstration

[`code/thermodynamic_processes_demo.py`](code/thermodynamic_processes_demo.py)
prints every number above. It:

1. computes $\Gamma_d$, $\kappa = R_d/c_p$, and states the one-line derivation;
2. integrates a dry adiabat $16\ \mathrm{km}$ upward with a second-order method and
   reports the total drift of $\theta$, $7.8\times10^{-7}\ \mathrm{K}$;
3. tabulates $N^2$, $N$ and $2\pi/N$ for seven lapse rates spanning the inversion
   ($-2\ \mathrm{K\,km^{-1}}$), neutral and superadiabatic cases;
4. integrates the nonlinear parcel equation for three stable cases and reports the
   measured period against $2\pi/N$ (agreement better than $0.01\%$), then does the
   unstable case and reports the measured growth rate against $|N|$ with the
   $\tanh$ explanation of the $1.8\%$ residual, and finally tabulates the buoyancy
   work needed to lift a parcel $1\ \mathrm{km}$ through three environments;
5. checks conservation of $c_p T + gz$;
6. computes $\Delta s$ along the adiabat and under a $500\ \mathrm{J\,kg^{-1}}$
   heat input.

```bash
cd 16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermodynamic_processes_demo.py
```

## 9. Exercises

Graded problems with worked solutions:
[`exercises/03-thermodynamic-processes-exercises.md`](exercises/03-thermodynamic-processes-exercises.md)
and
[`exercises/03-thermodynamic-processes-solutions.md`](exercises/03-thermodynamic-processes-solutions.md).

## Mastery checkpoint

Without notes:

> A synthetic sounding has $T = 295\ \mathrm{K}$ at $1000\ \mathrm{hPa}$ and
> $T = 279\ \mathrm{K}$ at $850\ \mathrm{hPa}$. **(a)** Compute the layer's
> mean lapse rate in $\mathrm{K\,km^{-1}}$, given the geometric thickness you must
> first obtain from the hypsometric equation. **(b)** Compute $\theta$ at both
> levels and state whether the layer is stable, neutral or unstable.
> **(c)** Compute $N^2$, $N$ and the oscillation period. **(d)** A parcel is
> lifted dry-adiabatically from the lower level; state whether it is positively or
> negatively buoyant at the upper level, and give the temperature difference.
> **(e)** State two assumptions you used and one way each could fail.

## Common pitfalls

1. **Using $\Gamma_d = 9.8\ \mathrm{K\,km^{-1}}$ as the atmospheric lapse rate.**
   It is the *dry adiabatic* rate. The observed mean tropospheric value is
   $6.5\ \mathrm{K\,km^{-1}}$, and the difference is the physics of this lesson.
2. **Confusing $\theta$ with $T$.** They coincide only at $p = 1000\
   \mathrm{hPa}$. At $500\ \mathrm{hPa}$ with $T = 250\ \mathrm{K}$,
   $\theta = 250 \times 2^{0.285715} = 304.75\ \mathrm{K}$ — a difference of
   $54.8\ \mathrm{K}$.
3. **Taking a stability sign from the sign of $\mathrm{d}T/\mathrm{d}z$ alone.**
   An isothermal layer is *stable* (if a little unusual),
   $N = 0.0194\ \mathrm{s^{-1}}$, because temperature falls more slowly than
   adiabatically. Only the comparison matters.
4. **Applying the dry adiabat to moist ascent.** In a saturated parcel,
   condensation heats the air and the parcel cools at $4\text{–}6\
   \mathrm{K\,km^{-1}}$, not $9.76$. Using $\Gamma_d$ for a cloudy parcel
   overestimates stability.
5. **Forgetting entrainment.** A real updraught mixes with its environment; the
   parcel's $\theta$ is not conserved even if it is adiabatic.
6. **Treating $N^2$ as a constant.** It varies with height; a single $N$ is a
   local or layer-averaged statement.
7. **Comparing $\theta$ values from different reference pressures.** Change $p_0$
   and every $\theta$ changes; only differences are physical.

## Related modules

- [01 Atmospheric Composition and Vertical Structure](01-atmospheric-composition.md) —
  where $c_p$ comes from and why $\Gamma_d$ has its value.
- [02 Hydrostatic Balance and Pressure-Height Relations](02-hydrostatic-balance.md) —
  the pressure–height relation used for the parcel's environment.
- [04 Moisture, Humidity Variables and Cloud Formation](04-moisture-and-clouds.md) —
  the moist adiabat, and why the real lapse rate is smaller than $\Gamma_d$.
- [05 Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind](05-atmospheric-dynamics-basics.md) —
  what happens to a stably stratified atmosphere once it rotates.
- [02-05-02 First Law, Work and Energy Balances](../../02-physics/05-thermodynamics/02-first-law.md) —
  the general thermodynamics behind §3.1.
- [02-06-01 Fluid Statics, Pressure and Buoyancy](../../02-physics/06-fluid-mechanics/01-fluid-statics.md) —
  buoyancy in its general form.
- [16-03 Atmospheric Circulation](../03-atmospheric-circulation/README.md) —
  where $N$ reappears as the restoring force for gravity waves.
