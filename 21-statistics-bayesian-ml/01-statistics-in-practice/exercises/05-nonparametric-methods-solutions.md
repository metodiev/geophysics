# Solutions — 21-01-05 Nonparametric Statistics and Kernel Density Estimation

> Read after attempting. Lesson:
> [05 Nonparametric Methods](../05-nonparametric-methods.md). Numbers quoted
> from the demonstration reproduce its output.

---

## ★1 — ECDF variance and the DKW band

$$\operatorname{Var}\hat F_n(x) = \frac{F(1-F)}{n} = \frac{0.4\times0.6}{200}
= 0.0012, \qquad \mathrm{sd} = \sqrt{0.0012} = 0.03464 .$$

The DKW bound $P(\sup_x|\hat F_n - F| > \varepsilon) \le 2e^{-2n\varepsilon^{2}}$
gives, on setting the right-hand side to $2e^{-2}$ (so $n\varepsilon^{2} = 1$),
$\varepsilon = 1/\sqrt{200} = 0.0707$. The sup-distance is thus about
$0.071$ at that confidence — twice the pointwise standard error, which is the
price of the uniform statement.

---

## ★2 — Mann-Whitney normal approximation

$$\mathbb E[U] = \frac{n_1 n_2}{2} = \frac{40\times40}{2} = 800 ,$$

$$\operatorname{sd}(U) = \sqrt{\frac{n_1 n_2 (n_1+n_2+1)}{12}}
= \sqrt{\frac{40\times40\times81}{12}} = \sqrt{10800} = 103.92 ,$$

$$z = \frac{678.0 - 800}{103.92} = -1.174 .$$

Two-sided $p = 2(1-\Phi(1.174)) = 2\times0.1202 = 0.2404$, against the
demonstration's exact $0.2423$. The difference is the normal approximation's
error at $n_1 = n_2 = 40$; it is small enough that the conclusion is unchanged
in either case.

---

## ★3 — Exact sign test

Under the null $X \sim \mathrm{Binomial}(30, 1/2)$. The two-sided $p$-value is
$2\,P(X \ge 15)$, but since the distribution is symmetric and $15$ is the
median outcome, $P(X\ge15) = 0.5 + \tfrac12 P(X = 15)$:

$$P(X = 15) = \binom{30}{15}2^{-30} = 155\,117\,520 \times 9.3132\times10^{-10}
= 0.14446 ,$$

$$P(X \ge 15) = 0.5 + 0.07223 = 0.57223, \qquad
p = \min(1,\ 2\times0.57223) = 1.0000 .$$

This is the demonstration's value exactly: $15$ of $30$ is the least surprising
possible outcome under the null, so the test cannot reject, whatever the
magnitudes of the differences were.

---

## ★★4 — Wilcoxon signed-rank normal approximation

$$\mathbb E[W^{+}] = \frac{n(n+1)}{4} = \frac{30\times31}{4} = 232.5 ,$$

$$\operatorname{Var}(W^{+}) = \frac{n(n+1)(2n+1)}{24}
= \frac{30\times31\times61}{24} = 2363.75, \qquad \mathrm{sd} = 48.62 .$$

$$z = \frac{226.0 - 232.5}{48.62} = -0.134, \qquad
p = 2(1-\Phi(0.134)) = 2\times0.4467 = 0.893 .$$

The demonstration prints $0.9032$; the small gap is the continuity correction
(using $226.5$ or $225.5$ in the numerator moves $z$ by $\pm0.010$, and a
$t$-like approximation is used by `scipy`). The conclusion — no evidence of a
shift — is identical.

---

## ★★5 — Bandwidth rules

$$n^{-1/5} = 200^{-0.2} = e^{-1.05966} = 0.34657 .$$

Silverman:

$$h = 1.06 \times \min\Big(s,\ \frac{\mathrm{IQR}}{1.349}\Big) \times n^{-1/5}
= 1.06 \times 1.663 \times 0.34657 = 0.6110 ,$$

the printed $0.6108$ (the last digit is the precision of $s$). The $\min$
selected the **standard deviation**: for this bimodal sample the interquartile
range divided by $1.349$ is slightly larger than $s$, so the scale-outlier
protection of the rule never engages.

Scott:

$$h = s\,n^{-1/5} = 1.663 \times 0.34657 = 0.5764 ,$$

the printed $0.5762$. Scott's rule is Silverman's with the $1.06$ factor
dropped, which makes it about $6\ \%$ narrower here — the two estimates of the
same curve differ by a visibly different trough depth in the demonstration's
table.

---

## ★★6 — Optimal bandwidth

Write $\mu_2 = \int u^{2}K\,\mathrm du$, $R_K = \int K^{2}\,\mathrm du$ and
$R_{f''} = \int (f'')^{2}\,\mathrm dx$. Then

$$\mathrm{MISE}(h) \approx \frac{h^{4}}{4}\mu_2^{2}R_{f''} + \frac{R_K}{nh} .$$

Differentiate and set to zero:

$$\frac{d}{dh}: \quad h^{3}\mu_2^{2}R_{f''} - \frac{R_K}{nh^{2}} = 0
\;\Longrightarrow\;
h^{5} = \frac{R_K}{n\,\mu_2^{2} R_{f''}} ,$$

$$h_{\text{opt}} = \left(\frac{R_K}{\mu_2^{2} R_{f''}}\right)^{1/5} n^{-1/5} .$$

The exponent is $n^{-1/5}$, the slow nonparametric rate. For the Gaussian kernel,
$\mu_2 = 1$ and
$R_K = \int (2\pi)^{-1/2}e^{-u^{2}/2}\,\mathrm du \cdot \ldots = (4\pi)^{-1/2} =
0.28209$, so

$$h_{\text{opt}} = \left(\frac{0.28209}{R_{f''}}\right)^{1/5} n^{-1/5} .$$

Everything unknown is in $R_{f''}$. Silverman's and Scott's rules replace it by
the Gaussian-reference value: for $f = \mathcal N(0,\sigma^{2})$,
$R_{f''} = 3/(8\sqrt\pi\,\sigma^{5}) = 0.2116/\sigma^{5}$, and substituting gives
$h = 1.06\,\sigma\,n^{-1/5}$ — Scott's rule, up to the constant. The
$1.06\,\min(s, \mathrm{IQR}/1.349)$ variant of Silverman is a guard against the
Gaussian reference understating the spread of a heavy-tailed sample.

---

## ★★★7 — Power study of three two-sample tests

**Design.** Independent groups of $n_1 = n_2 = 40$ draws from
$\mathcal N(0,1)$ and $\mathcal N(\delta, 1)$; for each contamination fraction
$f \in \{0, 0.05, 0.1, 0.2, 0.3\}$ replace $\lceil f n_2\rceil$ values in group
2 with $+8$. Tests: Welch $t$, Mann-Whitney, and a permutation test with
$B = 2000$ shuffles. Shifts $\delta \in \{0, 0.25, 0.5, 0.75, 1.0\}$.

**Replicate count.** A power estimate has standard error
$\sqrt{p(1-p)/M}$; resolving a $5\ \%$ difference near $p = 0.5$ needs
$\sqrt{0.25/M} = 0.025$, i.e. $M = 400$; use $M = 2000$ to keep the Monte-Carlo
noise well below the effect being studied.

**Predictions.** At $f = 0$ all three have the nominal $5\ \%$ size and the
$t$ test is the most powerful by a few per cent (it is the exact optimal test
under the Gaussian alternative). At $f = 0.3$ the $t$ test's **size** departs
from $5\ \%$ — its type-I error inflates to roughly $20\ \%$–$35\ \%$ because
the five shifted values move the mean and the variance — while Mann-Whitney and
the permutation test (on the mean statistic they would also break; on the rank
statistic permutation is identical to Mann-Whitney) retain their level. The
study's headline number is the empirical size at $\delta = 0$ as a function of
$f$; a test that is not correctly sized cannot be compared on power.

---

## ★★★8 — Cross-validated bandwidth selection for a bimodal sample

**Candidate grid.** $h \in \{0.05, 0.10, \dots, 1.50\}$ — 30 values, fine enough
that the selected $h$ is not grid-limited.

**Criterion.** Likelihood cross-validation: for each $h$, maximise

$$\mathrm{LCV}(h) = \frac1n\sum_{i=1}^{n}\ln \hat f_{-i}(x_i; h),$$

the leave-one-out log-density of each point under the estimate built from the
other $n-1$ points. Equivalently, use the least-squares cross-validation score
$\int \hat f^{2} - \frac{2}{n}\sum_i \hat f_{-i}(x_i)$.

**Selection.** Take the $h$ maximising $\mathrm{LCV}$; repeat over 50 bootstrap
replicates of the sample to obtain a distribution of selected $h$.

**Failure diagnostic.** LCV is known to under-smooth on multi-modal data: the
selected $h$ will typically be **smaller** than the MISE-optimal value. Detect it
by computing, on the replicates, the number of modes of the selected estimate
and the depth of the trough between the two true modes. If the selected estimate
has more than two modes in a majority of replicates, or a trough deeper than,
say, $20\ \%$ of the peak, LCV has under-smoothed and the honest response is to
report the *bandwidth-averaged* density (an ensemble of estimates over a range
of $h$) rather than a single curve.
