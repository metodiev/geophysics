# Solutions — 03-13-02 Testing Numerical Code Against Analytic Solutions

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; derived values are shown with the arithmetic
> that produced them.

---

## ★1 — Orders and the asymptotic approach

**(a)** With $p = \log_2(e_{\text{coarse}}/e_{\text{fine}})$:

$$p(32) = \log_2\frac{2.876115\times10^{-4}}{7.647078\times10^{-5}} = 1.9111,
\qquad
p(128) = \log_2\frac{1.972041\times10^{-5}}{5.007489\times10^{-6}} = 1.9775 .$$

**(b)** The scheme is second order, $p = 2$. The mean of the last three observed
orders ($n = 64, 128, 256$ pairs) is *computed*: $1.9738$.

**(c)** The error has the form $e_h = C h^2 (1 + \alpha h^2 + \dots)$ with
$\alpha h^2 > 0$, so the observed order is $2 - \mathcal{O}(h^2)$ and approaches
2 from *below* as $h$ shrinks. An oscillation around 2 would indicate round-off
contamination — the observed order would then bounce randomly rather than rise
monotonically, and the lesson's Section 5 says the finest grid here is still
four orders above the round-off floor, which is why the sequence is clean.

---

## ★2 — The stability limit

**(a)** $\Delta t_{\max} = \tfrac12 \Delta x^2/\kappa
= 0.5 \times (0.005)^2 / 10^{-6} = 12.5$ s. *Measured* by the demo's guard:
the scheme raises for $n_t = 1000$ (which gives $\Delta t = 20$ s, $r = 0.8$)
and runs for $n_t = 1600$ ($\Delta t = 12.5$ s, $r = 0.5$ exactly at the bound).

**(b)** $n_t = t/\Delta t_{\max} = 2\times10^4/12.5 = 1600$ steps.

**(c)** Halving $\Delta x$ divides $\Delta t_{\max}$ by 4, so the student must
also quarter $\Delta t$ — a factor of 8 more work in one dimension, and
$2^{d+1}$ in $d$ dimensions. Keeping the old $\Delta t$ gives $r = 2.0$,
four times the stability bound, and the solution blows up rather than merely
losing accuracy. This is exactly why the guard test exists: the failure is
catastrophic and it appears as an overflow or a nonsense number, not as a
slightly wrong answer.

---

## ★3 — Verification, solution verification, validation

**(a)** **Code verification.** A closed form derived independently of the
implementation checks that the equations are being solved correctly.

**(b)** **Validation.** A thermocouple is a physical measurement; agreement
establishes that the *model* is adequate for this problem, which no amount of
code checking can.

**(c)** **Solution verification.** The estimate is of *this* solution's
discretisation error, not of the code's correctness; the code could be
second-order and still solving the wrong equation.

**(d)** **Code verification**, in the far field. The shell theorem is exact, so
the comparison isolates numerical error — with the caveat from the lesson's
Section 4 that the quadrature must be converged before the difference means
anything.

---

## ★4 — The two competing terms

**(a)** Predicted at $\Delta t = 1.25$ s:
$\lvert A\phi - \tfrac12 B \Delta t\rvert
= \lvert 4.0587\times10^{-6} - 1.2175\times10^{-6}\rvert
= 2.8412\times10^{-6}$. The measurement is $2.3322\times10^{-6}$. The ratio
measured/predicted is $0.82$, and it is $0.82$ at every step of the table
($4.6645/5.6813 = 0.821$, $6.6633/8.1130 = 0.821$, $1.3327/1.6237 = 0.821$),
which is the constant of the expansion being $0.82$ rather than 1. **The model
is right and its constant is absorbed**: the ratio is what you assert on, not
the absolute value of the prediction.

**(b)** Cancellation at $\Delta t^\ast = 2A\phi/B = 2\times4.0587\times10^{-6}
/1.948\times10^{-6} = 4.17$ s. The tabulated minimum is
$6.6633\times10^{-7}$ at $\Delta t = 5$ s, and $\Delta t = 2.5$ s is already
worse at $1.3327\times10^{-6}$, so the true minimum lies strictly between 2.5 s
and 5 s — which brackets 4.17 s.

**(c)** The rows $\Delta t = 5.0$ s ($6.6633\times10^{-7}$) and
$\Delta t = 2.5$ s ($1.3327\times10^{-6}$) refute it: halving the step made the
error **larger** by a factor 2. The next row continues the trend
($2.3322\times10^{-6}$ at 1.25 s). The assertion is false for this scheme on
this grid, and the demo encodes the refutation as a test.

---

## ★5 — Richardson extrapolation and consistency

**(a)** Successive pairs, $r = 2$:

$$p(8\to16) = 1.8255,\qquad p(64\to128) = 1.9775,\qquad p(128\to256) = 1.9887 .$$

**(b)** Non-successive pairs use $p = \log_2(e_1/e_2)/\log_2 r$:

$$p(8\to64) = \frac{\log_2(1.019379\times10^{-3}/1.972041\times10^{-5})}{3}
= \frac{5.6919}{3} = 1.8973,$$
$$p(64\to256) = \frac{\log_2(1.972041\times10^{-5}/1.261675\times10^{-6})}{2}
= \frac{3.9663}{2} = 1.9831 .$$

Both lie in the same range as the successive-pair values, which is the point:
the rate is a property of the scheme, so a fourfold or eightfold refinement
measures the same thing as a doubling, as long as the grids are all inside the
asymptotic range. The $1.8973$ from the coarsest pair is the least reliable value
because $n = 8$ is furthest from the asymptotic regime.

**(c)** Applying $\lvert p_{\text{first}} - p_{\text{last}}\rvert \le 0.1$:

| triple | $p_{\text{first}}$ | $p_{\text{last}}$ | difference | verdict |
|---|---|---|---|---|
| $16 \to 64 \to 256$ | 3.8664 | 3.9663 | 0.0999 | consistent |
| $8 \to 64 \to 256$ | 5.6919 | 3.9663 | 1.7256 | **inconsistent** |

(The raw $\log_2$ ratios are quotients over $r$, so the comparison is the same
after dividing by $\log_2 r$; the first triple passes by a hair and the second
fails badly.) A failure would have said that the two grids are not in the same
asymptotic regime, so the "order" you measured is an artefact of where you
happened to sample the error curve — and any value extrapolated from it is
unreliable. That is precisely why the check comes *before* the extrapolation, not
after.

---

## ★6 — Quadrature error versus physics

**(a)** It is measuring **quadrature discretisation error**, because the shell
theorem makes $GM/d^2$ exact for the exterior field of a spherically symmetric
body. Physical effects — deviation from sphericity, density heterogeneity, the
dipole moment of the mass distribution — are *not* represented in this model at
all, so no difference here can be physical.

**(b)** At $d = 1000$ m the two grids differ by a factor $2.667$ per axis and the
error ratio is $4.037\times10^{-5}/5.677\times10^{-6} = 7.11$, which is above
first order ($2.667$) and numerically equal to second order
($2.667^2 = 7.11$) for this pair. But a single pair does not establish an order:
across all five grids the ratio per *doubling* ranges from about 2.5 to 4, which
brackets first order ($2$) and stops well short of second ($4$) at the
coarsest steps. The demo reports the range rather than one number because the
effective smoothness of the integrand changes as the field point approaches the
surface, and a claimed order would be an artefact of which pair you quoted.

At $d = 110$ m the same two grids give
$2.860\times10^{-4}/4.002\times10^{-5} = 7.15$ — the same rate, an order of
magnitude higher error level.

**(c)** The argument is refuted twice over. **First**, the shell theorem is
exact, so the sphere's finite size cannot matter at any level in this model: the
$3.873\times10^{-5}$ difference at $d = 500$ m is entirely quadrature error, and
it *falls* as the mesh is refined — $3.434\times10^{-5}$ at the 1.30 M-point grid
and $4.826\times10^{-6}$ at 24.58 M points, measured. **Second**, an effect that
shrinks when you refine the discretisation is by definition not a physical
effect; a physical effect would be mesh-independent. Confusing the two is the
error this lesson's Section 4 documents as having been made and corrected.

---

## ★7 — A manufactured solution for variable advection–diffusion

**(a)** Choose

$$u(x,t) = e^{-t}\sin(\pi x), \qquad c(x) = c_0(1 + \beta x), \qquad
\kappa, \beta, c_0 \ \text{constants},$$

so that $u(0,t) = u(1,t) = 0$ for all $t$ and the initial condition is
$u(x,0) = \sin(\pi x)$. Substituting into
$u_t + c(x)u_x - \kappa u_{xx} = f$ gives

$$f(x,t) = e^{-t}\Big[-\sin(\pi x)
+ \pi c_0(1+\beta x)\cos(\pi x)
+ \kappa\pi^2\sin(\pi x)\Big].$$

The source term is analytic, so the discrete problem can be solved with $f$
evaluated at whatever point the stencil requires, and the exact solution is known
at every node at every time — which is what makes the convergence rate
measurable.

**(b)** The choice exercises the **variable advection** term, because
$c(x)u_x$ is nonzero and $c$ varies in $x$; a scheme that discretised
$c u_x$ as a constant $c_0 u_x$ would converge to the wrong solution and the rate
test would fail. It leaves **nonlinear terms and steep gradients nearly
untested**: $u$ is a single smooth harmonic and $e^{-t}$ is a slow decay, so
shock-capturing, limiters, and any term depending on $|\nabla u|$ are never
exercised. A manufactured solution tests the terms you put into it and no others;
that is a property to state, not to hide.

**(c)** Two refinements at least, ideally three, with everything else fixed, at
$h$, $h/2$, $h/4$, $h/8$; measure $p = \log_2(e_h/e_{h/2})$ for each pair; assert
that all three observed orders lie in $[1.9, 2.1]$ **and** that the errors fall
monotonically. The tolerance: assert on $p$, not on $e_h$, so no absolute
tolerance is needed at all — which is the second lesson of the convergence-test
design. If a residual assertion is wanted as a smoke test, its tolerance is the
measured $e$ at the finest grid times a margin of 10, and it must be above the
round-off floor of the stencil (which for a second-order method is around
$u^{2/3} \approx 3.7\times10^{-11}$).

---

## ★8 — Verifying a $b$-value

**(a)** Two steps, each with its own analytic or independent reference.

1. **Verify the estimator** against synthetic data with a known $b$: generate a
   catalogue from a Gutenberg–Richter law with $b = 1.0$ and confirm the
   estimator recovers it inside the standard error. This is exactly what
   `code/apis_demo.py` does, and the measured result is $b = 1.016$ with
   $\sigma_b = 0.087$ — the truth $1.0$ lies inside one standard error.
2. **Verify the catalogue ingestion** against the server's own reported total:
   the measured fetch in the APIs lesson returns 137 of 137 events, and a
   pagination bug would show up as a mismatch here before it reached the
   estimator.

**(b)** Refining the grid establishes **solution verification**: that the
numerical solution of whatever equations were programmed is grid-converged.
It does not establish that the equations are right, that the estimator is
unbiased, or that the catalogue is complete. A grid-converged answer to the wrong
problem is still wrong, and more refinements make it wronger-to-many-more-digits.
The honest claim is "converged", not "correct".

**(c)** The one measurement that could establish correctness is **an independent
determination of $b$ for the same volume and period** — a different catalogue, a
different magnitude type, or a different estimator (for example a
linear least-squares fit to the cumulative counts, or a Bayesian
Weibull-method estimate). Agreement within the stated uncertainties is evidence;
disagreement is a finding. No test suite can perform it, because a test suite
computes only from the code and its fixtures, and this requires data the code
does not contain. That is the boundary between verification and validation, and
it is why the two words exist.

---

## ★9 — Asserting a non-monotone refinement result

**(a)** Deleting the test loses the information that the behaviour was measured
and understood. A future reader who finds the errors rising as the step is
refined will either "fix" the code, "fix" the tolerance, or conclude the scheme is
broken. The test encodes the *explanation in executable form*: two refinements
help, the third does not, and the ratio at the third is 2.0 because the linear
term dominates there. It is documentation that cannot rot into a comment that no
longer matches the code.

**(b)** *Measured*: $\text{errs} = (4.6645\times10^{-6},\ 6.6633\times10^{-7},\
1.3327\times10^{-6})$, so $\text{errs}[2]/\text{errs}[1] = 1.3327/0.66633 =
2.0000$. The model predicts, from $A\phi - \tfrac12 B\Delta t$, the ratio
$1.6237\times10^{-6}/8.1130\times10^{-7} = 2.001$. Asserting with `rel=0.1`
gives a band of $[1.8, 2.2]$: narrow enough to fail if the ratio became 1.0
(the error flattening) or 4.0 (a first-order scheme), and wide enough to survive
the third significant figure moving under a different summation order.

**(c)** All three assertions are at risk in principle, but only the third has
margin to lose. `errs[1] < errs[0]` compares values differing by a factor 7, and
`errs[2] > errs[1]` compares values differing by a factor 2 — both are robust to
an eighth-digit perturbation. The ratio assertion compares against a band of
$\pm 10\%$, and the measured ratio is $2.0000$ against a model value of $2.001$,
so the margin is 10% against a perturbation of order $10^{-8}$ relative: safe by
six orders of magnitude. The correct response to a future failure would be to
re-measure, not to widen the band — but the measurement, not the intuition, is
what says the margin exists.
