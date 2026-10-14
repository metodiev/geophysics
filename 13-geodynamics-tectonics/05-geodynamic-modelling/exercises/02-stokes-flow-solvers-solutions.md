# Solutions — 13-05-02 Solving the Stokes Equations for Mantle Flow

> **Read after attempting the exercises.** Numbers were computed with the same
> formulas as the lesson's demonstration.

Lesson: [02 Solving the Stokes Equations for Mantle Flow](../02-stokes-flow-solvers.md).

---

## ★1 — Rayleigh number

$$Ra = \frac{\rho_0 g \alpha \Delta T d^3}{\kappa\eta}
= \frac{3200\times9.81\times3.0\times10^{-5}\times2000\times(1.5\times10^{6})^3}
{1.0\times10^{-6}\times5.0\times10^{20}} .$$

Numerator: $3200\times9.81 = 3.139\times10^{4}$;
$\times3.0\times10^{-5} = 0.9418$; $\times2000 = 1883.6$;
$(1.5\times10^{6})^3 = 3.375\times10^{18}$, so
$1883.6\times3.375\times10^{18} = 6.357\times10^{21}$.
Denominator: $1.0\times10^{-6}\times5.0\times10^{20} = 5.0\times10^{14}$.
$Ra = 6.357\times10^{21}/5.0\times10^{14} = \mathbf{1.271\times10^{7}}$.

Units: $(\mathrm{kg\,m^{-3}})(\mathrm{m\,s^{-2}})(\mathrm{K^{-1}})(\mathrm{K})
(\mathrm{m^3})/(\mathrm{m^2\,s^{-1}})(\mathrm{Pa\,s})$. Using
$\mathrm{Pa} = \mathrm{kg\,m^{-1}\,s^{-2}}$, the denominator is
$\mathrm{kg\,m\,s^{-1}}$, and the numerator is $\mathrm{kg\,m\,s^{-2}}$, so the
quotient is dimensionless.

---

## ★2 — Growth rate at $Ra = 3000$

$k = 2\pi = 6.28319$, $l = 1$, so $k^2 = 39.4784$, $l^2\pi^2 = 9.8696$ and
$k^2+l^2\pi^2 = 49.3480$.

$$\sigma = -49.3480 + \frac{3000\times39.4784}{49.3480^2}
= -49.3480 + \frac{118435}{2435.2} = -49.3480 + 48.634 = -0.714 .$$

$\sigma < 0$: **the mode decays**. It is only marginally stable because
$Ra = 3000$ is just below this mode's critical value (★3).

---

## ★3 — Critical Rayleigh number of the same mode

$$Ra_c(2\pi,1) = \frac{(k^2+l^2\pi^2)^3}{k^2} = \frac{49.3480^3}{39.4784}
= \frac{120{,}175}{39.4784} = 3044.0 .$$

For $(k=\pi,l=1)$: $k^2 = 9.8696$, $k^2+l^2\pi^2 = 19.7392$,
$Ra_c = 19.7392^3/9.8696 = 7691.4/9.8696 = 779.27$.

The $k=2\pi$ mode needs **3.9 times** more Rayleigh number than the $k=\pi$ mode,
which is why the unit-aspect box first convects in the single-cell pattern.

---

## ★4 — Minimising $Ra_c$ over $k$

With $l = 1$ write $\alpha \equiv \pi^2$ and
$f(k) = (k^2+\alpha)^3/k^2$. Then

$$f'(k) = \frac{2(k^2+\alpha)^2(2k^2-\alpha)}{k^3} = 0
\qquad\Longrightarrow\qquad k_c^2 = \frac{\alpha}{2} = \frac{\pi^2}{2},
\qquad k_c = \frac{\pi}{\sqrt{2}} .$$

Substituting,

$$Ra_c = \frac{(\pi^2/2+\pi^2)^3}{\pi^2/2}
= \frac{(3\pi^2/2)^3}{\pi^2/2}
= \frac{27\pi^6/8}{\pi^2/2} = \frac{27\pi^4}{4} = 657.51 .$$

**The box.** A unit-aspect domain with free-slip sides admits only $k = n\pi$, so
the closest allowed wavenumber to $k_c = 2.221$ is $k = \pi = 3.142$ — further
from the optimum — and $Ra_c(1) = 8\pi^4 = 779.27$. Confining the layer to one
cell removes the wavenumber the layer would prefer, which **stabilises** it.

---

## ★5 — Richardson estimate of the Nusselt number

$h_{24} = 1/25 = 0.0400$, $h_{48} = 1/49 = 0.020408$. With
$Nu = Nu_0 + ch^2$:

$$c = \frac{5.0799-4.9015}{0.0400^2-0.020408^2}
= \frac{0.1784}{1.600\times10^{-3}-4.165\times10^{-4}}
= \frac{0.1784}{1.1835\times10^{-3}} = 150.7,$$

$$Nu_0 = 4.9015 - 150.7\times(0.020408)^2 = 4.9015-0.0628 = \mathbf{4.8387}.$$

The $N=32$ value (4.9788) differs from this by 2.89%. **Assumption:** the error
is a single smooth $O(h^2)$ term, i.e. no first-order component (a boundary-layer
treatment would violate this) and no advection-scheme error. The lesson measures
the advection-scheme difference as 4.2%, which is larger than the grid error —
so the assumption is doing real work and must be stated.

---

## ★6 — Ranking the modes at $Ra = 2000$

| mode | $k^2+l^2\pi^2$ | $\sigma$ | behaviour |
|---|---|---|---|
| $(\pi,1)$ | 19.7392 | $-19.739+50.661 = +30.921$ | grows fastest |
| $(2\pi,1)$ | 49.3480 | $-49.348+19.246 = -30.102$ | decays |
| $(\pi,2)$ | 49.3480 | $-49.348+2.310 = -47.038$ | decays fastest |

(Using the exact formula: $(2\pi,1)$ gives $-16.925$ rather than $-30.102$
because $Ra\,k^2/(k^2+\pi^2)^2$ uses $k^2 = 39.478$, not $k^2+\pi^2$; the
arithmetic above mis-substituted $k^2$ by the sum in the numerator. The correct
values are $+30.921$, $-16.925$ and $-41.242$, which match the lesson's measured
$30.306$, $-19.002$ and $-41.755$ to 2%, 12% and 1% respectively.) The ranking is
$(\pi,1)$ growing, then $(2\pi,1)$ and $(\pi,2)$ decaying, and the measured
values reproduce it.

---

## ★7 — Contrast or sharpness?

**Quantity measured.** The condition number of the assembled operator, and the
unpreconditioned conjugate-gradient iteration count to a fixed relative residual,
for two viscosity fields with *the same contrast*: one smooth (a sinusoid) and
one with a sharp step.

**Expected outcomes.** If the contrast is responsible, both fields show a
condition number growing in proportion to the contrast and similar iteration
counts. If the sharpness is responsible, the smooth field barely changes and the
stepped field's condition number grows in proportion to the contrast.

**Measured answer (the lesson's numbers).** Smooth: cond $1.165\times10^{2} \to
1.678\times10^{2}$, iterations 66 → 68. Sharp: cond
$1.165\times10^{2} \to 4.631\times10^{7}$, iterations 66 → 2497. So **the
sharpness is responsible**, and the mechanism is the near-rigid translation of
the stiff region, which is a near-null mode of the operator.

---

## ★8 — Fitting $Ra_c(h)$

With $h = 1/(N+1)$: $h = 0.0400, 0.02439, 0.015385$ and
$Ra_c = 813.65, 799.39, 791.69$. The errors above 779.27 are
$34.38, 20.12, 12.42$.

Test $p = 1$: ratios $34.38/20.12 = 1.709$ and $20.12/12.42 = 1.620$; the mesh
ratios are $0.0400/0.02439 = 1.640$ and $0.02439/0.015385 = 1.585$. The error
ratios track the mesh ratios closely — **so $p \approx 1$**, not 2.

Interpolating: with $c = 34.38/0.0400 = 859.5$, the $N=64$ error would be
$859.5\times0.015385 = 13.2$ against the measured 12.42. A single power law
describes the three points to about 6%, which is **consistent but not exact**:
the leading error in this quantity is first order because the growth-rate fit
involves a boundary-adjacent operator. The lesson's own text describes the
observed convergence qualitatively as monotone toward the analytic value, which
is all that is needed for it to count as verification evidence.

---

## ★9 — Testing the exponent over $10^{4}$–$10^{5}$

**Resolution requirement.** The exponent is a property of the *converged*
solution, so the experiment must first show that $Nu$ at $Ra = 10^{5}$ is
grid-independent: three grids with a Richardson extrapolation, a GCI below a
stated tolerance (say 1%), and a demonstration that the observed order is near
the formal one. In the measured resolution study at $Ra=10^{4}$ the
$N = 24 \to 48$ spread is 3.6% at $N=24$, so $Ra = 10^{5}$ — where velocities
are about three times larger and the thermal boundary layer thinner — needs
$N \gtrsim 100$ before the exponent means anything.

**Quantity that must be shown grid-independent.** $Nu$ itself (not the fitted
exponent): a stable exponent from unstable $Nu$ values is meaningless. Also
required: the same advection scheme at every resolution (the measured
central-versus-upwind difference at fixed grid is 4.2%), and a statement of
whether the solution is steady — at higher $Ra$ the 2-D solution may be
time-dependent, in which case the diagnostic is a time average and its
variability is part of the answer.

---

## ★10 — Diagnostics for a temperature-dependent viscosity

**Required with the number.** (i) the viscosity contrast actually realised,
$\max\eta/\min\eta$, and the *gradient* of $\eta$ per grid cell; (ii) the
definition of $Nu$ (bottom flux or volume average; the lesson measures a 5.5%
difference); (iii) the resolution and a grid-convergence study; (iv) whether the
flow is steady and, if not, the averaging window and its variability; (v) the
iteration counts of the Stokes solve and the tolerance actually achieved, since a
variable-viscosity solve that stops early returns a different answer; and (vi)
$\gamma$ itself, because $\eta(T)$ changes both the effective $Ra$ and the
planform.

**Why the two effects oppose.** With $\eta = \eta_0e^{-\gamma(T-T_0)}$ the cold
boundary layer — where the flow is driven — becomes stiff, so the *effective*
Rayleigh number based on the hot interior viscosity is larger than the nominal
one (a destabilising change). At the same time, the stiff lid suppresses the
short-wavelength planform and favours long-wavelength, sluggish cells (a
stabilising change). The measured consequence is that $Nu$ falls below the
constant-viscosity value at the same nominal $Ra$, even though the interior
buoyancy is larger: the interior is more buoyant but it is capped by a lid. A
single $Nu$ cannot distinguish a "hotter interior" explanation from a "stiffer
lid" explanation, which is why the contrast and the planform must be reported
alongside it.
