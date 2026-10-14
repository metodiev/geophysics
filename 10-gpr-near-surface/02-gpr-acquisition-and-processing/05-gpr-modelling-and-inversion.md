---
id: 10-02-05
title: "GPR Modelling and Full-Waveform Inversion"
level: research
prereqs: ["10-02-04", "10-02-03", "18-01-01"]
tags: [gpr, near-surface, modelling, fdtd, full-waveform-inversion, adjoint-state, cycle-skipping, uncertainty]
---

# GPR Modelling and Full-Waveform Inversion

> **All models and data in this module are SYNTHETIC.** The layered model, the
> anomaly, the FDTD grid, the source and the noise level below are chosen
> teaching values. The FDTD schemes are written out in full in the demonstration;
> the numbers quoted are properties of those schemes on those synthetic models.
> No field data, measured velocity or published inversion result is involved.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the convolutional (reflectivity) forward model and **state** which
   physics it omits.
2. **Discretise** the scalar wave equation with a second-order finite-difference
   time-domain (FDTD) scheme, **derive** its stability condition, and **verify**
   a modelled reflection time against an analytic value.
3. **Demonstrate** numerical dispersion with a grid-convergence test rather than
   asserting it.
4. **Derive** the adjoint-state gradient for the scalar wave equation, and
   **verify** it against finite differences — the step that makes an inversion a
   measurement rather than an assertion.
5. **Explain** why the first FWI iteration is a migration image, and **interpret**
   the first gradient of a synthetic model.
6. **Quantify** cycle skipping from the misfit function itself, including the
   position of its first spurious minimum.
7. **Report** an inversion result with its misfit reduction, its failure to
   recover amplitude, and the spread of the answer under noise and different
   starting models.

## Prerequisites

- [10-02-04 3-D GPR Imaging and Time Slices](04-gpr-3d-imaging.md) — the migrated
  image that FWI generalises.
- [10-02-03 Velocity Analysis and Common-Midpoint Sounding](03-gpr-velocity-analysis.md) —
  the starting velocity an inversion needs.
- [18-02-01 Foundations of Inverse Problems](../../18-inverse-problems/01-inverse-problem-foundations/README.md) —
  misfit functions, gradients and ill-posedness.

## 1. Three forward models, and what each is for

GPR interpretation uses three forward models of increasing fidelity and cost.

**The convolutional (reflectivity) model.** A layered medium is represented by a
reflectivity series $r(z)$, and the trace is

$$d(t) = \sum_k R_k\, w\!\left(t - \frac{2z_k}{v}\right), \tag{1.1}$$

with $w$ the source wavelet. It is exact for horizontally layered, non-dispersive
media and for **primary reflections only**: no multiples, no transmission losses,
no geometric spreading and no lateral variation.

**The finite-difference time-domain (FDTD) model.** Discretise the scalar wave
equation

$$\frac{\partial^{2}u}{\partial t^{2}}
= v^{2}\nabla^{2}u + s(\mathbf{x}, t) \tag{1.2}$$

on a grid with $h$ the cell size and $\Delta t$ the time step:

$$u^{m}_{i,j} = 2u^{m-1}_{i,j} - u^{m-2}_{i,j}
+ \left(\frac{v_{i,j}\Delta t}{h}\right)^{2}
L\,u^{m-1}_{i,j} + s^{m}_{i,j}, \tag{1.3}$$

where $L$ is the five-point Laplacian on the interior of the grid (the boundary
values are held at zero here, which is the simplest and least physical choice).
Equation (1.3) carries all the wave physics of the scalar approximation —
multiple scattering, transmission, geometric spreading — but not the vector
nature of the electromagnetic field, not the permittivity–conductivity split, and
not (in this form) attenuation or dispersion.

**The full Maxwell model.** Where the polarisation or the conductivity matters
directly, the vector equations have to be solved. That is beyond this module; the
scalar model here is the standard test bed for GPR inversion, and its limitations
are the subject of Section 7.

## 2. Stability, and the first thing to verify

For the explicit scheme (1.3) with a five-point Laplacian the Courant–Friedrichs–
Lewy (CFL) condition is

$$\Delta t \le \frac{h}{v_{\max}\sqrt{2}}. \tag{2.1}$$

In the demonstration's model ($h = 0.020\ \mathrm{m}$, $v_{\max} = 0.120\
\mathrm{m\,ns^{-1}}$) the limit is $0.1179\ \mathrm{ns}$ and the run uses
$\Delta t = 0.050\ \mathrm{ns}$ — $42\%$ of the limit, chosen so that the
numerical dispersion (Section 3) is tolerable as well as stable.

Stability is necessary but not sufficient. A stable scheme can still be wrong,
and the only way to know is to compare a modelled travel time with an analytic
one.

**Worked example 1 (verification).** A two-layer model with the interface at
$0.40\ \mathrm{m}$ and $v = 0.14\ \mathrm{m\,ns^{-1}}$ below it has a normal-incidence
reflection time from the interface of $2\times0.40/0.10 = 8.00\ \mathrm{ns}$. With
the source and receiver $0.05\ \mathrm{m}$ apart on the surface, the analytic
difference between the reflection and the direct arrival is

$$\frac{2\sqrt{0.40^{2}+0.025^{2}} - 0.05}{0.10} = 7.516\ \mathrm{ns}.$$

The measured difference from the FDTD traces, with the grid refined:

| $h$ (m) | $\Delta t$ (ns) | measured (ns) | analytic (ns) | error (ns) |
|---|---|---|---|---|
| 0.040 | 0.100 | 8.400 | 7.516 | $+0.884$ |
| 0.020 | 0.050 | 7.850 | 7.516 | $+0.334$ |
| 0.010 | 0.025 | 7.725 | 7.516 | $+0.209$ |

The error falls by a factor of about $2.6$ when $h$ is halved, then by $1.6$:
this is **numerical dispersion** of a second-order scheme, plus the effect of the
discrete source. It is not a physics error, and it is *reportable*: a modelling
result quoted without a grid-convergence test has no error bar at all.

## 3. The adjoint: what makes an inversion verifiable

Write the discrete forward problem as a linear system $M(v)\,u = s$. The misfit
is

$$J(v) = \frac{1}{2}\sum_{m}\left(u^{m}_{\text{rec}} - d^{m}\right)^{2}. \tag{3.1}$$

Form the Lagrangian and set its derivative with respect to the field to zero. The
result is the **adjoint equation**

$$M^{T}\lambda = R^{T}r, \qquad r^{m} = u^{m}_{\text{rec}} - d^{m},
\tag{3.2}$$

which for the scheme (1.3) is the *same recursion run backwards in time* with the
residual injected at the receivers. The gradient then follows without any further
derivation:

$$\boxed{\;\frac{\partial J}{\partial v_{i,j}}
= \sum_{m}\frac{2\,v_{i,j}\,\Delta t^{2}}{h^{2}}\,
\lambda^{m}_{i,j}\,\left(L\,u^{m-1}\right)_{i,j}\;} \tag{3.3}$$

— a **zero-lag cross-correlation of the forward field with the adjoint field**.
Two properties of (3.3) are worth naming: it costs one extra wave simulation
regardless of the number of model parameters, and it is the *same* formula that
underlies seismic FWI and travel-time tomography, with different forward
operators.

**Worked example 2 (verification).** The demonstration perturbs ten grid points by
$\pm10^{-5}\ \mathrm{m\,ns^{-1}}$, evaluates the misfit by finite differences,
and compares. For a SYNTHETIC model with a Gaussian anomaly of
$+0.040\ \mathrm{m\,ns^{-1}}$ at $(0.40, 0.32)\ \mathrm{m}$ in a
$0.100\ \mathrm{m\,ns^{-1}}$ background, the two agree with a **maximum relative
difference of $5.5\times10^{-4}$ and a median of $7.4\times10^{-6}$** across the
ten points. The largest disagreement is at the point with the smallest gradient
(the difference is at the level of the finite-difference step), and the median is
five orders of magnitude smaller.

This test is the difference between an inversion and a plausible picture. A
gradient that has not been checked against finite differences on a small problem
is an unverified claim, and a sign error in it produces a model that fits worse
with every iteration.

## 4. Full-waveform inversion: the first iteration is a migration

Substitute the definition of the residual into (3.3) and the structure becomes
transparent. The adjoint field is the back-propagation of the residual, so
$\lambda$ arrives at the anomaly from the receivers along the same paths the data
travelled; the cross-correlation with the forward field is largest where those
paths intersect a scatterer. The first iteration of FWI is therefore a
**migration image**, and its peak locates the scatterer.

**Worked example 3 (measurement).** In the demonstration's SYNTHETIC FWI model
($41 \times 41$ grid at $0.020\ \mathrm{m}$, two sources and eleven receivers on
the surface, an anomaly of $+0.040\ \mathrm{m\,ns^{-1}}$ at $(0.400, 0.320)\
\mathrm{m}$, initial misfit $J = 9.8166$):

- the raw gradient is **largest at the surface**, where the direct wave dominates,
  at $(0.44, 0.12)\ \mathrm{m}$;
- inside the region below the direct-wave footprint ($z > 0.20\ \mathrm{m}$) its
  peak is at $(0.400, 0.320)\ \mathrm{m}$ — **exactly** the anomaly centre, to
  the grid.

So the migration step finds the anomaly, and the *masking* of the near-surface
sensitivity is part of the method, not a cosmetic choice.

Iterating with a normalised steepest-descent direction and a line search over the
step length gives

| iteration | misfit | reduction from the start | recovered peak |
|---|---|---|---|
| 0 | 9.8166 | — | $0.1000\ \mathrm{m\,ns^{-1}}$ |
| 1 | 8.8128 | $-0.47\ \mathrm{dB}$ | $0.1003$ |
| 2 | 7.9111 | $-0.94\ \mathrm{dB}$ | $0.1008$ |
| 3 | 7.6717 | $-1.07\ \mathrm{dB}$ | $0.1010$ |
| 4 | 7.4751 | $-1.18\ \mathrm{dB}$ | $0.1012$ |

After four iterations the recovered peak sits at $(0.40, 0.24)\ \mathrm{m}$ and
amounts to **$3\%$ of the true contrast** ($0.040\ \mathrm{m\,ns^{-1}}$). This is
the shape of a gradient inversion: the lateral position is recovered well, the
amplitude very poorly, and the depth slightly shallow. Four steepest-descent steps
along a normalised direction is a deliberately minimal inversion — the point of
the exercise is that the gradient was *verified* and the answer is reported as it
is, not that the image is good.

## 5. Cycle skipping

FWI minimises a misfit that is a function of the *full waveform*, so it is
sensitive to phase: if the modelled arrival is displaced by more than about half
a period, the difference is dominated by the wrong cycle and the gradient can
push the model further away. The condition is easy to measure.

**Worked example 4 (measurement).** Take a single synthetic reflection and shift
it in time, computing the squared difference from the unshifted trace:

| shift (ns) | misfit (relative to the edge of the search window) |
|---|---|
| $-4.55$ | 0.9137 |
| $0.00$ | 0.0000 |
| $+4.55$ | 0.9137 |

The misfit has a global minimum at zero and its first spurious minima at
$\pm4.55\ \mathrm{ns}$, which is $0.91$ of the dominant period
$1/f_0 = 5.00\ \mathrm{ns}$. The commonly quoted criterion — that a starting model
wrong by more than about **half** a period may land in the neighbouring basin —
is a rule of thumb sitting inside that interval: at $\pm2.5\ \mathrm{ns}$ the two
solutions are already comparable in misfit, and by $\pm4.55\ \mathrm{ns}$ the
shifted trace's own wavelet sits under the original's flank.

The practical consequences are the standard ones: FWI needs low frequencies (which
make the period long and the basin wide), a good starting model (from a CMP
sounding, lesson 02-03), or both. GPR has an advantage here — the wavelengths are
short, so a wavelength-scaled starting-model error is often achievable from
hand-held sounding — and a corresponding disadvantage, because attenuation removes
the low frequencies that make the basin wide.

## 6. Noise, non-uniqueness, and what to report

**Worked example 5 (measurement).** One normalised gradient step with $10\%$
noise on the observed traces and four different draws of a $2\%$ random starting
model gives, **at the fixed anomaly location**:

| run | starting model | value at the anomaly |
|---|---|---|
| 0 | uniform | $0.1010\ \mathrm{m\,ns^{-1}}$ |
| 1 | $2\%$ random | $0.0999$ |
| 2 | $2\%$ random | $0.0972$ |
| 3 | $2\%$ random | $0.1009$ |

a spread of $0.0014\ \mathrm{m\,ns^{-1}}$, i.e. **$3\%$ of the true contrast**.
Two reporting rules follow.

- Quote the value at a **fixed location**, not the global maximum of the model.
  Under noise the global maximum wanders elsewhere entirely (in these runs it
  appears at $(0.24, 0.12)$, $(0.40, 0.48)$, $(0.54, 0.40)$ and $(0.24, 0.06)\
  \mathrm{m}$), and a maximum is not a measurement.
- Quote the **spread over runs**, including different starting models. A single
  run's answer is one sample from a distribution that has been left unexamined.

## 7. Assumptions and regime of validity

1. **The scalar wave equation.** Real GPR is a vector electromagnetic problem.
   The scalar approximation is standard for inversion tests, and it cannot
   distinguish a permittivity change from a conductivity change, nor represent
   polarisation.
2. **Non-dispersive, lossless propagation** in the FDTD scheme of this lesson.
   Adding attenuation is straightforward (a first-derivative term) and changes
   both the amplitudes and the achievable resolution.
3. **The band is finite, so the answer is band-limited.** The recovered model is
   the true model convolved with a resolution kernel; a "velocity" from FWI is a
   smooth average, not a point value.
4. **Dirichlet boundaries.** The box reverberates. In this lesson's tests the
   same operator is used for the data, the gradient verification and the
   inversion, so the tests remain valid; a real survey needs absorbing boundaries
   or a domain large enough that the reverberation arrives after the events of
   interest.
5. **A starting model within half a period.** Section 5 quantifies the failure
   mode when it is not.
6. **The misfit is $L_2$.** A small number of large errors dominate it; robust
   norms change the inversion's behaviour and must be stated.
7. **Two sources and eleven receivers is a test bed.** Nothing here licenses a
   statement about an inversion of a real survey; the geometry is chosen to make
   the gradient verifiable, not realistic.

## 8. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| CFL limit | ns | $h/(v_{\max}\sqrt{2})$ |
| misfit $J$ | (field unit)$^2$ | $1/2\sum r^{2}$ |
| gradient $\partial J/\partial v$ | $\mathrm{(field\ unit)^{2}\,ns\,m^{-1}}$ | (3.3) |
| misfit reduction | dB | $10\log_{10}(J/J_0)$ |
| cycle-skip limit | ns | $\approx 1/(2f_0)$ |

The misfit is *dimensionful*, so its absolute value means nothing: only ratios
(hence the dB in the tables) and the gradient's agreement with finite differences
carry information.

## 9. Python demonstration

`code/gpr_modelling_and_inversion_demo.py` prints everything above and:

1. builds a three-interface convolutional model and verifies picked times against
   the analytic two-way times ($16.00$, $30.00$ and $52.00\ \mathrm{ns}$, all
   exact to the printed digits);
2. verifies an FDTD reflection time against an analytic value and demonstrates
   grid convergence ($+0.884$, $+0.334$ and $+0.209\ \mathrm{ns}$ at
   $h = 0.040$, $0.020$ and $0.010\ \mathrm{m}$);
3. computes the adjoint gradient and validates it against finite differences
   (maximum relative difference $5.5\times10^{-4}$, median $7.4\times10^{-6}$);
4. runs four FWI iterations, reporting the misfit reduction per iteration and the
   recovered peak, and locates the first gradient's peak inside the masked region;
5. measures the misfit-versus-shift function and its first spurious minimum;
6. repeats one inversion step under $10\%$ noise with four starting models and
   reports the spread of the value at a fixed location.

## Mastery checkpoint

Without notes:

> A scalar FDTD model uses $h = 0.025\ \mathrm{m}$, $v_{\max} = 0.13\
> \mathrm{m\,ns^{-1}}$, $f_0 = 250\ \mathrm{MHz}$ and a two-layer interface at
> $0.50\ \mathrm{m}$ depth with $v = 0.09\ \mathrm{m\,ns^{-1}}$ below it.
> **(a)** Compute the CFL limit for $\Delta t$ and state whether
> $\Delta t = 0.060\ \mathrm{ns}$ is stable.
> **(b)** Compute the expected reflection time at normal incidence and state what
> you would compare it with to verify the model.
> **(c)** State the adjoint equation for this scheme and the gradient formula, and
> describe the finite-difference test that would validate them.
> **(d)** A starting model differs from the truth by a uniform $6\ \mathrm{ns}$ in
> travel time. Compute the fraction of a period this represents and state whether
> cycle skipping is a risk.
> **(e)** List three things a scalar inversion of this kind cannot determine.

Parts (a)–(e) are worked in
[`exercises/05-gpr-modelling-and-inversion-solutions.md`](./exercises/05-gpr-modelling-and-inversion-solutions.md).

## Common pitfalls

1. **Quoting a modelled travel time without a grid-convergence test.** Numerical
   dispersion mimics physics.
2. **Running an inversion on an unverified gradient.** A sign error makes every
   iteration worse and looks like "difficult data".
3. **Reporting the global maximum of an inverted model.** Under noise it wanders;
   quote the value at a fixed location with its spread.
4. **Assuming FWI recovers velocity.** It recovers a band-limited, smoothed
   scattering potential within the illumination footprint.
5. **Ignoring cycle skipping** when a starting model is more than about half a
   period off.
6. **Reporting a misfit reduction as a quality measure.** A $1.2\ \mathrm{dB}$
   reduction with the right lateral position and a $3\%$ amplitude is a *result*;
   a larger reduction with the wrong position is not.
7. **Forgetting that the scalar model cannot separate permittivity from
   conductivity.** Two different media can produce the same scalar response.

## Related modules

- [10-02-02 Processing Steps](02-gpr-processing.md) — migration, which is FWI's
  first iteration with a fixed velocity.
- [10-02-04 3-D GPR Imaging and Time Slices](04-gpr-3d-imaging.md) — the imaging
  step before inversion.
- [10-01-01 GPR Physics](../01-gpr-principles/01-gpr-physics.md) — where the
  vector equations this lesson approximates are derived.
- [18-04 Nonlinear Inversion and Optimisation](../../18-inverse-problems/04-nonlinear-inversion/README.md) —
  line searches, step lengths and convergence criteria.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  the systematic treatment of the spread measured in Section 6.
- [05-03-05 Forward-Model Validation](../../05-core-geophysics/03-forward-modelling-principles/05-forward-model-validation.md) —
  the verification discipline applied throughout this lesson.

Materials: [`code/gpr_modelling_and_inversion_demo.py`](./code/gpr_modelling_and_inversion_demo.py),
[`exercises/05-gpr-modelling-and-inversion-exercises.md`](./exercises/05-gpr-modelling-and-inversion-exercises.md),
[`exercises/05-gpr-modelling-and-inversion-solutions.md`](./exercises/05-gpr-modelling-and-inversion-solutions.md).
