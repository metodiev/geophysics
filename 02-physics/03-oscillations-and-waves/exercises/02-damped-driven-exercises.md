# Exercises — 02-03-02 Damped and Driven Oscillations, Resonance and Quality Factor

Attempt these **closed-book** before opening the
[solutions](./02-damped-driven-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Several problems refer to
[`../code/damped_driven_demo.py`](../code/damped_driven_demo.py). Run and modify
it rather than reasoning about what it would print.

---

## ★ Foundational

**★1.** A 0.50 kg mass on a spring of stiffness $50\ \mathrm{N\,m^{-1}}$ is
damped with $\beta = 1.5\ \mathrm{s^{-1}}$.

(a) Compute $\omega_0$, $\omega_d$, $T_d$ and $Q$.
(b) State which regime the system is in.
(c) Compute the ratio of successive peak amplitudes.
(d) How long until the amplitude has fallen to 1 per cent of its initial value?

---

**★2.** Show that the three definitions $Q = \omega_0/2\beta$, $Q = \pi/\delta$
and $Q = \omega_0/\Delta\omega$ are not identical by evaluating all three for
$\beta = 2\ \mathrm{s^{-1}}$ and $\omega_0 = 10\ \mathrm{rad\,s^{-1}}$.

---

**★3.** Verify dimensionally that $A_{\max}/A(0) = Q$ and state which limits
must be taken for the identity to hold.
$A(0) = F_0/(m\omega_0^2)$ and $A_{\max}$ is given by equation (11) of the
lesson.

---

**★4.** A driven oscillator has $\omega_0 = 20\ \mathrm{rad\,s^{-1}}$ and
$Q = 50$.

(a) Compute the damping coefficient $\beta$.
(b) Compute the resonance frequency for the displacement response.
(c) Compute the half-power bandwidth from the exact formula and from
$2\beta$, and report the percentage difference.
(d) Sketch, in words, how the phase lag varies from $\omega \ll \omega_0$ to
$\omega \gg \omega_0$.

---

## ★★ Applied

**★★5.** A geophone is specified with $\omega_0 = 2\pi\times10\
\mathrm{rad\,s^{-1}}$ and a damping ratio $\zeta = \beta/\omega_0 = 0.7$.

(a) Compute $Q$ and the half-power bandwidth.
(b) Compute the phase lag at 1, 10 and 100 Hz and state over which band the
instrument response is nearly flat in phase.
(c) Explain why $\zeta \approx 0.7$ (i.e. $Q \approx 0.71$) is a common design
choice, in terms of (i) the amplitude response and (ii) ringing after an
impulse.

---

**★★6.** A free-decay test on a geophone gives successive peak amplitudes
1.000, 0.870, 0.757, 0.659 (arbitrary units), with the peaks separated by
0.100 s.

(a) Compute the logarithmic decrement and $Q$ from the averaged ratio.
(b) Compute $\omega_d$ and hence $\beta$ and $\omega_0$.
(c) State which of the four definitions of $Q$ you used and what its
approximation error is at this $Q$.

---

**★★7.** Run the demo and, from its output,

(a) report the measured $Q = \pi/\delta$ and $Q = \omega_0/2\beta$ at
$\beta = 0.5$ and $\beta = 2.0$, and compare the ratios of the two with the
prediction $(\omega_0/\omega_d)$;
(b) report $A_{\max}/A(0)$ and compare with $Q$ and with the exact expression of
equation (11);
(c) explain why the numerical amplitude at $\omega = 10$ has a smaller relative
error ($5.6\times10^{-8}$) than the values at neighbouring frequencies
($\sim3\times10^{-5}$);
(d) identify which of the six columns of the bandwidth table is the best test of
the exact formula in equation (13).

---

**★★8.** The energy of a lightly damped oscillator decays as
$E(t) = E_0e^{-2\beta t}$.

(a) Show that the fractional energy loss per cycle is $2\pi/Q$ to first order in
$1/Q$.
(b) Show that the number of cycles for the energy to fall by a factor $e$ is
$Q/\pi$.
(c) A rock has $Q = 100$ at 10 Hz and a P speed of 5.6 km/s. Compute the
amplitude decay per wavelength and the distance over which the amplitude falls
by $e^{-1}$.
(d) Repeat for $Q = 20$ and comment on the difference in survey reach.

---

## ★★★ Research-oriented

**★★★9.** A driven oscillator is not started from the steady state; it is
released from rest at $t = 0$ with $x = 0$ while the force $F_0\cos\omega t$ is
applied.

(a) Show that the solution is
$x(t) = A(\omega)\left[\cos(\omega t - \delta) - \cos\delta\,e^{-\beta t}\cos\omega_d t\right]
+ \ldots$, i.e. that the transient and the steady state have comparable
amplitude when $\omega$ is far from $\omega_0$.
(b) Show that near resonance ($\omega \approx \omega_0$) the envelope builds up
over a time $\sim 1/\beta$, and that the number of cycles needed is about
$Q/\pi$.
(c) Verify the build-up time numerically, by measuring the time for the envelope
to reach 90 per cent of its steady value, for $Q = 5, 10, 25$ and comparing with
$2.3/(2\beta)$.
(d) State the practical consequence for a field measurement of resonance: why
must the source be run for several $Q$ cycles before the amplitude is
meaningful?

---

**★★★10.** Two attenuation mechanisms act on the same mode: a velocity-
proportional dashpot with coefficient $\beta_1$ and a constant-friction (Coulomb)
damper with amplitude-independent force $F_c$.

(a) Show that the dashpot alone gives amplitude decay proportional to $e^{-\beta
t}$ (exponential), while the Coulomb damper alone gives *linear* amplitude decay
in time, $A(t) = A_0 - 2F_c t/(\pi m\omega_0)$.
(b) Write a program that integrates both and reports, for four successive
peaks, the ratio of successive amplitudes. Report the ratios in a table.
(c) Show that the ratio of successive amplitudes is constant for the dashpot and
increases towards one for the Coulomb damper.
(d) State the diagnostic consequence: a measured decay that is not exponential
is evidence for a rate-independent loss mechanism, which is common in soil and
in fractured rock at moderate strain.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
