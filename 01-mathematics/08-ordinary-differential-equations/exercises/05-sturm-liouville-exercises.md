# Exercises — 01-08-05 Sturm–Liouville Theory and Eigenfunction Expansions

Attempt these **closed-book** before opening the
[solutions](./05-sturm-liouville-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Companion lesson: [05 Sturm–Liouville Theory](../05-sturm-liouville.md).

---

## ★ Foundational

**★1.** Put each equation into self-adjoint form
$-(py')' + qy = \lambda wy$ and identify $p$, $q$ and $w$:

(a) $y'' + \lambda y = 0$
(b) $(1-x^{2})y'' - 2xy' + \lambda y = 0$
(c) $y'' + 2y' + \lambda y = 0$
(d) $xy'' + y' + \dfrac{\lambda}{x}y = 0$

State in each case whether the interval endpoint is regular or singular, and
what boundary condition replaces the usual one where it is singular.

---

**★2.** Solve the eigenvalue problem $y'' + \lambda y = 0$ on $[0,2]$ with
$y(0) = 0$ and $y'(2) = 0$.

(a) Give $\lambda_n$ and $y_n(x)$ for $n = 0,1,2,3$, numerically.
(b) State the weight function and the value of $\int_0^{2}y_n^{2}w\,dx$.
(c) Verify orthogonality numerically for the pair $(n,m) = (0,1)$.

---

**★3.** For the same problem, expand $f(x) = x$ on $(0,2)$ in the eigenfunctions.

(a) Compute $b_0$, $b_1$, $b_2$ in closed form and numerically.
(b) Tabulate the $L^{2}$ error of the partial sums for $N = 1, 2, 3, 5, 10, 20,
50$ terms.
(c) Determine the observed convergence rate as a power of $N$ from your table,
and explain it in terms of the smoothness of the periodic extension of $f$.

---

## ★★ Applied

**★★4.** Legendre's equation is
$-\dfrac{d}{dx}\left[(1-x^{2})\dfrac{dy}{dx}\right] = \lambda y$ on $[-1,1]$,
with eigenvalues $n(n+1)$ and eigenfunctions $P_n$.

(a) Express $x^{2}$ as a combination of $P_0$ and $P_2$.
(b) Using orthogonality only, compute $\int_{-1}^{1}x^{2}P_3(x)\,dx$ and
$\int_{-1}^{1}x^{2}P_2(x)\,dx$. State which integral is zero and why, *before*
evaluating either.
(c) State what replaces the boundary condition at $x = \pm1$ and why.

---

**★★5.** Consider $-(xy')' = \lambda\,y/x$ on $[1,e]$ with $y(1) = y(e) = 0$, so
that $p = x$, $q = 0$ and $w = 1/x$.

(a) Show by the substitution $t = \ln x$ that this problem is *identical* to
$-Y'' = \lambda Y$ on $[0,1]$ with $Y(0) = Y(1) = 0$, and hence that
$\lambda_n = n^{2}\pi^{2}$ with $y_n = \sin(n\pi\ln x)$.
(b) Explain in one sentence why the weight $w = 1/x$ is essential for that
equivalence — what goes wrong if it is omitted?
(c) Compute the Rayleigh quotient of the admissible trial function
$y = \ln x\,(1-\ln x)$ and compare with $\lambda_1$.

---

**★★6.** A slab of thickness 2 m has $\kappa = 2\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}$,
with one face held at zero and the other insulated ($u(0,t) = 0$,
$\partial_xu(2,t) = 0$).

(a) Using the eigenfunctions of ★2, compute the decay rate and time constant of
the first three modes.
(b) Compute the amplitude of each of those modes at a time equal to the
time constant of mode 0, as a fraction of its initial value.
(c) State which mode controls the long-time behaviour and what that means for
the practical cooling time of the slab.

---

## ★★★ Research-oriented

**★★★7.** For the problem of ★5, carry out a two-term Rayleigh–Ritz calculation
with the trial space

$$\operatorname{span}\left\{\ln x\,(1-\ln x),\ \left(\ln x\right)^{2}
\left(1-\ln x\right)^{2}\right\}.$$

(a) Set up the generalised eigenvalue problem
$\det(\mathsf{A}-\lambda\mathsf{B}) = 0$ and state what each entry of
$\mathsf{A}$ and $\mathsf{B}$ is as an integral.
(b) Solve for the smaller root and report it to seven significant figures.
(c) State the excess over $\lambda_1 = \pi^{2}$, and compare with the excess of
the one-term trial function of ★5(c).
(d) Explain, in one sentence, why the result you obtained must be an *upper*
bound whatever the trial space, and add the one sentence of algebra that
justifies it.

---

**★★★8.** Show that the boundary term in the Lagrange identity vanishes for
**Robin** conditions $\alpha y(a)+\beta y'(a) = 0$ and
$\gamma y(b)+\delta y'(b) = 0$ with all four constants non-zero, and then
construct a pair $(y,z)$ and an operator for which it does *not* vanish.

(a) Carry out the algebra for the Robin case, evaluating the bracket
$p(zy'-yz')$ at each endpoint.
(b) Give the simplest non-separated — that is, mixed-endpoint — boundary
condition for which the operator fails to be symmetric, and state physically
what kind of problem produces one.
(c) Compute both sides of the Lagrange identity numerically for
$p = 1$, $y = \cos\pi x$, $z = \sin 2\pi x$ on $[0,1]$ with $z$ satisfying
Dirichlet conditions and $y$ not satisfying them, and state the value you obtain.

---

## Extension ideas

- Show that the Legendre problem is singular at both endpoints and that the
  boundedness requirement is what selects $P_n$ rather than the second,
  unbounded solution (the Legendre function of the second kind).
- Derive the Rayleigh–Ritz equations by minimising $R[y]$ over
  $y = \sum_ic_i\phi_i$ and setting $\partial R/\partial c_i = 0$; identify where
  the generalised eigenproblem appears.
- For the heat problem of ★6, compute the temperature at the insulated face
  after one time constant of the fundamental mode, taking the initial condition
  to be uniform at $u = 1$ and expanding in the eigenfunctions. State how many
  modes you need for 1 % accuracy and why.
