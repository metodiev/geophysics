---
id: 04-04-03
title: "Fold Geometry, Mechanisms and Interpretation"
level: intermediate
prereqs: ["04-04-01", "04-03-02"]
estimated_minutes: 90
tags: [folds, buckling, ramsay-classification, excess-area, kinematics]
---

# Fold Geometry, Mechanisms and Interpretation

A fold is a shape. An interpretation is a claim about the *mechanism* that
produced the shape, and the two are not the same thing — which is the whole
difficulty of structural analysis of folds. Many mechanisms can produce visually
similar folds, so the shape alone under-determines the kinematics, and a
structural geologist's job is to find the observations that separate the
candidates.

This lesson does two things. It computes the **geometry** of a folded surface, so
that statements about amplitude, wavelength, limb dip, curvature and shortening
are exactly related rather than separately measured. And it evaluates the two
classical **mechanisms** — parallel folding by flexural slip, and similar folding
by vertical shear — against measurable quantities, so that the mechanism claim can
be tested. It finishes with a construction that inverts the shape for something
not visible in it at all: the depth to the detachment, by the excess-area method.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the dip, curvature and arc-to-chord shortening of a folded surface
   from its amplitude and wavelength, and explain why dips alone do not determine
   a fold.
2. **Recover** fold amplitude and wavelength from synthetic dip measurements by
   least squares, and state what the fit requires and what it cannot determine.
3. **Apply** Ramsay's thickness classification and explain why the thickness
   ratio is diagnostic of the mechanism rather than of the fold shape alone.
4. **Compute** the flexural-slip shear strain across a limb and contrast it with
   the homogeneous simple shear that would produce the same dip.
5. **State** the buckling relation between dominant wavelength and viscosity
   ratio, verify its exponent, and explain why the relation is used as a
   consistency check rather than as a measurement.
6. **Apply** the excess-area method to recover a detachment depth, derive its
   closed form for a sinusoidal fold belt, and state its kinematic assumption and
   the factor by which it can be wrong.
7. **Classify** a fold by its interlimb angle and state what the classification
   does not tell you.

## Prerequisites

- [01 Stress, Strain and Brittle vs Ductile Deformation](./01-stress-strain-rocks.md)
  — the strain measures used to describe fold kinematics, and the rheology that
  decides which mechanism operates.
- [04-03-02 Stratigraphic Principles and Relative Dating](../03-geologic-time-and-stratigraphy/02-stratigraphic-principles.md)
  — the layered sequence that a fold deforms, and the superposition that makes
  "way-up" a testable property.
- [01-12-02 Interpolation, Splines and Approximation Theory](../../01-mathematics/12-numerical-methods/02-interpolation.md)
  — the least-squares fitting used in §3.

## 1. The geometry of a folded surface

Describe an upright, symmetric fold by its amplitude and wavelength — two numbers
that fix everything else:

$$z(x) = A\cos\frac{2\pi x}{\lambda}. \tag{1}$$

The dip is the slope of the surface, the curvature is the rate of change of the
tangent, and the shortening is the difference between the arc length and the
chord. For a fold with $A = 200$ m and $\lambda = 2000$ m:

```text
   x (m)     z (m)   dip (deg)    curvature (1/m)        fold position
       0     200.0       -0.00         1.9739e-03        hinge (crest)
     250     141.4      -23.96         1.0653e-03                 limb
     500       0.0      -32.14         7.3375e-20 inflection (max dip)
    1000    -200.0       -0.00         1.9739e-03       hinge (trough)
    1500      -0.0       32.14         2.2013e-19 inflection (max dip)
```

Three structural facts are visible in that table, and each is a statement about
folds in general rather than about this one.

**The dip is zero at the hinges and maximum at the inflection points.** For a
sinusoid the maximum limb dip is $\arctan(2\pi A/\lambda) = \arctan(0.628) =
32.14^\circ$, which depends only on the amplitude-to-wavelength ratio.

**The curvature is maximum at the hinges and zero at the inflection points.** This
is why the hinge is where a fold is most likely to be cut by an axial-plane
cleavage, and why hinge zones are where the strain record is most intense.

**The shortening is determined by $A$ and $\lambda$, not measured separately.**
Over four wavelengths the demo finds

```text
  over four wavelengths: chord = 8,000.0 m, arc length = 8,739.1 m
  excess length (shortening) = 739.1 m = 8.4575% of the arc length
  the same quantity per wavelength: 184.78 m
```

so the shortening per wavelength is a consequence of the shape. **Reporting limb
dips alone therefore leaves a fold under-determined**: many combinations of
amplitude and wavelength give the same maximum dip, with different shortennings.
This is why a competent field study reports amplitude and wavelength, or a
bed-length balance, and not just a set of dips.

## 2. What a least-squares fit can and cannot recover

Field measurements are dips at scattered positions, and the natural inversion is
to fit the slope. Because $\mathrm{d}z/\mathrm{d}x = -2\pi A/\lambda\,
\sin(2\pi x/\lambda)$, a sinusoid in the slope with a known frequency has an
amplitude that is proportional to $2\pi A/\lambda$. The demo measures 24 synthetic
dips with 1.5° of random error — a realistic compass-clinometer precision:

```text
  fitted sine coefficient = -0.64191 (slope units)
  recovered amplitude = |c| lambda/(2 pi) = 153.2 m against a true 150.0 m
  error +3.2 m (+2.16%)
  rms residual 0.03019 in slope units = 1.729 deg in dip
```

The amplitude is recovered to 2 per cent, and the residual is consistent with the
1.5° input error. But **the wavelength was supplied**. Fitting the frequency as
well is a nonlinear problem, and with the dips of a single surface it is poorly
conditioned for gentle folds, because a gentle fold at one wavelength and a
slightly steeper one at another are nearly indistinguishable over a short
traverse. This is the practical reason field studies report both dip and
wavelength, and why a map with a handful of dip measurements supports only a rough
fold shape. It is also why the same fold measured along one traverse and along
another rarely gives exactly the same amplitude.

## 3. Mechanisms, and the measurement that distinguishes them

Two end-member mechanisms account for most folds.

**Flexural slip (parallel folding).** The layers slide past one another and each
layer maintains constant thickness measured perpendicular to its boundaries. The
orthogonal thickness at limb dip $\alpha$ is $t_\alpha = t_0\cos\alpha$, so the
thickness ratio is

$$t' = \frac{t_\alpha}{t_0} = \cos\alpha, \tag{2}$$

and the shear strain accumulated across the limb by the layer-parallel slip is

$$\gamma = 2\tan\frac{\alpha}{2}. \tag{3}$$

**Similar folding (vertical shear).** Layers are flattened in the vertical
direction while maintaining their *vertical* thickness, so orthogonal thickness
grows on the limbs. The thickness ratio stays near 1, the fold has a
constant-amplitude, similar shape, and the strain is dominated by flattening
rather than by slip.

The demo tabulates both predictions against the measured quantity:

```text
 alpha (deg)  alpha-prime   parallel t-prime   similar t-prime       class
          10.0        0.111             0.9848            1.0000       1A/1B
          30.0        0.333             0.8660            1.0000          1C
          50.0        0.556             0.6428            1.0000          1C
          70.0        0.778             0.3420            1.0000           3
          90.0        1.000             0.0000            1.0000           3
```

The classification column is Ramsay's, and the point of the table is not the names
but the separation: **at 50° of limb dip the two mechanisms predict thickness
ratios of 0.64 and 1.00**, which is a difference far larger than a field
measurement error. Measuring the thickness ratio therefore discriminates the
mechanisms — which is what makes it worth measuring, and what makes a fold whose
thickness ratio has not been measured a fold whose mechanism is unknown.

Equation (3) deserves its own comparison, because it is easy to assume that a limb
dipping at $\alpha$ records a shear strain of $\tan\alpha$:

```text
    alpha = 30.0 deg: flexural-slip shear strain gamma = 2 tan(alpha/2) = 0.5359;
      homogeneous simple shear to the same dip would need gamma = tan(alpha) = 0.5774
    alpha = 60.0 deg: flexural-slip shear strain gamma = 2 tan(alpha/2) = 1.1547;
      homogeneous simple shear to the same dip would need gamma = tan(alpha) = 1.7321
```

The two differ by 8 per cent at 30° and by 50 per cent at 60°. **A finite-strain
measurement across a limb therefore distinguishes flexural slip from homogeneous
shear**, which is why strain markers — ooids, reduction spots, deformed fossils —
are measured in folded rocks, and why the fold shape alone is not enough.

## 4. Buckling: why folds have the wavelength they do

When a competent layer embedded in a weaker matrix is shortened, it does not
wrinkle at a random wavelength. The classical viscous-buckling analysis gives a
dominant wavelength that depends on the viscosity ratio $G = \eta_{\text{layer}}/
\eta_{\text{matrix}}$:

$$\frac{\lambda_d}{d} = 2\pi\left(\frac{G}{6}\right)^{1/3}, \tag{4}$$

with $d$ the layer thickness. The demo evaluates it:

```text
       G    G^1/6   lambda_d/d   for d = 100 m (m)
      10.0    1.468       7.4495               745.0
     100.0    2.154      16.0495              1605.0
    1000.0    3.162      34.5777              3457.8
```

and verifies the exponent by finite difference on the relation itself:

```text
    from G = 30 to G = 240 (factor 8), the
    wavelength ratio is 2.000000 = 8^(0.333333)
    fitted exponent 0.333333 against the predicted 1/3 = 0.333333
```

The exponent is exactly 1/3, and that is the useful content: **a measured fold
wavelength constrains the viscosity ratio only as its cube.** A factor of two in
wavelength is a factor of eight in viscosity ratio, so the relation is extremely
insensitive in the direction in which it would be used as a measurement. It is
useful in the other direction — as a consistency check on a viscosity ratio
estimated independently, and as an explanation of why folds of similar wavelength
occur in rocks of a range of competence contrasts. Treating equation (4) as a
measurement of viscosity would be a serious over-claim, and the steepness of the
cube-root dependence is the reason.

## 5. The excess-area method, inverted numerically

Chamberlin's construction is the standard way to estimate the depth to a
detachment from a folded section. It states

$$h = \frac{A}{S}, \tag{5}$$

with $h$ the depth to detachment, $A$ the **excess area** of the folded section
above its regional datum, and $S$ the **bed-length shortening**. It is a statement
about where the shortening is accommodated, so it is a kinematic model rather than
a measurement — and it is exact only for the model it assumes.

For a sinusoidal fold belt the model has a closed form, which is what makes it
testable. Over $n$ waves of amplitude $A$ and wavelength $\lambda$:

$$A_{\text{excess}} = \frac{n\lambda A}{2}, \qquad
S = \frac{n\pi^2A^2}{4\lambda} \quad\text{(to second order in the dip)}, \qquad
h = \frac{2\lambda^2}{\pi^2A}. \tag{6}$$

The number of waves cancels, so the method predicts a detachment depth that
depends only on the amplitude and the wavelength. The demo tests this by
integrating the excess area and the arc length numerically:

```text
  amplitude 800 m, wavelength 4000 m, maximum limb dip 51.5 deg,
  predicted h = 4,052.8 m
  waves n   A_excess (m^2)      S (m)   h = A/S (m)  closed form (m)   difference
          2        3,200,000     739.07       4,329.8          4,052.8      +276.90
         20       32,000,000   7,390.72       4,329.8          4,052.8      +276.90
```

The recovery is independent of $n$, which is the content of equation (6), and the
numerical and closed-form values differ by 6.83 per cent. That difference is not
numerical error: it is the second-order arc-length approximation failing at a
maximum limb dip of 51.5°, where the expansion of $\sqrt{1 + w'^2}$ in $w'$ is no
longer adequate. **The rule that follows is to use the exact arc length whenever
the limbs are steeper than about 30°**, which is most folds of interest. This is a
good example of a case where the approximation, not the data, is the limiting
error — and where knowing the approximation's domain is what lets you tell.

The sensitivity of the recovered depth is worth stating in the same breath:

```text
  amplitude (m)  wavelength (m)      h (m)   h for A+10% (m)  h for lambda+10% (m)
              800           4,000      4,330             3,984                 5,184
  the two perturbed columns change h by -8.0% and +19.7% respectively
```

The asymmetry is the point: $h$ is proportional to $1/A$ but to $\lambda^2$, so a
10 per cent error in wavelength moves the depth twice as much as a 10 per cent
error in amplitude. **Detachment depths from this method are limited by the
wavelength estimate**, and the wavelength of a fold belt is exactly the quantity
most sensitive to how much of the belt is exposed.

Finally, the kinematic caveat, stated rather than hidden. Equation (5) assumes
that the shortening is accommodated entirely at the detachment and that the
section is balanced. A single ramp with no flat gives $A = hS/2$ instead, so the
same fold belt would be inverted to $h = 2A/S = 8{,}660$ m — **a factor of two,
larger than every measurement error in the tables above.** The kinematic model,
not the measurements, sets the uncertainty.

## 6. Fold tightness, and what a classification does not say

The **interlimb angle** is the angle between the two limbs measured in the profile
plane. For a symmetric fold with limb dip $\alpha$ it is $180^\circ - 2\alpha$:

```text
  limb dip (deg)   interlimb angle (deg)           class
               5.0                   170.0     gentle/open
              40.0                   100.0           close
              60.0                    60.0           tight
              80.0                    20.0       isoclinal
              90.0                     0.0      not a fold
```

The names differ slightly between schemes, so the honest practice is to report the
angle and name the scheme. What matters more is what the classification **does not
say**. An interlimb angle carries no information about amplitude, wavelength or
shortening: a tight fold at one wavelength and a gentle fold at many wavelengths
can shorten the same bed by the same amount. Tightness describes the *shape* of a
hinge, and the shortening describes the *deformation*; a report that gives only
one of them is incomplete. This is the same point as §1, sharpened: shape and
shortening are related only once the fold is parameterised, and the parameter count
is small.

## 7. Assumptions and regime of validity

- **Sinusoidal geometry is a model.** Real folds have straight limbs and sharp
  hinges (chevron and kink geometries), or rounded hinges and planar limbs, or
  irregular profiles. A sinusoid is the simplest shape that has an amplitude and a
  wavelength, which is why it is a useful reference and not a description.
- **Two-dimensional plane strain.** Folds are treated in a profile plane with no
  along-strike variation. Folds that plunge, or that vary along strike, need a
  third dimension.
- **Layer-parallel slip and vertical shear are end members.** Real folds combine
  them with flattening, and the mixture is the point: measuring $t'$ places a fold
  between the two predictions, which is more informative than assigning it to one.
- **The buckling relation assumes Newtonian viscous layers and a single competent
  layer.** Power-law rheology, multiple layers and a free surface all modify the
  wavelength and the amplification rate.
- **The excess-area method assumes a balanced section and a known kinematic
  model.** Its factor-of-two sensitivity to the model is larger than its
  measurement errors, as §5 shows.
- **Bed-length balance assumes no penetrative strain.** If the bed itself
  shortened, the arc length is not the original length and the shortening is
  underestimated.

## 8. Python demonstration

[`code/03-folds_demo.py`](./code/03-folds_demo.py) computes the fold geometry and
shortening, performs the least-squares amplitude recovery, tabulates the Ramsay
classification and the flexural-slip shear strain, evaluates and verifies the
buckling relation, and inverts a sinusoidal fold belt for its detachment depth with
an exact arc-length quadrature. Its output is quoted in §1 to §6.

The two verifications worth running yourself: the finite-difference exponent in
§4, which must come out as 1/3, and the excess-area inversion in §5, which must
recover a depth that is independent of the number of waves.

```bash
cd 04-earth-science-geology/04-structural-geology/code
.venv/bin/python 03-folds_demo.py
```

All folds in the script are synthetic constructions from the stated mechanisms.
No named fold belt is being described.

## 9. Common mistakes

1. **Reporting limb dips as if they determined the fold.** They do not; amplitude
   and wavelength do, and the shortening follows from them.
2. **Fitting a wavelength from the dips of a single traverse.** The problem is
   poorly conditioned, and the result is a consequence of the traverse length.
3. **Assigning a mechanism without measuring the thickness ratio.** At 50° limb
   dip the two mechanisms differ by a factor of 1.6 in $t'$.
4. **Assuming a limb records a shear strain of $\tan\alpha$.** Flexural slip gives
   $2\tan(\alpha/2)$, which is 8 per cent smaller at 30° and 50 per cent smaller at
   60°.
5. **Using the second-order arc-length formula on steep limbs.** The error reaches
   7 per cent at 51° of dip.
6. **Treating the buckling wavelength as a viscosity measurement.** The cube-root
   dependence makes it an extremely weak one.
7. **Quoting a detachment depth without the kinematic model.** The model can
   change the answer by a factor of two.
8. **Confusing fold tightness with finite shortening.** They are different
   quantities, and neither determines the other.
9. **Ignoring penetrative strain when balancing a section.** Bed-length balance
   underestimates the shortening if the bed itself shortened.
10. **Measuring a fold in one profile plane and assuming it is cylindrical.**
    Plunging and non-cylindrical folds need more than one section.

## 10. Real-world applications

- **Balanced cross-sections in fold-and-thrust belts.** The excess-area method of
  §5 and bed-length balancing are the standard tools for estimating detachment
  depth and shortening in an exploration play
  ([04-06-01 Source, Reservoir, Seal and Trap: The Petroleum System](../06-petroleum-and-mineral-systems/01-petroleum-system.md)).
- **Trap geometry.** Four-way dip closures and fault-bend folds are recognised from
  the geometry of §1 and §6, and their volumes depend on amplitude and wavelength.
- **Cleavage and hinge-zone strain.** The curvature maximum at the hinge is where
  axial-plane cleavage develops, and where a fold's strain record is concentrated.
- **Seismic imaging of folds.** Amplitude, wavelength and limb dip are what an
  interpreter measures on a stacked section, and the fold axis is a
  horizon-consistent attribute
  ([06-09-09 Structural and Stratigraphic Interpretation](../../06-seismology/09-reflection-seismology/09-interpretation-reflection.md)).
- **Anisotropy from folded fabric.** The crystallographic and shape fabrics
  developed by the mechanisms of §3 are a cause of seismic anisotropy, and
  measurement of the fabric is what calibrates it
  ([04-04-04](./04-fractures-joints.md)).
- **Geological storage and cap-rock integrity.** Fold geometry controls whether a
  closure exists, and the hinge zone is where the cap rock is most likely to be
  fractured.

## 11. Further reading

- **Ramsay, J. G. *Folding and Fracturing of Rocks* (McGraw-Hill).** The source of
  the thickness classification of §3 and the geometric analysis of §1; still the
  reference treatment. Level: advanced.
- **Ramsay, J. G., & Huber, M. I. *The Techniques of Modern Structural Geology,
  Volume 2: Folds and Fractures* (Academic Press).** The classification in its
  applied form, with the measurements and the plotting methods. Level: advanced.
- **Fossen, H. *Structural Geology* (Cambridge University Press).** The observation
  and description of folds, with the modern kinematic vocabulary. Level:
  intermediate to advanced.
- **Suppe, J. *Principles of Structural Geology* (Prentice-Hall).** The
  kinematic-model approach to folds, including the kink methods that the
  excess-area discussion in §5 relates to. Level: advanced.
- **Twiss, R. J., & Moores, E. M. *Structural Geology* (W. H. Freeman).** A
  broader treatment, with the mechanics of folding developed alongside the
  geometry. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [01 Stress, Strain and Brittle vs Ductile Deformation](./01-stress-strain-rocks.md)
  — the rheology that decides which fold mechanism operates, and the strain
  measures used in §3.
- [02 Fault Geometry, Kinematics and Fault Classification](./02-faults.md) — the
  brittle response to the same shortening.
- [04 Fractures, Joints and Their Geophysical Signature](./04-fractures-joints.md)
  — the fracture fabrics that folds and their hinges develop, and their seismic
  signature.
- [05 Reading Geological Maps and Constructing Cross-Sections](./05-geologic-maps-sections.md)
  — the planar and folded geometries drawn on a map, and how a section is built
  from them.
- [04-03-02 Stratigraphic Principles and Relative Dating](../03-geologic-time-and-stratigraphy/02-stratigraphic-principles.md)
  — the layered sequence that provides the way-up evidence a fold analysis needs.
- [04-03-04 Sedimentary Basins: Formation, Fill and Subsidence](../03-geologic-time-and-stratigraphy/04-sedimentary-basins.md)
  — the subsidence that the fold belt later shortens.
- [06-09-09 Structural and Stratigraphic Interpretation](../../06-seismology/09-reflection-seismology/09-interpretation-reflection.md)
  — how fold geometry appears in reflection data.

Exercises:
[`exercises/03-folds-exercises.md`](./exercises/03-folds-exercises.md)
and
[`exercises/03-folds-solutions.md`](./exercises/03-folds-solutions.md).

## Self-assessment checklist

- [ ] I can compute the maximum limb dip and the shortening of a sinusoidal fold
      from its amplitude and wavelength. (§1)
- [ ] I can explain why limb dips alone leave a fold under-determined. (§1, §2)
- [ ] I can recover an amplitude from synthetic dips by least squares and state
      what the fit had to assume. (§2)
- [ ] I can state the thickness-ratio predictions of the two mechanisms and say
      how large their difference is at a given limb dip. (§3)
- [ ] I can compute the flexural-slip shear strain and compare it with
      homogeneous simple shear. (§3)
- [ ] I can state the buckling relation, verify its exponent, and explain why it
      is a weak constraint on viscosity. (§4)
- [ ] I can apply the excess-area method and derive its closed form for a
      sinusoidal fold belt. (§5)
- [ ] I can state the factor by which the excess-area method depends on its
      kinematic model. (§5)
- [ ] I can classify a fold by its interlimb angle and say what the
      classification omits. (§6)
- [ ] I can list the assumptions of a fold kinematic model and the regime in
      which each fails. (§7)
