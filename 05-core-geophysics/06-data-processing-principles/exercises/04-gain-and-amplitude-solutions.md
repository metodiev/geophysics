# Solutions — 05-06-04 Gain Control, Amplitude Recovery and True-Amplitude Handling

> **Read this after attempting the exercises, not before.**

---

## ★1 — Geometric spreading

Energy conservation: the power through a sphere of radius $r$ is constant, and the area
is $4\pi r^{2}$, so the intensity falls as $r^{-2}$ and the **amplitude** as
$r^{-1}$ — equation (1) of the lesson. For a line source the wavefront is cylindrical
with area $2\pi r$ (per unit length), so the intensity falls as $r^{-1}$ and the
amplitude as $r^{-1/2}$ — equation (2). The square root appears because amplitude is
the square root of intensity.

---

## ★2 — Absorption

$$A = \exp\!\left(-\frac{\pi \times 30 \times 1.5}{60}\right)
= \exp(-\pi \times 0.75) = \exp(-2.356) = \boxed{0.0948}.$$

Only 9.5 % of the amplitude survives 1.5 s at $Q = 60$ and 30 Hz — which is why the
same $Q$ at 60 Hz would leave only 0.9 %.

---

## ★3 — Correction and normalisation

- A **correction** removes a physically modelled effect with measurable parameters and
  is reversible in principle: time-dependent gain for spreading and absorption.
- A **normalisation** divides by a quantity computed from the data itself (a running
  RMS, a per-trace RMS), and is therefore not invertible because the divisor is not
  recorded: AGC.

---

## ★4 — The gain factor

$$\frac{3}{0.2}\exp\!\left(\frac{\pi \times 25 \times 3}{100}\right)
= 15 \times \exp(2.356) = 15 \times 10.55 = \boxed{158.2}.$$

A factor 158 applied to a late sample — with the same factor applied to the noise.

---

## ★5 — Why the S/N cannot improve

The correction multiplies signal and noise by an identical frequency- and
time-dependent factor, so their ratio is unchanged at every instant. An amplitude
correction preserves ratios; it does not create signal.

---

## ★★6 — Apparent and true ratios

**(a)** Apparent ratio $= 0.30/0.003 = \boxed{100}$.

**(b)** The decay model gives, for the two times,
$\text{decay}(0.5) = (0.2/0.5)\exp(-\pi\cdot30\cdot0.5/90) = 0.4 \times 0.5924 = 0.23696$
and
$\text{decay}(3.0) = (0.2/3.0)\exp(-\pi\cdot30\cdot3.0/90) = 0.066667\times0.04321
= 0.002881$. So the true coefficient ratio is
$0.30/0.23696 \div 0.003/0.002881 = 1.2660 / 1.0413 = \boxed{1.216}$ — i.e. the two
coefficients are nearly equal, and the apparent factor of 100 is almost entirely
propagation.

**(c)** An interpreter reading the raw amplitudes would conclude that the deep event
is 100× weaker in reflectivity, i.e. that the lithology changes drastically or that
the deep event is a different rock type. The correct conclusion is the opposite: the
two events have **comparable** reflectivity, and the amplitude difference is
propagation. Interpreting amplitude without a decay correction is the most common
error in amplitude work.

---

## ★★7 — A wrong $Q$ in a true-amplitude correction

**(a)** The correction divides by $\exp(-\pi f t/Q_{\text{assumed}})$, so the error
factor is

$$\frac{\exp(-\pi f t/Q_{\text{true}})}{\exp(-\pi f t/Q_{\text{assumed}})}
= \exp\!\left[-\pi f t\left(\frac{1}{80}-\frac{1}{120}\right)\right]
= \exp\!\left[-\pi \times 25 \times 3.5 \times 4.16667\times10^{-3}\right]$$
$$= \exp(-1.1454) = \boxed{0.318} .$$

The amplitude is wrong by a factor 0.32 — a **−68 % error**, larger than the
lithological changes the survey is trying to measure.

**(b)** A **bias**: it is systematic in time and identical on every trace, so it does
not average out and does not appear in any repeatability measure.

**(c)** The assumed $Q$ and its *source* (measured, from a VSP, or assumed as a
literature range), the frequency at which the correction was applied, the reference
time, the spreading law used, and the resulting amplitude uncertainty. Without these
the quoted amplitudes are not interpretable — see
[05-06-06](../06-processing-transparency.md).

---

## ★★8 — Wrong dimensionality of spreading

**(a)** Using $1/t$ where $1/\sqrt{t}$ is correct applies an extra factor
$\sqrt{t}$; over a factor 10 in time that is
$\sqrt{2.5/0.25} = \sqrt{10} = \boxed{3.16}$.

**(b)** The absorption term over the same interval at $Q = 80$, 25 Hz:
$\exp(-\pi\cdot25\cdot(2.5-0.25)/80) = \exp(-2.209) = 0.1098$, i.e. a factor 9.1 of
*differential* attenuation between the two times. So the dimensionality error (3.16)
is about a third of the absorption effect (9.1) — smaller, but of the same order, and
much easier to get right.

**(c)** Fix the **dimensionality first**, because it is a modelling error that costs
nothing to correct once the geometry is known, whereas refining $Q$ requires a
measurement (VSP, spectral ratio) and carries its own uncertainty. Correcting the
smaller-but-cheap error first is the general rule: a 3× error from a wrong model
swamps a 10 % error from a better $Q$ estimate.

---

## ★★9 — Quoting a relative amplitude

**(a)** From the lesson's S/N table, the events' pre-correction S/N values are
717.43, 40.82, 4.87, 0.66, 0.07, 0.01 at $t$ = 0.2, 0.45, 0.8, 1.2, 1.7, 2.3 s. A
ratio is meaningfully measurable only where both events have S/N comfortably above 1,
so the **latest usable time is about 0.8 s** in this synthetic trace, and the ratio
must involve events at or above that quality.

**(b)** The ratio must be accompanied by (i) the signal-to-noise at which each event
was measured, and (ii) the complete amplitude-processing description — the decay model
(spreading dimension, $Q$ and its source), the reference time, and confirmation that
no AGC or trace normalisation was applied. A ratio from AGC-processed data is not a
measurement at all (measured error −54.3 % in the lesson).

**(c)** At S/N = 0.7 the measured amplitude is dominated by noise, so the ratio can
take almost any value; quoting it as a measurement would be reporting a random number
as a rock property. The honest statement is that event B's amplitude is below the
detection threshold of this dataset.

---

## ★★★10 — Surface-consistent scaling

A satisfactory implementation:

1. Model $\ln A_{ij} = \ln s_i + \ln r_j + \ln g_k + \ln m_l$ with $k$ an offset
   class and $l$ the (wanted) reflectivity, which is treated as a nuisance parameter.
2. Assemble the linear system in the log domain with one row per trace and solve by
   least squares; regularise towards zero to stabilise poorly covered factors.
3. **Expected result:** the recovered $s_i$ and $r_j$ match the true factors up to a
   single multiplicative constant, as the lesson states — because
   $s_i \to c\,s_i$, $r_j \to r_j/c$ leaves $A_{ij}$ unchanged. Enforce
   $\sum_i \ln s_i = 0$ (or an equivalent gauge) to remove the null direction.
4. **Recovery error vs number of traces:** falls as the coverage per factor grows;
   report the RMS error in $\ln s_i$ against the number of traces per source.
5. **Ill-conditioning:** when some source or receiver position appears in very few
   traces, its factor is poorly constrained and couples to the offset classes; the
   problem becomes ill-conditioned exactly as in
   [05-06-02](../02-noise-suppression.md), and the residual does not fall with more
   regularisation. The practical fix is to constrain or drop such positions and to
   report which were dropped.

---

## ★★★11 — Recovering a lithological amplitude anomaly

A satisfactory experiment builds a reflector whose coefficient increases by 30 % over
a 200 m interval at a chosen two-way time, then applies each scheme and measures the
recovered contrast:

| scheme | recovered contrast (% of true) | usable to |
|---|---|---|
| no gain | the *shape* is right but the measurement is dominated by the near-trace display problem; a 30 % change at 2 s is below the visual dynamic range | shallow only (~0.5 s) |
| $t$-gain | recovers most of the geometric term, so the contrast is recovered to within the residual absorption error — order tens of per cent | ~1 s |
| AGC | the contrast is systematically compressed; 30 % may appear as 10–15 % | not usable for amplitude |
| true amplitude | recovers the contrast to within the $Q$ uncertainty | to the S/N limit |

The depth range is set in every case by the *pre-correction S/N* — the lesson's
measured column shows S/N = 0.66 at 1.2 s in a synthetic trace with modest noise, so
beyond that time no scheme recovers anything. The honest conclusion: **the usable
depth range is a property of the data's S/N, not of the gain scheme.**

---

## ★★★12 — Testing the "it is noise" claim

A satisfactory experiment scales the noise and reports:

| noise factor | input noise | measured ratio error (%) |
|---|---|---|
| 1 | 0.0008 | −13.7 (the lesson's value) |
| 1/2 | 0.0004 | smaller |
| 1/4 | 0.0002 | smaller again |
| 1/10 | 0.00008 | smaller again |

The errors should fall roughly in proportion to the noise, because the fourth event's
recovered amplitude is dominated by the amplified noise near its time (amplitudes
0.23273 measured against a true 0.20). Extrapolating to zero noise, the ratio error
should tend to a **small residual**, and identifying that residual is the point of the
question: it is *not* zero in general, because

- the peak-picking window has finite width and the wavelet is not perfectly isolated;
- neighbouring events overlap at late times, so the "peak" near event 4 includes
  contributions from event 3's tail;
- the convolution of the ideal model with the discrete grid introduces a small
  time-quantisation error.

So the honest two-part conclusion is: **most of the measured −13.7 % is noise (it
scales with the noise), and a small residual is a modelling artefact of measuring a
peak in a finite window.** The experiment distinguishes them by the scaling, which is
exactly the diagnostic that a single experiment cannot provide.
