# Exercises — 19-05-03 Numerical Green's Functions and Their Computation

Attempt these before reading the
[solutions](./03-greens-function-numerics-solutions.md). The lesson is
[03 Numerical Green's Functions and Their Computation](../03-greens-function-numerics.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For $L = 1$, evaluate the tent function $G(x;0.5) = x_{<}(1-x_{>})$
at the five nodes $x = 0.1, 0.3, 0.5, 0.7, 0.9$ and confirm the value at the
source.

**★2.** Compute $\int_{0}^{L}\ln|t - L/2|\,\mathrm{d}t$ for $L = 1$ and state the
sign.

**★3.** State why the discrete 1-D Green's function is exact at the nodes and why
the same is not true in two dimensions.

## ★★ Applied

**★★4.** From the lumped-source table ($n = 128$: error $1.923\times10^{-3}$;
$n = 512$: $4.864\times10^{-4}$) show that the error is proportional to $h$ and
estimate the constant.

**★★5.** For $y = 2.5$ km and a node centre $c = 0.498564$ km, compute the
monopole estimate $M_0/|y-c|$ from $M_0 = 4.04726574\times10^{2}$ and compare
with the printed $202.2180799309$.

**★★6.** The screened lattice-versus-$K_0$ table gives relative errors
$7.124\times10^{-2}$ at $h = 0.5$ km and $1.764\times10^{-2}$ at $h = 0.25$ km.
Compute the observed order and predict the error at $h = 0.0625$ km.

## ★★★ Research-oriented

**★★★7.** The Laplace constant increments by $0.10959$, $0.11017$ and $0.11043$
for successive doublings of $L$, against $\frac{1}{2\pi}\ln2 = 0.110318$. Explain
why the increments converge *from below* and what that says about the grid
error's sign.

**★★★8.** Design an experiment using only this lesson's tools that determines
whether a kernel error of $1\%$ comes from the source-mass normalisation or from
the grid symbol, and state the observable that separates them.
