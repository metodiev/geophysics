# Exercises — 06-10-06 Engineering Seismology Applications

**All values are SYNTHETIC.** Attempt these before reading the
[solutions](./06-engineering-seismics-solutions.md). The lesson is
[06 Engineering Seismology Applications](../06-engineering-seismics.md).
The demonstration site is $4\ \mathrm{m}$ at $V_p/V_s = 400/150$,
$6\ \mathrm{m}$ at $1500/250$, $8\ \mathrm{m}$ at $1900/450$, and a half-space at
$3500/1800\ \mathrm{m\,s^{-1}}$, with densities $1800$, $1900$, $2000$,
$2500\ \mathrm{kg\,m^{-3}}$.

## ★ Foundational

**★1.** A two-layer target lies $20\ \mathrm{m}$ deep with
$v_1 = 1000\ \mathrm{m\,s^{-1}}$ and $v_2 = 3000\ \mathrm{m\,s^{-1}}$. Compute the
crossover distance and the spread that places it at one third of the line.

**★2.** With $1\ \mathrm{ms}$ picks and 40 equally spaced far-branch picks over
$x_c$ to $3x_c$ for ★1, compute $\sigma_{t_i}$, $\mathrm{d}h/\mathrm{d}t_i$ and
$\sigma_h$. Is a $\pm 0.5\ \mathrm{m}$ depth specification met?

**★3.** For the $8\ \mathrm{m}$ gravel layer ($V_p = 1900$,
$V_s = 450\ \mathrm{m\,s^{-1}}$, $\rho = 2000\ \mathrm{kg\,m^{-3}}$), compute
$\mu$, $\nu$, $E$ and $M$. State which of the four relations are exact and which
contain an assumption.

## ★★ Applied

**★★4.** The $V_s$ of ★3 is uncertain by $5\%$. Compute the fractional change in
$\mu$ and the resulting value, then compute the change in $\nu$ from
$\partial\nu/\partial V_s = -V_sV_p^{2}/(V_p^{2}-V_s^{2})^{2}$.

**★★5.** The demonstration's $18\ \mathrm{m}$ column has a travel-time-average
$V_s = 263.0\ \mathrm{m\,s^{-1}}$. Compute the site period, and the stiffness that
would put a $2.0\times10^{5}\ \mathrm{kg}$ single-degree-of-freedom oscillator on
that period.

**★★6.** A design event gives a surface velocity of $0.15\
\mathrm{m\,s^{-1}}$ in the top layer ($V_s = 150\ \mathrm{m\,s^{-1}}$). Estimate
the shear strain, and with a SYNTHETIC reduction curve
$G/G_{\max} = 1/(1+\gamma/10^{-3})$ compute $G/G_{\max}$ and the reduced $V_s$.

## ★★★ Research-oriented

**★★★7.** The demonstration's $V_{S30}$ budget is $\sigma = 3.020\
\mathrm{m\,s^{-1}}$ from the velocity errors alone and $3.841\
\mathrm{m\,s^{-1}}$ from a $0.10\ \mathrm{m}$ boundary tolerance, for a total of
$4.880\ \mathrm{m\,s^{-1}}$. A client asks for $\pm 2\ \mathrm{m\,s^{-1}}$. Show
whether that is achievable, and state the achievable target if only the boundary
tolerance can be halved.

**★★★8.** At a dominant frequency of $50\ \mathrm{Hz}$, which of the four
demonstration layers would a P-wave refraction survey resolve as a separate arrival,
and which would an S-wave survey resolve? Give the numbers, state the criterion
used, and compute the frequency at which the $6\ \mathrm{m}$ clay layer would become
resolvable to a P-wave survey.
