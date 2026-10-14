# 11 — Exploration Geophysics

**Stages:** intermediate → research

Exploration geophysics is the part of the subject in which a measurement has to
answer an economic question. That sentence does more work than it looks like it
does. It means the survey cannot be evaluated by whether it produced good data,
or even by whether it found something; it is evaluated by whether it changed a
decision for the better — whether it moved a drill rig, stopped a bad hole, or
priced a risk that was until then a guess. The organising principle of this
folder is therefore **decision-making under uncertainty**, and every module in it
is written so that the decision, not the section, is the unit of interpretation.

The central honest difficulty follows from that principle and is worth stating
once, plainly: **an anomaly is not an orebody, an aquifer, a reservoir or a
water-bearing fault.** Geophysics measures a *contrast in a physical property* —
conductivity, density, elastic modulus, magnetisation — and every target of
economic interest is a *state* (mineralised, saturated, permeable, hot,
contaminated) that only correlates with that property. The correlation is real
but never unique, so an interpretation must carry its **false-positive rate**:
the fraction of anomalies of that type that turn out to be nothing. A report that
gives the anomaly and withholds the false-positive rate has not answered the
question it was commissioned to answer.

A third theme runs through the folder because it is forced by the first two: **the
right survey is chosen, not found.** Depth of investigation, resolution,
sensitivity to the target's property contrast, footprint, cost and the base rate
of the region all enter the design, and they trade against one another. A cheap
regional screen followed by an expensive confirmation is usually better than
either alone, and the arithmetic that shows this — expected value, value of
information, cost per discovery — is as much part of the subject as the forward
model. Modules 01 and 07 develop that arithmetic explicitly; the target modules
apply it.

Three distinctions recur often enough to state once:

- **Detection versus resolution versus identification.** A thin layer, a small
  object or a weak anomaly can be detected long after it is unresolvable, and a
  response can be modelled long after it is identifiable. Reporting one as
  another is the commonest overclaim in exploration, and several lessons measure
  the difference with numbers.
- **Measurement, model and choice.** The reference field, the inversion
  regularisation, the wavelet, the depth-weighting kernel, the recovery factor
  and the base rate are models or choices; none is measured, and each changes the
  answer. Lessons here quote them instead of hiding them.
- **Resource versus reserve, success versus profit.** A quantity in the ground is
  not a quantity that pays; the conversion requires a flow rate, a cost and a
  price, and the conversion is where most disappointment lives.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Describe** the exploration lifecycle from reconnaissance to reserve
   definition, and **state** what decision each stage exists to inform.
2. **Select** a method suite for a stated target and budget, and **justify** each
   choice with a resolution, detection or contrast number.
3. **Compute** the expected value and the value of information of a survey, and
   **state** when a survey destroys value.
4. **Quantify** the physical signature of each major target class (mineral,
   hydrocarbon, geothermal, groundwater, geotechnical) in the property that the
   method measures.
5. **Compute** a positive predictive value from a base rate and indicator
   performance, and **interpret** it as a targets-per-discovery count.
6. **Demonstrate** the bias from assuming correlated indicators or correlated play
   elements are independent, and **state** how to model the dependence instead.
7. **Interpret** an anomaly quantitatively, **report** the admitted range of
   bodies or models that explain it, and **state** the assumptions each range
   carries.
8. **Design** a staged survey and **compare** strategies by net value rather than
   by the number of targets found.
9. **Convert** a resource estimate into a reserve statement using a flow-rate or
   recovery distribution, and **state** which parameters dominate the range.
10. **Compute** a false-positive or false-negative rate for a stated decision rule
    and **report** it with the interpretation.
11. **Distinguish** measurement, model and choice in any exploration product, and
    **write** an interpretation in which each number is labelled.
12. **Critique** a published or commercial exploration claim, isolating its base
    rate, its independence assumptions and its non-uniqueness.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [The Exploration Workflow](./01-exploration-workflow/README.md) | The lifecycle from reconnaissance to reserve definition; targeting logic; cost, risk and the value of information | The decision framework every later module applies; read it before any target module |
| 02 | [Mineral Exploration Geophysics](./02-mineral-exploration/README.md) | Deposit signatures; magnetics, gravity, EM, radiometrics and IP for IOCG, porphyry, massive sulphide and iron ore; multi-method targeting | The classic hard-rock exploration suite, and the archetype for anomaly-versus-orebody |
| 03 | [Hydrocarbon Exploration Geophysics](./03-hydrocarbon-exploration/README.md) | Reflection seismic from 2-D to 3-D, seismic stratigraphy, reservoir characterisation, inversion, unconventional reservoirs, borehole integration | The largest applied market, and the source of most processing and inversion practice |
| 04 | [Geothermal Exploration Geophysics](./04-geothermal-exploration-geophysics/README.md) | Signatures of geothermal reservoirs, magnetotellurics for resource assessment, microseismic monitoring | Where resistivity maps a cap rather than a fluid, and where monitoring becomes regulation |
| 05 | [Groundwater Exploration Geophysics](./05-groundwater-exploration/README.md) | Aquifer and saline-interface signatures, EM and ERT, refraction and surface waves, airborne EM | The applied hydrogeophysics suite, and the sharpest example of a conductivity that is not water |
| 06 | [Geotechnical and Engineering Geophysics](./06-geotechnical-and-engineering/README.md) | Site investigation and method selection, tunnels, dams and foundations, UXO and clearance, landfill and brownfield assessment | The branch where a false negative is a failure, not a missed opportunity |
| 07 | [Exploration Case Studies](./07-exploration-case-studies/README.md) | Porphyry district, basin and play assessment, geothermal field development, arid-region groundwater — written as argument archetypes | The folder's integration: probability, value and uncertainty accounting in four complete decisions |

## The dependency spine

```text
11-01 Exploration workflow ──┬──> 11-02 Mineral ──┬──> 11-07 Case studies
   (lifecycle, targeting,    │                    │        ^
    cost, value of info)     ├──> 11-03 Hydrocarbon ───────┤
        │                    │                            │
        │                    ├──> 11-04 Geothermal ───────┤
        │                    │                            │
        │                    ├──> 11-05 Groundwater ──────┤
        │                    │                            │
        │                    └──> 11-06 Geotechnical ─────┘
        │
        └──> (assumes 05-core-geophysics, 07-gravity-geodesy, 08-geomagnetism,
              09-electrical-em-methods, 10-gpr-near-surface, 06-seismology,
              18-inverse-problems, 21-statistics-bayesian-ml)
```

Four rules of thumb follow:

1. **The question before the method.** No module here starts with an instrument.
   Every one starts from what has to be decided, and this is why the workflow
   module is first.
2. **A property contrast before a target.** The target modules (02-06) all rest
   on a rock-physics relation between the property measured and the state sought;
   if that relation is ambiguous, so is every interpretation built on it.
3. **Resolution and detection are acquisition properties.** They depend on
   spacing, frequency, gate time, altitude, array geometry and the stated noise
   level — not on the ground alone. Any depth or thickness quoted without them is
   not a measurement of the Earth.
4. **A probability before a decision.** Modules 02-06 end in a target; module 07
   turns targets into decisions, and that is where the base rate, the false
   positive rate and the value of information appear. Read 11-01-03 and module 07
   together, whichever target module you came through.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand what an exploration survey is for | 01 |
| Work on mineral targets or prospectivity | 01, 02, 07 |
| Work on hydrocarbon exploration or reservoir characterisation | 01, 03, 07 |
| Work on geothermal exploration or monitoring | 01, 04, 07 |
| Work on groundwater or water-resource assessment | 01, 05, 07 |
| Work on civil, environmental or UXO projects | 01, 06 |
| Understand anomaly interpretation and risk | 01, 07 (then the relevant target module) |
| Prepare an exploration programme from scratch | 01, then 07, then the target module(s) |
| Critique an exploration claim or a promotion document | 01, 07 |

## Suggested paths

**If you are new to exploration:** read
[11-01-01](./01-exploration-workflow/01-exploration-lifecycle.md) for the
lifecycle, then [11-01-03](./01-exploration-workflow/03-cost-benefit.md) for the
decision arithmetic, and then pick one target module. Do not read all five target
modules before reading the decision material; the target modules assume it and
will otherwise read as catalogues of methods.

**If you come from the physics-side folders:** read
[11-01-02](./01-exploration-workflow/02-targeting-and-strategy.md) for the
targeting logic, then the target module closest to your interest, then
[11-07-01](./07-exploration-case-studies/01-case-study-porphyry.md) and
[11-07-02](./07-exploration-case-studies/02-case-study-basin.md) for how a
complete argument is assembled. The unfamiliar content will be economic and
statistical, not physical.

**If you already practise near-surface geophysics:** read 11-06, then
[11-05-04](./05-groundwater-exploration/04-airborne-groundwater.md) for the
regional scale-up, then [11-07-04](./07-exploration-case-studies/04-case-study-groundwater.md)
for the decision framing. The unfamiliar content will be the base rate and the
value-of-information arithmetic.

**If you are preparing a research project:** read the "assumptions and regime of
validity" section of every lesson in your target module, plus
[11-07-03 §3](./07-exploration-case-studies/03-case-study-geothermal.md) (resource
versus reserve) and [11-07-01 §3.2](./07-exploration-case-studies/01-case-study-porphyry.md)
(correlated indicators). Each is a worked example of stating what a data set does
*not* determine.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **For a target of your choice, a defensible exploration recommendation from a
> synthetic data set.** Generate your own synthetic data using the forward models
> of the relevant target module. Then: **(a)** state the economic question and the
> threshold that defines success; **(b)** design a method suite and justify each
> method with a resolution or detection number computed from a forward model;
> **(c)** produce the interpretation with an explicit admitted range of models and
> the assumptions each carries; **(d)** estimate the base rate for the setting and
> compute the posterior probability that a target selected by your criterion is
> economic; **(e)** compute the expected value of the first hole and the value of
> information of the *next* survey, naming the decision it would change; and
> **(f)** for each number in (a)-(e), label it as **measured**, **modelled** or
> **chosen**, and name the single additional observation that would most reduce
> the largest remaining uncertainty.

The point of the checkpoint is the accounting, not the digits: a defensible
exploration product is one in which every number carries its label and every
probability carries its base rate. A worked example of the groundwater and
porphyry versions appears in the module 07 exercises; the structure is the same
for any target.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $\rho_a$, $\sigma_a$ | Apparent resistivity, apparent conductivity | $\Omega\,\mathrm{m}$, $\mathrm{S\,m^{-1}}$ |
| $\sigma$, $\rho$ | Conductivity, resistivity | $\mathrm{S\,m^{-1}}$, $\Omega\,\mathrm{m}$ |
| $S = \sigma h$ | Conductance of a layer | S |
| $v_p, v_s$ | Compressional and shear wave speed | m/s |
| $\delta$ | Skin (diffusion) depth, $503.29\sqrt{\rho/f}$ | m |
| $d(t)$ | Time-domain diffusion depth, $1261.6\sqrt{\rho t}$ | m |
| $\gamma$, $\Delta g$ | Gravity (total, anomaly) | mGal ($10^{-5}$ m/s²) |
| $\mu\mathrm{Gal}$ | Microgravity unit | $10^{-8}$ m/s² |
| $\mathbf{m}$, $M$ | Magnetic moment; magnetisation | $\mathrm{A\,m^{2}}$; A/m |
| $B$ | Magnetic flux density | nT ($10^{-9}$ T) |
| $G_{\max}$ | Small-strain shear modulus, $\rho v_s^{2}$ | Pa |
| $v_{s30}$ | Travel-time average $v_s$ to 30 m | m/s |
| $q$ | Footing pressure | kPa |
| $T$ | Temperature | °C or K |
| $\mathrm{Pe}$ | Péclet number | dimensionless |
| $p$ | Base rate (prior probability) | dimensionless |
| $\mathrm{TPR}, \mathrm{FPR}$ | True- and false-positive rates | dimensionless |
| $\mathrm{PPV}$ | Positive predictive value | dimensionless |
| $\mathrm{CoS}$ | Chance of success | dimensionless |
| $\mathrm{EMV}$ | Expected monetary value | currency |
| $\mathrm{VOI}$ | Value of information | currency |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the rounded physical constants used as anchors are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Conductivities, resistivities, velocities, densities, depths, recoveries,
basement structures, water salinities, indicator performances, base rates, costs
and success ratios **vary** — between regions, between models, between markets
and between analysts of the same data. Where this folder gives a number it gives
a *teaching value* with its units and its provenance (a synthetic model run by a
demonstration, or a named standard constant such as
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ or
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$). No number in this folder is
presented with the authority of a measurement of the Earth, a real deposit, a
real field or a real programme.

The case-studies module goes further and quotes **no site-specific number at
all**: real places are named, if at all, only as argument archetypes, with an
explicit statement that no factual claim and no site-specific figure is made
about them. Every demonstration is reproducible from the code in its module's
`code/` directory, is print-only, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.
**Unless a lesson explicitly says otherwise, all models and data in this folder
are SYNTHETIC.**

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 11-exploration-geophysics/05-groundwater-exploration/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python aquifer_signatures_demo.py
```

The demonstrations fall into four kinds, and it is worth knowing which you are
reading. Some **derive and verify a forward relation** against a limit or a
second route (the two-layer sounding series against its asymptotes, the diffusion
kernel against its normalisation, the Gassmann speeds against the density
change). Some **measure a trade-off** (water level against resolution, spacing
range against admitted depth, altitude against penetration, aperture against
velocity). Some **measure a non-uniqueness** (conductance equivalence, the
shape ambiguity in a magnetic depth, correlated indicators). And some **measure a
decision** (expected value, value of information, false-positive and clearance
rates). If a demonstration reports a number, that number is either printed by the
code you are running or is a stated standard constant.

The repository-wide quality gate, which checks structure, frontmatter, links and
LaTeX, is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

Exploration geophysics sits between the measurement foundations and the
application domains. It assumes the property contrasts of
[05-core-geophysics](../05-core-geophysics/README.md), the potential fields of
[07-gravity-geodesy](../07-gravity-geodesy/README.md), the magnetic and
inductive methods of
[08-geomagnetism-electromagnetism](../08-geomagnetism-electromagnetism/README.md),
the electrical methods of
[09-electrical-em-methods](../09-electrical-em-methods/README.md), the
near-surface and GPR methods of
[10-gpr-near-surface](../10-gpr-near-surface/README.md) and the seismic methods of
[06-seismology](../06-seismology/README.md). It depends on
[18-inverse-problems](../18-inverse-problems/README.md) for the inversion and
uncertainty theory it uses,
[21-statistics-bayesian-ml](../21-statistics-bayesian-ml/README.md) for the
probability it applies, and
[23-field-methods-instruments](../23-field-methods-instruments/README.md) for
the acquisition practice behind its surveys. It supplies
[14-hydrology-hydrogeophysics](../14-hydrology-hydrogeophysics/README.md) with
the hydrogeophysical method suite and the water-resource decision framing,
[04-earth-science-geology](../04-earth-science-geology/README.md) with the
geophysical expression of its resource systems, and
[25-projects-capstone](../25-projects-capstone/README.md) with the template for a
complete, decision-driven exploration study.
