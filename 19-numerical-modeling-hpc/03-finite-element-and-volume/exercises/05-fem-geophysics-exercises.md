# Exercises — 19-03-05 FEM in Geophysics: EM, Geodynamics and Seismology

Attempt these before reading the
[solutions](./05-fem-geophysics-solutions.md). The lesson is
[05 FEM in Geophysics: EM, Geodynamics and Seismology](../05-fem-geophysics.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute the skin depth for $\sigma = 0.1$ S/m at $f = 0.1$ Hz, using
$\mu_0 = 4\pi\times10^{-7}$ H/m, and state its unit.

**★2.** For a uniform half-space of conductivity $\sigma$, state the exact
impedance $Z$, the phase, and the apparent resistivity, and verify the apparent
resistivity against the reciprocal of $\sigma$ for $\sigma = 0.01$ S/m.

**★3.** Write the radiation (admittance) boundary condition used at the base of
the magnetotelluric domain and state, in one sentence, which physical branch of
the solution fixes the sign.

## ★★ Applied

**★★4.** The SH transfer function uses $\gamma = \rho_1\beta_1/(\rho_2\beta_2)$
with $\rho_1 = 2000$ kg/m³, $\beta_1 = 500$ m/s, $\rho_2 = 2500$ kg/m³,
$\beta_2 = 1500$ m/s. Compute $\gamma$, the quarter-wavelength frequency for
$H = 100$ m, and the amplification $1/\gamma$ expected at resonance.

**★★5.** The steady Stokes model has $\nu(y) = 1+0.5y$ and manufactured
$u = y(1-y)$. Verify that $f = 1.5+2y$ produces it, and check the stress balance
$\tau(1) - \tau(0) = -\int_0^1 f\,\mathrm{d}y$.

**★★6.** The two-layer magnetotelluric model has $\sigma_1 = 0.01$ S/m over
2 km and $\sigma_2 = 0.001$ S/m. Explain why the apparent resistivity *rises*
from 93 Ω·m at 5 Hz to 511 Ω·m at 0.1 Hz, and state which parameter controls
where the rise begins.

## ★★★ Research-oriented

**★★★7.** Show that changing the sign of the admittance in the radiation
condition corresponds to launching an exponentially *growing* solution in the
half-space, and predict what a convergence study would report for that run
consistently with the measured failure.

**★★★8.** Design a verification test that distinguishes an error in the
element formulation from an error in the recovery of $E'(0)$ at the surface, for
the layered magnetotelluric problem. State the two runs, the metric, and the
diagnosis each outcome supports.
