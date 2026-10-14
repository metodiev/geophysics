# Exercises — 20-07-02 Compressive Sensing and Data Reconstruction

Attempt these before reading the
[solutions](./02-compressive-sensing-signals-solutions.md). The lesson is
[02 Compressive Sensing and Data Reconstruction](../02-compressive-sensing-signals.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Using $\mu(A) = \max_{i\neq j}\lvert a_i^{T}a_j\rvert /
(\lVert a_i\rVert_2\lVert a_j\rVert_2)$, compute $\mu$ for the two-column matrix
$A = [\,(1,0)^{T},\ (1,\varepsilon)^{T}\,]$ with $\varepsilon = 0.5$ and with
$\varepsilon = 0$. State what the second case means for recovery.

**★2.** A mask keeps $m$ of $n = 128$ samples with a uniform stride
$s = n/m$. Explain, using the aliasing rule of the classical sampling theorem,
why the coherence of the resulting Fourier sensing matrix is 1 for $s = 4$.

**★3.** For the phase-transition table, state the smallest $m$ with 3/3 exact
recovery for $k = 4$ and for $k = 8$, and compute $m/k$ for each.

## ★★ Applied

**★★4.** The alias set for the stride-4 mask is bins $\{8, 24, 40, 56\}$ for a
tone at bin 40. Verify with the folding rule that bin 8 folds to the same
sampled column as bin 40, and compute the alias frequencies in cycles/sample.

**★★5.** From the median-error table, describe the shape of the error surface:
for $k = 4$ the median is 0.913 at $m = 16$ and 0.000 for every $m \ge 24$; for
$k = 6$ the median is 1.091 at 16 and 0.000 from 24. Compute the fraction of the
grid cells that are "0.000" for each $k$ and comment on what the flat zero means.

**★★6.** Using the restricted-eigenvalue table, decide whether $m = 12$ samples
can identify a support of size $k = 2$ in this dictionary. Justify with the two
numbers given and state the caveat about their size.

## ★★★ Research-oriented

**★★★7.** Design a measurement of the *stopping* behaviour of the phase
transition under noise. Specify the noise level, the success criterion, the grid
in $(k, m)$, the number of trials, and the prediction for how the transition
curve moves as the noise level rises from 0 % to 20 % of the signal rms. State
which quantity you expect to be more sensitive and why.

**★★★8.** The lesson measures the phase transition with a debiasing step that
makes the error either $O(10^{-16})$ or $O(1)$. Remove the debiasing in thought:
predict the shape of the error table, and explain why the transition would be a
blur rather than an edge. Then state what the debiasing costs in a noisy
setting.
