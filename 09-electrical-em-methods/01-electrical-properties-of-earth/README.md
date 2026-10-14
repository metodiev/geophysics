# Module 09-01 — Electrical Properties of Earth Materials

**Stages:** intermediate → graduate · **Prerequisites:** electrostatics and
field theory (module 02-07), the rock-physics property relations (module
05-04), basic multivariable calculus.

Resistivity is the property that makes electrical methods useful and the
property that makes them dangerous. It is useful because it responds strongly to
the things we care about — water, salinity, clay, sulphide, temperature — and it
is dangerous because almost all of those things change it, often by comparable
amounts, and a single resistivity measurement cannot say which one moved. This
module builds the property relations from the mechanisms up, and it spends as
much effort on the ambiguity as on the models: what Archie's law assumes, what a
surface-conduction term does to a porosity estimate, and how much of a
resistivity change a temperature change can explain.

Every lesson follows the same discipline. A relation is either *derived* from a
stated mechanism (the Nernst–Einstein form for ionic conduction, the geometric
factor of a capillary bundle, the Arrhenius temperature law), or *stated
explicitly as empirical* and then tested for what it can separate (Archie's $a$,
$m$ and $n$; the counter-ion conductance $\beta$). The demonstrations print
every number used in the text, including the negative results: an $a$/$m$ pair
that is exactly degenerate at one porosity, a surface term that produces a water
saturation of 370%, a Debye phase spectrum whose integral is $\ln(\sigma_\infty/
\sigma_0)$ and not the chargeability.

**All models and data in this module are SYNTHETIC.** The resistivities,
porosities, CEC values, activation energies and relaxation parameters are chosen
teaching values, not measurements. The physical constants quoted ($k_B$,
$\varepsilon_0$, $e$, $N_A$, and the limiting ionic mobilities) are standard
values stated with their units; no site, instrument or data set is referred to.

## Learning objectives

By the end of this module you will be able to:

1. **Convert** between resistivity and conductivity in SI units, **derive** the
   half-space point-source potential, and **explain** why a two-electrode
   measurement is not a resistivity measurement.
2. **Derive** the formation factor from a pore-geometry model, **state** Archie's
   laws as empirical forms, and **quantify** the $1/m$ amplification of a
   porosity error and the exact $(a,m)$ degeneracy at a single porosity.
3. **Compute** an ionic conductivity from mobilities, **bound** a two-phase
   mixture, and **demonstrate** that conductivity alone cannot separate a
   conductive mineral's presence from its connectivity.
4. **Convert** a cation exchange capacity into a pore-volume cation excess,
   **compute** the surface conductivity, and **detect** an inadmissible water
   saturation produced by ignoring it.
5. **Compute** a Debye complex conductivity, **verify** the phase-area identity
   $\frac{2}{\pi}\int|\varphi|\,\mathrm{d}\ln f = \ln(\sigma_\infty/\sigma_0)$
   numerically, and state what a phase measurement does and does not give.
6. **Compute** the conductivity change produced by temperature, freezing,
   compaction and frequency, and **decide** which of them an observed change can
   be attributed to.

## Prerequisites

- [02-07 Electromagnetism and Electromagnetic Induction](../../02-physics/07-electromagnetism/README.md) —
  electrostatics, current continuity and conduction in a continuum.
- [05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md) —
  porosity, density and the electrical properties of rocks.
- [01-06 Multivariable Calculus](../../01-mathematics/06-multivariable-calculus/README.md) —
  divergence, flux and the divergence theorem.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Resistivity and Conductivity: Definitions and Ranges](01-resistivity-conductivity.md) | intermediate | Six decades of conductivity, one factor of $2\pi$, and a contact resistance that geometry cannot remove |
| 02 | [Archie's Law, Porosity and Saturation](02-archies-law.md) | advanced | The exponent is a bigger error source than the measurement; one porosity cannot give $a$ and $m$ |
| 03 | [Electrolytic, Electronic and Surface Conduction](03-conduction-mechanisms.md) | graduate | Connectivity, not conductivity, decides; removing the surface term amplifies error |
| 04 | [Clay Effects, CEC and Membrane Polarisation](04-clay-and-surface-conduction.md) | graduate | $Q_v$ from CEC, an impossible saturation, and a phase spectrum whose area is not the chargeability |
| 05 | [Temperature, Pressure and Frequency Dependence](05-temperature-and-pressure-effects.md) | graduate | Mobility, phase change and compaction; two frequency scales eight decades apart |

## Suggested path

**If you are new to electrical methods:** lessons 01–03 in order, running each
demonstration. Lesson 02 is the one that changes how you read a resistivity
number.

**If you already know Archie's law:** start at 02 §5 (the degeneracy) and 03 §4
(the three-term decomposition), then 04 §3 (the conditioning of the repair) —
these are the parts that decide whether a porosity or saturation estimate is
defensible.

**If you are preparing a research project:** 03 §4–5, 04 §5 (the phase-area
identity) and 05 §4 (the two frequency scales), plus the ★★★ exercises, which
ask for calibration designs and falsification criteria.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-resistivity-conductivity.md`](01-resistivity-conductivity.md) | Lesson 01 |
| [`02-archies-law.md`](02-archies-law.md) | Lesson 02 |
| [`03-conduction-mechanisms.md`](03-conduction-mechanisms.md) | Lesson 03 |
| [`04-clay-and-surface-conduction.md`](04-clay-and-surface-conduction.md) | Lesson 04 |
| [`05-temperature-and-pressure-effects.md`](05-temperature-and-pressure-effects.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 09-electrical-em-methods/01-electrical-properties-of-earth/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resistivity_conductivity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python archies_law_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python conduction_mechanisms_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python clay_and_surface_conduction_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python temperature_and_pressure_effects_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), imports no plotting library, and exits 0.
They require no network access.

## Mastery checkpoint

Complete this without notes:

> A clay-bearing sand has $\phi = 0.22$, $m = 2$, $\rho_w = 2.0\
> \Omega\,\mathrm{m}$ at $25\ ^\circ\mathrm{C}$, $\mathrm{CEC} = 12\
> \mathrm{meq/100\,g}$, $\rho_g = 2.65\ \mathrm{g\,cm^{-3}}$ and a counter-ion
> conductance of $0.10\ \mathrm{(\Omega\,m)^{-1}}$ per $(\mathrm{eq/L})$. It is
> measured at $10\ ^\circ\mathrm{C}$ and gives $\rho = 25\
> \Omega\,\mathrm{m}$. **(a)** Compute $F$, $Q_v$ and the surface conductivity.
> **(b)** Correct the measurement to $25\ ^\circ\mathrm{C}$ and compute the water
> saturation with $n = 2$, with and without the surface term. **(c)** State which
> answer is admissible and why. **(d)** State the one measurement that would
> most reduce the remaining uncertainty.

A worked version of (a)–(c) appears in the lesson-04
[solutions](exercises/04-clay-and-surface-conduction-solutions.md).

## Common pitfalls across this module

1. **Reading a resistivity as a saturation, a porosity or a salinity.** It is a
   single number that several mechanisms can produce.
2. **Quoting $a$, $m$ or $n$ without a calibration.** They are rock-type fits,
   and the exponent divides or multiplies the answer.
3. **Ignoring surface conduction.** It can carry most of the current in a clay,
   and it produces impossible saturations when ignored.
4. **Adding conductivities and resistivities interchangeably.** The sums are in
   $\sigma$.
5. **Treating temperature as a correction.** It is worth a factor of two in an
   aquifer, and freezing is worth a factor of ten.

## Related modules

- [09-02 Resistivity Methods](../02-dc-resistivity/README.md) — the measurement
  that uses these properties.
- [09-03 Induced Polarisation](../03-induced-polarisation/README.md) — the
  frequency dependence introduced here, in full.
- [09-05 Applied Electromagnetic Methods](../05-em-methods-applications/README.md).
- [14-03 Petrophysical Relations for Saturated Media](../../14-hydrology-hydrogeophysics/03-petrophysics-hydrology/README.md) —
  the hydrogeological use of the same relations.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of the non-uniqueness this module keeps finding.
