---
id: 07-02-04
title: "Practical Correction Workflow and Processing Sequence"
level: advanced
prereqs: ["07-02-03", "07-01-04", "05-06-01"]
tags: [gravity, surveys, processing, corrections, workflow, verification, quality-control]
---

# Practical Correction Workflow and Processing Sequence

**All models and data in this module are SYNTHETIC.** The terrain, buried body,
readings, drift and noise are chosen teaching values. No survey, dataset,
instrument or published result is reproduced. The exact quantities used are
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$, the four WGS84
defining constants used to build normal gravity, $1\ \mathrm{mGal} = 10^{-5}\
\mathrm{m\,s^{-2}}$ and $1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the processing sequence from a raw reading to a delivered anomaly as a
   chain of named steps, and **state** what each step removes and what it needs as
   input.
2. **Explain** why the order of the steps is constrained, and **test** the
   commutation of two steps numerically.
3. **Build** a terrain model from prisms, and **verify** the prism code against an
   independent computation before trusting it.
4. **Verify** a whole pipeline against a known synthetic truth, and **distinguish**
   the pipeline residual from the reading noise.
5. **Run** three failure diagnostics — skipped terrain, wrong density, wrong
   free-air coefficient — and **identify** each from the spatial pattern of the
   residual.
6. **Quantify** the discretisation error of a terrain model by comparing two cell
   sizes, rather than assuming it is negligible.
7. **Assemble** an error budget for a reduced anomaly, **rank** the terms, and
   **state** which are controllable by better modelling and which are conventions.

## Prerequisites

- [07-02-03 Survey Procedures: Loops, Drift, Repeatability and Ties](03-survey-procedures.md)
  — the loop, drift and tie steps that precede the corrections here.
- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../01-gravity-fundamentals/04-gravity-reduction.md)
  — the derivations of the free-air, slab and terrain terms used here.
- [05-06-01 The Processing Pipeline Concept](../../05-core-geophysics/06-data-processing-principles/01-processing-pipeline-concept.md)
  — the general architecture of a processing sequence.

## 1. The sequence, as a chain of named steps

| # | step | removes | inputs | diagnostic |
|---|---|---|---|---|
| 1 | drift correction | instrument zero and drift | loop readings, base occupations | drift-model residuals, closure |
| 2 | tie to absolute | the arbitrary level | an absolute value with uncertainty | tie check, correlated shift |
| 3 | coordinates and heights | — (assignment) | GNSS/levelling, datum definition | positional sensitivity |
| 4 | normal gravity | latitude and reference-ellipsoid effect | adopted ellipsoid and formula | the $-1.138\ \mathrm{mGal}$ latitude spread of this SYNTHETIC survey |
| 5 | free air | station height above the ellipsoid | $\mathrm{d}\gamma/\mathrm{d}h$ at the station's latitude | slope of anomaly vs elevation |
| 6 | Bouguer slab | the rock between station and datum | an **assumed density** | correlation of the anomaly with relief |
| 7 | terrain | the actual topography's deviation from the slab | a digital elevation model and a density | convergence with the model's extent and cell size |
| 8 | (optional) isostasy | the deep compensation | a compensation model | the residual's correlation with topography |

Three of the eight steps (6, 7, 8) inject a **model**, and two of them (1, 4) inject
a convention. The chain is therefore not a sequence of measurements but a sequence of
differences between a measurement and a model, and the delivered anomaly is exactly
as trustworthy as the model chain — a fact quantified in Section 7.

## 2. Order matters, and here is where

The chain has only one strict ordering constraint that is easy to violate: **the
free-air and Bouguer terms both use the station's height, and the terrain term uses
the height *difference* between the station and the surrounding topography.** So
heights must be consistent (same datum, same units) before steps 5–7, and the
terrain model must be in the same vertical datum as the station heights. Mixing an
orthometric station height with an ellipsoidal DEM is a systematic error that looks
like a smooth anomaly (module [04](../04-geodesy-reference-frames/README.md)).

The steps that *do* commute are worth identifying, because their commutativity is a
useful test of an implementation. The slab and terrain terms combine into the
attraction of the actual topography, so

$$\text{slab} - \text{terrain} = A_{\text{topography}},$$

independently of the intermediate bookkeeping. The demonstration checks this on
every station and finds $\max\left|\text{slab} - \text{terrain} -
A_{\text{topography}}\right| = 0.000000\ \mathrm{mGal}$ — an exact identity in the
implementation, and therefore a test that catches sign and bookkeeping errors. This
is the strongest form of check available in a pipeline: an identity that must hold
exactly, rather than a comparison with a tolerance.

**A sign convention that must be stated.** The terrain term in this demonstration is
defined as $\text{slab} - A_{\text{topography}}$, so it is positive on a hilltop and
*negative* where the station sits below the surrounding terrain (measured here:
$-0.084$ to $+0.994\ \mathrm{mGal}$). The conventional Hammer compartment correction
is quoted as always positive, because it compares the real terrain with a plate over
the same finite compartments rather than with an infinite plate. The two conventions
differ only in the bookkeeping of the plate's extent, and the delivered anomaly is
the same; but a terrain-correction number quoted without its convention is
ambiguous, and the only unambiguous statement is the identity above.

## 3. Building and verifying a terrain model

Terrain corrections need the attraction of topography at each station, which is a
volume integral over a digital elevation model. The standard numerical device is the
**rectangular prism**, for which the vertical attraction has a closed form:

$$g_{z} = G\rho\left|\left[x\ln\left(y+r\right) + y\ln\left(x+r\right)
- z\arctan\frac{xy}{zr}\right]\right|_{\text{eight corners by signs}},
\qquad r = \sqrt{x^{2}+y^{2}+z^{2}},$$

with $x$, $y$, $z$ measured from the observation point to each corner and $z$
positive downwards (the standard convention for this formula). Two details decide
whether an implementation is correct:

- The limiting cases $x = 0$, $y = 0$ or $z = 0$ must be handled explicitly, because
  $0\times\ln 0$ and $\arctan\left(xy/0\right)$ are the limits that carry the
  formula. Handling them with `arctan2` and branch-explicit products is what makes a
  surface observation well defined.
- The formula must be **verified independently**. The demonstration does two checks:

| check | result |
|---|---|
| one prism $200\times200\times50\ \mathrm{m}$, observation at $100\ \mathrm{m}$ offset: closed form vs brute-force point-mass sum over 64 000 cells | $0.047871$ vs $0.047863\ \mathrm{mGal}$, difference $+0.016\%$ |
| whole hill at its centre: prism summation with 100 m cells vs a Monte-Carlo volume integral with $1.5\times10^{6}$ points | $7.856716$ vs $7.741085 \pm 0.200952\ \mathrm{mGal}$, i.e. $+0.58$ Monte-Carlo sigma |

Both checks pass at the level their discretisation predicts, which is the point: a
terrain code is not trustworthy because it looks standard, but because it agrees with
an independent computation whose error is known.

**Cell size is a real error.** Recomputing the same hill with 200 m cells instead of
100 m changes the attraction at a station by up to $156.16\ \mathrm{\mu Gal}$
($0.156\ \mathrm{mGal}$). That is the discretisation systematic of the model, it is
larger than the survey's own reading noise, and it is *reportable*: choose the cell
size, compare two sizes, and quote the difference.

## 4. The SYNTHETIC survey used here

| property | value |
|---|---|
| stations | 30 on a $6\times5$ grid, 280 m spacing |
| station heights | 261.3 to 326.9 m above the datum (relief up to 76.9 m) |
| latitude spread | 45.0027 to 45.0153 deg |
| free-air coefficient | 0.308555 mGal/m |
| normal gravity | 980620.0209 to 980621.1592 mGal (spread 1.138 mGal) |
| reading noise | 2.0 µGal |
| drift | 15.0 µGal/h, single loop with base bracketing |
| buried body | sphere, radius 250 m, depth 400 m, $\Delta\rho = 250\ \mathrm{kg\,m^{-3}}$ |
| terrain | Gaussian hill, 80 m high, 500 m $\sigma$ |

Corrections, in order of size: normal gravity
$\approx 980\,620\ \mathrm{mGal}$, free air $3.477$–$23.735\ \mathrm{mGal}$,
slab $1.262$–$8.613\ \mathrm{mGal}$, terrain term $-0.084$ to
$+0.994\ \mathrm{mGal}$, and the signal itself $0.012$–$0.532\ \mathrm{mGal}$.
**The signal is the smallest number in the chain, by two to five orders of
magnitude**: this single table is the reason the workflow must be verified rather
than assumed.

## 5. Verification of the whole pipeline against truth

Because the SYNTHETIC world was constructed with the anomaly being exactly the
buried sphere's attraction, the pipeline's output can be compared with it:

| quantity | value |
|---|---|
| truth | $0.012$ to $0.532\ \mathrm{mGal}$ |
| recovered residual rms | $0.0029\ \mathrm{mGal} = 2.9\ \mathrm{\mu Gal}$ |
| recovered residual max | $0.0050\ \mathrm{mGal} = 5.0\ \mathrm{\mu Gal}$ |
| reading noise | $2.0\ \mathrm{\mu Gal}$ |
| drift-model residual rms | $1.58\ \mathrm{\mu Gal}$ |
| expected floor, $\sqrt{2.0^{2}+1.58^{2}}$ | $2.55\ \mathrm{\mu Gal}$ |

The pipeline residual ($2.9\ \mathrm{\mu Gal}$) is consistent with the noise floor
computed from the two independent error sources — a genuine end-to-end validation,
and one that is only possible in a synthetic study. In a real survey the equivalent
check is the *closure* of the reduction: a loop or a repeat line should return the
same anomaly, and any discrepancy is un-modelled error.

## 6. Failure diagnostics: each mistake has a shape

The same SYNTHETIC survey, with one thing done wrong at a time:

| mistake | rms error (mGal) | max error (mGal) | correlation with relief |
|---|---|---|---|
| terrain skipped | 0.3380 | 0.9935 | $-0.9480$ |
| Bouguer density 2400 instead of 2670 $\mathrm{kg\,m^{-3}}$ | 0.4372 | 0.7729 | $+0.9986$ |
| free-air coefficient wrong by $0.3\%$ | 0.0389 | — | $+0.9886$ |

Three lessons, each with a number attached:

1. **All three mistakes produce a residual that correlates strongly with relief.**
   The correlation coefficient is the diagnostic: a residual correlated with
   topography is a reduction error, not geology. $-0.95$ to $+0.999$ are
   unmistakable, and a scatter plot of the anomaly against elevation or relief is
   the cheapest quality-control test that exists.
2. **The magnitude of the density error is not simply $2\pi G\Delta\rho h$.** The
   plate formula predicts a slope of $0.01132\ \mathrm{mGal\,m^{-1}}$ and the fitted
   slope is $0.00980\ \mathrm{mGal\,m^{-1}}$ ($87\%$), because the residual is
   proportional to the hill's *attraction* — a broader, smoother function of
   position — not to its relief. The plate formula gives the order of magnitude and
   the sign, not an identity.
3. **Small coefficient errors tilt the map.** A $0.3\%$ error in the free-air
   coefficient is $0.0389\ \mathrm{mGal}$ rms here, perfectly correlated with relief
   — and it would be read as a long-wavelength geological trend if the map were
   interpreted without the check.

## 7. The error budget of the delivered anomaly

Terms, expressed as the cost of each item being wrong by a stated amount:

| term | cost (µGal) | type |
|---|---|---|
| reading noise (single reading) | 2.00 | random |
| drift model (loop bracket) | 1.58 | correlated in time |
| absolute tie | 5.00 | correlated across the survey |
| calibration scale ($0.04\%$ of a $3\ \mathrm{mGal}$ span) | 1.20 | correlated |
| normal-gravity convention | 0.50 | convention |
| free-air coefficient, if wrong by $0.3\%$ | 33.39 | model |
| terrain model, 100 m vs 200 m cells | 156.16 | model |
| **total in quadrature** | **159.80** | |

Read this as a *sensitivity table*, not as a measurement: each row answers "what
does this term cost if it is wrong by the stated amount?" The conclusions are:

1. **The reduction model dominates the instrument.** The terrain-model cell size and
   the free-air coefficient together exceed every instrumental and survey term by an
   order of magnitude. Buying a better gravimeter would change nothing here.
2. **The dominant term is controllable.** A finer DEM or a smaller cell reduces the
   $156\ \mathrm{\mu Gal}$; using the latitude-dependent free-air coefficient removes
   the $33\ \mathrm{\mu Gal}$. Neither requires new hardware.
3. **The tie is correlated and cancels in anomalies.** It dominates the *absolute*
   value's budget ($5\ \mathrm{\mu Gal}$) and is absent from a map of anomalies
   within the survey.
4. **The convention is not an error.** The normal-gravity convention contributes
   $0.5\ \mathrm{\mu Gal}$ of *definition*, not of mistake; the honest response is to
   state the convention, not to reduce the term.

## 8. Reproducibility: the workflow is part of the result

A reduction is a computation with inputs, and two analysts with the same data can
produce different anomalies. A reproducible workflow records:

- the **density** used, its provenance and its uncertainty;
- the **DEM**: product, resolution, vertical datum, integration cell size and the
  residual between two cell sizes;
- the **terrain-correction convention and extent**, with the convergence test and
  the difference between the two extents;
- the **reference system** for normal gravity (ellipsoid, formula, tide system);
- the **station coordinates and heights** with their datum and their uncertainty;
- the **software** version, the parameter file and the intermediate products, so
  that any single step can be re-run without repeating the whole chain.

The discipline is the same one that module
[22](../../22-data-engineering-reproducibility/README.md) develops in general: a
reduction that cannot be re-run identically by someone else is not a result, it is a
claim.

## 9. Assumptions and regime of validity

1. **Consistent vertical datum** between station heights and the DEM.
2. **The free-air coefficient is applied at the station's latitude** and from a
   stated ellipsoid/convention.
3. **The Bouguer density is stated with its provenance.** Section 6 measures its
   effect, and it is model-dependent.
4. **The terrain model's extent and cell size are stated**, with the discretisation
   error estimated by comparison (Section 3).
5. **Station positions are accurate** to the tolerance implied by the latitude
   gradient: $0.813\ \mathrm{mGal\,km^{-1}}$ at $45^\circ$ means 100 m of position
   error is $0.08\ \mathrm{mGal}$.
6. **The reduction is validated against an identity or a repeat**, not against a
   hope: the slab−terrain identity, a loop closure, or a comparison with an
   independent survey.
7. **The delivered quantity is named**: free-air anomaly, simple Bouguer, complete
   Bouguer, or isostatic residual. Each is a different number from the same data.
8. **The pipeline is reproducible**: versioned code, recorded inputs, stored
   intermediate products.

## 10. Python demonstration

`code/corrections_workflow_demo.py` prints, with units:

1. the SYNTHETIC survey: stations, heights, latitudes, readings, drift;
2. the drift correction from the loop, the implied rate and its residual rms;
3. normal gravity and the free-air correction over the survey;
4. the prism terrain model with two independent verifications (brute-force point
   sum; Monte-Carlo volume integral) and the cell-size error;
5. the slab, the terrain term with its convention stated, and the identity check;
6. the delivered complete Bouguer anomaly against the known truth, with the residual
   compared with the noise floor;
7. the three failure diagnostics and the error budget.

Exercises and solutions:
[`exercises/04-corrections-workflow-exercises.md`](exercises/04-corrections-workflow-exercises.md),
[`exercises/04-corrections-workflow-solutions.md`](exercises/04-corrections-workflow-solutions.md).

## Mastery checkpoint

Answer without notes.

> A SYNTHETIC survey of 40 stations covers 900 m of relief. **(a)** Draw the
> processing sequence as a list of steps with what each removes. **(b)** Compute the
> free-air, slab and terrain terms for a station 400 m above the datum with a
> $0.5\ \mathrm{mGal}$ terrain term. **(c)** State which of the three mistakes
> (terrain skipped, density error, free-air error) would produce a residual
> correlated *negatively* with relief, and why. **(d)** State the identity that a
> correct implementation must satisfy exactly, and how you would use it as a test.
> **(e)** Rank the four largest terms of your error budget and state which one you
> would attack first.

A worked version of (b)–(d) is in the
[solutions](exercises/04-corrections-workflow-solutions.md).

## Common pitfalls

1. **Treating the sequence as data processing rather than modelling.** Most steps
   inject a model, and the models dominate the error budget.
2. **Applying the corrections out of order or with inconsistent heights.** The
   free-air, slab and terrain terms all depend on the vertical datum.
3. **Quoting a terrain correction without its sign convention.**
4. **Ignoring the terrain model's cell size.** Measured here: $156\
   \mathrm{\mu Gal}$ between 100 m and 200 m cells — larger than the instrument's
   contribution.
5. **Trusting a standard formula without an independent check.** The prism code was
   verified twice; both checks are cheap and neither is optional.
6. **Assuming the density error scales as a plate.** The measured slope was $87\%$ of
   the plate prediction.
7. **Not naming the delivered quantity.** Free-air, simple Bouguer and complete
   Bouguer anomalies from the same readings differ systematically.
8. **Failing to archive inputs and versions.** An unreproducible reduction is not a
   result.

## Related modules

- [Module 02 — Gravity Instruments and Surveys](README.md) — this module; lessons
  [01](01-absolute-gravimeters.md)–[03](03-survey-procedures.md) produce the readings
  and differences reduced here, and lesson [05](05-airborne-marine-gravity.md) adds
  the moving-platform corrections.
- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../01-gravity-fundamentals/04-gravity-reduction.md) —
  the derivations of each correction.
- [05-06 Data Processing Principles](../../05-core-geophysics/06-data-processing-principles/README.md) —
  pipeline architecture, transparency and reproducibility.
- [Module 04 — Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md) —
  datums and height systems, without which the height terms are undefined.
- [Module 22 — Data Engineering and Reproducibility](../../22-data-engineering-reproducibility/README.md) —
  versioning, provenance and reproducible pipelines.
