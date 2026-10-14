---
id: 23-02-03
title: "Seismic Network Design and Station Siting"
level: doctoral
prereqs: ["23-02-01", "06-04-01"]
estimated_minutes: 120
tags: [seismology, network-design, detection, location, array, siting]
---

# Seismic Network Design and Station Siting

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the probability that an $N$-station network declares an event, from
   a per-station detection probability and a coincidence threshold, and **derive** the network magnitude of completeness from it.
2. **Formulate** the linearised location problem as a design matrix and **compute** the horizontal error ellipse from the model covariance.
3. **Derive** the closed-form horizontal uncertainty of a uniform ring network and use it as a design benchmark.
4. **Compute** the azimuthal gap of a candidate geometry and **explain** its dominant role in location uncertainty.
5. **Compute** the array main-lobe width, the first-sidelobe level and the grating-lobe position, and **decide** whether the grating lobe lies inside the physically reachable slowness range.
6. **Compute** the spatial aliasing limit $f_{\max} = V_{\min}/(2\Delta x)$ and
   **state** why the site's lowest velocity sets it.
7. **Diagnose** a design that is strong in detection and weak in location (or the reverse), and **propose** the single station that would most improve it.

All networks, magnitudes, detection probabilities, velocities and geometries in
this lesson are **SYNTHETIC**. No real network, catalogue completeness estimate or
measured array response is used or reproduced.

## Prerequisites

- [01 Seismometers: Broadband, Short-Period, Geophones, MEMS](01-seismometers.md) —
  what each station contributes to the network.
- [06-04-01 Hypocentre Location: Arrival Times, Inversions and Error Ellipses](../../06-seismology/04-earthquake-location-and-magnitude/01-hypocentre-location.md) —
  the inversion this lesson designs for.

## 1. Intuition: a network is not a station count

A seismic network is a set of coupled decisions: how many stations, where they
sit, what each sensor measures, how a detection is declared and what the resulting
data can resolve. Those decisions trade against each other, and they trade
differently for the three things a network is usually asked to do:

- **Detect** events above some size (a statement about probability and threshold);
- **Locate** them (a statement about geometry);
- **Resolve** the wavefield (a statement about aperture and sampling).

Adding a station improves all three, but never equally, and sometimes not at all:
a tenth station next to the ninth adds detection redundancy and nothing to
geometry, whereas one station 100 km away in an empty azimuth sector can halve
the location error.

The design loop is therefore: state the target (a magnitude and a location
quality), compute the *marginal* contribution of each candidate site, place the
station that contributes most, and repeat. This lesson supplies the arithmetic for
each step.

## 2. Detection is a network property

Let $p(m)$ be the probability that one station detects an event of magnitude $m$,
and require $k$ of $N$ stations to declare an event. If detections are independent
across stations,

$$P_{\text{net}}(m) = \sum_{j=k}^{N} \binom{N}{j} p(m)^{j}\left[1-p(m)\right]^{N-j}.$$

The demonstration uses a logistic per-station curve,
$p(m) = 1/(1 + e^{-(m-M_{50})/s})$ with $M_{50} = 1.2$ and $s = 0.25$ magnitude
units, $N = 8$ and $k = 4$:

| $m$ | $p$ (1 station) | expected detections | $P_{\text{net}}$ |
|---|---|---|---|
| 0.0 | 0.0082 | 0.07 | 0.0000 |
| 0.5 | 0.0573 | 0.46 | 0.0006 |
| 1.0 | 0.3100 | 2.48 | 0.2127 |
| 1.2 | 0.5000 | 4.00 | 0.6367 |
| 1.5 | 0.7685 | 6.15 | 0.9803 |
| 2.0 | 0.9608 | 7.69 | 1.0000 |
| 2.5 | 0.9945 | 7.96 | 1.0000 |

The **magnitude of completeness** $M_c$ of the network is the magnitude at which
$P_{\text{net}}$ crosses a stated level: 1.140 at 0.50, 1.361 at 0.90 and 1.549 at
0.99. Three consequences are worth stating explicitly.

1. **$M_c$ is a property of the network, not of a station.** The same single
   station has $p = 0.5$ at $m = 1.2$, yet the network's 90 % completeness is at
   1.361, because the network needs four coincident detections.
2. **The threshold choice moves $M_c$.** Raising $k$ from 4 to 5 shifts the whole
   curve right and raises $M_c$; lowering it admits more false events. The choice
   is a detection-versus-false-alarm decision, not a technical detail.
3. **The curve saturates.** Above $m = 2$ the network is certain to detect, so
   adding stations buys nothing for detection there — but it still buys location geometry.

The independence assumption behind the binomial is the weak point: real stations
share noise sources (weather, cultural activity, a common microseism field), so
detections are positively correlated and $P_{\text{net}}$ is overestimated where
$p$ is near 0.5. The binomial is a design tool; a measured detection curve from a
catalogue is the real check.

## 3. Location geometry

For a source at the origin with an unknown origin time, the arrival time at
station $i$ is $t_i = t_0 + d_i/V$. Linearising about the true source position, the
design matrix rows are

$$g_i = \left[-\frac{x_i}{V d_i},\; -\frac{y_i}{V d_i},\; 1\right],$$

and the model covariance is $\mathbf{C} = \sigma_t^{2}(\mathbf{G}^{\mathsf T}
\mathbf{G})^{-1}$ for independent pick errors of standard deviation $\sigma_t$. The
horizontal uncertainty is

$$\sigma_h = \sqrt{C_{xx} + C_{yy}} .$$

For a uniform ring of $N$ stations at radius $R$ with the source at the centre,
$\sum \cos^{2} = \sum \sin^{2} = N/2$ and all cross terms vanish, giving the
closed form

$$\sigma_h^{\text{ring}} = \frac{2V\sigma_t}{\sqrt{N}} .$$

The demonstration measures exactly this: with $V = 6.0\ \mathrm{km/s}$,
$\sigma_t = 0.05\ \mathrm{s}$ and $N = 8$, the closed form gives 0.212 km and the
numerical inversion gives $\sigma_h = 0.212\ \mathrm{km}$, with
$a = b = 0.150\ \mathrm{km}$ (a circular ellipse) and a 95 % area of
$0.4\ \mathrm{km^2}$.

Now replace the ring with **eight stations along an access road**, spread over
18–22 km in a narrow azimuth band — the geometry that results whenever deployment
follows the roads:

| Geometry | azimuthal gap | $\sigma_h$ (km) | $a$ (km) | $b$ (km) | 95 % area (km²) |
|---|---|---|---|---|---|
| along an access road | 350.4° | 81.151 | 81.128 | 1.938 | 2959.9 |
| even ring, 20 km | 45.0° | 0.212 | 0.150 | 0.150 | 0.4 |

Same number of stations, same sensors, same picks — a factor of **383** in
$\sigma_h$ and a factor of about 7400 in the 95 % ellipse area. The azimuthal gap
(350.4° versus 45.0°) is the single number that predicts this.

The practical rules that follow:

- **Instruments where the geology is, but site where the geometry is.** The
  dominant control on location quality is azimuthal coverage, and it is cheap to
  check on a map before mobilisation.
- **A gap beyond about 180° is a warning; beyond 270° the depth is usually
  unconstrained as well.** The exact thresholds depend on the target and the
  required accuracy, and should be stated as design criteria rather than assumed.
- **Depth resolution is a separate problem** and requires stations close to the
  source. A wide-aperture network with a large nearest-station distance locates
  epicentres well and depths badly.

## 4. Array response: resolution, sidelobes and grating lobes

For a plane wave arriving with horizontal slowness vector $\mathbf{s}$, the
response of an array of positions $\mathbf{r}_j$ at frequency $f$ to a slowness
offset $\Delta\mathbf{s}$ is

$$R(\Delta\mathbf{s}) = \left|\frac{1}{M}\sum_{j=1}^{M}
e^{-2\pi i f\, \Delta\mathbf{s}\cdot\mathbf{r}_j}\right| .$$

For a continuous ring of radius $R$ this reduces to a Bessel function,
$R = |J_0(2\pi f R |\Delta s|)|$, whose first zero is at
$|\Delta s| = 2.405/(2\pi f R)$. The demonstration reports this resolution limit:

| $f$ (Hz) | $\Delta s$ (s/km) |
|---|---|
| 0.5 | 1.531 |
| 1.0 | 0.766 |
| 2.0 | 0.383 |

and, from a numerical evaluation of the response along a slowness cut at 1 Hz with
a physical limit of $|\mathbf{s}| \le 1/V_{\min} = 2.00\ \mathrm{s/km}$ for
$V_{\min} = 500\ \mathrm{m/s}$:

| Geometry | main lobe (s/km) | first sidelobe (dB) | peak in band (dB) | aliased? |
|---|---|---|---|---|
| ring, 12 at 500 m | 1.471 | −7.9 | −7.9 | no |
| grid, 4×4 at 180 m | 2.657 | −11.3 | −11.3 | no |
| grid, 4×4 at 700 m | 0.683 | −11.3 | −0.0 | yes |

Three design facts emerge.

- **The ring's main lobe is broad but its sidelobes are low** (−7.9 dB, close to
  the Bessel prediction), so a ring is a good choice when a single, unambiguous
  slowness estimate is wanted and the resolution requirement is modest.
- **A sparse grid is sharper** (0.683 s/km) but repeats: the grating lobe at
  $1/(f\Delta x) = 1/(1 \times 700) = 1.43\ \mathrm{s/km}$ falls inside the
  reachable range and reaches −0.0 dB, i.e. it is a second, equally strong
  solution. An array with a grating lobe inside the physical range cannot
  distinguish the true slowness from its alias.
- **The physical range is set by the site, not the array.** The same 700 m grid is
  alias-free where $V_{\min}$ is high (so that $1/V_{\min}$ is small) and aliased
  where it is low. This is why site velocity information is required before an
  array is designed.

## 5. Spatial sampling of the wavefield

The wavefield is aliased when the station spacing is too large for the highest
wavenumber present. With a minimum apparent velocity $V_{\min}$ and spacing
$\Delta x$,

$$f_{\max} = \frac{V_{\min}}{2\Delta x}, \qquad k_{\text{Nyq}} = \frac{\pi}{\Delta x}.$$

The demonstration's table:

| $\Delta x$ (m) | $V_{\min}$ (m/s) | $f_{\max}$ (Hz) | $k_{\text{Nyq}}$ (rad/m) |
|---|---|---|---|
| 25 | 500 | 10.0 | 0.12566 |
| 25 | 1500 | 30.0 | 0.12566 |
| 100 | 1000 | 5.0 | 0.03142 |
| 100 | 3000 | 15.0 | 0.03142 |
| 250 | 3000 | 6.0 | 0.01257 |

The rule is used backwards in practice: from the highest frequency of interest
$f_{\text{target}}$ and the lowest velocity expected, the required spacing is
$\Delta x \le V_{\min}/(2 f_{\text{target}})$. For a 30 Hz target in a basin with a
300 m/s surface layer, $\Delta x \le 5\ \mathrm{m}$ — which is why strong-motion
arrays and microzonation surveys use such tight spacings while regional networks
spaced at 30 km accept a $f_{\max}$ of order 0.05 Hz.

## 6. The design loop, and what to do with a fixed number of stations

1. **State the target** as a magnitude with a probability and a location accuracy
   with a confidence level: for example "detect $M \ge 1.5$ with 90 % probability"
   and "locate with $\sigma_h \le 0.5\ \mathrm{km}$".
2. **Compute the detection requirement** from Section 2 — here $P_{\text{net}}
   (1.5) = 0.9803$ with 8 stations and $k = 4$, so the target is met.
3. **Compute the geometry** from Section 3. If the candidate deployment follows roads, the gap will be large and the location target will fail even though detection passes. This is the most common failure of a real design.
4. **Add stations by marginal contribution.** For each empty azimuth sector, ask what the ellipse does if a station is placed there. A station that reduces the
   largest gap most reduces $\sigma_h$ most.
5. **Check the array and sampling criteria** only if the network is also used for wavefield work (Sections 4 and 5); for a detection/location network they are secondary.
6. **Record the criteria** with the design, so that a later change (a station lost to vandalism, a site moved) can be evaluated against them.

## 7. Assumptions and regime of validity

1. **Station independence.** The binomial detection model overstates $P_{\text{net}}$
   when stations share noise. Report it as a design estimate.
2. **A known and homogeneous velocity.** The design matrix uses a single velocity; with real structure, both the location and the ellipse change, and the ellipse of a linearised inversion is a lower bound on the true uncertainty.
3. **Gaussian pick errors, uncorrelated between stations.** Real pick errors are correlated through the shared waveform and the shared analyst practice.
4. **Small errors.** The covariance is the linearised (Gauss–Newton) covariance; for a source outside the network or a large error, the nonlinear uncertainty is much larger and asymmetric.
5. **A point source and a plane-wave array model.** Both ignore finite-source effects and near-field terms; the array response of Section 4 is the far-field transfer function only.
6. **The velocity used for the physical slowness limit is $V_{\min}$.** If the site
   has a low-velocity layer that is not known when the array is deployed, the array can be aliased in ways the design did not anticipate.

## 8. The honest summary

- $M_c$ is a network property, and it moves with the coincidence threshold:
  1.140 at $P = 0.5$, 1.361 at $P = 0.9$, 1.549 at $P = 0.99$ for this model.
- Eight stations give $\sigma_h = 0.212\ \mathrm{km}$ on a ring and
  $81.2\ \mathrm{km}$ along a road; the azimuthal gap is the reason.
- A ring resolves slowness broadly and cleanly; a sparse grid resolves sharply but
  repeats, and a repeat inside the physical range is fatal.
- Spacing is set by the site's *lowest* velocity, not its average.
- Design by marginal contribution to the largest gap, and write the criteria down.

## 9. Python demonstration

[`code/seismic_network_design_demo.py`](./code/seismic_network_design_demo.py)
prints every number quoted above. It:

1. evaluates the network detection probability for an 8-station, 4-detection
   network and solves for $M_c$ at three probability levels;
2. inverts the linearised location problem for an access-road deployment and a ring
   and reports the gaps, $\sigma_h$, the ellipse axes and the 95 % area;
3. evaluates the array response along a slowness cut for a ring and two grids and reports the main lobe, the first sidelobe and whether a grating lobe lies inside
   the physical slowness range;
4. tabulates $f_{\max}$ and $k_{\text{Nyq}}$ for five spacing/velocity pairs.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/02-seismic-instruments-and-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_network_design_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/03-seismic-network-design-exercises.md`](./exercises/03-seismic-network-design-exercises.md)
and
[`exercises/03-seismic-network-design-solutions.md`](./exercises/03-seismic-network-design-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. Six stations each detect with $p = 0.5$ and three coincident detections are
   required. Compute $P_{\text{net}}$ exactly.
2. Station azimuths are 10°, 25°, 40°, 200°, 215° and 230°. Compute the azimuthal
   gap and state what a designer should do about it.
3. A full ring of 16 stations has $V = 6\ \mathrm{km/s}$ and
   $\sigma_t = 0.05\ \mathrm{s}$. Compute $\sigma_h$ and the number of stations
   needed for $\sigma_h = 0.10\ \mathrm{km}$.
4. A ring of radius 1 km is used at 2 Hz. Compute the slowness resolution and the
   corresponding velocity resolution at $V = 3\ \mathrm{km/s}$.
5. State the spacing required for a 30 Hz target where the surface velocity is
   300 m/s.

## 12. Common pitfalls

1. **Designing from a station count.** Eight stations gave 0.212 km or 81 km; the
   count is not the design.
2. **Following roads and calling it a network.** Access-driven geometry
   concentrates azimuth and the ellipse lengthens across the unobserved sector.
3. **Quoting $M_c$ without the detection rule.** $M_c$ depends on the coincidence
   threshold and on whether it is defined at the 50 % or 90 % level.
4. **Treating a grating lobe as a sidelobe.** A repeat inside the physical slowness
   range is an ambiguity, not a resolution loss.
5. **Using the average velocity for the aliasing criterion.** The lowest velocity
   of the shallowest layer sets it.
6. **Believing the linearised ellipse.** For sources at the network edge, or with
   depth as a free parameter and a large gap, the true uncertainty is far larger
   and asymmetric.
7. **Ignoring depth.** Epicentral accuracy and depth accuracy are controlled by
   different parts of the geometry.

## 13. Where this is used

- Permanent and temporary observatory network design, and the refurbishment of an
  ageing network where a single new site must be chosen.
- Dense array deployments for ambient-noise and receiver-function work, where the
  array response of Section 4 is the design criterion.
- Induced-seismicity monitoring networks, where a magnitude of completeness target
  is usually specified by a regulator and must be demonstrated.
- Microzonation and engineering arrays, where the spacing criterion of Section 5
  dominates every other consideration.
- Network operations: adding a station, or losing one, changes $M_c$ and the
  location quality, and the change can be computed before it happens.

## 14. Related lessons

- [01 Seismometers: Broadband, Short-Period, Geophones, MEMS](01-seismometers.md) —
  what each site must actually record.
- [05 Deployment, Orientation, Timing and Metadata](05-seismic-deployment.md) —
  how the designed network is realised in the ground.
- [06 Field QC: Noise Checks, Continuity, Station Uptime](06-seismic-field-qc.md) —
  whether the network you designed is the network you have.
- [06-02-04 Ray Tracing in Laterally Varying Media](../../06-seismology/02-ray-theory-and-travel-times/04-ray-tracing.md) —
  what replaces the straight-ray design matrix when the structure matters.
- [06-11-01 Gutenberg-Richter, b-Value and Magnitude of Completeness](../../06-seismology/11-earthquake-statistics-and-hazard/01-gutenberg-richter.md) —
  how $M_c$ is estimated from a catalogue and what biases it.
- [23-07-01 Case Study: Deploying a Temporary Seismic Array](../07-field-campaign-case-studies/01-case-study-seismic-array.md) —
  this design loop executed on a real plan.

## 15. Self-assessment checklist

- [ ] I can compute a network detection probability and a completeness magnitude.
- [ ] I can assemble a location design matrix and invert it for a covariance.
- [ ] I can derive and use the ring-network $\sigma_h$ result.
- [ ] I can compute an azimuthal gap and say why it dominates.
- [ ] I can decide whether an array's grating lobe is inside the physical range.
- [ ] I can compute the spacing a target frequency and site velocity require.
