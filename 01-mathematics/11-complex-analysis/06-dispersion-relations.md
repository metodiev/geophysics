---
id: 01-11-06
title: "Dispersion Relations and Causality in Wave Physics"
level: doctoral
prereqs: ["01-11-03", "01-11-04", "02-03-07"]
estimated_minutes: 90
tags: [causality, kramers-kronig, attenuation, dispersion, minimum-phase]
---

# Dispersion Relations and Causality in Wave Physics

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the statement that causality of a linear response is equivalent to
   analyticity of its transfer function in one half of the complex frequency
   plane, and state which half plane belongs to which sign convention.
2. **Derive** the Kramers–Kronig relations from that analyticity by indenting a
   contour around a pole on the real axis, and write them in the forms used for
   a transfer function and for a modulus.
3. **Verify** the relations numerically in both directions, using a principal
   value quadrature that removes the singularity by subtraction rather than
   avoiding it.
4. **Recognise** the log-amplitude/phase (minimum-phase) relation, apply it, and
   explain why its integrals converge slowly.
5. **Demonstrate** that a frequency-dependent real response is non-causal, both
   by the Kramers–Kronig contradiction and by the time-domain support of its
   impulse response.
6. **Show** for the standard linear solid that the attenuation and the dispersion
   are fixed by the same two time constants, and quantify the dissipated energy
   per cycle directly from the stress–strain loop.
7. **State** the conditions under which a near-constant-$Q$ description is
   legitimate, and decline to quote a coefficient that requires assumptions this
   lesson does not verify.

## Prerequisites

[01-11-03 Contour Integration, Residues and Real
Integrals](./03-contour-integration.md) — principally the principal-value
technique of Section 4.4, which is the whole of the derivation below;
[01-11-04 The Laplace Transform and Transient
Problems](./04-laplace-transform.md) — analyticity in a half plane, poles and
causality in the time domain;
[02-03-07 Dispersion](../../02-physics/03-oscillations-and-waves/07-dispersion.md) —
phase and group velocity, and the physical meaning of a dispersive medium.

## 1. Intuition: causality has consequences for the frequency response

Causality is the simplest physical principle in the book: **nothing responds
before it is driven**. In the time domain, for a linear system with impulse
response $h(t)$,

$$h(t) = 0 \qquad \text{for } t < 0 .$$

In the laboratory this is nearly untestable — you cannot measure a response at a
time before the input — and it is almost never imposed deliberately in
modelling. Yet it is not a triviality, because it translates into a *global*
constraint on the frequency response. The constraint is the subject of this
lesson, and its content can be stated in one sentence:

> **You cannot choose the attenuation and the dispersion of a medium
> independently. Choosing one determines the other, up to a constant.**

That is a strong statement about physics, and it is why a model that specifies
attenuation as a function of frequency, with no statement about velocity
dispersion, is incomplete rather than merely simplified. It is also why real
seismic data cannot be corrected for attenuation by any scheme that ignores
dispersion, and why the phase of a causal filter is determined by its amplitude
spectrum (the "minimum-phase" property used whenever a wavelet is estimated from
its autocorrelation).

The mathematics is a one-line consequence of the material already developed:

1. Write the response function as a transform over the past only,
   $H(\omega) = \int_{0}^{\infty}h(t)e^{-i\omega t}\mathrm{d}t$.
2. Note that this integral converges in a whole half plane of complex $\omega$,
   so $H$ is analytic there.
3. Apply the contour argument of Cauchy's theorem, indenting around the point
   where the answer is wanted, and read off a principal-value integral.

Everything after that is the physics of the indent.

## 2. Causality becomes analyticity

### 2.1 The derivation

Work with the convention used throughout this module: a steady-state field
oscillates as $e^{-i\omega t}$, so a wave travelling in $+x$ is
$e^{i(kx-\omega t)}$. Let $h(t)$ be the impulse response of a linear,
time-invariant system, real and causal. Define

$$H(\omega) = \int_{-\infty}^{\infty}h(t)e^{-i\omega t}\,\mathrm{d}t
= \int_{0}^{\infty}h(t)e^{-i\omega t}\,\mathrm{d}t .$$

Put $\omega = \omega_{r} + i\omega_{i}$. Then
$|e^{-i\omega t}| = e^{\omega_{i}t}$, so for $\omega_{i} < 0$ the exponential is
*decaying* in $t$ and the integral converges for any $h$ that grows no faster
than a power. Therefore:

> **$H(\omega)$ is analytic in the lower half plane.** Equivalently, from
> $h$ real, $H(-\omega) = \overline{H(\omega)}$, so the real part of $H$ is even
> and the imaginary part odd.

The convention sign matters, and it is worth being blunt about it. With the
opposite convention ($e^{+i\omega t}$), the same argument puts the analyticity in
the *upper* half plane. Both statements are correct; mixing them produces sign
errors that are invisible in every amplitude and catastrophic in every phase.
**Write the convention down before deriving anything.** The demo verifies the
even/odd structure exactly:

| $\omega$ | $H(-\omega)$ | $\overline{H(\omega)}$ | difference |
|---|---|---|---|
| 0.3 | $+0.917431193+0.275229358i$ | $+0.917431193+0.275229358i$ | $0$ |
| 1.7 | $+0.257069409+0.437017995i$ | $+0.257069409+0.437017995i$ | $0$ |
| 6.0 | $+0.027027027+0.162162162i$ | $+0.027027027+0.162162162i$ | $0$ |

with the reference response

$$h(t) = \frac{1}{\tau}e^{-t/\tau}\Theta(t), \qquad \tau = 1,
\qquad H(\omega) = \frac{1}{1+i\omega\tau},$$

whose only singularity is the pole at $\omega = i/\tau = +i$ — in the *upper*
half plane, exactly where the derivation needs it to be absent.

### 2.2 Causality, measured in the time domain

Analyticity is a statement about a half plane, and the demo makes the
corresponding statement about time by inverting the transform numerically,

$$h(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty}H(\omega)e^{i\omega t}\,\mathrm{d}\omega,$$

with the integral truncated at $|\omega| = 2000$ and Simpson-integrated on
$2\times10^{5}$ nodes:

| $t$ | numeric $h(t)$ | exact |
|---|---|---|
| $-2.00$ | $-0.000058128092$ | $0$ |
| $-1.00$ | $-0.000058334910$ | $0$ |
| $-0.50$ | $+0.000179405041$ | $0$ |
| $0.25$ | $0.779363902156$ | $0.778800783071$ |
| $1.00$ | $0.367937924161$ | $0.367879441171$ |
| $2.00$ | $0.135393356966$ | $0.135335283237$ |

For $t<0$ the quadrature returns zero to about $10^{-4}$, and the residual is
pure truncation: the integrand $e^{i\omega t}/(1+i\omega\tau)$ decays only as
$1/\omega$, so cutting the range at $\Omega$ leaves an oscillatory tail of order
$1/(2\pi\Omega) \approx 8\times10^{-5}$. For $t>0$ the same truncation accounts
for the $5\times10^{-4}$ discrepancy from the exponential. **The contrast that
matters is between $10^{-4}$ and $0.78$**: the response is large after the
impulse and nothing before it, and the $10^{-4}$ is the numerical method, not the
physics. The exact statement — zero for $t<0$ — follows at once from analyticity:
for $t<0$ the contour can be closed in the lower (singularity-free) half plane,
where the integrand is analytic, so the integral is zero by Cauchy's theorem.

## 3. The Kramers–Kronig relations

### 3.1 Derivation

Apply Cauchy's integral formula to $H(\omega')/(\omega'-\omega)$ on the contour
made of the real axis with a small semicircular indentation *below* the point
$\omega' = \omega$, closed by a large arc in the lower half plane. Since $H$ is
analytic inside, the closed integral is zero. The indentation contributes
$i\pi H(\omega)$ (a half-circuit traversed clockwise), and the large arc
contributes nothing when $H(\omega')\to0$ as $|\omega'|\to\infty$ there. Hence

$$\mathrm{P.V.}\int_{-\infty}^{\infty}\frac{H(\omega')}{\omega'-\omega}
\,\mathrm{d}\omega' = -i\pi H(\omega),$$

which, on separating real and imaginary parts, gives the **Kramers–Kronig
relations** in this convention:

$$\operatorname{Re}H(\omega) =
-\frac{1}{\pi}\,\mathrm{P.V.}\int_{-\infty}^{\infty}
\frac{\operatorname{Im}H(\omega')}{\omega'-\omega}\,\mathrm{d}\omega',$$

$$\operatorname{Im}H(\omega) =
+\frac{1}{\pi}\,\mathrm{P.V.}\int_{-\infty}^{\infty}
\frac{\operatorname{Re}H(\omega')}{\omega'-\omega}\,\mathrm{d}\omega'.$$

Because $\operatorname{Im}H$ is odd and $\operatorname{Re}H$ is even, each can be
folded onto $0 < \omega' < \infty$:

$$\operatorname{Re}H(\omega) = -\frac{2}{\pi}\,\mathrm{P.V.}
\int_{0}^{\infty}\frac{\omega'\operatorname{Im}H(\omega')}
{\omega'^{2}-\omega^{2}}\,\mathrm{d}\omega',$$

$$\operatorname{Im}H(\omega) = +\frac{2\omega}{\pi}\,\mathrm{P.V.}
\int_{0}^{\infty}\frac{\operatorname{Re}H(\omega')}
{\omega'^{2}-\omega^{2}}\,\mathrm{d}\omega'.$$

The folded form is the one used in practice, because physical attenuation is
quoted for positive frequencies.

### 3.2 Handling the principal value in practice

The integrand has a $1/(\omega'-\omega)$ singularity at the point where the answer
is wanted, and the principal value is what makes it finite. The clean way to
evaluate it is to **subtract the singularity** rather than to dodge it:

$$\mathrm{P.V.}\int_{0}^{\infty}\frac{g(\omega')}{\omega'^{2}-\omega^{2}}
\,\mathrm{d}\omega' = \int_{0}^{\infty}
\frac{g(\omega')-g(\omega)}{\omega'^{2}-\omega^{2}}\,\mathrm{d}\omega',$$

which holds precisely because
$\mathrm{P.V.}\int_{0}^{\infty}\mathrm{d}\omega'/(\omega'^{2}-\omega^{2}) = 0$
(the logarithm of the ratio of the two limits vanishes). The subtracted integrand
is finite at $\omega' = \omega$ and equals $g'(\omega)/(2\omega)$ there, so an
ordinary quadrature rule applies. Add the substitution $\omega' = \tan u$, which
maps the infinite range exactly onto $[0,\pi/2)$, and the integral converges
spectrally.

### 3.3 The verification

With that machinery the demo checks both directions of the Kramers–Kronig
relations against the closed form of the Debye response:

| $\omega$ | $\operatorname{Re}H$ exact | $-(2/\pi)$ P.V. | difference |
|---|---|---|---|
| 0.10 | $0.99009900990099$ | $0.99009900990105$ | $5.7\times10^{-14}$ |
| 0.30 | $0.91743119266055$ | $0.91743119265861$ | $1.9\times10^{-12}$ |
| 1.00 | $0.50000000000000$ | $0.50000000000000$ | $8.9\times10^{-16}$ |
| 2.50 | $0.13793103448276$ | $0.13793103448243$ | $3.3\times10^{-13}$ |
| 10.00 | $0.00990099009901$ | $0.00990099009900$ | $1.1\times10^{-14}$ |
| 100.00 | $0.00009999000100$ | $0.00009999000100$ | $1.9\times10^{-16}$ |

and the conjugate relation

| $\omega$ | $\operatorname{Im}H$ exact | $+(2\omega/\pi)$ P.V. | difference |
|---|---|---|---|
| 0.10 | $-0.09900990099010$ | $-0.09900990099010$ | $5.6\times10^{-15}$ |
| 0.30 | $-0.27522935779817$ | $-0.27522935779758$ | $5.8\times10^{-13}$ |
| 1.00 | $-0.50000000000000$ | $-0.50000000000000$ | $8.9\times10^{-16}$ |
| 2.50 | $-0.34482758620690$ | $-0.34482758620608$ | $8.2\times10^{-13}$ |
| 10.00 | $-0.09900990099010$ | $-0.09900990098999$ | $1.1\times10^{-13}$ |
| 100.00 | $-0.00999900009999$ | $-0.00999900009997$ | $2.0\times10^{-14}$ |

Worst differences of $1.9\times10^{-12}$ and $8.2\times10^{-13}$ on a response
whose real and imaginary parts are both of order one: the relations are exact to
twelve digits, and the residual is the quadrature.

### 3.4 The same theorem for a modulus

The relations above are stated for a transfer function that vanishes at high
frequency. A modulus $M(\omega)$ — the ratio of stress to strain, or of pressure
to density change — differs in two ways: the physically interesting quantity
tends to a non-zero *unrelaxed* modulus at high frequency, and it is a ratio of
two causal quantities rather than an impulse-response transform. Both differences
have consequences:

- The relation must be applied to the combination that **vanishes** at infinity,
  here $M(\omega)-M_{U}$ where $M_{U}$ is the unrelaxed modulus.
- The sign of the relation is **opposite** to the transfer-function case. The
  modulus is an upper-half-plane object under our convention; it is the
  reflection, $\omega \to -\omega$, of a causal transform, and reflection flips
  the sign of the closure.

The demo verifies this explicitly for the standard linear solid of Section 6:

| $\omega$ | $\operatorname{Re}(M-M_{U})$ | $+(2/\pi)$ P.V. | difference |
|---|---|---|---|
| 0.10 | $-0.999375390381$ | $-0.999375390381$ | $7.0\times10^{-15}$ |
| 0.50 | $-0.984615384615$ | $-0.984615384615$ | $5.4\times10^{-15}$ |
| 1.00 | $-0.941176470588$ | $-0.941176470588$ | $1.3\times10^{-15}$ |
| 4.00 | $-0.500000000000$ | $-0.500000000000$ | $8.7\times10^{-15}$ |
| 20.00 | $-0.038461538462$ | $-0.038461538462$ | $4.4\times10^{-16}$ |

worst difference $8.7\times10^{-15}$. **Do not copy a Kramers–Kronig formula out
of a paper without checking which of these two cases the author is in.** The
sign, the combination, and the reference modulus all change between them, and all
three are routinely left unstated.

## 4. The log-amplitude / phase relation, and its slow convergence

### 4.1 Minimum phase

For a response that has no zeros in the lower half plane — the condition for the
system to be **minimum phase** — the same argument applies to $\log H$, whose
real part is $\ln|H|$ and whose imaginary part is $\arg H$:

$$\arg H(\omega) = \frac{2\omega}{\pi}\,\mathrm{P.V.}
\int_{0}^{\infty}\frac{\ln|H(\omega')|}{\omega'^{2}-\omega^{2}}
\,\mathrm{d}\omega' .$$

The physical reading is the reason this relation is on every seismic processor's
desk: **the phase of a minimum-phase causal filter is completely determined by
its amplitude spectrum.** Estimate the amplitude spectrum of a wavelet — from
its autocorrelation, say — and the phase is not an independent unknown; it can be
computed. Conversely, a wavelet that has been given an arbitrary phase is not
minimum phase, and the amplitude/phase pair will not satisfy the relation.

### 4.2 Why the integral converges slowly

For $H(\omega) = 1/(1+i\omega\tau)$ we have
$\ln|H| = -\tfrac12\ln(1+\omega^{2}\tau^{2})$ and
$\arg H = -\arctan(\omega\tau)$. Both are known exactly, so the relation can be
checked without any model uncertainty:

| $\omega$ | nodes | $\arg H$ exact | $(2\omega/\pi)$ P.V. | difference |
|---|---|---|---|---|
| 0.30 | 100000 | $-0.291456794478$ | $-0.291480533967$ | $2.4\times10^{-5}$ |
| 0.30 | 1000000 | $-0.291456794478$ | $-0.291458938168$ | $2.1\times10^{-6}$ |
| 1.00 | 100000 | $-0.785398163397$ | $-0.785477295028$ | $7.9\times10^{-5}$ |
| 1.00 | 1000000 | $-0.785398163397$ | $-0.785405309032$ | $7.2\times10^{-6}$ |

Note the column that is missing compared with Section 3.3: the residual does not
fall as $10^{-12}$; it falls **roughly in proportion to the node spacing**, a
factor of ten for a factor of ten in $n$. The reason is not the quadrature. The
integrand in $u = \arctan\omega'$ contains
$\ln|H(\tan u)| \sim -\ln(\cot u) \to -\infty$ as
$u \to \pi/2$: a logarithmic endpoint singularity, which no amount of nodes
removes.

This is a property of dispersion relations for attenuation, not an artefact.
Attenuation grows with frequency, so the log-amplitude decays, but only
logarithmically, so the Kramers–Kronig integral that converts it into phase
converges differently from the one that converts the real part into the imaginary
part. Everything downstream inherits the behaviour: the dispersion integral of a
constant-$Q$ model is slowly convergent at the band edges, which is exactly why
those models are always specified with explicit low- and high-frequency cutoffs
rather than over an unbounded band.

## 5. A real, frequency-dependent response is non-causal

### 5.1 The construction

Take a response whose real part is $1/(1+\omega^{2}\tau^{2})$ — a perfectly
reasonable-looking low-pass amplitude — and set its imaginary part to zero. It is
real, even, bounded and tends to zero. Is it causal?

Two independent tests, both run by the demo.

**Test 1: the Kramers–Kronig contradiction.** The conjugate relation demands

$$\operatorname{Im}H(\omega) = \frac{2\omega}{\pi}\,\mathrm{P.V.}
\int_{0}^{\infty}\frac{\operatorname{Re}H(\omega')}
{\omega'^{2}-\omega^{2}}\,\mathrm{d}\omega',$$

and the quadrature gives

| $\omega$ | implied $\operatorname{Im}H$ | assumed | conflict |
|---|---|---|---|
| 0.10 | $-0.099009900990$ | $0$ | $9.9\times10^{-2}$ |
| 0.50 | $-0.400000000000$ | $0$ | $4.0\times10^{-1}$ |
| 1.00 | $-0.500000000000$ | $0$ | $5.0\times10^{-1}$ |
| 3.00 | $-0.300000000000$ | $0$ | $3.0\times10^{-1}$ |

The implied imaginary part is exactly $-\omega/(1+\omega^{2})$, the imaginary part
of the causal response $1/(1+i\omega)$ — that is, the *same* real part belongs to
a causal response only if the imaginary part is that specific function. Setting
it to zero is a contradiction, and the conflict is not small.

**Test 2: the time-domain support.** The inverse transform of the real-only
response is

$$\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{e^{i\omega t}}{1+\omega^{2}}
\,\mathrm{d}\omega = \frac{1}{2}e^{-|t|},$$

the two-sided exponential. The demo's numerical inversion reproduces it:

| $t$ | numeric $h(t)$ | $(1/2)e^{-\vert t\vert}$ |
|---|---|---|
| $-3.00$ | $0.024893522830$ | $0.024893534184$ |
| $-1.50$ | $0.111565091737$ | $0.111565080074$ |
| $-0.50$ | $0.303265461278$ | $0.303265329856$ |
| $0.00$ | $0.499840845070$ | $0.500000000000$ |
| $0.50$ | $0.303265461278$ | $0.303265329856$ |
| $1.50$ | $0.111565091737$ | $0.111565080074$ |
| $3.00$ | $0.024893522830$ | $0.024893534184$ |

At $t = -1.50$ the response is $0.112$ — it anticipates the impulse by an amount
that would be a spectacular experimental discovery if it were real. (The residual
of about $1.6\times10^{-4}$ at $t=0$ is again the oscillatory-tail truncation of
the quadrature.)

**The conclusion.** A frequency-*independent* real response — a constant modulus
— is both real and causal, and it describes a medium with no attenuation and no
dispersion. Every frequency-*dependent* real response is non-causal. In
particular:

> A model that specifies a frequency-dependent velocity or modulus and no
> attenuation is not a simplification of a physical medium; it is a description
> of an impossible one.

## 6. Attenuation implies dispersion: the standard linear solid

### 6.1 The model and its causal solution

The **standard linear solid** (Zener) relates stress $\sigma$ and strain
$\varepsilon$ by

$$\sigma + \tau_{\sigma}\dot\sigma = M_{R}\bigl(\varepsilon +
\tau_{\varepsilon}\dot\varepsilon\bigr), \qquad \tau_{\varepsilon} >
\tau_{\sigma} > 0 .$$

It is a differential equation, so it is causal by construction — no memory
integral over the future appears anywhere. Solving it with the integrating factor
$e^{t/\tau_{\sigma}}$ and an integration by parts gives

$$\sigma(t) = M_{U}\varepsilon(t) - C\int_{-\infty}^{t}
e^{-(t-s)/\tau_{\sigma}}\varepsilon(s)\,\mathrm{d}s,
\qquad C = \frac{M_{R}(\tau_{\varepsilon}-\tau_{\sigma})}{\tau_{\sigma}^{2}},
\qquad M_{U} = M_{R}\frac{\tau_{\varepsilon}}{\tau_{\sigma}} .$$

The memory kernel is an exponential, so the memory integral obeys
$\tau_{\sigma}\dot I + I = \tau_{\sigma}\varepsilon$ — a first-order ODE, which
is how the demo integrates it. For a sinusoid $\varepsilon = \cos\omega t$ the
complex modulus follows from the same equation in one line,

$$M(\omega) = M_{R}\frac{1-i\omega\tau_{\varepsilon}}
{1-i\omega\tau_{\sigma}},$$

with limits $M(0) = M_{R}$ (the relaxed modulus) and
$M(\infty) = M_{U}$ (the unrelaxed modulus).

### 6.2 The time-domain check

The demo integrates the ODE for the memory integral with a fourth-order
Runge–Kutta scheme and compares $\sigma(t)$ with
$\operatorname{Re}[M(\omega)e^{-i\omega t}]$. With
$M_{R} = 1$, $\tau_{\varepsilon} = 0.5$, $\tau_{\sigma} = 0.25$ (so
$M_{U} = 2$, $C = 4$):

| $\omega$ | $t$ | $\sigma$ from the ODE | $\operatorname{Re}[Me^{-i\omega t}]$ | difference |
|---|---|---|---|---|
| 0.50 | $-12.541$ | $1.013757872$ | $1.013757855$ | $1.7\times10^{-8}$ |
| 0.50 | $-6.258$ | $-1.013757872$ | $-1.013757855$ | $1.7\times10^{-8}$ |
| 2.00 | $-3.135$ | $1.194878838$ | $1.194878837$ | $6.0\times10^{-10}$ |
| 2.00 | $-1.565$ | $-1.194878838$ | $-1.194878837$ | $6.0\times10^{-10}$ |
| 8.00 | $-0.784$ | $1.794831464$ | $1.794831464$ | $1.6\times10^{-12}$ |
| 8.00 | $-0.391$ | $-1.794831464$ | $-1.794831464$ | $1.6\times10^{-12}$ |

The causal differential equation and the complex modulus are the same model.

### 6.3 Which sign of $\operatorname{Im}M$ is dissipation?

This is the question that convention confusion gets wrong, and it can be settled
by measurement rather than argument. The energy dissipated per unit volume per
cycle is the area of the stress–strain hysteresis loop,

$$W = \oint\sigma\,\mathrm{d}\varepsilon,$$

which must be positive for a passive material. The demo computes $W$ directly by
integrating the ODE solution over one cycle and accumulating
$\sigma\,\mathrm{d}\varepsilon$:

| $\omega$ | $W$ from the loop | $-\pi\varepsilon_{0}^{2}\operatorname{Im}M$ | $1/Q = \vert\operatorname{Im}M/\operatorname{Re}M\vert$ |
|---|---|---|---|
| 0.50 | $0.386656921$ | $0.386657557$ | $0.121212121$ |
| 2.00 | $1.256634994$ | $1.256637061$ | $0.333333333$ |
| 8.00 | $1.256634994$ | $1.256637061$ | $0.222222222$ |

Two conclusions. First, the loop area equals $-\pi\varepsilon_{0}^{2}
\operatorname{Im}M$ to $10^{-6}$ (the residual is the nested quadrature), which
is a derivation check rather than a coincidence: carrying $M = M' + iM''$ through
$\oint\sigma\,\mathrm{d}\varepsilon$ with
$\varepsilon = \varepsilon_{0}\cos\omega t$ gives
$-\pi\varepsilon_{0}^{2}M''$ directly. Second, since $W>0$ and
$\operatorname{Im}M$ is *negative* for this model, the dissipative sign in the
$e^{-i\omega t}$ convention is

$$\operatorname{Im}M < 0 \qquad (\text{attenuating}),$$

the opposite of what an argument by analogy with the $e^{+i\omega t}$ literature
would suggest. The demo confirms the value $\operatorname{Im}M = -0.123077$ at
$\omega = 0.5$ from the closed form. Getting this sign wrong turns attenuation
into *gain*, and the resulting modelling error grows exponentially with distance.

### 6.4 Attenuation and dispersion, quantified together

With $\rho = 1$ define $k = \omega\sqrt{\rho/M(\omega)}$, so
$v = \omega/\operatorname{Re}k$ and $\alpha = \operatorname{Im}k$. The demo
reports:

| $\omega$ | $v$ | $\alpha$ | $1/Q$ exact | $\omega(\tau_{\varepsilon}-\tau_{\sigma})/(1+\omega^{2}\tau_{\varepsilon}\tau_{\sigma})$ |
|---|---|---|---|---|
| 0.050 | 1.000136668 | 0.000312347 | 0.012496095 | 0.012496095 |
| 0.100 | 1.000546068 | 0.001247564 | 0.024968789 | 0.024968789 |
| 0.500 | 1.013186152 | 0.029799593 | 0.121212121 | 0.121212121 |
| 1.000 | 1.047722428 | 0.104772243 | 0.222222222 | 0.222222222 |
| 2.828 | 1.206553287 | 0.402143934 | 0.353553387 | 0.353553387 |
| 8.000 | 1.366062915 | 0.642853136 | 0.222222222 | 0.222222222 |
| 40.000 | 1.412016957 | 0.704247859 | 0.049751244 | 0.049751244 |

and the exact loss formula
$1/Q = \omega(\tau_{\varepsilon}-\tau_{\sigma})/
(1+\omega^{2}\tau_{\varepsilon}\tau_{\sigma})$ is confirmed in the last two
columns to all printed digits. The peak of $1/Q$ is at
$\omega = 1/\sqrt{\tau_{\varepsilon}\tau_{\sigma}} = 2.828427125$ and equals

$$\frac{1}{Q_{\max}} = \frac{M_{U}-M_{R}}{2\sqrt{M_{R}M_{U}}} = 0.353553391,$$

matched by the measured $0.353553387$.

**The velocity rises monotonically with frequency**, from
$v = \sqrt{M_{R}/\rho} = 1.000000$ at low frequency to
$v = \sqrt{M_{U}/\rho} = 1.414213562$ at high frequency, and the total
dispersion is exactly $\sqrt{M_{U}/M_{R}} = 1.414213562$. That is the whole
content of the statement that attenuation and dispersion are not independent:
one pair of time constants, $\tau_{\varepsilon}$ and $\tau_{\sigma}$, fixes both
$\alpha(\omega)$ and $v(\omega)$, and the Kramers–Kronig relation of
Section 3.4 is the bookkeeping that connects them. A medium that attenuates
without dispersing does not exist.

### 6.5 What this model does *not* say, and the constant-$Q$ question

The standard linear solid has a **single** relaxation time, so $1/Q$ rises, peaks
and falls; it is not a constant-$Q$ medium. Seismological practice uses
near-constant $Q$ over a finite band, which requires a **broad spectrum** of
relaxation times — the Kolsky–Futterman and power-law models are constructions of
that kind. For a band over which $1/Q$ is approximately constant, the widely
quoted approximate dispersion law is

$$v(\omega) \approx v(\omega_{0})\left[1 -
\frac{1}{\pi Q}\ln\frac{\omega}{\omega_{0}}\right],$$

referenced to a specific $\omega_{0}$.

Two cautions, both of which this lesson declines to resolve by assertion:

1. The coefficient depends on the definition of $Q$, on whether phase or group
   velocity is meant, and on whether the reference frequency is the band centre
   or an endpoint. Published forms differ by factors of order two, and the
   difference is invisible in a plot of $v(\omega)$ over a limited band.
2. The logarithm is a consequence of the slow convergence of Section 4.2, so the
   law is a *band-limited* statement: applied over an unbounded band it diverges,
   which is the same statement as "strictly constant $Q$ at all frequencies is
   not causal".

What this lesson *does* establish, with numbers, is the mechanism: one relaxation
gives $1/Q_{\max} = 0.353553$ at
$\omega = 2.828427$ and a total velocity dispersion of $\sqrt2$, and the
Kramers–Kronig relation for the modulus holds to $8.7\times10^{-15}$. Whether a
particular published coefficient applies to a particular dataset is a
model-selection question, not a fact to be quoted.

## Assumptions and regime of validity

| assumption | statement | where it fails |
|---|---|---|
| **Linearity** | the response is a convolution with an impulse response | nonlinear soil, saturation, large-amplitude wave propagation |
| **Time invariance** | one $h(t)$ describes the system for the whole record | a medium that changes while the wave crosses it |
| **Causality** | $h(t) = 0$ for $t<0$ | any model with a frequency-dependent real response and no imaginary part |
| **Real response** | $H(-\omega) = \overline{H(\omega)}$, so $\operatorname{Re}H$ is even and $\operatorname{Im}H$ odd | complex-valued observables; a two-component field where the two components are not in quadrature |
| **Decay in the closing half plane** | $H\to0$ uniformly as $\vert\omega\vert\to\infty$ there, and in the time domain the impulse response is one-sided | $e^{-a\omega^{2}}$, which is analytic but does not decay (Section ★★2(c) of the exercises) |
| **Minimum phase** for the log-amplitude/phase relation | no zeros in the lower half plane | a non-minimum-phase sensor; a record shifted by an unknown whole number of samples |
| **A stated reference** for any subtracted relation | the relation holds for the combination that vanishes at infinity, e.g. $M-M_{U}$ | applying the unsubtracted relation to $M$ itself |

**Regime of validity, stated in physical terms.**

- **The relation is exact; its content is a constraint, not a formula for a
  number.** It says that the pair (attenuation, dispersion) is a one-parameter
  family up to a constant. It does not say how big the dispersion is: that
  depends on how the loss is distributed in frequency, which is a question about
  relaxation mechanisms, not about causality.
- **Everything is band-limited in practice.** Both relations integrate over all
  frequencies, and the data do not. The unmeasured tails contribute, and a test
  that ignores them can fail (or pass) for reasons that have nothing to do with
  causality. A tail model is therefore part of any dispersion-relation test, and
  its influence must be reported.
- **Single relaxation is not constant $Q$.** The standard linear solid has one
  loss peak; a $Q$ that is nearly constant across a decade requires a broad
  spectrum of relaxation times. The relation holds in both cases; the resulting
  dispersion does not have the same shape, and the logarithmic law of
  Section 6.5 belongs to the constant-$Q$ case.
- **Conventions are part of the physics statement.** The signs of
  $\operatorname{Im}M$, of the relation, and of the impedance phase all follow
  from $e^{-i\omega t}$ versus $e^{+i\omega t}$. A medium's attenuation is a fact;
  the sign of an imaginary part is a convention, and the two are frequently
  confused in print.

## 7. Python demonstration

[`code/dispersion_causality_demo.py`](./code/dispersion_causality_demo.py) prints
every table above in about six seconds:

```text
python3 code/dispersion_causality_demo.py
```

It uses only `cmath` and `math`. The method is as important as the results, and
four choices deserve stating:

**One convention, declared once, and tested.** The file's docstring fixes
$e^{-i\omega t}$ and states the resulting half plane. The conjugate symmetry is
then *measured* (differences of exactly $0$), so a convention error would show up
as a failed test rather than as a plausible wrong sign.

**Principal values by subtraction, not by avoidance.** The subtracted integrand
is finite at the singular point, and the identity that justifies the subtraction
is stated. Combined with $\omega' = \tan u$, this is what takes the
Kramers–Kronig residuals to $10^{-12}$ while the *same* machinery leaves
$10^{-5}$ on the log-amplitude relation — the contrast is the physics of
Section 4.2, and it would have been hidden if a coarser method had been used for
both.

**Physical signs are measured, not assumed.** $\operatorname{Im}M<0$ is
established by computing the hysteresis loop area and requiring it positive. A
sign convention that is only asserted cannot be checked, and this one is the
easiest in the subject to get backwards.

**Every claim has a second route.** Causality is checked in the time domain and
by analyticity; the modulus is checked against a time-domain ODE integration;
the dissipated energy is checked against $-\pi\varepsilon_{0}^{2}
\operatorname{Im}M$; the dispersion is checked against $\sqrt{M_{U}/M_{R}}$.
Where only one route is available — the literature's constant-$Q$ coefficient,
for instance — this lesson says so and does not quote a number.

## 8. Common mistakes

1. **Mixing the sign convention.** Every sign in this lesson, including the sign
   of $\operatorname{Im}M$ for an attenuating medium, follows from $e^{-i\omega t}$
   versus $e^{+i\omega t}$. Decide once, write it down, test it.
2. **Applying the transfer-function form to a modulus.** Section 3.4: the
   modulus needs the vanishing combination and carries the opposite sign.
3. **Assuming $\operatorname{Re}$ and $\operatorname{Im}$ relations are
   interchangeable.** They are, given conjugate symmetry — and conjugate symmetry
   is a consequence of the response being real, which fails for a complex-valued
   observable.
4. **Ignoring the logarithmic convergence of the phase relation.** Section 4.2:
   a dispersion integral of attenuation converges slowly at the band edges, which
   is why constant-$Q$ models need explicit cutoffs.
5. **Believing a frequency-dependent real modulus is causal.** Section 5: the
   contradiction is quantitative, and the impulse response has support at
   negative time.
6. **Forgetting the reference modulus in a subtracted relation.** The relation
   applies to $M-M_{U}$ (or $M-M_{R}$ plus a constant term), not to $M$ itself.
7. **Correcting for attenuation without dispersion.** Since the two are linked,
   a processing step that removes attenuation and leaves the velocity
   dispersion in place introduces a frequency-dependent travel-time error — the
   classic reason migrated sections have a stretch at the top of the band.
8. **Quoting a constant-$Q$ dispersion coefficient without its definitions.**
   Section 6.5.

## 9. Real-world applications

- **Seismic attenuation.** $Q$ is measured from spectral ratios, from
  amplitude decay with offset and from the rise time of a wavelet; every one of
  those measurements has a dispersion counterpart that must be handled
  consistently in modelling and in migration
  ([06-seismology](../../06-seismology/README.md),
  [02-03-07
  Dispersion](../../02-physics/03-oscillations-and-waves/07-dispersion.md)).
- **Minimum-phase wavelets.** The log-amplitude/phase relation is why a wavelet
  can be estimated from the autocorrelation of a trace for deconvolution, and why
  a wavelet that violates minimum phase is detectable
  ([20-signal-processing](../../20-signal-processing/README.md)).
- **Electromagnetic diffusion.** The response of a conducting earth is causal and
  dissipative, so the in-phase and quadrature components of a magnetotelluric
  impedance are Kramers–Kronig pairs — the basis of the consistency tests the
  method applies to its own data
  ([09-electrical-em-methods](../../09-electrical-em-methods/README.md)).
- **Dielectric and GPR properties.** The permittivity of a wet soil has a real
  and an imaginary part linked by a dispersion relation; GPR velocity and
  attenuation are one measurement, not two
  ([10-gpr-near-surface](../../10-gpr-near-surface/README.md)).
- **Viscoelastic and poroelastic modelling.** Constitutive models must be causal
  by construction; the standard linear solid of Section 6 is the simplest such
  model, and the same structure appears in poroelasticity
  ([02-04 Elasticity and Continuum
  Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)).
- **Optical and laboratory measurements.** The same relations connect the
  refractive index to absorption in any spectroscopic measurement, which is the
  origin of the method and the reason it is stated with the optical sign
  convention.

## 10. Further reading

- **Landau, L. D., Lifshitz, E. M. & Pitaevskii, L. P. (1984). *Electrodynamics
  of Continuous Media* (2nd ed.). Pergamon.** §§77–82. Level: graduate. The
  derivation of Kramers–Kronig from analyticity, with the sign conventions laid
  out explicitly.
- **Jackson, J. D. (1998). *Classical Electrodynamics* (3rd ed.). Wiley.**
  §7.10. Level: graduate. The same relations derived as a consequence of
  causality and used for the refractive index.
- **Aki, K. & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** §5.5. Level: graduate. The standard treatment of
  attenuation and dispersion in seismology, including the linear-attenuation
  model and its dispersion.
- **Futterman, W. I. (1962). Dispersive body waves. *Journal of Geophysical
  Research*, 67(13), 5279–5291.** Level: graduate. The paper that made
  attenuation–dispersion coupling standard in exploration seismology; its
  dispersion law follows from causality and requires explicit cutoffs.
- **Toll, J. S. (1956). Causality and the dispersion relation: logical
  foundations. *Physical Review*, 104(6), 1760–1770.** Level: graduate. The
  precise statement of what causality does and does not imply, written to correct
  its own literature.
- **Mavko, G., Mukerji, T. & Dvorkin, J. (2009). *The Rock Physics Handbook*
  (2nd ed.). Cambridge University Press.** Chapter 6. Level: intermediate. The
  laboratory and rock-physics side: measured $Q$, velocity dispersion, and how
  they are reported.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library before citing them.

## 11. Related lessons

- [03 Contour Integration, Residues and Real
  Integrals](./03-contour-integration.md) — the principal-value machinery; its
  Section 4.4 is the prototype of the derivation here.
- [04 The Laplace Transform and Transient
  Problems](./04-laplace-transform.md) — analyticity in a half plane, and the
  causality of a transform pair.
- [05 The z-Transform and Discrete Linear
  Systems](./05-z-transform.md) — the sampled version, where minimum phase is a
  statement about zeros inside the unit circle.
- [02-03-07
  Dispersion](../../02-physics/03-oscillations-and-waves/07-dispersion.md) — what
  phase and group velocity mean before they are constrained.
- [02-03-10
  Attenuation](../../02-physics/03-oscillations-and-waves/10-attenuation.md) —
  the physical mechanisms of attenuation and their models.
- [01-10-06 Hilbert Transform and the Analytic
  Signal](../10-fourier-analysis/06-hilbert-transform.md) — the same
  Hilbert-transform pair applied to a trace rather than to a material property.

## 12. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/06-dispersion-relations-exercises.md`](./exercises/06-dispersion-relations-exercises.md).
Solutions:
[`exercises/06-dispersion-relations-solutions.md`](./exercises/06-dispersion-relations-solutions.md).

## Self-assessment checklist

- [ ] I can derive that a causal real response is analytic in one half plane,
      and state which half plane belongs to which convention.
- [ ] I can derive the Kramers–Kronig relations by indenting a contour, and give
      both the transfer-function and the modulus form with their signs.
- [ ] I can evaluate a principal value by subtracting the singularity and
      explain why the subtraction is legitimate.
- [ ] I can verify both Kramers–Kronig directions numerically to about
      $10^{-12}$.
- [ ] I can state and use the log-amplitude/phase relation, and explain why it
      converges more slowly than the conjugate relation.
- [ ] I can show that a frequency-dependent real response is non-causal, by two
      independent routes.
- [ ] I can compute the dissipated energy per cycle from a stress–strain loop and
      use its sign to fix the sign of $\operatorname{Im}M$.
- [ ] I can state, for the standard linear solid, the peak of $1/Q$ and the total
      velocity dispersion between the relaxed and unrelaxed limits.
- [ ] I can say what a near-constant-$Q$ description assumes and why it needs
      frequency cutoffs.
