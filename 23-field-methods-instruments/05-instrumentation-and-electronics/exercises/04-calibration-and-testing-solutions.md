# Solutions — 23-05-04 Calibration, Testing and Traceability

The lesson is [04 Calibration and Testing](../04-calibration-and-testing.md). All
values are **SYNTHETIC**.

## ★1

$$\sum r_i^{2} = 0.0260^{2} + 0.0410^{2} + 0.0120^{2} + 0.0050^{2} + 0.0080^{2}
= 0.002590 .$$

$$\text{RMS} = \sqrt{\frac{0.002590}{5}} = \sqrt{5.180\times10^{-4}} = 0.02276 ,$$

$$\hat\sigma = \sqrt{\frac{0.002590}{3}} = \sqrt{8.633\times10^{-4}} = 0.02938 .$$

The ratio is $\sqrt{5/3} = 1.291$, i.e. the RMS understates the residual scatter by
22.5 % here. It is $\hat\sigma$ — the $n-2$ version — that enters
$\mathrm{se}(a)$ and $\mathrm{se}(b)$: the two fitted parameters consume two degrees of
freedom, so the residuals can hide a slope and intercept error that the fit itself
cannot see. Both numbers are quoted in the demonstration because the RMS is the useful
"how well does it fit in value units" figure and $\hat\sigma$ is the input to the
uncertainties.

Note also the *sign pattern* of the residuals, $+ - + - +$: at five points evenly
spaced this is what a slight curvature produces, and the honest conclusion is that the
residual scatter here is not a pure noise estimate. If the same pattern persisted with
20 points, the linear model would have to be rejected.

## ★2

$$\mathrm{se}(a) = \frac{\hat\sigma}{\sqrt{\sum(x_i-\bar x)^{2}}}
= \frac{0.02938}{\sqrt{100\,000}} = \frac{0.02938}{316.228}
= 9.29\times10^{-5} ,$$

$$\mathrm{se}(b) = \hat\sigma\sqrt{\frac{1}{n} + \frac{\bar x^{2}}
{\sum(x_i-\bar x)^{2}}}
= 0.02938\sqrt{0.2 + 0.9} = 0.02938 \times 1.0488 = 0.03082 .$$

$$\frac{\mathrm{se}(a)}{a} = \frac{9.29\times10^{-5}}{0.099970} = 9.29\times10^{-4}
= 0.0929\ \% .$$

These reproduce the demonstration's 9.291573e−05, 0.03082 and 0.0929 %. The design
lesson: $\mathrm{se}(a)$ depends on the *spread* of the raw readings, so a calibration
confined to the middle of the range cannot constrain the scale however many points it
uses, and $\mathrm{se}(b)$ depends on $\bar x$, so a calibration whose mean is far from
the working value has a poorly determined offset.

## ★3

$$\sigma_{\text{tot}} = \sqrt{0.02938^{2} + 0.02000^{2} + 0.01000^{2} + 0.00500^{2}}
= \sqrt{1.3882\times10^{-3}} = 0.03726 .$$

| Component | Value | Variance | Share |
|---|---|---|---|
| fit residual | 0.02938 | 8.6318e−4 | 62.2 % |
| reference standard | 0.02000 | 4.0000e−4 | 28.8 % |
| check repeatability | 0.01000 | 1.0000e−4 | 7.2 % |
| drift since calibration | 0.00500 | 2.5000e−5 | 1.8 % |
| **total** | **0.03726** | 1.3882e−3 | 100 % |

The fit residual dominates at 62.2 % of the variance, so it is attacked first — and
the way to attack it is to **add calibration points and improve their repeatability**:
a sixth point at 600 (keeping the 100 spacing) raises $\sum(x-\bar x)^{2}$ from 100 000
to 175 000, which lowers $\mathrm{se}(a)$ by about 24 %, while the extra degrees of
freedom also make $\hat\sigma$ itself better determined. Buying a better reference
standard would change only the 28.8 % term: reducing it to *zero* would take the
quadrature total from 0.03726 to
$\sqrt{1.3882\times10^{-3} - 4.0000\times10^{-4}} = 0.03144$, a 16 % gain for a much
larger cost.

## ★4

$$T_{\text{cal}} = \frac{\tau}{r} = \frac{0.05}{0.005} = 10\ \text{days} ,$$

matching the demonstration's table, in which day 10 is exactly at the limit and day 20
is out. For a 30-day interval at the same tolerance,

$$r \le \frac{0.05}{30} = 1.67\times10^{-3}\ \text{value units per day} ,$$

a factor of 3 better than the assumed drift rate.

The single measurement that establishes $r$ is the **difference between the calibration
performed before a deployment and the calibration performed after it, divided by the
elapsed time** — the same data a before-and-after calibration pair already produces, so
recording the elapsed time and the environment beside each calibration is what makes
$r$ measurable rather than assumed.

One coherence check: here $\tau = 0.05$ is *larger* than the calibration's own
quadrature budget of 0.03726, so the 10-day interval is set by a standalone acceptance
limit and not by a budget allocation. If the requirement were instead that the drift
contribute a small part of the value budget, the interval would shorten in proportion:
a drift term of 0.01 would give 2 days. The tolerance must therefore be declared by the
science requirement *before* the interval is computed, and the two must appear together
in the calibration record.

## ★5

**(a)** The present scale uncertainty is $0.0929\ \% = 9.29\times10^{-4}$ relative, so

$$\Delta B = 9.29\times10^{-4} \times 50\,000 = 46.5\ \mathrm{nT} .$$

**(b)** The requirement is $0.5/50\,000 = 1.0\times10^{-5}$ relative, so the improvement
factor needed is

$$\frac{9.29\times10^{-4}}{1.0\times10^{-5}} = 92.9 \approx 93 .$$

**(c)** At the present span ($\sqrt{\sum(x-\bar x)^{2}} = 316.23$, $\hat\sigma = 0.02938$),
$\mathrm{se}(a)$ is proportional to $\hat\sigma$, so the residual scatter would have to
fall to $0.02938/93 = 3.2\times10^{-4}$ — a 93-fold improvement in the *scatter* of a
five-point calibration, which no realistic procedure delivers. At the present
$\hat\sigma$, $\mathrm{se}(a)$ is proportional to $1/\sqrt{\sum(x-\bar x)^{2}}$, so
$\sum(x-\bar x)^{2}$ must rise by $93^{2} = 8650\times$, and since
$\sum(x-\bar x)^{2} \propto (\text{span})^{2}$ for fixed $n$ and even spacing, the span
must widen by 93× — from 400 counts to about 37 000 counts, i.e. a calibrated field span
of roughly 3700 nT (±1850 nT) around the working value. That is a coil facility, not a
field procedure.

**(d)** Neither route is the right answer. The measurement the survey actually needs is
*relative* between stations, so the scale error is **common mode**: if every station is
measured with the same instrument, or all instruments are calibrated against one
transfer standard at the same time, the scale factor multiplies every station equally
and cancels in the station-to-station differences, leaving only the reading's own
scatter and repeatability. The two designs that deliver the requirement are therefore

1. **roving with one instrument** against a base station, repeated on a loop, which
   makes the scale common mode by construction and converts the requirement into a
   repeatability requirement; or
2. **simultaneous multi-instrument recording** at a common reference station, used to
   estimate a per-instrument scale correction at the field value itself — an
   inter-instrument comparison, which is a calibration in the sense of this lesson but
   at 50 000 nT rather than at the calibration span.

The audit question that must be asked first is whether the 0.5 nT applies to
*differences* or to *absolute* values: if absolute, the scale term is binding and the
coil route in (c) is unavoidable, and the survey's requirement must be renegotiated or
its uncertainty honestly reported as 46 nT.

## ★6

A model answer. The logger records three-component geophones on 12 channels with a
known sampling rate and a common clock.

| Test | What it verifies | Signal | Metric | When | Failure threshold |
|---|---|---|---|---|---|
| Geophone sensitivity | scale per channel | driven mass or a step response | V/(mm/s) at 1 Hz reference | before and after | 5 % from the nominal value |
| Channel gain spread | relative scale between channels | the same injection into all 12 | ratio of RMS amplitudes | before and after | 1 % peak-to-peak spread |
| Channel timing | inter-channel skew | a common pulse into all 12 at once | sample offset of the first break | before and after | 1 sample |
| Clock | absolute time and drift | reference pulse per second | offset in ms, and ms/day | before, during, after | 1 ms offset, 1 ms/day |
| Dynamic range and clipping | no saturation in service | a full-scale test signal, then the longest expected event | number of clipped samples, and the noise floor | before | any clipping in a real event |
| Anti-alias filter | stopband attenuation and corner | swept sine at the sample rate and above | dB at the stopband edge vs the passband | before | 3 dB from the design value |
| Crosstalk | independence of channels | an injection into one channel only | dB relative to the injection | before | −60 dB or the stated limit |

The clock, filter, dynamic-range and crosstalk tests are the ones the *calibration*
does not cover: a calibration establishes a scale at one frequency and one amplitude,
and says nothing about timing, band edges or leakage between channels.

Two systematic errors this set cannot detect: (i) a **common** timing offset shared by
all channels and the clock — consistently late but self-consistent — and (ii) a
**common** scale error affecting all 12 channels equally, for example a wrong reference
value at the calibration stage. Both are common-mode and cancel in relative results;
detecting them requires an external reference or an independent method, which is why
"the data are internally consistent" is not the same claim as "the data are correct".
