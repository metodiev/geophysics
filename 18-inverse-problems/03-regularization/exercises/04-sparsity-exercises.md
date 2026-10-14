# Exercises — 18-03-04 L1 Regularisation, Sparsity and Compressive Sensing

Attempt these before reading the
[solutions](./04-sparsity-solutions.md). The lesson is
[04 L1 Regularisation, Sparsity and Compressive Sensing](../04-sparsity.md).
All models are **SYNTHETIC**. Reference values: $n = 128$ cells, $m = 64$
measurements, Gaussian design with $\|A^{\mathsf T}A\|_2 = 5.1616$,
$\alpha_{\max} = \|A^{\mathsf T}d\|_\infty = 2.6527$, and a true model with 4
spikes of amplitude in $[0.7,3.0]$.

## ★ Foundational

**★1.** Compute $\mathrm{soft}(1.4,0.6)$, $\mathrm{soft}(0.5,0.6)$ and
$\mathrm{soft}(-2.5,3.0)$. State which of the three corresponds to a Lasso
solution that is exactly zero.

**★2.** For a single-column Lasso with $a = 2$, $d = 3$, $\alpha = 0.4$, compute
the solution from the soft-threshold form and verify the optimality condition
$m_i \ne 0 \Rightarrow a(am-d) = -\alpha\,\mathrm{sign}(m)$.

**★3.** For $A = (2,1)^{\mathsf T}$ and $d = (3,1)^{\mathsf T}$ (one unknown, two
data), compute $\alpha_{\max}$ and state what the solution is for
$\alpha = 8$.

## ★★ Applied

**★★4.** The demonstration reports $\alpha_{\max} = 2.6527$ and uses
$\alpha = 0.05\,\alpha_{\max}$ for the phase-transition experiment. Compute
$\alpha$, then state the number of non-zeros found at
$\alpha/\alpha_{\max} = 0.5$ and $0.1$ from the measured table, and explain the
direction of the change in terms of what the penalty is doing.

**★★5.** With a known support, the demonstration verifies
$m_{\mathrm{hat},S} = m_{\mathrm{true},S}
- \alpha(A_S^{\mathsf T}A_S)^{-1}\mathrm{sign}(m_S)$ to about $10^{-15}$. For a
single isolated spike with $\|a_j\|_2 = 1$ and amplitude $2.5$, compute the
shrinkage at $\alpha = 0.05\alpha_{\max}$ and the recovered amplitude, and say
why the measured median ($0.9386$) is slightly lower.

**★★6.** Compute the coherence bound $k < \tfrac12(1+1/\mu)$ for the Gaussian
design ($\mu = 0.4928$) and for the line-mass kernel ($\mu = 0.9999$). Compare
each with the measured support-recovery rates and state what the comparison says
about the bound.

## ★★★ Research-oriented

**★★★7.** Derive the shrinkage of the $\ell_1$ estimator for two *correlated*
columns: $A_S^{\mathsf T}A_S = \begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}$ with
equal true amplitudes $c$, and show how the recovered amplitudes depend on
$\rho$. State what happens as $\rho\to1$ and connect the result to the coherence
failure measured in Section 6.

**★★★8.** Design an experiment that separates "the extra coefficients are
noise-fitting" from "the extra coefficients are a genuine feature of the
correlated design" for the $k = 16$ row of the over-selection table, and state
which measurement distinguishes them.
