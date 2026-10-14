# Exercises — 23-06-08 Laboratory Uncertainty Budgets and Reporting

Attempt these before reading the
[solutions](./08-lab-data-uncertainty-solutions.md). The lesson is
[08 Laboratory Uncertainty Budgets and Reporting](../08-lab-data-uncertainty.md). All values
are **SYNTHETIC**.

## ★ Foundational

**★1.** Convert to standard uncertainties: (a) a repeatability $s = 0.30$ from $n = 9$
repeats; (b) a calibration certificate with $U = 0.80$ at $k = 2$; (c) a resolution of 0.02
assumed rectangular; (d) a temperature coefficient of $\pm0.04$ assumed rectangular.

**★2.** Combine the four terms of ★1, compute $u_c$, $U$ at $k = 2$ and each term's variance
share.

## ★★ Applied

**★★3.** Compute the effective degrees of freedom for the combination of ★1, using
$\nu = 8$ for the Type A term and infinite degrees of freedom for the Type B terms, and state
the coverage factor you would actually use for a 95 % interval.

**★★4.** A porosity is $\phi = \Delta m/(\rho_w V)$ with $\Delta m = 4.20 \pm 0.015$ g,
$V = 18.44 \pm 0.030$ cm³ and $\rho_w = 0.998 \pm 0.0005$ g/cm³. Compute $\phi$, each term's
variance share, the combined relative uncertainty and $U$ in porosity points at $k = 2$.

**★★5.** Two laboratories report $12.40 \pm 0.05$ and $12.30 \pm 0.04$ for the same
property. Compute the difference, the combined standard uncertainty and $E_n$, state the
verdict, and state what you would do next.

## ★★★ Research-oriented

**★★★6.** A rock-physics dataset of 40 specimens must be published with porosity,
permeability, P- and S-velocity and thermal conductivity, each with a defensible uncertainty,
and a reviewer asks for one number per property with its basis.

Write the reporting specification: the uncertainty statement for each property (value, $U$,
$k$, $n$, the dominant term and the measurement conditions); the two properties whose budgets
are dominated by *preparation* rather than by the instrument, with the arithmetic that shows
it; the budget you would put in the data table's metadata; the inter-laboratory comparison
you would run and the $E_n$ acceptance criterion; and the one thing a reader cannot recover
from the published table, with the sentence you would add to prevent it.
