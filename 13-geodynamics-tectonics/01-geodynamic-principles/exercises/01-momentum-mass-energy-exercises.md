# Exercises — 13-01-01 Momentum, Mass and Energy Balances in the Solid Earth

Attempt these before reading the
[solutions](./01-momentum-mass-energy-solutions.md). The lesson is
[01 Momentum, Mass and Energy Balances](../01-momentum-mass-energy.md). All
models are **SYNTHETIC** teaching values unless stated otherwise.

## ★ Foundational

**★1.** A buoyant sphere of radius $50\ \mathrm{km}$ and density contrast
$30\ \mathrm{kg\,m^{-3}}$ rises in a fluid of density $3300\ \mathrm{kg\,m^{-3}}$
and viscosity $10^{21}\ \mathrm{Pa\,s}$. Compute the Stokes velocity in
$\mathrm{m\,s^{-1}}$ and in $\mathrm{mm\,yr^{-1}}$, and compute the Reynolds
number. State whether the Stokes result is valid and why.

**★2.** A shear zone $20\ \mathrm{km}$ thick accommodates
$20\ \mathrm{mm\,yr^{-1}}$ of relative motion with
$\eta = 10^{21}\ \mathrm{Pa\,s}$. Compute the strain rate, the volumetric
dissipation rate and the column-integrated heat flux in
$\mathrm{mW\,m^{-2}}$.

**★3.** State the units of (a) $\eta u/L^{2}$, (b) $uL/\kappa$, (c)
$\rho c_p V\Delta T$, and verify by dimensional analysis that (a) is a force per
unit volume.

## ★★ Applied

**★★4.** A SYNTHETIC crust $40\ \mathrm{km}$ thick has
$k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$, uniform radiogenic production
$H = 2	imes10^{-6}\ \mathrm{W\,m^{-3}}$ and $600\ ^\circ$C at its base.
**(a)** Compute the surface and Moho heat fluxes and the fraction of the surface
flux that is radiogenic, and explain in one sentence why the Moho flux is so small
here. **(b)** At what $H$ would the Moho heat flux vanish, and what is the
physical meaning of that value?

**★★5.** For $u = 30\ \mathrm{mm\,yr^{-1}}$ and
$\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, compute the Péclet number at
$L = 10$ km and at $L = 1000$ km, and the diffusive and advective times at both
scales. At which scale does diffusion matter?

**★★6.** A spherical blob is observed to rise $500\ \mathrm{km}$ in 20 Myr.
Taking $\Delta\rho = 25\ \mathrm{kg\,m^{-3}}$ and $a = 120\ \mathrm{km}$, invert
the Stokes law for the viscosity. State the two largest sources of error in that
inversion.

## ★★★ Research-oriented

**★★★7.** The global budget of the lesson uses
$q_{\text{avg}} = 87\ \mathrm{mW\,m^{-2}}$ and a radiogenic production of
20 TW. Repeat the budget for $q_{\text{avg}} = 100\ \mathrm{mW\,m^{-2}}$ and a
production of 25 TW. Compute the new heat loss, Urey ratio and cooling time, and
state which of the two inputs the conclusion is more sensitive to.

**★★★8.** Design a numerical experiment that would demonstrate that a
divergence-free velocity field is *necessary*, not merely convenient, for a
convection code. State the diagnostic you would compute, the initial condition,
the run length, and the result that would convince you. A specification that
could not be executed is a failed answer.

**★★★9.** The lesson claims that the cooling time of $\sim6\ \mathrm{Gyr}$ is
a consistency constraint rather than a prediction. Write a short argument
(150–250 words) that makes the claim precise: what would have to be true for the
present heat loss and production to have been constant over Earth history, and
which of those assumptions fails first?
