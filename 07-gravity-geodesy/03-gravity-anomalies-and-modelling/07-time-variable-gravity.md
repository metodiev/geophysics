---
id: 07-03-07
title: "Time-Variable Gravity: Hydrology, Ice and Mass Redistribution"
level: research
prereqs: ["07-03-04", "07-05-03"]
tags: [gravity, geodesy, time-variable, hydrology, ice, gravity-change, equivalent-water-height]
---

# Time-Variable Gravity: Hydrology, Ice and Mass Redistribution

All models and data in this module are SYNTHETIC. The layer thicknesses, region
sizes, observation altitudes, noise levels and trends used below are chosen
teaching values. No real mission, product, basin or glacier is referenced, and no
published measurement is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the gravity change produced by a thin surface mass layer, in the
   flat-Earth limit and for a global shell, and **explain** the factor of two
   between them.
2. **Convert** a water-layer thickness to a gravity change and back, in microgal
   and metres of equivalent water height.
3. **Explain** why gravity constrains the product of density and thickness, and
   what additional assumption is needed to separate them.
4. **Compute** the attenuation of a compact mass observed at altitude and
   **state** the resolution this implies.
5. **Measure** the leakage and amplitude bias introduced by a smoothing filter
   and **interpret** a recovered amplitude as a lower bound.
6. **Separate** a secular trend from seasonal cycles by least squares and
   **quantify** the record length needed.
7. **Account** for the error budget of a mass-change estimate, including area,
   density, leakage and noise contributions.

## Prerequisites

- [04 Gravity Inversion and Its Severe Non-Uniqueness](04-inversion-gravity.md) —
  the general problem of separating mass from geometry.
- [07-05-03 Spherical Harmonic Solutions and Coefficient Interpretation](../05-satellite-gravimetry/03-spherical-harmonic-solutions.md) —
  the coefficient representation of the field that time-variable gravity is
  expressed in.

## 1. Why gravity changes with time

Everything that moves mass changes the gravity field: water stored in soil and
snow, groundwater depletion, ice-sheet growth and loss, sea level, post-glacial
rebound, volcanic inflation, and the tides. The changes are small — microgal for
metres of water, tens of microgal for ice-sheet mass loss over years — and they
are measured from the ground (repeat microgravity) and from orbit (satellite
gravimetry).

This lesson is about the *conversion*: from an observed gravity change to a mass
change. The conversion is where the physics lives, and where the assumptions
decide the answer, because gravity responds to mass per unit area, not to water
depth, and not to ice thickness.

## 2. The local and the global constants

### 2.1 A thin surface layer (flat-Earth limit)

For an infinite horizontal slab of density $\rho$ and thickness $h$ the anomaly
is the Bouguer value

$$g = 2\pi G\rho h .$$

For water, $\rho = 1000\ \mathrm{kg\,m^{-3}}$, so with
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}kg^{-1}s^{-2}}$:

$$1\ \mathrm{m}\ \text{of water} \;\rightarrow\;
2\pi G\rho h = 41.936\ \mu\mathrm{Gal}.$$

### 2.2 A global shell

For a thin spherical shell of surface density $\sigma$ surrounding the Earth, the
shell theorem gives a field just outside of $4\pi G\sigma$, so for a global water
layer

$$g = 4\pi G\rho h = 83.872\ \mu\mathrm{Gal}\ \text{per metre}.$$

The demonstration prints both and the ratio $2.00$ for every thickness tested
($0.01$, $0.1$, $1$, $10\ \mathrm{m}$). **The factor of two is geometry, not
sloppiness**: a global layer's mass is distributed over a sphere and its field is
purely radial, whereas an infinite slab's field is the half-space value. Quoting
"$41.9\ \mu\mathrm{Gal}$ per metre of water" without saying which model it belongs
to is an error of a factor two.

**Definition.** The **equivalent water height** (EWH) is the thickness of a
water layer of density $1000\ \mathrm{kg\,m^{-3}}$ that would produce the
observed mass per unit area:

$$\mathrm{EWH} = \frac{\Delta\sigma}{\rho_w}
= \frac{\Delta g}{2\pi G\rho_w}$$

in the flat-Earth limit, with $\Delta\sigma$ the surface mass change in
$\mathrm{kg\,m^{-2}}$.

## 3. Worked example: a seasonal storage cycle

*A catchment stores and releases $0.5\ \mathrm{m}$ of water equivalent, with an
annual period.*

1. **Gravity amplitude.** Using the local slab relation,
   $\Delta g = 2\pi G\rho_w h = 41.936\times0.5 = 20.97\ \mu$Gal amplitude,
   i.e. $41.92\ \mu$Gal peak to peak. The demonstration prints exactly these
   numbers.
2. **Record.** Sampling every $10$ days over two years gives the cycle directly:
   $+20.97\ \mu$Gal at $t=0$, $+0.47$ at $90\ \mathrm{d}$, $-20.95$ at
   $180\ \mathrm{d}$.
3. **The density ambiguity.** The same signal would be produced by
   $h = 0.5 \times 1000/2500 = 0.200\ \mathrm{m}$ of rock at
   $2500\ \mathrm{kg\,m^{-3}}$: the demonstration prints $20.968\ \mu$Gal for
   both. **Gravity fixes the product of density and thickness, never either
   alone.** A hydrology interpretation assumes the density; a permafrost or
   ice interpretation assumes a different one, and the two give different answers
   from the same data.
4. **Detectability.** Whether $20.97\ \mu$Gal is measurable depends on the
   instrument and on the noise: a modern relative gravimeter reaches a few
   microgal at a well-controlled site, while a satellite product has an
   uncertainty of the order of centimetres of EWH over large regions. The lesson
   for both is the same: state the noise, and propagate it.

## 4. Attenuation with altitude

A surface mass distribution $\sigma(x,y)$ produces, at height $H$ above it,

$$\Delta g(\mathbf{k}) = 2\pi G\,\tilde{\sigma}(\mathbf{k})\,e^{-kH},$$

so every wavelength is attenuated by $e^{-kH}$ — the same upward-continuation
operator derived in [05](05-derivatives-and-filters.md). The demonstration uses a
Gaussian footprint of $1\ \mathrm{m}$ EWH observed at $H = 400\ \mathrm{km}$:

| footprint $\sigma$ (km) | peak on the ground ($\mu$Gal) | peak at $400\ \mathrm{km}$ ($\mu$Gal) | retained fraction |
|---|---|---|---|
| 20 | 41.9359 | 0.1050 | 0.003 |
| 40 | 41.9359 | 0.4111 | 0.010 |
| 80 | 41.9359 | 1.5230 | 0.036 |
| 160 | 41.9359 | 4.8552 | 0.116 |

Two lessons. **On the ground the peak is the local slab value $2\pi G\rho h = 41.94\ \mu$Gal for every footprint** — the peak of a smooth layer is insensitive to
its extent. **At altitude the compactness destroys the signal**: a $20\ \mathrm{km}$
footprint retains $0.3\%$, a $160\ \mathrm{km}$ footprint $11.6\%$. Satellite
gravimetry is a large-scale technique by construction, and the size of the mass
change cannot be inferred from the *shape* of what little arrives.

## 5. Leakage: what filtering does to an amplitude

Take the $40\ \mathrm{km}$ footprint and apply a Gaussian smoothing filter of
radius $r_f$ — the standard step in satellite gravity processing that suppresses
high-wavenumber noise:

| filter radius (km) | recovered peak (m EWH) | peak bias (%) | mass outside $3\sigma$ (%) |
|---|---|---|---|
| 20 | 0.800 | $-20.00$ | 2.72 |
| 40 | 0.500 | $-50.00$ | 10.54 |
| 80 | 0.200 | $-80.00$ | 40.69 |
| 160 | 0.059 | $-94.12$ | 76.77 |

For a 2-D Gaussian the attenuation is exactly
$\sigma^{2}/(\sigma^{2}+r_f^{2})$, which reproduces the table: $r_f/\sigma = 0.5$
gives $0.8$, $1.0$ gives $0.5$, $2.0$ gives $0.2$, $4.0$ gives $0.059$. The
recovered amplitude is therefore **a lower bound** on the true storage, and the
leaked signal appears as mass where there is none — $76.8\%$ of the recovered
mass lies outside three source radii at the largest filter radius. Any basin-scale
mass estimate must state the filter and either correct for the attenuation or
report the uncorrected value as a bound.

## 6. From gravity change to mass change

For a region of area $A$ over which a change $\Delta g$ is measured, and assuming
the change is spread uniformly and only over that region,

$$\Delta M = \frac{\Delta g\,A}{2\pi G},
\qquad \Delta\mathrm{EWH} = \frac{\Delta M}{\rho_w A}
= \frac{\Delta g}{2\pi G\rho_w}.$$

The demonstration evaluates this for a $200\times200\ \mathrm{km}$ region:

| $\Delta g$ ($\mu$Gal) | mass (kg) | EWH (m) |
|---|---|---|
| 1.00 | $9.538\times10^{11}$ | 0.024 |
| 2.00 | $1.908\times10^{12}$ | 0.048 |
| 10.00 | $9.538\times10^{12}$ | 0.238 |

Three error terms enter linearly or worse:

1. **Noise.** $0.2\ \mu$Gal on a $2\ \mu$Gal signal is a $10\%$ error in mass
   before any other term.
2. **Leakage.** From §5 a $50\%$ amplitude bias is not exceptional; it is
   systematic, and it is not reduced by averaging.
3. **Area and density assumptions.** Both are statements about where the mass is
   and what it consists of. A uniform layer assumption over a region with
   internally variable storage gives a regional mean, not the storage field.

## 7. Separating a trend from a season

A ten-year record with a trend of $-0.05\ \mathrm{m\,yr^{-1}}$ in EWH and a
$0.30\ \mathrm{m}$ annual cycle is fitted with a constant, a linear trend and
annual sine/cosine terms. The demonstration recovers the trend and the amplitude
exactly with no noise, and with white noise:

| noise ($\mu$Gal) | scatter of the trend ($\mathrm{m\,yr^{-1}}$) | scatter of the annual amplitude (m) |
|---|---|---|
| 0.0 | $0.00000$ | 0.00000 |
| 0.5 | $0.00039$ | 0.00151 |
| 1.0 | $0.00078$ | 0.00319 |
| 2.0 | $0.00159$ | 0.00610 |

Ten years of a $0.05\ \mathrm{m\,yr^{-1}}$ trend integrate to $0.5\ \mathrm{m}$,
i.e. about $21\ \mu$Gal, so even microgal-level noise leaves the trend determined
to a few $10^{-4}\ \mathrm{m\,yr^{-1}}$. **Shorten the record or reduce the
trend, and the noise dominates**: the same $2\ \mu$Gal noise on a one-year record
of a $0.005\ \mathrm{m\,yr^{-1}}$ trend would drown it. This is why
time-variable gravity is a long-baseline method, and why the annual and
semi-annual terms are always modelled explicitly rather than smoothed away.

## 8. Assumptions and regime of validity

1. **Flat-Earth versus spherical geometry**, chosen explicitly as in §2. Errors
   of a factor of two live here.
2. **Mass changes confined to a thin surface layer.** Deep mass changes (mantle
   convection, post-glacial rebound) require a full spherical treatment and are
   the subject of
   [07-06-04 Post-Glacial Rebound: Viscosity and Ice History Inference](../06-earth-tides-and-rotation/04-post-glacial-rebound.md).
3. **Known density** for the conversion, or a stated range.
4. **A stated filter and a stated noise level.** Without them the amplitude is
   not reproducible.
5. **No competing mass change.** Two simultaneous effects (groundwater depletion
   and rebound, say) superpose; separating them needs either spatial patterns or
   independent data — the same non-uniqueness as
   [04](04-inversion-gravity.md), in the time domain.
6. **The reference frame is stable** or its motion is modelled
   ([07-04-05 ITRF, Plate Motion Models and Frame Transformations](../04-geodesy-reference-frames/05-itrf-and-plate-models.md)).

## 9. Physical interpretation

- Gravity senses surface mass, so it measures water storage, snow and ice mass
  per unit area directly — the quantity hydrologists and glaciologists actually
  want — without needing the density profile underground.
- The conversion constant $2\pi G$ is the same one that appears in the Bouguer
  slab: a mass-change map is a Bouguer map in disguise, which is why the same
  caveats apply.
- The altitude attenuation $e^{-kH}$ is a low-pass filter imposed by physics, not
  by the analyst: the satellite cannot see compact targets, and no processing
  recovers them.
- Because the atmosphere, oceans and solid Earth all move, any observed
  time-variable field is a sum of contributions; attribution is the research
  problem, and it is an inverse problem with a rich null space.

## 10. Python demonstration

`code/time_variable_gravity_demo.py` prints:

1. the slab-versus-shell constants and their ratio;
2. the seasonal cycle in EWH and microgal, and the water-versus-rock equivalence;
3. the ground and $400\ \mathrm{km}$ peaks versus footprint size, with retained
   fractions;
4. leakage and amplitude bias versus filter radius, including the mass fraction
   outside three source radii;
5. the region-to-mass conversion table;
6. the trend/season separation with the trend and amplitude scatter versus noise.

All output carries units; the script uses `np.random.default_rng(20261014)` and
exits 0.

## 11. Exercises

See
[`exercises/07-time-variable-gravity-exercises.md`](./exercises/07-time-variable-gravity-exercises.md)
and
[`exercises/07-time-variable-gravity-solutions.md`](./exercises/07-time-variable-gravity-solutions.md).

- **★** Convert $5\ \mathrm{cm}$ of water to a gravity change in both models.
- **★** State the difference between the slab constant and the shell constant and
  which one applies to a $100\ \mathrm{km}$ basin.
- **★★** A groundwater loss of $0.3\ \mathrm{m\,yr^{-1}}$ EWH over
  $150\times150\ \mathrm{km}$: compute the annual gravity change and the mass
  loss.
- **★★** Using the leakage table, estimate the true EWH of a $40\ \mathrm{km}$
  feature recovered as $0.35\ \mathrm{m}$ with a $40\ \mathrm{km}$ filter.
- **★★★** Design a processing chain that would distinguish a trend from a
  seasonal cycle in a five-year record with $1.5\ \mu$Gal noise, and state the
  residual risk.

## Mastery checkpoint

Without notes:

> A satellite product shows a $6\ \mu$Gal decrease over five years within a
> $300\times300\ \mathrm{km}$ region; the processing used a $60\ \mathrm{km}$
> filter and the regional noise is $1\ \mu$Gal.

**(a)** Convert the signal to mass change and EWH, stating the model you use.
**(b)** Convert the noise to an uncertainty on the mass.
**(c)** State the direction of the leakage bias and whether the true change is
larger or smaller than your estimate.
**(d)** List two other mass changes that could produce the same signal and one
measurement that could separate them.

## Common pitfalls

1. **Using the slab constant for a global change**, or the shell constant for a
   basin. A factor of two.
2. **Reading the filtered amplitude as the true amplitude.** Smoothing always
   lowers a peak; the demonstration measures $-20\%$ to $-94\%$.
3. **Assuming a density without saying so.** The water/rock ambiguity is exact
   and unfixable from gravity alone.
4. **Ignoring the altitude attenuation.** A compact anomaly is invisible from
   orbit; the retained fraction is $0.3\%$ for a $20\ \mathrm{km}$ footprint.
5. **Fitting a trend to a short record with large seasonal terms** and calling
   the result a trend.
6. **Averaging away a systematic.** Leakage, not noise, usually dominates a
   basin-scale mass error.

## 12. Applications

- **Groundwater monitoring.** Repeat microgravity measures storage change
  directly; satellite gravimetry maps it at basin scales. Both need the
  conversions in §2 and §6.
- **Ice-sheet and glacier mass balance.** The same constants convert to ice
  mass once a density is assumed
  ([07-05-05 Applications: Groundwater Depletion, Ice Loss, Sea Level](../05-satellite-gravimetry/05-grace-applications.md)).
- **Sea level and ocean mass.** Time-variable gravity separates ocean mass
  change from steric (thermal) change, and the separation depends on the frame
  used ([07-07-03 Sea Surface Topography and the Marine Geoid](../07-geoid-and-height-modern/03-sea-surface-topography.md)).
- **Volcano and geothermal monitoring.** Repeat microgravity detects magma and
  fluid movement at depths of kilometres.

## Related modules

- [04 Gravity Inversion and Its Severe Non-Uniqueness](04-inversion-gravity.md).
- [05 Derivatives, Upward/Downward Continuation and Euler Deconvolution](05-derivatives-and-filters.md) —
  the attenuation operators used here.
- [07-05-01 GRACE and GRACE-FO: Mission Concept and Data Products](../05-satellite-gravimetry/01-grace-gracefo.md) and
  [07-05-04 Mass Concentration Solutions, Leakage and Filtering](../05-satellite-gravimetry/04-mascons-and-leakage.md) —
  where leakage and mascons come from.
- [07-06-04 Post-Glacial Rebound: Viscosity and Ice History Inference](../06-earth-tides-and-rotation/04-post-glacial-rebound.md) —
  the deep-mass counterpart.

## 13. Self-assessment checklist

- [ ] I can derive both conversion constants and say which applies when.
- [ ] I can convert between EWH, mass and gravity change in both directions.
- [ ] I can state and use the altitude attenuation factor.
- [ ] I can predict the amplitude bias of a smoothing filter.
- [ ] I can assemble a mass-change error budget with a noise, leakage and
      assumption term.
- [ ] I can fit a trend and a season together and state the record length needed.
