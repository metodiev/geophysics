---
id: 02-03-01
title: "Simple Harmonic Motion and Small-Oscillation Approximation"
level: beginner
prereqs: ["01-03-05", "01-05-04", "02-02-02"]
estimated_minutes: 90
tags: [oscillations, harmonic-motion, linearisation, seismometry]
---

# Simple Harmonic Motion and Small-Oscillation Approximation

## Learning objectives

By the end of this lesson you will be able to:

1. **Write down** the equation of simple harmonic motion (SHM) for a mass on a
   spring, a pendulum and a general one-dimensional potential well, and read off
   the angular frequency $\omega_0$ in each case.
2. **Derive** $\omega_0 = \sqrt{k/m}$ from Newton's second law and
   $\omega_0 = \sqrt{g/L}$ as the small-angle limit of the pendulum.
3. **Linearise** an arbitrary smooth potential about a stable equilibrium and
   explain why *every* small oscillation is harmonic, whatever the physics.
4. **Quantify** the error of the small-oscillation approximation: state that the
   leading correction to the period of a pendulum is $T = T_0(1 + \theta_0^2/16
   + \cdots)$, and know the amplitude at which the approximation fails by 1 per
   cent.
5. **Verify** the claims numerically, and measure the stated convergence orders
   of the numerical integration rather than trusting them.
6. **Explain** why a seismometer or geophone is a small-oscillation device and
   what breaks when the ground motion is large.

## Prerequisites

- [01-03-05 Phase, Harmonics and Simple Harmonic Motion](../../01-mathematics/03-trigonometry/05-phase-and-harmonics.md)
  — sine and cosine, amplitude, period, phase.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../../01-mathematics/05-single-variable-calculus/04-taylor-series.md)
  — the expansion that does all the work in this lesson.
- [02-02-02 Newton's Laws of Motion](../02-classical-mechanics/02-newtons-laws.md)
  — force, acceleration, and the meaning of an equilibrium.

## 1. The phenomenon, and why it is everywhere

Pluck one guitar string, bow a violin string, and the two look very different.
Yet a single equation describes the small vibration of both:

$$\frac{d^2x}{dt^2} + \omega_0^2 x = 0 . \tag{1}$$

Its general solution is $x(t) = A\cos(\omega_0 t + \varphi)$, with amplitude $A$
and phase $\varphi$ fixed by the initial conditions. Everything that oscillates
small does so this way, and the reason is not that pendulums and strings are
similar — it is that *any smooth function near its minimum is a parabola*. That
single fact is the most reusable idea in this module, and the rest of the module
is built on it.

Geophysics depends on it three times over:

1. **Instruments.** A seismometer is a mass on a spring (a pendulum for long
   periods). Its response is the solution of equation (1), and its calibration
   is the statement that the ground motion is small compared with the instrument
   scale.
2. **Modes.** The Earth rings in normal modes after a great earthquake. Each
   mode is a harmonic oscillator with its own $\omega_0$, and reading those
   frequencies is how the deep interior is probed.
3. **Waves.** A wave is a chain of coupled oscillators. Lesson
   02-03-05 derives the wave equation by taking the continuum limit of exactly
   the chain studied in lesson 02-03-03, and the wave speed that comes out is the
   oscillation frequency per wavelength.

## 2. Precise definitions

### 2.1 Simple harmonic motion

A system performs **simple harmonic motion** if there is a coordinate $x$,
measured from a stable equilibrium, whose equation of motion is exactly
equation (1) for some constant $\omega_0 > 0$. The constant is the **angular
frequency**, and

$$T = \frac{2\pi}{\omega_0}, \qquad f = \frac{1}{T} = \frac{\omega_0}{2\pi}
\tag{2}$$

are the **period** and the **ordinary frequency**. The solution is periodic, and
its amplitude does not decay. Two constants of integration, $A$ and $\varphi$,
fix the trajectory: a second-order equation needs exactly two.

### 2.2 Energy

Multiplying equation (1) by $m\dot{x}$ and integrating gives the conserved
energy

$$E = \tfrac{1}{2}m\dot{x}^2 + \tfrac{1}{2}m\omega_0^2 x^2
= \tfrac12 m\omega_0^2 A^2 . \tag{3}$$

For a spring this is kinetic plus elastic energy; for a pendulum it is kinetic
plus gravitational potential. The form of equation (3) — one term quadratic in
velocity, one quadratic in displacement — is the signature of a harmonic
oscillator, and it will reappear in electromagnetism, in normal modes, and in
the mechanical analogue of a resonant circuit.

### 2.3 The quality of an oscillator

Real oscillators lose energy. The **quality factor** $Q$ is defined by the
fractional energy lost per radian of phase,

$$\frac{1}{Q} = -\frac{1}{E}\frac{dE}{d\phi}
= -\frac{1}{\omega_0 E}\frac{dE}{dt} , \tag{4}$$

and is treated properly in lesson 02-03-02. Recording it here matters because
$Q$ is the parameter that survives into seismology, where it measures
attenuation.

## 3. Derivations

### 3.1 Mass on a spring: the prototype

Hooke's law for a linear spring is $F = -kx$ with $k > 0$. Newton's second law
gives

$$m\ddot x = -kx \quad\Longrightarrow\quad \ddot x + \frac{k}{m}x = 0
\quad\Longrightarrow\quad \omega_0 = \sqrt{\frac{k}{m}} . \tag{5}$$

Three things to notice. First, $\omega_0$ depends on the *ratio* $k/m$, not on
the amplitude: the period of a harmonic oscillator is independent of how far it
is displaced. Second, the equation is linear, so solutions superpose — the basis
of lesson 02-03-06. Third, the force must be *negative* feedback: $F = +kx$
gives exponential growth, not oscillation.

### 3.2 The pendulum and the small-angle approximation

For a pendulum of length $L$ displaced by angle $\theta$, the tangential
equation of motion is

$$mL\ddot\theta = -mg\sin\theta \quad\Longrightarrow\quad
\ddot\theta + \frac{g}{L}\sin\theta = 0 . \tag{6}$$

This is **not** SHM. Expanding $\sin\theta = \theta - \theta^3/6 + O(\theta^5)$,

$$\ddot\theta + \frac{g}{L}\theta = \frac{g}{6L}\theta^3 + O(\theta^5) . \tag{7}$$

Dropping the right-hand side gives $\omega_0 = \sqrt{g/L}$ with a *relative*
error in the frequency of order $\theta_0^2/16$: the cubic term is not small in
the sense of being negligible, it is small in the sense of being of order
$\theta_0^2$ times the linear term.

The standard route to the exact period uses the energy integral and gives a
complete elliptic integral of the first kind,

$$T = 4\sqrt{\frac{L}{g}}\,K\!\left(\sin\frac{\theta_0}{2}\right), \qquad
K(k) = \int_0^{\pi/2}\frac{d\phi}{\sqrt{1 - k^2\sin^2\phi}} , \tag{8}$$

whose expansion is the classical series

$$T = T_0\left(1 + \frac{\theta_0^2}{16} + \frac{11\,\theta_0^4}{3072} +
O(\theta_0^6)\right), \qquad T_0 = 2\pi\sqrt{\frac{L}{g}} . \tag{9}$$

The demo computes $K$ by the arithmetic–geometric mean, so no elliptic-integral
library is needed.

### 3.3 The general potential well

Let a particle of mass $m$ move in a smooth potential $V(x)$ with a stable
equilibrium at $x_\ast$, so $V'(x_\ast) = 0$ and $V''(x_\ast) > 0$. Taylor
expanding about the equilibrium and choosing $V(x_\ast) = 0$,

$$V(x) = \tfrac12 V''(x_\ast)(x - x_\ast)^2
+ \tfrac16 V'''(x_\ast)(x-x_\ast)^3 + \cdots . \tag{10}$$

Keeping only the quadratic term, the force is $-V''(x_\ast)(x-x_\ast)$ — a spring
with stiffness $k_{\mathrm{eff}} = V''(x_\ast)$ — and therefore

$$\omega_0 = \sqrt{\frac{V''(x_\ast)}{m}} . \tag{11}$$

This is the **small-oscillation approximation** in its most general form. It
explains why the same mathematics governs a pendulum, a diatomic molecule, a
building, a seismic mode and a resonant circuit: all of them are quadratic near
a minimum.

The error of the approximation is controlled by the first neglected term. From
equation (10), the cubic term shifts the oscillation frequency at second order
in amplitude, by an amount proportional to $V'''/V''$ times the amplitude. The
demo measures this for an explicitly asymmetric well.

### 3.4 Step-by-step: the period of a pendulum by the AGM

1. Multiply equation (6) by $\dot\theta$ and integrate: with $\theta(0) =
   \theta_0$, $\dot\theta(0) = 0$,
   $\tfrac12\dot\theta^2 = \tfrac{g}{L}(\cos\theta - \cos\theta_0)$.
2. Separate variables: $dt = -\sqrt{\frac{L}{2g}}\,
   \frac{d\theta}{\sqrt{\cos\theta - \cos\theta_0}}$ for the quarter period.
3. Substitute $\sin(\theta/2) = \sin(\theta_0/2)\sin\phi$ to get
   $T = 4\sqrt{L/g}\,K(\sin(\theta_0/2))$.
4. Evaluate $K$ numerically: $K(k) = \pi/(2\,\mathrm{AGM}(1,\sqrt{1-k^2}))$,
   where the AGM is the limit of $a_{n+1} = (a_n+b_n)/2$,
   $b_{n+1} = \sqrt{a_nb_n}$; it converges quadratically, so six or seven
   iterations give full double precision.

## 4. Physical interpretation

**The frequency is a stiffness-to-inertia ratio.** Every version of $\omega_0$
in this lesson has the form $\sqrt{\text{(restoring coefficient)}/\text{(inertia
coefficient)}}$: $\sqrt{k/m}$, $\sqrt{g/L}$ (with $mL$ the inertia and $mg$ the
restoring force per radian), $\sqrt{V''/m}$. This reading is worth carrying into
elasticity, where the same ratio becomes $\sqrt{\text{modulus}/\text{density}}$
and produces the seismic wave speeds.

**Amplitude is not a frequency.** The idealised oscillator has a period
independent of amplitude. That independence is what makes clocks possible, and
its failure at large amplitude is what makes clocks need a linearising
mechanism. The failure is second order in amplitude, which is why a pendulum
clock is accurate to one part in $10^4$ at a few degrees of swing.

**Energy sloshes between two quadratic reservoirs.** Half the energy is kinetic
at the equilibrium and half is potential at the turning points; the time average
of each is the same. This is the statement that will become, for a wave, the
equal partition between kinetic and elastic energy.

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Linear restoring force | $F = -k x$ exactly | Period becomes amplitude-dependent; the motion is no longer sinusoidal (§3.3) |
| One degree of freedom | Energy stays in a single coordinate | Coupling redistributes energy; see lesson 02-03-03 |
| No dissipation | No damping term | Amplitude decays and $Q$ becomes finite; see lesson 02-03-02 |
| Small displacement in the linear-geometry sense | Pendulum $\theta_0 \ll 1$ | Geometric and material nonlinearity, chaotic motion of a driven pendulum |
| Inertia constant in time | $m$ fixed | Variable-mass systems (a rocket, a melting glacier) need a different equation |

The quantitative statement of the first row: $T/T_0 - 1 = \theta_0^2/16$ for a
pendulum at amplitude $\theta_0$ in radians. The approximation is good to 1 per
cent for $\theta_0 \le 0.398$ rad ($22.8^\circ$) and to 10 per cent for
$\theta_0 \le 1.21$ rad ($69.3^\circ$). Those amplitudes are *large* — much
larger than a seismometer diaphragm deflection — which is why the small-
oscillation approximation is so serviceable.

## 6. Units and dimensional analysis

In SI, $\omega_0$ has units of radians per second (s⁻¹), $T$ seconds, and
$f$ hertz (also s⁻¹). Radians are dimensionless, which is why $\omega$ and $f$
have the same dimensions but different numerical values: $f = \omega/2\pi$.

Check equation (5): $[k] = \mathrm{N\,m^{-1}} = \mathrm{kg\,s^{-2}}$, so
$[k/m] = \mathrm{s^{-2}}$ and $\sqrt{k/m}$ has units of s⁻¹. ✓

Check equation (11): $[V''] = \mathrm{J\,m^{-2}} = \mathrm{kg\,s^{-2}}$, so
$[V''/m] = \mathrm{s^{-2}}$. ✓

Check the phase in equation (3) of lesson 02-03-02 (used later):
$\omega_0 t$ is (s⁻¹)(s), dimensionless, as an angle must be. A common error is
to write $x = A\cos(2\pi f t + \varphi)$ and then substitute $\omega = 2\pi f$
as well, doubling the frequency.

The combination $g/L$ has units $\mathrm{m\,s^{-2}/m} = \mathrm{s^{-2}}$ ✓, and
for $L = 1$ m, $g = 9.80665$ m s⁻², $T_0 = 2.006\,409$ s. All the numbers in
this lesson were computed with $g = 9.80665$ m s⁻².

## 7. Python demonstration

[`code/shm_demo.py`](./code/shm_demo.py) runs with the standard library alone.

```python
# From the demo: the exact period needs the complete elliptic integral,
# computed by the arithmetic-geometric mean.
def elliptic_K(k):
    a, b = 1.0, math.sqrt(1.0 - k * k)
    for _ in range(64):
        a, b = 0.5 * (a + b), math.sqrt(a * b)
        if abs(a - b) < 1e-17:
            break
    return math.pi / (2.0 * a)

def pendulum_period_exact(length, theta0):
    return 4.0 * math.sqrt(length / G) * elliptic_K(math.sin(0.5 * theta0))
```

Observed output (excerpt) with $L = 1$ m, $g = 9.80665$ m s⁻²:

```text
k = 25.0 N/m, m = 4.0 kg  ->  omega0 = 2.500000 rad/s, T = 2.513274 s
  dt = 1e-02: x(2 s) = +1.418310848815e-02 m, exact = +1.418310927316e-02 m, relative error = 1.570e-08
  dt = 1e-03: x(2 s) = +1.418310927308e-02 m, exact = +1.418310927315e-02 m, relative error = 1.300e-12
  dt = 1e-04: x(2 s) = +1.418310927316e-02 m, exact = +1.418310927314e-02 m, relative error = 4.884e-13
  Relative error falls by ~10^4 per decade of dt: RK4 is 4th order.
```

```text
L = 1.0 m, g = 9.80665 m/s^2  ->  T0 (small angle) = 2.006409293 s

  theta0    exact T(s)   series T(s)   numeric T(s)    T0 err  series err
   0.010   2.006421833   2.006421833    2.006421833 6.250e-06   0.000e+00
   0.100   2.007664017   2.007664017    2.007664017 6.254e-04  -2.347e-10
   0.500   2.038215958   2.038208463    2.038215958 1.585e-02  -3.677e-06
   1.000   2.139502939   2.138994282    2.139502939 6.633e-02  -2.377e-04
   2.000   2.666326241   2.622962148    2.666326242 3.289e-01  -1.626e-02
```

```text
 theta0(rad)  theta0(deg)     T/T0 - 1  theta0^2/16
      0.0100        0.573     0.000006     0.000006
      0.1000        5.730     0.000625     0.000625
      0.5000       28.648     0.015853     0.015625
      1.0000       57.296     0.066334     0.062500
  period error reaches   1.0% at theta0 = 0.3982 rad = 22.81 deg
  period error reaches  10.0% at theta0 = 1.2100 rad = 69.33 deg
```

```text
Any smooth potential well is a parabola near its minimum:
  Example: V(x) = 12.5 x^2 + 5 x^3, V''(0) = 25.0 N/m -> omega_eff = 2.500000 rad/s
  amplitude  0.001 m: measured T = 2.513275 s, T_SHM = 2.513274 s, +1.501e-07
  amplitude  0.100 m: measured T = 2.517219 s, T_SHM = 2.513274 s, +1.569e-03
```

### What to observe

| Observation | Consequence |
|---|---|
| The RK4 relative error falls by $10^4$ per decade of $dt$ | The integrator is fourth order; a measurement of the order is a measurement of the code, and it should always be made before trusting a simulation |
| The series period matches the exact elliptic period to $2\times10^{-10}$ at $\theta_0 = 0.1$ | The $\theta_0^2/16$ term is the whole story below $10^\circ$; the $\theta_0^4$ term only matters for large swings |
| The exact minus small-angle error is $6.25\times10^{-4}$ at $\theta_0 = 0.1$ | The small-angle approximation is good to one part in 1600 at 5.7° — far better than any field measurement of a pendulum |
| Energy drift is $1.7\times10^{-13}$ relative at $dt = 10^{-3}$ s | Fourth-order accuracy in the *solution* also buys conservation of the energy invariant to the same order |
| The cubic well shows a period shift that scales as the amplitude | The frequency shift is second order in amplitude, as §3.3 predicts |

> **Breaking exercise.** Change `theta0` to 3.0 rad in the exact-period loop and
> predict, before running, whether the series still agrees with the elliptic
> result to three digits. Then explain the answer in one sentence.

## 8. Common mistakes

1. **Confusing $\omega$ and $f$.** Writing $T = 2\pi/\omega$ is correct; writing
   $T = 2\pi f$ is not. The factor $2\pi$ is where most sign-and-factor errors in
   this module originate.
2. **Assuming the period is always independent of amplitude.** It is true for a
   linear restoring force only. For a pendulum the dependence is
   $\theta_0^2/16$, and for a strongly nonlinear system it can be large.
3. **Linearising about an unstable equilibrium.** If $V''(x_\ast) < 0$ the
   equilibrium is a maximum, $\omega_0^2 < 0$, and the solution is exponential —
   not an oscillation but an instability.
4. **Forgetting that small oscillation is an approximation with a stated
   regime.** The usual failure is a *driven* pendulum at large amplitude, where
   the motion becomes chaotic and no small-angle expansion is valid.
5. **Treating the amplitude as a property of the oscillator.** It is a property
   of the initial conditions. $\omega_0$ is a property of the system.
6. **Believing that "harmonic" means "sinusoidal".** Damped and driven
   oscillators are still linear systems with a well-defined resonance, but their
   solutions are not pure sines (lesson 02-03-02).
7. **Applying the energy expression (3) to a pendulum with large amplitude.**
   The potential $mgL(1-\cos\theta)$ is not $\tfrac12mgL\theta^2$ beyond the
   small-angle regime, and the period correction above is precisely the
   consequence.

## 9. Real-world applications

- **Seismometry.** A geophone is a mass–spring oscillator inside a case; the
  ground motion is inferred from the relative displacement of the mass. For that
  inference to be linear, the ground displacement must be small compared with
  the instrument scale, so the small-oscillation approximation is a design
  requirement, not an idealisation. Standard data are distributed by
  [EarthScope](https://www.earthscope.org) and [ORFEUS](https://www.orfeus-eu.org),
  and read with [ObsPy](https://docs.obspy.org).
- **Normal modes of the Earth.** The lowest-order spheroidal mode has a period
  near 54 minutes; each mode is a harmonic oscillator whose frequency measures
  the radial structure of the planet (lesson
  02-03-03, and [06-seismology](../../06-seismology/README.md)).
- **Tidal forcing.** The solid Earth responds to the tidal potential as a driven
  oscillator whose resonance, if any, is very far from the tidal frequencies, so
  the response is essentially quasi-static; the small-oscillation algebra still
  determines the Love numbers.
- **Instrument calibration.** The $Q$ of a geophone determines its useful
  bandwidth; a $Q$ near $1/\sqrt2$ flattens the response, which is why damped
  geophones are specified by their damping rather than their $Q$
  (lesson 02-03-02).
- **Rocking of structures and slopes.** The fundamental mode of a building or a
  soil column is a small-oscillation problem whose frequency shifts as the
  material softens; measuring that shift is the basis of structural health
  monitoring and of site-response seismology.

## 10. Further reading

- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** Chapter 1 treats the harmonic oscillator as the
  building block of the seismometer response. Level: advanced.
- **Stein, S., & Wysession, M. *An Introduction to Seismology, Earthquakes and
  Earth Structure* (Blackwell, 2003).** The instrument-response chapter is the
  clearest published account for this level. Level: intermediate.
- **Rayleigh, Lord. *The Theory of Sound* (1896; Dover reprint).** The original
  treatment of the pendulum and of the small-oscillation method, still worth
  reading for how the approximations are argued. Level: intermediate.
- **Landau, L. D., & Lifshitz, E. M. *Mechanics* (Pergamon).** §21–23 derive the
  general small-oscillation theory for many degrees of freedom from the
  potential expansion used in §3.3. Level: advanced.
- **Mavko, G., Mukerji, T., & Dvorkin, J. *The Rock Physics Handbook*
  (Cambridge University Press).** For the oscillator analogy in rock physics.
  Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 Damped and Driven Oscillations, Resonance and Quality Factor](./02-damped-driven.md)
  — what happens when energy is lost, and when a force is applied.
- [03 Coupled Oscillators and Normal Modes](./03-coupled-oscillators.md) —
  many oscillators at once, and the diagonalisation that solves them.
- [04 Wave Description](./04-wave-basics.md) — the kinematic language of waves,
  built on the oscillating source.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../../01-mathematics/05-single-variable-calculus/04-taylor-series.md)
  — the tool used in every derivation here.
- [01-08 Ordinary Differential Equations](../../01-mathematics/08-ordinary-differential-equations/README.md)
  — the systematic theory of linear second-order equations.
- [02-04 Elasticity and Continuum Mechanics](../04-elasticity-and-continuum-mechanics/README.md)
  — where the oscillator becomes a continuum and the frequencies become wave
  speeds.
- [06-seismology](../../06-seismology/README.md) — the discipline that is built
  on this lesson.

Exercises and worked solutions:
[`exercises/01-simple-harmonic-motion-exercises.md`](./exercises/01-simple-harmonic-motion-exercises.md)
and
[`exercises/01-simple-harmonic-motion-solutions.md`](./exercises/01-simple-harmonic-motion-solutions.md).

## Self-assessment checklist

Work through this without notes. If any item is not a clear "yes", reread the
section named beside it.

- [ ] I can write the SHM equation and identify $\omega_0$ for a spring, a
      pendulum and a general potential well. (Sections 2, 3.1–3.3)
- [ ] I can derive $\omega_0 = \sqrt{k/m}$ from Newton's second law in three
      lines and state the sign condition on the restoring force. (Section 3.1)
- [ ] I can explain why every small oscillation is harmonic, and what
      $V''(x_\ast) > 0$ has to do with it. (Section 3.3)
- [ ] I can quote the leading period correction of a pendulum and the amplitude
      at which it reaches 1 per cent. (Section 5)
- [ ] I can state the units of $\omega_0$, $T$, $f$ and check $\sqrt{k/m}$ and
      $\sqrt{V''/m}$ dimensionally. (Section 6)
- [ ] I can convert between $\omega_0$, $T$ and $f$ without dropping a $2\pi$.
      (Section 6)
- [ ] I can describe what an energy-conservation check on a numerical
      integration tells me, and what it does not. (Section 7)
- [ ] I can name three geophysical systems that are small-oscillation problems
      and state the coordinate that plays the role of $x$. (Section 9)
