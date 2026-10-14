---
id: 13-02-03
title: "Mantle Plumes, Hotspots and Large Igneous Provinces"
level: doctoral
prereqs: ["13-02-01", "12-01-04", "02-05-07"]
tags: [geodynamics, tectonophysics, mantle-plumes, hotspots, large-igneous-provinces, melt-generation]
---

# Mantle Plumes, Hotspots and Large Igneous Provinces

> All models and data in this module are **SYNTHETIC**. The plume parameters, the
> buoyancy flux, the solidus and the hotspot track below are chosen teaching
> models, and every number quoted here is printed by
> `code/mantle_plumes_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the thermal buoyancy of a plume head from an excess potential
   temperature and **derive** its Stokes rise speed, including the difference
   between a rigid and a low-viscosity sphere.
2. **Derive** the conduit velocity from cylindrical Poiseuille flow and **compute**
   the volume and buoyancy fluxes, stating the scaling with conduit viscosity.
3. **Invert** a buoyancy flux for an excess temperature or a volume flux, and
   **state** which of the two is better constrained.
4. **Quantify** the heat carried by a plume relative to the mantle heat loss and
   **conclude** what fraction of the budget hotspot volcanism can supply.
5. **Apply** the Rayleigh-number criterion to a *blob* rather than a layer, and
   **explain** why the incubation question is about buoyancy sources, not
   stability.
6. **Compute** a melt column from synthetic phase relations and **convert** it to
   an igneous crustal thickness, stating the productivity assumption.
7. **Read** a hotspot track for plate speed and **state** the testable
   approximation that the analysis rests on.

## Prerequisites

- [13-02-01 Rayleigh-Benard Convection Applied to the Mantle](01-rayleigh-benard-mantle.md) —
  the Rayleigh number criterion reused here for a blob.
- [12-01-04 Lower-Mantle Heterogeneity and LLSVPs](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/04-lower-mantle-heterogeneity.md) —
  the deep structures often invoked as plume sources.
- [02-05-07 Thermodynamic Phase Equilibria and Mantle Mineralogy](../../02-physics/05-thermodynamics/07-phase-equilibria.md) —
  where solidus and liquidus relations come from.
- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](../01-geodynamic-principles/02-rheology-of-earth.md) —
  why the conduit's viscosity, not the mantle's, sets the flux.

## 1. Intuition: a narrow thing in a wide fluid

The mantle convects in broad rolls
([13-02-02](02-convection-numerical.md)), yet some of the most conspicuous
volcanism on Earth is *narrow*: chains of islands a few hundred kilometres wide,
a few thousand kilometres long, apparently fixed with respect to one another
while the plates move over them. A plume theory explains the observation with one
structure — a narrow, hot, buoyant upwelling — and the theory's credibility rests
entirely on whether the numbers work.

Two numbers decide most of the argument.

- **The buoyancy anomaly.** An excess potential temperature of 200 K makes mantle
  rock about 0.6% less dense. Small — but $L^{3}$ beats $\eta\kappa$ in the
  Rayleigh number, so a hot blob a few hundred kilometres across is unstable by
  orders of magnitude.
- **The conduit flux.** The volume flux through a narrow pipe scales as
  $a^{4}$ and as $1/\eta_{\text{conduit}}$. Because the conduit's viscosity is
  itself lowered by the same temperature anomaly that drives the flow, the flux
  is a strong positive feedback — and an extremely uncertain number. Getting
  $\eta_{\text{conduit}}$ wrong by a factor of 10 moves the heat carried per
  plume by a factor of 10, which is the difference between hotspots being
  important and being negligible in the global heat budget.

That last sentence is the intellectual honesty point of the lesson: the popular
narrative ("plumes carry a substantial fraction of the mantle's heat") and the
measured budget in §4 of the demonstration point in different directions, and the
resolution is a thermodynamically motivated preference for a larger conduit
viscosity rather than a measurement.

## 2. The buoyancy of a hot blob

### 2.1 Density anomaly

At constant pressure, an excess potential temperature $\Delta T$ changes density
by

$$\Delta\rho = \rho_0\,\alpha\,\Delta T .$$

With SYNTHETIC $\rho_0 = 3300\ \mathrm{kg\,m^{-3}}$,
$\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$ and $\Delta T = 200$ K:

$$\Delta\rho = 19.80\ \mathrm{kg\,m^{-3}} = 0.60\%\ \text{of }\rho_0 .$$

**Six parts in a thousand.** Everything a plume does — rising, melting,
generating a swell — is driven by that number, which is why plume dynamics is
dominated by the same thermally induced buoyancy as every other process in this
module, and why an error in $\alpha$ or in $\Delta T$ propagates directly.

### 2.2 Rise speed

A spherical blob of radius $a$ in a fluid of viscosity $\eta$ rises (for inertia
negligible, which §[13-01-01 §4](../01-geodynamic-principles/01-momentum-mass-energy.md)
established with $Re\sim10^{-20}$) at

$$u = \frac{2\Delta\rho\,g\,a^{2}}{9\eta}\quad\text{(rigid sphere)},
\qquad
u = \frac{2\Delta\rho\,g\,a^{2}}{3\eta}\quad\text{(zero internal viscosity)} .$$

The factor of three is the Hadamard–Rybczynski correction: a blob whose interior
can circulate feels less drag. Measured with $\eta = 10^{21}$ Pa s:

| head radius (km) | rigid sphere (m/yr) | low-viscosity sphere (m/yr) | rise time over 2900 km (Myr) |
|---|---|---|---|
| 150 | 0.031 | 0.092 | 94.6 |
| 250 | 0.085 | 0.255 | 34.1 |
| 500 | 0.341 | 1.022 | 8.5 |

A 250 km head rises at $0.085\ \mathrm{m\,yr^{-1}} = 85\ \mathrm{mm\,yr^{-1}}$,
comparable with plate speeds: plume rise and plate motion are the same order of
magnitude because both are Stokes velocities driven by a few-tens-of-kg m$^{-3}$
density anomaly. That coincidence is not physics — it is two ratios of
$\Delta\rho g L^{2}/\eta$ landing near each other — but it does explain why a
mantle-plume and a plate-motion explanation for hotspot tracks cannot be
distinguished by speed alone.

## 3. The conduit: Poiseuille flow and buoyancy flux

### 3.1 Velocity and flux

A buoyant fluid of density anomaly $\Delta\rho$ in a vertical cylindrical conduit
of radius $a$ and viscosity $\eta_c$, driven by its own buoyancy, has the
Poiseuille profile

$$u(r) = \frac{\Delta\rho\,g}{4\eta_c}\left(a^{2} - r^{2}\right),
\qquad
u_{\max} = \frac{\Delta\rho\,g\,a^{2}}{4\eta_c},
\qquad
Q = \pi a^{2}\langle u\rangle
= \frac{\pi\,\Delta\rho\,g\,a^{4}}{8\eta_c} .$$

The fourth power of the radius and the first power of $1/\eta_c$ are the whole
story of plume flux: narrow conduits are not merely inefficient, they are
dramatically inefficient.

### 3.2 Measured values

With $a = 50$ km:

| $\eta_c$ (Pa s) | $u$ (m/s) | $u$ (m/yr) | $Q$ (m$^{3}$/s) | $B = \Delta\rho g Q$ (kg/s) |
|---|---|---|---|---|
| $10^{18}$ | $6.07\times10^{-8}$ | 1.915 | $4.767\times10^{2}$ | $9.260\times10^{4}$ |
| $10^{19}$ | $6.07\times10^{-9}$ | 0.192 | $4.767\times10^{1}$ | $9.260\times10^{3}$ |
| $10^{20}$ | $6.07\times10^{-10}$ | 0.019 | $4.767$ | $9.260\times10^{2}$ |

The **buoyancy flux** $B = \Delta\rho\,g\,Q$ (kg s$^{-1}$) is the observable: a
hotspot swell records the dynamic support that the flux provides, and $B$ can be
inverted for either $Q$ (given $\Delta\rho$) or $\Delta\rho$ (given $Q$). The
inseparability of the two is a real non-uniqueness of the method, and it is not
removed by any amount of swell geometry: a bigger conduit with a smaller
temperature anomaly looks like a smaller conduit with a bigger one.

## 4. Heat transport: the budget that constrains the story

The heat carried by a conduit is the product of the mass flux and the excess
enthalpy:

$$q_{\text{plume}} = \rho_0 c_p \Delta T\,Q .$$

Measured with $\rho_0 c_p\Delta T = (3300)(1250)(200) = 8.25\times10^{8}$
J m$^{-3}$:

| $\eta_c$ (Pa s) | $Q$ (m$^{3}$/s) | heat per plume (TW) | plumes needed for 44.4 TW |
|---|---|---|---|
| $10^{18}$ | $4.767\times10^{2}$ | 0.3933 | 113 |
| $10^{19}$ | $4.767\times10^{1}$ | 0.0393 | 1129 |

The mantle loses 44.4 TW in this module's SYNTHETIC budget
([13-01-01 §9](../01-geodynamic-principles/01-momentum-mass-energy.md)). Carrying
all of it through conduits of this size would take between 113 and 1129 plumes —
against a few tens of recognised hotspots. **Hotspot volcanism is a minor term in
the global heat budget**, and the observation that the Earth's surface has
thousands of kilometres of plate boundary and a few dozen hotspots is exactly
what the numbers say.

The honest caveats, which are also the escape routes used in the literature:

- $B$ is not measured for most hotspots; it is inferred from swell geometry, with
  a large uncertainty and a model dependence on how the swell is compensated.
- A larger conduit radius (which the model fixes at 50 km) increases the flux as
  $a^{4}$; a 100 km conduit would quadruple the flux.
- Plume heads, not steady conduits, may deliver the bulk of the heat in pulses;
  the time-averaged budget of a pulsating plume is not the steady flux computed
  here.

What the numbers *do* establish is the order of magnitude, and that order of
magnitude says plumes are a modulator of the plate-scale flow, not its equal.

## 5. Incubation: the same Rayleigh number for a blob

The layer criterion of [13-02-01](01-rayleigh-benard-mantle.md) generalises by
replacing $\alpha\Delta T$ with $\Delta\rho/\rho_0$ and $d$ with a blob size $L$:

$$Ra_{\text{blob}} = \frac{\Delta\rho\,g\,L^{3}}{\eta\kappa} .$$

Measured with $\eta = 10^{21}$ Pa s and $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$:

| $L$ (km) | $\Delta\rho$ (kg m$^{-3}$) | $Ra_{\text{blob}}$ | $Ra_{\text{blob}}/Ra_c$ |
|---|---|---|---|
| 500 | 19.80 | $2.428\times10^{4}$ | 36.9 |
| 1000 | 19.80 | $1.942\times10^{5}$ | 295 |
| 1000 | 30.00 | $2.943\times10^{5}$ | 448 |

A few hundred kilometres of 0.6% density anomaly is unstable by a factor of 37;
a thousand kilometres by a factor of 300. So **the stability question is not
interesting** — the barriers to plume formation are not dynamical instability but
(a) whether a buoyancy source exists at the base of the mantle and (b) whether the
anomaly survives long enough to rise. On (b), the comparison is favourable to
thermal plumes: at $L = 500$ km the diffusive time is
$L^{2}/\kappa = 2.5\times10^{17}\ \mathrm{s} = 7.9\ \mathrm{Gyr}$, while the rise
time from §2.2 is 34 Myr. The Péclet number of the blob,

$$Pe = \frac{uL}{\kappa} = \frac{t_{\text{diff}}}{t_{\text{adv}}}
\approx 1.4\times10^{3},$$

says that advection beats conduction by three orders of magnitude, so a thermal
anomaly of plume scale is not erased during ascent. What *is* short at small scale
is the conduction time for the *conduit*: a 50 km conduit loses its anomaly on
$(5\times10^{4})^{2}/\kappa = 79$ Myr, comparable to the time between plume
pulses, which is why conduits must be continuously fed from below rather than
being one-off structures. The quantitative case for compositional buoyancy is
therefore about the *source* and the *conduit*, not about the head.

## 6. Melting: from excess temperature to igneous crust

### 6.1 A synthetic melt column

Take SYNTHETIC linear phase relations,

$$T_{\text{sol}}(z) = 1350 + 3z\ \mathrm{K}, \quad
T_{\text{liq}}(z) = T_{\text{sol}} + 400\ \mathrm{K}, \quad (z \text{ in km}),$$

and a decompressing plume adiabat $T_{\text{plume}}(z) = 1600 - 0.5z$ K. The melt
fraction is the leverage rule

$$F(z) = \mathrm{clamp}\!\left(
\frac{T_{\text{plume}} - T_{\text{sol}}}{T_{\text{liq}} - T_{\text{sol}}},\,
0,\,1\right).$$

Measured:

| $z$ (km) | 0 | 20 | 40 | 60 | 80 | 100 |
|---|---|---|---|---|---|---|
| $T_{\text{plume}}$ (K) | 1600 | 1590 | 1580 | 1570 | 1560 | 1550 |
| $T_{\text{sol}}$ (K) | 1350 | 1410 | 1470 | 1530 | 1590 | 1650 |
| $F$ | 0.625 | 0.450 | 0.275 | 0.100 | 0.000 | 0.000 |

The melting column is 75 km deep with mean melt fraction 0.319. Note the structure
in one sentence: melting is deepest and most intense at shallow depth, and it
stops where the rising adiabat meets the solidus — a "solidus crossing" that
*shallows* as the excess temperature grows. Raise $\Delta T$ and both the depth
extent and the mean $F$ increase, which is why excess temperature is the key
parameter in the plume-melting literature.

### 6.2 Igneous crustal thickness

If melt is extracted and emplaced with a productivity factor $f$ (the fraction of
melt that becomes crust, and the amount of mantle that melted), the igneous
crustal thickness is $h_{\text{crust}} = f\,F_{\text{mean}}\,h_{\text{melt}}$:

| productivity | crustal thickness |
|---|---|
| 0.5 | 12.0 km |
| 1.0 | 23.9 km |

That range, 12–24 km of igneous crust, is the right order for the thickest
oceanic plateaus, and it is worth stating precisely what the calculation does and
does not show. It shows that a 200 K anomaly with a sensible phase diagram
produces plateau-scale crust. It does *not* invert an observed crustal thickness
for a temperature, because the productivity factor and the pre-existing lithosphere
thickness both enter at the same order — the classic non-uniqueness of igneous
petrology.

## 7. Hotspot tracks: kinematics and one testable assumption

If a hotspot is fixed with respect to the mantle and a plate moves over it, the
track records the plate's motion. Measured for a SYNTHETIC 3000 km track whose
oldest volcano is 60 Myr old:

$$v = \frac{3000\ \mathrm{km}}{60\ \mathrm{Myr}}
= 1.5844\times10^{-9}\ \mathrm{m\,s^{-1}} = 50.0\ \mathrm{mm\,yr^{-1}},$$

| distance (km) | 0 | 750 | 1500 | 2250 | 3000 |
|---|---|---|---|---|---|
| age (Myr) | 0 | 15 | 30 | 45 | 60 |

A change in plate direction makes a bend, and the bend angle equals the change in
plate velocity direction *only if the hotspot is fixed*. That assumption is
testable: a hotspot moving even a few mm yr$^{-1}$ in the mantle frame visibly
bends a track whose age progression should be simply linear. The physics is
therefore not "tracks record plate motion" but "tracks record the *difference*
between plate and hotspot motion", and the second term is the one that must be
argued rather than assumed. Because the plume's own rise speed from §2.2 is
comparable to plate speeds, that argument is not trivial.

## 8. Sensitivity and assumptions

A Monte Carlo over SYNTHETIC uncertainties — 15% in $\Delta T$, 10% in the head
radius, and a factor of $10^{0.5}$ (1σ) in viscosity — gives the rise speed of a
250 km head as

$$u = 0.084\ \mathrm{m\,yr^{-1}}
\quad {}^{+0.182}_{-0.058}\ (1\sigma) .$$

Viscosity dominates the budget: because $u\propto1/\eta$ and $\eta$ is log-normally
uncertain over half a decade, the rise-speed distribution is nearly log-normal
with an order-of-magnitude spread. **Plume speeds are far less constrained than
hotspot-track geometry**, which is the practical reason plume studies lean on
kinematics (tracks, plate reconstructions) rather than dynamics (speeds,
fluxes).

| assumption | where it fails |
|---|---|
| constant mantle viscosity | the conduit viscosity differs from the ambient by decades |
| axisymmetric steady conduit | pulsating conduits, tilted conduits, conduit drift |
| thermal buoyancy only | chemically dense or light material changes the sign |
| linear solidus/liquidus | real phase relations are curved and composition-dependent |
| melt extraction at $F_{\text{mean}}$ | melt retention, reactive porous flow, melt focusing |
| fixed hotspot | hotspot motion of a few mm/yr is enough to matter |
| no lithospheric interaction | a thick lid suppresses melting and deflects the flow |

## 9. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| density anomaly | $\Delta\rho$ | kg m$^{-3}$ | $\rho\alpha\Delta T$ |
| rise speed | $u$ | m s$^{-1}$ | $\Delta\rho g a^{2}/\eta$ |
| volume flux | $Q$ | m$^{3}$ s$^{-1}$ | $\pi a^{4}\Delta\rho g/(8\eta_c)$ |
| buoyancy flux | $B$ | kg s$^{-1}$ | $\Delta\rho g Q$ |
| heat flux | $q$ | W | $\rho c_p\Delta T Q$ |
| melt fraction | $F$ | — | temperature leverage |
| crustal thickness | $h$ | m | $f\,F\,h_{\text{melt}}$ |

A scaling check worth doing once: $Q\propto a^{4}/\eta_c$ means doubling the
conduit radius multiplies the flux by 16 while multiplying the cross-sectional
area by 4 — the Poiseuille profile's excess over plug flow. If a plume calculation
treats $Q$ as proportional to area, it is wrong by $a^{2}$.

## 10. The demonstration

`code/mantle_plumes_demo.py` prints every number above:

```bash
cd 13-geodynamics-tectonics/02-mantle-convection/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mantle_plumes_demo.py
```

It computes the head buoyancy and rise speeds for three sizes and two internal-
viscosity limits; the conduit velocity, volume flux and buoyancy flux for three
conduit viscosities; the plume heat flux against the mantle budget; the blob
Rayleigh numbers; the melt column and igneous crustal thickness; the hotspot-track
kinematics; and a Monte Carlo sensitivity of the rise speed. Fixed seed,
print-only, no network, exits 0.

Exercises:
[`exercises/03-mantle-plumes-exercises.md`](exercises/03-mantle-plumes-exercises.md)
and
[`exercises/03-mantle-plumes-solutions.md`](exercises/03-mantle-plumes-solutions.md).

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC plume has $\Delta T = 250$ K, $\rho_0 = 3300\ \mathrm{kg\,m^{-3}}$,
> $\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$, a conduit of radius 40 km with
> $\eta_c = 3\times10^{19}$ Pa s, and $\eta_{\text{mantle}} = 10^{21}$ Pa s.
> **(a)** Compute $\Delta\rho$, the conduit volume flux and the buoyancy flux.
> **(b)** Compute the heat carried per plume and the number of such plumes needed
> for a 44 TW loss. **(c)** A colleague infers an excess temperature twice as
> large from the same buoyancy flux. What has to be assumed about the conduit, and
> by what factor does $Q$ change? **(d)** State one observation that would
> distinguish a deep mantle plume from a shallow, lithosphere-controlled origin,
> and the measurement that would test it.

A worked version appears in the
[solutions](exercises/03-mantle-plumes-solutions.md).

## Common pitfalls

1. **Confusing buoyancy flux with heat flux.** $B = \Delta\rho g Q$ has units of
   kg s$^{-1}$; heat flux needs $c_p\Delta T$.
2. **Treating the conduit viscosity as the mantle viscosity.** The flux scales as
   $1/\eta_c$; the difference is a factor of 100 in the model above.
3. **Reifying a plume temperature from a buoyancy flux.** $\Delta\rho$ and $Q$
   trade off, and neither is measured directly.
4. **Using $Ra\sim657$ as a stability threshold for a blob.** The blob's critical
   size is where $Ra_{\text{blob}}$ reaches the appropriate critical value for its
   geometry; every geologically plausible plume is far above any of them.
5. **Assuming conduction erases a plume's anomaly during ascent.** It does not:
   the Péclet number of a 500 km blob is $\sim10^{3}$. What conduction does limit
   is the *conduit*, whose anomaly erases in 79 Myr, so a plume must be fed
   continuously.
6. **Reading a hotspot track as absolute plate motion.** It is the *relative*
   motion of plate and hotspot.
7. **Reporting a crustal thickness from a melt model without the productivity
   assumption.** The two factors in the table differ by a factor of 2.

## Related modules

- [13-02-01 Rayleigh-Benard Convection Applied to the Mantle](01-rayleigh-benard-mantle.md) —
  the layer scalings generalised here to a blob.
- [13-02-02 Numerical Modelling of Mantle Convection](02-convection-numerical.md) —
  how a plume is represented in a convection code.
- [13-02-04 Subduction Dynamics, Slab Geometry and Slab Pull](04-subduction-dynamics.md) —
  the cold counterpart of the upwelling described here.
- [12-01-04 Lower-Mantle Heterogeneity and LLSVPs](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/04-lower-mantle-heterogeneity.md) —
  the deep-seated structures that may anchor plumes.
- [02-05-07 Thermodynamic Phase Equilibria and Mantle Mineralogy](../../02-physics/05-thermodynamics/07-phase-equilibria.md) —
  the phase relations replaced by straight lines above.
