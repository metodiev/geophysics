---
id: 25-04-06
title: "Project: Crustal Structure from Receiver Functions"
level: graduate
prereqs: ["25-02-01", "06-08-02", "06-08-01", "18-04-01"]
estimated_minutes: 200
tags: [projects, seismology, receiver-functions, crust, h-k, teaching]
---

# Project: Crustal Structure from Receiver Functions

## Learning objectives

By the end of this project you will be able to:

1. **Derive** the delay times of the Ps, PpPs and PpSs+PsPs phases in terms of
   crustal thickness, $V_p$, $V_p/V_s$ and the ray parameter.
2. **Construct** a synthetic receiver function and **identify** each phase's
   arrival and polarity convention.
3. **Perform** H-K stacking on a grid and **report** the recovered thickness,
   $V_p/V_s$ and the peak value of the stack.
4. **Demonstrate** the $H$–$V_p/V_s$ trade-off by inverting with one phase at a
   time, and **state** why all three are stacked.
5. **Report** the result as a region rather than a point, using the half-maximum
   contour as the resolution statement.
6. **State** the four assumptions that the method makes, including the assumed
   $V_p$, and where each fails.
7. **Grade** an H-K result by whether it carries its $V_p$, its ray parameter, its
   noise level and its trade-off region.

All data in this project are **SYNTHETIC**: a receiver function built as a sum of
Gaussians at the exact ray-theoretical arrival times by
[`code/receiver_function_demo.py`](./code/receiver_function_demo.py). Waveforms and
station metadata for the project itself are available from the IRIS/EarthScope FDSN
services at <https://service.iris.edu/fdsnws/dataselect/1/query> and
<https://service.iris.edu/fdsnws/station/1/query>.

## Prerequisites

- [25-02-01 Project: Travel-Time Curves and 1-D Velocity Structure](../02-intermediate-projects/01-travel-time-curves.md) —
  the delay-time algebra used here.
- [06-08-01 Receiver Function Principles and Estimation](../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md) —
  how a receiver function is estimated from a three-component record.
- [06-08-02 H-K Stacking and Crustal Thickness Estimation](../../06-seismology/08-receiver-functions-and-crustal-structure/02-h-k-stacking.md) —
  the method this project implements and interrogates.
- [18-04-01 Local Linearisation, Jacobians and Iteration](../../18-inverse-problems/04-nonlinear-inversion/01-local-linearization.md) —
  the grid-search alternative to a linearised inversion.

## 1. The question

*How thick is the crust here, and how much of that answer is the assumed $V_p$?*

The H-K method is the standard crustal-thickness estimator from teleseismic data,
and it works because three different multiples of the Moho conversion depend on
crustal thickness $H$ and the ratio $k = V_p/V_s$ in *different* ways. A single
phase constrains a curve in the $(H,k)$ plane; three phases intersect at a point.
The demonstration measures both halves of that statement: the joint stack recovers
$H = 35.00\ \mathrm{km}$ and $k = 1.750$ exactly, while the Ps phase alone gives
$28.50\ \mathrm{km}$ and $1.925$, PpPs alone $36.75\ \mathrm{km}$ and $1.630$, and
PpSs+PsPs alone $23.50\ \mathrm{km}$ and $2.000$ — every one of them wrong.

## 2. The model and the phases

**Synthetic crust (SYNTHETIC).** $H = 35.0\ \mathrm{km}$,
$V_p = 6.30\ \mathrm{km\,s^{-1}}$, $V_p/V_s = 1.75$ (hence
$V_s = 3.600\ \mathrm{km\,s^{-1}}$), and a teleseismic ray parameter
$p = 0.060\ \mathrm{s\,km^{-1}}$.

With the vertical slownesses $\eta_p = \sqrt{V_p^{-2}-p^{2}}$ and
$\eta_s = \sqrt{V_s^{-2}-p^{2}}$:

| phase | delay time | value (s) |
|---|---|---|
| Ps | $H(\eta_s-\eta_p)$ | $4.3493$ |
| PpPs | $H(\eta_s+\eta_p)$ | $14.6361$ |
| PpSs+PsPs | $2H\eta_s$ | $18.9854$ |

The three expressions are **linearly independent in $H$ and $k$**: Ps measures the
difference of the vertical slownesses, PpPs their sum, and PpSs+PsPs twice the
S-leg. That is the entire basis of the method, and the reason a single phase cannot
determine both parameters.

**The receiver function (SYNTHETIC).** A sum of Gaussians of half-width
$0.5\ \mathrm{s}$ at the three times, with amplitudes $1.00$, $0.50$ and $0.35$
after the standard polarity convention (the PpPs phase is negated so that all three
contribute positively to the stack), plus $2\%$ noise, sampled at $0.05\
\mathrm{s}$ over a $30\ \mathrm{s}$ window.

## 3. The project specification

**Steps.**

1. Compute the three delay times for the true model and verify that they are
   independent functions of $H$ and $k$.
2. Build the synthetic receiver function with a stated polarity convention.
3. Grid-search $H \in [20, 60]\ \mathrm{km}$ and $k \in [1.60, 2.00]$ on a
   $161 \times 81$ grid, computing the weighted stack of the three predicted
   arrivals; report the peak location and value.
4. Repeat with one phase at a time and report each phase's peak location, to
   demonstrate the trade-off.
5. Report the half-maximum region of the joint stack as the resolution statement.
6. Perturb the assumed $V_p$ by $\pm 5\%$, refit, and report how $H$ and $k$ move.
7. Write the report: the phases, the polarity convention, the recovered
   $(H, k)$, the trade-off demonstration, the resolution region, and the assumed
   $V_p$.

**Deliverable.** The delay-time table, the H-K surface peak, the per-phase peak
table, the half-maximum region, and the $V_p$ sensitivity.

**Success criterion.** $H$ is reported with the assumed $V_p$; $k$ is reported with
its trade-off region; the polarity convention is stated; the resolution is a
region, not a pair of numbers.

## 4. H-K stacking and the trade-off

The objective is the weighted sum of the receiver function sampled at the three
predicted arrival times,

$$s(H,k) = w_1\,A\bigl[t_\text{Ps}(H,k)\bigr]
+ w_2\,A\bigl[t_\text{PpPs}(H,k)\bigr]
+ w_3\,A\bigl[t_\text{2}(H,k)\bigr],
\qquad (w_1,w_2,w_3) = (0.5, 0.3, 0.2),$$

maximised over the $(H,k)$ grid. Measured on the demonstration's synthetic RF:

| quantity | value |
|---|---|
| grid | $161 \times 81$ ($H$ 20–60 km, $k$ 1.60–2.00) |
| peak stack value | $0.729$ |
| recovered $H$ | $35.00\ \mathrm{km}$ (true 35.0) |
| recovered $V_p/V_s$ | $1.750$ (true 1.750) |
| half-maximum region | $H$ 24.75–46.75 km, $k$ 1.60–2.00 |

The recovery is **exact** because the synthetic receiver function was built from the
same ray-theoretical times used in the stack — which makes the demonstration a test
of the *method* rather than of the model. The half-maximum region is broad
($\pm 11\ \mathrm{km}$ in $H$), and that breadth, not the exact recovery, is the
honest resolution statement: a smoothing filter, a dipping Moho or a real noise
level would widen it further, and the method's formal precision is set entirely by
how sharply the three arrivals can be timed.

**One phase at a time** (same RF, same grid):

| phase | $H$ (km) | $V_p/V_s$ | stack peak |
|---|---|---|---|
| Ps only | $28.50$ | $1.925$ | $1.028$ |
| PpPs only | $36.75$ | $1.630$ | $0.503$ |
| PpSs+PsPs only | $23.50$ | $2.000$ | $0.503$ |

Each single-phase solution sits at a different, wrong point on the same
$(H,k)$ trade-off curve, and each is a plausible-looking answer. This is the
project's central demonstration: **the trade-off is not a caveat, it is the reason
three phases are stacked**, and a study that reports a single-phase thickness has
reported a point on a curve as if it were an intersection.

## 5. Why the trade-off exists, and how far it extends

$H$ enters each delay time linearly, so any phase gives
$t = H\,f(k)$, a hyperbola in the $(H,k)$ plane. Three hyperbolas intersect at a
point only because their $f(k)$ differ; where they are nearly parallel — for a
narrow $k$ range, or a small velocity contrast across the Moho — the intersection
becomes a long thin region. The half-maximum contour of the demonstration's stack
is exactly that region, and it is broad because the synthetic arrivals are wide
Gaussians.

Two practical consequences:

1. **The width of the trade-off region scales with the arrival-time uncertainty
   divided by the separation of the hyperbolas' slopes.** A noisy station, a
   thick sedimentary column (whose own conversions contaminate the window), or a
   dipping interface all widen it.
2. **Averaging over many stations does not help if they share the assumed $V_p$.**
   The bias from $V_p$ is common-mode: only an independent $V_p$ — from a
   refraction profile, a borehole, or a joint inversion with surface waves
   (which measure $V_s$ and hence, with the same $H$, remove the ambiguity) —
   removes it.

## 6. Assumptions and regime of validity

1. **A laterally homogeneous, flat-layered crust.** A dipping Moho, a thick
   sedimentary basin or a Moho with topography violates it and fans the arrivals;
   the azimuthal dependence of the recovered $H$ is the diagnostic.
2. **Correct $V_p$.** $H$ scales with $V_p$ almost linearly, so a $5\%$ $V_p$ error
   is a $5\%$ thickness error. $V_p$ is rarely measured where the receiver
   functions were recorded, which is why the number belongs in the report.
3. **An isotropic crust.** Anisotropy converts $V_p/V_s$ into an apparent,
   direction-dependent quantity and is one of the standard false positives for
   lower-crustal mafic composition.
4. **A single conversion interface.** Intracrustal converters and multiples
   contaminate the window and shift the stack peak; a migrated or
   common-conversion-point stack mitigates it.
5. **An accurate ray parameter.** $p$ enters through $\eta_p$ and $\eta_s$; an
   error in the earthquake's distance or the velocity model above the crust biases
   $k$.

## The honest summary

The project's product is a method tested on its own assumptions. The H-K stack
recovers $H = 35.00\ \mathrm{km}$ and $V_p/V_s = 1.750$ exactly from a synthetic
receiver function built from the same delay times, with a stack peak of $0.729$ and
a half-maximum region spanning $24.75$–$46.75\ \mathrm{km}$; each phase alone gives
a *wrong* point on the trade-off curve ($28.50/1.925$, $36.75/1.630$,
$23.50/2.000$). The transferable results are that the thickness is only as good as
the assumed $V_p$, that the honest output is a region rather than a pair of
numbers, and that a single-phase estimate is a curve reported as a point.

## Python demonstration

[`code/receiver_function_demo.py`](./code/receiver_function_demo.py) prints every
number quoted above. It:

1. prints the crustal model and the three delay times with their expressions;
2. builds the synthetic receiver function and prints the amplitudes near each
   arrival, with the polarity convention;
3. grid-searches $(H,k)$, prints the peak value and the recovered model, and prints
   the half-maximum region;
4. repeats the stack with one phase at a time, printing each phase's (wrong) peak
   location.

Run it with the project virtual environment:

```bash
cd 25-projects-capstone/04-graduate-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python receiver_function_demo.py
```

The script prints only, writes no files, uses no network and exits 0. It runs in
under a second.

## Exercises

Graded problems and worked solutions are in
[`exercises/06-receiver-function-project-exercises.md`](./exercises/06-receiver-function-project-exercises.md)
and
[`exercises/06-receiver-function-project-solutions.md`](./exercises/06-receiver-function-project-solutions.md).
The ★★★ item asks you to design a study that removes the $V_p$ ambiguity, not to
rerun the grid search.

## Mastery checkpoint

Without notes:

1. Write the three delay-time expressions and state which is which.
2. For $H = 30\ \mathrm{km}$, $V_p = 6.0\ \mathrm{km\,s^{-1}}$ and
   $V_p/V_s = 1.8$, compute the Ps delay at $p = 0.06\ \mathrm{s\,km^{-1}}$.
3. State why a single phase cannot determine both $H$ and $V_p/V_s$, and what
   three phases do that one cannot.
4. A study reports $H = 38 \pm 1\ \mathrm{km}$ with no $V_p$ and no trade-off
   region. Name the two things missing and what each would change.

## Common pitfalls

1. **Reporting a single-phase result as a thickness.** It is a curve, not a point.
2. **Omitting the assumed $V_p$.** It scales $H$ almost one-for-one.
3. **Treating the grid peak as the precision.** The half-maximum region is
   typically an order of magnitude wider than the grid step.
4. **Ignoring sediment and intracrustal converters.** They add arrivals inside the
   window and shift the peak.
5. **Reading $V_p/V_s$ as composition.** Anisotropy and alteration produce the same
   ratio.

## Where this is used

H-K stacking is a standard step in continental structure studies, and its results
feed the crustal thickness maps used in isostasy and geodynamic modelling. The
$V_p/V_s$ it returns is one of the inputs to the joint inversions of
[25-04-05](./05-joint-inversion-project.md), and its thickness is a constraint on
the Moho depth that a travel-time inversion estimates independently in
[25-02-01](../02-intermediate-projects/01-travel-time-curves.md) — a comparison
worth making, because the two methods fail in different ways. In professional
practice the assumed $V_p$ and the trade-off region are the two items a reviewer
checks first.

## Related lessons

- [06-08-05 Joint Inversion of Receiver Functions and Surface Waves](../../06-seismology/08-receiver-functions-and-crustal-structure/05-joint-inversion-rf.md) —
  the method that removes the $V_p$ ambiguity by adding dispersion.
- [06-10-04 MASW/SASW: Surface-Wave Dispersion and Vs Profiles](../../06-seismology/10-refraction-and-near-surface-seismology/04-masw-sasw.md) —
  the shallow analogue of the $V_s$ constraint.
- [13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength](../../13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md) —
  where a crustal thickness measurement is used.
- [25-02-01 Project: Travel-Time Curves and 1-D Velocity Structure](../02-intermediate-projects/01-travel-time-curves.md) —
  the independent thickness estimate from refraction.

## Self-assessment checklist

- [ ] I can derive the three delay times from the slowness algebra.
- [ ] I can build a receiver function with a stated polarity convention.
- [ ] I can run an H-K grid search and locate the peak.
- [ ] I can demonstrate the trade-off with single-phase stacks.
- [ ] I can report a half-maximum region as the resolution.
- [ ] I can state the effect of the assumed $V_p$ on the thickness.
