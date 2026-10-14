---
id: 02-10-03
title: "Radiative Transfer, Blackbody Radiation and Kirchhoff's Law"
level: graduate
prereqs: ["02-10-02", "02-05-05", "02-07-05"]
estimated_minutes: 90
tags: [radiative-transfer, planck, kirchhoff, emissivity, brightness-temperature, remote-sensing]
---

# Radiative Transfer, Blackbody Radiation and Kirchhoff's Law

Every satellite radiometer, every thermal camera, every infrared thermometer and
every planetary energy-balance model is an application of four equations: the
Planck function, the Stefan–Boltzmann law, Wien's displacement law and the
radiative transfer equation. This lesson derives them, verifies them numerically,
and computes the numbers that appear in real retrievals — the optical depth at
which an atmosphere becomes opaque, the brightness-temperature error caused by
an emissivity assumption, and the sensitivity of a thermal measurement to a
radiance error.

The four equations:

$$B_\lambda(T) = \frac{2hc^2}{\lambda^5}\frac{1}{e^{hc/\lambda k_BT}-1},
\qquad
F = \sigma T^4, \qquad
\lambda_{\max}T = \frac{hc}{xk_B}, \qquad
\frac{\mathrm dI}{\mathrm d\tau} = -I + S . \tag{1}$$

The first three are one law and two of its consequences — §3 proves that
numerically rather than asserting it. The fourth is the transport equation that
turns a radiance measurement into a temperature or a composition.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** radiance, irradiance, flux and intensity, and use the solid
   angle that converts one into another.
2. **Derive** the Wien and Stefan–Boltzmann laws from the Planck function, and
   verify each numerically: the integral of $x^3/(e^x-1)$ against $\pi^4/15$, and
   the maximum of $B_\lambda$ against the root of $x = 5(1-e^{-x})$.
3. **Derive** the radiative transfer equation for a plane-parallel medium
   without scattering, solve it for an isothermal layer over a surface, and
   interpret the optical-depth dependence.
4. **State and use Kirchhoff's law**, $\epsilon = \alpha$, and convert between
   emissivity and reflectance.
5. **Compute** a brightness temperature with the inverse Planck function and
   state the emissivity assumption's error in kelvin.
6. **Compute** the band-integrated fraction of a blackbody spectrum and explain
   why the thermal infrared window matters.
7. **Compute** a planetary effective temperature from an adopted solar constant
   and albedo, and explain why a grey single-layer atmosphere overshoots.
8. **State** the regime of validity of each approximation and identify the
   observation that would falsify it.

## Prerequisites

- [02-10-02 Interference and Diffraction in Optical Instruments](./02-interference-diffraction-optics.md)
  — how the measurement is made, and the resolution it can achieve.
- [02-05-05 Convection, Radiation and Combined Heat Transfer](../05-thermodynamics/05-convection-radiation.md)
  — the $T^4$ flux, the radiative heat-transfer coefficient $4\sigma T^3$ and the
  planetary energy balance, treated there as heat transfer.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../07-electromagnetism/05-em-waves.md)
  — what the radiation *is*: a propagating electromagnetic field with a
  well-defined Poynting flux.

## 1. Radiometric quantities and the solid angle

Radiometry is a bookkeeping discipline, and nearly every error in it is a
missing solid angle. The four quantities:

| Quantity | Symbol | Unit | Meaning |
|---|---|---|---|
| Radiant flux | $\Phi$ | W | Power through a surface |
| Irradiance | $E$ | W m⁻² | Flux *incident* on a surface per unit area |
| Radiance | $L$ | W m⁻² sr⁻¹ | Flux per unit area per unit solid angle |
| Intensity | $I$ | W sr⁻¹ | Flux per unit solid angle from a source |

A satellite radiometer measures **radiance**, because it accepts light from one
small solid angle; an energy-balance model uses **irradiance**, because it sums
over all directions. The conversion for a Lambertian (isotropic) emitter is

$$E = \pi L \quad\text{(hemispherical flux from a Lambertian surface)} , \tag{2}$$

and the $\pi$ is not a fudge: it is $\int_{\text{hemisphere}}\cos\theta\,
\mathrm d\Omega = \pi$. Confusing $L$ with $E$ is the commonest photometric
error, and the demo computes both sides of it:

```text
    rho  theta (deg)   L (W/m2/sr)
   0.05          0.0       21.6610
   0.20          0.0       86.6440
   0.20         30.0       75.0359
   0.20         60.0       43.3220
   0.50          0.0      216.6099
```

at $L = \rho E\cos\theta/\pi$ with $E = 1361$ W m⁻² (an adopted nominal solar
constant). For a reflectance of 0.20 at normal incidence the radiance is
86.64 W m⁻² sr⁻¹; the radiance of the same surface is not 272.2 W m⁻² sr⁻¹,
because the cosine-weighted hemisphere average supplies the $\pi$.

## 2. The Planck function

### 2.1 The two forms

The spectral radiance of a blackbody is

$$B_\lambda(T) = \frac{2hc^2}{\lambda^5}\frac{1}{e^{hc/\lambda k_BT}-1}
\quad [\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}] , \tag{3}$$

or, per unit frequency,

$$B_\nu(T) = \frac{2h\nu^3}{c^2}\frac{1}{e^{h\nu/k_BT}-1}
\quad [\mathrm{W\,m^{-2}\,sr^{-1}\,Hz^{-1}}] . \tag{4}$$

They describe the same field and are related by the Jacobian
$\mathrm d\nu/\mathrm d\lambda = -c/\lambda^2$:

$$B_\lambda = B_\nu\left|\frac{\mathrm d\nu}{\mathrm d\lambda}\right|
= \frac{c}{\lambda^2}B_\nu . \tag{5}$$

The demo's first section checks (5) for five temperature–wavelength pairs and
prints the ratio $B_\lambda(\lambda^2/c)/B_\nu$, which is 1.00000000 throughout:

```text
   T (K)   lambda (um)   B_lambda (W/m2/sr/um)       B_nu (W/m2/sr/Hz)       ratio
     300         10.00            9.924033e+00            3.310301e-12  1.00000000
     300          0.55            3.193330e-29            3.222170e-44  1.00000000
    5772          0.50            2.623854e+07            2.188059e-08  1.00000000
    1000          2.00            2.797947e+03            3.733179e-11  1.00000000
     255         11.00            4.404570e+00            1.777740e-12  1.00000000
```

The Jacobian matters in practice: a blackbody curve peaks at
$\lambda = 2898/T$ µm but at $\nu = 5.879\times10^{10}T$ Hz, and those two peaks
are **not** related by $\lambda\nu = c$. A spectrum quoted per micron looks
different from one quoted per wavenumber, and a retrieval that mixes the two
conventions produces a biased temperature. The demo's constants are
$c_1 = 2hc^2 = 1.191043\times10^{-16}$ W m² and
$c_2 = hc/k_B = 1.438777\times10^{-2}$ m K.

### 2.2 Planck in exponential form, and numerical care

Implementing (3) naively overflows: at $\lambda = 0.5$ µm and $T = 255$ K the
Planck variable is $x = c_2/(\lambda T) = 112.8$, and $e^x$ exceeds $10^{48}$ —
representable, but $e^{700}$ and beyond is not. The demo uses `math.expm1(x)` for
$e^x-1$, which also preserves precision when $x$ is small, and falls back to the
Wien limit $c_1\lambda^{-5}e^{-x}$ for $x>700$. Choosing the numerically stable
branch of a formula is part of using it.

## 3. Verifying Wien and Stefan–Boltzmann numerically

### 3.1 Stefan–Boltzmann from the Planck integral

Integrating (3) over all wavelengths and substituting
$x = c_2/(\lambda T)$ gives

$$F = 2\pi k_B^4\frac{T^4}{h^3c^2}\int_0^\infty\frac{x^3}{e^x-1}\,
\mathrm dx
= \frac{2\pi^5k_B^4}{15h^3c^2}T^4 \equiv \sigma T^4 , \tag{6}$$

because the integral is $\Gamma(4)\zeta(4) = 6\pi^4/90 = \pi^4/15$. The demo
computes the integral with Simpson's rule and then forms $\sigma$ from the
*measured* integral, not from the closed form:

```text
  Simpson, n =   2001, x_max =   40: int = 6.493939404923
  Simpson, n =  20001, x_max =   40: int = 6.493939402267
  Simpson, n = 200001, x_max =   60: int = 6.493939402266

  int x^3/(e^x-1) dx = 6.493939402266
  pi^4/15            = 6.493939402267
  relative difference = 1.372e-13

  sigma from the *numerically integrated* Planck function,
    sigma = 2 pi k^4/(h^3 c^2) * int x^3/(e^x-1) dx =
    5.670374419184e-08 W m^-2 K^-4
  exact (SI defining constants, truncated here to 10 digits) =
    5.670374419000e-08 W m^-2 K^-4
  relative difference = 3.239e-11
```

Three things to read here. First, the integral converges to $\pi^4/15$ at the
$10^{-13}$ level as the grid is refined, so the quadrature is verified to the
level of the arithmetic. Second, $\sigma$ derived from the numerically
integrated Planck function agrees with the exact SI value to $3\times10^{-11}$,
which is the truncation of the exact value shown to ten digits plus the
quadrature error — not a physical discrepancy. Third, **$\sigma$ is not an
independent constant**: it is $2\pi^5k_B^4/(15h^3c^2)$, and because $h$, $c$ and
$k_B$ are exact by definition since 2019, $\sigma$ is exact too. That is why the
value $\sigma = 5.670\,374\,419\times10^{-8}$ W m⁻² K⁻⁴ may be quoted to the
digits shown, unlike every emissivity in this lesson.

### 3.2 Wien's displacement law

Maximising $B_\lambda$ over $\lambda$ gives the transcendental equation

$$x = 5\left(1-e^{-x}\right), \qquad x = \frac{hc}{\lambda_{\max}k_BT}
= 4.965\,114\,231\,744\ldots, \tag{7}$$

and hence

$$b = \frac{hc}{xk_B} = 2.897\,771\,955\times10^{-3}\ \mathrm{m\,K} . \tag{8}$$

The demo verifies it by two independent routes — a ternary search on
$B_\lambda(T)$ and a bisection on $x-5(1-e^{-x})$:

```text
  T =  5772.0 K: lambda_max =   0.502039 um, x = 4.965114220206

  x = 5(1-e^-x) solved by bisection gives x = 4.965114231744.
  b = c2/x  = 2.897771955185e-03 m K
  published = 2.897771955000e-03 m K
  relative difference = 6.390e-11
```

The two routes agree to $10^{-12}$ and reproduce the published constant to
$6\times10^{-11}$. The displacement law is therefore **not a separate law**: it
is the location of the Planck maximum, and the constant $x$ is a pure number
obtained from a transcendental equation that has nothing to do with the Earth.

Computed warm- and cold-body cases:

```text
     T (K)      sigma T^4 (W/m2)    4 sigma T^3 (W/m2/K)   lambda_max (um)
     100.0          5.670374e+00            2.268150e-01           28.9777
     255.0          2.397576e+02            3.760904e+00           11.3638
     288.0          3.901052e+02            5.418127e+00           10.0617
     300.0          4.593003e+02            6.124004e+00            9.6592
    1000.0          5.670374e+04            2.268150e+02            2.8978
    1400.0          2.178331e+05            6.223803e+02            2.0698
    5772.0          6.293859e+07            4.361649e+04            0.5020
```

Read the 288 K row: the Earth's surface radiates 390 W m⁻² and peaks at
10.0617 µm, squarely in the thermal infrared. The 5772 K row peaks at 0.502 µm,
in the visible. The two spectra barely overlap, which is the entire physical
basis of the greenhouse effect — and also why no single grey emissivity can
describe an atmosphere (lesson [16-02/03](../../16-atmosphere-climate/02-radiation-and-energy-balance/03-greenhouse-effect.md)).

## 4. Energy in bands

The fraction of a blackbody's total flux between two wavelengths follows from
the same substitution:

$$f(\lambda_1,\lambda_2,T) = \frac{15}{\pi^4}\int_{x_2}^{x_1}
\frac{x^3}{e^x-1}\,\mathrm dx , \tag{9}$$

with $x_i = c_2/(\lambda_iT)$. The demo computes:

```text
   T (K)  band                        fraction
     288  visible 0.40-0.70 um        0.000000
     288  SWIR 1.55-1.75 um           0.000000
     288  thermal 8-14 um             0.365826
     288  thermal 10-12 um            0.127626
     288  thermal 3-5 um              0.009559
     300  thermal 8-14 um             0.375742
     300  thermal 10-12 um            0.130369
    5772  visible 0.40-0.70 um        0.366383
    5772  SWIR 1.55-1.75 um           0.027734
    5772  thermal 8-14 um             0.001108
```

At 288 K, **36.6 per cent of the emitted terrestrial flux lies between 8 and
14 µm**, the atmospheric window, and 12.8 per cent between 10 and 12 µm alone.
At 5772 K, 36.6 per cent of the solar flux is in the visible. That numerical
coincidence is why a thermal infrared radiometer in the 10–12 µm band measures
the surface rather than the air, and why land surface temperature is retrievable
at all: a third of the radiation leaves through a window the atmosphere mostly
transmits, and a further third arrives from the Sun as visible light that the
atmosphere transmits almost perfectly.

## 5. The radiative transfer equation

### 5.1 Derivation

Consider a beam of radiance $I$ crossing a slab of thickness $\mathrm dz$ with
absorption coefficient $\kappa_\rho\rho$ (per metre), which both absorbs and, in
local thermodynamic equilibrium at temperature $T$, emits. Over $\mathrm dz$:

$$\mathrm dI = -\kappa_\rho\rho\,I\,\mathrm dz + \kappa_\rho\rho\,B(T)\,
\mathrm dz . \tag{10}$$

Defining the **optical depth** $\mathrm d\tau = \kappa_\rho\rho\,\mathrm dz$
measured inward (so $I$ decreases with increasing $\tau$ in the outward
direction), (10) becomes the **Schwarzschild equation**:

$$\frac{\mathrm dI}{\mathrm d\tau} = -I + B(T) , \tag{11}$$

the form quoted in (1). Its solution for the radiance leaving an isothermal layer
of temperature $T_a$ and optical depth $\tau$ over a surface of radiance $I_s$ is

$$I = B(T_a)\left(1-e^{-\tau}\right) + I_s e^{-\tau} . \tag{12}$$

Two limits are immediate: a thin layer ($\tau\to0$) passes the surface radiance
through, and a thick layer ($\tau\to\infty$) replaces it with the layer's own
emission. The demo computes the transition, with a surface at 290 K and a layer
at 250 K observed at 10 µm:

```text
     tau    I (W/m2/sr/um)     T_B (K)   emissivity 1-e^-tau
    0.01          8.354746     289.682              0.009950
    0.10          7.961304     286.914              0.095163
    0.30          7.203996     281.342              0.259182
    1.00          5.482066     267.148              0.632121
    3.00          4.013373     252.580              0.950213
   10.00          3.783707     250.002              0.999955
   30.00          3.783497     250.000              1.000000
```

$T_B$ is the **brightness temperature**, obtained by inverting the Planck
function: the temperature a blackbody would need to emit the measured radiance
at that wavelength. At $\tau = 0.01$ the radiometer sees 289.68 K, essentially
the surface. At $\tau = 3$ it sees 252.58 K; at $\tau \ge 10$ it sees 250.000 K,
the layer, and the surface has vanished from the measurement. **Optical depth of
order one is the transition between seeing through and seeing only the
medium** — the same criterion as the seismic skin depth of a thin bed.

Inverting (3) is done analytically rather than numerically:

$$T_B = \frac{c_2}{\lambda}\left[\ln\!\left(1 + \frac{c_1}{\lambda^5 I}\right)
\right]^{-1} . \tag{13}$$

Getting (13) right matters: a common implementation error is to write
$\ln(1+X)$ as $\ln(1/X)$, which returns a temperature of order $10^5$ K instead
of 290 K while still "increasing with radiance" and therefore passing a
sanity check that only looks at the trend. The demo's implementation is
$\ln(1+c_1/(\lambda^5I))$, and the table above is the verification: at
$\tau\to0$ it returns the surface temperature to three decimals.

### 5.2 Kirchhoff's law

In local thermodynamic equilibrium the emissivity of a body at a given
wavelength and direction equals its absorptivity:

$$\epsilon(\lambda,\theta,\phi) = \alpha(\lambda,\theta,\phi) . \tag{14}$$

For an opaque body, energy conservation at the surface gives
$\alpha + \rho = 1$, so

$$\boxed{\ \epsilon = 1 - \rho\ } \tag{15}$$

at the same wavelength, direction and temperature. Three consequences are used
constantly:

- **The emissivity of an isothermal slab is exactly $1-e^{-\tau}$.** The last
  column of the table above is that identity; it is where the "emissivity" of an
  atmosphere comes from.
- **A reflectance spectrum predicts an emissivity spectrum.** This is why
  laboratory spectral libraries measured in reflectance (lesson
  [02-10-04](./04-spectroscopy.md)) are used to interpret thermal infrared
  measurements.
- **A perfect reflector is a perfect non-emitter** ($\rho = 1 \Rightarrow
  \epsilon = 0$), which is why a metal roof has a low thermal signature and why
  the thermal infrared is a compositional remote-sensing tool rather than a
  pure thermometer.

### 5.3 Brightness temperature and the emissivity assumption

The **brightness temperature** of a greybody is

$$T_B = \epsilon^{1/4}T \tag{16}$$

for a broadband observation. The demo computes the flux and the error introduced
by assuming $\epsilon = 1$, using a nominal emissivity range for rock and soil
in the thermal infrared rather than a single "fact":

```text
  epsilon  F = e sigma T^4 (W/m2)   change vs e=1    T_B if e=1 assumed (K)
     0.90                413.3703         -10.00%                  292.2011
     0.92                422.5563          -8.00%                  293.8111
     0.94                431.7423          -6.00%                  295.3951
     0.95                436.3353          -5.00%                  296.1776
     0.96                440.9283          -4.00%                  296.9539
     0.98                450.1143          -2.00%                  298.4886
```

With a true emissivity of 0.93 at 300 K, assuming $\epsilon = 1$ returns
294.606 K: an error of **−5.394 K** from the emissivity assumption alone. Any
thermal product quoted without an emissivity treatment carries an error of this
order, and any method section quoting "the emissivity of rock" as a single value
is describing a quantity that varies with mineralogy, grain size, roughness,
moisture and wavelength. Use a nominal range and a spectral library.

**Emissivity values are ranges, not facts.** They vary with surface state, and
the honest statement is "0.90–0.96 for typical dry rock and soil in the thermal
infrared, from a spectral library or a laboratory measurement at the relevant
wavelength and viewing geometry" — never "rock has emissivity 0.95".

### 5.4 Sensitivity of a thermal measurement

Differentiating (3) with respect to $T$ at fixed $\lambda$ gives the fractional
radiance change per kelvin,

$$\frac{1}{L}\frac{\partial L}{\partial T} \approx
\frac{c_2}{\lambda T^2} \quad (x \gg 1) , \tag{17}$$

and the demo computes it by finite difference:

```text
 lambda (um)    dL/L per K radiance error for 1%   K error
         8.0      0.020168             49.584632    0.4958
        10.0      0.016197             61.740205    0.6174
        11.0      0.014782             67.650355    0.6765
        12.0      0.013620             73.421750    0.7342
        14.0      0.011835             84.492853    0.8449
```

A 1 per cent radiance error is a temperature error of 0.5 K at 8 µm and 0.84 K
at 14 µm. That is why operational land surface temperature products quote
accuracies of order 1 K and not 0.01 K: the radiometric calibration is that
good, and the rest is emissivity and atmospheric correction. At a wavelength of
11 µm one part in 14 800 in radiance is one kelvin.

## 6. Planetary energy balance and the grey atmosphere

### 6.1 Effective radiating temperature

A planet intercepting irradiance $S$ with albedo $a$ absorbs a flux averaged over
its surface of $S(1-a)/4$ (the factor 4 is the ratio of surface area to
cross-section) and radiates $\sigma T_e^4$:

$$T_e = \left(\frac{S(1-a)}{4\sigma}\right)^{1/4} . \tag{18}$$

```text
      a    F (W/m2)    Te (K)    Ts = 2^0.25 Te (K)
   0.20    272.2000   263.220               313.023
   0.25    255.1875   259.007               308.013
   0.30    238.1750   254.578               302.746
   0.35    221.1625   249.905               297.189
   0.40    204.1500   244.954               291.301
```

The sensitivity follows from (18):

$$\frac{\mathrm dT_e}{\mathrm dS} = \frac{T_e}{4S} = 0.0468\
\mathrm{K\ per\ W\,m^{-2}} , \tag{19}$$

so a 1 per cent change in $S$ moves $T_e$ by 0.64 K. For scale: the geothermal
flux of about 87 mW m⁻² is $3.7\times10^{-4}$ of the absorbed solar flux. The
Earth's internal heat engine is irrelevant to surface climate and decisive for
tectonics, and (18) is the number that disposes of any confusion between them.

### 6.2 The Sun's effective temperature, and a check on the solar constant

The Sun's solid angle from Earth and its mean radiance are
$\Omega = \pi R_\odot^2/d^2$ and $L = S/\Omega$; since a Lambertian emitter
radiates $F = \pi L$ and $F = \sigma T^4$,

$$T_{\text{eff}} = \left(\frac{\pi S}{\Omega\sigma}\right)^{1/4}
= \left(\frac{\pi S d^2}{\pi R_\odot^2\sigma}\right)^{1/4} . \tag{20}$$

The demo computes, with $S = 1361$ W m⁻² (adopted nominal),
$d = 1$ au $= 1.495\,978\,707\times10^{11}$ m (defined by the IAU) and
$R_\odot = 6.957\times10^8$ m (IAU nominal):

```text
  solid angle of the Sun from Earth = pi R^2/d^2 = 6.794274e-05 sr
  mean solar radiance L = S/omega = 2.0032e+07 W m^-2 sr^-1
  A Lambertian emitter radiates L = F/pi, so the surface flux is
  pi L = 6.2931e+07 W m^-2, and with F = sigma T^4:
  T_eff = (pi S/(omega sigma))^(1/4) = 5771.827 K
```

The adopted irradiance returns 5771.8 K, in agreement with the IAU nominal solar
effective temperature of 5772 K at the 0.1 K level. Older texts using 1367 W m⁻²
return 5778.2 K instead: a 0.44 per cent difference in $S$ is a 0.11 per cent
difference in $T$, because the fourth root divides it by four. This is a useful
discipline — $T_{\text{eff}}$ is robust and $S$ is the number you must state,
with its provenance.

### 6.3 Why a grey single-layer atmosphere overshoots

A single layer that transmits all sunlight and absorbs all infrared emits
$\sigma T_a^4$ upward and downward, so the surface must radiate
$2\sigma T_a^4$ and, in balance, $T_s = 2^{1/4}T_e$. The demo computes
$T_s = 302.75$ K for $a = 0.30$ — **hotter than the observed 288 K** (nominal).
A *grey* atmosphere with unit infrared emissivity over-shoots because the real
atmosphere is not opaque at every infrared wavelength: the 8–14 µm window lets
36.6 per cent of the emitted flux escape directly from the surface (§4). The
greenhouse effect is a spectral statement; a grey model is a first estimate,
misleading in the direction that matters. This is the same conclusion Kirchhoff's
law reached from the other side: a single grey emissivity cannot describe a
radiatively active atmosphere.

## 7. Physical interpretation

**Everything radiative is a product of a density of states and an occupation
number.** The $\lambda^{-5}$ in (3) is the density of electromagnetic modes; the
Bose–Einstein factor $(e^x-1)^{-1}$ is the occupation. That is why the peak
shifts with temperature and why the integral is a pure number times $T^4$: the
shape is universal and only the scale changes.

**Optical depth is the natural coordinate, not distance.** $\tau$ counts
absorptions, so a thin layer of a strong absorber can be optically thick while a
thick layer of a weak absorber is thin. Every retrieval statement — "the
atmosphere is opaque here" — is a statement about $\tau$, not about kilometres.

**Kirchhoff's law is the second law of thermodynamics in radiative form.** A body
cannot emit more at a wavelength than it absorbs there, or a cool body would
heat a warm one. The identity $\epsilon = 1-\rho$ is therefore not a
material property but a constraint, and it is why reflectance libraries can be
used to predict emissivity and vice versa.

**Brightness temperature is a calibrated lie.** It is the temperature a
blackbody would need; for a real surface it is a lower bound on the true kinetic
temperature whenever $\epsilon<1$, and it is the quantity that is actually
measured. Reporting $T_B$ as "the temperature" is the error; reporting $T_B$ and
stating the emissivity assumption is the measurement.

## 8. Assumptions and regime of validity

| Approximation | Statement | What breaks outside it |
|---|---|---|
| Local thermodynamic equilibrium | A single $T$ describes the emission at each point | Non-LTE emission (upper atmosphere, aurora, laser-pumped media); then $B(T)$ must be replaced by the actual source function |
| No scattering | Extinction is absorption only | Clouds, aerosols, snow, vegetation canopies: add a scattering source term, and the problem becomes integro-differential |
| Plane-parallel, horizontally uniform | Properties depend on height only | Limb viewing, spherical geometry, broken cloud, heterogeneous terrain |
| Blackbody / greybody | $\epsilon$ independent of wavelength | The greenhouse effect in full; mineral identification; any multi-band retrieval |
| Lambertian surface | Reflectance isotropic | Specular water, glint, BRDF effects; the Snell-window geometry of [02-10-01](./01-geometrical-optics.md) |
| Single layer | One isothermal slab | Real atmospheres: the solution is a vertical integral over $\tau$ with $B(T(z))$ |
| Steady state | Flux balance instantaneous | Diurnal cycle, volcanic eruptions, seasonal heat storage |
| Adopted $S$ and albedo | Nominal values | Real orbital and solar variability; the 0.1–0.3 per cent solar cycle |
| Inverse Planck for $T_B$ | Monochromatic radiance at one $\lambda$ | Broadband measurements: $T_B$ depends on the band, and the inversion is band-weighted, not monochromatic |

## 9. Units and dimensional analysis

- $B_\lambda$: $\mathrm{J\,s}\cdot\mathrm{m^2\,s^{-2}}/\mathrm{m^5}
  = \mathrm{W\,m^{-3}\,sr^{-1}}$ ✓, quoted per metre of wavelength or, in
  practice, per micrometre — the demo prints per µm, a factor $10^{-6}$ from SI.
- $B_\nu$: $\mathrm{W\,m^{-2}\,sr^{-1}\,Hz^{-1}}$. The ratio
  $B_\lambda(\lambda^2/c)/B_\nu$ is dimensionless and equals 1 ✓ (the demo's
  ratio column).
- $x = c_2/(\lambda T)$: $\mathrm{m\,K}/(\mathrm{m}\cdot\mathrm{K})$ ✓
  dimensionless, as required for an exponential.
- $\sigma T^4$: $\mathrm{W\,m^{-2}\,K^{-4}}\cdot\mathrm{K^4} =
  \mathrm{W\,m^{-2}}$ ✓. $4\sigma T^3$: $\mathrm{W\,m^{-2}\,K^{-1}}$, the same
  units as a convective coefficient — the basis of the comparison in
  [02-05-05](../05-thermodynamics/05-convection-radiation.md).
- $S(1-a)/4$: the factor 4 is the ratio of a sphere's surface area to its
  cross-section; omitting it makes the Earth 60 K too hot. Check: at 288 K the
  flux is 390 W m⁻² and at 320 K it is 594 W m⁻², so a 4-fold omission is not a
  small error.
- Optical depth is dimensionless by construction: $\tau =
  \int\kappa_\rho\rho\,\mathrm dz$ has units
  $\mathrm{m^2\,kg^{-1}}\cdot\mathrm{kg\,m^{-3}}\cdot\mathrm{m} = 1$ ✓. A
  quantity called "optical depth" with units is a bug.
- $T_B = c_2/(\lambda\ln(\cdot))$: $\mathrm{m\,K}/\mathrm{m} = \mathrm{K}$ ✓,
  and the argument of the logarithm is dimensionless because both $c_1$ and
  $\lambda^5I$ are in W m².
- $\Omega$: $\pi R_\odot^2/d^2 = \mathrm{m^2/m^2}$ = sr ✓ (a solid angle in
  steradians is an area ratio).
- **Useful anchors:** $\sigma = 5.670\,374\,419\times10^{-8}$ (exact);
  $b = 2.8977\times10^{-3}$ m K; $c_2 = 1.4388\times10^{-2}$ m K;
  $T_e = 254.58$ K for $a = 0.30$ and $S = 1361$ W m⁻²; the 8–14 µm window
  carries 36.6 per cent of terrestrial emission at 288 K; 1 K is 1.5 per cent of
  radiance at 11 µm.

## 10. Python demonstration

[`code/radiative_transfer_demo.py`](./code/radiative_transfer_demo.py) computes
the Planck function in both variables, verifies the Stefan–Boltzmann and Wien
laws numerically, computes band fractions, solar photometry, the radiative
transfer solution for a layer over a surface, brightness temperatures and
emissivity effects, and the single-layer greenhouse result. It uses the standard
library only. Every number quoted in this lesson is its actual output.

### What to observe

| Observation | Consequence |
|---|---|
| $\int x^3/(e^x-1)\,\mathrm dx$ converges to $\pi^4/15$ at $1.4\times10^{-13}$ | The Stefan–Boltzmann law is the Planck integral, verified numerically |
| $\sigma$ from the numeric integral matches the exact value to $3\times10^{-11}$ | $\sigma$ is derived, and exact, not measured |
| Wien's constant from two independent methods: $6.4\times10^{-11}$ relative | The displacement law is the Planck maximum |
| $B_\lambda(\lambda^2/c)/B_\nu = 1.00000000$ for all pairs | The Jacobian conversion is not optional |
| 288 K surface: 390.1 W m⁻², peak 10.06 µm | The thermal infrared is where the Earth's climate physics lives |
| 8–14 µm carries 36.6 per cent at 288 K | The window is a quantitative, not a qualitative, statement |
| $T_B$ saturates from 289.68 K to 250.000 K as $\tau$ goes 0.01 → 30 | Optical depth of order one is the see-through/see-only transition |
| $\epsilon = 0.93$ assumed as 1: −5.394 K | Emissivity is a first-order error term, not a correction |
| 1 per cent radiance error $= 0.68$ K at 11 µm | Why thermal products quote ~1 K, not 0.01 K |
| $T_{\text{eff}} = 5771.8$ K from $S = 1361$ W m⁻² | The solar constant and the solar temperature are the same statement |
| Grey single layer gives $T_s = 302.75$ K $>$ 288 K | A grey atmosphere over-shoots; the spectrum is the physics |

> **Breaking exercise.** Before running anything, predict the brightness
> temperature at $\tau = 0.1$ for an observer at 14 µm instead of 10 µm, with the
> same surface and layer temperatures, and predict the effect on the emissivity
> table if the surface temperature were 320 K instead of 300 K. Then change the
> demo and check both. Explain the second answer in terms of (16).

## 11. Common mistakes

1. **Using degrees Celsius in $\sigma T^4$.** The law is in kelvin; using 15
   instead of 288 underestimates the flux by a factor of $3.9\times10^5$.
2. **Forgetting the factor 4 in $S(1-a)/4$.** It is the geometry of a sphere, not
   a convention. Omitting it puts $T_e$ near 320 K.
3. **Mixing $B_\lambda$ and $B_\nu$ without the Jacobian.** A blackbody's peak
   wavelength and peak frequency are not related by $\lambda\nu=c$; using $c/\nu$
   in place of $\lambda$ mixes two spectra with different shapes.
4. **Reporting a brightness temperature as a temperature.** $T_B$ equals the
   kinetic temperature only for $\epsilon = 1$ and $\tau = 0$; otherwise it is a
   radiance in disguise.
5. **Quoting an emissivity as a single number.** Emissivity varies with
   wavelength, mineralogy, grain size, roughness and moisture; give a range and
   a source.
6. **Assuming a grey atmosphere.** It over-shoots the greenhouse effect (302.75 K
   against an observed 288 K here) precisely because it removes the window.
7. **Getting the inverse Planck function wrong.** $\ln(1+c_1/(\lambda^5I))$, not
   $\ln(1/\cdot)$; check the inversion by round-tripping a known $T$.
8. **Treating optical depth as a length.** $\tau$ is dimensionless: a thin,
   dense layer can be optically thick and a thick, tenuous one optically thin.
9. **Confusing radiance and irradiance.** They differ by $\pi$ for a Lambertian
   surface and by a factor of order 4 for a planet's energy balance.
10. **Comparing the geothermal flux with the solar flux without computing the
    ratio.** It is $3.7\times10^{-4}$; the comparison is not close, and stating it
    numerically ends the argument.

## 12. Real-world applications

- **Sea and land surface temperature.** Every thermal retrieval is an inversion
  of the radiative transfer equation with an emissivity and an atmospheric
  correction; the split-window technique exploits differential absorption in two
  nearby bands to remove the atmosphere
  ([17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md)).
- **Volcano and geothermal monitoring.** Radiant flux from a lava surface
  follows $\sigma T^4$; at 1400 K the emission is 2.18 × 10⁵ W m⁻² and the
  measurement is a thermal infrared one
  ([02-05-05](../05-thermodynamics/05-convection-radiation.md)).
- **Planetary energy balance and climate.** $T_e = (S(1-a)/4\sigma)^{1/4}$ is the
  zero-dimensional climate model from which every energy-balance model grows
  ([16-02 Earth's Energy Balance](../../16-atmosphere-climate/02-radiation-and-energy-balance/04-earth-energy-balance.md)).
- **Mineral mapping in the thermal infrared.** Emissivity spectra carry
  vibrational features; the reststrahlen bands of silicates fall in the 8–12 µm
  window, which is why thermal infrared hyperspectral sensing is a compositional
  tool ([02-10-04](./04-spectroscopy.md)).
- **Instrument calibration.** Blackbody sources at a known temperature define the
  radiance scale of every thermal radiometer; the Planck function is the transfer
  standard.
- **Greenhouse-gas remote sensing.** Absorption bands in the thermal infrared
  (CO₂ near 15 µm, water vapour, ozone near 9.6 µm) are the basis of nadir
  sounders, and the retrieval is a radiative transfer inverse problem.

## 13. Further reading

- **Goody, R. M., & Yung, Y. L. *Atmospheric Radiation: Theoretical Basis*
  (2nd ed., Oxford University Press).** The radiative transfer equation, its
  formal solution, and the grey and non-grey atmosphere models. Level:
  graduate.
- **Liou, K. N. *An Introduction to Atmospheric Radiation* (2nd ed., Academic
  Press).** Absorption, scattering, and the retrieval framework used by
  satellite remote sensing. Level: graduate.
- **Chandrasekhar, S. *Radiative Transfer* (Dover).** The classical treatment,
  including scattering and the two-stream approximations. Level: doctoral.
- **Petty, G. W. *A First Course in Atmospheric Radiation* (2nd ed., Sundog
  Publishing).** A careful and readable introduction with worked numbers.
  Level: advanced.
- **Rees, W. G. *Physical Principles of Remote Sensing* (3rd ed., Cambridge
  University Press).** Radiance, the Planck function and the instrument
  calibration chain, written for Earth observation. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 14. Related lessons

- [02-10-02 Interference and Diffraction in Optical Instruments](./02-interference-diffraction-optics.md)
  — the instrument that measures these radiances.
- [02-10-04 Spectroscopy Principles for Remote Sensing](./04-spectroscopy.md)
  — what the wavelength dependence of emissivity and reflectance tells you.
- [02-05-05 Convection, Radiation and Combined Heat Transfer](../05-thermodynamics/05-convection-radiation.md)
  — the heat-transfer view of the same laws.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../07-electromagnetism/05-em-waves.md)
  — the field-theoretic view of radiation.
- [16-02 Radiation and Energy Balance](../../16-atmosphere-climate/02-radiation-and-energy-balance/README.md)
  — the climate system built on these four equations.
- [17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md)
  — the observing systems.

Exercises:
[`exercises/03-radiative-transfer-exercises.md`](./exercises/03-radiative-transfer-exercises.md)
and
[`exercises/03-radiative-transfer-solutions.md`](./exercises/03-radiative-transfer-solutions.md).

## Self-assessment checklist

- [ ] I can distinguish radiance, irradiance and intensity and convert between
      them with the correct solid angle. (§1)
- [ ] I can write the Planck function in both variables and convert between them
      with the Jacobian. (§2)
- [ ] I can derive $\sigma T^4$ from the Planck integral and verify it
      numerically. (§3.1)
- [ ] I can derive Wien's law and verify the constant numerically. (§3.2)
- [ ] I can compute the band-integrated fraction of a blackbody spectrum. (§4)
- [ ] I can derive the radiative transfer equation and solve it for a layer over
      a surface. (§5.1)
- [ ] I can state Kirchhoff's law and use it to convert reflectance to
      emissivity. (§5.2)
- [ ] I can compute a brightness temperature and quantify the emissivity
      assumption's error. (§5.3)
- [ ] I can compute a planetary effective temperature and its sensitivity to the
      absorbed flux. (§6.1)
- [ ] I can explain why a grey atmosphere over-shoots the greenhouse effect.
      (§6.3)
