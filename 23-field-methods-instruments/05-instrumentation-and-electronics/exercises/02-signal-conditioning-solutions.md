# Solutions — 23-05-02 Amplification, Filtering and Analog-Digital Conversion

> Read after attempting. Lesson:
> [02 Signal Conditioning](../02-signal-conditioning.md). All values are
> **SYNTHETIC**.

---

## ★1 — The noise-figure optimum

The noise figure is the total input-referred noise divided by the source's own
thermal noise:

$$F = \frac{e_n^{2} + (i_n R)^{2} + 4kTR}{4kTR} .$$

Differentiating with respect to $R$ and setting the derivative to zero gives

$$R_{\text{opt}} = \frac{e_n}{i_n}
= \frac{5\times10^{-9}\ \mathrm{V/\sqrt{Hz}}}{0.5\times10^{-12}\ \mathrm{A/\sqrt{Hz}}}
= 1.0\times10^{4}\ \Omega = 10\ \mathrm{k\Omega}.$$

Units: V/√Hz divided by A/√Hz gives V/A = Ω. The same relation applies to the
demonstration's amplifier ($10\ \mathrm{nV/\sqrt{Hz}}$, $1\ \mathrm{pA/\sqrt{Hz}}$)
which gave 10 kΩ, and it is the reason a low-current-noise (FET input) amplifier is
used with high-impedance sources and a low-voltage-noise (bipolar) amplifier with
low-impedance ones.

---

## ★2 — Input-referred noise at 10 kΩ

Three contributions, each as a spectral density:

$$e_n^{2} = (5\times10^{-9})^{2} = 2.5\times10^{-17}\ \mathrm{V^{2}/Hz},$$

$$(i_n R)^{2} = (0.5\times10^{-12} \times 10^{4})^{2} = (5\times10^{-9})^{2}
= 2.5\times10^{-17}\ \mathrm{V^{2}/Hz},$$

$$4kTR = 4 \times 1.380649\times10^{-23} \times 300 \times 10^{4}
= 1.65678\times10^{-16}\ \mathrm{V^{2}/Hz}.$$

$$v_{\text{in}} = \sqrt{2.5 + 2.5 + 16.5678}\times10^{-17}
= \sqrt{21.5678\times10^{-17}} = 1.4694\times10^{-8}\ \mathrm{V/\sqrt{Hz}}
= 14.69\ \mathrm{nV/\sqrt{Hz}}.$$

Note that the **source's own thermal noise dominates** (16.57 of 21.57 in units of
$10^{-17}$ V²/Hz, i.e. 77 % of the variance) even at the noise-figure optimum. That
is the definition of a good amplifier: at $R_{\text{opt}}$ the added noise is
comparable with the source noise and the noise figure is near its minimum. At
$R \ll R_{\text{opt}}$ the amplifier's voltage noise dominates; at
$R \gg R_{\text{opt}}$ its current noise does.

---

## ★★3 — Two-stage noise figure

$$F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1}
= 2 + \frac{10 - 1}{50} = 2 + 0.18 = 2.18 .$$

$$\text{NF} = 10\log_{10}(2.18) = 3.38\ \mathrm{dB}.$$

**Reversed** ($F_1 = 10$, $G_1 = 50$, $F_2 = 2$):

$$F_{\text{total}} = 10 + \frac{2 - 1}{50} = 10.02 \quad\Rightarrow\quad
\text{NF} = 10.01\ \mathrm{dB}.$$

**The lesson.** The two configurations use the same parts and differ by 6.6 dB of
noise figure, entirely because of the order. With a 50× (17 dB) first-stage gain,
the second stage's excess noise is divided by 50, so the first stage's noise
essentially *is* the system noise. The design rules follow: put the lowest-noise
stage first, give it as much gain as its bandwidth allows, and treat any loss before
it (a cable, a connector, an attenuator) as a first-stage noise factor equal to its
loss.

---

## ★★4 — ENOB and oversampling

$$\text{ENOB} = \frac{84 - 1.76}{6.02} = \frac{82.24}{6.02} = 13.66\ \text{bits}.$$

**Two more bits** requires 4 more bits of noise reduction, i.e.
$\sqrt{N} = 4 \Rightarrow N = 16$: an **oversampling ratio of 16**, since each
doubling of the rate buys 0.5 bit and 2 bits therefore needs $2^{4} = 16$.

The condition is that the noise being averaged is white and uncorrelated. If the
converter's floor is dominated by a coherent tone (a power-line harmonic, a clock
feedthrough), oversampling does not reduce it at all, and the measured ENOB will not
improve — which is exactly why the improvement must be *measured* after the change,
not assumed from the arithmetic.

---

## ★★★5 — A front end for a 1 kΩ source, 40 Hz band, 18 effective bits

**Amplifier noise requirement.** With $R = 1\ \mathrm{k\Omega}$ at $T = 300$ K the
source's thermal noise is

$$v_{\text{source}} = \sqrt{4kTR} = 4.070\ \mathrm{nV/\sqrt{Hz}}.$$

Over a 40 Hz band the source noise is
$4.070\sqrt{40} = 25.74\ \mathrm{nV}$ rms. For the amplifier's contribution to be
below one third of that in power (so the total rises by less than 0.5 dB), require

$$v_{\text{amp}} \le \frac{25.74}{\sqrt{2}} \approx 18\ \mathrm{nV\ rms}
\quad\Rightarrow\quad e_n \le \frac{18}{\sqrt{40}} = 2.85\ \mathrm{nV/\sqrt{Hz}}
\ \text{(with } i_n R \text{ included)}.$$

So an amplifier with $e_n \approx 2\ \mathrm{nV/\sqrt{Hz}}$ and an $i_n$ small
enough that $i_n \times 1\ \mathrm{k\Omega} < 2\ \mathrm{nV/\sqrt{Hz}}$ (i.e.
$i_n < 2\ \mathrm{pA/\sqrt{Hz}}$) is adequate; a 5 nV/√Hz general-purpose part would
add 0.9 dB of noise figure, which may still be acceptable.

**Gain and staging.** With a $\pm 10$ V converter and a full-scale signal amplitude
chosen so that a 100 mV rms signal fills one third of the range, the required gain is
about $10/(0.1 \times 1.4) \approx 70$, i.e. **40 dB**. Split it: **20 dB in a
low-noise first stage** (which makes the second stage's noise negligible per
Section 3) and **20 dB in a second stage** with the anti-alias filter around it.
Check each stage's gain-bandwidth product against the required 40 Hz band with a
large margin.

**Filter.** 80 dB at $f/f_c = 3$ requires

$$n \ge \frac{80}{20\log_{10}(3)} = \frac{80}{9.5424} = 8.38
\;\Rightarrow\; n = 9 \text{ poles (Butterworth).}$$

A 9-pole passive filter is impractical, so either use an active multi-stage
Butterworth (three 3-pole sections, each buffered and with its own Q) or relax the
transition ratio by sampling faster: at $f/f_c = 10$ the requirement is 4 poles.
Given the low sample rate needed for a 40 Hz band, **sampling at 200 sps and
placing the corner at 40 Hz with a transition ratio of 5 gives a 5-pole requirement**
— a single active stage with a steep roll-off. State the chosen type with its
passband ripple and group-delay behaviour: for a 40 Hz measurement of a waveform,
a Bessel (maximally flat delay) response is often preferable to a Butterworth.

**Sample rate and oversampling.** With the band ending at 40 Hz, sample at
**200 sps** (Nyquist 100 Hz, band-to-Nyquist ratio 0.4, so the 9- or 5-pole filter
has room). To reach 18 effective bits from a converter that measures 16 ENOB at
200 sps, oversample by $2^{2\times2} = 16$, i.e. sample at **3200 sps** and decimate
with a digital filter to 200 sps, buying 4 bits. The digital decimation filter also
provides much of the anti-alias attenuation, which is why the analogue filter can be
relaxed — the standard argument for a high oversampling ratio.

**Checks on the assembled circuit.** (i) Measure the input-referred noise with the
source replaced by a metal-film resistor of the same value, and compare with
$4.070\ \mathrm{nV/\sqrt{Hz}}$ plus the amplifier's specification. (ii) Measure the
frequency response through the whole chain, including the anti-alias filter, with a
sine sweep, and verify the corner and the stopband. (iii) Measure the ENOB of the
assembled front end with a near-full-scale sine (see ★★★6), not the converter alone.
(iv) Check the common-mode rejection with a large common-mode signal applied.
(v) Check the temperature drift of the offset and gain over the intended range.

**One assumption that cannot be verified analytically.** The **interference
environment**. The noise model assumes the only inputs are the source's thermal
noise and the amplifier's own noise; in practice the chain picks up power-line
harmonics, clock feedthrough, ground loops and cable-motion noise, none of which are
in the model and all of which can dominate. Only a measurement in the intended
environment — with the intended cable and the intended grounding — establishes the
achievable ENOB, which is why the field test is part of the design rather than a
final check.

---

## ★★★6 — Measuring the ENOB of an assembled front end

**Stimulus.** A low-distortion sine applied at the *front end's input* through a
resistive attenuator that presents the intended source impedance (1 kΩ here), at a
frequency not harmonically related to the sample rate and not a sub-multiple of it,
at an amplitude 1–2 dB below the chain's full scale. Using the intended source
impedance is essential: the chain's noise figure depends on it, and a test with a
0 Ω source measures something else.

**Analysis.** Digitise a record containing an integer number of cycles (coherent
sampling), take the discrete Fourier transform, and compute the ratio of the power in
the signal bin to the total power in all other bins, excluding DC and the few bins
around the signal that contain its own leakage.

**Metric.** SINAD in dB, and ENOB $=$ (SINAD − 1.76)/6.02 in bits; also the
spurious-free dynamic range in dB, which distinguishes a noise-limited chain from
one with a dominant tone.

**Number of samples.** At least $2^{18}$ samples with an integer number of cycles,
and the measurement repeated at two or three amplitudes to check linearity: a
genuine ENOB is amplitude-independent over the intended range, while a distorted
chain improves at lower amplitude.

**Two effects a converter-only test misses.**

1. **The amplifier's noise contribution**, which is added before the converter and
   therefore sets the chain's floor. A converter-only test would report the
   converter's ENOB, and the assembled chain can be one to two bits worse — the
   single most common surprise in an instrumentation project.
2. **Frequency-dependent gain and phase errors** in the amplifier and the anti-alias
   filter, including the peaking of a high-Q filter near its corner. These do not
   appear in a single-tone ENOB test at one frequency, but they distort a broadband
   signal; a two-tone or swept measurement is needed to see them.
