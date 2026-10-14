# Exercises — 18-08-01 Setting Up a Solvable Inverse Problem

Attempt these before reading the
[solutions](./01-problem-setup-solutions.md). The lesson is
[01 Setting Up a Solvable Inverse Problem](../01-problem-setup.md). All models
are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For the demonstration's grids, state which discretisations give
$\operatorname{tr}R$ above 6 and explain in one sentence why
$\operatorname{tr}R$ cannot exceed the number of observations.

**★2.** A cell has $\|G_{:,j}\| = 0.45$ in the demonstration's units and
$\sigma = 1.0$. State whether it is a parameter of the problem, and what would
have to change for the answer to become yes.

**★3.** Write the definition of $R$ and state the meaning of $R_{jj} = 0.95$,
$R_{jj} = 0.31$ and $\operatorname{tr}R = 4.94$ for a 40-cell model.

## ★★ Applied

**★★4.** For the 12- and 40-cell models the printed chi values are 0.851 and
0.424 and the model errors 0.6921 and 2.3886. Explain why chi < 1 is possible at
all, and which model you would report and with what caveat.

**★★5.** A colleague proposes an 80-cell grid to image a 0.5-km layer. Using the
sensitivity table, state whether the layer can be resolved, and if not, what the
purpose of the fine grid can legitimately be.

**★★6.** The condition number of $G^{T}G+\lambda D^{T}D$ grows from $2.29\times
10^{2}$ to $3.92\times10^{3}$ as the grid is refined. State two consequences for
the numerical solution and one for the interpretation.

## ★★★ Research-oriented

**★★★7.** Design the setup for a refraction experiment intended to resolve a
low-velocity layer of stated thickness at stated depth. Specify the data count,
the noise level you would require, the parameterisation, and the quantity you
would compute to demonstrate that the layer is resolvable. A specification that
could not be executed is a failed answer.

**★★★8.** The demonstration uses Gaussian kernels and a smoothness prior. Argue
whether the choice of prior can change the *rank* of the problem, and construct
a case in which two priors give different answers to "how many parameters are
resolved" for the same data.
