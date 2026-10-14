# Solutions — 01-14-03 Constrained Optimisation and Lagrange Multipliers

> **Read this after attempting the exercises, not before.**
>
> All numbers were computed exactly (rational arithmetic) or verified with
> [`../code/constrained_demo.py`](../code/constrained_demo.py). The KKT
> calculations are small enough to check by hand.

---

## ★1 — Equality-constrained quadratic

**(a)** With $A = \operatorname{diag}(2,8)$, $b = (2,8)^{\mathsf{T}}$,
$C = [1\ 1]$, $d = 1$, the KKT system (3.1) is

$$\begin{bmatrix} 2 & 0 & 1\\ 0 & 8 & 1\\ 1 & 1 & 0\end{bmatrix}
\begin{bmatrix} m_1 \\ m_2 \\ \lambda \end{bmatrix}
= \begin{bmatrix} 2 \\ 8 \\ 1 \end{bmatrix}.$$

**(b)** Eliminating $\lambda$ from the first two rows,
$m_1 = (2-\lambda)/2$ and $m_2 = (8-\lambda)/8$; imposing $m_1 + m_2 = 1$ gives

$$\frac{2-\lambda}{2} + \frac{8-\lambda}{8} = 1
\;\Longrightarrow\; 4(2-\lambda) + (8-\lambda) = 8
\;\Longrightarrow\; 16 - 5\lambda = 8 ,$$

so $\lambda = 8/5 = 1.6$ and

$$m = (0.2,\ 0.8)^{\mathsf{T}},\qquad \lambda = 1.6 .$$

**(c)** The unconstrained minimiser solves $Am = b$, i.e.
$m = (1, 1)^{\mathsf{T}}$. Misfits:
$f_{\text{unc}} = \tfrac12(2 + 8) - (2 + 8) = -5$, and
$f_{\text{con}} = \tfrac12(2(0.04) + 8(0.64)) - (0.4 + 6.4) = 2.6 - 6.8 = -4.2$.
The misfit increase is $0.8$, and the constraint is active with $\lambda > 0$.

**Consistency check.** Stationarity:
$Am + C^{\mathsf{T}}\lambda = (0.4 + 1.6,\ 6.4 + 1.6) = (2, 8) = b$. ✓

---

## ★2 — KKT for a one-sided constraint

The problem is $\min f(m) = m^{2}$ subject to $g(m) = 1 - m \le 0$. The
conditions are

1. **Stationarity:** $2m + \mu\,\frac{dg}{dm} = 2m - \mu = 0$.
2. **Primal feasibility:** $m \ge 1$.
3. **Dual feasibility:** $\mu \ge 0$.
4. **Complementary slackness:** $\mu(1 - m) = 0$.

At $m^{*} = 1$: stationarity gives $\mu = 2m = 2 \ge 0$ ✓; feasibility
$1 \ge 1$ ✓; and $\mu(1-1) = 0$ ✓. All four hold, so $m^{*} = 1$ is a KKT point,
and since $f$ is convex and the feasible set convex it is the global minimiser.

**Contrast.** If the constraint were instead $m \le -3$ (inactive at the
unconstrained minimum $m = 0$), then $\mu = 0$ and $m^{*} = 0$; exact
complementarity holds in both cases, and the multiplier exactly distinguishes the
two situations.

---

## ★★3 — Verifying the multiplier as a derivative

With the constraint right-hand side $c$, the analysis of ★1 generalises:
$16 - 5\lambda = 8c$, so $\lambda(c) = (16 - 8c)/5$ and

$$m_1(c) = \frac{8c - 6}{10}, \qquad m_2(c) = \frac{3 + c}{5}.$$

Evaluating the constrained optimum:

| $c$ | $m_1$ | $m_2$ | $\lambda$ | $f^{*}$ |
|---|---|---|---|---|
| $0.99$ | $0.192$ | $0.798$ | $1.616$ | $-4.18392$ |
| $1.00$ | $0.200$ | $0.800$ | $1.600$ | $-4.20000$ |
| $1.01$ | $0.208$ | $0.802$ | $1.584$ | $-4.21592$ |

Central difference:

$$\frac{df^{*}}{dc} \approx \frac{-4.21592 - (-4.18392)}{0.02} = -1.6000,
\qquad -\lambda = -1.6000 .$$

Agreement to five decimal places with a step of $0.01$; the two agree exactly
because $f^{*}(c)$ is *linear* here — the constrained problem of ★1 is a
quadratic with one linear constraint, so the optimal value is an affine function
of $c$ and the central difference is exact. That is a useful special case to
recognise: a linear $f^{*}$ means the multiplier is constant, which is why
inversion codes can quote a single price for a small constraint relaxation.

---

## ★★4 — A box-constrained two-cell problem

**(a)** $G^{\mathsf{T}}G = \begin{bmatrix}2 & 2.02\\ 2.02 & 2.0404\end{bmatrix}$,
$\det = 4\times10^{-4}$, and $G^{\mathsf{T}}d = (0.07, 0.0704)^{\mathsf{T}}$.
The unconstrained normal-equation solution is

$$m_{\text{unc}} = (1.550000,\ -1.500000)\ \text{s/km},$$

with misfit $\approx 2.6\times10^{-28}$ (zero to round-off — the data were
generated from a model in the kernel's range). Both components lie far outside
$[0, 0.05]$, so the unconstrained model is physically meaningless.

**(b)** Solving the box problem (projected gradient, and an independent
$501\times501$ grid search, which agree) gives

$$m_{\text{box}} = (0.035,\ 0.000)\ \text{s/km}, \qquad \text{misfit} = 2.25\times10^{-4}.$$

Bound status: $m_2$ is **at its lower bound** $0$; $m_1$ is **free** at
$m_1 = 0.035$, inside the interval.

**(c)** The gradient at the solution is
$\nabla\phi = Gm - d$ multiplied by $G^{\mathsf{T}}$; in the normal-equation form
$g = Am - b$:

$$g = (2\times0.035 + 2.02\times0 - 0.07,\ 2.02\times0.035 + 2.0404\times0 - 0.0704)
= (0.000,\ 0.0003).$$

- For the free coordinate $m_1$: $g_1 = 0$ ✓ (stationarity).
- For the lower-bound-active coordinate $m_2$: $g_2 = +0.0003 \ge 0$ ✓ (dual
  feasibility; a positive gradient at a lower bound means the objective wants to
  decrease $m_2$ further, which the bound forbids).

All three verifiable KKT conditions hold (stationarity, dual feasibility,
complementarity with $g(m_2) = -m_2 = 0$).

**(d)** The unconstrained misfit is zero, so the cost of the bounds is the whole
of $2.25\times10^{-4}$. One bound is doing all the work: with $0.05$ bounds the
model was still physically absurd in $m_2$, and clamping it to zero raised the
misfit from $0$ to $2.25\times10^{-4}$. Note the shape of the answer: the bound
did not merely shrink $m_2$, it *re-optimised* $m_1$ from $1.55$ to $0.035$
(a 98 per cent change) — constraints redistribute the free parameters, which is
the behaviour that makes them useful and the reason a constrained solve cannot be
faked by clipping the unconstrained model.

---

## ★★5 — Penalty scaling

**(a)** Differentiating
$\phi_\mu(m) = \tfrac12\|Gm-d\|^{2} + \tfrac{\mu}{2}(m_1+m_2-c)^{2}$:

$$\left(A + \mu\,\mathbf{1}\mathbf{1}^{\mathsf{T}}\right)m
= G^{\mathsf{T}}d + \mu c\,\mathbf{1},$$

a symmetric positive definite system for every $\mu > 0$.

**(b)** At the solution, stationarity of $\phi_\mu$ implies
$G^{\mathsf{T}}(Gm-d) + \mu\,\mathbf{1}(m_1+m_2-c) = 0$, whose second term is
$O(\mu\times\text{violation})$. For this to balance a bounded first term the
violation must be $O(1/\mu)$. The companion script measures this: the violation
ratios for tenfold increases in $\mu$ are $5.5$ (pre-asymptotic), $9.182$,
$9.911$, $9.991$ and $9.999$ — so violation $\propto 1/\mu$ is the correct
scaling once $\mu$ is large enough.

**(c)** The penalty term multiplies the largest eigenvalue of the system by
roughly $\mu$, so $\kappa(A + \mu\mathbf{1}\mathbf{1}^{\mathsf{T}})$ grows
linearly in $\mu$ while the violation falls only linearly. Beyond some weight the
round-off in the solve costs more accuracy than the reduced violation gains, and
the practical remedy is an exact KKT solve or an augmented Lagrangian that
updates the multiplier rather than the weight.

---

## ★★6 — Why every enumerated pattern must be checked

The $27$ patterns partition the possible *active sets*, and the KKT point of a
pattern is a candidate only if it is feasible. A pattern that is infeasible, or
whose gradient signs violate complementarity, is not a solution of any
sub-problem — but the scan cannot know that without constructing the candidate
and testing it; the test *is* the construction. Discarding a pattern in advance
would require knowing which constraints are active, which is the answer being
sought.

**The experiment.** Take the three-cell box problem of the lesson and relax the
upper bound from $0.03$ to $0.05$, then $0.08$, then $0.20$ s/km, re-running the
27-pattern scan at each value.

**Expected observable.** While the bound is active, the best pattern places cell
1 at the bound (`u f f`) and exactly one KKT pattern is found. As the bound is
loosened past the value at which the unconstrained solution becomes feasible, the
active pattern becomes the all-free one — the KKT point count can rise above one
because the two patterns coincide at the transition (degeneracy), and then must
fall back to one once the bound is genuinely slack. The signal of the transition
is therefore:

- the active pattern changing from `u f f` to `f f f`;
- the dual variable of the bound row becoming exactly $0$ in the dual LP;
- the misfit becoming the unconstrained misfit.

Those three signals should coincide, and reporting all three is how a claim like
"the bound is now inactive" is made auditable. The number of KKT patterns alone
is not a reliable signal, precisely because of degeneracy at the transition.

---

## ★★7 — Positivity bounds and bias

**Setup.** Let the unconstrained estimate of a cell be $\hat m = 2\sigma$ with
$\sigma = 0.01$ (in the cell's units), so $\hat m = 0.02$ and the estimate is two
standard deviations from zero. Impose $m \ge 0$.

**What the bound removes.** Models with $m < 0$ are physically impossible for a
slowness perturbation, a density contrast or a conductivity; the bound removes
an unphysical part of the model space rather than a possible one.

**What the bound introduces.** If the true value is close to zero, the bound
truncates the estimator's distribution. With $\hat m = 2\sigma$, the true value
could be $0$ (the estimate is $+2\sigma$, a $2.3$ per cent tail event), in which
case the bounded estimate reports $m > 0$ and its nominal standard error
understates the error, because the estimator's sampling distribution has been cut
in half. The bias is of order $\sigma\phi(2)/\Phi(2) \approx 0.01\times
0.054/0.977 \approx 5.5\times10^{-4}$ in magnitude for this simple normal model —
small compared with $\sigma$ itself, but not negligible relative to a bound
that is *exactly* zero.

**Diagnostic to report.** Two numbers make the decision auditable:

1. the **multiplier** of the bound, $\mu = -\partial\phi/\partial m$ at the
   active bound, in misfit units per model unit — i.e. how hard the data are
   pushing against the bound;
2. the **misfit cost** of the bound, $f_{\text{bounded}} - f_{\text{unbounded}}$,
   which is zero to round-off if the unconstrained solution already satisfied the
   bound and positive otherwise.

Reporting both turns "we imposed positivity" from an assumption into a measured
statement, and lets a reader see whether the bound is binding because the data
demand it or because the parameterisation allowed a negative value that the
data merely tolerated. This is the constrained analogue of the rule that an
inversion must report the data fit as well as the model.
