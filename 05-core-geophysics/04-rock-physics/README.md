# Module 05-04 — Rock Physics and Property Relations

**Stages:** advanced → doctoral · **Prerequisites:** [05-01-01](../01-what-geophysics-measures/01-physical-property-contrast.md),
[05-04-01](./01-porosity-density-velocity.md) and the elasticity module
[02-04-03](../../02-physics/04-elasticity-and-continuum-mechanics/03-constitutive-laws.md).

Rock physics answers the question every other module defers: *where do the
contrasts come from?* It connects mineralogy, porosity and pore fluid to the
elastic and electrical properties that surveys measure, and it is where the
relationship between a measurement and a rock is either justified or
hand-waved.

The module's stance is uncompromising about assumptions. Every relation is
stated with the conditions under which it holds, its limits are tested
numerically, and at least one model is deliberately driven outside its
assumptions to show what failure looks like.

## Learning objectives

1. Derive the density mixing law and state which rock properties are measured
   and which are modelled.
2. Compute Voigt, Reuss, Hill and Hashin–Shtrikman bounds, and explain why the
   shear lower bounds collapse to zero for a fluid-saturated rock.
3. Perform Gassmann fluid substitution with every input stated, verify its
   limits, and use its $V_s$ prediction as a falsifiable test.
4. State the calibration range of empirical velocity–porosity relations and
   demonstrate their divergence.
5. Compute Thomsen parameters from a VTI stiffness matrix and verify them
   against an independent Christoffel solution.
6. Relate $Q$ and velocity dispersion through the Zener element and the
   Kramers–Kronig constraint.
7. Demonstrate Archie's law failing in clay-bearing rock, including a returned
   saturation greater than one.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Porosity, Density and Velocity Relationships](./01-porosity-density-velocity.md) | advanced | Density is arithmetic; velocity is not |
| 02 | [Effective-Medium Theories (Voigt, Reuss, Hashin–Shtrikman)](./02-effective-medium-theory.md) | graduate | Bounds bracket the truth; they never predict it |
| 03 | [Gassmann Fluid Substitution and Saturation Effects](./03-gassmann-fluid-substitution.md) | graduate | Exact within its assumptions, silent outside |
| 04 | [Velocity–Porosity–Clay Models](./04-velocity-porosity-clay.md) | graduate | Empirical relations carry their dataset |
| 05 | [Anisotropy in Rocks: Causes and Magnitudes](./05-anisotropy-rock.md) | doctoral | Intrinsic, structural, stress-induced — different physics |
| 06 | [Attenuation and Velocity Dispersion in Rocks](./06-attenuation-dispersion-rock.md) | doctoral | You cannot choose one without the other |
| 07 | [Electrical Properties, Archie's Law and Clay Effects](./07-electrical-properties-rock.md) | advanced | A second conduction path breaks the model |

## Materials

| Path | Contents |
|---|---|
| [`exercises/`](./exercises/) | Graded problem sets and worked solutions for all seven lessons |
| [`code/bounds_demo.py`](./code/bounds_demo.py) | Voigt/Reuss/Hill/HS, the zero-shear degeneracy, independent assembly check |
| [`code/gassmann_demo.py`](./code/gassmann_demo.py) | Gassmann limits, substitution, $V_s$ prediction, a classic misuse |
| [`code/petrophysics_demo.py`](./code/petrophysics_demo.py) | Velocity–porosity laws, Thomsen parameters, $Q$ and dispersion, Archie failure |

## How to run the demonstrations

```bash
cd /Users/miroslav/Documents/workspace/geophysics/05-core-geophysics/04-rock-physics
for f in code/*.py; do /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python "$f"; done
```

All three are offline, print labelled results with SI units, quote grid sizes and
node counts rather than timings, and exit 0. Every numeric input is printed with
the label `SYNTHETIC`.

## A note on constants

This module does **not** quote "typical" rock properties as facts. Where a
number is needed it is either derived in front of you, computed from a stated
synthetic model, or given as a range with its cause. If you need real property
values, take them from a cited compilation (for example Schön's *Physical
Properties of Rocks*) together with the range and the provenance, and report
both.

## Mastery checkpoint

**(a)** Compute Voigt, Reuss and Hashin–Shtrikman bounds for a stated
mineral–fluid mixture. **(b)** Show that the Reuss shear modulus is zero and say
what that implies. **(c)** Perform a fluid substitution, stating $K_\text{dry}$,
$K_\text{min}$, $K_\text{fl}$ and $\phi$. **(d)** State the falsifiable $V_s$
prediction and describe what its violation would tell you. **(e)** Invert an
Archie model on data generated with clay conduction and explain why
$S_w = 1.33$ is a *useful* result.

## Common pitfalls

1. Quoting a rock property without a range and a source.
2. Reporting the Reuss shear modulus of a saturated rock (it is zero).
3. Using $K_\text{sat}$ where Gassmann requires $K_\text{dry}$.
4. Extrapolating an empirical relation past its calibration.
5. Applying attenuation without the dispersion that causality requires.
6. Silently clipping an impossible saturation.

## Related modules

- [05-01 What Geophysics Measures](../01-what-geophysics-measures/README.md)
- [05-02 Fields and Observables](../02-geophysical-fields-and-observables/README.md)
- [05-03 Forward Modelling Principles](../03-forward-modelling-principles/README.md)
- [09-electrical-em-methods](../../09-electrical-em-methods/README.md)
- [04-earth-science-geology](../../04-earth-science-geology/README.md)
