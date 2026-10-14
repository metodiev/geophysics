---
id: 16-02-06
title: "Aerosols, Clouds and Their Radiative Effects"
level: doctoral
prereqs: ["16-02-02", "16-02-03", "16-02-04", "16-01-04"]
tags: [atmosphere, climate, radiation, aerosols, clouds, scattering, radiative-forcing, remote-sensing]
---

# Aerosols, Clouds and Their Radiative Effects

> **All models and data in this module are SYNTHETIC.** Every number below is
> either an exact standard constant (stated with units), a stated convention, or
> an output of the demonstration in
> [`code/aerosols_and_clouds_radiation_demo.py`](code/aerosols_and_clouds_radiation_demo.py),
> which was run to produce it. The particle refractive indices, size
> distributions, cloud properties and scene parameters are **chosen inputs**, not
> measurements. No aerosol or cloud dataset, mission, station or published
> radiative-forcing value is quoted anywhere in this lesson.

## Learning objectives

1. **Derive** the extinction optical depth of a droplet layer from its liquid-water
   path and effective radius, and **quantify** the error of the geometric-optics
   approximation against an explicit Mie calculation.
2. **Explain** why three and only three parameters — optical depth $\tau$, single-
   scattering albedo $\omega_0$ and asymmetry parameter $g$ — summarise the
   single-scattering behaviour of a particle population.
3. **Derive** the two-stream (Eddington) diffuse equations from the moments of the
   radiative-transfer equation, and **state** the three exact identities that any
   correct solution must satisfy.
4. **Apply** delta-Eddington scaling and **quantify** how much of the two-stream
   error is phase-function truncation rather than arithmetic.
5. **Compute** the cloud radiative forcing as the difference between two model
   states, and **show** why its sign depends on cloud height and optical depth.
6. **Derive** the susceptibility of cloud albedo to droplet number
   ($\mathrm{d}A/\mathrm{d}\ln N_d$) and **analyse** the regime in which the
   asymptotic form $A(1-A)/3$ is reliable.
7. **Decide**, from a thin-layer criterion, whether an aerosol layer brightens or
   dims a scene, and **justify** why that sign is observable but the
   single-scattering albedo itself is not.
8. **Distinguish** systematically what is measured, what is modelled and what is
   inferred for each quantity in this lesson, and **demonstrate** with a synthetic
   retrieval why a saturated albedo carries little information.

## Prerequisites

- [02 Radiative Transfer in the Atmosphere](../02-radiation-and-energy-balance/02-radiative-transfer-atmosphere.md)
  — optical depth, transmittance, grey layers, emission level.
- [03 The Greenhouse Effect](../02-radiation-and-energy-balance/03-greenhouse-effect.md)
  — longwave opacity, emission level, Planck response.
- [04 Earth Energy Balance](../02-radiation-and-energy-balance/04-earth-energy-balance.md)
  — TOA budget, albedo, the two-box surface relation.
- [16-01-04 Moisture and Clouds](../01-atmospheric-structure-and-thermodynamics/04-moisture-and-clouds.md)
  — saturation, condensation, why clouds exist where they do.
- [02-10-03 Radiative Transfer](../../02-physics/10-optics-and-photometry/03-radiative-transfer.md)
  — absorption, emission and the radiative-transfer equation in a
  non-participating medium.

---

## 1. Intuition: the same physics at two size parameters

A cloud droplet and an aerosol particle are both small spheres of refractive index
$m$ in air. What separates them is the **size parameter**

$$x \equiv \frac{2\pi r}{\lambda}. \tag{1}$$

For a droplet of effective radius $r_e = 10\ \mu\mathrm{m}$ at
$\lambda = 0.55\ \mu\mathrm{m}$, $x = 114.2$; for a $0.1\ \mu\mathrm{m}$ aerosol
particle, $x = 1.14$. At $x \gg 1$ the interaction is essentially geometric — the
particle intercepts a shadow of twice its own cross-section and throws most of
that light forward into a narrow diffraction lobe — whereas at $x \sim 1$ the
interaction is resonant and the particle can absorb a large fraction of what it
intercepts.

Two consequences drive everything here. First, **a cloud is a nearly perfect
scatterer in the visible and a nearly perfect absorber in the thermal infrared**:
the demonstration computes $\omega_0 = 0.9999983$ at $0.55\ \mu\mathrm{m}$ and an
absorption optical depth of $49.94\ \mathrm{m^2\,kg^{-1}}$ at $11\ \mu\mathrm{m}$
for the same synthetic population with $r_e = 10\ \mu\mathrm{m}$. Second, **a bright
surface is hard to brighten and easy to darken**: a scattering layer adds reflected
light in proportion to how *dark* the scene beneath it is, while an absorbing layer
removes light in proportion to how *bright* that scene is. That competition is the
whole physics of the aerosol direct effect, and it is a sign argument, not a
magnitude argument.

## 2. Precise definitions

**Extinction optical depth.** For a population with number concentration $N(r)$,

$$\tau = \int_0^z \int_0^\infty N(r)\,\sigma_{\text{ext}}(r)\,\mathrm{d}r\,\mathrm{d}z',
\qquad
\sigma_{\text{ext}} = Q_{\text{ext}}\,\pi r^2 . \tag{2}$$

$Q_{\text{ext}}$ is the extinction efficiency: the ratio of the energy removed from
the beam to the energy geometrically incident on the particle.

**Single-scattering albedo.**

$$\omega_0 = \frac{\sigma_{\text{sca}}}{\sigma_{\text{ext}}} \in [0,1]. \tag{3}$$

$\omega_0 = 1$ means the particle scatters everything it intercepts; $\omega_0 = 0$
means it absorbs everything.

**Asymmetry parameter.**

$$g = \frac{1}{4\pi}\oint p(\cos\Theta)\cos\Theta\,\mathrm{d}\Omega , \tag{4}$$

the mean cosine of the scattering angle, with $g > 0$ forward-peaked,
$g = 0$ isotropic and $g < 0$ backward-peaked.

**Liquid-water path and effective radius.**

$$\text{LWP} = \int_0^z \rho_w \int_0^\infty \frac{4}{3}\pi r^3 N(r)\,\mathrm{d}r\,\mathrm{d}z',
\qquad r_e = \frac{\langle r^3\rangle}{\langle r^2\rangle}. \tag{5}$$

**Cloud radiative forcing.** For any quantity $F$,

$$\text{CF}_{\text{SW}} = F_{\text{SW}}^{\text{clear}} - F_{\text{SW}}^{\text{cloudy}},
\qquad
\text{CF}_{\text{LW}} = F_{\text{LW}}^{\text{clear}} - F_{\text{LW}}^{\text{cloudy}},
\tag{6}$$

so a cloud that reflects more solar radiation has a **negative** shortwave forcing
and a cloud that reduces the outgoing longwave radiation has a **positive**
longwave forcing. The net is their sum, and its sign is the question.

**Retrieval versus measurement.** A *measured* quantity is one a detector reports;
a *retrieved* quantity is inferred from measurements through a model; a *modelled*
quantity is computed from other modelled quantities. §3.7 keeps these apart.

## 3. Derivations

### 3.1 From water path to optical depth, and the geometric limit

Assume a narrow size distribution so that $\sigma_{\text{ext}} \approx Q_{\text{ext}}
\pi r_e^2$ and, in the geometric limit, $Q_{\text{ext}} = 2$ exactly. Then

$$\tau = \int N \pi r_e^2 Q_{\text{ext}}\,\mathrm{d}z
= \frac{Q_{\text{ext}}\pi r_e^2}{(4/3)\pi r_e^3 \rho_w}\,\text{LWP}
= \frac{3\,\text{LWP}}{2\rho_w r_e}. \tag{7}$$

Three properties of (7) deserve emphasis. It is **dimensionally** a mass extinction
coefficient: $3/(2\rho_w r_e) = 150\ \mathrm{m^2\,kg^{-1}}$ at $r_e = 10\ \mu$m, so
a liquid-water path of $100\ \mathrm{g\,m^{-2}} = 0.1\ \mathrm{kg\,m^{-2}}$ gives
$\tau = 15.0$. It is **inversely proportional to $r_e$**, which is why a change in
droplet number at fixed water path changes $\tau$. And it **hides the whole of the
optics in one assumption**, $Q_{\text{ext}} = 2$, which §3.7 of the demonstration
tests directly.

The demonstration integrates (2) over a gamma distribution with effective variance
$v_e = 0.10$ and $Q_{\text{ext}}$ from Mie theory. The result:

| $r_e$ ($\mu$m) | $Q_{\text{ext}}$ (integrated) | $\omega_0$ | $g$ | $\tau/\text{LWP}$ (m² kg⁻¹) | $3/(2\rho_w r_e)$ | ratio |
|---|---|---|---|---|---|---|
| 5 | 2.1731 | 0.9999991 | 0.8419 | 321.62 | 300.00 | 1.0721 |
| 10 | 2.1044 | 0.9999983 | 0.8619 | 156.76 | 150.00 | 1.0451 |
| 15 | 2.0869 | 0.9999976 | 0.8648 | 103.68 | 100.00 | 1.0368 |
| 20 | 2.0630 | 0.9999968 | 0.8720 | 77.04 | 75.00 | 1.0272 |

The integrated $Q_{\text{ext}}$ sits a few per cent **above** 2 at these sizes
because the Mie efficiency oscillates around the geometric value with an
amplitude of order $x^{-2/3}$; the ratio falls from 1.072 to 1.027 as $r_e$ grows
from 5 to $20\ \mu$m, which *is* the statement that geometric optics is being
approached. Averaged over size parameters $x \in [60,260]$ the demonstration finds
$\langle Q_{\text{ext}}\rangle = 2.0716$ with a spread about that mean of 0.05 —
the extinction paradox, recovered as a statistical statement about the ripple.

### 3.2 The two-stream equations from moments of the transfer equation

Write the azimuthally averaged radiative-transfer equation for the diffuse
intensity $I(\mu,\tau)$, with $\mu$ the cosine of the zenith angle (positive
upward), a collimated beam of irradiance $F_0$ entering the top along direction
cosine $-\mu_0$, and a synthetic phase function $p_0$:

$$\mu\frac{\partial I}{\partial\tau} = I
- \frac{\omega_0}{2}\int_{-1}^{1}p_0(\mu,\mu')I(\mu')\,\mathrm{d}\mu'
- \frac{\omega_0}{2}p_0(\mu,-\mu_0)F_0e^{-\tau/\mu_0}. \tag{8}$$

Define the flux sum and flux difference of the diffuse field,

$$S = F_\uparrow + F_\downarrow, \qquad D = F_\uparrow - F_\downarrow. \tag{9}$$

**Zeroth moment** ($\int_{-1}^{1}\mathrm{d}\mu$). The left side gives
$\mathrm{d}(4\pi H)/\mathrm{d}\tau$ with $H = \frac12\int\mu I\,\mathrm{d}\mu$; under
the Eddington closure $I = I_0 + \mu I_1$ one has $H = I_1/3$ and $S = 2\pi I_0$,
$D = 4\pi I_1/3$. The scattering integral on the right reduces to $2\omega_0I_0$ if
the phase function has unit normalisation, and the beam contributes
$\omega_0F_0e^{-\tau/\mu_0}$. Hence

$$\frac{\mathrm{d}D}{\mathrm{d}\tau} = 2(1-\omega_0)\,S - \omega_0F_0e^{-\tau/\mu_0}.
\tag{10}$$

**First moment** ($\int_{-1}^{1}\mu\,\mathrm{d}\mu$). The left side gives
$\mathrm{d}(2K)/\mathrm{d}\tau$ with $K = I_0/3$; the diffuse scattering contributes
$2\omega_0gI_1/3$; the beam, scattering from a *downward* direction into an upward
one, contributes $-\omega_0g\mu_0F_0e^{-\tau/\mu_0}$ because
$p_0(\mu,-\mu_0) = 1-3g\mu\mu_0$ to first order in the Legendre expansion. Hence

$$\frac{\mathrm{d}S}{\mathrm{d}\tau} = \tfrac{3}{2}(1-\omega_0g)\,D
+ \tfrac{3}{2}\omega_0g\mu_0F_0e^{-\tau/\mu_0}. \tag{11}$$

**The sign in (11) is the most error-prone step here.** Enter the beam's direction
with the wrong sign and the beam coefficient comes out negative, after which the
model claims that a strongly forward-scattering layer reflects $1.8$ times more
than it can; the demonstration makes that detectable by two independent routes.

With the abbreviations

$$a = \tfrac{3}{2}(1-\omega_0g),\quad c = 2(1-\omega_0),\quad
p = \tfrac{3}{2}\omega_0g\mu_0F_0,\quad q = \omega_0F_0 , \tag{12}$$

equations (10)–(11) are a closed $2\times2$ linear system in $(S,D)$ with boundary
conditions

$$D(0) = S(0) \quad\text{(no diffuse radiation entering the top)}, \tag{13}$$
$$F_\uparrow(\tau_{\text{tot}}) = \alpha_s\bigl[F_\downarrow(\tau_{\text{tot}})
+ \mu_0F_0e^{-\tau_{\text{tot}}/\mu_0}\bigr] \quad\text{(Lambertian surface)},
\tag{14}$$

which in terms of $(S,D)$ reads $D(\tau_{\text{tot}}) = rS(\tau_{\text{tot}}) + \beta$
with $r = (\alpha_s-1)/(\alpha_s+1)$ and $\beta = 2\alpha_s\mu_0F_0
e^{-\tau_{\text{tot}}/\mu_0}/(1+\alpha_s)$.

**Three exact identities.** Because the surface reflects as well as the layer, the
two boundary conditions plus (10) fix the reflected and transmitted fractions
without any reference to (11):

1. If $\omega_0 = 1$ then the medium absorbs nothing, so $R + T = 1$ for a black
   surface, where $T$ includes the residual direct beam.
2. If in addition $\alpha_s = 1$, nothing may leave through the bottom, so the
   system albedo is exactly $1$: $R = 1$.
3. If $\omega_0 = 0$ there is no diffuse source at all, so $R = 0$ and
   $T = e^{-\tau_{\text{tot}}/\mu_0}$ exactly (Beer–Lambert).

The demonstration checks all three for both closures and finds residues of order
$10^{-16}$; the largest of the printed values is $1.11\times10^{-16}$ and the
$\omega_0 = 0$ transmittance matches $e^{-4/0.6} = 0.00127263$ to all printed
digits.

### 3.3 Phase-function truncation: the one real approximation

Equation (11) uses only $g$, i.e. only the **first** moment of the phase function.
The backscattered fraction of the beam implied by the Eddington form
$p_0 = 1 - 3g\mu\mu_0$ is

$$b_{\text{Edd}}(\mu_0) = \frac12\int_0^1 p_0(\mu,-\mu_0)\,\mathrm{d}\mu
= \frac{1 - \tfrac{3}{2}g\mu_0}{2} = 0.112 \quad (g = 0.8619,\ \mu_0 = 0.6), \tag{15}$$

whereas the true azimuth-averaged Henyey–Greenstein phase function with the same
$g$ gives $b = 0.061$. The Eddington closure therefore overestimates the
backscattered fraction by a factor $1.83$, and the demonstration measures exactly
that: the ratio of the plain two-stream reflectance to the exact single-scattering
value is $1.829$ at $\tau = 0.002$ and stays near $1.83$ down to the thinnest layer
tested.

**Delta-Eddington scaling** removes the forward diffraction peak before the
two-stream is applied:

$$\tau' = (1-\omega_0g^2)\tau,\qquad
\omega_0' = \frac{\omega_0(1-g^2)}{1-\omega_0g^2},\qquad
g' = \frac{g}{1+g}. \tag{16}$$

For $g = 0.8619$ the scaled asymmetry is $g' = 0.463$ and the scaled depth
$\tau' = 0.2571\tau$. The measured thin-layer ratio drops from $1.829$ to $1.224$,
and it *falls* with $\tau$ ($1.224 \to 1.191$ from $\tau = 0.002$ to $0.2$), as it
must, since multiple scattering is second order in $\tau$. **This is the honest
error budget of the whole lesson: tens of per cent on an albedo, produced by
truncating a phase function, not by arithmetic.**

### 3.4 Longwave opacity and cloud emissivity

At thermal wavelengths the same droplet population has
$Q_{\text{abs}} \approx Q_{\text{ext}}$ with $Q_{\text{sca}}$ small, so the
absorption optical depth follows from the same argument as (7) with
$Q_{\text{abs}}$ in place of $Q_{\text{ext}}$:

$$\tau_{\text{abs}} = \frac{3\,\text{LWP}}{4\rho_w r_e}\,Q_{\text{abs}},
\qquad \varepsilon = 1 - e^{-\tau_{\text{abs}}}. \tag{17}$$

The geometric factor is $3/(4\rho_wr_e) = 75\ \mathrm{m^2\,kg^{-1}}$ at
$r_e = 10\ \mu$m — **not** $150$, because only the absorption efficiency
contributes. For the synthetic index $m = 1.20 + 0.05i$ at $11\ \mu$m the Mie
calculation gives $49.94\ \mathrm{m^2\,kg^{-1}}$, i.e. $Q_{\text{abs}} = 0.666$:
the size parameter is only $5.7$, so the geometric limit is not reached and (17)
with $Q_{\text{abs}} = 1$ would overstate the opacity by 50%.

The resulting emissivities are the reason a modest cloud is black in the infrared:

| LWP (g m⁻²) | 5 | 10 | 25 | 50 | 100 | 200 |
|---|---|---|---|---|---|---|
| $\tau_{\text{abs}}$ | 0.250 | 0.499 | 1.249 | 2.497 | 4.994 | 9.989 |
| $\varepsilon$ | 0.2210 | 0.3931 | 0.7131 | 0.9177 | 0.9932 | 0.99995 |

### 3.5 Cloud radiative forcing and its sign

Consider a single overcast layer at height $z_c$, temperature
$T_c = T_s - \Gamma z_c$ with the stated convention $\Gamma = 6.5\ \mathrm{K\,km^{-1}}$,
scene insolation $\mu_0S$, and shortwave scene albedo $R$ from §3.2. Then

$$\text{CF}_{\text{SW}} = -\bigl(R - \alpha_{\text{clear}}\bigr)\mu_0S,
\qquad
\text{CF}_{\text{LW}} = \varepsilon\bigl(\sigma T_s^4 - \sigma T_c^4\bigr). \tag{18}$$

The shortwave term depends on the scene albedo *difference*; the longwave term on
the *emissivity* and on how much colder the cloud is than the surface. Both grow
with $\tau$, but the shortwave term saturates once $R$ does while the longwave term
saturates once $\varepsilon$ does — and $\varepsilon$ saturates at a much smaller
water path. That is why a thin high cloud can have a **positive** net forcing while
a thick low cloud has a strongly negative one, and the demonstration measures the
crossover. At $z_c = 12$ km, $T_c = 288.15 - 6.5\times12 = 210.15$ K, and with
$\mu_0S = 816.6\ \mathrm{W\,m^{-2}}$:

| LWP (g m⁻²) | $\tau$ | $R$ | $\varepsilon$ | CF_SW | CF_LW | net |
|---|---|---|---|---|---|---|
| 2 | 0.31 | 0.1498 | 0.0951 | −24.36 | +26.65 | **+2.28** |
| 5 | 0.78 | 0.1904 | 0.2210 | −57.50 | +61.95 | **+4.45** |
| 10 | 1.57 | 0.2489 | 0.3931 | −105.25 | +110.21 | **+4.96** |
| 20 | 3.14 | 0.3409 | 0.6317 | −180.40 | +177.08 | **−3.32** |
| 50 | 7.84 | 0.5115 | 0.9177 | −319.73 | +257.25 | **−62.48** |

(all fluxes in W m⁻²). The net passes through zero between LWP $= 10$ and
$20\ \mathrm{g\,m^{-2}}$ for this scene. The physics is in the *order* of the two
saturations, and it is robust to the closure error of §3.3 in the sense that both
terms are affected similarly; the *value* of the crossover water path is not.

### 3.6 The indirect effect on cloud albedo

At fixed liquid-water path, $r_e \propto N_d^{-1/3}$ (because LWP fixes
$\int Nr^3$) and therefore

$$\tau \propto N_d^{1/3} \quad\Rightarrow\quad
\frac{\mathrm{d}\ln\tau}{\mathrm{d}\ln N_d} = \frac13 . \tag{19}$$

Differentiating the albedo with respect to optical depth and using the asymptotic
result for a thick conservative layer gives the classical susceptibility

$$\frac{\mathrm{d}A}{\mathrm{d}\ln N_d} = \frac{\mathrm{d}A}{\mathrm{d}\ln\tau}
\cdot\frac13 \;\approx\; \frac{A(1-A)}{3} . \tag{20}$$

The demonstration measures both sides at LWP $= 100\ \mathrm{g\,m^{-2}}$
($\tau = 15.676$, $R = 0.6380$ with the delta-Eddington closure):

| $N_d/N_{\text{ref}}$ | $r_e$ ($\mu$m) | $\tau$ | $A$ | measured $\mathrm{d}A/\mathrm{d}\ln N_d$ | $A(1-A)/3$ |
|---|---|---|---|---|---|
| 0.25 | 15.87 | 9.88 | 0.5301 | — | 0.0830 |
| 0.50 | 12.60 | 12.44 | 0.5849 | 0.0791 | 0.0809 |
| 1.00 | 10.00 | 15.68 | 0.6380 | 0.0766 | 0.0770 |
| 2.00 | 7.94 | 19.75 | 0.6881 | 0.0724 | 0.0715 |
| 4.00 | 6.30 | 24.88 | 0.7345 | 0.0669 | 0.0650 |
| 8.00 | 5.00 | 31.35 | 0.7764 | 0.0604 | 0.0579 |

Doubling the droplet number changes the albedo by $+0.05019$ at this water path,
and (20) reproduces the measured derivative to within a few per cent. **That
agreement is a property of this regime, not an identity**: at this optical depth
the albedo is already near its saturating value, which is precisely the condition
under which (20) was derived. Both quantities are model outputs and both change if
the closure changes.

### 3.7 The aerosol direct effect: the sign criterion

Expand the solution of (10)–(11) to first order in a thin layer's optical depth
$\tau_a$ on a surface of albedo $\alpha_s$. Using (10) for $D$ and (11) for $S$,
and keeping the linear term in the surface boundary condition (the beam is slightly
attenuated on its way down and back):

$$\left.\frac{\mathrm{d}\alpha}{\mathrm{d}\tau_a}\right|_{0}
= \frac{q + r\,(a\alpha_s\mu_0 + p) - c\,\alpha_s\mu_0
- \dfrac{2\alpha_s}{1+\alpha_s}}{\mu_0(1-r)} . \tag{21}$$

The last term in the numerator is the beam attenuation at the surface; **omitting
it reverses the sign of the result for a moderately absorbing aerosol**, which is
exactly the kind of error a numerical check catches. The demonstration verifies
(21) against a numerical derivative of the full solution: for
$(\omega_0,\alpha_s) = (0.5,0.2)$ the analytic slope is $-0.14533$ and the measured
slope $-0.14487$; for $(0.95,0.2)$ they are $+0.34787$ and $+0.34697$. The residual
is the second-order term.

Solving (21) for the critical single-scattering albedo at $g = 0.30$,
$\mu_0 = 0.6$:

| $\alpha_s$ | critical $\omega_0$ | behaviour of a layer with $\omega_0 = 0.95$ |
|---|---|---|
| 0.05 | 0.2367 | brightens |
| 0.20 | 0.6326 | brightens |
| 0.50 | 0.9110 | brightens |

and the full solution at aerosol optical depth $0.15$ confirms the structure
($\Delta\alpha$ = scene albedo change):

| $\omega_0$ | $\alpha_s = 0.05$ | $\alpha_s = 0.20$ | $\alpha_s = 0.50$ |
|---|---|---|---|
| 0.70 | +0.04278 brighter | +0.00844 brighter | −0.05615 dimmer |
| 0.85 | +0.05849 brighter | +0.03103 brighter | −0.01761 dimmer |
| 0.95 | +0.06947 brighter | +0.04689 brighter | +0.00968 brighter |
| 1.00 | +0.07512 brighter | +0.05507 brighter | +0.02384 brighter |

The critical albedo rises with surface albedo, and above it the aerosol dims the
scene. **The criterion is a statement about a ratio of two things that are both
hard to measure** — how much the particle scatters and how bright the surface
beneath it is — which is why the *sign* of the direct effect is far more
accessible than its magnitude.

## 4. Physical interpretation

- **Optical depth is a water-path measurement.** By (7), the shortwave optical
  depth of a cloud is how much water is in the column divided by how finely it is
  divided — which is why the indirect effect exists: partitioning the same water
  into more droplets raises $\tau$ without changing LWP.
- **Albedo saturation sets the payoff.** The increments $\mathrm{d}R$ for a
  doubling of $\tau$ are $+0.1265$ at $\tau = 2$, peak at $+0.1628$ near
  $\tau = 5$, and fall to $+0.0482$ at $\tau = 80$: adding droplets to an already
  bright cloud buys almost nothing.
- **The longwave responds to water path, the shortwave to droplet size.** The
  emissivity depends on LWP alone (with $r_e$ fixed); the albedo depends on
  $\tau$ and hence on $r_e$. That asymmetry is the mechanism of the indirect
  effect, and it makes the two forcings saturate at different water paths.
- **Height sets the sign.** The longwave term of (18) is a difference of two
  fourth powers: raising a cloud cools it and increases
  $\sigma T_s^4 - \sigma T_c^4$ without changing its albedo. The sign flip of §3.5
  is a temperature argument, not an optical one.

## 5. Worked numerical examples

**Example 1: optical depth of a cloud.** LWP $= 200\ \mathrm{g\,m^{-2}}
= 0.2\ \mathrm{kg\,m^{-2}}$, $r_e = 10\ \mu$m. Geometric estimate from (7):

$$\tau = \frac{3 \times 0.2}{2 \times 1000 \times 10^{-5}} = \frac{0.6}{0.02} = 30.0 .$$

The Mie-integrated coefficient is $156.76\ \mathrm{m^2\,kg^{-1}}$, giving
$\tau = 156.76 \times 0.2 = 31.352$ — a **4.5%** correction, exactly the ratio
tabulated in §3.1. Using the delta-Eddington closure with $g = 0.8619$ and
$\mu_0 = 0.6$ gives a cloud albedo of $0.7764$ (§3.6 table), and the plain
Eddington closure gives the same value to five decimals ($0.77638$), which is the
statement that the two closures agree once the layer is thick.

**Example 2: emissivity and the longwave term.** For the same cloud
($\text{LWP} = 0.2\ \mathrm{kg\,m^{-2}}$):

$$\tau_{\text{abs}} = 49.94 \times 0.2 = 9.989,\qquad
\varepsilon = 1 - e^{-9.989} = 0.99995 .$$

With $T_s = 288.15$ K and a cloud at $5$ km where
$T_c = 288.15 - 6.5\times5 = 255.65$ K:
$\sigma T_s^4 = 5.670374419\times10^{-8}\times288.15^4 = 390.92\ \mathrm{W\,m^{-2}}$
and $\sigma T_c^4 = 5.670374419\times10^{-8}\times255.65^4 = 242.21\ \mathrm{W\,m^{-2}}$,
so $\text{CF}_{\text{LW}} = 0.99995 \times (390.92 - 242.21) = 147.7\mathrm{W\,m^{-2}}$ — matching the demonstration's $147.70$. For the same cloud at
$1$ km ($T_c = 281.65$ K, $\sigma T_c^4 = 356.82\ \mathrm{W\,m^{-2}}$) the longwave
forcing is only $33.87\ \mathrm{W\,m^{-2}}$, a factor $4.36$ smaller, while the
shortwave forcing is unchanged.

**Example 3: the sign criterion.** Take $g = 0.30$, $\mu_0 = 0.6$, $\alpha_s = 0.5$,
so that from (12) $a = 1.5(1-0.3\omega_0)$, $c = 2(1-\omega_0)$,
$p = 0.27\omega_0$, $q = \omega_0$, $r = -1/3$ and $2\alpha_s/(1+\alpha_s) = 2/3$.
Setting the numerator of (21) to zero and multiplying out:

$$\omega_0 - \tfrac13(0.45 + 0.135\omega_0) - 0.6 + 0.6\omega_0 - 0.6667 = 0
\;\Longrightarrow\; 1.555\,\omega_0 = 1.4167
\;\Longrightarrow\; \omega_0 = 0.9110,$$

the value in the §3.7 table. **Aerosols with $\omega_0$ below $0.91$ dim a scene of
albedo $0.5$; above it they brighten it**, and since the numerator depends
monotonically on $\alpha_s$ the threshold rises with surface albedo.

**Example 4: why a saturated albedo is uninformative.** The demonstration's
synthetic retrieval adds 2% relative noise to reflectance and inverts for $\tau$.
At $\tau = 2$ the retrieved value is $2.0 \pm 0.1$; at $\tau = 32$ it is
$31.6 \pm 2.6$; at $\tau = 128$ it is $125.3 \pm 39.1$. The information content
collapses because $\mathrm{d}R/\mathrm{d}\tau \to 0$: an albedo of $0.9334$ and one
of $0.9334 \pm 0.02$ correspond to optical depths differing by tens. **The
uncertainty is a property of the measurement geometry, not of the cloud.**

## 6. Assumptions and regime of validity

**Model assumptions, stated so they can be attacked.**

1. **Plane-parallel, horizontally homogeneous layers.** Real clouds are not; this
   is the leading error in broken cloud fields, where horizontal photon transport
   between cloudy and clear columns is large.
2. **Independent columns and a Lambertian surface.** No horizontal transport and no
   surface bidirectional reflectance.
3. **Azimuthally averaged transfer.** Valid for fluxes, not for radiances at a
   given azimuth; the glory, the corona and the cloud bow are discarded.
4. **Two-stream closure.** The largest single error in the lesson: the plain
   Eddington closure overestimates the thin-layer reflectance by a factor $1.83$,
   delta-Eddington by $1.22$. Every conclusion in §4 is therefore drawn from
   *comparisons within one closure* — changes, ratios, signs, saturation order —
   and never from an absolute albedo.
5. **Spherical homogeneous particles, one synthetic aerosol mode.** Mie values
   inherit the ripple of the exact solution, so fixed-size single-particle numbers
   are unreliable to a few per cent while ensemble averages are robust; real
   aerosol is internally and externally mixed, so no composition statement follows.
6. **No dynamics, chemistry or microphysics.** Droplet number is imposed, not
   predicted, so the indirect effect on *lifetime* is absent, and any real
   attribution would need a model in which $N_d$, LWP and cloud fraction all
   respond.
7. **No cloud fraction.** Every forcing number is an *overcast local* value; a
   global mean needs the joint distribution of cloud fraction, insolation, height
   and optical depth and is **not** the sum of the numbers in §3.5.

**Uncertainty and attribution statement.** In this lesson, the *measured* inputs of
the synthetic experiments are reflectances and transmittances; the retrieved
quantities are $\tau$ and $r_e$; the modelled quantities are albedos, emissivities,
forcings and the indirect-effect sensitivity. The indirect effect is an
*inference* from the covariation of droplet size and albedo; in this model the
covariation is built in by construction (19), so the demonstration measures the
sensitivity of the model, not of the atmosphere. Any real attribution of an
observed albedo change to a change in droplet number requires ruling out
simultaneous changes in LWP and cloud fraction, which a single-layer model cannot
do.

**Temperature and lapse-rate conventions.** $T_s = 288.15$ K and
$\Gamma = 6.5\ \mathrm{K\,km^{-1}}$ are stated conventions used to place a cloud at
a temperature; the longwave forcing is therefore proportional to a modelling
choice, not to a measured profile.

## 7. Units and dimensional analysis

- $\tau$, $\omega_0$ and $g$ are dimensionless by (2)–(4); $x$ is dimensionless
  with both lengths in the same unit.
- Mass coefficients are $\mathrm{m^2\,kg^{-1}}$, so $\tau = k\,\text{LWP}$ needs
  LWP in $\mathrm{kg\,m^{-2}}$ and $100\ \mathrm{g\,m^{-2}}$ is $0.1$, **not**
  $100$. With $k = 156.76$ and $k_{\text{abs}} = 49.94\ \mathrm{m^2\,kg^{-1}}$, a
  100 g m⁻² cloud has $\tau = 15.7$ and $\tau_{\text{abs}} = 5.0$.
- Albedo and emissivity lie in $[0,1]$; a printed value outside that range is a
  bug, which the finite-difference cross-check also tests.
- Forcing is $\mathrm{W\,m^{-2}}$ at the top of the atmosphere: the shortwave term
  scales with insolation, the longwave term with $\sigma T^4$.

## 8. Python demonstration

[`code/aerosols_and_clouds_radiation_demo.py`](code/aerosols_and_clouds_radiation_demo.py)
prints, in order: (1) Mie validation — energy conservation for a non-absorbing
sphere, the Rayleigh limit, the extinction paradox; (2) droplet and aerosol optics
and the optical depth per unit water path against the geometric formula; (3) the
two-stream identities for two closures, an independent finite-difference solution
of the same equations, and the thin-layer comparison against exact single
scattering; (4) cloud albedo, its saturation, and the indirect-effect
susceptibility; (5) longwave emissivity and the cloud-radiative-forcing
decomposition including a crossover scan; (6) the aerosol direct-effect sign
criterion and its verification against the full solution; (7) the
measured/modelled/inferred classification and a synthetic retrieval experiment.
It uses a fixed seed (`RNG = np.random.default_rng(20261014)`) and prints only
labelled numbers with units; it takes under a second and exits 0.

Exercises: [`exercises/06-aerosols-and-clouds-radiation-exercises.md`](exercises/06-aerosols-and-clouds-radiation-exercises.md)
with solutions in
[`exercises/06-aerosols-and-clouds-radiation-solutions.md`](exercises/06-aerosols-and-clouds-radiation-solutions.md).

## Mastery checkpoint

1. Compute the shortwave optical depth of a cloud with
   $\text{LWP} = 50\ \mathrm{g\,m^{-2}}$ and $r_e = 12\ \mu$m, both with (7) and
   with the Mie-integrated coefficient (interpolate between the tabulated values).
2. State which of the three identities of §3.2 still holds for an absorbing layer
   and which does not, with a one-line reason.
3. Compute the emissivity for LWP $= 30\ \mathrm{g\,m^{-2}}$ and $r_e = 10\ \mu$m,
   and the longwave forcing for that cloud at 3 km.
4. A cloud's droplet number is halved with LWP held fixed. Compute the new $r_e$,
   $\tau$ and albedo, and compare the albedo change with (20).
5. Using (21), determine whether an aerosol with $\omega_0 = 0.80$ brightens or
   dims a scene with $\alpha_s = 0.15$.
6. Explain in three sentences why the net cloud forcing can be positive for a thin
   high cloud but not for a thick low one.

## Common pitfalls

- **Using $3/(2\rho_wr_e)$ for the longwave.** The absorption efficiency, not the
  extinction efficiency, sets the infrared opacity: $3/(4\rho_wr_e)$, and then
  multiplied by a $Q_{\text{abs}}$ that is not 1 unless $x \gg 1$.
- **Confusing $\tau$ with LWP.** A mass extinction coefficient of
  $156.76\ \mathrm{m^2\,kg^{-1}}$ multiplies $\mathrm{kg\,m^{-2}}$; using
  $\mathrm{g\,m^{-2}}$ inflates $\tau$ by $10^3$.
- **Getting the beam sign wrong in (11).** The failure is not subtle — reflectances
  exceed 1 at moderate optical depth — but it is invisible if only qualitative
  statements are checked. Two exact identities plus an independent solver are what
  make it visible.
- **Quoting a two-stream albedo as a cloud property.** The closure error here is
  tens of per cent; only differences and signs survive it.
- **Treating the indirect effect as measured.** In this model it is imposed by
  (19); in the atmosphere it is inferred from covariation with confounders.
- **Adding local forcings to get a global mean.** Without the joint distribution
  of cloud fraction, insolation and cloud properties, that sum is meaningless.

## Related modules

- [16-02-01 Solar and Terrestrial Radiation](../02-radiation-and-energy-balance/01-solar-and-terrestrial-radiation.md)
  — the blackbody laws that all of the above is built on.
- [16-02-02 Radiative Transfer in the Atmosphere](../02-radiation-and-energy-balance/02-radiative-transfer-atmosphere.md)
  — grey layers and the emission level, used directly in §3.4–3.5.
- [16-02-04 Earth Energy Balance](../02-radiation-and-energy-balance/04-earth-energy-balance.md)
  — where the cloud forcing of (18) enters the planetary budget.
- [16-02-05 Energy Balance Models](../02-radiation-and-energy-balance/05-energy-balance-models.md)
  — what a forcing does to temperature once it is in the budget.
- [16-02 Module overview](../02-radiation-and-energy-balance/README.md)
  — how this lesson sits in the radiation sequence.
- [16-01-04 Moisture and Clouds](../01-atmospheric-structure-and-thermodynamics/04-moisture-and-clouds.md)
  — the thermodynamics that decide where a cloud forms.
- [16-03 Atmospheric Circulation](../03-atmospheric-circulation/README.md)
  — the dynamics that distributes the clouds whose distribution this lesson
  cannot supply.
- [16-08 Climate Observations and Data Products](../08-climate-observation-and-data/README.md)
  — how the quantities listed in §3.7 are actually observed.
- [02-10-03 Radiative Transfer](../../02-physics/10-optics-and-photometry/03-radiative-transfer.md)
  — the transfer equation for an absorbing and emitting medium.
- [17-01-03 Atmospheric Effects in Remote Sensing](../../17-remote-sensing-gis/01-remote-sensing-physics/03-atmospheric-effects.md)
  — the applied version of the same equations.
- [01-12-04 Numerical Integration](../../01-mathematics/12-numerical-methods/04-numerical-integration.md)
  — the quadrature used for the single-scattering reference.
