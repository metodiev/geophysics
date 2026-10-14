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

## 6. Worked examples

**6.1** A 2 mGal anomaly is $2\times10^{-5}$ m s⁻² $= 20\ \mathrm{\mu m\,s^{-2}}$
$= 2\times10^{4}$ nm s⁻².

**6.2** A 500 nT anomaly is $5\times10^{-7}$ T. As a fraction of a 50 000 nT main
field it is 1%, so the linearised $\Delta T$ is accurate to about 0.005%.

**6.3** A magnetisation of 5 A/m in a body of volume $10^{6}$ m³ gives a moment
of $5\times10^{6}$ A·m²; from the demo, the anomaly directly above at 100 m is
1000 nT at 90° inclination and 0 nT at 0° inclination.

**6.4** A resistivity of 250 Ω·m is a conductivity of 0.004 S/m = 4 mS/m.

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

## Extended worked example: a units walk-through with magnitudes

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
