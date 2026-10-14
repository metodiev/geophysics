# Solutions — 19-03-05 FEM in Geophysics: EM, Geodynamics and Seismology

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [05 FEM in Geophysics: EM, Geodynamics and Seismology](../05-fem-geophysics.md).

---

## ★1 — Skin depth

$$\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}}
= \sqrt{\frac{2}{2\pi(0.1)(4\pi\times10^{-7})(0.1)}} = 5032.921\ \text{m}.$$

Unit check: $\omega\mu_0\sigma$ has units
$\text{s}^{-1}\cdot\text{H\,m}^{-1}\cdot\text{S\,m}^{-1} =
\text{s}^{-1}\text{m}^{-2}$, so $2/(\omega\mu_0\sigma)$ is m² and its square root
is metres. Note the scaling: $\sigma$ fell by 10 and $f$ by 10 relative to the
lesson's 1 Hz, 0.01 S/m case, so $\delta$ is unchanged — the square root of the
product is what matters.

---

## ★2 — Uniform half-space

$$Z = \sqrt{\frac{\mathrm{i}\omega\mu_0}{\sigma}}, \qquad
\arg Z = 45^\circ, \qquad
\rho_a = \frac{|Z|^2}{\omega\mu_0} = \frac{1}{\sigma}.$$

For $\sigma = 0.01$ S/m: $1/\sigma = 100.000000$ Ω·m, and the lesson measures
$\rho_a = 100.000000$ Ω·m and phase $45.000000^\circ$ with
$|Z| = 2.809926\times10^{-2}$ Ω at $f = 1$ Hz. The identity
$\rho_a = 1/\sigma$ for a uniform half-space is exact, and it is the first test any
MT code should pass.

---

## ★3 — Radiation condition

At the base of the domain ($z = L$), with $E(z) = E_0e^{-kz}$ and
$p = 1/(\mathrm{i}\omega\mu_0)$:

$$\frac{E'(L)}{E(L)} = -k \quad\Longrightarrow\quad
\boxed{\,p\,E'(L) = -\sqrt{\frac{\sigma}{\mathrm{i}\omega\mu_0}}\,E(L)\,} .$$

**The sign is fixed by the decaying branch.** Only $e^{-kz}$ remains bounded as
$z\to\infty$; the other solution $e^{+kz}$ grows without bound, and the sign of
the admittance is what selects the bounded one. There is no freedom here, and the
reported "slightly wrong answer" of a sign error is in fact an $O(1)$ error
(Section 7 below).

---

## ★4 — Site response parameters

$$\gamma = \frac{\rho_1\beta_1}{\rho_2\beta_2}
= \frac{(2000)(500)}{(2500)(1500)} = 0.266667,$$

$$f_0 = \frac{\beta_1}{4H} = \frac{500}{4(100)} = 1.2500\ \text{Hz},
\qquad \frac{1}{\gamma} = 3.750000 .$$

The lesson measures the resonances at 1.2506 Hz and 3.7509 Hz against predictions
1.2500 and 3.7500 — both within one scan grid step (0.0026 Hz) — and the largest
$|T|$ on the scan as $3.750346$ against $1/\gamma = 3.750000$.

---

## ★5 — Manufactured solution and stress balance

With $u = y(1-y)$: $u' = 1-2y$, $u'' = -2$. With $\nu = 1+0.5y$: $\nu' = 0.5$.

$$-(\nu u')' = -\left[\nu'u' + \nu u''\right]
= -\left[0.5(1-2y) - 2(1+0.5y)\right]
= -\left[0.5-2 - y - y\right] = 1.5 + 2y . ✔$$

Stress: $\tau = \nu u' = (1+0.5y)(1-2y)$, so

$$\tau(0) = 1(1) = 1.000, \qquad
\tau(1) = 1.5(-1) = -1.500, \qquad
\tau(1)-\tau(0) = -2.500 .$$

The right-hand side: $-\int_0^1 f\,\mathrm{d}y = -(1.5 + 2\cdot0.5) = -2.500$ ✔.

The balance holds exactly for the manufactured pair, which is the point: the
manufactured *forcing* was chosen so that the stress difference equals it. A
solver that reproduces $u$ but not this identity has an assembly error that a
small $\mathrm{L}^2$ error would hide.

---

## ★6 — Why the apparent resistivity rises with period

The diffusive skin depth grows as $\sqrt{T}$, where $T = 1/f$ is the period. At
5 Hz the skin depth in layer 1 ($\sigma_1 = 0.01$ S/m) is

$$\delta_1 = \sqrt{\frac{2}{2\pi(5)(4\pi\times10^{-7})(0.01)}} = 2250\ \text{m},$$

comparable to the 2000 m layer thickness, so the measurement senses mostly layer 1
and $\rho_a \to 100$ Ω·m (measured 93 Ω·m at 5 Hz: close, and slightly low because
a little of the resistive half-space is already felt).

At 0.1 Hz, $\delta_1$ grows by $\sqrt{50} = 7.07$ to about 15.9 km, far beyond
the layer, so the measurement senses the 1000 Ω·m half-space and $\rho_a$ rises
(measured 511 Ω·m at 0.1 Hz — intermediate between 100 and 1000 because the
transition is not complete).

**The controlling parameter is the ratio of skin depth to layer thickness**, not
frequency alone. Doubling the layer thickness moves the rise to a longer period
by a factor 4, since $\delta \propto \sqrt{T}$. That is why MT model curves are
plotted against period on a log scale: the layer's signature appears when
$\delta \gtrsim h_1$.

---

## ★7 — The growing branch, and what the wrong sign does

Writing $k = \sqrt{\mathrm{i}\omega\mu_0\sigma} = (1+\mathrm{i})/\delta$ (a
standard form for the diffusive wavenumber), the two solutions are
$e^{-kz}$ (decaying) and $e^{+kz}$ (growing). Choosing the wrong sign in the
admittance imposes $E'/E = +k$ instead of $-k$, i.e. it selects the growing
branch.

**Magnitude of the growth.** With $L = 4\delta$ the exponent is
$|k|L = 4\sqrt{2} = 5.6569$, so the growing solution is larger at the bottom than
at the top by

$$e^{4\sqrt{2}} = 2.8625\times10^{2}.$$

That number matches the *measured* magnitude of the failure: the relative
$\mathrm{L}^2$ error against the analytic $e^{-kz}$ was $2.203\times10^{2}$ at 50
elements. The error is the size of a solution that has been turned inside out.

**What a convergence study reports.** From the recorded run the errors were
$2.203\times10^{2} \to 6.785\times10^{1} \to 5.740\times10^{1} \to 5.527\times10^{1}
\to 5.476\times10^{1}$ for 50 to 800 elements: the error drops quickly and then
*stagnates* at about 55. A fitted slope over that range gives 0.502, which looks
like a slow first-order-ish rate and is misleading: the sequence is converging,
but to a **different function**. With $|R| = 1$ at the artificial boundary the
discrete problem has a reflected (standing-wave) solution, and the distance from
that solution to the decaying one is $O(1)$ at every mesh.

**The diagnostic.** Stagnation of the error under refinement — not its size — is
what identifies a wrong boundary condition. A truncation error would keep
falling; a wrong datum gives a floor.

---

## ★8 — Formulation error versus derivative-recovery error

**Two runs, one physical model** (the two-layer MT model of the lesson):

- **Run A — the isolated formulation test.** A *uniform* half-space, where the
  exact field $e^{-kz}$ is known and no layered structure is present, solved with
  the same elements and the same radiation datum. Metric: the relative
  $\mathrm{L}^2$ error of the *field* $E(z)$ against $e^{-kz}$, as a function of
  mesh. No derivative recovery is involved, so this measures the formulation.
  Measured: $1.038\times10^{-3}$ at 50 elements falling at order **2.000** — the
  formulation is second-order correct.

- **Run B — the layered problem, impedance metric.** The same code on the
  two-layer model, with the *surface impedance* computed from $E(0)$ and a
  one-sided difference for $E'(0)$. Metric: the relative error of $\rho_a$
  against the exact recursion. Measured: $1.7$–$5.0\times10^{-3}$ at 600
  elements.

**Diagnosis.**

- If Run A is second order and Run B is stuck at $10^{-3}$-ish regardless of the
  number of elements, the formulation is sound and the **derivative recovery**
  limits the answer. The fix is a better $E'(0)$: a quadratic element, or a
  weak-flux recovery, and the test is that Run B's error should then fall with
  mesh.
- If Run A fails (order below 2, or a stagnating error), the **element
  formulation or the datum** is at fault, and improving the derivative recovery
  would be fixing the wrong thing.
- If both fail with the *same* stagnating error, the radiation datum is the
  suspect — which is exactly the sign test of Section 7.

**Why this design works.** The two error sources live in different places: the
formulation error is in the *field*, the recovery error is in a *derivative*. A
test that measures the field on a problem with an exact field isolates one; a
test that measures an impedance from a differentiated field exposes the other.
