---
id: 06-09-02
title: "Reflection Processing Flow: Deconvolution, NMO, Stack, Migration"
level: graduate
prereqs: ["06-09-01", "06-08-01"]
tags: [seismology, reflection-seismology, processing, nmo, stacking]
---

# Reflection Processing Flow: Deconvolution, NMO, Stack, Migration

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the normal-moveout (NMO) hyperbola from the two-layer geometry, and
   the higher-order term that makes it fail at long offset.
2. **Quantify** the hyperbolic approximation's error against an exact ray-traced
   travel time.
3. **Explain** stacking as an average, and derive the $\sqrt{N}$ improvement for
   random noise.
4. **Show** that stacking does *not* attenuate coherent noise with a different
   moveout, and measure the difference.
5. **Place** deconvolution and migration in the flow and state what each one
   removes.
6. **State** the assumptions of each step and the artefacts each introduces.

## Prerequisites

- [01 Acoustic Impedance, Reflection Coefficients and the Convolution Model](01-reflection-principle.md) —
  the convolutional model and two-way time.
- [01 Receiver Functions: Deconvolution and Ps Conversions](../08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md) —
  the deconvolution machinery, developed there in a crustal setting.

## 1. Intuition: the processing flow is a sequence of approximations

Raw reflection data are a collection of traces recorded at many source–receiver
separations (offsets). Two things must be done before they can be interpreted:
the wavelet must be shortened or removed (deconvolution), and traces that sample
the *same* subsurface point must be combined so that noise averages down
(stacking). For the traces to combine, the reflection from a given interface must
arrive at a *predictable* time as a function of offset — and that prediction is
the moveout equation.

Every step is an approximation. NMO assumes a hyperbolic moveout that is only
exact for a single interface over a constant-velocity medium. Stacking assumes
noise is uncorrelated between traces. Deconvolution assumes a stationary
wavelet. The honest practitioner states which approximation is being relied on
and checks the residual.

All numbers here are **SYNTHETIC**.

## 2. Precise definitions

### 2.1 Offset, CMP, fold

- **Offset** $x$: horizontal source–receiver distance.
- **CMP (common midpoint) gather**: the set of traces whose source and receiver
  share a midpoint; these sample the same subsurface point.
- **Fold** $N$: the number of traces in a gather (strictly, the redundancy at a
  CMP).

### 2.2 Normal moveout

The reflection from an interface at two-way time $t_0$ (zero offset) arrives at

$$t(x) = \sqrt{t_0^{2} + \frac{x^{2}}{v_{\text{nmo}}^{2}}}$$

in the hyperbolic approximation, where $v_{\text{nmo}}$ is the
**normal-moveout velocity**. The **moveout** is $t(x)-t_0$.

### 2.3 Stacking

The **stack** is the (usually mean) sum of the traces in a gather after NMO
correction:

$$s(t_0) = \frac{1}{N}\sum_{i=1}^{N} d_i\!\left(t_0\right).$$

## 3. Derivations

### 3.1 The NMO hyperbola from geometry

Consider one interface at depth $h$, horizontal, with a constant speed $v$ above
it. A source at $(-x/2,0)$ and a receiver at $(+x/2,0)$ both illuminate the
reflection point at the midpoint. The image point (mirror) is at depth $h$ below
the surface, so the distance from source to the reflection point to receiver is
the straight distance from source to the mirror image:

$$\text{path} = 2\sqrt{\left(\frac{x}{2}\right)^{2} + h^{2}}.$$

Dividing by $v$:

$$t(x) = \frac{2}{v}\sqrt{\frac{x^{2}}{4}+h^{2}}
= \sqrt{\frac{4h^{2}}{v^{2}}+\frac{x^{2}}{v^{2}}}
= \sqrt{t_0^{2}+\frac{x^{2}}{v^{2}}}, \qquad t_0 = \frac{2h}{v}.$$

This is **exact** for a single interface with constant velocity above it.

### 3.2 The hyperbolic approximation and its failure

For a stack of layers, no single constant velocity reproduces $t(x)$ exactly.
The standard approach defines the RMS velocity

$$v_{\text{rms}} = \sqrt{\frac{\sum_i v_i^{2}\,\Delta t_i}{\sum_i \Delta t_i}},
\qquad \Delta t_i = \frac{2h_i}{v_i},$$

and approximates $t^{2} \approx t_0^{2} + x^{2}/v_{\text{rms}}^{2}$. Expanding the
exact travel time for layered media gives a series in $x^{2}$:

$$t^{2}(x) = t_0^{2} + \frac{x^{2}}{v_{\text{nmo}}^{2}}
+ c_4\,x^{4} + \cdots,$$

and $v_{\text{nmo}} = v_{\text{rms}}$ only when the higher-order term vanishes
(which requires a particularly simple velocity function). The quartic term is
what makes the hyperbola drift at long offset.

*Numerical check (SYNTHETIC).* A three-layer model (500 m at 2200 m/s, 700 m at
2800 m/s, 800 m at 3400 m/s over a 4000 m/s half-space) has
$t_0 = 1.4251\ \mathrm{s}$ and $v_{\text{rms}} = 2848.1\ \mathrm{m\,s^{-1}}$.
Comparing the exact ray-traced time with the hyperbola:

| offset (m) | exact $t$ (s) | hyperbola (s) | error (ms) |
|---|---|---|---|
| 0 | 1.4251 | 1.4251 | $+0.000$ |
| 500 | 1.4359 | 1.4359 | $+0.005$ |
| 997 | 1.4674 | 1.4675 | $+0.070$ |
| 2004 | 1.5883 | 1.5893 | $+1.038$ |
| 3002 | 1.7679 | 1.7725 | $+4.565$ |
| 3992 | 1.9868 | 1.9990 | $+12.199$ |

The error reaches $12\ \mathrm{ms}$ at 4 km offset and has a maximum of
$79\ \mathrm{ms}$ over the full spread. Because a 30 Hz wavelet has a period of
$33\ \mathrm{ms}$, an error of $12\ \mathrm{ms}$ is a third of a period: at long
offset the hyperbola visibly mis-stacks. **The failure grows with offset and with
the strength of the velocity contrast**, and is worst when a fast layer overlies
a slow one.

### 3.3 Deconvolution in the flow

Deconvolution attempts to invert the wavelet, turning the convolutional model
$s = w * r$ into an estimate of $r$. In its simplest form (spiking deconvolution)
it designs a filter $f$ such that $w * f \approx \delta$, then applies it to every
trace. Two problems are unavoidable and were met in detail in
[08-01 §3.4](../08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md):

- **The wavelet is not known exactly**, so the filter is designed from
  statistical assumptions (whiteness of reflectivity, minimum phase) that may not
  hold.
- **The inversion is ill-posed** where the wavelet spectrum is small; a
  stabilisation (pre-whitening, a water level) is required and trades resolution
  against noise.

What deconvolution does *not* do is change the arrival times; it changes the
wavelet. That is why it is applied before velocity analysis in the flow, so that
the events are sharp enough to pick.

### 3.4 Stacking as an average: random noise

Model each pre-stack trace as signal $s$ plus noise $n_i$, with the noise
independent between traces, zero mean and variance $\sigma^{2}$. The mean stack is

$$\bar{d} = \frac{1}{N}\sum_{i=1}^{N}(s+n_i) = s + \frac{1}{N}\sum_i n_i,$$

whose noise term has variance

$$\operatorname{Var}\!\left(\frac{1}{N}\sum_i n_i\right)
= \frac{1}{N^{2}}\sum_i \sigma^{2} = \frac{\sigma^{2}}{N}.$$

So the noise standard deviation falls as $\sigma/\sqrt{N}$ and the
signal-to-noise ratio improves as $\sqrt{N}$.

*Numerical check.* The demonstration builds a 16-fold gather, adds noise at 0.30
of the wavelet peak, and measures the ratio of noise rms (outside the arrival
window) for a single trace against an $N$-fold stack, averaged over 40
realisations:

| fold $N$ | predicted $\sqrt{N}$ | measured |
|---|---|---|
| 4 | 2.00 | 2.04 |
| 8 | 2.83 | 2.98 |
| 16 | 4.00 | 4.48 |

The measured values run slightly ahead of $\sqrt{N}$ because the single-trace
reference also contains the moveout stretch, but the **scaling** is confirmed:
stacking improves random-noise SNR as the square root of the fold.

### 3.5 Stacking does *not* fix coherent noise

If the noise is a *coherent event* with a different moveout — a multiple, a
refraction, a converted wave — then it is not independent between traces and does
not average to zero. Summing $N$ traces of a coherent event amplifies it exactly
as it amplifies the signal.

*Numerical check.* The demonstration adds a coherent event at
$v = 0.72\,v_{\text{rms}}$ and measures the primary/coherent amplitude ratio:

| | single trace | 16-fold stack |
|---|---|---|
| primary / coherent event | 1.000 | 0.916 |

There is **no $\sqrt{N}$ improvement**: the ratio is essentially unchanged
(0.92 against 1.00) because NMO with the primary's velocity does not align the
coherent event, but summing still passes it through. Attenuating a coherent event
requires a method that exploits its *moveout* — a Radon transform, an f–k filter,
or SRME — not more stacking. This is the honest limitation of the fold argument:
**fold buys random-noise suppression, nothing else.**

### 3.6 Where migration fits

NMO and stack position an event at the correct $t_0$ for a *flat* reflector
directly beneath the midpoint. A dipping reflector or a point diffractor is
mispositioned and smeared by the stack. Migration is the step that moves energy
to its true $(x,z)$ position by summing along the diffraction curves that the
data actually follow. Its velocity sensitivity is severe and is treated in
[04 Migration and Imaging](04-migration-imaging.md).

### 3.7 Deconvolution in practice: what it can and cannot recover

The deconvolution step is often described as if it recovered the reflectivity.
It cannot, for a reason that follows directly from the convolution theorem. If
$S(\omega)=W(\omega)R(\omega)$, then dividing by $W$ recovers $R$ exactly *only*
where $W(\omega)\ne0$ and only if $W$ is known exactly. Two failures follow:

1. **Spectral nulls.** Where the wavelet has no energy, the reflectivity is
   unrecoverable. The recovered reflectivity is therefore band-limited, and its
   resolution is set by the wavelet's band, not by the deconvolution.
2. **Unknown wavelet.** A statistical deconvolution designs $W$ from assumptions
   (minimum phase, white reflectivity). Where those fail — a mixed-phase source,
   a coloured reflectivity — the filter removes real signal along with the
   wavelet.

The practical consequence is the same trade-off met in receiver functions
(lesson 08-01): a stabilisation (pre-whitening) is required and it trades
resolution for stability. **Deconvolution sharpens within the band; it cannot
create band.** A processing report that claims "resolution improved by
deconvolution" should specify the band over which it improved.

### 3.8 Migration aperture and what is missing

Migration sums data along diffraction curves of a finite lateral extent — the
**aperture**. A reflector whose dip requires energy from outside the aperture is
simply not reconstructed, and its absence is not evidence about the geology.

The aperture needed for a dip $\theta$ at depth $z$ is roughly
$x_{\text{ap}} \approx z\tan\theta$ on each side of the image point. For
$\theta = 45^\circ$ and $z = 2\ \mathrm{km}$ this is $2\ \mathrm{km}$ — larger
than many surveys' full cable length. The symptom of an inadequate aperture is
that steeper dips are progressively lost in a *smooth* fashion (not imaged at
all), whereas an inadequate velocity produces a *distorted* image. Distinguishing
"not there" from "not imaged" requires knowing the aperture.

## 4. Physical interpretation

- **NMO is a geometry statement.** It converts offset to zero offset by
  accounting for the longer path to an off-axis reflection point — nothing more.
- **Velocity is the only free parameter** in the equation, so every method that
  improves the stack is, implicitly or explicitly, estimating a velocity.
- **Stacking is a filter, not a truth machine.** It produces one trace per CMP
  from many, and its action is an average over offsets: everything with a
  consistent moveout survives, everything else is attenuated in proportion to its
  incoherence.
- **The sequence matters.** Deconvolution before velocity analysis (sharp
  events), NMO and stack after (regularised geometry), migration last (image).

## 5. Assumptions

1. **Hyperbolic moveout.** Good at short offset and weak velocity contrast; it
   fails for strong lateral variation, anisotropy, or long offsets.
2. **Known velocity.** $v_{\text{nmo}}$ is estimated (lesson 03) and its error
   propagates into the stack.
3. **Noise is random and independent between traces** for the $\sqrt{N}$ result.
   Coherent noise voids it.
4. **A stationary wavelet** for global deconvolution; the wavelet lengthens with
   time as high frequencies are attenuated, so a single filter is an average.
5. **Flat layering within the gather.** Dipping events need DMO or pre-stack
   migration.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $x$ | m | |
| $t, t_0$ | s | |
| $v_{\text{nmo}}$ | $\mathrm{m\,s^{-1}}$ | |
| $x^{2}/v^{2}$ | $\mathrm{m^{2}/(m^{2}\,s^{-2})} = \mathrm{s^{2}}$ | |
| $\sqrt{t_0^{2}+x^{2}/v^{2}}$ | s | |
| $\sigma/\sqrt{N}$ | same as noise | dimensionless ratio $N$ |

A moveout computed in ms with velocity in m/s and offset in m must be converted
carefully: $x^{2}/v^{2}$ is in $\mathrm{s^{2}}$, and mixing ms with s introduces a
factor of $10^{6}$.

## 7. Worked examples

### Example 1 — moveout at a given offset

$t_0 = 1.425\ \mathrm{s}$, $v = 2848\ \mathrm{m\,s^{-1}}$, $x = 2000\ \mathrm{m}$:

$$\frac{x^{2}}{v^{2}} = \frac{4.0\times10^{6}}{8.111\times10^{6}}
= 0.4931\ \mathrm{s^{2}},$$
$$t = \sqrt{1.425^{2}+0.4931} = \sqrt{2.0306+0.4931} = \sqrt{2.5237}
= 1.5886\ \mathrm{s}.$$

Moveout $= 0.1636\ \mathrm{s}$. The exact ray trace gives $1.5883\ \mathrm{s}$, so
the hyperbola errs by $0.3\ \mathrm{ms}$ here — small at 2 km, large by 4 km.

### Example 2 — how much fold is needed?

Suppose an interpretation requires a signal-to-noise ratio of 10 and a single
trace has SNR 2. Then $\sqrt{N} = 5$, $N = 25$ traces. If the cable provides only
16 traces, the target is not achievable by stacking alone, and the honest options
are more shots, a longer cable, or a processing method that suppresses the
specific noise. **Fold cannot be conjured from nowhere; it is set by geometry.**

### Example 3 — the cost of coherent noise

With a coherent multiple at 0.8 of the primary amplitude and 16-fold stacking,
the measured ratio is 0.916 — essentially the same as the single trace's 1.000.
If instead the multiple were random, the ratio would improve by
$\sqrt{16} = 4$. The difference — a factor of about 4 — is the quantitative value
of recognising the noise as coherent, and the reason multiple-attenuation methods
exist.

### Example 4 — how much detail does the band contain?

A 30 Hz Ricker has essentially no energy above about $4f_0 = 120\ \mathrm{Hz}$
and none at DC. Suppose the useful band is $10$–$80\ \mathrm{Hz}$. The shortest
recoverable wavelet is then about one cycle at 80 Hz, i.e. $\sim12\ \mathrm{ms}$
of simple period, and the vertical resolution is roughly
$v/(4f_{\text{max}}) = 3000/(4\times80) = 9.4\ \mathrm{m}$ at most. A broadband
acquisition extending to 150 Hz would give $5\ \mathrm{m}$. **Deconvolution cannot
exceed these numbers**: it can only redistribute energy within the recorded band.
This is why high-resolution seismology invests in sources and receivers with
high-frequency output, not in cleverer filters.

## 8. Python demonstration

`code/processing_flow_demo.py`:

1. ray-traces the exact travel time through a three-layer model and tabulates the
   hyperbola's error versus offset (max $79\ \mathrm{ms}$);
2. builds a 16-fold CMP gather and stacks it after NMO (peak
   $1.428\ \mathrm{s}$ against $t_0 = 1.425\ \mathrm{s}$);
3. measures random-noise reduction versus fold and compares with $\sqrt{N}$;
4. measures the primary/coherent-event ratio for a single trace and a 16-fold
   stack, showing that coherent noise is not attenuated.

The demo prints the timestep ($2\ \mathrm{ms}$), the sample count ($1500$) and the
fold, so every number can be reproduced.

## 9. Exercises

Full sets are in
[`exercises/02-processing-flow-exercises.md`](./exercises/02-processing-flow-exercises.md)
and
[`exercises/02-processing-flow-solutions.md`](./exercises/02-processing-flow-solutions.md).

- **★** Compute the moveout at $x = 1500\ \mathrm{m}$ for $t_0 = 1.0\ \mathrm{s}$,
  $v = 2500\ \mathrm{m\,s^{-1}}$.
- **★★** Derive $t(x)$ for a single interface from the mirror-image geometry and
  state where the derivation assumes constant velocity.
- **★★** Show that the stack of $N$ traces with independent noise improves SNR by
  $\sqrt{N}$ and state the assumption that fails for coherent noise.
- **★★★** Design a processing sequence for a data set with a strong water-bottom
  multiple and justify the position of each step.

## 10. Common mistakes

1. **Using the hyperbola at arbitrarily long offsets.** Check the residual; the
   quartic term is measurable (Section 3.2).
2. **Believing that more fold fixes multiples.** It does not (Section 3.5).
3. **Picking velocities on un-deconvolved data.** The wavelet is too long to
   pick the peak reliably.
4. **Applying a single deconvolution filter to data whose wavelet changes with
   time.** The filter becomes an average and shortens some events while
   distorting others.
5. **Stacking across a fault or a steep dip without DMO/pre-stack migration.**
   The events do not align and the stack is destructive.

## 11. Real-world applications

- **Marine and land acquisition design.** Cable length sets the maximum offset
  and hence the moveout curvature available for velocity analysis (lesson 03);
  fold sets the random-noise suppression.
- **Time-lapse (4-D) processing.** Extremely careful NMO and stack alignment are
  what make repeat surveys comparable (lesson 08).
- **Automated velocity picking.** Semblance-based auto-pickers use exactly the
  objective derived in lesson 03 and rely on the wavelet being short.
- **Teaching the limits of averaging.** The random-versus-coherent distinction is
  the same one that appears in any stacking problem, from seismic to gravity
  surveys.

## 12. Further reading

- **Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists.** Level: intermediate to advanced. The standard reference for
  the whole flow.
- **Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press.** Level: intermediate.
- **Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: advanced. The moveout expansion and its
  higher-order terms.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related lessons

- [01 Acoustic Impedance, Reflection Coefficients and the Convolution Model](01-reflection-principle.md).
- [03 Velocity Analysis and Moveout Interpretation](03-velocity-analysis.md) —
  how $v_{\text{nmo}}$ is estimated.
- [04 Migration and Imaging: Time vs Depth, Kirchhoff and RTM](04-migration-imaging.md).
- [06 Multiple Attenuation](06-multiple-elimination.md) — the remedy for coherent
  noise.
- [08-01 Receiver Functions: Deconvolution and Ps Conversions](../08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md) —
  the deconvolution trade-off in detail.

## 14. Self-assessment checklist

- [ ] I can derive the NMO hyperbola from the mirror-image geometry.
- [ ] I can explain and quantify the hyperbola's failure at long offset.
- [ ] I can derive the $\sqrt{N}$ improvement for random noise.
- [ ] I can explain why coherent noise survives stacking and what does fix it.
- [ ] I can state where deconvolution and migration sit in the flow and why.
- [ ] I can list three assumptions and the artefact each introduces.
