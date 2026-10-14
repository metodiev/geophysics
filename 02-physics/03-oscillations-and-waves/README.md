# Module 02-03 — Oscillations and Waves

**Stages:** beginner → advanced · **Prerequisites:**
[02-01 Measurement, Units and Physical Reasoning](../01-measurement-and-physical-reasoning/README.md),
[02-02 Classical Mechanics](../02-classical-mechanics/README.md),
[01-03 Trigonometry](../../01-mathematics/03-trigonometry/README.md) (phase and
harmonics), [01-05 Single-Variable Calculus](../../01-mathematics/05-single-variable-calculus/README.md)
(Taylor expansion), [01-06 Multivariable and Vector Calculus](../../01-mathematics/06-multivariable-calculus/README.md)
(divergence and the divergence form of a conservation law).

Oscillation and wave theory is the physics that seismology, radar, sonar,
ultrasound and fibre-optic sensing are all made of. This module builds it in the
order in which it is used: one oscillator, then damping and resonance, then many
oscillators, then the continuum limit that produces the wave equation, then the
phenomena that the wave equation does and does not describe.

The module is deliberately **derivation-first**. Every frequency, speed and
coefficient is obtained from Newton's second law and a constitutive assumption,
and every approximation is stated with the regime in which it holds. Two of those
statements carry most of the weight downstream: the wave equation derived in
lesson 05, and the distinction between phase and group velocity in lesson 07.

## Learning objectives

By the end of this module you will be able to:

1. Identify the small-oscillation limit of any smooth potential, and state the
   amplitude at which it fails.
2. Analyse a damped and driven oscillator, and measure $Q$ from a decay, from a
   spectrum and from a phase lag.
3. Diagonalise a system of coupled oscillators, interpret the normal modes, and
   compute beats and mode shapes.
4. Derive the wave equation from continuum physics for a string, a rod and a
   fluid, and explain why the geometry changes the speed.
5. Solve the wave equation analytically (d'Alembert) and numerically (explicit
   finite differences), with a measured convergence order and a verified Courant
   limit.
6. Superpose waves: interference, standing waves, energy bookkeeping and the
   quantisation of wavelengths in a bounded system.
7. Distinguish phase from group velocity, classify dispersion relations, and
   measure both speeds from a packet.
8. Apply Snell's law, the reflection and transmission coefficients, and the
   critical-angle behaviour, and state what the elastic (Zoeppritz) problem adds.
9. Estimate diffraction and resolution limits, and choose the right limit
   (Rayleigh, Fresnel zone, migrated) for the geometry.
10. Measure attenuation, define $Q$, and state why attenuation and dispersion
    cannot be specified independently.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Simple Harmonic Motion and Small-Oscillation Approximation](./01-simple-harmonic-motion.md) | beginner | Every smooth well is a parabola near its minimum |
| 02 | [Damped and Driven Oscillations, Resonance and Quality Factor](./02-damped-driven.md) | intermediate | Resonance, the bandwidth and the four definitions of $Q$ |
| 03 | [Coupled Oscillators and Normal Modes](./03-coupled-oscillators.md) | advanced | $N$ oscillators are $N$ independent oscillators in the right coordinates |
| 04 | [Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity](./04-wave-basics.md) | beginner | The vocabulary, and the sampling limit that cannot be undone |
| 05 | [Deriving the Wave Equation from Continuum Physics](./05-wave-equation-derivation.md) | advanced | Newton's second law plus a constitutive law produces $u_{tt} = c^2\nabla^2u$ |
| 06 | [Superposition, Interference and Standing Waves](./06-superposition-interference.md) | intermediate | Interference redistributes energy; a standing wave transports none |
| 07 | [Dispersion, Group Velocity and Phase vs Group Speed](./07-dispersion.md) | advanced | The phase and the envelope travel at different speeds |
| 08 | [Reflection, Refraction and Snell's Law for Waves](./08-reflection-refraction.md) | intermediate | Snell's law is phase matching; the coefficients come from the boundary conditions |
| 09 | [Diffraction, Scattering and Resolution Limits](./09-diffraction.md) | advanced | An edge radiates; resolution is $\lambda/D$ and the Fresnel zone |
| 10 | [Attenuation, Absorption and the Quality Factor Q](./10-attenuation.md) | advanced | Loss and dispersion are one constitutive statement |

## Suggested path

**If you are working through the physics folder in order:** all ten lessons. The
sequence 01 → 02 → 03 → 05 is the dependency spine of the module; lesson 04 can be
read early (it is kinematic and beginner-level) and lessons 06–10 can be read in
any order after 05.

**If you are here for seismology:** read
[01](./01-simple-harmonic-motion.md) §3, [02](./02-damped-driven.md) (for instrument
response and $Q$), [03](./03-coupled-oscillators.md) §3.2,
[05](./05-wave-equation-derivation.md) in full — including the bar-versus-P-speed
warning in §3.3 — then [07](./07-dispersion.md) and [08](./08-reflection-refraction.md).
That is the shortest route to reading a seismology paper critically.

**If you are here for GPR or near-surface work:** read
[04](./04-wave-basics.md) (sampling and resolution),
[09](./09-diffraction.md) (Fresnel zones) and
[10](./10-attenuation.md) (loss and skin depth), then
[02-07 Electromagnetism](../07-electromagnetism/README.md).

**If you already have a physics background:** attempt ★★★9 of
[05](./05-wave-equation-derivation.md) and ★★★10 of
[07](./07-dispersion.md) first. If both come out cleanly, use lessons 01–04 as
reference and go directly to module 04.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-simple-harmonic-motion.md`](./01-simple-harmonic-motion.md) … [`10-attenuation.md`](./10-attenuation.md) | The ten lessons |
| [`exercises/01-simple-harmonic-motion-exercises.md`](./exercises/01-simple-harmonic-motion-exercises.md) | Exercises for lesson 01 (the same pattern for lessons 02–10) |
| [`exercises/05-wave-equation-derivation-solutions.md`](./exercises/05-wave-equation-derivation-solutions.md) | Worked solutions including the impedance-averaging and shallow-water problems |
| [`exercises/08-reflection-refraction-solutions.md`](./exercises/08-reflection-refraction-solutions.md) | Worked solutions including the thin-layer composite reflection |
| [`code/shm_demo.py`](./code/shm_demo.py) | Pendulum period by the AGM, RK4 accuracy, the breakdown of the small-angle approximation |
| [`code/damped_driven_demo.py`](./code/damped_driven_demo.py) | Logarithmic decrement, resonance curves, exact half-power bandwidth |
| [`code/coupled_oscillators_demo.py`](./code/coupled_oscillators_demo.py) | Jacobi diagonalisation, closed-form chain frequencies, beats, single-mode purity |
| [`code/wave_basics_demo.py`](./code/wave_basics_demo.py) | Parameter table, aliasing, cycle skipping in phase-velocity measurement |
| [`code/wave_equation_derivation_demo.py`](./code/wave_equation_derivation_demo.py) | Lattice dispersion, second-order convergence, the exact Courant limit |
| [`code/interference_demo.py`](./code/interference_demo.py) | Exact two-source fringes, energy bookkeeping, standing-wave profile, beam steering |
| [`code/dispersion_demo.py`](./code/dispersion_demo.py) | Measured phase and group velocities, packet spreading against $d^2\omega/dk^2$ |
| [`code/reflection_refraction_demo.py`](./code/reflection_refraction_demo.py) | Snell's law, a finite-difference measurement of $R$ and $T$, boundary-condition residuals |
| [`code/diffraction_demo.py`](./code/diffraction_demo.py) | Slit and Airy patterns by quadrature, $J_1$ zeros, Fresnel zones, resolution limits |
| [`code/attenuation_demo.py`](./code/attenuation_demo.py) | $\alpha$ versus $Q$, $Q$ from a decay, spectral-ratio $Q$ with noise, SLS dispersion |

Every script uses only the Python standard library, so they run in any Python 3
installation with no packages. Run them; do not read them.

## Mastery checkpoint

Complete this without notes and without a computer beyond arithmetic.

> A granite-like rock has $\rho = 2700\ \mathrm{kg\,m^{-3}}$, $\lambda = 25$ GPa
> and $\mu = 30$ GPa. **(a)** Write down the wave equation you would use to model
> P-wave propagation in it, and justify the choice of the speed by deriving it
> from Newton's second law and a constitutive law. **(b)** State, with numbers,
> why the 1-D bar speed $\sqrt{E/\rho}$ is not the answer, and give the ratio.
> **(c)** A 30 Hz wavelet propagates 10 km. Using $Q = 100$, compute the amplitude
> loss and the frequency below which the signal is still above 10 per cent of its
> initial amplitude. **(d)** At what depth would a 25 Hz reflection survey place
> the first Fresnel zone radius at 200 m, and what lateral resolution could
> migration achieve there? **(e)** List the three most important approximations you
> made and one observation for each that would falsify it.

Parts (a) and (b) are lesson [05](./05-wave-equation-derivation.md) §3.3 and the
derivation completed in
[02-04-05](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md); part (c)
is lesson [10](./10-attenuation.md) §3.1; part (d) is lesson
[09](./09-diffraction.md) §3.5. Part (e) is the habit the whole module is trying to
instil.

## Common pitfalls across this module

1. **Dropping a factor of $2\pi$.** The most frequent error in the subject; §6 of
   every lesson is a dimensional check for exactly this reason.
2. **Using a formula outside its geometry.** $\sqrt{E/\rho}$, $\sqrt{K/\rho}$,
   $\sqrt{(\lambda+2\mu)/\rho}$ and $\sqrt{\mu/\rho}$ are all "the sound speed",
   and picking the wrong one is a tens-of-per-cent error.
3. **Quoting a small-angle or high-$Q$ result as exact.** Fringe spacing
   $\lambda L/d$, bandwidth $2\beta$, decay $Q = \pi/\delta$ and
   $\omega_r = \omega_0$ are all approximations with measurable errors, quoted in
   the lessons.
4. **Confusing phase and group velocity.** They differ by factors of two in the
   commonest geophysical dispersion relations.
5. **Believing that attenuation can be specified without dispersion.** Causality
   forbids it.
6. **Mixing amplitude and energy conventions at an interface.** State whether a
   coefficient refers to pressure, velocity or energy.
7. **Treating numerical dispersion as physics.** Measure the convergence order
   before interpreting a dispersive arrival.
8. **Measuring $Q$ from a raw amplitude decay.** Geometric spreading, coupling and
   transmission losses usually dominate.

## Related modules

- [02-01 Measurement, Units and Physical Reasoning](../01-measurement-and-physical-reasoning/README.md)
  — units, uncertainty and scaling, used throughout.
- [02-02 Classical Mechanics](../02-classical-mechanics/README.md) — the force
  laws behind every derivation here.
- [02-04 Elasticity and Continuum Mechanics](../04-elasticity-and-continuum-mechanics/README.md)
  — the vector version of this module, and the source of the P- and S-wave speeds.
- [01-06 Multivariable and Vector Calculus](../../01-mathematics/06-multivariable-calculus/README.md)
  — the operators used in the derivations.
- [01-10 Fourier Analysis](../../01-mathematics/10-fourier-analysis/README.md) —
  the decomposition of a wave field into frequencies.
- [20-signal-processing](../../20-signal-processing/README.md) — sampling,
  filtering and spectral estimation in practice.
- [06-seismology](../../06-seismology/README.md) — the discipline built on this
  module.
- [05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)
  — where the elastic and anelastic parameters of rocks are measured.
