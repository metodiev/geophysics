# Solutions — Global Search: Monte Carlo, Simulated Annealing, Genetic Algorithms

**1.1** $B = \ln(1-P)/\ln(1-v) = \ln 0.5/\ln(0.92656) = -0.69315/(-0.076287) = 9.09$, so 10 samples.

**1.2** $a = \exp(-\Delta f/T)$. At $T = 0.5$: $\exp(-0.5) = 0.6065$. At $T = 0.05$: $\exp(-5) = 6.738\times10^{-3}$. The tenfold cooling changed the acceptance probability by a factor $e^{4.5} = 90$.

**1.3** A basin volume counts starts that *converge* to a minimum; a tolerance volume counts models whose objective is within a stated tolerance of the global minimum, and it is the one a global search needs.

**2.1** Basin: $(0.07344/0.24284)^{1/6} = 0.3046^{1/6} = 0.820$ per dimension, i.e. 18% loss a dimension. Tolerance: $(10^{-5}/0.05225)^{1/4} = 1.914\times10^{-4}$ over one step of 4 dims, so about $(1.914\times10^{-4})^{1/2} = 0.0138$ per dimension, i.e. 98.6% loss a dimension. The exponential is in the tolerance volume.

**2.2** The largest basin is well 4 (0.2340) with $f(\text{centre}) = 0.17762$, against the global minimum at $f = -0.018591$. The largest-basin strategy returns an objective 0.196 worse, i.e. ten times the 0.05 tolerance away from global.

**2.3** $\mathrm{se}(0.24) = \sqrt{0.24\cdot0.76/25} = 0.0854$; $\mathrm{se}(0.52) = \sqrt{0.52\cdot0.48/25} = 0.0999$. The difference 0.28 has standard error $\sqrt{0.0854^2 + 0.0999^2} = 0.1315$, so the difference is 2.1 standard errors: resolved at the 5% level marginally, and the demo therefore also prints the median objective, which agrees in direction.

**3.1** Track the acceptance rate over the last $M$ proposals; raise $T$ by a factor when the rate falls below a floor and lower it when it exceeds a ceiling. The test: at equal evaluation budget, compare success rates over at least 25 runs at several temperatures and check whether the intervals overlap. The null hypothesis is that the adaptive and geometric schedules have equal success probability.

**3.2** Restart when the population standard deviation falls below a fraction of its initial value, e.g. 10% (here 0.051), by resampling half the population uniformly. Cost: one evaluation per resampled member. Resampling 25 members every restart adds 25 evaluations, 0.4% of the 6000 budget; the measured payoff should be tested as a change in success rate over 25 runs, with the standard error from 2.3.

**3.3** Not automatically, for three measured reasons. (i) The tolerance volume at $n = 4$ was $4\times10^{-5}$, so the success of any method is a statement about a target of that size, and a real objective has a different size. (ii) The wells are Gaussian and the layout is nested, so the measured basin fractions (0.1341 for the global well, 0.2340 for a worse one) are properties of the declared function, not of a class of functions. (iii) The 25-run success rates carry $\pm0.13$, so small differences cannot be transferred with any confidence at all.
