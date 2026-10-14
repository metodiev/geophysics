# Solutions — 17-01-01 The Electromagnetic Spectrum and Sensing Windows

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All spectra are **SYNTHETIC** model output; the physical constants are exact.

Lesson: [01 The Electromagnetic Spectrum and Sensing Windows](../01-em-spectrum-remote-sensing.md).

---

## ★1 — Frequency and photon energy

$$\nu = \frac{c}{\lambda} = \frac{2.99792458\times10^{8}}{3.70\times10^{-6}}
= 8.1025\times10^{13}\ \mathrm{Hz} = 81.02\ \mathrm{THz}.$$

$$E = \frac{hc}{\lambda} = \frac{1.9864459\times10^{-25}}{3.70\times10^{-6}}
= 5.3688\times10^{-20}\ \mathrm{J}
= \frac{5.3688\times10^{-20}}{1.602176634\times10^{-19}} = 0.3351\ \mathrm{eV}.$$

**Unit check:** $\mathrm{J\,s}\cdot\mathrm{m\,s^{-1}}/\mathrm{m} = \mathrm{J}$. ✔

---

## ★2 — A cold cloud top

$$\lambda_{\max} = \frac{b}{T} = \frac{2.897771955\times10^{-3}}{220}
= 1.3172\times10^{-5}\ \mathrm{m} = 13.172\ \mathrm{\mu m}.$$

$$M = \sigma T^{4} = 5.670374419\times10^{-8}\times220^{4}
= 5.670374419\times10^{-8}\times2.34256\times10^{9}
= 132.8\ \mathrm{W\,m^{-2}}.$$

Ratio to the Earth at $288\ \mathrm{K}$: $\sigma T^{4}$ scales as $T^{4}$
(or $220^{4}/288^{4} = 0.3405$), so $M/M_{\rm Earth} = 132.8/390.1 = 0.340$.
A cold cloud therefore radiates about one third as much per unit area, which is
why it appears bright in a thermal *image* only when expressed as a brightness
temperature (low radiance ↔ low temperature), not when expressed as radiance.

---

## ★3 — Optical depth and transmittance

Optical depth $\tau = \int \kappa\,\mathrm{d}z$ (dimensionless) and transmittance
$T = e^{-\tau}$.

- $T = 0.50 \Rightarrow \tau = -\ln 0.50 = 0.693$.
- $\tau = 3 \Rightarrow T = e^{-3} = 0.0498$ (about 5%).

---

## ★4 — Round trip at $2.70\ \mathrm{\mu m}$

Reflected sunlight traverses the atmosphere on the way down and again on the way
up, so

$$T_{\rm round} = T^{2} = 0.015^{2} = 2.25\times10^{-4}.$$

Only $0.0225\%$ of the surface-reflected radiance reaches the top of the
atmosphere. **The band is unusable for surface reflectance**, no matter how
diagnostic the surface feature is. (It could still be a useful *emission* or
*sounding* band, where the atmosphere itself is the target.)

---

## ★5 — Which band loses more to the atmosphere

- Reflected solar, two-way: $T^{2} = 0.773^{2} = 0.5975$, so $40.2\%$ is lost.
- Thermal, one-way: $T = 0.498$, so $50.2\%$ is lost.

The **thermal** band loses more fractional signal here, because a single pass in
the $11\ \mathrm{\mu m}$ region of this synthetic model is dirtier than the
*squared* visible transmittance. The general rule is subtler than "two passes is
worse": what matters is each band's optical depth. Note also that for the thermal
case the atmosphere partly re-emits toward the sensor, so the naive "$T$ of the
surface signal is lost" statement is an upper bound on the loss.

---

## ★6 — Rayleigh weights

Reference $\lambda_0 = 0.55\ \mathrm{\mu m}$; weight $= (\lambda/\lambda_0)^{-4}$.

- $0.45\ \mathrm{\mu m}$: $(0.45/0.55)^{-4} = (0.81818)^{-4} = 2.232$.
- $0.65\ \mathrm{\mu m}$: $(0.65/0.55)^{-4} = (1.18182)^{-4} = 0.5126$.

Ratio blue/red $= 2.232/0.5126 = 4.35$.

**Consequence.** The atmosphere adds roughly $4.35\times$ more scattered
("path") radiance in a blue band than in a red band. A blue-band surface
reflectance product therefore needs a larger and more carefully modelled
atmospheric correction than a red-band one, and topographic or adjacency effects
are correspondingly stronger in blue.

---

## ★7 — A $400\ \mathrm{K}$ source at $10\ \mathrm{\mu m}$

$$B_\lambda(T) = \frac{2hc^{2}}{\lambda^{5}}\frac{1}{e^{hc/(\lambda k_B T)}-1}.$$

For $T = 400\ \mathrm{K}$, $\lambda = 10^{-5}\ \mathrm{m}$:

$$\frac{hc}{\lambda k_B T} = \frac{1.9864459\times10^{-25}}
{10^{-5}\times1.380649\times10^{-23}\times400} = 3.5969,$$
$$e^{3.5969} - 1 = 36.4865 - 1 = 35.4865,$$
$$B_\lambda = \frac{1.19104\times10^{9}}{35.4865} = 3.356\times10^{7}\
\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}.$$

For $T = 288\ \mathrm{K}$ the same expression gives
$8.114\times10^{6}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$ (the demonstration's
value). The ratio is $3.356\times10^{7}/8.114\times10^{6} = 4.14$.

So a modestly warm surface at $400\ \mathrm{K}$ is about four times brighter in
this band than the ambient Earth. That sensitivity, not the absolute value, is
what makes a warm anomaly detectable against a background.

---

## ★8 — A gain-invariant two-band ratio

Define, with $\rho_a$ and $\rho_b$ the reflectances in bands $a$ and $b$,

$$I = \frac{\rho_b - \rho_a}{\rho_b + \rho_a}, \qquad -1 \le I \le +1,$$

(the normalised difference form). Under a multiplicative gain
$\rho \mapsto g\rho$ in *both* bands,

$$I' = \frac{g\rho_b - g\rho_a}{g\rho_b + g\rho_a}
= \frac{g(\rho_b-\rho_a)}{g(\rho_b+\rho_a)} = I.$$

**Invariance proved.** The index is unchanged by any factor common to both
bands, which covers sensor gain and a uniform change in illumination.

**Assumption that the invariance needs, and where it fails.** The index is
invariant only if the *atmosphere* acts multiplicatively and equally on the two
bands. In reality the sensor radiance is
$L_b = L_{\rm path,b} + \rho_b E_b T_b/\pi$: the additive path radiance
$L_{\rm path,b}$ and the band-dependent transmittance $T_b$ both differ between
bands. Adding an offset $\beta_b$ to band $b$ alone,
$\rho_b \mapsto g\rho_b + \beta_b$, breaks the invariance, and the residual error
grows exactly as the ratio $\beta_b/\rho_b E_b$ grows. The index must therefore
be applied **after** atmospheric correction, or at least after a haze
correction that removes the additive term.

---

## ★9 — Albedo sensitivity of the effective temperature

$$T_{\rm eff}(A) = \left[\frac{S(1-A)}{4\sigma}\right]^{1/4}
\;\Rightarrow\;
\frac{\partial T_{\rm eff}}{\partial A}
= -\frac{1}{4}\,\frac{T_{\rm eff}}{1-A}.$$

At $A = 0.30$, $T_{\rm eff} = 254.6\ \mathrm{K}$:

$$\frac{\partial T_{\rm eff}}{\partial A}
= -\frac{254.6}{4\times0.70} = -90.9\ \mathrm{K\ per\ unit}\ A.$$

For $\Delta A = 0.01$: $\Delta T_{\rm eff} = -0.909\ \mathrm{K}$.

**Why the surface need not follow.** The surface temperature is set by the
balance *including* the greenhouse effect, which depends on the atmospheric
composition and on the vertical temperature profile, and it changes as the
surface warms (water vapour, lapse rate). A $0.9\ \mathrm{K}$ change in the
radiating temperature is the radiative-forcing-only answer; the realised surface
change includes feedbacks and is generally larger for the same forcing.
