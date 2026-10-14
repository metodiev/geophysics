# Solutions — 02-11-03 Seismic Velocities, Elastic Moduli and Mineralogy

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Densities and velocities are **nominal**
> handbook characteristics unless stated otherwise.

---

## ★1 — Inverting the wave speeds

**(a)** $\mu = \rho v_s^2 = 2900\times(3.7\times10^3)^2 = 3.970\times10^{10}$ Pa
$= \mathbf{39.70}$ GPa. And
$\phi = 6.5^2-\tfrac43(3.7)^2 = 42.25-18.2533 = 23.997$ km² s⁻², so
$K = 2900\times23.997\times10^6 = 6.959\times10^{10}$ Pa $= \mathbf{69.59}$ GPa.

**(b)** $\phi = \mathbf{23.997}$ km² s⁻² $= 2.3997\times10^7$ m² s⁻², and
$\rho\phi = 2900\times2.3997\times10^7 = 6.959\times10^{10}$ Pa $=$ $K$ ✓. The
factor $10^6$ between km² s⁻² and m² s⁻² is the only conversion needed.

**(c)** $\nu = (42.25-2\times13.69)/[2(42.25-13.69)] = 14.87/57.12 = \mathbf{0.260}$.

**(d)** $K/\mu = 69.59/39.70 = 1.7529$; and
$(v_p/v_s)^2-\tfrac43 = (6.5/3.7)^2-1.3333 = 3.0861-1.3333 = 1.7529$ ✓. The
agreement to four digits is the arithmetic identity of ★2, and it is a useful
check on any velocity table.

---

## ★2 — The $K/\mu$ identity

**(a)** Divide $v_p^2$ by $v_s^2$:

$$\left(\frac{v_p}{v_s}\right)^2
= \frac{(K+\tfrac43\mu)/\rho}{\mu/\rho}
= \frac{K}{\mu}+\frac{4}{3}
\quad\Longrightarrow\quad
\frac{K}{\mu} = \left(\frac{v_p}{v_s}\right)^2-\frac{4}{3}. \qquad\blacksquare$$

**(b)** $K/\mu = 1.86^2-1.3333 = 3.4596-1.3333 = \mathbf{2.1263}$;
$\nu = (1.5\times2.1263-1)/(3\times2.1263+1) = (3.1895-1)/(6.3789+1)
= 2.1895/7.3789 = \mathbf{0.2967}$.

**(c)** $\nu = (1.86^2-2)/(2(1.86^2-1))$ in velocity form requires $\rho$-free
velocities: with $v_s = 1$ and $v_p = 1.86$,
$\nu = (3.4596-2)/(2(3.4596-1)) = 1.4596/4.9192 = 0.2967$ ✓.

**(d)** The error is treating the square as linear. From (a),
$K/\mu = (v_p/v_s)^2-4/3$, so $K/\mu = 3.2$ implies
$(v_p/v_s)^2 = 4.533$ and $v_p/v_s = 2.129$, not 3.2. The colleague has forgotten
the square, which is a factor of 1.5 in this case.

---

## ★3 — Impedance and reflection

**(a)** With $\rho$ in kg m⁻³ and $v$ in km/s, $Z = \rho v_p$ is in
$10^3$ kg m⁻² s⁻¹:
$Z_1 = 4400\times10.3 = 45\,320$; $Z_2 = 4600\times10.9 = 50\,140$.

**(b)** $R = (50\,140-45\,320)/(50\,140+45\,320) = 4820/95\,460 = \mathbf{0.0505}$,
i.e. 5.05 per cent of amplitude.

**(c)** The energy reflection coefficient is $R^2 = 0.00255$, i.e.
**0.255 per cent** — a factor of $R$ smaller than the amplitude figure, which is
why amplitude and energy must never be quoted interchangeably.

**(d)** Two effects, in opposite directions. A *lower* $v_{p2}$ reduces $Z_2$ and
therefore reduces $R$ towards zero — the partial cancellation of §5 of the lesson.
And if $Z_2$ fell below $Z_1$, $R$ would become **negative**, meaning a
phase reversal on reflection; the magnitude would then grow again as the
impedance contrast grew.

---

## ★4 — Limits

**(a)** Poisson solid: $v_p/v_s = \sqrt3 = \mathbf{1.732}$,
$\nu = \mathbf{0.25}$,
$K/\mu = 5/3 = \mathbf{1.667}$.

**(b)** $K/\mu = 1.8^2-1.3333 = 3.24-1.3333 = 1.9067$;
$\nu = (1.5\times1.9067-1)/(3\times1.9067+1) = 1.8600/6.7200 = \mathbf{0.2768}$.
This is close to the upper mantle's 0.277.

**(c)** As $v_p/v_s\to\infty$, $K/\mu\to\infty$ and $\nu\to0.5$. The limit is
$\mu\to0$ at fixed $K$: a material that resists compression but not shear at all —
a **fluid**. In the outer core this is reached exactly, and it is why $v_s = 0$
there.

**(d)** $K/\mu = 3.1^2-1.3333 = 9.61-1.3333 = \mathbf{8.28}$. That is **4.4 times**
the mantle's approximately 2, so relative to its resistance to compression the
inner core resists shear very poorly. It is a peculiar state of matter, not an
extrapolation of the mantle trend, and it is one of the seismological constraints
that any inner-core composition model must reproduce.

---

## ★★5 — The density–velocity degeneracy

**(a)** $\phi = 8.0^2-\tfrac43(4.5)^2 = 64-27 = \mathbf{37.0}$ km² s⁻².

**(b)**

| $\rho$ (kg m⁻³) | $\mu$ (GPa) | $K$ (GPa) | $\nu$ |
|---|---|---|---|
| 3000 | 60.75 | 111.0 | 0.2686 |
| 5000 | 101.25 | 185.0 | 0.2686 |
| 8000 | 162.0 | 296.0 | 0.2686 |

**(c)** $\phi$ and $\nu$ are independent of $\rho$ — they are functions of the
velocities alone. $\mu$ and $K$ scale **linearly** with $\rho$: tripling the
density triples both moduli.

**(d)** Because $v_p$ and $v_s$ determine only $K/\rho$ and $\mu/\rho$, and both
of those ratios are identical for crustal rock and for a much denser material with
the same speeds. Seismology measures $K/\rho$ and $\mu/\rho$; it does not measure
$K$, $\mu$ or $\rho$ separately. Three resolving measurements: (i) free
oscillations or a moment-of-inertia constraint, which fixes the absolute
densities; (ii) an independent equation of state that predicts $\rho(P,T)$ for a
candidate composition; (iii) in the shallow crust, a density log or gravity
survey, which measures $\rho$ directly.

---

## ★★6 — Birch's law

**(a)** At $\rho = 3300$ kg m⁻³ $= 3.3$ g cm⁻³:
$v_p = -0.6258+2.5576\times3.3 = -0.6258+8.4401 = 7.81$ km/s, against the handbook
8.10, so residual $-0.29$ km/s, $+3.5$ per cent of the observed value. At
$\rho = 4000$ kg m⁻³: $v_p = -0.6258+10.2304 = 9.60$ km/s against 9.70, residual
$-0.10$ km/s, $-1.0$ per cent. Both agree with the demo's table.

**(b)** At $\rho = 4400$ kg m⁻³ $= 4.4$ g cm⁻³:
$v_p = -0.6258+2.5576\times4.4 = -0.6258+11.2534 = 10.63$ km/s, against the
handbook 10.3 km/s. Residual $+0.33$ km/s, $+3.2$ per cent. So the law holds to a
few per cent throughout the mantle and is slightly biased high at the base of the
transition zone.

**(c)** $v_p = -0.6258+2.5576\times11.05 = -0.6258+28.2615 = 27.64$ km/s, against
9.15 observed — a factor of three wrong in the wrong direction. The size of the
misfit measures the **change of mean atomic weight**: the core's mean atomic
weight is near iron's (about 50) rather than a silicate's (about 20), and at fixed
density a heavier mean atomic weight gives a lower velocity. The law is a
correlation at constant mean atomic weight, so the violation *is* the signal that
the mean atomic weight has changed.

**(d)** The assumption is a constant mean atomic weight (equivalently, that the
correlation was calibrated on a family of similar materials). It is violated at
the core–mantle boundary, where the material changes from silicate to metal.
The corollary is that Birch's law must not be extrapolated across a known
compositional boundary, and a claim of a "dense core" derived from extrapolated
velocities alone is not defensible.

---

## ★★7 — The outer core

**(a)** $v_s = 0$ means $\mu = \mathbf{0}$ exactly. Then
$\phi = v_p^2 = 64.0$ km² s⁻² $= 6.40\times10^7$ m² s⁻² and
$K = 9900\times6.40\times10^7 = 6.336\times10^{11}$ Pa $= \mathbf{633.6}$ GPa.

**(b)** Above: $\phi = 13.7^2-\tfrac43(7.3)^2 = 187.69-71.05
= \mathbf{116.64}$ km² s⁻².

**(c)** $\phi$ ratio $= 64.0/116.64 = \mathbf{0.549}$ (a drop of 45 per cent);
$K$ ratio $= 633.6/649.7 = \mathbf{0.975}$ (a drop of 2.5 per cent).

**(d)** $K$ is a material property that is primarily set by the electron density
and is continuous across a compositional boundary to within a few per cent; a
nearly unchanged $K$ across the CMB is physically unremarkable. $\phi = K/\rho$,
however, is divided by a density that jumps by a factor of 1.78, so $\phi$
necessarily drops by nearly that factor even though $K$ is unchanged. The lesson is
that **$\phi$ mixes a material property with the density, and $K$ alone does not.**

---

## ★★8 — Impedance contrasts across the boundaries

**(a)–(c)** From the demo:

| Boundary | Density contrast | $Z_1$ ($10^3$ kg m⁻² s⁻¹) | $Z_2$ | $R$ | $R$ (%) |
|---|---|---|---|---|---|
| Moho | 1.14 | 18.850 | 26.730 | 0.1729 | 17.29 |
| 410 km | 1.00 | 29.160 | 32.760 | 0.0581 | 5.81 |
| CMB | 1.78 | 76.309 | 79.200 | 0.0186 | 1.86 |
| ICB | 1.05 | 125.660 | 140.800 | 0.0568 | 5.68 |

Ranked by impedance contrast: Moho > 410 km > ICB > CMB. Ranked by density
contrast: CMB > Moho > ICB > 410 km (where the contrast is exactly 1.00 in this
rounded model). **The two rankings are nearly reversed.**

**(d)** Because $Z = \rho v_p$ and the two factors multiply. At the CMB, $\rho$
rises by 78 per cent while $v_p$ falls by 42 per cent, and $(1.78)(0.58) = 1.03$ —
$Z$ changes by only 3 per cent. At the Moho, $\rho$ rises by 14 per cent and $v_p$
*also* rises, by 25 per cent, so the factors multiply and $Z$ rises by 42 per cent.
Where the factors reinforce, the boundary is a strong reflector; where they
partially cancel, it is a weak one.

---

## ★★★9 — Phase boundary versus chemical boundary

**(a)** A boundary produces a step in $\rho$, in $v_p$ and in $v_s$, and hence a
reflection and a conversion of wave types. A phase boundary and a chemical
boundary both produce all of these, so the seismological signature *alone* does
not distinguish them: any sharp change of elastic properties reflects.

**(b)** For a phase change with Clapeyron slope $\gamma = \mathrm{d}P/\mathrm{d}T$,
the depth shift for a temperature anomaly $\Delta T$ is
$\Delta z = \gamma\,\Delta T/(\rho g)$. A positive slope (the 410 km, adoption of
$+2$ to $+3$ MPa/K) means a **hot** mantle **deepens** the boundary; a negative
slope (the 660 km, $-2$ to $-3$ MPa/K) means a hot mantle **shallows** it. So a
temperature anomaly of one sign displaces the two discontinuities in **opposite**
directions — an anti-correlation.

**(c)** Measure the depths of the 410 km and 660 km discontinuities beneath a
region of known thermal anomaly — a subducting slab (cold) or a mantle plume (hot)
— using receiver functions or SS precursors. The confirming pattern is that the
two depths shift in opposite directions, with the 410 shallower and the 660 deeper
beneath a cold slab, and the reverse beneath a hot plume. A chemical boundary
would have no reason to respond to temperature at all, and certainly not in an
anti-correlated way between two different depths.

**(d)** The 410 and 660 are matched by laboratory determinations of the relevant
reactions' Clapeyron slopes, so a *quantitative* prediction exists to be tested.
The core–mantle boundary has no such calibration: no phase change of a
silicate or a metal at 135 GPa has the required volume change to produce a factor
of 1.78 density jump at essentially fixed pressure. The boundary cannot be tested
by the Clapeyron method because there is no reaction to test, which is itself the
argument for its chemical nature.

---

## ★★★10 — Amplitude, energy and angle

**(a)** The energy flux is proportional to impedance times the square of
amplitude, and at a boundary with the same geometry on both sides the transmitted
and reflected powers must sum to the incident. Solving the two boundary conditions
gives a reflected *power* fraction of $R^2$ for amplitude coefficient $R$. For
$R = 0.0186$: $R^2 = 3.46\times10^{-4}$, i.e. **0.035 per cent** of the energy.

**(b)** Because at normal incidence the reflection is controlled by the impedance
ratio alone, and the ratio is nearly 1. At oblique incidence the boundary
conditions involve the shear modulus and the ray parameter, and the P-reflection
coefficient becomes a function of angle; it rises appreciably as the incidence
angle approaches the critical angle for the transmitted P wave, and beyond that
angle the transmitted wave becomes evanescent. That angular dependence is the
origin of the PKP caustic structure.

**(c)** Because $\mu = 0$ in the fluid outer core, so there is no transmitted shear
wave and all the incident shear energy is reflected: $|R_S| = 1$. The minus sign
means a **phase reversal** of 180° for reflection from the lower-impedance side
(the core), which is the standard behaviour of a free-surface-like reflection.

**(d)** Two things. First, $R$ is a *normal-incidence* result and most observed
arrivals encounter the boundary obliquely, where $R$ is not 0.019. Second, and
more importantly, the energy accounting must include **mode conversion**: an
incident P wave at the CMB produces a reflected S as well as a reflected P, and an
incident S wave produces converted P. The shear channel is where the CMB is
decisive, and it is invisible in a P-only normal-incidence calculation.

---

## ★★★11 — What the isotropic inversion omits

**(a)** When the real material is anisotropic, a reference model reports the
**isotropic average** of the corresponding combination of the elastic tensor
components — a velocity that is what a hypothetical isotropic material with the
same average behaviour would have. Two models can agree on the average and differ
in the anisotropy.

**(b)** An anisotropic medium has three body-wave speeds in the general case (one
quasi-compressional and two quasi-shear), and in the common case of hexagonal
symmetry with a vertical axis it has a fast and a slow shear wave. The observable
is **shear-wave splitting**: a single shear arrival is split into two with
different polarisations and a time lag proportional to the anisotropy and the path
length.

**(c)** Because anisotropy is a consequence of the *alignment* of a material's
constituents: crystal preferred orientation from past strain, or aligned
inclusions. A measured anisotropy therefore constrains the deformation history and
the mechanism — for example, it is how flow directions in the lowermost mantle are
inferred. A perfectly isotropic deep Earth would tell us nothing about how it
deformed.

**(d)** The reported precision is unwarranted: the inversion has converted a
directional observation into a single scalar by averaging, and the anisotropy (3
per cent) is a systematic uncertainty larger than the third digit being quoted.
The appropriate statement is the isotropic-average moduli to two significant
figures, with the anisotropy explicitly reported alongside as a separate
measurement and not folded into the inversion.
