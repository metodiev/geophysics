# Solutions — 03-02-05 Linear Algebra with numpy.linalg

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values attributed to a verified snippet were
> produced with the project interpreter (NumPy 2.5.4).

---

## ★1 — A well-conditioned 2×2

**(a)** $x = (4/2,\ 1/0.5)^{\top} = (2, 2)^{\top}$.

**(b)** $A$ is diagonal and symmetric, so its singular values are the absolute
values of its eigenvalues: $s_1 = 2$, $s_2 = 0.5$ and
$\mathrm{cond}_2(A) = 2 / 0.5 = 4$.

**(c)** With $b' = (4, 1.001)$ the solution is $(2, 2.002)$:
$\lVert \Delta x\rVert / \lVert x \rVert =
0.002 / \sqrt{8} = 7.07 \times 10^{-4}$, while
$\lVert \Delta b\rVert / \lVert b \rVert =
0.001 / \sqrt{17} = 2.43 \times 10^{-4}$. The amplification is $2.9$, below the
bound $\mathrm{cond}(A) = 4$ — as it must be, since the bound is worst-case over
all perturbation directions. The direction of the perturbation here (the second
component only) is not the worst case for this diagonal matrix, which would be a
perturbation along $x_2$ scaled by $1/0.5 = 2$ relative to the *data* component.

**(d)** $\log_{10} 4 = 0.6$ digits lost, so about 15 of the 16 digits of `float64`
remain. In single precision, about 6.4 digits remain.

---

## ★2 — Column scaling

**(a)** $\lVert \text{col}_1\rVert = \sqrt{50} = 7.07$;
$\lVert \text{col}_2\rVert = \sqrt{\sum x_i^2} = 4.103 \times 10^3$;
$\lVert \text{col}_3\rVert = \sqrt{\sum x_i^4} = 3.210 \times 10^6$ (both computed on
the interpreter). Largest to smallest: $4.54 \times 10^5$.

**(b)** The condition number is bounded below by the ratio of the largest column
norm to the smallest, so $\mathrm{cond}(A) \gtrsim 4.5 \times 10^5$; the measured
value is $\mathrm{cond}(A) = 1.31 \times 10^6$ and
$\mathrm{cond}(A^{\top}A) = 1.71 \times 10^{12}$. The mechanism is not only the
scaling but the *correlation*: a ramp and a parabola sampled on $[0, 1000]$ with a
non-negative mean are nearly linearly dependent, so normalising the columns would
lower the ratio bound but the near-dependence would remain.

**(c)**

```python
xc = (x - x.mean()) / np.abs(x - x.mean()).max()      # xc in [-1, 1]
A = np.column_stack([np.ones_like(xc), xc, xc ** 2])
```

**(d)** The **fitted curve is unaffected** — the model predicts the same values at
the same $x$. What changes is the **condition number** (and therefore the
numerical error) and the **meaning and covariance of the coefficients**: they now
refer to the rescaled variable and cannot be compared term by term with the
original ones.

---

## ★3 — One-liners

**(a)** Because `solve` performs a square LU factorisation and back-substitution;
an over-determined system has no exact solution and an under-determined one has
infinitely many, so there is nothing for it to return.

**(b)** The sum of squared residuals (an array of length 1 when the system is
over-determined, and an empty array when it is exactly determined).

**(c)** It is a product of the eigenvalues, so it underflows or overflows for
perfectly usable matrices, and a value near zero does not distinguish "nearly
singular" from "badly scaled" (the 12×12 Hilbert determinant is
$2.77 \times 10^{-78}$).

**(d)** That the matrix is symmetric; `eigh` reads only one triangle, so passing an
asymmetric matrix silently computes the eigen-decomposition of a different matrix.

---

## ★4 — Stability in single precision

**(a)** Stable: LU with partial pivoting has a backward-stable error bound.
**(b)** Less accurate: the explicitly formed inverse adds a full matrix of rounding
errors, so the effective error is larger; it is also slower.
**(c)** Stable and the safest of the four, but it is doing more work than the
problem needs when $A$ is square and non-singular.
**(d)** Stable *for this matrix* because it is diagonal, so the division is exact
in each component. It is not a general method — for a dense $A$ it is simply
wrong.

---

## ★5 — Reporting the demo

**(a)** `residual ||Ax - b||_inf    = 1.7763568394002505e-15`,
`det(A)                    = -3.0000000000000036`,
`cond(A)                   = 32.71284150099982`.

**(b)** `condition number of A                 = 1.1285e+07`,
`condition number of A (centred/scaled)= 3.6227e+00`,
`condition number of A^T A             = 1.2735e+14`.

**(c)**

```
route                                       m0              m1              m2
normal equations + solve             12.018186      -3.898e-04       1.896e-08
normal equations + inv               12.018186      -3.898e-04       1.896e-08
lstsq (QR / SVD)                     12.018186      -3.898e-04       1.896e-08
true (synthetic)                     12.000000      -4.000e-04       2.000e-08
```

**(d)** All three norms are `2.3369652324`, and the best possible value is
`2.128967`.

**(e)** `np.linalg.solve :    3.875 ms`, `np.linalg.inv   :   9.813 ms`,
`ratio inv/solve = 2.53x`.

**(f)** `n = 12: cond(H) = 1.6595e+16, 1/cond(H) = 6.026e-17` and
`computed solution error = 5.167e-01`.

---

## ★★6 — Weighted least squares

**(a)** Minimise $\sum_i \left(d_i - (Am)_i\right)^2 / \sigma_i^2$, which is the
solution of the **scaled** system $W\!Am = Wd$ where
$W = \mathrm{diag}(1/\sigma_i)$.

**(b)**

- **Row scaling** (cheap, $O(mn)$): multiply row $i$ of $A$ and $d$ by
  $1/\sigma_i$, then use `lstsq` or the normal equations on the scaled system.
- **Weight matrix** (expensive, $O(m^2 n)$): form
  $A^{\top}W^2A\,m = A^{\top}W^2 d$, which materialises an $m \times m$ diagonal (or
  dense) matrix and, if dense, squares the cost.

Row scaling is cheaper by a factor of order $m$ and is numerically preferable
because it does not square the weights.

**(c)** With $A = [[1,0],[1,1],[1,2],[1,3]]$, $d = [1.0, 2.1, 2.9, 4.2]$,
$\sigma = [0.1, 0.1, 1.0, 1.0]$:

- unweighted: $m = (0.99,\ 1.04)$
- weighted: $m = (1.00417761,\ 1.08815355)$

Both verified on the interpreter.

**(d)** The two low-$\sigma$ rows (1 and 2, with weights 10) dominate the weighted
fit, which therefore passes close to them: the intercept is pulled to 1.004 and the
slope to 1.088. The unweighted fit treats all four rows alike and is dragged by the
less precise rows 3 and 4. Weighting is a statement about which measurements the
inverse *believes*, and it must be justified from the data acquisition, not chosen
to make the residual look better.

---

## ★★7 — Rank deficiency

**(a)** `np.linalg.matrix_rank(B) = 1`; the singular values are
`[5.0, 1.8e-16]` — the second is zero to machine precision, not exactly zero, which
is why a threshold is always involved.

**(b)** `lstsq` returns `[0.4, 0.8]` with rank 1. Both columns are the same
direction in model space (the second is twice the first), so any $(\beta, 0)$ with
$\beta$ such that $\beta \cdot 1 + 0 \cdot 2 = \text{fit}$ would do; the
minimum-norm solution spreads the effect equally between the two columns in
proportion to their lengths, giving $(0.4, 0.8) = \frac{0.4}{1}(1, 2)$.

**(c)** $B^{\top}B$ is singular, so `solve` either raises
`LinAlgError: Singular matrix` or returns huge garbage values (of order
$1/\epsilon$) depending on rounding. Either way the answer is not usable: the
problem has no unique solution and the arithmetic cannot invent one.

**(d)** Either (i) **the model parameterisation is redundant** — two basis functions
that are linearly dependent, such as a constant plus a normalised constant, or a
dipole pair with zero separation; or (ii) **the data cannot distinguish two
parameters** — for example two adjacent cells of a gravity mesh whose kernels are
numerically identical at the station spacing. The remedies are, respectively, to
reparameterise so the basis is independent, and to regularise (damping, smoothing)
so that a particular solution is selected by the prior rather than by rounding.

---

## ★★★8 — Tikhonov regularisation

**(a)** The regularised system is $A^{\top}A + \alpha^2 I$. If
$A = USV^{\top}$ then $A^{\top}A = VS^2V^{\top}$ and
$A^{\top}A + \alpha^2 I = V(S^2 + \alpha^2 I)V^{\top}$, so its eigenvalues are
$s_i^2 + \alpha^2$ and its condition number is
$\sqrt{(s_1^2 + \alpha^2)/(s_n^2 + \alpha^2)}$.

**(b)** With $s_1 = 1$, $s_n = 10^{-9}$:

- $\alpha = 10^{-4}$: $\sqrt{(1 + 10^{-8})/(10^{-18} + 10^{-8})} = \sqrt{10^8} = 10^4$.
- $\alpha = 10^{-6}$: $\sqrt{(1 + 10^{-12})/(10^{-18} + 10^{-12})} = \sqrt{10^6} = 10^3$.

So the error bound improves as $\alpha$ grows; the price is bias.

**(c)** With $A$ as above, the resolution matrix is

$$R = A\left(A^{\top}A + \alpha^2 I\right)^{-1}A^{\top}
    = U\,\mathrm{diag}\!\left(\frac{s_i^2}{s_i^2 + \alpha^2}\right)U^{\top}.$$

When $\alpha = 0$, $R = UU^{\top} = I$ on the range of $A$: the model is fully
resolved but the noise is amplified by $1/s_n$. When $\alpha \to \infty$,
$R \to 0$: the data have no influence and the solution is the null (prior) model.
Between those extremes each singular direction is damped by
$s_i^2/(s_i^2 + \alpha^2)$, which is the trade-off in explicit form.

**(d)** Increasing $\alpha$ **reduces the model variance** and **increases the
model bias**; the resolution matrix $R$ moves from $I$ towards $0$ as it does so.

---

## ★★★9 — A tomographic inversion

**(a)** $A^{\top}A$ is $500 \times 500$: $250\,000$ values $= 2$ MB in `float64`.
The data vector is $5000$ values $= 40$ kB. The normal matrix is **50 times larger
than the entire data vector** — small, in this example, which is why the normal
equations are affordable here and not in a $10^5$-parameter problem.

**(b)** The singular values $s_1 \ge \cdots \ge s_n$ measure how strongly each
model direction is illuminated. Count the directions with
$s_i / s_1 > \tau$ for a threshold $\tau$; the conventional choices are
$\tau = n\,\epsilon_{\text{machine}}$ (the default in `lstsq`'s `rcond`) or a
physically motivated value such as $10^{-2}$ when a 1 per cent model perturbation is
below the resolution you care about. The count is the **effective number of
resolved parameters**, and it is a result to report, not a technical detail.

**(c)** $\mathrm{Cov}(m) = \sigma^2 (A^{\top}A)^{-1}$, whose diagonal entries are the
parameter variances. If $s_n \approx \epsilon_{\text{machine}}$, inverting
$A^{\top}A$ multiplies $\sigma^2$ by $1/s_n^2 \approx 10^{32}$: the computed
variances are meaningless *and* they overflow the range in which the linearisation
is valid. The fix is regularisation, which replaces
$(A^{\top}A)^{-1}$ with $(A^{\top}A + \alpha^2 I)^{-1}$ and thereby gives finite,
if biased, variances.

**(d)** At this size `lstsq` (LAPACK `gelsd`, an SVD of the $5000 \times 500$
matrix) is actually affordable, so the honest answer is that a dense solve is fine
*here*; the iterative solvers become necessary when $n$ reaches $10^4$–$10^5$,
where the $O(mn^2)$ factorisation and the $O(mn)$-per-iteration Krylov methods
differ by orders of magnitude in both time and memory. Both approaches can report
the same diagnostic: the **residual norm and the model norm as functions of the
number of iterations (or of $\alpha$)**, i.e. the L-curve, which is the practical
way to choose the damping without pretending to know the noise level exactly.
