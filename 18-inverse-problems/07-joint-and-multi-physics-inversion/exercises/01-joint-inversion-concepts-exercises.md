# Exercises — 18-07-01 Why Joint Inversion: Complementary Sensitivities

Attempt these before reading the
[solutions](./01-joint-inversion-concepts-solutions.md). The lesson is
[01 Why Joint Inversion](../01-joint-inversion-concepts.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A method's model resolution matrix has
$\operatorname{diag}R = (0.95, 0.62, 0.31, 0.08)$ on four cells. State which
cells are resolved, which are averages of their neighbours, and compute
$\operatorname{tr}R$. Explain in one sentence what $\operatorname{tr}R$ counts.

**★2.** Operator $G_1$ has rank 6 at a $10^{-3}$ cut and 40 model cells;
$G_2$ has rank 10. The joint operator is not the sum of the ranks. State the
range of joint ranks that is *possible* in principle and the rank the
demonstration measured, and explain why the sum is not attained.

**★3.** A gravity-like datum measures $d = H\Delta\rho = 1.2000$ with
$\sigma = 0.020$. List three $(\Delta\rho, H)$ pairs that reproduce it exactly
and compute $\Delta\rho$ for $H = 4.5\ \mathrm{km}$.

## ★★ Applied

**★★4.** For the demonstration's two-parameter problem with
$\sigma_1 = 0.020$, $\sigma_2 = 0.10\ \mathrm{km}$ and the truth
$(H,\Delta\rho) = (4.00, 0.30)$, compute
$C_{\text{post}} = (G^{T}C_d^{-1}G)^{-1}$ by hand for $\rho = 0$ and verify
$\sigma_H = 0.1000$ km, $\sigma_{\Delta\rho} = 0.0090$ and
$\rho_{H\Delta\rho} = -0.832$. Then repeat for $\rho = 0.9$ and state which
quantity changed and which did not.

**★★5.** The demonstration's joint operator has a mean
$\operatorname{diag}R$ of 0.3500 against 0.1500 and 0.2500 for the individual
operators, yet 35 of 40 cells still have $\operatorname{diag}R < 0.5$. Write two
sentences a reviewer would accept: one about the gain, one about the limitation.

**★★6.** The equivalence curve $H\Delta\rho = 1.2000$ is exact, while the
linearised null direction is only tangent to it. Compute the product for a step
of $0.50$ along the normalised tangent $(H,-\Delta\rho)$ and compare with the
first-order prediction (zero change). State the order of the residual.

## ★★★ Research-oriented

**★★★7.** Design a joint experiment that removes the $H\Delta\rho$ ambiguity
*without* measuring $H$ directly, using a data set that constrains a different
function of the same two parameters (for example one measuring $\Delta\rho$
through a second, differently shaped kernel). Specify the forward operator, the
expected rank of the joint system, and the quantity that decides whether the
ambiguity is removed. A specification that could not be executed is a failed
answer.

**★★★8.** Section 5 reports $\sigma_{\Delta\rho}$ varying by a factor of 3.3
over $\rho \in (-0.9, 0.9)$. Construct a case in which the correlation is
*negative* and explain physically what shared error would produce it. Then state
the practical rule you would adopt for reporting joint-inversion uncertainty
when $\rho$ is unknown.
