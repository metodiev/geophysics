# Solutions — 01-08-03 Damped and Driven Oscillators as Physical Models

> **Read this after attempting the exercises, not before.** Every amplitude,
> phase, gain and frequency below was computed from the formulas derived in the
> lesson.

---

## ★1 — Amplitude and phase across the resonance

With $\omega_0 = 10$, $\zeta = 0.05$ and $F_0/m = 1$,

$$A(\omega) = \frac{1}{\sqrt{(100-\omega^{2})^{2} + (0.1\times10\times\omega)^{2}}}
= \frac{1}{\sqrt{(100-\omega^{2})^{2}+\omega^{2}}}, \qquad
\varphi = \operatorname{atan2}\!\left(\omega,\ 100-\omega^{2}\right).$$

| $\omega$ | $A(\omega)$ | $\varphi$ |
|---|---|---|
| 0 | 0.010000 | 0.000° |
| 5 | 0.013304 | 3.814° |
| 10 | 0.100000 | 90.000° |
| 12 | 0.021926 | 164.745° |
| 20 | 0.003326 | 176.186° |

Checks: at $\omega = 0$ the response is the static value $F_0/(m\omega_0^{2})
= 1/100 = 0.01$ ✓. At $\omega = 5$ the denominator is
$\sqrt{75^{2}+5^{2}} = \sqrt{5625+25} = \sqrt{5650} = 75.166$ ✓. At
$\omega = \omega_0 = 10$ the first term vanishes and $A = 1/(2\zeta\omega_0^{2})
= 1/10 = 0.1$, which is exactly $Q = 1/(2\zeta) = 10$ in units of the static
response — **the row the question asks for**. The response is already down again
at $\omega = 12$ (five times the static value, but a fifth of the peak), which
is the narrowness of a $Q = 10$ resonance in one line.

---

## ★2 — Bandwidth and build-up

**(a)** Since $\Delta f/f_0 = 1/Q$ and $\Delta f = 2(0.5) = 1.0$ Hz around
$f_0 = 20$ Hz,

$$Q = \frac{f_0}{\Delta f} = \frac{20}{1.0} = 20, \qquad
\zeta = \frac{1}{2Q} = 0.025 .$$

**(b)** The decay time of the free response is
$\tau = 1/(\zeta\omega_0)$, and the build-up time of the driven response is
$2Q/\omega_0$. With $\omega_0 = 2\pi(20) = 125.6637$ rad/s:

$$\tau = \frac{1}{0.025\times125.6637} = 0.318310\ \mathrm{s}, \qquad
\frac{2Q}{\omega_0} = \frac{40}{125.6637} = 0.318310\ \mathrm{s}.$$

**They are equal because they are the same quantity**: $1/(\zeta\omega_0)
= 2Q/\omega_0$ given $Q = 1/(2\zeta)$. The free decay and the forced build-up
are the same relaxation of the same mode, observed with and without a driver.

**(c)** The build-up lasts $Q/\pi = 20/\pi = 6.366$ forced cycles, or
equivalently $0.318310$ s at 20 Hz, which is $0.318310\times20 = 6.366$ cycles
✓ (the two calculations agree, as they must).

---

## ★3 — The resonance peak, exactly

**(a)** The peak of the driven response is at
$\omega_{\text{peak}} = \omega_0\sqrt{1-2\zeta^{2}}$ provided
$\zeta<1/\sqrt2$. With $\zeta = 0.3$:

$$\sqrt{1-2(0.09)} = \sqrt{0.82} = 0.905539, \qquad
\omega_{\text{peak}} = 0.905539\times31.415927 = 28.448331\ \mathrm{rad/s}.$$

The ratio to $\omega_0$ is $0.905539$, a **9.45 % shift**, so the rule "resonance
at $\omega_0$" is not adequate here. At $\omega = \omega_0$ the response is

$$A(\omega_0) = \frac{1}{2\zeta\omega_0^{2}}
= \frac{1}{2(0.3)(987.0)} = 1.688\times10^{-3},$$

while at the peak $A_{\text{peak}} = A(\omega_0)/\sqrt{1-\zeta^{2}}
= 1.688\times10^{-3}/0.953939 = 1.770\times10^{-3}$. So
$A(\omega_0)/A_{\text{peak}} = \sqrt{1-\zeta^{2}} = 0.9539$: the response at
$\omega_0$ is **4.6 % below the peak**.

**(b)** For $\zeta = 0.75 > 1/\sqrt2 = 0.707107$ **no interior peak exists**:
the derivative of $A^{2}$ with respect to $\omega^{2}$ sets the stationary point
at $\omega^{2} = \omega_0^{2}(1-2\zeta^{2}) < 0$, which is not a physical
frequency. The response is monotonically decreasing in $\omega$, and the
largest value is at $\omega = 0$. **The criterion is $1-2\zeta^{2}>0$; the
formula's output of an imaginary frequency is the symptom, not the argument.**

---

## ★★4 — Undamped resonance

**(a)** With $x = (\sin t - t\cos t)/2$:

$$x' = \tfrac12\left(\cos t - \cos t + t\sin t\right) = \tfrac12t\sin t, \qquad
x'(0) = 0 \;\checkmark$$

$$x'' = \tfrac12\left(\sin t + t\cos t\right), \qquad
x''+x = \tfrac12\left(\sin t+t\cos t+\sin t-t\cos t\right) = \sin t \;\checkmark$$

and $x(0) = 0$ ✓. All three conditions hold, so the solution is correct (and
unique, by the existence-and-uniqueness theorem for linear equations with
continuous coefficients).

**(b)** For large $t$ the term $t\cos t/2$ dominates, so the envelope is
$\lvert t/2\rvert$, i.e. the amplitude grows **linearly in time**, not
exponentially. At $t = 50$:

$$x(50) = \frac{\sin 50 - 50\cos 50}{2} = \frac{-0.262374 - 48.248466}{2}
= -24.255338,$$

consistent with an envelope of $25$ and a phase near antiphase.

**(c)** The amplitude grows without bound because the forcing acts in phase with
the velocity at every cycle (the phase lag is exactly $90°$ at resonance), so
each cycle injects energy and none is removed; in reality **damping** removes
energy at a rate proportional to the square of the velocity, and the balance of
injection and removal fixes a finite amplitude $QF_0/(m\omega_0^{2})$.

---

## ★★5 — A 30 s broadband sensor

**(a)** With $\omega_0 = 2\pi/30 = 0.209440$ rad/s and $\zeta = 0.7$:

| $f$ (Hz) | $\omega$ | $\lvert H\rvert$ |
|---|---|---|
| 1.0 | 6.283185 | 1.000022 |
| 0.1 | 0.628319 | 0.996073 |
| 0.01 | 0.062832 | 0.089798 |

**(b)** Solving $\lvert H\rvert = 0.99$ numerically by bisection gives
$\omega = 0.517349$ rad/s, i.e.

$$f = \frac{\omega}{2\pi} = 0.082339\ \mathrm{Hz} = 82.3\ \mathrm{mHz}.$$

Note that this is well *above* the nominal corner $f_c = 1/T_0 = 33.3$ mHz:
with $\zeta = 0.7$ the response is still 1 % low at 82 mHz, because the approach
to flat is algebraic ($\lvert H\rvert \to 1$ only as $\omega\to\infty$) and not
sudden.

**(c)** The claim is wrong for two separate reasons. First, $\lvert H\rvert =
1.000022$ at 1 Hz is *not* exactly 1; the deviation is $2\times10^{-5}$, which is
negligible, so for a 1 Hz signal the claim happens to be harmless. But second —
and this is the error — the sensor's flatness at 1 Hz says nothing about its
response at 0.01 Hz, where $\lvert H\rvert = 0.0898$: **a signal at 10 mHz is
attenuated by a factor of 11 and is therefore misreported by 1000 % if no
correction is applied.** A transfer function is a property of a *frequency
band*, and quoting it at one frequency is meaningless.

---

## ★★6 — A 4.5 Hz geophone

**(a)** $\omega_0 = 2\pi(4.5) = 28.274334$ rad/s.

| $f$ (Hz) | $f/f_0$ | $\lvert H\rvert$ |
|---|---|---|
| 0.5 | 0.111 | 0.012348 |
| 1.0 | 0.222 | 0.049371 |
| 2.0 | 0.444 | 0.194527 |
| 4.5 | 1.000 | 0.714286 |
| 10.0 | 2.222 | 0.983942 |
| 20.0 | 4.444 | 0.999731 |

The corner value $\lvert H(\omega_0)\rvert = 1/(2\zeta) = 0.714286$ ✓ — a $Q$
bump, and note it is *less* than 1, which is why a geophone is normally used
well above its corner.

**(b)** The ratio of the response at 1 Hz to that at 4.5 Hz is
$0.049371/0.714286 = 0.06912$. The direction of the error depends on the
calibration assumption, and both cases are worth stating:

- If the instrument is **calibrated at 4.5 Hz** — the usual practice, since the
  geophone is used above its corner — then a 1 Hz signal is reported at
  $0.06912$ of its true amplitude: an **underestimate by a factor of 14.5**, a
  gain error of $-93$ %.
- If the response is **ignored altogether**, so that the output is taken to be
  ground velocity, then a 1 Hz signal is reported at $0.049371$ of its true
  value: an underestimate by a factor of **20.3**.

Both are large, and neither can be guessed from the sensor's nominal frequency
alone: the correction factor at any frequency must be read off the measured
transfer function.

**(c)** This is the important subtlety. At low frequency the relative error is
huge (a factor of 20 at 1 Hz), but the absolute ground motion at low frequency
is usually also tiny — the geophone's output at 1 Hz is $0.049\times$ the ground
velocity, which may be below the instrument's own noise floor or below the
digitizer's resolution. Then no correction can recover the information, because
the *signal-to-noise ratio*, not the gain, is what limits the measurement. For a
velocity measurement what matters is therefore the **signal-to-noise ratio at
the frequency of interest**, not the size of the gain error alone: a frequency
where the response is small but the ground motion is large (a teleseismic
surface wave) is measurable, and a frequency where the response is small and the
ground motion is also small is not.

---

## ★★★7 — Instrument-response correction

**(a)** The recorded amplitude is the product of the true amplitude and the
instrument response, so dividing gives

$$A_{\text{corrected}} = \frac{2.16\ \mathrm{mm}}{1.08} = 2.00\ \mathrm{mm}.$$

**(b)** The procedure divides the spectrum by $\hat H(\omega)$, so it is
ill-conditioned wherever $\lvert\hat H\rvert$ is small — for a velocity sensor,
**below its corner frequency**, where $\lvert H\rvert \approx
(\omega/\omega_0)^{2}$. There, dividing by a small number multiplies the noise
by a large one, and the noise is what dominates the recorded signal at those
frequencies. In practice the correction is applied only within a stated passband
and tapered, which is a regularisation: the data are trusted where the sensor is
sensitive, and the rest is not invented. See
[18-inverse-problems](../../../18-inverse-problems/README.md) for why this is an
inverse problem rather than a division.

**(c)** Time-domain deconvolution with an inverse filter gives, in principle,
the same answer, and its advantages are that it handles non-stationary noise
naturally and can be applied causally to a streamed record with a finite
filter length. Its disadvantage is that a *stable, causal* inverse filter must
be designed explicitly (the exact inverse of a physical response is neither
stable nor causal, so the filter is an approximation whose error is hard to
quantify from the filter coefficients alone), and the filter length must be
chosen to balance high-frequency accuracy against ringing. **Advantage:
locality and causality. Disadvantage: the approximation error is less
transparent than a simple passband choice.**

---

## ★★★8 — Resonance or diffusion?

**(a) System A is diffusive; system B is resonant.** Two features decide it, and
they must be read together.

*The phase.* System A's lag *decreases* from 63° to 6° as frequency rises, i.e.
it is largest at low frequency and tends to zero at high frequency. That is the
signature of a first-order lag, $H(\omega) = i\omega\tau/(1+i\omega\tau)$, whose
lag is $90° - \arctan(\omega\tau)$: **maximum lag at low frequency, vanishing at
high frequency.** System B's lag *increases* through exactly $90°$ at
$\omega = 2$ toward $180°$, which is the signature of a second-order resonance.

*The amplitude.* System A rises monotonically and *flattens*: it reaches 0.995
and can go no higher, because $\lvert H\rvert\le1$. System B peaks at 2.5 and
then *falls*: by $\omega = 10$ it has dropped by a factor of 60 from the peak.
An amplitude that turns over is impossible for a first-order (monotone) response
and is the defining feature of a resonance.

A single number is not enough for either: amplitude *ratios* alone cannot
distinguish "rising and flattening" from "rising, peaking and falling" unless the
band extends past the peak, and phase alone is ambiguous between a first-order
lag approaching $90°$ and a resonance passing through it.

**(b)** *System A:* the corner is where $\lvert H\rvert = 1/\sqrt2 = 0.7071$
and the lag is $45°$, both attained at $\omega = 1$. Then
$\tau = 1/\omega_{\text{corner}} = 1.000$ s. Check: at $\omega = 0.5$,
$\lvert H\rvert = 0.5/\sqrt{1.25} = 0.4472$ ✓, and
$90°-\arctan(0.5) = 63.43°$ ✓.

*System B:* the resonance is at the frequency of $90°$ lag, $\omega_0 = 2.000$
rad/s, where $\lvert H\rvert = 2.500 = 1/(2\zeta)$, so
$\zeta = 1/(2\times2.5) = 0.2$ and $Q = 2.5$. Check: at $\omega = 1$ the
denominator is $0.75+0.2i$, giving $\lvert H\rvert = 1/0.7762 = 1.2883$ ✓ and a
lag of $\arctan(0.2/0.75) = 14.93°$ ✓.

**(c)** Far above resonance the $\omega^{2}$ term dominates the denominator, so

$$\lvert H\rvert \approx \frac{1}{(\omega/\omega_0)^{2}}
= \left(\frac{\omega_0}{\omega}\right)^{2} = \left(\frac{2}{\omega}\right)^{2}.$$

| $\omega$ | $(\omega_0/\omega)^{2}$ | tabulated $\lvert H\rvert$ | ratio |
|---|---|---|---|
| 4 | 0.2500 | 0.3221 | 1.288 |
| 10 | 0.0400 | 0.0415 | 1.038 |

The asymptotic law is **approached but not attained** at $\omega = 4$ (29 % high)
and is good to 4 % at $\omega = 10$; it becomes exact only as
$\omega/\omega_0\to\infty$, where the damping term $2i\zeta\omega_0\omega$ becomes
negligible compared with $\omega^{2}$. **Quoting the asymptote as if it held at
$\omega = 2\omega_0$ would be a 29 % error**, which is exactly the kind of
statement that a "high-frequency approximation" invites and a table refutes.

**(d)** The phase at the characteristic frequency is a *structural* marker: it
follows from the order of the governing equation in time, not from the sizes of
the coefficients. A first-order (diffusive) system has a phase that is confined
to $0°$–$90°$ and can never exceed $90°$; a second-order (resonant) system must
pass through $90°$ and reach $180°$, because its transfer function has two poles
and the phase must accumulate $180°$ overall. Amplitude behaviour, by contrast,
depends on the balance of the coefficients: a lightly damped resonance and a
mild first-order lag can look quantitatively similar at frequencies far from
their characteristic frequency. **So read the phase to identify the class of
system, and the amplitude to estimate its parameters.**
