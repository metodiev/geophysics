# Exercises — 08-05-03 EM Forward Modelling: Integral Equation, FD, FE Methods

Attempt these before reading the
[solutions](./03-em-modelling-solutions.md). The lesson is
[03 EM Forward Modelling](../03-em-modelling.md). All models are **SYNTHETIC**
teaching values with $\mu_0=4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ exact.

## ★ Foundational

**★1.** For $f=100\ \mathrm{Hz}$ and the three conductivities $0.01$, $0.002$ and
$0.05\ \mathrm{S\,m^{-1}}$, compute $k^2=i\omega\mu_0\sigma$ and then $u$ at
$\lambda=0.025\ \mathrm{m^{-1}}$. State the unit of $\lambda$, $u$ and $k$.

**★2.** Carry the admittance recursion one step: with $q_{j+1}$ known and a layer
of thickness $h_j$ and vertical wavenumber $u_j$, state $q_j$ and evaluate it for
$u_j=0.025+0.00016i\ \mathrm{m^{-1}}$, $q_{j+1}=0.025+0.00069i\ \mathrm{m^{-1}}$
and $h_j=60\ \mathrm{m}$.

**★3.** Convert the reflection coefficient
$R=-1.8086\times10^{-5}-2.7626\times10^{-3}i$ into the admittance $q$ at
$\lambda=0.025\ \mathrm{m^{-1}}$ and check that it reproduces the $q_1$ of the
lesson's worked example.

## ★★ Applied

**★4.** Prove that the recursion gives $q_j=u_j$ whenever
$q_{j+1}=u_j$, for any thickness $h_j$. Why does this test catch a
$u_j\leftrightarrow q_{j+1}$ transposition that the homogeneous-halfspace test
would miss?

**★5.** Derive the element stiffness and mass matrices for linear finite elements
on a uniform mesh, state the assembled interior equation, and show that the
resulting matrix is tridiagonal.

**★6.** The lesson's FD and FEM solutions have $L_2$ errors of
$9.181\times10^{-4}$ at 32 cells and $2.296\times10^{-4}$ at 64 cells. Compute
the convergence ratio, state the order it implies, and say what you would do if
the next refinement failed to continue the trend.

## ★★★ Research-oriented

**★7.** Design a resolution check for a three-dimensional finite-element EM model
that would detect a mesh which is too coarse in one direction only. State the
quantity you will monitor, the refinement you will perform, and the pattern of
results that would indicate a single-direction failure rather than a global one.

**★8.** The lesson measures a Born (linearised) error of about $3\%$ at a
conductivity contrast of $5$ for a $20\ \mathrm{m}$ layer at $50\ \mathrm{m}$
depth, and $6\%$ at a contrast of $20$. Outline the experiment you would run to
produce the equivalent curve for a target whose conductance is ten times larger,
and predict whether its linear regime will be wider or narrower, with a reason
that does not depend on the numbers in the lesson.
