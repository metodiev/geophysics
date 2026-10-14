# Exercises — 19-02-06 FD for Diffusion, Laplace and Poisson Problems

Attempt these before reading the
[solutions](./06-fd-diffusion-and-potential-solutions.md). The lesson is
[06 Diffusion and Potential](../06-fd-diffusion-and-potential.md). All models
are **SYNTHETIC**. Numbers printed by
`../code/fd_diffusion_and_potential_demo.py` may be quoted directly.

## ★ Foundational

**★1.** Write the five-point Laplacian and its truncation error in terms of
$u_{xxxx}$ and $u_{yyyy}$.

**★2.** State the condition number scaling of the discrete Laplacian with $h$
and explain what it implies for the number of iterations of a Krylov solver.

**★3.** For the unit square with Dirichlet zeros, state the decay law of the
fundamental mode of $u_t = \alpha\nabla^{2}u$ and its timescale for
$\alpha = 1$.

## ★★ Applied

**★★4.** For $u = \sin(\pi x)\sin(\pi y)$ on the unit square, derive the leading
error constant of the five-point scheme in the form $C h^{2}$ and state the
numerical value. Then compute the expected maximum error at $h = 1/50$ and
compare with the measured $0.822083\,h^{2}$ at $h = 1/65$.

**★★5.** A five-point Poisson problem on a $128\times128$ grid is solved to
$10^{-10}$ by CG. Using the measured growth exponent, estimate the iteration
count, then estimate it for a $256\times256$ grid and state the expected time
increase if each iteration costs proportional to the unknown count.

**★★6.** A backward-Euler march of the fundamental mode at $\alpha = 1$,
$dt = 10^{-3}$ gives an amplitude of $2.006603\times10^{-2}$ at $t = 0.2$ s
against an exact $1.929630\times10^{-2}$. Compute the relative bias and explain
its sign.

## ★★★ Research-oriented

**★★★7.** Design a Poisson benchmark for an iterative solver that measures,
independently: the discretisation order, the iteration-count scaling, and the
effect of a preconditioner. State the exact solution or right-hand side, the
metric, the grids, and the acceptance criteria. Explain why a single-mode
right-hand side must be avoided.

**★★★8.** A colleague proposes to solve a steady geothermal model as
"an explicit diffusion run to steady state" instead of a direct sparse solve.
Evaluate the proposal quantitatively for a $100\times100$ grid with
$h = 100$ m and $\alpha = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, giving step counts
and comparing the two approaches on work and robustness.
