# Solutions — 07-07-01 Determining the Geoid: Stokes, Remove-Restore, Kriging

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All values are teaching values.

Lesson: [01 Determining the Geoid](../01-geoid-determination.md).

---

## ★1 — The weighting of nearby data

With $\psi$ in radians and $S$ from the Stokes function:

| $\psi$ | $S(\psi)$ | $\psi S(\psi)$ |
|---|---|---|
| $0.02^\circ$ | 5751.537 | 2.0077 |
| $0.5^\circ$ | 241.448 | 2.1070 |
| $3^\circ$ | 44.888 | 2.3503 |

**What the near-constancy implies:** in the integral $\iint\Delta g\,S\,\mathrm
{d}\Omega$, the element of solid angle is $\sin\psi\,\mathrm{d}\psi\,\mathrm
{d}\phi \approx \psi\,\mathrm{d}\psi\,\mathrm{d}\phi$ near the evaluation point,
so the *effective* weight of data at distance $\psi$ is
$\psi S(\psi) \approx 2$ — nearly independent of distance. Nearby data are
therefore weighted **equally per unit distance**, not per unit area, and the
inner zone accumulates weight linearly in $\psi$. That is why a finite grid must
resolve the inner zone (the integral converges, but slowly: the inner cap of
radius $\psi_c$ carries weight $2\psi_c$), and why an unresolved inner zone
appears as a systematic offset rather than as noise.

---

## ★2 — Spectral shares

From the band table (rms values):

**Geoid.** Degrees 2–10: $188.85^2/\Sigma$, degrees 11–20: $22.55^2/\Sigma$:
$$P(2\text{–}20) = \frac{188.85^{2}+22.55^{2}}{190.55^{2}}
= \frac{35664+508.5}{36309} = \frac{36173}{36309} = 99.63\%,$$
$$P(21\text{–}60) = 0.37\%.$$

**Anomaly.**

$$P_{\Delta g}(2\text{–}20) = \frac{58.17^{2}+45.60^{2}}{92.42^{2}}
= \frac{3384+2079}{8541} = \frac{5463}{8541} = 63.96\%,$$
$$P_{\Delta g}(21\text{–}60) = 36.04\%.$$

So the geoid is $99.6\%$ long-wavelength while the anomaly is only $64\%$
long-wavelength: **the two quantities live in different parts of the spectrum**,
and the conversion operator in Stokes' integral is what mixes them. A survey
that measures the anomaly's high-degree part well therefore determines only about
$0.4\%$ of the geoid's variance from local data.

---

## ★3 — Dimensional check

$$\left[\frac{R}{4\pi\gamma}\right]
= \frac{\mathrm{m}}{\mathrm{m\,s^{-2}}} = \mathrm{s^{2}},$$
$$[\Delta g] = \mathrm{m\,s^{-2}},\qquad
[S] = 1,\qquad[\mathrm{d}\Omega] = 1,$$
$$\left[\frac{R}{4\pi\gamma}\iint\Delta g\,S\,\mathrm{d}\Omega\right]
= \mathrm{s^{2}}\times\mathrm{m\,s^{-2}} = \mathrm{m}\ \checkmark$$

The $4\pi$ normalisation is dimensionless, so it cannot hide a unit error; the
one place a mistake hides is a missing or extra factor of $R$, which is why the
$R$ in the prefactor is worth checking against the $R^{-(l+1)}$ radial scaling
each time.

---

## ★4 — Reference-model error propagation

Measured relation (from the demonstration): the geoid error is very nearly linear
in the relative coefficient error,

$$\frac{2.0591}{1.0} = 2.06\ \mathrm{m\ per\ per\ cent},$$

so a $0.3\%$ error gives

$$\sigma_N \approx 0.3 \times 2.06 = 0.62\ \mathrm{m} = 62\ \mathrm{cm}.$$

**For a $1\ \mathrm{cm}$ geoid:** the allowed reference error is
$0.01/2.06 = 0.0049$, i.e. about $5\times10^{-3}$ per cent relative — better
than one part in $2\times10^{4}$ in the long-wavelength coefficients. That is a
demanding but achievable requirement for a satellite-only model at the very long
wavelengths, and it is why modern geoid models quote the reference model's error
as a separate line in their budget.

**Caveat:** the linear relation holds because the reference geoid dominates the
total. If the reference error became comparable with the residual geoid, the
$N_{\text{res}}$ term would correct part of it and the relation would flatten —
another reason the residual integral and the reference model must be reported
together.

---

## ★5 — Deriving the collocation estimator

Let the residual geoid at the target point be $N$ and the observations be
$\mathbf d = \Delta g$ at $n$ points, with

$$\mathrm{Cov}(\mathbf d) = \mathbf C_{dd} + \mathbf D, \qquad
\mathrm{Cov}(N, \mathbf d) = \mathbf c_{Nd},$$

where $\mathbf D$ is the observation-noise covariance. Seek a linear estimator
$\hat N = \mathbf w^{\mathsf T}\mathbf d$ that is unbiased (guaranteed, since the
process has zero mean by construction) and of minimum variance. The variance is

$$\mathrm{Var}(\hat N) = \mathbf w^{\mathsf T}(\mathbf C_{dd}+\mathbf D)\mathbf w
- 2\mathbf w^{\mathsf T}\mathbf c_{Nd} + C_{NN},$$

and $\partial/\partial\mathbf w = 0$ gives

$$(\mathbf C_{dd}+\mathbf D)\,\mathbf w = \mathbf c_{Nd}
\;\Longrightarrow\;
\boxed{\;\hat N = \mathbf c_{Nd}^{\mathsf T}(\mathbf C_{dd}+\mathbf D)^{-1}
\mathbf d\;}$$

with formal variance
$\sigma^{2} = C_{NN} - \mathbf c_{Nd}^{\mathsf T}(\mathbf C_{dd}+\mathbf D)^{-1}
\mathbf c_{Nd}$. $\blacksquare$

**The assumption that makes it "optimal":** that the covariances are *correct*.
The estimator is best-linear-unbiased **under the assumed covariance**; nothing in
the derivation checks the covariance against reality, and the formal variance
$\sigma^{2}$ shrinks as the covariance becomes smoother regardless of whether it
is true. If the covariance is wrong, both the estimate and its error bar are
wrong, and only independent data can reveal it.

---

## ★6 — Truncated covariances and conditioning

The covariance is a sum of terms with *positive* coefficients
$(2l+1)\sigma_l^{2}f_1f_2$ multiplying $P_l(\cos\psi)$. Truncating the sum at
$L_{\max}$ makes the kernel's effective correlation length $\sim 2\pi R/L_{\max}$
in the *shortest*-wavelength direction, but the *long*-wavelength truncation
(keeping only $l \ge l_{\min}$, as remove–restore does) has a different effect:
the retained terms oscillate on scales much shorter than the data spacing, so the
matrix entries are large and highly correlated, and the matrix's eigenvalues span
many orders of magnitude — measured during the demonstration's experiments as a
condition number of order $10^{5}$ with 20–60 closely spaced points.

**Two practical remedies:**

1. **Remove–restore first.** The residual field has a smaller dynamic range and a
   shorter correlation length, so the normal matrix is better conditioned and the
   estimator is closer to an interpolation than an extrapolation.
2. **Regularise, and reduce the data.** Add a small multiple of the identity (or
   use the actual observation-noise covariance, which is a physical
   regulariser), and keep at most about one observation per correlation area —
   adding more densely spaced data does not add information and does add
   numerical noise.

A third, standard remedy is to use a covariance built from the *full* spectrum
(all degrees, not a truncated band) with a smooth taper, which is positive
definite by construction and better conditioned.

---

## ★7 — How large a cap can be used without a reference model (specification)

1. **Test field.** A band-limited synthetic field with a *stated* degree-variance
   law, so both the truth $N$ and the observed $\Delta g$ are known exactly. Use
   at least two spectra (one steep, one shallow) to show the dependence on the
   spectrum.
2. **Cap experiment.** For cap radii from $0.5^\circ$ to $180^\circ$, compute the
   Stokes integral restricted to the cap, with the inner zone treated
   analytically: split the integral into a far part summed on a polar grid centred
   on the evaluation point and a near part evaluated with the closed-form cap
   integral of the kernel (the demonstration's one-dimensional quadrature), so
   that the quadrature error is below the $5\ \mathrm{cm}$ budget.
3. **Diagnostic.** The error in the reconstructed $N$ at the cap centre as a
   function of cap radius; the radius at which the error crosses $5\ \mathrm{cm}$.
4. **Expected dependence.** The answer depends on (i) the amplitude of the
   low-degree part of the field (which no cap can see), (ii) the cap radius
   relative to the longest wavelength retained, and (iii) the inner-zone
   treatment. For the demonstration's spectrum ($98\%$ of the geoid variance in
   degrees 2–10) the $5\ \mathrm{cm}$ cap must be *larger than the Earth*, so the
   honest conclusion is that **no cap suffices** for that spectrum: the method
   requires the reference model. Repeating with a spectrum whose geoid variance is
   concentrated at degrees 50–60 gives a finite cap size, which is the quantitative
   statement of "remove–restore converts a global problem into a regional one".

---

## ★8 — Validating a collocation covariance (specification)

1. **Independent data.** Geoid undulations from levelling plus GNSS along lines
   that were *not* used in the collocation; alternatively the geoid from an
   independent combination of data (a satellite-only model at long wavelengths, a
   different regional data set at short ones).
2. **Diagnostic.** The *normalised* residuals $r_i/\sigma_i$ at the validation
   points: their variance, their spatial correlation and their dependence on the
   distance to the nearest data point.
3. **What a wrong covariance looks like:**
   - covariance too smooth (correlation length too long) $\Rightarrow$
     $\mathrm{Var}(r_i/\sigma_i) > 1$ and a positive *spatial correlation of
     residuals*, with the largest misfits at the validation points farthest from
     data;
   - covariance too rough $\Rightarrow$ $\mathrm{Var}(r_i/\sigma_i) < 1$ with
     residuals that look like white noise but a *bias* where data are sparse
     (the estimator under-extrapolates);
   - a scaling error (a wrong $\sigma_l$ amplitude) $\Rightarrow$ the normalised
     residual variance is uniformly off by a factor, and the collocation's formal
     error bars are uniformly too small or too large.
4. **A second, sharper test.** Compare the *empirical* covariance of the data
   (computed by binning pairs of observations by separation) with the model
   covariance: a systematic shape difference locates the spectral band that is
   mis-modelled, which is far more diagnostic than an rms residual.
