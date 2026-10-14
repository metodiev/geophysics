# Exercises — 13-05-03 Benchmarking Geodynamic Codes

Attempt these before reading the
[solutions](./03-benchmarking-geodynamics-solutions.md). The lesson is
[03 Benchmarking Geodynamic Codes](../03-benchmarking-geodynamics.md) and its
numbers come from
[`code/benchmarking_geodynamics_demo.py`](../code/benchmarking_geodynamics_demo.py).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** State, in one sentence each, the difference between verification and
validation, and give one example of each that could be carried out for a
mantle-convection code.

**★2.** A quantity takes the values 5.31066, 4.97829 and 4.90191 on three grids
with $h = 0.058824$, 0.030303 and 0.020408. Compute the observed order $p$ and
state why the value may be noise rather than the formal order.

**★3.** Using the same three values and $p$ from ★2, compute the Richardson
extrapolation and the Grid Convergence Index with a safety factor of 1.25.

## ★★ Applied

**★★4.** The lesson measures $Nu$ at $Ra=10^{4}$ as 5.0799 ($N=24$), 4.9788
($N=32$) and 4.9015 ($N=48$), and finds an 8.338% deviation at $N=16$. Estimate
the grid error you would report for a result at $N=32$ and state the two
assumptions behind the estimate.

**★★5.** The same solution gives $Nu = 4.90191$ from the bottom flux and
$Nu = 4.63216$ from the volume average. Compute the relative difference and
explain which of the three error sources in the lesson's budget it exceeds.

**★★6.** A colleague's benchmark reports "$Nu$ within 0.5% of the reference".
Design one additional benchmark quantity that would test the interior field, and
explain why the Nusselt number alone is a weak constraint.

**★★7.** The measured critical Rayleigh number is 813.65, 799.39 and 791.69 at
$N = 24, 40, 64$ against $8\pi^4 = 779.27$. Compute the three errors and state
what a *non-monotonic* error sequence would have indicated.

## ★★★ Research-oriented

**★★★8.** An upwind run at $N=32$, $Ra=10^{4}$ reports $Nu$ values 3.138, 3.927,
2.343, 1.428, 3.375, 1.674 sampled every 1000 steps. Specify the additional
diagnostics and the decision rule you would use to decide whether the solution is
time-dependent (physically interesting) or numerically unstable (a defect).

**★★★9.** Design a two-code benchmark comparison that would be informative even
if both codes use the same discretisation family. State the quantities compared,
the tolerance, and why the comparison is not circular.

**★★★10.** The lesson concludes that a GCI of 1.389% understates the uncertainty
of a reported $Nu$ because the diagnostic definition contributes 5.503%. Write
the uncertainty statement you would publish for $Nu = 4.90$ at $Ra = 10^{4}$,
naming every contribution you include and every one you exclude, with a
justification for each exclusion.
