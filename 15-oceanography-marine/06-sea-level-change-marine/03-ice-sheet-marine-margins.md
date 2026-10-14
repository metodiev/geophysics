---
id: 15-06-03
title: "Ice Sheet Marine Margins and Stability"
level: research
prereqs: ["15-06-01", "15-06-02", "15-03-01", "02-04-07"]
tags: [oceanography, marine-geophysics, sea-level-change, glaciology, ice-shelf, ice-dynamics]
---

# Ice Sheet Marine Margins and Stability

> **All models and data in this module are SYNTHETIC.** The flow law, the geometry,
> the mass balance and every table below are teaching models with the stated
> constants. No real ice sheet, glacier, shelf, catchment or published number is
> referenced.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the flotation condition at a grounding line and **compute** the
   grounding-line thickness and freeboard for any water depth.
2. **Derive** the shallow-ice flux law $q\propto h^{n+2}$ and **explain** why a
   20% thickness change changes the flux by 149%.
3. **Compute** the equilibrium thickness set by a catchment's accumulation supply.
4. **Demonstrate** why a retrograde bed has no nearby steady state, using the
   flux-gradient argument, and **compute** the disequilibrium distance.
5. **Quantify** buttressing as a back stress, compare it with the driving stress,
   and **compute** the inland shift produced by its loss.
6. **Compare** the basal-melt and accumulation fluxes of an ice shelf and **decide**
   which of the two competing failure modes (slow geometric retreat, rapid shelf
   removal) the numbers support.
7. **State** which quantities in a marine-margin projection are measured, which are
   modelled, and which are essentially unconstrained.

## Prerequisites

- [15-06-01 Palaeo Sea Level Reconstruction](01-paleo-sea-level.md) — how ice
  volume is converted to a sea-level equivalent.
- [15-06-02 Observing Modern Sea Level Rise](02-sea-level-rise-observation.md) —
  the mass observations that constrain the ice sheets.
- [15-03-01 Mid-Ocean Ridges: Structure, Magmatism and Hydrothermal Systems](../03-seafloor-tectonics/01-mid-ocean-ridges.md) —
  the bathymetric and subsidence framework of the sea floor on which margins sit.
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md) —
  the creep law used in Section 3.2.

## 1. Intuition: the bathymetry is a boundary condition, and it is the wrong shape

An ice sheet that reaches the sea does not end at a cliff. It thins, goes afloat,
and continues as a floating ice shelf, while the point where it last touches the
bed — the grounding line — determines how much ice can be discharged. Two facts make
this the hardest problem in sea-level projection.

First, the flux across the grounding line is a very steep function of thickness:
$q\propto h^{n+2}$ with $n=3$ in Glen's law, i.e. $q\propto h^5$ in this model. A
20% thicker ice discharges 149% more.

Second, in many places the bed *deepens inland*. That is the wrong way round. If
retreat into deeper water means thicker ice means more discharge, and more discharge
means more retreat, then a perturbation grows rather than being absorbed. This is
the **marine ice sheet instability**: no steady state exists near the original
position, and the margin retreats until the bed shallows inland, the catchment
shrinks, or lateral drag takes over.

There is a second, entirely different failure mode: a floating shelf can be melted
and calved faster than the interior supplies ice to it. In the model here, a melt
rate of 10 m/yr over a 50 km shelf removes **8.3 times** what accumulation supplies,
so the shelf would disappear in about 50 years *unless the flow accelerates*. Which
mode dominates is a competition between numbers, not a matter of principle — and
that competition is what this lesson quantifies.

## 2. Precise definitions

**Grounding line**: the boundary between grounded ice and floating ice.

**Ice shelf**: floating ice attached to the grounded sheet.

**Ice rise / pinning point**: a locally grounded feature that anchors a shelf and
raises its resistance.

**Buttressing**: the resistance a shelf exerts on the inland ice through
longitudinal stress and through lateral drag on embayment walls and pinning points.

**Retrograde / prograde bed**: bed slope such that water depth *increases* /
*decreases* inland.

**MISI (marine ice sheet instability)**: the positive feedback between retreat,
grounding-line thickness and discharge on a retrograde bed.

**Driving stress** $\tau_d$: the gravitational stress $\rho_i g h\alpha$ that pushes
the ice down-slope.

**Back stress**: the longitudinal and lateral stress opposing the flow; a shelf's
own unconfined back stress is the reference against which buttressing is compared.

**Accumulation supply** $aW$: the ice per unit width and per year delivered to the
grounding line from a catchment of width $W$ with surface mass balance $a$.

## 3. Derivations and measurements

### 3.1 Flotation

At the grounding line the ice is exactly at the point of going afloat, so
Archimedes gives $\rho_ih_g=\rho_{\text{sw}}d$:

$$\boxed{h_g=\frac{\rho_{\text{sw}}}{\rho_i}d=1.1210\,d}$$

for $\rho_i=917$ and $\rho_{\text{sw}}=1028\ \mathrm{kg\,m^{-3}}$. The freeboard is

$$h_g-d=h_g\left(1-\frac{\rho_i}{\rho_{\text{sw}}}\right)=0.1079\,h_g ,$$

i.e. **10.8% of the thickness**.

| $d$ (m) | $h_g$ (m) | freeboard (m) |
|---|---|---|
| 200 | 224.2 | 24.2 |
| 500 | 560.5 | 60.5 |
| 800 | 896.8 | 96.8 |
| 1000 | 1121.0 | 121.0 |
| 1500 | 1681.6 | 181.6 |

The flotation condition is exact given the densities and is the one relation in this
lesson that is not a rheological model. Everything else inherits the flow law. Note
the direct consequence: **thickness and water depth are locked together**, so a bed
map is a thickness map is a flux map.

### 3.2 The grounding-line flux law

Take the shallow-ice approximation with Glen's law
$\dot\varepsilon=A\tau^3$ ($n=3$). Balancing the driving stress
$\tau=\rho_i g h\alpha$ against the vertically averaged shear gives

$$u=\frac{2A}{n+2}(\rho_i g\alpha)^nh^{n+1},\qquad
q=uh=\frac{2A}{n+2}(\rho_i g\alpha)^nh^{n+2}.$$

With $A=2.40\times10^{-24}\ \mathrm{Pa^{-3}s^{-1}}$, $\alpha=0.010$ and
$\rho_ig\alpha=89.93\ \mathrm{Pa\,m^{-1}}$:

| $h$ (m) | $q$ (m²/yr) | $q/q(1000\ \mathrm{m})$ |
|---|---|---|
| 600 | 1 713 | 0.078 |
| 800 | 7 219 | 0.328 |
| 1000 | 22 032 | 1.000 |
| 1200 | 54 822 | 2.488 |
| 1500 | 167 302 | 7.594 |

**The exponent is 5, not 1.** $1.2^5=2.488$: a 20% thickness increase is a 149%
discharge increase. That single number is the engine of the instability.

*Units check*: $A\tau^3$ has units $\mathrm{Pa^{-3}s^{-1}Pa^3=s^{-1}}$, so the
velocity is dimensionless times $\mathrm{m^{n+1}}$ times the units of
$(\rho_ig\alpha)^n$, which is $(\mathrm{Pa\,m^{-1}})^n$. The product must come out as
a velocity; the demonstration performs this with SI seconds and converts to years
with $3.155\,76\times10^{7}$ s/yr.

### 3.3 Equilibrium thickness

In steady state the discharge must equal the supply. For a catchment of width $W$
with surface mass balance $a$,

$$q_{\text{in}}=aW,\qquad\text{so}\qquad
h_{\text{eq}}=h_*\left(\frac{aW}{q(h_*)}\right)^{1/5},$$

a pivot formula that lets the reference $q(1000\ \mathrm{m})=22032\ \mathrm{m^2\,yr^{-1}}$
be rescaled. For $W=200$ km and $a=0.3$ m/yr,

$$aW=60000\ \mathrm{m^2\,yr^{-1}},\qquad
h_{\text{eq}}=1000\left(\frac{60000}{22032}\right)^{1/5}=1221.9\ \mathrm{m},$$

corresponding to the water depth $h_{\text{eq}}/1.1210=1090$ m. Note how insensitive
the *thickness* is to the supply — the fifth root of a factor of 2.7 is 1.22 — while
the *flux* is violently sensitive to thickness. This asymmetry is the whole story:
geometry responds weakly, dynamics responds strongly.

### 3.4 The instability, argued properly

Suppose the grounding line sits at $d=1090$ m and is perturbed 10 km inland on a bed
that deepens inland at 10 m/km:

| retreat (km) | $d$ (m) | $h$ (m) | $q$ (m²/yr) | excess over supply |
|---|---|---|---|---|
| 0 | 1090 | 1221.9 | 60 000 | 0 |
| 5 | 1140 | 1277.9 | 75 084 | 15 084 |
| 10 | 1190 | 1334.0 | 93 061 | 33 061 |
| 20 | 1290 | 1446.1 | 139 312 | 79 312 |
| 40 | 1490 | 1670.3 | 286 411 | 226 411 |

The excess at 10 km is $93061-60000=33061\ \mathrm{m^2\,yr^{-1}}$, and the local
gradient is

$$\frac{\mathrm{d}q}{\mathrm{d}x}=5\frac{q}{h}\frac{\mathrm{d}h}{\mathrm{d}d}
\frac{\mathrm{d}d}{\mathrm{d}x}=3.98\ \mathrm{m^2\,yr^{-1}}\ \text{per metre} .$$

Dividing gives a **disequilibrium distance** of $33061/3.98=8314$ m ≈ 8.3 km. The
name matters: this is where the flux *would* match the supply if the gradient stayed
constant. It does not — the excess grows with retreat (33 061 at 10 km, 79 312 at
20 km) and the required retreat grows with it. **The model's honest output is not a
retreat rate but the statement that no steady state exists for this geometry.** The
retreat continues until the bed shallows (prograde), the catchment shrinks to cut
the supply, or lateral drag rises.

The slope sensitivity shows the same thing from the other side:

| bed slope (m/km) | excess at 10 km (m²/yr) | disequilibrium distance (km) |
|---|---|---|
| 5 | 15 084 | 9.1 |
| 10 | 33 061 | 8.3 |
| 20 | 79 312 | 7.1 |

A flatter retrograde bed gives a smaller excess but also a smaller gradient, so the
distance is *slightly* larger; a bed that shallows inland reverses the sign of
$\mathrm{d}h/\mathrm{d}x$ and removes the feedback. That sign is the classical
stability criterion often quoted as "grounding lines are stable on prograde beds".

### 3.5 Buttressing

An unconfined shelf of thickness $h$ exerts a longitudinal back stress

$$\sigma_b=\frac{\rho_ig h}{2}\left(1-\frac{\rho_i}{\rho_{\text{sw}}}\right) ,$$

and the driving stress at the same thickness is $\tau_d=\rho_igh\alpha$. Comparing
the two **at the same thickness** — the comparison is only meaningful that way, and
the model's equilibrium thickness of 1222 m is 2.4 times the shelf thickness used
below — the ratio is

$$\frac{\sigma_b}{\tau_d}=\frac{1-\rho_i/\rho_{\text{sw}}}{2\alpha} ,$$

which is **independent of thickness**. For $\alpha=0.010$ with $h=500$ m:
$\sigma_b=0.243$ MPa against $\tau_d=0.0450$ MPa, a ratio of **5.40**; for
$\alpha=0.005$ the ratio is 10.80 and for $\alpha=0.020$ it is 2.70.

The interpretation therefore has to be careful: an *unconfined* shelf already exerts
several times the driving stress, so it is not the case that the presence of a shelf
does nothing. What decides whether a margin holds is the **additional** resistance
from lateral drag on embayment walls and pinning points, which is why the sensitivity
is expressed through $\beta$ below rather than through the mere existence of a shelf.

Parametrising the loss of that extra resistance as a fractional reduction $\beta$ of
the discharge capacity, the equilibrium thickness must rise to keep the flux at the
supply:

$$h(\beta)=h_0(1-\beta)^{-1/5} .$$

| $\beta$ | $h$ required (m) | $d$ (m) | inland shift (km) |
|---|---|---|---|
| 0.0 | 1221.9 | 1090 | 0.0 |
| 0.2 | 1277.6 | 1140 | 5.0 |
| 0.4 | 1353.3 | 1207 | 11.7 |
| 0.6 | 1467.6 | 1309 | 21.9 |

**The flux is weakly sensitive to $\beta$ — the fifth root again — but the position
is not.** Losing 60% of the buttressing raises the required thickness by only 20%
yet moves the grounding line 21.9 km inland, because the thickness change is
converted to a position change by the bed slope. This is why "the shelf looks fine"
is not a stability argument: the geometry absorbs the change.

### 3.6 Basal melt versus accumulation

For a 50 km shelf and a 10 m/yr basal melt rate,

$$\text{melt flux}=10\times50000=5\times10^5\ \mathrm{m^2\,yr^{-1}},\qquad
\frac{\text{melt}}{aW}=\frac{5\times10^5}{6\times10^4}=8.3 .$$

The shelf's volume per unit width is $hW=500\times50000=2.5\times10^7\ \mathrm{m^2}$,
so at that melt rate, with no inflow, it would be removed in

$$t=\frac{2.5\times10^7}{5\times10^5}=50\ \mathrm{yr} .$$

Two honest qualifications. The "no inflow" assumption is false — the shelf is fed by
the same discharge that the buttressing keeps in balance, and the calculation is
therefore a statement about the *competition*, not a prediction. And a 10 m/yr basal
melt requires warm water at depth, whose supply is itself a circulation question
([15-01-03](../01-physical-oceanography/03-thermohaline-circulation.md)). The point
is the ratio: **8.3** is not a marginal number, and it is why shelf thinning is
observed to be a fast process on human timescales while grounding-line migration is
a fast process on decadal timescales.

## 4. Physical interpretation

- **The bed is the parameter that matters.** Flotation ties thickness to depth, so a
  bathymetric survey is the primary stability dataset — which is why marine
  geophysics contributes directly to sea-level projection
  ([15-02-02](../02-marine-geophysics-methods/02-multibeam-bathymetry.md)).
- **Exponent 5 is everything.** Weak supply sensitivity, violent thickness
  sensitivity; the two combine into an instability rather than a balance.
- **Two failure modes, different clocks.** Geometry-driven retreat operates through
  the flux law on a slope; shelf removal operates through melting against
  accumulation. A margin can be destabilised by either.
- **Buttressing loss is amplified by geometry.** A 20% thickness change is a 22 km
  position change; reports of stable-looking thickness therefore say little.
- **Nothing here gives a rate.** This is the honest limitation: the model gives
  existence and direction of instability, an equilibrium thickness, and a
  competition ratio — not a timescale for retreat, because the flux excess is not a
  velocity and the ice has to dynamically accelerate to deliver it.
- **What would add the rate**: a transient flow model with an evolving surface,
  lateral drag, calving and a melt boundary condition; and observations of
  grounding-line position through time.

## 5. Assumptions and regime of validity

1. **The shallow-ice approximation.** Valid where the aspect ratio is small and
   shear dominates over longitudinal stress — precisely the assumption that *fails*
   at a grounding line, where longitudinal stress and membrane effects dominate. The
   flux law here is a calibrated parameterisation, not a derivation for the
   grounding-line region.
2. **A single, uniform $A$ and isothermal ice at $-10\ ^\circ\mathrm{C}$-like
   stiffness.** Real ice is anisotropic and temperature-dependent, and $A$ varies by
   orders of magnitude with temperature and fabric.
3. **$n=3$, no sliding.** Sliding and till deformation add a term that can dominate,
   and the exponent for sliding is different ($\propto h^3$). The instability
   survives, but the numbers change.
4. **Equilibrium/steady-state arguments.** All balance results require a steady
   state that §3.4 shows may not exist; they are local-in-time statements.
5. **A plug-flow, unconfined shelf for the back stress.** No lateral drag, no
   pinning points, no ice-rise anchors: the whole point of the comparison in §3.5 is
   that the *unconfined* shelf value is the baseline, not the total resistance.
6. **$\beta$ as a fractional capacity reduction.** This is a scalar idealisation of a
   tensorial, spatially varying buttressing field.
7. **Constant accumulation, no surface melt, no calving.** Each is a real term of
   comparable magnitude in a real catchment, and each adds its own uncertainty.
8. **A 50 km shelf and 10 m/yr melt are model choices.** The 8.3 ratio and the 50 yr
   follow from them; a different geometry or melt rate gives a different number, and
   the reported quantity should always carry its inputs.
9. **No geology.** Sediment strength, subglacial hydrology and bed roughness control
   sliding and are all but unconstrained beneath ice.
10. **No sea-level coupling.** Grounding-line retreat lowers the ice surface and
    changes local sea level, which changes flotation — a coupled problem this model
    ignores.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| ice / seawater density | $\rho_i,\rho_{\text{sw}}$ | kg m⁻³ | 917, 1028 |
| flotation ratio | — | dimensionless | 1.1210 |
| thickness, depth | $h,d$ | m | $h=\text{ratio}\times d$ |
| freeboard | | m | 0.108 $h$ |
| strain-rate factor | $A$ | Pa⁻³ s⁻¹ | 2.40e−24 |
| driving stress | $\tau$ | Pa | $\rho_igh\alpha$ |
| flux | $q$ | m² yr⁻¹ | $uh$, per unit width |
| surface balance | $a$ | m yr⁻¹ | |
| supply | $aW$ | m² yr⁻¹ | |
| back stress | $\sigma_b$ | Pa (MPa) | $\rho_igh(1-\rho_i/\rho_{\text{sw}})/2$ |
| melt rate | $\dot m$ | m yr⁻¹ | |

Two checks worth performing every time: $uh$ must have units m²/yr, i.e. volume per
unit width per year, and comparing it with $aW$ is legitimate only because both are
per unit width. Mixing a total flux with a per-unit-width supply is a factor-$W$
error, and it is easy to make.

## 7. Worked examples

All numbers are printed by `code/ice_sheet_marine_margins_demo.py`.

### Example 1 — the grounding line in 1000 m of water

$h_g=1.1210\times1000=1121.0$ m, freeboard $121.0$ m (10.8%).

### Example 2 — the flux sensitivity

$q(1000)=22032$ and $q(1200)=54822\ \mathrm{m^2\,yr^{-1}}$; the ratio is 2.488, i.e.
**+149% for +20% thickness**.

### Example 3 — the equilibrium

$W=200$ km, $a=0.3$ m/yr: $aW=60000$; $h_{\text{eq}}=1221.9$ m, i.e.
$d=1090$ m.

### Example 4 — the disequilibrium distance

10 km of retreat gives $q=93061$, an excess of 33 061 m²/yr;
$\mathrm{d}q/\mathrm{d}x=3.98$ m²/yr per m; the distance is 8.3 km — but the excess
grows, so no equilibrium is reached.

### Example 5 — losing buttressing

$\beta=0.6$: $h$ rises from 1222 to 1468 m, i.e. a water depth of 1309 m, an inland
shift of 21.9 km.

### Example 6 — the melt competition

10 m/yr over 50 km is 500 000 m²/yr, **8.3×** the accumulation supply, and the shelf's
2.5×10⁷ m² of section per unit width would go in 50 yr without inflow.

## 8. Python demonstration

`code/ice_sheet_marine_margins_demo.py` prints, with units:

1. the flotation table and freeboard fraction;
2. the flux-law table, the exponent-5 statement and the equilibrium thickness from a
   catchment supply;
3. the MISI retreat table, $\mathrm{d}q/\mathrm{d}x$, the disequilibrium distance,
   the slope sensitivity, and the statement that no steady state exists;
4. the like-for-like stress comparison and its thickness-independent ratio, the
   $\beta$ table and the inland shifts, and the melt-versus-accumulation competition;
5. the worked-example values of Section 7.

```bash
cd 15-oceanography-marine/06-sea-level-change-marine/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ice_sheet_marine_margins_demo.py
```

## 9. Exercises

[`exercises/03-ice-sheet-marine-margins-exercises.md`](./exercises/03-ice-sheet-marine-margins-exercises.md)
and
[`exercises/03-ice-sheet-marine-margins-solutions.md`](./exercises/03-ice-sheet-marine-margins-solutions.md).

## 10. Real-world applications

- **Sea-level projection.** Marine margins are the largest single uncertainty in
  century-scale projections, and the instability is why projections are asymmetric.
- **Bathymetric survey planning.** The critical data for stability are the water
  depth and bed slope beneath and inland of the grounding line
  ([15-02-02](../02-marine-geophysics-methods/02-multibeam-bathymetry.md)).
- **Ice-shelf monitoring.** Thickness-change and melt-rate estimates feed the
  competition of §3.6
  ([07-05-01](../../07-gravity-geodesy/05-satellite-gravimetry/01-grace-gracefo.md)).
- **Palaeo analogues.** Past rapid retreats provide the empirical constraint the
  models lack ([15-06-01](01-paleo-sea-level.md)).
- **Sediment and fjord records.** Grounding-zone deposits record past positions
  ([15-02-04](../02-marine-geophysics-methods/04-sub-bottom-profiling.md)).
- **Ocean heat supply.** Basal melt is a circulation problem as much as a
  glaciological one ([15-01-03](../01-physical-oceanography/03-thermohaline-circulation.md)).

## 11. Further reading

- **Schoof, C., "Ice sheet grounding line dynamics: steady states, stability and
  hysteresis", *Journal of Geophysical Research*.** Level: research. The boundary
  layer theory behind the flux parameterisation used here.
- **Weertman, J., "Stability of the junction of an ice sheet and an ice shelf",
  *Journal of Glaciology*.** Level: research (historical). The first statement of
  the instability.
- **Joughin, I., Smith, B. E., & Medley, B., "Marine ice sheet collapse potentially
  under way for the Thwaites Glacier basin", *Science*.** Level: research. An
  observational treatment of a retrograde bed and the honest caveats that go with it.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint
- [ ] I can derive and use the flotation condition and freeboard fraction.
- [ ] I can derive $q\propto h^{n+2}$ and state the 149% result.
- [ ] I can compute an equilibrium thickness from a supply.
- [ ] I can explain why a retrograde bed has no nearby equilibrium and compute a
      disequilibrium distance.
- [ ] I can compute an unconfined-shelf back stress and compare it with the driving
      stress.
- [ ] I can quantify the inland shift from a buttressing loss.
- [ ] I can state which of these numbers are measured, modelled or unconstrained.
## Common pitfalls
1. **Treating the stress ratio as a stability verdict.** The unconfined shelf stress
   is 2.7–10.8 times the driving stress depending on the surface slope, so the ratio
   tells you the shelf matters, not whether the margin is stable. What decides it is
   the additional lateral and pinning resistance, represented by $\beta$.
2. **Reading a retreat rate off a static flux balance.** The model gives instability,
   not a rate.
3. **Using the shallow-ice flux law at the grounding line without caveat.** That is
   where its assumptions fail worst.
4. **Ignoring sliding.** Adding it can change the exponent and the magnitude.
5. **Quoting $\beta$ as if it were measured.** It is a scalar idealisation.
6. **Assuming a shelf thins by melt alone.** Melting and inflow compete; the ratio is
   what matters.
7. **Confusing prograde and retrograde.** Only the sign of the bed slope inland
   decides whether the feedback amplifies or damps.
8. **Forgetting that flotation couples to sea level itself.** Retreat changes local
   sea level, which changes flotation.

## Related modules
- [15-06-01 Palaeo Sea Level Reconstruction](01-paleo-sea-level.md) — converting an
  ice volume to a sea-level equivalent.
- [15-06-02 Observing Modern Sea Level Rise](02-sea-level-rise-observation.md) — how
  the ice-sheet mass term is actually measured.
- [15-02-02 Multibeam Bathymetry](../02-marine-geophysics-methods/02-multibeam-bathymetry.md) —
  the data that make the bed slope known.
- [15-01-03 Thermohaline Circulation](../01-physical-oceanography/03-thermohaline-circulation.md) —
  where the warm water that melts shelves comes from.
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md) —
  the creep law and its exponents.
- [15-03-01 Mid-Ocean Ridges](../03-seafloor-tectonics/01-mid-ocean-ridges.md) — how
  sea-floor depth is generated and how it subsides.
