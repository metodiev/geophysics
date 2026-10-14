---
id: 15-01-01
title: "Seawater Properties: Temperature, Salinity, Density"
level: intermediate
prereqs: ["02-06-01", "02-06-07", "01-01-03"]
tags: [oceanography, marine-geophysics, seawater, equation-of-state, density, buoyancy, cabbeling]
---

# Seawater Properties: Temperature, Salinity, Density

> **All models and data in this module are SYNTHETIC.** The equation of state
> used here is a *teaching* equation of state: its coefficients are chosen
> numbers, printed by the demonstration in `code/`, not measured coefficients of
> real seawater. No data set, station, cruise or salinity standard is reproduced.

Almost every quantity in physical oceanography is a density in disguise. A
current is driven by a horizontal pressure gradient, and the pressure gradient
is set by the *weight* of the water above — which depends on temperature and
salinity only through their effect on density. Wind, tides and river discharge
all enter the ocean as forces, but the ocean's slow interior circulation runs on
density differences of a few parts in $10^{4}$.

That creates the central difficulty of this lesson, and of the module. Density is
not measured directly and is not a function of one variable. It is a function
$ \rho(T,S,p)$ of three, only two of which we can measure cheaply, and the
sensitivity to one of them (compression) is *larger* than the sensitivity to
either of the others. The ocean is nearly, but not exactly, incompressible, and
the "nearly" is where all the structure lives.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** practical salinity, potential temperature and potential density, and
   state precisely which pressure a "potential" property is referenced to.
2. **Derive** $\sigma_t$, the thermal expansion coefficient $\alpha$ and the
   haline contraction coefficient $\beta$ from a given equation of state, and
   **state** their units.
3. **Compute** the density of a mixture of two water masses and **quantify** the
   cabbeling anomaly, explaining why a *linear* equation of state gives exactly
   zero.
4. **Derive** and **evaluate** the buoyancy (Brunt–Väisälä) frequency
   $N^{2} = (g/\rho)\,\partial\rho_\theta/\partial z$ from a temperature and
   salinity profile, and state the sign convention that makes $N^{2}$ positive
   for a stable column.
5. **Explain** why in-situ density must not be used for a stability argument, and
   **quantify** the error that would follow if it were.
6. **Compute** a first-order sound speed from a chosen formula and state why a
   fractional sound-speed error maps almost one-for-one into a fractional depth
   error.
7. **State** the regime of validity of a linear equation of state and quantify
   the error it makes over a stated $T$–$S$ range.

## Prerequisites

- [02-06-01 Fluid Statics and Pressure](../../02-physics/06-fluid-mechanics/01-fluid-statics.md) —
  hydrostatic balance, which converts depth into pressure.
- [02-06-07 Geophysical Fluids and Their Properties](../../02-physics/06-fluid-mechanics/07-geophysical-fluids.md) —
  the properties that make a fluid geophysical: stratification and rotation.
- [01-01-03 Units and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md) —
  the habit of checking that a slowness times a length is a time.

## 1. What is being measured

Three quantities describe a seawater parcel for most purposes.

| Quantity | Symbol | Unit | What it measures |
|---|---|---|---|
| Temperature | $T$ | $^\circ$C | molecular kinetic energy, referenced to the ice point |
| Salinity | $S$ | g kg$^{-1}$ (practical) | dissolved mass, conventionally determined from electrical conductivity |
| Pressure | $p$ | dbar | hydrostatic load; $1\ \mathrm{dbar} = 10^{4}\ \mathrm{Pa}$ |

Two cautions that are easy to state and hard to remember.

**Salinity is defined by a measurement procedure, not by a mass.** What a
conductivity sensor records is a conductivity ratio against a standard solution;
the number reported as salinity is that ratio converted by a assigned
polynomial. The scale has been redefined more than once, and the definitions are
not interchangeable at the level of accuracy we care about. Whenever a salinity
enters a calculation, the scale it is on is part of the data.

**Temperature is not a conservative property.** A parcel moved downward is
compressed and warms adiabatically. The temperature that is conserved under
adiabatic displacement is the **potential temperature** $\theta$, the temperature
the parcel would have if brought adiabatically to a reference pressure
(conventionally the surface, $p = 0$). Every "potential" property in this
lesson is a property evaluated at that reference pressure.

### 1.1 One more definition: sigma

Because $\rho \approx 1027\ \mathrm{kg\,m^{-3}}$ and variations are in the third
decimal place, oceanographers work with anomalies:

$$\sigma_t = \rho(S, T, p = 0) - 1000\ \mathrm{kg\,m^{-3}}, \qquad
\sigma_\theta = \rho(S, \theta, p = 0) - 1000\ \mathrm{kg\,m^{-3}}.$$

Both are in kg m$^{-3}$. The subtraction of exactly 1000 is a reporting
convention, not physics, but it makes the interesting digits visible.

## 2. A teaching equation of state

We need a $\rho(T,S,p)$. The demonstration uses

$$\boxed{\;\rho(T,S,p) = \rho_0\left[1 - \alpha\,(T - T_0) + \beta\,(S - S_0)
+ \kappa\,p\right]\;}$$

with the chosen reference state $\rho_0 = 1027.0\ \mathrm{kg\,m^{-3}}$,
$T_0 = 10\ ^\circ$C, $S_0 = 35\ \mathrm{g\,kg^{-1}}$, and the chosen coefficients

$$\alpha = 1.70\times10^{-4}\ ^\circ\mathrm{C}^{-1},\quad
\beta = 7.60\times10^{-4}\ \mathrm{(g\,kg^{-1})^{-1}},\quad
\kappa = 4.40\times10^{-6}\ \mathrm{dbar^{-1}}.$$

These numbers are *typical in magnitude* of real seawater but they are chosen
values; nothing below depends on them being the real ones. Dimensional check:
$\alpha(T-T_0)$, $\beta(S-S_0)$ and $\kappa p$ are all dimensionless, so they may
be added — a fact worth verifying, because a coefficient quoted in the wrong
units is the commonest error in this subject.

### 2.1 Numerical example — the sensitivity ratio

The demonstration prints, from finite differences on the grid,

$$\frac{\partial \sigma_t}{\partial S} = +0.781\
\mathrm{kg\,m^{-3}\,(g\,kg^{-1})^{-1}}, \qquad
\frac{\partial \sigma_t}{\partial T} = -0.175\ \mathrm{kg\,m^{-3}\,^\circ C^{-1}},$$

whose ratio is $0.781/0.175 = 4.5$. **A salinity change of
$1\ \mathrm{g\,kg^{-1}}$ is worth a temperature change of
$4.5\ ^\circ$C.** This single number explains why the ocean's salinity
structure, though small in absolute terms, is dynamically decisive.

## 3. Compressibility: why in-situ density is the wrong tool for stability

At $T = 4\ ^\circ$C and $S = 34.9\ \mathrm{g\,kg^{-1}}$, the demonstration walks
one water mass down the column:

| $z$ (m) | $p$ (dbar) | $\rho$ in situ (kg m$^{-3}$) | $\rho_\theta$ (kg m$^{-3}$) | compression term |
|---|---|---|---|---|
| 0 | 0 | 1027.969 | 1027.969 | 0.000 |
| 1000 | 1007 | 1032.522 | 1027.969 | 4.553 |
| 4000 | 4030 | 1046.180 | 1027.969 | 18.211 |
| 6000 | 6045 | 1055.285 | 1027.969 | 27.316 |

At 4000 m, compression adds $18.211\ \mathrm{kg\,m^{-3}}$, i.e. $1.77\,\%$ of
the density, from pressure alone with $T$ and $S$ unchanged. Expressed as an
equivalent cooling that would produce the same density change, it is
$1.77\times10^{-2}/\alpha \approx 104\ ^\circ$C. No temperature difference in the
ocean comes close to that.

So a stability calculation that uses in-situ density is wrong at leading order.
The correct object is the **potential density** $\rho_\theta$: density evaluated
at the reference pressure. The vertical gradient of potential density, not of
in-situ density, decides whether a parcel displaced upward comes back.

### 3.1 Derivation of the buoyancy frequency

Let $z$ be depth, positive downward, and let $\rho_\theta(z)$ be potential
density. Displace a parcel of density $\rho_\theta(z_0)$ upward by
$\delta z < 0$ into an environment of density $\rho_\theta(z_0 + \delta z)$.
The buoyancy force per unit mass is

$$b = g\frac{\rho_\theta(z_0 + \delta z) - \rho_\theta(z_0)}{\rho_\theta}
\approx g\frac{\partial \rho_\theta}{\partial z}\frac{\delta z}{\rho_\theta}.$$

With $\delta z$ measured positive *upward* as $\zeta = -\delta z$ and the
displacement equation $\ddot\zeta = -N^{2}\zeta$, we read off

$$\boxed{\;N^{2} = +\frac{g}{\rho_0}\frac{\partial \rho_\theta}{\partial z}
\qquad (z\mathrm{\ positive\ downward})\;}$$

and stability requires $N^{2} > 0$, i.e. potential density increasing with
depth. **The sign of the relation depends on the sign convention for $z$.** In
height coordinates the same physics reads $N^{2} = -(g/\rho)\,\partial\rho/\partial z$.
Getting this sign wrong turns a stable ocean into a convecting one and is a
classic first-year error; the demonstration computes it with $z$ downward and
prints positive values.

### 3.2 Numerical example — $N^{2}$ from a profile

The demonstration's synthetic profile is

$$T(z) = 4 + 22e^{-z/120}\ ^\circ\mathrm{C}, \qquad
S(z) = 34.8 + 0.5\left(1 - e^{-z/300}\right)\ \mathrm{g\,kg^{-1}},$$

with $z$ in metres. Evaluating $\rho_\theta$ on a $1\ \mathrm{m}$ grid and
differencing:

| $z$ (m) | $T$ ($^\circ$C) | $S$ (g kg$^{-1}$) | $\sigma_t$ | $N^{2}$ (s$^{-2}$) | $N$ (rad s$^{-1}$) | period (s) |
|---|---|---|---|---|---|---|
| 0 | 26.00 | 34.800 | 24.050 | $3.175\times10^{-4}$ | 0.01782 | 353 |
| 100 | 13.56 | 34.942 | 26.333 | $1.418\times10^{-4}$ | 0.01191 | 528 |
| 500 | 4.34 | 35.206 | 28.148 | $7.087\times10^{-6}$ | 0.00266 | 2360 |
| 1500 | 4.00 | 35.297 | 28.279 | $8.494\times10^{-8}$ | 0.00029 | 21559 |

The buoyancy period across the thermocline is $353\ \mathrm{s} \approx 6$ min;
at 1500 m it is $21559\ \mathrm{s} \approx 6$ h. **$N$ spans a factor of 60 in
one 1.5 km column.** A single "typical $N$" is therefore a fiction, and any
claim that uses one (for example an internal-wave speed) inherits the error of
that choice.

Hand check at $z=0$. From the profile, $\partial T/\partial z = -22/120 =
-0.18333\ ^\circ\mathrm{C\,m^{-1}}$ and $\partial S/\partial z = 0.5/300 =
1.667\times10^{-3}\ \mathrm{(g\,kg^{-1})\,m^{-1}}$. To first order in the
linear equation of state,

$$\frac{1}{\rho_0}\frac{\partial \rho_\theta}{\partial z}
= -\alpha\frac{\partial T}{\partial z} + \beta\frac{\partial S}{\partial z}
= 1.70\times10^{-4}(0.18333) + 7.60\times10^{-4}(1.667\times10^{-3})
= 3.117\times10^{-5} + 1.267\times10^{-6}
= 3.244\times10^{-5}\ \mathrm{m^{-1}},$$

$$N^{2} = 9.81 \times 3.244\times10^{-5} = 3.18\times10^{-4}\ \mathrm{s^{-2}},$$

against the printed $3.175\times10^{-4}$ — agreement to $0.2\,\%$, the
difference being the curvature of the exponential neglected by the one-sided
difference. **Note which term dominates:** the thermal term is $3.12\times10^{-5}$
and the haline term $1.27\times10^{-6}$, so salinity contributes $4\,\%$ of the
stratification here. In the deep ocean with a weak thermal gradient the same
comparison reverses, and salinity becomes the controlling term.

## 4. Cabbeling: mixing as a source of dense water

Because $\rho(T,S)$ is curved, the density of a *mixture* is not the mean of the
densities of its constituents. The demonstration solves for two water masses
with exactly equal density but very different $T$ and $S$:

| | $T$ ($^\circ$C) | $S$ (g kg$^{-1}$) | $\rho$ (kg m$^{-3}$) |
|---|---|---|---|
| water A | 14.00 | 35.500 | 1026.5687 |
| water B | 2.00 | 33.289 | 1026.5687 |
| 50/50 mixture | 8.00 | 34.395 | **1026.84595** |

The mean of the two densities is $1026.56866$ and the mixture is
$1026.84595\ \mathrm{kg\,m^{-3}}$: the mixture is denser by
$277.3\ \mathrm{g\,m^{-3}}$. This is **cabbeling**, and it matters because it
means a water mass can sink as a consequence of mixing rather than in spite of
it.

### 4.1 Why a linear equation of state cannot show it

Write $\rho(T,S) = \rho_0[1 - \alpha(T-T_0) + \beta(S-S_0)]$, linear in both
arguments. Then, since $T_m = \tfrac12(T_A+T_B)$ and $S_m = \tfrac12(S_A+S_B)$,

$$\rho(T_m, S_m) = \rho_0\left[1 - \alpha\left(\tfrac{T_A+T_B}{2}-T_0\right)
+ \beta\left(\tfrac{S_A+S_B}{2}-S_0\right)\right]
= \tfrac12\left[\rho(T_A,S_A) + \rho(T_B,S_B)\right].$$

The anomaly is *identically zero*. Cabbeling is not a small correction to a
linear theory; it is invisible to one. The demonstration prints
$0.0000\ \mathrm{g\,m^{-3}}$ for the linear case alongside
$277.3\ \mathrm{g\,m^{-3}}$ for the curved one.

### 4.2 Where the curvature enters, and how big it is

The demonstration's nonlinear form makes $\alpha$ depend on temperature,
$\alpha(T) = \alpha_0 + \Delta_\alpha (T - T_0)$ with
$\Delta_\alpha = 1.50\times10^{-5}\ ^\circ\mathrm{C}^{-2}$, so that

$$\rho(T,S,p) = \rho_0\left[1 - \left(\alpha_0\Delta T +
\tfrac12\Delta_\alpha \Delta T^{2}\right) + \beta\Delta S + \kappa p\right],
\qquad \Delta T = T - T_0 .$$

The quadratic term is the entire source of cabbeling. **The size of the effect
is set by $\Delta_\alpha$, which is a chosen number.** A real estimate of
cabbeling requires real $\alpha(T)$ — and then the answer is a few tens of
$\mathrm{g\,m^{-3}}$, not hundreds. Our value is large because our curvature is
large; the *structure* of the result is what transfers.

## 5. Sound speed: a property with a sting

A chosen teaching formula,

$$c(T,S,z) = 1449 + 4.6T - 0.055T^{2} + 1.34(S-35) + 0.016z\ \mathrm{m\,s^{-1}},$$

gives the demonstration's table:

| $T$ ($^\circ$C) | $z$ (m) | $c$ (m s$^{-1}$) |
|---|---|---|
| 0 | 0 | 1449.0 |
| 10 | 0 | 1489.5 |
| 25 | 0 | 1529.6 |
| 10 | 1000 | 1505.5 |
| 4 | 4000 | 1530.5 |
| 4 | 6000 | 1562.5 |

The range across the ocean is $5.9\,\%$. The reference value $c = 1500\
\mathrm{m\,s^{-1}}$ is the one used throughout this folder.

The sting: an echo sounder converts a two-way travel time $t$ into a depth
$z = ct/2$ using an *assumed* $c$. If the true speed differs by a fraction
$\epsilon$, then $z$ is wrong by the same fraction, because $t$ is measured and
$c$ is assumed:

$$\frac{\delta z}{z} = \frac{\delta c}{c}.$$

A $1\,\%$ error in $c$ — well within the real range of ocean sound speeds — is a
$1\,\%$ error in depth: $10\ \mathrm{m}$ at $1000\ \mathrm{m}$ depth, $40\
\mathrm{m}$ at $4000\ \mathrm{m}$. This is the quantitative reason that marine
swath and sub-bottom surveys resist spending effort on sound-speed profiles, and
it is picked up again in
[Module 15-02](../02-marine-geophysics-methods/README.md).

## 6. Assumptions and regime of validity

1. **Small perturbations.** The linear equation of state is a first-order Taylor
   expansion about $(T_0, S_0, p=0)$. Every coefficient is a derivative at that
   point and is held constant.
2. **Quantified error.** Over $T \in [0,30]\ ^\circ$C and
   $S \in [33,37]\ \mathrm{g\,kg^{-1}}$ (2501 grid points), the demonstration
   measures a maximum discrepancy against the curved form of
   $3.081\ \mathrm{kg\,m^{-3}}$, i.e. $0.300\,\%$ of $\rho_0$, equivalent to a
   $17.65\ ^\circ$C temperature error. That is *too large* for a cabbeling
   calculation and *acceptable* for an order-of-magnitude stability argument.
3. **No pressure dependence of the coefficients.** In reality $\alpha$ falls
   sharply with pressure and even changes sign at low temperature and high
   pressure; our $\alpha$ does not.
4. **Salinity treated as a single conserved scalar.** No distinction between the
   conservative and the practical scale is made.
5. **No dissolved gases, no suspended sediment.** Both change density and, in
   the second case, sound speed.
6. **Locally valid only.** Everything above is a point property. Turning it into
   a statement about a water mass requires assuming the parcel moves without
   exchanging heat or salt — the adiabatic and isohaline assumption.

## 7. Worked examples

### Example 1 — density difference between two stations

Station A: $T = 18.0\ ^\circ$C, $S = 35.60\ \mathrm{g\,kg^{-1}}$.
Station B: $T = 6.0\ ^\circ$C, $S = 35.10\ \mathrm{g\,kg^{-1}}$.
Both at the surface.

$$\rho_A = 1027\left[1 - 1.70\times10^{-4}(8) + 7.60\times10^{-4}(0.60)\right]
= 1027\left[1 - 1.360\times10^{-3} + 4.560\times10^{-4}\right]
= 1027(0.999120) = 1026.096\ \mathrm{kg\,m^{-3}},$$

$$\rho_B = 1027\left[1 - 1.70\times10^{-4}(-4) + 7.60\times10^{-4}(0.10)\right]
= 1027\left[1 + 6.800\times10^{-4} + 7.600\times10^{-5}\right]
= 1027(1.000756) = 1027.776\ \mathrm{kg\,m^{-3}}.$$

$\sigma_t(A) = 26.10$ and $\sigma_t(B) = 27.78$: A is lighter by
$1.68\ \mathrm{kg\,m^{-3}}$. A is also saltier by $0.50\ \mathrm{g\,kg^{-1}}$,
which on its own would make it *heavier* by
$\beta\rho_0(0.50) = 0.390\ \mathrm{kg\,m^{-3}}$. Temperature therefore wins by
a factor $4.4$ here, essentially the sensitivity ratio of Section 2.1.

### Example 2 — the depth of a pressure level

Using the demonstration's conversion $p = \rho_0 g z/10^{4}$ dbar:

$$z = 4000\ \mathrm{m} \Rightarrow p = \frac{1027 \times 9.81 \times 4000}{10^{4}}
= 4030\ \mathrm{dbar}.$$

The conversion is exact only for a constant density; a real column's pressure at
4000 m differs by a per cent or so because $\rho$ rises with depth. The
demonstration's table uses this same approximation, and the compression term it
reports ($18.211\ \mathrm{kg\,m^{-3}}$) is correspondingly approximate.

### Example 3 — reading a stability table

At $z = 0$ the demonstration gives $N^{2} = 3.175\times10^{-4}\ \mathrm{s^{-2}}$
and at $z = 1500$ m, $N^{2} = 8.494\times10^{-8}\ \mathrm{s^{-2}}$. The ratio is
$3.175\times10^{-4}/8.494\times10^{-8} = 3.74\times10^{3}$.

Two consequences follow directly. First, an internal wave of fixed frequency
exists in a narrower band of wavenumbers in the deep water than in the
thermocline: the band is bounded by $f$ and $N$, and $N$ has shrunk by a factor
60. Second, an "average $N$" over the column would misrepresent both ends by
orders of magnitude. If a problem needs $N$, it needs $N(z)$.

## 8. Python demonstration

`code/seawater_properties_demo.py` prints everything quoted above, with units:

1. the $\sigma_t$ surface on a synthetic $T$–$S$ grid, plus the two
   sensitivities and their ratio;
2. the compression term from 0 to 6000 m for one water mass;
3. the cabbeling experiment, including the exact zero obtained with the linear
   equation of state;
4. $N^{2}$, $N$ and the buoyancy period on the demonstration profile;
5. the sound-speed table and its total range;
6. an error budget: the maximum linear-versus-curved discrepancy over a stated
   $T$–$S$ box.

Run it with

```bash
cd 15-oceanography-marine/01-physical-oceanography/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seawater_properties_demo.py
```

It is print-only, needs no network, uses the fixed seed
`np.random.default_rng(20261014)`, and exits 0 in well under a second.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-seawater-properties-exercises.md`](exercises/01-seawater-properties-exercises.md)
and
[`exercises/01-seawater-properties-solutions.md`](exercises/01-seawater-properties-solutions.md).

- ★ Compute $\sigma_t$ for $(T,S) = (5\ ^\circ\mathrm{C}, 34.5\
  \mathrm{g\,kg^{-1}})$ and state the units of each factor.
- ★★ Derive $N^{2} = (g/\rho_0)\partial\rho_\theta/\partial z$ from the
  displacement argument, and evaluate it for the demonstration profile at
  $z = 200$ m.
- ★★ Reproduce the cabbeling anomaly by hand for the two water masses of
  Section 4, and explain why the answer depends on $\Delta_\alpha$.
- ★★★ Design a measurement that would distinguish "the water column is stable"
  from "the water column is stable with respect to adiabatic displacement", and
  state what data it needs.

## Mastery checkpoint

Without notes, and showing your arithmetic:

> A synthetic ocean station has, at the surface, $T = 22.0\ ^\circ$C and
> $S = 35.80\ \mathrm{g\,kg^{-1}}$, and at 1000 m, $T = 6.0\ ^\circ$C and
> $S = 35.00\ \mathrm{g\,kg^{-1}}$. Use $\rho_0 = 1027.0\ \mathrm{kg\,m^{-3}}$,
> $\alpha = 1.70\times10^{-4}\ ^\circ\mathrm{C}^{-1}$ and
> $\beta = 7.60\times10^{-4}\ \mathrm{(g\,kg^{-1})^{-1}}$.
> **(a)** Compute $\sigma_t$ at both levels and state which is denser.
> **(b)** Compute $N^{2}$ from the two levels as a single finite difference, and
> the corresponding buoyancy period. State your sign convention explicitly.
> **(c)** A colleague computes $N^{2}$ from in-situ densities, adding the
> compression term with $\kappa = 4.40\times10^{-6}\ \mathrm{dbar^{-1}}$ at
> $p = 1007\ \mathrm{dbar}$. Compute the spurious $N^{2}$ they obtain and state
> the factor by which the column appears more stable than it is.
> **(d)** State two properties of the profile that the two numbers above do not
> determine.

Worked versions of (a)–(c) appear in the lesson-01
[solutions](exercises/01-seawater-properties-solutions.md), and the same
calculation is printed by `code/seawater_properties_demo.py` in its sections 2
and 4.

## Common pitfalls

1. **Using in-situ density for stability.** Section 3: compression contributes
   $1.77\,\%$ of the density at 4000 m, an order of magnitude more than any $T$
   or $S$ contrast. Only $\rho_\theta$ may be differenced for a stability test.
2. **Flipping the sign of $N^{2}$.** With $z$ positive downward the relation is
   $N^{2} = +(g/\rho_0)\partial\rho_\theta/\partial z$. Writing the minus sign
   from height coordinates produces a stable ocean that looks convecting.
3. **Attributing cabbeling to a linear equation of state.** It is exactly zero
   there, by construction (Section 4.1).
4. **Quoting a single $N$.** The demonstration's $N$ varies by a factor 60 over
   1.5 km. Report the profile or the range.
5. **Treating salinity as a mass.** It is defined by a conductivity procedure on
   an assigned scale; two "salinity" numbers on different scales are not
   interchangeable at the accuracy that matters here.
6. **Forgetting that thermal expansion is a function of temperature and
   pressure.** Our constant $\alpha$ is the largest single simplification in the
   lesson and it is the one that fails first in the deep ocean and at low
   temperature.

## Related modules

- [02 Wind-Driven Circulation, Ekman Transport and Gyres](02-wind-driven-circulation.md) —
  what the density field does when the wind pushes on it.
- [03 Thermohaline Circulation and Deep Water Formation](03-thermohaline-circulation.md) —
  where cabbeling and surface buoyancy fluxes become a circulation.
- [04 Internal Waves, Tides and Mixing](04-internal-waves-and-tides.md) —
  the waves whose speed is set by the $N^{2}$ computed here.
- [Module 15-02 Marine Geophysical Methods](../02-marine-geophysics-methods/README.md) —
  the sound-speed sensitivity of Section 5 as it appears in real instruments.
- [02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) —
  the continuum equations this lesson supplies with an equation of state.
- [09-01-01 Resistivity, Conductivity and the Electrical Structure of Rocks](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md) —
  the electrical property that makes salinity measurable in the first place.

## Self-assessment checklist

- [ ] I can define practical salinity, potential temperature and potential
      density, and say what pressure the last two are referenced to.
- [ ] I can derive $\alpha$ and $\beta$ from an equation of state and give units.
- [ ] I can compute a cabbeling anomaly and say why the linear equation of state
      gives zero.
- [ ] I can write $N^{2}$ with the correct sign for depth coordinates.
- [ ] I can compute a sound-speed depth error from a fractional speed error.
- [ ] I can state the measured error of a linear equation of state over a stated
      range, with units.
