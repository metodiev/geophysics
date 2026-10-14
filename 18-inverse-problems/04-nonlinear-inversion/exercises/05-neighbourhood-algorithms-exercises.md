# Exercises — Neighbourhood and Very Fast Simulated Annealing

Refer to [the lesson](../05-neighbourhood-algorithms.md). All models are SYNTHETIC.
Demo: `../code/neighbourhood_annealing_demo.py`.

## ★ Foundational

**1.1** Define the Voronoi cell of the current best model and write the inscribed radius $r_{\text{ins}}$ in terms of distances to the evaluated samples.

**1.2** Write the VFSA proposal for one coordinate and state what happens to it as $T \to 0$.

**1.3** State the measured contraction of the inscribed radius over the first four generations and the corresponding volume change.

## ★★ Applied

**2.1** From the measured radii (0.137896 at generation 1, 0.000101 at generation 5), compute the ball volume fractions at $n = 2$ from $\pi r^2/4$ and compare with the printed 1.493e-02 and 8.050e-09.

**2.2** Compute the acceptance probability of a proposal that raises the objective by 0.3 at $T = 0.5$, 0.1, 0.02.

**2.3** The demo's default schedule is $T_k = 0.5 \times 0.995^{k}$ with a Cauchy-like proposal. Compute the step index at which $T = 0.05$ and at which $T = 0.01$.

## ★★★ Research-oriented

**3.1** The measured acceptance fraction stayed near 0.02 while the inscribed radius fell by three orders of magnitude. Propose a mechanism and design the measurement that would confirm or refute it.

**3.2** Add a restart rule to the neighbourhood algorithm: restart when the acceptance fraction is below 0.01 for ten consecutive generations. Implement it, measure success over twelve runs at equal budget, and report whether the improvement exceeds the binomial standard error.

**3.3** Argue whether either algorithm can be said to have converged on a real dataset, given that both are declared success only against a reference minimum computed by dense local search.
