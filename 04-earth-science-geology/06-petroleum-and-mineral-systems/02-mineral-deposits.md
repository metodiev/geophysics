---
id: 04-06-02
title: "Mineral Deposit Types and Their Geophysical Signatures"
level: advanced
prereqs: ["04-01-03", "04-01-04", "04-01-05"]
estimated_minutes: 75
tags: [mineral-deposits, porphyry, iocg, vms, magmatic-sulphide, laterite, placer, property-contrast]
---

# Mineral Deposit Types and Their Geophysical Signatures

A mineral deposit is an **anomalous concentration** of one or more elements,
produced by a specific sequence of processes, hosted in a specific set of rocks.
For a geophysicist the operative question is never "where is the copper?" but
**"which physical property changes, by how much, over what volume, and at what
depth?"** That is the entire content of this lesson. Every deposit type below is
presented as a *process* that concentrates a mineral, followed by the *property*
that the mineral assemblage changes, followed by the *method* that measures that
property.

Two structural facts make the subject tractable.

- **Minerals have distinct physical properties.** Magnetite changes
  susceptibility by orders of magnitude; sulphides change conductivity by orders
  of magnitude; dense oxides and silicates change density; potassium-bearing
  alteration minerals change natural gamma emission. Each of these is a physical
  contrast, and each maps to a method.
- **Alteration is usually a larger target than the ore.** A porphyry ore body
  might be a few hundred metres across; the potassic, phyllic, argillic and
  propylitic alteration halo around it is kilometres across, and the minerals in
  that halo (magnetite, sericite, clay, K-feldspar) are exactly what magnetics,
  radiometrics and electromagnetics detect. In exploration the halo is usually
  the detection and the ore is the intersection.

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** the main deposit types (porphyry, IOCG, VMS, magmatic sulphide,
   laterite, placer) by the process that concentrates the metal.
2. **State**, for each type, which physical property differs and therefore which
   method could detect it.
3. **Compute** the magnetic anomaly of an induced sphere, its peak, its zero
   crossing and its half-width, and invert the half-width for depth.
4. **Compute** the gravity anomaly of the same body and explain why the two
   methods respond differently to the same target.
5. **Compute** a normal-incidence reflection coefficient at an ore–host contact
   and explain when an ore body is a seismic target.
6. **Compute** Hashin–Shtrikman conductivity bounds for a sulphide-bearing rock
   and explain why **connectivity** rather than abundance controls the
   electromagnetic response.
7. **Compute** the density of a placer from a heavy-mineral fraction and the
   gravity anomaly of the resulting layer.
8. **State** the approximations behind each calculation and the conditions under
   which each fails.

## Prerequisites

- [04-01-03 Rock-Forming Minerals and Their Physical Properties](../01-earth-structure/03-mineralogy.md)
  — the properties that make each mineral a target.
- [04-01-04 Igneous, Sedimentary and Metamorphic Rocks](../01-earth-structure/04-rock-types.md)
  — the hosts and the alteration assemblages.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
  — the density, velocity and porosity relations used in §8.

---

## 1. Why a deposit type matters more than an anomaly

An anomaly is a measurement. A deposit type is a *model* that says which
properties should be anomalous and in what spatial arrangement. The distinction is
practical:

- A porphyry has a **magnetic high** in the potassic core, a **magnetic low**
  where magnetite has been destroyed by phyllic alteration, a **potassium high**
  in the same core from K-feldspar and biotite, a **chargeability high** from
  disseminated sulphide, and a **resistivity low** from the clay halo. The
  *pattern*, not any single anomaly, is the target.
- A massive sulphide body is a **conductivity high**, a **density high**, a
  **velocity high**, and — for pyrrhotite-bearing ores — a **magnetic high**. It
  is a compact three-dimensional object, so it is a gravity and EM target when it
  is large, and often invisible to those methods when it is small.
- A placer is a **density** and **susceptibility** contrast in an otherwise
  unremarkable sand: a magnetic or gravimetric *pattern* in a channel.

The rest of this lesson is that table in detail.

## 2. Porphyry deposits

**Process.** A shallow, water-rich granitic intrusion releases metal-bearing
aqueous fluid into a fractured carapace. Cooling and reaction produce a
**zonal alteration** assemblage around the intrusion, and ore minerals
(chalcopyrite, bornite, molybdenite) precipitate where the fluid cools and
boils.

**Alteration zones and their properties.**

| Zone | Characteristic minerals | Physical property changed |
|---|---|---|
| Potassic (core) | Biotite, K-feldspar, magnetite | Susceptibility (magnetite **high**), K (radioactivity **high**) |
| Phyllic | Sericite, pyrite, quartz | Magnetite destroyed (**magnetic low**), resistivity **low** (sericite + pyrite), chargeability **high** |
| Argillic | Clay minerals | Resistivity **low**, K **low** |
| Propylitic (outer) | Chlorite, epidote, calcite | Magnetic and radiometric **neutral or slightly low** |

**Method mapping.** Aeromagnetics for the magnetite pattern; gamma-ray
spectrometry for potassium; induced polarisation for disseminated sulphide;
resistivity/EM for the clay halo; gravity for the intrusive body's density
contrast where the host is more mafic.

**Physical reasoning.** The observation that makes porphyry exploration work is
that **magnetite and sulphide are anticorrelated within a single system**: the
core retains magnetite and is magnetic, the phyllic shell has its magnetite
destroyed and its pyrite added and is not. A magnetic low inside a magnetic high,
with a chargeability high in the low, is a *system* signature rather than an
isolated anomaly.

## 3. IOCG deposits

**Process.** Iron-oxide–copper–gold systems occur where oxidised, saline brines
have altered and mineralised a host, producing magnetite–haematite bodies with
copper and gold. They are not tied to a single intrusion, and their ages and
settings are varied.

**Properties.** Very high density (magnetite/hematite), very high susceptibility
(if magnetite rather than haematite dominates), and locally high radioactivity
where potassic alteration is present. The host is often a granite or a
volcanic sequence with a moderate susceptibility, so the contrast is large.

**Method mapping.** This is the *easiest* target in the list for potential-field
methods: a dense and magnetic body at a few hundred metres to a few kilometres
depth gives a coincident gravity and magnetic high. The diagnostic difficulty is
mineralogical — magnetite and haematite have the same density but very different
susceptibility, so a magnetite-poor IOCG is a gravity target and a
magnetite-rich one is both.

## 4. VMS and SEDEX deposits

**Process.** Volcanogenic massive sulphide (VMS) deposits precipitate at or near
the seafloor from hydrothermal fluid venting through volcanic rock; sedimentary
exhalative (SEDEX) deposits precipitate from fluid venting into a basin. Both
produce **stratiform, massive** sulphide bodies.

**Properties.** Massive sulphide is conductive (electrical and electromagnetic),
dense, seismically fast, and — where pyrrhotite is a significant phase —
magnetic. The host volcanic or sedimentary sequence is comparatively resistive,
so the conductivity contrast is one to three orders of magnitude.

**Method mapping.** Electromagnetics is the primary method, because the target is
a compact, highly conductive body at shallow to moderate depth. Gravity responds
to the density contrast where the body is thick enough. Seismic reflection can
image a large massive body because the impedance contrast with the host is
large and positive.

**Why EM works here and fails for a disseminated deposit.** The response depends
on the body's **conductance** (conductivity times thickness) and on the
**connectivity** of the conducting phase. A massive body has both; disseminated
grains in a resistive matrix usually have neither.

## 5. Magmatic sulphide deposits

**Process.** An immiscible sulphide liquid segregates from a mafic or ultramafic
magma, scavenges Ni, Cu and the platinum-group elements, and settles or is
trapped in a conduit, reef or contact.

**Properties.** Pyrrhotite (conductive and weakly magnetic) plus pentlandite and
chalcopyrite (conductive). The ore is **conductive and moderately magnetic** and
denser than the host silicate rock; the host itself is often magnetic, which is
the diagnostic difficulty.

**Method mapping.** EM for the sulphide, magnetics for the host and for
pyrrhotite, gravity for the density contrast, and — because the deposits are
often in layered or conduit geometries — a combination of the three to locate and
orient the body.

## 6. Laterite and supergene deposits

**Process.** Intense tropical weathering leaches silica and alkalis from the
upper part of a rock and concentrates the residually insoluble or immobile
elements: iron and aluminium as oxides, nickel as hydrous silicates in the
saprolite below a ferruginous cap.

**Properties.** The saprolite is **less dense** than the fresh rock (porosity is
high, mineralogy is hydrous), clay-rich and therefore **more conductive**, and
poorly magnetic except where maghemite and goethite carry a weak remanence. The
profile is layered: ferruginous cap, saprolite, saprock, fresh rock.

**Method mapping.** Gravity for the density contrast (a *low* over thick
saprolite), electrical and electromagnetic methods for the conductive clay, and
gamma-ray spectrometry — because weathering leaches potassium and uranium, so the
profile has a characteristic **radiometric signature**. The radiometric method
here is a pathfinder for the *weathering profile*, not for the metal.

## 7. Placers

**Process.** Physical concentration of dense, chemically resistant minerals
(magnetite, ilmenite, rutile, zircon, monazite, cassiterite, gold, diamond) in
flowing water: a sorting process, so placers are found in channel and beach
sediments with a hydrodynamic trap.

**Properties.** A **density** contrast and — where the heavy minerals are
magnetic (magnetite, ilmenite) — a **susceptibility** contrast, in a matrix of
otherwise unremarkable quartz sand. Monazite brings a **radioactivity** contrast
from thorium; gold brings only density.

**Method mapping.** Magnetics is usually the primary method because magnetite and
ilmenite dominate the heavy-mineral assemblage; gravity for the density contrast;
radiometrics where monazite or zircon are present; seismic and GPR for the
geometry of the host channel or beach.

## 8. The property-contrast table

The table is the deliverable of this lesson. Read it as: *the mineral that
concentrates the value, the property it changes, and the method that measures
it.*

| Deposit type | Concentrated phase | Property contrast | Primary method |
|---|---|---|---|
| Porphyry | Magnetite, pyrite, chalcopyrite | Susceptibility (high then low), K (high), conductivity/chargeability | Magnetics, radiometrics, IP, EM |
| IOCG | Magnetite / haematite | Density (high), susceptibility (high if magnetite) | Gravity, magnetics |
| VMS / SEDEX | Pyrite, pyrrhotite, sphalerite, galena | Conductivity (very high), density, velocity | EM, gravity, seismic |
| Magmatic sulphide | Pyrrhotite + pentlandite | Conductivity, susceptibility, density | EM, magnetics, gravity |
| Laterite / supergene | Fe and Al oxides, Ni silicates | Density (low in saprolite), conductivity (clay), radioactivity | Gravity, EM/ERT, radiometrics |
| Placer | Magnetite, ilmenite, zircon, monazite, gold | Density, susceptibility, radioactivity (Th) | Magnetics, gravity, radiometrics |
| Skarn | Magnetite, calc-silicates | Susceptibility, density, velocity | Magnetics, gravity, seismic |
| BIF-hosted iron | Magnetite, haematite | Susceptibility, density | Magnetics, gravity |
| Epithermal Au-Ag | Silica, adularia, clay | Resistivity (high in silicification, low in clay), K | Resistivity, radiometrics |

**The unifying statement.** In every row the detection question is the same
three-part question: (i) which property differs, (ii) by how much at the
deposit's scale, and (iii) at what depth. A deposit that fails any part is
invisible to that method — which is why multi-method surveys exist, and why a
single method can miss a large deposit entirely.

## 9. Quantitative treatment with units

| Quantity | Symbol | Unit | Value used here (MODELLED) |
|---|---|---|---|
| Inducing field | $B$ | nT | 50 000 |
| Susceptibility | $k$ | SI | 0.10 |
| Body radius | $a$ | m | 100 |
| Depth to centre | $z$ | m | 200 |
| Density contrast | $\Delta\rho$ | kg m⁻³ | 150–1500 |
| Host conductivity | $\sigma_1$ | S m⁻¹ | $10^{-3}$ |
| Sulphide conductivity | $\sigma_2$ | S m⁻¹ | $10^{3}$ |

**Magnetic sphere.** With $H = B/\mu_0 = 39.79$ A m⁻¹, the induced moment is
$m = kH(4/3)\pi a^{3} = 1.667\times10^{7}$ A m². The vertical anomaly at the
surface above the centre is

$$
\Delta Z(0) = \frac{\mu_0}{4\pi}\frac{2m}{z^{3}}
= \frac{\mu_0 m}{2\pi z^{3}} = 4.17\times10^{-7}\ \mathrm{T} = 417\ \mathrm{nT}.
$$

The shape function $(2 - u^{2})/(1+u^{2})^{5/2}$ with $u = x/z$ is
**independent of $k$, $a$ and $\mu_0$**, so its zero crossing at $u = \sqrt2$
and its half-maximum at $u = 0.5007$ are universal: **$z = 1.997\,x_{1/2}$**.
Amplitude gives the moment, width gives the depth, and the two are separable.

**Gravity sphere.** For the same geometry,
$\Delta g(0) = (4/3)\pi G\Delta\rho a^{3}/z^{2}$, which for
$\Delta\rho = 1500$ kg m⁻³ is $1.05\times10^{-5}$ m s⁻² $= 1.05$ mGal. Both
anomalies scale as $z^{-3}$ at fixed mass, so depth is what decides
detectability, not the size of the body.

**Reflection coefficient.** For massive sulphide
($\rho = 4200$ kg m⁻³, $v_P = 6000$ m s⁻¹) in a volcanic host
($\rho = 2750$ kg m⁻³, $v_P = 5500$ m s⁻¹), $R = +0.25$ — a very large
positive reflection, and one of the strongest in any exploration setting.

**Conductivity bounds.** The Hashin–Shtrikman bounds for a two-phase mixture
give, for 10 per cent sulphide in a resistive matrix, a bulk conductivity between
$1.33\times10^{-3}$ and $6.90\times10^{1}$ S m⁻¹ — a **four-order-of-magnitude**
span. That span *is* the percolation problem: whether the sulphide is connected.

## 10. Assumptions and regime of validity

**Potential-field anomalies.**

1. The sphere formulas are **dipole** approximations, valid for $z \gtrsim 3a$.
   Shallower than that the finite body size matters and the amplitudes are
   overestimates.
2. Remanent magnetisation is neglected. Many orebodies carry a strong remanence
   that changes the anomaly *shape*, so an induced-only interpretation can be
   wrong even when the amplitude is right.
3. Uniform susceptibility and density are assumed. Ore bodies are heterogeneous
   by nature.
4. The regional field must be removed before interpretation; a misfit regional
   becomes a spurious anomaly.

**Conductivity.**

1. The Hashin–Shtrikman bounds are *variational*: they bracket any geometry, so
   they constrain but do not predict. The upper bound corresponds to the
   sulphide being the continuous phase, which is geometrically impossible at low
   fraction.
2. Induced polarisation measures a **polarisation** (reported in millivolts per
   volt) whose relation to sulphide content is mineral-specific and
   empirically calibrated. No universal conversion exists, so no number is quoted
   here.
3. A conductive overburden or a clay horizon can attenuate or mask an EM
   response entirely.

**Seismic.**

1. A thin body (thickness much less than the wavelength) is a **tuning** effect
   rather than a discrete reflection, and its amplitude depends on thickness in a
   nonlinear way.
2. Steeply dipping or geometrically complex orebodies require migration, and
   their seismic response is often a scattering pattern rather than a reflection.

## 11. Python demonstration

[`code/mineral_deposits_demo.py`](./code/mineral_deposits_demo.py) computes the
magnetic anomaly of an induced sphere and its half-width depth rule, the gravity
anomaly for four density contrasts and its depth attenuation, reflection
coefficients at an ore contact, Hashin–Shtrikman conductivity bounds for
sulphide-bearing rock, and the density and anomalies of a placer.

```text
  COMPUTED dipole moment m = k H (4/3) pi a^3 = 1.6667e+07 A m^2
  COMPUTED peak anomaly at x = 0: 416.7 nT
  COMPUTED zero crossing at x = sqrt(2) z = 282.8 m (independent of k and a)
  COMPUTED the half-maximum point lies at u = x/z = 0.500683,
  so the horizontal distance from the centre to the half-maximum is
  0.5007 z and, inverted, z = 1/0.5007 x_half = 1.9973 x_half.
    massive sulphide in volcanics        d_rho =   1500 kg/m^3:     1.048 mGal
    porphyry with disseminated sulphide  d_rho =    150 kg/m^3:     0.105 mGal
    z =    500 m: gravity    0.168 mGal, magnetic     26.7 nT
    massive sulphide (VMS)        : R = +0.2498 (+24.98 per cent)
  MODELLED host sigma = 1e-03 S/m (1000 ohm m)
    0.10       1.3333e-03             750.00       6.8966e+01             0.0145
    f = 0.20: rho =  2512.0 kg/m^3  (d_rho =  +357.0)
    f = 0.20, t =  20.0 m: d_rho =   357.0 kg/m^3, anomaly =   0.299 mGal
```

### What to observe

- The zero crossing at $282.8$ m is exactly $\sqrt2\,z$, and the half-width rule
  $z = 1.997 x_{1/2}$ is exact **independent of the magnetisation**. A magnetic
  survey can locate a body whose magnetisation is entirely unknown, which is why
  magnetics is a *depth* method as much as a detection method.
- Gravity and magnetics fall off identically with depth at fixed mass
  ($26.7$ nT and $0.168$ mGal at 500 m versus $416.7$ nT and $1.048$ mGal at
  200 m), so a deep target requires both a larger body and a better instrument —
  there is no way to trade depth for contrast.
- The conductivity bounds at 10 per cent sulphide span four orders of magnitude.
  *This* is the quantitative statement of why massive and stringer sulphide are
  detectable and disseminated grains are not: it is connectivity, not grade.
- A 20 per cent magnetite placer 20 m thick gives $0.299$ mGal, and the same
  magnetite gives a magnetic anomaly that depends on the sheet's width, strike
  and magnetic latitude — which is why the *magnetic* answer is not a single
  number and the demo refuses to print one.

## 12. Common mistakes

1. **Interpreting an anomaly without a deposit model.** An anomaly is not a
   target; a pattern is.
2. **Using the sphere formula for a shallow body.** The dipole approximation
   needs $z \gtrsim 3a$.
3. **Ignoring remanence.** A strong remanence changes the anomaly shape and can
   invert the apparent depth.
4. **Treating a magnetic low as an absence of mineralisation.** In a porphyry it
   may be the phyllic shell, which is part of the target.
5. **Equating conductivity with sulphide content.** Connectivity decides.
6. **Quoting a chargeability without the instrument and procedure.** It is an
   empirical, calibration-dependent quantity.
7. **Assuming a conductive anomaly is shallow.** A conductive overburden screens
   the target, and an EM anomaly may be the overburden itself.
8. **Forgetting that ore bodies are three-dimensional.** A 2-D interpretation of a
   compact body misestimates its volume, and therefore everything derived from it.
9. **Assuming regional removal is objective.** It is an interpretation, and the
   residual depends on the method chosen.
10. **Quoting a grade or a tonnage.** Those are assay and economic quantities; no
    such number is computed or stated in this lesson.

## 13. Real-world applications

- **Regional targeting.** Aeromagnetics, gravity and radiometrics at regional
  scale define the belts and the structures within which deposit-scale work is
  then done ([11-01-01 The Exploration Lifecycle](../../11-exploration-geophysics/01-exploration-workflow/01-exploration-lifecycle.md)).
- **Deposit-scale detection.** EM and IP for sulphide, gravity for dense oxides,
  magnetics for magnetite — each chosen from the contrast, not from habit.
- **Alteration mapping.** Radiometrics for potassium, magnetics for
  magnetite-destructive alteration, resistivity for clay: the halo mapped at
  kilometre scale around a metre-scale ore body.
- **Mine-scale and grade control.** High-resolution magnetics, EM and
  radiometrics on the bench, and geophysics for the geotechnical and
  hydrological context
  ([11-06-01 Site Investigation](../../11-exploration-geophysics/06-geotechnical-and-engineering/01-site-investigation.md)).
- **Mineral sands and placers.** Magnetics and radiometrics for heavy-mineral
  distribution and monazite, over large soft-rock areas.
- **Environmental and legacy-mining work.** Acid-generating sulphide waste is
  mapped by the same conductivity methods as the ore
  ([14-04 Contaminant and Environmental Geophysics](../../14-hydrology-hydrogeophysics/04-contaminant-and-environmental/README.md)).

## 14. Further reading

- **Robb, L. *Introduction to Ore-Forming Processes* (Blackwell).** The process
  classification used in §2–§7. Level: undergraduate to graduate textbook.
- **Hedenquist, J. W., & Lowenstern, J. B. (1994). The role of magmas in the
  formation of hydrothermal ore deposits.** *Nature*. Level: advanced; the
  porphyry model of §2.
- **Seedorff, E., & others (2005). Porphyry deposits.** *Economic Geology 100th
  Anniversary Volume*. Level: advanced; the alteration zoning and its geometry.
- **Franklin, J. M., & others on VMS deposits.** The classification and setting
  of volcanogenic massive sulphide. Level: advanced.
- **Naldrett, A. J. *Magmatic Sulfide Deposits* (Springer).** The sulphide
  segregation mechanism of §5. Level: graduate.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics*
  (Cambridge).** The potential-field formulas and their interpretation, including
  the half-width rules of §9. Level: graduate textbook.
- **Nabighian, M. N. (ed.) *Electromagnetic Methods in Applied Geophysics*
  (SEG).** The EM theory behind the conductivity discussion, with the limits of
  each method. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 15. Related lessons

- [01 Source, Reservoir, Seal and Trap: The Petroleum System](./01-petroleum-system.md)
  — the same contrast logic in a fluid system.
- [03 Geothermal Systems, Heat Flow and Resource Assessment](./03-geothermal-systems.md)
  — which shares the resource-assessment structure and the same caution about
  recovery factors.
- [04 Aquifer Types and Groundwater Occurrence](./04-groundwater-aquifers.md)
  — where near-surface conductivity mapping is met again, at shallow scale.
- [04-01-03 Rock-Forming Minerals and Their Physical Properties](../01-earth-structure/03-mineralogy.md)
  — the mineral-scale origin of every contrast in §8.
- [04-04-04 Fractures, Joints and Their Geophysical Signature](../04-structural-geology/04-fractures-joints.md)
  — the structural control on where a deposit sits.
- [11-02-01 Deposit Signatures](../../11-exploration-geophysics/02-mineral-exploration/01-deposit-signatures.md)
  — the exploration-side treatment of the same table.
- [11-02-06 IP for Minerals](../../11-exploration-geophysics/02-mineral-exploration/06-ip-for-minerals.md)
  — the chargeability method in practice.

Exercises:
[`exercises/02-mineral-deposits-exercises.md`](./exercises/02-mineral-deposits-exercises.md)
and
[`exercises/02-mineral-deposits-solutions.md`](./exercises/02-mineral-deposits-solutions.md).

## Self-assessment checklist

- [ ] I can classify the six main deposit types by process. (§2–§7)
- [ ] For any deposit type I can name the property contrast and a method. (§8)
- [ ] I can compute a magnetic sphere anomaly and invert its half-width for
      depth. (§9, §11)
- [ ] I can compute a gravity sphere anomaly and explain the common depth
      dependence. (§9)
- [ ] I can compute a reflection coefficient at an ore contact and say when
      seismic is a suitable method. (§9)
- [ ] I can compute Hashin–Shtrikman conductivity bounds and state why they are
      bounds rather than predictions. (§9, §10)
- [ ] I can compute a placer density from a heavy-mineral fraction. (§11)
- [ ] I can state when the dipole approximation fails and what remanence does to
      an interpretation. (§10)
- [ ] I can explain why an alteration halo is usually the detection and the ore
      body is the intersection. (§1, §13)
