# Exercises — Multi-Start, Hybrid and Memetic Strategies

Refer to [the lesson](../06-multi-start-and-hybrid.md). All models are SYNTHETIC.
Demo: `../code/multistart_hybrid_demo.py`.

## ★ Foundational

**1.1** Derive $P_k = 1-(1-p)^{k}$ from independence of starts.

**1.2** Compute the budget $k$ for $P = 0.95$ at the measured $p = 0.122$ and at $p = 0.02$.

**1.3** State the two assumptions behind the multi-start law and give one way each could be violated.

## ★★ Applied

**2.1** From the measured 400-start success count at $n = 4$ (49 hits), compute $p$, its standard error, and the resulting 95%-budget with its uncertainty.

**2.2** The measured $p$ was 0.122 against a basin volume fraction of 0.1482 at $n = 4$, and 0.375 against 0.2014 at $n = 2$. Explain how the same two mechanisms produce opposite signs of the difference.

**2.3** Reproduce the evaluation arithmetic: 23 starts, 310 median forward evaluations, 13.5 evaluations per polish. Check the product and state what an evaluation counts.

## ★★★ Research-oriented

**3.1** Design a two-stage hybrid for a problem where one forward evaluation costs one second, with a target of 90% success, and compute the wall-clock budget from the measured per-polish cost. State the assumption that makes the calculation valid.

**3.2** The measured success at $k = 6$ (0.565) exceeded the prediction (0.543) while $k = 4$ fell short (0.335 against 0.407). Determine whether a single value of $p$ can explain all five rows within their sampling errors, and say what measurement would settle it.

**3.3** Argue whether the multi-start law can be used to certify a global solution, or only to budget one.
