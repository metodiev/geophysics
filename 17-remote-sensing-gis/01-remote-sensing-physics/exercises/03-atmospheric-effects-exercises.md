# Exercises — 17-01-03 Atmospheric Attenuation, Scattering and Correction

Attempt these before reading the
[solutions](./03-atmospheric-effects-solutions.md). The lesson is
[03 Atmospheric Attenuation, Scattering and Correction](../03-atmospheric-effects.md).
All atmospheres are **SYNTHETIC** teaching models.

Useful values from the lesson's demonstration (all synthetic): vertical optical
depth at $0.55\ \mathrm{\mu m}$, $\tau_{\rm vert} = 0.250$; sun zenith $30°$,
view nadir unless stated; $E_{\rm sun} = 800\ \mathrm{W\,m^{-2}\,\mu m^{-1}}$;
$L_{\rm path} = 17.4587$, $L = 62.0365\ \mathrm{W\,m^{-2}\,sr^{-1}\,\mu m^{-1}}$;
true surface reflectance $\rho = 0.300$.

## ★ Foundational

**★1.** With $\tau_{\rm vert} = 0.35$, compute the transmittance at zenith angles
$0°$, $45°$ and $70°$ using the plane-parallel air mass.

**★2.** Compute the round-trip transmittance for a sun zenith of $45°$ and a
sensor view zenith of $30°$, with $\tau_{\rm vert} = 0.250$.

**★3.** State in one sentence why transmittance is a product of two one-way
factors for reflected solar radiation but a single factor for emitted thermal
radiation.

## ★★ Applied

**★★4.** Derive $\delta\rho/\rho \approx -(m_\downarrow+m_\uparrow)\delta\tau$ and
evaluate it for a $5\%$ error on $\tau_{\rm vert} = 0.250$ with sun $30°$ and view
nadir.

**★★5.** A dark-object estimate of path radiance is $20\%$ too low. Using the
lesson's numbers, compute the retrieved reflectance and the percentage error.

**★★6.** The Ångström exponent is estimated from two wavelengths. Show that a
$2\%$ relative error in the ratio of the two optical depths produces
$\delta\alpha \approx 0.12$ for the pair $(0.55, 0.65)\ \mathrm{\mu m}$, and state
whether the estimator is unbiased in the absence of such errors.

**★★7.** Using the lesson's thermal budget, compute the retrieved surface
temperature (a) with a blackbody surface and no atmosphere, (b) with the
emissivity known and no atmosphere, and (c) with $\tau$ and the atmospheric up
term modelled but the reflected-sky term ignored. State which neglect produces
the largest bias and explain why the no-atmosphere cases look deceptively good.

## ★★★ Research-oriented

**★★★8.** Derive
$\mathbb{E}[\rho_{\rm ret}/\rho_{\rm true}]
= \exp\left(\tfrac12(\tau m_{\rm round}\sigma_u)^{2}\right)$
for a centred Gaussian fractional uncertainty $\sigma_u$ in the optical depth, and
evaluate the bias and spread for $\sigma_u = 0.20$. Explain in two sentences why
this matters for a decadal reflectance composite.

**★★★9.** Design a dark-object calibration procedure for a new sensor: state how
you select the dark objects, how you transfer the estimate to the rest of the
scene, how you validate it, and the uncertainty you can defend. Then state the
reflectance error your uncertainty implies for a target with
$\rho = 0.30$. A specification that could not be executed is a failed answer.
