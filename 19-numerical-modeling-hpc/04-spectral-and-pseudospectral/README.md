# Module 19-04 — Spectral and Pseudospectral Methods

**Stages:** research · **Prerequisites:** modules 19-01 and 19-03, and the
Fourier sequence in 01-10.

**All models and data in this module are SYNTHETIC.** The test functions,
coefficient sets, grids and bands are chosen teaching models; every reference
value is either an exact mathematical identity (the alias frequency, the exact
transform of a product, orthonormality, Parseval) or a number printed by the
demonstration named in the lesson.

This module is about what happens when the basis functions are **global** and
**matched to the geometry**. A Fourier series suits a periodic interval, a
Chebyshev series an interval with boundaries, and spherical harmonics a sphere;
in each case the payoff is that the error of an analytic function falls faster
than any power of the resolution, rather than by a fixed factor per refinement.
That change of *law* — geometric rather than algebraic — is the single idea the
module is built around, and every lesson measures it against something
independent: a finite-difference stencil, an exact product, an analytic factor, or
a closed-form resonance frequency.

Three things follow from adopting a global basis, and each is measured here.
First, the **operator becomes dense** and its norm grows with the resolution, so
double-precision round-off becomes a hard floor that no refinement improves —
every convergence table in this module therefore ends where the improvement
stops, and says why. Second, **nonlinear terms alias**: a product of two modes
can exceed what the grid can carry, and the lost mode reappears at a low mode with
full amplitude, which no choice of time step removes. Third, a global basis
**cannot follow geometry**, which is why the module ends with spectral elements
(local elements, high-order basis) and with spherical harmonics (a global basis
that matches the one geometry that has no elements at all).

## Learning objectives

By the end of this module you will be able to:

1. **Measure** the exponential convergence of a spectral derivative on smooth
   data, **identify** the round-off floor that terminates it, and **contrast** the
   rate with second- and fourth-order finite differences at equal resolution.
2. **Predict** and **measure** how a kink or an endpoint discontinuity changes the
   rate, and **state** which norm does and does not converge.
3. **Choose** a basis from the geometry of a problem, and **justify** the choice
   with a measured error rather than a preference.
4. **Compute** alias frequencies and fold indices, **derive** the aliasing of a
   quadratic nonlinearity, and **implement** both standard de-aliasing rules with
   their conditions stated.
5. **Derive** the diagonal mass matrix of a Gauss-Lobatto-Legendre spectral
   element, **separate** the lumping error from the discretisation error, and
   **measure** both the exponential $p$-rate and the algebraic $h$-rate.
6. **Measure** how the extreme eigenvalue of a spectral-element operator scales
   with order and with element size, and **convert** that into an explicit
   time-step limit.
7. **Verify** a spherical harmonic synthesis/analysis pair against orthonormality
   and Parseval, **compute** the sampling a band-limited field requires, and
   **quantify** the degree at which downward continuation stops being useful.

## Prerequisites

- [19-01 Numerical Foundations for Simulation](../01-numerical-foundations/README.md) —
  convergence rates and numerical dispersion, the language used throughout.
- [19-03 Finite Element and Finite Volume Methods](../03-finite-element-and-volume/README.md) —
  the element, quadrature and assembly machinery that spectral elements reuse.
- [01-10 Fourier Analysis and Spectral Methods](../../01-mathematics/10-fourier-analysis/README.md) —
  the transforms and the sampling theorems applied here.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Spectral Methods: Basis Choice and Exponential Convergence](01-spectral-methods.md) | research | Global matched bases converge geometrically; a kink or a boundary mismatch collapses the rate; the round-off floor is $\lVert D\rVert \epsilon$ |
| 02 | [Pseudospectral Methods, Transforms and Aliasing](02-pseudospectral.md) | research | A grid relabels modes above Nyquist; a quadratic product folds a lost mode into a low one, and the 2/3 rule and 3/2 padding have stated conditions |
| 03 | [Spectral Element Methods and Their Geophysical Use](03-spectral-elements.md) | research | GLL nodes make the mass matrix exactly diagonal while the diagonal itself is under-integrated; $p$-refinement is exponential, $h$-refinement algebraic, and both shrink the time step |
| 04 | [Spherical Harmonic Modelling of Global Fields](04-spherical-harmonics-modelling.md) | research | The basis that matches a sphere; a band limit is an exact sampling requirement, and downward continuation is exact but unstable |

## Suggested path

**If you are new to spectral methods:** lessons 01 and 02 in order. Lesson 01's
Sections 2–4 are the heart: what exponential convergence looks like, where it
stops, and how it fails.

**If you already use FFTs for modelling:** start at lesson 01 §6 (the
conditioning and the round-off floor), then lesson 02 in full — the aliasing
measurements are the ones that change code.

**If you are preparing a research project:** lessons 01 §8, 02 §4.1, 03 §5 and 04
§5, plus the ★★★ exercises, which ask for measurement designs and for the
arithmetic of band and padding choices.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-spectral-methods.md`](01-spectral-methods.md) | Lesson 01 |
| [`02-pseudospectral.md`](02-pseudospectral.md) | Lesson 02 |
| [`03-spectral-elements.md`](03-spectral-elements.md) | Lesson 03 |
| [`04-spherical-harmonics-modelling.md`](04-spherical-harmonics-modelling.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 19-numerical-modeling-hpc/04-spectral-and-pseudospectral/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spectral_methods_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python pseudospectral_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spectral_elements_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spherical_harmonics_modelling_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), exits 0, and runs in well under 20 s. They
are print-only: no plots, no files, no network.

## Mastery checkpoint

Complete this without notes:

> A periodic field on a 64-point grid is advanced with a pseudospectral code, and
> its spectrum currently reaches mode 24.
> **(a)** State the highest mode a quadratic term can produce and whether the
> naive product aliases. **(b)** Compute the mode the alias folds onto and say
> whether it lies in the band the solver trusts. **(c)** State the largest input
> band the 2/3 rule permits at this $N$, whether the present solution satisfies
> it, and the padded grid size a 3/2 scheme would use. **(d)** State what happens
> to the defect if the time step is halved. **(e)** The same solution is analysed
> with 20 latitude nodes on a sphere; state what that demonstrates and what it
> does not.

A worked version of (a)–(c) appears in the
[lesson-02 solutions](exercises/02-pseudospectral-solutions.md); (e) is treated in
the [lesson-04 solutions](exercises/04-spherical-harmonics-modelling-solutions.md).

## Common pitfalls across this module

1. **Continuing a convergence table past the round-off floor.** The measured
   error rises from $6.3\times10^{-14}$ to $1.4\times10^{-13}$ between $N = 64$
   and $N = 128$; nothing improves after that.
2. **Reporting a maximum error at a kink.** It stagnates, by measurement, at the
   size of the derivative jump; the rms error converges at order $\tfrac12$.
3. **Choosing a basis by reputation.** A periodic basis on a non-periodic
   function costs a measured factor $5.6\times10^9$ at $N = 128$ against a
   Chebyshev basis.
4. **Believing a mode above Nyquist is merely inaccurate.** It is exactly equal
   to a different mode; 110 Hz *is* 10 Hz at 100 samples/s.
5. **Applying the 2/3 rule without its premise.** Measured: with an input band
   above $N/3$ the rule's error in its own trusted band is worse than the naive
   product's.
6. **Reducing the time step to cure aliasing.** The defect is in the spatial
   operator; the measured one-step error is 874% of the signal.
7. **Reading "diagonal mass matrix" as "exact mass matrix".** The off-diagonal is
   exactly zero; the diagonal is under-integrated, with a measured error of
   $2.7\times10^{-1}$ at $p=2$.
8. **Quoting a stability or resolution limit without the other.** They are
   independent constraints on the same run.
9. **Reading a smooth map as a smooth Earth.** Truncation makes maps smooth; the
   degrees above the band limit are assumptions, not measurements.

## Related modules

- [19-03 Finite Element and Finite Volume Methods](../03-finite-element-and-volume/README.md) —
  the local discretisations whose limitations spectral methods trade away.
- [19-05 Integral Equation and Boundary Methods](../05-integral-equation-and-boundary-methods/README.md) —
  another family that uses exact basis functions, for potentials rather than
  fields.
- [19-06 High-Performance and Parallel Computing](../06-hpc-and-parallel-computing/README.md) —
  transform libraries and the cost of the dense operators measured here.
- [01-10 Fourier Analysis and Spectral Methods](../../01-mathematics/10-fourier-analysis/README.md) —
  the underlying transforms and sampling theory.
- [08-01 The Earth's Magnetic Field](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/README.md) —
  a measured global field expanded in the basis of lesson 04.
- [12-01 Seismic Structure of the Earth](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/README.md) —
  the global models whose degree limits matter.
