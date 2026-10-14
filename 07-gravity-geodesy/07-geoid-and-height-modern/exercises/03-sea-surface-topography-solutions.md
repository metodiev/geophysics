# Solutions — 07-07-03 Sea Surface Topography and the Marine Geoid

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All values are teaching values.

Lesson: [03 Sea Surface Topography](../03-sea-surface-topography.md).

---

## ★1 — The slope under a $0.5\ \mathrm{m\,s^{-1}}$ current at $50^\circ$N

$$f = 2(7.2921150\times10^{-5})\sin50^\circ = 1.11722\times10^{-4}\
\mathrm{s^{-1}},$$
$$\frac{\partial\eta}{\partial x} = \frac{fv}{g}
= \frac{(1.11722\times10^{-4})(0.5)}{9.81} = 5.694\times10^{-6}
= 5.69\ \mathrm{mm\ per\ km}.$$

So a half-metre-per-second current is driven by under $6\ \mathrm{mm}$ of sea
surface height per kilometre. **This is the number that makes the marine geoid
hard**: the geoid must be known to the level of the *slope*, not the level, over
the length of the current.

---

## ★2 — A constant-slope estimate at $35^\circ$N

$$f = 2(7.2921150\times10^{-5})\sin35^\circ = 8.36517\times10^{-5}\
\mathrm{s^{-1}},$$

$$v = \frac{g}{f}\frac{\Delta\eta}{\Delta x}
= \frac{9.81}{8.36517\times10^{-5}}\cdot\frac{2.0}{2.0\times10^{5}}
= 1.1727\ \mathrm{m\,s^{-1}}.$$

**Why it is an upper bound:** a real jet's height profile is not a linear ramp.
For a sech² profile of half-width $L$, the maximum slope is about
$0.77\,(\eta_{\max}/L)$, whereas a constant-slope estimate uses
$\eta_{\max}/\Delta x$ with $\Delta x = 2L$ — a factor of about $1.5$ smaller, so
the constant-slope velocity overestimates the peak by roughly that factor. Both
numbers are useful: the estimate gives the order, the profile gives the peak.

---

## ★3 — Relative accuracy of the geoid

$$\frac{\text{MDT}}{N} = \frac{1.5\ \mathrm{m}}{100\ \mathrm{m}} = 1.5\times10^{-2}.$$

So the ocean's signal is $1.5\%$ of the quantity that must be subtracted. To
determine the MDT to $10\%$, the geoid must be known to
$0.1\times1.5\% = 0.15\%$ of $N$, i.e. $15\ \mathrm{cm}$ — and, crucially, **in the
band of the oceanographic target**, because the geostrophic balance weights the
slope. A $1\ \mathrm{cm}$ absolute geoid accuracy concentrated at
$10\,000\ \mathrm{km}$ wavelength is of no use for a $100\ \mathrm{km}$ jet.

---

## ★4 — Velocity error for a $3\ \mathrm{cm}$ geoid error

$$\delta v = \frac{g}{f}\,k\,\delta N, \qquad k = \frac{2\pi}{\lambda}, \qquad
\frac{g}{f} = 1.0464\times10^{5}\ \mathrm{m^{2}\,s^{-1}}.$$

| wavelength | $k$ | $\delta v$ |
|---|---|---|
| 100 km | $6.283\times10^{-5}\ \mathrm{m^{-1}}$ | $0.1973\ \mathrm{m\,s^{-1}}$ |
| 300 km | $2.094\times10^{-5}\ \mathrm{m^{-1}}$ | $0.0657\ \mathrm{m\,s^{-1}}$ |
| 1000 km | $6.283\times10^{-6}\ \mathrm{m^{-1}}$ | $0.0197\ \mathrm{m\,s^{-1}}$ |

**Which scale matters:** for a jet of $100\ \mathrm{km}$ width the energy is at
wavelengths of a few hundred kilometres, so the $300\ \mathrm{km}$ column
($0.066\ \mathrm{m\,s^{-1}}$, about $8\%$ of a $0.8\ \mathrm{m\,s^{-1}}$ jet) is
the relevant one; the $1000\ \mathrm{km}$ column is irrelevant to the jet and the
$100\ \mathrm{km}$ column is not resolvable by a $3\ \mathrm{cm}$ geoid. **The
requirement must be stated as an error spectrum, and matched to the target's
band.** If the geoid error happened to be concentrated at $1000\ \mathrm{km}$
instead, the same $3\ \mathrm{cm}$ would be harmless for this jet — which is
precisely why quoting a scalar geoid accuracy is uninformative.

---

## ★5 — Why averaging does not reduce a geoid error

Write the altimetric mean sea surface as

$$\overline{\text{SSH}} = N + \overline{\text{MDT}} +
\overline{\varepsilon_{\text{alt}}},$$

where the bar is a time average. The *ocean's* variability
(eddies, meanders) contributes a term $\overline{\text{MDT}}$ whose deviation from
the true mean MDT falls as $1/\sqrt{n}$ in variance with $n$ independent samples —
so it *does* average down, by roughly $\sigma_{\text{eddy}}/\sqrt{n}$.

The geoid error is not a random sample: it is a **fixed field** that is identical
in every cycle, so

$$\mathrm{Var}\left(\overline{\delta N}\right) = \mathrm{Var}(\delta N)
\quad\text{for every } n,$$

because averaging a constant adds no information about it. Hence the mean
converges to (true MDT) + (geoid error), not to the truth. What averaging buys is
the suppression of the eddy variability — which is why altimetric MDT products are
built from many years of data — and what it cannot buy is the geoid.

**Practical corollary:** the geoid-error contribution to an MDT product is a
*systematic* error field, so it appears in the product's error budget as a
spatially correlated term and must be quantified with an independent geoid
model comparison, not with the data's internal scatter.

---

## ★6 — Two MDT products differing by $8\ \mathrm{cm}$

**Likely causes, in order:**

1. **Different geoid models (or epochs/filters of the same model).** The most
   common cause, because the geoid dominates the error budget and different
   products use different gravity data and different filtering. *Diagnostic:* the
   difference field's spectrum. A difference concentrated at long wavelengths is a
   geoid-model difference; a difference correlated with the coastline suggests a
   different treatment of the coastal strip.
2. **Different time-mean periods.** Two MDTs built from different decades differ
   by the low-frequency ocean variability, which at $8\ \mathrm{cm}$ is plausible
   in a boundary-current region. *Diagnostic:* split one product's record into two
   halves and compute the internal difference — the variability's own magnitude
   sets a floor for any comparison.
3. **Different corrections and filters** (inverted barometer, the reference level
   for the geostrophic velocity, the smoothing applied before differencing).
   *Diagnostic:* apply the documented processing to the same input and check
   whether the difference reproduces; if it does, the difference is a processing
   choice rather than a data discrepancy.

**What distinguishes them cleanly:** the *spectral and temporal signature* of the
difference. A geoid difference is static and long-wavelength; time-mean
variability has a temporal signature when the comparison is repeated for
sub-periods; a processing difference appears exactly when the filter is applied.

---

## ★7 — Validating an MDT product (specification)

1. **Independent data.** (a) Drifting-buoy velocities and drogued drifter
   trajectories; (b) shipboard ADCP sections across the jet; (c) moored current
   meters providing absolute transport at a few sections; (d) Argo displacements
   for the vertical shear and an independent reference velocity; (e) an
   independent geoid model with a different data combination.
2. **Diagnostic at each scale.** Band-pass the MDT-derived velocity and the
   in-situ velocity into the same bands (e.g. 50–150, 150–500, 500–2000 km) and
   compute, per band: the bias, the rms difference, and the correlation. Report
   the *slope of the regression* of in-situ on derived velocity, because a
   scaling error in the geoid's slope shows up as a slope different from 1.
3. **Noise model.** Add in-situ measurement noise and the different sampling
   (few sections vs continuous fields), and Monte-Carlo the resulting uncertainty
   in the band statistics.
4. **What remains degenerate even if validation passes.** (a) A *spatially
   uniform* error in the geoid slope over the whole validation region is
   indistinguishable from a uniform bias in the in-situ velocity, since both
   shift the regression; (b) an error in the geoid that matches the shape of the
   true signal over the validated region cannot be detected there at all —
   validation in one basin says nothing about another; (c) the reference level for
   the transport is not tested by velocity comparisons.
5. **The honest conclusion.** Validation bounds the error *in the validated
   region and band*, and the specification must say so rather than claim a global
   accuracy.

---

## ★8 — Inverted-barometer contamination (specification)

1. **Synthetic truth.** An MDT from a stated jet; an atmospheric pressure field
   whose corresponding inverted-barometer response (a $1\ \mathrm{hPa}$ change
   corresponds to about $1\ \mathrm{cm}$ of sea level, a rounded conventional
   figure) is added to the SSH.
2. **Two error scenarios of the same magnitude.** (a) An error of $2\
   \mathrm{cm}$ in the pressure-derived correction, smoothly varying; (b) a geoid
   error of $2\ \mathrm{cm}$ with the same spatial scale.
3. **Analysis.** Compute the velocity field in both cases and compare with the
   truth.
4. **Prediction.** Both produce a velocity error of the same magnitude and, if
   their spectra are chosen similarly, nearly the same *pattern* — so a single
   realisation cannot separate them. The distinguishing features are:
   - **time dependence:** the inverted-barometer term varies with the weather and
     therefore with time, while a geoid error is static. Comparing two epochs of
     an MDT product separates a time-varying term from a static one.
   - **data source:** the pressure field is independently measured, so an error in
     it can be tested against barometer networks, while a geoid error requires
     independent gravity data.
5. **The experiment's real content** is thus that the contamination is *not*
   separable spatially, and the separation is achieved by the **temporal**
   signature or by an independent realisation of one of the two terms — a
   conclusion that generalises to every systematic term in an MDT budget.
