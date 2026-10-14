# Exercises — 03-03-07 scipy.ndimage and scipy.linalg for Field Data

Attempt these **closed-book** before opening the
[solutions](./07-ndimage-linalg-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to
[`../code/ndimage_linalg_demo.py`](../code/ndimage_linalg_demo.py) require you
to run it and report its actual output:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/ndimage_linalg_demo.py
```

The grid is $201\times201$ over $20\times20$ km (0.1 km spacing) and the noise
is 5% of the peak anomaly, $\sigma_n = 0.0705$ mGal.

---

## ★ Foundational

**★1.** The smoothing table is

```
     sigma (px)   residual noise (mGal)   signal distortion (mGal)  total (mGal)
           none                  0.0702                     0.0000        0.0702
            1.0                  0.0199                     0.0004        0.0199
            2.0                  0.0100                     0.0013        0.0101
            4.0                  0.0064                     0.0041        0.0076
            8.0                  0.0130                     0.0128        0.0182
```

(a) Compute the ratio of residual noise to input noise for $\sigma = 1$ and
$\sigma = 2$.
(b) The white-noise gain of a two-dimensional Gaussian filter is
$(2\sigma\sqrt\pi)^{-1}$. Verify (a) against it.
(c) State the smoothing scale that minimises the total error, and the physical
reason the total error rises on either side of it.
(d) Predict the residual noise at $\sigma = 32$ from the gain law and state
whether the signal distortion would make the total error larger or smaller than
the measurement at $\sigma = 16$.

---

**★2.** The spike experiment reports

```
    spiked grid              max |error| =   2.3405 mGal   RMS =   0.1947 mGal
    median_filter(5)         max |error| =   0.0832 mGal   RMS =   0.0180 mGal
    gaussian_filter(2)       max |error| =   0.1867 mGal   RMS =   0.0283 mGal
    median then gaussian     max |error| =   0.0385 mGal   RMS =   0.0097 mGal
```

(a) The 300 spikes are $\pm30$ noise sigmas. Compute their amplitude in mGal.
(b) Compute the ratio of the Gaussian filter's maximum error to the spike
amplitude, and relate it to the window size.
(c) Explain why doubling the spike amplitude would double the Gaussian's error
but not the median's.
(d) State the two-stage recipe and the measured improvement over the better
single filter.

---

**★3.** The least-squares comparison reports

```
    route                                residual |Ax-b|    max |x - x_qr|
    scipy.linalg.lstsq (QR/SVD)                2.119e-06         0.000e+00
    normal equations + cho_factor              2.119e-06         1.881e-09
    linalg.solve(A^T A, A^T b, pos)            2.119e-06         4.214e-09

    condition number of the design matrix A   = 2.0034e+04
    condition number of the normal matrix A^T A = 4.0138e+08
```

(a) Verify that $\text{cond}(A^TA) = \text{cond}(A)^2$.
(b) Compute the number of decimal digits lost by each factorisation, assuming
16 significant digits in double precision.
(c) Explain why all three routes reach the same residual while their
coefficients differ.
(d) State which route you would use for a degree-6 trend removal on a survey
profile, with a one-sentence justification.

---

## ★★ Applied

**★4.** The derivative table is

```
    sobel on the noisy grid                   0.3054         227.19
    gaussian sigma =  4.0 then sobel                0.0128           9.53
    gaussian sigma =  6.0 then sobel                0.0114           8.51
    gaussian sigma = 10.0 then sobel                0.0141          10.48
```

with a peak analytic derivative of 0.1344 mGal/km.

(a) Explain why the raw derivative's RMS error exceeds the peak derivative.
(b) State the optimal smoothing scale and the error at that scale as a
percentage of the peak.
(c) Explain the two mechanisms that set the optimum, and which one dominates
below and above it.
(d) Predict what happens to the optimum if the noise level is halved, with a
reason.

---

**★5.** The noise-free diagnostic reports

```
     sigma    whole grid RMS    interior RMS
       0.0           0.00304         0.00001
       4.0           0.00807         0.00001
       8.0           0.01094         0.00010
```

(a) Express the interior discretisation error of $1.425\times10^{-5}$ as a
percentage of the peak derivative.
(b) Compute the ratio of the whole-grid error to the interior error at
$\sigma = 0$, and explain the ratio.
(c) Explain why the whole-grid error grows with $\sigma$ while the interior one
does not.
(d) State the practical consequence for a derivative map computed on a
potential-field grid, in terms of how many smoothing widths of the edge should
be discarded.

---

**★6.** The rotated-profile table is

```
    grid                    order   RMS (mGal)   max (mGal)
    4 km spacing (decimated)      0      0.16355      0.40027
                                1      0.04169      0.11755
                                3      0.00607      0.01812
    0.4 km spacing (decimated)      0      0.01653      0.04863
                                1      0.00041      0.00109
                                3      0.00023      0.00217
```

(a) Compute the ratio of the order-1 to order-3 error at each grid spacing.
(b) The improvement from 4 km to 0.4 km for order 1 is a factor of 102, which is
the expected $h^2$ behaviour. Compute the same ratio for order 3 and state
whether it matches $h^4$.
(c) Explain the discrepancy in (b).
(d) State the practical rule this produces about grid refinement versus
interpolation order.

---

## ★★★ Research-oriented

**★7.** The ill-conditioning study gives

```
     degree     cond(A)   cond(A^T A)  coef error  prediction error   Cholesky
          5   3.593e+03     1.291e+07   1.093e-10         2.454e-17           ok
          8   6.346e+05     4.027e+11   3.154e-06         4.142e-13           ok
         11   1.176e+08     1.354e+16   1.570e-02         5.155e-10           ok
         14   2.279e+10     4.099e+18         nan               nan  LinAlgError
```

(a) For each degree, compute the digits lost by the normal-equations route.
(b) Explain why the *prediction* error stays small even when the coefficients
are wrong in the second digit, and state the model classes for which prediction
accuracy does and does not imply interpretability.
(c) The degree-14 case raises `LinAlgError`. Explain what that proves about the
matrix and why it is a better outcome than a wrong answer.
(d) Design an alternative basis for a degree-11 trend that keeps the condition
number below $10^{4}$ on 60 equispaced samples. Justify it quantitatively.

---

**★8.** A gravity survey is levelled with a low-order polynomial trend removal
per line, then gridded.

(a) The lines are 8 km long with 200 samples. State the highest polynomial
degree for which the Vandermonde design matrix has $\text{cond}(A) < 10^{6}$,
justifying with the condition numbers measured above.
(b) Explain why per-line trend removal introduces a discontinuity between
adjacent lines and how a two-dimensional trend avoids it.
(c) The levelling uses a Gaussian filter with $\sigma = 4$ pixels on a 0.1 km
grid, i.e. 0.4 km. State the shortest wavelength the levelling removes and the
wavelength it leaves partly attenuated.
(d) Propose the quantitative check that would reveal the levelling filter's
effect on the anomaly, and the number it should produce for a grid left
unfiltered.
