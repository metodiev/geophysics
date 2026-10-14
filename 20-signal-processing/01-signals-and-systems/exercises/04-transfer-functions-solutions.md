# Solutions — 20-01-04 Transfer Functions, Poles and Zeros

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All models are **SYNTHETIC**.

Lesson: [04 Transfer Functions](../04-transfer-functions.md).

---

## ★1 — Difference equation, poles, zeros, stability

$$y[n] = 1.1\,y[n-1] - 0.3\,y[n-2] + x[n] + 0.5\,x[n-1],$$

$$H(z) = \frac{1 + 0.5z^{-1}}{1 - 1.1z^{-1} + 0.3z^{-2}}
= \frac{z^{2} + 0.5z}{z^{2} - 1.1z + 0.3}.$$

**Zero:** $1 + 0.5z^{-1} = 0 \Rightarrow z = -0.5$, radius $0.5$, angle
$180^{\circ}$ (a null at Nyquist).

**Poles:** $z^{2} - 1.1z + 0.3 = 0 \Rightarrow
z = \frac{1.1 \pm \sqrt{1.21 - 1.2}}{2} = \frac{1.1\pm0.1}{2}$, i.e.
$z = 0.6$ and $z = 0.5$ — both real, radii $0.6$ and $0.5$, angles
$0^{\circ}$. Both radii are $< 1$, so the causal system is **stable**.

**DC gain:** $H(1) = (1+0.5)/(1-1.1+0.3) = 1.5/0.2 = 7.5$.

Real poles mean no oscillation: the impulse response is a sum of two decaying
exponentials with decay rates $0.6^{n}$ and $0.5^{n}$. The decaying exponential
with the larger radius dominates at late times.

---

## ★2 — Poles alone give decay and frequency

Radius $r = 0.9$, angle $\theta = 25^{\circ} = 0.436332\ \mathrm{rad}$.

- Time constant: $\tau = -1/\ln r = -1/\ln 0.9 = 9.4912$ samples
  ($= 47.46\ \mathrm{ms}$ at $f_s = 200\ \mathrm{Hz}$).
- $60\ \mathrm{dB}$ (amplitude factor $10^{-3}$) takes
  $n = \ln(1000)\times\tau = 6.907755\times9.4912 = 65.55$ samples
  $= 327.8\ \mathrm{ms}$.
- Oscillation: $f = \theta f_s/(2\pi) = 0.436332\times200/6.283185
  = 13.889\ \mathrm{Hz}$.

Note the exactitude: $\tau$ and $f$ follow from the pole position alone, with no
knowledge of the numerator — provided no zero sits near the pole.

---

## ★3 — Resonance position and height

$\omega_0 = 2\pi\cdot10 = 62.831853\ \mathrm{rad/s}$, $\zeta = 0.05$.

$$\omega_r = \omega_0\sqrt{1-2\zeta^{2}} = 62.831853\sqrt{1-0.005}
= 62.674607\ \mathrm{rad/s} \Rightarrow
f_r = \frac{\omega_r}{2\pi} = 9.975\ \mathrm{Hz},$$

$$\lvert H(i\omega_r)\rvert = \frac{1}{2\zeta\sqrt{1-\zeta^{2}}}
= \frac{1}{0.1\times0.998749} = 10.012523,
\qquad \frac{1}{2\zeta} = 10.000000 .$$

The shortcut is low by $0.125\%$ here — the difference grows with $\zeta$: at
$\zeta = 0.25$ the shortcut is low by $3.3\%$, and at $\zeta = 0.5$ by $15.5\%$.

---

## ★4 — Designing a resonator from its specification

Requirements: ring at $f_0 = 25\ \mathrm{Hz}$ with time constant
$\tau = 0.2\ \mathrm{s}$ at $f_s = 500\ \mathrm{Hz}$.

$$r = e^{-\Delta t/\tau} = e^{-1/(500\times0.2)} = e^{-0.01} = 0.990050,
\qquad \theta = 2\pi\frac{25}{500} = 0.314159\ \mathrm{rad},$$

$$a_1 = -2r\cos\theta = -2(0.990050)(0.951057) = -1.883187, \qquad
a_2 = r^{2} = 0.980199 .$$

So $A(z) = 1 - 1.883187z^{-1} + 0.980199z^{-2}$, giving the recursion
$y[n] = 1.883187\,y[n-1] - 0.980199\,y[n-2] + b\,x[n]$.

**Group delay at the resonance:** a numerical evaluation of
$\tau_g = -\mathrm d\varphi/\mathrm d\omega$ gives a peak of $99.03$ samples at
$25.0001\ \mathrm{Hz}$, i.e. $0.19806\ \mathrm{s}$ — about one ring-down time
$\tau = 0.2\ \mathrm{s}$. That identification is a rule of thumb for a
high-$Q$ resonator, not an identity.

**Which numbers are exact, which are approximations.**

- $r = e^{-\Delta t/\tau}$ and $a_2 = r^{2}$ are **exact**: they implement the
  stated requirement "amplitude decays by $1/e$ in $\tau$" exactly at the sample
  points.
- $\theta = 2\pi f_0\Delta t$ is exact because $25\ \mathrm{Hz}$ is an exact
  multiple of $0.5\ \mathrm{Hz}$, the DFT spacing; had $f_0 = 25.3\ \mathrm{Hz}$
  been asked for, the pole would sit at the nearest representable angle and the
  peak would be displaced by up to half a bin of the pole angle.
- The peak gain is not specified here; with the DC-normalised numerator
  $b = 1 - 2r\cos\theta + r^{2} = 0.097012$, the exact peak gain is

$$\lvert H(e^{i\theta})\rvert = \frac{b}{(1-r)\sqrt{1-2r\cos(2\theta)+r^{2}}}
= \frac{0.097012}{0.009950\times0.615034} = 15.8525,$$

which is $23.99\ \mathrm{dB}$. Check the building blocks: $1-r = 0.009950$ (the
pole-to-zero distance along the radius) and
$\sqrt{1-2r\cos2\theta+r^{2}} = 0.615034$. The product form shows why a
resonator's gain is set by $1/(1-r)$ scaled by the numerator, so moving the
required time constant from $0.2\ \mathrm{s}$ to $0.4\ \mathrm{s}$ *doubles*
$(1-r)$ and halves the gain.

---

## ★5 — Bilinear design with and without pre-warping

**Pre-warped.** The corner must land at $f_c = 10\ \mathrm{Hz}$ with
$f_s = 100\ \mathrm{Hz}$, so the analog prototype is placed at the *warped*
frequency

$$\omega_{\text{a}} = 2f_s\tan\!\left(\frac{\pi f_c}{f_s}\right)
= 200\tan(0.314159) = 200\times0.324920 = 64.983939\ \mathrm{rad/s}.$$

Designing $H(s) = \omega_{\text{a}}/(s+\omega_{\text{a}})$ and applying the
bilinear transform gives

$$b = [0.245237,\ 0.245237], \qquad a = [1,\ -0.509525].$$

The measured $-3\ \mathrm{dB}$ frequency is $9.9998\ \mathrm{Hz}$ — the design
target, to a part in $10^{4}$ (the residual is the frequency grid of the search).
Note the sum of coefficients: $\sum b/(1 + \sum a_{>0}) = 0.245237\times2/(1 - 0.509525) = 1.000$,
so the DC gain is exactly 1 as it must be for a low-pass.

**Unwarped.** Placing the analog corner at $\omega_c = 2\pi f_c = 62.831853$
gives $b = [0.239057,\ 0.239057]$, $a = [1, -0.521886]$, and the measured
$-3\ \mathrm{dB}$ frequency is $9.6893\ \mathrm{Hz}$ — the corner is **$3.1\%$
low**. The error is systematic and grows with $f_c/f_s$: the warp is
$2f_s\tan(\pi f_c/f_s)$ against the intended $2\pi f_c$, and
$\tan x > x$ for $0<x<\pi/2$.

---

## ★6 — Derivation of the resonance peak

$$\lvert H(i\omega)\rvert^{2} =
\frac{\omega_0^{4}}{(\omega_0^{2}-\omega^{2})^{2}
+ 4\zeta^{2}\omega_0^{2}\omega^{2}} .$$

Write $u = \omega^{2}$; the denominator is
$D(u) = (\omega_0^{2}-u)^{2} + 4\zeta^{2}\omega_0^{2}u$, so maximising
$\lvert H\rvert^{2}$ means minimising $D$:

$$\frac{\mathrm dD}{\mathrm du} = -2(\omega_0^{2}-u) + 4\zeta^{2}\omega_0^{2} = 0
\;\Longrightarrow\; u = \omega_0^{2}(1-2\zeta^{2}).$$

Since $u = \omega^{2} \ge 0$, a positive solution exists only for
$\zeta < 1/\sqrt2$. Hence

$$\omega_r = \omega_0\sqrt{1-2\zeta^{2}}, \qquad
\lvert H(i\omega_r)\rvert = \frac{1}{2\zeta\sqrt{1-\zeta^{2}}} .$$

**For $\zeta = 0.1$:** $\omega_r = \omega_0\sqrt{0.98} = 0.989949\omega_0$ and
$\lvert H\rvert_{\max} = 1/(0.2\sqrt{0.99}) = 1/0.198997 = 5.025189$, against
$1/(2\zeta) = 5.000000$ — the shortcut is low by $0.50\%$.

**Largest $\zeta$ with a peak:** $\zeta = 1/\sqrt2 = 0.707107$. There
$\omega_r = 0$ and $\lvert H\rvert_{\max} = 1/(2\zeta\sqrt{1-\zeta^{2}})
= 1/(2\cdot0.707107\cdot0.707107) = 1.000000$: the response is maximally flat —
monotone, with the $-3\ \mathrm{dB}$ point exactly at $\omega_0$ and no
overshoot. Above that value the response is monotone with a rounded corner, and
quoting $1/(2\zeta)$ would predict a peak that does not exist.

---

## ★7 — Two near-cancelling pole–zero tables

Both tables have a pole at $p = 0.98$. Table A has a zero at $0.975$; Table B a
zero at $0.9995$.

$$H(1) = \frac{1-a}{1-p}: \qquad
\text{A: } \frac{0.025}{0.02} = 1.250000, \qquad
\text{B: } \frac{0.0005}{0.02} = 0.025000 .$$

The two DC gains differ by a **factor 50** while the pole is identical and both
zeros are "near" it. Group delays at DC from the boxed formula:

$$\tau_g(0) = -\frac{a}{1-a} + \frac{p}{1-p}:
\qquad \text{A: } -39 + 49 = +10\ \text{samples}, \qquad
\text{B: } -1999 + 49 = -1950\ \text{samples},$$

and a numerical phase-slope evaluation returns $+10.00$ and $-1943.9$ samples
respectively (the second differs because the true group delay varies rapidly with
frequency near a near-cancellation, so a finite-difference at $\omega = 0$ on a
grid is itself approximate). The gain differs by a factor 50 and the low-frequency
delay by a factor $-195$ and a change of sign.

**Which table to trust: neither, from the tables alone.** A pole–zero pair
0.005 apart is inside the uncertainty of any tabulated sensor calibration; the
pair is best regarded as a *cancellation* and its exact positions carry almost no
information. The measurement that settles it is a direct gain-and-phase
measurement at the frequencies of interest — ideally a swept-sine or
broadband-noise calibration with a coherence estimate, so that the frequency
range where the response is actually determined is visible. If the calibration
cannot resolve the pair, report the sensor as a single-pole response with an
uncertainty band wide enough to contain both tables.

---

## ★8 — A notch that cannot be built as specified

Specification: $\ge 40\ \mathrm{dB}$ attenuation over $49.5$–$50.5\ \mathrm{Hz}$,
gain within $0.5\ \mathrm{dB}$ below $40\ \mathrm{Hz}$, $f_s = 500\ \mathrm{Hz}$.

**Try the standard two-zero/two-pole notch.** Place zeros at
$e^{\pm i\omega_0}$ with $\omega_0 = 2\pi(50)/500 = 0.628319\ \mathrm{rad}$ and
poles at $re^{\pm i\omega_0}$, normalising the DC gain to 1:

$$b = K\,[1,\ -2\cos\omega_0,\ 1], \quad
a = [1,\ -2r\cos\omega_0,\ r^{2}], \quad
K = \frac{1-2r\cos\omega_0+r^{2}}{2(1-\cos\omega_0)} .$$

The **numerator alone** sets the depth at the band edge. Since

$$1 - 2\cos(\omega_0)z^{-1} + z^{-2} = 2z^{-1}\bigl(\cos\omega - \cos\omega_0\bigr)
\quad\text{on } z = e^{i\omega},$$

the unnormalised magnitude at $49.5\ \mathrm{Hz}$ is
$2\lvert\cos\omega-\cos\omega_0\rvert$ with
$\omega = 0.622035$, i.e.

$$\frac{\lvert B\rvert}{\lvert B(0)\rvert} =
\frac{2(0.0036928)}{2(0.190983)} = 0.019337
\quad\Longrightarrow\quad -34.31\ \mathrm{dB}.$$

Measured with the poles included, the attenuation is $-35.11\ \mathrm{dB}$ at
$r = 0.5$, $-33.00\ \mathrm{dB}$ at $r = 0.7$ and $-24.30\ \mathrm{dB}$ at
$r = 0.9$ — the poles add at most about $1\ \mathrm{dB}$ and otherwise *reduce*
the attenuation as $r$ approaches the zeros:

| $r$ | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 |
|---|---|---|---|---|---|
| $\lvert H(49.5\ \mathrm{Hz})\rvert$ (dB) | $-35.11$ | $-34.47$ | $-33.00$ | $-30.12$ | $-24.30$ |
| $\lvert H(40\ \mathrm{Hz})\rvert$ (dB) | $-9.45$ | $-8.84$ | $-7.56$ | $-5.32$ | $-2.11$ |

**The specification is unachievable with this structure.** The best attenuation
at $49.5\ \mathrm{Hz}$ is about $-35\ \mathrm{dB}$, set by the zero pattern, and
that comes with a $-9.4\ \mathrm{dB}$ gain error at $40\ \mathrm{Hz}$ — nineteen
times the $0.5\ \mathrm{dB}$ budget. Requirements fail in *both* directions at
once, so no choice of $r$ rescues them.

**What would work.** A $\pm0.5\ \mathrm{Hz}$ notch at $50\ \mathrm{Hz}$ demands a
null of finite width, i.e. zeros spread over the band rather than a single
conjugate pair: a higher-order elliptic or Chebyshev-II design with several zero
pairs inside $49.5$–$50.5\ \mathrm{Hz}$, plus an equaliser that restores the
passband. The difficulty is the ratio of band half-width to guard distance,
$0.5\ \mathrm{Hz}$ against $10\ \mathrm{Hz}$, i.e. $Q \approx 50$; that is what
drives the required order. The alternative answer — equally legitimate — is to
challenge the specification: a $40\ \mathrm{dB}$ suppression over a $1\
\mathrm{Hz}$-wide band is usually more than the application needs, and loosening
the band to $\pm0.2\ \mathrm{Hz}$ brings a single second-order section back into
range.


---

## Mastery checkpoint answers

**(a)** With $b = [1, 0.5]$, $a = [1, -1.1, 0.3]$:

$$y[n] = 1.1\,y[n-1] - 0.3\,y[n-2] + x[n] + 0.5\,x[n-1],$$
$$H(z) = \frac{1 + 0.5z^{-1}}{1 - 1.1z^{-1} + 0.3z^{-2}},$$

zero at $z = -0.5$; poles at $z = 0.6$ and $z = 0.5$ (both real), so both radii
are below 1 and the causal system is **stable**.

**(b)** The larger pole radius is $r = 0.6$, so the time constant is
$-1/\ln 0.6 = 1.9576$ samples and $60\ \mathrm{dB}$ (an amplitude factor
$10^{-3}$) takes $\ln(1000)\times1.9576 = 13.52$ samples. **There is no
oscillation**: both poles are real, so the impulse response is a sum of two
decaying exponentials with no imaginary part and no oscillatory frequency. At
$f_s = 250\ \mathrm{Hz}$ the response is a decay, not a ring.

**(c)** $\zeta = 0.2$: $\omega_r = \omega_0\sqrt{1-2(0.04)} = 0.959166\,\omega_0$
and $\lvert H\rvert_{\max} = 1/(2\zeta\sqrt{1-\zeta^{2}}) = 2.551552$, against
the shortcut $1/(2\zeta) = 2.500000$ — an error of $2.06\%$.

**(d)** $\omega_0 = 2\pi(50)/500 = 0.628319\ \mathrm{rad}$,
$2\cos\omega_0 = 1.618034$, so the zero pair sits on the unit circle at
$B = [1,\,-1.618034,\,1]$ (normally scaled by $K$ to set the DC gain). If the
interference drifts to $50.2\ \mathrm{Hz}$ the notch depth collapses from the
numerical floor to about $-50.6\ \mathrm{dB}$; at $51\ \mathrm{Hz}$ it is only
$-36.5\ \mathrm{dB}$. The notch is a point null, and a drifting interferer needs
the zeros pulled slightly inside the unit circle (wider, shallower notch) or a
wider stopband design.
