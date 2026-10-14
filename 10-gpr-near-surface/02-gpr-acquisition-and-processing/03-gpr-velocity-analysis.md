---
id: 10-02-03
title: "Velocity Analysis and Common-Midpoint Sounding"
level: doctoral
prereqs: ["10-02-01", "10-02-02", "10-01-02"]
tags: [gpr, near-surface, velocity-analysis, common-midpoint, semblance, dix, slant-stack]
---

# Velocity Analysis and Common-Midpoint Sounding

> **All models and data in this module are SYNTHETIC.** The two-layer velocity
> model, offsets, noise level and analysis parameters below are chosen teaching
> values. No field gather, measured velocity or published velocity analysis is
> involved.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the semblance coherency measure and **compute** the semblance
   surface of a synthetic CMP gather over a $(v, t_0)$ grid.
2. **Define** a velocity resolution from a stated coherency threshold, and
   **compare** it with the analytic error propagation
   $\delta v = v^{3} t\, \delta t / x^{2}$.
3. **Explain** why the two disagree where they do, and **attribute** the
   disagreement to model error rather than to noise.
4. **Quantify** the short-offset non-uniqueness: how the velocity peak widens as
   the maximum offset shrinks, and what that means for a shallow GPR sounding.
5. **Derive** the Dix relation and **propagate** pick errors through it.
6. **Cross-check** a moveout velocity with an independent estimator — the slant
   stack of a direct arrival — and **state** why the two are independent.
7. **Report** a velocity with its uncertainty, its aperture and its model error.

## Prerequisites

- [10-02-01 Survey Design: Profile, Grid, CMP and Transillumination](01-gpr-survey-design.md) —
  the offset design that makes this analysis possible.
- [10-02-02 Processing Steps: Dewow, Gain, Filtering, Migration](02-gpr-processing.md) —
  what must be true of the data before a semblance is computed.
- [10-01-02 Velocity Estimation and Depth Conversion in GPR](../01-gpr-principles/02-gpr-velocity-and-depth.md) —
  the moveout equation and the Dix relation.

## 1. What a CMP gather contains

A common-midpoint gather records the same subsurface point with a range of
antenna separations. Its events obey the small-offset hyperbolic approximation in
**GPR geometry** (both antennas moving away from the midpoint):

$$t^{2}(x) \simeq t_0^{2} + \frac{x^{2}}{v_{\mathrm{nmo}}^{2}},
\qquad
v_{\mathrm{nmo}}^{2} = \frac{\sum_i v_i^{2}\Delta t_i}{t_0}. \tag{1.1}$$

Velocity analysis is the search for the $v_{\text{nmo}}$ that makes an event
horizontally coherent after correction, and its honest output is not "the
velocity" but the set of velocities that make it *acceptably* coherent — a
resolution question, exactly like the resolution questions of
[10-01-05](../01-gpr-principles/05-gpr-resolution.md).

## 2. The coherency measure

The standard measure is **semblance**. Within a time window of $2h+1$ samples
centred on a candidate path,

$$S(v, t_0) = \frac{\sum_{\tau}\left(\sum_{i=1}^{N} y_i(\tau)\right)^{2}}
{N \sum_{\tau}\sum_{i=1}^{N} y_i^{2}(\tau)}, \tag{2.1}$$

where $y_i$ is the $i$-th trace after normal-moveout correction with velocity $v$
and zero-offset time $t_0$. $S = 1$ when every trace carries the same value along
the path, and $S \to 0$ for uncorrelated noise. It is a *normalised* measure, so
it is insensitive to absolute amplitude — a virtue when the input gain is
uncertain, and a limitation when amplitude information is wanted.

**Worked example 1 (measurement).** SYNTHETIC two-layer model:
$v_1 = 0.0600\ \mathrm{m\,ns^{-1}}$, $h_1 = 1.20\ \mathrm{m}$,
$v_2 = 0.0900\ \mathrm{m\,ns^{-1}}$, a reflector at $2.40\ \mathrm{m}$; offsets
$0$ to $4.00\ \mathrm{m}$ in $0.20\ \mathrm{m}$ steps ($21$ traces), noise rms
$0.02$ relative to the first reflection. Exact two-way times: $40.000\
\mathrm{ns}$ and $66.667\ \mathrm{ns}$ at $x=0$; at maximum offset $77.746\
\mathrm{ns}$ and $85.619\ \mathrm{ns}$. Scanning $v$ from $0.030$ to $0.130\
\mathrm{m\,ns^{-1}}$ in steps of $0.001$:

| event | peak semblance | recovered $v$ | recovered $t_0$ |
|---|---|---|---|
| 1 (single layer) | 0.9995 | $0.0600\ \mathrm{m\,ns^{-1}}$ | 40.00 ns |
| 2 (two layers) | 0.9956 | $0.0740\ \mathrm{m\,ns^{-1}}$ | 67.27 ns |

The first velocity is recovered to the grid step ($+0.00\%$). The second is a
*two-layer* arrival, and its moveout velocity is not $v_2$: the Dix prediction
(1.1) from the model is $0.0735\ \mathrm{m\,ns^{-1}}$, and the recovered
$0.0740$ is $+0.70\%$ above it. Both numbers are correct answers to different
questions — the semblance measures the hyperbolic NMO velocity of the event, and
the model $\overline{v^2}$ is a definition.

## 3. Resolution of a moveout velocity

Two estimates of the same quantity are available, and comparing them is the point
of this section.

**Analytic.** From $t^{2} = t_0^{2} + x^{2}/v^{2}$,

$$\frac{\partial t}{\partial v} = -\frac{x^{2}}{v^{3}t}
\;\Longrightarrow\;
\delta v = \frac{v^{3}\,t\,\delta t}{x^{2}} \tag{3.1}$$

which **falls as $x^{-2}$**: this is the whole argument for wide offsets.

**Measured.** Define the velocity resolution as the range of $v$ over which the
semblance stays above $0.9$ of its peak. For the SYNTHETIC gather of Example 1:

| event | analytic $\delta v$ ($\delta t = 0.05\ \mathrm{ns}$) | analytic $\delta v$ ($\delta t = 0.25\ \mathrm{ns}$) | measured $0.9$-of-peak width |
|---|---|---|---|
| 1 | $0.00005\ \mathrm{m\,ns^{-1}}$ ($0.09\%$) | $0.00026$ ($0.44\%$) | $0.0000$ (one grid step) |
| 2 | $0.00011$ ($0.15\%$) | $0.00055$ ($0.74\%$) | $0.0020$ ($2.70\%$) |

Three honest readings of that table:

- Event 1 is **exactly hyperbolic** in this model (single layer), so its
  semblance peak is one grid step wide: the width measures the grid, not the
  data.
- Event 2 is only approximately hyperbolic, and its measured width is
  **$3.7\times$** the analytic prediction for a $0.25\ \mathrm{ns}$ pick error.
  The excess is *model error* — non-hyperbolic moveout — and no amount of
  averaging removes it.
- The analytic formula and the measured width therefore bound the answer from
  opposite sides: the formula says what noise would do, the measurement says what
  the model does. Reporting only one of them is a half-truth.

## 4. Short-offset non-uniqueness

The same analysis restricted to progressively shorter offsets makes the
ill-posedness explicit. For event 2:

| maximum offset (m) | offset / target depth | $0.9$-of-peak velocity width ($\mathrm{m\,ns^{-1}}$) |
|---|---|---|
| 0.8 | 0.33 | 0.0750 |
| 1.6 | 0.67 | 0.0160 |
| 2.4 | 1.00 | 0.0070 |
| 4.0 | 1.67 | 0.0020 |

With an aperture under about one target depth the velocity is effectively
undetermined — the width ($0.0750$) is larger than the entire plausible velocity
range of the medium. This is the practical form of the velocity–depth trade-off
derived in
[10-01-02 §4](../01-gpr-principles/02-gpr-velocity-and-depth.md): a
monostatic (zero-offset) profile cannot measure velocity at all, and the
measurement improves as roughly the square of the aperture.

The consequence for survey design is blunt: **if the depth must be known
absolutely rather than relatively, a zero-offset profile is not enough**, and a
CMP sounding — or a known target for calibration — must be included in the
programme.

## 5. Dix inversion and its error amplification

Dix's relation inverts two moveout picks for the interval velocity between them:

$$v_{n}^{2} = \frac{v_{\mathrm{nmo},n}^{2}t_{0,n}
- v_{\mathrm{nmo},n-1}^{2}t_{0,n-1}}{t_{0,n}-t_{0,n-1}}. \tag{5.1}$$

**Worked example 2.** Using the recovery of Example 1 —
$(t_{0,1}, v_{\text{nmo},1}) = (40.00\ \mathrm{ns}, 0.0600)$ and
$(t_{0,2}, v_{\text{nmo},2}) = (67.27\ \mathrm{ns}, 0.0740)$:

$$v_2 = \sqrt{\frac{0.0740^{2}\times67.27 - 0.0600^{2}\times40.00}{27.27}}
= \sqrt{\frac{0.3684 - 0.1440}{27.27}} = 0.0907\ \mathrm{m\,ns^{-1}},$$

against a true $0.0900$: an error of $+0.79\%$. Perturbing each pick by $+5\%$ in
turn gives:

| perturbed pick | resulting $v_2$ | change |
|---|---|---|
| $v_{\text{nmo},2}$ | $0.0980$ | $+8.09\%$ |
| $v_{\text{nmo},1}$ | $0.0877$ | $-3.35\%$ |
| $t_{0,2}$ | $0.0890$ | $-1.85\%$ |
| $t_{0,1}$ | $0.0927$ | $+2.20\%$ |

A $5\%$ error in one pick becomes up to an $8\%$ error in the interval velocity,
and the two NMO velocities dominate the total. The interval velocity is
therefore the *least* well-determined quantity in a depth conversion, which is
why it should be reported with the amplification stated.

## 6. An independent check: the slant stack

Moveout curvature gives one velocity; the **linear moveout of a direct arrival**
gives another, and the two use different physics of the same recording. The
slant stack (linear Radon transform) sums along lines of constant ray parameter
$p$:

$$\tilde{y}(p, \tau) = \sum_i y_i\!\left(\tau + p\,x_i\right),
\qquad p = \frac{1}{v}. \tag{6.1}$$

For the direct ground wave $t = x/v_1 + t_0$ the stack peaks at $p = 1/v_1$ and
$\tau = t_0$. In the demonstration, stacking a synthetic direct wave built with
$v_1 = 0.0600\ \mathrm{m\,ns^{-1}}$ over a $p$ grid from $10$ to $25\
\mathrm{ns\,m^{-1}}$ gives a peak at

$$p = 16.6500\ \mathrm{ns\,m^{-1}} \;\Longrightarrow\;
v = 0.0601\ \mathrm{m\,ns^{-1}} \quad (+0.10\%),$$

with the intercept at $\tau = 5.00\ \mathrm{ns}$, the direct wave's zero-offset
time.

Why this counts as independent: the slant stack uses **no curvature** — it is
sensitive only to the linear moveout of the first arrival — so it cannot inherit
the model error that widens the semblance peak of the deeper event. It measures
the top-layer velocity, which is precisely the quantity that a surface
reflection survey most often gets wrong.

## 7. Assumptions and regime of validity

1. **Hyperbolic moveout.** The whole analysis assumes it; the residual after NMO
   in this SYNTHETIC model reaches $0.675\ \mathrm{ns}$ ($13.5$ samples) at the
   far offset for the two-layer event, and that residual is the source of the
   wide semblance peak in Example 1.
2. **Layered, horizontal, isotropic structure.** Semblance will happily fit a
   velocity to a dipping event's moveout, and the number will be wrong in a way
   the semblance value does not reveal.
3. **The offset is exactly known.** A drifting antenna separation perturbs the
   curvature, and hence $v$, directly.
4. **The wavelet does not change with offset.** Frequency-dependent attenuation
   and antenna directivity both modify the pulse; if the deeper-offset traces
   carry a different spectrum, the correlation measured by (2.1) is partly
   spectral, not kinematic.
5. **Semblance is amplitude-normalised.** It cannot distinguish a strong event
   from a weak one, so a spurious high-semblance path through coherent noise is
   possible.
6. **The slant stack measures the direct wave, not the ground.** Its $p$ is a
   top-layer average along the first metre or so of the array, and it is
   therefore the most reliable velocity in the section and the least
   representative of anything deeper.

## 8. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| semblance | 1 | normalised ratio |
| velocity | $\mathrm{m\,ns^{-1}}$ | $x/\sqrt{t^{2}-t_0^{2}}$ |
| $\delta v$ | $\mathrm{m\,ns^{-1}}$ | $v^{3}t\,\delta t/x^{2}$ |
| ray parameter $p$ | $\mathrm{ns\,m^{-1}}$ | $1/v$ |
| interval velocity | $\mathrm{m\,ns^{-1}}$ | Dix relation |

The ray parameter deserves attention because it is the reciprocal of velocity in
the *GPR* time unit: with $v$ in $\mathrm{m\,ns^{-1}}$, $p$ is in
$\mathrm{ns\,m^{-1}}$, and $p = 16.65$ for $v = 0.060$. Carrying a
$\mathrm{s\,m^{-1}}$ value into this convention is a factor $10^{9}$ error.

## 9. Python demonstration

`code/gpr_velocity_analysis_demo.py` prints everything in this lesson:

1. builds a SYNTHETIC CMP gather over a two-layer model using exact Fermat ray
   times, and computes a semblance surface over $(v, t_0)$ for each event;
2. reports the recovered velocities, semblance peaks and $0.9$-of-peak widths;
3. compares the measured widths with the analytic $\delta v$ from (3.1);
4. repeats the analysis at four maximum offsets to show the resolution collapse;
5. performs a Dix inversion and propagates $+5\%$ pick errors;
6. cross-checks the top-layer velocity with a slant stack of the direct wave;
7. verifies the picked times against a forward model (event 1 residual
   $0.0000\ \mathrm{ns}$, event 2 up to $0.675\ \mathrm{ns}$).

## Mastery checkpoint

Without notes:

> A GPR CMP gather has 21 traces from $0$ to $4.0\ \mathrm{m}$ and an event with
> $t_0 = 66.7\ \mathrm{ns}$ whose moveout corresponds to
> $v = 0.0740\ \mathrm{m\,ns^{-1}}$.
> **(a)** Compute the time at maximum offset and the residual after NMO with
> $v = 0.0735$.
> **(b)** Compute the analytic velocity error from a $0.25\ \mathrm{ns}$ pick
> error at that offset and compare with the measured $0.9$-of-peak width of
> $0.0020\ \mathrm{m\,ns^{-1}}$.
> **(c)** Explain why the two differ, and state which one you would quote.
> **(d)** Redo the velocity error estimate for a maximum offset of $1.0\
> \mathrm{m}$ and state the consequence for a shallow sounding.
> **(e)** State an independent measurement that would test the top-layer velocity.

Parts (a)–(e) are worked in
[`exercises/03-gpr-velocity-analysis-solutions.md`](./exercises/03-gpr-velocity-analysis-solutions.md).

## Common pitfalls

1. **Reporting a semblance peak as "the velocity".** The peak is a maximum of a
   coherency measure; the resolution width is the answer.
2. **Reading the two-layer event's NMO velocity as $v_2$.** It is a weighted
   average; Dix is the conversion.
3. **Trusting a velocity from a short aperture.** Below about one target depth
   the peak is wider than the plausible velocity range.
4. **Ignoring non-hyperbolic moveout.** It, not noise, sets the width of the
   deeper event's peak here.
5. **Amplifying Dix without saying so.** A $5\%$ pick error can move the interval
   velocity by $8\%$.
6. **Mixing $p$ conventions.** $p = 1/v$ in $\mathrm{ns\,m^{-1}}$, not
   $\mathrm{s\,m^{-1}}$.
7. **Believing a high semblance value is a quality guarantee.** Semblance is
   amplitude-normalised and can peak on coherent noise.

## Related modules

- [10-01-02 Velocity Estimation and Depth Conversion in GPR](../01-gpr-principles/02-gpr-velocity-and-depth.md) —
  the same moveout mathematics with fewer unknowns.
- [10-02-04 3-D GPR Imaging and Time Slices](04-gpr-3d-imaging.md) — where the
  velocity from this lesson ends up determining positions.
- [06-09-03 Velocity Analysis](../../06-seismology/09-reflection-seismology/03-velocity-analysis.md) —
  the seismic version, including the same non-hyperbolic caveats.
- [18-02 Linear Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/README.md) —
  the formal statement of the resolution question in Section 3.

Materials: [`code/gpr_velocity_analysis_demo.py`](./code/gpr_velocity_analysis_demo.py),
[`exercises/03-gpr-velocity-analysis-exercises.md`](./exercises/03-gpr-velocity-analysis-exercises.md),
[`exercises/03-gpr-velocity-analysis-solutions.md`](./exercises/03-gpr-velocity-analysis-solutions.md).
