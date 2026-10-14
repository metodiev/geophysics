# Exercises — Global Search: Monte Carlo, Simulated Annealing, Genetic Algorithms

Refer to [the lesson](../04-global-search.md). All models are SYNTHETIC.
Demo: `../code/global_search_demo.py`.

## ★ Foundational

**1.1** State the uniform-sampling budget formula $B(P,v)$ and evaluate it for $P = 0.5$ and $v = 0.07344$.

**1.2** Write the Metropolis acceptance probability and evaluate it for a worsening of $\Delta f = 0.25$ at $T = 0.5$ and at $T = 0.05$.

**1.3** Explain in one sentence the difference between a basin volume and a tolerance volume.

## ★★ Applied

**2.1** The measured global basin volume fell from 0.24284 at $n = 2$ to 0.07344 at $n = 8$, while the tolerance volume fell from 0.05225 at $n = 2$ to $<10^{-5}$ at $n = 6$. Compute both per-dimension factors and comment.

**2.2** From the measured 4-D basin fractions (0.1341, 0.1336, 0.1530, 0.2340, 0.1515, 0.1938), state which well a method that finds the largest basin would return, and its objective value.

**2.3** The GA success rate was 0.24 and DE 0.52 over 25 runs at 6000 evaluations. Compute the standard error of each and of the difference, and decide whether the difference is resolved.

## ★★★ Research-oriented

**3.1** Design a cooling schedule whose temperature is set by a measured acceptance rate rather than by a formula, and state the measurement that would show it beats the geometric schedule at equal budget.

**3.2** The measured population standard deviation collapsed from 0.51 to 0.03 by generation 12 while the best objective was still 0.09 above $f_{\text{glob}}$. Propose a restart rule and compute the evaluation cost it adds at 6000 evaluations.

**3.3** Argue whether a global-search ranking measured on a declared synthetic objective transfers to a field dataset. Cite three measured numbers.
