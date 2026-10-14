# Exercises — 01-08-03 Damped and Driven Oscillators as Physical Models

Attempt these **closed-book** before opening the
[solutions](./03-oscillators-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Companion lesson: [03 Damped and Driven Oscillators](../03-oscillators.md).

---

## ★ Foundational

**★1.** For an oscillator with $\omega_0 = 10$ rad/s, $\zeta = 0.05$ and
$F_0/m = 1$, compute the steady-state amplitude and the phase lag at
$\omega = 0,\ 5,\ 10,\ 12,\ 20$ rad/s. Present the results as a table and
identify the row where the response is exactly $Q$ in these units.

---

**★2.** A resonator has a peak at $f_0 = 20$ Hz and the amplitude falls to
$1/\sqrt2$ of its peak at $f_0 \pm 0.5$ Hz.

(a) Compute $Q$ and $\zeta$.
(b) Compute the decay time of the free response and the build-up time of the
driven response, and state why they are equal.
(c) State the number of forced cycles needed for the response to reach steady
state.

---

**★3.** An oscillator has $\omega_0 = 2\pi\times5$ rad/s and $\zeta = 0.3$.

(a) Compute the frequency of the driven-response peak exactly, its ratio to
$\omega_0$, and the response at $\omega_0$ as a fraction of the peak.
(b) State whether a peak exists at all for $\zeta = 0.75$ and justify your
answer from the criterion, not from the formula's output.

---

## ★★ Applied

**★★4.** An undamped oscillator is driven from rest at its own frequency:
$x'' + x = \sin t$, $x(0) = x'(0) = 0$.

(a) Show that $x(t) = (\sin t - t\cos t)/2$ by substituting it into the ODE and
the initial conditions.
(b) State the envelope of $x$ for large $t$ and compute the value of $x$ at
$t = 50$.
(c) Explain in one sentence why the amplitude grows without bound and what
physical mechanism bounds it in reality.

---

**★★5.** A broadband seismometer has $T_0 = 30$ s and $\zeta = 0.7$. Its
normalised velocity response is
$\lvert H(\omega)\rvert = \omega^{2}/\lvert\omega_0^{2}-\omega^{2}
+2i\zeta\omega_0\omega\rvert$.

(a) Compute $\lvert H\rvert$ at 1 Hz, 0.1 Hz and 0.01 Hz.
(b) Find the frequency above which $\lvert H\rvert \ge 0.99$, to three
significant figures.
(c) A colleague claims that because $\lvert H\rvert = 1.000$ at 1 Hz the sensor
is "flat" and no correction is needed. Critique the claim using your numbers.

---

**★★6.** A 4.5 Hz geophone has $\zeta = 0.7$.

(a) Compute $\lvert H\rvert$ at 0.5, 1, 2, 4.5, 10 and 20 Hz.
(b) Compute the ratio of the response at 1 Hz to that at 4.5 Hz, and interpret
it as a percentage gain error a user would make by ignoring the response.
(c) Explain why the *relative* error is large at low frequency but the
*absolute* signal is also small, and state which of the two matters for a
velocity measurement.

---

## ★★★ Research-oriented

**★★★7.** A long-period signal at 20 mHz is recorded on a sensor whose
normalised response at that frequency happens to be 1.08 (an 8 % amplification
because the signal sits near the sensor's resonance). The recorded amplitude is
2.16 mm.

(a) Compute the corrected amplitude.
(b) The correction is applied in the frequency domain by dividing by a measured
transfer function. State the frequency range where this procedure is
ill-conditioned and explain why, using the shape of $\lvert H\rvert$ from
★5/★6.
(c) A second analyst applies the correction in the time domain by convolving
with an inverse filter built from the same transfer function. State one
advantage and one disadvantage of that approach compared with the frequency
domain.

---

**★★★8.** You are given amplitude and phase for two unknown one-dimensional
geophysical systems, measured over the same frequency band. Both numbers are
given relative to the response at the lowest frequency of the band (system A) or
as absolute magnitudes (system B).

**System A**

| $\omega$ (rad/s) | 0.5 | 1.0 | 2.0 | 10.0 |
|---|---|---|---|---|
| $\lvert H\rvert$ | 0.4472 | 0.7071 | 0.8944 | 0.9950 |
| phase lag | 63.43° | 45.00° | 26.57° | 5.71° |

**System B**

| $\omega$ (rad/s) | 0.5 | 1.0 | 2.0 | 4.0 | 10.0 |
|---|---|---|---|---|---|
| $\lvert H\rvert$ | 1.0607 | 1.2883 | 2.5000 | 0.3221 | 0.0415 |
| phase lag | 6.09° | 14.93° | 90.00° | 165.07° | 175.24° |

(a) Classify each system as resonant or diffusive, and state the two features of
the data you used.
(b) For each system, estimate the characteristic frequency (corner or
resonance) and the parameter ($\tau$, $\zeta$, $Q$) that follows from it.
(c) For system B, state the high-frequency power law of the amplitude and check
it against the tabulated values at $\omega = 4$ and $\omega = 10$.
(d) Explain why the phase at the characteristic frequency is a more robust
signature of the response class than the amplitude is.

---

## Extension ideas

- Derive the half-power bandwidth relation $\Delta\omega/\omega_0 = 2\zeta$
  directly from $A(\omega)^{2} = \tfrac12A_{\max}^{2}$, working to first order in
  $\zeta$, and identify the step where the first-order truncation enters.
- Show that at resonance the average power dissipated by damping equals the
  average power delivered by the forcing, by evaluating both explicitly for the
  steady-state solution.
- Show that the phase lag passes through $90°$ at $\omega = \omega_0$ for
  *every* $\zeta$ by setting the real part of
  $\omega_0^{2}-\omega^{2}+2i\zeta\omega_0\omega$ to zero, and explain why this
  makes $90°$ a robust frequency marker in the presence of unknown damping.
