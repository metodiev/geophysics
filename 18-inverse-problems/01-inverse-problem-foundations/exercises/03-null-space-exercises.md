# Exercises — 18-01-03 Null Space, Non-Uniqueness and Equivalence Classes

Attempt these before reading the
[solutions](./03-null-space-solutions.md). The lesson is
[03 Null Space and Non-Uniqueness](../03-null-space.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A $5\times16$ ray-path matrix has singular values
$2.6458, 2, 2, 1.7321, 1.4142$. State rank, the dimension of
$\operatorname{range}(G)$, the dimension of $\mathcal{N}(G)$ and verify
rank-nullity.

**★2.** For the same problem, one ray covers cells 2 and 3 with equal weight.
Write down a null vector and evaluate $G\mathbf{n}$.

**★3.** Cells 8 and 11 are visited by no ray. Explain in one sentence why
$\mathbf{e}_8$ is a null vector and what practical consequence it has for the
interpretation of those cells.

## ★★ Applied

**★★4.** With bounds $0\le m_j\le1$ the feasible interval of cell 10 is
$[0.2000,1.0000]$. The diagonal reading is $1.2$ and cells 0, 5, 15 have row-sum
caps $0.4$, $0.3$, $0.3$. Reproduce the lower bound by hand and state which
measurement produced it.

**★★5.** The interval of $m_3+m_7+m_{11}+m_{15}$ is $[0,2.0]$ while the interval of
$m_0+m_1+m_2+m_3$ is $[0.4,0.4]$. Explain the difference using
$\operatorname{range}(G^{\!\top})$.

**★★6.** Verify $\kappa(G^{\!\top}G) = \kappa(G)^{2}$ for
$\sigma = (2.6458,1.4142)$ with rank $5$, and state how many digits of accuracy in
the model a matrix with $\kappa(G) = 10^{8}$ would leave in double precision when
the normal equations are used.

## ★★★ Research-oriented

**★★★7.** A colleague presents a tomographic model from a survey with 40 rays and
200 cells, claiming "the ray coverage is good, so each cell is constrained".
Design the smallest analysis that would test the claim, state what you would
report instead of per-cell values, and give the one number that settles the
"coverage" argument.

**★★★8.** Extend the interval analysis of the demonstration to intervals of
*products* of parameters (e.g. $m_0 m_{10}$) and explain why the result is not the
product of the individual intervals. State what class of problem the extended
analysis becomes and one computational method that scales to $10^{4}$ parameters.
