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

### 3.1 The Biot–Willis form, derived from the standard form

Gassmann's equation appears in two forms in the literature, and they are the same
equation. Showing the equivalence is worth the four lines, because the second
form displays the physics.

Start from the standard form,

$$K_\text{sat} = K_\text{dry} +
\frac{\left(1-K_\text{dry}/K_\text{min}\right)^2}
{\dfrac{\phi}{K_\text{fl}} + \dfrac{1-\phi}{K_\text{min}}
- \dfrac{K_\text{dry}}{K_\text{min}^2}} .$$

Define the **Biot–Willis coefficient**

$$\alpha \equiv 1 - \frac{K_\text{dry}}{K_\text{min}},$$

so that $\alpha = 0$ when the frame is as stiff as the mineral (no pore space
contributes) and $\alpha \to 1$ for a very compliant frame. Now manipulate the
last two denominator terms:

$$\frac{1-\phi}{K_\text{min}} - \frac{K_\text{dry}}{K_\text{min}^2}
= \frac{1}{K_\text{min}}\left(1-\phi-\frac{K_\text{dry}}{K_\text{min}}\right)
= \frac{1}{K_\text{min}}\left[\left(1-\frac{K_\text{dry}}{K_\text{min}}\right)
- \phi\right]
= \frac{\alpha-\phi}{K_\text{min}} .$$

The denominator becomes $\phi/K_\text{fl} + (\alpha-\phi)/K_\text{min}$ and the
numerator is $\alpha^2$, so

$$\boxed{\;K_\text{sat} = K_\text{dry}
+ \frac{\alpha^2}{\dfrac{\phi}{K_\text{fl}}
+ \dfrac{\alpha-\phi}{K_\text{min}}}\;}$$

**Numerical check.** For three stated cases
($K_\text{dry}, \phi$) = (18.5 GPa, 0.20), (12.0 GPa, 0.35), (30.0 GPa, 0.10)
with $K_\text{min} = 37$ GPa and $K_\text{fl} = 2.2$ GPa, the two forms agree to
nine decimal places: 21.024813896, 12.065137753 and 30.602409639 GPa. The
algebra is exact.

**Physical interpretation.** The second form displays the structure: the rock's
stiffness is the frame's stiffness plus a term proportional to $\alpha^2$, the
square of the pore-pressure coupling. The denominator is a *slowness-like*
combination of two compliances, the fluid's and the pore-space's. Two limits are
immediate by inspection:

- $K_\text{fl} \to 0$: the denominator diverges, the correction vanishes, and
  $K_\text{sat}\to K_\text{dry}$ — the vacuum-filled frame;
- $K_\text{fl} = K_\text{min}$: with $K_\text{dry} = K_\text{min}(1-\alpha)$ the
  bracket becomes $(\alpha-\phi)/K_\text{min}+\phi/K_\text{min} = \alpha/K_\text{min}$,
  so the correction is $\alpha^2K_\text{min}/\alpha = \alpha K_\text{min}$, giving
  $K_\text{sat} = K_\text{min}(1-\alpha)+\alpha K_\text{min} = K_\text{min}$ ✓,
  reproducing the exact limit of Section 3.

### 3.2 Wood's equation, derived as an isostress average

The fluid modulus $K_\text{fl}$ of a mixture of immiscible fluids is not a
volume average of their moduli. It is the **Reuss** (isostress) average, and the
reason is that pore pressure must be common to all phases in contact.

Apply a uniform pressure change to a mixture of fractions $S_i$ with moduli
$K_i$. Each phase is in parallel *for volume change*, so the volume strains add
weighted by fraction, and the effective compliance is the weighted mean
compliance:

$$\frac{\Delta V}{V} = \sum_i S_i\frac{\Delta V_i}{V_i}
= -\Delta p\sum_i \frac{S_i}{K_i}
\qquad\Longrightarrow\qquad
\frac{1}{K_\text{fl}} = \sum_i \frac{S_i}{K_i} .$$

Dimensional check: each term is Pa⁻¹ ✓. This is exactly the Reuss expression of
[05-04-02](./02-effective-medium-theory.md), applied to the fluid, and it has the
same character: **a small amount of a very compressible phase dominates.** With
$S_w = 0.5$, $K_w = 2.2$ GPa and $K_h = 0.05$ GPa,

$$\frac{1}{K_\text{fl}} = \frac{0.5}{2.2}+\frac{0.5}{0.05}
= 0.22727+10.0 \ \mathrm{GPa^{-1}} = 10.2273\ \mathrm{GPa^{-1}},
\qquad K_\text{fl} = 0.0978\ \mathrm{GPa}.$$

**The lesson.** A 50% gas saturation drops the fluid modulus from 2.2 GPa to
0.098 GPa — a factor of 22 — even though half the pore volume is still brine.
Gassmann then responds to $K_\text{fl}$, so the elastic effect of a small gas
fraction is disproportionately large. This is why a few percent of free gas is
detectable seismically, and why saturation estimates from seismic amplitudes are
poorly conditioned in the gas range: $K_\text{fl}$ is nearly flat in $S_g$ over
a wide interval, so many saturations map to almost the same modulus.

### 3.3 When the low-frequency assumption fails, derived

Gassmann assumes the pore pressure is equilibrated over the wave period. That
requires the fluid to diffuse across the relevant pore or patch distance within a
period. The relevant diffusivity is (a Darcy-scale result)

$$D = \frac{k\,K_\text{fl}}{\mu\,\phi},$$

with $k$ permeability, $\mu$ fluid viscosity. Dimensional check:
$\mathrm{m^2\cdot Pa/(Pa\,s)} = \mathrm{m^2\,s^{-1}}$ ✓.

**Numbers.** $k = 10^{-14}$ m², $K_\text{fl} = 2.2$ GPa, $\mu = 10^{-3}$ Pa s,
$\phi = 0.2$:

$$D = \frac{10^{-14}\cdot2.2\times10^{9}}{10^{-3}\cdot0.2} = 0.11\ \mathrm{m^2\,s^{-1}},$$

so the equilibration time over a patch of length $L = 0.1$ m is
$t \sim L^2/D = 0.091$ s, and equilibration holds for periods
$T \gg 0.09$ s, i.e. **frequencies below about 11 Hz**.

**Physical interpretation and consequence.** Above that frequency the pore
pressure is not equilibrated, the rock is stiffer than Gassmann predicts, and
measured $V_p$ exceeds the Gassmann value. Laboratory ultrasonic measurements
(10⁵–10⁶ Hz) are therefore in the *unrelaxed* regime, and back-calculating a
"dry-frame modulus" from them gives a quantity that is not the low-frequency
frame modulus that field seismic needs. **The bias is systematic, not random, and
it grows with frequency and with patch size.** The honest statement of a
substitution result includes the frequency band it applies to.

### 3.4 Why the fluid modulus matters most at low porosity — or seems to

The Biot–Willis form of Section 3.1 shows the fluid entering only through the
combination $\phi/K_\text{fl}$:

$$K_\text{sat} = K_\text{dry} + \frac{\alpha^2}
{\dfrac{\phi}{K_\text{fl}} + \dfrac{\alpha-\phi}{K_\text{min}}} .$$

That single observation explains a result that otherwise looks paradoxical.

**The structure.** When $\phi$ is small, $\phi/K_\text{fl}$ is small compared with
$(\alpha-\phi)/K_\text{min}$, so the denominator is dominated by the mineral and
pore-space terms and $K_\text{sat}$ is insensitive to $K_\text{fl}$. When $\phi$
is large, $\phi/K_\text{fl}$ can dominate and the fluid controls the answer. **So
the fluid's influence grows with porosity** — monotonically and structurally, not
by coincidence.

**The measurement agrees.** From the demonstration's porosity sweep (fluid A to
fluid B, a 44-fold reduction in $K_\text{fl}$):

| $\phi$ | $\Delta V_p/V_p$ | $\Delta V_s/V_s$ |
|---|---|---|
| 0.02 | $+0.171\%$ | $+0.307\%$ |
| 0.20 | $+1.072\%$ | $+3.638\%$ |
| 0.35 | $-7.698\%$ | $+7.527\%$ |

A tenfold increase in porosity from 0.02 to 0.20 multiplies the $V_p$ effect by
6.3 — the qualitatively derived trend, with a magnitude consistent with the
$\phi/K_\text{fl}$ structure (the dependence is not purely linear because
$K_\text{dry}$ also changes with $\phi$ in the stated frame law).

**The apparent paradox, resolved.** The two statements are about different
quantities. The *absolute* sensitivity of $V_p$ to $K_\text{fl}$ grows with
porosity — that is the measured table above. The *relative importance* of a
$K_\text{fl}$ error is nevertheless largest at low porosity, because there the fluid
term is small and easily swamped by a relative error in $K_\text{dry}$:
- **the fluid's effect** grows with porosity;
- **the sensitivity of the answer to a fluid-modulus error** is largest where the
  competing uncertainties are smallest.

**The practical rule.** At low porosity, measure $K_\text{dry}$ well and do not
agonise over $K_\text{fl}$. At high porosity, measure $K_\text{fl}$ well — its
composition, pressure and temperature — and do not expect the frame to save you.

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

### 4.1 Assumptions, and the size of each failure

| Assumption | Failure | Quantified consequence |
|---|---|---|
| Low frequency (equilibrated pore pressure) | ultrasonic or large patches | >11 Hz for 0.1 m patches in 10⁻¹⁴ m² rock; velocities too high, $V_p$ error of order the dispersion (1–5%) |
| Homogeneous, isotropic mineral | mixed mineralogy | the effective $K_\text{min}$ is itself an average; a 10% error in $K_\text{min}$ shifts $K_\text{dry}$ by several percent |
| Connected, uniform saturation | patchy saturation | velocities exceed Gassmann; the excess is a diagnostic of patch size |
| No fluid–frame interaction | swelling clays | frame softening; the $V_s$ prediction fails in the direction of *lower* $V_s$ |
| Known $K_\text{dry}$ | back-calculated from a saturated measurement | the inversion inherits every error in $K_\text{min}$, $\phi$, $K_\text{fl}$ |
| Zero fluid shear modulus | viscous fluids at very high frequency | negligible below MHz |

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

### 5.1 Extended worked example: recovering the dry frame, then substituting

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

### 7.1 A shortcut that fails: using ultrasonic laboratory moduli as dry-frame moduli

**The shortcut.** Take $K_\text{sat}$ measured at 1 MHz on a saturated core,
invert Gassmann to get $K_\text{dry}$, and use that frame modulus to predict
seismic velocities at 30 Hz.

**Why it fails.** Section 3.3 derives the condition: equilibration requires
$f \ll 11$ Hz for a 0.1 m patch in a 10⁻¹⁴ m² rock. At 1 MHz the fluid pressure
is emphatically *not* equilibrated, so the measured saturated modulus is the
**unrelaxed** value, which is stiffer than the Gassmann value. Inverting Gassmann
on it therefore returns a dry-frame modulus that is too high — the inversion
imposes an assumption the measurement violates.

**Quantify the direction and the size.** Total velocity dispersion between the
relaxed and unrelaxed limits scales as $\sqrt{1+\Delta}-1$ for a relaxation
strength $\Delta$. For a rock with a few percent of dispersion the error in
$V_p$ is of order 1–5% — the same as the saturation effect being studied (the
demonstration's substitution changed $V_p$ by 1.07%). **So the artefact is the
same size as the signal**, which is the worst possible situation: the answer
looks plausible and is wrong by an amount comparable to the answer.

**What to do instead.** Either (a) measure the dry modulus *dry*, at the
frequency of interest or extrapolated to it; or (b) measure at several
frequencies and fit a dispersion model
([05-04-06](./06-attenuation-dispersion-rock.md)) so the relaxed limit can be
extrapolated rather than assumed; or (c) state the frequency of the measurement
and the frequency of the application, and the size of the dispersion between
them, as an explicit uncertainty.

**The generalisable lesson.** Every modulus is a function of frequency, and a
modulus quoted without its frequency is incomplete in the same way that a
resistivity quoted without its pore fluid is incomplete. Gassmann's own
assumption list (Section 4) names "low frequency" first for a reason.

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
