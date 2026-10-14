# Exercises — 07-03-04 Gravity Inversion and Its Severe Non-Uniqueness

Attempt these before reading the
[solutions](./04-inversion-gravity-solutions.md). The lesson is
[04 Gravity Inversion](../04-inversion-gravity.md). All models are **SYNTHETIC**.

## ★ Foundational

**★1.** Write $\mathbf{d} = \mathbf{A}\mathbf{m}$ for three stations and two cells,
and state the units of every entry.

**★2.** State the model resolution matrix for a Tikhonov-regularised linear
problem and explain why $\mathrm{trace}(\mathbf{R}) \le n$, the number of data.

**★3.** Give two distinct density distributions that produce the same field
outside their own support.

## ★★ Applied

**★★4.** The lesson's $\alpha$ table has a formal misfit floor of
$0.0109\ \mathrm{mGal}$ against a stated noise of $0.02\ \mathrm{mGal}$. Choose a
regularisation from the table and justify it against that mismatch.

**★★5.** Compute the mass of a body producing $0.30\ \mathrm{mGal}$ at
$1000\ \mathrm{m}$ depth under the point-mass assumption, then use the aperture
table to give the admitted depth and mass ranges for a $1\ \mathrm{km}$ aperture.

**★★6.** From the resolution table, state the depth at which
$\mathrm{diag}(\mathbf{R})$ falls below $0.1$ and explain the physical reason for
the depth dependence.

## ★★★ Research-oriented

**★★★7.** Derive the two-sheet annihilator condition for depths $h_1 < h_2$ and
show that the required amplitude ratio grows exponentially with $h_2-h_1$. Compute
the ratio for $k = 2\pi/500\ \mathrm{m^{-1}}$ and $h_2-h_1 = 2\ \mathrm{km}$.

**★★★8.** Design a survey and processing scheme that would reduce the admitted
mass range for the lesson's point mass from a factor $3.2$ to below $1.3$, stating
the aperture, the noise and any prior you assume. If the reduction cannot be
achieved by geometry alone, say what additional assumption you are forced to
make.
