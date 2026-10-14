---
id: 05-08-01
title: "The Borehole Environment and Invasion Profiles"
level: advanced
prereqs: ["05-07-04", "02-06-01", "09-01-01"]
tags: [borehole, invasion, mud-filtrate, environmental-corrections, logging, formation-damage]
---

# The Borehole Environment and Invasion Profiles

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** the borehole as a physical perturbation of the formation, and list
   the six quantities that a wireline tool measures *about the borehole* before
   it measures anything about the rock.
2. **Solve** radial filtrate invasion from a fixed wall concentration, and state
   why the cylindrical geometry makes the front advance more slowly than the
   planar $\sqrt{t}$ law.
3. **Compute** the invasion profile, the 50 per cent invasion radius, and the
   response of tools with different depths of investigation.
4. **Quantify** the effect of each environmental correction — hole size, mud
   weight, mudcake, temperature and salinity — and say what happens if it is
   omitted.
5. **Distinguish** mud-filtrate resistivity from formation-water resistivity, and
   explain why confusing them destroys a saturation calculation.
6. **State** the honest limits of a borehole measurement: it samples a cylinder
   of order metres, along a line, after drilling has already changed it.

## Prerequisites

- [05-07-04 Ground Truthing: Boreholes, Outcrop and Drill Core](../07-interpretation-and-integration/04-ground-truthing.md)
  — what a borehole can and cannot validate.
- [02-06-05 Flow Through Porous Media](../../02-physics/06-fluid-mechanics/05-porous-media-flow.md)
  — Darcy flow and the pressure relations behind overbalance, mudcake growth and
  invasion.
- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md)
  — the conductivity scale of mud, filtrate and formation water.

## 1. Intuition: the borehole is an experiment performed on the rock

A borehole is a hole filled with fluid, held at a pressure chosen by the driller.
The instant it is drilled:

1. **The stress state is changed.** Rock that was confined is now free to move
   into the hole. This is why caliper logs measure an *enlarged* hole in weak
   rocks and why borehole breakouts reveal stress orientation
   ([02-04-08 Failure, Friction and the Brittle Regime](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md)).
2. **The fluid is replaced.** Drilling fluid invades the permeable rock, displacing
   the in-situ fluid. The zone nearest the wall is almost completely flushed; the
   transition back to virgin fluid is the **invasion profile**.
3. **The temperature is reset.** Drilling fluid is cooler than the formation at
   depth, and the hole takes time to re-equilibrate — the subject of
   [05-09-01](../09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md).
4. **The fluid pressure differs from the formation pressure.** The driller keeps
   the mud pressure slightly above the pore pressure (**overbalance**) to prevent
   inflow, and it is that overbalance which drives the invasion.

The consequence is the discipline of the whole module: **every log is an
invasion-modified measurement of a disturbed formation, made through a fluid of
known but imperfectly known properties, in a hole whose size is not the bit
size.** The three corrections that follow from that sentence — invasion,
environmental, and geometry — are where a log goes wrong silently.

## 2. Precise definitions

### 2.1 Overbalance, mudcake and spurt loss

**Overbalance** is $\Delta p = p_{\text{mud}} - p_{\text{pore}} > 0$. When the mud
column contacts permeable rock, the solid phase deposits a filter cake
(**mudcake**) whose thickness grows while the filtrate volumed passed per unit
area slows. The initial flush before the cake forms is the **spurt loss**;
thereafter the flow is approximately proportional to $1/\sqrt{t}$.

### 2.2 Invaded zone, flushed zone, transition zone

- **Flushed zone ($R_{xo}$).** Nearest the wall, where the movable fluid has been
  displaced by filtrate. Its resistivity is written $R_{xo}$.
- **Transition zone.** Where filtrate and formation fluid are mixed.
- **Virgin (uninvaded) zone ($R_t$).** Beyond the invasion, the formation's own
  resistivity $R_t$.

The pair $(R_{xo}, R_t)$ is the *first* thing a resistivity interpretation uses,
and the *difference* between a shallow and a deep reading is the only direct
evidence that invasion occurred.

### 2.3 Depth of investigation

The **depth of investigation** of a tool is the radial distance from the wall
within which, say, 90 per cent of its signal originates. It is a property of the
tool *and* the formation, and it must be quoted with the weighting function used
to define it (Section 3.3).

### 2.4 Environmental corrections

Six corrections are applied routinely, each of which changes the reading:

| Correction | What it corrects for | Consequence if omitted |
|---|---|---|
| Hole size / caliper | Signal originating in the fluid-filled hole rather than the rock | Porosity and density biased by several per cent; worst in washed-out or under-gauge holes |
| Mud weight / mud type | The fluid column's density contrast and its (K, U, Th) content in the gamma channels | Density and neutron offsets that vary with the mud programme |
| Mudcake | A layer of different density and slowness between tool and formation | Density and sonic wrong by a few per cent in permeable zones |
| Temperature | The tool's response drifts, and fluid and rock properties are temperature-dependent | Drift that looks like a formation trend |
| Salinity | The fluid's density and hydrogen index, and the water resistivity $R_w$ | Porosity wrong in the fluid term; $R_w$ wrong by a large factor |
| Pressure | Small effect on most tools, larger on NMR and on fluid properties | Usually negligible; state that you checked |

None of these is a fixed number. Each is a *service-company chart or algorithm*
that differs between tools and vintages, which is why the correction must be
identified by name and version in the report, and why no value in this lesson is
quoted as a specification.

## 3. Derivations

### 3.1 Radial diffusion of filtrate

Take the filtrate concentration $c(r,t)$ as the fraction of the pore fluid that is
mud filtrate, with a constant wall value (mudcake control) and an initially
invaded-free formation. Conservation with Fickian mixing gives, in cylindrical
coordinates,

$$\frac{\partial c}{\partial t} = \frac{1}{r}\frac{\partial}{\partial r}
\left(r D \frac{\partial c}{\partial r}\right), \qquad
c(r_w,t) = 1,\quad c(r,0) = 0, \tag{1}$$

which the demonstration solves with Crank–Nicolson on a fine radial grid.

### 3.2 Why the front is *not* $\sqrt{t}$ in a borehole

In plane geometry equation (1) collapses to pure diffusion, whose front position
grows exactly as $t^{1/2}$. The demonstration verifies that: its planar front
positions are 0.0976, 0.3128 and 0.9883 m at 10, 100 and 1000 h, giving measured
exponents **0.5058** and **0.4997**. Then the same solver on the cylindrical
problem gives front positions 0.1701, 0.2596 and 0.4338 m, with exponents
**0.1835** and **0.2229**.

The reason is dimensional, not numerical. Cylindrical diffusion from a fixed
radius has *three* length scales: $r_w$, $\sqrt{Dt}$ and the outer boundary. It is
therefore **not self-similar**, and no single $\sqrt{Dt}$ law can describe it. The
measured exponent is converged in grid size (0.183–0.187 and 0.209–0.223 across a
fourfold refinement) but depends weakly on the outer boundary distance, so it is
reported as a range and *not* as a universal law. Real invasion is also partly
advective and mudcake-controlled; this model isolates the geometry.

> **What to carry away.** "Invasion goes as the square root of time" is a planar
> result. In a borehole it is an approximation, and the honest statement is that
> invasion slows markedly with time — the first decade of time matters far more
> than the second.

### 3.3 Tool response as a weighted radial average

Model a tool's response by an exponential radial weighting of the formation
property. For a shallow-reading tool,

$$w_s(r) \propto e^{-(r-r_w)/L_s}\, r, \qquad L_s = 0.15\ \mathrm{m}
\ \text{(SYNTHETIC)}, \tag{2}$$

and for a deep-reading tool $L_d = 1.5$ m. The apparent conductivity is then

$$\sigma_{\text{app}} = \frac{\int \sigma(r) w(r)\,\mathrm{d}r}{\int w(r)\,\mathrm{d}r}.
\tag{3}$$

The measured responses are:

| Time (h) | $R_{\text{inv}}$ (m) | $\sigma_{\text{shallow}}$ (S/m) | $\sigma_{\text{deep}}$ (S/m) | ratio |
|---|---|---|---|---|
| 10 | 0.170 | 0.5297 | 0.0712 | 7.44 |
| 100 | 0.260 | 0.9634 | 0.1352 | 7.13 |
| 1000 | 0.434 | 1.2957 | 0.3573 | 3.63 |
| 2778 | 0.526 | 1.3762 | 0.4633 | 2.97 |

Two things are visible and both are used in practice. Early on, the shallow/deep
ratio is large — that *is* the invasion signal. As the front passes the deep
tool's reach, the ratio collapses and the deep reading is itself contaminated.

### 3.4 Depth of investigation, quantified

From equation (2), the fraction of the signal from within radius $r$ is
$\int_{r_w}^{r} w\,\mathrm{d}r / \int w\,\mathrm{d}r$, which for $r-w \ll L$
varies nearly as $(r - r_w)^2$ because of the $r$ factor. For $L_s = 0.15$ m, 50
per cent of the signal comes from within about 0.13 m and 90 per cent from within
about 0.36 m of the wall. Quote the weighting function whenever you quote a depth
of investigation; without it the number is arbitrary.

### 3.5 Saturation and the cost of ignoring invasion

Archie's law in the form $S_w^n = aR_w/(\phi^m R_t)$ gives, with the synthetic
values of the demonstration ($R_w = 20$ Ω m, $R_{mf} = 1$ Ω m, $\phi = 0.25$,
$a = m = n = 1, 2, 2$, true $S_w = 0.4$):

- true $R_t = 2000$ Ω m;
- the deep apparent reading is 22.65 Ω m — **two orders of magnitude low**;
- the uncorrected $S_w$ from that reading is **3.759**, i.e. greater than 1.

A saturation above 1 is the honest diagnosis: the reading is filtrate-dominated
and no saturation can be computed from it. Then the two-reading inversion:

| Case | $R_t$ recovered | $S_w$ recovered |
|---|---|---|
| Smooth diffusion profile (truth) | 40.35 Ω m ($-98.0$ %) | 2.816 |
| Genuine step profile | 1722.04 Ω m ($-13.9$ %) | 0.431 (true 0.4) |

The step-profile case works (to 8 per cent in $S_w$) and the smooth one fails,
because the correction *is* a model of the invasion geometry. Note also the
conditioning: the deep tool's geometric factor is only 0.019, so the two-equation
system amplifies small errors by roughly 15-fold.

### 3.6 Two resistivities that are constantly confused

- $R_w$: the **formation water** resistivity. It is a property of the rock's
  water, enters Archie's law, and is obtained from a produced-water sample, a
  water catalogue, or an SP-derived estimate.
- $R_{mf}$: the **mud filtrate** resistivity. It is a property of the drilling
  fluid, sets $R_{xo}$, and is measured at the flowline with a resistivity cell.

Using $R_{mf}$ where $R_w$ belongs makes the computed saturation meaningless — and
in a fresh mud over a saline formation the two can differ by a factor of tens.
Invasion is *why* the two must be distinguished, and why the mud system is part of
the log header.

## 4. Worked examples

### 4.1 How long does invasion take to reach a metre?

From the measured front positions, extrapolating the cylindrical trend: the front
reaches 0.43 m at 1000 h and 0.53 m at 2778 h. A one-metre front would require
times beyond the range computed here, and the demonstration's log-log slope of
about 0.2 implies roughly a factor of $10^{1/0.2} = 10^{5}$ in time to double the
front, i.e. of order decades. **In a permeable, overbalanced well, invasion
therefore usually saturates at the decimetre-to-metre scale and then stops**,
which is good news: the deep reading becomes usable again if the hole is logged
after the near-wellbore zone has stabilised.

### 4.2 What the caliper tells you before any correction

A bit that drills a 0.216 m hole logging a caliper of 0.30 m in a shale and
0.22 m in a sandstone says: the shale is washed out (mechanical or chemical
erosion) and the sandstone is essentially in gauge. The density and neutron tools
read part of the hole fluid in the washed-out shale, so uncorrected density
porosity there is biased towards the mud's density; the hole-size correction is
largest exactly where the rock is weakest. This is why the caliper is the first
log examined and the last one quoted.

### 4.3 Salinity and temperature, in the fluid term

Both $R_w$ and the fluid density and hydrogen index depend on salinity and
temperature. A change of 20 °C in the water's temperature changes its resistivity
by roughly the ratio of the temperature-dependent mobilities; over a 2 km interval
that shift is comparable with the contrast the interpretation is trying to
resolve. The recipe: convert every fluid resistivity to a *stated reference
temperature*, quote the conversion used, and carry the salinity that goes with
it. Refer to
[09-01-05 Temperature, Pressure and Frequency Dependence](../../09-electrical-em-methods/01-electrical-properties-of-earth/05-temperature-and-pressure-effects.md)
for the quantitative form.

## 5. Assumptions

1. **The filtrate mixing is diffusion-like.** Real invasion is mudcake-controlled,
   partly advective, and anisotropic in layered rock.
2. **Radial symmetry.** Fractures, high-permeability streaks and dipping beds break
   it, producing a non-circular invaded zone that a radial model cannot represent.
3. **A single filtrate concentration at the wall.** Partial flushing leaves
   residual hydrocarbon, so $R_{xo}$ is not $R_{mf}$.
4. **The tool weighting functions in Section 3.3 are stated synthetics.** Real
   tool responses are not exponentials and are not transferable between tools.
5. **The corrections are known.** Each environmental correction is a chart or
   algorithm tied to a tool; using the wrong one is worse than using none, because
   it looks applied.
6. **The hole is stable at logging time.** Time-lapse caliper changes mean the
   formation is still moving, and every subsequent correction is invalid.

## 6. Units and dimensional analysis

- Equation (1): $D$ in m² s⁻¹, so $\sqrt{Dt}$ is m ✓. A filtrate diffusivity
  quoted in cm² s⁻¹ must be converted: 1 cm² s⁻¹ = 10⁻⁴ m² s⁻¹, a factor of
  $10^{4}$.
- Conductivity S m⁻¹ against resistivity Ω m: reciprocal, and the reciprocal of an
  *average* is not the average of reciprocals (Section 2 of the resistivity
  lesson).
- $w(r) \propto r e^{-(r-r_w)/L}$: the $r$ factor carries the cylindrical area
  element and is dimensionless relative to a unit radius, so $L$ alone sets the
  scale.
- Overbalance $\Delta p$ in Pa (or psi in the field): 1 psi = 6.895 kPa. Mixing
  units here produces mud weights that are wrong by 7 per cent, which is enough to
  matter for a fracture gradient.
- Depth: **measured depth** (along the hole) versus **true vertical depth**. In a
  deviated well they differ by $\cos(\text{inclination})$; a 30° deviation is a
  13 per cent difference, and the caliper, logs and core are all reported in
  measured depth unless stated otherwise.

## 7. Python demonstration

`code/borehole_env_demo.py` solves invasion, validates the solver on plane
geometry, computes the tool responses and runs the invasion correction.

```python
x, conc = diffuse(t_final, "cylinder")     # Crank-Nicolson, fixed wall value
sigma = SIG_XO * conc + SIG_T * (1.0 - conc)
r_sh = 1.0 / tool_response(x, sigma, 0.15)
r_dp = 1.0 / tool_response(x, sigma, 1.50)
```

Measured output, abridged:

```
planar front positions: 0.0976 m, 0.3128 m, 0.9883 m
  exponent over decade 1: 0.5058   (theory: 0.5)
  exponent over decade 2: 0.4997   (theory: 0.5)

t =     10 h  R_inv(50%) = 0.1701 m (R - r_w = 0.0701 m)
t =    100 h  R_inv(50%) = 0.2596 m (R - r_w = 0.1596 m)
t =   1000 h  R_inv(50%) = 0.4338 m (R - r_w = 0.3338 m)
  exponent over decade 1: 0.1835
  exponent over decade 2: 0.2229

time (h)   R_inv (m)   sigma_shallow   sigma_deep   ratio
     10     0.170        0.5297       0.0712     7.44
    100     0.260        0.9634       0.1352     7.13
   1000     0.434        1.2957       0.3573     3.63
   2778     0.526        1.3762       0.4633     2.97

true Rt = 2000 ohm m; shallow reading 2.13 ohm m; deep reading 22.65 ohm m
Sw from the deep reading, uncorrected =  3.759
step-model geometric factors: shallow 0.434, deep 0.019
Rt recovered from the SMOOTH profile =      40.35 ohm m (-98.0 per cent)
applied to a genuine step profile with the same Rxo, Rt and r_i:
Rt recovered =    1722.04 ohm m (-13.9 per cent), Sw = 0.431
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Plane-geometry exponent 0.5058 and 0.4997 | The solver is validated before its cylindrical result is believed |
| Cylindrical exponent 0.18–0.22, not 0.5 | Invasion has no universal $\sqrt{t}$ law in a borehole |
| Shallow/deep ratio 7.44 early, 2.97 late | The invasion signal is transient and must be logged while it exists |
| Uncorrected $S_w = 3.759$ | A saturation above 1 is a diagnosis, not a failure of arithmetic |
| Step profile recovered to 8 per cent, smooth profile to $-98$ per cent | An invasion correction is a model of geometry, not an exact inversion |

> **Breaking exercise.** Change `D_FIL` by a factor of ten and re-run. Predict
> which columns change and whether the *shape* of the ratio-versus-time curve
> changes. Explain your answer using the absence of self-similarity from §3.2.

## 8. Exercises

Full sets in
[`exercises/01-borehole-environment-exercises.md`](./exercises/01-borehole-environment-exercises.md)
with worked solutions in
[`exercises/01-borehole-environment-solutions.md`](./exercises/01-borehole-environment-solutions.md).

### ★ Foundational

**★1.** State the six environmental corrections and, for each, one observable
symptom of omitting it.

**★2.** Distinguish $R_w$ and $R_{mf}$: what each is a property of, where each is
measured, and which appears in Archie's law.

**★3.** Convert a filtrate diffusivity of 3 cm² s⁻¹ to SI and recompute
$\sqrt{4Dt}$ at $t = 100$ h.

### ★★ Applied

**★★4.** Run `code/borehole_env_demo.py` and report the front positions and
exponents for a diffusivity of $1\times10^{-6}$ m² s⁻¹.

**★★5.** Using the weighting function of equation (2) with $L = 0.15$ m, compute
numerically the radii containing 50 and 90 per cent of the signal, and compare
with the values quoted in §3.4.

**★★6.** For a formation with $R_t = 200$ Ω m, $R_{xo} = 2$ Ω m and an invasion
radius of 0.4 m, compute the apparent resistivity of the two synthetic tools of
§3.3 and the resulting uncorrected $S_w$ using $\phi = 0.3$, $a = 1$, $m = 2$,
$n = 2$, $R_w = 0.2$ Ω m.

### ★★★ Research-oriented

**★★★7.** Extend the solver to two-layer anisotropic invasion (a radial
permeability contrast at a bed boundary) and report how much the invasion front
departs from a circle. State the extra assumption your model needs and what
measurement would test it.

**★★★8.** The demonstration's correction fails on the smooth profile. Construct a
correction that works for *both* the step and the smooth profile by parameterising
the invasion profile with one additional shape parameter, and report the residual
error in $R_t$ for each. Then state what field measurement would constrain that
extra parameter.

## 9. Common mistakes

1. **Using the bit size as the hole size.** The caliper is the measurement.
2. **Confusing $R_w$ and $R_{mf}$.** They differ by a factor of tens in fresh mud
   over saline water, and the error goes straight into $S_w$.
3. **Quoting an invasion radius without the time since drilling** and without the
   mud properties.
4. **Applying a correction chart from a different tool vintage.** Identify the
   chart, version and service company.
5. **Believing a saturation above 1.** It means the reading is filtrate-dominated;
   recompute the interpretation, do not clip the number.
6. **Assuming the hole is in gauge.** A washed-out hole biases density and neutron
   porosity towards the mud, in exactly the weak rocks where porosity matters.
7. **Reporting measured depth as if it were true vertical depth.** In a deviated
   well they differ by $\cos(\text{inclination})$.

## 10. Real-world applications

- **Petrophysics.** Corrected logs are the input to every saturation and porosity
  calculation in a reservoir model.
- **Geomechanics.** Caliper breakouts and image logs give stress orientation, one
  of the few direct in-situ stress measurements available
  ([02-04-08 Failure, Friction and the Brittle Regime](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md)).
- **Hydrogeology.** Invasion disturbs the salinity profile, which is the quantity a
  borehole conductivity log is used to map
  ([14-03-01 Petrophysics for Hydrology](../../14-hydrology-hydrogeophysics/03-petrophysics-hydrology/README.md)).
- **Geothermal wells.** High-temperature wells require temperature-corrected tools
  and mud systems, and the invasion profile in a fractured reservoir is not radial.
- **Scientific drilling.** Where the borehole *is* the experiment, the disturbance
  must be characterised before any downhole measurement is interpreted
  ([05-09-01](../09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md)).

## 11. Further reading

- **Ellis, D. V. & Singer, J. M. (2007). *Well Logging for Earth Scientists*
  (2nd ed.). Springer.** Chapters 1–4. Level: intermediate to advanced. The
  standard treatment of the borehole environment, invasion and environmental
  corrections.
- **Hearst, J. R., Nelson, P. H. & Paillet, F. L. (2000). *Well Logging for
  Physical Properties*. Wiley.** Chapters 1–3. Level: advanced. Borehole
  environment and tool physics, with the weighting-function formalism of §3.3.
- **Serra, O. (1984). *Fundamentals of Well-Log Interpretation*, Vol. 1.
  Elsevier.** Level: intermediate. The classical reference for corrections and
  their charts.
- **Carslaw, H. S. & Jaeger, J. C. (1959). *Conduction of Heat in Solids*
  (2nd ed.). Oxford University Press.** Chapter 7. Level: advanced. The
  cylindrical diffusion solutions, applicable to filtrate invasion by analogy and
  the source of the non-self-similar behaviour of §3.2.
- **Tiab, D. & Donaldson, E. C. (2015). *Petrophysics* (4th ed.). Gulf
  Professional Publishing.** Level: intermediate. Invasion, mudcake and spurt
  loss from the reservoir-engineering side.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-08-02 Natural Gamma and Spectral Gamma Logging](./02-gamma-logging.md)
  — the first log run, and its own volume of investigation.
- [05-08-03 Resistivity, Induction and Laterolog Tools](./03-resistivity-logging.md)
  — the tool physics behind the shallow/deep pair used in §3.5.
- [05-08-07 Log Interpretation, Petrophysics and Uncertainty](./07-log-interpretation.md)
  — the full workflow, including depth matching and the datum problem.
- [05-09-01 Measuring Terrestrial Heat Flow](../09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md)
  — the temperature disturbance of item 3 in §1.
- [23-05-01 Sensors and Transducers](../../23-field-methods-instruments/05-instrumentation-and-electronics/01-sensors-and-transducers.md)
  — how the downhole sensor actually works.

## Self-assessment checklist

- [ ] I can list the four ways drilling perturbs the formation. (§1)
- [ ] I can distinguish flushed, transition and virgin zones and name their
      resistivities. (§2.2)
- [ ] I can solve radial diffusion and explain why the borehole front is not
      $\sqrt{t}$. (§3.1–3.2)
- [ ] I can compute a tool's apparent reading from a weighting function and an
      invasion profile. (§3.3)
- [ ] I can define a depth of investigation and say what it depends on. (§2.3,
      §3.4)
- [ ] I can name the six environmental corrections, what each corrects and what
      happens if it is omitted. (§2.4)
- [ ] I can explain why uncorrected $S_w$ can exceed 1 and what that means. (§3.5)
- [ ] I can distinguish $R_w$ from $R_{mf}$ and say where each comes from. (§3.6)
- [ ] I can state the honest limits of a borehole measurement. (§1, §5)
