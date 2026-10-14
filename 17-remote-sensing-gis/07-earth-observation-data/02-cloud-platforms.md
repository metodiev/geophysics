---
id: 17-07-02
title: "Cloud Platforms: GEE, Copernicus, NASA Earthdata"
level: advanced
prereqs: ["17-07-01", "22-06-02", "03-08-04"]
tags: [remote-sensing, earth-observation, cloud-platforms, data-cubes, cloud-masking, reproducibility]
---

# Cloud Platforms: GEE, Copernicus, NASA Earthdata

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** what a cloud geospatial platform provides that a download does
   not: an archive of assets, a compute layer beside the data, and a versioned
   catalogue.
2. **Define** the reducer as the operation that maps an image stack to an array
   of answers, and **state** why the reducer, not the pixels, decides the
   result.
3. **Quantify** the difference between compositing a synthetic stack with and
   without a cloud mask, and **attribute** the residual bias to the mask.
4. **Demonstrate** that a cloud mask has false negatives, so the reported count
   of clear observations overstates the true count.
5. **Compute** the data volume and egress ratio for compute-at-source versus
   download.
6. **Show** that a reprocessing between archive versions shifts a product by a
   measurable amount, and **state** the reproducibility fix.
7. **Decide**, for a stated task, whether to download or to reduce at source,
   and **state** the assumptions the decision rests on.

## Prerequisites

- [17-07-01 Landsat, Sentinel and MODIS Data Products](01-landsat-sentinel.md)
  — products, levels and calibration, which a platform serves.
- [22-06-02 Cloud Computing for Research](../../22-data-engineering-reproducibility/06-high-performance-and-cloud/02-cloud-computing-research.md)
  — the compute model the platform is built on.
- [03-08-04 Dask and Chunking](../../03-scientific-computing/08-gridded-geospatial-data/04-dask-chunking.md)
  — lazy, chunked arrays, which is how a "data cube" is held without loading it.

> All models and data in this module are **SYNTHETIC**. The cube, cloud cover,
> mask accuracy and archive versions below are chosen teaching values. No
> archive, account or network is used, and no number is a measurement of any
> real collection. Three platform **families** are named — Google Earth Engine,
> the Copernicus services and NASA Earthdata — as the canonical examples of an
> archive-plus-compute service; no specification of any of them is quoted.

## 1. From downloading files to querying a collection

The traditional workflow was: search a catalogue, download scenes, process them
locally. The cloud workflow is: search a collection, apply a **reducer** at the
archive, and download only the result. The archive holds the pixels; the compute
layer holds the CPU; the catalogue holds the metadata and the version. Your
analysis becomes a *program* that the platform evaluates where the data lives.

This is a genuine change in the physics of the workflow, not merely in the
ergonomics. Two things follow.

- **Egress stops being the bottleneck.** Downloading a global multi-year stack
  is often impossible; reducing it at source returns a small array.
- **The reducer becomes part of the method.** When you compute a median of a
  masked stack at the archive, the mask, the compositor and the resampler are
  *your* choices, executed on someone else's machine. If you do not record them,
  your result is not reproducible — even if the pixels are exactly right.

## 2. Definitions

- **Asset.** One observation: a raster (or a set of bands) with a footprint, a
  timestamp and a version.
- **Collection / version.** A named, versioned set of assets. A reprocessing
  creates a new version; the identifier changes; the numbers can change.
- **Stack.** The set of assets a reducer consumes — usually those overlapping a
  region of interest (ROI) and a time window.
- **Reducer.** Any function mapping the stack to an output. A *compositor* is a
  reducer that collapses the time axis (median, mean, maximum index). A
  *spatial* reducer collapses space (mean over a region).
- **Lazy evaluation.** The graph of operations is built first and executed only
  when the result is requested. This is why a malformed query can be cheap.
- **Egress.** Data leaving the platform to you. It is what a download bill
  counts, and it is usually the quantity the cloud model exists to avoid.

## 3. Cloud masking is a model, not a measurement

Clouds are bright; a temporal median is robust to a minority of bright samples.
So one might hope that compositing without a mask is "good enough". The
synthetic cube of [`code/cloud_platforms_demo.py`](code/cloud_platforms_demo.py)
lets us measure how good.

The cube has $T = 60$ observations on an $8\times8$ grid, a surface signal with
season and noise, and clouds that brighten the surface by $+0.25$ in
reflectance. A cloud mask flags $80\%$ of the true clouds and misses the rest.
Compositing over time:

| Composite | Mean reflectance | Bias vs clear-sky truth | RMS error |
|---|---|---|---|
| unmasked median | 0.2801 | $+0.0397$ | 0.0743 |
| masked median | 0.2615 | $+0.0211$ | 0.0600 |
| clear-sky truth | 0.2404 | — | — |

Two honest readings. First, the unmasked median is biased *upwards* by
$+0.0397$ in reflectance, because the bright clouds pull it. Second — and this
is the part that surprises people — **masking halves the bias but does not
remove it**, because the mask has false negatives. The bias is also not uniform:
the worst masked error is $0.2263$, and it sits in the persistently cloudy
corner, where the mean absolute masked error is $0.1862$ against $0.0063$
elsewhere. A single scalar "accuracy" for a compositing method hides this
structure; the *spatial* pattern of the error is the honest report.

### 3.1 Why a median helps but is not a cure

For a sample of $T$ values of which a fraction $f$ are contaminated by clouds
that are higher than the truth, the sample median equals the truth when the
contaminants are fewer than half the samples and the clean samples straddle the
truth. When cloud cover exceeds $50\%$ in a pixel — as it does in the synthetic
corner, where it is $85\%$ — the median is contaminated no matter what mask is
used, unless the mask is nearly perfect. The median's robustness is a property
of the *fraction* of outliers, not of their size.

## 4. Valid-observation counts

Automated compositing almost always degrades silently when a pixel is observed
too few times. The demonstration reports, per pixel:

- **flagged** cloud-free observations: min 14, mean 49.2, max 57 of 60;
- **actually** clear observations: min 4, mean 46.7, max 57 of 60.

The mask over-counts clear looks by $2.5$ observations on average, and six of
the sixty-four pixels — all in the cloudy corner — fall below $25$ actually-clear
observations. A product that reports a value for every pixel without reporting
the *count behind it* is presenting a gap-filled guess as a measurement. **The
count is part of the value.** Any compositing pipeline should return, alongside
the composite, an observation-count layer, and any downstream consumer should
read it.

## 5. Versioning: the same query, two answers

Reprocessing an archive to a new version changes the product. In the
demonstration a small additive calibration offset of $+0.0100$ between two
versions shifts the composite mean from $0.2801$ to $0.2901$: a difference of
exactly $+0.0100$ in reflectance, with identical code and identical requests.

The reproducibility rule is immediate and non-negotiable: **pin the version**.
A result reported as "the median composite from collection X" is not
reproducible, because collection X will be reprocessed. A result reported as
"collection X, version V, mask M, reducer R, window W" is. This is the same
provenance requirement as in the previous lesson, escalated by the fact that
the platform, not you, controls the version.

## 6. The egress arithmetic

Why does the cloud model exist? Because of orders of magnitude. Take a
synthetic global-scale stack: $10^4 \times 10^4$ pixels, $200$ observations,
$3$ bands, $4$ bytes per value:

$$
\text{full} = 10^8 \times 200 \times 3 \times 4 = 2.4\times10^{11}\ \text{bytes}
= 240.00\ \text{GB (decimal)}.
$$

A one-number-per-pixel summary returned at source is

$$
\text{summary} = 10^8 \times 4 = 4.0\times10^{8}\ \text{bytes}
= 400.0\ \text{MB},
$$

a ratio of $600:1$. The cloud model is not a convenience; the download is often
simply not possible. But the ratio is also the price: you have replaced
"download and decide locally" with "trust the platform's reducer". For a
reduction this drastic, the reducer's definition must be part of the record.

### 6.1 A bound on the compositing bias

For a stack in which a fraction $f$ of samples is contaminated by an additive
bias $b$, the sample **mean** is biased by exactly $f\,b$. In the synthetic
cube the clouds brighten the surface by $b = +0.25$ and the cloud fraction is
$f = 0.25$, so the mean-of-stack bias would be

$$
f\,b = 0.25 \times 0.25 = +0.0625
$$

in reflectance. The unmasked **median** measured in the demonstration is biased
by only $+0.0397$ — smaller than the mean bound, because the median discounts a
contaminated sample to its *rank* rather than to its value. Two useful readings:
the compositing bias can never exceed $f\,b$, and the gap between the mean bound
($+0.0625$) and the median result ($+0.0397$) is the robustness the order
statistic buys. The residual $+0.0397$ is what the mask fails to remove.

## 7. Assumptions and regime of validity

1. **The platform's assets equal the archive's assets.** A collection is a view;
   if it lags the archive or applies an undocumented harmonisation, your result
   inherits that choice.
2. **The reducer is deterministic.** Lazy, distributed execution can introduce
   order-dependence in floating-point sums; a mean over chunks may not be
   bit-identical to a mean over the whole array.
3. **The mask is adequate for the question.** A mask tuned to remove bright
   clouds may miss thin cloud and cloud shadow; a shadow is *dark*, so a
   bright-cloud mask leaves a low bias.
4. **The region and window are stated exactly.** A one-pixel change in the ROI
   or one-day change in the window changes the stack and the answer.
5. **Egress is the binding constraint.** For a small region or a short window,
   downloading is simpler and *more* reproducible; the cloud model is not
   automatically better.
6. **The compute is charged, if not in money then in access.** Quotas and
   limits are real constraints on the design, and an algorithm that is
   "obviously" fine may be rejected.

## 8. Worked example — choosing between download and reduce

A study needs the mean surface reflectance over a $2000\times2000$ pixel region
for one year at $16$-day revisit (about $23$ observations), $4$ bands,
$4$ bytes.

1. Full stack: $2000^2 \times 23 \times 4 \times 4 = 1.47\times10^{9}$ bytes
   $\approx 1.47\ \text{GB}$.
2. A one-number summary: $2000^2 \times 4 = 1.6\times10^{7}$ bytes
   $= 16\ \text{MB}$.

The ratio is about $92:1$. Either is feasible locally; the deciding question is
not volume but **control**. If the study must vary the mask interactively,
having the pixels locally is worth $1.5\ \text{GB}$. If the study will fix one
reducer and run it on many regions, reducing at source is worth the loss of
control — provided the reducer is recorded. Notice that the honest answer is a
*decision with a stated criterion*, not a rule.

## 9. Worked example — the mask's blind spot

Using §4, suppose a downstream model uses the composite only where the *flagged*
clear count exceeds $25$. Within the cloudy corner the flagged count averages
$(1 - 0.85 \times 0.8)\times 60 = 19.2$, so the corner is excluded — good. But
elsewhere the flagged count is about $49.2$, while the true count is $46.7$.
Because the mask misses $20\%$ of clouds, a pixel with a flagged count of $26$
may have a true count near $26 - 0.2\times(\text{clouds})$, i.e., closer to the
threshold than it appears. The practical rule: **threshold on a conservative
estimate of the true count, not on the flagged count**, or state the mask
accuracy and propagate it.

## Mastery checkpoint

Complete this without notes.

> A platform returns a masked median composite, and for one pixel the mask
> flags $12$ of $60$ observations as cloud. **(a)** If the mask detects $80\%$
> of true clouds and the cloud cover is $25\%$, estimate the actually-clear
> count and compare it with the flagged clear count. **(b)** State whether the
> composite's bias is more likely positive (bright clouds leak through) or
> negative (cloud shadows leak through), and why the sign of the mask's error
> matters. **(c)** The same query against a reprocessed version returns a value
> $0.01$ higher. Give the two-step reproducibility fix. **(d)** State one task
> for which you would download the pixels instead of reducing at source, and one
> for which you would reduce.

A worked version appears in the
[solutions](exercises/02-cloud-platforms-solutions.md).

## Common pitfalls

1. **Reporting a composite without its observation count.** A gap-filled pixel
   is not a measurement.
2. **Trusting the mask as truth.** It has false negatives; sometimes also false
   positives.
3. **Assuming a median removes clouds.** It removes a *minority* of outliers,
   not a majority.
4. **Quoting a collection without a version.** Reprocessing changes the answer.
5. **Confusing access with permission.** Free to query is not free to
   redistribute; see [17-07-03](03-data-discovery.md).
6. **Over-reducing.** A reducer chosen for speed may bury the spatial structure
   the question needed.
7. **Treating egress as the only cost.** Quota, latency and control are costs
   too.

## Related modules

- [17-07-01 Landsat, Sentinel and MODIS Data Products](01-landsat-sentinel.md)
  — what the platform serves, and at which level.
- [17-07-04 Satellite Time Series and Trend Analysis](04-time-series-satellite.md)
  — the reducer that turns a cube into a trend.
- [22-02-05 Data Versioning](../../22-data-engineering-reproducibility/02-reproducible-workflows/05-data-versioning.md)
  — versioning as a general practice.
- [22-04-05 Cloud-Native Geoscience](../../22-data-engineering-reproducibility/04-databases-and-large-data/05-cloud-native-geoscience.md)
  — the storage formats that make compute-at-source possible.

## Materials

- Demonstration: [`code/cloud_platforms_demo.py`](code/cloud_platforms_demo.py)
  — cube, masking, valid counts, version shift and the egress arithmetic.
- Exercises: [`exercises/02-cloud-platforms-exercises.md`](exercises/02-cloud-platforms-exercises.md)
  with [solutions](exercises/02-cloud-platforms-solutions.md).
