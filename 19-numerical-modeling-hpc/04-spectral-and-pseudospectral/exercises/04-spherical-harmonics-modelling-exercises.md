# Exercises — 19-04-04 Spherical Harmonic Modelling of Global Fields

Attempt these before reading the
[solutions](./04-spherical-harmonics-modelling-solutions.md). The lesson is
[04 Spherical Harmonic Modelling of Global Fields](../04-spherical-harmonics-modelling.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** State the minimum number of Gauss-Legendre latitude nodes and uniform
longitude samples needed to analyse a field band-limited to $L = 30$, and say
whether the requirement is approximate or exact.

**★2.** Compute the number of coefficients in a real spherical harmonic expansion
truncated at $L = 30$.

**★3.** State Parseval's identity in the fully normalised convention used in the
lesson, and state what a non-zero residual in it indicates.

## ★★ Applied

**★★4.** The lesson measures a degree-8 coefficient error of
$1.104\times10^{-1}$ at 8 latitude nodes and $6.1\times10^{-15}$ at 9. Explain why
the improvement is a jump rather than a gradual decay, and predict what 10 nodes
would give.

**★★5.** Compute the downward-continuation factor at $l = 50$, $100$ and $150$ for
$r/R = 1.03$, and the maximum usable degree for a target relative error of
$10^{-2}$ with a relative coefficient error of $10^{-5}$.

**★★6.** A model is truncated at $L = 50$ and a map is drawn from it. State what
the smoothness of the map demonstrates and what it does not.

## ★★★ Research-oriented

**★★★7.** A satellite field is measured at $r = 1.05R$ with a coefficient error
of $10^{-6}$ up to degree 200. Decide which degrees survive downward continuation
to the surface at a relative tolerance of $10^{-2}$, and state how much of the
original band is lost.

**★★★8.** Design a verification test for a spherical harmonic synthesis/analysis
pair that would detect (i) a wrong normalisation convention and (ii) too few
latitude nodes. State the metric and the expected outcome for each fault.
