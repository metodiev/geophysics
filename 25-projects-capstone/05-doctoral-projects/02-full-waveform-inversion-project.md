---
id: 25-05-02
title: "Project: A Small-Scale Full-Waveform Inversion"
level: doctoral
prereqs: ["06-06-04", "06-06-05", "18-04-01", "25-05-01"]
estimated_minutes: 240
tags: [projects, seismology, fwi, adjoint, waveform-inversion, doctoral]
---

# Project: A Small-Scale Full-Waveform Inversion

## Learning objectives

By the end of this project you will be able to:

1. **Derive** the adjoint-state gradient for a second-order-in-time wave equation
   and **implement** it as the exact transpose of the discrete forward scheme.
2. **Validate** the adjoint by a finite-difference gradient test and **state** what
   the test does and does not prove.
3. **Invert** a waveform dataset with a quasi-Newton optimiser and **report** the
   residual against the noise level rather than against zero.
4. **Diagnose** cycle skipping from the travel-time error expressed in fractions of
   the source period, and **predict** whether a given starting model will converge.
5. **State** the resolution limit in wavelengths and check it against the recovered
   structure.
6. **Design** a multiscale FWI workflow that inverts low frequencies first and
   **justify** the frequency scheduling from the travel-time criterion.
7. **Report** an FWI result with its starting model, its resolved length scale and
   its unconstrained regions, none of which the final image reveals.

All data in this project are **SYNTHETIC**: a 1-D acoustic model whose waveform
response is computed in [`code/full_waveform_inversion_demo.py`](./code/full_waveform_inversion_demo.py).
For the project itself, seismic waveform data from open networks are available
through the IRIS/EarthScope FDSN services at
<https://service.iris.edu/fdsnws/dataselect/1/query> and
<https://service.iris.edu/fdsnws/station/1/query>.

## Prerequisites

- [06-06-04 Full-Waveform Inversion](../../06-seismology/06-seismic-tomography/04-full-waveform-inversion.md) —
  the method and its misfit functions.
- [06-06-05 Adjoint Methods](../../06-seismology/06-seismic-tomography/05-adjoint-methods.md) —
  the theory of the gradient used here.
- [18-04-01 Local Linearisation, Jacobians and Iteration](../../18-inverse-problems/04-nonlinear-inversion/01-local-linearization.md) —
  why a gradient inversion converges to the nearest local minimum.
- [25-05-01 Project: Local Earthquake Tomography](./01-tomography-project.md) —
  the travel-time inversion this project generalises.

## 1. The question

*Can a waveform dataset determine a velocity model that travel-time data cannot,
and what decides whether the inversion finds it?*

Full-waveform inversion uses the entire seismogram, so it carries roughly an order of
magnitude more information per source–receiver pair than picked travel times — in
principle a factor of $1/10$ finer resolution. The demonstration makes both halves
of that statement quantitative. The adjoint gradient is exact
($\cos = 1.0000000000$ against finite differences, magnitude ratio $1.0000009$), so
the optimisation is not the bottleneck; from a starting model $5.5\%$ high the
inversion recovers the layered structure ($1798/1995/1682$ against
$1800/2000/1700\ \mathrm{m\,s^{-1}}$ and reaches the noise level, rms residual
$0.0303$ against a noise level of $0.0309$). From a starting model $13\%$ low it
stalls at rms $0.0479$ and from one $21\%$ high at $0.0416$ — both far above the
noise, both in a local minimum that has nothing to do with the Earth. **FWI is
limited by the starting model and the low-frequency content, not by the gradient.**

## 2. The forward problem, discretised

One-dimensional acoustic wave equation in pressure–slowness-squared form:

$$\frac{\partial^2 p}{\partial t^2} = \frac{1}{m}\,\frac{\partial^2 p}{\partial z^2} + s(t)\,\delta(z-z_s),
\qquad m = \frac{1}{c^2}.$$

Leapfrog in time, second-order in space, Dirichlet at the free surface ($p = 0$) and
at the model bottom:

$$p^{n+1}_i = 2p^n_i - p^{n-1}_i + \frac{\Delta t^2}{m_i\,\Delta z^2}
\bigl(p^n_{i+1} - 2p^n_i + p^n_{i-1}\bigr) + \Delta t^2 s^n \delta_{i,i_s}.$$

**Measured configuration (demo).** $\Delta z = 10$ m, 100 cells ($1.00$ km),
$\Delta t = 1$ ms, 700 steps ($0.70$ s), CFL number $c_{\max}\Delta t/\Delta z = 0.21$
(stable below $1$), a $12\ \mathrm{Hz}$ Ricker source with a co-located receiver.
Dominant wavelength at $2100\ \mathrm{m\,s^{-1}}$ is $175\ \mathrm{m} = 17.5$ cells,
so the best conceivable resolution is about half a wavelength, $88$ m — one fifth of
the model's $1$ km extent, and the number any structure in the final image must be
compared against.

**The model.** Four velocity layers: $1800$, $2000$, $1700$, $2100\
\mathrm{m\,s^{-1}}$ at $0$–$200$, $200$–$400$, $400$–$600$ and $600$–$1000$ m, so a
low-velocity ($1700$) layer sits between two faster ones — the classic
cycle-skipping geometry, because this reflector produces a strong, polarity-reversed
arrival that moves by nearly a full wavelet when the starting model is wrong.

**The data.** Direct-arrival peak $3.086$, rms $0.585$; added noise $0.0309$, i.e.
$1.0\%$ of the peak, giving signal-to-noise $18.9$. Two-way times to the $200$,
$400$ and $600$ m reflectors are $0.222$, $0.422$ and $0.658$ s, so the $0.70$ s
record contains the first two reflections comfortably and **truncates the third** —
which is why the deepest layer is only weakly constrained by this dataset.

## 3. The adjoint gradient

Rather than the continuous adjoint, transpose the discrete scheme exactly. With
$\lambda^n = \partial J/\partial p^n$ and $J = \tfrac{1}{2}\sum_n (p^n_\text{rec}-d^n)^2$,
the reverse sweep over the same time loop is

$$\lambda^n_i \mathrel{+}= 2\lambda^{n+1}_i
+ \frac{\Delta t^2}{m_i\,\Delta z^2}\bigl[L\lambda^{n+1}\bigr]_i,\qquad
\lambda^{n-1}_i \mathrel{+}= -\lambda^{n+1}_i,\qquad
\frac{\partial J}{\partial m_j} = \sum_n \lambda^{n+1}_j\left(-\frac{A_j}{m_j}\right)
\bigl[Lp^n\bigr]_j,$$

with $A_j = \Delta t^2/(m_j\Delta z^2)$ and $L$ the three-point Laplacian. The
source term $\lambda^n_\text{rec} \mathrel{+}= (p^n_\text{rec}-d^n)$ carries **no**
$\Delta t^2$ — a $\Delta t^2$ there scales the whole gradient by $10^{-6}$, the most
common single error in a hand-written adjoint.

**The gradient test (demo).**

| quantity | value |
|---|---|
| $\lVert g_\text{adjoint}\rVert$ | $8.3310\times10^{7}$ |
| $\lVert g_\text{finite difference}\rVert$ | $8.3310\times10^{7}$ |
| $\cos(g_\text{adj}, g_\text{FD})$ | $1.0000000000$ |
| $\lVert g_\text{FD}\rVert/\lVert g_\text{adj}\rVert$ | $1.0000009$ |

The test verifies the gradient of the *discrete* objective, against the *discrete*
parameters, at *one* point in model space. It does not verify the forward solver, the
misfit function or the physics; those need the separate tests in §5.

## 4. Inversion from three starting models

Twenty parameters (layer slowness squared), $701$ data, L-BFGS-B with the analytic
gradient, bounds of a factor $\pm 4$ on the starting model. The misfit of the true
model on the noisy data is $0.3301$ (rms $0.0307$ against a noise level of
$0.0309$), which is the target: an FWI that reaches the noise level has explained
the data, one that reaches zero has fitted the noise.

| start $c$ (m/s) | $J$ start | $J$ final | rms residual | iterations | recovered $c$ at 100/300/500/700 m | verdict |
|---|---|---|---|---|---|---|
| 1900 | 2.6834 | 0.3228 | 0.0303 | 121 | 1798 / 1995 / 1682 / 1898 | recovered |
| 1650 | 5.8857 | 0.8048 | 0.0479 | 122 | 1798 / 1606 / 1288 / 1650 | cycle skipped |
| 2300 | 20.0516 | 0.6067 | 0.0416 | 400 | 1800 / 2459 / 2350 / 2304 | cycle skipped |
| true | — | 0.3301 | 0.0307 | — | 1800 / 2000 / 1700 / 2100 | — |

Three readings, all doctoral-level:

1. **The successful run is not exact.** $1798/1995/1682$ against
   $1800/2000/1700$ — errors of $0.1\%$, $0.25\%$, $1.1\%$ — but the deepest layer
   returns $1898$ against $2100$, an $11\%$ error, because its reflector's arrival is
   truncated by the end of the record. The image is only as complete as the
   illumination.
2. **Two of the three starts fail, with residuals ten times the noise level.** Both
   failures look like plausible models (the $1650$ start returns a smooth, gently
   varying structure) and both would be published by an unwary practitioner.
3. **The best-fitting model is not the true model.** The true model has rms $0.0307$
   while the successful inversion reaches $0.0303$: twenty parameters can absorb
   slightly more noise than the truth does. Model selection can never be done by
   comparing data residuals alone.

## 5. Cycle skipping, quantified

The condition for the local-minimum problem is a travel-time error smaller than half
the dominant period. With $f_0 = 12\ \mathrm{Hz}$, $T/2 = 41.7$ ms. For a
constant-velocity starting model $c_0$, the two-way time to the $400$ m reflector is
$0.800/c_0$ against a true $0.422$ s, and, comparing with the actual inversion
outcome:

| start $c_0$ (m/s) | TWT to 400 m (s) | error (ms) | fraction of $T/2$ | outcome |
|---|---|---|---|---|
| 1900 | 0.421 | $1$ | $0.02$ | converged |
| 1650 | 0.485 | $63$ | $1.5$ | cycle skipped |
| 2300 | 0.348 | $74$ | $1.8$ | cycle skipped |

The criterion predicts the demonstration's three outcomes exactly, which is why it
is the first thing to compute when an FWI fails: **the starting model must be good
enough that no arrival is mis-timed by more than half a period.** The same criterion
supplies the frequency scheduling — inverting $5\ \mathrm{Hz}$ first allows a
travel-time error five times larger, so a multiscale FWI starts where the data are
few and the basin of attraction is wide.

## 6. The project specification

**Steps.**

1. Build the forward solver; report the grid, the CFL number, the source, the
   dominant wavelength and the resolution limit in metres.
2. Build a layered synthetic model, generate the reference data, and add noise;
   report peak, rms and signal-to-noise ratio, and the two-way time to each
   reflector against the record length.
3. Derive and implement the adjoint; verify it with a finite-difference test and
   report the cosine and the magnitude ratio.
4. Invert from a starting model inside the half-period criterion; report the misfit
   trajectory, the final residual against the noise level, and the recovered
   structure against the truth.
5. Invert from two starting models outside the criterion; report their residuals and
   the structures they return.
6. Compute the half-period criterion for each starting model and check it against the
   outcomes.
7. State which parts of the model are constrained by the data and which are not.
8. Design a multiscale schedule (which frequencies, in which order, and why) and
   state the resolution you would claim from each stage.

**Deliverable.** The verified adjoint, the three inversions, the criterion table, and
a statement of the resolved and unresolved parts of the model.

**Success criterion.** The adjoint passes a finite-difference test to within a
stated tolerance; the residual of the successful inversion is compared with the noise
level, not with zero; the failures are diagnosed with the half-period criterion; and
the unconstrained deepest layer is named.

## 7. Assumptions and failure modes

1. **Acoustic, 1-D, constant density.** Real FWI is elastic, 3-D and
   density-coupled; the acoustic approximation misplaces amplitudes and generates
   spurious structure where converted waves are strong.
2. **The source wavelet is known exactly.** In practice the source is estimated
   jointly (or deconvolved), and the source–model trade-off is a null direction that
   can absorb real structure.
3. **Cycle skipping** (§5). The dominant failure, and the reason low frequencies and
   a good starting model matter more than the optimiser.
4. **The free-surface and bottom reflections.** With Dirichlet boundaries both
   reflect; a real acquisition suppresses them with an absorbing boundary condition.
   Any unmodelled arrival is a systematic error that FWI will fit with structure.
5. **Resolution limited by wavelength.** Structures thinner than about half the local
   wavelength ($88$ m here) cannot be recovered however good the data, and a
   "high-resolution" image containing thinner features is a resolution artefact.
6. **Amplitude inconsistency between the true and starting models** biases the
   gradient towards the wrong model even before cycle skipping.

## 8. Rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Forward scheme correct and characterised | 15% | CFL number, wavelength and resolution limit reported |
| Adjoint validated | 20% | finite-difference test with cosine and ratio; scope of the test stated |
| Successful inversion reported honestly | 20% | residual compared with noise; errors per layer given |
| Failures diagnosed | 20% | half-period criterion computed and matched to the outcomes |
| Multiscale design | 15% | frequency schedule justified by the criterion, resolution per stage |
| Resolution and illumination statement | 10% | resolved length scale and the unconstrained layer named |

## 9. The honest summary

The product of this project is an inversion that works, an inversion that fails, and
the quantitative reason for both. The adjoint is exact
($\cos = 1.0000000000$); from a starting model within the half-period criterion
($1$ ms error against a $41.7$ ms limit) the inversion reaches the noise level
($0.0303$ against $0.0309$) and recovers three of the four layers to better than
$1.1\%$; from starts outside it ($63$ and $74$ ms errors) the residual stays ten
times the noise and the model is fiction. The deepest layer carries an $11\%$ error
because its arrival is truncated. A defensible FWI report states the starting model,
the frequency content, the residual against the noise level, the resolved length
scale, and which parts of the image the data do not constrain.

## Python demonstration

[`code/full_waveform_inversion_demo.py`](./code/full_waveform_inversion_demo.py)
prints every number above: the forward configuration, the dataset and its noise
level, the adjoint gradient test, and the three inversions with their residuals and
recovered velocities.

```bash
cd 25-projects-capstone/05-doctoral-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python full_waveform_inversion_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, no network, no files, no
plots, exits 0, runs in about $4.7$ s.

## Exercises

Graded problems and worked solutions are in
[`exercises/02-full-waveform-inversion-project-exercises.md`](./exercises/02-full-waveform-inversion-project-exercises.md)
and
[`exercises/02-full-waveform-inversion-project-solutions.md`](./exercises/02-full-waveform-inversion-project-solutions.md).
The ★★★ item asks for a multiscale schedule derived from the criterion, not a
re-run of the demo.

## Mastery checkpoint

Without notes:

1. Write the discrete forward update and its exact transpose for the adjoint.
2. State the finite-difference gradient test and the two numbers it produces.
3. Compute $T/2$ for a $12\ \mathrm{Hz}$ source and decide whether a start model
   $10\%$ low will converge.
4. State the resolution limit in wavelengths and turn it into metres.
5. Name three things an FWI report must contain that the final image does not show.

## Common pitfalls

1. **Using the continuous adjoint with a discrete forward code.** The gradient is
   then wrong at the $O(\Delta t)$ level; use the exact transpose.
2. **Injecting the data residual with a $\Delta t^2$ factor**, which scales the
   gradient by $10^{-6}$ and makes the inversion look like it is not moving.
3. **Driving the residual towards zero.** Stop at the noise level; below it you are
   fitting noise with structure.
4. **Ignoring the half-period criterion.** Then the failure is blamed on the
   optimiser or the step length.
5. **Publishing structure thinner than half a wavelength.** It cannot be there.

## Where this is used

FWI is the standard high-resolution velocity-estimation tool in exploration
seismology, and its adjoint machinery is the same as that used for
source-inversion, full-waveform ambient-noise tomography and geodynamic adjoint
modelling. The cycle-skipping criterion reappears whenever a nonlinear inversion is
started from a poorly constrained initial model, including the trans-dimensional
problem of [25-05-04](./04-bayesian-inversion-project.md), and the resolution limit
in wavelengths is the same statement as the smoothing length in
[25-05-03](./03-geodynamic-model-data.md).

## Related lessons

- [06-06-05 Adjoint Methods](../../06-seismology/06-seismic-tomography/05-adjoint-methods.md) —
  the derivation and the continuous limit.
- [06-06-07 Tomography Controversies](../../06-seismology/06-seismic-tomography/07-tomography-controversies.md) —
  what goes wrong when these inversions are pushed beyond their resolution.
- [18-03-03 Choosing the Regularisation Parameter](../../18-inverse-problems/03-regularization/03-parameter-choice.md) —
  the same discrepancy argument used here for the stopping rule.
- [25-05-01 Project: Local Earthquake Tomography](./01-tomography-project.md) —
  the travel-time counterpart of this project.

## Self-assessment checklist

- [ ] I can derive and implement the exact discrete adjoint.
- [ ] I can pass a finite-difference gradient test and explain its scope.
- [ ] I can compare the final residual with the noise level, not with zero.
- [ ] I can compute the half-period criterion and predict convergence.
- [ ] I can state the resolution limit in metres and check the image against it.
- [ ] I can name the unconstrained parts of a model from the illumination.
