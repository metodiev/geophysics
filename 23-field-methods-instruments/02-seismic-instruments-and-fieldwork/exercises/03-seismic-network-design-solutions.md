# Solutions — 23-02-03 Seismic Network Design and Station Siting

> Read after attempting. Lesson:
> [03 Seismic Network Design](../03-seismic-network-design.md). All values are
> **SYNTHETIC**.

---

## ★1 — Six stations, three coincident detections

With $N = 6$, $k = 3$ and $p = 0.5$, $1-p = 0.5$ and the binomial terms are
$\binom{6}{j}$:

$$P_{\text{net}} = \sum_{j=3}^{6}\binom{6}{j}(0.5)^{j}(0.5)^{6-j}
= \frac{20 + 15 + 6 + 1}{64} = \frac{42}{64} = 0.65625 .$$

Raising the threshold to four detections keeps only $j = 4, 5, 6$:

$$P_{\text{net}} = \frac{15 + 6 + 1}{64} = \frac{22}{64} = 0.34375 .$$

The threshold nearly halves the detection probability at $p = 0.5$ — and note that
$p = 0.5$ per station is exactly the magnitude at which a *single* station is
50 % likely to detect, which is the point of the lesson: the network's
50 % completeness is well above the station's.

---

## ★2 — Azimuthal gap

Sort the azimuths: 10, 25, 40, 200, 215, 230. The gaps between consecutive
stations, including the wrap from 230° to 10° + 360° = 370°:

$$\Delta = \{15, 15, 160, 15, 15, 140\}\ \text{degrees}, \qquad
\text{gap} = \max \Delta = 160^\circ .$$

**Judgement.** A 160° gap means that a 160° sector contains no station, so an
event beneath that sector is constrained only by arrivals from the far side. The
resulting ellipse is elongated in the direction of the gap and the depth is often
poorly constrained. Common design practice is to keep the gap below 180° for
regional work and below 120° where good depth control is required; the acceptable
value depends on the target and must be stated as a criterion rather than assumed.

**Cheapest change.** Place one station in the middle of the 160° gap (near 320°
azimuth). That single station reduces the largest gap from 160° to about 80° for
the cost of one site, and is far more valuable than a second station near any
existing azimuth. This is the "marginal contribution to the largest gap" rule of
Section 6.

---

## ★★3 — Ring network uncertainty

$$\sigma_h = \frac{2V\sigma_t}{\sqrt{N}} = \frac{2 \times 6.0 \times 0.05}{\sqrt{16}}
= \frac{0.6}{4} = 0.150\ \mathrm{km}.$$

**Stations for $\sigma_h = 0.10\ \mathrm{km}$.** Invert the relation:

$$\sqrt{N} = \frac{2V\sigma_t}{\sigma_h} = \frac{0.6}{0.10} = 6
\;\Rightarrow\; N = 36 \text{ stations}.$$

Because $\sigma_h \propto N^{-1/2}$, halving the uncertainty needs *four times* the
stations: 16 → 64 for $\sigma_h = 0.075$ km, and so on. Uncertainty in location
is expensive to buy with stations.

**The assumption.** That the stations form a *uniform ring* with the source at its
centre, so that $\sum\cos^{2} = \sum\sin^{2} = N/2$ and the cross terms vanish, and
that pick errors are independent Gaussians of equal variance with a known
homogeneous velocity. Real geometries are not rings and the source is never at the
centre; the value is a benchmark, not a prediction.

---

## ★★4 — Ring array resolution at 2 Hz

The first zero of $J_0$ is at 2.405, so

$$|\Delta s| = \frac{2.405}{2\pi f R}
= \frac{2.405}{2\pi \times 2 \times 1000} = 1.9138\times10^{-4}\ \mathrm{s/m}
= 0.1914\ \mathrm{s/km}.$$

**Velocity resolution.** With slowness $s = 1/V$, $ds = -dV/V^{2}$, so

$$|\Delta V| = V^{2}|\Delta s| = (3.0)^{2} \times 1.9138\times10^{-4}
= 1.72\times10^{-3}\ \mathrm{km/s} = 1.72\ \mathrm{m/s}.$$

Units: $\Delta s$ in s/m or s/km; the conversion to velocity requires $s$ in
s/km and $V$ in km/s, giving $\Delta V$ in km/s. Note the quadratic penalty: at
$V = 6\ \mathrm{km/s}$ the same array would resolve only $6.9\ \mathrm{m/s}$,
because a given slowness difference corresponds to a larger velocity difference at
higher velocity. Resolution in slowness is geometry; resolution in velocity is
geometry times the velocity squared.

---

## ★★★5 — Designing the temporary network

**Step 1: minimum station count.** At the target magnitude $m = 1.5$ the
per-station detection probability is

$$p(1.5) = \frac{1}{1 + e^{-(1.5-1.2)/0.25}} = \frac{1}{1+e^{-1.2}} = 0.7685 .$$

With a threshold of $k = 4$ coincident detections, evaluate
$P_{\text{net}}(N)$ for increasing $N$:

| $N$ | $P_{\text{net}}(1.5)$ |
|---|---|
| 4 | 0.3488 |
| 5 | 0.6718 |
| 6 | 0.8588 |
| 7 | 0.9453 |
| 8 | 0.9803 |

The requirement is $P_{\text{net}} \ge 0.90$, so **$N = 7$** is the minimum
(six stations give 0.8588, which fails). Seven stations meet the detection target
with a little margin; eight would give 0.9803.

**Step 2: siting.** Seven stations cannot form a uniform ring with the required
station quality unless the site allows it, so site by azimuthal sector: divide the
map into seven sectors, choose the best available site in each (access, noise,
geology, power) and compute the gap of the resulting set. If the available sites
concentrate in a valley, accept that the gap will be large and report it as a
design limitation rather than discovering it after the campaign.

**Step 3: expected location accuracy.** Take an eight-station ring of radius 20 km
as the reference (the lesson's ring case):

$$\sigma_h = \frac{2V\sigma_t}{\sqrt{N}} = \frac{2 \times 6.0 \times 0.05}{\sqrt{8}}
= \frac{0.6}{2.828} = 0.212\ \mathrm{km}.$$

For the realistic road-following geometry of the lesson's Section 3 the same
$N = 8$ gives $\sigma_h = 81.151\ \mathrm{km}$ with an azimuthal gap of 350.4° —
a design that meets the detection requirement and fails any location requirement.
A seven-station deployment with a gap of, say, 200° would land between these two
cases; the only way to know which side of acceptable it lands on is to invert the
design matrix for the actual coordinates.

**Step 4: the requirement that forces more stations.** Depth control. Depth is
constrained by stations with small source–receiver distance, so a network designed
for epicentral accuracy with a large nearest-station distance will have depth
errors of tens of kilometres. If the scientific target includes depth (aftershock
relocation, a seismogenic-zone study), the design must add at least one station
inside or adjacent to the target volume — an eighth or ninth station chosen for
proximity, not for azimuth. That is the requirement that forces the addition.

---

## ★★★6 — Measuring the achieved completeness magnitude

**Data.** A catalogue for the network's operating period and region: origin times,
hypocentres, magnitudes and the number of stations contributing to each solution,
together with the station metadata (operating intervals, sensor, gain) so that
periods of reduced network strength can be identified. The key derived field is
the *detection state* of the network at each origin time: how many stations were
operating, and how far away each was.

**Estimator.** Three complementary approaches, which should agree:

1. **Maximum curvature.** Take the cumulative or non-cumulative magnitude
   frequency distribution of the catalogue, and fit the Gutenberg–Richter
   relation to the well-recorded part; $M_c$ is the magnitude at which the
   observed counts fall below the extrapolated straight line by a stated amount,
   or where the curve's curvature is maximal. Report the fitting range, because the
   answer moves with it.
2. **b-value stability.** Compute the $b$-value while raising the trial $M_c$; the
   estimate stabilises once the trial value exceeds the true $M_c$. The criterion
   is a threshold on $|db/dM_c|$.
3. **Goodness-of-fit (the $R$ statistic).** Compare the observed cumulative
   distribution with the Gutenberg–Richter fit shifted at each trial $M_c$ and take
   the value that maximises a fit statistic.

**Metric and uncertainty.** Report $M_c$ with a *bootstrap* confidence interval:
resample the magnitudes with replacement (or use a block bootstrap over time),
recompute $M_c$ for each resample, and quote the 5th and 95th percentiles. A
single number without an interval is not a measurement.

**Two biases specific to self-assessment.**

1. **Circularity.** The catalogue is produced by the network being assessed, so
   $M_c$ estimated from it is the threshold at which *that network and that
   processing* produced events, not a physical property. A change in the
   processing code, in the analyst, or in the association parameters moves the
   apparent $M_c$ with no change in the network. The test is to re-process a
   fixed, archived data set with the old and new processing and compare the
   resulting catalogues.
2. **Temporal and spatial non-stationarity of detection.** The network changes:
   stations fail, are added, or lose gain, and detection probability varies with
   distance. A single $M_c$ for a multi-year catalogue averages over those states
   and hides the periods of poor performance. Report $M_c$ per calendar year (and
   ideally per station-subset), or restrict the analysis to periods when the
   operating configuration, verified from the station metadata, is stable.

A third, more subtle bias is that repeated events near the detection threshold are
reported with magnitude estimates biased upward (the "magnitude is at least large
enough to be detected" effect), which flattens the magnitude–frequency curve just
above $M_c$ and biases $b$ as well as $M_c$.
