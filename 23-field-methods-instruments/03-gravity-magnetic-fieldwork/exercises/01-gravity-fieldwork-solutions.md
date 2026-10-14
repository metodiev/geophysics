# Solutions — 23-03-01 Gravity Fieldwork: Loops, Drift, Base Stations, Ties

> Read after attempting. Lesson:
> [01 Gravity Fieldwork](../01-gravity-fieldwork.md). All values are
> **SYNTHETIC**.

---

## ★1 — Linear drift over a 4 h loop

$$\Delta g_{\text{drift}} = 0.012 \times 4 = 0.048\ \mathrm{mGal}.$$

A two-tie linear correction assigns to a station read at $t = 2.5\ \mathrm{h}$ the
correction

$$c(t) = r\,\frac{t - t_0}{t_1 - t_0} \times \Delta g_{\text{base}}
= 0.012 \times 2.5 = 0.030\ \mathrm{mGal},$$

which is subtracted from the reading. Equivalently, the correction removes the
fraction $2.5/4 = 0.625$ of the total drift, as it must.

Units: drift rate in mGal/h, accumulated drift and the correction in mGal, the
time in h. If the correction is being *added* rather than subtracted, the sign
convention has been lost — state the convention explicitly in the field protocol,
because the sign error is invisible in a closure check: it cancels at the base and
grows linearly with distance from it.

---

## ★2 — Closure error

$$e_{\text{closure}} = 1000.150 - 1000.000 = 0.150\ \mathrm{mGal}.$$

**Consistency with the lesson's model.** From the demonstration's closure table,
the worst closures over four start times were 0.1209 mGal at 2 h, 0.1564 mGal at
4 h and 0.1871 mGal at 6 h. A 0.150 mGal closure on a 3 h loop is therefore
entirely plausible — between the 2 h and 4 h worst cases, and closer to the 4 h
value because the start time may have been on the steep part of the tidal curve.
So this closure does **not** by itself indicate a problem.

**Two other causes it could indicate.** (i) An instrument disturbance: the
gravimeter was transported without being re-levelled, tilted excessively, or read
before it had thermally settled, which adds a step or a faster drift than modelled.
(ii) A human or bookkeeping error: a mistyped base value, a station read out of
order, a charging or transport pause that shifted the time base, or the instrument
zero point being reset between the two occupations. The diagnostic that separates
these from ordinary drift is the *shape* of the change: an instrument disturbance
produces a step, a bookkeeping error produces an offset, and an ordinary drift
produces a smooth change consistent with the duration and the time of day.

---

## ★★3 — Repeatability and its physical meaning

$$s = 0.004\ \mathrm{mGal}.$$

**Standard error of a three-reading station value:**

$$\mathrm{se} = \frac{s}{\sqrt{3}} = \frac{0.004}{1.732} = 0.00231\ \mathrm{mGal}.$$

**95 % repeatability of a single reading** with the coverage factor 2.23 for
$n = 10$:

$$2.23 \times 0.004 = 0.00892\ \mathrm{mGal}.$$

The coverage factor is the two-sided 95 % Student-$t$ value for 9 degrees of
freedom, and it is larger than the Gaussian 1.96 precisely because $s$ is itself
estimated from only ten readings.

**Free-air equivalent** of the standard error:

$$\delta h = \frac{0.00231\ \mathrm{mGal}}{0.3086\ \mathrm{mGal/m}}
= 0.00749\ \mathrm{m} = 7.5\ \mathrm{mm}.$$

So this station's value corresponds to a levelling accuracy of under a centimetre
— a demanding but achievable requirement with a total station or RTK GNSS, and one
that must be stated in the survey plan before the levelling crew is asked for it.
Note the asymmetry of the comparison: the gravity repeatability (0.0023 mGal =
7.5 mm) is *better* than typical levelling accuracy, which means that in a real
microgravity survey the elevation error, not the gravimeter, usually dominates the
final error budget.

---

## ★★4 — Tidal residual for a 0.08 mGal term

The lesson's table is for $A = 0.10\ \mathrm{mGal}$; scale by
$0.08/0.10 = 0.8$:

| $\Delta t$ (h) | lesson value at $A = 0.10$ (mGal) | scaled to $A = 0.08$ (mGal) |
|---|---|---|
| 2 | 0.0084 | 0.0067 |
| 4 | 0.0314 | 0.0251 |

**Longest interval with residual below 0.01 mGal.** Scaling the lesson's values:
at 2 h the residual is 0.0067 mGal (passes) and at 3 h it is
$0.8 \times 0.0183 = 0.0146$ mGal (fails). Linear interpolation between them puts
the 0.010 mGal crossing at

$$\Delta t \approx 2 + \frac{0.010 - 0.0067}{0.0146 - 0.0067} = 2 + 0.42
= 2.42\ \mathrm{h}.$$

So the longest interval is **about 2.4 h**. The interpolation is between two
tabulated worst-case values and inherits their worst-case-over-phase character: a
loop that happens to sit near the turning point of the tide will do better, which is
exactly why the criterion must be stated for the worst case rather than for the
average.

---

## ★★★5 — A looping schedule for 0.01 mGal

**Assumptions and how to measure them.**

- **Drift rate.** Measure it by occupying the base station for 30–60 minutes at the
  start and end of each day with the instrument otherwise undisturbed, and fitting
  the slope; repeat over several days. For planning, assume a value an order of
  magnitude above the manufacturer's typical drift until measured — the survey's
  rejection criterion depends on it. Take $0.010\ \mathrm{mGal/h}$.
- **Tidal amplitude.** Compute it from a standard tidal prediction for the site
  (the tidal acceleration is a calculable function of position and time, not a
  measured quantity), and record the prediction used. Take a semi-diurnal amplitude
  of $0.08\ \mathrm{mGal}$.

**Loop duration.** The linear instrument term contributes $0.010\,\Delta t$; the
tidal term contributes the worst-case residual of ★★4. Requiring both below
0.01 mGal in quadrature:

$$\sqrt{(0.010\,\Delta t)^{2} + r_{\text{tide}}^{2}} \le 0.01 .$$

The linear term alone exhausts the budget at $\Delta t = 1\ \mathrm{h}$, so a
two-tie loop cannot meet 0.01 mGal at this assumed drift. The design therefore
needs more ties rather than a shorter loop.

**Loop duration and ties together.** Use 3 h intervals between base occupations.
Within one 3 h interval the worst-case tidal residual scaled to $A = 0.08$ is
$0.8 \times 0.0183 = 0.0146$ mGal — above target — so also require the instrument
term to be small: over 3 h it is $0.010 \times 3 = 0.030$ mGal before correction,
which the linear correction removes almost completely (the drift is linear by
assumption), leaving only its curvature.

The honest conclusion: at a nominal 0.010 mGal/h drift the *instrument* is the
binding constraint, and a 0.01 mGal target requires either a better instrument
(measured drift below 0.003 mGal/h) or a correction for the tide computed from a
tidal model rather than interpolated between base ties. With a computed tidal
correction, the residual becomes the difference between the model and the true
tide — typically far smaller than the interpolated residual — and 3 h intervals
become comfortable.

**Stations per loop.** With 8 minutes of measurement and 6 minutes of travel per
station, one station takes 14 minutes, so a 3 h interval fits
$180/14 = 12.9$, i.e. **12 stations** between base occupations, leaving the base
occupation itself (a few minutes) inside the budget. In practice one plans 10
stations to leave margin for the inevitable delays, and one lets the *access*, not
the drift, set the number: if the stations are 2 km apart the travel time
dominates and the loop holds fewer stations.

**Acceptance check for the day.** Before leaving the site: (i) every loop closed
within the tolerance computed for its own duration and start time, not a global
number; (ii) the measured drift between the first and last base occupation
consistent with the assumed rate, with no step; (iii) at least one station repeated
with a difference inside the 95 % repeatability; (iv) the elevation and position of
every station recorded, with their uncertainties, and the time of each reading in
the notebook. The day's data are accepted when all four hold, and the reason for any
failure is written down rather than resolved by re-reading the numbers.

---

## ★★★6 — Detecting an unstable base station

**Measurement.** Occupy the base station repeatedly with the same gravimeter, at
fixed times of day (to make the tidal contribution predictable) and with a fixed
procedure, over a long enough period. To separate the base's own movement from the
instrument's behaviour, occupy a **second** base 5–20 km away in the same session
and compare the two series: a common trend is the instrument, a trend in one only
is that station.

**Frequency of occupation.** A stability test for a monthly drift of
$0.02\ \mathrm{mGal}$ requires occupations at least monthly, and better weekly, so
that the trend is sampled rather than aliased. If the suspected mechanism is
seasonal (soil moisture, irrigation, water table), occupy through a full annual
cycle; if it is construction or traffic, occupy around the events.

**Metric.** The rate of change of the base value, in mGal per month, estimated by
least squares on the occupation series with its standard error; and the residual
scatter about that trend, in mGal, which is the short-term stability. Report both,
with the number of occupations.

**Duration needed.** The standard error of a slope from $n$ evenly spaced
occupations spanning $T$ months is approximately
$\sigma_{\text{read}}/(T\sqrt{n}/ \sqrt{12})$ for a uniform design. With
$\sigma_{\text{read}} = 0.005\ \mathrm{mGal}$ and monthly occupations
($T = 12$ months, $n = 13$), the slope uncertainty is of order
$0.005/(12 \times 3.6/\sqrt{12}) = 0.005/12.5 \approx 0.0004\ \mathrm{mGal/month}$,
far below the $0.02\ \mathrm{mGal/month}$ target — so a year of monthly occupations
detects such a drift many times over. Two or three occupations detect only a gross
instability.

**What the experiment cannot distinguish.**

1. **A base that moves and an instrument that drifts the same way.** A slow
   instrument drift correlated with season (temperature, ageing) mimics a
   base-station trend in a single-site test; only the two-base comparison separates
   them, and even that fails if both bases share the same hydrological setting.
2. **A real change in the local gravity field from a change in the base's own
   monument.** If the monument is settling or the soil beneath it is compacting, the
   measurement is correct and the "instability" is physical — which is not a defect
   of the survey but a change in the reference level, and it must be reported as
   such rather than corrected away.
