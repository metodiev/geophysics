---
id: 26-02-03
title: "Physical Constants and Earth Parameters with Sources"
level: beginner
prereqs: []
estimated_minutes: 25
tags: [reference, constants, si-units, provenance]
---

# Physical Constants and Earth Parameters with Sources

A reference table with **provenance**. Every value is classified as one of three
kinds, and you must treat the three kinds differently:

| Class | Meaning | May you quote it to all its digits? |
|---|---|---|
| **Exact (defining)** | Fixed by international agreement as part of the SI or a standard datum. Has *zero* uncertainty. | Yes. |
| **Measured** | Determined experimentally; carries a real uncertainty. | Only with its uncertainty. |
| **Nominal / typical** | A representative value for a naturally variable quantity. | **No.** Quote as an order of magnitude or a range. |

> **The cardinal rule for this page.** Never quote a *nominal* value as though it
> were *measured*, and never quote a *measured* value without its uncertainty.
> Doing so is the error this entire curriculum is built to prevent.

## 1. SI defining constants (exact by definition)

Since the 2019 redefinition of the SI, these constants have **exact** numerical
values — they are definitions, not measurements. Every other unit is derived
from them.

| Constant | Symbol | Exact value | Unit |
|---|---|---|---|
| Caesium hyperfine frequency | $\Delta\nu_{\mathrm{Cs}}$ | 9 192 631 770 | Hz |
| Speed of light in vacuum | $c$ | 299 792 458 | m/s |
| Planck constant | $h$ | 6.626 070 15 × 10⁻³⁴ | J·s |
| Elementary charge | $e$ | 1.602 176 634 × 10⁻¹⁹ | C |
| Boltzmann constant | $k_B$ | 1.380 649 × 10⁻²³ | J/K |
| Avogadro constant | $N_A$ | 6.022 140 76 × 10²³ | mol⁻¹ |
| Luminous efficacy | $K_{cd}$ | 683 | lm/W |

**Derived exactly from the above** (so also exact):

| Constant | Symbol | Exact value | Unit |
|---|---|---|---|
| Molar gas constant | $R = N_A k_B$ | 8.314 462 618 153 24… | J mol⁻¹ K⁻¹ |
| Faraday constant | $F = N_A e$ | 96 485.332 12… | C/mol |
| Stefan–Boltzmann constant | $\sigma = 2\pi^5k_B^4/(15h^3c^2)$ | 5.670 374 419… × 10⁻⁸ | W m⁻² K⁻⁴ |
| Standard atmosphere | — | 101 325 | Pa |
| Standard gravity | $g_n$ | 9.806 65 | m/s² |

**Why "exact" is a real claim and not a figure of speech.** Because $c$ is
*defined* as 299 792 458 m/s, the metre is *defined* as the distance light
travels in 1/299 792 458 s. There is no measurement and no uncertainty. If you
report $c$ with an error bar, you have misunderstood the SI.

> Verification note: the exact values above are the SI defining constants and the
> standard-gravity definition. Confirm against the BIPM SI brochure and the
> NIST CODATA pages before quoting them in a publication, since the derived
> constants are shown here rounded to fit a table.

## 2. Measured physical constants

These require measurement and have genuine uncertainty. The dominant source of
value and uncertainty is CODATA, maintained by the Committee on Data for
Science and Technology and published by NIST.

| Constant | Symbol | Value | Relative standard uncertainty | Source |
|---|---|---|---|---|
| Newtonian constant of gravitation | $G$ | 6.674 30(15) × 10⁻¹¹ m³ kg⁻¹ s⁻² | 2.2 × 10⁻⁵ | CODATA |
| Vacuum magnetic permeability | $\mu_0$ | ≈ 1.256 637 062 12 × 10⁻⁶ N A⁻² | ~1.5 × 10⁻¹⁰ | CODATA (measured since 2019) |
| Vacuum electric permittivity | $\varepsilon_0 = 1/(\mu_0c^2)$ | ≈ 8.854 187 8128 × 10⁻¹² F m⁻¹ | ~1.5 × 10⁻¹⁰ | derived from $\mu_0$ |

**Note on $G$ specifically.** $G$ is the **least precisely known** of the
fundamental constants, by a wide margin — its relative uncertainty is about
$2.2\times10^{-5}$, roughly ten orders of magnitude worse than many others. This
is not a measurement failure but a physical fact: gravity is extraordinarily
weak, so the experiment is very hard. **Any geophysical quantity derived from a
measured mass depends on $G$, and inherits this limitation.** This matters in
[07-gravity-geodesy](../../07-gravity-geodesy/README.md) and is worked through in
[01-01-01 exercise ★★★10](../../01-mathematics/01-arithmetic/exercises/01-number-systems-and-precision-solutions.md).

**Note on $\mu_0$ specifically.** Before 2019, $\mu_0$ was exact by definition
($4\pi\times10^{-7}$ N/A²). After the 2019 redefinition it is a **measured**
quantity with a small uncertainty. This is a trap for anyone using pre-2019
formulas: citing $\mu_0 = 4\pi\times10^{-7}$ N/A² as exact is now wrong in
principle, though the difference is far below the precision of any geophysical
measurement.

## 3. Earth parameters

### 3.1 Defining parameters of the WGS 84 ellipsoid

The World Geodetic System 1984 is the standard reference frame for global
positioning. Its ellipsoid parameters are **defining** values of the datum.

| Parameter | Symbol | Value | Class |
|---|---|---|---|
| Semi-major axis (equatorial radius) | $a$ | 6 378 137 m | defining (exact) |
| Inverse flattening | $1/f$ | 298.257 223 563 | defining (exact) |
| Angular velocity of the Earth | $\omega$ | 7.292 115 × 10⁻⁵ rad/s | defining |
| Geocentric gravitational constant | $GM_\oplus$ | 3.986 004 418 × 10¹⁴ m³ s⁻² | defining |
| Derived semi-minor axis | $b = a(1-f)$ | ≈ 6 356 752.3142 m | derived from the above |
| Ellipsoid identifier | — | EPSG:7030 (ellipsoid); EPSG:4326 (coordinate system) | — |

> **Verification required.** These are the widely implemented WGS 84 defining
> parameters, but parameter sets are revised and new realisations appear. Before
> using them in precision geodetic or navigation work, confirm them against the
> current official release in the EPSG registry or the responsible national
> agency. Do not copy them from a secondary source such as this page.

**Why $a$ and $1/f$ are defining rather than measured.** A datum is a *choice*: a
convention that everyone agrees to use so that coordinates are comparable. You
could define a different ellipsoid; the point of WGS 84 is that it is a fixed,
shared definition.

### 3.2 Derived and nominal terrestrial parameters

| Quantity | Value | Class and source |
|---|---|---|
| Earth mass | ≈ 5.972 × 10²⁴ kg | **derived** from $GM_\oplus/G$; uncertainty dominated by $G$ |
| Mean radius | ≈ 6 371 km | **nominal**; the Earth is not a sphere |
| Equatorial radius | 6 378.137 km | from WGS 84 |
| Polar radius | ≈ 6 356.752 km | from WGS 84 |
| Mean density | ≈ 5 514 kg/m³ | **derived** from mass and volume |
| Surface area | ≈ 5.10 × 10¹⁴ m² | **derived** from the mean radius |
| Flattening $f$ | ≈ 1/298.257 | from WGS 84 |
| Age | ≈ 4.54 × 10⁹ yr | **measured**, with uncertainty of order 1%; from radiometric dating of meteorites and terrestrial samples |
| Surface gravity, mean | ≈ 9.81 m/s² | **nominal**; varies with latitude and elevation |
| Standard gravity | 9.806 65 m/s² | **exact** by definition |

**Note on "Earth mass".** You will often see the Earth's mass "known" to many
digits. It is not. What is measured precisely is $GM_\oplus$ (from satellite
orbits). Dividing by $G$ — which has a relative uncertainty of $2.2\times10^{-5}$
— limits the mass to about **5 significant figures**, not the 9 or 10 sometimes
printed. If you need many digits of $GM_\oplus$, use $GM_\oplus$ directly and
never divide by $G$.

### 3.3 Interior structure: characteristic values

The following are **rounded characteristic values from the Preliminary Reference
Earth Model (PREM)** and from seismological practice. Treat them as nominal
anchors, not as exact model output. **Consult the reference model itself for
precise values at specific depths**, and note that later models differ in detail.

| Region | Depth range | $\rho$ (kg/m³) | $v_p$ (km/s) | $v_s$ (km/s) |
|---|---|---|---|---|
| Continental crust | 0–~35 km | 2 600–2 900 | 5.8–6.5 | 3.2–3.7 |
| Oceanic crust | 0–~7 km | 2 800–3 000 | 6.5–7.0 | 3.5–3.8 |
| Uppermost mantle | below Moho | ~3 300 | ~8.1 | ~4.5 |
| Transition zone | 410–660 km | 3 600–4 400 | 9.1–10.3 | 5.0–5.6 |
| Lower mantle | 660–2 891 km | 4 400–5 570 | 10.3–13.7 | 5.6–7.3 |
| Outer core (liquid) | 2 891–5 153 km | 9 900–12 200 | ~8.0–10.3 | 0 (cannot support shear) |
| Inner core (solid) | 5 153–6 371 km | 12 800–13 100 | 11.0–11.3 | 3.5–3.7 |

**Three facts worth reading off this table rather than memorising the numbers:**

1. **Density jumps by a factor of ~2 at the core–mantle boundary** while $v_p$
   *drops*. A discontinuity in different directions for different properties is
   the signature of a change in *composition*, not just in state.
2. **$v_s = 0$ in the outer core.** The outer core cannot transmit shear waves,
   so it is liquid. This is the single most direct seismological evidence for a
   liquid outer core.
3. **The inner core solidifies despite being hotter**, because pressure raises
   the melting temperature faster than the geotherm rises. This is a
   thermodynamic statement, treated in
   [02-05 Thermodynamics](../../02-physics/05-thermodynamics/README.md).

### 3.4 Nominal mantle and crustal properties

These vary by orders of magnitude in nature. **They are order-of-magnitude
anchors only.**

| Quantity | Typical value | Variability |
|---|---|---|
| Mantle dynamic viscosity | ~10²¹ Pa·s | 10¹⁹–10²² Pa·s; strongly temperature-dependent |
| Asthenosphere viscosity | ~10¹⁹–10²⁰ Pa·s | a low-viscosity channel |
| Crustal density | ~2 700 kg/m³ | 2 200–3 000 |
| Mantle density | ~3 300 kg/m³ | 3 300–5 500 with depth |
| Thermal conductivity (crustal rock) | ~2.5 W m⁻¹ K⁻¹ | 1.5–3.5 |
| Thermal diffusivity | ~10⁻⁶ m²/s | 0.5–2 × 10⁻⁶ |
| Hydraulic diffusivity (crust) | 10⁻²–10⁰ m²/s | depends on fracture density and stress |
| Specific heat capacity (rock) | ~800 J kg⁻¹ K⁻¹ | 700–1 000 |
| Crustal geothermal gradient | ~25 K/km | 10–40; higher in extensional regions |
| Continental surface heat flow | ~65 mW/m² | 40–100 |
| Oceanic surface heat flow | ~100 mW/m² | higher near ridges, lower in old crust |
| Crustal radiogenic heat production | ~1 µW/m³ | 0.1–5, depends on U, Th, K content |
| Rock Young's modulus | ~50 GPa | 10–100 |
| Rock Poisson's ratio | ~0.25 | 0.1–0.35 (higher when fluid-saturated and porous) |
| Seismic quality factor $Q$ (crust) | ~100–500 | 20–1000; lower in hot or fractured rock |

**Why the ranges are so wide.** Rock properties depend on porosity, fluid
content, mineralogy, temperature, pressure, and—for permeability and viscosity—
on the connectivity of the pore or dislocation network. **A single "typical"
value is a starting hypothesis for an order-of-magnitude estimate, and nothing
more.** This is why
[05-core-geophysics rock physics](../../05-core-geophysics/04-rock-physics/README.md)
exists as a separate subject.

### 3.5 Geomagnetic parameters

| Quantity | Value | Class |
|---|---|---|
| Surface field intensity | 25 000–65 000 nT | **nominal** range; varies with location |
| Equatorial surface field | ≈ 30 000 nT | **nominal** |
| Polar surface field | ≈ 60 000 nT | **nominal** |
| Axial dipole moment | ≈ 7.8 × 10²² A m² | **nominal**, and *time-varying* |
| Angle of the dipole to the rotation axis | ≈ 10° | **nominal**, and time-varying |

**Important caveat on the dipole moment.** The geomagnetic dipole moment
**changes measurably over decades** — it is currently decreasing, which is
itself a topic of active research. Do not quote it as a fixed constant. To obtain
the present value, evaluate it from the **current** International Geomagnetic
Reference Field (IGRF) Gauss coefficient $g_1^0$; the IGRF is published by the
International Association of Geomagnetism and Aeronomy and distributed through
NOAA's National Centers for Environmental Information. See
[08-01 The Earth's Magnetic Field](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/README.md).

Note that [01-01-02 Orders of Magnitude](../../01-mathematics/01-arithmetic/02-orders-of-magnitude.md)
uses $8.0\times10^{22}$ A m² as a round order-of-magnitude anchor in its
demonstration code. That is deliberate: the demo's purpose is to show that
dimensional reasoning recovers the right *order of magnitude*, so the anchor is
rounded on purpose.

### 3.6 Physical properties of water, air and ice

Useful anchors for hydrogeophysics, oceanography, and climate work.

| Quantity | Value | Class |
|---|---|---|
| Density of fresh water at 4 °C | 1 000 kg/m³ | defining of the old litre; near-exact at that temperature |
| Density of seawater | ~1 025 kg/m³ | nominal; depends on temperature and salinity |
| Density of ice | ~917 kg/m³ | nominal; nearly temperature-independent |
| Density of air (sea level, 15 °C) | ~1.225 kg/m³ | nominal |
| Specific heat of water | 4 186 J kg⁻¹ K⁻¹ | nominal at 20 °C |
| Latent heat of fusion of ice | 3.34 × 10⁵ J/kg | nominal |
| Latent heat of vaporisation of water | 2.26 × 10⁶ J/kg | nominal at 100 °C |
| Speed of sound in water | ~1 480 m/s | nominal at 20 °C, increases with salinity, pressure, temperature |
| Speed of sound in air | ~343 m/s | nominal at 20 °C |
| Thermal conductivity of water | ~0.6 W m⁻¹ K⁻¹ | nominal |
| Thermal conductivity of ice | ~2.2 W m⁻¹ K⁻¹ | nominal |

**Note the ordering that matters physically.** The speed of sound in seawater
(~1 480 m/s) is **more than four times** its speed in air. This is why
airgun-sourced marine seismic surveys are so energy-efficient, and why the
ocean is practically opaque to sound over long ranges only through attenuation,
not through impedance mismatch.

## 4. How to cite a constant properly

A defensible citation looks like this:

> We adopt $G = 6.674\,30(15)\times10^{-11}$ m³ kg⁻¹ s⁻² (CODATA 2018, as
> distributed by NIST).

and **not** like this:

> We adopt $G = 6.67\times10^{-11}$ m³ kg⁻¹ s⁻².

The second form is not wrong, but it discards the uncertainty and hides the
provenance, so a reader cannot tell whether you knew the value or guessed it.

**The general pattern:**

$$\text{value} \pm \text{uncertainty} \quad (\text{determining body, year})$$

## 5. Common mistakes

1. **Quoting a nominal value to many digits.** "Mantle viscosity is
   1.2×10²¹ Pa·s" is false precision; the mantle viscosity varies by orders of
   magnitude.
2. **Dividing $GM$ by $G$ and reporting 9 significant figures of mass.** See
   Section 3.2.
3. **Using $4\pi\times10^{-7}$ for $\mu_0$ and calling it exact.** True before
   2019, false now.
4. **Treating the Earth's dipole moment as constant.** It is changing on
   human timescales.
5. **Quoting $c$ with an uncertainty.** It is exact by definition.
6. **Assuming precession or flattening values are exact** when they are derived
   from mixture of defining and measured parameters.
7. **Copying a constant from a textbook without checking the edition.** Some
   older texts use pre-2019 values with different uncertainties.

## 6. Further reading

- **BIPM (2019). *The International System of Units (SI)* (9th ed.).** The
  authoritative statement of the defining constants and the 2019 redefinition.
  Level: reference. Essential for anyone who must be certain what is exact.
- **NIST, *CODATA Internationally Recommended Values of the Fundamental Physical
  Constants*.** Level: reference. The definitive source for $G$, $\mu_0$ and the
  rest, with full uncertainty budgets and correlation coefficients. Distributed
  at <https://physics.nist.gov/cuu/Constants/>.
- **Dziewonski, A. M., & Anderson, D. L. (1981). Preliminary reference Earth
  model. *Physics of the Earth and Planetary Interiors*, 25(4), 297–356.**
  Level: graduate. The origin of the PREM values in Section 3.3. This is a
  primary research paper, not a summary — read it if you need the actual model.
- **IERS, *IERS Conventions* (current edition).** Level: reference. Earth
  orientation, reference frames, and geodetic parameters. See
  <https://www.iers.org>.
- **EPSG Geodetic Parameter Registry.** Level: reference. Coordinate systems and
  ellipsoid parameters; WGS 84 ellipsoid is EPSG:7030. See
  <https://epsg.org>.
- **IAGA, *International Geomagnetic Reference Field* (current generation).**
  Level: reference. Distributed through NOAA NCEI; the source for the current
  geomagnetic dipole moment.
- **Taylor, J. R. (1997). *An Introduction to Error Analysis* (2nd ed.).**
  Level: beginner to intermediate. For the treatment of measured values and
  uncertainty that this page assumes.

> Citation note: bibliography and verified links only. This repository does not
> host copyrighted tables or text. Confirm editions and current releases through
> the responsible body.

## Related lessons

- [Symbol Handbook: Notation Used Throughout](./01-symbol-handbook.md)
- [Units Handbook, Conversions and Preferred Conventions](./02-units-handbook.md)
- [Dimensional Analysis Quick Reference](./04-dimensional-analysis-reference.md)
- [01-01-01 Number Systems, Precision and Scientific Notation](../../01-mathematics/01-arithmetic/01-number-systems-and-precision.md)
- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)
