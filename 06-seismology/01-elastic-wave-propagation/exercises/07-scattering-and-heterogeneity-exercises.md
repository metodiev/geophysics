# Exercises — 06-01-07 Scattering, Coda and Random Media

Attempt these before reading the
[solutions](./07-scattering-and-heterogeneity-solutions.md). The lesson is
[07 Scattering, Coda and Random Media](../07-scattering-and-heterogeneity.md);
all numbers are printed by
[`../code/scattering_demo.py`](../code/scattering_demo.py). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For the demonstration's background ($v_0 = 3000\ \mathrm{m\,s^{-1}}$,
$\rho_0 = 2500\ \mathrm{kg\,m^{-3}}$) compute $Z_0$ with its unit, and compute the
single-interface reflection coefficient for a jump up to $1.1\,Z_0$ in the
potential convention.

**★2.** With $v_j = v_0(1+\sigma\xi_j)$ and $\rho_j = \rho_0(1+\sigma\eta_j)$ for
independent standard normal $\xi,\eta$, derive $\sigma_Z^2 = 2\sigma^2$ and
evaluate it for $\sigma = 0.02$.

**★3.** The demonstration's second check uses a single 1 m layer of impedance
$2Z_0$ over a half space $Z_0$ and prints $R = +0.3333333333$. Derive that value
from the impedance contrast, and say what property of the recursion this check
fixes (and why the trivial uniform-stack check $|R| = 0$ cannot fix it).

## ★★ Applied

**★★4.** For $\sigma = 0.01$ and $N = 2000$ one-metre layers, compute the three
limits: one interface, a fully coherent stack, and an incoherent stack. Then state
which of them the demonstration's measured $2\ \mathrm{Hz}$ value
$6.124800\times10^{-5}$ lies closest to, and what that says about the phase
correlation at that frequency.

**★★5.** Compute the number of cycles of two-way phase wrapped across the 2 km
stack at $f = 2\ \mathrm{Hz}$ and at $f = 160\ \mathrm{Hz}$ for
$v = 3000\ \mathrm{m\,s^{-1}}$. Then state, with the number, why the
small-phase law $|R|^2 \propto \omega^2$ cannot describe the low end of the
demonstration's band.

**★★6.** Using the demonstration's frequency table, compute the local power-law
exponent of $\lvert R_{\text{Born}}\rvert^{2}$ in $f$ over the octaves
$2\!-\!5\ \mathrm{Hz}$, $5\!-\!10\ \mathrm{Hz}$ and $10\!-\!20\ \mathrm{Hz}$, and
say whether the exponent is increasing or decreasing with frequency.

## ★★★ Research-oriented

**★★★7.** The demonstration's medium has no correlation length: each layer's
perturbation is independent of its neighbour. Design an experiment that measures
how the frequency exponent changes when the fluctuations are correlated over a
stated length $\ell$. State the generation recipe, the fit range, and the
qualitative prediction, and say which regime you expect to be most sensitive to
$\ell$.

**★★★8.** Derive the Born sum from the exact recursion by expanding to first
order in the interface coefficients, stating at each step what is discarded, and
show that the resulting sum is a discrete Fourier transform of the reflectivity
sequence evaluated at the two-way phase.

**★★★9.** The demonstration prints a "coherent limit" of $\sigma_Z^2/2$; the exact
fully coherent value of a stack is $\sigma_Z^2/4$. Derive the telescoping result,
explain the factor of two, and state which of the two numbers the measured
$2\ \mathrm{Hz}$ value is consistent with.
