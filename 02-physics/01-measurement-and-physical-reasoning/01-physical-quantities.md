---
id: 02-01-01
title: "Physical Quantities, SI Units and Dimensional Homogeneity"
level: beginner
prereqs: ["01-01-01", "01-01-03"]
estimated_minutes: 90
tags: [units, dimensional-analysis, si-units, measurement]
---

# Physical Quantities, SI Units and Dimensional Homogeneity

## Learning objectives

By the end of this lesson you will be able to:

1. **Decompose** any geophysical quantity into a number and a unit, and state
   which of the seven SI base dimensions the unit is built from.
2. **Convert** between the units that geophysics actually uses (mGal, Gal, nT,
   Ω·m, mW m⁻², Ma) and coherent SI, without looking up a conversion factor for
   the last one — because you can derive it.
3. **Represent** a dimension as a vector of exponents and use vector arithmetic
   to decide whether a formula is dimensionally homogeneous, exactly rather
   than approximately.
4. **Derive** the dimensions of compound quantities (permeability, seismic
   moment, surface heat flow) from the equations that define them.
5. **State** what a dimensional check does *not* prove, and give two pairs of
   physically unrelated quantities in this curriculum that share a dimension.

## Prerequisites

- [01-01-01 Number Systems, Precision and Scientific Notation](../../01-mathematics/01-arithmetic/01-number-systems-and-precision.md) —
  scientific notation, and the difference between exact and measured numbers.
- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md) —
  unit conversion by ratio, and the idea of dimensional consistency.

Nothing in this lesson requires calculus. Everything in the rest of the folder
requires this lesson.

## 1. Intuition: a measurement is a number *and* a unit *and* a regime

Write down a velocity as `5.5`. Is that fast? In geophysics the answer depends
entirely on what follows the number:

| Written as | Physical meaning | Where it is the natural unit |
|---|---|---|
| 5.5 km/s | a P-wave in granite | seismology |
| 5.5 mm/yr | a plate velocity — *glacial rebound*, not tectonics | geodesy |
| 5.5 m/s | a river in flood, or a borehole flow | hydrology |
| 5.5 μm/s | a centimetre per half hour — Darcy flow in tight rock | hydrogeophysics |

Four different Earth processes, one bare number. A unit is not decoration on a
measurement; it *is* part of the measurement, and dropping it is the most common
way a geophysical result becomes meaningless. Worse, a unit is also a claim
about *scale*: `5.5 mm/yr` tells a reader that the process is slow, and that
observation will require years of repeat measurement rather than an afternoon in
the field.

There is a second reason units matter more in geophysics than in most physics
courses. The discipline spans 30-plus orders of magnitude of length, time and
mass — from a 1 cm core plug to the 6 371 km of the Earth; from a microsecond
ultrasonic pulse to the 10⁸ years it takes heat to diffuse through the
lithosphere. There is no single human-scale intuition available, so
**dimensional bookkeeping is the only reliable internal error check you have**.
A geophysicist who can check dimensions catches sign errors, missing factors of
$2\pi$, and confused formulas before wasting a field season.

## 2. Precise definitions

### 2.1 Physical quantity

A **physical quantity** is the product of a numerical value and a unit:

$$Q = \{Q\}\,[Q],$$

where $\{Q\}$ is the numerical value in that unit and $[Q]$ is the unit. The
same physical quantity has different numerical values in different units; the
product does not change. This is the entire content of unit conversion:

$$Q = \{Q\}_1[Q]_1 = \{Q\}_2[Q]_2 \quad\Longrightarrow\quad
\{Q\}_2 = \{Q\}_1\,\frac{[Q]_1}{[Q]_2}.$$

### 2.2 The seven SI base units

The SI takes seven quantities as independent. Everything else in this folder is
a product of powers of these.

| Base quantity | Unit | Symbol | Dimension symbol |
|---|---|---|---|
| mass | kilogram | kg | M |
| length | metre | m | L |
| time | second | s | T |
| electric current | ampere | A | I |
| thermodynamic temperature | kelvin | K | $\Theta$ |
| amount of substance | mole | mol | N |
| luminous intensity | candela | cd | J |

Two facts about this table that are easy to miss:

- **The kilogram carries an SI prefix.** It is the base unit of mass although
  the gram is the reference quantity; this is the only such case. Coherent SI
  therefore requires *grams* to be written as $10^{-3}$ kg, not as a "milli-base
  unit".
- **Angle and solid angle are not base quantities.** The radian is a
  dimensionless ratio (arc length over radius), which is why angular frequency
  $\omega$ (rad/s) and frequency $\nu$ (Hz = s⁻¹) have identical dimensions and
  are *not* interchangeable as numbers. Confusing them is a factor-of-$2\pi$
  error, and the dimensions will never catch it.

### 2.3 Coherent derived units used in this folder

| Quantity | Coherent SI unit | In base units |
|---|---|---|
| force | newton, N | kg m s⁻² |
| energy, work, heat | joule, J | kg m² s⁻² |
| power | watt, W | kg m² s⁻³ |
| pressure, stress | pascal, Pa | kg m⁻¹ s⁻² |
| acceleration | m s⁻² | m s⁻² |
| density | kg m⁻³ | kg m⁻³ |
| dynamic viscosity | Pa s | kg m⁻¹ s⁻¹ |
| kinematic viscosity, diffusivity | m² s⁻¹ | m² s⁻¹ |
| surface heat flow | W m⁻² | kg s⁻³ |
| thermal conductivity | W m⁻¹ K⁻¹ | kg m s⁻³ K⁻¹ |
| electric field | V m⁻¹ | kg m s⁻³ A⁻¹ |
| magnetic flux density | tesla, T | kg s⁻² A⁻¹ |
| magnetic field strength | A m⁻¹ | A m⁻¹ |
| magnetic dipole moment | A m² | A m² |
| massic magnetisation | A m² kg⁻¹ | A m² kg⁻¹ |
| electrical resistivity | Ω m | kg m³ s⁻³ A⁻² |
| electrical conductivity | S m⁻¹ | kg⁻¹ m⁻³ s³ A² |
| permittivity | F m⁻¹ | kg⁻¹ m⁻³ s⁴ A² |
| permeability | H m⁻¹ | kg m s⁻² A⁻² |

### 2.4 Dimension is not the same thing as unit

The **dimension** of a quantity is the list of exponents of the base
dimensions. The **unit** is the size of the reference amount used to express it.
Length is a dimension; metre, foot and ångström are units of it. This
distinction is what makes dimensional analysis powerful: it is invariant under
changing units, so it can be checked once and trusted forever.

Formally, write a dimension as a vector

$$[Q] = \mathrm{M}^{\alpha}\mathrm{L}^{\beta}\mathrm{T}^{\gamma}
\mathrm{I}^{\delta}\Theta^{\epsilon}\mathrm{N}^{\zeta}\mathrm{J}^{\eta},$$

and represent it by the exponent tuple $(\alpha,\beta,\gamma,\delta,\epsilon,
\zeta,\eta)$. Then

- a *product* of quantities multiplies their dimension vectors (add exponents),
- a *quotient* subtracts them,
- a *power* $Q^{p}$ multiplies the exponents by $p$,
- a sum $Q_1+Q_2$ is only meaningful when the two vectors are **equal**.

That last rule is the **principle of dimensional homogeneity**: every term in a
physically meaningful equation must have the same dimension, and both sides must
match. It is a theorem about how physical laws are assembled, not a convention.

### 2.5 The units geophysics actually uses

SI coherence is not the same as field practice. These are the legacy units you
will meet, with the exact conversion where the unit is defined:

| Unit | Quantity | Conversion | Status |
|---|---|---|---|
| Gal | acceleration | $1\ \mathrm{Gal} = 10^{-2}\ \mathrm{m\,s^{-2}}$ | exact, defining |
| mGal | acceleration | $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ | exact, derived |
| Eötvös (E) | gravity gradient | $1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}$ | exact, defining |
| gamma (γ) | magnetic flux density | $1\ \gamma = 10^{-9}\ \mathrm{T} = 1\ \mathrm{nT}$ | exact, defining |
| gal/cm³ or g/cm³ | density | $1\ \mathrm{g\,cm^{-3}} = 10^{3}\ \mathrm{kg\,m^{-3}}$ | exact, derived |
| bar | pressure | $1\ \mathrm{bar} = 10^{5}\ \mathrm{Pa}$ | exact, defining |
| atmosphere (atm) | pressure | $1\ \mathrm{atm} = 101\,325\ \mathrm{Pa}$ | exact (standard atmosphere) |
| darcy (D) | permeability | $1\ \mathrm{D} \approx 0.9869\times10^{-12}\ \mathrm{m^2}$ | defined via a flow experiment |
| gal/min (gpm) | volume rate | $1\ \mathrm{gpm} = 6.309\times10^{-5}\ \mathrm{m^3\,s^{-1}}$ | exact, derived |
| Ma, Ga | time | $1\ \mathrm{Ma} = 10^{6}\ \mathrm{yr}$, $1\ \mathrm{Ga} = 10^{9}\ \mathrm{yr}$ | exact, derived |
| ohm m | resistivity | base unit itself | coherent |

> **Note the pattern.** The interesting legacy units are all *decimal powers* of
> SI units. That is why they can be converted in your head: a mGal is
> $10^{-5}\ \mathrm{m\,s^{-2}}$, so a 2 mGal anomaly is
> $2\times10^{-5}\ \mathrm{m\,s^{-2}}$. The unit carries the exponent for you.

The darcy and the gallon-per-minute are the exceptions: they are historical
definitions tied to particular fluids and geometries, so they are *not* decimal
powers of SI units, and the conversion factors must be looked up. That
difference — decimal power versus historical accident — predicts which
conversions you can do in your head and which you must check.

## 3. Step-by-step: dimensional bookkeeping as arithmetic

### 3.1 The homogeneity check, worked

Take the gravitational field of a spherically symmetric body, which you will
meet formally in [02-08-01](../08-potential-theory/01-gravitational-potential.md):

$$g = \frac{GM}{R^{2}}.$$

Check it with the exponent vectors. $G$ has dimension
$\mathrm{m^3\,kg^{-1}\,s^{-2}}$, i.e. $(-1,3,-2,0,0,0,0)$. Then

$$[GM] = (-1,3,-2) + (1,0,0) = (0,3,-2) = \mathrm{L^3T^{-2}},$$

$$[GM/R^2] = (0,3,-2) - 2(0,1,0) = (0,1,-2) = \mathrm{L\,T^{-2}},$$

which is the dimension of acceleration. The formula is homogeneous. Note
that this check says nothing about whether the *exponent* 2 is right — $GM/R$
and $GM/R^3$ are also homogeneous-looking in the sense that they are legitimate
quantities (a potential and a field gradient). Only the physics fixes the
exponent; only the check rejects the impossible.

### 3.2 Deriving the dimension of an unfamiliar quantity

The reliable route is: **find the defining equation, then read off the
dimensions.** Two examples from later in this folder.

**Permeability $k$ (Module 06).** Darcy's law in its differential form is

$$\mathbf{q} = -\frac{k}{\mu}\left(\nabla p - \rho\mathbf{g}\right),$$

where $\mathbf{q}$ is a volumetric flux (dimension $\mathrm{L\,T^{-1}}$),
$\mu$ a dynamic viscosity ($\mathrm{M\,L^{-1}T^{-1}}$) and $\nabla p$ a pressure
gradient ($\mathrm{M\,L^{-2}T^{-2}}$). Therefore

$$[k] = [q]\,\frac{[\mu]}{[\nabla p]}
      = \mathrm{L\,T^{-1}}\cdot\frac{\mathrm{M\,L^{-1}T^{-1}}}
        {\mathrm{M\,L^{-2}T^{-2}}}
      = \mathrm{L^{2}}.$$

**Permeability has the dimension of area.** This is not a coincidence; it is a
statement that the pore network is a geometric object, and it explains why
laboratories express permeability in μm², and why the darcy is within 2% of
$10^{-12}\ \mathrm{m^2}$.

**Seismic moment $M_0$ (Module 06).** From the definition

$$M_0 = \mu A D,$$

with $\mu$ the shear modulus (Pa $=\mathrm{M\,L^{-1}T^{-2}}$), $A$ an area
($\mathrm{L^2}$) and $D$ a slip ($\mathrm{L}$):

$$[M_0] = \mathrm{M\,L^{-3}T^{-2}}\cdot \mathrm{L^2}\cdot \mathrm{L}
        = \mathrm{M\,L^{2}T^{-2}} = \mathrm{J}.$$

So $M_0$ has the dimension of energy. **It is not an energy** — it is the
far-field amplitude scale of a double-couple source, and it would be wrong to
add it to a thermal energy budget. Keep this example: it is the reason the
self-assessment asks you to find a second quantity with the same dimension.

### 3.3 Half-integer exponents are normal

Wave speeds in an elastic solid go as

$$v_p = \sqrt{\frac{K + \tfrac{4}{3}\mu}{\rho}},$$

so the dimension of $v_p$ involves a square root of
$\mathrm{L^{2}T^{-2}}$, i.e. exponents $(0,1,-1)$ — integer, because elastic
moduli are chosen as $\mathrm{M\,L^{-1}T^{-2}}$ precisely so that this works.
But take the square root of an acceleration and you get
$\mathrm{L^{1/2}\,T^{-1}}$, which has a genuinely half-integer exponent. Such
quantities are legitimate (they appear in similarity laws, e.g. the
dimensionless group $u/\sqrt{gL}$), and they are the reason a dimensional
scheme must use rational exponents rather than integers. The demonstration below
does exactly that.

## 4. Physical interpretation

### 4.1 Why homogeneity is a physical statement

The homogeneity principle holds because physical laws must be usable by observers
who have agreed on arbitrary units. If an equation mixed metres and seconds
additively, its form would change for an observer using feet and minutes, and it
could not be a law of nature. Homogeneity is therefore a *constraint on the form
of physical laws*, discovered by Fourier and formalised by Buckingham (see
[02-01-03](./03-scaling-laws.md)).

### 4.2 What a unit tells you about the measurement

| Unit in a paper | What it implies about the observation |
|---|---|
| mGal ($10^{-8}$ of $g$) | an instrument with a levelled, drift-corrected spring or superconducting sensor |
| nT (1 part in $10^5$ of the Earth's field) | a magnetometer needing diurnal and base-station correction |
| Ω·m | a resistivity survey with geometric soundings, not a laboratory bridge |
| W m⁻² | a heat-flow measurement needing a thermal-conductivity log as well |
| Ma, Ga | dating by radioactive decay, with a closure-temperature caveat |
| Pa s (10²¹) | an inference from glacial rebound, not a laboratory value |

Each unit announces the measurement method and, with it, the assumptions.

### 4.3 Dimensions as a filter for nonsense

Before any physical argument, three questions are free:

1. Do the two sides of the equation have the same dimension?
2. Does each term in a sum match the others?
3. Are the arguments of transcendental functions ($\exp$, $\log$, $\sin$)
   dimensionless?

A "no" to any of these is conclusive. A "yes" to all three proves nothing.

## 5. Units and dimensional analysis: worked numbers

### 5.1 Surface gravity from the two WGS 84 defining parameters

The World Geodetic System 1984 defines, among others (constant handbook,
[26-02-03](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)):

| Parameter | Value | Class |
|---|---|---|
| geocentric gravitational constant $GM_\oplus$ | $3.986\,004\,418\times10^{14}\ \mathrm{m^3\,s^{-2}}$ | defining (exact) |
| semi-major axis $a$ | $6\,378\,137\ \mathrm{m}$ | defining (exact) |
| angular velocity $\omega$ | $7.292\,115\times10^{-5}\ \mathrm{rad\,s^{-1}}$ | defining |
| standard gravity $g_n$ | $9.806\,65\ \mathrm{m\,s^{-2}}$ | exact by definition |

Evaluate $GM_\oplus/a^2$:

$$\frac{3.986\,004\,418\times10^{14}}{(6\,378\,137)^2}
= 9.798\,285\,5\ \mathrm{m\,s^{-2}}.$$

The centrifugal term at the equator is

$$\omega^{2}a = (7.292\,115\times10^{-5})^{2}\times 6\,378\,137
= 0.033\,915\,7\ \mathrm{m\,s^{-2}},$$

so gravitational minus centrifugal is $9.764\,369\,8\ \mathrm{m\,s^{-2}}$ —
about $0.042\,28\ \mathrm{m\,s^{-2}}$ **below** the standard value
$g_n = 9.806\,65$. The centrifugal term supplies $0.0339$ of that $0.0423$; the
remaining $0.0084\ \mathrm{m\,s^{-2}}$ is the free-air effect of the equatorial
bulge: the equator is farther from the centre of mass than the mean radius is.
Evaluating at the nominal mean radius instead,

$$\frac{GM_\oplus}{(6.371\times10^{6})^{2}} = 9.820\,250\,5\ \mathrm{m\,s^{-2}},$$

which is **above** $g_n$ because 6 371 km is smaller than the semi-major axis.
These three numbers ($9.798$, $9.764$, $9.820$) are the reason that a
"surface gravity" without a stated latitude and elevation is an incomplete
statement — a point developed into a full forward model in
[07-gravity-geodesy](../../07-gravity-geodesy/README.md).

> **Check the model, not just the units.** $GM_\oplus/a^2$ assumes a spherical
> Earth of radius $a$ with all the mass at the centre. Both assumptions are
> wrong: the Earth is an oblate ellipsoid and its mass is distributed. The
> formula is still the right first approximation because Newton's shell theorem
> makes the *exterior* field of any spherically symmetric body identical to that
> of a point mass at its centre, and because the flattening is small
> ($f \approx 1/298$). The regime of validity is "outside a nearly spherical
> body"; inside a body, or beside a large mass anomaly, it fails.

### 5.2 Gravity gradients and the Eötvös unit

Differentiate $g = GM/r^{2}$ with respect to $r$ and evaluate at $r = 6\,371$ km:

$$\left|\frac{dg}{dr}\right| = \frac{2GM_\oplus}{r^{3}}
= 3.0828\times10^{-6}\ \mathrm{s^{-2}} = 3082.8\ \mathrm{E}.$$

The same number in survey units is $0.3083\ \mathrm{mGal\,m^{-1}}$: the vertical
gravity gradient is about one third of a mGal per metre, which is why a
gravimeter's elevation must be known to centimetres for a 0.01 mGal survey.
That sentence is a dimensional-analysis result, not a rule of thumb.

### 5.3 Two unit conversions, done by ratio

**(a)** A magnetic anomaly of 500 nT in tesla. Since $1\ \mathrm{nT} =
10^{-9}\ \mathrm{T}$ exactly,

$$500\ \mathrm{nT} = 5\times10^{-7}\ \mathrm{T}.$$

**(b)** A resistivity of 100 Ω·m in SI base units. From the table in §2.3,
$[\Omega\,\mathrm{m}] = \mathrm{kg\,m^3\,s^{-3}\,A^{-2}}$, so

$$100\ \Omega\,\mathrm{m} = 100\ \mathrm{kg\,m^3\,s^{-3}\,A^{-2}}.$$

The number is unchanged because Ω·m is already coherent — a legible reminder
that "SI base units" and "SI units" differ for named derived units.

### 5.4 A dimensional audit of a formula you will meet in Module 04

The P-wave speed in an isotropic elastic solid is
$v_p = \sqrt{(\lambda + 2\mu)/\rho}$. With $\lambda, \mu$ in Pa
($\mathrm{M\,L^{-1}T^{-2}}$) and $\rho$ in $\mathrm{kg\,m^{-3}}$:

$$\left[\frac{\lambda}{\rho}\right]
= \frac{\mathrm{M\,L^{-1}T^{-2}}}{\mathrm{M\,L^{-3}}}
= \mathrm{L^{2}T^{-2}},$$

so $[\sqrt{\lambda/\rho}] = \mathrm{L\,T^{-1}}$: a speed. The elastic moduli and
the density are the *only* quantities that can appear, which is already a
physical statement: **wave speed in a homogeneous elastic solid cannot depend on
frequency.** That is why the dispersion you will observe in real rocks
([02-03-07](../03-oscillations-and-waves/07-dispersion.md)) is
evidence that the material is *not* a perfectly elastic solid.

## 6. Assumptions and regime of validity

1. **Coherent-unit assumption.** Exponent arithmetic as presented assumes a
   coherent system (no stray factors of $10^{3}$ inside formulas). In a
   non-coherent system, $E = mc^{2}$ acquires a numerical factor. Use SI; if you
   must use mGal and nT, convert at the boundary of the calculation, not in the
   middle.
2. **Rational-exponent assumption.** Dimensional arguments treat exponents as
   rational numbers. This is safe for the algebraic laws used here. It is *not*
   a theorem that every legitimate physical quantity has rational exponents;
   $\ln(x)$ of a dimensional quantity is undefined, and quantities such as
   turbulence spectra with fractional exponents are handled by restricting the
   comparison to the argument of a dimensioned reference.
3. **Dimensionless does not mean unimportant.** Strain, Poisson's ratio, $Q$,
   Reynolds number, Rayleigh number and reflection coefficients are all
   dimensionless. A dimensionless quantity cannot be checked by dimensions at
   all — which is why each of them must be shown to be dimensionless *in the
   correct way* (a ratio of like quantities at the same point and time).
4. **Homogeneity is necessary, not sufficient.** $M_0$ and an energy share a
   dimension; so do torque and energy; so do $GM/r$ and $v^{2}/2$. Every such
   pair requires an independent physical argument to keep separate.
5. **Angles are dimensionless, so $\omega$ and $\nu$ look alike.** The radian
   is $\mathrm{m\,m^{-1}}$; cycles are counts. Use $\omega = 2\pi\nu$
   explicitly, and never let a unit check substitute for knowing which one is
   meant.
6. **Nominal values are not constants.** A "typical" mantle density of
   3 300 kg m⁻³ is an order-of-magnitude anchor with a real range
   (3 300–5 500 kg m⁻³ inside the mantle). Its dimension is exact; its value is
   not. See the constant handbook's classification of exact, measured and
   nominal values.

## 7. Python demonstration

The script builds an exact dimensional algebra from integer and rational
exponents, checks derived units against their definitions, checks the
homogeneity of eight formulas used later in this folder, and then fails four
formulas on purpose.

Full listing: [`code/dimensional_analysis_demo.py`](./code/dimensional_analysis_demo.py).

Key excerpt — the algebra is three lines of arithmetic:

```python
def mul(*dims: Dimension) -> Dimension:
    out = [0] * 7
    for d in dims:
        for i in range(7):
            out[i] += d[i]
    return tuple(out)


def div(a: Dimension, b: Dimension) -> Dimension:
    return tuple(a[i] - b[i] for i in range(7))


def root(a: Dimension) -> Dimension:
    """Square root: divides every exponent by two. Odd exponents give halves."""
    return tuple(x / 2 for x in a)
```

Observed output (Python 3.14.4, standard library only):

```text

======================================================================
1. The seven SI base dimensions used in this repository
======================================================================
Dimension vector order: kg, m, s, A, K, mol, cd

======================================================================
2. Derived units are dimension vectors, not names
======================================================================
  newton   N  = m a          -> M^1 L^1 T^-2               match=True
  joule    J  = N m          -> M^1 L^2 T^-2               match=True
  pascal   Pa = N / m^2      -> M^1 L^-1 T^-2              match=True
  watt     W  = J / s        -> M^1 L^2 T^-3               match=True
  volt     V  = W / A        -> M^1 L^2 T^-3 I^-1          match=True
  ohm      Ohm = V / A       -> M^1 L^2 T^-3 I^-2          match=True
  ohm-metre (resistivity)    -> M^1 L^3 T^-3 I^-2          match=True
  tesla    T  = kg s^-2 A^-1 -> M^1 T^-2 I^-1              match=True
  gal      Gal = cm s^-2     -> L^1 T^-2                   match=True

======================================================================
3. Homogeneity of formulas used later in this curriculum
======================================================================
  v = v0 + g t           lhs=L^1 T^-1               rhs=L^1 T^-1               HOMOGENEOUS
  h = v^2 / (2 g)        lhs=L^1                    rhs=L^1                    HOMOGENEOUS
  g = GM / R^2           lhs=L^1 T^-2               rhs=L^1 T^-2               HOMOGENEOUS
  T = 2 pi sqrt(L/g)     lhs=T^1                    rhs=T^1                    HOMOGENEOUS
  v_p = sqrt(K/rho)      lhs=L^1 T^-1               rhs=L^1 T^-1               HOMOGENEOUS
  sigma = F / A          lhs=M^1 L^-1 T^-2          rhs=M^1 L^-1 T^-2          HOMOGENEOUS
  q = k dT/dz            lhs=M^1 T^-3               rhs=M^1 T^-3               HOMOGENEOUS
  omega = sqrt(g/L)      lhs=T^-1                   rhs=T^-1                   HOMOGENEOUS

======================================================================
4. Wrong formulas, caught by dimensions alone
======================================================================
  F = m v          lhs=M^1 L^1 T^-2         rhs=M^1 L^1 T^-1         DIFFERENT -> formula is wrong
  E = m g          lhs=M^1 L^2 T^-2         rhs=M^1 L^1 T^-2         DIFFERENT -> formula is wrong
  p = rho g        lhs=M^1 L^-1 T^-2        rhs=M^1 L^-2 T^-2        DIFFERENT -> formula is wrong
  v = sqrt(2 g)    lhs=L^1 T^-1             rhs=L^1/2 T^-1           DIFFERENT -> formula is wrong

======================================================================
5. g from the WGS 84 defining parameters
======================================================================
  GM / a^2 (gravitational only)  : 9.7982855 m/s^2
  centrifugal term omega^2 a     : 0.0339157 m/s^2
  gravitational minus centrifugal: 9.7643698 m/s^2
  standard gravity g_n           : 9.80665 m/s^2 (exact)
  GM / R^2 at R = 6371 km        : 9.8202505 m/s^2

======================================================================
6. Unit-prefix arithmetic: why geophysicists keep legacy units
======================================================================
  gravity anomaly       2.0 mGal   -> 2.000000e-05 SI
  magnetic anomaly    500.0 nT     -> 5.000000e-07 SI
  resistivity         100.0 ohm m  -> 1.000000e+02 SI
  1 Eotvos unit = 1e-9 s^-2 = 1e-4 mGal/m (a gravity gradient)

======================================================================
7. What a dimensional check cannot do
======================================================================
  SYNTHETIC seismic moment mu A D : 1.5000e+18 (dimension of J)
  Earth rotational energy I w^2/2 : 2.1270e+29 J
  Identical dimensions, different physics.

======================================================================
8. Order of magnitude of the two anomalies in Section 6
======================================================================
  gravity: 1e9 kg at 300 m depth -> 0.0742 mGal (point mass)
  A 0.074 mGal signal is at the edge of a modern relative
  gravimeter's repeatability; the survey must justify it.
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| `ohm-metre -> M^1 L^3 T^-3 I^-2` matches `kg m^3 s^-3 A^-2` | resistivity's dimension is not "Ω·m by definition"; it is forced by V/A·m |
| `q = k dT/dz` comes out `M^1 T^-3` | surface heat flow is W m⁻², whose base form has no length or kelvin left |
| `v = sqrt(2 g)` is reported `L^1/2 T^-1` vs `L^1 T^-1` | the square root of an acceleration is a legitimate quantity with a half-integer exponent |
| `M0 = mu A D` and `I w^2/2` both print `M^1 L^2 T^-2` | dimensional agreement is necessary, never sufficient |
| $GM/a^{2} = 9.798\,285\,5$ and $g_n = 9.806\,65$ differ by 0.043 m s⁻² | the two numbers are different *quantities*: one is the gravitational attraction at the equator, the other a defined reference |

> **Breaking exercise.** Add the formula $E = \tfrac12 \rho v^{2}$ (kinetic
> energy per unit volume) to the list of checks and predict its dimension before
> running. It should come out as a pressure. Then try $E = \tfrac12 \rho v$
> and watch the check reject it.

## 8. Common mistakes

1. **Dropping the unit to save space.** "The velocity is 5.5" is not a
   measurement. In an inversion result this omission can hide a factor of 10³.
2. **Treating the prefix as decoration.** `500 nT` and `500 T` differ by twelve
   orders of magnitude; `1 mGal` and `1 Gal` by one hundred.
3. **Adding unlike quantities.** `g + g_z` where $g$ is total field and $g_z$ an
   anomaly is legal only because both are accelerations; adding a *potential*
   (m² s⁻²) to a *field* (m s⁻²) is a dimension error, not a units slip.
4. **Assuming homogeneity implies correctness.** The seismic moment example:
   $M_0$ and $J$ share a dimension and mean different things.
5. **Forgetting the $4\pi$ is dimensionless and therefore invisible.** Gravity
   is full of dimensionless factors ($4\pi G$, $G M/r^{2}$ vs $2GM/r^{3}$) that
   no dimensional check can confirm. Only a known case can.
6. **Using $\mu_0 = 4\pi\times10^{-7}$ N A⁻² as exact.** Since the 2019 SI
   redefinition it is measured, with a relative uncertainty of about
   $1.5\times10^{-10}$ (constant handbook). The numerical difference is
   irrelevant to geophysics; the *claim* is not.
7. **Mixing rad/s and Hz.** Both are s⁻¹ in dimensions. A factor of $2\pi$ is
   about 6.28, which is larger than many geophysically interesting effects.
8. **Quoting a nominal value as exact.** Mantle viscosity "10²¹ Pa·s" is a
   nominal anchor spanning 10¹⁹–10²² Pa·s; its dimension is exact, its value is
   not.

## 9. Real-world applications

1. **Gravimeter specification.** A modern relative gravimeter's repeatability
   (§5.2) demands orthometric heights to centimetres. The 0.308 mGal/m gradient
   turns a survey-statistics question into a levelling-geometry question.
2. **Magnetic survey units.** Because 1 γ = 1 nT exactly, old Russian and
   American literature can be combined without conversion — but only because
   both are decimal powers of the tesla. Survey *gradients* in nT/m are not so
   forgiving.
3. **Darcy's law in the field.** Permeability in m² and hydraulic conductivity in
   m/s differ by $\rho g/\mu \approx 10^{7}$ for water. Reporting one as the
   other is a factor-$10^{7}$ error that a dimensional check catches instantly.
   See [02-06-05](../06-fluid-mechanics/05-porous-media-flow.md).
4. **Heat-flow reporting.** Surface heat flow of 65 mW m⁻² is
   $65\times10^{-3}\ \mathrm{W\,m^{-2}}$; because it depends on a thermal
   conductivity measured at one point, the dimension of the *product* is exact
   while its value carries the full uncertainty of the log.
5. **Instrument manuals.** An instrument that reports counts must state counts
   per mGal or per nT. Without that, a dataset is not interpretable, and no
   amount of downstream processing recovers the unit.
6. **Publishing.** Journals require SI with the legacy unit in parentheses.
   Doing this conversion correctly is the last checkpoint at which an error can
   be caught cheaply.

## 10. Further reading

- **BIPM (2019). *The International System of Units (SI)* (9th ed.).** The
  authoritative statement of the base units, the defining constants and the
  rules for prefixes. Level: reference.
- **NIST, *CODATA Internationally Recommended Values of the Fundamental
  Physical Constants*.** For $G$, $\mu_0$ and the rest — with uncertainties.
  <https://physics.nist.gov/cuu/Constants/> (level: reference).
- **Taylor, J. R. (1997). *An Introduction to Error Analysis* (2nd ed.).**
  Chapters 1–2 cover the number-plus-unit view and the reporting of units that
  this lesson assumes. Level: beginner.
- **Fowler, C. M. R. *The Solid Earth: An Introduction to Global Geophysics*
  (2nd ed.).** Chapter 1 fixes the units and scales of global geophysics; the
  appendix tables are a useful cross-check on the constants used here.
  Level: intermediate.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.).** The front matter tabulates the field units (mGal,
  nT, Ω·m) used by practitioners. Level: intermediate.
- **NIST, *Guide for the Use of the International System of Units (SI)*.** The
  practical rules — including the one about prefixes and the kilogram.
  Level: reference.

> Citation note: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text. This lesson cites
> no external URL beyond the NIST constants page, which is registered in
> [`tools/verified_links.tsv`](../../tools/verified_links.tsv).

## 11. Related lessons

- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](./02-measurement-uncertainty.md) —
  the other half of a measurement: this lesson gives the unit, that one gives
  the error bar.
- [02-01-03 Scaling Laws, Similarity and Dimensional Reasoning](./03-scaling-laws.md) —
  Buckingham's π theorem turns the exponent arithmetic of §2.4 into a machine
  for generating dimensionless groups.
- [02-01-04 Conservation Laws as the Engine of Physical Modelling](./04-conservation-laws.md) —
  where homogeneity is used to guess the form of a conservation equation.
- [02-08-01 Newtonian Gravitational Potential and Field](../08-potential-theory/01-gravitational-potential.md) —
  the full treatment of $g = GM/r^{2}$, including the shell theorem quoted in
  §5.1.
- [26-02-02 Units Handbook, Conversions and Preferred Conventions](../../26-reference-library/02-symbols-and-units/02-units-handbook.md)
  and [26-02-03 Physical Constants and Earth Parameters with Sources](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md) —
  the repository's own unit and constant references.
- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md) —
  the mathematics-course treatment of the same material.

## Exercises

Attempt the graded problems in
[`exercises/01-physical-quantities-exercises.md`](./exercises/01-physical-quantities-exercises.md),
then compare with
[`exercises/01-physical-quantities-solutions.md`](./exercises/01-physical-quantities-solutions.md).
The solutions show a valid route with verified arithmetic, not the only route.

## Self-assessment checklist

- [ ] I can write any quantity from this folder as a number times a unit, and
      name its SI base-unit decomposition. (Section 2.3)
- [ ] I can explain the difference between a dimension and a unit, and give an
      example of a change of unit that leaves the dimension untouched.
      (Section 2.4)
- [ ] I can carry out a homogeneity check on a formula I have never seen, using
      exponent vectors, and say what the check does and does not prove.
      (Sections 3.1, 6.4)
- [ ] I can derive the dimension of permeability and of seismic moment from
      their defining equations. (Section 3.2)
- [ ] I can compute $GM_\oplus/a^{2}$, the centrifugal term, and the difference
      from $g_n$, and explain each of the three numbers physically.
      (Section 5.1)
- [ ] I can convert between mGal, Gal, m s⁻², nT, T, and Ω·m in base units
      without a table. (Sections 2.5, 5.3)
- [ ] I can state two pairs of physically unrelated quantities with the same
      dimension. (Sections 3.2, 6.4)
- [ ] I can explain why a wave speed in a perfectly elastic homogeneous solid
      cannot depend on frequency, from dimensions alone. (Section 5.4)
