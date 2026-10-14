# Exercises — 17-08-05 Remote Sensing for Disaster Response

Attempt these before reading the
[solutions](./05-disaster-response-rs-solutions.md). The lesson is
[05 Remote Sensing for Disaster Response](../05-disaster-response-rs.md). All
models and values are **SYNTHETIC** teaching numbers.

## ★ Foundational

**★1.** A detector returns $\mathrm{TP} = 2806$, $\mathrm{FP} = 1035$,
$\mathrm{FN} = 3$. Compute precision, recall and $F_1$.

**★2.** With a revisit of $6$ days and a clear-sky probability of $0.6$, compute
the expected latency in days.

**★3.** State what *precision* and *recall* mean operationally for a flood map:
what does each error cost the responder?

## ★★ Applied

**★★4.** With $c_{\text{miss}} = 10$ and $c_{\text{fa}} = 1$, compute the cost
for (i) $\mathrm{FP} = 1035, \mathrm{FN} = 3$ and (ii)
$\mathrm{FP} = 365, \mathrm{FN} = 20$. Which threshold would you choose?

**★★5.** With $c_{\text{miss}} = 100$ and $c_{\text{fa}} = 1$, recompute the
costs for FP/FN pairs $(80, 126)$, $(365, 20)$ and $(1035, 3)$. State where the
optimum moves and why.

**★★6.** A change-threshold flags $4154$ pixels, of which $1329$ are saturated
soil and $2700$ are water. Compute the false-alarm fraction of the flagged set
and state what it means for a pixel-count damage total.

## ★★★ Research-oriented

**★★★7.** Design a validation of a rapid flood map for a fresh event, where no
ground truth yet exists. State the reference you would construct, how you would
handle its own uncertainty, the metric, and the timeliness requirement. A
specification that could not be executed is a failed answer.

**★★★8.** Explain why water beneath emergent vegetation is a *physical* false
negative in a radar flood map (not an algorithmic one), and describe one radar
configuration or accessory data set that could recover it.
