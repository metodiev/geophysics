---
id: 01-08-02
title: "Second-Order Linear ODEs and Characteristic Equations"
level: intermediate
prereqs: ["01-08-01", "01-05-03"]
estimated_minutes: 90
tags: [ordinary-differential-equations, second-order, characteristic-equation, damping, oscillators]
---

# Second-Order Linear ODEs and Characteristic Equations

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the general constant-coefficient second-order linear ODE in
   standard form and explain why two independent solutions — and therefore two
   initial conditions — are needed.
2. **Substitute** the trial solution $e^{rt}$ and derive the characteristic
   equation, rather than quoting it.
3. **Classify** the three cases (real distinct, repeated, complex conjugate
   roots) and write the general solution in each, including why the repeated
   root needs a factor of $t$.
4. **Translate** roots into physical quantities: frequency, decay rate, damped
   frequency $\omega_d$, quality factor $Q$, and logarithmic decrement $\delta$.
5. **Set up and solve** the damped oscillator for a spring-supported gravimeter,
   a buoyancy oscillation in a stratified fluid, and a free oscillation of the
   Earth, and explain which features of the mathematics correspond to which
   observable.
6. **Verify** any claimed solution by substituting it back into the ODE
   numerically, and explain why that check is stronger than a plot.

## Prerequisites

- [01 First-Order ODEs: Separation of Variables and Integrating Factors](./01-first-order-odes.md) —
  the exponential solution and the use of an initial condition.
- [01-05-03 Differentiation Rules and Implicit Differentiation](../05-single-variable-calculus/03-differentiation-rules.md) —
  the derivatives of $e^{rt}$, $\sin$ and $\cos$ used throughout.
- [01-02-03 Exponentials, Logarithms and Decay Laws](../02-algebra/03-exponentials-logarithms.md) —
  exponential growth and decay, and the meaning of a rate constant.

## 1. Intuition: inertia plus a restoring force

A first-order equation needs one number to pin down its solution because it
contains one integration constant. A second-order equation contains two, so it
needs two conditions: typically a position and a velocity at the initial time.
The physics behind that extra constant is **inertia**. A body with mass obeys
Newton's second law, $F = ma = m x''$, and a restoring force pulls it back
toward equilibrium. With a spring or a buoyancy force the restoring force is
proportional to displacement, and the equation of motion is

$$m x'' = -k x \qquad\text{(undamped)}$$

or, with a linear damping force $-c x'$ (viscous drag, or the resistance of a
lubricated bearing),

$$m x'' + c x' + k x = 0.$$

Dividing by $m$ puts it in the canonical form used in this lesson,

$$\boxed{\;x'' + 2\zeta\omega_0 x' + \omega_0^2 x = 0\;}, \qquad
\omega_0 = \sqrt{\frac{k}{m}}, \qquad
\zeta = \frac{c}{2\sqrt{km}} .$$

Two parameters, $\omega_0$ and $\zeta$, capture everything. That is a
remarkable compression: the mass of a gravimeter's proof mass, the stiffness of
its spring and the viscosity of its damping oil all collapse into one frequency
and one dimensionless number.

The single most useful thing to know before any algebra: **$\omega_0$ sets the
timescale and $\zeta$ decides the character.** Dividing the equation by
$\omega_0^2$ shows that $1/\omega_0$ is the only time in the problem, so the
solution can depend on time only in the combination $\omega_0 t$. The quantity
$\zeta$ is dimensionless and therefore cannot be scaled away; it is the only
knob that changes the *shape* of the response.

## 2. The characteristic equation, derived

Propose the trial solution $x(t) = e^{rt}$ with $r$ a constant to be found.
Then $x' = re^{rt}$ and $x'' = r^2e^{rt}$, and substituting into the ODE gives

$$r^2e^{rt} + 2\zeta\omega_0 r e^{rt} + \omega_0^2 e^{rt} = 0 .$$

Since $e^{rt}$ never vanishes, it divides out, leaving the **characteristic
equation**

$$\boxed{\;r^2 + 2\zeta\omega_0\,r + \omega_0^2 = 0\;}
\qquad\Longrightarrow\qquad
r = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}.$$

Two remarks, because both matter later:

- **Why the trial works.** The operator $x \mapsto x'' + 2\zeta\omega_0x' + \omega_0^2x$
  is linear, and $e^{rt}$ is its eigenfunction: differentiating it returns a
  multiple of itself. The whole method is a search for eigenfunctions of a
  differential operator, and the same idea reappears in
  [04 Systems of ODEs](./04-systems-of-odes.md) and in
  [05 Sturm–Liouville Theory](./05-sturm-liouville.md).
- **Why it is a quadratic.** Second-order constant coefficients give a
  quadratic whose two roots supply exactly the two integration constants.

The **discriminant** of the characteristic equation is $\omega_0^2(\zeta^2-1)$,
so the sign of $\zeta - 1$ partitions the problem into three cases. It is worth
naming the boundary before writing any solutions: $\zeta = 1$ is **critical
damping**, $\zeta < 1$ is **underdamped**, $\zeta > 1$ is **overdamped**.

### 2.1 Case 1: overdamped, $\zeta > 1$

The roots are real and distinct: $r_{1,2} = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2-1}$,
both negative (their sum is $-2\zeta\omega_0 < 0$ and their product is
$\omega_0^2 > 0$, so both have the same sign, and that sign is negative).
The general solution is

$$x(t) = C_1e^{r_1t} + C_2e^{r_2t}.$$

There is no oscillation: the two exponentials decay at different rates and the
slower one eventually dominates. For $\zeta = 2$ and $\omega_0 = 1$ the roots
are $-0.267949$ and $-3.732051$ — a *fast* mode that dies in about a third of a
time unit and a *slow* mode that takes nearly four. **An overdamped instrument
is slow, and the slowness is the slow root's, not the fast one's.**

### 2.2 Case 2: critically damped, $\zeta = 1$

The roots coincide at $r = -\omega_0$. One solution is $e^{-\omega_0t}$;
the second must be linearly independent, and $te^{-\omega_0t}$ is:

$$x(t) = (C_1 + C_2t)\,e^{-\omega_0t}.$$

Dividing the equation by $(r+\omega_0)^2$ shows why: the operator factors as
$(\tfrac{d}{dt}+\omega_0)^2$, and the second solution of a repeated-root
problem always carries a factor of $t$. **The factor of $t$ is not a technical
detail.** It is the reason critical damping is the fastest non-oscillatory
return to rest: any faster and the system would overshoot, any slower and the
exponential is too broad.

### 2.3 Case 3: underdamped, $\zeta < 1$

Write the roots as $r = -\zeta\omega_0 \pm i\omega_d$ with

$$\omega_d = \omega_0\sqrt{1-\zeta^2}.$$

Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ turns the complex
exponentials into real ones, and the general solution is

$$x(t) = e^{-\zeta\omega_0 t}\left(A\cos\omega_d t + B\sin\omega_d t\right).$$

The motion is an oscillation at the **damped frequency** $\omega_d$ inside a
decaying envelope $e^{-\zeta\omega_0t}$. Three quantities follow immediately
and are the ones geophysicists actually measure:

$$\text{decay time } \tau_{\text{decay}} = \frac{1}{\zeta\omega_0}, \qquad
\delta = \frac{2\pi\zeta}{\sqrt{1-\zeta^2}}, \qquad
Q = \frac{\omega_0}{2\zeta\omega_0} = \frac{1}{2\zeta}.$$

Here $\delta$ is the **logarithmic decrement**: the natural logarithm of the
ratio of successive peak amplitudes. Since successive peaks are one damped
period $T_d = 2\pi/\omega_d$ apart, the envelope ratio is
$e^{\zeta\omega_0 T_d}$, whose logarithm is exactly $\delta$. And $Q$ is the
**quality factor**, defined physically as (energy stored)/(energy lost per
radian). For the equation as written, $Q = 1/(2\zeta)$.

## 3. Derivations, step by step

### 3.1 From roots to the general solution, with the constants fixed

Take $\zeta = 0.2$, $\omega_0 = 1$, $x(0) = 1$, $x'(0) = 0$. The roots are
$-0.2 \pm 0.979795897i$, so $\omega_d = 0.979795897$ and

$$x(t) = e^{-0.2t}\left(A\cos(0.979795897\,t) + B\sin(0.979795897\,t)\right).$$

Imposing $x(0)=1$ gives $A = 1$. Differentiating,

$$x'(t) = e^{-0.2t}\left[(B\omega_d - 0.2A)\cos\omega_d t
- (A\omega_d + 0.2B)\sin\omega_d t\right],$$

so $x'(0) = B\omega_d - 0.2 = 0 \Rightarrow B = 0.2/0.979795897 = 0.2041241$.
The solution is therefore
$x = e^{-0.2t}(\cos 0.9798t + 0.2041\sin 0.9798t)$, which at $t=1$ equals
$0.594966233$ — the value printed by the demonstration.

The general recipe in all three cases is the same:

1. Form the characteristic equation and find its roots.
2. Write the general solution appropriate to the case.
3. Impose $x(0)$ and $x'(0)$, which for the underdamped case means a $2\times2$
   linear system in $A$ and $B$.

Step 3 is the one that goes wrong most often, and the reason is simple: the
amplitude $A$ alone is not enough information. A system released from rest and
a system launched with a velocity have the same $\omega_0$ and $\zeta$ and
different solutions.

### 3.2 The logarithmic decrement, verified

With $\zeta = 0.2$, the predicted logarithmic decrement is

$$\delta = \frac{2\pi(0.2)}{\sqrt{1-0.04}} = \frac{1.25663706}{0.97979590} = 1.28254983 .$$

The demonstration measures the ratio of successive peaks numerically and gets
$3.605822248$ for every pair, with $\ln(3.605822248) = 1.282549830$. **The
agreement is exact because it is an identity, not an approximation** — but it
is worth measuring, because the same measurement applied to field data is how
$Q$ is estimated from a seismogram or a free-oscillation recording.

Two useful conversions, both exact:

$$Q = \frac{1}{2\zeta}, \qquad
\delta = \frac{2\pi}{\sqrt{4Q^2-1}} \approx \frac{\pi}{Q}
\quad\text{for } Q \gg 1 .$$

The approximation $\delta \approx \pi/Q$ is the working form used in
seismology, and the demonstration shows why it is allowed: for $Q = 1/(2\zeta)$
with $\zeta = 10^{-3}$, $Q = 500$ and $2\pi/\sqrt{4Q^2-1} = 0.0062833$ against
$\pi/Q = 0.0062832$ — agreement to seven figures.

### 3.3 Continuous passage through $\zeta = 1$

The three cases look like different formulas, but the solution is a continuous
function of $\zeta$. The demonstration evaluates $x(1)$ at
$\zeta = 0.999999$, $1.0$ and $1.000001$ and obtains

$$0.735758759716, \qquad 0.735758882343, \qquad 0.735759004969 .$$

The outer two differ from the middle one by about $1.2\times10^{-7}$ — the
seventh decimal — for a change in $\zeta$ of one part in $10^{6}$. **The three
cases are one solution seen in three coordinate systems, not three unrelated
problems.** This matters when a numerical model is near $\zeta = 1$: a code
that branches on $\zeta < 1$ and uses the $\zeta > 1$ formula otherwise can
produce a visible glitch unless the branch is handled with care, because the
parameterisation through $\sqrt{1-\zeta^2}$ is not smooth at the transition.

### 3.4 A gravimeter, from equation to specification

Take $m = 0.05$ kg and choose the spring so that the natural period is 1 s:
$k = m\omega_0^2$ with $\omega_0 = 2\pi$ gives $k = 1.9739$ N/m. Then compare
damping choices:

| $\zeta$ | $c$ (N s/m) | free-decay time from the slow root (s) | six e-foldings (s) |
|---|---|---|---|
| 0.1 | 0.062832 | 1.5915 | 9.55 |
| 0.7 | 0.439823 | 0.2274 | 1.36 |
| 5.0 | 3.141593 | 1.5755 | 9.45 |

Read the table as an engineer. Reducing $\zeta$ from 0.7 to 0.1 makes the
instrument ring for ten seconds; raising it to 5 makes it *slow again*, because
the slow root of an overdamped system approaches zero as
$\zeta \to \infty$:

$$r_{\text{slow}} = -\omega_0\left(\zeta - \sqrt{\zeta^2-1}\right)
\;\xrightarrow[\zeta\to\infty]{}\; -\frac{\omega_0}{2\zeta} .$$

So the free-decay time is minimized near critical damping, which is
$\sqrt{2}$ times faster than either a ten-times more damped or a ten-times less
damped instrument. **"More damping is safer" is wrong, and the reason is in
the roots.**

### 3.5 Buoyancy oscillation in a stratified fluid

A fluid parcel displaced vertically by $z$ in a stably stratified environment
experiences a restoring buoyancy force and obeys

$$\frac{d^2z}{dt^2} = -N^2 z, \qquad
N^2 = -\frac{g}{\rho}\frac{d\rho}{dz} > 0 ,$$

so $\omega_0 = N$, the **Brunt–Väisälä frequency**, and the oscillation period
is $2\pi/N$. With $N = 0.01$ rad/s the period is 628.32 s, i.e. **10.47
minutes**. That is a physically meaningful number in the ocean: internal
waves with periods of tens of minutes are the standard signature of a
stratified water column, and a surface-wave or seismic measurement can pick
them up as noise. Note what the equation assumes: **no damping and no
background shear.** With shear the oscillation couples to the mean flow, the
operator is no longer self-adjoint, and instability (Kelvin–Helmholtz) becomes
possible — none of which this equation can show.

### 3.6 Free oscillations of the Earth

A normal mode of the Earth obeys the same mathematics with $\omega_0$ equal to
the mode's eigenfrequency. The longest-period fundamental spheroidal mode,
$_0S_2$, is commonly tabulated near $3.2\times10^3$ s (about 54 min) and the
radial mode $_0S_0$ near $1.2\times10^3$ s (about 20 min); the eigenperiods
depend on the Earth model, so treat them as order-of-magnitude anchors rather
than constants. The demonstration converts them to angular frequency and, for
a representative mantle $Q$ of a few hundred, to a decay envelope. With
$Q = 300$ and $T = 3233$ s the amplitude envelope decays with time constant
$2Q/\omega_0 = 3.09\times10^5$ s, about 3.6 days. That is why the 2004 Sumatra
event's gravest modes were still measurable for weeks: **$Q$ near 300 means
hundreds of oscillations, not tens.**

## 4. Physical interpretation

**The three cases in one picture.** Trace what happens as $\zeta$ increases
from 0. The undamped system oscillates forever; adding damping makes the
envelope decay; at $\zeta = 1$ the oscillation period has stretched to
infinity; beyond it, two real decay rates replace the oscillation. Nothing is
discontinuous — the frequency simply reaches zero and becomes imaginary, at
which point the mathematics replaces $e^{\pm i\omega t}$ with
$e^{\pm|\omega|t}$ and the oscillation becomes two exponentials.

**Which regime does nature use?**

| System | Typical $\zeta$ | Consequence |
|---|---|---|
| Seismic normal mode, mantle $Q \sim 300$ | $1/(2Q) \sim 1.7\times10^{-3}$ | hundreds of visible oscillations |
| Ocean buoyancy oscillation | small | tens of periods |
| Instrument designed for reading | $0.5$–$0.7$ | fast settling without ringing |
| Instrument badly designed | $\gg 1$ | sluggish, drifting zero |
| Dry friction-dominated mechanism | $\gg 1$ | dead-beat, no overshoot |

**Energy bookkeeping.** Multiply the ODE by $x'$ and integrate:

$$\frac{d}{dt}\left[\tfrac12 m x'^2 + \tfrac12 k x^2\right] = -c\,x'^2 \le 0 .$$

The bracket is the mechanical energy, and the right-hand side is negative
definite: **a linear damping term can only remove energy, never add it.** With
$c < 0$ the same algebra gives growth, which is how a negative-resistance
oscillator (a squealing bearing, a self-excited flute) is modelled. Whether
$c$ is positive is a physical question, not a mathematical one.

**What the equation cannot say.** $x'' + 2\zeta\omega_0x' + \omega_0^2x = 0$ is
*linear*: it assumes the restoring force is exactly proportional to
displacement. Real gravimeter springs are non-linear at large extension, real
sediments are non-linear at large strain, and real damping in rocks is not
viscous — it is close to frequency-independent over a wide band, which no
constant $c$ can reproduce. The constant-coefficient model is the local,
small-amplitude approximation, and its validity must be established
separately. This is exactly the linearisation error analysis of
[01-05-04 Taylor Series and Linearisation](../05-single-variable-calculus/04-taylor-series.md).

## 5. Python demonstration

The companion script is
[`code/second_order_linear_demo.py`](./code/second_order_linear_demo.py);
it uses only the standard library.

| Section | Claim being tested | Observed result |
|---|---|---|
| 1 | The discriminant separates the three cases | $\zeta=0.2$: $-0.2\pm0.979796i$; $\zeta=1$: $-1,-1$; $\zeta=2$: $-0.267949,-3.732051$ |
| 2 | Closed forms satisfy the ODE | residuals $\le 2.2\times10^{-10}$ over all three regimes (the stencil's round-off floor) |
| 3 | Log decrement equals the peak ratio's logarithm | every successive ratio is $3.605822248$, $\ln = 1.282549830$ |
| 4 | $Q = 1/(2\zeta)$ and $Q/\pi$ cycles per e-folding | $\zeta = 10^{-3}\Rightarrow Q = 500$, 159.2 cycles |
| 5 | Overdamping is slow | 0.2274 s at $\zeta=0.7$, but 1.5755 s at $\zeta=5$ |
| 6 | Buoyancy period from $N$ | $N = 0.01$ rad/s $\Rightarrow$ 10.47 min |
| 7 | Mode periods to $Q$ | $_0S_2$: 53.88 min, $Q=300 \Rightarrow$ 3.57 d envelope |
| 8 | The solution is continuous through $\zeta=1$ | $x(1)$ agrees to 8 decimals across $\zeta = 1$ |

Section 2 deserves a comment on method. Instead of plotting the solution and
saying it "looks right", the script *substitutes* the closed form back into the
left-hand side of the ODE using a fourth-order finite-difference stencil, and
reports the residual. A residual of $10^{-10}$ is six orders below the size of
the terms being cancelled, which is what a successful check looks like. The
residual is *not* zero because the stencil is not exact: read it as the
precision of the test, not as an error in the solution.

> **Breaking exercise.** Change $\zeta$ to $1.0000001$ in Section 2 and to
> $0.9999999$. Predict whether the two residuals will differ in magnitude more
> than the values of $x$ do, and then check.

## 6. Exercises

Attempt these closed-book. See
[`exercises/02-second-order-linear-exercises.md`](./exercises/02-second-order-linear-exercises.md)
and the worked
[`exercises/02-second-order-linear-solutions.md`](./exercises/02-second-order-linear-solutions.md).

## 7. Common mistakes

1. **Using one initial condition for a second-order equation.** Two constants,
   two conditions. Position alone is not enough.
2. **Forgetting the factor of $t$ at a repeated root.** Writing
   $x = C_1e^{rt} + C_2e^{rt}$ at $\zeta = 1$ gives only one independent
   solution.
3. **Confusing $\omega_0$ with $\omega_d$.** They differ by
   $\sqrt{1-\zeta^2}$, which is 1 % at $\zeta = 0.1$ and 11 % at
   $\zeta = 0.5$. For high-$Q$ systems the distinction is negligible; for an
   instrument at $\zeta \approx 0.5$ it is not.
4. **Writing $Q = 1/(2\zeta)$ for a differently normalised equation.** That
   identity holds for $x'' + 2\zeta\omega_0x' + \omega_0^2x = 0$. If the
   damping term is written $+\gamma x'$, then $\zeta = \gamma/(2\omega_0)$ and
   $Q = \omega_0/\gamma$. Check the normalisation before using a memorised
   formula.
5. **Assuming damping always slows the system down.** For $\zeta > 1$ the
   slow root *does* slow it; for $0 < \zeta < 1$ the period lengthens only
   slightly. The instruction "add damping to settle faster" is right only up
   to $\zeta = 1$.
6. **Reading a decay rate off the amplitude instead of the energy.** A
   seismologist's $Q$ is defined on energy, which is why it is $1/(2\zeta)$
   and not $1/\zeta$.
7. **Trusting the linear model outside its range.** Large-amplitude behaviour
   in real springs, soils and magma is non-linear and no value of $\zeta$
   fixes it.

## 8. Real-world applications

- **Gravimeters and seismometers.** The proof mass, spring and damping of a
  relative gravimeter are chosen by the trade-off in Section 3.4. See
  [07-01-05 Gravity Units and Instruments](../../07-gravity-geodesy/01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md)
  and [23-02-01 Seismometers](../../23-field-methods-instruments/02-seismic-instruments-and-fieldwork/01-seismometers.md).
- **Normal modes and free oscillations.** The eigenperiods and $Q$ values of
  the modes governed by this equation are the primary constraints on the
  Earth's radial structure. See
  [12-05-01 Free Oscillations of the Earth (Normal Modes)](../../12-global-geophysics-interior/05-earth-tides-rotation-global/01-free-oscillations.md).
- **Buoyancy oscillations and internal waves.** The Brunt–Väisälä frequency of
  Section 3.5 is the frequency of internal gravity waves, and it appears in
  oceanography, atmospheric science and lake physics alike.
- **Seismic attenuation.** $Q$ measured from the decay of a wave train or a
  mode is a rock property that depends on temperature, fluid content and
  strain amplitude.
- **Spring and buoyancy supports in instrumentation.** Tiltmeters, spring
  gravimeters and floating platforms are all designed by choosing
  $(\omega_0,\zeta)$.
- **Reservoir-induced and volcanic seismicity** uses the same oscillator
  response to infer the geometry of a source from the frequency of its
  oscillations (long-period and very-long-period events).

## 9. Further reading

- **Boyce, W. E., & DiPrima, R. C. *Elementary Differential Equations and
  Boundary Value Problems.* Wiley.** Chapter 3 is the canonical treatment of
  the three cases, with the repeated-root argument done properly. Level:
  intermediate.
- **Bender, C. M., & Orszag, S. A. *Advanced Mathematical Methods for
  Scientists and Engineers.* Springer.** The chapters on constant-coefficient
  equations and on boundary-layer behaviour explain the $\zeta \to 1$ limit
  from a more advanced viewpoint. Level: advanced.
- **Strogatz, S. H. *Nonlinear Dynamics and Chaos.* Westview/CRC.** The early
  chapters, even though they are about non-linear systems, contain the clearest
  treatment of damping, energy and the transition from oscillation to
  exponential decay. Level: intermediate.
- **Aki, K., & Richards, P. G. *Quantitative Seismology.* University Science
  Books.** The sections on attenuation and $Q$. Level: graduate.
- **Lay, T., & Wallace, T. C. *Modern Global Seismology.* Academic Press.** The
  free-oscillation and instrument-response chapters map the quantities of
  Section 3.6 onto observed spectra. Level: graduate.
- **Torge, W. *Gravimetry.* de Gruyter.** Instrument design and the damping
  trade-offs of Section 3.4, at the level of a working gravimetrist.
- **Turcotte, D. L., & Schubert, G. *Geodynamics.* Cambridge University
  Press.** Buoyancy oscillations, Rayleigh–Taylor instabilities and the
  stratification arguments that decide when the oscillation model is admissible.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted
> text, and you should confirm current editions and availability through your
> library before citing them yourself.

## 10. Related lessons

- [01 First-Order ODEs: Separation of Variables and Integrating Factors](./01-first-order-odes.md) —
  the one-parameter case this lesson generalises.
- [03 Damped and Driven Oscillators as Physical Models](./03-oscillators.md) —
  what happens when a forcing term is added to this equation.
- [04 Systems of ODEs, Phase Portraits and Stability](./04-systems-of-odes.md) —
  the same roots, written as eigenvalues of a matrix.
- [05 Sturm–Liouville Theory and Eigenfunction Expansions](./05-sturm-liouville.md) —
  the boundary-value version, where the "frequency" is an eigenvalue.
- [01-09-03 The Wave Equation and Its Physical Content](../09-partial-differential-equations/03-wave-equation.md) —
  where a continuum of oscillators replaces a single one.
- [02-03-01 Simple Harmonic Motion](../../02-physics/03-oscillations-and-waves/01-simple-harmonic-motion.md)
  and [02-03-02 Damped and Driven Oscillations](../../02-physics/03-oscillations-and-waves/02-damped-driven.md) —
  the physics course's parallel treatment.
- [02-03-10 Attenuation, Absorption and the Quality Factor Q](../../02-physics/03-oscillations-and-waves/10-attenuation.md) —
  $Q$ as a rock property rather than an abstract number.

## Self-assessment checklist

- [ ] I can derive the characteristic equation from the trial $e^{rt}$ without
      quoting it. (Section 2)
- [ ] I can write the general solution in all three cases, including the
      repeated root. (Sections 2.1–2.3)
- [ ] I can fix both constants from $x(0)$ and $x'(0)$, and I know why one
      condition is not enough. (Section 3.1)
- [ ] I can convert between $\zeta$, $\omega_d$, $\delta$ and $Q$, and state
      the normalisation I am assuming. (Sections 2.3, 3.2, Section 7.4)
- [ ] I can explain why the free-decay time is minimised near $\zeta = 1$.
      (Section 3.4)
- [ ] I can compute a buoyancy period from $N$ and say what the equation
      neglects. (Section 3.5)
- [ ] I can turn a mode period and a $Q$ into a decay time. (Section 3.6)
- [ ] I can verify a claimed solution by substituting it into the ODE and
      interpreting the residual as a test precision. (Section 5)
