---
id: 16-02-02
title: "Radiative Transfer in the Atmosphere"
level: graduate
prereqs: ["16-02-01", "16-01-01", "02-05-05"]
tags: [atmosphere, climate, radiative-transfer, optical-depth, schwarzschild, greenhouse, two-stream]
---

# Radiative Transfer in the Atmosphere

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** optical depth, transmittance and emissivity, and **derive** the
   Beer–Lambert law and its limits.
2. **Write** the Schwarzschild radiative-transfer equation in local thermodynamic
   equilibrium and **derive** its formal solution for the upward intensity leaving
   the top of the atmosphere.
3. **Solve** the single-grey-layer model exactly and **compute** the surface
   temperature as a function of layer emissivity.
4. **Derive** the $T_s = (N+1)^{1/4}T_e$ law for $N$ perfectly opaque layers, and
   **explain** precisely why it is an unphysical idealisation and for which
   question it is nonetheless the right abstraction.
5. **Discretise** a grey atmosphere into $N$ layers, **show** that the surface
   temperature converges as $N$ is increased at fixed total optical depth, and
   **quantify** the angular-closure error against the Eddington analytic result.
6. **Compute** the effective emission level and **explain** why increasing the
   infrared opacity raises it and therefore raises the surface temperature.
7. **Explain** with numbers why a broadband (grey) optical depth cannot reproduce
   both the outgoing spectrum and its sensitivity to a change in absorber.

## Prerequisites

- [01 Solar and Terrestrial Radiation, Blackbody Laws](01-solar-and-terrestrial-radiation.md) —
  the Planck function, radiance versus flux, Kirchhoff's law, $T_e$ and the Solar
  and terrestrial spectra.
- [16-01-01 Atmospheric Composition and Vertical Structure](../01-atmospheric-structure-and-thermodynamics/01-atmospheric-composition.md) —
  the atmospheric state and the scale height.
- [02-05-05 Convection, Radiation and Combined Heat Transfer](../../02-physics/05-thermodynamics/05-convection-radiation.md) —
  radiation as a heat-transfer mode, and the concept of an absorption coefficient.

The general transport equation is
[02-10-03 Radiative Transfer](../../02-physics/10-optics-and-photometry/03-radiative-transfer.md);
this lesson specialises it to a plane-parallel planetary atmosphere in local
thermodynamic equilibrium. The spectroscopic input — which molecules absorb at
which wavelengths, and how strongly — is *not* derived here and is
[02-10-04 Spectroscopy](../../02-physics/10-optics-and-photometry/04-spectroscopy.md):
this module uses only synthetic band shapes and says so at every point where a
spectrum appears.

> **All models and data in this module are SYNTHETIC.** Optical depths, layer
> temperatures, band positions and band strengths below are chosen inputs of a
> teaching model, printed by the demonstration. $\sigma$ and the solar constant are
> standard constants. **No measured absorption spectrum is used, and no atmospheric
> constituent is identified with any spectral feature.**

## 1. Intuition: the atmosphere is a filter, not a blanket

A blanket works by conduction. The atmosphere does not touch the Sun, so the
greenhouse effect cannot be a blanket: it is a **filter with a bias**. The
atmosphere is comparatively transparent to the shortwave radiation arriving from a
$5772\ \mathrm{K}$ source and comparatively opaque to the longwave radiation
leaving a $\sim255$–$288\ \mathrm{K}$ surface. Because by Kirchhoff's law an
absorber is also an emitter, the opaque layers do not merely block the outgoing
radiation — they replace it with their own emission at *their* temperature.

That single sentence contains the whole physics, and everything else in this lesson
is the bookkeeping. Three consequences follow, and each is quantified below.

- **The outgoing flux is set by the temperature at optical depth about one.**
  Radiation escaping to space last interacted with the atmosphere where
  $\tau \approx 1$. If that level is at $5.1\ \mathrm{km}$ (the demonstration's
  value for a $288\ \mathrm{K}$ surface with a $6.5\ \mathrm{K\,km^{-1}}$ lapse
  rate), then that level is at $288 - 6.5 \times 5.1 = 255\ \mathrm{K}$ — the
  effective radiating temperature. The surface must be warmer than the level that
  radiates, and the difference is the greenhouse effect. **The surface is not in
  radiative balance with space; the level at $\tau \approx 1$ is.**
- **More absorber means a higher emission level means a warmer surface.** Raise
  the opacity and the $\tau \approx 1$ level moves up into colder air, so the
  planet radiates less for the same surface temperature; equilibrium then demands a
  higher surface temperature. In the grey models below the relation is smooth and
  monotone: with a total infrared optical depth of $0.5$ the surface is at
  $269.2\ \mathrm{K}$, at $\tau = 2$ it is at $302.7\ \mathrm{K}$, and at
  $\tau = 8$ at $380.7\ \mathrm{K}$ (no convection, no feedbacks).
- **Spectral structure is not a detail.** Two models with the *same* broadband
  emissivity of $0.80$ — one grey, one with a synthetic absorption window — give
  outgoing longwave fluxes of $221.5$ and $226.7\ \mathrm{W\,m^{-2}}$, and they
  respond to the same fractional increase in absorber by factors differing by
  $2.4$. A single optical depth cannot represent two different functions of
  wavelength, and the sensitivity is the second function.

## 2. Precise definitions

### 2.1 Optical depth, transmittance, emissivity

For a path through a medium with absorption coefficient $\kappa_\nu$ and density
$\rho$,

$$\tau_\nu = \int \kappa_\nu\,\rho\,\mathrm{d}s,
\qquad T_\nu = e^{-\tau_\nu}
\qquad\text{(transmittance)},$$

$$\varepsilon_\nu = 1 - e^{-\tau_\nu}
\qquad\text{(emissivity, for a homogeneous layer)}.$$

By Kirchhoff's law, $\varepsilon_\nu = a_\nu$ at the same wavelength: a layer that
absorbs $\varepsilon$ also emits $\varepsilon$. This is not an additional
assumption; it is a consequence of local thermodynamic equilibrium.

### 2.2 The optical-depth scale and the emission level

$\tau = 1$ defines the **visible depth**: $\varepsilon = 1-e^{-1} = 0.632$. A
medium with $\tau \gg 1$ is opaque — radiation cannot cross it — but it still emits
at its own temperature, and that emission is what a satellite sees.

The **effective emission level** (or emission height) $z_e$ is the height at which
$\tau \approx 1$ measured from the top, i.e. the centroid of the region from which
escaping radiation originates.

### 2.3 The source function and local thermodynamic equilibrium

For an atmosphere in **local thermodynamic equilibrium (LTE)** the source function
equals the Planck function at the local temperature:

$$S_\nu = B_\nu(T(z)).$$

LTE holds when collisions dominate over radiative transitions — true in the
troposphere and stratosphere, and false high enough that level populations are set
by radiation alone. Everything in this lesson assumes LTE.

### 2.4 The weighing function

The contribution of a level at optical depth $\tau$ to the radiation escaping from
the top is weighted by

$$w(\tau) = \frac{\partial}{\partial\tau}\left(e^{-\tau}\right) = e^{-\tau},$$

so the emission is spread over $\tau \sim 1$ rather than coming from a sharp
surface. This is why $z_e$ is a centroid, not a boundary.

## 3. Derivations

### 3.1 Beer–Lambert and its limits

For a direct beam in a purely absorbing (non-emitting) medium, energy conservation
along a path gives

$$\frac{\mathrm{d}I_\nu}{\mathrm{d}s} = -\kappa_\nu\rho I_\nu
\;\Longrightarrow\;
I_\nu(s) = I_\nu(0)e^{-\tau_\nu}, \qquad \tau_\nu = \int_0^s\kappa_\nu\rho\,\mathrm{d}s'.$$

The demonstration tabulates it: $\tau = 0.1$ transmits $0.904837$, $\tau = 1$
transmits $0.367879$, $\tau = 5$ transmits $0.006738$. **Beer–Lambert is not the
whole story in a planetary atmosphere**, because the absorbing medium also emits,
and ignoring that omission is the commonest conceptual error in this subject. The
next subsection supplies the missing term.

### 3.2 The Schwarzschild equation and its formal solution

Adding emission, and using $\mathrm{d}\tau = -\kappa\rho\,\mathrm{d}s$ with $\tau$
measured downward from the top:

$$\boxed{\;\frac{\mathrm{d}I_\nu}{\mathrm{d}\tau} = I_\nu - B_\nu(T)\;}$$

With $\mu = \cos\theta$ the direction cosine and $\mathrm{d}\tau/\mu$ the slant
path, the standard form is
$\mu\,\mathrm{d}I/\mathrm{d}\tau = I - B$. The **formal solution** for the upward
intensity at the top of the atmosphere, from a surface of temperature $T_s$ at
optical depth $\tau_s$:

$$I_\nu^\uparrow(0) = B_\nu(T_s)\,e^{-\tau_s}
+ \int_0^{\tau_s} B_\nu\!\left(T(\tau')\right)e^{-\tau'}\,\mathrm{d}\tau',$$

which is the statement that the escaping radiation is the surface Planck function
attenuated by the full atmosphere, plus the atmosphere's own emission from each
level attenuated by the atmosphere *above* that level. The weighting function
$e^{-\tau'}$ in §2.4 is the integrand's kernel.

**Two limits worth naming.**

- **Transparent atmosphere** ($\tau_s \to 0$): $I_\nu^\uparrow(0) \to B_\nu(T_s)$;
  the surface is seen directly.
- **Opaque atmosphere** ($\tau_s \to \infty$): the first term vanishes and the
  integral is dominated by $\tau' \approx 1$, so the escaping intensity is
  $B_\nu(T(z_e))$ with $z_e$ the level where $\tau = 1$. This is the emission-level
  picture of §1, and it is the origin of the greenhouse effect: the planet radiates
  at the temperature of the atmosphere near $\tau = 1$, not at the surface
  temperature.

### 3.3 The single grey layer: an exact solution

Take a black surface at $T_s$ and one isothermal grey layer at $T_a$ with
emissivity $\varepsilon$ (transmittance $1-\varepsilon$). Two balances:

$$\text{TOA:}\quad (1-\varepsilon)\sigma T_s^4 + \varepsilon\sigma T_a^4 = F,
\qquad
\text{surface:}\quad \sigma T_s^4 = F + \varepsilon\sigma T_a^4,$$

where $F = S(1-a)/4$ is the absorbed solar flux. Eliminating $T_a$:

$$\sigma T_s^4 = F + \varepsilon\sigma T_a^4 = F + \varepsilon\left(
\frac{F - (1-\varepsilon)\sigma T_s^4}{\varepsilon}\right)
= 2F - (1-\varepsilon)\sigma T_s^4,$$

$$\boxed{\;\sigma T_s^4 = \frac{2F}{2-\varepsilon}
\qquad\Longrightarrow\qquad
T_s = \left(\frac{2F}{\sigma(2-\varepsilon)}\right)^{1/4}\;}$$

Three checks:

- $\varepsilon = 0$: $T_s^4 = F/\sigma$, so $T_s = T_e$ — no atmosphere, no
  greenhouse effect.
- $\varepsilon = 1$: $T_s^4 = 2F/\sigma$, so $T_s = 2^{1/4}T_e = 302.75\
  \mathrm{K}$ for $T_e = 254.58\ \mathrm{K}$ — an increment of $48.17\ \mathrm{K}$.
- The layer temperature is $T_a^4 = (F/\sigma - (1-\varepsilon)T_s^4)/\varepsilon$,
  which comes out *below* $T_e$ at every $\varepsilon$: the layer radiates to space
  from a colder place than the planet's mean, which is exactly the emission-level
  picture.

| $\varepsilon$ | $T_s$ (K) | $T_a$ (K) | $T_s - T_e$ (K) |
|---|---|---|---|
| 0.00 | 254.578 | — | 0.000 |
| 0.25 | 263.220 | 221.34 | 8.642 |
| 0.50 | 273.562 | 230.04 | 18.984 |
| 0.75 | 286.320 | 240.77 | 31.741 |
| 0.90 | 295.618 | 248.58 | 41.040 |
| 0.99 | 301.994 | 253.95 | 47.416 |
| 1.00 | 302.746 | 254.58 | 48.168 |

**Read the last two rows together.** Going from $\varepsilon = 0.90$ to
$\varepsilon = 1.00$ — a $10\%$ increase in emissivity — raises the surface by only
$7.1\ \mathrm{K}$, whereas going from $0$ to $0.10$ raises it by $3.3\ \mathrm{K}$
and from $0$ to $0.50$ by $19.0\ \mathrm{K}$. The response **saturates**: once the
layer is nearly opaque, making it blacker changes little, because the emission
level has already reached the top of the layer. Any statement that "more
greenhouse gas always warms by the same amount" contradicts this algebra.

### 3.4 $N$ opaque layers, and the $(N+1)^{1/4}$ law

For $N$ perfectly opaque layers ($\varepsilon = 1$) each in radiative equilibrium,
the linear equilibrium system has the exact solution

$$\boxed{\;T_s = (N+1)^{1/4}\,T_e\;}$$

The demonstration solves the system numerically and reproduces it to
$10^{-4}\ \mathrm{K}$: $302.7461$, $335.0437$, $360.0279$, $398.4363$,
$463.6276$ and $600.7054\ \mathrm{K}$ for $N = 1, 2, 3, 5, 10, 30$.

**Why the law is exact** (one line): each black layer at its own temperature
requires $\sigma T_i^4 = (F_{in}^\uparrow + F_{in}^\downarrow)/2$, which with
$\varepsilon = 1$ forces $\sigma T_i^4$ to increase by one $T_e^4$ per layer
downward, and the surface to be one step further along — hence $N+1$ steps.

**Why it is unphysical, precisely.** Two separate reasons, and both matter:

1. **Infinite opacity.** Each layer is opaque at *every* wavelength, so the model
   has infinite total optical depth regardless of $N$. The continuum limit of
   "more and more layers" is not a large integer $N$ but an integral over
   $\mathrm{d}\tau$ — §3.5.
2. **Fixed-everything-else.** Increasing $N$ at fixed layer emissivity changes the
   total opacity, so it does not correspond to adding absorber to a fixed
   atmosphere. Adding absorber means increasing $\tau_s$, not $N$.

So the $(N+1)^{1/4}$ law is neither a model of the real greenhouse effect nor a
valid asymptotic limit. What it *is* is a clean demonstration of one idea: **the
surface temperature is not the planetary radiating temperature, and the offset
grows with the number of optically thick layers that separate them.** For that
purpose it is excellent, which is why it survives in textbooks.

### 3.5 A grey atmosphere discretised properly

Hold the **total** optical depth $\tau_s$ fixed and divide it into $N$ layers of
emissivity

$$\varepsilon_N = 1-e^{-\tau_s/N}.$$

Each layer is in radiative equilibrium; the surface is black and absorbs all of the
downward flux plus the absorbed solar flux. The unknowns are
$x_i = \sigma T_i^4$ and $x_s = \sigma T_s^4$, and the system is **linear** in
them, so it can be assembled and solved exactly (the demonstration does this rather
than iterating, whose convergence is unusably slow for the black-slab case). The
flux recurrences are

$$F^\uparrow_i = (1-\varepsilon)F^\uparrow_{i+1} + \varepsilon\sigma T_i^4,
\qquad
F^\downarrow_{i+1} = (1-\varepsilon)F^\downarrow_i + \varepsilon\sigma T_i^4,$$

which in the limit $\varepsilon \to 0$ with $\varepsilon N = \tau_s$ become the
two-stream equations $\mathrm{d}F^\uparrow/\mathrm{d}\tau = \sigma T^4 - F^\uparrow$
and $\mathrm{d}F^\downarrow/\mathrm{d}\tau = F^\downarrow - \sigma T^4$.

**The measured behaviour.** At fixed $\tau_s$ the surface temperature *converges*
as $N$ increases:

| $\tau_s$ | $N=1$ | $N=4$ | $N=40$ | $N=400$ | Eddington |
|---|---|---|---|---|---|
| 0.5 | 268.910 | 269.166 | 269.183 | 269.184 | 246.220 |
| 1.0 | 279.941 | 281.615 | 281.736 | 281.737 | 269.184 |
| 2.0 | 293.290 | 301.974 | 302.738 | 302.746 | 302.746 |
| 4.0 | 301.376 | 330.730 | 334.997 | 335.043 | 348.207 |
| 8.0 | 302.721 | 361.067 | 380.430 | 380.681 | 406.490 |

The Eddington column is the analytic two-stream radiative-equilibrium result

$$T_s = T_e\left(\frac{3\tau_s}{4} + \frac{1}{2}\right)^{1/4}$$

(the Eddington approximation gives $T^4 = \tfrac{3}{4}T_e^4(\tau + 2/3)$ with
$\tau$ measured downward from the top). The discrete model differs from it by
$+4.66\%$ at $\tau_s = 1$, $-3.78\%$ at $4$ and $-6.35\%$ at $8$ — **and the sign
changes with $\tau_s$.** That behaviour identifies the discrepancy not as a
discretisation error (which would shrink with $N$, and it does not) but as the
**angular-closure error**: this model carries a single vertical flux, while
Eddington's closure uses the first moment of the intensity. No single diffusivity
factor removes it, which is the honest reason two-stream schemes are quoted as
accurate to a few per cent in temperature and no better.

**The physics that survives.** The surface temperature rises monotonically with
total infrared optical depth, by $14.6\ \mathrm{K}$ at $\tau_s = 0.5$,
$27.2\ \mathrm{K}$ at $1$, $48.2\ \mathrm{K}$ at $2$, $80.5\ \mathrm{K}$ at $4$ and
$126.1\ \mathrm{K}$ at $8$ (all relative to $T_e = 254.58\ \mathrm{K}$). The
relation is close to linear in $\tau_s$ for moderate values. **That is the
quantitative content of "the greenhouse effect depends on the amount of infrared
absorber"**, expressed without any claim about which gas or how much.

### 3.6 The emission level

Set $\tau(z) = 1$ and ask where that is. For an opacity that falls off with scale
height $H_\tau$, $\tau(z) = \tau_s e^{-z/H_\tau}$, so

$$z_e = H_\tau\ln \tau_s .$$

For the surface temperature, invert the lapse rate instead: the planet radiates at
$T_e$, the temperature equals $T_e$ at height

$$z_e = \frac{T_s - T_e}{\Gamma}.$$

For $T_e = 254.58\ \mathrm{K}$ and $\Gamma = 6.5\ \mathrm{K\,km^{-1}}$:

| $T_s$ (K) | $z_e$ (km) |
|---|---|
| 288.00 | 5.14 |
| 295.00 | 6.22 |
| 302.70 | 7.40 |

The two expressions must be consistent, and that consistency *is* the greenhouse
feedback loop: raising the absorber increases $\tau_s$, which raises $z_e$ (first
expression), which requires a warmer surface to keep $T(z_e) = T_e$ (second
expression). The loop closes only when the two give the same $z_e$. Convection and
water-vapour feedback modify each step, and that is where the physics of
[04-02](../04-climate-system-and-feedbacks/02-climate-feedbacks.md) begins.

### 3.7 Why a grey optical depth is not enough

The demonstration builds a synthetic single-layer model with one strong band
($13$–$17\ \mu\mathrm{m}$), one moderate band ($8$–$13\ \mu\mathrm{m}$), a window
below $8\ \mu\mathrm{m}$ and partial absorption above $17\ \mu\mathrm{m}$ — all
**arbitrary model choices**, not gas data. The spectral scale is then adjusted so
that the *flux-weighted broadband emissivity at the surface temperature* equals
$0.800$, exactly matching a grey model.

| model | outgoing longwave flux (W m⁻²) |
|---|---|
| grey, $\varepsilon = 0.800$ | 221.514 |
| spectral, matched broadband emissivity | 226.678 |

and under a uniform fractional increase of the absorber:

| increase factor | $\Delta$OLR grey (W m⁻²) | $\Delta$OLR spectral (W m⁻²) | ratio |
|---|---|---|---|
| 1.02 | $-1.2645$ | $-0.5253$ | 0.42 |
| 1.10 | $-5.9345$ | $-2.4636$ | 0.42 |
| 1.50 | $-22.0672$ | $-9.4337$ | 0.43 |

**So a grey model matched to the broadband emissivity gets both the outgoing flux
and the sensitivity to added absorber wrong** — the spectral model is $2.3$ times
*less* sensitive, because the window lets the surface radiate directly to space in
a band where adding absorber changes little, while the strong band is already
saturated where the surface is brightest. This is why operational radiative
transfer is done band by band (line-by-line or correlated-$k$ schemes). It also
means a "grey atmosphere" is a conceptual tool, not a quantitative one.

## 4. Physical interpretation

- **The atmosphere does not trap heat; it changes where the heat escapes from.**
  Energy conservation is exact: at equilibrium the outgoing longwave flux equals
  the absorbed solar flux whatever the opacity is. What opacity changes is the
  *temperature* at which the escaping radiation was emitted.
- **The surface energy budget is not the planetary budget.** The surface is warmed
  by absorbed sunlight *plus* downwelling infrared from the atmosphere; a surface
  at $288\ \mathrm{K}$ radiates $390\ \mathrm{W\,m^{-2}}$, far more than the
  $238\ \mathrm{W\,m^{-2}}$ the planet absorbs, and the difference is supplied by
  the atmosphere.
- **Saturation is algebra, not opinion.** The $\varepsilon \to 1$ limit of §3.3 and
  the flattening of the $\tau_s$ curve in §3.5 both show diminishing returns. The
  relevant question is never "does more absorber warm?" — it does, monotonically,
  in this model — but "how much, at the current opacity, in the current bands?".
- **The window is where the leverage is.** A band that is already opaque cannot
  contribute more to the greenhouse effect; the marginal greenhouse effect of an
  absorber lives in the parts of the spectrum where $\tau \sim 1$.
- **Clouds are not a grey layer.** They are approximately black in the infrared
  (an optically thick cloud has $\varepsilon \approx 1$) but they *also* reflect
  sunlight, so they change $F$ and the outgoing longwave simultaneously, in
  opposite directions. That competition is the subject of
  [06](06-aerosols-and-clouds-radiation.md).

## 5. Worked numerical examples

**Example 1 — from optical depth to transmittance and emissivity.**

| $\tau$ | $T = e^{-\tau}$ | $\varepsilon = 1-e^{-\tau}$ |
|---|---|---|
| 0.01 | 0.990050 | 0.009950 |
| 0.10 | 0.904837 | 0.095163 |
| 1.00 | 0.367879 | 0.632121 |
| 5.00 | 0.006738 | 0.993262 |
| 10.00 | 0.000045 | 0.999955 |

At $\tau = 10$ the layer transmits $4.5\times10^{-5}$ of the surface radiance and
replaces it, in full, with its own emission at its own temperature. **Nothing is
"trapped"; the radiation is exchanged.**

**Example 2 — the single-layer greenhouse increment.**

With $F = S(1-a)/4 = 238.17\ \mathrm{W\,m^{-2}}$ and
$T_e = (F/\sigma)^{1/4} = 254.58\ \mathrm{K}$, the exact result
$\sigma T_s^4 = 2F/(2-\varepsilon)$ gives:

$$\varepsilon = 0.5:\quad T_s = \left(\frac{2\times238.17}
{5.670374419\times10^{-8}\times1.5}\right)^{1/4}
= \left(\frac{476.35}{8.505561629\times10^{-8}}\right)^{1/4}
= (5.6005\times10^{9})^{1/4} = 273.56\ \mathrm{K},$$

an increment of $18.98\ \mathrm{K}$ over $T_e$. For $\varepsilon = 1$:
$T_s = 2^{1/4}\times254.58 = 1.18921\times254.58 = 302.75\ \mathrm{K}$.

**Example 3 — the emission level and the loop.**

Take $T_s = 288\ \mathrm{K}$ and $\Gamma = 6.5\ \mathrm{K\,km^{-1}}$. The
temperature reaches $T_e = 254.58\ \mathrm{K}$ at

$$z_e = \frac{288.00 - 254.58}{6.5\times10^{-3}} = 5142\ \mathrm{m} = 5.14\
\mathrm{km}.$$

For the same atmosphere to have $\tau(z_e) = 1$ with an opacity scale height
$H_\tau$, we need $\tau_s = e^{z_e/H_\tau}$: with $H_\tau = 2\ \mathrm{km}$,
$\tau_s = e^{2.57} = 13.1$. With $H_\tau = 4\ \mathrm{km}$, $\tau_s = e^{1.29} =
3.6$. **The required total opacity is exponentially sensitive to the scale height
of the absorber** — which is why the vertical *distribution* of a greenhouse gas
matters, not only its column amount. (Both scale heights here are model choices;
the point is the exponential dependence.)

## 6. Assumptions and regime of validity

| Assumption | Where used | What breaks it |
|---|---|---|
| Local thermodynamic equilibrium | the source function $B_\nu(T)$ | Above roughly the mesopause, scattering and non-LTE emission (as in airglow) dominate; also in strong lines driven by solar pumping |
| Plane-parallel, horizontally uniform | the whole derivation | Breaks for low Sun angles and for broken cloud; the *spherical* geometry matters for the twilight and for limb sounding |
| Grey opacity | §§3.3–3.6 | Quantitatively wrong: §3.7 measures a factor $2.4$ error in sensitivity at matched broadband emissivity |
| Beer–Lambert transmittance | the layer recurrences | Ignores scattering; in the shortwave, scattering (by molecules and clouds) is first-order, and the two-stream must carry a reflection term |
| Single vertical flux (no diffusivity factor) | the discrete model | The closure error is measured at $+4.7\%$ to $-6.4\%$ in temperature (§3.5); a diffusivity factor of $1.66$ is conventional but does not remove the discrepancy |
| Radiative equilibrium of each layer | §§3.4–3.5 | Real tropospheres are *convectively* adjusted, not in radiative equilibrium; the radiative-equilibrium profiles here reach $380.7\ \mathrm{K}$ at $\tau_s = 8$, which no real atmosphere attains because convection carries the heat |
| No dynamics, no latent heat, no clouds | everything | All of them change the temperature profile, and therefore change the emission level |

**The most important entry is the sixth.** The numbers in §3.5 are not predictions
of the Earth's surface temperature and should not be read as such: with
$\tau_s = 8$ the grey radiative-equilibrium surface is $380.7\ \mathrm{K}$
($107\ \mathrm{^\circ C}$), which the real Earth does not reach because convection
transports the energy upward and short-circuits the radiative gradient. Turning
this radiative model into something with a realistic surface temperature *requires*
adding convection, and that is precisely what a *radiative–convective*
equilibrium model does ([05 Energy Balance Models](05-energy-balance-models.md)).

**Climate-claim discipline.** The chain in this lesson is:

1. **Exact**: the Schwarzschild equation, its formal solution, Kirchhoff's law and
   the $\varepsilon \to 1$ single-layer result are algebra and thermodynamics.
2. **Approximate**: the discrete two-stream solution and the Eddington relation
   differ by a few per cent, and *that difference is the honest uncertainty of the
   method*, not of the physics.
3. **Idealised past usefulness**: the $(N+1)^{1/4}$ law is an abstraction whose
   premise is unphysical.
4. **Model, not measurement**: every temperature quoted is the output of a
   zero-dimensional box model with a synthetic spectrum.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| Optical depth | $\tau_\nu$ | dimensionless | $\kappa$ (m² kg⁻¹) × $\rho$ (kg m⁻³) × length (m) ✔ |
| Transmittance, emissivity | $T_\nu, \varepsilon_\nu$ | dimensionless | both in $[0,1]$ |
| Absorption coefficient | $\kappa_\nu$ | m² kg⁻¹ | mass-specific; $\kappa\rho$ is m⁻¹ |
| Source function | $B_\nu$ | $\mathrm{W\,m^{-2}\,Hz^{-1}\,sr^{-1}}$ | same as $I_\nu$ |
| Flux | $F$ | $\mathrm{W\,m^{-2}}$ | |
| Scale height | $H_\tau$ | m | |
| Emission level | $z_e$ | m | $H_\tau\ln\tau_s$ ✔ |

The check worth doing: $\tau$ must be **dimensionless**, so any expression for it
must contain a length. An absorption coefficient quoted per mole or per molecule
must be converted to a mass-specific one (m² kg⁻¹) before it can enter a column
integral.

## 8. Python demonstration

[`code/radiative_transfer_demo.py`](code/radiative_transfer_demo.py) prints every
number quoted above. It:

1. tabulates Beer–Lambert transmittance and emissivity for seven optical depths;
2. solves the single-grey-layer **exact** relation for seven emissivities and
   tabulates $T_s$, $T_a$ and the greenhouse increment;
3. assembles and solves the linear equilibrium system for $N$ perfectly black
   layers and reproduces $(N+1)^{1/4}T_e$ to $10^{-4}\ \mathrm{K}$ for
   $N = 1, 2, 3, 5, 10, 30$;
4. solves the grey atmosphere with a fixed total optical depth at
   $N = 1, 4, 40, 400$ layers, shows convergence, and measures the angular-closure
   error against the Eddington analytic result;
5. tabulates the surface temperature against total optical depth;
6. computes the emission level for three surface temperatures and discusses the
   $H_\tau\ln\tau_s$ consistency;
7. builds a **synthetic** band/window spectrum, matches its broadband emissivity to
   a grey value, and measures the resulting difference in outgoing flux and in
   sensitivity to a uniform increase in absorber.

```bash
cd 16-atmosphere-climate/02-radiation-and-energy-balance/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python radiative_transfer_demo.py
```

## 9. Exercises

Graded problems with worked solutions:
[`exercises/02-radiative-transfer-atmosphere-exercises.md`](exercises/02-radiative-transfer-atmosphere-exercises.md)
and
[`exercises/02-radiative-transfer-atmosphere-solutions.md`](exercises/02-radiative-transfer-atmosphere-solutions.md).

## Mastery checkpoint

Without notes:

> A planet has absorbed solar flux $F = 200\ \mathrm{W\,m^{-2}}$ and a single
> grey layer of emissivity $\varepsilon = 0.6$ at temperature $T_a$ over a black
> surface at $T_s$. **(a)** Compute $T_e$, $T_s$ and $T_a$ from the two balance
> equations. **(b)** Verify that your $T_s$ satisfies the exact relation
> $\sigma T_s^4 = 2F/(2-\varepsilon)$. **(c)** Compute the height at which the
> temperature equals $T_e$ for a lapse rate of $6.0\ \mathrm{K\,km^{-1}}$, and
> state what total optical depth that implies if the absorber has a scale height
> of $3\ \mathrm{km}$. **(d)** State three ways in which the model you just used
> differs from a real atmosphere, and rank them by how much they change $T_s$.
> **(e)** If the layer's emissivity were raised to $0.9$, compute the fractional
> change in $T_s$ and compare it with the fractional change in $1-\varepsilon$.
> State in one sentence what that comparison shows.

## Common pitfalls

1. **Calling the greenhouse effect a "radiation trap".** The outgoing flux at
   equilibrium is unchanged; the *temperature at which it is emitted* changes.
2. **Forgetting emission.** Beer–Lambert alone (`§3.1`) applies to a non-emitting
   absorber. In a planetary atmosphere the emission term is the whole phenomenon.
3. **Reading the $380.7\ \mathrm{K}$ from §3.5 as a prediction.** It is a grey
   radiative-equilibrium result without convection.
4. **Treating the $(N+1)^{1/4}$ law as a limit.** Its premise — layers opaque at
   every wavelength — means infinite total opacity; the continuum limit is a
   different calculation.
5. **Assuming a higher emissivity always warms proportionally.** The response
   saturates: $0.90 \to 1.00$ in emissivity buys $7.1\ \mathrm{K}$, while
   $0 \to 0.50$ buys $19.0\ \mathrm{K}$.
6. **Calibrating a grey model to the broadband flux.** §3.7 shows this leaves both
   the outgoing spectrum and the sensitivity wrong by a factor of about $2.4$.
7. **Assuming the surface is in radiative balance with space.** It is not; the
   level at $\tau \approx 1$ is.
8. **Ignoring the vertical distribution of the absorber.** The required total
   opacity depends exponentially on the absorber's scale height.

## Related modules

- [01 Solar and Terrestrial Radiation, Blackbody Laws](01-solar-and-terrestrial-radiation.md) —
  the Planck function, Kirchhoff's law and $T_e$ used throughout.
- [03 The Greenhouse Effect: Physics, Not Rhetoric](03-greenhouse-effect.md) —
  this lesson's mechanism, examined for what it does and does not imply.
- [04 Earth Energy Balance and Global Mean Temperature](04-earth-energy-balance.md) —
  the observational budget this model has to reproduce.
- [05 Zero- and One-Dimensional Energy Balance Models](05-energy-balance-models.md) —
  where convection is added to the radiative model of §3.5.
- [06 Aerosols, Clouds and Their Radiative Effects](06-aerosols-and-clouds-radiation.md) —
  the scatterers this lesson deliberately left out.
- [16-01-03 Adiabatic Processes, Lapse Rates and Stability](../01-atmospheric-structure-and-thermodynamics/03-thermodynamic-processes.md) —
  where the lapse rate used in §3.6 comes from.
- [02-10-03 Radiative Transfer](../../02-physics/10-optics-and-photometry/03-radiative-transfer.md) —
  the general transport equation, including scattering.
- [17-01-03 Atmospheric Effects in Remote Sensing](../../17-remote-sensing-gis/01-remote-sensing-physics/03-atmospheric-effects.md) —
  the same equations applied to a signal passing through the atmosphere twice.
