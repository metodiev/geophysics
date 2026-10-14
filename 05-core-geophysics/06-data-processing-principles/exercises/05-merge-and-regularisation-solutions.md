# Solutions — 05-06-05 Gridding, Merging and Levelling of Survey Data

> **Read this after attempting the exercises, not before.** All reference values are
> the ones printed by the module's demonstration scripts.

---

## ★1 — Gridding as invention

Gridding assigns a value to every node of a regular grid, but only a subset of nodes
coincides with a measurement. Between measurements the value is produced by a rule —
a polynomial, a weighting kernel, a smoothness functional — not by observation. The
rule is the invention.

The invention is unavoidable whenever the derived products (contours, derivatives,
continuation) require a regular grid, which is most of the time; and it is
unavoidable when merging surveys with different sampling. What *is* avoidable is
presenting the result as though the invented values were measured.

---

## ★2 — Continuation transfer functions

A potential field in a source-free region satisfies Laplace's equation, so a Fourier
component at horizontal wavenumber $|k|$ varies vertically as $e^{\pm|k|z}$.
Finiteness as $z \to +\infty$ selects $e^{-|k|z}$, giving upward continuation

$$\hat f(k; z_2) = e^{-|k|\Delta z}\hat f(k; z_1), \qquad \Delta z = z_2 - z_1 > 0,$$

and downward continuation, the formal inverse,

$$\hat f(k; z_1) = e^{+|k|\Delta z}\hat f(k; z_2). \ \boxed{}$$

The **upward** operator is bounded by 1 for all $k$; the downward operator is
unbounded.

---

## ★3 — The derivative noise gain

White noise has a flat spectral density over the representable band
$|k| \le k_N$, so the ratio of output to input variance for the operator $k^{n}$ is
the mean of $k^{2n}$ over the band:

$$\frac{\sigma_{\text{out}}^{2}}{\sigma_{\text{in}}^{2}}
= \frac{\int_{-k_N}^{k_N}k^{2n}\,\mathrm{d}k}{\int_{-k_N}^{k_N}\mathrm{d}k}
= \frac{2k_N^{2n+1}/(2n+1)}{2k_N} = \frac{k_N^{2n}}{2n+1},$$

hence an **amplitude** gain $k_N^{n}/\sqrt{2n+1}$ with
$k_N = \pi/\Delta x$. $\boxed{}$

---

## ★4 — Gains at 50 m spacing

$k_N = \pi/50 = 0.062832$ rad/m.

- $n = 1$: $0.062832/\sqrt3 = \boxed{0.036276}$ per metre.
- $n = 2$: $0.062832^{2}/\sqrt5 = 3.9478\times10^{-3}/2.2361
  = \boxed{1.7655\times10^{-3}}$ per metre².

Both agree with the lesson's measured row for $\Delta x = 50$ m (0.03632 and
0.00177).

---

## ★5 — Reduction to the pole

RTP assumes **induced magnetisation** with a **known ambient field direction**, so
that the magnetisation and the measured component share one direction. When the
assumption fails — because the magnetisation is remanent, or the direction is wrong —
the operator is simply incorrect, and the result is a distorted anomaly whose shape
and position are both wrong (the lesson measures up to 9.85 % of the peak as a
systematic error for a 30° error in the assumed inclination).

---

## ★★6 — Undersampling at 250 m over a 300 m body

**(a)** The lesson's table for a comparable geometry gives −9.51 % at 250 m spacing.

**(b)** The table gives −3.84 % at 100 m. So a spacing between 100 and 250 m is needed
for below 5 %; interpolating between −9.51 % (250 m) and −3.84 % (100 m), about
**150 m** would give roughly −5 %.

**(c)** Because a linear interpolant can never exceed the maximum of its samples, and
cubic and RBF interpolants can only overshoot locally. The peak is *between* samples,
so its true value was never recorded; every interpolant must guess, and the guesses
cluster near the sample values. The only fix is a finer grid — Section 2.2 of the
lesson.

---

## ★★7 — Downward continuation of a 400 m dipole by 100 m

**(a)** $(h/(h-\Delta z))^{3} = (400/300)^{3} = \boxed{2.370}$.

**(b)** $k_N = \pi/20 = 0.157080$ rad/m; the grid's $|k|$ ranges over
$[0, \sqrt2 k_N] = [0, 0.22214]$ rad/m. The predicted white-noise gain is the RMS of
$e^{|k|\Delta z}$ over the grid's wavenumbers; a reasonable estimate from the lesson's
scaling (which used $\Delta x = 25$ m and gave $2.989\times10^{6}$ at
$\Delta z = 100$ m) scales as $e^{|k|\Delta z}$ with $|k| \propto 1/\Delta x$, so at
$\Delta x = 20$ m the gain is larger. A defensible answer reports the gain as
$\mathcal{O}(10^{8})$ and states that it must be measured numerically on the actual
grid rather than estimated.

**(c)** $5\ \mathrm{nT} \times 10^{8} = 5\times10^{8}$ nT of noise against a signal of
2400 nT — the continuation is **meaningless**. It is exactly the case the lesson's
measured table shows: at $\Delta z = 100$ m the noise reached $5.1\times10^{7}$ nT
against a signal of 3125 nT. Only a band-limited (stabilised) continuation is
usable, and its retained wavelengths set the resolution.

---

## ★★8 — RTP with a 25° error in inclination

**(a)** The lesson measures 5.51 % at a 15° discrepancy (true 45° against an assumed
60°) and 5.26 % at a 15° discrepancy on the other side (75°), and 9.85 % at 30°
(true 90°). A 25° discrepancy (true 40° against assumed 65°) therefore lies between:
**roughly 8–10 % of the peak**. The exact value requires running the operator, which
is the honest answer — the lesson's table is not linear in the discrepancy.

**(b)** **No.** The error is a deterministic function of the operator and the field, so
a repeated survey reproduces it exactly. Repeatability tests cannot see a systematic
transformation error.

**(c)** Deliver a **direction-free quantity** — the analytic signal amplitude, or a
total-horizontal-derivative magnitude — alongside the RTP product, and state that RTP
carries an unquantified direction assumption. The lesson's measured table says why:
the analytic signal is symmetric over the source and independent of the assumed
magnetisation direction, so it locates the body without the assumption. What it does
*not* do is improve the noise — its noise gain is of the same order as the first
derivative's (measured 0.0579 against 0.0614 per metre).

---

## ★★9 — Where the peak error comes from

**(a)** The **undersampling** term dominates, 25 % against 5 % — a factor 5. More
precisely, if the error contributions add in quadrature the totals are
$\sqrt{25^{2}+5^{2}} = 25.5$, so undersampling carries 96 % of the variance.

**(b)** **No.** A better interpolator addresses the 5 % term. The 25 % term is
information that was never acquired, and no interpolant can recover it — the lesson's
measured peak errors of −46.34 % (1000 m), −37.93 % (500 m), −9.51 % (250 m) and
−3.84 % (100 m) are all from the *same* linear interpolator.

**(c)** Recommendation: "The peak amplitude is under-estimated by about 25 % because
the station spacing is too coarse for the target's depth; this is an acquisition
limitation, not a processing one, and it cannot be corrected. If the peak amplitude
matters, re-acquire at approximately 150 m spacing; otherwise report the anomaly
amplitude as a lower bound and state the bound."

---

## ★★★10 — Minimum curvature versus the interpolants

A satisfactory answer will:

1. Implement the minimum-curvature surface as the solution of the biharmonic equation
   (or a finite-difference equivalent) subject to honouring the data at the sample
   nodes.
2. Report for the lesson's synthetic field: a small RMS error in the interior,
   a peak error comparable with or better than cubic, and — the key diagnostic —
   **behaviour in a data gap**: minimum curvature produces the smoothest possible
   surface, so a gap is filled with a broad, flat interpolation that can *under*shoot
   the true anomaly substantially.
3. Explain why it is **not** a reconstruction: reconstruction (the sinc interpolant)
   presumes a band limit and recovers the unique band-limited field; minimum curvature
   presumes a *smoothness functional* and recovers the smoothest surface, which is a
   different field whenever the truth is not the smoothest surface consistent with the
   samples.
4. Report the honest limitation: in a gap, the uncertainty is not the interpolant's
   error but the *range* of plausible fields, which cannot be estimated from the
   interpolant at all.

---

## ★★★11 — FFT wraparound in continuation

A satisfactory experiment varies the taper width (from no taper to a full
half-cosine) and reports, separately, the **interior** error (against the analytic
continuation) and the **edge** error:

- **Interior error** falls rapidly with taper width and saturates once the taper's
  width exceeds the decay length of the operator's impulse response.
- **Edge error** falls with taper width but at the price of *discarding data*: the
  tapered region's values are attenuated and then divided out, which amplifies noise
  there (the same mechanism as the taper used to be divided out). So the edge error
  after de-tapering can *increase* with taper width.

**Practical rule:** apply the operator with explicit padding (reflection or
extrapolation) rather than a taper, and evaluate results only in the interior with a
margin of the operator's effective width. **Cost:** the interior area shrinks, and for
small grids the usable area can be a small fraction of the input — which is why
continuation of small grids is unreliable and is one of the reasons the operators are
applied to regional compilations rather than to local surveys.

---

## ★★★12 — Micro-levelling versus real structure

A satisfactory experiment builds a field containing:

- line-correlated stripes at the acquisition line spacing (the artefact);
- a genuine linear dyke crossing the lines (the signal).

Applying a micro-levelling filter with a correlation length $\ell$ and reporting the
recovered dyke amplitude:

| $\ell$ relative to the dyke width | recovered dyke amplitude | stripes removed |
|---|---|---|
| much smaller than the dyke width | close to true | few |
| comparable to the dyke width | **attenuated** | most |
| much larger than the dyke width | strongly attenuated or removed entirely | all |

**Criterion for choosing the filter:** require the filter to remove the stripe
component while leaving the power spectrum at the dyke's characteristic wavenumber
unchanged. This is checkable on real data by comparing the radially averaged spectra
before and after — a *spectral* test, not a visual one — and by checking that the
known-interval stripes are gone.

**Caveat that must be stated:** if the dyke's wavenumber is close to the stripe
wavenumber, *no* filter separates them, and the honest answer is that the survey
cannot distinguish the two. That is a data-design conclusion, not a processing one.
