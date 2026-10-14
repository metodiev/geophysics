# Solutions — 18-05-01 Bayes' Theorem as an Inverse-Problem Formulation

> Read after attempting the exercises. Numbers below were computed, not estimated.
> Lesson: [01 Bayes' Theorem as an Inverse-Problem Formulation](../01-bayes-inverse-formulation.md).

---

## ★1 — One datum, one prior

$$
\frac{1}{s_{\text{post}}^2} = \frac{1}{s_0^2}+\frac{1}{\sigma^2}
= \frac{1}{1.0}+\frac{1}{0.25} = 1+4 = 5\ \text{(model-units)}^{-2}.
$$

So $s_{\text{post}} = 1/\sqrt5 = 0.447214$ (model units) and

$$
m_{\text{post}} = \frac{m_0/s_0^2 + d/\sigma^2}{1/s_0^2+1/\sigma^2}
= \frac{1.0 + 8.0}{5} = 1.8000 .
$$

$95\%$ interval: $1.8000 \pm 1.96(0.447214) = [0.9235,\,2.6765]$ (model units).

The datum alone would give $[1.020,\,2.980]$; the prior pulls the interval
leftward because $m_0 = 1.0 < d = 2.0$. Units: $m$, $d$, $\sigma$, $s_0$ all in
the same model unit; precisions in that unit$^{-2}$.

---

## ★2 — Prior share of precision

Data precision $= N/\sigma^2 = 9$; prior precision $= 1/0.4^2 = 6.25$. Share:

$$
\frac{6.25}{6.25+9} = 0.4098\ \Rightarrow\ 41.0\% .
$$

A prior that supplies $41\%$ of the information in the answer is not weak in any
defensible sense: nearly half of what is reported came from the choice of prior.
The threshold is a matter of judgement, but the number is not.

---

## ★3 — Where each term comes from

$$
-\ln p(m\mid d) = \frac{1}{2}(d-Gm)^{\top}C_d^{-1}(d-Gm)
+ \frac{1}{2}(m-m_0)^{\top}C_M^{-1}(m-m_0) + \text{const}.
$$

The first quadratic is the negative log likelihood and comes from the noise model;
the second is the negative log prior and comes from the admitted set. The evidence
$p(d)$ is a constant **with respect to $m$**, so it shifts the posterior vertically
but not horizontally. It matters only when posteriors under different models are
compared (lesson [07](../07-evidence-and-model-selection.md)).

---

## ★★4 — Two-parameter posterior

$G^{\top}G = \begin{bmatrix}2&1\\1&2\end{bmatrix}$, so
$G^{\top}C_d^{-1}G = 4\begin{bmatrix}2&1\\1&2\end{bmatrix} = \begin{bmatrix}8&4\\4&8\end{bmatrix}$,
and $C_M^{-1} = \frac{1}{2.25}I = 0.444444\,I$. Hence

$$
C_{\text{post}} = \begin{bmatrix}8.444444&4\\4&8.444444\end{bmatrix}^{-1}
= \begin{bmatrix}0.152679&-0.072321\\-0.072321&0.152679\end{bmatrix}.
$$

$G^{\top}d = (1.0+0.5,\ 0.0+0.5) = (1.5,\,0.5)$, so
$G^{\top}C_d^{-1}d = (6.0,\,2.0)$ and

$$
m_{\text{post}} = C_{\text{post}}\begin{bmatrix}6\\2\end{bmatrix}
= (0.771429,\ -0.128571).
$$

Standard deviations: $\sqrt{0.152679} = 0.390741$ each. Correlation:
$-0.072321/0.152679 = -0.473684$. Marginal $95\%$ interval for $m_1$:
$0.771429 \pm 1.96(0.390741) = [-0.9944,\,2.5373]$.

---

## ★★5 — Tikhonov equivalence

$$
\lambda^2 = \frac{\sigma_d^2}{s_0^2} = \frac{0.25}{2.25} = 0.111111 .
$$

The damped solution is

$$
m_\lambda = \left(G^{\top}G+\lambda^2I\right)^{-1}G^{\top}d
= \begin{bmatrix}2.111111&1\\1&2.111111\end{bmatrix}^{-1}\begin{bmatrix}1.5\\0.5\end{bmatrix}
= (0.771429,\ -0.128571),
$$

identical to the posterior mean of ★4. This is a check of the algebra of lesson
[01](../01-bayes-inverse-formulation.md) Section 4, not a coincidence: the two are
the same normal equation.

---

## ★★6 — Null-space posterior width

$v = (1,-1)/\sqrt2$ satisfies $G_{\text{bad}}v = 0$, so the data contain no
information along it and the posterior precision there is the prior precision:

$$
\sigma_{\text{post}}(v) = \sqrt{v^{\top}C_{\text{post}}v} = 3.0000\ \text{(model units)},
$$

equal to the prior standard deviation $s_0 = 3$. The prior has not supplied
information about this direction; it has declined to, and the posterior says so.

---

## ★★7 — A specification for falsifying Gaussianity

- **Inject**: a known model $m_{\text{true}}$ and a known noise realisation drawn
  from a *stated* non-Gaussian distribution, for example Student-$t$ with $\nu=4$.
- **Assume**: a Gaussian likelihood with the correct $\sigma$.
- **Statistic**: the posterior predictive distribution of the residual, compared
  through (i) an empirical quantile plot against the assumed normal, (ii) the
  sample kurtosis, and (iii) a posterior predictive $p$-value for the statistic
  "number of residuals beyond $3\sigma$".
- **Threshold**: reject the Gaussian likelihood when the observed tail count lies
  outside the central $95\%$ of its posterior predictive distribution, or when the
  sample kurtosis exceeds the replicated $97.5\%$ quantile. State the number of
  replicates (at least $1000$) so the threshold's Monte Carlo error is bounded.

The specification is executable because every quantity is defined by a number and
a distribution, and because the truth is known by construction.

---

## ★★8 — When a flat prior gives the least-squares solution

With $C_M^{-1}\to 0$ the posterior exponent becomes
$\frac{1}{2\sigma_d^2}\|d-Gm\|^2$: the posterior is proportional to the likelihood,
its mode is the least-squares solution, and this holds for any design.

It **requires** that the likelihood be normalisable on its own. If $G$ has a
non-trivial null space and the flat prior is improper, the posterior is also
improper — constant along the null direction, so it integrates to infinity, and

- no credible interval can be quoted, because no probability content is defined;
- no posterior mean exists, because the necessary integral diverges.

Before quoting an interval one must state a truncation (a box, a bound, or a
weakly informative Gaussian), and it is that truncation, not the likelihood,
that supplies the width along the null directions.
