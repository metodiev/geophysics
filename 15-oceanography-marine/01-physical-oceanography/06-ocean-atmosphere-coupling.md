---
id: 15-01-06
title: "Ocean-Atmosphere Coupling and ENSO"
level: doctoral
prereqs: ["15-01-02", "15-01-03", "02-06-04"]
tags: [oceanography, marine-geophysics, air-sea-coupling, enso, bulk-formulas, oscillator, spectral-peak]
---

# Ocean-Atmosphere Coupling and ENSO

> **All models and data in this module are SYNTHETIC.** The bulk coefficients and
> the oscillator parameters below are chosen teaching values, printed by the
> demonstration in `code/`. They are not fitted to observations and no
> reanalysis, buoy array, satellite product or real ENSO event is described. The
> physical constants used ($\rho_{\text{air}}$, $c_p$, $L_v$, $\Omega$) are
> standard values with units.

Everything up to this point has treated the atmosphere as a given: a wind stress,
a surface heat flux, a prescribed freshwater flux. **Coupled** behaviour begins
when the ocean's own state changes the forcing. Then a small anomaly can grow
rather than decay, and the question becomes one about a feedback loop.

The phenomenon that motivated this study in the ocean — the quasi-periodic
warming and cooling of the equatorial Pacific and the global weather anomalies
that come with it — is the cleanest example in the Earth sciences of a *coupled
mode*: an oscillation that belongs to neither the ocean nor the atmosphere but to
the pair. It is also a case study in a methodological trap. A coupled mode with a
broad spectral peak can be described as a damped oscillator driven by noise or as
a self-sustained oscillation, and the two descriptions fit the same record. This
lesson builds both and measures what a finite record can and cannot distinguish.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the bulk formulas for wind stress, sensible heat flux and latent
   heat flux, and **compute** each for stated winds and air–sea differences with
   units.
2. **Explain** why the three bulk fluxes are products of three uncertain factors,
   and **quantify** the resulting multiplicative error.
3. **Derive** the eigenvalues of a two-variable recharge oscillator and
   **express** its period, growth rate and damping time in terms of the
   coefficients.
4. **Compute** the critical coupling at which the oscillation ceases to exist and
   the system becomes a pair of real modes, and **state** what changes physically
   across that boundary.
5. **Derive** the steady-state thermocline–SST relation $h = -(\epsilon/r)T$ and
   **state** why it is a model output rather than an observation.
6. **Compute** the response spectrum of the damped oscillator to white-noise
   forcing, and **compare** the analytic spectral peak with the peak of a
   periodogram of a finite record.
7. **Quantify** how well a finite synthetic record determines the period, and
   **state** why a skewness test discriminates linear from nonlinear behaviour.

## Prerequisites

- [15-01-02 Wind-Driven Circulation, Ekman Transport and Gyres](02-wind-driven-circulation.md) —
  the wind stress and its effect on the equatorial ocean.
- [15-01-03 Thermohaline Circulation and Deep Water Formation](03-thermohaline-circulation.md) —
  a two-variable coupled model, and how its stability is classified.
- [02-06-04 Turbulence and Eddy Transport](../../02-physics/06-fluid-mechanics/04-turbulence.md) —
  why a bulk transfer coefficient is a parameterisation and not a constant.

## 1. What "coupled" means

A one-way problem specifies the forcing and predicts the response. A coupled
problem has two conditions:

- the forcing depends on the state of the forced system (**feedback**), and
- the response time of each subsystem is of the same order as the other's
  (**no timescale separation**).

Both hold in the tropical Pacific. The trade winds push warm surface water
westward, which raises the thermocline in the east and lowers it in the west; the
resulting east–west sea-surface temperature contrast drives the winds that
produced it. The loop has a positive feedback (a stronger contrast gives stronger
winds, which strengthen the contrast) and several negative ones (the
thermocline's discharge and the ocean's adjustment by equatorial waves).

The feedback loop's existence is a statement about physics. Its *strength* is a
number, and that number is what an oscillator model estimates.

## 2. Bulk formulas

The surface fluxes are parameterised as

$$\tau = \rho_{\text{air}}C_D|\mathbf{U}|\mathbf{U}, \qquad
H = \rho_{\text{air}}c_pC_H|\mathbf{U}|(T_s - T_a), \qquad
LE = \rho_{\text{air}}L_vC_E|\mathbf{U}|(q_s - q_a),$$

with $\mathbf{U}$ the wind vector at a reference height, $T_s$, $T_a$ the sea and
air temperatures, and $q_s$, $q_a$ the specific humidities. Using

$$\rho_{\text{air}} = 1.225\ \mathrm{kg\,m^{-3}},\quad
c_p = 1005\ \mathrm{J\,kg^{-1}\,K^{-1}},\quad
L_v = 2.501\times10^{6}\ \mathrm{J\,kg^{-1}},$$

and chosen coefficients $C_D = 1.2\times10^{-3}$, $C_H = 1.1\times10^{-3}$,
$C_E = 1.2\times10^{-3}$, the demonstration prints

| $U$ (m s$^{-1}$) | $\tau$ (N m$^{-2}$) | $\Delta T$ (K) | $\Delta q$ (g kg$^{-1}$) | $H$ (W m$^{-2}$) | $LE$ (W m$^{-2}$) |
|---|---|---|---|---|---|
| 2.0 | 0.0059 | $-1.0$ | $-3.0$ | $-2.71$ | $-22.06$ |
| 6.0 | 0.0529 | $-1.0$ | $-3.0$ | $-8.13$ | $-66.18$ |
| 6.0 | 0.0529 | $-3.0$ | $-3.0$ | $-24.38$ | $-66.18$ |
| 12.0 | 0.2117 | $-1.0$ | $-3.0$ | $-16.25$ | $-132.35$ |

Three structural facts follow.

- **Stress is quadratic in wind speed** ($|\mathbf{U}|\mathbf{U}$) while the heat
  fluxes are linear in $|\mathbf{U}|$ times a difference. Doubling the wind
  quadruples the stress but only doubles the fluxes at fixed differences.
- **Every flux is a product of a coefficient, a speed and a difference.** All
  three are uncertain, and they multiply: an independent $20\,\%$ error in each
  gives a factor $1.2^{3} = 1.73$ in the flux. That factor is the honest starting
  point for any coupled heat budget.
- **The latent flux dominates.** For the same conditions $LE$ is $8$ times $H$
  here. Latent heat release is the tropical atmosphere's fuel, which is why a
  small SST anomaly can drive a large atmospheric response.

## 3. The recharge oscillator

### 3.1 The model

Let $T$ be the SST anomaly in the eastern equatorial Pacific (K or $^\circ$C) and
$h$ the equatorial thermocline-depth anomaly (m). The two-variable model is

$$\frac{\mathrm{d}T}{\mathrm{d}t} = R\,T + \gamma\,h + \xi(t),
\qquad
\frac{\mathrm{d}h}{\mathrm{d}t} = -\epsilon\,T - r\,h,$$

with the readings:

- $R>0$: the **Bjerknes feedback** — a warm anomaly strengthens the winds that
  warm it further;
- $\gamma$: the thermocline depth's effect on SST (a deeper thermocline means
  warmer surface water in the east);
- $\epsilon$: the **discharge** — a warm anomaly drives a thermocline response
  that eventually removes the anomaly;
- $r$: the damping of the depth anomaly;
- $\xi$: white noise, standing in for all the weather that the model does not
  represent.

Chosen values: $\gamma = 1.0\ ^\circ\mathrm{C\,(m\,yr)^{-1}}$ and, as Section 4
explains, $\epsilon$ is *solved* so that the damped natural frequency corresponds
to a 4-year period.

### 3.2 Eigenvalues

With $A = \begin{pmatrix} R & \gamma\\ -\epsilon & -r\end{pmatrix}$,

$$\lambda = \frac{\operatorname{tr}A \pm \sqrt{(\operatorname{tr}A)^{2}
- 4\det A}}{2}, \qquad
\operatorname{tr}A = R - r, \qquad
\det A = \gamma\epsilon - Rr .$$

Writing $\lambda = -\beta \pm \mathrm{i}\omega_0$,

$$\beta = \frac{r - R}{2}, \qquad
\omega_0^{2} = \det A - \beta^{2} = \gamma\epsilon - Rr
- \frac{(R-r)^{2}}{4}.$$

An **oscillation** requires $\omega_0^{2}>0$; **growth** requires $\beta<0$;
**decay** requires $\beta>0$. The two conditions are independent, and that
independence is what makes the model a useful teaching device: the period and the
stability are controlled by different combinations of the coefficients.

With $R = 0.5$, $r = 0.5$:

$$\beta = 0, \qquad \omega_0 = \frac{2\pi}{4} = 1.5708\ \mathrm{rad\,yr^{-1}}
\;\Rightarrow\; \epsilon = \frac{\omega_0^{2}+\beta^{2}+Rr}{\gamma}
= \frac{2.4674 + 0.25}{1.0} = 2.7174\ \mathrm{m\,(^\circ C\,yr)^{-1}},$$

eigenvalues $\pm1.5708\mathrm{i}\ \mathrm{yr^{-1}}$: a **neutral oscillation** of
period exactly 4.00 years.

With $R = 0.2$, $r = 1.5$:

$$\beta = 0.65\ \mathrm{yr^{-1}}, \qquad
\epsilon = \frac{2.4674 + 0.4225 + 0.30}{1.0} = 3.1899,$$

eigenvalues $-0.65 \pm 1.5708\mathrm{i}\ \mathrm{yr^{-1}}$: a **decaying
oscillation** with period 4.00 yr and an $e$-folding decay time of
$1/0.65 = 1.54$ yr.

**The period is an input, not a prediction.** $\epsilon$ was solved to produce
it. That must be said out loud, because it changes what the model can be asked:
it can be asked *how sensitive* the behaviour is to the coefficients, not *what*
the period is.

## 4. Growth rate and the critical coupling

Holding $\gamma$, $r$ and $\epsilon$ at the neutral case and varying only $R$:

| $R$ (yr$^{-1}$) | max $\mathrm{Re}\,\lambda$ (yr$^{-1}$) | period (yr) | behaviour |
|---|---|---|---|
| 0.0 | $-0.250$ | 3.856 | decaying oscillation |
| 0.2 | $-0.150$ | 3.900 | decaying oscillation |
| 0.4 | $-0.050$ | 3.962 | decaying oscillation |
| 0.5 | $0.000$ | 4.000 | neutral oscillation |
| 0.6 | $+0.050$ | 4.043 | growing oscillation |
| 0.8 | $+0.150$ | 4.148 | growing oscillation |
| 1.0 | $+0.250$ | 4.280 | growing oscillation |
| 1.5 | $+0.500$ | 4.795 | growing oscillation |

Two features matter. **The growth rate is exactly $\beta = (R-r)/2$** — linear in
the coupling, and independent of the period — so a fit to the growth rate
determines the *difference* $R - r$ and says nothing about either separately.
And **the period lengthens as the coupling grows** (3.86 yr at $R=0$ to 4.80 yr at
$R=1.5$), because raising $R$ steepens the feedback without changing the discharge
coefficient. A model that fits a period can therefore compensate for a wrong $R$
by adjusting $\epsilon$, which is a degeneracy worth knowing about.

For large enough $R$ the oscillation disappears altogether: the discriminant
vanishes when

$$\gamma\epsilon = Rr + \frac{(R-r)^{2}}{4},$$

which with these parameters happens at $R = 2.797\ \mathrm{yr^{-1}}$. Beyond it
the two eigenvalues are real and negative (if $R < r$) or real and positive (if
$R>r$): the system has two **decay modes** or two **growth modes**, and there is
no oscillatory behaviour at all. Crossing this boundary is an example of a
different bifurcation from the saddle-node of
[Lesson 03](03-thermohaline-circulation.md): here two complex eigenvalues collide
on the real axis and separate, rather than two real roots colliding and
disappearing.

## 5. The thermocline–SST relation

At steady state, setting $\mathrm{d}h/\mathrm{d}t = 0$:

$$h = -\frac{\epsilon}{r}T .$$

The neutral case gives $\epsilon/r = 2.7174/0.5 = 5.4348\
\mathrm{m\,^\circ C^{-1}}$; the damped case gives $3.1899/1.5 = 2.1266\ \mathrm{m\,
^\circ C^{-1}}$. **The same oscillation period corresponds to two very different
thermocline responses** — a factor 2.6 — and nothing in the period distinguishes
them.

This ratio is the quantity a real analysis would try to estimate from a
combination of satellite altimetry (thermocline proxy) and SST. It is a single
number standing in for an entire pattern of wind and thermocline response.
Reporting it as "the coupling strength" is a category error: it is the *steady*
balance of a *particular* model.

## 6. Stochastic forcing, and what a finite record can determine

### 6.1 The response spectrum

Add white noise to the $T$ equation only. The transfer function from noise to $T$
is

$$G_0(\omega) = \frac{\mathrm{i}\omega + r}{(\mathrm{i}\omega - R)(\mathrm{i}\omega + r)
+ \gamma\epsilon}, \qquad
S_T(\omega) \propto \frac{\omega^{2} + r^{2}}{\left|(\mathrm{i}\omega - R)
(\mathrm{i}\omega + r) + \gamma\epsilon\right|^{2}},$$

which the demonstration evaluates on a fine frequency grid. The lesson's
expectation — that a damped oscillator's response peak sits away from its natural
frequency — is then **tested, not assumed**:

| $R$ (yr$^{-1}$) | $r$ (yr$^{-1}$) | $\epsilon$ (m ($^\circ$C yr)$^{-1}$) | PSD peak period (yr) | peak / 4.000 yr |
|---|---|---|---|---|
| 0.20 | 0.20 | 2.5074 | 4.0000 | 1.0000 |
| 0.20 | 0.50 | 2.5899 | 3.9852 | 0.9963 |
| 0.20 | 1.00 | 2.8274 | 3.9439 | 0.9860 |
| 0.20 | 1.60 | 3.2774 | 3.9880 | 0.9970 |
| 0.50 | 0.50 | 2.7174 | 4.0000 | 1.0000 |
| 0.80 | 1.60 | 3.9074 | 4.0003 | 1.0001 |

**The measured shift is at most about $1.5\,\%$.** For *this* model the response
peak is an adequate proxy for the deterministic period, and the widely repeated
warning that "the spectral peak of a damped oscillator is not at its natural
frequency" is quantitatively small here. The general statement is real; a number
attached to it is not, and the honest answer is the measured $1.5\,\%$ rather
than a recollection.

### 6.2 A marginally stable oscillator has no stationary distribution

Forcing the *neutral* case ($\beta=0$) with white noise gives a variance that
grows without bound:

| record length (yr) | standard deviation of $T$ ($^\circ$C) |
|---|---|
| 100 | $8.3\times10^{3}$ |
| 200 | $1.0\times10^{8}$ |
| 400 | $2.6\times10^{16}$ |

This is a random walk in amplitude, and it is a property of the MODEL, not of the
ocean. **A linear model intended to oscillate about a bounded state must be
damped or nonlinear.** The damped case is well behaved: over an 800-year
synthetic record the standard deviation of $T$ is $0.509\ ^\circ$C.

### 6.3 How well can a finite record determine the period?

Split the 800-year record into eight independent 100-year segments and measure
the periodogram peak of each:

$$4.167,\ 3.704,\ 4.167,\ 4.762,\ 3.448,\ 3.704,\ 3.448,\ 3.846\ \mathrm{yr}.$$

$$\text{mean} = 3.906\ \mathrm{yr}, \qquad
\text{standard deviation} = 0.443\ \mathrm{yr}, \qquad
\text{range} = 3.448 - 4.762\ \mathrm{yr}.$$

The scatter is $\pm11\,\%$ about the deterministic 4.000-yr period, and the mean
of the eight finite-record peaks (3.906 yr) sits within one standard deviation of
the analytic continuous-model peak (3.969 yr). The response is **broad** — the
quality factor is $\omega_0/2|\beta| = 1.208$ — so the peak is a poor estimator.
A single record cannot do better, and this is why published "ENSO periods" differ
by years: they are estimates of the peak of a broad spectrum from records of
finite length.

### 6.4 Skewness, and the limit of a linear model

The synthetic index has a skewness of $+0.046$: sampling scatter about zero. **A
linear model forced by symmetric Gaussian noise produces a symmetric
distribution**, so it cannot reproduce the asymmetry that a real ENSO index shows.
Reproducing that skew requires nonlinearity — a state-dependent $\gamma$, a
threshold, or an amplitude-dependent damping — and the skewness of an index is
therefore a test that a linear model fails by construction. Recognising which
features a model *cannot* produce is as useful as fitting the features it can.

## 7. Assumptions and regime of validity

1. **Two variables for a basin-scale, three-dimensional phenomenon.** $T$ and $h$
   are indices, not fields. The model has no geography and no spatial structure.
2. **Linear dynamics.** The Bjerknes feedback is linearised; the real one
   saturates, and saturation is what bounds the amplitude in a self-sustained
   regime. A growing linear mode is a statement that the model is being used
   outside its regime.
3. **The period is imposed.** $\epsilon$ was solved to produce 4 yr. The model
   therefore cannot be said to "predict" the period of anything.
4. **White noise.** Real atmospheric forcing has a red spectrum with its own
   timescales; substituting white noise changes the shape of the response
   spectrum, though not the eigenfrequencies.
5. **Constant coefficients.** A seasonal cycle in the coupling (real, and
   important) is omitted. So is the annual cycle in the background state.
6. **Bulk coefficients constant.** Section 2: they multiply into every flux, and
   their uncertainty is a factor of order $1.7$ in the flux.
7. **Only one variable is forced.** Noise enters the $T$ equation only; forcing
   both changes the spectrum's shape.

## 8. Worked examples

### Example 1 — the wind stress and its error

For $U = 8.0\ \mathrm{m\,s^{-1}}$:

$$\tau = 1.225 \times 1.2\times10^{-3} \times 8.0 \times 8.0
= 0.0941\ \mathrm{N\,m^{-2}} .$$

If $C_D$ is uncertain by $15\,\%$ and $U$ by $5\,\%$, the stress is uncertain by
approximately $\sqrt{0.15^{2} + (2\times0.05)^{2}} = \sqrt{0.0225+0.01} = 0.180$,
i.e. **$18\,\%$**. The wind enters squared, so its relative error is doubled
before combination — a general rule for power laws that is worth applying to every
quadratic parameterisation in geophysics.

### Example 2 — reading the eigenvalue formula

Take $R = 0.6$, $r = 0.5$, $\epsilon = 2.7174$, $\gamma = 1.0$.

$$\operatorname{tr}A = 0.1, \qquad \det A = 2.7174 - 0.3 = 2.4174,$$

$$\lambda = \frac{0.1 \pm \sqrt{0.01 - 9.6696}}{2}
= \frac{0.1 \pm 3.1090\mathrm{i}}{2} = 0.05 \pm 1.5545\mathrm{i}\ \mathrm{yr^{-1}},$$

period $2\pi/1.5545 = 4.043$ yr, growth rate $+0.05\ \mathrm{yr^{-1}}$
($e$-folding time 20 yr). Compare with the demonstration's table row for
$R=0.6$: growth $+0.050$, period 4.043 yr. ✔

### Example 3 — the critical coupling by hand

Solve $\gamma\epsilon = Rr + (R-r)^{2}/4$ with $\gamma = 1$, $\epsilon = 2.7174$,
$r = 0.5$:

$$2.7174 = 0.5R + \frac{(R-0.5)^{2}}{4}
= 0.5R + \frac{R^{2} - R + 0.25}{4}
= 0.25R^{2} + 0.25R + 0.0625 .$$

So $0.25R^{2} + 0.25R - 2.6549 = 0$, i.e. $R^{2} + R - 10.6196 = 0$:

$$R = \frac{-1 \pm \sqrt{1 + 42.4784}}{2} = \frac{-1 \pm 6.5953}{2}
\;\Rightarrow\; R = 2.7976\ \mathrm{yr^{-1}},$$

against the demonstration's bisection result $2.7969$. The remaining difference is
the coarseness of the arithmetic here (five significant figures on $\epsilon$).

## 9. Python demonstration

`code/ocean_atmosphere_coupling_demo.py` prints all the above with units:

1. the three bulk formulas over a table of winds and differences;
2. the two oscillator cases, with $\epsilon$ solved for the target period, and the
   PSD peak period — the test of a standard expectation, reported as measured;
3. the growth-rate scan and the critical coupling by bisection;
4. the thermocline–SST ratio for both cases;
5. a stochastic integration: the unbounded variance of the neutral case, and the
   eight-segment periodogram scatter of the damped case ($\pm11\,\%$);
6. verification: eigenvalues against a zero-crossing measurement of an integrated
   trajectory (relative difference $2.2\times10^{-16}$), the analytic spectrum
   against the periodogram peak, and dimensional checks on both equations.

Run it with

```bash
cd 15-oceanography-marine/01-physical-oceanography/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ocean_atmosphere_coupling_demo.py
```

Print-only, no network, fixed seed `np.random.default_rng(20261014)`, exit 0, in
about half a second.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/06-ocean-atmosphere-coupling-exercises.md`](exercises/06-ocean-atmosphere-coupling-exercises.md)
and
[`exercises/06-ocean-atmosphere-coupling-solutions.md`](exercises/06-ocean-atmosphere-coupling-solutions.md).

- ★ Compute $\tau$, $H$ and $LE$ for $U = 4\ \mathrm{m\,s^{-1}}$,
  $\Delta T = -2$ K, $\Delta q = -4\ \mathrm{g\,kg^{-1}}$.
- ★★ Compute the eigenvalues, period and growth rate for $R = 0.8$,
  $r = 0.6$, $\gamma = 1.0$, $\epsilon = 2.9$.
- ★★ Derive the critical-coupling condition and solve it for $r = 0.8$.
- ★★★ Design a test that would distinguish "damped oscillator driven by noise"
  from "self-sustained oscillation", and state which of the two the demonstration's
  statistical diagnostics can and cannot separate.

## Mastery checkpoint

Without notes, and showing your arithmetic. Use $\gamma = 1.0\
^\circ\mathrm{C\,(m\,yr)^{-1}}$, $\rho_{\text{air}} = 1.225\
\mathrm{kg\,m^{-3}}$, $c_p = 1005\ \mathrm{J\,kg^{-1}\,K^{-1}}$,
$L_v = 2.501\times10^{6}\ \mathrm{J\,kg^{-1}}$, $C_D = 1.2\times10^{-3}$,
$C_H = 1.1\times10^{-3}$, $C_E = 1.2\times10^{-3}$.

> **(a)** For $U = 10\ \mathrm{m\,s^{-1}}$, $\Delta T = -1.5$ K and
> $\Delta q = -2.5\ \mathrm{g\,kg^{-1}}$, compute $\tau$, $H$ and $LE$ with units,
> and state which of the three is largest in magnitude.
> **(b)** For $R = 0.4\ \mathrm{yr^{-1}}$, $r = 0.9\ \mathrm{yr^{-1}}$,
> $\epsilon = 3.0\ \mathrm{m\,(^\circ C\,yr)^{-1}}$, compute $\operatorname{tr}A$,
> $\det A$, the eigenvalues, the period and the $e$-folding time. State whether
> the mode grows or decays.
> **(c)** Compute the steady thermocline–SST ratio $\epsilon/r$ and state in one
> sentence why it is not an observation.
> **(d)** The response spectrum peaks at essentially the deterministic period for
> every damping parameter tested (within $1.5\,\%$), yet eight 100-year segments of
> one record give peaks spanning 3.45–4.76 yr. Reconcile these two statements.

A worked version of (a)–(d) is in the lesson-06
[solutions](exercises/06-ocean-atmosphere-coupling-solutions.md).

## Common pitfalls

1. **Treating a bulk coefficient as known.** Section 2: the flux is a triple
   product, and three $20\,\%$ errors compound to $73\,\%$.
2. **Forgetting that the wind enters the stress quadratically.** An $x\,\%$ wind
   error is a $2x\,\%$ stress error.
3. **Believing a model that "predicts" an imposed period.** $\epsilon$ was solved
   to give 4 years; the period is an input.
4. **Reading a spectral peak as an eigenfrequency.** For this model they agree to
   $1.5\,\%$; for a broader response they would not, and in either case a
   finite-record peak scatters by $11\,\%$.
5. **Forcing a marginally stable linear oscillator and expecting a bounded
   response.** The variance grows without bound (Section 6.2); a bounded
   oscillation needs damping or nonlinearity.
6. **Using skewness as evidence for a mechanism.** A linear model cannot produce
   skew, so a skew test can *reject* linearity; it cannot confirm any particular
   nonlinearity.
7. **Quoting $\epsilon/r$ as a coupling constant.** It is the steady ratio of one
   model's two variables and it differs by a factor 2.6 between two cases with the
   same period.

## Related modules

- [15-01-02 Wind-Driven Circulation, Ekman Transport and Gyres](02-wind-driven-circulation.md) —
  the trade winds that the model's feedback modifies.
- [15-01-03 Thermohaline Circulation and Deep Water Formation](03-thermohaline-circulation.md) —
  the other coupled oscillation in this folder, analysed the same way.
- [15-01-04 Internal Waves, Tides and Mixing](04-internal-waves-and-tides.md) —
  the ocean's internal adjustment timescales, which set the model's parameters.
- [Module 15-06 Sea Level Change and Marine Records](../06-sea-level-change-marine/README.md) —
  another long-record estimation problem with the same statistical limits.
- [16-04-04 Natural Variability and Internal Modes](../../16-atmosphere-climate/04-climate-system-and-feedbacks/04-natural-variability.md) —
  the atmospheric side, and how coupled modes are separated from forced change.
- [21-07-03 Spectral Analysis and Statistical Inference](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/03-spectral-analysis-statistical.md) —
  the statistical machinery behind Section 6.3.

## Self-assessment checklist

- [ ] I can write and evaluate the three bulk formulas with units.
- [ ] I can derive the eigenvalues of the recharge oscillator.
- [ ] I can compute the critical coupling and say what changes across it.
- [ ] I can derive the steady thermocline–SST ratio and say what it is not.
- [ ] I can compute the response spectrum and compare it with a periodogram.
- [ ] I can quantify how well a finite record determines a broad spectral peak.
- [ ] I can say which feature of an index a linear model cannot reproduce.
