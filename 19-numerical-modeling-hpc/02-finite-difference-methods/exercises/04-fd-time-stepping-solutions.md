# Solutions — 19-02-04 Explicit vs Implicit Time Stepping and Stability Limits

> **Read after attempting the exercises.** Demonstration values are quoted where
> they apply; arithmetic is shown.

Lesson: [04 Time Stepping](../04-fd-time-stepping.md).

---

## ★1 — FTCS

$$u_i^{n+1} = u_i^{n} + r\left(u_{i+1}^{n} - 2u_i^{n} + u_{i-1}^{n}\right),
\qquad r = \frac{\alpha\,dt}{h^{2}},$$

$G(\theta) = 1 - 4r\sin^{2}(\theta/2)$, stable for $0\le r\le1/2$. At $r = 1/2$
the highest mode ($\theta = \pi$) has $G = 1-4(0.5) = -1$: modulus one, i.e.
**exactly neutral** — the mode neither grows nor decays, which is stability at
the boundary rather than a good working value.

---

## ★2 — Orders in time

Forward Euler: first order. Backward Euler: first order. Crank–Nicolson: second
order. Measured in the demonstration against the exact semi-discrete solution:
$1.0000$, $0.9926$, $2.0001$.

---

## ★3 — Wave leapfrog

$$u_i^{n+1} = 2u_i^{n} - u_i^{n-1} + C^{2}\left(u_{i+1}^{n} - 2u_i^{n}
+ u_{i-1}^{n}\right), \qquad C = \frac{c\,dt}{h},$$

stable for $C\le1$. Beyond it the Nyquist-mode growth is
$\lvert G\rvert = \lvert 1-2C^{2}\rvert + \sqrt{(1-2C^{2})^{2}-1}$; the
demonstration measures exact agreement at $C = 1.02, 1.05, 1.10$.

---

## ★4 — A 2-D diffusion problem

$$dt_{\max} = \frac{h^{2}}{2\alpha d} = \frac{10^{4}}{2\times2\times10^{-7}
\times2} = \frac{10^{4}}{8\times10^{-7}} = 1.25\times10^{10}\ \mathrm{s}.$$

Steps to $t = 10^{7}$ s at that step: one. **The physical timescale binds, not
the stability limit** — a genuinely common situation in geothermal and
subsidence modelling, where the diffusivity is small and the grid is coarse. The
honest step choice is then set by accuracy: run at $dt = 10^{5}$ s, then halve it
and confirm the answer changes by less than the tolerance.

---

## ★5 — Growth at $C = 1.08$

At $\theta = \pi$: $b = 1 - 2C^{2} = 1 - 2(1.1664) = -1.3328$;

$$\lvert G\rvert = 1.3328 + \sqrt{1.3328^{2}-1} = 1.3328 + \sqrt{0.77635}
= 1.3328 + 0.88111 = 2.21391.$$

Steps to exceed $10^{6}$: $n = \ln 10^{6}/\ln 2.21391 = 13.8155/0.794837
= 17.4$, i.e. **18 steps**. An unstable wave run is visible almost immediately.

---

## ★6 — Stable and wrong at the same time

**Amplitude ratio $0.99992$ after 1000 steps.** This measures the *growth* of
the numerical solution relative to its own initial amplitude — a property of the
amplification factor. The trapezoidal scheme has $\lvert G\rvert = 1$ for every
$C$ and every mode, so no mode grows; the tiny deficit is round-off and the
windowing of the measurement, not a systematic decay.

**$L^{2}$ error $2.03\times10^{-1}$ against the exact solution.** This measures
*the difference from the correct answer*, and it grows linearly in $C$
($1.10\times10^{-2}$ at $C = 0.5$, $4.36\times10^{-2}$ at $C = 2$,
$2.03\times10^{-1}$ at $C = 10$). At $C = 10$ the scheme takes ten cells per
step, so the numerical phase speed of most modes is badly wrong even though the
amplitudes are preserved.

**How both are true.** Stability constrains the *magnitude* of the amplification;
accuracy constrains its *phase* (and the amplitude's deviation from the exact
exponential). A scheme can be exactly neutral in amplitude and completely wrong
in phase — which is what "unconditionally stable, inconsistent for coarse steps"
looks like.

---

## ★7 — Making the thermal run ten times faster

**Current cost.** $dt_{\max} = h^{2}/(2\alpha d) = 625/(2\times10^{-6}\times2)
= 1.5625\times10^{8}$ s. For a physical horizon of, say, $10^{6}$ years
($3.156\times10^{13}$ s), the explicit scheme needs about $2\times10^{5}$ steps.

**Change.** Switch to Crank–Nicolson. It is unconditionally stable and
second-order in time, so $dt$ can be set by accuracy. A tenfold to hundredfold
increase in $dt$ is typical; at $dt = 100\,dt_{\max}^{\text{accuracy}}$ the step
count falls by that factor, at the cost of one sparse solve per step.

**Risks and tests.** (i) *Time-truncation error.* Test by running at $dt$ and
$dt/2$ and confirming the observed order is two and the answer changes by less
than the tolerance. (ii) *Oscillatory artefacts.* Crank–Nicolson does not damp
the highest modes — they are neutral, so a poor initial condition can leave a
non-decaying grid-scale ringing. Test by initialising a checkerboard perturbation
at $10^{-6}$ and confirming it does not grow and does not persist in the reported
solution (or add a small amount of numerical damping, e.g. a
backward-Euler/CN blend for the first few steps).

---

## ★8 — A stable scheme with an unresolvable artefact

**Scenario.** A time-dependent diffusion or wave problem solved with an implicit
scheme at a step that is stable but much larger than the physical timescale of
the process being observed. The scheme's removal of the stability limit permits
$dt$ to exceed the time it takes the physics to change.

**Mechanism.** The amplification factor of an implicit scheme approximates
$e^{-\lambda dt}$ at small $dt$; at large $dt$ it deviates. For the model problem
$u_t = -\lambda u$, Crank–Nicolson gives
$G = (1-\lambda dt/2)/(1+\lambda dt/2)$, which is negative for
$\lambda dt>2$: the solution alternates in sign each step while decaying. The
physics has no such oscillation; the scheme has introduced one, and it is a
property of $dt$, not of $h$.

**Measurement that distinguishes it.** Refine $dt$ at fixed $h$: a numerical
artefact moves or disappears as $dt\to0$ (the oscillation frequency scales with
$1/dt$ and the amplitude with $(\lambda dt)^{n}$), while a physical oscillation
is unchanged. A second, independent check is to compare against the exact
solution of the *space-discretised* problem: that comparison removes the spatial
error and exposes the temporal one, exactly as the demonstration does for the
order measurement.
