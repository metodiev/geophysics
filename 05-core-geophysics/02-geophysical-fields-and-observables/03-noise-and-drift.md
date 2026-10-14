---
id: 05-02-03
title: "Noise, Drift, Tides and Instrument Bias in Field Data"
level: advanced
prereqs: ["05-02-02"]
tags: [noise, drift, tides, instrument-bias, qc]
---

# Noise, Drift, Tides and Instrument Bias in Field Data

## Learning objectives

1. **Separate** four distinct error sources — random readout noise, instrument
   drift, Earth tides, and bias — and explain how each is recognised in data.
2. **Apply** base-station repeat tying and state what it can and cannot remove.
3. **Quantify** a noise budget and decide how much of it a survey can tolerate.
4. **Explain** why a bias is undetectable by repetition within one survey.
5. **Design** a QC loop that would reveal each error source.

## Prerequisites

- [05-02-02 Units and Conventions](./02-field-measurement-units.md)

## 1. Intuition

A field reading is a difference between what the instrument now reads and what
it read at a reference station. Everything that changes between the two
moments — the instrument's own elastic creep, the Earth's body tide, the
operator's handling — is folded into that difference. Correction is possible
only because the unwanted signals have different *structure* from the target:
drift is slow and monotonic, tides are periodic and predictable, noise is
uncorrelated, and bias is constant.

## 2. Precise definitions

**Random noise (precision).** Short-period, uncorrelated scatter. Reduced by
averaging: $\sigma_\text{mean} = \sigma/\sqrt{N}$ for $N$ independent samples.

**Drift.** A slow, usually monotonic change in the instrument's zero, caused by
elastic creep in a spring, thermal expansion, or electronic offset. Removed by
re-occupying a base station and assuming linearity between occupations.

**Tide.** The time-variable component of the gravity field caused by the
relative motion of Sun, Moon and Earth (and the solid-Earth response). It is
*predictable* from an ephemeris and is a signal, not noise — it must be modelled
and removed.

**Bias (accuracy).** A constant offset or scale error. Repetition within the
survey cannot detect it, because every station shares it. Only an absolute
reference (a calibration range, an absolute gravimeter, a known station)
reveals it.

**Tie.** The operation of re-occupying a station, allowing drift to be
interpolated.

## 3. Derivation: what base-station tying removes

Model the reading at station $i$ at time $t_i$ as

$$r_i = g_i + \beta(t_i) + \tau(t_i) + \epsilon_i,$$

where $g_i$ is the true gravity, $\beta$ the drift, $\tau$ the tide and
$\epsilon_i$ the random noise. Repeat the base at times $t_a$ and $t_b$, with
true value $g_b$ known:

$$\beta(t_b) - \beta(t_a) = [r_b(t_b)-r_a(t_a)] - [\tau(t_b)-\tau(t_a)] -
(\epsilon_b-\epsilon_a).$$

Interpolating linearly gives $\hat\beta(t)$ for all $t$, and

$$\hat g_i = r_i - \hat\beta(t_i) - \tau(t_i) = g_i + (\beta-\hat\beta)(t_i) +
(\epsilon_i - \text{interpolated noise}).$$

The residual contains the *non-linearity* of the drift plus a noise contribution
that is $(1+\text{weight})$ times the individual noise. Units: everything in
mGal. Dimensional check is trivial here; the useful check is *magnitude* — is
$\beta-\hat\beta$ smaller than the target anomaly?

### 3.1 The residual variance after base-station tying, derived

Section 3 showed *what* tying removes. Now compute *how much noise it adds*,
because that sets the effective precision of a survey.

Model the drift between two successive base occupations as a straight line
interpolated from the two tied values $y_1$ and $y_2$, each with variance
$\sigma_b^2$. At a fraction $t\in[0,1]$ along the interval the interpolated drift
is $(1-t)y_1 + ty_2$, whose variance is

$$\operatorname{Var}\!\left[(1-t)y_1+ty_2\right]
= \left[(1-t)^2+t^2\right]\sigma_b^2$$

using independence of the two ties. A station reading has variance $\sigma^2$,
and its drift-corrected value is the difference of the two, so

$$\boxed{\;\sigma^2_\text{corrected} = \sigma^2
+ \left[(1-t)^2+t^2\right]\sigma_b^2\;}$$

The bracket $f(t) = (1-t)^2+t^2$ equals 1 at the ties and falls to $1/2$ at the
midpoint:

| position in the tie interval | $f(t)$ | $\sigma_\text{corrected}$, $\sigma = \sigma_b = 0.02$ mGal |
|---|---|---|
| at a tie | 1.000 | 0.02828 mGal |
| quarter interval | 0.625 | 0.02646 mGal |
| midpoint | 0.500 | 0.02449 mGal |

**Physical interpretation.** Tying is not free. It converts an unbounded drifting
error into a bounded one, at the price of a contribution between 0.5 and 1 times
the base-station noise variance. For equal station and base noise the effective
precision is degraded by 22% to 41% relative to the raw repeatability, so a
gravimeter quoted at 0.02 mGal delivers roughly 0.024–0.028 mGal of *survey*
precision in a tied loop. **A repeatability quoted without the tie interval is
incomplete**, and this formula says how to complete it. Because $f$ is smallest
at midpoints, accuracy is worst nearest the ties — a small free advantage to a
survey whose target sits mid-interval.

### 3.2 Residual drift after tying: the $\tau^2$ law

Real drift is not exactly linear. Suppose it has a quadratic component
$\beta(t) = c\,t^2$. Between ties at $t = 0$ and $t = \tau$, linear interpolation
gives $L(t) = c\tau\,t$, so the residual is

$$r(t) = \beta(t) - L(t) = c\,t^2 - c\tau t = c\,t(t-\tau),$$

extremal at $t = \tau/2$ with

$$|r|_{\max} = \frac{c\,\tau^2}{4} .$$

**The $\tau^2$ law is the whole point:** halving the tie interval quarters the
residual drift. **Worked arithmetic** for a total quadratic drift of 0.02 mGal
over a 4-hour day ($c = 0.02/16 = 1.25\times10^{-3}$ mGal/h²):

| tie interval $\tau$ | $\lvert r\rvert_{\max}$ |
|---|---|
| 1.0 h | 0.000313 mGal |
| 1.5 h | 0.000703 mGal |
| 2.0 h | 0.001250 mGal |

All are far below a 0.02 mGal reading noise, so a 2-hour tie interval is more
than adequate *for this drift curvature* — a calculation rather than a habit.
The mismatch scales as the square of the interval because a parabola is the first
function a straight line cannot follow; the same $\tau^2$ governs trapezoidal
quadrature error and every piecewise-linear approximation of a smooth function.

### 3.3 Correlated noise does not average as $\sqrt{N}$

The $\sigma/\sqrt{N}$ rule requires *independent* samples, and field noise rarely
is: microseism, instrument hysteresis and cultural vibration all have finite
correlation times. For noise with lag-1 autocorrelation $\rho$ (the AR(1) model),

$$\operatorname{Var}[\bar{x}] = \frac{\sigma^2}{N}\cdot\frac{1+\rho}{1-\rho},
\qquad\text{so}\qquad
N_\text{eff} = N\,\frac{1-\rho}{1+\rho}.$$

**Measured check.** AR(1) series of length $N = 200$, averaged over 4000
realisations:

| $\rho$ | measured $\operatorname{Var}[\bar x]$ | AR(1) formula | $N_\text{eff}$ |
|---|---|---|---|
| 0.00 | 0.004943 | 0.004966 | 200 |
| 0.80 | 0.122323 | 0.119798 | 22.2 |
| 0.95 | 1.804048 | 1.643270 | 5.1 |

At $\rho = 0.95$ the 200 samples are worth about **5**, so the achievable
reduction is $\sqrt{5} = 2.2$ rather than $\sqrt{200} = 14.1$ — a factor of 6.4
over-optimistic if $\sqrt{N}$ is applied blindly.

**Design consequence.** The effective number of independent samples is set by the
correlation time $t_c$ and the total recording time $T$, not by the sampling
rate: $N_\text{eff}\approx T/(2t_c)$. Sampling faster than $t_c$ adds data but
not information. The correct strategy is to **record longer**, and to estimate
$t_c$ from the autocorrelation function of the data rather than assume it.

### 3.4 The tidal signal, derived in form

The tide is worth deriving in form even though evaluating it needs astronomical
data, because the derivation shows why it is a *signal* rather than noise.

The gravitational acceleration produced by the Moon at the Earth's centre is
$a_0 = GM_m/d_m^2$ directed toward the Moon. At a surface point displaced by
$\mathbf{R}$ from the centre, the acceleration differs by the *differential*
(tidal) term. Expanding $GM_m/|\mathbf{d}_m-\mathbf{R}|^2$ to first order in
$R/d_m$ and taking the difference gives the residual

$$\mathbf{a}_\text{tidal} \approx \frac{2GM_m}{d_m^3}\,\mathbf{R} ,$$

to the leading order (the full expansion in spherical harmonics also has the
component that produces the permanent tide). Units:
$\mathrm{m^3kg^{-1}s^{-2}\cdot kg\,m^{-3}\cdot m} = \mathrm{m\,s^{-2}}$ ✓.

**The important structural facts, all derived and none needing a number:**

- the tide scales as $d_m^{-3}$, the *cube* of the body's distance — so the
  Moon's tide exceeds the Sun's by a large factor even though the Sun's
  gravitational attraction at the Earth is far larger;
- the ratio of the two is
  $\left(M_s/M_m\right)\left(d_m/d_s\right)^{3}$, a pure number requiring only
  tabulated masses and distances;
- the amplitude depends on latitude and on the Earth's elasticity (the Love
  numbers), so a *model*, not a formula, is required for survey work;
- **and critically, it is perfectly predictable in time**, which is what makes it
  a signal rather than noise. It can be computed for any station and epoch in
  advance.

**How to state it honestly.** The demonstration uses a *stated synthetic* tide of
0.15 mGal amplitude with a 12.42 h period, which is the correct order for the
semidiurnal band at mid-latitude. Evaluating a real tide requires an ephemeris,
the Love numbers and an ocean-loading model; the standard formulation is
Longman's (1959), cited in Section 9. **Do not quote a remembered tidal amplitude
as though it were universal** — it varies with latitude, time and local
elasticity, and the ocean-loading term alone can reach a tenth of the body tide
near a coast.

### 3.5 Why drift and signal can be confused

There is a deeper difficulty than "estimate the drift well", and it is worth
stating because it limits what any processing can do.

Suppose the true signal contains a long-wavelength component and the instrument
drift is a slow monotonic function of time. In a survey where *time correlates
with position* — a traverse run in one direction, a loop closed over the same
ground — the drift and the long-wavelength signal are **not separable**. Both are
smooth functions of a variable that is itself correlated with the independent
variable. Formally, the design matrix of a regression of reading on (position,
time) is ill-conditioned, exactly as in
[05-03-01](../03-forward-modelling-principles/01-forward-problem.md).

**The practical consequences, all of which follow from that one observation:**

- **Loop closure is not optional.** Running back over the same stations in
  reverse (a "forward and reverse" or "repeat" traverse) breaks the
  time–position correlation and makes drift and signal separable.
- **Tie intervals bound what wavelengths of signal are recoverable.** If the drift
  is interpolated over $\tau$, any geophysical signal with a time signature
  comparable to $\tau$ is partly absorbed into the drift estimate. That is why
  long-wavelength regional trends from a short survey should be treated with
  suspicion.
- **The $\tau^2$ law of Section 3.2 cuts both ways.** Shorter ties reduce residual
  drift (good) and also absorb more short-wavelength signal (bad), because a
  linear interpolation over a short interval tracks whatever varies in that
  interval.
- **Drift removed on a repeat traverse is the test.** If the drift estimate from
  the forward pass disagrees with that from the reverse pass beyond the reading
  noise, the model of drift (linearity, or the tie interval) is wrong.

**How to state the residual honestly.** "Drift removed by linear interpolation
between 90-minute ties, with residual drift bounded by 0.02 mGal (Section 3.2)"
is a complete description: it names the model, the interval, and the bound.
"Drift corrected" is not, because it asserts an accuracy without naming the
operation that produced it.

## 4. Units and magnitudes

| Source | Typical magnitude | Time signature | Removable? |
|---|---|---|---|
| Readout noise | 0.005–0.05 mGal (relative gravimeter) | white | by averaging |
| Drift | 0.01–0.1 mGal per hour, up to mGal/hour in bad conditions | monotonic | by tying (if linear) |
| Earth tide | up to ~0.2–0.3 mGal peak-to-peak | periodic, ~12.42 h and 24 h | by model |
| Bias (scale) | up to 0.1% of the reading | constant | only by calibration |
| Magnetic diurnal variation | tens of nT | periodic + irregular | by base/repeat or model |

These magnitudes are *ranges*, and they depend strongly on instrument,
latitude, and conditions; use them to plan, not to conclude. The demonstration
below uses stated synthetic values.

## 5. Assumptions

1. **Drift is linear between ties.** Poorly satisfied if the instrument is
   moved, warmed, or handled roughly.
2. **The tide model is correct to better than the target.** Modern models are,
   but the *ocean loading* term requires a local model.
3. **The base station is stable.** A monument that moves is a bias.
4. **Random noise is independent.** Correlated noise (e.g. microseism) averages
   less efficiently than $\sqrt{N}$.
5. **Repetition measures precision, not accuracy.** This is the assumption
   most often violated in practice.

## 6. Worked examples (measured)

Using the module demonstration with stated synthetic inputs (target 4 mGal
Gaussian, drift 0.05 mGal/h, tide amplitude 0.15 mGal, noise $\sigma = 0.02$
mGal, relief ±8 m, Bouguer density 2400 kg/m³):

- **Raw** readings depart from the target by 0.2324 mGal RMS, with a largest
  single error of 0.3623 mGal. The contamination exceeds the target.
- **After removing drift and the tide model** the RMS departure is 0.0212 mGal
  — but note this is *not* the noise floor, because the elevation effect is
  still present in both the data and the comparison.
- **After the free-air and Bouguer corrections** the residual is 0.0212 mGal
  against a stated $\sigma = 0.02$ mGal: the corrections removed exactly what
  the model put in.

The demonstration notes explicitly that it removed drift *exactly*, which is
optimistic; real residual drift of 0.01–0.05 mGal over a survey is routine.

### 6.1 A shortcut that fails: "average more samples"

**The shortcut.** A 0.03 mGal microseismic oscillation at 0.2 Hz corrupts a
reading. Averaging 100 samples taken 1 s apart is expected to give
$0.03/\sqrt{100} = 0.003$ mGal.

**Why the arithmetic is wrong.** The period is 5 s, so 1 s samples are one fifth
of a cycle apart and strongly correlated: for a sinusoid sampled at 1 s intervals
the lag-1 correlation is $\cos(2\pi/5) = 0.309$, and the AR(1) result of
Section 3.3 gives

$$N_\text{eff} = 100\cdot\frac{1-0.309}{1+0.309} = 52.8
\qquad\Longrightarrow\qquad
\sigma_\text{mean} \approx \frac{0.03}{\sqrt{52.8}} = 0.0041\ \mathrm{mGal},$$

so the promised 0.003 mGal is not delivered — and even this understates the
problem, because a pure tone has *no* decorrelation within one period.

**The correct arithmetic.** Average over a whole number $n$ of periods. The
residual of the sinusoid after averaging over $n$ complete periods is exactly
zero at integer $n$; the error is bounded by the incomplete-period fraction,
$\le 0.03/(\pi n)$. To reduce it tenfold, $n \approx 3$ whole periods are needed,
i.e. **15 s of recording** — 15 samples, not 100. The count is irrelevant; the
duration relative to the period is everything. Five hundred samples at 0.1 s
intervals over the same 15 s achieve the same result; 100 samples at 1 s
intervals over 100 s also work, but because 100 s is 20 periods, not because the
count is 100.

**The generalisable lesson.** Reduction of correlated noise is governed by
*duration divided by correlation time*. The same principle appears in the spatial
domain as the distinction between sample spacing and aperture
([05-01-02](../01-what-geophysics-measures/02-method-taxonomy.md)).

### 6.2 Extended worked example: reading a residual plot

The demonstration's synthetic survey provides a worked case in the order a field
geophysicist would actually reason.

**Step 1 — look at the raw spread.** The raw readings depart from the known
target by 0.2324 mGal RMS with a largest single error of 0.3623 mGal. Since the
target amplitude is 4.0 mGal, the contamination is about 6% of the signal — not
fatal for a large target, but fatal for a subtle one. **The first number to
compute is always this ratio**, because it decides whether the target is
reachable at all.

**Step 2 — ask which contaminant has which structure.** Over a 4-hour loop the
drift reaches $0.05\times4 = 0.20$ mGal — a slow trend across the whole survey.
The tide, with 0.15 mGal amplitude and a 12.42 h period, changes smoothly and
predictably within the loop. The readout noise, $\sigma = 0.02$ mGal, is
uncorrelated station to station. Three different signatures; three different
treatments.

**Step 3 — remove what you can model.** Subtracting the exact drift and the tide
model leaves 0.0212 mGal RMS, which is the elevation effect plus noise. The
residual is *not* yet the noise floor: the terrain terms are still in the data
*and* absent from the comparison, so they appear as residual. This is a subtle
and common misreading — checking a processing step against a model that omits
one of the terms in the data.

**Step 4 — apply the corrections, then re-check.** After the free-air and
Bouguer corrections the residual is still 0.0212 mGal, now equal to the stated
noise $\sigma = 0.02$ mGal. The peak recovered anomaly is 3.9995 mGal against a
true 4.0000 mGal — a 0.01% error, i.e. at the noise level. All three
corrections did exactly what the forward model required.

**Step 5 — ask what the residual would have told you if it had been larger.**
A residual larger than the noise has two possible causes: a real feature, or a
mis-specified correction. The demonstration shows the second explicitly: with
$\rho_B = 3000$ kg/m³ instead of 2400, the peak anomaly shifts by $+0.157$ mGal
— 3.9% of the target, well above the noise. **From the data alone you cannot
tell which cause is operative**; you must test the corrections independently
(e.g. a Nettleton density profile, or a repeat survey with a different
correction set).

**Step 6 — state what was assumed.** The demonstration removed drift *exactly*,
using the known drift function. Real ties estimate it, and residual drift of
0.01–0.05 mGal is routine. Reporting a synthetic residual of 0.0212 mGal without
that caveat would overstate the achievable precision by a factor of two or more.

## 7. Python demonstration

`code/noise_reduction_demo.py` builds the survey, applies each correction, and
prints the effect of each. Predict the raw RMS error before running. Then
modify the script to make the drift *non-linear* (add a quadratic term) and
observe how much residual survives base-station tying — that is the honest
measure of a tie's power.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/03-noise-and-drift-exercises.md`](./exercises/03-noise-and-drift-exercises.md).

**Common mistakes.** (1) Averaging $N$ samples and claiming $\sqrt{N}$ noise
reduction when the noise is correlated. (2) Forgetting the tide is a *signal* to
be modelled, not noise. (3) Confusing precision with accuracy. (4) Tying only at
the start and end of a long day. (5) Ignoring ocean-loading in coastal surveys.

**Applications.** Microgravity monitoring of volcanoes and aquifers needs
tidal and drift control at the 0.005 mGal level; magnetic base stations serve
the same role for diurnal variation; repeat surveys for 4-D need *accuracy*
reproducibility, which is a calibration problem.

## 9. Further reading

- **Telford, Geldart & Sheriff (1990).** Chapter 2. Level: intermediate.
- **Longman, I. M. (1959). Formulas for computing the tidal accelerations due
  to the Moon and the Sun.** *JGR* 64, 2351–2355. The classical tidal
  formulation.
- **Milsom & Eriksen, *Field Geophysics*.** Level: intermediate. Practical
  drift and tie procedure.

## 10. Related lessons

- [05-02-04 Reduction of Observations to Anomalies](./04-reduction-of-observations.md)
- [05-01-05 Choosing a Method](../01-what-geophysics-measures/05-choosing-a-method.md)
- [07-01-05 Gravity Units and Instruments](../../07-gravity-geodesy/01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md)

## Self-assessment checklist

- [ ] I can list the four error sources and their time signatures.
- [ ] I can derive what base-station tying removes and what it leaves.
- [ ] I can explain why repetition does not detect bias.
- [ ] I can state typical magnitudes as ranges, not values.
- [ ] I can design a QC loop for each source.
