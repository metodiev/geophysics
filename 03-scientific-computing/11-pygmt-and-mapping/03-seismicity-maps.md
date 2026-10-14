---
id: 03-11-03
title: "Plotting Seismicity, Focal Mechanisms and Plate Boundaries"
level: advanced
prereqs: ["03-11-02", "03-10-01"]
estimated_minutes: 120
tags: [pygmt, seismicity, focal-mechanisms, gutenberg-richter, tectonics]
---

# Plotting Seismicity, Focal Mechanisms and Plate Boundaries

A seismicity map is a plot of a catalogue, and a catalogue is a biased sample of
what the Earth did. Magnitudes are truncated by detection, depths by location
quality, and the symbol sizes in the figure are a non-linear function of the
quantity they encode. Nothing about this is solved by drawing it beautifully.

This lesson builds a synthetic catalogue with known properties — so that every
estimator can be checked against the truth that generated it — computes the
statistics a reader will infer from the map, and then plots it with PyGMT.

```bash
.venv/bin/python 03-scientific-computing/11-pygmt-and-mapping/code/seismicity_maps_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Sample** a Gutenberg–Richter catalogue and **recover** its $b$-value with two
   estimators, comparing both with the input.
2. **Quote** the standard error of a $b$-value estimate and explain why the tail
   of a catalogue constrains almost nothing.
3. **Measure** depth and distance statistics, and **state** what each depends on.
4. **Convert** between seismic moment and moment magnitude, and **state** the
   scaling relations a focal-mechanism size implies.
5. **Plot** epicentres, focal mechanisms and a trench line, and **say** what the
   symbol size does and does not encode.

## Prerequisites

- [03-11-02 Gridding, Contours, Shading and Hillshade](./02-grids-and-contours.md)
- [03-10-01 ObsPy Architecture and Data Models](../10-obspy-and-seismic-data/01-obspy-overview.md)
  — the catalogue and waveform formats this lesson's plotting consumes.

## 1. Intuition: a magnitude scale is a logarithm, and a map is linear

Gutenberg–Richter is an exponential law in magnitude,

$$N(M) \propto 10^{-bM},$$

so plotting $\log_{10} N$ against $M$ should give a straight line of slope $-b$.
The moment magnitude scale is logarithmic in energy,

$$M_w = \frac{\log_{10} M_0 - 9.1}{1.5},$$

so an order of magnitude in seismic moment is only $0.67$ in $M_w$. Every step in
this lesson is therefore about the same hazard: **a linear visual encoding of a
logarithmic quantity**. The map's circles, the magnitude axis, the depth range —
all of them compress.

## 2. Precise definitions

**Completeness magnitude $M_c$.** The magnitude above which the catalogue is
complete — every event of that size that occurred was recorded.

**$b$-value.** The slope of the Gutenberg–Richter relation. Near 1.0 for most
tectonic regions, and a measured quantity in any given study.

**Aki–Utsu maximum-likelihood estimator.** For magnitudes above $M_c$ binned with
width $\Delta M$:

$$\hat{b} = \frac{\log_{10} e}{\bar{M} - \left(M_c - \tfrac{\Delta M}{2}\right)}.$$

**Moment magnitude.** $M_w = (\log_{10} M_0 - 9.1)/1.5$ with $M_0$ in N·m.

**Focal mechanism.** The double-couple description of slip on a fault, given as
strike, dip and rake, or as a moment tensor.

**Trench (in this lesson).** A polyline approximating the surface trace of a
subduction zone, used as a distance reference. **The distances measured here are
to the nearest polyline vertex**, which is stated in the output because it is an
approximation that weakens with fewer vertices.

## 3. Derivation: the Aki–Utsu estimator

If magnitudes are exponentially distributed above $M_c$ with

$$p(M) = \beta e^{-\beta(M - M_c)}, \qquad \beta = b\ln 10,$$

then the mean exceeds $M_c$ by $1/\beta$:

$$\mathbb{E}[M] - M_c = \frac{1}{\beta} = \frac{1}{b\ln 10}
\quad\Longrightarrow\quad b = \frac{\log_{10} e}{\mathbb{E}[M] - M_c}.$$

Substituting the sample mean $\bar M$ gives the estimator. With magnitudes binned
to width $\Delta M$, the effective lower bound is $M_c - \Delta M/2$, which gives
the form quoted in Section 2. **The two forms differ only in the denominator, and
that difference is the entire subject of Section 4.**

The standard error of $\hat b$ from $n$ events is approximately

$$\mathrm{SE}(\hat b) \approx \frac{\hat b}{\sqrt{n}},$$

which is the reason a $b$-value from 100 events has a 10 % uncertainty and from
10 000 events has 1 %.

## 4. The measured b-value, two ways

```
  4000 synthetic events generated with b = 1.0 and completeness Mc = 2.5, then rounded to 0.1
  mean(M) measured = 2.926250; the exact exponential mean for b = 1.0 is Mc + 1/(b ln10) = 2.934294
  standard error of the sample mean: 0.006724, so the measured mean is +1.20 standard errors from the theoretical one
  b = log10(e) / (mean(M) - Mc)            = 1.018873
  b = log10(e) / (mean(M) - (Mc - dM/2))   = 0.911904  (Utsu's binning correction)
  input b = 1.0; the two estimators bracket it, and the
  whole difference between them is the 0.05 in the denominator
```

This is the most instructive measurement in the lesson, and it is a small
embarrassment for the naive reading of the formula.

- The sample mean is $1.20$ standard errors **below** the theoretical
  $M_c + 1/(b\ln 10) = 2.934294$ — ordinary sampling variation for $n = 4000$.
- The estimator **without** the binning correction gives $1.0189$, which is 1.9 %
  above the input.
- The estimator **with** Utsu's correction gives $0.9119$, which is 8.8 % *below*
  the input.

Both are defensible and they disagree by more than either disagrees with the
truth. The correction assumes magnitudes are reported at bin centres and the
lower bound is $M_c - \Delta M/2$; my synthetic sample rounds to $0.1$ and takes
the completeness cut at exactly $M_c = 2.5$, so neither convention matches the
sample exactly. **The honest conclusion: state which estimator you used, and do
not quote three significant figures for a $b$-value whose estimator choice moves
it by 9 %.**

### 4.1 The binned slope, and the tail

```
  counts per 0.5 magnitude bin (log10 of the count in brackets):
      M [2.5, 3.0):  2593 [+3.414]
      M [3.0, 3.5):   964 [+2.984]
      M [3.5, 4.0):   314 [+2.497]
      M [4.0, 4.5):    89 [+1.949]
      M [4.5, 5.0):    31 [+1.491]
      M [5.0, 5.5):     6 [+0.778]
      M [5.5, 6.0):     3 [+0.477]
      M [6.0, 6.5):     0 [+0.000]   (and four more empty bins)
  least-squares slope of log10(N) against M over the 5 bins with at least 10 events: -0.9759 (expected -1.0000)
  the sample contains 0 events above M 6; the GR law predicts 1.26 for this catalogue size
  largest event in the sample: M 5.9
```

Three lessons:

- **The binned slope fits only where counts are sufficient.** Over the five bins
  with at least ten events the slope is $-0.9759$ against $-1.0000$, a 2.4 %
  difference. Including the empty bins would require an arbitrary floor and would
  bias the fit.
- **The tail is consistent with the law and constrains nothing.** Zero events
  above $M\,6$ against a prediction of $1.26$: entirely ordinary, and it means a
  $b$-value estimated from the $M > 6$ part of this catalogue would be arithmetic
  on no data.
- **The largest event is $M\,5.9$.** For 4000 events and $b = 1$, the expected
  maximum is around $M_c + \log_{10}(4000)/b \approx 6.1$; a realised 5.9 is
  unremarkable.

## 5. Depth and distance statistics

```
  depth (km): min 3.0, median 12.7, mean 18.45, max 90.0
  fraction shallower than 30 km: 80.4 %; deeper than 60 km: 3.7 %
  distance from each event to the NEAREST TRENCH VERTEX
  (a vertex approximation, not a perpendicular to the segments):
      median 205.78 km, mean 227.25 km, max 709.89 km
      within    25 km of a vertex: 1.1 %
      within    50 km of a vertex: 3.3 %
      within   100 km of a vertex: 12.5 %
  total trench length: 1242.0 km over 4 vertices
```

The depth distribution was generated as an exponential with mean 18 km clipped to
$[3, 90]$ km, and the measured mean of 18.45 km reflects that clipping. The
physical reading — most events shallow, few deep — is the shape of a subduction
catalogue, which is what makes it a useful stage for plotting.

**The distance measurement is the one to be careful with.** The trench here is
four vertices, so "nearest vertex" can exceed the true perpendicular distance
wherever the trace bends; with four vertices over 1242 km the segments are
hundreds of kilometres long and the approximation is poor. Real trench traces
have hundreds of vertices and the vertex approximation converges to the
perpendicular distance. **The fraction within 50 km measured here (3.3 %) is
therefore a property of my four-point polyline as much as of the catalogue**, and
it is stated with its method for that reason.

## 6. Magnitudes, moments and rupture dimensions

```
  Mw = (log10(M0) - 9.1) / 1.5 with M0 in N m
      M0 =  1.0e+15 N m -> Mw =  3.933
      M0 =  1.0e+18 N m -> Mw =  5.933
      M0 =  1.0e+19 N m -> Mw =  6.600
      M0 =  1.0e+21 N m -> Mw =  7.933
      Mw 5.0: rupture length about     10.0 km, width about    7.9 km, area about        79 km^2
      Mw 6.0: rupture length about    100.0 km, width about   25.1 km, area about      2512 km^2
      Mw 7.0: rupture length about   1000.0 km, width about   79.4 km, area about     79433 km^2
      Mw 8.0: rupture length about  10000.0 km, width about  251.2 km, area about   2511886 km^2
```

The scaling relations used are the common ones, $L \approx 10^{M_w - 4}$ km and
$W \approx 10^{0.5M_w - 1.6}$ km. They are **illustrative empirical relations**,
not a measurement here, and they give a $M_w\,9$ rupture 100 000 km long — which
is impossible, and is the reason these relations are only used within their
calibrated range (roughly $M_w\,5$–$8$). The point of printing them is the
dimensional and physical sanity check: **a scaling law extrapolated beyond its
calibration is a wrong answer with a right formula.**

## 7. The map, and what its symbols encode

```
  epicentre symbol sizes: 0.0200 to 0.3743 cm^2, i.e. a factor of 18.7 between the smallest
  and largest event in the catalogue; without the 0.02 offset
  the smallest event would have zero area and would not be drawn at all
  figure: 530 x 611 px, 68539 bytes
```

The size column was built as $s = 0.02 + 0.05(M - M_c)^{1.6}$, so the smallest
event still has a drawable marker. Without the offset, $M = M_c$ gives zero area
and the event disappears — a real defect in many published maps, where the
smallest catalogue events are silently absent.

The map layers, in draw order: basemap frame, coastline, epicentres (magnitude
scaled), the trench polyline, a ridge segment, three focal mechanisms, two labels,
a legend and a depth colour bar. The figure is $530 \times 611$ px at 100 dpi and
68 539 bytes; at 300 dpi it would be about $1590 \times 1833$ px.

**A caveat I must state rather than paper over.** The demonstration prints both
interpretations of the size column — as an area in cm² or as a diameter in cm —
and the ratio between the two radii is not a constant:

```
      M 3.0: size parameter 0.03649 (cm^2 if an area, cm if a diameter)
              as an area: radius 0.10778 cm; as a diameter: radius 0.01825 cm
      M 5.0: size parameter 0.23661 ... radius 0.27444 cm ... 0.11830 cm
      M 7.0: size parameter 0.57477 ... radius 0.42773 cm ... 0.28738 cm
  the radius ratio between the two interpretations, measured:
      M 3.0: 5.90 x
      M 5.0: 2.32 x
      M 7.0: 1.49 x
```

Because the radius is $\sqrt{s/\pi}$ under one reading and $s/2$ under the
other, the discrepancy is $2/\sqrt{\pi s}$ — larger for small markers, and
$5.9\times$ at the smallest magnitude plotted here. **I did not verify in this
environment which interpretation GMT uses for a size column passed to
`fig.plot(style="cc", size=...)`.** I make no claim about it. What is certain is
that the caption has to state the convention, because a reader who assumes the
size is the magnitude — or uses the other convention — will read the map wrong by
a factor that changes from marker to marker.

### 7.1 Focal mechanisms

The three mechanisms are given as strike, dip and rake in a table whose column
order must be exactly

```
longitude, latitude, depth, strike, dip, rake, magnitude
```

because `fig.meca` reads a plain vector table. Two practical notes from building
it: the `depth` column is mandatory (the call fails with a `KeyError` without it),
and the columns are positional, so passing a DataFrame with extra columns raises
`All arrays must have same size`. Passing the seven columns as a NumPy array is
the version that works.

## 8. Assumptions and limitations

- **The catalogue is synthetic**, generated from a Gutenberg–Richter law with a
  stated $b$ and $M_c$, an exponential depth distribution, and a Gaussian spatial
  distribution about a stated latitude. It has no aftershocks, no spatial
  clustering along the trench, and no depth–magnitude dependence. Real catalogues
  have all three, and a $b$-value from a real catalogue is affected by declustering
  choices this lesson does not exercise.
- **The $b$-value estimators disagree by 9 %** on this sample, for reasons given
  in Section 4. The lesson quotes both.
- **Distances are to polylines vertices**, not perpendicular to segments
  (Section 5).
- **The scaling relations of Section 6 are illustrative** and are not used for any
  quantitative conclusion.
- **The size-column interpretation is unverified** (Section 7).
- **The focal mechanism parameters are invented**, in the sense that they are
  chosen to look like a subduction interface, a normal-faulting outer rise and a
  strike-slip event. They are not from any event.
- **No real data is downloaded.** The demonstration runs offline.

## 9. Worked examples

### 9.1 Reading a b-value off a map's catalogue

Suppose a colleague fits $b = 1.02$ from 3000 events in a region and another fits
$b = 0.90$ from 2500 events in the adjacent region. The standard errors are
$1.02/\sqrt{3000} = 0.019$ and $0.90/\sqrt{2500} = 0.018$, so the estimates
differ by about 4.6 combined standard errors — a real difference, provided both
used the same estimator and the same $M_c$. Given Section 4's 9 % estimator
dependence, **the first question to ask is which estimator each used.**

### 9.2 A distance-dependent depth plot

The map's depth colour bar invites the reader to see a dipping plane. With the
measured depths (median 12.7 km, 80.4 % shallower than 30 km) and the measured
distances (median 206 km from the trench), a cross-section plotting depth against
trench distance is the honest version of the claim; a map alone cannot show a
dipping interface because the depth is not a map dimension. Add a depth
cross-section when the point is the dip — that is the subject of
[03-05-04 3-D and Surfaces](../05-plotting-and-visualisation/04-3d-and-surfaces.md).

### 9.3 The legend has to say what the size means

The legend text in the demonstration is explicit: `- M > 2.5 (n = 4000)`. A
legend that says only "magnitude" leaves the reader to assume linearity. Since the
size column here is $(M - M_c)^{1.6}$, a factor of 18.7 in marker area across the
catalogue, the caption must say so: **"circle area proportional to
$(M - 2.5)^{1.6}$"** is one short clause that makes the figure honest.

## 10. Python demonstration

`code/seismicity_maps_demo.py` runs in five parts:

| Part | Result | Key measured output |
|---|---|---|
| 1 | Gutenberg–Richter sample | two $b$ estimates: `1.018873` and `0.911904` |
| 2 | Depth and distance | median depth `12.7` km; `3.3 %` within 50 km of a trench vertex |
| 3 | Moment magnitude | $M_0 = 10^{19}$ N·m → $M_w = 6.600$ |
| 4 | The map | `530 x 611` px, `68539` bytes, 3 mechanisms |
| 5 | Symbol semantics | size range `0.0200`–`0.3743`, factor `18.7` |

The script writes its figure into a scratch directory and deletes it before exit.
It downloads nothing.

## 11. Exercises

Solutions are in
[`exercises/03-seismicity-maps-exercises.md`](./exercises/03-seismicity-maps-exercises.md).

### ★ Foundational

**★1.** Convert to $M_w$: (a) $M_0 = 10^{16}$ N·m, (b) $M_0 = 10^{20}$ N·m,
(c) $M_0 = 5\times10^{18}$ N·m.

**★2.** For $b = 1.0$ and $M_c = 2.0$, how many events of $M \ge 5.0$ does a
catalogue of 10 000 events predict?

**★3.** State two ways a real catalogue is a biased sample of what the Earth did.

**★4.** What do strike, dip and rake describe?

### ★★ Applied

**★★5.** Reproduce the $b$-value measurement for $n = 500$ and $n = 20\,000$
events with the same seed, and report both estimates and their standard errors.
State how the estimator disagreement scales with $n$.

**★★6.** Fit the binned slope with and without the empty bins and report both
slopes. Explain which you would quote.

**★★7.** Build the same map with a logarithmic size column,
$s = 0.02 + 0.05\log_{10}(M - M_c + 1)$, and report the size range. State which
of the two encodings you would use and why.

**★★8.** Replace the four-vertex trench with a 100-vertex polyline interpolated
along the same path, and report the change in the fraction of events within 50 km.
State whether the change is what you expected.

### ★★★ Research-oriented

**★★★9.** Design a completeness test. Using your synthetic catalogue, compute
(a) the maximum curvature of the magnitude–frequency distribution and (b) the
goodness-of-fit test of the GR fit as a function of a trial $M_c$, and report the
$M_c$ each method returns against the input of 2.5. Then state which you would
trust on a real catalogue and what would change if the catalogue had a magnitude
rounding interval different from the one you used.

**★★★10.** Quantify the symbol-size distortion. For a magnitude range
$M_c$–$M_c+4$, compute the marker area, the radius and the ratio to the smallest
event under (a) area proportional to $M - M_c$ and (b) area proportional to
$10^{M}$ (energy-like). Report the two dynamic ranges and state which encoding a
reader is more likely to interpret correctly, citing whatever evidence you can
find — and say plainly if you cannot find any.

## 12. Common mistakes

1. **Quoting a $b$-value to three figures without stating the estimator.** The
   estimator choice moved it by 9 % here.
2. **Fitting the binned slope including empty bins.**
3. **Sizing markers linearly in magnitude** without saying so in the caption.
4. **Letting the smallest event vanish** because its size column is zero.
5. **Reading a dipping interface from a map.** Depth is not a map dimension.
6. **Forgetting the `depth` column when plotting mechanisms.**
7. **Assuming a scaling relation holds outside its calibrated magnitude range.**
8. **Calling a vertex-distance statistic a distance-to-trench statistic.**

## 13. Real-world applications

- **Routine catalogue analysis.** $b$-values, completeness and depth distributions
  are the standard first pass on any regional catalogue.
- **Seismic hazard.** Magnitude–frequency relations and maximum-magnitude
  estimates feed directly into recurrence intervals.
- **Subduction-zone geometry.** Distances to the trench, combined with depth, are
  the first-order constraint on slab dip.
- **Moment tensor catalogues.** Plotting mechanisms on a map is how a stress
  regime is communicated; the conventions matter because a mechanism is
  symmetric under a 180° rotation.
- **Reporting.** A figure with a stated size convention, a stated $M_c$ and a
  stated distance reference is one a reviewer can check.

## 14. Further reading

- **PyGMT documentation** (pygmt.org). Level: advanced. The `plot`, `meca`,
  `legend` and `colorbar` pages, including the `convention` values for mechanisms.
- **ObsPy documentation** (docs.obspy.org). Level: intermediate. Reading real
  catalogues (QuakeML, ISC, USGS) into the tables this lesson plots.
- **Gutenberg, B. & Richter, C. F. (1944). Frequency of earthquakes in California.
  *Bulletin of the Seismological Society of America*, 34(4), 185–188.** Level:
  advanced. The original magnitude–frequency relation.
- **Aki, K. (1965). Maximum likelihood estimate of b in the formula log N = a − bM
  and its confidence limits. *Bulletin of the Earthquake Research Institute*,
  43, 237–239.** Level: advanced. The estimator of Section 3.
- **Utsu, T. (1965). A method for determining the value of b in a formula log n =
  a − bM showing the magnitude–frequency relation for earthquakes. *Geophysical
  Bulletin of the Hokkaido University*, 13, 99–103.** Level: advanced. The binning
  correction whose effect is measured in Section 4.
- **Wessel, P. & Smith, W. H. F. (1991). Free software helps map and display data.
  *EOS Transactions AGU*, 72(41), 441–446.** Level: intermediate. The GMT paper
  that introduced the design PyGMT wraps.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 15. Related lessons

- [01 PyGMT Fundamentals and the GMT Ecosystem](./01-pygmt-basics.md)
- [02 Gridding, Contours, Shading and Hillshade](./02-grids-and-contours.md)
- [04 Layout, Insets, Legends and Multi-Panel Maps](./04-inset-and-layout.md)
- [03-10 ObsPy and Seismological Data Handling](../10-obspy-and-seismic-data/README.md)
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) — the
  estimation theory behind Sections 3 and 4.

## 16. Self-assessment checklist

- [ ] I can sample a GR catalogue and recover $b$ two ways. (§4)
- [ ] I can quote the standard error of a $b$-value. (§3)
- [ ] I can say why the tail of a catalogue constrains little. (§4.1)
- [ ] I can convert between $M_0$ and $M_w$. (§6)
- [ ] I can build a magnitude-scaled map whose smallest event is still visible.
      (§7)
- [ ] I can state what a focal mechanism's parameters mean. (§2)
- [ ] I can say what a distance-to-trench statistic depends on. (§5)
- [ ] I can write a caption that makes the symbol size unambiguous. (§9.3)
