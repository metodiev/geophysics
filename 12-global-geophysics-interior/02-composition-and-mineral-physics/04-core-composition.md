---
id: 12-02-04
title: "Core Composition, Light Elements and the Geodynamo"
level: research
prereqs: ["12-01-06", "12-01-05", "12-02-01", "12-02-02", "04-01-01"]
tags: [global-geophysics, earth-interior, core-composition, light-elements, inner-core-age, geodynamo, core-thermal-evolution]
---

# Core Composition, Light Elements and the Geodynamo

> **All models and data in this module are SYNTHETIC.** The density profile of the
> Earth, the pure-iron equation of state, the thermal parameters, the heat flow and
> the light-element densities used here are chosen teaching values, picked to lie in
> the range normally discussed for the core. They are not measurements and no
> published model or equation of state is reproduced. The only numbers that are not
> assumptions are exact standard constants (the gravitational constant, the Earth's
> mass and radius) and named layer-depth conventions.

## Learning objectives

By the end of this lesson you will be able to:

1. **Integrate** the hydrostatic equation for a given core density model to obtain
   the pressure at the core–mantle boundary and at the inner-core boundary, and
   **check** the model against the Earth's total mass.
2. **Compare** a seismological density with a pure-iron equation of state at the
   same pressure *and temperature*, and **compute** the resulting density deficit.
3. **Convert** a density deficit into a light-element mass fraction under an explicit
   mixing assumption, and **state** why the conversion is strongly model-dependent
   and non-unique.
4. **Derive** the adiabatic temperature gradient from the thermodynamic relation
   $dT/dP = \alpha T/(\rho C_p)$ and **evaluate** the temperature rise across the
   outer core.
5. **Compute** the heat conducted down the adiabat, **compare** it with the heat
   leaving the core, and **explain** the "new core paradox" that follows when the
   two are close.
6. **Estimate** the age of the inner core from a cooling rate, a melting-curve slope
   and the latent heat of freezing, and **explain** how the seismological ICB density
   jump constrains the composition of the inner core.
7. **Justify** the existence of the geodynamo from the magnetic Reynolds number and
   **explain** the role of light elements as the compositional buoyancy source.

## Prerequisites

- [12-01-06 Outer Core, Inner Core Anisotropy and Rotation](../01-seismic-structure-of-the-earth/06-outer-and-inner-core.md) —
  the seismological observations this lesson tries to explain.
- [12-01-05 Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite](../01-seismic-structure-of-the-earth/05-core-mantle-boundary.md) —
  the boundary through which the core loses its heat.
- [12-01-01 PREM, IASP91 and Reference Earth Models](../01-seismic-structure-of-the-earth/01-prem-and-reference-models.md) —
  where the density profile comes from and why it is non-unique.
- [12-02-01 Mantle Composition and Peridotite Models](01-mantle-composition.md) —
  the same deficit argument applied to the mantle.
- [12-02-02 High-Pressure Experiments and Diamond Anvil Cells](02-high-pressure-experiments.md) —
  how a pure-iron equation of state is measured at core pressures.
- [04-01-01 Crust, Mantle, Core: Seismological and Geochemical Evidence](../../04-earth-science-geology/01-earth-structure/01-layered-earth.md) —
  the lower-level version of the same story.

## 1. What seismology gives the core, and what it cannot

A reference Earth model is built from travel times, free oscillations and the mass
and moment of inertia. It returns radial functions $v_p(r)$, $v_s(r)$, $\rho(r)$ and
the derived $P(r)$ and $g(r)$. In the outer core it says one thing very clearly:
**$v_s = 0$** — no shear waves propagate, which forces a liquid of low viscosity and
high density, i.e. an iron-rich alloy.

Everything beyond that is inference: the model cannot see composition directly, it
sees density, and density is a product of composition, temperature, pressure and
phase. This lesson follows the standard chain of inferences — *density deficit →
light elements → core temperature → inner-core age → dynamo* — and flags at each step
where a different assumption gives a different answer.

The construction used throughout is the **reference-state method**. Rather than
asking "what is the core made of?", ask the operational question:

> At the *same pressure and temperature*, how much lighter is the core than pure
> iron?

The answer is a number with units (a density deficit in per cent), not a composition.
Converting it into a composition needs a second, independent piece of information —
an assumed light-element density, an assumed partitioning, or an assumed temperature —
which is why core composition is one of the most persistently debated problems in the
subject. All numbers below are printed by
[`code/core_composition_demo.py`](code/core_composition_demo.py).

## 2. Mass, gravity and pressure in the core

### 2.1 Hydrostatic equilibrium

For a spherically symmetric body the momentum equation reduces to hydrostatic
balance,

$$\frac{dP}{dr} = -\rho(r)\,g(r),\qquad g(r) = \frac{G\,M(r)}{r^{2}},\qquad
M(r) = \int_0^{r} 4\pi x^{2}\rho(x)\,dx .$$

Given a density profile, gravity is a cumulative integral and pressure is an integral
from the surface inward:

$$P(r) = \int_r^{R} \rho(x)\,g(x)\,dx .$$

This is the only route to $P(r)$ in the core; no seismological observable returns
pressure directly. Two consequences matter: **pressure at the CMB is set by the
mantle alone** (the mass above it and the gravity it produces), and **a mass check is
mandatory** — a model that misses the Earth's total mass by several per cent will miss
every pressure by several per cent too.

### 2.2 What the synthetic model gives

The demonstration builds a three-shell mantle (crust, upper mantle, lower mantle),
a smooth outer-core profile from 9.90 g cm$^{-3}$ at the CMB to
12.15 g cm$^{-3}$ at the ICB, and an inner core from 12.75 to
13.50 g cm$^{-3}$, then integrates:

| quantity | value |
|---|---|
| total model mass | $5.9143\times10^{24}$ kg (standard Earth mass $5.9722\times10^{24}$ kg, i.e. $-1.0$ %) |
| core mass | $1.9161\times10^{24}$ kg (outer core $1.8164\times10^{24}$ kg, inner core $0.0996\times10^{24}$ kg) |
| gravity at the CMB | 10.559 m s$^{-2}$ |
| gravity at the ICB | 4.456 m s$^{-2}$ |
| pressure at the CMB | 126.2 GPa |
| pressure at the ICB | 315.0 GPa |
| pressure at the centre | 351.4 GPa |

The $-1$ % mass error is the honest measure of a three-shell mantle, and it is also
roughly how wrong $P_\text{CMB}$ would be if the mantle mass were worse, since
$P_\text{CMB}$ is proportional to the weight of the mantle. Gravity *falls* from the
CMB to the ICB (10.559 to 4.456 m s$^{-2}$) because most of the core's mass lies in
its outer part — the fact that controls the shape of every gradient below.

## 3. The pure-iron reference state

### 3.1 The equation of state

The third-order Birch–Murnaghan equation of state is the workhorse of mineral
physics. With $x = (\rho/\rho_0)^{1/3}$,

$$P(\rho) = \frac{3}{2}K_0\left(x^{7}-x^{5}\right)
\left[1 + \frac{3}{4}\left(K_0'-4\right)\left(x^{2}-1\right)\right],$$

where $\rho_0$ is the zero-pressure density, $K_0$ the zero-pressure bulk modulus
and $K_0'$ its pressure derivative. It is derived by expanding the Helmholtz energy
to third order in the Eulerian finite strain — which is exactly the kind of energy
expansion the tensor work of [12-02-03](03-ab-initio-mineral-physics.md) uses for
elastic constants.

The demonstration inverts the EOS numerically (bisection on $\rho$) and reports, for
the assumed reference state $\rho_0 = 8.00$ g cm$^{-3}$, $K_0 = 160$ GPa,
$K_0' = 5.0$:

$$\rho_\text{Fe}(126\ \mathrm{GPa}, 300\ \mathrm{K}) = 11.209\ \mathrm{g\,cm^{-3}},\qquad
\rho_\text{Fe}(315\ \mathrm{GPa}, 300\ \mathrm{K}) = 13.504\ \mathrm{g\,cm^{-3}}.$$

### 3.2 The temperature correction, and why it cannot be skipped

At 300 K these densities are irrelevant to the real core, which is at 4000–5000 K.
A linear thermal correction is the minimum honest treatment:

$$\rho(P,T) \simeq \rho(P,300\ \mathrm{K})\left[1 - \alpha\left(T - 300\ \mathrm{K}\right)\right],
\qquad \alpha = 1.0\times10^{-5}\ \mathrm{K^{-1}},$$

which for the model's adiabat (section 4, $T_\text{ICB} = 4963$ K) gives

$$\rho_\text{Fe}^\text{CMB} = 10.794\ \mathrm{g\,cm^{-3}},\qquad
\rho_\text{Fe}^\text{ICB} = 12.874\ \mathrm{g\,cm^{-3}}.$$

The thermal correction is worth about 3.7 % at the CMB and 4.9 % at the ICB — larger
than most of the effects being discussed, so **the temperature is part of the
equation of state, not a refinement of it**: a hotter core is lighter, and a cooler
core needs fewer light elements to explain the same density.

### 3.3 Melting, and the solid-iron reference

The inner core is solid, so its reference is the *solid* EOS. Freezing a liquid
generally increases its density by a few per cent at constant pressure and
temperature; with an assumed melting jump of 3 %,

$$\rho_\text{Fe,solid}^\text{ICB} = 1.03 \times 12.874 = 13.260\ \mathrm{g\,cm^{-3}}.$$

## 4. The density deficit and the light-element content

### 4.1 The deficit

Comparing the seismological density with the pure-iron reference at equal $P$ and
$T$ defines the **density deficit**

$$\Delta(r) = 1 - \frac{\rho_\text{model}(r)}{\rho_\text{Fe}(r)} .$$

| level | model density (g cm$^{-3}$) | pure iron (g cm$^{-3}$) | deficit |
|---|---|---|---|
| outer core, CMB | 9.900 | 10.794 | 8.3 % |
| outer core, ICB | 12.150 | 12.874 | 5.6 % |
| inner core, ICB | 12.750 | 13.260 (solid) | 3.8 % |

Two features of this table are the substance of the whole problem:

* the deficit is **large** (5–8 %), so a light alloying component is unavoidable;
* the deficit **decreases inward**, from 8.3 % to 5.6 %, which a fixed-composition
  core with a smooth EOS would not predict.

### 4.2 From deficit to mass fraction

Under **ideal volume additivity** — the light element occupies its own volume as if
it were a separate phase, with no interaction with the iron — the specific volumes
add in proportion to mass fraction $x$:

$$\frac{1}{\rho_\text{mix}} = \frac{1-x}{\rho_\text{Fe}} + \frac{x}{\rho_\text{L}}
\quad\Longrightarrow\quad
x = \frac{1/\rho_\text{mix} - 1/\rho_\text{Fe}}{1/\rho_\text{L} - 1/\rho_\text{Fe}} .$$

With assumed light-element densities of 5.0 g cm$^{-3}$ (CMB) and 6.0 g cm$^{-3}$
(ICB), the model gives

$$x_\text{CMB} = 7.8\ \text{mass}\,\%,\qquad x_\text{ICB} = 5.2\ \text{mass}\,\%,\qquad
x_\text{inner core} = 3.3\ \text{mass}\,\% .$$

The extreme sensitivity to the light-element density is immediate from the formula —
it appears in the denominator as a *contrast*:

| assumed $\rho_\text{L}$ at the CMB | implied $x$ |
|---|---|
| 3.5 g cm$^{-3}$ | 4.3 mass % |
| 5.0 g cm$^{-3}$ | 7.8 mass % |
| 6.5 g cm$^{-3}$ | 13.7 mass % |

The same deficit is compatible with 4 % or 14 % light elements, purely through the
choice of $\rho_\text{L}$. This is the first great **non-uniqueness** of the problem,
and it is why seismology alone can never give a core composition.

### 4.3 The deficit profile is itself a constraint

Suppose the light-element fraction is uniform at the value found at the CMB
(7.8 mass %). Applying the same mixing relation at the ICB pressure gives

$$\rho_\text{predicted}^\text{ICB} = 11.819\ \mathrm{g\,cm^{-3}},$$

whereas the model density there is 12.150 g cm$^{-3}$ — the prediction is 2.8 % too
light. Either the light-element content increases upward (a stratified outer core),
or the assumed EOS, temperature or light-element density is wrong by that much.
**The shape of the deficit, not just its size, is the observable.**

### 4.4 Which light elements?

Nothing so far distinguishes candidates. Independent constraints that do:

1. **Cosmochemical abundance.** The core formed by segregation of metal from a
   chondritic reservoir, so the candidates come from the abundant, moderately
   volatile elements that enter metal: O, S, Si, C and H. That fixes the inventory,
   not the amount.
2. **Sound velocity as well as density.** The pairing of $v_p$ with $\rho$ — through
   Birch's law and the ratio $\xi = \partial \ln v_s / \partial \ln \rho$ —
   distinguishes the *type* of light element, because O, S and Si change $v_p$ at
   constant density differently. This is the reasoning chain that
   [12-02-03](03-ab-initio-mineral-physics.md) and
   [12-02-02](02-high-pressure-experiments.md) feed.
3. **Partitioning at the ICB.** Freezing rejects some light elements and incorporates
   others. The model's ICB jump of 0.60 g cm$^{-3}$ splits into 0.39 g cm$^{-3}$ from
   melting at constant composition and 0.21 g cm$^{-3}$ left over for a compositional
   change — making the jump a *partition-coefficient* observable, and direct evidence
   that the inner core is more iron-rich than the outer core.
4. **The dynamo needs buoyancy** (section 7): light elements are a power source, not
   a passive passenger.

## 5. The thermal state: adiabat, gradient and conducted heat

### 5.1 The adiabatic gradient

A convecting core is close to adiabatic. Starting from the thermodynamic identity
for an isentrope, $dT/dP = \alpha T/(\rho C_p)$, and combining it with
$dP/dr = -\rho g$,

$$\boxed{\ \frac{dT}{dr} = -\frac{\alpha\,g\,T}{C_p}\ }$$

so the temperature **increases inward** in proportion to gravity times temperature,
divided by the heat capacity. At the CMB the model gives
$\alpha g T / C_p = 0.528$ K km$^{-1}$; at the ICB, where $g$ has fallen from 10.56
to 4.46 m s$^{-2}$, it is only 0.276 K km$^{-1}$. The gradient *weakens* with depth
even though the temperature is higher, because $g$ falls faster than $T$ rises.
Integrating the gradient across the outer core gives

$$T_\text{CMB} = 4000\ \mathrm{K} \ \rightarrow\ T_\text{ICB} = 4963\ \mathrm{K},
\qquad \Delta T_\text{ad} = 963\ \mathrm{K}\ \text{over}\ 2258\ \mathrm{km}.$$

That 963 K is a *requirement* of a convective, adiabatic core, not a measurement.

### 5.2 The conducted heat flow and the "new core paradox"

Heat conducted down the adiabat leaves the core as surely as heat carried by
convection. The core-side flux at the CMB is

$$Q_\text{ad} = 4\pi R_c^{2}\,k\,\left|\frac{dT}{dr}\right|_\text{CMB},$$

with core-side area $4\pi R_c^2 = 1.522\times10^{14}$ m$^{2}$ and $k$ the thermal
conductivity of the core alloy. For the model:

| $k$ (W m$^{-1}$ K$^{-1}$) | $Q_\text{ad}$ (TW) | vs assumed 10 TW CMB heat flow |
|---|---|---|
| 30 | 2.41 | conduction leaves 7.59 TW for everything else |
| 60 | 4.82 | 5.18 TW left |
| 90 | 7.23 | 2.77 TW left |
| 120 | 9.64 | 0.36 TW left |
| 150 | 12.05 | **nothing left** |

Setting $Q_\text{ad} = Q_\text{CMB}$ defines a threshold conductivity,

$$k^{*} = \frac{Q_\text{CMB}}{4\pi R_c^{2}\,\left|dT/dr\right|_\text{CMB}}
= 124\ \mathrm{W\,m^{-1}K^{-1}} .$$

Above $k^{*}$, conduction down the adiabat alone removes more heat than the mantle
lets through, and there is no energy left to cool the core or to grow the inner core.
Because modern estimates of the core's conductivity have moved upward over the years,
this tension — conduction eating the dynamo's lunch — is known as the **new core
paradox**. Note carefully what the paradox is *and is not*: it is a statement about a
budget of assumed numbers. It is dissolved by a lower conductivity, a higher CMB heat
flow, or by a significant additional heat source in the core, and it cannot be
settled by seismic data alone.

## 6. Cooling, inner-core growth and the age of the inner core

### 6.1 Why there is a liquid outer core at all

Both the adiabat and the melting curve rise inward, at rates $A = |dT/dr|_\text{ad}$
and $M = |dT_m/dr|$. Let $s$ measure depth below the CMB. The core is liquid where
the adiabat lies *above* the melting curve. With a difference in slopes
$D = A - M > 0$, the adiabat crosses the melting curve exactly once, at

$$s^{*} = \frac{T_\text{ad}(\text{CMB}) - T_m(\text{CMB})}{D},$$

and everything deeper than $s^{*}$ is solid. This is the whole reason the Earth has a
liquid outer core around a solid inner core; if $M > A$ the core would freeze from the
top downward and be entirely solid, so **the observed structure constrains the slope
of the melting curve.**

With the model's $A = 0.276$ K km$^{-1}$ at the ICB and an assumed
$M = 0.15$ K km$^{-1}$, $D = 0.126$ K km$^{-1}$; matching the present ICB depth
(2258 km) fixes the CMB-side offset, and the inner core nucleated when
$s^{*}$ had grown from the centre outward — i.e. when the core had cooled by
$D \times R_\text{ICB} = 0.126 \times 1221.5\ \mathrm{km} = 154\ \mathrm{K}$.

### 6.2 The energy budget and the cooling rate

For the whole core, with the adiabatic conduction removed first,

$$Q_\text{CMB} - Q_\text{ad} = M_\text{core}C_p\,\Gamma + L\,\frac{dm_i}{dt},$$

where $\Gamma$ is the cooling rate of the core adiabat and the second term is the
latent heat released by the mass freezing per second. Because the geometry ties the
ICB radius to the temperature ($dr_i/dt = \Gamma/D$),

$$\Gamma = \frac{Q_\text{CMB} - Q_\text{ad}}
{M_\text{core}C_p + L\,\rho_\text{ICB}\,4\pi R_\text{ICB}^{2}/D }
\ ,\qquad
\text{age} = \frac{D\,R_\text{ICB}}{\Gamma}.$$

The model's core heat capacity is $M_\text{core}C_p = 1.533\times10^{27}$ J K$^{-1}$,
and with $L = 2.5\times10^{5}$ J kg$^{-1}$ the latent term adds 31 % to the heat that
must be removed per kelvin of cooling, lengthening the required time by the same
factor. The results, at $Q_\text{CMB} = 10$ TW:

| $k$ (W m$^{-1}$ K$^{-1}$) | cooling (K Myr$^{-1}$) | age (Gyr) | age with latent heat (Gyr) |
|---|---|---|---|
| 30 | 0.156 | 0.99 | 1.29 |
| 60 | 0.107 | 1.45 | 1.90 |
| 90 | 0.057 | 2.71 | 3.55 |
| 110 | 0.024 | 6.46 | 8.45 |
| 120 | 0.007 | 20.95 | 27.41 |
| 150 | no cooling | — | — |

and, at $k = 30$ W m$^{-1}$ K$^{-1}$, a CMB heat flow of 8, 10 or 12 TW gives an age
of 1.34, 0.99 or 0.78 Gyr (1.76, 1.29, 1.02 Gyr including latent heat). Two lessons
follow:

* the age is **not** a measurement that pins down anything on its own — it is a
  *ratio* of assumed quantities, with a steep dependence on both $k$ and
  $Q_\text{CMB}$;
* the "young inner core" statements in the literature are conditional on
  low-conductivity (or low-conduction-loss) models, and become impossible if $k$
  reaches the threshold of section 5.2.

Note also the direction of the bias: neglecting gravitational energy release (which
also powers the dynamo) makes the model age too large, while neglecting a radiogenic
component in the core makes it too small.

## 7. The dynamo, and what it tells us about composition

### 7.1 Magnetic Reynolds number and diffusion time

The induction equation, obtained by combining Ohm's law with Ampère's and Faraday's
laws in a moving conductor, is

$$\frac{\partial \mathbf{B}}{\partial t}
= \underbrace{\nabla\times\left(\mathbf{u}\times\mathbf{B}\right)}_\text{advection}
+ \underbrace{\eta\nabla^{2}\mathbf{B}}_\text{diffusion},
\qquad \eta = \frac{1}{\mu_0\sigma}.$$

Scaling length by $L$, velocity by $U$ and time by $L/U$ gives the single
dimensionless group that decides whether a flow can regenerate a field:

$$Rm = \frac{UL}{\eta} = \mu_0\sigma U L .$$

For the model's inputs — $\sigma = 10^{6}$ S m$^{-1}$, $U = 5\times10^{-4}$ m s$^{-1}$,
$L = 2258$ km — the magnetic diffusivity is

$$\eta = \frac{1}{\mu_0\sigma} = \frac{1}{(4\pi\times10^{-7})(10^{6})}
= 0.796\ \mathrm{m^{2}s^{-1}},$$

$$Rm = \frac{(5\times10^{-4})(2.258\times10^{6})}{0.796} = 1419 .$$

Dynamo action requires $Rm$ above a threshold of order 10–100, so the core clears the
bar easily. The same numbers give the magnetic diffusion time

$$\tau_\eta = \frac{L^{2}}{\eta} = \frac{(2.258\times10^{6})^{2}}{0.796}
= 6.41\times10^{12}\ \mathrm{s} \approx 2.0\times10^{5}\ \mathrm{yr},$$

which is the key argument: an *unmagnetised* core would re-diffuse a field away in
$2\times10^{5}$ years, so a palaeomagnetic record of a field billions of years old
requires a continuously maintained dynamo.

### 7.2 Why composition, not just heat

The Elsasser number measures the Lorentz to Coriolis force ratio,

$$\Lambda = \frac{\sigma B^{2}}{\rho\Omega}
= \frac{(10^{6})(10^{-3})^{2}}{(9900)(7.292\times10^{-5})} = 1.39,$$

of order unity — the observed regime of the geodynamo. A dynamo needs a *buoyancy*
source to drive $\mathbf{u}$; two are available:

* **thermal**: hot fluid rises, but in the outer core the adiabat is the reference
  state and most of the heat flow is consumed by conduction (section 5.2), leaving
  little to drive convection;
* **compositional**: light elements released at the ICB as the inner core freezes are
  buoyant and rise, converting gravitational energy into motion independently of the
  temperature gradient.

The model's inner-core growth rate of 0.94 km Myr$^{-1}$ corresponds to a mass growth
of $7.15\times10^{6}$ kg s$^{-1}$, of which the light-element fraction of the liquid
($5.2$ mass %) is rejected at $3.72\times10^{5}$ kg s$^{-1}$. Accumulated over a
billion years that is $\sim10^{19}$ kg, comparable with a large part of the core's
light-element inventory. So light elements are not merely a passive explanation for a
density deficit: they are the reason the dynamo can keep running once conduction has
taken its share of the heat.

## 8. Assumptions and regime of validity

Everything above is conditional on the following, and each line is a place where a
different choice moves the answers by a few per cent to a factor of several:

1. **Spherical symmetry and hydrostatic equilibrium.** No lateral structure and no
   dynamics, which is valid at the 1 % level for radial averages.
2. **The assumed density profile.** Three mantle shells and two smooth core
   polynomials; it reproduces the Earth's mass to 1.0 % and gives
   $P_\text{CMB} = 126.2$ GPa.
3. **The assumed pure-iron EOS.** $\rho_0 = 8.00$ g cm$^{-3}$, $K_0 = 160$ GPa,
   $K_0' = 5.0$. A 5 % error in $K_0$ moves the CMB deficit by about a percentage
   point, i.e. the light-element fraction by 20 % relative.
4. **A linear thermal correction** with $\alpha = 10^{-5}$ K$^{-1}$. At core
   conditions a thermal-pressure formulation is better; the neglected non-linearity
   is of the order of the difference between the 3.7 % and 4.9 % corrections quoted
   above.
5. **Ideal volume additivity** for the light element, with no Fe–light-element
   interaction and a single "average" light element rather than a mixture. Real
   interactions, and the difference between interstitial O and substituting Si, matter
   at the level of the conclusions.
6. **A single adiabatic reference state** with constant $\alpha$ and $C_p$; the
   963 K rise is an order-of-magnitude estimate.
7. **The melting-curve slope is assumed, not measured.** It decides whether a liquid
   outer core exists and where the ICB sits — the weakest link in the chain.
8. **The ICB jump decomposition** assumes a 3 % melting jump; melting and
   compositional contributions cannot be separated without a known partition
   coefficient.
9. **A parameterised dynamo.** $Rm$ and $\Lambda$ test plausibility from assumed
   $\sigma$, $U$ and $B$; the mechanism itself needs the full induction equation
   ([08-01-05](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/05-dynamo-theory.md)).

## 9. Worked examples

### Example 1 — pressure at the CMB by hand

The pressure at the CMB is the weight of the mantle per unit area, to within the
variation of gravity across the mantle. Take the model's mantle mass
$3.998\times10^{24}$ kg and an average gravity of 9.9 m s$^{-2}$ acting over the
mantle's mean radius $5.75\times10^{6}$ m:

$$P_\text{CMB} \simeq \frac{M_\text{mantle}\,g_\text{avg}}{4\pi \bar r^{2}}
= \frac{(3.998\times10^{24})(9.9)}{4\pi(5.75\times10^{6})^{2}}
= \frac{3.96\times10^{25}}{4.15\times10^{14}} = 9.53\times10^{10}\ \mathrm{Pa}
= 95\ \mathrm{GPa}.$$

The full numerical integration gives 126.2 GPa. The difference is the price of using
a single average gravity instead of the actual $g(r)$ profile and a mean radius
instead of the true weighting — which is why no serious core model uses the
one-line version. The *scaling* it exposes is the useful part:

$$P_\text{CMB} \propto \frac{M_\text{mantle}\,\bar g}{4\pi\bar r^{2}} .$$

### Example 2 — deficit to light-element fraction

At the top of the outer core, $\rho_\text{mix} = 9.900$ and
$\rho_\text{Fe} = 10.794$ g cm$^{-3}$; take $\rho_\text{L} = 5.0$ g cm$^{-3}$. Then

$$\frac{1}{\rho_\text{mix}} = 0.101010,\qquad
\frac{1}{\rho_\text{Fe}} = 0.092644,\qquad
\frac{1}{\rho_\text{L}} = 0.200000\ \mathrm{cm^{3}g^{-1}},$$

$$x = \frac{0.101010 - 0.092644}{0.200000 - 0.092644}
= \frac{0.008366}{0.107356} = 0.0779 \approx 7.8\ \text{mass}\,\%.$$

Because the numerator is a small difference of two similar numbers, the *relative*
error in $x$ is amplified: a 0.5 % error in either density becomes a ~6 % relative
error in the deficit. **Deficit-to-composition inversion is an ill-conditioned
problem, as every core-composition paper has to admit.**

### Example 3 — the adiabatic gradient and its heat flow

With $\alpha = 10^{-5}$ K$^{-1}$, $g = 10.559$ m s$^{-2}$, $T = 4000$ K and
$C_p = 800$ J kg$^{-1}$ K$^{-1}$:

$$\left|\frac{dT}{dr}\right|_\text{CMB}
= \frac{(10^{-5})(10.559)(4000)}{800} = 5.28\times10^{-4}\ \mathrm{K\,m^{-1}}
= 0.528\ \mathrm{K\,km^{-1}}.$$

Conducted heat flow for $k = 30$ W m$^{-1}$ K$^{-1}$:

$$Q_\text{ad} = 4\pi(3.48\times10^{6})^{2}(30)(5.28\times10^{-4})
= (1.522\times10^{14})(1.58\times10^{-2}) = 2.41\times10^{12}\ \mathrm{W}
= 2.41\ \mathrm{TW}.$$

Doubling $k$ doubles $Q_\text{ad}$; the budget is linear in conductivity and the
threshold of 124 W m$^{-1}$ K$^{-1}$ follows immediately from
$Q_\text{ad} = 10$ TW.

### Example 4 — the age of the inner core, and its leverage

With $Q_\text{CMB} - Q_\text{ad} = 10 - 2.41 = 7.59$ TW, $D = 0.126$ K km$^{-1}$ and
$M_\text{core}C_p = 1.533\times10^{27}$ J K$^{-1}$:

$$\Gamma = \frac{7.59\times10^{12}}{1.533\times10^{27}}
= 4.95\times10^{-15}\ \mathrm{K\,s^{-1}} = 0.156\ \mathrm{K\,Myr^{-1}},$$

$$\text{age} = \frac{D\,R_\text{ICB}}{\Gamma}
= \frac{(1.26\times10^{-4})(1.2215\times10^{6})}{4.95\times10^{-15}}
= 3.11\times10^{16}\ \mathrm{s} = 0.99\ \mathrm{Gyr}.$$

Including the latent-heat term of $4.74\times10^{26}$ J K$^{-1}$ (31 % of the heat
capacity) gives $\Gamma = 3.78\times10^{-15}$ K s$^{-1}$ and an age of 1.29 Gyr.
Now raise $k$ to 90 W m$^{-1}$ K$^{-1}$: $Q_\text{ad} = 7.23$ TW, the excess falls to
2.77 TW, and the age rises to 2.70 Gyr (3.53 Gyr with latent heat). **A factor of 3
in conductivity produces a factor of 2.7 in the age** — because the age is inversely
proportional to a difference of two large numbers that are allowed to approach each
other.

## 10. Python demonstration

[`code/core_composition_demo.py`](code/core_composition_demo.py) builds the assumed
radial model, integrates mass, gravity and pressure, evaluates and inverts a
Birch–Murnaghan pure-iron EOS with a thermal correction, converts the density deficit
into a light-element mass fraction (with sensitivity studies and a consistency test),
derives the adiabatic gradient and the conducted heat flow, computes cooling rates
and inner-core ages with and without latent heat, and estimates the dynamo
diagnostics $Rm$, $\tau_\eta$ and $\Lambda$. It prints labelled results with units and
runs in about 0.1 s:

```bash
cd 12-global-geophysics-interior/02-composition-and-mineral-physics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python core_composition_demo.py
```

The demonstration is print-only; it does not open a window. Nothing in it is a
measurement.

## 11. Exercises

[Exercises](exercises/04-core-composition-exercises.md) with
[solutions](exercises/04-core-composition-solutions.md): hydrostatic pressure,
deficit inversion, adiabatic heat flow, the inner-core age and its leverage, and the
dynamo diagnostics, in three tiers.

## Mastery checkpoint

Without notes:

> A model core has a total mass of $1.90\times10^{24}$ kg, $C_p = 800$
> J kg$^{-1}$ K$^{-1}$, and an adiabatic gradient at the CMB of
> $5.3\times10^{-4}$ K m$^{-1}$. The core-side area is $4\pi R_c^{2}$ with
> $R_c = 3480$ km, and the melting-curve difference is
> $D = 1.2\times10^{-4}$ K m$^{-1}$.
> **(a)** Compute $Q_\text{ad}$ for $k = 40$ W m$^{-1}$ K$^{-1}$.
> **(b)** For a CMB heat flow of 11 TW, compute the cooling rate in K Myr$^{-1}$.
> **(c)** Compute the inner-core age, ignoring latent heat, and state one reason the
> true value differs.
> **(d)** Compute the threshold conductivity at which the inner core stops growing
> altogether.

A worked version appears in the lesson-04
[solutions](exercises/04-core-composition-solutions.md).

## Common pitfalls

1. **Comparing densities at different temperatures.** The thermal correction is 4–5 %
   at core conditions — larger than most of the effects being discussed. An
   unthermalised deficit is not a deficit.
2. **Quoting a light-element fraction without the assumed $\rho_\text{L}$.** The same
   deficit gives anything from 4 % to 14 % depending on that one number.
3. **Treating the inner-core age as a measurement.** It is a ratio of assumed
   quantities with a steep dependence on conductivity and CMB heat flow; report the
   assumptions with the number.
4. **Forgetting the latent heat.** It is ~30 % of the effective heat capacity here and
   lengthens the age by the same factor.
5. **Using $Q_\text{ad} = 4\pi R^2 k\,\Delta T/\Delta r$ with a volume-averaged
   gradient.** The adiabatic flux is defined *at the CMB*, with the CMB gradient and
   $R_c$ — not with the outer-core average.
6. **Getting the direction of the adiabat right.** The temperature rises inward, so
   $dT/dr < 0$; mixing up the sign makes the core freeze from the top.
7. **Assuming a solid inner core is inevitable.** It requires the melting curve to be
   shallower than the adiabat; the observed structure constrains that slope, but the
   slope itself is not measured.
8. **Reading $Rm \sim 10^{3}$ as "the dynamo is proven".** It shows the core *can*
   sustain dynamo action; the mechanism needs the full induction equation and, in
   practice, numerical models.
9. **Neglecting composition in the buoyancy budget.** Thermal buoyancy alone is hard
   to reconcile with the conduction loss; the light-element flux from inner-core
   growth is not a detail.

## Related modules

- [01 Mantle Composition and Peridotite Models](01-mantle-composition.md) — the same
  deficit-and-mixing argument for the mantle, where samples exist.
- [02 High-Pressure Experiments and Diamond Anvil Cells](02-high-pressure-experiments.md) —
  how the pure-iron EOS used here is actually measured.
- [03 Ab Initio Mineral Physics and Elastic Constants](03-ab-initio-mineral-physics.md) —
  the computed side of the same reference states.
- [12-01-06 Outer Core, Inner Core Anisotropy and Rotation](../01-seismic-structure-of-the-earth/06-outer-and-inner-core.md) —
  the seismic observations that define the targets.
- [12-01-05 Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite](../01-seismic-structure-of-the-earth/05-core-mantle-boundary.md) —
  the thermal boundary layer that sets $Q_\text{CMB}$.
- [08-01-05 The Geodynamo: Mechanism and Evidence](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/05-dynamo-theory.md) —
  the induction equation in full, and the numerical dynamo.
- [13-02-01 Rayleigh-Benard Convection Applied to the Mantle](../../13-geodynamics-tectonics/02-mantle-convection/01-rayleigh-benard-mantle.md) —
  the convective framework borrowed here for the core.
- [04-01-01 Crust, Mantle, Core: Seismological and Geochemical Evidence](../../04-earth-science-geology/01-earth-structure/01-layered-earth.md) —
  the introductory version.

## Self-assessment checklist

- [ ] I can integrate $dP/dr = -\rho g$ for a layered model and check the total mass.
- [ ] I can invert a Birch–Murnaghan EOS numerically and apply a thermal correction.
- [ ] I can convert a density deficit into a light-element mass fraction and state
      three assumptions the conversion needs.
- [ ] I can derive $dT/dr = -\alpha g T/C_p$ and evaluate the adiabatic rise.
- [ ] I can compute $Q_\text{ad}$, find the threshold conductivity, and explain the
      new core paradox.
- [ ] I can estimate an inner-core age, with and without latent heat, and say what it
      depends on.
- [ ] I can compute $\eta$, $Rm$, $\tau_\eta$ and $\Lambda$ and interpret each.
