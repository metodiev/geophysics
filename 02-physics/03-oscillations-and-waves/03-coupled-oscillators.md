---
id: 02-03-03
title: "Coupled Oscillators and Normal Modes"
level: advanced
prereqs: ["02-03-01", "01-07-06", "01-06-01"]
estimated_minutes: 90
tags: [oscillations, normal-modes, eigenvalue-problem, seismology]
---

# Coupled Oscillators and Normal Modes

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the equations of motion of a chain of coupled oscillators as a
   symmetric matrix eigenvalue problem, including the fixed-end boundary
   condition.
2. **Derive** the closed-form frequencies
   $\omega_n = 2\sqrt{k/m}\,\sin\!\left(n\pi/(2(N+1))\right)$ for a fixed-end
   chain and explain physically why the highest mode is at $2\sqrt{k/m}$.
3. **Diagonalise** a coupled system, state why the eigenvectors are orthogonal,
   and use that orthogonality to expand an arbitrary initial condition.
4. **Explain** beats as the interference of two normal modes and compute the
   beat period from the frequency difference.
5. **Recognise** the same mathematics in the normal modes of the Earth, of a
   building, of a molecule and of a discretised wave equation — the last of which
   becomes the wave equation in lesson 02-03-05.
6. **Verify** all of the above numerically, including measured orthonormality
   and eigen-residuals rather than assumed ones.

## Prerequisites

- [02-03-01 Simple Harmonic Motion and Small-Oscillation Approximation](./01-simple-harmonic-motion.md)
  — the single oscillator, and the linearisation of a potential.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../../01-mathematics/07-linear-algebra/06-eigenvalues.md)
  — the eigenvalue problem, symmetric matrices and orthogonality.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../../01-mathematics/06-multivariable-calculus/01-partial-derivatives.md)
  — for the multi-variable Taylor expansion used in §3.1.

## 1. From one oscillator to many

Two identical pendulums joined by a weak spring do not oscillate at one
frequency. Start one swinging and, after a while, the other is swinging and the
first is nearly still; the energy returns periodically. Nothing about either
pendulum changed — the *system* has two characteristic frequencies, and the
apparent complexity is the superposition of two simple motions.

The general statement, which is the content of this lesson, is:

> A system of $N$ coupled harmonic oscillators has exactly $N$ **normal modes**.
> In a normal mode every part of the system moves sinusoidally at the *same*
> frequency, and the mode is therefore a single oscillator. Any motion of the
> system is a superposition of the normal modes.

This is the most useful theorem in classical physics after Newton's second law,
and it is the reason a seismogram can be decomposed into free oscillations, a
building response into modes, and a wave into Fourier components.

## 2. Precise definitions

**Normal mode.** A motion in which every coordinate oscillates at a single common
frequency $\omega_n$ with fixed relative amplitudes: $\mathbf{x}(t) = \mathbf{v}_n
\cos(\omega_n t + \varphi_n)$, where $\mathbf{v}_n$ is the mode shape.

**Mode shape (eigenvector).** The vector $\mathbf{v}_n$ giving the relative
amplitudes of the coordinates in mode $n$.

**Degeneracy.** Two or more distinct mode shapes sharing the same frequency.
Degenerate modes can be combined arbitrarily, which is why a circular drum has
families of equal-frequency patterns and why an isotropic elastic solid has two
equal-speed S polarisations (lesson
[02-04-05](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)).

## 3. Derivations

### 3.1 The general coupled-oscillator problem

Let a system have generalised coordinates $\mathbf{x} = (x_1,\dots,x_N)$, kinetic
energy $\tfrac12\dot{\mathbf{x}}^{\mathsf{T}}\mathbf{M}\dot{\mathbf{x}}$ and a
potential expanded to second order about a stable equilibrium,

$$V(\mathbf{x}) = \tfrac12\,\mathbf{x}^{\mathsf{T}}\mathbf{K}\mathbf{x}
+ O(\|\mathbf{x}\|^3) , \tag{1}$$

with $\mathbf{M}$ the (symmetric, positive-definite) mass matrix and
$\mathbf{K}$ the (symmetric) stiffness matrix whose entries are the second
derivatives of $V$. Lagrange's equations give

$$\mathbf{M}\ddot{\mathbf{x}} + \mathbf{K}\mathbf{x} = \mathbf{0} . \tag{2}$$

Substituting $\mathbf{x} = \mathbf{v}e^{i\omega t}$ gives the **generalised
eigenvalue problem**

$$\left(\mathbf{K} - \omega^2\mathbf{M}\right)\mathbf{v} = \mathbf{0}
\qquad\Longleftrightarrow\qquad
\mathbf{K}\mathbf{v} = \omega^2\mathbf{M}\mathbf{v} . \tag{3}$$

For $N$ degrees of freedom there are $N$ eigenfrequencies $\omega_n^2 \ge 0$; the
inequality is strict if the equilibrium is stable, and $\omega_1 = 0$ signals a
zero-frequency (rigid-body) mode, i.e. a direction in which the system can move
without cost — a rigid translation of the whole Earth, the rotation of a
satellite, the uniform translation of a coupled chain with free ends.

When $\mathbf{M} = m\mathbf{I}$, equation (3) is an ordinary symmetric
eigenvalue problem and the eigenvectors can be chosen orthonormal:
$\mathbf{v}_m^{\mathsf{T}}\mathbf{v}_n = \delta_{mn}$.

### 3.2 The fixed-end chain, and its closed form

Take $N$ equal masses $m$ joined by equal springs $k$, with the two ends
attached to rigid walls. The displacement of mass $j$ obeys

$$m\ddot u_j = k(u_{j+1} - 2u_j + u_{j-1}), \qquad j = 1,\dots,N , \tag{4}$$

with $u_0 = u_{N+1} = 0$. In matrix form, $(\mathbf{K}/m)$ is tridiagonal with
$2k/m$ on the diagonal and $-k/m$ on the off-diagonals.

Try a mode shape $u_j^{(n)} = \sin(j\theta_n)$:
substitution into equation (4) with $u = \sin(j\theta)e^{i\omega t}$ gives

$$-m\omega^2\sin j\theta = k\left[\sin((j+1)\theta) - 2\sin j\theta
+ \sin((j-1)\theta)\right]
= -4k\sin^2\!\left(\tfrac{\theta}{2}\right)\sin j\theta , \tag{5}$$

using the identity
$\sin((j+1)\theta)+\sin((j-1)\theta) = 2\sin j\theta\cos\theta$. Hence

$$\omega^2 = \frac{4k}{m}\sin^2\!\left(\frac{\theta}{2}\right). \tag{6}$$

The boundary condition $u_{N+1} = 0$ requires
$\sin((N+1)\theta) = 0$, so

$$\theta_n = \frac{n\pi}{N+1}, \qquad n = 1,\dots,N , \tag{7}$$

and therefore

$$\boxed{\ \omega_n = 2\sqrt{\frac{k}{m}}\,\sin\!\left(\frac{n\pi}{2(N+1)}\right)\ } \tag{8}$$

with mode shapes $u_j^{(n)} = \sin\!\left(\dfrac{jn\pi}{N+1}\right)$.

Four consequences:

1. **Fundamental.** $\omega_1 = 2\sqrt{k/m}\sin(\pi/(2(N+1))) \approx
   \sqrt{k/m}\,\pi/(N+1)$ for large $N$ — lower for a longer chain, as expected
   for a softer system.
2. **Ceiling.** $\omega_N = 2\sqrt{k/m}\sin(N\pi/(2(N+1))) \to 2\sqrt{k/m}$ as
   $N$ grows: no mode exceeds twice the single-oscillator frequency, because the
   stiffest relative motion is adjacent masses in exact antiphase.
3. **Packing.** Modes are not equally spaced; the density of modes increases with
   frequency. This is the discrete origin of the density of states in a
   continuum, and it is why a fine spatial sampling is needed to resolve high
   wavenumbers.
4. **Continuum limit.** Writing $j a \to x$, $N a \to L$ and using
   $\sin\theta \approx \theta$ for small $\theta$ gives
   $\omega_n \to (n\pi/L)\sqrt{ka^2/m}$ — a set of frequencies linear in $n$,
   which is what a wave equation predicts. Setting $k a = T$ (tension) and
   $m/a = \mu$ (linear density) identifies the speed $c = \sqrt{T/\mu}$. This is
   the derivation of the wave equation, completed in lesson 02-03-05.

### 3.3 Orthogonality, and why it matters

For $\mathbf{M} = m\mathbf{I}$, let $\mathbf{v}_m$, $\mathbf{v}_n$ be eigenvectors
with $\omega_m \ne \omega_n$. Taking the scalar product of
$\mathbf{K}\mathbf{v}_m = \omega_m^2 m\mathbf{v}_m$ with $\mathbf{v}_n$,
subtracting the same relation with $m$ and $n$ interchanged, and using the
symmetry of $\mathbf{K}$,

$$0 = \left(\omega_m^2 - \omega_n^2\right)m\,\mathbf{v}_n^{\mathsf{T}}\mathbf{v}_m
\quad\Longrightarrow\quad
\mathbf{v}_n^{\mathsf{T}}\mathbf{v}_m = 0 . \tag{9}$$

Orthogonality is what makes the modes *independent coordinates*: write
$\mathbf{x}(t) = \sum_n q_n(t)\mathbf{v}_n$ and substitute into equation (2);
projecting onto $\mathbf{v}_l$ and using equation (9) leaves $N$ *uncoupled*
equations $\ddot q_l + \omega_l^2q_l = 0$. The normal-mode coordinates $q_n$ are
the coordinates in which the coupled problem is $N$ independent oscillators.

### 3.4 Two masses, exactly

For $N = 2$, equation (8) gives $\omega_1 = 2\sqrt{k/m}\sin(\pi/6) =
\sqrt{k/m}$ and $\omega_2 = 2\sqrt{k/m}\sin(\pi/3) = \sqrt{3k/m}$, with mode
shapes $(1,1)$ and $(1,-1)$: the two masses move together (in-phase) and in
antiphase. Starting the system with $u_1 = A$, $u_2 = 0$ excites
$(\mathbf{v}_1 + \mathbf{v}_2)/\sqrt2$, so

$$u_1(t) = \frac{A}{2}\left[\cos\omega_1t + \cos\omega_2t\right], \qquad
u_2(t) = \frac{A}{2}\left[\cos\omega_1t - \cos\omega_2t\right] . \tag{10}$$

Using the product-to-sum identity,

$$u_2(t) = A\sin\!\left(\frac{\omega_1+\omega_2}{2}t\right)
\sin\!\left(\frac{\omega_2-\omega_1}{2}t\right), \tag{11}$$

a fast oscillation with a slow envelope of period $2\pi/|\omega_2-\omega_1|$: the
**beat**. The energy is entirely on mass 1 at $t = 0$, entirely on mass 2 at
$t = \pi/|\omega_2-\omega_1|$, and so on. This is the time-domain shape of a wave
packet (lesson 02-03-07), and the algebra is the same.

## 4. Physical interpretation

**Normal modes are the natural coordinates of a system.** Laboratory
spectroscopists call them vibrational modes, engineers call them eigenmodes,
seismologists call them free oscillations, and numerical analysts call them
eigenvectors of the stiffness matrix. The physics is one theorem.

**Mode order is a spatial frequency.** Mode $n$ has $n$ half-wavelengths across
the system: increasing $n$ means finer spatial structure and a stiffer effective
spring, hence a higher frequency. Counting nodes measures $n$.

**Beats are the exchange of energy between modes.** In a beat, energy moves
between coordinates at the difference frequency; in a wave packet it moves along
the medium at the group velocity. Both are statements about two nearby
frequencies, and both are governed by $|\omega_2-\omega_1|$ and by the mode
shapes.

**Degeneracy signals symmetry.** If two modes share a frequency, the system has a
symmetry that makes two directions equivalent. Breaking the symmetry (a slightly
anisotropic crystal, a rotating Earth) splits the degeneracy, and measuring the
splitting measures the symmetry-breaking. This is the principle of normal-mode
splitting used to image mantle anisotropy and Earth's rotation.

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Quadratic potential | Small displacements about a stable equilibrium | Nonlinear coupling: frequency pulling, energy transfer between modes, chaos (Fermi–Pasta–Ulam–Tsingou) |
| Linear springs, constant coefficients | Fixed $k$, $m$ | Slow parameter change: adiabatic invariants, mode conversion |
| No damping | Energy conserved | Modes have finite $Q$ and complex frequencies $\omega_n - i\beta_n$; the decomposition still works but with decaying amplitudes |
| $N$ finite | Discrete spectrum | Continuum: continuous spectrum, and the sum over modes becomes an integral (Fourier) |
| Symmetric $\mathbf{K}$ | Reciprocal coupling | Gyroscopic or convective coupling destroys the simple orthogonality and requires left and right eigenvectors |

## 6. Units and dimensional analysis

- $[k/m] = \mathrm{s^{-2}}$ ✓, so $\omega_n = 2\sqrt{k/m}\sin(\cdots)$ is s⁻¹;
  the sine is dimensionless and must be, since it is the argument of a
  trigonometric function.
- $\mathbf{K}$: N m⁻¹ = kg s⁻²; $\mathbf{M}$: kg; so the ratio $\mathbf{K/M}$ has
  s⁻² ✓ and its eigenvalues are squared frequencies.
- Mode shapes are dimensionless relative amplitudes; their normalisation sets
  their units.
- The beat period $2\pi/|\omega_2-\omega_1|$ is a time ✓, and it diverges as the
  two frequencies become equal — as must happen, because a degenerate pair cannot
  beat.

## 7. Python demonstration

[`code/coupled_oscillators_demo.py`](./code/coupled_oscillators_demo.py) builds
the tridiagonal matrix, diagonalises it with the Jacobi method, and integrates
the chain. Observed output with $k = 30$ N m⁻¹, $m = 0.5$ kg:

```text
N = 3 masses, k = 30.0 N/m, m = 0.5 kg:
    n   omega_numeric   omega_formula   rel.diff
    1     5.928506242     5.928506242   1.50e-16
    2    10.954451150    10.954451150   0.00e+00
    3    14.312680173    14.312680173   2.48e-16
  max |v_i . v_j - delta_ij| over all pairs = 2.220e-16
  max ||A v - omega^2 v||                       = 8.286e-14
```

```text
N = 2: omega1 = 7.745966692 rad/s, omega2 = 13.416407865 rad/s
  check: 2 sqrt(k/m) sin(pi/6) = 7.745966692 rad/s
  check: 2 sqrt(k/m) sin(pi/3) = 13.416407865 rad/s
  beat frequency |omega2 - omega1| = 5.670441173 rad/s, beat period = 1.108059341 s
  relative energy drift over 8 s: 3.749e-07
  measured envelope maxima at t = 1.635, 2.817, 3.999, 4.905 s ...
  mean spacing of envelope maxima = 1.1130 s (beat period 2 pi/|omega2-omega1| = 1.1081 s)
  largest |x2| measured = 0.009998 m (theory 0.010000 m)
```

```text
  mode 1: omega = 4.787271 rad/s, max deviation from cos(omega t) * mode over 3 s = 8.140e-10
  mode 2: omega = 9.105930 rad/s, max deviation from cos(omega t) * mode over 3 s = 5.553e-09
  mode 3: omega = 12.533237 rad/s, max deviation from cos(omega t) * mode over 3 s = 1.423e-08
  mode 4: omega = 14.733704 rad/s, max deviation from cos(omega t) * mode over 3 s = 2.308e-08
```

### What to observe

| Observation | Consequence |
|---|---|
| The eigenvalues match equation (8) to $2\times10^{-16}$ relative | The closed form for a fixed-end chain is exact, and the numerical diagonalisation is trustworthy at the level of round-off |
| $\max|\mathbf{v}_i\cdot\mathbf{v}_j - \delta_{ij}| = 1.1\times10^{-15}$ | Orthogonality is a property of the *computed* eigenvectors too, which is why the mode expansion is numerically stable |
| $\max\|\mathbf{A}\mathbf{v} - \omega^2\mathbf{v}\| \approx 10^{-13}$ | The eigen-residual is the right quality check to quote for any eigen-solver output |
| The envelope maxima are spaced 1.1130 s apart against a predicted beat period of 1.1081 s | The measurement is limited to one fast period (0.594 s) by the way the envelope is sampled, and the honest agreement is "0.4 per cent under sampling that cannot do better than 0.3 s" |
| The energy is conserved to $3.7\times10^{-7}$ relative over 8 s | The leapfrog integrator conserves a nearby invariant; an apparent energy loss of 1 part in $10^7$ is the integrator, not damping |
| Each single-mode initial condition follows $\cos(\omega t)$ times the mode shape to $10^{-8}$ | Exciting one normal mode excites *only* that mode, which is the operational definition of a normal mode |

> **Breaking exercise.** Set the initial condition to $u_1 = 0.01$,
> $u_2 = 0.02$ and predict, before running, how many normal modes the motion
> contains. Then verify by projecting the initial condition onto the eigenvectors
> in the script.

## 8. Common mistakes

1. **Assuming the mode frequencies are harmonically related.** They are
   $\sin(n\pi/(2(N+1)))$, not $n$ times the fundamental. Only the continuum limit
   is harmonic.
2. **Treating a mode shape as an absolute amplitude.** Only ratios are physical;
   the overall scale is the mode's excitation.
3. **Forgetting the boundary conditions.** Equation (8) is for fixed ends. Free
   ends give a rigid-body mode at $\omega = 0$; a heavy end mass changes every
   frequency.
4. **Believing a general motion is periodic.** A sum of modes with
   incommensurate frequencies never repeats; it is quasi-periodic. Only if the
   frequency ratios are rational does the motion return to its initial state.
5. **Ignoring damping when comparing with data.** A damped mode has complex
   frequency $\omega_n - i\beta_n$; fitting an undamped model to a long record
   biases the frequency.
6. **Using the same symbol for mode order and coordinate index.** Confusing
   $n$ (mode number) with $j$ (mass index) is the most common algebra slip in
   this topic; label them explicitly in every derivation.
7. **Assuming degeneracy is accidental.** It is a symmetry statement, and lifting
   the symmetry lifts the degeneracy in a predictable way.

## 9. Real-world applications

- **Free oscillations of the Earth.** After a great earthquake the planet rings in
  spheroidal and toroidal modes with periods from about 54 minutes up to tens of
  seconds; each period is a normal-mode eigenvalue of an elastic sphere, and the
  splitting of degenerate modes measures rotation and anisotropy. See
  [06-seismology](../../06-seismology/README.md).
- **Building and soil-column response.** The fundamental mode of a structure
  determines which frequencies are amplified; the same eigenproblem with
  distributed mass and stiffness is solved numerically for every seismic design.
- **Seismic instruments.** A sensor's mass–spring system is a single oscillator
  whose mode is deliberately chosen; coupling two instruments (a coil and a
  boom) produces two modes whose separation must exceed the design bandwidth.
- **Numerical modelling.** Any finite-difference discretisation of the wave
  equation *is* a coupled-oscillator chain; its mode frequencies are the
  dispersion relation of the scheme, and the highest mode sets the stability
  limit (lesson 02-03-05).
- **Molecular and mineral physics.** Vibrational modes of a crystal lattice give
  the phonon spectrum, hence the heat capacity and thermal expansion used in
  mineral-physics models of the deep Earth.
- **Engineering and structural health.** A shift in a mode frequency is the
  standard warning of stiffness loss in a bridge, a dam or a pressure vessel.

## 10. Further reading

- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** The normal-mode chapter derives the free oscillations
  of an elastic sphere from the same eigenvalue problem treated here. Level:
  advanced.
- **Stein, S., & Wysession, M. *An Introduction to Seismology, Earthquakes and
  Earth Structure* (Blackwell, 2003).** Normal modes and their observation, at
  the level of this lesson. Level: intermediate.
- **Landau, L. D., & Lifshitz, E. M. *Mechanics* (Pergamon).** §21–23 and §48 give
  the general theory of small oscillations and of normal modes, including
  degeneracy. Level: advanced.
- **Strogatz, S. H. *Nonlinear Dynamics and Chaos* (CRC Press).** The chapters on
  coupled oscillators and on beats give the intuition without the tensor
  formalism. Level: beginner to intermediate.
- **Ben-Menahem, A., & Singh, S. J. *Seismic Waves and Sources* (Springer,
  1981).** The most complete classical treatment of mode theory in geophysics.
  Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [01 Simple Harmonic Motion and Small-Oscillation Approximation](./01-simple-harmonic-motion.md)
  — the single oscillator, and the potential expansion used in §3.1.
- [02 Damped and Driven Oscillations, Resonance and Quality Factor](./02-damped-driven.md)
  — each mode acquires its own $Q$.
- [05 Deriving the Wave Equation from Continuum Physics](./05-wave-equation-derivation.md)
  — the continuum limit of the chain studied here.
- [07 Dispersion, Group Velocity and Phase vs Group Speed](./07-dispersion.md)
  — why the lattice is dispersive and the continuum is not.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../../01-mathematics/07-linear-algebra/06-eigenvalues.md)
  — the linear algebra this lesson applies.
- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — the Christoffel problem, a normal-mode problem in a continuum.
- [06-seismology](../../06-seismology/README.md) — free oscillations and
  normal-mode seismology.

Exercises:
[`exercises/03-coupled-oscillators-exercises.md`](./exercises/03-coupled-oscillators-exercises.md)
and
[`exercises/03-coupled-oscillators-solutions.md`](./exercises/03-coupled-oscillators-solutions.md).

## Self-assessment checklist

- [ ] I can write the coupled equations of motion in matrix form for any chain I
      am given, including the boundary conditions. (Section 3.2)
- [ ] I can derive the fixed-end dispersion relation
      $\omega_n = 2\sqrt{k/m}\sin(n\pi/(2(N+1)))$ without notes. (Section 3.2)
- [ ] I can explain why $\omega_N \to 2\sqrt{k/m}$ and why the modes are not
      equally spaced. (Section 3.2)
- [ ] I can prove orthogonality of the mode shapes from the symmetry of
      $\mathbf{K}$. (Section 3.3)
- [ ] I can expand an arbitrary initial condition in normal modes and say what
      determines each modal amplitude. (Sections 3.3, 3.4)
- [ ] I can derive the beat period and explain the energy exchange.
      (Section 3.4)
- [ ] I can state two physical consequences of degeneracy and two of its
      absence. (Section 4)
- [ ] I can explain what the continuum limit of the chain produces and identify
      $c = \sqrt{T/\mu}$ in it. (Section 3.2)
