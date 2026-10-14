---
id: 17-01-02
title: "Reflectance, Emissivity and Spectral Signatures"
level: advanced
prereqs: ["17-01-01", "02-10-04"]
tags: [remote-sensing, gis, reflectance, emissivity, spectral-signature, kirchhoff]
---

# Reflectance, Emissivity and Spectral Signatures

A remote-sensing instrument does not measure a material. It measures radiance at
an aperture, at specific wavelengths, at a specific time, from a specific
geometry. Everything called a "spectral signature" is the product of a radiance
measurement and a model that turns radiance into a material property. This
lesson builds that model for the two properties the rest of the folder uses
constantly — **reflectance** in the reflected-solar region and **emissivity** in
the thermal region — and shows exactly how much interpretation each one
requires.

Two ideas organise the lesson.

The first is **energy conservation**. Radiation arriving at a surface is either
reflected, transmitted or absorbed. If the surface is opaque the transmitted term
vanishes and the absorbed fraction is fixed by the reflected fraction. Kirchhoff's
law then says the absorbed fraction equals the emitted fraction at the same
wavelength and in the same direction. Emissivity is therefore not a separate
material property to be measured in the thermal infrared: it is the complement of
reflectance, and getting one right means getting the other right.

The second is that **a signature is a shape, not a value**. A reflectance
spectrum carries information in where its absorption features sit and how deep
they are. Extracting that information requires the illumination spectrum against
which the reflectance is weighted, the viewing geometry through which it is
sampled, and the atmosphere in between. Each of those can remove a real signal or
manufacture a false one, and this lesson quantifies how much.

All models and data in this module are **SYNTHETIC**. The three spectral
reflectance curves are sums of logistic and Gaussian terms with parameters chosen
in `code/reflectance_emissivity_demo.py`; they are teaching shapes, not measured
spectra of any real material, and the notional bands are intervals defined in
that file.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** radiance, irradiance, BRDF, directional-hemispherical reflectance
   and albedo, and **state** the units of each.
2. **Derive** the Lambertian relation $L = \rho E/\pi$ by integrating the BRDF
   over the hemisphere, and **explain** where the factor $\pi$ comes from.
3. **Apply** energy conservation and Kirchhoff's law to compute emissivity from
   reflectance for an opaque surface, and **state** what changes for a
   translucent one.
4. **Invert** the Planck function numerically to obtain a brightness temperature,
   and **explain** why it is not the surface temperature.
5. **Quantify** the temperature error caused by a wrong emissivity assumption,
   analytically and numerically.
6. **Compute** a broadband albedo as a spectrum-weighted mean and **demonstrate**
   that the same surface has a different albedo under a different illumination.
7. **State** what a bidirectional reflectance measurement can and cannot tell you
   about the hemispherical reflectance it is usually reported as.

## Prerequisites

- [17-01-01 The Electromagnetic Spectrum and Sensing Windows](01-em-spectrum-remote-sensing.md)
  — the Planck function, the constants, and the sensing windows used here.
- [02-10-04 Spectroscopy Principles for Remote Sensing](../../02-physics/10-optics-and-photometry/04-spectroscopy.md)
  — absorption features and the spectroscopic vocabulary behind "spectral
  signature".

---

## 1. Intuition: what a spectrum is a spectrum *of*

Put a leaf under a laboratory spectrometer and measure its reflectance. Put the
same leaf under a satellite and measure a radiance. The two numbers are related
but not equal, and the difference is not a nuisance — it is the entire content of
optical remote sensing. The laboratory measurement isolates the leaf. The
satellite measurement contains

$$L_{\rm sensor} = \underbrace{L_{\rm path}}_{\text{atmosphere scattering}}
+ \underbrace{\frac{T_\uparrow}{\pi}\Big[\rho\,E_{\rm sun}T_\downarrow +
\rho\,E_{\rm sky}\Big]}_{\text{surface, attenuated}} ,$$

schematically: an additive atmospheric term that never touched the ground, and a
multiplicative surface term attenuated on the way down and on the way up. Only
after both are modelled does the radiance become a reflectance, and only after
that does it become a material property.

The thermal region has the same structure with emitted rather than reflected
radiation:

$$L_{\rm sensor} = L_{\rm path,\uparrow}
+ T_\uparrow\left[\varepsilon B_\lambda(T_s) + (1-\varepsilon)L_{\rm down}\right],$$

where the $(1-\varepsilon)$ term is the *reflected sky* contribution — a surface
that emits badly reflects well, and in the thermal infrared that reflection is
not negligible.

This lesson builds the surface terms $\rho$ and $\varepsilon$ and their
properties. The atmospheric terms are the subject of
[17-01-03](03-atmospheric-effects.md).

## 2. Precise definitions and units

### 2.1 The four radiometric quantities

| Quantity | Symbol | Unit | Meaning |
|---|---|---|---|
| spectral radiance | $L_\lambda$ | W m⁻² sr⁻¹ m⁻¹ | power per area, per solid angle, per wavelength |
| spectral irradiance | $E_\lambda$ | W m⁻² m⁻¹ | power per area **arriving** on a surface |
| spectral exitance | $M_\lambda$ | W m⁻² m⁻¹ | power per area **leaving** a surface |
| BRDF | $f_r(\theta_i,\phi_i;\theta_r,\phi_r)$ | sr⁻¹ | reflected radiance per unit incident irradiance |

The BRDF is the fundamental surface property in the reflected domain:

$$f_r = \frac{\mathrm{d}L_r(\theta_r,\phi_r)}
{\mathrm{d}E_i(\theta_i,\phi_i)}
\qquad [\mathrm{sr^{-1}}].$$

It is **not** bounded by unity; only its hemispherical integral is.

### 2.2 Reflectance and its several meanings

The **directional-hemispherical reflectance** for a beam arriving from
$(\theta_i,\phi_i)$ is the fraction of that beam's energy returned into the whole
hemisphere:

$$\rho_{\rm dh}(\theta_i,\phi_i)
= \int_{2\pi} f_r(\theta_i,\phi_i;\theta_r,\phi_r)
\cos\theta_r\,\mathrm{d}\Omega_r \quad \in[0,1].$$

The **albedo** (or bihemispherical reflectance) is the same quantity averaged
over an incident hemisphere, i.e. the fraction of *all* incoming energy returned:

$$\alpha = \frac{\displaystyle\int_{2\pi}\!\!\int_{2\pi}
f_r\cos\theta_r\cos\theta_i\,\mathrm{d}\Omega_r\,\mathrm{d}\Omega_i}
{\displaystyle\int_{2\pi}\cos\theta_i\,\mathrm{d}\Omega_i}.$$

For a Lambertian surface the two coincide; for a real one they do not, which is
Section 4.4.

### 2.3 Energy conservation and the optical taxonomy

At every wavelength, for a layer,

$$\rho(\lambda) + \tau(\lambda) + \alpha(\lambda) = 1,$$

where $\tau$ is transmittance and $\alpha$ is **absorptance** (not to be confused
with broadband albedo; the symbols clash across the literature and you must read
each source's definition). Three useful limits:

- **Opaque**: $\tau = 0$, so $\alpha = 1-\rho$.
- **Perfect reflector**: $\rho = 1$, $\alpha = 0$.
- **Blackbody**: $\rho = 0$, $\alpha = 1$.

The synthetic demonstration prints the identity explicitly: at
$0.65\ \mathrm{\mu m}$ a soil-like surface has $\rho = 0.360$, $\tau = 0$,
$\alpha = 0.640$, and the three sum to $1.000$.

### 2.4 Emissivity and Kirchhoff's law

The spectral emissivity is the ratio of the surface's emission to that of a
blackbody at the same temperature:

$$\varepsilon(\lambda) = \frac{L_{\rm emitted}(\lambda)}{B_\lambda(T)}
\qquad \in[0,1].$$

**Kirchhoff's law** (for a body in local thermodynamic equilibrium) states that
the spectral emissivity equals the spectral absorptance *in the same direction
and at the same wavelength*:

$$\varepsilon(\lambda,\theta,\phi) = \alpha(\lambda,\theta,\phi).$$

Combining with energy conservation for an opaque body,

$$\boxed{\;\varepsilon(\lambda) = 1 - \rho(\lambda)\;}\qquad(\text{opaque, LTE}).$$

This is why a reflectance measurement in the thermal infrared is a way to *get*
emissivity: the demonstration obtains
$\varepsilon = 0.890$ (soil-like), $0.860$ (vegetation-like) and $0.995$
(water-like) purely from the synthetic reflectance curves at
$10.8\ \mathrm{\mu m}$.

## 3. Derivations

### 3.1 The Lambertian relation $L = \rho E/\pi$

Assume the surface reflects isotropically, so $f_r = f_0$ (constant). Then the
exitance is

$$M = \int_{2\pi} L_r\cos\theta_r\,\mathrm{d}\Omega_r
= L_r\int_0^{2\pi}\!\!\int_0^{\pi/2}\cos\theta_r\sin\theta_r\,
\mathrm{d}\theta_r\,\mathrm{d}\phi_r = \pi L_r,$$

because $\int_0^{\pi/2}\cos\theta\sin\theta\,\mathrm{d}\theta = 1/2$ and the
azimuthal integral contributes $2\pi$. Requiring $M = \rho E$ (all reflected
energy leaves) gives

$$\boxed{\;L_r = \frac{\rho E}{\pi}\;}\qquad\text{and}\qquad
f_0 = \frac{\rho}{\pi}.$$

The $1/\pi$ is not a fudge factor; it is the solid-angle geometry of a
hemisphere. Forgetting it is one of the commonest numerical errors in this
subject, and it always shows up as a factor of $3.14$ in a radiance budget.

*Numerical check.* With $E = 800\ \mathrm{W\,m^{-2}}$ (SYNTHETIC surface
irradiance) and $\rho_{\rm red} = 0.363$:
$L = 0.363\times800/\pi = 92.38\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$ — the value
the demonstration prints for the soil-like surface in the red band.

### 3.2 Kirchhoff's law from detailed balance

Place the surface inside an isothermal cavity at temperature $T$. In equilibrium
the surface receives the blackbody radiance $B_\lambda(T)$ from every direction
and must return exactly that radiance, or the cavity would not be in equilibrium
(a net flow would violate the second law). Its outgoing radiance is its own
emission plus its reflection of the cavity:

$$\varepsilon(\lambda)B_\lambda(T) + \rho(\lambda)B_\lambda(T) = B_\lambda(T)
\;\Longrightarrow\; \varepsilon + \rho = 1,$$

which is Kirchhoff's law for an opaque body. For a translucent body the cavity
radiation that passes through must be subtracted, and the law becomes

$$\varepsilon = 1 - \rho - \tau = \alpha.$$

Two caveats worth stating: the law requires **local thermodynamic equilibrium**
(it fails in the upper atmosphere, where emission lines invert), and it is
**directional and spectral** (a surface can be a good reflector at one angle and
a poor one at another).

### 3.3 Inverting the Planck function for a brightness temperature

Given a measured spectral radiance $L$ at wavelength $\lambda$, the **brightness
temperature** $T_b$ is the temperature of the blackbody that would produce it.
Inverting

$$L = \frac{2hc^{2}}{\lambda^{5}}\frac{1}{e^{hc/(\lambda k_B T)}-1}$$

gives

$$\boxed{\;T_b = \frac{hc}{\lambda k_B}\,
\frac{1}{\ln\!\left(1 + \dfrac{2hc^{2}}{\lambda^{5} L}\right)}\;}.$$

The demonstration implements exactly this and verifies it by forward modelling:
substituting $T_b$ back into Planck reproduces $L$ to a relative error of
$1.9\times10^{-16}$ to $3.4\times10^{-16}$, i.e. double-precision round-off.

*Numerical check.* For the soil-like surface, $\varepsilon = 0.890$ and
$T = 300\ \mathrm{K}$ at $10.8\ \mathrm{\mu m}$ give
$L = 0.890\,B_\lambda(300) = 8.6058\times10^{6}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$.
Feeding that $L$ into the inversion returns $T_b = 292.412\ \mathrm{K}$, not
$300\ \mathrm{K}$: **the brightness temperature is a radiance in temperature
units, and it is systematically below the surface temperature whenever
$\varepsilon < 1$.**

### 3.4 The emissivity error propagated to temperature

Suppose the true surface has emissivity $\varepsilon_{\rm t}$ and temperature
$T_{\rm t}$, and the analyst retrieves temperature from the same radiance using
an assumed emissivity $\varepsilon_{\rm a}$:

$$L = \varepsilon_{\rm t}B_\lambda(T_{\rm t})
= \varepsilon_{\rm a}B_\lambda(T_{\rm a}).$$

Take logarithms of $L = \varepsilon B_\lambda(T)$ and differentiate at fixed $L$:

$$0 = \mathrm{d}\ln\varepsilon + \frac{\partial \ln B_\lambda}{\partial T}\mathrm{d}T.$$

In the Wien limit ($e^{hc/\lambda k_BT}\gg1$)
$\ln B_\lambda \approx \text{const} - hc/(\lambda k_B T)$, so
$\partial\ln B_\lambda/\partial T = hc/(\lambda k_B T^{2})$ and

$$\boxed{\;\frac{\mathrm{d}T}{\mathrm{d}\ln\varepsilon}
= \frac{\lambda k_B T^{2}}{hc}\;}.$$

The quantity $\lambda k_B T^{2}/(hc)$ is a temperature, and it is the *sensitivity
of the retrieval to fractional emissivity errors*.

*Numerical check.* At $\lambda = 10.8\ \mathrm{\mu m}$, $T = 300\ \mathrm{K}$:

$$\frac{\lambda k_B T^{2}}{hc}
= \frac{10.8\times10^{-6}\times1.380649\times10^{-23}\times9.0\times10^{4}}
{1.9864459\times10^{-25}} = 67.56\ \mathrm{K}.$$

So a $1\%$ emissivity error (a $\ln\varepsilon$ change of $0.01$) moves the
retrieved temperature by about $0.68\ \mathrm{K}$. For the soil-like surface,
using $\varepsilon_{\rm a} = 0.95$ instead of $\varepsilon_{\rm t} = 0.890$ gives

$$\Delta T \approx 67.56\ln\!\left(\frac{0.890}{0.95}\right)
= 67.56\times(-0.0652) = -4.41\ \mathrm{K},$$

against the demonstration's measured $-4.29\ \mathrm{K}$; the $2.7\%$ difference
is the Wien approximation. The same formula predicts $-6.6\ \mathrm{K}$ for the
vegetation-like surface ($\varepsilon_{\rm t} = 0.860$) against a measured
$-6.50\ \mathrm{K}$, and $+3.2\ \mathrm{K}$ for water-like
($\varepsilon_{\rm t} = 0.995$) against a measured $+3.12\ \mathrm{K}$.

### 3.5 Band depth: turning a shape into a number

Absorption features are summarised by a **continuum removal** and a band depth.
Fit a straight-line (or convex-hull) continuum across the feature, then

$$D = 1 - \frac{R_{\rm feature}}{R_{\rm continuum}},$$

where $R$ is the reflectance. This is the quantity that later lessons in this
folder feed into mineral and vegetation indices. Its weakness is stated here once:
$D$ depends on the *continuum endpoints you choose*, so two analysts with
different endpoints obtain different depths from the same spectrum. The
demonstration's synthetic features have depths chosen in the code; the recovered
band depth is only comparable between spectra processed with the *same* endpoint
rule.

## 4. Physical interpretation

- **Reflectance is a ratio, so it is scale-invariant** to a common gain, but not
  to an additive path radiance. That asymmetry is why band ratios work (they
  cancel multiplicative terms) and why haze must still be corrected.
- **Emissivity and reflectance are one measurement** in the opaque thermal
  infrared. Choosing which to report is a choice about which error model you
  prefer, not about which physics you use.
- **The brightness temperature is always a lower bound** on the surface
  temperature when $\varepsilon < 1$ and the atmosphere is transparent, because
  a real surface emits less than a blackbody at the same temperature.
- **A spectral signature is illumination-dependent.** The demonstration gives the
  soil-like surface a broadband albedo of $0.395$ under a synthetic $5772\
  \mathrm{K}$ illumination and $0.416$ under a reddened $4500\ \mathrm{K}$ one —
  same surface, different "signature", because albedo is a weighted integral and
  the weight changed. Single band reflectances are far less illumination-sensitive
  than broadband albedos, which is why narrow bands are preferred for material
  discrimination.
- **Geometry is a parameter, not a nuisance.** The synthetic forward-scattering
  surface reports a directional reflectance $35\%$ above its hemispherical
  reflectance at nadir viewing. Reporting the former as the latter is a
  $35\%$ systematic error.

## 5. Assumptions and regime of validity

1. **Local thermodynamic equilibrium** — required for Kirchhoff's law. It holds
   in the lower atmosphere and at the surface; it fails in emission-line regions
   high in the atmosphere, which is outside this folder's scope.
2. **Opaque surface** for $\varepsilon = 1-\rho$. A translucent surface needs
   $1-\rho-\tau$, and the demonstration's "clear water" row shows the identity
   breaking if you forget $\tau$.
3. **Lambertian reflection** for $L = \rho E/\pi$. Real surfaces are
   anisotropic; the relation is exact only for the hemispherical integral of an
   isotropic reflector.
4. **Known, uniform illumination spectrum.** The broadband albedo is a weighted
   mean and its value moves with the weight (Section 3.5 and the demonstration).
5. **Grey, isothermal surface over the band** if a single emissivity is used for a
   broad band. Real emissivity varies across a band; the error it causes is the
   subject of [17-02-03](../02-optical-and-thermal-remote-sensing/03-thermal-infrared.md).
6. **No atmosphere** for everything in Sections 2.4–3.4. With an atmosphere the
   retrieved quantity is a top-of-atmosphere reflectance or brightness
   temperature, and the correction in [17-01-03](03-atmospheric-effects.md) is
   mandatory before any material interpretation.

## 6. Units and dimensional analysis

| Expression | Unit arithmetic | Result |
|---|---|---|
| $f_r = \mathrm{d}L/\mathrm{d}E$ | $\mathrm{W\,m^{-2}\,sr^{-1}}/\mathrm{W\,m^{-2}}$ | $\mathrm{sr^{-1}}$ |
| $\rho_{\rm dh} = \int f_r\cos\theta\,\mathrm{d}\Omega$ | $\mathrm{sr^{-1}}\cdot\mathrm{sr}$ | dimensionless |
| $L = \rho E/\pi$ | $1\cdot\mathrm{W\,m^{-2}}/\mathrm{sr}$ | $\mathrm{W\,m^{-2}\,sr^{-1}}$ |
| $\varepsilon = L_{\rm em}/B_\lambda$ | $\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$ ratio | dimensionless |
| $\mathrm{d}T/\mathrm{d}\ln\varepsilon$ | $\mathrm{m}\cdot\mathrm{J\,K^{-1}}\cdot\mathrm{K^{2}}/(\mathrm{J\,s}\cdot\mathrm{m\,s^{-1}})$ | K |

The last row is the one to check by hand: the numerator is
$[\mathrm{m}][\mathrm{J\,K^{-1}}][\mathrm{K^{2}}] = \mathrm{J\,m\,K}$ and the
denominator is $[\mathrm{J\,m}]$, so the ratio is a temperature. ✔

## 7. Worked examples

### Example 1 — reflectance to radiance to reflectance again

A SYNTHETIC surface has $\rho_{\rm red} = 0.363$ and is illuminated by
$E = 800\ \mathrm{W\,m^{-2}}$. A sensor at the surface measures
$L = 92.0\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$.

1. Lambertian prediction: $L = \rho E/\pi = 0.363\times800/3.14159 = 92.38$.
2. Invert the measurement: $\rho = \pi L/E = 3.14159\times92.0/800 = 0.3613$.
3. The difference, $-0.0017$ (about $-0.5\%$), is entirely in the assumed
   irradiance and the measurement; note that a $1\%$ error in $E$ is a $1\%$ error
   in $\rho$, because the relation is linear.

### Example 2 — emissivity error to temperature error

The vegetation-like surface has $\varepsilon_{\rm t} = 0.860$ at
$10.8\ \mathrm{\mu m}$ and $T_{\rm t} = 300\ \mathrm{K}$. An analyst assumes
$\varepsilon_{\rm a} = 0.95$.

1. Sensitivity: $\lambda k_BT^{2}/(hc) = 67.56\ \mathrm{K}$ (Section 3.4).
2. $\Delta T = 67.56\ln(0.860/0.95) = 67.56\times(-0.0998) = -6.74\ \mathrm{K}$
   (analytic), against $-6.50\ \mathrm{K}$ measured by the demonstration.
3. Conclusion: a $10\%$ emissivity error costs about $6.5\ \mathrm{K}$ of
   surface temperature — larger than most real thermal contrasts this folder
   cares about. **Emissivity is not a correction; it is a first-order term.**

### Example 3 — albedo under two illuminations

Same soil-like reflectance curve, two synthetic illumination spectra:

| Illumination | Broadband albedo |
|---|---|
| $5772\ \mathrm{K}$ (solar-like) | $0.395$ |
| $4500\ \mathrm{K}$ (reddened) | $0.416$ |

The reflectance curve did not change; the *weight* did. Because the soil-like
reflectance rises toward the near-infrared, a reddened (infrared-rich)
illumination raises the weighted mean. A reported albedo without the illumination
spectrum it was computed against is therefore not a well-defined quantity, and
the correct practice is to report either the narrow-band reflectances or the
albedo with its weight stated.

## 8. Python demonstration

`code/reflectance_emissivity_demo.py` prints, with units:

1. the energy-conservation identity $\rho+\tau+\alpha=1$ on three synthetic
   surfaces;
2. notional band means for the three synthetic reflectance curves, with the
   Gaussian feature parameters listed;
3. broadband albedos ($0.395$, $0.240$, $0.032$) under a synthetic solar
   spectrum, and ($0.416$, $0.303$, $0.023$) under a reddened one;
4. Lambertian radiances for a stated $E = 800\ \mathrm{W\,m^{-2}}$ (red band:
   $92.382$, $34.809$, $11.049\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$);
5. emissivities from Kirchhoff ($0.890$, $0.860$, $0.995$);
6. brightness temperatures and the retrieval error for an assumed
   $\varepsilon = 0.95$ ($-4.29$, $-6.50$, $+3.12\ \mathrm{K}$);
7. the bidirectional-versus-hemispherical bias ($+35\%$ at nadir);
8. a forward-model check of the Planck inversion (closure to
   $\sim2\times10^{-16}$).

The script generates everything in code; it reads no files and uses no network.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/02-reflectance-and-emissivity-exercises.md`](./exercises/02-reflectance-and-emissivity-exercises.md)
and
[`exercises/02-reflectance-and-emissivity-solutions.md`](./exercises/02-reflectance-and-emissivity-solutions.md).

- **★** Compute $L$ for $\rho = 0.25$, $E = 1000\ \mathrm{W\,m^{-2}}$, and state
  the unit.
- **★** A surface has $\rho = 0.12$ and $\tau = 0.03$. Find $\alpha$ and
  $\varepsilon$.
- **★★** Derive the Lambertian $1/\pi$ and show that omitting it changes albedo
  by $3.14\times$.
- **★★** Compute the temperature bias of a $1\%$, $5\%$ and $10\%$ emissivity
  error at $10.8\ \mathrm{\mu m}$, $300\ \mathrm{K}$.
- **★★★** Show that the ratio of two band reflectances cancels a common gain but
  not an additive path radiance, and derive the residual error.

## Mastery checkpoint

Without notes: an opaque surface has $\rho = 0.14$ at $10.8\ \mathrm{\mu m}$.
**(a)** Compute its emissivity. **(b)** Compute the temperature error if an analyst
assumes $\varepsilon = 0.95$ while the true surface temperature is
$305\ \mathrm{K}$. **(c)** State why that error is systematic rather than random.
**(d)** Compute the Lambertian radiance for $\rho = 0.36$ and
$E = 900\ \mathrm{W\,m^{-2}}$.

## 10. Common pitfalls

1. **Forgetting the $1/\pi$.** Radiance to reflectance without it is wrong by
   $3.14\times$.
2. **Treating brightness temperature as surface temperature.** For
   $\varepsilon = 0.860$ that is a $9.8\ \mathrm{K}$ error before any atmospheric
   term.
3. **Using $\varepsilon = 1-\rho$ on a translucent surface** (vegetation canopies,
   water, snow in the visible). The $-\tau$ term is not optional.
4. **Reporting albedo without the illumination spectrum.** The same surface moves
   from $0.395$ to $0.416$ in the demonstration.
5. **Assuming Lambertian because the equation is convenient.** The synthetic
   anisotropic surface is $35\%$ off at nadir.
6. **Comparing band depths from different continuum endpoints.** A depth is
   defined relative to a chosen continuum, and the choice is part of the result.

## 11. Real-world applications

- **Vegetation monitoring.** Reflectance in the red and near-infrared, combined
  into an index, is the basis of the indices in
  [17-02-06](../02-optical-and-thermal-remote-sensing/06-vegetation-and-geobotany.md).
- **Land surface temperature.** Every operational product depends on an
  emissivity assumption, and Section 3.4 is why products report their emissivity
  source.
- **Mineral mapping.** Absorption band position and depth distinguish alteration
  minerals; the depth pipeline of Section 3.5 is the front end of
  [17-02-02](../02-optical-and-thermal-remote-sensing/02-hyperspectral.md).
- **Albedo products.** Used in climate and hydrology, they are weighted integrals
  and are only meaningful with the illumination model and angular model
  documented.
- **Calibration and validation.** Because reflectance is a ratio, a reflectance
  product can be validated against a reference panel at a site without absolute
  radiometry — but only if the panel's own reflectance and the geometry are
  known.

## 12. Further reading

- *Physical Principles of Remote Sensing* (Rees) — reflectance, BRDF and
  emissivity in a single consistent notation.
- *Remote Sensing and Image Interpretation* (Lillesand and Kiefer) — the applied
  side of reflectance products.
- [02-10-04 Spectroscopy Principles for Remote Sensing](../../02-physics/10-optics-and-photometry/04-spectroscopy.md)
  — absorption features and band-depth measurement.
- [02-10-03 Radiative Transfer, Blackbody Radiation and Kirchhoff's Law](../../02-physics/10-optics-and-photometry/03-radiative-transfer.md)
  — Kirchhoff's law derived at the level of the radiative-transfer equation.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related modules

- [01 The Electromagnetic Spectrum and Sensing Windows](01-em-spectrum-remote-sensing.md) —
  the radiative quantities this lesson quantifies.
- [03 Atmospheric Attenuation, Scattering and Correction](03-atmospheric-effects.md) —
  removing the atmospheric terms from the sensor radiance.
- [17-02-01 Multispectral Imaging, Band Ratios and Indices](../02-optical-and-thermal-remote-sensing/01-multispectral-imaging.md) —
  what reflectance spectra become once they are reduced to a few bands.
- [17-02-03 Thermal Infrared: Land Surface Temperature and Heat Flow](../02-optical-and-thermal-remote-sensing/03-thermal-infrared.md) —
  emissivity in an operational temperature retrieval.

## 14. Self-assessment checklist

- [ ] I can write the BRDF and its units and integrate it to a reflectance.
- [ ] I can derive $L = \rho E/\pi$ and explain the $\pi$.
- [ ] I can apply Kirchhoff's law to an opaque and to a translucent body.
- [ ] I can invert the Planck function and verify my inversion by forward modelling.
- [ ] I can compute $\lambda k_BT^{2}/(hc)$ and use it to size an emissivity error.
- [ ] I can compute a spectrum-weighted albedo and say why the weight matters.
- [ ] I can explain the difference between directional and hemispherical reflectance.
