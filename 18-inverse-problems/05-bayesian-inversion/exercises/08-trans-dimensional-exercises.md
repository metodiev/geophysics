# Exercises — 18-05-08 Trans-Dimensional and Reversible-Jump MCMC

Lesson: [08 Trans-Dimensional and Reversible-Jump MCMC](../08-trans-dimensional.md).
Attempt these before reading the [solutions](./08-trans-dimensional-solutions.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the birth acceptance ratio for a move from order $k$ to $k+1$ that
creates a coefficient $u \sim \mathcal{N}(0,s^2)$, with prior
$\mathcal{N}(0,\tau^2)$ and proposal probabilities $\pi_{\text{birth}}(k)$,
$\pi_{\text{death}}(k+1)$. State what happens when $s = \tau$.

**★2.** A trans-D run of $100\,000$ iterations spends $200$ of them in $k = 0$, and
the run contains $9000$ accepted birth-or-death transitions. Estimate $P(k=0)$ and
give an honest standard error, explaining the choice of denominator.

**★3.** List the four factors that appear in a reversible-jump acceptance ratio
(other than the likelihood ratio) and state the role of each.

## ★★ Applied

**★★4.** Using the analytic log evidences $(-20.4768,\ -15.3904,\ -14.8061)$ for
orders $k = 0,1,2$ with a uniform model prior, compute $P(k\mid d)$ for each $k$.

**★★5.** Compute the Bayes factor $B_{21}$ implied by the same numbers, and state
whether the expected log-odds of order 2 against order 1 exceeds one.

**★★6.** In the demonstration, birth and death acceptance rates are $0.582$ and
$0.126$. Explain the asymmetry physically, and state what a death rate of $0.02$
would indicate about the chain.

## ★★★ Research-oriented

**★★★7.** Design a synthetic recovery test for a trans-D layer-count inversion.
State the injected model, the family and priors, the number of chains, the
diagnostics, and the criterion for declaring the implementation verified. State
what the test cannot establish.

**★★★8.** A trans-D posterior over the number of layers piles up at the largest
order in the family. Give two explanations, and for each state the experiment that
would distinguish it from an implementation error.
