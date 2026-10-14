# Exercises — Gradient, Gauss-Newton and Full Newton Methods

Refer to [the lesson](../02-gradient-and-newton.md). All models are SYNTHETIC.
Demo: `../code/gradient_newton_demo.py`.

## ★ Foundational

**1.1** For $f(u) = \tfrac12 u^{\mathsf T}Au - b^{\mathsf T}u$ with $A = \operatorname{diag}(1, 100)$, cite the steepest-descent rate $1 - 2/(\kappa+1)$ and evaluate it.

**1.2** Define the Gauss–Newton Hessian $J^{\mathsf T}J$ and state one property it always has that the true Hessian does not.

**1.3** The demo measured steepest descent needing 1287 iterations and CG 17 iterations to reach the same tolerance at $\kappa = 100$. Verify the order of magnitude of the steepest-descent count from $1 - 2/(\kappa+1) = 0.98020$.

## ★★ Applied

**2.1** Given the residual vector $r(u)$ and its Jacobian $J$, write the damped (Levenberg–Marquardt) update and explain what happens to the step as $\lambda \to \infty$.

**2.2** The demo measured the nonlinear race: steepest descent 348 iterations, Gauss–Newton 5, full Newton 8, LM 5. Compute the ratio 348/5 and state what the ratio says about the second-order information.

**2.3** Reproduce the indefinite-Hessian warning: at $(0.2, 2.0)$ the demo measured $\lambda_{\min}(H) = -0.17826$ while $J^{\mathsf T}J$ stayed positive definite with $\lambda_{\min} = 2.457\times10^{-3}$. Explain the sign difference.

## ★★★ Research-oriented

**3.1** Design a damped Gauss–Newton scheme whose damping parameter is chosen by a trust-region argument, and measure the evaluation count against a fixed $\lambda$ on the demo's objective.

**3.2** The demo found one of 49 grid starts failing to converge, at $(1000,1000)$, because a Jacobian column was numerically zero. Characterise the set of such failure points for a stiff synthetic problem and state how you would detect them in practice.

**3.3** Argue for or against reporting the Gauss–Newton Hessian as the parameter covariance. Use at least two measured numbers from the lesson.
