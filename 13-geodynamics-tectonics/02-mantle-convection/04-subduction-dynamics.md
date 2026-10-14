---
id: 13-02-04
title: "Subduction Dynamics, Slab Geometry and Slab Pull"
level: research
prereqs: ["13-02-01", "13-01-04", "12-01-03"]
tags: [geodynamics, tectonophysics, subduction, slab-pull, bending, trench-migration]
---

# Subduction Dynamics, Slab Geometry and Slab Pull

> All models and data in this module are **SYNTHETIC**. The slab thermal model,
> plate age, viscosity, plate length and rheology are chosen teaching values, and
> every number quoted here is printed by
> `code/subduction_dynamics_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** slab pull per unit trench length from the integral of a slab's
   thermal density anomaly, and **explain** why thickness enters sub-linearly.
2. **Derive** the sinking speed from a balance of slab buoyancy against viscous
   drag on both faces, and **state** the assumptions that make it a scaling
   rather than a prediction.
3. **Derive** the bending length from a balance of bending moment against
   buoyancy torque, and **show** that a thick elastic slab cannot bend at
   geological radii.
4. **Compute** the elastic core thickness that can bend at a given radius, and
   **explain** why the bending stiffness of a slab is a few kilometres rather
   than a hundred.
5. **Assemble** a force inventory for a plate with an attached slab and **derive**
   the implied plate speed, with the viscosity dependence stated.
6. **Estimate** the depth at which a slab's thermal anomaly is erased, and
   **explain** why slab pull decays with depth.
7. **Analyse** slab dip as a kinematic quantity, and **state** why dip alone
   cannot be inverted for a single force.

## Prerequisites

- [13-02-01 Rayleigh-Benard Convection Applied to the Mantle](01-rayleigh-benard-mantle.md) —
  the cold boundary layer whose descent is subduction.
- [13-01-04 Driving Forces, Stress Fields and Intraplate Stress](../01-geodynamic-principles/04-forces-and-stresses.md) —
  the GPE integrals and the force inventory used here.
- [12-01-03 Upper-Mantle Discontinuities at 410 and 660 km](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/03-upper-mantle-discontinuities.md) —
  the depths that pin or deflect slabs.
- [13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure](../01-geodynamic-principles/03-lithospheric-strength.md) —
  the flexural rigidity $D$ used in the bending balance.

## 1. Intuition: the cold downwelling that organises the planet

Subduction is the return flow of mantle convection, and it is the part of the
cycle that does almost all the geological work: it makes mountains, earthquakes,
arc volcanoes, ore deposits and the deep-ocean trenches. Dynamically it has three
distinctive features that a layer-convection model lacks.

- **It is localised.** A slab is a narrow sheet, not a diffuse downwelling, and
  its narrowness is what allows it to penetrate the transition zone and reach the
  lower mantle.
- **It is stiff.** The slab is the coldest material in the mantle and therefore
  the strongest; on the way down it transmits its own weight to the surface plate
  as **slab pull**, the largest driving force in the plate system.
- **It is self-lubricating.** The bending that forms a slab requires stresses
  that exceed the elastic limit (measured in §4), so the slab's own strength is
  concentrated in a thin shell and the interior deforms viscously.

The lesson's arc follows those three features: how much force a slab can supply
(§3), how fast it therefore sinks (§3), how it bends (§4), how the forces close
into a plate speed (§5), and how the thermal anomaly that supplies the force
decays with depth (§6). The final section is about what slab geometry can and
cannot be inverted for, which is the practical question in most of the
literature.

## 2. The slab's thermal anomaly

The slab is the cooled boundary layer of the ocean plate, so its temperature
structure inherited from the ridge is a half-space cooling profile:

$$T(y) = T_m\,\mathrm{erf}\!\left(\frac{y}{2\sqrt{\kappa t}}\right),
\qquad
\Delta\rho(y) = \rho_m\alpha\left[T_m - T(y)\right] ,$$

with $y$ measured across the slab from its upper surface and $t$ the plate age at
the trench. With SYNTHETIC $t = 100$ Myr, $\kappa = 10^{-6}\ \mathrm{m^{2}\,
s^{-1}}$, $T_m = 1300$ K, $\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$,
$\rho_m = 3300\ \mathrm{kg\,m^{-3}}$ and slab thickness $h = 100$ km:

$$\int_0^{h}\Delta\rho\,\mathrm{d}y = 7.1423\times10^{6}\ \mathrm{kg\,m^{-2}},
\qquad
\langle\Delta\rho\rangle = 71.42\ \mathrm{kg\,m^{-3}} .$$

The average anomaly is 71 kg m$^{-3}$ — 2.2% of the mantle density — and it is
concentrated in the upper half of the slab, where the $\mathrm{erf}$ profile is
steepest. That concentration is what makes the block approximation of §3 work as
well as it does.

## 3. Slab pull and the sinking speed

### 3.1 The force

The buoyancy of the slab cross-section, integrated down-dip over a length $L$,
gives the force per unit trench length

$$F_{SP} = gL\int_0^{h}\Delta\rho(y)\,\mathrm{d}y .$$

Measured for $L = 600$ km:

$$F_{SP} = 4.2039\times10^{13}\ \mathrm{N\,m^{-1}} = 42.04\ \mathrm{TN\,m^{-1}} .$$

The dependence on slab thickness is sub-linear because the deeper part of the slab
is warmer:

| $h$ (km) | $F_{SP}$ (TN m$^{-1}$) |
|---|---|
| 50 | 28.67 |
| 75 | 36.87 |
| 100 | 42.04 |

The first 50 km supply 68% of the force of the first 100 km: a slab three times
thicker does not pull three times harder. Any argument that treats slab pull as
proportional to plate thickness is therefore systematically wrong, and wrong in
the direction of overestimating the force from old, thick plates.

Comparing with the ridge push of
[13-01-04 §3](../01-geodynamic-principles/04-forces-and-stresses.md)
($4.11\ \mathrm{TN\,m^{-1}}$):

$$\frac{|F_{SP}|}{|F_{RP}|} = \frac{42.04}{4.11} = 10.2 .$$

Both forces act on the plate in the *same* direction — away from the ridge, toward
the trench — so they add rather than compete.

### 3.2 The sinking speed

Balance the buoyancy of the slab against the viscous drag on its two faces. With
an effective density anomaly $\overline{\Delta\rho} = 71.42$ kg m$^{-3}$, the
buoyant force per unit area of the slab's face is $\overline{\Delta\rho}\,g\,h$;
the shear stress from a mantle of viscosity $\eta$ moving a distance $\sim h$ is
$\eta u/h$ on each face, so

$$\overline{\Delta\rho}\,g\,h = 2\frac{\eta u}{h}
\;\;\Longrightarrow\;\;
\boxed{\;u = \frac{\overline{\Delta\rho}\,g\,h^{2}}{2\eta}\;}.$$

Measured:

| $\eta$ (Pa s) | $u$ (m/s) | $u$ (mm/yr) | time to descend 660 km (Myr) |
|---|---|---|---|
| $10^{20}$ | $3.5033\times10^{-8}$ | 1105.5 | 0.6 |
| $10^{21}$ | $3.5033\times10^{-9}$ | 110.6 | 6.0 |
| $10^{22}$ | $3.5033\times10^{-10}$ | 11.06 | 59.7 |

At the reference viscosity of $10^{21}$ Pa s the slab sinks at
$110\ \mathrm{mm\,yr^{-1}}$ and crosses the upper mantle in 6 Myr. Two remarks,
in decreasing order of importance.

- **This is a scaling, not a prediction.** The drag law assumes a single
  viscosity, an $O(1)$ velocity profile imposed over a length scale $h$, and no
  pressure- or temperature-dependence. Factor the integral differently and the
  coefficient changes by a factor of a few. What the calculation establishes is
  that *slab pull with these magnitudes produces plate-tectonic speeds*, which is
  a consistency check on the whole force inventory and not a measurement of
  subduction rates.
- **The speed is fast compared with the geological rate of subduction.** 110
  mm/yr is twice a typical convergence rate, which is itself informative: slabs do
  not free-fall through the mantle, because the plate attached to them and the
  mantle wedge resist. The dynamical balance of §5 is where that resistance is
  accounted for.

## 4. Bending: why slab strength is a thin shell

### 4.1 The bending length

Balancing the bending moment a slab can generate, $D/l$, against the buoyancy
torque available over that length, $q\,l^{2}/2$ with $q = \overline{\Delta\rho}gh$:

$$\frac{D}{l} = \frac{q\,l^{2}}{2}
\;\;\Longrightarrow\;\;
\boxed{\;l_b = \left(\frac{2D}{q}\right)^{1/3}\;}.$$

With $T_e = 30$ km, $E = 70$ GPa, $\nu = 0.25$:

$$D = \frac{E T_e^{3}}{12(1-\nu^{2})} = 1.6800\times10^{23}\ \mathrm{N\,m},
\qquad q = 7.0066\times10^{7}\ \mathrm{Pa},$$

$$l_b = 168.6\ \mathrm{km},
\qquad \text{check: } \frac{D}{l_b} = \frac{q\,l_b^{2}}{2}
= 9.9624\times10^{17}\ \mathrm{N\,m}\ \checkmark$$

The bending length is a few hundred kilometres: a slab cannot negotiate a corner
tighter than that without help from yielding, and $l_b$ is the scale at which the
slab's geometry and its stiffness are in balance.

### 4.2 The elastic bending stress is impossible

The bending stress at the outer fibre when a slab of thickness $h$ bends to
radius $R$ is

$$\sigma_b = \frac{E\,(h/2)}{R} .$$

At $R = l_b = 168.6$ km with $h = 100$ km:

$$\sigma_b = 2.0755\times10^{10}\ \mathrm{Pa} = 20\,755\ \mathrm{MPa} .$$

Against a SYNTHETIC yield strength of 700 MPa that is a factor of 30 over the
limit. **A 100 km thick elastic slab cannot bend at all at geological radii.** The
resolution is that the slab does not bend elastically as a whole: it yields, and
the bending is accommodated by a thin elastic core. Solving $\sigma_y = Ey/R$ for
the core thickness:

| curvature radius $R$ (km) | elastic core thickness (km) |
|---|---|
| 100 | 2.0 |
| 300 | 6.0 |
| 1000 | 20.0 |

So the part of a slab that behaves elastically during bending is a few kilometres
thick — not the 30 km of §4.1 and not the 100 km of the slab. This is the
reconciliation of two apparently contradictory facts: slabs *are* strong
(they transmit slab pull over thousands of kilometres without buckling) and slabs
*do* deform dramatically at trenches. The strength is in the plate's interior; the
deformation is in a thin yielding shell at the bend.

## 5. Closing the force balance with a plate attached

Adding the two driving forces and balancing them against basal drag over a plate
of length 5000 km, channel thickness 200 km and viscosity $\eta = 10^{21}$ Pa s:

$$F_{\text{net}} = |F_{SP}| + |F_{RP}| = 46.15\ \mathrm{TN\,m^{-1}},$$

$$u = \frac{F_{\text{net}}\,d}{\eta L_p}
= \frac{(4.6152\times10^{13})(2\times10^{5})}{(10^{21})(5\times10^{6})}
= 1.8460\times10^{-9}\ \mathrm{m\,s^{-1}} = 58.3\ \mathrm{mm\,yr^{-1}} .$$

This is identical to the plate-speed calculation of
[13-01-04 §5](../01-geodynamic-principles/04-forces-and-stresses.md) because it
is the same balance; what the slab-specific version adds is the observation that
the *slab pull term dominates the inventory by an order of magnitude*. The
corollary used throughout the literature follows immediately: **the speed at
which a plate moves should correlate with the length of subducting slab attached
to it**, and this is the one force-inventory prediction that is robust to the
factor-of-few uncertainty in the coefficient, because it compares two plates with
the same drag parameters rather than predicting an absolute speed.

## 6. How deep does a slab stay cold?

The slab's thermal anomaly diffuses away on

$$t_{\text{eq}} = \frac{(h/2)^{2}}{\kappa}
= \frac{(5\times10^{4})^{2}}{10^{-6}} = 2.5\times10^{12}\ \mathrm{s}
= 79.2\ \mathrm{Myr} .$$

Combined with the descent speed:

| sinking speed | depth at which the anomaly is erased |
|---|---|
| 50 mm/yr | 3961 km |
| 100 mm/yr | 7922 km |

Both are deeper than the mantle. The conclusion is the opposite of the naive one:
a slab sinking at plate-tectonic speed **keeps its cold core all the way to the
core-mantle boundary**, and the seismic images of fast anomalies at 1500–2500 km
depth ([06-06-01](../../06-seismology/06-seismic-tomography/01-tomography-principle.md))
are the expected consequence. Correspondingly, a *slow* slab warms as it descends
and loses its driving force — a feedback, not a fixed property: slower sinking
leads to faster heating leads to less pull. This is one of the clearest
quantitative connections between slab thermal structure and slab dynamics, and it
is why slab pull is largest for old, thick, fast-subducting plates.

## 7. Dip is kinematics, not a force

Dip is geometry. Pin the slab tip at a fixed depth (the 660 km discontinuity is
the natural choice, from
[12-01-03](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/03-upper-mantle-discontinuities.md))
and let the trench retreat at $v_r$. With a slab segment of down-dip length $L$,
$\sin\theta = \text{depth}/L$, so

$$\frac{\mathrm{d}\theta}{\mathrm{d}t} \approx \frac{v_r}{L} .$$

Measured for $L = 800$ km:

| rollback $v_r$ (mm/yr) | dip change (deg/Myr) |
|---|---|
| 0 | 0.00 |
| 15 | 1.07 |
| 30 | 2.15 |

Two consequences. First, a slab steepens with *no* change in the driving force:
rollback alone produces dip evolution, so an observed steepening cannot be
attributed to slab pull without additional information. Second, the convergence
rate $V$ does not appear directly — only through $L$. This is why dip is a
diagnostic of trench motion, and why the "why do slabs dip at different angles?"
question has more than one answer: buoyancy (a dynamics question), rollback (a
kinematics question), and the resistance of the 660 km discontinuity (a rheology
question) all contribute, and they are not separable from dip alone.

## 8. Assumptions and regime of validity

| assumption | where it fails |
|---|---|
| half-space cooling thermal structure | slab heating during descent; a plate model caps the anomaly |
| uniform mantle viscosity | the wedge is weak, the slab interior strong, the lower mantle stiffer |
| plane drag law on both faces | slab-anchored flow, wedge suction, and an unmodelled pressure field |
| elastic bending | measured in §4.2 to be violated by a factor of 30 |
| 2-D force balance | torques, plate rotation, oblique convergence |
| no trench suction | first-order in many margins, especially for young slabs |
| rigid plate | plate deformation at the MPa level; intraplate stress |
| pinned slab tip | slabs can stagnate, buckle or break through the 660 km discontinuity |

The most consequential is the uniform-viscosity assumption. A slab entering a
mantle whose viscosity increases by a factor of 30 at 660 km (which the
references of [12-01-03](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/03-upper-mantle-discontinuities.md)
support) experiences a jump in drag and can stagnate rather than descend — one of
the observations that forced the community away from simple whole-mantle
convection models.

## 9. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| density anomaly integral | | kg m$^{-2}$ | $\int\Delta\rho\,\mathrm{d}y$ |
| slab pull | $F_{SP}$ | N m$^{-1}$ | $gL\times$(kg m$^{-2}$) |
| sinking speed | $u$ | m s$^{-1}$ | $\Delta\rho g h^{2}/\eta$ |
| bending length | $l_b$ | m | $(D/q)^{1/3}$: (N m / Pa)$^{1/3}$ = m |
| bending stress | $\sigma_b$ | Pa | $E(h/2)/R$ |
| elastic core | $h_{el}$ | m | $2\sigma_y R/E$ |
| dip rate | $\mathrm{d}\theta/\mathrm{d}t$ | rad s$^{-1}$ | $v_r/L$ |

The bending-length check is worth doing once by hand: N m / Pa = N m / (N m$^{-2}$)
= m$^{3}$, and the cube root is a length. If your expression yields anything else,
a modulus or a thickness has been misplaced.

## 10. The demonstration

`code/subduction_dynamics_demo.py` prints every number above:

```bash
cd 13-geodynamics-tectonics/02-mantle-convection/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python subduction_dynamics_demo.py
```

It computes the slab density-anomaly integral and slab pull for three slab
thicknesses; the sinking speed for three mantle viscosities; the flexural
rigidity, bending length (with its moment-balance check) and the elastic-core
thickness; the force inventory and implied plate speed; the slab thermal
equilibration depth; and the dip-rate kinematics. Fixed seed, print-only, no
network, exits 0.

Exercises:
[`exercises/04-subduction-dynamics-exercises.md`](exercises/04-subduction-dynamics-exercises.md)
and
[`exercises/04-subduction-dynamics-solutions.md`](exercises/04-subduction-dynamics-solutions.md).

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC slab is 80 km thick, 500 km long down-dip, with a mean density
> anomaly of 60 kg m$^{-3}$; $\eta = 2\times10^{21}$ Pa s, $E = 70$ GPa,
> $\nu = 0.25$, $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, and a SYNTHETIC yield
> strength of 500 MPa.
> **(a)** Compute the slab pull per unit trench length. **(b)** Compute the sinking
> speed and the time to descend 660 km. **(c)** Compute the elastic core thickness
> that can bend to a radius of 250 km, and compare it with the slab thickness —
> what does the comparison say about the assumption of an elastic slab?
> **(d)** Compute the depth at which the slab's thermal anomaly is erased. Would
> you expect this slab to be imaged seismically at 1500 km depth? Justify.

A worked version appears in the
[solutions](exercises/04-subduction-dynamics-solutions.md).

## Common pitfalls

1. **Treating slab pull as proportional to slab thickness.** The thermal anomaly
   is concentrated at the top; the dependence is sub-linear (§3.1).
2. **Forgetting the factor of two for two faces.** Drag acts on both sides of a
   slab; omitting one doubles the inferred speed.
3. **Believing an elastic slab bends at a trench.** Measured here: the required
   stress exceeds plausible yield by a factor of 30.
4. **Reading dip as a force measurement.** Rollback steepens slabs with no change
   in force.
5. **Assuming a slab warms up as it descends.** At plate-tectonic speeds it does
   not; it stays cold to great depth, which is why slab pull does not vanish.
6. **Using the same viscosity for the wedge, the slab and the lower mantle.**
   The contrasts are factors of 10–100 and they change the regime.
7. **Assuming a slab sinks in a straight line.** Slabs can stagnate, fold and
   pond; each implies a specific viscosity structure.

## Related modules

- [13-02-01 Rayleigh-Benard Convection Applied to the Mantle](01-rayleigh-benard-mantle.md) —
  the cold boundary layer in a layer-convection framework.
- [13-02-02 Numerical Modelling of Mantle Convection](02-convection-numerical.md) —
  how slabs are represented in a solver.
- [13-02-03 Mantle Plumes, Hotspots and Large Igneous Provinces](03-mantle-plumes.md) —
  the upwelling counterpart.
- [13-01-04 Driving Forces, Stress Fields and Intraplate Stress](../01-geodynamic-principles/04-forces-and-stresses.md) —
  the full force inventory.
- [13-05-02 Solving the Stokes Equations for Mantle Flow](../05-geodynamic-modelling/02-stokes-flow-solvers.md) —
  the numerical treatment of the viscous slab.
- [13-06-03 Glacial Isostatic Adjustment: Ice, Viscosity and Sea Level](../06-crustal-and-lithospheric-dynamics/03-glacial-isostatic-adjustment.md) —
  an independent constraint on the same mantle viscosity.
