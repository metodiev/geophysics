---
id: 26-03-05
title: "Formula Sheet: Electromagnetics and Electrical Methods"
level: advanced
prereqs: []
estimated_minutes: 35
tags: [reference, formulas, electromagnetics, resistivity]
---

# Formula Sheet: Electromagnetics and Electrical Methods

Maxwell's equations, the diffusion and wave regimes they imply, the
magnetotelluric impedance, the geometric factors of the DC arrays, and the
GPR formulas. Every entry states whether it assumes the **diffusive**
(low-frequency) or the **propagative** (high-frequency) regime; confusing the
two is the commonest error in this subject.

## How to use this page

Find the quantity, then read the *regime* column before the formula. Numbers
quoted in the worked example come from
`code/formulas_em_electrical_demo.py`.

*Provenance:* no measured data. The worked example is **SYNTHETIC** — the
conductivities and array geometries are chosen test values.

## 1. Maxwell's equations and constitutive relations

| Equation | Differential form | Integral form |
|---|---|---|
| Faraday | $\nabla\times\mathbf{E} = -\partial_t\mathbf{B}$ | $\oint\mathbf{E}\cdot d\mathbf{l} = -d\Phi_B/dt$ |
| Ampère–Maxwell | $\nabla\times\mathbf{H} = \mathbf{J} + \partial_t\mathbf{D}$ | $\oint\mathbf{H}\cdot d\mathbf{l} = I + d\Phi_D/dt$ |
| Gauss (electric) | $\nabla\cdot\mathbf{D} = \rho_f$ | $\oint\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$ |
| Gauss (magnetic) | $\nabla\cdot\mathbf{B} = 0$ | $\oint\mathbf{B}\cdot d\mathbf{S} = 0$ |

| Constitutive relation | Form | Notes |
|---|---|---|
| Ohm | $\mathbf{J} = \sigma\mathbf{E}$ | isotropic; $\sigma$ in S/m |
| Polarisation | $\mathbf{D} = \varepsilon\mathbf{E} = \varepsilon_r\varepsilon_0\mathbf{E}$ | $\varepsilon_0 = 8.854\times10^{-12}$ F/m |
| Magnetisation | $\mathbf{B} = \mu\mathbf{H} = \mu_r\mu_0\mathbf{H}$ | $\mu_0 = 4\pi\times10^{-7}$ H/m (defining) |
| Charge conservation | $\nabla\cdot\mathbf{J} + \partial_t\rho_f = 0$ | follows from Maxwell's equations |

## 2. Two regimes from one equation

Combining Faraday and Ampère in a source-free, homogeneous medium gives the
telegrapher's equation, which simplifies in two opposite limits:

| Regime | Condition | Governing equation | Solution form |
|---|---|---|---|
| Diffusive (low frequency) | $\sigma \gg \omega\varepsilon$ | $\nabla^{2}\mathbf{E} = \mu\sigma\,\partial_t\mathbf{E}$ | diffusion, with skin depth |
| Propagative (high frequency) | $\omega\varepsilon \gg \sigma$ | $\nabla^{2}\mathbf{E} = \mu\varepsilon\,\partial_t^{2}\mathbf{E}$ | waves at $v = 1/\sqrt{\mu\varepsilon}$ |

| Quantity | Formula | Where it applies |
|---|---|---|
| Skin depth | $\delta = \sqrt{2/(\omega\mu\sigma)} = \sqrt{1/(\pi f\mu\sigma)}$ | diffusive regime |
| Attenuation | amplitude $\propto e^{-z/\delta}$ | diffusive regime |
| Wave speed (lossless) | $v = c/\sqrt{\varepsilon_r}$ | GPR, propagative |
| Wavelength | $\lambda = v/f$ | GPR |
| Resolution limit | $\approx \lambda/4$ | the practical vertical resolution |
| Induction number | $B = L/\delta$; small $B$ is the "low-induction" limit | frequency-domain loop systems |

The two regimes meet at the frequency where $\sigma = \omega\varepsilon$, which
for typical soils (σ ~ 0.01 S/m, ε_r ~ 9) lies in the MHz band — which is why
GPR is a wave method and MT is a diffusion method, even though both solve
Maxwell's equations.

## 3. Magnetotellurics

| Quantity | Formula | Conditions |
|---|---|---|
| Impedance tensor | $\mathbf{E} = \mathbf{Z}\mathbf{H}$ with $\mathbf{Z}$ a $2\times2$ complex tensor | horizontal components only |
| Uniform half-space impedance | $Z = \sqrt{i\omega\mu_0/\sigma}$ | 1-D, uniform |
| Apparent resistivity | $\rho_a = \lvert Z\rvert^{2}/(\omega\mu_0)$ | recovers $\rho$ exactly for a half-space |
| Phase | $\phi = \arg Z$ | $45°$ for a uniform half-space |
| Skin depth | $\delta \approx 500\sqrt{\rho_a[\Omega\cdot\text{m}]/f[\text{Hz}]}$ m | convenient form, $\sigma \gg \omega\varepsilon$ |
| Impedance phase and resistivity | $\rho_a = \frac{1}{\omega\mu_0}\lvert Z\rvert^{2}$, $\phi = \arctan(\operatorname{Im}Z/\operatorname{Re}Z)$ | rotation to principal axes for 2-D |
| Tipper | $\mathbf{T}$ from $H_z = \mathbf{T}\cdot(H_x, H_y)$ | inductive indicator in 3-D |
| Depth of investigation | order $\delta$ (often quoted as several $\delta$) | a scale, not a sharp boundary |

## 4. DC resistivity

| Configuration | Geometric factor $K$ | Array geometry |
|---|---|---|
| Half-space point source, potential | $V = \dfrac{\rho I}{2\pi r}$ | single current electrode |
| General four-electrode | $K = 2\pi\bigl[(1/r_{A1M}) - (1/r_{A2M}) - (1/r_{A1N}) + (1/r_{A2N})\bigr]^{-1}$ | four distinct distances |
| Wenner | $K = 2\pi a$ | equal spacings $a$ |
| Schlumberger | $K = \pi(L^{2} - l^{2})/(2l)$ | current half-spacing $L$, potential half-spacing $l$ |
| Dipole–dipole | $K = \pi n(n+1)(n+2)a$ | separation $n$ times the dipole length $a$ |
| Apparent resistivity | $\rho_a = K\,V/I$ | always the definition used in the field |
| Current density | $\mathbf{J} = \sigma\mathbf{E} = I/A\hat{\mathbf{n}}$ | uniform current assumption only |
| Induction / IP chargeability | $M = V_{\text{secondary}}/V_{\text{primary}}$ | mV/V; frequency-domain equivalent is phase in mrad |

**Apparent resistivity is not a material property.** It is the resistivity of the
fictitious homogeneous half-space that would give the measured resistance with
the same array. Where it is quoted without the array geometry, it is not
interpretable.

## 5. Frequency-domain and transient EM systems

| Quantity | Formula | Notes |
|---|---|---|
| Loop field at the centre | $B = \mu_0 I/(2a)$ | circular loop, radius $a$ |
| Dipole field, axial | $B = (\mu_0/4\pi)(2m/r^{3})$ | $m$ in A·m² |
| Mutual inductance of coils | geometry-dependent | sets the primary field |
| Secondary/primary ratio | $\approx$ linear in $\omega\mu_0\sigma L^{2}$ at small induction number | the basis of conductivity meters |
| Time constant of a sphere | $\tau \approx \mu_0\sigma a^{2}/\pi^{2}$ | leading behaviour; real decay sums over modes |
| Late-time decay | a power law whose exponent depends on body shape | quote the exponent only from a source that derives it |
| Time-to-depth (approximate) | $d \sim \sqrt{2t/(\mu_0\sigma)}\times$config factor | diffusive scale, not an exact inversion |

## 6. Ground-penetrating radar

| Quantity | Formula | Conditions |
|---|---|---|
| Velocity | $v = c/\sqrt{\varepsilon_r\mu_r}$ | low-loss; $\mu_r = 1$ in soils |
| Attenuation | $\alpha \approx \dfrac{\sigma}{2}\sqrt{\mu/\varepsilon}$ | low-loss limit |
| Wavelength | $\lambda = v/f$ |  |
| Reflectivity | $R = \dfrac{\sqrt{\varepsilon_1} - \sqrt{\varepsilon_2}}{\sqrt{\varepsilon_1} + \sqrt{\varepsilon_2}}$ | normal incidence, negligible conductivity |
| Depth from two-way time | $d = v\,t/2$ | requires a velocity, which requires a dielectric constant |

Water dominates the radar response: $\varepsilon_r \approx 80$ for liquid water
against 3–6 for dry rock and soil, so a change of moisture content changes both
velocity and attenuation by a large factor.

## Worked example (numbers from the verification script)

| Quantity | Value |
|---|---|
| Skin depth, $f = 1$ Hz, $\sigma = 0.01$ S/m | 5032.9 m = 5.033 km |
| Skin depth, $f = 1$ Hz, $\sigma = 0.001$ S/m | 15915.5 m = 15.915 km |
| Skin depth, $f = 100$ Hz, $\sigma = 0.01$ S/m | 503.3 m |
| Ratio when $\sigma$ falls by 10 at fixed $f$ | 3.1623 $= \sqrt{10}$ |
| MT half-space, $T = 10$ s, $\sigma = 0.01$ S/m | $\lvert Z\rvert = 8.885766\times10^{-3}$ Ω, $\rho_a = 100.0000$ Ω·m, phase $45.000°$ |
| Same at $T = 100$ s and $T = 1000$ s | $\rho_a = 100.0000$ Ω·m, phase $45.000°$ in every case |
| Wenner, $a = 10$ m, $V/I = 10$ Ω | $K = 62.831853$ m, $\rho_a = 628.3185$ Ω·m |
| Schlumberger, $L = 100$ m, $l = 10$ m | $K = 1555.088364$ m, $\rho_a = 15550.8836$ Ω·m |
| Current density, 1 A through 0.01 m² | 100.000 A/m² |
| GPR in $\varepsilon_r = 9$: $v$ | $9.993082\times10^{7}$ m/s |
| GPR at 100 MHz / 400 MHz | $\lambda = 0.9993$ m / 0.2498 m; $\lambda/4 = 0.2498$ m / 0.0625 m |
| Induction number, $L = 20$ m, $\delta = 100$ m | 0.200000 (low-induction regime) |
| Sphere time constant, $\sigma = 0.01$ S/m, $a = 500$ m | $3.183099\times10^{-4}$ s = 0.318310 ms |
| Loop field, $I = 10$ A, $a = 0.5$ m | $1.256637\times10^{-5}$ T = 12.5664 µT |

The MT result is the cleanest check on the whole sheet: for a uniform
half-space, apparent resistivity must equal the true resistivity at *every*
period and the phase must be exactly $45°$. The script reproduces both at three
decades of period, which means the impedance, the normalisation and the phase
conventions are mutually consistent. The skin-depth entries show the two
half-space truths that govern MT survey design: depth of investigation grows as
$1/\sqrt{\sigma}$ and as $1/\sqrt{f}$.

## Assumptions and regime of validity

- The diffusive forms assume $\sigma \gg \omega\varepsilon$; at GPR frequencies
  in dry rock this fails, and the wave forms must be used.
- MT formulas above assume a **1-D (layered) Earth** and plane-wave sources.
  Real data are affected by 2-D and 3-D structure, anisotropy and noise, which
  the scalar impedance cannot represent.
- Apparent resistivity in DC work is geometry-dependent; comparisons between
  surveys require the same array.
- The sphere time constant is a leading-order result; real transient responses
  are sums over modes and depend on the transmitter waveform and the receiver
  window.
- GPR depth conversion assumes a known, constant permittivity; in reality
  moisture varies, so the velocity is itself an unknown.

## Verification script

[`code/formulas_em_electrical_demo.py`](./code/formulas_em_electrical_demo.py) —
print-only, seeded, under a second, exit 0. It prints the skin depth table, the
MT half-space identity, the DC geometric factors, GPR velocity and resolution,
the induction number, the sphere time constant and the loop field quoted above.

## Related pages

- [Formula Sheet: Gravity, Magnetics and Potential Theory](./04-formulas-potential-fields.md)
- [Formula Sheet: Inverse Theory and Statistics](./06-formulas-inverse-statistics.md)
- [Glossary: A-F](../01-glossary/01-glossary-a-f.md) — apparent resistivity and attenuation
- [08-geomagnetism-electromagnetism folder overview](../../08-geomagnetism-electromagnetism/README.md)
- [09-electrical-em-methods folder overview](../../09-electrical-em-methods/README.md)
