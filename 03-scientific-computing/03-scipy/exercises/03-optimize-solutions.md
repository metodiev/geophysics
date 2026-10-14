# Solutions — 03-03-03 scipy.optimize: Root Finding, Minimisation and Curve Fitting

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked *measured* come from running a
> modified copy, with the modification stated.

---

## ★1 — Reading a `curve_fit` output

**(a)** $n - p = 25 - 3 = 22$ degrees of freedom.

**(b)** $\chi^2 = \chi^2_\nu \times 22 = 1.243904 \times 22 = 27.366$.

**(c)** Declaring $\sigma = 0.75$ K instead of 1.5 K halves the assumed
uncertainty, so every squared residual is four times larger:
$\chi^2_{\rm new} = 4 \times 27.366 = 109.46$ and
$\chi^2_\nu = 4.9756$. The fit is unchanged — the parameters and the residuals
are identical — so this is *not* evidence of a worse fit, it is evidence that
the stated $\sigma$ is now inconsistent with the residuals by a factor of
about 5 in $\chi^2$. The reduced $\chi^2$ tests the *pair* (model, error
model), not the model alone.

**(d)** The fitted $\tau$ lies 0.56 of its own standard error from the true
value — an entirely ordinary discrepancy for a single realisation, since 32% of
well-behaved fits would exceed it in absolute value.

---

## ★2 — `absolute_sigma` and its consequences

**(a)** $102.4480/91.8566 = 1.1153$.

**(b)** With `absolute_sigma=False`, `curve_fit` rescales the covariance so
that the reduced $\chi^2$ is exactly 1: the factor is
$\sqrt{\chi^2_\nu} = \sqrt{1.243904} = 1.1153$, which is exactly the ratio
measured in (a). Note the reported `reduced chi^2` is 1.243904 in *both* runs,
because the demo computes it from the supplied $\sigma$, not from the
covariance — the rescaling affects only the error bars.

**(c)** Quote the `absolute_sigma=True` bars, 1.0974 K and 91.86 yr. The
instrument's $\sigma$ is an external measurement; using it makes the error bars
a statement about the experiment. Using `False` sets the bars so the model
"fits" by construction and hides the 24% excess scatter of this realisation.

**(d)** If the noise doubled while $\sigma$ stayed at 1.5 K, the residuals would
double, so $\chi^2$ would rise by a factor of 4 to about 109 and
$\chi^2_\nu$ to 4.98, while the `absolute_sigma=True` error bars would stay
almost the same (they scale as $\sigma$, not as the residuals). That is the
diagnostic signature: a large reduced $\chi^2$ with small error bars means the
model or the error model is wrong, not that the parameters are well determined.

---

## ★3 — Bracketing an isotherm

**(a)** With $K_0 = 260$ GPa and $K_0' = 4$, and $f(V) = P(V) - 135$:

| $V/V_0$ | $P$ (GPa) | $f$ (GPa) |
|---|---|---|
| 0.5 | 727.30 | +592.30 |
| 1.0 | 0.00 | −135.00 |
| 1.5 | −47.00 | −182.00 |

$f(0.5) > 0$ and $f(1.0) < 0$, so $(0.5, 1.5)$ brackets a root; the sign change
is already within $(0.5, 1.0)$.

**(b)** If $f$ is continuous and $f(a)$ and $f(b)$ have opposite signs, then by
the intermediate value theorem a root exists in $(a,b)$ and Brent's method
cannot leave the interval, so it must converge to *a* root inside it — which is
what an open method cannot promise.

**(c)** Bisection halves the interval each step: from width 1.0 to $10^{-14}$ is
about $\log_2(10^{14}) = 46.5$ iterations. `brentq` used 11 — Brent's method
interpolates rather than halving, so it converges superlinearly once it is
close, while retaining the bracket guarantee.

**(d)** $|P(V_{\rm found}) - P_{\text{target}}| = 2.84\times10^{-14}$ GPa, i.e.
the *root equation's* residual at the returned point. It says the returned
$V/V_0$ is a root to machine precision; it says nothing about whether
the third-order Birch–Murnaghan form is the right equation of state for the
material.

---

## ★4 — Correlation and window length

**(a)** $\tau$ and the offset, with $r = -0.826$. The $A$–$\tau$ pair is nearly
degenerate at $r = -0.092$ *over this window*, which is the point of (b).

**(b)** $316.4/94.9 = 3.33$.

**(c)** Over a window of one time constant the exponential is approximated by
its first three Taylor terms:
$\Delta T \approx (A + c) - A\,t/\tau + A\,t^2/(2\tau^2)$. The data determine
three combinations — the constant, the linear coefficient and the quadratic
coefficient — and $A$ and $\tau$ enter only through the *ratios*
$-A/\tau$ and $A/(2\tau^2)$. The window determines the polynomial's
coefficients well but leaves the pair badly determined, which appears as
$|r| \to 1$ and a large $\sigma_\tau$.

**(d)** To reach 1% on $\tau$ the window must exceed several time constants and
the noise must be small. From the measured table in ★8(c), $\sigma_\tau/\tau$
falls from $0.105$ at 1 time constant to $0.032$ at 4; extrapolating the
measured trend, a window of 8–10 time constants with the same 25 samples and
1.5 K noise is needed for 1%. Extending the window is the only lever that
matters, because the information about $\tau$ lives in the ratio of the
curvature to the slope, which only becomes distinguishable when the curve has
bent appreciably.

---

## ★5 — What a Jacobian costs

**(a)** $1 + p$ residual-vector evaluations: one to evaluate the residual at
the base point and $p$ to perturb each parameter in turn.

**(b)** $35/5 = 7$ Jacobians. The arithmetic is
$n_{\rm vectors} = n_{\rm jac}(1+p)$ with $p = 4$.

**(c)** $2100/960 = 2.19$, not 5, because the analytic route also *uses* its
Jacobian: it evaluates the residual 8 times and the Jacobian 8 times, so its
total work is 16 units against the finite-difference route's 35. The saving
per Jacobian is a factor of 5; the saving overall is smaller because both
routes need Jacobians and both need residual evaluations, and only the
*Jacobian* cost is reduced.

**(d)** For $p = 12$ the per-Jacobian factor is $13$ against 1, so the ratio of
total work approaches $13$ times the ratio of the Jacobian counts — the
advantage scales as $1 + p$, so it grows linearly with the size of the model
and is independent of the number of data points. (The point-evaluation count
also grows with $n$, but it cancels in the ratio.)

---

## ★6 — Roots, and what a solver promises

**(a)** `fsolve` uses MINPACK's hybrid (Powell) method, which takes a Newton-like
step from the start point. From 2.5 the step is large enough to overshoot the
root at 2 and land in the basin of the root at 1, where the residual is
$1.78\times10^{-15}$. The trajectory is not monotone in the start point and
nothing in the returned result exposes it.

**(b)** Scan $f$ over the physically plausible range on a fine grid, detect every
sign change, and call `brentq` on each bracketing interval. The procedure is
*complete* over the scanned range: every sign change contains a root and
`brentq` will find one. Its guarantee is exactly the resolution of the scan — a
pair of roots closer together than the grid spacing can be missed, which is the
only failure mode.

**(c)** It raises `ValueError: f(a) and f(b) must have different signs`. That is
preferable because the request was ill-posed: with no sign change there is
either no root or an even number of roots in the interval, and returning 2.3
by minimising $|f|$ would silently answer a different question. A hard error
forces the caller to state what is being looked for.

**(d)** The residual proves only that a root of the *discrete* misfit equations
was found. It does not prove the root is unique (★6(a)), that it is the global
minimum (★7(c)), or that the model is identifiable — a residual of
$10^{-12}$ in a two-parameter model whose parameters are correlated at 0.99 is
perfectly consistent with one combination of them being well determined and
the other not determined at all.

---

## ★7 — Optimiser comparison

**(a)** Nelder-Mead maintains a simplex of $p+1$ points and moves it by
reflection, expansion and contraction using only function values; on a smooth
problem its convergence is linear at best, whereas BFGS builds a quasi-Newton
model of the curvature from successive gradients and converges superlinearly.
It is not an argument against Nelder-Mead because it needs no derivatives and
tolerates a non-smooth or noisy objective, where BFGS's gradient estimate is
meaningless — exactly the case a geophysical misfit often is.

**(b)** Either Powell stopped on its convergence test before reaching the
minimum, or it converged to a slightly different local minimum. The two are
distinguished by restarting: run Powell again from its own answer and, if the
RSS falls to $2.0179068433\times10^{2}$, it was premature termination; if it
stays at $2.0179070141\times10^{2}$, it is a different stationary point.

**(c)** It proves that the returned point satisfies the solver's stopping test
to the requested tolerances — the gradient and step criteria are met. It does
*not* prove global optimality: a local minimum with a small gradient looks
identical to a global one from the inside.

**(d)** Stage 1: explore with a derivative-free local method (Nelder-Mead or
Powell) from several starting points, or with `differential_evolution` for a
genuinely multimodal misfit, to locate candidate basins. Stage 2: refine inside
the best basin with `least_squares` or BFGS, pass an analytic Jacobian, and
report the covariance. Stage 1 answers "which minimum?", stage 2 answers "how
well determined is it?" — and the covariance from stage 2 is meaningful only if
stage 1 found the right basin.

---

## ★8 — The degeneracy, derived and measured

**(a)** For $t \in [0, W]$ with $W \ll \tau$,
$e^{-t/\tau} = 1 - t/\tau + t^2/(2\tau^2) + O(t^3/\tau^3)$, so

$$\Delta T(t) \approx \underbrace{(A + c)}_{c_0}
\underbrace{- \frac{A}{\tau}}_{c_1} t
+ \underbrace{\frac{A}{2\tau^2}}_{c_2} t^2 .$$

The least-squares fit determines $c_0$, $c_1$, $c_2$ well, since they are the
coefficients of a quadratic in $t$. The physical parameters follow as
$\tau = -c_1/(2c_2)$ and $A = -c_1\tau$: both depend on $c_1$ and $c_2$, which
are small (they scale as $1/\tau$ and $1/\tau^2$) and are estimated from the
*curvature* of a nearly straight line.

**(b)** As $W \to 0$ the quadratic term $c_2 t^2$ becomes unmeasurable compared
with the linear term, so $c_2$'s uncertainty grows relative to $c_1$'s and
$\tau = -c_1/(2c_2)$ inherits a relative error that grows without bound. The
correlation between $A$ and $\tau$ tends to $\pm1$, since a change in $c_2$
(taken up by $\tau$) can be compensated by a change in $c_1$ (taken up by
$A$). The fit remains *formally* determined — the Jacobian still has full
column rank — but the practical identifiability collapses.

**(c)** *Measured* with the demo's procedure (25 samples, 1.5 K noise, seed
`19980815 + int(t_hi)`):

| window | $\sigma_\tau$ (yr) | corr$(A,\tau)$ | local $p$ |
|---|---|---|---|
| 0.25 $\tau$ | 672.6 | +0.9935 | -- |
| 0.5 $\tau$ | 444.4 | +0.9847 | 0.60 |
| 1 $\tau$ | 316.4 | +0.9675 | 0.49 |
| 2 $\tau$ | 143.1 | +0.7074 | 1.14 |
| 4 $\tau$ | 94.9 | −0.0754 | 0.59 |

The local exponent $p$ is **not constant**: it is about 0.6 between adjacent
windows once the pair is degenerate (0.25–2 $\tau$), and it rises to 1.14
between 2 and 4 time constants, where the degeneracy breaks and the fit starts
to see the exponential's tail. Fitting the whole range gives $p \approx 0.71$.
A student who assumes a single power law will mis-predict the short-window
errors badly; this is why the exponent should be *measured*.

**(d)** Four times as many samples over the same window reduces
$\sigma_\tau$ by only $\sqrt4 = 2$, because the information about $\tau$ is
limited by the window's *geometry*, not by the number of points: 100 samples
over a quarter of a time constant still barely resolve the curvature. It helps,
but it is a factor of two, where lengthening the window by a factor of 4 gives
a factor of about 3.3 and eventually breaks the degeneracy.

---

## ★9 — A published time constant

**(a)** First: how long was the record compared with the reported time constant
(the exercise says 0.8 time constants — the record ends before the exponential
has bent much, so $\tau$ is determined mainly by curvature). Second: why
`absolute_sigma=False`, which rescales the covariance so that
$\chi^2_\nu = 1$ by construction and can only inflate or deflate the error bars
relative to the instrument's own uncertainty.

**(b)** $\sigma_A\sqrt{1-r^2} = \sigma_A\sqrt{1 - 0.994^2} = 0.1094\,\sigma_A$.
This is the *conditional* standard error of the amplitude: the uncertainty in
$A$ once $\tau$ is known. The marginal $\sigma_A$ is 9.1 times larger, because
without knowing $\tau$ the amplitude could be traded against it almost freely.
Quoting $\sigma_A$ without stating this distinction invites the reader to
believe the amplitude is determined to the conditional precision.

**(c)** Two sentences that should accompany it: "The record spans 0.8 time
constants, so the time constant is constrained mainly by the curvature of the
decay and is strongly correlated with the amplitude ($r = 0.994$). The
reported uncertainty is therefore dominated by this degeneracy and would be
reduced more by extending the record in time than by adding samples within the
existing window."

**(d)** One measurement at a time comparable with several time constants —
for a borehole experiment, a deeper temperature log, or a repeat measurement
several $\tau$ later. The reason is (★8): the information that breaks the
degeneracy is the exponential's tail, which is only reachable at
$t \gtrsim 2\tau$; no amount of additional sampling inside the existing window
substitutes for it.
