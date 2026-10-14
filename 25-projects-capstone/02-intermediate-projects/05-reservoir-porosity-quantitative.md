---
id: 25-02-05
title: "Project: Porosity from Well Logs with Uncertainty"
level: intermediate
prereqs: ["25-01-01", "05-04-01", "05-04-04", "05-04-07"]
estimated_minutes: 150
tags: [projects, petrophysics, well-logs, porosity, uncertainty, teaching]
---

# Project: Porosity from Well Logs with Uncertainty

## Learning objectives

1. **Derive** the density-porosity and Wyllie sonic-porosity relations from their volumetric and
 travel-time definitions.
2. **Compute** both porosities for a depth interval and **report** each with its propagated
 uncertainty in porosity units.
3. **Combine** two independent estimates by inverse-variance weighting and **state** the weight
 each receives and why.
4. **Compute** the sensitivity $\partial\phi/\partial\rho_\text{ma}$ and **measure** the
 systematic porosity error produced by a wrong matrix assignment.
5. **Use** the disagreement between two estimators as a diagnostic: compute how many standard
 errors apart they are and **state** what a large value implies.
6. **Separate** the random and systematic parts of the uncertainty budget, and **explain** why
 averaging more samples does not reduce the larger one.

## Prerequisites

- [25-01-01 Project: Units, Conversions and First Scientific Plots](../01-beginner-projects/01-units-and-plotting.md) —
  the unit audit, including the porosity-unit convention used throughout.
- [05-04-01 Porosity, Density and Velocity Relationships](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  the volumetric relations this project inverts.
- [05-04-04 Velocity-Porosity-Clay Models and Empirical Relations](../../05-core-geophysics/04-rock-physics/04-velocity-porosity-clay.md) —
  what Wyllie's relation neglects, and which alternatives exist.
- [05-04-07 Electrical Properties, Archie's Law and Clay Effects](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md) —
  the third, independent porosity estimator that a full interpretation would add.

## 1. The question

*What is the porosity of this interval, and how much of the answer is a
measurement rather than an assumption?*

Petrophysics is the part of geophysics in which the **assumptions are usually
larger than the errors**, and this project is built to show it quantitatively. A
density log with $0.02\ \mathrm{g\,cm^{-3}}$ precision gives porosity to about
$1.2$ porosity units per sample; using the wrong matrix density shifts it by
$2.9$ porosity units — a systematic term almost **ten times** the random one.
The deliverable is therefore not a porosity but a porosity *with a budget*.

## 2. The data

**Synthetic logs.** Ten samples at 1 m spacing from 2000 to 2009 m, with bulk
density $\rho_b$ drawn about $2.32\ \mathrm{g\,cm^{-3}}$ with a log uncertainty of
$0.02\ \mathrm{g\,cm^{-3}}$, and compressional slowness $\Delta t$ drawn about
$76.5\ \mathrm{\mu s\,ft^{-1}}$ with a log uncertainty of
$2.0\ \mathrm{\mu s\,ft^{-1}}$. The measured sample means are
$\rho_b = 2.3270 \pm 0.0222\ \mathrm{g\,cm^{-3}}$ and
$\Delta t = 76.5405 \pm 2.0061\ \mathrm{\mu s\,ft^{-1}}$.

**Assumed parameters (not measured).** Sandstone matrix
$\rho_\text{ma} = 2.65\ \mathrm{g\,cm^{-3}}$ and
$\Delta t_\text{ma} = 55.5\ \mathrm{\mu s\,ft^{-1}}$; fluid
$\rho_f = 1.00\ \mathrm{g\,cm^{-3}}$ and
$\Delta t_f = 189.0\ \mathrm{\mu s\,ft^{-1}}$. A limestone matrix is taken as the
alternative in §6, with $\rho_\text{ma} = 2.71\ \mathrm{g\,cm^{-3}}$ and
$\Delta t_\text{ma} = 47.5\ \mathrm{\mu s\,ft^{-1}}$. **Every one of these is an
assumption about the rock, and each is a term in the budget.**

**Provenance.** SYNTHETIC. Real log suites exist in national data repositories and
in operator archives; this project uses chosen values so that the measurement
errors and the assumption errors can be separated exactly.

## 3. The project specification

**Steps.**

1. State the two estimator equations, the assumed matrix and fluid parameters,
   and the unit of the result (porosity units, where
   $1\ \mathrm{p.u.} = 1\%$ of bulk volume).
2. Compute both porosities sample by sample, then report the interval mean of
   each with its standard error.
3. Propagate the *log* uncertainty to a per-sample porosity uncertainty for each
   estimator, and then to the standard error of each mean.
4. Combine the two means by inverse-variance weighting and report the weights.
5. Compute the sensitivity $\partial\phi/\partial\rho_\text{ma}$ and the porosity
   shift produced by switching the matrix from sandstone to limestone; repeat for
   the sonic estimator.
6. Compare the two estimators' means and express their difference in units of
   their combined standard error.
7. Write the budget: random term, systematic term, combined, and the percentage of
   the combined variance that each contributes.

**Deliverable.** A two-estimator porosity log, a weighted porosity with its
budget, and a sensitivity table for the matrix and fluid parameters.

**Success criterion.** Every porosity is in p.u.; the random and systematic terms
are separated; the assumed matrix is named; the estimator disagreement is
quantified rather than attributed to noise without testing.

## 4. The two estimators

**Density porosity.** A rock of porosity $\phi$ filled with fluid of density
$\rho_f$ has bulk density

$$\rho_b = \phi\,\rho_f + (1-\phi)\,\rho_\text{ma}
\;\Longrightarrow\;
\boxed{\;\phi_D = \frac{\rho_\text{ma} - \rho_b}{\rho_\text{ma} - \rho_f}.\;}$$

With $\rho_\text{ma} = 2.65$ and $\rho_f = 1.00\ \mathrm{g\,cm^{-3}}$, the
denominator is $1.65\ \mathrm{g\,cm^{-3}}$, so a $0.02\ \mathrm{g\,cm^{-3}}$ log
error becomes $0.0121$ of porosity, i.e. $1.21\ \mathrm{p.u.}$

**Wyllie sonic porosity.** Travel time through the rock is the sum of the matrix
and fluid contributions:

$$\Delta t = (1-\phi)\Delta t_\text{ma} + \phi\,\Delta t_f
\;\Longrightarrow\;
\boxed{\;\phi_S = \frac{\Delta t - \Delta t_\text{ma}}{\Delta t_f - \Delta t_\text{ma}}.\;}$$

With $\Delta t_f - \Delta t_\text{ma} = 189.0 - 55.5 = 133.5\
\mathrm{\mu s\,ft^{-1}}$, a $2.0\ \mathrm{\mu s\,ft^{-1}}$ log error becomes
$1.50\ \mathrm{p.u.}$

Both estimators are *linear* in their log reading, which is why their
uncertainties propagate so simply — and why the sensitivity to the *assumed*
parameters is also linear and equally easy to quantify.

## 5. Uncertainty propagation, in closed form

For the density estimator, differentiating with respect to each input:

$$\frac{\partial\phi_D}{\partial\rho_b} = -\frac{1}{\rho_\text{ma}-\rho_f}
= -\frac{1}{1.65} = -0.6061\ (\mathrm{g\,cm^{-3}})^{-1},$$

$$\frac{\partial\phi_D}{\partial\rho_\text{ma}}
= \frac{\rho_b-\rho_f}{(\rho_\text{ma}-\rho_f)^{2}}
= \frac{2.3270-1.00}{1.65^{2}} = 0.4874\ (\mathrm{g\,cm^{-3}})^{-1}.$$

For the sonic estimator,

$$\frac{\partial\phi_S}{\partial\Delta t}
= \frac{1}{\Delta t_f-\Delta t_\text{ma}} = \frac{1}{133.5}
= 0.007491\ (\mathrm{\mu s\,ft^{-1}})^{-1}.$$

The two derivatives are the entire budget. The first gives the random term, the
second the systematic one, and their **ratio** is what decides how to spend
effort: a matrix uncertainty of $0.06\ \mathrm{g\,cm^{-3}}$ (the
sandstone-to-limestone difference) multiplies $0.4874$ into $0.0292$, i.e.
$2.92\ \mathrm{p.u.}$, which is larger than the log noise contribution of
$1.21\ \mathrm{p.u.}$ — and unlike the log noise it does not average away.

## 6. Worked example: the demonstration's numbers

**Per-estimator results.**

| estimator | interval mean (p.u.) | sample sd (p.u.) | SEM (p.u.) | per-sample $\sigma$ (p.u.) |
|---|---|---|---|---|
| density | $19.575$ | $1.348$ | $0.426$ | $1.212$ |
| sonic (Wyllie) | $15.761$ | $1.503$ | $0.475$ | $1.498$ |

**Combination.** Using the standard errors of the means,
$\sigma_{\bar D} = 1.212/\sqrt{10} = 0.383$ and
$\sigma_{\bar S} = 1.498/\sqrt{10} = 0.474\ \mathrm{p.u.}$, the inverse-variance
weights are $60.4\%$ (density) and $39.6\%$ (sonic), and

$$\phi_w = \frac{w_D\bar\phi_D + w_S\bar\phi_S}{w_D+w_S} = 18.066\ \mathrm{p.u.},
\qquad
\sigma_w = \frac{1}{\sqrt{w_D+w_S}} = 0.298\ \mathrm{p.u.}$$

**Systematic term.** Switching the matrix to limestone
($\rho_\text{ma} = 2.71\ \mathrm{g\,cm^{-3}}$):

$$\Delta\phi = \frac{\partial\phi_D}{\partial\rho_\text{ma}}\,\Delta\rho_\text{ma}
= 0.4874 \times 0.06 = +0.0292 = +2.92\ \mathrm{p.u.},$$

which agrees with the exact recomputation ($19.575 \rightarrow 22.397\
\mathrm{p.u.}$) to first order. That shift is **9.8 times** the random
uncertainty $\sigma_w = 0.298\ \mathrm{p.u.}$

The sonic estimator is even more matrix-sensitive: using
$\Delta t_\text{ma} = 47.5$ instead of $55.5\ \mathrm{\mu s\,ft^{-1}}$ moves
$\phi_S$ from $15.761$ to $20.523\ \mathrm{p.u.}$, a shift of
$+4.763\ \mathrm{p.u.}$

**Budget.**

| term | value (p.u.) | share of variance |
|---|---|---|
| random (log precision) | $0.30$ | $1\%$ |
| systematic (matrix assignment) | $2.92$ | $99\%$ |
| combined | $2.94$ | $100\%$ |

$$\phi = 18.07 \pm 0.30\ (\text{random}) \pm 2.92\ (\text{systematic})\ 
\mathrm{p.u.}$$

## 7. The disagreement between estimators is a diagnostic

The two estimators differ by $19.575 - 15.761 = 3.814\ \mathrm{p.u.}$, which is
**6.3 times** their combined standard error
$\sqrt{0.383^{2}+0.474^{2}} = 0.608\ \mathrm{p.u.}$

That is a detection. Two estimators of the same physical quantity that differ by
more than a few standard errors are telling you that at least one of the shared
assumptions is wrong. The candidates, in order of likelihood:

1. **The matrix assignment.** A shaly or dolomitic interval breaks both
   relations in different directions, and the sign of the discrepancy identifies
   which.
2. **The Wyllie relation itself.** It assumes a uniform, water-filled,
   intergranular pore system; vuggy, fractured or hydrocarbon-bearing rock
   satisfies it poorly, and the departure is the standard "secondary porosity"
   indicator.
3. **Shale.** Clay-bound water has a density near the matrix and a slowness near
   the fluid, so it moves the two estimators in opposite directions.

Reporting the discrepancy as 6.3 standard errors, and naming the candidates, is
the deliverable. Reporting the weighted mean without it hides the single most
informative number in the interval.

## 8. Failure modes and how to detect them

1. **A matrix parameter treated as measured.** *Detect:* the sensitivity table;
   $2.92\ \mathrm{p.u.}$ for a $0.06\ \mathrm{g\,cm^{-3}}$ change.
2. **Averaging the two estimators without checking they agree.** *Detect:* the
   $6.3\sigma$ discrepancy; inverse-variance weighting is only valid for
   *consistent* estimators.
3. **Quoting porosity without units or the p.u. convention.** *Detect:* a
   dimensionless $0.18$ and $18\ \mathrm{p.u.}$ are the same number written two
   ways; mixing them with a fraction is a factor-of-100 error waiting to happen.
4. **Propagating the log error as if it were the mean's error.** *Detect:*
   compare the per-sample $\sigma$ ($1.21\ \mathrm{p.u.}$) with the SEM
   ($0.38\ \mathrm{p.u.}$); they differ by $\sqrt{10}$.
5. **Ignoring hydrocarbon or invasion effects.** *Detect:* a gas-bearing interval
   raises density porosity and lowers neutron porosity; a single porosity from a
   single log has no way to see it.

## 9. Rubric

| Criterion | 4 — exemplary | 3 — competent | 2 — developing | 1 — incomplete |
|---|---|---|---|---|
| Estimators | Both derived with units and assumptions | Both stated | One | Formula only |
| Uncertainty | Per-sample and per-mean, random separated from systematic | Random term | Stated | Absent |
| Combination | Inverse-variance with weights quoted, consistency checked | Weighted mean | Simple average | One estimator |
| Systematic | $\partial\phi/\partial\rho_\text{ma}$ computed and applied | Shift quoted | Mentioned | Absent |
| Report | Budget table with shares, plus the discrepancy diagnostic | Budget | Value | Unsupported |

## 10. Assumptions and regime of validity

1. **Known matrix and fluid properties.** These are the dominant budget term, and
   they are assumptions about the rock, not measurements of it.
2. **A single, uniform pore fluid.** A gas–water transition invalidates both
   relations in different ways; a full interpretation uses neutron and resistivity
   logs to identify the fluid.
3. **No shale.** Clay-bound water contributes to neither the matrix nor the free
   fluid, and the omission biases density porosity high and sonic porosity low.
4. **Linear relations.** Both estimators are endpoints-interpolations; real
   rocks have stress, clay and textural effects that make the relation
   non-linear, and the Wyllie relation in particular is a plain-time-average
   idealisation.
5. **The interval is homogeneous.** Averaging over an interval assumes the
   porosity is one number; over a heterogeneous interval the mean is a
   thickness-weighted average and the *spread* is geology, not noise.

## The honest summary

Two linear estimators, one budget, one diagnostic. The density log gives
$19.575\ \mathrm{p.u.}$ and the sonic log $15.761\ \mathrm{p.u.}$ over the
interval; inverse-variance weighting gives $18.066\ \mathrm{p.u.}$ with a random
uncertainty of only $0.298\ \mathrm{p.u.}$; and switching the matrix from
sandstone to limestone moves the density porosity by $+2.92\ \mathrm{p.u.}$ —
nine times the random term, and $99\%$ of the combined variance. The two
estimators disagree by $6.3$ standard errors, which is not noise but a statement
that a shared assumption is wrong. The transferable lesson is the ordering: the
matrix and fluid parameters are not bookkeeping, they are the answer's largest
single term, and a porosity quoted without them is quoted to a precision that does
not exist.

## Python demonstration

[`code/porosity_well_logs_demo.py`](./code/porosity_well_logs_demo.py) prints every number quoted above, writes no files,
uses no network and exits 0:

```bash
cd 25-projects-capstone/02-intermediate-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python porosity_well_logs_demo.py
```

It is seeded with `np.random.default_rng(20261014)` and runs in under a second.
## Exercises

Graded problems and worked solutions are in
[`exercises/05-reservoir-porosity-quantitative-exercises.md`](./exercises/05-reservoir-porosity-quantitative-exercises.md)
and
[`exercises/05-reservoir-porosity-quantitative-solutions.md`](./exercises/05-reservoir-porosity-quantitative-solutions.md).
The ★★★ item asks you to design an interpretation that identifies the cause of the
estimator discrepancy, not to average one more pair of numbers.

## Mastery checkpoint

Without notes:

1. Derive the density-porosity relation from the volumetric mixing equation.
2. Compute $\phi_D$ for $\rho_b = 2.40\ \mathrm{g\,cm^{-3}}$ with a quartz matrix
   and a $1.00\ \mathrm{g\,cm^{-3}}$ fluid, and give the answer in p.u.
3. Compute the porosity shift produced by using $\rho_\text{ma} = 2.71$ instead of
   $2.65\ \mathrm{g\,cm^{-3}}$ when $\rho_b = 2.40\ \mathrm{g\,cm^{-3}}$.
4. Two estimators give $18.0 \pm 0.3$ and $16.0 \pm 0.4\ \mathrm{p.u.}$ Are they
   consistent? Quantify.

## Common pitfalls

1. **Treating the two estimators as interchangeable.** Their disagreement is a diagnostic for shale, gas or a bad matrix value, not a nuisance to be averaged away.
2. **Fixing the matrix parameters.** The porosity scales with them; their uncertainty must be propagated, not assumed away.
3. **Propagating only the log-measurement noise.** The matrix and fluid terms usually dominate the budget.
4. **Reporting porosity without the depth basis.** Net-to-gross, depth interval and cut-offs all change the number.
5. **Quoting a porosity to more digits than the estimator supports.** The ratio of two uncertain quantities rarely justifies more than two significant figures.

## Where this is used

Porosity is the input to every volumetric reserve estimate and to the
density–velocity relations used in seismic inversion. The next project in the
folder, [25-03-06](../03-advanced-projects/06-gravity-inversion-uq.md), applies
the same random-versus-systematic accounting to an inversion, and
[25-04-05](../04-graduate-projects/05-joint-inversion-project.md) couples log
petrophysics to seismic and gravity data through a petrophysical relation — where
the matrix assumption of this project becomes the prior of that inversion. In
professional practice the budget table of §6 is the standard "uncertainty
statement" on a petrophysical evaluation, and the discrepancy diagnostic of §7 is
the standard secondary-porosity indicator.

## Related lessons

- [05-04-03 Gassmann Fluid Substitution and Saturation Effects](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md) —
  what changes when the pore fluid is not water.
- [09-01-02 Archie's Law, Porosity and Saturation](../../09-electrical-em-methods/01-electrical-properties-of-earth/02-archies-law.md) —
  the third estimator, with its own independent assumptions.
- [18-05-02 Constructing Likelihoods and Error Models](../../18-inverse-problems/05-bayesian-inversion/02-likelihood-models.md) —
  the formal treatment of combining estimators and weighting them.
- [25-03-06 Project: Gravity Inversion with Uncertainty Quantification](../03-advanced-projects/06-gravity-inversion-uq.md) —
  the same budget logic applied to a geophysical inversion.

## Self-assessment checklist

- [ ] I can derive both porosity relations from their mixing equations.
- [ ] I can propagate a log uncertainty to a porosity uncertainty per sample.
- [ ] I can compute and use $\partial\phi/\partial\rho_\text{ma}$.
- [ ] I can combine two estimators by inverse-variance weighting with weights.
- [ ] I can test two estimators for consistency in units of their errors.
- [ ] I can write a budget that separates random from systematic terms.
