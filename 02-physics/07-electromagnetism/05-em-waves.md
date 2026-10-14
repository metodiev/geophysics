---
id: 02-07-05
title: "Electromagnetic Waves, Impedance and Polarisation"
level: advanced
prereqs: ["02-07-03", "02-07-04", "01-11-01"]
estimated_minutes: 90
tags: [em-waves, wave-impedance, polarisation, magnetotellurics, apparent-resistivity]
---

# Electromagnetic Waves, Impedance and Polarisation

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the plane-wave solution of the wave equation and prove that
   $\mathbf E$, $\mathbf B$ and the propagation direction form a right-handed
   orthogonal triple.
2. **Define** the wave impedance $\eta = \sqrt{\mu/\varepsilon}$, show that
   $E/H = \eta$, verify $\eta_0 = \mu_0c = 376.730\,314$ Ω, and check the
   dimensions of $E/H$ in full.
3. **Explain** why a magnetotelluric survey measures $\mathbf E/\mathbf H$ and
   why the ratio is a property of the ground rather than of the ionospheric
   source.
4. **Derive** the apparent resistivity of a uniform half-space,
   $\rho_a = |Z|^2/(\omega\mu_0)$, show that it returns the true resistivity
   exactly and that the phase is 45°, and interpret the two-layer response.
5. **State** the complex impedance of a general lossy medium and reduce it to the
   lossless and strongly-conductive limits.
6. **Describe** linear, circular and elliptical polarisation and compute Stokes
   parameters, verifying $S_1^2+S_2^2+S_3^2 = S_0^2$.
7. **Compute** a normal-incidence reflection coefficient from an impedance
   mismatch and use it to explain GPR reflections.

## Prerequisites

- [02-07-03 Maxwell's Equations and Their Physical Meaning](./03-maxwell-equations.md)
  — the wave equation, and the Helmholtz equation it comes from.
- [02-07-04 Faraday's Law, Induction and Eddy Currents](./04-em-induction.md)
  — the diffusive limit, which is the low-frequency face of the same impedance.
- [01-11-01 Complex Arithmetic](../../01-mathematics/11-complex-analysis/01-complex-arithmetic.md)
  — complex amplitudes, phases and the exponential notation used throughout.

## 1. Plane waves, and why the transverse geometry is forced

In a charge-free, non-conducting, uniform medium, Maxwell's equations give the
wave equation (lesson [02-07-03](./03-maxwell-equations.md) equation 3). Its
simplest solution is the **plane wave**:

$$\mathbf E = \mathbf E_0\,e^{i(\mathbf k\cdot\mathbf r - \omega t)},
\qquad
\mathbf B = \mathbf B_0\,e^{i(\mathbf k\cdot\mathbf r - \omega t)} , \tag{1}$$

with $|\mathbf k| = k = \omega\sqrt{\mu\varepsilon} = \omega/v$. Substituting (1)
into the two divergence equations shows that

$$\mathbf k\cdot\mathbf E_0 = 0, \qquad \mathbf k\cdot\mathbf B_0 = 0 : \tag{2}$$

**both fields are transverse to the direction of propagation.** No longitudinal
electromagnetic wave exists in a source-free medium — a sharp contrast with
elastic waves, where $\mathbf u$ is *parallel* to $\mathbf k$ for a P wave
([02-04-05](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)). The
physical reason is Gauss's law: a longitudinal electric field would require net
charge density in a region that has none.

Faraday's law then fixes the relative magnitude and orientation. Substituting (1)
and using $\partial/\partial t\to-i\omega$ and $\nabla\to i\mathbf k$:

$$i\mathbf k\times\mathbf E_0 = i\omega\mathbf B_0
\qquad\Longrightarrow\qquad
\mathbf B_0 = \frac{\mathbf k\times\mathbf E_0}{\omega} . \tag{3}$$

So $\mathbf B$ is perpendicular to $\mathbf E$ *and* to $\mathbf k$: the triple
$(\mathbf E,\mathbf B,\hat{\mathbf k})$ is right-handed and mutually orthogonal,
and $E/B = \omega/k = v$. In a vacuum $E/B = c$ exactly; this is the cleanest
way to remember why the ratio $\mathbf E/\mathbf B$ has units of speed while
$\mathbf E/\mathbf H$ has units of resistance.

## 2. Wave impedance: why $E/H$ is an ohm

Dividing the magnetic relation (3) rewritten for $\mathbf H = \mathbf B/\mu$ by
the electric amplitude defines the **intrinsic impedance** of the medium:

$$\boxed{\ \eta = \frac{E_0}{H_0} = \frac{\omega\mu}{k} = \sqrt{\frac{\mu}{\varepsilon}}\ } , \tag{4}$$

and this is the first appearance of the quantity that organises the rest of the
module. Its dimensions:

$$[\eta] = \sqrt{\frac{[\mu]}{[\varepsilon]}}
= \sqrt{\frac{\mathrm{H/m}}{\mathrm{F/m}}}
= \sqrt{\frac{\mathrm{V\,s/(A\,m)}}{\mathrm{A\,s/(V\,m)}}}
= \sqrt{\frac{\mathrm V^2}{\mathrm A^2}} = \frac{\mathrm V}{\mathrm A} = \Omega . \tag{5}$$

Equivalently, directly from the fields: $[\mathbf E/\mathbf H] =
\mathrm{(V/m)/(A/m)} = \Omega$. There is no factor of $4\pi$ to argue about: a
ratio of an electric field to a magnetic field *is* a resistance per square.

For vacuum (and, to within a part in a thousand, for air):

$$\eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} = \mu_0c
= (1.25663706212\times10^{-6})(2.99792458\times10^{8})
= 376.730\,314\ \Omega . \tag{6}$$

The two forms agree because $\varepsilon_0 \equiv 1/(\mu_0c^2)$, so
$\eta_0 = \sqrt{\mu_0\cdot\mu_0c^2} = \mu_0c$ is an identity. In a non-magnetic
dielectric, $\eta = \eta_0/\sqrt{\varepsilon_r}$: 188.4 Ω for
$\varepsilon_r = 4$, 41.9 Ω for $\varepsilon_r = 81$ (water-like).

**The general lossy medium.** For a medium with both conduction and displacement
currents the Helmholtz relation $\mathbf k = \omega\sqrt{\mu\varepsilon}\,
(1 - i\sigma/\omega\varepsilon)^{1/2}$ gives

$$\eta = \frac{\omega\mu}{k}
= \sqrt{\frac{i\omega\mu}{\sigma + i\omega\varepsilon}} , \tag{7}$$

with the two instructive limits

$$\sigma \ll \omega\varepsilon:\quad \eta \to \sqrt{\frac{\mu}{\varepsilon}} \ \text{(real, wave-like)},
\qquad
\sigma \gg \omega\varepsilon:\quad \eta \to \sqrt{\frac{\omega\mu}{2\sigma}}(1+i) \ \text{(45°, diffusive).} \tag{8}$$

The 45° phase of the diffusive limit is the whole reason magnetotelluric data are
reported as *amplitude and phase*, and the whole reason a half-space MT phase is
45°: in a diffusive field decay and lag are the same number (lesson
[02-07-06](./06-em-in-conductors.md)).

## 3. Physical interpretation: what a magnetotelluric survey measures

Natural electromagnetic fields from the ionosphere and magnetosphere arrive at the
Earth's surface as (locally) plane waves with a broad spectrum of periods. The
horizontal electric and magnetic fields at the surface are recorded, and the
datum is their ratio:

$$Z(\omega) = \frac{E_x(\omega)}{H_y(\omega)} , \tag{9}$$

a **complex transfer function** — an impedance — in ohms. Three things make this
the foundation of the method:

1. **The source cancels.** Whatever current system in the ionosphere produced the
   wave, $E$ and $H$ both scale with its strength, so $Z$ does not depend on it.
   This is why MT works without any knowledge of the ionospheric current system —
   a property no controlled-source method has to rely on.
2. **The ground sets the impedance.** $Z$ is a functional of the conductivity
   distribution, not of the geometry of the source, provided the source is
   sufficiently distant and laterally uniform (the *plane-wave assumption*,
   whose failure is the main systematic error in MT).
3. **The frequency selects depth.** Because the penetration is diffusive with
   $\delta\propto\sqrt{1/\omega}$ (lesson [02-07-06](./06-em-in-conductors.md)),
   a broad period range samples a broad depth range in one measurement.

**Apparent resistivity and phase.** For a uniform half-space of resistivity
$\rho$, equation (8) with $\sigma = 1/\rho$ gives
$|Z| = \sqrt{\omega\mu_0\rho}$ and a phase of 45°. Inverting:

$$\boxed{\ \rho_a = \frac{|Z|^2}{\omega\mu_0}\ }
\qquad\text{and}\qquad \phi = \arg Z , \tag{10}$$

and for the half-space this returns $\rho_a = \rho$ **exactly** at every period,
with $\phi = 45.0000°$ at every period. The demo verifies both, to six decimal
places. Everything interesting in MT is therefore a *departure* of
$(\rho_a,\phi)$ from a constant, 45° pair: layering, anisotropy and
three-dimensionality.

**The general case: an impedance tensor.** For a 3-D Earth the linear relation
between $\mathbf E$ and $\mathbf H$ couples components:

$$\begin{pmatrix}E_x\\E_y\end{pmatrix}
= \begin{pmatrix}Z_{xx} & Z_{xy}\\ Z_{yx} & Z_{yy}\end{pmatrix}
\begin{pmatrix}H_x\\H_y\end{pmatrix} . \tag{11}$$

For a 1-D (layered) Earth $Z_{xy} = -Z_{yx} = Z$ and $Z_{xx} = Z_{yy} = 0$; the
tensor's off-diagonal symmetry and the presence of a *tipper* (the vertical field
as a linear function of the horizontal ones) are the standard diagnostics of
two- and three-dimensional structure. The tensor is where the *polarisation* of
the field becomes a measurement rather than a nuisance.

**The two-layer response.** A first layer of resistivity $\rho_1$ and thickness
$d$ over a basement $\rho_2$ shows: $\rho_a \to \rho_1$ and $\phi\to45°$ for
periods short enough that the field dies before reaching the interface; a
transition in which $\phi$ departs from 45°; and $\rho_a\to\rho_2$ for long
periods. The crossover period is set by $\delta(\rho_1)\approx d$, i.e.

$$T_{\text{cross}} \approx \frac{\pi\mu_0 d^2}{\rho_1} , \tag{12}$$

which for $d = 5$ km and $\rho_1 = 100$ Ω·m is 0.987 s. The demo's two-layer run
shows exactly this transition: $\rho_a$ rises from 100 Ω·m to 837 Ω·m between
$T = 0.1$ s and $T = 1000$ s while the phase dips to 25.6°.

## 4. Polarisation

A monochromatic plane wave propagating along $z$ has
$\mathbf E = (E_x,E_y)$ with the two components possibly differing in amplitude
and phase. Writing $E_x = a_x\cos\omega t$ and $E_y = a_y\cos(\omega t+\phi)$, the
locus of the tip of $\mathbf E$ is an ellipse (a line and a circle are degenerate
cases). The **Stokes parameters**

$$S_0 = a_x^2+a_y^2, \quad
S_1 = a_x^2-a_y^2, \quad
S_2 = 2a_xa_y\cos\phi, \quad
S_3 = 2a_xa_y\sin\phi \tag{13}$$

satisfy $S_1^2+S_2^2+S_3^2 = S_0^2$ for fully polarised light (verified to
zero in the demo), and classify the state:

| State | Condition | Meaning |
|---|---|---|
| Linear | $S_3=0$, $\lvert S_2\rvert\le S_0$ | tip oscillates along a line |
| Circular | $\lvert S_3\rvert = S_0$ | tip traces a circle; sign gives hand-edness |
| Elliptical | otherwise | the general case |

**Why polarisation matters in EM geophysics.** The incident natural field is not
perfectly polarised — it is a superposition of many sources and is partially
coherent only over a limited time and bandwidth. What is measured is the
*relationship* between the horizontal $\mathbf E$ and $\mathbf H$, i.e. the
impedance tensor (11). An isotropic 1-D Earth produces a response that is
independent of the polarisation of the incident field; a 2-D or 3-D Earth
couples the components, so the response depends on the polarisation and the
principal axes must be estimated. The standard 2-D decomposition, the
identification of the *strike* direction and the use of the tipper all rest on
this. In controlled-source systems the same idea appears as the choice of
transmitter and receiver coil orientations — a coplanar or coaxial configuration
probes different components of the conductivity structure.

## 5. Reflection and refraction at an interface

At normal incidence on a plane interface between media of impedance $\eta_1$ and
$\eta_2$, continuity of the tangential $\mathbf E$ and $\mathbf H$ gives the
reflection and transmission coefficients

$$r = \frac{\eta_2-\eta_1}{\eta_2+\eta_1}, \qquad t = \frac{2\eta_2}{\eta_2+\eta_1},
\qquad R = |r|^2, \qquad T = 1-R . \tag{14}$$

For lossless dielectrics, substituting $\eta = \eta_0/\sqrt{\varepsilon_r}$
yields the familiar GPR form

$$r = \frac{\sqrt{\varepsilon_1}-\sqrt{\varepsilon_2}}{\sqrt{\varepsilon_1}+\sqrt{\varepsilon_2}} . \tag{15}$$

Two worked numbers:

- **Dry soil over saturated soil** ($\varepsilon_r$ from 4 to 25):
  $r = (2-5)/(2+5) = -0.4286$, so $R = 0.1837$: about **18 % of the incident
  energy** is reflected, with a 180° phase inversion. This is the strongest
  contrast in most near-surface GPR sections and is why the water table is often
  visible as a reflector.
- **Soil over air** ($\varepsilon_r$ from 4 to 1):
  $r = (2-1)/(2+1) = +0.3333$, $R = 0.1111$: 11 % reflected with no phase
  inversion. This is the ground–air reflection that produces the strong "surface"
  event in any GPR record and the reason antennas must be shielded.

In a conducting medium the impedance is complex, so $r$ is complex: reflection
carries a phase shift that is itself diagnostic. The general form (14) remains
valid.

## 6. Assumptions and regime of validity

| Assumption | Where it entered | What breaks outside it |
|---|---|---|
| A uniform, distant plane-wave source | Section 3's claim that the source cancels | Fails near the coastline (the coast effect) and under the auroral electrojet (the source effect); both bias $\rho_a$ systematically and are the main interpretational hazard in MT |
| Time-harmonic steady state | Writing every field as $e^{i\omega t}$ | Transients (a TEM switch-off) must be treated in the time domain or by Fourier synthesis |
| Linear, isotropic media with scalar $\sigma$, $\varepsilon$ | The scalar impedance | Anisotropic rock makes $\sigma$ a tensor; the impedance becomes the tensor (11) and the principal axes must be estimated (exercise ★★★10) |
| Non-magnetic medium | $\eta = \sqrt{\mu/\varepsilon}$ | $\mu_r\neq1$ changes both the impedance and the skin depth |
| Normal incidence for the reflection coefficients | Equations (14)–(15) | Oblique incidence: Fresnel coefficients, polarisation dependence, a Brewster angle and total internal reflection all appear |
| Lossless dielectrics for equation (15) | Deriving the $\sqrt{\varepsilon}$ form | In a lossy medium $\eta$ is complex and the reflection coefficient carries a phase shift (equation 7) |
| The medium is thicker than the penetration depth | The half-space formulas | A thin layer is described by its conductance, not its resistivity, and $\rho_a$ then grows with period instead of saturating (lesson [02-07-06](./06-em-in-conductors.md) ★★★10) |
| The measured $\mathbf E$ and $\mathbf H$ are the Earth's response alone | Throughout | Anthropogenic noise below 1 s in populated regions dominates the natural signal; this, not theory, limits most MT surveys |

The first and last rows together define the practical boundaries of the method: the
*physics* of MT is the impedance relation, and the *difficulty* of MT is that both
the source and the ambient noise violate the assumptions under which the relation
is exact.

## 7. Units and dimensional analysis

- $[\eta] = \Omega$ (equation 5).
- $[Z] = [\mathbf E]/[\mathbf H] = \Omega$; the MT impedance is literally an ohm.
- $[\rho_a] = [|Z|^2/(\omega\mu_0)] = \Omega^2/(\mathrm{s^{-1}\,H/m}) = \Omega^2\cdot\mathrm{m/(H\,s^{-1})}$;
  since $\mathrm{H = \Omega\,s}$, this is $\Omega^2\mathrm{m/(\Omega\,s\cdot s^{-1})} = \Omega\,\mathrm m$ ✓.
- $[\mathbf E/\mathbf B] = \mathrm{(V/m)/T} = \mathrm{m/s}$ ✓ — a speed, not an
  impedance. The two ratios differ by $\mu$, and conflating them is the most common
  error in this lesson.
- A useful anchor: at $T = 1$ s in 100 Ω·m rock, $|Z| = 2.81\times10^{-2}$ Ω
  (from the demo). MT impedances are tiny numbers; the amplification and
  calibration chain is what makes the measurement hard.

## 8. Python demonstration

[`code/em_waves_demo.py`](./code/em_waves_demo.py) verifies every claim above.
Observed output:

```text
sqrt(mu0/eps0) = 376.730314 ohm
mu0 c          = 376.730314 ohm
difference     = 8.185e-12 ohm
   eps_r    eta = eta0/sqrt(eps_r) (ohm)
       1                        376.7303
       4                        188.3652
      20                         84.2395
      81                         41.8589
```

```text
rho = 100 ohm m
   T (s)     delta (m)     |Z| (ohm)        Z real        Z imag   rho_a (ohm m)   phase (deg)
   0.001         159.2  8.885766e-01  6.283185e-01  6.283185e-01      100.000000       45.0000
   1.000        5032.9  2.809926e-02  1.986918e-02  1.986918e-02      100.000000       45.0000
1000.000      159154.9  8.885766e-04  6.283185e-04  6.283185e-04      100.000000       45.0000
```

```text
layer 1: 100 ohm m to 5 km;  half-space below: 1000 ohm m
   T (s)   delta_1 (m)     |Z| (ohm)   rho_a (ohm m)   phase (deg)
   0.001         159.2  8.885766e-01        100.0000       45.0000
   0.010         503.3  2.809926e-01        100.0000       45.0000
   0.100        1591.5  8.903023e-02        100.3888       45.0000
   1.000        5032.9  2.653289e-02         89.1619       37.5384
  10.000       15915.5  1.384370e-02        242.7250       25.5616
 100.000       50329.2  6.779722e-03        582.1488       33.3941
1000.000      159154.9  2.570918e-03        837.1178       40.4032
  T for delta = 5 km in 100 ohm m: T = pi mu0 d^2/rho = 0.9870 s
```

```text
                  case    ax    ay  phi (deg)      S0      S1      S2      S3     check
         linear, 0 deg   1.0   0.0        0.0    1.00    1.00    0.00    0.00  0.00e+00
        linear, 45 deg   1.0   1.0        0.0    2.00    0.00    2.00    0.00  0.00e+00
        circular right   1.0   1.0      -90.0    2.00    0.00    0.00   -2.00  0.00e+00
         circular left   1.0   1.0       90.0    2.00    0.00    0.00    2.00  0.00e+00
        elliptical 2:1   2.0   1.0       90.0    5.00    3.00    0.00    4.00  0.00e+00
```

```text
[E/H] = (kg m s^-3 A^-1) / (A m^-1) = kg m^2 s^-3 A^-2
      = W A^-2 = V A^-1 = ohm
```

### What to observe

| Observation | Consequence |
|---|---|
| $\sqrt{\mu_0/\varepsilon_0}$ and $\mu_0c$ agree to $8\times10^{-12}$ Ω, i.e. to the rounding of the tabulated $\mu_0$ | Equation (6) is an identity, not a coincidence: it follows from the definition of $\varepsilon_0$ |
| $\eta$ falls as $1/\sqrt{\varepsilon_r}$, from 376.73 Ω to 41.86 Ω | The impedance of a medium is set by its permittivity alone, for non-magnetic materials |
| For a 100 Ω·m half-space, $\rho_a = 100.000000$ Ω·m and $\phi = 45.0000°$ at *every* period from 1 ms to 1000 s | Equation (10) is exact for a half-space; a uniform Earth carries no depth information — only its resistivity |
| $|Z|$ falls by exactly $\sqrt{10}$ per decade of period | $|Z| \propto \omega^{-1/2}$: the same square-root law as the skin depth, seen from the impedance side |
| The two-layer model returns 100 Ω·m for short periods, 837 Ω·m at $T = 1000$ s, and $\phi$ dips to 25.6° in between | The transition *is* the sounding; the phase dip is the classic indicator of a resistive basement beneath a conductor |
| The crossover period from equation (12), 0.9870 s, matches the onset of the transition at $T = 0.1$–1 s | The skin depth gives a reliable first-order depth estimate before any inversion |
| All five polarisation states satisfy $S_1^2+S_2^2+S_3^2-S_0^2 = 0.00\times10^{0}$ | Equation (13) as implemented is consistent; the Stokes description is complete for fully polarised fields |
| The dimension reduction gives $\Omega$ exactly | There is no hidden factor of $\mu_0$ in $E/H$; the ratio is an impedance in SI |

> **Breaking exercise.** Change the basement resistivity in the two-layer model
> from 1000 Ω·m to 10 Ω·m and predict, before running, whether the phase will
> rise above 45° or dip below it. Then run it. Relate the sign of the phase
> excursion to whether the deeper layer is more or less resistive than the layer
> above, and state the rule that follows.

## 9. Common mistakes

1. **Writing $Z = E/B$.** That ratio is a speed, $v$ or $c$, in m/s. The
   impedance uses $\mathbf H = \mathbf B/\mu$.
2. **Reporting a phase without stating the time convention.** With $e^{+i\omega t}$
   the half-space impedance is $\propto(1+i)$ and the phase is $+45°$; with
   $e^{-i\omega t}$ it is $-45°$. Both conventions appear in the MT literature;
   state yours, and remember that $\rho_a$ is convention-independent.
3. **Using the lossless velocity inside a conductor.** In the diffusive limit
   there is no meaningful phase velocity; the relevant length is the skin depth.
4. **Assuming a single scalar impedance for a 3-D Earth.** The response is a
   tensor (11), and the scalar $Z_{xy}$ is a derived, orientation-dependent
   quantity.
5. **Assuming the plane-wave source.** MT's cancellation of source strength is
   exact only for a laterally uniform incident field; near the auroral
   electrojet or at the coastline the assumption fails systematically.
6. **Treating $\rho_a = |Z|^2/(\omega\mu_0)$ as "the resistivity".** It is the
   resistivity of the uniform half-space *equivalent* to the measurement, and it
   can lie outside the range of any actual layer in the section.
7. **Using $\eta_0 = 377$ Ω to four-digit precision and then reporting
   resistivities to four digits.** The approximation is fine; the inconsistent
   precision is not.
8. **Confusing the reflection coefficient for the electric field with that for
   the energy.** $|r|^2$ is the energy reflection coefficient only at normal
   incidence in a lossless medium.

## 10. Real-world applications

- **Magnetotellurics and geomagnetic depth sounding.** Section 3 in full; the
  standard tool for crustal and mantle conductivity
  ([09 Electrical and EM Methods](../../09-electrical-em-methods/README.md)).
- **Controlled-source EM and induction logging.** The same impedance formalism
  with a known source; the source no longer cancels, so geometry must be modelled
  exactly.
- **Ground-penetrating radar.** Equations (14)–(15) give the reflection
  coefficients, and the impedance contrast between dry and wet soil is the
  dominant signal in most near-surface surveys
  ([10 GPR and Near-Surface](../../10-gpr-near-surface/README.md)).
- **Antenna design and calibration.** An antenna is matched to the impedance of
  its medium; the ratio in equation (4) is what "50 Ω" refers to in radio
  engineering.
- **Radio propagation and remote sensing.** The same plane-wave impedance controls
  reflection at the sea surface, ice and the ionosphere.
- **Fibre-optic and DAS sensing.** Although mechanical, the electromagnetic
  impedance language recurs in the electro-optic modulators used to interrogate
  fibre sensors ([02-10-05 Fibre-Optic Sensing](../10-optics-and-photometry/05-fiber-optics-sensing.md)).

## 11. Further reading

- **Griffiths, D. J. *Introduction to Electrodynamics* (4th ed., Cambridge
  University Press, 2017).** Chapter 9 derives plane waves, impedance,
  polarisation and reflection at normal incidence, with the same notation used
  here. Level: intermediate.
- **Jackson, J. D. *Classical Electrodynamics* (3rd ed., Wiley, 1999).** §7.3–7.9
  for waves in conducting media, the complex impedance, and oblique incidence.
  Level: graduate.
- **Simpson, F., & Bahr, K. *Practical Magnetotellurics* (Cambridge University
  Press, 2005).** The definitive account of the impedance tensor (11), its
  decomposition and the practical treatment of polarisation and noise. Level:
  advanced.
- **Chave, A. D., & Jones, A. G. (eds) *The Magnetotelluric Method: Theory and
  Practice* (Cambridge University Press, 2012).** The plane-wave assumption, its
  failure modes, and modern estimation practice. Level: graduate.
- **Daniels, D. J. *Ground Penetrating Radar* (2nd ed., IET, 2004).** Reflection
  coefficients and antenna–ground coupling in the wave regime. Level: advanced.
- **Balanis, C. A. *Advanced Engineering Electromagnetics* (2nd ed., Wiley,
  2012).** The engineering treatment of wave impedance, polarisation and
  scattering, with the antenna-design viewpoint. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [03 Maxwell's Equations and Their Physical Meaning](./03-maxwell-equations.md)
  — where the wave equation and the Helmholtz relation come from.
- [06 EM Fields in Conductors: Skin Depth and Diffusion](./06-em-in-conductors.md)
  — the diffusive limit of the impedance in detail, and the origin of the 45° phase.
- [04 Faraday's Law, Induction and Eddy Currents](./04-em-induction.md) — the
  physical mechanism that makes the impedance depend on conductivity.
- [02-03-04 Wave Basics](../03-oscillations-and-waves/04-wave-basics.md) —
  wavelength, phase velocity and polarisation in the mechanical setting.
- [02-03-08 Reflection and Refraction](../03-oscillations-and-waves/08-reflection-refraction.md)
  — the impedance-based reflection coefficient in its general form.
- [26-02-03 Physical Constants and Earth Parameters with Sources](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — $\mu_0$, $\varepsilon_0$ and $c$ with their provenance.

Exercises:
[`exercises/05-em-waves-exercises.md`](./exercises/05-em-waves-exercises.md)
and
[`exercises/05-em-waves-solutions.md`](./exercises/05-em-waves-solutions.md).

## Self-assessment checklist

Work through this without notes. Every item should be a clear "yes".

- [ ] I can derive the plane-wave solution and prove both fields are transverse.
      (Section 1)
- [ ] I can derive $\mathbf B = \mathbf k\times\mathbf E/\omega$ and explain what
      it implies for the relative orientation of the fields. (Section 1)
- [ ] I can define the wave impedance, verify $\eta_0 = \mu_0c$, and check its
      dimensions from first principles. (Section 2)
- [ ] I can state the complex impedance of a lossy medium and its two limits.
      (Section 2)
- [ ] I can explain why MT measures $E/H$, why the source cancels, and what the
      plane-wave assumption costs. (Section 3)
- [ ] I can derive $\rho_a = |Z|^2/(\omega\mu_0)$ and show it is exact for a
      half-space, with a 45° phase. (Section 3)
- [ ] I can write the impedance tensor and say what breaks 1-D symmetry.
      (Section 3)
- [ ] I can compute Stokes parameters and classify a polarisation state.
      (Section 4)
- [ ] I can compute a normal-incidence reflection coefficient from an impedance
      mismatch and use it for a GPR contrast. (Section 5)
- [ ] I can explain the difference between $E/H$ and $E/B$ and give the units of
      each. (Section 7)
