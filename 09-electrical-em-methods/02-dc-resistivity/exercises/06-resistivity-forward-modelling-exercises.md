# Exercises — 09-02-06 Forward Modelling Resistivity Data

Attempt these before reading the
[solutions](./06-resistivity-forward-modelling-solutions.md). The lesson is
[06 Forward Modelling Resistivity Data](../06-resistivity-forward-modelling.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute the reflection coefficient $k$ for a two-layer model with
$\rho_1 = 80$ and $\rho_2 = 400\ \Omega\,\mathrm{m}$.

**★2.** Write the first three image terms of the series for the model in ★1 with
$h = 5$ m, and evaluate the series to three terms at $r = 10$ m with
$I = 0.1$ A.

**★3.** State what the recurrence $R_N = 0$ means and why the recursion runs
from the bottom upwards.

## ★★ Applied

**★★4.** Verify the half-space limit analytically: show that the integrand in
the layered formula vanishes when all $k_i = 0$, and state the resulting
potential.

**★★5.** From the sensitivity table of the lesson, estimate the depth below
which the sounding at $a = 1$ m has essentially no information, and the depth
above which the $a = 48$ m spacing has essentially no information.

**★★6.** The lesson's null direction is
$\hat{v} = (+0.0007, +0.6899, +0.0153, +0.0767, -0.7196)$ in the order
$(\ln\rho_1, \ln\rho_2, \ln\rho_3, \ln h_1, \ln h_2)$. Verify that
$h_2\rho_2$ is conserved to first order along this direction.

## ★★★ Research-oriented

**★★★7.** Repeat the Jacobian and SVD analysis for a model whose third layer is
*conductive* relative to its neighbours, and predict from the structure of the
sensitivity kernel whether the null direction will be dominated by
$h_2/\rho_2$ (conductance) rather than $h_2\rho_2$ (resistance). Then state the
numerical test that would confirm your prediction without touching the data.

**★★★8.** A colleague proposes to use a neural network trained on a million
synthetic soundings to report five-layer models without uncertainty estimates.
State, using the null-space results of this lesson, the specific falsification
test you would demand, and what the network must output if it is to pass.
