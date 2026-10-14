# Exercises — 08-05-02 Time-Domain EM (TDEM): Sounding, Transients and Decay Curves

Attempt these before reading the
[solutions](./02-time-domain-em-solutions.md). The lesson is
[02 Time-Domain EM (TDEM)](../02-time-domain-em.md). All models are **SYNTHETIC**
teaching values with $\mu_0=4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ exact.

## ★ Foundational

**★1.** A SYNTHETIC body has $\sigma=0.02\ \mathrm{S\,m^{-1}}$ and thickness
$d=30\ \mathrm{m}$. Compute $D=1/(\mu_0\sigma)$, $\tau_1$, $\tau_2$ and the
diffusion length $\sqrt{Dt}$ for $t=1\ \mathrm{ms}$. Show units throughout.

**★2.** Dimensional analysis: show that $\mu_0\sigma d^2$ is a time, and that
$\sqrt{Dt}$ is a length. What physical quantity has the units of $\sigma d$?

**★3.** A body is $200\ \mathrm{m}$ across with $\sigma=0.05\ \mathrm{S\,m^{-1}}$.
Using the slab eigenmode formula as a rough scale, compute $\tau_1$ and say
whether a system whose first usable channel is $50\ \mathrm{\mu s}$ after
switch-off could see it.

## ★★ Applied

**★4.** Derive $\tau_n=\mu_0\sigma d^2/(n^2\pi^2)$ by separation of variables,
stating the boundary conditions and how the initial condition enters only through
the mode amplitudes.

**★5.** A late-time decay gives $\tau=2.0\ \mathrm{\mu s}$. **(a)** Compute
$\sigma d^2$. **(b)** If the early-time amplitude implies a conductance
$\sigma d=0.20\ \mathrm{S}$, solve for $d$ and $\sigma$. **(c)** State, in one
sentence, what a late-time-only interpretation would have been able to say.

**★6.** The demonstration measures a decay constant of $0.5087\ \mathrm{\mu s}$
for a slab whose continuum eigenvalue is $0.5093\ \mathrm{\mu s}$. Attribute the
$0.13\%$ difference to a mechanism and justify the attribution with a number from
the lesson's convergence table.

## ★★★ Research-oriented

**★7.** Design a two-channel TDEM experiment to determine $\sigma$ and $d$
separately for a conductor of thickness between $20$ and $50\ \mathrm{m}$ and
conductivity near $0.01\ \mathrm{S\,m^{-1}}$, with a receiver noise floor of
$1\times10^{-4}$ of the early amplitude. Specify the transmitter timing, the
fitted channels, the noise-driven uncertainty on each parameter, and the largest
remaining source of error. Predict the outcome using the $\sigma d^2$ and
$\sigma d$ scalings.

**★8.** Section 4 gives the halfspace similarity solution for a uniform initial
field removed at the surface. That is a 1-D idealisation: a real TDEM loop
produces a *ring* of current whose maximum depth is often quoted as
$\sqrt{2t/(\mu_0\sigma)}$. Using only the diffusion equation and a scaling
argument — no new solution — decide whether the two scales can differ by more than
a factor of order unity, and state what measurement would settle it.
