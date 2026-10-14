---
id: 04-01-03
title: "Rock-Forming Minerals and Their Physical Properties"
level: intermediate
prereqs: ["04-01-01", "02-11-03"]
estimated_minutes: 75
tags: [mineralogy, density, elastic-moduli, silicates, photoelectric, magnetic-minerals]
---

# Rock-Forming Minerals and Their Physical Properties

A rock is an aggregate of minerals, and a geophysical measurement responds to
the *aggregate*, not to the rock's name. The bridge between the two is the
mineral: if you know which minerals are present in what proportions, you can
predict a density and an elastic modulus, and if you measure a density and an
elastic modulus you can constrain the mineralogy. Both directions are used
constantly in this curriculum.

This lesson builds three mineral properties from first principles rather than
listing them, because the derivations are the reason to believe the numbers:

- **Density from the crystal structure.** A unit cell contains a known number
  of formula units in a known volume, so the density is arithmetic. Every
  mineral in the demo reproduces its measured density to about one per cent,
  which is the check that the structure and the composition are consistent.
- **Elastic moduli from measured velocities.** $G = \rho v_s^2$ and
  $K = \rho(v_p^2 - \frac43 v_s^2)$ invert a measurement into the modulus that
  controls deformation. This is the direction a seismic interpreter works.
- **Mean atomic number and electron density.** These set the photoelectric and
  density responses of a borehole log, and they are *not* monotonic in
  density — which is the reason two different nuclear logs are run instead of
  one.

Four minerals do most of the work in the crust: quartz, the feldspars, the
micas and the clay minerals. Three more do most of the work in the mantle:
olivine, pyroxene and garnet. Two oxide and sulfide minerals — magnetite and
pyrite — matter out of proportion to their abundance because they carry the
magnetisation and the conductivity anomaly that a survey detects.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a mineral's density from its unit-cell volume, cell contents and
   formula mass, and state the check that makes the result credible.
2. **Compute** the bulk and shear moduli, Young's modulus and Poisson's ratio
   of a mineral from its measured $v_p$, $v_s$ and density.
3. **Explain** why iron-bearing minerals are both the dense minerals and the
   magnetically important ones.
4. **Compute** a mean atomic number and explain its role in the photoelectric
   log.
5. **Explain** why quartz, olivine and calcite share a mean atomic number while
   their densities differ, and what that implies for lithology discrimination.
6. **State** the diagnostic physical properties — density, hardness, cleavage,
   magnetism, radioactivity — and say which geophysical method each one serves.
7. **Convert** a grain density and a porosity into a bulk density, and state
   why porosity often dominates mineralogy in the density a survey measures.
8. **Distinguish** a mineral property from a rock property, and say which of the
   two a typical measurement is sensitive to.

## Prerequisites

- [04-01-01 Crust, Mantle, Core: Seismological and Geochemical Evidence](./01-layered-earth.md)
  — where these minerals sit, and the property ranges they produce.
- [02-11-03 Seismic Velocities, Elastic Moduli and Mineralogy](../../02-physics/11-physics-of-earths-interior-and-atmosphere/03-seismic-parameter-relations.md)
  — the equations connecting moduli and velocities, derived.

## 1. The minerals that matter

| Mineral | Formula | Role | Density (g/cm³) | Diagnostic property |
|---|---|---|---|---|
| Quartz | $\mathrm{SiO_2}$ | Continental crust, sandstone | 2.65 | Hardness 7, no cleavage, no magnetism |
| Alkali feldspar | $(\mathrm{K,Na})\mathrm{AlSi_3O_8}$ | Most abundant crustal mineral | 2.55 – 2.63 | Two cleavages at 90° |
| Plagioclase | $(\mathrm{Na,Ca})\mathrm{AlSi_3O_8}$ | Most abundant crustal mineral | 2.62 – 2.76 | Two cleavages, striations |
| Biotite / muscovite | sheet silicates | Micas | 2.8 – 3.1 | Perfect basal cleavage, biotite magnetic |
| Clay minerals | sheet silicates | Shale, soil | 2.6 – 2.8 | Very fine, high surface area, low permeability |
| Olivine | $(\mathrm{Mg,Fe})_2\mathrm{SiO_4}$ | Dominant upper-mantle mineral | 3.2 – 4.4 | High velocity, green, no cleavage |
| Pyroxene | $(\mathrm{Mg,Fe,Ca})\mathrm{Si_2O_6}$ | Mantle and mafic rocks | 3.2 – 3.6 | Two cleavages near 90° |
| Garnet | $\mathrm{X_3Y_2Si_3O_{12}}$ | Metamorphic, deep crust | 3.6 – 4.3 | Isotropic, hard, dense |
| Calcite / dolomite | $\mathrm{CaCO_3}$ / $\mathrm{CaMg(CO_3)_2}$ | Limestone, dolostone | 2.71 / 2.87 | Hardness 3, reacts with acid |
| Halite | $\mathrm{NaCl}$ | Evaporite, salt domes | 2.17 | Cubic cleavage, soluble |
| Magnetite | $\mathrm{Fe_3O_4}$ | Magnetic anomaly source | 5.17 | Strongly magnetic |
| Pyrite | $\mathrm{FeS_2}$ | Sulfide deposits | 5.01 | Metallic, conductive |

Three things to notice before any calculation.

**The range is a factor of two.** From quartz at 2.65 to magnetite at 5.17
g/cm³. A rock's density is therefore largely a statement about its mineralogy,
and a density contrast of 10 per cent between two rock bodies is a
mineralogical statement.

**Iron is the lever.** Every mineral above 3.5 g/cm³ contains iron. Iron also
carries the remanent and induced magnetisation that a magnetic survey measures,
and it is the abundant element whose electron configuration gives the
iron-bearing silicates their colour and their opacity. Density and magnetisation
are correlated in rocks through iron content, which is why a gravity and a
magnetic survey are so often flown together.

**Calcite and dolomite are the odd ones out.** They have moderate densities but
unusually low shear stiffness relative to their bulk modulus, which gives them
a high Poisson's ratio and a distinctive seismic response. A carbonate
reservoir does not look like a sandstone reservoir on a seismic section, and
the reason is in
[§2](#2-quantitative-treatment-density-from-the-unit-cell).

## 2. Quantitative treatment: density from the unit cell

The density of a mineral follows from its crystal structure:

$$\rho = \frac{Z\,M}{N_A\,V_\text{cell}},$$

with $Z$ the number of formula units per cell, $M$ the formula mass in g/mol,
$N_A$ Avogadro's number and $V_\text{cell}$ the cell volume in cm³.

This is not an approximation or a fit. If the structure and the composition are
both right, the density is exact to the precision of the cell volume. The demo
computes it for six minerals and compares with the measured density:

```text
  mineral       formula     Z   V (A^3)  rho_calc  rho_meas   diff %
  alpha-quartz  SiO2        3    112.99     2.649      2.65     -0.0
  forsterite    Mg2SiO4     4    290.30     3.219      3.22     -0.0
  calcite       CaCO3       6    367.90     2.710      2.71      0.0
  halite        NaCl        4    179.40     2.164      2.17     -0.3
  pyrite        FeS2        4    159.03     5.011      5.01      0.0
  hematite      Fe2O3       6    302.70     5.256      5.26     -0.1
```

The agreement is the point. A density computed from a structure that is wrong,
or with the wrong number of formula units, would be off by 20 per cent or more,
not by 0.1 per cent. This is the kind of check that turns an assertion into a
derivation, and it costs one line of code.

## 3. Quantitative treatment: elastic moduli from velocities

For a homogeneous isotropic elastic solid the moduli follow from measured
velocities by

$$G = \rho v_s^2, \qquad K = \rho\left(v_p^2 - \tfrac{4}{3}v_s^2\right), \qquad
E = \frac{9KG}{3K+G}, \qquad \nu = \frac{3K-2G}{2(3K+G)}.$$

The demo inverts the tabulated velocities of the six minerals and prints the
result:

```text
  mineral         v_P (km/s)  v_S (km/s)   G (GPa)   K (GPa)   E (GPa)      nu
  alpha-quartz          6.05        4.09      44.3      37.9      95.7   0.079
  forsterite            8.55        5.03      81.5     126.8     201.3   0.235
  calcite               6.50        3.30      29.5      75.1      78.3   0.326
  halite                4.54        2.60      14.7      25.2      36.8   0.256
  pyrite                8.10        4.70     110.7     181.1     275.8   0.246
  hematite              8.50        5.00     131.5     204.7     324.9   0.235
```

Two rows are diagnostic. Quartz's Poisson's ratio, 0.079, is anomalously low:
quartz is stiff in shear relative to its resistance to compression. Calcite is
the opposite — 0.326 — because a carbonate is easy to compress and relatively
hard to shear compared with a silicate. Those two numbers are why a limestone
and a quartz sandstone of the same porosity have different $v_p/v_s$ ratios, and
why $v_p/v_s$ is used to discriminate lithology in a seismic reservoir study
([06-01-02 P and S Waves](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md)).

## 4. Physical reasoning: mean atomic number, and a trap

The photoelectric absorption cross section per electron scales roughly as the
cube of the atomic number, so the photoelectric response of a mineral is set by
its **mean atomic number**

$$\bar Z = \frac{\sum_i n_i Z_i}{\sum_i n_i},$$

averaged over the atoms of the formula unit. The demo computes it:

```text
  mineral           Zbar    Zbar^3   (Zbar/10)^3   rho_e (e/cm^3 x 1e24)
  alpha-quartz     10.00    1000.0          1.00                    0.80
  forsterite       10.00    1000.0          1.00                    0.96
  calcite          10.00    1000.0          1.00                    0.82
  halite           14.00    2744.0          2.74                    0.63
  pyrite           19.33    7226.4          7.23                    1.46
  hematite         15.20    3511.8          3.51                    1.51
```

Quartz, forsterite and calcite all have $\bar Z = 10.00$ exactly, because each
formula unit happens to average ten protons per atom: $(14 + 2\times8)/3 = 10$,
$(2\times12 + 14 + 4\times8)/7 = 10$, $(20 + 6 + 3\times8)/5 = 10$. Their
densities span a factor of 1.2, and a photoelectric log cannot tell them apart
at all.

Halite is the opposite case. It has the lowest density in the table, 2.17
g/cm³, and a mean atomic number of 14.0, so it stands out strongly on the
photoelectric curve and weakly on the density curve.

That is the reason the two nuclear logs are run together. The density log
responds to electrons per unit volume; the photoelectric log responds to the
atomic number. A mineral pair that is degenerate in one is usually separated in
the other, and the pair together separates lithologies that either one alone
confuses. A single measurement cannot resolve a two-dimensional ambiguity, and
this is a particularly clean example of the general rule.

## 5. Quantitative treatment: from mineral to rock density

A rock's density is the mineral density reduced by its porosity:

$$\rho_\text{bulk} = (1-\phi)\,\rho_\text{grain} + \phi\,\rho_\text{fluid},$$

with $\phi$ the porosity as a volume fraction. The demo tabulates it for a
quartz grain with water-filled pores:

```text
       phi  rho_bulk, dry (g/cm^3)   rho_bulk, water-sat  density contrast vs quartz
      0.00                   2.650                 2.650                        0.0%
      0.10                   2.385                 2.485                       -6.2%
      0.20                   2.120                 2.320                      -12.5%
      0.30                   1.855                 2.155                      -18.7%
```

A 30 per cent porosity sandstone is 19 per cent less dense than quartz, which is
a *larger* contrast than the one between quartz and calcite. And the same rock
saturated with brine instead of air differs by 300 kg/m³, which is comparable
with the entire mineralogical range of the common silicates.

The consequence for interpretation is uncomfortable and worth stating plainly.
**A density measurement does not distinguish "a different rock" from "the same
rock with different pores".** Separating the two needs a second measurement
that responds to the pore fluid or to the pore geometry — a seismic velocity, a
resistivity, or a nuclear log — and even then the separation relies on a model.
That is why rock physics is a subject rather than a table.

## 6. Assumptions and regime of validity

| Assumption | Where it holds | What breaks without it |
|---|---|---|
| The unit cell is the composition of the mineral | Everywhere; it is a definition | Solid solution changes $Z$ and $M$ together, so the density must be recomputed for the actual composition |
| $V_\text{cell}$ measured at ambient pressure | For crustal minerals near the surface | At 30 GPa the cell volume is 15 – 20 per cent smaller and the density correspondingly higher |
| The solid is isotropic | Almost never true for a single crystal | A single crystal is elastically anisotropic; the moduli above are orientation averages |
| The rock is a simple two-phase mixture | Clean sandstone, clean limestone | Clay, cement and multiple pore fluids each add a phase |
| $\bar Z$ from the formula unit | For minerals of known composition | Solid solution and trace elements change it, and heavy trace elements change it a lot |
| Tabulated velocities are representative | As a nominal value | Velocities vary with pressure, temperature, composition and defects |

The anisotropy row deserves emphasis. Quartz, olivine and calcite are all
strongly anisotropic single crystals: $v_p$ in a quartz crystal varies by about
20 per cent with direction. The moduli in §3 are values recovered from
*measured velocities of the mineral*, and if those velocities were measured on
a single crystal in one orientation, the numbers are orientation-specific. This
is why mineral-physics work quotes a full stiffness tensor $c_{ijkl}$ and why
the isotropic moduli above should be read as engineering averages.

The pressure row matters for the mantle. Forsterite's density at ambient
conditions is 3.22 g/cm³; at the base of the upper mantle the same mineral has
been compressed to about 3.6 g/cm³ and has transformed to wadsleyite or
ringwoodite, with a further density change at each transformation. Ambient
mineral densities are therefore the *starting point* for a mantle model, not
the model — which is the subject of
[02-11-02 Equations of State](../../02-physics/11-physics-of-earths-interior-and-atmosphere/02-equations-of-state.md).

## 7. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| Density | g/cm³, or kg/m³ in SI | 1 g/cm³ = 1000 kg/m³ |
| Cell volume | Å³ | 1 Å³ = $10^{-24}$ cm³ |
| Formula mass | g/mol | Numerically equal to the molar mass |
| Moduli | GPa, Pa | $[\rho v^2] = (\text{kg/m}^3)(\text{m/s})^2 = \text{Pa}$ |
| Poisson's ratio | dimensionless | Must lie in $-1 < \nu < 0.5$ |
| Mean atomic number | dimensionless | Between the lightest and heaviest element in the formula |

The density check, worked once. For quartz with $Z = 3$, $M = 60.083$ g/mol and
$V = 112.99$ Å³:

$$\rho = \frac{3 \times 60.083}{6.022\times10^{23} \times 112.99\times10^{-24}}
= \frac{180.25}{68.04} = 2.649\ \text{g/cm}^3 .$$

The units are consistent because $N_A V$ is a number of cells times a volume per
cell, which is a volume per mole — the molar volume, 22.7 cm³/mol here. That
reading is worth keeping: **a mineral's density is its formula mass divided by
its molar volume**, and the unit-cell calculation is one way of measuring the
molar volume.

The modulus check. $[\rho v_s^2]$ with $\rho = 2650$ kg/m³ and $v_s = 4090$ m/s
gives $4.43\times10^{10}$ Pa = 44.3 GPa, matching the table. A velocity entered
in km/s instead of m/s gives a modulus a million times too small, and the
resulting "mineral" would have the stiffness of foam.

## 8. Python demonstration

[`code/mineralogy_demo.py`](./code/mineralogy_demo.py) computes the six mineral
densities from their unit cells, inverts the tabulated velocities for the
elastic moduli, computes mean atomic numbers and electron densities, and
tabulates bulk densities against porosity. The structural and velocity data are
labelled `TABULATED` in the output; the densities and moduli are computed from
them and printed next to the measured values they are checked against.

The three sections of the output quoted in §2, §3 and §5 above are the whole
demonstration. What to look for in each:

- **§2**: the density differences are all below one per cent, so the structural
  data and the composition are consistent. This is a *verification*, not a
  prediction, and reporting it as a prediction would be dishonest.
- **§3**: the moduli span a factor of nine in $G$, so a change in mineralogy can
  move a rock's velocity substantially. That is the physical basis of seismic
  lithology discrimination.
- **§5**: a porosity change of 10 per cent moves the bulk density by more than a
  mineralogy change from quartz to calcite, which is the quantitative statement
  of §5's warning.

One further computation is worth doing by hand from the same tables, and the
exercise set asks for it: predict a density and a $v_p$ for a rock of stated
mineralogy and porosity, then compare with the measured values in the table of
§1. The exercise is the whole method of the next two lessons in miniature.

## 9. Common mistakes

1. **Treating a mineral density as a rock density.** Porosity, and the pore
   fluid, can move the bulk density further than mineralogy can.
2. **Assuming a density contrast implies a lithology contrast.** A density log
   cannot distinguish the two without help.
3. **Using ambient-pressure densities to model the mantle.** Compression to
   30 GPa changes the density by 15 per cent, and the phase changes change it
   again.
4. **Quoting an isotropic modulus for a strongly anisotropic mineral.** Quartz's
   $v_p$ varies by about 20 per cent with direction; the isotropic value is an
   average.
5. **Expecting the photoelectric log to separate silicates from carbonates.**
   Quartz, olivine and calcite all have $\bar Z = 10$.
6. **Confusing hardness with strength.** Mohs hardness is a scratch resistance,
   not a strength or a modulus, and diamond is not "stiffer" than steel in the
   elastic sense in the way the hardness scale suggests.
7. **Forgetting the density units.** $2.65$ g/cm³ is $2650$ kg/m³, and a mixture
   problem done in g/cm³ with one term in kg/m³ is a factor of 1000 wrong.
8. **Assuming a mineral name identifies a composition.** Plagioclase, olivine
   and garnet are solid solutions with a compositional range, and their
   properties vary across it.

## 10. Real-world applications

- **Gravity and magnetic surveying.** Density and magnetisation contrasts
  between rock bodies are mineralogical contrasts, and the two surveys are
  complementary because iron controls both
  ([08-03-01 Magnetic Anomaly Basics](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/01-magnetic-anomaly-basics.md)).
- **Borehole logging.** The density, photoelectric, neutron and natural-gamma
  curves are four different views of mineralogy and porosity, and their
  combination is what makes a log interpretation possible.
- **Carbonate and evaporite reservoirs.** Calcite's Poisson's ratio, and
  halite's photoelectric contrast, are routinely used to identify them.
- **Mine and ore-deposit geophysics.** Pyrite and magnetite are the minerals
  that make a sulfide body a conductivity or a magnetic anomaly, and their
  abundance is what an exploration programme is looking for.
- **Critical-mineral exploration.** The minerals that host lithium, rare earths
  and cobalt are dense, radioactive or magnetic in ways that an airborne survey
  can detect, and the mineralogy is what turns an anomaly into a target.

## 11. Further reading

- **Klein, C., & Dutrow, B. *Manual of Mineral Science* (Wiley).** The standard
  mineralogy text: structures, compositions, physical properties and the
  determinative tables. Level: intermediate.
- **Deer, W. A., Howie, R. A., & Zussman, J. *An Introduction to the
  Rock-Forming Minerals* (Pearson).** The reference work on the rock-forming
  minerals. Level: advanced.
- **Anderson, D. L. *Theory of the Earth* (Blackwell).** Chapters on mineral
  elasticity and the mineralogy of the mantle. Level: advanced.
- **Bassinot, F. C., & Labeyrie, L. D. (1996). *Mineral structure and
  density*.** Published tables of mineral densities computed from structures;
  useful as an independent check on any calculation of the kind in §2.
- **International Mineralogical Association, *Commission on New Minerals,
  Nomenclature and Classification*.** The authority for mineral names and
  formulae; confirm a formula there before relying on it.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04-01-04 Igneous, Sedimentary and Metamorphic Rocks](./04-rock-types.md) —
  how minerals are assembled into the rock classes.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](./05-rock-physics-basics.md)
  — the mixture laws this lesson stops short of.
- [04-01-02 Lithosphere, Asthenosphere and the Rheological Definition](./02-lithosphere-asthenosphere.md)
  — why the same mineral assemblage can be strong or weak.
- [05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)
  — effective-medium theory, Gassmann substitution and the velocity–porosity
  relations.
- [08-01-07 Rock Magnetism: Remanence, Susceptibility and Magnetic Mineralogy](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/07-rock-magnetism.md)
  — the magnetic minerals and what magnetisation a survey measures.

Exercises:
[`exercises/03-mineralogy-exercises.md`](./exercises/03-mineralogy-exercises.md)
and
[`exercises/03-mineralogy-solutions.md`](./exercises/03-mineralogy-solutions.md).

## Self-assessment checklist

- [ ] I can compute a mineral density from its unit cell and state the check.
      (§2)
- [ ] I can compute $G$, $K$, $E$ and $\nu$ from measured velocities. (§3)
- [ ] I can explain what a low and a high Poisson's ratio imply about a
      mineral's stiffness. (§3)
- [ ] I can compute a mean atomic number and explain its role in a
      photoelectric log. (§4)
- [ ] I can explain why quartz, olivine and calcite are photoelectrically
      indistinguishable. (§4)
- [ ] I can convert a grain density and a porosity into a bulk density. (§5)
- [ ] I can explain why porosity often dominates mineralogy in a measured
      density. (§5)
- [ ] I can state the regime in which ambient-pressure densities are valid, and
      what replaces them at depth. (§6)
- [ ] I can check the density and moduli calculations dimensionally. (§7)
- [ ] I can name the diagnostic physical properties and the method each serves.
      (§1, §10)
