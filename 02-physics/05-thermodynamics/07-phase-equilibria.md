---
id: 02-05-07
title: "Thermodynamic Phase Equilibria and Mantle Mineralogy"
level: doctoral
prereqs: ["02-05-03", "02-05-06"]
estimated_minutes: 90
tags: [phase-equilibria, clapeyron, mantle-mineralogy, inner-core]
---

# Thermodynamic Phase Equilibria and Mantle Mineralogy

Thermodynamics decides which mineral assemblage is stable at a given pressure and
temperature. That single statement is why the 410 km and 660 km seismic
discontinuities exist, why they are at those depths and not others, why they move
up and down where the mantle is hot or cold, and why the Earth has a solid inner
core that is hotter than the liquid outer core above it.

This lesson builds the machinery — Gibbs energy, chemical potential, the phase
rule and Clausius–Clapeyron — then applies it three times: to the ice–water
transition (where the answer is measured and the formula can be checked), to the
mantle's two great discontinuities, and to the freezing of the inner core. The core result is counter-intuitive and worth stating at the outset:

> The centre of the Earth is at about 5200 K and is **solid**. The top of the
> outer core is at about 4000 K and is **liquid**. The inner core is roughly
> 1300 K hotter than the liquid above it and is solid anyway, because the melting
> temperature rises with pressure faster than the adiabat does.

That is a thermodynamic statement, and the sharpest test of whether
Clausius–Clapeyron has been understood.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the equilibrium condition between two phases in terms of the Gibbs
   energy, and explain why a denser phase becomes stable at higher pressure.
2. **Derive** the Clausius–Clapeyron relation $\mathrm{d}P/\mathrm{d}T =
   \Delta S/\Delta V = L/(T\Delta V)$ and check it against the measured
   pressure-melting behaviour of ice.
3. **Deduce** the sign of $\Delta S$ for a mantle phase transition from the
   observed slope and the known density change.
4. **Compute** the depth shift of a phase boundary for a temperature perturbation,
   $\Delta z = \gamma\Delta T/(\rho g)$, and explain why the 410 and 660 shift in
   opposite directions.
5. **Explain** why the 410 km and 660 km discontinuities are thermodynamically
   required rather than merely permitted.
6. **Derive** the adiabatic gradient in the core and calculate the melting-curve
   slope required for a solid inner core.
7. **Apply** the Gibbs phase rule and explain what local equilibrium means, and
   when it fails.
8. **Compute** the latent heat and entropy of inner-core growth and the
   present-day power it releases.

## Prerequisites

- [02-05-03 Second Law, Entropy and Irreversibility](./03-second-law.md) — the
  entropy that drives phase stability.
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](./06-geotherms.md)
  — the geotherm that the phase boundaries are plotted against.

## 1. The equilibrium condition

### 1.1 Gibbs energy and chemical potential

For a system at fixed temperature and pressure the quantity that decreases in a
spontaneous process is the **Gibbs free energy**

$$G = U - TS + PV . \tag{1}$$

At equilibrium $G$ is a minimum, so a phase $\beta$ is stable against a phase
$\alpha$ when $G_\beta < G_\alpha$. The molar Gibbs energy of a component is its
**chemical potential** $\mu$, and equilibrium between two phases requires

$$\mu_\alpha(P,T) = \mu_\beta(P,T) . \tag{2}$$

Equation (2) defines a curve in the $P$–$T$ plane — the phase boundary — and
equation (2) differentiated along that curve is the Clausius–Clapeyron relation.

### 1.2 Why pressure favours dense phases

Comparing two phases,

$$G_\beta - G_\alpha = \Delta U - T\Delta S + P\Delta V . \tag{3}$$

For a transition to a denser structure, $\Delta V = V_\beta - V_\alpha < 0$, so the
$P\Delta V$ term becomes more negative as $P$ rises: **the denser phase is
progressively favoured by pressure**. At low pressure the low-density phase wins
because its $U$ and $S$ terms are favourable; at some pressure the two cross. That
crossing is the phase boundary, and it *must* occur somewhere if $\Delta V \ne 0$.
Nothing else — no fit, no assumption — is needed to explain why densification
reactions happen in the mantle: they are required by equation (3).

## 2. Derivation of Clausius–Clapeyron

Differentiate equation (2) along the coexistence curve. For each phase,
$\mathrm{d}\mu = -\bar s\,\mathrm{d}T + \bar v\,\mathrm{d}P$ with $\bar s$, $\bar v$
the molar entropy and volume. Along the boundary both phases remain in
equilibrium, so their chemical potentials change equally:

$$-\bar s_\alpha\,\mathrm{d}T + \bar v_\alpha\,\mathrm{d}P
= -\bar s_\beta\,\mathrm{d}T + \bar v_\beta\,\mathrm{d}P , \tag{4}$$

and therefore

$$\boxed{\ \frac{\mathrm{d}P}{\mathrm{d}T}
= \frac{\bar s_\beta - \bar s_\alpha}{\bar v_\beta - \bar v_\alpha}
= \frac{\Delta S}{\Delta V}
= \frac{L}{T\,\Delta V}\ } \tag{5}$$

for a melting transition, where $L = T\Delta S$ is the latent heat. Equation (5)
is exact for a single-component, single-reaction system in equilibrium. It is one
of the few exact relations in high-pressure petrology, and it is *strongly*
constraining because the signs of $\Delta S$ and $\Delta V$ can often be
determined independently.

### 2.1 Check on ice

Ice melting is the textbook case where the answer is measured. With
$L = 3.34\times10^5$ J kg⁻¹ (nominal), $T = 273.15$ K, $\rho_{\text{ice}} = 917$
and $\rho_{\text{water}} = 1000$ kg m⁻³:

$$\Delta v = \frac{1}{1000} - \frac{1}{917}
= -9.051\times10^{-5}\ \mathrm{m^3\,kg^{-1}}
\quad\text{(negative: liquid water is denser)}, \tag{6}$$

$$\Delta s = \frac{L}{T} = \frac{3.34\times10^5}{273.15}
= 1222.77\ \mathrm{J\,kg^{-1}\,K^{-1}} , \qquad
\frac{\mathrm{d}P}{\mathrm{d}T} = \frac{1222.77}{-9.051\times10^{-5}}
= -1.351\times10^7\ \mathrm{Pa\,K^{-1}} , \tag{7}$$

$$\frac{\mathrm{d}T}{\mathrm{d}P} = -0.0740\ \mathrm{K\,MPa^{-1}} . \tag{8}$$

The measured pressure-melting rate of ice is about −0.074 K per MPa, so **the
formula reproduces a measured number from two other measured numbers, with no
fitting** — the check to perform before applying equation (5) where nothing is
directly measurable.

The sign is the physics: because water is denser than ice, $\Delta V < 0$ and
pressure *lowers* the melting point. For almost every silicate the liquid is less
dense than the solid, $\Delta V > 0$, and pressure *raises* the melting point.
Glacier sliding on a water film and the depth of the basalt melting region are two
consequences of one sign change.

## 3. The mantle's two great discontinuities

### 3.1 What the transitions are

| Depth (km) | Transition | Approximate $P$ (GPa) | $\gamma = \mathrm{d}P/\mathrm{d}T$ (MPa K⁻¹) | $\Delta V$ |
|---|---|---|---|---|
| ~410 | olivine → wadsleyite (α → β) | 13.5–14 | +2 to +3 | < 0 |
| ~520 | wadsleyite → ringwoodite (β → γ), diffuse | ~17–18 | small | < 0 |
| ~660 | ringwoodite → bridgmanite + periclase | ~23–24 | −2 to −3 | < 0 |

The depths and Clapeyron slopes are adopted from the mineral-physics literature;
the pressures are model values and carry at least a few per cent uncertainty.

### 3.2 Why they are required, and their slopes

Each transition is a densification: $\Delta V < 0$ for all three. By equation (3)
each must therefore occur at some pressure, so their existence is required by
thermodynamics. Their *depths* are where the equilibrium pressure along the actual
geotherm happens to fall — which is why they are at 410 and 660 km rather than at
some arbitrary depths, and why they move when the geotherm moves.

Now apply the sign analysis of equation (5) to the observed slopes:

- **410 km, $\gamma = \mathrm{d}P/\mathrm{d}T > 0$ and $\Delta V < 0$**
  $\Rightarrow \Delta S = \gamma\Delta V < 0$. The denser phase has *lower*
  entropy, which is what a more closely packed, more ordered structure should
  have.
- **660 km, $\gamma < 0$ and $\Delta V < 0$** $\Rightarrow \Delta S > 0$. The
  product assemblage (bridgmanite + periclase) has *higher* entropy than
  ringwoodite, consistent with the decomposition into two phases and the
  reordering of silicon into six-fold coordination.

Neither sign was assumed; both follow from the measured slope and the measured
density change. This is the kind of cross-check that gives confidence in a
high-pressure mineral assemblage.

### 3.3 Depth shifts, and the seismological observable

For a perturbation $\Delta T$ of the geotherm, the boundary moves so as to keep
$P$ on the boundary curve. Since $\mathrm{d}P = \gamma\,\mathrm{d}T$ and
$\mathrm{d}P = \rho g\,\mathrm{d}z$,

$$\boxed{\ \Delta z = \frac{\gamma\,\Delta T}{\rho g}\ } \tag{9}$$

With $\gamma = +2.5$ MPa K⁻¹ at 410 km ($\rho = 3400$ kg m⁻³) and
$\gamma = -2.5$ MPa K⁻¹ at 660 km ($\rho = 4000$ kg m⁻³):

| Boundary | $\gamma$ (MPa K⁻¹) | $\Delta T$ (K) | $\Delta z$ (km) |
|---|---|---|---|
| 410 | +2.5 | +100 | +7.50 |
| 410 | +2.5 | −100 | −7.50 |
| 660 | −2.5 | +100 | −6.37 |
| 660 | −2.5 | −100 | +6.37 |

A uniform-density estimate of the pressure gives 13.67 GPa at 410 km and
25.24 GPa at 660 km, against commonly quoted values near 13.5 and 23.5 GPa. The
estimate overshoots at greater depth because the real density is not constant and
$g$ falls; the point of that calculation is only that the discontinuities sit at
pressures of order 10–25 GPa, as the mineral physics requires.

**Read the signs.** A hot mantle deepens the 410 and shallows the 660; a cold slab
does the opposite. The boundaries move in *opposite* directions, so the transition
zone thickens or thins. That is the seismological observable: a deepened 660 km
boundary above subducting slabs, detected with receiver functions, is *explained*
by the negative Clapeyron slope rather than fitted by it. The prediction came
first and the observation followed, the strongest kind of test.

**But note the magnitude.** A 100 K perturbation moves a boundary by only 6–8 km,
so km-scale depth control is needed and separating the shift from the slab's own
thermal structure takes care. This is a hard measurement, not a routine one.

### 3.4 The seismic signature

A phase transition changes both density and elastic moduli, and therefore both
seismic velocities. The 410 and 660 show up as jumps in $v_p$ and $v_s$ on the
PREM profile, and the velocity contrast is what makes them discontinuities rather
than gradients. The thermodynamic calculation tells you *where* to look; the
seismological observation tells you the size of the velocity jump; and the mineral
physics has to reproduce both from the same assemblage. That three-way closure is
the standard of evidence in the deep Earth.

## 4. Melting, and the solid inner core

### 4.1 The melting curve

For a melting transition with $\Delta V > 0$ and $L > 0$, equation (5) gives
$\mathrm{d}T_m/\mathrm{d}P = \Delta V/\Delta S > 0$: **pressure raises the melting
temperature.** For silicates and metals the slope is a few to a few tens of
kelvin per gigapascal, decreasing with pressure as $\Delta V$ shrinks.

### 4.2 The adiabatic gradient in the outer core

From lesson [02](./02-first-law.md), the isentropic gradient is

$$\frac{\mathrm{d}T}{\mathrm{d}P}\bigg|_{\text{ad}}
= \frac{\alpha T}{\rho c_p} . \tag{10}$$

With nominal core values $\alpha = 10^{-5}$ K⁻¹, $T = 4500$ K,
$\rho = 11\,500$ kg m⁻³ and $c_p = 700$ J kg⁻¹ K⁻¹:

$$\frac{\mathrm{d}T}{\mathrm{d}P}\bigg|_{\text{ad}} = 5.59\
\mathrm{K\,GPa^{-1}} . \tag{11}$$

Across the outer core, $P_{\text{ICB}} - P_{\text{CMB}} = 329 - 135 = 194$ GPa, so
the adiabat rises by **1084 K** from the core–mantle boundary to the inner-core
boundary, reaching 5085 K if the CMB temperature is 4000 K (a nominal value).

### 4.3 The condition for a solid inner core

The outer core is liquid at its top, so there

$$T_{\text{ad}}(P_{\text{CMB}}) > T_m(P_{\text{CMB}}) . \tag{12}$$

The inner core is solid, so at the inner-core boundary the melting curve has
caught up:

$$T_m(P_{\text{ICB}}) = T_{\text{ad}}(P_{\text{ICB}}) . \tag{13}$$

Adopting $T_m(P_{\text{CMB}}) = 3600$ K — below the adiabat, hence liquid at the
top of the outer core — equations (12) and (13) fix the *average* melting slope:

$$s_m = \frac{5084.5 - 3600}{194} = 7.65\ \mathrm{K\,GPa^{-1}}
\quad\text{against}\quad s_{\text{ad}} = 5.59\ \mathrm{K\,GPa^{-1}} . \tag{14}$$

**The melting curve must be steeper than the adiabat by a factor of 1.37.** Then
extend both:

| Location | $P$ (GPa) | $T_{\text{ad}}$ (K) | $T_m$ (K) | $T_m - T_{\text{ad}}$ (K) | State |
|---|---|---|---|---|---|
| CMB | 135 | 4000.0 | 3600.0 | −400.0 | liquid |
| Mid outer core | 232 | 4542.2 | 4342.2 | −200.0 | liquid |
| ICB | 329 | 5084.5 | 5084.5 | 0.0 | boundary |
| Centre | 364 | 5280.1 | 5352.3 | +72.2 | **solid** |

Read the CMB row against the centre row. **The centre of the Earth is at 5280 K
and is solid; the top of the outer core is at 4000 K and is liquid.** The solid
inner core is 1280 K *hotter* than the liquid above it. Pressure, not temperature,
decides the phase, because the melting curve rises faster with pressure than the
adiabat does: descending material is dragged from the liquid side of the melting
curve to the solid side.

**The conclusion is robust; the numbers are not.** Every slope and temperature in
that table is nominal, and the margin at the centre is only 72 K — far smaller
than the uncertainty on any input. What survives is the *ordering*: $s_m >
s_{\text{ad}}$ is required for a solid inner core to exist at all, so the observed
inner core constrains the core's thermal parameters. Light elements lower the
melting point and widen the gap, so its existence is entangled with the outer
core's composition
([12-02/04](../../12-global-geophysics-interior/02-composition-and-mineral-physics/04-core-composition.md)).

### 4.4 Latent heat and the power of inner-core growth

The inner core has radius 1221 km and density ~12 800 kg m⁻³ (nominal), so

$$V = \frac{4}{3}\pi r^3 = 7.625\times10^{18}\ \mathrm{m^3}, \qquad
M = 9.760\times10^{22}\ \mathrm{kg} , \tag{15}$$

and with $L = 2.5\times10^5$ J kg⁻¹ (nominal for iron at core conditions) the
cumulative latent heat released to date is

$$Q = LM = 2.44\times10^{28}\ \mathrm{J}, \qquad
\Delta S = \frac{Q}{T} = \frac{2.44\times10^{28}}{5200}
= 4.69\times10^{24}\ \mathrm{J\,K^{-1}} . \tag{16}$$

The cumulative figure says nothing about present-day power. For that, adopt a
growth rate of 1 mm yr⁻¹ (nominal and poorly constrained):

$$\frac{\mathrm{d}M}{\mathrm{d}t} = 4\pi r^2\rho v = 7.599\times10^{6}\
\mathrm{kg\,s^{-1}} , \qquad
P = L\frac{\mathrm{d}M}{\mathrm{d}t} = 1.90\ \mathrm{TW} . \tag{17}$$

A couple of terawatts is a real contribution to the core's energy budget and a
significant term in the planet's budget of lesson [06](./06-geotherms.md) §3.4.
The same freezing front rejects light elements into the outer core, and the
resulting compositional buoyancy is one of the drivers of the geodynamo.

### 4.5 Melting in the mantle, and why upwelling melts

The mantle is solid because its geotherm lies below the solidus. Melting happens
where the two cross, and the reason upwelling material crosses is a *slope*
argument:

- lithostatic gradient: $\mathrm{d}P/\mathrm{d}z = \rho g = 0.0324$ GPa km⁻¹;
- mantle adiabat: 0.4 K km⁻¹;
- dry peridotite solidus: 110–135 K GPa⁻¹, i.e. **3.6–4.4 K km⁻¹**.

The solidus rises with depth about ten times faster than the adiabat does. So if
the adiabat is above the solidus at one depth it is above it at all greater depths,
and a rising parcel (following the adiabat) crosses the solidus once, at a depth
fixed by the potential temperature and the solidus intercept. For melting to begin
at the observed 60–70 km beneath a normal mid-ocean ridge, with a potential
temperature of about 1573 K, the solidus must pass through

$$T_s(65\ \mathrm{km}) = 1573 + 0.4\times65 = 1599\ \mathrm{K}
\quad\text{at}\quad P = 0.0324\times65 = 2.11\ \mathrm{GPa} . \tag{18}$$

That is where petrological models place it, and the agreement is a genuine
consistency check rather than a fit: the inference used only the adiabat slope,
the lithostatic gradient and the observed depth of first melting.

**Decompression melting is a phase-equilibrium consequence, not a pressure effect
on temperature.** The rising parcel's own temperature *falls* slightly, but the
solidus falls faster, so the parcel becomes super-solidus. This is the mechanism
behind mid-ocean-ridge basalt, and why melt production correlates with spreading
rate and potential temperature rather than with depth.

## 5. Physical interpretation

**A phase boundary is a locus of equal Gibbs energy, and nothing more.** Its
slope is fixed by two entropy-like and volume-like quantities; its position is
fixed by the geotherm. That is why the same boundary can be shallow in a hot
region and deep in a cold one, and why the depth of a discontinuity is
simultaneously a mineral-physics and a thermal measurement.

**Pressure and temperature compete, and pressure usually wins at depth.** In the
mantle, a 100 K temperature change moves a boundary by 6–8 km, whereas the
pressure change over that distance is ~0.3 GPa. The mantle's mineralogy is
therefore primarily a function of depth, with temperature as a perturbation — the
opposite of the situation in the crust, where temperature dominates.

**The inner core is the clearest demonstration of the whole lesson.** Temperature
alone would melt it; pressure keeps it solid, because the melting point depends on
pressure through equation (5).

**Entropy, not just energy, decides which phase appears.** Two structures with
nearly the same energy but different entropy will swap stability as temperature
changes, and that is the difference between the positive slope at 410 km and the
negative one at 660 km.

## 6. Assumptions and regime of validity

| Approximation | Statement | What breaks outside it |
|---|---|---|
| Local equilibrium | Every point is at its equilibrium assemblage | Fast tectonic exhumation and metastable assemblages: diamond at the surface, aragonite in a cold slab |
| Single-component transition | Equation (5) applies with one $L$ | Multicomponent systems melt over an interval; use the phase rule and the lever rule |
| Clapeyron slope is constant | Linear depth shifts | Slopes vary with $P$ and $T$; curved boundaries need the full $\Delta S$, $\Delta V$ |
| $\Delta V$ and $\Delta S$ known | Equation (5) is predictive | At core pressures both are uncertain; the slope is inferred from the observed boundary, not predicted |
| Two phases only at a boundary | Sharp discontinuity | The 520 km transition is diffuse because its slope is near zero and the chemistry smears it |
| No chemical diffusion | Equilibrium maintained | Diffusion is slow at mantle temperatures in solid phases; disequilibrium is real over short times |
| Adiabatic core geotherm | Equation (11) | Requires efficient convection; a stably stratified layer would have a different gradient |
| Melting curve linear in the core | The 5084 K figure | Both $T_m$ and the adiabat curve; the true ICB temperature is model-dependent |

## 7. Units and dimensional analysis

- $G$, $\mu$: J mol⁻¹ (or J kg⁻¹ in the specific form used here for $L$).
- $\mathrm{d}P/\mathrm{d}T$: Pa K⁻¹. In MPa K⁻¹ it is quoted as 2–3 for the 410.
  The demo prints the ice value as $-1.351\times10^7$ Pa K⁻¹ =
  $-13.51$ MPa K⁻¹ and the equivalent $\mathrm{d}T/\mathrm{d}P$ as
  $-0.074$ K MPa⁻¹; quoting the first as "the slope of the ice melting curve"
  without inverting it is a common source of a factor of 200 error.
- Equation (9): $\gamma\Delta T/(\rho g)$:
  $\mathrm{Pa\,K^{-1}}\cdot\mathrm{K}/(\mathrm{kg\,m^{-3}}\cdot\mathrm{m\,s^{-2}})
  = \mathrm{m}$ ✓.
- Equation (10): $\alpha T/\rho c_p$:
  $\mathrm{K^{-1}}\cdot\mathrm{K}/(\mathrm{kg\,m^{-3}}\cdot
  \mathrm{J\,kg^{-1}K^{-1}}) = \mathrm{m^3\,J^{-1}} = \mathrm{Pa^{-1}} =
  \mathrm{K\,Pa^{-1}}$ ✓ — the same units as the ice slope above, so equations
  (5) and (10) are directly comparable, which is exactly what §4.3 does.
- Equation (17): $L\,\mathrm{d}M/\mathrm{d}t$:
  $\mathrm{J\,kg^{-1}}\cdot\mathrm{kg\,s^{-1}} = \mathrm{W}$ ✓.
- **Useful anchors**: Clapeyron slopes in the mantle are a few MPa K⁻¹ (not GPa
  K⁻¹); a 100 K thermal anomaly moves a boundary by ~7 km; the core adiabat is
  ~5.6 K GPa⁻¹; a melting curve in the core is ~8 K GPa⁻¹. Any computed
  boundary shift of 700 km or any core adiabat of 0.005 K GPa⁻¹ is a unit error.

## 8. Python demonstration

[`code/phase_equilibria_demo.py`](./code/phase_equilibria_demo.py) checks
Clausius–Clapeyron against ice, computes pressure estimates and boundary shifts,
computes the core adiabat, finds the melting slope required by a solid inner core,
and computes the latent heat of inner-core growth. Observed output:

```text
  ice: L = 3.340e+05 J/kg, T = 273.15 K, rho_ice = 917, rho_water = 1000 kg/m3
  dV = 1/1000 - 1/917 = -9.051254e-05 m3/kg  (NEGATIVE: water is denser)
  dS = L/T = 1222.7714 J kg^-1 K^-1
  dP/dT = -1.350941e+07 Pa/K = -13.5094 MPa/K
  dT/dP = -0.074022 K/MPa
```

```text
  410 km   rho = 3400 kg/m3 -> P = 13.67 GPa (commonly quoted near 13.5 GPa)
  660 km   rho = 3900 kg/m3 -> P = 25.24 GPa (commonly quoted near 23.5 GPa)

boundary      gamma (MPa/K)  rho (kg/m3)   dT (K)   dz (km)
410                     2.5         3400      100      7.50
410                     2.5         3400     -100     -7.50
660                    -2.5         4000      100     -6.37
660                    -2.5         4000     -100      6.37
```

```text
  dT/dP = 5.5901e-09 K/Pa = 5.590 K/GPa
  dP across the outer core = 194 GPa
  adiabatic temperature rise CMB -> ICB = 1084.5 K
  with an adopted T_CMB = 4000 K, the adiabat reaches
  5084.5 K at the inner-core boundary
```

```text
    s_m = (5084.5 - 3600) / 194 GPa = 7.652 K/GPa
  against the computed adiabatic slope 5.590 K/GPa.
  The melting curve is steeper by a factor 1.369.

location         P (GPa)   T_ad (K)    T_m (K)  T_m - T_ad    state
CMB                135.0     4000.0     3600.0      -400.0   liquid
mid outer core     232.0     4542.2     4342.2      -200.0   liquid
ICB                329.0     5084.5     5084.5         0.0 BOUNDARY
centre             364.0     5280.1     5352.3        72.2    solid

  core is at 5280 K and is SOLID; the outermost outer core
  is at 4000 K and is LIQUID — hotter by 1280 K
  and solid all the same.
```

```text
  Volume = 7.6249e+18 m3,  Mass = 9.7599e+22 kg
  Total latent heat released to date = L M = 2.4400e+28 J
  Entropy = Q/T with T ~ 5200 K -> 4.6923e+24 J/K

  For the present-day power, adopt a growth rate of 1 mm/yr:
    v = 1 mm/yr = 3.1688e-11 m/s (nominal, poorly constrained)
    dM/dt = 4 pi r^2 rho v = 7.5988e+06 kg/s
    P = L dM/dt = 1.8997e+12 W = 1.90 TW
```

### What to observe

| Observation | Consequence |
|---|---|
| The ice slope comes out at −0.074 K MPa⁻¹ against a measured −0.074 | Clausius–Clapeyron is verified against a real measurement before use at depth |
| The slope is negative only because $\Delta V < 0$ | The sign of the density change is the whole physics |
| 410 shifts +7.50 km and 660 shifts −6.37 km for the same +100 K | Opposite Clapeyron slopes give opposite shifts and a changing transition-zone thickness |
| Core adiabat 5.590 against a required melting slope 7.652 K GPa⁻¹ | A solid inner core requires $s_m > s_{\text{ad}}$, a factor of 1.37 |
| ICB row is the exact meeting point | Equation (13) was used to *derive* the slope, and the table confirms it |
| Centre 5280 K solid against CMB 4000 K liquid | Pressure, not temperature, decides the phase |
| Margin at the centre is 72 K | Robust conclusion, fragile numbers — the honest summary |
| Latent power 1.90 TW at 1 mm yr⁻¹ growth | A measurable contribution to the core's budget |

> **Breaking exercise.** Set the adiabatic slope in the core to 6.5 K GPa⁻¹ (by
> raising $\alpha$ to 1.16 × 10⁻⁵ K⁻¹) while keeping $T_m(\text{CMB}) = 3600$ K,
> and predict, before running, whether the required melting slope rises or falls
> and whether the crossing depth moves up or down. Then explain why a *larger*
> adiabatic gradient makes a solid inner core *harder* to achieve.

## 9. Common mistakes

1. **Treating a phase boundary as a function of depth.** It is a function of
   pressure and temperature; the depth is *derived* from the geotherm. A boundary
   that does not move when the geotherm changes is not an equilibrium boundary.
2. **Getting the sign of $\mathrm{d}T/\mathrm{d}P$ from intuition rather than
   from $\Delta V$.** The sign is decided by the volume change and nothing else;
   ice and silicates differ because $\Delta V$ differs.
3. **Confusing $\mathrm{d}P/\mathrm{d}T$ with $\mathrm{d}T/\mathrm{d}P$.** The ice
   melting curve is $-13.5$ MPa K⁻¹ as a pressure-per-temperature slope and
   $-0.074$ K MPa⁻¹ as a temperature-per-pressure slope; quoting the wrong one is a
   factor of 180 error.
4. **Assuming the 410 and 660 shift the same way with temperature.** Their
   Clapeyron slopes have opposite signs, so they move in opposite directions and
   the transition zone thickens or thins rather than shifting bodily.
5. **Applying the melting curve to the mantle as if it were the solidus.** A
   multicomponent silicate melts over an interval; the solidus, the liquidus and
   the melt fraction at a given $P$ and $T$ are three different statements.
6. **Assuming the inner core is solid because it is cold.** It is the hottest part
   of the Earth. It is solid because $\mathrm{d}T_m/\mathrm{d}P > \mathrm{d}T/
   \mathrm{d}P|_{\text{ad}}$, so pressure wins at depth.
7. **Quoting a core temperature or Clapeyron slope as a measurement.** At core
   conditions these are all model-dependent, with factor-of-two uncertainties;
   what is robust is the sign and the ordering of the slopes.
8. **Ignoring metastability.** Equilibrium requires time to be attained; a fast,
   cold slab can carry olivine below 410 km. The thermodynamic prediction is what
   *would* happen at equilibrium, not what a fast process must produce.
9. **Using $\rho g z$ with a constant $\rho$ to place a boundary.** It is a useful
   estimate to within 10 per cent, not a substitute for an Earth model.
10. **Assuming a discontinuity must be sharp.** Sharpness is a statement about the
    Clapeyron slope and about kinetics; the near-zero slope of the 520 km feature
    is why it is diffuse.

## 10. Real-world applications

- **Seismic imaging of the transition zone.** The depth and sharpness of the 410
  and 660 constrain mantle temperature and composition; the Clapeyron slopes of
  §3.3 convert a depth anomaly into a temperature anomaly
  ([12-01/03](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/03-upper-mantle-discontinuities.md)).
- **Slab thermal structure.** A cold slab's phase boundaries are displaced from
  the ambient mantle's, and the displacement is a thermometer for the slab
  interior.
- **Mantle melting and basalt petrogenesis.** Melt fraction and the depth of the
  melting column follow from the slopes in §4.5 and explain the major-element
  chemistry of mid-ocean-ridge basalt.
- **Core composition and the geodynamo.** The inner-core boundary temperature, the
  light-element content and the power available to the dynamo are all linked
  through equation (13)
  ([12-02/04](../../12-global-geophysics-interior/02-composition-and-mineral-physics/04-core-composition.md)).
- **Inner-core structure and history.** The age of the inner core, its growth rate
  and its seismic anisotropy are constraints on the thermal history of the core
  ([12-01/06](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/06-outer-and-inner-core.md)).
- **Metamorphic belts.** The same Gibbs-energy machinery gives the
  pressure–temperature path of a metamorphic rock, the standard record of
  tectonic history.
- **CO₂ and hydrogen storage.** Phase equilibria in H₂O–CO₂–hydrocarbon systems at
  reservoir conditions decide what phases are present (§1).

## 11. Further reading

- **Anderson, D. L. *Theory of the Earth* (Blackwell, 1989).** The thermodynamic
  foundations of mantle mineralogy and the PREM thermal model. Level: graduate.
- **Poirier, J.-P. *Introduction to the Physics of the Earth's Interior*
  (2nd ed., Cambridge University Press, 2000).** Melting, the Lindemann and
  Kraut–Kennedy laws, and the thermal state of the core. Level: graduate.
- **Jackson, I. (ed.) *The Earth's Mantle: Composition, Structure and Evolution*
  (Cambridge University Press, 1998).** Phase relations, the 410 and 660, and the
  mineral physics behind §3. Level: graduate.
- **Navrotsky, A. *Physics and Chemistry of Earth Materials* (Cambridge University
  Press).** The thermodynamics of solid-state transitions, with the derivations of
  equation (5) in a mineralogical setting. Level: advanced.
- **Ringwood, A. E. *Composition and Petrology of the Earth's Mantle*
  (McGraw-Hill, 1975).** The original argument that the mantle's olivine-rich
  mineralogy requires the observed discontinuities; a primary source.
  Level: doctoral.
- **Philpotts, A. R., & Ague, J. J. *Principles of Igneous and Metamorphic
  Petrology* (2nd ed., Cambridge University Press, 2009).** Solidus and liquidus
  relations, the phase rule, and the petrology of melting. Level: intermediate.
- **Callen, H. B. *Thermodynamics and an Introduction to Thermostatistics*
  (2nd ed., Wiley).** The Gibbs energy, the phase rule and coexistence, derived
  from first principles. Level: intermediate to advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [02 First Law, Work and Energy Balances](./02-first-law.md) — the adiabatic
  gradient that equation (10) is an instance of.
- [03 Second Law, Entropy and Irreversibility](./03-second-law.md) — the entropy
  in $\Delta S$, and why a phase transition has a sign.
- [06 Geotherms, Heat Flow and the Earth's Thermal Budget](./06-geotherms.md) —
  the geotherm these boundaries sit on, and the latent heat in the budget.
- [02-11-02 Equations of State and High-Pressure Mineral Physics](../11-physics-of-earths-interior-and-atmosphere/02-equations-of-state.md)
  — the $P$–$V$–$T$ relations that supply $\Delta V$ at depth.
- [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)
  — the seismic observations of the 410, the 660 and the inner core.
- [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) — the
  dynamic consequences of a variable transition-zone thickness.

Exercises:
[`exercises/07-phase-equilibria-exercises.md`](./exercises/07-phase-equilibria-exercises.md)
and
[`exercises/07-phase-equilibria-solutions.md`](./exercises/07-phase-equilibria-solutions.md).

## Self-assessment checklist

- [ ] I can state the equilibrium condition in terms of Gibbs energy and explain
      why pressure favours the denser phase. (§1.1, §1.2)
- [ ] I can derive Clausius–Clapeyron and check it against the measured melting
      point of ice. (§2, §2.1)
- [ ] I can deduce the sign of $\Delta S$ for a mantle transition from the
      observed Clapeyron slope and the density change. (§3.2)
- [ ] I can explain why the 410 and 660 km discontinuities are thermodynamically
      required, not merely permitted. (§3.2)
- [ ] I can compute a boundary's depth shift for a temperature anomaly and state
      the sign for each boundary. (§3.3)
- [ ] I can compute the adiabatic gradient in the core and the temperature rise
      across the outer core. (§4.2)
- [ ] I can derive the melting slope required for a solid inner core and show
      that it exceeds the adiabatic slope. (§4.3)
- [ ] I can explain how the inner core can be hotter than the outer core and
      still solid. (§4.3, §5)
- [ ] I can compute the latent heat, entropy and present-day power of inner-core
      growth. (§4.4)
- [ ] I can argue, from slopes, why decompression melting must begin at a single
      depth. (§4.5)
