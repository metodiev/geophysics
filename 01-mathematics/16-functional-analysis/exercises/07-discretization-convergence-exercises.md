# Exercises — 01-16-07 Discretisation, Convergence and Regularisation Discrepancy

Attempt these **closed-book** before opening the
[solutions](./07-discretization-convergence-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: the kernel is $K(s) = (z/\pi)/(s^2+z^2)$ with $z = 0.05$ on $[0,1]$,
discretised on $n$ nodes with spacing $h$; $\delta$ is the noise norm, fixed at a
1 per cent relative level; $\alpha$ is the Tikhonov parameter and
$R_\alpha = (F^{\mathsf T}F+\alpha I)^{-1}F^{\mathsf T}F$. Errors are weighted
$L^2$ on the model grid. Report the residual *and* the model norm throughout.

---

## ★ Foundational

**★1.** Name the three errors carried by a regularised inversion. State how each
behaves as $h\to0$ at fixed $\alpha$ and fixed $\delta$, and say which one does not
shrink.

---

**★2.** Define the regularisation discrepancy in your own words and explain why it
is the practically relevant quantity when the theory's limit $\delta\to0$ is not
available.

---

**★3.** State the two conditions on $\alpha(\delta)$ in the convergence theorem for
Tikhonov regularisation, and explain what goes wrong if each is violated. Why is a
*source condition* needed before any convergence *rate* can be quoted?

---

## ★★ Applied

**★★4.** From the table of Section 1.1 of the lesson, compute the ratio of
$\lambda_{\min}$ between consecutive grids and the ratio of condition numbers.
Show that $\log_{10}(\text{condition})$ is approximately linear in $n$ and report
the slope per node.

---

**★★5.** Using the fixed-$\alpha$ table, compute the ratio of the model error at
$n = 20$ to that at $n = 160$ for $\alpha = 10^{-1}$ and for $\alpha = 10^{-3}$.
Explain why one is ≈1 and the other is ≈0.64, and what the difference says about
which regime each $\alpha$ is in.

---

**★★6.** Consider the $n = 40$ column of the discrepancy-principle table:
$\alpha_{\text{disc}} = 3.224\times10^{-3}$, residual $=\delta = 3.067\times10^{-3}$.
Argue that the residual is monotone increasing in $\alpha$, bracket the root by
evaluating the residual at $\alpha = 10^{-3}$ and $\alpha = 5\times10^{-3}$ (the
lesson's fixed-$\alpha$ table gives $2.031\times10^{-3}$ at the first), and state
the bisection that locates $\alpha_{\text{disc}}$ to three significant figures.

Then check the triangle inequality: the residual at that $\alpha$ measured against
the *exact* data is $2.200\times10^{-3}$ (computed for these solutions). Verify
$\lvert\lVert Km-d^\delta\rVert - \lVert Km-d\rVert\rvert \le \lVert d^\delta -
d\rVert$.

---

## ★★★ Research-oriented

**★★★7.** Reproduce the Landweber iteration at $n = 80$ and, for
$j = 25, 50, 100, 200, 400$, report the model error, the residual, and the filter
factor of the mode whose $\lambda_k$ is closest to the cutoff value
$\lambda^\ast = \ln 2/(\tau j)$ implied by $f_k^{(j)} = 1-(1-\tau\lambda_k)^j = 0.5$.

(a) Tabulate $j$, the index $k$ of the mode nearest $\lambda^\ast$, and that mode's
filter factor.
(b) Show that the identified index increases with $j$ and that the filter factor at
it is ≈0.5 in every case.
(c) Use the moving cutoff to predict the optimal stopping index from the noise
level, and compare with the measured optimum.

---

**★★★8.** Redo the refinement study with the inverse crime removed: synthesise the
data on the $n = 320$ grid, invert on $n = 20, 40, 80, 160$.

(a) Report the model-error sequence at fixed $\alpha = 10^{-3}$ and with the
discrepancy principle.
(b) Compare with the crime-committing results of the lesson.
(c) State whether a plateau appears that is *not* explained by the noise level, and
identify it with the existence floor of lesson 01-16-05 if it does.

---

**★★★9.** For this kernel on $[0,1]$ the singular values satisfy
$\sigma_k \approx e^{-\pi zk}$, because the $k$-th singular function has about
$k/2$ cycles per unit length and the Fourier multiplier is $e^{-2\pi zf}$.

(a) Using the filter knee $\sigma_k = \sqrt\alpha$, derive
$k^\ast(\alpha) = \ln(1/\alpha)/(2\pi z)$ and evaluate it for
$\alpha = 10^{-1}, 10^{-3}, 10^{-8}$ with $z = 0.05$.
(b) Compare each with the measured $\operatorname{tr}R_\alpha$ ($7.75$, $22.56$,
$60.24$) and report the ratio. Explain the systematic offset.
(c) Hence show that the resolved index is independent of the mesh while the
retained *fraction* of the Nyquist band falls like $h$, and explain why no
polynomial scaling $\alpha_n\propto h^p$ makes the resolved band scale like the
Nyquist wavenumber.
