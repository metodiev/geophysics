# Exercises — 01-16-06 Tikhonov Regularisation and the L-Curve

Attempt these **closed-book** before opening the
[solutions](./06-regularization-theory-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $J_\alpha(m) = \lVert Fm-d\rVert^2 + \alpha\lVert m\rVert^2$;
$\sigma_k$ are the singular values of $F$; $R_\alpha =
(F^{\mathsf T}F+\alpha I)^{-1}F^{\mathsf T}F$ is the resolution matrix of lesson
01-16-04; $\delta$ is the noise norm; $m$ denotes both the number of data and a
model — the context makes it clear, and the number of data is written $n_d$ where
ambiguity is possible. State model units wherever $\alpha$ is quoted.

---

## ★ Foundational

**★1.** Derive $m_\alpha = (F^{\mathsf T}F+\alpha I)^{-1}F^{\mathsf T}d$ from
$J_\alpha$ by differentiation, and again from the augmented least-squares system
$\min\lVert\binom{F}{\sqrt\alpha I}m - \binom{d}{0}\rVert^2$. State the eigenvalue
bound that gives stability.

---

**★2.** Write $m_\alpha$ in the singular-value basis of $F$, define the filter
factor, and give its limits as $\sigma_k^2/\alpha\to\infty$ and $\to0$. State the
limit of the *coefficient* $\sigma_k/(\sigma_k^2+\alpha)$ in the same two regimes,
and explain why the two limits differ.

---

**★3.** Show that $\operatorname{tr}R_\alpha =
\sum_k\sigma_k^2/(\sigma_k^2+\alpha)$ is strictly decreasing in $\alpha$ for
$\alpha>0$, with $\operatorname{tr}R_\alpha\to n$ (for full column rank $n$) as
$\alpha\to0$ and $\to0$ as $\alpha\to\infty$.

---

## ★★ Applied

**★★4.** Evaluate $\operatorname{tr}R_\alpha$ by hand for the separable kernel of
lesson 01-16-04 with $a = (1, 0.4, 0.1, 0.02)$ at $\alpha = 0.1$ and
$\alpha = 0.01$, and state how many of the four retained parameters the data
resolve at each $\alpha$. Compare the $\alpha = 0.01$ result with the value
$2.46973702$ obtained in that lesson's exercise set.

---

**★★5.** Derive the curvature formula
$\kappa = (x'y''-y'x'')/((x')^2+(y')^2)^{3/2}$ for a parametric curve
$(x(t),y(t))$ and show that it is unchanged by a reparameterisation $t\to s(t)$.
Then evaluate it at the middle of the three consecutive L-curve points printed in
the lesson's table for $\alpha = 10^{-5}, 1.78\times10^{-5}, 3.16\times10^{-5}$,
with $(\lVert Km-d\rVert, \lVert m\rVert) = (0.001770, 0.415102)$,
$(0.001818, 0.399111)$, $(0.001867, 0.389301)$. The program reports a
full-precision curvature of 15.75 at that point; compare your value and explain the
difference and its implication for locating a corner.

---

**★★6.** Using the sensitivity table of Section 5, compute the model error at
$0.1\alpha_c$ and at $10\alpha_c$, report their ratio, and state whether the
error is decreasing or increasing with $\alpha$ in that range. Explain the sign
in terms of the bias and variance contributions.

---

**★★7.** Use $\alpha = \sigma_d^2/\sigma_m^2$ with
$\sigma_d = 0.01\lVert d\rVert$, $\lVert d\rVert = 0.274947$ and a prior
$\sigma_m = \lVert m_{\text{true}}\rVert/\sqrt3$ with
$\lVert m_{\text{true}}\rVert = 0.376565$. Report the implied $\alpha$ and
compare it with the discrepancy-principle value $2.474\times10^{-3}$ and the
L-curve corner $3.162\times10^{-5}$.

---

## ★★★ Research-oriented

**★★★8.** Implement the three parameter-choice rules — the L-curve corner by
maximum curvature, the discrepancy principle by bisection, and GCV — for noise
levels $\varepsilon = 10^{-1}, 10^{-2}, 10^{-3}$ on the gravity-kernel problem of
the lesson.

(a) Tabulate the three $\alpha$ and the three model errors at each noise level.
(b) Report which rule is most accurate at each level and which is most stable
across levels, defining "stable" explicitly.
(c) State which rule you would use for a data set whose noise covariance is
estimated rather than measured, and why.

---

**★★★9.** Replace the penalty $\lVert m\rVert^2$ by $\lVert Lm\rVert^2$ with $L$
the first-difference operator on the model grid.

(a) Write the modified estimator and its filter factors in the generalised
singular value decomposition of $(F,L)$ — or, if you prefer, in the eigenbasis of
$F^{\mathsf T}F + \alpha L^{\mathsf T}L$.
(b) Redo the L-curve and the discrepancy-principle comparison.
(c) Report how the model error and $\operatorname{tr}R_\alpha$ change relative to
the $\lVert m\rVert^2$ penalty, and explain which singular directions are now
damped and which are not.

---

**★★★10.** Compute the posterior covariance
$C_m = \sigma_d^2(F^{\mathsf T}F+\alpha I)^{-1}F^{\mathsf T}F
(F^{\mathsf T}F+\alpha I)^{-1}$ at $\alpha = \alpha_{\text{disc}}$ and at
$\alpha = \alpha_c$.

(a) Report the diagonal entries at both, and the ratio of the largest to the
smallest diagonal at each.
(b) Explain the pattern along the model axis in terms of the kernel's
shift-invariance and the survey boundaries.
(c) Write two sentences a reviewer would accept, reporting the model *and* its
spatially varying uncertainty, for the $\alpha_{\text{disc}}$ case.
