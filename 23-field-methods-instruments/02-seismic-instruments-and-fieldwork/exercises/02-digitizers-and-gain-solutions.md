# Solutions — 23-02-02 Digitizers, Dynamic Range, Gain and Anti-Alias Filtering

> Read after attempting. Lesson:
> [02 Digitizers and Gain](../02-digitizers-and-gain.md). All values are
> **SYNTHETIC**.

---

## ★1 — An 18-bit, $\pm2.5$ V converter

$$\text{LSB} = \frac{2V_{\text{FS}}}{2^{N}} = \frac{5.0}{2^{18}}
= \frac{5.0}{262\,144} = 1.9073\times10^{-5}\ \mathrm{V}.$$

$$q = \frac{\text{LSB}}{\sqrt{12}} = \frac{1.9073\times10^{-5}}{3.4641}
= 5.5060\times10^{-6}\ \mathrm{V}.$$

$$\text{SNR} = 6.02 \times 18 + 1.76 = 108.36 + 1.76 = 110.12\ \mathrm{dB}.$$

Units: LSB in V, $q$ in V (rms), SNR in dB (dimensionless ratio). The SNR is for a
*sinusoid that fills the range*; a smaller signal has proportionally less SNR, and
the quantisation floor itself is absolute, at $5.51\ \mathrm{\mu V}$ rms.

---

## ★2 — Alias frequencies at 400 sps

$$f_{\text{alias}} = \left| (f + f_s/2) \bmod f_s - f_s/2 \right|,
\qquad f_s = 400\ \mathrm{sps}, \quad f_s/2 = 200\ \mathrm{Hz}.$$

- $f = 250\ \mathrm{Hz}$: $250 \bmod 400 = 250$; $250 > 200$, so
  $f_{\text{alias}} = 400 - 250 = 150\ \mathrm{Hz}$.
- $f = 500\ \mathrm{Hz}$: $500 \bmod 400 = 100$; $100 \le 200$, so
  $f_{\text{alias}} = 100\ \mathrm{Hz}$.

Distance to the wanted signal at 100 Hz: $|150 - 100| = 50\ \mathrm{Hz}$ for the
250 Hz signal, and **0 Hz** for the 500 Hz signal — it lands exactly on the wanted
signal and is indistinguishable from it in the record.

The 500 Hz signal is therefore the more dangerous one, and it is the *lower*
frequency: the fold is not monotonic in the frequency of the interferer. Any
frequency $f$ with $f \bmod f_s$ equal to the wanted frequency, or equal to
$f_s - f_{\text{wanted}}$, aliases onto it. This is why an anti-alias filter is
specified across the whole stopband, not at a single frequency.

---

## ★★3 — Filter order for 120 dB at 160 Hz

Butterworth attenuation at frequency $f$ with corner $f_c$:

$$\text{att}(f) = 10\log_{10}\!\left(1 + (f/f_c)^{2n}\right) .$$

For $f/f_c = 160/40 = 4$ and a large $n$ the "+1" is negligible, so

$$\text{att} \approx 20n\log_{10}(4) = 20n \times 0.60206 = 12.0412\,n\ \mathrm{dB}.$$

Setting $12.0412\,n = 120$ gives $n = 9.966$, so **$n = 10$ poles**.

Check at $n = 10$: $(4)^{20} = 1.0995\times10^{12}$ and

$$10\log_{10}(1 + 1.0995\times10^{12}) = 120.41\ \mathrm{dB}.$$

At $n = 9$ the value is 108.37 dB, which fails the requirement by 11.6 dB. The
lesson is that the order rounds *up*: an under-designed filter does not fail
gradually, it fails by the difference between the requirement and the achieved
attenuation at a single critical frequency.

---

## ★★4 — Clipping at 1.2× full scale

$$\text{clipped fraction} = \frac{2}{\pi}\arccos\!\left(\frac{1}{A}\right)
= \frac{2}{\pi}\arccos(0.83333) = \frac{2}{\pi} \times 0.58569 = 0.3729 .$$

So **37.29 %** of the cycle sits at the limiter.

$$\text{apparent} = \frac{1}{A} = \frac{1}{1.2} = 0.8333,$$

i.e. the event is reported at 83.3 % of its true amplitude.

**A 20-cycle wave train.** Each cycle spends 37.29 % of its duration clipped, so
approximately $20 \times 0.3729 = 7.46$ cycles' worth of samples — about 37 % of
the samples in the train — are pinned at the limit. Note that this is a *fraction
of the samples*, not a small perturbation: the reported amplitude error of 16.7 %
is accompanied by a much larger loss of waveform shape, so any quantity that
depends on the shape (a duration magnitude, a spectral ratio, a rise time) is
badly biased, not merely scaled.

---

## ★★★5 — Recording configuration for local earthquakes

**Requirements.** Band 2–30 Hz; peak ground velocity (PGV) between
$10^{-5}$ and $10^{-3}\ \mathrm{m/s}$; 24-bit converter, $\pm10\ \mathrm{V}$.

**(a) Sample rate.** The band ends at 30 Hz. Sampling at $f_s = 200\ \mathrm{sps}$
puts Nyquist at 100 Hz, more than three times the highest frequency of interest,
which leaves room for an anti-alias transition band and for a factor-of-two margin
on any sharp spectral peak. (A tighter choice, $f_s = 100\ \mathrm{sps}$, would
work but leaves almost no transition band.) *Driven by: band of interest.*

**(b) Anti-alias filter.** The band ends at 30 Hz, so the corner is placed at
30–40 Hz. The dangerous frequencies are those that alias into the band: at
$f_s = 200\ \mathrm{sps}$, a frequency $f$ aliases to $200 - f$ for
$100 < f < 200$, so $140\ \mathrm{Hz} \to 60\ \mathrm{Hz}$ and $170\ \mathrm{Hz}
\to 30\ \mathrm{Hz}$ — inside the band. With a 40 Hz corner and $n$ poles,

$$\text{att}(170\ \mathrm{Hz}) \approx 20n\log_{10}(170/40) = 20n \times 0.6284
= 12.57\,n\ \mathrm{dB}.$$

Requiring 100 dB gives $n = 7.96$, so **8 poles**. *Driven by: the converter's
own dynamic range — an alias must sit below the noise floor of the data.*

**(c) Sensor and gain.** Choose a generator constant of
$G = 1500\ \mathrm{V/(m/s)}$ (a typical choice for a short-period or small
broadband sensor; the value must come from the sensor's own calibration). Then

$$v_{\text{clip}} = \frac{10.0}{1500} = 6.67\times10^{-3}\ \mathrm{m/s},$$

which is $6.7\times$ the largest expected PGV of $10^{-3}\ \mathrm{m/s}$ — too much
headroom, and it wastes bits on the small events. Add a preamplifier with gain
$x$: the design rule is that the largest expected event should reach about half of
full scale:

$$G_{\text{total}}\, v_{\max} = \frac{V_{\text{FS}}}{2}
\;\Rightarrow\; G_{\text{total}} = \frac{5.0}{10^{-3}}
= 5000\ \mathrm{V/(m/s)},$$

so $x = 5000/1500 = 3.33$. Round to a standard value of 4× (which puts the largest
event at 0.6 of full scale and leaves 4.4 dB of headroom) or 2× (which puts it at
0.3 and keeps 10 dB of headroom). Take $x = 4$: $G_{\text{total}} = 6000\ \mathrm{V/(m/s)}$
and

$$v_{\text{clip}} = \frac{10.0}{6000} = 1.67\times10^{-3}\ \mathrm{m/s}.$$

*Driven by: the largest expected event and the headroom policy.*

**(d) Smallest resolvable velocity.** $\text{LSB} = 1.1921\times10^{-6}\ \mathrm{V}$
and $q = 3.4413\times10^{-7}\ \mathrm{V}$ (Section 2 of the lesson). Through
$G_{\text{total}} = 6000\ \mathrm{V/(m/s)}$,

$$v_{\text{smallest}} = \frac{q}{G_{\text{total}}}
= \frac{3.4413\times10^{-7}}{6000} = 5.74\times10^{-11}\ \mathrm{m/s}.$$

The electronic window is
$20\log_{10}(1.67\times10^{-3}/5.74\times10^{-11}) = 149.3\ \mathrm{dB}$ — the same
149 dB as in the lesson, because gain cancels between the two ends.

**(e) Does the design cover the required range?** The required PGV range spans
$10^{-3}/10^{-5} = 100$, i.e. 40 dB. The converter provides 149 dB of electronic
range, but the *usable* range is set by the sensor's self-noise and the site's
ambient noise, not by the converter. The check that matters: is the sensor's
input-referred self-noise above or below $v_{\text{smallest}}$ in the 2–30 Hz band?
If it is above, the smallest events are limited by the sensor, not the converter,
and increasing the gain further buys nothing. That check uses the methods of
[01 Seismometers](../01-seismometers.md), Section 4.

---

## ★★★6 — Measuring the effective number of bits (ENOB)

**Stimulus.** A spectrally pure sinusoid from a low-distortion source, at a
frequency that is *not* a sub-multiple of the sample rate (to spread the samples
over the transfer characteristic rather than hitting the same codes), with an
amplitude close to full scale (typically 1–2 dB below it), recorded for a
sufficient number of cycles. A coherent-sampling setup — where the signal
frequency is chosen so that an integer number of cycles fills the record — avoids
leakage and lets the FFT give exact bins.

**Analysis.** Take the discrete Fourier transform of the record, identify the
signal bin, and compute the ratio of the signal power in that bin to the total
power in *all other* bins (excluding DC and a few bins around the signal to
exclude its own leakage). That ratio is SINAD, the signal-to-noise-and-distortion
ratio.

**Metric.** $\text{SINAD}$ in dB, and

$$\text{ENOB} = \frac{\text{SINAD} - 1.76}{6.02} \ \text{bits}.$$

Also report the spurious-free dynamic range (the ratio of the signal to the
largest single spur, in dB), which distinguishes a converter limited by noise from
one limited by a single dominant distortion product.

**Assumptions.** (i) The source is cleaner than the converter, otherwise the
measurement characterises the source. (ii) The window and the record length are
chosen so that leakage does not masquerade as noise — hence the coherent-sampling
requirement. (iii) The converter's own anti-alias filter does not attenuate the
test frequency. (iv) The temperature and the supply are the ones of interest, since
linearity is temperature-dependent.

**Number of samples.** Use at least $2^{16}$ samples and enough coherent cycles to
average the spectral estimate; the SINAD estimate is itself a spectral estimate and
its uncertainty falls only as more independent bins contribute. A record of
$2^{18}$ samples with an integer number of cycles in it is a good working choice.

**What the test does not measure.** (i) The behaviour at the *edges* of the range
in the way a real signal experiences them: a near-full-scale sine tests linearity
in the middle of the range, not the last code, and a code-density (histogram) test
is needed to expose missing codes and large differential nonlinearity. (ii) The
performance of the *whole* acquisition chain, since ENOB is measured at the
converter's input: a preamplifier that adds noise or distortion upstream of the
converter will not appear in this test, and the chain's effective number of bits
must be measured end to end at the sensor's terminals
([23-05-04 Calibration, Testing and Traceability](../../05-instrumentation-and-electronics/04-calibration-and-testing.md)).
