---
id: 15-04-03
title: "Marine Minerals and Deep-Sea Mining Geophysics"
level: doctoral
prereqs: ["15-04-01", "15-02-05", "09-01-01", "21-02-01"]
tags: [oceanography, marine-geophysics, seafloor-mapping, marine-minerals, geostatistics, electromagnetics]
---

# Marine Minerals and Deep-Sea Mining Geophysics

> **All models and data in this module are SYNTHETIC.** The deposit, the
> abundance field and the grades are teaching models with stated model constants.
> No real mine site, licence area, deposit, cruise or survey is referenced, and no
> number is quoted from a published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the gravity and magnetic anomaly of a model massive-sulphide body
   and **state**, with numbers, why neither can detect it.
2. **Compute** the skin depth of seawater and of a conductive crust, and
   **demonstrate** why marine electromagnetics must be towed near the seafloor.
3. **Estimate** a depth of investigation for a stated target response and noise
   level, and **state** the assumptions that make it an order-of-magnitude
   estimate rather than a resolution.
4. **Fit** an exponential variogram to a sampled abundance field, **compare** the
   fitted parameters with the truth, and **quantify** the estimator variance
   against sampling density.
5. **Perform** ordinary kriging and **compare** the kriging standard deviation
   with the measured error, and **explain** the difference.
6. **Design** a sampling programme for an area-mean estimate and **demonstrate**
   that beyond a certain density more samples of the same area cannot improve it.
7. **Compute** a tonnage and contained-metal estimate, and **rank** the
   parameters that dominate its uncertainty.

## Prerequisites

- [15-04-01 Benthic Habitat Mapping and Classification](01-habitat-mapping.md) —
  the seafloor mapping frame that any mineral survey starts from.
- [15-02-05 Marine Gravity and Magnetic Surveys](../02-marine-geophysics-methods/05-marine-gravity-magnetics.md) —
  the potential-field data used in §3.1.
- [09-01-01 Electrical Properties of the Earth](../../09-electrical-em-methods/01-electrical-properties-of-earth/README.md) —
  conductivity, resistivity and the skin depth.
- [21-02-01 Regionalised Variables](../../21-statistics-bayesian-ml/02-geostatistics/01-regionalized-variables.md) —
  variograms, kriging and the geostatistical vocabulary.

## 1. Intuition: the target is tiny and the environment is loud

Deep-sea mineral deposits come in four broad forms — seafloor massive sulphides
at hydrothermal vents, polymetallic nodules lying on abyssal plains, cobalt-rich
ferromanganese crusts on seamounts, and rare-earth-rich muds. Their geophysics is
defined by one brutal fact: **the deposit is small compared with everything
around it.**

A model massive-sulphide mound 200 m across at 1 km depth produces a gravity
anomaly of 0.04 mGal and a magnetic anomaly of 0.8 nT. A survey measures gravity
to a few tenths of a mGal and magnetics to a few nT. The deposit is invisible.
What the geophysics maps is the **setting**: the volcanic ridge that hosts the
vents, the alteration that changes density and magnetisation over kilometres, the
sediment cover, and the crustal structure. That setting then constrains where a
deposit could be — a prospectivity argument, not a detection.

Nodules are the opposite problem. They are everywhere on the abyssal plain, so
detection is easy and *quantification* is the difficulty. Abundance varies at
scales of hundreds of metres to kilometres, and the resource arithmetic multiplies
that abundance by an area — so the uncertainty is a geostatistical question, and
this lesson shows that the naive sample-count formula is optimistic by a factor of
five to nine.

Electromagnetics sits between the two. A sulphide body is a good conductor in a
resistive crust, which is exactly the contrast a marine EM system wants. The
problem is the 2 km of conductive seawater in the way: at 1 Hz the field is
attenuated by 69 dB on the way down, so the system must be towed close to the
seafloor, and then the *frequency* that reaches depth is too low to resolve much.
§3.2 quantifies both halves of that squeeze.

## 2. Precise definitions

**Seafloor massive sulphide (SMS)**: a hydrothermal precipitate, typically
metres to tens of metres thick and tens to hundreds of metres across, with high
density and high conductivity relative to the surrounding basalt.

**Polymetallic nodule**: a concentric ferromanganese concretion, a few centimetres
in diameter, lying on the sediment surface; quantified as **abundance**
($\mathrm{kg\,m^{-2}}$, wet) and metal grades.

**Cobalt-rich crust**: a ferromanganese pavement on rock substrate, millimetres
to tens of centimetres thick, whose resource is an *area × thickness × grade*
problem like the nodules but with a much thinner, harder-to-measure layer.

**Skin depth** $\delta$: the depth over which a plane wave's amplitude falls by
$1/e$ in a conductor, $\delta=\sqrt{2/(\omega\mu_0\sigma})=503.29\sqrt{\rho/f}$
for $\rho$ in $\Omega\,\mathrm{m}$ and $f$ in Hz.

**Variogram** $\gamma(h)$: half the expected squared difference of the variable
at two points separated by $h$. The exponential model
$\gamma(h)=C_0+(C-C_0)(1-e^{-h/L})$ has a **nugget** $C_0$, a **partial sill**
$C-C_0$ and a **range** $L$ (the practical correlation length).

**Kriging**: best linear unbiased prediction of a variable at an unsampled
location, which returns both an estimate and a **kriging variance** derived from
the fitted variogram.

**Coefficient of variation** $\mathrm{cv}=\sigma/\bar x$: the dimensionless
measure that turns a required relative error into a required sample count.

## 3. Derivations and measurements

### 3.1 The scale of the anomalies

For a buried sphere of radius $a$, depth $z$ and density contrast $\Delta\rho$,
the maximum vertical gravity anomaly is

$$g_{\max}=\frac{4}{3}\pi G\Delta\rho\frac{a^{3}}{z^{2}} .$$

With $\Delta\rho=1500\ \mathrm{kg\,m^{-3}}$ (sulphide against basalt),
$a=100\ \mathrm{m}$, $z=1000\ \mathrm{m}$ and $G=6.67430\times10^{-11}\
\mathrm{m^{3}\,kg^{-1}\,s^{-2}}$:

$$g_{\max}=4.194\times10^{-7}\ \mathrm{m\,s^{-2}}=0.0419\ \mathrm{mGal},$$

using the exact $1\ \mathrm{mGal}=10^{-5}\ \mathrm{m\,s^{-2}}$. For scale, a flat
layer of the same contrast contributes
$2\pi G\Delta\rho t$, i.e. $0.629\ \mathrm{mGal}$ per $10\ \mathrm{m}$ of
thickness, $3.145$ per 50 m and $31.45$ per 500 m.

**The conclusion is a design statement**: a body 200 m across at 1 km depth
cannot be detected, while a few tens of metres of contrasting *layer* anywhere in
the survey area is unmissable. Potential-field surveys for SMS are therefore
setting-mapping tools.

The magnetic equivalent for a dipole moment $m$ at distance $r$ is
$B=\mu_0m/(4\pi r^{3})$ (equatorial), with $m=JV$. With $J=2.0\ \mathrm{A\,m^{-1}}$
and $V=(4/3)\pi(100)^{3}=4.189\times10^{6}\ \mathrm{m^{3}}$,
$m=8.378\times10^{6}\ \mathrm{A\,m^{2}}$ and

$$B=\frac{4\pi\times10^{-7}\times8.378\times10^{6}}{4\pi\times10^{9}}
=8.4\times10^{-10}\ \mathrm{T}=0.84\ \mathrm{nT}$$

equatorially, and twice that on axis. A 1 nT anomaly is at the edge of what a
careful marine magnetometer survey resolves, and this is a *200 m* body.

### 3.2 The electromagnetic squeeze

Skin depths, from $\delta=503.29\sqrt{\rho/f}$:

| $f$ (Hz) | $\delta$ in seawater ($0.25\ \Omega\,\mathrm{m}$) | $\delta$ in crust ($1\ \Omega\,\mathrm{m}$) |
|---|---|---|
| 0.1 | 795.8 m | 1591.5 m |
| 1 | 251.6 m | 503.3 m |
| 10 | 79.6 m | 159.2 m |
| 100 | 25.2 m | 50.3 m |

A plane wave from a surface source to a seafloor receiver is attenuated by
$20\log_{10}e^{-h/\delta}$ decibels. At 1 Hz over 2000 m of water that is

$$20\log_{10}\left(e^{-2000/251.6}\right)=-69.0\ \mathrm{dB},$$

a factor $3.5\times10^{-4}$: the field that reaches the seafloor is a
thousandth of what a surface system would need to see a target response.

To keep the water-column loss under 1% (20 dB) the frequency must fall to

$$f=\left(\frac{503.29\sqrt{0.25}}{2000/\ln 100}\right)^{2}=0.336\ \mathrm{Hz},$$

at which the skin depth in a $1\ \Omega\,\mathrm{m}$ crust is 869 m — the system
reaches the seafloor but resolves nothing beneath it. **The squeeze is the whole
argument for deep-towed EM**: at 50 m above the seafloor the loss at 1 Hz is
$-1.7\ \mathrm{dB}$ instead of $-69.0\ \mathrm{dB}$, a factor of
$10^{(69.0-1.7)/20}\approx2\times10^{3}$ more signal.

A depth-of-investigation estimate for a target whose response decays as
$e^{-z/\delta}$ against a noise floor of 5% of the primary is
$z_{\max}=\delta\ln 20$:

| $f$ (Hz) | $\delta$ (1 Ω·m) | $z_{\max}$ (m) |
|---|---|---|
| 0.1 | 1591.5 | 4768 |
| 1 | 503.3 | 1508 |
| 10 | 159.2 | 477 |
| 100 | 50.3 | 151 |

**Read this table as the honest limit**: even at 0.1 Hz the number is thousands of
metres only because the model ignores the frequency dependence of the *target*
contrast and treats the response as a pure diffusion decay. It gives an order of
magnitude for the depth, not a resolution.

### 3.3 Variogram, kriging and the sampling question

The demonstration generates a $20\times20\ \mathrm{km}$ abundance field with an
exponential covariance ($L=2000$ m), a mean of $15.0\ \mathrm{kg\,m^{-2}}$, a
field standard deviation of $4.00\ \mathrm{kg\,m^{-2}}$ and an added nugget of
$1.50\ \mathrm{kg\,m^{-2}}$. Sampling it on a 1 km grid (400 samples) and fitting
the exponential variogram gives

$$\hat C_0=0.00,\qquad \hat C-\hat C_0=18.57\ (\mathrm{kg\,m^{-2}})^{2},\qquad
\hat L=1656\ \mathrm{m},$$

against the true values $C_0=2.25$, $C-C_0=16.00$ and $L=2000$ m. The nugget is
driven to zero because the shortest lag with enough pairs is 250 m: **a nugget
smaller than the correlation at the shortest usable lag is not identifiable.**

Repeating the estimation with five field realisations at each sampling density:

| spacing (m) | samples | mean fitted range (m) | sd of range (m) |
|---|---|---|---|
| 500 | 1600 | 2491 | 1225 |
| 1000 | 400 | 1821 | 671 |
| 2000 | 100 | 2485 | 2862 |
| 4000 | 25 | 2247 | 2272 |

The mean is roughly right in every case and the *scatter* is the estimator's
problem: with 25 samples the fitted range is uncertain by a factor of two, and
**every kriging number built on it inherits that factor.** This is the weakest
link in the whole workflow, not the kriging algebra.

Kriging 60 validation cells with the fitted parameters gives an RMS error of
$5.30\ \mathrm{kg\,m^{-2}}$ against a mean kriging standard deviation of
$2.66\ \mathrm{kg\,m^{-2}}$ — a ratio of **1.99**. The kriging variance
*understates* the true error by a factor of two, and the reason is checkable: the
fitted range (1656 m) is 17% shorter than the truth, so the kriging over-weights
nearby samples and reports a confidence it does not have.

### 3.4 The area mean, and why more samples of the same area stop helping

Monte-Carlo over 25 realisations, sampling a regular grid and estimating the mean
of the whole 400 km² area:

| spacing (km) | samples | measured sd of the mean | naive $\sigma/\sqrt n$ | ratio |
|---|---|---|---|---|
| 0.5 | 1600 | 0.909 | 0.107 | 8.5 |
| 1.0 | 400 | 0.874 | 0.214 | 4.1 |
| 2.0 | 100 | 1.285 | 0.427 | 3.0 |
| 4.0 | 25 | 1.491 | 0.854 | 1.7 |
| 8.0 | 4 | 1.912 | 2.136 | 0.9 |

Two results matter.

1. For every spacing finer than the range, the naive independent-sample formula
   **understates the true error by a factor of 3 to 8.5.** Spatial correlation
   destroys the effective sample size, and a sample-count formula that ignores the
   variogram is wrong by nearly an order of magnitude.
2. The measured error **stops improving** below about 1 km spacing: 0.909 at
   0.5 km against 0.874 at 1 km. Beyond that point the residual error is the
   difference between *this area's* mean and the regional mean — a property of the
   realisation, not of the sampling. **No density of sampling within one area can
   remove it**; only sampling more areas can.

This is why the honest output of an abundance survey is an interval that includes
a between-area component of variance, which the within-area grid cannot
measure.

### 3.5 The resource arithmetic

With $A=400\ \mathrm{km^{2}}$, a sampled mean abundance of
$14.07\ \mathrm{kg\,m^{-2}}$ and grades of Ni 1.30% and Cu 1.10% (model values):

$$\text{tonnage}=A\times\text{abundance}
=4\times10^{8}\ \mathrm{m^{2}}\times14.07\ \mathrm{kg\,m^{-2}}
=5.63\times10^{6}\ \mathrm{t}=5.7\ \mathrm{Mt (wet)},$$

$$\text{contained Ni}=5.63\times10^{6}\times0.0130=7.3\times10^{4}\ \mathrm{t},
\qquad
\text{contained Cu}=6.2\times10^{4}\ \mathrm{t}.$$

Every factor is linear, so a factor of two in abundance, grade or area is a factor
of two in the metal. The sample-count table from
$n=(1.96\,\mathrm{cv}/\varepsilon)^{2}$:

| cv | $n$ for 10% | $n$ for 20% | $n$ for 30% |
|---|---|---|---|
| 0.2 | 16 | 4 | 2 |
| 0.5 | 97 | 25 | 11 |
| 1.0 | 385 | 97 | 43 |
| 1.5 | 865 | 217 | 97 |

With $\mathrm{cv}=0.5$ the formula asks for 97 samples for a 10% error — but §3.4
shows that the formula's model of the error is optimistic by a factor of 3–8 for
the *area mean*, so the honest answer is that 97 samples constrain the local
abundance, not the area mean to 10%.

## 4. Physical interpretation

- **Detection is a contrast problem and the contrasts are set by the setting.**
  SMS and crusts are small; nodules are ubiquitous; the geophysics differentiates
  the *host*, not the *ore*.
- **The seafloor is a conductor's worst neighbour.** Seawater is a better
  conductor than most rocks, so it shields everything below it; the deep tow is
  not a convenience, it is the enabling technology.
- **Frequency trades depth against resolution, and seawater fixes the exchange
  rate.** The ocean sets a ceiling on the usable frequency for a given altitude.
- **Abundance is a geostatistical variable with a long correlation length.**
  That is what makes the resource uncertainty large and the sample-count formula
  deceptive.
- **The nugget is the unresolvable part.** It bounds the confidence of any local
  estimate and it is the reason a kriging variance never reaches zero.
- **The area mean has a between-area component.** Two adjacent licence areas can
  differ by more than the sampling error of either, and no grid inside one can
  detect it.

## 5. Assumptions and regime of validity

1. **The sphere and slab formulas assume uniform density contrast.** Real
   sulphide mounds are layered, altered and irregular; the anomaly is a
   superposition, and the inversion is non-unique.
2. **Induced magnetisation with a stated intensity.** Remanent magnetisation can
   dominate in volcanic rocks, and its direction is unknown — an inferred
   magnetisation is a model.
3. **Plane-wave diffusion in a uniform half-space for the skin depth.** The
   target is a bounded conductor in a layered medium, so the true response is a
   scattering problem, not a diffusion decay.
4. **A stated noise floor.** The 5% used here is a model value; real noise from
   swell, navigation, altitude variation and system drift is much larger and
   strongly correlated with sea state.
5. **Second-order stationarity of the abundance field.** The variogram assumes a
   constant mean and variance over the area; a regional gradient or a change of
   sediment type violates it, and the fitted range then has no meaning.
6. **An exponential covariance model.** The structure may be better described by
   spherical or Matérn models, and the fitted range depends on the model form as
   well as on the data.
7. **Unbiased, noise-free samples.** Box-core abundance estimates have their own
   errors (washout, sub-sampling) that add to the nugget, and the sampling design
   is rarely random.
8. **No recovery or mining factors.** Tonnage in place is not a reserve, and for
   nodule mining the recovery, the sediment disturbance and the environmental
   constraints are all outside the geophysics.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| gravity anomaly | $g$ | $\mathrm{m\,s^{-2}}$ | 1 mGal $=10^{-5}$ exactly |
| magnetic field | $B$ | T | 1 nT $=10^{-9}$ T |
| density contrast | $\Delta\rho$ | $\mathrm{kg\,m^{-3}}$ | |
| magnetisation | $J$ | $\mathrm{A\,m^{-1}}$ | moment in $\mathrm{A\,m^{2}}$ |
| conductivity | $\sigma$ | $\mathrm{S\,m^{-1}}$ | $\rho=1/\sigma$ |
| skin depth | $\delta$ | m | $503.29\sqrt{\rho/f}$ |
| abundance | — | $\mathrm{kg\,m^{-2}}$ | wet |
| tonnage | — | t | $1\ \mathrm{t}=10^{3}$ kg |
| variogram | $\gamma$ | (units)² | nugget, sill, range |
| kriging variance | — | (units)² | compare with the measured RMS² |

The dimensional checks that matter: $g=4\pi G\Delta\rho a^{3}/(3z^{2})$ must come
out in $\mathrm{m\,s^{-2}}$ (it does: $\mathrm{m^3\,kg^{-1}\,s^{-2}}\times
\mathrm{kg\,m^{-3}}=\mathrm{s^{-2}}$, times $\mathrm{m^3/m^2}=\mathrm{m}$), and
$503.29\sqrt{\rho/f}$ must come out in metres, which fixes the constant: it is
$\sqrt{2/(\mu_0\omega)}$ evaluated in SI, not a fitted number.

## 7. Worked examples

All numbers are printed by `code/marine_minerals_demo.py`.

### Example 1 — the deposit is invisible

$$g_{\max}=\frac{4\pi}{3}\times6.67430\times10^{-11}\times1500\times
\frac{10^{6}}{10^{6}}=4.194\times10^{-7}\ \mathrm{m\,s^{-2}}
=0.0419\ \mathrm{mGal}.$$

The same contrast in a 10 m layer gives $2\pi G\Delta\rho t
=2\pi\times6.67430\times10^{-11}\times1500\times10=6.29\times10^{-6}\
\mathrm{m\,s^{-2}}=0.629\ \mathrm{mGal}$.

### Example 2 — the magnetic effect

$m=2.0\times4.189\times10^{6}=8.378\times10^{6}\ \mathrm{A\,m^{2}}$,
$B=10^{-7}\times8.378\times10^{6}/10^{9}=8.38\times10^{-10}\ \mathrm{T}
=0.84\ \mathrm{nT}$ equatorially.

### Example 3 — the EM squeeze

$\delta_{\text{seawater}}(1\ \mathrm{Hz})=503.29\sqrt{0.25}=251.6$ m; loss over
2000 m $=-69.0\ \mathrm{dB}$; at 0.336 Hz the loss falls to $-20$ dB but the
crustal skin depth rises to 869 m.

### Example 4 — the variogram

Fitted range 1656 m against a true 2000 m (−17%), fitted nugget 0.00 against a
true 2.25; kriging RMS 5.30 against a reported sd of 2.66. **All three
discrepancies point the same way**: a short fitted range makes the kriging
over-confident.

### Example 5 — the sample count

With $\mathrm{cv}=0.5$ and a 10% target, $n=(1.96\times0.5/0.10)^{2}=96.04$, i.e.
97 samples. The Monte-Carlo experiment says the achievable error for the area
mean with a 0.5 km grid (1600 samples) is 0.909 kg/m² = 6.5% of 15 — better than
10%, but only by 1.5× while the sample count rose by 16×. **Sampling returns
diminish harshly once the grid is finer than the range.**

### Example 6 — the resource

$A=400\ \mathrm{km^{2}}$, abundance $14.07\ \mathrm{kg\,m^{-2}}$:
$5.63\times10^{6}$ t wet, containing $7.3\times10^{4}$ t Ni and
$6.2\times10^{4}$ t Cu at the model grades. A ±20% abundance uncertainty (the
between-area component of §3.4 is already 6.5% at best) moves every figure by
±20%.

## 8. Python demonstration

`code/marine_minerals_demo.py` prints, with units:

1. the gravity and magnetic anomalies of a model deposit, beside the equivalent
   layer and a fine-scale survey-noise comparison
2. seawater skin depths, the water-column attenuation, the frequency that
   survives 2000 m, the gain from a deep tow, and a depth-of-investigation table;
3. the synthetic abundance field, the grid-sampled variogram with its fitted and
   true parameters, the estimator-variance table, the kriging validation and the
   area-mean Monte Carlo;
4. the tonnage, contained metal, sensitivity table and sample-count table;
5. the worked-example values of Section 7.

```bash
cd 15-oceanography-marine/04-seafloor-mapping-and-habitats/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python marine_minerals_demo.py
```

## 9. Exercises

[`exercises/03-marine-minerals-exercises.md`](./exercises/03-marine-minerals-exercises.md)
and
[`exercises/03-marine-minerals-solutions.md`](./exercises/03-marine-minerals-solutions.md).

## 10. Real-world applications

- **Licence-area assessment.** Resource statements for nodule and crust
  exploration are built from exactly this arithmetic and its uncertainty.
- **Environmental baseline and monitoring.** Abundance and sediment-plume
  measurements use the same geostatistics, with the same sample-count trap.
- **Hydrothermal exploration.** Plume and bathymetric surveys locate the *setting*;
  only drilling or a deep-towed EM/induced-polarisation survey tests the deposit
  ([15-03-01](../03-seafloor-tectonics/01-mid-ocean-ridges.md)).
- **EM system design.** Frequency, altitude and power budgets follow from §3.2
  ([15-02-07 Marine CSEM and EM](../02-marine-geophysics-methods/07-marine-csem-em.md)).
- **Any regional resource estimate.** The variogram-estimation and
  sampling-density lessons transfer directly to groundwater, mineral and
  geohazard mapping.

## 11. Further reading

- **Mavko, G., Mukerji, T., & Dvorkin, J., *The Rock Physics Handbook*, Cambridge
  University Press.** Level: research reference. The density and conductivity
  contrasts behind §3.1.
- **Deutsch, C. V., & Journel, A. G., *GSLIB: Geostatistical Software Library and
  User's Guide*, Oxford University Press.** Level: research reference. Variogram
  estimation, kriging and the practical sampling designs.
- **Chave, A. D., & Jones, A. G. (eds), *The Magnetotelluric Method*, Cambridge
  University Press.** Level: research monograph. Controlled-source and marine EM,
  including the seawater shielding problem.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint
- [ ] I can compute the gravity and magnetic anomaly of a model body and say
      whether a survey can detect it.
- [ ] I can compute a skin depth in water and rock and an attenuation in dB.
- [ ] I can compute the frequency that survives a water column and state what it
      costs in resolution.
- [ ] I can fit an exponential variogram and compare it with a known truth.
- [ ] I can perform ordinary kriging and validate its variance.
- [ ] I can explain why more samples of the same area stop helping.
- [ ] I can compute a tonnage, contained metal and the sample count for a target
      accuracy, and say which number is optimistic.
## Common pitfalls
1. **Reporting a deposit-scale anomaly as detectable.** 0.04 mGal and 0.84 nT are
   not measurements of the deposit.
2. **Using a surface-towed EM system and expecting sub-seafloor resolution.** The
   69 dB of water column decides the answer before the target does.
3. **Treating a skin depth as a resolution.** It is an attenuation length; a
   target can be detected at several skin depths and resolved at fractions of one.
4. **Fitting a variogram with too few pairs and quoting the range to three
   figures.** The estimator scatter is a factor of two at 25 samples.
5. **Trusting a kriging variance without validating it.** Here it understated the
   error by 2×.
6. **Using $\sigma/\sqrt n$ for a spatially correlated variable.** It understated
   the area-mean error by up to 8.5×.
7. **Sampling one area more densely to reduce the area-mean error.** Beyond the
   range, the limit is the between-area variance.
8. **Quoting tonnage as a reserve.** Recovery, processing and regulation are
   absent from the arithmetic.

## Related modules
- [15-04-01 Benthic Habitat Mapping and Classification](01-habitat-mapping.md) —
  the mapping products these resources are delineated on.
- [15-04-02 Gas Hydrates: Occurrence, Geophysics and Resource Potential](02-gas-hydrates.md) —
  the same resource arithmetic for a phase rather than an ore.
- [15-03-01 Mid-Ocean Ridges, Spreading Centres and Hydrothermal Systems](../03-seafloor-tectonics/01-mid-ocean-ridges.md) —
  the processes that create massive sulphides.
- [15-02-07 Marine CSEM and EM for Gas Hydrates](../02-marine-geophysics-methods/07-marine-csem-em.md) —
  the acquisition system whose depth of investigation is computed here.
- [21-02-01 Regionalised Variables](../../21-statistics-bayesian-ml/02-geostatistics/01-regionalized-variables.md) —
  the full geostatistical treatment.
- [21-06-06 Mineral Prospectivity with ML](../../21-statistics-bayesian-ml/06-ml-in-geophysics/06-mineral-prospectivity-ml.md) —
  where a setting map becomes a probability map.
