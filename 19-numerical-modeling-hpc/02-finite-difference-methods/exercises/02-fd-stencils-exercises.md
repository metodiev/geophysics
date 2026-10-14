# Exercises — 19-02-02 High-Order and Compact Stencils; Staggered Grids

Attempt these before reading the
[solutions](./02-fd-stencils-solutions.md). The lesson is
[02 FD Stencils](../02-fd-stencils.md). All models are **SYNTHETIC**. Numbers
printed by `../code/fd_stencils_demo.py` may be quoted directly.

## ★ Foundational

**★1.** Write the weights of the fourth-order centred first-derivative stencil
and its leading truncation term.

**★2.** Give the staggered two-point derivative formula and its leading
truncation term, and state the ratio of its constant to the centred
second-order stencil's.

**★3.** Define the resolving power of a scheme in one sentence, and state the
measured points per wavelength needed for a 1 % error by the second-order
explicit and the staggered two-point stencils.

## ★★ Applied

**★★4.** A wave model must keep the phase error at a carrier of
$\mathrm{PPW} = 10$ below $1\,\%$. Using the measured dispersion table, decide
whether the explicit fourth-order stencil, the staggered two-point stencil or
the compact fourth-order scheme is the cheapest sufficient choice, and justify
with numbers from the table.

**★★5.** The compact fourth-order scheme at $n = 256$ has an error of
$2.016\times10^{-9}$ against the explicit five-point stencil's
$1.210\times10^{-8}$ on the same grid. Compute the error ratio and state the
ratio of non-zeros per row for the two approaches at $n = 1024$.

**★★6.** Explain why the energy drift of a staggered leapfrog update stays at
$10^{-10}$ while an upwind update at the same Courant number removes the
highest mode in one step. Support the answer with the amplification factors.

## ★★★ Research-oriented

**★★★7.** Design and justify a scheme choice for a 3-D elastic wave model that
must run at 4 points per wavelength for the S wave and keep the phase error
below 2 %, given that memory is the binding constraint. State the scheme, its
measured resolving power, the CPML/sponge implications, and the verification you
would run before using it.

**★★★8.** The nine-point Laplacian reduces angular anisotropy by two orders of
magnitude at PPW $=16$ while increasing the matrix bandwidth by a factor $1.8$.
Construct an argument, with numbers from the measured tables, for or against
using it in a 3-D frequency-domain EM solver where the linear solve dominates
the cost.
