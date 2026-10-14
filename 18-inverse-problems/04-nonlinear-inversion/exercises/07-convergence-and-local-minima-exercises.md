# Exercises — Convergence Diagnosis and Local-Minimum Traps

Refer to [the lesson](../07-convergence-and-local-minima.md). All models are SYNTHETIC.
Demo: `../code/convergence_diagnostics_demo.py`.

## ★ Foundational

**1.1** State the second-order condition that distinguishes a minimiser from a saddle and name the quantity that must be computed.

**1.2** For the measured eigenvalues $\lambda = (1.1953, 3.4180)$ at the global minimum, compute the displacement permitted along each eigendirection at a gradient tolerance of $10^{-3}$, in metres.

**1.3** Explain why a Gauss–Newton Hessian cannot be used to classify a saddle.

## ★★ Applied

**2.1** The demo's finite-difference check of the analytic gradient gave a worst discrepancy of 1.509e-10 at $h = 10^{-6}$. Predict the discrepancy at $h = 10^{-3}$ and at $h = 10^{-8}$, giving the two competing error terms.

**2.2** From the measured $H$ and $H^{-1}$, verify the product $H H^{-1} = I$ by hand to three decimals and check the correlation formula $\rho = C_{12}/\sqrt{C_{11}C_{22}}$.

**2.3** Compute the accepted volume ratio between $\text{tol} = 10^{-4}$ and $\text{tol} = 5\times10^{-2}$ from the measured counts and compare with the ratio of spreads.

## ★★★ Research-oriented

**3.1** Design a convergence report for a field inversion and state, for each field, what measurement produces it and what its failure mode is.

**3.2** The measured near-equivalent set at $\text{tol} = 0.05$ spans 0.29 km while the linearised 1-sigma widths are (0.55, 0.91) km. Reconcile the two numbers and say which is larger and why.

**3.3** Argue whether a saddle found by an optimiser is an error or a result, using the measured eigenvalues and the measured accepted-set table.
