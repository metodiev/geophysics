---
id: 16-02-04
title: "Earth Energy Balance and Global Mean Temperature"
level: advanced
prereqs: ["16-02-03", "16-02-02", "16-01-03"]
tags: [atmosphere, climate, energy-balance, albedo, bowen-ratio, heat-transport, budget]
---

# Earth Energy Balance and Global Mean Temperature

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the global-mean top-of-atmosphere budget, and **explain** why the
   equality of absorbed and emitted radiation is a definition rather than a result.
2. **Explain** how a net imbalance that is a fraction of a per cent of the gross
   fluxes can still be the quantity a changing composition perturbs, and what that
   implies for the observational problem.
3. **Write** the surface energy budget including the non-radiative fluxes, and
   **derive** the two-box relation
   $\sigma T_s^4(2-\varepsilon) = F(1+f_s) - (H+LE)$.
4. **Demonstrate** the degeneracy between atmospheric opacity and non-radiative
   cooling in a surface budget, and **state** what breaks it.
5. **Compute** the required poleward energy transport from a latitude-dependent
   net top-of-atmosphere flux, and **derive** its analytic form for a
   $\sin^2\phi$ profile.
6. **Distinguish** the parts of the transport requirement that follow from geometry
   and equilibrium alone from those that depend on a model of the flux profile.
7. **State** which of the fluxes in a planetary energy budget are measured, which
   are model closures, and which are inferred residuals.

## Prerequisites

- [03 The Greenhouse Effect: Physics, Not Rhetoric](03-greenhouse-effect.md) —
  the effective temperature, the downwelling infrared and the Planck response.
- [02 Radiative Transfer in the Atmosphere](02-radiative-transfer-atmosphere.md) —
  the transfer solutions this lesson assembles into a budget.
- [16-01-03 Adiabatic Processes, Lapse Rates and Stability](../01-atmospheric-structure-and-thermodynamics/03-thermodynamic-processes.md) —
  why the surface cannot simply heat up until it radiates enough.

> **All models and data in this module are SYNTHETIC.** The solar constant and
> $\sigma$ are standard constants. The albedo, the surface temperature, the
> atmospheric emissivity, the solar partition, the Bowen ratio and the zonal flux
> profile are **chosen inputs**, printed by the demonstration. No measured flux,
> satellite product, reanalysis value or published energy budget is used or
> reproduced.

## 1. Intuition: one strong constraint and one large number

Two statements organise the whole of planetary energy balance, and they are easy
to confuse with each other.

**The strong constraint: at equilibrium the top-of-atmosphere budget closes.**
Absorbed sunlight equals emitted longwave radiation, exactly, for the planet as a
whole. With $S = 1361\ \mathrm{W\,m^{-2}}$ and a chosen albedo $a = 0.30$:

$$\frac{S}{4} = 340.25\ \mathrm{W\,m^{-2}}
\;\longrightarrow\;
F = \frac{S(1-a)}{4} = 238.17\ \mathrm{W\,m^{-2}}
\;\longrightarrow\;
T_e = \left(\frac{F}{\sigma}\right)^{1/4} = 254.58\ \mathrm{K}.$$

**The large number: the surface fluxes are far bigger than the net.** The surface
of the model emits $\sigma T_s^4 = 390.11\ \mathrm{W\,m^{-2}}$ at
$T_s = 288\ \mathrm{K}$, a factor $1.638$ more than the planet absorbs, and it
receives back $\sim10^{2}\ \mathrm{W\,m^{-2}}$ of infrared from the sky. The net
at the top of the atmosphere is *zero*, and every individual flux is of order
$10^{2}$–$10^{3}\ \mathrm{W\,m^{-2}}$.

**Why that matters.** A change in composition perturbs the budget by a few
$\mathrm{W\,m^{-2}}$ — a fraction of a per cent of the throughput. The physics is
not the difficulty; the difficulty is that a small difference of large numbers is
an observational problem in calibration and sampling, not in theory. The
demonstration makes the ratio explicit: $1\ \mathrm{W\,m^{-2}}$ is $0.4199\%$ of
the absorbed solar flux and $238$ times smaller than it.

The second thing this lesson does is follow the *geography*. The global mean hides
a large latitudinal structure: the tropics absorb more than they emit and the poles
emit more than they absorb, and the difference must be carried by the atmosphere
and the ocean. For the demonstration's illustrative profile that requirement peaks
at **$3.93\ \mathrm{PW}$** ($3.93\times10^{15}\ \mathrm{W}$) at
$35.3^\circ$ latitude — the largest number in this lesson, and one that follows from
geometry and equilibrium with no composition, no dynamics and no radiative transfer
in it at all.

## 2. Precise definitions

### 2.1 The top-of-atmosphere budget

$$\text{absorbed} = \frac{S(1-a)}{4}, \qquad
\text{emitted} = \mathrm{OLR}, \qquad
N \equiv \text{absorbed} - \mathrm{OLR} .$$

$N$ is the **net top-of-atmosphere flux**. Global mean $N = 0$ at equilibrium; a
nonzero global mean $N$ means the planet is warming or cooling, and the *rate* is
related to $N$ by the heat capacity of the system — which is dominated by the
ocean and is a topic for
[16-04](../04-climate-system-and-feedbacks/README.md), not for this lesson.

### 2.2 The surface budget

$$\underbrace{f_s F}_{\text{absorbed solar}} + \underbrace{D}_{\text{downwelling IR}}
= \underbrace{\sigma T_s^4}_{\text{emitted}} + \underbrace{H + LE}_{\text{non-radiative}} .$$

- $f_s$ — the fraction of the absorbed solar flux that reaches the surface;
  $1-f_s$ is absorbed within the atmosphere.
- $D$ — the downwelling infrared flux at the surface, an **observable**.
- $H$ — the **sensible** heat flux, energy transferred by turbulence between the
  surface and the air.
- $LE$ — the **latent** heat flux, energy carried away as water vapour and released
  elsewhere on condensation ([16-01-04](../01-atmospheric-structure-and-thermodynamics/04-moisture-and-clouds.md)).
- $B \equiv H/LE$ — the **Bowen ratio**, a *diagnostic ratio* of two fluxes, both of
  which are measured; it is not a constant of nature and varies from about $0.1$
  over wet surfaces to above $1$ over dry ones.

### 2.3 Zonal imbalance and transport

Define the zonal net flux $N(\phi)$ at latitude $\phi$. In a steady state the polar
cap north of $\phi$ has zero net energy, so the **northward** energy transport
across the latitude circle at $\phi$ is

$$H(\phi) = -2\pi R_E^2\int_\phi^{\pi/2} N(\phi')\cos\phi'\,\mathrm{d}\phi' .$$

$H$ must vanish at both ends: at the pole because nothing lies beyond it, and at the
equator because in a hemispherically symmetric state the two hemispheres cannot
exchange net energy.

## 3. Derivations

### 3.1 The top-of-atmosphere constraint

Per unit surface area, averaged over the sphere and over time:

$$\text{incident} = \frac{S}{4} = 340.25\ \mathrm{W\,m^{-2}},
\qquad
\text{absorbed} = \frac{S(1-a)}{4} = 238.17\ \mathrm{W\,m^{-2}},$$

$$\text{reflected} = \frac{S a}{4} = 102.08\ \mathrm{W\,m^{-2}},
\qquad
\text{emitted} = F = 238.17\ \mathrm{W\,m^{-2}} \quad\text{(at equilibrium)}.$$

Setting the emitted flux to $\sigma T_e^4$ defines the effective radiating
temperature:

$$T_e = \left(\frac{S(1-a)}{4\sigma}\right)^{1/4} = 254.58\ \mathrm{K}
= -18.57\ \mathrm{^\circ C}.$$

**The logical status of this number.** The equality
absorbed $=$ emitted is the definition of equilibrium. $T_e$ is then *computed*
from a chosen albedo. Neither is an observation, and calling $T_e$ "the temperature
the Earth would have without a greenhouse effect" is a category error: a world with
the greenhouse gases removed but with the present cloud field is a different model,
and a world with no atmosphere has a different albedo again.

### 3.2 The two-box balance, with non-radiative fluxes and partial solar absorption

Extend the one-layer model of [02 §3.3](02-radiative-transfer-atmosphere.md) with
two new ingredients: a fraction $f_a = 1 - f_s$ of the absorbed solar flux is taken
up within the atmosphere, and the surface loses $H + LE$ non-radiatively. Let the
layer have emissivity $\varepsilon$ and temperature $T_a$, and recall that for a
grey slab the upward and downward emissions are equal, $\varepsilon\sigma T_a^4$.

$$\text{TOA:}\qquad
(1-\varepsilon)\sigma T_s^4 + \varepsilon\sigma T_a^4 = F,$$

$$\text{surface:}\qquad
f_s F + \varepsilon\sigma T_a^4 = \sigma T_s^4 + (H + LE),$$

$$\text{layer:}\qquad
f_a F + \varepsilon\sigma T_s^4 + (H + LE) = 2\varepsilon\sigma T_a^4 .$$

Use the TOA equation to eliminate $\varepsilon\sigma T_a^4 = F - (1-\varepsilon)
\sigma T_s^4$:

$$\text{surface:}\quad f_s F + F - (1-\varepsilon)\sigma T_s^4
= \sigma T_s^4 + (H+LE)
\;\Longrightarrow\;
F(1+f_s) - (H+LE) = \sigma T_s^4(2-\varepsilon).$$

$$\boxed{\;\sigma T_s^4 = \frac{F(1+f_s) - (H+LE)}{2-\varepsilon}\;}$$

Two checks:

- With $f_s = 1$ and $H + LE = 0$ this reduces to $\sigma T_s^4 = 2F/(2-\varepsilon)$,
  the lesson-02 result. ✔
- Substituting the same elimination into the layer equation and using
  $f_s + f_a = 1$ gives $2 - f_a = 1 + f_s$, which is the same statement: **the
  three equations are consistent for any $\varepsilon$**, so the solar partition
  does not constrain the pressure level and the balance is genuinely
  two-parameter degenerate in $\varepsilon$ and $(H+LE)$.

### 3.3 The opacity/non-radiative degeneracy

Solve the boxed relation for the non-radiative flux required to hold a prescribed
surface temperature:

$$H + LE = F(1+f_s) - \sigma T_s^4(2-\varepsilon).$$

With $F = 238.17\ \mathrm{W\,m^{-2}}$, $f_s = 1$, $T_s = 288\ \mathrm{K}$
($\sigma T_s^4 = 390.11\ \mathrm{W\,m^{-2}}$):

| $\varepsilon$ | radiative-only $T_s$ (K) | required $H+LE$ for $288\ \mathrm{K}$ (W m⁻²) |
|---|---|---|
| 0.50 | 273.562 | $-108.81$ |
| 0.70 | 283.526 | $-30.79$ |
| 0.7789 | 287.999 | $-0.01$ |
| 0.90 | 295.618 | $+47.23$ |
| 1.00 | 302.746 | $+86.24$ |

**Read the sign.**

- **Positive $H+LE$**: the radiative-only model is too *warm* and the surface must
  export the excess non-radiatively. At $\varepsilon = 1$ the radiative model gives
  $302.75\ \mathrm{K}$, i.e. $14.7\ \mathrm{K}$ too warm, and the surface must
  export $86.24\ \mathrm{W\,m^{-2}}$.
- **Negative $H+LE$**: the model is too *cold*, and the surface would need to be
  *heated* non-radiatively. Convection and evaporation at a planetary surface cool,
  they do not heat, so a negative requirement means the model is inconsistent with a
  $288\ \mathrm{K}$ surface. Opacities below about $0.78$ fail this test in this
  two-box model.
- **Zero**: at $\varepsilon = 0.7789$ the purely radiative model happens to
  reproduce the surface temperature. That is exactly the value fitted in
  [03 §3.2](03-greenhouse-effect.md) — so **the fit is equivalent to assuming that
  convection and evaporation do not exist.**

**The degeneracy, stated plainly.** $(\varepsilon = 0.779,\ H+LE = 0)$ and
$(\varepsilon = 1.0,\ H+LE = 86.24\ \mathrm{W\,m^{-2}})$ give the *same* surface
temperature. A surface energy budget alone cannot determine either. What breaks the
degeneracy is the **vertical structure**: the radiative-convective models of
[05](05-energy-balance-models.md) impose a lapse rate and a convective adjustment
and thereby tie $\varepsilon$ to a temperature profile, which fixes both.

### 3.4 The required poleward transport

Take a model net flux profile whose area-weighted mean is zero (required, or the
planet is not in equilibrium):

$$N(\phi) = 40 - 120\sin^2\phi \quad \mathrm{W\,m^{-2}},$$

which is $+40\ \mathrm{W\,m^{-2}}$ at the equator, zero at
$\sin^2\phi = 1/3$, and $-80\ \mathrm{W\,m^{-2}}$ at the pole. (The demonstration
records a first attempt, $N = 60 - 120\sin^2\phi$, whose mean is
$+40\ \mathrm{W\,m^{-2}}$ — a globally unbalanced planet. That error is instructive
enough to be printed.)

The northward transport across latitude $\phi$ is

$$H(\phi) = -2\pi R_E^2\int_\phi^{\pi/2}N(\phi')\cos\phi'\,\mathrm{d}\phi' .$$

With $u = \sin\phi'$, $\cos\phi'\,\mathrm{d}\phi' = \mathrm{d}u$, and
$\int_u^1(40 - 120u'^2)\,\mathrm{d}u' = -40u + 40u^3$, so

$$\boxed{\;H(\phi) = 80\pi R_E^2\,\sin\phi\left(1 - \sin^2\phi\right)\;}$$

The extremum follows from $\mathrm{d}/\mathrm{d}s\,[s(1-s^2)] = 1-3s^2 = 0$, i.e.
$\sin^2\phi = 1/3$, $\phi = 35.26^\circ$:

$$H_{\max} = 80\pi R_E^2\cdot\frac{2}{3\sqrt{3}}
= 80\pi(6.371\times10^{6})^2\times0.38490 = 3.93\times10^{15}\ \mathrm{W}
= 3.93\ \mathrm{PW}.$$

| $\phi$ | $N$ (W m⁻²) | $H$ (PW, northward) |
|---|---|---|
| 0° | $+40.00$ | 0.0000 |
| 15° | $+31.96$ | 2.4634 |
| 30° | $+10.00$ | 3.8255 |
| 35.26° | $+0.01$ | 3.9265 |
| 45° | $-20.00$ | 3.6067 |
| 60° | $-50.00$ | 2.2086 |
| 75° | $-71.96$ | 0.6601 |
| 90° | $-80.00$ | 0.0000 |

### 3.5 What is robust here and what is not

**Robust (geometry and equilibrium only).** The transport must vanish at the
equator in a hemispherically symmetric state and at the pole; it must be positive
(northward) in the northern hemisphere; it must have one maximum per hemisphere;
and its magnitude is set by the *area integral* of the imbalance, hence by the
latitude range over which the tropics are in surplus. None of this depends on
composition, on dynamics, or on radiative transfer.

**Not robust (model-dependent).** The *value* $3.93\ \mathrm{PW}$ depends entirely
on the chosen profile $N(\phi) = 40 - 120\sin^2\phi$. Change the coefficients and
the number changes in proportion. **So $3.93\ \mathrm{PW}$ is a model output**, and
the measurement that would test it is a satellite-derived map of the net
top-of-atmosphere flux. What the calculation demonstrates is the *structure* of the
requirement and the fact that it is large — not the number.

## 4. Physical interpretation

- **The atmosphere is not a passive filter; it is an engine.** It absorbs
  $86\ \mathrm{W\,m^{-2}}$ from the surface non-radiatively in the opaque model and
  delivers it back radiatively, which is the mechanism by which the surface
  temperature and the emission level are tied together.
- **The surface loses energy non-radiatively, always.** Evaporation and turbulent
  exchange cool the surface, never warm it. Any budget that requires a negative
  $H+LE$ is wrong somewhere, and that is a useful diagnostic.
- **The degeneracy is the reason energy-balance models need extra physics.** A
  surface budget with one radiative and one non-radiative unknown is
  underdetermined; the models of [05](05-energy-balance-models.md) close it with a
  lapse rate.
- **Energy transport is required, not optional.** A planet with a latitudinal
  imbalance and no transport would heat at the equator and freeze at the poles
  without limit. The transport requirement is the boundary condition that the
  circulation of [16-03](../03-atmospheric-circulation/README.md) must satisfy, and
  it is one of the few statements in climate science that is almost purely
  geometrical.
- **The small net is a measurement problem, not a physics problem.** A few
  $\mathrm{W\,m^{-2}}$ is $<1\%$ of the throughput; measuring it requires
  absolute calibration of radiometers to better than that, plus sampling that
  represents the whole globe and the whole diurnal and seasonal cycle. That is the
  subject of [16-08](../08-climate-observation-and-data/README.md).
- **Nothing here says how a change happens.** The budget constrains the
  *equilibrium*, not the pathway. The thermal inertia of the ocean means the actual
  state lags, and the *rate* of change introduces the heat capacity that this
  lesson has deliberately left out.

## 5. Worked numerical examples

**Example 1 — the budget, closed.**

| term | value (W m⁻²) | status |
|---|---|---|
| incident solar $S/4$ | 340.25 | standard constant $S$, geometric factor |
| reflected (albedo $0.30$) | 102.08 | albedo is a chosen input here |
| absorbed $F$ | 238.17 | computed |
| emitted longwave | 238.17 | constraint of equilibrium |
| net | 0.00 | by construction |

$$T_e = (238.17/5.670374419\times10^{-8})^{1/4} = 254.58\ \mathrm{K}
= -18.57\ \mathrm{^\circ C}.$$

**Example 2 — the surface budget at $288\ \mathrm{K}$ with an opaque layer.**

At $\varepsilon = 1$ the layer emits $\sigma T_a^4$ both ways, and the TOA
constraint forces $\sigma T_a^4 = F = 238.17\ \mathrm{W\,m^{-2}}$ (all the surface
emission is absorbed, and the layer must emit exactly what the planet absorbs).
With $f_s = 1$:

| term | value (W m⁻²) |
|---|---|
| absorbed solar at surface | $+238.17$ |
| downwelling infrared $D = \varepsilon\sigma T_a^4$ | $+238.17$ |
| emitted $\sigma T_s^4$ | $-390.11$ |
| non-radiative $H + LE$ | $-86.24$ |
| net | $0.00$ |

Partitioning with a Bowen ratio $B = 0.25$:

$$LE = \frac{H+LE}{1+B} = \frac{86.24}{1.25} = 68.99\ \mathrm{W\,m^{-2}},
\qquad H = 0.25 \times 68.99 = 17.25\ \mathrm{W\,m^{-2}},$$

and $H + LE = 86.24\ \mathrm{W\,m^{-2}}$ ✔. **The surface must export
$86\ \mathrm{W\,m^{-2}}$ by convection and evaporation** — that is the sense in
which the atmosphere is this model's cooling system, and it is also the reason the
same surface temperature can be obtained with a lower opacity and no
non-radiative cooling at all (§3.3).

**Example 3 — the transport requirement.**

From §3.4, at $\phi = 35.26^\circ$:

$$H_{\max} = 80\pi R_E^2 \times \frac{2}{3\sqrt3}
= 80\pi \times 4.05896\times10^{13} \times 0.38490
= 1.02023\times10^{16}\times 0.38490 = 3.927\times10^{15}\ \mathrm{W}
= 3.93\ \mathrm{PW}.$$

For scale, that is $3.93\times10^{15}\ \mathrm{W}$ — a *rate* of energy transport
of nearly four thousand trillion watts, sustained continuously by the atmosphere
and the ocean. Two things about the number are worth separating: the *structure*
(zero at both ends, one maximum per hemisphere, of order several PW) follows from
the geometry, and the *magnitude* $3.93$ depends on the assumed shape of $N(\phi)$.
The alternative to transporting it is a planet that does not reach equilibrium.

## 6. Assumptions and regime of validity

| Assumption | Where used | What breaks it |
|---|---|---|
| Global annual mean | §3.1 | Instantaneous and regional budgets differ by a factor of two or more; the mean is only a mean |
| Equilibrium | the equality absorbed $=$ emitted | The real system has a nonzero net (that is what "warming" means), so the equality holds only as an idealisation or as a statement about the long-term mean |
| Single grey layer | §§3.2–3.3 | The measured sensitivity and spectrum error is a factor of about $2.4$ ([02 §3.7](02-radiative-transfer-atmosphere.md)) |
| Constant Bowen ratio | §3.2 | $B$ varies with surface moisture, wind and stability, from $\sim0.1$ over wet surfaces to $>1$ over dry ones |
| Albedo constant | §3.1 | Reflectivity depends on cloud, ice and surface, and responds to temperature; that response is a feedback ([16-04-02](../04-climate-system-and-feedbacks/02-climate-feedbacks.md)) |
| No heat capacity | everywhere | The ocean's heat capacity delays the response; a nonzero net $N$ is exactly what charges it |
| Radiative-only closure of the surface budget (§3.3) | the degeneracy | Requires a lapse rate to break; supplied by the radiative–convective models of [05](05-energy-balance-models.md) |
| $\sin^2\phi$ form for $N(\phi)$ | §3.4 | Chosen; the magnitude of $H_{\max}$ scales with it, though its structure does not |

**Climate-claim discipline.** The fluxes in this lesson fall into three classes,
and the classes must not be mixed:

1. **Measured in reality**: the downwelling infrared at a surface, the reflected
   shortwave, the outgoing longwave (spectrally and broadband), surface and air
   temperatures, the sensible and latent fluxes (by eddy covariance). Each has a
   stated calibration and sampling uncertainty, and none is reproduced here.
2. **Closed by construction** in a model: the residual of a budget. If you specify
   all fluxes but one, the last is determined; *being determined is not being
   measured*, and this is the commonest way a budget diagram misleads.
3. **Inferred**: the balance itself, and every "required" quantity such as the
   $3.93\ \mathrm{PW}$ transport, which is a consequence of an assumed flux
   profile.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| Flux density | $F$, $D$, $H$, $LE$, $N$ | $\mathrm{W\,m^{-2}}$ | |
| Albedo, $f_s$ | | dimensionless | $[0,1]$ |
| Bowen ratio | $B = H/LE$ | dimensionless | ratio of two fluxes |
| Emissivity | $\varepsilon$ | dimensionless | $[0,1]$ |
| Temperature | $T_e, T_s, T_a$ | K | |
| Transport | $H(\phi)$ in PW | W | $(\mathrm{W\,m^{-2}})\times\mathrm{m^2}$ ✔ |
| Area element | $2\pi R_E^2\cos\phi\,\mathrm{d}\phi$ | $\mathrm{m^2}$ | distinguishes *zonal* from *total* by the factor $2\pi$ |

Two checks that catch most errors: a *zonal* mean flux times the Earth's surface
area overestimates a *global* mean by a factor of order 2 if the area weighting is
omitted (the poles have less area), and any expression for a transport must come out
in watts, not in $\mathrm{W\,m^{-2}}$.

## 8. Python demonstration

[`code/earth_energy_balance_demo.py`](code/earth_energy_balance_demo.py) prints
every number quoted above. It:

1. closes the global-mean top-of-atmosphere budget and computes $T_e$;
2. contrasts the net (zero) with the gross fluxes and quantifies the ratio
   ($1\ \mathrm{W\,m^{-2}}$ is $0.4199\%$ of $F$);
3. assembles the surface budget for the opaque-layer case and partitions $H+LE$
   with a chosen Bowen ratio;
4. tabulates the required non-radiative flux against opacity, showing the
   degeneracy and the sign diagnostic, and identifies $\varepsilon = 0.7789$ as the
   value at which the radiative-only model needs no non-radiative flux;
5. tabulates the zonal imbalance and the required northward transport, and derives
   the peak analytically at $\phi = 35.26^\circ$ ($3.93\ \mathrm{PW}$);
6. records, in its own output, the earlier attempt with a globally unbalanced
   $N(\phi)$ and why it was wrong.

```bash
cd 16-atmosphere-climate/02-radiation-and-energy-balance/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python earth_energy_balance_demo.py
```

## 9. Exercises

Graded problems with worked solutions:
[`exercises/04-earth-energy-balance-exercises.md`](exercises/04-earth-energy-balance-exercises.md)
and
[`exercises/04-earth-energy-balance-solutions.md`](exercises/04-earth-energy-balance-solutions.md).

## Mastery checkpoint

Without notes:

> A planet has $S = 900\ \mathrm{W\,m^{-2}}$, albedo $0.35$, surface temperature
> $300\ \mathrm{K}$, solar partition $f_s = 0.75$ and Bowen ratio $0.4$.
> **(a)** Compute the top-of-atmosphere budget and $T_e$. **(b)** Compute the
> surface budget, taking the layer emissivity as $\varepsilon = 0.9$ and treating
> the layer's downward emission as equal to its upward emission. **(c)** Derive the
> required non-radiative flux from the boxed relation and check it against your
> (b) budget. **(d)** Partition it into $H$ and $LE$. **(e)** Find the emissivity at
> which the required non-radiative flux would be zero, and state in one sentence
> what that value means. **(f)** State which of your quantities are measurements,
> which are model closures, and which are inferred.

## Common pitfalls

1. **Treating "absorbed $=$ emitted" as a result.** It is the definition of
   equilibrium, and it holds whatever the composition is.
2. **Calling $T_e$ "the temperature without the greenhouse effect".** It is the
   effective radiating temperature for a chosen albedo; the counterfactual must be
   specified.
3. **Confusing the global mean with a local one.** $S/4 = 340\ \mathrm{W\,m^{-2}}$
   is a global mean; no location receives that flux on any given day.
4. **Assuming the surface is in radiative balance with space.** It is not: it
   radiates $390\ \mathrm{W\,m^{-2}}$ while the planet absorbs $238\ \mathrm{W\,m^{-2}}$.
5. **Allowing the budget to require a negative $H+LE$.** Convection and evaporation
   cool the surface; a negative requirement means the model is wrong.
6. **Believing a budget diagram's residuals are measured.** A residual is what is
   left over; it is closed by construction.
7. **Treating the poleward transport as optional or dynamic.** It is required by
   the zonal imbalance; the *mechanism* is dynamic, the *requirement* is geometry.
8. **Forgetting the area weighting in a zonal average.** A simple mean over latitude
   bands over-weights the poles.
9. **Using a chosen profile's number as a measured one.** The $3.93\ \mathrm{PW}$
   here is a model output that scales with the assumed shape of $N(\phi)$.

## Related modules

- [03 The Greenhouse Effect: Physics, Not Rhetoric](03-greenhouse-effect.md) —
  the downwelling infrared and the one-layer fit that §3.3 generalises.
- [02 Radiative Transfer in the Atmosphere](02-radiative-transfer-atmosphere.md) —
  where the downwelling flux actually comes from.
- [05 Zero- and One-Dimensional Energy Balance Models](05-energy-balance-models.md) —
  the lapse rate that breaks the degeneracy of §3.3.
- [06 Aerosols, Clouds and Their Radiative Effects](06-aerosols-and-clouds-radiation.md) —
  the albedo is not a constant.
- [01 Solar and Terrestrial Radiation, Blackbody Laws](01-solar-and-terrestrial-radiation.md) —
  the factor four and the insolation-versus-latitude formula used in §3.4.
- [16-01-04 Moisture, Humidity Variables and Cloud Formation](../01-atmospheric-structure-and-thermodynamics/04-moisture-and-clouds.md) —
  the latent heat flux $LE$.
- [16-03-01 Global Circulation: Hadley, Ferrel, Polar Cells, Jets](../03-atmospheric-circulation/01-global-circulation.md) —
  the machinery that actually performs the $3.93\ \mathrm{PW}$ of transport.
- [16-08-01 Surface, Radiosonde and Satellite Climate Records](../08-climate-observation-and-data/01-surface-and-satellite-records.md) —
  how the measured fluxes in this budget are actually obtained.
