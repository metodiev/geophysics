# Exercises — 01-08-02 Second-Order Linear ODEs and Characteristic Equations

Attempt these **closed-book** before opening the
[solutions](./02-second-order-linear-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Companion lesson: [02 Second-Order Linear ODEs](../02-second-order-linear.md).

---

## ★ Foundational

**★1.** Solve each initial-value problem and state which damping case applies.

(a) $x'' + 5x' + 6x = 0$, $x(0) = 1$, $x'(0) = 0$
(b) $x'' + 4x' + 4x = 0$, $x(0) = 0$, $x'(0) = 1$
(c) $x'' + 2x' + 5x = 0$, $x(0) = 2$, $x'(0) = 0$

For (b), also find the time and value of the maximum displacement.

---

**★2.** For each equation give the roots of the characteristic equation, the
value of $\zeta$, and the damping case:

(a) $x'' + 3x' + 2x = 0$ (b) $x'' + 2x' + x = 0$ (c) $x'' + x' + x = 0$

---

**★3.** For $x'' + 0.4x' + x = 0$ compute $\omega_0$, $\zeta$, $\omega_d$, the
damped period $T_d$, the amplitude decay time, the logarithmic decrement
$\delta$, and $Q$. State the ratio $t_{1/2}/\tau$ for the *envelope*.

---

## ★★ Applied

**★★4.** A field record of a freely decaying oscillation shows successive peak
amplitudes in the ratio $1.30$, and the time between successive peaks is 2.5 s.

(a) Compute the logarithmic decrement and hence $\zeta$.
(b) Compute $\omega_d$, $\omega_0$, and the fractional difference between them.
(c) Compute $Q$ and the number of cycles required for the amplitude to fall to
$1/e$ of its initial value.

---

**★★5.** A moving-mass gravimeter has proof mass $m = 0.1$ kg and a natural
period of 2 s.

(a) Compute the spring stiffness $k$.
(b) Compute the damping coefficient $c$ needed for $\zeta = 0.7$, and the
free-decay time of the slowest mode.
(c) Repeat (b) for $\zeta = 3$ and comment on the practical consequence.
(d) State the damping ratio that minimises the free-decay time and compute that
minimum for this instrument.

---

**★★6.** A stably stratified ocean has buoyancy frequency $N = 0.015$ rad/s.

(a) Compute the period of a vertically displaced parcel, in minutes.
(b) Using $N^{2} = -(g/\rho)\,d\rho/dz$ with $\rho = 1025\ \mathrm{kg\,m^{-3}}$
and $g = 9.81\ \mathrm{m\,s^{-2}}$, compute $d\rho/dz$ and state its sign and
meaning.
(c) State two physical effects the equation neglects that would change the
observed period.

---

## ★★★ Research-oriented

**★★★7.** A free oscillation of the Earth has period 1500 s and quality factor
$Q = 250$.

(a) Compute the angular frequency and the amplitude decay time $2Q/\omega_0$, in
days.
(b) Compute the fraction of the amplitude and of the energy remaining after 10
complete oscillations.
(c) A second mode has the same period but $Q = 1000$. State the ratio of the
decay times and of the half-widths of the two spectral peaks, and explain why
both follow from the same identity.

---

**★★★8.** The solution of $x'' + 2\zeta\omega_0x' + \omega_0^2x = 0$ is a
continuous function of $\zeta$, even though the algebraic form changes at
$\zeta = 1$.

(a) With $\omega_0 = 1$, $x(0) = 1$, $x'(0) = 0$, compute $x(1)$ for
$\zeta = 1-\epsilon$ and $\zeta = 1+\epsilon$ with $\epsilon = 10^{-2}$,
$10^{-3}$ and $10^{-4}$, and tabulate the difference $\Delta(\epsilon)$.
(b) Determine the power law $\Delta \propto \epsilon^{p}$ from your table.
(c) Explain in one sentence why the *parameterisation* through
$\sqrt{1-\zeta^{2}}$ suggests a half-power behaviour while the function itself
is smooth, and what a numerical code must do about it.

---

## Extension ideas

- Derive the logarithmic decrement $\delta = 2\pi\zeta/\sqrt{1-\zeta^{2}}$
  directly from $x(t)$ evaluated at successive maxima, rather than from the
  envelope ratio.
- Show that the energy of the underdamped oscillator,
  $E = \tfrac12m x'^{2} + \tfrac12kx^{2}$, decays as $e^{-2\zeta\omega_0t}$ on
  average, and deduce $Q = 1/(2\zeta)$ from the definition
  $Q = 2\pi E/(\text{energy lost per cycle})$.
- Solve $x'' + \omega_0^{2}x = 0$ with $x(0) = 0$, $x'(0) = v_0$ and compare the
  amplitude $v_0/\omega_0$ with the *static* displacement produced by the same
  force. What does the ratio tell you about a seismometer's sensitivity?
