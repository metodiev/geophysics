# Solutions — 03-03-07 scipy.ndimage and scipy.linalg for Field Data

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked *measured* come from a modified
> copy, with the modification stated.

---

## ★1 — Smoothing and the noise gain

**(a)** $\sigma = 1$: $0.0199/0.0702 = 0.2835$. $\sigma = 2$:
$0.0100/0.0702 = 0.1425$.

**(b)** $(2\sigma\sqrt\pi)^{-1}$: at $\sigma = 1$, $1/(2\sqrt\pi) = 0.2821$ —
0.5% below the measured 0.2835. At $\sigma = 2$, $1/(4\sqrt\pi) = 0.1410$ —
1.0% below the measured 0.1425. The gain law is
$g_{2D} = g_{1D}^2 = (2\sigma\sqrt\pi)^{-1}$ because a Gaussian filter is
separable, so the noise gain is the product of the one-dimensional gains. The
small excess is the finite kernel truncation and edge handling.

**(c)** $\sigma = 4$ pixels minimises the total error at 0.0076 mGal. Below it,
the residual noise dominates (0.0702 at $\sigma = 0$, 0.0199 at 1, 0.0100 at
2); above it, the signal distortion dominates (0.0128 at $\sigma = 8$, 0.0401
at 16). The optimum is where the two contributions cross — it is a
bias–variance optimum, and its location depends on the anomaly width and the
noise level.

**(d)** At $\sigma = 32$ the gain law gives $1/(64\sqrt\pi) = 0.0088$, so the
residual noise would be about $0.0702\times0.0088 = 6.2\times10^{-4}$ mGal,
essentially zero. But the distortion at $\sigma = 16$ is already 0.0401 mGal and
grows roughly as $\sigma^2$, so at 32 it would be about 0.16 mGal — a total error
of order 0.16 mGal, nearly three times the worst row in the table. The optimum
is a genuine minimum: removing the last of the noise costs far more signal than
it is worth.

---

## ★2 — Spikes

**(a)** $30 \times 0.0705 = 2.115$ mGal, matching the demo's stated
$\pm2.114$ mGal.

**(b)** $0.1867/2.3405 = 0.0798$. The mechanism is the kernel's centre value: a
normalised two-dimensional Gaussian with $\sigma = 2$ has
$k(0) = (2\pi\sigma^2)^{-1} = 1/(8\pi) = 0.0398$, so a 2.34 mGal spike becomes a
bump of $2.34\times0.0398 = 0.093$ mGal. The measured maximum error is larger
because it also contains the noise-driven error, whose RMS at $\sigma = 2$ is
0.0283 mGal; the maximum of that field over $201\times201$ pixels is about four
times its RMS, i.e. 0.11 mGal. Spike plus noise gives up to about 0.20 mGal,
consistent with the measured 0.1867.

**(c)** A linear filter's response to a spike is proportional to the spike's
amplitude — the bump is $A\,k(0)$ — so doubling $A$ doubles the bump. The median
is an order statistic: as long as the spike is not the majority of the window,
the median is unchanged, and the response is not merely small but *insensitive*
to the amplitude. That independence is the reason to use it.

**(d)** Median first, then a Gaussian. *Measured*: maximum error 0.0385 mGal
against the median's 0.0832 (a factor of 2.16 better) and RMS 0.0097 against
0.0180 (a factor of 1.86 better). Both single filters are beaten on both
measures.

---

## ★3 — Normal equations against QR

**(a)** $(2.0034\times10^{4})^2 = 4.0136\times10^{8}$, against the tabulated
$4.0138\times10^{8}$ — agreement to three digits, the difference being that the
ratio is computed from the *numerically* factored matrices.

**(b)** Digits lost $= \log_{10}\text{cond}$: 4.30 for $A$ and 8.60 for
$A^TA$. Of 16 available double-precision digits, the design matrix leaves 11.7
and the normal matrix 7.4.

**(c)** Because the residual measures how well the *fitted curve* matches the
data, and a nearly singular system still has a good-fitting solution: many
different coefficient vectors give nearly the same curve. The coefficients
differ because they are recovered from ratios of small numbers, which is where
the lost digits go.

**(d)** `scipy.linalg.lstsq`. At $\text{cond}(A) = 2\times10^4$ the normal
equations lose 8.6 of 16 digits, and the measured coefficient difference of
$4.2\times10^{-9}$ already exceeds the level at which a trend's amplitude
would be quoted. There is no performance reason to prefer the normal equations
at degree 6 on 60 samples.

---

## ★4 — The derivative optimum

**(a)** Differentiation multiplies the noise's spectrum by $k$, so it amplifies
the high-wavenumber part where the noise lives and the anomaly does not. With
5% noise and a Sobel operator the noise term dominates completely: 0.3054
mGal/km of RMS error against a peak derivative of 0.1344 mGal/km — 227%, i.e.
the output is not a derivative of the anomaly at all.

**(b)** $\sigma = 6$ pixels, where the RMS error is 0.0114 mGal/km = **8.51% of
the peak derivative**. The error at $\sigma = 4$ is 9.53% and at $\sigma = 10$ is
10.48%, so the optimum is broad — the rms error varies by only a fifth across
$\sigma = 4$–10, which is fortunate because the optimum depends on the anomaly
width, which is rarely known exactly.

**(c)** Below the optimum, the *variance* term dominates: unsmoothed noise. The
noise's contribution to the derivative falls as the smoothing removes high
wavenumbers. Above the optimum, the *bias* term dominates: smoothing removes the
anomaly's own short wavelengths, and the derivative of the smoothed field is not
the derivative of the true field. The measured optimum is where the two
contributions are equal.

**(d)** Halving the noise reduces the variance term by a factor of 2, so the
optimum moves to a smaller $\sigma$ (roughly, the crossing point moves to where
the distortion is half as large, which for distortion $\propto\sigma^2$ means
$\sigma$ falls by about $\sqrt2$ — to about 4 pixels). The resulting error at the
new optimum is lower than 0.0114, because with less noise there is less to
remove.

---

## ★5 — Interior against boundary error

**(a)** $1.425\times10^{-5}/0.1344 = 1.06\times10^{-4}$, i.e. **0.011%** of the
peak derivative.

**(b)** $0.00304/1.425\times10^{-5} = 213$, i.e. the whole-grid error is about
200 times the interior error. The excess is entirely the outermost rows: with
`mode='nearest'` the difference stencil at the edge is one-sided, so its
truncation error is $O(h)$ rather than $O(h^2)$ — a much larger local error over
a thin strip is enough to dominate an RMS over the whole grid.

**(c)** The interior error is unchanged by smoothing out to $\sigma = 4$ because
it is a *discretisation* error of the Sobel operator on a field that is already
smooth; smoothing the field before differencing does not change the stencil's
accuracy. The whole-grid error grows because smoothing widens the region over
which the boundary's one-sided difference is inaccurate — the kernel reaches
further into the edge zone with every increase in $\sigma$.

**(d)** Discard or treat separately a margin of at least three to four smoothing
widths (for $\sigma = 4$ pixels, 12–16 pixels, i.e. 1.2–1.6 km on a 0.1 km
grid). The measurable justification is the 213-fold ratio in (b): any residual
quoted from a derivative map that includes the margin is a statement about the
boundary condition, not about the field.

---

## ★6 — Interpolation order against grid spacing

**(a)** At 4 km: $0.04169/0.00607 = 6.87$. At 0.4 km:
$0.00041/0.00023 = 1.78$. The cubic's advantage shrinks by a factor of four when
the grid is refined tenfold.

**(b)** Order 3: $0.00607/0.00023 = 26.4$, whereas $h^4$ predicts $10^4$.
So the cubic error is **not** following its asymptotic rate here.

**(c)** Because at 4 km the grid cannot represent the field: the anomalies have
standard deviations of 4.5, 6 and 8 km, so the narrowest is sampled at only
2–3 points per standard deviation and the error is a *sampling* error rather
than the spline's asymptotic interpolation error. Sampling errors fall much more
slowly with $h$ (the measured local exponent is
$\log(26.4)/\log(10) = 1.42$). Order 1, being larger, is already in its
asymptotic regime and does show the expected $h^2$ behaviour (a factor of 102
for a factor of 10 in $h$).

**(d)** Refine the grid before refining the interpolant. Higher orders buy
little when the data are under-sampled relative to the field's structure, and
the choice of order is only worth making once the grid is fine enough that the
spline's own error dominates. That is the same conclusion the lesson draws from
the coarse-grid row: order 0 → 1 → 3 changes the error by a factor of 27 at
4 km and by a factor of 2 at 0.4 km.

---

## ★7 — Conditioning and basis choice

**(a)** Digits lost $= \log_{10}\text{cond}(A^TA)$:

| degree | $\text{cond}(A^TA)$ | digits lost | digits remaining of 16 |
|---|---|---|---|
| 5 | $1.291\times10^{7}$ | 7.11 | 8.9 |
| 8 | $4.027\times10^{11}$ | 11.61 | 4.4 |
| 11 | $1.354\times10^{16}$ | 16.13 | −0.1 |
| 14 | $4.099\times10^{18}$ | 18.61 | −2.6 |

At degree 11 there are no significant digits left, which is exactly what the
measured coefficient error of $1.57\times10^{-2}$ — wrong in the second digit —
shows.

**(b)** The fitted *curve* is still nearly the same even when the coefficients
are not, because the lost digits correspond to combinations of basis functions
that barely change the curve over the fitted range. The high-degree monomials
$x^{11}$ and $x^{10}$ are nearly parallel functions on $[0,1]$, so their
coefficients trade off almost freely; any two coefficient vectors along that
near-null direction give the same prediction. Prediction accuracy therefore does
*not* imply interpretability: if you want to say "the trend steepens with
distance", that statement is about coefficients and is not supported; if you
only want to subtract the trend, the prediction is fine.

**(c)** It proves that the matrix is numerically singular — the Cholesky
factorisation encountered a non-positive pivot, so $A^TA$ is not positive
definite at the working precision. That is a *detection*, and the alternative
(the QR route, which happily returns coefficients) is worse in one respect: it
returns numbers that look like answers. The correct response is to reduce the
degree, change the basis, or regularise.

**(d)** Use a **Chebyshev basis** (or any orthogonal polynomial basis) evaluated
on the same 60 equispaced samples in $[0,1]$. *Measured* condition numbers:

| degree | monomial Vandermonde | Chebyshev basis |
|---|---|---|
| 5 | $3.59\times10^{3}$ | 2.48 |
| 8 | $6.35\times10^{5}$ | 2.56 |
| 11 | $1.18\times10^{8}$ | 2.58 |
| 14 | $2.28\times10^{10}$ | 2.66 |

The Chebyshev basis holds a condition number of about **2.6 at every degree**,
a factor of $4.6\times10^{7}$ better than monomials at degree 11. It works
because the basis functions are nearly orthogonal with respect to the uniform
node measure, so no near-null direction exists. The cost is that the fitted
coefficients are Chebyshev coefficients and must be converted (via
`numpy.polynomial.chebyshev.cheb2poly`) if monomial coefficients are wanted —
and that conversion reintroduces the conditioning, which is why it should be
done only at the end and never fed back into a fit.

---

## ★8 — Levelling a gravity survey

**(a)** From the measured table, $\text{cond}(A) = 3.59\times10^3$ at degree 5
and $6.35\times10^5$ at degree 8 on 60 nodes; on 200 nodes the conditioning is
better for the same degree (more nodes, better sampling of the basis). Degree 5
is safely below $10^6$; degree 8 is marginal and degree 11 fails. So the answer
is **degree 5–6**, and the check is to print `np.linalg.cond(A)` rather than to
assume it. For a levelling trend, degree 2–3 is the normal choice anyway, and
the conditioning argument is a reason not to reach for a high degree "to
capture the long wavelength".

**(b)** A per-line polynomial has its own coefficients fitted to that line, so
the value at the end of line $i$ and at the start of line $i+1$ need not agree:
the trend is discontinuous across every line boundary, producing a striping
artefact parallel to the lines. A two-dimensional trend (a polynomial in $x$
*and* $y$, or a bilinear/bicubic surface) is continuous by construction, so
adjacent lines share the same trend and no discontinuity is introduced. The
cost is a larger least-squares problem and, at high total degree, the same
conditioning problem as ★7.

**(c)** A Gaussian filter with $\sigma = 0.4$ km has a transfer function
$\exp(-2\pi^2\sigma^2k^2)$ with $k = 1/\lambda$, so the attenuation is
$\exp(-3.158/\lambda^2)$ for $\lambda$ in kilometres. The half-power wavelength
solves $3.158/\lambda^2 = \ln 2$, giving $\lambda = 2.13$ km. The values:

| $\lambda$ (km) | attenuation |
|---|---|
| 3.0 | 0.70 |
| 2.13 | 0.50 |
| 1.6 | 0.29 |
| 1.0 | 0.04 |

So the levelling removes everything shorter than about 1 km, halves a 2.1 km
feature and preserves 70% of a 3 km one — exactly the band where near-surface
anomalies live.

**(d)** The check is the grid's radially averaged power spectrum before and
after levelling: the ratio of the two spectra is the filter's transfer
function, and it should equal $\exp(-2\pi^2\sigma^2k^2)$ for the applied
$\sigma$. For an unfiltered grid the ratio is 1 at every wavenumber, and any
wavenumber at which it is 0.3 identifies a wavelength the levelling removed.
Plotting that ratio is the single most useful diagnostic for a levelling
sequence, because it shows exactly what the processing took out.
