---
id: 23-06-07
title: "Rock Mechanics Testing: Strength, Friction, Fracture"
level: research
prereqs: ["23-06-02", "02-04-08"]
estimated_minutes: 115
tags: [laboratory, rock-mechanics, strength, friction, fracture, triaxial, brittleness]
---

# Rock Mechanics Testing: Strength, Friction, Fracture

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a secant modulus and a Poisson's ratio from a stress–strain record, and
   **correct** both for the testing machine's compliance.
2. **Fit** a Mohr-Coulomb criterion to triaxial peak strengths, **inspect** the residuals,
   and **convert** the fit into a friction angle and a cohesion.
3. **Apply** Byerlee's law to a stress state and **compute** the stress ratio that
   reactivates a critically oriented fault.
4. **Compute** a brittleness index and **locate** the brittle–ductile transition from the
   confining-pressure dependence of peak and residual strength.
5. **Compute** the strain-rate and size effects on strength, and **state** which is larger.
6. **State** what must accompany every strength number for it to be comparable.

All strengths, moduli, strains, stresses and coefficients here are **SYNTHETIC** teaching
values combined with the standard relations quoted in the text (linear elasticity, the
Mohr-Coulomb criterion and its conversion to $c$ and $\phi$, Byerlee's friction law, the
compliance of an elastic machine, rate-dependent friction, a power-law size effect). No
laboratory standard, instrument specification or measured rock property is reproduced.

## Prerequisites

- [02 Ultrasonic Velocity Measurement and Pressure Dependence](02-ultrasonic-velocity.md) —
  the dynamic moduli these static tests are compared with.
- [02-04-08 Rock Failure, Fracture and Rate-State Friction](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md) —
  the failure theory the measurements calibrate.

## 1. Intuition: a strength test measures the machine as much as the rock

A rock-mechanics test applies a load and measures a displacement, so the record contains
three contributions: the rock's deformation, the machine's compliance, and the load train's
(specimen ends, spherical seat, load cell). The first is what is wanted and the other two are
usually of the same order:

- a **soft frame** makes a stiff rock look compliant (here a machine at 5000 kN/mm gives an
  apparent modulus 9.0 % low);
- the **strain rate** and the **specimen size** both change the measured strength, the size
  effect by far the more;
- the **confining pressure** changes peak strength, residual strength and, above a
  transition, the entire mode of failure.

The design consequence is that a strength number is a **procedure**, not a property, until
the machine stiffness, the specimen geometry, the strain rate, the confinement and the
saturation are stated. Everything in this lesson is the arithmetic of those statements.

## 2. Moduli and the machine compliance

From a uniaxial test, the secant (or tangent) modulus is $\Delta\sigma/\Delta\varepsilon$
over a chosen interval — the interval is part of the definition. For a synthetic record of
0–40 MPa over 0–1.1429 × 10⁻³ axial strain, the secant modulus is **34.999 GPa**, and a
lateral/axial strain ratio of 0.2500 gives $\nu = 0.2500$.

But the measured displacement is the specimen's *plus* the machine's, so

$$\frac{1}{E_{\text{app}}} = \frac{1}{E} + \frac{A}{K_m L} ,$$

with $A$ the specimen area, $L$ its length and $K_m$ the machine stiffness:

| Machine stiffness | Apparent $E$ | Error |
|---|---|---|
| 10 000 kN/mm | 33.351 GPa | −4.7 % |
| 5 000 kN/mm | 31.850 GPa | −9.0 % |
| 2 000 kN/mm | 28.063 GPa | −19.8 % |
| 1 000 kN/mm | 23.421 GPa | −33.1 % |

Three conclusions:

1. **The error is one-signed and systematic**, so it is not reduced by repeating the test; it
   is reduced by measuring $K_m$ (a test on a steel or aluminium specimen of known modulus)
   and correcting.
2. **The correction matters most for short, large specimens**, because $A/(K_mL)$ grows as
   $L$ falls — the same geometry argument as the ultrasonic end effect.
3. **The machine compliance also contaminates the post-peak branch**, where it determines
   whether a violent failure is recorded as a violent drop or as a controlled one. A soft
   machine can make a brittle rock appear ductile, and the reported post-peak slope is then
   a property of the frame.

## 3. Triaxial peak strength and Mohr-Coulomb

The Mohr-Coulomb criterion in principal stresses is linear:

$$\sigma_1 = \text{UCS} + q\sigma_3, \qquad
q = \frac{1+\sin\phi}{1-\sin\phi} ,$$

so a set of peak strengths at different confining pressures gives $\phi$ from the slope and
the uniaxial compressive strength from the intercept. For the synthetic tests
$\sigma_3 = 5, 20, 50$ MPa with $\sigma_1 = 60, 105, 180$ MPa:

| $\sigma_3$ (MPa) | $\sigma_1$ peak (MPa) | Fitted | Residual |
|---|---|---|---|
| 5.0 | 60.0 | 62.14 | −2.14 |
| 20.0 | 105.0 | 101.79 | +3.21 |
| 50.0 | 180.0 | 181.07 | −1.07 |

giving $q = 2.6429$, UCS $= 48.9286$ MPa, and hence

$$\phi = \arcsin\left(\frac{q-1}{q+1}\right) = 26.81^\circ, \qquad
c = \frac{\text{UCS}(1-\sin\phi)}{2\cos\phi} = 15.0486\ \mathrm{MPa} .$$

The important observations, all visible in the three residuals:

1. **The residuals alternate in sign**, which is the honest signature of *scatter* rather
   than of a wrong model — but with three points a curvature cannot be excluded, and the
   line is an extrapolation to $\sigma_3 = 0$. Four or five confining pressures are the
   minimum for a defensible fit, and the residual plot belongs in the report.
2. **$c$ and $\phi$ are correlated.** A steeper slope with the same intercept is a larger
   $\phi$ and a smaller $c$; the pair forms a covariance ellipse, and quoting both without
   their correlation overstates the precision of either.
3. **The criterion is a *peak* criterion.** The residual strength follows a different
   (usually steeper) line, and for design the residual is often the governing one, because a
   failed rock mass retains residual strength rather than losing all of it.

## 4. Friction: Byerlee's law and reactivation

For sliding on an existing surface, the empirical observation known as Byerlee's law is
approximately

$$\tau = 0.85\sigma_n \quad (\sigma_n \lesssim 200\ \mathrm{MPa}), \qquad
\tau = 50 + 0.6\sigma_n \quad (\text{higher normal stress}) ,$$

with $\sigma_n$ the *effective* normal stress:

| $\sigma_n$ (MPa) | $\tau$ (MPa) | $\tau/\sigma_n$ |
|---|---|---|
| 5 | 4.25 | 0.8500 |
| 10 | 8.50 | 0.8500 |
| 50 | 42.50 | 0.8500 |
| 200 | 170.00 | 0.8500 |
| 400 | 290.00 | 0.7250 |
| 800 | 530.00 | 0.6625 |

The friction coefficient is remarkably **constant** across minerals, rock types and
laboratory conditions, which is why it can be used as a first-order constraint on field
stress states. Its consequence is a reactivation *criterion* in terms of a stress ratio: for
a critically oriented plane, $\tau/\sigma_n = (\sigma_1-\sigma_3)/(\sigma_1+\sigma_3)$, so
the ratio required to slip is

$$\frac{\sigma_1}{\sigma_3} > \frac{1+\mu}{1-\mu} ,$$

| $\sigma_1/\sigma_3$ | $\tau/\sigma_n$ | Reactivated? |
|---|---|---|
| 3.0 | 0.5000 | no |
| 5.0 | 0.6667 | no |
| 8.0 | 0.7778 | no |
| 12.3 | 0.8500 | at the limit |
| 15.0 | 0.8750 | yes |
| 20.0 | 0.9048 | yes |

so a differential stress ratio of about **12.3** is needed for reactivation with
$\mu = 0.85$ — a large ratio, and the reason pore pressure matters so much: it reduces the
*effective* normal stress while the shear stress is unchanged, so a ratio that is safe dry
can reactivate when the pore pressure rises. The correct field statement is therefore in
terms of effective stress, and the friction coefficient alone does not predict whether a
fault slips — the stress state does.

## 5. Post-peak behaviour and the brittle–ductile transition

With a synthetic peak $180 - 0.4\sigma_3$ and residual $60 + 0.55\sigma_3$:

| $\sigma_3$ (MPa) | Peak | Residual | Drop | Brittleness index |
|---|---|---|---|---|
| 0 | 180.00 | 60.00 | 120.00 | 0.6667 |
| 10 | 176.00 | 65.50 | 110.50 | 0.6278 |
| 25 | 170.00 | 73.75 | 96.25 | 0.5662 |
| 50 | 160.00 | 87.50 | 72.50 | 0.4531 |
| 100 | 140.00 | 115.00 | 25.00 | 0.1786 |
| 200 | 100.00 | 170.00 | −70.00 | negative |

The peak and residual lines meet at

$$\sigma_3^{*} = \frac{180-60}{0.4+0.55} = 126.32\ \mathrm{MPa} ,$$

above which a "brittleness index" is meaningless (the drop is negative, i.e. the material
work-hardens) and the failure criterion becomes a **yield envelope** rather than a peak
strength. Three practical rules follow:

1. **Report the confinement band with every strength number.** A strength without a
   confinement range is a number from an unknown part of the curve.
2. **Define the brittleness index and state the definition**, since several are in use
   (the drop over the peak, a ratio of elastic to total strain, and others) and they do not
   agree numerically.
3. **The transition is a property of the mineralogy, the porosity and the temperature**, so
   a laboratory transition at 126 MPa does not transfer to a 10 km depth at 300 °C without
   the corresponding high-temperature tests.

## 6. Strain rate and size: the two numbers that must be stated

Friction and strength are rate-dependent, approximately as

$$\Delta\tau = a\,\sigma_{\text{eff}}\ln\frac{V}{V_0} ,$$

with $a \approx 0.01$ a typical value:

| Rate ratio | $\Delta\tau$ at $\sigma_{\text{eff}} = 50$ MPa | $\Delta\tau/\sigma_{\text{eff}}$ |
|---|---|---|
| 2 | 0.3466 MPa | 0.00693 |
| 10 | 1.1513 MPa | 0.02303 |
| 100 | 2.3026 MPa | 0.04605 |
| 1000 | 3.4539 MPa | 0.06908 |

so a **10× rate change is about 1.2 MPa** — significant, but small compared with the
strength itself. The **size effect** is not:

| Size ratio | Strength ratio (power −0.20) |
|---|---|
| 2 | 0.8706 |
| 5 | 0.7248 |
| 10 | 0.6310 |
| 50 | 0.4573 |

A **10× larger specimen is 37 % weaker**: a laboratory plug strength is therefore not the
strength of a rock mass, and the difference is not a correction factor that can be looked up
but a scale-dependent extrapolation that must be argued. The two effects are therefore of
very different sizes, and both must be stated — together with the geometry, the end
condition (lubricated or not) and the saturation, which changes strength by tens of percent
in porous rocks.

## 7. Assumptions and regime of validity

1. **The specimen is homogeneous and isotropic.** A core with a bedding plane, a vein or a
   fracture measures that feature's orientation as much as the rock.
2. **The stress state is uniform in the specimen.** End friction (barrelling), non-parallel
   ends and a poorly centred load train all break it, and all are common.
3. **The strain measurement excludes the machine.** Otherwise the elastic moduli are wrong by
   tens of percent.
4. **The failure criterion is linear in $\sigma_1$–$\sigma_3$.** Real rocks curve it, and a
   linear fit over a wide confinement range is a model choice.
5. **The pore fluid is controlled.** Effective stress requires the pore pressure to be known
   and held; a saturated specimen tested drained and one tested undrained are different
   materials.
6. **The temperature is the in-situ temperature, or the difference is accounted for.**
   Strength falls with temperature, and the strongest rocks in a basin are the cool ones.
7. **The strain rate is stated and comparable.** Rate effects are small but systematic, and
   a dynamic test (a split-Hopkinson or a seismic-frequency measurement) is not comparable
   with a quasi-static one.

## 8. The honest summary

- A strength test measures the machine as well as the rock: a 5000 kN/mm frame makes a
  34.999 GPa rock read as 31.850 GPa, a −9.0 % systematic error.
- Three triaxial tests gave $q = 2.6429$, UCS $= 48.9286$ MPa, $\phi = 26.81^\circ$ and
  $c = 15.0486$ MPa, with alternating residuals that are consistent with scatter but cannot
  exclude curvature.
- Byerlee's law is $\tau = 0.85\sigma_n$ below 200 MPa; it predicts reactivation at
  $\sigma_1/\sigma_3 \approx 12.3$, which is why pore pressure, not friction, decides whether
  a fault slips.
- The brittleness index falls from 0.6667 at zero confinement to 0.1786 at 100 MPa and turns
  negative at the transition, $\sigma_3^{*} = 126.32$ MPa, where the criterion becomes a
  yield envelope.
- A 10× rate change is 1.2 MPa; a 10× size change is a 37 % strength reduction.
- Every strength number needs its confinement, rate, size, saturation, temperature and
  machine.

## 9. Python demonstration

[`code/rock_mechanics_demo.py`](./code/rock_mechanics_demo.py) prints every number quoted
above: the modulus and Poisson's ratio with a machine-compliance table, the triaxial fit with
its residuals and the conversion to $c$ and $\phi$, Byerlee's law with the reactivation
ratios, the brittleness table and the brittle–ductile transition, and the rate and size
effects.

```bash
cd 23-field-methods-instruments/06-laboratory-measurements/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rock_mechanics_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/07-rock-mechanics-lab-exercises.md`](./exercises/07-rock-mechanics-lab-exercises.md)
and
[`exercises/07-rock-mechanics-lab-solutions.md`](./exercises/07-rock-mechanics-lab-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A synthetic uniaxial record gives 25 MPa at 0.8 × 10⁻³ axial strain. Compute the secant
   modulus, and the apparent modulus for a machine stiffness of 4000 kN/mm with
   $A = 1.13\times10^{-3}$ m² and $L = 0.080$ m.
2. Triaxial peaks are 80, 130 and 200 MPa at $\sigma_3 = 5, 25, 60$ MPa. Fit the line, compute
   $q$, $\phi$ and the UCS, then the cohesion.
3. Compute $\tau$ for $\sigma_n = 30$ and 500 MPa with Byerlee's law.
4. Compute the $\sigma_1/\sigma_3$ ratio needed for reactivation with $\mu = 0.6$, and state
   what a rise in pore pressure does to it.
5. A 5× larger specimen and a 20× faster test: compute both effects for $a\sigma_{\text{eff}}
   = 0.5$ MPa.

## 12. Common pitfalls

1. **Quoting a modulus without the machine compliance.** It is a systematic, one-signed error.
2. **Fitting a linear criterion to three points and calling it the rock's friction angle.**
   Check the residuals and the confinement range.
3. **Quoting $\phi$ and $c$ without their correlation.** They trade off against each other.
4. **Using peak strength where residual strength governs.** A failed rock still carries load.
5. **Ignoring the size effect.** A plug is not a rock mass.
6. **Comparing a quasi-static test with a dynamic one.** Different rates, different strengths.
7. **Forgetting the saturation and the temperature.** Both change strength by tens of percent.

## 13. Where this is used

- Geomechanical models for wells, tunnels, slopes and storage, where the strength parameters
  are the inputs — see
  [02-04-08 Rock Failure, Fracture and Rate-State Friction](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md).
- Earthquake mechanics, where the friction coefficient and the rate dependence constrain
  whether a fault slips seismically or aseismically.
- Caprock and seal integrity, where reactivation is the question and the effective stress is
  the variable.
- Any comparison of laboratory strength with field behaviour, which requires the size, rate,
  saturation and temperature statements of §6–§7.

## 14. Related lessons

- [02 Ultrasonic Velocity Measurement and Pressure Dependence](02-ultrasonic-velocity.md) —
  the dynamic moduli that the static moduli are compared with.
- [03 Laboratory Density, Porosity and Permeability Measurement](03-density-porosity-lab.md) —
  the porosity that controls both the strength and the elastic moduli.
- [01 Sample Preparation, Coring and Drying Protocols](01-sample-preparation.md) —
  the geometry and end condition the strength depends on.
- [08 Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md) —
  how the systematic terms here are reported.

## 15. Self-assessment checklist

- [ ] I can compute a secant modulus and a Poisson's ratio from a record.
- [ ] I can correct a modulus for machine compliance.
- [ ] I can fit Mohr-Coulomb, inspect the residuals and convert to $c$ and $\phi$.
- [ ] I can apply Byerlee's law and compute a reactivation ratio.
- [ ] I can compute a brittleness index and locate the ductile transition.
- [ ] I can compute the rate and size effects and say which is larger.
- [ ] I can list everything that must accompany a strength number.
