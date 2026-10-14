# Exercises — 08-01-05 The Geodynamo: Mechanism and Evidence

Attempt these before reading the
[solutions](./05-dynamo-theory-solutions.md). The lesson is
[05 The Geodynamo: Mechanism and Evidence](../05-dynamo-theory.md). All
parameters are **SYNTHETIC** teaching values.

Use $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ and
$1\ \mathrm{yr} = 3.1557\times10^{7}\ \mathrm{s}$.

## ★ Foundational

**★1.** Compute the magnetic diffusivity $\eta = 1/(\mu_0\sigma)$ for
$\sigma = 1.0\times10^{6}\ \mathrm{S\,m^{-1}}$ and state its unit.

**★2.** Using the $\eta$ of ★1 and $L = 1.0\times10^{6}\ \mathrm{m}$, compute the
diffusion time $L^2/\eta$ in years, and the free-decay time of the slowest
degree-1 mode, $L^2/(2\eta)$.

**★3.** For $U = 1.0\times10^{-3}\ \mathrm{m\,s^{-1}}$ and the $\eta$ and $L$ of
★★, compute $Rm$ and state which term of the induction equation dominates.

## ★★ Applied

**★★4.** The decay rate of degree $n$ is $n(n+1)\eta/L^2$. Compute the
free-decay times of the degree-1 and degree-2 modes for $L = 2.10\times10^{6}\
\mathrm{m}$ and $\eta = 1.5915\ \mathrm{m^{2}\,s^{-1}}$, and say which is longer.

**★★5.** For the two-by-two mean-field system with decay rate
$k = 2.2778\times10^{-5}\ \mathrm{yr^{-1}}$ and $\alpha = 3.22\times10^{-5}\
\mathrm{yr^{-1}}$, find the value of $\omega$ at the critical dynamo number, and
the growth rate for $\omega$ twice that value.

**★★6.** For $B = 5.0\times10^{-4}\ \mathrm{T}$, $L = 2.0\times10^{6}\
\mathrm{m}$ and $\sigma = 1.0\times10^{5}\ \mathrm{S\,m^{-1}}$, compute the
magnetic energy of the sphere, the characteristic current density, the ohmic
dissipation, and the ratio of energy to dissipation in years.

## ★★★ Research-oriented

**★★★7.** Design a time-dependent dynamo experiment: a quenching law of your
choice, a target field strength, and a requirement that the field reach within
10% of saturation in $10^{9}$ yr. Specify the supercriticality $D - 1$ needed,
the numerical scheme, and the unit test that would show the integrator is
converged. A specification that could not be executed is a failed answer.

**★★★8.** Show algebraically that the ratio of magnetic energy to ohmic
dissipation in this lesson is identically $L^{2}/(2\eta)$ for the assumed
$J \sim B/(\mu_0L)$, and explain why a quantity that is an identity cannot be used
as independent evidence for the dynamo.
