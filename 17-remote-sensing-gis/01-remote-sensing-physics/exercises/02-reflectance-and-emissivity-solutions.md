# Solutions — 17-01-02 Reflectance, Emissivity and Spectral Signatures

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Surfaces and bands are **SYNTHETIC**; the constants are exact.

Lesson: [02 Reflectance, Emissivity and Spectral Signatures](../02-reflectance-and-emissivity.md).

---

## ★1 — Lambertian radiance

$$L = \frac{\rho E}{\pi} = \frac{0.25\times1000}{3.14159}
= 79.58\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}.$$

**Unit check:** $1\cdot\mathrm{W\,m^{-2}}/\mathrm{sr}$ gives
$\mathrm{W\,m^{-2}\,sr^{-1}}$ (per unit wavelength, since the quantities were
spectral). ✔

---

## ★2 — Absorptance and emissivity

$$\alpha = 1 - \rho - \tau = 1 - 0.12 - 0.03 = 0.85.$$

By Kirchhoff's law in local thermodynamic equilibrium, $\varepsilon = \alpha$, so
$\varepsilon = 0.85$. Note that using the opaque formula
$\varepsilon = 1-\rho = 0.88$ would be wrong by $0.03$ — the transmitted fraction
is exactly the amount that is not available for absorption and therefore not
available for emission.

---

## ★3 — Brightness temperature

$$T_b = \frac{hc}{\lambda k_B}\,
\frac{1}{\ln\!\left(1 + \dfrac{2hc^{2}}{\lambda^{5}L}\right)}.$$

With $\lambda = 10.8\times10^{-6}\ \mathrm{m}$, $L = 8.00\times10^{6}$:

$$\frac{2hc^{2}}{\lambda^{5}L}
= \frac{1.19104\times10^{-16}}{(10.8\times10^{-6})^{5}\times8.00\times10^{6}}
= \frac{1.19104\times10^{-16}}{1.46933\times10^{-25}\times8.00\times10^{6}}
= \frac{1.19104\times10^{-16}}{1.17546\times10^{-18}} = 101.33.$$

$$\ln(1 + 101.33) = \ln(102.33) = 4.6283,\qquad
\frac{hc}{\lambda k_B} = \frac{1.9864459\times10^{-25}}
{10.8\times10^{-6}\times1.380649\times10^{-23}} = 1332.1\ \mathrm{K},$$
$$T_b = \frac{1332.1}{4.6283} = 287.8\ \mathrm{K}.$$

With $\varepsilon<1$ the surface emits less than a blackbody at the same
temperature, so the blackbody temperature matching that radiance is **below** the
true surface temperature: $T_b$ is a lower bound.

---

## ★4 — Deriving the $1/\pi$

For a Lambertian surface $f_r = f_0$ is constant. Reflected radiance is
$L_r = f_0 E$ (by the definition of the BRDF). Exitance is the radiance
integrated over the outward hemisphere:

$$M = \int_{2\pi} L_r\cos\theta_r\,\mathrm{d}\Omega_r
= L_r\int_0^{2\pi}\!\!\int_0^{\pi/2}\!\cos\theta_r\sin\theta_r\,
\mathrm{d}\theta_r\,\mathrm{d}\phi_r = L_r\,(2\pi)\left(\tfrac{1}{2}\right)
= \pi L_r.$$

Energy conservation requires the reflected exitance to equal the reflected
irradiance $\rho E$, hence $M = \rho E = \pi L_r$ and

$$L_r = \frac{\rho E}{\pi}, \qquad f_0 = \frac{\rho}{\pi}.$$

**Numerical consequence.** With $\rho = 0.363$ and $E = 800\ \mathrm{W\,m^{-2}}$:

$$L_{\rm correct} = \frac{0.363\times800}{\pi} = 92.44\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}},$$
$$L_{\rm no\ \pi} = 0.363\times800 = 290.4\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}.$$

The omission multiplies the radiance by exactly $\pi = 3.14159$ — a factor of
three, not a rounding.

---

## ★5 — Emissivity error to temperature error

$$\frac{\mathrm{d}T}{\mathrm{d}\ln\varepsilon} = \frac{\lambda k_BT^{2}}{hc}
= \frac{10.8\times10^{-6}\times1.380649\times10^{-23}\times300^{2}}
{6.62607015\times10^{-34}\times2.99792458\times10^{8}}
= 67.56\ \mathrm{K}.$$

For an assumed emissivity that is a factor $(1+\delta)$ too high,

$$\Delta T = 67.56\ln\!\left(\frac{1}{1+\delta}\right) = -67.56\ln(1+\delta).$$

| $\delta$ | $\Delta T$ (K) |
|---|---|
| $0.01$ | $-0.67$ |
| $0.05$ | $-3.30$ |
| $0.10$ | $-6.44$ |

A $10\%$ emissivity error is a $6.4\ \mathrm{K}$ temperature error, which is
larger than most of the land-surface-temperature contrasts a geothermal or
volcanic study is trying to measure.

---

## ★6 — Normalised difference index

$$I = \frac{R_{\rm NIR}-R_{\rm red}}{R_{\rm NIR}+R_{\rm red}}.$$

| Surface | $R_{\rm red}$ | $R_{\rm NIR}$ | $I$ |
|---|---|---|---|
| soil-like | 0.363 | 0.369 | $+0.008$ |
| vegetation-like | 0.137 | 0.473 | $+0.551$ |
| water-like | 0.043 | 0.014 | $-0.509$ |

**Interpretation.** The soil-like value is essentially zero because the soil's
reflectance is nearly flat across the red–NIR boundary: there is no red-edge
rise to detect. The vegetation-like value is strongly positive because of the
synthetic red edge (a logistic step at $0.70\ \mathrm{\mu m}$); this is the
feature that makes such indices useful for vegetation. The water-like value is
negative because its reflectance falls through the near-infrared. The index is a
*shape* descriptor, not a material identifier: a red-painted roof would also give
a negative value if its reflectance fell in the same way.

---

## ★7 — Illumination weight and albedo

Relative change:

$$\frac{0.416 - 0.395}{0.395} = +0.0532 = +5.3\%.$$

**Why the reddened illumination raises it.** The soil-like reflectance curve
*rises* toward the shortwave infrared (a logistic step at $1.30\ \mathrm{\mu m}$
plus a higher baseline), so it reflects infrared more than visible light. Reddening
the illumination — shifting its weight toward longer wavelengths, here from a
$5772\ \mathrm{K}$ to a $4500\ \mathrm{K}$ Planck spectrum — therefore moves the
weight onto the part of the spectrum the surface reflects most strongly. The
albedo is a weighted mean, and the weight changed. The same argument in reverse
explains why a blue-rich illumination *lowers* this surface's albedo.

---

## ★8 — Ratio algebra with an additive term

With $L_b = g\rho_b + \beta_b$,

$$R = \frac{L_2}{L_1} = \frac{g\rho_2 + \beta_2}{g\rho_1 + \beta_1}.$$

If $\beta_1 = \beta_2 = 0$, then $R = g\rho_2/(g\rho_1) = \rho_2/\rho_1$: the
gain cancels exactly, independently of its value.

With $\beta_1 = \beta_2 = \beta \ne 0$ (equal offsets),

$$R = \frac{g\rho_2 + \beta}{g\rho_1 + \beta}
= \frac{\rho_2 + \beta/g}{\rho_1 + \beta/g},$$

so the ratio equals the true reflectance ratio evaluated with an *offset*
$\beta/g$ added to both bands. The relative error is

$$\frac{R - \rho_2/\rho_1}{\rho_2/\rho_1}
= \frac{\rho_1 - \rho_2}{\rho_1}\cdot
\frac{\beta/g}{\rho_2 + \beta/g},$$

which grows linearly in the offset-to-reflectance ratio $\beta/(g\rho)$ and is
largest for a large contrast $\rho_1-\rho_2$.

With *unequal* offsets the gain does **not** cancel:

$$R = \frac{g\rho_2 + \beta_2}{g\rho_1 + \beta_1},$$

and $R$ depends on $g$ through the ratio $\beta_b/(g\rho_b)$.

**Condition for $1\%$ usability.** Requiring the offset term to perturb each band
by less than $1\%$ of its surface signal gives

$$\frac{\beta_b}{g\rho_b} < 0.01,
\qquad\text{i.e.}\qquad
\frac{\beta_b}{\rho_b} < 0.01\,g .$$

In radiometric terms: the path radiance must be below about $1\%$ of the
surface radiance, band by band. That is a strong requirement in the visible,
where path radiance is largest — which is why ratios are applied after
atmospheric correction, not instead of it.

---

## ★9 — Specifying a hemispherical reflectance measurement

**Measurement.** A goniometer-mounted radiometer and a reference panel, with the
illumination direction fixed and *measured* (a collimated source with known
zenith and azimuth), and the sensor stepped through at least five view zenith
angles covering the range that the application needs (for a satellite cross-check,
include the satellite's view zenith) plus, where possible, at least three relative
azimuths. At each geometry record the radiance from the target and from the
reference panel; the panel's directional reflectance is known from its
calibration.

**Processing.**

1. Convert each target radiance to a directional reflectance using the panel,
   $\rho_{\rm dir}(\theta_r) = \rho_{\rm panel}\,\dfrac{L_{\rm target}(\theta_r)}
   {L_{\rm panel}(\theta_r)}$, with both measured at the same geometry.
2. Fit a BRDF model (at minimum a kernel-driven linear model with isotropic,
   geometric and volumetric kernels) to the measured $\rho_{\rm dir}$ set.
3. **Integrate the fitted BRDF over the view hemisphere** to obtain
   $\rho_{\rm dh}(\theta_i)$:
   $\rho_{\rm dh} = \int_{2\pi} f_r\cos\theta_r\,\mathrm{d}\Omega_r$.
4. For a bihemispherical albedo, additionally weight the incident hemisphere by
   the illumination's angular distribution, or use the actual direct-plus-diffuse
   illumination of the site.
5. Report the integral with an uncertainty from the model fit's residuals and the
   panel's calibration uncertainty, propagated through the integration step.

**Two largest error sources.**

- **Insufficient angular sampling.** The integral is over the *whole* hemisphere;
  if measurements stop at $\theta_r = 60^\circ$, the contribution from
  $60^\circ$–$90^\circ$ is extrapolated by the model, and for a surface with a
  strong forward or backward lobe that extrapolation dominates the error near the
  horizon (the integrand has a $\cos\theta\sin\theta$ weight that peaks at
  $45^\circ$ but does not vanish at $90^\circ$ for a peaked BRDF).
- **Illumination knowledge.** The hemispherical reflectance is defined relative to
  a specified incident distribution; an unmeasured diffuse-sky fraction changes
  the reported albedo. This is the same weight-sensitivity demonstrated in the
  lesson, where the synthetic soil-like albedo moved from $0.395$ to $0.416$ when
  the weight changed.
