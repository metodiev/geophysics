# Exercises — 19-04-02 Pseudospectral Methods, Transforms and Aliasing

Attempt these before reading the
[solutions](./02-pseudospectral-solutions.md). The lesson is
[02 Pseudospectral Methods, Transforms and Aliasing](../02-pseudospectral.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A cosine of frequency 80 Hz is sampled at $f_s = 100$ samples/s. Compute
its alias frequency and state, in one sentence, whether any processing can
recover the true frequency.

**★2.** For a quadratic nonlinearity computed on $N = 64$ uniform periodic
points, state the highest mode an input at $m = 24$ can produce and the mode it
folds onto. (Note that an input mode above $N/2 = 32$ would itself be an alias
and not a well-defined input.)

**★3.** State the 2/3 rule, and state the condition on the input spectrum that
makes it exact in the band it keeps.

## ★★ Applied

**★★4.** A solution's spectrum has significant power up to $m = 20$ on a grid of
$N = 64$ points. Decide whether the naive product aliases; state the largest
input band the 2/3 rule permits; and compute the minimum padded grid size
$M$ satisfying $M \ge 4K$ for that band.

**★★5.** The lesson measures a naive relative error of 874% for
$k_1 = 10$, $k_2 = 12$ on 32 points, and 0.000% for $k_1 = 6$, $k_2 = 7$. Verify
both outcomes from the fold index, and predict the outcome for $k_1 = 11$,
$k_2 = 13$.

**★★6.** Explain in three sentences why reducing $\Delta t$ does not remove the
aliasing error of a nonlinear term, even though it does remove a truncation
error.

## ★★★ Research-oriented

**★★★7.** A code retains $N = 512$ modes and needs a cubic nonlinearity $u^3$
computed without aliasing. Derive the required input band and the required padded
grid size, and compare the cost with the quadratic case.

**★★★8.** Design a test that would detect an un-de-aliased quadratic term in a
code whose solution spectrum is narrow enough to be safe. Your test must be
executable as stated and must state what the code should produce with and without
de-aliasing.
