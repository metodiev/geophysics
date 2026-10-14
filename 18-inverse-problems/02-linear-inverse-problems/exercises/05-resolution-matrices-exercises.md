# Exercises — 18-02-05 Resolution and Information Matrices in Interpretation

Attempt these before reading the
[solutions](./05-resolution-matrices-solutions.md). The lesson is
[05 Resolution and Information Matrices](../05-resolution-matrices.md). All models
are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Define $R$, $D$ and $N$, and write the substitution that shows
$\hat{\mathbf{m}} = R\mathbf{m}_{\text{true}} + G^{+}\mathbf{e}$.

**★2.** State the four identities of the lesson and say what implementation error
each would catch.

**★3.** $\operatorname{tr}R = \operatorname{tr}D = 12$ for a 16-cell model with
12 rays. State what the two traces mean and why they are equal.

## ★★ Applied

**★★4.** The measured mean kernel width over the covered cells is
$4.0650\ \mathrm{km}$ with cells 1 km wide. (a) State the finest structure the
inversion can honestly report. (b) Explain why quoting the cell width (1 km) as the
resolution would be wrong by a factor of four.

**★★5.** A 2-cell checkerboard has $\lVert G\mathbf{p}\rVert/\lVert\mathbf{p}\rVert
= 0.1732$ and recovered fraction $0.7923$. (a) Compute the invisible energy
fraction. (b) Predict what happens to the *estimated amplitude* of the pattern if
the true amplitude is $0.08\ \mathrm{s}$. (c) Give the measurement that would make
the pattern resolvable.

**★★6.** Per-cell posterior sds run from $0.003189$ to $0.017106\ \mathrm{s}$; the
median three-cell-average sd is $0.002835\ \mathrm{s}$ against a median per-cell sd
of $0.009500\ \mathrm{s}$. (a) Compute the ratio. (b) Explain why a regional average
is better determined than any of its cells.

## ★★★ Research-oriented

**★★★7.** Write the reporting template you would attach to any inversion result,
specifying the fields (resolution, covariance, pattern tests, verification), and
justify each field with a measurement from this lesson.

**★★★8.** The information matrix is $F = G^{\!\top}C_d^{-1}G$. Extend the lesson's
analysis to correlated noise with $C_d$ an AR(1) matrix, and state (a) how the
eigenvalues change, (b) which model directions gain and which lose, and (c) the
diagnostic that tells you whether your weighting changed the conclusion.
