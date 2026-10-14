# Exercises — Local Linearisation, Jacobians and Iteration

Refer to [the lesson](../01-local-linearization.md). All models are SYNTHETIC.
Demo: `../code/local_linearization_demo.py`.

## ★ Foundational

**1.1** For the one-parameter problem $d = e^{-a u}$ with $d = 0.6065$ and $u_0 = 1.0$, form the Jacobian entry $J = \partial d/\partial u$ and write the Gauss–Newton update $u_1$.

**1.2** Show that the linearisation error of $e^{-a(u+\delta)}$ after one Gauss–Newton step is second order in $\delta$ by expanding to three terms, and state what that implies for the measured convergence order.

**1.3** The demo reports the measured order of the exact-data iteration. Explain in two sentences why the order is 2 and not 1.

## ★★ Applied

**2.1** A two-parameter model has $J = \begin{pmatrix}1 & 1\\ 1 & 1.1\end{pmatrix}$ at the current iterate and residual $(0.2, -0.1)$. Compute the Gauss–Newton step $\Delta = -(J^{\mathsf T}J)^{-1}J^{\mathsf T}r$ by hand and check the sign convention.

**2.2** Build the same iteration in Python with a finite-difference Jacobian at step sizes $h = 10^{-3}, 10^{-5}, 10^{-7}, 10^{-9}$ for a synthetic forward operator of your choice, and report which $h$ minimises the Jacobian error. Compare with the value measured in the lesson.

**2.3** Explain why a finite-difference Jacobian costs $p+1$ forward evaluations and propose a scheme that costs fewer when the Jacobian is sparse, with the sparsity pattern you would need to know in advance.

## ★★★ Research-oriented

**3.1** The lesson measures a linearisation error whose order degrades as noise grows. Design an experiment that separates the truncation error from the noise-amplification error, and state the null hypothesis for each.

**3.2** Parameterise the same synthetic model two ways (for example depth and slowness versus depth and velocity) and measure the Gauss–Newton convergence for both. Report whether the iteration count changes while the converged model does not, and explain the result.

**3.3** Discuss whether a convergence order measured on synthetic data with a known forward operator can be quoted for a field dataset. Ground your answer in at least two measured numbers from the lesson.
