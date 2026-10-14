# Exercises — 20-03-05 Adaptive Filtering and Noise Cancellation

Attempt these before reading the
[solutions](./05-adaptive-filtering-solutions.md). The lesson is
[05 Adaptive Filtering](../05-adaptive-filtering.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Apply one normalised LMS update with $M = 3$, $\mu = 0.5$,
$\mathbf{x} = [1, -1, 0.5]^{\top}$, $d = 2$, starting from $w = [0,0,0]^{\top}$.
Show every step.

**★2.** State the NLMS convergence bound on $\mu$ and explain why normalising by
the input energy makes the bound independent of the signal power.

**★3.** In a noise canceller, which signal is the output — the error $e$ or the
filter output $y$? Answer the same question for an adaptive line enhancer.

## ★★ Applied

**★★4.** Using the demo's step-size table, explain why the SNR improvement rises
and then falls as $\mu$ increases, naming the two competing effects.

**★★5.** The demo's filter-length sweep peaks at $M = 8$ for a 9-sample
interference path. Explain why $M = 128$ performs worse, and state whether that
means "longer filters are always worse".

**★★6.** A reference channel contains 10% of the desired signal in amplitude.
Predict the effect on the canceller output and design a test that would reveal it
from data alone.

## ★★★ Research-oriented

**★★★7.** Derive the excess mean squared error of NLMS to first order in $\mu$
and compare its predicted scaling with the measured floors at $\mu = 0.05$ and
$\mu = 0.005$ in the demo's convergence table.

**★★★8.** A canceller must track an interference path that changes every 2 s. State
how you would choose $M$ and $\mu$ jointly, and give a quantitative argument for
each.