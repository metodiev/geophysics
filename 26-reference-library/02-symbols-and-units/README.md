# Module 26-02 — Symbols, Units and Conventions

**Stages:** beginner → advanced · **Prerequisites:** none (lookup resource)

Four quick-reference pages. They are deliberately terse: this module exists to
be searched, not read.

## Lessons

| # | Lesson | Level | Use it for |
|---|---|---|---|
| 01 | [Symbol Handbook: Notation Used Throughout](./01-symbol-handbook.md) | beginner | Resolving which letter means what |
| 02 | [Units Handbook, Conversions and Preferred Conventions](./02-units-handbook.md) | beginner | Converting mGal, nT, Ω·m, and friends |
| 03 | [Physical Constants and Earth Parameters with Sources](./03-constant-handbook.md) | beginner | Accepted values, with uncertainty and provenance |
| 04 | [Dimensional Analysis Quick Reference](./04-dimensional-analysis-reference.md) | intermediate | Dimensions of common quantities; checking equations fast |

## Conventions adopted across this repository

Consistency matters more than which convention you pick, provided you state it.
This repository uses:

| Choice | Convention used here | Why |
|---|---|---|
| Vector notation | boldface $\mathbf{u}$; components $u_i$ | Distinguishes vectors from scalars clearly in plain text |
| Tensor notation | $C_{ijkl}$, with Einstein summation over repeated indices | Standard in elasticity and continuum mechanics |
| Angular frequency | $\omega = 2\pi f$ | Separates the two uses explicitly: $\omega$ in rad/s, $f$ in Hz |
| Wavenumber | $k = 2\pi/\lambda$ | Consistent with $\omega$; $\omega = ck$ then holds exactly |
| Fourier transform sign | $e^{-i\omega t}$ for the forward transform | Physics convention; avoids sign errors in dispersion relations |
| Gravity anomaly sign | positive for excess mass | Matches gravitational acceleration magnitude convention |
| Magnetic field symbols | $\mathbf{B}$ for flux density (tesla), $\mathbf{H}$ for field strength (A/m) | Avoids the $\mathbf{B}$/$\mathbf{H}$ confusion endemic in geophysics |
| Depth coordinate | $z$ positive downward | Matches the gravity/geodesy convention, so $g_z = -\partial V/\partial z$ |
| Time unit | SI seconds in equations; Ma/Ga only for geological durations | Prevents unit-mixing errors |

**Where this repository knowingly diverges from subfield practice**, the lesson
that introduces the topic says so explicitly. Two examples you will meet:

1. **Seismology** often writes displacement as $\mathbf{u}$ and also uses $u$
   for slowness in ray theory. Context disambiguates; both are flagged when they
   first appear.
2. **Potential-field geophysics** frequently reports the *vertical* component of
   the field with a sign convention that makes anomalies over excess mass
   positive. Gravitational acceleration itself points toward the mass. The
   lesson states which convention it uses.

## Mastery checkpoint

This module has no checkpoint — it is a reference. The relevant skill is simply:
**know that it is here**, so you look up a conversion rather than guessing one.

## Related lessons

- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md) — the teaching treatment of this material.
- [01-01-01 Number Systems, Precision and Scientific Notation](../../01-mathematics/01-arithmetic/01-number-systems-and-precision.md) — how to write the numbers.
