---
id: 15-04-02
title: "Gas Hydrates: Occurrence, Geophysics and Resource Potential"
level: research
prereqs: ["15-04-01", "15-03-01", "15-02-01", "05-04-01"]
tags: [oceanography, marine-geophysics, seafloor-mapping, gas-hydrates, rock-physics, resources]
---

# Gas Hydrates: Occurrence, Geophysics and Resource Potential

> **All models and data in this module are SYNTHETIC.** The phase boundary, the
> rock-physics models and the reservoir geometry are teaching models with stated
> model constants. No real field, well, basin, hydrate deposit or cruise is
> referenced, and no number is quoted from a published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the gas yield of structure-I methane hydrate from its unit-cell
   stoichiometry, and **state** which assumed constants set the answer.
2. **Compute** a hydrate dissociation pressure from a Clausius–Clapeyron model
   and **determine** the base of the stability zone for a given seafloor
   temperature and geothermal gradient.
3. **Quantify** how seafloor temperature, water depth and gradient move the base,
   and **state** what a bottom-simulating reflector does and does not measure.
4. **Compute** a hydrate-saturated velocity with a Gassmann fluid-substitution
   model, and **invert** an observed velocity for saturation.
5. **Demonstrate** with numbers that the inverted saturation depends on the
   rock-physics model by a factor of about two, and that the velocity constrains
   a curve in (porosity, saturation) rather than either parameter.
6. **Compute** a gas-in-place estimate and **propagate** the parameters the
   velocity cannot constrain into the result.
7. **Distinguish** what the seismic data measure (velocities, a reflector, a
   blanking pattern) from what the resource statement requires (porosity,
   saturation, thickness, recovery).

## Prerequisites

- [15-04-01 Benthic Habitat Mapping and Classification](01-habitat-mapping.md) —
  the seafloor characterisation that frames a hydrate survey.
- [15-03-01 Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems](../03-seafloor-tectonics/01-mid-ocean-ridges.md) —
  the sea-floor depth and heat-flow framework this lesson quantifies, and the
  conductive geotherm that the stability zone sits on.
- [15-02-01 Marine Seismic Reflection](../02-marine-geophysics-methods/01-marine-seismic-reflection.md) —
  how the reflector and the velocities are measured.
- [05-04-01 Porosity, Density and Velocity](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  the rock physics used in §3.3.

## 1. Intuition: a solid that is a fluid, and a resource that is a phase

Gas hydrate is methane trapped in a water-ice-like cage. It is a solid mineral —
it has a shear modulus — but it occupies pore space exactly where a fluid would,
and it is stable only within a pressure–temperature window. Those two facts
control everything in this lesson.

The window is why hydrate has a **bottom-simulating reflector**: at the base of
the stability zone the hydrate dissociates, the sediment's velocity drops, and a
reflection appears. That reflector is one of the few geophysical signals that
follows a *thermodynamic* boundary rather than a geological one, and it is
tempting to read it as a thermometer. It is not: the depth depends on the phase
boundary (a model), the seafloor temperature (measured), the pressure profile
(nearly known) and the geothermal gradient (the unknown), and the last two trade
off.

The solid-but-pore-filling character is why hydrate is hard to quantify. A
velocity anomaly proves that *something* has stiffened the sediment. Turning that
into a saturation requires a rock-physics model, and §3.3 shows that two
reasonable models — hydrate as part of the pore fluid, and hydrate as a cement of
the grain frame — give saturations that differ by a factor of 2.08 from the same
measured velocity. A resource estimate built on that velocity then inherits the
ambiguity, and adds to it the porosity, the thickness and the recovery factor.

**The honest summary of this lesson is that the geophysics measures a velocity
anomaly and a reflector depth; the resource number is a model output.** The
lesson's job is to make the model's inputs explicit enough that the number can be
argued with.

## 2. Precise definitions

**Clathrate (hydrate)**: a non-stoichiometric crystalline inclusion compound in
which guest molecules occupy cages formed by host water molecules.
**Structure I** is the common methane hydrate structure, with a unit cell of
46 water molecules and up to 8 guest molecules.

**Occupancy**: the fraction of available cages filled. It is a model parameter
(reflecting gas availability and formation history), not a constant.

**Gas yield $Y$**: the volume of gas at standard temperature and pressure
released by a unit volume of hydrate, $\mathrm{m^3\,(STP)\,m^{-3}}$.

**Hydrate stability zone (HSZ)**: the depth interval in which the local
temperature and pressure place the system inside the hydrate stability field.
Its base is the **bottom-simulating reflector (BSR)** where the transition is
sharp enough to reflect.

**Fluid substitution**: the prediction of a saturated rock's moduli from its dry
moduli and a pore-fluid modulus — Gassmann's equation, exact under stated
assumptions.

**Critical porosity / dry-frame model**: an empirically parameterised relation
between porosity and the dry-rock elastic moduli. Every rock-physics inversion of
hydrate saturation uses one, and the choice moves the answer.

**Recovery factor**: the fraction of in-place gas that could be produced. It is
not a geophysical quantity and it multiplies the uncertainty of everything above.

## 3. Derivations

### 3.1 The gas yield from the unit cell

The ideal structure-I cell contains $N_w=46$ water molecules and $N_g=8$ guest
sites. At full occupancy the mass fraction of methane is

$$f_{\mathrm{CH_4}}=\frac{N_gM_{\mathrm{CH_4}}}{N_gM_{\mathrm{CH_4}}+N_wM_{\mathrm{H_2O}}}
=\frac{8\times16.043}{8\times16.043+46\times18.015}=0.13411,$$

using the exact molar masses $M_{\mathrm{CH_4}}=16.043\ \mathrm{g\,mol^{-1}}$
and $M_{\mathrm{H_2O}}=18.015\ \mathrm{g\,mol^{-1}}$. One cubic metre of hydrate
of density $\rho_h$ holds $\rho_hf_{\mathrm{CH_4}}/M_{\mathrm{CH_4}}$ moles of
methane, and one mole occupies $V_m=22.414\times10^{-3}\ \mathrm{m^3}$ at STP
($273.15\ \mathrm{K}$, $101.325\ \mathrm{kPa}$ — the standard molar volume of an
ideal gas). Hence

$$\boxed{\;Y=\frac{\rho_hf_{\mathrm{CH_4}}}{M_{\mathrm{CH_4}}}V_m
=\frac{900\times0.13411}{16.043\times10^{-3}}\times22.414\times10^{-3}
=168.6\ \mathrm{m^3\,(STP)\,m^{-3}}\;}$$

The demonstration's sensitivity table:

| $\rho_h$ (kg/m³) | occupancy | $Y$ (m³/m³) |
|---|---|---|
| 850 | 0.8 | 130.9 |
| 850 | 1.0 | 159.3 |
| 900 | 0.8 | 138.6 |
| 900 | 1.0 | 168.6 |
| 950 | 1.0 | 178.0 |

**Two assumed constants — density and occupancy — move the yield by 36%.** The
yield is derived, not measured, and it is quoted with its assumptions or not at
all.

### 3.2 The base of the stability zone

Use a Clausius–Clapeyron model for the dissociation pressure,

$$\ln\frac{p_{\text{eq}}}{p_{\text{ref}}}
=-\frac{\Delta H}{R}\left(\frac{1}{T}-\frac{1}{T_{\text{ref}}}\right),$$

with the model constants $\Delta H/R=6516\ \mathrm{K}$ (equivalent to
$\Delta H=54.2\ \mathrm{kJ\,mol^{-1}}$), $T_{\text{ref}}=273.15\ \mathrm{K}$ and
$p_{\text{ref}}=2.60\ \mathrm{MPa}$. The demonstration's curve:

| $T$ (K) | $p_{\text{eq}}$ (MPa) | equivalent hydrostatic depth (m) |
|---|---|---|
| 275.15 | 3.09 | 297 |
| 280.15 | 4.72 | 458 |
| 285.15 | 7.10 | 694 |
| 290.15 | 10.52 | 1033 |
| 295.15 | 15.39 | 1516 |
| 300.15 | 22.23 | 2194 |

The base of the HSZ is where the **geotherm** $T(z)=T_s+\Gamma z$ intersects the
boundary, with the pressure given hydrostatically,
$p(z)=p_{\text{seafloor}}+\rho_wgz$. Solving for the model settings:

| water depth (m) | $T_s$ (°C) | $\Gamma$ (°C/km) | base (m below seafloor) |
|---|---|---|---|
| 500 | 2 | 25 | 660 |
| 500 | 4 | 40 | 206 |
| 1000 | 2 | 25 | 930 |
| 1000 | 2 | 40 | 496 |
| 1000 | 4 | 40 | 431 |
| 2000 | 2 | 25 | 1214 |
| 2000 | 4 | 40 | 640 |

The base spans **206–1214 m** across plausible parameters. Since the boundary
slope is steep (a 20% pressure rise per kelvin, from the table), the crossing is
sensitive to both the seafloor temperature and the gradient:

- A $2\ ^\circ\mathrm{C}$ warmer seafloor shallows the base from 496 m to 431 m
  at 1000 m water depth and 40 °C/km. Note what is *not* changing: the
  temperature at the base moves only from $21.8$ to $21.2\ ^\circ\mathrm{C}$,
  because the base lies on the phase boundary by construction. The 2 K of
  seafloor warming is absorbed entirely by a 65 m shallowing of the base, which
  is 13% of its depth — so the base depth is a sensitive proxy for seafloor
  temperature *given* a gradient;
- Doubling the water depth to 2000 m *deepens* the base (640 m at 4 °C and
  40 °C/km), because the extra pressure extends the stability field.

**A BSR depth therefore measures a combination of the seafloor temperature, the
gradient and the phase boundary.** To use it as a geothermometer, the boundary
must be assumed; to use it as a phase-boundary test, the gradient must be
measured. It cannot do both, and that is the honest statement of this section.

### 3.3 Velocity, saturation and the rock-physics choice

Take a clean sand with porosity $\phi=0.35$, mineral moduli
$K_s=36\ \mathrm{GPa}$, $G_s=45\ \mathrm{GPa}$, $\rho_s=2650\
\mathrm{kg\,m^{-3}}$, water $K_w=2.2\ \mathrm{GPa}$, $\rho_w=1030\
\mathrm{kg\,m^{-3}}$, hydrate $K_h=7.9\ \mathrm{GPa}$, $G_h=3.3\ \mathrm{GPa}$,
$\rho_h=920\ \mathrm{kg\,m^{-3}}$, and a stated dry-frame model
$K_{\text{dry}}=1.0\ \mathrm{GPa}$,
$G_{\text{dry}}=0.6\ \mathrm{GPa}$ at $\phi=0.35$ (a soft, unconsolidated frame).
Gassmann's equation,

$$K_{\text{sat}}=K_{\text{dry}}+\frac{(1-K_{\text{dry}}/K_s)^2}
{\dfrac{\phi}{K_{\text{fl}}}+\dfrac{1-\phi}{K_s}-\dfrac{K_{\text{dry}}}{K_s^{2}}},
\qquad G=G_{\text{dry}},$$

with $v_p=\sqrt{(K_{\text{sat}}+\tfrac43G)/\rho}$ and
$\rho=(1-\phi)\rho_s+\phi[S_h\rho_h+(1-S_h)\rho_w]$.

**Model A (pore-filling):** hydrate is part of the pore fluid, so
$K_{\text{fl}}=[S_h/K_h+(1-S_h)/K_w]^{-1}$ (the Reuss average of the two pore
fluids).
**Model B (cementation):** hydrate stiffens the frame, so
$K_{\text{dry}}\to K_{\text{dry}}+4.0\sqrt{S_h}\ \mathrm{GPa}$,
$G_{\text{dry}}\to G_{\text{dry}}+3.0\sqrt{S_h}\ \mathrm{GPa}$ and
$K_{\text{fl}}=K_w$.

| $S_h$ | $v_p$ pore-filling (m/s) | $v_p$ cementation (m/s) |
|---|---|---|
| 0.0 | 1853.9 | 1853.9 |
| 0.1 | 1903.3 | 2119.1 |
| 0.2 | 1958.6 | 2221.4 |
| 0.3 | 2020.8 | 2297.8 |
| 0.4 | 2091.6 | 2360.8 |
| 0.5 | 2172.9 | 2415.5 |
| 0.7 | 2379.7 | 2508.9 |
| 1.0 | 2896.1 | 2624.2 |

The models agree at $S_h=0$ (both are water-saturated sand at
$1853.9\ \mathrm{m\,s^{-1}}$) and *reverse their ranking* by $S_h=1$: the
pore-filling model is the steeper one at high saturation, the cementation model
at low saturation.

**Inversion.** An observed $v_p=2300\ \mathrm{m\,s^{-1}}$ gives

$$S_h^{\text{pore-filling}}=0.631,\qquad S_h^{\text{cementation}}=0.303,$$

a ratio of **2.08**. The round-trip check confirms the pore-filling inversion
reproduces 2300.000 m/s. The lesson's central claim is therefore not a warning
about precision but a statement of fact: **the same measured velocity is
consistent with saturations a factor of two apart, and the choice between the
models is a geological argument, not a geophysical measurement.**

**The shear velocity is the discriminator.** Gassmann leaves the shear modulus
untouched by fluid substitution, so a pore-filling hydrate changes $v_s$ only
through the density; a cementing hydrate stiffens the frame and raises $v_s$ by a
factor of two. The demonstration prints both:

| $S_h$ | $v_s$ pore-filling | $v_s$ cementation | $v_p/v_s$ pore-filling | $v_p/v_s$ cementation |
|---|---|---|---|---|
| 0.0 | 536.7 | 536.7 | 3.45 | 3.45 |
| 0.3 | 538.2 | 1040.6 | 3.75 | 2.21 |
| 0.5 | 539.2 | 1148.3 | 4.03 | 2.10 |
| 1.0 | 541.7 | 1327.0 | 5.35 | 1.98 |

At $S_h=0.5$ the two models differ by 243 m/s in $v_p$ but by **609 m/s in
$v_s$**, and the $v_p/v_s$ ratios (4.03 against 2.10) are separated by a factor of
two. A converted-wave or ocean-bottom survey therefore settles the question that
a $v_p$ section cannot — and the reason is structural, not merely quantitative:
the two models differ in *which* elastic modulus they change.

**The (porosity, saturation) trade-off.** Using the pore-filling model, the pairs
reproducing 2300 m/s are

| $\phi$ | $S_h$ |
|---|---|
| 0.25 | 0.397 |
| 0.30 | 0.534 |
| 0.35 | 0.631 |
| 0.40 | 0.703 |
| 0.45 | 0.760 |

Velocity constrains a **curve**, not a point. Porosity must come from a log, a
core, or an independent seismic attribute.

### 3.4 Gas in place

For a model accumulation of $A=100\ \mathrm{km^2}$, $h=50\ \mathrm{m}$,
$\phi=0.35$, $S_h=0.40$ and the derived yield
$Y=168.6\ \mathrm{m^3\,(STP)\,m^{-3}}$:

$$V_{\text{gas}}=Ah\phi S_hY
=10^{8}\times50\times0.35\times0.40\times168.6
=1.180\times10^{11}\ \mathrm{m^3\ (STP)},$$

i.e. $118.0\times10^{9}\ \mathrm{m^3}$ or $4.17\times10^{12}\ \mathrm{ft^3}$
(using the exact $1\ \mathrm{m^3}=35.3147\ \mathrm{ft^3}$).

**Sensitivity** (gas in place, $10^9\ \mathrm{m^3}$):

| $\phi$ \ $S_h$ | 0.2 | 0.4 | 0.6 |
|---|---|---|---|
| 0.25 | 42.2 | 84.3 | 126.5 |
| 0.35 | 59.0 | 118.0 | 177.1 |
| 0.45 | 75.9 | 151.8 | 227.6 |

The corner-to-corner range is **5.4×** from porosity and saturation alone — the
two parameters the velocity cannot separate. Add the rock-physics ambiguity
(2.08×) and a recovery factor, and the resource number is an interval of more
than an order of magnitude. **Any hydrate resource figure quoted to two
significant figures is quoting the inputs, not the reservoir.**

## 4. Physical interpretation

- **Hydrate is a phase, so its distribution is thermodynamic first and
  geological second.** That is why BSRs are common in deep water and absent where
  the geotherm is steep.
- **The BSR tracks the base of the *stability* field, not the base of the
  *hydrate*.** Below the base there may be no hydrate; above it there may be
  little, if gas was never supplied. A BSR is necessary but not sufficient for a
  hydrate accumulation.
- **A velocity anomaly is a stiffening measurement.** Hydrate, cementation,
  compaction, a different mineralogy and overpressure all stiffen; velocity alone
  cannot apportion them.
- **Free gas below the base sharpens the reflector** because it drops the
  velocity further; that is why BSRs are often strong. It also means the
  reflector's amplitude is a free-gas measurement as much as a hydrate one.
- **The interesting quantities are all products.** $Ah\phi S_hY$ is a product of
  five numbers, four of which are models or assumptions.

## 5. Assumptions and regime of validity

1. **Ideal structure-I stoichiometry and stated density.** Real hydrates have
   mixed guests (methane, carbon dioxide, heavier hydrocarbons), variable
   occupancy, and a density that depends on both.
2. **A pure-methane, pure-water phase boundary with constant $\Delta H$.** Salinity
   depresses the boundary (by several kelvin at seawater salinity), and the
   Clapeyron slope is not constant over a wide temperature range.
3. **Hydrostatic pressure.** Overpressure or underpressure shifts the boundary
   directly, and overpressure is common in the settings that host hydrates.
4. **A conductive geotherm with no advection.** Fluid flow along a permeable
   layer — exactly what a hydrate-bearing system encourages — distorts it.
5. **Gassmann's assumptions:** isotropic, homogeneous, fully connected pore fluid,
   a single effective fluid modulus at the seismic frequency, and a frame that is
   the same with and without the fluid. A hydrate-cemented frame violates the last
   one, which is precisely the ambiguity of §3.3.
6. **The dry-frame model.** Both $K_{\text{dry}}$ and its porosity dependence are
   fitted model choices; a stiffer or softer frame moves every velocity by tens of
   metres per second and the inversion by a comparable fraction.
7. **A uniform reservoir.** Thickness, porosity and saturation are treated as
   constants over 100 km²; real accumulations are heterogeneous at every scale,
   and averaging over a heterogeneous medium changes the effective elastic
   properties.
8. **No recovery.** Gas in place is not a reserve; recovery requires permeability
   (in a system whose permeability hydrate itself reduces), a drive mechanism and
   an economic price.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| molar mass | $M$ | $\mathrm{kg\,mol^{-1}}$ | $16.043\times10^{-3}$ for CH₄ |
| density | $\rho$ | $\mathrm{kg\,m^{-3}}$ | hydrate ≈ 900 (model) |
| gas yield | $Y$ | $\mathrm{m^3\,m^{-3}}$ | volume ratio, dimensionless |
| pressure | $p$ | Pa | 1 MPa = $10^{6}$ Pa |
| temperature | $T$ | K | K, not °C, inside exponentials |
| gradient | $\Gamma$ | $\mathrm{^\circ C\,km^{-1}}$ | divide by 1000 for per metre |
| moduli | $K,G$ | Pa | GPa = $10^{9}$ Pa |
| velocity | $v_p$ | $\mathrm{m\,s^{-1}}$ | |
| gas volume | $V$ | $\mathrm{m^3}$ (STP) | $1\ \mathrm{m^3}=35.3147\ \mathrm{ft^3}$ |

The two checks worth doing: the exponential argument in the Clausius–Clapeyron
relation must be dimensionless (so $T$ in kelvin and $\Delta H/R$ in kelvin), and
$v_p=\sqrt{(K+4G/3)/\rho}$ requires both moduli and density in SI. A density left
in $\mathrm{g\,cm^{-3}}$ inflates every velocity by a factor of 31.6.

## 7. Worked examples

All numbers are printed by `code/gas_hydrates_demo.py`.

### Example 1 — the gas yield

$$f_{\mathrm{CH_4}}=\frac{128.344}{128.344+828.690}=0.13411,\quad
Y=\frac{900\times0.13411}{0.016043}\times0.022414=168.6\ \mathrm{m^3\,m^{-3}}.$$

At 0.8 occupancy and $\rho_h=850\ \mathrm{kg\,m^{-3}}$ the yield falls to
130.9 m³/m³, a 22% reduction from the occupancy alone.

### Example 2 — the phase boundary

$$p_{\text{eq}}(285.15\ \mathrm{K})=2.60\exp\left[-6516\left(
\frac{1}{285.15}-\frac{1}{273.15}\right)\right]=7.10\ \mathrm{MPa},$$

equivalent to a hydrostatic depth of 694 m, and
$p_{\text{eq}}(295.15\ \mathrm{K})=15.39\ \mathrm{MPa}$ (1516 m). A 10 K warming
more than doubles the pressure required to keep the hydrate stable.

### Example 3 — the base of the stability zone

At 1000 m water depth, $T_s=2\ ^\circ\mathrm{C}$ and
$\Gamma=40\ \mathrm{^\circ C\,km^{-1}}$, the base is **496 m** below the seafloor;
at $T_s=4\ ^\circ\mathrm{C}$ it is **431 m**; at $\Gamma=25\
\mathrm{^\circ C\,km^{-1}}$ and $2\ ^\circ\mathrm{C}$ it deepens to **930 m**.
The three settings bracket the range of BSR depths seen in practice by an order
of magnitude in the ratio of gradient to boundary slope.

### Example 4 — one velocity, two saturations

With $\phi=0.35$ and $v_p=2300\ \mathrm{m\,s^{-1}}$: pore-filling
$S_h=0.631$, cementation $S_h=0.303$. The forward models at $S_h=0.5$ give 2173
and 2416 m/s — a 243 m/s difference, which is much larger than the precision of
a careful velocity analysis and therefore resolvable *in principle*, but only if
the model form is already known or if the saturation is already bracketed. The
$v_s$ values at $S_h=0.5$, 539.2 and 1148.3 m/s, differ by 609 m/s, and the
$v_p/v_s$ ratios 4.03 and 2.10 differ by a factor of two: **the shear measurement
is the discriminative one, and it is not optional.**

### Example 5 — gas in place

$Ah\phi S_hY=10^{8}\times50\times0.35\times0.40\times168.6
=1.180\times10^{11}\ \mathrm{m^3}$ (STP) $=4.17\times10^{12}\ \mathrm{ft^3}$.
Changing $\phi$ from 0.35 to 0.25 and $S_h$ from 0.4 to 0.2 gives
$4.22\times10^{10}\ \mathrm{m^3}$ — a factor 2.8 below the base case, and the
model choice in Example 4 would move it by a further factor 2.08.

## 8. Python demonstration

`code/gas_hydrates_demo.py` prints, with units:

1. the unit-cell mass fraction, the molar volume, and the derived gas yield, with
   its sensitivity to density and occupancy;
2. the dissociation pressure curve and the equivalent hydrostatic depths;
3. the base of the stability zone for a grid of water depths, seafloor
   temperatures and gradients;
4. $v_p(S_h)$ for the pore-filling and cementation models, the inversion of
   $v_p=2300\ \mathrm{m\,s^{-1}}$, and the round-trip check;
5. the $(\phi,S_h)$ trade-off curve at fixed velocity;
6. the gas-in-place estimate and its sensitivity table;
7. the worked-example values of Section 7.

```bash
cd 15-oceanography-marine/04-seafloor-mapping-and-habitats/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gas_hydrates_demo.py
```

## 9. Exercises

[`exercises/02-gas-hydrates-exercises.md`](./exercises/02-gas-hydrates-exercises.md)
and
[`exercises/02-gas-hydrates-solutions.md`](./exercises/02-gas-hydrates-solutions.md).

## 10. Real-world applications

- **Energy resource assessment.** National hydrate resource estimates are built
  from exactly this arithmetic, and their uncertainty is dominated by $S_h$,
  $\phi$ and recovery.
- **Drilling hazard.** Hydrate dissociation during drilling releases gas and
  water; the stability field defines the hazard window.
- **Seafloor stability and climate.** Dissociation on slopes is a landslide
  trigger and a potential methane source; both depend on the same phase boundary
  ([04-07-03 Landslides](../../04-earth-science-geology/07-geologic-hazards/03-landslides.md)).
- **Seismic interpretation.** BSRs, blanking, velocity pull-up and amplitude
  anomalies are the standard hydrate indicators and all are rock-physics
  inferences ([15-02-01](../02-marine-geophysics-methods/01-marine-seismic-reflection.md)).
- **Carbon storage analogue.** The same cage chemistry is used for CO₂ storage in
  hydrate form.

## 11. Further reading

- **Sloan, E. D., & Koh, C. A., *Clathrate Hydrates of Natural Gases*, CRC
  Press.** Level: research monograph. The phase equilibria and structure
  chemistry behind §3.1–3.2.
- **Mavko, G., Mukerji, T., & Dvorkin, J., *The Rock Physics Handbook*, Cambridge
  University Press.** Level: research reference. Gassmann's equation and the
  dry-frame models used in §3.3.
- **Chand, S., & Minshull, T. A., "The effect of hydrate content on seismic
  attenuation", *Geophysical Research Letters*.** Level: research. An example of
  the model-dependence of saturation estimates.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint
- [ ] I can derive the gas yield and state what it depends on.
- [ ] I can compute a dissociation pressure and the equivalent hydrostatic depth.
- [ ] I can find the base of the stability zone for given $T_s$, $\Gamma$ and
      water depth.
- [ ] I can run a Gassmann fluid substitution with a hydrate-bearing pore fluid.
- [ ] I can invert a velocity for saturation under two models and state the
      difference.
- [ ] I can produce the $(\phi,S_h)$ trade-off curve at fixed velocity.
- [ ] I can compute gas in place and name the parameters that dominate its range.
- [ ] I can state which of those parameters a seismic survey actually measures.
## Common pitfalls
1. **Quoting a gas yield without the density and occupancy.** A 36% range is
   spanned by two assumed constants.
2. **Reading a BSR as a geothermometer.** It measures a product of the phase
   boundary, the seafloor temperature and the gradient.
3. **Using one rock-physics model as *the* answer.** Pore-filling and cementation
   differ by a factor 2.08 in saturation for the same velocity.
4. **Reporting a saturation without a porosity.** They trade off along a curve.
5. **Assuming the BSR marks the top of the hydrate.** It marks the base of the
   stability field; hydrate abundance is a separate, supply-limited question.
6. **Treating in-place gas as a reserve.** Permeability, drive and price are
   absent from the arithmetic.
7. **Forgetting salinity.** Seawater composition depresses the phase boundary and
   therefore shallows the base.
8. **Quoting five significant figures from a product of five models.** The
   numbers in §3.4 have one useful significant figure beyond the leading digit of
   the range.

## Related modules
- [15-04-01 Benthic Habitat Mapping and Classification](01-habitat-mapping.md) —
  the backscatter and terrain attributes that accompany a hydrate survey.
- [15-04-03 Marine Minerals and Deep-Sea Mining Geophysics](03-marine-minerals.md) —
  the same resource arithmetic applied to a solid ore rather than a phase.
- [15-03-01 Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems](../03-seafloor-tectonics/01-mid-ocean-ridges.md) —
  the heat flow that sets the geotherm.
- [05-04-01 Porosity, Density and Velocity](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  the rock physics in full.
- [09-05-01 TEM Sounding](../../09-electrical-em-methods/05-em-methods-applications/01-tem-sounding.md) —
  the electromagnetic route to a resistive hydrate-bearing layer.
- [18-06-06 Decision Under Uncertainty](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md) —
  how to present an interval rather than a number.
