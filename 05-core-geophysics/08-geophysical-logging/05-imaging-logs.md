---
id: 05-08-05
title: "Borehole Imaging, Dipmeter and Fracture Detection"
level: graduate
prereqs: ["05-08-01", "05-08-04", "13-03-01"]
tags: [imaging, dipmeter, fracture, breakout, stress-orientation, aliasing, aperture]
---

# Borehole Imaging, Dipmeter and Fracture Detection

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** what a borehole image log measures physically — a
   resistivity or acoustic property of the *wall* on a fine grid — and why it is
   not a photograph.
2. **Derive** the relation between a planar boundary's sinusoid on an unwrapped
   image and the bed's true dip and dip azimuth.
3. **Compute** the dip and azimuth from a synthetic image by least squares, and
   state the azimuthal sampling limit and the aliasing rule that governs it.
4. **Correct** an image-log dip for borehole deviation, and quantify the error
   incurred by not doing so.
5. **Explain** why a fracture aperture from an image is a calibration-dependent
   estimate, and report it accordingly.
6. **Use** borehole breakouts to determine stress orientation, and state the
   assumptions that makes.

## Prerequisites

- [05-08-01 The Borehole Environment and Invasion Profiles](./01-borehole-environment.md)
  — breakouts and hole geometry.
- [05-08-04 Density, Neutron and Sonic Porosity Logs](./04-porosity-logs.md)
  — the other wall-contact measurement and the fractured-porosity case.
- [13-03-01 Quantitative Plate Tectonics: Kinematics and Driving Forces](../../13-geodynamics-tectonics/03-plate-tectonics-quantitative/README.md)
  — the tectonic context in which stress orientation matters.

## 1. Intuition: a map of the wall, not a picture of the rock

An image log is a two-dimensional array: one index is depth along the hole, the
other is azimuth around the hole. The value in each cell is a measured property of
the formation within a few millimetres of the wall:

- **Resistivity images** (pad electrodes or a rotating button): a map of
  micro-resistivity contrast. Conductive features are dark; resistive features are
  light.
- **Acoustic images** (rotating transducer): a map of reflected amplitude and
  travel time, which images the wall's geometry and its hardness contrast.

Two consequences follow immediately:

1. **It is a surface measurement.** It says nothing about the rock a metre into the
   formation. A fracture seen on the image is a fracture at the wall; whether it is
   open, conductive or connected at reservoir scale is a separate inference.
2. **It is a borehole measurement of a disturbed wall.** The mudcake, the
   enlargement, the tool's own pad pressure and the invasion profile all appear in
   the image. Distinguishing a geological feature from a drilling artefact is the
   first interpretive skill.

What image logs buy is *geometry*: bed attitudes at a resolution no other log has,
fracture and fault identification, and stress orientation from breakouts.

## 2. Precise definitions

### 2.1 The unwrapped image and azimuth

A cylindrical borehole wall is cut along one azimuth and flattened, producing an
image whose horizontal axis is azimuth (0–360°) and whose vertical axis is measured
depth. The tool records the azimuth of each pad or of the transducer, so the
horizontal coordinate is *absolute* azimuth, not a relative one.

### 2.2 The sinusoid of a planar bed

A planar bed intersecting a circular cylinder of diameter $D$ appears on the
unwrapped image as

$$z(\theta) = z_0 - \frac{D}{2}\tan\delta\,\cos(\theta - \theta_d), \tag{1}$$

where $\delta$ is the bed's dip from horizontal, $\theta_d$ the dip azimuth, and
$z_0$ the depth at the axis. The **amplitude** gives the dip, the **phase** the
azimuth, and the offset the depth.

### 2.3 Breakout and drilling-induced fracture

- **Breakout:** the hole enlarges in the direction of the *least* principal
  horizontal stress, because the compressive stress concentration there exceeds the
  rock strength. Breakouts are therefore aligned with $\sigma_{h,\min}$ and are
  orthogonal to $\sigma_{H,\max}$.
- **Drilling-induced fracture:** a tensile fracture at the wall aligned with the
  direction of *greatest* principal horizontal stress, i.e. orthogonal to a
  breakout.

Reading stress orientation from them requires the hole to be vertical (or the
deviation to be corrected), the failure to be drilling-induced rather than
natural, and the rock to be competent enough that no other mechanism produced the
feature.

### 2.4 Apparent (relative) dip

The angle an image actually measures is between the bed and the **hole axis**:

$$\cos\delta_{\text{rel}} = \cos\theta\cos\delta
+ \sin\theta\sin\delta\cos\Delta, \tag{2}$$

with $\theta$ the hole inclination from vertical, $\delta$ the true bed dip, and
$\Delta$ the azimuth difference between the hole direction and the bed's dip
direction.

## 3. Derivations

### 3.1 Dip and azimuth from the sinusoid, verified

Equation (1) is linear in $(\cos\theta, \sin\theta, 1)$, so a three-parameter linear
least squares recovers the amplitude $A = (D/2)\tan\delta$ and the phase directly:

$$\delta = \arctan\!\left(\frac{2A}{D}\right), \qquad
\theta_d = \operatorname{atan2}(b,a). \tag{3}$$

The demonstration confirms this exactly: for a true dip of $22.00°$ and azimuth
$135.0°$ in a 0.20 m hole, it recovers dip $22.00°$ ($-0.000$ per cent) and azimuth
$135.0°$ ($+0.00°$), with the fitted amplitude 0.0404 m equal to the true one. So
the *estimator* is exact; everything else in this lesson is about whether the data
it is given are the bed's sinusoid.

### 3.2 What azimuthal sampling costs, and the aliasing rule

A perfectly planar bed is a single sinusoid, so **any** three or more azimuths
represent it exactly — the sampling limit does not exist for a plane. The limit
appears for a *folded* surface, which contains harmonics. A harmonic of order $m$
(measured in cycles per revolution) sampled at $P$ evenly spaced azimuths folds to

$$m_{\text{folded}} = \left| m - P\,\mathrm{round}(m/P) \right|. \tag{4}$$

If $m_{\text{folded}} = 1$ the harmonic lands on the fundamental and biases the dip;
if it is 0 or $\ge 2$ it does not. The measured table (bed with a 25 per cent
harmonic into the same synthetic image) confirms the rule row by row:

| $m$ | $P$ | folded order | dip error | azimuth error |
|---|---|---|---|---|
| 2 | 3 | 1 | $+3.677°$ | $-8.543°$ |
| 2 | 4 | 2 | $-0.000°$ | $+0.000°$ |
| 3 | 4 | 1 | $-5.142°$ | $+0.000°$ |
| 4 | 3 | 1 | $+3.677°$ | $+8.543°$ |
| 4 | 5 | 1 | $+3.677°$ | $+8.543°$ |
| 4 | 6 | 2 | $+0.000°$ | $+0.000°$ |
| any | 360 | $\ge 2$ or 0 | $0$ | $0$ |

Two practical conclusions. A **rotating tool with hundreds of azimuths per
revolution is immune** to this. A **four- or six-pad tool is not**, and its output
carries no warning: it reports a dip, confidently, for the wrong surface. The rule
of equation (4) is the same aliasing arithmetic as
[05-07-06 §3.3](../07-interpretation-and-integration/06-interpretation-pitfalls.md),
applied around the hole instead of along it.

### 3.3 Borehole deviation, quantified

Equation (2) converts a true dip into the angle the image log measures. For a hole
at $30°$ from vertical and a true bed dip of $22°$:

| Azimuth difference $\Delta$ | relative dip | error if called true dip |
|---|---|---|
| 0° | 8.00° | $-14.00°$ |
| 60° | 26.28° | $+4.28°$ |
| 90° | 36.59° | $+14.59°$ |
| 180° | 52.00° | $+30.00°$ |

A single true dip of $22°$ produces image-log dips from **8.0° to 52.0°** —
a factor of six — purely as a function of the hole's orientation relative to the
bed. Reporting the raw sinusoidal dip as stratigraphic dip is therefore wrong by an
amount that can exceed the dip itself. Deviation must come from the same run, and
the correction must precede any structural interpretation.

### 3.4 Fracture aperture: the answer is mostly the calibration

Open fractures are conductive (in a water-based mud) and appear as dark traces. The
aperture is *not* directly measured; it is inferred from the trace's conductivity
anomaly through an empirical relation of the form

$$w \propto \text{(anomaly)}^{\,p}, \tag{5}$$

in which the exponent $p$ and the constant come from modelling, from core
comparison, or from a published relation. The demonstration shows the consequence
with a synthetic trace of anomaly 0.35 and a stated constant:

| Assumed exponent | Recovered aperture |
|---|---|
| 0.50 | 0.2958 mm |
| 0.725 | 0.2336 mm |
| 1.00 | 0.1750 mm |

The same trace gives apertures differing by a factor of **1.7**. So an aperture
from an image log is a *calibration-dependent* estimate: report the relation, its
source, and the range. Quoting a value to two decimals without the relation
overstates the measurement, and comparing apertures between two wells interpreted
with different relations is comparing calibrations, not rocks.

## 4. Worked examples

### 4.1 A dip sequence and a structural interpretation

An image log through a folded interval gives a dip-and-azimuth track. Before
mapping:

1. Correct for deviation (§3.3), to true dip and true azimuth.
2. Check the *azimuth consistency*: a fold's limbs should show two coherent azimuth
   populations, not scatter. Scatter usually means the picks are following
   artefacts.
3. Separate structural dip from sedimentary dip through a cross-bedding or
   foreset pattern, which shows as a characteristic upward-steepening or
   upward-shallowing trend.
4. State the depth reference and the deviation source.

The routine failure is to interpret the raw track, which mixes hole orientation
with structure and produces a fold that does not exist.

### 4.2 Fracture characterisation, with the honest limits

From an image log one can report: the number of conductive traces per metre, their
orientation (often in sets with common strike), and a *range* of apertures under a
stated relation. One cannot report directly: whether the fractures are open at
reservoir conditions, whether they are connected, or their permeability. Those
require a flow test, a pressure transient, or a borehole image *plus* a production
log — and the last is exactly the kind of combined evidence that
[05-07-03](../07-interpretation-and-integration/03-multi-method-integration.md)
insists on.

### 4.3 Stress orientation from breakouts

Measured breakout azimuths across an interval give the direction of
$\sigma_{h,\min}$. Requirements and caveats:

- The hole must be near-vertical, or the breakout azimuth must be rotated into the
  geographic frame using the deviation survey.
- The breakouts must be drilling-induced; a natural cave or a keyseat looks similar.
- The interval must be in a competent lithology, or the breakouts reflect
  lithology rather than stress.
- A single well gives a line, not a field: orientations can rotate between wells,
  and one well cannot resolve that.

Report the azimuth with its dispersion and the interval it came from; a single
number with no spread hides whether the measurement is one population or two.

## 5. Assumptions

1. **The image is of the formation**, not of mudcake, and the tool has contacted
   the wall (pad tools fail in rugose holes).
2. **The sinusoid is a bed**, which fails for a fault, a channel margin or a
   slumped surface.
3. **The bed is planar over the imaged interval.** Curved surfaces give non-sinusoidal
   traces and the fit is biased.
4. **Deviation and azimuth references are correct and from the same run.**
5. **The aperture relation is stated**, with its source and its range.
6. **Breakouts are drilling-induced and the rock is competent**, for stress work.
7. **Azimuthal coverage is adequate** for the feature being interpreted: rotating
   tools for folds, pads are sufficient only for planar beds (§3.2).

## 6. Units and dimensional analysis

- Depth: measured depth, m. Azimuth: degrees from north, clockwise. Do not mix with
  the geological convention (clockwise from north is standard in borehole work;
  structural geology often uses right-hand rules) without stating it.
- Dip: degrees from horizontal. Equation (3): $A/D$ is dimensionless, so the
  arctangent is in radians and must be converted to degrees.
- Equation (1): $z$ in m, $D$ in m, $\tan\delta$ dimensionless ✓.
- Aperture: mm or µm; state which. The relation of equation (5) is dimensionally
  heterogeneous (empirical), so its constant carries the units — quote it.
- Fracture density: number per metre, or a count over a stated interval. A count
  without its interval is not a density.

## 7. Python demonstration

`code/imaging_demo.py` fits sinusoids, scans the aliasing table, and computes the
deviation correction.

```python
design = np.column_stack([np.cos(np.radians(az)), np.sin(np.radians(az)),
                          np.ones_like(az)])
coef, *_ = np.linalg.lstsq(design, z, rcond=None)
dip = np.degrees(np.arctan(2.0 * np.hypot(coef[0], coef[1]) / DIAMETER))
phase = np.degrees(np.arctan2(coef[1], coef[0])) % 360.0
```

Measured output, abridged:

```
true dip 22.00 deg, azimuth 135.0 deg
fitted amplitude 0.0404 m -> dip 22.00 deg (-0.000 per cent)
fitted phase 135.0 deg (error +0.00 deg)

m   P    folded order   dip error (deg)   azimuth error (deg)
 2    3              1            +3.677               -8.543
 3    4              1            -5.142               +0.000
 4    5              1            +3.677               +8.543
 4    6              2            +0.000               +0.000

true bed dip from horizontal = 22.0 deg, hole inclination = 30.0 deg from vertical
azimuth difference   relative dip (deg)   error if called true dip (deg)
               0                 8.00                       -14.00
              90                36.59                       +14.59
             180                52.00                       +30.00

  exponent 0.500 (square-root           ): aperture = 0.2958 mm
  exponent 0.725 (commonly used exponent): aperture = 0.2336 mm
  exponent 1.000 (linear                ): aperture = 0.1750 mm
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Dip and azimuth recovered exactly for a plane | The estimator is not the weak link |
| A 4-pad tool aliases the $m=4$ harmonic by $+3.7°$ | Pad count, not depth resolution, is the sampling limit for folds |
| One true dip gives relative dips from 8.0° to 52.0° | Deviation correction is not optional |
| Three plausible exponents give apertures differing by 1.7× | An aperture is a calibration, and must be reported as one |

> **Breaking exercise.** Set the hole inclination to $0°$ and re-run Section 3.
> Predict the table before running, and explain in one sentence why a vertical hole
> makes the apparent dip equal the true dip.

## 8. Exercises

[`exercises/05-imaging-logs-exercises.md`](./exercises/05-imaging-logs-exercises.md)
and
[`exercises/05-imaging-logs-solutions.md`](./exercises/05-imaging-logs-solutions.md).

### ★ Foundational

**★1.** State what an image log measures and three things it does not measure.

**★2.** For $D = 0.20$ m and a sinusoid amplitude of 0.05 m, compute the dip.

**★3.** State the two directions a breakout and a drilling-induced fracture
indicate, and which principal stresses they correspond to.

### ★★ Applied

**★★4.** Run `code/imaging_demo.py` and report the aliasing table for $m = 6$ with
$P \in \{3,4,5,6,8,12\}$, together with the folded order for each row.

**★★5.** A horizontal well ($90°$ from vertical) crosses a bed dipping $10°$. Using
equation (2), compute the relative dip and state what the image tool would report
and how wrong it would be.

**★★6.** For a conductive trace of anomaly 0.20 and the three exponents of §3.4,
report the three apertures and the range, and state what additional measurement
would constrain the exponent.

### ★★★ Research-oriented

**★★★7.** Build a synthetic image of a folded surface containing harmonics 1
through 6 with decreasing amplitude, sample it with 4, 6 and 96 pads, and report
the dip bias as a function of fold amplitude. Compare with the $m_{\text{folded}}=1$
rule and state where the rule under-predicts the bias.

**★★★8.** From the demonstration's breakout algebra, design a stress-orientation
study for a field with three wells at different azimuths. State the number of
independent orientation measurements, the expected dispersion, and the tectonic
conclusion you could and could not support.

## 9. Common mistakes

1. **Treating the image as a photograph.** It is a wall property map on a fine grid.
2. **Reporting the raw sinusoidal dip as true dip.** Error up to 30° in the
   demonstration (§3.3).
3. **Believing a dip from a 4-pad tool through a fold.** Aliasing, with no warning
   (§3.2).
4. **Quoting a fracture aperture without the calibration relation.** A factor of
   1.7 in the demonstration (§3.4).
5. **Reading a breakout as stress in a washed-out or faulted interval.**
6. **Comparing fracture intensities between wells logged with different tools and
   processing.**
7. **Ignoring the tool's pad pressure and the mudcake**, which produce features that
   look geological.

## 10. Real-world applications

- **Structural interpretation.** Dip sequences are the highest-resolution
  structural data available in a well, and they anchor 3-D models between seismic
  lines.
- **Fractured reservoir characterisation.** Fracture orientation sets and density
  are primary inputs; permeability still requires a flow measurement.
- **Geomechanics and wellbore stability.** Breakout azimuths give stress
  orientation, which controls drilling direction and completion design.
- **Unconventional reservoirs.** Image logs identify natural fractures, bed
  boundaries and the minimum horizontal stress direction for hydraulic fracture
  design.
- **Geothermal wells.** Fracture networks control permeability in most geothermal
  systems, and image logs are the standard acquisition for it
  ([05-09-03](../09-geothermal-and-heat-flow-methods/03-geothermal-exploration.md)).

## 11. Further reading

- **Ellis, D. V. & Singer, J. M. (2007). *Well Logging for Earth Scientists*
  (2nd ed.). Springer.** Chapter 16. Level: intermediate to advanced. Imaging tool
  physics, including acoustic and resistivity devices.
- **Serra, O. (1986). *Fundamentals of Well-Log Interpretation*, Vol. 2.
  Elsevier.** Level: intermediate. Dipmeter processing and structural
  interpretation.
- **Zoback, M. D. (2007). *Reservoir Geomechanics*. Cambridge University Press.**
  Chapters 4 and 6. Level: advanced. Breakouts, drilling-induced fractures and
  stress orientation, including the assumptions of §4.3.
- **Luthi, S. M. (2001). *Geological Well Logs: Their Use in Reservoir Modeling*.
  Springer.** Level: advanced. Image-log interpretation for sedimentary and
  structural geology.
- **Prioul, R., Donald, J., Koepsell, R., El Marzouki, Z. & Bratton, T. (2007).
  Forward modeling of fracture-induced sonic anisotropy. *Geophysics*, 72(4),
  D67–D83.** Level: advanced. Fracture signature in other measurements, useful for
  cross-checking an image-log fracture interpretation.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-07-06 Common Interpretation Pitfalls and False Positives](../07-interpretation-and-integration/06-interpretation-pitfalls.md)
  — the aliasing arithmetic of §3.2 in its general form.
- [05-08-06 Vertical Seismic Profiling and Check Shots](./06-seismic-while-drilling.md)
  — the other borehole measurement that images geometry away from the wall.
- [05-08-07 Log Interpretation, Petrophysics and Uncertainty](./07-log-interpretation.md)
  — where fracture and stress results enter a full interpretation.
- [13-04-02 Fault Mechanics](../../13-geodynamics-tectonics/04-tectonophysics-deformation/02-fault-mechanics.md)
  — the mechanical context for fracture orientation.
- [05-09-03 Geothermal Exploration Geophysics](../09-geothermal-and-heat-flow-methods/03-geothermal-exploration.md)
  — a setting where fracture characterisation decides the resource.

## Self-assessment checklist

- [ ] I can state what an image log measures and its two physical variants. (§1)
- [ ] I can derive dip and azimuth from a sinusoid and verify the fit. (§3.1)
- [ ] I can apply the aliasing rule and say which tools are immune. (§3.2)
- [ ] I can correct a dip for deviation and quantify the error of not doing so.
      (§3.3)
- [ ] I can report a fracture aperture with its calibration and range. (§3.4)
- [ ] I can state the assumptions behind a breakout stress orientation. (§2.3, §4.3)
- [ ] I can run the demonstration and interpret every printed number. (§7)
