# Solutions — 20-03-04 Phase Response, Zero-Phase Filtering and Distortion

> **Read after attempting the exercises.** Lesson:
> [04 Phase Response and Zero-Phase Filtering](../04-phase-and-zero-phase.md).

---

## ★1 — Group delay of a 201-tap linear-phase FIR

$$\tau_g = \frac{N-1}{2} = \frac{201-1}{2} = 100\ \text{samples}.$$

In time: $100/400\ \mathrm{Hz} = 0.25$ s $= 250$ ms.

---

## ★2 — Group delay and dispersionlessness

$$\tau_g(\omega) = -\frac{\mathrm{d}\phi(\omega)}{\mathrm{d}\omega}.$$

Dispersionless means $\tau_g$ is constant over the band, i.e. the phase is a
linear function of frequency (linear phase). A filter with constant group delay
delays every frequency equally and therefore preserves waveform shape.

---

## ★3 — Forward-backward filtering

- **Phase**: the total response is $H H^{*} = |H|^2$, a positive real number, so
  the phase is exactly zero at every frequency.
- **Magnitude**: the response is squared, so every value in dB is doubled: a
  $-3.01$ dB cutoff becomes $-6.02$ dB, and roll-off is twice as steep.

---

## ★4 — Differential delay from the table

$$17.395 - 10.155 = 7.240\ \text{samples} = \frac{7.240}{1000}\ \mathrm{s}
= 7.24\ \mathrm{ms}.$$

A broadband wavelet spanning both frequencies is dispersed over about 7 ms: its
high-frequency content arrives measurably later than its low-frequency content.
For a converted-phase or AVO measurement, where waveform shape *is* the signal,
this distortion is indistinguishable from a real physical dispersion unless it is
removed.

---

## ★5 — Attenuation after `filtfilt`

Causal: $-3.01$ dB, amplitude ratio $10^{-3.01/20} = 0.7071$.
Forward-backward: $-6.02$ dB, amplitude ratio $10^{-6.02/20} = 0.5000$.

The amplitude ratio is halved, not quartered: squaring the *amplitude* gives
$(0.7071)^2 = 0.5$, and squaring the value in **dB** gives double the dB. Reading
$-6.02$ dB as a factor of four is the standard error.

---

## ★6 — Why a shift cannot fix asymmetry

A constant time shift adds $-\omega\tau_0$ to the phase, which changes the
*slope* of the phase but not its curvature. Dispersion is curvature: different
frequencies are delayed by different amounts. Shifting the whole record moves
every frequency by the same amount and therefore cannot re-align components that
were delayed unequally. The correct correction is either the inverse phase
$\phi^{-1}$ or, equivalently and more simply, zero-phase filtering. The measured
growth of the envelope skew from 0.0092 to 0.0233 is exactly this curvature made
visible.

---

## ★★7 — Two different filters

Filtering forward with $H_1$, reversing, filtering with $H_2$, and reversing back
gives

$$H_{\text{total}}(e^{i\omega}) = H_1(e^{i\omega})\,H_2(e^{-i\omega}).$$

The phase is $\phi_1(\omega) - \phi_2(\omega)$. It vanishes for all $\omega$ only
if $\phi_1 = \phi_2$ (identical filters), or more weakly if $H_1$ and $H_2$ are
both real and positive (zero-phase each). If $|H_1| = |H_2|$ but their phases
differ, the total magnitude is $|H|^2$ with a residual phase
$\phi_1 - \phi_2 \ne 0$: **matched magnitudes are not sufficient for zero phase.**
The practical conclusion is that the two passes must use the same coefficients.

---

## ★★★8 — Picking an onset with zero-phase filtering

The problem: `filtfilt` runs the filter backwards as well, so energy arrives
*before* the physical onset by roughly the filter's group delay, which biases an
onset pick early.

Remedies:

1. **Causal filtering plus an explicit group-delay correction.** Filter forward
   only, then subtract $\tau_g$ from the pick time. The correction is exact if the
   phase is linear; for an IIR filter it is approximate, so use an FIR or measure
   $\tau_g$ at the dominant frequency.
2. **Pad the record** with synthetic noise (matched to the record's statistics)
   before `filtfilt` and discard the padding afterwards. The reverse pass then
   operates on the padding, and the pre-onset artifact is pushed into the part that
   is thrown away. The artifact introduced is that the padding's statistics must be
   realistic; a constant or zero pad creates a step that the filter rings on.
3. **Design a minimum-phase filter** for the onset work. A minimum-phase filter is
   causal and front-loaded, so it does not smear energy before the onset, at the
   cost of a non-linear phase across the band.

All three trade one artifact for another. The choice depends on which is more
harmful: an early bias (remedy 1), a need for realistic padding statistics
(remedy 2), or a dispersed waveform (remedy 3).