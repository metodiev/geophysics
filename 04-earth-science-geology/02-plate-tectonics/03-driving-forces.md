---
id: 04-02-03
title: "Mantle Convection, Slab Pull and Ridge Push"
level: advanced
prereqs: ["04-02-02", "02-06-06", "02-05-06"]
estimated_minutes: 90
tags: [slab-pull, ridge-push, mantle-convection, driving-forces, viscosity, rayleigh-number]
---

# Mantle Convection, Slab Pull and Ridge Push

A plate moves because it is pushed and pulled, and the question this lesson
answers is *by what*, and *how much*. Four candidates are usually listed:

1. **Slab pull** — the negative buoyancy of a cold, dense descending slab.
2. **Ridge push** — the gravitational sliding of lithosphere off the elevated
   ridge.
3. **Basal drag** — shear traction between the plate and the convecting mantle
   beneath it, which can drive or resist.
4. **Slab suction** — the traction that a descending slab exerts on the
   surrounding mantle, which pulls the overriding plate toward the trench.

The lesson's method is to **compute each force from its own mechanism** rather
than to quote a ranking. The forces then differ by an order of magnitude, and
the ranking is the robust part of the result while the individual values are
not. That distinction — what is robust and what is not — is the difference
between a force estimate and a force guess.

Two of the calculations are worth stating in advance because they are the
intellectual pay-off.

**Slab pull comes from the same physics as seafloor depth.** The density excess
of a slab is the thermal contraction that makes old ocean floor sit deeper than
young ocean floor, integrated over the slab's cross-section. So a model that
predicts the bathymetry of the ocean basins also predicts the force that drives
the plates, with no new parameters.

**A viscosity the observations require.** If slab pull is the main driver and a
plate moves at its observed speed, the viscosity needed to balance the drive
against drag follows from the drag law. The number that comes out — of order
$10^{20}$ to $10^{21}$ Pa·s — is the same number that post-glacial rebound
infers from a completely different observation. That agreement is the strongest
single piece of evidence that the forces and the viscosities in this lesson are
the right order of magnitude.

## Learning objectives

By the end of this lesson you will be able to:

1. **List** the candidate driving forces and the mechanism behind each.
2. **Compute** slab pull from the thermal structure of a subducting slab and
   state its dependence on slab age and on how much slab is counted.
3. **Compute** ridge push from the pressure difference at the ridge and explain
   why its value is dominated by an ambiguous thickness.
4. **Compute** basal drag from a viscosity, a plate speed and an asthenospheric
   thickness, and explain why its *sign* is the unresolved part.
5. **Derive** the effective viscosity required to balance slab pull against drag
   and compare it with the viscosity inferred from post-glacial rebound.
6. **Compute** a mantle Rayleigh number and state why its value settles whether
   the mantle convects but not how.
7. **Rank** the forces by order of magnitude and state which parts of the
   ranking are robust.
8. **Explain** why the sign and magnitude of basal drag, and the absolute
   importance of ridge push, remain matters of active measurement.

## Prerequisites

- [04-02-02 Divergent, Convergent and Transform Boundaries](./02-plate-boundaries.md)
  — the boundary types whose motion these forces produce.
- [02-06-06 Mantle Convection and Rayleigh–Bénard Instability](../../02-physics/06-fluid-mechanics/06-mantle-convection.md)
  — the convection theory, including the critical Rayleigh number.
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../../02-physics/05-thermodynamics/06-geotherms.md)
  — the temperature structure that makes a slab dense.

## 1. The forces, and the mechanism behind each

| Force | Mechanism | Order of magnitude (N per m of boundary) | Sign |
|---|---|---|---|
| Slab pull | Negative buoyancy of cold, dense lithosphere | $10^{13}$ | Drives, along the slab |
| Ridge push | Gravitational sliding off the elevated ridge | $10^{12}$ | Drives, away from the ridge |
| Basal drag | Shear traction with the asthenosphere | $10^{12}$ | Either, depending on relative motion |
| Slab suction | Traction from slab-driven mantle flow | $10^{12}$ | Drives the overriding plate toward the trench |

The units need stating. A force per unit length of boundary has units N/m, and it
is the natural quantity because a plate boundary is a line: multiplying by the
length of the boundary gives a force. Every number in this lesson is in N/m.

The order-of-magnitude column is the answer the lesson derives. Read it as a
ranking with error bars of a factor of a few, not as a set of measurements.

## 2. Physical reasoning: why a slab is dense, and how dense

A subducting slab is the cold thermal boundary layer of the ocean plate, and its
temperature structure is the one from the seafloor cooling model:

$$T(z) = \Delta T\,\operatorname{erf}\!\left(\frac{z}{2\sqrt{\kappa t}}\right),$$

with $t$ the slab's age at subduction and $z$ measured downward from the top of
the plate. The temperature *deficit* is therefore
$\Delta T\,\operatorname{erfc}(z/2\sqrt{\kappa t})$, and the density excess
relative to the mantle at the same depth is

$$\Delta\rho(z) = \rho_m\alpha\Delta T\,\operatorname{erfc}\!\left(\frac{z}{2\sqrt{\kappa t}}\right).$$

This is the same thermal contraction that produces the depth–age curve of
[04-02-01](./01-tectonic-theory.md), applied to a vertical section instead of a
horizontal one. The force along the slab is that density excess integrated over
the slab's cross-section:

$$F = g\,L_\text{slab}\int_0^h \Delta\rho(z)\,\mathrm{d}z .$$

The demo computes it:

```text
   slab age (Ma)  scale depth (km)  mass excess (kg/m^2)
              20                50             3.642e+06
              60                87             5.972e+06
             100               112             7.142e+06
             140               133             7.870e+06

    slab age      L = 660 km     L = 2900 km   ratio
          20        2.36e+13        1.04e+14     4.4
          60        3.87e+13        1.70e+14     4.4
         100        4.62e+13        2.03e+14     4.4
         140        5.10e+13        2.24e+14     4.4
```

Three things to read off.

**A slab that cooled for longer is thicker and colder**, so it pulls harder: the
140 Ma slab pulls 2.2 times as hard as the 20 Ma slab. That is a *prediction*,
and it is testable: plates attached to old, deeply subducted slabs should move
faster. Over the large plates the correlation is present and weak, which is
exactly the situation that keeps a question open rather than closed.

**The force depends on how much slab is counted.** Counting the slab down to the
660 km discontinuity, where phase changes and the viscosity increase alter its
behaviour, gives a few times $10^{13}$ N/m; counting the whole mantle path gives
about 4.4 times that. Both are the same physics with a different *definition* of
the slab, which is why slab pull should be quoted as a range. A comparison of
two papers' force estimates that does not check what each one counted is a waste
of an afternoon.

**The dip decides how much of the force is useful.** The along-slab force acts
down-dip; the component that drives the plate toward the trench is that force
times $\cos(\text{dip})$. A 60° slab transmits half of it horizontally, a 30°
slab transmits 87 per cent. The dip therefore matters as much as the force when
the question is how fast a plate moves.

## 3. Physical reasoning: ridge push, and an honest ambiguity

The ridge stands higher than old ocean floor because young lithosphere is hot
and therefore light. At the base of the plate, the pressure beneath the ridge is
lower than beneath old lithosphere by

$$\Delta P = g\left(\rho_m - \rho_w\right)\Delta h,$$

with $\Delta h$ the ridge elevation above the reference ocean floor — 3547 m at
100 Ma from the half-space cooling law. That pressure difference acts over the
plate thickness $h$, so

$$F_\text{ridge} = g\left(\rho_m - \rho_w\right)\Delta h\,h .$$

The demo tabulates it:

```text
      h (km)       F (N/m)
          40      3.20e+12
          60      4.80e+12
          80      6.40e+12
         100      8.00e+12
```

The ambiguity is entirely in $h$, the thickness over which the pressure
difference acts, and $h$ is *not* a well-defined quantity: it is roughly the
depth at which the cooling plate reaches the adiabat, which is exactly where the
thermal model stops being sharp. The honest statement is a range of order
$10^{12}$ N/m, an order of magnitude below slab pull, and remarkably insensitive
to everything except $h$.

Ridge push is a real force and it is not the main one. It does have one
qualitative signature that matters: because it acts away from the ridge, it is
the reason a plate with no attached slab still tends to move, and it is a
significant term in the force balance of the large, slowly moving continental
plates whose slab pull is weak.

## 4. Physical reasoning: basal drag and its sign

A plate moving at speed $v$ over an asthenosphere of viscosity $\eta$ and
thickness $d$ experiences a shear traction

$$\tau = \frac{\eta v}{d},$$

and the force per unit length of the plate margin is that traction times the
plate dimension along the direction of motion:

```text
    eta (Pa s)  v (mm/a)    tau (Pa)    F (N/m), L=10 000 km
         1e+19        50   7.922e+04                7.92e+11
         4e+19        50   3.169e+05                3.17e+12
         1e+20        50   7.922e+05                7.92e+12
         1e+21        50   7.922e+06                7.92e+13
```

With a $4\times10^{19}$ Pa·s channel the traction is a few times $10^5$ Pa — a
tenth of a megapascal — and the force over a 10 000 km plate is of order
$10^{12}$ N/m, the same order as ridge push.

What the table cannot tell you is the **sign**. If the mantle beneath a plate
moves faster than the plate, the drag drives it; if the mantle moves slower, the
drag resists. Both cases exist: some plates appear to be dragged by a
fast-moving asthenosphere and some appear to be held back by it. A force
magnitude without a direction is only half an answer, and this is the honest
reason basal drag is the least settled of the candidates.

The same remark applies to **slab suction**, which is not a separate force but
the mantle-flow part of the interaction: the descending slab drives flow in the
surrounding mantle, and that flow exerts a traction on both plates. It is
included in any self-consistent convection calculation and it is not separately
measurable, which is why it appears in the table of §1 and not as a section of
this lesson.

## 5. Quantitative treatment: the viscosity the balance requires

Now do the thing that makes the lesson more than a ranking. Assume slab pull is
the dominant drive and that it is balanced by drag over the plate:

$$F_\text{slab}\,L_\text{trench} = \tau\,A_\text{plate}
= \frac{\eta v}{d}L_\text{plate}L_\text{trench}
\quad\Longrightarrow\quad
\eta = \frac{F_\text{slab}\,d}{v\,L_\text{plate}} .$$

```text
    v (mm/a)  L_plate (km)    eta (Pa s)
          20          5000      2.92e+21
          50         10000      5.84e+20
          80         10000      3.65e+20
          50         15000      3.89e+20
```

For plausible plate speeds and sizes the required viscosity lands between
$10^{20}$ and $10^{21}$ Pa·s. That is the range that **post-glacial rebound**
infers independently, from the relaxation of a Pleistocene ice load — a
completely different observation, on a completely different timescale, using
none of the inputs of this calculation.

Two independently determined numbers agreeing is the strongest kind of evidence
available in this subject, and here the agreement has a particular force because
viscosity is the *only* free parameter the force balance has. Change the plate
speed and the geometry and the required viscosity moves within a factor of a
few; the rebound value stays where it is. That is what a consistency check looks
like.

## 6. Quantitative treatment: does the mantle convect?

$$\mathrm{Ra} = \frac{\rho g\alpha\Delta T d^3}{\eta\kappa}.$$

```text
    eta (Pa s)    d (km)          Ra    Ra/Ra_crit
         1e+21       700    4.33e+05      4.33e+02
         1e+21      2890    3.05e+07      3.05e+04
         1e+22       700    4.33e+04      4.33e+01
         1e+22      2890    3.05e+06      3.05e+03
```

The critical Rayleigh number for the onset of convection in a fluid layer is of
order $10^3$. Every case in the table exceeds it, by one to nearly five orders
of magnitude. So the question is never *whether* the mantle convects: it is
whether the convection is layered, how fast it is, and how the plates couple to
it. Those are the live questions of the subject, and they are why the relative
importance of the three forces in §2 to §4 is an area of active measurement
rather than a settled fact.

The magnitude of the Rayleigh number has a second consequence worth noting. A
vigorously convecting fluid has thin thermal boundary layers, and the Earth's
plates *are* those boundary layers: the lithosphere is the cold upper boundary
layer of a convecting cell, and the slabs are the descending limbs. Plate
tectonics is therefore what mantle convection looks like when the fluid's
surface is a cold, strong, brittle lid rather than a free-slip boundary — which
is a statement about the temperature dependence of viscosity, and it is the
reason the Earth has plates while Venus may not.

## 7. Assumptions and regime of validity

| Assumption | Where it holds | What breaks without it |
|---|---|---|
| The slab's density excess is thermal only | The upper mantle, above the phase changes | Below 410 and 660 km the phase changes contribute, and their sign depends on the mineralogy |
| The slab is a rigid sheet of constant thickness | As a first model | Slabs thicken, buckle and may stagnate at 660 km |
| Steady-state force balance | On million-year timescales | The earthquake cycle is not steady; interseismic stress accumulates and is released episodically |
| Newtonian viscosity for the drag law | Diffusion creep, low stress | Dislocation creep gives a non-Newtonian effective viscosity that depends on stress |
| One viscosity for the asthenosphere | An order-of-magnitude estimate | The real viscosity varies with depth, temperature and water content |
| A constant plate dimension $L$ | A rectangular plate | Real plates have complex geometry and the drag integral is over the actual shape |

The steady-state row is the one that explains why this lesson is about forces
rather than about accelerations. On a million-year timescale a plate is in
dynamic equilibrium: the forces balance and there is no acceleration to measure.
The *instantaneous* state is very different, and it is the one the earthquake
cycle lives in.

## 8. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| Force per unit length | N/m | $\text{Pa}\,\text{m} = \text{N/m}$ |
| Density excess | kg/m³ | $[\rho\alpha\Delta T]$ |
| Mass excess per unit area | kg/m² | $[\rho\alpha\Delta T\,h]$ |
| Traction $\tau$ | Pa | $[\eta v/d] = \text{Pa·s}\cdot\text{m/s}/\text{m}$ |
| Viscosity | Pa·s | $10^{21}$ for the mantle |
| Rayleigh number | dimensionless | All units cancel |
| Slab length | m | 660 km = $6.6\times10^5$ m |

Three checks.

**The slab-pull check.** $F = g\,\Delta m\,L$ with $\Delta m$ the mass excess per
unit area in kg/m² and $L$ in m gives
$(\text{m/s}^2)(\text{kg/m}^2)(\text{m}) = \text{kg·m/s}^2/\text{m} = \text{N/m}$.
For the 100 Ma slab, $9.81 \times 7.142\times10^6 \times 6.6\times10^5 =
4.62\times10^{13}$ N/m, matching the table.

**The traction check.** $[\eta v/d]$ with $\eta$ in Pa·s, $v$ in m/s and $d$ in m
gives Pa. A speed left in mm/a gives a traction smaller by
$3.17\times10^{10}$, which is a strikingly small number rather than an obviously
wrong one — the reason unit discipline matters more than usual in this subject.

**The Rayleigh-number check.** $\rho g\alpha\Delta T d^3$ has units
$(\text{kg/m}^3)(\text{m/s}^2)(\text{K}^{-1})(\text{K})(\text{m}^3) =
\text{kg·m/s}^2 = \text{N}$, and $\eta\kappa$ has units
$(\text{Pa·s})(\text{m}^2/\text{s}) = \text{Pa·m}^2 = \text{N}$. The ratio is
dimensionless, which is the whole reason the Rayleigh number is meaningful as a
criterion for a system described in any units.

## 9. Python demonstration

[`code/driving_forces_demo.py`](./code/driving_forces_demo.py) computes the slab
buoyancy from the half-space cooling profile, the ridge-push estimate across a
range of ambiguity in $h$, the basal traction across a range of viscosities, the
viscosity required by the force balance, and the mantle Rayleigh number.

Sections §2 to §6 above quote its output. What each demonstrates:

- **§2**: slab pull is derived from the *same* thermal model as seafloor
  subsidence, so the two predictions share their inputs and cannot be tuned
  independently. That is a strong form of consistency.
- **§3**: the honest treatment of an ill-defined parameter. Printing the range
  is more informative than picking one value.
- **§5**: the consistency check with post-glacial rebound, which is the
  argument that turns a set of force estimates into a model of the mantle.
- **§6**: the Rayleigh number, which settles the qualitative question and leaves
  the quantitative ones open.

One methodological point about the demo worth carrying into any force estimate:
every result is printed with the *sensitivity that dominates its uncertainty* —
slab length for slab pull, thickness for ridge push, viscosity for drag. A force
quoted without its dominant sensitivity cannot be compared with another force,
because the reader cannot tell whether a difference of a factor of two is a
disagreement or a definition.

## 10. Common mistakes

1. **Quoting slab pull as a single number.** It depends on the slab length
   counted, and the range is a factor of about four.
2. **Forgetting the dip.** The along-slab force is not the horizontal force that
   moves the plate.
3. **Treating ridge push as negligible.** It is an order of magnitude below slab
   pull, and it is decisive for plates without a significant attached slab.
4. **Giving basal drag a magnitude and no sign.** The direction is the
   unresolved part of the problem.
5. **Using a laboratory creep law at mantle strain rates without stating the
   extrapolation.** It spans ten orders of magnitude and dominates the
   uncertainty.
6. **Assuming one viscosity.** Both the drag law and the rebound inversion need
   a profile, and the effective value depends on the depth sampled.
7. **Treating the force balance as instantaneous.** On a million-year timescale
   it is; in an earthquake cycle it is not.
8. **Concluding that a high Rayleigh number settles the dynamics.** It settles
   that the mantle convects, and nothing about how.

## 11. Real-world applications

- **Plate-motion models and their frame.** The forces here are what a kinematic
  model in [04-02-04](./04-plate-motion-frames.md) parameterises, and an
  absolute frame is defined by removing the net rotation that the forces do not
  constrain.
- **Post-glacial rebound and sea level.** The viscosity profile that rebound
  inverts is the same quantity that appears in the drag law
  ([04-01-02](../01-earth-structure/02-lithosphere-asthenosphere.md)).
- **Geothermal and heat-flow studies.** The convection calculation sets the
  mantle heat flux that a surface heat-flow measurement is compared with
  ([12-03-02 Global Heat Flow and Its Distribution](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/02-heat-flow-global.md)).
- **Long-term seismic hazard.** The plate speed that drives a megathrust is a
  force-balance result on long timescales, and it sets the moment budget of
  [04-02-05](./05-tectonics-hazards.md).
- **Comparative planetology.** Whether a planet has plate tectonics at all
  depends on whether its lithosphere can stay strong enough to be a plate, which
  is a statement about viscosity and Rayleigh number
  ([04-08 Planetary Science](../08-planetary-science/README.md)).

## 12. Related lessons

- [04-02-02 Divergent, Convergent and Transform Boundaries](./02-plate-boundaries.md)
  — the kinematics these forces produce.
- [04-02-04 Plate Motion Frames, Euler Poles and Global Models](./04-plate-motion-frames.md)
  — how the resulting motion is described globally.
- [04-01-02 Lithosphere, Asthenosphere and the Rheological Definition](../01-earth-structure/02-lithosphere-asthenosphere.md)
  — the viscosity that appears in every calculation here.
- [02-06-06 Mantle Convection and Rayleigh–Bénard Instability](../../02-physics/06-fluid-mechanics/06-mantle-convection.md)
  — the convection theory behind §6.
- [13-01-04 Driving Forces, Stress Fields and Intraplate Stress](../../13-geodynamics-tectonics/01-geodynamic-principles/04-forces-and-stresses.md)
  — the same problem treated as a full stress balance.

Exercises:
[`exercises/03-driving-forces-exercises.md`](./exercises/03-driving-forces-exercises.md)
and
[`exercises/03-driving-forces-solutions.md`](./exercises/03-driving-forces-solutions.md).

## Self-assessment checklist

- [ ] I can list the candidate driving forces and the mechanism behind each.
      (§1)
- [ ] I can compute slab pull from a thermal profile and state its dependence on
      age and on slab length. (§2)
- [ ] I can explain why slab pull and seafloor depth share their inputs. (§2)
- [ ] I can compute ridge push and state the ambiguity in it. (§3)
- [ ] I can compute a basal traction and a drag force. (§4)
- [ ] I can explain why the sign of basal drag is unresolved. (§4)
- [ ] I can derive the viscosity the force balance requires and compare it with
      the rebound value. (§5)
- [ ] I can compute a mantle Rayleigh number and interpret it. (§6)
- [ ] I can rank the forces and state which parts of the ranking are robust.
      (§1, §6)
- [ ] I can check the units of a force per unit length, a traction and a
      Rayleigh number. (§8)
