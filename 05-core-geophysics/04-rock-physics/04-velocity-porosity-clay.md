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

## Extended worked example: which uncertainty actually controls the answer?

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
