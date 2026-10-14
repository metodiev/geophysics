# Exercises — 21-09-02 Honest Reporting of Uncertainty and Limitations

Attempt these before reading the
[solutions](./02-reporting-uncertainty-ethics-solutions.md). The lesson is
[02 Reporting Uncertainty](../02-reporting-uncertainty-ethics.md). All numbers are
**SYNTHETIC**, printed by
[`code/reporting_uncertainty_ethics_demo.py`](../code/reporting_uncertainty_ethics_demo.py).

Setup: true value $10.0$ mm; measurement scatter $0.5$ mm; $10$ observations per
estimate; statistical standard error $0.1581$ mm; nominal 95% half-width
$0.3099$ mm; unmodelled systematic offset $0.40$ mm ($2.53$ standard errors);
5 processing variants with a spread of $0.30$ mm.

| Protocol | Coverage | Mean reported | Bias |
|---|---|---|---|
| pre-specified, statistical only | $0.9511$ | $9.9986$ mm | $-0.0014$ mm |
| pre-specified, systematic ignored | $0.2837$ | $10.4005$ mm | $+0.4005$ mm |
| best of five variants | $0.4533$ | $10.3473$ mm | $+0.3473$ mm |

Combined standard uncertainty: $\sqrt{0.1581^2 + 0.40^2} = 0.4301$ mm, a factor of
$2.72$ above the statistical part.

## ★ Foundational

**★1.** Compute the combined standard uncertainty and the 95% half-width for the
three cases: statistical only, plus the systematic, and with the systematic doubled.
State how many significant figures the value supports in each case.

**★2.** Compute the statistical standard error for $n = 4$, $10$ and $40$
observations at $0.5$ mm scatter, and state at which $n$ the systematic offset stops
dominating the budget.

**★3.** Verify the coverage of $0.2837$ from the bias-to-standard-error ratio, using
the Gaussian tail, and state why the answer does not depend on the interval's width
once the ratio is fixed.

## ★★ Applied

**★★4.** The selection protocol's mean reported value is $+0.3473$ mm above the
truth with a half-width of $0.3099$ mm. Compute the coverage predicted from that
bias, compare with the measured $0.4533$, and state how the bias would grow with
$10$ variants.

**★★5.** Write the limitations paragraph for a study that reports $10.0$ mm with a
statistical-only interval, when the systematic term is unknown but bounded by an
intercomparison at $\pm0.5$ mm. State the quantity affected, the direction and the
size, and what would resolve it.

**★★6.** Design the intercomparison that would bound the systematic offset to
$\pm0.1$ mm. State the design, the number of comparisons needed, the metric and the
assumption it relies on.

## ★★★ Research-oriented

**★★★7.** Design a validation protocol that measures the coverage of a reported
interval in the field, where no truth is available. State the three substitutes for
the truth, what each can and cannot establish, and the coverage measurement each
supports.

**★★★8.** Design the experiment that measures how the selection effect depends on
the correlation between the variants tried and on the criterion used to choose among
them. State the generator, the sweep, the metric and the predicted direction for two
different criteria.

**★★★9.** A doctoral thesis reports fourteen results, each with a nominal 95%
interval, obtained from one data set with many specification choices. Specify the
analysis that decides whether the reported intervals are jointly credible,
including the statistic, the correction and the sensitivity to the number of
implicit specifications.
