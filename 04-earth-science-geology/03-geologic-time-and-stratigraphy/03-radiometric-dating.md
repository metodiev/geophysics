---
id: 04-03-03
title: "Radiometric Dating Methods and Their Assumptions"
level: advanced
prereqs: ["04-03-02", "02-09-02"]
estimated_minutes: 105
tags: [geochronology, isochron, concordia, closure-temperature, geochronology-assumptions]
---

# Radiometric Dating Methods and Their Assumptions

Begin with a distinction that this whole lesson rests on.

A **measurement** is a comparison of a quantity with a standard. A **date** is a
ratio of concentrations of isotopes, converted into years by a model. In a
mass-spectrometer run, the measured quantities are isotope ratios — a number like
$^{206}\mathrm{Pb}^{*}/^{238}\mathrm{U} = 0.167\,80$ with an uncertainty and a
stated instrument standard. The number "1000 Ma" is not measured by the
instrument. It is produced by inverting a decay law, and the inversion requires
three things beyond the ratio: a **decay constant**, an **assumption about the
system's closure**, and an **assumption about the initial isotopic composition**.
Change any of the three and the age changes.

Therefore: **a published age is a model-dependent interpretation of a
measurement, and it is only as good as the assumptions it states.** An age quoted
without its decay-constant compilation, its closure model and its initial-ratio
treatment is not a weaker result than one that states them; it is a different and
weaker kind of object, because it cannot be checked.

The decay law, the half-life, the Bateman equations and the isochron equation are
derived in
[02-09-02 Radioactive Decay, Half-Life and Dating](../../02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md).
This lesson does not re-derive them. It does the geology: which system dates what,
how a **concordia** turns one set of ratios into an internal consistency test,
how three specific assumptions fail in ways that are recognisable in the data, and
how a dating result is tied to a position in a stratigraphic sequence.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** a date from a measurement, and state exactly which quantity
   the instrument measured and which model produced the years.
2. **Explain** the isochron as a two-parameter fit and state why it converts an
   assumption into a measurement — and why a single-sample model age does not.
3. **Construct** the U–Pb concordia curve and explain what "concordant" and
   "discordant" mean in terms of the two independent decay chains.
4. **Derive** the discordia chord for a single-stage Pb-loss episode and use its
   two intercepts to recover a crystallisation age and a disturbance age from one
   set of analyses.
5. **Quantify** the age error produced by each of three assumptions: uncorrected
   common Pb, an open system, and a non-zero initial daughter ratio.
6. **Recognise** a mixing line and explain why an isochron-fit statistic cannot
   distinguish it from an isochron.
7. **State**, for each of the principal chronometers, what it dates, its
   half-life range, its closure behaviour and its dominant failure mode.
8. **Attach** a numerical age to a stratigraphic bracket, and state what is
   assumed in the attachment.

## Prerequisites

- [02-09-02 Radioactive Decay, Half-Life and Dating](../../02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md)
  — the decay law, half-life, the isochron equation and closure temperature. This
  lesson assumes all of it.
- [02 Stratigraphic Principles and Relative Dating](./02-stratigraphic-principles.md)
  — the bracket that an age is fitted into.
- [01-08-01 First-Order ODEs](../../01-mathematics/08-ordinary-differential-equations/01-first-order-odes.md)
  — the mathematics of $\dot N = -\lambda N$, assumed known.

## 1. What was measured, and what was inferred

Take a U–Pb analysis of a zircon. The instrument reports, for a population of
spots, ratios such as $^{206}\mathrm{Pb}/^{238}\mathrm{U}$ and
$^{207}\mathrm{Pb}/^{235}\mathrm{U}$, both corrected for instrumental mass
fractionation against a reference material. Three transformations then occur.

**Correction for common Pb.** Some of the measured $^{206}\mathrm{Pb}$ and
$^{207}\mathrm{Pb}$ did not come from decay in the mineral; it was present at
crystallisation or introduced later. Correcting it requires measuring a
non-radiogenic isotope — usually $^{204}\mathrm{Pb}$ — and assuming a common-Pb
composition, or using a regression that determines it. The corrected quantity is
denoted with a star: $^{206}\mathrm{Pb}^{*}$. Whether the correction is right is
**an assumption with a magnitude**, and §4 quantifies it.

**Choosing a decay constant.** The decay constants are tabulated. In part 02-09
the values used were $\lambda_{238} = 1.551\,25 \times 10^{-10}$ a$^{-1}$ and
$\lambda_{235} = 9.8485 \times 10^{-10}$ a$^{-1}$, labelled as values in
long-standing common use, and the demonstration was explicit that compilations
differ and that ages are tied to a stated set of constants. That is the discipline
here as well: **quote the compilation with the age**. The relevant point is that
the two chains have different constants, and that the *ratio* of the two
daughter/parent ratios therefore depends only on age. That ratio is the basis of
§3.

**Assuming closure.** The decay law counts time from the moment the system
closed: when the mineral stopped exchanging parent and daughter with its
surroundings. Everything before that moment is invisible and everything after it
is lost. Closure is a temperature-dependent process and is treated at length in
[02-09-02 §5](../../02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md);
the point to carry here is that **an age is a time since closure, and the closure
temperature is part of the answer**.

## 2. Isochron and model age, in one paragraph each

An **isochron** is a straight-line fit to several cogenetic samples:

$$\frac{^{87}\mathrm{Sr}}{^{86}\mathrm{Sr}} = R_0 +
\left(e^{\lambda t} - 1\right)\frac{^{87}\mathrm{Rb}}{^{86}\mathrm{Sr}},
\tag{1}$$

so the slope gives the age and the intercept gives the initial ratio. Both are
fitted, and both carry an uncertainty. The age is then a joint property of a
dataset, and the initial ratio is a result rather than a premise.

A **model age** uses one sample and one assumed initial ratio:

$$\frac{^{87}\mathrm{Sr}}{^{86}\mathrm{Sr}} - R_0^{\text{assumed}} = x
\left(e^{\lambda t} - 1\right). \tag{2}$$

The demonstration in 02-09-02 showed what this costs: for one synthetic sample,
two defensible assumptions about the initial ratio gave ages of 451 Ma and
188 Ma against an isochron age of 349 Ma for a rock whose true age was 350 Ma.
The failure mode is worse than it looks, because the *error* in a model age is
proportional to $1/x$: a sample with a small parent/daughter ratio is nearly
insensitive to the age and extremely sensitive to the assumed intercept.

The demo for this lesson measures exactly that sensitivity. A synthetic suite with
a true age of 300 Ma and a true initial ratio of 0.7060 is analysed with an
assumed initial ratio of 0.7040:

```text
    Rb/Sr    Sr87/86   model age (Ma)   error (Ma)
     0.05     0.7062          3,050.5     +2,750.5
     0.10     0.7064          1,688.7     +1,388.7
     0.25     0.7071            858.8       +558.8
     0.50     0.7081            579.9       +279.9
     1.00     0.7103            440.1       +140.1
     2.00     0.7145            370.1        +70.1
     4.00     0.7231            335.1        +35.1
```

The low-ratio analysis returns an age ten times too old. Two per cent of error in
the assumed intercept is enough. That is why an age built from one low-ratio
analysis is not an age regardless of the precision of the mass spectrometry, and
it is why isochron fitting exists.

## 3. Concordia: two decay chains as an internal test

U–Pb has a property no other system has. There are two independent decay chains
from the same parent element to two isotopes of the same daughter element, and
both chains are measured in the same aliquot:

$$\frac{^{206}\mathrm{Pb}^{*}}{^{238}\mathrm{U}} = e^{\lambda_{238} t} - 1,
\qquad
\frac{^{207}\mathrm{Pb}^{*}}{^{235}\mathrm{U}} = e^{\lambda_{235} t} - 1.
\tag{3}$$

For any $t$, equation (3) gives a single point in the
$\left(^{206}\mathrm{Pb}^{*}/^{238}\mathrm{U},\,
^{207}\mathrm{Pb}^{*}/^{235}\mathrm{U}\right)$ plane. The curve traced out as $t$
runs from zero to the age of the Earth is the **concordia** curve. A sample whose
two ratios define a point on that curve is **concordant**: both chains agree, and
there is a single $t$ that satisfies both. A sample whose point is off the curve
is **discordant**: the two chains disagree, and no single age explains the
measurement.

The demo verifies the curve against the age equation, which is a check on the
algebra rather than on the geology:

```text
  synthetic crystallisation age      1,000.00 Ma
  206Pb*/238U                        0.16780393
  207Pb*/235U                        1.67741024
  age recovered from 206Pb*/238U     1,000.000000 Ma (residual 0.000e+00 a)
  age recovered from 207Pb*/235U     1,000.000000 Ma (residual 0.000e+00 a)
```

The corresponding table shows why the two chains together are informative and one
alone is not:

```text
    t (Ma)       206/238       207/235     207/206
        50        0.0078        0.0505      6.4825
       500        0.0806        0.6363      7.8894
     1,000        0.1678        1.6774      9.9963
     2,700        0.5202       13.2834     25.5354
     4,400        0.9789       75.1984     76.8179
```

The $^{207}\mathrm{Pb}/^{206}\mathrm{Pb}$ ratio is almost constant for young rocks
(table row 50 Ma: 6.48; 500 Ma: 7.89) and rises steeply for old ones. That is
because $^{235}\mathrm{U}$ decays roughly six times faster than $^{238}\mathrm{U}$,
so for young samples the $^{207}\mathrm{Pb}$ inventory barely grows. A single
chain gives an age that cannot be checked. Two chains give a ratio whose
dependence on age is different from either, and the agreement between the three
is the test.

## 4. Discordia: deriving the chord, and what its intercepts mean

The demonstration of §3 is an algebraic identity. The geology starts when a
sample is discordant, and the most common cause is **episodic loss of radiogenic
Pb**.

Derive it carefully, because the bookkeeping of U decay is where this is normally
got wrong. Let the sample crystallise $t_1$ ago, lose a fraction $f$ of its
radiogenic Pb at a time $t_2$ ago, and remain closed since. Writing
$^{206}\mathrm{Pb}^{*}/^{238}\mathrm{U}$ as $x$, the daughter present just before
the loss is a ratio to the uranium *then*, but the measured ratio is a ratio to
the uranium *now*, and the uranium has decayed in the interval. Carrying the
exponential through gives

$$x_{\text{now}} = \left(e^{\lambda_{238} t_1} - 1\right) - f\left(e^{\lambda_{238}
t_1} - e^{\lambda_{238} t_2}\right) = x_1 - f\left(x_1 - x_2\right), \tag{4}$$

and identically for the $^{235}\mathrm{U}$ chain. Equation (4) says that
$x_{\text{now}}$ moves linearly from the concordia point at $t_1$ (for $f = 0$) to
the concordia point at $t_2$ (for $f = 1$). **The family of discordant analyses
therefore lies on the chord between the concordia points at the crystallisation
age and at the disturbance age.** That chord is the **discordia**, and its two
intersections with concordia are the two ages that the data determine.

The demo constructs such a family for a synthetic rock with a true age of 1800 Ma
disturbed at 300 Ma, fits the chord, and intersects it with concordia:

```text
  Pb lost      206/238      207/235   apparent t (Ma)
     0.00     0.322105     4.886903           1,800.0
     0.40     0.212318     3.069637           1,241.2
     1.00     0.047637     0.343738             300.0

  discordia fit:  207/235 = 16.552657 * (206/238) + -0.444787
  max chord residual over the 7 analyses: 2.665e-15 (a single-stage loss gives a mathematically exact line)
  intersections with concordia: 300.00, 1,800.00 Ma
  upper intercept 1,800.00 Ma vs true age 1,800.00 Ma   -> error +0.000 Ma
  lower intercept 300.00 Ma vs disturbance 300.00 Ma -> error +0.000 Ma
```

Both ages are recovered exactly, and **neither was an input**: the input was a
set of ratios. This is what makes U–Pb a dating *system* rather than a
ratio-to-age conversion, and it is why a discordant zircon population is more
informative than a concordant one.

The same output shows the cost of ignoring discordance:

```text
  If the same analyses were used as single chronometer ages and averaged naively, they would report:
    mean of the seven 206/238 ages = 1,147.7 Ma, spread 1,500.0 Ma
    true age = 1,800.0 Ma; error -652.3 Ma (-36.2%)
```

A mean with a spread of 1500 Ma has no interpretation except that the population
is discordant. The spread *is* the diagnostic, and averaging it away is the error.

## 5. The assumptions ledger, with magnitudes

### 5.1 Uncorrected common Pb

An uncorrected common-Pb contribution adds a constant to the measured ratio. The
demo adds a range of offsets to a synthetic 1000 Ma analysis:

```text
  common-Pb offset  206/238 meas.  app. age (Ma)   error (Ma)
             0.000       0.167804        1,000.0         +0.0
             0.005       0.172804        1,027.5        +27.5
             0.010       0.177804        1,055.0        +55.0
             0.020       0.187804        1,109.5       +109.5
```

Because the offset is a constant *added to the ratio*, its effect on the age is
relatively larger for young rocks: the same offset of 0.01 shifts a 100 Ma age by
63.2 Ma, which is 63.2 per cent of the age, against 5.5 per cent at 1000 Ma. Every
U–Pb age is therefore either corrected by measuring a non-radiogenic isotope or
reported with the correction stated.

### 5.2 An open system

A change in the parent inventory has the same effect in the opposite direction. A
five per cent loss of $^{238}\mathrm{U}$ moves a synthetic 500 Ma age by

```text
   lost/added fraction of 238U   apparent age (Ma)   error (Ma)
                         -0.10               553.2        +53.2
                         +0.05               477.0        -23.0
```

Tens of millions of years from a few per cent. When two chronometers in the same
rock disagree by more than their uncertainties, the assumption that failed is
usually closure, and the disagreement is the measurement.

### 5.3 A non-zero initial daughter ratio

Covered in §2: an error of 0.002 in an assumed $^{87}\mathrm{Sr}/^{86}\mathrm{Sr}$
intercept is worth from 35 Ma to 2750 Ma depending on the parent/daughter ratio of
the analysis.

### 5.4 A mixing line, which is not an isochron at all

This one is different in kind. A line through a set of samples can be produced by
two-component mixing rather than by decay, and it can be a perfect line:

```text
  SYNTHETIC end members  x (Rb/Sr)   A = 0.20, B = 0.90
                         y (Sr87/86) A = 0.7110, B = 0.7600
  9 mixtures give a perfect line: slope = 0.070000, intercept = 0.697000
  r^2 = 1.00000000 -- an isochron-fit statistic cannot distinguish this from an isochron.
  'Age' read from the slope with lambda_Rb: 4,764.7 Ma
```

The "age" is a property of the two end-member compositions and of nothing else.
No goodness-of-fit statistic will flag it, because there is nothing wrong with the
fit. The diagnostic is geological and geochemical:

- a mixing line passes through the compositions of its end members, so a suite
  that extrapolates to a plausible crustal or mantle reservoir is suspicious
  rather than reassuring;
- it correlates the isotope ratio with an element ratio that has no business in
  the isochron, for example $1/\mathrm{Sr}$;
- adding a third component bends it.

The demo shows the third test: adding a third component leaves a maximum
departure of 0.0095 in $^{87}\mathrm{Sr}/^{86}\mathrm{Sr}$ from the two-component
line, which is orders of magnitude above a modern measurement precision. A line
becomes an isochron only after mixing has been excluded, and the exclusion is an
argument, not a regression.

## 6. Which systems date what

A summary in the form a reader needs it: the quantity that matters is not the
half-life alone but what the system's closure behaviour makes it date. The
half-life and its compilation-dependence are treated in
[02-09-02 §4](../../02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md);
what follows adds the geological interpretation.

| System | Parent → daughter | Typical use | What the age means | Dominant failure mode |
|---|---|---|---|---|
| U–Pb (zircon, monazite, baddeleyite) | $^{238}\mathrm{U}, ^{235}\mathrm{U} \to \mathrm{Pb}$ | The highest-precision absolute ages available; the backbone of the time scale | Crystallisation, or high-temperature metamorphism, with closure above the temperature of Pb diffusion in zircon | Pb loss (discordance) and inherited cores |
| Rb–Sr (whole rock, mica) | $^{87}\mathrm{Rb} \to ^{87}\mathrm{Sr}$ | Whole-rock isochrons for igneous and metamorphic rocks; mica ages for cooling | Whole-rock: crystallisation or a metamorphic homogenisation; mica: cooling through the Sr closure temperature | Open-system Rb or Sr mobility in fluids; mixing lines |
| Sm–Nd | $^{147}\mathrm{Sm} \to ^{143}\mathrm{Nd}$ | Mafic and ultramafic rocks, and mantle-evolution models | Crystallisation or a high-temperature event; Sm and Nd are relatively immobile | Low parent/daughter ratios give imprecise ages; metamorphic disturbance |
| K–Ar and Ar–Ar | $^{40}\mathrm{K} \to ^{40}\mathrm{Ar}$ | Dating cooling and exhumation; volcanic rocks | Time since the mineral passed its Ar closure temperature | Excess Ar and Ar loss; only useful when the closure temperature is stated |
| Re–Os | $^{187}\mathrm{Re} \to ^{187}\mathrm{Os}$ | Sulfides, molybdenite, organic-rich sediments; mantle melts | Crystallisation or deposition | Re mobility in oxidising fluids |
| $^{14}\mathrm{C}$ | $^{14}\mathrm{C} \to ^{14}\mathrm{N}$ | The last tens of thousands of years: archaeology, Quaternary | Time since the organism stopped exchanging carbon with the atmosphere; requires a calibration curve | Reservoir effects, contamination, and the assumption that the atmospheric inventory was constant |
| (U–Th)/He and fission track | thermochronometers | Exhumation histories | Time since cooling through a low closure temperature | He diffusion is complicated by radiation damage |

Two habits follow. **Never compare two ages from this table without their closure
temperatures**: the table's third column is not decoration, and the second age
from the same rock is usually the evidence about the cooling path rather than a
contradiction. And **never quote a $^{14}\mathrm{C}$ age as a calendar age**:
the conventional age is a model output with a stated half-life, and converting it
to a calendar date requires a named and versioned calibration curve.

## 7. Units, dimensional analysis, and the age equation

The dimensional check is worth doing every time, because one error in it produces
a plausible and completely wrong age.

- $\lambda t$ must be dimensionless, so a decay constant in a$^{-1}$ requires a
  time in years. A $\lambda$ in s$^{-1}$ with $t$ in years is out by the number of
  seconds in a year, $3.155\,76 \times 10^7$.
- A $\lambda$ in a$^{-1}$ with $t$ in **Ma** is out by $10^6$, and the result is a
  rock that is far too young.
- The ratios in equation (3) are dimensionless, so $^{206}\mathrm{Pb}^{*}/^{238}
  \mathrm{U}$ and $^{207}\mathrm{Pb}^{*}/^{235}\mathrm{U}$ have the same units and
  can be plotted against each other.
- An age *difference* carries the uncertainty of both ages, with the correlation
  term, exactly as in
  [04-03-01 §5](./01-geologic-time-scale.md).

## 8. Tying an age to a stratigraphic position

An age in years is not yet a geological statement. The chain from a ratio to a
statement about a rock is:

1. **A geological context.** Which unit, which mineral, which textural site
   within that mineral. A zircon age from a xenocryst in a lava flow dates the
   source rock, not the flow.
2. **A closure model.** Crystallisation, cooling, or a metamorphic
   recrystallisation, stated explicitly.
3. **A bracket.** The dated horizon lies between two stratigraphic levels, and
   the age applies to the interval between them, in the sense of
   [04-03-02 §4](./02-stratigraphic-principles.md).
4. **An attachment to the chart.** The bracket is correlated to a chart boundary,
   and the chart version is recorded. The correlation carries its own uncertainty,
   which is frequently larger than the analytical uncertainty on the age.
5. **A stated uncertainty budget.** Analytical, decay-constant, and
   correlation/stratigraphic uncertainties are different kinds and should be
   reported separately rather than combined into one number.

Step 4 is where most of the total uncertainty lives for an age used in a
correlation, and it is the step most often omitted from a reported age.

## 9. Python demonstration

[`code/03-radiometric_dating_demo.py`](./code/03-radiometric_dating_demo.py)
builds the concordia curve, verifies it against the age equation, constructs and
fits a discordia, recovers both intercepts by numerical intersection with the
curve, and quantifies each assumption in the ledger. Its output is quoted in §3,
§4 and §5.

The two sections that carry the argument are the intercept recovery (§4) and the
mixing test (§5.4). Read the first as a demonstration that a *pair* of ages can
come out of ratios the analyst did not choose, and the second as a demonstration
that a line is not evidence of an age.

Run it with the project environment:

```bash
cd 04-earth-science-geology/03-geologic-time-and-stratigraphy/code
.venv/bin/python 03-radiometric_dating_demo.py
```

## 10. Common mistakes

1. **Calling a date a measurement.** State what was measured and what was
   modelled; a reader cannot evaluate an age without both.
2. **Averaging a discordant population.** A large spread is the signal, not noise
   to be reduced.
3. **Quoting a half-life or decay constant without its compilation.** Ages move
   when compilations move, and a comparison against an older published age must
   use the older constants or say that it does not.
4. **Assuming the initial ratio instead of fitting it** and not saying so.
5. **Ignoring the parent/daughter ratio when assessing a model age.** A
   low-ratio analysis cannot carry an age no matter how precise it is.
6. **Fitting an isochron to a mixing line.** Use the geochemical tests, not the
   goodness of fit.
7. **Mixing units of time inside the age equation.** Compare
   [04-03-01 §5](./01-geologic-time-scale.md); this is the easiest error to make
   and the hardest to notice.
8. **Comparing chronometers without closure temperatures.** Two ages from one rock
   are a cooling history until proven otherwise.
9. **Reporting a $^{14}\mathrm{C}$ age as a calendar age.** Name the calibration
   curve and its version, or report it as a conventional age.
10. **Combining analytical and correlation uncertainty into a single number.**
    They are different kinds of uncertainty and they are used differently
    downstream.

## 11. Real-world applications

- **Building the time scale.** Every boundary age in the Phanerozoic is pinned by
  U–Pb zircon ages from ash beds, with the correlation to the boundary level
  assessed separately ([04-03-01](./01-geologic-time-scale.md)).
- **Basin thermal history.** Apatite fission-track and (U–Th)/He
  thermochronology inverted through a thermal model gives the exhumation history
  that a basin model needs
  ([04](./04-sedimentary-basins.md), [13-06 Crustal and Lithospheric Dynamics](../../13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/README.md)).
- **Provenance and crustal evolution.** Detrital-zircon age populations are the
  standard tool for identifying source terranes, and their interpretation depends
  entirely on the closure assumptions in the table of §6
  ([04-06-02](../06-petroleum-and-mineral-systems/02-mineral-deposits.md)).
- **Archaeology and Quaternary science.** Radiocarbon with a named calibration
  curve, plus U-series for carbonates and speleothems
  ([04-05-04](../05-geomorphology-and-quaternary/04-quaternary-climate.md)).
- **Hydrocarbon charge timing.** Whether a trap was filled before or after it was
  breached is a question about two dates and their uncertainties
  ([04-06-01](../06-petroleum-and-mineral-systems/01-petroleum-system.md)).
- **Volcanic hazard and eruption chronologies.** $^{40}\mathrm{Ar}/^{39}\mathrm{Ar}$
  and $^{14}\mathrm{C}$ on eruption products, where the closure assumption is the
  whole argument ([04-07-02](../07-geologic-hazards/02-volcanic-hazards.md)).

## 12. Further reading

- **Dickin, A. P. *Radiogenic Isotope Geology* (Cambridge University Press).**
  The standard modern treatment: isochrons, concordia, closure temperature and
  the failure modes of each system, with worked data. Level: advanced.
- **Faure, G. *Principles of Isotope Geology* (Wiley).** Complementary account,
  stronger on the classical systems and the analytical chemistry. Level:
  intermediate.
- **Wetherill, G. W. (1956). Discordant uranium–lead ages.** The paper that
  introduced the discordia construction used in §4; the classic reference for the
  geometry. Level: advanced.
- **Steiger, R. H., & Jäger, E. (1977). Subcommission on geochronology: convention
  on the use of decay constants in geo- and cosmochronology.** Establishing why
  the decay constants must be stated with the age. Level: intermediate.
- **Dodson, M. H. (1973). Closure temperature in cooling geochronological and
  petrological systems.** The closure-temperature treatment that this lesson
  defers to 02-09-02 for. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [01 The Geologic Time Scale and Deep Time](./01-geologic-time-scale.md) — what
  the ages are used for, and why the chart is revised.
- [02 Stratigraphic Principles and Relative Dating](./02-stratigraphic-principles.md)
  — the bracket that an age is fitted into.
- [04 Sedimentary Basins: Formation, Fill and Subsidence](./04-sedimentary-basins.md)
  — the archive whose thermal history a thermochronometer inverts for.
- [02-09-02 Radioactive Decay, Half-Life and Dating](../../02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md)
  — the decay law, the isochron equation, closure temperature and the
  compilation problem, all derived.
- [02-09-06 Dosimetry, Radiation Safety and Regulatory Limits](../../02-physics/09-radiation-and-atomic-physics/06-dosimetry.md)
  — the same decay arithmetic used for activity and dose rather than for age.
- [26-02-03 Physical Constants and Earth Parameters with Sources](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the exact/measured/nominal discipline applied to decay constants.

Exercises:
[`exercises/03-radiometric-dating-exercises.md`](./exercises/03-radiometric-dating-exercises.md)
and
[`exercises/03-radiometric-dating-solutions.md`](./exercises/03-radiometric-dating-solutions.md).

## Self-assessment checklist

- [ ] I can state, for a published age, what quantity was measured and which
      model produced the years. (§1)
- [ ] I can explain why an isochron converts an assumption into a measurement and
      why a model age does not. (§2)
- [ ] I can explain what concordant and discordant mean in terms of the two decay
      chains. (§3)
- [ ] I can derive the discordia chord of equation (4) and say what each
      intercept means. (§4)
- [ ] I can quantify the age error from an uncorrected common-Pb offset, from a
      few per cent of parent loss, and from an error in an assumed initial ratio.
      (§5, §9)
- [ ] I can list three geochemical tests that distinguish a mixing line from an
      isochron, and state why no statistical test will. (§5.4)
- [ ] I can name the principal chronometers, what each dates, and its dominant
      failure mode. (§6)
- [ ] I can perform the dimensional check on an age equation in both directions.
      (§7)
- [ ] I can describe the five steps that turn a ratio into a statement about a
      stratigraphic position, and say which step usually dominates the total
      uncertainty. (§8)
