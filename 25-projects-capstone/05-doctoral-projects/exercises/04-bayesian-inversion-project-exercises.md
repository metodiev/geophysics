# Exercises — 25-05-04 Project: Trans-Dimensional Bayesian Inversion

Attempt these before reading the
[solutions](./04-bayesian-inversion-project-solutions.md). The project is
[04 Trans-Dimensional Bayesian Inversion](../04-bayesian-inversion-project.md); all
numbers are **SYNTHETIC** and printed by
[`code/transdimensional_demo.py`](../code/transdimensional_demo.py):

| Quantity | Value |
|---|---|
| data | 20 samples, Gaussian kernel of 1.0 cell half-width, $\sigma_d = 0.15$ km/s |
| true model | 3 layers 4.00 / 5.60 / 7.00 km/s, boundaries at cells 6 and 13 |
| prior | $k$ uniform on 1–5; boundaries uniform given $k$; values $N(0, 1.5^2)$ |
| exact posterior | $P(3) = 0.9318$, $P(4) = 0.0675$, $P(5) = 0.0007$, $P(1) = P(2) = 0.0000$ |
| exact MAP model | $k=3$, boundaries (6, 13), $P = 0.9306$ |
| model space | 5036 enumerated subsets ($k \le 5$) out of $2^{19} = 524288$ boundary sets |
| rjMCMC, 3 chains | $P(3) = 0.9834 / 0.9807 / 0.9825$, $P(4) = 0.0165 / 0.0191 / 0.0174$ |
| total variation distances | 0.0516, 0.0489, 0.0506 |
| acceptance rates | value 0.354, boundary 0.004, birth 0.007, death 0.007 |
| profile, chain at $k=3$ | mean 4.00 / 5.58 / 6.94 at depths 2.5 / 8.5 / 16.5; sd 0.06 / 0.07 / 0.06 |
| exact profile | mean 3.99 / 5.58 / 6.93; sd 0.06 / 0.08 / 0.06 |
| profile agreement | MCMC mean − exact mean: 0.017 km/s rms; posterior mean − truth: 0.036 km/s rms |

## ★ Foundational

**★1.** Write the joint posterior for this model space. State what the prior on the
number of layers is, what the prior on the boundary positions is, and why the
normalisation of the boundary prior depends on $k$.

**★2.** Derive the birth (split) acceptance ratio for a move that replaces one layer
with value $v$ by two layers with values $v-u$ and $v+u$, where $u \sim N(0,
\sigma_u^2)$ is the proposal. Identify each factor: likelihood ratio, value-prior
ratio, boundary-prior ratio, move probabilities, position-choice ratio, proposal
density, Jacobian.

**★3.** Write the Gaussian evidence for a fixed boundary set $b$:
$\log p(\mathbf d \mid b) = -\tfrac12\mathbf d^{\mathsf T}\mathbf C_b^{-1}\mathbf d
-\tfrac12\log|\mathbf C_b| - \tfrac{n}{2}\log 2\pi$ with
$\mathbf C_b = \mathbf G\mathbf S_b\mathbf G^{\mathsf T} + \sigma_d^2\mathbf I$.
Explain what the $\log|\mathbf C_b|$ term does and why it produces the Occam penalty
rather than a reward for extra parameters.

## ★★ Applied

**★★4.** From the exact posterior, compute the posterior odds $P(4)/P(3)$ and the
prior odds $\binom{19}{2}/\binom{19}{3}$. Hence compute the Bayes factor
$\mathrm{BF}_{43}$ and state separately how much of the total odds comes from the
prior on the number of boundaries and how much from the data.

**★★5.** How many boundary sets exist with exactly 4 layers, and how many with
exactly 5? Given that the demonstration enumerates 5036 models, verify that number
from the binomial coefficients and state how many models with $k = 6$ the enumeration
is missing.

**★★6.** The $k=4$ probability is estimated as 0.0165 while the exact value is
0.0675. Show that this is a bias rather than Monte Carlo noise: estimate the number of
accepted births in a 120 000-iteration run from the printed acceptance rate and
attempt fractions, and compare the resulting binomial standard error with the
discrepancy. Then state whether a ten-times longer run would fix it.

**★★7.** The profile from the sampler matches the exact posterior mean to
0.017 km/s rms, while $P(4)$ is wrong by a factor of three. Explain how both can be
true at once, and state which quantity a user of the inversion would care about.

**★★8.** All three chains give essentially the same $P(k)$ distribution regardless of
their starting model. Explain why that is *not* evidence that the sampler is correct,
and name the diagnostic that would catch the shared bias.

## ★★★ Research-oriented

**★★★9.** Design a validation protocol for a trans-dimensional inversion of a problem
whose exact answer is **not** available (for example, a real receiver-function dataset
in which the number of crustal discontinuities is the unknown). Your protocol must
specify: the synthetic test-bed used to validate the sampler before it is applied, how
the sampler's bias is measured there, the chain and prior-sensitivity diagnostics used
on the real problem, at least one proposal improvement with its justification, the
acceptance rates you would report, and the statement you would be willing to defend if
the real and synthetic cases disagree. An answer that consists only of "run more
iterations" or "check $\hat R$" is a failed answer.
