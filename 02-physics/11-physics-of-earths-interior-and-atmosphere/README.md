# Module 02-11 — Physics of the Earth's Interior and Atmosphere

**Stages:** advanced → doctoral · **Prerequisites:**
[02-06-01 Fluid Statics, Pressure and Buoyancy](../06-fluid-mechanics/01-fluid-statics.md)
for hydrostatic balance, [02-08-01 Newtonian Gravitational Potential and Field](../08-potential-theory/01-gravitational-potential.md)
for $g$ inside a body, [02-04-04 Elastic Moduli](../04-elasticity-and-continuum-mechanics/04-elastic-moduli.md)
for $K$ and $\mu$, and [02-05-07 Thermodynamic Phase Equilibria](../05-thermodynamics/07-phase-equilibria.md)
for why the mantle has discontinuities at all.

This is the module where the physics folder stops building instruments and
starts building planets. Every preceding module contributed one tool: fluid
statics supplies hydrostatic balance, potential theory supplies gravity inside a
body of arbitrary shape, elasticity supplies the moduli that seismic velocities
measure, thermodynamics supplies the equations of state and the adiabat. Put
them together and you get the numbers that a reference Earth model is made of —
and you get the argument for why those numbers mean *iron core, silicate mantle*,
rather than merely *denser material below*.

Two rules govern everything here, and they are the reason this module is placed
at the end of the folder:

- **Every interior number is a model output, not a measurement.** No one has
  sampled the lower mantle or the outer core. The densities, pressures and
  temperatures quoted here are rounded characteristics of a reference model,
  taken from the [constant handbook](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  §3.3 or computed from those characteristics by the equations in these lessons.
  Where a number is computed, the lesson says so and shows the computation.
  Precise values at a specific depth require the reference model itself; the
  primary description of the Preliminary Reference Earth Model is Dziewonski and
  Anderson (1981), *Physics of the Earth and Planetary Interiors* **25**,
  297–356.
- **Every relation is checked.** The two demonstrations that carry the module —
  the numerical integration of hydrostatic balance and the segment-wise
  integration of the standard atmosphere — are verified against independent
  quantities (the Earth's mass and moment of inertia; the analytic isentropic
  pressure law). The measured discrepancies are reported in the lessons, not
  hidden.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the hydrostatic equation $\mathrm{d}P/\mathrm{d}r = -\rho(r)g(r)$
   for a self-gravitating sphere, and integrate it numerically over a layered
   reference model to obtain $P(r)$, $g(r)$ and $\rho(r)$.
2. **Explain** the density jump at the core–mantle boundary as a change of
   composition rather than of state, using the fact that $\rho$ jumps upward
   while $v_p$ jumps downward.
3. **Write** the Birch–Murnaghan equation of state, evaluate it at mantle and
   core pressures, invert it for volume at a given pressure, and explain what
   its third-order term means.
4. **Use** the seismic parameter $\phi = v_p^2 - \tfrac{4}{3}v_s^2 = K/\rho$, the
   Adams–Williamson relation $\mathrm{d}\rho/\mathrm{d}z = \rho g/\phi$, and the
   adiabatic temperature gradient $(\mathrm{d}T/\mathrm{d}z)_s = \gamma gT/\phi$.
5. **Recover** $K$, $\mu$ and Poisson's ratio from $(v_p, v_s, \rho)$, and
   explain why $(v_p, v_s)$ alone cannot determine $\rho$ — the density–velocity
   ambiguity that makes composition inference non-unique.
6. **Derive** the dry adiabatic lapse rate $\Gamma_d = g/c_p$, compute the
   scale height $H = RT/g$, integrate hydrostatic balance through the standard
   atmosphere, and compare the result with the observed tropospheric lapse rate.
7. **Apply** the moment-of-inertia factor $C/(MR^2)$ and the magnetic Reynolds
   number to other bodies, and state what each diagnostic does and does not
   constrain.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Pressure, Density and Gravity Inside the Earth](./01-pressure-density-depth.md) | advanced | **The mastery lesson**: integrate $\mathrm{d}P/\mathrm{d}r=-\rho g$ over a layered model and recover the mass, $g(r)$ and the centre pressure |
| 02 | [Equations of State and High-Pressure Mineral Physics](./02-equations-of-state.md) | doctoral | Birch–Murnaghan, $\phi = K/\rho$, Adams–Williamson, and why an isothermal EOS is never enough |
| 03 | [Seismic Velocities, Elastic Moduli and Mineralogy](./03-seismic-parameter-relations.md) | graduate | $(v_p, v_s, \rho) \to K, \mu, \nu$; the 410 and 660; and why the outer core transmits no $S$ waves |
| 04 | [Atmospheric Structure, Hydrostatic Balance and Lapse Rates](./04-atmospheric-structure.md) | advanced | The same hydrostatic equation in a compressible gas: scale height, dry adiabat, and the real temperature profile |
| 05 | [Comparative Planetary Physics and Interiors](./05-planetary-physics.md) | doctoral | Moment of inertia, dynamo criteria and atmospheric escape as the three diagnostics that transfer to other bodies |

## Suggested path

**If you are working through the physics folder in order:** all five lessons in
numeric order. Lesson 01 is the one that must be worked rather than read, because
it contains the numerical integration that every later number depends on.

**If you are here for global geophysics or seismology:** read [01](./01-pressure-density-depth.md)
in full, then [03](./03-seismic-parameter-relations.md) §2–§5, then
[12-global-geophysics-interior/01 Seismic Structure](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/01-prem-and-reference-models.md)
and [06-seismology/01-02 P and S Waves](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md).

**If you are here for mineral physics:** read [02](./02-equations-of-state.md) in
full, then [03](./03-seismic-parameter-relations.md) §2, then
[12-global-geophysics-interior/02 Composition and Mineral Physics](../../12-global-geophysics-interior/02-composition-and-mineral-physics/02-high-pressure-experiments.md).

**If you are here for atmosphere or climate:** read [04](./04-atmospheric-structure.md)
in full, then [16-atmosphere-climate/01-02 Hydrostatic Balance](../../16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/02-hydrostatic-balance.md)
and [16-atmosphere-climate/02 Radiation and Energy Balance](../../16-atmosphere-climate/02-radiation-and-energy-balance/01-solar-and-terrestrial-radiation.md).
Lesson 01 is not required; lesson 02 is not required.

**If you are here for planetary science:** read [05](./05-planetary-physics.md)
first for the diagnostic toolbox, then [01](./01-pressure-density-depth.md) for
the Earth as the worked example, then
[12-global-geophysics-interior/07 Planetary Interiors](../../12-global-geophysics-interior/07-planetary-interiors-comparative/01-terrestrial-planets-interiors.md).

**If you already have a geophysics background:** attempt ★★★8 of
[01](./01-pressure-density-depth.md), ★★★7 and ★★★8 of
[02](./02-equations-of-state.md) and ★★★8 of [05](./05-planetary-physics.md)
first. If those close cleanly, use lessons 03 and 04 as reference.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-pressure-density-depth.md`](./01-pressure-density-depth.md) … [`05-planetary-physics.md`](./05-planetary-physics.md) | The five lessons |
| [`code/interior_pressure_demo.py`](./code/interior_pressure_demo.py) | The layered reference model, the hydrostatic integration, and the mass, $g$, moment-of-inertia and Adams–Williamson checks |
| [`code/eos_mineral_physics_demo.py`](./code/eos_mineral_physics_demo.py) | Birch–Murnaghan second and third order, EOS inversion, the mantle adiabat, thermal pressure |
| [`code/velocity_moduli_demo.py`](./code/velocity_moduli_demo.py) | $K$, $\mu$, $\nu$ from velocities; the density–velocity ambiguity; Birch's law; impedance contrasts at four boundaries |
| [`code/atmospheric_structure_demo.py`](./code/atmospheric_structure_demo.py) | The dry adiabatic lapse rate, the scale height, the standard atmosphere, potential temperature and $N$ |
| [`code/planetary_physics_demo.py`](./code/planetary_physics_demo.py) | The two-layer moment-of-inertia inversion, the dynamo diagnostics and the Jeans escape parameter |
| [`exercises/`](./exercises) | Exercises and full worked solutions for all five lessons |

Every script uses only the Python standard library, so they run in any Python 3
installation with no packages. Run them; do not read them.

## Mastery checkpoint

Complete this without notes, with a calculator and no code.

> A spherically symmetric planet has a mean radius $R = 6371$ km and total mass
> $M = 5.972\times10^{24}$ kg. **(a)** Derive
> $\mathrm{d}P/\mathrm{d}r = -\rho(r)g(r)$ from the balance of forces on a thin
> shell, and derive $g(r) = GM(r)/r^2$ from the shell theorem, stating why only
> the mass *inside* $r$ contributes. **(b)** Explain why the pressure at the
> centre of a body of this mass is of order $GM^2/R^4$ and evaluate the
> coefficient: show that using the mean density gives
> $P_c \sim 0.4\,G M^2/R^4$ for a uniform sphere, and evaluate it. **(c)** A
> rounded model has a uniform mantle of density 4138 kg/m³ out to $r = 3480$ km
> and a uniform core of density 12576 kg/m³ inside (these are the two-layer
> values implied by part (e); they are derived in lesson 05 §1). Compute the
> pressure at the centre using the two-layer approximation (integrate the mantle
> analytically and add the core contribution). **(d)** Compare with the
> numerically integrated value from
> [`code/interior_pressure_demo.py`](./code/interior_pressure_demo.py) and explain
> why the two-layer answer is too high. **(e)** The same body has
> $C/(MR^2) = 0.33$. Explain in one sentence each what this tells you that the
> mass and radius alone do not, and what it still does not tell you.

Parts (a) and (b) are lesson [01](./01-pressure-density-depth.md) §2;
parts (c)–(e) are lesson [01](./01-pressure-density-depth.md) §§3–4.

**Worked answer for (b)–(d):**

For a uniform sphere $M(r) = Mr^3/R^3$, so with $\rho = M/(\tfrac43\pi R^3)$,

$$P_c = \int_0^R \rho\frac{GM(r)}{r^2}\,\mathrm{d}r = \rho\frac{GM}{R^3}\int_0^R r\,\mathrm{d}r
= \frac{3GM^2}{8\pi R^4} = 0.1194\,\frac{GM^2}{R^4},$$

which evaluates to $0.1194 \times 6.674\,30\times10^{-11}\times(5.972\times10^{24})^2/(6.371\times10^6)^4
= 1.7246\times10^{11}$ Pa, i.e. **172.5 GPa**. It is a *lower* bound: concentrating
mass toward the centre raises the central pressure, and the demo's 356.7 GPa is
twice as large.

For the two-layer planet the integral splits into a core part and a mantle part,

$$P_c=\underbrace{\tfrac{2}{3}\pi G\rho_c^2r_c^2}_{\text{core}}
+\underbrace{\tfrac{4}{3}\pi G\rho_m\Big[(\rho_c-\rho_m)r_c^2\Big(1-\frac{r_c}{R}\Big)
+\tfrac{\rho_m}{2}\big(R^2-r_c^2\big)\Big]}_{\text{mantle}},$$

because inside the core $g \propto r$ while outside it the mantle sits on top of a
fixed core mass. With $\rho_c = 12\,576$ kg m⁻³, $\rho_m = 4138$ kg m⁻³ and
$r_c = 3480$ km this gives $267.7 + 121.8 = \mathbf{389.5}$ GPa.

Comparing with the numerical layered model, **389.5 GPa over-predicts 356.7 GPa
by 9.2 per cent.** The reason is that the two-layer model puts the whole core at
its mean density, whereas the real core is lighter at its top (9900 kg m³ near
the CMB from the handbook) and heavier only near its centre; the same applies to
the mantle. Because the pressure integrand weights the outer part of the body
most strongly — a shell at radius $r$ contributes $\rho g\,\mathrm{d}r$ to the
pressure but contributes $\propto r^2$ to the mass above it — the two-layer
model, which pushes mass outward, is biased high.

Parts (d) and (e) are the module's central methodological point: the *shape* of
the density profile, not merely its mean, sets the pressure; the mass and radius
fix the mean, and the moment of inertia is what constrains the shape.

## Common pitfalls across this module

1. **Treating a reference-model value as a measurement.** $g$ at the CMB, the
   density at 2000 km and the temperature of the core are model outputs. Quoting
   them to four digits presents a fit as a fact.
2. **Assuming an equation of state calibrated at 300 K applies at 3000 K.** The
   thermal pressure term in lesson [02](./02-equations-of-state.md) §6 is tens
   of gigapascals, comparable to the whole pressure at the top of the lower
   mantle.
3. **Extrapolating Birch's law across the core–mantle boundary.** It is an
   empirical correlation at nearly constant mean atomic weight and it does not
   survive the change of material.
4. **Reading a velocity jump as a density jump.** At the CMB they point in
   opposite directions, which is exactly the information that matters.
5. **Confusing $v_s = 0$ with "we cannot observe it".** The outer core has no
   shear modulus because it is liquid; that is a physical statement, not an
   instrumental limit.
6. **Using the dry adiabatic lapse rate for the real troposphere.** 9.8 K/km
   against an observed 6.5 K/km is a 50 per cent error, and the difference is
   latent heat.
7. **Applying the ideal-gas scale height to an incompressible body.** $H = RT/g$
   requires an ideal gas; the deep atmosphere is not one and neither is the
   mantle.
8. **Forgetting that a hydrostatic integration needs a boundary condition.**
   $P(R) = 0$ at the surface is the only one available; everything else follows.
9. **Reporting a moment of inertia without saying which axis.** The polar and
   equatorial moments differ, and the difference is itself a measurement of the
   planet's flattening.
10. **Quoting a planetary magnetic field as a constant.** The Earth's dipole
    moment alone changes measurably over decades.

## Related folders

- [02-physics/05 Thermodynamics and Heat Transfer](../05-thermodynamics/README.md)
  — the adiabat, the geotherm and the phase transitions that make the 410 and
  660 km discontinuities.
- [02-physics/06 Fluid Mechanics](../06-fluid-mechanics/README.md) — hydrostatic
  balance in full, and the convection that drives the geodynamo.
- [02-physics/08 Potential Theory](../08-potential-theory/README.md) — the shell
  theorem, Poisson's equation and the gravity field of a layered body.
- [06-seismology](../../06-seismology/README.md) — how $v_p$ and $v_s$ are
  actually measured, and how a reference model is built.
- [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)
  — the seismological structure, core composition and thermal evolution of the
  Earth in detail.
- [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) — mantle
  convection and the temperature field this module treats as an input.
- [16-atmosphere-climate](../../16-atmosphere-climate/README.md) — atmospheric
  thermodynamics, radiation and the climate system.
- [26-reference-library/02 Constants and Units](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the classification of every constant used here as exact, measured or
  nominal.
