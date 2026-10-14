# Exercises — 09-02-05 Electrical Resistivity Tomography (ERT) Acquisition and Design

Attempt these before reading the
[solutions](./05-ert-tomography-solutions.md). The lesson is
[05 ERT Acquisition and Design](../05-ert-tomography.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A line has 64 electrodes at 3.0 m spacing. Compute the line length and
the number of dipole-dipole measurements for $n = 1$ and $n = 6$.

**★2.** Using the scaling law, compute the DOI of $n = 4$ at $a = 4$ m.

**★3.** Compute $\Delta V$ for $n = 3$, $a = 2$ m at $\rho = 100\
\Omega\,\mathrm{m}$, $I = 0.1$ A, using $|k|/a = 188.4956$.

## ★★ Applied

**★★4.** With a 0.5 mV noise floor and a requirement of ten times the floor for
1% precision, determine the largest usable $n$ at $a = 2$ m for
$\rho = 30\ \Omega\,\mathrm{m}$ and for $\rho = 300\ \Omega\,\mathrm{m}$.

**★★5.** A target is 8 m deep and 6 m across in a $50\ \Omega\,\mathrm{m}$
ground. Compute the required spacing, the aperture, the footprint at the target
and the deepest-array signal at $I = 0.1$ A. State whether the target will be
resolved or only detected.

**★★6.** The lesson's coverage table gives a 90% coverage depth of 2.5 m for
$n = 1..2$ and 5.3 m for $n = 1..6$ with 41 and 123 measurements. Compute the
coverage depth per measurement for each design and comment on the marginal
return.

## ★★★ Research-oriented

**★★★7.** Design an ERT survey that resolves a 3 m thick conductive layer at
20 m depth to better than a factor 2 in thickness, in ground of
$150\ \Omega\,\mathrm{m}$, with a 0.5 mV noise floor. State the electrode
spacing, the minimum current (allowing 16-fold stacking), the line length, the
number of electrodes and the footprint; then state which of your numbers is the
binding constraint.

**★★★8.** The DOI in this module is defined from the cumulative $|s(z)|$. Show,
using the sign-change argument of [02](02-electrode-arrays-solutions.md), how the
DOI of a dipole-dipole array would change if $s(z)$ (not $|s|$) were used, and
why any published DOI number must always be quoted with its convention.
