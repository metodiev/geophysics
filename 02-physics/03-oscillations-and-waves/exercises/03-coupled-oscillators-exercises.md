# Exercises — 02-03-03 Coupled Oscillators and Normal Modes

Attempt these **closed-book** before opening the
[solutions](./03-coupled-oscillators-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to
[`../code/coupled_oscillators_demo.py`](../code/coupled_oscillators_demo.py)
require you to run it and report its actual numbers.

---

## ★ Foundational

**★1.** Two equal masses $m$ are joined by springs of stiffness $k$ to each
other and to fixed walls (three springs in all).

(a) Write the two equations of motion.
(b) Write the mass and stiffness matrices.
(c) Find the two eigenfrequencies and the two mode shapes by hand.
(d) Identify which mode is in-phase and which is antiphase, and explain why the
antiphase mode is faster.

---

**★2.** Using equation (8) of the lesson, compute $\omega_1$ and $\omega_N$ for
$N = 2, 5, 20$ with $k/m = 60\ \mathrm{s^{-2}}$.

(a) Report all six frequencies.
(b) Show numerically that $\omega_1$ is close to
$\sqrt{k/m}\,\pi/(N+1)$ for large $N$ and state the percentage error at
$N = 20$.
(c) State the limit of $\omega_N$ as $N\to\infty$.

---

**★3.** A system of three equal masses in a line is coupled to fixed walls with
springs $k$ throughout.

(a) Write down $\mathbf{K}/m$ with $k/m = 60\ \mathrm{s^{-2}}$ and
$\mathbf{M} = m\mathbf{I}$.
(b) Write the three mode shapes from
$u_j^{(n)} = \sin(jn\pi/(N+1))$.
(c) Verify by direct multiplication that each shape satisfies
$(\mathbf{K}/m)\mathbf{v} = \omega^2\mathbf{v}$ for the $\omega^2$ from
equation (8).

---

**★4.** Two identical oscillators of frequency $\omega_0$ are coupled with a weak
spring of stiffness $\epsilon k \ll 1$.

(a) Show that the two normal frequencies are approximately
$\omega_0\sqrt{1\pm\epsilon/2}$.
(b) Show that the beat period is approximately $2\pi/(\epsilon\omega_0/2)$ and
that it diverges as $\epsilon\to0$.
(c) Explain physically why weak coupling gives a long beat period.

---

## ★★ Applied

**★★5.** The demo reports, for $N = 2$, $k = 30$ N m⁻¹, $m = 0.5$ kg,

```text
  |omega2 - omega1| = 5.670441173 rad/s, beat period = 1.108059341 s
  mean spacing of envelope maxima = 1.1130 s
  largest |x2| measured = 0.009998 m (theory 0.010000 m)
```

(a) Verify the beat period from the two frequencies.
(b) Explain why the measured envelope spacing exceeds the predicted beat period
by 0.4 per cent, in terms of how the envelope is sampled.
(c) Show analytically that the peak of $|u_2|$ in equation (11) is
$A|\sin((\omega_1+\omega_2)t/2)|$, and hence that the largest value of $|u_2|$ over
all time is exactly $A$, approached but not reached at the envelope maxima.
(d) State what the measured 0.009998 m tells you about the accuracy of the
integration.

---

**★★6.** For $N = 5$ masses, the demo reports $\omega_3 = 10.954451150\
\mathrm{rad\,s^{-1}}$ and, for $N = 3$, $\omega_2 = 10.954451150\
\mathrm{rad\,s^{-1}}$ as well.

(a) Explain this coincidence using equation (8), where the argument is
$n\pi/(2(N+1))$.
(b) Find all $n$, $N$ pairs up to $N = 8$ for which a mode frequency equals
$2\sqrt{k/m}\sin(\pi/3)$ exactly.
(c) State the physical significance: which mode has the shape
$\sin(2j\pi/3)$ and what does that shape look like for $N = 5$?

---

**★★7.** A single mode is excited by setting the initial displacement
proportional to the mode shape.

(a) State what the demo measured for the deviation from
$\cos(\omega t)\times\text{mode}$ over 3 s, for the four modes with $N = 4$.
(b) Explain the systematic trend in those numbers with mode order.
(c) Predict how the deviations would change if the time step were halved, and
verify by modifying the script.
(d) Explain why this test is a stronger statement than merely checking that the
eigen-residual is small.

---

**★★8.** A two-storey building is modelled as two equal masses $m$ on two equal
columns of stiffness $k$.

(a) Write the coupled equations and find the two periods.
(b) Take $m = 2.0\times10^5$ kg and $k = 4.0\times10^7$ N m⁻¹ and compute both
periods in seconds.
(c) The ground moves at the frequency of the *second* mode. Describe
qualitatively the relative motion of the two floors, and explain why a taller
building is more vulnerable to the fundamental mode.

---

## ★★★ Research-oriented

**★★★9.** Consider the chain with *free* ends (no walls).

(a) Show that the boundary conditions become $u_0 = u_1$ and $u_N = u_{N+1}$
(mirror conditions) and find the $N$ mode shapes, one of which has
$\omega = 0$.
(b) Verify your analytic frequencies against a numerical diagonalisation of the
free-end stiffness matrix for $N = 4$ and report the differences.
(c) Show that the zero mode is a rigid translation and explain the general
statement that a freely floating elastic body has six zero modes in three
dimensions (three translations and three rotations).
(d) Explain why a finite-element model of a structure usually reports six
near-zero frequencies and why engineers discard them.

---

**★★★10.** Damping is added to the chain: each mass carries a dashpot
$2m\beta\dot u_j$ to ground, so that
$\mathbf{M}\ddot{\mathbf{u}} + 2\beta\mathbf{M}\dot{\mathbf{u}} +
\mathbf{K}\mathbf{u} = \mathbf{0}$.

(a) Show by projecting onto the undamped modes that the modal coordinates now
satisfy $\ddot q_n + 2\beta\dot q_n + \omega_n^2q_n = 0$ — that is, that *this*
form of damping does not couple the modes. Such damping is called proportional
or Rayleigh damping.
(b) Show that a general (non-proportional) damping matrix $\mathbf{C}$ *does*
couple the modes, and construct a $2\times2$ example in which it does.
(c) Simulate the $N = 4$ chain with proportional damping $\beta = 0.5\
\mathrm{s^{-1}}$ and measure $Q_n$ for each mode from its decay; report a table
of measured $Q_n$, predicted $Q_n = \omega_n/(2\beta)$ and the discrepancies.
(d) State the practical consequence for interpreting seismic attenuation: why is
proportional damping a *modelling choice* rather than a physical law?

Report measured values only if you verify them numerically, and state clearly
which of your results are analytic.
