# Solutions — 18-05-02 Constructing Likelihoods and Error Models

> Read after attempting the exercises. Numbers were computed, not estimated.
> Lesson: [02 Constructing Likelihoods and Error Models](../02-likelihood-models.md).

---

## ★1 — Variance inflation under AR(1)

$$
\frac{\operatorname{Var}(\bar e)}{\sigma^2/n}
= 1 + 2\sum_{k=1}^{n-1}\left(1-\frac{k}{n}\right)\rho^{k}
= 1 + 2(3.6182) = 8.2364 \quad (n = 12,\ \rho = 0.9).
$$

Asymptotically, $\operatorname{Var}(\bar e)\to \frac{\sigma^2}{n}\frac{1+\rho}{1-\rho}$,
so the factor is $(1+0.9)/(1-0.9) = 19.000$. The understated standard error is
$\sqrt{8.2364} = 2.870$ at $n = 12$, rising to $\sqrt{19} = 4.359$ asymptotically.
Correlated errors make a mean far less informative than the independent formula
claims.

---

## ★2 — Understated slope uncertainty

$$
\frac{0.0213}{0.0167} = 1.275,
\qquad 1 - \frac{0.0167}{0.0213} = 21.6\% .
$$

The Gaussian (independent) interval is $1.28$ times — about $22\%$ — too narrow.
The point estimate moved by only $0.0100$, from $0.5240$ to $0.5340$: the
independence error corrupts the interval, not the estimate.

---

## ★3 — Three negative log likelihoods

Gaussian: $-\ln p = \sum_i r_i^2/(2\sigma^2) + \text{const}$ — **quadratic** in
$\lvert r_i\rvert$.

Laplace: $-\ln p = \sum_i \lvert r_i\rvert/\sigma + \text{const}$ — **linear**.

Student-$t$: $-\ln p = \frac{\nu+1}{2}\sum_i \ln\!\left(1+r_i^2/(\nu\sigma^2)\right)
+ \text{const}$ — **logarithmic**.

The growth rate is the influence: quadratic gives unbounded influence, linear
bounded, logarithmic nearly nil.

---

## ★★4 — Influence ratios

At $\delta/\sigma = 8$ the shifts are Gaussian $-0.0280$, Laplace $-0.0064$,
Student-$t$ $-0.0071$, so

$$
\frac{\text{Gaussian}}{\text{Laplace}} = \frac{0.0280}{0.0064} = 4.375,
\qquad
\frac{\text{Gaussian}}{\text{Student-}t} = \frac{0.0280}{0.0071} = 3.944 .
$$

The ratio measures how much more a single bad datum moves a Gaussian fit than a
robust one at that displacement. Its growth with $\delta$ is the statement that the
Gaussian influence is unbounded while the robust influences saturate.

---

## ★★5 — Covariance from a shared calibration

Write the error as $e_i = \epsilon_i + a\,x_i\,\delta\rho$, where $\epsilon_i$ is
independent station noise with variance $\sigma_0^2$, $\delta\rho$ is the single
unknown regional-density error with standard deviation $s_\rho$, and $a x_i$
converts a density error into a gravity error at station $i$ (the Bouguer term is
linear in density, so $x_i$ is the local free-air-to-Bouguer conversion factor).
Then

$$
C_{ij} = \sigma_0^2\delta_{ij} + a^2 x_i x_j\,s_\rho^2 .
$$

All off-diagonal entries are **non-zero**, of rank-one form $a^2s_\rho^2 x_ix_j$.
This is the commonest correlated-error structure in potential-field work: a single
unknown scalar multiplies a known sensitivity vector. Treating $C$ as diagonal
removes a systematic that no amount of averaging over stations reduces.

---

## ★★6 — Inflation from estimating the scale

With flat priors on the coefficients and the reference prior on $\sigma$, the joint
posterior factorises into a Gaussian conditional for the coefficients given
$\sigma$ and an inverse-gamma for $\sigma^2$. From the inverse-gamma,

$$
\mathbb{E}[\sigma^2\mid d] = \frac{\text{rss}/2}{N/2-1} = \frac{\text{rss}}{N-2},
$$

and the conditional variance of a coefficient is $\sigma^2[(A^{\top}A)^{-1}]_{jj}$.
Marginalising replaces $\sigma^2$ by its posterior mean, so

$$
\frac{\operatorname{Var}_{\text{marginal}}}{\operatorname{Var}_{\text{known }\sigma}}
= \frac{\text{rss}/(N-2)}{\text{rss}/N} = \frac{N}{N-2} .
$$

For $N = 12$, $d = 2$: $12/10 = 1.2000$, so the standard deviation is inflated by
$\sqrt{1.2} = 1.0954$, i.e. $9.5\%$.

---

## ★★7 — Specification for model sensitivity

- **Metric:** the width of the $95\%$ interval of the fitted slope, reported for
  each of the three data types under a Gaussian likelihood, and the coverage of
  that interval against the known true slope.
- **Replicates:** at least $500$ synthetic data sets per cell, so the Monte Carlo
  standard error on a reported width is below $1\%$ of the width.
- **Predicted ordering under a Gaussian likelihood:** clean Gaussian is the
  narrowest and well calibrated; AR(1) is too narrow (measured $21.6\%$ in ★2 at
  $\rho = 0.9$, and it will also be biased in coverage); contamination is both
  biased in the slope and too narrow in the interval.
- **Most severe:** the contaminated case, because the Gaussian likelihood squares a
  $5\sigma$ outlier and moves the point estimate as well as the interval, whereas
  the AR(1) case leaves the estimate nearly unbiased and corrupts only the width.

The specification is executable: every cell has a defined generating process, a
statistic and a replicate count.

---

## ★★8 — The cost of fixing $\sigma$ at its estimate

Plugging in $\hat\sigma$ treats a random quantity as known. It removes the
variance of $\hat\sigma$ from the interval, which is a real omission, and it also
removes the heavy tail that the marginal posterior has. Quantitatively, for the
★★6 case:

$$
\hat\sigma \approx 0.2417,\qquad
s_{\text{fixed}} = 0.01672,\qquad
s_{\text{marginal}} = 0.01672\sqrt{\frac{12}{10}} = 0.01832\ \text{(slope units)}.
$$

The corrected $95\%$ interval is $9.5\%$ wider, and — more importantly — its shape
is a Student-$t$ with $N-d = 10$ degrees of freedom rather than a Gaussian, so its
$97.5\%$ quantile is larger still: $t_{10,0.975} = 2.228$ against $1.960$, a
further factor of $1.137$. The combined effect on the interval half-width is
$1.095 \times 1.137 = 1.245$, i.e. about $25\%$ wider than the plug-in interval.
