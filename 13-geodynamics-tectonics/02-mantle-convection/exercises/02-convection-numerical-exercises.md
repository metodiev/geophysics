# Exercises — 13-02-02 Numerical Modelling of Mantle Convection

Attempt these before reading the
[solutions](./02-convection-numerical-solutions.md). The lesson is
[02 Numerical Modelling](../02-convection-numerical.md). All numbers refer to the
**SYNTHETIC** solver in `code/convection_numerical_demo.py`; $Ra_c = 27\pi^{4}/4$
is exact for free-slip boundaries.

## ★ Foundational

**★1.** For $\mathrm{CFL} = 0.7$, $\Delta z = 1/48$, $|u|_{\max} = 30$ and a
sampling interval $\Delta x = 2.8284/48$, compute the maximum stable time step and
the number of steps needed to reach $t_{\text{end}} = 0.5$.

**★2.** Compute the eigenvalue of the discrete second-derivative operator
$2(1-\cos\pi\Delta z)/\Delta z^{2}$ for $\Delta z = 1/48$ and compare it with
$\pi^{2}$. State what the difference implies for the accuracy of a Poisson solve.

**★3.** For $N_x = 49$ points, how many independent Fourier modes does a real FFT
return? Explain why the mean-mode coefficient of a uniform row of $1.0$ is $N_x$
rather than 1.0, and what goes wrong physically if this is forgotten.

## ★★ Applied

**★★4.** The scheme's amplification factor for a single mode is
$(1+\Delta t\,C)/(1+\lambda\Delta t)$ with $\lambda = \pi^{2}+k_c^{2}$ and
$C = Ra\,k_c^{2}/\lambda^{2}$. For $Ra = 800$, compute $\lambda$, $C$ and the
measured growth rate at $\Delta t = 0.01$. Compare with the analytic
$\sigma = -\lambda + C$ and state why the two differ.

**★★5.** From the lesson's Nusselt-number table ($Nu$ = 1.651, 3.103, 4.741,
5.862 at $Ra$ = 1000, 3000, 10000, 20000), compute the three local logarithmic
slopes and state which interval is closest to the asymptotic exponent.

**★★6.** The energy-balance check reports a top-to-bottom flux agreement of
$4.6\times10^{-3}$ but a maximum flux-profile deviation of $1.5\times10^{-1}$ at
$Ra = 10^{4}$. Explain in two or three sentences how both can be true, and what
each number tells you about the solution.

## ★★★ Research-oriented

**★★★7.** Design a grid-convergence study for this solver that would establish
the order of accuracy of the upwind advection scheme. State the grids, the
quantity you would converge, how you would estimate the order, and the result
that would show the scheme is first order.

**★★★8.** An earlier version of the code cooled the interior at a rate
proportional to $1/N_x$ per step. Explain the mechanism (what was mis-scaling),
describe the diagnostic that revealed it (the mean temperature drift in a purely
conducting state), and outline a unit test that would catch the same class of bug
in any transform-based Poisson solver.
