# Exercises — 21-09-01 Statistical Reproducibility, p-Hacking and Multiple Comparisons

Attempt these before reading the
[solutions](./01-reproducibility-statistical-solutions.md). The lesson is
[01 Reproducibility](../01-reproducibility-statistical.md). All numbers are
**SYNTHETIC**, printed by
[`code/reproducibility_statistical_demo.py`](../code/reproducibility_statistical_demo.py).

Measured: 20 null tests per experiment, 4000 experiments, $\alpha = 0.05$;
uncorrected family-wise rate $0.6280$ (analytic $0.6415$), Bonferroni $0.0410$,
Benjamini-Hochberg $0.0425$. With 5 true alternatives (mean $z = 2.5$, 400
experiments): Bonferroni power $0.292$, $0.05$ false discoveries per experiment,
FDR $0.033$, $1.51$ findings per experiment; BH power $0.413$, $0.14$ false
discoveries, FDR $0.066$, $2.21$ findings. Optional stopping with five looks:
rate $0.1485$, inflation $2.97\times$, mean reported effect $0.3724\sigma$ under the
null.

## ★ Foundational

**★1.** Compute the analytic family-wise error rate $1-(1-\alpha)^m$ for
$m = 5, 20, 100$ at $\alpha = 0.05$, and compute the number of tests at which the
rate exceeds 0.5.

**★2.** Apply Benjamini-Hochberg at $q = 0.05$ by hand to the ten $p$-values
$0.001, 0.008, 0.039, 0.041, 0.042, 0.060, 0.074, 0.205, 0.212, 0.216$. State the
number of rejections and compare with what Bonferroni would reject.

**★3.** Compute the probability that at least one of five *independent* looks
exceeds the nominal 0.05, and compare it with the measured $0.1485$. State what the
difference tells you about the dependence between looks.

## ★★ Applied

**★★4.** Derive the expected number of false discoveries and the false discovery
rate for a procedure that rejects everything with $p \le \alpha$, when $m_0$ of the
$m$ hypotheses are null. Evaluate it for $m = 20$, $m_0 = 15$, $\alpha = 0.05$, and
state what the number means for a literature.

**★★5.** Write the pre-analysis plan for a study that will test for a precursory
signal at 40 stations, with two candidate windows and three magnitude thresholds.
State the hypotheses and their number, the primary specification, the correction,
and the one decision that most needs pre-specification.

**★★6.** A monitoring network computes a correlation between a geophysical
parameter and an outcome at 200 station pairs. Using the measured family-wise
behaviour, state the corrected threshold, the number of stations you would need to
see a signal at 0.001 uncorrected for it to survive the correction, and the
alternative that you would prefer to the correction.

## ★★★ Research-oriented

**★★★7.** Design the simulation that measures how the correlation between tests
changes the Bonferroni and BH error rates. State the generator, the sweep, the
metric, and the predicted direction for each procedure.

**★★★8.** Design a sequential monitoring scheme with a stated spending function.
State the statistic, the boundary, the frequency of looks, the false-alarm
contract, and how the boundary changes if the looks are added after the fact.

**★★★9.** Design the audit of a published claim of a significant relationship in a
multi-station study. List the five quantities you would request and, for each, the
reply that would change your assessment.
