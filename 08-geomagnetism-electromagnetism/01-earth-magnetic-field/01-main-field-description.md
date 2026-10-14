---
id: 08-01-01
title: "Describing the Main Field: Declination, Inclination, Intensity"
level: intermediate
prereqs: ["05-02-01", "05-02-02", "02-07-02"]
tags: [geomagnetism, main-field, magnetic-elements, declination, inclination, units]
---

# Describing the Main Field: Declination, Inclination, Intensity

The Earth's magnetic field at a point is a **vector**, but almost nothing a
geophysicist wants to say about it is a vector statement. A survey report says
"declination is 4.3° east"; a palaeomagnetist says "inclination is 64°"; a
compass says "the needle points 4° east of north". Those are three different
scalars extracted from the same vector, and the whole of this module depends on
being able to move between them without losing track of which is measured, which
is derived, and which is defined only where the field geometry allows it.

**All models and data in this module are SYNTHETIC.** The sites in the
demonstration are chosen teaching vectors; no survey, observatory or published
field model is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** between the three field components $(X,Y,Z)$ and the elements
   $(H,F,D,I)$, stating the sign conventions explicitly.
2. **Derive** the relations $H^2 = X^2+Y^2$, $\tan D = Y/X$,
   $\tan I = Z/H$ and $F^2 = X^2+Y^2+Z^2$ from the geometry of the
   north–east–down frame.
3. **Convert** between nT, T, gamma and the equivalent magnetising field in
   A/m, and explain why a "conversion" between $B$ and $H$ is not a unit
   conversion but a physical relation.
4. **Compute** how a component error propagates into $D$ and $I$, and identify
   the region where $D$ becomes ill-conditioned.
5. **Order** the elements by how directly they are measured, and state what each
   instrument type actually returns.
6. **State** the assumptions that make "the field at a site" a well-defined
   object at all.

## Prerequisites

- [05-02-01 Scalar and Vector Fields; Potentials and Gradients](../../05-core-geophysics/02-geophysical-fields-and-observables/01-scalar-vs-vector-fields.md)
  — components, magnitude, direction.
- [05-02-02 Units and Conventions for Gravity, Magnetic and EM Data](../../05-core-geophysics/02-geophysical-fields-and-observables/02-field-measurement-units.md)
  — the nT and the sign conventions used across the curriculum.
- [02-07-02 Magnetostatics, Biot–Savart and Ampère's Law](../../02-physics/07-electromagnetism/02-magnetostatics.md)
  — $\mathbf{B}$, $\mathbf{H}$ and $\mu_0$.

## 1. The frame, the conventions, and the seven elements

Choose a right-handed local frame at the observation point:

- $X$: **north**, positive towards geographic north;
- $Y$: **east**, positive towards geographic east;
- $Z$: **down**, positive towards the centre of the Earth.

With that frame fixed, the field vector has three components, and three
magnitudes and two angles are derived from them:

| Symbol | Name | Definition | Unit |
|---|---|---|---|
| $X$ | north component | — | nT |
| $Y$ | east component | — | nT |
| $Z$ | vertical component (down) | — | nT |
| $H$ | horizontal intensity | $\sqrt{X^2+Y^2}$ | nT |
| $F$ | total intensity | $\sqrt{X^2+Y^2+Z^2}$ | nT |
| $D$ | **declination** | $\arctan(Y/X)$, positive east of north | ° |
| $I$ | **inclination** (dip) | $\arctan(Z/H)$, positive downward | ° |

Only seven of the eight entries are independent, because $F^2 = H^2 + Z^2$ ties
the three magnitudes together. This is the arithmetic content of the whole
lesson: the field has three degrees of freedom, and any three independent
combinations of the above can carry them.

### 1.1 Derivation of the relations

Decompose in two stages. First, project the vector onto the horizontal plane:
the north and east components form a right triangle with hypotenuse $H$, so

$$H = \sqrt{X^2+Y^2}, \qquad X = H\cos D, \qquad Y = H\sin D,
\qquad \tan D = \frac{Y}{X}.$$

Second, the horizontal vector $H$ and the vertical $Z$ form a second right
triangle with hypotenuse $F$:

$$Z = H\tan I, \qquad F = \frac{H}{\cos I} = H\sqrt{1+\tan^2 I},
\qquad \tan I = \frac{Z}{H}.$$

Combining, $F^2 = H^2 + Z^2 = X^2+Y^2+Z^2$: the total intensity is the
Euclidean norm of the component triple. Nothing here is a new law of physics; it
is the geometry of a right-handed orthogonal frame, and the only content is the
convention that $D$ is measured towards **east** and $I$ towards **down**.

### 1.2 Worked example — components to elements

Take the SYNTHETIC site A of the demonstration:
$X = 20000\ \mathrm{nT}$, $Y = 1500\ \mathrm{nT}$, $Z = 42000\ \mathrm{nT}$.

$$H = \sqrt{20000^2 + 1500^2} = \sqrt{4.0225\times10^{8}}
= 20056.171\ \mathrm{nT},$$
$$F = \sqrt{20056.171^2 + 42000^2} = \sqrt{2.16625\times10^{9}}
= 46542.991\ \mathrm{nT},$$
$$D = \arctan\!\left(\frac{1500}{20000}\right) = \arctan(0.0750)
= 4.2892^{\circ}\ \text{(east)},$$
$$I = \arctan\!\left(\frac{42000}{20056.171}\right) = \arctan(2.09412)
= 64.4742^{\circ}\ \text{(down)}.$$

Checks that the demonstration prints: $H^2+Z^2 = 2166250000.0\
\mathrm{nT^2} = F^2$ exactly, and $X^2+Y^2+Z^2$ gives the same value. The
round trip through $(H,D,I)$ returns the components to within
$1.5\times10^{-11}\ \mathrm{nT}$, which is double-precision round-off, not
physics.

### 1.3 Worked example — elements to components

Invert the same relations: $X = H\cos D$, $Y = H\sin D$, $Z = H\tan I$. With
$H = 20000\ \mathrm{nT}$, $D = 30^{\circ}$, $I = 60^{\circ}$:

$$X = 20000\cos 30^{\circ} = 17320.508\ \mathrm{nT}, \quad
Y = 20000\sin 30^{\circ} = 10000.000\ \mathrm{nT},$$
$$Z = 20000\tan 60^{\circ} = 34641.016\ \mathrm{nT}, \quad
F = \frac{20000}{\cos 60^{\circ}} = 40000.000\ \mathrm{nT}.$$

Note the asymmetry that matters in practice: going from $(X,Y,Z)$ to
$(H,D,I,F)$ is **algebraic and lossless**, while going back requires a *choice*
of quadrant for $D$. `arctan` returns one branch; you must supply the other
(see [01-03-03 Inverse Trigonometric Functions and Branch Ambiguity](../../01-mathematics/03-trigonometry/03-inverse-trig.md)).
$\arctan(Y/X)$ cannot distinguish $(X,Y)$ from $(-X,-Y)$, so $D$ and
$D+180^{\circ}$ are both consistent with the same ratio. Use the four-quadrant
form.

## 2. Units, and the $B$ versus $H$ confusion

The field is quoted in nanotesla: $1\ \mathrm{nT} = 10^{-9}\ \mathrm{T}$, an
exact definition of the SI prefix. The historical unit **gamma** is *identical*
to the nanotesla, not merely similar: $1\ \gamma = 1\ \mathrm{nT}$ by
definition, so a table in gammas needs no numerical conversion at all.

The demonstration's synthetic site A gives $F = 46542.991\ \mathrm{nT}
= 4.654299\times10^{-5}\ \mathrm{T} = 46.543\ \mu\mathrm{T}$.

The trap is the third unit. In SI,

$$\mathbf{B} = \mu_0\left(\mathbf{H} + \mathbf{M}\right),
\qquad \mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}},$$

so in free space $B = \mu_0 H$ and the quantity $\mathbf{H}$ has units
$\mathrm{A\,m^{-1}}$. Dividing the synthetic field by $\mu_0$,

$$H_{\text{equiv}} = \frac{46542.991\times10^{-9}}{4\pi\times10^{-7}}
= 37.0377\ \mathrm{A\,m^{-1}},$$

and one ampere per metre corresponds to $\mu_0\times1 = 1256.64\ \mathrm{nT}$.
Because the relation is **linear**, converting a field from nT to $\mathrm{A/m}$
is a scaled division, not a derivative and not a definition; the conversion
factor is a physical constant. Two consequences:

- A susceptibility measurement relates $\mathbf{M}$ to $\mathbf{H}$, so in SI
  $M = \kappa H$ and $\kappa$ is dimensionless. Reporting the same rock in
  $\mathrm{cgs}$ changes $\kappa$ by $4\pi$, which is why the unit must always
  be stated (see
  [05-02-02 Units and Conventions for Gravity, Magnetic and EM Data](../../05-core-geophysics/02-geophysical-fields-and-observables/02-field-measurement-units.md)).
- Because $B = \mu_0 H$ in air, a "50000 nT field" and a
  "39.7887 $\mathrm{A/m}$ field" are the same physical object. A lesson that
  silently swaps them has not made an error in physics, only in bookkeeping —
  but the bookkeeping is what makes the numbers comparable.

### 2.1 Which elements are measured?

This is where the seven scalars stop being interchangeable:

| Instrument | What it returns | Comment |
|---|---|---|
| Total-field magnetometer | $F$ | scalar; no orientation needed |
| Three-axis fluxgate | $X$, $Y$, $Z$ | needs levelling and a heading |
| Declination-and-inclination theodolite | $D$, $I$ | needs a true-north reference |
| Compass (historic) | a bearing, hence $D$ | the oldest scalar |

The pattern is that **scalar instruments are orientation-free and component
instruments are not**. It is also why $F$ survives in the historical record as
the best-measured element, and why a $D$ with an unstated north reference is not
a datum. Modules
[08-02 Magnetic Instruments and Surveys](../02-magnetic-instruments-and-surveys/README.md)
turn this table into hardware.

## 3. Sensitivity: how a component error becomes an angle error

Differentiate the definitions. From $\tan D = Y/X$,

$$\mathrm{d}D = \frac{X\,\mathrm{d}Y - Y\,\mathrm{d}X}{X^2+Y^2}
= \frac{1}{H}\left(\cos D\,\mathrm{d}Y - \sin D\,\mathrm{d}X\right)
\quad\text{(radians)},$$

and for the common case $\mathrm{d}X = 0$,

$$\mathrm{d}D \approx \frac{\mathrm{d}Y}{H}\quad\text{(radians)}.$$

Likewise, from $\tan I = Z/H$,

$$\mathrm{d}I = \frac{H\,\mathrm{d}Z - Z\,\mathrm{d}H}{H^2+Z^2}
= \frac{H\,\mathrm{d}Z - Z\,\mathrm{d}H}{F^2}, \qquad
\mathrm{d}I \approx \frac{H}{F^2}\,\mathrm{d}Z,$$

where the second form sets $\mathrm{d}H = 0$ — the case of an error in the
vertical component alone, which is exactly what a mis-levelled sensor produces.

### 3.1 Worked example — the linearised approximations versus exact numbers

At site A, $H = 20056.171\ \mathrm{nT}$ and $F = 46542.991\ \mathrm{nT}$. The
demonstration compares the exact recomputation with the linearisations:

| perturbation | exact $\mathrm{d}D$ | $\mathrm{d}Y/H$ | exact $\mathrm{d}I$ | $H\,\mathrm{d}Z/F^2$ |
|---|---|---|---|---|
| $1\ \mathrm{nT}$ in $Y$ | $0.00285^{\circ}$ | $0.00286^{\circ}$ | — | — |
| $10\ \mathrm{nT}$ in $Y$ | $0.02849^{\circ}$ | $0.02857^{\circ}$ | — | — |
| $100\ \mathrm{nT}$ in $Y$ | $0.28477^{\circ}$ | $0.28568^{\circ}$ | — | — |
| $1\ \mathrm{nT}$ in $Z$ | — | — | $0.00053^{\circ}$ | $0.00053^{\circ}$ |
| $100\ \mathrm{nT}$ in $Z$ | — | — | $0.05294^{\circ}$ | $0.05305^{\circ}$ |

The linearisation is right to 3 significant figures at $100\ \mathrm{nT}$ and
drifts by about 0.3% at that size; the offending term is the $\tan$ curvature at
$I = 64.5^{\circ}$, which is where $\mathrm{d}^2 I/\mathrm{d}Z^2$ is largest.
Reading $D$ to one arcminute ($0.01667^{\circ}$) at this site requires
$\mathrm{d}Y < 5.834\ \mathrm{nT}$; to one tenth of an arcminute it requires
$\mathrm{d}Y < 0.583\ \mathrm{nT}$.

### 3.2 The same error at other sites

The demonstration repeats the $\mathrm{d}Y = 1\ \mathrm{nT}$ calculation at four
synthetic sites:

| site | $H$ (nT) | $\mathrm{d}D$ (deg) | $\mathrm{d}D$ (arcmin) |
|---|---|---|---|
| A: mid-latitude | 20056.171 | 0.00285 | 0.171 |
| B: dip-equator side | 27115.494 | 0.00210 | 0.126 |
| C: high latitude | 9035.486 | 0.00632 | 0.379 |
| D: near the dip pole | 471.699 | 0.10289 | 6.173 |

A fixed sensor error of one nanotesla is a 0.17-arcminute statement at
mid-latitude and a 6-arcminute statement near the dip pole. **Declination is
ill-conditioned wherever $H$ is small**, and at $H\to0$ it is undefined: the
four-quadrant formula divides by $X$ and the direction of a horizontal vector of
zero length has no meaning. A "declination anomaly" quoted at a site with
$H = 40\ \mathrm{nT}$ is not a measurement of the field direction.

## 4. Assumptions and regime of validity

1. **The field is a vector field and the station is a point.** Everything above
   describes $\mathbf{B}$ at one location. Over a gradient — a strong anomaly, a
   magnetic body, an aircraft's own field — the "site value" is a spatial
   average over the sensor, not a point sample
   (see [08-01-03](03-spherical-harmonic-magnetic.md) for the length scales).
2. **The field is instantaneous.** $X$, $Y$, $Z$ change with time: externally
   driven daily variation and internally driven secular variation both enter the
   numbers (see [08-01-04](04-secular-variation.md)). The elements as computed
   here carry an unstated epoch.
3. **A north reference exists.** $D$ is defined relative to geographic north; a
   gyro or GNSS heading, not the magnetic needle, supplies it. $I$ needs only a
   level reference, which is why it is the more robust of the two angles.
4. **The frame is right-handed and the signs are the stated ones.** A change of
   sign convention ($Z$ up rather than down, $D$ west positive) changes the
   numbers and leaves the physics alone. Mixing conventions is the most common
   arithmetic failure in this subject.
5. **$H \neq 0$.** Section 3.2 quantifies the failure as $H$ shrinks; the
   formula degrades gracefully but the reported uncertainty must grow with it.

## 5. Python demonstration

`code/main_field_description_demo.py` prints, with units:

1. $(X,Y,Z)\to(H,F,D,I)$ for four synthetic sites, with the identity checks
   $H^2+Z^2 = F^2 = X^2+Y^2+Z^2$ and the round trip back to components;
2. the unit conversions nT ↔ T ↔ gamma ↔ A/m with $\mu_0$ stated exactly;
3. the sensitivity table of section 3, exact and linearised;
4. the inclination geometry $\tan I = 2\tan(\text{latitude})$ at synthetic
   latitudes, as a preview of the dipole model of the next lesson;
5. angular-resolution tables and the site-to-site comparison of $\mathrm{d}D$;
6. five standard-normal draws from the seeded generator, so the record of the
   run is reproducible.

Exercises, with worked solutions, are in
[`exercises/01-main-field-description-exercises.md`](./exercises/01-main-field-description-exercises.md)
and
[`exercises/01-main-field-description-solutions.md`](./exercises/01-main-field-description-solutions.md).

## Mastery checkpoint

Without notes:

1. A site has $X = 12500\ \mathrm{nT}$, $Y = -3400\ \mathrm{nT}$,
   $Z = -20500\ \mathrm{nT}$. Compute $H$, $F$, $D$ and $I$, and state the
   hemisphere and rough latitude regime from the sign of $Z$.
2. Convert $F$ to tesla, to gammas, and to the equivalent magnetising field in
   $\mathrm{A/m}$.
3. Estimate $\mathrm{d}D$ for a $2\ \mathrm{nT}$ error in $Y$ using the
   linearisation, and say whether the exact answer is larger or smaller.
4. Explain in one sentence why a total-field magnetometer cannot give you
   declination.
5. State the condition under which $D$ becomes meaningless, and the element that
   still behaves there.

## Common pitfalls

1. **West-positive declination.** Many navigation and some older texts define
   $D$ west-positive; SI-based geophysics is east-positive. Always state it.
2. **$Z$ up.** A sign slip in $Z$ flips the sign of $I$ and moves the apparent
   magnetic equator by $180^{\circ}$.
3. **Treating gamma and nT as different sizes.** They are the same unit; a
   "correction factor" here is a bug.
4. **Converting nT to A/m by dividing by $4\pi\times10^{-7}\times 10^{9}$ and
   dropping a factor of $10^{3}$.** Write the constant out; it is exact.
5. **Quoting $D$ without a north reference or an epoch.** Both are part of the
   datum.
6. **Reporting a declination at a pole.** Where $H$ is small the element is
   ill-conditioned; section 3.2 gives the numbers.

## Related modules

- [08-01-02 The Geocentric Dipole, IGRF and WMM Models](02-dipole-and-igrf.md) —
  where the elements come from as functions of position.
- [08-01-04 Secular Variation, Jerks and Core Dynamics](04-secular-variation.md) —
  the time dependence assumed away in section 4.
- [08-02 Magnetic Instruments and Surveys](../02-magnetic-instruments-and-surveys/README.md) —
  what each instrument returns.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — the parallel
  story for a scalar field, including the same dependence on a reference frame.
- [18-inverse-problems](../../18-inverse-problems/README.md) — non-uniqueness
  as a formal subject.

## Self-assessment checklist

- [ ] I can write down the seven elements and their definitions with units.
- [ ] I can convert in both directions without looking up a formula.
- [ ] I can quote $\mu_0$ exactly and use it to move between nT and A/m.
- [ ] I can linearise $\mathrm{d}D$ and $\mathrm{d}I$ and say when the
      linearisation stops being adequate.
- [ ] I can name the element each instrument type measures.
- [ ] I can state why declination fails near a pole.
