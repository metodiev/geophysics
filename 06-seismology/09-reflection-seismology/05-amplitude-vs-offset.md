---
id: 06-09-05
title: "AVO/AVA Analysis and Its Assumptions"
level: doctoral
prereqs: ["06-09-01", "06-09-04"]
tags: [seismology, reflection-seismology, avo, zoeppritz, fluid-substitution]
---

# AVO/AVA Analysis and Its Assumptions

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why normal-incidence data cannot separate $v_p$ from $\rho$, and
   why oblique incidence can.
2. **Derive** the structure of the Aki–Richards small-angle (weak-contrast)
   approximation to the Zoeppritz equations from the normal-incidence limit and
   the first-order sensitivity to $v_s$.
3. **Interpret** the intercept, gradient and far-angle terms physically.
4. **Compute** a fluid substitution with Gassmann's equation and show its effect
   on the AVO curve.
5. **Demonstrate** that AVO inversion is non-unique: construct two different
   $(v_p,v_s,\rho)$ triples that fit the same near-angle curve exactly.
6. **State** the assumptions of AVO analysis and the circumstances that void it.

## Prerequisites

- [01 Acoustic Impedance, Reflection Coefficients and the Convolution Model](01-reflection-principle.md).
- [04 Migration and Imaging](04-migration-imaging.md) — amplitude fidelity
  after imaging is a precondition for AVO.

## 1. Intuition: the angle is the extra measurement

At normal incidence the reflection coefficient depends on $(v_p,\rho)$ only
through the product $Z=\rho v_p$. Measure at an angle, however, and the incident
wave also feels the *shear* modulus, because part of the energy converts to S at
the interface. The reflection coefficient then depends on $v_p$, $v_s$ and $\rho$
separately. That is the entire physical basis of AVO: **the angle dependence
carries the information that normal incidence throws away.**

The practical prize is fluid detection. Replacing brine with gas in a porous rock
lowers the bulk modulus and the density; the impedance contrast with the overlying
shale changes, and — critically — it changes *differently at different angles*, so
the gas sand has a characteristic AVO signature. The prize comes with a price:
the inversion is non-unique, and this lesson demonstrates the degeneracy rather
than hiding it.

All numbers are **SYNTHETIC**; the rock and fluid parameters are chosen teaching
values.

## 2. Precise definitions

### 2.1 Incidence angle and the AVA curve

Let $\theta$ be the P-wave incidence angle at the interface. The
**reflectance** $R(\theta)$ is the ratio of reflected to incident P amplitude.
An **AVA (amplitude-versus-angle) curve** is $R(\theta)$ over the recorded range
of angles; **AVO** refers to the same quantity measured in offset (which maps to
angle through the velocity and depth). The two are synonyms in practice.

### 2.2 Zoeppritz equations

The exact $R(\theta)$ for a planar interface between two elastic half-spaces
follows from four boundary conditions (continuity of displacement and traction,
in both components) applied to the incident P, reflected P, reflected S,
transmitted P and transmitted S waves. The resulting linear system is the
**Zoeppritz equations**; its solution gives $R_{pp}(\theta)$ together with the
conversion coefficient $R_{ps}$.

### 2.3 Weak-contrast (Aki–Richards) approximation

For small contrasts in $v_p$, $v_s$ and $\rho$, the P–P reflection coefficient is
approximated by a series in $\sin^{2}\theta$:

$$R(\theta) \approx A + B\sin^{2}\theta + C\sin^{2}\theta\tan^{2}\theta,$$

with

$$A = \frac{1}{2}\left(\frac{\Delta\rho}{\bar\rho}
+ \frac{\Delta v_p}{\bar v_p}\right), \qquad
B = \frac{1}{2}\frac{\Delta v_p}{\bar v_p}
- 2\left(\frac{\bar v_s}{\bar v_p}\right)^{2}
\left(\frac{\Delta\rho}{\bar\rho}
+ 2\frac{\Delta v_s}{\bar v_s}\right),$$

$$C = \frac{1}{2}\frac{\Delta v_p}{\bar v_p},$$

where $\Delta$ denotes the difference (lower minus upper) and an overbar the
average of the two layers.

## 3. Derivations

### 3.1 Where the approximation comes from

The Zoeppritz system is exact but opaque. The approximation is obtained by
(i) linearising in the contrasts, and (ii) expanding the angle dependence. The
three terms have a clean hierarchy:

1. **The intercept $A$** is the normal-incidence coefficient to first order in
   the contrasts. Verify: for small $\Delta Z$,
   $\frac{Z_2-Z_1}{Z_2+Z_1} \approx \frac{\Delta Z}{2Z}
   = \frac{1}{2}(\frac{\Delta\rho}{\rho}+\frac{\Delta v_p}{v_p}) = A$. ✔
2. **The gradient $B$** contains what the shear modulus adds. The factor
   $2(\bar v_s/\bar v_p)^{2}$ is the coupling to S; when $v_s\to0$ (a fluid),
   $B\to\frac{1}{2}\Delta v_p/\bar v_p$ and the angle dependence weakens.
3. **The far-angle term $C\sin^{2}\theta\tan^{2}\theta$** grows rapidly with
   angle and is dominated by the *density* contrast. It becomes significant only
   beyond about $30$–$35^\circ$, which is why AVO with limited offsets cannot
   constrain density.

*Numerical check* (two-layer model $v_p$ 3000→3400, $v_s$ 1600→1900,
$\rho$ 2300→2450):

| $\theta$ | $R$ (3-term) | $R$ (2-term) | difference |
|---|---|---|---|
| $0^\circ$ | $+0.09408$ | $+0.09408$ | $0.00000$ |
| $10^\circ$ | $+0.08870$ | $+0.08864$ | $0.00006$ |
| $20^\circ$ | $+0.07395$ | $+0.07298$ | $0.00097$ |
| $30^\circ$ | $+0.05420$ | $+0.04899$ | $0.00521$ |
| $40^\circ$ | $+0.03774$ | $+0.01956$ | $0.01818$ |

Fitted: $A = +0.09408$, $B = -0.18036$. The intercept is large and positive while
the gradient is large and negative: the AVA curve decreases strongly with angle.
The two-term form is adequate to $20^\circ$ and progressively inadequate beyond
$30^\circ$ — a quantitative statement of the approximation's validity.

**A caution on the intercept.** The approximation's $A$ is *not* exactly the
normal-incidence coefficient: with a ~10% contrast the exact value is
$+0.093894$ and the approximation gives $+0.094079$, a difference of
$1.85\times10^{-4}$, which is the second-order term the approximation drops. An
"AVO intercept" is a **first-order** impedance contrast, not the impedance
contrast.

### 3.2 Fluid substitution: Gassmann's equation

To predict the effect of changing the pore fluid, use Gassmann's equation for the
saturated bulk modulus:

$$K_{\text{sat}} = K_{\text{dry}}
+ \frac{\left(1-K_{\text{dry}}/K_{\text{min}}\right)^{2}}
{\dfrac{\phi}{K_{\text{fl}}}
+ \dfrac{1-\phi}{K_{\text{min}}}
- \dfrac{K_{\text{dry}}}{K_{\text{min}}^{2}}}.$$

The shear modulus is **unchanged** by the fluid,
$\mu_{\text{sat}}=\mu_{\text{dry}}$, and the density is
$\rho = (1-\phi)\rho_{\text{min}} + \phi\rho_{\text{fl}}$. Then

$$v_p = \sqrt{\frac{K_{\text{sat}}+\tfrac{4}{3}\mu}{\rho}}, \qquad
v_s = \sqrt{\frac{\mu}{\rho}}.$$

Because $\mu$ is fixed, a fluid change moves $v_s$ only through the density;
$v_p$ moves through both $K_{\text{sat}}$ and $\rho$. That asymmetry is why
$v_p/v_s$ is the fluid indicator it is.

*Numerical check* (SYNTHETIC frame: $\phi = 0.25$,
$K_{\text{dry}} = 8\ \mathrm{GPa}$, $\mu = 8\ \mathrm{GPa}$,
$K_{\text{min}} = 36\ \mathrm{GPa}$, $\rho_{\text{min}} = 2650\
\mathrm{kg\,m^{-3}}$; fluids: brine $K=2.2\ \mathrm{GPa}$,
$\rho=1000$; oil $K=0.8$, $\rho=800$; gas $K=0.05$, $\rho=150$):

| saturation | $\rho$ (kg/m³) | $v_p$ (m/s) | $v_s$ (m/s) | $R(0)$ | $R(30^\circ)$ |
|---|---|---|---|---|---|
| brine | 2238 | 3233 | 1891 | $+0.0236$ | $-0.0120$ |
| oil | 2188 | 3062 | 1912 | $-0.0148$ | $-0.0626$ |
| gas | 2025 | 3046 | 1988 | $-0.0560$ | $-0.1072$ |

Two features stand out and both are physically necessary:

- **$R(0)$ changes sign** from brine to hydrocarbon. That sign change is the
  physical basis of the classic "bright spot" and a large part of why AVO works.
- **$v_s$ *increases* from brine to gas**, because the density drops while $\mu$
  is unchanged. A naive expectation that all velocities drop with gas is wrong;
  only $v_p$ does, and $v_s$ follows the density.

### 3.3 Non-uniqueness, constructed explicitly

In the two-term approximation the AVA curve is fixed by the pair $(A,B)$. Layer 2
has three unknowns $(\Delta v_p, \Delta v_s, \Delta\rho)$ but only two equations,
so a **one-parameter family** of models gives the same curve. The demonstration
constructs a member of that family by choosing a different $\Delta v_s$ and
solving for the $\Delta v_p$ and $\Delta\rho$ that keep $(A,B)$:

| | $v_p$ (m/s) | $v_s$ (m/s) | $\rho$ (kg/m³) |
|---|---|---|---|
| model A | 3400 | 1900 | 2450 |
| model B | 3026 | 1705 | 2754 |

Measured differences:

| comparison | max $|R_A-R_B|$ | in units of $\sigma=0.005$ |
|---|---|---|
| two-term, $0$–$30^\circ$ | $0.00000$ | $0.00\sigma$ |
| two-term, $0$–$40^\circ$ | $0.00000$ | $0.00\sigma$ |
| three-term, $0$–$40^\circ$ | $0.01695$ | $3.39\sigma$ |

The two-term curves are **identical**: model B is slower in $v_p$
($-374\ \mathrm{m\,s^{-1}}$) and in $v_s$ ($-195\ \mathrm{m\,s^{-1}}$) and denser
($+304\ \mathrm{kg\,m^{-3}}$), and the $\chi^{2}$ test on repeated noisy
realisations returns a **tie** for every realisation. Only the far-angle third
term, which the near-angle data do not constrain, distinguishes them, and it does
so by $3.4\sigma$ at $40^\circ$.

**The honest conclusion.** AVO inversion of a limited-angle data set does not
recover a unique $(v_p,v_s,\rho)$. It recovers a ridge in model space — the same
geometry as the receiver-function $H$–$k$ trade-off of
[06-08-01](../08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md).
A unique triple requires long offsets (to constrain $C$), or prior information
(rock physics, well logs, a $v_p/v_s$ relation).

### 3.4 AVO classes, and what they are calibrated against

The intercept $A$ and gradient $B$ define a two-dimensional classification of
reflections. The conventional classes (a *classification scheme*, not a law of
nature) are:

| class | $A$ | $A+B$ (approximately $R$ at far angle) | typical cause |
|---|---|---|---|
| I | large positive | decreasing, may cross zero | high-impedance sand | 
| II | near zero | negative | near-zero impedance contrast |
| III | negative | more negative | low-impedance (soft) sand, e.g. gas |
| IV | negative | less negative (increasing) | very soft sand, thin bed tuning |

The classification is useful because it organises observations and predicts
which reflections are fluid candidates. It is also dangerous if used as a
diagnosis: the classes overlap with lithology changes, tuning effects
(lesson 07), and anisotropy, and the boundaries between them are defined by the
*intercept and gradient*, which are themselves non-unique (Section 3.3).
**Always report the fitted $(A,B)$ and their uncertainties, not only the class
label.**

*Numerical check.* For the demonstration's brine-saturated case,
$A = +0.0236$, $B$ negative enough that $A+B\sin^{2}(30^\circ)$ is $+0.0236 -
0.03(0.25)\cdot(\ldots)$ — the measured $R(30^\circ)$ is $-0.0120$, so $A$ is
positive and the far-angle response is negative: this is a class-I-like response
for brine. For gas, $A = -0.0560$ and $R(30^\circ) = -0.1072$: a class-III
response. **The fluid change moved the reflection from class I to class III**,
which is the quantitative statement behind "gas sand shows a class-III AVO
anomaly".

### 3.5 What an AVO inversion actually estimates

Given a usable range of angles, a two-term inversion estimates the pair $(A,B)$.
These are two *combinations* of the three rock parameters. The combinations are:

- $A$: the impedance contrast, $\tfrac{1}{2}(\Delta\rho/\rho+\Delta v_p/v_p)$;
- $B$: the gradient combination, dominated by $\Delta v_s/v_s$ at moderate angles.

A *three*-term inversion nominally estimates $(A,B,C)$ and hence three
combinations — enough, in principle, for three parameters. In practice the third
term is poorly conditioned unless the far-angle data are excellent, which is why
the honest output is often the pair $(A,B)$ plus a *range* for density. The
demonstration's $\chi^{2}$ tie between two different triples fitting the same
near-angle curve is the concrete statement of this limitation.

## 4. Physical interpretation

- **Angle is a second dimension.** Normal incidence collapses three rock
  parameters onto one; oblique incidence unfolds them.
- **$v_s$ is the fluid-sensitive part of the angle dependence.** $B$ carries the
  $(\bar v_s/\bar v_p)^{2}$ coupling, and $v_s$ responds to fluid only through
  density.
- **The far-angle term is density, and it is fragile.** It requires long offsets
  and good amplitude fidelity; without them, density is effectively unconstrained.
- **Non-uniqueness is structural, not incidental.** Two measurements cannot
  determine three parameters, however precise the measurements.

## 5. Assumptions

1. **Small contrasts** for the Aki–Richards approximation; it degrades for large
   contrasts and steep angles.
2. **A planar interface** between homogeneous half-spaces; thin-bed tuning
   (lesson 07) modifies the amplitudes.
3. **Isotropic elasticity.** Anisotropy changes the angle dependence and can
   mimic or mask fluid effects.
4. **Amplitude fidelity.** Transmission losses, attenuation, geometrical
   spreading, and migration amplitude errors must be removed before AVO; this is
   rarely perfect and is usually the dominant error.
5. **Known angles**, hence a known velocity and depth — circular, since AVO is
   often used to refine the velocity model.
6. **Correctly separated primaries.** Multiples and mode conversions that remain
   in the data bias the fit.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $R$, $A$, $B$, $C$ | dimensionless | ratios of elastic parameters |
| $\Delta v/v$, $\Delta\rho/\rho$ | dimensionless | |
| $\theta$ | rad | $\sin$, $\tan$ dimensionless |
| $K$, $\mu$ | Pa | $\mathrm{kg\,m^{-1}\,s^{-2}}$ |
| $\rho$ | $\mathrm{kg\,m^{-3}}$ | |
| $v_p, v_s$ | $\mathrm{m\,s^{-1}}$ | $\sqrt{\mathrm{Pa}/(\mathrm{kg\,m^{-3}})} = \mathrm{m\,s^{-1}}$ ✔ |

The velocity formula's dimensions are worth checking once:
$\mathrm{Pa} = \mathrm{kg\,m^{-1}\,s^{-2}}$, so
$\mathrm{Pa}/(\mathrm{kg\,m^{-3}}) = \mathrm{m^{2}\,s^{-2}}$, and the square root
is $\mathrm{m\,s^{-1}}$. ✔

## 7. Worked examples

### Example 1 — computing $A$ and $B$ by hand

For the model above: $\Delta v_p/\bar v_p = 400/3200 = 0.125$;
$\Delta\rho/\bar\rho = 150/2375 = 0.06316$;
$\Delta v_s/\bar v_s = 300/1750 = 0.17143$;
$\bar v_s/\bar v_p = 1750/3200 = 0.54688$, squared $= 0.29908$.

$$A = \frac{1}{2}(0.06316+0.125) = 0.09408 \;✔$$

$$B = \frac{1}{2}(0.125) - 2(0.29908)(0.06316+2(0.17143))
= 0.0625 - 0.59816(0.40602) = 0.0625 - 0.24286 = -0.18036 \;✔$$

The hand calculation matches the demonstration exactly.

### Example 2 — why $v_s$ increases with gas

Brine-saturated: $\rho = 2238$, $\mu = 8\ \mathrm{GPa}$ →
$v_s = \sqrt{8\times10^{9}/2238} = 1891\ \mathrm{m\,s^{-1}}$. Gas-saturated:
$\rho = 2025$ → $v_s = \sqrt{8\times10^{9}/2025} = 1988\ \mathrm{m\,s^{-1}}$, a
$5\%$ *increase*. Meanwhile $v_p$ falls from 3233 to 3046. **$v_p/v_s$ is
therefore a much stronger fluid discriminator than $v_p$ alone** — which is
exactly why $v_p/v_s$ estimates from AVO are sought and why their
non-uniqueness matters.

### Example 3 — reading the non-uniqueness table

A near-angle AVA curve is fitted and yields $A$ and $B$. The interpreter
converts it to a gas-sand model. The demonstration shows that a different triple
(model B) fits the *same* curve with zero residual. The interpreter's model is
therefore one member of an equivalence class, and the correct statement of the
result is "the data are consistent with $v_p/v_s$ between $X$ and $Y$", not "the
reservoir has $v_p/v_s = Z$".

### Example 5 — moving across a class boundary

Take the demonstration's two-term fit $A = +0.09408$, $B = -0.18036$ and compute
$R$ at $30^\circ$: $A + B\sin^{2}30^\circ = 0.09408 - 0.18036(0.25) = 0.0490$.
The reflection is positive at both $0^\circ$ and $30^\circ$ (class I). Now rotate
the impedance contrast so $A \to -0.01$ while $B$ stays $-0.18$: $R(0) = -0.01$
and $R(30^\circ) = -0.055$, a class-III-like response. So a *small* change in $A$
near zero flips the classification while barely changing the far-angle response.
**This is why a classification near $A=0$ is fragile and must not be reported
without the uncertainties in $A$ and $B$.** A reflection with
$A = 0.00 \pm 0.02$ spans classes II and I; the label carries less information
than the numbers.

## 8. Python demonstration

`code/avo_demo.py`:

1. verifies the Aki–Richards intercept against the exact impedance formula,
   reporting the second-order residual ($1.85\times10^{-4}$);
2. prints the AVA curve and the two- versus three-term difference;
3. computes $A$ and $B$ and interprets them;
4. performs Gassmann fluid substitution for brine/oil/gas and prints the
   $R(0)$ and $R(30^\circ)$ change;
5. constructs an explicit pair of different $(v_p,v_s,\rho)$ triples with
   identical two-term AVA curves (tie in $\chi^{2}$ for every noise realisation)
   and a $3.4\sigma$ difference in the far-angle term.

## 9. Exercises

Full sets are in
[`exercises/05-amplitude-vs-offset-exercises.md`](./exercises/05-amplitude-vs-offset-exercises.md)
and
[`exercises/05-amplitude-vs-offset-solutions.md`](./exercises/05-amplitude-vs-offset-solutions.md).

- **★** Compute $A$ and $B$ for $\Delta v_p/\bar v_p = 0.10$,
  $\Delta v_s/\bar v_s = 0.15$, $\Delta\rho/\bar\rho = 0.05$,
  $\bar v_s/\bar v_p = 0.55$.
- **★★** Show that $A$ reduces to the exact normal-incidence coefficient to
  first order in the contrasts.
- **★★** Perform a Gassmann substitution for a $20\%$ porosity sand and compare
  the brine and gas $v_p/v_s$.
- **★★★** Construct a second member of the AVO equivalence class for a given
  $(A,B)$ and state what additional measurement would break the degeneracy.

## 10. Common mistakes

1. **Treating the AVO intercept as the exact normal-incidence coefficient.**
   They differ at second order in the contrast.
2. **Ignoring the third term but using offsets beyond $30$–$35^\circ$.** The
   error reaches $0.018$ in the demonstration's example — comparable to the
   signal.
3. **Reporting a unique $(v_p,v_s,\rho)$.** It is a ridge, not a point.
4. **Expecting $v_s$ to fall with gas.** It rises through the density change.
5. **Analysing amplitudes without correcting for geometrical spreading,
   transmission and attenuation.** These dominate the raw amplitude variation
   with offset.
6. **Ignoring anisotropy.** It modifies the angle dependence and can be mistaken
   for a fluid effect.

## 11. Real-world applications

- **Hydrocarbon detection.** Gas sands typically show a class-III or class-IV AVO
  signature; the interpretation is calibrated with wells and rock physics.
- **Lithology and porosity from seismic.** Joint $v_p$–$v_s$ inversion is a
  standard reservoir-characterisation product.
- **CO$_2$ monitoring.** Fluid substitution predicts the 4-D AVO change from
  injected CO$_2$; the same non-uniqueness applies.
- **Quantitative interpretation limits.** AVO is the clearest example in
  geophysics of a method whose value is limited by *non-uniqueness* rather than
  by noise, which is why rock-physics priors are essential (see
  [05-04-03 Gassmann Fluid Substitution](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md)).

## 12. Further reading

- **Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: advanced. The Zoeppritz equations and the
  weak-contrast approximation.
- **Shuey, R. T. (1985). A simplification of the Zoeppritz equations.
  *Geophysics*, 50(4), 609–614.** Level: research. The two-term form used here.
- **Gassmann, F. (1951). Über die Elastizität poröser Medien. *Vierteljahrsschrift
  der Naturforschenden Gesellschaft in Zürich*, 96, 1–23.** Level: research. The
  fluid-substitution equation.
- **Mavko, G., Mukerji, T., & Dvorkin, J. (2009). *The Rock Physics Handbook*
  (2nd ed.). Cambridge University Press.** Level: advanced. Practical rock
  physics, including Gassmann's equation.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Confirm current editions through
> your library.

## 13. Related lessons

- [01 Acoustic Impedance, Reflection Coefficients and the Convolution Model](01-reflection-principle.md).
- [07 Seismic Attributes and Quantitative Interpretation](07-seismic-attributes.md) —
  the resolution limits that bound AVO.
- [05-04-03 Gassmann Fluid Substitution](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md) —
  the rock physics in full.
- [06-08-01 Receiver Functions](../08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md) —
  the same ridge-in-model-space geometry.

## 14. Self-assessment checklist

- [ ] I can explain why oblique incidence separates $v_p$ from $\rho$.
- [ ] I can write and interpret the three Aki–Richards terms.
- [ ] I can perform a Gassmann fluid substitution and explain the sign changes.
- [ ] I can construct two distinct models fitting the same near-angle curve.
- [ ] I can state what extra measurement would break the degeneracy.
- [ ] I can list four preprocessing requirements before AVO is meaningful.
