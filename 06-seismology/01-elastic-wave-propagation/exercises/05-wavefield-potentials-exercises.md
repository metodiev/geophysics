# Exercises — 06-01-05 Helmholtz Decomposition and Wavefield Potentials

Attempt these before reading the
[solutions](./05-wavefield-potentials-solutions.md). The lesson is
[05 Wavefield Potentials](../05-wavefield-potentials.md); all numbers are printed
by [`../code/wavefield_potentials_demo.py`](../code/wavefield_potentials_demo.py).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** State the Helmholtz decomposition for a vector field $\mathbf u$ in two
dimensions and in three dimensions, name the gauge freedom in each case, and say
what the gauge freedom means physically.

**★2.** For the demonstration's grid ($n = 256$ points, domain $L = 1.0\
\mathrm{m}$, periodic), compute $\Delta x$ and state the Nyquist wavenumber in
$\mathrm{rad\,m^{-1}}$. Then decide whether the injected P wavenumber
$\lvert\mathbf k\rvert = \sqrt{18.8496^{2} + 6.2832^{2}}$ is resolvable.

**★3.** Explain why a Poisson equation $\nabla^2\phi = \nabla\cdot\mathbf u$ cannot
determine the constant (zero-wavenumber) part of $\phi$, and state how the
demonstration handles it.

## ★★ Applied

**★★4.** The demonstration recovers $\phi$ and $\psi$ with relative $L^2$ errors
$3.226\times10^{-16}$ and $3.173\times10^{-16}$. Explain why these are at the
level of double-precision round-off rather than of the discretisation, by stating
what the *exact* derivative operator is on a periodic grid and comparing it with a
finite-difference operator at $\Delta x = 3.906\times10^{-3}\ \mathrm{m}$.

**★★5.** From the reported energies $\sum\lvert\nabla\phi\rvert^{2} =
1.293629\times10^{7}$ and $\sum\lvert\nabla\times(\psi\hat{\mathbf z})\rvert^{2} =
5.497922\times10^{6}$ (both in the same dimensionless grid units), compute the P
share of the kinetic energy and compare with the printed value $0.701754$.

**★★6.** The cross term $2\nabla\phi\cdot\nabla\times(\psi\hat{\mathbf z})$
integrates to $1.605827\times10^{-11}$ against $1.293629\times10^{7}$ of P energy,
a ratio of $8.711\times10^{-19}$. Explain why this is a *machine-precision* zero
rather than a small number, and state what property of the decomposition it
verifies.

## ★★★ Research-oriented

**★★★7.** In a three-dimensional elastic medium the S potential is a vector
$\boldsymbol\psi$ with $\nabla\cdot\boldsymbol\psi = 0$. Write the decomposition
for that case, state how many scalar fields it contains, and explain why the
two-dimensional scalar-$\psi$ shortcut used in this lesson is not generally
available in three dimensions.

**★★★8.** The demonstration builds a field from known potentials and then recovers
them. Design the reverse experiment: given only a three-component record on a
surface, specify the array geometry, the wavenumber band, and the test you would
apply to decide whether the decomposition is meaningful. State explicitly which
part of the field the surface array cannot determine, and why.

**★★★9.** A colleague decomposes a *non-periodic* field on a bounded grid with the
same Fourier method and reports relative errors of $10^{-1}$. Give three
independent explanations for the failure, ranked by how much of the error each
would explain, and state the cheapest fix for each.
