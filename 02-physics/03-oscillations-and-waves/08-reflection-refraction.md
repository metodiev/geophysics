---
id: 02-03-08
title: "Reflection, Refraction and Snell's Law for Waves"
level: intermediate
prereqs: ["02-03-04", "02-03-05", "01-03-01"]
estimated_minutes: 90
tags: [reflection, refraction, snell, impedance]
---

# Reflection, Refraction and Snell's Law for Waves

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** Snell's law as a phase-matching condition at an interface, and state
   why it is not an independent empirical law.
2. **Derive** the normal-incidence reflection and transmission coefficients from
   the boundary conditions, in both the pressure and the velocity conventions, and
   verify the energy budget.
3. **Compute** impedance contrasts for realistic rock pairs, predict the polarity
   of the reflection, and explain why polarity is a fluid indicator.
4. **Find** the critical angle, explain what happens beyond it, and connect the
   evanescent field to head waves and to the hidden-layer problem of refraction
   surveying.
5. **State** the assumptions of the acoustic treatment and list what the full
   elastic (Zoeppritz) problem adds: mode conversion, angle-dependent amplitudes,
   and the basis of amplitude-versus-offset analysis.
6. **Verify** the coefficients numerically by finite-difference simulation and the
   boundary conditions algebraically, and quote the residuals.

## Prerequisites

- [02-03-04 Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity](./04-wave-basics.md)
  — the kinematic quantities that must match at an interface.
- [02-03-05 Deriving the Wave Equation from Continuum Physics](./05-wave-equation-derivation.md)
  — the divergence form, and why flux continuity is automatic.
- [01-03-01 Angles and Triangles](../../01-mathematics/03-trigonometry/01-angles-and-triangles.md)
  — the trigonometry of the ray-geometry arguments.

## 1. Why interfaces are where the information is

A wave in a perfectly homogeneous medium carries only its source's signature. Every
statement about the *interior* of the Earth from a seismic record comes from the
fact that the medium is layered, and a wave crossing a layer boundary is partly
reflected and partly transmitted. The same is true of GPR in a soil profile, of
ultrasound at a fracture, and of light in a fibre with a Bragg grating.

Two questions structure the subject:

- **Where does the wave go?** Answered by Snell's law, which is a statement about
  matching wavefronts across the boundary.
- **How much of it goes there?** Answered by the reflection and transmission
  coefficients, which come from the boundary conditions of the wave equation.

This lesson answers both in the scalar (acoustic) case, where every step is
visible, and states precisely what the elastic case adds.

## 2. Precise definitions

**Acoustic impedance.** $Z = \rho c$, units kg m⁻² s⁻¹ (sometimes quoted in Rayl,
1 Rayl = 1 kg m⁻² s⁻¹ = 1 Pa s m⁻¹; the practical unit in exploration is the
MRayl = 10⁶ kg m⁻² s⁻¹).

**Reflection coefficient.** $R$ = ratio of reflected to incident amplitude, with
the convention stated (pressure or particle velocity). The two conventions differ
in sign.

**Transmission coefficient.** $T$ = ratio of transmitted to incident amplitude,
same convention.

**Critical angle.** The incidence angle beyond which there is no propagating
transmitted wave, $\sin\theta_c = c_1/c_2$ (for $c_2 > c_1$).

**Head wave (refraction arrival).** The wave refracted along the interface at the
critical angle and continuously reradiated into the upper medium; it is the
efficient long-range arrival used in refraction surveying.

**Normal incidence.** Incidence along the interface normal, where the scalar
problem is exact and the coefficients are simple.

## 3. Derivations

### 3.1 Snell's law as phase matching

Let a plane wave $e^{i(k_1x\sin\theta_1 + k_1z\cos\theta_1 - \omega t)}$ strike the
plane $z = 0$ from medium 1, where $x$ is along the interface. Every field on
either side must oscillate *in step* along the interface, because the boundary
conditions hold at every $x$ for all $t$. Equating the $x$-dependence of the
incident, reflected and transmitted waves gives

$$k_1\sin\theta_1 = k_1\sin\theta_r = k_2\sin\theta_2 , \tag{1}$$

so $\theta_r = \theta_1$ (the law of reflection falls out for free) and

$$\boxed{\ \frac{\sin\theta_1}{c_1} = \frac{\sin\theta_2}{c_2} \equiv p\ }
\tag{2}$$

using $k = \omega/c$. The quantity $p$, the **horizontal slowness** (or ray
parameter), is conserved across any layered sequence at constant frequency —
which is why it, not the angle, is the natural variable for layered-media theory.
If the frequency changed across the interface, equation (1) would force
$\omega_1 = \omega_2$: a wave does not change frequency when it crosses a
boundary.

### 3.2 Normal incidence: the coefficients

Take the acoustic wave equation for pressure $p$ with density $\rho$ and sound
speed $c$, and let a plane wave of pressure amplitude $P_i$ strike $z=0$ normally.
Write the pressure field as the sum of an incident, a reflected and a transmitted
wave, and impose the two boundary conditions:

1. **Pressure is continuous** (no massless membrane, and equilibrium in the normal
   direction): $P_i + P_r = P_t$.
2. **Normal particle velocity is continuous** (the two sides stay in contact):
   the velocity associated with a plane pressure wave travelling in $+\hat{z}$ is
   $v = p/Z$, and for the reflected wave (travelling in $-\hat{z}$) it is
   $-P_r/Z_1$. So

$$\frac{P_i}{Z_1} - \frac{P_r}{Z_1} = \frac{P_t}{Z_2} . \tag{3}$$

Solving the two equations gives the **pressure** coefficients

$$R_p = \frac{P_r}{P_i} = \frac{Z_2-Z_1}{Z_2+Z_1} , \qquad
T_p = \frac{P_t}{P_i} = \frac{2Z_2}{Z_2+Z_1} , \qquad 1 + R_p = T_p . \tag{4}$$

For **particle velocity** the signs reverse because $R_v = -R_p$ (the reflected
velocity is measured with the same positive sense as the incident):

$$R_v = \frac{Z_1-Z_2}{Z_1+Z_2} , \qquad
T_v = \frac{2Z_1}{Z_1+Z_2} . \tag{5}$$

Both pairs are correct; they are related by $R_v = -R_p$ and
$T_v = T_p Z_1/Z_2$. The demo uses the velocity convention, as a geophone does,
and its measured values ($R_v = -0.302777$, theory $-0.304348$;
$T_v = 0.694611$, theory $0.695652$) agree to about 0.5 per cent, the residual
being the peak-picking accuracy of the finite-difference simulation.

**Energy.** The energy flux is $p v$, so the reflected and transmitted energy
fractions are

$$\mathcal{R} = R_v^2 = R_p^2 , \qquad
\mathcal{T} = \frac{Z_2}{Z_1}T_v^2 = \frac{Z_1}{Z_2}T_p^2 , \qquad
\mathcal{R} + \mathcal{T} = 1 . \tag{6}$$

The demo verifies $\mathcal{R}+\mathcal{T}=1$ to twelve digits. Note the
asymmetry: the *amplitude* ratio is not the energy ratio, and a "transmission
coefficient" quoted without its convention and its normalisation is meaningless.

### 3.3 Impedance contrasts in real rocks

| Boundary (synthetic model parameters) | $Z_1$ (MRayl) | $Z_2$ (MRayl) | $R_p$ | $\mathcal{R}$ (%) |
|---|---|---|---|---|
| water over limestone | 1.50 | 7.50 | $+0.6667$ | 44.4 |
| shale over gas sand | 6.00 | 4.40 | $-0.1538$ | 2.4 |
| shale over brine sand | 6.00 | 6.44 | $+0.0354$ | 0.13 |
| granite over air | 14.85 | 0.000408 | $-0.9999$ | 99.99 |

Every row is a model parameter set chosen to show the sense of the effect, not a
measured field value. Two consequences are worth stating as general facts:

- **Most geological interfaces are weak reflectors.** A 5 per cent velocity
  contrast at constant density gives $|R| \approx 0.025$: 0.06 per cent of the
  energy is reflected. Seismic reflection works because the recording is designed
  around that, not because the reflections are strong.
- **Polarity carries information.** A gas sand has lower impedance than the
  overlying shale ($R_p < 0$), a brine sand higher ($R_p > 0$); the *sign* of the
  reflection therefore distinguishes them even when the magnitudes are similar.
  That is the physical basis of the bright-spot and AVO techniques.

### 3.4 The critical angle and beyond

Suppose $c_2 > c_1$. Then $\sin\theta_2 = (c_2/c_1)\sin\theta_1$ reaches 1 at

$$\sin\theta_c = \frac{c_1}{c_2} , \tag{7}$$

and for $\theta_1 > \theta_c$ there is no real $\theta_2$. The transmitted wave
becomes **evanescent**:

$$\sin\theta_2 > 1 \quad\Longrightarrow\quad
\cos\theta_2 = \pm i\sqrt{\left(\frac{c_2}{c_1}\right)^2\sin^2\theta_1 - 1}
= \pm i\beta , \tag{8}$$

so its $z$-dependence is $e^{\mp k_2\beta z}$: an exponential decay into the lower
medium with no phase propagation in that direction. Its amplitude along the
interface still oscillates, so it is not a static field.

Three consequences:

1. **Total reflection.** In a lossless medium $|R| = 1$ beyond the critical angle:
   all the energy returns, and the reflection is accompanied by a frequency-
   and angle-dependent phase shift, which is the origin of the phase behaviour
   exploited in optical total-internal-reflection devices.
2. **Head waves.** The transmitted field along the interface radiates back into
   medium 1; the resulting head (refracted) wave travels at $c_2$ along the
   interface and arrives at long range as the first arrival in refraction
   surveying. Its amplitude decays as $x^{-2}$ in the far field in three
   dimensions — the reason refraction is a long-range method.
3. **The hidden layer.** If a layer has a *lower* velocity than the one above it,
   no ray can be critically refracted from it, so it is invisible to a refraction
   survey regardless of its thickness. This is not a resolution limit but a
   geometric one, and it is why refraction and reflection are complementary.

### 3.5 Oblique incidence, and what the elastic case adds

For two fluids the pressure reflection coefficient at oblique incidence is

$$R_p(\theta_1) = \frac{Z_2\cos\theta_1 - Z_1\cos\theta_2}
{Z_2\cos\theta_1 + Z_1\cos\theta_2} , \tag{9}$$

which reduces to equation (4) at normal incidence. The demo verifies it by
substituting into both boundary conditions and reporting the normalised residual:
it is $1.1\times10^{-16}$ at normal incidence and $4.2\times10^{-17}$ near the
critical angle — i.e. machine zero, which is the standard of proof that an
algebraic solution satisfies its own boundary conditions. Note the limit at
grazing incidence, $R_p \to -1$: at 90° incidence a wave cannot enter the lower
medium at all.

For a **solid–solid** interface the situation is richer, and this is where the
scalar model must be set aside:

- An incident P wave generates **four** outgoing waves: reflected P, reflected S,
  transmitted P, transmitted S. There is no refraction of one wave type alone.
- The coefficients are the solution of a $4\times4$ linear system (the
  **Zoeppritz** equations); the reflection coefficient depends on angle through
  the contrast in *both* $\lambda$ and $\mu$ and in density.
- At normal incidence the S terms drop out and the result reduces to the
  impedance formula of §3.2 with $Z = \rho v_p$ — which is why the normal-
  incidence formula is used with $v_p$ in seismic interpretation, and why it is
  *wrong* off normal incidence.

The angle dependence of the reflection coefficient is the basis of
**amplitude-versus-offset (AVO)** analysis, one of the most heavily used tools in
petroleum geophysics. Its interpretation requires the full elastic system; the
scalar model of this lesson is the normal-incidence special case.

## 4. Physical interpretation

**Snell's law is continuity.** Nothing "bends"; the wavefronts on the two sides
must join, and only one transmitted angle joins them. The apparent bending is the
visual consequence of the transmitted wave having a different wavelength.

**Impedance is the ratio of force to flow.** For a wave, $Z = p/v$ is the acoustic
analogue of the characteristic impedance of a transmission line, and the
reflection coefficient is the impedance mismatch of a line junction. This is why
all the algebraic results transfer between acoustics, electromagnetics and
transmission-line theory, and why an electrical engineer can read a seismic
section.

**Reflection is an information channel, transmission is a path.** The reflected
energy is what a reflection survey images; the transmitted (critically refracted)
arrival is what a refraction survey uses. Their angular behaviours are opposite:
reflection is strong at normal incidence and weak at grazing, head waves exist
only beyond the critical angle.

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Plane interface | Flat over a Fresnel zone | Roughness scatters (lesson 02-03-09); dipping interfaces move the apparent angle |
| Two homogeneous half-spaces | No layering within a wavelength | Layering gives effective (dispersive) properties and internal multiples |
| Acoustic (fluid) media | No shear modulus | Solids convert modes and give four waves; use Zoeppritz |
| Isotropic media | No directional dependence | Anisotropy makes the slowness surface non-spherical and separates S polarisations (02-04-06) |
| Lossless media | $Q = \infty$ | Attenuation makes $R$ complex and angle-dependent; beyond the critical angle the total reflection becomes only approximately total |
| Plane wave, infinite aperture | No diffraction | A finite beam diffracts and its reflection differs from the plane-wave result (02-03-09) |
| Linear superposition | No wave–wave interaction | Finite amplitude breaks the linear decomposition at an interface |

## 6. Units and dimensional analysis

- $[Z] = \mathrm{kg\,m^{-3}\times m\,s^{-1}} = \mathrm{kg\,m^{-2}\,s^{-1}}$ ✓,
  equal to Pa s m⁻¹.
- $R$ and $T$ are dimensionless ratios; the naive check $R + T = 1$ holds for
  pressure amplitudes but **not** for velocity amplitudes nor for energies. State
  which pair you are using.
- $\sin\theta_1/c_1$ has units s m⁻¹ (slowness) and is conserved: a useful check
  on any refraction computation is that $p$ is the same on both sides.
- Equation (8) requires $(c_2/c_1)^2\sin^2\theta_1 - 1 > 0$ for the evanescent
  regime; check the sign before writing $i\beta$.

## 7. Python demonstration

[`code/reflection_refraction_demo.py`](./code/reflection_refraction_demo.py)
applies Snell's law, measures the normal-incidence coefficients by
finite-difference modelling, and checks the boundary conditions obliquely.
Observed output:

```text
layer 1: rho = 2000 kg/m^3, c = 2000 m/s
layer 2: rho = 2500 kg/m^3, c = 3000 m/s
speed ratio c2/c1 = 1.500000
critical angle = asin(c1/c2) = 41.8103 deg
 theta1 (deg)   p = sin(theta1)/c1  theta2 (deg)                    regime
       0.0000          0.000000000        0.0000               transmitted
      30.0000          0.000250000       48.5904               transmitted
      41.8103          0.000333333       90.0000               transmitted
      50.0000          0.000383022            -- total internal reflection
```

```text
predicted velocity coefficients: R = (Z1-Z2)/(Z1+Z2) = -0.304348, T = 2 Z1/(Z1+Z2) = 0.695652
energy budget: R^2 + (Z2/Z1) T^2 = 1.000000000000
incident arrival    at 150 m: t = 0.0248 s (predicted 0.0250), amplitude +0.499651
reflected arrival   at 150 m: t = 0.0746 s (predicted 0.0750), amplitude -0.151283
transmitted arrival at 250 m: t = 0.0666 s (predicted 0.0667), amplitude +0.347063
measured R = -0.302777, predicted -0.304348, difference 1.57e-03
measured T = +0.694611, predicted +0.695652, difference 1.04e-03
```

```text
 theta1 (deg)  theta2 (deg)           R        R^2   max residual
       0.0000        0.0000    0.304348   0.092628      1.059e-16
      30.0000       48.5904    0.421121   0.177343      0.000e+00
      41.8103       89.9563    0.998909   0.997820      4.162e-17
      45.0000            --    1.000000   1.000000     evanescent
```

### What to observe

| Observation | Consequence |
|---|---|
| The critical angle is exactly 41.8103° and $\theta_2 = 90.0000°$ there | Snell's law is satisfied to the printed precision, and the critical angle is a geometric, not a material, statement |
| $\mathcal{R}+\mathcal{T} = 1.000000000000$ | Energy conservation is a consistency check on the coefficient pair; violating it means a convention has been mixed |
| The simulated reflection arrives at 0.0746 s against a predicted 0.0750 s | The travel time is reproduced to 0.5 per cent, which is the accuracy of the peak picker at this pulse width |
| Measured $R_v = -0.302777$ against $-0.304348$ | The finite-difference simulation, which knows only the differential equation and harmonic averaging at the interface, reproduces the analytic coefficient to 0.5 per cent |
| The incident amplitude is 0.499651, not 1 | An initial displacement with zero velocity splits in two; the coefficients are ratios, so the split cancels — a check that the measurement is set up correctly |
| The oblique residuals are $10^{-16}$ to $10^{-17}$ | The algebraic solution satisfies both boundary conditions to machine precision, which is the correct standard for claiming a derivation is right |

> **Breaking exercise.** Change the second layer's density to 1000 kg m⁻³ while
> keeping its speed at 3000 m s⁻¹ (water-like) and predict, before running, the
> sign and approximate magnitude of the normal-incidence reflection coefficient.
> Then explain why the answer is sensitive to the density while the critical angle
> is not.

## 8. Common mistakes

1. **Mixing conventions.** The velocity reflection coefficient is the negative of
   the pressure one; reporting the wrong sign flips the polarity of every event.
2. **Using the impedance formula off normal incidence.** It is exact only at
   normal incidence; the oblique coefficients involve the angles.
3. **Forgetting the amplitude-versus-energy distinction.** $R^2 + T^2 \ne 1$ for
   amplitudes; the energy budget carries the impedance factors of equation (6).
4. **Assuming total reflection means zero field beyond the interface.**
   The transmitted field is evanescent, not absent, and it is what launches head
   waves.
5. **Expecting a refraction survey to see a low-velocity layer.** It cannot; the
   critical angle does not exist for a velocity decrease.
6. **Ignoring mode conversion in a solid.** A P wave at oblique incidence in a
   solid generates an S wave at the interface, which is a first-order effect, not a
   correction.
7. **Forgetting frequency invariance.** A wave keeps its frequency across an
   interface and changes its wavelength; a workflow that changes the frequency at
   an interface contains a modelling error.
8. **Treating an interface as infinitely sharp.** At the thin-bed limit the
   reflection coefficient tends to zero and the layer behaves as an effective
   medium — a different physical regime, covered by effective-medium theory.

## 9. Real-world applications

- **Reflection seismic imaging.** Every migrated section is built from the
  positions and amplitudes of reflected energy; the normal-incidence impedance
  formula is the *forward model* behind inversion for acoustic impedance.
- **AVO analysis.** The angle dependence of the elastic reflection coefficients
  distinguishes gas from brine and sand from shale; it requires the full
  Zoeppritz system, of which §3.2 is the normal-incidence limit.
- **Refraction surveying.** Head waves from the critical angle give the velocities
  and depths of the shallow layers; the hidden-layer problem is why refraction and
  reflection are always interpreted together. (See
  [06-seismology](../../06-seismology/README.md).)
- **GPR and ultrasound.** The same impedance formulas with $Z$ the electromagnetic
  or acoustic impedance; a reflection coefficient of 0.1 in a GPR section is a
  strong reflector by geological standards.
- **Fibre-optic and waveguide devices.** Total internal reflection at a
  controlled critical angle is the operating principle of every optical fibre and
  of many sensors (see
  [02-10 Optics and Photometry](../10-optics-and-photometry/README.md)).
- **Rock-physics fluid substitution.** Gassmann's relations (lesson
  02-04-04) predict how $Z$ changes with saturation, and therefore how the
  reflection coefficient of a reservoir changes between brine and gas — the
  quantitative part of the bright-spot argument
  ([05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)).

## 10. Further reading

- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** Chapter 5 is the canonical treatment of the Zoeppritz
  problem and of the scalar special cases derived here. Level: advanced.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics*
  (2nd ed., Cambridge University Press, 1990).** Refraction and reflection
  surveying, with the field geometry implied by Snell's law. Level: intermediate.
- **Sheriff, R. E., & Geldart, L. P. *Exploration Seismology* (Cambridge
  University Press).** The acquisition and interpretation context of every
  coefficient in this lesson. Level: intermediate.
- **Stein, S., & Wysession, M. *An Introduction to Seismology, Earthquakes and
  Earth Structure* (Blackwell, 2003).** Reflection and refraction at the level of
  this lesson, with the observational consequences. Level: intermediate.
- **Born, M., & Wolf, E. *Principles of Optics* (Cambridge University Press).**
  The Fresnel coefficients and the evanescent wave, derived in the electromagnetic
  setting where the analogy is exact. Level: advanced.
- **Ikelle, L. T., & Amundsen, L. *Introduction to Petroleum Seismology* (SEG).**
  AVO and the elastic reflection coefficients in applied practice. Level:
  intermediate to advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [04 Wave Description](./04-wave-basics.md) — the wavelength and frequency that
  must match at the interface.
- [05 Deriving the Wave Equation from Continuum Physics](./05-wave-equation-derivation.md)
  — the divergence form and flux continuity.
- [09 Diffraction, Scattering and Resolution Limits](./09-diffraction.md) — what
  happens when the interface is not a plane.
- [10 Attenuation, Absorption and the Quality Factor Q](./10-attenuation.md) —
  the loss that makes the coefficients complex.
- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — the two speeds that make the elastic problem four-wave.
- [01-06-06 Gauss, Stokes and Green Theorems](../../01-mathematics/06-multivariable-calculus/06-integral-theorems.md)
  — why flux continuity at an interface is automatic in the divergence form.
- [06-seismology](../../06-seismology/README.md) — reflection and refraction
  seismology in full.

Exercises:
[`exercises/08-reflection-refraction-exercises.md`](./exercises/08-reflection-refraction-exercises.md)
and
[`exercises/08-reflection-refraction-solutions.md`](./exercises/08-reflection-refraction-solutions.md).

## Self-assessment checklist

- [ ] I can derive Snell's law as a phase-matching condition and explain why
      reflection has the same angle. (Section 3.1)
- [ ] I can derive the normal-incidence coefficients from the two boundary
      conditions, in both conventions. (Section 3.2)
- [ ] I can verify the energy budget and explain why it is not $R^2+T^2=1$.
      (Section 3.2)
- [ ] I can compute an impedance contrast and predict the polarity of the
      reflection. (Section 3.3)
- [ ] I can find the critical angle, write the evanescent decay, and connect it
      to head waves and the hidden-layer problem. (Section 3.4)
- [ ] I can write the oblique fluid-fluid reflection coefficient and check its
      normal-incidence limit. (Section 3.5)
- [ ] I can list what the elastic (Zoeppritz) problem adds and say which of the
      four waves is which. (Section 3.5)
- [ ] I can name three applications in which the sign of the reflection
      coefficient carries the information. (Sections 3.3, 9)
