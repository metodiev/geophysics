---
id: 02-05-05
title: "Convection, Radiation and Combined Heat Transfer"
level: advanced
prereqs: ["02-05-04", "02-01-03"]
estimated_minutes: 90
tags: [convection, rayleigh-number, radiation, heat-transfer]
---

# Convection, Radiation and Combined Heat Transfer

Conduction is not the only way heat moves, and in most of the Earth it is not
even the main way. Three mechanisms carry heat:

| Mode | Carrier | Governing quantity | Typical setting |
|---|---|---|---|
| Conduction | Lattice and molecular vibration | $k$ | The lithosphere; a borehole; a magma's host rock |
| Convection | Bulk motion of a fluid or creeping solid | Ra, Nu | The mantle, the outer core, oceans, atmosphere, hydrothermal systems |
| Radiation | Photons | $\sigma T^4$ | The Earth's surface to space; a lava surface; the core–mantle boundary |

The engineering question is never "which is better" but "which dominates here",
and the answer is a dimensionless number. For an imposed flow it is the Péclet
number; for a buoyancy-driven flow it is the Rayleigh number; for radiation against
conduction or convection it is a comparison of $4\sigma T^3$ with a heat-transfer
coefficient. This lesson computes each of them, applies them to the mantle, to
groundwater, to a lava lake and to the planetary energy balance, and gives the
numbers that decide every case.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Rayleigh number by non-dimensionalising the Boussinesq
   equations, and state what each factor in
   $\mathrm{Ra} = \rho g\alpha\Delta T d^3/(\kappa\eta)$ does physically.
2. **Compute** a Rayleigh number for the mantle, an upper-mantle layer, a water
   layer and a lava lake, and compare each with the critical value.
3. **Derive** the boundary-layer scaling $\mathrm{Nu} \sim \mathrm{Ra}^{1/3}$ and
   use it to convert a Rayleigh number into a convective heat flux.
4. **Compute** a blackbody flux $\sigma T^4$ and a radiative heat-transfer
   coefficient $4\sigma T^3$, and decide when radiation beats convection.
5. **Compute** the Earth's effective radiating temperature from an adopted solar
   constant and albedo, and state the sensitivity $\mathrm{d}T_e/\mathrm{d}S$.
6. **Apply** the Péclet number to decide whether groundwater flow or conduction
   controls a temperature field.
7. **State** the Rayleigh number's regime of validity and say precisely how the
   real mantle violates it.

## Prerequisites

- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](./04-heat-conduction.md)
  — the conductive baseline and the diffusion timescales.
- [02-01-03 Scaling Laws, Similarity and Dimensional Reasoning](../01-measurement-and-physical-reasoning/03-scaling-laws.md)
  — the non-dimensionalisation technique used throughout.

## 1. The three modes and how to compare them

### 1.1 Fluxes, not temperatures

Every comparison in this lesson is a comparison of **fluxes** in W m⁻²:

- conduction: $q_{\text{cond}} = k\,\Delta T/L$,
- convection: $q_{\text{conv}} = \mathrm{Nu}\,q_{\text{cond}}$, or
  $\mathrm{Nu}\,k\Delta T/L$,
- radiation: $q_{\text{rad}} = \epsilon\sigma T^4$.

Because convection and radiation both scale with temperature in ways that
conduction does not, the ranking changes with the regime. Radiation is negligible
against conduction at 100 K and overwhelming at 1400 K; convection beats conduction
by a factor of 40 in the whole mantle and by a factor of 500 in a metre of water.

### 1.2 The radiation core

The Planck function gives the spectral radiance of a blackbody:

$$B_\lambda(T) = \frac{2hc^2}{\lambda^5}\frac{1}{e^{hc/\lambda k_BT}-1}
\qquad [\mathrm{W\,m^{-3}\,sr^{-1}}] . \tag{1}$$

Two consequences are used constantly:

$$F = \epsilon\sigma T^4 \quad\text{(integrated flux)}, \qquad
\lambda_{\max}T = \frac{hc}{x k_B} \quad\text{(Wien)} , \tag{2}$$

with $\sigma = 5.670\,374\,419\times10^{-8}$ W m⁻² K⁻⁴ (exact by definition,
$2\pi^5k_B^4/15h^3c^2$) and $x = 4.965\,114\,232…$ the root of $x = 5(1-e^{-x})$.
Wien's constant is therefore also exact:

$$b = \frac{hc}{xk_B} = 2.897\,772\times10^{-3}\ \mathrm{m\,K} . \tag{3}$$

Linearising $F$ about a mean temperature $T$ gives the **radiative
heat-transfer coefficient**

$$h_{\text{rad}} \equiv \frac{\mathrm{d}F}{\mathrm{d}T} = 4\sigma T^3 , \tag{4}$$

which is what allows radiation to be compared with a convective coefficient
directly.

## 2. Derivations

### 2.1 The Rayleigh number from the Boussinesq equations

For a layer of thickness $d$ with a temperature difference $\Delta T$, small
density variations and no compressibility effects, the governing equations are

$$\nabla\cdot\mathbf{u} = 0, \qquad
\rho_0\left(\frac{\partial\mathbf{u}}{\partial t}
+ \mathbf{u}\cdot\nabla\mathbf{u}\right)
= -\nabla p + \eta\nabla^2\mathbf{u} + \rho_0 g\alpha(T-T_0)\hat{\mathbf{z}},
\qquad
\frac{\partial T}{\partial t} + \mathbf{u}\cdot\nabla T = \kappa\nabla^2T .
\tag{5}$$

Non-dimensionalise with $x \to dx'$, $t \to (d^2/\kappa)t'$,
$\mathbf{u} \to (\kappa/d)\mathbf{u}'$ and $T \to \Delta T\,T'$. The momentum
equation becomes

$$\frac{1}{\mathrm{Pr}}\left(\frac{\partial\mathbf{u}'}{\partial t'}
+ \mathbf{u}'\cdot\nabla'\mathbf{u}'\right)
= -\nabla' p' + \nabla'^2\mathbf{u}'
+ \mathrm{Ra}\,\frac{\mathrm{Pr}}{\mathrm{Pr}}\,T'\hat{\mathbf{z}} , \tag{6}$$

and the single dimensionless group multiplying the buoyancy term is

$$\boxed{\ \mathrm{Ra} = \frac{\rho_0 g\alpha\Delta T d^3}{\kappa\eta}\ }
\qquad \mathrm{Pr} = \frac{\eta}{\rho_0\kappa} . \tag{7}$$

Read equation (7) factor by factor. The numerator is the buoyancy force that
drives the motion: density contrast $\rho_0\alpha\Delta T$ times gravity, acting
over a volume $d^3$. The denominator is the sum of the two ways of defeating it:
viscous resistance ($\eta$) and thermal smoothing ($\kappa$). **Ra is the ratio
of driving to damping.** The cube on $d$ is why convection is violently
size-dependent: doubling a layer's depth multiplies its Rayleigh number by eight.

The linear stability problem for a plane layer with rigid boundaries gives

$$\mathrm{Ra}_c = 1708 \quad\text{(free–free)}, \qquad
\mathrm{Ra}_c \approx 1101 \quad\text{(rigid–rigid)} , \tag{8}$$

with the values depending on the mechanical boundary conditions. A convenient
round threshold is 1000; a system at $\mathrm{Ra} \sim 10^7$ is not marginally
convecting, it is in the fully developed turbulent regime.

### 2.2 From the Rayleigh number to a heat flux

At high Ra the transport is organised into thin boundary layers of thickness
$\delta$, with an interior that is nearly isothermal along the adiabat. Balancing
conduction across the layer against convection of the interior:

$$\frac{k\Delta T}{\delta} \sim \rho c_p \,\bar u\,\Delta T . \tag{9}$$

A scaling argument for the boundary-layer thickness — the classical
"Malkus–Howard" or marginal-stability assumption that the layer adjusts itself so
that its own local Rayleigh number sits at the critical value,
$\rho g\alpha\Delta T\delta^3/(\kappa\eta) \sim \mathrm{Ra}_c$ — gives

$$\delta \sim d\,\mathrm{Ra}^{-1/3} \qquad\Longrightarrow\qquad
\mathrm{Nu} \equiv \frac{q_{\text{conv}}}{q_{\text{cond}}} = \frac{d}{\delta}
\sim \mathrm{Ra}^{1/3} . \tag{10}$$

Equation (10) is the **one-third-power scaling**. Empirically, with a prefactor,

$$\mathrm{Nu} \approx 0.1\,\mathrm{Ra}^{1/3} , \tag{11}$$

which is the form used in this lesson's demo.

**Regime of validity.** Equations (10) and (11) assume: a plane layer, no internal
heating, no phase changes, negligible inertia (infinite Prandtl number, true for
the mantle, false for air), constant viscosity, and both boundaries rigid or both
free. Every one is violated in the Earth somewhere. For the mantle the two serious
failures are the strongly temperature-dependent viscosity and the internal
heating; both raise the exponent and the prefactor, and a mantle calculation must
use the boundary-layer or mean-field scaling rather than equation (11).

### 2.3 Why a solid mantle convects

The mantle is rock, yet it convects on a geological timescale that makes it a
fluid. The resolution is that convection is not a property of a phase; it is a
property of a *timescale*. Rock subjected to a shear stress for long enough
deforms by solid-state creep at a rate $\dot\varepsilon = A\sigma^n
e^{-E_a/RT}$; the relevant material parameter is the effective viscosity
$\eta = \sigma/(2\dot\varepsilon)$, which for the mantle is of order
$10^{21}$ Pa s — about $10^{24}$ times water's, hence the entry in equation (7).

## 3. Computed cases

### 3.1 Rayleigh numbers

With $g = 9.806\,65$ m s⁻² (exact) and nominal material properties:

| System | $\rho$ (kg m⁻³) | $\alpha$ (K⁻¹) | $\Delta T$ (K) | $d$ (m) | $\kappa$ (m² s⁻¹) | $\eta$ (Pa s) | Ra | Ra/Ra$_c$ | Nu |
|---|---|---|---|---|---|---|---|---|---|
| Whole mantle | 3300 | 3 × 10⁻⁵ | 2500 | 2.9 × 10⁶ | 10⁻⁶ | 10²¹ | 5.92 × 10⁷ | 5.9 × 10⁴ | 39.0 |
| Upper mantle | 3300 | 3 × 10⁻⁵ | 1300 | 6.6 × 10⁵ | 10⁻⁶ | 10²⁰ | 3.63 × 10⁶ | 3.6 × 10³ | 15.4 |
| Water, 1 m layer | 1000 | 2 × 10⁻⁴ | 10 | 1 | 1.43 × 10⁻⁷ | 10⁻³ | 1.37 × 10¹¹ | 1.4 × 10⁸ | 515 |
| Lava lake, 10 m | 2600 | 5 × 10⁻⁵ | 300 | 10 | 10⁻⁶ | 10² | 3.83 × 10⁹ | 3.8 × 10⁶ | 156 |

Every system exceeds the critical value by three to eight orders of magnitude.
**Convection is not marginal anywhere in geophysics.** It is the default state of
any fluid layer heated from below, from the outer core to the atmosphere. What
differs between the mantle and a lava lake is not whether convection happens but
how fast: metres per second in water, centimetres per year in the mantle.

### 3.2 Convective fluxes

Converting each Rayleigh number into a flux with equations (10)–(11) and
$q_{\text{cond}} = k\Delta T/d$:

| System | $q_{\text{cond}}$ (W m⁻²) | Nu | $q_{\text{conv}}$ (W m⁻²) |
|---|---|---|---|
| Whole mantle | 3.45 × 10⁻³ | 39.0 | 0.134 |
| Upper mantle | 7.88 × 10⁻³ | 15.4 | 0.121 |
| Water, 1 m layer | 6.00 | 515 | 3.09 × 10³ |
| Lava lake, 10 m | 54.0 | 156 | 8.44 × 10³ |

**Read the mantle row carefully.** The convective flux comes out at
$134$ mW m⁻², against an observed mean surface heat flow of order 90 mW m⁻²
(nominal). Agreement to a factor of 1.5 from such a crude calculation is the
sense in which the scaling is useful; it is a one-third-power law with an
empirical prefactor, not a prediction to two digits, and quoting it as one is the
commonest abuse of this section. The water and lava rows show what vigorous
convection really means: three to four orders of magnitude more flux than
conduction through the same layer.

### 3.3 Radiation

Blackbody flux and the radiative coefficient over the range that matters:

| $T$ (K) | $F = \sigma T^4$ (W m⁻²) | $h_{\text{rad}} = 4\sigma T^3$ (W m⁻² K⁻¹) | Example |
|---|---|---|---|
| 254.6 | 2.383 × 10² | 3.74 | Earth's effective radiating temperature |
| 288.0 | 3.901 × 10² | 5.42 | Earth's mean surface |
| 373.1 | 1.099 × 10³ | 11.8 | boiling water |
| 1000 | 5.670 × 10⁴ | 227 | hot lava crust |
| 1400 | 2.178 × 10⁵ | 622 | erupting lava |
| 5772 | 6.294 × 10⁷ | 43 616 | photosphere |

Raising a surface from 288 K to 1400 K multiplies its radiative flux by **558**.
No compositional change can compete: the $T^4$ is everything.

Two comparisons matter:

- $h_{\text{rad}} = 5.4$ W m⁻² K⁻¹ at 300 K is comparable with natural convection
  in air (5–25 W m⁻² K⁻¹). At ambient temperature, radiation and convection
  compete.
- $h_{\text{rad}} = 622$ W m⁻² K⁻¹ at 1400 K exceeds any convective coefficient.
  Above about 1000 K, radiation wins outright.

**Regime of validity.** Equation (2) is the blackbody law. A real surface is
described by an emissivity $\epsilon < 1$ that varies with wavelength, and a
partially transparent gas layer (the atmosphere) requires the radiative transfer
equation rather than a surface flux. The grey-body approximation with a single
$\epsilon$ is adequate to about 10 per cent for most geophysical surfaces and is
inadequate for the atmospheric greenhouse, where the wavelength dependence *is*
the physics.

### 3.4 Wien displacement

$$\lambda_{\max}T = 2.897\,772\times10^{-3}\ \mathrm{m\,K} : \quad
5772\ \text{K} \to 0.502\ \mu\text{m (visible)}, \quad
288\ \text{K} \to 10.06\ \mu\text{m (thermal IR)}, \quad
254.6\ \text{K} \to 11.38\ \mu\text{m}. \tag{12}$$

The Sun radiates in the visible and the Earth in the thermal infrared, and the two
spectra barely overlap. That separation is why the atmosphere can be transparent
to sunlight and opaque to infrared simultaneously — which is the greenhouse
effect, and why a single grey emissivity cannot describe a radiative balance
([16-02/03](../../16-atmosphere-climate/02-radiation-and-energy-balance/03-greenhouse-effect.md)).

### 3.5 The Earth's effective radiating temperature

With an absorbed flux per unit area $S(1-a)/4$ and $S = 1361$ W m⁻²,
$a = 0.30$ (both nominal):

$$F_{\text{abs}} = \frac{1361\times0.70}{4} = 238.175\ \mathrm{W\,m^{-2}},
\qquad
T_e = \left(\frac{238.175}{5.670\times10^{-8}}\right)^{1/4}
= 254.578\ \text{K} = -18.57\ ^\circ\text{C} . \tag{13}$$

The sensitivity follows by differentiating:

$$\frac{\mathrm{d}T_e}{\mathrm{d}S} = \frac{T_e}{4S} = 0.0468\
\mathrm{K\ per\ W\,m^{-2}} , \tag{14}$$

so a 1 per cent change in $S$ moves $T_e$ by 0.64 K. The fourth power is what makes
the surface temperature stable against modest changes in absorbed flux and
violent against large ones.

**And the geothermal flux, for scale:** at 87 mW m⁻² it is
3.7 × 10⁻⁴ of the absorbed solar flux. The Earth's internal heat engine is
irrelevant to surface climate and decisive for tectonics. Conflating the two is a
classic error, and equation (13) is the number that disposes of it.

### 3.6 Combined transfer at a lava surface

At 1400 K against 300 K air over 1 m of rock, with a nominal natural-convection
coefficient $h = 15$ W m⁻² K⁻¹:

| Mechanism | Flux (W m⁻²) | Share |
|---|---|---|
| Radiation | 2.178 × 10⁵ | 0.922 |
| Convection to air | 1.650 × 10⁴ | 0.070 |
| Conduction through 1 m of rock | 1.980 × 10³ | 0.008 |
| **Total** | 2.363 × 10⁵ | 1.000 |

Radiation carries 92 per cent. This is why lava lakes crust over only when the
crust suppresses radiation, and why a magma body at the surface cools by a
completely different mechanism from one at depth, where conduction into the host
rock takes over.

### 3.7 Advection versus conduction: the Péclet number

For an imposed flow of speed $v$, the Péclet number

$$\mathrm{Pe} = \frac{vL}{\kappa} \tag{15}$$

compares advective to conductive transport. For groundwater over $L = 1$ km with
$\kappa = 1.157\times10^{-6}$ m² s⁻¹:

| $v$ (m yr⁻¹) | Pe | Regime |
|---|---|---|
| 0.01 | 0.274 | conduction |
| 0.0365 | 1.000 | crossover |
| 0.10 | 2.74 | advection |
| 1.0 | 27.4 | advection |
| 10 | 274 | advection |
| 100 | 2739 | advection |

The crossover is at $v = \kappa/L = 1.157\times10^{-9}$ m s⁻¹ =
**3.65 cm yr⁻¹**. Groundwater moving faster than a few centimetres per year
carries more heat than conduction does over a kilometre, which is why heat flow in
sedimentary basins and geothermal fields is routinely dominated by fluid flow, and
why a conductive geotherm fitted to a well in an aquifer province can be badly
wrong.

The Péclet number is the right tool when the flow is imposed from outside. When
the flow organises itself by buoyancy there is no externally set velocity, and the
Rayleigh number is the right tool instead.

## 4. Physical interpretation

**Convection is a stiffening of the temperature gradient, not a replacement of
conduction.** All the heat still crosses the boundary layers by conduction; what
convection does is thin them. $\mathrm{Nu} = d/\delta$ is literally the ratio of
the layer thickness to the boundary-layer thickness. That is why
$\mathrm{Nu} \sim \mathrm{Ra}^{1/3}$ and not some exponential.

**The Rayleigh number is a ratio, and every factor in it is a story.** $d^3$ is
why big systems convect. $\eta$ is why the mantle needs $10^8$ yr per overturn
while a lava lake turns over in seconds. $\kappa$ is why the mantle would not
convect if it conducted its heat away faster. $\alpha$ is why near-incompressible
materials are hard to convect.

**Radiation is a surface phenomenon and conduction is a volume phenomenon.**
Radiation from a body scales with its *area*; conduction into it scales with
gradient. That is why a lava body cools radiatively when small and conductively
when large, and why the crossover is a size, not a temperature.

**$T^4$ vs $T^3$.** The flux goes as $T^4$, the coefficient as $T^3$, and the
optical peak as $1/T$. All three exponents recur in every radiative problem in
this curriculum, and getting them right is most of the arithmetic.

**Dimensionless numbers are the same number read differently.** Ra says whether
convection happens; Nu says how much heat it carries; Pe says whether an imposed
flow beats conduction. All three are ratios of a transport term to a diffusive
term, and the only trick is knowing which transport.

## 5. Assumptions and regime of validity

| Approximation | Statement | What breaks outside it |
|---|---|---|
| Boussinesq approximation | Density varies only in the buoyancy term | Compressible convection, which matters for the outer core and the deep mantle |
| Constant $\eta$ | Equation (7) is a number | Mantle viscosity varies by orders of magnitude with temperature; use a temperature-dependent law |
| No internal heating | Equations (10)–(11) | The mantle is substantially internally heated; the scaling changes |
| No phase changes | One material | Melting, and the 410/660 transitions, which add latent-heat and buoyancy terms |
| Infinite Prandtl number | Inertia negligible | Holds for the mantle, fails for air and water |
| Rigid or free boundaries | Equation (8) | Real boundary conditions are mixed and time-dependent |
| Blackbody radiation | Equation (2) | Grey or wavelength-dependent emissivity; a transparent atmosphere |
| Steady radiative balance | Equation (13) | On glacial timescales the planetary heat content changes |
| Imposed flow for Pe | Equation (15) | Buoyancy-driven flow; use Ra |

## 6. Units and dimensional analysis

- Ra: $\mathrm{kg\,m^{-3}}\cdot\mathrm{m\,s^{-2}}\cdot\mathrm{K^{-1}}\cdot
  \mathrm{K}\cdot\mathrm{m^3}/(\mathrm{m^2\,s^{-1}}\cdot\mathrm{kg\,m^{-1}\,s^{-1}})$
  $= 1$ ✓. A non-zero net unit means a substituted quantity.
- Nu $= q_{\text{conv}}/q_{\text{cond}}$ and $= d/\delta$: dimensionless ✓, and
  **always $\ge 1$** in a convecting layer. A computed Nu below 1 is a sign that
  the layer is not convecting and the scaling is being applied outside its regime.
- $\sigma T^4$: $\mathrm{W\,m^{-2}K^{-4}}\cdot\mathrm{K^4} =
  \mathrm{W\,m^{-2}}$ ✓. $4\sigma T^3$: $\mathrm{W\,m^{-2}K^{-1}}$ ✓, the same
  units as a convective $h$.
- $F_{\text{abs}} = S(1-a)/4$: the factor 4 is the ratio of the sphere's surface
  area to its cross-section, and omitting it makes the Earth 60 K too hot.
- Wien: $hc/(xk_B)$ is $\mathrm{J\,s}\cdot\mathrm{m\,s^{-1}}/\mathrm{J\,K^{-1}}
  = \mathrm{m\,K}$ ✓.
- Pe: dimensionless ✓. For the mantle with $v = 5$ cm yr⁻¹, $L = 2900$ km and
  $\kappa = 10^{-6}$ m² s⁻¹, Pe ≈ 4.6 — but this is the wrong number to quote,
  because the mantle's velocity is an *output* of the convection, not an input.
- **Useful anchors**: $\mathrm{Ra}_c \approx 10^3$; the mantle at
  $\mathrm{Ra} \sim 10^7$; $\mathrm{Nu} \sim 10$–$10^2$ in the mantle;
  $f_{\text{geothermal}}/f_{\text{solar}} \sim 4\times10^{-4}$;
  $\lambda_{\max} \approx 10\ \mu$m for the Earth and $0.5\ \mu$m for the Sun.

## 7. Python demonstration

[`code/convection_radiation_demo.py`](./code/convection_radiation_demo.py)
computes Rayleigh and Nusselt numbers for four systems, blackbody fluxes and
radiative coefficients, the Earth's effective temperature, the combined balance at
a lava surface, Wien wavelengths and Péclet numbers. Observed output:

```text
system                    Ra     Ra/Ra_c   Nu = 0.1 Ra^1/3
whole mantle       5.920e+07   5.920e+04             38.97
upper mantle       3.629e+06   3.629e+03             15.37
water 1 m          1.369e+11   1.369e+08            515.35
lava lake 10 m     3.825e+09   3.825e+06            156.38
```

```text
system             q_cond (W/m2)        Nu   q_conv (W/m2)
whole mantle          3.4483e-03      39.0      1.3439e-01
upper mantle          7.8788e-03      15.4      1.2107e-01
water 1 m             6.0000e+00     515.3      3.0921e+03
lava lake 10 m        5.4000e+01     156.4      8.4448e+03
```

```text
     T (K)        F (W/m2)    h_rad (W/m2/K)   example                           
     254.6      2.3826e+02            3.7432   Earth effective radiating temperature
     288.0      3.9011e+02            5.4181   Earth mean surface                
     373.1      1.0994e+03           11.7848   boiling water                     
    1000.0      5.6704e+04          226.8150   hot lava crust                    
    1400.0      2.1783e+05          622.3803   erupting lava                     
    5772.0      6.2939e+07        43616.4882   photosphere                       
```

```text
  absorbed flux per unit area, S(1-a)/4 = 238.1750 W/m2
  T_e = (S(1-a)/(4 sigma))^(1/4) = 254.5781 K = -18.57 C

  Sensitivity: dT_e/dS = T_e/(4S) = 0.046763 K per W/m2, so a 1 per cent change in S
  moves T_e by 0.636 K.

  For comparison, the geothermal flux of ~0.087 W/m2 is
  3.653e-04 of the absorbed solar flux.
```

```text
mechanism                      flux (W/m2)       share
radiation                       2.1783e+05    0.921799
conduction through 1 m rock      1.9800e+03    0.008379
natural convection in air       1.6500e+04    0.069823
total                           2.3631e+05    1.000000
```

```text
  x = 4.965114232,  b = 2.897772e-03 m K  (= 2.89777 mm K)
     T (K)   lambda_max (um)          band
 5772.0000            0.5020       visible
 1400.0000            2.0698       near IR
  288.0000           10.0617    thermal IR
  254.5781           11.3826    thermal IR
```

```text
    v (m/yr)       v (m/s)          Pe                regime
      0.0100    3.1688e-10      0.2739            conduction
      0.0365    1.1566e-09      0.9997            conduction
      0.1000    3.1688e-09      2.7388             advection
      1.0000    3.1688e-08     27.3881             advection
     10.0000    3.1688e-07    273.8815             advection
    100.0000    3.1688e-06   2738.8148             advection

  The crossover is at v = kappa/L = 1.1570e-09 m/s = 3.651 cm/yr.
```

### What to observe

| Observation | Consequence |
|---|---|
| All four systems have $\mathrm{Ra} \gg \mathrm{Ra}_c$ | Convection is the norm, not the exception |
| Mantle Ra is $10^{14}$ below a metre of water | Viscosity, entering linearly, spans 24 orders of magnitude |
| $\mathrm{Nu} = 39$ for the whole mantle gives 134 mW m⁻² | Within a factor of ~1.5 of the observed mean; a scaling, not a fit |
| $h_{\text{rad}}$ is 5.4 at 300 K and 622 at 1400 K | The $T^3$ makes radiation negligible cold and dominant hot |
| $T_e = 254.58$ K from an adopted $S$ and albedo | The planetary temperature is an energy-balance result, not a fitted one |
| Geothermal flux is 3.65 × 10⁻⁴ of absorbed solar | The two heat engines are separated by three and a half orders of magnitude |
| Radiation takes 92 per cent at a lava surface | Hot surfaces lose heat by photons, not by contact |
| Wien peaks at 0.50 µm and 11.4 µm | The solar and terrestrial spectra are disjoint, which is the greenhouse mechanism |
| Pe crosses 1 at 3.65 cm yr⁻¹ | Groundwater flows faster than that dominate conduction over a kilometre |

> **Breaking exercise.** Change the mantle viscosity from $10^{21}$ to
> $10^{23}$ Pa s and predict, before running, the new Ra and Nu and the new
> convective flux. Then explain why the flux drops by only a factor of about five
> when the viscosity rises by a hundred — the answer is in the exponent of
> equation (10).

## 8. Common mistakes

1. **Using the Rayleigh number outside its regime and trusting the digits.**
   Equation (11) gives a factor-of-two answer for the mantle, not a
   three-significant-figure one.
2. **Quoting Nu below 1.** A convecting layer always transports more than the
   conductive baseline; $\mathrm{Nu} < 1$ means the scaling has been misapplied.
3. **Forgetting the factor 4 in $S(1-a)/4$.** The planetary flux is diluted by the
   ratio of surface area to cross-section; omitting it puts the Earth at ~320 K.
4. **Using °C in $\sigma T^4$.** The law is in kelvin. Using 15 instead of 288
   makes the flux smaller by a factor of $3.9\times10^5$.
5. **Assuming blackbody for a real surface.** $\epsilon$ for rock is 0.7–0.95 and
   varies with wavelength and roughness; a 20 per cent emissivity error is a
   20 per cent flux error.
6. **Treating the atmosphere as a grey absorber.** The greenhouse effect is
   entirely a wavelength-dependent phenomenon; a grey atmosphere with the observed
   absorptivity gives the wrong surface temperature.
7. **Applying the Péclet number to a buoyancy-driven flow.** There is no imposed
   $v$ in the mantle; using a nominal plate speed as if it were an input is a
   category error.
8. **Believing convection needs a liquid.** Solid-state creep gives an effective
   viscosity; the mantle is a fluid on $10^8$ yr.
9. **Comparing a flux with a temperature.** "Radiation dominates because it is
   hotter" is not an argument; put both in W m⁻².
10. **Assuming the mantle's heat transport is conduction at depth but convection
    in the interior.** The whole mantle convects; the lithosphere is the
    conductive lid, and its thickness is where the two gradients meet.

## 9. Real-world applications

- **Mantle convection and plate tectonics.** Ra is the criterion; Nu gives the
  heat flux; the temperature-dependent viscosity is the complication
  ([13-02/01](../../13-geodynamics-tectonics/02-mantle-convection/01-rayleigh-benard-mantle.md),
  [02-06/06](../06-fluid-mechanics/06-mantle-convection.md)).
- **Core dynamics and the geodynamo.** The outer core convects compositionally
  and thermally; the same Rayleigh-number logic applies with a compositional
  buoyancy term added ([12-02/04](../../12-global-geophysics-interior/02-composition-and-mineral-physics/04-core-composition.md)).
- **Geothermal and hydrothermal systems.** Whether a field is dominated by
  conduction or by fluid advection is a Péclet-number question
  ([05-09/03](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/03-geothermal-exploration.md)).
- **Volcano monitoring and lava cooling.** The radiative-to-convective switch at
  ~1000 K controls crust formation, and hence the thermal signature a satellite
  sees ([13-06/02](../../13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/02-volcano-geodesy.md)).
- **Planetary energy balance and climate.** $T_e = (S(1-a)/4\sigma)^{1/4}$ is the
  zero-dimensional climate model, the starting point for every energy-balance
  model ([16-02/04](../../16-atmosphere-climate/02-radiation-and-energy-balance/04-earth-energy-balance.md)).
- **Remote sensing.** Wien's law sets the band, and Planck's law sets the
  radiance–temperature relation; every thermal infrared instrument is calibrated
  against equation (1).
- **Building and ground engineering.** $h_{\text{rad}}$ and $h_{\text{conv}}$ are
  combined into a single surface coefficient for ground heat-exchanger design.

## 10. Further reading

- **Turcotte, D. L., & Schubert, G. *Geodynamics* (3rd ed., Cambridge University
  Press, 2014).** The Rayleigh number, boundary-layer scaling, and mantle
  convection with temperature-dependent viscosity. Level: graduate.
- **Chandrasekhar, S. *Hydrodynamic and Hydromagnetic Stability* (Dover).** The
  linear stability problem and the exact $\mathrm{Ra}_c$ values for each pair of
  boundary conditions. Level: advanced.
- **Incropera, F. P., & DeWitt, D. P. *Fundamentals of Heat and Mass Transfer*
  (Wiley).** Convection correlations, the radiative coefficient, and the combined
  coefficients used in §3.6. Level: intermediate.
- **Goody, R. M., & Yung, Y. L. *Atmospheric Radiation* (2nd ed., Oxford
  University Press).** Planck's law, Wien's law and the radiative transfer that
  replaces the grey approximation. Level: advanced.
- **Schubert, G., Turcotte, D. L., & Olson, P. *Mantle Convection in the Earth and
  Planets* (Cambridge University Press).** The full treatment, including
  internally heated and mixed-mode convection. Level: doctoral.
- **Stüwe, K. *Geodynamics of the Lithosphere* (2nd ed., Springer, 2007).**
  Conductive lids, convective interiors, and the lithosphere-asthenosphere
  boundary as a Rayleigh-number transition. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [04 Heat Conduction, Fourier's Law and Thermal Diffusivity](./04-heat-conduction.md)
  — the diffusive baseline against which both other modes are measured.
- [06 Geotherms, Heat Flow and the Earth's Thermal Budget](./06-geotherms.md) —
  where the convective flux appears in the global budget.
- [02-06-06 Mantle Convection and Rayleigh–Bénard Instability](../06-fluid-mechanics/06-mantle-convection.md)
  — the instability derived in full.
- [02-06-05 Flow in Porous Media: Darcy's Law and Permeability](../06-fluid-mechanics/05-porous-media-flow.md)
  — where the Péclet number of §3.7 comes from.
- [16-atmosphere-climate/02 Radiation and Energy Balance](../../16-atmosphere-climate/02-radiation-and-energy-balance/01-solar-and-terrestrial-radiation.md)
  — the planetary energy budget in full.
- [13-geodynamics-tectonics/02 Mantle Convection](../../13-geodynamics-tectonics/02-mantle-convection/README.md)
  — the geophysical consequences.

Exercises:
[`exercises/05-convection-radiation-exercises.md`](./exercises/05-convection-radiation-exercises.md)
and
[`exercises/05-convection-radiation-solutions.md`](./exercises/05-convection-radiation-solutions.md).

## Self-assessment checklist

- [ ] I can derive the Rayleigh number by non-dimensionalising the Boussinesq
      equations, and explain each factor. (§2.1)
- [ ] I can compute Ra for a given layer and compare it with $\mathrm{Ra}_c$.
      (§3.1)
- [ ] I can derive $\mathrm{Nu} \sim \mathrm{Ra}^{1/3}$ from a boundary-layer
      argument and state its regime of validity. (§2.2)
- [ ] I can convert a Rayleigh number into a convective heat flux and compare it
      with an observed value, stating the accuracy honestly. (§3.2)
- [ ] I can compute $\sigma T^4$ and $4\sigma T^3$ and decide which of radiation
      and convection dominates. (§3.3, §3.6)
- [ ] I can compute the Earth's effective radiating temperature and its
      sensitivity to the absorbed flux. (§3.5)
- [ ] I can use Wien's law to place a body's emission in the spectrum. (§3.4)
- [ ] I can compute a Péclet number and state whether advection or conduction
      controls a temperature field. (§3.7)
- [ ] I can list at least three ways the real mantle violates the assumptions of
      equation (11). (§5)
