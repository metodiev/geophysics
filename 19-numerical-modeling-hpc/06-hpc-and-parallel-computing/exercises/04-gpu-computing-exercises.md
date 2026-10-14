# Exercises — 19-06-04 GPU Computing: CUDA, OpenCL and Portability Layers

Attempt these before reading the
[solutions](./04-gpu-computing-solutions.md). The lesson is
[04 GPU Computing: CUDA, OpenCL and Portability Layers](../04-gpu-computing.md).
**No GPU is used by these exercises or by the demonstration**; the thread
geometry of the sector counts is a stated assumption.

## ★ Foundational

**★1.** Assuming 32-byte sectors holding 4 doubles, compute the sectors touched by
a warp of 32 lanes accessing every 3rd double.

**★2.** State the crossover size implied by a $0.37\ \mu\mathrm{s}$ fixed cost and
a $0.1848$ ns marginal cost per element.

**★3.** State the two quantities compared in the gather-versus-slice table and
their measured values.

## ★★ Applied

**★★4.** Compute the per-element cost of the gather ($4.708$ ms) and slice
($1.646$ ms) forms on a $1024^{2}$ grid, and the time a $10^{5}$-step run would
take in each form.

**★★5.** A $10^{6}$-term accumulation must be accurate to $10^{-8}$ relative.
Using the printed fp32 and fp64 errors, decide the precision and justify it.

**★★6.** Explain why the measured CPU stride penalty is $1.11\times$ at stride 8
while the sector arithmetic predicts $4\times$ more sectors.

## ★★★ Research-oriented

**★★★7.** Design an experiment that decides whether the gather stencil's cost is
indexing arithmetic or memory transactions, and state the observable for each.

**★★★8.** A portability layer is used to run one kernel on two devices. State the
three things it does not guarantee, and for each give a test that would detect the
difference.
