# Solutions — 18-06-03 Sensitivity Analysis: Local, Global, Sobol Indices

> Read after attempting the exercises. Numbers were computed, not estimated.
> Lesson: [03 Sensitivity Analysis](../03-sensitivity-analysis.md).

---

## ★1 — The factor variance

The factor is $g_i(x) = (\lvert4x-2\rvert + a_i)/(1+a_i)$. Its first moment is

$$
\mathbb{E}[\lvert 4x-2\rvert]
= \int_0^{1/2}(2-4x)\,\mathrm{d}x + \int_{1/2}^1 (4x-2)\,\mathrm{d}x
= \tfrac12 + \tfrac12 = 1,
$$

so $\mathbb{E}[g_i] = (1+a_i)/(1+a_i) = 1$. Its second moment is

$$
\mathbb{E}[\lvert 4x-2\rvert^{2}]
= \frac14\int_{-2}^{2}u^{2}\,\mathrm{d}u
= \frac14\cdot\frac{2^{3}-(-2)^{3}}{3}
= \frac14\cdot\frac{16}{3} = \frac43 ,
$$

using $u = 4x-2$. Therefore

$$
\mathbb{E}[g_i^{2}] = \frac{\tfrac43 + 2a_i + a_i^{2}}{(1+a_i)^{2}},
$$

and, because $\mathbb{E}[g_i] = 1$,

$$
\operatorname{Var}[g_i] = \mathbb{E}[g_i^{2}] - 1
= \frac{\tfrac43 + 2a_i + a_i^{2} - (1+a_i)^{2}}{(1+a_i)^{2}}
= \frac{\tfrac43 - 1}{(1+a_i)^{2}}
= \frac{1}{3(1+a_i)^{2}} .
$$

For $a = (0,\ 0.5,\ 3)$ this gives
$V = (0.333333,\ 0.148148,\ 0.020833)$, and
$\operatorname{Var}(f) = \prod_i(1+V_i) - 1 = 0.562757$, as printed.

---

## ★2 — Third index

$$
S_3 = \frac{V_3}{\operatorname{Var}(f)} = \frac{0.020833}{0.562757} = 0.037020,
$$

$$
S_{T3} = 1 - \frac{\prod_{j\ne3}(1+V_j) - 1}{\operatorname{Var}(f)}
= 1 - \frac{1.333333\times1.148148 - 1}{0.562757}
= 1 - \frac{0.530864}{0.562757} = 0.056673 .
$$

Both match the printed table. The interaction share
$S_{T3} - S_3 = 0.019653$ is small, as expected for the parameter with the largest
$a_i$.

---

## ★3 — The two inequalities

$$
\sum_i S_i \le 1, \qquad S_{Ti} \ge S_i .
$$

The first becomes an equality for an **additive** model: if
$f = f_0 + \sum_i f_i(x_i)$ then the variance decomposes with no interaction terms.
The second becomes an equality for a parameter that **does not interact** with any
other, i.e. for which every coefficient involving it also contains only itself.

---

## ★★4 — Relative standard errors

$$
\frac{0.000669}{0.592203} = 0.113\%, \qquad
\frac{0.000264}{0.694143} = 0.038\% .
$$

The total index is better determined than the first-order index, essentially because
$\widehat{S_{T1}}$ is an average of squared differences while $\hat S_1$ involves a
product with a Monte Carlo average, and the latter has more variance for the same
number of samples. The practical consequence is that a factor-fixing decision — which
relies on $S_{Ti}$ — can be made with fewer samples than a ranking decision based on
$S_i$.

---

## ★★5 — Local ranking at a different nominal point

At $x_0 = (0.2, 0.5, 0.5)$:

$$
\frac{\partial f}{\partial x_1} = 20(0.2-0.5) = -6, \qquad
\frac{\partial f}{\partial x_2} = 1, \qquad
\frac{\partial f}{\partial x_3} = 0.5 .
$$

Local ranking by $\lvert\partial f/\partial x_i\rvert$: $x_1$ first, $x_2$ second,
$x_3$ third — which now *agrees* with the global ranking. At the nominal point
$(0.5,0.5,0.5)$ the derivative with respect to $x_1$ is exactly zero and the local
ranking puts $x_1$ last. The difference between the two nominal points is the entire
point: a local sensitivity is a statement about one point, and at
$(0.5,0.5,0.5)$ the point happens to sit at the minimum of the parabola, where the
first-order effect vanishes while the second-order effect — which is what dominates
the global variance — is at its most influential.

---

## ★★6 — Extrapolating the convergence table

The error falls roughly as $N^{-1}$ here (measured slope $-1.007$), so reducing it by
a factor of $11$ requires

$$
N \to 11\,N = 11 \times 16384 = 180\,224 \approx 2\times10^{5}
$$

base samples, i.e. about $1.4\times10^{6}$ forward evaluations with $d = 3$ and the
$N(2d+2)$ design. The estimate assumes the measured rate continues to hold, which is
an extrapolation: the rate is a property of the integrand's smoothness and of the
dimension, and a rougher or higher-dimensional problem returns the plain Monte Carlo
rate $-0.5$, in which case the required $N$ is the *square* of the factor, i.e.
$121\times$ rather than $11\times$.

---

## ★★7 — What an additive conclusion needs

$S = (0.4, 0.35, 0.3)$ sums to $1.05$, which is impossible for first-order indices:
$\sum_i S_i \le 1$. The values are therefore either mislabelled (they might be total
indices, which can sum above one) or wrong. If they are total indices, the study has
*not* shown additivity — total indices can sum above one precisely because of
interactions, and additive models are the case where total and first-order indices
coincide. What should have been reported: both $S_i$ and $S_{Ti}$ with standard
errors, and the statement $\sum_i S_i = 1.000 \pm \epsilon$ as the evidence for
additivity, together with $S_{Ti} - S_i \approx 0$ for every parameter.

---

## ★★8 — Sensitivity analysis for 12 parameters on 1000 solves

- **Method:** Morris elementary effects for screening, because the budget is too
  small for Sobol indices in 12 dimensions. A trajectory design with $10$
  trajectories costs $10(12+1) = 130$ solves and gives a mean and a standard
  deviation of each elementary effect, which ranks the parameters and flags
  nonlinear or interacting ones.
- **Then:** Sobol indices for the three to five parameters the screening keeps, if
  the budget allows: a Sobol design with $N$ base samples in $d'$ dimensions costs
  $N(2d'+2)$; with $d' = 4$ that is $10N$, so about $80$ base samples — a very
  coarse estimate with a standard error of the order of $0.05$ on each index.
- **Standard-error target:** $0.02$ on the ranked parameters would need
  $N \gtrsim 500$ base samples in $d'=4$, i.e. $5000$ solves, which exceeds the
  budget; hence the two-stage strategy.
- **With $10^{5}$ solves:** skip the screening, use $N = 4000$ base samples in all
  $12$ dimensions ($4000\times26 = 104\,000$ solves), report $S_i$ and $S_{Ti}$ with
  replicate-based standard errors, and add a bootstrap over the input distribution to
  quantify the sampling uncertainty in the indices themselves.
