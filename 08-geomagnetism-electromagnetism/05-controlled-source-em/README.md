# Module 08-05 — Controlled-Source Electromagnetics

**Stages:** graduate → research · **Prerequisites:** modules 08-04 and 02-07;
the diffusion equation.

This module is about EM measurements in which the source is a generator we
control: a coil, a loop or a wire, at a separation we choose, at frequencies we
choose. That control buys amplitude, repeatability and geometry, and it buys the
ability to design an experiment rather than wait for a natural source. It does
not buy information the physics does not contain, and the honesty point of the
module is quantitative throughout: a coplanar coil pair measures $\sigma r^2$ and
not $\sigma$; a decay curve measures $\sigma d^2$ from its slope and $\sigma d$
from its amplitude; a layered response cannot distinguish models inside an
equivalence band; and an airborne survey is limited by its altimeter before it is
limited by its electronics. Every one of those statements is *measured* in the
lesson that makes it, with the resolution check printed next to the number.

The five lessons form one arc: the frequency-domain response and its exact
solution (08-05-01), the same physics after switch-off (08-05-02), the three
families of forward model with their measured convergence (08-05-03), the
inversion and its resolution and dimensionality limits (08-05-04), and the
airborne case where geometry becomes a data uncertainty (08-05-05). Along the way
the module builds one reusable asset: a verified layered electromagnetic solver,
with its verification and its convergence rate on the record.

All models and data in this module are **SYNTHETIC**. The conductivities,
separations, heights, frequencies, noise levels and meshes are chosen teaching
values. No real survey, system, station or published measurement is described.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the diffusion equation in a conductor, the skin depth
   $\delta=\sqrt{2/(\omega\mu_0\sigma)}$ and the criterion that licenses dropping
   displacement current.
2. **Derive** the exact halfspace response of a coplanar coil pair as a Sommerfeld
   integral, and **verify** it against adaptive quadrature, the perfect-conductor
   image limit, the analytic weak-induction limit and a scale-invariance check.
3. **Quantify** the error of the low-induction-number approximation (about
   $1.5\theta$) and **propagate** it into an apparent conductivity.
4. **State** the conductivity–separation ambiguity and name the two measurements
   that break it.
5. **Derive** the eigenmode decay of a conductive body and the halfspace
   similarity solution, and **verify** a finite-difference solution against both.
6. **State** the $\sigma d^2$ versus $\sigma d$ ambiguity and **explain** why the
   late-time slope and the early-time amplitude carry different information.
7. **Derive** the layered admittance recursion from the interface conditions and
   **verify** a layered code four ways.
8. **Measure** model equivalence, the linearisation (Born) validity range, and the
   convergence order of finite-difference and finite-element discretisations.
9. **Construct** an Occam inversion, **measure** its misfit–roughness trade-off,
   and **report** its singular-value spectrum and resolution kernels.
10. **Distinguish** dimensional errors a 1-D inversion absorbs (amplitude → bias)
    from those it cannot (phase → misfit).
11. **Quantify** the height–conductivity trade-off, overburden masking and depth
    of investigation of an airborne EM system.

## Prerequisites

- [08-04 Electromagnetic Induction in the Earth](../04-electromagnetic-induction/README.md)
  — induction, skin depth and conductivity structure.
- [02-07 Electromagnetism](../../02-physics/07-electromagnetism/README.md) —
  Maxwell's equations, induction and EM fields in conductors.
- [01-10 Fourier Analysis](../../01-mathematics/10-fourier-analysis/README.md) and
  [01-12 Numerical Methods](../../01-mathematics/12-numerical-methods/README.md)
  — transforms and discretisation, used without further proof.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Frequency-Domain EM (FDEM) Systems and Responses](01-frequency-domain-em.md) | graduate | Bucking removes the primary; the LIN form is good to $1.5\theta$; one separation measures $\sigma r^2$ |
| 02 | [Time-Domain EM (TDEM): Sounding, Transients and Decay Curves](02-time-domain-em.md) | graduate | $\tau=\mu_0\sigma d^2/\pi^2$ and the $\sqrt{Dt}$ law; the slope gives $\sigma d^2$, the amplitude $\sigma d$ |
| 03 | [EM Forward Modelling: Integral Equation, FD, FE Methods](03-em-modelling.md) | research | An admittance recursion verified four ways; equivalence and Born validity measured, not asserted |
| 04 | [EM Inversion and Dimensionality](04-em-inversion.md) | research | Occam inverts a misfit against roughness; the Jacobian's singular values *are* the resolution |
| 05 | [Airborne EM for Conductivity Mapping](05-airborne-em.md) | doctoral | Height multiplies the signal; a metre of height costs $4$–$25\%$ of the conductivity |

## Suggested path

**If you are new to controlled-source EM:** lessons 01 and 02 in order, running
each demonstration. Lesson 01 establishes the response and its approximation;
lesson 02 shows why the time domain is preferred in the field.

**If you already know a coil system:** start at the verification section of
lesson 01 (§7), then lesson 03 (§3, §5, §7) for the modelling craft, then lessons
04 and 05 for what the numbers can support.

**If you are preparing a research project:** lesson 03's equivalence and Born
measurements, lesson 04's resolution analysis, and the ★★★ exercises of each
lesson — they ask for designs and specifications rather than calculations.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-frequency-domain-em.md`](01-frequency-domain-em.md) | Lesson 01 |
| [`02-time-domain-em.md`](02-time-domain-em.md) | Lesson 02 |
| [`03-em-modelling.md`](03-em-modelling.md) | Lesson 03 |
| [`04-em-inversion.md`](04-em-inversion.md) | Lesson 04 |
| [`05-airborne-em.md`](05-airborne-em.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 08-geomagnetism-electromagnetism/05-controlled-source-em/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fdem_response_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tdem_decay_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_modelling_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_inversion_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python airborne_em_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access, and exits 0. The
slowest (the inversion) takes about four seconds.

## Mastery checkpoint

Complete this without notes:

> A coplanar coil pair on the ground records a quadrature of
> $1.1\times10^{-2}$ at $f=1\ \mathrm{kHz}$, and a second pair half the
> separation records $2.8\times10^{-3}$ at the same frequency. **(a)** Compute
> $\sigma r^2$ from the LIN form for both and decide whether the two are
> consistent with a homogeneous ground. **(b)** State the sign and size of the
> LIN bias at the larger induction number and correct the conductivity
> accordingly. **(c)** A time-domain sounding at the same site gives
> $\tau=1.0\ \mathrm{\mu s}$ and a conductance of $0.3\ \mathrm{S}$. Compute
> $\sigma d^2$, then $d$ and $\sigma$, and state which of the two is the weaker
> number and why. **(d)** Name the two observations that would most reduce the
> remaining ambiguity.

A worked version of the frequency-domain steps appears in the lesson-01
[solutions](exercises/01-frequency-domain-em-solutions.md), and the
conductance–depth step in the lesson-02
[solutions](exercises/02-time-domain-em-solutions.md).

## Common pitfalls across this module

1. **Reporting a conductivity without a geometry.** Coil separations, heights and
   thicknesses are part of the measurement, not context.
2. **Treating the low-induction form as exact.** Its bias is $1.5\theta$ and it
   propagates into every apparent conductivity.
3. **Quoting one number from a decay curve.** The slope and the amplitude measure
   different combinations.
4. **Publishing a forward model without a resolution check.** Every number in this
   module comes with the change under refinement printed next to it.
5. **Publishing an inversion as a model.** The misfit–roughness set, the
   singular-value spectrum and the kernel widths are part of the result.
6. **Assuming the data are one-dimensional.** Amplitude effects are absorbed
   silently as conductivity bias; only phase and multi-component data protest.
7. **Flying higher to cover more ground.** Height costs signal, time and
   conductivity accuracy, in that order of visibility and the reverse order of
   seriousness.

## Related modules

- [08-04 Electromagnetic Induction in the Earth](../04-electromagnetic-induction/README.md)
  — the natural-source methods that share this physics.
- [08-06 Applied Magnetism in Hazard and Environmental Studies](../06-magnetic-methods-hazards/README.md)
  — the magnetic counterpart of the applied surveying idea.
- [09-electrical-em-methods](../../09-electrical-em-methods/README.md) — DC
  resistivity and induced polarisation, the galvanic neighbours of these methods.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general theory
  behind lesson 04.
- [11-exploration-geophysics](../../11-exploration-geophysics/README.md) — where
  controlled-source EM is used and what it is asked to find.
