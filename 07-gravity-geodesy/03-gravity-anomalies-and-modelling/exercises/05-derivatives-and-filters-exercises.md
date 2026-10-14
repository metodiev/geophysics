# Exercises — 07-03-05 Derivatives, Upward/Downward Continuation and Euler Deconvolution

Attempt these before reading the
[solutions](./05-derivatives-and-filters-solutions.md). The lesson is
[05 Derivatives and Filters](../05-derivatives-and-filters.md). All models are
**SYNTHETIC**.

## ★ Foundational

**★1.** Write the wavenumber-domain multipliers for $\partial/\partial x$,
$\partial/\partial z$ ( $z$ upward) and upward continuation by $1\ \mathrm{km}$,
and give the units of each result when the input is in mGal.

**★2.** Explain in two sentences why the space-domain filter corresponding to a
vertical derivative does not have compact support.

**★3.** State the amplification factor of downward continuation at the Nyquist
wavenumber for a $100\ \mathrm{m}$ station spacing and a $500\ \mathrm{m}$
continuation, and the physical reason it is so large.

## ★★ Applied

**★★4.** A survey has $100\ \mathrm{m}$ spacing and $0.03\ \mathrm{mGal}$ rms
noise, and the smallest target has a $700\ \mathrm{m}$ wavelength. Using the
lesson's bias–variance table, choose a cutoff wavelength and justify the choice in
terms of bias and noise.

**★★5.** Derive the Euler equation from the homogeneity of
$g = GMz_0/r^{3}$ (degree $-2$ in the source-to-observer vector) and confirm that
the coefficient of the $g_z$ term is $z_0$.

**★★6.** From the lesson's structural-index table, state the depth error you would
report as the *range* implied by the four trial indices for the
$800\ \mathrm{m}$ source, and say what evidence would let you reject the wrong
ones.

## ★★★ Research-oriented

**★★★7.** With a $0.03\ \mathrm{mGal}$ noise level, an $100\ \mathrm{m}$ grid and
a tolerance of $0.1\ \mathrm{mGal}$ on the continued field, find the maximum depth
to which downward continuation is admissible, stating your assumption about the
noise spectrum.

**★★★8.** A two-source field is windowed for Euler deconvolution. Design a
rejection criterion that would flag the windows whose estimates are contaminated,
and explain how you would report the surviving estimates spatially rather than as
a single number.
