---
id: 06-05-03
title: "Attenuation Tomography and Temperature Interpretation"
level: doctoral
prereqs: ["06-05-01", "06-05-02", "06-06-02"]
tags: [seismology, attenuation, t-star, tomography, inversion, temperature, null-space]
---

# Attenuation Tomography and Temperature Interpretation

Attenuation tomography maps $Q^{-1}$ in the Earth from the frequency-dependent
decay of seismic amplitudes. Its appeal is direct: of all the quantities
seismology can image, $Q^{-1}$ is the one most tightly coupled to temperature and
to the presence of fluid or melt, so a $Q^{-1}$ map is the closest thing the
subject has to a thermometer at depth. Its difficulty is equally direct, and it
comes in three layers.

- The observable is a **product over the ray path**, so the inverse problem is
  a path integral with the same geometric smearing as travel-time tomography, but
  with a worse noise model because amplitudes are contaminated by everything the
  travel time is not.
- The amplitude of the **source** is unknown and trades off against path
  attenuation. That trade-off is not exact — it can be broken, but only weakly —
  and the demonstration measures exactly which directions of model space it
  leaves unconstrained.
- Even a perfect $Q^{-1}$ map is not a temperature map. Converting one to the
  other requires a creep law, an activation enthalpy, and a **frequency
  extrapolation of six or more decades** between the seismic band and the
  laboratory band.

This lesson does all three layers numerically and states at each step what is
measured, what is assumed, and what is unrecoverable.

All models and data in this module are **SYNTHETIC**. The tomographic model below
is a chosen teaching model, not an inversion of real data, and no observational
$Q$ or temperature is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** the linear attenuation-tomography problem, including the
   per-event amplitude terms, and **explain** why they must be inverted for
   jointly rather than removed.
2. **Compute** the null space of the joint Jacobian and **demonstrate**
   non-uniqueness by exhibiting two models that fit the data to machine
   precision while differing by a physically large amount.
3. **Distinguish** the exact null directions from the approximate
   source–amplitude trade-off, and **quantify** the latter with the singular
   values.
4. **Choose** a damping parameter against a stated noise level and **state** what
   the damping buys (stability) and what it costs (a smoothed, biased image).
5. **Compute** the precision of a $t^{*}$ measurement from its band and noise,
   and **design** a band for a target precision.
6. **Explain** why a constant-$Q$ model must be built from a finite absorption
   band, and **relate** the number of relaxations to the flatness achieved and to
   the modelling cost.
7. **Derive** the temperature sensitivity of an anelastic relaxation and
   **critique** the inference from a $Q$ anomaly to a temperature anomaly,
   naming at least four competing explanations and the measurement that
   discriminates each.

## Prerequisites

- [01 Measuring Q: Spectral Ratio, Rise Time, Multiple Methods](01-attenuation-measurement.md) —
  $Q$, $\alpha$, $t^{*}$ and the estimator errors.
- [02 Separating Scattering from Intrinsic Attenuation](02-scattering-vs-intrinsic.md) —
  why a measured $Q$ is an apparent $Q$.
- [06-06-02 Travel-Time Tomography: Parametrisation and Inversion](../06-seismic-tomography/02-travel-time-tomography.md) —
  the ray-path matrix and its inverse, which this lesson reuses with amplitudes.

## 1. The observable and the forward problem

Write the observed spectral amplitude of event $e$ at receiver $r$ and frequency
$f$ as

$$\ln A_{er}(f) = \ln S_e(f) + \ln G_{er} + \ln C_{r} - \pi f\, t^{*}_{er},$$

where $S_e$ is the event's source spectrum, $G_{er}$ the geometric spreading and
$C_r$ the receiver response. Group everything that is *flat in frequency* into a
single term $b_{er}$, and measure the decay **relative to a reference frequency**
$f_{\text{ref}}$:

$$\ln\frac{A_{er}(f)}{A_{er}(f_{\text{ref}})} = -\,\pi \left(f - f_{\text{ref}}\right) t^{*}_{er}.$$

This is why the observable of attenuation tomography is a *slope*, not an
amplitude: the flat term $b_{er}$ — source, spreading, site, instrument gain —
cancels from a relative measurement, and with it the largest systematic error in
the method. What remains is $t^{*}$, which is a path integral:

$$t^{*}_{er} = \int_{\text{ray}} \frac{\mathrm{d}l}{Q(\mathbf{x})\,v(\mathbf{x})}
= \sum_{c} G_{erc}\,\frac{1}{Q_{c}},
\qquad
G_{erc} = \int_{\text{ray } er \cap c} \frac{\mathrm{d}l}{v(\mathbf{x})},$$

i.e. the **time** spent by ray $er$ in cell $c$. The problem is therefore
*linear in $1/Q$* for fixed paths, with the same row structure as travel-time
tomography and, crucially, **no positivity or boundedness built in**: $1/Q < 0$
is unphysical but is a perfectly ordinary least-squares output.

In practice, and in the demonstration, one works directly with the
frequency-domain data rather than with fitted slopes, because the errors are
then explicit. The Jacobian row of ray $r$ (event $e$) at frequency $f$ is

$$\frac{\partial}{\partial (1/Q_c)} = -\pi f\, G_{erc}, \qquad
\frac{\partial}{\partial b_e} = 1,$$

using one amplitude term per event (any per-receiver terms are absorbed by
normalising each receiver to its own reference; the demonstration normalises per
event and per receiver pair, which is the standard interchangeability assumption
and is itself a model choice).

## 2. Why the source term must be inverted for jointly

Suppose $1/Q$ were increased uniformly by $\delta$. Every $t^{*}$ grows by
$\delta \tau_{\text{ray}}$ (the ray's travel time), so every $\ln A$ falls by
$\pi f \delta \tau_{\text{ray}}$. A per-event amplitude term can absorb *most* of
that, because a single event's rays have similar travel times: the term
$b_e \to b_e - \pi f \delta \bar{\tau}_e$ removes the common part. What is left
over is the *variation* of travel time within the event's ray fan, and that is a
real, physical, if weak, constraint.

Two consequences follow immediately, and they are the reason this lesson is
doctoral rather than graduate:

- the trade-off between a uniform $1/Q$ increase and the source amplitudes is
  **approximate, never exact** — the demonstration measures this;
- the directions in model space that it fails to constrain are the
  **smallest singular values** of the joint Jacobian, so the honest way to report
  resolution is through the singular spectrum and the resolution matrix, not
  through a single "uncertainty".

## 3. The demonstration's problem and its null space

SYNTHETIC set-up: a $5\times5$ cell model over $100\ \mathrm{km}\times100\
\mathrm{km}$, 5 events at $100\ \mathrm{km}$ depth, 12 surface receivers,
60 rays, straight rays, 40 frequencies in $[0.5, 10]\ \mathrm{Hz}$, so
$60 \times 40 = 2400$ data. Model vector: $1/Q$ in each of 25 cells plus 5 event
amplitude terms, so 30 parameters. Background $Q = 300$ with a central cell at
$Q = 60$ and a neighbour at $Q = 120$.

The five largest and smallest singular values of the joint Jacobian $J$:

$$\sigma_{\max} = [6.9714, 5.1032, 4.5267, 3.4413, 3.0545]\times10^{3},$$

$$\sigma_{\min} = [1.5488\times10^{-12}, 4.2239\times10^{-13},
4.2239\times10^{-13}, 4.2239\times10^{-13}, 4.2239\times10^{-13}].$$

The numerical rank, at a threshold of $10^{-3}$ of the largest singular value, is
**22 of 30**, and $\sigma_{\min}/\sigma_{\max} = 6.059\times10^{-17}$: eight
directions have *exactly* zero singular value at double precision.

Note which eight. The amplitude block of $J$ is an identity on the rays of each
event, so it is full rank; an exact null vector must therefore have **zero**
amplitude component and must lie in the null space of $G$ alone. All eight exact
null directions are **spatial**. The source–amplitude trade-off can only ever be
an approximate degeneracy — a distinction that matters, because an approximate
degeneracy is (barely) constrained by data while an exact one is not constrained
at all.

The demonstration then exhibits the non-uniqueness in the units that matter.
Adding $5.1882\times10^{-3}$ times an exact null vector changes:

| quantity | value |
|---|---|
| $\|J m - d\|$ for the least-squares fit | $1.623\times10^{-13}$ (data scale $1.020\times10^{2}$) |
| $\|J v\|$ for the exact null vector | $4.509\times10^{-27}$ |
| rms change in $1/Q$ | $1.037631\times10^{-3}\ \mathrm{s^{-1}}$ |
| as a fraction of the mean $1/Q$ field | $0.2552$ |
| change in any event amplitude | $0.000\times10^{0}$ |
| relative change in the data | $7.204\times10^{-17}$ |
| largest single-cell change in $1/Q$ | cell 24, $0.0000 \to -5.1882\times10^{-3}\ \mathrm{s^{-1}}$ |

Two models, indistinguishable in the data at the $10^{-16}$ level, differing by
**a quarter of the mean $1/Q$ field**, and one of them gives a cell a *negative*
$1/Q$ (i.e. $Q = \infty$ in the other direction — the fit assigned that cell
exactly zero, because it lies in the null space and the data say nothing about it
at all). This is what "underdetermined" means in practice, and it is not a
numerical accident: with eight exact null directions there is an entire
eight-parameter affine family of exact fits.

## 4. The approximate trade-off, quantified

For each of the smallest *non-zero* singular directions $v_k$, compute the rms
change in $1/Q$ that the direction must have before it moves the data by the
noise level ($\sigma = 0.02$ in $\ln A$):

| $k$ | $\sigma_k$ | $\|v_{1/Q}\|$ | $\|v_b\|$ | rms $\mathrm{d}(1/Q)$ at noise | as % of mean $1/Q$ |
|---|---|---|---|---|
| 0 | $6.9714\times10^{3}$ | 1.0000 | 0.0027 | $5.74\times10^{-7}$ | 0.014 |
| 10 | $7.8417\times10^{2}$ | 1.0000 | 0.0027 | $5.10\times10^{-6}$ | 0.125 |
| 21 | $1.0352\times10^{1}$ | 0.0032 | 1.0000 | $1.25\times10^{-6}$ | 0.031 |

Read the table as a resolution statement, and read the *third* row carefully:
for the last constrained direction, the vector's amplitude component is **300
times larger** than its $1/Q$ component. That is the source–amplitude trade-off
appearing exactly where theory says it should — in the worst-constrained
direction of the joint problem — and it means that direction is essentially
"shift this event's amplitude against the whole model", bounded only by the
within-event travel-time spread. The first row is the opposite case: a direction
that constrains $1/Q$ to better than a part in $10^{4}$ of the mean field.

**Resolution is not a scalar and it is not uniform over the model.** A single
"error bar" per cell, however it is computed, hides this structure.

## 5. Damping: what it buys and what it costs

Regularise with damped least squares,
$m(\lambda) = (J^{\mathsf T}J + \lambda I)^{-1}J^{\mathsf T}d$, and add noise
$\sigma = 0.02$ in $\ln A$ to the 2400 data:

| $\lambda$ | rms misfit | rms model error | $Q$ at anomaly | $Q$ at neighbour |
|---|---|---|---|---|
| $10^{-8}$ | 0.019984 | $5.0897\times10^{-3}$ | 67.2 | 152.9 |
| $10^{-7}$ | 0.019984 | $2.5384\times10^{-3}$ | 79.6 | 236.6 |
| $10^{-6}$ | 0.019984 | $2.3852\times10^{-3}$ | 77.8 | 221.6 |
| $10^{-5}$ | 0.019984 | $2.3743\times10^{-3}$ | 77.7 | 220.4 |
| $10^{-4}$ | 0.019984 | $2.3735\times10^{-3}$ | 77.7 | 220.3 |
| $10^{-3}$ | 0.019984 | $2.3734\times10^{-3}$ | 77.7 | 220.3 |

(true $Q$: 60 at the anomaly, 120 at its neighbour, 300 elsewhere; data noise rms
is 0.020.)

Three lessons, all measured:

1. **The misfit stops falling when it reaches the noise level** — it sits at
   0.019984, just below 0.020, for every $\lambda$ from $10^{-8}$ to
   $10^{-3}$. This is the operational content of the discrepancy principle: any
   smaller misfit is fitting noise.
2. **Too little damping lets noise dominate the model error**: at
   $\lambda = 10^{-8}$ the rms model error is $5.09\times10^{-3}$, twice the best
   achievable.
3. **No $\lambda$ recovers the anomaly.** The best is $Q = 77.7$ against a true
   60, and the neighbour comes out at 220 against a true 120. The image is a
   **smoothed field**, and the smoothing is the price of the stability that the
   null space makes mandatory. Reporting "the anomaly" as a pixel value would be
   reporting an artefact of the damping.

## 6. The band problem: a constant $Q$ is always an absorption band

Every derivation above used $\alpha = \pi f/(Q v)$, a loss *linear in frequency*.
[Lesson 01](01-attenuation-measurement.md) §3 showed that an unbounded
constant-$Q$ model is impossible; the way out is the **absorption band** (Kolsky)
model: superpose $N$ standard linear solids with relaxation frequencies
log-spaced across the band, and $1/Q$ is nearly flat in the middle and elastic
outside. The demonstration measures what "nearly" costs.

Target $Q = 100$ at $f_{\text{ref}} = 1\ \mathrm{Hz}$, relaxation frequencies
covering $[0.01, 50]\ \mathrm{Hz}$, strengths fitted by non-negative least squares
so that $1/Q$ is as flat as the basis allows over the central decade:

| $N$ | peak spacing | $Q(f_{\text{ref}})$ | max deviation, central decade | band within $10\%$ |
|---|---|---|---|---|
| 2 | 5000.000 | 272.849 | $79.78\%$ | $11.0\%$ |
| 3 | 70.711 | 93.203 | $32.81\%$ | $27.4\%$ |
| 4 | 17.100 | 112.816 | $19.08\%$ | $30.4\%$ |
| 6 | 5.493 | 100.568 | $1.77\%$ | $67.2\%$ |
| 8 | 3.376 | 99.965 | $0.17\%$ | $94.9\%$ |
| 12 | 2.169 | 99.995 | $0.00\%$ | $98.5\%$ |
| 16 | 1.764 | 99.997 | $0.00\%$ | $100.0\%$ |

A single relaxation holds $1/Q$ within $10\%$ of its peak over only
$0.3841$ decades — four tenths of a decade, not the two or three that a rock
apparently sustains. The deviations collapse once the peaks overlap (spacing
below about 5) and are negligible by $N = 8$, at which point six of the 3.7
decades are reproduced to better than $2\%$ and $95\%$ of the band sits within
$10\%$. **The cost is linear in $N$**: one memory variable per grid point and one
extra update per time step per relaxation in a finite-difference code. That is
why production viscoacoustic codes use a handful of relaxations and accept a
plateau rather than an exact constant $Q$ — and why the band edges of a
tomographic model are physical parameters, not numerics.

The dispersion that comes with the band is not optional. For $Q = 100$ the
nearly-constant-$Q$ law predicts $v(f)/v(f_{\text{ref}}) - 1 =
(1/(\pi Q))\ln(f/f_{\text{ref}})$ with $1/(\pi Q) = 0.003183$, and the
demonstration's measured velocities follow it to about $4\times10^{-5}$ over
$[0.02, 20]\ \mathrm{Hz}$ — three orders of magnitude below the dispersion
itself:

| $f$ (Hz) | $Q$ | $v$ ($\mathrm{m\,s^{-1}}$) | $v/v_{\text{ref}}-1$ | $\ln(f/f_{\text{ref}})/(\pi Q)$ |
|---|---|---|---|---|
| 0.020 | 90.939 | 3526.34 | $-0.012437$ | $-0.012452$ |
| 0.100 | 100.054 | 3544.74 | $-0.007286$ | $-0.007329$ |
| 1.000 | 99.964 | 3570.75 | $0.000000$ | $0.000000$ |
| 10.000 | 99.897 | 3597.07 | $0.007371$ | $0.007329$ |
| 20.000 | 99.889 | 3605.47 | $0.009722$ | $0.009536$ |

Above the band the model becomes elastic: $Q$ climbs to $521.776$ at
$0.001\ \mathrm{Hz}$ and to $118.920$ at $60\ \mathrm{Hz}$, against a target of
$100$ — i.e. a factor $5.2$ and $1.19$. **A measured $Q$ is a band average, and
quoting it without the band is incomplete**; the top of the band is also where
the velocity stops rising, so the logarithmic law must not be extrapolated past
it.

## 7. From $Q$ to temperature, and why it is a minefield

The physical basis for a temperature reading is that anelastic relaxation is
**thermally activated**. For a single activated process the relaxation time obeys

$$\tau(T) = \tau_0 \exp\!\left(\frac{H^{*}}{R T}\right),$$

with $R = 8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}$ the gas constant, $T$ in kelvin
and $H^{*}$ the activation enthalpy (a **model parameter**; the appropriate value
for a given rock must come from a measured compilation, and it is not constant
across mechanisms). The relaxation is governed by the dimensionless group
$\omega\tau$, so the *sensitivity* of anything controlled by where the relaxation
sits is

$$\frac{\mathrm{d}\ln \tau}{\mathrm{d}T} = -\frac{H^{*}}{R T^{2}}.$$

*Worked example (SYNTHETIC parameter choice).* Take $H^{*} = 300\
\mathrm{kJ\,mol^{-1}}$ and $T = 1000\ \mathrm{K}$. Then

$$\frac{\mathrm{d}\ln\tau}{\mathrm{d}T} = -\frac{3.0\times10^{5}}
{8.314 \times 10^{6}} = -3.608\times10^{-2}\ \mathrm{K^{-1}},$$

so
- a $1\%$ change in relaxation time corresponds to only
  $\Delta T = 0.01/0.03608 = 0.277\ \mathrm{K}$;
- a $100\ \mathrm{K}$ change (from $900$ to $1000\ \mathrm{K}$) multiplies the
  relaxation time by $\exp\left(\frac{H^{*}}{R}\left(\frac{1}{900} -
  \frac{1}{1000}\right)\right) = e^{4.009} = 55.1$;
- a factor of $10$ in the relaxation time (a very ordinary anomaly in a $Q$ map)
  corresponds to $\Delta T = \ln 10 \cdot RT^{2}/H^{*} = 2.3026/0.03608 =
  63.8\ \mathrm{K}$.

The sensitivity is therefore *excellent* — which is exactly the problem, because
it is excellent in both directions. The same factor amplifies any error: a $10\%$
error in $H^{*}$ becomes a $10\%$ error in the inferred $\Delta T$, and an
unknown $Q$ band edge of a factor of a few mimics tens of kelvin.

A defensible $Q \to T$ inference must therefore state all five of: the **creep
law** and its parameters ($H^{*}$, $\tau_0$) with their provenance; the
**frequency band**, together with the assumption that the band position does not
move with $T$ — an assumption that is *false* if the band edge lies inside the
analysis band (§6); the **dynamical regime** (subsolidus, melt-bearing or
fluid-saturated), since in the melt regime $Q^{-1}$ rises with melt fraction
through a different functional form and the temperature sensitivity can change
sign; the **scattering contribution**, which is not thermally activated at all
([lesson 02](02-scattering-vs-intrinsic.md)) and therefore appears as an apparent
temperature anomaly with no temperature change; and the **resolution**, which for
a damped inversion is a smoothed field (§5).

Competing explanations for a low-$Q$ anomaly, and the measurement that
discriminates each: partial melt (a velocity reduction at the same location, and a
$V_p/V_s$ change), free water or brine (a shear-modulus reduction with little
$V_p$ change, plus electrical conductivity), composition (an independent density
estimate), scattering ([lesson 02](02-scattering-vs-intrinsic.md)'s two-band
test), and a band-edge artefact (measure a wider band and check the flatness of
$1/Q$).

**No single $Q$ anomaly establishes a temperature.** The honest output of an
attenuation tomographic study is a smoothed $1/Q$ field with a stated
resolution, stated band and stated damping, plus the list of effects that could
have produced it.

## 8. Worked numeric examples

### Example 1 — precision of $t^{*}$ from a finite band

For one ray, with white residuals of standard deviation $\sigma$ in $\ln A$ and
$N$ frequencies uniformly spanning a band of width $W$, the fitted slope has
standard deviation $\sigma_{m} = \sigma\sqrt{2}/\sqrt{\sum_i(f_i-\bar f)^2}$
(the $\sqrt{2}$ because the ratio of two amplitude estimates, each with
variance $\sigma^2$, appears). Since $t^{*} = m/\pi$, the fractional error on
$t^{*}$ equals that on the slope. With $\sigma = 0.02$ and the band
$[0.5, 10]\ \mathrm{Hz}$ at $N = 40$:

$$\sum_i (f_i-\bar f)^2 \approx \frac{N W^{2}}{12}
= \frac{40 \times 9.5^{2}}{12} = 300.8, \qquad
\sigma_m = \frac{0.02\sqrt{2}}{\sqrt{300.8}} = 1.63\times10^{-3}\ \mathrm{Hz^{-1}}.$$

Since $m = \pi t^{*}$, the fractional error is
$\sigma_{t^{*}}/t^{*} = \sigma_m/m$; for $t^{*} = 0.50\ \mathrm{s}$,
$m = \pi \times 0.5 = 1.5708\ \mathrm{Hz}$ (dimensionless per second of $t^{*}$),
giving $1.63\times10^{-3}/1.5708 = 1.04\times10^{-3}$, i.e. **$0.104\%$**. The demonstration's table reports
$0.101\%$ predicted and $0.100\%$ measured for this configuration: the
discrepancy is the logarithmic-versus-uniform spacing of the 40 frequencies, and
the agreement confirms that **the precision of $t^{*}$ is a bandwidth statement
and nothing else**. Halving the band doubles the error — the demonstration
measures $0.214\%$ for $[0.5, 5]\ \mathrm{Hz}$ against $0.101\%$ for
$[0.5, 10]\ \mathrm{Hz}$. There is no bias: the noise is symmetric and the model
is exactly linear in $t^{*}$.

### Example 2 — choosing $\lambda$ by the discrepancy principle

With $\sigma = 0.02$ in $\ln A$ and 2400 data, the expected misfit at the
solution is about $\sigma$: the demonstration measures 0.019984 for every
$\lambda \le 10^{-3}$, i.e. the fit is already at the noise floor at
$\lambda = 10^{-8}$. The discrepancy principle then says: **pick the largest
$\lambda$ whose misfit is still at the noise level**, which is
$\lambda = 10^{-3}$ in this table (misfit unchanged at 0.019984, model error at
its minimum $2.3734\times10^{-3}$). Choosing $\lambda = 10^{-8}$ because "less
damping is less biased" would double the model error for no misfit gain — a
concrete illustration that the bias–variance trade-off is decided by the noise
level, not by taste.

### Example 3 — the sensitivity of an inferred temperature

From §7 with $H^{*} = 300\ \mathrm{kJ\,mol^{-1}}$, $T = 1000\ \mathrm{K}$:
a measured $Q$ contrast of a factor 10 implies
$\Delta T = \ln 10 \cdot RT^{2}/H^{*} = 63.8\ \mathrm{K}$. Now suppose the
analysis band's upper edge sits inside the absorption band, so that the measured
$1/Q$ is depressed by a factor 5.2 (the demonstration's own band-edge value,
$Q = 521.776$ instead of $100$ at $0.001\ \mathrm{Hz}$). Then $\ln Q$ is wrong by
$\ln 5.2 = 1.65$, which the inversion converts to a spurious
$\Delta T = 1.65 \times 63.8/\ln 10 = 45.7\ \mathrm{K}$. **A band-edge artefact
and a real $64\ \mathrm{K}$ temperature contrast differ by less than a factor of
two in this reading** — which is the quantitative statement of why the band must
be measured, not assumed.

## 9. Assumptions and regime of validity

1. **Fixed ray paths.** Straight or ray-theoretical paths with a velocity model
   assumed known; the $1/Q$ inversion is linear only in this sense. Errors in the
   velocity model map into $G$ and hence into the image.
2. **Frequency-flat terms cancel.** The per-event amplitude terms are assumed
   frequency-independent over the band. A source corner frequency inside the band
   violates this and biases $t^{*}$ directly.
3. **A single arrival per window**, or a corrected one. Multi-pathing inside a
   window biases the slope.
4. **Interchangeability / normalisation.** Per-event, per-receiver amplitude
   terms are identified only through the rays that link them; the assumption must
   be stated and tested with a synthetic recovery test (see the ★★★ problem 7 in
   the [exercise set](exercises/03-attenuation-tomography-exercises.md)).
5. **Additivity of losses** over the ray ([lesson 02](02-scattering-vs-intrinsic.md) §3);
   $1/Q$ values are band averages with a stated band (§6).
6. **Damping is a choice, not a property of the Earth.** The image is a smoothed
   field; the smoothing kernel must be reported with it.
7. **Causality and dispersion are satisfied by the same model.** If the inversion
   uses a non-dispersive propagator, the travel-time bias of
   [lesson 01](01-attenuation-measurement.md) §3 appears in the predicted arrival
   times and the comparison with travel-time tomography is inconsistent.
8. **The temperature mapping requires an independent creep law**, plus the
   caveats of §7. A $Q$ map is not a temperature map.

## 10. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| $t^{*}$ | $t^{*}$ | $\mathrm{s}$ | $\int \mathrm{d}t/Q$ |
| ray-kernel element | $G_{erc}$ | $\mathrm{s}$ | $\int \mathrm{d}l/v$: path time in the cell |
| model parameter | $1/Q$ | dimensionless | |
| data | $\ln(A/A_{\text{ref}})$ | dimensionless | $-\pi f t^{*}$ |
| Jacobian entry | $\partial/\partial(1/Q)$ | $\mathrm{s}$ | $-\pi f \times \mathrm{s} = \mathrm{s}$ times $\mathrm{s^{-1}}$ |
| activation enthalpy | $H^{*}$ | $\mathrm{J\,mol^{-1}}$ | $R$ is $\mathrm{J\,mol^{-1}\,K^{-1}}$ |

The Jacobian entry check is worth doing once explicitly: $\pi f$ has units
$\mathrm{s^{-1}}$ and $G$ has seconds, so their product is dimensionless while
$G$ *itself* is a time. Mixing these up is the commonest unit error in
attenuation tomography, and it produces a Jacobian that is wrong by the whole
frequency vector.

## 11. Python demonstrations

Two demonstrations support this lesson.

- [`code/tstar_tomography_demo.py`](code/tstar_tomography_demo.py) — the
  source-amplitude trade-off, measured. Sections: (1) $t^{*}$ precision versus
  band and noise, against a closed-form prediction; (2) the exact null space from
  the SVD, and two models that fit the data to machine precision while differing
  by a quarter of the mean $1/Q$ field; (3) what damping costs on noisy data.
  Section 2 is the one that changes how an attenuation image should be reported.
- [`code/absorption_band_demo.py`](code/absorption_band_demo.py) — the number of
  relaxations required for a "constant" $Q$, the accuracy of the logarithmic
  dispersion law, and the price of the band edges. Read it before trusting any
  statement that a model is "constant $Q$".

Full sets with worked solutions are in
[`exercises/03-attenuation-tomography-exercises.md`](exercises/03-attenuation-tomography-exercises.md)
and
[`exercises/03-attenuation-tomography-solutions.md`](exercises/03-attenuation-tomography-solutions.md).

## Mastery checkpoint

Without notes:

> A 30-parameter joint inversion for $1/Q$ in 25 cells plus 5 event amplitudes
> has measured singular values ranging from $6.97\times10^{3}$ to
> $4.22\times10^{-13}$, with numerical rank 22 at a $10^{-3}$ threshold.
> **(a)** How many exact null directions are there, and why must none of them
> contain an amplitude component? **(b)** The data noise is $\sigma = 0.02$ in
> $\ln A$; explain in one paragraph why the honest report of a cell's $1/Q$ is an
> interval plus a smoothing kernel rather than a number. **(c)** For a measured
> $Q$ contrast of a factor 5, compute the implied $\Delta T$ for
> $H^{*} = 300\ \mathrm{kJ\,mol^{-1}}$ at $T = 900\ \mathrm{K}$, and state two
> effects that could produce the same contrast without any temperature change.
> **(d)** A $t^{*}$ is measured over $[1, 8]\ \mathrm{Hz}$ with
> $\sigma = 0.03$ and 32 samples. Compute $\sigma_{t^{*}}/t^{*}$ and decide
> whether the measurement can distinguish $Q = 100$ from $Q = 105$.

A worked version appears in the
[solutions](exercises/03-attenuation-tomography-solutions.md).

## Common pitfalls

1. **Reporting a pixel value from a damped inversion.** The image is a smoothed
   field (§5).
2. **Treating the source-amplitude trade-off as exact.** It is approximate, and
   the demonstration shows it living in the worst-constrained direction, not in
   the null space.
3. **Assuming the null space is small.** Eight exact directions out of thirty in
   a modest synthetic problem.
4. **Quoting $Q$ without the band.** The band is the measurement (§6).
5. **Forgetting that $1/Q$ can come out negative** and applying no constraint;
   and its converse, constraining so hard that the anomaly is smoothed away.
6. **Mapping $Q$ to temperature without an activation enthalpy and its
   provenance.** The sensitivity is $H^{*}/(RT^{2})$ per kelvin — enormous — so
   errors in $H^{*}$ matter as much as errors in $Q$.
7. **Ignoring scattering.** A non-thermally-activated contribution that reads as
   temperature.
8. **Using a non-dispersive propagator with an attenuating model**, producing
   internally inconsistent travel times.

## Related modules

- [06-05 Attenuation and Anelasticity](README.md) — this module.
- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) — the
  travel-time sibling of this inversion, with the same kernels and a much better
  noise model.
- [06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md) —
  how the resulting uncertainties are carried into decisions.
- [18-inverse-problems](../../18-inverse-problems/README.md) — null space,
  resolution matrices and regularisation in general form.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — the
  viscoacoustic implementation cost that the absorption band implies.

## Self-assessment checklist

- [ ] I can write the forward problem including the per-event amplitude terms.
- [ ] I can explain why the source trade-off is approximate, not exact.
- [ ] I can compute a null space and exhibit two indistinguishable models.
- [ ] I can choose $\lambda$ against a stated noise level and say what it costs.
- [ ] I can compute $\sigma_{t^{*}}/t^{*}$ and design a band.
- [ ] I can state how many relaxations a "constant-$Q$" model needs and why the
      band edges matter.
- [ ] I can derive $\mathrm{d}\ln\tau/\mathrm{d}T$ and list four competing
      explanations for a $Q$ anomaly.
