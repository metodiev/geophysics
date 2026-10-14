# Solutions — 05-02-03 Noise, Drift, Tides and Instrument Bias

> Numbers marked *verified* were computed.

---

## ★1

| Source | Signature | Remedy |
|---|---|---|
| Random readout noise | white, short period | averaging, repeats |
| Drift | monotonic, hours | base-station ties |
| Earth tide | periodic (12.42 h, 24 h) | tide model from ephemeris |
| Bias | constant | absolute calibration, not repetition |

---

## ★2

Precision: repeat readings differ by 0.01 mGal (they cluster tightly).
Accuracy: every reading is 0.3 mGal high because the instrument's scale is
slightly wrong — precise, and wrong. A survey can be precise and inaccurate at
the same time.

---

## ★3

$\sigma_\text{mean} = 0.02/\sqrt{100} = 0.002$ mGal. The condition is that the
samples be independent; correlated noise (microseism, instrument hysteresis)
averages less effectively.

---

## ★★4 *(verified)*

Drift: $0.04\times6 = 0.24$ mGal. Tide: the maximum excursion over a 6 h window
is less than the full amplitude envelope; over a 12.42 h period the
peak-to-peak is $2\times0.18 = 0.36$ mGal, and over 6 h more than half of that
is achieved. So the **tide dominates** the drift over a 6-hour loop. Both are
larger than a typical shallow target anomaly, which is why both must be
removed.

---

## ★★5

If the drift is exactly linear, tying removes it *exactly* (zero residual) up to
the noise on the base readings. For a quadratic component of 0.02 mGal over a
4-hour day, the residual at the midpoint of a 90-minute interval is roughly
$0.02\times(1.5/4)^2 \approx 0.003$ mGal for a linear interpolation — small, but
larger than a 0.005 mGal target requirement if the survey is longer or the
curvature larger. Shorter tie intervals reduce it quadratically.

---

## ★★6

A repeat measures the difference between two readings at the same station. That
difference is $(\beta(t_2)-\beta(t_1)) + (\tau(t_2)-\tau(t_1)) +
(\epsilon_2-\epsilon_1)$: it contains drift, tide and noise, but *not* any
constant bias that affects both readings equally. Repetition therefore bounds
precision only. Accuracy requires a reference the survey does not itself provide.

---

## ★★7

Diurnal variation (40 nT) exceeds the target (25 nT), so a single magnetometer
cannot distinguish the target from the daily variation. Design changes: use two
magnetometers (one at a fixed base) and subtract; or use a gradiometer, which
cancels the common-mode diurnal signal; or model the diurnal variation from a
nearby observatory. Simply acquiring more slowly does not help, because the
variation is correlated rather than random.

---

## ★★★8

Expected structure of results:

- **Linear drift, any tie interval:** RMS residual equals the base-reading noise
  only (approximately), because a linear function is exactly interpolated.
- **Linear + quadratic drift:** residual grows as the square of the tie interval.
  A 120-minute tie leaves roughly four times the residual of a 60-minute tie.
- **A bump (step):** no tie interval removes it if the bump is inside the
  interval; ties bracketing the bump reveal it as an impossible jump in the tie
  sequence.

Detecting the bump: the *base-station readings themselves* show a discontinuity
between consecutive occupations that is inconsistent with the modelled drift
slope; and the stations occupied after the bump show a constant offset relative
to a smooth regional field. The signature is a step, not scatter — which is why
a residual plot is more informative than an RMS number.

---

## ★★★9

Residual RMS against tie interval should show a quadratic rise for a quadratic
drift model and a flat floor at the noise level for a linear one.

For a 0.03 mGal sinusoidal microseismic term at 0.2 Hz, samples 5 s apart
(0.25 of a period) are strongly correlated; the effective number of independent
samples in a 60 s window is roughly one per half-period, i.e. 0.2 Hz means 12
cycles per minute, so about 12 independent samples per minute rather than 12 per
5 s. To average to 0.005 mGal from 0.03 mGal you need 36 *independent* samples,
i.e. about 3 minutes of recording — the $\sqrt{N}$ rule applied naively to 5 s
samples would predict only 36 samples = 180 s, coincidentally close, but the
reasoning differs and the naive rule would fail badly at other frequencies.
State the correlation time explicitly.
