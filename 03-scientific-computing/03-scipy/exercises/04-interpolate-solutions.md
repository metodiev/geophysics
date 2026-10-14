# Solutions — 03-03-04 scipy.interpolate: Splines, Griddata and RegularGrid

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked *measured* come from running a
> modified copy, with the modification stated.

---

## ★1 — Reading the interpolant table

**(a)** The noise level is 5 m s⁻¹ (`noise sigma = 5 m/s` in the demo's header).
`interp1d(linear)`, `CubicSpline`, `PchipInterpolator`, `Akima1DInterpolator`
and `UnivariateSpline(s=0)` all **interpolate** — they pass through every
sample. `UnivariateSpline(s=n*sigma^2)` **fits**: it does not reproduce the
samples.

**(b)** `UnivariateSpline(s=0)` with $s = 0$ is the interpolating cubic
smoothing spline, which is the natural cubic spline up to the boundary
conditions; with the default `k=3` and no smoothing it is arithmetically the
same construction as `CubicSpline`, so every number is identical. The two
classes differ in what they *offer* (`UnivariateSpline` supports smoothing and
`CubicSpline` supports arbitrary boundary conditions and derivative access),
not in what they compute at $s = 0$.

**(c)** Because the smoothing spline is a *fit*, not an interpolant: it ignores
part of every sample and therefore avoids chasing the noise, which is what the
RMS column rewards. But the same refusal means it misses the 20 m bed at
1600 m, so its maximum error (62.7 m s⁻¹) is much larger than the cubic
spline's (30.2) or Akima's (41.9). RMS and maximum error measure different
things: an RMS average is dominated by the many samples in smooth regions, a
maximum is decided by the one sharp feature.

**(d)** Zero overshoot guarantees the interpolant never reports a value outside
the range of the measured samples. It is necessary whenever a physical bound
must be respected — a velocity that cannot exceed the velocity of the fastest
mineral, a porosity that cannot be negative or exceed 1, a saturation that must
lie in $[0,1]$ in a reservoir model. A cubic spline through noisy samples near
such a bound will cross it.

---

## ★2 — Node residuals

**(a)** Both values are at the level of accumulated round-off: the linear solve
for the spline coefficients involves $O(n)$ arithmetic operations with numbers
of order $10^3$, so an error of a few times $\epsilon \times 10^3 \approx
10^{-13}$ is expected. Neither is a *fit* error, which is why the third row is
different.

**(b)** A design decision. The fit minimises a penalised residual
$\sum_i (v_i - f(z_i))^2 + \lambda\int f''^2$, and with
$s = n\sigma^2$ the penalty is large enough to leave 13.5 m s⁻¹ of residual at
nodes — a little under 3 noise standard deviations at the worst node, which is
what a $\chi^2$-like target of $n$ permits.

**(c)** The counter-argument is in the RMS column: the smoothing spline's RMS
error against the truth is 5.773 m s⁻¹, the *lowest of the fitted methods* and
below the 6.576 of the interpolating cubic. "Does not pass through the samples"
and "is a worse estimate of the truth" are different statements, and here the
first is true while the second is false.

**(d)** A node residual of exactly zero for noisy data means the interpolant is
reproducing the noise exactly, i.e. it has been fitted to the realisation
rather than to the signal. The residual to *check* is not the node residual but
the error against an independent estimate of the truth (a repeat log, a nearby
well, a known rock-physics bound) — the node residual is a consistency measure
and cannot detect over-fitting by construction.

---

## ★3 — The 2-D grid

**(a)** $2.9319/0.1537 = 19.08$.

**(b)** For $f = 250\sin(\pi x/4)e^{-z/2.5}$,$\partial^2 f/\partial x^2 = -250(\pi/4)^2\sin(\pi x/4)e^{-z/2.5}$, whose
magnitude is at most $250(\pi/4)^2 = 154.2$ m s⁻¹ km⁻². With $h = 1$ km the
bound is $\frac{1}{8}\times154.2 = 19.3$ m s⁻¹. The measured maximum linear
error is 16.6 m s⁻¹ — inside the bound, as it must be, and within 15% of it,
which is why the bound is useful for predicting an interpolation error before
running the code.

**(c)** `RectBivariateSpline` with `kx = ky = 3` is the tensor-product cubic
spline evaluated on a rectangular grid; `RegularGridInterpolator(method='cubic')`
is the same order of interpolation reached through a different code path. They
agree to about 1% (0.1518 against 0.1537 m s⁻¹ RMS), which is close enough to
treat them as the same method for practical purposes and far enough apart to
remind you that the two implementations differ at the edges. Neither is more
"accurate"; the lesson is that a 1% difference between two routines is not a
reason to prefer one, and a 10× difference would be.

**(d)** Asymptotically the linear error falls as $h^{2}$ (a factor of 4 per
halving) and the cubic as $h^{4}$ (a factor of 16). Those are the *asymptotic*
rates, and the caveat is the one measured in ★6: they require the field to be
well resolved on the coarse grid. At $h = 1$ km this field has a 6 km scale
length, so it is comfortable and the rates hold; at $h = 4$ km it is not, and
the measured local exponent falls to 1.42. Predicting an error from a
convergence rate is only valid once the rate has been *measured* on the problem
at hand.

---

## ★4 — Clustered samples

**(a)** The inserted sample damages the interpolant locally; the thin bed at
1600 m produces a larger global maximum (30.2 m s⁻¹) and would mask the effect
being measured. Restricting the window to $\pm20$ m around the inserted sample
isolates the mechanism from the unrelated feature.

**(b)** CubicSpline: $510.004/29.987 = 17.0$. PCHIP: $28.927/29.663 = 0.98$ —
i.e. unchanged within 2%.

**(c)** The spline solves for second derivatives $M_i$ from a tridiagonal system
whose right-hand side contains divided differences such as
$(v_{i+1}-v_i)/(z_{i+1}-z_i)$. When two nodes are 5 cm apart with values that
differ by the size of the outlier, that divided difference is large, and the
recurrence propagates the resulting curvature along the whole log. The
mechanism is a division by the node spacing, so the error grows as the spacing
falls — measured as a factor of 17 between 2.00 m and 0.05 m.

**(d)** Two lines: `gaps = np.diff(z)` then
`assert gaps.min() > 0.5 * np.median(gaps)`, or the constructive version used
in the demo — keep only samples at least 2 m apart while building the log. Also
check for exact duplicates (`np.unique(z).size == z.size`), which make the
tridiagonal system singular rather than merely ill-conditioned.

---

## ★5 — Extrapolation

**(a)** At $z = 11$ km: linear
$|2998.3546/2997.8297 - 1| = 1.751\times10^{-4}$; cubic
$|2997.9248/2997.8297 - 1| = 3.174\times10^{-5}$. At $z = 20$ km: linear
$|3012.6864/2999.9407 - 1| = 4.249\times10^{-3}$; cubic
$|3046.6975/2999.9407 - 1| = 1.559\times10^{-2}$.

**(b)** The cubic extrapolates its own polynomial: the last cubic segment,
continued beyond its interval of validity, diverges as the cube of the distance
beyond the edge. The linear rule continues the last slope, which is a bounded
and (for a nearly straight edge trend) reasonable continuation. At 10% beyond
the edge the cubic's smaller local error wins; at 100% beyond, the polynomial's
divergence dominates.

**(c)** $|-690\,412.8|/|-620.031| = 1113.6$ over a distance ratio of
$150/10 = 15$, so $p = \ln(1113.6)/\ln(15) = 2.59$. The exponent is consistent
with cubic growth ($p = 3$) and is smaller than 3 because the two points do not
isolate the asymptotic regime — the last spline segment is short and noisy, so
its own coefficient is the largest source of error at both distances.

**(d)** Refuse: `fill_value=np.nan` with `bounds_error=False` for
`RegularGridInterpolator`, or `extrapolate=False` for `CubicSpline`. A NaN
propagates visibly into every downstream map and statistic, whereas a
plausible-looking number does not — and an extrapolated value is a statement
about a model that has not been chosen or defended.

---

## ★6 — Scattered data

**(a)** 22.25% is the fraction of the 400 check points that lie outside the
convex hull of the 60 stations. It is identical for `linear` and `cubic`
because both are built on the *same* Delaunay triangulation and both return
NaN outside it; only `nearest` extends indefinitely, by Voronoi-cell
assignment.

**(b)** The excess is the sampling-density term. With 60 stations over
$200\ \mathrm{km^2}$ the mean station spacing is about 1.8 km, and a field with
a 6 km scale length interpolated from points 1.8 km apart cannot be recovered
to better than a few per cent of its 250 m s⁻¹ amplitude — of order 10 m s⁻¹
from the sampling alone, and the measured values are consistent with the sum of
that term and the noise term.

**(c)** `nearest` assigns every point in the plane to the closest station, so it
answers everywhere, including hundreds of kilometres outside the survey. The
geophysical consequence is that a `nearest`-gridded national dataset has a
constant value plateau beyond the last station, which is then high-pass
filtered, differentiated or continued by a subsequent processing step as if it
were data.

**(d)** Quadrupling the number of stations halves the average spacing, and the
sampling-density contribution to the error scales roughly linearly with
spacing for a fixed field smoothness, so the sampling term halves: from about
29.5 m s⁻¹ to about 15 m s⁻¹ (a factor of 2, on the assumption that the
sampling term dominates and the 4 m s⁻¹ noise term is unchanged and adds in
quadrature). The noise floor of 4 m s⁻¹ then becomes comparable, so further
densification has diminishing returns.

---

## ★7 — Choosing the smoothing parameter

**(a)** The minimum in the swept range is at $s = 0.5\,n\sigma^2$, with an RMS
error of 5.383 m s⁻¹. The textbook $s = n\sigma^2$ gives 5.773 m s⁻¹, a
**7.2% penalty** — small, and well inside the flat region between
$0.25\,n\sigma^2$ and $1\,n\sigma^2$ where the RMS varies by only 0.6 m s⁻¹.
The criterion is therefore not sharp, which is reassuring: it means the choice
of $s$ is not a hidden tuning parameter of the result.

**(b)** The RMS error is an *average* over the whole log, and most of the log is
smooth: increasing $s$ reduces noise-induced error in those regions faster than
it harms them. The maximum error is decided by the single sharpest feature (the
20 m bed), where smoothing removes signal. As $s$ grows the bed is flattened
monotonically, so the maximum grows monotonically while the average improves
until the flattening spreads.

**(c)** The maximum error, or an RMS measured *within the bed*. A thin-bed study
needs the interpolant that best preserves a 20 m feature, which at a median
sample spacing of 4.7 m is already at the resolution limit; smoothing trades
that feature away. Use PCHIP or the interpolating cubic, and report the
overshoot so the reader knows the trade that was made.

**(d)** Interpolation of noisy data adds a noise-induced error term to whatever
error the interpolant has on the noise-free signal. At $s = 0$ the fit passes
through every sample, so the error at a node is exactly the noise (5 m s⁻¹ in
RMS) and between nodes it is the noise plus the interpolation error, giving
6.576. The best achievable RMS of 5.383 is only 8% above the noise level, which
says that **the interpolant's own signal error is at or below the noise** — the
log cannot be represented better at this sample spacing, and only more samples
or lower noise will improve it.

---

## ★8 — A 3-D model queried at stations

**(a)** `RegularGridInterpolator` on the (lat, lon, depth) axes, with
`method='linear'` or `'cubic'` per axis, because the model is stored on a
rectangular grid and the stations are *queries*, not data. `griddata` is for
scattered *input* data; `CubicSpline` is 1-D; `RectBivariateSpline` is 2-D.

**(b)** The cubic interpolant rings: its kernel has negative lobes, so a
discontinuity produces an oscillatory overshoot of roughly the size of the jump
on both sides, decaying over a few grid cells. The linear interpolant produces a
monotone staircase with no overshoot. The 1-D measurement to cite is the thin
bed of the lesson's §1.2: linear 67.2 m s⁻¹ versus cubic 18.3 m s⁻¹ RMS in a
window around a feature three samples wide — i.e. linear is worse *in the
average sense* at a sharp feature, while the cubic's overshoot is what a
physical bound would forbid.

**(c)** Interpolate *within* each side of the discontinuity and evaluate the
interface depth per station from a separate (smooth) interface grid, choosing
the side by comparing the station depth with the interface depth. The cost is
two interpolations plus one interface lookup instead of one; the benefit is that
no interpolant ever straddles the discontinuity, so neither the ringing nor the
averaging occurs.

**(d)** A $0.25^\circ$ longitude interval corresponds to a physical distance that
shrinks as $\cos(\text{latitude})$: $0.25^\circ$ is 27.8 km at the equator
($0.25 \times 111.3$ km) and only about 9.4 km at $70^\circ$N. The model is
therefore four times finer in the east–west direction than the grid spacing
suggests, and an interpolant that treats the longitude axis as uniform
implicitly applies a different length scale in $x$ and $y$. The correction is to
interpolate in a local Cartesian frame (or on a projected grid) rather than in
degrees, or to supply the interpolator with a metric-corrected coordinate.

---

## ★9 — Gridding a marine gravity survey

**(a)** Along track, 100 m sampling supports wavelengths down to 200 m
(Nyquist), so even a 100 m grid is at the limit; a 1 km grid is safe and
comfortable. Across track, a 10 km line spacing supports no wavelength shorter
than 20 km, so the grid must be no finer than 5 km — and 1–2 km is the usual
compromise because the along-track detail is real and the cross-track detail is
not. The rule is that the grid spacing should not be finer than half the
*tightest* sampling interval in any direction if the product is to be
interpreted as measured data; a finer grid is legitimate only if it is labelled
as interpolated.

**(b)** Linear interpolation (or a spline with tension) along track, and
*across* track something much stiffer: minimum-curvature or spline-in-tension
gridding, or kriging with a strongly anisotropic variogram. The data are
anisotropic — 100 m sampling against 10 km spacing — and an isotropic
interpolant applies the along-track length scale across track, where no
information exists.

**(c)** Without regularisation, a cubic spline across track has freedom between
lines with no data to constrain it, and it oscillates from line to line. The
artefact is a **corrugation** along the ship tracks — a "railroad" or
"egg-carton" pattern whose wavelength is the line spacing — and it is visually
obvious in a shaded-relief map and invisible in a contour map. The related
artefact from minimum-curvature gridding of sparse or clustered control is the
"bull's-eye", a circular high or low between control points.

**(d)** Two quantitative checks. First, **line-withholding cross-validation**:
remove one line, grid from the rest, and compute the RMS misfit on the removed
line, comparing it with the along-track noise level. If the misfit is several
times the noise, the gridding is not predictive across track. Second, a **2-D
spectrum of the grid**: line-correlated artefacts appear as a ridge at the
wavenumber corresponding to the 10 km line spacing, and the ratio of the power
in that ridge to the power at neighbouring wavenumbers is the number to report.
For a well-gridded dataset that ratio should be near 1; a corrugated grid gives
a ridge that is an order of magnitude above its neighbours.
