# Solutions — 06-13-03 Volcano Seismology: LP Events, Tremor and Eruption Forecasting

The lesson is [03 Volcano Seismology](../03-volcano-seismology.md). All models are
**SYNTHETIC**.

## ★ Foundational

**★1.**
$$Q = \frac{f_{\text{peak}}}{\Delta f} = \frac{1.50}{0.075} = 20.0 .$$
Invert the peak-shift relation for the undamped frequency:
$$f_0 = \frac{f_{\text{peak}}}{\sqrt{1 - 1/(4Q^{2})}}
= \frac{1.50}{\sqrt{1 - 1/1600}} = \frac{1.50}{0.999687} = 1.5005\ \mathrm{Hz},$$
$$\sigma = \frac{\pi f_0}{Q} = \frac{\pi \times 1.5005}{20.0}
= 0.23570\ \mathrm{s^{-1}}, \qquad
\tau = \frac{1}{\sigma} = 4.243\ \mathrm{s}.$$
The ringing lasts about $6\tau = 25.5\ \mathrm{s}$. Units: $\sigma$ is
$\mathrm{s^{-1}}$ because it multiplies $t$ in the exponent, and $Q$ is
dimensionless, so $\pi f_0/Q$ is $\mathrm{s^{-1}}$ as required.

**★2.**
$$f_{\text{peak}} = 1.5005\sqrt{1 - 1/(4 \times 20.0^{2})}
= 1.5005 \times 0.999687 = 1.5000\ \mathrm{Hz},$$
so the shift is $1.5005 - 1.5000 = 0.0005\ \mathrm{Hz}$, or
$0.031\%$ of $f_0$. A $0.01\ \mathrm{Hz}$ spectral resolution cannot see it: the
shift is about 20 times smaller than one resolution element, which is why the
lesson says the peak position is only diagnostic at *low* $Q$ (where the shift is
$0.5\%$ at $Q = 5$).

**★3.** RSAM (real-time seismic amplitude measurement) is the root-mean-square of
a velocity record computed in a moving window:
$$\mathrm{RSAM}(t; T_w) = \sqrt{\frac{1}{T_w}\int_{t-T_w}^{t} v^{2}(t')\,dt'} .$$
Its units are those of the record it is computed from — for a velocity record,
$\mathrm{m\,s^{-1}}$. The one free parameter is the window length $T_w$.

## ★★ Applied

**★★4.** Precision $= p h / (p h + (1-p) f)$ with $h = 0.9$, $f = 0.25$:

| $p$ | numerator $ph$ | denominator | precision |
|---|---|---|---|
| 0.4 | 0.360 | 0.360 + 0.150 = 0.510 | 0.706 |
| 0.05 | 0.045 | 0.045 + 0.2375 = 0.2825 | 0.159 |
| 0.002 | 0.0018 | 0.0018 + 0.2495 = 0.2513 | 0.00716 |

With $f$ halved to $0.125$ at $p = 0.002$: numerator unchanged at $0.0018$,
denominator $= 0.0018 + 0.12475 = 0.12655$, precision $= 0.0142$ — a factor
**1.99** improvement (as it must be, since for small $p$ precision
$\approx ph/f$, so halving $f$ doubles precision).

With $h$ raised to $0.99$ at $p = 0.002$: numerator $= 0.00198$, denominator
$= 0.00198 + 0.2495 = 0.25148$, precision $= 0.00787$ — a factor **1.10**
improvement. For rare eruptions, **halving the false-alarm rate is worth far more
than improving the hit rate from 90% to 99%**, which is the operational lesson of
the base-rate analysis.

**★★5.** From the measured table (mean values):

| window | mean latency | mean false alarms in $415.9\ \mathrm{s}$ |
|---|---|---|
| 1 s | $4.76\ \mathrm{s}$ | 56.05 |
| 5 s | $10.48\ \mathrm{s}$ | 18.40 |
| 20 s | $47.29\ \mathrm{s}$ | 3.40 |
| 60 s | $80.78\ \mathrm{s}$ | 1.70 |

Latency $< 20\ \mathrm{s}$ is satisfied by the $1\ \mathrm{s}$ and
$5\ \mathrm{s}$ windows; false alarms $< 5$ is satisfied by the $20\ \mathrm{s}$
and $60\ \mathrm{s}$ windows. **No window satisfies both**, which is exactly the
measured trade-off: the latency requirement and the false-alarm requirement pull
in opposite directions, and the gap between them (a factor of about 4 in latency
between the $5\ \mathrm{s}$ and $20\ \mathrm{s}$ windows) is the price of the
reduction. The honest resolution is to change a *different* parameter — raise the
threshold at a $5\ \mathrm{s}$ window, which trades hit rate for false alarms —
or to add a second, independent observable.

**★★6.** A single-mode fit has three free parameters (amplitude, $f_0$, $Q$), and
it must absorb a two-mode spectrum with them. The second peak cannot be matched
in position, so the fit will broaden the single resonance — lowering the
recovered $Q$, i.e. **biasing $Q$ low** — and will place $f_0$ between the two
peaks, biasing the frequency low as well. The residual then shows a systematic
pattern (a deficit at the second peak, an excess between the peaks), which is the
diagnostic that the model is wrong rather than the data: a residual with
structure, rather than a residual at the noise level, is the signal to add a mode
rather than to adjust $Q$.

## ★★★ Research-oriented

**★★★7. Protocol.**

- **Base rate.** $p = 1/30$ per unrest day, i.e. $p \approx 0.033$ per day of
  unrest (assuming unrest episodes average one day; state the episode definition
  explicitly).
- **Observable.** RSAM in the $[1, 8]\ \mathrm{Hz}$ band at a stated station,
  plus a low-frequency LP-detection count as a second, partially independent
  channel.
- **Window.** $10\ \mathrm{s}$ (interpolating the lesson's table: latency of
  order $20$–$25\ \mathrm{s}$, false alarms of order $5$–$10$ per quiet period).
  State this interpolation as an estimate, not a measurement, and verify it on
  the site's own noise before adopting it.
- **Threshold rule.** Alarm if RSAM exceeds median $+ 3 \times 1.4826 \times$ MAD
  of a rolling $30\ \mathrm{min}$ baseline, recomputed every hour; require **two
  consecutive crossings** $60\ \mathrm{s}$ apart to reduce single-sample false
  alarms. The re-estimated baseline must be logged, because it changes the
  effective false-alarm rate.
- **Alarm logic and expected performance.** State expected latency
  ($\sim 25\ \mathrm{s}$ plus $60\ \mathrm{s}$ confirmation = $\sim 85\
  \mathrm{s}$) and expected false-alarm rate per day. Report **precision at
  $p = 0.033$**, not hit rate.
- **Reporting format.** Alert level changes with timestamp, the quantity and
  threshold that triggered them, the estimated precision and its dependence on
  the base-rate estimate, and the latency the operator should expect.
- **Numbers you do not have yet.** The site's noise spectrum and its daily
  variability; the site-specific $(h, f)$ of the rule; the base rate $p$ with its
  uncertainty; the station's coupling and its stability; the cost ratio of a
  false alarm to a missed eruption. Every one of these is required before the
  precision figure can be defended.

**★★★8. Narrowband versus broadband in volcano monitoring.**

- **Narrowband target: an LP phase to be inverted for $Q$.** Window: the LP
  duration (a few tens of seconds, from $6\tau$); processing: bandpass around the
  resonance and a matched filter or spectral fit; sacrifice: the broadband
  amplitude information and the ability to see a slow precursor ramp, because the
  narrow band rejects both. Gauge/threshold choices are irrelevant here — what
  matters is the band and the spectral fit's residual structure.
- **Broadband target: tremor envelope.** Window: long ($20$–$60\ \mathrm{s}$) for
  stability; processing: RSAM with a robust threshold; sacrifice: latency, and
  the ability to resolve individual LP events inside the tremor.
- **Direct conflict.** An accelerating LP rate is the classic precursor, and it
  is best seen as an *event count* in a narrow band, while the tremor it is
  embedded in is best seen as an envelope in a broad band. A long RSAM window
  smooths the very rate increase that matters, and a narrow LP band discards the
  amplitude trend. **Resolution in an operational setting:** run both detectors
  in parallel and combine them with an explicit logic (e.g. escalate on either,
  with the LP-count channel providing the confirmation), and report them as two
  separate diagnostics with their own $(h, f)$ pairs — never as a single
  undifferentiated "seismic unrest" indicator, because the combined $(h, f)$ then
  depends on the combination rule and is not measurable from the catalogue.
