---
id: 03-03-04
title: "scipy.interpolate: Splines, Griddata and RegularGrid"
level: intermediate
prereqs: ["03-03-01", "01-12-02", "03-02-01"]
estimated_minutes: 75
tags: [interpolation, splines, well-log, gridding, extrapolation]
---

# scipy.interpolate: Splines, Griddata and RegularGrid

Interpolation is the most-used and least-examined operation in geophysics.
A well log is sampled every 15 cm in the borehole and compared with a
seismic trace sampled every 4 ms; a velocity field is known at station
locations and needed on a grid; a potential-field map is filtered on a grid
finer than the survey line spacing. Every one of those is an interpolation,
and every one of them returns a number whether or not the data support it.

`scipy.interpolate` provides the whole spectrum of methods, and the reason to
read this lesson rather than the docstrings is that **the methods differ in
exactly the ways that matter for physical data: overshoot, smoothness,
robustness to clustered samples and behaviour outside the data.** All four are
measured below against synthetic data whose generating function is known.

Run the demonstration before reading on:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/interpolate_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Choose** between linear, cubic-spline, PCHIP, Akima and smoothing
   interpolants for a depth–velocity log, from measured overshoot and accuracy.
2. **Explain** why a smoothing spline is the right choice when the samples
   carry noise, and quantify what the smoothing parameter buys.
3. **Recognise** the clustered-sample failure mode of a cubic spline and
   prevent it by enforcing a minimum spacing.
4. **Interpolate** a two-dimensional field on a regular grid with
   `RegularGridInterpolator` and predict the error of linear against cubic
   from the grid spacing.
5. **Quantify** the error of extrapolation beyond the data, and know which
   arguments make a routine refuse rather than guess.
6. **Grid** scattered stations with `griddata`, and explain the convex hull and
   the NaN counts that come with it.

## Prerequisites

- [03-03-01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — in particular §3.2 on the `numpy.interp` overlap.
- [01-12-02 Interpolation](../../01-mathematics/12-numerical-methods/02-interpolation.md)
  — Lagrange and Newton interpolation, and why high-order polynomial fits
  oscillate.
- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
  — the array model the spline objects consume.
- [05-08-01 The Borehole Environment](../../05-core-geophysics/08-geophysical-logging/01-borehole-environment.md)
  — the borehole setting of §2.

## 1. Why interpolation needs a lesson

Consider the honest version of the task. You have 221 samples of a
depth–velocity log, irregularly spaced (minimum spacing 2.01 m, median
4.69 m, maximum 28.15 m in the synthetic data below), each carrying about
5 m s⁻¹ of noise, and you want the velocity at an arbitrary depth — for a
synthetic seismogram, for a depth-to-time conversion, for a rock-physics
cross-plot. Four ordinary answers are available and they disagree by more
than the noise:

```
    method                          RMS (m/s)  max (m/s)   overshoot (m/s)
    interp1d(linear)                    9.022    100.248             0.000
    CubicSpline                         6.576     30.186             6.991
    PchipInterpolator                   8.378     85.561             0.000
    Akima1DInterpolator                 5.859     41.856             0.665
    UnivariateSpline(s=0)               6.576     30.186             6.991
    UnivariateSpline(s=n*sigma^2)       5.773     62.740             0.000
```

The columns are the two error measures that matter, and they are different
questions:

- **RMS error against the truth** answers "how close is the interpolated
  value?" Here Akima (5.9 m s⁻¹) and the smoothing spline (5.8) win; linear
  (9.0) is worst. Note that the noise level is 5 m s⁻¹, so the best methods
  are at the noise floor: **you cannot interpolate below the noise, only down
  to it.**
- **Overshoot** answers "does the interpolant report velocities that were
  never measured?" The cubic spline leaves the data range by 7.0 m s⁻¹;
  PCHIP and linear cannot leave it at all; Akima leaves it by 0.7.

Both are real defects. A cubic spline that overshoots by 7 m s⁻¹ in a
low-velocity shale will produce acoustic impedances that no rock has.

### 1.1 Node exactness is not accuracy

```
    CubicSpline at the 221 nodes: max |f(z_s) - v_s| = 4.55e-13 m/s
    UnivariateSpline(s=0)               : max |f(z_s) - v_s| = 1.36e-12 m/s
    UnivariateSpline(s=n*sigma^2)       : max |f(z_s) - v_s| = 13.483 m/s
```

The first two reproduce the samples to round-off: they *interpolate*. The
third does not, by construction — it is a **smoothing** spline fitted with
$s = n\sigma^2$, and a 13.5 m s⁻¹ miss at a node is the fit refusing to chase
noise. That refusal is why it has the smallest RMS error in the table.

> **With noisy data, the interpolant that reproduces every sample exactly is
> the one carrying the most noise into the answer.** Where the samples are
> exact — a computed velocity model, a tabulated standard — interpolate.
> Where they are measurements, smooth.

### 1.2 The thin bed: where the methods separate

A 20 m wide low-velocity bed at 1600 m, sampled at a median spacing of 4.7 m,
is a feature barely three samples wide. Error inside the 1590–1610 m window:

```
    interp1d(linear)                            67.166
    CubicSpline                                 18.285
    PchipInterpolator                           56.926
    Akima1DInterpolator                         26.558
    UnivariateSpline(s=0)                       18.285
    UnivariateSpline(s=n*sigma^2)               42.692
```

Linear is worst by a factor of 3.7: it cuts the corner, and cutting the
corner of a 20 m bed is a systematic amplitude error of roughly half the bed
amplitude. The cubic spline is best (18.3) because it uses information from
neighbouring nodes, which is exactly what a local, monotone-preserving method
cannot do. PCHIP is barely better than linear here (56.9) — the
monotonicity constraint that prevents overshoot also flattens the trough.

**The ranking of interpolants is not a property of the interpolants; it is a
property of the feature you are trying to resolve.** For a smooth, well-
sampled field, cubic wins on accuracy. For a spiky field, the same cubic
rings. There is no method that is best on both, which is why the choice has
to be made per dataset and defended in the methods section.

## 2. The clustered-sample failure

The most dangerous assumption of a cubic spline is easy to state and easy to
violate: **the nodes must be reasonably separated relative to the curvature
being estimated.** The demo takes the same log, inserts one extra sample
carrying a 30 m s⁻¹ error (an outlier, a miscorrected pick, a duplicated
depth with independent noise) at a decreasing distance after an existing
sample, and refits:

```
     spacing (m)               CubicSpline               PCHIP
                    overshoot    max error overshoot max error
            2.00        0.000       29.987     0.000    29.663
            0.30        0.000       86.069     0.000    28.094
            0.05       55.922      510.004     0.000    28.927
```

At a normal 2 m spacing both methods are affected only locally, by about the
size of the inserted error. Move the pair to 5 cm apart and the cubic spline's
curvature estimator divides by the square of a nearly zero interval: the
interpolant grows a spike of 56 m s⁻¹ beyond the data range and the local
error reaches 510 m s⁻¹, an order of magnitude worse than the outlier itself.
PCHIP's numbers do not move at all, because it never forms that curvature.

Two practical consequences:

- **Deduplicate the depth channel and enforce a minimum spacing before
  interpolating.** A duplicated log depth is a data-quality problem, and this
  is where it becomes a physics problem.
- **If the clustering is intrinsic** — samples genuinely close together in a
  region of interest — then the interpolant is unstable there and PCHIP,
  Akima or a smoothing spline is the defensible choice.

## 3. Two-dimensional grids: `RegularGridInterpolator`

For a velocity field known on a regular grid, `RegularGridInterpolator` takes
the axis arrays and the values and interpolates by `method='linear'` or
`method='cubic'`. The demo uses a synthetic field
$v(x,z) = 3000 + 250\sin(\pi x/4)e^{-z/2.5}$ on a 21 × 11 node grid with 1 km
spacing and queries 3000 random points:

```
    method                       RMS (m/s)   max (m/s)  RMS % of field
    RegularGridInterpolator linear      2.9319     16.6276          0.0977
    RegularGridInterpolator cubic      0.1537      1.6964          0.0051
    RectBivariateSpline kx=ky=3      0.1518      1.7193          0.0051
```

Cubic interpolation is **19 times better in RMS** than linear, and
`RectBivariateSpline` agrees with it to about 1% (0.1518 against 0.1537 m s⁻¹
RMS) — the same construction with different boundary handling, which makes the
comparison a useful cross-check but not an identity.

The linear error has a formula you can predict without running the code. For
piecewise-linear interpolation in one dimension, on an interval of length $h$,

$$\max|f - I_h f| \le \frac{h^2}{8}\max|f''| , \tag{1}$$

and in two dimensions the two axes contribute additively. With $h = 1$ km and
$f'' \sim 250\pi^2/16 \approx 154$ m s⁻¹ km⁻² for the $\sin$ term, equation (1)
predicts a few m s⁻¹ — which is what the table shows. `RectBivariateSpline` is
in the same table to make the point that **finding the analytic formula for
your interpolant's error is usually easier than trusting the interpolant.**

Where the field is most curved the cubic still wins, but the ratio narrows:

```
    13 query points near the origin
    linear   RMS =   7.2740 m/s   max =  14.6139 m/s
    cubic    RMS =   0.2440 m/s   max =   0.5476 m/s
```

## 4. Extrapolation: the measured failure

Nothing in an interpolant knows that it has left the data, so the only
protection is an argument. The demo queries below the deepest node at
$z = 10$ km:

```
      z (km)  truth (m/s) linear (m/s) cubic (m/s)  fill=nan
         9.0    2995.1698    2995.1698   2995.1660 2995.1660
        10.0    2996.7622    2996.7622   2996.7619 2996.7619
        11.0    2997.8297    2998.3546   2997.9248       nan
        13.0    2999.0248    3001.5395   3000.3527       nan
        20.0    2999.9407    3012.6864   3046.6975       nan
```

The errors are small in absolute terms because the field is smooth and nearly
flat — 1.8 parts in $10^4$ at 10% beyond the edge, 4.2 parts in $10^3$ at
100% — but the structure is the lesson. **The cubic is *worse* than the
linear at 20 km** (1.6% against 0.42% relative error): a linear rule
extrapolates the last slope, while a cubic extrapolates its own polynomial,
and a cubic polynomial diverges. `fill_value=np.nan` with
`bounds_error=False` returns `nan` instead, which is the honest default: a
NaN propagates into every map, statistic and figure downstream, where a
plausible number does not.

The one-dimensional version is more dramatic, because the last interval on a
real log is short and noisy:

```
       z (m)  truth (m/s)    spline (m/s)   error (m/s)  extrapolate=False
      2010.0     2655.267        2035.236      -620.031                nan
      2050.0     2568.038      -28566.705    -31134.744                nan
      2100.0     2620.000     -213340.590   -215960.590                nan
      2150.0     2671.962     -690412.846   -693084.807                nan
```

−620 m s⁻¹ at 10 m past the last sample, and −690 000 m s⁻¹ at 150 m. The
spline extrapolates the cubic segment fitted to a 1.94 m noisy interval, and
a cubic's error grows as the cube of the distance. `extrapolate=False`
returns `nan` at the same query points.

> **Every extrapolation is a model assumption.** The numerical value of the
> extrapolated quantity is meaningless without a statement of the model used
> to obtain it — "constant continuation", "linear trend from the last
> interval", or an explicitly fitted physical trend. An interpolant's
> extrapolation is the last of these with the model chosen by accident.

## 5. Scattered data: `griddata`

When the stations are not on a grid — gravity stations, seismic receivers,
well locations — the tool is `griddata`, which is a wrapper over
Delaunay triangulation with `method` in `{'nearest', 'linear', 'cubic'}`. Sixty
synthetic stations over a 20 × 10 km area, 400 check points:

```
    method       RMS (m/s)   max (m/s)  NaN count   NaN %
    nearest        35.0775    217.3912          0    0.00
    linear         36.6198    247.8435         89   22.25
    cubic          29.4580    225.7072         89   22.25
```

(RMS and max are taken over the 311 points inside the convex hull, so that all
three methods are compared on the same points.)

Three facts:

- **`nearest` and `linear` disagree by little.** At this station density the
  sampling, not the interpolant, sets the error. Nearest is a step function of
  station position, which shows up as a blocky map, but its RMS is no worse.
- **`linear` and `cubic` return NaN for 22.25% of the domain** — precisely the
  points outside the convex hull of the stations. That is the honest
  behaviour, and it is why a station layout should be designed with an
  interior grid in mind.
- **The measured RMS is 7 to 9 times the 4 m s⁻¹ station noise.** The extra
  error is the sampling-density term, and it is the one that shrinks with more
  stations. `griddata` on scattered picks cannot beat the pick spacing,
  however smooth the interpolant.

`nearest` never returns NaN — it answers everywhere, including outside the
hull, by repeating the edge station's value. For a national gravity database
gridded onto a national grid, that "feature" is how a coastline becomes a
line of constant anomaly.

## Worked code

The four decisions in one script — method, smoothing, grid, and refusal:

```python
import numpy as np
from scipy import interpolate

# 1. a noisy log: smooth rather than interpolate, and refuse to extrapolate
z = np.array([...]);  v = np.array([...])          # measured depths and speeds
spl = interpolate.UnivariateSpline(z, v, s=len(z) * 5.0 ** 2)   # sigma = 5 m/s
print(spl(1500.0))                                  # inside the data
print(spl(2100.0))                                  # inside: extrapolates anyway

# 2. a shape-preserving interpolant, if overshoot is unacceptable
pch = interpolate.PchipInterpolator(z, v)
print(np.all((pch(z) - v) == 0.0))                  # node-exact

# 3. a regular grid, linear versus cubic, with an explicit refusal
rgi = interpolate.RegularGridInterpolator(
    (x_nodes, z_nodes), V, method="cubic",
    bounds_error=False, fill_value=np.nan)
print(rgi(np.column_stack([xq, zq])))               # nan outside the box

# 4. scattered stations, and the hull they imply
g = interpolate.griddata((sx, sz), sv, (gx, gz), method="linear")
print(np.isnan(g).sum(), "points outside the convex hull")
```

Four arguments carry the whole lesson: `s=` (smooth or interpolate),
`method='pchip'` (overshoot or accuracy), `fill_value=np.nan` (guess or
refuse), and `np.isnan(...).sum()` (the count of the domain you have not
measured).

## Physical interpretation

A depth–velocity log is an *average over a volume*, not a point measurement:
the tool has a vertical resolution of tens of centimetres to a metre and a
lateral investigation depth of the same order. Interpolating it to 1 cm does
not create information; it manufactures the appearance of resolution. The
same is true of a potential-field map, where the flight-line spacing sets the
shortest wavelength that can be measured, and of a seismic velocity grid,
where the Fresnel zone sets the lateral resolution. **The correct question is
never "what interpolant is most accurate?" but "what is the resolution of the
measurement, and which interpolant does not pretend to beat it?"**

The thin-bed result in §1.2 is the quantitative version of this for
stratigraphy. A 20 m bed sampled every 4.7 m is three samples wide; the
best-case interpolation error of 18 m s⁻¹ stands in for a reflection
amplitude error of the same relative size, which propagates directly into
impedance and into the synthetic seismogram used to tie the log to seismic.

In two dimensions, equation (1) is the statement that a grid's information
content is $\propto h^{-2}$ — halving the spacing quadruples the number of
values but the error falls by a factor of 4 in the same ratio, so the
information per value is constant. Grid refinement improves a map only when
the underlying field is smooth on the new scale.

## Assumptions and limits

- **`CubicSpline` assumes well-separated nodes and a smooth fourth derivative.**
  Both are violated by real logs (§2).
- **`UnivariateSpline`'s `s` parameter is in units of the *squared residual*,
  summed.** Setting `s = nσ²` targets a residual RMS of σ; the fit does not
  guarantee it exactly, and the demo's smoothing spline misses nodes by up to
  13.5 m s⁻¹ at σ = 5.
- **`RegularGridInterpolator(method='cubic')` requires at least 4 points along
  each interpolated axis** and uses a tensor-product spline; it is not the
  same as a 2-D thin-plate spline and does not smooth.
- **`griddata(method='cubic')` is a Clough–Tocher piecewise cubic, not a
  globally smooth cubic spline.** It requires the triangulation to exist, so
  it fails on collinear or coincident stations.
- **Every method here assumes the field is a function of position.** Time-lapse
  or 4-D data violate that, and repeating an interpolation per vintage is a
  model assumption about temporal continuity.
- **No routine here reports a resolution.** The overshoot and RMS columns of §1
  are proxies, and the honest statement of resolution comes from the sampling
  geometry.

## Python demonstration

[`code/interpolate_demo.py`](./code/interpolate_demo.py) prints the four
tables. Useful modifications:

- Sweep `s` from `0` to `10 * n * sigma**2` and plot the RMS error against the
  truth: the curve has a minimum near `s = 0.5 * n sigma**2` and is flat
  between `0.25` and `1` times `n sigma**2`, so the standard criterion
  `s = n sigma^2` (5.773 m s⁻¹ RMS here against the best 5.383) is inside the
  flat region. The *maximum* error behaves differently from the RMS — it grows
  monotonically with `s`, from 30.2 to 62.7 m s⁻¹ at `s = n sigma^2` — because
  a smoothing spline trades away exactly the sharp features an RMS average does
  not punish.
- Change the log's minimum spacing in `part1_well_log` from 2.0 m to 0.1 m and
  re-run. Every method's global RMS rises and PCHIP's advantage over cubic
  narrows — clustered nodes hurt all of them, and the cubic catastrophically.
- Replace `velocity_true` with a field containing a fault (a step in $x$) and
  re-run §3. Linear interpolation produces a staircase along the fault, cubic
  produces ringing, and the RMS errors jump by an order of magnitude. This is
  the argument for interpolating *along* structure rather than across it.
- In §4, set `fill_value="extrapolate"` in the `RegularGridInterpolator` and
  compare with `None`. For `method='linear'` they are identical; for
  `method='cubic'` they differ, and the difference is a warning that
  "extrapolate" is not one algorithm.

## Common mistakes

- **Interpolating a noisy log with a spline that passes through every sample.**
  You have built a noise amplifier with a smooth shape. (§1.1)
- **Believing a small RMS error.** The smoothing spline has the smallest RMS in
  §1 *because* it does not interpolate; it is a fit, and it will not reproduce
  a genuine spike.
- **Interpolating a grid with `method='cubic'` when the field has a
  discontinuity.** Cubic interpolation rings at a fault or an unconformity in
  exactly the way PCHIP does not.
- **Extrapolating and reporting the number.** §4 gives the measurement:
  −690 000 m s⁻¹ is what an unexamined extrapolation looks like.
- **Using `griddata` to fill a map edge to edge.** The 22% of the domain
  outside the hull has no data; a routine that always answers is a routine
  that always lies.
- **Forgetting that `np.interp` and `interp1d` reject out-of-range queries by
  default, while a spline object does not.** The default differs between the
  two, and it changed between SciPy versions for `interp1d`.

## Real-world applications

- **Well-to-seismic ties.** Logs are resampled to seismic time and depth,
  and the interpolant's amplitude response is a direct contribution to the
  synthetic trace used to correlate the two datasets.
- **Depth conversion.** A time–depth pair per well, interpolated between
  wells, converts a seismic surface to depth; the interpolation error is a
  mapped depth error and appears in the volumetric uncertainty.
- **Gridding of survey data.** Marine gravity and magnetic data arrive along
  ship tracks; gridding across 20 km of empty water is an interpolation
  problem with a well-known failure mode (the "bull's-eye" artefact of
  minimum-curvature gridding) that spline and kriging methods handle
  differently.
- **Potential-field continuation.** Upward continuation is an integral
  operator applied to an interpolated grid; the interpolation error is
  amplified by the continuation kernel, which is why continuation is done on
  the survey grid rather than on a refined one.
- **Atmospheric and oceanographic reanalysis.** Model output on a grid is
  regridded to station locations or to another grid; conservative regridding
  (preserving integrals) is a different problem from accurate point
  interpolation.
- **Time-series resampling.** A 1 Hz geodetic series resampled to 1 day, or a
  100 Hz seismic record decimated to 20 Hz, is interpolation with a filter
  attached; decimation without a low-pass filter aliases, which is the
  subject of [lesson 05](./05-signal.md).

## Further reading

- **de Boor, C. *A Practical Guide to Splines* (revised ed., Springer, 2001).**
  The reference for the theory behind `CubicSpline` and `UnivariateSpline`,
  including the variational interpretation of the smoothing parameter. Level:
  advanced.
- **Davis, P. J. *Interpolation and Approximation* (Dover reprint).** The
  classical error bounds, including the $h^2/8$ of equation (1) and the
  oscillation theorems behind the overshoot of §1.2. Level: intermediate to
  advanced.
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P.
  *Numerical Recipes* (3rd ed., Cambridge University Press, 2007).** Chapter 3
  covers interpolation and rational functions with the practical warnings.
  Level: intermediate.
- **Isaaks, E. H., & Srivastava, R. M. *An Introduction to Applied
  Geostatistics* (Oxford University Press, 1989).** The variogram-based view
  of spatial interpolation, and the reason kriging and splines disagree about
  what a smooth map is. Level: intermediate.
- **Fritsch, F. N., & Carlson, R. E. "Monotone Piecewise Cubic Interpolation,"
  *SIAM Journal on Numerical Analysis*, 1980.** The algorithm behind PCHIP.
  Level: advanced; consult it when you need to defend the choice.
- **Smith, W. H. F., & Wessel, P. "Gridding with continuous curvature splines
  in tension," *Geophysics*, 1990.** The spline-in-tension method that
  handles the survey-gridding failure modes of §5. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text;
> confirm editions and availability through your library before citing them
> yourself.

## Related lessons

- [01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — §3.2, the `numpy.interp` overlap and the cost of a default.
- [03 scipy.optimize](./03-optimize.md) — fitting a functional form is the
  alternative to interpolating, and the covariance matrix tells you which is
  better determined.
- [05 scipy.signal](./05-signal.md) — resampling with an anti-alias filter,
  which is what interpolation becomes when the data have a spectrum.
- [07 scipy.ndimage and scipy.linalg](./07-ndimage-linalg.md) — smoothing,
  which is interpolation's sibling operation on grids.
- [01-12-02 Interpolation](../../01-mathematics/12-numerical-methods/02-interpolation.md)
  — the error bounds behind equation (1).
- [01-10-04 The Discrete Fourier Transform](../../01-mathematics/10-fourier-analysis/04-discrete-fourier.md)
  — why a sampled field has a shortest resolvable wavelength.

Exercises:
[`exercises/04-interpolate-exercises.md`](./exercises/04-interpolate-exercises.md)
and
[`exercises/04-interpolate-solutions.md`](./exercises/04-interpolate-solutions.md).

## Self-assessment checklist

- [ ] I can name the interpolant that cannot overshoot, and one that
      overshoots the most. (§1)
- [ ] I can explain why the smoothing spline has the smallest RMS error in
      §1. (§1.1)
- [ ] I can predict which interpolation method wins at a thin bed, and why.
      (§1.2)
- [ ] I can reproduce the clustered-sample failure and say how to avoid it.
      (§2)
- [ ] I can use equation (1) to predict a linear-interpolation error before
      running the code. (§3)
- [ ] I can state the measured error of extrapolating 10% and 100% beyond a
      grid edge. (§4)
- [ ] I can make a routine refuse to extrapolate rather than guess. (§4)
- [ ] I can explain the NaN count from `griddata` and what a `nearest` map
      hides. (§5)
- [ ] I can state the resolution limit the sampling imposes on a log, in
      metres. ('Physical interpretation')
