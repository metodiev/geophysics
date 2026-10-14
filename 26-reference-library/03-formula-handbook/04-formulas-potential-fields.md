---
id: 26-03-04
title: "Formula Sheet: Gravity, Magnetics and Potential Theory"
level: advanced
prereqs: []
estimated_minutes: 35
tags: [reference, formulas, gravity, magnetics]
---

# Formula Sheet: Gravity, Magnetics and Potential Theory

Potential-theory identities, the gravity and magnetic anomaly formulas for the
standard source shapes, the reduction formulas, and the rules of thumb that get
abused most often. Every shape formula states the geometry it assumes.

## How to use this page

Potential-field formulas are cheap to evaluate and easy to misuse, because the
answer depends on assumptions about depth, density contrast, magnetisation
direction and the reference field. Each row states its geometry. The reduction
constants are given with the honest caveat that they depend on latitude and on
the chosen ellipsoid. Numbers quoted in the worked example come from
`code/formulas_potential_fields_demo.py`.

*Provenance:* no measured data. The worked example is **SYNTHETIC** — the buried
bodies are illustrative models chosen to make the arithmetic checkable.

## 1. Potential theory

| Quantity | Formula | Conditions |
|---|---|---|
| Gravitational potential | $V(\mathbf{r}) = -G\int \rho(\mathbf{r}')\,dV'/\lvert\mathbf{r}-\mathbf{r}'\rvert$ | sign convention: attractive |
| Gravitational field | $\mathbf{g} = -\nabla V$ | outside the source |
| Poisson's equation | $\nabla^{2}V = 4\pi G\rho$ | inside a source |
| Laplace's equation | $\nabla^{2}V = 0$ | source-free region |
| Magnetic scalar potential | $V_m$ with $\mathbf{B} = -\mu_0\nabla V_m$ | current-free region |
| Newton's law | $\mathbf{F} = G m_1 m_2\,\hat{\mathbf{r}}/r^{2}$ | point masses |
| Gauss's law for gravity | $\oint\mathbf{g}\cdot d\mathbf{S} = -4\pi G M_{\text{enc}}$ | the origin of the slab formula below |
| Source-geometry decay | point: potential $\propto 1/r$; line: $\propto \ln r$; sheet: $\propto r$ | controls how fast anomalies fall off with height |

## 2. Gravity of standard shapes

| Body | Vertical attraction $\Delta g_z$ | Notes |
|---|---|---|
| Infinite horizontal slab | $2\pi G\rho h$ | independent of depth; the Bouguer plate |
| Sphere, i.e. point mass at its centre | $G m z / \bigl[(x^{2}+z^{2})^{3/2}\bigr]$ | $z$ = depth to centre, $x$ = horizontal offset |
| Horizontal cylinder | $2\pi G\lambda z / (x^{2}+z^{2})$ | $\lambda$ = mass per unit length; strictly an infinite cylinder |
| Semi-infinite slab with a vertical face | $\pi G\rho h$ plus an arctangent term | the step model used for fault scarps |
| Sphere by half-width rule | $z = 1.305\,x_{1/2}$ | $x_{1/2}$ = offset at half the peak anomaly |
| Sphere, horizontal component | $G m x / \bigl[(x^{2}+z^{2})^{3/2}\bigr]$ | maximum at $x = z/\sqrt{2}$ |
| Sphere, vertical derivative | $G m\,(x^{2} - 2z^{2}) / \bigl[(x^{2}+z^{2})^{5/2}\bigr]$ | falls off as $1/r^{3}$ at the axis |

The half-width rule is the fastest depth estimate in gravity work and the one
most often applied outside its validity: it assumes an isolated sphere whose
dimensions are small compared with its depth.

## 3. Magnetic sources

| Body | Anomaly in SI units | Notes |
|---|---|---|
| Dipole, axial | $B_{\text{axial}} = (\mu_0/4\pi)\,(2m/r^{3})$ | $m$ = dipole moment in A·m² |
| Dipole, equatorial | $B_{\text{equatorial}} = (\mu_0/4\pi)\,(m/r^{3})$ | same dipole, transverse field line |
| Uniformly magnetised sphere | a dipole at its centre with $m = M\,(4/3)\pi a^{3}$ | $M$ = magnetisation in A/m |
| Vertical prism | closed form in arctangents and logarithms | the Bhattacharyya expression; basis of most forward codes |
| Thin sheet, magnetised vertically | derivative of the cylinder expression | used for dykes and contacts |
| Induced magnetisation | $\mathbf{M} = \chi\mathbf{H}$ | $\chi$ dimensionless in SI, larger by $4\pi$ in CGS |
| Koenigsberger ratio | $Q_K = M_r/M_i$ | if $Q_K \gtrsim 1$ remanence cannot be neglected |
| Reduction to the pole | phase rotation in the wavenumber domain | needs a known field direction; unstable at low latitude |

Wavenumber-domain operations have simple kernels:

| Operation | Multiplier in the 2-D Fourier domain |
|---|---|
| Upward continuation by $\Delta h$ | $e^{-k\Delta h}$ |
| Downward continuation by $\Delta h$ | $e^{+k\Delta h}$ — amplifies short-wavelength noise |
| Vertical derivative | $\lvert k\rvert$ |
| Horizontal derivative in $x$ | $i k_x$ |
| Reduction to the pole | $\lvert k\rvert^{2} / (\text{factors in } I,\ D)$ |

These kernels are the reason field data are almost always processed in the
wavenumber domain, and also the reason processing must be tapered: the
downward-continuation kernel grows without bound as $k \to \infty$.

## 4. Reductions and corrections

| Correction | Formula | Notes |
|---|---|---|
| Free-air | $\Delta g_{\text{FA}} = g_{\text{obs}} - g_{\text{normal}} + (2g/a)\,h$ | compute $2g/a$ from your ellipsoid |
| Bouguer plate | $\Delta g_B = \Delta g_{\text{FA}} - 2\pi G\rho h$ | $\rho$ is the reduction density and must be stated |
| Bouguer rule of thumb | $\Delta g_B\ [\text{mGal}] = 0.04193\,\rho\,[\text{g cm}^{-3}]\,h\,[\text{m}]$ | the same $2\pi G\rho h$ in practical units |
| Terrain correction | added, always positive | removes the excess mass of the topography above the slab |
| Tidal correction | from the tide-generating potential | tens of µGal in amplitude |
| Eötvös correction | from platform velocity and heading | essential in marine and airborne gravity |
| Normal gravity | Somigliana closed formula | defined, not measured, on the reference ellipsoid |

**A caution about the free-air constant.** Textbooks often quote
$0.3086$ mGal/m. That figure is the polar-radius approximation. Evaluating
$2g_n/a$ with the mean radius 6371 km gives 0.307853 mGal/m, and the exact
normal-gravity gradient varies with latitude between roughly 0.3067 and
0.3086 mGal/m. Compute it from the ellipsoid in use rather than quoting one
number.

## 5. Isostasy and flexure

| Model | Relation | Notes |
|---|---|---|
| Airy | $t = \rho_c h_{\text{elev}}/(\rho_m - \rho_c)$ | $t$ = root thickness |
| Pratt | $\rho h =$ constant | density varies laterally instead of thickness |
| Flexure | $D\nabla^{4}w + \Delta\rho\,g\,w = q$ | elastic plate under load $q$ |
| Flexural rigidity | $D = E T_e^{3}/[12(1-\nu^{2})]$ | N·m; $T_e$ = effective elastic thickness |

## Worked example (numbers from the verification script)

| Quantity | Value |
|---|---|
| Bouguer slab, $\rho = 2670$ kg/m³, $h = 100$ m | $1.119688\times10^{-4}$ m/s² = 11.1969 mGal |
| The same by rule of thumb, $\rho = 2.67$ g/cm³ | 11.1953 mGal |
| Free-air gradient, $a = 6371$ km (mean radius) | 0.307853 mGal/m |
| Free-air gradient, $a = 6356.752$ km (polar radius) | 0.308543 mGal/m |
| Buried sphere, $a = 500$ m, $\Delta\rho = 300$ kg/m³, depth 1000 m | $m = 1.570796\times10^{11}$ kg |
| Peak vertical anomaly at $x = 0$ | $+1.048397$ mGal |
| At $x = 1000$ m | $g_z = +0.370664$ mGal, $g_x = +0.370664$ mGal, $\lvert g\rvert = 0.524198$ mGal |
| Offset at half maximum | 766.4 m $= 0.766z$ |
| Inverse half-width rule | $z = 1.305 \times 766.4 = 1000.2$ m |
| Vertical derivative of the sphere anomaly at $x = 0$ | $-2.096793\times10^{-8}$ s⁻² $= -20.9679$ E |
| Upward continuation, 20 km wavelength, 2 km height | factor 0.533488; 50 nT becomes 26.6744 nT |
| Magnetic sphere, $M = 1$ A/m, $r = 1000$ m | $B_{\text{axial}} = 104.7198$ nT, $B_{\text{equatorial}} = 52.3599$ nT |
| Same at $r = 2000$ m | $B_{\text{axial}} = 13.0900$ nT, ratio 8.0000 as $1/r^{3}$ requires |

Two sanity checks are worth copying into your own code. At $x = z$ the vertical
and horizontal components of a sphere anomaly are equal, because the geometry is
symmetric there. And the inverse half-width rule recovers the model depth of
1000 m to within the rounding of the printout, which is exactly what it is for.

## Assumptions and regime of validity

- Every shape formula assumes a **homogeneous body with a constant contrast** in
  a uniform background. A variable density contrast or a gradient in the
  reference field invalidates the simple forms.
- The infinite-slab formula is exact only for an infinite plate, which is why
  terrain corrections exist for real surveys.
- Depth estimates from half-width rules are model-dependent: a different shape
  gives a different coefficient. They are starting models, not results.
- Wavenumber-domain filters assume a flat observation surface, uniform sampling
  and no edge effects; tapering and padding change the answer.
- Reduction to the pole at low magnetic latitude is unstable and requires
  explicit stabilisation.
- Gravity data constrain the product of density contrast and volume; magnetics
  constrain the product of magnetisation and volume. Neither determines shape,
  depth and contrast independently without additional assumptions.

## Verification script

[`code/formulas_potential_fields_demo.py`](./code/formulas_potential_fields_demo.py) —
print-only, seeded with `default_rng(20261014)`, under a second, exit 0. It
prints the slab, free-air, sphere, half-width, vertical-derivative, continuation
and dipole checks quoted above, and prints *both* free-air gradient values so
the textbook constant can be compared honestly.

## Related pages

- [Formula Sheet: Electromagnetics and Electrical Methods](./05-formulas-em-electrical.md)
- [Formula Sheet: Waves, Elasticity and Seismology](./03-formulas-waves-seismology.md)
- [Physical Constants and Earth Parameters with Sources](../02-symbols-and-units/03-constant-handbook.md)
- [07-gravity-geodesy folder overview](../../07-gravity-geodesy/README.md)
- [08-geomagnetism-electromagnetism folder overview](../../08-geomagnetism-electromagnetism/README.md)
