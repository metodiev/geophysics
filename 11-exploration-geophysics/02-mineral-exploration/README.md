# Module 11-02 — Mineral Exploration Geophysics

**Stages:** advanced → research · **Prerequisites:** modules 04-06 and 11-01;
the method modules 07-03, 08-03, 08-05 and 09-03.

This module is about turning geophysical measurements into statements about ore
bodies, and its central honest difficulty is that **no geophysical method detects
ore.** Each one detects a physical-property contrast, and every property that makes
an ore body anomalous is shared with barren rock: graphite conducts as well as
massive sulphide, banded iron formation is as dense and as magnetic as many IOCG
systems, and a clay-rich saprolite polarises as strongly as a disseminated sulphide
body. The lessons therefore do not stop at "the method sees the target". Each one
quantifies what the measurement actually constrains — a *product*, a *ratio* or a
*direction* — and then names the additional measurement, if any, that breaks the
resulting ambiguity.

That structure repeats, and it is worth stating once. Magnetics constrains the
**direction** of the total magnetisation only through the shape of the anomaly,
which is also where the depth comes from, so the two are entangled and reduction to
the pole requires the very direction it is used to estimate. Gravity constrains the
excess mass as a product $\Delta\rho V$, and the depth only through a shape
assumption that one profile cannot test. EM constrains the **conductance**
$\sigma t$ exactly, so conductivity and thickness are inseparable by any inductive
measurement, and the decay time gives $\sigma a^{2}$, another product. Radiometrics
constrains the **surface** K/U/Th ratios and nothing below the top half-metre.
Induced polarisation constrains polarisability, which responds to a few per cent of
sulphide but *fails* on massive sulphide because a connected conductor shunts the
current around the polarisable interfaces. In every case the mapping from the
measurement to a geological statement passes through an assumption that the data
cannot check, and the lessons measure the error that assumption introduces rather
than mentioning it as a caveat.

The last lesson turns the same scepticism on the way these layers are combined. A
prospectivity map that sums the evidence of several layers assumes those layers are
conditionally independent given the ore, and in the demonstration's controlled
experiment the violation of that assumption costs almost nothing in the usual
summary statistic and a factor of eleven in the number of deposits found at a
realistic drilling budget. That is the module's closing argument: aggregate scores
can be healthy while the decision they support is wrong, and only a
decision-relevant metric reveals it.

All models and data in this module are **SYNTHETIC**. Property contrasts, deposit
class tables, magnetisation directions, density contrasts, resistivities,
conductances, radioelement concentrations, Cole-Cole parameters and prospectivity
layers are chosen teaching values or generated fields. No number anywhere in these
lessons is a measurement of, or an average over, any real deposit, district,
company or dataset; a few standard physical constants (the gravitational constant,
the permeability of free space, the density of air and two mass attenuation
coefficients) and standard model results are used explicitly and identified where
they appear.

## Learning objectives

By the end of this module you will be able to:

1. **Construct** a signature vector for a deposit class from property contrasts, and
   **compute** the anomaly of a common body for gravity, magnetics, EM and
   radiometrics.
2. **Determine** which deposit classes a method can and cannot separate, and
   **state** the role of the amplitude-versus-direction distinction.
3. **Derive** the depth rules of magnetic and gravity anomalies, **quantify** the
   depth error introduced by a wrong shape or magnetisation direction, and
   **compute** self-demagnetisation where it invalidates the linear relation.
4. **Derive** the conductance degeneracy of thin conductors and the sphere time
   constant, **verify** the latter numerically, and **explain** which additional
   measurement breaks each ambiguity.
5. **Derive** the height response of an infinite plane gamma source, **compute** the
   stripping inverse and its error amplification, and **quantify** the burial limit
   and the counting-statistics detection limit.
6. **Set up** the Cole-Cole model, **derive and verify** the phase-area identity,
   **compute** the chargeability of a blocked-path mixture, and **measure** the
   (m, τ, c) ranges consistent with a spectrum of a stated bandwidth.
7. **Build** a prospectivity map, **measure** its capture curve against a known
   truth, and **diagnose** the conditional-independence failure and the chance AUC
   of an irrelevant layer.

## Prerequisites

- [11-01-02 Targeting Strategy and Method Selection](../01-exploration-workflow/02-targeting-and-strategy.md)
  — the anomaly formulas, detection probability and method-ranking framework these
  lessons apply.
- [11-01-03 Cost, Risk and Value of Information in Exploration](../01-exploration-workflow/03-cost-benefit.md)
  — what a ranking or a detection is worth.
- [07-03 Gravity Anomalies and Modelling](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/README.md),
  [08-03 Magnetic Anomalies and Modelling](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/README.md)
  and [08-05 Controlled-Source EM](../../08-geomagnetism-electromagnetism/05-controlled-source-em/README.md)
  — the general theory behind lessons 02–04.
- [09-03 Induced Polarisation](../../09-electrical-em-methods/03-induced-polarisation/README.md)
  — the measurement and models behind lesson 06.
- [04-06-02 Mineral Deposit Types and Their Geophysical Signatures](../../04-earth-science-geology/06-petroleum-and-mineral-systems/02-mineral-deposits.md)
  — the geology being targeted.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Geophysical Signatures of Major Deposit Types](01-deposit-signatures.md) | advanced | A signature is a direction, not a magnitude; with the amplitude unknown, only the pattern identifies the class |
| 02 | [Magnetics for IOCG, Porphyry and Magmatic Sulphides](02-magnetics-for-minerals.md) | graduate | The anomaly shape is set by the total magnetisation direction, which RTP and every depth rule need as an input |
| 03 | [Gravity for Chromite, Massive Sulphide and Iron Ore](03-gravity-for-minerals.md) | graduate | One exact depth rule (cylinder), one calibrated (sphere), and a shape-free excess-mass invariant for 2-D bodies only |
| 04 | [EM for Conductors, Massive Sulphides and Graphite](04-em-for-minerals.md) | graduate | EM measures conductance, not conductivity; the degeneracy is exact and graphite is a perfect sulphide mimic |
| 05 | [Radiometrics and Alteration Mapping](05-radiometrics-for-minerals.md) | graduate | Ratios remove the gain and the source strength but import a height bias; the method sees the top half-metre |
| 06 | [IP for Disseminated Sulphides and Porphyry Systems](06-ip-for-minerals.md) | graduate | Disseminated sulphide polarises strongly and massive sulphide weakly; every chargeability is window-dependent |
| 07 | [Multi-Method Targeting and Prospectivity Analysis](07-multi-method-targeting.md) | research | Summing log odds assumes conditional independence, and violating it costs a factor of eleven in capture |

## Suggested path

**If you are new to minerals geophysics:** lessons 01 and 02, then 03. From lesson
01, keep the signature table open — the later lessons each take one column of it
and show what it costs to interpret.

**If you are a geophysicist learning the exploration context:** 01 §4–§6 (what
identifies a class and what does not), then 04 and 06 together, because the
disseminated-versus-massive contrast is the module's most useful practical result.

**If you are preparing a research project:** 03 §5–§6 (regional removal and the
excess-mass invariant), 06 §2–§3 (the phase-area identity and the bandwidth
dependence of parameter resolution), and 07 in full, plus the ★★★ exercises, which
ask for specifications and for numerical experiments.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-deposit-signatures.md`](01-deposit-signatures.md) | Lesson 01 |
| [`02-magnetics-for-minerals.md`](02-magnetics-for-minerals.md) | Lesson 02 |
| [`03-gravity-for-minerals.md`](03-gravity-for-minerals.md) | Lesson 03 |
| [`04-em-for-minerals.md`](04-em-for-minerals.md) | Lesson 04 |
| [`05-radiometrics-for-minerals.md`](05-radiometrics-for-minerals.md) | Lesson 05 |
| [`06-ip-for-minerals.md`](06-ip-for-minerals.md) | Lesson 06 |
| [`07-multi-method-targeting.md`](07-multi-method-targeting.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 11-exploration-geophysics/02-mineral-exploration/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python deposit_signatures_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetics_for_minerals_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_for_minerals_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_for_minerals_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python radiometrics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_for_minerals_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multi_method_targeting_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access, runs in a few seconds
and exits 0. Several of them verify their results numerically against an
independent route: the gravity voxel sum against the closed form, the magnetic
dipole against a voxel sum, the sphere decay constant against a finite-difference
solution of the radial diffusion equation, the plane-source height response against
a direct annular integral, and the WofE posterior against its own contingency table.

## Mastery checkpoint

Complete this without notes:

> A SYNTHETIC target is a sphere of radius $120\ \mathrm{m}$ at $z = 250\
> \mathrm{m}$ with $\Delta\rho = 600\ \mathrm{kg\,m^{-3}}$,
> $\kappa = 0.05$ SI, resistivity $1\ \Omega\,\mathrm{m}$ in a host of
> $200\ \Omega\,\mathrm{m}$, $B_0 = 50\ \mathrm{\mu T}$ and $m = 0.15$ with
> $\tau = 0.5\ \mathrm{s}$. **(a)** Compute its gravity and magnetic anomalies and
> the EM index at $100\ \mathrm{Hz}$. **(b)** State, for each of the three methods,
> the one quantity the anomaly constrains and the one assumption you must add to
> turn it into a statement about the body. **(c)** A barren graphite body at the
> same depth produces the same EM index: compute the conductance the EM anomaly
> actually measures, and name the two measurements that would separate the two
> bodies. **(d)** Compute the chargeability the IP survey would report in a
> $200$–$800\ \mathrm{ms}$ window, and state why the same body could report twice
> that in another survey. **(e)** State which of the three anomalies you would
> trust most as a *drilling* justification, and why.

Worked versions of the individual steps appear in the lesson solutions.

## Common pitfalls across this module

1. **Reading a signature amplitude as an identification.** With size and depth
   unknown, only the *direction* of the signature identifies a class, and a class
   pair with cosine 0.999 cannot be separated at any budget.
2. **Reporting an RTP map or a depth without the assumed magnetisation direction.**
   Ignoring a $Q = 1.5$ remanence biased the demonstration's depth by $9.6\%$, and a
   badly wrong direction made the shape rule inapplicable.
3. **Using $\Delta B \propto \kappa$ for a magnetic body.** Self-demagnetisation
   made the linear formula over-predict by a factor of $2$ at $\kappa = 3$ SI.
4. **Quoting a conductivity from an EM anomaly.** The observable is conductance;
   $\sigma$ and $t$ are exactly degenerate.
5. **Expecting massive sulphide to be an IP target.** A connected conductor shunts
   the current and collapses the measured chargeability by a factor of $21$ in the
   demonstration's mixture model.
6. **Quoting a chargeability without its window and delay.** A factor of five for a
   typical rock and $570$ for a fast-relaxing one.
7. **Forming radioelement ratios before height correction.** A $30\%$ apparent Th/K
   change can be pure terrain.
8. **Summing prospectivity layers without an independence check.** The measured
   cost was $0.03$ of AUC and a factor of eleven in capture at a 10-site budget.
9. **Reporting an AUC with no simulated null.** An irrelevant smooth layer reached
   AUC $0.6553$ in the demonstration's null experiment.

## Related modules

- [11-01 The Exploration Workflow](../01-exploration-workflow/README.md) — the
  decision framework inside which these measurements are bought.
- [11-03 Hydrocarbon Exploration Geophysics](../03-hydrocarbon-exploration/README.md)
  — the same reflection-seismic toolbox for a different target class.
- [11-07 Exploration Case Studies](../07-exploration-case-studies/README.md) —
  where these signatures and ambiguities are worked through end to end.
- [05-07 Interpretation and Integration](../../05-core-geophysics/07-interpretation-and-integration/README.md)
  — reporting results with uncertainty, which every number in this module must obey.
