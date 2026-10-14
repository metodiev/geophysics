# Exercises — 18-02-02 Underdetermined Problems and Minimum-Norm Solutions

Attempt these before reading the
[solutions](./02-underdetermined-solutions.md). The lesson is
[02 Underdetermined Problems](../02-underdetermined.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A system has $N = 3$, $M = 8$ and rank $3$. State the dimension of the
feasible set and write the general solution.

**★2.** Derive $\hat{\mathbf{m}} = G^{\!\top}(GG^{\!\top})^{-1}\mathbf{d}$ using a
Lagrange multiplier, and state why the result contains no null-space component.

**★3.** For the demonstration's three rays, compute
$GG^{\!\top}$ and its determinant, and state why it is invertible.

## ★★ Applied

**★★4.** The demonstration reports $\lVert\mathbf{m}\rVert = 0.605434$ at
$\lVert\mathbf{w}\rVert = 0$ and $0.637613$ at $\lVert\mathbf{w}\rVert = 0.2$.
Verify both with $\lVert\mathbf{m}\rVert^{2} = \lVert\hat{\mathbf{m}}\rVert^{2}
+\lVert\mathbf{w}\rVert^{2}$.

**★★5.** Two feasible models differ by $0.31\ \mathrm{s\,km^{-1}}$ in cell 0 but
have identical data. (a) State the maximum data discrepancy allowed by the
arithmetic. (b) Explain why reporting the minimum-norm model without qualification
misrepresents the experiment.

**★★6.** Of the three selection rules in the lesson, the $L_{1}$ solution has
$\lVert\mathbf{m}\rVert_2 = 1.1786$ against $0.6054$ for the minimum-norm solution,
but only 3 non-zero cells against 8. (a) Explain the apparent paradox.
(b) Which rule would you use for a compartmentalised ore body, and what must you
state with the result?

## ★★★ Research-oriented

**★★★7.** Design an experiment that determines all eight cells of the
demonstration's model with a feasible interval narrower than $0.1\
\mathrm{s\,km^{-1}}$ per cell, using rays of your choosing. State the ray
geometry, the predicted rank, and the LP you would solve to verify the claim.

**★★★8.** Generalise the minimum-norm rule to a **weighted** norm
$\lVert\mathbf{m}\rVert_{W}^{2} = \mathbf{m}^{\!\top}W\mathbf{m}$ with $W$ the
inverse of a model covariance $C_m$. Derive the estimator, explain what the weights
express physically, and state how it relates to the Bayesian posterior mean under a
Gaussian prior.
