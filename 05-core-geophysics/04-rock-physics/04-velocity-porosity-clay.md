---
id: 05-04-04
title: "Velocity-Porosity-Clay Models and Empirical Relations"
level: graduate
prereqs: ["05-04-03"]
tags: [wyllie, raymer, clay, empirical-relations, shaly-sand]
---

# Velocity-Porosity-Clay Models and Empirical Relations

## Learning objectives

1. **State** the Wyllie time-average and Raymer-Hunt-Gardner relations, with
   their units and their calibrated ranges.
2. **Compare** them on identical inputs and quantify where they diverge.
3. **Derive** a two-component (matrix + fluid) time average from a travel-time
   sum, and explain why it is only approximately valid.
4. **Explain** why empirical relations carry an implicit dataset and are not
   transferable without justification.
5. **Decide** when to use a bound, when to use an empirical fit, and when to
   measure.

## Prerequisites

- [05-04-01 Porosity, Density and Velocity](./01-porosity-density-velocity.md)
- [05-04-03 Gassmann Fluid Substitution](./03-gassmann-fluid-substitution.md)

## 1. Intuition

Empirical velocity–porosity relations were fitted to specific rocks. They are
useful within their calibrated range and dangerous outside it. The professional
habit is: state the relation, state the calibrating lithology and porosity
range, and state the residual scatter. A velocity quoted without those three
pieces of information cannot be assessed.

## 2. The relations

**Wyllie time-average** (a travel-time sum, not a stiffness average):

$$\frac{1}{V_p} = \frac{\phi}{V_\text{fl}} + \frac{1-\phi}{V_\text{ma}},$$

so $V_p$ is the harmonic-style combination of the matrix and fluid velocities —
a "slowness average". Units: each term is s/m, and inverting gives m/s. ✓

**Raymer-Hunt-Gardner** (an empirical polynomial fit):

$$V_p = (1-\phi)^2V_\text{ma} + \phi V_\text{fl}.$$

Units are immediately consistent (both terms m/s). The quadratic weighting of
the matrix term was chosen to fit data; it is not derived.

**Wood's equation** for the fluid, used inside either relation:
$1/K_\text{fl} = \sum_i S_i/K_i$, derived in
[05-04-03](./03-gassmann-fluid-substitution.md).

## 3. Derivation of the time average, and why it is only approximate

If the wave traverses the matrix and the fluid in series (a 1-D layered medium
loaded normal to the layers), travel times add:

$$t_\text{total} = t_\text{ma} + t_\text{fl}
\implies \frac{L}{V_p} = \frac{(1-\phi)L}{V_\text{ma}} + \frac{\phi L}{V_\text{fl}},$$

which is Wyllie's form. The assumption is *series* path geometry and a
uniform, connected fluid path — neither of which holds in a real rock, where
the fluid is confined and the frame carries the shear. Hence Wyllie is a good
fit in clean, high-porosity, fluid-saturated sands and poor in stiff, low-porosity
or clay-rich rocks.

**Measured divergence.** With stated SYNTHETIC inputs $V_\text{ma} = 4500$ m/s,
$V_\text{fl} = 1500$ m/s:

| $\phi$ | Wyllie (m/s) | Raymer (m/s) | difference |
|---|---|---|---|
| 0.05 | 4090.9 | 4136.2 | $-1.1\%$ |
| 0.10 | 3750.0 | 3795.0 | $-1.2\%$ |
| 0.20 | 3214.3 | 3180.0 | $+1.1\%$ |
| 0.30 | 2812.5 | 2655.0 | $+5.6\%$ |
| 0.40 | 2500.0 | 2220.0 | $+11.2\%$ |

Both reduce correctly at the endpoints (4500 m/s at $\phi=0$, 1500 m/s at
$\phi=1$). They agree to about 1% below $\phi = 0.15$, cross over near 0.15–0.2,
and diverge to 11% at $\phi = 0.40$. **Reporting "the velocity" from one of them
without naming it and its range is not a prediction.**

### 3.1 Inverting the time average: porosity from velocity, and its sensitivity

Wyllie's relation is used in reverse far more often than forward. The inversion
is exact algebra, and its error amplification is not.

$$1-\phi = \frac{V_\text{ma}}{V}\left(\frac{1}{V}-\frac{1}{V_\text{fl}}\right)
V_\text{fl} \quad\text{— rather, solve directly:}\qquad
\phi = \frac{\dfrac{1}{V_p}-\dfrac{1}{V_\text{ma}}}
{\dfrac{1}{V_\text{fl}}-\dfrac{1}{V_\text{ma}}} .$$

Dimensional check: numerator and denominator are both s m⁻¹, so $\phi$ is
dimensionless ✓.

**Sensitivity.** Differentiating with respect to the measured velocity,

$$\frac{\partial\phi}{\partial V_p}
= -\frac{1}{V_p^2}\cdot\frac{1}{\dfrac{1}{V_\text{fl}}-\dfrac{1}{V_\text{ma}}}
= \frac{1}{V_p^2}\cdot
\frac{V_\text{ma}V_\text{fl}}{V_\text{ma}-V_\text{fl}} .$$

**Worked numbers** for $V_\text{ma} = 4500$, $V_\text{fl} = 1500$ m/s and a
measured $V_p = 3500$ m/s:

$$\phi = \frac{2.857\times10^{-4}-2.222\times10^{-4}}{6.667\times10^{-4}
-2.222\times10^{-4}} = \frac{6.35\times10^{-5}}{4.444\times10^{-4}} = 0.1429,$$

$$\frac{\partial\phi}{\partial V_p} = -1.8367\times10^{-4}\ \mathrm{per\ m\,s^{-1}} .$$

So a **50 m/s** velocity error — well within typical log and laboratory
uncertainty — gives $\Delta\phi = -0.0092$, a **6.4% relative error** in
porosity. The amplification factor is the whole story: the inversion converts
a 1.4% velocity error into a 6.4% porosity error.

**The same for Raymer.** Raymer is quadratic in $\phi$:
$V_\text{ma}\phi^2 + (V_\text{fl}-2V_\text{ma})\phi + (V_\text{ma}-V_p) = 0$, whose
physical root at $V_p = 3500$ m/s is $\phi = 0.1461$ (the other root, 1.52, is
unphysical). The sensitivity is

$$\frac{\partial\phi}{\partial V_p} = \frac{1}{V_\text{fl}-2V_\text{ma}
+2V_\text{ma}\phi} = -1.617\times10^{-4},$$

so a 50 m/s error gives $-0.0081$, a 5.5% relative porosity error. **The two
relations disagree on the porosity (0.1429 vs 0.1461, 2.2%) and on its
sensitivity (13%), which is the practical size of the model choice compared with
the input uncertainty.**

### 3.2 What the two relations assume, structurally

Comparing the two expressions exposes what each one *is*:

$$\text{Wyllie: } \frac{1}{V_p} = \frac{\phi}{V_\text{fl}}
+ \frac{1-\phi}{V_\text{ma}},
\qquad
\text{Raymer: } V_p = (1-\phi)^2V_\text{ma} + \phi V_\text{fl} .$$

Wyllie is a **weighted average of slownesses** with weights $\phi$ and
$1-\phi$, which sum to 1. That is a physical statement: the wave spends a
fraction of its path in each medium, and the weights are the volume fractions.
It follows from the series (isostress) geometry of
[05-04-02](./02-effective-medium-theory.md).

Raymer is a **weighted average of velocities** with weights $\phi$ and
$(1-\phi)^2$, which sum to

$$\phi + (1-\phi)^2 = 1 - \phi + \phi^2 .$$

That expression equals 1 only at $\phi = 0$ and $\phi = 1$, and has a minimum of
**0.75 at $\phi = 0.5$**. So Raymer's weighting is *not* a volume weighting: it
falls 25% short of unity at mid-porosity, which is precisely why Raymer
under-predicts relative to Wyllie at high porosity (measured: 2220 vs 2500 m/s at
$\phi = 0.40$, an 11.2% difference).

**Physical interpretation.** Raymer's $(1-\phi)^2$ is a *fitted* device that
encodes the empirical observation that velocities fall faster than linearly with
porosity in consolidated rocks. Wyllie's $1-\phi$ is a *derived* weight that
encodes a series geometry. Neither is universally right; each is a statement
about the geometry it was built on, and the fits were calibrated on particular
lithologies. That is why the module insists that a relation be quoted with its
calibrating dataset.

## 4. Clay: why the two-component picture fails

Clay affects velocity in three distinct ways, all of which a two-component
relation ignores:

1. **It is a third phase**, with its own moduli, and it occupies pore space,
   reducing *effective* porosity.
2. **It is compliant**, so it lowers the frame modulus beyond what its volume
   fraction alone would suggest.
3. **It conducts and it holds bound water**, which changes the effective fluid
   and hence the electrical properties
   ([05-04-07](./07-electrical-properties-rock.md)). Bound water is not free to
   move, so it does not participate in Wood's average the way free water does.

The practical consequence for velocity: at fixed porosity, increasing clay
content *lowers* $V_p$. A relation fitted to clean sands will overpredict the
velocity of a shaly sand, and the misfit grows with clay content. Any
shaly-sand velocity model (e.g. a three-phase or effective-porosity
formulation) must be calibrated on shaly samples. This lesson does not derive
one; it insists that you state which model you used and on what it was
calibrated.

## 5. Units and dimensional analysis

| Quantity | Unit |
|---|---|
| $V_p, V_\text{ma}, V_\text{fl}$ | m/s (or km/s, ×10³) |
| $\phi$ | dimensionless |
| slowness $1/V$ | s/m |

Check for Raymer: $(1-\phi)^2$ is dimensionless, so both terms are m/s. ✓
Check for Wyllie: $\phi/V_\text{fl}$ is s/m; the sum is s/m; the reciprocal is
m/s. ✓

## 6. Assumptions

1. **Wyllie:** series geometry, uniform connected saturation, and a calibrated
   lithology. Validated originally for clean, high-porosity sandstones.
2. **Raymer:** empirical, fitted over a stated porosity range; extrapolation
   beyond it is unjustified.
3. **Both:** a single fluid phase with a known $V_\text{fl}$, and a known
   $V_\text{ma}$ that is a *weighted* average over the minerals present.
4. **Isotropy and no dispersion** over the measurement band.
5. **No clay effects** beyond the matrix averaging.

### 6.1 Assumptions, and the size of each failure

| Assumption | Failure | Quantified consequence |
|---|---|---|
| Known $V_\text{ma}$ | mineralogical variation | 200 m/s error in $V_\text{ma}$ → 2.6% in $V_p$ → ~12% in inverted porosity |
| Series geometry (Wyllie) | non-layered pore space | up to 7% velocity bias at fixed porosity; 13% porosity understatement |
| Fitted form (Raymer) | outside calibration range | 11.2% divergence from Wyllie at $\phi = 0.40$ |
| Single fluid phase | partial saturation | $V_\text{fl}$ is itself a modulus average ([05-04-03](./03-gassmann-fluid-substitution.md)), and a small gas fraction dominates it |
| No dispersion | broad band | velocity is frequency-dependent ([05-04-06](./06-attenuation-dispersion-rock.md)); a laboratory value may not apply at seismic frequency |
| Isotropic rock | shale fabric | anisotropy of order 10% in $V_p$ ([05-04-05](./05-anisotropy-rock.md)) is larger than the porosity effect at low $\phi$ |

### 6.2 Critical porosity, and what the empirical relations omit

Both empirical relations interpolate smoothly from the matrix at $\phi = 0$ to the
fluid at $\phi = 1$. Real rocks do not behave that way: **the grain framework
ceases to be load-bearing at a porosity well below 1**, and the velocity
collapses rather than passing smoothly to the fluid value.

That porosity is the **critical porosity** $\phi_c$ (also called the critical
porosity or the suspension limit), and its value is a lithology-dependent
constant — for many sandstones it is of order 0.4, and it must be calibrated, not
assumed. A simple stated frame law makes the consequence explicit:

$$K_\text{dry}(\phi) = K_\text{min}\left(1-\frac{\phi}{\phi_c}\right),
\qquad\text{so}\qquad K_\text{dry}(\phi_c) = 0 .$$

**Measured consequences** with the stated synthetic law ($K_\text{min} = 37$ GPa,
$\phi_c = 0.40$), as used in the Gassmann demonstration:

| $\phi$ | $K_\text{dry}$ (GPa) | $K_\text{dry}/K_\text{min}$ |
|---|---|---|
| 0.10 | 27.75 | 0.75 |
| 0.20 | 18.50 | 0.50 |
| 0.30 | 9.25 | 0.25 |
| 0.35 | 4.63 | 0.125 |
| 0.40 | 0 | 0 |

**What the empirical relations miss.** Wyllie at $\phi = 0.35$ returns 2647 m/s
and Raymer 2426 m/s, both finite and both decreasing smoothly — neither has any
notion that the frame has lost 87.5% of its stiffness and that at $\phi_c$ it has
none at all. In the suspension limit the shear modulus vanishes (a fluid
suspension cannot support shear), so $V_s\to0$ — a behaviour no
velocity-porosity relation of this family can represent, because each was fitted
over a porosity range where the frame is still competent.

**The practical consequences.**

1. **Do not extrapolate to high porosity.** Above roughly $0.8\phi_c$ the frame
   law departs rapidly from any relation fitted at lower porosity, and the
   prediction degrades fast.
2. **Critical porosity explains why "unconsolidated" rocks cluster.** Sands near
   $\phi_c$ have velocities close to those of suspensions, and the transition is
   sharp rather than gradual.
3. **The concept is a rock-physics model, not a measurement.** $\phi_c$ must be
   stated with its source, exactly like $\rho_m$ in
   [04-01](./01-porosity-density-velocity.md).

## 7. Worked examples

**7.1** $\phi = 0.20$, $V_\text{ma} = 4500$, $V_\text{fl} = 1500$: Wyllie gives
3214.3 m/s; Raymer gives 3180.0 m/s. The two differ by 34 m/s — smaller than the
typical uncertainty in $V_\text{ma}$.

**7.2** If $V_\text{ma}$ is uncertain by ±200 m/s (a plausible range for a
mineralogical mixture), how much does $V_p$ change at $\phi = 0.20$? Wyllie:
$1/V = 0.2/1500 + 0.8/V_\text{ma}$, so $V_\text{ma} = 4700$ gives
$1/V = 1.333\times10^{-4}+1.702\times10^{-4} = 3.035\times10^{-4}$,
$V = 3294$ m/s; $V_\text{ma} = 4300$ gives $1/V = 1.333\times10^{-4}+1.860
\times10^{-4} = 3.193\times10^{-4}$, $V = 3131$ m/s. So a ±200 m/s error in the
matrix velocity moves $V_p$ by about $\pm80$ m/s ($\mp2.6\%$) — larger than the
Wyllie–Raymer difference at that porosity. **The input uncertainty dominates the
model choice.**

**7.3** An observed $V_p = 2600$ m/s at $\phi = 0.30$ lies 7.4% below Wyllie
(2812.5) and 2.1% below Raymer (2655). Neither is "the answer"; the honest
statement is that the rock is slower than either clean-sand relation predicts,
which is itself evidence of clay or of a compliant mineral assemblage.

### 7.1 Extended worked example: which uncertainty actually controls the answer?

A model-comparison question — "should I use Wyllie or Raymer here?" — is often
the wrong question. The arithmetic below shows why.

**Stated inputs.** $V_\text{fl} = 1500$ m/s. The matrix velocity of a
mixed-mineral assemblage is not known exactly: take $V_\text{ma} = 4500$ m/s
with a plausible range of $\pm200$ m/s.

**Sensitivity to the matrix velocity at $\phi = 0.20$.** Wyllie:
$1/V = 0.2/1500 + 0.8/V_\text{ma}$.
At $V_\text{ma} = 4500$: $1/V = 1.33333\times10^{-4} + 1.77778\times10^{-4}
= 3.11111\times10^{-4}$, $V = 3214.3$ m/s.
At 4700: $1/V = 1.33333\times10^{-4}+1.70213\times10^{-4}
= 3.03546\times10^{-4}$, $V = 3294.4$ m/s.
At 4300: $1/V = 1.33333\times10^{-4}+1.86047\times10^{-4}
= 3.19379\times10^{-4}$, $V = 3131.1$ m/s.

So $\pm200$ m/s in $V_\text{ma}$ moves $V_p$ by $-2.6\%$ / $+2.5\%$, i.e.
$\mp83$ m/s.

**Sensitivity to the model choice at the same porosity.** Wyllie gives 3214.3
m/s, Raymer gives 3180.0 m/s — a difference of **34.3 m/s, or 1.1%**.

**The conclusion.** The input uncertainty is 2.4 times the model-choice
difference. Measuring $V_\text{ma}$ better (from mineralogy and the elastic
moduli of the constituent minerals, or from a core measurement) buys more
accuracy than arguing about which empirical relation to use. This ordering — get
the inputs right before refining the model — is general, and it is why this
module's bounds and error bars matter more than its formulas.

**The clay exception.** Clay changes the ordering, because it breaks the model
rather than perturbing an input. A shaly sand can be 7% slower than Wyllie
predicts at the same porosity — larger than any plausible $V_\text{ma}$
uncertainty, and not fixable by better inputs to a two-phase relation. This is
the difference between a *sensitivity* and a *structural* failure, and the two
require different responses.

### 7.2 Worked arithmetic: the porosity error from a 50 m/s velocity error

Take the stated synthetic pair $V_\text{ma} = 4500$ m/s, $V_\text{fl} = 1500$
m/s, and suppose a measured $V_p$ has a stated uncertainty of $\pm50$ m/s (1.4%)
at 3500 m/s.

| relation | $\phi$ at 3500 m/s | $\partial\phi/\partial V_p$ | $\Delta\phi$ for $\pm50$ m/s | relative error |
|---|---|---|---|---|
| Wyllie | 0.1429 | $-1.837\times10^{-4}$ | $\mp0.0092$ | 6.4% |
| Raymer | 0.1461 | $-1.617\times10^{-4}$ | $\mp0.0081$ | 5.5% |

**Read the table as a two-term error budget.** The *model* choice contributes
0.0032 in porosity (2.2%); the *input* uncertainty contributes 0.008–0.009
(5.5–6.4%). The input term is 2.5 times the model term — so, as in
[04-04's sibling analysis](./01-porosity-density-velocity.md), **getting the
inputs right matters more than choosing the model**. An analyst who argues about
Wyllie versus Raymer while accepting a 50 m/s velocity uncertainty is optimising
the smaller term.

**One more consequence worth stating.** Porosity error is *not* symmetric in
velocity error: because the relation is non-linear, a velocity that is too high
gives a porosity that is too low, and the magnitudes differ slightly on the two
sides. For a $\pm10\%$ velocity band (3150–3850 m/s), Wyllie gives
$\phi = 0.2143$ to $0.0844$ — a range of 0.130, i.e. 91% of the central value of
$0.1429$. **At
low porosity, velocity is a poor porosity estimator**, which is the quantitative
form of "you cannot invert an empirical relation and call it a measurement".

### 7.3 A shortcut that fails: inverting Wyllie on a shaly sand

**The shortcut.** Apply the Wyllie inversion to a shaly sand using $V_\text{ma}$
for quartz, and report the porosity.

**Why it fails, in two independent ways.**

1. **The matrix velocity is wrong.** A shaly sand has a compliant clay fraction
   with a lower $V_\text{ma}$ than quartz. From the sensitivity analysis of
   [04-04's sibling lesson](./01-porosity-density-velocity.md), a 200 m/s error
   in $V_\text{ma}$ moves $V_p$ by about 2.6% at $\phi = 0.15$, which the
   inversion converts into roughly 12% of the porosity value.
2. **The model structure is wrong.** Wyllie assumes a series (layered) geometry.
   Clay coats grains and fills pores in a geometry that is not layered; it
   softens the *frame* in a way no matrix-averaging scheme captures. A rock can
   be 7% slower than Wyllie predicts at the same porosity — larger than any
   plausible $V_\text{ma}$ error and not fixable by better inputs.

**Quantified.** If the true rock at $\phi = 0.20$ has $V_p = 3214$ m/s (Wyllie
with quartz, verified: the inversion of 3214 m/s returns $\phi = 0.20006$) but
measures 2990 m/s because of clay — 7.0% slower — the Wyllie inversion returns
$\phi = 0.2525$: a **26% overstatement** of porosity, from the model alone, on a
perfectly consistent dataset. Note the *direction*: clay-softened rock is
slower, and a slower rock inverts to a *higher* porosity, so the bias is
positive. Getting the sign of a model bias right is as important as its size.

**What to do instead.** Use a shaly-sand model (a three-phase or effective-
porosity formulation) calibrated on cores from the interval, and report the
calibration. Where no calibration exists, report the *range* of porosities
compatible with the velocity under the plausible model class — which is the
honest answer, and which is almost always wider than the single number a
published relation would give.

## 8. Python demonstration

`code/petrophysics_demo.py` Section 1 prints both relations across the porosity
range and the limits check. Section 4 shows the analogous failure of Archie's
law with clay, which is the electrical counterpart of this lesson.

## 9. Exercises, mistakes, applications

Exercises: [`exercises/04-velocity-porosity-clay-exercises.md`](./exercises/04-velocity-porosity-clay-exercises.md).

**Common mistakes.** (1) Using Wyllie for carbonates or shaly sands.
(2) Extrapolating Raymer beyond its fitted range. (3) Treating $V_\text{ma}$ as
a constant rather than a weighted mineral average. (4) Inverting a
velocity–porosity relation to get porosity and reporting it as a measurement.
(5) Ignoring that bound water behaves differently from free water.

**Applications.** Porosity prediction from sonic logs; synthetic seismogram
construction; identifying undercompaction and gas effect on logs; rock-physics
templates for quantitative interpretation.

## 10. Further reading

- **Wyllie, M. R. J., Gregory, A. R. & Gardner, L. W. (1956).** Elastic wave
  velocities in heterogeneous and porous media. *Geophysics* 21, 41–70.
- **Raymer, L. L., Hunt, E. R. & Gardner, J. S. (1980).** An improved sonic
  transit-time-to-porosity transform. *SPWLA 21st Annual Logging Symposium*.
- **Mavko, Mukerji & Dvorkin, *The Rock Physics Handbook*.** Chapter 7. Level:
  graduate. Includes the empirical relations with their calibration ranges.

## 11. Related lessons

- [05-04-03 Gassmann Fluid Substitution](./03-gassmann-fluid-substitution.md)
- [05-04-07 Electrical Properties, Archie's Law and Clay](./07-electrical-properties-rock.md)
- [09-01-04 Clay and Surface Conduction](../../09-electrical-em-methods/01-electrical-properties-of-earth/04-clay-and-surface-conduction.md)

## Self-assessment checklist

- [ ] I can write both relations with units and check the dimensions.
- [ ] I can derive the time average from a travel-time sum and state its
      geometric assumption.
- [ ] I can compute both relations and report their divergence.
- [ ] I can list the three ways clay defeats a two-component model.
- [ ] I can state a relation's calibrated range and residual before using it.
