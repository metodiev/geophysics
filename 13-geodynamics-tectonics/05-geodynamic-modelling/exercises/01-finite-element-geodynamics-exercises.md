# Exercises — 13-05-01 Finite Element and Finite Volume Methods in Geodynamics

Attempt these before reading the
[solutions](./01-finite-element-geodynamics-solutions.md). The lesson is
[01 Finite Element and Finite Volume Methods](../01-finite-element-geodynamics.md),
and its numbers come from
[`code/finite_element_geodynamics_demo.py`](../code/finite_element_geodynamics_demo.py).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For the P1 element stiffness matrix on an interval of length $h$,

$$k_e = \frac{1}{h}\begin{pmatrix}1 & -1\\ -1 & 1\end{pmatrix},$$

compute $k_e$ for $h = 0.1$ m, verify that each row sums to zero, and explain in
one sentence why that must be true physically.

**★2.** A first-order upwind face scheme is used with $u = 0.1$ m/s and
$h = 0.01$ m. Compute (a) the cell Péclet number if the physical diffusivity is
$D = 2\times10^{-3}$ m²/s, and (b) the numerical diffusivity $|u|h/2$. State both
in m²/s and give the ratio $D_{\text{eff}}/D$.

**★3.** The demonstration measures $\beta_h = 1.912\times10^{-1}$ for Q1-Q1 at
$n = 4$ and $7.462\times10^{-2}$ at $n = 12$. Compute the ratio of the two and the
ratio of the mesh sizes, and state whether $\beta_h$ is bounded away from zero.

## ★★ Applied

**★★4.** For the periodic advection–diffusion problem of the lesson, derive the
condition $Pe_h = |u|h/D > 2$ for central differencing to lose monotonicity, by
requiring that the coefficient multiplying the upwind neighbour in the discrete
equation be non-negative.

**★★5.** Use the three finest $L^2$ errors of the P1 convergence table
($3.549\times10^{-4}$ at $n=64$, $1.419\times10^{-3}$ at $n=32$,
$5.661\times10^{-3}$ at $n=16$) to compute the observed order between successive
pairs. State what the agreement implies and what it does not.

**★★6.** A mantle convection model advects temperature with $|u| = 4$ cm/yr on
$h = 25$ km, with $\kappa = 1.0\times10^{-6}$ m²/s. Compute $Pe_h$ and the ratio
$D_{\text{num}}/\kappa$ for a first-order upwind scheme, and state whether either
elementary scheme is acceptable.

**★★7.** The demonstration verifies the assembly of the divergence operator by
evaluating $\|M_v^{-1}B^{\mathsf{T}}\mathbf{1}\|_\infty$ and finds
$1.678\times10^{-17}$. Design a second, independent assembly check that would
catch a bug this test cannot.

## ★★★ Research-oriented

**★★★8.** The stabilised Q1-Q1 pair has $\beta_h = 1.0039$ at $n = 4$ and
$0.63555$ at $n = 12$. Design a numerical experiment that decides whether the
stabilisation parameter should scale as $h^2$, $h$ or a constant, and state the
metric you would use and the outcome you would predict.

**★★★9.** A finite-volume scheme uses a flux form but reconstructs face values
with a non-conservative limiter. Specify a numerical experiment that would detect
the loss of conservation, including the quantity to monitor and the tolerance you
would demand, and explain why a global mass budget is a weaker test than a
flux-balance residual.

**★★★10.** For heat transport in a mantle model, argue for or against using the
same advection scheme for temperature and for a chemical tracer. Your answer must
name the quantity each transport law must conserve and identify one case in which
the two requirements conflict.
