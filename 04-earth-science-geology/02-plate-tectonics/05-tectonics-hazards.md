---
id: 04-02-05
title: "Tectonics and the Distribution of Earthquakes and Volcanoes"
level: intermediate
prereqs: ["04-02-02", "04-02-04"]
estimated_minutes: 75
tags: [seismicity, hazard, gutenberg-richter, b-value, recurrence, tsunami, volcano-distribution]
---

# Tectonics and the Distribution of Earthquakes and Volcanoes

The global map of earthquakes and volcanoes is a map of the plate boundaries,
and this lesson is about the chain of reasoning that turns a plate boundary into
a number that an engineer or an emergency planner can use. The chain has four
links, and each is a calculation in this lesson:

1. **The magnitude–frequency relation.** The Gutenberg–Richter law,
   $\log_{10}N(\ge M) = a - bM$, with a $b$-value near 1. Everything downstream
   depends on the $b$-value being estimated correctly, and there is a specific
   way to get it wrong.
2. **Recurrence and probability.** The rate of events above a magnitude gives a
   mean recurrence interval and, through the Poisson model, the probability of
   at least one event in an exposure window.
3. **Recurrence from the plate rate.** Independently of any catalogue, a
   megathrust's area and convergence rate give a moment budget, and the budget
   distributed over magnitudes gives the recurrence of great earthquakes. This
   is a check on the catalogue that uses none of the catalogue's inputs.
4. **Tsunami.** The shallow-water speed and the shoaling amplification decide
   the travel time and the coastal height, and both are one line of arithmetic.

The unifying idea is that **the hazard is a consequence of the kinematics**, and
that a hazard number should be traceable to a plate rate or a catalogue
parameter that the reader can check.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the Gutenberg–Richter relation and estimate a $b$-value by maximum
   likelihood.
2. **Demonstrate** the bias introduced by analysing a catalogue below its
   magnitude of completeness, and explain its direction.
3. **Compute** a recurrence interval and a Poisson probability of exceedance
   for a stated exposure window.
4. **Compute** a megathrust's moment rate from its area and convergence rate,
   and derive the recurrence of great earthquakes by balancing the moment over a
   magnitude distribution.
5. **Explain** why attributing the whole moment budget to a single magnitude is
   wrong, and recognise the implausible number it produces.
6. **Compute** a tsunami's shallow-water speed, travel time and shoaling
   amplification.
7. **Explain** why the offshore amplitude and the travel time are the two
   quantities a warning system depends on.
8. **State** what the seismic coupling coefficient is and why a
   moment-balance recurrence is an upper bound.

## Prerequisites

- [04-02-02 Divergent, Convergent and Transform Boundaries](./02-plate-boundaries.md)
  — the three boundary types and their seismicity and volcanism.
- [04-02-04 Plate Motion Frames, Euler Poles and Global Models](./04-plate-motion-frames.md)
  — the convergence rates the moment budget needs.

## 1. The magnitude–frequency relation

The Gutenberg–Richter law is an empirical power law in the number of events:

$$\log_{10}N(\ge M) = a - bM, \qquad b \approx 1 .$$

A $b$-value of 1 means that each magnitude step reduces the rate by a factor of
ten. The law holds over the magnitude range where the catalogue is complete, and
its two parameters are: $a$, which is the productivity, and $b$, which is the
slope.

The $b$-value is estimated by maximum likelihood (Aki–Utsu):

$$b = \frac{\log_{10}e}{\bar M - M_c},$$

where $\bar M$ is the mean of the magnitudes at or above the completeness
magnitude $M_c$. The formula is short, and the requirement that it be applied
*above* $M_c$ is where almost all the difficulty lies.

The demo generates a synthetic catalogue of one million events from $b = 1.0$
with $M_c = 2.0$, recovers the $b$-value, then simulates network incompleteness
and analyses it two ways:

```text
  Complete catalogue, analysed at Mc = 2.0:
    events used 1000000, recovered b = 0.999 (input 1.000, error -0.1 %)

  Now make the catalogue incomplete below magnitude 3.0 (only 30 per
  cent of the small events recorded, which is what a real network
  did until recently):
    analysed at Mc = 2.0 (wrong): b = 0.696, 369776 events
    analysed at Mc = 3.0 (right):  b = 0.996, 100190 events
```

The first analysis is biased and the second is not. The bias is *flatter* than
the truth — a smaller $b$ means the rate falls more slowly with magnitude, so the
large-event rate looks higher and the hazard looks worse. The fix is not a
better estimator; it is a completeness analysis, and every catalogue used for
hazard should state its $M_c$ and how it was determined.

This is the single most common error in an amateur hazard estimate, and it is
worth understanding why it is so easy to make. Network sensitivity improves over
decades, so an old catalogue is incomplete in a way that depends on time as well
as magnitude; the $M_c$ is then a step function of the date, and a correct
analysis uses one per epoch. The demo's single-step approximation is already a
simplification, and it produces a 30 per cent error in $b$.

## 2. Quantitative treatment: recurrence and probability

Given $b$ and a rate above $M_c$,

$$N(\ge M) = N(\ge M_c)\,10^{-b(M-M_c)} .$$

The demo tabulates the consequence:

```text
       M  rate (per a)   mean interval (a)   P(>=1 in 50 a)   P(>=1 in 500 a)
     4.0            10                 0.1            1.000             1.000
     5.0             1                   1            1.000             1.000
     6.0           0.1                  10            0.993             1.000
     7.0          0.01                 100            0.393             0.993
     8.0         0.001                1000            0.049             0.393
     9.0        0.0001                1e+04            0.005             0.049
```

Two features drive the practice of hazard assessment.

**The recurrence interval is a Poisson average, not a clock.** Ten events per
year at $M\ge4$ gives a mean interval of 0.1 a, and that is an exact statement
about a memoryless process: an event yesterday does not make one tomorrow less
likely. A "100-year recurrence" is a 1 per cent annual probability, not a
promise about the next century.

**The probability accumulates and then saturates**, and it saturates at different
levels for different magnitudes. In a 50-year window the probability of at least
one $M\ge6$ is 0.993 while the probability of at least one $M\ge9$ is 0.005.
That is why a hazard map for a 50-year building code and a hazard map for a
long-lived facility on the same fault are different maps: the exposure time and
the magnitude range that matters for the decision both change, and neither map
is more correct than the other.

The probability is

$$P(\ge 1 \text{ in } T) = 1 - e^{-\text{rate}\times T},$$

which is the Poisson form and is used throughout engineering seismology.

## 3. Quantitative treatment: recurrence from the plate rate

Now do something independent of the catalogue. A subduction megathrust has an
area and a convergence rate, so it has a moment rate:

$$\dot M_0 = \mu A v .$$

For a 1000 km by 150 km megathrust converging at 60 mm/a:

```text
  Area A = 1.500e+11 m^2
  M0 rate = mu A v = 8.556e+12 N m/s
                      = 2.700e+20 N m/a
```

**The naive version of the next step is wrong**, and the demo shows it because
the wrong answer is instructive:

```text
    event Mw     M0 (N m)  naive interval (a)
         7.5    2.239e+20                 0.8
         8.0    1.259e+21                 4.7
         8.5    7.079e+21                26.2
         9.0    3.981e+22               147.4
```

An interval of less than a year for magnitude 7.5 would mean the megathrust
produced one such event every year and had nothing left for anything else. The
error is treating the moment budget as if it were spent on one magnitude rather
than distributed over a magnitude range.

**The correct version balances the moment over the whole distribution.** With
$b = 1$ and magnitudes between 6.0 and 9.5, the Gutenberg–Richter intercept that
matches the moment rate is found by integration:

```text
    a = 6.288, i.e.  N(>=M) = 10^(6.288 - M) per year.

     M >= Mw  rate (per a)   mean interval (a)
         6.0         1.941                   1
         7.0        0.1941                   5
         8.0       0.01941                  52
         9.0      0.001941                 515
```

$M\ge8$ roughly once every fifty years and $M\ge9$ roughly once every five
centuries, with the smaller events filling the time between. Nothing in this used
a catalogue, a regression or an extrapolation of small events: it used the plate
motion of [04-02-04](./04-plate-motion-frames.md) and the assumption that the
magnitude distribution has the standard form.

The algebra is worth writing out once, because it is easy to get a factor of
$\ln 10$ wrong in it. The moment rate is the integral over magnitude of the
moment released in each magnitude band:

$$\dot M_0 = \int M_0(M)\left(-\frac{\mathrm{d}N}{\mathrm{d}M}\right)\mathrm{d}M,
\qquad -\frac{\mathrm{d}N}{\mathrm{d}M} = b\ln 10\;10^{a-bM},
\qquad M_0 = 10^{1.5M+9.1}.$$

With $b = 1$ the $\ln 10$ from the density cancels against the
$1/(0.5\ln 10)$ from the integral of $10^{0.5M}$, leaving

$$\dot M_0 = 2\cdot10^a\cdot10^{9.1}\left(10^{0.5M_\text{max}}
- 10^{0.5M_\text{min}}\right),$$

which is what the demo solves for $a$. A useful internal check comes with it:
attributing the entire budget to $M_w$ 9 alone would give an interval of 147 a,
which is the *shortest* interval any distribution can produce, since nothing else
would then receive any moment. The balanced answer, 515 a, is several times
longer, as it must be.

Two sensitivities decide the answer, and both are worth stating because they are
where the argument is vulnerable.

- **The maximum magnitude dominates.** The moment integral is weighted toward the
  largest magnitudes, so a larger $M_\text{max}$ absorbs more of the budget into
  rare great events and leaves fewer for the smaller ones. The estimate of
  $M_\text{max}$ is therefore the most consequential input to a long-term
  assessment, and it is argued about.
- **The coupling coefficient matters.** The calculation assumes the entire
  convergence is released seismically. Real margins are partly *aseismic*: slow
  slip events and creep accommodate part of the motion without producing strong
  shaking. The fraction released seismically differs between margins by large
  factors and is a target of offshore observatories. So the recurrence above is
  an **upper bound** on the rate of strongly shaking events, and it is a bound
  with a physical meaning rather than a fitted number.

## 4. Physical reasoning: why the events and the volcanoes are where they are

Put the pieces together and the global map follows.

**Earthquakes** occur where the strain rate is high, the rock is brittle, and
the temperature is low enough for brittle failure. That combination exists in
the shallow crust everywhere and in the *cold interior of a subducting slab* to
700 km depth — which is why deep earthquakes exist at all, and why they occur
only in slabs. The deepest earthquakes define the Wadati–Benioff zone, and its
geometry is a direct image of the descending slab.

**Volcanoes** at convergent boundaries occur where water released from the
dehydrating slab enters the mantle wedge and lowers its melting temperature. The
arc sits above the depth where that release happens, which is typically 100 to
150 km above the slab, so the arc–trench distance depends on the slab dip:

$$\text{arc–trench distance} \approx \frac{D}{\tan(\text{dip})},$$

with $D$ the depth to the melting column. For $D = 110$ km, a 30° dip puts the
arc 190 km from the trench, a 45° dip puts it at 110 km, and a 60° dip at 63 km.
That is why volcanic arcs are close to the trench where the slab is steep and
far from it where the slab is shallow, and it is a prediction that is confirmed
wherever the slab geometry is imaged seismically.

**Volcanoes at divergent boundaries** are the direct expression of decompression
melting beneath the ridge, and they are basaltic rather than andesitic because
the melt has not passed through a thick continental crust.

**Transform boundaries** have no reason to produce magma - no material is
created or destroyed — which is why they are the one plate boundary type without
volcanism. The exceptions are at step-overs and pull-apart basins, where local
extension does produce decompression melting, and they are a useful reminder
that the classification describes the boundary and not every feature inside it.

## 5. Quantitative treatment: tsunami

A tsunami is a long-wavelength shallow-water wave, and its speed depends only on
the depth:

$$c = \sqrt{gh}.$$

```text
   depth (m)   c (m/s)  c (km/h)   time over 8000 km (h)
        6000     242.6     873.4                    9.16
        4000     198.1     713.1                   11.22
        2000     140.1     504.3                   15.86
         500      70.0     252.1                   31.73
          20      14.0      50.4                  158.65
```

Across a 4 km deep ocean the wave crosses 8000 km in about eleven hours at
roughly 700 km/h, comparable to a jet's cruising speed. That is the number the
warning system is built on: a tsunami generated at a trench arrives at a distant
coast within hours, so a warning must be issued within minutes of the earthquake
and cannot wait for an analysis of the rupture.

As the wave enters shallow water it slows, and because the energy flux is
conserved the amplitude grows. In the Green's law limit for a slowly varying
depth,

$$\frac{H_2}{H_1} = \left(\frac{h_1}{h_2}\right)^{1/4}.$$

```text
    from depth (m)  to depth (m)  amplification    H_out for H_in = 0.5 m
              4000           200           2.11                      1.06
              4000            50           2.99                      1.50
              4000            20           3.76                      1.88
              4000            10           4.47                      2.24
```

Green's law is an idealisation — it ignores refraction, trapping, reflection,
harbour resonance and run-up on a beach, all of which matter for the height at a
particular address. What it shows is why an offshore wave of half a metre
becomes a serious coastal hazard: the amplification is a factor of three or more
*before* any local effect is added, and the offshore amplitude is therefore a
quantity worth measuring with the seafloor pressure gauges that are now part of
the warning systems.

There is a second effect the shallow-water formula hides. A tsunami's wavelength
is hundreds of kilometres, so it feels the seafloor along its whole length and
shoals over a distance comparable with its own wavelength: the entire wavefront
slows and steepens at once. That is why a tsunami arrives as a wall of water
rather than as a breaking swell, and why the physics of a wind-driven wave does
not apply to it.

## 6. Assumptions and regime of validity

| Assumption | Where it holds | What breaks without it |
|---|---|---|
| Gutenberg–Richter over the analysed range | Above the completeness magnitude, below the maximum | Flattening near $M_\text{max}$ and incompleteness at the low end |
| The catalogue is complete above $M_c$ | After a completeness analysis, per epoch | A $b$-value biased low and a hazard estimate biased high |
| Events are independent and Poisson | For long-term, large-area assessment | Aftershock sequences violate it, and are removed by declustering |
| The moment budget is released seismically | Never exactly | Aseismic and slow slip reduce the rate of shaking events |
| Green's law for shoaling | Slowly varying depth, no resonance | Harbours, shelves and beaches need a full propagation model |
| Shallow-water tsunami theory | Wavelength $\gg$ depth | The deep-ocean generation region near the source |

Two rows deserve a sentence each.

**Declustering.** An $M$ 7 earthquake is followed by hundreds of aftershocks, and
a catalogue that counts them treats a single event as many. The standard fix is
declustering, which removes events that are too close in space and time to be
independent, and every hazard rate should state whether it was applied.

**The near-field tsunami.** The shallow-water theory used above is valid in the
deep ocean, where the wavelength is far greater than the depth. Near the source,
where the rupture displaces the seafloor over a distance comparable with the
water depth, the full linear or non-linear equations are needed, and that is the
domain of a tsunami source model.

## 7. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| Magnitude $M$, $M_w$ | dimensionless | A logarithm of a ratio, so it has no unit |
| $b$-value | dimensionless | The slope of $\log_{10}N$ against $M$ |
| Rate | per year | Must be stated for a magnitude threshold |
| Recurrence interval | years | Reciprocal of the rate |
| Probability | dimensionless, 0 – 1 | $1 - e^{-\text{rate}\,T}$ |
| Seismic moment | N·m | $[\mu A D]$ |
| Tsunami speed | m/s | $[\sqrt{gh}] = \sqrt{\text{m/s}^2 \cdot \text{m}}$ |
| Shoaling factor | dimensionless | A ratio of a fourth root |

Three checks.

**The magnitude-unit check.** A magnitude is a logarithm, so it cannot be
multiplied by anything physical. An "energy" computed as $10^{1.5M + 4.8}$ J is
a definitional conversion, not a measurement, and it inherits the uncertainty of
the empirical constants.

**The rate-unit check.** A rate must carry its threshold: "$0.01$ per year"
without a magnitude is not a rate. A recurrence computed from $N(\ge M)$ for the
wrong $M$ gives a number that is *plausible* at the wrong threshold, which is
why the threshold should be written into every table.

**The tsunami-speed check.** $\sqrt{gh}$ with $g = 9.81$ m/s² and $h = 4000$ m
gives 198 m/s = 713 km/h, matching the table. A depth in kilometres gives 6.3,
which is a number that looks like a velocity but is wrong by a factor of 31.6.

## 8. Python demonstration

[`code/tectonics_hazards_demo.py`](./code/tectonics_hazards_demo.py) generates a
synthetic catalogue from Gutenberg–Richter, estimates the $b$-value with and
without completeness, tabulates recurrence and Poisson probability, computes a
megathrust moment rate and derives a recurrence by magnitude balancing, and
tabulates tsunami travel time and shoaling.

Sections §1 to §5 above quote its output. What each demonstrates:

- **§1**: the estimator is verified on a complete catalogue and *shown to fail*
  on an incomplete one. Demonstrating a method's failure mode is as valuable as
  demonstrating its success.
- **§2**: the Poisson model is applied rather than described, and the saturation
  of the probability is visible in the table.
- **§3**: both the wrong calculation and the right one are printed, because the
  wrong one is the mistake a reader is most likely to make.
- **§5**: the tsunami numbers are computed from $g$ and $h$ and nothing else.

The catalogue is synthetic and the boundary dimensions are illustrative, and the
demo labels both. No specific fault, region or published recurrence estimate is
used, because a real hazard number carries a source model and an uncertainty
that a demonstration cannot supply.

## 9. Common mistakes

1. **Estimating $b$ below the completeness magnitude.** The estimate is biased
   low and the hazard biased high; the demo produces 0.696 against a true 1.0.
2. **Treating a recurrence interval as a schedule.** It is a Poisson average;
   the process has no memory.
3. **Attributing the whole moment budget to one magnitude.** It gives an
   interval of less than a year for $M_w$ 7.5 on a major margin.
4. **Quoting a rate without its magnitude threshold.** A rate of 0.01 per year
   means nothing until the threshold is given.
5. **Using a raw catalogue for a long-term rate.** Aftershocks inflate it;
   decluster first.
6. **Forgetting the coupling coefficient.** A moment-balance recurrence is an
   upper bound because part of the convergence is aseismic.
7. **Applying Green's law to a harbour.** Resonance, refraction and run-up
   dominate the height at a specific location.
8. **Using a depth in kilometres in $\sqrt{gh}$.** A factor of 31.6, and the
   result looks like a wave speed.

## 10. Real-world applications

- **Building codes and design spectra.** A probabilistic hazard map is derived
  from exactly the recurrence and probability calculations in §2 and §3, with an
  attenuation model added ([04-07-01 Earthquake Hazard](../07-geologic-hazards/01-earthquake-hazard.md)).
- **Tsunami warning systems.** The travel-time table of §5 is the basis for
  deciding when a warning can be issued and which coasts need one
  ([04-07-05 Tsunami](../07-geologic-hazards/05-tsunami.md)).
- **Volcanic hazard and monitoring.** The arc position and the magma supply set
  which volcanoes exist, and the monitoring strategy follows from the expected
  style ([04-07-02 Volcanic Hazards](../07-geologic-hazards/02-volcanic-hazards.md)).
- **Insurance and catastrophe modelling.** A catalogue-based recurrence model is
  the input to a loss model, and its $M_c$ and coupling assumptions are the
  first things an auditor checks.
- **Long-term facility siting.** For a repository or a dam, the exposure window
  is $10^4$ to $10^6$ years and the relevant magnitudes are the largest
  conceivable ones, which is the opposite of the 50-year building-code problem.

## 11. Further reading

- **Gutenberg, B., & Richter, C. F. *Seismicity of the Earth and Associated
  Phenomena* (Princeton University Press).** The origin of the relation.
  Level: intermediate.
- **Aki, K. (1965). Maximum likelihood estimate of b in the formula
  log N = a - bM and its confidence limits. *Bulletin of the Earthquake
  Research Institute* 43, 237–239.** The estimator of §1. Level: advanced.
- **Kanamori, H. (1977). The energy release in great earthquakes. *Journal of
  Geophysical Research* 82, 2981–2987.** The moment–magnitude relation behind
  the moment budget. Level: advanced.
- **Stein, S., & Wiemer, S. (2009). *Earthquake rate and moment rate* and
  related work on catalogue completeness.** Recent treatments of $M_c$ and the
  catalogue bias; search the current literature for the latest review.
- **Ward, S. N., & Asphaug, E. (2000) and the tsunami literature.** Tsunami
  generation and propagation, including where shallow-water theory fails.
  Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04-02-02 Divergent, Convergent and Transform Boundaries](./02-plate-boundaries.md)
  — the boundary types whose signatures this lesson quantifies.
- [04-02-04 Plate Motion Frames, Euler Poles and Global Models](./04-plate-motion-frames.md)
  — the convergence rate the moment budget uses.
- [04-02-03 Mantle Convection, Slab Pull and Ridge Push](./03-driving-forces.md)
  — why the convergence happens at the rate it does.
- [04-07 Geologic and Geophysical Hazards](../07-geologic-hazards/README.md) —
  where these rates become engineering decisions.
- [21 Statistics, Bayesian Inference and Machine Learning](../../21-statistics-bayesian-ml/README.md)
  — the estimation theory behind the $b$-value and the completeness analysis.

Exercises:
[`exercises/05-tectonics-hazards-exercises.md`](./exercises/05-tectonics-hazards-exercises.md)
and
[`exercises/05-tectonics-hazards-solutions.md`](./exercises/05-tectonics-hazards-solutions.md).

## Self-assessment checklist

- [ ] I can estimate a $b$-value by maximum likelihood above $M_c$. (§1)
- [ ] I can explain the direction and size of the bias from using a too-low
      $M_c$. (§1)
- [ ] I can compute a recurrence interval and a Poisson exceedance probability.
      (§2)
- [ ] I can compute a moment rate and balance it over a magnitude distribution.
      (§3)
- [ ] I can explain why attributing the budget to one magnitude is wrong. (§3)
- [ ] I can state the two inputs that dominate a moment-balance recurrence. (§3)
- [ ] I can explain why deep earthquakes occur only in slabs, and where a
      volcanic arc sits relative to a slab. (§4)
- [ ] I can compute a tsunami speed, travel time and shoaling factor. (§5)
- [ ] I can check the units of a magnitude, a rate and a wave speed. (§7)
- [ ] I can state what declustering and the coupling coefficient change. (§6)
