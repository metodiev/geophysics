---
id: 05-07-02
title: "Quantitative Interpretation and Depth Estimation"
level: advanced
prereqs: ["05-07-01", "05-03-02", "18-01-01"]
tags: [depth-estimation, least-squares, spectral-depth, euler-deconvolution, regional-trend, uncertainty]
---

# Quantitative Interpretation and Depth Estimation

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** depth estimation as an inverse problem with a stated model
   family, a stated noise model, and a stated parameter covariance.
2. **Derive** the depth estimator for a point mass and a line mass, and the
   relation between the parameter covariance and the fitted residual.
3. **Derive** the Fourier spectral depth rule and state the exact condition under
   which it holds — 2-D sources — and the reason it is biased for 3-D sources.
4. **Derive** Euler's homogeneity equation and use it to obtain a depth from an
   anomaly and its derivatives.
5. **Quantify** the bias introduced by an incompletely removed regional field,
   and by a profile that is too short, and show numerically that neither is fixed
   by sampling more densely.
6. **Distinguish** the *statistical* error on a depth (from the noise) from the
   *model* error (from the shape family), and report both.

## Prerequisites

- [05-07-01 Qualitative Interpretation: Anomaly Shape and Position Rules](./01-qualitative-interpretation.md)
  — the half-width constants and the far-field falloff derived there are used
  here without re-derivation.
- [05-03-02 Analytical Solutions for Simple Bodies (Sphere, Sheet, Dyke)](../03-forward-modelling-principles/02-analytical-solutions.md)
  — the model families being fitted.
- [18-01-01 Forward vs Inverse Problems and the Practical Asymmetry](../../18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md)
  — the general framing; this lesson is a single-parameter example of it.

## 1. Intuition: a depth is a fitted parameter, not a recorded number

A depth cannot be measured by a gravimeter. What the instrument records is a
field, and depth enters the field only through a *model*. So every depth you have
ever read in a report satisfies

$$\text{depth} = \text{estimator}\big(\text{data},\ \text{model family},\
\text{noise model},\ \text{processing choices}\big),$$

and there are four inputs, three of which are choices. A depth with no stated
model family is not a scientific statement; it is a number.

This lesson develops the machinery for the simplest model families, because they
are the ones used in practice and the ones whose failure modes are clearest:

- **Curve fitting.** Choose a parametric model (point mass, line mass, prism), fit
  it by least squares, and read the depth from the fitted parameter. This gives a
  covariance, so it gives a *statistical* error.
- **Spectral depth.** Transform the profile and use the decay of the amplitude
  with wavenumber. This is nearly model-free, and that is its attraction — but the
  rule it relies on is exact only for 2-D sources.
- **Euler deconvolution.** Use the homogeneity of the field to solve for the
  source position, with a chosen structural index. Powerful, and catastrophically
  dependent on that index.

The lesson's honest conclusion, demonstrated numerically in Sections 4 and 7, is
that the spread between these three estimators exceeds the statistical error of
any one of them by roughly an order of magnitude. That spread *is* the
uncertainty, and it does not shrink when the data get better.

## 2. Precise definitions

### 2.1 The model family

A **model family** $\mathcal{M}$ is a parametrised set of sources,
$\mathbf{m} = (m_1, \ldots, m_P)$, together with the forward map
$g = \mathcal{F}[\mathbf{m}]$ that produces the predicted data. For a compact body
at a known location,

$$\mathcal{F}[\mathbf{m}](x) = \frac{GMz}{\left((x-x_0)^2+z^2\right)^{3/2}}, \qquad
\mathbf{m} = (M, x_0, z), \tag{1}$$

and a linear regional term adds two more parameters.

### 2.2 The estimator

Given $N$ observations $d_i$ with standard deviations $\sigma_i$, the **least-squares
estimator** is

$$\hat{\mathbf{m}} = \arg\min_{\mathbf{m}}
\sum_{i=1}^{N}\frac{\left(d_i - \mathcal{F}[\mathbf{m}](x_i)\right)^2}{\sigma_i^2}
= \arg\min_{\mathbf{m}} \Phi(\mathbf{m}). \tag{2}$$

### 2.3 The covariance, and what it is not

For Gaussian errors and a well-conditioned problem,
$\operatorname{cov}(\hat{\mathbf{m}}) \approx \left(\mathbf{J}^{\!\top}
\mathbf{W} \mathbf{J}\right)^{-1}$ with $J_{ip} = \partial \mathcal{F}_i/\partial m_p$
and $W = \mathrm{diag}(\sigma_i^{-2})$. This covariance describes the spread of
estimates over *noise realisations within the assumed family*. It is not the
uncertainty in the depth of the Earth, because it excludes every model error
(Section 5).

### 2.4 Structural index

The **structural index** $N$ is the degree of homogeneity of the field:
$\mathcal{F}[\lambda \mathbf{m}] = \lambda^{-N}\mathcal{F}[\mathbf{m}]$ when only
the source coordinate scales. A point mass has $N=2$; a line mass $N=1$; a
contact, $N=0$. Section 3.4 derives the equation in which $N$ appears.

## 3. Derivations

### 3.1 Least squares for the point-mass depth

Take $\mathcal{F}(x) = GMz/\left((x-x_0)^2+z^2\right)^{3/2} + a + bx$ with
parameters $(M, x_0, z, a, b)$. The normal equations are non-linear in $x_0$ and
$z$ and are solved iteratively; the demonstration uses Levenberg–Marquardt via
`scipy.optimize.curve_fit`. Two analytic facts make the result interpretable:

- **Depth–mass trade-off.** For $z$ much larger than the profile half-length, the
  anomaly is nearly a broad dome and $M/z^2$ (the peak) is well determined while
  $M$ and $z$ separately are not. The peak of equation (1) is $GM/z^2$; its
  curvature scales as $GM/z^4$. So the *ratio* of curvature to peak, which is what
  a shape measurement uses, is $z^{-2}$ — this is why depth is a weak parameter.
- **Half-width equivalence.** Equating the half-width of equation (1) at two
  different fractions gives the shape constants of
  [05-07-01 §3](./01-qualitative-interpretation.md). Any estimator that uses only
  widths inherits their 30 per cent model spread.

### 3.2 The spectral depth rule, and exactly when it is exact

For a line mass at depth $z$, equation (4) of
[05-07-01](./01-qualitative-interpretation.md) gives the profile

$$g_\ell(x) = 2G\lambda\,\frac{z}{x^2+z^2}
\quad\Longrightarrow\quad
\hat{g}_\ell(k) = 2G\lambda \int_{-\infty}^{\infty}\frac{z\,e^{-ikx}}{x^2+z^2}
\,\mathrm{d}x = 2\pi G\lambda\, e^{-|k|z}. \tag{3}$$

The transform in equation (3) is the standard Lorentzian pair, and it is exact for
every $z>0$. Taking logarithms,

$$\ln|\hat{g}_\ell(k)| = \ln(2\pi G\lambda) - |k|\,z
\quad\Longrightarrow\quad
z = -\frac{\mathrm{d}\ln|\hat{g}|}{\mathrm{d}|k|}. \tag{4}$$

**So for a 2-D source the spectral depth rule is not a rule of thumb; it is an
identity.** The demonstration confirms it to 0.01 per cent at both 6 km and 30 km
profile lengths.

For a **3-D** (point-mass) source the profile is a *slice* through a 2-D field.
The 1-D spectrum involves a Hankel transform whose asymptotic form is
proportional to $|k|K_1(|k|z)$, not $e^{-|k|z}$. Then

$$\ln|\hat{g}| \approx \text{const} - |k|z + \tfrac12\ln|k|z , \tag{5}$$

and the fitted slope is $z$ minus a term of order $1/(2|k|)$, which *increases*
the fitted slope and therefore biases the depth **shallow**. Measured over the
band $kz = 2$ to $8$: the estimate is 451.5 m for a true 500 m (a 9.7 per cent
shallow bias) at 6 km aperture and 453.7 m at 30 km. The bias is a property of
using a 2-D rule on 3-D data, and it does not go away with a longer profile.

### 3.3 Depth from an incompletely removed regional

Suppose the true data are $d = \mathcal{F} + a_r + b_r x$ and the analyst fits a
model with only a constant offset. The residual after the best fit then must
absorb the ramp. Since a deep point mass is nearly a parabola in $x$ while a ramp
is linear, the estimator can trade one for the other: a straight line is
approximated by part of a very broad, very weak parabola. Hence the fit drives
$z\to\infty$ and $M$ up, keeping $GM/z^2$ small. The demonstration makes this
explicit: with a 0.30 mGal offset and a $10^{-4}$ mGal m⁻¹ slope present but not
fitted, the recovered depth is **7.5 × 10⁴ m** with a residual of only
0.056 mGal. Fitting the ramp, or detrending on the wings before fitting, recovers
depth to $+2.3$ per cent.

> **The general lesson.** An unmodelled term of the wrong *shape* is absorbed
> into the model parameters, and the misfit it leaves can be small. Residual size
> is not a diagnostic of model correctness.

### 3.4 Euler's homogeneity equation

Let $f$ be homogeneous of degree $-N$ in the source-relative coordinate: for a
translation-invariant field, $\mathcal{F}(\lambda \mathbf{r}) =
\lambda^{-N}\mathcal{F}(\mathbf{r})$ about the source position
$\mathbf{r}_0$. Differentiate with respect to $\lambda$ and set $\lambda = 1$:

$$\frac{\mathrm{d}}{\mathrm{d}\lambda}
\left[\lambda^{-N}\mathcal{F}(\mathbf{r})\right]_{\lambda=1}
\;\Longrightarrow\;
(\mathbf{r}-\mathbf{r}_0)\cdot\nabla \mathcal{F} = -N\,\mathcal{F}. \tag{6}$$

Rearranged into the working form, with a constant background $B$,

$$(x-x_0)\frac{\partial g}{\partial x} + (z-z_0)\frac{\partial g}{\partial z}
= -N\,(g - B). \tag{7}$$

For $N$ known, equation (7) is **linear** in $(x_0, z_0, B)$ at each station, so
a set of stations over a profile or a grid gives an overdetermined linear system
that can be solved in closed form. The catch is visible in the equation: $N$
multiplies the data, so a 20 per cent error in $N$ propagates almost directly
into the position and background. Euler deconvolution is best used as a
*classification* tool — scan $N$ and see which value gives consistent solutions
over a window — rather than as a depth meter with a known answer.

### 3.5 Why sampling does not fix the model error

The demonstration fits a **line-mass** model to **point-mass** data at 61, 601
and 6001 stations. The recovered depths are 372.95, 373.28 and 373.31 m, against
a true 500 m: the error is $-25.4$, $-25.3$ and $-25.3$ per cent. Refining the
sampling by two orders of magnitude moves the answer by 0.04 per cent.

This is the quantitative form of the theorem in
[02-08-06](../../02-physics/08-potential-theory/06-uniqueness-theorems.md): the
null space of the potential-field inverse problem contains the difference between
a sphere and a cylinder, and adding more stations samples the same null-space
direction more finely without leaving it.

## 4. Worked examples

### 4.1 One profile, four estimators

Synthetic data: a point mass of $1.0\times10^{10}$ kg at $z = 500$ m, a profile
from $-3$ to $+3$ km with 601 stations, and 0.02 mGal Gaussian noise
(peak signal 0.267 mGal, so signal-to-noise 13).

| Estimator | Depth (m) | Error (%) | Statistical error (m) |
|---|---|---|---|
| Half-width, point-mass rule | 500.03 | $-0.0$ | n/a (noise-free here) |
| Half-width, line-mass rule | 383.23 | $-23.4$ | n/a |
| Least squares, point-mass model | 511.53 | $+2.3$ | 10.6 |
| Least squares, line-mass model | 383.37 | $-23.3$ | 9.1 |
| Spectral, $kz \in [2,8]$ | 451.5 | $-9.7$ | n/a |

The two least-squares fits have residuals of 0.0202 and 0.0204 mGal — the same to
within 1 per cent. **The residual cannot choose between them.** The statistical
error on the point-mass depth is 10.6 m; the spread between the two model families
is 128 m, twelve times larger.

### 4.2 Detecting a trend by its effect, not its size

**Problem.** A survey over a deep target has a 0.30 mGal datum offset and a
$1.0\times10^{-4}$ mGal m⁻¹ drift. The anomaly itself peaks at 0.267 mGal. Will a
constant-only fit mislead?

*Answer.* Yes, catastrophically. Measured recovered depth: 75 309.66 m, i.e.
$+14\,962$ per cent, with residual 0.056 mGal. The offset is *larger* than the
anomaly, and the ramp spans 1 mGal across the 10 km profile. **Always compare the
magnitude of a candidate trend with the amplitude of the anomaly before deciding
whether it can be neglected**, and always plot the trend that was removed.

### 4.3 Depth from a contact gradient

For a thin slab at depth $z$ the horizontal gradient is a Lorentzian of half-width
exactly $z$ (from equation (8) of
[05-07-01](./01-qualitative-interpretation.md)). Measured: a true depth of 100 m
gives a gradient half-width of 100.00 m, and 300 m gives 300.00 m — 0.00 per cent
error in both cases. This estimator is exact for its model, which is a thin slab;
for a slab of finite thickness the half-width is larger than the depth to the
top, so the estimate is a *depth to the centroid-like* quantity, and it should be
labelled that way.

## 5. Assumptions

1. **The source belongs to the fitted family.** Every estimator in Section 3 has
   a model in it; the model error is the dominant error and is not represented by
   any covariance.
2. **Gaussian, zero-mean, independent errors** for the covariance formula to mean
   anything. Correlated (geological) noise inflates the true spread.
3. **An isolated source on a correctly removed regional.** Section 3.3 quantifies
   the cost of getting this wrong.
4. **A profile through, or near, the source centre.** Off-centre profiles
   overestimate depth.
5. **A flat, correctly reduced observation surface.** Terrain and elevation errors
   enter as a long-wavelength false regional.
6. **No remanence/self-demagnetisation effects** in the magnetic case.
7. **Enough aperture.** The spectral estimator needs $kz \gtrsim 2$ and the Euler
   method needs the far field; a profile of two source depths satisfies neither.

## 6. Units and dimensional analysis

- Equation (4): $z = -\mathrm{d}\ln|\hat{g}|/\mathrm{d}|k|$. The left side is m,
  the right is $1/(\mathrm{rad\,m^{-1}})$ ✓, provided $k$ is an angular wavenumber
  in rad m⁻¹. Using cycles per metre without the $2\pi$ inflates the depth by
  $2\pi$; this is the single most common arithmetic error in spectral depth work.
- Equation (6): each of $\partial g/\partial x$, $\partial g/\partial z$ has units
  mGal m⁻¹, and $\mathcal{F}$ has mGal, so
  $\mathrm{m}\cdot\mathrm{mGal\,m^{-1}} = \mathrm{mGal}$ ✓. $N$ is dimensionless.
- Equation (2): $\Phi$ is dimensionless if $\sigma_i$ carries the data units.
  Expressing $\sigma$ in mGal and $d$ in m s⁻² is a silent factor of $10^{5}$.
- The trade-off in Section 3.1: curvature/peak has units of m⁻², so its square
  root is a length — the only length available is $z$, which is why the shape
  measurement is a *depth* measurement and not a mass measurement.

## 7. Python demonstration

`code/quant_interp_demo.py` produces every number quoted above. Predict each
block before running it.

```python
popt, pcov = curve_fit(model_point, x, g, p0=[1e10, 0.0, 500.0, 0.0, 0.0],
                       maxfev=20000)
z = popt[2]
print(f"recovered depth = {z:.2f} +/- {np.sqrt(pcov[2, 2]):.2f} m")
```

Measured output, abridged:

```
1. Half-width rule, with the correct shape assumed
half-width                         =   383.23 m
depth from point-mass rule (1.3048)=   500.03 m
depth from line-mass rule  (1.0)   =   383.23 m
error from using the wrong rule    =   -23.35 per cent

2. Nonlinear least-squares fits, both models, with noise
point mass  recovered depth =   511.53 +/-  10.56 m (   2.31 per cent), RMS 0.0202 mGal
line mass   recovered depth =   383.37 +/-   9.10 m ( -23.33 per cent), RMS 0.0204 mGal

3. Fourier spectral depth: exact for 2-D sources, biased for 3-D
line mass       6 km: kz 2.1-7.8, implied depth  499.96 m (  -0.01 per cent)
line mass      30 km: kz 2.1-8.0, implied depth  500.00 m (  +0.00 per cent)
point mass      6 km: kz 2.1-7.8, implied depth  451.48 m (  -9.70 per cent)
point mass     30 km: kz 2.1-8.0, implied depth  453.73 m (  -9.25 per cent)

4. Depth from a contact's horizontal gradient
true depth    100 m -> gradient half-width   100.00 m (+0.00 per cent)
true depth    300 m -> gradient half-width   300.00 m (+0.00 per cent)

5. Depth error from an unremoved regional trend
fit with a trend term       -> depth    511.30 m (   +2.26 per cent)
detrended on the wings first-> depth    511.30 m (   +2.26 per cent)
fit with a constant only    -> depth  75309.66 m (+14961.93 per cent)
RMS of the constant-only fit = 0.0563 mGal

6. Refining the sampling does not remove the shape ambiguity
   61 stations -> line-mass depth   372.95 m (-25.41 per cent)
  601 stations -> line-mass depth   373.28 m (-25.34 per cent)
 6001 stations -> line-mass depth   373.31 m (-25.34 per cent)
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Two models fit to 0.0202 and 0.0204 mGal RMS but disagree by 128 m | Residual is not a model-selection criterion; report the model spread |
| The point-mass depth has a $\pm10.6$ m statistical error | That number is the *smallest* part of the uncertainty |
| Spectral depth is exact for a line mass and 9.7 per cent shallow for a point mass | The rule's derivation says which sources it applies to |
| The constant-only trend fit returns 75 km with 0.056 mGal residual | Small residuals accompany absurd models |
| Sampling 61 → 6001 stations changes the answer by 0.04 per cent | The ambiguity is in the physics, not in the data density |

> **Breaking exercise.** Set the noise to zero in Section 2 of the demonstration.
> Predict, before running, whether the two models will then agree. They will not:
> the disagreement is model error, and it survives perfect data.

## 8. Exercises

Full problem sets and solutions are in
[`exercises/02-quantitative-interpretation-exercises.md`](./exercises/02-quantitative-interpretation-exercises.md)
and
[`exercises/02-quantitative-interpretation-solutions.md`](./exercises/02-quantitative-interpretation-solutions.md).

### ★ Foundational

**★1.** Write down equation (2) for a point mass at a known horizontal position,
with three parameters $(M, z, a)$. Identify which parameters enter linearly.

**★2.** Using $g_{\max} = GM/z^2$ and the curvature
$\partial^2 g/\partial x^2|_{0} = -3GM/z^4$, show that the ratio of curvature to
peak equals $-3/z^2$ and explain why this makes depth weakly determined.

**★3.** A spectral fit in cycles per metre gives a slope of $-5\times10^{-4}$
cycles⁻¹. Convert to a depth in metres, and state the error if the $2\pi$ is
wrongly omitted.

### ★★ Applied

**★★4.** Reproduce the demonstration's Section 5 numbers using a profile of
5 km half-length. Does the constant-only fit still fail as badly? Explain the
scaling with profile length.

**★★5.** Fit a line mass to point-mass data with the correct quantity of noise
and compute the covariance. Compare the statistical error on $z$ with the actual
error. Why is the actual error so much larger?

**★★6.** The demonstration's spectral bias for a point mass is about $-9.7$ per
cent in the band $kz \in [2,8]$. Compute the bias predicted by equation (5), i.e.
the difference between $z$ and the slope of
$\text{const} - kz + \tfrac12\ln(kz)$, over the same band, and compare.

### ★★★ Research-oriented

**★★★7.** Implement Euler deconvolution of the form of equation (7) for the
synthetic point-mass profile, using the analytic derivatives of the fitted model
for $\partial g/\partial z$. Scan $N \in \{0.5, 1, 1.5, 2, 2.5, 3\}$ and report
which value minimises the scatter of the recovered depths. Then explain why the
scatter *decreases* with $N$ and why that makes the choice of $N$ an
identification rather than a measurement.

**★★★8.** Build a two-body model (a compact body at 300 m and a deep body at
1200 m) and fit a single body to it. Quantify how the recovered depth and mass
depend on the mass ratio of the two bodies, and identify the mass ratio below
which the single-body fit is indistinguishable from the truth at 0.02 mGal
noise. Report the value and the number of stations used.

## 9. Common mistakes

1. **Reporting the covariance as the uncertainty.** It excludes model error, and
   model error is the larger term by an order of magnitude (§4.1).
2. **Forgetting the $2\pi$ in spectral depth.** A factor of 6.28 in depth.
3. **Applying the 2-D spectral rule to 3-D data.** A systematic 10 per cent
   shallow bias (§3.2).
4. **Using a profile shorter than several source depths.** The asymptotic rules
   are not valid, and the failure is silent.
5. **Assuming that more stations, or lower noise, will resolve the model
   ambiguity.** Measured: 0.04 per cent change over a 100-fold refinement (§3.5).
6. **Accepting a model because the residual is small.** The demonstration reaches
   0.056 mGal residual with a 75 km depth (§3.3).
7. **Fitting a trend of unstated order.** The order changes the answer by up to a
   factor of 2.8 in the pitfalls demonstration
   ([05-07-06](./06-interpretation-pitfalls.md)).

## 10. Real-world applications

- **Mineral exploration depth-to-top maps.** These are produced by exactly the
  estimators of Section 3 and are widely used for drilling decisions; the model
  spread of §4.1 is the number a mine geologist needs and is usually the number
  left out.
- **Euler deconvolution in aeromagnetic interpretation.** Standard in regional
  mapping for dyke and contact identification; its dependence on $N$ is the
  reason it is used as a classifier.
- **Spectral depth for basin and Curie-depth mapping.** The 2-D/3-D distinction of
  §3.2 is the difference between a correct basin depth and a 10 per cent error.
- **Reservoir and geothermal depth estimation.** Depth uncertainty translates
  directly into drilling risk and cost, which is why the model spread must be in
  the report ([05-07-05](./05-reporting-results.md)).
- **Inverse-problem practice generally.** The demonstration's Section 6 is the
  cleanest possible statement of why regularisation, priors and independence of
  physics — not data density — are what constrain a geophysical model.

## 11. Further reading

- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*. Cambridge University Press.** Chapters 9–11. Level: advanced.
  The spectral methods of §3.2 are developed properly, including the
  two- versus three-dimensional distinction.
- **Reid, A. B., Allsop, J. M., Granser, H., Millett, A. J. & Somerton, I. W.
  (1990). Magnetic interpretation in three dimensions using Euler deconvolution.
  *Geophysics*, 55(1), 80–91.** Level: advanced. The paper that made Euler
  deconvolution standard practice.
- **Spector, A. & Grant, F. S. (1970). Statistical models for interpreting
  aeromagnetic data. *Geophysics*, 35(2), 293–302.** Level: advanced. The origin
  of the spectral depth method; check your library for access.
- **Menke, W. (2012). *Geophysical Data Analysis: Discrete Inverse Theory*
  (3rd ed.). Academic Press.** Chapters 3–5. Level: advanced. Least squares,
  covariance and resolution in the general form used here.
- **Parker, R. L. (1994). *Geophysical Inverse Theory*. Princeton University
  Press.** Level: graduate. The rigorous account of why potential-field inverses
  have the null spaces that Section 3.5 demonstrates.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-07-01 Qualitative Interpretation: Anomaly Shape and Position Rules](./01-qualitative-interpretation.md)
  — the shape constants and far-field slopes used here.
- [05-07-03 Integrating Multiple Methods and Constraints](./03-multi-method-integration.md)
  — what an independent dataset does to the model spread of §4.1.
- [05-07-05 Reporting Geophysical Results with Honest Uncertainty](./05-reporting-results.md)
  — how to put the statistical error and the model spread into one sentence.
- [05-07-06 Common Interpretation Pitfalls and False Positives](./06-interpretation-pitfalls.md)
  — aliasing and trend artefacts, both of which appear here as silent biases.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md)
  — the general theory of the direction in which §3.5 shows sampling does not help.

## Self-assessment checklist

- [ ] I can write a depth estimation as a model family, an estimator, and a noise
      model, and name which of the three dominates the answer. (§1, §2)
- [ ] I can derive the spectral depth rule and state that it is exact for 2-D
      sources. (§3.2)
- [ ] I can explain the 3-D spectral bias in terms of the Hankel transform. (§3.2)
- [ ] I can derive Euler's equation from homogeneity and explain why $N$ is the
      weak link. (§3.4)
- [ ] I can quantify the damage done by an unremoved linear trend. (§3.3, §4.2)
- [ ] I can demonstrate numerically that sampling does not remove model error.
      (§3.5)
- [ ] I can report a depth as an interval with the statistical error *and* the
      model spread stated separately. (§4.1)
- [ ] I can run the demonstration and explain every printed number. (§7)
