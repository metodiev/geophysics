# Exercises — 11-02-04 EM for Conductors, Massive Sulphides and Graphite

Attempt these before reading the
[solutions](./04-em-for-minerals-solutions.md). The lesson is
[04 EM for Minerals](../04-em-for-minerals.md). All resistivities, sizes,
conductances, overburden parameters and windows are **SYNTHETIC** teaching values.

Useful: $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$,
$\delta = \sqrt{2/(\omega\mu_0\sigma)}$,
$\tau = \mu_0\sigma a^{2}/\pi^{2}$.

## ★ Foundational

**★1.** Compute the skin depth at $50$ and $500\ \mathrm{Hz}$ in a body of
resistivity $2\ \Omega\,\mathrm{m}$ and in a host of $400\ \Omega\,\mathrm{m}$, and
state the ratio of the host's skin depth to the body's.

**★2.** Compute the time constant of a sphere of radius $80\ \mathrm{m}$ with
$\rho = 1.5\ \Omega\,\mathrm{m}$, and the frequency at which $\omega\tau = 1$.

**★3.** A sheet of thickness $15\ \mathrm{m}$ has $\sigma = 4\ \mathrm{S\,m^{-1}}$.
Compute its conductance in siemens, and compute the conductivity a
$3\ \mathrm{m}$ sheet would need for the same EM response.

**★4.** Compute the overburden screening factor $1+\mu_0\omega Sz/2$ for
$S = 8\ \mathrm{S}$, $f = 200\ \mathrm{Hz}$, $z = 150\ \mathrm{m}$.

## ★★ Applied

**★★5.** A late-time decay has a fitted time constant of $2.5\ \mathrm{ms}$ for an
assumed radius of $100\ \mathrm{m}$. Compute the implied conductivity and
resistivity, then repeat for assumed radii of $70$ and $140\ \mathrm{m}$, and state
the factor by which the inferred conductivity changes across that range.

**★★6.** Using the window-length results of the lesson, state the fitted time
constant you would expect from a power-law host response fitted by an exponential
over a quarter-decade window, and explain why reporting such a number as "the
target's time constant" is a specific, quantifiable error.

**★★7.** A target index has the form
$(a/z)^{3}e^{-2z/\delta}\frac{\omega\tau}{\sqrt{1+(\omega\tau)^{2}}}
\frac{1}{1+\mu_0\omega Sz/2}$. Compute the index at $100$ and $1000\ \mathrm{Hz}$
for a body with $a = 100\ \mathrm{m}$, $z = 200\ \mathrm{m}$,
$\rho_{\text{t}} = 1\ \Omega\,\mathrm{m}$, $\rho_{\text{host}} = 200\
\Omega\,\mathrm{m}$, $S = 0$, and state which frequency wins and why.

**★★8.** For the same body with $S = 15\ \mathrm{S}$, recompute both frequencies
and state whether the answer changes. Explain the competition in one sentence.

## ★★★ Research-oriented

**★★★9.** The conductance degeneracy is exact for a thin sheet. Design a survey
that measures $\sigma$ and $t$ separately, and state (a) the physical principle
that makes the separation possible, (b) the geometry, (c) the quantity you would
fit, and (d) the precision needed on that quantity for a stated
$(\sigma,t)$ resolution.

**★★★10.** For a *thin circular sheet* of radius $L$ and conductance $S$, the
diffusion problem has a different structure from a sphere (the governing
diffusivity is not $1/(\mu_0\sigma)$). Use dimensional analysis to show that the
time constant must have the form $\tau = c\,\mu_0 S L$ with $c$ dimensionless,
state the numerical procedure you would use to determine $c$, and explain why
this makes the sheet's time constant depend on its *size* rather than on its
conductivity alone.

**★★★11.** Two conductors lie 120 m apart within one transmitter footprint. Show,
with a computed example, how a single-exponential inversion of the composite decay
returns a plausible but wrong time constant, and specify the measurement that
would reveal the second body.
