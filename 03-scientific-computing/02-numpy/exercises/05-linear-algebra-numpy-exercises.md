# Exercises — 03-02-05 Linear Algebra with numpy.linalg

Attempt these **closed-book** before opening the
[solutions](./05-linear-algebra-numpy-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/linalg_demo.py`](../code/linalg_demo.py) require
you to run it and report its actual output:

```
.venv/bin/python 03-scientific-computing/02-numpy/code/linalg_demo.py
```

Each numerical answer must be accompanied by the **residual** or the **condition
number** that justifies trusting it.

---

## ★ Foundational

**★1.** For $A = \begin{pmatrix}2 & 0\\ 0 & 0.5\end{pmatrix}$ and
$b = (4, 1)^{\top}$:

(a) Solve $Ax = b$ by hand.
(b) Compute $\mathrm{cond}_2(A)$ from the singular values.
(c) Perturb $b$ to $b' = (4, 1.001)^{\top}$ and compute the relative change in
$x$; compare it with $\mathrm{cond}(A)$ times the relative change in $b$.
(d) State the number of decimal digits you trust in the solution of (a), from the
rule of thumb in the lesson.

---

**★2.** A design matrix has columns of very different scale:

```python
x = np.linspace(0.0, 1000.0, 50)
A = np.column_stack([np.ones_like(x), x, x ** 2])
```

(a) Compute the ratio of the largest to smallest column norm.
(b) Explain why `np.linalg.cond(A)` is large without computing it.
(c) Write the rescaling that maps the second column to $[-1, 1]$.
(d) State which quantity is unaffected by the rescaling and which one changes.

---

**★3.** Answer in one line each.

(a) Why does `np.linalg.solve(A, b)` require `A` to be square?
(b) What does `np.linalg.lstsq` return as its second value?
(c) Why is `np.linalg.det` a poor singularity test?
(d) What does `np.linalg.eigh` assume that `np.linalg.eig` does not?

---

**★4.** For the system in ★1, state whether each of the following is a stable way
to obtain `x` in single precision, and why:

(a) `np.linalg.solve(A, b)`
(b) `np.linalg.inv(A) @ b`
(c) `np.linalg.lstsq(A, b)`
(d) `x = b / np.diag(A)`

---

## ★★ Applied

**★★5.** Run the demo. Report, quoting its output:

(a) The residual, determinant and condition number of the 3×3 system.
(b) `cond(A)`, `cond(A)` after centring and scaling, and `cond(A^T A)`.
(c) The coefficient table for the three routes and the true values.
(d) The three residual norms and the "best possible residual".
(e) The `solve` and `inv` timings and the ratio.
(f) The 12×12 Hilbert condition number and the computed solution error.

---

**★★6.** A gravity survey has 60 observations with standard errors
$\sigma_i$ that differ by a factor of ten between two groups of stations.

(a) Write down the weighted least-squares objective and the modified system.
(b) Give the two ways to implement the weighting (row scaling and a weight
matrix) and state which is cheaper.
(c) Using the demo-style design matrix
`A = [[1,0],[1,1],[1,2],[1,3]]` and data `d = [1.0, 2.1, 2.9, 4.2]` with
$\sigma = [0.1, 0.1, 1.0, 1.0]$, compute the weighted and unweighted slope fits.
(d) Explain, using your two answers, what weighting does to the influence of each
observation.

---

**★★7.** A colleague builds a design matrix whose first column is all ones and
whose second column is a multiple of the first.

(a) State `np.linalg.matrix_rank` and the singular values for
`B = column_stack([ones(5), 2*ones(5)])`.
(b) State the `lstsq` solution for `d = [0,1,2,3,4]` and explain why it is the
*minimum-norm* solution.
(c) State what `np.linalg.solve(B.T @ B, B.T @ d)` returns instead, and why it is
not a usable answer.
(d) Give the two physical explanations for a rank-deficient geophysical design
matrix, and the remedy for each.

---

## ★★★ Research-oriented

**★★★8.** Tikhonov regularisation replaces $A^{\top}A$ with
$A^{\top}A + \alpha^2 I$.

(a) Show that the singular values of the regularised system are
$\sqrt{s_i^2 + \alpha^2}$ and hence that the condition number is
$\sqrt{(s_1^2 + \alpha^2)/(s_n^2 + \alpha^2)}$.
(b) Compute the condition number for $s_1 = 1$, $s_n = 10^{-9}$ and
$\alpha = 10^{-4}$, and for $\alpha = 10^{-6}$.
(c) Derive the resolution matrix $R = A(A^{\top}A + \alpha^2 I)^{-1}A^{\top}$ and
state its value when $\alpha = 0$ and when $\alpha \to \infty$.
(d) State the trade-off in one sentence, naming the two quantities that move in
opposite directions.

---

**★★★9.** A tomographic inversion has a design matrix with
$m = 5000$ observations and $n = 500$ model parameters.

(a) State the shape of $A^{\top}A$ and the ratio of its size to a single
`float64` array of the data.
(b) The SVD decomposition of $A$ has $n$ singular values; state how to use them to
count the number of parameters the data actually resolve, and what threshold you
would use.
(c) Write down the model covariance $\sigma^2 (A^{\top}A)^{-1}$ and explain why it
is unavailable when the smallest singular value is at the machine epsilon.
(d) State why an iterative solver (CGLS/LSQR) is used instead of `lstsq` at this
size, and name the one diagnostic that both approaches can report.
