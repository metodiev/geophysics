---
id: 05-02-02
title: "Units and Conventions for Gravity, Magnetic and EM Fields"
level: intermediate
prereqs: ["05-02-01"]
tags: [units, conventions, mGal, nanotesla, ohm-metre, sign-convention]
---

# Units and Conventions for Gravity, Magnetic and EM Fields

## Learning objectives

1. **Derive**, rather than recall, every conversion factor used in gravity,
   magnetic and electrical surveying.
2. **State** the sign and coordinate conventions that each method uses, and
   explain why conventions are a source of real errors.
3. **Convert** among SI and field units without a look-up table.
4. **Explain** why some quantities are reported as differences, ratios or
   dimensionless numbers.
5. **Check** an unfamiliar quantity for dimensional consistency before using it.

## Prerequisites

- [05-02-01 Scalar and Vector Fields](./01-scalar-vs-vector-fields.md)
- [01-01-03 Units and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)

## 1. Intuition

Field units are not sloppy SI; they are historical units sized to the physics.
Anomalies are small fractions of a large background, so units were chosen so
that the anomalies are order-1 numbers. Learning to derive the conversions
rather than memorising them is the difference between a practitioner who can
find an error and one who cannot.

## 2. Derived conversion table

**Gravity.** $1\ \mathrm{Gal} := 1\ \mathrm{cm\,s^{-2}} = 10^{-2}\ \mathrm{m\,s^{-2}}$,
so $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$. Also
$1\ \mathrm{\mu m\,s^{-2}} = 0.1\ \mathrm{mGal}$.

**Magnetics.** $1\ \gamma := 1\ \mathrm{nT} = 10^{-9}\ \mathrm{T}$. The SI unit
of $\mathbf{B}$ is the tesla; of the magnetic moment, A·m²; of magnetisation,
A/m; of susceptibility, dimensionless (SI) or dimensionless per unit volume
(cgs, differing by $4\pi$ — a classic trap).

**Electrical.** Resistivity $\rho_e$ in Ω·m; conductivity
$\sigma = 1/\rho_e$ in S/m. Field practice reports apparent resistivity from a
geometric factor, so the *unit* is Ω·m but the quantity is a computed
equivalent, not a measured resistivity.

**Density.** $1\ \mathrm{g\,cm^{-3}} = 10^{3}\ \mathrm{kg\,m^{-3}}$.

## 3. Derivations you should be able to reproduce

### 3.1 Magnetic field of a dipole in field units

$$\mathbf{B} = \frac{\mu_0}{4\pi}\frac{3(\mathbf{m}\cdot\hat{\mathbf{r}})
\hat{\mathbf{r}}-\mathbf{m}}{r^3}.$$

With $[\mathbf{m}] = \mathrm{A\,m^2}$, $[\mu_0] = \mathrm{H\,m^{-1}}$, the
combination $\mu_0|\mathbf{m}|/(4\pi r^3)$ has units
$\mathrm{H\,m^{-1}\cdot A\,m^2/m^3} = \mathrm{H\,A\,m^{-2}} = \mathrm{T}$. ✓
Practical form: a moment of $1\ \mathrm{A\,m^2}$ at 100 m gives
$\mu_0/(4\pi)\cdot 1/10^{6}\cdot(2\ \text{for the axial factor})
\approx 2\times10^{-13}\ \mathrm{T} = 2\times10^{-4}\ \mathrm{nT}$. Small
moments are measurable because magnetometers resolve ~1 nT.

### 3.2 Why $\Delta T$ is not $|\mathbf{B}|$

Let $\mathbf{B}_0$ be the main field and $\mathbf{B}_a$ the anomaly. Then

$$|\mathbf{B}_0+\mathbf{B}_a| = \sqrt{B_0^2 + 2\mathbf{B}_0\cdot\mathbf{B}_a +
B_a^2} \approx B_0\left(1 + \frac{\mathbf{B}_0\cdot\mathbf{B}_a}{B_0^2}\right)
\implies \Delta T \approx \hat{\mathbf{b}}_0\cdot\mathbf{B}_a.$$

The approximation is first order in $B_a/B_0$; it fails when the anomaly exceeds
a few percent of the main field, which happens in iron-rich terrain.

### 3.3 Why EM uses ratios

In EM the source strength and coupling are poorly known, so the primary field is
measured and removed, and results are reported as ratios (e.g. apparent
resistivity from a ratio of receiver to transmitter field, or a tipper
$\mathbf{Z}_{zx}/\mathbf{Z}_{xx}$). Ratios are dimensionless; apparent
resistivity re-introduces the Ω·m unit through an explicit formula.

### 3.4 The exact total-field expansion, and the case where the first order vanishes

Section 3.2 linearised. Doing it exactly reveals something the linear form hides.

Let $\mathbf{B}_0$ have magnitude $B_0$ and let the anomaly $\mathbf{B}_a$ have
magnitude $B_a = \varepsilon B_0$, making an angle $\varphi$ with
$\mathbf{B}_0$. Then

$$|\mathbf{B}_0+\mathbf{B}_a| = B_0\sqrt{1 + 2\varepsilon\cos\varphi
+ \varepsilon^2},$$

so

$$\Delta T = B_0\left[\varepsilon\cos\varphi
+ \frac{\varepsilon^2\sin^2\varphi}{2} + O(\varepsilon^3)\right].$$

Three cases follow, and they are not degenerate special cases — they are the
normal situations:

| geometry | exact $\Delta T$ | first-order $B_a\cos\varphi$ |
|---|---|---|
| anomaly **parallel** to $\mathbf{B}_0$ ($\varphi = 0$) | $B_0\varepsilon = B_a$ (exact to all orders) | $B_a$ — exact |
| at 45° | $B_0[\varepsilon/\sqrt2 + \varepsilon^2/4 + \ldots]$ | $0.7071\,B_a$ |
| anomaly **perpendicular** to $\mathbf{B}_0$ ($\varphi = 90°$) | $B_0\varepsilon^2/2$ | $0$ — **wrong at every order** |

**Measured check** (with $B_0 = 50\,000$ nT):

| $\varepsilon$ | $\varphi$ | exact $\Delta T$ (nT) | first-order (nT) | second-order term (nT) |
|---|---|---|---|---|
| 0.01 | 0° | 500.000000 | 500.000000 | 0.000000 |
| 0.01 | 45° | 354.794599 | 353.553391 | 1.250000 |
| 0.01 | 90° | 2.499938 | 0.000000 | 2.500000 |
| 0.05 | 90° | 62.460986 | 0.000000 | 62.500000 |

**The lesson.** For a *parallel* anomaly the linearised formula is exact — which
is why $\Delta T \approx \hat{\mathbf{b}}_0\cdot\mathbf{B}_a$ is used so widely
and works so well for the common case of an induced anomaly along the field. For
a *transverse* anomaly the first-order term is identically zero and the observed
signal is entirely the second-order term $B_0\varepsilon^2/2$. So a 500 nT
transverse anomaly appears as 2.5 nT, and a 2500 nT one (5%) as 62.5 nT. **The
usual advice — "assume linear" — is therefore not a small-error approximation:
in one whole class of geometry it is a factor-of-infinity relative error.**

**Practical rule.** Before applying the linear form, ask what angle the anomaly
makes with the main field. If it is near parallel, use it with confidence. If it
is near perpendicular (a body striking east–west at low magnetic latitude, for
instance), compute the exact expression, or work with the measured components
rather than the total field.

### 3.5 The scalar potential in SI, and the cgs trap derived

**Units of the magnetic scalar potential.** In a current-free region
$\mathbf{B} = -\mu_0\nabla\psi$, so

$$[\nabla\psi] = \left[\frac{B}{\mu_0}\right]
= \frac{\mathrm{T}}{\mathrm{H\,m^{-1}}}
= \frac{\mathrm{kg\,s^{-2}A^{-1}}}{\mathrm{kg\,m\,s^{-2}A^{-2}}}
= \mathrm{A\,m^{-1}},$$

hence $[\psi] = \mathrm{A}$. Not volts, not tesla-metres: **amperes**. The
magnetic scalar potential and the electric scalar potential do not share a unit,
which is a frequent source of confusion when the two appear in the same
expression.

**The cgs factor, derived from the constitutive relation.** Write the
constitutive relation for a magnetic medium in the two systems:

$$\text{SI:}\quad \mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M}_\text{SI}),
\qquad\qquad
\text{cgs (Gaussian):}\quad \mathbf{B} = \mathbf{H} + 4\pi\mathbf{M}_\text{cgs}.$$

Define the volume susceptibility as $\chi = M/H$ in each system. Comparing the
two forms term by term, the magnetisation that appears with a factor $1$ in SI
appears with $4\pi$ in cgs, so the same physical response is described by

$$\chi_\text{SI} = 4\pi\,\chi_\text{cgs}.$$

**Why this produces a factor-of-$12.6$ error.** Suppose an interpreter reads
$\chi = 5\times10^{-3}$ from a table that is in cgs and feeds it to an SI code.
The induced magnetisation in a field $\mathbf{H}$ is

$$\text{SI interpretation:}\quad M = \chi H = 5\times10^{-3}H,$$
$$\text{correct (cgs value converted):}\quad
M = \frac{4\pi\chi_\text{cgs}}{4\pi}H = 1.25\times10^{-3}H .$$

The SI interpretation is larger by exactly $4\pi = 12.566$. Measured for
$B_0 = 50\,000$ nT ($H = B_0/\mu_0 = 39.79$ A/m):

| interpretation | $M$ (A/m) |
|---|---|
| treat 5e-3 as SI | 0.1990 |
| treat 5e-3 as cgs and convert to SI | 0.01583 |

The ratio is 12.566. Since predicted anomaly amplitude is proportional to $M$,
a body thought to give 100 nT would be predicted at 1257 nT. **Detection
strategy:** if a model's misfit is systematically $\approx 4\pi$ or $\approx
1/4\pi$ across several bodies of different sizes and depths, the cause is a
convention mismatch, not the geology. Check the magnitude range too: SI
susceptibilities of common rocks are typically $\lesssim10^{-2}$ while cgs values
of the same rocks are typically $\lesssim10^{-3}$.

### 3.6 The gravity-gradient unit chain, derived

Gradiometry is increasingly common, and its units are the least familiar in the
subject. They follow from the same definitions.

A gravity gradient is $\partial g/\partial x$ with units
$\mathrm{m\,s^{-2}\,m^{-1}} = \mathrm{s^{-2}}$. The historical unit is the
**Eötvös**:

$$1\ \mathrm{E} \equiv 10^{-9}\ \mathrm{s^{-2}} .$$

**Convert the corrections you already know.** The free-air gradient derived in
[05-02-04](./04-reduction-of-observations.md) is
$-2g/R = -3.0730\times10^{-6}\ \mathrm{s^{-2}} =
-3073\ \mathrm{E}$, and expressed the other way,
$-0.30730$ mGal/m $= -3.0730\times10^{-6}$ s⁻² $= -3073$ E. So:

$$1\ \mathrm{mGal\,m^{-1}} = 10^{-5}\ \mathrm{s^{-2}}
= 1.0\times10^{4}\ \mathrm{E} .$$

**Resolution arithmetic.** A modern borehole or airborne gradiometer resolving
1 E therefore resolves $10^{-4}$ mGal/m — equivalently, over a 10 m station
separation it resolves a gravity *difference* of $10^{-3}$ mGal. Since a relative
gravimeter resolves 0.02 mGal over the same separation, the gradient measurement
is **20 times more sensitive to nearby mass** than the difference of two
station readings, which is exactly why gradiometry is used for void detection,
tunnel location and archaeological prospecting.

**The full chain, so it need not be memorised.**

$$1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}
= 10^{-4}\ \mathrm{mGal\,m^{-1}}
= 10^{-9}\ \mathrm{m\,s^{-2}\,m^{-1}} .$$

Each step is exact arithmetic on the definitions of the Eötvös, the Gal and the
metre. **The unit that carries the exponent is doing the work**: a gradiometer
quoted as "1 E" and one quoted as "$10^{-4}$ mGal/m" are the same instrument, and
confusing them is a factor of $10^{4}$ error.

## 4. Units and dimensional analysis

| Quantity | Field unit | SI | Derivation |
|---|---|---|---|
| gravity anomaly | mGal | $10^{-5}$ m s⁻² | definition of the Gal |
| magnetic anomaly | nT (γ) | $10^{-9}$ T | definition of the gamma |
| magnetic gradient | nT/m | $10^{-9}$ T m⁻¹ | quotient |
| resistivity | Ω·m | Ω·m | base unit |
| conductivity | mS/m | $10^{-3}$ S m⁻¹ | prefix |
| seismic velocity | km/s | $10^{3}$ m s⁻¹ | prefix |
| density | g/cm³ | $10^{3}$ kg m⁻³ | prefix |
| induced polarisation | mV/V | dimensionless ×10⁻³ | ratio |
| MT impedance | — | Ω | $[\mathbf{E}]/[\mathbf{H}] = \mathrm{V\,A^{-1}} = \Omega$ |

## 5. Assumptions and conventions

1. **Signs.** Gravity positive downward (toward the mass) is the common
   exploration convention; potential $\Phi$ is negative, so the negative sign
   in $\mathbf{g} = -\nabla\Phi$ is essential.
2. **Coordinate frames.** Magnetics uses $x$ north, $y$ east, $z$ down in
   geomagnetism, but $z$ *up* in some aeromagnetic conventions. Declination and
   inclination are defined relative to these. Always state the frame.
3. **Susceptibility system.** SI (dimensionless) and cgs (also dimensionless)
   differ by a factor $4\pi$. Mixing them is a factor-of-12.6 error.
4. **The $\Delta T$ approximation** above.
5. **$\mu_0$.** With the 2019 SI, $\mu_0 = 1.25663706212(19)\times10^{-6}$ H/m,
   no longer exactly $4\pi\times10^{-7}$.

### 5.1 Assumptions of this lesson, and their failure modes

| Assumption | Failure | Consequence |
|---|---|---|
| Conversions are exact unit identities | none | they are definitions; only the *measured* digits limit precision |
| $1\ \mathrm{Gal} = 10^{-2}$ m s⁻², $\gamma = 10^{-9}$ T | none | defining conventions |
| $\mu_0 = 4\pi\times10^{-7}$ H/m exactly | post-2019 SI | error in the ninth significant figure — irrelevant here, but state the value used |
| Anomaly is a projection of the field | large anomaly, transverse geometry | Section 3.4: the first-order term can vanish; use the exact form |
| $z$ down in geomagnetism, sometimes $z$ up elsewhere | mixing frames | a sign error in the anomaly, not a magnitude error — and therefore easy to miss |
| SI versus cgs susceptibility | mixing systems | a factor 12.566 in magnetisation, hence in predicted amplitude |

## 6. Worked examples

**6.1** A 2 mGal anomaly is $2\times10^{-5}$ m s⁻² $= 20\ \mathrm{\mu m\,s^{-2}}$
$= 2\times10^{4}$ nm s⁻².

**6.2** A 500 nT anomaly is $5\times10^{-7}$ T. As a fraction of a 50 000 nT main
field it is 1%, so the linearised $\Delta T$ is accurate to about 0.005%.

**6.3** A magnetisation of 5 A/m in a body of volume $10^{6}$ m³ gives a moment
of $5\times10^{6}$ A·m²; from the demo, the anomaly directly above at 100 m is
1000 nT at 90° inclination and 0 nT at 0° inclination.

**6.4** A resistivity of 250 Ω·m is a conductivity of 0.004 S/m = 4 mS/m.

### 6.1 Extended worked example: a units walk-through with magnitudes

**Gravity.** A 2 mGal anomaly:
$2\ \mathrm{mGal}\times10^{-5} = 2\times10^{-5}\ \mathrm{m\,s^{-2}}
= 20\ \mathrm{\mu m\,s^{-2}} = 2\times10^{4}\ \mathrm{nm\,s^{-2}}$.
For comparison, the Earth's mean field is $9.81$ m s⁻²: the anomaly is
$2\times10^{-6}$ of it, i.e. 2 parts per million. **This ratio is why
gravimeters are relative instruments** — measuring a ppm-level change against an
absolute field would demand a stability no field instrument has, so a reference
station and a difference are used instead.

**Magnetics.** A 500 nT anomaly is $5\times10^{-7}$ T. Against a stated main
field of 50 000 nT it is 1.0% of the field. The second-order term in
$|\mathbf{B}_0+\mathbf{B}_a|$ is $\tfrac12B_a^2/B_0
= 0.5(500\times10^{-9})^2/(5\times10^{-5}) = 2.5\times10^{-9}$ T
$= 2.5$ nT. So the linearised $\Delta T$ is in error by about 2.5 nT against a
500 nT anomaly, i.e. 0.5% — acceptable against a 1 nT instrument, but only
because the anomaly is small. At a 5000 nT anomaly (10%) the second-order term
would be 250 nT, and the linearisation would fail outright.

**A dipole in field units.** Moment $5\times10^{6}$ A m² observed at 300 m
axially: $|\mathbf{B}| = \frac{\mu_0}{4\pi}\frac{2m}{r^3}
= \frac{1.2566\times10^{-6}}{4\pi}\cdot\frac{10^{7}}{2.7\times10^{7}}
= 3.7037\times10^{-8}$ T $= 37.04$ nT. Note the geometry: the *axial* factor is
2, the equatorial factor is 1. The demonstration's $18.519$ nT at 300 m due
north corresponds to the transverse component only; the factor-of-two
difference between axial and equatorial is the same factor that appears in
Section 2 of the dipole lesson.

**Resistivity and conductivity.** $250\ \Omega\cdot\mathrm{m}
= 1/250\ \mathrm{S\,m^{-1}} = 4\times10^{-3}$ S/m $= 4$ mS/m. A factor-of-10
resistivity contrast is a factor-of-10 conductivity contrast; there is no
$4\pi$ and no ambiguity here, which is why electrical units are the least
error-prone of the three families.

**The checklist this example implies.** For every reported number: (1) state the
SI value and the field unit; (2) state the ratio to the background, because that
governs whether linearisations are valid; (3) state which unit system and which
sign convention were used; (4) if it is a ratio, say so and do not attach units.

### 6.2 A complete unit audit, worked

Take a single synthetic body and carry it through *every* unit system the module
has introduced, so the chain can be checked end to end. Stated inputs: a point
mass $m = 10^{10}$ kg at 250 m depth, an anomaly of 1.0679 mGal, a magnetisation
of 5 A/m in a volume of $10^{6}$ m³, and a formation conductivity of 4 mS/m.

| step | SI | field unit | conversion applied |
|---|---|---|---|
| mass | $10^{10}$ kg | — | — |
| $g_z$ | $1.0679\times10^{-5}$ m s⁻² | 1.0679 mGal | $/10^{-5}$ |
| $g_z$ gradient | $3.0730\times10^{-6}$ s⁻² | 3073 E | $/10^{-9}$ |
| magnetic moment | $5\times10^{6}$ A m² | — | — |
| $B$ (axial, 300 m) | $3.7037\times10^{-8}$ T | 37.04 nT | $/10^{-9}$ |
| $B$ gradient | — | nT m⁻¹ | $/10^{-9}$ per metre |
| conductivity | $4\times10^{-3}$ S m⁻¹ | 4 mS/m | $\times10^{3}$ |
| resistivity | $250$ Ω m | 250 Ω m | none |
| density (bulk) | $2237.5$ kg m⁻³ | 2.2375 g cm⁻³ | $/10^{3}$ |

**Every conversion in the table is exact arithmetic on a definition.** The only
measured quantities are the four stated inputs; everything else is a unit
restatement. That is the point of the audit: **if a report contains a number whose
conversion is not an exact restatement, that number is a derived quantity and must
carry its derivation, not just its unit.**

**Two checks a reviewer can apply in seconds.**

1. *Order of magnitude.* A mGal-scale gravity anomaly is $10^{-5}$ m s⁻², about
   one part in $10^{6}$ of $g$. A nT-scale magnetic anomaly is $10^{-9}$ T, one
   part in $5\times10^{4}$ of the main field. Any quoted anomaly more than an order
   of magnitude outside these bands deserves a question.
2. *Dimension trace.* Follow one compound unit through: the Bouguer gradient
   $2\pi G\rho$ gives $\mathrm{s^{-2}}$, which divided by $10^{-5}$ gives
   mGal m⁻¹ — the unit the correction is applied in. If the trace does not close,
   the formula is wrong, regardless of the numeric answer.

**The habit this builds.** Units are the cheapest error detector available, and
they cost nothing to apply. A dimensional trace catches coefficient errors,
forgotten factors and wrong exponents; it does not catch a wrong *physical model*
(a point mass used for a tabular body), which is why the assumptions sections
exist. Together they cover the two error classes this module warns about.

## 7. Python demonstration

`code/field_conventions_demo.py` Section 1 derives the mGal and gamma factors
from their definitions and prints a 2 mGal and a 500 nT anomaly in SI; Section 3
prints dipole components, $|\mathbf{B}|$ and $\Delta T$ for three inclinations,
and Section 4 verifies the skin-depth formula numerically.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/02-field-measurement-units-exercises.md`](./exercises/02-field-measurement-units-exercises.md).

**Common mistakes.** (1) Mixing SI and cgs susceptibility. (2) Reporting $\Delta T$
when the anomaly is large. (3) Using $z$ up and $z$ down in the same model.
(4) Writing "resistivity 250 Ω·m" for an apparent resistivity without saying so.
(5) Treating a ratio (IP in mV/V, or a tipper) as having units.

**Applications.** Airborne gradiometry reports nT/m; borehole gravity reports
µGal or mGal and is a direct measure of in-situ density over an interval;
magnetotelluric apparent resistivity is plotted on log Ω·m axes against period.

### 8.1 The three unit failures worth memorising

The audit above is a procedure; these three are the failures it catches most
often, each with its size attached.

| failure | factor | how it appears |
|---|---|---|
| SI susceptibility used where cgs was tabulated | $4\pi = 12.566$ | predicted magnetic anomalies too large by 12.6, or too small by the same |
| $z$-up and $z$-down mixed between model and data | sign only | a whole anomaly inverted; undetectable by magnitude checks |
| mGal read as µGal (or g/cm³ as kg/m³) | $10^{3}$ | a target that is "obviously detectable" and never found |

**The common thread:** each is a *factor*, not a *shape*, so each leaves the
anomaly's form intact and its amplitude wrong. That is why they survive visual
inspection and why they must be caught by arithmetic. **The $\Delta T$
linearisation failure of Section 3.4 is the exception** — it changes the anomaly's
order in the small parameter, and hence its shape and sign, which is exactly why
it is the most instructive of the four.

## 9. Further reading

- **Telford, Geldart & Sheriff (1990).** Chapters 2–3, 6. Level: intermediate.
- **Blakely (1995).** Appendix on unit systems. Level: advanced.
- **BIPM, *The International System of Units* (9th ed., 2019).** Level:
  reference. Defines the tesla, henry and the current value of $\mu_0$.
- **NIST CODATA constants** —
  [physics.nist.gov/cuu/Constants](https://physics.nist.gov/cuu/Constants/).

## 10. Related lessons

- [05-02-01 Scalar and Vector Fields](./01-scalar-vs-vector-fields.md)
- [05-02-04 Reduction of Observations to Anomalies](./04-reduction-of-observations.md)
- [08-03-01 Magnetic Anomaly Basics](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/01-magnetic-anomaly-basics.md)

## Self-assessment checklist

- [ ] I can derive mGal and gamma from their definitions.
- [ ] I can state the coordinate and sign conventions for each field.
- [ ] I can explain the $\Delta T$ approximation and when it fails.
- [ ] I can convert between resistivity and conductivity.
- [ ] I can say which reported quantities are dimensionless ratios.
