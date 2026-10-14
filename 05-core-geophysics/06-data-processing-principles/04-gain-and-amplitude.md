---
id: 05-06-04
title: "Gain Control, Amplitude Recovery and True-Amplitude Handling"
level: advanced
prereqs: ["05-06-01", "02-03-10"]
tags: [gain, agc, spherical-divergence, absorption, true-amplitude, ava]
---

# Gain Control, Amplitude Recovery and True-Amplitude Handling

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the geometric-spreading amplitude decay for two- and three-dimensional
   wave propagation, and state which applies to a given geometry.
2. **Derive** the absorption term $\exp(-\pi f t/Q)$ and evaluate it for a stated
   $Q$.
3. **Distinguish** display gain, automatic gain control (AGC) and a physically based
   amplitude correction, and state what each preserves and destroys.
4. **Measure** the relative-amplitude error of a synthetic marker under each scheme,
   and state which scheme is admissible for quantitative interpretation.
5. **Explain** why an amplitude correction cannot improve signal-to-noise, and use the
   pre-correction S/N to state the depth beyond which relative amplitudes are
   unusable.
6. **Specify** the information a true-amplitude processing report must contain.

## Prerequisites

- [05-06-01 The Processing Pipeline](./01-processing-pipeline-concept.md) — where
  amplitude handling sits in the sequence.
- [02-03-10 Attenuation, Absorption and the Quality Factor Q](../../02-physics/03-oscillations-and-waves/10-attenuation.md)
  — the physical origin of the absorption term used here.
- [05-04-06 Attenuation and Velocity Dispersion in Rocks](../04-rock-physics/06-attenuation-dispersion-rock.md)
  — the measured $Q$ values that make the absorption term large.

## 1. Intuition: amplitude is the only quantitative observable in a seismic section

Travel times give structure; **amplitudes give rock properties**. Reflection
coefficients, acoustic impedance, fluid content and AVA (amplitude-versus-angle)
behaviour all live in the amplitudes of the recorded wavefield. Every gain applied to
the data therefore either preserves those ratios or destroys them.

The distinction that organises this lesson is between two kinds of gain:

- **A correction** removes a known, physically modelled effect: geometric spreading,
  absorption, transmission loss, the instrument's own response, source and receiver
  coupling. It is reversible in principle, and its parameters are measurable.
- **A normalisation** forces every part of the record into a similar amplitude range:
  AGC, per-trace scaling to a common RMS, and most display gains. It is not
  reversible, because the factor applied to each sample depends on the data around
  it, and it therefore *removes exactly the amplitude information the data carries*.

Both have legitimate uses. The error is to apply the second and then interpret
amplitudes as if the first had been done.

## 2. Derivation: how amplitude decays with time

### 2.1 Geometric spreading

For a wave expanding from a point source, the energy crossing a surface of area
$4\pi r^{2}$ is conserved, so the energy density falls as $r^{-2}$ and the **amplitude**
falls as $r^{-1}$:

$$A_{\text{3D}}(r) \propto \frac{1}{r} = \frac{1}{vt} ,
\tag{1}$$

using the two-way travel time $t$ and an average velocity $v$ (absorbing the factor 2
into the units of $v$). For a **line** source, or for a wavefront that is effectively
cylindrical (a refraction along a line, a borehole source, or a 2-D modelling
problem), the energy spreads over a cylinder of area $2\pi r$, so

$$A_{\text{2D}}(r) \propto \frac{1}{\sqrt{r}} = \frac{1}{\sqrt{vt}} .
\tag{2}$$

Equations (1) and (2) are **different by a square root**, and using the wrong one is a
systematic, depth-dependent amplitude error — the subject of Section 5.

### 2.2 Absorption

Attenuation in a linear viscoelastic medium is described by the quality factor $Q$.
Over a travel time $t$ at frequency $f$, the amplitude is reduced by

$$A_{\text{abs}}(f,t) = \exp\!\left(-\frac{\pi f t}{Q}\right),
\tag{3}$$

so that the loss depends on *frequency times time*, not on either alone. This is why
absorption is the fundamental limit on the bandwidth of a deep reflection: at fixed
$Q$, doubling the travel time halves the frequency that survives a given attenuation.

### 2.3 Combined decay factor

Combining Section 2.1 and equation (3) with a reference time $t_0$ gives the model
used in the demonstration:

$$A(t, f) = \frac{t_0}{t}\exp\!\left(-\frac{\pi f t}{Q}\right).
\tag{4}$$

Formula (4) is the *model*; in practice its parameters ($v$ as a function of time,
$Q$, and the transmission losses) are estimated, and the honest correction uses the
estimate with its uncertainty, not a nominal curve.

## 3. The three schemes, and what each measures

| scheme | factor applied to sample at time $t$ | preserves relative amplitude? | admissible for AVA / impedance? |
|---|---|---|---|
| **no gain** | 1 | yes, but the record is dominated visually by the near trace | amplitudes are correct but unreadable |
| **$t^{n}$ gain / physical recovery** | $\dfrac{t}{t_0}\exp\!\left(+\dfrac{\pi f t}{Q}\right)$ per frequency | **yes**, to the accuracy of the model | yes, with the model stated |
| **AGC** | $\dfrac{1}{\sqrt{\langle y^{2}\rangle_{W}(t)}}$ over a window $W$ | **no** | never |
| **trace normalisation** | $\dfrac{1}{\operatorname{RMS}(y)}$ per trace | no, if traces differ | only if every trace is known to have the same energy |

**AGC** computes a running RMS in a window and divides by it, which equalises the
envelope by construction. Its purpose is to make weak events visible on a plot; its
side effect is to make every event look equally strong, which is precisely the
information a quantitative interpreter needs.

## 4. Measured: what each scheme does to a known reflectivity

[`code/gain_amplitude_demo.py`](./code/gain_amplitude_demo.py) builds a synthetic trace
with six known reflection coefficients, a 25 Hz Ricker wavelet, and the decay of
equation (4) with $Q = 80$ at a reference time of 0.2 s (*SYNTHETIC* throughout).

| $t$ (s) | true coefficient | decay factor | expected amplitude |
|---|---|---|---|
| 0.20 | 0.85 | 0.82172 | 0.69847 |
| 0.45 | 0.40 | 0.28573 | 0.11429 |
| 0.80 | −0.30 | 0.11398 | −0.03420 |
| 1.20 | 0.20 | 0.05131 | 0.01026 |
| 1.70 | −0.12 | 0.02217 | −0.00266 |
| 2.30 | 0.07 | 0.00909 | 0.00064 |

The recovered peak amplitude of each event under the four schemes:

| $t$ (s) | no gain | $t$-gain | AGC | true amplitude | true coefficient |
|---|---|---|---|---|---|
| 0.20 | 0.69732 | 0.13946 | 5.77319 | 0.84860 | 0.85 |
| 0.45 | 0.11478 | 0.05165 | 5.79769 | 0.40171 | 0.40 |
| 0.80 | −0.03439 | −0.02751 | −5.70997 | −0.30172 | −0.30 |
| 1.20 | 0.01198 | 0.01436 | 6.33801 | 0.23273 | 0.20 |
| 1.70 | −0.00319 | −0.00540 | −3.46617 | −0.14279 | −0.12 |
| 2.30 | −0.00164 | −0.00370 | −2.31223 | 0.18389 | 0.07 |

The true-amplitude column tracks the coefficient column closely for the first three
events and diverges at the last two. The relative-amplitude test makes the comparison
quantitative — the ratio of event 2 (0.40) to event 4 (0.20), whose true value is
2.000:

| scheme | measured ratio | error |
|---|---|---|
| no gain | 9.577 | +378.8 % |
| $t$-gain | 3.597 | +79.9 % |
| AGC | 0.915 | −54.3 % |
| true amplitude | 1.726 | −13.7 % |

Three conclusions, each a design requirement:

1. **The uncorrected record overstates the ratio by a factor 4.8.** Any interpretation
   of relative amplitude from raw amplitudes is wrong by hundreds of per cent.
2. **A simple $t$-gain removes the geometric term but not the absorption**; the
   residual error is +79.9 %. Half a correction is not half an answer.
3. **AGC gives the wrong answer in the other direction** (−54.3 %), and it does so
   *systematically*: it always compresses the dynamic range towards unity.

### 4.1 The −13.7 % residual is noise, not a method failure

The true-amplitude correction applies the factor $(t/t_0)\exp(+\pi f t/Q)$ and the
noise is multiplied by the same factor. The signal-to-noise ratio of an *event* is
therefore unchanged by the correction, and it can be quoted directly:

| $t$ (s) | gain factor applied | true amplitude | amplified noise | event S/N |
|---|---|---|---|---|
| 0.20 | 1.22 | 0.69847 | 0.00097 | 717.43 |
| 0.45 | 3.50 | 0.11429 | 0.00280 | 40.82 |
| 0.80 | 8.77 | 0.03420 | 0.00702 | 4.87 |
| 1.20 | 19.49 | 0.01026 | 0.01559 | 0.66 |
| 1.70 | 45.11 | 0.00266 | 0.03609 | 0.07 |
| 2.30 | 109.99 | 0.00064 | 0.08799 | 0.01 |

**Beyond about 1.2 s the fourth event's amplitude is below the noise, before and after
the correction.** The measured ratio of 1.726 instead of 2.000 is therefore the honest
consequence of measuring an event with S/N below 1, not a defect of the correction. A
processing report that quotes relative amplitudes must quote the S/N at which they
were measured; a ratio measured at S/N = 0.7 is not a measurement.

## 5. The 2-D versus 3-D trap

Equations (1) and (2) differ by a square root, and the choice is made by the
*acquisition and processing geometry*, not by preference:

| situation | correct spreading | note |
|---|---|---|
| point source, receivers on a surface, 3-D wavefield | $1/t$ | the default for a 3-D survey |
| line source, or a 2-D modelled dataset | $1/\sqrt{t}$ | a 2-D migration or modelling exercise |
| long receiver line, far offsets, single line | between the two | the effective dimension of the wavefield changes with offset |

The practical consequence is measurable: applying a $t$-gain where $1/\sqrt{t}$ is
correct multiplies the late events by an extra factor $t^{1/2}$. Over the range
$t = 0.2$ s to $t = 2.3$ s that is a factor $\sqrt{2.3/0.2} = 3.4$ — a 240 % error
in the ratio of the last event to the first, several times larger than the error the
absorption term contributes at $Q = 80$. **Get the dimension right before refining the
$Q$.**

## 6. Absorption, measured

The demo evaluates equation (3) at the wavelet's dominant frequency of 25 Hz:

| $t$ (s) | $Q = 40$ | $Q = 80$ | $Q = 200$ |
|---|---|---|---|
| 0.5 | 0.3747 | 0.6121 | 0.8217 |
| 1.0 | 0.1404 | 0.3747 | 0.6752 |
| 2.0 | 0.0197 | 0.1404 | 0.4559 |
| 4.0 | 0.0004 | 0.0197 | 0.2079 |

Over 4 s at $Q = 40$ only 0.039 % of the amplitude survives; at $Q = 200$, 20.8 %
survives. Since $Q$ for sedimentary rocks is typically in the tens to low hundreds
(see [05-04-06](../04-rock-physics/06-attenuation-dispersion-rock.md) for how it is
measured), the uncertainty in $Q$ is the dominant uncertainty in a deep
amplitude correction — much larger than the geometric term's uncertainty. A
true-amplitude correction that quotes a $Q$ without its uncertainty has not stated its
own error bar.

## 7. Surface-consistent scaling: the multiplicative error no gain removes

Sections 2–4 correct a *time-dependent* effect that is common to the whole survey.
Real data also carry *per-trace* multiplicative errors: source coupling, receiver
coupling, geophone or hydrophone sensitivity, instrument gain settings and near-surface
transmission losses. These vary from trace to trace and do not depend on time, so no
time-dependent gain can remove them.

The standard model writes the amplitude of trace $(i,j)$ as a product of factors

$$A_{ij} = s_i\,r_j\,g_k\,m_l ,
\tag{5}$$

where $s_i$ is the source factor, $r_j$ the receiver factor, $g_k$ a factor for the
offset or ray-parameter class, and $m_l$ the (wanted) reflectivity. Taking logarithms
turns the product into a sum, and the factors can then be estimated by an
over-determined least-squares fit over the whole survey — this is what
*surface-consistent amplitude scaling* means. Two practical points follow:

- **The decomposition is only identifiable up to a constant**, because multiplying all
  $s_i$ by $c$ and dividing all $r_j$ by $c$ leaves $A_{ij}$ unchanged. The absolute
  amplitude level is therefore set by an external constraint, exactly as a datum set the
  absolute travel time in [05-06-03](./03-static-and-datum.md).
- **A surface-consistent fit is a large, sparse inverse problem**, and it inherits the
  ill-posedness of Section 6 of
  [05-06-02](./02-noise-suppression.md): with sparse coverage the factors are poorly
  determined, and the solution must be regularised towards a smooth or zero model.

The honest diagnostic is the *residual* after scaling: if the per-trace amplitude
scatter is not reduced, the factors were not the dominant term, and the correction has
added a parameterisation without removing an error. Reporting the scatter before and
after is the same two-number discipline as in Sections 2 and 4.

## 8. Assumptions

1. **A single decay model applies to the whole trace.** Equation (4) uses one $Q$ and
   one velocity function; a laterally varying near surface or a strong velocity
   contrast invalidates it, and the error appears as an amplitude anomaly that can
   mimic a lithological change.
2. **Two-way, primary-only propagation.** Multiples have their own (larger) decay and
   are not corrected by a primary model.
3. **Source and receiver coupling and instrument response are constant.** Their
   variation is a *multiplicative* error per trace, which no time-dependent gain
   removes; it must be corrected separately, by surface-consistent scaling.
4. **No clipping.** A clipped or over-ranged trace has lost its amplitude information
   irreversibly, and a gain applied to it amplifies a flat top.
5. **AGC window much longer than the wavelet.** Otherwise the window follows the
   wavelet itself and the "gain" is a non-linear distortion of each event.
6. **Synthetic parameters.** Coefficients, $Q$ and noise in Sections 4–6 are stated
   synthetic values.

## 9. Units and dimensional analysis

Equation (1): $[1/t] = \mathrm{s^{-1}}$ and $[1/r] = \mathrm{m^{-1}}$, so the
amplitude is in whatever units the $1/r$ scaling is referred to — a *relative*
amplitude has no unit and the choice of reference length cancels. Equation (2):
$[1/\sqrt{t}] = \mathrm{s^{-1/2}}$, which is why the two schemes cannot be
interchanged without tracking the reference.

The argument of the exponential in equation (3) must be dimensionless:
$[\pi f t/Q] = \mathrm{s^{-1}\cdot s} = 1$, with $Q$ dimensionless (the standard
definition of $Q$ is an energy ratio per cycle). The gain factors in Section 4.1 are
dimensionless by construction, and the noise column in that table is in the same
units as the trace because it is the input noise multiplied by a dimensionless gain.

## 10. Python demonstration

[`code/gain_amplitude_demo.py`](./code/gain_amplitude_demo.py) produces every number in
Sections 4–6. The AGC is the operator to be suspicious of, and it is four lines:

```python
def agc(y, window_s, dt):
    w = int(window_s / dt)
    power = np.convolve(y ** 2, np.ones(w) / w, mode="same")
    return y / np.sqrt(power + 1e-30)
```

The `+1e-30` is a guard against dividing by zero in a quiet window; it also shows why
AGC is not invertible — the divisor depends on the data in a neighbourhood that is not
recorded with the output.

## 11. Exercises, common mistakes, applications

Companion problem sets:
[`exercises/04-gain-and-amplitude-exercises.md`](./exercises/04-gain-and-amplitude-exercises.md)
and [`exercises/04-gain-and-amplitude-solutions.md`](./exercises/04-gain-and-amplitude-solutions.md).

### Common mistakes

1. **Interpreting relative amplitudes from AGC'd data.** Measured error −54.3 % in the
   demonstration, and always in the direction of compressing the range.
2. **Applying a $t$-gain and calling it a true-amplitude correction.** The measured
   residual is +79.9 %.
3. **Using 3-D spreading for a 2-D dataset.** A factor $t^{1/2}$, which reaches 3.4 over
   the range of one trace.
4. **Quoting a $Q$ without its uncertainty.** Section 6 shows how fast the term grows
   with depth and how strongly it depends on $Q$.
5. **Applying a gain before the edit and before stacking.** A gain applied first
   amplifies spikes and changes the relative weights of the traces being stacked.
6. **Quoting a relative amplitude without the S/N.** Section 4.1.

### Real-world applications

- **AVA and impedance inversion.** Both require amplitudes whose ratios are physically
  meaningful, which is the definition of true-amplitude processing. The report must
  list every gain applied.
- **Amplitude-versus-offset fluid detection.** The signal is a *change* of amplitude
  with offset of a few tens of per cent; a residual gain error of 79 % makes the
  method meaningless.
- **Time-lapse (4-D) seismic.** Non-repeatable gain is one of the largest sources of
  4-D noise; the correction must be applied identically to every epoch.
- **Potential fields.** The analogue is the removal of the known source-geometry
  falloff before interpretation — for example continuing to a common level rather
  than comparing raw amplitudes at different heights
  ([05-06-05](./05-merge-and-regularisation.md)).

## 12. Further reading

- **Yilmaz, Ö. (2001). *Seismic Data Analysis* (2nd ed.). SEG.** Chapters on gain,
  amplitude recovery and true-amplitude processing; the practitioner's reference.
- **Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press.** Amplitude and attenuation in the reflection chapter.
- **Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.). University
  Science Books.** The derivation of geometric spreading and anelastic attenuation
  from the elastodynamic equations. Level: advanced.
- **Johnston, D. H., & Toksöz, M. N. (1981). *Seismic Wave Attenuation*. SEG
  Geophysical Reprint Series.** The classic compilation of $Q$ measurements, useful for
  choosing a defensible range. Level: advanced.
- **USGS earthquake and seismic-hazard pages** — <https://earthquake.usgs.gov> — for
  documented $Q$ and attenuation models in specific regions.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text, and you should
> confirm current availability and editions through your library before citing them.

## 13. Related lessons

- [05-06-01 The Processing Pipeline](./01-processing-pipeline-concept.md) — the order in which gains may be applied.
- [05-06-02 Noise Suppression](./02-noise-suppression.md) — why the S/N column of Section 4.1 cannot be improved by a gain.
- [05-06-03 Static Corrections, Datum and Elevation Effects](./03-static-and-datum.md) — the other correction that protects the stack.
- [05-06-06 Documenting Processing: Reproducibility in Practice](./06-processing-transparency.md) — recording every gain that was applied.
- [02-03-10 Attenuation, Absorption and the Quality Factor Q](../../02-physics/03-oscillations-and-waves/10-attenuation.md) — where equation (3) comes from.

## 14. Self-assessment checklist

- [ ] I can derive $1/r$ and $1/\sqrt r$ spreading and say which fits a given geometry.
- [ ] I can evaluate the absorption term and state how it depends on $f$, $t$ and $Q$.
- [ ] I can distinguish a correction from a normalisation in one sentence.
- [ ] I can measure the relative-amplitude error of each scheme and say which is admissible.
- [ ] I can explain why an amplitude correction cannot improve S/N.
- [ ] I can state the S/N below which a relative amplitude must not be quoted.
- [ ] I can list the assumptions of the decay model and the error each introduces.
- [ ] I can specify what an amplitude-processing report must contain.
