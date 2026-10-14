---
id: 17-08-05
title: "Remote Sensing for Disaster Response"
level: doctoral
prereqs: ["17-02-05", "17-03-03", "21-01-01"]
tags: [remote-sensing, earth-observation, disaster-response, flood-mapping, change-detection, decision-thresholds]
---

# Remote Sensing for Disaster Response

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a disaster map is a *decision* output rather than a
   measurement, and **state** what that changes about how it should be reported.
2. **Construct** a synthetic pre/post image pair and **detect** an inundation by
   a threshold on backscatter.
3. **Compute** a confusion matrix, precision, recall and $F_1$ for a detection,
   and **interpret** each in operational terms.
4. **Derive** and **apply** a cost-weighted threshold that depends on the
   relative cost of a miss and a false alarm.
5. **Build** a change-magnitude damage proxy and **state** its confusions
   (water versus saturated soil).
6. **Compute** the expected time to a usable image from the revisit interval and
   the probability of a cloud-free acquisition, and **state** why latency is part
   of the measurement.
7. **Report** a response map with its threshold, its cost assumption and its
   timeliness.

## Prerequisites

- [17-02-05 Change Detection and Time-Series Analysis](../02-optical-and-thermal-remote-sensing/05-change-detection.md)
  — the pre/post comparison this lesson operationalises.
- [17-03-03 InSAR Time Series: PS-InSAR and SBAS](../03-radar-remote-sensing/03-insar-time-series.md)
  — the radar observations used for rapid mapping.
- [21-01-01 Descriptive Statistics](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md)
  — the proportion machinery behind a confusion matrix.

> All models and data in this module are **SYNTHETIC**. The scenes, the
> backscatter values, the costs and the cloud statistics below are chosen
> teaching values, not a real event or sensor. No real disaster, region or
> mission is referred to.

## 1. A map that decides

In a disaster response, a map is not a description — it is a set of decisions.
Each pixel labelled "flooded" may dispatch a boat; each pixel labelled "dry" may
not. The classification therefore has a **cost structure**, and the right
threshold is the one that minimises expected cost, not the one that maximises
some abstract accuracy. This lesson builds the detection, then shows that the
threshold is a *choice* with a defensible criterion, and that timeliness is part
of the measurement itself.

Radar is the workhorse of rapid inundation mapping because it sees through cloud
and at night: smooth open water acts as a mirror and returns very little energy,
so water is **dark** in a synthetic-aperture-radar image. That is a
measurement — but "dark" is not "flooded", and the gap between them is the
decision this lesson makes explicit.

## 2. Definitions

- **Backscatter coefficient**: the radar energy returned per unit area,
  conventionally given in decibels, $\mathrm{dB} = 10\log_{10}(\text{linear
  ratio})$.
- **Threshold detector**: label a pixel as water if its backscatter is below a
  chosen threshold.
- **Confusion matrix**: counts of true positives (TP), false positives (FP),
  false negatives (FN) and true negatives (TN) against a reference.
- **Precision** $= \mathrm{TP}/(\mathrm{TP}+\mathrm{FP})$; **recall**
  $= \mathrm{TP}/(\mathrm{TP}+\mathrm{FN})$; $F_1 = 2PR/(P+R)$.
- **Latency**: the time from the event to the first usable image.

## 3. Derivations

### 3.1 Detection and its costs

For a threshold $\theta$, the detector is $\hat{y} = \mathbb{1}[\,x < \theta\,]$.
Given costs $c_{\text{miss}}$ (a missed flooded pixel) and $c_{\text{fa}}$ (a
false alarm), the expected cost of a threshold is

$$
C(\theta) = c_{\text{miss}}\,\mathrm{FN}(\theta) + c_{\text{fa}}\,\mathrm{FP}(\theta),
$$

and the operating threshold is $\theta^\star = \arg\min_\theta C(\theta)$.
Maximising $F_1$ is the special case $c_{\text{miss}} = c_{\text{fa}}$ —
appropriate when misses and false alarms cost the same, which in a response they
almost never do.

### 3.2 Latency

If each acquisition is cloud-free with probability $p$ and acquisitions come at
interval $r$, the number of attempts to the first clear image is geometric with
mean $1/p$, so the expected latency is

$$
\mathbb{E}[\,\text{days}\,] = \frac{r}{p}.
$$

Latency is a function of the orbit and the weather, not of the sensor's quality.

### 3.3 The optimal threshold is a cost-weighted likelihood ratio

Minimising $C(\theta) = c_{\text{miss}}\mathrm{FN}(\theta) +
c_{\text{fa}}\mathrm{FP}(\theta)$ is the same problem as a likelihood-ratio
test. At a pixel $x$, labelling it *water* costs
$c_{\text{fa}}\,P(\text{dry}\mid x)$ in expectation, and labelling it *dry*
costs $c_{\text{miss}}\,P(\text{water}\mid x)$. The cheaper label is *water*
when

$$
c_{\text{fa}}\,P(\text{dry}\mid x) \le c_{\text{miss}}\,P(\text{water}\mid x)
\quad\Longleftrightarrow\quad
\frac{P(\text{water}\mid x)}{P(\text{dry}\mid x)} \ge \frac{c_{\text{fa}}}{c_{\text{miss}}}.
$$

So the decision rule is a threshold on the **posterior odds**, at the ratio of
costs. Because lower backscatter makes water more likely, this posterior-odds
rule is equivalent to a threshold on backscatter, and the position of that
threshold is set by $c_{\text{fa}}/c_{\text{miss}}$. With
$c_{\text{miss}} = 10$ and $c_{\text{fa}} = 1$ the bar is $0.1$ — low, so water
is declared readily and recall is high; with equal costs the bar is $1$, and the
rule becomes the maximum-likelihood choice. This is exactly the movement seen in
the threshold sweep of §5, now derived rather than observed.

## 4. Worked example 1 — a threshold and its confusion matrix

The synthetic scene of
[`code/disaster_response_rs_demo.py`](code/disaster_response_rs_demo.py) is
$120\times120$ pixels. Open water (a disc of $2809$ pixels, $19.5\%$) has
backscatter near $-18.5\ \mathrm{dB}$; a saturated-soil ring
($3793$ pixels, $26.3\%$) sits near $-13.0\ \mathrm{dB}$; dry land is near
$-8.0\ \mathrm{dB}$, all with speckle. The truth is the open water only.

At $\theta = -14.0\ \mathrm{dB}$:

$$
\mathrm{TP} = 2806,\quad \mathrm{FP} = 1035,\quad \mathrm{FN} = 3,\quad
\mathrm{TN} = 10556,
$$

$$
P = \frac{2806}{2806+1035} = 0.731, \qquad
R = \frac{2806}{2806+3} = 0.999, \qquad F_1 = 0.844.
$$

The recall is almost perfect — nearly every flooded pixel is found — but
precision is $0.731$, because the saturated soil is dark enough to cross the
threshold. In operational terms: a third of the "flooded" pixels are not open
water. Whether that matters depends entirely on the response: for a boat
dispatch it is a nuisance; for a pixel-count damage total it is a $37\%$
overestimate.

## 5. The threshold is a choice

Sweeping the threshold shows the trade and lets the cost choose:

| Threshold (dB) | Precision | Recall | $F_1$ | FP | FN | Cost |
|---|---|---|---|---|---|---|
| $-16$ | 0.971 | 0.955 | 0.963 | 80 | 126 | 1340 |
| $-15$ | 0.884 | 0.993 | 0.935 | 365 | 20 | 565 |
| $-14$ | 0.731 | 0.999 | 0.844 | 1035 | 3 | 1065 |
| $-13$ | 0.584 | 1.000 | 0.737 | 2001 | 0 | 2001 |

With $c_{\text{miss}} = 10$ and $c_{\text{fa}} = 1$, the minimum-cost threshold
is $-15\ \mathrm{dB}$ (cost $565$). Note that $-15$ is **not** the
$F_1$-maximising threshold ($-16$, $F_1 = 0.963$): because a miss is ten times
as costly as a false alarm, the optimum is pushed toward higher recall
($0.993$), accepting $365$ false alarms to avoid $106$ more misses. This is the
whole point of the cost framework: **$F_1$ is a special case, and rarely the
right one in a response.**

## 6. A change-magnitude damage proxy

Comparing the post and pre images, the mean change is $-10.50\ \mathrm{dB}$ over
water, $-5.02\ \mathrm{dB}$ over saturated soil and $+0.02\ \mathrm{dB}$ over
dry land. Thresholding the change at $-6\ \mathrm{dB}$ flags $4154$ pixels, of
which $1329$ are saturated soil (false alarms) and $2700$ are water. The
change is a *proxy* for inundation or damage: a large drop means a change in
surface roughness or moisture, and saturated soil can cross the same threshold.
A single change map is evidence, not a verdict, and it carries the same
precision/recall structure as the absolute detection.

### 6.1 A worked change threshold

The change magnitudes are class means: $-10.50\ \mathrm{dB}$ for water and
$-5.02\ \mathrm{dB}$ for saturated soil. A change threshold at the midpoint of
the two means would be

$$
\frac{-10.50 + (-5.02)}{2} = -7.76\ \mathrm{dB},
$$

which separates the classes by $2.74\ \mathrm{dB}$ on each side. The lesson's
threshold of $-6\ \mathrm{dB}$ sits $4.50\ \mathrm{dB}$ below the water mean but
only $0.98\ \mathrm{dB}$ below the wet-soil mean — deliberately biased *away*
from flagging wet soil, which is why $1329$ wet-soil pixels still cross it while
$2700$ water pixels do. Choosing the midpoint ($-7.76\ \mathrm{dB}$) would flag
substantially fewer wet-soil pixels and also fewer water pixels, trading
precision for recall in the opposite direction. The point is that the threshold
is a *placed* decision on a known class separation, and its position relative to
the class means — not the confusion matrix alone — is the interpretable
quantity.

## 7. Timeliness is part of the measurement

With a revisit of $5$ days:

| Clear fraction | Expected days to first clear image |
|---|---|
| 0.90 | 5.6 |
| 0.70 | 7.1 |
| 0.50 | 10.0 |
| 0.30 | 16.7 |

A perfect map delivered on day $17$ may inform fewer decisions than a coarse map
delivered on day $6$, because the decisions are made in the first days. This is
not a caveat; it is a property of the product. A response product should quote
its latency alongside its accuracy, because the two trade against each other and
only the decision-maker can weigh them.

## 8. Assumptions and regime of validity

1. **Smooth water is the target.** Wind roughening, vegetation emerging above
   water and floating debris all raise backscatter and hide water.
2. **The threshold transfers.** A threshold fitted in one scene, sensor or
   incidence angle may not transfer; it is a *tuned parameter*, not a constant.
3. **Costs are known and constant.** In a response they are neither; the
   framework makes the assumption explicit so it can be challenged.
4. **The reference is correct.** Precision and recall are only as good as the
   reference mask, which for a fresh event is often itself a rapid product.
5. **The change is caused by the event.** Seasonal, agricultural and tidal
   changes appear in a pre/post difference; a second baseline helps.
6. **Revisit and cloud are independent draws.** Persistent cloud violates this
   and makes latency longer than $r/p$.

## 9. Worked example 2 — the cost of a wrong cost

Suppose the response is actually pixel-count-based, so a false alarm is as
costly as a miss ($c_{\text{miss}} = c_{\text{fa}} = 1$). Recomputing over the
table, the cost becomes $\mathrm{FP} + \mathrm{FN}$:

- $\theta = -16$: $80 + 126 = 206$.
- $\theta = -15$: $365 + 20 = 385$.
- $\theta = -14$: $1035 + 3 = 1038$.

The optimum moves to $\theta = -16\ \mathrm{dB}$, the $F_1$-maximiser, because
the cost structure changed. The detection algorithm did not change; the
*decision context* did, and with it the right answer. Any published threshold is
uninterpretable without the cost assumption behind it.

## Mastery checkpoint

Complete this without notes.

> A water detector flags $2000$ pixels, of which $1600$ are truly water; the
> reference has $1800$ water pixels. **(a)** Compute precision, recall and
> $F_1$. **(b)** With $c_{\text{miss}} = 20$ and $c_{\text{fa}} = 1$, compute
> the cost and state whether you would raise or lower the threshold to reduce
> it. **(c)** State why a river pixel emerging through vegetation can be a false
> negative, and why that is a physical, not algorithmic, limit. **(d)** Given
> a $6$-day revisit and a clear-sky probability of $0.6$, compute the expected
> latency and state one way to reduce it.

A worked version appears in the
[solutions](exercises/05-disaster-response-rs-solutions.md).

## Common pitfalls

1. **Maximising accuracy or $F_1$ by default.** In a response, misses usually
   cost more.
2. **Publishing a threshold without its cost assumption.** The number is
   meaningless alone.
3. **Treating the change map as a flood map.** Saturated soil mimics water.
4. **Ignoring wind and emergent vegetation.** They hide or fake water.
5. **Trusting the reference.** It is often a rapid product with its own errors.
6. **Reporting accuracy without latency.** Both constrain usefulness.
7. **Assuming cloud draws are independent.** Persistent cloud breaks the simple
   latency formula.

## Related modules

- [17-02-05 Change Detection and Time-Series Analysis](../02-optical-and-thermal-remote-sensing/05-change-detection.md)
  — the change methods behind a damage proxy.
- [17-03-01 SAR Principles: Geometry, Polarisation, Backscatter](../03-radar-remote-sensing/01-sar-principles.md)
  — why water is dark in a radar image.
- [21-01-01 Descriptive Statistics](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md)
  — proportions, confusion matrices and their estimation.
- [11-06 Geotechnical and Engineering Geophysics](../../11-exploration-geophysics/06-geotechnical-and-engineering/README.md)
  — where a false negative is a failure rather than a missed opportunity.

## Materials

- Demonstration: [`code/disaster_response_rs_demo.py`](code/disaster_response_rs_demo.py)
  — scenes, a threshold, the confusion matrix, cost-weighted thresholds and
  latency.
- Exercises: [`exercises/05-disaster-response-rs-exercises.md`](exercises/05-disaster-response-rs-exercises.md)
  with [solutions](exercises/05-disaster-response-rs-solutions.md).
