# Exercises — 19-01-03 Consistency, Stability and the Lax Equivalence Theorem

Attempt these before reading the
[solutions](./03-consistency-stability-solutions.md). The lesson is
[03 Consistency and Stability](../03-consistency-stability.md). All models are
**SYNTHETIC**. Numbers printed by `../code/consistency_stability_demo.py` may be
quoted directly.

## ★ Foundational

**★1.** For the upwind scheme with $C = 0.8$, write the amplification factor
$G(\theta)$ and compute $|G|$ at $\theta = 0$, $\pi/2$ and $\pi$.

**★2.** State the Lax equivalence theorem and the two hypotheses it needs.

**★3.** For the centred-in-space, forward-Euler-in-time scheme, state
$|G|^{2}$ and decide whether it is stable at $C = 0.3$.

## ★★ Applied

**★★4.** The upwind scheme at $C = 1.4$ starts from a perturbation of
$10^{-6}$ in the Nyquist mode. Predict the amplitude after 100 steps and state
how many steps are needed to exceed unity.

**★★5.** Apply the upwind operator to the exact solution
$u = \sin(2\pi(x-t))$ at $C = 0.5$ and derive the leading residual in the form
$C_1 h\,u_{xx}$. Then state what the residual is at $C = 1$ and why.

**★★6.** A run shows an error growing by a factor $1.118$ per step at the
highest mode of the grid. Identify the scheme and the Courant number, then state
what measurement would confirm the diagnosis.

## ★★★ Research-oriented

**★★★7.** Construct a scheme that is stable but *inconsistent* for
$u_t + au_x = 0$ (for example by using a deliberately wrong coefficient), predict
its convergence behaviour from Lax equivalence applied in reverse, and specify
the numerical experiment that would demonstrate it. State what a practitioner
would see first.

**★★★8.** Lax equivalence is stated for linear, well-posed problems. Choose a
nonlinear case relevant to geophysics (for example advection with a
velocity-dependent speed, or a variable-coefficient wave equation), explain
precisely which hypothesis fails, and give a measurement that shows a stable,
consistent scheme failing to converge to the exact solution.
