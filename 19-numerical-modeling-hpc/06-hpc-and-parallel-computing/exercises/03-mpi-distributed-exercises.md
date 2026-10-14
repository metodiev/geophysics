# Exercises — 19-06-03 Distributed-Memory Parallelism with MPI

Attempt these before reading the
[solutions](./03-mpi-distributed-solutions.md). The lesson is
[03 Distributed-Memory Parallelism with MPI](../03-mpi-distributed.md). All
configurations are **SYNTHETIC**; the interconnect parameters used by the model
are **assumed**, and the demonstration states them.

## ★ Foundational

**★1.** Compute the halo fraction for $p = 16$ equal bands on a $512^{2}$ grid,
and for $p = 64$ bands.

**★2.** State why the parallel and serial Jacobi results in the demonstration are
bitwise identical, in terms of the arithmetic each point performs.

**★3.** For $p = 8$ bands, state the number of messages per sweep and the bytes
per rank per sweep, and convert the bytes to kB.

## ★★ Applied

**★★4.** With $t_{\text{sweep}} = 0.461$ ms, $\alpha = 5\ \mu\mathrm{s}$ and
$\beta = 10$ GB/s, reproduce the comm/compute ratio at $p = 4$ and at $p = 16$.

**★★5.** Using the same parameters, find the $p$ at which the comm/compute ratio
reaches $1.0$ for this $512^{2}$ grid, and state whether the model is credible
there.

**★★6.** The pairwise tree and the linear gather differ by
$2.22\times10^{-16}$ on $16$ values. Convert that difference into ulp of the
result and state what it implies for a reproducibility claim.

## ★★★ Research-oriented

**★★★7.** Design a weak-scaling experiment for this solver: state what is held
constant, predict the comm/compute ratio from the same two parameters, and state
how the predicted efficiency curve differs from the strong-scaling table.

**★★★8.** A code exchanges halos with blocking `Send`/`Recv` in a ring, and
hangs intermittently. State the two candidate causes the lesson distinguishes and
the observable that separates them.
