# Solutions — 23-05-05 Building Low-Cost Instruments for Teaching and Research

The lesson is [05 Instrument Design for Low-Cost Builds](../05-instrument-design-lowo.md).
All values are **SYNTHETIC**.

## ★1

$$v_{\text{sig}} = S v = 25 \times 2\times10^{-6} = 50\ \mathrm{\mu V} .$$

$$v_{\text{Johnson}} = \sqrt{4k_BTRB}
= \sqrt{4(1.380649\times10^{-23})(300)(200)(40)}
= 1.151\times10^{-8}\ \mathrm{V} = 11.51\ \mathrm{nV} .$$

$$\mathrm{SNR} = \frac{50\times10^{-6}}{11.51\times10^{-9}} = 4343
\;\Rightarrow\; 20\log_{10}(4343) = 72.8\ \mathrm{dB} .$$

Note the two halves of this design pull in opposite directions: the sensor's own noise
allows 72.8 dB, which no converter in this lesson can use. The sensor is not the
problem here — the converter is.

## ★2

$$\mathrm{LSB} = \frac{2.5}{2^{16}} = 3.8147\times10^{-5}\ \mathrm{V}
= 38.147\ \mathrm{\mu V},$$

$$v_q = \frac{\mathrm{LSB}}{\sqrt{12}} = \frac{38.147}{3.4641} = 11.012\ \mathrm{\mu V},$$

$$\mathrm{SNR}_q = \frac{50}{11.012} = 4.54
\;\Rightarrow\; 20\log_{10}(4.54) = 13.1\ \mathrm{dB} .$$

So a 16-bit converter destroys the sensor's 72.8 dB in a single step: this is why the
converter must be chosen against the requirement, and why the LSB — 38.1 µV, larger
than the fine signal structure — is not the noise floor to quote.

## ★3

**(a)** $e_n\sqrt{B} = 8\sqrt{40} = 50.60$ nV.

**(b)** The crossover is where the referred quantization noise equals the amplifier
noise:

$$G^{*} = \frac{v_q}{e_n\sqrt{B}} = \frac{11012}{50.60} = 217.6 \approx 218 .$$

**(c)** At $G^{*}$ the referred terms are: sensor 11.51 nV, amplifier 50.60 nV,
quantization $11012/217.6 = 50.60$ nV, so

$$\sigma_{\text{tot}} = \sqrt{11.51^{2} + 50.60^{2} + 50.60^{2}}
= \sqrt{132.5 + 2560 + 2560} = 72.47\ \mathrm{nV},$$

$$\mathrm{SNR} = \frac{50\,000}{72.47} = 690 \;\Rightarrow\; 56.8\ \mathrm{dB} .$$

Gain bought 43.7 dB over the ungained 16-bit case (13.1 dB), which is the whole point:
**resolve the signal with analog gain, not with bits**, and then stop at the crossover
because beyond it the amplifier is the limit and extra gain only eats headroom.

## ★4

$$\bar I = 30\ \mathrm{\mu A} + (4\ \mathrm{mA})(0.005)
+ (100\ \mathrm{mA})\frac{5}{86\,400} = 30 + 20 + 5.79 = 55.79\ \mathrm{\mu A} .$$

$$t_{\text{life}} = \frac{0.60 \times 10\,000\ \mathrm{mAh}}{0.05579\ \mathrm{mA}}
= 107\,550\ \mathrm{h} = 4481\ \mathrm{days} \;(\approx 12.3\ \text{years}) .$$

The shares are: sleep 30/55.79 = **53.8 %**, acquisition 20/55.79 = 35.8 %, transmit
5.79/55.79 = 10.4 %. So the sleep current is attacked first, and the lesson's warning
applies directly — a sleep current that triples at −10 °C would take the life from
12.3 years to about 7.5 years, which is exactly the kind of margin that decides whether
a deployment is feasible.

## ★5

$$y = 0.02\ \mathrm{ppm} = 2\times10^{-8}, \qquad
\Delta t_{\text{day}} = 2\times10^{-8} \times 86\,400 = 1.728\times10^{-3}\ \mathrm{s}
= 1.728\ \mathrm{ms},$$

$$T_{\text{sync}} = \frac{\tau}{y} = \frac{5\times10^{-3}}{2\times10^{-8}}
= 2.5\times10^{5}\ \mathrm{s} = 69.4\ \mathrm{h} \;(\approx 2.89\ \mathrm{days}) .$$

So a 5 ms absolute budget survives nearly three days without a reference — this is the
kind of oscillator that makes an unattended multi-day deployment possible at all.

If the requirement is 5 ms **relative** between nodes disciplined at the same epoch,
the common part of the error cancels and the residual is the *difference* in the
disciplining residuals plus the inter-node drift difference, which is much smaller;
the resynchronisation interval therefore extends by orders of magnitude. The design
change is not a better oscillator but a **procedure**: a common disciplining epoch, a
recorded common reference signal, or a joint post-hoc alignment on a shared event. What
must then be verified is the alignment residual between node pairs, not the absolute
time.

## ★6

A model answer with the arithmetic shown.

**Requirement.** Detect $1\times10^{-6}$ m/s in the DC–50 Hz band, 24 hours a day for
six months, unattended, exposed to −10 °C, with no mains power. Signal at the
requirement: $30 \times 10^{-6} = 30\ \mathrm{\mu V}$.

**Noise budget** (as in the lesson): Johnson 17.63 nV, amplifier $10\ \mathrm{nV/\sqrt{Hz}}$
over 50 Hz = 70.71 nV, current 2.65 nV, quantization (24-bit, ENOB 20 at 5 V full scale)
1.377 µV → total 1.378 µV, SNR 26.8 dB. **Dominant term: the converter.**

**Gain.** The crossover is $G^{*} = 1377/70.71 \approx 19$; choose **20**. Then the
referred quantization noise is $1377/20 = 68.85$ nV and

$$\sigma_{\text{tot}} = \sqrt{17.63^{2} + 70.71^{2} + 2.65^{2} + 68.85^{2}}
= \sqrt{310.8 + 5000.0 + 7.0 + 4740.3} = 100.3\ \mathrm{nV},$$

$$\mathrm{SNR} = \frac{30\,000}{100.3} = 299 \;\Rightarrow\; 49.5\ \mathrm{dB},$$

an improvement of 22.7 dB over the ungained chain. The chain is now amplifier-limited,
so nothing is left on the table.

**Power.** Acquisition 10 min per hour (a 1/6 duty cycle, 16.7 % temporal coverage),
transmit 10 s per day:

$$\bar I = 20\ \mathrm{\mu A} + \frac{12\ \mathrm{mA}}{6}
+ \frac{(120\ \mathrm{mA})(10)}{86\,400} = 20 + 2000 + 13.9 = 2.034\ \mathrm{mA},$$

$$t_{\text{life}} = \frac{0.70 \times 20\,000}{2.034} = 6883\ \mathrm{h}
= 286.8\ \mathrm{days} .$$

Six months needs 183 days, so there is a 1.57× margin — thin, and thin for a good
reason: the margin covers the cold-night capacity loss and the end-of-life fade. **Servicing
every 180 days**, with a mid-deployment check if the site allows it.

**Timing.** The budget follows from the science, and here the honest answer is that
continuous GNSS disciplining is impossible: at ~25 mA average the receiver alone would
draw $25 \times 24 = 600$ mAh/day, i.e. 14 Ah in 23 days. So either
(a) an OCXO with a 55.6 h resynchronisation interval for 1 ms, disciplined at each
visit and drifted within budget between visits; or (b) a TCXO with GNSS run briefly per
day, which holds 1 ms for only 16.7 min and therefore requires the *relative* timing
framing instead. The design decision is to specify **relative** timing between stations
(the array's science uses arrival-time differences) and to discipline all nodes at a
common epoch, which the 2.89-day TCXO budget then satisfies comfortably.

**Calibration and test access.** A measured sensitivity per sensor, a measured and
recorded fixed gain (no field-programmable gain), a two-point calibration at
deployment temperature, an injection test into each channel at every visit, a
repeatability check on a check mass, and all of it recorded in the same file as the
gain and coefficients. The enclosure must be openable without disturbing the sensor, or
the calibration does not transfer.

**What the build cannot deliver.** Not traceability (no accredited chain), not absolute
timing with continuous GNSS, not a defensible noise floor in a noisy cultural
environment, and not robustness in extreme cold. The report must say so, and the
inversion must account for a station-specific noise level that is probably far above
100 nV.

## ★7

From the lesson's table:

| Design | Noise floor | Relative cost | Per unit cost |
|---|---|---|---|
| A: gain 100 + 24-bit | 47.68 nV | 18.0 | 2.649 |
| B: gain 1000 + 32-bit sigma-delta | 1.19 nV | 26.0 | 0.046 |

B is better on the metric by $2.649/0.046 = 57.6\times$.

Reasons to prefer A anyway:

1. **The requirement is the sensor, not the converter.** The sensor's own Johnson noise
   is 17.63 nV, and the analog chain contributes 72.9 nV, so neither design can go below
   the front end's ~73 nV without changing the sensor or the pre-amplifier. B's 1.19 nV
   is not usable: it is 61× below the chain it is attached to.
2. **Headroom and saturation.** At a gain of 1000 with a 5 V range the input full scale
   is ±5 mV; an unexpected local event will clip, and a clipped recording is worse than
   a noisy one. Gain 100 leaves ±50 mV.

A third reason is available and worth stating: a 32-bit sigma-delta converter at ENOB 22
usually means a lower sample rate, so the choice must be checked against the 100 Hz
sampling the 50 Hz band requires — a reminder that the metric ranks one axis only.
