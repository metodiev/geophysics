---
id: 10-01-02
title: "Velocity Estimation and Depth Conversion in GPR"
level: advanced
prereqs: ["10-01-01", "02-03-08"]
tags: [gpr, near-surface, gpr-principles, velocity-analysis, depth-conversion, diffraction-hyperbola]
---

# Velocity Estimation and Depth Conversion in GPR

> **All models and data in this module are SYNTHETIC.** The velocities, layer
> thicknesses and picking errors below are chosen teaching values. No field site,
> instrument or measured travel time is involved.

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** a two-way time to a depth for a stated velocity, and **quantify**
   the depth error produced by a velocity error.
2. **Use** the air wave and the ground wave to set time zero and to estimate the
   top-layer velocity, and **compute** the depth bias a time-zero error causes.
3. **Derive** the GPR offset geometry $t(x) = \sqrt{4d^{2}+x^{2}}/v$ and explain
   why GPR carries $4d^{2}$ where reflection seismology carries $4d^{2}$ with a
   different factor convention.
4. **Fit** a diffraction hyperbola in $t^{2}$ against $x^{2}$ to recover a
   velocity, and **state** what the fit's curvature actually measures.
5. **Derive** the multi-layer moveout $t^{2} = t_0^{2} + x^{2}/v_{\mathrm{nmo}}^{2}$
   and **apply** the Dix relation to obtain an interval velocity.
6. **Recognise** when a constant-velocity correction fails, and **measure** the
   residual moveout it leaves.
7. **Test** a velocity by predicting a time that was not used to derive it.

## Prerequisites

- [01 GPR Physics](01-gpr-physics.md) — $v = c/\sqrt{\varepsilon_r}$, the
  reflection coefficient and the two-way time.
- [02-03-08 Reflection, Refraction and Snell's Law for Waves](../../02-physics/03-oscillations-and-waves/08-reflection-refraction.md) —
  the ray geometry at an interface.

## 1. Depth conversion is one equation and one unknown too many

A GPR record is a function of time. The quantity of interest is a depth:

$$d = \frac{v\,t}{2}. \tag{1.1}$$

Because $d$ is linear in $v$ at fixed $t$, the fractional depth error equals the
fractional velocity error exactly, with no cancellation and no sign change. In
the demonstration, for a pick at $t = 80.0\ \mathrm{ns}$:

| assumed $v$ ($\mathrm{m\,ns^{-1}}$) | $d$ (m) | depth error |
|---|---|---|
| 0.06750 (90% of nominal) | 2.7000 | $-10.0\%$ |
| 0.07125 | 2.8500 | $-5.0\%$ |
| 0.07500 | 3.0000 | nominal |
| 0.07875 | 3.1500 | $+5.0\%$ |
| 0.08250 | 3.3000 | $+10.0\%$ |

So the question is not "how do we convert time to depth" but "how do we get
$v$". This lesson is a catalogue of the answers and of their limits.

## 2. Time zero: the air wave and the ground wave

With antennas separated by $x$, the first arrival is the **air wave**:

$$t_{\mathrm{air}} = \frac{x}{c}, \tag{2.1}$$

because nothing in the ground is faster than $c$. It is used to define $t=0$.
The second arrival is the **ground wave**, travelling in the top layer:

$$t_{\mathrm{ground}} = \frac{x}{v_1}. \tag{2.2}$$

The ratio of the two arrival times is the ratio $c/v_1 = \sqrt{\varepsilon_{r1}}$,
so the ground wave is a direct measurement of the top-layer permittivity. In the
demonstration, at $x = 0.30\ \mathrm{m}$: $t_{\mathrm{air}} = 1.001\
\mathrm{ns}$ and, for $v_1 = 0.060\ \mathrm{m\,ns^{-1}}$,
$t_{\mathrm{ground}} = 5.000\ \mathrm{ns}$, a ratio of $5.00$ and hence
$\varepsilon_{r1} = 25.0$.

A time-zero error $\delta t_0$ shifts every depth by

$$\delta d = \frac{v}{2}\,\delta t_0. \tag{2.3}$$

At $0.2\ \mathrm{ns}$ sampling this is $0.60\ \mathrm{cm}$ for
$v = 0.060\ \mathrm{m\,ns^{-1}}$ and $0.90\ \mathrm{cm}$ for
$v = 0.090\ \mathrm{m\,ns^{-1}}$ per single-sample error. Small — but it is a
**systematic** shift, identical on every trace, and it therefore biases a depth
map rather than averaging out of it.

## 3. The diffraction hyperbola

A point scatterer at depth $d$ and lateral position $x_0$ produces, in a
zero-offset section,

$$t(x) = \frac{2\sqrt{d^{2}+(x-x_0)^{2}}}{v}
= \frac{\sqrt{4d^{2} + \xi^{2}}}{v}, \qquad \xi \equiv 2(x-x_0). \tag{3.1}$$

The factor 4 deserves explanation because it is the commonest source of a factor
of two error when moving between GPR and reflection seismology. Write the
transmitter and receiver positions as $x \pm x/2$ for an antenna separation $x$.
The two-way path is

$$2\sqrt{d^{2}+\left(\frac{x}{2}\right)^{2}} = \sqrt{4d^{2}+x^{2}}, \tag{3.2}$$

so in **GPR offset geometry both antennas move away from the midpoint** and the
moveout is $t^{2} = t_0^{2} + x^{2}/v^{2}$. In reflection seismology the source
and receiver are *both* moved and the conventional form is
$t^{2} = t_0^{2} + 4h^{2}/v^{2}$ with $h$ the half-offset. The two are the same
physics with different letters; the failure mode is to copy the seismic $4$
without copying the definition of the offset.

Squaring (3.1) linearises the hyperbola:

$$t^{2} = \frac{4d^{2}}{v^{2}} + \frac{x^{2}}{v^{2}}, \tag{3.3}$$

so a least-squares fit of $t^{2}$ against $x^{2}$ returns the intercept
$t_0^{2} = 4d^{2}/v^{2}$ and the slope $1/v^{2}$ **directly**. The velocity is
what the curvature carries; the depth follows from the intercept and the velocity
together.

**Worked example 1.** A synthetic hyperbola for $v = 0.0900\
\mathrm{m\,ns^{-1}}$ and $d = 2.40\ \mathrm{m}$, sampled at $x = 0, 0.8, \dots,
4.0\ \mathrm{m}$, gives $t = 53.333\ \mathrm{ns}$ at $x=0$ and
$69.424\ \mathrm{ns}$ at $x = 4.0\ \mathrm{m}$. The fit returns intercept
$2844.4444\ \mathrm{ns^{2}}$ and slope $123.4568\ \mathrm{ns^{2}\,m^{-2}}$, hence

$$v = \frac{1}{\sqrt{123.4568}} = 0.09000\ \mathrm{m\,ns^{-1}},
\qquad
d = \frac{v\sqrt{2844.4444}}{2} = 2.4000\ \mathrm{m},$$

both exact because the synthetic data are exact. What matters is not the
exactness but what was used: only the **curvature in $x$**. A hyperbolic fit
whose aperture is narrow is therefore a weak measurement, whatever its formal
precision.

**Worked example 2 — the aperture matters.** Adding picking noise of
$0.2\ \mathrm{ns}$ (one sample) to the same hyperbola and refitting three times
gives $v = 0.09060$, $0.09038$ and $0.09017\ \mathrm{m\,ns^{-1}}$: biased high by
$0.2$–$0.7\%$, and the bias does not average away because the noise enters
$t^{2}$ asymmetrically. Over a $2\ \mathrm{m}$ aperture the same pick noise would
move the fitted velocity by several per cent.

## 4. Multi-layer moveout and the Dix relation

For a stack of horizontal layers the small-offset moveout is approximately
hyperbolic with an **NMO velocity**

$$t^{2} \simeq t_0^{2} + \frac{x^{2}}{v_{\mathrm{nmo}}^{2}},
\qquad
v_{\mathrm{nmo}}^{2} = \frac{\sum_i v_i^{2}\,\Delta t_i}{t_0}, \tag{4.1}$$

where $\Delta t_i = 2h_i/v_i$ is the two-way interval time in layer $i$. Inverting
(4.1) for the interval velocity between two picked reflections is the **Dix
relation**:

$$v_{n}^{2} = \frac{v_{\mathrm{nmo},n}^{2}\,t_{0,n}
- v_{\mathrm{nmo},n-1}^{2}\,t_{0,n-1}}{t_{0,n}-t_{0,n-1}}. \tag{4.2}$$

Two features of (4.2) matter.

- The **difference** in the numerator and denominator means both picks enter with
  weights of comparable size, so errors do not shrink: perturbing any pick by
  $5\%$ moves the interval velocity by $+2.2\%$, $-3.4\%$, $-1.9\%$ or $+8.1\%$
  depending on which one.
- The correction is only as good as the hyperbolic approximation. Equation (4.1)
  is exact for a single layer and approximate for anything else.

**Worked example 3 — how badly does it fail?** Take $v_1 = 0.0600\
\mathrm{m\,ns^{-1}}$, $h_1 = 1.20\ \mathrm{m}$, $v_2 = 0.0900\
\mathrm{m\,ns^{-1}}$ and a reflector at $2.40\ \mathrm{m}$. The exact two-way
time is obtained by Fermat's principle: minimise

$$t(a) = \frac{2\sqrt{(a+x/2)^{2}+h_1^{2}}}{v_1}
+ \frac{2\sqrt{a^{2}+(d-h_1)^{2}}}{v_2} \tag{4.3}$$

over the signed refraction offset $a$. Because the second term is shorter in the
fast layer, the minimum sits at **negative** $a$: the ray refracts towards the
transmitter side, which is easy to get wrong. At $x=0$ the exact time is
$66.667\ \mathrm{ns}$, matching $2h_1/v_1 + 2(d-h_1)/v_2$. Fitting
$t^{2}$ against $x^{2}$ over $0$–$4.0\ \mathrm{m}$ gives
$v_{\mathrm{nmo}} = 0.07438\ \mathrm{m\,ns^{-1}}$, while the Dix relation (4.1)
predicts $0.07348\ \mathrm{m\,ns^{-1}}$: the two differ by $1.2\%$ and both are
*correct answers to different questions*. After NMO with the Dix velocity the
residual moveout at the far offset is $0.448\ \mathrm{ns}$, i.e. $2.01\
\mathrm{cm}$ of depth.

That residual is the honest limit of a constant-velocity correction, and it is
also the reason a semblance peak for a deeper event is broader than the pick
noise alone would allow.

### 4.1 Why the refraction offset is negative

The sign of $a$ is not an accident of the numbers; it follows from the
stationarity condition. Differentiating (4.3) with respect to $a$ and setting the
derivative to zero gives

$$\frac{a+x/2}{v_1\sqrt{(a+x/2)^{2}+h_1^{2}}}
= -\frac{a}{v_2\sqrt{a^{2}+(d-h_1)^{2}}}, \tag{4.4}$$

which is Snell's law at the interface written in terms of horizontal slownesses.
If $a$ were positive the left side would be positive and the right side negative,
so (4.4) cannot hold: a solution requires $a<0$. Since the left side must then
still be positive, $a > -x/2$ is also required. **The refraction point therefore
lies between the transmitter and the midpoint**, never beyond the transmitter. In
the two-layer model above, at $x = 3.0\ \mathrm{m}$ the minimum sits near
$a = -0.75\ \mathrm{m}$, inside the interval $(-1.5, 0)$. A solver that searches
only $a \ge 0$ returns the vertical path and an arrival time wrong by more than
$10\ \mathrm{ns}$.

## 5. Assumptions and regime of validity

1. **Constant velocity within each layer.** Gradients in moisture or compaction
   violate it, and the hyperbola becomes skewed rather than symmetric.
2. **Horizontal, planar layers.** A dipping interface changes the apex position
   and the apparent velocity; this is the subject of
   [02-05 GPR Modelling and Full-Waveform Inversion](../02-gpr-acquisition-and-processing/05-gpr-modelling-and-inversion.md)
   and of [02-04 3-D GPR Imaging and Time Slices](../02-gpr-acquisition-and-processing/04-gpr-3d-imaging.md).
3. **Small offsets compared with depth** for the hyperbolic approximation. The
   demonstration puts a number on it: with a maximum offset of
   $1.67\times$ the target depth, the residual after NMO is $2.01\ \mathrm{cm}$.
4. **The offset is known and the antenna separation is constant.** A varying
   separation changes $x$ trace by trace and corrupts the curvature.
5. **Ray parameter within the critical angle.** Beyond total internal reflection
   (Section 3 of the antennas lesson) no transmitted ray exists and the geometry
   changes.
6. **Time zero is fixed.** Equation (2.3) is a systematic depth bias, not noise.

## 6. Worked example 4 — verifying a velocity with an unused prediction

The rule this module follows is simple:

> A velocity used for depth conversion must be tested against a time that was not
> used to derive it.

From the synthetic two-layer model, converting the $66.667\ \mathrm{ns}$ pick
with the top-layer velocity alone gives $d = 0.0600 \times 66.667/2 = 2.0000\
\mathrm{m}$ against a true $2.40\ \mathrm{m}$: an error of $-0.4000\ \mathrm{m}$
($-16.67\%$). Converting the same pick through the two-layer model, subtracting
the known time in layer 1 first, gives exactly

$$\frac{2h_1 + v_2\left(t_0 - 2h_1/v_1\right)}{2}
= \frac{2.40 + 0.0900 \times 26.667}{2} = 2.4000\ \mathrm{m}.$$

The two conversions differ by $17\%$ on identical data; only the second used a
velocity that had been measured over the interval it was applied to.

## 7. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| two-way time $t$, $t_0$ | ns | $2d/v$ |
| offset $x$ | m | transmitter-to-receiver separation |
| velocity $v$, $v_{\mathrm{nmo}}$ | $\mathrm{m\,ns^{-1}}$ | $c/\sqrt{\varepsilon_r}$ |
| hyperbola slope | $\mathrm{ns^{2}\,m^{-2}}$ | $1/v^{2}$ |
| intercept | $\mathrm{ns^{2}}$ | $4d^{2}/v^{2}$ |

The slope of $t^{2}$ against $x^{2}$ has dimensions $\mathrm{ns^{2}\,m^{-2}}$,
the inverse square of a speed in $\mathrm{m\,ns^{-1}}$ — a quick check that the
velocity will come out in the right unit.

## 8. Python demonstration

`code/gpr_velocity_and_depth_demo.py` produces every number above. It:

1. tabulates the depth conversion $d = vt/2$ for five speeds and four times;
2. computes the air-wave and ground-wave arrival times for five antenna
   separations and the depth bias from a time-zero error;
3. builds a synthetic diffraction hyperbola, fits $t^{2}$ against $x^{2}$, and
   repeats the fit with $0.2\ \mathrm{ns}$ pick noise;
4. computes exact two-layer ray times by Fermat minimisation, fits an NMO
   velocity, compares it with the Dix prediction, and measures the residual
   moveout at the far offset;
5. shows the error amplification of the Dix relation for a $\pm 5\%$ perturbation
   of each pick;
6. verifies the two-layer conversion against the forward model.

## Mastery checkpoint

Without notes:

> A hyperbola apex is at $t_0 = 53.333\ \mathrm{ns}$ and the event has a slope of
> $123.5\ \mathrm{ns^{2}\,m^{-2}}$ in a plot of $t^{2}$ against $x^{2}$.
> **(a)** Compute $v$. **(b)** Compute the depth. **(c)** State the depth you
> would report if the true velocity were $10\%$ lower. **(d)** A second event has
> $t_0 = 66.667\ \mathrm{ns}$ and $v_{\mathrm{nmo}} = 0.0744\
> \mathrm{m\,ns^{-1}}$; compute the interval velocity below the first event using
> the first event's picks as $t_{0,1} = 40.000\ \mathrm{ns}$ and
> $v_{\mathrm{nmo},1} = 0.0600\ \mathrm{m\,ns^{-1}}$. **(e)** State one
> measurement that would test your answer.

A worked version appears in
[`exercises/02-gpr-velocity-and-depth-solutions.md`](./exercises/02-gpr-velocity-and-depth-solutions.md).

## Common pitfalls

1. **Copying the seismic moveout convention.** In GPR both antennas move apart;
  in seismic the whole spread moves. The constant and the definition of the
  offset must match.
2. **Fitting a hyperbola over too short an aperture.** The curvature is the
  measurement; a short aperture throws it away.
3. **Assuming a positive refraction offset.** The Fermat minimum for a
  lower-velocity over higher-velocity interface sits on the source side of the
  midpoint.
4. **Reporting a Dix interval velocity without its error bars.** The relation
  amplifies pick errors; a thin top layer amplifies them most.
5. **Trusting a single-velocity conversion through a layered medium.** The
  demonstration's $-16.7\%$ error is typical, not extreme.
6. **Ignoring time zero.** A one-sample, $0.2\ \mathrm{ns}$ error is $6\
  \mathrm{mm}$ at $0.06\ \mathrm{m\,ns^{-1}}$ — on every trace, always the same
  sign.

## Related modules

- [01 GPR Physics](01-gpr-physics.md).
- [03 Attenuation, Penetration Depth and Frequency Trade-Offs](03-gpr-attenuation-penetration.md) —
  the other half of what the medium does to the pulse.
- [02-03 Velocity Analysis and Common-Midpoint Sounding](../02-gpr-acquisition-and-processing/03-gpr-velocity-analysis.md) —
  the survey geometry designed to measure $v$ rather than assume it.
- [06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md) —
  the same moveout mathematics at a much lower frequency.
- [18 Inverse Problems, Optimization and Uncertainty Quantification](../../18-inverse-problems/README.md) —
  what it means for a fit like (3.3) to be well posed.

Materials: [`code/gpr_velocity_and_depth_demo.py`](./code/gpr_velocity_and_depth_demo.py),
[`exercises/02-gpr-velocity-and-depth-exercises.md`](./exercises/02-gpr-velocity-and-depth-exercises.md),
[`exercises/02-gpr-velocity-and-depth-solutions.md`](./exercises/02-gpr-velocity-and-depth-solutions.md).
