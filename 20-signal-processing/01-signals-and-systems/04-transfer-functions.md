---
id: 20-01-04
title: "Transfer Functions, Poles and Zeros"
level: graduate
prereqs: ["20-01-02", "20-01-03", "01-11-05"]
tags: [signal-processing, transfer-function, poles, zeros, stability, resonance, bilinear]
---

# Transfer Functions, Poles and Zeros

A rational transfer function is the compact description of everything an LTI
system does: the numerator's roots (zeros) are the frequencies it removes, the
denominator's roots (poles) are the frequencies it rings at and the rate at which
it forgets. This lesson derives those identifications, states the stability
theorem that makes them useful, and then treats the two places where the
geophysicist actually meets them: a resonance (an instrument, a building, a
water column) and a discretisation (an analog design that has to run on a
computer).

**All models and data in this module are SYNTHETIC.** Every system below is a
chosen teaching transfer function with a closed-form answer, so each measured
number is checked against algebra rather than against a recording.

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** a difference equation to $H(z) = B(z)/A(z)$ and back, and
   **locate** its poles and zeros with their radii and angles.
2. **State** the stability theorem for causal systems (all poles strictly inside
   the unit circle) and **test** it on a given filter.
3. **Compute** the frequency response as $H(e^{i\omega})$ and **relate** the pole
   radius to the measured decay rate of the impulse response.
4. **Derive** the resonance peak of a second-order analog system — position
   $\omega_r = \omega_0\sqrt{1-2\zeta^{2}}$ and height
   $1/(2\zeta\sqrt{1-\zeta^{2}})$ — and state where the popular $1/(2\zeta)$
   shortcut fails.
5. **Derive** the Butterworth pole pattern and verify the $-3\ \mathrm{dB}$ point
   and the $20N\ \mathrm{dB}$ per decade roll-off.
6. **Derive** the bilinear transform's frequency warp
   $\omega_{\text{a}} = 2f_s\tan(\omega_{\text{d}}/2)$ and **explain** why impulse
   invariance aliases while the bilinear transform does not.
7. **Separate** a system into minimum-phase and all-pass factors and
   **demonstrate** that only the phase — and hence the time-domain energy
   concentration — differs.

## Prerequisites

- [20-01-02 LTI Systems and Impulse Response](02-lti-systems.md) — impulse and
  step responses, BIBO stability.
- [20-01-03 Convolution, Correlation and Filtering](03-convolution-and-filters.md) —
  the filters whose transfer functions are analysed here.
- [01-11-05 The z-Transform](../../01-mathematics/11-complex-analysis/05-z-transform.md) —
  the transform this lesson's algebra lives in.

## 1. Intuition: poles ring, zeros silence

Two intuitions carry most of the weight.

- A **pole** is a frequency the system likes. Feeding it energy near a pole makes
  the output large, and after the input stops the system keeps oscillating at
  that frequency, decaying at a rate set by how close the pole is to the unit
  circle. Poles are memory and resonance.
- A **zero** is a frequency the system refuses. The output at a zero is exactly
  zero regardless of the input, which is why a moving average can annihilate a
  periodic interference
  ([20-01-03 §5.1](03-convolution-and-filters.md)). Zeros are notches.

A transfer function with no poles except at the origin is an FIR filter: it has
no ringing of its own and can only shape what is already there. Add a pole and
you add a memory with a time constant.

## 2. Precise definitions

### 2.1 The z-transform and the transfer function

For a sequence $x[n]$, the **z-transform** is

$$X(z) = \sum_{n=-\infty}^{\infty} x[n]\,z^{-n},$$

defined on an annulus (its **region of convergence**, ROC) where the sum
converges absolutely. The **transfer function** of an LTI system is the
z-transform of its impulse response:

$$H(z) = \frac{Y(z)}{X(z)} = \sum_{n}h[n]z^{-n}
= \frac{b_0 + b_1z^{-1} + \dots + b_Mz^{-M}}
       {1 + a_1z^{-1} + \dots + a_Nz^{-N}}
= \frac{B(z)}{A(z)} .$$

Multiplying through by $A(z)$ and transforming back gives the **difference
equation** $y[n] = \sum_{k=0}^{M}b_kx[n-k] - \sum_{k=1}^{N}a_ky[n-k]$: the same
object in three notations. The roots of $B$ are the **zeros** $z_k$; the roots of
$A$ are the **poles** $p_k$. In factored form

$$H(z) = \frac{b_0}{a_0}\,
\frac{\prod_{k=1}^{M}(1 - z_kz^{-1})}{\prod_{k=1}^{N}(1 - p_kz^{-1})}.$$

### 2.2 Stability, stated exactly

**Theorem (causal stability).** A causal LTI system is BIBO-stable if and only if
every pole lies strictly inside the unit circle, $\lvert p_k\rvert < 1$.

*Why.* For a causal system the ROC is $\lvert z\rvert > r_{\max}$ with
$r_{\max} = \max_k \lvert p_k\rvert$. BIBO stability is equivalent to
$\sum_n \lvert h[n]\rvert < \infty$, which is exactly the statement that the ROC
includes the unit circle; $\lvert z\rvert = 1 > r_{\max}$ iff
$r_{\max} < 1$. A pole *on* the circle gives a marginally stable system (an
undamped oscillator): bounded input, unbounded output at the pole frequency if
the pole is repeated or if the input itself has energy there.

## 3. From pole radius and angle to the impulse response

Expand in partial fractions. For a single real pole $p$,

$$\frac{1}{1-pz^{-1}} \;\longleftrightarrow\; p^{n}u[n],$$

and for a complex-conjugate pair of radius $r$ and angle $\pm\theta$,

$$p^{n}u[n] + (p^{*})^{n}u[n]
= 2r^{n}\cos(n\theta)\,u[n].$$

So the pole's **radius** is the decay per sample and its **angle** is the
oscillation, in radians per sample:

$$\text{decay} = r^{n}, \qquad f_{\text{osc}} = \frac{\theta}{2\pi}f_s,
\qquad \text{time constant} = \frac{-1}{\ln r}\ \text{samples}.$$

*Numerical check (SYNTHETIC).* The system

$$y[n] = 1.2\,y[n-1] - 0.5\,y[n-2] + x[n] - 0.9\,x[n-1]$$

has $A(z) = 1 - 1.2z^{-1} + 0.5z^{-2}$, i.e. $z^{2} - 1.2z + 0.5 = 0$, so

$$p_{1,2} = \frac{1.2 \pm \sqrt{1.44 - 2.0}}{2} = 0.6 \pm 0.374166i,
\qquad \lvert p\rvert = \sqrt{0.36 + 0.14} = \sqrt{0.5} = 0.707107,$$

with angles $\pm31.948^{\circ}$ — so the impulse response is a damped oscillation
at $31.948/360 \times f_s$. The demonstration measures the decay slope of
$\ln\lvert h[n]\rvert$ as $-0.343416$ per sample against $\ln\lvert p\rvert =
-0.346574$: agreement to $1\%$, the residual being that the response is a sum of
two exponentials and the fit window is finite. To fall by $60\ \mathrm{dB}$ takes
$\ln(10^{-3})/\ln\lvert p\rvert = 19.9$ samples $= 199.32\ \mathrm{ms}$ at
$f_s = 100\ \mathrm{Hz}$.

The same filter, evaluated three ways, agrees exactly:

| $\omega$ (rad) | $H(z)$ from the rational form | `freqz` | from $\sum h[n]z^{-n}$ |
|---|---|---|---|
| 0 | $+0.333333$ | $+0.333333$ | — |
| $\pi/4$ | $+1.917229-0.210019i$ | $+1.917229-0.210019i$ | — |
| $\pi/2$ | $+0.934911-0.443787i$ | $+0.934911-0.443787i$ | $+0.934911-0.443787i$ |
| $\pi$ | $+0.703704$ | $+0.703704$ | — |

and the direct time-domain recursion matches `scipy.signal.lfilter` to
$2.78\times10^{-17}$.

## 4. The frequency response, gain and group delay

Setting $z = e^{i\omega}$ evaluates $H$ on the unit circle:

$$H(e^{i\omega}) = \lvert H(e^{i\omega})\rvert\,e^{i\varphi(\omega)} .$$

- **Gain**: $\lvert H\rvert$, the amplitude scaling of that frequency.
- **Phase delay**: $-\varphi(\omega)/\omega$, the delay of a single frequency.
- **Group delay**: $\tau_g(\omega) = -\dfrac{\mathrm d\varphi}{\mathrm d\omega}$,
  the delay of a narrow band of frequencies around $\omega$.

The group delay is the physically meaningful quantity for a transient: expanding
a narrow-band packet about $\omega_0$ shows that it emerges delayed by
$\tau_g(\omega_0)$ and reshaped in proportion to
$\mathrm d\tau_g/\mathrm d\omega$, the *group-delay dispersion*. A constant
$\tau_g$ means every frequency is delayed equally and the waveform survives
unchanged; variation of $\tau_g$ with frequency means the filter — or the Earth —
has dispersed the pulse.

*Numerical check.* For the second-order system above the measured group delay
peaks at $2.368$ samples at $\omega = 0.5714\ \mathrm{rad}$
($23.679\ \mathrm{ms}$ at $100\ \mathrm{Hz}$), while at $\omega\to0$ it is
$-8.333323$ samples. The decomposition shows why: the numerator contributes
$-9.0000$ samples (its zero at $z = 0.9$ sits close to $z = 1$ and has a large
positive phase slope) and the denominator $+0.6667$. **Negative group delay is
not acausality**; it is the reshaping of the leading edge of a pulse by a
numerator zero. Reporting group delay without saying whether it refers to the
whole system or to its denominator is a common source of confusion, especially
when comparing an instrument response with a processing filter.

## 5. Continuous prototypes: resonance and Butterworth

### 5.1 A second-order resonance, derived

Take

$$H(s) = \frac{\omega_0^{2}}{s^{2} + 2\zeta\omega_0s + \omega_0^{2}}.$$

With $s = i\omega$,

$$\lvert H(i\omega)\rvert^{2} =
\frac{\omega_0^{4}}{(\omega_0^{2}-\omega^{2})^{2} +
4\zeta^{2}\omega_0^{2}\omega^{2}} .$$

Differentiating the denominator with respect to $\omega^{2}$ and setting it to
zero gives the **resonant frequency**

$$\omega_r = \omega_0\sqrt{1-2\zeta^{2}} \quad (\zeta < 1/\sqrt2),$$

and substituting back gives the **peak height**

$$\lvert H(i\omega_r)\rvert = \frac{1}{2\zeta\sqrt{1-\zeta^{2}}}.$$

The often-quoted $1/(2\zeta)$ is the small-$\zeta$ limit and is always an
underestimate; for $\zeta \ge 1/\sqrt2 = 0.707107$ there is no peak at all, and
the shortcut silently predicts one.

*Numerical check* (numerically maximising $\lvert H(i\omega)\rvert$ on a fine
grid, $\omega_0 = 1\ \mathrm{rad/s}$):

| $\zeta$ | measured peak | $\omega_r$ (exact) | $1/(2\zeta)$ | exact peak |
|---|---|---|---|---|
| 0.05 | 10.0125 | 0.9975 | 10.0000 | 10.0125 |
| 0.10 | 5.0252 | 0.9899 | 5.0000 | 5.0252 |
| 0.25 | 2.0656 | 0.9354 | 2.0000 | 2.0656 |
| 0.50 | 1.1547 | 0.7071 | 1.0000 | 1.1547 |

The measured and exact columns agree to all printed digits; the $1/(2\zeta)$
column disagrees by $12.5\%$ at $\zeta = 0.25$ and $15.5\%$ at $\zeta = 0.5$.

### 5.2 Butterworth poles, derived

The order-$N$ Butterworth low-pass with corner $\omega_c$ is
$\lvert H(i\omega)\rvert^{2} = 1/(1+(\omega/\omega_c)^{2N})$. Its poles are the
$N$ roots of $(-1)^{N+1}(s/\omega_c)^{2N} = -1$ in the left half-plane:

$$s_k = \omega_c\exp\!\Bigl[i\pi\frac{2k + N + 1}{2N}\Bigr],
\qquad k = 0,1,\dots,N-1 .$$

They lie on a semicircle of radius $\omega_c$, equally spaced in angle by
$\pi/N$.

*Numerical check* ($N = 4$, $\omega_c = 2\ \mathrm{rad/s}$): the analytic poles
are $-0.765367 \pm 1.847759i$ and $-1.847759 \pm 0.765367i$, each with
$\lvert s_k\rvert = 2.000000$ and angles $\pm112.5^{\circ}, \pm157.5^{\circ}$.
They match `scipy.signal.butter(4, 2, analog=True)` to
$3.24\times10^{-15}$ (a permutation of the root ordering). The measured
magnitudes are

| $\omega$ (rad/s) | 0.1 | 1.0 | 2.0 | 4.0 |
|---|---|---|---|---|
| $\lvert H\rvert$ | 1.000000 | 0.998053 | 0.707107 | 0.062378 |
| dB | $-0.000$ | $-0.017$ | $-3.010$ | $-24.099$ |

consistent with the $-3\ \mathrm{dB}$ point at $\omega = \omega_c$ and a roll-off
of $20N = 80\ \mathrm{dB}$ per decade.

## 6. Discretisation: two mappings, two failure modes

### 6.1 The bilinear transform

$$s = 2f_s\,\frac{1-z^{-1}}{1+z^{-1}}
\;\;\Longleftrightarrow\;\;
\omega_{\text{a}} = 2f_s\tan\!\Bigl(\frac{\omega_{\text{d}}}{2}\Bigr) .$$

The mapping sends the whole $i\omega$ axis onto the unit circle exactly once, so
it cannot alias; the price is **frequency warping**, which compresses the analog
axis into $0 \le \omega_{\text{d}} < \pi$. *Derivation for the test system.* With
$H(s) = 1/(s+1)$ and $f_s = 100\ \mathrm{Hz}$:

$$H(z) = \frac{1}{\frac{200(1-z^{-1})}{1+z^{-1}} + 1}
= \frac{1+z^{-1}}{201 - 199z^{-1}}
= \frac{0.004975\,(1+z^{-1})}{1 - 0.990050\,z^{-1}},$$

which is exactly the coefficients the demonstration prints
($b = [0.004975,\ 0.004975]$, $a = [1,\ -0.990050]$), with
$1/201 = 0.004975$.

*Numerical check of the warp.* Using
$\omega_{\text{a}} = 2f_s\tan(\pi f/f_s)$ and the *analog* magnitude
$1/\sqrt{1+\omega_{\text{a}}^{2}}$:

| $f$ (Hz) | 2 | 10 | 30 | 45 |
|---|---|---|---|---|
| $\omega_{\text{a}}$ (rad/s) | 12.5829 | 64.9839 | 275.2764 | 1262.7503 |
| $1/\sqrt{1+\omega_{\text{a}}^{2}}$ | 0.079223 | 0.015387 | 0.003633 | 0.000792 |
| measured $\lvert H_{\text{bilinear}}\rvert$ | 0.079223 | 0.015387 | 0.003633 | 0.000792 |

The two columns are equal to all printed digits at every frequency, including
45 Hz where the digital response is 4.5 times *smaller* than the analog one
(0.000792 against 0.003537): the bilinear transform preserves the response at the
warped frequency and nowhere else.

### 6.2 Impulse invariance

Sampling the analog impulse response, $h[n] = \Delta t\,h(n\Delta t)$, gives
$b = [0.01]$, $a = [1, -0.990050]$ for the same prototype. It matches the analog
response slightly *better* at low frequency than the bilinear transform
(0.079776 against 0.079327 at 2 Hz) because it does not warp — but its
high-frequency response is contaminated by **aliasing**: the analog tail above
Nyquist folds back, so at 45 Hz the impulse-invariant filter returns 0.005088
against an analog 0.003537, i.e. $44\%$ too large, and at the Nyquist frequency
the error is unbounded. Impulse invariance is the right tool only when the analog
response is negligible above Nyquist; the bilinear transform is the right tool
when it is not.

## 7. Minimum-phase and all-pass factors

Any rational $H$ with no poles on the unit circle can be written

$$H(z) = H_{\min}(z)\,H_{\text{ap}}(z),$$

where $H_{\min}$ has all its zeros inside the unit circle and $H_{\text{ap}}$ is
**all-pass**, $\lvert H_{\text{ap}}(e^{i\omega})\rvert = 1$ for every $\omega$.
The construction: for each zero $z_k$ outside the circle, replace it by
$1/z_k^{*}$ and multiply by the all-pass factor
$-(1/z_k) \frac{z^{-1}-z_k^{*}}{1-z_kz^{-1}}$.

Three consequences, all measured on a synthetic pair:

- **Identical magnitude.** $h_{\min} = [1, -0.8, 0.15]$ (zeros $0.5$ and $0.3$)
  and $h_{\max} = [0.15, -0.8, 1]$ (zeros $2$ and $10/3$) differ in their
  magnitude spectra by at most $8.88\times10^{-16}$. From a magnitude spectrum
  alone you cannot tell them apart.
- **Different phase.** At $\omega = 0.5\ \mathrm{rad}$ the minimum-phase factor
  has $+0.596480\ \mathrm{rad}$ and the maximum-phase factor $-1.596480\
  \mathrm{rad}$; the difference is exactly the all-pass phase.
- **Different energy concentration.** Partial energy in the first $L$ samples:

| $L$ | 1 | 2 | 3 |
|---|---|---|---|
| minimum-phase | 1.000000 | 1.640000 | 1.662500 |
| maximum-phase | 0.022500 | 0.662500 | 1.662500 |
| ratio | 44.444 | 2.475 | 1.000 |

The minimum-phase filter puts $44\times$ more energy in its first sample. This is
the time-domain face of the same statement, and it is why seismic
deconvolution prefers a minimum-phase estimate of the wavelet: the front-loaded
version is the one that concentrates the reflectivity at the right times
([20-04 Deconvolution and Inverse Filtering](../04-deconvolution-and-inverse-filtering/README.md)).

## 8. Units and dimensional analysis

| Quantity | Unit | Note |
|---|---|---|
| $z$ | dimensionless | $z = e^{i\omega}$, $\omega$ in rad/sample |
| $H(z)$ | output per input | dimensionless if both share units |
| $b_k$ | output per input | |
| $a_k$ | dimensionless | the recursion's feedback weights |
| pole radius | dimensionless | must be $<1$ for causal stability |
| pole angle | rad/sample | $\times \Delta t$ for a frequency in rad/s |
| $s$ | $\mathrm{s^{-1}}$ | so $H(s)$ has the units of $h(t)$ times seconds |
| $\zeta$ | dimensionless | $-1/\ln$ of a decay ratio, for a discrete pole |

In continuous time a pole with $\lvert s_k\rvert$ in $\mathrm{s^{-1}}$ has a decay
time constant $1/\lvert \mathrm{Re}\,s_k\rvert$ in seconds; in discrete time the
pole radius is dimensionless and the time constant is
$-1/\ln r$ **samples**, which becomes seconds only after multiplying by
$\Delta t$. Mixing the two is the most common error in transcribing an analog
instrument response to a digital filter.

## 9. Worked examples

### Example 1 — poles, angles and an oscillation frequency

For $A(z) = 1 - 1.2z^{-1} + 0.5z^{-2}$: $r = \sqrt{0.5} = 0.707107$,
$\theta = 31.948^{\circ} = 0.557599\ \mathrm{rad/sample}$. At
$f_s = 100\ \mathrm{Hz}$,

$$f_{\text{osc}} = \frac{\theta}{2\pi}f_s = \frac{0.557599}{6.283185}\times100
= 8.875\ \mathrm{Hz},$$

and the response should decay by $1/e$ in $-1/\ln r = 2.885$ samples
$= 28.85\ \mathrm{ms}$. The two statements are the same statement: an amplitude
ratio of $10^{-3}$ (60 dB) needs $n/\tau = \ln 1000 = 6.907755$ time constants,
so $n = 6.907755 \times 2.885 = 19.93$ samples — exactly the measured 19.9. The
measured decay slope $-0.343416$ differs from $\ln r = -0.346574$ by $1\%$
because the response is a sum of two exponential terms and the fit window is
finite.

### Example 2 — designing a notch from a zero

To place an exact null at $\omega_0 = 2\pi f_0/f_s$, put a zero at
$z = e^{i\omega_0}$ and its conjugate: $B(z) = (1 - e^{i\omega_0}z^{-1})
(1 - e^{-i\omega_0}z^{-1}) = 1 - 2\cos(\omega_0)z^{-1} + z^{-2}$. For
$f_0 = 10\ \mathrm{Hz}$ at $f_s = 100\ \mathrm{Hz}$, $\omega_0 = 0.628319\ \mathrm{rad}$
and $2\cos\omega_0 = 1.618034$, so $B = [1, -1.618034, 1]$. The zeros sit *on* the
unit circle, so the notch is infinitely deep at exactly one frequency and shallow
nearby — the same sharpness measured for the moving average in
[§5 of the previous lesson](03-convolution-and-filters.md), and the reason
notch design in practice moves the zeros slightly inside the circle (to make the
notch robust to a drifting interference frequency) at the cost of depth.

### Example 3 — the two delay contributions

For the system of Section 3, at $\omega\to0$:

$$\tau_g^{\text{num}} = -\frac{0.9}{1-0.9} = -9.0000\ \text{samples},
\qquad
\tau_g^{\text{den}} = \frac{2\,\mathrm{Re}\left[\frac{p}{1-p}\right]}{1}
= 2\,\mathrm{Re}\!\left[\frac{0.6+0.374166i}{0.4-0.374166i}\right]
= 2(0.333333) = +0.6667\ \text{samples},$$

totalling $-8.333323$ as measured. The general small-$\omega$ result is

$$\boxed{\;\tau_g(0) = -\sum_i \frac{a_i}{1-a_i} + \sum_k \frac{p_k}{1-p_k}\;}
\qquad\text{for real zeros } a_i \text{ and poles } p_k \text{ with }
\lvert a_i\rvert,\lvert p_k\rvert < 1,$$

which follows from $\arg(1-c e^{-i\omega}) \approx c\omega/(1-c)$ for small
$\omega$. Check: $-0.9/0.1 + 0.6667 = -8.3333$. ✔ The practical lesson is that a
*numerator* with zeros near $z = 1$ buys an apparent advance at low frequency.
That is exactly what a differentiator does, and it is why differentiating a
seismic trace shifts its apparent onset earlier while leaving the arrival alone.

## 10. Python demonstration

`code/transfer_functions_demo.py` is print-only, single-process, uses `numpy`
and `scipy.signal`, and runs in about a second. It:

1. finds the zeros and poles of a second-order IIR filter and tests stability;
2. computes $H(e^{i\omega})$ three ways and compares with a time-domain
   recursion;
3. measures the impulse-response decay against the pole radius;
4. measures the resonance peak against $1/(2\zeta)$ and the exact expression;
5. verifies the Butterworth pole pattern and the $-3\ \mathrm{dB}$ frequency;
6. discretises the same prototype by bilinear transform and by impulse
   invariance, and verifies the bilinear warp numerically;
7. contrasts minimum-phase and maximum-phase factors;
8. splits the group delay into its numerator and denominator parts.

```bash
cd 20-signal-processing/01-signals-and-systems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python transfer_functions_demo.py
```

## 11. Assumptions and regime of validity

1. **Rational, finite-order, LTI.** Real instrument responses are rational but of
   high order and are usually tabulated (poles and zeros plus a normalisation
   constant) rather than used as a formula; the identification of radius with
   decay assumes no nearby pole-zero cancellation, and a *cancelling* pair
   contributes nothing to the response even though it appears in the tables.
2. **The stability theorem is for causal systems.** An anticausal system is
   stable with poles *outside* the circle, and a two-sided system may be stable
   with poles on both sides. State the ROC whenever you state the poles.
3. **Marginal stability is not stability.** A pole exactly on the unit circle
   gives a growing output to a sinusoidal input at that frequency; numerically,
   its measured decay slope is zero and a long enough record will show the
   growth.
4. **The $1/(2\zeta)$ resonance rule is an approximation.** It is exact only in
   the limit $\zeta\to0$; the error is $12.5\%$ at $\zeta = 0.25$ and there is no
   peak at all above $\zeta = 1/\sqrt2$.
5. **The bilinear transform preserves the magnitude only at the warped
   frequency.** Away from it, and for the phase, the digital filter is a
   different function; pre-warp the critical frequency (usually the corner or the
   passband edge) or the specification will be missed.
6. **Impulse invariance requires negligible analog response above Nyquist.**
   Otherwise the aliased tail is a systematic error of tens of per cent.
7. **Group delay describes narrow-band signals.** A broadband transient under a
   filter with strong group-delay dispersion is distorted in a way no single
   delay number captures; the second derivative $\mathrm d\tau_g/\mathrm d\omega$
   is then the quantity you must also report.

## 12. Exercises

- [`exercises/04-transfer-functions-exercises.md`](./exercises/04-transfer-functions-exercises.md)
- [`exercises/04-transfer-functions-solutions.md`](./exercises/04-transfer-functions-solutions.md)

## 13. Common pitfalls

1. **Confusing the pole *radius* with the pole *magnitude in dB*.** A radius of
   $0.9$ is only $-0.92\ \mathrm{dB}$ per sample but takes $65.6$ samples to decay
   by $60\ \mathrm{dB}$.
2. **Reading a pole radius as a frequency.** Radius is decay; angle is
   frequency. A real pole resonates at DC (or Nyquist if negative).
3. **Using $1/(2\zeta)$ for a peaked system.** It under-reports the peak and
   predicts a peak where none exists.
4. **Quoting bilinear coefficients as "the analog response".** The warp at the
   Nyquist frequency is a factor $2f_s\tan(\pi/2)$; the digital filter's corner
   frequency is *not* the analog one unless pre-warped.
5. **Assuming minimum phase.** A recorded wavelet is minimum phase only if the
   physics produced it that way; a magnitude spectrum cannot tell you, and the
   deconvolution result depends on the assumption.
6. **Ignoring the numerator's group delay.** A zero near $z=1$ contributes a
   large negative delay; the whole-system group delay, not the denominator's, is
   what shapes the record.
7. **Forgetting that FIR means no poles.** A pure FIR has poles only at
   $z = 0$; it is unconditionally stable and its group delay is bounded by
   $(M-1)/2$ for a symmetric kernel.

## 14. Mastery checkpoint

Without notes:

**(a)** Write the difference equation, $H(z)$, zeros and poles of the system
with $b = [1, 0.5]$ and $a = [1, -1.1, 0.3]$; state whether it is stable and give
the two pole radii.
**(b)** From the poles alone, estimate the number of samples for the impulse
response to fall by $60\ \mathrm{dB}$, and the oscillation frequency in Hz at
$f_s = 250\ \mathrm{Hz}$.
**(c)** Derive $\omega_r$ and the peak height for $\zeta = 0.2$, and compute the
error made by quoting $1/(2\zeta)$.
**(d)** Design a digital notch at $50\ \mathrm{Hz}$ with $f_s = 500\ \mathrm{Hz}$
and give $B = [b_0, b_1, b_2]$; then state what happens to the notch depth if
the interference drifts to $50.2\ \mathrm{Hz}$.
**(e)** Explain in three sentences why the bilinear transform cannot alias and
why it still distorts a broadband signal.
**(f)** Give the group delay at DC of $H(z) = (1-0.5z^{-1})/(1-0.8z^{-1})$ from
the boxed formula and verify it from a phase evaluation.

Answers for (a)–(d) are in the
[solutions](./exercises/04-transfer-functions-solutions.md).

## 15. Related modules

- [20-01-03 Convolution, Correlation and Filtering](03-convolution-and-filters.md) —
  where the zeros of a moving average were measured.
- [20-01-05 Sampling, Nyquist and Reconstruction](05-sampling-theory.md) — the
  sampling conditions that make these digital filters meaningful.
- [20-02-01 Practical DFT/FFT](../02-fourier-and-spectral-analysis/01-dft-fft-practice.md) —
  the discrete transform of finite records, which is where these transfer
  functions are measured.
- [20-03 Digital Filtering](../03-digital-filtering/README.md) — systematic design
  to a specification, including the pole-placement rules derived here.
- [20-04 Deconvolution and Inverse Filtering](../04-deconvolution-and-inverse-filtering/README.md) —
  inverting $H$, whose zeros are where the inverse does not exist.
- [01-11 Complex Analysis](../../01-mathematics/11-complex-analysis/README.md) —
  the $z$- and Laplace-transform machinery used throughout.
