---
id: 01-11-01
title: "Complex Numbers, Polar Form and Argand Diagrams"
level: intermediate
prereqs: ["01-03-05", "01-05-02"]
estimated_minutes: 90
tags: [complex-numbers, phasors, impedance, argand-diagram]
---

# Complex Numbers, Polar Form and Argand Diagrams

## Learning objectives

By the end of this lesson you will be able to:

1. **Perform** addition, multiplication, division and conjugation in
   rectangular and in polar form, and convert between them without losing
   track of the branch of the argument.
2. **Read** a complex number as an instruction — scale by the modulus, rotate by
   the argument — and use that reading to multiply and divide by inspection.
3. **Represent** a sinusoid as a phasor, add and scale phasors, and recover the
   amplitude and phase of the sum without a trigonometric identity.
4. **Write** the impedance of a series circuit or a damped oscillator as a
   complex number, and read its modulus and argument as the steady-state
   amplitude and phase.
5. **Recognise** the Argand diagram as a map of a physical quantity, and state
   where the principal branch of the argument is discontinuous and why that
   matters.
6. **Verify** a phasor result against a direct time-domain simulation, and say
   what the residual measures.

## Prerequisites

[01-03-05 Phase and Harmonics](../03-trigonometry/05-phase-and-harmonics.md) —
sinusoids written as amplitude and phase, and the addition of two sinusoids of
the same frequency;
[01-05-02 Derivatives](../05-single-variable-calculus/02-derivatives.md) —
because the time derivatives of $\cos\omega t$ and $\sin\omega t$ are what turn
a differential equation into an algebraic one in later sections.

## 1. Intuition: the square root of minus one is a bookkeeping device

Geophysics measures oscillations. Ground motion, tidal height, an
electromagnetic field in a magnetotelluric survey, the potential of a
gravitating body — all of them are described by a number that varies sinusoidally
and a *lag*: an amplitude and a phase. Writing

$$a\cos(\omega t) + b\sin(\omega t)$$

carries two numbers ($a$ and $b$) that are not the two numbers a physicist wants.
The quantities a physicist wants are

$$A = \sqrt{a^{2}+b^{2}}, \qquad \phi, \quad\text{such that}\quad
a\cos\omega t + b\sin\omega t = A\cos(\omega t - \phi),$$

where $A$ is the **amplitude** and $\phi$ is the **phase lag**. Converting
between $(a,b)$ and $(A,\phi)$ by hand is an exercise in trigonometric
identities, and adding three or four such oscillations by hand is unbearable —
but it is exactly what a seismic array, a set of tidal constituents or a
multi-loop electromagnetic sounding requires.

Complex numbers remove the trigonometry. Define $z = a + ib$ and read it as the
pair $(\text{amplitude}, \text{phase})$: the modulus $|z| = A$ and the argument
$\arg z = \phi$. Then:

- adding two sinusoids of the same frequency is **adding two complex numbers**;
- scaling a sinusoid is multiplying a modulus;
- shifting a sinusoid in time is adding to an argument;
- differentiating a sinusoid is multiplying by $i\omega$.

The last of those four is the one that pays. It turns the differential equations
of [01-08 Ordinary Differential
Equations](../08-ordinary-differential-equations/README.md) and
[02-03 Oscillations and
Waves](../../02-physics/03-oscillations-and-waves/README.md) into algebra, and it
is why every instrument response in geophysics is quoted as a complex function
of frequency.

> **A warning about what is physical.** A complex number is not a measurement.
> The physical signal is the real part of the complex expression, and the
> convention for which part that is (and whether the exponent is $+i\omega t$ or
> $-i\omega t$) must be stated. This lesson uses $e^{-i\omega t}$, so that
> $\cos\omega t = \operatorname{Re} e^{-i\omega t}$ and a wave travelling in the
> $+x$ direction is $e^{i(kx-\omega t)}$.

## 2. The field $\mathbb{C}$ and its arithmetic

### 2.1 Definition

A complex number is an ordered pair of real numbers written

$$z = x + iy, \qquad x = \operatorname{Re} z, \quad y = \operatorname{Im} z,
\qquad i^{2} = -1 .$$

The set of all such $z$ is $\mathbb{C}$. The two laws that define it are

$$(x_{1}+iy_{1}) + (x_{2}+iy_{2}) = (x_{1}+x_{2}) + i(y_{1}+y_{2}),$$

$$(x_{1}+iy_{1})(x_{2}+iy_{2}) = (x_{1}x_{2}-y_{1}y_{2}) +
i(x_{1}y_{2}+y_{1}x_{2}),$$

and division is defined through the **complex conjugate** $\bar z = x - iy$:

$$\frac{z_{1}}{z_{2}} = \frac{z_{1}\bar z_{2}}{z_{2}\bar z_{2}}
= \frac{z_{1}\bar z_{2}}{|z_{2}|^{2}}, \qquad |z|^{2} = z\bar z = x^{2}+y^{2}.$$

The identity $z\bar z = |z|^{2}$ is worth memorising: it converts a complex
division into a real division, and it is the reason complex arithmetic can be
done by hand with no more machinery than real arithmetic.

### 2.2 The four facts that make $\mathbb{C}$ useful

| Operation | Rectangular form | Polar form |
|---|---|---|
| Conjugation | $x - iy$ | same modulus, negated argument |
| Modulus | $\sqrt{x^{2}+y^{2}}$ | $r$ |
| Multiplication | expand and use $i^{2}=-1$ | $r_{1}r_{2}\,e^{i(\theta_{1}+\theta_{2})}$ |
| Division | rationalise by the conjugate | $(r_{1}/r_{2})\,e^{i(\theta_{1}-\theta_{2})}$ |

The polar column is the reason the polar form exists: multiplication is
rotation and scaling, with no algebra at all. Contrast the two readings of
$(2e^{i\pi/6})(3e^{i\pi/4})$: in the polar column the answer $6e^{i5\pi/12}$ is
immediate; in the rectangular column it is a page of sines and cosines.

### 2.3 Polar form, Euler's formula, and the branch of the argument

Every $z \neq 0$ can be written

$$z = r e^{i\theta}, \qquad r = |z| > 0, \qquad \theta = \arg z \in \mathbb{R},$$

with $\theta$ determined only up to $2\pi k$. The **principal value**
$\operatorname{Arg} z \in (-\pi,\pi]$ is the representative chosen by every
library function: `cmath.phase`, `atan2`, `arg`. Because the interval is
half-open, $\operatorname{Arg}$ jumps by $2\pi$ across the negative real axis
and is **discontinuous there**:

$$\operatorname{Arg}\,(-1 - 0^{+}i) \to -\pi, \qquad
\operatorname{Arg}\,(-1 + 0^{+}i) \to +\pi .$$

That jump is not a curiosity. A phase spectrum that is plotted without
unwrapping, a seismic trace whose instantaneous phase crosses $\pm\pi$, and a
transfer-function fit whose phase residual does an unexplained $2\pi$ hop are
all the same phenomenon. The convention in this repository is to report wrapped
phases in $(-\pi,\pi]$ only when the range is stated, and to unwrap whenever a
phase is differentiated or interpolated.

Euler's formula connects the two forms:

$$e^{i\theta} = \cos\theta + i\sin\theta, \qquad\text{hence}\qquad
\cos\theta = \operatorname{Re}e^{i\theta}, \qquad
\sin\theta = \operatorname{Im}e^{i\theta}.$$

Both follow from the Taylor series of $e^{i\theta}$, $\cos$ and $\sin$, so no new
analysis is needed: the identity is a statement about power series, and its
geometric content is that the exponential of an imaginary number moves you round
the unit circle.

### 2.4 De Moivre, powers and roots

Raising to a power is multiplying arguments, which gives **De Moivre's
theorem**:

$$\bigl(r e^{i\theta}\bigr)^{n} = r^{n} e^{in\theta}, \qquad n \in \mathbb{Z}.$$

The converse is that every nonzero $z = re^{i\theta}$ has exactly $n$ distinct
$n$-th roots,

$$z^{1/n} = r^{1/n}\exp\!\left(i\frac{\theta + 2\pi k}{n}\right),
\qquad k = 0, 1, \dots, n-1,$$

which are the vertices of a regular $n$-gon of radius $r^{1/n}$ centred on the
origin. The special case $z=1$ gives the **roots of unity**
$w_{k} = e^{2\pi i k/n}$, whose sum is zero:

$$\sum_{k=0}^{n-1} w_{k} = \frac{1-w^{n}}{1-w} = 0 \qquad (w \neq 1).$$

That zero is the discrete Fourier transform's orthogonality relation in
disguise, and it is why a transform of a constant has energy only in the
zero-frequency bin ([01-10-01 Fourier
Series](../10-fourier-analysis/01-fourier-series.md)).

## 3. Phasors: amplitude and phase, without trigonometry

### 3.1 The representation

Let an oscillation of angular frequency $\omega$ be written

$$a\cos(\omega t) + b\sin(\omega t)
= \operatorname{Re}\bigl[(a + ib)e^{-i\omega t}\bigr]
= \operatorname{Re}\bigl[Z e^{-i\omega t}\bigr],$$

with $Z = a + ib$ the **complex amplitude**, or **phasor**. Equivalently, if the
oscillation is $A\cos(\omega t - \phi)$, then

$$Z = A e^{-i\phi}, \qquad A = |Z|, \qquad \phi = -\arg Z .$$

The phasor carries the two pieces of information that survive after the common
factor $e^{-i\omega t}$ is factored out. Nothing is lost, and the time
dependence never has to be written.

### 3.2 The addition theorem, verified

The sum of two oscillations of the same frequency is a single oscillation of
that frequency, because

$$\operatorname{Re}\bigl[Z_{1}e^{-i\omega t}\bigr] +
\operatorname{Re}\bigl[Z_{2}e^{-i\omega t}\bigr]
= \operatorname{Re}\bigl[(Z_{1}+Z_{2})e^{-i\omega t}\bigr],$$

so the phasors add and the answer is read off the modulus and argument of the
sum. The demo tests this by brute force: it sums the sinusoids in the time
domain and compares with the single sinusoid that the phasor sum predicts, over
one period. The residual is pure floating-point round-off:

| case | phasor sum $|Z|$ | phase (deg) | worst $|$direct $-$ phasor$|$ |
|---|---|---|---|
| equal amplitudes, $90^{\circ}$ apart | 4.242641 | 45.000000 | $1.3\times10^{-15}$ |
| equal amplitudes, $180^{\circ}$ apart | 0.000000 | 90.000000 | $3.1\times10^{-15}$ |
| $1+1$ in phase | 2.000000 | 0.000000 | $0$ |
| $1.5 + 2.0$ at $30^{\circ}$ | 3.383216 | 17.192124 | $2.2\times10^{-15}$ |

Three things in that table are worth naming. The second row is **destructive
interference**: the amplitude is zero to round-off, and the phase is undefined
(the sum is the zero phasor, whose argument the algorithm still reports).
The fourth row is the general case, where no trigonometric identity shortens the
work but the phasor sum is two lines of arithmetic.

### 3.3 Beats, and what a phasor cannot do

Phasors add sinusoids **of one frequency**. Two sinusoids of different
frequencies produce a beat whose amplitude varies in time; it is not a phasor,
and attempting to represent it as one is a category error. The correct
description is a sum of two phasors, each rotating at its own rate, and the
envelope of the sum moves at the difference frequency. The tidal spring–neap
cycle, the interference of two seismic wavelets with slightly different
frequencies, and the moiré of two nearby spectral lines are all the same
structure ([02-03-06
Superposition](../../02-physics/03-oscillations-and-waves/06-superposition-interference.md)).

## 4. Impedance: the phasor's natural habitat

### 4.1 Definition

For a linear system driven by a sinusoid, the **impedance** $Z$ is the complex
ratio of the phasor of the driving quantity to the phasor of the response. For an
electrical series circuit driven by a voltage $V_{0}\cos\omega t$:

| element | time-domain law | impedance |
|---|---|---|
| resistor $R$ | $v = Ri$ | $R$ |
| capacitor $C$ | $i = C\,\dot v$ | $1/(i\omega C) = -i/(\omega C)$ |
| inductor $L$ | $v = L\,\dot i$ | $i\omega L$ |

The table is the whole content of "differentiation becomes multiplication by
$-i\omega$" applied to the constitutive laws, and it is the reason alternating
current circuit analysis is done with complex numbers.

### 4.2 A worked network

Take $R = 1000\ \Omega$, $C = 100\ \mathrm{nF}$ at $f = 1000\ \mathrm{Hz}$, so
$\omega = 2\pi f = 6283.185307\ \mathrm{rad\,s^{-1}}$ and
$1/(\omega C) = 1591.549431\ \Omega$. Then

$$Z = R + \frac{1}{i\omega C} = 1000.000000 - 1591.549431\,i\ \Omega .$$

Reading it:

$$|Z| = 1879.635494\ \Omega, \qquad \arg Z = -57.858092^{\circ} .$$

The modulus is what multiplies the current to give the voltage amplitude; the
argument is the phase by which the current **leads** the voltage (the current
leads when $\arg Z < 0$, which is the signature of a capacitive load). The
**corner frequency**, where the reactance equals the resistance and
$|Z| = \sqrt2 R$, is $1/(2\pi RC) = 1591.549\ \mathrm{Hz}$; at $1000\ \mathrm{Hz}$
the reactance still exceeds the resistance, and the phase is
$-57.86^{\circ}$ rather than the $-90^{\circ}$ of a pure capacitor.

Sweeping the frequency shows the whole story of a low-pass network in three
columns ($|I|/|V|$ is normalised by $1/R$, its high-frequency limit):

| $f$ (Hz) | $|Z|$ ($\Omega$) | $\arg Z$ (deg) | $|I|R/|V|$ |
|---|---|---|---|
| 10.000 | 159158.084654 | $-89.640005$ | 0.006283 |
| 100.000 | 15946.879291 | $-86.404726$ | 0.062708 |
| 1000.000 | 1879.635494 | $-57.858092$ | 0.532018 |
| 1591.549 | 1414.213562 | $-45.000000$ | 0.707107 |
| 10000.000 | 1012.585945 | $-9.043061$ | 0.987570 |
| 100000.000 | 1000.126643 | $-0.911814$ | 0.999873 |

At the corner frequency $1/(2\pi RC) = 1591.549\ \mathrm{Hz}$ the impedance
modulus is $\sqrt2 R = 1414.213562\ \Omega$, the phase is exactly
$-45^{\circ}$, and the current magnitude is $1/\sqrt2 = 0.707107$ of the
high-frequency asymptote $|V|/R$: the three facts are one fact. (Measured against
the value at $100\ \mathrm{kHz}$, which is $0.999873$ rather than $1$, the ratio is
$0.707196$ — the difference between an asymptote and a measurement.) Below the
corner the current grows almost in proportion to $f$: the last-column values at
$10$ Hz and $100$ Hz are in the ratio $9.980516$, and the departure from exactly
$10$ is the first appearance of the resistive term, which is the same physics
that makes the impedance level off at $R$ above $10^5$ Hz.

### 4.3 Verification against the time domain

The demo integrates the circuit's own differential equation,

$$R\dot q + \frac{q}{C} = V_{0}\cos\omega t,$$

with a fourth-order Runge–Kutta scheme, and measures the steady-state charge
amplitude by least-squares projection onto $\cos\omega t$ and $\sin\omega t$
(not by reading a peak off a sampled record, which would bias the answer by the
sampling phase). Result:

| quantity | value |
|---|---|
| measured steady-state charge amplitude | $8.467330149\times10^{-8}$ C |
| prediction $V_{0}/(\omega\vert Z\vert)$ | $8.467330160\times10^{-8}$ C |
| relative difference | $1.234\times10^{-9}$ |

The agreement is the practical content of the phasor method: complex arithmetic
gives the answer that the differential equation, integrated numerically for
several hundred cycles, produces. Note the $\omega$ in the prediction: the
charge is the integral of the current, so $|q| = |I|/\omega = V_{0}/(\omega|Z|)$.
Dropping that factor is a common error and a factor of 6283 in this example.

### 4.4 The mechanical analogue, and where the phase comes from

The same algebra describes a driven damped oscillator,

$$m\ddot x + c\dot x + kx = F_{0}\cos\omega t,$$

whose impedance is

$$Z(\omega) = m(\omega_{0}^{2}-\omega^{2}) + i c\omega, \qquad
\omega_{0} = \sqrt{k/m},$$

so the steady-state displacement has amplitude $F_{0}/|Z|$ and phase
$-\arg Z$. With $m = 1$, $c = 0.6$, $k = 25$, $F_{0} = 2$ the demo obtains

| $\omega$ (rad/s) | $|Z|$-predicted amplitude | demodulated RK4 amplitude | difference |
|---|---|---|---|
| 2.000 | 0.095082984 | 0.095082986 | $1.6\times10^{-8}$ |
| 5.000 | 0.666666667 | 0.666666669 | $2.9\times10^{-9}$ |
| 9.000 | 0.035549391 | 0.035549391 | $1.0\times10^{-9}$ |

with the phases $-3.270^{\circ}$, $-90.000^{\circ}$ and $-174.492^{\circ}$. The
middle row is resonance for the undamped system ($\omega_{0} = 5$), and there
the response lags the force by exactly a quarter cycle. With damping, the
amplitude peak sits not at $\omega_{0}$ but at
$\sqrt{\omega_{0}^{2} - c^{2}/(2m^{2})} = 4.981967\ \mathrm{rad\,s^{-1}}$ — a
shift that the impedance formula gives without any further work, and that
matters in seismology whenever a resonance is used to infer a structure.

### 4.5 The derivation, done once

It is worth seeing why the impedance method is not a trick. Substitute the
trial solution $x = \operatorname{Re}[Xe^{-i\omega t}]$ into the oscillator
equation. Differentiating brings down factors of $-i\omega$:

$$m(-i\omega)^{2}X + c(-i\omega)X + kX = F_{0}
\quad\Longrightarrow\quad
\bigl[k - m\omega^{2} - i c\omega\bigr]X = F_{0}.$$

This is one algebraic equation for one unknown, because the common factor
$e^{-i\omega t}$ cancelled. Solving,

$$X = \frac{F_{0}}{k - m\omega^{2} - ic\omega} = \frac{-F_{0}}{m(\omega_{0}^{2}-\omega^{2}) + ic\omega}.$$

The amplitude is $|X| = F_{0}/|Z|$ and the phase is $\arg X = -\arg Z$ once the
sign convention for $Z$ is fixed; that sign is the only place where errors
enter, and it is why the convention is stated at the top of this lesson. The
general rule the derivation illustrates is:

> In steady state, every $\mathrm{d}/\mathrm{d}t$ acts as a multiplication by
> $-i\omega$, so a linear differential equation becomes a complex algebraic
> equation.

Everything in the rest of this module is a consequence of that single
substitution, extended from polynomials in $\omega$ to arbitrary functions of a
complex variable.

## 5. The Argand diagram, and mappings of the plane

### 5.1 Reading the diagram

The **Argand diagram** plots $z$ as the point $(x,y)$. Then:

- addition is vector addition;
- $|z_{1}-z_{2}|$ is the distance between the points;
- the set $|z - z_{0}| = r$ is a circle and $|z - z_{1}| = |z - z_{2}|$ is the
  perpendicular bisector;
- multiplication by $z_{0}$ is the similarity that scales by $|z_{0}|$ and
  rotates by $\arg z_{0}$.

That last reading turns complex arithmetic into geometry, and it is what makes
the transformation $w = f(z)$ of the next lesson a *map of the plane* rather
than a computation.

### 5.2 Where the branch cut bites

$\arg$ is discontinuous on the negative real axis, so any function built from
$\arg$ — notably $\log z = \ln|z| + i\arg z$ and $\sqrt z$ — has a **branch
cut** there. The consequences are physical:

- The reflectivity of a layered medium is a square root of a product of
  impedances; the branch of that square root fixes the sign of the transmitted
  amplitude.
- The vertical wavenumber $k_{z} = \sqrt{\omega^{2}/c^{2} - k_{x}^{2}}$ switches
  from real to imaginary across the branch point at $\omega/c = |k_{x}|$; the
  choice of branch is the choice between a propagating and an evanescent wave.
- The velocity from a complex modulus is $\sqrt{M/\rho}$; the branch decides
  whether the material attenuates or amplifies.

In all three cases the physical principle (outgoing or decaying) selects the
branch, not the algebra. When a code produces a growing solution, the branch is
the first thing to inspect.

## Assumptions and regime of validity

Everything in Sections 3 to 5 rests on the same four hypotheses, and each of them
fails somewhere in practice.

| assumption | what it means | where it breaks |
|---|---|---|
| **Linearity** | response is proportional to drive; superposition holds | large strains, saturating sensors, nonlinear soil response at high strain |
| **Time invariance** | the system does not change during the measurement | drifting instruments, temperature-dependent gain, time-varying medium |
| **Single frequency, steady state** | the transient has died and only one $\omega$ is present | any record shorter than a few time constants; broadband or impulsive sources |
| **Real signal, stated convention** | the physical quantity is $\operatorname{Re}[Ze^{-i\omega t}]$ | complex-valued observables (e.g. a two-component field), where conjugate symmetry does not hold |

Two further qualifiers are mathematical rather than physical, and both bite:

- **The branch of the argument.** Phasors add algebraically, so a sum that crosses
  the negative real axis produces an apparent $2\pi$ jump in the phase. That jump
  is bookkeeping, not physics, and any phase that will be differentiated,
  interpolated, or averaged must be unwrapped first.
- **The branch of a square root or logarithm.** Impedances of layered media
  involve square roots of products, and the choice of branch fixes the sign of a
  transmitted amplitude or the reality of a vertical wavenumber. The physical
  requirement (an outgoing, decaying wave) selects the branch; the algebra does
  not.

**What the method does not do.** A phasor carries no information beyond amplitude
and phase at one frequency. It cannot represent a transient, a beat, a chirp or
any broadband signal, and reading an "impedance" off data that are not in steady
state produces a number that changes with the window you chose. When a phasor
answer is quoted, the frequency, the convention and the steady-state assumption
are all part of the result.

## 6. Python demonstration

[`code/complex_arithmetic_demo.py`](./code/complex_arithmetic_demo.py) runs in
under a second and prints every table above:

```text
python3 code/complex_arithmetic_demo.py
```

It contains no third-party imports — only `cmath` and `math` — and it computes:

- rectangular/polar round trips (residuals $1.1\times10^{-16}$ to
  $4.4\times10^{-16}$);
- multiplication and division as rotation and scaling ($|ab| = 6.000000$,
  $\arg(ab) = 75.000000^{\circ}$);
- sums of the roots of unity for $n = 3, 5, 8$ (moduli
  $4.3\times10^{-16}$, $1.6\times10^{-16}$, $3.4\times10^{-16}$);
- a sixth root of $1+i$ and the check that its sixth power returns $1+i$ to
  $2.5\times10^{-16}$;
- phasor addition against direct time-domain summation;
- the RC network against a Runge–Kutta integration of the circuit's own
  differential equation;
- the driven oscillator against a Runge–Kutta integration with least-squares
  demodulation.

Two methodological points, because they are the difference between a demo and a
check:

**Measure amplitude by projection, not by peak-picking.** The projected
amplitude is the exact least-squares fit of $a\cos\omega t + b\sin\omega t$ to
the samples, so it is unbiased by where the peak falls between samples. Reading
`max(abs(x))` instead gives an error of order $(\omega\,\Delta t)^{2}/8$, which
for a coarse grid can exceed the effect being demonstrated.

**Integrate the equation you claim to be solving.** The RC check integrates
$R\dot q + q/C = V\cos\omega t$, not a second-order equation that happens to
have the same impedance at one frequency. A test that silently solves a
different problem is worse than no test.

## 7. Common mistakes

1. **Reporting a wrapped phase as if it were smooth.** $\arg$ jumps by $2\pi$
   across the negative real axis. Unwrap before differentiating or
   interpolating, and say which interval you report.
2. **Confusing the phasor with the signal.** The phasor $Z = Ae^{-i\phi}$
   contains no time dependence; writing $\operatorname{Re} Z$ when you mean
   $\operatorname{Re}[Ze^{-i\omega t}]$ loses a factor of $\cos\omega t$.
3. **Mixing sign conventions between steps.** If the forward transform uses
   $e^{-i\omega t}$ then a derivative multiplies by $-i\omega$ for a field of the
   form $e^{-i\omega t}$, and by $+i\omega$ when the field is written
   $e^{i(kx-\omega t)}$. Write the convention at the top of the page.
4. **Adding phasors of different frequencies.** Phasors add at one frequency
   only.
5. **Forgetting the $\omega$ in integral relations.** Charge is the integral of
   current, so $|q| = |I|/\omega$; displacement is the integral of velocity.
6. **Assuming $|z_{1}+z_{2}| = |z_{1}|+|z_{2}|$.** The triangle inequality is an
   inequality, and the gap is exactly the interference that geophysics spends
   its time measuring.
7. **Ignoring which branch of a square root is intended.** See Section 5.2; the
   sign of a reflectivity or the reality of a vertical wavenumber hangs on it.

## 8. Real-world applications

- **Magnetotellurics.** The impedance tensor is literally a complex $2\times2$
  matrix relating horizontal electric to magnetic field phasors as a function of
  frequency; its phase is the basis of the method's depth sensitivity
  ([09-electrical-em-methods](../../09-electrical-em-methods/README.md)).
- **Instrument response.** A seismometer is described by its poles and zeros in
  $\mathbb{C}$ and its response is a complex function of frequency; removing it
  from a record is division by that function
  ([20-signal-processing](../../20-signal-processing/README.md)).
- **Seismic attributes.** The instantaneous amplitude, phase and frequency of a
  trace are the modulus and argument of a complex trace
  ([01-10-06 Hilbert
  transform](../10-fourier-analysis/06-hilbert-transform.md)).
- **Tidal and harmonic analysis.** Constituent amplitudes and phase lags are
  phasors; the datum of a tide gauge is defined through them
  ([01-10-01 Fourier series](../10-fourier-analysis/01-fourier-series.md)).
- **Impedance in the field.** The complex impedance of a buried conductor, of a
  seismic base isolation bearing, or of a piezoelectric transducer is measured
  and inverted for the physical parameters behind it.
- **Potential fields.** A two-dimensional gravity or magnetic anomaly can be
  written as the real part of an analytic function of $z = x + iy$; poles in the
  complex plane are the equivalent sources
  ([01-06-08 Potential theory](../06-multivariable-calculus/08-potential-theory.md),
  and lesson [02 Complex Functions](./02-complex-functions.md)).

## 9. Further reading

- **Nahin, P. J. (2010). *An Imaginary Tale: The Story of $\sqrt{-1}$*.
  Princeton University Press.** Level: beginner. History and motivation, with
  the geometry kept visible; useful if the algebra feels arbitrary.
- **Boas, M. L. (2005). *Mathematical Methods in the Physical Sciences*
  (3rd ed.). Wiley.** Chapters 1–2. Level: intermediate. The standard
  presentation of phasors and impedance with worked circuit problems.
- **Aki, K. & Richards, P. G. (2002). *Quantitative Seismology*
  (2nd ed.). University Science Books.** §§1.3–1.5. Level: advanced. Complex
  representation of harmonic waves, and the convention question settled
  explicitly.
- **Bracewell, R. N. (2000). *The Fourier Transform and Its Applications*
  (3rd ed.). McGraw-Hill.** Chapter 1–4. Level: intermediate. The most careful
  short account of why the sign convention matters.
- **Ward, S. H. & Hohmann, G. W. (1988). Electromagnetic theory for geophysical
  applications. In *Electromagnetic Methods in Applied Geophysics*, Vol. 1,
  ed. M. N. Nabighian, SEG.** Level: advanced. Where the impedance tensor of
  magnetotellurics is defined and interpreted.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library before citing them.

## 10. Related lessons

- [02 Holomorphic Functions and Cauchy-Riemann
  Equations](./02-complex-functions.md) — what happens when the complex number
  becomes a variable, and why that solves Laplace's equation.
- [03 Contour Integration, Residues and Real
  Integrals](./03-contour-integration.md) — where the poles of an impedance-like
  function are turned into numbers.
- [04 The Laplace Transform and Transient
  Problems](./04-laplace-transform.md) — the same algebra for signals that are
  not sinusoidal in steady state.
- [05 The z-Transform and Discrete Linear
  Systems](./05-z-transform.md) — the discrete counterpart, on the unit circle.
- [02-03 Oscillations and
  Waves](../../02-physics/03-oscillations-and-waves/README.md) — the driven
  damped oscillator whose steady state Section 4.4 computes.
- [01-03-05 Phase and Harmonics](../03-trigonometry/05-phase-and-harmonics.md) —
  the trigonometric language that phasors replace.

## 11. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/01-complex-arithmetic-exercises.md`](./exercises/01-complex-arithmetic-exercises.md).
Solutions:
[`exercises/01-complex-arithmetic-solutions.md`](./exercises/01-complex-arithmetic-solutions.md).

## Self-assessment checklist

- [ ] I can convert between rectangular and polar form and state the interval
      used for the principal argument.
- [ ] I can multiply, divide and conjugate in both forms, and explain the
      geometry of multiplication.
- [ ] I can add two sinusoids of the same frequency by adding phasors, and give
      the amplitude and phase of the sum.
- [ ] I can write the impedance of a series $R$, $C$, $L$ network and read off
      the amplitude and phase response.
- [ ] I can find the condition for resonance of a damped driven oscillator and
      say how much the peak is shifted from $\omega_{0}$.
- [ ] I can say where a branch cut is discontinuous and give one geophysical
      quantity whose interpretation depends on the branch.
- [ ] I can verify a phasor result against a time-domain integration and state
      what the residual measures.
