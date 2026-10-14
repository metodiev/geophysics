---
id: 10-02-02
title: "Processing Steps: Dewow, Gain, Filtering, Migration"
level: graduate
prereqs: ["10-02-01", "10-01-05", "05-06-02"]
tags: [gpr, near-surface, processing, dewow, gain, filtering, migration, background-removal]
---

# Processing Steps: Dewow, Gain, Filtering, Migration

> **All models and data in this module are SYNTHETIC.** The attenuation, drift,
> noise level, AGC window, filter cut-offs and migration parameters below are
> chosen model parameters, labelled where they appear. No field dataset, measured
> processing gain or instrument is involved.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** what dewow removes and **measure** the bias it removes from a
   pick, from a zero crossing and from an amplitude ratio.
2. **Distinguish** constant gain from automatic gain control (AGC), and
   **demonstrate** that AGC destroys the amplitude ratios that attenuation and
   reflection-coefficient work depends on.
3. **Measure** the signal-to-noise gain and the pulse broadening produced by a
   band-pass filter, and **state** the trade as a pair of numbers.
4. **Derive** the depth-converted apparent dip of a dipping reflector
   ($\tan\theta_{\text{app}} = \sin\theta$) and **measure** the dip a Kirchhoff
   migration recovers.
5. **Predict** the imaged dip of a wrong-velocity migration from the tangency
   condition $\sin\theta_{\text{mig}} = (v_{\text{mig}}/v)\sin\theta$, and
   **verify** it against a synthetic section.
6. **Measure** the improvement in target-to-clutter ratio produced by a spatial
   median (background-removal) filter, and **state** what it removes that was
   signal.
7. **Order** the steps of a processing sequence and **justify** the order from
   the assumptions each step makes.

## Prerequisites

- [10-02-01 Survey Design: Profile, Grid, CMP and Transillumination](01-gpr-survey-design.md) —
  what the recorded data contain.
- [10-01-05 Vertical and Horizontal Resolution Limits](../01-gpr-principles/05-gpr-resolution.md) —
  the migration and resolution background.
- [05-06-02 Noise Suppression](../../05-core-geophysics/06-data-processing-principles/02-noise-suppression.md) —
  the general treatment of coherent and incoherent noise.

## 1. Why the order matters

A GPR processing sequence is not a list of filters; it is an ordered set of
statements about the data. Each step assumes the previous ones have already held:

$$\text{dewow} \to \text{time zero} \to \text{gain} \to \text{filter} \to
\text{background removal} \to \text{migration}. \tag{1.1}$$

The order is forced by the assumptions. Dewow must come first because a
low-frequency drift biases every later amplitude. Time zero must come before any
depth conversion. Gain must be recorded with its formula, because an amplitude
analysis that uses an unknown gain measures the gain. Filtering must precede
migration if the filter changes the wavelet the migration assumes. Background
removal must precede migration because a horizontally coherent ringing train is
otherwise smeared along migration operators. Any reordering must be justified by
one of these dependencies, not by habit.

## 2. Dewow

The receiver records an inductive ("wow") component: the field that couples
directly from transmitter to receiver, which takes the form of a low-frequency
transient added to the trace. It is not ground response, and it must be removed
before anything is measured. The standard implementation subtracts a running mean
over a window shorter than the period of the shallowest event of interest:

$$y_{\text{dewow}}(t) = y(t) - \frac{1}{W}\int_{t-W/2}^{t+W/2} y(\tau)\,
\mathrm{d}\tau. \tag{2.1}$$

**Worked example 1.** A SYNTHETIC trace containing two reflections at
$16.0\ \mathrm{ns}$ and $40.0\ \mathrm{ns}$ with a true amplitude ratio
$a_2/a_1 = 0.5488$, plus a chosen drift of peak-to-peak amplitude $0.25$ and
noise of rms $0.020$, gives:

| trace | first zero crossing after $t_2$ (ns) | amplitude ratio |
|---|---|---|
| clean (reference) | 41.1254 | 0.5488 |
| with drift | 41.5671 | 0.7071 |
| after dewow ($20\ \mathrm{ns}$ window) | 41.1595 | 0.5711 |

The drift delays the zero crossing by $442\ \mathrm{ps}$ and biases the amplitude
ratio by $+28.8\%$. After a running-mean removal with a chosen $20\ \mathrm{ns}$
window the zero-crossing bias falls to $+34\ \mathrm{ps}$ and the ratio to
$+4.1\%$ of the true value.

Two lessons: the bias is **large** ($29\%$ in an amplitude ratio that an
attenuation measurement would use), and dewow does not remove it
completely — the residual depends on the window length relative to the drift's
period. Choosing the window is a real decision, and it should be stated.

## 3. Gain, and what AGC destroys

Attenuation and geometric spreading mean the deepest part of a trace is often
tens of decibels weaker than the top, and display needs that compensated. There
are two different operations, and confusing them is the point of this section:

- **constant (or deterministic) gain**: multiply by a function of time that is
  known in closed form, $g(t)$, so that the recorded amplitude can be recovered
  exactly by multiplying by $1/g(t)$;
- **automatic gain control (AGC)**: multiply by a *data-dependent* factor that
  equalises the local signal strength, typically

$$g_{\text{agc}}(t) = \frac{\bar{A}}{\text{rms}_W\!\left[y\right](t)},
\qquad \bar{A} = \text{a chosen target level}. \tag{3.1}$$

**Worked example 2.** Continuing Example 1 with a chosen $20\ \mathrm{ns}$
running-rms window:

| processing | measured $a_2/a_1$ | noise rms in a deep window |
|---|---|---|
| dewowed trace | 0.5711 | 0.02983 |
| constant gain $\times 2$ | 0.5711 | 0.05966 |
| AGC | 1.0334 | 0.03828 |

The constant gain scales signal *and* noise and preserves the ratio exactly. The
AGC drives the ratio to $1.03$: it has destroyed the amplitude information that
the attenuation and reflection-coefficient estimates are built on, while
amplifying the noise in quiet windows. AGC is a **display** operation. An
amplitude analysis performed on AGC'd data measures the AGC.

## 4. Band-pass filtering: a two-sided trade

Filtering suppresses out-of-band noise and distorts the pulse. Both effects are
measurable on the same trace, and both must be reported.

**Worked example 3.** A fourth-order Butterworth band-pass with cut-offs at
$0.4f_0$ and $2.5f_0$ — i.e. $80$ to $500\ \mathrm{MHz}$ for $f_0 = 200\
\mathrm{MHz}$ — applied zero-phase, gives:

| processing | signal-to-noise in the target window | envelope FWHM |
|---|---|---|
| raw | 17.41 dB | 2.575 ns (12.87 cm) |
| band-passed | 32.89 dB | 4.275 ns (21.36 cm) |

A $15.5\ \mathrm{dB}$ signal-to-noise gain, paid for with a $66\%$ wider pulse.
In depth terms the resolution degrades from $12.87\ \mathrm{cm}$ to $21.36\
\mathrm{cm}$ at $v = 0.09993\ \mathrm{m\,ns^{-1}}$. **Any statement about a
filter's benefit must come with its resolution cost**, and vice versa: a
resolution claim on unfiltered noisy data is a claim about noise.

## 5. Migration: from apparent to true dip

A dipping interface at angle $\theta$ produces, in a zero-offset record, an event
whose time is

$$t(x) = \frac{2\left(d_0 + x\sin\theta\right)}{v}. \tag{5.1}$$

Converting this to depth with the *correct* velocity gives
$d_{\text{app}}(x) = d_0 + x\sin\theta$, so the apparent dip on the
depth-converted, unmigrated section obeys

$$\tan\theta_{\text{app}} = \sin\theta. \tag{5.2}$$

Migration removes the effect: the migrated image sits at the true dip and the true
position. With a **wrong** velocity, $v_{\text{mig}}$, the migrated dip follows
from the tangency condition between the event and the migration operator: the
event's slope must equal the hyperbola's slope, giving

$$\boxed{\;\sin\theta_{\text{mig}}
= \frac{v_{\text{mig}}}{v}\,\sin\theta.\;} \tag{5.3}$$

**Worked example 4.** A SYNTHETIC interface dipping $\theta = 20^\circ$ with
$d_0 = 2.00\ \mathrm{m}$ in $v = 0.09993\ \mathrm{m\,ns^{-1}}$. The time dip is
$2\sin\theta/v = 6.845\ \mathrm{ns\,m^{-1}}$; the depth-converted apparent dip
is $\arctan(\sin 20^\circ) = 18.88^\circ$, matching (5.2) exactly. Migrating with
an unweighted Kirchhoff sum over a $\pm3\ \mathrm{m}$ aperture gives:

| migration velocity | imaged dip | (5.3) predicts | depth at $x=0$ |
|---|---|---|---|
| correct | $19.39^\circ$ | $20.00^\circ$ | 2.100 m |
| $10\%$ low | $17.32^\circ$ | $17.93^\circ$ | 1.860 m |
| $10\%$ high | $21.11^\circ$ | $22.10^\circ$ | 2.340 m |

The imaged dip tracks (5.3) to within a degree, and the depth at $x=0$ moves by
$\pm0.24\ \mathrm{m}$ for a $\pm10\%$ velocity error — the same linear
sensitivity that depth conversion has, now acting on a dipping event's position.

That the correct-velocity migration gives $19.39^\circ$ rather than $20.00^\circ$
is worth stating plainly: a real migration on a finite aperture with a
peak-picking estimate of the reflector position has an error of a few per cent.
A migration that claims to be exact has usually been tested on something easier
than a dipping reflector.

## 6. Background removal

Coherent horizontal ringing — from antenna coupling, from the ground surface, or
from a horizontal layer that is not of interest — can be suppressed by a spatial
filter across traces, most simply a running median with a short window:

$$\tilde{y}(t, x) = y(t, x) - \operatorname{median}_{x'\in
[x-h, x+h]} y(t, x'). \tag{6.1}$$

**Worked example 5.** A SYNTHETIC section with $161$ traces containing a point
target at $1.20\ \mathrm{m}$ and a five-term ringing train constructed in the demo as
amplitudes $0.35/k$ for $k = 1\ldots5$ at $6, 12, 18, 24, 30\ \mathrm{ns}$ gives:

| processing | target peak | clutter rms | target/clutter |
|---|---|---|---|
| raw | 1.1284 | 0.0967 | 21.34 dB |
| background removed (5-trace median) | 0.4894 | 0.0189 | 28.25 dB |

A $6.9\ \mathrm{dB}$ improvement. The cost is in the same table: the target peak
*fell* by more than half, because a median over five traces subtracts whatever is
common to them, and the diffraction hyperbola's flanks are partly common. **A
flat-lying real reflector has exactly the property this filter removes**, so
background removal must be applied with a window much shorter than the lateral
extent of anything you want to keep — and then declared, because it changes the
data's lateral content.

## 7. Assumptions and regime of validity

1. **Dewow's drift is additive and low frequency.** A drift with significant
   energy in the signal band cannot be removed without also removing signal;
   judge by comparing spectra before and after.
2. **The gain is known.** If AGC or an unlogged instrument gain has been applied,
   amplitude work is impossible; state which gain was used or requote results in
   relative terms only.
3. **The filter is zero-phase** (forward-backward) if the interpretation depends
   on picking times; a causal filter shifts the wavelet and biases picks.
4. **The migration velocity is spatially constant** for (5.3), and the medium is
   2-D. Real velocity errors are not uniform, and the imaged dip then varies along
   the event.
5. **The migration aperture is adequate.** Aperture truncation limits the dip
   that can be imaged (see [10-01-05 §4](../01-gpr-principles/05-gpr-resolution.md)),
   so a "wrong" dip may be an aperture artefact rather than a velocity error.
6. **Background removal assumes the clutter is laterally coherent and the signal
   is not.** For a grid survey of a flat-lying target, the assumption is false.

## 8. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| drift, gain | arbitrary (same as data) | ratio operations |
| filter cut-offs | Hz (or MHz) | fraction of $f_0$ |
| pulse width | ns (or m at $v/2$) | envelope FWHM |
| signal-to-noise | dB | $20\log_{10}$ of an amplitude ratio |
| time dip | $\mathrm{ns\,m^{-1}}$ | $2\sin\theta/v$ |
| imaged dip | deg | $\arcsin((v_{\text{mig}}/v)\sin\theta)$ |

Two conventions to keep straight: a pulse width in nanoseconds converts to depth
by $v/2$ (two-way), and a signal-to-noise ratio in dB uses $20\log_{10}$ for
amplitudes.

## 9. Python demonstration

`code/gpr_processing_demo.py` prints everything above:

1. builds a trace with a drift and measures the zero-crossing delay
   ($442\ \mathrm{ps}$) and amplitude-ratio bias ($+28.8\%$) before and after
   dewow;
2. compares an unprocessed trace, a constant gain and an AGC on the same
   amplitude ratio and its noise;
3. measures the signal-to-noise gain and pulse broadening of a band-pass filter;
4. builds a dipping reflector section and compares the apparent dip with the dip
   recovered by migration at three velocities, against (5.3);
5. measures the target-to-clutter ratio before and after a spatial median filter;
6. verifies the migrated apex of a synthetic point target (error $0.00\
   \mathrm{cm}$ in the noise-free case) and the imaged dip against the true
   $20.0^\circ$.

## Mastery checkpoint

Without notes:

> A $200\ \mathrm{MHz}$ profile over $v = 0.09993\ \mathrm{m\,ns^{-1}}$ targets a
> reflector dipping $30^\circ$ at $1.5\ \mathrm{m}$ depth.
> **(a)** Compute the time dip in $\mathrm{ns\,m^{-1}}$ and the depth-converted
> apparent dip.
> **(b)** Compute the dip a migration would produce with a velocity $10\%$ too
> high, using (5.3).
> **(c)** State the depth error at $x = 0$ for that velocity error.
> **(d)** A drift of amplitude $0.2$ is present; estimate the amplitude-ratio bias
> it causes for two reflections with a true ratio of $0.5$, and state what you
> would report.
> **(e)** A colleague applies AGC and then estimates $\alpha$ from the
> amplitude ratio of two reflections. State what their estimate measures.

Parts (a)–(e) are worked in
[`exercises/02-gpr-processing-solutions.md`](./exercises/02-gpr-processing-solutions.md).

## Common pitfalls

1. **Applying gain before dewow.** The drift is then amplified and multiplied into
   the data.
2. **Using AGC for amplitude work.** It measures the AGC window, not the ground.
3. **Reporting a filter's signal-to-noise gain without its resolution cost.**
   Both are consequences of the same operation.
4. **Reading an unmigrated apparent dip as the true dip.** $\tan\theta_{\text{app}}
   = \sin\theta$ is a $10$–$30\%$ effect at moderate dips.
5. **Attributing a wrong migrated dip entirely to velocity.** Aperture truncation
   and a wrong datum do the same thing.
6. **Background-removing a flat-lying target.** The filter removes what is
   laterally coherent, and a flat reflector is exactly that.
7. **Believing a short processing sequence is a neutral one.** Each omitted step
   is an unstated assumption.

## Related modules

- [10-02-01 Survey Design](01-gpr-survey-design.md) — where the parameters that
  processing depends on are chosen.
- [10-02-03 Velocity Analysis and Common-Midpoint Sounding](03-gpr-velocity-analysis.md) —
  how the migration velocity of Section 5 is obtained rather than assumed.
- [10-02-04 3-D GPR Imaging and Time Slices](04-gpr-3d-imaging.md) — the same
  steps applied to a cube.
- [05-06 Processing Principles](../../05-core-geophysics/06-data-processing-principles/README.md) —
  the general framework, including processing transparency.
- [06-09-04 Migration and Imaging](../../06-seismology/09-reflection-seismology/04-migration-imaging.md) —
  the seismic treatment of the same operators.

Materials: [`code/gpr_processing_demo.py`](./code/gpr_processing_demo.py),
[`exercises/02-gpr-processing-exercises.md`](./exercises/02-gpr-processing-exercises.md),
[`exercises/02-gpr-processing-solutions.md`](./exercises/02-gpr-processing-solutions.md).
