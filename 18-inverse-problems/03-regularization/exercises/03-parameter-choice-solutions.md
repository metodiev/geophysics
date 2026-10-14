# Solutions — 18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted as printed.

Lesson: [03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](../03-parameter-choice.md).
All models are **SYNTHETIC**.

---

## ★1 — Which way to move $\alpha$

$0.4\,n\sigma_e^2$ is below the expected residual $\|e\|^2 = n\sigma_e^2$ by a
factor of $2.5$, so the estimate is fitting part of the noise. The residual grows
with $\alpha$, so **$\alpha$ must be increased** until the residual reaches the
noise level. The reason is not aesthetic: a residual below $n\sigma_e^2$ means
the model has absorbed data variability that is noise by assumption, and that
absorption is exactly the variance term of the bias–variance decomposition.

---

## ★2 — GCV value check

$$G(\alpha) = \frac{\|Km_\alpha-d\|^2/n}{(1-\sum_i f_i/n)^2}
= \frac{2.7155\times10^{-5}/64}{(1-31.291/64)^2}
= \frac{4.2430\times10^{-7}}{(0.51108)^2}
= \frac{4.2430\times10^{-7}}{0.261203} = 1.6244\times10^{-6}.$$

The demonstration prints $1.627\times10^{-6}$. The difference (0.16%) is
rounding in the two quoted inputs ($\|r\|^2$ and $\sum f_i$ are printed to
limited precision), not a discrepancy in the formula.

---

## ★3 — What is wrong with the corner solution

The corner solution fits the data **better than the noise level allows**
($0.507\,n\sigma_e^2$), so part of what it reproduces is noise. The test that
revealed it is the residual ratio to $n\sigma_e^2$, which requires only a noise
estimate and no truth — and it is the reason a practitionar should compute that
ratio for whatever $\alpha$ any rule returns.

---

## ★4 — How many significant figures GCV supports

$$\frac{1.66\times10^{-3}}{1.62\times10^{-4}} = 10.25 .$$

The flat region spans one decade of $\alpha$, so GCV determines
$\log_{10}\alpha$ to about $\pm0.5$, i.e. **about one significant figure**. A
report of "$\alpha = 7.848\times10^{-4}$" is over-precise by three digits; the
honest forms are "$2\times10^{-4}$ to $2\times10^{-3}$" or "$\approx10^{-3}$".

---

## ★5 — Asymmetry of a wrong $\sigma_e$

Underestimating by a factor of four ($0.25\times$) gives median errors
$626.67283$ against $0.02730$ at the correct $\sigma_e$:

$$\frac{626.67283}{0.02730} = 2.30\times10^{4},$$

i.e. **more than four orders of magnitude** worse. Overestimating by the same
factor of four gives $0.04751/0.02730 = 1.74$: a factor of $1.7$ worse.

The asymmetry comes from the **shape of the error curve near its minimum**: on
the under-smoothing side the error rises like $\sigma_e/\sigma_{\min}$ (a steep
power law, unbounded as $\alpha\to0$), while on the over-smoothing side the bias
rises gently because the model coefficients $x_i$ decay fast. The measured curve
in the lesson shows exactly this: error $0.2982$ at $\alpha = 10^{-10}$ versus
$0.2974$ at $10^{-4}$ on the left, but $0.8918$ at $10^{-1}$ on the right — so
the *safe* direction to mis-state $\sigma_e$ is upward.

---

## ★6 — Reproducibility in multiplicative terms

$$10^{0.15} = 1.41, \qquad 10^{0.39} = 2.45 .$$

The discrepancy rule reproduces $\alpha$ to within a factor of about $1.4$
between realisations; the L-curve corner to within about $2.5$. For reproducing
a colleague's result, the discrepancy rule is the more reproducible **provided**
both of you use the same $\sigma_e$ — which is the assumption that Section 5
shows to be the dangerous one. Reproducibility here is conditional, and the
condition is worth more than the number.

---

## ★★★7 — GCV with a general penalty operator

For $L$ with $\mathrm{rank}(L) = p \le n$, use the generalised SVD: there are
matrices $U$, $V$ and an invertible $X$ with

$$K = U C X^{-1}, \qquad L = V S X^{-1}, \qquad C^{\mathsf T}C+S^{\mathsf T}S = I,$$

where $C$ and $S$ are diagonal (or block-diagonal in the rank-deficient case).
The generalised singular values are $\gamma_i = c_i/s_i$ for $s_i \ne 0$, and
the filter factors of the penalised solution are

$$f_i = \frac{\gamma_i^2}{\gamma_i^2+\alpha} \quad (s_i \ne 0),
\qquad f_i = 1 \quad (s_i = 0).$$

The second line is the important one: the $n - p$ modes in the null space of $L$
are **not** filtered at all — that is the constant-model direction measured in
lesson [02 §6](../02-tikhonov.md), where the $L=D$ solution's mean came from the
data. The GCV function keeps its form,

$$G(\alpha) = \frac{\|(I-A)d\|^2/n}{\left(1-\mathrm{tr}A/n\right)^2},
\qquad A = K\left(K^{\mathsf T}K+\alpha L^{\mathsf T}L\right)^{-1}K^{\mathsf T},$$

but $\mathrm{tr}\,A = \sum_i f_i$ must be computed from the generalised
decomposition, **not** from the SVD of $K$ alone. Two practical consequences:
(i) the "effective number of parameters" can now reach at most
$n$ but never exceeds it, with $n-p$ of them contributing $f_i = 1$ regardless
of $\alpha$, so $G(\alpha)$ has a smaller dynamic range and its minimum is often
flatter than for $L=I$; (ii) if the null space of $L$ is poorly represented in
the data, the denominator approaches zero and GCV can develop spurious minima
there.

---

## ★★★8 — Measuring the L-curve's bias against $q$

**Statistic.** $B(q) = \text{median}\big(E_{\text{LC}}^{(r)} /
E_{\text{oracle}}^{(r)}\big)$ over realisations $r$, where both errors are
relative model errors against the synthetic truth. Report the 10–90% interval of
the per-realisation ratio as well, because a median ratio alone cannot separate
bias from spread.

**Design.** Use the three kernels of lesson 01's depth control ($q = 1.64$,
$3.24$, $6.34$ at fixed station spacing, grid, model and noise), 300 realisations
each, and compute the L-curve corner with a *fixed* spline smoothing (the hidden
parameter must be held constant or it becomes a second uncontrolled variable).
For a standard error of the median ratio of about $0.05$ with a per-realisation
scatter of $0.5$, roughly $n \ge (1.253\times0.5/0.05)^2 \approx 160$
realisations are needed; 300 gives margin.

**Prediction.** $B(q)$ increases with $q$: for a steeper spectrum the corner sits
further below the optimum (because the bend moves towards the noise floor), so
the bias grows.

**Not systematically biased** would mean: $B(q) \approx 1$ within its confidence
interval for all three $q$, with no monotone trend. A trend of 7.6 at $q = 3.24$
(as measured in the demonstration) falling towards 1 would falsify the
"systematically biased towards under-smoothing" reading, and would point at the
corner's *location* rather than at the rule itself.
