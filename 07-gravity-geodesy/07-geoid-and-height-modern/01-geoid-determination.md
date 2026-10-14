---
id: 07-07-01
title: "Determining the Geoid: Stokes, Remove-Restore, Kriging"
level: research
prereqs: ["07-01-02", "07-04-02", "07-05-03"]
tags: [gravity, geodesy, geoid, stokes, remove-restore, collocation]
---

# Determining the Geoid: Stokes, Remove-Restore, Kriging

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the geodetic boundary-value problem that the geoid solves, and
   **derive** Stokes' integral from the $(l-1)$ relation between the gravity
   anomaly and the disturbing potential.
2. **Describe** the Stokes function: its $1/\psi$ behaviour, its vanishing
   integral over the sphere, and what each implies for a numerical
   implementation.
3. **Quantify** what a regional gravity data set can determine, by computing the
   spectral content of the geoid and of the gravity anomaly and comparing them.
4. **Explain and apply** remove–restore, and **measure** the error a reference
   model's coefficient error propagates into the geoid.
5. **Derive** the least-squares collocation (Kriging) estimator and state the
   sense in which its answer is a promise about the covariance rather than a
   measurement.
6. **Choose** between a global integral, remove–restore and collocation for a
   stated data situation, and **justify** the choice with numbers.
7. **State** the non-uniqueness that remains in every geoid determination, and
   the independent data that constrain it.

## Prerequisites

- [07-01-02 Gravitational Potential, Equipotentials and the Geoid](../01-gravity-fundamentals/02-gravity-potential.md) —
  the disturbing potential, Bruns' formula and the boundary condition.
- [07-04-02 Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](../04-geodesy-reference-frames/02-height-systems.md) —
  what the geoid is used for, and how it enters a height.
- [07-05-03 Spherical Harmonic Solutions and Coefficient Interpretation](../05-satellite-gravimetry/03-spherical-harmonic-solutions.md) —
  the $(l-1)$ factor and the degree-variance formalism used throughout.

> **All models and data in this module are SYNTHETIC.** The coefficient spectrum,
> the reference model, the noise and the data distribution are teaching values.
> No measured gravity field, geoid model or levelling datum is used.

## 1. The problem, and why a boundary-value problem is the right frame

The geoid is the equipotential surface that best fits mean sea level. Determining
it from gravity is a **boundary-value problem**: given the gravity anomaly
$\Delta g$ on the surface of the Earth (which is itself unknown), find the
disturbing potential $T$ — and hence, by Bruns' formula $N = T/\gamma$, the
geoid.

Stokes solved the spherical, constant-radius version of this problem in the
nineteenth century. The result is an integral operator:

$$\boxed{\;N(P) = \frac{R}{4\pi\gamma}\iint_{\sigma}\Delta g\,S(\psi)\,
\mathrm{d}\Omega\;}$$

with $S$ the Stokes function and $\psi$ the angular distance from the evaluation
point $P$. The demonstration works with exactly this operator, band-limited to
degree 60, and its numbers set the scale of the whole lesson: a synthetic geoid
of rms $190.55\ \mathrm{m}$ and gravity anomalies of rms $92.42\ \mathrm{mGal}$.

**Why an integral and not a sum.** From
[07-05-03](../05-satellite-gravimetry/03-spherical-harmonic-solutions.md), the
degree-$l$ gravity anomaly is $(l-1)$ times the corresponding geoid term. Inverting
degree by degree would give a factor $1/(l-1)$, so the conversion is a *filter* —
and a filter with a kernel that spreads every anomaly over the entire sphere. The
non-local character of that kernel is the origin of every practical difficulty in
this lesson.

## 2. The Stokes function

$$S(\psi) = \frac{1}{\sin(\psi/2)} - 6\sin\frac{\psi}{2} + 1 - 5\cos\psi
- 3\cos\psi\,\ln\!\left(\sin\frac{\psi}{2} + \sin^{2}\frac{\psi}{2}\right).$$

The demonstration evaluates it, and its cap integral
$\int_0^{\psi_c}S(\psi)\sin\psi\,\mathrm{d}\psi$ (computed by one-dimensional
quadrature to machine precision):

| $\psi$ | $S(\psi)$ | $\psi S(\psi)$ | $2\pi\int_0^{\psi_c}S\sin\psi\,\mathrm{d}\psi$ |
|---|---|---|---|
| $0.01^\circ$ | 11483.2 | 2.0042 | 0.002196 |
| $0.1^\circ$ | 1163.04 | 2.0299 | 0.022111 |
| $1^\circ$ | 124.737 | 2.1771 | 0.230491 |
| $5^\circ$ | 27.916 | 2.4362 | 1.254719 |
| $30^\circ$ | 1.894 | 0.9918 | 6.586473 |
| $90^\circ$ | $-1.828$ | $-2.8721$ | $-2.043498$ |
| $180^\circ$ | 3.079 | 9.6744 | $-0.000000$ |

Three facts, each with a consequence:

1. **$S \sim 2/\psi$ as $\psi \to 0$.** The kernel is singular but integrable:
   $\psi S \to 2$ as $\psi \to 0$, so the *integrand* stays finite. The singular
   behaviour is a statement about the *weighting* of nearby data, and a finite
   quadrature grid that does not resolve the inner zone gives a wrong answer —
   as the writing of this demonstration confirmed before the inner zone was
   handled by the analytic cap integral.
2. **$\int_0^{180^\circ} S\sin\psi\,\mathrm{d}\psi = 0$** (measured:
   $-1.3\times10^{-11}$ against a peak running integral of $6.586$, i.e. zero to
   $2\times10^{-12}$ relative — the residual is quadrature round-off on a
   cancellation of order $10^{12}$). The kernel integrates to zero,
   which is why a *constant* gravity anomaly produces *no* geoid signal: the mean
   of $\Delta g$ over the sphere is not part of the problem. Numerically, this
   cancellation is a brutal test of any quadrature scheme.
3. **$\psi S(\psi)$ is nearly constant out to a few degrees** — the famous
   $S \approx 2/\psi$ regime. The geoid at a point is therefore dominated by the
   gravity anomalies within a few degrees of it, *through a kernel that does not
   decay*.

## 3. What a regional survey can and cannot see

Here is the quantitative heart of the lesson. Splitting the synthetic field into
degree bands:

| degrees | $\Delta g$ rms (mGal) | $N$ rms (m) | share of $N$ variance |
|---|---|---|---|
| 2–10 | 58.17 | 188.85 | **98.23%** |
| 11–20 | 45.60 | 22.55 | 1.40% |
| 21–40 | 43.76 | 10.57 | 0.31% |
| 41–60 | 34.37 | 4.67 | 0.06% |
| 2–60 | 92.42 | 190.55 | 100.00% |

**Gravity anomalies are spread across the spectrum; the geoid is almost entirely
long-wavelength.** In this synthetic field, $98.2\%$ of the geoid variance comes
from degrees 2–10, while those degrees contribute only $(58.17/92.42)^2 = 40\%$
of the anomaly variance.

*Worked example 1 (the two rms levels are not comparable).* A survey that
determines the local gravity anomaly to $1\ \mathrm{mGal}$ observes the
high-degree part of the field well and the low-degree part not at all. Since the
geoid is $98\%$ low-degree, such a survey determines $98\%$ *less* of the geoid
than the naive ratio of rms values would suggest: the geoid from local data alone
is missing the part that matters. The numerical version of this statement: with a
$5^\circ$ cap and an unmodelled long-wavelength field, the error is of order the
reference geoid's rms, $190\ \mathrm{m}$ — for a *centimetre* target that is a
factor $10^{4}$.

The lesson is not that regional gravity is useless: it is that regional gravity
determines the *residual* geoid, and the long wavelengths must come from
somewhere else — a global satellite model, or (historically) astrogeodetic
deflections of the vertical.

## 4. Remove–restore, and what it inherits

The method:

1. **Remove** a reference field (here degrees 2–20) from the observed anomalies:
   $\Delta g_{\text{res}} = \Delta g - \Delta g_{\text{ref}}$.
2. **Compute** the residual geoid by Stokes' integral of $\Delta g_{\text{res}}$
   over the data region.
3. **Restore** the reference geoid: $N = N_{\text{ref}} + N_{\text{res}}$.

The demonstration verifies the identity: with a *perfect* reference field the
reconstruction error is $3.5\times10^{-13}\ \mathrm{m}$ — round-off. The method is
exact; its error is entirely the reference model's.

*Worked example 2 (the reference model IS the answer).* Perturb the reference
coefficients by a relative error and measure the geoid error:

| reference coefficient error | geoid error rms (m) | max (m) |
|---|---|---|
| 0.0% | 0.0000 | 0.0000 |
| 0.1% | 0.1328 | 0.4349 |
| 1.0% | 2.0591 | 6.5362 |
| 5.0% | 7.8625 | 18.1393 |
| 10.0% | 18.4577 | 45.9052 |

The error is almost exactly linear in the perturbation (a $1\%$ error gives
$2.06\ \mathrm{m}$; a $10\%$ error gives $18.5\ \mathrm{m}$), because the
reference geoid dominates the total. **A $0.1\%$ coefficient error is already
$13\ \mathrm{cm}$**, so a centimetre geoid requires the long-wavelength model to
be good to better than $10^{-4}$ relative — which is why satellite gravity
missions, whose strength is exactly the long wavelengths, are the enabling
technology for modern geoid models.

The demonstrably honest summary of a geoid computation is therefore a
**three-part statement**: the reference model and its error, the data region and
its resolution, and the residual integral's method. Any one of the three omitted
makes the reported accuracy meaningless.

## 5. Least-squares collocation (Kriging)

The alternative to an explicit integral is to treat the residual field as a
random process with a covariance function derived from its degree-variance
spectrum,

$$C(\psi) = \sum_l \sigma_l^{2}(2l+1)\,P_l(\cos\psi)\;f_1(l)\,f_2(l),$$

with $f_{\Delta g}(l) = (GM/R^{2})(l-1)$ and $f_N(l) = GM/(R\gamma)$ for the two
quantities. The residual geoid at a point is then estimated by

$$\hat N = C_{N\Delta g}^{\mathsf T}\left(C_{\Delta g\Delta g} +
\mathbf{D}\right)^{-1}\mathbf{d},$$

where $\mathbf{d}$ are the residual anomaly observations and $\mathbf{D}$ their
noise covariance. This is least-squares collocation, and it is Kriging with a
covariance known from physics rather than fitted to variograms.

*Worked example 3 (what "optimal" means here).* The estimator is the
minimum-variance linear unbiased estimate **under the assumed covariance**. Its
formal error bar is $\sigma^{2}= C_{NN} -
C_{N\Delta g}^{\mathsf T}(C_{\Delta g\Delta g}+\mathbf{D})^{-1}C_{N\Delta g}$,
which is small whenever the covariance is *smooth* — regardless of whether it is
right. Two consequences:

- A wrong covariance gives a **confident wrong answer**. Validation against
  independent data (levelling, GNSS/geoid differences, a satellite-only model at
  long wavelengths) is part of the method, not an optional extra.
- The estimator is a *projection onto the model space of the covariance*: what it
  cannot know, it substitutes with the covariance's implied continuation. It
  therefore does not escape Section 3: without a reference model, the long
  wavelengths are still invented rather than measured.

**Numerical warning, measured during the writing of this demonstration.** With
the covariance built from a truncated spectrum and many closely spaced points,
the normal matrix $C_{\Delta g\Delta g} + \mathbf{D}$ has a condition number of
order $10^{5}$ and the estimator becomes unstable: adding a dense local network
to a covariance whose correlation length exceeds the network diameter does not
add information, it adds numerical noise. The practical remedies are exactly the
practitioner's habits — remove–restore first, so the residuals are small and
better conditioned; keep the data set to one observation per correlation area;
and regularise.

## 6. Assumptions and regime of validity

1. **Spherical, non-rotating, constant-radius boundary.** Stokes' formula assumes
   the boundary is a sphere; real computations need the ellipsoidal correction
   and the downward continuation of surface gravity to the geoid.
2. **$T$ harmonic outside the masses.** Everything above the topography must be
   removed (the terrain correction) or the data are not on a harmonic boundary.
3. **$\gamma$ is the normal gravity.** Its latitude dependence is a
   $0.5\%$ effect, i.e. metres, so it must be modelled (see
   [07-05-03](../05-satellite-gravimetry/03-spherical-harmonic-solutions.md)).
4. **A complete global data set, or a reference model.** Stokes' integral is
   non-local; a cap is a truncation, and the truncation error is a
   long-wavelength error.
5. **A covariance, if collocation is used.** Its correctness cannot be verified
   from the same data.
6. **No masses outside the boundary.** Classical Stokes theory assumes no
   topography; in practice the terrain and the atmosphere-ocean mass are removed
   with models whose errors are systematic.

## 7. Python demonstration

`code/geoid_determination_demo.py` prints, with units:

1. **A synthetic field** band-limited to degree 60: geoid rms $190.55\ \mathrm{m}$,
   anomaly rms $92.42\ \mathrm{mGal}$.
2. **The Stokes kernel** and its cap integral, showing $S\sim2/\psi$ and
   $\int_0^\pi S\sin\psi\,\mathrm{d}\psi = -1.3\times10^{-11}$, i.e. zero to
   $2\times10^{-12}$ relative.
3. **The regional-blindness result**: a table of the spectral content of $N$ and
   $\Delta g$, with $98.23\%$ of the geoid variance in degrees 2–10.
4. **Remove–restore**: exact to $3.5\times10^{-13}\ \mathrm{m}$ with a perfect
   reference field, and the measured propagation of reference-model errors
   ($1\%$ coefficient error $\to$ $2.06\ \mathrm{m}$ geoid rms).
5. **The collocation estimator**, stated with the conditioning warning measured
   during the experiment.

Print-only, fixed seed, no network, exits 0.

## 8. Exercises

Full sets with worked solutions are in
[`exercises/01-geoid-determination-exercises.md`](./exercises/01-geoid-determination-exercises.md)
and
[`exercises/01-geoid-determination-solutions.md`](./exercises/01-geoid-determination-solutions.md).

- **★** Compute the ratio $\psi S(\psi)$ at $0.02^\circ$, $0.5^\circ$ and
  $3^\circ$, and state what its near-constancy implies for the weighting of
  nearby data.
- **★** From the band table, compute the share of the geoid variance in degrees
  2–20 and in degrees 21–60.
- **★★** A reference model has a $0.3\%$ relative coefficient error. Estimate the
  resulting geoid error from the demonstration's linear relation, and state what
  accuracy of the coefficients a $1\ \mathrm{cm}$ geoid needs.
- **★★** Derive the collocation estimator from the Bayesian/minimum-variance
  argument, and state precisely which assumption makes it "optimal".
- **★★★** Design a numerical experiment that determines how large a data cap can
  be without a reference model before the truncation error exceeds a
  $5\ \mathrm{cm}$ budget, and specify how the inner zone is handled.

## 9. Mastery checkpoint

Do this without notes:

> Using the demonstration's numbers: **(a)** state Stokes' formula and the
> quantity each symbol denotes; **(b)** explain why
> $\int_0^{\pi}S\sin\psi\,\mathrm{d}\psi = 0$ matters physically;
> **(c)** given that $98.23\%$ of the geoid variance is in degrees 2–10, state
> what fraction of the geoid a survey that measures only $\Delta g$ can determine,
> and what it must be given; **(d)** a reference model's coefficients are wrong by
> $0.5\%$: estimate the geoid error; **(e)** state two independent data sets that
> could detect such an error.

*Answers.* **(a)** $N(P) = \frac{R}{4\pi\gamma}\iint_\sigma\Delta g\,S(\psi)\,
\mathrm{d}\Omega$: $R$ the mean Earth radius, $\gamma$ the normal gravity,
$\Delta g$ the gravity anomaly on the boundary, $S$ the Stokes function,
$\psi$ the spherical distance from $P$, $\mathrm{d}\Omega$ the element of solid
angle. **(b)** A constant $\Delta g$ over the whole sphere corresponds to a
different total mass, not to a geoid *shape*; the kernel's zero integral projects
out the mean, which is why the mean anomaly carries no geoid information and why
quadrature schemes that do not reproduce the zero give systematic offsets.
**(c)** Local $\Delta g$ determines the *residual* geoid only; the long
wavelengths (which are $98.2\%$ of the variance here) must come from a global
model or an independent technique — historically astrogeodetic deflections, today
a satellite-only model. **(d)** From the measured linear relation
($1\%\to2.06\ \mathrm{m}$), $0.5\%$ gives about $1.0\ \mathrm{m}$, i.e.
$103\ \mathrm{cm}$. **(e)** Levelling plus GNSS (geoid undulations along a
levelling line differ only in the long wavelengths), and an independent
satellite-only solution's low-degree coefficients; a third is a set of
astrogeodetic deflections.

## 10. Common pitfalls

1. **Quoting a geoid accuracy without the reference model.** The reference *is*
   the answer at long wavelengths.
2. **Assuming regional data determine the geoid.** They determine the residual
   geoid; the rest is a model.
3. **Ignoring the inner zone of the kernel.** A quadrature grid that does not
   resolve $\psi \to 0$ gives a wrong answer, and the error looks like a
   constant offset.
4. **Trusting a collocation error bar from an unvalidated covariance.**
5. **Confusing the geoid and the anomaly spectra.** One is long-wavelength, the
   other is not.
6. **Forgetting the terrain and the atmosphere.** The boundary must be harmonic.
7. **Mixing the ellipsoidal correction with the datum offset.** They are
   different kinds of number, and one of them is a choice (see
   [02](02-vertical-datum-modernisation.md)).

## 11. Real-world applications

- **National height systems.** A geoid model converts GNSS ellipsoidal heights to
  orthometric heights; this is the operational reason geoid models exist.
- **Levelling network control.** Geoid differences between levelling benchmarks
  detect and correct systematic levelling errors over long lines.
- **Ocean and ice surfaces.** A geoid is the reference for dynamic ocean
  topography ([03](03-sea-surface-topography.md)) and for ice-sheet surface
  elevations.
- **Datum unification.** Replacing spirit levelling over long distances with
  GNSS plus a geoid model is a datum decision, and its error budget is the geoid
  error of Section 4.

## 12. Further reading

- **Heiskanen, W. A. & Moritz, H., *Physical Geodesy*** — Stokes' theory, the
  Stokes function and least-squares collocation, in the classical formulation.
- **Hofmann-Wellenhof, B. & Moritz, H., *Physical Geodesy*** — the modern
  boundary-value treatment and the ellipsoidal corrections.
- **Torge, W. & Müller, J., *Geodesy*** — geoid computation in practice, with the
  reference-model and data requirements.
- **Kaula, W. M., *Theory of Satellite Geodesy*** — degree variances and the
  spectral language used in Section 3.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Editions and years are omitted
> because they differ between printings.

## 13. Related lessons

- [02 Vertical Datum Modernisation and National Height Systems](02-vertical-datum-modernisation.md) —
  what the geoid is used for, and what a datum offset means.
- [03 Sea Surface Topography and the Marine Geoid](03-sea-surface-topography.md) —
  the same geoid over the ocean, where the signal is the sea surface itself.
- [07-05-03 Spherical Harmonic Solutions and Coefficient Interpretation](../05-satellite-gravimetry/03-spherical-harmonic-solutions.md) —
  where the long wavelengths come from.
- [07-04-02 Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](../04-geodesy-reference-frames/02-height-systems.md) —
  the height systems the geoid defines.

## 14. Related modules

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md).
- [07-04 Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md).
- [07-05 Satellite Gravimetry](../05-satellite-gravimetry/README.md).
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the estimator, the
  covariance and the regularisation.
- [26-reference-library](../../26-reference-library/README.md).

## 15. Self-assessment checklist

- [ ] I can state the boundary-value problem and Stokes' formula.
- [ ] I can describe the kernel's singularity and its zero integral.
- [ ] I can compute the spectral split of the geoid and the anomaly.
- [ ] I can apply remove–restore and propagate a reference error.
- [ ] I can write the collocation estimator and say what makes it "optimal".
- [ ] I can state when collocation is ill-conditioned and what to do.
- [ ] I can name the independent data that constrain a geoid model.
