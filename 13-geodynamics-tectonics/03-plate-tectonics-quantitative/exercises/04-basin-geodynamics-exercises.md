# Exercises — 13-03-04 Basin Formation and Subsidence Modelling

Attempt these before reading the
[solutions](04-basin-geodynamics-solutions.md). The lesson is
[04 Basin Formation and Subsidence Modelling](../04-basin-geodynamics.md).
All models and data in this module are **SYNTHETIC**.

Use $\rho_m = 3330$, $\rho_w = 1030\ \mathrm{kg\,m^{-3}}$,
$a = 125\ \mathrm{km}$, $\kappa = 31.558\ \mathrm{km^{2}\,Myr^{-1}}$,
$A = 8.065\ \mathrm{km}$, $B = 1.829\ \mathrm{km}$, $g = 9.81\
\mathrm{m\,s^{-2}}$, and for the elastic plate $E = 70\ \mathrm{GPa}$,
$\nu = 0.25$.

## ★ Foundational

**★1.** A well has $0.2\ \mathrm{km}$ of water and two beds:
$0.8\ \mathrm{km}$ at $2100\ \mathrm{kg\,m^{-3}}$ and $1.1\ \mathrm{km}$ at
$2450\ \mathrm{kg\,m^{-3}}$ (top to bottom). Backstrip both beds and give the
water-loaded tectonic subsidence at the base of the lower bed, with the
arithmetic for each term.

**★2.** State the two limits of the backstripping equation as $\rho_i \to
\rho_w$ and $\rho_i \to \rho_m$, and explain in one sentence why each is
correct.

**★3.** Compute $D$ and $\alpha$ for $T_e = 15\ \mathrm{km}$ using
$\Delta\rho = \rho_m - \rho_w$.

## ★★ Applied

**★★4.** For the SYNTHETIC basin $X(t) = [S(t)-S(0)](\rho_m-\rho_w)/(\rho_m-
\rho_{\text{fill}})$ with $\rho_{\text{fill}} = 2200$: compute $X$ at post-rift
times $20$, $40$, $60$ and $80\ \mathrm{Myr}$, using $S(0) = 3.118\ \mathrm{km}$
and the McKenzie curve for $\beta = 2$, $\tau = 50.17\ \mathrm{Myr}$. Compare
with the bed boundaries $1.616$, $0.854$ and $0.343\ \mathrm{km}$ of the lesson.

**★★5.** Backstrip the lesson's four beds using the **present-day** densities
given in the lesson's table and compare with curve A. Then repeat with all
densities set to $2200\ \mathrm{kg\,m^{-3}}$ and explain the sign of the
difference in terms of the buoyancy of each stripped bed.

**★★6.** A foreland basin is $3.0\ \mathrm{km}$ deep at its depocentre and
$150\ \mathrm{km}$ wide, with the forebulge $90\ \mathrm{km}$ beyond the
depocentre. Estimate $\alpha$ and $T_e$ and state the assumptions.

**★★7.** The backstrip of a SYNTHETIC margin gives a total subsidence of
$2.4\ \mathrm{km}$ at $60\ \mathrm{Myr}$ after break-up. Using the McKenzie
closed forms with $\tau = 50.17\ \mathrm{Myr}$, compute the $\beta$ implied by
the total subsidence alone, and state why the answer is sensitive to $\tau$.

## ★★★ Research-oriented

**★★★8.** Write a short specification for a flexural (non-local) backstripping
scheme: state the equation to be solved, the unknown, the boundary conditions,
the additional parameters relative to local backstripping, and the observation
that would reveal that local backstripping is inadequate.

**★★★9.** The lesson shows that a wrong compaction model returns
$\beta = 3.35$ instead of $2.00$ with a residual of only $5.9\ \mathrm{m}$.
Design a test that would detect this error using data that do not enter the
backstripping, and state what would falsify your test.
