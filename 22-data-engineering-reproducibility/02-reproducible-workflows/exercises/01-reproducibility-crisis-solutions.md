# Solutions — 22-02-01 The Reproducibility Problem in the Computational Sciences

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [01 The Reproducibility Problem](../01-reproducibility-crisis.md).

---

## ★1 — Classifying the failures

(a) **Repeatability**, category 5 (uncontrolled randomness): the same team on the
same setup obtains a different number because the seed is not recorded.

(b) **Reproducibility**, category 3 (environment drift): a different team on the
same intended setup obtains a different number because the dependencies resolved
to a different set.

(c) **Replicability**, category 6 (the claim exceeds the evidence, here in its
legitimate form): a different team, different setup and different data find a
weaker effect, which is a statement about the world rather than about the code.
Note that (a) and (b) are failures and (c) is an observation.

## ★2 — Power at $\delta = 0.4$

$$\text{power} = \Phi\!\left(0.4\sqrt{n} - 1.959964\right).$$

- $n = 20$: $0.4 \times 4.4721 = 1.7889$; $1.7889 - 1.95996 = -0.1711$;
  $\Phi(-0.1711) = 0.4321$ → **0.432**.
- $n = 50$: $0.4 \times 7.0711 = 2.8284$; minus 1.95996 = $0.8684$;
  $\Phi(0.8684) = 0.8074$ → **0.807**.
- $n = 100$: $0.4 \times 10 = 4.0$; minus 1.95996 = $2.0400$;
  $\Phi(2.0400) = 0.9793$ → **0.979**.

The expected replication rate of a significant result equals the power when the
true effect is the same in both studies: **0.432**, **0.807** and **0.979**
respectively.

## ★3 — The $n = 30$, $\delta = 0.5$ row

Power $= \Phi(0.5\sqrt{30} - 1.95996) = \Phi(0.7785) = 0.7819$ → printed 0.782.
Significant studies out of 20 000: **15 707** (printed), i.e. 78.5 % of the
simulated studies, consistent with the power within Monte Carlo error
($\sqrt{0.782 \times 0.218/20000} = 0.0029$, so $0.782 \pm 0.003$). Measured
replication rate: **0.781** (printed).

The agreement is expected: the significant subset is the studies whose noise
draw exceeded the threshold, and the replication is an independent draw from the
same distribution with the same true effect, so its probability of exceeding the
threshold again is exactly the power.

## ★★4 — Sample size for 80 % power at $\delta = 0.3$

$$z_{1-\alpha/2} + z_{0.80} = 1.959964 + 0.841621 = 2.801585,$$
$$\sqrt{n} = \frac{2.801585}{0.3} = 9.3386
\;\Longrightarrow\;
n = 87.2 \;\Longrightarrow\; 88 \ \text{observations}.$$

Check by evaluating the power function: at $n = 88$,
$0.3\sqrt{88} - 1.95996 = 2.8138 - 1.95996 = 0.8538$ and
$\Phi(0.8538) = 0.803$ ✔ (80.3 %).

Consistency check from the demonstration's tables: at $\delta = 0.2$, $n = 100$
gives power 0.516 and $n = 196$ gives 0.80, i.e. $n\delta^2 = 100 \times 0.04 =
4.0$ and $196 \times 0.04 = 7.84$; for $\delta = 0.3$ the answer must satisfy
$n\delta^{2} = 88 \times 0.09 = 7.92$, matching the 7.84 needed at 80 % power for
the 0.2 case (the small difference is the $n = 87.2$ exact value against the
rounded $n = 88$). The lesson's rule is therefore
$n \approx (2.8016/\delta)^{2}$, i.e. $n\delta^{2} \approx 7.85$.

## ★★5 — Direction of a winner's curse

The reported value is more likely to **over-state** the true effect: among studies
selected for significance, the favourable noise draws are over-represented, so
the conditional mean of $|\hat\delta|$ exceeds $\delta$. From the lesson's table,
an inflation factor of 1.387 corresponds to 52 % power and 1.137 to 78 % power;
50 % power is closest to the 1.2 factor asked about, so a reported 0.6 corresponds
to a true effect near

$$\delta_{\text{true}} \approx \frac{0.6}{1.2} = 0.50\ (\text{in units of } \sigma).$$

The estimate is crude by construction: the inflation factor depends on the
power, and the lesson's factors were measured for specific $(n, \delta)$ pairs, so
the statement to defend is the direction and the order of magnitude (a true
effect of about 0.5 with an uncertainty of a few tenths), not the second decimal.

## ★★6 — Expected false discoveries among 15 tests

Inputs: the number of tests ($m = 15$), the per-test level ($\alpha = 0.05$) and
the prior fraction of true effects ($\pi_1 = 2/15 = 0.133$). Assuming full power
for the true effects:

- expected false positives $= (1 - \pi_1)\,m\,\alpha = 13 \times 0.05 = 0.65$;
- expected true positives $= \pi_1 m = 2$;
- expected significant results $= 2.65$;
- mean false discovery proportion $= 0.65 / 2.65 = 0.245$.

So about **0.65 of the three reported discoveries are expected to be false**, and
roughly **25 %** of the reported set would be expected to be false under this
model — with the caveat that with only three observed discoveries the
uncertainty on that fraction is very large (a binomial count of 3). The estimate
depends on (i) the prior $\pi_1$, which the authors' belief supplies and which a
reader cannot check, and (ii) the assumption of full power, which flatters the
true effects: at 50 % power the true positives drop to 1 and the FDP rises to
0.65/1.65 = 0.394.

## ★★★7 — Designing the replication study

**Sample size.** For 90 % power at $\delta = 0.3$:
$n = ((1.959964 + 1.281552)/0.3)^{2} = (3.241516/0.3)^{2} = 10.8051^{2} =
116.75 \to 117$ observations. (Check: $0.3\sqrt{117} - 1.95996 = 3.2450 -
1.95996 = 1.2850$, $\Phi = 0.9006$ ✔.)

**Pre-registered decision rule.** A two-sided test at $\alpha = 0.05$ on the same
effect measure, with the direction, the estimator and the exclusion rules fixed
before data collection. Report the effect estimate with its 95 % confidence
interval and the test decision, and record the sample size in advance because
optional stopping destroys the level.

**Prediction for the replication's effect.** The original 0.3 was selected for
having been significant. If the original study had 50 % power, the lesson's table
suggests its reported value is inflated by a factor of about 1.2, so the
*replication* should be expected to find roughly $0.3/1.2 = 0.25$ rather than
0.3 — i.e. the correct prediction is a **smaller** effect, and the confidence
interval of the replication should be centred there, not on the published value.
If the original had high power the factor is near 1 and 0.3 is the right target.

**If the replication is not significant.** Report: the replication's own estimate
and interval; the difference from the original and whether that difference is
larger than sampling error; the power of the replication and the power of the
original (if it can be reconstructed); and the conclusion that the evidence for
the effect is weaker than the original paper implied. Do **not** report "failure
to replicate" as proof of absence: at 90 % power a null result is informative,
but the correct object of the inference is the combined evidence, not a verdict
on the original authors.

## ★★★8 — FDP as a function of level, number of tests and prior

Let $m$ tests, prior fraction $\pi_1$ truly non-zero, per-test level $\alpha$
and power 1 for the true effects (a simplification). Then

$$\text{E}[\text{false positives}] = (1-\pi_1)\,m\,\alpha, \qquad
\text{E}[\text{true positives}] = \pi_1 m,$$

$$\text{FDP}(\alpha, m, \pi_1) = \frac{(1-\pi_1)\alpha}
{(1-\pi_1)\alpha + \pi_1}.$$

Note that $m$ cancels: the *expected proportion* of false discoveries depends on
the level and the prior, not on how many hypotheses were tested — the number of
tests enters only through the variance of the realised proportion. Setting
$\text{FDP} = 0.20$ with $\alpha = 0.05$:

$$0.05(1-\pi_1) = 0.20\,[0.05(1-\pi_1) + \pi_1]$$
$$0.04(1-\pi_1) = 0.20\,\pi_1
\;\Longrightarrow\;
0.04 = \pi_1(0.20 + 0.04)
\;\Longrightarrow\;
\pi_1 = 0.16\bar{6}.$$

So a prior of about **17 %** of tested hypotheses being truly non-zero is needed
for the mean false discovery proportion to fall below 0.20 at $\alpha = 0.05$ with
full power. Sparse, exploratory searches (small $\pi_1$) therefore need either a
lower per-test level or an explicit correction; that is exactly the content of a
false-discovery-rate procedure.

## ★★★9 — Measuring the repeatability of a group's pipelines

**Statistic.** The **coefficient of variation across repeated runs** of each
pipeline's headline number, and the **bitwise-equality rate** of the output files.
Repeatability is the weakest of the three claims and the only one a single group
can measure against its own infrastructure.

**Protocol and number of runs.** For each of $k$ representative pipelines, run it
$R$ times from a clean checkout on the same machine, recording (i) whether the
output files are byte-identical and (ii) the relative difference of the
headline scalar. Choose $R$ so that a repeatability defect with probability $p$
is detected with 95 % confidence: $R > \log(0.05)/\log(1-p)$; for $p = 0.1$,
$R \gtrsim 29$, so use $R = 30$ per pipeline. Report the fraction of pipelines
with byte-identical outputs and, for the rest, the size of the variation in
relative terms.

**Confounder.** The **machine and its scheduler**: thread counts, BLAS
implementations and the number of MPI ranks change the last bits of floating-point
sums (the container demonstration measures a relative difference of
$1.04\times10^{-7}$ between float32 and float64 accumulation of a million
samples). A pipeline can therefore fail byte-equality for reasons that have
nothing to do with its own design, and a measurement that does not pin the
machine reports the host, not the pipeline. Pin the environment and record the
thread count before interpreting any failure.

**What it cannot tell you.** Repeatability says nothing about correctness: a
pipeline that always produces the same number, and whose formula is wrong,
has perfect repeatability and a wrong result. Correctness needs a comparison
against an independent reference — an analytic solution, a published benchmark or
a second implementation — which is the subject of module 22-07.
