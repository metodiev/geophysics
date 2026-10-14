# Solutions — 03-03-06 scipy.sparse: Storage Formats and Sparse Solvers

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked *measured* were produced by
> running a modified copy, and the modification is stated.

---

## ★1 — Counting non-zeros

**(a)** A tridiagonal matrix with Dirichlet ends (the boundary values are not
unknowns) has one diagonal entry per row and one off-diagonal entry for each
adjacent pair: $\text{nnz} = N + 2(N-1) = 3N - 2$. For $N = 100$: 298, as
tabulated.

**(b)** Values: $298 \times 8 = 2384$ bytes. Column indices:
$298 \times 4 = 1192$ bytes. Row pointer: $(N+1)\times4 = 404$ bytes. Total:
$2384 + 1192 + 404 = 3980$ bytes, exactly the tabulated value. Note that the
row pointer has $N+1$ entries even for a square matrix, because it stores the
end offset as well as each row's start.

**(c)** $\text{nnz} = 3\times10^6 - 2 \approx 3.0\times10^6$; bytes
$= 3.0\times10^6\times12 + 4\times10^6 = 4.0\times10^7$, i.e. about 40 MB.
The dense array is $8\times10^{12}$ bytes $= 8$ TB, so the ratio is
$8\times10^{12}/4.0\times10^7 = 2\times10^5$.

**(d)** Each node has 5 stencil entries except at the boundary: interior nodes
have 5, edge nodes have 4 and the four corners have 3. Counting:
$5N - 4n - 4$, since there are $4(n-2)$ edge nodes losing one entry each and 4
corners losing two each: $4N - (4n-8) - 4\times2 = 4N - 4n$.
So $\text{nnz} = 5N - 4n$ (the demo prints exactly this for $n = 40$: 7840).
Check at $n = 200$: $5\times40000 - 800 = 199200$, matching the demo.

---

## ★2 — The break-even fill fraction

**(a)** Sparse cost $\approx 12\,\text{nnz} + 4N = 12fN^2 + 4N$; dense cost
$8N^2$. Sparse wins while $12fN^2 < 8N^2$, i.e. $f < 8/12 = 2/3 = 0.667$.

**(b)** At $N = 10^4$: dense $= 8\times10^8$ bytes $= 800$ MB.

| fill $f$ | sparse bytes | ratio dense/sparse |
|---|---|---|
| 5% | $0.05\times10^8\times12 = 6.0\times10^7$ | 13.3 |
| 25% | $3.0\times10^8$ | 2.67 |
| 50% | $6.0\times10^8$ | 1.33 |
| 80% | $9.6\times10^8$ | 0.83 |

At 80% fill the sparse matrix needs **20% more** memory than the dense array.

**(c)** Dense storage is $8N^2 = 8\times4\times10^{10} = 3.2\times10^{11}$ bytes
$= 320$ GB; sparse breaks even at $12\,\text{nnz} = 3.2\times10^{11}$, i.e.
$\text{nnz} \approx 2.7\times10^{10}$ non-zeros — which is a fill fraction of
$2.7\times10^{10}/(4\times10^{10}) = 0.67$. The word for a square matrix with
that many non-zeros is "dense"; the matrix's *size* is not what determines
whether sparse storage helps.

**(d)** A `csr` matrix also carries `has_sorted_indices` (and
`has_canonical_format`) — small metadata that determines whether index-based
operations are valid without a preliminary sort. It matters for arithmetic and
for slicing: `A * B` assumes canonical format, and `A.tocsr()` on a matrix built
from unsorted `coo` input can produce duplicate entries unless `sum_duplicates()`
is called first. The practical consequence is that a matrix assembled from
index lists should be passed through `.tocsr()` (which canonicalises) before any
arithmetic.

---

## ★3 — Convergence order

**(a)** Second order: the error is $O(h^2)$, and refining $n$ by 2 refines $h$ by
2, so the error falls by 4.

**(b)** The observed ratios are 3.853, 3.920, 3.960 — approaching 4 from below
because the leading error term is $c_1h^2$ but the next term is $c_2h^4$ with
the opposite sign, so as $h$ falls the ratio rises towards 4. The asymptotic
regime is approached, not attained.

**(c)** $n = 400$: $2.036\times10^{-5}/4 = 5.09\times10^{-6}$. $n = 800$:
$1.27\times10^{-6}$. Both follow from the measured order, and both should be
checked by running the modified script — an extrapolation that is not verified
is a hypothesis.

**(d)** The residual would stay at the level of round-off (it is already
$1.3\times10^{-10}$ at $n = 200$ and is dominated by the condition number of
the matrix, which grows as $h^{-2}$, so it might rise slightly to of order
$10^{-9}$), while the error would fall by a factor of 4. The two are unrelated:
the residual measures how well the linear system was solved, the error measures
how far the *discretisation* is from the continuum problem.

---

## ★4 — Fill-in growth

**(a)** $\log(8.28/5.23)/\log(2) = 0.663$;
$\log(11.69/8.28)/\log 2 = 0.498$;
$\log(15.99/11.69)/\log 2 = 0.452$. The local exponent falls towards
$O(\log N)$-like growth rather than staying constant, so the growth is *not* a
power law over this range; measured as an overall fit from $n = 20$ to 160,
$\log(15.99/5.23)/\log 8 = 0.455$.

**(b)** $O(N\log N)/O(N) = c\log N$: from $n = 80$ ($N = 6400$) to $n = 160$
($N = 25600$) the factor $\log N$ rises from 8.76 to 10.15, a ratio of 1.159, so
the predicted fill factor is $11.69\times1.159 = 13.55$ against a measured
**15.99**. The nested-dissection bound is asymptotic; COLAMD is an approximate
minimum-degree ordering, not nested dissection, and its fill grows somewhat
faster than the bound.

**(c)** Fill-in is the creation of new non-zeros during Gaussian elimination.
Eliminating unknown $k$ replaces the equations of its neighbours with
combinations that couple *every* neighbour of $k$ to every other neighbour —
so a row/column whose pattern is a star becomes a clique. The matrix's pattern
determines how many cliques are created, and the ordering determines their
size.

**(d)** $10^{7.5} = 3.16\times10^7$ entries, each needing 8 bytes of value and 4
of index, so about $3.8\times10^8$ bytes $= 0.38$ GB — plus whatever triangular
factors are stored, and an in-core LU also needs the working array. The matrix
itself has $7\times10^6$ entries and is trivial by comparison. The reason to
solve iteratively is that the factor's $O(N^{4/3})$ growth means the *factor*,
not the matrix, exceeds memory at around $n \sim 200$, while a Krylov method
needs only a handful of vectors.

---

## ★5 — One factorisation, many solves

**(a)** `factorized` calls `splu` once and returns a closure that performs the
two triangular solves with the cached factors. `spsolve` on a single
right-hand side performs exactly the same two operations; the result is
therefore bit-identical, which verifies that the cached path is the same
computation and not a re-derived one. If the two differed even in the last bit,
the caching layer would be doing something different from what the user
believes.

**(b)** `spsolve`-per-step costs one factorisation ($O(N^{3/2})$ in 2-D) plus two
back-substitutions ($O(N\log N)$) per step: 5000 factorisations. The
`factorized` route costs one factorisation and 5000 back-substitutions. For a
grid where the factorisation dominates by a factor of 100 or more, the saving is
two orders of magnitude — the single largest algorithmic saving available in
implicit modelling.

**(c)** CG's iteration count scales as $\sqrt{\kappa(A)}$, and the 5-point
Laplacian's condition number scales as $h^{-2} = (n+1)^2$, so the count scales as
$n$. Measured: 103 (n = 50), 208 (n = 100), 416 (n = 200) — almost exactly
doubling per doubling, so about **830 iterations at $n = 400$**. The *sharp*
statement to make in a methods section is the measured linear scaling, not the
theoretical bound.

**(d)** Symmetry and positive definiteness. Check numerically with
`(abs(A - A.T)).nnz == 0` for symmetry and, for definiteness, attempt a
`scipy.sparse.linalg.splu`/`cholesky` factorisation (which fails on an
indefinite matrix) or verify that all eigenvalues of a small analogous problem
are positive. For an advection–diffusion operator, symmetry is lost and
`gmres`/`bicgstab` is the correct choice instead.

---

## ★6 — Three dimensions

**(a)** A node has 7 stencil entries (itself and six neighbours). Boundary nodes
have fewer: the 6 faces of the cube lose one entry each ($6n^2$ nodes), the 12
edges lose two each ($12n$ nodes), the 8 corners lose three each. So

$$\text{nnz} = 7N - 6n^2 - 12n - 8 \cdot 2 + \dots$$

Counting carefully: each node's count is $1 + \deg$, with $\deg$ the number of
in-grid neighbours. Summing $7N$ overcounts each missing neighbour link once,
and the number of missing links is the number of links between a boundary node
and a node outside the grid. For the $\pm x$ direction that is $2n^2$ links,
and likewise for $y$ and $z$: $6n^2$ in total. Hence
$\text{nnz} = 7N - 6n^2$ exactly.

**(b)** *Measured* with the Kronecker construction:

| $n$ | $N$ | measured nnz | $7N - 6n^2$ |
|---|---|---|---|
| 10 | 1000 | 6400 | 6400 |
| 20 | 8000 | 53600 | 53600 |
| 30 | 27000 | 183600 | 183600 |

**(c)** $\text{nnz}/N$ equals 6.4, 6.7 and 6.8 for the three 3-D grids, rising
towards the asymptotic 7 as $n$ grows (the boundary correction $6n^2$ falls
relative to $7n^3$). The 2-D value at $n = 30$ is
$(5\times900 - 120)/900 = 4.87$, rising towards 5. So the 3-D stencil costs 40%
more non-zeros per unknown, and — crucially — $N$ grows as $n^3$ for the same
resolution, which is why a 3-D implicit problem is so much larger.

**(d)** With $n = 100$, $N = 10^6$ and a constant of 10, the factor has
$10\times N^{4/3} = 10\times10^{8} = 10^9$ entries, i.e. about $1.2\times10^{10}$
bytes $= 12$ GB. The matrix has $7\times10^6$ entries, about 84 MB. The factor is
**140 times** the matrix, which is the quantitative statement of (★4d).

---

## ★7 — Preconditioning

**(a)** *Measured* on the $n = 100$ system: Jacobi-preconditioned CG converges in
**208 iterations**, exactly the same as unpreconditioned CG. The reason is that
the scaled five-point Laplacian has a *constant* diagonal
($4/h^2$ for every row), so $M = \mathrm{diag}(A)^{-1}$ is a scalar multiple of
the identity and changes nothing except the convergence criterion. It is a
scaling, not a preconditioner, for this problem; it only helps when the diagonal
varies (variable coefficients, non-uniform grids, multiple unknowns per node).

**(b)** *Measured* with `spilu(A, drop_tol=1e-4, fill_factor=10)` and the default
pivoting: CG **does not converge**, reaching a relative residual of 0.51 after
500 iterations against $7.5\times10^{-11}$ for the unpreconditioned run. The
cause is that SuperLU's default partial pivoting makes the incomplete factors
non-symmetric, and CG's convergence theory requires a symmetric
positive-definite preconditioner; a non-symmetric one can stall or diverge.
Setting `diag_pivot_thresh=0` with `options=dict(SymmetricMode=True)` reduces
the asymmetry but does not remove it in this configuration — *measured*
$\langle Mu, v\rangle = -0.04111$ against $\langle u, Mv\rangle = -0.04080$,
a 1% asymmetry that is enough to break the method.

**(c)** The preconditioner must be symmetric and positive definite. The two-line
check:

```python
u = rng.normal(size=A.shape[0]);  v = rng.normal(size=A.shape[0])
print(abs((M @ u) @ v - u @ (M @ v)), (u @ (M @ u)))     # asymmetry, positivity
```

Both numbers should be zero (to round-off) and positive respectively. For an
SPD matrix the right tool is an *incomplete Cholesky* factorisation; where only
`spilu` is available, use it with a symmetric mode and verify the check above
before trusting CG with it.

**(d)** *Measured* at $n = 100$ ($\text{nnz}(A) = 49\,600$):

| ordering | $\text{nnz}(L)+\text{nnz}(U)$ | ratio to $\text{nnz}(A)$ |
|---|---|---|
| `NATURAL` | 2 000 198 | 40.33 |
| `COLAMD` (default) | 645 750 | 13.02 |
| `MMD_AT_PLUS_A` | 371 346 | 7.49 |

The ordering alone changes the factor's memory by a factor of 5.4, and
`MMD_AT_PLUS_A` — which minimises degree on the pattern of $A^TA$, appropriate
for a structurally symmetric matrix — is 1.7 times better than the default here.
**The ordering is free performance, and it is worth measuring rather than
assuming.**
