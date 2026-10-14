# Solutions — 18-05-03 Priors: Informative, Reference and Their Influence

> Read after attempting the exercises. Numbers were computed, not estimated.
> Lesson: [03 Priors: Informative, Reference and Their Influence](../03-priors.md).

---

## ★1 — Shrinkage for two prior widths

$$
K = \frac{s_0^2}{s_0^2+\sigma^2}, \qquad
m_{\text{post}} = K d\ (m_0 = 0), \qquad
s_{\text{post}} = \sqrt{\frac{s_0^2\sigma^2}{s_0^2+\sigma^2}} .
$$

$s_0 = 0.25$: $K = 0.0625/(0.0625+0.25) = 0.2000$,
$m_{\text{post}} = 0.4000$, $s_{\text{post}} = \sqrt{0.05} = 0.2236$.

$s_0 = 4.0$: $K = 16/(16.25) = 0.98462$,
$m_{\text{post}} = 1.9692$, $s_{\text{post}} = 0.49614$.

The datum is $2.0$; a prior of width $0.25$ holds the answer at $0.4$.

---

## ★2 — Equal precisions

Data precision $N/\sigma^2 = 25/4 = 6.25$. For the prior to match it,

$$
\frac{1}{s_0^2} = 6.25 \ \Rightarrow\ s_0 = 0.4 .
$$

---

## ★3 — Poisson rate

$$
\ln p(k\mid\lambda) = k\ln\lambda - \lambda - \ln k!
\ \Rightarrow\
\frac{\partial^2\ln p}{\partial\lambda^2} = -\frac{k}{\lambda^2}
\ \Rightarrow\
I(\lambda) = \frac{\mathbb{E}[k]}{\lambda^2} = \frac{1}{\lambda}.
$$

So $\pi(\lambda)\propto \lambda^{-1/2}$ and the posterior is proportional to
$\lambda^{k-1/2}e^{-\lambda}$, i.e. $\text{Gamma}(\text{shape } k+\tfrac12,\
\text{rate }1)$. For $k_{\text{obs}}=3$: shape $3.5$, rate $1$, mean $3.5$,
mode $3-0.5 = 2.5$ (the mode of a Gamma with shape $\alpha>1$ is
$(\alpha-1)/\text{rate}$).

---

## ★★4 — Prior share and displacement

$$
\frac{1/s_0^2}{1/s_0^2+N/\sigma^2} = \frac{1}{1+64} = 0.015385 = 1.54\% .
$$

With such a prior the posterior mean is pulled from the data mean by a factor
$1-K$ where $K = s_0^2/(s_0^2+\sigma^2/N) = 1/(1+0.003906) = 0.99611$. Choosing
$m_0$ one prior standard deviation away therefore moves the posterior mean by only
$1-K = 0.0039$ of that offset, i.e. $0.39\%\cdot1 = 0.0039$ model units. This is
acceptable: the prior carries $1.5\%$ of the information. For comparison, at
$s_0 = 0.5$ in the same design the prior share is $1/(1+64\cdot0.25) = 5.88\%$,
and at $s_0 = 0.125$ it is $50\%$ — the same design, three very different claims.

---

## ★★5 — Why the two flat priors differ

The two priors are related by the change of variable $u = \log\sigma$. A prior
that is flat in $\sigma$ has density in $u$ proportional to $\sigma(u) =
e^{u}$, i.e. it puts increasing mass at large scale. A prior flat in $u$ is
$p(\sigma)\propto 1/\sigma$ (up to a constant), which is the Jeffreys prior for a
scale and is unchanged if one instead parameterises by $\sigma^{-1}$: the same
log-scale is merely reflected.

Measured on the demonstration's $n = 9$ SYNTHETIC samples: the flat-in-$\sigma$
interval is $[0.7020, 1.9309]$ and the Jeffreys / flat-in-$\log\sigma$ interval is
$[0.6742, 1.7694]$, a width ratio of $1.1221$, i.e. the flat-$\sigma$ interval is
$12.2\%$ wider. The invariant one is the Jeffreys prior; the flat prior on
$\sigma$ encodes a preference for large scales.

---

## ★★6 — Truncated posterior at a bound

Untruncated likelihood: mean $0.32$, standard deviation $0.12/\sqrt2 = 0.084853$.
With a flat prior on $[0,0.5]$, integrated on a grid:

| data | posterior mean | posterior std | mass within $0.02$ of the bound |
|---|---|---|---|
| $(0.30,\,0.34)$ | 0.316399 | 0.080776 | $1.29\%$ |
| $(0.60,\,0.64)$ | 0.461663 | 0.033610 | $37.09\%$ |

**First case**: the bound is irrelevant; report the posterior mean and a
$95\%$ credible interval, and note that the interval was truncated at $0$, which
costs $1.3\%$ of the mass over the whole upper edge but almost nothing here.

**Second case**: the likelihood mean $0.62$ lies outside the admitted set; the
posterior is squeezed against the bound and $37\%$ of its mass sits within $0.02$
of it. Report **the edge mass first**, then the interval, and state that the data
prefer an inadmissible value. Reporting "$\phi = 0.462 \pm 0.034$" alone would be
a misdescription of what the data say.

---

## ★★7 — Sensitivity study for a prior-dominated inversion

- **Priors compared:** uniform on $[0,H_{\max}]$ for the layer thickness with
  $H_{\max} \in \{20, 40, 80, 160\}$ km, and a Gaussian
  $\mathcal{N}(40\,\text{km},\ s^2)$ with $s \in \{5, 20, 80\}$ km.
- **Metric:** posterior mean and $95\%$ credible interval of $H$; the prior share
  of the posterior precision from the Fisher information of the data; and the
  Bayes factor between the two-layer and one-layer families under each prior.
- **Replicates:** one inversion per prior; the metric is the sensitivity itself, so
  no replication is needed for the prior sweep, but each inversion should report
  an MCMC effective sample size above $400$ so that Monte Carlo error is small
  relative to the prior effect.
- **Decision rule:** call the result prior-dominated if the change in the $95\%$
  interval across the prior family exceeds the change produced by a $10\%$
  perturbation of the data values, or if the prior share of precision exceeds
  $50\%$ for any prior in the family.

---

## ★★8 — Three explanations for mass at the upper bound

1. **The truth is at or above the bound.** Diagnostic: refit with the bound
   relaxed and check whether the posterior moves interior; if it does, the bound
   was the problem.
2. **The bound is real, and the data are only weakly informative.** Diagnostic:
   compute the likelihood alone; if it is broad and overlaps the bound, the pile-up
   is the honest summary, and the answer is "the data do not distinguish values
   above the bound from the bound itself".
3. **A coding or parameterisation error compresses the scale.** Diagnostic: run a
   synthetic recovery test with a known interior truth. If the posterior piles up
   at the bound when the truth is interior, the likelihood or the prior range is
   wrong.

The three are distinguished by relaxing the bound, by inspecting the likelihood
alone, and by injecting a known truth — all three are cheap, and all three should
be run before the pile-up is reported as a result.
