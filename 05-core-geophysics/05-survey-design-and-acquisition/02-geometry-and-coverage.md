---
id: 05-05-02
title: "Array Geometry, Fold, Offsets and Spatial Sampling"
level: advanced
prereqs: ["05-05-01", "02-03-09"]
tags: [geometry, fold, offsets, cmp, 3d-survey, binning, resolution]
---

# Array Geometry, Fold, Offsets and Spatial Sampling

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the fold of a 2-D split-spread survey from the trace density per
   bin, and check it against a measured fold profile.
2. **Explain** what fold buys (noise rejection, in the ratio $\sqrt{\text{fold}}$)
   and what it does not buy (resolution).
3. **Describe** the offset range and the offset distribution, and state which
   part of the wavefield each offset range carries.
4. **Distinguish** 2-D profiles from 3-D arrays, and state the specific ambiguity
   that a 2-D line cannot resolve (out-of-plane energy).
5. **Quantify** the resolution limit of a potential-field survey from the
   separation at which two bodies merge, and say why no processing recovers them.
6. **Design** a bin size and station spacing from an aliasing requirement.

## Prerequisites

- [05-05-01 Survey Planning](./01-survey-planning.md) — the detectability
  arithmetic that decides whether the survey is worth acquiring.
- [02-03-09 Diffraction, Scattering and Resolution Limits](../../02-physics/03-oscillations-and-waves/09-diffraction.md)
  — the Fresnel zone used in Section 5, and the general statement that resolution
  is a wave-physics limit and not an instrument property.

## 1. Intuition: geometry decides what can be resolved, before any processing

Processing is a sequence of linear operators applied to data. It cannot create
information that the acquisition geometry did not record. The geometry makes three
decisions, and they are made only once:

- **Where the samples are** — the station spacing and the bin size, which set the
  Nyquist wavenumber and therefore the aliasing limit
  ([05-05-03](./03-spatial-sampling-theory.md)).
- **How many samples per estimate** — the fold, which sets the noise level of the
  stacked result through $\sqrt{N}$ and nothing else.
- **Which directions and distances were sampled** — the offset and azimuth
  distribution, which sets whether a target at depth can be illuminated and
  located in three dimensions, or merely detected.

The honest statement of the trade-off is this: **fold buys noise rejection;
spacing buys resolution; offsets buy depth reach and velocity information. The
three are bought separately and priced separately.**

## 2. Precise definitions

### 2.1 Common midpoint (CMP) and bin

For a source at $s$ and a receiver at $g$ on a line, the **midpoint** is
$(s+g)/2$ and the **offset** is $|g-s|$. All traces whose midpoints fall in the same
cell of width $b$ (the **bin**) are gathered and stacked.

### 2.2 Fold

The **fold** of a bin is the number of traces that contribute to it. For a
constant-geometry 2-D profile it follows from trace density:

- the number of midpoint positions per shot inside one bin is
  $\dfrac{\Delta x/2}{b}$, since a split spread places midpoints $\Delta x/2$ apart;
- the number of shots whose midpoint coverage includes that bin is
  $\dfrac{N\Delta x/2}{\Delta s} = \dfrac{N\Delta x}{2\Delta s}$, where
  $\Delta s$ is the shot interval.

Multiplying,

$$\boxed{\ \text{fold} = \frac{N\,\Delta x}{2\,\Delta s}\cdot\frac{\Delta x}{2b}\ }
\tag{1}$$

with $N$ the number of live channels, $\Delta x$ the receiver interval, $\Delta s$
the shot interval and $b$ the bin width. For the standard configuration
$\Delta s = \Delta x$ and $b = \Delta x/2$, this reduces to

$$\text{fold} = \frac{N}{2},
\tag{2}$$

a result worth remembering and worth checking by measurement, which Section 4 does.

### 2.3 Offset

The **offset** $x = |g - s|$ ranges from $x_{\min}$ to $x_{\max}$. The **offset
distribution** is the number of traces per offset interval, measured by the demo. A
survey whose offset distribution is concentrated at one offset is poor for velocity
analysis; a survey with a wide, well-sampled distribution constrains velocity,
anisotropy and multiple behaviour.

### 2.4 Azimuth

In three dimensions each trace has an **azimuth**, the compass direction from
source to receiver. Sampling many azimuths makes the survey sensitive to
direction-dependent velocity and to out-of-plane structure; a single tight azimuth
range makes the result sensitive to those effects in a way it cannot detect.

## 3. Derivation: why fold buys only $\sqrt{N}$

Stacking $N$ traces with a perfectly aligned signal $A$ and independent noise of
standard deviation $\sigma$ gives

$$S = \frac{1}{N}\sum_{i=1}^{N}(A + n_i) = A + \frac{1}{N}\sum_i n_i ,
\qquad \operatorname{Var}(S) = \frac{\sigma^2}{N},
\tag{3}$$

so the signal-to-noise ratio improves as

$$\mathrm{SNR}(N) = \sqrt{N}\cdot\frac{A}{\sigma} .
\tag{4}$$

This is the whole content of "fold". Note what it requires:

- **the signal must be aligned** across traces. Statics, NMO and residual
  alignment errors all break this assumption, and their cost in attenuation is
  derived in [05-06-03](../06-data-processing-principles/03-static-and-datum.md);
- **the noise must be independent** across traces. Coherent noise — ground roll,
  power-line harmonics, air blast — is *not* reduced by stacking in proportion to
  $\sqrt{N}$, and in the worst case (identical noise on every trace) it is not
  reduced at all;
- **the improvement is in amplitude ratio, not in resolution.** Fourfold fold
  halves the noise; it does not make the bin smaller.

## 4. Measured fold: the numbers behind equation (1)

[`code/geometry_fold_demo.py`](./code/geometry_fold_demo.py) builds the geometry
explicitly — it generates every source and receiver position, computes every
midpoint and histograms the result — so the fold is measured rather than assumed.
Parameters are *SYNTHETIC*: receiver interval 20 m, one station move per shot,
CMP bin 10 m, 400 shots.

| channels $N$ | max offset (m) | fold (traces/bin) |
|---|---|---|
| 24 | 230 | 12.0 |
| 48 | 470 | 24.0 |
| 96 | 950 | 48.0 |
| 192 | 1910 | 96.0 |

The measured fold is exactly $N/2$, confirming equation (2), and the maximum offset
is $N\Delta x/2$, confirming the geometry.

The fold profile along the line is the part that planning mistakes ignore:

| quantity | measured |
|---|---|
| bins at full fold (48) | 706 of 891 (79.2 %) |
| bins below full fold | 185 (92.5 per end) |
| measured ramp length per end | 925 m of midpoint axis |
| predicted ramp $N\Delta x/2 - \Delta s$ | 940 m |
| fold at the start of the ramp | 1, 2, 2, 3, 3, 4 … |

The measured ramp agrees with the prediction to better than one bin width. The
physical reason is that a bin is fully covered only by shots whose whole split
spread reaches it; the coverage therefore ramps linearly from 1 trace at the line
end to full fold over almost the entire half-spread length. **A target in the first
or last kilometre of a profile is being surveyed at a fraction of the planned
fold**, and the profile must be extended beyond the target for that reason alone.

## 5. Resolution: what geometry decides and processing cannot

### 5.1 The Fresnel zone for wavefield methods

A reflection from depth $h$ with dominant wavelength $\lambda$ is illuminated over
a disc of radius

$$r_F = \sqrt{\frac{\lambda h}{2}} ,
\tag{5}$$

derived from the half-period path difference condition in
[02-03-09](../../02-physics/03-oscillations-and-waves/09-diffraction.md). Measured
values for $\lambda = 100$ m (*SYNTHETIC*: a 25 Hz event at 2500 m/s):

| depth $h$ (m) | $r_F$ (m) | diameter (m) |
|---|---|---|
| 200 | 100.0 | 200.0 |
| 500 | 158.1 | 316.2 |
| 1000 | 223.6 | 447.2 |
| 2000 | 316.2 | 632.5 |

Horizontal resolution therefore degrades as $\sqrt{h}$ — at fixed wavelength.
Tightening the station spacing below $r_F$ does not improve the *image* resolution;
it only removes aliasing. This is the single most common misunderstanding in
seismic survey design, and the reason a 5 m receiver interval in a 2 km deep
survey is money spent on nothing.

### 5.2 The two-body limit for potential fields, measured

For potential fields there is no wavelength and therefore no Fresnel zone; the
limit is the natural width of the anomaly. The demo places two equal point masses
at depth $h$ and varies their separation $s$, measuring the ratio of the field at
the midpoint to the peak:

| separation $s$ | $s/h$ | peak (mGal) | midpoint/peak | resolvable? |
|---|---|---|---|---|
| 75 m | 0.25 | 1.4491 | 1.000 | no |
| 150 m | 0.50 | 1.3543 | 1.000 | no |
| 300 m | 1.00 | 1.0613 | 1.000 | no |
| 600 m | 2.00 | 0.8094 | 0.648 | yes |
| 900 m | 3.00 | 0.7651 | 0.331 | yes |

The midpoint ratio is exactly 1 for all $s \le h$: the summed field is still
maximum at the centre, so **two bodies closer than one body depth produce a single
anomaly**. The demo locates the transition numerically by scanning the separation:

| quantity | value |
|---|---|
| measured critical separation $s_{\text{crit}}$ | 301.06 m, i.e. $1.0035\,h$ |
| analytic value $h$ | 300.00 m, i.e. $1.0000\,h$ |

The analytic value follows from the second derivative of the summed profile at the
midpoint, which vanishes when $s = h$. (An earlier draft of the demo asserted
$s_{\text{crit}} = \sqrt{2}\,h$; the measurement contradicts it, and $s_{\text{crit}}
= h$ is what both the scan and the curvature derivation give. This is the sort of
discrepancy that only a numerical check finds.)

**The consequence is absolute.** No filter, no continuation, no inversion recovers
two bodies from a field that has already merged them: the merged field *is* the
data, and the information needed to split it was never recorded. This is
non-uniqueness in its most concrete form; the general theory is in
[05-01-04 Non-Uniqueness of Geophysical Models](../01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md)
and [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md).

## 6. Worked examples

### 6.1 Fold of a non-standard configuration

A crew uses $N = 240$ channels at $\Delta x = 25$ m, shooting every
$\Delta s = 50$ m (two station moves), with a bin of $b = 12.5$ m. Equation (1):

$$\text{fold} = \frac{240 \times 25}{2 \times 50} \times \frac{25}{2 \times 12.5}
= 60 \times 1 = 60 .$$

Doubling the shot interval halved the fold relative to the standard case with
$\Delta s = \Delta x$. The cost per shot is unchanged; the cost per *useful* bin
doubled. This is why shot interval is a design variable and not a logistics
afterthought.

### 6.2 Bin size from an aliasing requirement

The maximum unaliased frequency on a receiver (or bin) spacing $\Delta x$ for an
event with apparent velocity $v_a$ is

$$f_{\max} = \frac{v_a}{2\Delta x} .
\tag{6}$$

With $\Delta x = 25$ m and $v_a = 2000\ \mathrm{m\,s^{-1}}$ (both *SYNTHETIC*),
$f_{\max} = 40$ Hz. Halving the bin to 12.5 m raises it to 80 Hz. If the target
bandwidth is 60 Hz, the 25 m bin aliases it and the survey must use at most
$\Delta x = v_a/(2 f_{\max}) = 2000/120 = 16.7$ m — the calculation behind
[05-05-03](./03-spatial-sampling-theory.md).

### 6.3 Offset required to illuminate a target

A target at two-way time $t_0$ and interval velocity $v$ is illuminated with useful
incidence angles when the maximum offset satisfies roughly

$$x_{\max} \gtrsim v\,t_0 ,$$

which is the "offset equals depth" rule for a horizontal reflector (since depth
$= v t_0/2$, and offset $\approx$ depth means $x_{\max} \approx v t_0/2$; the
larger value is used to leave room for the moveout to be measurable). For
$t_0 = 1.0$ s and $v = 2500\ \mathrm{m\,s^{-1}}$, $v t_0 = 2500$ m, so a streamer or
spread of at least 2.5 km is required. The measured table in Section 4 shows that
reaching 2500 m with $\Delta x = 20$ m alone would need about 250 channels; in
practice a longer receiver interval is used at far offsets, which is why real
spread designs are not uniform.

## 7. 2-D profiles against 3-D arrays

A 2-D line assumes that all energy arrives from the vertical plane through the
line. That assumption fails in three ways, and each is a real interpretation
error:

| failure | what happens | how 3-D fixes it |
|---|---|---|
| **Sideswipe** | a reflector or a body *beside* the line produces an arrival that the processing places *on* the line, at a wrong depth and position | the cross-line geometry locates energy by azimuth as well as by distance |
| **Out-of-plane potential-field sources** | the line crosses a part of the anomaly, so the profile is a slice, not the full response; the peak is missed and the anomaly is under-estimated | a 3-D grid measures the peak and the shape |
| **Velocity anisotropy and dipping structure** | a single azimuth cannot separate dip from anisotropy | multiple azimuths break the trade-off |

The cost is severe: a 3-D template requires a source and a receiver grid, and the
channel count grows as the square of the areal extent for the same fold. The
planning rule is that 3-D is justified when the target's size is comparable to its
depth (so that a single line cannot pass through the peak) or when the structural
dip is unknown. The demo's measured two-body limit gives the numbers for the first
case: bodies closer than $h$ cannot be separated even on a perfect line, and a
single line will also miss their peak if the pair lies off-line.

## 8. Assumptions

1. **Constant geometry.** Equation (1) assumes the same channel count and spacing
   for every shot. Real surveys change the spread, and the fold must then be
   computed, not quoted.
2. **Flat layering for NMO and the Fresnel formula.** With dip or strong lateral
   velocity change, the bin's traces do not share a midpoint in the subsurface
   (the reflection point smears); dip moveout and prestack migration address this,
   and both need a wider azimuth range than a single line provides.
3. **Bin size is a processing choice, not a physical limit.** A coarser bin raises
   the fold and lowers the resolution; the bin must be chosen from the *shortest
   wavelength to be preserved*, not from the fold target.
4. **Independent noise.** Coherent noise defeats the $\sqrt{N}$ law of Section 3.
5. **Offsets uniform in this idealised model.** The demo measures a uniform offset
   distribution because a constant split spread produces one; real 3-D templates
   do not, and their offset/azimuth coverage must be measured from the template
   geometry file rather than assumed.

## 9. Units and dimensional analysis

Equation (1) must be dimensionless:

$$\left[\frac{N\,\Delta x}{2\,\Delta s}\right] = \frac{1\cdot\mathrm{m}}{\mathrm{m}}
= 1, \qquad
\left[\frac{\Delta x}{2b}\right] = \frac{\mathrm{m}}{\mathrm{m}} = 1 .$$

The Fresnel radius, equation (5), is a length:
$[\sqrt{\lambda h}] = \sqrt{\mathrm{m}\cdot\mathrm{m}} = \mathrm{m}$. The
separation limit is dimensionless in the sense that $s_{\text{crit}}/h = 1$: it is
a statement about a *ratio*, and therefore independent of units — which is why it
is quoted as $s/h$ in the table rather than as metres.

## 10. Python demonstration

[`code/geometry_fold_demo.py`](./code/geometry_fold_demo.py) measures the tables in
Sections 4 and 5. The fold measurement is a literal histogram of midpoints:

```python
offsets = dx / 2.0 + dx * np.arange(n_channels // 2)
offsets = np.concatenate([-offsets[::-1], offsets])
midpoints = np.array([shot * shot_interval + offsets / 2
                      for shot in range(n_shots)]).ravel()
counts, _ = np.histogram(midpoints, bins=np.arange(midpoints.min(),
                                                   midpoints.max() + bin_size,
                                                   bin_size))
fold = int(np.max(counts[1:-1]))          # 48 for N = 96, as equation (2) says
```

The measurement agrees with equation (2) for every channel count tried, and the
ramp at the ends agrees with $N\Delta x/2 - \Delta s$ to within one bin.

## 11. Exercises, common mistakes, applications

Companion problem sets:
[`exercises/02-geometry-and-coverage-exercises.md`](./exercises/02-geometry-and-coverage-exercises.md)
and [`exercises/02-geometry-and-coverage-solutions.md`](./exercises/02-geometry-and-coverage-solutions.md).

### Common mistakes

1. **Equating fold with resolution.** Doubling the channel count halves the noise
   but does not shrink the bin, the Fresnel zone, or the two-body limit.
2. **Ignoring the end taper.** 185 of 891 bins in the measured example are below
   full fold; anything within ~925 m of the line end is under-covered.
3. **Assuming a uniform offset distribution.** It is uniform for a constant split
   spread and strongly non-uniform for most 3-D templates.
4. **Using a 2-D line to test a 3-D hypothesis.** Sideswipe and off-line peaks are
   interpretation errors that the data cannot reveal.
5. **Choosing the bin to reach a target fold.** The bin is set by the shortest
   wavelength to be preserved; the fold follows from the channel count.

### Real-world applications

- **Seismic reflection design.** The $N/2$ fold rule and the offset range are the
  two numbers on the first page of every acquisition report.
- **Potential-field surveys.** Here the geometry is a station grid, and the
  two-body limit $s_{\text{crit}} = h$ is the honest statement of what the survey
  can and cannot separate.
- **Marine streamer surveys.** The offset range is limited by the streamer length;
  the resulting range of incidence angles determines whether AVA analysis is
  possible at all.
- **Passive arrays.** The analogue of offset is the inter-station distance, and of
  fold is the number of stations per wavelength; the same $\sqrt{N}$ logic applies
  to beamforming arrays.

## 12. Further reading

- **Vermeer, G. J. O. (2002). *3-D Seismic Survey Design*. Society of Exploration
  Geophysicists.** The definitive treatment of fold, bins, offsets and symmetry in
  3-D templates. Level: advanced practitioner.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied Geophysics*
  (2nd ed.). Cambridge University Press.** Sections on reflection field
  procedures and on array design. Level: intermediate.
- **Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press.** Chapters 3 and 6 for the geometry-to-resolution
  argument. Level: intermediate to advanced.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*. Cambridge University Press.** Chapter 9 on survey layout and the
  interpretation of profiles as opposed to grids. Level: advanced.
- **USGS gravity and magnetic methods pages** — <https://www.usgs.gov> — for the
  standard grid spacings used in national-scale programmes, useful as a sanity
  check on a planned spacing. (Opens in a browser; the site blocks automated
  requests.)

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text, and you should
> confirm current availability and editions through your library before citing them.

## 13. Related lessons

- [05-05-01 Survey Planning](./01-survey-planning.md) — the detectability budget this geometry serves.
- [05-05-03 Spatial Sampling, Wavenumber Aliasing and Reconstruction](./03-spatial-sampling-theory.md) — why the bin size is an aliasing limit.
- [05-05-05 Acquisition QC](./05-quality-control.md) — measuring whether the planned fold was achieved.
- [05-06-02 Noise Suppression: Stacking, Filtering, Median, KL Transform](../06-data-processing-principles/02-noise-suppression.md) — the $\sqrt{N}$ law in practice, and what breaks it.
- [05-01-04 Non-Uniqueness of Geophysical Models](../01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md) — the general theory behind the two-body limit.
- [02-03-09 Diffraction, Scattering and Resolution Limits](../../02-physics/03-oscillations-and-waves/09-diffraction.md) — the Fresnel zone.

## 14. Self-assessment checklist

- [ ] I can derive the fold formula and reduce it to $N/2$ for the standard case.
- [ ] I can explain what fold buys and what it does not.
- [ ] I can state the offset range of a given spread and what each part of it carries.
- [ ] I can state the ramp length at the end of a profile and why it exists.
- [ ] I can compute a Fresnel-zone radius and explain why it does not improve with denser receivers.
- [ ] I can quote the two-body separation limit for equal point masses and justify it.
- [ ] I can name the three things a 2-D line cannot resolve that a 3-D array can.
- [ ] I can list the assumptions behind each of the above and say which field conditions violate them.
