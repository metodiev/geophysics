# Exercises — 01-14-02 Unconstrained Minimisation: Gradient, Newton, Quasi-Newton

Attempt these **closed-book**, on paper, before opening the
[solutions](./02-unconstrained-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** For the quadratic $f(m) = \tfrac12(m-m^{*})^{\mathsf{T}}A(m-m^{*})$ with
$A \succ 0$, eigenvalues $\mu < L$, derive the iteration error
$e_{k+1} = (I - \alpha A)e_k$ for the fixed-step update
$m_{k+1} = m_k - \alpha\nabla f(m_k)$.

(a) State the range of $\alpha$ for which the iteration converges.
(b) State the optimal $\alpha$ and the resulting worst-case contraction factor.

**★2.** Write out the BFGS update (2.4) of the lesson for $n = 1$, where $s$ and
$y$ are scalars, and show that the result is $B = s/y$. Then explain why this is
the secant approximation to $1/f''$ and confirm that on a quadratic it gives the
exact inverse curvature after one step.

---

## ★★ Applied

**★★3.** A quadratic has $\kappa = 100$ and the iteration is stopped when
$\|\nabla f\| \le 10^{-8}\|\nabla f_0\|$.

(a) Use $k \approx (\kappa/2)\ln(1/\varepsilon)$ to predict the iteration count.
(b) Compare with the measured count of $922$ in
`code/unconstrained_demo.py` Section 2 and explain the agreement (or lack of it).

**★★4.** Gradient components are supplied by central differences with step $h$.

(a) Write down the truncation and round-off terms and derive the optimal $h$
given a relative evaluation error $\epsilon$.
(b) For binary64 ($\epsilon = 2.2\times10^{-16}$) compute the optimal $h$ and the
resulting gradient accuracy, and compare with the measured Rosenbrock values
$3.786\times10^{-9}$ at $h = 10^{-6}$ and $7.069\times10^{-7}$ at $h = 10^{-8}$.

**★★5.** Derive the Newton step from the second-order Taylor model of $f$ about
$m_k$, and say what property of $f$ makes the step exact. Then explain, from the
same expansion, why an indefinite Hessian makes the step unreliable.

**★★6.** For $f(x) = \log(1 + x^{2})$, start Newton's method at $x = 2$ with no
line search.

(a) Compute the first four iterates by hand.
(b) Explain the growth pattern and identify where the method's assumption fails.
(c) State one modification that repairs it, with the reason.

---

## ★★★ Research-oriented

**★★★7.** Consider the Broyden class of quasi-Newton updates. Explain, without
deriving the full algebra, why BFGS rather than DFP became the default for
large-scale optimisation, and design a numerical experiment on the Rosenbrock
function that would distinguish the two: state the controlled variables, the
measured quantity, and the number of runs needed for the comparison to be
meaningful.

**★★★8.** A practitioner reports that their inversion "converges in 500
iterations" using a preconditioned conjugate-gradient inner solver. Design an
experiment to separate the cost due to (i) the condition number of the
normal-equation matrix, (ii) the finite-difference gradient accuracy, and (iii)
the stopping tolerance. State what you would hold fixed, what you would vary, and
what observable would identify each contribution.
