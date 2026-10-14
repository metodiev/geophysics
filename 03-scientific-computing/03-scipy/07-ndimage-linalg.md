---
id: 03-03-07
title: "scipy.ndimage and scipy.linalg for Field Data"
level: advanced
prereqs: ["03-03-01", "03-02-04", "01-14-04", "03-03-03"]
estimated_minutes: 90
tags: [ndimage, smoothing, derivatives, cholesky, least-squares, potential-fields]
---

# scipy.ndimage and scipy.linalg for Field Data

A potential-field survey produces a grid: gravity or magnetic values on a
regular mesh of latitude and longitude, or of easting and northing. Almost
everything done to that grid afterwards — smoothing, derivative computation,
continuation, trend removal, profile extraction — is either a filter applied
with `scipy.ndimage` or a linear least-squares problem solved with
`scipy.linalg`. The two subpackages are unrelated in their internals and
inseparable in practice, which is why they share a lesson.

The lesson is organised around the three operations that decide the quality of
a derived field product:

1. **Smoothing**, where the question is how much of the noise comes out and
   how much of the anomaly goes with it.
2. **Differentiation**, where the same trade appears as a bias-variance
   optimum that can be measured and predicted.
3. **Least-squares solving**, where the choice between Cholesky on the normal
   equations and QR on the design matrix decides how many digits survive.

Run the demonstration before reading on:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/ndimage_linalg_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Separate** the noise removed by a Gaussian filter from the signal it
   distorts, and locate the smoothing scale that minimises the total error.
2. **Choose** between a linear and an order-statistic filter from the noise
   model, and demonstrate the difference on spike-contaminated data.
3. **Measure** the bias-variance trade-off in a numerical derivative and
   predict which smoothing scale minimises the error.
4. **Separate** the discretisation error from the noise error using noise-free
   data, and identify the boundary contribution explicitly.
5. **Resample** a grid along a rotated profile, choosing the interpolation
   order deliberately and refusing to leave the grid.
6. **Explain** why `cond(A^T A) = cond(A)^2` costs half the available digits,
   and **measure** the point at which Cholesky on the normal equations fails.
7. **Decide** between `scipy.linalg.lstsq`, `cho_factor`/`cho_solve` and
   `linalg.solve(A^T A, A^T b, assume_a='pos')` with a stated reason.

## Prerequisites

- [03-03-01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — including §3.1, which sets up the `scipy.linalg`/`numpy.linalg` choice.
- [03-03-03 scipy.optimize](./03-optimize.md) — least-squares fitting, whose
  linear case is §5 here.
- [03-02-04 Universal Functions, Reductions and Axis Semantics](../02-numpy/04-ufuncs-reductions.md)
  — the array operations the filter functions broadcast over.
- [01-14-04 Least Squares](../../01-mathematics/14-optimization/04-least-squares.md)
  — the normal equations and the condition number.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — the field data
  whose processing motivates §2 to §4.

## 1. The synthetic field

Everything below is measured against a field whose value is known. The demo
uses a sum of three two-dimensional Gaussian anomalies on a linear regional
trend, on a 201 × 201 grid over 20 × 20 km (0.1 km spacing), with noise added
at 5% of the peak anomaly:

```
  201 x 201 grid over 20 x 20 km (spacing 0.1000 km).
  Anomaly range -0.606 to 1.409 mGal (span 2.015 mGal);
  added noise sigma = 0.0705 mGal
  (5.0% of the peak anomaly).
```

Three Gaussian anomalies with widths 6.0, 4.5 and 8.0 km are a stand-in for a
sedimentary basin, an intrusive body and a broad crustal feature. The point of
the synthetic field is not realism but **knowability**: every filter's
remaining error can be split into the part that is noise and the part that is
signal, because the noise-free field is available.

## 2. Smoothing: what comes out and what goes with it

`ndimage.gaussian_filter` convolves with a discretised Gaussian of standard
deviation `sigma` in pixels. It is **separable** — implemented as a sequence
of 1-D convolutions — which is why a 201 × 201 grid smooths instantly, and
**isotropic**, which is what distinguishes it from a box or a median filter.

```
     sigma (px)   residual noise (mGal)   signal distortion (mGal)  total (mGal)
           none                  0.0702                     0.0000        0.0702
            1.0                  0.0199                     0.0004        0.0199
            2.0                  0.0100                     0.0013        0.0101
            4.0                  0.0064                     0.0041        0.0076
            8.0                  0.0130                     0.0128        0.0182
           16.0                  0.0400                     0.0401        0.0566
```

The two columns behave as the theory says they should, and the theory is worth
stating because it predicts the optimum:

- **Residual noise** is the RMS of the difference between the smoothed noisy
  grid and the noise-free grid, excluding the distortion term. For white noise
  of variance $\sigma_n^2$ smoothed by a filter with sum-of-squares gain $g$,
  the residual noise standard deviation is $\sigma_n g$. For a Gaussian of
  width $\sigma$ in pixels the **two-dimensional** gain is
  $g = (4\pi\sigma^{2})^{-1/2} = 1/(2\sigma\sqrt\pi)$ — the square of the
  one-dimensional gain $(2\sigma\sqrt\pi)^{-1/2}$ — so the residual noise falls
  as $1/\sigma$. The measurements follow it: the ratio to the input noise is
  0.2835 at $\sigma = 1$ against the predicted 0.2821, and 0.1425 at
  $\sigma = 2$ against 0.1411.
- **Signal distortion** is the difference between the smoothed noise-free
  field and the noise-free field: how much the *anomaly* was changed. It grows
  roughly as $\sigma^2$ times the field's curvature, which for these anomaly
  widths is 0.0004 → 0.0013 → 0.0041 → 0.0128 → 0.0401 for
  $\sigma = 1, 2, 4, 8, 16$.
- **There is an optimum.** The total error is 0.0199 at $\sigma = 1$,
  0.0101 at 2, **0.0076 at 4**, and rises again by $\sigma = 8$. The minimum
  is the smoothing scale at which the noise removal and the signal
  distortion balance — and it is a property of the anomaly width and the
  noise level, not a universal setting. A survey with half the noise has a
  smaller optimum; a field with a narrow target has a smaller optimum still.

### 2.1 Spikes are not Gaussian noise

A dead pixel, a mis-tied flight line or a mis-picked station produces an
outlier, and the right filter for an outlier is an **order statistic**. The
demo inserts 300 spikes of ±30 noise sigmas — ±2.114 mGal in a field whose
peak anomaly is 1.409 mGal — and compares:

```
    spiked grid              max |error| =   2.3405 mGal   RMS =   0.1947 mGal
    median_filter(5)         max |error| =   0.0832 mGal   RMS =   0.0180 mGal
    gaussian_filter(2)       max |error| =   0.1867 mGal   RMS =   0.0283 mGal
    median then gaussian     max |error| =   0.0385 mGal   RMS =   0.0097 mGal
```

A Gaussian of $\sigma = 2$ dilutes one bad pixel by roughly the number of
pixels in its window, so a 2.34 mGal spike still leaves a 0.187 mGal bump.
Crucially, **a bigger spike would leave a bigger bump, because dilution is
linear.** The 5 × 5 median cannot be moved by one sample out of 25 at all:
its maximum error is 0.083 mGal at both a 0.79 mGal and a 2.34 mGal spike.

The two-stage recipe is the one to keep: **median first to remove the
outliers, then a Gaussian to smooth the remaining noise** — 0.0385 mGal
maximum and 0.0097 mGal RMS, better than either filter alone on both
measures.

## 3. Derivatives: a bias-variance optimum you can measure

The horizontal derivative of a potential field is the standard enhanced
product — it sharpens edges and separates nearby sources — and it is the
operation where noise does the most damage. Differentiation multiplies the
amplitude spectrum by $k$, so white noise (flat spectrum) becomes blue noise
whose power grows as $k^2$, while the anomaly's own spectrum decays. The
result is that the derivative of a raw noisy grid can be dominated by noise:

```
  Analytic d/dx of the noise-free field, peak 0.1344 mGal/km.
  kernel                       RMS error (mGal/km)   as % of peak
    sobel on the noisy grid                   0.3054         227.19
    gaussian sigma =  1.0 then sobel                0.1012          75.26
    gaussian sigma =  2.0 then sobel                0.0335          24.92
    gaussian sigma =  3.0 then sobel                0.0175          13.05
    gaussian sigma =  4.0 then sobel                0.0128           9.53
    gaussian sigma =  6.0 then sobel                0.0114           8.51
    gaussian sigma = 10.0 then sobel                0.0141          10.48
```

The raw Sobel derivative has an RMS error **2.27 times the peak derivative**:
it is not a derivative of the anomaly at all, it is a derivative of the noise.
Pre-smoothing with a Gaussian of $\sigma = 1$ brings the error to 75% of the
peak; $\sigma = 4$ to 9.5%; $\sigma = 6$ to 8.5%; and $\sigma = 10$ makes it
worse again (10.5%). **The minimum is a bias-variance optimum**: small
$\sigma$ leaves noise-dominated error (variance), large $\sigma$ removes the
anomaly's own short wavelengths (bias). It is measured, not asserted, and its
location depends on the anomaly width and the noise level.

### 3.1 Separating the two errors

The same operator applied to the *noise-free* field isolates the
discretisation error — and the result is the most useful line in the lesson:

```
     sigma    whole grid RMS    interior RMS
       0.0           0.00304         0.00001
       1.0           0.00430         0.00001
       2.0           0.00584         0.00001
       4.0           0.00807         0.00001
       8.0           0.01094         0.00010
```

In the interior the discretisation error is $1.425\times10^{-5}$ mGal km⁻¹ —
**0.01% of the peak derivative** — and it is *unchanged* by smoothing out to
$\sigma = 4$. The whole-grid number is 200 times larger and rises with
$\sigma$, and both facts come from the **boundary**, where `mode='nearest'`
forces a one-sided difference. On a real grid this term is always present,
and it is the reason derivative maps are unreliable within a few smoothing
widths of the edge.

The anisotropy check confirms the operator is behaving:

```
    x (axis=0)   RMS error = 0.00304 mGal/km
    y (axis=1)   RMS error = 0.00345 mGal/km
```

The two differ by 13%, which is the difference in the field's structure along
the two axes, not a defect of Sobel (whose $x$ and $y$ kernels are exact
transposes).

## 4. Resampling: `map_coordinates`

Rotating a grid to a structural trend, extracting a profile along a flight
line, and comparing a grid with a second dataset at different node positions
all require interpolation at arbitrary coordinates.
`ndimage.map_coordinates` does it with a spline of chosen order:

```
    grid                    order   RMS (mGal)   max (mGal)
    4 km spacing (decimated)      0      0.16355      0.40027
                                1      0.04169      0.11755
                                3      0.00607      0.01812
    0.4 km spacing (decimated)      0      0.01653      0.04863
                                1      0.00041      0.00109
                                3      0.00023      0.00217
    0.1 km spacing (full)       0      0.00414      0.01159
                                1      0.00003      0.00007
                                3      0.00001      0.00015
```

The pattern is the one from [lesson 04](./04-interpolate.md): order 0 is a step
function, order 1 has a discontinuous gradient, orders 3 and 5 are smooth.
The new information here is the interaction with grid spacing. On a 4 km grid
(order-3 error 0.00607 mGal) the spline buys a factor of 7 over linear; on the
full 0.1 km grid both are at $10^{-5}$ mGal and the choice is irrelevant.
**Interpolation cannot beat the grid it reads**, so refine the grid before
worrying about the interpolation order.

Outside the grid the two modes differ in exactly the way that matters:

```
           query (x, y) km   mode=nearest   mode=constant    analytic
                (0.0, 0.0)         0.9516          0.9516      0.9516
              (20.0, 20.0)        -0.0919         -0.0919     -0.0919
              (28.0, 10.0)         0.0081             nan      0.0421
             (10.0, -12.0)         0.6970             nan      0.0571
```

`mode='nearest'` clamps to the edge value and answers confidently — 0.0081
mGal where the true field is 0.0421, and 0.6970 where it is 0.0571, an error
of a factor of 12. `mode='constant', cval=np.nan` refuses, and the NaN is
visible in every map, statistic and figure built downstream. This is the same
principle as `fill_value=np.nan` in
[lesson 04](./04-interpolate.md) §4, applied to a rotated profile.

## 5. `scipy.linalg` and the squared condition number

The classic geophysical grid operation that is not a filter is **trend
removal** or, more generally, fitting a linear model to a profile or a grid:
fit a low-order polynomial in position, subtract it, and call the residual the
anomaly. That is a linear least-squares problem, $A x \approx b$, and there
are three standard ways to solve it.

For a degree-6 polynomial fitted to 60 samples:

```
    route                                residual |Ax-b|    max |x - x_qr|
    scipy.linalg.lstsq (QR/SVD)                2.119e-06         0.000e+00
    normal equations + cho_factor              2.119e-06         1.881e-09
    linalg.solve(A^T A, A^T b, pos)            2.119e-06         4.214e-09

    condition number of the design matrix A   = 2.0034e+04
    condition number of the normal matrix A^T A = 4.0138e+08
    ratio = 2.0034e+04, and cond(A) = 2.0034e+04
```

**All three routes reach the same residual** — $2.119\times10^{-6}$ — because
a small residual only says that a good fit exists. It says nothing about
whether the coefficients are determined. The coefficients differ in the ninth
digit already, at a perfectly ordinary condition number of $2\times10^4$, and
the reason is in the ratio column: $\text{cond}(A^TA) = \text{cond}(A)^2$ to
three digits. Squaring $2\times10^4$ gives $4\times10^8$, and since double
precision carries about 16 significant digits, **half of them are gone before
the factorisation starts.**

### 5.1 Where Cholesky on the normal equations actually fails

Raise the polynomial degree on the same 60 samples and watch:

```
     degree     cond(A)   cond(A^T A)  coef error  prediction error   Cholesky
          5   3.593e+03     1.291e+07   1.093e-10         2.454e-17           ok
          8   6.346e+05     4.027e+11   3.154e-06         4.142e-13           ok
         11   1.176e+08     1.354e+16   1.570e-02         5.155e-10           ok
         14   2.279e+10     4.099e+18         nan               nan  LinAlgError
```

At degree 5 the two routes agree to $1.1\times10^{-10}$. At degree 11 the
normal matrix has $\text{cond} = 1.4\times10^{16}$ and the Cholesky
coefficients are wrong in the **second** digit, while QR still returns a stable
answer. At degree 14 the normal matrix is numerically singular and
`cho_factor` raises `LinAlgError` rather than returning a wrong number — which
is the better failure, and the only reason it is a failure at all is that
Cholesky can detect indefiniteness.

Note the prediction-error column: even at degree 11, the Cholesky route's
*predicted values* differ from QR's by only $5.2\times10^{-10}$ in the field's
own units (m s⁻², i.e. about $5\times10^{-5}$ mGal), because the fitted curve is
nearly the same even when the coefficients are not. **A model whose purpose is
prediction tolerates an ill-conditioned solve; a model whose purpose is
interpretation does not**, because the coefficients are the interpretation.

> **Do not form the normal equations unless you have to.** `linalg.lstsq` uses
> QR or SVD and never squares the condition number. The reasons to use
> Cholesky anyway are that $A^TA$ is smaller, denser in a structured way, and
> that a regularised problem (Tikhonov) is naturally written as an augmented
> normal system — and in that case the regularisation is what keeps it
> conditionable.

## Worked code

Grid processing in the form a processing script uses it:

```python
import numpy as np
from scipy import linalg, ndimage

# 1. outliers first, then Gaussian noise: two different noise models
z = ndimage.median_filter(grid, size=5)
z = ndimage.gaussian_filter(z, sigma=2.0)

# 2. a derivative, with the largest sigma that still resolves the target
dzdx = ndimage.sobel(ndimage.gaussian_filter(z, sigma=4.0), axis=0) / (8 * dx)

# 3. resample along a profile, and refuse to leave the grid
order = 3
prof = ndimage.map_coordinates(z, [sx / dx, sy / dx], order=order,
                               mode="constant", cval=np.nan)
print("NaN fraction outside the grid:", np.isnan(prof).mean())

# 4. a polynomial trend via QR -- not via the normal equations
A = np.vander(x / x.max(), 4)                  # cubic trend
coef, *_ = linalg.lstsq(A, profile)
print("condition number of the design matrix:", np.linalg.cond(A))
print("residual RMS:", np.sqrt(np.mean((A @ coef - profile) ** 2)))

# 5. only if you need positive definiteness, form the normal matrix knowingly
ata, atb = A.T @ A, A.T @ profile
coef_chol = linalg.cho_solve(linalg.cho_factor(ata), atb)
print("coef difference vs QR:", np.abs(coef - coef_chol).max())
```

The two lines to notice are `mode="constant", cval=np.nan` and the printed
condition number. The first makes a missing data region visible; the second
tells you in advance whether the second route in step 5 is safe.

## Physical interpretation

Each operation in this lesson is a statement about the field's information
content.

**Smoothing** removes wavelengths shorter than the filter width. If the
measurement cannot resolve those wavelengths — because the station spacing,
the flight-line spacing or the instrument's noise floor does — then smoothing
removes noise and nothing else, and it is a strictly good operation. If the
target has a shorter wavelength than the filter width, smoothing removes the
target. The optimum in §2 is the quantitative version of that statement, and
it is the same optimum that [lesson 04](./04-interpolate.md) found for
interpolation.

**Differentiation** is the operation that makes the noise problem acute,
because the derivative's spectrum is the field's spectrum times $k$: it
amplifies exactly the part of the spectrum where the signal-to-noise ratio is
lowest. The measurement in §3 — an RMS error 2.27 times the peak derivative
for a raw Sobel operator — is the reason derivative maps are always made from
a smoothed grid, and the reason the smoothing parameter must be reported
alongside them.

**Trend removal** by polynomial least squares is a filter, not a
pre-processing step: it removes the long wavelengths entirely. The condition
number of the design matrix measures how well the chosen basis fits the chosen
node distribution, and the classical warning applies — a high-order polynomial
on equispaced nodes is a badly conditioned basis, not a rich model. Use
orthogonal polynomials, a local basis, or a lower order.

**`spsolve` versus `lstsq` versus `cho_solve`** is a statement about the
geometry of the fit. The five-point Laplacian of
[lesson 06](./06-sparse.md) is a symmetric positive-definite operator
discretising a *local* physical relation, and Cholesky is its natural solver.
The normal matrix of a polynomial fit is symmetric positive definite by
construction but *not local* — every data point influences every basis
function — and its condition number is the square of the design matrix's.
Same factorisation, different problem, different consequences.

## Assumptions and limits

- **`gaussian_filter` assumes the grid spacing is uniform and isotropic.** A
  grid with 0.1 km spacing in $x$ and 1 km in $y$ needs the per-axis
  `sigma=(sx, sy)` form, and forgetting it produces an anisotropic filter that
  looks like a structural fabric.
- **A Gaussian filter assumes Gaussian noise.** It is the optimal linear
  smoother for Gaussian noise and the wrong tool for spikes (§2.1).
- **`mode='reflect'` (the default) is a boundary model, not a neutral
  choice.** It invents data by mirroring the edge, and a strongly directional
  field then shows a mirrored artefact. Use `mode='nearest'` for a flat
  continuation or `mode='constant'` with a NaN margin you then exclude.
- **Sobel's $1/(8\,\Delta x)$ scaling assumes a uniform grid.** On a
  non-uniform grid the derivative must be computed from the spacings.
- **`map_coordinates` order ≥ 2 requires at least as many nodes as the spline
  order supports**, and its error grows near the boundary for any `mode`.
- **`cho_factor` requires positive definiteness and will raise if the matrix
  is not.** `linalg.solve(..., assume_a='pos')` will *not* always raise: it may
  return a wrong answer, because it trusts your assertion. Prefer
  `cho_factor` when the claim is uncertain.
- **`lstsq`'s default driver uses QR with column pivoting or SVD depending on
  the shape and conditioning**, and the returned rank may be less than the
  number of columns. Check `rank` before interpreting coefficients.

## Python demonstration

[`code/ndimage_linalg_demo.py`](./code/ndimage_linalg_demo.py) prints all the
tables above and runs in about two seconds. The experiments that teach most:

- Change `SOURCES` to include an anomaly 1.5 km wide and re-run §2. The
  optimal smoothing scale collapses from $\sigma = 4$ to $\sigma \approx 1$,
  because the target now has a wavelength comparable with the noise.
- Halve the noise level in `make_grid` and re-run §3. The optimum moves to a
  smaller $\sigma$ and the residual error falls: the bias-variance optimum is
  a function of the signal-to-noise ratio, and this is the demonstration.
- Change `mode='nearest'` to `mode='reflect'` in the derivative and compare
  the boundary error. Different boundary models give different edge artefacts,
  and the interior is unchanged in all of them.
- Add a 50% NaN region to the grid and run `median_filter` and
  `gaussian_filter` over it. Neither handles missing data; `ndimage` will
  propagate the NaN across the whole grid through any convolution. This is why
  real processing uses a masked or normalised convolution, and it is the
  single most common way a NaN in a grid becomes a NaN in a map.
- In §5, replace `linalg.lstsq` with `numpy.linalg.lstsq` and compare the
  coefficient differences. They agree to round-off, as
  [lesson 01](./01-scipy-overview.md) §3.1 predicts.

## Common mistakes

- **Smoothing without reporting the scale.** A smoothed anomaly map without
  its filter width is an uninterpretable map. (§2)
- **Using a Gaussian filter on spike-contaminated data.** The outlier survives,
  scaled by the window size. (§2.1)
- **Differentiating a raw grid.** The RMS error of 227% in §3 is not an
  exaggeration; it is what happens.
- **Choosing the smoothing scale by eye.** The optimum is measurable (§2, §3)
  and can be estimated before the field is processed.
- **Judging a derivative map only in the middle.** The boundary term in §3.1 is
  200 times the interior discretisation error.
- **Filling a grid edge to edge with `mode='nearest'`.** An answer of 0.6970
  mGal where the field is 0.0571 is not an approximation, it is a fabricated
  anomaly. (§4)
- **Forming normal equations and never checking `cond(A)`.** §5.1 gives the
  degrees at which the coefficients stop meaning anything.
- **Treating a small residual as evidence of a well-determined model.** Three
  routes reached the same residual to 1e-14 while their coefficients differed.
- **Using `assume_a='pos'` on an unverified matrix.** It is a promise; break it
  and you get a wrong answer rather than an error.

## Real-world applications

- **Aeromagnetic and gravity survey processing.** Levelling, micro-levelling,
  wavelength filtering and derivative products are all `ndimage` operations
  with a documented filter width.
- **Regional–residual separation.** Polynomial or spline trend removal, with
  the conditioning problem of §5 at the heart of how much of the long
  wavelength is "regional" and how much is signal.
- **Upward and downward continuation.** Frequency-domain operators whose
  amplification at short wavelength makes the smoothing choice of §2 decisive.
- **Grid merging and draping.** Regridding between surveys of different
  spacing, with `map_coordinates` and an explicit refusal outside the data.
- **Satellite gravity and altimetry.** Filtering of along-track data before
  gridding, and the same bias-variance optimum in the filter width.
- **Crustal deformation and geoid modelling.** Large least-squares systems
  whose normal matrices are built, conditioned and solved exactly as in §5,
  with the same digit-counting consequences.

## Further reading

- **Blakely, R. J. *Potential Theory in Gravity and Magnetic Applications*
  (Cambridge University Press, 1995).** The field-theoretic setting for
  smoothing, derivatives and continuation, with the filter design in
  geophysical terms. Level: graduate.
- **Golub, G. H., & Van Loan, C. F. *Matrix Computations* (4th ed., Johns
  Hopkins University Press, 2013).** §5.3 to §5.5 on the normal equations,
  QR and the condition-number inequality behind §5. Level: advanced.
- **Higham, N. J. *Accuracy and Stability of Numerical Algorithms* (2nd ed.,
  SIAM, 2002).** The definitive account of how many digits a given
  factorisation preserves, with the forward-error bounds that §5.1 measures
  empirically. Level: advanced.
- **Björck, Å. *Numerical Methods for Least Squares Problems* (SIAM, 1996).**
  Everything about least squares that is not in the two books above,
  including the rank-deficient cases. Level: advanced.
- **Niblack, W. *An Introduction to Digital Image Processing* (Prentice-Hall,
  1986).** Dated but clear on the neighbourhood operations that `ndimage`
  implements, including the order-statistic filters of §2.1. Level:
  intermediate.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory* (4th ed.,
  Academic Press, 2018).** Trend removal and regional–residual separation as
  inverse problems, with the resolution matrix that generalises §5. Level:
  graduate.

> Note on citations: bibliographic details are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text;
> confirm editions and availability through your library before citing them
> yourself.

## Related lessons

- [01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  §3.1 — the overlap whose first real consequence appears in §5.
- [03 scipy.optimize](./03-optimize.md) — the non-linear version of the fit in
  §5, with the covariance matrix that the condition number predicts.
- [04 scipy.interpolate](./04-interpolate.md) — splines and extrapolation,
  whose grid version is §4 here.
- [06 scipy.sparse](./06-sparse.md) — the sparse counterpart of the same
  factorisation, and the Laplacian these grids discretise.
- [01-14-04 Least Squares](../../01-mathematics/14-optimization/04-least-squares.md)
  — the normal equations derived.
- [01-01-05 Error and Conditioning](../../01-mathematics/01-arithmetic/05-error-and-conditioning.md)
  — what a condition number means in digits.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md) — the surveys whose
  processing this is.

Exercises:
[`exercises/07-ndimage-linalg-exercises.md`](./exercises/07-ndimage-linalg-exercises.md)
and
[`exercises/07-ndimage-linalg-solutions.md`](./exercises/07-ndimage-linalg-solutions.md).

## Self-assessment checklist

- [ ] I can separate residual noise from signal distortion in a smoothing
      test. (§2)
- [ ] I can explain why the residual noise falls as $1/\sigma$. (§2)
- [ ] I can name the filter to use for spikes and give the measured reason.
      (§2.1)
- [ ] I can predict the shape of the derivative error against smoothing
      scale. (§3)
- [ ] I can quote the interior discretisation error of a Sobel derivative and
      the boundary contribution separately. (§3.1)
- [ ] I can choose an interpolation order from the grid spacing rather than
      from habit. (§4)
- [ ] I can make a resampling refuse outside the grid and count the refusals.
      (§4)
- [ ] I can state the relation between $\text{cond}(A)$ and
      $\text{cond}(A^TA)$. (§5)
- [ ] I can name the polynomial degree at which Cholesky on the normal
      equations fails on a stated problem. (§5.1)
- [ ] I can explain why a small residual does not imply a well-determined
      model. (§5)
