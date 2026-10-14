# Exercises — 03-03-06 scipy.sparse: Storage Formats and Sparse Solvers

Attempt these **closed-book** before opening the
[solutions](./06-sparse-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to
[`../code/sparse_demo.py`](../code/sparse_demo.py) require you to run it and
report its actual output:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/sparse_demo.py
```

Take a float64 value as 8 bytes, a `csr` column index as 4 bytes and the row
pointer as 4 bytes per row.

---

## ★ Foundational

**★1.** The demo reports the 1-D Laplacian:

```
          N       nnz     nnz/N^2   sparse bytes   dense bytes     ratio
        100       298   2.980e-02           3980         80000      20.1
       1000      2998   2.998e-03          39980       8000000     200.1
```

(a) Derive the formula for `nnz` of a tridiagonal matrix with Dirichlet ends.
(b) Verify the byte count for $N = 100$ from the per-element costs.
(c) Predict the byte count and the memory ratio at $N = 10^6$.
(d) Derive the formula for `nnz` of a five-point stencil on an $n \times n$ grid,
and verify it against the demo's $n = 200$ row (199200).

---

**★2.** The demo states that CSR needs more memory than a dense array above a
fill fraction of about two-thirds.

(a) Derive that break-even fill fraction from the per-element costs.
(b) Compute the memory ratio (dense/sparse) at fill fractions of 5%, 25%, 50%
and 80%, each for $N = 10^4$.
(c) A colleague says "the matrix is $200\,000 \times 200\,000$, so it must be
sparse". Construct the counterexample: how many non-zeros would make the sparse
storage worse than the dense array, and what word describes such a matrix?
(d) The demo counts only `data`, `indices` and `indptr`. State one further array
a `csr` matrix carries and one operation for which it matters.

---

**★3.** The Poisson convergence table is

```
         n  unknowns    solver   max |error|     L2 error  ratio to previous
        25       625   spsolve     1.218e-03    6.331e-04                 --
        50      2500   spsolve     3.160e-04    1.613e-04              3.853
       100     10000   spsolve     8.061e-05    4.072e-05              3.920
       200     40000   spsolve     2.036e-05    1.023e-05              3.960
```

(a) State the convergence order and derive what ratio it implies.
(b) Explain why the ratio approaches 4 from below rather than equalling it.
(c) Predict the maximum error at $n = 400$ and at $n = 800$.
(d) The same run reports `|A u - b|max = 1.302e-10`. State what would happen to
that number and to the error if the grid were refined to $n = 800$, and why the
two behave differently.

---

## ★★ Applied

**★4.** The fill-in table is

```
         n    nnz(A)  nnz(L)+nnz(U)  fill factor   nnz(A)/N^2
        20      1920          10048         5.23    1.200e-02
        40      7840          64902         8.28    3.063e-03
        80     31680         370282        11.69    7.734e-04
       160    127360        2036562        15.99    1.927e-04
```

(a) Compute $\log(\text{fill})/\log(n)$ between consecutive rows and state
whether the growth is a power law.
(b) The theory for nested dissection is $O(N\log N)$ entries in the factor
against $O(N)$ in the matrix. Compute the predicted fill factor for
$n = 160$ from the $n = 80$ value assuming that scaling, and compare with the
measured 15.99.
(c) Explain what fill-in is, in terms of elimination.
(d) A 3-D problem with $n = 100$ has $10^6$ unknowns and a factor with about
$10^{7.5}$ entries. Estimate the memory of the factor in GB and explain why
3-D implicit problems are solved iteratively.

---

**★5.** The demo reports

```
    factorized(a) solved two right-hand sides; the first is
    identical to spsolve(a, b1) to 0.000e+00.
    |A u1 - b1|max = 3.190e-11; |A u2 - b2|max = 3.101e-12
    Conjugate gradients on the same system converged in 208 iterations (info = 0)
```

(a) Explain why the first solution is bit-identical to `spsolve` and what that
verifies.
(b) A time-stepping code with 5000 steps solves the same system each step.
Compare the work of the `spsolve`-per-step route with the `factorized` route.
(c) The CG run needs 208 iterations. Estimate the number of iterations at
$n = 400$ and state the scaling law, with a reason.
(d) State one property a matrix must have for CG and how to check it.

---

## ★★★ Research-oriented

**★6.** Extend the sparse demo to three dimensions.

(a) Derive the non-zero count of the seven-point Laplacian on an
$n \times n \times n$ grid and show that it is $7N - 6n^2$ with $N = n^3$.
(b) Verify the formula numerically for $n = 10, 20, 30$.
(c) Compute the ratio `nnz/N` for each and compare with the 2-D value at
$n = 30$. Explain the difference.
(d) The direct factorisation of a 3-D seven-point Laplacian needs
$O(N^{4/3})$ entries. Compute the factor memory for $n = 100$ (assume the
constant is 10) and compare with the matrix itself.

---

**★7.** Preconditioning is not automatically an improvement. Investigate.

(a) Apply a Jacobi preconditioner ($M = \mathrm{diag}(A)^{-1}$) to the
$n = 100$ Poisson system and measure the iteration count. Explain the result in
terms of the matrix's diagonal.
(b) Build an `spilu` preconditioner with the default options and use it with
`cg`. Measure the outcome. Explain what property of the preconditioner is
responsible.
(c) State the property a preconditioner must have for CG, and write the
two-line numerical check that verifies it.
(d) State the ordering result: the demo's factor uses `permc_spec='COLAMD'`.
Measure the fill for `'NATURAL'`, `'COLAMD'` and `'MMD_AT_PLUS_A'` at
$n = 100$ and report the ratios to `nnz(A)`.
