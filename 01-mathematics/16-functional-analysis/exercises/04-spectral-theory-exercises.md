# Exercises — 01-16-04 Spectral Theory of Operators and Eigenfunction Bases

Attempt these **closed-book** before opening the
[solutions](./04-spectral-theory-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $K$, $L$, $F$ denote linear operators; eigenvalues of a self-adjoint
operator are written $\lambda_k$ in decreasing order of magnitude unless stated;
the second-difference matrix on $n$ interior nodes has spacing $h = 1/(n+1)$;
$R_\alpha = (F^{\mathsf T}F+\alpha I)^{-1}F^{\mathsf T}F$. State the norm in every
error you quote.

---

## ★ Foundational

**★1.** Prove that a self-adjoint operator has real eigenvalues and that
eigenvectors belonging to distinct eigenvalues are orthogonal. State where each
hypothesis is used.

---

**★2.** Show that $4\sin^2(k\pi h/2)/h^2 < k^2\pi^2$ for all $h>0$ with $kh<1$,
and interpret the result with the Rayleigh quotient. Why does this make
finite-element eigenvalues lower bounds?

---

**★3.** State the spectral theorem for a compact self-adjoint operator. Explain
in two sentences why the nonzero eigenvalues can accumulate only at zero, and why
that is equivalent to compactness.

---

## ★★ Applied

**★★4.** (a) For the separable kernel with amplitudes $a = (1, 0.4, 0.1, 0.02)$,
show that the relative truncation error after $r$ terms in the **operator norm**
equals $\lvert a_{r+1}\rvert/\lvert a_1\rvert$, and evaluate it for $r = 1,2,3$.

(b) For the gravity kernel of Section 3 of the lesson, the demonstration reports
**entrywise** relative truncation errors of $9.613\times10^{-1}$,
$8.833\times10^{-1}$ and $6.770\times10^{-1}$ for $r = 1, 2, 4$. Compute the
corresponding operator-norm values from the quoted eigenvalues and explain why
the entrywise values are the larger of the two.

---

**★★5.** Explain why the number of modes with wavenumber below $K$ on a
fixed-fixed string of length $L$ is approximately $KL/\pi$, and evaluate it for
$L = 25$ m and $K = 40$ rad/m. Compute the first two eigenvalues of that string
and their spacing, and state what happens to the spacing when $L$ is doubled.

---

**★★6.** Derive the eigenvalues of the three-point second-difference matrix by
substituting $v_i = \sin(ik\pi h)$, state the largest eigenvalue and its limit as
$h \to 0$, and compute that limit for $h = 1/25$.

---

## ★★★ Research-oriented

**★★★7.** Show that $\operatorname{tr}R_\alpha \le n$ for the resolution matrix
(1) of the lesson, and that $\lVert R_\alpha - I\rVert \to 0$ as $\alpha \to 0$
when $F$ has full column rank.

Then compute $\operatorname{tr}R_\alpha$ by hand at $\alpha = 10^{-2}$ for the
*separable* kernel of Section 2.2 with $a = (1, 0.4, 0.1, 0.02)$, using
$\operatorname{tr}R_\alpha = \sum_k(1+\alpha/a_k^2)^{-1}$ over the nonzero
eigenvalues, and state how many parameters the data resolve at that $\alpha$.

---

**★★★8.** Implement the resolution matrix for the gravity kernel at $z = 0.05$
with $n = 60$ and compute, for $\alpha = 10^{-2}, 10^{-3}, 10^{-4}$, the
half-width of the row at the **edge** of the model (parameter index 1) rather
than at the centre.

(a) Report the three edge half-widths and compare with the centre ones from the
lesson ($5, 3, 3$ cells at those $\alpha$).
(b) Explain the difference in terms of the shift-invariance of the kernel and the
absence of neighbouring parameters on one side.
(c) State the implication for interpreting an inverted model near a survey
boundary.

---

**★★★9.** Take the interval Laplacian with the three-point discretisation and
compute $\lambda_{\max}$ for $n = 24, 48, 96, 192$ using
$\lambda_{\max} = 4\cos^2(\pi h/2)/h^2$.

(a) Tabulate $\lambda_{\max}$ and $4/h^2$ and report the ratio.
(b) Tabulate $\lambda_{\max}/\lambda_{\min}$ for each $n$ and report the observed
scaling with $n$.
(c) Explain why this ratio, not the physical conditioning of the problem,
determines the iteration count of a Krylov solver for a fixed tolerance.

---

**★★★10.** Write a short paragraph for a paper reporting a normal-mode
measurement, stating: what operator's spectrum is being measured; why the
spectrum is discrete and what would make it continuous; the role of the boundary
conditions in fixing the eigenvalues; and what a "split multiplet" means in terms
of the perturbation of the operator. Every claim must be supported by the theory
of this lesson.
