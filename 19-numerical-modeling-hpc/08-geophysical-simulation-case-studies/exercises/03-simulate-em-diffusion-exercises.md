# Exercises — 19-08-03 Simulating EM Diffusion in Conductive Media

Attempt these before reading the
[solutions](./03-simulate-em-diffusion-solutions.md). The lesson is
[03 Simulating EM Diffusion in Conductive Media](../03-simulate-em-diffusion.md).
All models are **SYNTHETIC**.

## ★ Foundational

**★1.** Compute the skin depth in a half-space of resistivity $50$ $\Omega$ m at
$0.05$ Hz, using both $\delta = \sqrt{2\rho/(\omega\mu_0)}$ and
$\delta = 503.29\sqrt{\rho/f}$, and state whether they agree.

**★2.** A layer is $200$ m thick with resistivity $40$ $\Omega$ m. Compute its
conductance in siemens.

**★3.** Explain in two sentences why the magnetotelluric phase over a uniform
half-space is exactly $45^\circ$, and why a departure from $45^\circ$ is
informative.

## ★★ Applied

**★★4.** Two layered models have the same conductance $S = 1$ S. The demonstration
measures their apparent-resistivity difference as $1.939$ per cent at $0.1$ s and
$0.625$ per cent at $1$ s. Estimate the period at which the difference would reach
$5$ per cent, and state the assumption behind the estimate.

**★★5.** A conductor has $\rho = 10$ $\Omega$ m. Compute the magnetic diffusivity
$D$ and the diffusion length $\sqrt{Dt}$ at $t = 1$ ms, then compute the fraction of
a surface step remaining at $100$ m depth at that time, using
$\mathrm{erfc}$ in a table or by interpolation.

**★★6.** The demonstration measures a first-order convergence for a layered solver
when a layer boundary falls exactly on a grid node. State the mechanism, the
measured orders ($2.06$ per cent at $\Delta z = 200$ m, $9.43$ at $100$, $4.86$ at
$50$, $2.47$ at $25$), and the two standard fixes.

## ★★★ Research-oriented

**★★★7.** You must resolve a $300$ m thick layer of $5$ $\Omega$ m beneath $500$ m
of $200$ $\Omega$ m, and to distinguish it from a $150$ m layer of $2.5$ $\Omega$ m.
Compute the periods at which the two models differ by more than $2$ per cent in
apparent resistivity, state whether they are practically measurable, and say what
limits the answer.

**★★★8.** A report claims a depth of investigation of $2$ km from a sounding whose
longest period is $100$ s in a $50$ $\Omega$ m half-space. Compute the relevant
diffusion length, state the threshold that the claim implicitly uses, and rewrite
the claim so that it is defensible.
