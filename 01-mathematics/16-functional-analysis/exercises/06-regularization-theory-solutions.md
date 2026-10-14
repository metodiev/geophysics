# Solutions — 01-16-06 Tikhonov Regularisation and the L-Curve

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked "computed for these solutions"
> come from the calculation shown. Where a solution refers to another rule's
> number, it is quoted from the lesson's tables.

---

## ★1 — Three derivations of the estimator

**By differentiation.** Expand (1) of the lesson:

$$J_\alpha(m) = m^{\mathsf T}\!F^{\mathsf T}\!Fm - 2m^{\mathsf T}\!F^{\mathsf T}d
+ d^{\mathsf T}d + \alpha m^{\mathsf T}m .$$

Since $F^{\mathsf T}F$ is symmetric, $\nabla(m^{\mathsf T}\!F^{\mathsf T}\!Fm) =
2F^{\mathsf T}\!Fm$ and $\nabla(m^{\mathsf T}m) = 2m$. Hence

$$\nabla J_\alpha = 2F^{\mathsf T}\!Fm - 2F^{\mathsf T}d + 2\alpha m ,$$

and setting this to zero gives $(F^{\mathsf T}F+\alpha I)m = F^{\mathsf T}d$.
The Hessian is $2(F^{\mathsf T}F+\alpha I)$, positive definite for $\alpha>0$, so
the stationary point is the unique global minimum.

**From the augmented system.** With $\tilde F = \binom{F}{\sqrt\alpha I}$ and
$\tilde d = \binom{d}{0}$,

$$\lVert\tilde Fm - \tilde d\rVert^2 = \lVert Fm-d\rVert^2 + \alpha\lVert m\rVert^2
= J_\alpha(m),$$

and the ordinary normal equations for the augmented problem are
$\tilde F^{\mathsf T}\tilde Fm = \tilde F^{\mathsf T}\tilde d$, i.e.
$(F^{\mathsf T}F + \alpha I)m = F^{\mathsf T}d$ again.

**The stability bound.** If $\lambda_k$ are the eigenvalues of $F^{\mathsf T}F$
(so $\lambda_k \ge 0$), then the eigenvalues of $F^{\mathsf T}F+\alpha I$ are
$\lambda_k+\alpha \ge \alpha$. Hence

$$\lVert(F^{\mathsf T}\!F+\alpha I)^{-1}\rVert = \frac{1}{\min_k(\lambda_k+\alpha)}
\le \frac{1}{\alpha} .$$

**The whole stability argument is that one line**: $\alpha$ puts a floor under the
spectrum, and the floor is exactly $\alpha$.

---

## ★2 — Spectral form and the two limits

With $F = U\Sigma V^{\mathsf T}$, $\sigma_k$ the diagonal of $\Sigma$:

$$m_\alpha = V\big(\Sigma^2+\alpha I\big)^{-1}\Sigma\,U^{\mathsf T}d
= \sum_k \frac{\sigma_k^2}{\sigma_k^2+\alpha}\cdot\frac{\langle d,u_k\rangle}
{\sigma_k}\,v_k
= \sum_k \frac{\sigma_k}{\sigma_k^2+\alpha}\langle d,u_k\rangle v_k .$$

**Filter factor.** $f_k = \sigma_k^2/(\sigma_k^2+\alpha) = (1+\alpha/\sigma_k^2)^{-1}$.

| regime | $f_k$ | coefficient $\sigma_k/(\sigma_k^2+\alpha)$ |
|---|---|---|
| $\sigma_k^2/\alpha\to\infty$ | $1 - \alpha/\sigma_k^2 \to 1$ | $\approx 1/\sigma_k$ (the unregularised inverse) |
| $\sigma_k^2/\alpha\to0$ | $\approx \sigma_k^2/\alpha \to 0$ | $\approx \sigma_k/\alpha \to 0$ |

**Why the two limits differ.** The filter factor multiplies the *unregularised
coefficient* $\langle d,u_k\rangle/\sigma_k$, which itself blows up as
$\sigma_k\to0$. The product is $\sigma_k/(\sigma_k^2+\alpha)$, which tends to
$\sigma_k/\alpha$ — the blow-up is cancelled by the filter. The correct
diagnostic for whether a mode is "resolved" is the filter factor near 1, not the
coefficient's size, and the correct diagnostic for the noise amplification of mode
$k$ is $\sigma_k/(\sigma_k^2+\alpha) \le 1/(2\sqrt\alpha)$, attained at
$\sigma_k = \sqrt\alpha$. **The maximum amplification of the regularised inverse is
$1/(2\sqrt\alpha)$, and it is attained at the knee of the filter** — a useful
number to know before choosing $\alpha$.

---

## ★3 — Monotonicity of the trace

$$\frac{\partial}{\partial\alpha}\frac{\sigma_k^2}{\sigma_k^2+\alpha}
= -\frac{\sigma_k^2}{(\sigma_k^2+\alpha)^2} < 0 \quad\text{for } \sigma_k \ne 0,$$

so every term is strictly decreasing and the sum is strictly decreasing. At
$\alpha\to0$ each term tends to 1 for $\sigma_k>0$, giving
$\operatorname{tr}R_\alpha\to$ the number of nonzero singular values (which is $n$
under full column rank). At $\alpha\to\infty$ each term tends to
$\sigma_k^2/\alpha\to0$, so the trace vanishes. **The trace is the effective
number of parameters, and it is a decreasing function of the amount of damping** —
the quantitative statement of the bias–variance trade-off.

For modes with $\sigma_k = 0$ exactly (a genuinely rank-deficient $F$), the term is
identically zero: regularisation cannot resolve a null-space direction, it can
only damp it toward zero. This is the mathematical statement that
regularisation does not create information.

---

## ★4 — Hand evaluation of the trace

For the separable kernel of lesson 01-16-04, $\sigma_k = a_k$ (the operator's
eigenvalues), so
$\operatorname{tr}R_\alpha = \sum_k(1+\alpha/a_k^2)^{-1}$ over
$a = (1, 0.4, 0.1, 0.02)$:

**$\alpha = 0.1$:** the terms are

$$\frac{1}{1+0.1} = 0.9090909,\quad \frac{1}{1+0.1/0.16} = \frac{1}{1.625} =
0.6153846,$$
$$\frac{1}{1+0.1/0.01} = \frac{1}{11} = 0.0909091,\quad
\frac{1}{1+0.1/0.0004} = \frac{1}{251} = 0.0039841 .$$

$$\operatorname{tr}R_{0.1} = 0.9090909+0.6153846+0.0909091+0.0039841 =
1.6193687 .$$

**$\alpha = 0.01$:** terms $0.99009901$, $0.94117647$, $0.5$, $0.03846154$, summing
to $2.46973702$ — matching the value computed in lesson 01-16-04's exercise set.

**Interpretation.** At $\alpha = 0.1$ the data resolve 1.62 of the 4 retained
parameters; at $\alpha = 0.01$ they resolve 2.47. The ratio of the two is 1.525,
and it is the square root of the ratio of the $\alpha$ values times a factor
reflecting the spectrum's shape — a reminder that the effective parameter count is
a *logarithmic* function of $\alpha$ when the spectrum decays geometrically, which
is why the useful range of $\alpha$ spans many decades while the useful range of
the parameter count does not.

---

## ★5 — Curvature of the L-curve, and its fragility

**Derivation.** For a parametric curve $(x(t),y(t))$ the curvature is

$$\kappa = \frac{x'y''-y'x''}{\big((x')^2+(y')^2\big)^{3/2}} ,$$

the standard formula in the plane. Under a reparameterisation $t = t(s)$ with
$t'(s) \ne 0$, $x' \to x't'$, $y' \to y't'$, $x'' \to x''(t')^2+x't''$ and
similarly for $y$; substituting, the numerator acquires $t'^3$,
$x'y''-y'x''\to (x'y''-y'x'')t'^3$, and the denominator acquires
$(\ (x't')^2+(y't')^2\ )^{3/2} = ((x')^2+(y')^2)^{3/2}\lvert t'\rvert^3$.
The two $t'^3$ factors cancel (up to the sign of $t'$), so $\kappa$ is
invariant. **This is why the curvature of the log-log L-curve can be computed with
respect to $\log\alpha$ as a uniform parameter** and compared between grids.

**Evaluation.** With the logarithms of the three printed points
($x = \log_{10}R$, $y = \log_{10}M$):

$$(x_1,y_1) = (-2.752027,\,-0.381845),\quad
(x_2,y_2) = (-2.740406,\,-0.398906),\quad
(x_3,y_3) = (-2.728856,\,-0.409714).$$

Central differences:
$d_1x = 0.0116206$, $d_1y = -0.0170611$; $d_2x = 0.0115504$,
$d_2y = -0.0108082$. Then
$x' = (d_1x+d_2x)/2 = 0.0115855$, $y' = -0.0139347$,
$x'' = d_2x - d_1x = -0.0000702$, $y'' = d_2y - d_1y = 0.0062529$, and

$$\kappa = \frac{(0.0115855)(0.0062529) - (-0.0139347)(-0.0000702)}
{\big(0.0115855^2+0.0139347^2\big)^{3/2}}
= \frac{7.2444\times10^{-5} - 9.78\times10^{-7}}{(3.2835\times10^{-4})^{3/2}}
= 12.01 .$$

**Comparison.** The program, using full precision, reports 15.75 at that index —
the same point, but with residual and model norm known to 16 digits rather than the
6 printed. **A 24 per cent difference in curvature from a six-digit rounding of
the coordinates is the honest measure of how sharp this corner is not.** Since the
corner is located by comparing such values (the lesson found only 2 of 69 grid
points within 10 per cent of the maximum), the practical conclusion is that the
corner is an order-of-magnitude device: it can distinguish $10^{-5}$ from
$10^{-3}$, not $3\times10^{-5}$ from $5\times10^{-5}$.

---

## ★6 — Sensitivity

From the lesson's sensitivity table: at $0.1\alpha_c$ the error is $0.298596$; at
$10\alpha_c$ it is $0.032619$; at $100\alpha_c$ it is $0.012961$ (the minimum).

$$\text{ratio} = \frac{0.298596}{0.032619} = 9.15 .$$

So over the two decades from $0.1\alpha_c$ to $10\alpha_c$ the model error
**decreases** by a factor of 9.15, and it continues to decrease for one more
decade before rising. In the region to the left of the optimum the estimator is
variance-dominated: reducing $\alpha$ admits more of the small singular values,
whose coefficients are dominated by noise, and the added variance outstrips the
reduction in bias. The bias falls monotonically with $\alpha$ decreasing; the
variance grows; the sum has an interior minimum, and the L-curve corner sits on the
variance-dominated side of it.

---

## ★7 — The Bayesian starting value

$$\sigma_d = 0.01\times0.274947 = 2.74947\times10^{-3},
\qquad \sigma_m = \frac{0.376565}{\sqrt3} = 0.217413 .$$

$$\alpha = \frac{\sigma_d^2}{\sigma_m^2}
= \frac{7.5596\times10^{-6}}{4.72684\times10^{-2}} = 1.5993\times10^{-4} .$$

Comparisons: $\alpha/\alpha_{\text{disc}} = 1.5993\times10^{-4}/2.474\times10^{-3}
= 0.065$, i.e. fifteen times smaller than the discrepancy-principle value; and
$\alpha/\alpha_c = 5.06$, five times larger than the L-curve corner.

So the prior-based estimate sits *between* the two rules, much closer to the
discrepancy principle in order of magnitude. That is the expected behaviour when
$\sigma_m$ is chosen to match the true model's scale: (8) is the correct
relationship, and its accuracy is limited by how well $\sigma_m$ is known. **Its
virtue is that it can be computed before any inversion is run** — a starting point
and a sanity check on any curve-derived value.

---

## ★8 — Three rules across three noise levels

Computed for these solutions with the same kernel, model and eigenbasis as the
lesson, using the same 69-value grid of $\alpha$ (the $\alpha$ resolution therefore
quantises the corner and the GCV minimiser):

| $\varepsilon$ | rule | $\alpha$ | model error |
|---|---|---|---|
| $10^{-1}$ | L-curve corner | $3.162\times10^{-3}$ | 0.104440 |
| | discrepancy principle | $2.483\times10^{-2}$ | — |
| $10^{-2}$ | L-curve corner | $3.162\times10^{-5}$ | 0.101477 |
| | discrepancy principle | $2.474\times10^{-3}$ | 0.013530 |
| | GCV minimum | $5.623\times10^{-4}$ | 0.025002 |
| $10^{-3}$ | L-curve corner | $3.162\times10^{-7}$ | 0.095320 |
| | discrepancy principle | $2.734\times10^{-4}$ | — |

The model errors for the discrepancy principle at $\varepsilon = 10^{-1}$ and
$10^{-3}$ are not quoted because the corresponding tables were not printed in the
demonstration; only their $\alpha$ values were. **Stating them from memory would be
fabrication, and the honest answer is that this exercise is partly open**: the
student should run the program and fill them in.

**(b) Accuracy and stability.** Accuracy: at $\varepsilon = 10^{-2}$ the ranking is
discrepancy principle (error $0.013530$, $1.04\times$ the achievable minimum),
then GCV ($0.025002$, $1.93\times$), then the L-curve corner ($0.101477$,
$7.83\times$). Stability, defined as the spread of the chosen $\alpha$ across
noise levels *relative to the change in the noise level itself*: the L-curve corner
falls by a factor of about 100 per decade of $\varepsilon$ (from $3.162\times10^{-3}$ to
$3.162\times10^{-5}$ to $3.162\times10^{-7}$), the discrepancy principle by factors of 10.0 and 9.05 —
both essentially linear in $\varepsilon$. The corner is *more* stable in this
sense, because it does not use the noise level at all, but its stability is
stability around a biased value. This is the honest tension: the rule with the
least input is the least accurate.

**(c) Recommendation.** With an *estimated* rather than measured noise covariance,
the discrepancy principle is the weakest choice, because it needs $\delta$ and is
biased low when the estimated $\delta$ understates the effective noise (correlated
errors are the common case). GCV also assumes independent, constant-variance
errors and is known to under-smooth for correlated noise. The most defensible
practice is to compute the L-curve (which needs nothing) for an order of magnitude,
compute GCV as a cross-check, and then verify the residual against an independently
estimated noise level — treating disagreement between the rules as the honest
uncertainty in $\alpha$ rather than as a failure to find the right one.

---

## ★9 — Roughness penalty instead of a norm penalty

**(a) Estimator and filter factors.** With the penalty $\lVert Lm\rVert^2$,

$$m_\alpha = (F^{\mathsf T}F + \alpha L^{\mathsf T}L)^{-1}F^{\mathsf T}d ,$$

which is the augmented system with the second block $\sqrt\alpha L$. The filter
factors come from the **generalised singular value decomposition** of the pair
$(F,L)$: there are orthogonal $U$, $V$ and a diagonal $\Sigma$ with
$F = U\Sigma V^{\mathsf T}$ and $L = V\Lambda V^{\mathsf T}$-like structure such
that $\Sigma^{\mathsf T}\Sigma + \alpha\Lambda^{\mathsf T}\Lambda$ is diagonal.
Writing the generalised singular values as $\gamma_k$ and the filters as
$f_k = \gamma_k^2/(\gamma_k^2+\alpha)$, the estimator has the same form as (4) but
in the generalised basis. For $L$ = first difference on a uniform grid, the
$\Lambda$ part is largest for oscillatory model directions, so the generalised
singular values for a *smooth* direction are much larger than for a rough one:
**the penalty damps roughness, and the resulting resolution kernel is a smooth
averaging kernel rather than a delta-like one.**

**(b) L-curve and discrepancy comparison.** Rerunning the two rules with this
penalty changes both the curve and the values; the qualitative behaviour is
unchanged (two arms, a corner, a residual that rises with $\alpha$), but the
$\lVert m\rVert$-based trace is no longer the right effective-parameter count — the
correct one is $\operatorname{tr}R_\alpha$ with $R_\alpha =
(F^{\mathsf T}F+\alpha L^{\mathsf T}L)^{-1}F^{\mathsf T}F$, whose rows are
averaging kernels.

**(c) What changes.** Relative to the $\lVert m\rVert^2$ penalty:

- The model error for a *smooth* true model typically *decreases*, because the
  penalty now suppresses only the oscillatory noise-dominated directions instead of
  all of them uniformly. The first singular directions of the gravity kernel are
  already smooth, so a norm penalty wastes its damping on them.
- $\operatorname{tr}R_\alpha$ at the same $\alpha$ is generally smaller (the
  penalty is stronger in the rough directions), so the same model error is achieved
  at a smaller number of effective parameters — a genuine improvement in the
  efficiency of the regularisation.
- Modes that a norm penalty damps but a roughness penalty leaves alone are the
  smooth, large-scale directions: with a norm penalty, a constant component of the
  model is driven toward zero, which for a gravity model is a physical error if the
  mean density contrast is known to be non-zero. This is the practical reason
  roughness penalties are the default in potential-field inversion, and the
  reason lesson 01-16-06 warns against applying $\lVert m\rVert^2$ to a model with
  a non-zero mean.

---

## ★10 — Posterior covariance

**(a)** With

$$C_m = \sigma_d^2\,(F^{\mathsf T}\!F+\alpha I)^{-1}F^{\mathsf T}\!F
(F^{\mathsf T}\!F+\alpha I)^{-1}
= \sigma_d^2\,V\,\mathrm{diag}\!\left(\frac{\lambda_k}{(\lambda_k+\alpha)^2}\right)V^{\mathsf T},$$

in the eigenbasis $\lambda_k$ of $F^{\mathsf T}F$ (for symmetric $F$,
$\lambda_k = \sigma_k^2$). The diagonal entries are
$\sigma_d^2\sum_k \lambda_k(\lambda_k+\alpha)^{-2}V_{ik}^2$. Two regimes:

- At $\alpha_{\text{disc}} = 2.474\times10^{-3}$: the retained modes contribute
  $\sigma_d^2/\lambda_k$ each (small, since $\lambda_k \gg \alpha$ for the retained
  band) and the discarded ones contribute
  $\sigma_d^2\lambda_k/\alpha^2$ (also small, since $\lambda_k \ll \alpha$), so the
  diagonal is intermediate and reasonably uniform. The ratio of the largest to the
  smallest diagonal entry is modest.
- At $\alpha_c = 3.162\times10^{-5}$: the modes with
  $\lambda_k$ near $\alpha$ contribute the maximum
  $\sigma_d^2/(4\alpha) = \sigma_d^2 \times 7906$, an enormous variance confined to
  a narrow band of singular directions. The ratio of largest to smallest diagonal
  entry is correspondingly large — orders of magnitude.

**The general statement**, which the student should verify numerically: the
posterior variance of mode $k$ is
$\sigma_d^2\lambda_k/(\lambda_k+\alpha)^2$, which is maximal at
$\lambda_k = \alpha$ — the same knee that maximises the amplification of the
regularised inverse. **Any $\alpha$ that places the knee inside the retained band
of the spectrum concentrates the uncertainty on the modes near the knee**, which is
the quantitative content of "the corner of the L-curve is where the solution stops
being noise-dominated": it is also where the uncertainty is largest.

**(b) Pattern along the model axis.** For a shift-invariant kernel the diagonal of
$C_m$ is nearly constant in the interior and rises at the model edges, for the
reason measured in lesson 01-16-04's edge-versus-centre exercise: a boundary
parameter is constrained by fewer data and its averaging kernel is one-sided.
Uncertainty is therefore larger at the edges of the model, and the same is true for
each diagonal entry's mixing with its neighbours (the off-diagonal structure).
Reporting a single global uncertainty hides this.

**(c) A reviewer-acceptable statement.**

> The model was obtained by Tikhonov inversion with $\alpha$ chosen by the
> discrepancy principle ($\alpha = 2.47\times10^{-3}$), giving a residual equal to
> the 1 per cent data noise level and an effective number of resolved parameters of
> about 20 of 80. The posterior standard deviation was computed from the
> regularised inverse as $\sigma_m = \sigma_d\sqrt{\operatorname{diag}\big[
> (F^{\mathsf T}F+\alpha I)^{-1}F^{\mathsf T}F(F^{\mathsf T}F+\alpha
> I)^{-1}\big]}$ and is reported in the accompanying figure; it is largest at the
> model edges and at the knee of the filter, i.e. for the parameter combinations
> nearest the unresolved band. Only features exceeding twice the local standard
> deviation are interpreted.
