# Exercises — 12-01-01 PREM, IASP91 and Reference Earth Models

Attempt these before reading the
[solutions](./01-prem-and-reference-models-solutions.md). The lesson is
[01 PREM, IASP91 and Reference Earth Models](../01-prem-and-reference-models.md).
All models and data are **SYNTHETIC** teaching values; the interface depths are
conventional labels, not measurements.

Useful constants: Earth radius $R = 6371\ \mathrm{km}$,
$1\ \mathrm{rad} = 57.2958°$, $1° \approx 111.19\ \mathrm{km}$ on a sphere of
radius $R$.

## ★ Foundational

**★1.** Convert $p = 0.0600\ \mathrm{s\,km^{-1}}$ (the flat-Earth convention) into
(a) $\mathrm{s\,rad^{-1}}$ and (b) $\mathrm{s\,deg^{-1}}$ on a sphere of radius
$R = 6371\ \mathrm{km}$, given that the two conventions coincide at the surface
where $r = R$. State which one you would use as input to the spherical ray
integrals.

**★2.** A model has, over the depth interval 670–2891 km, a linear $v_p$ from
$10.75$ to $13.72\ \mathrm{km\,s^{-1}}$. Compute the vertical travel time through
that interval exactly by integrating $\mathrm{d}r/v$ over the linear profile, and
compare it with the estimate obtained by dividing the interval length by the
midpoint velocity. Report both with units and state which is larger.

**★3.** For a homogeneous sphere of radius $R = 6371\ \mathrm{km}$ and
$v = 8.00\ \mathrm{km\,s^{-1}}$, compute the epicentral distance and travel time
of the ray that turns at $r_{tp} = 5000\ \mathrm{km}$. Use the closed forms
$\Delta = 2\arccos(r_{tp}/R)$ and $T = 2\sqrt{R^2-r_{tp}^2}/v$.

## ★★ Applied

**★★4.** Using the branch table of the lesson ($\Delta = 86.404°$ at
$p = 4.8099\ \mathrm{s\,deg^{-1}}$, $T = 778.27\ \mathrm{s}$; and
$\Delta = 89.666°$ at $p = 4.5470\ \mathrm{s\,deg^{-1}}$,
$T = 793.53\ \mathrm{s}$), use the slowness identity to estimate the depth of the
turning point at $\Delta = 88°$. You may approximate the model near that depth by
a locally linear $v_p(r)$ with $v = 13.4\ \mathrm{km\,s^{-1}}$ at $r = 3580\
\mathrm{km}$ and $\mathrm{d}v/\mathrm{d}r = -5.0\times10^{-3}\ \mathrm{s^{-1}}$.

**★★5.** A two-layer Earth has $\rho_m = 4.7\ \mathrm{g\,cm^{-3}}$,
$\rho_c = 11.0\ \mathrm{g\,cm^{-3}}$ and a core radius of $3000\ \mathrm{km}$.
Compute $C/MR^2$ using
$\frac{C}{MR^2} = \frac{2}{5}\frac{\rho_c q^5 + \rho_m(1-q^5)}
{\rho_c q^3 + \rho_m(1-q^3)}$ with $q = a/R$, and say whether this model is
compatible with the conventional value $0.3307$. Justify the answer with the
number.

**★★6.** The lesson's model gives $T_\text{vert} = 507.818\ \mathrm{s}$ from the
surface to the ICB and $1015.720\ \mathrm{s}$ from the surface to the centre.
Explain the factor-of-two difference between these two numbers, and use them to
estimate the mean $v_p$ in the inner core with an explicit assumption about the
outer core.

## ★★★ Research-oriented

**★★★7.** Construct a perturbation of a two-layer model that changes $v$ without
changing the travel time of *any* ray to first order. Write the perturbation
explicitly, verify the claim by computing $T(\Delta)$ for two rays with and
without it, and state how many parameters of the perturbation are constrained by
the data. Quantify the size of the unconstrained direction relative to the
constrained one.

**★★★8.** Design a validation test for a new travel-time code that is stronger
than the homogeneous-sphere check of the lesson. State the analytic reference
you would use, the expected error, and the failure mode the test would catch that
the homogeneous sphere does not.

**★★★9.** The synthetic model's mass is 3.0 % below the standard Earth mass while
its $C/MR^2$ is within 0.4 % of the conventional value. Explain how both can be
true at once, using the integrals for $M$ and $C$. Then state which of the two
numbers is the more sensitive test of the density profile near the *centre*, and
prove it with the powers of $r$ in the two integrands.
