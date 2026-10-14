# Exercises — 16-02-04 Earth Energy Balance and Global Mean Temperature

Attempt these before reading the
[solutions](./04-earth-energy-balance-solutions.md). The lesson is
[04 Earth Energy Balance](../04-earth-energy-balance.md). Use
$\sigma = 5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$,
$S = 1361\ \mathrm{W\,m^{-2}}$ and
$R_E = 6.371\times10^{6}\ \mathrm{m}$ unless stated otherwise. All models are
**SYNTHETIC**: albedos, surface temperatures, emissivities, solar partitions and
Bowen ratios are chosen teaching values.

## ★ Foundational

**★1.** For a planetary albedo of $0.30$, compute $S/4$, the reflected flux, the
absorbed flux $F$ and the effective radiating temperature. Repeat for an albedo of
$0.15$ and state the ratio of the two $T_e$ values.

**★2.** A surface at $290\ \mathrm{K}$ absorbs $238.175\ \mathrm{W\,m^{-2}}$ of
sunlight and receives $200\ \mathrm{W\,m^{-2}}$ of downwelling infrared. Compute
its emitted flux, the ratio of emitted to absorbed solar flux, and the
non-radiative flux it must export. State the sign convention you used.

**★3.** A planet's net top-of-atmosphere flux profile is modelled as
$N(\phi) = 30 - 90\sin^2\phi\ \mathrm{W\,m^{-2}}$. Verify that its area-weighted
mean is zero, derive $H(\phi)$ analytically, and compute $H_{\max}$ in PW.

**★4.** For $F = 227.5\ \mathrm{W\,m^{-2}}$ compute $T_e$, the Planck response
$4\sigma T_e^3$, and the no-feedback temperature change for a forcing of
$2.0\ \mathrm{W\,m^{-2}}$.

## ★★ Applied

**★★5.** Derive
$\sigma T_s^4(2-\varepsilon) = F(1+f_s) - (H+LE)$
from the three energy-balance equations for a two-box (surface + single grey layer)
model, showing the elimination of the layer temperature and verifying that the
result reduces to the lesson-02 one-layer formula when $f_s = 1$ and $H+LE = 0$.

**★★6.** For the planet $S = 1300\ \mathrm{W\,m^{-2}}$, $a = 0.30$,
$T_s = 288\ \mathrm{K}$, $f_s = 0.80$, compute the required non-radiative flux for
$\varepsilon = 0.5$, $0.7$, $0.85$, $0.95$ and $1.0$. Find the emissivity at which
it is zero, and state in one sentence what that value means.

**★★7.** Derive $H(\phi)$ for a general profile $N = A + B\sin^2\phi$ subject to
global balance, and show that it reduces to the lesson's result for $B = -120$ and
to the result of ★3 for $B = -90$. State which quantity in your expression is a
model choice and which is geometric.

**★★8.** A surface at $288\ \mathrm{K}$ is in balance with $f_s = 1$,
$\varepsilon = 1$ and a Bowen ratio of $0.25$. Compute $H$, $LE$ and the fraction
of the absorbed solar flux that leaves the surface non-radiatively. Then repeat for
a Bowen ratio of $0.8$ and state which quantity changed and which did not.

## ★★★ Research-oriented

**★★★9.** Design a procedure that would determine the required poleward energy
transport from measurements alone, with no assumed profile for $N(\phi)$. Specify
the measurement, the spatial and temporal sampling needed to close the integral,
the metric, and two error sources that would make the closure fail without any
physical violation. State what would falsify the claim that the transport must
vanish at the equator.

**★★★10.** The lesson shows that a surface energy budget is degenerate between
atmospheric opacity and non-radiative flux. Design an observational programme that
breaks the degeneracy using only quantities measured at the surface or from a
single column, and state precisely which measurement does the breaking and what
independent assumption it still requires. Then state the measurement that would
break it without any assumption at all, and whether it is feasible.

**★★★11.** "The global mean surface temperature rose by $X$ kelvin." Analyse this
statement: what must be specified for it to be well defined (spatial weighting,
temporal window, definition of "surface", treatment of missing regions, treatment
of changing station networks), and which of those are definitional and which are
physical. Then state which component of the uncertainty is reducible with more
stations and which is not.

**★★★12.** Construct a planetary energy budget whose residual is positive, and
show that the planet must be warming. Then relate the rate of warming to the
residual using the heat capacity of the system, stating which component dominates
and what additional measurement is required to convert the residual into a rate.
Explain why this is the one place where the "equilibrium" assumption of the lesson
must be abandoned, and what changes as a result.
