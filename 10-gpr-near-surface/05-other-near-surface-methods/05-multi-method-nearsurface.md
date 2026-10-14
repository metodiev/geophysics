---
id: 10-05-05
title: "Integrating Near-Surface Methods"
level: graduate
prereqs: ["05-04-07", "05-07-03", "10-05-01", "10-05-03"]
tags: [near-surface, integration, joint-inversion, rock-physics, water-content]
---

# Integrating Near-Surface Methods

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why different near-surface methods measure different physical
   properties, and **translate** each property into a common parameter
   (water content, porosity, clay content) through an explicit rock-physics
   relation.
2. **Show**, with a worked calculation, that one geophysical reading determines a
   *product* of unknowns rather than any one of them.
3. **Quantify** how much a second, independent measurement narrows the admissible
   set, and **state** the remaining correlation between the parameters.
4. **Propagate** measurement uncertainties through the two relations by Monte
   Carlo, and **report** the result as a correlated set rather than two
   independent error bars.
5. **Demonstrate** the degeneracy that survives a joint inversion: the same pair
   of readings is fitted by fresh water in a porous medium and by saline water in
   a tight one.
6. **State** precisely what was measured, what was inferred and what was assumed
   in an integrated interpretation, and **name** the observation that would settle
   each assumption.

## Prerequisites

- [05-04-07 Electrical Properties of Rocks](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md) —
  conductivity, saturation and Archie's law.
- [05-07-03 Multi-Method Integration](../../05-core-geophysics/07-interpretation-and-integration/03-multi-method-integration.md) —
  the general reasoning this lesson applies quantitatively.
- [10-05-01 EM Induction and Conductivity Meters](01-electromagnetic-induction-nearsurface.md) —
  where the conductivity reading comes from, and why it is an average.
- [10-05-03 Thermal Methods for Shallow Subsurface Investigation](03-thermal-nearsurface.md) —
  the thermal mixing model and its sensitivity to water content.

> All models and data in this module are **SYNTHETIC**. The petrophysical
> relations, exponents, material properties, water contents and uncertainties
> below are chosen teaching values, not calibrations and not site parameters.

## 1. Intuition: two shadows of one object

Each near-surface method senses a different contrast, and no single contrast
identifies a material. Conductivity responds to pore water and clay; thermal
conductivity responds to the solid framework, the porosity and the water fraction;
seismic velocity responds to the elastic frame and the fluid bulk modulus; density
responds to the mineral grains and their packing. In a wet soil all four change
together — which is exactly why combining them can work, and exactly why the
combination is not self-contained.

The organising picture is two shadows of one object. One shadow (conductivity)
depends on two things at once; the other (thermal conductivity) depends on one of
them. Together they locate the object better than either alone — but only if the
*geometry of the shadows* is different, and only up to the point where the
materials themselves are unknown. This lesson makes both statements quantitative
with one worked example, and refuses to hide the residual degeneracy behind a
single "best-fit" pair of numbers.

## 2. Precise definitions

**Property, parameter and material.** A *property* is what a method measures
(conductivity $\sigma$, thermal conductivity $k$, seismic velocity $v_s$,
dielectric permittivity). A *parameter* is a state variable you want
(volumetric water content $\theta$, saturation $S_w$, porosity $\phi$, clay
fraction, salinity). A *material* is the assemblage that turns one into the
other. Rock physics is the map from parameters and materials to properties.

**Petrophysical relation.** Any such map, with stated validity conditions and
stated constants. Two are used here, both as teaching forms:

$$\sigma = \sigma_w\,\theta^{m} \qquad \text{(Archie-type, unsaturated)},$$
$$k = k_s^{\,1-\phi}\,k_w^{\,\theta}\,k_a^{\,\phi-\theta}
\qquad \text{(geometric-mean mixing)}.$$

The first is written so that the reading is *linear in the pore-water
conductivity* $\sigma_w$ — the property that makes the electrical measurement
insensitive to the water content alone. The second has **no** free fluid-conductivity
parameter: thermal conductivity of water is a material constant, so the thermal
reading isolates the geometry.

**Admissible set.** The set of parameter values whose predicted readings lie within
the measurement uncertainties. Reported as an interval, a curve or a region — never
as a point, unless an independent constraint closes it.

**Degeneracy.** A direction in parameter space along which the data do not
constrain. A joint inversion removes degeneracies only where the two methods'
sensitivities are linearly independent.

## 3. Derivations and the worked example

### 3.1 Why one reading cannot give one parameter

Differentiate the Archie-type relation logarithmically:

$$\frac{\mathrm d\sigma}{\sigma} = \frac{\mathrm d\sigma_w}{\sigma_w}
+ m\,\frac{\mathrm d\theta}{\theta} .$$

A percentage error in $\theta$ and a percentage error in $\sigma_w$ enter the
reading in the *same* way, scaled by $m$. Therefore, from a single reading of
$\sigma$,

$$\theta = \left(\frac{\sigma}{\sigma_w}\right)^{1/m},$$

so the water content is determined only once $\sigma_w$ is known. The sensitivity
of the *inference* is the reciprocal of that of the forward problem:

$$\frac{\partial\ln\theta}{\partial\ln\sigma_w}\bigg|_{\sigma}
= -\frac{1}{m},$$

so the fractional uncertainty of the inferred water content is $1/m$ times that of
the assumed pore-water conductivity. With $m = 1.5$ and an order-of-magnitude
uncertainty in $\sigma_w$, the water content is uncertain by a factor of
$10^{2/3} = 4.6$ — before any measurement error is considered.

### 3.2 What the thermal reading contributes

For the mixing model, the logarithmic sensitivity to water content is *constant*:

$$\frac{\mathrm dk}{\mathrm d\theta}\bigg|_{k} = k\ln\frac{k_w}{k_a},$$

independent of $\theta$. With $k_w = 0.60$ and $k_a = 0.025\ \mathrm{W\,m^{-1}\,K^{-1}}$,
$\ln(k_w/k_a) = 3.178$, so

$$\frac{\partial\ln k}{\partial\theta} = 3.178\ \text{per unit }\theta,$$

i.e. the *relative* sensitivity is a fixed number per unit water content, in
contrast with the Archie relation where the sensitivity scales as $m/\theta$. The
forward sensitivity d$k$/d$\theta$ is largest where $k$ is largest (in wet ground),
which is the opposite of the electrical case. **That difference in the shape of
the two sensitivities is what makes the pair informative.**

### 3.3 The joint inversion of the teaching case

Truth: $\phi = 0.45$, $m = 1.5$, $\sigma_w = 0.250\ \mathrm{S\,m^{-1}}$,
$\theta = 0.20$, $k_s = 3.0$, $k_w = 0.60$,
$k_a = 0.025\ \mathrm{W\,m^{-1}\,K^{-1}}$. The forward model gives

$$\sigma = 0.250(0.20)^{1.5} = 0.250(0.089443) = 0.022361\ \mathrm{S\,m^{-1}}
= 22.36\ \mathrm{mS\,m^{-1}},$$
$$k = 3.0^{0.55}(0.60)^{0.20}(0.025)^{0.25} = 0.6569\ \mathrm{W\,m^{-1}\,K^{-1}}.$$

A realisation with 5% and 3% relative errors gives
$\sigma = 21.83\ \mathrm{mS\,m^{-1}}$ and
$k = 0.6661\ \mathrm{W\,m^{-1}\,K^{-1}}$ — the numbers the demonstration uses.

**From $\sigma$ alone**, over a teaching prior $\sigma_w \in [0.05, 1.00]\
\mathrm{S\,m^{-1}}$, the admissible water content runs from $0.078$ (at
$\sigma_w = 1.0$) to the porosity ceiling $0.45$ (at $\sigma_w = 0.05$): a range of
width $0.372$ and a factor of $5.8$. The reading constrains the product
$\sigma_w\theta^{m}$, nothing more.

**Adding $k$** determines $\theta$ on its own. Inverting the mixing model for the
observed $k$ with a 3% error gives

$$\theta = 0.2043 \pm 0.0094,$$

a one-sigma interval $0.1947$–$0.2136$ of width $0.0189$ — **19.7 times narrower**
than the electrical-only admissible set. The pore-water conductivity then follows
from $\sigma_w = \sigma/\theta^{m}$:

$$\sigma_w = \frac{0.02183}{(0.2043)^{1.5}} = 0.2364\ \mathrm{S\,m^{-1}},$$

against an unknown truth of $0.250$ — within its uncertainty, but with the error
**amplified**: the fractional error of $\sigma_w$ is
$\sqrt{(0.05)^2 + (1.5 \times 0.046)^2} = 0.086$, i.e. $8.6\%$, not $5\%$. The
$1/m$ factor of Section 3.1 acts in reverse: a water content known to $4.6\%$
costs $6.8\%$ in $\sigma_w$.

### 3.4 Why the answer is still a set

The demonstration's Monte Carlo (20000 trials, first 2000 used for the statistics)
gives

$$\theta = 0.2042 \pm 0.0093\ (4.6\%), \qquad
\sigma_w = 0.2373 \pm 0.0203\ (8.6\%),$$

with a **correlation coefficient of $-0.808$.** The two parameters are strongly
anti-correlated: a lower water content must be compensated by a more conductive
pore water to explain the same conductivity. Any error bar quoted for one of them
*without* the correlation is therefore misleading, because the joint confidence
region is an elongated ellipse, not a rectangle. This is the same geometry as the
$H$–$k$ trade-off in receiver functions
([06-08-01](../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md))
and the thickness–velocity ridge in surface waves
([10-05-02](02-seismic-surface-wave-nearsurface.md)) — an elongated valley in the
misfit surface, produced by different physics.

### 3.5 The degeneracy that survives — measured

Keep the same two readings and change the *assumed material*:

| $\phi$ | $k_s$ (W/m/K) | $\theta$ | $\sigma_w$ (S/m) | predicted $\sigma$ | predicted $k$ |
|---|---|---|---|---|---|
| 0.45 | 3.00 | 0.200 | 0.2500 | 22.36 mS/m | 0.6569 |
| 0.35 | 3.00 | 0.049 | 1.9886 | 21.83 mS/m | 0.6570 |

Both rows reproduce the measurements within their stated uncertainties. The water
content differs by a **factor of 4.0** and the pore-water conductivity by a
**factor of 8.0**. The reason is identifiable: lowering the porosity raises the
predicted thermal conductivity at fixed $\theta$, so a *drier* soil with less
pore space gives the same thermal reading; keeping the electrical reading then
requires much more saline pore water. **These are two physically different
grounds, and the geophysics alone does not separate them.**

The lesson generalises: a joint inversion removes exactly the degeneracies along
which the two methods' sensitivities are independent. Where both sensitivities
depend on the same material with the *same* functional form, the degeneracy
survives. Section 6 names the observations that break it.

## 4. Physical interpretation

**The two sensitivities have different shapes.** Electrical sensitivity to water
content is $m/\theta$ per unit, so it is *large* when the soil is dry; thermal
sensitivity is $k\ln(k_w/k_a)$, so it is *large* when the soil is wet. The pair
therefore covers the parameter range better than either alone — one is a dry-end
sensor, the other a wet-end sensor. This is a general principle for choosing
method pairs: pick methods whose sensitivity *profiles* differ, not merely whose
physics differ.

**Linear dependence is what matters.** Conductivity and thermal conductivity are
both sensitive to water content and to porosity. The joint inversion resolves them
only because the sensitivities to $\theta$ and $\phi$ enter with different
weights. When a third measurement is added, the test is whether its sensitivity
vector is independent of the existing two — a rank question, exactly as in
[18 Inverse Problems](../../18-inverse-problems/README.md).

**Error amplification has a direction.** The factor $1/m$ appears whenever a
parameter is recovered by dividing by a measured quantity raised to a power.
Choosing a method pair with *both* sensitivities of order unity, and *opposite
sign*, gives the narrowest joint interval: opposite signs mean the errors partially
cancel in the joint fit.

**Reporting.** An integrated interpretation should state, for each number: the
property measured, the relation used, the constants assumed, the resulting
parameter with its admissible set, and the correlation with any other parameter.
A single number per station with no assumed constants is not an interpretation; it
is a restatement of the reading.

## 5. Assumptions and regime of validity

1. **The relations apply.** $\sigma = \sigma_w\theta^{m}$ is a teaching form. Real
   soils have surface conduction (clay) that adds a term independent of $\sigma_w$,
   and $m$ varies with texture and saturation. Applying it outside its range
   produces a plausible parameter with a large systematic error.
2. **The constants are known.** $\phi$, $k_s$, $m$ and the mixing model are
   *assumed*, and Section 3.5 measures what a wrong $\phi$ costs.
3. **One-dimensional, uniform ground at the measurement scale.** A layered soil
   makes both readings weighted averages (see
   [10-05-01](01-electromagnetic-induction-nearsurface.md) and
   [10-05-03](03-thermal-nearsurface.md)), so the "same" $(\sigma, k)$ pair may
   come from different layered profiles for each method.
4. **Coincident footprints.** The two methods must sample the same volume; a
   coil-spacing footprint of several metres against a thermal probe of centimetres
   compares different ground.
5. **Independent errors.** The Monte Carlo assumes the two measurement errors are
   independent. A shared nuisance parameter — a wrong porosity, a wrong
   temperature correction, a wrong depth datum — correlates them and makes the
   joint result worse than advertised.
6. **No time-lapse assumption.** This lesson inverts a single epoch. Repeat
   measurements add the temporal constraint that
   [06-01 Time-Lapse Near-Surface Geophysics](../06-nearsurface-monitoring/01-time-lapse-nearsurface.md)
   develops, and are usually a much stronger constraint than a second method.
7. **Petrophysical non-uniqueness is not an inversion failure.** The degeneracy of
   Section 3.5 is a property of the physics, not of the algorithm. No regularisation,
   no machine-learning prior and no finer mesh removes it.

## 6. What settles the residual degeneracy

| Unknown | Observation that settles it |
|---|---|
| porosity $\phi$ | a borehole sample, or a density log ([05-08 Borehole and Well-Log Geophysics](../../05-core-geophysics/08-geophysical-logging/README.md)) |
| pore-water conductivity $\sigma_w$ | a water sample from a piezometer; or the conductivity of a saturated extract |
| Archie exponent $m$ | a laboratory set of cores at known saturation; or a site calibration curve |
| mineral conductivity $k_s$ | a probe measurement on a dried sample of the matrix |
| one-dimensionality | a multi-offset or multi-spacing survey on the same line |
| spatial coincidence | a common survey layout with overlapping footprints |

Notice the pattern: **the physics gives the parameter set; the ground truth picks
the member.** Every item in this table is a measurement, not a modelling choice.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| bulk conductivity | $\sigma$ | $\mathrm{S\,m^{-1}}$ | |
| pore-water conductivity | $\sigma_w$ | $\mathrm{S\,m^{-1}}$ | same as $\sigma$ |
| volumetric water content | $\theta$ | $\mathrm{m^{3}\,m^{-3}}$ | dimensionless; capped by $\phi$ |
| porosity | $\phi$ | $\mathrm{m^{3}\,m^{-3}}$ | $\theta \le \phi$ |
| Archie exponent | $m$ | dimensionless | |
| thermal conductivity | $k, k_s, k_w, k_a$ | $\mathrm{W\,m^{-1}\,K^{-1}}$ | all in the same unit |
| sensitivity | d$k$/d$\theta$ | $\mathrm{W\,m^{-1}\,K^{-1}}$ | $k\ln(k_w/k_a)$ |

Two checks that catch most errors: every exponent in a power law must be
dimensionless (so $\theta$ and $\phi$ must be volume fractions, not percentages),
and a sensitivity d$k$/d$\theta$ must carry the units of $k$ because $\theta$ is
dimensionless. Expressing water content in per cent while carrying a calibrated
slope in per unit is the classic factor-of-100 error.

## 8. Python demonstration

`code/multi_method_demo.py` implements the whole chain and prints labelled results
with units. It:

1. builds the two teaching relations, prints the truth's readings
   ($22.36\ \mathrm{mS\,m^{-1}}$, $0.6569\ \mathrm{W\,m^{-1}\,K^{-1}}$), and draws a
   synthetic observation with 5% and 3% errors;
2. inverts the electrical reading alone and reports the admissible range
   $0.078$–$0.45$ (a factor of $5.8$);
3. adds the thermal reading, reports $\theta = 0.2043 \pm 0.0094$ and the narrowing
   factor $19.7$, and derives $\sigma_w = 0.2364 \pm 0.0202\ \mathrm{S\,m^{-1}}$;
4. propagates the uncertainties by Monte Carlo, reporting the correlation
   $-0.808$ between the two parameters;
5. reproduces the two readings with two different materials, and prints the factor
   of $4.0$ in water content and $8.0$ in pore-water salinity between them.

The demonstration is print-only, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network, and runs in under a second.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/05-multi-method-nearsurface-exercises.md`](./exercises/05-multi-method-nearsurface-exercises.md)
and
[`exercises/05-multi-method-nearsurface-solutions.md`](./exercises/05-multi-method-nearsurface-solutions.md).

- **★** Differentiate $\sigma = \sigma_w\theta^{m}$ and state which fractional
  uncertainty dominates the inferred water content for $m = 2$.
- **★** Compute $k$ for $\phi = 0.40$, $\theta = 0.15$ with the teaching
  constants.
- **★★** For the measured pair of Section 3.3, compute the admissible water
  content if $\sigma_w$ is known to be $0.100 \pm 0.010\ \mathrm{S\,m^{-1}}$, and
  compare with the thermal-only interval.
- **★★** Quantify the effect of assuming $\phi = 0.40$ instead of the true
  $0.45$: recompute the inferred $\theta$ from the same thermal reading.
- **★★★** Design a survey that determines water content to 5% relative in a
  clay-rich soil, naming the calibration measurements and the falsification test.

## Mastery checkpoint
Complete this without notes:

> A station gives $\sigma = 30.0\ \mathrm{mS\,m^{-1}}$ (5% error) and
> $k = 1.00\ \mathrm{W\,m^{-1}\,K^{-1}}$ (3% error) over ground whose porosity is
> believed to be $0.40$ with an Archie exponent $m = 1.8$.
> **(a)** Invert the thermal reading for $\theta$ and state the one-sigma
> interval. **(b)** Derive $\sigma_w$ and its uncertainty. **(c)** State why the
> answer is a correlated set rather than two independent numbers.
> **(d)** A sample shows the porosity is actually $0.45$. Recompute $\theta$ and
> state the sign and rough size of the change. **(e)** List the three numbers you
> assumed and the observation that would remove each.

A worked version of (a)–(c) appears in the exercise solutions.

## Common pitfalls
1. **Reporting a parameter from one method.** Section 3.1 shows that one reading
   determines a product; the "measured" water content is an assumption in
   disguise.
2. **Independent error bars for correlated parameters.** The correlation here is
   $-0.808$; quoting $\pm 0.009$ and $\pm 0.020$ separately overstates the certainty
   of the pair.
3. **Reusing published petrophysical constants.** $m$, $k_s$ and the mixing model
   are site properties. A calibration from another soil is an assumption, not a
   measurement.
4. **Comparing methods with different footprints.** A metre-scale coil pair and a
   centimetre-scale probe do not sample the same ground.
5. **Believing more methods always help.** Only independent sensitivity directions
   help; three methods that respond to the same contrast give three copies of the
   same shadow.
6. **Confusing property with material.** The same readings are two different
   grounds (Section 3.5).
7. **Forgetting the time dimension.** Repeat measurement of one property is often
   a stronger constraint than adding a second method at one epoch.

## Related modules
- [10-05-01 EM Induction and Conductivity Meters](01-electromagnetic-induction-nearsurface.md) —
  the electrical reading and its depth weighting.
- [10-05-02 Surface-Wave Methods for Shallow Layers](02-seismic-surface-wave-nearsurface.md) —
  the elastic reading and its own thickness–velocity degeneracy.
- [10-05-03 Thermal Methods for Shallow Subsurface Investigation](03-thermal-nearsurface.md) —
  the thermal mixing model used here.
- [10-05-04 Nuclear and Radiometric Near-Surface Methods](04-nuclear-and-radiometric-nearsurface.md) —
  the fourth contrast, and the calibration that is a material property.
- [10-06 Near-Surface Monitoring and Time-Lapse](../06-nearsurface-monitoring/README.md) —
  the temporal constraint that usually beats a second static method.
- [05-07 Interpretation and Geological Integration](../../05-core-geophysics/07-interpretation-and-integration/README.md) —
  the qualitative version of this reasoning.
- [14-03 Petrophysical Relations for Saturated Media](../../14-hydrology-hydrogeophysics/03-petrophysics-hydrology/README.md) —
  the hydrology-side treatment of the same relations.
