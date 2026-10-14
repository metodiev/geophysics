# Exercises — 06-09-01 Acoustic Impedance, Reflection Coefficients and the Convolution Model

Attempt these before reading the
[solutions](./01-reflection-principle-solutions.md). The lesson is
[01 Reflection Principle](../01-reflection-principle.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute the acoustic impedance and the normal-incidence reflection
coefficient for $\rho_1 = 2.10\ \mathrm{g\,cm^{-3}}$,
$v_1 = 2.40\ \mathrm{km\,s^{-1}}$ over
$\rho_2 = 2.40\ \mathrm{g\,cm^{-3}}$, $v_2 = 2.80\ \mathrm{km\,s^{-1}}$, and
state the polarity in words.

**★2.** For the demonstration's model, compute the two-way time to the base of
layer 1 ($h = 0.60\ \mathrm{km}$, $v_p = 2.20\ \mathrm{km\,s^{-1}}$) and to the
base of layer 2 ($h = 0.40\ \mathrm{km}$, $v_p = 2.80\ \mathrm{km\,s^{-1}}$),
and compare with the printed values.

**★3.** State the units of $Z = \rho v$ when $\rho$ is in
$\mathrm{g\,cm^{-3}}$ and $v$ in $\mathrm{km\,s^{-1}}$, and show by dimensional
analysis that $R$ is dimensionless.

## ★★ Applied

**★★4.** Derive $T = 2Z_2/(Z_1+Z_2)$ from pressure and particle-velocity
continuity, then verify $1+R = T$ numerically at the demonstration's interface 2
($Z_1 = 6.440$, $Z_2 = 7.840$ in the lesson's units) and at the model's own
values (interface 2 has $R = +0.0980$).

**★★5.** A two-way time of $1.60\ \mathrm{s}$ is measured to a target. Using the
demonstration's overburden (layer 1: $2.20\ \mathrm{km\,s^{-1}}$,
$0.60\ \mathrm{km}$; layer 2: $2.80\ \mathrm{km\,s^{-1}}$, $0.40\ \mathrm{km}$;
layer 3: $3.20\ \mathrm{km\,s^{-1}}$, $0.50\ \mathrm{km}$; below that
$3.60\ \mathrm{km\,s^{-1}}$), compute the target depth. Then compute the depth
that a single average velocity of $3.00\ \mathrm{km\,s^{-1}}$ would give, and
state the error.

**★★6.** The demonstration shows that a layer with
$v = 3.08\ \mathrm{km\,s^{-1}}$, $\rho = 2.091\ \mathrm{g\,cm^{-3}}$ has the same
impedance as one with $v = 2.80\ \mathrm{km\,s^{-1}}$,
$\rho = 2.30\ \mathrm{g\,cm^{-3}}$. Verify the impedance equality numerically,
then find a third member of the family with $\rho = 2.00\
\mathrm{g\,cm^{-3}}$ and confirm that $R$ at the interface above it is unchanged.

## ★★★ Research-oriented

**★★★7.** A colleague claims that a two-interface model can be replaced by an
equivalent one-interface model "because the convolution is linear". State
precisely what can and cannot be preserved by such a replacement, and give the
one situation in which two primaries *can* be collapsed into a single arrival
with no loss — including the condition on the wavelet.

**★★★8.** The lesson shows that normal-incidence data cannot separate velocity
from density. Design a measurement that breaks that degeneracy, state the
physically independent quantity it measures, and say what else must be known for
the separation to be quantitative.
