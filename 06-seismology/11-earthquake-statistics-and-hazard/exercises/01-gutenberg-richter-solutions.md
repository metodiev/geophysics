# Solutions — 06-11-01 Gutenberg-Richter, b-Value and Magnitude of Completeness

> Read after attempting the exercises. Numbers were computed with the same
> formulas the demonstration uses, not estimated by hand. All values are
> **SYNTHETIC**.

Lesson: [01 Gutenberg-Richter](../01-gutenberg-richter.md).

---

## ★1 — b-value from a summary statistic

$$\hat b = \frac{\log_{10}e}{\bar m - (M_c - \Delta/2)}
= \frac{0.4343}{2.4821 - (2.0 - 0.05)} = \frac{0.4343}{0.5321} = 0.8162.$$

Standard error: $\hat b/\sqrt N = 0.8162/\sqrt{400} = 0.8162/20 = 0.0408$.

So $b = 0.82 \pm 0.04$. The unit of $b$ is "per magnitude unit"
(magnitudes$^{-1}$): it is a slope in $\log_{10}N$ against $m$.

---

## ★2 — the largest event in a sample

Expected largest event:

$$M_c + \frac{\log_{10}N}{b} = 1.5 + \frac{2.3979}{0.95} = 1.5 + 2.5241
= 4.024 \approx M\,4.0.$$

Probability of no event above $M\,5.0$:

$$P = \exp\!\big[-N\,10^{-b(m-M_c)}\big]
= \exp\!\big[-250\times10^{-0.95\times3.5}\big]
= \exp\!\big[-250\times10^{-3.325}\big].$$

$10^{-3.325} = 4.732\times10^{-4}$, so the exponent is
$-250\times4.732\times10^{-4} = -0.1183$ and

$$P = e^{-0.1183} = 0.888.$$

There is an 89% chance that a 250-event catalogue contains nothing above $M5.0$.
The parent law has no upper bound; the sample does.

---

## ★3 — moment and energy

$$M_0 = 10^{1.5\times5.6 + 9.1} = 10^{17.5} = 3.16\times10^{17}\ \mathrm{N\,m},$$
$$E = 10^{1.5\times5.6 + 4.8} = 10^{13.2} = 1.58\times10^{13}\ \mathrm{J}.$$

Per magnitude unit both scale as $10^{1.5} = 31.62$.

---

## ★4 — the direction of the $M_c$ bias

**(a)** At $M_c = 1.0$: $\bar m - (M_c - 0.05) = 1.3817 - 0.95 = 0.4317$,
$\hat b = 0.4343/0.4317 = 1.0059$. With $N = 5000$ the standard error is
$1.0059/\sqrt{5000} = 0.0142$, so this is $+0.42$ s.e. from 1.0000 — unbiased.

**(b)** At $M_c = 0.5$: $\bar m - (M_c - 0.05) = 1.3817 - 0.45 = 0.9317$,
$\hat b = 0.4343/0.9317 = 0.4661$, i.e. $-53.4\%$ of the true value.

**(c)** Assuming $M_c$ too low lowers the denominator $\bar m - (M_c-\Delta/2)$ but
does *not* add any new events, because the catalogue contains none below the true
$M_c$. The denominator therefore grows without bound as $M_c$ falls, and $b$ is
driven towards zero — a large, one-sided bias. Assuming $M_c$ too high raises the
denominator only slightly (the retained events have a mean barely above the new
threshold, since the exponential's mean is $M_c + 1/\beta$ and both shift
together), so the bias is small; the real cost is statistical, since $N$ falls
sharply (484 events at $M_c = 2.0$, 145 at $M_c = 2.5$) and the standard error
grows as $1/\sqrt N$.

---

## ★5 — is maximum curvature's b-value a fluctuation?

At the maximum-curvature estimate:

$$\hat b = 0.8662,\quad N = 15206,\quad
\hat\sigma_b = \frac{0.8662}{\sqrt{15206}} = \frac{0.8662}{123.31} = 0.00702.$$

The deviation from $b = 1.00$ is $0.1338$, i.e. $0.1338/0.00702 = 19$ standard
errors. This cannot be a fluctuation.

At the 99%-detection level:

$$\hat b = 0.9935,\quad N = 1851,\quad
\hat\sigma_b = \frac{0.9935}{\sqrt{1851}} = \frac{0.9935}{43.02} = 0.0231,$$

so the deviation $0.0065$ is $0.28$ standard errors — entirely consistent.

**Conclusion:** with >15000 events, a b-value built on the maximum-curvature $M_c$
is biased low by a systematic 13%, not scattered by noise; the bias belongs to the
completeness decision, not to the estimator.

---

## ★6 — sample size for a 10% b-difference

For two independent windows the difference has
$\sigma_{\Delta b} \approx b\sqrt{2/N}$. Requiring
$2\sigma_{\Delta b} \le 0.10\,b$:

$$2b\sqrt{\frac{2}{N}} \le 0.10\,b
\quad\Longrightarrow\quad
\sqrt{\frac{2}{N}} \le 0.05
\quad\Longrightarrow\quad
N \ge \frac{2}{0.05^2} = 800.$$

So **800 events above $M_c$ per region**, and that is before allowing for a
systematic contribution from $M_c$ or declustering. In most regions this is a
multi-decade catalogue requirement — which is why most reported 10% b-value
differences are not resolvable.

---

## ★7 — distribution and quantiles of the largest event

For independent events, each exceeding $m$ with probability
$p(m) = 1 - 10^{-b(m-M_c)}$:

$$P(M_{\max} < m) = \big[1 - p(m)\big]^{N}
\approx \exp\!\big[-N\,10^{-b(m-M_c)}\big]$$

(the approximation is excellent for the small probabilities involved).

Inverting: set $P(M_{\max}<m) = q$, so
$N10^{-b(m-M_c)} = -\ln q$ and

$$m_q = M_c + \frac{\log_{10}N - \log_{10}(-\ln q)}{b}.$$

- 5th percentile: $-\ln 0.05 = 2.996$, $\log_{10} = 0.4765$, so
  $m_{0.05} = 1 + (3.699 - 0.4765)/1.0 = 4.22$.
- 95th percentile: $-\ln 0.95 = 0.0513$, $\log_{10} = -1.2905$, so
  $m_{0.95} = 1 + (3.699 + 1.2905)/1.0 = 5.99$.
- median: $-\ln 0.5 = 0.6931$, $\log_{10} = -0.1592$, so
  $m_{0.50} = 1 + 3.858 = 4.86$.

The demonstration's catalogue has largest event $M\,4.7$, comfortably inside the
90% interval $[4.22, 5.99]$ — and 0.16 magnitudes below the median, which is
unremarkable.

**Consequence:** the 90% interval for the largest event of a 5000-event catalogue
spans 1.8 magnitude units, so the observed maximum barely constrains the upper end
of the magnitude distribution. A "maximum magnitude" taken from the largest
observed event is a statement about the catalogue size.

---

## ★8 — experiment specification (binning convention)

**Metric:** $\Delta b = \hat b_{\text{floored}} - \hat b_{\text{rounded}}$ for
catalogues drawn from the *same* parent magnitudes, with each convention's own
standard correction applied (floored with $- (M_c - \Delta/2)$, rounded with
$- M_c$). Also report $\hat b$ against the known $b_\text{true}$.

**Construction:** draw $M \sim \text{GR}(b=1.0, M_c=1.0)$ on a continuous scale,
then produce two catalogues: (i) $\mathrm{floor}(10m)/10$; (ii)
$\mathrm{round}(10m)/10$. Use the same random draws of the parent magnitudes for
both, and $N \ge 5000$ with at least 20 replicates to separate bias from scatter.

**Prediction and derivation:** flooring shifts each value down by an average of
$\Delta/2$ relative to rounding, so the denominator
$\bar m - (M_c - \Delta/2)$ differs between the conventions by $\Delta = 0.1$ in the
grid and by about $\Delta/2$ in the mean. With $\bar m - M_c \approx 0.4343$ at
$b=1$, using the wrong correction changes $b$ by roughly
$(\Delta/2)/0.4343 \approx 11.5\%$ — an order of magnitude larger than the
statistical error of a 5000-event catalogue ($1/\sqrt{5000} = 1.4\%$).

**Control:** report the *same* parent realisation through both conventions, and
verify that with the correct correction each convention recovers $b_\text{true}$ to
within its standard error. Without that control the experiment cannot distinguish a
convention error from a sampling fluctuation.
