---
id: 05-04-03
title: "Gassmann Fluid Substitution and Saturation Effects"
level: graduate
prereqs: ["05-04-02"]
tags: [gassmann, fluid-substitution, saturation, poroelasticity]
---

# Gassmann Fluid Substitution and Saturation Effects

## Learning objectives

1. **State** Gassmann's equation, name every symbol with its unit, and state
   each assumption.
2. **Verify** the equation against its three exact limits.
3. **Perform** a fluid substitution from measured/modelled dry-frame properties
   and report the velocity changes.
4. **Derive** the falsifiable prediction that $V_s$ changes only through density,
   and explain what a violation implies.
5. **Identify** the misuse of using a saturated modulus where the dry modulus is
   required, and quantify the error.

## Prerequisites

- [05-04-02 Effective-Medium Theories](./02-effective-medium-theory.md)
- [02-06-05 Flow in Porous Media](../../02-physics/06-fluid-mechanics/05-porous-media-flow.md)

## 1. Intuition

At low frequency the pore fluid has time to equilibrate its pressure throughout
the connected pore space. Then the fluid's only elastic role is to resist
*volume* change, and its contribution depends on the fluid's bulk modulus, the
mineral's bulk modulus, the porosity and the dry-frame stiffness — but not on
the pore geometry. Gassmann's equation is that statement made precise, and it is
remarkable for what it does not need. It is equally remarkable for what it
assumes away, and every failure of Gassmann is a failure of one of those
assumptions.

## 2. Gassmann's equation

$$K_\text{sat} = K_\text{dry} + \frac{\left(1 - K_\text{dry}/K_\text{min}\right)^2}
{\dfrac{\phi}{K_\text{fl}} + \dfrac{1-\phi}{K_\text{min}}
- \dfrac{K_\text{dry}}{K_\text{min}^2}},
\qquad G_\text{sat} = G_\text{dry}.$$

| Symbol | Meaning | Unit |
|---|---|---|
| $K_\text{sat}$ | saturated bulk modulus | Pa |
| $K_\text{dry}$ | dry-frame bulk modulus | Pa |
| $K_\text{min}$ | mineral (grain) bulk modulus | Pa |
| $K_\text{fl}$ | pore-fluid bulk modulus | Pa |
| $G_\text{dry}$ | dry-frame shear modulus | Pa |
| $\phi$ | porosity | dimensionless |

Dimensional check: the numerator is dimensionless and squared; the denominator
is $1/\mathrm{Pa}$, so the fraction is in Pa, matching $K_\text{sat}$. ✓

Velocities then follow from the density law of
[05-04-01](./01-porosity-density-velocity.md):

$$V_p = \sqrt{\frac{K_\text{sat}+\frac43G_\text{sat}}{\rho_\text{sat}}},
\qquad V_s = \sqrt{\frac{G_\text{sat}}{\rho_\text{sat}}}.$$

For a mixed fluid, $1/K_\text{fl} = \sum_i S_i/K_i$ (Wood's equation, which is
itself an isostress average and assumes uniform pressure — hence the name
"uniform saturation").

## 3. Exact limits (any correct implementation must satisfy these)

**(a) $K_\text{fl} = K_\text{min}$.** The pore fluid *is* the mineral, so the
rock is homogeneous and $K_\text{sat} = K_\text{min}$ for every $\phi$.
Measured: with $K_\text{min} = 37$ GPa and $\phi = 0.20$, the computed
$K_\text{sat} = 37.000000000$ GPa, relative difference $0.00\times10^{0}$.

**(a') $K_\text{fl}\to\infty$.** An incompressible fluid bearing load through the
pores gives a $K_\text{sat}$ *above* $K_\text{min}$. Measured for the same
frame: $K_\text{sat} = 48.591087$ GPa at $K_\text{fl} = 10^{3}$ GPa and
$49.333333$ GPa at $10^{9}$ GPa. This surprises students; it is correct, and it
shows that a bulk modulus is not bounded by its constituents' moduli.

**(b) $K_\text{fl}\to0$.** A vacuum-filled frame is the dry frame. Measured
$K_\text{sat} = 18.500001$ GPa against $K_\text{dry} = 18.500000$ GPa.

**(c)** $G_\text{sat} = G_\text{dry}$ by construction.

*Note on framing.* Limit (a) must be tested at $K_\text{fl} = K_\text{min}$
exactly. Testing "very large $K_\text{fl}$" instead tests limit (a'), which gives
a different answer — a mistake worth making once, deliberately.

## 4. Assumptions

1. **Low frequency.** Pore pressure is equilibrated (the "undrained" or relaxed
   limit). Fails when the wave period approaches the pore-fluid diffusion time.
2. **Homogeneous, isotropic, linearly elastic mineral.**
3. **Connected, uniformly distributed pore fluid.** Patchy saturation violates
   this and produces velocities above Gassmann's prediction.
4. **No chemical interaction** between fluid and frame (no softening clays).
5. **Known $K_\text{dry}$.** In practice this is the weakest link: it is either
   measured on a dry core or back-calculated from a saturated measurement, and
   the back-calculation inverts the same equation, so errors propagate.

## 5. Worked example: substitution with every input stated

Stated SYNTHETIC inputs: $K_\text{min} = 37$ GPa, $G_\text{min} = 44$ GPa,
$\rho_\text{min} = 2650$ kg/m³; dry-frame law
$K_\text{dry} = K_\text{min}(1-\phi/\phi_c)$, $G_\text{dry} = G_\text{min}
(1-\phi/\phi_c)$ with $\phi_c = 0.40$; $\phi = 0.20$, hence $K_\text{dry} = 18.50$
GPa, $G_\text{dry} = 22.00$ GPa. Fluid A: $K = 2.2$ GPa, $\rho = 1000$ kg/m³.
Fluid B: $K = 0.05$ GPa, $\rho = 200$ kg/m³.

| | fluid A | fluid B | change |
|---|---|---|---|
| $K_\text{sat}$ (GPa) | 21.0248 | 18.5624 | $-11.712\%$ |
| $\rho_\text{sat}$ (kg/m³) | 2320.0 | 2160.0 | — |
| $V_p$ (m/s) | 4659.0 | 4708.9 | $+1.072\%$ |
| $V_s$ (m/s) | 3079.4 | 3191.4 | $+3.638\%$ |

Note the signs: substituting a **softer and much lighter** fluid *reduces* the
modulus but *increases both velocities* here, because the density reduction
dominates at this porosity. A naive expectation of "gas lowers $V_p$" is not
universally true — it depends on porosity and on the specific fluids.

**Porosity dependence** (dry frame recomputed at each porosity, so these are
physically distinct rocks):

| $\phi$ | $K_\text{dry}$ (GPa) | $\Delta V_p/V_p$ | $\Delta V_s/V_s$ |
|---|---|---|---|
| 0.02 | 35.15 | $+0.171\%$ | $+0.307\%$ |
| 0.10 | 27.75 | $+0.789\%$ | $+1.650\%$ |
| 0.20 | 18.50 | $+1.072\%$ | $+3.638\%$ |
| 0.35 | 4.63 | $-7.698\%$ | $+7.527\%$ |

The effect grows steeply with porosity, and the sign of the $V_p$ change flips.

## 6. The falsifiable $V_s$ prediction

Gassmann says $G$ does not change, so

$$\frac{V_s^\text{sat}}{V_s^\text{dry}} = \sqrt{\frac{\rho_\text{dry}}
{\rho_\text{sat}}}.$$

Measured for the stated case: 0.955925 (fluid A) and 0.990697 (fluid B).
**If a laboratory or borehole measurement shows additional $V_s$ softening, one
of Gassmann's assumptions is violated** — usually patchy saturation, clay
softening, or high frequency. The size of the excess is a diagnostic of the
mechanism, which is more useful than the failure itself.

## 7. Classic misuse

Gassmann's first argument is the **dry-frame** modulus. Passing the *saturated*
modulus inflates the predicted change: measured $K_\text{sat} = 21.0713$ GPa and
$V_p = 4830.7$ m/s instead of 18.5624 GPa and 4708.9 m/s, errors of $+13.52\%$
in $K_\text{sat}$ and $+2.59\%$ in $V_p$. The error grows with porosity and with
the fluid contrast.

## 8. Python demonstration

Run `code/gassmann_demo.py`. Five sections: the limits, the substitution, the
$V_s$ prediction, the misuse, and the porosity sweep.

## 9. Exercises, mistakes, applications

Exercises: [`exercises/03-gassmann-fluid-substitution-exercises.md`](./exercises/03-gassmann-fluid-substitution-exercises.md).

**Common mistakes.** (1) Using $K_\text{sat}$ as $K_\text{dry}$.
(2) Applying Gassmann at ultrasonic frequencies without acknowledging the
dispersion. (3) Using Wood's equation for patchy saturation. (4) Treating
$K_\text{fl}$ as a constant of the fluid type when it varies strongly with
pressure, temperature and gas fraction. (5) Assuming Gassmann predicts a
decrease in $V_p$ on gas substitution at all porosities.

**Applications.** 4-D seismic feasibility studies; time-lapse interpretation
(saturation versus pressure changes); rock-physics templates for lithology and
fluid discrimination; log-to-seismic ties.

## Extended worked example: recovering the dry frame, then substituting

In practice you rarely have $K_\text{dry}$; you have a *saturated* measurement
and you must invert Gassmann before you can substitute anything.

Take the stated synthetic rock of Section 5 at $\phi = 0.20$ with fluid A:
$K_\text{sat} = 21.0248$ GPa, $K_\text{min} = 37$ GPa,
$K_\text{fl} = 2.2$ GPa. Solving the Gassmann relation for $K_\text{dry}$ gives

$$K_\text{dry} = \frac{K_\text{sat}\left(\dfrac{\phi K_\text{min}}{K_\text{fl}}
+ 1-\phi\right) - K_\text{min}}{\dfrac{\phi K_\text{min}}{K_\text{fl}}
+ \dfrac{K_\text{sat}}{K_\text{min}} - 1 - \phi}.$$

**Numerator:** $\phi K_\text{min}/K_\text{fl} = 0.2\cdot37/2.2 = 3.363636$;
$+1-\phi = +0.8$ gives 4.163636; times $K_\text{sat} = 21.0248$ gives 87.53962;
minus $K_\text{min} = 37$ gives 50.53962 (all in GPa).

**Denominator:** $3.363636 + 21.0248/37 - 1 - 0.2 = 3.363636 + 0.568238 - 1.2
= 2.731874$.

**Result:** $K_\text{dry} = 50.53962/2.731874 = 18.5000$ GPa — recovering exactly
the value used to generate the measurement. This round-trip is the standard
sanity check for a substitution workflow: forward-model, invert, and confirm you
recover the input. If you do not, either the algebra or the assumed
$K_\text{min}$, $\phi$ or $K_\text{fl}$ is inconsistent.

**Why the round-trip is not enough.** It confirms the implementation, not the
physics. A perfectly implemented Gassmann inversion on a core measurement taken
at ultrasonic frequency will still give a $K_\text{dry}$ that is not the
low-frequency frame modulus, because the measurement itself violates the
low-frequency assumption. That is why laboratory protocols specify the
frequency and why ultrasonic-derived dry moduli are used with caution.

**The sensitivity that matters.** The substitution result is most sensitive to
$K_\text{fl}$ of the *new* fluid and to $\phi$. For a gas, $K_\text{fl}$ varies
strongly with pressure and temperature and with the exact composition; a factor
of two error in $K_\text{fl}$ for a soft phase moves $K_\text{sat}$ by several
percent, which is the same order as the effect being modelled. **Always state
the fluid moduli, their source, and their uncertainty**, not just the fluid
"type".

## 10. Further reading

- **Gassmann, F. (1951).** Über die Elastizität poröser Medien.
  *Vierteljahrsschrift der Naturforschenden Gesellschaft in Zürich* 96, 1–23.
  Level: graduate. The original.
- **Mavko, Mukerji & Dvorkin, *The Rock Physics Handbook*.** Chapter 6. Level:
  graduate.
- **Smith, T. M., Sondergeld, C. H. & Rai, C. S. (2003).** Gassmann fluid
  substitutions: a tutorial. *Geophysics* 68, 430–440. Level: graduate.

## 11. Related lessons

- [05-04-02 Effective-Medium Theories](./02-effective-medium-theory.md)
- [05-04-04 Velocity-Porosity-Clay Models](./04-velocity-porosity-clay.md)
- [05-04-06 Attenuation and Velocity Dispersion](./06-attenuation-dispersion-rock.md)

## Self-assessment checklist

- [ ] I can write Gassmann's equation and name every unit.
- [ ] I can verify the three exact limits and explain limit (a').
- [ ] I can perform a substitution with all inputs stated.
- [ ] I can state the $V_s$ prediction and what its violation implies.
- [ ] I can quantify the error from using $K_\text{sat}$ as $K_\text{dry}$.
