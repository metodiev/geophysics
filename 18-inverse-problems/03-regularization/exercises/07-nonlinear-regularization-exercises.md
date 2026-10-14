# Exercises — 18-03-07 Regularisation of Nonlinear Problems

Attempt these before reading the
[solutions](./07-nonlinear-regularization-solutions.md). The lesson is
[07 Regularisation of Nonlinear Problems](../07-nonlinear-regularization.md).
All models are **SYNTHETIC**. Reference values: 12 depths and 12 line densities,
48 stations; true depths a Gaussian ridge from $1.01$ to $3.09\ \mathrm{km}$;
noise $\sigma = 0.2727\ \mathrm{mGal}$ ($0.50\%$ of the peak);
$n\sigma^2 = 3.7127\times10^{-5}$; oracle $\alpha = 10^{-6}$ with relative model
error $0.21997$; discrepancy $\alpha = 6.392\times10^{-6}$ with $0.24095$.

## ★ Foundational

**★1.** Reproduce the first three damped Gauss–Newton iterations of the
one-parameter problem $F(u) = e^{-u}$, $d = 0.5$, $u_0 = 0$, and tabulate the
error after each step against the exact $u^\star = \ln 2$.

**★2.** The analytic Jacobian verification has an optimum step near
$h = 10^{-5}\ \mathrm{km}$ with a relative deviation of $1.073\times10^{-8}$.
Using the central-difference estimate $h^\star \approx \epsilon^{1/3}$ with
$\epsilon = 2.2\times10^{-16}$, compute $h^\star$ and compare.

**★3.** Write the damped Gauss–Newton system for the penalised objective and
state which symbol is the damping, which is the regularisation parameter, and
which is the linearisation point.

## ★★ Applied

**★★4.** The measured step-norm ratios over iterations 6–15 are $0.394$, $0.317$,
$0.298$, $0.300$, $0.311$. State the convergence order, compute the expected
factor by which the error falls over ten further iterations at that rate, and
explain why a quadratic method would show a *falling* ratio instead.

**★★5.** At $\alpha = 10^{-10}$ the demonstration measures a depth error of
$0.27381$ and a density error of $0.31140$; at $\alpha = 10^{-6}$, $0.29739$ and
$0.15912$. Compute the change in each block and explain the pattern in terms of
the depth–density trade-off.

**★★6.** At the $\alpha = 10^{-6}$ solution the data term is
$2.302913\times10^{-5} = 0.620\,n\sigma^2$ with $n\sigma^2 = 3.7127\times10^{-5}$.
Compute the admissible extra data term, and the value of $\chi^2/(n\sigma^2)$
that a model moved along $v_{-5}$ (max $\|\delta z\| = 0.6479\ \mathrm{km}$)
reaches. State whether that model is rejectable by the data.

## ★★★ Research-oriented

**★★★7.** Derive the IRLS weight $w_k = 1/\sqrt{(Dz)_k^2+\epsilon}$ from the
derivative of $\sqrt{(Dz)_k^2+\epsilon}$ and state the effective penalty as a
function of $\epsilon$ as $\epsilon\to0$.

**★★★8.** Design an experiment that measures how the depth-versus-density error
split depends on the penalty operator (magnitude only; depth roughness only;
densities roughness only; both), and predict which block degrades in each case.
