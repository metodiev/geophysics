# Exercises — 01-03-05 Phase, Harmonics and Superposition of Oscillations

Attempt these **closed-book**. Solutions are in
[`05-phase-and-harmonics-solutions.md`](./05-phase-and-harmonics-solutions.md).
Difficulty: ★ foundational · ★★ applied · ★★★ research-oriented.

Phases are in radians unless stated; frequencies are in hertz. Where a convention
matters, state the one you used.

---

## ★ Foundational

**★1.** Convert each phase difference into a time shift.

(a) $1°$ at 1 Hz
(b) $45°$ at 0.1 Hz
(c) $180°$ at 20 Hz

State the formula you used and why the answer depends on frequency.

---

**★2.** Write $4\cos\omega t - 3\sin\omega t$ in the form $A\cos(\omega t - \varphi)$.
Give $A$ exactly and $\varphi$ in radians and degrees. Then state the time delay
it represents at 2 Hz.

---

**★3.** Two sinusoids of unit amplitude have frequencies 2.0 Hz and 2.2 Hz.

(a) Give the carrier frequency and the beat period.
(b) Give the first two times at which the envelope vanishes.
(c) State the maximum envelope value and explain why it cannot exceed it.

---

**★4.** The square wave of period 1 s discussed in the lesson has the series

$$f(t) = \frac{4}{\pi}\sum_{\substack{n \ge 1 \\ n\ \text{odd}}}
\frac{\sin(2\pi n t)}{n}.$$

(a) Write the first three non-zero terms explicitly.
(b) Evaluate the three-term partial sum at $t = 0.25$ s and compare with the ideal
value of 1.
(c) Evaluate it at $t = 0.5$ s and explain the result.
(d) State what happens to the error at $t = 0.5$ as more terms are added.

---

## ★★ Applied

**★★5.** A medium has the dispersion relation $\omega = 3k + 0.5k^{2}$ with
$\omega$ in rad/s and $k$ in rad/km.

(a) For $k = 2$ rad/km, compute $f$, the period $T$ and the wavelength $\lambda$.
(b) Compute the phase velocity $c = \omega/k$ and the group velocity
$c_g = d\omega/dk$ at $k = 2$.
(c) Which is larger, and what does that imply about how a pulse changes as it
travels?
(d) At $k = 6$ rad/km, recompute both. Comment on whether the dispersion is
stronger or weaker at higher wavenumber.

---

**★★6.** The M2 tidal constituent has period $12.4206012$ h and S2 has period
exactly $12$ h.

(a) Compute the two frequencies in cycles per hour.
(b) Compute the beat (spring–neap) period in hours and days.
(c) At a given location the two constituents are in phase at $t = 0$. Give the
times of the next two occasions on which they are again in phase.
(d) State one physical reason why a real tide gauge's neap-to-spring interval
differs from your answer.

---

**★★7.** Two stations record a Rayleigh wave whose period is 12 s, and their
phases differ by $60°$.

(a) Convert the phase difference to a time shift.
(b) If the phase velocity is 3.0 km/s, what is the separation of the stations?
(c) Repeat for a phase difference of $300°$. Explain why the answer is not
simply five times larger, and state the ambiguity that makes the 3 km/s assumption
unnecessary.
(d) A third station records the same wave with a phase difference of $420°$ from
the first. What do you report, and why?

---

**★★8.** A response is the sum of two contributions of equal amplitude $A$ with a
phase difference of $\pi$.

(a) Show algebraically that the sum is zero.
(b) Compute the sum if the phase difference is $179°$ instead, keeping $A = 1$.
Express the residual as a fraction of $A$. (Use the sum-to-product identity.)
(c) An analyst reports only amplitudes and ignores phases. What would they
report in (a) and in (b), and what would they miss?

---

## ★★★ Research-oriented

**★★★9.** The Gibbs phenomenon, measured.

Take the square wave of period 1 s and its odd-harmonic series.

(a) Implement the partial sum for $N$ retained harmonics.
(b) For $N \in \{1, 3, 5, 11, 51, 201\}$, compute the rms error over one full
period on a uniform grid of at least 2000 samples, the maximum absolute pointwise
error, and the maximum value of the partial sum (the overshoot peak).
(c) The overshoot peak sits within about $1/N$ of the discontinuity, so the grid
used to find it must refine as $N$ grows. Demonstrate that a fixed grid gives a
*decreasing* apparent overshoot, and explain why.
(d) Report the limiting overshoot as a percentage of the jump, and compare it with
the value your fixed grid would have suggested.
(e) Explain why the maximum pointwise error does not decrease with $N$, and what
that means for a band-limited representation of a sharp arrival.
(f) State the limits of your result: does the limiting overshoot depend on the
function, on the number of samples, or on the platform?

---

**★★★10.** Phase velocity and group velocity, measured rather than assumed.

Superpose two unit-amplitude waves with wavenumbers $k_0 \pm dk$ and angular
frequencies $\omega_0 \pm d\omega$.

(a) Show by the sum-to-product identity that the result factorises into a carrier
and an envelope, and identify the velocity of each.
(b) Implement the superposition for $k_0 = 2$, $\omega_0 = 6$, $dk = 0.1$,
$d\omega = 0.35$ (arbitrary but consistent units). Sample a spatial grid at fixed
$t$ and locate both the carrier peaks and the envelope peak.
(c) Track the envelope peak over a series of times and measure its speed
numerically. Compare with $d\omega/dk$.
(d) Track a carrier zero crossing and measure the phase velocity numerically.
Compare with $\omega_0/k_0$.
(e) Reduce $dk$ by a factor of ten and repeat. Do the measured velocities move?
Do the measured *uncertainties* shrink? Explain what this says about the two-wave
construction as a tool for measuring dispersion.
(f) State the approximation under which $c_g = d\omega/dk$ is the envelope speed,
and describe what happens when it fails.

---

## Extension ideas

- Take a teaching or open waveform dataset, and estimate a dispersion curve by
  cross-correlating two nearby stations in overlapping narrow bands. Report the
  phase as a function of period, and state every assumption you had to make about
  the source. Data access is described in
  [20-signal-processing](../../../20-signal-processing/README.md).
- Repeat ★★★9 for a sawtooth wave, whose Fourier coefficients fall as $1/n$
  rather than $1/n$ only for odd $n$. Compare the rms convergence rate and the
  overshoot, and explain the difference in terms of the series coefficients.
