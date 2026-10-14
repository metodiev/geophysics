---
id: 11-02-05
title: "Radiometrics and Alteration Mapping"
level: graduate
prereqs: ["05-01-01", "05-02-02", "11-02-01"]
tags: [exploration-geophysics, mineral-exploration, radiometrics, gamma-spectrometry, alteration, Poisson-statistics]
---

# Radiometrics and Alteration Mapping

Airborne gamma-ray spectrometry is the cheapest geophysical survey in existence
and the only one that measures *geochemistry* directly. It is also the most
severely limited: gamma rays are stopped by a few tens of centimetres of rock, so
the method maps the surface and nothing below it. This lesson builds the method
from its physics — the exponential attenuation of gamma photons, the response of
an infinite plane source as a function of flying height, the three-window
spectrometer and its stripping inverse, the radioelement ratios that are the real
product of an alteration survey, and the Poisson counting statistics that set every
detection limit.

**All models and data in this module are SYNTHETIC.** Concentrations, sensitivity
coefficients, stripping ratios, counting times and noise levels are chosen
teaching values. Two quantities are used as standard constants and are stated
where they appear: the density of air
($\rho_{\text{air}} = 1.225\times10^{-3}\ \mathrm{g\,cm^{-3}}$) and the mass
attenuation coefficients of air at the two window energies.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the flux from an infinite plane source through an attenuating
   atmosphere, $F(h) = (M/2)E_2(\mu h)$, verify it against a direct numerical
   integral, and **compute** the count rate at any flying height.
2. **Compute** the half-height of each spectrometer window and **explain** why the
   Th/K ratio drifts with flying height.
3. **Set up and invert** the three-window stripping matrix, and **state** the
   conditioning requirement for the inverse to be usable.
4. **Compute** the burial attenuation and **state** the resulting depth limit of the
   method, with the half-value layer as the natural unit.
5. **Compute** radioelement ratios for altered and unaltered rocks and **quantify**
   their separability given Poisson counting noise.
6. **Compute** the counting-statistics limit on precision versus integration time,
   and **state** why radiometric surveys are flown fast and wide.
7. **State** which inputs of a radiometric interpretation are calibrations, which
   are measurements, and which are geological assumptions — including
   U-series disequilibrium.

## Prerequisites

- [05-01-01 The Central Idea: Property Contrasts Produce Signals](../../05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md)
  — what a radioelement contrast is and why it produces a signal.
- [05-02-02 Units and Conventions for Gravity, Magnetic and EM Fields](../../05-core-geophysics/02-geophysical-fields-and-observables/02-field-measurement-units.md)
  — units and calibration conventions.
- [11-02-01 Geophysical Signatures of Major Deposit Types](01-deposit-signatures.md)
  — where the radioelements sit in the deposit-class signature table.

## 1. The physics: attenuation, and why it fixes everything

A gamma photon of energy $E$ is removed from a beam according to
$I = I_0e^{-\mu d}$ with the **linear attenuation coefficient**

$$\mu = \left(\frac{\mu}{\rho}\right)\rho \qquad (\mathrm{cm^{-1}}),$$

and in aeroradiometry two very different media matter:

| path | medium | $\mu/\rho$ (cm² g⁻¹) | $\rho$ (g cm⁻³) | $\mu$ |
|---|---|---|---|---|
| between the ground and the aircraft | air | 0.053 (K, 1.46 MeV) | 1.225×10⁻³ | 6.49×10⁻³ m⁻¹ |
| between a buried source and the surface | soil/rock | 0.060 | 1.6–2.7 | 0.096–0.162 cm⁻¹ |

The **air** coefficient is what sets the flying-height penalty; the **rock**
coefficient is what sets the depth limit. They are four orders of magnitude apart
in their effect, and conflating them is the commonest error in the subject.

The natural unit for burial is the **half-value layer**,

$$\text{HVL} = \frac{\ln 2}{\mu} = \frac{0.6931}{0.0960} = 7.22\ \mathrm{cm\ of\
soil}\ (\rho = 1.6\ \mathrm{g\,cm^{-3}}),$$

and the transmitted fraction measured by the demonstration is $0.383$ at
$10\ \mathrm{cm}$, $0.0561$ at $30\ \mathrm{cm}$, $0.00823$ at $50\ \mathrm{cm}$
and $6.8\times10^{-5}$ at $100\ \mathrm{cm}$. Ten half-value layers is
$72.2\ \mathrm{cm}$: **radiometrics is a surface geochemical mapper, and its
depth of investigation is a consequence of one constant.**

## 2. The height response of an infinite plane source

A uniform source on the ground is best modelled as an infinite plane of emission
$M$ per unit area. Take an annulus of radius $x$ and width $\mathrm{d}x$ at
horizontal distance $x$ from the point directly below the detector, which flies at
height $h$. The path length is $r = \sqrt{x^{2}+h^{2}}$, the obliquity factor is
$h/r$, the solid angle is $\mathrm{d}A\cos\theta/(4\pi r^{2})$, and the
attenuation is $e^{-\mu r}$, so

$$\mathrm{d}F = \frac{M\,(2\pi x\,\mathrm{d}x)\,(h/r)}{4\pi r^{2}}
e^{-\mu r} = \frac{Mh}{2}\frac{x\,\mathrm{d}x}{r^{3}}e^{-\mu r}.$$

Substituting $r = \sqrt{x^{2}+h^{2}}$, so that $x\,\mathrm{d}x = r\,\mathrm{d}r$,

$$F(h) = \frac{Mh}{2}\int_h^{\infty}\frac{e^{-\mu r}}{r^{2}}\,\mathrm{d}r
= \frac{M}{2}\,E_2(\mu h),
\qquad
E_2(z) = \int_1^{\infty}\frac{e^{-zt}}{t^{2}}\,\mathrm{d}t ,$$

and the normalised height response is therefore

$$\boxed{\;R(h) = \frac{F(h)}{F(0)} = E_2(\mu h)\;}$$

using $E_2(0) = \int_1^\infty t^{-2}\,\mathrm{d}t = 1$, which is the unattenuated
result that half of a surface emission escapes upward regardless of altitude.

The demonstration verifies this against a direct annular numerical integration:
at $h = 30\ \mathrm{m}$ the numeric integral gives $0.580645$ against the closed
form's $0.580645$ (difference $1.8\times10^{-8}$), and at $h = 120\ \mathrm{m}$
$0.207468$ against $0.207468$ ($6.3\times10^{-10}$).

### The measured height dependence

With the air coefficients of §1:

| $h$ (m) | $\mu_Kh$ | $R_K$ | $\mu_{\text{Th}}h$ | $R_{\text{Th}}$ | Th/K drift |
|---|---|---|---|---|---|
| 0 | 0.000 | 1.0000 | 0.000 | 1.0000 | 1.0000 |
| 30 | 0.195 | 0.5806 | 0.132 | 0.6679 | 1.1503 |
| 60 | 0.390 | 0.3968 | 0.265 | 0.5028 | 1.2672 |
| 120 | 0.779 | 0.2075 | 0.529 | 0.3108 | 1.4981 |
| 200 | 1.299 | 0.0966 | 0.794 | 0.1772 | 1.8330 |

Two results:

1. **Height is a first-order control on count rate.** The half-heights are
   $41.2\ \mathrm{m}$ (K window) and $60.6\ \mathrm{m}$ (Th window), computed by
   solving $E_2(\mu h) = 0.5$. Flying at $120\ \mathrm{m}$ instead of $30\
   \mathrm{m}$ costs a factor of $2.8$ in the K window.
2. **The response is not a pure exponential.** For large $\mu h$,
   $E_2(z) \to e^{-z}/z$, so the flux falls slightly *faster* than $e^{-\mu h}$
   (the demonstration measures the ratio $E_2(z)/(e^{-z}/z) = 0.55$ at $z = 2$,
   $0.74$ at $z = 5$ and $0.91$ at $z = 20$: the asymptotic is approached
   slowly). Fitting a simple exponential to a height-attenuation curve therefore
   gives a height-dependent apparent coefficient.

## 3. Differential attenuation and the Th/K ratio

Th (2.61 MeV) is attenuated less than K (1.46 MeV), so the Th/K ratio **rises
with flying height**. Measured, relative to $30\ \mathrm{m}$:

| height (m) | Th/K relative to 30 m | bias (%) |
|---|---|---|
| 30 | 1.1503 | 0.00 |
| 60 | 1.2672 | +10.16 |
| 90 | 1.3815 | +20.10 |
| 120 | 1.4981 | +30.24 |
| 180 | 1.7452 | +51.72 |

**A ratio flown at $120\ \mathrm{m}$ and interpreted as if it were flown at
$30\ \mathrm{m}$ is biased by $30\%$.** Over a drape with $100\ \mathrm{m}$ of
relief, the apparent Th/K varies by that amount across the map **with no change in
the ground**. The consequence is a reporting rule: ratios are formed only after
height correction, and an uncorrected ratio map is substantially a map of terrain.
The *strength* of the ratio is real, however — it cancels the source concentration,
the instrument gain and the soil-moisture factor simultaneously, none of which can
be measured in flight.

## 4. The three-window spectrometer and the stripping inverse

K, U and Th are detected through different photopeaks, but Compton scattering moves
counts between the windows, so the raw window count rates $\mathbf{w}$ are a
mixture:

$$\mathbf{w} = \mathbf{S}\left(\mathbf{s}\odot\mathbf{c}\right),$$

where $\mathbf{c}$ is the concentration vector (K %, eU ppm, eTh ppm),
$\mathbf{s}$ the per-unit sensitivities and $\mathbf{S}$ the **stripping matrix**.
For the SYNTHETIC calibration of the demonstration

$$\mathbf{S} = \begin{pmatrix}1.00 & 0.30 & 0.10\\ 0.05 & 1.00 & 0.30\\
0.00 & 0.00 & 1.00\end{pmatrix}, \qquad
\mathbf{s} = (95.0,\ 4.2,\ 2.4),$$

with singular values $1.2694$, $0.9704$, $0.7996$ and condition number
**1.588**. Inverting gives

| rock | %K | eU | eTh | recovered %K | recovered eU | recovered eTh |
|---|---|---|---|---|---|---|
| unaltered granodiorite | 2.0 | 2.0 | 10.0 | 2.000 | 2.000 | 10.000 |
| potassic alteration | 4.5 | 2.5 | 6.0 | 4.500 | 2.500 | 6.000 |
| argillic alteration | 0.8 | 3.5 | 14.0 | 0.800 | 3.500 | 14.000 |
| potassic core | 5.5 | 2.0 | 3.0 | 5.500 | 2.000 | 3.000 |

with a worst round-trip error of $1.8\times10^{-15}$. **The conditioning matters
because the inverse amplifies noise by the condition number:** with
$\kappa = 1.588$, a $1\%$ error in a window count rate becomes at most a $1.6\%$
error in a concentration — acceptable. Real stripping matrices in high-U terrain
can have $\kappa$ of several units, and a poorly conditioned one turns counting
noise into negative concentrations, which is the practical signal that the
stripping constants are wrong or the window widths are inappropriate.

## 5. Worked example — alteration mapping and the noise floor

Alteration changes the radioelement **ratios**, so the diagnostic is Th/K (or
K/(K+U+Th)) rather than any single channel:

| rock | %K | eU | eTh | Th/K | K/(K+U+Th) |
|---|---|---|---|---|---|
| unaltered granodiorite | 2.00 | 2.00 | 10.00 | 5.00 | 0.143 |
| potassic alteration | 4.50 | 2.50 | 6.00 | 1.33 | 0.346 |
| argillic alteration | 0.80 | 3.50 | 14.00 | 17.50 | 0.044 |
| potassic core | 5.50 | 2.00 | 3.00 | 0.55 | 0.524 |

The ratios differ by factors of four to thirty while the individual concentrations
differ by factors of two to five: **the ratio is the sensitive diagnostic because
alteration adds or removes K while the Th content is largely inherited from the
protolith.**

Now propagate Poisson noise. For a count rate $N$ (counts/s) integrated for $T$
seconds, the counts are $N T$ and

$$\frac{\sigma_N}{N} = \frac{1}{\sqrt{NT}}, \qquad
\sigma_{a/b} = \frac{a}{b}\sqrt{\left(\frac{\sigma_a}{a}\right)^{2}
+\left(\frac{\sigma_b}{b}\right)^{2}} .$$

At $T = 300\ \mathrm{s}$:

| rock | Th/K | $\sigma$(Th/K) | separation from host (σ) |
|---|---|---|---|
| unaltered granodiorite | 5.000 | 0.0624 | 0.0 |
| potassic alteration | 1.333 | 0.0206 | **177.8** |
| argillic alteration | 17.500 | 0.2063 | **60.6** |
| potassic core | 0.545 | 0.0118 | **377.0** |

**Every unit is separated from the host at tens to hundreds of sigma** in five
minutes of counting. This is why radiometrics is such an efficient mapping tool:
the *signal* is enormous compared with counting noise. It is also why the method's
limitations are never about noise — they are about cover, about calibration, and
about whether the surface pattern is connected to anything at depth.

## 6. Counting statistics: why surveys are flown fast and wide

The detection limit follows from §5's relation directly:

| $T$ (s) | $N_K$ (counts) | relative σ | σ(%K) | σ(Th/K) |
|---|---|---|---|---|
| 10 | 1 949 | 0.02265 | 0.0453 | 0.3420 |
| 30 | 5 848 | 0.01308 | 0.0262 | 0.1975 |
| 100 | 19 492 | 0.00716 | 0.0143 | 0.1082 |
| 300 | 58 476 | 0.00414 | 0.0083 | 0.0625 |
| 1000 | 194 920 | 0.00227 | 0.0045 | 0.0342 |

The uncertainty falls as $T^{-1/2}$, so **a factor of ten in precision costs a
factor of a hundred in time**. The economics follow immediately: a survey can
either fly slowly for precision or quickly for coverage, and since the signal is
already separated at hundreds of sigma (§5), coverage wins. The same relation is
the reason a radiometric map should be read with its pixel size in mind: two
adjacent pixels with different Th/K may differ only because of counting noise, a
question a variogram answers and a contour map hides.

## 7. Assumptions and regime of validity

1. **Infinite plane source.** The $E_2$ result requires a source that is
   indefinitely wide compared with the height and whose radioelement content is
   uniform. Over a unit $50\ \mathrm{m}$ across, flown at $120\ \mathrm{m}$, the
   assumption fails in the direction that *reduces* the anomaly; the standard
   correction is a footprint or "field of view" calculation, which the
   demonstration does not do.
2. **Single, constant attenuation coefficient per window.** The air coefficient is
   energy-dependent, and a spectrum drifting with temperature changes the effective
   window energy. Spectral stabilisation is therefore a prerequisite, not an
   accessory.
3. **Uniform soil moisture and vegetation.** Water attenuates gamma rays; wet soil
   and a forest canopy suppress the signal and alter the ratio, and neither is
   corrected by a height measurement. This is the largest *unquantified* error in
   most surveys.
4. **U-series equilibrium.** eU is inferred from a decay product (²¹⁴Bi for the
   $1.76\ \mathrm{MeV}$ window), so the measurement assumes secular equilibrium in
   the ²³⁸U chain. Radon escape from the soil breaks that assumption, and the
   resulting "radon anomaly" can be larger than the geological signal.
5. **The stripping constants and sensitivities are calibrations.** They come from
   pads, test ranges or a synthesis — not from the survey data. Reporting a
   concentration means reporting which calibration produced it.
6. **The concentration–count-rate relation is linear.** Detector dead time makes it
   non-linear at high count rates, which is exactly where the K-rich alteration
   target sits.
7. **The surface pattern represents the bedrock.** This is a *geological*
   assumption, not a geophysical one, and it is the one that fails under cover,
   under transported soil, and in farmland.
8. **All numbers SYNTHETIC**, except the two standard constants named in the
   header.

## 8. Units, dimensional checks and the identities worth memorising

| Quantity | Unit | Check |
|---|---|---|
| $\mu/\rho$ | cm² g⁻¹ | standard tabulated quantity |
| $\mu = (\mu/\rho)\rho$ | cm⁻¹ | g cm⁻³ × cm² g⁻¹ = cm⁻¹ ✔ (× 100 for m⁻¹) |
| HVL | cm | $\ln 2/\mu$ ✔ |
| $E_2(\mu h)$ | – | argument dimensionless, function dimensionless ✔ |
| concentration | % K, ppm eU, ppm eTh | the conventional units, not SI |
| sensitivity $s$ | counts s⁻¹ per unit concentration |  |
| separation | σ | a difference divided by its standard error ✔ |

Three identities worth checking on any radiometric calculation:

1. $E_2(0) = 1$ and $E_2(z) \to e^{-z}/z$: the height response must start at 1 and
   must eventually decay faster than an exponential. The demonstration confirms
   both, to $0.999986$ and to a ratio of $0.91$ at $z = 20$;
2. the ratio of two windows over the same source is a **pure height function**
   once the ground is uniform, which is exactly why height correction is applied
   before ratio maps are made;
3. $\sigma/N = 1/\sqrt{NT}$ must reproduce a Monte Carlo: the demonstration's
   analytic $0.011785$ against a simulated $0.011816$ over $2\times10^{5}$ Poisson
   draws.

## 9. Exercises

Full sets with worked solutions:
[`exercises/05-radiometrics-for-minerals-exercises.md`](exercises/05-radiometrics-for-minerals-exercises.md)
and
[`exercises/05-radiometrics-for-minerals-solutions.md`](exercises/05-radiometrics-for-minerals-solutions.md).

## Mastery checkpoint

Without notes:

> A SYNTHETIC survey area has a host with K = 2.2%, eU = 1.8 ppm, eTh = 9.5 ppm,
> and an altered zone with K = 4.0%, eU = 2.6 ppm, eTh = 6.5 ppm. **(a)** Compute
> Th/K and K/(K+U+Th) for both and state the fractional change in each. **(b)**
> Compute the Th/K ratio you would measure at $60\ \mathrm{m}$ and at
> $150\ \mathrm{m}$ flying height for the *host* if the ground value is 4.32,
> using the demonstration's air coefficients, and give the percentage difference.
> **(c)** Compute the transmitted fraction of a gamma flux from bedrock beneath
> $40\ \mathrm{cm}$ of soil at $\rho = 1.7\ \mathrm{g\,cm^{-3}}$ with
> $\mu/\rho = 0.06\ \mathrm{cm^{2}\,g^{-1}}$. **(d)** Compute the relative
> uncertainty in the K window after a $120\ \mathrm{s}$ integration if the count
> rate is $180\ \mathrm{counts\,s^{-1}}$. **(e)** State the two assumptions your
> answers depend on most.

A worked version is in the
[solutions](exercises/05-radiometrics-for-minerals-solutions.md).

## Common pitfalls

1. **Conflating air and soil attenuation.** They differ by four orders of
   magnitude, and mixing them makes either the height or the burial effect wrong.
2. **Forming ratios before height correction.** A $30\%$ apparent Th/K change can
   be entirely terrain.
3. **Quoting a concentration without its calibration.** Sensitivities and stripping
   constants are calibration inputs, not measurements of the ground.
4. **Treating eU as a uranium measurement.** It is a ²¹⁴Bi measurement that assumes
   secular equilibrium; radon escape breaks it.
5. **Ignoring moisture and vegetation.** Neither is corrected by height, and both
   suppress and re-weight the spectrum.
6. **Reading a contour map as if it were noiseless.** At typical pixel sizes the
   counting noise is a substantial part of the short-wavelength variation.
7. **Assuming the surface pattern is the bedrock.** Under transported cover,
   radiometrics maps the cover.
8. **Pushing count rates into detector dead time.** A K-rich zone is exactly where
   the linear assumption fails, so the highest values are the least reliable.

## Related modules

- [11-02-01 Geophysical Signatures of Major Deposit Types](01-deposit-signatures.md)
  — the radioelement rows of the signature table, and the direction-based
  discrimination argument.
- [11-02-02 Magnetics for IOCG, Porphyry and Magmatic Sulphides](02-magnetics-for-minerals.md)
  — where the radioelements and the magnetics disagree, and why that is useful.
- [11-02-07 Multi-Method Targeting and Prospectivity Analysis](07-multi-method-targeting.md)
  — how a radiometric layer is combined with the others, and how combination
  fails.
- [05-02 Geophysics Fields and Observables](../../05-core-geophysics/02-geophysical-fields-and-observables/README.md)
  — the general treatment of measurement units and calibration.
