# Exercises — Conjugate Gradient and Large-Scale Inversion

Refer to [the lesson](../03-conjugate-gradient-inverse.md). All models are SYNTHETIC.
Demo: `../code/conjugate_gradient_inverse_demo.py`.

## ★ Foundational

**1.1** State the conjugacy condition for search directions and explain what property of the normal matrix it uses.

**1.2** For $K^{\mathsf T}K = \begin{pmatrix}3 & 3\\ 3 & 3.02\end{pmatrix}$, compute the eigenvalues and the condition numbers of $K$ and of $K^{\mathsf T}K$.

**1.3** Write the CG step length $\alpha_k$ and explain why the denominator must be positive for a PSD matrix.

## ★★ Applied

**2.1** Carry out the first CG step of the lesson by hand from $m_0 = (0,0)^{\mathsf T}$ with $b = (6.0, 6.02)^{\mathsf T}$ and verify $\beta_0 = 0.159616$.

**2.2** In the demo the ten smallest eigenvalues of the 800-column $K^{\mathsf T}K$ were all below $10^{-15}\lambda_{\max}$, with some negative. Explain the negative signs and why they do not indicate an indefinite matrix.

**2.3** From the semiconvergence table, compute the ratio of the model error at iteration 120 to the error at iteration 7 at 0.05% noise, and the same ratio for the residual. Comment on the difference.

## ★★★ Research-oriented

**3.1** The discrepancy-style stopping rule failed at 5% noise with a model error $1.126\times10^{8}$ against an oracle $5.66\times10^{-1}$. Design a stopping rule that cannot fail in that way, and state the false-stop risk it introduces.

**3.2** Prove or disprove by experiment: for CG applied to a consistent linear system with exact data, the model error decreases monotonically. Use the demo's exact-data configuration.

**3.3** Compare early stopping with Tikhonov regularisation at matched model error, and report which gives the smaller residual at that error, citing the lesson's numbers where they apply.
