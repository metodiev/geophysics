# Exercises — 19-03-03 Assembly, Sparsity and Linear System Structure

Attempt these before reading the
[solutions](./03-fem-assembly-solutions.md). The lesson is
[03 Assembly, Sparsity and Linear System Structure](../03-fem-assembly.md). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A Q1 mesh has $n = 64$ cells per side of the unit square. State the
number of unknowns with homogeneous Dirichlet data on all four sides, and the
number of non-zeros using the measured nnz/row from the lesson. Compute the
storage in megabytes for a sparse matrix (8 bytes per entry for the value, and
count only values) and for a dense one, and give the ratio.

**★2.** State the measured relation between $\lambda_{\min}$ of the assembled
stiffness matrix and $h$. Use it to compute $\lambda_{\min}$ at $n = 32$ and
compare with the measured value.

**★3.** State the measured asymptotic value of $\lambda_{\max}$ and explain in
one sentence why it does not depend on the mesh.

## ★★ Applied

**★★4.** The measured condition number at $n = 64$ is $8.281\times10^{2}$. Using
the measured exponent, predict $\mathrm{cond}$ at $n = 256$, and predict the
factor by which unpreconditioned CG iterations grow.

**★★5.** The demonstration measures identical CG iteration counts (10, 22, 46, 93)
with and without Jacobi preconditioning on the uniform mesh. Prove from the
assembled matrix that diagonal preconditioning must be a no-op there, and state
the smallest change to the model that would make it useful.

**★★6.** At $n = 128$ the sparse matrix has $143641$ non-zeros. A colleague
stores it dense "to keep the code simple". Compute the memory in gigabytes and
the ratio, then state one further reason beyond memory why the dense choice
changes the algorithm rather than only its cost.

## ★★★ Research-oriented

**★★★7.** The pure-Neumann Laplacian on a closed domain is singular. Construct
the three-line repair used in the lesson, prove that adding
$\frac1N\mathbf{e}\mathbf{e}^{\mathsf{T}}$ removes the null space, and compute by
how much the smallest non-zero eigenvalue changes when $N = 289$.

**★★★8.** Design a numerical experiment that decides whether the CG iteration
growth in the lesson is governed by $\sqrt{\mathrm{cond}(K)}$ or by the mesh
spacing directly. State the two matrices you would compare, the metric, and what
each outcome would mean.
