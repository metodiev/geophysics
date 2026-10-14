---
id: 04-07-04
title: "Subsidence, Sinkholes and Karst"
level: intermediate
prereqs: ["04-01-05", "04-06-04", "04-04-01"]
estimated_minutes: 75
tags: [subsidence, karst, sinkholes, effective-stress, compaction, insar, microgravity]
---

# Subsidence, Sinkholes and Karst

Subsidence is the least dramatic geological hazard and the most expensive one,
because it happens slowly over the largest area. A metre of regional lowering is
not an event; it is a decade of damage distributed over every foundation,
pipeline, drain and railway in a basin, and it is measured in money rather than
in casualties. Sinkholes are its violent opposite: a void that has been growing
for hundreds of thousands of years collapses in an afternoon, and the damage is
concentrated on one address.

Both are consequences of the same mechanics. The ground lowers when the
**effective stress** in a compressible layer increases, and it collapses when a
void's roof can no longer span the void. This lesson derives both, and it
identifies which measurement bears on which part: water level and compressibility
for the slow part, and void geometry for the fast one — where the honest
conclusion is that the relevant geometry is usually the quantity nobody has
measured.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the effective-stress increase produced by a decline in hydraulic
   head, and compute the compaction of a clay layer in both of the forms used in
   practice: a constrained modulus and a compression index.
2. **Explain** why the two forms can differ by a factor of three for the same
   head decline, and what extra information the logarithmic form requires.
3. **Derive** the free-air gradient from $g = GM/r^2$ and distinguish it from the
   conventional free-air coefficient, stating why they differ.
4. **Compute** the Bouguer and residual gravity gradients and state which
   quantity a borehole gravimeter measures.
5. **Derive** a karst denudation rate from a dissolved-load mass balance and
   compute the time required to remove a void of a given size.
6. **Compute** the residual gravity change produced by a water-level decline and
   separate it from the free-air term, with attention to the sign convention.
7. **Derive** the InSAR phase change for a line-of-sight displacement, compute
   the sensitivity, and solve two look geometries for vertical and horizontal
   motion.
8. **State** the assumptions in each calculation and identify which of them a
   geophysical measurement cannot test.

## Prerequisites

- [04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
  — porosity, saturation and compressibility, the three properties that decide
  how much a layer compacts.
- [04-06-04 Aquifer Types and Groundwater Occurrence](../06-petroleum-and-mineral-systems/04-groundwater-aquifers.md)
  — confined and unconfined aquifers, storativity and the response of a water
  level to pumping, which is the forcing term in §2.
- [04-04-01 Stress, Strain and Brittle vs Ductile Deformation](../04-structural-geology/01-stress-strain-rocks.md)
  — effective stress and the difference between elastic and irrecoverable
  volumetric strain.

## 1. What subsides, and why

Three mechanisms account for nearly all observed ground lowering.

**Compaction of a compressible layer.** A clay or silt layer loses volume
irrecoverably when the effective stress on it increases. This is the dominant
mechanism in deltas and sedimentary basins, where the layer was deposited under
a load and has not finished consolidating.

**Dissolution.** Limestone, dolomite, gypsum and halite dissolve in
groundwater. The rock is removed in solution rather than compacted, and the
removal is slow — the subject of §5 — but it is what makes the void that
eventually collapses.

**Fluid withdrawal from a reservoir at depth.** Oil and gas reservoirs compact
as their pore pressure falls; the same effective-stress arithmetic applies, with
a much larger depth and a much stiffer rock.

The first and third are the same calculation with different numbers, and the
second is the subject of a different one. What all three share is that the
measurable quantities are **water level**, **compressibility** and
**geometry** — and of the three, only the first is easy to measure.

## 2. Effective stress and compaction, derived

Terzaghi's principle is that deformation responds to the effective stress
$\sigma' = \sigma - u$. When the hydraulic head in a confined aquifer falls by
$\Delta h$, the pore pressure falls by $\rho_w g\Delta h$ and the effective
stress rises by the same amount, because the total stress is unchanged:

$$\Delta\sigma' = \rho_w g \,\Delta h . \tag{1}$$

For $\Delta h = 5$ m, $\Delta\sigma' = 1000\times9.807\times5 = 49.0$ kPa.
That is a small stress by the standards of rock mechanics and a large one by the
standards of a soft clay, which is why the compaction is concentrated in the
softest layer.

The strain that follows depends on the constitutive relation, and practice uses
two forms.

**A constrained modulus.** Define the coefficient of volume compressibility
$m_v$ as the strain per unit effective stress in one-dimensional compression,
$m_v = 1/E_\mathrm{oed}$. Then

$$\Delta H = m_v \,\Delta\sigma' \,H_0 . \tag{2}$$

Equation (2) is a *definition* rather than a model: $m_v$ is measured in an
oedometer test, and (2) is what "measured in an oedometer" means. The values
differ between clays by more than an order of magnitude, so (2) is only as good
as the test. For a 30 m clay with $m_v = 0.5$ m² MN⁻¹ and a 5 m head decline,
$\Delta H = 0.5\times0.049\times30 = 0.74$ m — three quarters of a metre from
five metres of drawdown.

**A compression index.** For a normally consolidated clay, the void ratio falls
linearly against the *logarithm* of effective stress:

$$\Delta H = \frac{C_c}{1+e_0}\,H_0
\log_{10}\!\left(\frac{\sigma'_0 + \Delta\sigma'}{\sigma'_0}\right), \tag{3}$$

with $C_c$ the compression index and $e_0$ the initial void ratio, both
measured. The logarithmic form encodes the two facts that make compaction hard
to forecast: the response is **irreversible** (a reloading curve has a much
smaller slope than the loading curve) and **history-dependent** (a clay that has
already carried a larger load — an over-consolidated clay — barely compresses
until that pre-consolidation stress is exceeded).

The two forms differ substantially for the same input. The same 5 m of drawdown
over the same 30 m of clay gives 0.15 m, 0.74 m or 2.21 m depending on whether
$m_v$ is 0.1, 0.5 or 1.5 m² MN⁻¹, and 1.34 m or 0.43 m depending on whether the
pre-consolidation stress is 50 or 200 kPa (with $C_c = 0.3$ and $e_0 = 1.0$,
both NOMINAL, in (3)).
**A subsidence forecast is therefore a statement about a laboratory test and a
stress history, and no geophysical method supplies either.** What geophysics
supplies is the geometry: where the compressible layer is, how thick, and how it
varies laterally.

## 3. Gravity gradients, derived

Subsidence is measured by levelling, GNSS or InSAR. The *mass* that moved is
measured by gravity, and the two must be separated carefully, because a vertical
displacement produces a gravity change on its own.

**The free-air gradient.** Differentiate $g = GM/r^2$:

$$\frac{\mathrm{d}g}{\mathrm{d}z} = -\frac{2GM}{r^3} = -\frac{2g}{R} . \tag{4}$$

With $g = 9.80665$ m s⁻² and $R = 6.371\times10^6$ m this is
$-3.0785\times10^{-6}$ m s⁻² per metre, i.e. $0.30785$ mGal m⁻¹ or
$3.0785$ µGal cm⁻¹.

The conventional free-air coefficient, **0.3086 mGal m⁻¹**, differs from this
by 0.25 per cent, and the difference is not an error in (4). The conventional
value is the gradient of the *normal* gravity field on the ellipsoid — the
Somigliana formula — which contains the flattening and a latitude dependence
that $2g/R$ does not. Use the conventional value to reduce a survey; use (4)
when you need to know why the number is what it is.

**The Bouguer slab.** A slab of density $\rho$ and thickness $h$ attracts
downward with $\Delta g = 2\pi G\rho h$, so the Bouguer correction per metre is
$2\pi G\rho$. For $\rho = 2670$ kg m⁻³ it is 0.11197 mGal m⁻¹. Combining the two
gives the **residual gradient** in uniform rock,

$$\frac{\mathrm{d}g}{\mathrm{d}z}\bigg|_\mathrm{residual}
= \frac{2g}{R} - 2\pi G\rho = 0.19588\ \mathrm{mGal\,m^{-1}} \tag{5}$$

for $\rho = 2670$ kg m⁻³. That is what a borehole gravimeter measures in
uniform rock, and the amount by which the measurement departs from it is the
density — which is why borehole gravity is a densimeter, and why it is the
standard way to find a density inversion that a sonic log cannot see.

## 4. The mass change, and the sign convention

Now consider the observation that a subsidence monitoring programme actually
makes: gravity is measured repeatedly at benchmarks whose elevation is also
measured. Two effects add.

*The free-air effect.* If the ground lowers by $\Delta h$, a benchmark set in the
ground lowers with it and moves toward the centre, where $g$ is larger. The
free-air contribution is **positive**:

$$\Delta g_\mathrm{FA} = \frac{2g}{R}\Delta h . \tag{6}$$

For $\Delta h = 5$ m, $\Delta g_\mathrm{FA} = +1539$ µGal. This is a large
number, and it is not a mass change.

*The mass effect.* If the lowering is caused by draining pore water from a layer
of porosity $\phi$, the layer loses mass and gravity falls. With the draining
treated as a slab of density change $-\phi\rho_w$ over a thickness $\Delta h$:

$$\Delta g_\mathrm{mass} = -2\pi G\,\phi\rho_w\,\Delta h . \tag{7}$$

For $\phi = 0.30$ and $\Delta h = 5$ m, $\Delta g_\mathrm{mass} = -62.9$ µGal.

The measured change is the sum, $+1476$ µGal, and it is the residual after
removing the free-air term that reports the mass loss. Two remarks:

- **The sign convention is the commonest error in 4-D microgravity.** The
  free-air term is positive because the ground went down; the mass term is
  negative because water left. Reporting "gravity decreased, so the ground
  subsided" is right for the wrong reason and gives the wrong magnitude, since
  the free-air term dominates by a factor of 24.
- **The mass term is proportional to the porosity**, and the free-air term is
  not. That is the diagnostic: the residual gravity change divided by the
  elevation change gives $\phi$, and the same measurement at a borehole
  gravimeter gives it with depth resolution. Microgravity detects a water-level
  decline of about 0.4 m at a repeatability of 5 µGal for $\phi = 0.3$, which is
  the sensitivity that makes the method useful for monitoring rather than only
  for inventory.

## 5. Karst: dissolution as a mass balance

Karst is what happens to a soluble rock with a through-flowing groundwater
system. The denudation rate follows from a mass balance over a catchment,
without any kinetics at all. Over an area $A$ with recharge $P$ (a depth per
year) carrying a dissolved load concentration $c$ (mass per volume), the mass
removed per year is $cPA$; the rock volume removed is that divided by the rock
density; and the lowering rate is that divided by $A$:

$$D = \frac{c\,P}{\rho_\mathrm{rock}} . \tag{8}$$

All three quantities are measured, and none of them comes from a model. With
$c = 100$ mg L⁻¹, $P = 0.5$ m a⁻¹ and $\rho = 2700$ kg m⁻³,
$D = 1.85\times10^{-5}$ m a⁻¹ = 18.5 mm ka⁻¹ = 18.5 m Ma⁻¹.

The consequence is the shape of the hazard. Removing a 10 m void takes

$$t = \frac{10\ \mathrm{m}}{1.85\times10^{-5}\ \mathrm{m\,a^{-1}}}
= 5.4\times10^5\ \mathrm{a}, \tag{9}$$

half a million years. **Karst is a landscape built by a slow process, and a
sinkhole is the instantaneous failure of a void that has existed for
geological time.** The hazard is therefore not the dissolution rate; it is the
distribution, size and roof thickness of the voids that already exist — which is
a geophysical question, and specifically a microgravity, GPR and resistivity
question.

## 6. Void stability, and an honest warning

The temptation is to compute a critical void span. A crude model: treat the roof
as a simply supported beam of unit width, thickness $t$, spanning $D$, loaded by
its own weight $w = \rho g t$. Then $M = wD^2/8$, the extreme fibre stress is
$\sigma = 6M/t^2 = 3\rho gD^2/(4t)$, and setting $\sigma$ equal to a tensile
strength $\sigma_t$ gives a critical span

$$D_c = \sqrt{\frac{4\sigma_t t}{3\rho g}} . \tag{10}$$

For $t = 3$ m, $\sigma_t = 20$ kPa and $\rho = 1800$ kg m⁻³ this gives
$D_c = 2.13$ m. The scaling it exposes is real — $D_c$ grows as the square root
of both the roof thickness and the tensile strength, so doubling the thickness
buys only 41 per cent more span — but **every assumption in the model is
wrong**: a soil roof carries load by arching rather than bending, tensile
strength is not a soil property in the engineering sense, the water table (the
actual control on soil strength) does not appear at all, and the geometry of a
real cavity is not a beam.

The model is included here to make a point that is worth more than the formula:
**a critical span can be computed and still be useless.** Sinkhole prediction is
not a solved problem, and the honest deliverable of a geophysical survey is a
map of *where voids and cavities are*, plus a map of *where the roof is thin*,
not a predicted date.

## 7. Measuring the ground from a satellite: InSAR

InSAR measures the phase of a radar echo, and a change in the round-trip path
length $r$ changes the phase by

$$\Delta\phi = \frac{4\pi\,\Delta r}{\lambda} , \tag{11}$$

the factor of 4π because the path is traversed twice and the phase is $2\pi$ per
wavelength. At a C-band wavelength of 5.56 cm, one fringe ($2\pi$) is
$\lambda/2 = 2.78$ cm of line-of-sight motion, and 1 cm gives 2.26 rad or 0.36
of a fringe.

Two consequences are structural rather than incidental.

**The measurement is one-dimensional.** If the surface moves vertically by
$u_z$ and the satellite looks at incidence angle $\theta$ from the vertical, the
line-of-sight component is

$$u_\mathrm{LOS} = u_z\cos\theta . \tag{12}$$

At $\theta = 39^\circ$ this is 0.777, so a centimetre of vertical motion appears
as 0.78 cm of path change. A displacement that is purely horizontal and
perpendicular to the look direction produces **no phase change at all**.

**Two geometries resolve it.** With an ascending and a descending track,
$u_\mathrm{LOS}^\mathrm{asc} = u_z\cos\theta + u_h\sin\theta$ and
$u_\mathrm{LOS}^\mathrm{desc} = u_z\cos\theta - u_h\sin\theta$, so

$$u_z\cos\theta = \tfrac12\left(u_\mathrm{LOS}^\mathrm{asc}
+ u_\mathrm{LOS}^\mathrm{desc}\right), \qquad
u_h\sin\theta = \tfrac12\left(u_\mathrm{LOS}^\mathrm{asc}
- u_\mathrm{LOS}^\mathrm{desc}\right). \tag{13}$$

For a pair of measurements of $+2.0$ cm and $-1.0$ cm at $\theta = 39^\circ$,
$u_z = 0.64$ cm and $u_h = 2.38$ cm: **the motion is mostly horizontal**, and a
single track would have reported a small vertical displacement and missed the
larger horizontal one. This is the standard reason that a monitoring programme
uses two geometries and a GNSS network to fix the reference frame.

## 8. Physical interpretation

- **Effective stress is the only variable that drives compaction.** Total stress
  changes do nothing to a saturated layer until the pore pressure responds, and
  the pore pressure responds on the timescale of the layer's permeability. That
  is why subsidence follows drawdown with a lag of months to years.
- **Compaction is irreversible** for a normally consolidated clay. Removing the
  load afterwards does not restore the ground; the void ratio follows a
  reloading curve with a slope an order of magnitude smaller.
- **Free air is not mass.** Two thirds of a 4-D microgravity time series in a
  subsiding basin is the free-air term from the elevation change, and no
  interpretation is possible without the elevation.
- **Dissolution removes mass; compaction does not.** They have opposite gravity
  signatures at constant elevation — one is a mass loss, the other is a volume
  loss — which is why gravity helps to tell a dissolving limestone from a
  compacting clay.
- **A void is an absence of mass**, so its gravity anomaly is negative, compact
  and much smaller than its dimensions: a 3 m cavity at 3 m depth in soil
  produces a signal at the limit of what a careful survey can resolve, and the
  depth is what makes it hard.

## 9. Units and dimensional analysis

| Quantity | Expression | Units |
|---|---|---|
| Effective-stress change | $\rho_w g\Delta h$ | kg m⁻³ × m s⁻² × m = Pa |
| Compaction (modulus form) | $m_v\Delta\sigma' H$ | (m² N⁻¹)(N m⁻²)(m) = m |
| Compression-index term | $C_c H\log_{10}(\cdot)/(1+e_0)$ | dimensionless × m = m |
| Free-air gradient | $2g/R$ | (m s⁻²)/m = s⁻² |
| Bouguer gradient | $2\pi G\rho$ | m³ s⁻² kg⁻¹ × kg m⁻³ = s⁻² |
| Denudation rate | $cP/\rho_\mathrm{rock}$ | (kg m⁻³)(m a⁻¹)/(kg m⁻³) = m a⁻¹ |
| InSAR phase | $4\pi\Delta r/\lambda$ | m/m = dimensionless (rad) |
| Line-of-sight component | $u_z\cos\theta$ | m |

The free-air and Bouguer gradients are both accelerations per metre, so their
difference is a gradient in the same units, and the residual in (5) is a genuine
difference of physical effects rather than of conventions. The compression-index
term in the table is dimensionless only because a logarithm of a ratio is; the
ratio's units cancel, which is why the pre-consolidation stress must be quoted
in the same units as the stress increment.

## 10. Assumptions and regime of validity

1. **One-dimensional consolidation** in (2) and (3). The strain is vertical and
   lateral strain is zero, which is the oedometer condition and a fair
   approximation under a wide load.
2. **Terzaghi's effective stress** in (1). It holds for soils and porous rocks
   with a connected pore network; it fails in unsaturated soils, where matric
   suction rather than a pore pressure controls the stress state.
3. **A homogeneous compressible layer** in (2) and (3). Real basins are layered,
   and the subsidence is dominated by the softest layer, often one that a
   seismic section sees only as a discontinuity in velocity.
4. **A constant $m_v$ or $C_c$** over the stress range. Both depend on the stress
   level, the stress history and the strain rate — secondary compression
   continues for decades after the primary phase, and it is what makes very long
   records of subsidence impossible to fit with a single parameter.
5. **A slab approximation** in (7). A local density change is not an infinite
   slab, and near the edge of a subsidence bowl the finite extent matters.
   The slab is the standard approximation and it is stated as one.
6. **The two-layer, $2\pi G\rho h$ and $\cos\theta$ geometry** in §7. A real
   orbit has a heading and a squint, and the look vector must be computed per
   pixel from the imaging geometry rather than taken as a global $\theta$.
   Horizontal motion in the along-track direction is invisible to a single
   geometry and requires the two-track combination (13).
7. **Phase unwrapping and coherence** in §7. Subsidence faster than a fringe per
   revisit wraps, and the inversion needs a velocity model or a longer
   wavelength (L-band) to keep the gradient between adjacent pixels below
   $\pi$. Decorrelation over vegetation removes the measurement entirely.
8. **A planar cavity roof** in (10). See §6: the model is a warning, not a
   method.

## 11. Python demonstration

[`code/subsidence_sinkholes_demo.py`](./code/subsidence_sinkholes_demo.py)
computes the effective stress, both compaction forms, the gravity gradients,
the karst denudation, the InSAR sensitivity and the residual gravity. Every
parameter is labelled NOMINAL.

The compaction forms, side by side:

```text
     m_v (m^2/MN)   dH (m)   dH (mm)
           0.10    0.1471      147.1
           0.50    0.7355      735.5
           1.50    2.2065     2206.5
```

```text
     sig'_0 (kPa)   dH (m)
          50.0    1.3356
         100.0    0.7798
         200.0    0.4285
```

The gradient, and the residual that a borehole gravimeter measures:

```text
  -2g/R = -3.078528e-06 (m/s^2) per m
  = 0.30785 mGal per metre = 3.0785 microgal per cm
  ... the conventional value is the gradient of the NORMAL gravity field ...
  For rho = 2670 the Bouguer term is 0.1119 mGal/m, so the combined
  free-air minus Bouguer gradient is 0.19588 mGal/m.
```

And the sign convention, which is the point of §4:

```text
  mass term  2 pi G drho dh = -6.290380e-07 m/s^2 = -62.904 microgal
  free-air term from the surface declining by the same 5.0 m = 1539.264 microgal
  ...
  The measured change is the sum, 1476.4 microgal,
  and it is the residual after removing the free-air term that reports
  the mass loss.
```

### What to observe

- The same 5 m of drawdown gives 0.15 m, 0.74 m or 2.21 m of subsidence
  depending only on $m_v$, and 1.34 m or 0.43 m depending on the
  pre-consolidation stress. The *forcing* is measured; the *response* is a
  property of a specific layer at a specific place, and a forecast without a
  test of that layer is a forecast of nothing.
- The free-air term is $+1539$ µGal and the mass term is $-63$ µGal. Their ratio
  is 24, and it is set by the ratio of $2g/R$ to $2\pi G\phi\rho_w$ — a
  dimensionless group of constants and the porosity. Any 4-D gravity
  interpretation that does not remove the free-air term is measuring the
  elevation change, not the mass change.
- The Bouguer term for $\rho = 2670$ kg m⁻³ is 0.112 mGal m⁻¹ and the free-air
  gradient is 0.308 mGal m⁻¹, so the residual is 0.196 mGal m⁻¹. Almost exactly
  two thirds of the free-air gradient is cancelled by the rock: this near
  cancellation is why borehole gravity is sensitive to *departures* from a
  uniform density rather than to the rock itself.
- The InSAR fringe value of 2.78 cm is a hard limit on measurable motion between
  revisits, and it is a *relative* limit: a steady 2 cm per year is easy to
  track over a year and impossible to see in a single interferogram pair over a
  week.

## 12. Common mistakes

1. **Ignoring the free-air term in 4-D microgravity.** It dominates by an order
   of magnitude and has the opposite sign to the mass effect.
2. **Using the total stress in a compaction calculation.** Compaction responds
   to effective stress; pumping does not change the total stress.
3. **Using a single $m_v$ for a layered sequence.** The softest layer usually
   dominates the total, and its thickness is often inferred from a geophysical
   log rather than cored.
4. **Quoting the free-air gradient as $2g/R$ when reducing a survey.** The
   conventional coefficient is 0.3086 mGal m⁻¹, and the 0.25 per cent
   difference matters at the microgal level.
5. **Expecting the ground to recover.** For a normally consolidated clay the
   compaction is irrecoverable; recharging the aquifer restores the pressure and
   not the elevation.
6. **Treating a dissolution rate as a sinkhole forecast.** The rate gives the
   timescale of the void, not the date of its collapse.
7. **Reporting an InSAR displacement without the look geometry.** A line-of-sight
   displacement of 2.8 cm could be nearly all vertical or nearly all horizontal.
8. **Assuming a subsidence bowl is centred on the pumping well.** It is not: the
   bowl is centred where the compressible layer is thickest, which is a
   geological question.
9. **Taking a karst denudation rate from a concentration measured in a losing
   stream.** The concentration is not the catchment-average value, and the
   difference can be a factor of several.
10. **Quoting a sinkhole model as a prediction.** §6 is deliberately included as
    a warning; use the geophysics to map the void, and say what you cannot
    predict.

## 13. Real-world applications

- **Groundwater management.** Subsidence is the main reason that aquifer
  drawdown is regulated in sedimentary basins, and the monitoring is
  levelling, GNSS and InSAR against a water-level network
  ([14-01 Hydrology Fundamentals for Geophysicists](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/README.md)).
- **Infrastructure damage.** Drains, railways, pavements and pipelines fail at a
  differential displacement ten times smaller than the total subsidence, so the
  *gradient* of the bowl is what is mapped.
- **Sinkhole risk mapping.** Microgravity for the void, GPR for the roof, and
  resistivity for the water content and the karstic plumbing
  ([10 GPR and Near-Surface Methods](../../10-gpr-near-surface/README.md)).
- **Seismic hazard coupling.** A subsiding basin is also a basin that amplifies
  ground motion, for the same reason: it is filled with soft material
  ([04-07-01 Earthquake Hazard and Ground Motion](./01-earthquake-hazard.md)).
- **Reservoir compaction.** The same arithmetic at a depth of kilometres, with
  consequences for well integrity and for the overburden.
- **Sea-level change in deltas.** Natural compaction and human-induced
  subsidence are superimposed on sea-level rise and are often the larger term,
  which is why delta subsidence is measured rather than assumed
  ([15-06 Sea Level Change and Marine Records](../../15-oceanography-marine/06-sea-level-change-marine/README.md)).

## 14. Further reading

- **Terzaghi, K. *Theoretical Soil Mechanics* (Wiley).** The source of the
  effective-stress principle and of one-dimensional consolidation theory.
  Level: advanced, historical.
- **Burbey, T. J., and others, on aquifer-system compaction.** The literature on
  the coupling between groundwater flow and subsidence, which is what (2) and
  (3) are a static limit of. Level: graduate.
- **Galloway, D. L., Jones, D. R., & Ingebritsen, S. E. (eds), *Land Subsidence
  in the United States* (USGS Professional Paper 1726).** A comprehensive survey
  of measured subsidence, its causes and its measurement methods, freely
  available from USGS. Level: advanced.
- **Ford, D., & Williams, P. *Karst Hydrogeology and Geomorphology* (Wiley).**
  The standard account of karst processes, including the denudation-rate
  arithmetic in §5. Level: graduate.
- **Hanssen, R. F. *Radar Interferometry* (Kluwer).** The full treatment of
  InSAR, including the geometry, the coherence and the unwrapping problems that
  §7 reduces to two equations. Level: graduate.
- **USGS, *Land Subsidence in the United States* and the Groundwater and
  Landslide Hazards programs, reached from <https://www.usgs.gov>; and the NOAA
  National Geodetic Survey at <https://geodesy.noaa.gov>.** Reference material
  for both subsidence and the geodetic heights that make it measurable. Level:
  reference.
- **Copernicus and ESA data access at <https://dataspace.copernicus.eu/> and
  <https://www.esa.int>.** The InSAR and optical archives used in regional
  subsidence mapping. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 15. Related lessons

- [04-07-01 Earthquake Hazard and Ground Motion](./01-earthquake-hazard.md) —
  the site response that a soft basin also produces.
- [04-07-03 Landslides, Slope Stability and Geotechnical Geophysics](./03-landslides.md)
  — the same effective-stress mechanics applied to shear failure.
- [04-07-05 Tsunami Generation, Propagation and Warning](./05-tsunami.md) — the
  hazard that shares the coastal setting of many subsiding deltas.
- [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md)
  — the spaceborne measurement of mass change, at basin to global scale.
- [08-02 Gravity Instruments and Surveys](../../07-gravity-geodesy/02-gravity-instruments-and-surveys/README.md)
  — the microgravity instruments and repeat-survey practice that §4 depends on.
- [04-06-04 Aquifer Types and Groundwater Occurrence](../06-petroleum-and-mineral-systems/04-groundwater-aquifers.md)
  — the aquifer framework being pumped.

Exercises:
[`exercises/04-subsidence-sinkholes-exercises.md`](./exercises/04-subsidence-sinkholes-exercises.md)
and
[`exercises/04-subsidence-sinkholes-solutions.md`](./exercises/04-subsidence-sinkholes-solutions.md).

## Self-assessment checklist

- [ ] I can compute the effective-stress change from a head decline. (§2)
- [ ] I can compute compaction in both the modulus and the compression-index
      form, and state what each requires. (§2)
- [ ] I can derive the free-air gradient from $g = GM/r^2$ and state why it
      differs from the conventional coefficient. (§3)
- [ ] I can compute the Bouguer and residual gravity gradients. (§3)
- [ ] I can separate the free-air and mass contributions to a 4-D gravity
      change and get the signs right. (§4)
- [ ] I can derive a karst denudation rate from a mass balance and compute the
      time to remove a void. (§5)
- [ ] I can state why a critical-span calculation is not a sinkhole prediction.
      (§6)
- [ ] I can compute the InSAR phase for a displacement and the fringe value.
      (§7)
- [ ] I can solve two look geometries for vertical and horizontal motion. (§7)
- [ ] I can name three things no geophysical survey can supply for a subsidence
      forecast. (§10)
