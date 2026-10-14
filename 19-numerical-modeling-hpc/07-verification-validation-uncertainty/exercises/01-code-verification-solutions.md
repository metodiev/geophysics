# Solutions — 19-07-01 Code Verification: Order-of-Accuracy and Manufactured Solutions

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Lesson: [01 Code Verification](../01-code-verification.md).

---

## ★1 — Truncation term and predicted error

Taylor expansion gives

$$\frac{u_{i-1} - 2u_i + u_{i+1}}{h^{2}} = u'' + \frac{h^{2}}{12}u^{(4)} + O(h^{4}),$$

so $\tau = \frac{h^{2}}{12}u^{(4)}$. For $u = \cos(2\pi x)$,
$u^{(4)} = (2\pi)^{4}\cos(2\pi x) = 16\pi^{4}\cos(2\pi x)$. The error satisfies
$L_h e = \tau$ and $L_h \approx -(2\pi)^{2}$ on this mode, so

$$e \approx -\frac{h^{2}}{12}\cdot\frac{16\pi^{4}}{4\pi^{2}}\cos(2\pi x)
= -\frac{h^{2}\pi^{2}}{3}\cos(2\pi x).$$

At $N = 64$, $h = 1.560\times10^{-2}$, $h^{2} = 2.4414\times10^{-4}$:

$$\text{amplitude} = \frac{2.4414\times10^{-4}\times9.8696}{3}
= 8.032\times10^{-4}, \qquad
\text{RMS} = \frac{8.032\times10^{-4}}{\sqrt{2}} = 5.68\times10^{-4}.$$

This equals the demonstration's measured FD2 error at $N = 64$,
$5.682\times10^{-4}$, because $\sin(2\pi x)$ and $\cos(2\pi x)$ share the same
wavenumber and therefore the same $h^{2}\pi^{2}/3$ amplitude.

---

## ★2 — Observed order

$$p = \frac{\ln\left(\frac{4.00\times10^{-2}}{1.00\times10^{-2}}\right)}{\ln 2}
= \frac{\ln 4}{\ln 2} = 2,$$

and the second pair gives $\ln(4)/\ln 2 = 2$ again. The values are exactly
second order, so the scheme is consistent with a second-order code. Note the
converse is not implied: a first-order code with a fortuitously $4\times$ error
drop cannot happen twice in a row *and* be first order, so this pair of ratios is
already strong evidence.

---

## ★3 — Why the $\sqrt{h}$ weight

The discrete sum $h\sum_i e_i^{2}$ approximates $\int e^{2}\,\mathrm{d}x$, so its
square root approximates the continuous $L^{2}$ norm and is independent of $N$.
Dropping the weight leaves $\sqrt{\sum_i e_i^{2}}$, which grows as $N^{1/2}$ for a
fixed per-point error: two codes on different grids would then differ by the
$\sqrt{N}$ factor alone, and a refinement study would show an apparent order
$p - 1/2$ instead of $p$.

---

## ★4 — Centred and backward differences

With $u_{i\pm1} = u_i \pm h u'_i + \frac{h^{2}}{2}u''_i \pm \frac{h^{3}}{6}u'''_i
+ \frac{h^{4}}{24}u^{(4)}_i \pm \dots$,

$$\frac{u_{i+1} - u_{i-1}}{2h} = u'_i + \frac{h^{2}}{6}u'''_i + O(h^{4}):$$

second order for a first derivative. The backward difference has
$\tau = -\frac{h}{2}u''$, first order. For the **steady** advection equation
$au' = f$ solved with the centred operator, the discrete system is a consistent
second-order approximation and the global error is $O(h^{2})$. Marching with the
backward difference, the error obeys a recurrence in which the local $O(h)$
truncation accumulates over $N = 1/h$ steps, giving $O(h)$ globally — the
demonstration measures $1.004$.

---

## ★5 — A manufactured solution that tests both derivatives

Take $u_m = \sin(2\pi x)\sin(3\pi y)$, so

$$\nabla^{2}u_m = -\left(4\pi^{2} + 9\pi^{2}\right)u_m = -13\pi^{2}u_m,
\qquad f = -13\pi^{2}u_m .$$

The sensitivity comes from $a \neq b$: the two partial derivatives have different
magnitudes, so a code that drops or swaps one of them produces an $O(1)$ error
instead of an $O(h^{2})$ one. With $u_m = \sin(2\pi x)\sin(2\pi y)$ (equal
wavenumbers) a swap is invisible, and with $u_m = \sin(2\pi x)$ alone a dropped
$y$-derivative is invisible.

---

## ★6 — Why the residual check fails

The residual is $\lVert A u_h - f_h\rVert$ with $f_h$ the *code's* source. Scaling
the source by $1.02$ changes both $f_h$ and the solution $u_h$ consistently:
$u_h = 1.02\,u$, so $Au_h - f_h = 1.02(Au - f) = 1.02 \times 0$ to the accuracy of
the linear solve. The measured residual $1.83\times10^{-13}$ is round-off, which is
$10^{11}$ times smaller than the error $2.02\times10^{-2}$ it is supposed to detect.

The check that does catch it: compare $u_h$ with a **manufactured** exact solution,
$u_m = \sin(\pi x)\sin(2\pi y)$, at two or more resolutions, and confirm the
observed order is $2$. A wrong source makes the error converge to a constant
(measured apparent orders $0.139$, $0.037$, $0.009$).

---

## ★7 — Separating spatial and temporal orders

**Design.** Manufacture $u_m(x,t)$ for the semi-discrete problem, then choose the
time step so the two error terms are comparable and can be varied independently:

1. **Temporal order first.** Fix $h$ well inside the asymptotic range (say the
   measured $L^{2}$ spatial error at that $h$ is $10^{-3}$), then refine $\Delta t$
   by factors of $2$ until the error stops falling. The plateau at the spatial error
   level, and the rate of fall before it, give the time order.
2. **Spatial order second.** With $\Delta t$ small enough that $e_{\text{time}} <
   10^{-2}e_{\text{space}}$, refine $h$ and measure the spatial order.
3. **Coupling.** If you must vary both, impose
   $\Delta t = C h^{p_s/p_t}$ so that $e_{\text{time}} = C^{p_t}h^{p_s}$ has the same
   order as $e_{\text{space}}$; the measured order is then the common $p_s$, and the
   two contributions appear as a single coefficient you cannot separate. The
   *first* design is the one that answers the question.

**Expected orders.** $p_s = 2$ from the spatial study, $p_t = 2$ from the
temporal study. If the time integrator were first order, the temporal study would
show $1$ and the coupled study would show an order that drifts between $1$ and $2$
with the value of $C$ — the diagnostic symptom of a coupled order study.

---

## ★8 — A wrong-order boundary condition

If the error is $O(h^{2})$ at $N$ interior nodes and $O(h)$ in a boundary layer of
$m$ nodes (with $m$ fixed as $h \to 0$), the discrete squared norm is
$h\sum e_i^{2} \approx h\left(mh^{2} + Nh^{4}\right) = mh^{3} + h^{4}$, so
$\lVert e\rVert \approx \sqrt{m}\,h^{3/2}$: the observed order reads about $1.5$,
not $2$ and not $1$ — a value that is easy to dismiss as "not yet asymptotic" and
hard to interpret.

**Local diagnostic.** Refine and plot $\log|e_i|$ against node index. In the
asymptotic range the interior error falls by $4$ per doubling while the boundary
layer's error falls by $2$; the *spatial extent* of the slow region also shrinks,
so the pattern is a wedge at the boundary, not a uniform offset. A sharper test is
to impose the boundary data exactly (Dirichlet) on a problem with a known
solution: if the $O(h)$ wedge survives exact boundary data, the operator itself,
not the data, is at fault.
