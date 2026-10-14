# Solutions — 01-12-05 Direct vs Iterative Linear Solvers and Convergence

> **Read this after attempting the exercises, not before.**
>
> All arithmetic was computed. Operation counts are leading-order estimates, as
> stated in each case.

---

## ★1 — The tiny-pivot system

$$\begin{pmatrix}10^{-20}&1\\1&1\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}
= \begin{pmatrix}1\\2\end{pmatrix}, \qquad \text{exact } \mathbf x = (1,1).$$

**Without pivoting.** The multiplier is $m = 1/10^{-20} = 10^{20}$. Row 2 becomes

$$\left[1 - 10^{20}(10^{-20}),\ 1 - 10^{20}(1)\right] = [0,\ 1-10^{20}],$$

and the right-hand side becomes $2 - 10^{20}$. Then
$x_2 = (2-10^{20})/(1-10^{20}) = 1$ (to round-off), and

$$x_1 = \frac{b_1 - x_2}{10^{-20}} = \frac{1-1}{10^{-20}} = 0 .$$

The computed solution is $(0,1)$: the relative error in $x_1$ is
$\boxed{1.0}$ — total loss, with every significant digit destroyed. The
round-off in $b_1$ (of order $u = 2.2\times10^{-16}$) was amplified by
$1/10^{-20} = 10^{20}$, and $2.2\times10^{-16}\times10^{20} = 2.2\times10^{4}$ is
larger than $b_1$ itself.

**With partial pivoting.** The rows are interchanged so the pivot is 1, the
multiplier is $10^{-20}$, and the computed solution is $(1.0, 1.0)$ exactly.
The relative error is $\boxed{0}$.

**The rule.** The amplification factor at step $k$ is
$\max_{i\ge k}\lvert a_{ik}\rvert/\lvert a_{kk}\rvert$. Choosing the largest
available entry as pivot makes that ratio $\le1$ by construction. Pivoting is
therefore not a refinement — it is the difference between an answer and an
artefact, and it costs only a comparison and a possible row swap.

---

## ★2 — Thomas algorithm and its cost

For $a_ix_{i-1}+b_ix_i+c_ix_{i+1}=d_i$ with $a_0=c_{n-1}=0$:

**Forward sweep.** Set $c'_0 = c_0/b_0$, $d'_0 = d_0/b_0$, then for
$i = 1,\dots,n-1$

$$m_i = b_i - a_ic'_{i-1}, \qquad c'_i = \frac{c_i}{m_i}, \qquad
d'_i = \frac{d_i - a_id'_{i-1}}{m_i}.$$

**Back substitution.** $x_{n-1} = d'_{n-1}$ and for $i=n-2,\dots,0$,
$x_i = d'_i - c'_ix_{i+1}$.

**Operation count per row.** Forward: one multiply ($a_ic'_{i-1}$), one subtract,
one multiply-add for $d$, two divisions $= 1\,\text{mult}+1\,\text{div}+
1\,\text{mult}+1\,\text{sub}+2\,\text{div} \approx 5$ operations, of which 3
divisions. Back substitution: one multiply and one subtract. So roughly
$\boxed{8n}$ operations in total, against $\tfrac23n^3$ for dense elimination.

**Why the count matters.** The ratio is $\tfrac23n^3/(8n) = n^2/12$, which at
$n = 10^4$ is $8.3\times10^6$ — the dense route is eight million times more
expensive. The structure is not an optimisation; it is the difference between a
feasible solve and an impossible one.

---

## ★3 — Conditioning at $n=8$

Eigenvalues of $\text{tridiag}(-1,2,-1)$:

$$\lambda_k = 2 - 2\cos\frac{k\pi}{n+1},\qquad k=1,\dots,n .$$

At $n=8$, $h = 1/9$:

$$\lambda_{\min} = 2-2\cos\frac{\pi}{9} = 2-2(0.939693) = 0.120615,$$

$$\lambda_{\max} = 2-2\cos\frac{8\pi}{9} = 2-2(-0.939693) = 3.879385,$$

$$\kappa = \frac{3.879385}{0.120615} = \boxed{32.16}.$$

The asymptotic formula $4(n+1)^2/\pi^2 = 4(81)/9.8696 = 32.83$ agrees to 2%.
**Digits at risk:** $\log_{10}\kappa = 1.51$, or directly
$\kappa u = 32.16\times2.2\times10^{-16} = 7.1\times10^{-15}$. So about
**1.5 digits** may be lost, leaving roughly 14 good digits — this system is
perfectly safe in double precision, which is why it is a good teaching example and
a poor warning. The warning case is the *normal equations*, where $\kappa$ is
squared: at $n=8$ that gives $\kappa(A^{\mathsf T}A) = 1034$ and 3 digits at risk,
and at $n = 640$ it gives $2.8\times10^{10}$ with 10 digits at risk.

---

## ★4 — Sparsity of the five-point Laplacian

For an interior grid of $40\times40$, $N = 1600$ unknowns. Each unknown has 5
stencil entries, less the duplication at boundaries:

$$\text{nnz} = 5N - 4n = 8000 - 160 = \boxed{7840}, \qquad
\text{dense entries} = N^2 = 2.56\times10^{6},$$

$$\text{fraction nonzero} = \frac{7840}{2.56\times10^{6}} = \boxed{0.306\%}.$$

**Consequences.** Storing the matrix densely wastes memory by a factor of 327;
forming and factorising it densely costs $\tfrac23(1600)^3 = 2.7\times10^9$ flops
against a few $\times10^5$ for the sparsity-respecting alternatives. Note also the
$4n$ correction — it is the boundary rows, and getting it right matters when the
nonzero count is used as a cost model. In three dimensions the same reasoning
gives 7 nonzeros per unknown, and the *fill-in* during elimination becomes the
dominant concern, which is why 3-D problems are solved iteratively almost
universally.

---

## ★★5 — Deriving the Jacobi spectral radius

The Jacobi iteration matrix for $A = \text{tridiag}(-1,2,-1)$ is

$$M = I - D^{-1}A = \tfrac12\,\text{tridiag}(1,0,1),$$

i.e. $(M\mathbf v)_i = \tfrac12(v_{i-1}+v_{i+1})$ with zero boundary values.

**Eigenvectors.** Take $v_i = \sin\frac{ik\pi}{n+1}$ for $k=1,\dots,n$. Using the
identity

$$\sin\frac{(i-1)k\pi}{n+1} + \sin\frac{(i+1)k\pi}{n+1}
= 2\sin\frac{ik\pi}{n+1}\cos\frac{k\pi}{n+1},$$

we get

$$(M\mathbf v)_i = \tfrac12\left(v_{i-1}+v_{i+1}\right)
= \cos\frac{k\pi}{n+1}\,v_i,$$

with $v_0 = v_{n+1} = 0$ satisfied because $\sin0 = \sin k\pi = 0$. So the
eigenvalues of $M$ are $\cos\frac{k\pi}{n+1}$, and the spectral radius is the
largest absolute value:

$$\rho(M) = \cos\frac{\pi}{n+1} = \cos \pi h, \qquad h = \frac{1}{n+1}.$$

Since $\rho<1$ for every finite $n$, Jacobi converges for this matrix, at the rate

$$\rho = \cos\pi h \approx 1 - \frac{\pi^2h^2}{2}
\quad\Longrightarrow\quad
k \approx \frac{\ln(1/\text{tol})}{\pi^2h^2/2}
= \frac{2\ln(1/\text{tol})}{\pi^2}(n+1)^2 .$$

That is the $O(n^2)$ sweep count measured in the lesson. **Note what the
derivation did and did not use:** no norm, no diagonal dominance, only the
eigenvalues of a constant-coefficient difference operator. For a matrix that is
merely diagonally dominant the bound $\rho\le\|M\|_\infty<1$ is available but much
weaker; whenever the eigenvectors are known, use them.

---

## ★★6 — The 2-D case and a sweep prediction

For the five-point Laplacian the Jacobi iteration matrix acts as

$$(M\mathbf u)_{i,j} = \tfrac14\left(u_{i-1,j}+u_{i+1,j}+u_{i,j-1}+u_{i,j+1}\right),$$

and the eigenvectors separate: $u_{i,j} =
\sin\frac{ik\pi}{n+1}\sin\frac{jl\pi}{n+1}$ with eigenvalues

$$\mu_{k,l} = \tfrac14\left(2\cos\frac{k\pi}{n+1} + 2\cos\frac{l\pi}{n+1}\right)
= \tfrac12\left(\cos\frac{k\pi}{n+1}+\cos\frac{l\pi}{n+1}\right).$$

The maximum absolute value is attained at $k=l=1$ (both cosines positive and
largest), giving

$$\rho_{\text{2-D}} = \cos\frac{\pi}{n+1} = \cos\pi h,$$

**the same expression as in one dimension.** That coincidence is worth noticing:
the 2-D operator is a sum of two 1-D operators, and its Jacobi rate is the average
of their rates, which at the extreme mode equals the 1-D value.

At $n=64$, $h=1/65$ and $\rho = 0.9988322$. For a tolerance of $10^{-8}$:

$$k = \frac{\ln10^{-8}}{\ln 0.9988322} = \frac{-18.42}{-0.0011687}
= \boxed{1.58\times10^{4}\ \text{sweeps}},$$

each costing $O(N) = O(4096)$ flops. The point of the exercise is the scaling:
refining from $n=64$ to $n=128$ multiplies the sweep count by about 4, so the
total work grows like $n^4$ for Jacobi in two dimensions. That is the motivation
for SOR, Krylov methods, and ultimately multigrid.

---

## ★★7 — The optimal SOR factor

For a consistently ordered matrix (the five-point Laplacian on a rectangular grid
is one), the SOR iteration matrix has spectral radius

$$\rho_{\text{SOR}} = \omega-1 \quad\text{at the optimum}, \qquad
\omega_{\text{opt}} = \frac{2}{1+\sqrt{1-\rho_J^2}},$$

where $\rho_J$ is the Jacobi spectral radius. This is the standard Young formula;
its derivation proceeds from the *consistent ordering* property, which makes the
eigenvalues of the SOR iteration matrix satisfy a quadratic relation in those of
the Jacobi matrix.

Substituting $\rho_J = \cos\pi h$:

$$\omega_{\text{opt}} = \frac{2}{1+\sqrt{1-\cos^2\pi h}}
= \frac{2}{1+\sin\pi h}.$$

At $n=40$, $h = 1/41$:

$$\sin\frac{\pi}{41} = 0.076549, \qquad
\omega_{\text{opt}} = \frac{2}{1.076549} = \boxed{1.857788}, \qquad
\rho_{\text{SOR}} = 0.857788.$$

The lesson's measured sweep count at this $n$ is 153 against the prediction
$\ln(1/\text{tol})/\lvert\ln\rho\rvert = \ln(10^{10})/0.15347 = 150$.

**Two cautions.** (i) The formula requires consistent ordering; applying it to an
unstructured finite-element matrix is unjustified and can give $\omega$ above the
divergence threshold. (ii) The optimum is sharp: at
$\omega = 2/(1+\sin\pi h)$ the rate is $\omega-1$, but for $\omega$ significantly
above the optimum the iteration *diverges*, and just below it the rate degrades
rapidly. A practical code estimates $\rho_J$ by a few power iterations
(see [01-12-08](../08-matrix-eigen-solvers.md)) and then uses the formula.

---

## ★★8 — Cost of a tomographic solve

System: $10^{6}$ rays, $10^{4}$ cells, 200 nonzeros per row, so
$\text{nnz}(A) = 2\times10^{8}$.

**(a) Normal equations.** Forming $A^{\mathsf T}A$ costs, per row of $A$, about
$200^2 = 4\times10^{4}$ operations (all the outer products within the row), so

$$\text{form} = 10^{6}\times4\times10^{4} = 4\times10^{10}\ \text{flops},$$

and factorising the resulting dense $10^{4}\times10^{4}$ matrix costs

$$\text{factor} = \frac{(10^{4})^3}{3} = 3.3\times10^{11}\ \text{flops},
\qquad \text{total} \approx \boxed{3.7\times10^{11}\ \text{flops}}.$$

Memory is the harder constraint: $A^{\mathsf T}A$ is dense with $10^{8}$ entries,
and the factor fills in completely, so both need of order $8\times10^{2}$ MB in
double precision — before any pivoting workspace.

**(b) CG.** Each iteration needs one $A$ matvec and one $A^{\mathsf T}$ matvec,
i.e. $2\times2\times10^{8} = 4\times10^{8}$ flops, so 300 iterations cost

$$\boxed{1.2\times10^{11}\ \text{flops}},$$

with memory $O(\text{nnz}(A)) = O(2\times10^{8})$ words — but note that is
$\sim1.6$ GB, so in practice a matrix-free implementation recomputes the ray
lengths rather than storing them, and the *storage* is $O(N)$ rather than
$O(\text{nnz})$. That is the real advantage in production.

**The assumption that makes the comparison valid.** That
$\sqrt{\kappa(A^{\mathsf T}A)}$ iterations suffice, i.e. that CG converges in about
300 iterations at the stated tolerance. Since
$\kappa(A^{\mathsf T}A) = \kappa(A)^2$, a bound of 300 iterations implies
$\kappa(A)\lesssim 10^{3}$ — a well-posed, well-regularised tomographic system. If
$\kappa(A)$ were $10^{6}$, the CG count would be of order $10^{6}$ and route (b)
would be hopeless; the honest statement is that the comparison is conditional on
the conditioning, which is exactly the quantity a designer must estimate *before*
choosing the solver. In the flop count alone the two routes are within a factor of
three; the decisive advantages of CG are the memory and the avoidance of the
squared condition number.

---

## ★★★9 — CG with and without a Jacobi preconditioner

**Method.** Solve the 2-D Poisson system on a $32\times32$ interior grid
($N=1024$, unit right-hand side) with CG, then with the preconditioned system
$M^{-1}A\mathbf x = M^{-1}\mathbf b$ where $M = \text{diag}(A) = 4I$. Because the
diagonal is constant, the preconditioned system is $\tfrac14A\mathbf x =
\tfrac14\mathbf b$, whose spectrum is that of $A$ scaled by $\frac14$: the
*condition number is unchanged*, and the iteration count is identical. The
preconditioner helps only when the diagonal varies.

**That result is worth stating as the answer rather than a measured table.** A
constant diagonal preconditioner cannot change the condition number of this
problem, so reporting a large improvement would be a fabrication. The
demonstration's measured figures for unpreconditioned CG on this system are 59
sweeps at $n=32$ with a final relative residual of $8.3\times10^{-9}$, and 10, 28
and 44 sweeps at $n = 8, 16$ and $24$ — roughly $1.8n$ sweeps, i.e. growing like
$\sqrt\kappa\sim n$.

**How to make the exercise produce a real improvement.** Use a grid with
*variable* coefficients (a heterogeneous medium), where $\text{diag}(A)$ varies by
orders of magnitude across the grid. Then the Jacobi preconditioner removes the
diagonal scaling and the iteration count falls substantially — in typical diffusion
problems with conductivity contrasts of $10^{3}$–$10^{6}$ the reduction is a
factor of several. Alternatively use an incomplete-Cholesky or multigrid
preconditioner, where the reduction for a Poisson problem is the difference between
$O(n)$ and $O(1)$ sweeps.

**Why the explanation must be spectral.** Preconditioning replaces the spectrum of
$A$ with that of $M^{-1}A$. What matters for CG is not the size of the eigenvalues
but their *spread*: CG's rate depends on $\sqrt{\kappa(M^{-1}A)}$, and its
finite-termination property means it needs at most as many iterations as there are
distinct eigenvalues of the preconditioned operator. A good preconditioner either
clusters the spectrum (few distinct eigenvalues) or squeezes it into a short
interval — and, in the constant-diagonal case, does neither.

---

## ★★★10 — A small residual with an oscillatory model

**Why both observations are simultaneously possible.** The two are consistent
because the residual and the error are related by the condition number:

$$\frac{\|\hat{\mathbf x}-\mathbf x\|}{\|\mathbf x\|}
\lesssim \kappa\,\frac{\|\mathbf b-A\hat{\mathbf x}\|}{\|\mathbf b\|} .$$

The normal equations square the conditioning, so
$\kappa(A^{\mathsf T}A) = \kappa(A)^2$. For a typical gravity design matrix with
$\kappa(A)\sim10^{4}$–$10^{5}$, the normal equations have
$\kappa\sim10^{8}$–$10^{10}$, and a relative residual of $10^{-12}$ still permits a
relative model error of $10^{-12}\times10^{10} = 10^{-2}$ — one percent of the
model's *norm*, distributed in the directions with the smallest singular values.
Those directions are exactly the short-wavelength, oscillatory components, because
a gravity kernel is a smoothing operator: high-wavenumber model components produce
almost no data, so they are almost unconstrained. The residual is small because
the data are fit; the model oscillates because the fit is achieved with the
unconstrained components, which contribute nothing to $\|\mathbf b-A\mathbf x\|$.

**The resolution matrix view.** The solution of a damped least-squares problem is
$\hat{\mathbf x} = R\mathbf x_{\text{true}}$ with
$R = (A^{\mathsf T}A+\lambda^2I)^{-1}A^{\mathsf T}A$, whose eigenvalues
$\sigma_i^2/(\sigma_i^2+\lambda^2)$ measure how much of each singular direction is
resolved. With $\lambda=0$ the direction with $\sigma_i\approx0$ has
$R_{ii}\approx0$: the estimate in that direction is entirely the null-space
component of the noise and the round-off. A high-frequency oscillation in the
recovered model *is* that null-space component, and no amount of iteration or
residual reduction removes it.

**The two changes I would make.**

1. **Stop forming and solving the normal equations; use the SVD or a QR
   factorisation of $A$ directly.** Truncating or damping the singular spectrum is
   then explicit: $\hat{\mathbf x} = \sum_i
   \frac{\sigma_i}{\sigma_i^2+\lambda^2}\mathbf u_i^{\mathsf T}\mathbf b\,\mathbf v_i$.
   The model's norm and roughness become controllable, and the condition number
   never squares. This is the change that makes the oscillation go away, and it is
   a *modelling* decision about which directions to trust, not a numerical trick.
2. **Add an explicit model-space constraint — Tikhonov smoothness, a bound on
   model norm, or a covariance prior — rather than tuning the solver.** Choosing
   $\lambda$ (or a truncation index) by a discrepancy principle or L-curve makes
   the resolution an explicit, reportable property: the resolution matrix's
   diagonal tells you what the data constrain, and its oscillation-free structure
   tells you what they do not. Reporting the resolution is the difference between
   a model and a plausible picture.

A third change is worth mentioning but is secondary: solve with CGLS/LSQR on the
*undeformed* system, which also avoids the squaring and allows early termination
to act as regularisation (the "iterative regularisation" of Krylov methods). It is
cheaper than the SVD and gives much of the benefit, at the price of a stopping rule
that is harder to interpret than an explicit $\lambda$.

See [01-07-08](../../07-linear-algebra/08-svd.md) for the resolution and covariance
formulas and [18 Inverse Problems](../../../18-inverse-problems/README.md) for the
regularisation theory.
