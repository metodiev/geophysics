# Module 06-01 — Elastic Wave Propagation

**Stages:** advanced → doctoral · **Prerequisites:** multivariable calculus
(divergence, curl and the vector identities); the mechanics of an elastic
continuum up to the elastodynamic equation; basic Python with NumPy.

This module is where seismology stops being a list of named arrivals and becomes
one equation with consequences. It builds the elastodynamic equation from
Hooke's law and Newton's second law, splits it into the two body-wave modes,
derives the free-surface and interface boundary-value problems that produce
surface and interface waves, and then shows — in the last three lessons — what
happens to all of it when the two assumptions that made the derivations tidy are
removed.

The central honest difficulty of the module is that **every named wave is an
approximation to a part of a wavefield**. A "P arrival" is a stationary-phase
contribution to a slowness integral; a "head wave" is a branch-line
contribution; a "Stoneley mode" exists only for certain contrasts; a "scattered
coda" is the energy that a single-scattering formula has already thrown away.
Each lesson states which approximation is in force and what it discards, and
each demonstration measures where the approximation stops working rather than
quoting a validity condition. Where a measurement contradicts a comfortable
statement — the coherent-stack scattering limit, the $\omega^2$ scattering law,
the direction-dependence of shear-wave splitting — the measurement wins.

All models and data in this module are **SYNTHETIC**. No real station, event or
waveform is used, and no number is quoted from a published measurement. Real
numbers appear only where they are exact standard constants with stated units
(for example the Poisson-solid ratio $\sqrt{3}$, or the tabulated travel times of
the standard `iasp91` reference model, which the demonstration queries rather
than asserts).

## Learning objectives

By the end of this module you will be able to:

1. Derive the elastodynamic equation from kinematics, dynamics and a
   constitutive law, and separate it into the two wave equations for $\phi$ and
   $\boldsymbol\psi$.
2. Derive the P and S speeds, the ratio $v_p/v_s$, its two lower bounds, and the
   polarisation structure, and measure them on synthetic three-component data.
3. Derive the Love-wave dispersion relation and the Rayleigh secular equation,
   and distinguish phase from group velocity on a measured dispersion curve.
4. Solve the normal-incidence and Zoeppritz boundary-value problems, verify the
   energy-flux balance with the correct impedance factor, and read a
   travel-time table as a set of named arrivals.
5. Derive and invert the Helmholtz decomposition, and measure the orthogonality
   of the P and S energies.
6. Distinguish the critical-point types that produce body, surface, head and
   interface arrivals, and measure the existence boundary of a trapped welded
   mode.
7. Derive the exact and single-scattering responses of a random medium, measure
   where Born fails, and state where the missing energy goes.
8. Solve the Christoffel equation, build a VTI tensor from Thomsen parameters,
   and measure the ray–phase split and the shear-wave splitting.

## Prerequisites

- [01-06 Multivariable Calculus](../../01-mathematics/06-multivariable-calculus/README.md) —
  especially
  [04 Divergence and Curl](../../01-mathematics/06-multivariable-calculus/04-divergence-and-curl.md),
  which supplies the vector identities used in every derivation here.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md) —
  stress, strain, the constitutive law and
  [05 Elastodynamics](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md).
- [03-10 ObsPy and Seismic Data](../../03-scientific-computing/10-obspy-and-seismic-data/README.md) —
  the tooling used for the one demonstration that queries a standard Earth model.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [From Hooke's Law and Newton to the Elastodynamic Equation](01-wave-equation-elastic.md) | graduate | Three ingredients, one vector equation, two wave equations |
| 02 | [P and S Waves: Particle Motion, Speeds and Polarisation](02-p-and-s-waves.md) | advanced | $v_p/v_s$ has two lower bounds, and the weaker assumption is the physical one |
| 03 | [Rayleigh and Love Waves: Dispersion and Depth Sensitivity](03-surface-waves.md) | graduate | A waveguide must be a low-velocity layer; $c$ and $U$ are different measurements |
| 04 | [Reflected, Refracted and Converted Body Waves](04-body-wave-arrivals.md) | advanced | The flux factor is $Z_2/Z_1$; the boundary conditions, not the energy sum, catch a sign error |
| 05 | [Helmholtz Decomposition and Wavefield Potentials](05-wavefield-potentials.md) | graduate | The split is orthogonal, which is why the two energies add |
| 06 | [Interface Waves, Head Waves and the Total Wavefield](06-interface-waves.md) | doctoral | A ray is a name for a critical point; the ray sum is not the field |
| 07 | [Scattering, Coda and Random Media](07-scattering-and-heterogeneity.md) | doctoral | Born is a measured regime; the deficit is coda, not attenuation |
| 08 | [Wave Propagation in Anisotropic Media](08-anisotropic-propagation.md) | doctoral | Polarisation is an eigenvector, and the ray is not the phase direction |

## Suggested path

**If you are new to the subject:** lessons 01–05 in order, running each
demonstration before reading the next lesson. Lesson 02 is the shortest route to
a usable result, and lesson 04 is where the sign conventions are settled.

**If you already know the isotropic theory:** read 01 §4 for the factorisation,
then 06, 07 and 08, which are the three ways the isotropic picture fails.

**If you are preparing a research project:** 05 (the decomposition, and where it
stops being convenient), 07 (scattering and the limits of single scattering),
08 (the Christoffel equation, group versus phase velocity), plus the ★★★
exercises in each companion.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-wave-equation-elastic.md`](01-wave-equation-elastic.md) | Lesson 01 |
| [`02-p-and-s-waves.md`](02-p-and-s-waves.md) | Lesson 02 |
| [`03-surface-waves.md`](03-surface-waves.md) | Lesson 03 |
| [`04-body-wave-arrivals.md`](04-body-wave-arrivals.md) | Lesson 04 |
| [`05-wavefield-potentials.md`](05-wavefield-potentials.md) | Lesson 05 |
| [`06-interface-waves.md`](06-interface-waves.md) | Lesson 06 |
| [`07-scattering-and-heterogeneity.md`](07-scattering-and-heterogeneity.md) | Lesson 07 |
| [`08-anisotropic-propagation.md`](08-anisotropic-propagation.md) | Lesson 08 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Eight runnable, print-only demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 06-seismology/01-elastic-wave-propagation/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python wave_equation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python p_s_waves_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python surface_waves_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python body_wave_arrivals_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python wavefield_potentials_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python interface_waves_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python scattering_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python anisotropic_propagation_demo.py
```

Every demonstration prints labelled section headers and every result **with
units**, uses a fixed random seed (`np.random.default_rng(20261014)`) wherever
randomness enters, requires no network access, and exits 0.

## Mastery checkpoint

Complete this without notes:

> A SYNTHETIC two-layer model has $v_p = 3000\ \mathrm{m\,s^{-1}}$,
> $v_s = 1732\ \mathrm{m\,s^{-1}}$, $\rho = 2400\ \mathrm{kg\,m^{-3}}$ above, and
> $v_p = 4500\ \mathrm{m\,s^{-1}}$, $v_s = 2600\ \mathrm{m\,s^{-1}}$,
> $\rho = 2600\ \mathrm{kg\,m^{-3}}$ below. **(a)** Compute both impedances and the
> potential-convention reflection coefficient. **(b)** Verify the energy-flux
> balance with the correct factor, and state what the same sum gives with
> $v_1/v_2$ in place of the impedance ratio. **(c)** Compute the P critical angle.
> **(d)** State one measurement that would distinguish a dipping interface from
> anisotropy, and one that would not.

A worked version of (a)–(c) appears in the lesson-04
[solutions](exercises/04-body-wave-arrivals-solutions.md).

## Common pitfalls across this module

1. **Using $v_1/v_2$ as the energy-flux factor.** It is $Z_2/Z_1$; the measured
   error for a plausible density contrast is 56 per cent (lesson 04).
2. **Quoting $|R|^2 \propto \omega^2$ for scattering.** It needs a small phase
   across the scattering volume, which fails by a factor of more than ten in the
   demonstration's band (lesson 07).
3. **Calling a measured speed a medium property without checking grid
   dispersion.** At the coarsest grid the demonstration's finite-difference speed
   is 3.7 per cent low (lesson 01).
4. **Treating a coherent stack as many reflectors.** It telescopes to one, and
   the exact coherent power is *half* a single interface's variance (lesson 07).
5. **Reading a shear-wave splitting as a scalar.** Along a symmetry axis it is
   exactly zero however anisotropic the medium (lesson 08).
6. **Reporting agreement between two solvers as physical validation.** Two
   discretisations of the same physics validate the arithmetic, not the model
   (lessons 01 and 06).

## Related modules

- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  what you get when the wavelength is small compared with the structure.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  the energy loss this module deliberately excludes, and how to separate it from
  scattering.
- [06-08 Receiver Functions and Crustal Structure](../08-receiver-functions-and-crustal-structure/README.md) —
  anisotropy and layering as an inverse problem from body-wave conversions.
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) — the same
  boundary conditions applied to imaging.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) — where
  the elastic moduli, and the anisotropy, actually come from.
