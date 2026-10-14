# Solutions — 17-01-03 Atmospheric Attenuation, Scattering and Correction

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> The atmosphere is a **SYNTHETIC** teaching model.

Lesson: [03 Atmospheric Attenuation, Scattering and Correction](../03-atmospheric-effects.md).

Recall $T = \exp(-\tau_{\rm vert}\sec\theta)$, $m_{\rm round} = \sec\theta_{\rm sun}
+ \sec\theta_{\rm view}$, and
$\rho = \pi(L-L_{\rm path})/(E_{\rm sun}T_\downarrow T_\uparrow)$.

---

## ★1 — Transmittance at three zenith angles

With $\tau_{\rm vert} = 0.35$:

| $\theta$ | $m=\sec\theta$ | $\tau_{\rm slant}$ | $T = e^{-\tau_{\rm slant}}$ |
|---|---|---|---|
| $0°$ | 1.000 | 0.350 | 0.7047 |
| $45°$ | 1.414 | 0.495 | 0.6096 |
| $70°$ | 2.924 | 1.023 | 0.3594 |

So more than half the signal is lost at a $70°$ zenith angle even though the
vertical optical depth is only $0.35$.

---

## ★2 — Round trip, sun $45°$, view $30°$

$$T_\downarrow = e^{-0.250\times1.41421} = e^{-0.35355} = 0.7022,$$
$$T_\uparrow = e^{-0.250\times1.15470} = e^{-0.28868} = 0.7493,$$
$$T_\downarrow T_\uparrow = 0.7022\times0.7493 = 0.5261.$$

---

## ★3 — One pass or two

Reflected solar radiation passes through the atmosphere **on the way down to the
surface and again on the way up**, so its surface contribution is multiplied by
the product of two transmittances. Thermal radiance **originates at the surface**
and passes through the atmosphere only once on its way up (the atmosphere then
also adds its own emitted radiance, which is a separate additive term).

---

## ★4 — Reflectance sensitivity to optical depth

From $\rho = \pi(L-L_{\rm path})/(E_{\rm sun}T_\downarrow T_\uparrow)$ and
$T_\downarrow T_\uparrow = \exp[-\tau(m_\downarrow+m_\uparrow)]$, taking
logarithms:

$$\ln\rho = \text{const} - \tau\left(m_\downarrow+m_\uparrow\right)
\;\Longrightarrow\;
\frac{\partial\ln\rho}{\partial\tau} = -(m_\downarrow+m_\uparrow),
\qquad
\frac{\delta\rho}{\rho} \approx -(m_\downarrow+m_\uparrow)\delta\tau.$$

With sun $30°$ and view nadir: $m_\downarrow = 1.1547$,
$m_\uparrow = 1.0000$, so $m_{\rm round} = 2.1547$. For a $5\%$ error,
$\delta\tau = 0.01250$:

$$\frac{\delta\rho}{\rho} = -2.1547\times0.01250 = -0.0269 = -2.7\%.$$

The correction is **amplified** by the round-trip air mass, which exceeds $2$
whenever the Sun is not at zenith.

---

## ★5 — Path radiance $20\%$ too low

$$L_{\rm path}^{\rm est} = 0.80\times17.4587 = 13.9670,$$
$$T_\downarrow T_\uparrow = 0.5835,\quad
E_{\rm sun}T_\downarrow T_\uparrow = 800\times0.5835 = 466.82,$$
$$\rho_{\rm ret} = \frac{\pi\left(62.0365-13.9670\right)}{466.82}
= \frac{151.01}{466.82} = 0.3235.$$

Error: $(0.3235-0.3000)/0.3000 = +7.8\%$. An under-estimate of the path radiance
leaves too much radiance attributed to the surface, so the reflectance comes out
too **high** — the sign follows directly from the additive term in the numerator.

---

## ★6 — Ångström-exponent sensitivity

$$\alpha = -\frac{\ln\left(\tau_{\rm aer}(\lambda_1)/\tau_{\rm aer}(\lambda_2)\right)}
{\ln(\lambda_1/\lambda_2)},
\qquad
\ln\!\left(\frac{0.65}{0.55}\right) = 0.16705.$$

Differentiating with respect to the log-ratio (which is dimensionless),
$\delta\alpha = \delta\left(\text{log-ratio}\right)/\ln(\lambda_2/\lambda_1)$.
A $2\%$ relative error in the ratio is a $\delta(\text{log-ratio}) = 0.02$, so

$$\delta\alpha = \frac{0.02}{0.16705} = 0.120.$$

**Bias in the absence of errors:** the estimator is *exactly* the exponent for a
pure power law, so it is unbiased for that model (the demonstration recovers
$1.3000$ from both wavelength pairs). In reality the aerosol optical depth is not
a perfect power law, and that model error — not the algebra — is the accuracy
limit.

---

## ★7 — Thermal retrievals under four assumed models

True state: $T_s = 300\ \mathrm{K}$, $\varepsilon = 0.95$,
$\tau = 0.85$, $T_a = 280\ \mathrm{K}$ at $10.8\ \mathrm{\mu m}$. The sensor
radiance is $L = 9.1591\times10^{6}\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$, built
from a surface emission term $\varepsilon B(T_s) = 9.1859\times10^{6}$
($100.3\%$ of $L$), a reflected-sky term
$\tau(1-\varepsilon)B(T_a) = 2.9828\times10^{5}$ ($3.26\%$), a transmittance
reduction of the surface term of $1.3779\times10^{6}$ ($15.0\%$), and an
atmospheric up term $(1-\tau)B(T_a) = 1.0528\times10^{6}$ ($11.49\%$).

| Model | Inversion used | $T$ (K) | Bias (K) |
|---|---|---|---|
| (a) blackbody, no atmosphere | $T = B^{-1}(L)$ | 296.422 | $-3.58$ |
| (b) $\varepsilon$ known, no atmosphere | $T = B^{-1}(L/\varepsilon)$ | 299.805 | $-0.20$ |
| (c) $\tau$ and up term, no sky term | $T = B^{-1}\!\left(\frac{L-L_{\rm up}}{\tau\varepsilon}\right)$ | 302.523 | $+2.52$ |
| (d) full | $T = B^{-1}\!\left(\frac{(L-L_{\rm up})/\tau-(1-\varepsilon)B(T_a)}{\varepsilon}\right)$ | 300.000 | $0.00$ |

**Largest bias:** (a), the blackbody no-atmosphere inversion, at $-3.58\ \mathrm{K}$
— but the important observation is that (b) is deceptively accurate. The
atmospheric up term *adds* $11.49\%$ of the radiance while the transmittance
factor *removes* $15.0\%$ of the surface term, and at these parameter values the
two effects nearly cancel. Model (b) is therefore right for the wrong reason: it
will break as soon as the atmosphere becomes more opaque ($\tau$ smaller, so the
up term grows while the surface term shrinks), the surface temperature changes, or
the emissivity changes. Model (c) shows that the reflected-sky term alone, when
omitted, biases the retrieval $+2.52\ \mathrm{K}$ **high**.

---

## ★8 — Convexity bias from optical-depth noise

Write $\tau_{\rm assumed} = \tau(1+u)$ with $u\sim N(0,\sigma_u^{2})$. The
retrieved reflectance is

$$\rho_{\rm ret} = \rho_{\rm true}\,
\exp\!\left[\tau m_{\rm round}\,u\right],$$

so $\ln(\rho_{\rm ret}/\rho_{\rm true})$ is Gaussian with standard deviation
$\sigma_{\ln\rho} = \tau m_{\rm round}\sigma_u$. Hence

$$\mathbb{E}\!\left[\frac{\rho_{\rm ret}}{\rho_{\rm true}}\right]
= \exp\!\left(\tfrac{1}{2}\sigma_{\ln\rho}^{2}\right) > 1,
\qquad
\mathrm{sd}\!\left[\frac{\rho_{\rm ret}}{\rho_{\rm true}}\right]
= \sqrt{e^{\sigma_{\ln\rho}^{2}}-1}.$$

With $\tau = 0.250$, $m_{\rm round} = 2.1547$, $\sigma_u = 0.20$:

$$\sigma_{\ln\rho} = 0.250\times2.1547\times0.20 = 0.10774,$$
$$\text{bias} = e^{0.10774^{2}/2}-1 = e^{0.00580}-1 = +0.58\%,$$
$$\text{relative spread} = \sqrt{e^{0.01161}-1} = 10.80\%.$$

(Twice the uncertainty of the lesson's $10\%$ case gives roughly twice the spread,
$10.80\%$ against $5.37\%$, and four times the bias, $+0.58\%$ against
$+0.145\%$, because the bias is second order in $\sigma_u$.)

**Why it matters for a decadal composite.** Averaging many scenes does not cancel
this bias — it *is* the mean. If each scene's correction carries an independent
$10\%$–$20\%$ optical-depth uncertainty, the composite is biased high by a few
tenths of a per cent relative to the truth, and, worse, the bias depends on the
scene's air mass, so a composite built from data acquired at different solar
zenith angles acquires a spurious seasonal cycle. Consistency of the correction
across the record matters more than absolute accuracy for trend detection.

---

## ★9 — Designing a dark-object calibration

**Selection.** Identify candidate dark objects from the scene's own histogram
instead of assuming a material: (i) build a histogram of the blue-band
reflectance after a first-guess correction; (ii) take the lowest percentile as
candidates, excluding water if the study target is land; (iii) require spatial
compactness (a few hundred contiguous pixels) to avoid single-pixel
anomalies; (iv) require temporal stability across the acquisitions used. The
assumption being made explicit — and testable — is that at least one object in
the scene reflects essentially nothing, so its measured radiance *is* the path
radiance.

**Transfer within the scene.** Dark-object subtraction assumes the path radiance
is uniform across the scene, so a single offset is subtracted from every pixel.
That assumption is the weak point: with a horizontal aerosol gradient the
procedure must be applied on tiles, with blending between tile offsets.

**Validation.** Compare against (a) an independent atmospheric model driven by
the scene's own geometry, (b) a pseudo-invariant bright target whose reflectance
should be unchanged between acquisitions, and (c) any ground reflectance
measurement available. A correction that agrees with (a) and (b) but not (c) has an
unmodelled surface or instrument issue, not an atmospheric one.

**Defensible uncertainty.** Assume a $5\%$ relative uncertainty in the estimated
path radiance (achievable on a clear scene, optimistic on a hazy one). From the
retrieval formula with $L-L_{\rm path} = 44.5778$ and
$L_{\rm path} = 17.4587$:

$$\delta\rho = \frac{\pi\,\delta L_{\rm path}}{E_{\rm sun}T_\downarrow T_\uparrow}
= \frac{\pi\times0.05\times17.4587}{466.82} = 0.00587,$$

a $+1.96\%$ error on a true $\rho = 0.300$, i.e. $\rho = 0.300\pm0.006$ at one
standard deviation. Combining with the optical-depth uncertainty of ★4 (a
$2.7\%$ reflectance error for a $5\%$ optical-depth error) gives a total
uncertainty of about $\sqrt{1.96^{2}+2.7^{2}} = 3.3\%$ — so
$\rho = 0.300\pm0.010$. **Any reflectance product quoted to more than two
significant figures without an accompanying uncertainty of this order is
over-claiming.**
