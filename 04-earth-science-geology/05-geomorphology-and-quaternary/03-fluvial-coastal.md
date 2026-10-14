---
id: 04-05-03
title: "Fluvial, Coastal and Aeolian Systems"
level: intermediate
prereqs: ["04-05-01", "04-03-04"]
estimated_minutes: 75
tags: [fluvial, coastal, aeolian, sediment-transport, shields, manning, waves, dunes]
---

# Fluvial, Coastal and Aeolian Systems

Water and wind sort sediment; ice does not. That single difference is why the
three systems in this lesson produce *layered, graded, permeable* deposits, and
why they matter far beyond geomorphology: the same sorting that makes a river
deposit a sand body is what makes that sand body an aquifer, a reservoir or a
placer. The shapes are consequences of transport mechanics, and the transport
mechanics are a small number of dimensionless groups — the Shields parameter, the
Rouse number, the Froude number, and for waves the ratio of depth to wavelength.

This lesson builds each system from its transport law, gives the quantitative
relations with units, and connects each deposit to the physical property that
makes it detectable. Where a relation is empirical (a drag correlation, a
threshold, a roughness coefficient), it is labelled as such and its limitations
are stated.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a settling velocity from a drag balance, state why Stokes' law
   fails for sand, and use the Rouse number to discriminate bedload from
   suspension.
2. **Compute** a Shields threshold and compare it with a bed shear stress from
   the depth–slope product, and explain grain-size sorting in a point bar.
3. **Use** Manning's equation to compute velocity and discharge in a channel, and
   explain the hydraulic-geometry sum rule $b + f + m = 1$.
4. **Solve** the linear wave dispersion relation, compute a shoaling
   amplification and a breaking depth from an energy-flux balance.
5. **Compute** an aeolian threshold friction velocity and a potential saltation
   flux, and state why a measured flux is almost always smaller.
6. **State** the Bruun rule and its assumptions, and say why it is a model rather
   than a physical law.
7. **Map** each deposit type to the property contrast it produces, and choose a
   geophysical method that can see it.

## Prerequisites

- [04-05-01 Landform Processes and Shapes](./01-landforms.md) — the mass-balance
  frame and the erosion law that transport laws feed.
- [04-03-04 Sedimentary Basins: Formation, Fill and Subsidence](../03-geologic-time-and-stratigraphy/04-sedimentary-basins.md)
  — where these deposits accumulate and how they are preserved.

---

## 1. Sediment transport in one page

Everything in this lesson is a variation on one balance: a *driving force*
proportional to a stress, against a *resisting force* proportional to weight.

**Settling.** For a grain falling at terminal velocity the drag balances the
submerged weight:

$$
v_s = \sqrt{\frac{4 d (\rho_s - \rho_f) g}{3 C_D \rho_f}},
$$

with $d$ the grain diameter [m], $\rho_s$ and $\rho_f$ the grain and fluid
densities [kg m⁻³], and $C_D$ the drag coefficient, which for a sphere is a
function of the Reynolds number $\mathrm{Re} = \rho_f v_s d/\mu$. This is implicit
in $v_s$ and is solved by iteration. Below $\mathrm{Re} \approx 1$ the drag law
becomes $C_D = 24/\mathrm{Re}$ and the expression collapses to **Stokes' law**,
$v_s = (\rho_s - \rho_f) g d^{2}/(18\mu)$.

**Onset of motion.** A grain on a bed moves when the bed shear stress exceeds a
threshold proportional to its submerged weight. Non-dimensionalised, this is the
**Shields parameter**

$$
\tau^{*} = \frac{\tau_b}{(\rho_s - \rho_f) g d},
\qquad \tau^{*}_c \approx 0.045,
$$

with $\tau_b$ the bed shear stress [Pa], given for steady uniform flow by the
depth–slope product $\tau_b = \rho_f g h S$.

**Suspension.** A grain stays in suspension when the upward turbulent velocity
fluctuations exceed its settling velocity. The ratio is the **Rouse number**

$$
P = \frac{v_s}{\kappa u_{*}}, \qquad u_{*} = \sqrt{\tau_b/\rho_f},
$$

with $\kappa \approx 0.40$ the von Kármán constant and $u_*$ the shear velocity
[m s⁻¹]. The conventional thresholds are $P > 2.5$ for bedload-dominated
transport, $1.2$–$2.5$ for roughly half the load in suspension, $0.8$–$1.2$ for
full suspension, and $P < 0.8$ for wash load. These thresholds are **conventions**,
not exact boundaries.

## 2. Fluvial channels

**Flow resistance.** For steady uniform flow the depth-averaged velocity is given
by **Manning's equation**

$$
V = \frac{1}{n} R_h^{2/3} S^{1/2},
$$

with $n$ the Manning roughness coefficient [s m$^{-1/3}$], $R_h = A/P$ the
hydraulic radius (area over wetted perimeter) and $S$ the energy slope. Discharge
follows as $Q = VA$ and the flow regime from the **Froude number**

$$
\mathrm{Fr} = \frac{V}{\sqrt{g h'}},
$$

where $h'$ is a depth scale (the hydraulic depth for a non-rectangular section).
$\mathrm{Fr} < 1$ is subcritical, $\mathrm{Fr} > 1$ supercritical.

**Hydraulic geometry.** Downstream of a given point, width, depth and velocity are
observed to scale as powers of discharge:

$$
W = aQ^{b}, \qquad D = cQ^{f}, \qquad V = kQ^{m}, \qquad b + f + m = 1 .
$$

The sum rule is not an empirical finding — it is continuity, $Q = WDV$. It is
therefore the first check to apply to any published set of exponents, and a set
that does not sum to one is misreported.

**Channel pattern and deposit.** Meandering channels build point bars with
fining-upward sequences (gravel → sand → silt/clay); braided channels build
sheet-like, sand-rich, mud-poor bodies; anastomosing and anastomosed systems keep
mud between channels. This architecture is the direct control on aquifer
connectivity and on reservoir quality, and it is what a ground-penetrating radar
or shallow-seismic survey of a floodplain actually images.

**Terraces.** A fluvial terrace is a former floodplain abandoned by incision. Its
*strath* or its alluvial fill is a datable surface and a palaeo-hydraulic record:
the fill grain size gives a palaeo-slope, the elevation gives the incision
history, and the geophysical expression is a soil-over-gravel contrast.

## 3. Coastal systems

**Linear wave theory.** For a wave of angular frequency $\omega$ in water of depth
$h$, the wavenumber $k$ satisfies

$$
\omega^{2} = gk\tanh(kh),
$$

which is implicit and is solved by iteration. Two limits matter:

- **Deep water** ($kh \gtrsim 3$): $c = \sqrt{g/k} = gT/2\pi$, dispersion is
  strong and long waves travel faster.
- **Shallow water** ($kh \lesssim 0.3$): $c = \sqrt{gh}$, non-dispersive, and
  refraction becomes geometry.

**Shoaling.** Conserving energy flux $E c_g$ with $E = \frac{1}{8}\rho g H^{2}$ as
a wave enters shallow water amplifies the height, roughly as $H \propto h^{-1/4}$
in the shallow limit (Green's law). The wave **breaks** when its height
approaches a fixed fraction of the local depth, the *breaker index*
$H_b/h_b \approx 0.78$ (an empirical value, and a parameterisation, not a
derived constant). Combining the two gives

$$
h_b^{5/2} = \frac{H_0^{2} c_{g0}}{\gamma^{2}\sqrt{g}},
$$

which is a *computed* result of the energy-flux assumption plus the *modelled*
breaker index.

**Longshore transport and the shoreline.** Once broken, waves drive a
longshore current and a littoral drift that moves sediment along the coast; the
local balance of that flux with the supply from rivers is what decides whether a
shoreline advances or retreats.

**The Bruun rule.** For a rising sea level, the widely quoted model is

$$
R = \frac{S\, L^{*}}{B + h^{*}},
$$

with $S$ the sea-level rise rate, $L^{*}$ the distance from the shoreline to the
closure depth, $B$ the berm height and $h^{*}$ the closure depth. It assumes that
the shoreface profile translates landward without changing shape and that sand is
conserved on the profile. It ignores longshore transport, supply, rock and
shoreline hardening. It is a *model*, it is stated here as one, and its answer is
linear in an assumed $L^{*}$.

## 4. Aeolian systems

**Threshold.** The wind moves a loose grain when the aerodynamic lift and drag
exceed its weight, expressed as a threshold friction velocity

$$
u_{*t} = A\sqrt{\frac{(\rho_s - \rho_a) g d}{\rho_a}},
$$

with $A \approx 0.1$ an empirically calibrated coefficient. Bagnold's form is
monotonic in $d$, so it does *not* reproduce the measured minimum near
$0.08$–$0.1$ mm; that minimum requires an added cohesive term, which is a model
input. Stating the failure is part of using the formula.

**Saltation flux.** Above the threshold, the saturated (potential) mass flux is
often written in Bagnold's form

$$
q = C \frac{\rho_a}{g} u_{*}^{3},
$$

with $C$ an empirical coefficient of order 1 to 2. Because $q \propto u_*^{3}$,
transport is extremely sensitive to wind speed, and because it is a *potential*
flux it is an upper bound: moisture, vegetation, armouring and limited supply all
reduce the real flux.

**Bedforms.** Ripples form near the threshold, dunes at several times it, and a
flat sand sheet at very high transport rates; the transition is controlled by the
ratio of the shear velocity to the threshold and by the saturation length — the
distance over which the flux adjusts to a new bed. Dune spacing scales with dune
height, so a dune field is a self-organising pattern with a characteristic
wavelength that a topographic or radar survey measures directly.

**Loess.** Wind-blown silt deposited beyond the sand-transport limit. It is a
first-order Quaternary archive (a loess–palaeosol sequence is a climate
stratigraphy), it is a slope-stability hazard when wet, and its low density and
low susceptibility make it a distinctive and mappable unit.

## 5. From deposit to detectable contrast

This is the section that connects the geomorphology to the geophysics. For each
deposit, the physical property that differs and the method that responds to it:

| Deposit | Property contrast | Typical method |
|---|---|---|
| Channel sand in floodplain mud | Resistivity, permittivity, shear modulus | ERT, EM, GPR, surface waves |
| Basal gravel of a terrace | Density, P-wave velocity, resistivity | Seismic refraction, gravity, ERT |
| Sand-and-gravel aquifer | Resistivity (fresh vs saline), permittivity | ERT, TEM, GPR |
| Deltaic mud wedge | Resistivity (low), velocity (low), density (low) | EM, seismic reflection, gravity |
| Coastal sand barrier | Density and velocity against underlying mud | Refraction, surface waves, GPR |
| Dune sand (dry) | Very high resistivity; radar-transparent | GPR, ERT |
| Dune sand (saturated) | Resistivity drops; velocity rises | GPR, ERT, refraction |
| Loess | Low density, low susceptibility, low resistivity | Gravity, magnetics, ERT |
| Placer (heavy minerals) | Density (high), susceptibility (high) | Gravity, magnetics |
| Beachrock / cemented horizon | Velocity (high), resistivity (high) | Seismic refraction, ERT |

The point of the table is that no single method sees everything. A channel sand
body is nearly invisible to gravity but obvious to ERT and GPR; a placer is the
reverse. Matching method to contrast is the first design decision of any survey.

## 6. Quantitative treatment with units

| Quantity | Symbol | Unit | Value used here (MODELLED) |
|---|---|---|---|
| Grain and fluid densities | $\rho_s$, $\rho_f$ | kg m⁻³ | 2650, 1000 (water), 1.225 (air) |
| Dynamic viscosity of water | $\mu$ | Pa s | $1.002\times10^{-3}$ |
| Shields critical value | $\tau^{*}_c$ | – | 0.045 |
| Manning roughness | $n$ | s m$^{-1/3}$ | 0.030 |
| Breaker index | $\gamma$ | – | 0.78 |
| von Kármán constant | $\kappa$ | – | 0.40 |
| Bagnold coefficients | $A$, $C$ | – | 0.10, 1.75 |

**Worked check 1 (settling).** For $d = 0.25$ mm quartz in water the drag balance
gives $v_s = 0.03397$ m s⁻¹ at $\mathrm{Re} = 8.48$, while Stokes' law gives
$0.05609$ m s⁻¹ — an error of $+65$ per cent. Stokes' law is a $\mathrm{Re} \ll 1$
result and sand is not in that regime.

**Worked check 2 (threshold).** For $d = 0.15$ mm,
$\tau_c = 0.045 \times 1650 \times 9.81 \times 1.5\times10^{-4} = 0.109$ Pa. A
flow of $h = 2$ m at $S = 3\times10^{-4}$ has
$\tau_b = 1000 \times 9.81 \times 2 \times 3\times10^{-4} = 5.89$ Pa, a ratio of
54. The bed is mobile, and it is the *ratio* that matters, which is why a finer
bed moves first at the same stress.

**Worked check 3 (waves).** A 2 m, 8 s swell has $c_0 = gT/2\pi = 12.49$ m s⁻¹ and
$c_{g0} = 6.246$ m s⁻¹. Then
$h_b^{5/2} = 4 \times 6.246 / (0.78^{2}\sqrt{9.81}) = 13.11$, so
$h_b = 2.80$ m and $H_b = 2.18$ m. The surf zone is about 120 m wide on a 1:50
slope, and it is where the littoral drift is generated.

## 7. Assumptions and regime of validity

1. **Drag balance** assumes a sphere, steady fall, no grain interaction and no
   shape or surface-roughness effect. Natural grains are irregular and settle
   10–30 per cent slower than the equivalent sphere.
2. **Stokes' law** is valid for $\mathrm{Re} \ll 1$, i.e. clay and fine silt. For
   sand it overestimates by a factor of 2 to 40 across the sand range.
3. **Shields** assumes non-cohesive, uniform, loose grains on a flat bed with
   steady flow. Cohesion, armouring, bioturbation and unsteady flow all shift it.
4. **Manning's $n$** is a lumped parameter that hides bedform roughness, bank
   roughness and vegetation. It is calibrated, not measured.
5. **Hydraulic geometry** exponents are site and regime specific.
6. **Linear wave theory** assumes irrotational, incompressible, inviscid flow, a
   small wave steepness $H/L$, and a horizontal bed. It fails in the surf zone
   itself, which is where the transport is largest.
7. **The breaker index** is empirical and varies with beach slope and wave
   steepness; 0.78 is a nominal value for a plane slope.
8. **Bagnold's flux** is a potential flux for dry, loose, unbounded sand.
9. **The Bruun rule** is a two-dimensional, conservative model.
10. **All property ranges are nominal.** A survey must measure its own.

## 8. Python demonstration

[`code/fluvial_coastal_demo.py`](./code/fluvial_coastal_demo.py) computes the
settling velocity from the drag balance and compares it with Stokes, the Shields
thresholds and the bed mobility ratios, Manning flow with the hydraulic-geometry
rule, the wave dispersion relation and the breaking depth, the Rouse number, the
aeolian threshold and potential flux, and the Bruun rule.

```text
   d (mm)     v_drag (m/s)   Re     C_D    v_Stokes (m/s)  Stokes error
   0.2500        0.03397    8.48   4.676        0.05609      +65.12 per cent
   1.0000        0.15502  154.71   0.898        0.89746     +478.94 per cent
  COMPUTED for 0.25 mm quartz sand: v = 0.03397 m/s (3.397 cm/s), Re = 8.48, C_D = 4.676
    h =  2.0 m, S = 3.0e-04: tau = 5.8860 Pa
        fine sand 0.15 mm     : tau/tau_c =  53.872  moves
        gravel 10 mm          : tau/tau_c =   0.808  static
   width(m) depth(m)  slope     R_h(m)   V(m/s)   Q(m^3/s)   Fr
        50      2.0 5.0e-04    1.852    1.124      112.40   0.254
     8.0  100.0   0.06288    99.92    12.490      12.490    6.288
     8.0    5.0   0.11837    53.08     6.635      12.490    0.592
    H0 =  2.0 m, T =  8.0 s: h_b =  2.80 m, H_b =  2.18 m, H_b/h_b = 0.78
    medium sand 0.35 mm   : w_s =  0.05227 m/s, P =   2.613  bedload dominated
    fine sand 0.15 mm     : w_s =  0.01588 m/s, P =   0.794  wash load (essentially all in suspension)
    d = 0.2500 mm: u*t = 0.2303 m/s (23.03 cm/s)
    u* = 0.35 m/s: q = 0.00937 kg/(m s) =    295.7 t/(m yr) =     184.8 m^3/(m yr)  (potential)
    S =  2.0 mm/yr, L* =   5000 m, B = 1 m, h* =  15 m: R = 0.6250 m/yr
```

### What to observe

- The Stokes error grows from 5 per cent at 0.0625 mm to more than 4000 per cent
  at 5 mm. The failure is not subtle, and it is systematic in the direction that
  makes fine material look coarser than it is in a settling analysis.
- At $10^{-4} \le \theta \le 0.045$: the mobility ratio barely changes along the
  channel, but between grain sizes it changes by a factor of 500. Sorting is a
  threshold phenomenon, not a flux phenomenon.
- The dispersion table recovers $c = gT/2\pi$ to three figures in deep water and
  drops to 6.6 m s⁻¹ in 5 m of water for the same 8 s period. Refraction of swell
  is entirely a consequence of this one number changing.
- The potential aeolian flux is 185 m³ m⁻¹ yr⁻¹ at $u_* = 0.35$ m s⁻¹, which is
  a saturated value; a real dune field transports a fraction of it. The demo
  labels it *potential* for exactly this reason.

## 9. Common mistakes

1. **Using Stokes' law for sand.** It is a $\mathrm{Re} \ll 1$ result.
2. **Quoting a Shields threshold as an absolute stress.** It is a dimensionless
   ratio; the stress depends on the grain.
3. **Comparing a shear stress with a critical shear stress for a different grain
   size.** The comparison is only meaningful within one size class.
4. **Treating a Manning $n$ as a material property.** It is a calibration, and it
   absorbs everything the equation does not represent.
5. **Quoting hydraulic-geometry exponents that do not sum to one.** Continuity
   forbids it.
6. **Confusing the deep-water wavelength with the local wavelength.** Shoaling
   changes both.
7. **Using the breaker index as a derived constant.** It is empirical.
8. **Reading a sea-level rise into shoreline retreat without the profile
   assumptions.** The Bruun rule is a model, and it fails on rocky or
   supply-limited coasts.
9. **Treating a potential aeolian flux as a site flux.** It is an upper bound.
10. **Assuming a sand body is a single body.** Point bars, channel fills and
    overbank deposits are interbedded, and the *connectivity*, not the total sand
    fraction, controls flow.

## 10. Real-world applications

- **Alluvial aquifers and riverbank filtration.** Channel and point-bar sands are
  the highest-permeability units in a floodplain and are the first target of any
  groundwater investigation ([14-01-03 Hydraulic Head and Darcy's Law](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/03-hydraulic-head-darcy.md)).
- **Reservoir architecture.** Fluvial and deltaic bodies are the classic clastic
  reservoirs; the geobodies of §2 are the flow units of a field development
  ([11-03-03 Reservoir Characterisation](../../11-exploration-geophysics/03-hydrocarbon-exploration/03-reservoir-characterisation.md)).
- **Coastal hazard and shoreline management.** Wave climate, breaking depth,
  littoral drift and the Bruun response are the standard inputs to a shoreline
  management plan ([15 Oceanography and Marine Geophysics](../../15-oceanography-marine/README.md)).
- **Desertification and dust.** Threshold friction velocity and potential flux are
  the physics behind wind-erosion models and dust-emission inventories, and the
  mineral dust itself is mapped from orbit
  ([17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md)).
- **Placer and heavy-mineral exploration.** Density and susceptibility contrasts
  in a beach or channel placer are what gravity and magnetics detect
  ([04-06-02 Mineral Deposit Types](../06-petroleum-and-mineral-systems/02-mineral-deposits.md)).
- **Flood hazard.** Hydraulic geometry plus Manning's equation is the basis of
  every stage–discharge rating curve and flood-frequency estimate.
- **Palaeoclimate from loess and dunes.** Loess–palaeosol sequences and dune
  activity records are dated archives of Quaternary wind strength and aridity.

## 11. Further reading

- **Dingman, S. L. *Fluvial Hydrology* (Waveland).** Manning's equation,
  hydraulic geometry and the transport relations with their measured ranges.
  Level: undergraduate to graduate.
- **Van Rijn, L. C. *Principles of Sediment Transport in Rivers, Estuaries and
  Coastal Seas* (Aqua).** The standard engineering reference for all of §1–§3.
  Level: professional.
- **Soulsby, R. *Dynamics of Marine Sands* (Thomas Telford).** Wave and current
  bed shear stress, threshold, and the empirical relations with their
  coefficients. Level: professional.
- **Bagnold, R. A. *The Physics of Blown Sand and Desert Dunes* (Dover reprint).**
  The origin of the flux law of §4. Level: classic monograph.
- **Kok, J. F., & others (2012). The physics of wind-blown sand and dust.**
  *Reports on Progress in Physics*. Level: advanced review; the modern statement
  of what §4 simplifies.
- **Masselink, G., Hughes, M., & Knight, J. *Introduction to Coastal Processes
  and Geomorphology* (Routledge).** Surf-zone processes and shoreline response.
  Level: undergraduate.
- **Nichols, G. *Sedimentology and Stratigraphy* (Wiley).** The deposit-scale
  architecture that §5 maps onto property contrasts. Level: undergraduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [01 Landform Processes and Shapes](./01-landforms.md) — the hillslope and
  channel-incision laws that deliver sediment to these systems.
- [02 Glacial and Periglacial Landforms and Sediments](./02-glacial-landforms.md)
  — the unsorted end of the sediment spectrum.
- [04 Quaternary Climate Change and Landscape Records](./04-quaternary-climate.md)
  — the climate record that terraces, loess and dunes preserve.
- [05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)
  — the elastic and electrical relations behind the table in §5.
- [14-03 Petrophysics for Hydrology](../../14-hydrology-hydrogeophysics/03-petrophysics-hydrology/README.md)
  — porosity, permeability and saturation relations for the units found here.
- [15 Oceanography and Marine Geophysics](../../15-oceanography-marine/README.md)
  — waves and currents at the scale of a shelf.
- [10-03-01 GPR Hydrogeology](../../10-gpr-near-surface/03-gpr-applications/01-gpr-hydrogeology.md)
  — imaging a channel sand body with radar.

Exercises:
[`exercises/03-fluvial-coastal-exercises.md`](./exercises/03-fluvial-coastal-exercises.md)
and
[`exercises/03-fluvial-coastal-solutions.md`](./exercises/03-fluvial-coastal-solutions.md).

## Self-assessment checklist

- [ ] I can write the drag balance and explain why it must be solved
      iteratively. (§1)
- [ ] I can state the Reynolds-number limit of Stokes' law and quantify its
      error for sand. (§1, §6)
- [ ] I can compute a Shields threshold and a bed shear stress and interpret
      their ratio. (§1, §6)
- [ ] I can compute a Rouse number and name the regime. (§1)
- [ ] I can use Manning's equation and explain the hydraulic-geometry sum rule.
      (§2)
- [ ] I can solve $\omega^{2} = gk\tanh(kh)$ and identify the deep and shallow
      limits. (§3)
- [ ] I can compute a breaking depth from an energy-flux balance. (§3, §6)
- [ ] I can state the Bruun rule and two reasons it fails. (§3, §7)
- [ ] I can compute an aeolian threshold and say why Bagnold's form misses the
      observed minimum. (§4)
- [ ] For any deposit in §5 I can name the contrast and choose a method.
