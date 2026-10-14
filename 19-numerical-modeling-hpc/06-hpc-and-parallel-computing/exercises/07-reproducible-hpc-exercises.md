# Exercises — 19-06-07 Reproducibility and Provenance in HPC Workflows

Attempt these before reading the
[solutions](./07-reproducible-hpc-solutions.md). The lesson is
[07 Reproducibility and Provenance in HPC Workflows](../07-reproducible-hpc.md).
All arrays and chunk counts are **SYNTHETIC**; every ulp difference is measured.

## ★ Foundational

**★1.** The decomposition table spans $-604.9947385276926$ to
$-604.9947385276923$. Compute the absolute spread and express it relative to the
value.

**★2.** State what `math.fsum` guarantees about order dependence and what it costs.

**★3.** State the difference between "the result is reproducible" and "the result
is bitwise reproducible across pool sizes at a fixed decomposition".

## ★★ Applied

**★★4.** A for-loop accumulation differs from numpy's pairwise sum by $-63.0$ ulp
on $200\,000$ values. Using $\epsilon = 2.22\times10^{-16}$ and the printed
absolute difference $7.162\times10^{-12}$, verify the ulp count.

**★★5.** A checkpoint is written with six digits per value and the round trip's
largest absolute error is $4.999\times10^{-7}$. State the consequence for a
restart that must reproduce the trajectory bitwise.

**★★6.** Two manifests differ only in `dt_s` ($0.004$ against $0.0041$). State
whether their digests can coincide, and why canonical key ordering is required
for the question to be answerable at all.

## ★★★ Research-oriented

**★★★7.** Write a reproducibility claim for a solver, then state three
experiments that would falsify it and the observable each would use.

**★★★8.** Design a provenance record for a run that spans two devices and three
pool sizes, and state which fields exist because of this lesson's measurements.
