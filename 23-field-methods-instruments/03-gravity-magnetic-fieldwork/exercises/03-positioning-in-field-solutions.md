# Solutions — 23-03-03 Positioning and Elevation Determination in the Field

> Read after attempting. Lesson:
> [03 Positioning in the Field](../03-positioning-in-field.md). All values are
> **SYNTHETIC**.

---

## ★1 — Elevation gradients and the accuracy they require

$$\frac{\partial g_{\text{FA}}}{\partial h} = 0.3086\ \mathrm{mGal/m},$$

$$\frac{\partial g_{\text{B}}}{\partial h} = 0.0419 \times 2.67
= 0.1119\ \mathrm{mGal/m},$$

$$\frac{\partial g_{\text{BA}}}{\partial h} = 0.3086 - 0.1119
= 0.1967\ \mathrm{mGal/m}.$$

**Elevation accuracy for 0.02 mGal** on the Bouguer anomaly:

$$\delta h = \frac{0.02}{0.1967} = 0.1017\ \mathrm{m} \approx 0.10\ \mathrm{m}.$$

Units: the gradients are mGal/m, the target is mGal, so the answer is in metres.
Note that this is the *whole* budget for the elevation term: if elevation is to
contribute no more than half the total error, it must be accurate to about 5 cm,
which is why microgravity surveys specify levelling rather than GNSS alone. Note
also that the free-air column of the lesson's table (0.3086 mGal/m) is the
sensitivity *before* reduction; after reduction the sensitivity is 36 % smaller,
so an error calculated with the free-air gradient alone overstates the problem by
that factor.

---

## ★2 — Latitude

$$\frac{\partial g}{\partial \text{north}} = 0.811\sin(2 \times 40^\circ)
= 0.811 \sin(80^\circ) = 0.811 \times 0.98481
= 0.7987\ \mathrm{mGal/km}.$$

For a 60 m north–south error ($0.060\ \mathrm{km}$):

$$\delta g = 0.7987 \times 0.060 = 0.0479\ \mathrm{mGal}.$$

That is nearly five times a 0.01 mGal target and about 1.5 times the 0.02 mGal
figure used in ★1 — so at this latitude a 60 m position error dominates the
elevation term unless the elevation is levelled to centimetres. The gradient is
largest near 45° and vanishes at the equator and the poles, so the same survey
design has different positioning requirements at different latitudes; state the
latitude with the specification.

---

## ★★3 — Averaging an autonomous GNSS solution

Random error after 400 epochs:

$$\frac{6.0}{\sqrt{400}} = \frac{6.0}{20} = 0.30\ \mathrm{m}.$$

**The residual error** is the *systematic* part of the solution: the offset of the
computed position from the reference frame caused by satellite geometry,
broadcast-orbit and clock errors, uncorrected ionospheric delay, and multipath at
the site. Averaging reduces the scatter of the estimates about their common mean
but does not move the mean towards the truth, so the averaged solution converges to
a *precisely determined but biased* position. Typical magnitudes for autonomous
positioning are metres, which is what makes averaging to 0.30 m misleading: the
error bar is not the accuracy.

**The field check that detects it** is a **tie to a known mark**: occupy a
published benchmark or a continuously operating reference station (CORS) with the
same receiver and method, and compare the computed coordinates with the published
ones. The difference *is* the systematic error of that day's configuration, and it
should be recorded in the survey log. Two independent ties, on different days,
separate a stable bias (a frame or antenna-height problem) from a
configuration-dependent one (satellite geometry, ionospheric activity).

---

## ★★4 — Ignoring the geoid

$$\delta g_{\text{BA}} = 0.1967 \times 35 = 6.88\ \mathrm{mGal}.$$

So an ignored geoid undulation of 35 m produces a **6.88 mGal** error in the
Bouguer anomaly — larger than most targets in a microgravity survey and comparable
with a modest regional anomaly. Worse, the error is *smooth and spatially varying*
(the undulation field has gradients of centimetres to metres per kilometre), so it
appears as a long-wavelength anomaly that could be interpreted as a deep structure.

**Remedies, in order of preference.**

1. **Apply a regional geoid model** to convert ellipsoidal heights to orthometric
   heights. Record the model's name, version and the date it was downloaded. In
   well-surveyed countries such models are accurate to a few centimetres, so the
   contribution to the anomaly error is under $0.1967 \times 0.05 = 0.01$ mGal; over
   large areas far from the model's control data the accuracy is not guaranteed and
   must be stated as a limitation.
2. **Carry the height by optical levelling** from a benchmark of known orthometric
   height. This removes the geoid question entirely, and the accuracy is that of
   the levelling — a few millimetres per station, but at a large cost in field time
   for a 2 km² survey.

A third option, **using a common arbitrary vertical datum**, is acceptable only if
the survey is interpreted in a relative sense and never compared with other data;
that caveat must be written in the report.

---

## ★★★5 — A positioning plan for 0.015 mGal over 2 km²

**Elevation requirement.** Elevation enters with 0.1967 mGal/m. If the elevation
term is allowed to contribute half the total error budget, its standard error must
be at most $0.015/2 = 0.0075$ mGal, i.e.

$$\sigma_h \le \frac{0.0075}{0.1967} = 0.038\ \mathrm{m} = 3.8\ \mathrm{cm}.$$

**How to achieve it.**

- **Spirit or digital levelling** along the survey lines, tied to a benchmark, with
  closed loops checked against a misclosure tolerance; this is the only method that
  reliably delivers a few centimetres *orthometrically* and it also delivers the
  orthometric datum directly.
- **RTK or network RTK GNSS with a geoid model** is the alternative where the survey
  area is large or the line spacing does not suit levelling. Then the height error
  has three parts: the GNSS ellipsoidal height error (a few centimetres for RTK over
  a short baseline), the geoid model error (a few centimetres) and the datum
  transformation. The *combination* must be tested against levelling at a few
  stations, and the test result becomes the survey's stated height accuracy.

**North–south position requirement.** The latitude term is
$0.811\sin(2\varphi)$ mGal/km. At 45° that is 0.811 mGal/km, so a position error of
0.0075/0.811 = 0.0092 km = **9 m** would consume half the budget. So the position
requirement is an order of magnitude looser than the height requirement: RTK
delivers it easily, and even DGPS with careful averaging is adequate. The reason to
care about position at all is the *reduction* (latitude and terrain), not the
anomaly value at a point.

**Datum handling.** Record the coordinate reference system (including the epoch if
it is a dynamic frame), the geoid model and version, the vertical datum, and the
antenna height for every occupation. Convert everything to one system before
processing, and keep the original observations.

**Field checks.**

1. Close every levelling loop and compare the misclosure with the tolerance computed
   from the loop length.
2. Tie to at least one published benchmark per day and record the difference.
3. Occupy one station by two independent methods (levelling and GNSS) at the start,
   the middle and the end of the survey; compare.
4. Check the *anomaly* at one repeat station against the previous day's value, which
   tests the whole chain including the datum conversion.

**Contribution to the error budget.** With $\sigma_h = 0.038$ m the elevation term
is 0.0075 mGal. Compare with the lesson's other terms:
repeatability (3 readings) 0.005 mGal; drift and tide residual 0.016 mGal;
position/latitude 0.0075 mGal; density assumption 0.020 mGal. In quadrature:

$$\sqrt{0.005^2 + 0.016^2 + 0.0075^2 + 0.0075^2 + 0.020^2}
= \sqrt{0.000025 + 0.000256 + 0.000056 + 0.000056 + 0.000400} = 0.0282\ \mathrm{mGal}.$$

The dominant term is the **density assumption**, at 50 % of the variance, followed
by the drift/tide residual at 32 %. The conclusion is uncomfortable and useful:
achieving a 0.038 m levelling accuracy is *not* what limits this survey — the
0.015 mGal target is limited by the reduction assumptions, so the levelling
specification could be relaxed to about 0.08 m without materially changing the
result. Spending the field budget on levelling while leaving the density assumption
unexamined would be a misallocation.

---

## ★★★6 — Establishing the achieved positioning accuracy

**Measurements.**

1. **Repeat occupations** of a subset of stations (at least 20) at different times
   and, where possible, with different satellite geometries — the same stations
   re-occupied on another day and at another hour.
2. **Independent tie measurements** at the same stations by a different method
   (optical levelling for height; a total station or a static GNSS session for
   horizontal position).
3. **Ties to published control** — benchmarks, CORS stations — occupied with the
   production method and configuration.

**Reference.** The published coordinates of the control points, with their stated
accuracies, for the ties; and the independent method for the repeats. Where no
published control exists near the survey, establish a local control network with
long static GNSS sessions and treat it as the reference, stating its own
uncertainty.

**Metric.** The difference between the production and the reference value for each
check point, in metres, separated into two components: the mean (the systematic
part, in m) and the standard deviation about the mean (the random part, in m). For
height, report the same two numbers for the orthometric height, since that is what
the reduction uses. Report horizontal differences in the north–south and east–west
directions separately, because only the north–south component carries the latitude
error.

**Number of check points.** To demonstrate a standard deviation of 0.05 m with 95 %
confidence from a two-sided $\chi^2$ interval, the sample standard deviation $s$
from $n$ points must satisfy
$s\sqrt{n/\chi^2_{0.025,\,n-1}} \le 0.05$. For $n = 30$ the factor is
$\sqrt{30/46.98} = 0.799$, so $s \le 0.0626$ m suffices; for $n = 20$ the factor is
$\sqrt{20/32.85} = 0.780$, so $s \le 0.064$ m. Practical answer: **at least 30
check points**, more if the expected scatter is larger, and report the interval
rather than the point estimate. Note that this bounds the *random* part; the
systematic part is bounded only by the accuracy of the control against which it is
measured.

**Two systematic errors the test cannot detect.**

1. **A bias common to the production method and the reference.** If the check points
   are occupied with the same RTK base and the same geoid model as the survey, a
   base-coordinate error or a geoid-model error is present in both and cancels in
   the difference. Only an *independent* reference — spirit levelling from a
   benchmark, or published control — reveals it.
2. **An error that is constant over the whole survey area**, such as a wrong datum
   transformation or a projection mis-specification applied uniformly. Every check
   point is displaced by the same amount, the spread of differences is unchanged,
   and the test reports a good scatter while the survey is uniformly offset. This
   is caught by comparing the survey's coordinates with an external dataset (a
   national elevation model, a published map, a previous survey), not by internal
   repeatability.
