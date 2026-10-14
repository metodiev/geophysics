# Exercises — 23-05-04 Calibration, Testing and Traceability

Attempt these before reading the
[solutions](./04-calibration-and-testing-solutions.md). The lesson is
[04 Calibration and Testing](../04-calibration-and-testing.md). All values are
**SYNTHETIC**.

Use the demonstration's five-point calibration. The fitted line is
$y = 0.099970\,x + 0.027000$ with residuals $+0.0260$, $-0.0410$, $+0.0120$,
$-0.0050$, $+0.0080$ value units at raw readings 100…500.

## ★ Foundational

**★1.** Compute $\sum r_i^{2}$, the RMS residual with $n = 5$ and the residual
standard deviation with $n-2 = 3$ degrees of freedom. State the ratio of the two, and
which one enters the parameter uncertainties.

**★2.** With $\hat\sigma = 0.02938$, $\bar x = 300$, $\sum(x_i-\bar x)^{2} = 100\,000$
and $n = 5$, compute $\mathrm{se}(a)$, $\mathrm{se}(b)$ and the relative scale
uncertainty $\mathrm{se}(a)/a$ for $a = 0.099970$. Report the relative figure as a
percentage to three significant figures.

## ★★ Applied

**★★3.** A budget has four independent components: fit residual 0.02938, reference
standard 0.02000, check repeatability 0.01000 and drift since calibration 0.00500
value units. Compute the quadrature total and each component's share of the *variance*.
State which component you would attack first and one concrete way to attack it.

**★★4.** A device drifts at 0.005 value units per day and the acceptance tolerance is
0.05. Compute the re-calibration interval. Then compute the drift rate that would be
needed to justify a 30-day interval at the same tolerance, and state the single
measurement that establishes the drift rate you are using.

## ★★★ Research-oriented

**★★★5.** The five-point calibration above gives a scale uncertainty of 0.0929 %. The
instrument is a magnetometer whose raw reading is in counts with $a = 0.1$ nT per
count, and a survey requires 0.5 nT *relative* accuracy between stations where the
field is about 50 000 nT.

(a) compute the field error contributed by the present scale uncertainty;
(b) compute the factor by which the relative scale uncertainty must improve;
(c) compute the residual scatter $\hat\sigma$ that would be needed at the present
calibration span, and the span increase needed at the present $\hat\sigma$;
(d) state which of the two routes (c) you would actually take, and why the *design*
of the survey is a better answer than either.

**★★★6.** Specify the acceptance tests for a 12-channel logger that will record
three-component geophones for six weeks. State, for each test, what it verifies, the
signal used, the metric with units, the moment it is performed, and the failure
threshold. Include at least one test that the calibration itself does not cover, and
state two systematic errors that your test set cannot detect.
