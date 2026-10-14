# Solutions — 19-01-03 Consistency, Stability and the Lax Equivalence Theorem

> **Read after attempting the exercises.** Arithmetic is shown; the measured
> numbers come from `../code/consistency_stability_demo.py`.

Lesson: [03 Consistency and Stability](../03-consistency-stability.md).

---

## ★1 — Amplification at three modes

$$G(\theta) = 1 - C\left(1 - e^{-\mathrm i\theta}\right),
\qquad C = 0.8.$$

$\theta = 0$: $G = 1$, $|G| = 1$ (a constant is preserved exactly).

$\theta = \pi/2$: $G = 1 - 0.8(1 - \mathrm i) = 0.2 + 0.8\mathrm i$,
$|G| = \sqrt{0.04+0.64} = \sqrt{0.68} = 0.824621$.

$\theta = \pi$: $G = 1 - 0.8(2) = -0.6$, $|G| = 0.6$.

---

## ★2 — The theorem

**Theorem.** For a consistent discretisation of a well-posed linear
initial-value problem, stability is equivalent to convergence.

**Hypotheses.** (i) *Linearity* — so that the error equation
$e^{n+1} = Se^{n} + dt\,\tau^{n}$ superposes and the bound
$\|e^{n}\|\le KT\max\|\tau\|$ can be formed. (ii) *Well-posedness* of the
continuous problem — so a bounded scheme is approximating something that has a
unique solution.

---

## ★3 — Central in space, forward in time

$$G = 1 - \mathrm iC\sin\theta, \qquad |G|^{2} = 1 + C^{2}\sin^{2}\theta.$$

At $C = 0.3$ and $\theta = \pi/2$: $|G| = \sqrt{1.09} = 1.044031$. The scheme is
**unconditionally unstable**: for every $C>0$ and every mode with
$\sin\theta\ne0$, $|G|>1$. The measured demonstration values
(1.03077641 at $C = 0.25$, 1.11803399 at $C = 0.5$, 1.41421356 at $C = 1.0$)
match $\sqrt{1+C^{2}}$ exactly at $\theta = \pi/2$.

---

## ★4 — Growth at $C = 1.4$

$|G(\pi)| = |1-2(1.4)| = 1.8$ exactly (since $\sin\pi = 0$). After 100 steps:
$1.8^{100} = 3.1\times10^{25}$. Numerical check:
$\ln 1.8 = 0.5877867$, $\times100 = 58.77867$, $e^{58.77867}
= 3.1\times10^{25}$.

Amplitude $= 10^{-6}\times3.1\times10^{25} = 3.1\times10^{19}$.

Steps to reach unity: $n = -\ln(10^{-6})/\ln 1.8 = 13.8155/0.5877867 = 23.5$,
so 24 steps. **The instability is visible within 24 steps** — this is why
unstable runs are rarely ambiguous.

---

## ★5 — Consistency residual

With $u = \sin(2\pi(x-t))$, $u_{xx} = -4\pi^{2}u$ and
$u_{tt} = a^{2}u_{xx}$ along $u_t + au_x = 0$:

$$R = \frac{u(t+dt)-u(t)}{dt} + a\frac{u(x)-u(x-h)}{h}
      = \frac{dt\,a^{2}}{2}u_{xx} - \frac{ah}{2}u_{xx} + O(dt^{2},h^{2})
      = \frac{ah}{2}(C-1)u_{xx} + \cdots$$

So $R/h \to \frac{a}{2}(1-C)\cdot4\pi^{2}\sin(2\pi(x-t))$ — a finite, non-zero
limit: consistent of order one, with a diffusion-shaped leading term.

**At $C = 1$** the leading term vanishes identically. The next terms are
$O(dt^{2},h^{2})$, and in fact the scheme becomes exact: with $C = 1$,
$U_j^{n+1} = U_{j-1}^{n}$ is a pure shift by one cell, reproducing the exact
solution of $u_t + au_x = 0$ on the grid. The measured $L^{\infty}$ error after
100 steps is $7.772\times10^{-16}$, i.e. round-off.

---

## ★6 — Identifying the scheme from its growth rate

$|G| = 1.11803399 = \sqrt{1.25} = \sqrt{1+C^{2}}$ at $\theta = \pi/2$ with
$C = 0.5$. That is the signature of **centred-in-space, forward-Euler-in-time
advection**, unconditionally unstable at $C = 0.5$; the demonstration prints
this exact value (1.11803399 at $C = 0.5$, 123.8 steps to grow $10^{6}\times$).

**Confirmation:** start the run in the pure eigenmode $e^{\mathrm i\pi j/2}$
and measure the growth per step for three consecutive $C$ values; the measured
rates must lie on the curve $\sqrt{1+C^{2}\sin^{2}\theta}$ at
$\theta = \pi/2$. A second, independent confirmation is to check the *spatial*
symmetry: replacing the centred difference by an upwind difference should make
the run stable at the same $C$, which isolates the cause to the spatial
discretisation rather than the time step.

---

## ★7 — Stable but inconsistent

**Construction.** Use upwind differencing but with the *wrong* speed:
$U_j^{n+1} = U_j^{n} - C'(U_j^{n} - U_{j-1}^{n})$ with
$C' = C(1-\epsilon)$, i.e. the scheme advances with $a' = a(1-\epsilon)$.

**Prediction.** Consistency fails: the residual is
$\epsilon a\,u_x + O(h)$, which does not vanish as $h\to0$ at fixed $\epsilon$.
The scheme is stable for $C'\le1$, so by the contrapositive of Lax equivalence it
cannot converge to the solution of the intended equation; it converges to the
solution of $u_t + a'u_x = 0$ instead.

**Experiment.** Advect a pulse over a long distance with $\epsilon = 0.01$ and
refine $h$ at fixed $C$: the error against the exact solution of the intended
equation *saturates* at a non-zero value (the accumulated travel-time error
$\epsilon a T$), while, measured against $u_t + a'u_x = 0$, the scheme
converges at order one.

**What a practitioner sees first.** A travel-time bias that does not shrink with
refinement — the classic symptom of a wrong coefficient, and the reason
verification against an *exact* solution is not optional.

---

## ★8 — Where the linearity hypothesis fails

**Case.** Variable-coefficient advection, $u_t + a(x)u_x = 0$ with a smooth
$a(x)$ discretised with a locally upwind scheme.

**Which hypothesis fails.** Linearity of the *proven* statement: the error
equation now has an operator $S(x)$ that varies from cell to cell, so the bound
$\|S^{m}\|\le K$ must hold uniformly in $x$, not merely for a single constant
operator. A locally stable scheme can fail to be uniformly stable when the
coefficient varies — a resonance between the coefficient variation and the grid
can excite a growing mode that von Neumann analysis of the frozen coefficient
never sees.

**Measurement.** Freeze the coefficient at a value, verify the growth of the
grid-Nyquist mode is below one (frozen-coefficient stability), then run the same
scheme with the coefficient varying by $\pm10\,\%$ over ten cells and repeat the
eigenmode experiment. If the measured growth exceeds one, the frozen-coefficient
test was not sufficient. A second measurement is the convergence study: run
refinements at fixed CFL and check that the observed order matches the
truncation order; a stable, consistent scheme that is not *uniformly* stable
will show an order that degrades with refinement instead of improving.
