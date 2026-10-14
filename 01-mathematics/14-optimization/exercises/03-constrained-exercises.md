# Exercises — 01-14-03 Constrained Optimisation and Lagrange Multipliers

Attempt these **closed-book**, on paper, before opening the
[solutions](./03-constrained-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Minimise $f(m) = \tfrac12(2m_1^{2} + 8m_2^{2}) - 2m_1 - 8m_2$ subject to
$m_1 + m_2 = 1$.

(a) Write the KKT system (3.1) of the lesson explicitly.
(b) Solve it for $m$ and $\lambda$.
(c) State the unconstrained minimiser and the misfit increase caused by the
constraint.

**★2.** State the four KKT conditions for $\min m^{2}$ subject to $m \ge 1$, and
verify all four at the solution.

---

## ★★ Applied

**★★3.** For the problem of ★1, verify $df^{*}/dc = -\lambda$ by re-solving with
$c = 1.01$ and $c = 0.99$ and taking a central difference.

**★★4.** A two-cell model has
$G = \begin{bmatrix}1&1\\1&1.02\end{bmatrix}$ and $d = (0.05, 0.02)$ s, with
bounds $0 \le m_i \le 0.05$ s/km.

(a) Compute the unconstrained solution and its misfit.
(b) Solve the box-constrained problem, stating which bounds are active.
(c) Verify the KKT sign conditions at the active bounds.
(d) State the cost of the bounds in misfit.

**★★5.** A penalty method is applied to the constraint $m_1 + m_2 = c$ with
weight $\mu$, so the objective becomes $\tfrac12\|Gm-d\|^{2} +
\tfrac{\mu}{2}(m_1+m_2-c)^{2}$.

(a) Derive the linear system that the penalty solution satisfies.
(b) Predict how the constraint violation scales with $\mu$.
(c) State one practical reason not to make $\mu$ arbitrarily large.

---

## ★★★ Research-oriented

**★★★6.** The companion script's Section 4 reports that exactly one of the
$27$ bound patterns satisfies feasibility and the KKT sign conditions. Explain
why enumerated patterns that fail the KKT test must nevertheless be *checked*
rather than discarded, and design an experiment that shows what happens to the
number of KKT patterns as a bound is loosened until it is inactive. State the
observable that signals the transition.

**★★★7.** A colleague imposes a positivity bound on a cell whose true value is
separated from zero by two standard deviations of the unconstrained estimate.
Discuss, with a numerical example of your own construction, the trade between
removing an unphysical model and biasing the estimate, and state what diagnostic
you would report to make the decision auditable.
