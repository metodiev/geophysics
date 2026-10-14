# Exercises — 21-07-03 Statistical Spectral Analysis and Significance Testing

Attempt these before reading the
[solutions](./03-spectral-analysis-statistical-solutions.md). The lesson is
[03 Spectral Significance](../03-spectral-analysis-statistical.md). All numbers
are **SYNTHETIC**, printed by
[`code/spectral_analysis_statistical_demo.py`](../code/spectral_analysis_statistical_demo.py).

Measured: 400 AR(1) realisations with $\varphi = 0.80$, $n = 512$, 255 interior
frequencies, normalising spectrum spanning $80.8\times$; per-frequency level
$2.9957$; measured rate at a pre-specified frequency $0.030$ (MC error $0.011$);
rate for the maximum at that level $1.000$; empirical 95th percentile of the
maximum $8.658$; family-wise level $8.512$ with measured rate $0.060$.
Segment averaging with 4 segments of 128 samples: level $1.9384$, rate at a
pre-specified frequency $0.060$, rate for the maximum at the per-frequency level
$0.963$, family-wise level $3.3386$ with measured rate $0.037$, ordinate scatter
ratio $0.492$.

## ★ Foundational

**★1.** Derive $\Pr[R > -\ln\alpha] = \alpha$ for $R \sim \mathrm{Exp}(1)$ and
compute the level for $\alpha = 0.10$, $0.05$ and $0.01$.

**★2.** Compute the family-wise level for $m = 255$ at $\alpha = 0.05$ using both
the exact formula and the Bonferroni approximation $-\ln(\alpha/m)$, and state the
size of the discrepancy.

**★3.** For the averaged estimator, compute the ratio of the averaged
per-frequency level to the raw one, and compare it with the measured ratio of the
ordinate scatters. State whether the two are related or coincidental, and why.

## ★★ Applied

**★★4.** Show that the per-frequency level for a $\chi^2_\nu$ ordinate is
$\chi^2_\nu(1-\alpha)/\nu$, evaluate it for $\nu = 2$ and $\nu = 8$, and verify
against the printed levels.

**★★5.** A colleague finds the largest peak of a 512-sample record at
$R = 6.5$. Compute the significance of that peak under (a) the per-frequency test
and (b) the family-wise test, and state the conclusion in each case.

**★★6.** Design the experiment that determines how much of the spectrum's dynamic
range can be handled by a single constant normalisation before the false-alarm
rate departs from nominal. State the generator, the metric, the sweep and the
result that would set a practical rule.

## ★★★ Research-oriented

**★★★7.** Design a spectral detection procedure for a signal whose frequency is
believed to lie in a narrow band $[f_1, f_2]$ but is otherwise unknown. State the
statistic, its null distribution, the level, and how the answer changes if the
band is widened.

**★★★8.** Design the experiment that measures the false-alarm rate of a
multitaper estimator with $K$ tapers, and state how the effective number of
independent frequencies and the family-wise level depend on $K$.

**★★★9.** A published record shows a peak at a period of 100 ka in a
palaoeclimate proxy of length 200 samples. Specify the full analysis you would
require to evaluate the claim, including the null model, the estimator, the level,
and the two independent tests that would falsify a cyclostratigraphic
interpretation.
