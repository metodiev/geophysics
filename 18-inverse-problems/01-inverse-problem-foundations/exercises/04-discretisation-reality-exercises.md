# Exercises — 18-01-04 Discretisation, Parameterisation and Model Choice

Attempt these before reading the
[solutions](./04-discretisation-reality-solutions.md). The lesson is
[04 Discretisation and Model Choice](../04-discretisation-reality.md). All models
are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Name the three errors that enter an inversion result and state where each
one is introduced.

**★2.** A block-averaged representation has data errors
$5.550\times10^{-3}$ at $5\ \mathrm{km}$ blocks and
$1.887\times10^{-3}$ at $2.5\ \mathrm{km}$ blocks. Compute the ratio and state
whether it is consistent with second-order convergence.

**★3.** Seven gravity readings include one at the surface and one at the bottom of
the stack. Explain why the two are exactly opposite, and state the numerical rank
of the kernel.

## ★★ Applied

**★★4.** Model errors for $M = 3,4,5,7,20$ blocks are
$0.9999\%,\ 0.6334\%,\ 0.8773\%,\ 1.6433\%,\ 1.3618\%$. (a) Identify the
non-monotonicity. (b) Explain it in terms of the estimator, not the noise.
(c) Recommend which $M$ to report and justify the choice.

**★★5.** The $M = 100$ kernel has $\sigma_1 = 8.136166\times10^{-2}$ and
$\sigma_7 = 3.949768\times10^{-17}$. Compute the relative singular value, compare
with $\varepsilon = 2.220\times10^{-16}$, and compute the amplification $1/\sigma_7$
that an untruncated pseudo-inverse would apply to a data error in that direction.

**★★6.** The reported density at $z = 5\ \mathrm{km}$ for the 300 sampled models
spans $[2620.4,3200.8]\ \mathrm{kg\,m^{-3}}$, while the truth is
$2909.9\ \mathrm{kg\,m^{-3}}$. (a) Compute the relative spread. (b) State the fit
of those models relative to the min-norm fit. (c) Explain in two sentences what
you would write in a report instead of a single number.

## ★★★ Research-oriented

**★★★7.** You must choose between 2 km blocks and 2 km-spaced linear elements for
a target with a known smooth gradient. Using the representation-error table for an
exactly linear truth, justify the choice with numbers, and state the condition
under which your justification would fail.

**★★★8.** A reviewer objects that a regularised inversion "invented" structure
because the unregularised result looked sharper. Using the $\alpha$ table
(0, $10^{-2}$, $3\times10^{-2}$) construct a quantitative reply: what is the
misfit and the model error at each $\alpha$, and which of the two is more
faithful to the truth in this experiment? State the honest limitation of your
answer.
