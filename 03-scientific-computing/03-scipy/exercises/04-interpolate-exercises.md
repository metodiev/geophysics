# Exercises — 03-03-04 scipy.interpolate: Splines, Griddata and RegularGrid

Attempt these **closed-book** before opening the
[solutions](./04-interpolate-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to
[`../code/interpolate_demo.py`](../code/interpolate_demo.py) require you to run
it and report its actual output:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/interpolate_demo.py
```

---

## ★ Foundational

**★1.** The demo's first table is

```
    method                          RMS (m/s)  max (m/s)   overshoot (m/s)
    interp1d(linear)                    9.022    100.248             0.000
    CubicSpline                         6.576     30.186             6.991
    PchipInterpolator                   8.378     85.561             0.000
    Akima1DInterpolator                 5.859     41.856             0.665
    UnivariateSpline(s=0)               6.576     30.186             6.991
    UnivariateSpline(s=n*sigma^2)       5.773     62.740             0.000
```

(a) State the noise level and identify which methods are interpolating and
which are fitting.
(b) Explain why `CubicSpline` and `UnivariateSpline(s=0)` have identical
numbers.
(c) Explain why the method with the lowest RMS error has the second-largest
maximum error.
(d) The overshoot column is zero for three methods. State what that guarantees
and give one situation in which it is a necessary property.

---

**★2.** The demo reports

```
    CubicSpline at the 221 nodes: max |f(z_s) - v_s| = 4.55e-13 m/s
    UnivariateSpline(s=0)               : max |f(z_s) - v_s| = 1.36e-12 m/s
    UnivariateSpline(s=n*sigma^2)       : max |f(z_s) - v_s| = 13.483 m/s
```

(a) Explain the first two values at the level of floating-point arithmetic.
(b) Explain the third: is 13.483 m s⁻¹ an error or a design decision?
(c) A colleague argues the smoothing spline "does not fit the data" and
rejects it. Give the measured counter-argument from the RMS column of ★1.
(d) State what a node residual of exactly zero would mean for noisy data, and
why nobody wants it.

---

**★3.** The two-dimensional interpolation table is

```
    method                       RMS (m/s)   max (m/s)  RMS % of field
    RegularGridInterpolator linear      2.9319     16.6276          0.0977
    RegularGridInterpolator cubic      0.1537      1.6964          0.0051
    RectBivariateSpline kx=ky=3      0.1518      1.7193          0.0051
```

(a) Compute the ratio of the linear to the cubic RMS error.
(b) The grid spacing is 1 km. Using $\max|f - I_h f| \le \frac{h^2}{8}|f''|$,
estimate $|f''|$ for the field $3000 + 250\sin(\pi x/4)e^{-z/2.5}$ in the
$x$ direction and check the order of magnitude of the linear error.
(c) Explain why the two cubic methods agree to three digits.
(d) State what happens to each method's error if the grid spacing is halved,
with a reason.

---

## ★★ Applied

**★4.** The clustered-sample experiment gives

```
     spacing (m)               CubicSpline               PCHIP
                    overshoot    max error overshoot max error
            2.00        0.000       29.987     0.000    29.663
            0.30        0.000       86.069     0.000    28.094
            0.05       55.922      510.004     0.000    28.927
```

(a) Explain why the error is measured within 20 m of the inserted sample rather
than over the whole log.
(b) Compute the ratio of the CubicSpline maximum errors between the 2.00 m and
0.05 m rows, and between the PCHIP rows.
(c) Explain in terms of the spline's construction why the error grows as the
spacing falls.
(d) Describe the two-line data-quality check that prevents the 0.05 m row from
ever occurring in practice.

---

**★5.** The extrapolation table for the two-dimensional field is

```
      z (km)  truth (m/s) linear (m/s) cubic (m/s)  fill=nan
        11.0    2997.8297    2998.3546   2997.9248       nan
        13.0    2999.0248    3001.5395   3000.3527       nan
        20.0    2999.9407    3012.6864   3046.6975       nan
```

(a) Compute the relative errors of both methods at $z = 11$ km and at
$z = 20$ km.
(b) Explain why the cubic becomes worse than the linear at $z = 20$ km.
(c) The one-dimensional version reports −620 m s⁻¹ at 10 m past the data and
−690 000 m s⁻¹ at 150 m. Estimate the growth exponent from these two numbers.
(d) State the correct handling of a query outside the data range, and one
sentence of justification.

---

**★6.** The scattered-data table is

```
    method       RMS (m/s)   max (m/s)  NaN count   NaN %
    nearest        35.0775    217.3912          0    0.00
    linear         36.6198    247.8435         89   22.25
    cubic          29.4580    225.7072         89   22.25
```

(a) Explain what the 22.25% represents and why it is identical for two methods.
(b) The station noise is 4 m s⁻¹ and the RMS error is 29–37 m s⁻¹. Explain the
difference.
(c) Explain why `nearest` returns no NaN, and give a geophysical consequence.
(d) Compute how the RMS error would change if the number of stations were
quadrupled, assuming the error is dominated by the sampling density.

---

**★7.** The smoothing-spline parameter sweep on the demo's log gives

```
    s = 0.00 n sigma^2   RMS =  6.576   max =  30.186
    s = 0.25 n sigma^2   RMS =  5.985   max =  41.860
    s = 0.50 n sigma^2   RMS =  5.383   max =  45.971
    s = 1.00 n sigma^2   RMS =  5.773   max =  62.740
    s = 2.00 n sigma^2   RMS =  9.941   max =  94.488
```

(a) State the optimal $s$ from the RMS criterion, and the penalty for using the
textbook $s = n\sigma^2$ instead.
(b) Explain why the maximum error grows monotonically with $s$ while the RMS
error has a minimum.
(c) State which criterion you would use if the log is to be used for a
thin-bed study, and why.
(d) Explain why the RMS error at $s = 0$ (6.576 m s⁻¹) exceeds the noise level of
5 m s⁻¹, and what that says about the best achievable.

---

## ★★★ Research-oriented

**★8.** A 3-D velocity model is stored on a $0.25^\circ \times 0.25^\circ$
latitude–longitude grid and must be queried at 12 000 station coordinates.

(a) State which interpolator is appropriate and why the alternatives are not.
(b) The model has a sharp discontinuity at a subduction interface at 60 km
depth. Predict what a cubic interpolant does there and what a linear one does,
and cite the 1-D measurement from §1.2 of the lesson.
(c) Propose an interpolation strategy that respects the discontinuity, and
state its cost.
(d) The stations lie between $70^\circ$N and $72^\circ$N, where the longitude
spacing in kilometres is $\cos(70^\circ) \approx 0.34$ times the equatorial
value. State the effect on the interpolant and the correction.

---

**★9.** Design and justify a gridding scheme for a marine gravity survey.

(a) The ship tracks run east–west with 10 km between lines and gravity is
sampled every 100 m along track. Propose a grid spacing with a reason based on
the Nyquist criterion in each direction.
(b) State which interpolation method is appropriate for the cross-track
direction and why, given that the data are strongly anisotropic.
(c) Predict the artefact that will appear if a spline is used across track
without regularisation, and name it.
(d) Propose the verification step that would detect the artefact
quantitatively, and state the number it would produce.
