# Exercises — 19-06-05 Domain Decomposition and Load Balancing

Attempt these before reading the
[solutions](./05-domain-decomposition-solutions.md). The lesson is
[05 Domain Decomposition and Load Balancing](../05-domain-decomposition.md). All
grids, velocity fields and work weights are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute the halo fraction for a $1024\times1024$ grid decomposed into
$16$ bands, and into a $4\times4$ block layout.

**★2.** State the makespan bound of a static contiguous schedule in one sentence,
and the bound of a dynamic work queue.

**★3.** The velocity field ranges over a factor $2.333$ and the per-column cost is
taken as $1/v$. State the range of the cost and why the two ratios are equal.

## ★★ Applied

**★★4.** From the printed equal-width loads $[51.6, 51.52, 88.16, 87.99]$, verify
the max/mean of $1.263$ and state the makespan penalty it implies in percent.

**★★5.** Explain why the balanced partition has cell counts
$[157, 154, 95, 106]$ rather than four equal counts, and state the cost this
choice carries.

**★★6.** With $f = 0.0551$, find the rank count at which the Amdahl efficiency
falls below $50\%$ and state the ceiling there.

## ★★★ Research-oriented

**★★★7.** Design a refinement of the sub-domain count that removes the
granularity bound of the lesson's Section 8, and state what it costs in halo
fraction and in communication messages.

**★★★8.** The measured makespan ratio is $1.336$ while the predicted ratio from
the work weights is $1.256$. List the two effects that explain the gap and state
which one is an artefact of the emulation.
