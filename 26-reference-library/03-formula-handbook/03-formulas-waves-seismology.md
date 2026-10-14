---
id: 26-03-03
title: "Formula Sheet: Waves, Elasticity and Seismology"
level: advanced
prereqs: []
estimated_minutes: 35
tags: [reference, formulas, seismology, elasticity]
---

# Formula Sheet: Waves, Elasticity and Seismology

Elasticity, the wave equation, ray geometry, reflection coefficients and source
scaling, in the order in which they are used in practice. Every entry carries its
assumption: isotropic or anisotropic, acoustic or elastic, far field or near
field.

## How to use this page

The sheet is grouped: constitutive relations first, then wave propagation, then
observation-side formulas (travel times, reflection amplitudes, magnitudes).
Numbers quoted in the worked example come from
`code/formulas_waves_seismology_demo.py`.

*Provenance:* no measured data. The worked example is **SYNTHETIC** — the elastic
parameters are chosen test values, not measurements.

## 1. Stress, strain and constitutive relations

| Quantity | Formula | Notes |
|---|---|---|
| Strain tensor | $\varepsilon_{ij} = \tfrac{1}{2}(\partial_i u_j + \partial_j u_i)$ | small-strain, symmetric |
| Rotation | $\omega_{ij} = \tfrac{1}{2}(\partial_i u_j - \partial_j u_i)$ | antisymmetric; no stress |
| Hooke's law | $\sigma_{ij} = C_{ijkl}\varepsilon_{kl}$ | linear elastic; $C_{ijkl}$ has 81 components, 21 independent in the most general anisotropic case |
| Isotropic case | $\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij}$ | two constants, $\lambda$ and $\mu$ |
| Equation of motion | $\rho\,\partial_t^{2}u_i = \partial_j\sigma_{ij} + f_i$ | $f_i$ is a body force density |
| P-wave equation | $\rho\,\partial_t^{2}(\nabla\cdot\mathbf{u}) = (\lambda + 2\mu)\nabla^{2}(\nabla\cdot\mathbf{u})$ | homogeneous isotropic medium |
| S-wave equation | $\rho\,\partial_t^{2}(\nabla\times\mathbf{u}) = \mu\nabla^{2}(\nabla\times\mathbf{u})$ | same assumptions |
| Wave speeds | $v_p = \sqrt{(\lambda + 2\mu)/\rho}$, $v_s = \sqrt{\mu/\rho}$ | $\mu = 0$ in a fluid, so $v_s = 0$ |
| Acoustic limit | $v = \sqrt{K/\rho}$ | fluid, $K$ the bulk modulus |

## 2. Isotropic moduli and their relations

| Modulus | In terms of $v_p$, $v_s$, $\rho$ | In terms of $E$, $\nu$ |
|---|---|---|
| Shear modulus $\mu$ | $\mu = \rho v_s^{2}$ | $\mu = E/[2(1+\nu)]$ |
| Lamé parameter $\lambda$ | $\lambda = \rho(v_p^{2} - 2v_s^{2})$ | $\lambda = E\nu/[(1+\nu)(1-2\nu)]$ |
| Bulk modulus $K$ | $K = \rho(v_p^{2} - \tfrac{4}{3}v_s^{2})$ | $K = E/[3(1-2\nu)]$ |
| Young's modulus $E$ | $E = \mu(3\lambda + 2\mu)/(\lambda + \mu)$ | — |
| Poisson's ratio $\nu$ | $\nu = \dfrac{v_p^{2} - 2v_s^{2}}{2(v_p^{2} - v_s^{2})}$ | — |
| P-to-S speed ratio | $v_p/v_s = \sqrt{2(1-\nu)/(1-2\nu)}$ | 1.73 for $\nu = 0.25$ |
| $M$ (P-wave modulus) | $M = \lambda + 2\mu = \rho v_p^{2}$ | the relevant modulus for normal-incidence P waves |

**Consistency check.** Any four of $\lambda$, $\mu$, $K$, $E$, $\nu$, $v_p$, $v_s$
determine the rest in an isotropic medium, but only two are independent. When a
table of rock properties violates that, the table has been mis-transcribed.

## 3. Ray geometry

| Quantity | Formula | Conditions |
|---|---|---|
| Ray parameter | $p = \dfrac{\sin\theta}{v}$ | constant along a ray in a laterally homogeneous (1-D) medium |
| Snell's law | $\dfrac{\sin\theta_1}{v_1} = \dfrac{\sin\theta_2}{v_2} = p$ | welded interface |
| Critical angle | $\theta_c = \arcsin(v_1/v_2)$ | requires $v_2 > v_1$ |
| Horizontal slowness | $p = \dfrac{dT}{dX}$ | from the observed travel-time curve |
| Two-layer intercept time | $T_i = \dfrac{2h\cos\theta_c}{v_1}$ | head wave, thickness $h$ |
| Dipping refractor, downdip | $v_{\text{app}} = \dfrac{v_2}{\cos\alpha}$ | $\alpha$ the refractor dip |
| Turning point in a layered medium | $p = 1/v(z_{\text{turn}})$ | the depth where the ray is horizontal |

$$ X(p) = 2\int_0^{z_{\text{turn}}} \frac{p\,v(z)\,dz}{\sqrt{1 - p^{2}v^{2}(z)}} $$

$$ T(p) = 2\int_0^{z_{\text{turn}}} \frac{dz}{v(z)\sqrt{1 - p^{2}v^{2}(z)}} $$

These two integrals are the τ–p formulation of 1-D travel times; the singular
integrand at the turning point is the reason numerical evaluation needs care.

## 4. Travel times and moveout in reflection work

| Quantity | Formula | Conditions |
|---|---|---|
| Single layer, offset $x$ | $t = \sqrt{t_0^{2} + x^{2}/v^{2}}$ | constant velocity |
| Layered medium | $t^{2} \approx t_0^{2} + x^{2}/v_{\text{rms}}^{2}$ | hyperbolic approximation, offsets small relative to depth |
| Normal moveout | $\Delta t_{\text{NMO}} \approx \dfrac{x^{2}}{2t_0v_{\text{rms}}^{2}}$ | same conditions |
| Root-mean-square velocity | $v_{\text{rms}}^{2} = \dfrac{\sum_i v_i^{2}\Delta t_i}{\sum_i \Delta t_i}$ | vertical travel-time weighting |
| Dix relation | $v_{\text{int}}^{2} = \dfrac{v_{\text{rms},n}^{2}t_n - v_{\text{rms},n-1}^{2}t_{n-1}}{t_n - t_{n-1}}$ | interval velocity between two picked reflectors |
| Depth conversion | $z = \dfrac{v\,t_0}{2}$ | constant velocity only |

The quadratic NMO formula is the leading term of the hyperbolic one; the two
differ by $O(x^{4})$, which becomes visible at offsets comparable with depth
(the verification script quantifies this).

## 5. Reflection and transmission coefficients

| Case | Formula | Conditions |
|---|---|---|
| Acoustic impedance | $Z = \rho v$ | along the ray |
| Normal incidence, amplitude | $R = \dfrac{Z_2 - Z_1}{Z_2 + Z_1}$ | elastic or acoustic half-spaces |
| Normal incidence, energy | $R_E = R^{2}$, $T_E = 1 - R^{2}$ | energy is conserved |
| Normal incidence, transmitted amplitude | $T = \dfrac{2Z_1}{Z_1 + Z_2}$ | check with $R + T = 1$ only in impedance terms |
| Zoeppritz | full solution for $R_{pp}$, $R_{ps}$, $T_{pp}$, $T_{ps}$ | exact, plane wave, welded interface |
| Shuey small-angle approximation | $R(\theta) \approx R_0 + G\sin^{2}\theta$, $G$ from $v_p$, $v_s$, $\rho$ contrasts | incidence below the critical angle |
| Aki–Richards | linearised $P$-wave reflection coefficients | same validity regime |
| AVA intercept, gradient | $R_0 = \tfrac{1}{2}(\Delta v_p/v_p + \Delta\rho/\rho)$, $G$ contains $v_s$ | $\Delta$ denotes the difference across the interface |

Amplitude reflection coefficients and energy reflection coefficients disagree;
the factor $1-R^{2} = 0.970$ in the worked example below is the energy fraction,
not an amplitude.

## 6. Attenuation, dispersion and surface waves

| Quantity | Formula | Notes |
|---|---|---|
| Quality factor | $Q = 2\pi\dfrac{E_{\text{stored}}}{E_{\text{lost per cycle}}}$ | dimensionless; large $Q$ = low attenuation |
| Amplitude decay | $A(x) = A_0\exp(-\alpha x)$, $\alpha = \dfrac{\pi f}{Qv}$ | combined absorption; geometric spreading is separate |
| Dispersion relation | $\omega = \omega(k)$; phase $v = \omega/k$, group $v_g = d\omega/dk$ | both needed to interpret a dispersive arrival |
| Group velocity from phase | $v_g = v + k\dfrac{dv}{dk}$ or $v_g = v - \lambda\dfrac{dv}{d\lambda}$ | valid for smooth dispersion |
| Rayleigh wave, homogeneous | $v_R \approx 0.92\,v_s$ | Poisson's ratio near 0.25; varies from 0.87 to 0.96 with $\nu$ |
| Love wave | $v_s$ of the waveguide | requires a low-velocity layer |

**The group velocity is not the phase velocity.** A dispersion curve read off a
record is usually a phase-velocity or group-velocity curve depending on the
method; using one where the other belongs shifts shear-speed estimates by tens of
per cent.

## 7. Source scaling

| Quantity | Formula | Notes |
|---|---|---|
| Seismic moment | $M_0 = \mu\,\bar{A}\,\bar{D}$ | $\bar{A}$ fault area, $\bar{D}$ average slip |
| Moment magnitude | $M_w = \tfrac{2}{3}\bigl(\log_{10}M_0 - 9.1\bigr)$ | $M_0$ in N·m |
| Stress drop | $\Delta\sigma = C\mu\bar{D}/\bar{L}$ | $C$ of order 1, depends on fault geometry |
| Corner frequency | $f_c \approx k\,v_s/(2\pi\bar{L})$ | $k$ depends on the rupture model; often near 2 |
| Radiated energy, empirical | $\log_{10}E \approx 1.5\,M_w + 4.8$ | $E$ in J; a rough estimate, not a measurement |
| Double-couple radiation pattern | four-lobed, nodal lines at $\pm 45°$ to the slip plane | the basis of fault-plane solutions |
| Moment tensor decomposition | $\mathbf{M} = \mathbf{M}_{\text{iso}} + \mathbf{M}_{\text{DC}} + \mathbf{M}_{\text{CLVD}}$ | isotropic, double couple, compensated linear vector dipole |

## 8. Wavefields and Green's functions

| Quantity | Statement | Conditions |
|---|---|---|
| Representation theorem | $\mathbf{u}(\mathbf{x},t) = \int G_{ij}(\mathbf{x},\mathbf{x}',t)\ast f_j(\mathbf{x}',t)\,dV'$ | linear elastic medium |
| Reciprocity | $G_{ij}(\mathbf{x},\mathbf{x}') = G_{ji}(\mathbf{x}',\mathbf{x})$ | elastic, no attenuation |
| Green's function, 3-D acoustic | $G \propto \dfrac{1}{r}\delta(t - r/v)$ | far field; amplitude decays as $1/r$ |
| Green's function, 2-D | $G \propto \dfrac{1}{\sqrt{r}}\mathcal{H}(t - r/v)$ | line source; decays as $1/\sqrt{r}$ |
| Born approximation | scattered field $\propto \int G\,\delta m\,G\,f$ | weak perturbation $\lvert\delta m/m\rvert \ll 1$ |
| Attenuative Green's function | multiply by $e^{-i\omega t^{*}}$ or $e^{-\omega r/(2Qv)}$ | constant-$Q$ model; only an approximation to real absorption |

## Worked example (numbers from the verification script)

Given $\rho = 2700$ kg/m³, $v_p = 6000$ m/s and $v_s = 3500$ m/s (chosen test
values):

| Quantity | Value |
|---|---|
| $\mu$ | $3.3075\times10^{10}$ Pa = 33.0750 GPa |
| $\lambda$ | $3.1050\times10^{10}$ Pa = 31.0500 GPa |
| $K$ | $5.3100\times10^{10}$ Pa = 53.1000 GPa |
| $E$ | $8.2165\times10^{10}$ Pa = 82.1653 GPa |
| $\nu$ | $0.242105$ |
| $v_p/v_s$ | $1.714286$ |
| Ray parameter for 30° incidence in $v_p = 6000$ m/s | $8.333333\times10^{-5}$ s/m |
| Refraction angle in $v_p = 8000$ m/s | $41.810315°$ |
| Critical angle into 8000 m/s | $48.590378°$ |
| $R$ for $Z_1 = 4.4\times10^{6}$, $Z_2 = 6.24\times10^{6}$ kg m⁻² s⁻¹ | $+0.172932$ (energy $R^{2} = 0.029906$) |
| Hyperbolic travel time, $t_0 = 1.20$ s, $x = 1500$ m, $v_{\text{rms}} = 3000$ m/s | $1.300000$ s |
| Normal moveout | $0.100000$ s = 100.000 ms |
| Quadratic NMO approximation | $0.104167$ s (4.2 % high) |
| Depth from $t_0$ and $v_{\text{rms}}$ | 1800.0 m |
| Local group velocity at 0.30 Hz, $c(f) = 3000(1 - 0.05/f)$ | 3125.000 m/s (phase velocity 2500.000 m/s) |
| $M_0$ for $\mu = 3\times10^{10}$ Pa, $A = 10^{9}$ m², $\bar{D} = 2$ m | $6.000000\times10^{19}$ N·m |
| $M_w$ | $7.118768$ |
| Empirical energy estimate | $3.0071\times10^{15}$ J |

The elastic moduli table is verified by back-substituting into
$v_p = \sqrt{(\lambda+2\mu)/\rho}$ and $v_s = \sqrt{\mu/\rho}$, which returns
6000.000 and 3500.000 m/s exactly — the standard way to check a rock-physics
conversion. The dispersion entry shows why the discretisation of a dispersion
curve matters: over the 0.2–0.4 Hz band the secant estimate is 3000 m/s, while
the local group velocity at 0.30 Hz is 3125 m/s, and the phase velocity there is
2500 m/s.

## Assumptions and regime of validity

- All elastic relations above are **isotropic, linear and small-strain**. In
  anisotropic rock, $v_p$ and $v_s$ depend on propagation direction, and the
  two-constant relations do not hold.
- The hyperbolic travel-time formula is a small-offset approximation; it fails
  near the critical offset and in the presence of strong lateral velocity
  gradients.
- Zoeppritz and its linearisations assume plane waves, a welded interface and
  homogeneous half-spaces. Real data also contain tuning, attenuation and
  anisotropy, none of which these formulas represent.
- $M_0 = \mu\bar{A}\bar{D}$ assumes the shear modulus at the source is known;
  $\mu$ is derived from $v_s$ and $\rho$ at hypocentral depth, which carries its
  own uncertainty.
- The empirical $\log_{10}E = 1.5M_w + 4.8$ relation has scatter of roughly half
  an order of magnitude and should never be used as if it were exact.

## Verification script

[`code/formulas_waves_seismology_demo.py`](./code/formulas_waves_seismology_demo.py) —
print-only, seeded, under a second, exit 0. It prints the moduli conversion with
back-substitution, the Snell and critical-angle checks, the impedance and
reflection coefficients, travel time and NMO, the dispersion trio, and the
moment-magnitude calculation quoted above.

## Related pages

- [Formula Sheet: Gravity, Magnetics and Potential Theory](./04-formulas-potential-fields.md)
- [Formula Sheet: Inverse Theory and Statistics](./06-formulas-inverse-statistics.md)
- [Symbol Handbook: Notation Used Throughout](../02-symbols-and-units/01-symbol-handbook.md)
- [06-seismology folder overview](../../06-seismology/README.md)
- [05-core-geophysics folder overview](../../05-core-geophysics/README.md)
