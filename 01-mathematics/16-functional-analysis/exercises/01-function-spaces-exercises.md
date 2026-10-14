# Exercises — 01-16-01 Vector Spaces of Functions, Norms and Inner Products

Attempt these **closed-book** before opening the
[solutions](./01-function-spaces-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $\Omega$ is a region with finite measure unless stated otherwise;
$\lVert\cdot\rVert_p$ is the $L^p$ norm of Section 3.2 of the lesson and includes
no quadrature weights unless explicitly written; $C[0,1]$ carries the supremum
norm unless stated. State the norm and the space in every answer that depends on
them.

---

## ★ Foundational

**★1.** Verify axioms (N1), (N2) and (N3) for $\lVert f\rVert_\infty$ on
$C[0,1]$. Then explain what fails about (N1) if functions are treated as
pointwise objects and the norm is $\lVert f\rVert_1$.

---

**★2.** Compute $\lVert f\rVert_1$, $\lVert f\rVert_2$ and
$\lVert f\rVert_\infty$ in closed form for $f(x) = \sin(\pi x)$ on $[0,1]$.
Report the three pairwise ratios, and state which two are independent of the
function and why.

---

**★3.** State the two ways to discretise $\lVert f\rVert_2$ on a uniform grid with
spacing $h$, say which is the Riemann sum, and compute the factor that relates
them. If a convergence study reports an error of $10^{-4}$ using the unweighted
form and $h = 10^{-3}$, what is the error in the weighted (continuum) norm?

---

## ★★ Applied

**★★4.** Prove that $\lVert f\rVert_p$ is non-increasing in $p$ on a set of
finite measure. Exhibit a function on $[0,1]$ for which
$\lVert f\rVert_\infty / \lVert f\rVert_1 > 3$, and give the numerical value.

---

**★★5.** State Hölder's inequality for $p = 1$, $q = \infty$ and its equality
condition. Use it to show that $\ell(m) = m(x_0)$ is a bounded functional on
$C[0,1]$ with the supremum norm. Now show that no constant $C$ satisfies
$\lvert m(x_0)\rvert \le C\lVert m\rVert_2$ for all $m \in L^2(0,1)$: construct a
sequence of functions whose ratio diverges, and compute the ratio for
$\varepsilon = 10^{-4}$.

---

**★★6.** Reproduce the Section 8 fit table (intercept, slope, cost, residual at
the bad pick) for the $L^2$, $L^1$ and $L^\infty$ criteria. Then repeat with the
outlier reduced from $+1.8$ s to $+0.2$ s and report the $L^2$ and $L^1$ results
side by side. What does the change tell you about when the norm choice matters?

---

**★★7.** Prove that $\max_{\lVert x\rVert_2 \le 1}\lVert x\rVert_1 = \sqrt{n}$ in
$\mathbb{R}^n$ and identify the vector that attains it. The demonstration reports
measured maxima of 3.0544, 8.4326, 25.7408 and 80.4228 for $n = 10, 100, 1000,
10^4$; compute the ratio of each to $\sqrt{n}$ and explain why the measured values
fall short.

---

## ★★★ Research-oriented

**★★★8.** A weighted least-squares misfit is
$\chi^2 = \sum_i (r_i/\sigma_i)^2$ with $\sigma_i = 0.05 + 0.02x_i$ on the same
pick set. Fit the line by minimising $\chi^2$ and report intercept, slope and
$\chi^2$.

(a) Compare the slope with the unweighted $L^2$ slope and with the true $0.5$.
(b) State precisely which picks gained influence and which lost it, in terms of
the ratio $\sigma_{10}/\sigma_1$.
(c) Explain why the weighted fit has a *larger* $\chi^2$ than the unweighted fit
has sum of squares, and why that is not a contradiction.

---

**★★★9.** Implement a Huber misfit with threshold $\gamma$,
$\rho(r) = r^2/2$ for $\lvert r\rvert \le \gamma$ and
$\rho(r) = \gamma(\lvert r\rvert - \gamma/2)$ otherwise, and fit the pick set of
Section 8 (outlier $+1.8$ s) for $\gamma \in \{0.05, 0.1, 0.2, 0.5, 1.0, 1.5,
2.0\}$.

(a) Tabulate the recovered slope against $\gamma$.
(b) Identify the range of $\gamma$ over which the answer changes from the $L^1$
answer to the $L^2$ answer, and give the two limiting slopes.
(c) Explain the transition in terms of which residuals exceed $\gamma$, and say
what this implies for the practice of choosing a Huber threshold from a robust
estimate of the noise scale.

---

**★★★10.** A colleague reports that their inversion "converged to a misfit of
0.4 per cent" and concludes that the model is accurate. Write a short critical
response that covers: (a) the norm in which the 0.4 per cent is measured; (b) the
possibility of a small norm error with a large pointwise error, using the
$f_n(x) = x^n$ example; (c) the units and weighting question; (d) whether 0.4 per
cent is below the noise level and what that would signify; (e) what additional
number would make the claim defensible.
