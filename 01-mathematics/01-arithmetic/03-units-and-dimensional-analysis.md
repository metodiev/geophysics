---
id: 01-01-03
title: "Units, SI Conventions and Dimensional Analysis"
level: beginner
prereqs: ["01-01-01", "01-01-02"]
estimated_minutes: 90
tags: [units, si, dimensional-analysis, conventions]
---

# Units, SI Conventions and Dimensional Analysis

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** the seven SI base quantities from derived quantities, and
   state each base unit and symbol.
2. **Convert** between any two unit systems by treating units as algebraic
   factors, and verify the conversion by reasoning about relative magnitude.
3. **Perform** a dimensional analysis of any equation and use it to detect
   algebraic errors, including errors in exponents and in stray constants.
4. **Recognise** the geophysics-specific conventions — mGal, nT, γ, Ω·m, Ma,
   km/s — and convert freely between them and SI.
5. **Identify** dimensionless groups (e.g. Reynolds number, Rayleigh number) and
   explain why they, rather than raw dimensional quantities, govern physical
   behaviour.

## Prerequisites

[01-01 Number Systems, Precision and Scientific Notation](./01-number-systems-and-precision.md)
and [01-02 Orders of Magnitude](./02-orders-of-magnitude.md).

## 1. Intuition: units are physics, not decoration

A number without units is not a physical quantity; it is an arithmetic object.
The statement "the velocity is 6" is meaningless — 6 m/s, 6 km/s, and 6 ft/s
describe geologically different media (slow sediment, fast mantle, and a
leisurely walk).

More useful than that truism is this: **units encode relationships between
physical quantities.** If you know that

$$1\ \mathrm{N} = 1\ \mathrm{kg\,m\,s^{-2}},$$

you know something physical — force is mass times acceleration — before you have
written any equation. Dimensional analysis is the systematic exploitation of
this fact, and it is the single most powerful error-detection tool available to
you. It catches a large fraction of algebra mistakes in one line, for free.

There is a professional reason to care. NASA's Mars Climate Orbiter was lost in
1999 because one team computed thrust in pound-force-seconds and another
expected newton-seconds. A trivial dimensional check would have caught it. In
geophysics, unit errors in gravity corrections, seismic velocity units, and EM
impedances are a recurring source of published erratum.

## 2. Precise definitions

### 2.1 The SI base quantities

Since the 2019 redefinition, each base unit is defined by fixing the numerical
value of a defining constant. There are seven:

| Quantity | SI unit | Symbol | Defining constant (2019) |
|---|---|---|---|
| Time | second | s | caesium-133 hyperfine frequency |
| Length | metre | m | speed of light $c$ |
| Mass | kilogram | kg | Planck constant $h$ |
| Electric current | ampere | A | elementary charge $e$ |
| Thermodynamic temperature | kelvin | K | Boltzmann constant $k_B$ |
| Amount of substance | mole | mol | Avogadro constant $N_A$ |
| Luminous intensity | candela | cd | luminous efficacy $K_{cd}$ |

For geophysics the first six matter routinely; the candela essentially never
appears (it is a photometric unit weighted by human vision and is irrelevant to
instrument physics).

### 2.2 Derived units used constantly

| Quantity | Unit | In base units |
|---|---|---|
| Force | newton (N) | $\mathrm{kg\,m\,s^{-2}}$ |
| Pressure, stress | pascal (Pa) | $\mathrm{kg\,m^{-1}\,s^{-2}}$ |
| Energy | joule (J) | $\mathrm{kg\,m^{2}\,s^{-2}}$ |
| Power | watt (W) | $\mathrm{kg\,m^{2}\,s^{-3}}$ |
| Frequency | hertz (Hz) | $\mathrm{s^{-1}}$ |
| Gravitational acceleration | (no special name) | $\mathrm{m\,s^{-2}}$ |
| Dynamic viscosity | (no special name) | $\mathrm{Pa\,s} = \mathrm{kg\,m^{-1}\,s^{-1}}$ |
| Kinematic viscosity | (no special name) | $\mathrm{m^{2}\,s^{-1}}$ |
| Diffusivity | (no special name) | $\mathrm{m^{2}\,s^{-1}}$ |
| Density | (no special name) | $\mathrm{kg\,m^{-3}}$ |

**Note the coincidence that is not a coincidence.** Kinematic viscosity,
thermal diffusivity, and hydraulic diffusivity all share the unit
$\mathrm{m^{2}\,s^{-1}}$ because they all describe the same physical process —
transport of a quantity by a gradient, down a gradient. That shared unit is why
$\tau \sim L^{2}/\kappa$
([lesson 02](./02-orders-of-magnitude.md), Section 3.3) applies to all three.

## 3. Dimensional analysis

### 3.1 The method

Assign each quantity a **dimension** — the product of base dimensions. Write
dimensions in square brackets:

$$[v] = \mathrm{L\,T^{-1}}, \qquad [\rho] = \mathrm{M\,L^{-3}}, \qquad
[G] = \mathrm{L^{3}\,M^{-1}\,T^{-2}}.$$

The **principle of dimensional homogeneity**: every term in a physically
meaningful equation must have the same dimensions. Addition of quantities with
different dimensions is meaningless; equality between quantities with different
dimensions is false.

### 3.2 Worked error detection: the interior gravity field

A student derives the gravitational acceleration inside a uniform sphere of
density $\rho$ and radius $r$, and writes

$$g = -\frac{4}{3}\pi G \rho\, r^{3} \qquad [\text{suspect}].$$

**Check.**

$$[G][\rho][r^{3}] = (\mathrm{L^{3}M^{-1}T^{-2}})(\mathrm{M\,L^{-3}})(\mathrm{L^{3}})
= \mathrm{L^{3}M^{-1}T^{-2} \cdot M\,L^{-3} \cdot L^{3}}.$$

The $\mathrm{M}$ cancels ($+1 - 1 = 0$). The $\mathrm{T^{-2}}$ remains. For
$\mathrm{L}$: $3 + (-3) + 3 = 3$. So

$$[\text{RHS}] = \mathrm{L^{3}\,T^{-2}} \neq \mathrm{L\,T^{-2}} = [g].$$

**The expression is dimensionally impossible.** The correct result, from Gauss's
law with $M_{\text{enc}} = \tfrac{4}{3}\pi r^{3}\rho$:

$$g(r) = -\frac{4}{3}\pi G \rho\, r,$$

and now $[\text{RHS}] = \mathrm{L^{3}M^{-1}T^{-2}\cdot M\,L^{-3}\cdot L} =
\mathrm{L\,T^{-2}}$. ✓

**The diagnostic value.** The dimensional failure pointed at an incorrect power
of $r$. This is typical: dimensional analysis does not tell you the answer, but
it tells you *what class of error* you have made, which is often enough.

### 3.3 What dimensional analysis cannot catch

Dimensional analysis is blind to **dimensionless** errors. Consider the
half-space cooling solution and suppose a student writes

$$T(z,t) = T_0\,\mathrm{erfc}\!\left(\frac{z}{\sqrt{\kappa t}}\right)
\qquad [\text{wrong}].$$

The argument $z/\sqrt{\kappa t}$ has dimensions
$\mathrm{L} / (\mathrm{L\,T^{-1/2}} \cdot \mathrm{T^{1/2}}) = \mathrm{L}/L = 1$ —
dimensionless, so it passes. But the correct argument is
$z/(2\sqrt{\kappa t})$. **The factor of 2 is invisible to dimensional analysis.**

> **Rule.** Dimensional analysis verifies the *form* of an equation. It never
> verifies the *dimensionless constants*. Those must be checked by derivation or
> by comparison with a known solution.

This is exactly why the diffusion-scaling exercise in
[lesson 02](./02-orders-of-magnitude.md) (★★★9) asked you to measure the
constant numerically: dimensions gave you $\tau \propto L^{2}/\kappa$, and only
computation could give you the $1.099$.

### 3.4 Dimensionless groups govern physics

The most valuable use of dimensional analysis is not error-checking but
**identifying the controlling dimensionless ratios**. Two famous examples:

**Reynolds number** — inertia versus viscous force:

$$\mathrm{Re} = \frac{\rho v L}{\mu} = \frac{vL}{\nu},$$

with $\nu = \mu/\rho$ the kinematic viscosity. Laminar flow for
$\mathrm{Re} \lesssim 2000$ in a pipe; turbulent above. **The behaviour depends
only on this ratio, not on the individual values of $v$, $L$ and $\nu$.** This is
why a 1:100 scale model in a flume can reproduce a river: matching $\mathrm{Re}$
gives dynamic similarity.

**Rayleigh number** — buoyancy versus diffusion, the controlling parameter for
convection:

$$\mathrm{Ra} = \frac{\alpha\,\rho\,g\,\Delta T\,L^{3}}{\kappa\,\eta},$$

with $\alpha$ thermal expansivity, $\Delta T$ temperature contrast across depth
$L$, $\kappa$ thermal diffusivity, and $\eta$ dynamic viscosity. Convection
begins above a critical value $\mathrm{Ra}_c \approx 10^{3}$ for simple
geometries.

**Apply it to the Earth.** Using mantle values
($\alpha \sim 2\times10^{-5}\ \mathrm{K^{-1}}$, $\rho \sim 3300\ \mathrm{kg\,m^{-3}}$,
$\Delta T \sim 10^{3}$ K, $L \sim 3\times10^{6}$ m,
$\kappa \sim 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, $\eta \sim 10^{21}$ Pa·s):

$$\mathrm{Ra} \sim \frac{(2\times10^{-5})(3300)(10)(10^{3})(3\times10^{6})^{3}}
{(10^{-6})(10^{21})}.$$

Numerator: $(2\times10^{-5})(3300) = 6.6\times10^{-2}$; $\times 10 = 0.66$;
$\times 10^{3} = 660$; $\times (3\times10^{6})^3 = 2.7\times10^{19}$ gives
$\approx 1.78\times10^{22}$.
Denominator: $10^{-6} \times 10^{21} = 10^{15}$.

$$\mathrm{Ra} \sim 1.8\times10^{7}.$$

**Interpretation.** The mantle is not marginally convecting — it is
$\sim10^{4}$ times above the critical value. Vigorous, time-dependent,
three-dimensional convection is therefore expected, and that is what
geodynamic models and seismic tomography show. **A dimensional-analysis
calculation has just established that the central process of plate tectonics is
inevitable** — a genuinely important physical conclusion obtained in three
lines. Note, though, that this same ratio is what makes mantle convection
computationally hard: resolving flow from $\mathrm{Ra} \sim 10^{7}$ to
$10^{9}$ requires enormous grids (see
[19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md)).

**Two ratios, two subdisciplines, one method.** This is the payoff of
dimensional reasoning, and it is why it is taught early.

## 4. Worked conversions with verification

### 4.1 The algebraic method

Treat units as algebraic symbols and multiply by ratios equal to one.

**Problem.** A seismic velocity is quoted as 8.1 km/s. Express in m/s and in
cm/yr (a unit useful for comparing to plate velocities).

$$\frac{8.1\ \mathrm{km}}{1\ \mathrm{s}} \times \frac{10^{3}\ \mathrm{m}}{1\ \mathrm{km}}
= 8.1\times10^{3}\ \mathrm{m\,s^{-1}}.$$

For cm/yr:

$$8.1\times10^{3}\ \frac{\mathrm{m}}{\mathrm{s}}
\times \frac{10^{2}\ \mathrm{cm}}{1\ \mathrm{m}}
\times \frac{3.156\times10^{7}\ \mathrm{s}}{1\ \mathrm{yr}}
= 8.1\times10^{3} \times 10^{2} \times 3.156\times10^{7}\ \mathrm{cm\,yr^{-1}}.$$

$$= 2.56\times10^{13}\ \mathrm{cm\,yr^{-1}}.$$

**Sanity check.** A seismic wave at 8 km/s crosses the Earth's radius in
$\sim800$ s. Plate motion at a few cm/yr has a *timescale* of a year per
centimetre. The ratio is $\sim10^{13}$: seismic waves are thirteen orders of
magnitude faster. **The check is the physics, not the arithmetic.**

### 4.2 Magnetic units and the factor of 10⁹

**Problem.** Convert a 500 nT anomaly to tesla, gauss, and gamma.

$$500\ \mathrm{nT} = 500\times10^{-9}\ \mathrm{T} = 5.00\times10^{-7}\ \mathrm{T}.$$

Since $1\ \mathrm{T} = 10^{4}\ \mathrm{G}$:

$$5.00\times10^{-7}\ \mathrm{T} \times 10^{4}\ \frac{\mathrm{G}}{1\ \mathrm{T}}
= 5.00\times10^{-3}\ \mathrm{G} = 5.00\ \mathrm{mG}.$$

Since $1\ \gamma = 1\ \mathrm{nT}$:

$$500\ \mathrm{nT} = 500\ \gamma.$$

**The traps, stated explicitly:**

| Trap | Consequence |
|---|---|
| Confusing gauss and tesla | Factor of $10^{4}$ (1 T = 10⁴ G) |
| Confusing γ and G | $1\ \gamma = 10^{-5}\ \mathrm{G} = 1\ \mathrm{nT}$; a factor of $10^{5}$ |
| Writing "gamma" for "microtesla" | γ is nT, and µT is 1000× larger |

The Earth's surface field is 25 000–65 000 nT = 0.25–0.65 G = 25–65 µT. Knowing
these three ranges is a permanent check on any magnetic calculation. See
[08-02 Magnetic Instruments and Surveys](../../08-geomagnetism-electromagnetism/02-magnetic-instruments-and-surveys/README.md).

### 4.3 The geophysics convention table

Memorise the left column; it is how the field writes these quantities.

| Quantity | Field convention | SI value | Notes |
|---|---|---|---|
| Gravity anomaly | mGal | $10^{-5}\ \mathrm{m\,s^{-2}}$ | 1 Gal = 1 cm/s² |
| Gravity gradient | Eötvös (E) | $10^{-9}\ \mathrm{s^{-2}}$ | 1 E = 10⁻⁹ s⁻², used in gradiometry |
| Magnetic field | nT (gamma) | $10^{-9}\ \mathrm{T}$ | 1 γ = 1 nT exactly |
| Resistivity | Ω·m | $\mathrm{kg\,m^{3}\,s^{-3}\,A^{-2}}$ | not a base combination worth memorising |
| Conductivity | S/m | $\Omega^{-1}\mathrm{m^{-1}}$ | reciprocal of resistivity |
| Seismic velocity | km/s | $10^{3}\ \mathrm{m\,s^{-1}}$ | crust 3–8, mantle 8–14 |
| Density | kg/m³ (or Mg/m³) | $\mathrm{kg\,m^{-3}}$ | 1 Mg/m³ = 1 g/cm³ |
| Geological time | Ma, Ga | $3.156\times10^{13}\ \mathrm{s}$, $3.156\times10^{16}\ \mathrm{s}$ | "Ma" is mega-annum, a *duration* |
| Heat flow | mW/m² | $10^{-3}\ \mathrm{W\,m^{-2}}$ | ~60–90 typical continental |
| Viscosity (mantle) | Pa·s | $\mathrm{kg\,m^{-1}\,s^{-1}}$ | $10^{19}$–$10^{22}$ |

**A precision point that matters in writing.** `Ma` denotes a duration
(mega-annum) in geochronology, while `Ma` in some stratigraphic usage denotes a
point in time before present. The ambiguity is real, it appears in the
literature, and it has caused genuine confusion. **State your convention
explicitly** when a distinction matters. The non-standard but unambiguous
alternatives are `Myr` for duration and `Ma` for time-before-present; use your
venue's style guide.

## 5. Python demonstration

Save as `code/units_and_dimensions.py`. This implements dimensional algebra
directly, so you can check equations mechanically.

```python
"""Dimensional analysis as executable code.

Run:  python3 units_and_dimensions.py
Requires: Python standard library only.

Dimensions are represented as dictionaries mapping base dimension symbols
('M', 'L', 'T', 'I', 'Theta', 'N', 'J') to rational exponents. Arithmetic on
these dictionaries IS dimensional analysis, which makes it mechanical and
therefore reliable.
"""

from __future__ import annotations

from fractions import Fraction

Dim = dict[str, Fraction]

# --- Base dimensions -------------------------------------------------------
BASE = ("M", "L", "T", "I", "Theta", "N", "J")

# --- Named derived dimensions ---------------------------------------------
DIMENSIONLESS: Dim = {}
LENGTH: Dim = {"L": Fraction(1)}
TIME: Dim = {"T": Fraction(1)}
MASS: Dim = {"M": Fraction(1)}
VELOCITY: Dim = {"L": Fraction(1), "T": Fraction(-1)}
ACCELERATION: Dim = {"L": Fraction(1), "T": Fraction(-2)}
DENSITY: Dim = {"M": Fraction(1), "L": Fraction(-3)}
FORCE: Dim = {"M": Fraction(1), "L": Fraction(1), "T": Fraction(-2)}
PRESSURE: Dim = {"M": Fraction(1), "L": Fraction(-1), "T": Fraction(-2)}
DYNAMIC_VISCOSITY: Dim = {"M": Fraction(1), "L": Fraction(-1), "T": Fraction(-1)}
KINEMATIC_VISCOSITY: Dim = {"L": Fraction(2), "T": Fraction(-1)}
# Gravitational constant G: m^3 kg^-1 s^-2
GRAV_CONSTANT: Dim = {"L": Fraction(3), "M": Fraction(-1), "T": Fraction(-2)}


def mul(*dims: Dim) -> Dim:
    """Multiply dimensions (add exponents)."""
    out: Dim = {}
    for d in dims:
        for key, exp in d.items():
            out[key] = out.get(key, Fraction(0)) + exp
    return {k: v for k, v in out.items() if v != 0}


def div(a: Dim, b: Dim) -> Dim:
    """Divide dimensions (subtract exponents)."""
    negated = {k: -v for k, v in b.items()}
    return mul(a, negated)


def power(a: Dim, n: int | Fraction) -> Dim:
    """Raise a dimension to an integer or rational power."""
    n = Fraction(n)
    return {k: v * n for k, v in a.items() if v * n != 0}


def fmt(d: Dim) -> str:
    """Human-readable dimension string."""
    if not d:
        return "dimensionless"
    parts = []
    for key in BASE:
        if key in d:
            exp = d[key]
            parts.append(key if exp == 1 else f"{key}^{exp}")
    return " ".join(parts)


def check(name: str, left: Dim, right: Dim) -> bool:
    ok = left == right
    mark = "OK  " if ok else "FAIL"
    print(f"  [{mark}] {name}")
    if not ok:
        print(f"          left : {fmt(left)}")
        print(f"          right: {fmt(right)}")
    return ok


def main() -> None:
    print("=" * 74)
    print("1. Do the classic formulas balance dimensionally?")
    print("=" * 74)
    results: list[bool] = []

    # g = G M / r^2
    results.append(check(
        "g = G*M/r^2                     (gravity, point mass)",
        div(mul(GRAV_CONSTANT, MASS), power(LENGTH, 2)),
        ACCELERATION,
    ))

    # F = m a
    results.append(check(
        "F = m*a                         (Newton's second law)",
        mul(MASS, ACCELERATION),
        FORCE,
    ))

    # tau = L^2 / kappa  (diffusion)
    results.append(check(
        "tau = L^2/kappa                 (diffusion timescale)",
        div(power(LENGTH, 2), KINEMATIC_VISCOSITY),
        TIME,
    ))

    # The SUSPECT interior-gravity expression: g = (4/3) pi G rho r^3
    results.append(check(
        "g = (4/3)pi*G*rho*r^3           (SUSPECT - should FAIL)",
        mul(GRAV_CONSTANT, DENSITY, power(LENGTH, 3)),
        ACCELERATION,
    ))

    # The corrected expression
    results.append(check(
        "g = (4/3)pi*G*rho*r             (corrected)",
        mul(GRAV_CONSTANT, DENSITY, LENGTH),
        ACCELERATION,
    ))

    # v = sqrt(G M / r)  (circular orbit speed)
    results.append(check(
        "v^2 = G*M/r                     (orbital speed)",
        power(div(mul(GRAV_CONSTANT, MASS), LENGTH), Fraction(1, 2)),
        VELOCITY,
    ))

    print()
    print("=" * 74)
    print("2. Reynolds number and Rayleigh number are dimensionless")
    print("=" * 74)
    # Re = rho * v * L / mu
    re_dim = div(mul(DENSITY, VELOCITY, LENGTH), DYNAMIC_VISCOSITY)
    results.append(check("Re = rho*v*L/mu", re_dim, DIMENSIONLESS))

    # Ra = alpha*rho*g*dT*L^3 / (kappa*eta)
    # alpha : 1/Theta ; dT : Theta  -> they cancel
    alpha_dT = DIMENSIONLESS
    ra_dim = div(
        mul(alpha_dT, DENSITY, ACCELERATION, power(LENGTH, 3)),
        mul(KINEMATIC_VISCOSITY, DYNAMIC_VISCOSITY),
    )
    results.append(check("Ra = alpha*rho*g*dT*L^3/(kappa*eta)", ra_dim, DIMENSIONLESS))

    print()
    print("=" * 74)
    print("3. Unit conversions with magnitude sanity checks")
    print("=" * 74)
    MGAL = 1e-5
    for value, unit in ((15.2, "mGal"), (-3.7, "mGal"), (1.05, "Gal")):
        si = value * MGAL * (100 if unit == "Gal" else 1)
        print(f"  {value:>7} {unit:<4} = {si:>12.4e} m/s^2 = {si * 1e6:>10.2f} um/s^2")

    print()
    print("  500 nT in other units:")
    t = 500e-9
    print(f"     {t:.3e} T")
    print(f"     {t * 1e4:.3e} G   (1 T = 1e4 G)")
    print(f"     {t * 1e9:.1f} gamma (1 gamma = 1 nT)")

    print()
    print("=" * 74)
    print("4. Mantle Rayleigh number (order of magnitude)")
    print("=" * 74)
    alpha = 2e-5      # 1/K
    rho = 3300.0      # kg/m^3
    g = 10.0          # m/s^2
    dT = 1e3          # K
    L = 3e6           # m
    kappa = 1e-6      # m^2/s
    eta = 1e21        # Pa s
    Ra = alpha * rho * g * dT * L ** 3 / (kappa * eta)
    print(f"  Ra = {Ra:.3e}")
    print(f"  critical Ra_c ~ 1e3  ->  Ra/Ra_c = {Ra / 1e3:.3e}")
    print("  Vigorous, time-dependent 3-D convection is expected.")

    print()
    print("=" * 74)
    print(f"SUMMARY: {sum(results)}/{len(results)} dimensional checks passed")
    print("(one intentional failure above is the SUSPECT formula)")
    print("=" * 74)


if __name__ == "__main__":
    main()
```

### What to observe

| Observation | Consequence |
|---|---|
| The SUSPECT formula fails, the corrected one passes | Mechanical error detection, no human judgement needed |
| $\mathrm{Re}$ and $\mathrm{Ra}$ both reduce to dimensionless | The physical behaviour depends only on these ratios |
| $\mathrm{Ra} \sim 10^{7}$, four orders above $\mathrm{Ra}_c$ | Mantle convection is inevitable, not marginal |
| 15.2 mGal → $152\ \mu\mathrm{m\,s^{-2}}$ | Consistent with lesson 01's conversion table |

> **Breaking exercise.** Add a check for the wave equation's dispersion relation
> $\omega = c k$ (angular frequency = speed × wavenumber). You will need to
> define wavenumber $k$ as $\mathrm{L^{-1}}$ and angular frequency $\omega$ as
> $\mathrm{T^{-1}}$. Then add one for $E = \tfrac{1}{2}\rho v^{2}$ (kinetic
> energy density), which should come out as
> $\mathrm{M\,L^{-1}\,T^{-2}}$ — note this is a *pressure*, which is why
> seismic energy density and stress share units.

## 6. Exercises

★★ and ★★★ solutions are in
[`exercises/03-units-and-dimensional-analysis-solutions.md`](./exercises/03-units-and-dimensional-analysis-solutions.md).

### ★ Foundational

**★1.** Express in SI base units: (a) 1 N, (b) 1 Pa, (c) 1 J, (d) 1 W.

**★2.** Convert: (a) 250 mGal to m/s²; (b) 45 000 nT to T; (c) 3.2 g/cm³ to
kg/m³; (d) 65 mW/m² to W/m².

**★3.** Dimensionally check $v = \sqrt{g\lambda/(2\pi)}$ where $\lambda$ is a
wavelength. Does it balance? What physical situation might it describe?

### ★★ Applied

**★★4.** The seismic quality factor is defined as
$Q = 2\pi E_{\text{stored}}/E_{\text{dissipated}}$. Determine whether $Q$ is
dimensionless. Then, given that attenuation is often written
$A = A_0 \exp(-\pi f x / (Q v))$, verify the exponent is dimensionless.

**★★5.** The gravitational potential of a point mass is $V = -GM/r$. Determine
its dimensions. Then verify that $g = -\nabla V$ has the correct dimensions, and
explain why potential ($\mathrm{L^{2}\,T^{-2}}$) is *not* measured in joules per
kilogram by accident.

**★★6.** A magnetotelluric impedance $Z = E/H$ relates electric field
($\mathrm{V\,m^{-1}}$) to magnetic field ($\mathrm{A\,m^{-1}}$). Show that
$[Z] = \mathrm{kg\,m^{2}\,s^{-3}\,A^{-2}}$, and explain why this is identified
with the ohm.

**★★7.** Consider the group $\eta/(\rho g L)$, where $\eta$ is dynamic viscosity,
$\rho$ density, $g$ gravity, and $L$ a length.

(a) Show that this group has the dimensions of **time**, not that it is
dimensionless. *(Caution: a similar-looking group with $L^{2}$ instead of $L$ is
**not** a time — compute both and note the difference. Getting this wrong is
easy and instructive.)*

(b) Identify it as the viscous relaxation timescale for a load of horizontal
width $L$ on a viscous substrate. Evaluate it for mantle viscosity
$\eta = 10^{21}\ \mathrm{Pa\,s}$, $\rho = 3300\ \mathrm{kg\,m^{-3}}$,
$g = 10\ \mathrm{m\,s^{-2}}$, for $L = 1$ km, $L = 100$ km and $L = 2000$ km.

(c) Which of these three timescales is relevant to post-glacial rebound, and
does it match the observed timescale of rebound in Fennoscandia and Laurentia
(which is of order $10^{3}$–$10^{4}$ years)? Explain why the answer depends so
strongly on $L$.

**★★8.** A heat-flow measurement reports $72\ \mathrm{mW\,m^{-2}}$ with a
thermal conductivity of $2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$. Compute the
geothermal gradient in K/km. Then check: does your answer fall in the range of
typical continental gradients from lesson 02's anchor table?

### ★★★ Research-oriented

**★★★9.** Derive the dimensionless groups governing heat transfer in a
convecting fluid — the Rayleigh number and the Nusselt number
($\mathrm{Nu} = $ convective / conductive heat transport) — using the
Buckingham Pi theorem. Then use published scaling relations of the form
$\mathrm{Nu} \propto \mathrm{Ra}^{\beta}$ to estimate the Nusselt number for
the mantle. Report $\beta$ as reported in the literature you consult (values
around 1/3 are commonly quoted, but **check and cite your source rather than
assuming this figure**), state the assumptions, and explain how your estimate
bears on whether mantle heat transport is dominated by conduction or convection.

**★★★10 — Unit forensics.** Three papers report a gravity-gradient quantity.

- Paper A: "a gradient anomaly of 2.4 Eötvös"
- Paper B: "a gradient anomaly of $2.4\times10^{-9}\ \mathrm{s^{-2}}$"
- Paper C: "a gradient of 24 mGal/km"

(a) Determine the dimensions of each of the three units. Show that all three are
**spatial gradients of gravitational acceleration** and therefore share the same
dimensions. (This is the point: they are *not* different kinds of quantity, which
is exactly why confusing them is easy.)

(b) Establish the conversion between mGal/km and Eötvös. How many Eötvös is
1 mGal/km? *(Work it out from first principles: convert mGal to m/s², then divide
by 1000 m.)*

(c) Papers A and B agree. Convert Paper C's value to Eötvös and determine
whether Paper C is consistent with A and B, or whether it represents a
factor-of-100 discrepancy.

(d) Identify the most likely origin of Paper C's value, and write two sentences
a referee would send to its author.

This is a real class of error in exploration geophysics publishing, and
recognising it depends entirely on dimensional reasoning.

## 7. Common mistakes

1. **Adding quantities with different dimensions.** "Adding apples and
   oranges" is not a metaphor; it is an algebra error.
2. **Trusting an equation because it is dimensionally balanced.** Balanced
   dimensions do not fix dimensionless constants (Section 3.3).
3. **Assuming the argument of $\exp$, $\sin$, or $\ln$ is fine.** It must be
   dimensionless. If you see $\exp(-\pi f x/(Qv))$, check it — it should be
   dimensionless, and in Section 5 it is.
4. **Confusing gauss, tesla, gamma, and microtesla.** A $10^{9}$ range of errors
   is available here.
5. **Treating $\mathrm{Ma}$ as unambiguous.** It is not; state your convention.
6. **Forgetting that km/s and m/s differ by 1000.** A velocity model quoted in
   the wrong unit is wrong by three orders of magnitude and will look like
   physically absurd rock.
7. **Using radian and steradian as if they were base units.** They are
   dimensionless ($\mathrm{m/m}$), which is why angular frequency
   $\omega = 2\pi f$ carries the same unit as $f$ — but the factor $2\pi$ still
   matters numerically.

## 8. Real-world applications

- **Instrument specification and cross-checking.** Converting between mGal,
  µm/s², and Eötvös correctly is prerequisite to reading any gravity
  specification sheet.
- **Catching publication errors.** Section 6 exercise ★★★10 describes a real
  class of error; dimensional reasoning is the tool that finds it.
- **Dimensional analysis as a design tool.** Rayleigh number calculations
  determine whether a geothermal reservoir convects, whether a magma chamber
  overturns, and whether a numerical model at a given resolution is physically
  meaningful.
- **Model validation.** When your numerical model's output has the wrong
  dimensions, no amount of tuning will fix it — the error is structural.
- **Legal and contractual work.** Seismic, gravity, and EM deliverables specify
  units; unit disputes are contractual disputes.

## 9. Further reading

- **BIPM (2019). *The International System of Units (SI)* (9th ed.).**
  Level: reference. The authoritative definition, including the 2019
  redefinition of all base units in terms of constants. Essential if you need
  exact definitions rather than conventions.
- **Taylor, J. R. (1997). *An Introduction to Error Analysis* (2nd ed.).
  University Science Books.** Chapter 2 and the dimensional-analysis sections.
  Level: beginner to intermediate. The clearest treatment of why dimensions
  matter and how to use them.
- **Bridgman, P. W. (1922). *Dimensional Analysis*. Yale University Press.**
  Level: intermediate, historical. The classic treatment; the Buckingham Pi
  theorem is derived rigorously.
- **Turcotte, D. L., & Schubert, G. (2014). *Geodynamics* (3rd ed.). Cambridge
  University Press.** Level: advanced undergraduate to graduate. The Rayleigh
  number and mantle convection are treated at length; the scaling analysis is
  the standard reference for geophysicists.
- **Fowler, C. M. R. (2005). *The Solid Earth: An Introduction to Global
  Geophysics* (2nd ed.). Cambridge University Press.** Level: advanced
  undergraduate to graduate. Excellent on why particular dimensionless groups
  appear in solid-Earth problems.
- **IUPAC (2007). *Quantities, Units and Symbols in Physical Chemistry*
  ("Green Book", 3rd ed.). RSC Publishing.** Level: reference. Useful for
  resolving conflicting conventions in the literature.

> Citation note: bibliography only. Verify editions and availability through
> your library; this repository does not host copyrighted text.

## 10. Related lessons

- [01 Number Systems, Precision and Scientific Notation](./01-number-systems-and-precision.md) — the conversion mechanics extended here.
- [02 Orders of Magnitude and Fermi Estimation](./02-orders-of-magnitude.md) — the diffusive scaling whose constant dimensions cannot supply.
- [04 Floating-Point Representation, Round-Off and Catastrophic Cancellation](./04-floating-point.md) — the next source of error after units.
- [26-reference-library Symbols, Units and Conventions](../../26-reference-library/02-symbols-and-units/README.md) — the full symbol and unit handbook.
- [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) — where the Rayleigh number does real work.
