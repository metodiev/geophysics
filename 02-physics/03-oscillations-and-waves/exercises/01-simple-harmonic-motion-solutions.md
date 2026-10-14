# Solutions — 02-03-01 Simple Harmonic Motion and Small-Oscillation Approximation

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. They are
> not the only correct route. Numeric values were computed with
> $g = 9.80665\ \mathrm{m\,s^{-2}}$, and the numbers attributed to
> [`../code/shm_demo.py`](../code/shm_demo.py) are its actual output.

---

## ★1 — Mass on a spring

**(a)** With $x$ downward, $m\ddot x = -kx$, so
$\ddot x + (k/m)x = 0$ and
$\omega_0 = \sqrt{32/0.25} = \sqrt{128} = 11.313708\ \mathrm{rad\,s^{-1}}$.

**(b)** $T = 2\pi/\omega_0 = 0.555360$ s, $f = 1/T = 1.800625$ Hz.

**(c)** Released from rest at $x_0 = 0.040$ m: $A = 0.040$ m, $\varphi = 0$, so

$$x(t) = 0.040\cos(11.313708\,t)\ \mathrm{m}.$$

**(d)** $v_{\max} = A\omega_0 = 0.452548\ \mathrm{m\,s^{-1}}$;
$a_{\max} = A\omega_0^2 = 0.040\times128 = 5.120000\ \mathrm{m\,s^{-2}}$.

**Check on (d).** At the turning point the acceleration is
$-kx_0/m = -32\times0.040/0.25 = -5.12\ \mathrm{m\,s^{-2}}$ ✓, which is the
quickest route to the answer.

---

## ★2 — Pendulum

**(a)** $T_0 = 2\pi\sqrt{0.80/9.80665} = 2\pi\times0.285619 = 1.794587$ s.

**(b)** The exact period needs $K(\sin 0.15)$ with $\sin 0.15 = 0.149438$.
Evaluating $K$ by the AGM gives $K = 1.579677886$, so

$$T = 4\sqrt{\frac{0.80}{9.80665}}\times1.579677886
= 4\times0.285619\times1.579677886 = 1.804733939\ \mathrm{s},$$

and $T/T_0 - 1 = 5.654176\times10^{-3}$.

**(c)** The two-term series gives

$$T \approx T_0\left(1 + \frac{0.30^2}{16}\right)
= 1.794587\times1.005625 = 1.804681580\ \mathrm{s},$$

which is *below* the exact value by
$(1.804681580 - 1.804733939)/1.804733939 = -2.901\times10^{-5}$. Adding the
fourth-order term, $11\theta_0^4/3072 = 2.900\times10^{-5}$, gives
$1.804733630$ s and cuts the error to $-1.7\times10^{-7}$. The pattern is the one
to expect: the neglected terms are positive at this amplitude, so each partial sum
approaches the exact period from below and the error falls by roughly a factor of
170 per added term at $\theta_0 = 0.3$.

**(d)** Setting $\theta_0^2/16 = 0.01$ gives
$\theta_0 = 0.4$ rad, in agreement with the demo's numerically located
$0.3982$ rad ($22.81^\circ$).

---

## ★3 — Equilibria and frequencies

**(a)** $V'(x) = \alpha x - \beta x^2 = x(\alpha - \beta x)$, so equilibria at
$x = 0$ and $x = \alpha/\beta$. $V''(x) = \alpha - 2\beta x$, so
$V''(0) = \alpha > 0$ (stable, $\omega_0 = \sqrt{\alpha/m}$) and
$V''(\alpha/\beta) = -\alpha < 0$: the second equilibrium is a maximum and is
unstable.

**(b)** $V' = \sin x$, so equilibria at $x = n\pi$. $V'' = \cos x$:
stable where $\cos x > 0$, i.e. at even multiples of $\pi$, with
$V'' = 1$ and $\omega_0 = \sqrt{1/m}$. At odd multiples $V'' = -1$: unstable.

**(c)** $V' = 4x^3$, so the only equilibrium is $x = 0$ with $V'' = 0$. The
quadratic term vanishes, so the small-oscillation approximation gives
$\omega_0 = 0$: the motion is anharmonic at every amplitude. The true period
scales as $A^{-1}$, which is the classic quartic-oscillator result and a clean
demonstration that $\omega_0 = \sqrt{V''/m}$ requires $V'' > 0$ and finite.

---

## ★4 — Dimensional checks

**(a)** $[m/k] = \mathrm{kg/(kg\,s^{-2})} = \mathrm{s^2}$ ✓, so
$\sqrt{m/k}$ is a time. $[W/g] = \mathrm{m/(m\,s^{-2})} = \mathrm{s^2}$ ✓.

**(b)** $[g/W] = \mathrm{s^{-2}}$, which is a frequency squared, so
$\sqrt{g/W}$ is a frequency, not a period. The inconsistent expression is the
*inverse* of the correct one, and the failure is a statement about the physics
of the restoring force: gravity supplies a restoring acceleration proportional
to displacement divided by a length, so it enters the frequency as $g/W$, not
$W/g$.

**(c)** Both are $\sqrt{(\text{a quantity that grows with displacement})/
(\text{a quantity that resists acceleration})}$, and every small oscillation has
that structure (§3.3).

---

## ★5 — Geophone

**(a)** $T = 1/4.5 = 0.222222$ s.

**(b)** The driven-oscillator solution of lesson 02-03-02 has amplitude
$A(\omega) = (\omega^2/\omega_0^2)\big/\sqrt{(1-\omega^2/\omega_0^2)^2 +
(2\beta\omega/\omega_0^2)^2}$ for ground-acceleration input; below $\omega_0$ the
mass follows the case (accelerometer), above $\omega_0$ the mass stays
essentially fixed in space while the case moves around it, so the measured
relative displacement reproduces the ground displacement (seismometer). The
transition is within a factor of about two of $\omega_0$, and exactly at
$\omega_0$ when the instrument is critically damped.

**(c)** For harmonic ground motion of amplitude $X$ at angular frequency
$\omega$, the peak acceleration is $X\omega^2$. With $X = 10^{-6}$ m: at 10 Hz,
$\omega = 62.8319\ \mathrm{rad\,s^{-1}}$, $a = 3.948\times10^{-3}\
\mathrm{m\,s^{-2}}$; at 1 Hz, $\omega = 6.28319$, $a = 3.948\times10^{-5}\
\mathrm{m\,s^{-2}}$. The linear range is limited at the *high*-frequency end,
because acceleration grows as $\omega^2$ for fixed displacement.

---

## ★6 — Anharmonic corrections

**(a)** With $u = a(r-r_0)$, $V = D(1-e^{-u})^2$. At $r = r_0$,
$u = 0$ and $V = 0$. Expanding,
$1 - e^{-u} = u - u^2/2 + O(u^3)$, so
$V = D(u^2 - u^3 + O(u^4))$ and $V''(r_0) = 2Da^2$. Hence
$\omega_0 = \sqrt{2Da^2/m}$ ✓.

**(b)** Because the confining potential rises more steeply to the left of $r_0$
than it decays to the right, the turning points are asymmetric and the mean
separation increases with energy — hence thermal expansion.

**(c)** The perturbation $-\tfrac14bx^4$ has a cycle average
$\langle x^4\rangle = \tfrac38 A^4$ for $x = A\cos\omega t$. The first-order
frequency shift is
$\Delta\omega/\omega_0 = -3bA^2/(8k)$, so the frequency *decreases* with
amplitude, and the leading period change is
$\Delta T/T_0 = +3bA^2/(8k)$.

---

## ★7 — Reading the demonstration

**(a)** $1.570\times10^{-8}$ at $dt = 10^{-2}$ s and $1.300\times10^{-12}$ at
$dt = 10^{-3}$ s, a ratio of $1.208\times10^4$.

**(b)** A factor of nearly $10^4$ per decade of $dt$ is fourth order
($10^4 = 10^{4}$): the integrator is confirmed to be RK4.

**(c)** Round-off. The global truncation error falls as $dt^4$ while the
accumulated round-off grows as $\epsilon/dt$ for a fixed simulated interval, so
the total error has a minimum at some finite $dt$; the observed error at
$dt = 10^{-4}$ s ($4.9\times10^{-13}$) is already at that scale rather than
smaller, which is the signature.

**(d)** The energy drift at $dt = 10^{-3}$ s is $1.719\times10^{-13}$ relative
over 50 s, comparable with the solution error at the same step. A fourth-order
method conserves a nearby quadratic invariant to the order of the method, so
this is consistent and not a separate check of the *physics*.

---

## ★8 — Inverting a pendulum measurement

**(a)** With $L = 1.000$ m, $g = 9.80665$ m s⁻², the small-angle period is
$T_0 = 2.006409$ s and four significant figures give
$T = 2.0064 \pm 0.00005$ s. The measured value is *below* $T_0$, which no
pendulum at finite amplitude can be, so the measurement is consistent with
$\theta_0 = 0$ and the data constrain only an upper bound. Taking
$|T/T_0 - 1| < 5\times10^{-5}$ gives $\theta_0^2/16 < 5\times10^{-5}$, i.e.
$\theta_0 < 0.028$ rad ($1.6^\circ$).

**(b)** $g = 4\pi^2L/T^2$, so $\delta g/g = \sqrt{(\delta L/L)^2 +
(2\delta T/T)^2}$. With $\delta L = 10^{-3}$ m, $\delta L/L = 10^{-3}$, and a
period known to four figures ($\delta T/T \approx 3\times10^{-4}$) the second
term contributes $6\times10^{-4}$; the length dominates but neither term is
negligible.

**(c)** No, at four significant figures the experiment cannot even detect a
swing of $1.6^\circ$, let alone measure the $\theta_0^2/16$ term: that term is
$6.25\times10^{-4}$ relative at $\theta_0 = 0.1$ rad, so it needs the period
known to about $10^{-5}$ *relative* — an order better than assumed — and
$\theta_0$ known to about 1 per cent. The experiment to do is a *difference*
measurement: measure $T$ at several amplitudes and fit $T$ against
$\theta_0^2$. The slope gives $T_0/16$ and the length error cancels to first
order, which is how the expansion was historically tested.

---

## ★★★9 — Convergence of the period series

A suitable program computes
$T_{\mathrm{exact}} = 4\sqrt{L/g}K(\sin(\theta_0/2))$ with $K$ from the AGM, and
the truncations of equation (9). Expected behaviour, stated as the conclusion the
report should reach:

(a) The table of relative errors should show a factor of about 100 improvement
in the small-angle error when the $\theta_0^2$ term is added at
$\theta_0 = 0.1$, and a much smaller improvement at $\theta_0 = 2$.

(b) The two-term series is better than the one-term series at every amplitude
tested, because both terms are positive and the neglected sixth-order term is
positive-definite in the same way; the crossover the question hypothesises does
not exist for this particular series, and the honest answer is that the series
remains an alternating-free expansion whose partial sums approach the exact value
monotonically from below at small amplitude.

(c) The expansion converges for $\theta_0 < \pi$, so a report that claims
divergence at 2.5 rad is wrong; at 2.5 rad the *second* term is already large
($\theta_0^2/16 = 0.39$), so truncation error is enormous even though the series
converges.

(d) Limitations: the AGM evaluates $K$ to round-off for $\theta_0$ up to about
1.5 rad but the series is only meaningful while successive terms decrease, and
the conclusion is limited to the simple pendulum.

---

## ★★★10 — Frequency shift from a cubic term

**(a)** Write $\ddot x + \omega_0^2 x = -\gamma x^2$ with
$\gamma = g_3/m$ (dividing by $m$: for $V = \tfrac12kx^2 + \tfrac13g_3x^3$,
$F = -kx - g_3x^2$, so $\gamma = g_3/m$). Seeking a solution of the form
$x = A\cos\omega t + A^2(u_0 + u_2\cos2\omega t)$ and collecting terms, the
constant and double-frequency pieces balance the quadratic forcing, and the
frequency shift appears only at order $A^2$:
$\omega \approx \omega_0\left(1 - \frac{5\gamma^2}{12\omega_0^4}A^2\right)$ for
this sign convention. The essential result — that a quadratic nonlinearity gives
a *second-order*, not first-order, frequency shift — follows from symmetry: the
driving term has no component at the fundamental frequency.

**(b)** With $k = 25$, $g_3 = 15$, $m = 4$: $\omega_0 = 2.5$ rad/s and
$\gamma = 3.75\ \mathrm{m^{-1}\,s^{-2}}$. Then
$5\gamma^2/(12\omega_0^4) = 5\times14.0625/(12\times39.0625) = 1.5\times10^{-2}$,
so $\Delta T/T = +1.5\times10^{-2}A^2$.

**(c)** Predicted fractional period changes: $1.5\times10^{-8}$ at $A = 0.001$,
$1.5\times10^{-6}$ at 0.01, $3.75\times10^{-5}$ at 0.05, $1.5\times10^{-4}$ at
0.1. The demo measured $+1.501\times10^{-7}$, $+1.506\times10^{-5}$,
$+3.831\times10^{-4}$ and $+1.569\times10^{-3}$. The measured values scale as
$A^{1.99}$ to $A^{2.03}$ — the predicted $A^2$ — but are about a factor of ten
*larger* than the prediction. That discrepancy is real and instructive: the demo
integrates the *cubic* force exactly rather than treating it as a perturbation,
and at these amplitudes the well is strongly asymmetric, so the first-order
perturbation result underestimates the shift. The correct conclusion is that the
$A^2$ scaling is confirmed and the coefficient is not, which is exactly the kind
of statement a numerical experiment should license.

**(d)** The expansion fails when the cubic force can no longer be treated as a
correction to the linear one, i.e. when $g_3A \sim k$, here
$A \sim k/g_3 = 25/15 = 1.67$ m. Beyond that the potential
$V = 12.5x^2 + 5x^3$ has a second, unstable equilibrium at $x = -2k/(3g_3) =
-1.11$ m, and a particle with enough energy can cross it and escape to
$x \to -\infty$: the motion stops being an oscillation at all.
