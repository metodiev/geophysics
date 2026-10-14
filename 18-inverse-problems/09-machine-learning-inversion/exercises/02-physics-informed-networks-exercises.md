# Exercises — 18-09-02 Physics-Informed Neural Networks

Attempt these before reading the
[solutions](./02-physics-informed-networks-solutions.md). The lesson is
[02 Physics-Informed Neural Networks](../02-physics-informed-networks.md). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the PINN loss for $-u''(z)=f(z)$ on $(0,1)$ with $u(0)=u(1)=0$,
identifying the collocation term, the boundary term and the weight $\beta$.

**★2.** Derive $\mathrm{d}^2u/\mathrm{d}z^2$ for
$u(z)=\mathbf{W}_2\cdot\tanh(\mathbf{W}_1 z+\mathbf{b}_1)+b_2$, showing the
intermediate quantities $h_j$, $\mathrm{d}h_j/\mathrm{d}z$ and
$\mathrm{d}^2h_j/\mathrm{d}z^2$.

**★3.** State the three rows of the comparison table (physics-only, data-only,
combined) with their L2 errors, and which row you would trust for extrapolation
outside the training interval.

## ★★ Applied

**★★4.** The data-only fit achieves a data rms of $2.36\times10^{-6}$ and an L2
error of 0.0626. Explain how both can be true simultaneously, and state which
number a practitioner who has only the training points would see.

**★★5.** With $f_{\text{wrong}} = 1.20 f$ the amplitude ratio is exactly 1.200.
Derive this from the linearity of the equation and state the general rule it
illustrates.

**★★6.** The physics-only fit has a physics residual of $4.275\times10^{-3}$
(rms) and an L2 error of $2.40\times10^{-5}$. Explain why the residual is larger
than the solution error, and what that says about using the residual as an error
estimate.

## ★★★ Research-oriented

**★★★7.** Design a PINN experiment that would *detect* a mis-specified source
term using only data that the training did not use. Specify the held-out data,
the diagnostic, and the decision rule. A specification that could not be executed
is a failed answer.

**★★★8.** For a PDE-constrained inverse problem (unknown coefficient field,
sparse data), compare a PINN formulation with a classical PDE-constrained least
squares in terms of (i) the information used, (ii) the cost per new data set, and
(iii) the guarantees available in each. State one setting in which each is
preferable.
