# Exercises — 02-03-01 Simple Harmonic Motion and Small-Oscillation Approximation

Attempt these **closed-book** before opening the
[solutions](./01-simple-harmonic-motion-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Several problems ask you to modify and run
[`../code/shm_demo.py`](../code/shm_demo.py). Do that literally: the point is to
compare a prediction with what the machine returns.

Throughout, $g = 9.80665\ \mathrm{m\,s^{-2}}$.

---

## ★ Foundational

**★1.** A 0.25 kg mass hangs from a spring of stiffness $32\ \mathrm{N\,m^{-1}}$.

(a) Write the equation of motion and identify $\omega_0$.
(b) Compute $T$ and $f$.
(c) The mass is pulled 4.0 cm down and released from rest. Write $x(t)$
explicitly.
(d) State the maximum speed and the maximum acceleration.

---

**★2.** A simple pendulum has $L = 0.80$ m.

(a) Compute $T_0$ for infinitesimal amplitude.
(b) Compute the exact period at $\theta_0 = 0.30$ rad.
(c) Compute the period at $\theta_0 = 0.30$ rad from the two-term series and
state the relative error of the series.
(d) At what amplitude does the small-angle period err by 1 per cent?

---

**★3.** For each potential, find the stable equilibrium points and the small-
oscillation frequency of a unit mass:

(a) $V(x) = \tfrac12\alpha x^2 - \tfrac13\beta x^3$ with $\alpha, \beta > 0$;
(b) $V(x) = -\cos x$;
(c) $V(x) = x^4$.

State for each whether the equilibrium is stable and what $V''$ is there.

---

**★4.** Dimensional check. A student proposes that the period of a mass on a
spring is $T = 2\pi\sqrt{m/k}$ and, separately, that the period of a
liquid sloshing in a tank of width $W$ is $T = 2\pi\sqrt{W/g}$.

(a) Verify both are dimensionally consistent.
(b) Verify one of them is dimensionally inconsistent if written as
$T = 2\pi\sqrt{g/W}$ and explain the failure.
(c) Explain in one sentence why both have the form
$\sqrt{\text{inertia}/\text{restoring coefficient}}$.

---

## ★★ Applied

**★★5.** A geophone has a natural angular frequency $\omega_0 = 2\pi\times
4.5\ \mathrm{rad\,s^{-1}}$.

(a) Compute its period.
(b) Above what frequency is the mass effectively stationary in space (a
seismometer) rather than following the ground (an accelerometer)? Argue from
the driven-oscillator solution of lesson 02-03-02 that the transition is near
$\omega_0$.
(c) The instrument is specified to be linear over a ground displacement of
$1\ \mu\mathrm{m}$. Estimate the peak acceleration it can record at that
displacement at 10 Hz and at 1 Hz, and comment on which end of its band is
limited by its own linearity.

---

**★★6.** The potential of a diatomic molecule is often modelled as
$V(r) = D\left(1 - e^{-a(r-r_0)}\right)^2$.

(a) Expand to second order about $r_0$ and show that the small-oscillation
frequency is $\sqrt{2Da^2/m}$.
(b) Sketch how the asymmetric higher-order terms make the *average* separation
increase with temperature. One sentence is enough; the physics is that the
turning points are not symmetric about $r_0$.
(c) Rocking of a soil column can be modelled with $V(x) = \tfrac12 k x^2 -
\tfrac14 b x^4$ with $b > 0$. Show that the frequency decreases with amplitude
and find the leading correction. *Hint:* treat $-\tfrac14bx^4$ as a
perturbation and average it over a cycle.

---

**★★7.** Run `shm_demo.py` and, using its output,

(a) report the measured relative error of RK4 at $dt = 10^{-2}$ and
$10^{-3}$ s and the ratio of the two;
(b) state the order of accuracy this implies and compare with the expected
value;
(c) explain why the ratio cannot be improved indefinitely by reducing $dt$;
(d) report the measured energy drift at $dt = 10^{-3}$ s over 50 s and state
whether it is consistent with your answer to (b).

---

**★★8.** The period of a pendulum is measured to four significant figures at
$T = 2.0064$ s, and the length is $L = 1.000$ m.

(a) What amplitude is consistent with that period, given equation (9)?
(b) Given a length uncertainty of 1 mm, what is the uncertainty in the inferred
$g$, and does it swamp the amplitude correction?
(c) State whether the experiment can measure the $\theta_0^2/16$ term at that
precision, and what change would make it measurable.

---

## ★★★ Research-oriented

**★★★9.** Write a program that measures the relative error of the small-angle
period as a function of amplitude, for $\theta_0 \in \{10^{-3}, 10^{-2},
10^{-1}, 0.5, 1.0, 2.0, 2.5\}$ rad, by comparing the elliptic-integral period
with the series truncated after 0, 1 and 2 terms.

(a) Report the errors in a table.
(b) Identify the amplitude at which the two-term series ($\theta_0^4$ included)
becomes the better approximation, and explain why a truncation should improve
matters there.
(c) Estimate the convergence radius of the series from the amplitudes at which
successive terms stop decreasing, and compare with the known result that the
expansion converges for $\theta_0 < \pi$.
(d) State the limitations of your conclusion.

---

**★★★10.** The Taylor expansion of a potential about an equilibrium is
controlled by the dimensionless ratio $V''' x / V''$, evaluated at the amplitude
$x$.

(a) Show that the frequency shift from a cubic term is second order in the
amplitude and proportional to $(V'''/V'')^2$.
(b) Apply the result to $V = \tfrac12 kx^2 + \tfrac13 g_3x^3$ with $k = 25\
\mathrm{N\,m^{-1}}$, $g_3 = 15\ \mathrm{N\,m^{-2}}$ and $m = 4$ kg, and predict
the fractional period change at amplitudes 0.001, 0.01, 0.05 and 0.1 m.
(c) Compare with the measured values in the demo output and report the
agreement.
(d) State the amplitude at which the expansion fails to describe the motion,
and what physically happens there (the well develops a second minimum and the
motion can escape it).

Report measured values only if you verify them numerically; state clearly which
of your results are analytic.
