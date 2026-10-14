# Solutions — 19-03-04 Finite Volume Methods and Conservative Discretisation

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [04 Finite Volume Methods and Conservative Discretisation](../04-finite-volume.md).

---

## ★1 — The conservation proof

Per cell, $u_i^{n+1} = u_i^n - \frac{\Delta t}{\Delta x_i}
(F_{i+1/2} - F_{i-1/2})$. Multiply by $\Delta x_i$ and sum over a periodic domain
of $N$ cells:

$$\sum_i (u_i^{n+1} - u_i^n)\Delta x_i
= -\Delta t \sum_i (F_{i+1/2} - F_{i-1/2}) = 0 .$$

The sum telescopes because each face appears twice, once as $F_{i+1/2}$ with a
plus sign (cell $i$) and once as $F_{i-1/2}$ with a minus sign (cell $i+1$). On a
periodic domain there are no boundary faces left over.

**The single design decision** is that each face carries *one* flux, used by both
of its cells. Nothing else about the scheme — order, limiter, mesh — enters the
proof.

---

## ★2 — Advection parameters

With $a = 2$ m/s, $\Delta x = 0.02$ m, $C = 0.6$:

$$\Delta t = \frac{C\Delta x}{a} = \frac{0.6(0.02)}{2} = 0.006\ \text{s},$$

$$D_{\rm num} = \frac{a\Delta x (1-C)}{2} = \frac{2(0.02)(0.4)}{2}
= 8.0\times10^{-3}\ \text{m}^2\,\text{s}^{-1},$$

$$\sqrt{2D_{\rm num}t} = \sqrt{2(8.0\times10^{-3})(0.5)}
= 8.94\times10^{-2}\ \text{m} .$$

The diffusion length is 4.5 cells: after half a second a sharp front has been
smeared over several cells, and the smearing is arithmetic, not accidental.

---

## ★3 — Faces of a one-dimensional cell

A cell $[x_{i-1/2}, x_{i+1/2}]$ has a left face $i-1/2$, a right face $i+1/2$,
and (counting the cell as a *volume* with two "ends") nothing else in one
dimension. **Both** faces are shared with another cell on a periodic mesh of more
than two cells: the left face with cell $i-1$, the right with cell $i+1$. There
are no boundary faces, which is exactly why the sum in ★1 vanishes. On a
non-periodic mesh there are two boundary faces (at the first cell's left and the
last cell's right), and they carry the physical fluxes entering and leaving the
domain.

---

## ★4 — One upwind step on two cells

With $a = 1$ m/s (so the upwind value at face $i+1/2$ is $u_i$), $\Delta x = 0.01$
m, $C = 0.7$, and $u_{i-1} = 1.0$, $u_i = 0.7$, $u_{i+1} = 0.2$:

- cell $i$: $u_i^{n+1} = 0.7 - 0.7(0.7 - 1.0) = 0.7 + 0.21 = 0.91$;
- cell $i+1$: $u_{i+1}^{n+1} = 0.2 - 0.7(0.2 - 0.7) = 0.2 + 0.35 = 0.55$.

Change over the pair: $(0.91-0.70) + (0.55-0.20) = 0.21 + 0.35 = 0.56$.

Net boundary flux of the pair: the flux in at the left face is
$F_{i-1/2} = u_{i-1} = 1.0$ and out at the right face $F_{i+3/2} = u_{i+1} = 0.2$,
so the change is $C(1.0 - 0.2) = 0.7(0.8) = 0.56$. ✔

The internal face $F_{i+1/2} = 0.7$ cancelled exactly: it appeared with opposite
signs in the two cells. That cancellation is the conservation proof in miniature.

---

## ★5 — First-order scaling of the measured diffusion

The measured $2D_{\rm num}$ values, divided by $a\Delta x$ with $a = 1$ m/s:

| $\Delta x$ (m) | $2D_{\rm num}$ (m²/s) | $2D_{\rm num}/(a\Delta x)$ |
|---|---|---|
| 0.01000 | 0.00199987 | 0.2000 |
| 0.00500 | 0.00099986 | 0.2000 |
| 0.00250 | 0.00049986 | 0.1999 |

The ratio is constant at $0.2000 = 1 - C$: the measured coefficient is exactly
$a\Delta x(1-C)$, i.e. $D_{\rm num} = a\Delta x(1-C)/2$, at every mesh — first
order in $\Delta x$ with no drift.

Prediction at $\Delta x = 0.00125$ m (one further halving):
$2D_{\rm num} = 0.00199987/8 = 2.4998\times10^{-4}$ m²/s, i.e.
$D_{\rm num} = 1.2499\times10^{-4}$ m²/s. Note that this is a *prediction from a
law the data already fixed*, not an independent measurement; the measurement that
would test it is the one line of code that reruns the experiment at
$N = 800$.

---

## ★6 — The theorem, and the measured numbers

**Godunov's theorem:** a *linear* monotone scheme for a scalar conservation law
is at most first-order accurate. Equivalently, no linear scheme of order
$\ge 2$ is monotone: there is no linear second-order scheme that avoids
overshoots.

Measured on a unit square pulse after 0.5 s at CFL 0.8 (total variation of the
data: 2.000000):

| scheme | $\max u$ | $\min u$ | total variation |
|---|---|---|---|
| upwind | 0.999995 | $+0.000000$ | 1.999990 |
| Lax–Wendroff | 1.174417 | $-0.174417$ | 3.003499 |

Upwind preserves the range and (very nearly) the total variation; Lax–Wendroff
overshoots by 17%, undershoots below zero, and raises the total variation by 50%.
Both facts are *measured consequences* of the theorem, and both are reported as
numbers a user can compare with a requirement.

---

## ★7 — The harmonic face transmissibility

Two half-cells of width $\Delta x/2$ sit in series between the two cell centres,
one with coefficient $a_L$ and one with $a_R$. A series resistance per unit area
adds:

$$R = \frac{\Delta x/2}{a_L} + \frac{\Delta x/2}{a_R}
= \frac{\Delta x}{2}\left(\frac{1}{a_L}+\frac{1}{a_R}\right).$$

The effective face coefficient $T$ satisfies $R = \Delta x/T$, so

$$\frac{\Delta x}{T} = \frac{\Delta x}{2}\cdot\frac{a_L+a_R}{a_La_R}
\Longrightarrow T = \frac{2a_La_R}{a_L+a_R},$$

the harmonic mean. **Check:** if $a_L = a_R = a$ then
$T = 2a^2/(2a) = a$ ✔ — a homogeneous medium must not be penalised by the
interface treatment. The arithmetic mean $\tfrac12(a_L+a_R)$ also reduces to $a$,
so the test does not distinguish the two; a jump does.

For $a_R/a_L = 1000$ (set $a_L = 1$): $T_{\rm harm} = 2(1000)/1001 = 1.998002$,
$T_{\rm arith} = 500.5$, ratio

$$\frac{T_{\rm arith}}{T_{\rm harm}} = \frac{(1+1000)^2}{4(1000)} = 250.5002,$$

agreeing with the closed form $(a_L+a_R)^2/(4a_La_R)$ from the lesson. The full
1000-fold contrast is reduced to a 1.998-fold effective contrast, which is the
physically correct answer and a 250-fold smaller error than the arithmetic mean
would introduce.

---

## ★8 — Numerical diffusion versus face-coefficient error

**Two configurations.** Solve the same advection problem, $u_t + (a(x)u)_x = 0$,
on the same graded mesh, with the same $\Delta x$ and CFL:

- **C1 (diffusion-limited):** a *smooth*, slowly varying $a(x)$ — say
  $a = 1 + 0.05\sin(2\pi x)$ — so the face coefficient is well represented by any
  reasonable average and the upwind truncation error is the only first-order
  term.
- **C2 (coefficient-limited):** the same $a(x)$ but with an interface-like jump
  of 10:1 at one face, or a piecewise-constant $a$, so the face coefficient is
  the dominant error.

**Metric.** The $\mathrm{L}^1$ error norm at a fixed time, and (decisively) its
*slope* against $\Delta x$ on three meshes, together with the error's spatial
distribution: a diffusion-dominated error is spread over $\sqrt{2D_{\rm num}t}$
of the domain; a coefficient error is localised at the face.

**Predictions.**

- In **C1** the error should scale as $D_{\rm num}t$ with the *measured*
  coefficient $a\Delta x(1-C)/2$ — the lesson's Section 2 result — and the error
  should be distributed across the whole front. Reducing $\Delta x$ by 2 halves
  it.
- In **C2** the error should be concentrated at the face and be proportional to
  the *contrast*, not to $\Delta x$ alone; halving $\Delta x$ does not halve it,
  and the measured sign of the error should be opposite on the two sides of the
  face (the interface is displaced one way or the other).
- **The decisive observation** is the spatial distribution: if the error is
  spread, it is diffusion; if it is a localised pair of opposite-sign lobes at a
  face, it is the coefficient. Neither a global error norm nor a single mesh
  distinguishes them, because both errors are first order overall.
