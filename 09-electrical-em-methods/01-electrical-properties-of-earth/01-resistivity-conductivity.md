---
id: 09-01-01
title: "Resistivity and Conductivity: Definitions and Ranges"
level: intermediate
prereqs: ["02-07-01", "01-06-04"]
tags: [electrical-methods, resistivity, conductivity, ohm-law, units]
---

# Resistivity and Conductivity: Definitions and Ranges

Resistivity is the one physical property of the ground that is almost entirely
controlled by what is *in* the pores rather than by what the rock is made of.
That single fact is why electrical methods are the workhorse of near-surface
geophysics, and it is also why they are so easy to over-interpret. This lesson
fixes the definitions, the units, the geometry, and the size of the number
range. Nothing here is difficult; everything here is used in every later lesson
of the folder.

**All models and data in this module are SYNTHETIC.** The catalogue of
resistivities below is a chosen teaching catalogue, not a set of measurements.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** current density, electric field, conductivity and resistivity, and
   convert between $\sigma$ and $\rho$ in SI units.
2. **Derive** the resistance of a conductor of arbitrary shape from
   $\mathbf{J} = \sigma \mathbf{E}$ and state which quantity is a material
   property and which is a geometry.
3. **Derive** the potential of a point current source on a conducting
   half-space, and **verify** by integration that the injected current is
   carried by the field.
4. **State** the resistivity range met in near-surface work and explain why the
   conductivity scale spans six decades.
5. **Compute** the resistance of a hemispherical electrode and explain why the
   contact geometry, not the ground, usually sets it.
6. **Propagate** measurement errors into a conductivity estimate, and identify
   which measurement dominates the error budget.
7. **Explain** why a two-electrode measurement is not a resistivity measurement.

## Prerequisites

- [02-07-01 Electrostatics, Coulomb's Law and Electric Potential](../../02-physics/07-electromagnetism/01-electrostatics.md) —
  the electric field as the gradient of a potential.
- [01-06-04 Divergence, Curl and Physical Meaning](../../01-mathematics/06-multivariable-calculus/04-divergence-and-curl.md) —
  flux and the divergence theorem, used here to carry current across a surface.

## 1. Definitions and units

Ohm's law in a continuum is a *local* statement, not a circuit law:

$$\mathbf{J} = \sigma \mathbf{E}, \qquad \rho = \frac{1}{\sigma},$$

where $\mathbf{J}$ is the current density ($\mathrm{A\,m^{-2}}$),
$\mathbf{E}$ the electric field ($\mathrm{V\,m^{-1}}$), $\sigma$ the
conductivity in siemens per metre ($\mathrm{S\,m^{-1}}$) and $\rho$ the
resistivity in ohm metres ($\Omega\,\mathrm{m}$). Since $\Omega = \mathrm{V/A}$,

$$1\ \Omega\,\mathrm{m} = 1\ \frac{\mathrm{V\,m}}{\mathrm{A}},
\qquad 1\ \mathrm{S\,m^{-1}} = 1\ \Omega^{-1}\mathrm{m^{-1}},$$

so $\rho = 1/\sigma$ is exact and unit-free as a conversion: $100\
\Omega\,\mathrm{m}$ *is* $0.01\ \mathrm{S\,m^{-1}}$.

In a resistor of length $L$ and uniform cross-section $A$ carrying current $I$,
$J = I/A$ and $E = V/L$. Substituting into $\mathbf{J} = \sigma\mathbf{E}$:

$$R = \frac{V}{I} = \frac{\rho L}{A}.$$

That is the whole of the classical law, and it shows the split that runs
through this folder: $\rho$ is a **material** property, while $R$ is a
**geometry** as well. Two samples of the same rock with different shapes have
different resistances and the same resistivity.

*Numerical check (SYNTHETIC)* — the demonstration
`code/resistivity_conductivity_demo.py` uses a core plug of length
$L = 0.100\ \mathrm{m}$ and radius $0.025\ \mathrm{m}$, so
$A = 1.963\times10^{-3}\ \mathrm{m^2}$. For $\rho = 100\ \Omega\,\mathrm{m}$ it
prints $R = 5093.0\ \Omega$; for $\rho = 1000\ \Omega\,\mathrm{m}$,
$R = 50929.6\ \Omega$. Driving $1.0\ \mathrm{mA}$ through the second plug gives
$J = I/A = 0.5093\ \mathrm{A\,m^{-2}}$ and $E = \rho J = 509.2958\
\mathrm{V\,m^{-1}}$, and the printed cross-check $V/L = 509.2958\
\mathrm{V\,m^{-1}}$ agrees with $E$ exactly: a 50.93 V drop over 0.1 m is the
same 509 V/m.

## 2. The point source on a half-space

Everything in DC resistivity rests on one solution. Put current $I$ into the
ground at a point on a flat surface. By symmetry the current spreads evenly over
hemispheres, so at distance $r$ the *total* current crossing a hemisphere of
radius $r$ is $I$:

$$I = \oint \mathbf{J}\cdot\mathrm{d}\mathbf{A}
= J(r)\,2\pi r^{2}.$$

Hence $J(r) = I/(2\pi r^{2})$, $E(r) = \rho I/(2\pi r^{2})$, and integrating
$-E$ radially from infinity gives the potential

$$V(r) = \frac{\rho I}{2\pi r} \qquad (\mathrm{V}).$$

The factor $2\pi$ — not $4\pi$ — is the signature of a **half**-space: the
return path is the surface, and no current goes into the air.

*Numerical check (SYNTHETIC).* With $\rho = 100\ \Omega\,\mathrm{m}$ and
$I = 0.10\ \mathrm{A}$ the demo prints:

| $r$ (m) | 0.5 | 1.0 | 2.0 | 5.0 | 10.0 | 20.0 |
|---|---|---|---|---|---|---|
| $V$ (V) | 3.18310 | 1.59155 | 0.79577 | 0.31831 | 0.15915 | 0.07958 |
| $J$ ($\mathrm{A\,m^{-2}}$) | $6.37\times10^{-2}$ | $1.59\times10^{-2}$ | $3.98\times10^{-3}$ | $6.37\times10^{-4}$ | $1.59\times10^{-4}$ | $3.98\times10^{-5}$ |

The product $V\,2\pi r/(\rho I)$ printed next to each row is $1.000000$ to six
places: the $1/r$ law is what makes a resistivity survey a *measurement of
geometry and resistance together*. The demo also integrates the current density
over the hemisphere numerically with Gauss–Legendre quadrature and prints

$$\int_0^{\pi/2}\sin\theta\,\mathrm{d}\theta = 1.000000000000, \qquad
\oint \mathbf{J}\cdot\mathrm{d}\mathbf{A} = 0.100000000000\ \mathrm{A},$$

i.e. exactly the injected current. This is the check that must pass before the
potential can be used as a forward model.

## 3. The teaching catalogue and its six decades

The demo's catalogue, with conductivity $1/\rho$:

| material (SYNTHETIC teaching value) | $\rho$ ($\Omega\,\mathrm{m}$) | $\sigma$ ($\mathrm{S\,m^{-1}}$) |
|---|---|---|
| connected massive sulphide | $0.1$ | $10$ |
| graphitic schist | $1$ | $1$ |
| saturated clay | $5$ | $0.2$ |
| shale | $20$ | $0.05$ |
| sandstone, brackish water | $30$ | $0.0333$ |
| sandstone, fresh water | $200$ | $5\times10^{-3}$ |
| dry limestone | $5\times10^{3}$ | $2\times10^{-4}$ |
| dry granite | $1\times10^{5}$ | $1\times10^{-5}$ |

The printed span is $10$ to $10^{-5}\ \mathrm{S\,m^{-1}}$, a factor
$10^{6}$ — six decades. Two consequences follow immediately and both are used
later. First, resistivity data are plotted and modelled logarithmically; a
linear colour scale on a resistivity section hides everything. Second, a
resistivity *measurement* is a measurement of the connected pore fluid and of
the connectivity of any metallic phase, not a measurement of the mineral
assemblage: dry granite is five orders of magnitude more resistive than the same
granite saturated with brackish water (compare modules
[09-01-03](03-conduction-mechanisms.md) and
[../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md)).

## 4. Electrodes and contact resistance

An electrode is a current source of finite size. Model it as a hemisphere of
radius $a$ at the surface; the potential at the conductor's surface is that of a
point source at distance $a$, so the resistance to a distant return is

$$R = \frac{\rho}{2\pi a}.$$

*Numerical check (SYNTHETIC).* For $\rho = 100\ \Omega\,\mathrm{m}$ the demo
prints $R = 795.77\ \Omega$ at $a = 0.02\ \mathrm{m}$, $318.31\ \Omega$ at
$0.05\ \mathrm{m}$, $159.15\ \Omega$ at $0.10\ \mathrm{m}$ and $63.66\
\Omega$ at $0.25\ \mathrm{m}$. The resistance *falls* as the electrode grows
because the current has more area to enter.

That is the good news. The bad news is that a real electrode also has a
**contact resistance** $R_c$ due to the electrochemical interface — the demo uses
a SYNTHETIC $200\ \Omega$ — and in a two-electrode measurement the contact
resistances add to the geometric one:

$$R_\text{measured} = \frac{\rho}{2\pi}\left(\frac{1}{a_1} +
\frac{1}{a_2}\right) + R_{c1} + R_{c2}.$$

With $a = 0.02$ m the geometric term dominates ($795.77\ \Omega$ against
$400\ \Omega$) and the error is $1.25\times$; with $a = 0.10$ m the geometric
term is only $159.15\ \Omega$ and the same contact resistances make the reading
$2.26\times$ too large. **Growing the electrode does not help: it makes the
contact term relatively worse.** This is the quantitative argument for four
electrodes, developed in
[09-02-01 Resistivity Principle and the Four-Electrode Arrangement](../02-dc-resistivity/01-resistivity-principle.md).

## 5. Worked example: resistivity from a resistance, with an error budget

A synthetic laboratory measurement gives $R = 50449.9\ \Omega$ for the plug
above (true value $50929.6\ \Omega$; the demo added 2% multiplicative noise).

$$\sigma = \frac{L}{R A} = \frac{0.100}{50449.9 \times 1.963\times10^{-3}}
= 1.010\times10^{-3}\ \mathrm{S\,m^{-1}},$$

$$\rho = \frac{1}{\sigma} = 990.6\ \Omega\,\mathrm{m}
\quad\text{against a true } 1000.0\ \Omega\,\mathrm{m},$$

a $-0.94\%$ error for a 2% resistance error. The demo also tabulates the two
geometric error terms: a $+1.0\ \mathrm{mm}$ length error on a 100 mm plug moves
$\sigma$ by $+1.00\%$, while a $+0.2\ \mathrm{mm}$ radius error on a 25 mm plug
moves it by $-1.60\%$; a $+1.0\ \mathrm{mm}$ radius error moves it by $-8.00\%$.
The relative error in a cylindrical sample is

$$\frac{\delta\sigma}{\sigma} = \frac{\delta L}{L} -
2\frac{\delta r}{r},$$

so the radius enters *doubled*. On a real plug, which is never a perfect
cylinder, this is the dominant term and it is the reason laboratory resistivity
on small samples is quoted to a few per cent at best.

## 6. Regime of validity and assumptions

1. **The fields are static or quasi-static.** "DC" resistivity means frequencies
   far below the charge-relaxation frequency $\sigma/(2\pi\varepsilon)$, which
   for $\sigma = 0.1\ \mathrm{S\,m^{-1}}$ and $\varepsilon_r = 10$ is about
   $1.8\times10^{8}\ \mathrm{Hz}$ — see
   [09-01-05](05-temperature-and-pressure-effects.md) for the computation. Any
   frequency dependence met below that is *polarisation*, not electromagnetics.
2. **The ground is isotropic and ohmic.** $\sigma$ is a scalar and $J$ is
   exactly proportional to $E$. Anisotropy (layered clays) and non-linearity are
   real in the field and are handled later.
3. **The surface is an insulator.** The air carries no current, which produces
   the factor $2\pi$ in every formula here.
4. **The electrodes are points** of negligible radius compared with the
   electrode separation. Section 4 shows what happens when they are not.
5. **Dissipation is the whole story.** Resistivity measures energy loss, not
   stored energy; the dielectric constant is irrelevant at these frequencies.

## 7. Units table

| Quantity | Symbol | SI unit | Check |
|---|---|---|---|
| current | $I$ | A | |
| current density | $J$ | $\mathrm{A\,m^{-2}}$ | $I/A$ |
| electric field | $E$ | $\mathrm{V\,m^{-1}}$ | $\rho J$ |
| conductivity | $\sigma$ | $\mathrm{S\,m^{-1}}$ | $1/\rho$ |
| resistivity | $\rho$ | $\Omega\,\mathrm{m}$ | $\mathrm{V\,m\,A^{-1}}$ |
| resistance | $R$ | $\Omega$ | $V/I$ |
| geometric factor | $k$ | m | $\rho_a = k\,V/I$ |

## 8. Worked example: geometry error versus material error

Suppose the same plug is measured twice, once with a 1% length error and once
with the bore off-centre by 1% of the radius. From the relation above the two
errors are $+1\%$ and $-2\%$: choosing the geometry carefully is worth as much
as choosing the receiver carefully. Now repeat the argument for a field
measurement: for a Wenner array with spacing $a = 5$ m, a $1\ \mathrm{cm}$ error
on an electrode moves the apparent resistivity by $0.13$–$0.31\%$ *over a
two-layer ground* and by exactly $0$ over a uniform half-space — the
demonstration in
[`code/resistivity_principle_demo.py`](../02-dc-resistivity/code/resistivity_principle_demo.py)
prints those numbers. Unit: a *percentage of the reading*, not an absolute
resistivity, because the effect only appears when the ground varies in space.

## 9. Mastery checkpoint

Without notes:

1. Derive $V(r) = \rho I/(2\pi r)$ from $\mathbf{J} = \sigma\mathbf{E}$, stating
   where the 2 in $2\pi$ comes from.
2. A rock has $\sigma = 2.5\times10^{-3}\ \mathrm{S\,m^{-1}}$. Give $\rho$ in
   $\Omega\,\mathrm{m}$ and place it in the catalogue of Section 3.
3. A core plug is 5.0 cm long, 2.0 cm in diameter, and measures $2.4\
   \mathrm{k}\Omega$. Compute $\rho$ and state the two largest uncertainty
   sources.
4. Explain in two sentences why a two-electrode measurement of ground
   resistivity is unreliable, and what replaces it.

Worked solutions to (3) and (4) appear in
[the lesson exercises](exercises/01-resistivity-conductivity-solutions.md).

## 10. Common pitfalls

1. **Confusing resistance with resistivity.** A number in ohms is meaningless
   without the geometry that produced it.
2. **Forgetting the half-space factor.** Using $4\pi$ instead of $2\pi$ is a
   factor-2 error in every potential in the folder.
3. **Assuming a log scale is for display only.** The conductivity range spans
   six decades; linear averages of resistivity data are dominated by the
   largest values.
4. **Reading a laboratory value as a field value.** A plug is not the ground:
   it is a 100 ml sample, usually drained, at room temperature.
5. **Blaming the instrument for a poor contact.** The contact resistance is a
   *geometry* problem, and it is what four electrodes solve.

## 11. Related modules

- [09-01-02 Archie's Law, Porosity and Saturation](02-archies-law.md) — how
  $\rho$ depends on the pore fluid and the porosity.
- [09-01-03 Electrolytic, Electronic and Surface Conduction](03-conduction-mechanisms.md) —
  what physically carries the current.
- [09-02-01 Resistivity Principle and the Four-Electrode Arrangement](../02-dc-resistivity/01-resistivity-principle.md) —
  the measurement built on this lesson.
- [05-04-07 Electrical Properties, Archie's Law and Clay Effects](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md) —
  the rock-physics view of the same properties.
- [09-02 Resistivity Methods](../02-dc-resistivity/README.md).

## 12. Demonstration and exercises

- [`code/resistivity_conductivity_demo.py`](code/resistivity_conductivity_demo.py)
  prints the catalogue, the Ohm's-law checks, the half-space table, the
  current-conservation check, the electrode resistances and the error budget.
- [Exercises](exercises/01-resistivity-conductivity-exercises.md) and
  [worked solutions](exercises/01-resistivity-conductivity-solutions.md).
