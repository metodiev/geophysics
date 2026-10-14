# Exercises — 14-03-01 Porosity-Permeability and Kozeny-Carman Relations

Attempt these before reading the
[solutions](./01-porosity-permeability-relations-solutions.md). The lesson is
[01 Porosity-Permeability and Kozeny-Carman Relations](../01-porosity-permeability-relations.md).
All models are **SYNTHETIC** teaching values. Use
$\tau = 2.5$ ($c_K = 5$) unless the question says otherwise, and
$S_0 = 6/d$ for spheres.

## ★ Foundational

**★1.** A synthetic sand has $\phi = 0.20$ and $d = 0.15\ \mathrm{mm}$. Compute
$S_0$, the hydraulic radius $R_h$ and the Kozeny–Carman permeability. Report $k$
in $\mathrm{m^{2}}$ and in millidarcy.

**★2.** Convert the permeability of ★1 to hydraulic conductivity for water at
$20\ ^\circ\mathrm{C}$ ($\rho = 998.2\ \mathrm{kg\,m^{-3}}$,
$\mu = 1.002\times10^{-3}\ \mathrm{Pa\,s}$). Report it in $\mathrm{m\,s^{-1}}$ and
in $\mathrm{m\,d^{-1}}$.

**★3.** State the unit of every factor in
$k = \phi^{3}/(c_K S_0^{2}(1-\phi)^{2})$ and verify by dimensional analysis that
the right-hand side has units of $\mathrm{m^{2}}$.

## ★★ Applied

**★★4.** Derive $\mathrm{d}\ln k/\mathrm{d}\phi$ for Kozeny–Carman and evaluate
it at $\phi = 0.30$. By what percentage does $k$ change for an absolute porosity
error of $0.01$? Compare with the value at $\phi = 0.25$ given in the lesson and
explain the trend.

**★★5.** Two synthetic samples both have $k = 5.0\times10^{-13}\ \mathrm{m^{2}}$.
One has $\phi = 0.18$ and the other $\phi = 0.28$. Compute the grain diameter KC
requires for each, and state which of the two is more plausible for a
well-sorted sand and why.

**★★6.** The synthetic clayey-sand generator of the lesson gives, at
$\phi = 0.25$, $k_\text{true} = 2353.94\ \mathrm{mD}$ and
$k_\text{KC} = 6254.63\ \mathrm{mD}$. Compute the flow porosity $\phi_f$ that the
generator used, and verify that $\phi - \phi_f$ matches the generator's clay
rule $\phi_\text{clay} = \min(0.06, 0.35\phi)$.

**★★7.** A survey reports $k = 6.2\times10^{-12}\ \mathrm{m^{2}}$ with a stated
porosity of $0.25 \pm 0.012$ from resistivity. Compute the implied one-sigma
range of $k$ and state three assumptions in the quoted number that the error bar
does not include.

## ★★★ Research-oriented

**★★★8.** A fracture set has aperture $b = 50\ \mu\mathrm{m}$ and spacing
$s = 1.0\ \mathrm{m}$. **(a)** Derive $k = b^{3}/(12s)$ for a set of parallel
smooth fractures from the cubic law for a single fracture, stating each step.
**(b)** Compute $k$ and convert to millidarcy. **(c)** Compute what KC predicts
for the same rock using $\phi = b/s$ and $d = 0.15\ \mathrm{mm}$, and state the
mismatch as a factor. **(d)** Which number would you report, and what must be
stated with it?

**★★★9.** Design a calibration experiment for the Kozeny constant of a synthetic
medium whose grain size can be varied in three steps and whose porosity can be
set in three steps. **(a)** State the measurements, the plot and the fitted
quantity. **(b)** Explain why $c_K$ fitted on one grain size may not transfer to
another. **(c)** Specify one check that would reveal a failure of the KC form
itself rather than of the fit. A specification that could not be executed is a
failed answer.
