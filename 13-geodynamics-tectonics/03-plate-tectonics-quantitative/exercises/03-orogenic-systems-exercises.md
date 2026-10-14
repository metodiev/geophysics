# Exercises — 13-03-03 Orogenic Systems, Crustal Thickening and Collapse

Attempt these before reading the
[solutions](03-orogenic-systems-solutions.md). The lesson is
[03 Orogenic Systems, Crustal Thickening and Collapse](../03-orogenic-systems.md).
All models and data in this module are **SYNTHETIC**.

Use $\rho_c = 2800$, $\rho_m = 3330$, $\rho_w = 1030\ \mathrm{kg\,m^{-3}}$,
$a = 125\ \mathrm{km}$, $T_m = 1300\ ^\circ\mathrm{C}$,
$\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$, $g = 9.81\ \mathrm{m\,s^{-2}}$, and a
reference crust $t_{c0} = 35\ \mathrm{km}$ at sea level.

## ★ Foundational

**★1.** A SYNTHETIC crust is $52\ \mathrm{km}$ thick. Compute its elevation
above the reference and its Moho depth below sea level.

**★2.** State the shortening required under volume conservation to thicken a
$35\ \mathrm{km}$ crust to $52\ \mathrm{km}$, and give the answer both as a
fraction and as kilometres of shortening per $100\ \mathrm{km}$ of section.

**★3.** Verify dimensionally that $\Gamma = \int[P(z)-P_{\text{ref}}(z)]\,
\mathrm dz$ has units of $\mathrm{N\,m^{-1}}$, and compute the mean deviatoric
stress it produces across a belt $150\ \mathrm{km}$ wide if
$\Gamma = 2.2\times10^{13}\ \mathrm{N\,m^{-1}}$.

## ★★ Applied

**★★4.** Compute $A - B$ style arithmetic from scratch: for the lesson's
densities, derive and evaluate the factor $(\rho_m-\rho_c)/\rho_m$ and state how
much crustal thickening is needed to raise the surface by $1\ \mathrm{km}$.

**★★5.** A plateau stands $3.0\ \mathrm{km}$ above the reference. Using the
two mechanisms of Section 5, find (i) the crustal thickening required,
(ii) the thickness of cold mantle lithosphere whose removal would explain the
same elevation, and (iii) the combination in which half the elevation comes from
each. State the physical quantity that would distinguish them.

**★★6.** Compute the buoyancy force per unit length for $t_c = 45\ \mathrm{km}$
using the lesson's exact integral, and compare it with
$g\rho_c(t_c^{2}-t_{c0}^{2})/2$. By what percentage does the scale overestimate
the force?

**★★7.** For a plateau with $e = 4.0\ \mathrm{km}$, $H = 65\ \mathrm{km}$,
$L = 300\ \mathrm{km}$, compute the collapse time for
$\eta = 10^{20}$, $10^{21}$ and $10^{22}\ \mathrm{Pa\,s}$, and state the
viscosity needed for the plateau to survive $40\ \mathrm{Myr}$.

**★★8.** A SYNTHETIC orogen at $5.0\ \mathrm{km}$ elevation is being eroded at
$0.3\ \mathrm{mm\,yr^{-1}}$. Compute the surface lowering rate and the rate of
Moho rise, and the time to remove the topography completely, assuming no
tectonic input.

## ★★★ Research-oriented

**★★★9.** The expression $\tau_c = \eta L/(\rho_c g\,\Delta e\,H)$ treats the
lithosphere as a viscous fluid with a single viscosity. Write down a
dimensionally consistent alternative in which the upper crust is elastic and only
a channel of thickness $h$ at the base of the crust deforms viscously, and
derive the new scaling. State which observations would separate the two models.

**★★★10.** Design a SYNTHETIC experiment to test whether a plateau's present
elevation is supported by a crustal root or by lithospheric buoyancy. Specify
the data types, the forward models, the noise model, the metric, and the
parameter trade-off you expect to find. A specification that could not be
executed is a failed answer.
