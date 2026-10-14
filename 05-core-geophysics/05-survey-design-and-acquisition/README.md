# Module 05-05 — Survey Design and Acquisition

**Stages:** intermediate → graduate · **Prerequisites:**
[05-01 What Geophysics Measures](../01-what-geophysics-measures/README.md)
(property contrasts, the resolution/depth trade-off, non-uniqueness),
[05-02 Geophysical Fields and Observables](../02-geophysical-fields-and-observables/README.md)
(units, and where noise and drift come from),
[05-03 Forward Modelling Principles](../03-forward-modelling-principles/README.md)
(the analytic solutions used to predict whether a target is detectable),
[01-10 Fourier Analysis](../../01-mathematics/10-fourier-analysis/README.md)
(the sampling theorem, aliasing and the folding formula),
[01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md)
(the standard deviation as the unit of detectability),
[05-04 Rock Physics](../04-rock-physics/README.md)
(for the property contrasts that make a target worth surveying).

This module is where physics meets economics. Every survey is a purchase of
information, and the information must be specified before it is bought: what target,
what property contrast, what depth, what resolution, what noise, what cost. The five
lessons move from that specification, through the geometry and sampling that
determine what is even representable in the data, to the positioning and quality
control that determine whether the recorded numbers mean what they claim.

The two features that distinguish this module:

- **Sampling is the subject, not a preliminary.** The Nyquist condition is derived,
  and then its *consequence* is demonstrated: a spatial alias is an exact
  substitution, not a distortion, and it cannot be removed afterwards by any
  processing. The demonstration measures a 100 m anomaly reported as a 150 m
  anomaly, with both a 100 m and a 150 m sinusoid fitting the same ten samples to
  within $10^{-15}$.
- **Every claim is computed.** All fourteen numbers quoted in the lessons come from
  runnable scripts with stated *SYNTHETIC* parameters, including the cases where the
  honest answer is that a target is not detectable.

## Learning objectives

By the end of this module you will be able to:

1. **Write** a survey objective as a falsifiable target statement and **compute**
   whether the target is detectable above a stated noise level.
2. **Derive** the fold of a split spread, **measure** it on a generated geometry, and
   state what fold does and does not buy.
3. **Derive** the spatial Nyquist condition and the folding formula, and **predict**
   the apparent wavelength that a coarse survey will report.
4. **Convert** a positioning accuracy into an anomaly error for gravity and for
   magnetics, and identify which term binds.
5. **Construct** a noise budget, identify its binding term, and **measure**
   repeatability, drift and loop closures.
6. **Decide** honestly when a target is not detectable by a proposed design, and say
   what would need to change.

## Lessons

| # | Lesson | Level | Key measured result |
|---|---|---|---|
| 01 | [Survey Planning: Objectives, Target Resolution, Budget](./01-survey-planning.md) | advanced | a 50 m, 1000 kg m⁻³ sphere at 300 m gives 0.03883 mGal, SNR 3.88 at $\sigma = 0.010$ mGal; a 100 kg m⁻³ body at 700 m gives 0.00571 mGal, SNR 0.57 — **not detectable** |
| 02 | [Array Geometry, Fold, Offsets and Spatial Sampling](./02-geometry-and-coverage.md) | advanced | fold = $N/2$ measured for $N$ = 24–192; 79.2 % of bins at full fold with a 925 m ramp per end; two equal point masses merge below $s_{\text{crit}} = h$ (measured 301.06 m at $h = 300$ m) |
| 03 | [Spatial Sampling, Wavenumber Aliasing and Reconstruction](./03-spatial-sampling-theory.md) | graduate | a 100 m wavelength sampled at 60 m is reported as **150.000 m**, with a fit residual of $7.1\times10^{-16}$; the true wavenumber lies outside the representable band by a factor 1.2 |
| 04 | [Positioning with GNSS/DGPS and Static Corrections](./04-positioning-gnss.md) | intermediate | the free-air gradient derived as $2g/a$ = **0.30785 mGal/m**; 0.5 m of height error = 0.154 mGal; the maximum horizontal gradient is $0.8587\,g^{\max}/h$ |
| 05 | [Acquisition QC: Noise Tests, Repeatability, Metadata](./05-quality-control.md) | advanced | a budget of 0.1642 mGal with the positioning term carrying **87.9 %** of the variance; raw repeatability 0.43096 mGal falling to 0.01262 mGal after drift removal; loop residual $\sigma_c/\sqrt{m}$ |

## Suggested path

**If you are new to survey design:** read 01 → 03 → 02 → 04 → 05. The sampling
lesson (03) is placed before geometry (02) deliberately, because the aliasing limit
is the constraint that all geometry choices are made against.

**If you have a seismic background:** start with 03 and 02, then 01; the potential-field
material in 04 and 05 is where the unfamiliar arithmetic lives.

**If you have a potential-field background:** start with 01 and 04; the free-air
gradient derivation and the vertical-versus-horizontal comparison are the numbers
most often mis-stated in the literature.

**If you want the hard part first:** attempt ★★★10–12 of
[03](./exercises/03-spatial-sampling-theory-exercises.md) and ★★★10–12 of
[01](./exercises/01-survey-planning-exercises.md). If those come out cleanly, use the
other lessons as reference.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-survey-planning.md`](./01-survey-planning.md) … [`05-quality-control.md`](./05-quality-control.md) | The five lessons |
| [`exercises/01-survey-planning-exercises.md`](./exercises/01-survey-planning-exercises.md), [solutions](./exercises/01-survey-planning-solutions.md) | Detectability arithmetic, the depth penalty, station counting and cost |
| [`exercises/02-geometry-and-coverage-exercises.md`](./exercises/02-geometry-and-coverage-exercises.md), [solutions](./exercises/02-geometry-and-coverage-solutions.md) | Fold derivation, the end taper, the Fresnel zone, the two-body limit |
| [`exercises/03-spatial-sampling-theory-exercises.md`](./exercises/03-spatial-sampling-theory-exercises.md), [solutions](./exercises/03-spatial-sampling-theory-solutions.md) | Folding arithmetic, anisotropic sampling, reconstruction and its limits |
| [`exercises/04-positioning-gnss-exercises.md`](./exercises/04-positioning-gnss-exercises.md), [solutions](./exercises/04-positioning-gnss-solutions.md) | Free-air conversion, the gradient rule, bias versus noise |
| [`exercises/05-quality-control-exercises.md`](./exercises/05-quality-control-exercises.md), [solutions](./exercises/05-quality-control-solutions.md) | Noise budgets, repeatability intervals, drift and loop closures |
| [`code/aliasing_demo.py`](./code/aliasing_demo.py) | The folding formula applied to a real grid; least-squares fits at both the true and the apparent wavelength; the spectrum of the sampled record |
| [`code/detectability_demo.py`](./code/detectability_demo.py) | Sphere anomalies versus noise; a simulated survey line with an estimated noise level; maximum detectable depth; the $\sqrt N$ law |
| [`code/geometry_fold_demo.py`](./code/geometry_fold_demo.py) | Fold measured by histogramming midpoints; the end taper; the Fresnel zone; the two-body separation limit and its analytic verification |
| [`code/positioning_error_demo.py`](./code/positioning_error_demo.py) | The free-air gradient derived, not remembered; vertical error to gravity error; measured horizontal gradients for gravity and magnetics |
| [`code/qc_noise_budget_demo.py`](./code/qc_noise_budget_demo.py) | Quadrature budget with variance shares; repeatability with drift; loop closures; measured $\sqrt N$ averaging |

Every script prints labelled results with units and exits zero under the project's
Python environment; each uses `np.random.default_rng(seed)` with the seed stated in
the file:

```text
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    05-core-geophysics/05-survey-design-and-acquisition/code/aliasing_demo.py
```

## Key results, with the numbers the demonstrations produce

| Result | Measured value |
|---|---|
| 50 m / 1000 kg m⁻³ sphere at 300 m | 0.03883 mGal, SNR 3.88 at $\sigma = 0.010$ mGal |
| 100 m / 100 kg m⁻³ body at 700 m | 0.00571 mGal, SNR 0.57 — **not detectable** |
| Maximum detectable depth, $R = 25, 50, 100$ m | 120.7, 341.3, 965.4 m at $3\sigma = 0.030$ mGal (ratios 2.83 = $2^{3/2}$) |
| Stacking: noise of an $N$-trace mean | 0.009880, 0.005016, 0.003304, 0.002029 for $N = 1, 4, 9, 25$ |
| Fold for $N = 24, 48, 96, 192$ | 12.0, 24.0, 48.0, 96.0 traces per bin — exactly $N/2$ |
| Fold taper | 185 of 891 bins below full fold; 925 m measured against 940 m predicted |
| Fresnel radius, $\lambda = 100$ m | 100.0, 158.1, 223.6, 316.2 m at $h = 200, 500, 1000, 2000$ m |
| Two-body critical separation | 301.06 m measured against $h = 300.00$ m analytic |
| Aliasing: 100 m sampled at 60 m | apparent wavelength 150.000 m, folded $k = -0.041888$ rad/m |
| Alias fit residual | $7.1\times10^{-16}$ at 150 m and $1.8\times10^{-16}$ at 100 m — both exact |
| Free-air gradient $2g/a$ | $3.0785\times10^{-6}$ s⁻² = 0.30785 mGal/m |
| Vertical error to gravity error | 0.0092 (0.03 m), 0.1539 (0.50 m), 0.9236 mGal (3.00 m) |
| Maximum horizontal gradient of a point-mass anomaly | $0.8587\,g^{\max}/h$ at $x = h/2$; measured 0.00089 mGal/m for $R = 50$ m, $h = 150$ m |
| Magnetic dipole gradients | 2742.8, 33.9, 0.3 nT/m at 10, 30, 100 m depth |
| Noise budget | total 0.1642 mGal; positioning term 87.9 % of the variance |
| Drift | 0.43096 mGal raw repeatability falling to 0.01262 mGal after correction; rate recovered as 0.02987 against 0.03000 mGal/min |
| Loop closure residual | 0.00505 mGal measured against $\sigma_c/\sqrt m = 0.00348$ mGal |

## Notation

| Symbol | Meaning |
|---|---|
| $\Delta x$ | station, receiver or grid spacing, m |
| $\Delta s$ | shot interval, m |
| $b$ | CMP bin width, m |
| $N$ | number of live channels (or of repeats, where stated) |
| $k$, $k_N$ | wavenumber and its Nyquist value, rad m⁻¹; $k_N = \pi/\Delta x$ |
| $\lambda$, $\lambda_N$ | wavelength and its Nyquist value, m; $\lambda_N = 2\Delta x$ |
| $R$, $h$ | target radius and depth to its centre, m |
| $\Delta\rho$, $\Delta\chi$ | density and susceptibility contrast |
| $\sigma$ | noise standard deviation, in the field's unit |
| $g_z^{\max}$ | peak vertical gravity anomaly, mGal or m s⁻² |
| $r_F$ | Fresnel-zone radius, m |
| $\dot d$, $T$ | drift rate and loop duration |
| $m$ | number of drift loops |
| $a$, $g$ | Earth radius (m) and gravity (m s⁻²); $2g/a$ is the free-air gradient |

Constants: $G = 6.67430\times10^{-11}\ \mathrm{m^{3}kg^{-1}s^{-2}}$ (CODATA 2018,
**measured**, relative standard uncertainty $2.2\times10^{-5}$);
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ (**defining**);
$\mu_0/4\pi = 10^{-7}$ T m A⁻¹ (**defining**);
$g = 9.80665\ \mathrm{m\,s^{-2}}$ (the standard value, **defining**);
$a = 6371$ km (IUGG mean radius, **nominal**). Instrument accuracies, target
contrasts, noise levels and drift rates used in the demonstrations are **SYNTHETIC**
and labelled as such in the lessons; no instrument specification is quoted as fact.

## What this module deliberately does not do

- It does not develop the physics of the fields. Those are
  [02-physics/03](../../02-physics/03-oscillations-and-waves/README.md),
  [02-physics/04](../../02-physics/04-elasticity-and-continuum-mechanics/README.md),
  [02-physics/07](../../02-physics/07-electromagnetism/README.md) and
  [02-physics/08](../../02-physics/08-potential-theory/README.md).
- It does not cover instruments and their operation; that is
  [23-field-methods-instruments](../../23-field-methods-instruments/README.md).
- It does not process the data; that is the companion module
  [05-06 Data Processing Principles](../06-data-processing-principles/README.md).
- It does not treat the inverse problem; that is
  [18-inverse-problems](../../18-inverse-problems/README.md).
- It does not quote real survey results or instrument datasheets. Every number in
  the demonstrations is the output of the script that accompanies the lesson.
