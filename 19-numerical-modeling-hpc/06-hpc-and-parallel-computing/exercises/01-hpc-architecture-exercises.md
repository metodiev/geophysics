# Exercises — 19-06-01 Computer Architecture, Memory Hierarchy and Roofline Thinking

Attempt these before reading the
[solutions](./01-hpc-architecture-solutions.md). The lesson is
[01 Computer Architecture, Memory Hierarchy and Roofline Thinking](../01-hpc-architecture.md).
All workloads are **SYNTHETIC**; every timing quoted is a measurement on the
machine that ran the demonstration.

## ★ Foundational

**★1.** Compute the arithmetic intensity of $y \leftarrow ax + y$ under (a) a
three-array model (two reads, one write) and (b) the five-pass model the
demonstration actually measures.

**★2.** From the size sweep, state the working-set size (per array) at which the
measured rate first exceeds $100$ GB/s, and the rate at the smallest size.

**★3.** State which of the two regimes — overhead or plateau — explains the
$44.72$ GB/s measured at $8$ KB per array.

## ★★ Applied

**★★4.** Predict the run time of the scale kernel ($1$ flop, $16$ bytes per
element) from the copy kernel's measured $115.45$ GB/s at
$8\,388\,608$ elements, and compare with the measured $105.48$ GB/s.

**★★5.** A kernel performs $20$ flops and moves $24$ bytes per element. Using the
measured plateau of about $108$ GB/s, state whether it is memory bound or compute
bound, and quote the crossover intensity.

**★★6.** The stencil's naive form is measured at $8.305$ ms and the
copy-bandwidth prediction for its $112$ bytes per point is $4.061$ ms. State the
ratio and give the two candidate explanations the lesson lists.

## ★★★ Research-oriented

**★★★7.** Design an experiment that separates the two explanations of the
stencil's $2.045$ ratio: row-slice strides and per-call overhead. State the
observable for each and how you would distinguish them.

**★★★8.** A colleague reports $210$ GB/s from a copy kernel and uses it as a
peak-bandwidth figure for their stencil. State what is wrong with the transfer and
what measurement they should make instead.
