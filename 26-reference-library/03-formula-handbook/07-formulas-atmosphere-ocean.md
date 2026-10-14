---
id: 26-03-07
title: "Formula Sheet: Atmosphere, Radiation and Ocean"
level: graduate
prereqs: []
estimated_minutes: 35
tags: [reference, formulas, atmosphere, ocean, radiation]
---

# Formula Sheet: Atmosphere, Radiation and Ocean

Thermodynamics and dynamics of the atmosphere and ocean, radiation laws, and the
scale analysis that decides which terms may be dropped. The organising idea is
that almost every "formula" here is a *balance* — hydrostatic, geostrophic,
radiative — valid only when the neglected terms are small.

## How to use this page

Look up the balance or the law, and read the validity condition with it. Where a
relation is empirical (sound speed in seawater, for example), the entry says so
and points to the published algorithm rather than reproducing coefficients that
are easy to mis-transcribe. Numbers quoted in the worked example come from
`code/formulas_atmosphere_ocean_demo.py`.

*Provenance:* no measured data. The worked example is **SYNTHETIC** — the
atmospheric states and optical properties are chosen test values.

## 1. Thermodynamics of the atmosphere

| Quantity | Formula | Conditions |
|---|---|---|
| Ideal gas law | $p = \rho R_d T$ | $R_d = 287.05$ J kg⁻¹ K⁻¹ for dry air |
| Hydrostatic balance | $\dfrac{dp}{dz} = -\rho g$ | valid for horizontal scales large compared with depth |
| Hypsometric relation | $z_2 - z_1 = \dfrac{R_d\bar{T}}{g}\ln\dfrac{p_1}{p_2}$ | isothermal layer approximation |
| Potential temperature | $\theta = T\left(\dfrac{p_0}{p}\right)^{R_d/c_p}$ | $p_0 = 1000$ hPa; adiabatic displacement |
| Equivalent potential temperature | $\theta_e \approx \theta\exp\!\left(\dfrac{L_v r_s}{c_pT}\right)$ | saturated ascent; adds latent heat |
| Dry adiabatic lapse rate | $\Gamma_d = g/c_p \approx 9.8$ K/km | unsaturated atmosphere |
| Density from $p$, $T$ | $\rho = p/(R_dT)$ | ideal-gas approximation |
| Buoyancy frequency | $N = \sqrt{\dfrac{g}{\theta}\dfrac{d\theta}{dz}}$ | stable when $N^{2} > 0$ |
| Static stability criterion | stable if $d\theta/dz > 0$ | a real criterion on the potential temperature, not on $T$ |

**The criterion is on $\theta$, not on $T$.** A layer in which temperature falls
with height may still be statically stable, because pressure also falls. This is
the commonest conceptual error in the subject.

## 2. Dynamics of the rotating atmosphere and ocean

| Quantity | Formula | Conditions |
|---|---|---|
| Coriolis parameter | $f = 2\Omega\sin\varphi$ | $\Omega = 7.292115\times10^{-5}$ rad/s (nominal) |
| Geostrophic wind | $u_g = -\dfrac{1}{\rho f}\dfrac{\partial p}{\partial y}$, $v_g = \dfrac{1}{\rho f}\dfrac{\partial p}{\partial x}$ | small Rossby number |
| Geostrophic current | $u_g = -\dfrac{g}{f}\dfrac{\partial \eta}{\partial y}$ | sea-surface slope $\eta$ |
| Rossby number | $Ro = U/(fL)$ | small $\Rightarrow$ rotation dominates |
| Thermal wind | $\dfrac{\partial u_g}{\partial z} = \dfrac{g}{fT}\dfrac{\partial T}{\partial y}$ | hydrostatic and geostrophic |
| Barotropic vorticity | $\dfrac{D(\zeta + f)}{Dt} = 0$ | shallow-water, frictionless |
| Shallow-water phase speed | $c = \sqrt{gH}$ | $H$ = mean depth |
| Rossby radius of deformation | $L_d = \dfrac{\sqrt{gH}}{f}$ | barotropic; $L_d$ replaces $\sqrt{g'H}/f$ for baroclinic |
| Ekman depth | $D_E = \sqrt{2K_v/f}$ | eddy viscosity $K_v$ constant |
| Richardson number | $Ri = N^{2}/(\partial u/\partial z)^{2}$ | $Ri < 1/4$ is the classical instability threshold |
| Potential vorticity | $q = \dfrac{\zeta + f}{h}$ | shallow-water form |

## 3. Radiation

| Law | Formula | Notes |
|---|---|---|
| Planck | $B_\lambda(T) = \dfrac{2hc^{2}}{\lambda^{5}}\dfrac{1}{e^{hc/(\lambda k_BT)} - 1}$ | spectral radiance |
| Wien displacement | $\lambda_{\max}T = 2.897771955\times10^{-3}$ m·K | peak wavelength of $B_\lambda$ |
| Stefan–Boltzmann | $F = \sigma T^{4}$, $\sigma = 5.670\,374\,419\times10^{-8}$ W m⁻² K⁻⁴ | flux from a blackbody |
| Inverse-square scaling | $F(r) = F(R)\,(R/r)^{2}$ | the solar constant follows from this |
| Kirchhoff | $\varepsilon_\lambda = \alpha_\lambda$ | emissivity equals absorptivity |
| Emitted flux, grebody | $F = \varepsilon\sigma T^{4}$ | $\varepsilon$ in [0, 1] |
| Effective temperature | $T_e = \left[\dfrac{(1-\alpha)S}{4\sigma}\right]^{1/4}$ | planetary energy balance, $\alpha$ = albedo |
| Beer–Lambert | $I = I_0e^{-\tau}$, $\tau = \int k\,ds$ | optical depth $\tau$ |
| Net imbalance | $N = S(1-\alpha) - \sigma T^{4}$ | the quantity that drives warming |

The factor of 4 in the effective-temperature formula is geometry, not physics:
the planet intercepts $\pi R^{2}$ of sunlight and radiates from $4\pi R^{2}$.

## 4. Ocean physics

| Quantity | Formula | Conditions |
|---|---|---|
| Seawater density | non-linear function of $T$, $S$, $p$ | use a published equation of state (TEOS-10) rather than a linear fit |
| Haline and thermal expansion | $\alpha = -\dfrac{1}{\rho}\dfrac{\partial\rho}{\partial T}$, $\beta = \dfrac{1}{\rho}\dfrac{\partial\rho}{\partial S}$ | nominal values: $\alpha \sim 1.4\times10^{-4}$—$3\times10^{-4}$ K⁻¹, $\beta \sim 7.6\times10^{-4}$ per unit salinity |
| Sound speed (simplified) | $c \approx 1449 + 4.6T - 0.055T^{2} + 0.0003T^{3} + (1.34 - 0.01T)(S-35) + 0.016z$ | approximate; use the full Mackenzie (1981) nine-term equation for quantitative work |
| Dynamic and kinematic viscosity | $\nu = \eta/\rho$ | m²/s |
| Stokes drift | $u_s = \dfrac{\omega k a^{2}}{2}\dfrac{\cosh[2k(z+H)]}{\sinh^{2}(kH)}$ | wave-induced mean drift; $a$ = wave amplitude |
| Deep-water wave dispersion | $\omega^{2} = gk$ | $H \gg \lambda$; phase speed $c = g/\omega$ |
| Shallow-water waves | $c = \sqrt{gH}$ | $H \ll \lambda$; non-dispersive |
| Group velocity, general | $c_g = \dfrac{1}{2}c\left(1 + \dfrac{2kH}{\sinh 2kH}\right)$ | $c/2$ in deep water, $c$ in shallow water |
| Wave energy flux | $P = E\,c_g$, $E = \tfrac{1}{8}\rho g H_{\text{wav}}^{2}$ | $H_{\text{wav}}$ = wave height |
| Steric sea level | $\eta_{\text{steric}} = -\dfrac{1}{\rho_0}\int \Delta\rho\,dz$ | density change, not mass change |
| Tidal potential | $V_{\text{tide}} \propto \dfrac{GMr^{2}}{d^{3}}\bigl(3\cos^{2}\psi - 1\bigr)$ | equilibrium tide, degree-2 term |

The sound-speed entry is deliberately marked *simplified*. Published algorithms
(Mackenzie 1981; Chen & Millero 1977; the UNESCO/TEOS-10 formulations) differ in
their coefficient sets and in their stated accuracy, and reproducing those
coefficients from memory is exactly the kind of transcription error this
curriculum's reference pages are meant to prevent: take them from the primary
source.

## 5. Scale analysis: which terms may be dropped

| Balance | Retained terms | Valid when |
|---|---|---|
| Hydrostatic | $\partial_zp = -\rho g$ | aspect ratio $H/L \ll 1$ |
| Geostrophic | Coriolis = pressure gradient | $Ro \ll 1$ |
| Cyclostrophic | centripetal = pressure gradient | $Ro \gg 1$ (small scales, low latitude) |
| Ekman | Coriolis = friction | boundary layer, $z \lesssim D_E$ |
| Thermal wind | geostrophic shear from $\partial_y T$ | hydrostatic + geostrophic |
| Quasi-geostrophic | potential-vorticity conservation | $Ro \ll 1$, slow evolution |

Quoting a "balance" without its small parameter is how a mid-latitude formula
gets applied to a tropical cyclone, or an ocean gyre model to a tidal channel.

## Worked example (numbers from the verification script)

| Quantity | Value |
|---|---|
| $R_d/c_p$ for dry air | 0.285622 |
| Potential temperature, $T = 288.15$ K, $p = 850$ hPa | 301.8409 K |
| Density from the ideal gas law at that $p$, $T$ | 1.027644 kg/m³ |
| Dry adiabatic lapse rate $g/c_p$ | $9.757861\times10^{-3}$ K/m = 9.7579 K/km |
| Coriolis parameter at 0°, 45°, 60° | $0$, $+1.031261\times10^{-4}$, $+1.263031\times10^{-4}$ s⁻¹ |
| Internal Rossby radius, $H = 1000$ m, $\varphi = 45°$ | 960.267 km |
| Geostrophic wind for 1 Pa/km at $\rho = 1.225$ kg/m³ | 7.9158 m/s = 28.497 km/h |
| Geostrophic current for a 1 mm/km sea-surface slope | $-0.095126$ m/s |
| Ekman depth, $K_v = 0.01$ m²/s at 45° | 13.9261 m |
| Wien peak for $T = 5772$ K | 502.0395 nm |
| Blackbody exitance at 5772 K | $6.293859\times10^{7}$ W/m² |
| Solar constant from $\sigma T^{4}(R_\odot/d)^{2}$ | 1361.1627 W/m² |
| Photon energy at 500 nm | $3.972892\times10^{-19}$ J |
| Optical depth for $k = 0.02$ m⁻¹ over 1500 m | 30.0000 (transmittance $9.36\times10^{-14}$) |
| Simplified sound speed, $T = 10$ °C, $S = 35$, $z = 1000$ m | 1505.9900 m/s |

Two results deserve attention. The solar constant computed from the
Stefan–Boltzmann law with the Sun's radius and the Earth's mean distance comes
out at 1361 W/m², which is the accepted order of magnitude — a genuine,
independent check that Wien's law, Planck's normalisation and the inverse-square
scaling are mutually consistent. And the potential temperature exceeds the
actual temperature by 13.7 K at 850 hPa, which is the size of the adiabatic
correction that must be removed before any horizontal temperature comparison.

## Assumptions and regime of validity

- Hydrostatic balance fails for convection and for flows with aspect ratio of
  order one; it is not a general property of the atmosphere.
- Geostrophic balance fails near the equator (where $f \to 0$), in the boundary
  layer, and for fast, small-scale flows.
- The sound-speed and equation-of-state formulas quoted here are approximate;
  quantitative work needs the published algorithms in their full form, with the
  stated ranges of validity (pressures, temperatures, salinities).
- The equilibrium tide ignores ocean-basin resonance, bathymetry and the
  solid-Earth tide; it is a forcing, not a sea-level prediction.
- Wien and Stefan–Boltzmann describe blackbodies. Real surfaces require
  spectral emissivity, which is why satellite retrieval is a separate problem.
- Optical depth is additive only for independent, non-interacting layers; in
  strong absorption bands this fails.

## Verification script

[`code/formulas_atmosphere_ocean_demo.py`](./code/formulas_atmosphere_ocean_demo.py) —
print-only, seeded, under a second, exit 0. It prints the thermodynamic state,
the Coriolis and Rossby scales, the geostrophic and Ekman estimates, the
radiation checks, the optical-depth example and the simplified sound speed
quoted above.

## Related pages

- [Formula Sheet: Mathematics and Calculus](./01-formulas-mathematics.md)
- [Physical Constants and Earth Parameters with Sources](../02-symbols-and-units/03-constant-handbook.md)
- [16-atmosphere-climate folder overview](../../16-atmosphere-climate/README.md)
- [15-oceanography-marine folder overview](../../15-oceanography-marine/README.md)
- [17-remote-sensing-gis folder overview](../../17-remote-sensing-gis/README.md)
