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

### 3.1 Inverting the amplitude law: the maximum detectable depth

Feasibility is usually asked backwards. Not "what anomaly will this body give?"
but "how deep can I see this contrast with this noise?" That is the same
equation, solved for $d$.

**Three-dimensional compact body.** With $m = \Delta\rho\,V$ and
$A = Gm/d^2$, requiring $A \ge k\sigma$ gives

$$d_{\max} = \sqrt{\frac{G\,\Delta\rho\,V}{k\,\sigma}} .$$

Dimensional check: $[\mathrm{m^3kg^{-1}s^{-2}\cdot kg\,m^{-3}\cdot m^3}/(\mathrm{m\,s^{-2}})]
= \mathrm{m^2}$, so $d_{\max}$ is metres. ✓

**Worked arithmetic.** $\Delta\rho = 500$ kg/m³, sphere radius 60 m
($V = 9.0478\times10^{5}$ m³), $k = 3$, $\sigma = 1\times10^{-7}$ m/s²
(= 0.01 mGal):

$$d_{\max} = \sqrt{\frac{(6.6743\times10^{-11})(500)(9.0478\times10^{5})}
{3\times10^{-7}}} = 317.2\ \mathrm{m}.$$

So a 120 m diameter, 500 kg/m³ body is a 3-sigma target to about 320 m and
nothing more. Note the square root: to double the reach you must *quadruple*
the excess mass, or reduce the noise fourfold, or accept half the confidence.

**Two-dimensional tabular body.** With $A = 2G\lambda/d$ the same inversion gives
$d_{\max} = 2G\lambda/(k\sigma)$ — *linear* in the contrast, not a square root.
That is the geometric advantage of tabular bodies: reach grows faster with
contrast.

### 3.2 The magnetic projection factor, derived

This is the step most often skipped, and it is the one that decides whether a
magnetic survey has any signal at all.

Let a uniformly magnetised body have moment $\mathbf{m}$. The total-field anomaly
is the projection of the anomaly on the ambient field direction
([05-02-02](../02-geophysical-fields-and-observables/02-field-measurement-units.md)):

$$\Delta T = \hat{\mathbf{b}}\cdot\mathbf{B}_\text{anom}
= \frac{\mu_0}{4\pi}\frac{3(\mathbf{m}\cdot\hat{\mathbf{r}})
(\hat{\mathbf{b}}\cdot\hat{\mathbf{r}}) - \mathbf{m}\cdot\hat{\mathbf{b}}}{r^3}.$$

Now observe **directly above** the body, so $\hat{\mathbf{r}}$ is vertically
downward, and suppose the magnetisation is *induced*, so that $\mathbf{m}$ is
parallel to $\hat{\mathbf{b}}$ (modulus $m$). Then
$\mathbf{m}\cdot\hat{\mathbf{r}} = m\sin I$ and
$\hat{\mathbf{b}}\cdot\hat{\mathbf{r}} = \sin I$ where $I$ is the inclination,
while $\mathbf{m}\cdot\hat{\mathbf{b}} = m$. Substituting:

$$\Delta T = \frac{\mu_0}{4\pi}\frac{m}{r^3}
\left(3\sin^2 I - 1\right).$$

Define the **projection factor** $F(I) \equiv 3\sin^2I - 1$. Its properties are
the content of the whole exercise:

- $F(90°) = +2$: the axial dipole factor, the largest possible;
- $F(0°) = -1$: the equatorial factor, half the magnitude and opposite in sign;
- $F(I) = 0$ at $\sin^2 I = \tfrac13$, i.e.

$$I_\text{null} = \arcsin\!\left(\frac{1}{\sqrt{3}}\right) = 35.264^\circ .$$

**Measured check.** For $m = 5\times10^{6}$ A m², $r = 300$ m:

| $I$ | $F = 3\sin^2I-1$ | $\Delta T$ (nT) |
|---|---|---|
| 0° | $-1.000000$ | $-18.518519$ |
| 20° | $-0.649067$ | $-12.019753$ |
| **35.2644°** | $+0.000001$ | $+0.000009$ |
| 45° | $+0.500000$ | $+9.259259$ |
| 60° | $+1.250000$ | $+23.148148$ |
| 90° | $+2.000000$ | $+37.037037$ |

A real body at a real latitude near 35° becomes **invisible in a single vertical
total-field reading**, while the same body at 90° gives 37 nT. The null is
*derived*, not fitted, and it is why magnetic surveys at mid-latitudes require
either an offset profile or a component measurement rather than a single
station.

**Physical interpretation.** A magnetometer measures a projection, and a
projection can be zero. Detection planning must evaluate $F(I)$ *before*
spending money: at $I$ near 35° a vertical-station magnetic survey is
indefensible regardless of instrument quality, whereas gravity over the same
body at the same depth is unaffected by any of this.

### 3.3 EM feasibility from the skin depth, inverted

For a diffusive target at depth $d$ in a half-space of conductivity $\sigma$,
require $\delta \ge d$ with $\delta = \sqrt{2/(\mu\sigma\omega)}$. Solving for
the period,

$$\delta^2 = \frac{2}{\mu\sigma\omega} = \frac{T}{\pi\mu\sigma}
\qquad\Longrightarrow\qquad
\boxed{\;T \ge \pi\mu\sigma d^2\;}$$

Dimensional check: $[\mathrm{H\,m^{-1}\cdot S\,m^{-1}\cdot m^2}] =
\mathrm{s}$. ✓

**Worked arithmetic.** $\sigma = 0.02$ S/m, $d = 500$ m:
$T \ge \pi(1.2566\times10^{-6})(0.02)(500)^2 = 0.0197$ s. At 1 Hz the skin depth
is 3559 m — far more than enough. So the constraint is not penetration at all;
it is resolution and signal strength, which must be modelled.

### 3.4 The cost side: why deep targets are expensive

Section 3.1 shows reach scales as $\sqrt{\Delta\rho V/\sigma}$ for compact bodies
and linearly in $\lambda$ for tabular ones. Combine that with the information
penalty of [05-01-03](./03-resolution-depth-tradeoff.md) — information about a
compact source falls as $d^{-3}$ — and the economics become explicit:

- to reach twice as deep at constant confidence, a compact body needs
  **8 times** the information;
- information can be bought by longer integration (noise $\propto 1/\sqrt{\tau}$),
  by more stations (noise $\propto 1/\sqrt{N}$), or by a bigger contrast.
- Since $\sqrt{\tau}$ and $\sqrt{N}$ both enter weakly, the cost of depth grows
  much faster than the depth itself. **This is the quantitative reason deep
  exploration uses large, expensive sources or accepts coarse resolution.**

### 3.5 The minimum detectable mass, derived

Invert the amplitude law once more, this time for the mass rather than the depth.
Requiring $Gm/d^2 \ge k\sigma$ gives the **minimum detectable mass** at a stated
depth:

$$m_{\min} = \frac{k\,\sigma\,d^2}{G} .$$

Dimensional check: $[\sigma d^2/G] = (\mathrm{m\,s^{-2}})(\mathrm{m^2})/
(\mathrm{m^3kg^{-1}s^{-2}}) = \mathrm{kg}$ ✓.

**Worked arithmetic** for $k = 3$, $\sigma = 1\times10^{-7}$ m s⁻² (0.01 mGal),
$d = 400$ m:

$$m_{\min} = \frac{3\cdot10^{-7}\cdot1.6\times10^{5}}{6.6743\times10^{-11}}
= 7.19\times10^{8}\ \mathrm{kg}.$$

Requiring a density contrast of 500 kg/m³ (a stated synthetic value), that mass
needs a volume of $1.44\times10^{6}$ m³, i.e. a sphere of radius 70 m. **The
calculation converts "can we see it?" into "how big must it be?" — a form a
geologist can answer directly.**

**Physical interpretation of the $d^2$.** The minimum detectable mass grows as the
*square* of depth, while the minimum detectable *contrast* at fixed volume grows
the same way. Doubling the depth therefore requires four times the excess mass,
or four times the contrast, or a fourfold reduction in noise. **Depth is the
expensive variable in potential-field exploration**, and that single exponent
explains most of the economics of the method.

**A design consequence.** Because $m_{\min}\propto\sigma$, and $\sigma$ is set by
the combined instrument, positional and geological noise, spending effort on
*positioning and correction quality* buys detection limit linearly — whereas
spending the same effort on a more sensitive instrument buys it only to the
extent that the instrument term is the dominant one. In most surveys it is not.

### 3.6 The value of a survey, derived

Feasibility asks whether a method *can* see the target. A budget asks whether it
is *worth* seeing. The two are different, and the second has a derivation.

Let the prior probability that the target exists be $p$, the value of acting
correctly be $V$ (finding it), the cost of acting on a false positive be $C$, and
the cost of the survey itself be $S$. A survey with detection probability
$p_d$ and false-alarm probability $p_f$ changes the expected value by

$$\Delta\mathbb{E} = p\,p_d\,V - (1-p)\,p_f\,C - S .$$

The survey is worth running iff $\Delta\mathbb{E} > 0$, i.e.

$$S < p\,p_d\,V - (1-p)\,p_f\,C .$$

**Read the structure.** The survey's value grows with the prior $p$ — which is why
regional-scale reconnaissance that raises $p$ cheaply is often better value than
a local detailed survey. It grows with the detection probability $p_d$, which is
the quantity the CNR calculation estimates. And it is *reduced* by false alarms,
which is why the geological-noise term $\sigma_\text{geol}$ of Section 2 enters the
economics and not only the physics.

**Worked arithmetic.** With $p = 0.3$, $p_d = 0.7$, $V = 10$ M, $C = 1$ M,
$p_f = 0.1$:

$$S < 0.3\cdot0.7\cdot10 - 0.7\cdot0.1\cdot1
= 2.10 - 0.07 = 2.03\ \text{M}.$$

So a survey costing less than about 2 M is worth running *on these numbers* —
and the numbers themselves are the model. **The derivation's value is not the
arithmetic but the identification of the four quantities that must be stated**,
because a proposal that omits $p$ and $C$ is not making an argument at all. Note
also how weak the dependence on $p_f$ is here (0.07 M against a 2.10 M benefit):
false alarms matter economically only when the cost of acting on them is
comparable to the value of a discovery.

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

### 6.1 A shortcut that gives an absurd answer, and why that is informative

**The shortcut:** apply the 2-D tabular formula to the buried channel of
Section 6 and solve for the depth at which it becomes a 3-sigma target.

**The arithmetic.** $\lambda = \Delta\rho\times\text{width} = 250\times15 =
3750$ kg/m, $\sigma = 1\times10^{-7}$ m/s², $k = 3$:

$$d_{\max} = \frac{2G\lambda}{k\sigma}
= \frac{2(6.6743\times10^{-11})(3750)}{3\times10^{-7}}
= 1.67\ \mathrm{m}.$$

**The answer is nonsense.** A 1.7 m "maximum depth" for a body whose contrast
was described as strong means the model, not the survey, has failed. The reason
is the assumption: the 2-D line-mass solution is valid only for $d$ comparable
to or greater than the body's *width* (here 15 m). At $d = 1.67$ m the
observation would be inside the body's own footprint and the line approximation
is meaningless. The algebra is correct; its domain of validity is violated.

**What the shortcut has actually told you.** Two things, both useful:

1. By the 3-D formula (Section 3.1) with $V = 15\times4\times100 = 6000$ m³ and
   $\Delta\rho = 250$:
   $d_{\max} = \sqrt{(6.6743\times10^{-11})(250)(6000)/(3\times10^{-7})} = 18.3$ m.
   So the target's *depth range* of 25–40 m is beyond gravity's reach by a factor
   of 1.4–2.2 in depth — a factor of 2–5 in required mass. That is a real,
   defensible conclusion.
2. The exercise has exposed, quantitatively, why **the generalisable rule is to
   check the model's validity domain before quoting its output**. A number that
   lies outside the assumptions of the formula that produced it is not a result;
   it is a symptom.

**The generalisable lesson.** Every feasibility formula carries a domain:
$d \gtrsim$ body dimension for point-mass/line-mass approximations, $\delta \ge d$
for the skin-depth argument, low frequency for Gassmann, and so on. Compute the
number, then check that the number lies inside the domain. When it does not,
change the model — do not report the number.

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
