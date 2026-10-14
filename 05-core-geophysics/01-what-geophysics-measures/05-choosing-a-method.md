---
id: 05-01-05
title: "Choosing a Method: A Decision Framework"
level: intermediate
prereqs: ["05-01-01", "05-01-02"]
tags: [survey-design, decision-framework, method-selection, cost]
---

# Choosing a Method: A Decision Framework

## Learning objectives

1. **Apply** a six-question framework that maps a stated objective to a method
   family.
2. **Compute** the contrast-to-noise ratio for a candidate method before any
   field work.
3. **Rank** candidate methods using an explicit, auditable scoring procedure
   rather than intuition.
4. **Identify** the failure mode that will kill a survey (access, contrast,
   resolution, cost) and test for it first.
5. **Document** a method decision so that a reviewer can reproduce it.

## Prerequisites

- [05-01-01 The Central Idea](./01-physical-property-contrast.md)
- [05-01-02 Taxonomy of Methods](./02-method-taxonomy.md)
- [05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off](./03-resolution-depth-tradeoff.md)

## 1. Intuition: choose the contrast, then the geometry

Method selection goes wrong when it starts from the method. The reliable order
is:

1. **What physical property difference does the target actually have?** If you
   cannot answer with a range and a source, you are not ready to design a
   survey.
2. **What is the required resolution and depth?** These two are linked
   (Section 3 of the previous lesson), so state both.
3. **What is the noise budget?** Instrument, access, cultural, geological.
4. **What method senses that contrast with that resolution at that depth?**
5. **What geometry delivers the required sampling?**
6. **What is the cost, and what is the cheaper test that would falsify the
   plan?**

Only then choose hardware.

## 2. Precise definitions

**Objective.** A falsifiable statement of what will be learned: "locate a body
of at least 5 m thickness with a density contrast above 300 kg/m³ to within
20 m horizontally and 10 m in depth, to 150 m depth."

**Contrast-to-noise ratio (CNR).** For a proposed method with predicted
anomaly amplitude $A$ and total uncertainty $\sigma$:

$$\mathrm{CNR} = \frac{A}{\sigma}, \qquad \sigma = \sqrt{\sigma_\text{instr}^2 + \sigma_\text{model}^2 + \sigma_\text{geol}^2}.$$

The geological noise term $\sigma_\text{geol}$ covers everything that varies in
the subsurface besides the target; in real surveys it is usually the largest.

**Feasibility test.** CNR $> 3$ before acquisition is the minimum bar for a
plan that has any chance.

## 3. Derivation: the CNR for each family, from first principles

**Gravity (compact body, point-mass approximation).**

$$A = \frac{G\,\Delta\rho\,V}{d^2}, \qquad V = \tfrac43\pi a^3.$$

Units: $[G\Delta\rho V] = \mathrm{m^3kg^{-1}s^{-2}\cdot kg\,m^{-3}\cdot m^3}
= \mathrm{m^3s^{-2}}$, divided by $\mathrm{m^2}$ gives $\mathrm{m\,s^{-2}}$.

**Magnetics (dipole, projected).**

$$A = \frac{\mu_0}{4\pi}\frac{|\mathbf{m}|}{d^3}\cdot P(\theta_m,\theta_b),$$

where $P$ is the projection factor of the ambient field on the anomaly.
$P$ can be zero — this is the Section 6.2 result of
[05-01-01](./01-physical-property-contrast.md), and it must be evaluated before
the survey, not after.

**EM (diffusive).** The signal at depth $d$ scales as $e^{-d/\delta}$, so
feasibility requires $d \lesssim \delta$ with the *longest usable period*:
choose $T$ from $\delta = \sqrt{2T/(2\pi\mu\sigma)} \ge d$.

**Seismic.** The signal is a reflection coefficient $R$ multiplied by
transmission losses; feasibility is a modeling question, not a formula, and the
right test is a synthetic shot gather.

## 4. Units and dimensional analysis

| Candidate method | Predicted amplitude | Reference noise | Field unit |
|---|---|---|---|
| Gravity | $\mu$m s⁻² range | 0.01–0.05 mGal (relative) | mGal |
| Magnetics | tens to thousands nT | 1–5 nT (modern), 10 nT (older) | nT |
| DC resistivity | tens of mV | 1% of reading | mV/V |
| TEM | $\mu$V A⁻¹ m⁻⁴ decay | instrument-dependent | V A⁻¹ |
| Seismic | reflection amplitude ~0.01–0.3 | ambient noise floor | dimensionless |

The magnetic noise *does not scale with the field*, which is why magnetic
surveys work at low latitudes as well as high: the instrument is fine; it is the
*signal* that vanishes.

## 5. Assumptions

1. **The contrast estimate is honest.** If it came from a remembered "typical"
   value rather than a measurement or a cited range, the whole design rests on
   nothing.
2. **An approximate forward model is adequate for feasibility.** It is; a factor
   of two error in CNR changes the design, a factor of two error in a full
   modelling study does not.
3. **$\sigma_\text{geol}$ can be bounded.** Often this is the hardest step and
   the reason to fly a test line before the main survey.
4. **Costs are known.** Feasibility and affordability are separate gates.

## 6. Worked example: an auditable decision

**Objective (stated).** Find a buried channel, 20 m wide, 5 m thick, at 40 m
depth, filled with material 300 kg/m³ less dense and 3 times more resistive than
the host, in an area with 1 m of soil cover and paved access.

**Step 1 — contrast candidates.** Density contrast 300 kg/m³ over
$20\times5\times100$ m: $V = 10^4$ m³, excess mass
$= 300\cdot10^4 = 3\times10^6$ kg. At $d = 40$ m,
$A = G\Delta m/d^2$ if compact, but the channel is tabular, so the 2-D line
formula applies: $A \approx 2G\lambda/d$ with $\lambda = 300\cdot100$ kg/m
$= 3\times10^4$ kg/m:

$$A \approx \frac{2(6.6743\times10^{-11})(3\times10^4)}{40}
= 1.00\times10^{-7}\ \mathrm{m\,s^{-2}} = 0.010\ \mathrm{mGal}.$$

That is at the level of gravimeter repeatability — marginally feasible at best,
and hopeless once geological noise is included.

**Step 2 — resistivity.** A 3:1 resistivity contrast at 40 m depth with a
20 m target is well within a standard multi-electrode survey; the electrode
spacing must be $\lesssim 10$ m to resolve 20 m laterally.

**Step 3 — decision.** EM or ERT, not gravity. The gravity contrast is real but
too weak at that depth; the resistivity contrast is strong and the geometry is
favourable.

**Step 4 — falsification test.** Before the full survey, occupy one 200 m line
with 5 m electrode spacing and check that the background resistivity is
homogeneous to within a factor of 2. If not, the plan is void.

Every number is either derived from the stated objective or measured; none is a
remembered constant.

## 7. Python demonstration

Use `code/property_contrast_demo.py` to generate the CNR table for a candidate
model, and `code/resolution_depth_demo.py` to convert a required lateral
resolution into a maximum target depth. The workflow is: pick the contrast,
compute the amplitude, divide by the stated noise, and print the decision. The
demo prints units so the arithmetic can be checked by hand.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/05-choosing-a-method-exercises.md`](./exercises/05-choosing-a-method-exercises.md).

**Common mistakes.**

1. **Starting from the method you own.** Ownership is a cost argument, not a
   physical one.
2. **Skipping the CNR calculation.** It takes twenty minutes and can save a
   season.
3. **Ignoring the magnetic projection factor.** A survey planned for a vertical
   magnetisation in a horizontal field is a survey with no signal.
4. **Treating geological noise as technical noise.** It is usually dominant and
   usually irreducible.
5. **Designing for the average case.** A target that is detectable at the
   median contrast may be invisible in most of the area.
6. **Failing to state the objective numerically.** "Map the bedrock" is not an
   objective; "resolve bedrock to 5 m at 30 m depth" is.

**Real-world applications.**

- **Groundwater exploration** selects EM or resistivity because the contrast is
  in the pore fluid.
- **Mineral exploration** uses magnetics first because it is cheap and fast,
  then gravity, EM or IP for the specific target.
- **Geotechnical site investigation** uses seismic (MASW/refraction) and GPR
  because the required resolution is metres and the depths are shallow.
- **Environmental monitoring** requires repeatability, which pushes toward
  methods with a stable datum (EM, seismic) rather than absolute-field ones.

## 9. Further reading

- **Kearey, Brooks & Hill (2002). *An Introduction to Geophysical
  Exploration*.** Chapter 1 and the method chapters. Level: beginner to
  intermediate. The classic practical framing.
- **Milsom, J. & Eriksen, A. *Field Geophysics* (4th ed.).** Level:
  intermediate. Design reality: access, cost, logistics.
- **Dentith, M. & Mudge, S. T. (2014). *Geophysics for the Mineral Exploration
  Geoscientist*.** Chapters 2–3. Level: intermediate. Contrast-driven method
  selection in practice.

## 10. Related lessons

- [05-01-04 Non-Uniqueness of Geophysical Models](./04-ambiguity-and-nonuniqueness.md)
- [05-05-01 Survey Planning: Objectives, Target Resolution, Budget](../05-survey-design-and-acquisition/01-survey-planning.md)
- [05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off](./03-resolution-depth-tradeoff.md)

## Self-assessment checklist

- [ ] I can write an objective as a falsifiable numeric statement.
- [ ] I can compute a CNR for gravity, magnetics and EM from stated inputs.
- [ ] I can evaluate the magnetic projection factor for a given latitude.
- [ ] I can name the four failure modes and the cheapest test for each.
- [ ] I can justify a method choice with a calculation a reviewer can repeat.
