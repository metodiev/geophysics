# Exercises — 10-03-01 GPR for Soil Moisture, Water Table and Aquifer Structure

Attempt these before reading the
[solutions](./01-gpr-hydrogeology-solutions.md). The lesson is
[01 GPR for Soil Moisture, Water Table and Aquifer Structure](../01-gpr-hydrogeology.md).
All models and data in this module are **SYNTHETIC**: the porosity, grain
permittivity and moisture values are teaching values, and the only non-chosen
numbers are physical constants ($c = 0.299792458\ \mathrm{m\,ns^{-1}}$,
$Z_0 = 376.73\ \Omega$, $\varepsilon_w = 80.1$ at $20\ ^\circ\mathrm{C}$).

## ★ Foundational

**★1.** A soil has $\phi = 0.40$, $\varepsilon_g = 5.0$, $\theta = 0.20$ and
$\varepsilon_w = 80.1$. Compute the CRIM permittivity $\varepsilon_r$, the
saturation $S$, the speed $v$, and the wavelength at $250\ \mathrm{MHz}$. State
the units of each.

**★2.** For the same soil, compute $\partial\theta/\partial\phi$ from the CRIM
inversion, and state how much a porosity error of $0.03$ moves the inferred
water content.

**★3.** Compute the normal-incidence reflection coefficient between
$\varepsilon_r = 6.0$ above and $\varepsilon_r = 21.0$ below an interface, express
it in dB, and state whether the reflected pulse is phase-reversed.

## ★★ Applied

**★★4.** A two-way time of $30.0\ \mathrm{ns}$ is measured to a reflector. A
shallow common-midpoint sounding gives $v = 0.115\ \mathrm{m\,ns^{-1}}$ and the
analyst converts with it. Later drilling shows the reflector is at
$1.40\ \mathrm{m}$ and the profile is $0.60\ \mathrm{m}$ of soil at
$\varepsilon_r = 5.0$ over material at $\varepsilon_r = 16.0$. Compute the true
two-way time, the reported depth, the error in metres and per cent, and identify
which layer the single velocity was biased toward.

**★★5.** A water-table contact has a sharp-interface coefficient
$R_0 = -0.31$. Using the demonstration's sinc result
$R(f) = R_0\,\mathrm{sinc}(f\tau)$, compute the observed $|R|$ at
$250\ \mathrm{MHz}$ for fringes of $0.05$, $0.10$ and $0.20\ \mathrm{m}$ in a
medium with $v = 0.10\ \mathrm{m\,ns^{-1}}$. For the $0.10\ \mathrm{m}$ fringe,
what sharp-interface $|R_0|$ would be inferred by an analyst who did not know
about the fringe, and by what factor would the moisture contrast then be
under-estimated?

**★★6.** A soil has $\varepsilon_r = 9.0$ and $\sigma = 0.02\ \mathrm{S\,m^{-1}}$.
Compute $\tan\delta$ at $100$ and $250\ \mathrm{MHz}$, decide in each case whether
the low-loss approximation is acceptable (state your threshold), and compute the
60 dB two-way depth at $250\ \mathrm{MHz}$ using the exact formula.

## ★★★ Research-oriented

**★★★7.** Design a field procedure that determines the water-table depth of a
sandy site to $\pm 0.10\ \mathrm{m}$ using only GPR, with a stated porosity. Your
answer must specify: the frequency, the survey geometry that gives the velocity
(reference to the lesson's dependence on aperture and on the profile), the
independent constraint on the porosity, and the number you will quote as the
result. A specification that could not be executed is a failed answer.

**★★★8.** The demonstration's Monte Carlo gives a depth standard deviation of
$0.0563\ \mathrm{m}$ for a $1.20\ \mathrm{m}$ water table, of which
$0.0475\ \mathrm{m}$ is velocity and $0.0306\ \mathrm{m}$ is picking. Using
$\sigma_z^2 = \sigma_v^2 + \sigma_t^2$ as the combination, find the factor by
which the velocity uncertainty would have to fall for the two terms to
contribute equally, state whether the result would then be dominated by either
term, and quote the total uncertainty in that case. Show the arithmetic.

**★★★9.** CRIM and an empirical calibration disagree by $1.79$ percentage points
of water content at $\varepsilon_r = 9.0$ in the demonstration. Construct two
concrete physical reasons for such a difference in a clay-bearing soil, and for
each reason state a measurement (not an assumption) that would detect it.
