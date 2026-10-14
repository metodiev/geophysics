# Solutions — 08-03-05 Depth Estimation

> **Read after attempting the exercises.** The lesson is
> [05 Depth Estimation](../05-magnetic-depth-estimation.md).

---

## ★1 — Euler's equation and the indices

$$\left(\mathbf{r}-\mathbf{r}_0\right)\cdot\nabla T = -N\left(T-T_0\right),$$

with the linear form used in practice,

$$x\,T_x + y\,T_y + N\,T = x_0\,T_x + y_0\,T_y + z_0\,T_z + N\,T_0 .$$

| Geometry | $N$ |
|---|---|
| Contact | 0 |
| Thin sheet, dike, fault | 1 |
| Vertical cylinder | 2 |
| Sphere, dipole | 3 |

---

## ★2 — Depth ratios

$$\frac{3.018}{3.000} = 1.006\ (0.6\%\ \text{high}), \qquad
\frac{2.424}{3.000} = 0.808\ (19\%\ \text{low}).$$

Only the first is acceptable. The second is a *systematic* error caused by
assuming the wrong geometry; the interquartile range also grows from 0.017 km to
0.397 km, so the wrong index is detectable by its own scatter and not only by
comparison with the truth — which is what makes a clustered solution set a
diagnostic rather than a decoration.

---

## ★3 — The half-width rule

$$\text{FWHM} = 2z \quad\Longrightarrow\quad z = \frac{3.0}{2} = 1.5\ \mathrm{km}.$$

The rule is exact for the model it is derived from
$T(x) = Az/\left(\left(x-x_0\right)^{2}+z^{2}\right)$.

---

## ★4 — The error of the wrong model

$$\frac{1.000}{2.00} = 0.50 \quad\Longrightarrow\quad -50\% .$$

The rule is not slightly wrong: the factor of two it contains *is* the model.
Applying it to a dipole multiplies a correct measurement by a factor belonging to
a different source geometry, and no amount of data quality removes that. A depth
estimator is a model plus arithmetic; only the arithmetic is checked by the
fit.

---

## ★5 — Depth from the spectral slope

$$\text{slope} = -2z_0 \quad\Longrightarrow\quad
z_0 = \frac{-\left(-8000\ \mathrm{m}\right)}{2} = 4000\ \mathrm{m} = 4.0\ \mathrm{km}.$$

Note the units: with $k$ in rad m$^{-1}$ the slope has units of metres, so no
conversion is needed; with $k$ in rad km$^{-1}$ the slope is in kilometres.
Mixing the two is the commonest spectral-depth error.

---

## ★6 — The noise effect

$$6.160 - 4.052 = 2.108\ \mathrm{km}, \qquad \frac{2.108}{3.000} = 70\% .$$

At zero noise the median is already 35% too deep, so the *smoothing* accounts for
the first 35% and the combination of noise and the shrinking accepted-window set
accounts for the rest. The two effects are distinguishable because the zero-noise
row isolates the smoothing: without that row, the bias would be attributed to
noise alone.

---

## ★★7 — Why the ensemble spectral estimate fails

The Spector–Grant derivation assumes the power spectrum of the composite anomaly
equals the **sum of the individual power spectra**. That is true only if the
sources are mutually incoherent — random phases, many of them, no correlation in
position. In the demonstration the ensemble is finite (160 and 800 bodies), so
the *cross terms* between pairs of sources do not cancel: with $n$ sources there
are $n(n-1)$ cross terms against $n$ direct terms, and their partial cancellation
is a statistical statement that only becomes accurate slowly.

The fitted value also moves with the number of bodies (2.951 km at 160, 3.146 km
at 800), which is the signature of an estimator dominated by cross terms rather
than by a depth.

**What would make the method succeed:** many more sources, spread over a wide
area compared with the source depths, with a random (incoherent) distribution of
moments and positions; or, equivalently, computing the spectrum over many
independent *windows* of a large survey and averaging the power spectra before
fitting. The innovation is to make the cross terms average to zero, not to
improve the fit.

---

## ★★8 — Testing a Werner depth (specification)

**Diagnostic.** The relative residual of the rational-function fit over the
profile, $\left\|T_{\text{obs}} - T_{\text{model}}\right\|/\left\|T_{\text{obs}}\right\|$,
computed on the same points that were used to solve for the parameters, **plus**
the residual on points held out of the fit.

**Threshold.** A residual comparable to the noise level of the profile. If the
profile is clean, a residual above about 5% means the rational function is not
describing the data.

**If it fails.** Report that the profile is not consistent with a single 2-D
sheet model, and either (i) fit a different model class and compare residuals, or
(ii) report only bounds — e.g. that the anomaly's half-width is between such and
such, which requires no model to interpret as a *width*. Do not report a depth
whose model has been rejected by its own fit.

---

## ★★9 — Three caveats for a reported Euler depth

1. **The smoothing bias.** The demonstration's zero-noise, smoothed run returns
   4.052 km for a 3.000 km body: a 1.35× bias. The reported 4.2 km must be
   corrected, or the smoothing stated, and a forward model at 3 km must be shown
   to reproduce the smoothed anomaly.
2. **The window size relative to the anomaly.** A window of 8 km is comparable to
   the body depths involved; the Euler equation is a *local* statement about a
   homogeneous source, and a window much larger than the source spans the
   regional field and other sources. Check the depth against windows of 2, 4 and
   8 km; a strong window dependence invalidates the number.
3. **The structural index.** The recovered depth moves from 3.018 to 2.424 to
   1.830 km for $N = 3, 2, 1$ on the same data. The assumed index must be
   justified from the geometry (and ideally corroborated by a second method),
   not chosen to produce a preferred depth.
