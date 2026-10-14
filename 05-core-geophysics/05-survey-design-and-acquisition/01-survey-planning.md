---
id: 05-05-01
title: "Survey Planning: Objectives, Target Resolution, Budget"
level: advanced
prereqs: ["05-01-03", "05-03-02"]
tags: [survey-design, detectability, resolution, cost-benefit, acquisition]
---

# Survey Planning: Objectives, Target Resolution, Budget

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a survey objective as a falsifiable statement about a target:
   property contrast, size, depth, and the anomaly amplitude it implies.
2. **Distinguish** resolution, sampling, and depth of investigation, and explain
   why they are three different budgets rather than one.
3. **Compute** the detectability of a target by forward-modelling it, adding a
   stated noise level, and comparing the anomaly with that noise.
4. **Derive** the depth dependence of detectability, and use it to state the
   maximum depth at which a given body is visible at a given noise level.
5. **Convert** a resolution requirement into a station spacing and a station count,
   and a station count into a cost, and **identify** which constraint binds.
6. **Decide** honestly when the correct answer is "this target cannot be detected
   by this method", and report that answer.

## Prerequisites

- [05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off](../01-what-geophysics-measures/03-resolution-depth-tradeoff.md)
  — the qualitative version of Section 3.
- [05-03-02 Analytical Solutions for Simple Bodies](../03-forward-modelling-principles/02-analytical-solutions.md)
  — the sphere and point-mass formulae used throughout; this lesson does not
  re-derive them, it uses them.
- [02-01-02 Measurement Uncertainty](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
  — the standard deviation as the unit in which detectability is measured.

## 1. Intuition: a survey is a computation you do before spending money

A geophysical survey is a purchase. What you buy is **information about a
specific question**, at a price per station, and the purchase is irreversible once
the field crew has driven away. The planning question is therefore not "how many
stations can we afford?" but "what is the smallest survey that could answer this
question, and does that survey exist within the budget?"

That reframing is the whole content of this lesson. It has three consequences:

- **Depth of investigation and resolution are separate budgets.** Depth of
  investigation is set by physics and geometry — how fast the field of a deep
  source decays, how far a wave penetrates before it is absorbed. Resolution is
  set by the shortest wavelength that can be recorded without aliasing, which is
  set by station spacing and bandwidth. You can spend money on one without
  improving the other, and processing cannot make either better than acquisition
  made it.
- **Detectability is arithmetic, not intuition.** A target of stated size and
  property contrast at a stated depth produces an anomaly of computable amplitude.
  Either that amplitude exceeds the noise or it does not. Section 4 does this
  arithmetic, including a case where the answer is "no".
- **The cheapest survey that answers the question is the best survey.** Extra
  stations cost money and buy nothing if the question is already decided. The
  skill is knowing which constraint binds.

## 2. Precise definitions

### 2.1 The target statement

A survey objective is a tuple

$$T = \big(\Delta \rho\ \text{or}\ \Delta\chi\ \text{or}\ \Delta v,\; R,\; h,\; N\big)$$

giving the property contrast, the characteristic size $R$, the depth to the top
(or centre) $h$, and the number of such targets $N$. Without all four the
objective cannot be tested. "Look for mineralisation" is not an objective; "detect
a 50 m radius body with density contrast $1000\ \mathrm{kg\,m^{-3}}$ at 300 m
depth" is.

### 2.2 Resolution

**Resolution** is the smallest separation between two features that the data can
distinguish. It is limited by:

- the **station spacing** $\Delta x$, which sets the Nyquist wavenumber
  $k_N = \pi/\Delta x$ (developed in
  [05-05-03 Spatial Sampling, Wavenumber Aliasing and Reconstruction](./03-spatial-sampling-theory.md));
- the **source–receiver geometry and bandwidth** for wavefield methods;
- the **physics**, through the Fresnel zone or the natural width of the anomaly.

### 2.3 Depth of investigation

**Depth of investigation** is the greatest depth at which a source of stated
properties produces an anomaly of stated amplitude at the surface. It is a
property of the *pair* (method, target) and the noise, not of the instrument
alone. For a potential field whose source field decays as $r^{-n}$,

$$\text{anomaly amplitude} \propto h^{-n},$$

so depth of investigation is a statement about the noise floor and the target
size, never a fixed number of metres.

### 2.4 The sampling interval and Nyquist

The spatial sampling theorem states that a field containing wavenumbers up to
$k_{\max}$ can be reconstructed from samples spaced $\Delta x$ only if

$$k_{\max} \le k_N = \frac{\pi}{\Delta x}, \qquad \text{equivalently} \qquad
\lambda_{\min} \ge 2\,\Delta x .$$

A geologically required *resolution* $d$ therefore implies $\Delta x \le d/2$ at
the very least; in practice four to five stations across an anomaly are needed to
recognise its shape at all.

## 3. Derivation: detectability, and the square-of-depth penalty

### 3.1 The anomaly of a compact body

For a uniform sphere of density contrast $\Delta\rho$ and radius $R$ whose centre
lies at depth $h$, the field outside the sphere is exactly that of a point mass
$M = \tfrac{4}{3}\pi R^3 \Delta\rho$ at the centre. The peak vertical gravity
directly above it is

$$g_z^{\max} = \frac{G M}{h^{2}} = \frac{4\pi G R^{3}\Delta\rho}{3 h^{2}} .
\tag{1}$$

The dependence on $h$ is the crux, and it must be stated carefully because the
exponent depends on what is held fixed:

- **fixed mass** (raise the depth of an existing body): $g_z^{\max}\propto h^{-2}$;
- **fixed moment** of a magnetic dipole: $B^{\max}\propto h^{-3}$, which is why
  magnetic anomalies fall off faster with depth than gravity anomalies from the
  same geometry, and why shallow magnetic sources dominate a magnetic map;
- **fixed density contrast and fixed radius**: the mass is fixed, so $h^{-2}$ again.

The $h^{-3}$ magnetic case in section 5 of
[`code/positioning_error_demo.py`](./code/positioning_error_demo.py) shows the
consequence directly: a vertical dipole of moment $10^{5}\ \mathrm{A\,m^{2}}$ has a
peak anomaly of 20000 nT at 10 m depth but only 20.0 nT at 100 m depth, a factor
1000 for a factor 10 in depth.

### 3.2 Detectability

Let the measurement noise have standard deviation $\sigma$. Define the amplitude
signal-to-noise ratio

$$\mathrm{SNR} = \frac{g_z^{\max}}{\sigma} .
\tag{2}$$

A working criterion for a *detectable* anomaly is $\mathrm{SNR} \gtrsim 3$: an
anomaly must exceed three standard deviations of the noise to be distinguished
from it with any confidence. Setting $\mathrm{SNR} = 3$ and solving (1) for depth
gives the **maximum detectable depth**

$$h_{\max} = \sqrt{\frac{4\pi G R^{3}\Delta\rho}{3 \cdot 3\sigma}}
= \sqrt{\frac{4\pi G R^{3}\Delta\rho}{9\sigma}} .
\tag{3}$$

Two consequences follow directly and both are counter-intuitive:

- $h_{\max} \propto R^{3/2}$: doubling the target radius extends the detectable
  depth by a factor $2^{3/2} = 2.83$.
- $h_{\max} \propto \sigma^{-1/2}$: to double the detectable depth you must reduce
  the noise by a factor of **four**. This is the quantitative reason why
  instrument improvement and careful field procedures matter so much: the depth
  reach responds to the square root of the noise.

### 3.3 Worked example: three targets, one noise level

Take a synthetic instrument of repeatability $\sigma = 0.010$ mGal — a
*SYNTHETIC* value chosen to represent a 0.01 mGal-class relative gravimeter, not a
quoted specification. The detection threshold is therefore $3\sigma = 0.030$ mGal.

| target | $\Delta\rho$ (kg m⁻³) | $R$ (m) | $h$ (m) | $g_z^{\max}$ (mGal) | SNR | detectable? |
|---|---|---|---|---|---|---|
| large massive orebody | 1000 | 50 | 200 | 0.08737 | 8.74 | yes |
| modest massive body | 1000 | 50 | 300 | 0.03883 | 3.88 | yes, marginally |
| deep host-rock variation | 100 | 100 | 700 | 0.00571 | 0.57 | **no** |
| small deep body | 200 | 20 | 500 | 0.00018 | 0.02 | **no** |

All four columns of amplitudes are computed by
[`code/detectability_demo.py`](./code/detectability_demo.py) from equation (1);
they are not estimated. Note the third row: a body of 100 m radius has *more*
mass than the 50 m orebody, but its density contrast is ten times smaller and it
is 400 m deeper, and it is invisible.

The maximum detectable depth from equation (3) is

| $R$ (m) | $h_{\max}$ (m) at $3\sigma = 0.030$ mGal |
|---|---|
| 25 | 120.7 |
| 50 | 341.3 |
| 100 | 965.4 |

The ratio $965.4/341.3 = 2.83$ is exactly $2^{3/2}$, as the derivation predicts.

### 3.4 A simulated survey line, and a detection verdict

Detection in practice is done on a profile, not at a point. The demo models 41
stations at 30 m spacing over the "modest massive body", adds Gaussian noise at
$\sigma = 0.010$ mGal, and estimates the noise from the quiet ends of the line
rather than assuming it:

| quantity | measured |
|---|---|
| forward-model peak (noise-free) | 0.03883 mGal |
| maximum of the noisy line | 0.05146 mGal |
| background standard deviation (quiet ends) | 0.01086 mGal |
| measured peak / measured noise | 4.74 |
| verdict | **DETECTABLE** |

The measured SNR of 4.74 exceeds the input 3.88 because the noise realisation
happened to add to the peak. A single realisation can overstate a marginal
detection by 20 % or more; that is why a detection claim should quote the
*modelled* amplitude against the *estimated* noise, not the maximum of one noisy
line. Section 5 of the demo quantifies the alternative, which is legitimate:
repeat the line and average.

## 4. Resolution, sampling and depth are three budgets

| Budget | Set by | Bought with | Not fixable by processing |
|---|---|---|---|
| Depth of investigation | source strength, depth, noise | a method with slower decay, or lower noise | yes — no operator recovers a signal below the noise |
| Resolution | station spacing, bandwidth, geometry | more stations, higher frequencies | yes — see the aliasing demonstration in 05-05-03 |
| Shape / interpretability | number of samples across the anomaly | station count inside the anomaly footprint | yes — a three-sample anomaly has no distinguishable shape |

A useful planning rule that follows from Section 3.1: the anomaly half-width of a
compact body is of order its depth. A body with centre at depth $h$ produces a
field that is essentially flat over a radius $\sim h$ and falls off outside it. To
characterise it, sample the anomaly at

$$\Delta x \le \frac{h}{4}
\tag{4}$$

so that at least eight stations lie across the anomaly. For the 300 m target above
that gives $\Delta x \le 75$ m, and the demo used 30 m — deliberately finer than
required, because the same line was also asked to resolve whether the body was a
sphere or a dyke. **The sampling requirement follows from the *interpretation*
question, not from the detection question.** Detection needs a handful of samples;
shape needs many.

The same rule applies to a wavefield method, but the physical length scale is the
Fresnel-zone radius rather than the measurement grid: the horizontal resolution of
a surface-seismic image of a reflector at depth $h$ with dominant wavelength
$\lambda$ is

$$r_F = \sqrt{\frac{\lambda h}{2}} .
\tag{5}$$

For $\lambda = 100$ m (a 25 Hz event at 2500 m/s; *SYNTHETIC*) the demo measures
$r_F = 158$ m at $h = 500$ m and $r_F = 316$ m at $h = 2000$ m. Resolution
degrades as $\sqrt{h}$ — more slowly than the $h^{-2}$ amplitude decay of a
potential field, which is why seismic penetrates much deeper than gravity while
retaining useful resolution, and why gravity is used for regional structure rather
than for thin targets at depth.

## 5. Geometry and coverage in one page

The third leg of the plan is the geometry: what the sources and receivers do, which
the next lesson develops in full
([05-05-02 Array Geometry, Fold, Offsets and Spatial Sampling](./02-geometry-and-coverage.md)).
At planning level, three numbers must be decided together:

- the **maximum offset** (or source–receiver distance), which controls whether a
  target at depth $h$ can be illuminated at all;
- the **fold**, the number of independent measurements contributing to one
  estimate, which controls the noise and hence the detectability;
- the **bin size**, the size of the cell into which measurements are gathered,
  which controls the aliasing limit.

The demo measures these on a split-spread geometry: with $N$ live channels the
fold is $N/2$ traces per bin, the maximum offset is $N \Delta x / 2$, and the fold
ramps from zero at the ends of the line to full over a distance of half the spread
length. Measured values for the standard configuration (20 m receiver interval,
400 shots):

| channels $N$ | max offset (m) | fold (traces/bin) |
|---|---|---|
| 24 | 230 | 12.0 |
| 48 | 470 | 24.0 |
| 96 | 950 | 48.0 |
| 192 | 1910 | 96.0 |

Note what this table says about the budget: fold and maximum offset are **not
independent knobs**. Both grow linearly with the channel count, so buying a deeper
target (larger maximum offset) buys noise rejection (higher fold) as a side effect
and doubles the acquisition cost per shot. On the 96-channel example the measured
fold profile has 706 of 891 bins at full fold (79.2 %), with 185 bins (92.5 per
end) below full fold, spanning a measured 925 m of the midpoint axis against a
predicted ramp length of $N\Delta x/2 - \Delta s = 940$ m. **The ends of a profile
are always worse than the middle**, and that must be in the plan, not discovered
afterwards; the derivation of the fold formula is in
[05-05-02](./02-geometry-and-coverage.md).

## 6. Assumptions

State these explicitly in a survey plan; each is a place where the arithmetic above
can be wrong:

1. **The `3 sigma` detection threshold is a convention, not a theorem.** It gives
   a sensible false-alarm/omission balance for a single, isolated anomaly. For a
   survey of $10^{5}$ independent cells, a 3-sigma criterion will produce
   $\sim 2.7\times10^{3}$ false positives by chance alone; the multiplicity of the
   test must be accounted for, which is the subject of
   [01-13-08 Hypothesis Testing, p-Values and Power](../../01-mathematics/13-probability-and-statistics-foundations/08-hypothesis-testing.md).
2. **The noise is additive, independent and Gaussian.** Real field noise is
   correlated over hundreds of metres (cultural noise, topography, near-surface
   variation), which reduces the effective number of independent samples and can
   mimic an anomaly far larger than the point noise level.
3. **The target is isolated.** Two bodies closer than about one body depth merge
   into a single anomaly: the geometry demo measures a critical separation
   $s_{\text{crit}} = h$ for two equal point masses, i.e. bodies separated by less
   than one depth cannot be resolved into a pair at all.
4. **The model class is right.** The point-mass formula assumes a compact,
   uniform, roughly equant body. A tabular body of the same mass at the same depth
   gives a *different* amplitude and a very different profile.
5. **The instrument behaves as specified over the whole survey.** Drift,
   coupling and temperature effects grow with survey duration; the plan must
   include the base-station repetition needed to control them, quantified in
   [05-05-05 Acquisition QC](./05-quality-control.md).

## 7. Units and dimensional analysis

Equation (1) in SI:

$$[G][M][h^{-2}] = \mathrm{m^{3}kg^{-1}s^{-2}} \cdot \mathrm{kg} \cdot \mathrm{m^{-2}}
= \mathrm{m\,s^{-2}},$$

which is an acceleration. Converting to the field unit

$$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$$

so a $3.883\times10^{-7}\ \mathrm{m\,s^{-2}}$ anomaly is $0.03883$ mGal. Note that
equation (3) inherits units

$$[h_{\max}] = \left( \frac{\mathrm{m^3kg^{-1}s^{-2}\cdot m^3 \cdot kg\,m^{-3}}}
{\mathrm{m\,s^{-2}}} \right)^{1/2} = \mathrm{m},$$

as required — the internal check that the expression has not picked up a stray
factor. Equation (5) likewise:

$$[\sqrt{\lambda h}] = \sqrt{\mathrm{m \cdot m}} = \mathrm{m}.$$

## 8. Python demonstration

[`code/detectability_demo.py`](./code/detectability_demo.py) computes everything in
Sections 3.3–3.4. The core is the detectability calculation, in five lines:

```python
G, MGAL = 6.67430e-11, 1.0e-5          # m^3 kg^-1 s^-2 ; m s^-2 per mGal
mass = 4.0 / 3.0 * np.pi * radius**3 * drho
g_peak = G * mass / depth**2 / MGAL    # equation (1)
snr = g_peak / sigma                   # equation (2)
h_max = np.sqrt(G * mass / (3.0 * sigma * MGAL))    # equation (3)
```

Measured results, for $\sigma = 0.010$ mGal, are the tables in Section 3; the demo
also reports the repeat-stacking behaviour, which is the honest route to a
marginal target:

| repeats $N$ | measured $\sigma$ of the mean (mGal) | $1/\sqrt{N}$ prediction |
|---|---|---|
| 1 | 0.009880 | 0.010000 |
| 4 | 0.005016 | 0.005000 |
| 9 | 0.003304 | 0.003333 |
| 16 | 0.002569 | 0.002500 |
| 25 | 0.002029 | 0.002000 |

(The single-realisation rows scatter by a few per cent around the prediction; the
scatter falls as the number of realisations rises, which the demo does not
belabour.) **Quartering the noise requires sixteen times the acquisition effort.**
That is the exchange rate of the entire discipline, and it should be quoted in
every survey plan that claims a marginal target.

## 9. Exercises, common mistakes, applications

Companion problem sets:
[`exercises/01-survey-planning-exercises.md`](./exercises/01-survey-planning-exercises.md)
and [`exercises/01-survey-planning-solutions.md`](./exercises/01-survey-planning-solutions.md).

### Common mistakes

1. **Quoting a "depth of investigation" for an instrument.** Depth of
   investigation belongs to a (method, target, noise) triple. A number without a
   target size is meaningless.
2. **Confusing resolution with accuracy.** A survey can locate a body's centre to
   a few metres and still be unable to say whether it is a sphere or a dyke.
3. **Planning to "fix it in processing".** Aliasing is not recoverable, and no
   filter restores signal below the noise; see Section 3 of
   [05-05-03](./03-spatial-sampling-theory.md).
4. **Ignoring the line ends.** The measured fold tapers over half a spread length
   at each end; targets within that taper are under-sampled by design.
5. **Reporting a detection from the maximum of a noisy profile.** The maximum of
   the noise over 41 stations is already about $2\sigma$; a claimed anomaly must
   be compared with an estimated noise level, ideally from repeats.

### Real-world applications

- **Mineral exploration targeting.** The calculation in Section 3.3 is the
  standard "does the orebody show up?" test. A body that fails it is not a
  geophysical target, whatever its economic value; the correct report says so.
- **Groundwater and environmental surveys.** Shallow targets have small depth and
  small contrast; the binding constraint is usually cultural noise and
  near-surface heterogeneity rather than instrument resolution.
- **Engineering and cavity detection.** Here resolution is the requirement and
  depth is small, so the survey is designed around the smallest feature, not the
  deepest.
- **Regional gravity and magnetics.** Large station spacing is acceptable because
  the targets are large and deep, and the noise per station can be reduced by
  long occupation times at a small number of stations.

## 10. Further reading

- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** Chapters 1–2 (the planning
  and detectability discussion) and Chapter 6 (gravity interpretation). Level:
  intermediate to advanced. The standard reference for the feasibility arithmetic
  in Section 3.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*. Cambridge University Press.** Chapter 9 on the practical
  resolution and depth questions. Level: advanced.
- **Kearey, P., Brooks, M., & Hill, I. (2002). *An Introduction to Geophysical
  Exploration* (3rd ed.). Blackwell.** Chapters 2–3. Level: introductory, useful
  for the vocabulary of survey design.
- **USGS, *Gravity and Magnetic Surveys* programme pages** —
  <https://www.usgs.gov> : general survey practice and data availability. (The
  USGS main site blocks automated requests; open it in a browser.)
- **NOAA National Geophysical Data Center (now NCEI)** —
  <https://www.ngdc.noaa.gov/mgg/gravity/> : global gravity data compilations,
  useful for regional planning and for testing planned filter parameters on real
  spectra before mobilisation.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text, and you should
> confirm current availability and editions through your library before citing them.

## 11. Related lessons

- [05-05-02 Array Geometry, Fold, Offsets and Spatial Sampling](./02-geometry-and-coverage.md) — the geometry leg of the plan.
- [05-05-03 Spatial Sampling, Wavenumber Aliasing and Reconstruction](./03-spatial-sampling-theory.md) — why the station spacing is a hard limit.
- [05-05-05 Acquisition QC](./05-quality-control.md) — how the noise level assumed here is measured in the field.
- [05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off](../01-what-geophysics-measures/03-resolution-depth-tradeoff.md) — the qualitative companion.
- [05-03-02 Analytical Solutions for Simple Bodies](../03-forward-modelling-principles/02-analytical-solutions.md) — where the sphere formula comes from.
- [18-01-01 Forward vs Inverse Problems and the Practical Asymmetry](../../18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md) — why the forward problem here is easy and the inverse will not be.

## 12. Self-assessment checklist

- [ ] I can write a target statement containing contrast, size and depth.
- [ ] I can compute the peak anomaly of a sphere from $\Delta\rho$, $R$ and $h$.
- [ ] I can state and justify the $3\sigma$ detection criterion, and its limits.
- [ ] I can derive $h_{\max} \propto \sigma^{-1/2}$ and explain the practical consequence.
- [ ] I can convert a resolution requirement into a station spacing, and say why
      four to five samples across an anomaly is the minimum for shape.
- [ ] I can explain why resolution, sampling and depth of investigation are
      separate budgets.
- [ ] I can state the assumptions behind my detectability estimate.
- [ ] I can describe a case in which the correct answer is "not detectable".
