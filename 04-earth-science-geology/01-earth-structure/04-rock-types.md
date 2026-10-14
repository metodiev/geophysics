---
id: 04-01-04
title: "Igneous, Sedimentary and Metamorphic Rocks"
level: beginner
prereqs: ["04-01-03", "03-05-03"]
estimated_minutes: 75
tags: [igneous, sedimentary, metamorphic, rock-classification, qapf, grain-size, facies]
---

# Igneous, Sedimentary and Metamorphic Rocks

Geologists classify rocks by how they formed, and geophysicists care about
classification only because it predicts physical properties. This lesson makes
the connection explicit: each of the three great rock classes is produced by a
different process, each process leaves a different texture and a different
mineral assemblage, and each assemblage occupies a different range of density,
velocity and porosity.

The lesson is built on three **decision procedures**, implemented and checked in
the demo, because a classification is not a vocabulary list. It is a rule that
takes measurements and returns a name:

- **Igneous rocks** are classified by their mode — the proportions of quartz
  (Q), alkali feldspar (A) and plagioclase (P) — positioned in the QAPF
  triangle. A volcanic rock of the same chemistry is classified by its silica
  content on the TAS diagram instead, because a fine-grained rock has no
  measurable mode.
- **Sedimentary rocks** are classified by grain size and sorting, both of which
  are measured, and both of which control the porosity and permeability that a
  hydrogeophysical survey will see.
- **Metamorphic rocks** are classified by **facies**, which is a position in the
  pressure–temperature plane. That is the important one for geophysics: it means
  metamorphic grade records a thermal history, not a depth.

## Learning objectives

By the end of this lesson you will be able to:

1. **Apply** the QAPF classification to a modal analysis, including the
   normalisation of Q, A and P.
2. **Explain** why a plutonic and a volcanic rock of the same chemistry have
   different names, and what each classification is based on.
3. **Convert** a grain size to the phi scale and assign a Wentworth class.
4. **Compute** the Folk and Ward graphical statistics of a grain-size
   distribution and interpret the sorting value.
5. **Explain** why sorting, rather than grain size alone, controls porosity and
   permeability.
6. **Place** a metamorphic assemblage in the facies grid and read the implied
   thermal gradient from it.
7. **Give** the physical-property range of each rock class, with the overlaps
   stated rather than hidden.
8. **Distinguish** a mineralogical density contrast from a porosity-related
   density contrast, and say which methods can separate them.

## Prerequisites

- [04-01-03 Rock-Forming Minerals and Their Physical Properties](./03-mineralogy.md)
  — the minerals these rocks are made of, and their densities.
- [03-05-03 Maps, Cross-Sections and Geological Symbology](../../03-scientific-computing/05-plotting-and-visualisation/03-maps-and-cross-sections.md)
  — how a classification is drawn on a map, and why the symbol set is standard.

## 1. The three classes, and the process that defines each

| Class | Formed by | Texture | Dominant control on properties |
|---|---|---|---|
| Igneous | Cooling of melt or lava | Crystalline; grain size records cooling rate | Mafic mineral content, and porosity if vesicular |
| Sedimentary | Deposition, then compaction and cementation | Clastic, biogenic or chemical | Porosity and sorting, then mineralogy |
| Metamorphic | Solid-state recrystallisation under changed $P$–$T$ | Foliated or non-foliated | Fabric (anisotropy), then mineralogy |

**Igneous rocks** crystallise from a liquid. Slow cooling below the surface
gives large crystals (plutonic, e.g. granite, gabbro); fast cooling at the
surface gives small crystals or glass (volcanic, e.g. basalt, rhyolite). The
same magma therefore carries two names depending on its cooling history, and
that is a statement about *texture* as much as composition.

**Sedimentary rocks** are deposited, mostly in layers. Their defining
geophysical property is porosity: a clastic sediment is a granular framework
plus voids, and the voids can be filled with brine, oil, gas or air. The
depositional process sorts the grains, and the sorting determines how much pore
space survives.

**Metamorphic rocks** are recrystallised in the solid state. The minerals that
grow are those stable at the prevailing pressure and temperature, so the
assemblage is a thermometer and a barometer. A foliation develops when the
minerals grow with a preferred orientation, which makes the rock *elastically
anisotropic* — a property a seismic survey can measure
([05-04-05 Anisotropy in Rocks](../../05-core-geophysics/04-rock-physics/05-anisotropy-rock.md)).

## 2. Igneous rocks: the QAPF classification, applied

Normalise the modal percentages of quartz, alkali feldspar and plagioclase to
100 per cent, and read the rock name from the position in the triangle: the
vertical axis is $Q$ and the horizontal axis is
$A/(A+P) \times 100$.

The demo classifies five modal analyses and checks each name against the one a
petrologist would give:

```text
  modal analysis         Q     A     P  mafic  colour index  QAPF name
  a granite             25    35    30     10           10%  monzogranite
  a granodiorite        22    18    45     15           15%  granodiorite
  a tonalite            25     5    60     10           10%  tonalite
  a gabbro               3     6    61     30           30%  diorite / gabbro
  a syenite              4    80    10      6            6%  syenite
```

Every name is recovered. Two consequences follow that matter for geophysics.

**The colour index is what tracks the physical properties.** The rock names
depend on the feldspar ratio, but a granite and a gabbro differ physically
because the gabbro has 30 per cent mafic minerals — olivine, pyroxene,
amphibole — with densities of 3.0 to 3.4 g/cm³ and velocities far above those
of quartz and feldspar. A classification by name tells a geophysicist almost
nothing; a classification by colour index tells them the density and the
velocity range.

**The silica content is the volcanic proxy.** A fine-grained rock has no
measurable mode, so a volcanic rock with the same chemistry is classified on the
TAS diagram by its $\mathrm{SiO_2}$ content — ultramafic below 45 wt per cent,
mafic 45 to 52, intermediate 52 to 63, felsic 63 to 77. The dividing lines are
chemistry, and chemistry correlates with the mafic content, which is why the
two classifications agree in substance while using different measurements.

## 3. Sedimentary rocks: the phi scale and sorting statistics

Grain size varies over four orders of magnitude within one deposit, so it is
measured on a logarithmic scale:

$$\phi = -\log_2(d/\text{mm}).$$

Larger grains give smaller (even negative) phi. The Wentworth classes attach
names to phi intervals — gravel above $-1$, sand from $-1$ to $4$, silt from
$4$ to $8$, clay below $8$ — and the class boundaries are conventional.

The quantity that controls the physics is not the mean grain size but the
**sorting**: how narrow the distribution is. Sorting is quantified by the Folk
and Ward graphical statistics, computed from percentiles of the cumulative
curve read in phi units:

$$M_z = \frac{\phi_{16}+\phi_{50}+\phi_{84}}{3}, \qquad
\sigma_I = \frac{\phi_{84}-\phi_{16}}{4} + \frac{\phi_{95}-\phi_{5}}{6.6}.$$

The demo generates a synthetic sample by mixing two log-normal populations,
which is what a moderately sorted sand actually looks like, and computes:

```text
    phi5 =  1.024   phi16 =  1.462   phi25 =  1.702   phi50 =  2.318
    phi75 =  3.070   phi84 =  3.388   phi95 =  3.954

    mean       Mz   = (phi16 + phi50 + phi84)/3          =  2.390
    sorting    sigma_I = (phi84-phi16)/4 + (phi95-phi5)/6.6 =  0.925
    skewness   Sk_I  = the two-term expression above        =  0.114
    kurtosis   K_G   = (phi95-phi5)/(2.44 (phi75-phi25))    =  0.878

  Sorting value 0.925 -> moderately sorted (Folk and Ward classes).
  Median grain size in mm: 0.2005 mm (fine sand).
```

The median grain size is a fine sand and the sorting is "moderately sorted" —
a mixture, as intended. The interpretation of a sorting value is graded
(under 0.35 very well sorted, up to 2.0 poorly sorted), and the grade is what a
sedimentologist records.

Why sorting is the geophysically important statistic: a perfectly sorted sand
packs to 36 to 40 per cent porosity regardless of grain size, and a *poorly*
sorted mixture of the same grains packs to much less, because the fine fraction
occupies the voids the coarse fraction left. Permeability falls further still,
because the fine particles block the pore *throats* rather than the pores. So
grain size sets the permeability scale and sorting decides how much of that
scale survives — and porosity and permeability are what a hydrogeophysical
survey is trying to map
([14-01-02 Aquifer Types and Properties](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/02-aquifer-types-and-properties.md)).

## 4. Metamorphic rocks: facies as a position in the P–T plane

A metamorphic facies is a set of mineral assemblages that grew under a similar
range of pressure and temperature. The facies fields are conventionally drawn on
a $P$–$T$ diagram, and the demo classifies `(P, T)` points against approximate
teaching boundaries:

```text
  cold subduction (linear, 10 K/km):
      z (km)   P (GPa)   T (C)   facies                        diagnostic assemblage
          25      0.69     260   blueschist                    glaucophane + lawsonite
          35      0.96     360   greenschist                   chlorite + actinolite + albite
          45      1.24     460   eclogite                      garnet + omphacite

  standard continental (conductive, q_m = 21 mW/m^2, A = 1.0 uW/m^3):
          25      0.69     345   blueschist                    glaucophane + lawsonite
          35      0.96     549   amphibolite                   hornblende + plagioclase
          45      1.24     793   eclogite                      garnet + omphacite

  extended / hot (conductive, q_m = 30 mW/m^2, A = 2.5 uW/m^3):
          15      0.41     302   greenschist                   chlorite + actinolite + albite
          25      0.69     622   amphibolite                   hornblende + plagioclase
          35      0.96    1042   granulite / partial melt      anhydrous + melt
```

At 35 km, where the pressure is 0.96 GPa in all three columns, the cold
subduction geotherm gives greenschist at 360 °C, the standard continental
geotherm gives amphibolite at 549 °C, and the extended geotherm gives a
granulite at 1042 °C. Same pressure, same depth, three different rocks.

That is the quantitative form of the lesson's most important statement about
metamorphic rocks: **grade is not depth**. It is a position in the $P$–$T$ plane,
and a rock's assemblage records the *path* it took through that plane. A
blueschist found in a mountain belt is evidence that a cold slab was there,
which is a tectonic conclusion recovered from a mineral assemblage.

The two geotherm models in the table differ in a way worth noticing. A purely
linear geotherm rises without limit and would give absurd temperatures at 45 km.
The conductive geotherm with radiogenic heat production flattens, because the
flux grows with depth as the crust generates heat, so the continental geotherm
reaches only about 550 °C at the Moho rather than the 1100 °C a linear
extrapolation would give. Reading a burial depth out of an assemblage therefore
requires a thermal model, not just a thermometer — see
[02-05-06 Geotherms and Heat Flow](../../02-physics/05-thermodynamics/06-geotherms.md).

### A caution about the boxes

The standard continental geotherm at 25 km lands at 345 °C and 0.69 GPa, just
inside the blueschist box used above. Real blueschist terranes are recognised by
the low geothermal gradient their assemblages imply and by their association
with other cold-subduction rocks, not by a single $P$–$T$ point. Moving one
boundary by 50 °C moves whole rows of the table, and that sensitivity is a
property of the classification rather than of the Earth. The exercise set asks
for the boundary to be moved and the consequence reported, because the habit is
worth acquiring.

## 5. Quantitative treatment: the property ranges by class

```text
  rock class                           rho_grain        porosity      rho_bulk (dry)
  granite (igneous, felsic)            2.60-2.70      0.005-0.02           2.55-2.69
  basalt (igneous, mafic)              2.85-3.00      0.010-0.10           2.56-2.97
  gabbro (igneous, mafic)              2.90-3.10      0.005-0.03           2.81-3.08
  peridotite (mantle)                  3.20-3.40      0.001-0.01           3.17-3.40
  sandstone (clastic)                  2.65-2.70      0.100-0.30           1.85-2.43
  shale (clastic)                      2.65-2.75      0.050-0.25           1.99-2.61
  limestone (carbonate)                2.70-2.75      0.020-0.20           2.16-2.69
  gneiss (metamorphic)                 2.65-2.80      0.005-0.03           2.57-2.79
  slate (metamorphic)                  2.70-2.80      0.005-0.02           2.65-2.79
```

Every range overlaps its neighbours, and the overlap is the honest part of the
table. Two rows carry the lesson.

**Sandstone versus granite: a porosity contrast.** Their grain densities are
nearly identical, 2.65 to 2.70 g/cm³, yet the sandstone's bulk density reaches
down to 1.85 against the granite's floor of 2.55 — a contrast of about
27 per cent, produced entirely by porosity. A gravity survey separates them,
and what it is mapping is porosity and fluid content rather than mineralogy.

**Peridotite versus gabbro: a mineralogical contrast.** 3.2 to 3.4 against 2.9
to 3.1 g/cm³, a contrast of about 15 per cent with essentially zero porosity on
either side. This is the contrast that makes the Moho visible in a gravity
profile, and it is mineralogical rather than porosity-related.

The two contrasts look identical in a density measurement and completely
different in a photoelectric or a seismic measurement, which is the reason
practitioners run more than one method. Distinguishing them requires a second
observable, and
[04-01-05](./05-rock-physics-basics.md) supplies it.

## 6. Assumptions and regime of validity

| Assumption | Where it holds | What breaks without it |
|---|---|---|
| The QAPF classification applies to coarse-grained rocks | Plutonic rocks with a measurable mode | Volcanic rocks need the TAS chemical classification |
| Modal percentages are representative | Samples larger than the largest grain | A thin section of a coarse rock can be unrepresentative |
| Wentworth boundaries are fixed | Everywhere; they are conventions | Different authors use slightly different boundaries for the gravel/sand limit |
| Folk and Ward statistics describe the distribution | Unimodal or mildly bimodal distributions | A strongly bimodal distribution has a graphical mean between its modes and the mean is misleading |
| Facies boundaries are reaction-defined | Never exactly; they depend on bulk composition | The teaching boxes are approximations of curved, composition-dependent boundaries |
| A rock class has a property range | As a prior | Real property ranges overlap between classes, and within one class they can exceed the between-class contrast |

The bimodality row is worth a comment. A grain-size distribution with two modes
— a sand with a gravel admixture, for instance — has a graphical mean that lies
between the modes where almost no grains are, and the sorting statistic is then
a measure of the mixing rather than of a depositional process. The right move is
to describe the two populations separately, which is what a
sedimentologist does and what the exercise set asks for.

## 7. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| Grain size $d$ | mm, µm | 1 mm = 1000 µm |
| Phi $\phi$ | dimensionless | $-\log_2$ of a length in mm; the reference unit must be stated |
| Sorting $\sigma_I$ | phi units | Dimensionless but meaningless without the phi reference |
| Modal percentage | per cent | Must sum to 100 after normalisation |
| Pressure | GPa | 1 GPa ≈ 33 – 36 km in the crust |
| Temperature | °C or K | A difference of 1 K equals a difference of 1 °C |
| Density | kg/m³ | 1 g/cm³ = 1000 kg/m³ |

The phi check is the one that catches people. $\phi = -\log_2(d/\text{mm})$
forces the reference length to be millimetres, so a grain size entered in
micrometres gives a phi that is 9.97 too large — which happens to look like a
plausible clay rather than an obvious error. Always write the reference unit.

The pressure–depth check. $P = \rho g z$ with $\rho = 2800$ kg/m³ gives 1 GPa at
$z = 1\times10^9/(2800 \times 9.81) = 36$ km, which is the conversion used in the
metamorphic table. In the mantle, at 3300 kg/m³, the same pressure is reached at
31 km, so the conversion is depth- and rock-dependent and should be recomputed
rather than remembered.

## 8. Python demonstration

[`code/rock_types_demo.py`](./code/rock_types_demo.py) implements the three
classification procedures, the grain-size statistics, the facies grid for three
geotherms, and the property-range table. Each classification is checked against
the expected name — the demo prints `OK` or `expected <name>` for every row, so
a wrong implementation is visible rather than plausible.

The three sections quoted in §2, §3 and §4 above are the substance of it. What
each one demonstrates:

- **§2**: the QAPF partition works as a decision procedure, and the colour index
  is the quantity that carries the physical information.
- **§3**: the sorting statistic is computed from a synthetic distribution rather
  than quoted, and the value it returns is consistent with the way the sample
  was constructed. The synthetic sample uses a fixed random seed, so a reader
  who runs the demo gets the same numbers.
- **§4**: the same `(P, T)` classification returns three different facies for
  three geotherms at the same depth, which is the quantitative statement of
  §4's lesson.

There is one deliberate simplification in §4's table and it is worth stating.
The facies decision procedure used is a set of **boxes**, whereas the real
boundaries are curved and composition-dependent. The demo says so in its own
output, and the exercise set asks for the sensitivity of the answer to moving
one boundary, which is the responsible way to use a simplified classification.

## 9. Common mistakes

1. **Classifying a volcanic rock by its mode.** A fine-grained rock has no
   measurable mode; use the chemistry.
2. **Equating a rock name with a property range.** "Granite" spans a range of
   density and velocity, and a weathered granite can have more porosity than a
   fresh sandstone.
3. **Forgetting the phi reference unit.** $\phi = -\log_2(d/\text{mm})$, always
   in millimetres; other units shift every boundary by a constant.
4. **Treating a graphical mean as a physical mean for a bimodal sample.** It
   falls between the modes, where no grains are.
5. **Reading a burial depth out of a metamorphic assemblage without a thermal
   model.** Facies is a position in the $P$–$T$ plane, and the plane needs a
   geotherm to be converted into depth.
6. **Assuming a density contrast identifies a rock type.** Porosity and pore
   fluid produce contrasts as large as mineralogy.
7. **Ignoring fabric.** A foliated metamorphic rock is elastically anisotropic,
   and an isotropic velocity model will mis-fit its seismic response.
8. **Using a classification boundary as a fact about nature.** Classification
   boundaries are conventions chosen for communication; the transitions in
   nature are continuous.

## 10. Real-world applications

- **Reservoir characterisation.** The porosity and permeability of a clastic
  reservoir, and the diagenesis that controls them, are what determine whether a
  seismic or an EM survey can map the fluids
  ([06-01 Petroleum Systems](../06-petroleum-and-mineral-systems/01-petroleum-system.md)).
- **Aquifer mapping.** Sorting and grain size are the two parameters in a
  porosity–permeability relation, and they are what a hydrogeophysical survey
  is calibrated against
  ([14-03-01 Porosity–Permeability Relations](../../14-hydrology-hydrogeophysics/03-petrophysics-hydrology/01-porosity-permeability-relations.md)).
- **Igneous province mapping with potential fields.** The mafic content of an
  igneous body sets both its density and its magnetisation, so a gravity and a
  magnetic survey map a province's composition.
- **Metamorphic terrane interpretation.** Facies mapping is how a thermal
  history is reconstructed, and the seismic anisotropy of a foliated terrane is
  how the fabric is mapped at depth.
- **Engineering geology and slope stability.** The weathering profile of a rock
  class, and its clay content, are what control the geotechnical properties that
  a near-surface survey measures
  ([04-07-03 Landslides](../07-geologic-hazards/03-landslides.md)).

## 11. Further reading

- **Le Maitre, R. W. (ed.) *Igneous Rocks: A Classification and Glossary of
  Terms* (Cambridge University Press).** The IUGS classification, which defines
  the QAPF and TAS diagrams used here. Level: reference.
- **Folk, R. L. *Petrology of Sedimentary Rocks* (Hemphill).** The source of the
  graphical statistics in §3, and still the clearest account of what sorting
  means. Level: intermediate.
- **Folk, R. L., & Ward, W. C. (1957). Brazos River bar: a study in the
  significance of grain size parameters. *Journal of Sedimentary Petrology* 27,
  3–26.** The original paper behind the sorting formula. Level: advanced.
- **Bucher, K., & Grapes, R. *Petrogenesis of Metamorphic Rocks* (Springer).**
  Facies, reaction boundaries and the $P$–$T$ paths that produce them.
  Level: advanced.
- **Blatt, H., Tracy, R. J., & Owens, B. E. *Petrology: Igneous, Sedimentary
  and Metamorphic* (Freeman).** A single text covering all three classes, which
  is what this lesson compresses. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04-01-03 Rock-Forming Minerals and Their Physical Properties](./03-mineralogy.md)
  — the minerals the classification is built from.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](./05-rock-physics-basics.md)
  — the mixture laws that turn a rock class into a number.
- [04-05 Geomorphology and Quaternary Geology](../05-geomorphology-and-quaternary/README.md)
  — where the sedimentary processes behind sorting are treated.
- [04-06 Petroleum, Mineral and Geothermal Systems](../06-petroleum-and-mineral-systems/README.md)
  — where a reservoir's rock type becomes an economic target.
- [03-05-03 Maps, Cross-Sections and Geological Symbology](../../03-scientific-computing/05-plotting-and-visualisation/03-maps-and-cross-sections.md)
  — how a classified rock body is drawn and communicated.

Exercises:
[`exercises/04-rock-types-exercises.md`](./exercises/04-rock-types-exercises.md)
and
[`exercises/04-rock-types-solutions.md`](./exercises/04-rock-types-solutions.md).

## Self-assessment checklist

- [ ] I can apply the QAPF classification to a modal analysis. (§2, §8)
- [ ] I can explain why a plutonic and a volcanic rock of the same chemistry
      have different names. (§2)
- [ ] I can convert a grain size to phi and assign a Wentworth class. (§3)
- [ ] I can compute $M_z$ and $\sigma_I$ from percentiles. (§3)
- [ ] I can interpret a sorting value and state why sorting controls
      permeability. (§3)
- [ ] I can read a facies from a $(P, T)$ point and state why grade is not
      depth. (§4)
- [ ] I can give the property ranges of the main rock classes and identify the
      overlaps. (§5)
- [ ] I can distinguish a porosity-related from a mineralogical density
      contrast, and name a second method that separates them. (§5)
- [ ] I can state the limits of a box classification. (§4, §6)
- [ ] I can check the phi and pressure–depth conversions. (§7)
