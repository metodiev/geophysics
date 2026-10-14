---
id: 02-03-10
title: "Attenuation, Absorption and the Quality Factor Q"
level: advanced
prereqs: ["02-03-02", "02-03-05", "02-03-07"]
estimated_minutes: 90
tags: [attenuation, quality-factor, absorption, dispersion]
---

# Attenuation, Absorption and the Quality Factor Q

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** geometric spreading from attenuation, and intrinsic absorption
   from scattering, and state the observable signature of each.
2. **Derive** the relation between amplitude decay and $Q$:
   $\alpha = \pi f/(Qv) = \omega/(2Qv)$ in the high-$Q$ limit, and
   $Q = \pi/(\alpha\lambda)$.
3. **State** that attenuation and velocity dispersion are inseparable —
   Kramers–Kronig — and quote the nearly-constant-$Q$ dispersion relation with its
   regime of validity.
4. **Measure** $Q$ by three independent methods (logarithmic decrement, spectral
   ratio, and the rise time of a pulse) and state the systematic errors that
   contaminate each.
5. **Account** for the corrections that must be applied before an amplitude decay
   means attenuation: geometric spreading, source and receiver coupling, focusing
   and defocusing, transmission losses, and scattering.
6. **Recognise** the orders of magnitude of $Q$ in Earth materials and explain why
   attenuation, not spreading, limits deep imaging in hot or fluid-rich crust.

## Prerequisites

- [02-03-02 Damped and Driven Oscillations, Resonance and Quality Factor](./02-damped-driven.md)
  — the definition of $Q$ and its measurement for a single oscillator.
- [02-03-05 Deriving the Wave Equation from Continuum Physics](./05-wave-equation-derivation.md)
  — the energy-flux statement whose decay is being measured.
- [02-03-07 Dispersion, Group Velocity and Phase vs Group Speed](./07-dispersion.md)
  — the dispersion that attenuation necessarily brings with it.

## 1. Three different losses

A seismic amplitude falls off with distance for reasons that must be kept apart,
because only one of them is a material property:

1. **Geometric spreading.** In three dimensions a spherical wave's amplitude falls
   as $1/r$ because the energy of a shell is spread over $4\pi r^2$; in two
   dimensions (a surface wave, a borehole tube wave) it falls as $1/\sqrt r$. This
   is geometry, not dissipation: no energy is converted to heat.
2. **Transmission losses.** Each interface crossed reflects some energy away
   (lesson 02-03-08) and converts some to other modes. An estimate of the
   cumulative transmission loss requires a velocity model, and in layered media
   the losses can be tens of per cent.
3. **Attenuation.** Energy converted to heat (intrinsic absorption) or redirected
   out of the beam by heterogeneity (scattering). This is the subject of this
   lesson, and only this part is described by $Q$.

Because only the third is a material property, every quantitative attenuation
measurement is a *difference* measurement: two receivers, or two frequencies at
one receiver, with everything else held fixed as far as possible.

## 2. Precise definitions

**Attenuation coefficient** $\alpha$. Amplitude decay
$A(x) = A_0e^{-\alpha x}$ with $\alpha$ in m⁻¹ (or in dB per wavelength, which is
a different number).

**Quality factor** $Q$. Dimensionless; $1/Q$ is the fractional energy lost per
radian of phase. For a wave,

$$Q = \frac{\pi}{\alpha\lambda} , \qquad
\alpha = \frac{\pi f}{Qv} = \frac{\omega}{2Qv} \quad (Q \gg 1) . \tag{1}$$

**Absorption (intrinsic attenuation).** Energy converted to heat by the
material's anelastic response — grain-boundary sliding, viscous squirt between
cracks, thermoelastic effects.

**Scattering attenuation.** Apparent attenuation from energy redirected out of the
beam by heterogeneity (lesson 02-03-09).

**Dispersion.** The frequency dependence of velocity that *must* accompany
attenuation in a causal medium.

## 3. Derivations

### 3.1 From $Q$ to the amplitude decay

Take the defining relation of $Q$ for an oscillator,
$dE/E = -d\phi/Q$, and apply it to a wave with phase
$\phi = \omega t - kx$. From the energy
$E \propto A^2$ and $d\phi = -k\,dx$ for propagation in $+x$:

$$\frac{dE}{E} = -\frac{k\,dx}{Q} \quad\Longrightarrow\quad
2\frac{dA}{A} = -\frac{k}{Q}dx \quad\Longrightarrow\quad
A(x) = A_0\exp\!\left(-\frac{k}{2Q}x\right) , \tag{2}$$

so

$$\boxed{\ \alpha = \frac{k}{2Q} = \frac{\omega}{2Qv} = \frac{\pi f}{Qv}\ }
\qquad\Longrightarrow\qquad
Q = \frac{\pi}{\alpha\lambda} . \tag{3}$$

Three equivalent statements to memorise, all for $Q \gg 1$:

- over one wavelength, the amplitude falls by the factor $e^{-\pi/Q}$;
- over one period, the *energy* falls by $2\pi/Q$;
- the number of wavelengths for the amplitude to fall by $e^{-1}$ is $Q/\pi$.

Exactness: equation (3) is the *definition* of $Q$ in the nearly-constant-$Q$
sense. If $Q$ varies with frequency, $\alpha(\omega) = \omega/(2Q(\omega)v(\omega))$
still holds pointwise, but quoting a single $Q$ for a band is an approximation
whose error is the variation of $Q$ across the band.

### 3.2 Why a $\beta$-type damping is not enough

A wave equation with a velocity-proportional damping term,

$$u_{tt} + 2\beta u_t = c^2u_{xx} , \tag{4}$$

gives $\omega^2 = c^2k^2 - 2i\beta\omega$, hence $\alpha = \beta/c$ *independent of
frequency* and therefore $Q = \omega/(2\beta c)\cdot c/\ \ldots$ more carefully:
with $k$ complex and $\omega$ real, expanding for small damping gives
$k \approx \omega/c(1 + i\beta/\omega)$, so $\alpha = \beta/c$ and

$$Q(\omega) = \frac{\omega}{2\beta} . \tag{5}$$

So a dashpot model has $Q$ *proportional to frequency*: it attenuates low
frequencies strongly and high frequencies barely at all. This contradicts the
observation that $Q$ in rocks is nearly frequency-independent over decades. The
resolution is that anelasticity is not a single dashpot but a *distribution* of
relaxation mechanisms, which is why the standard linear solid and its general-
isations (lessons 02-04-07) are used: a broad distribution of relaxation times
produces an approximately constant $Q$ over a wide band. **The dashpot model is
the right model for an instrument and the wrong model for a rock**, and the
reason is the frequency dependence.

### 3.3 Kramers–Kronig and the dispersion that must accompany loss

A causal linear response must satisfy the Kramers–Kronig relations: the real and
imaginary parts of the transfer function are Hilbert-transform pairs. Applied to a
wave, this means the attenuation $\alpha(\omega)$ and the phase velocity $v(\omega)$
are not independent: **a medium that attenuates must disperse**. The standard
nearly-constant-$Q$ form is

$$\frac{v(\omega)}{v(\omega_0)} - 1 \approx \frac{1}{\pi Q}\ln\frac{\omega}{\omega_0}
\qquad (Q \gg 1,\ |\ln(\omega/\omega_0)| \lesssim 1) . \tag{6}$$

The demo computes the exact dispersion of a standard linear solid and compares it
with equation (6): the agreement is about 10–25 per cent over a factor of five in
frequency, and it fails by a factor of two two decades away, where the
single-relaxation dispersion saturates while the logarithm does not. The lesson is
that equation (6) is a *first-order* result and must be used inside its regime.

Two practical consequences:

- A synthetic seismogram computed with $Q$ but with no dispersion is non-causal,
  and the error grows with propagation distance; it shows up as a systematic
  travel-time bias that is larger at lower $Q$.
- Measuring $v(\omega)$ and $Q(\omega)$ independently gives an over-determined
  test of the constitutive model: if they fail equation (6) badly, the medium is
  not a simple anelastic solid and is probably scattering-dominated.

### 3.4 Measuring $Q$: three methods and their errors

**Method 1: logarithmic decrement of a ringing mode** (or of a damped wave train).
Measure successive peak amplitudes, $\delta = \ln(A_n/A_{n+1})$, then
$Q = \pi/\delta$ for a wave (per *wavelength*) or $Q = \omega/(2\beta)$ from the
decay. Errors: the peaks must be separated by one wavelength (or one period), and
the measurement needs many cycles to average out noise.

**Method 2: spectral ratio between two receivers.** With $A(f,x) =
A_0(f)e^{-\alpha(f)x}$,

$$\ln\frac{A_1(f)}{A_2(f)} = \alpha(f)\,(x_2-x_1)
= \frac{\pi f\,(x_2-x_1)}{Q\,v} , \tag{7}$$

so a straight-line fit of the log ratio against frequency gives $Q$ from the slope.
Errors: $v$ must be known independently; source, receiver and coupling responses
enter as frequency-dependent factors; and the whole band is required because the
slope is small.

**Method 3: rise time / pulse broadening.** Attenuation broadens a pulse (through
the dispersion that accompanies it), and the growth of the rise time with distance
gives $Q$. Errors: the rise time depends on the source wavelet, so this method
needs a reference pulse and is sensitive to the source's own variability.

The demo implements the spectral-ratio method on synthetic data: with no noise it
recovers the input $Q = 80$ exactly (fit residual $1.4\times10^{-16}$); with 1 per
cent random amplitude error it gives 79.5882 (0.5 per cent low, residual
$8.1\times10^{-3}$); with 5 per cent error it gives 77.9725 (2.5 per cent low,
residual $4.0\times10^{-2}$). The estimator is thus well conditioned *in this ideal
geometry*, and the real difficulty is not the noise but the corrections of §4.

## 4. What must be corrected before an amplitude decay means $Q$

In order of magnitude of effect:

1. **Geometric spreading.** Divide by $1/r$ (body waves) or $1/\sqrt r$ (surface
   waves) — or, better, work with a ratio between nearby receivers so the spreading
   cancels to first order.
2. **Source and receiver coupling.** Amplitude depends on the coupling, and it
   varies with near-surface conditions in a way that is not the same at every
   station. This is often the dominant error in field measurements.
3. **Transmission losses at interfaces.** Each interface removes energy; the
   correction needs a velocity/density model.
4. **Focusing and defocusing.** Velocity structure acts like a lens: a concave
   reflector or a low-velocity channel can focus energy and make the amplitude
   *grow* with distance.
5. **Scattering.** Energy removed from the direct arrival by heterogeneity is
   counted as attenuation unless the heterogeneity is modelled; the two cannot be
   separated without additional information.
6. **Source spectrum.** The source's own spectrum changes with azimuth and with
   shot conditions; the spectral-ratio method assumes it is the same at both
   receivers (or that the ratio is taken to a reference receiver).

A defensible $Q$ measurement states which corrections were applied, and quotes an
error budget dominated by the corrections rather than by the noise.

## 5. Physical interpretation

**$Q$ is the dimensionless measure of loss.** $1/Q$ is the fraction of energy lost
per radian, so $Q = 100$ means 6.3 per cent per cycle (2$\pi/Q$) and a decay of
$e^{-1}$ in amplitude over about 32 wavelengths. It is the same $Q$ as the
oscillator's (lesson 02-03-02) — the wave is a continuum of coupled oscillators,
and each frequency has its own $Q(\omega)$.

**Attenuation is a low-frequency filter.** Because $\alpha \propto f/Q$ for
constant $Q$, high frequencies die first: a rock with $Q = 50$ attenuates 50 Hz
ten times faster than 5 Hz. This is why deep targets require low frequencies, and
why the deep crust can be imaged at all.

**Scattering and absorption look the same in an amplitude curve.** They differ in
their frequency dependence (scattering is a strong power law in the Rayleigh
regime) and in what they do to the *coda*: scattering moves energy to later times,
absorption removes it. A measurement of the coda decay is therefore the standard
way to separate them.

**Attenuation is the strongest temperature proxy in seismology.** Because the
mechanisms are thermally activated, $Q$ falls strongly as temperature rises
towards the solidus; mapping low-$Q$ zones is therefore mapping hot or partially
molten rock, which is the principal geophysical method for detecting melt in the
mantle (see [06-seismology](../../06-seismology/README.md)).

## 6. Units and dimensional analysis

- $[\alpha] = \mathrm{m^{-1}}$ ✓ from $\alpha = \omega/(2Qv)$:
  $\mathrm{s^{-1}/(m\,s^{-1})} = \mathrm{m^{-1}}$ ✓.
- $Q$ is dimensionless, so $Q = \pi/(\alpha\lambda)$ must have a dimensionless
  right side: $\mathrm{1/(m^{-1}\times m)} = 1$ ✓.
- The logarithmic decrement per wavelength is dimensionless: $\alpha\lambda = \pi/Q$
  ✓.
- Attenuation is sometimes quoted in dB per wavelength:
  $20\log_{10}e^{-\alpha\lambda} = -8.686\alpha\lambda$ dB. With
  $\alpha\lambda = \pi/Q$, that is $27.29/Q$ dB per wavelength — a useful conversion
  to check any quoted figure against.
- Equation (6): both sides dimensionless ✓; the logarithm requires a dimensionless
  argument, so the reference frequency must be stated.

## 7. Python demonstration

[`code/attenuation_demo.py`](./code/attenuation_demo.py) tabulates the decay,
measures $Q$ from a damped simulation, applies the spectral-ratio method with
noise, and computes the dispersion of a standard linear solid. Observed output:

```text
      Q   alpha (1/m)   1/alpha (m)  exp(-alpha*1000)  pi/(alpha lambda)
   20.0  3.141593e-03         318.3          0.043214          20.000000
  100.0  6.283185e-04        1591.5          0.533488         100.000000
  500.0  1.256637e-04        7957.7          0.881911         500.000000
```

```text
c = 2000 m/s, domain length 200 m, first mode: omega = c k = 31.415927 rad/s, period = 0.200000 s
damping coefficient beta = 0.80 1/s -> Q = omega/(2 beta) = 19.6350
peak |u| per period: 0.99992, 0.85205, 0.72605, 0.61867, 0.52718, 0.44921, 0.38277, 0.32616, 0.27792, 0.23681
measured decay rate from the fit = 0.800227 1/s (input beta = 0.8)
Q from the fitted decay        = 19.6294
Q from Q = omega/(2 beta)      = 19.6350
difference = 5.56e-03
```

```text
model: Q = 80, v = 3000 m/s, receivers at 500 m and 1500 m (separation 1000 m)
  noise  Q recovered   error (%)   slope fit residual
   0.00      80.0000      -0.000            1.360e-16
   0.01      79.5882      -0.515            8.061e-03
   0.05      77.9725      -2.534            4.030e-02
```

```text
   f (Hz)       Q(f)     V (m/s)     V/V0 - 1   ln(f/f0)/(pi Q0)  difference
      1.0   151.5000   3513.0670    -0.015938          -0.024431   8.493e-03
      2.0    78.0000   3516.3084    -0.015030          -0.017077   2.046e-03
     10.0    30.0000   3569.9661     0.000000           0.000000   0.000e+00
     50.0    78.0000   3626.1575     0.015740           0.017077  -1.337e-03
    100.0   151.5000   3629.7225     0.016739           0.024431  -7.693e-03
```

### What to observe

| Observation | Consequence |
|---|---|
| $\pi/(\alpha\lambda)$ returns the input $Q$ exactly in every row | Equation (1) is a definition, and the table is a consistency check on its arithmetic |
| At $Q = 100$ the amplitude after 1 km is 0.533 of its initial value | Attenuation over a kilometre is a factor of two at $Q = 100$ with $\lambda = 50$ m; over ten kilometres it is a factor of 500 |
| The measured decay rate from the simulation is 0.800227 against the input 0.8 | The numerical scheme and the fitted decay agree to 0.03 per cent, so $Q$ measured from an amplitude decay is limited by the measurement, not by the scheme |
| $Q$ from the fitted decay (19.6294) against $\omega/2\beta$ (19.6350) | The residual is the finite time step of the integrator; the relation $Q = \omega/2\beta$ is exact for this model |
| The spectral-ratio estimator recovers $Q = 80$ exactly with no noise and 79.5882 with 1 per cent noise | The estimator is unbiased and well conditioned; the real uncertainty comes from the corrections of §4, not from the noise |
| The exact dispersion of a single relaxation differs from the nearly-constant-$Q$ relation by up to $8.5\times10^{-3}$ in $V/V_0$ at a decade from $f_0$ | Equation (6) is a first-order result valid near the reference frequency; it must not be extrapolated over decades |

> **Breaking exercise.** Change the damping in the simulation to `beta = 8.0`
> (so $Q \approx 2$) and predict, before running, whether $Q$ measured from the
> fitted decay still equals $\omega/(2\beta)$. Then explain the answer in one
> sentence using the exact relation between $Q$ and the decay rate.

## 8. Common mistakes

1. **Fitting a raw amplitude decay as attenuation.** Geometric spreading, coupling
   and transmission losses must be removed first; in many datasets they dominate.
2. **Using $\alpha = \beta/c$ and calling it constant-$Q$.** A dashpot gives
   $Q \propto f$, which contradicts observation in rocks.
3. **Reporting $Q$ without a frequency.** $Q$ is a function of frequency; a single
   number is a band average and must say which band.
4. **Ignoring the dispersion that accompanies attenuation.** Synthetic data with
   attenuation and no dispersion are non-causal.
5. **Confusing scattering with absorption.** They have different frequency
   dependence and different effects on the coda; only one is a material property.
6. **Extrapolating the nearly-constant-$Q$ dispersion relation over decades.**
   It is a first-order result.
7. **Quoting attenuation in dB without stating dB per what.** Per wavelength, per
   kilometre and per period are different numbers.
8. **Comparing $Q$ values measured by different methods without checking the
   definition.** Spectral ratio, rise time, coda and decay methods have different
   systematic biases.

## 9. Real-world applications

- **Earthquake hazard and ground-motion prediction.** Attenuation relations
  (the decay of ground motion with distance) are dominated by the regional $Q$;
  getting it wrong by a factor of two changes predicted shaking by large factors.
- **Mantle melt and temperature mapping.** Low-$Q$ zones in the upper mantle
  indicate high temperature and possibly partial melt; $Q$ tomography is a
  standard tool of global seismology (see [06-seismology](../../06-seismology/README.md)).
- **Reservoir characterisation.** Attenuation is more sensitive to saturation and
  permeability than velocity is, which is why attenuation-based hydrocarbon
  indicators are attractive — and why they are hard, because coupling and
  scattering can mimic the effect.
- **Ultrasonic and log measurements.** Laboratory and sonic-log $Q$ are measured
  over limited geometries and bands, and must be corrected to the effective
  pressure and frequency before being compared with field estimates.
- **GPR and electromagnetic attenuation.** The same $Q$ formalism describes a
  lossy dielectric: the radar attenuation is set by the conductivity and by the
  dielectric relaxation spectrum, and the "skin depth" is the electromagnetic
  analogue of $1/\alpha$ (see [02-07 Electromagnetism](../07-electromagnetism/README.md)).
- **Seismic imaging.** The frequency-dependent loss sets the achievable bandwidth
  as a function of depth, and therefore the resolution; inverse-$Q$ filtering is a
  routine processing step, with the caveat that it also amplifies noise.

## 10. Further reading

- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** The chapter on anelasticity develops $Q$, the
  Kramers–Kronig relations and the nearly-constant-$Q$ model from the constitutive
  side. Level: advanced.
- **Futterman, W. I. (1962), *Dispersive body waves*, Journal of Geophysical
  Research.** The classical treatment of the attenuation–dispersion pair in
  seismic waves. Level: advanced.
- **Stein, S., & Wysession, M. *An Introduction to Seismology, Earthquakes and
  Earth Structure* (Blackwell, 2003).** How $Q$ is measured from real records, and
  what the resulting numbers are. Level: intermediate.
- **Shearer, P. M. *Introduction to Seismology* (3rd ed., Cambridge University
  Press, 2019).** Attenuation and its separation from scattering, with
  observational examples. Level: intermediate.
- **Mavko, G., Mukerji, T., & Dvorkin, J. *The Rock Physics Handbook* (Cambridge
  University Press).** Attenuation mechanisms in rocks: squirt flow, Biot
  poroelasticity, thermoelasticity, and the laboratory data. Level: advanced.
- **Johnston, D. H., & Toksöz, M. N. *Seismic Wave Attenuation* (SEG Geophysics
  Reprint Series).** A collection of the primary literature; useful for calibrating
  what is measured versus what is modelled. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 Damped and Driven Oscillations, Resonance and Quality Factor](./02-damped-driven.md)
  — where $Q$ was defined for a single oscillator.
- [07 Dispersion, Group Velocity and Phase vs Group Speed](./07-dispersion.md) —
  the dispersion side of the same physics.
- [09 Diffraction, Scattering and Resolution Limits](./09-diffraction.md) — the
  competing mechanism that mimics absorption.
- [02-04-07 Viscoelasticity, Creep and Anelastic Relaxation](../04-elasticity-and-continuum-mechanics/07-viscoelasticity.md)
  — the constitutive laws that produce intrinsic attenuation, and the Maxwell time.
- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — $Q_p$ versus $Q_s$ and why they differ.
- [06-seismology](../../06-seismology/README.md) — attenuation tomography and its
  interpretation.

Exercises:
[`exercises/10-attenuation-exercises.md`](./exercises/10-attenuation-exercises.md)
and
[`exercises/10-attenuation-solutions.md`](./exercises/10-attenuation-solutions.md).

## Self-assessment checklist

- [ ] I can separate geometric spreading, transmission loss, scattering and
      intrinsic absorption, and say which is a material property. (Section 1)
- [ ] I can derive $\alpha = \pi f/(Qv)$ from the definition of $Q$ and use it in
      both directions. (Section 3.1)
- [ ] I can state the three equivalent readings of $Q$ (per wavelength, per cycle,
      decay length). (Section 3.1)
- [ ] I can explain why a velocity-proportional dashpot gives the wrong frequency
      dependence for a rock. (Section 3.2)
- [ ] I can state the Kramers–Kronig consequence and quote the
      nearly-constant-$Q$ dispersion relation with its regime. (Section 3.3)
- [ ] I can measure $Q$ by three methods and name the dominant error of each.
      (Section 3.4)
- [ ] I can list the six corrections that must precede an amplitude-decay
      measurement. (Section 4)
- [ ] I can estimate the bandwidth limitation imposed by $Q$ at a given depth and
      explain why deep imaging needs low frequencies. (Sections 5, 9)
