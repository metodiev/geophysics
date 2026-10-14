---
id: 04-02-01
title: "Continental Drift to Plate Tectonics: The Evidence Trail"
level: beginner
prereqs: ["04-01-01", "08-01-06"]
estimated_minutes: 75
tags: [plate-tectonics, continental-drift, seafloor-spreading, magnetic-anomalies, heat-flow]
---

# Continental Drift to Plate Tectonics: The Evidence Trail

Plate tectonics was not accepted because it was elegant. It was accepted
because a set of *independent* observations, gathered by different methods over
about fifty years, all pointed the same way and none of the alternatives
survived. This lesson follows that trail, and it quantifies each link so that
the reader can see that each one is a measurement rather than a story.

The trail has four stages, and the lesson is organised around them:

1. **The fit and the fossils.** Continental outlines fit, and identical fossil
   assemblages and rock sequences appear on continents now separated by an
   ocean. This is suggestive but not decisive, and it is worth being clear that
   it is not decisive: a land bridge or a sunken continent could explain the
   same facts.
2. **Palaeomagnetism.** Rocks record the direction of the geomagnetic field
   when they form, and the directions point to different pole positions for
   different continents. Either the continents moved, or the field changed
   direction in a continent-specific way, which is not how a dipole
   works. See
   [08-01-06 Palaeomagnetism, Reversals and Magnetostratigraphy](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/06-palaeomagnetism.md).
3. **Seafloor spreading and magnetic anomalies.** Magnetic field surveys over
   the ocean floor found a pattern of stripes, symmetrical about the ridge,
   whose widths matched the independently dated reversal sequence. That is a
   *prediction* with a fingerprint in it, and it is the observation that made
   the theory.
4. **The thermal consequences.** Seafloor depth and heat flow both vary with
   age in the way a cooling plate predicts, with coefficients computed from
   laboratory thermal constants and not fitted. A model that explains the
   magnetisation must also explain the bathymetry, and it does.

The fourth stage is where the theory became quantitative, and it is also where
its first *failure* appeared: the half-space cooling model over-predicts the
depth and the heat flow of old ocean floor. That failure is part of the evidence
rather than an embarrassment, because it required the plate model and the
recognition of hydrothermal circulation, both of which are now accepted.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the observation that each stage of the evidence trail contributes,
   and what each one rules out.
2. **Explain** the Vine–Matthews–Morley hypothesis and why the *symmetry* of
   the anomaly pattern is a test rather than an ornament.
3. **Compute** a spreading rate from a magnetic anomaly pattern, and explain the
   role of the reversal timescale as an independent input.
4. **Derive** the half-space cooling subsidence and heat-flow laws and compute
   their coefficients from thermal constants.
5. **Evaluate** the agreement between the computed coefficients and the
   empirical ones, and state why the agreement is a test rather than a fit.
6. **State** where the half-space model fails and what the failure required.
7. **Estimate** the maximum age of the ocean floor from plate geometry, and
   explain why a finite maximum age is the strongest single argument for
   destruction.
8. **Explain** why the surface-area conservation argument forces creation and
   destruction to balance.

## Prerequisites

- [04-01-01 Crust, Mantle, Core: Seismological and Geochemical Evidence](../01-earth-structure/01-layered-earth.md)
  — the crust and mantle, and the property contrasts a ridge and a trench
  produce.
- [08-01-06 Palaeomagnetism, Reversals and Magnetostratigraphy](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/06-palaeomagnetism.md)
  — how a rock acquires a remanent magnetisation, and what the reversal
  sequence is.

## 1. The stages, and what each one rules out

| Stage | Observation | What it rules out |
|---|---|---|
| Continental fit and fossils | Matching coastlines, fossil assemblages, rock sequences | A coincidence, but not a land bridge or a sunken continent |
| Palaeomagnetic poles | Apparent polar wander paths differ between continents | A stable Earth with a geocentric axial dipole field |
| Magnetic anomaly stripes | Symmetrical stripes about ridges, widths matching the reversal timescale | Any mechanism that does not create new ocean floor at ridges |
| Depth and heat flow versus age | Both follow $\sqrt{t}$ and $1/\sqrt{t}$ with independently derived coefficients | A static ocean floor, and a model in which the ocean basins are old |

Read the third column as the content of the lesson. **A scientific observation
matters because of what it makes impossible**, not because of what it suggests,
and the trail is the sequence of alternatives being eliminated.

The continental fit is the weakest link and it is worth saying so explicitly,
because textbooks often present it as if it were conclusive. Alfred Wegener's
1912 argument assembled the fit, the fossils, the rock sequences and the
palaeoclimatic indicators, and it was still rejected — for a good reason. He
could not supply a mechanism. The mechanism came forty years later, from the
ocean floor, and from a technology (magnetic surveying from ships, and
radiometric dating of the ocean floor) that did not exist when he wrote.

## 2. Physical reasoning: the ridge as a tape recorder

Consider a ridge at which two plates diverge. Melt rises, solidifies, and
acquires a thermoremanent magnetisation parallel to the ambient geomagnetic
field at that moment — effectively when it cools through the Curie temperature
of its magnetic minerals. The field reverses at irregular intervals, and the
reversals are globally synchronous because they are generated in the core and
recorded by the field everywhere at once.

Now run the tape. Ocean floor created at time $t$ is carried away from the
ridge at the half-spreading rate, and it carries the polarity of time $t$. The
result is a sequence of normally and reversely magnetised stripes, whose widths
are the products of the interval durations and the spreading rate:

$$\text{width}_i = \text{rate} \times \Delta t_i .$$

Three consequences, each of which is testable.

- **Symmetry.** The two flanks are written from the same head, so the pattern
  must be mirror-symmetric about the ridge axis.
- **A fingerprint.** The reversal sequence is irregular. A set of stripe widths
  is therefore a specific pattern, and matching it identifies which reversal
  intervals you are looking at.
- **An inverse problem.** Given the pattern and the reversal timescale, the
  spreading rate is the scale factor. Given the rate, the pattern dates the
  crust.

The demo does the inverse problem explicitly. It synthesises a polarity
sequence, magnetises a synthetic ocean floor at a known half-spreading rate of
25.0 mm/a, and then searches a grid of trial rates for the one whose predicted
pattern matches:

```text
      half rate (mm/a)    misfit (rms)
                  22.0          0.3376
                  24.0          0.3021
                  25.0          0.0000
                  26.0          0.3009
                  28.0          0.3593

  Best rate on the grid: 25.0 mm/a; the input was
  25.0 mm/a.
```

The misfit is exactly zero at the true rate and large at every other, which is
what "the pattern is a fingerprint" means quantitatively. The exercise is a
forward-and-invert test: it verifies the *method*, not the Earth, and saying so
is part of using it honestly.

The symmetry test is the other half:

```text
  Symmetry test.  Compare the anomaly on the two flanks, matched by
  distance from the ridge: correlation = 1.000000.
```

A correlation of 1 is what the hypothesis predicts. A model in which the
magnetisation were random would give a correlation near zero, so this is a test
that the observation **could have failed** — which is the definition of a test
worth running. The measured stripe widths at 25 mm/a are 12.5 to 75 km, with a
mean of 33 km, and those are the scales a marine magnetic survey has to resolve.

## 3. Quantitative treatment: the cooling plate

The ocean floor is the top of a plate that cooled from the ridge. Treat it as a
half-space with its surface held at the seawater temperature and its interior
initially at the mantle temperature. The heat equation's solution is

$$T(z,t) = \Delta T\,\operatorname{erf}\!\left(\frac{z}{2\sqrt{\kappa t}}\right),$$

and the two observables follow from it.

**Subsidence by thermal contraction.** The plate's density increases as it
cools and it floats lower on the mantle:

$$d(t) - d(0) = \frac{2\rho_m\alpha\Delta T}{\rho_m - \rho_w}\sqrt{\frac{\kappa t}{\pi}}.$$

**Heat flow.** The surface gradient of the same solution gives

$$q(t) = \frac{k\,\Delta T}{\sqrt{\pi\kappa t}}.$$

Both laws are therefore $\sqrt{t}$ or $1/\sqrt{t}$ with coefficients fixed by
*measured* thermal constants — conductivity, diffusivity, thermal expansion,
the temperature contrast and the densities. Nothing is fitted.

The demo computes the coefficients and compares them with the empirical forms
that were established from bathymetry and heat-flow measurements:

```text
    coefficient = 6.314e-05 m per sqrt(s)
  At 100 Ma this gives a subsidence of 3547 m, and
  the empirical coefficient in d = 2500 + 350 sqrt(t) gives
  3500 m. The two agree to +1.3 per cent.

    age (Ma)   depth (m)   depth empirical    q (mW/m^2)   q empirical
         1.0        2855              2850         417.8         510.0
        20.0        4086              4065          93.4         114.0
       100.0        6047              6000          41.8          51.0
       150.0        6844              6787          34.1          41.6
```

The bathymetry agrees to about one per cent. That agreement is a genuine test,
because the thermal constants were measured in a laboratory and the bathymetry
was measured by ships, and the two had never been combined before the model
required it.

The heat flow is systematically lower than the empirical coefficient by about
20 per cent, and the direction of that discrepancy is informative: the
*computed* coefficient depends on the assumed thermal conductivity and on the
assumed temperature contrast, and a 20 per cent difference is within the
uncertainty of those two numbers taken together. A disagreement of that size
between two ways of getting the same coefficient is exactly the kind of thing
that should be reported rather than tuned away.

**Where the model fails.** The table shows the depth growing without limit as
$\sqrt{t}$ and the heat flow falling without limit as $1/\sqrt{t}$. Real ocean
floor flattens below about 5.5 to 6 km beyond roughly 70 Ma, and real heat flow
stops falling and rises slightly on the oldest crust. The half-space model
therefore fails on the oldest ocean floor, and the failure is informative: it
requires either a **plate model**, in which the lithosphere reaches a finite
thickness below which it stops cooling, or vigorous **hydrothermal
circulation**, which removes heat from young crust near the ridge and is the
reason measured heat flow near ridges falls below every conductive model. Both
are now accepted, and neither was in the original model.

## 4. Physical reasoning: why a finite maximum age is decisive

If ocean floor were only created and never destroyed, its age would span the age
of the Earth, exactly as continental crust does. It does not: no ocean floor is
older than a few hundred million years, while continental crust reaches 4 Ga.

That asymmetry is hard to explain without destruction. The demo estimates the
maximum age from the geometry — the crust formed at a ridge, carried at the
plate speed $v$ to a trench a distance $L$ away, is consumed after a time
$L/v$:

```text
    plate speed   50 mm/a, ridge-to-trench  8000 km -> maximum age 160 Ma
    plate speed   70 mm/a, ridge-to-trench 10000 km -> maximum age 143 Ma
    plate speed   30 mm/a, ridge-to-trench  6000 km -> maximum age 200 Ma
```

Every combination of plausible speeds and ocean widths gives a maximum age of
order $10^2$ Ma. The important observation is not the exact number but that it
is **finite** and that it is of the right order.

A second consequence is quantitative and forced by geometry. The Earth's surface
area is constant, so the rate at which crust is created must equal the rate at
which it is destroyed:

$$\sum_\text{ridges} v_\text{spreading} L_\text{ridge} =
\sum_\text{trenches} v_\text{convergence} L_\text{trench}
\quad\text{(approximately, for a lithosphere of constant thickness)}.$$

This is a strong constraint on any proposed plate model: a reconstruction in
which the rates do not balance requires an expanding or contracting Earth, and
the geodesy rules that out at the level of a few millimetres per year.

## 5. Quantitative treatment: the units that make the arithmetic easy

Two unit facts save a great deal of time in this subject.

- **1 mm/a = 1 km/Ma.** A rate of 25 mm/a means 25 km of new crust per million
  years on each flank. This is why the demo's magnetic-anomaly inversion can use
  kilometres and megayears interchangeably with millimetres per year, and why
  spreading rates can be read off a map as distances divided by ages.
- **A plate moving at 50 mm/a crosses the Atlantic in about 100 Ma.** A basin
  5000 km wide at 50 km/Ma takes 100 Ma. Orders of magnitude become immediate.

For the thermal calculation, the natural units are SI: $\kappa$ in m²/s, $t$ in
s, and the subsidence coefficient in m/$\sqrt{\text{s}}$. The demo's coefficient
of $6.314\times10^{-5}$ m/$\sqrt{\text{s}}$ gives 3547 m at $t = 100$ Ma, and
the check is that $6.314\times10^{-5}\sqrt{3.156\times10^{15}} = 3547$.

## 6. Assumptions and regime of validity

| Assumption | Where it holds | What breaks without it |
|---|---|---|
| Reversals are globally synchronous | Everywhere, to within the recording lag of the magnetisation | Extremely rapid reversals would break the correlation of a stripe with a time |
| Spreading rate is constant over the interval being matched | Young crust, and short intervals | A rate change within the pattern widens or narrows individual stripes and the match degrades |
| The magnetisation is acquired at the ridge | Fast-spreading ridges with a robust magnetised layer | Slow-spreading ridges have a weak and patchy magnetic signal, which is why the method works best on fast-spreading crust |
| Half-space cooling | Young ocean floor, above about 70 Ma | Old ocean floor, where the plate model and hydrothermal circulation dominate |
| The plate is a rigid body between boundaries | Everywhere except boundary zones | Interseismic strain accumulates within tens of kilometres of a boundary, and the "plate" is only rigid in the long-term average |
| Creation and destruction balance | Over millions of years | Short-term changes in ridge length are real but small |

The rigidity assumption is the one that is most often misread. A plate is rigid
on geological timescales, which is a statement about a *time average*;
instantaneously, the boundary zones deform continuously and the interior deforms
at the few nanometres per second level that GNSS can measure. Both statements
are true, and which is useful depends on the timescale of the question.

## 7. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| Spreading rate | mm/a or km/Ma | Numerically equal |
| Subsidence coefficient | m/$\sqrt{\text{s}}$ | $[2\rho_m\alpha\Delta T/(\rho_m-\rho_w)]\sqrt{\kappa/\pi}$ |
| Heat flow | mW/m² | $[k\Delta T/\sqrt{\pi\kappa t}]$ |
| Thermal conductivity $k$ | W m⁻¹ K⁻¹ | 3 to 3.5 for lithospheric rock |
| Thermal diffusivity $\kappa$ | m²/s | About $10^{-6}$ |
| Thermal expansion $\alpha$ | K⁻¹ | About $3\times10^{-5}$ |
| Age | Ma, Ga | Distinguished from a duration in years only by context |

Two checks that catch most errors.

**The age-unit check.** $\lambda$ in a decay law and $t$ in an age must share a
unit, and in this subject the same is true of a spreading rate and a duration.
A rate in km/Ma multiplied by a time in years is wrong by $10^6$, and the
result usually looks like a plausible distance rather than an obvious mistake.
Write the unit into the arithmetic.

**The subsidence check.** The coefficient is
$(2\times3300\times3\times10^{-5}\times1300/2300)\sqrt{10^{-6}/\pi}
= 0.1119 \times 5.642\times10^{-4} = 6.31\times10^{-5}$ m/$\sqrt{\text{s}}$.
Both factors are dimensionless or in SI, and the product is a length per square
root of time, which is what a diffusion-like law requires. A result with the
wrong dimensions in a $\sqrt{t}$ law is a sign that a density or a diffusivity
has been inverted.

## 8. Python demonstration

[`code/tectonic_theory_demo.py`](./code/tectonic_theory_demo.py) builds the
synthetic magnetic pattern, inverts it for the spreading rate, tests the
symmetry, computes the half-space subsidence and heat-flow coefficients from
thermal constants, and estimates the maximum age of the ocean floor from plate
geometry.

Sections §2, §3 and §4 above quote its output directly. Three points about what
it demonstrates rather than merely prints:

- **The inversion is a real inverse problem.** A grid search over rates is a
  crude but honest version of what a marine magnetic interpretation does, and
  seeing the misfit vanish at the true rate is the check that the forward model
  and the inversion are the same object.
- **The thermal coefficients are computed, not fitted.** Every input is a
  measured thermal constant, and the agreement with the empirical coefficients
  is therefore evidence. A fitted coefficient would be a description.
- **The failure is printed.** The demo's output states where the half-space
  model breaks down and what each candidate fix requires, because a model
  presented without its failure mode is not a scientific model.

The reversal sequence used is synthetic and evenly spaced only in the sense that
it is a fixed list; a real reversal sequence is irregular, and the irregularity
is what makes a stripe pattern a fingerprint rather than just a sequence of
stripes. The exercise set asks for the inversion to be repeated with a genuine
irregular pattern and for the effect of a rate change within the pattern to be
quantified.

## 9. Common mistakes

1. **Presenting the continental fit as conclusive.** It is not; it was
   insufficient for fifty years, and saying so is more informative than
   pretending otherwise.
2. **Treating the reversal timescale as derived from the stripes.** It is
   independent, from magnetostratigraphy dated by radiometric methods, and that
   independence is what makes the match a test.
3. **Forgetting the symmetry.** A stripe pattern alone could arise in other
   ways; a *symmetrical* pattern about the ridge, with matching widths, is what
   the tape-recorder model requires.
4. **Fitting the thermal coefficients.** A fitted coefficient reproduces the
   data and tests nothing; a computed coefficient either agrees or does not.
5. **Quoting the half-space model as valid everywhere.** It fails on old ocean
   floor, and the failure led to two accepted additions to the theory.
6. **Mixing mm/a and km/Ma as if they differed.** They are numerically equal,
   which is convenient and also a trap: a rate stated in one unit and used in
   the other is fine, but a rate in mm/a multiplied by a time in years is not.
7. **Assuming the ocean floor ages continuously to the age of the Earth.** It
   does not, and the finiteness of the maximum age is the argument.
8. **Ignoring the area balance.** Creation and destruction have to balance on a
   constant-area sphere, and a plate model that does not balance is wrong
   regardless of how well it fits locally.

## 10. Real-world applications

- **Marine magnetic surveying.** The method of §2 remains the standard way to
  date ocean crust and to measure spreading rates, and it is how a marine survey
  grid is planned ([15-03-01 Mid-Ocean Ridges](../../15-oceanography-marine/03-seafloor-tectonics/01-mid-ocean-ridges.md)).
- **Ocean basin reconstruction.** Plate reconstructions are built from magnetic
  isochrons and fracture-zone geometry, and they are the framework for
  palaeoclimate and palaeoceanographic modelling.
- **Heat-flow and geothermal resource assessment.** The cooling-plate model
  predicts the heat flow that a geothermal prospect can expect at a given
  crustal age ([04-06-03 Geothermal Systems](../06-petroleum-and-mineral-systems/03-geothermal-systems.md)).
- **Sea-level and subsidence studies.** The depth–age relation is the baseline
  for the thermal subsidence of rifted margins, and therefore for the
  accommodation space that a sedimentary basin fills.
- **Teaching the method of multiple working hypotheses.** The trail is the
  classic case study in how a scientific community replaces one explanation with
  another, and it is used in that role well outside the geosciences.

## 11. Further reading

- **Wegener, A. *The Origin of Continents and Oceans* (Dover reprint).** The
  original drift argument, including the parts that were right and the mechanism
  that was missing. Level: beginner.
- **Vine, F. J., & Matthews, D. H. (1963). Magnetic anomalies over oceanic
  ridges. *Nature* 199, 947–949.** The paper that made the theory. Two pages.
  Level: advanced.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (Cambridge University
  Press).** The cooling-plate model of §3, derived in full, and the plate model
  that fixes it. Level: advanced.
- **Cox, A. (ed.) *Plate Tectonics and Geomagnetic Reversals* (Freeman).** A
  collection of the primary papers, which is the best way to see the evidence
  trail in its original form. Level: intermediate.
- **Parsons, B., & Sclater, J. G. (1977). An analysis of the variation of ocean
  floor bathymetry and heat flow with age. *Journal of Geophysical Research*
  82, 803–827.** Where the empirical coefficients of §3 come from.
  Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04-02-02 Divergent, Convergent and Transform Boundaries](./02-plate-boundaries.md)
  — what happens at the ridge and the trench in detail.
- [04-02-04 Plate Motion Frames, Euler Poles and Global Models](./04-plate-motion-frames.md)
  — how a spreading rate becomes a global plate motion.
- [04-01-01 Crust, Mantle, Core: Seismological and Geochemical Evidence](../01-earth-structure/01-layered-earth.md)
  — the property contrasts that make a ridge and a trench visible.
- [04-03-03 Radiometric Dating Methods and Their Assumptions](../03-geologic-time-and-stratigraphy/03-radiometric-dating.md)
  — where the dates that calibrate the magnetic timescale come from.
- [08-01-06 Palaeomagnetism, Reversals and Magnetostratigraphy](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/06-palaeomagnetism.md)
  — the physics of the recording.

Exercises:
[`exercises/01-tectonic-theory-exercises.md`](./exercises/01-tectonic-theory-exercises.md)
and
[`exercises/01-tectonic-theory-solutions.md`](./exercises/01-tectonic-theory-solutions.md).

## Self-assessment checklist

- [ ] I can state the four stages of the evidence trail and what each rules
      out. (§1)
- [ ] I can explain the tape-recorder hypothesis and why symmetry is a test.
      (§2)
- [ ] I can compute a spreading rate from a stripe width and a duration. (§2)
- [ ] I can derive the $\sqrt{t}$ subsidence law and the $1/\sqrt{t}$ heat-flow
      law. (§3)
- [ ] I can compute the subsidence coefficient from thermal constants and
      compare it with the empirical value. (§3, §7)
- [ ] I can state where the half-space model fails and what the failure
      required. (§3)
- [ ] I can estimate the maximum ocean-floor age from geometry. (§4)
- [ ] I can write the creation–destruction area balance for a constant-area
      sphere. (§4)
- [ ] I can use 1 mm/a = 1 km/Ma without converting. (§5)
- [ ] I can state the regime of validity of the cooling-plate model and the
      rigidity assumption. (§6)
