# Exercises — 18-05-05 Hamiltonian Monte Carlo and Modern Samplers

Lesson: [05 Hamiltonian Monte Carlo and Modern Samplers](../05-hmc-and-modern-samplers.md).
Attempt these before reading the [solutions](./05-hmc-and-modern-samplers-solutions.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Show that the leapfrog map
$p \leftarrow p - \frac{\varepsilon}{2}\nabla U(m)$,
$m \leftarrow m + \varepsilon M^{-1}p$,
$p \leftarrow p - \frac{\varepsilon}{2}\nabla U(m)$
is exactly reversible: applying it with $-\varepsilon$ immediately after returns
the initial state.

**★2.** Using the measured coefficient $c \approx 0.13$ in
$\lvert\Delta H\rvert \sim c\,\varepsilon^{2}T$ at unit effective frequency,
estimate the step size that keeps the mean energy error below $0.01$ over a
trajectory duration $T = 1$.

**★3.** State the two properties of the Hamiltonian flow that justify omitting a
Jacobian from the acceptance ratio.

## ★★ Applied

**★★4.** From the measured energy-error table, compute the effective exponent
$\ln(\text{ratio})/\ln 2$ for each successive halving of $\varepsilon$ and state
which rows are in the asymptotic regime. Explain why a single fitted slope should
not be quoted as the order of the integrator.

**★★5.** Using the measured trajectory-length table, compute the ESS per gradient
evaluation at $L = 5$ and $L = 20$ and compare with $L = 10$. Explain the shape of
the curve.

**★★6.** Compute the factor by which a covariance-matched mass matrix improves the
ESS per gradient evaluation on the anisotropic target, from the measured table.
State why this factor is target-specific.

**★★7.** A production run reports acceptance $0.98$, split $\hat R = 1.001$ for
all parameters, and $14$ divergences. State the likely cause, the fix, and why the
acceptance rate did not reveal the problem.

## ★★★ Research-oriented

**★★★8.** Design a gradient check for a large inversion code that supplies an
adjoint gradient. State the test quantity, the perturbation sizes, the expected
scaling, and the acceptance threshold. Explain what a failure of the check would
look like and what it would not tell you.
