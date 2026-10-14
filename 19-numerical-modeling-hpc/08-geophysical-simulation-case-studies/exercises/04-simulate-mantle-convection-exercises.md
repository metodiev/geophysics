# Exercises — 19-08-04 Simulating Mantle Convection

Attempt these before reading the
[solutions](./04-simulate-mantle-convection-solutions.md). The lesson is
[04 Simulating Mantle Convection](../04-simulate-mantle-convection.md). All models
are **SYNTHETIC**.

## ★ Foundational

**★1.** Evaluate $\mathrm{Ra}_c = 27\pi^{4}/4$ numerically from $\pi$ alone, and
compute the critical wavenumber and the critical wavelength in layer depths.

**★2.** Write the exact steady conductive temperature profile for a layer of depth
$d$ with $T(0) = T_0$, $T(d) = T_1$ and no internal heating, and state why the
three-point stencil reproduces it exactly.

**★3.** Compute the Rayleigh number of a mantle-like layer with
$\alpha = 3\times10^{-5}$ K$^{-1}$, $g = 9.81$ m s$^{-2}$, $\Delta T = 1000$ K,
$d = 2.9\times10^{6}$ m, $\kappa = 10^{-6}$ m$^{2}$s$^{-1}$ and
$\nu = \eta/\rho$ with $\eta = 10^{21}$ Pa s and $\rho = 3300$ kg m$^{-3}$. State
which input dominates the uncertainty.

## ★★ Applied

**★★4.** At $\mathrm{Ra} = 4\,\mathrm{Ra}_c$ compute the unstable band of horizontal
wavenumbers by solving $(\pi^{2}+k^{2})^{3}/k^{2} = 4\,\mathrm{Ra}_c$, and state the
range of cell widths, in layer depths, that a simulation must represent.

**★★5.** At $\mathrm{Ra} = 5000$ in a free-slip box of aspect ratio $2\sqrt{2}$
compute the growth rate of the fundamental mode and its e-folding time in diffusion
units.

**★★6.** The thermal boundary layer at $\mathrm{Ra} = 10^{6}$ has a thickness of
about $0.01$ layer depths. Compute the vertical resolution needed for four points
across it, and say what that implies for a $3$-D simulation of a $10^{3}$ mesh in
the horizontal directions.

## ★★★ Research-oriented

**★★★7.** Design a resolution study that would produce a defensible Nusselt number
at $\mathrm{Ra} = 10^{5}$, stating the grids, the run lengths, the averaging window,
and the criterion for declaring the answer converged. Include the failure mode in
which the answer never converges.

**★★★8.** The demonstration monitors $\max\lvert\theta\rvert \le 1$. Explain exactly
what physical statement that invariant encodes, why it can be violated by an
under-resolved run, and design a second invariant that would detect a run that is
under-resolved only in the horizontal direction.
