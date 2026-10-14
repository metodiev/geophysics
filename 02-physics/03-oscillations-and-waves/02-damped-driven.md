---
id: 02-03-02
title: "Damped and Driven Oscillations, Resonance and Quality Factor"
level: intermediate
prereqs: ["02-03-01", "01-05-04", "01-08-01"]
estimated_minutes: 90
tags: [oscillations, damping, resonance, quality-factor]
---

# Damped and Driven Oscillations, Resonance and Quality Factor

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the damped, driven oscillator equation and classify the free
   solutions as underdamped, critically damped and overdamped, with the
   condition that separates them.
2. **Derive** the steady-state amplitude and phase of the driven response,
   including the resonance frequency $\omega_r = \sqrt{\omega_0^2 - 2\beta^2}$
   and the exact half-power frequencies.
3. **Define** the quality factor $Q$ in four equivalent ways — energy loss per
   radian, logarithmic decrement, half-power bandwidth, and resonance
   amplification — and state the regime in which they agree.
4. **Measure** $Q$ from a decay, from a spectrum and from a phase lag, and say
   which method is best for which data.
5. **Explain** why nearly every geophysical instrument is designed with a
   specified damping, and why a seismogram's decaying coda is a measurement of
   Earth's $Q$.

## Prerequisites

- [02-03-01 Simple Harmonic Motion and Small-Oscillation Approximation](./01-simple-harmonic-motion.md)
  — the undamped oscillator and energy.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../../01-mathematics/05-single-variable-calculus/04-taylor-series.md)
  — used for the high-$Q$ approximations.
- [01-08-02 Second-Order Linear Equations](../../01-mathematics/08-ordinary-differential-equations/02-second-order-linear.md)
  — the classification of second-order linear equations with constant
  coefficients, including the three damping regimes.

## 1. Why damping is not a detail

In [02-03-01](./01-simple-harmonic-motion.md) the oscillator conserved energy
exactly and oscillated forever. Neither statement is true of anything
geophysical. A geophone's coil loses energy to its own magnetic circuit; a
seismic wave loses energy to the anelasticity of the rock; a tidal response
loses energy to the ocean. Damping is what turns the oscillator from a
mathematical object into an instrument, because:

- the *decay rate* is a measurable property of the medium or the instrument;
- the *response to a driving force* depends on damping, so calibration requires
  it;
- energy loss and velocity dispersion are linked, so measuring one constrains the
  other (lesson 02-03-10).

This lesson sets up the algebra once. Every later treatment of attenuation in
this curriculum — seismic $Q$, electromagnetic skin depth, the quality factor of
a normal mode — is a variation on it.

## 2. Precise definitions

### 2.1 The free damped oscillator

$$m\ddot x + 2m\beta\dot x + m\omega_0^2x = 0
\qquad\Longleftrightarrow\qquad
\ddot x + 2\beta\dot x + \omega_0^2 x = 0 , \tag{1}$$

with damping coefficient $\beta \ge 0$ (units s⁻¹) and $\omega_0$ the undamped
angular frequency. The substitution $x = e^{\lambda t}$ gives the characteristic
equation

$$\lambda^2 + 2\beta\lambda + \omega_0^2 = 0
\quad\Longrightarrow\quad
\lambda = -\beta \pm \sqrt{\beta^2 - \omega_0^2} . \tag{2}$$

| Regime | Condition | Solution |
|---|---|---|
| Underdamped | $\beta < \omega_0$ | $x = Ae^{-\beta t}\cos(\omega_d t + \varphi)$, $\omega_d = \sqrt{\omega_0^2-\beta^2}$ |
| Critically damped | $\beta = \omega_0$ | $x = (A + Bt)e^{-\beta t}$ |
| Overdamped | $\beta > \omega_0$ | sum of two distinct real exponentials |

The **damped period** is $T_d = 2\pi/\omega_d > T_0$; damping *slows* the
oscillation as well as shrinking it.

### 2.2 The driven oscillator

$$m\ddot x + 2m\beta\dot x + m\omega_0^2 x = F_0\cos\omega t . \tag{3}$$

The general solution is a transient (the free solution, decaying as
$e^{-\beta t}$) plus a particular solution oscillating at the driving frequency.
After a few times $1/\beta$ only the particular solution remains:

$$x(t) \to A(\omega)\cos(\omega t - \delta(\omega)) , \tag{4}$$

with the **amplitude response** and **phase lag**

$$A(\omega) = \frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2 + (2\beta\omega)^2}},
\qquad
\tan\delta = \frac{2\beta\omega}{\omega_0^2 - \omega^2} . \tag{5}$$

### 2.3 The quality factor

Four definitions, all equivalent for a lightly damped oscillator:

$$Q = \frac{\omega_0}{2\beta}, \qquad
\frac{1}{Q} = -\frac{1}{E}\frac{dE}{d\phi} , \qquad
Q = \frac{\pi}{\delta} , \qquad
Q = \frac{\omega_0}{\Delta\omega} , \tag{6}$$

where $\delta = \ln(x_n/x_{n+1})$ is the **logarithmic decrement** (per cycle)
and $\Delta\omega$ is the half-power bandwidth. The relations among them are
*approximations of order $1/Q^2$*, and the demo measures both the approximation
error and the exact statements.

## 3. Derivations

### 3.1 The underdamped solution

With $\beta < \omega_0$, equation (2) gives
$\lambda = -\beta \pm i\omega_d$ with $\omega_d = \sqrt{\omega_0^2-\beta^2} > 0$.
Two complex solutions combine into

$$x(t) = e^{-\beta t}\left(C_1\cos\omega_d t + C_2\sin\omega_d t\right)
= A e^{-\beta t}\cos(\omega_d t + \varphi) , \tag{7}$$

with $A$ and $\varphi$ fixed by $x(0)$ and $\dot x(0)$. The envelope
$Ae^{-\beta t}$ is what can be measured: successive maxima one period apart have
ratio $e^{\beta T_d}$, so

$$\delta = \beta T_d = \frac{2\pi\beta}{\omega_d}
\quad\Longrightarrow\quad
Q = \frac{\pi}{\delta} = \frac{\omega_d}{2\beta}
= \frac{\omega_0}{2\beta}\sqrt{1 - \frac{1}{4Q^2}} . \tag{8}$$

The last equality is the exact relation between the two $Q$ definitions: they
differ by a factor $(1 - 1/(4Q^2))^{-1/2}$, which is 0.125 per cent at $Q = 10$
and 0.25 per cent at $Q = 7$. At $Q = 1$ the difference is 29 per cent and the
whole apparatus of "logarithmic decrement" has lost its meaning, because the
first maximum is no longer one period after the initial displacement.

### 3.2 The steady-state amplitude and phase

Substitute $x = \Re\{X e^{i\omega t}\}$ into equation (3). Using
$F_0\cos\omega t = \Re\{F_0e^{i\omega t}\}$,

$$\left(-\omega^2 + 2i\beta\omega + \omega_0^2\right)X = \frac{F_0}{m}
\quad\Longrightarrow\quad
X = \frac{F_0/m}{\left(\omega_0^2-\omega^2\right) + 2i\beta\omega} . \tag{9}$$

Then $A = |X|$ and $\delta = -\arg X$ reproduce equation (5). Two limits are
worth memorising: below resonance $A \to F_0/(m\omega_0^2)$, the static
deflection; at exactly $\omega = \omega_0$,

$$A(\omega_0) = \frac{F_0}{2m\beta\omega_0} , \qquad \delta(\omega_0) = 90^\circ
\text{ for every } \beta . \tag{10}$$

The 90° phase at $\omega_0$ is the operational definition of resonance when a
swept-frequency source is used.

### 3.3 Where the peak really is

Differentiating $A^2$ with respect to $\omega^2$ and setting the result to zero
gives the **displacement resonance**

$$\omega_r = \sqrt{\omega_0^2 - 2\beta^2} , \qquad
A_{\max} = \frac{F_0/m}{2\beta\sqrt{\omega_0^2-\beta^2}} . \tag{11}$$

For $\beta \to 0$, $A_{\max}/A(0) \to \omega_0/(2\beta) = Q$: **the amplification
at resonance equals the quality factor.** The demo measures
$A_{\max}/A(0) = 10.0125$ at $Q = 10$, 0.1 per cent above $Q$, which is the
$\omega_r \neq \omega_0$ correction.

### 3.4 The exact half-power frequencies

Setting $|X(\omega)| = A_{\max}/\sqrt2$ and solving for $\omega$ gives a result
worth deriving because it is quoted as "$\Delta\omega = 2\beta$" everywhere:

$$D(\omega) = \left(\omega_0^2-\omega^2\right)^2 + 4\beta^2\omega^2
= 2D(\omega_r), \tag{12}$$

whose solutions are

$$\omega_\pm^2 = \omega_0^2 - 2\beta^2 \pm 2\beta\sqrt{\omega_0^2-\beta^2},
\qquad
\omega_\pm = \sqrt{\omega_0^2-2\beta^2 \pm 2\beta\sqrt{\omega_0^2-\beta^2}}.
\tag{13}$$

The bandwidth is **not** exactly $2\beta$; it is $2\beta + O(\beta^2/\omega_0^2)$,
as the demo's last column shows: $\Delta\omega/2\beta = 1.0004$ at $Q = 25$ and
$1.0467$ at $Q = 2.5$. The familiar identity holds in the high-$Q$ limit and
should be stated that way.

### 3.5 Power absorption

The instantaneous power delivered by the driving force is $F\dot x$; averaging
over a cycle, with $\dot x$ lagging $F$ by $90^\circ-\delta$, gives

$$\langle P \rangle = \tfrac12 F_0 A(\omega)\,\omega\sin\delta
= \frac{F_0^2}{2m}\frac{2\beta\omega^2}
{(\omega_0^2-\omega^2)^2 + 4\beta^2\omega^2} . \tag{14}$$

At $\omega = \omega_0$ this is $\langle P\rangle = F_0^2/(4m\beta)$, half the
energy dissipated per cycle times the frequency — the statement that the
oscillator is absorbing energy as fast as it can lose it.

## 4. Physical interpretation

**Damping is a phase relationship, not a subtraction.** Energy enters the
oscillator only from the component of force in phase with the velocity. The
whole resonance curve is a statement about how the phase between force and
velocity changes with frequency: far below resonance the force moves a static
displacement, far above it moves an inertia, and at resonance it moves a
dashpot.

**$Q$ is a ratio of stored energy to lost energy.** Rearranging
$dE/E = -d\phi/Q$ over a cycle gives $Q = 2\pi E/\Delta E_{\text{cycle}}$: the
number of radians (not cycles) it takes to lose a factor $e$ of energy. A
seismic $Q = 100$ means 6.3 per cent of the energy is lost per cycle; the seismic
wave has to travel about $Q/\pi \approx 32$ wavelengths to fall by $e^{-1}$ in
amplitude.

**Resonance is narrow, not sharp, but it is real.** The response is large only
within $\Delta\omega \approx 2\beta = \omega_0/Q$ of the peak; the ratio of peak
to bandwidth is $Q$. A $Q$ of 10 gives a resonance 10 times sharper than the
bandwidth of a critically damped instrument, and that is why a high-$Q$
oscillator must be tuned, while a geophone is deliberately damped to about
$Q = 1/\sqrt2$.

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Linear damping $F_d = -2m\beta\dot x$ | Loss proportional to velocity | At high amplitude, friction becomes rate-independent (Coulomb) or nonlinear; the decay is no longer exponential |
| Constant coefficients | $\beta$, $\omega_0$ independent of time | Slowly changing $\omega_0(t)$ gives a WKB oscillator, not a damped one |
| Single degree of freedom | One resonant peak | Multiple peaks (coupled modes, lesson 02-03-03) |
| Steady state | $t \gg 1/\beta$ | The transient carries the initial conditions and must be analysed separately |
| Light damping for the identities in equation (6) | $Q \gtrsim 5$ | At $Q \lesssim 1$ the definitions of $Q$ diverge from each other; quote the exact forms |
| Frequency-independent $\beta$ | One $Q$ fits the band | Real rocks show $Q$ weakly dependent on frequency; a distribution of relaxation mechanisms is needed (lesson 02-04-07) |

## 6. Units and dimensional analysis

- $\beta$: s⁻¹ (it multiplies $\dot x$ to give m s⁻², so $\mathrm{s^{-1}
  \cdot m\,s^{-1}} = \mathrm{m\,s^{-2}}$ ✓).
- $Q$, $\delta$: dimensionless.
- $\Delta\omega$: s⁻¹, and $\omega_0/\Delta\omega$ is dimensionless ✓.
- $A(\omega)$: m for a force in N and $m$ in kg; the ratio $F_0/(m\omega_0^2)$
  has units $\mathrm{N/(kg\,s^{-2})} = \mathrm{m}$ ✓.

A useful check of the resonance amplification: $A_{\max}/A(0) = Q$, both
dimensionless, independent of $F_0$ and $m$ ✓. Any numerical result whose
"amplification" carries units is wrong.

## 7. Python demonstration

[`code/damped_driven_demo.py`](./code/damped_driven_demo.py) integrates the
equations and compares with equations (5) and (13). Observed output with
$m = 1$ kg, $k = 100$ N m⁻¹ ($\omega_0 = 10$ rad s⁻¹):

```text
  beta           regime    omega_d  x0/x1 meas  delta meas  Q=pi/delta    Q=w0/2b
  0.50            light    9.98749    1.369647    0.314553      9.9875    10.0000
  2.00         moderate    9.79796    3.605822    1.282550      2.4495     2.5000
 10.00         critical         --          --          --          --     0.5000
```

```text
beta = 0.5 rad/s -> Q = omega0/(2 beta) = 10.0000, static deflection A(0) = 0.010000 m
    omega    A numeric   A analytic   rel. diff
     5.00     0.013304     0.013304   +3.02e-05
     9.50     0.073462     0.073459   +3.01e-05
    10.00     0.100000     0.100000   -5.58e-08
    10.50     0.068151     0.068150   +1.42e-05
    15.00     0.007943     0.007943   +8.71e-06

  analytic peak at omega_r = sqrt(omega0^2 - 2 beta^2) = 9.97497 rad/s (fine sweep found 9.97500)
  A_max = 0.100125 m; A_max/A(0) = 10.0125 (compare Q = 10.0000)
```

```text
  beta   Q=w0/2b      A_res       w_lo       w_hi         Dw     w0/Dw    Dw/2b
  0.20    25.000    0.25005    9.79392   10.19408    0.40016   24.9900   1.0004
  0.50    10.000    0.10013    9.46111   10.46363    1.00252    9.9748   1.0025
  1.00     5.000    0.05025    8.83743   10.85817    2.02073    4.9487   1.0104
  2.00     2.500    0.02552    7.26692   11.45390    4.18698    2.3884   1.0467
```

```text
   omega    lag(deg)       A (m)  mean power (W)
    0.00      0.0000    0.010000        0.000000
   10.00     90.0000    0.100000        0.500000
   20.00    176.1859    0.003326        0.002212
```

### What to observe

| Observation | Consequence |
|---|---|
| $Q = \pi/\delta = 9.9875$ but $Q = \omega_0/2\beta = 10.0000$ | The two definitions differ by the factor $\omega_0/\omega_d$ of equation (8) — 0.13 per cent at $Q = 10$, exactly as predicted |
| The numerically measured amplitude matches the closed form to $3\times10^{-5}$ | The steady state has been reached; the residual is the $O(\omega\,dt)^2$ error of the fixed-step integrator, not a physical effect |
| The peak is at 9.975 rad/s, not 10 | $\omega_r = \sqrt{\omega_0^2-2\beta^2}$; the difference matters whenever $Q$ is modest, and it is a classic source of "the resonance is not where I predicted" confusion |
| $A_{\max}/A(0) = 10.0125$ against $Q = 10$ | The amplification equals $Q$ only in the limit $\beta\to0$ |
| $\Delta\omega/2\beta$ rises from 1.0004 to 1.0467 as $Q$ falls from 25 to 2.5 | The bandwidth identity is a high-$Q$ approximation, quantified here |
| The phase lag is exactly 90.0000° at $\omega = \omega_0$ while the amplitude peak is at 9.975 | Amplitude resonance and phase resonance are different frequencies; use whichever your measurement actually determines |

> **Breaking exercise.** Set `beta = 10.0` (critical damping) in part 2 and
> predict, before running, what the phase lag at $\omega = \omega_0$ becomes.
> Then explain the answer using equation (5).

## 8. Common mistakes

1. **Using $\omega_0$ where $\omega_d$ belongs.** The observed decay and the
   observed oscillation frequency are both governed by $\omega_d$, not
   $\omega_0$; the difference is $1/(4Q^2)$ relative.
2. **Quoting the resonance frequency as $\omega_0$.** For a displacement
   response it is $\sqrt{\omega_0^2-2\beta^2}$; for a velocity response it is
   $\omega_0$; for an acceleration response it is higher still. State which
   response function you mean.
3. **Assuming the identity $Q = \omega_0/\Delta\omega$.** It is the high-$Q$
   limit; the exact half-power frequencies are equation (13).
4. **Fitting a decay before the transient has ended.** A driven system needs
   $t \gg 1/\beta$; a free decay needs the initial condition to be a pure
   eigenmode, which it generally is not for $Q < 5$.
5. **Reporting $Q$ without saying how it was measured.** Decay, bandwidth and
   phase-lag methods agree only within their stated approximations, and in real
   data they are contaminated differently by noise and by interfering arrivals.
6. **Forgetting that damping also shifts the period.** Using $T_0$ to convert a
   measured $\delta$ into $\beta$ introduces the $\omega_0/\omega_d$ error.
7. **Confusing $Q$ of an instrument with $Q$ of a material.** A geophone's $Q$
   is set by its damping resistor and is a design choice; a rock's $Q$ is a
   material property and is measured. Both are dimensionless and both are called
   $Q$.

## 9. Real-world applications

- **Geophone and seismometer design.** Instruments are specified by their
  damping; critical damping (or a $Q$ near $1/\sqrt2$) flattens the response and
  removes ringing, at the cost of sensitivity. Broadband seismometers use
  force-balance feedback to synthesise a flat response over decades of
  frequency, which is a statement about the design's effective $\beta(\omega)$.
- **Earth $Q$.** The coda of a seismogram decays at a rate that measures the
  attenuation of the path; body-wave and surface-wave $Q$ are inverted for the
  thermal and melt state of the mantle, and are standard outputs of
  [ObsPy](https://docs.obspy.org)-based processing of [EarthScope](https://www.earthscope.org)
  and [ORFEUS](https://www.orfeus-eu.org) data.
- **Normal-mode $Q$.** Each free oscillation of the Earth has its own $Q$; the
  splitting and the $Q$ of a mode constrain the mantle's shear attenuation
  independently of its elastic structure.
- **Instrument calibration by ring-down.** A geophone's damping is measured by
  the logarithmic decrement of a known impulse — a direct application of
  equation (8).
- **Resonant buildings and site response.** A structure with $Q \approx 10$ can
  amplify ground motion by an order of magnitude at its resonant frequency; the
  same algebra used here is the basis of seismic design codes.
- **Electromagnetic and acoustic analogues.** The $Q$ of an induction-coil
  sensor, of a radar antenna and of a microwave cavity are all defined by
  equation (6); the physics changes, the algebra does not.

## 10. Further reading

- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** The introduction of $Q$ and its relation to
  attenuation, together with the instrument-response chapter that uses this
  lesson directly. Level: advanced.
- **Stein, S., & Wysession, M. *An Introduction to Seismology, Earthquakes and
  Earth Structure* (Blackwell, 2003).** Seismometer response, damping and the
  transfer function, at the level of this lesson. Level: intermediate.
- **Lay, T., & Wallace, T. C. *Modern Global Seismology* (Academic Press,
  1995).** Chapter on the seismic instrument and on attenuation measurements.
  Level: intermediate.
- **Rayleigh, Lord. *The Theory of Sound* (1896; Dover reprint).** The original
  treatment of driven resonance, including the bandwidth argument. Level:
  intermediate.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics*
  (2nd ed., Cambridge University Press, 1990).** Instrument specifications and
  the damping of field sensors. Level: beginner to intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [01 Simple Harmonic Motion and Small-Oscillation Approximation](./01-simple-harmonic-motion.md)
  — the undamped limit of everything here.
- [03 Coupled Oscillators and Normal Modes](./03-coupled-oscillators.md) — one
  resonant peak becomes $N$.
- [07 Dispersion, Group Velocity and Phase vs Group Speed](./07-dispersion.md) —
  what happens when $\omega_0$ depends on wavenumber.
- [10 Attenuation, Absorption and the Quality Factor Q](./10-attenuation.md) —
  $Q$ in a wave, including the dispersion that must accompany it.
- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../04-elasticity-and-continuum-mechanics/05-elastodynamics.md)
  — where the oscillator becomes a continuum.
- [06-seismology](../../06-seismology/README.md) — where Earth's $Q$ is measured.

Exercises:
[`exercises/02-damped-driven-exercises.md`](./exercises/02-damped-driven-exercises.md)
and
[`exercises/02-damped-driven-solutions.md`](./exercises/02-damped-driven-solutions.md).

## Self-assessment checklist

- [ ] I can classify a damped oscillator as under-, critically or overdamped and
      write its solution. (Section 2.1)
- [ ] I can derive the steady-state amplitude and phase by complex substitution.
      (Section 3.2)
- [ ] I can derive $\omega_r = \sqrt{\omega_0^2-2\beta^2}$ and explain why it is
      not $\omega_0$. (Section 3.3)
- [ ] I can state four definitions of $Q$ and say which are exact and which are
      high-$Q$ approximations. (Section 2.3, 3.4)
- [ ] I can explain why the phase lag is 90° at $\omega_0$ for any damping.
      (Section 3.2)
- [ ] I can explain the physical meaning of "energy lost per cycle is
      $2\pi/Q$". (Section 4)
- [ ] I can name two methods of measuring $Q$ in the field and state what
      contaminates each. (Sections 7, 9)
- [ ] I can say why a geophone is damped to about $Q = 1/\sqrt2$ rather than
      given a high $Q$. (Section 9)
