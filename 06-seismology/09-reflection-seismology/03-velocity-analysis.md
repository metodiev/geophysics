---
id: 06-09-03
title: "Velocity Analysis and Moveout Interpretation"
level: graduate
prereqs: ["06-09-02"]
tags: [seismology, reflection-seismology, velocity-analysis, semblance, dip-moveout]
---

# Velocity Analysis and Moveout Interpretation

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the semblance (coherency) objective used to pick stacking
   velocities, and explain why maximising it estimates $v_{\text{nmo}}$.
2. **Quantify** the resolution of a velocity pick as a function of cable length
   (maximum offset) and bandwidth.
3. **Derive** the dip-moveout relation $v_{\text{nmo}} = v/\cos\theta$ for a
   dipping reflector and compute the velocity and depth bias when the dip is
   ignored.
4. **Explain** what DMO correction removes and why it is applied before velocity
   analysis.
5. **State** the difference between stacking velocity, NMO velocity, RMS
   velocity and interval velocity, and when they coincide.
6. **Recognise** when a velocity pick is unconstrained rather than merely
   uncertain.

## Prerequisites

- [02 Reflection Processing Flow: Deconvolution, NMO, Stack, Migration](02-processing-flow.md).

## 1. Intuition: velocity is the only unknown, so it is the whole game

The NMO equation $t^{2} = t_0^{2} + x^{2}/v^{2}$ has one free parameter per
arrival. Everything that needs to know "how fast" — depth conversion, migration,
lithology prediction — depends on getting $v$ right. Velocity analysis is
therefore not a preprocessing chore; it is the central inference step of
reflection seismology.

The method is beautifully simple: for each candidate velocity, apply NMO and ask
how well the gather lines up. Alignment is measurable, and the velocity that
maximises it is the pick. The interesting part is not the objective but its
**resolution**: how precisely can the alignment be measured, and how does that
depend on the experiment? Two knobs dominate — the maximum offset (how much
moveout curvature is available) and the bandwidth (how sharply the events can be
picked). A third effect, dip, biases the answer systematically rather than
blurring it.

All numbers are **SYNTHETIC**.

## 2. Precise definitions

### 2.1 Semblance

For a gather of $N$ traces, NMO-corrected with trial velocity $v$, the semblance
at two-way time $t_0$ over a window of $M$ samples is

$$S(v,t_0) = \frac{\displaystyle\sum_{j=1}^{M}
\left(\sum_{i=1}^{N} d_i(t_0+\tau_j)\right)^{2}}
{\displaystyle N \sum_{j=1}^{M}\sum_{i=1}^{N} d_i^{2}(t_0+\tau_j)}.$$

$S$ lies between 0 (no alignment) and 1 (perfectly identical traces). The pick is
the $v$ that maximises $S$ over $t_0$.

### 2.2 Stacking, NMO, RMS and interval velocity

- $v_{\text{stack}}$: the velocity that maximises semblance — a *measurement*.
- $v_{\text{nmo}}$: the velocity in the moveout equation — a *parameter*.
- $v_{\text{rms}}$: $\sqrt{\sum v_i^{2}\Delta t_i/\sum \Delta t_i}$ — a *model
  quantity*.
- $v_{\text{int}}$: the interval velocity of a layer, recovered from RMS
  velocities via Dix's equation.

They coincide for a single interface over a constant-velocity medium and in
general they do not.

### 2.3 Dip moveout

For a planar reflector dipping at angle $\theta$ (measured in the vertical plane
containing the profile), the moveout remains approximately hyperbolic but with

$$v_{\text{nmo}} = \frac{v}{\cos\theta}.$$

## 3. Derivations

### 3.1 Why maximising semblance estimates the velocity

If NMO is applied with the true velocity, all $N$ traces of an event contribute
the same wavelet at the same $t_0$, so the numerator
$\left(\sum_i d_i\right)^{2}$ scales as $N^{2}$ while the denominator scales as
$N$ times the trace energy. More precisely, for identical traces, $\sum_i d_i = N d$ and
$\sum_i d_i^{2} = N d^{2}$, so $S = N^{2}d^{2}/(N\cdot N d^{2}) = 1$. For
misaligned traces, $\sum_i d_i$ is a *sum of shifted wavelets* whose peak is
smaller than $N$ times the peak of one, while the denominator (a sum of squares)
is unchanged; hence $S<1$. Maximising $S$ therefore minimises the misalignment,
and NMO misalignment is smallest at the true velocity. **Semblance is a
normalised measure of how much the traces look alike after correction, and
alignment is the physical proxy for the correct velocity.**

### 3.2 Resolution versus cable length

The moveout is $\Delta t \approx x^{2}/(2\,t_0\,v^{2})$ for small offset.
Differentiating with respect to $v$:

$$\frac{\partial(\Delta t)}{\partial v}
= -\frac{x^{2}}{t_0\,v^{3}}.$$

The *change* in moveout produced by a fractional velocity error
$\delta v/v$ is therefore proportional to $x^{2}$. To detect a given velocity
change you need a moveout difference large enough to break the alignment, and
that difference grows with the square of the offset. Hence:

$$\text{velocity resolution} \propto \frac{1}{x_{\max}^{2}}.$$

*Numerical check.* With a 30 Hz wavelet and offsets up to $x_{\max}$, the
demonstration measures the 90%-width of the semblance peak:

| $x_{\max}$ (m) | 90%-width (m/s) | relative width |
|---|---|---|
| 800 | 350 | 14.0% |
| 1200 | 160 | 6.4% |
| 1600 | 90 | 3.6% |
| 2400 | 50 | 2.0% |
| 3200 | 40 | 1.6% |

The width falls steeply with cable length and then flattens: the $1/x_{\max}^{2}$
scaling holds until the misalignment becomes comparable to the wavelet's
resolvable shift, after which the bandwidth limits further improvement. Over
$800\to3200\ \mathrm{m}$ (a factor of 4 in offset, 16 in $x^{2}$) the width falls
by a factor of about 9, close to the predicted trend with a bandwidth floor.

### 3.3 Resolution versus bandwidth

A shorter wavelet can be shifted by less before the alignment degrades. The
corresponding length scale is the Rayleigh-type criterion: two events can be
distinguished when their separation exceeds about half the dominant period, i.e.
$\Delta t \gtrsim 1/(2f_0)$. Setting this equal to the moveout difference
$x^{2}\delta v/(t_0 v^{3})$ gives the velocity resolution

$$\delta v \approx \frac{t_0\,v^{3}}{2 f_0\,x_{\max}^{2}}.$$

*Numerical check.*

| wavelet $f_0$ (Hz) | 90%-width (m/s) | relative width |
|---|---|---|
| 12 | 170 | 6.8% |
| 20 | 90 | 3.6% |
| 30 | 40 | 1.6% |
| 45 | 20 | 0.8% |
| 60 | 540 | 21.6% (sampling-limited) |

The width falls roughly as $1/f_0$ up to 45 Hz — the formula's prediction. The
60 Hz row *worsens*: at $\mathrm{d}t = 2\ \mathrm{ms}$ a 60 Hz Ricker spans only
about three samples, so the discrete NMO interpolation aliases and the pick
degrades. That is a sampling limit of the experiment, not evidence that bandwidth
hurts. **State the sampling rate whenever you quote a bandwidth resolution.**

### 3.4 Dip moveout: derivation and bias

For a dipping interface, the zero-offset reflection point is not at the midpoint,
and the travel-time curve is still hyperbolic to first order but with the
velocity scaled by $1/\cos\theta$. Deriving this from geometry: the wavefront
from a dipping reflector at depth $d$ (measured perpendicular) has an apparent
depth $d/\cos\theta$ beneath the midpoint, and the extra path length scales both
the time and the apparent velocity by the same factor $1/\cos\theta$. Hence

$$v_{\text{nmo}} = \frac{v}{\cos\theta}.$$

If the dip is ignored, the *stacking velocity* overestimates the true velocity by

$$\frac{\delta v}{v} = \frac{1}{\cos\theta}-1,$$

and the apparent reflector depth similarly overestimates the true (perpendicular)
depth by the same factor.

*Numerical check.*

| dip $\theta$ | $v_{\text{nmo}}/v$ | velocity bias | apparent depth bias |
|---|---|---|---|
| $10^\circ$ | 1.0154 | 1.54% | 1.54% |
| $20^\circ$ | 1.0642 | 6.42% | 6.42% |
| $30^\circ$ | 1.1547 | 15.47% | 15.47% |
| $40^\circ$ | 1.3054 | 30.54% | 30.54% |

At $20^\circ$ the velocity is 6.4% too high; at $30^\circ$ it is 15.5% too high.
A velocity error of that size propagates directly into migration (lesson 04) and
into any depth conversion.

**DMO correction** removes the $1/\cos\theta$ factor before velocity analysis by
redistributing energy according to dip, after which the recovered velocity is the
true one and steep dips stack correctly. Without DMO, dips and velocities are
traded against each other: a steeper reflector can be mistaken for a faster
medium.

### 3.5 Anisotropy: the same bias by another route

The dip bias of Section 3.4 is a *geometric* effect. A *physical* effect produces
a similar bias in layered rocks: **anisotropy**. In a transversely isotropic
medium with a vertical symmetry axis, the moveout velocity is

$$v_{\text{nmo}} \approx v_{\text{vertical}}\sqrt{1+2\delta},$$

where $\delta$ is Thomsen's anisotropy parameter. The vertical velocity — the one
that converts time to depth — is *not* the moveout velocity, and the two differ
by a factor that depends on $\delta$.

*Numerical check.* For $\delta = 0.05$ (a modest shale anisotropy),
$\sqrt{1+0.10} = 1.049$, so the moveout velocity is $4.9\%$ higher than the
vertical velocity. Converting a two-way time with the moveout velocity
overestimates depth by $4.9\%$; converting with the vertical velocity
underestimates the stacking quality. Neither velocity alone does both jobs.

**The practical rules.**

- **Dip and anisotropy bias the velocity in the same direction** (both increase
  the apparent moveout velocity), so their effects are hard to separate from
  moveout alone.
- **They are separated by geometry**: anisotropy is azimuthally systematic and
  dip-dependent in a specific way, and a multi-azimuth or wide-azimuth survey can
  distinguish them.
- **A depth conversion must state whether the velocity is a vertical velocity, an
  NMO velocity, or a migration velocity.** Conflating them is one of the most
  common sources of a several-per-cent depth error.

*Worked check.* A reflector gives $v_{\text{nmo}} = 3200\ \mathrm{m\,s^{-1}}$ at
$t_0 = 2.0\ \mathrm{s}$. If anisotropy has $\delta = 0.08$, the vertical velocity
is $3200/\sqrt{1.16} = 2971\ \mathrm{m\,s^{-1}}$, and the depth conversion
$h = v_{\text{vert}}t_0/2 = 2971\ \mathrm{m}$ is $229\ \mathrm{m}$ smaller than the
naive $3200\ \mathrm{m}$. Both numbers are "the velocity"; only one gives the
right depth.

## 4. Physical interpretation

- **Velocity analysis measures alignment**, and alignment is easier to measure
  when the moveout is large — hence long cables.
- **Resolution improves with offset curvature and with bandwidth**, and those are
  the only two physical knobs. Processing cannot create either.
- **Dip is a systematic error, not a random one.** It biases the answer in a
  direction determined by the geology, so it cannot be averaged away by more
  data.
- **The four velocities are different objects.** Confusing $v_{\text{stack}}$ with
  $v_{\text{int}}$ is a common source of depth errors of several per cent.

## 5. Assumptions

1. **Hyperbolic moveout** for the semblance to have a well-defined maximum.
2. **A single, isolated event** — overlapping events bias the pick toward a
   compromise velocity.
3. **Lateral homogeneity** within the gather; a fault or a lateral velocity
   change within the cable length violates it.
4. **No dip, or DMO applied.** Without DMO the $1/\cos\theta$ bias is
   unavoidable.
5. **Adequate sampling**, as the 60 Hz row demonstrates.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $S$ | dimensionless | ratio of squared sums |
| $v$, $v_{\text{nmo}}$ | $\mathrm{m\,s^{-1}}$ | |
| $x_{\max}$ | m | |
| $\delta v$ | $\mathrm{m\,s^{-1}}$ | $t_0 v^{3}/(f_0 x^{2})$: $\mathrm{s\,m^{3}s^{-3}/(s^{-1}m^{2})} = \mathrm{m\,s^{-1}}$ ✔ |
| $\theta$ | rad | $\cos\theta$ dimensionless |

The dimensional check of the resolution formula is worth doing once: it passes,
which is why the formula's *scaling* ($\delta v \propto 1/(f_0 x_{\max}^{2})$)
can be trusted even though its constant is approximate.

## 7. Worked examples

### Example 1 — moveout difference from a velocity error

$t_0 = 1.0\ \mathrm{s}$, $v = 2500\ \mathrm{m\,s^{-1}}$,
$x = 3000\ \mathrm{m}$:

$$\Delta t(v) = \frac{x^{2}}{2 t_0 v^{2}} = \frac{9.0\times10^{6}}
{2\,(1.0)(6.25\times10^{6})} = 0.720\ \mathrm{s}.$$

With $v' = 2600$ ($+4\%$): $\Delta t' = 9.0\times10^{6}/(2\times6.76\times10^{6})
= 0.666\ \mathrm{s}$. The moveout differs by $54\ \mathrm{ms}$ — larger than the
30 Hz period, so this velocity error is easily detected at 3 km offset, and
nearly invisible at 1 km (where the same calculation gives $6\ \mathrm{ms}$).

### Example 2 — the dip bias in depth

A reflector yields $v_{\text{stack}} = 3000\ \mathrm{m\,s^{-1}}$ at
$t_0 = 2.0\ \mathrm{s}$. Assuming no dip, the depth is
$h = v t_0/2 = 3000\ \mathrm{m}$. If the true dip is $25^\circ$, the true
velocity is $v = v_{\text{stack}}\cos 25^\circ = 2719\ \mathrm{m\,s^{-1}}$ and the
true perpendicular depth is $2719\ \mathrm{m}$ — an overestimate of $281\
\mathrm{m}$ ($10.3\%$) if the dip is ignored. The *along-dip* depth is larger
still, but that is a different quantity that must not be conflated.

### Example 3 — reading the resolution table

Below $1200\ \mathrm{m}$ offset the 90%-width is 15% of the velocity. A 15%
velocity error moves a reflector picked at $2.0\ \mathrm{s}$ by about $450\
\mathrm{m}$ in depth — far more than the vertical resolution. **No amount of
careful picking can fix a short cable**; the experiment must be redesigned.

### Example 4 — designing the cable for a 1% velocity target

From Section 3.3, $\delta v \approx t_0 v^{3}/(2f_0 x_{\max}^{2})$. Require
$\delta v/v \le 0.01$, i.e. $\delta v \le 30\ \mathrm{m\,s^{-1}}$ for
$v = 3000\ \mathrm{m\,s^{-1}}$, $t_0 = 2\ \mathrm{s}$, $f_0 = 30\ \mathrm{Hz}$:

$$x_{\max}^{2} \ge \frac{t_0 v^{3}}{2 f_0 \delta v}
= \frac{2\times2.7\times10^{10}}{2\times30\times30}
= 3.0\times10^{7}\ \mathrm{m^{2}},$$

$$x_{\max} \ge 5.5\ \mathrm{km}.$$

Since real cables are often shorter, **a 1% velocity target at 2 s with a 30 Hz
wavelet is not achievable with typical acquisition** — and the formula tells you
that before the survey is shot. The alternatives are a higher-frequency source, a
shallower target, or acceptance of a larger velocity uncertainty. The
demonstration's measured widths (2.0% at 2400 m, 1.6% at 3200 m) are consistent
with this scaling, with the bandwidth floor being reached around 2400–3200 m.

## 8. Python demonstration

`code/velocity_analysis_demo.py`:

1. defines the semblance objective and scans stacking velocity for a synthetic
   gather (true $v = 2500\ \mathrm{m\,s^{-1}}$), reporting the peak and 90%-width;
2. sweeps maximum offset from 800 to 3200 m and reports the width;
3. sweeps wavelet frequency from 12 to 60 Hz, exposing the sampling limit at
   60 Hz;
4. tabulates the dip-moveout bias from $0^\circ$ to $40^\circ$.

The semblance is computed by NMO mapping each trace with
$\mathrm{np.interp}$ and windowing the numerator and denominator, so the reported
widths are reproducible from the printed grid (161 trial velocities from 1800 to
3400 m/s).

## 9. Exercises

Full sets are in
[`exercises/03-velocity-analysis-exercises.md`](./exercises/03-velocity-analysis-exercises.md)
and
[`exercises/03-velocity-analysis-solutions.md`](./exercises/03-velocity-analysis-solutions.md).

- **★** Compute the moveout at 2 km offset for $t_0 = 1.5\ \mathrm{s}$,
  $v = 2800\ \mathrm{m\,s^{-1}}$.
- **★★** Derive $\partial(\Delta t)/\partial v$ and explain the $x^{2}$ scaling of
  velocity resolution.
- **★★** A reflector gives $v_{\text{stack}} = 3200\ \mathrm{m\,s^{-1}}$ at
  $t_0 = 1.8\ \mathrm{s}$ with a $30^\circ$ dip. Compute the true velocity and the
  depth bias from ignoring the dip.
- **★★★** Using the resolution formula, design a cable length that would recover
  velocity to 1% for a 30 Hz wavelet at $t_0 = 2\ \mathrm{s}$,
  $v = 3000\ \mathrm{m\,s^{-1}}$.

## 10. Common mistakes

1. **Reporting stacking velocity as interval velocity.** They differ whenever the
   overburden has velocity structure or dip.
2. **Ignoring dip.** A 20% depth error is easy to produce (Section 3.4).
3. **Picking on a single gather.** Velocity analysis is statistical: use many
   CMPs, and evaluate the lateral consistency of the picks.
4. **Trusting a pick whose semblance peak is broad and flat.** A flat maximum is
   an unconstrained velocity; report the width.
5. **Quoting velocity resolution without the sampling interval.** As Section 3.3
   shows, aliasing can dominate the true bandwidth effect.

## 11. Real-world applications

- **Depth conversion and drilling targets.** A 5% velocity error moves a target
  by tens of metres at typical reservoir depths; velocity analysis quality is
  directly a drilling-risk question.
- **Migration velocity model building.** Modern imaging iterates between
  migration and velocity update; the semblance pick is the starting point.
- **Anisotropy.** In the presence of anisotropy the hyperbolic NMO velocity
  depends on the anisotropy parameters, not just the vertical velocity; ignoring
  this biases velocities in exactly the way dip does.
- **Time-lapse feasibility.** 4-D interpretation requires that velocity changes
  from production are not confused with processing velocity changes, which are
  often larger.

## 12. Further reading

- **Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists.** Level: intermediate to advanced. Semblance picking and DMO.
- **Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press.** Level: intermediate. Velocity definitions.
- **Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: advanced. The moveout expansion and
  anisotropy.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related lessons

- [02 Reflection Processing Flow: Deconvolution, NMO, Stack, Migration](02-processing-flow.md).
- [04 Migration and Imaging: Time vs Depth, Kirchhoff and RTM](04-migration-imaging.md) —
  where the velocity is used and how sensitive the image is.
- [05 AVO/AVA Analysis and Its Assumptions](05-amplitude-vs-offset.md) — the
  amplitude counterpart of this lesson.
- [06-02-04 Ray Tracing](../02-ray-theory-and-travel-times/04-ray-tracing.md) —
  computing the exact travel times used for the error check.

## 14. Self-assessment checklist

- [ ] I can define semblance and explain why its maximum estimates velocity.
- [ ] I can derive the $1/x_{\max}^{2}$ and $1/f_0$ scalings of resolution.
- [ ] I can compute the dip-moveout bias and state what DMO removes.
- [ ] I can distinguish stacking, NMO, RMS and interval velocity.
- [ ] I can recognise an unconstrained pick from a flat semblance maximum.
- [ ] I can state the sampling caveat when quoting bandwidth resolution.
