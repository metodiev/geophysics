# Solutions — 01-12-06 Numerical ODE Solvers: Euler, Runge-Kutta, Implicit and Adaptive

> **Read this after attempting the exercises, not before.** All arithmetic below
> was computed; the values attributed to
> [`../code/ode_solvers.py`](../code/ode_solvers.py) are its actual output.

---

## ★1 — One Euler step vs the exact solution

**(a)** $y' = -3y$ has $y = 2\mathrm{e}^{-3t}$, so
$y(0.1) = 2\mathrm{e}^{-0.3} = 2\times0.740818 = \boxed{1.481636}$.

**(b)** One step: $y_1 = y_0 + h f(0,y_0) = 2 + 0.1(-6) = 1.4$, so the error is

$$y_1 - y(0.1) = 1.4 - 1.481636 = \boxed{-0.081636},$$

a relative error of $5.51$ per cent.

**(c)** With $y'' = 9y = 18$ at $t = 0$, the leading truncation term is
$\tfrac{h^{2}}{2}y'' = \tfrac{0.01}{2}\times18 = 0.09$. It agrees with (b) to one
figure and not more: it is a *local* term predicting one step's error, while
Euler's *global* error also accumulates the $O(h^{2})$ errors of every earlier
step in a slightly different way. The sign convention differs too — the exact
solution is convex there, so Euler undershoots, which is why the error is
negative and the truncated Taylor term is positive.

**(d)** Euler at $n$ steps has the multiplier $1 - 3h = 1 - 3/n$ per step, so
$y(1) = 2(1-3/n)^{n}$ at $t = 1$:

| $n$ | $h$ | Euler $y(1)$ | exact $y(1) = 2\mathrm{e}^{-3}$ | error |
|---|---|---|---|---|
| 10 | 0.1 | 0.0564950 | 0.0995741 | $-4.3079\times10^{-2}$ |
| 20 | 0.05 | 0.0775191 | 0.0995741 | $-2.2055\times10^{-2}$ |
| 40 | 0.025 | 0.0884503 | 0.0995741 | $-1.1124\times10^{-2}$ |

Successive error ratios are $4.3079/2.2055 = 1.953$ and
$2.2055/1.1124 = 1.983$, so the error falls like $h^{1.00}$: **order 1**, as the
local truncation analysis requires.

**(e)** $|1 + z| = |1 - 0.3| = 0.7 < 1$: stable, and comfortably so. Note that
stability here is a statement about $h\lambda$, not about accuracy — the run is
stable and wrong by 5 per cent.

---

## ★2 — Heun's stability function

**(a)** With $f(t,y) = \lambda y$, the predictor is
$\tilde y = y_n + h\lambda y_n = (1+z)y_n$ and Heun's update gives

$$y_{n+1} = y_n + \tfrac{h}{2}\left[\lambda y_n + \lambda(1+z)y_n\right]
= y_n\left[1 + \tfrac{z}{2} + \tfrac{z(1+z)}{2}\right]
= y_n\left(1 + z + \tfrac{z^{2}}{2}\right). \qquad\square$$

**(b)** $R(-2.5) = 1 - 2.5 + 3.125 = 1.625$;
$R(-2.2) = 1.220$; $R(-2.0) = 1.000$; $R(-1.9) = 0.905$; $R(0) = 1$.

**(c)** $|R(z)|\le1$ requires $z\in[-2,0]$, the same interval as forward Euler:
at $z = -2$ the value is exactly $1$ and immediately below it exceeds 1. Heun's
stability limit is $h \le 2/\lambda$, identical to Euler's.

**(d)** Because the stability interval is set by the *first* two terms of the
stability polynomial — $1 + z$ — and both methods share them. Order 2 buys
accuracy through the $z^{2}/2$ term without extending where the polynomial stays
inside the unit disc. The lesson's table shows the same asymmetry for RK4, whose
limit is only $2.78/\lambda$ despite being fourth order.

---

## ★3 — L-stability, and the one method that lacks it

**(a)**

| $z$ | backward Euler $1/(1-z)$ | trapezoidal $(1+z/2)/(1-z/2)$ |
|---|---|---|
| $-10$ | $0.090909$ | $-0.666667$ |
| $-100$ | $0.009901$ | $-0.960784$ |
| $-1000$ | $0.000999$ | $-0.996008$ |
| $-10^{6}$ | $9.99999\times10^{-7}$ | $-0.999996$ |

**(b)** Write $z = x + \mathrm{i}y$ with $x \le 0$. For backward Euler,

$$|R(z)| = \frac{1}{|1-z|} = \frac{1}{\sqrt{(1-x)^{2} + y^{2}}} \le 1
\quad\Longleftrightarrow\quad (1-x)^{2} + y^{2} \ge 1,$$

which holds because $x\le0$ makes the left side at least $1$. For the
trapezoidal rule, numerator and denominator have equal modulus when $x = 0$ and
the denominator is larger whenever $x<0$:

$$|R(z)| = \frac{\sqrt{(1+x/2)^{2} + (y/2)^{2}}}
{\sqrt{(1-x/2)^{2} + (y/2)^{2}}} \le 1
\quad\Longleftrightarrow\quad (1+x/2)^{2}\le(1-x/2)^{2}
\quad\Longleftrightarrow\quad x \le 0 . \qquad\square$$

**(c)** Backward Euler is **L-stable**: $R(z)\to0$ as $z\to-\infty$, so an
infinitely fast mode is annihilated in one step. The trapezoidal rule is
**A-stable but not L-stable**: $R(z)\to-1$, so the same mode is preserved in
magnitude and flips sign every step. That is precisely the ringing measured at
$h = 0.5$ in §3.3, where the second-order method
($7.253\times10^{-1}$) is 149 times worse than the first-order one
($4.863\times10^{-3}$); the ratio $7.253\times10^{-1}/4.863\times10^{-3} = 149$.

---

## ★4 — The explicit stability limit, and what happens at it

**(a)** $h \le 2/\lambda = 2/50 = 0.04$ s, so at least
$1/0.04 = \boxed{25}$ steps for $t\in[0,1]$.

**(b)** With $h = 0.04$, $\lambda h = 2$ and the multiplier is $1 - 2 = -1$:

$$y_1 = 1 + 0.04(-50)(1) = -1, \qquad
y_2 = -1 + 0.04(-50)(-1) = +1 .$$

The error of the first step is $|-1 - \mathrm{e}^{-2}| = 1 + 0.135335 =
\boxed{1.135335}$.

**(c)**

| $n$ | $h$ | $\lvert 1-\lambda h\rvert$ | max error on $[0,1]$ | verdict |
|---|---|---|---|---|
| 20 | 0.050000 | 1.500000 | $3.325\times10^{3}$ | unstable |
| 22 | 0.045455 | 1.272727 | $2.015\times10^{2}$ | unstable |
| 25 | 0.040000 | 1.000000 | $1.135$ | marginal |
| 26 | 0.038462 | 0.923077 | $1.069$ | stable |

**(d)** At $n = 25$ the multiplier is exactly $-1$: the solution alternates
between $+1$ and $-1$ forever instead of decaying to $\mathrm{e}^{-50t}$. It is
*bounded*, which is what stability means, and it contains no information about
the exact solution after the first step — the true solution at $t\ge0.1$ is below
$10^{-2}$. Marginal stability is not accuracy; the $n = 26$ row is barely better
($1.069$) because the multiplier is $0.923$, i.e. the error decays only 8 per
cent per step.

---

## ★★5 — The trapezoidal amplification factor and the ringing

**(a)** $y_{n+1} = y_n + \tfrac{h}{2}(\lambda y_n + \lambda y_{n+1})$ gives

$$y_{n+1}\left(1 - \tfrac{z}{2}\right) = y_n\left(1 + \tfrac{z}{2}\right)
\quad\Longrightarrow\quad R(z) = \frac{1 + z/2}{1 - z/2}. \qquad\square$$

**(b)** Part (b) of ★3 proves $|R|\le1$ for $\mathrm{Re}\,z\le0$. Dividing
numerator and denominator by $z$ and letting $z\to-\infty$,

$$\lim_{z\to-\infty} R(z) = \lim_{z\to-\infty}
\frac{1/z + 1/2}{1/z - 1/2} = \frac{1/2}{-1/2} = -1 .$$

**(c)** $R(-0.5) = 0.75/1.25 = 0.600$; $R(-2) = 0/2 = 0.000$;
$R(-10) = -4/6 = -0.666667$.

**(d)** The fast mode of the stiff problem decays like $\mathrm{e}^{-50t}$, so
after a few steps the physical solution is slowly varying. The trapezoidal rule
multiplies that mode by $R \approx -1$ per step instead of by $\approx0$, so it
survives as an alternating oscillation of *undiminished* magnitude; at $h = 0.5$
the lesson measures $7.253\times10^{-1}$ for the trapezoidal rule against
$4.863\times10^{-3}$ for backward Euler. The ringing is the stability function's
limit, not a coding error, and no amount of grid refinement of the *problem*
removes it — only a change of method (or a smaller $h$, which defeats the purpose
of using an implicit method).

---

## ★★6 — Adams–Bashforth 2: order, roots and the spurious mode

**(a)** Substitute a Taylor series for $y_{n-1}$:
$y_{n-1} = y_n - hy'_n + \tfrac{h^{2}}{2}y''_n + O(h^{3})$. With
$f_n = y'_n$ and $f_{n-1} = y'_n - hy''_n + O(h^{2})$,

$$y_n + \tfrac{h}{2}\left(3y'_n - y'_n + hy''_n\right) + O(h^{3})
= y_n + hy'_n + \tfrac{h^{2}}{2}y''_n + O(h^{3})
= y(t_{n+1}) + O(h^{3}),$$

so the local truncation error is $O(h^{3})$ and the method is order 2. $\square$

**(b)** With $f = \lambda y$ and $z = h\lambda$, dividing by $y_{n-1}$ and writing
$w$ for the shift operator gives

$$w^{2} - \left(1 + \tfrac{3z}{2}\right)w + \tfrac{z}{2} = 0, \qquad
w = \tfrac{1}{2}\left[\left(1 + \tfrac{3z}{2}\right)
\pm\sqrt{\left(1 + \tfrac{3z}{2}\right)^{2} - 2z}\right].$$

The principal root tends to $\mathrm{e}^{z}$ as $h\to0$; the second root is the
spurious computational mode, and it is the one that limits the step.

**(c)**

| $z$ | principal root $\lvert w_1\rvert$ | spurious root $\lvert w_2\rvert$ | verdict |
|---|---|---|---|
| $-0.5$ | 0.640388 | 0.390388 | stable |
| $-0.9$ | 0.518271 | 0.868271 | stable |
| $-1.0$ | 0.500000 | 1.000000 | marginal |
| $-1.1$ | 0.484707 | 1.134707 | unstable |
| $-1.5$ | 0.443000 | 1.693000 | unstable |

The modulus of the spurious root crosses 1 at $z = -1$, so the stability interval
is $[-1,0]$: $h \le 1/\lambda$.

**(d)** Heun's interval is $[-2,0]$, so AB2 is half as permissive *and* it carries
a mode the problem does not have. Practical consequence: for a stiff problem
($\lambda h \gg 1$) both are unusable, and for a mildly stiff one AB2 forces the
step to be half of what an explicit one-step method allows while the spurious
root must be damped at startup. A second-order one-step method is strictly
preferable here; multistep accuracy is bought with a step restriction.

---

## ★★7 — RK4 above its stability limit

**(a)** $z = h\lambda = 10^{-3}\times(-2\times10^{4}) = -20$, and

$$R(-20) = 1 - 20 + \frac{400}{2} - \frac{8000}{6} + \frac{160000}{24}
= 1 - 20 + 200 - 1333.333 + 6666.667 = \boxed{5514.333}.$$

**(b)** $|R| = 5514.33 > 1$: **unstable**, with round-off amplified by a factor
5514 per step, i.e. $3.7415$ decimal digits per step.

**(c)** Solving $|R(z)| = 1$ on the negative real axis by bisection gives
$z_{\min} = -2.7852935634$, so the largest stable step is
$h_{\max} = 2.7852936/2\times10^{4} = \boxed{1.3926468\times10^{-4}}$ s — the
reported step is $7.18$ times too large.

**(d)** The local truncation error at $h = 10^{-3}$ is $O(h^{5})$, of order
$10^{-15}$: it says nothing about stability, which is a property of $R$ at $z=-20$
and not of the truncation series. Over 1000 steps the amplification is
$5514.33^{1000} \approx 10^{3741}$, which exceeds the largest binary64 magnitude
($1.8\times10^{308}$) after $\log(1.8\times10^{308})/\log(5514.33) = 82.4$ steps:
the run reaches the floating-point ceiling in **83 steps** and then produces
infinities and NaNs. A stability limit is not advisory — it is a boundary between
a computation and an overflow.

---

## ★★8 — Why the adaptive estimator fails on a stiff problem

**(a)** Step doubling takes one step of size $h$ and two of size $h/2$ from the
same point, and forms $\left|y_{\text{two}} - y_{\text{one}}\right|/(2^{p+1}-1)$.
It assumes the local error is the smooth leading term $Ch^{p+1}$ of a
non-stiff Taylor expansion, so that the difference of the two approximations
estimates it.

**(b)** When $\lambda h \approx 1$ the error is dominated by the mismatch between
the method's stability polynomial $R(z)$ and $\mathrm{e}^{z}$, not by the $h^{5}$
term. The two competing contributions are (i) the Taylor truncation term the
estimator models, and (ii) the stability-function error, which is a function of
$z$ and does not scale as $h^{5}$. The estimator sees only (i) and therefore
underestimates the total.

**(c)** The model predicts that the error is controlled at the requested
tolerance, i.e. error $\propto \mathrm{tol}^{1}$ (slope 1). The measured slopes
were $0.49$ and $0.52$, and a measured exponent of $1/2$ means a *different* term
dominates: reducing the tolerance buys only the square root of the improvement,
so the controller is not in control of the quantity it is asked to control.

**(d)** The remedy is a stiffness-aware or implicit method (or a Rosenbrock /
implicit RK pair with an embedded stiff error estimate). A smaller safety factor
does not help because it does not change *which* term dominates: the same
underestimate recurs at every accepted step, and the lesson's uniform RK4 needed
128 steps for $10^{-6}$ to beat the adaptive controller outright on the same
problem.

---

## ★★★9 — A semi-implicit scheme for the damped oscillator

**(a)** Define $d = 1 + 2\zeta\omega_0h$. Solving the two updates for
$(x_{n+1}, v_{n+1})$ in terms of $(x_n, v_n)$:

$$v_{n+1} = \frac{v_n - h\omega_0^{2}x_n}{d}, \qquad
x_{n+1} = x_n + hv_{n+1} = x_n + \frac{h}{d}v_n - \frac{h^{2}\omega_0^{2}}{d}x_n,$$

so

$$A = \begin{pmatrix} 1 - \dfrac{h^{2}\omega_0^{2}}{d} & \dfrac{h}{d}\\[2mm]
-\dfrac{h\omega_0^{2}}{d} & \dfrac{1}{d}\end{pmatrix}, \qquad
\det A = \frac{1 - h^{2}\omega_0^{2}}{d}\cdot\frac1d
+ \frac{h^{2}\omega_0^{2}}{d^{2}} = \frac{1 + h^{2}\omega_0^{2}}{d}. \qquad\square$$

**(b)** The eigenvalues satisfy $\mu^{2} - (\operatorname{tr}A)\mu + \det A = 0$.
When the discriminant is negative the roots are a complex-conjugate pair of
modulus $\sqrt{\det A}$, so $|\mu|\le1 \iff \det A\le1$. Using (a):

$$\frac{1 + h^{2}\omega_0^{2}}{1 + 2\zeta\omega_0h}\le1
\quad\Longleftrightarrow\quad h^{2}\omega_0^{2}\le2\zeta\omega_0h
\quad\Longleftrightarrow\quad h \le \frac{2\zeta}{\omega_0}. \qquad\square$$

(The same condition follows for real roots, where the larger root is bounded by 1
exactly on this boundary; verified numerically for $h$ either side of the limit.)

**(c)** $\omega_0 = \sqrt{k/m} = 5$ rad s$^{-1}$,
$\zeta = c/(2\sqrt{km}) = 0.4/2 = 0.040000$. The limit is
$h \le 2(0.04)/5 = 0.016000$ s. The fully explicit scheme is limited only by
$h \le 2/\omega_0 = 0.4$ s — **25 times larger**. Verified directly from the
eigenvalues of $A$: $|\mu| = 0.9992477$ at $h = 0.01$, $|\mu| = 1.0009620$ at
$h = 0.0199$, $|\mu| = 1.0963225$ at $h = 0.1$.

**(d)** Integrating $x(0) = 1$, $v(0) = 0$ to $t = 2$ s, comparing with the exact

$$x(t) = \mathrm{e}^{-\zeta\omega_0t}\left[\cos\omega_dt +
\frac{\zeta\omega_0}{\omega_d}\sin\omega_dt\right], \qquad
\omega_d = \omega_0\sqrt{1-\zeta^{2}} = 4.9959984:$$

| $n$ | $h$ | computed $x(2)$ | error | ratio |
|---|---|---|---|---|
| 50 | 0.040 | $-0.5543740$ | $2.5391\times10^{-2}$ | — |
| 100 | 0.020 | $-0.5683285$ | $1.1436\times10^{-2}$ | 2.220 |
| 200 | 0.010 | $-0.5743203$ | $5.4444\times10^{-3}$ | 2.101 |
| 400 | 0.005 | $-0.5771064$ | $2.6583\times10^{-3}$ | 2.048 |
| 800 | 0.0025 | $-0.5784509$ | $1.3137\times10^{-3}$ | 2.024 |

The exact value is $x(2) = -0.5797647$. The ratios tend to 2, so the scheme is
**first order** — it splits the two terms of the equation and each half is
first-order accurate.

**(e)** The trade-off is the opposite of the hoped-for one. Treating the damping
implicitly adds no linear solve (the damping is linear, so the update is a
division) but it makes the scheme *less* permissive: the stability limit becomes
$2\zeta/\omega_0$, smaller than the explicit limit $2/\omega_0$ by the factor
$1/\zeta = 25$. That is the honest finding of the measurement: the stiff term in
this problem is the *restoring force*, not the damping, so making the damping
implicit removes no stiffness and introduces an imbalance that costs stability.
The variant that does help is the one that treats the restoring force implicitly
(the $\theta$-method or Newmark family), which restores the $2/\omega_0$ limit
with a solve per step.

---

## ★★★10 — Diagnosing a one-year explicit step

**(a)** One month is $30\times86400 = 2.592\times10^{6}$ s, so
$\lambda = 1/2.592\times10^{6} = 3.858025\times10^{-7}$ s$^{-1}$. The limit is
$h_{\max} = 2/\lambda = 5.184\times10^{6}$ s $= \boxed{2.0}$ months. The reported
step is one year $= 3.15576\times10^{7}$ s (Julian year), giving

$$\lambda h = 12.175, \qquad |1 - \lambda h| = 11.175 .$$

**(b)** The multiplier is $\boxed{11.175}$ per step: growth by
$11.175^{5} = 1.7428\times10^{5}$, $11.175^{20} = 9.2247\times10^{20}$, and
$11.175^{100} = 6.6796\times10^{104}$.

**(c)** The diagnostic plot shows an oscillation of alternating sign with a
magnitude that grows by an order of magnitude per step — the solution flips
between positive and negative temperatures (or pressures, or concentrations) and
takes absurd values within a few decades. A plausible-looking early value is not
evidence of stability: the first iterate is
$T_1 = T_0 + h(-k)(T_0 - T_s) = 12 - 12.175\times4 = -36.70$ °C, which is not a
physical temperature at all, and the "convergence" that a casual glance at a
later time might suggest is the sign alternation passing through zero.

**(d)** With $k = 1/(30\ \text{days})$, $T_s = 8$ °C, $T(0) = 12$ °C:

| method | step | $T$ after 1 yr | after 5 yr | after 20 yr | after 100 yr |
|---|---|---|---|---|---|
| explicit Euler | 1 yr | $-36.70$ | $-5.5742\times10^{3}$ | $3.6899\times10^{21}$ | $2.6719\times10^{105}$ |
| backward Euler | 1 yr | $8.0000206$ | $8.0000000$ | $8.0000000$ | $8.0000000$ |
| analytic | – | $8.0000206$ | $8.0000000$ | $8.0000000$ | $8.0000000$ |

The analytic value after one year is $8 + 4\mathrm{e}^{-12.175} =
8.0000206$ °C, and after 100 years ($40.58$ relaxation times)
$8 + 4\mathrm{e}^{-40.58} = 8.0000000$ °C to ten decimals. Backward Euler
reproduces both; explicit Euler is off by $-44.7$ °C at the first year and grows
without bound. Note that the *first* backward-Euler step is accurate to six
decimals even though $\lambda h = 12.175$: for a decaying problem, L-stability
means a large step is a legitimate *approximation* (the fast mode is exactly what
should be annihilated), whereas for explicit Euler the same large step is
*divergence*.

**(e)** In order of preference:

1. **Implicit time stepping** (backward Euler for a first-order relaxation, or
   Crank–Nicolson when second-order accuracy is needed). Cost: one linear solve
   per step — here a scalar division, so effectively free — and the step is chosen
   by accuracy rather than by stability. This is what production geothermal and
   palaeoclimate codes do.
2. **Reduce the step to at most two months** with the existing explicit scheme.
   Cost: six times as many steps, and the restriction recurs if the grid is
   refined, because the fastest relaxation time of a discretised diffusion problem
   shrinks as $\Delta x^{2}$.

A third option — sub-cycling only the fast part of the system — is a
semi-implicit split; it is the efficient middle ground when most of the physics is
slow, but it requires that the fast and slow parts be separable, which should be
demonstrated rather than assumed.
