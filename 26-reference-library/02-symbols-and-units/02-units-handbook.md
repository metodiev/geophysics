---
id: 26-02-02
title: "Units Handbook, Conversions and Preferred Conventions"
level: beginner
prereqs: []
estimated_minutes: 25
tags: [reference, units, conversions, conventions]
---

# Units Handbook, Conversions and Preferred Conventions

Conversion tables for the units you will actually meet, with the **internal
consistency checks** that let you verify a conversion reasoning rather than
trusting it.

> **How to avoid the error this page exists to prevent.** Do not memorise a
> conversion factor you have not checked once by hand. Every factor below is
> stated with its derivation route so you can re-derive it when memory fails.

## 1. SI prefixes

| Prefix | Symbol | Factor | Power of ten |
|---|---|---|---|
| tera | T | 10¹² | 12 |
| giga | G | 10⁹ | 9 |
| mega | M | 10⁶ | 6 |
| kilo | k | 10³ | 3 |
| hecto | h | 10² | 2 |
| deca | da | 10¹ | 1 |
| — | — | 10⁰ | 0 |
| deci | d | 10⁻¹ | −1 |
| centi | c | 10⁻² | −2 |
| milli | m | 10⁻³ | −3 |
| micro | µ | 10⁻⁶ | −6 |
| nano | n | 10⁻⁹ | −9 |
| pico | p | 10⁻¹² | −12 |
| femto | f | 10⁻¹⁵ | −15 |

**The prefix-trap.** `m` means *milli* as a prefix but *metre* as a unit — the
same symbol for two different roles. This is a genuine hazard in handwriting and
in badly typeset papers. In geophysics the classic case is `mGal` (milliGal,
a unit of acceleration) versus `m Gal`, and `nT` versus `n T`. Write compound
units as a single token (`mGal`, `nT`, `mW`) and keep a space between a number
and its unit.

## 2. Gravity and gravity gradients

The Gal (galileo) is defined as 1 cm/s². Gravity is *never* quoted in SI in
practice; it is quoted in mGal.

| Unit | Symbol | In m/s² | Derivation |
|---|---|---|---|
| galileo | Gal | 10⁻² | by definition: 1 cm/s² |
| milligal | mGal | 10⁻⁵ | 10⁻³ × Gal |
| microgal | µGal | 10⁻⁸ | 10⁻⁶ × Gal |
| Eötvös | E | 10⁻⁹ s⁻² | *gradient* unit, not acceleration |

**Worked conversions (verify each once by hand):**

$$\begin{aligned}
15.2\ \mathrm{mGal} &= 15.2\times10^{-5} = 1.52\times10^{-4}\ \mathrm{m\,s^{-2}} \\
15.2\ \mathrm{mGal} &= 152\ \mu\mathrm{m\,s^{-2}} \\
1.05\ \mathrm{Gal} &= 1.05\times10^{-2}\ \mathrm{m\,s^{-2}} = 1.05\times10^{4}\ \mu\mathrm{m\,s^{-2}} \\
1\ \mathrm{Gal} &= 1000\ \mathrm{mGal}
\end{aligned}$$

> **The Gal/mGal factor-of-1000 trap.** Because 1 Gal $=10^{-2}$ m/s² and
> 1 mGal $=10^{-5}$ m/s², we get $1\ \mathrm{Gal} = 10^{3}\ \mathrm{mGal}$.
> Writing 100 instead of 1000 is an easy and consequential slip — it was caught
> as a real bug in this repository's own demonstration code during development.

### Gravity gradients

A gravity gradient has dimensions of $\mathrm{s^{-2}}$. Three units are in use:

$$1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}, \qquad
1\ \mathrm{mGal\,km^{-1}} = 10\ \mathrm{E} \ \text{(verified)}, \qquad
1\ \mathrm{E} = 0.1\ \mathrm{mGal\,km^{-1}}.$$

**Derivation of $1\ \mathrm{mGal\,km^{-1}} = 10\ \mathrm{E}$.** A gradient of
1 mGal per km is $10^{-5}\ \mathrm{m\,s^{-2}}$ per $10^{3}$ m:

$$\frac{10^{-5}}{10^{3}} = 10^{-8}\ \mathrm{s^{-2}}
= 10 \times 10^{-9}\ \mathrm{s^{-2}} = 10\ \mathrm{E}.$$

**All three units share dimensions.** This is why a value quoted wrongly in one
of them is *invisible* to a dimensional check and must be caught by numerical
comparison. See
[01-01-03 exercise ★★★10](../../01-mathematics/01-arithmetic/exercises/03-units-and-dimensional-analysis-solutions.md)
for the full worked case.

## 3. Magnetic units

| Unit | Symbol | In tesla | Note |
|---|---|---|---|
| tesla | T | 1 | SI unit |
| gauss | G | 10⁻⁴ | CGS unit; 1 T = 10⁴ G |
| nanotesla | nT | 10⁻⁹ | the working unit of geomagnetism |
| gamma | γ | 10⁻⁹ | **identical** to 1 nT |
| microtesla | µT | 10⁻⁶ | 1000 nT |

**Verified conversions:**

$$500\ \mathrm{nT} = 5.00\times10^{-7}\ \mathrm{T} = 5.00\times10^{-3}\ \mathrm{G}
= 500\ \gamma = 0.500\ \mu\mathrm{T}.$$

**Reference ranges (nominal):** Earth's surface field is 25 000–65 000 nT
$= 0.25$–$0.65$ G $= 25$–$65\ \mu$T. Use this as a permanent sanity check — any
magnetic field value for the Earth's surface outside roughly 20 000–70 000 nT is
suspect.

**The three magnetic traps:**

| Trap | Factor |
|---|---|
| G vs T | 10⁴ |
| γ vs G | 10⁵ (since $1\ \gamma = 10^{-9}$ T $=10^{-5}$ G) |
| "gamma" used loosely for µT | 10³ |

## 4. Electrical and electromagnetic units

| Quantity | Unit | Symbol | Notes |
|---|---|---|---|
| Resistivity | ohm-metre | Ω·m | rocks: 10⁻¹ (sulphide) to 10⁴ (dry granite) |
| Conductivity | siemens per metre | S/m | reciprocal of resistivity; seawater ~4 S/m |
| Impedance | ohm | Ω | MT impedance; same dimensions as resistance |
| Electric field | volts per metre | V/m | |
| Magnetic field strength | amperes per metre | A/m | the $\mathbf{H}$ field |
| Magnetic flux density | tesla | T | the $\mathbf{B}$ field |

**One-dimensional resistivity convention.** Resistivity is a tensor in general;
in a layered Earth it is quoted as a scalar per layer and the vertical is
distinguished from the horizontal. MT papers use $\rho_{xy}$ and $\rho_{yx}$ for
the two polarisations.

**Skin depth.** The relation used for survey planning (with $\delta$ in metres,
$\rho$ in Ω·m, $T$ in seconds):

$$\delta \approx 503\sqrt{\rho\,T}.$$

**Verified penetration check.** For $\rho = 100$ Ω·m and $\delta = 10^{4}$ m,
solving gives $T \approx 4$ s — a practical broadband MT period. Because
$\delta \propto \sqrt{T}$, reaching ten times deeper requires a hundred times
longer period. See
[01-01-02 exercise ★★6](../../01-mathematics/01-arithmetic/exercises/02-orders-of-magnitude-solutions.md).

## 5. Density, pressure and stress

| Unit | Symbol | In SI | Notes |
|---|---|---|---|
| kilogram per cubic metre | kg/m³ | 1 | preferred SI form |
| gram per cubic centimetre | g/cm³ | 10³ kg/m³ | numerically equal to Mg/m³ and to t/m³ |
| megagram per cubic metre | Mg/m³ | 10³ kg/m³ | identical to g/cm³ — use to avoid ambiguity |
| pascal | Pa | 1 kg m⁻¹ s⁻² | stress, pressure |
| megapascal | MPa | 10⁶ Pa | rock mechanics |
| gigapascal | GPa | 10⁹ Pa | elastic moduli, deep Earth |
| bar | bar | 10⁵ Pa | not SI; still appears in older literature |
| atmosphere | atm | 101 325 Pa | **exact** by definition |

**Conversions:**

$$3.2\ \mathrm{g\,cm^{-3}} = 3.2\times10^{3}\ \mathrm{kg\,m^{-3}},
\qquad
1\ \mathrm{bar} = 10^{5}\ \mathrm{Pa} = 0.1\ \mathrm{MPa}.$$

**Note the pleasing identity:** $1\ \mathrm{g\,cm^{-3}} = 1000\ \mathrm{kg\,m^{-3}}$,
so numerical density in g/cm³ is exactly one-thousandth of the SI value. Crustal
rock is "2.7" in g/cm³ and 2700 in kg/m³.

## 6. Heat and temperature

| Unit | Symbol | In SI | Notes |
|---|---|---|---|
| watt per square metre | W/m² | 1 | heat flux density |
| milliwatt per square metre | mW/m² | 10⁻³ W/m² | the working unit for heat flow |
| heat flow unit | HFU | 41.84 mW/m² | $= 10^{-6}$ cal cm⁻² s⁻¹; deprecated, still seen |
| watt per metre per kelvin | W m⁻¹ K⁻¹ | 1 | thermal conductivity |
| square metre per second | m²/s | 1 | thermal **diffusivity** — note it is not conductivity |
| kelvin | K | 1 | use K, not °C, in equations |

**Conversions:**

$$65\ \mathrm{mW\,m^{-2}} = 6.5\times10^{-2}\ \mathrm{W\,m^{-2}},
\qquad
1\ \mathrm{HFU} \approx 41.8\ \mathrm{mW\,m^{-2}}.$$

**The conductivity/diffusivity distinction.** They differ by
$\kappa = k/(\rho c_p)$:

$$[\kappa] = \frac{\mathrm{W\,m^{-1}\,K^{-1}}}{\mathrm{kg\,m^{-3}}\cdot\mathrm{J\,kg^{-1}\,K^{-1}}}
= \frac{\mathrm{kg\,m\,s^{-3}\,K^{-1}}}{\mathrm{kg\,m^{-1}\,s^{-2}\,K^{-1}}}
= \mathrm{m^{2}\,s^{-1}}.$$

Conflating conductivity and diffusivity is a common error that produces answers
wrong by a factor of $10^{6}$ for rock. **Check the units every time.**

## 7. Seismic and wave quantities

| Quantity | Typical unit | Notes |
|---|---|---|
| Velocity | km/s | crust 3–8, mantle 8–14 |
| Wavelength | m or km | $\lambda = v/f$ |
| Frequency | Hz | exploration 10–100 Hz; teleseismic 0.01–1 Hz |
| Period | s | $T = 1/f$ |
| Angular frequency | rad/s | $\omega = 2\pi f$ |
| Wavenumber | rad/m or cycles/m | $k = 2\pi/\lambda$ (rad/m) |
| Slowness | s/m or s/km | $p = 1/v$; also ray parameter, s/rad or s/deg |
| Amplitude | m, or dimensionless | displacement, velocity, or acceleration — **state which** |
| Quality factor | dimensionless | never quote with units |

**The $\omega$ versus $f$ trap.** They differ by $2\pi$. Using $\omega$ where $f$
belongs is a factor-of-6.28 error — large enough to look like a discovery. Check
by writing out the dispersion relation $\omega = ck$ and confirming the units
balance.

**Slowness conventions.** In global seismology slowness is often quoted in
s/deg (the ray parameter), in exploration seismology in s/km, and in
teleseismic work in s/rad. These differ by factors involving $\pi/180$ and 1000.
Always state which.

## 8. Geological time

| Unit | Meaning | In SI seconds |
|---|---|---|
| yr | 1 Julian year | $3.156\times10^{7}$ |
| ka | 10³ yr | $3.156\times10^{10}$ |
| Ma | 10⁶ yr | $3.156\times10^{13}$ |
| Ga | 10⁹ yr | $3.156\times10^{16}$ |

**The Ma ambiguity — state your convention.** In geochronology `Ma` normally
denotes a *duration* (mega-annum). In some stratigraphic usage it denotes a *point
in time* before present. The two are different quantities, and the ambiguity has
caused real confusion in the literature.

To be unambiguous, adopt one of these:

- `Ma` for duration, `Ma BP` (or "x Ma ago") for a time in the past; or
- `Myr` for duration, `Ma` for time-before-present (the convention in much of
  the geosciences).

**Whichever you choose, declare it once.** If your venue has a style guide,
follow it.

## 9. Angle, solid angle and angular measurement

| Unit | Symbol | In radians | Notes |
|---|---|---|---|
| radian | rad | 1 | dimensionless: m/m |
| degree | ° | $\pi/180 \approx 1.745\times10^{-2}$ | |
| arcminute | ′ | $\pi/10800$ | |
| arcsecond | ″ | $\pi/648000$ | |
| steradian | sr | 1 | solid angle; also dimensionless |

**Because radians are dimensionless**, angular frequency has the same dimensions
as frequency, and $Q$ is dimensionless. The dimensional check will *not* catch a
$\omega$/$f$ mix-up — only careful attention to the factor $2\pi$ will.

**Geodetic angular distances (nominal, from the mean Earth radius):**

$$1° \text{ of latitude} \approx 111.1\ \mathrm{km}, \qquad
1' \approx 1.852\ \mathrm{km} = 1\ \text{nautical mile}.$$

**Verified:** circumference $2\pi(6.371\times10^{6}) = 4.00\times10^{7}$ m;
divided by 360 gives $1.11\times10^{5}$ m per degree.

## 10. Seismic magnitude and energy

| Quantity | Unit | Notes |
|---|---|---|
| Magnitude $M$ | dimensionless | never quote with units |
| Seismic moment $M_0$ | N·m | energy-equivalent; see the conversion note below |
| Radiated energy $E_s$ | J | empirically calibrated; cite the specific relation |
| Moment magnitude $M_{\mathrm{w}}$ | dimensionless | the modern standard |

**Deriving the moment-magnitude constant — do not just copy it.** The classic
Hanks & Kanamori (1979) form, and the IASPEI-consistent form, is

$$M_{\mathrm{w}} = \tfrac{2}{3}\log_{10}M_0 - 10.7,
\qquad M_0 \text{ in dyn}\cdot\mathrm{cm}.$$

Since $1\ \mathrm{N\,m} = 10^{7}\ \mathrm{dyn\,cm}$, substituting
$M_0[\mathrm{dyn\,cm}] = M_0[\mathrm{N\,m}]\times10^{7}$ gives

$$M_{\mathrm{w}} = \tfrac{2}{3}\log_{10}M_0[\mathrm{N\,m}]
+ \tfrac{2}{3}(7) - 10.7
= \tfrac{2}{3}\log_{10}M_0[\mathrm{N\,m}] - 6.033.$$

**Verified.** So with $M_0$ in N·m the constant is $-\mathbf{6.03}$
(equivalently $M_{\mathrm{w}} = \tfrac{2}{3}[\log_{10}M_0 - 9.05]$).

**Why you will also see $-6.07$.** That value corresponds to using 9.1 rather
than 9.05 inside the bracket, and it appears in a number of sources and
textbooks. It differs by about 0.03 magnitude units — negligible for most
purposes, but **not negligible if you are comparing $M_0$ and $M_{\mathrm{w}}$
at the level of a few percent.** State which form you use.

**On the energy relation.** The coefficients in
$\log_{10}E_s \approx 1.5M + 4.8$ are **empirically calibrated**, and published
calibrations differ. Treat that relation as an estimate good to a factor of a few
in energy, and cite the specific calibration you adopt.

**Calibration check.** For $M_{\mathrm{w}} = 7$, the $-6.03$ form gives
$\log_{10}M_0 = (7 + 6.033)\times1.5 = 19.55$, so $M_0 \approx 3.5\times10^{19}$
N·m (verified), while the $-6.07$ form gives $4.0\times10^{19}$ N·m. Published
$M_0$ values for $M_{\mathrm{w}} \approx 7$ events fall in exactly this range,
which is a useful check that the formula has been applied correctly.

Development in [06-seismology](../../06-seismology/README.md) and
[01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md).

## 11. Common mistakes

1. **The Gal/mGal factor-of-1000 slip.** See Section 2.
2. **Confusing gravity gradients with gravity.** Eötvös and mGal have different
   dimensions; mGal/km and Eötvös have the same dimensions but different size.
3. **Confusing conductivity with diffusivity.** Wrong by ~10⁶ for rock.
4. **Using $\omega$ for $f$.** Wrong by $2\pi$; not caught by dimensional
   checking, because radians are dimensionless.
5. **Quoting magnitude with units.** Magnitude is dimensionless.
6. **Assuming `Ma` is unambiguous.** It is not.
7. **Mixing G, T, γ and µT.** Four units spanning 10⁹ in the same quantity.
8. **Forgetting that $1\ \mathrm{HFU} = 41.84$ mW/m²**, not 41.84 mW/m² with a
   different base — check whether a paper is using cal or W.

## 12. Further reading

- **BIPM (2019). *The International System of Units (SI)* (9th ed.).**
  Level: reference. Prefixes, derived units, and the 2019 redefinition.
- **IUPAC (2007). *Quantities, Units and Symbols in Physical Chemistry*
  ("Green Book", 3rd ed.).** Level: reference. Best available resolver of
  conflicting unit conventions.
- **IAGA, *International Geomagnetic Reference Field* and the geomagnetic
  unit conventions published with it.** Level: reference. Defines nT as the
  working magnetic unit and the $\mathbf{B}$/$\mathbf{H}$ conventions.
- **IASPEI, *Standard Seismological Magnitude and Phase Nomenclature*
  (committee reports).** Level: reference. The authority on magnitude
  definitions and phase naming; consult the current reports.
- **Taylor, J. R. (1997). *An Introduction to Error Analysis* (2nd ed.).**
  Level: beginner to intermediate. Unit analysis in the service of uncertainty.

> Citation note: bibliography only; no copyrighted tables reproduced. Confirm
> current releases through the responsible body.

## Related lessons

- [Symbol Handbook: Notation Used Throughout](./01-symbol-handbook.md)
- [Physical Constants and Earth Parameters with Sources](./03-constant-handbook.md)
- [Dimensional Analysis Quick Reference](./04-dimensional-analysis-reference.md)
- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)
