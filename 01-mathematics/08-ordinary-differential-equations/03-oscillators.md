---
id: 01-08-03
title: "Damped and Driven Oscillators as Physical Models"
level: intermediate
prereqs: ["01-08-02", "01-03-05"]
estimated_minutes: 90
tags: [ordinary-differential-equations, oscillators, resonance, quality-factor, instrument-response]
---

# Damped and Driven Oscillators as Physical Models

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the driven damped oscillator equation and identify its three
   parameters in a physical system.
2. **Derive** the steady-state amplitude and phase by the complex-exponential
   method, and explain why the transient is a separate part of the solution.
3. **Locate** the resonance peak exactly, at $\omega_0\sqrt{1-2\zeta^2}$, and
   state when the approximation "resonance at $\omega_0$" is good enough.
4. **Relate** peak height and half-power bandwidth to $Q$, and derive both from
   the energy balance.
5. **Read** an instrument-response curve: explain why a velocity sensor is flat
   in velocity above its corner frequency, why it measures acceleration below
   it, and what that implies for long-period and normal-mode work.
6. **Distinguish** a genuine mechanical resonance from the diffusive
   (first-order) response of the ground to electromagnetic fields, and state
   how to tell them apart from a measured curve.

## Prerequisites

- [02 Second-Order Linear ODEs and Characteristic Equations](./02-second-order-linear.md) —
  the homogeneous equation, $\omega_0$, $\zeta$, $\omega_d$ and $Q$.
- [01-03-05 Phase, Harmonics and Superposition of Oscillations](../03-trigonometry/05-phase-and-harmonics.md) —
  phase, amplitude and superposition of sinusoids.
- [01-02-03 Exponentials, Logarithms and Decay Laws](../02-algebra/03-exponentials-logarithms.md) —
  helpful for the envelope and build-up arguments.

## 1. Intuition: driving a system at the wrong frequency

A free oscillator has only one interesting frequency, its own. A *driven*
oscillator has two — the driving frequency $\omega$ and the natural frequency
$\omega_0$ — and the whole subject is what happens when they compete.

Consider pushing a child on a swing. If you push at the swing's own frequency,
a small effort builds a large amplitude. If you push at twice that frequency,
the pushes cancel as often as they help and the swing barely moves. That is
resonance, and it is not an artefact of a mathematical idealisation: it is the
reason a building swaying at 0.3 Hz responds to ground motion at 0.3 Hz, why a
well's water column sloshes at its own period, why a lake seiche has a
characteristic period, and why an electromagnetic receiver coil rings.

The lesson has one physical message and one mathematical one:

- **Physically**, only two numbers matter: the ratio $\omega/\omega_0$ and the
  damping $\zeta$. Everything else is a scaling.
- **Mathematically**, the driven equation is solved most cleanly by allowing
  complex numbers temporarily and taking the real part at the end. This is not
  a shortcut; it is the reason the phase and the amplitude come out of one
  calculation instead of two.

## 2. The equation and its solution, stated

### 2.1 The equation

Take the homogeneous equation of
[02 Second-Order Linear ODEs](./02-second-order-linear.md) and add a harmonic
forcing:

$$\boxed{\;x'' + 2\zeta\omega_0 x' + \omega_0^2 x = \frac{F_0}{m}\cos(\omega t)\;}$$

where $F_0$ is the amplitude of the applied force, $\omega$ its angular
frequency, and $m$ the mass. The right-hand side is a **source term**. It is
not proportional to $x$ or $x'$, so the equation is non-homogeneous and its
general solution is

$$x(t) = \underbrace{x_{\text{hom}}(t)}_{\text{transient}} + \underbrace{x_{\text{part}}(t)}_{\text{steady state}} .$$

The homogeneous part decays as $e^{-\zeta\omega_0t}$ and is called the
**transient**; it remembers the initial conditions. The particular part
oscillates forever at the driving frequency and is called the **steady state**;
it forgets them. **The distinction is the whole content of Sections 3.1–3.2:
after a few decay times, the system's response depends only on the forcing, not
on how it was started.**

### 2.2 The complex method

Look for a particular solution of the form
$x_p = \operatorname{Re}[\hat{X}e^{i\omega t}]$ with $\hat X$ complex. Then
$x_p' = \operatorname{Re}[i\omega\hat Xe^{i\omega t}]$ and
$x_p'' = \operatorname{Re}[-\omega^2\hat Xe^{i\omega t}]$, and if the forcing is
written as $\operatorname{Re}[(F_0/m)e^{i\omega t}]$, the equation becomes —
after dividing out $e^{i\omega t}$ — a single algebraic equation:

$$\left(-\omega^2 + 2i\zeta\omega_0\omega + \omega_0^2\right)\hat X = \frac{F_0}{m}
\qquad\Longrightarrow\qquad
\hat X = \frac{F_0/m}{\omega_0^2 - \omega^2 + 2i\zeta\omega_0\omega} .$$

Write $\hat X = |\hat X|e^{-i\varphi}$ with $\varphi$ real. Then

$$x_p(t) = |\hat X|\cos(\omega t - \varphi),$$

$$|\hat X|(\omega) = \frac{F_0/m}
{\sqrt{(\omega_0^2-\omega^2)^2 + (2\zeta\omega_0\omega)^2}},
\qquad
\tan\varphi = \frac{2\zeta\omega_0\omega}{\omega_0^2-\omega^2},$$

where the **quadrant of $\varphi$ must be chosen from the sign of
$\omega_0^2-\omega^2$**, not from the ratio alone. Above resonance the response
is more than $90°$ behind the forcing; below it, less.

The **transfer function** is the dimensionless ratio $\hat X\,m\omega_0^2/F_0$,
and it is the object that instrument manufacturers publish. Section 3.4 uses
it in that form.

## 3. Derivations, step by step

### 3.1 The resonance peak, exactly

Differentiate $|\hat X|$ with respect to $\omega^2$ and set the derivative to
zero. With $u = \omega^2$,

$$\frac{d}{du}\left[( \omega_0^2-u)^2 + 4\zeta^2\omega_0^2u\right]
= -2(\omega_0^2-u) + 4\zeta^2\omega_0^2 = 0
\;\Longrightarrow\; u = \omega_0^2(1-2\zeta^2).$$

So the amplitude is maximal at

$$\boxed{\;\omega_{\text{peak}} = \omega_0\sqrt{1-2\zeta^2}
\quad\text{provided } \zeta < 1/\sqrt{2}\;}$$

If $\zeta \ge 1/\sqrt{2} \approx 0.7071$ there is no interior peak and the
response decreases monotonically from $\omega = 0$. This is testable and the
demonstration tests it: at $\zeta = 0.5$ the largest tabulated amplitude is at
$\omega = 0.707107$ with $A = 1.1547$, that being the endpoint of the search
range rather than a maximum. The demonstration's exact table shows the pattern:

| $\zeta$ | $\omega_{\text{peak}}$ | $A(\omega_{\text{peak}})$ | $A(\omega_0)$ | $1/(2\zeta)$ |
|---|---|---|---|---|
| 0.5 | 0.707107 | 1.1547 | 1.0000 | 1.0000 |
| 0.2 | 0.959166 | 2.5516 | 2.5000 | 2.5000 |
| 0.1 | 0.989949 | 5.0252 | 5.0000 | 5.0000 |
| 0.05 | 0.997497 | 10.0125 | 10.0000 | 10.0000 |
| 0.01 | 0.999900 | 50.0025 | 50.0000 | 50.0000 |
| 0.001 | 0.999999 | 500.0003 | 500.0000 | 500.0000 |

**The response at exactly $\omega_0$ is $Q = 1/(2\zeta)$ in these units to four
figures, for every row.** That is why "resonance is at $\omega_0$" is the
working rule, and why the exact shift $\sqrt{1-2\zeta^2}$ is usually ignored.
It is not always ignorable: at $\zeta = 0.5$ the shift is 29 %, and the peak
amplitude is 8 % above the response at $\omega_0$.

### 3.2 Phase, and the three special angles

From $\tan\varphi = 2\zeta\omega_0\omega/(\omega_0^2-\omega^2)$:

- **$\omega \ll \omega_0$:** $\varphi \to 0$. The response follows the force
  in phase. A mass on a stiff spring simply tracks the push.
- **$\omega = \omega_0$:** the denominator vanishes and $\tan\varphi$ is
  infinite, so $\varphi = 90°$ **exactly, for every $\zeta$.** The
  demonstration confirms this to three decimals for $\zeta = 0.5$, $0.2$ and
  $0.05$.
- **$\omega \gg \omega_0$:** $\varphi \to 180°$. The response is in
  antiphase: the system moves opposite to the force, which is how a
  mass-controlled system behaves (the mass lags the force by half a cycle).

How *fast* the phase passes through $90°$ is the sharpness of the resonance.
At $\omega/\omega_0 = 1.1$ the phase is $100.8°$ for $\zeta = 0.5$ but $152.4°$
for $\zeta = 0.05$: a high-$Q$ system has a phase that flips almost
discontinuously across a narrow band, and that steepness is what makes phase
measurements such a sensitive way to locate a resonance.

### 3.3 Bandwidth, build-up time and energy

Two derived quantities make $Q$ operational:

**Half-power bandwidth.** The amplitude falls to $1/\sqrt 2$ of its peak at the
two frequencies where the response has half the peak *power*. To first order in
$\zeta$ these sit at

$$\omega_\pm = \omega_0(1 \pm \zeta), \qquad
\frac{\Delta\omega}{\omega_0} = 2\zeta = \frac{1}{Q}.$$

The demonstration solves for the exact half-power points by bisection at
$\zeta = 0.01$ and finds $0.989849$ and $1.009851$ against the first-order
estimates $0.990000$ and $1.010000$ — a discrepancy of $1.5\times10^{-4}$ in
$\omega$, which is about 1.5 % of the half-bandwidth itself. **The rule is a
first-order-in-$\zeta$ approximation, and the demonstration measures how good
it is rather than asserting it.**

**Build-up time.** The resonant amplitude is not reached instantly. The
transient envelope grows as $1-e^{-\zeta\omega_0t}$, so the system needs

$$t_{\text{build}} \sim \frac{1}{\zeta\omega_0} = \frac{2Q}{\omega_0}
\quad\text{i.e.}\quad \frac{Q}{\pi}\ \text{cycles}$$

of forcing. At $\zeta = 0.01$ ($Q = 50$) the demonstration computes $2Q/\omega_0
= 100.0$ s, equal to $Q/\pi = 15.915$ forced cycles. **Bandwidth and build-up
time are the same statement in two domains**: a narrow resonance is both
selective in frequency and slow to establish. This is the time–bandwidth
relation in its mechanical form, and it is why a high-$Q$ seismometer takes
minutes to settle.

**Energy.** At steady resonance the energy stored in the oscillator is $Q$
times the energy injected per radian of phase. Equivalently, the amplification
of the *amplitude* at resonance is $Q$ (in the normalization above) and the
amplification of *energy* is $Q^2$. Keeping track of which quantity is being
amplified is a frequent source of factor-of-$Q$ confusion.

### 3.4 Instrument response: what a seismometer actually measures

An inertial sensor measures the motion of a proof mass relative to its frame.
For a velocity sensor with corner frequency $\omega_0$ the displacement
response, normalised so that it approaches 1 at high frequency, is

$$|H(\omega)| = \frac{\omega^2}
{\left| \omega_0^2 - \omega^2 + 2i\zeta\omega_0\omega \right|} .$$

The demonstration evaluates this and the readings are the point of the whole
section:

| $\omega/\omega_0$ | $\lvert H\rvert$, $\zeta = 0.7$ | $\lvert H\rvert$, $\zeta = 0.1$ | $(\omega/\omega_0)^2$ |
|---|---|---|---|
| 0.1 | 0.010002 | 0.010099 | 0.010000 |
| 0.2 | 0.040000 | 0.041631 | 0.040000 |
| 0.5 | 0.243685 | 0.330409 | 0.250000 |
| 1.0 | 0.714286 | 5.000000 | 1.000000 |
| 2.0 | 0.974740 | 1.321637 | 4.000000 |
| 5.0 | 1.000000 | 1.040764 | 25.000000 |
| 100.0 | 1.000002 | 1.000098 | 10000 |

Read the first two rows together. Far below the corner, $|H|$ tracks
$(\omega/\omega_0)^2$ to three figures: the instrument's output is
**proportional to ground acceleration**, not velocity, and to get velocity from
it you must integrate — which amplifies low-frequency noise. Read the last rows
together: far above the corner, $|H| = 1$ and the instrument is flat in
velocity. The corner frequency is the transition, and it is set by the sensor's
mechanical period:

$$f_c = \frac{1}{T_0}, \qquad T_0 = 120\ \mathrm{s} \Rightarrow f_c = 8.333\ \mathrm{mHz}, \qquad
T_0 = 1\ \mathrm{s} \Rightarrow f_c = 1\ \mathrm{Hz},$$

both computed in the demonstration. **This is why long-period and normal-mode
seismology needs long-period instruments.** A 1 Hz geophone is blind to the
$_0S_2$ mode at 0.31 mHz — three and a half decades below its corner — while a
120 s broadband sensor sees it as flat in velocity. Observe also that
$\zeta = 0.1$ gives $|H| = 5.0$ *at the corner*: a lightly damped sensor has a
response bump of $Q = 5$ there, and an uncorrected gain error of 500 % is not a
small mistake. Manufacturer response files exist precisely to remove this; they
are distributed with the waveform archives at
<https://ds.iris.edu/ds/nodes/dmc/>.

### 3.5 The same mathematics in a tuned receiver coil

A coil of inductance $L$, self-capacitance $C$ and resistance $R$ driven by an
alternating electromotive force obeys $Lq'' + Rq' + q/C = E(t)$, which is the
same equation with $\omega_0 = 1/\sqrt{LC}$ and $\zeta = R/(2\sqrt{L/C})$. For
$L = 10$ mH, $C = 100$ pF, $R = 25\ \Omega$ the demonstration computes
$f_0 = 159.155$ kHz, $\zeta = 0.0013$ and $Q = 400$; raising $R$ to
$400\ \Omega$ gives $Q = 25$. The first coil rings, the second does not.

**Now the important negative example.** It is tempting to describe the
electromagnetic response of conductive ground as a resonance. It is not. The
diffusion of a magnetic field into a conductor gives a response whose phase
increases with frequency toward $90°$ and never passes through it, because the
governing equation is *first order in time* (a diffusion equation), not second.
A measured curve that reaches $90°$ lag and then returns is a resonance; one
that approaches $90°$ asymptotically is diffusion. **Two superficially similar
curves, two different physics, and the discriminant is the order of the
equation in time** — which you must read off the constitutive model, not off
the plot. See
[19-08-03 Simulating EM Diffusion in Conductive Media](../../19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/03-simulate-em-diffusion.md).

## 4. Physical interpretation

**Resonance is not infinite, and the reason is the damping term.** In the
undamped case the denominator of $|\hat X|$ vanishes at $\omega = \omega_0$ and
the algebra signals a catastrophe. Physically, the amplitude instead grows
linearly in time — $x \to (t/2)\sin\omega_0t$ for the undamped case started from
rest, as
[06 Green's Functions](./06-green-functions.md) verifies numerically. Damping
bounds this growth by removing energy at a rate proportional to the square of
the velocity, and the balance between injection and removal sets the finite
amplitude $Q F_0/(m\omega_0^2)$.

**Resonance is a property of a *pair*, not of a system.** A structure does not
"have a resonance"; it has a natural frequency, and there must be a source at
that frequency for a resonance to occur. This is why site-effect amplification
in earthquake engineering depends jointly on the soil column and on the
spectrum of the incoming motion.

**Where the energy goes.** At steady state the average power delivered by the
forcing exactly equals the average power dissipated by damping; the stored
energy is constant. Off resonance, part of the delivered power goes into
changing the stored energy each cycle and is returned to the source, which is
the physical content of the phase lag.

**What breaks the model.** Three assumptions are worth naming, because each is
routinely violated in the field:

1. **Linear damping.** Rock attenuation is close to frequency-independent over
   decades of frequency, which no constant $c$ reproduces. Real attenuation is
   handled with a complex modulus or a fractional derivative, not this
   equation.
2. **A single degree of freedom.** A building, a basin or a magma chamber has
   many modes, and they couple. The single-mode response is a filter that
   happens to be first in a series.
3. **Constant coefficients.** A resonator whose stiffness changes with
   amplitude or temperature has a frequency that drifts, and a drifting
   resonance is how a damaged structure or a filling magma chamber announces
   itself.

## 5. Python demonstration

The companion script is [`code/oscillators_demo.py`](./code/oscillators_demo.py),
standard library only.

| Section | Claim being tested | Observed result |
|---|---|---|
| 1 | The resonance curve for four damping ratios | at $\omega = \omega_0$: 1.0000, 2.5000, 10.0000, 50.0000 for $\zeta = 0.5, 0.2, 0.05, 0.01$ |
| 2 | Peak location and height | $\zeta = 0.05$: peak 10.0125 at $\omega = 0.997497$ |
| 3 | The analytic amplitude is right | time-domain integration agrees to $2\times10^{-5}$ at $\omega = \omega_0$ and $4\times10^{-3}$ at $\omega = 2\omega_0$ |
| 4 | Phase is $90°$ at $\omega_0$ for any $\zeta$ | 90.000° for $\zeta = 0.5, 0.2, 0.05$ |
| 5 | Sensor response splits at the corner | $\omega/\omega_0 = 0.1$: 0.010002 vs $\omega^2$ prediction 0.010000 |
| 6 | Corner frequencies | $T_0 = 120$ s $\Rightarrow$ 8.3333 mHz; $T_0 = 1$ s $\Rightarrow$ 1000 mHz |
| 7 | Build-up time and exact half-power points | $2Q/\omega_0 = 100.0$ s $= Q/\pi = 15.9$ cycles; half-power at 0.989849 and 1.009851 |
| 8 | Tuned coil versus damped coil | $Q = 400$ at $R = 25\ \Omega$, $Q = 25$ at $R = 400\ \Omega$ |

Section 3 is the important one methodologically. The analytic amplitude is not
merely plotted; it is compared with the amplitude *measured from a time-domain
integration of the ODE itself*, after the transient has decayed. The agreement
is $2\times10^{-5}$ at resonance and $4\times10^{-3}$ far off it, and the
script attributes the difference honestly to the finite integration window and
the fixed step rather than to the formula.

> **Breaking exercise.** In Section 3, reduce the integration to 40 forced
> periods instead of 400 and predict, before running, whether the measured
> amplitude at $\zeta = 0.05$ will be too large or too small. Then check.

## 6. Exercises

Attempt these closed-book. See
[`exercises/03-oscillators-exercises.md`](./exercises/03-oscillators-exercises.md)
and the worked
[`exercises/03-oscillators-solutions.md`](./exercises/03-oscillators-solutions.md).

## 7. Common mistakes

1. **Writing $\omega_0$ where $\omega_d$ is meant, or vice versa.** The driving
   frequency is $\omega$, the natural frequency is $\omega_0$, the damped free
   frequency is $\omega_d = \omega_0\sqrt{1-\zeta^2}$, and the peak of the
   driven response is at $\omega_0\sqrt{1-2\zeta^2}$. Four different symbols,
   four different meanings.
2. **Confusing the transient with the steady state.** A measured amplitude
   taken before $2Q/\omega_0$ has elapsed is not the steady-state response.
3. **Quoting $Q$ for amplitude when the definition is about energy.** Amplitude
   amplification is $Q$; energy amplification is $Q^2$; the half-power
   bandwidth is $1/Q$. Say which you mean.
4. **Assuming a peak exists.** For $\zeta \ge 1/\sqrt{2}$ the response is
   monotone in $\omega$, and "the resonant frequency" is not defined.
5. **Ignoring the phase quadrant.** $\arctan$ returns a value in
   $(-90°,90°)$, but the true lag runs from $0°$ to $180°$ across resonance.
6. **Reading the resonance of a transducer as a property of the ground.** A
   coil or a geophone has its own resonance; only the corrected transfer
   function describes the ground.
7. **Applying the resonance formula to a diffusive response.** EM fields in a
   conductor obey a first-order-in-time equation. Section 3.5 gives the test.

## 8. Real-world applications

- **Seismometer and geophone design.** The corner frequency and damping of a
  sensor are the design variables, and the response curve is the specification.
  See [23-02-01 Seismometers](../../23-field-methods-instruments/02-seismic-instruments-and-fieldwork/01-seismometers.md).
- **Site response and earthquake engineering.** Soil columns amplify motion
  near their fundamental period; the amplification factor is $1/(2\zeta)$ with
  $\zeta$ standing for the soil's attenuation.
- **Normal-mode seismology.** The free oscillations of the Earth are standing
  waves whose spectral peaks have width $1/Q$; measuring the width gives $Q$.
  See [12-05-01 Free Oscillations of the Earth](../../12-global-geophysics-interior/05-earth-tides-rotation-global/01-free-oscillations.md).
- **Ocean and lake seiches, and well oscillations.** Enclosed water bodies and
  borehole water columns oscillate at their own periods; the amplitude at a
  given forcing frequency follows this curve.
- **Electromagnetic and IP receivers.** Transmitter and receiver coils are
  deliberately damped so that their own ringing does not contaminate the
  transient they are meant to measure.
- **Tidal and long-period gravity.** The response of a gravimeter to tidal
  forcing is an instrument response problem, and its calibration is done with
  known tidal signals.

## 9. Further reading

- **Boyce, W. E., & DiPrima, R. C. *Elementary Differential Equations and
  Boundary Value Problems.* Wiley.** The forced-oscillator chapter, with the
  amplitude–phase derivation done both by undetermined coefficients and by the
  complex method. Level: intermediate.
- **Strogatz, S. H. *Nonlinear Dynamics and Chaos.* Westview/CRC.** Chapter 7
  on limit cycles and forced oscillators puts this linear case in the context
  of what genuinely non-linear, self-excited oscillation looks like. Level:
  intermediate.
- **Aki, K., & Richards, P. G. *Quantitative Seismology.* University Science
  Books.** Attenuation, the seismic quality factor and the anelastic
  stress–strain relation. Level: graduate.
- **Havskov, J., & Ottemöller, L. *Routine Data Processing in Earthquake
  Seismology.* Springer.** The instrument-response chapter, written for
  practitioners who must remove a sensor's response from a waveform.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics.*
  Cambridge University Press.** The electromagnetic chapter, where the
  diffusive rather than resonant response of the ground is developed.
- **Thomson, W. T., & Dahleh, M. D. *Theory of Vibration with Applications.*
  Prentice Hall.** Level: intermediate. The engineering treatment of bandwidth,
  $Q$ and transmissibility in structural design.
- **Nabighian, M. N. (ed.). *Electromagnetic Methods in Applied Geophysics*,
  Vol. 1. Society of Exploration Geophysicists.** The inductive response of
  coils and of the half-space, and why the two must not be confused.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted
> text, and you should confirm current editions and availability through your
> library before citing them yourself.

## 10. Related lessons

- [02 Second-Order Linear ODEs and Characteristic Equations](./02-second-order-linear.md) —
  the undriven equation whose roots supply $\omega_0$, $\omega_d$ and $\zeta$.
- [06 Green's Functions and Impulse Response](./06-green-functions.md) — the
  response to an impulse, from which the response to any forcing follows by
  convolution; the linear-growth-at-resonance calculation is verified there.
- [07 Stiff Systems and Numerical Stability Challenges](./07-stiff-systems.md) —
  what happens when an oscillator's damping is so large that explicit
  time-stepping becomes impractical.
- [02-03-02 Damped and Driven Oscillations, Resonance and Quality Factor](../../02-physics/03-oscillations-and-waves/02-damped-driven.md) —
  the physics treatment of the same equation.
- [02-03-10 Attenuation, Absorption and the Quality Factor Q](../../02-physics/03-oscillations-and-waves/10-attenuation.md) —
  $Q$ as a property of rock.
- [20-signal-processing](../../20-signal-processing/README.md) — deconvolution
  and instrument-response removal as a filtering problem.
- [01-10-02 The Fourier Transform and Its Properties](../10-fourier-analysis/02-fourier-transform.md) —
  why the transfer function is the Fourier transform of the impulse response.

## Self-assessment checklist

- [ ] I can write the driven oscillator equation and split its solution into
      transient and steady state. (Section 2.1)
- [ ] I can derive the complex amplitude $\hat X$ and read the amplitude and
      phase off it. (Section 2.2)
- [ ] I can derive $\omega_{\text{peak}} = \omega_0\sqrt{1-2\zeta^2}$ and say
      when no peak exists. (Section 3.1)
- [ ] I can explain why the phase is exactly $90°$ at $\omega_0$ for every
      $\zeta$. (Section 3.2)
- [ ] I can relate $Q$ to the half-power bandwidth, to the build-up time and to
      the amplitude at resonance, and state the normalization.
      (Sections 3.3, Section 7.3)
- [ ] I can read an instrument-response curve and say whether it is flat in
      velocity or in acceleration at a given frequency. (Section 3.4)
- [ ] I can distinguish a resonant response from a diffusive one, and name the
      test. (Section 3.5)
- [ ] I can name three assumptions this model makes that field data violate.
      (Section 4)
