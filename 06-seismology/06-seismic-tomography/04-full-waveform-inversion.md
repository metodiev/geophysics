---
id: 06-06-04
title: "Full-Waveform Inversion: Objective Functions and Reliability"
level: research
prereqs: ["06-06-02", "06-06-03", "03-12-02"]
tags: [seismology, full-waveform-inversion, cycle-skipping, objective-functions, wave-modelling]
---

# Full-Waveform Inversion: Objective Functions and Reliability

All models and data in this module are **SYNTHETIC**. Every number below is
printed by `code/full_waveform_inversion_demo.py`: a one-dimensional
finite-difference experiment on 600 nodes with 10 m spacing (6 km), velocity
2000 / 2600 / 3200 m/s with interfaces at 1.0 km and 2.0 km, a Ricker source of
dominant frequency 20 Hz (peak delay 60 ms), a coincident source-receiver pair
20 m below the free surface, and an absorbing taper at the base. Vertical
incidence is exactly what a one-dimensional model describes, so each number can
be checked by hand.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the forward problem of waveform inversion as a wave equation whose
   coefficient is the model, and **identify** the three places where its
   numerical solution can fail.
2. **Verify** a finite-difference scheme by measuring its stability limit, its
   grid convergence and the arrival times of its reflections against $2z/c$.
3. **Quantify** cycle skipping: count the local minima of a misfit as a function
   of one model parameter, and **measure** the width of the basin around the true
   answer against the frequency band.
4. **Demonstrate** frequency continuation, and **explain** why a smaller final
   misfit can correspond to a worse model.
5. **Compare** least-squares and cross-correlation objective functions in both
   their landscapes and their amplitude sensitivity.
6. **Diagnose** the depth–velocity trade-off and **state** what breaks it.
7. **Interpret** a final misfit against the noise level, and **decide** whether
   an inversion has overfitted.

## Prerequisites

- [02 Travel-Time Tomography](02-travel-time-tomography.md) — parametrisation,
  damping and iteration.
- [03 Resolution, Null Space and Model Covariance](03-resolution-and-nullspace.md) —
  what a small misfit does and does not mean.
- [03-12-02 Stability and the CFL Condition](../../03-scientific-computing/12-numerical-simulation-python/02-stability-and-cfl.md) —
  the numerical condition that governs any explicit solver.

## 1. The forward problem, and the wave equation as a constraint

Full-waveform inversion (FWI) in its simplest form minimises the difference
between observed and synthetic seismograms,

$$
J(\mathbf{m}) \;=\; \tfrac{1}{2}\sum_r \int \bigl[u_r(\mathbf{x},t;\mathbf{m})
- d_r(\mathbf{x},t)\bigr]^2 \,\mathrm{d}t ,
\tag{1}
$$

where $u_r$ solves the wave equation with coefficients $\mathbf{m}$ — for a
constant-density acoustic medium,

$$
m(\mathbf{x})\,\partial_t^2 u - \nabla^2 u = f(\mathbf{x},t),
\qquad m = v^{-2}.
\tag{2}
$$

Three differences from travel-time tomography deserve to be stated at the start.

1. **No picking.** $J$ uses the whole seismogram, so the finite-frequency
   content, the amplitudes and the coda all carry information.
2. **The linearity is in the wrong place.** If the model is $m = v^{-2}$, the
   *field* is linear in $m$ for a fixed source; the difficulty is not the
   physics but the geometry of $J$ as a function of $\mathbf{m}$.
3. **The cost is a PDE solve per evaluation.** Section 4 of lesson 06-06-05
   computes the gradient so that a solve of the *adjoint* equation is all that a
   descent step costs.

For a numerically honest discussion of reliability, the scheme itself has to be
verified first.

## 2. Verifying the scheme before trusting the misfit

The demonstration uses the standard three-point explicit scheme for (2),

$$
u_i^{n+1} = 2u_i^{n} - u_i^{n-1} + \left(\frac{c_i\,\Delta t}{\Delta x}\right)^{2}
\bigl(u_{i+1}^{n} - 2u_i^{n} + u_{i-1}^{n}\bigr) + \Delta t^2 s_i^{n},
\tag{3}
$$

with $c\,\Delta t/\Delta x \le 1$ required for stability, a Dirichlet condition at
the free surface, and a damping taper at the base. Measured:

| test | result |
|---|---|
| CFL $= 0.50$ | max$\lvert u\rvert$ growth over the record: $1.000$ |
| CFL $= 0.90$ | $1.000$ |
| CFL $= 1.02$ | $4.602\times10^{8}$ (blow-up) |
| refinement, $\Delta x$ and $\Delta t$ halved at CFL 0.80 | reflected-field travel time changes by $+12.50$ ms |
| predicted two-way times $2z/c$ | $1.000$ s and $1.769$ s |
| largest peaks of the reflected field | $1.105$, $1.880$, $2.115$ s |
| peak separation against prediction | $0.775$ s against $0.769$ s, i.e. $+6$ ms |

Two remarks that matter later. The $12.5$ ms grid error is the resolution of the
scheme itself on this model: it is why two inversions, or an inversion and its
data, must use the same grid and time step. And the agreement of the *separation*
of the two primary reflections with $2z/c$ is the check that source, free
surface, absorbing taper and interfaces are all implemented consistently — with
two events you can measure a difference, which cancels the wavelet delay that a
single pick cannot.

## 3. Cycle skipping, measured

Take the model family $c_\alpha(z) = c_{\text{true}}\bigl(z(1+\alpha)\bigr)$: a
depth stretch that scales every arrival time by $1/(1+\alpha)$ and leaves every
reflection coefficient unchanged. A forecast is the natural statement of the
problem: a uniform change of arrival time by $\Delta t$ moves the seismogram by
one period whenever $\Delta t = 1/f$, so the misfit acquires a chain of local
minima whose spacing is set by the band.

| band (Hz) | local minima in $\alpha\in[-0.35,0.35]$ | first secondary minimum | shift (ms) | $1/(2f)$ (ms) |
|---|---|---|---|---|
| 8 | 15 | $+0.130$ | 115.0 | 62.5 |
| 16 | 42 | $+0.068$ | 63.2 | 31.2 |
| 32 | 47 | $+0.028$ | 26.8 | 15.6 |

The basin around the true answer is about **one period** wide and halves every
time the band doubles. A local optimiser started more than that far away — in
time — lands in a neighbouring minimum and returns a model that fits the data
badly *and* wrongly. Cycle skipping is therefore a property of the objective
function and the frequency band, not a defect of the optimiser.

## 4. Frequency continuation

Start from $\alpha = +0.050$, i.e. a 5 per cent depth stretch that moves the
first arrival by 48 ms, and let the same "nearest local minimum" descent act:

| strategy | final $\alpha$ | arrival error (ms) | misfit ($\mathrm{s^2}$) |
|---|---|---|---|
| 32 Hz from the start | $+0.0475$ | 45.3 | $2.917\times10^{2}$ |
| 16 Hz from the start | $+0.0675$ | 63.2 | $5.971\times10^{1}$ |
| 8 Hz, then 16, then 32 Hz | $0.0000$ | 0.0 | $0.000$ |

The starting model's misfit at 32 Hz is $5.388\times10^{2}$.
**Continuation is not a way of making the optimiser converge to a small misfit**:
the naive 32 Hz run reduces the misfit by 46 per cent and the error by 6 per
cent. It is the only way to expose the long-wavelength part of the model before a
short-wavelength band can be fitted wrongly — which is exactly the mechanism
section 3 quantified.

### Worked example — is the starting model one period away?

The starting model is 48 ms off in arrival time. Convert that to periods:
$48/125 = 0.38$ at 8 Hz, $48/62.5 = 0.77$ at 16 Hz, and $48/31.2 = 1.54$ at
32 Hz, using the measured periods $1/f_c$. Cycle skipping begins when the
starting error exceeds about one basin half-width, and the measured basin
half-widths are 115, 63 and 27 ms. So:

- at 8 Hz the start is inside a third of a basin: local descent can reach the
  truth;
- at 16 Hz it is at 0.77 of a basin — marginal, and the demonstration confirms a
  failure (final $\alpha = +0.0675$, a 63 ms error);
- at 32 Hz it is 1.54 basins away, i.e. there is at least one intervening local
  minimum between the start and the truth: the descent stops at the nearer one
  (final $\alpha = +0.0475$).

The arithmetic also predicts the *order* of the sequence: to be safe at 32 Hz the
model must be within 27 ms, so bands must be visited in ascending order, and the
test for advancing is exactly "is the current model within half a basin of the
next band".


## 5. The objective function is a choice

The same landscape at 16 Hz, evaluated two ways:

| objective | local minima | value at $\alpha=-0.35$ |
|---|---|---|
| least squares | 81 | $1.2162\times10^{2}$ |
| normalised cross-correlation | 63 | $1.8692\times10^{-2}$ |

and the amplitude behaviour of the same two objectives at the true times:

| model | least squares | cross-correlation |
|---|---|---|
| true model | $0.0$ | $-2.2\times10^{-16}$ |
| 30 per cent louder | $1.4824\times10^{2}$ | $1.4071\times10^{-2}$ |

Cross-correlation is nearly blind to a 30 per cent amplitude error. That is
exactly why it is used on data whose amplitudes are unreliable (unknown source
coupling, attenuation, three-dimensional scattering) and exactly why an inversion
run with it cannot be used to interpret amplitudes. The number of local minima
differs too — 63 against 81 — so the choice changes both the landscape and the
answer. It belongs in the text, not in the code.

## 6. What breaks the depth–velocity trade-off, and what does not

Data from a two-layer model: $2000\ \mathrm{m\,s^{-1}}$ above 1 km,
$2600\ \mathrm{m\,s^{-1}}$ below, reflection coefficient
$R = 600/4600 = 0.130$. Consider the family that preserves **both** the two-way
time $2d_1/c_1 = 1.00$ s **and** $R$:

| $d_1$ (m) | $c_1$ (m/s) | $c_2$ (m/s) | misfit ($\mathrm{s^2}$) | residual / trace rms |
|---|---|---|---|---|
| 700 | 1400 | 1820 | $4.07\times10^{1}$ | 1.000 |
| 850 | 1700 | 2210 | $8.12\times10^{1}$ | 1.412 |
| 1000 | 2000 | 2600 | $1.4\times10^{-26}$ | 0.000 |
| 1150 | 2300 | 2990 | $7.86\times10^{1}$ | 1.390 |
| 1300 | 2600 | 3380 | $4.16\times10^{1}$ | 1.011 |

Only the true depth fits. The layers with the same travel time and the same
reflection coefficient produce different wavefields because the *impedance*
differs, and the recorded amplitude scales with it. A model that gets the time
wrong by 10 per cent is worse still (residual/rms 2.03).

The consequence is double-edged. Waveform inversion can separate depth from
velocity where travel times cannot — but only through **amplitude** information,
which is the least reliable part of a real seismogram: source coupling,
attenuation, scattering out of the two-dimensional plane, and instrument
response all enter the amplitudes. This is why careful FWI practitioners invert
amplitudes with a stated data weighting, why correlation-based and
envelope-based objectives exist, and why a joint inversion with a data type whose
amplitudes are understood (surface waves, gravity) is often preferred.

## 7. Noise, and reading a final misfit

Add Gaussian noise at three signal-to-noise ratios and run the same one-parameter
localisation, 20 realisations each:

| SNR | noise rms | mean $\alpha$ | std of $\alpha$ | misfit / expected |
|---|---|---|---|---|
| 20 | $1.534\times10^{-1}$ | $0.00000$ | $0.00000$ | 1.130 |
| 8 | $3.836\times10^{-1}$ | $-0.00003$ | $0.00011$ | 1.082 |
| 3 | $1.023\times10^{0}$ | $-0.00008$ | $0.00044$ | 1.167 |

"misfit / expected" divides the final misfit by what pure noise would produce over
the *same samples* and the *same band*. The three values near one mean the
inversion stopped at the noise level — as it should. But that verdict depends
entirely on the normalisation, which is the point of the next table:

| normalisation of the same residual | value |
|---|---|
| whole record, full band | 0.065 |
| window, full band | 0.075 |
| window, band-limited to 16 Hz | 1.122 |

Only 26 per cent of the noise survives the 16 Hz low-pass, and the window holds
680 of the 1040 samples. The same residual is a clean fit to noise or a gross
overfitting depending on which number is quoted. **An inversion that reports a
final misfit without saying which samples and which band it was computed over has
reported a number, not a result.** At SNR 3 the recovered stretch moves by less
than $10^{-4}$, because a depth stretch is a long-wavelength parameter and those
survive noise far better than the cell-by-cell models of lesson 06-06-03.

## 8. Assumptions and regime of validity

1. **Acoustic, constant density, one dimension.** Real FWI is elastic and
   three-dimensional; the reliability arguments here (cycle skipping, objective
   choice, noise interpretation) are unaffected, the numerical cost is.
2. **A known source wavelet.** In practice it is estimated, often jointly, and
   source–model trade-offs are among the hardest practical problems.
3. **A known starting model.** Section 4 shows what happens without one; in
   practice the starting model comes from travel-time tomography, which is what
   makes those lessons prerequisites.
4. **Explicit time stepping.** Stability requires CFL $\le 1$ and accuracy
   requires several points per wavelength; both are measured here.
5. **Gaussian noise added to the observed trace.** Real noise is coloured,
   correlated between traces and often non-Gaussian; the convergence of the
   misfit ratio to one is then a modelling statement, not a fact.
6. **No attenuation.** Discarding attenuation discards the amplitude information
   that section 6 identifies as the only thing breaking the depth–velocity
   trade-off.

## 9. Demonstration

[`code/full_waveform_inversion_demo.py`](code/full_waveform_inversion_demo.py)
reproduces every table above. Exercises and worked solutions:
[`exercises/04-full-waveform-inversion-exercises.md`](exercises/04-full-waveform-inversion-exercises.md)
and
[`exercises/04-full-waveform-inversion-solutions.md`](exercises/04-full-waveform-inversion-solutions.md).

## Mastery checkpoint

> A 20 Hz band gives a basin half-width of 27 ms in arrival time; the starting
> model is 48 ms off. **(a)** Predict the outcome of a local inversion performed
> at 20 Hz and say what number you would report to justify the prediction.
> **(b)** Design a frequency-continuation sequence for a 2-60 Hz data set whose
> starting model may be up to 0.5 s off, and state the criterion for moving to
> the next band. **(c)** The final misfit is $0.05$ times the expected noise
> level computed over the full record. Explain why that is not evidence of
> success, and say what you would compute instead. **(d)** State the one
> measurement that can separate a 1.0 km interface at 2000 m/s from a 1.3 km
> interface at 2600 m/s in this geometry, and explain why it is fragile.

## Common pitfalls

1. **Trusting a small final misfit.** Frequency continuation reached misfit
   $0.000$; the naive 32 Hz run reached $2.9\times10^{2}$ and a *worse* model
   than a band below it.
2. **Choosing the band by what the data "look like".** The basin width is set by
   the band, and the band must be wide enough to see the starting-model error.
3. **Comparing misfits computed over different windows or bands.** Measured: the
   same residual gives 0.065 or 1.122 depending on the normalisation.
4. **Believing amplitudes.** They carry the information that breaks the
   depth–velocity trade-off and they are the least reliable part of the data.
5. **Ignoring the numerical scheme.** A CFL of 1.02 produced a
   $4.6\times10^{8}$ growth, and halving the grid moved arrival times by 12.5 ms.
6. **Assuming a finer grid is a better experiment.** Same point as lesson
   06-06-02, now for the wavefield: accuracy is a convergence property, and it
   must be measured rather than assumed.

## Related modules

- [05 The Adjoint Method](05-adjoint-methods.md) — how the gradient of the misfit
  in (1) is computed for a large model.
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) — the
  same wave equation, a controlled source, and the processing that comes before
  inversion.
- [06-08 Receiver Functions and Crustal Structure](../08-receiver-functions-and-crustal-structure/README.md) —
  waveform deconvolution, where the same conditioning problems appear.
- [03-12 Building Numerical Simulation Code in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md) —
  verification, stability and convergence in general.
