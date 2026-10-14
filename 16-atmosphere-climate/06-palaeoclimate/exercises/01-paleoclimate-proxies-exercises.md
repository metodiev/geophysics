# Exercises — 16-06-01 Palaeoclimate Proxies: Ice Cores, Sediments, Isotopes

Attempt these before reading the
[solutions](./01-paleoclimate-proxies-solutions.md). Lesson:
[01 Palaeoclimate Proxies](../01-paleoclimate-proxies.md). All models and data
are **SYNTHETIC**. The demonstration is
[`../code/paleoclimate_proxies_demo.py`](../code/paleoclimate_proxies_demo.py).

## ★ Foundational

**★1.** A sample has an isotope ratio $R = 0.98\,R_{\text{std}}$. Compute its
$\delta$ value and state the unit.

**★2.** With $\delta_0 = -12.0$ per mil, $\alpha = 1.00953$ and $f = 0.5$,
compute $\delta_v$ and $\delta_c$ using the Rayleigh expressions, showing the
arithmetic.

**★3.** Verify the identity
$\delta_c-\delta_v = (\alpha-1)(\delta_v+1000)$ at $f = 0.5$ using your answers
to ★2 and state what the difference represents.

## ★★ Applied

**★★4.** Two calibrations have slopes $0.7863$ and $1.1329$ per mil per K, both
anchored at the same reference point. Compute the temperature difference between
them for a measured $\delta$ that is $10$ per mil below the reference value.

**★★5.** The demonstration measures a sensitivity of about
$8.33\ \mathrm{K}$ of implied temperature per per mil of source composition. If
the source composition is uncertain by $\pm1.5$ per mil, compute the implied
temperature uncertainty.

**★★6.** From the demonstration's cooling table, the $\delta$ change over
successive equal temperature steps ($292.0 \to 283.6 \to 275.1 \to 266.7 \to
258.2 \to 250.0\ \mathrm{K}$) is $-4.58$, $-5.48$, $-6.54$, $-7.80$ and
$-9.04$ per mil. Compute the ratio of the largest step to the smallest and state
the implication for a single linear calibration.

## ★★★ Research-oriented

**★★★7.** Design a calibration experiment that would reduce the structural
uncertainty of Section 5 of the lesson (the fractionation parameterisation).
State the independent information needed, how it would be used, and what
residual uncertainty would remain.

**★★★8.** A reconstruction quotes a temperature from a single isotope value with
a $\pm0.2\ \mathrm{K}$ uncertainty taken from the regression's standard error.
Write a critique listing the omitted terms in order of likely magnitude.
