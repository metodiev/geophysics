# Solutions — 01-14-04 Linear and Nonlinear Least Squares

> **Read this after attempting the exercises, not before.** All arithmetic below
> was computed; values attributed to a demonstration are its actual output, and
> each exercise says which route was used.

---

## ★1 — The normal equations

**(a)** Expanding,

$$\phi(m) = \tfrac12 m^{\mathsf T}G^{\mathsf T}Gm - m^{\mathsf T}G^{\mathsf T}d
+ \tfrac12 d^{\mathsf T}d ,$$

and using $\nabla_m\tfrac12 m^{\mathsf T}Am = \tfrac12(A+A^{\mathsf T})m$ with
$A = G^{\mathsf T}G$ symmetric,

$$\nabla\phi(m) = G^{\mathsf T}Gm - G^{\mathsf T}d = -G^{\mathsf T}r, \qquad
r = Gm - d .$$

**(b)** Setting $\nabla\phi = 0$:

$$G^{\mathsf T}Gm = G^{\mathsf T}d .$$

Since $\nabla^{2}\phi = G^{\mathsf T}G$ is independent of $m$, the misfit is a
convex quadratic and the stationary point is the global minimum whenever
$G^{\mathsf T}G$ is positive definite. $\square$

**(c)** $G^{\mathsf T}r = G^{\mathsf T}(Gm - d) = G^{\mathsf T}Gm - G^{\mathsf T}d = 0$
at the solution. This says $r$ is **orthogonal to every column of $G$**: the
residual is perpendicular to the subspace in which the model can move, which is
the orthogonal-projection statement of the same condition.

**(d)** If $G$ has a nontrivial null space, $G^{\mathsf T}G$ is singular and the
solution set is an affine subspace: any $m$ plus a null-space vector fits equally
well, so the non-uniqueness is real and not numerical. The minimum-norm element of
that set is the pseudoinverse solution
$m = V\Sigma^{+}U^{\mathsf T}d$, and a regularised (Tikhonov) solution adds
$\alpha\|m\|^{2}$ to select one representative.

---

## ★2 — Why $G^{\mathsf T}G$ squares the condition number

**(a)** With $G = U\Sigma V^{\mathsf T}$ (thin SVD, $n\ge p$),

$$G^{\mathsf T}G = V\Sigma^{\mathsf T}U^{\mathsf T}U\Sigma V^{\mathsf T}
= V\Sigma^{2}V^{\mathsf T},$$

because $U^{\mathsf T}U = I$ and $\Sigma^{\mathsf T}\Sigma =
\operatorname{diag}(\sigma_1^{2},\dots,\sigma_p^{2})$.

**(b)** The eigenvalues of $G^{\mathsf T}G$ are $\sigma_i^{2}$, so

$$\kappa_2(G^{\mathsf T}G) = \frac{\sigma_1^{2}}{\sigma_p^{2}}
= \left(\frac{\sigma_1}{\sigma_p}\right)^{2} = \kappa_2(G)^{2}.$$

It is an identity — every term is exact — not a worst-case bound. The practical
consequence is that the normal-equation route loses twice as many digits as QR.

**(c)** The wall is $\kappa^{2} \ge 1/u$ with $u = 2.2\times10^{-16}$, i.e.

$$\kappa_2(G) \ge \frac{1}{\sqrt{u}} = \frac{1}{1.483\times10^{-8}}
= \boxed{6.74\times10^{7}} .$$

Above that, the *computed* $G^{\mathsf T}G$ loses all its digits in the smallest
singular direction: for $\kappa$ larger than about $10^{8}$ the matrix is
numerically singular of order the round-off, and the solution can be dominated by
error (measured in ★★★9 below).

**(d)** The second consequence is the model covariance. Since the eigenvalues of
$G^{\mathsf T}G$ are $\sigma_i^{2}$,

$$C_m = \hat\sigma^{2}\left(G^{\mathsf T}G\right)^{-1}
= \hat\sigma^{2}\,V\Sigma^{-2}V^{\mathsf T}
= \hat\sigma^{2}\sum_i\frac{\mathbf v_i\mathbf v_i^{\mathsf T}}{\sigma_i^{2}},$$

so the model variance in the $i$-th singular direction is inflated by
$1/\sigma_i^{2}$. The route that forms $G^{\mathsf T}G$ therefore *also* reports
inflated model variances in the weak directions — or, when the computation
misbehaves, underestimates them because the small $\sigma_i$ are lost rather than
inverted.

---

## ★3 — The exponential model

**(a)** With $f_i = a\,\mathrm{e}^{-x_i/h}$ the residual is
$r_i = a\mathrm{e}^{-x_i/h} - d_i$ and

$$J_i = \left(\frac{\partial r_i}{\partial a},\
\frac{\partial r_i}{\partial h}\right)
= \left(\mathrm{e}^{-x_i/h},\
\frac{ax_i}{h^{2}}\mathrm{e}^{-x_i/h}\right).$$

**(b)** The Gauss–Newton step is
$\delta = -\left(J^{\mathsf T}J\right)^{-1}J^{\mathsf T}r$, applied as
$(a,h) \leftarrow (a,h) + \delta$ after forming $J$ and $r$ at the current
parameters.

**(c)** At $x_i \gg h$, expanding $\mathrm{e}^{-x_i/h}$ as a function of $h$
gives

$$a\,\mathrm{e}^{-x_i/h} \approx a\mathrm{e}^{-x_i/h_0}
\left[1 + \frac{x_i(h-h_0)}{h_0^{2}}\right],$$

so the two columns of $J$ differ by the factor $x_i/h$ and the model is
effectively a single-amplitude function with a scale parameter. The determined
combination is the *logarithmic slope* of the data against $x$, i.e. the exponent
$1/h$ (with $a$ degenerate against it); what is lost is the separate amplitude.
Equivalently, with $z_i = x_i/h$ the data determine $a$ and $1/h$ only through
the product $a/h$ in the linearised model.

**(d)** With $a = 1$, $h = 1$:

| design | $\kappa_2(J)$ | $\sigma_{\min}^{2}$ of $J^{\mathsf T}J$ | reading |
|---|---|---|---|
| $x = 0,\dots,5$ | 2.42 | $0.203$ | well conditioned; both parameters determined |
| $x = 5,\dots,30$ | $7.72\times10^{2}$ | $1.98\times10^{-9}$ | usable but the amplitude and scale are correlated |
| $x = 50,\dots,100$ | $5.51\times10^{6}$ | $3.07\times10^{-54}$ | effectively one parameter; the amplitude is unrecoverable, and $G^{\mathsf T}G$ at $\kappa^{2} = 3\times10^{13}$ is at the edge of binary64 |

The practical consequence: a laboratory decay experiment must sample the range
where the exponential actually bends. Data taken entirely in the tail determine a
line through nearly zero values, which fixes the ratio $a/h$ and nothing else;
reporting separate error bars on $a$ and $h$ from such a design is a statement
about the prior, not about the data.

---

## ★4 — Weighting

**(a)** With $G$ the $4\times2$ matrix of ones and $x_i$, and
$d = (1.0, 2.0, 2.2, 3.4)$:

$$\hat m = (a, b) = (1.040000,\ 0.740000), \qquad
r = (0.040000,\ -0.220000,\ 0.320000,\ -0.140000),$$

$\|r\| = 0.414729$ and

$$\hat\sigma^{2} = \frac{\|r\|^{2}}{n-p} = \frac{0.172000}{2} = 0.0860000 .$$

**(b)** With $w = 1/\sigma^{2} = (100,100,1,1)$:

$$\hat m_W = (a, b) = (1.016846,\ 0.954258),$$

weighted residuals $r_W = (0.016846, -0.028896, 0.725362, 0.479620)$ — small in
units of $\sigma$ for the tight data and large for the loose data, as it must be.
The weighted scale is $\hat\sigma_W^{2} = 0.378652$ in weighted units, i.e.
$\chi^{2}$ per degree of freedom near 0.38.

The slope moved from $0.740000$ to $0.954258$: **+28.9 per cent**, produced
entirely by the stated uncertainties. The weights did not change the data; they
changed what "best" means.

**(c)** Standard errors from $C_m = \hat\sigma^{2}(G^{\mathsf T}G)^{-1}$:

| estimate | se$(a)$ | se$(b)$ |
|---|---|---|
| ordinary | 0.245357 | 0.131149 |
| weighted | 0.060214 | 0.080508 |

The ordinary fit's standard errors treat all four data as equally informative and
are therefore both wrong and misleadingly large for the first two points.

**(d)** Weights legitimately change the *estimate*, its covariance, and the
implied misfit that measures goodness of fit. They must not change the data, the
forward model, or the claim that the estimate is a maximum-likelihood estimate
for the stated uncertainties — if the stated $\sigma$ are wrong, the estimate is
still minimum-misfit but is no longer maximum likelihood, and its error bars are
uncalibrated. The lesson's §4.8 measures the cost of getting this wrong: a change
of $-42$ per cent in a slope from mis-stated uncertainties.

---

## ★★5 — Gauss–Newton on an exponential decay

**(a)** With $m = (A,\lambda)$ and residuals
$r_i = A\mathrm{e}^{-\lambda x_i} - d_i$,

$$J_i = \left(\mathrm{e}^{-\lambda x_i},\
-Ax_i\mathrm{e}^{-\lambda x_i}\right), \qquad
\delta = -\left(J^{\mathsf T}J\right)^{-1}J^{\mathsf T}r .$$

**(b)** Starting from $(1,1)$ with exact data from $A = 2$, $\lambda = 0.5$:

| iteration | $A$ | $\lambda$ | $\|r\|$ |
|---|---|---|---|
| 0 | 1.000000000 | 1.000000000 | $1.5233\times10^{0}$ |
| 1 | 1.975332647 | $-0.600378153$ | $4.6939\times10^{1}$ |
| 2 | 0.401285162 | $-0.558955999$ | $7.6842\times10^{0}$ |
| 3 | 0.469551595 | $-0.319563932$ | $3.1538\times10^{0}$ |
| 4 | 0.989062284 | $0.121100380$ | $1.2047\times10^{0}$ |
| 5 | 1.844327312 | $0.488112115$ | $1.8155\times10^{-1}$ |
| 6 | 1.999929753 | $0.500782181$ | $2.1554\times10^{-3}$ |
| 7 | 1.999999706 | $0.499999091$ | $2.2776\times10^{-6}$ |
| 8 | 2.000000000 | $0.500000000$ | $2.6189\times10^{-12}$ |

**(c)** The start has $\|r\| = 1.5233$; the largest residual norm encountered is
$4.6939\times10^{1}$ at step 1 — a factor of 31 *worse*; the run reaches
$\|r\| < 10^{-10}$ at **step 8**, with the last two steps showing the quadratic
tail characteristic of a small-residual problem.

**(d)** The first step increases the residual because the linearisation is only
locally valid: at the start the model is far from the data, $J^{\mathsf T}J$ is
rank-deficient in the direction of the nearly parallel columns (§★3), and the
implied step is enormous — it overshoots $\lambda$ to $-0.600$, outside the
physically admissible range and outside the region where the linear model
describes $r$. A trust region or Levenberg–Marquardt damping bounds the step
length: $(\delta^{\mathsf T}\delta \le \Delta^{2})$ or
$\delta = -(J^{\mathsf T}J + \lambda I)^{-1}J^{\mathsf T}r$, and the damping is
reduced as the residual falls. The lesson's §4.5 shows the same failure mode
catastrophically, with a start at $h = 90$ escaping to $h = 1645$ and a residual
63 times larger.

---

## ★★6 — Gauss–Newton is exact for a linear model

**(a)** For $F(m) = Gm$, $r_k = Gm_k - d$ and $J_k = \partial F/\partial m = G$
for every $k$.

**(b)** The step is

$$\delta_k = -(G^{\mathsf T}G)^{-1}G^{\mathsf T}(Gm_k - d)
= -m_k + (G^{\mathsf T}G)^{-1}G^{\mathsf T}d,$$

so $m_{k+1} = m_k + \delta_k = (G^{\mathsf T}G)^{-1}G^{\mathsf T}d$ — the
least-squares solution, reached in **one** step from any start. $\square$

**(c)** The misfit is a quadratic function whose Hessian is exactly
$G^{\mathsf T}G$, and $J^{\mathsf T}J = G^{\mathsf T}G$ is therefore the *true*
Hessian, not an approximation to it. That is the $\S3.1$ "by curvature"
derivation of the normal equations: Newton's method solves quadratics exactly, so
Gauss–Newton converges in one step whenever its curvature model is the true
Hessian. The lesson's §4.4 shows the same thing empirically for a mildly nonlinear
problem, where two iterations reached the plateau.

**(d)** For a nonlinear $F$, the true Hessian is
$J^{\mathsf T}J + \sum_ir_i\nabla^{2}F_i$, and the discarded term is
$\sum_ir_i\nabla^{2}F_i$ — the *residual-weighted* second derivatives. With large
residuals this term is not small, the step is not a Newton step, and convergence
degrades from quadratic to linear; the second reason is that even a correct step
may leave the region where the linearisation holds, which is why damping or a
trust region is needed as well.

---

## ★★7 — Where a fixed damping weight takes the iteration

**(a)** $r(m) = m^{2} - 2$, $J(m) = 2m$, so

$$\delta_{\text{GN}} = -\frac{Jr}{J^{2}} = -\frac{2m(m^{2}-2)}{4m^{2}}
= -\frac{m^{2}-2}{2m}, \qquad
m_{k+1} = m_k - \frac{m_k^{2}-2}{2m_k} = \frac{m_k^{2}+2}{2m_k}.$$

**(b)** $m_{k+1} = \frac12\left(m_k + \frac{2}{m_k}\right)$ is exactly Newton's
method for $m^{2} = 2$, i.e. Heron's iteration. It has a double root at
$m^{*} = \sqrt2$, so the error satisfies
$e_{k+1} \approx \frac{e_k^{2}}{2\sqrt2}$: **quadratic** convergence. Measured
from $m_0 = 1$: $1.50000000$, $1.41666667$, $1.41421569$, $1.41421356$ — three
steps to full precision.

**(c)** With $D = I$,

$$\delta_{\text{LM}} = -\frac{Jr}{J^{2}+\lambda}
= -\frac{2m(m^{2}-2)}{4m^{2}+\lambda}, \qquad
m_{k+1} = m_k - \frac{2m_k(m_k^{2}-2)}{4m_k^{2}+\lambda}.$$

**(d)** Errors $|m_{10} - \sqrt2|$ after exactly ten iterations from $m_0 = 1$:

| $\lambda$ | $m_{10}$ | error |
|---|---|---|
| 0 | 1.4142135624 | $2.2\times10^{-16}$ |
| 1 | 1.4142135623 | $3.6\times10^{-11}$ |
| 10 | 1.4124664099 | $1.7\times10^{-3}$ |
| 100 | 1.1702683298 | $2.4\times10^{-1}$ |

All four runs converge to $\sqrt2$ — the fixed point of the damped iteration
still satisfies $Jr = 0$ because $J^{2}+\lambda > 0$ — so damping does not *bias*
a convex problem. What it does is change the path: the $\lambda = 100$ run needs
295 iterations to reach the same $10^{-10}$ accuracy that undamped Gauss–Newton
needs 4, and after a fixed ten-iteration budget it is 13 orders of magnitude
worse. The honest statement is therefore narrower than "damping changes the
answer": damping changes the *rate* and, when the step is a descent step of a
different size, it changes which basin is reached on a non-convex problem. A
schedule that reduces $\lambda$ is what recovers the Gauss–Newton rate at the
end; a fixed $\lambda$ is a decision to be slow.

---

## ★★8 — Leverage and a single blunder

**(a)** $\bar x = 2$, $S_{xx} = \sum(x_i - \bar x)^{2} = 10$, so

$$h_i = \frac15 + \frac{(x_i-2)^{2}}{10}
= (0.6,\ 0.3,\ 0.2,\ 0.3,\ 0.6), \qquad \sum_ih_i = 2.0 = p .$$

The two endpoints carry $0.6$ of the fit each — three times the middle sample's
$0.2$. In a straight-line fit the extremes control the slope, which is the general
warning about extrapolation and about trimming endpoints from a profile.

**(b)** Ordinary least squares:

| data | $a$ | $b$ |
|---|---|---|
| blundered, $y = (1,2,2,4,9)$ | 0.000000 | 1.800000 |
| clean, $y = (1,2,2,4,4.6)$ | 0.880000 | 0.920000 |

**(c)** For a single perturbation $e$ at sample $j$, the normal equations give

$$\Delta a = e\left(\frac1n - \frac{\bar x(x_j-\bar x)}{S_{xx}}\right), \qquad
\Delta b = \frac{e\,(x_j - \bar x)}{S_{xx}}, \qquad
\Delta\hat y_j = e\,h_j .$$

With $e = 9 - 4.6 = 4.4$ and $j = 5$ ($x_j = 4$):

$$\Delta b = \frac{4.4\times2}{10} = +0.880000, \qquad
\Delta a = 4.4\left(0.2 - \frac{2\times2}{10}\right) = -0.880000, \qquad
\Delta\hat y = 4.4\times0.6 = 2.640000 .$$

The measured differences between the two fits of (b) are exactly
$b: 1.8 - 0.92 = +0.88$ and $a: 0 - 0.88 = -0.88$. The formulas are verified.

**(d)** Two different sensitivity factors are in play, and conflating them is a
common error. The influence on the *slope* is

$$\frac{\Delta b}{e} = \frac{x_j - \bar x}{S_{xx}} = \frac{2}{10} = 0.2 ,
\qquad\text{so}\qquad \Delta b = 0.880000,$$

whereas the influence on the *fitted value at the outlier* is the leverage
$h_j = 0.6$, giving $\Delta\hat y_j = 2.640000$. Both are exact here: the slope
moved by $0.88$, which is **96 per cent** of the clean-data slope $0.92$ — one
blunder at an endpoint has doubled the trend.

The comparison that makes it a warning is between samples: the same perturbation
$e = 4.4$ at the middle sample ($x = 2$) would move the slope by
$4.4\times(2-2)/10 = 0$ — nothing at all — because the slope is a *contrast*
between the ends. The slope sensitivity grows linearly from the centre (as
$x_j - \bar x$) while the leverage grows quadratically, so a remote station is
both heavily leveraged and steeply influential. That asymmetry is the mechanism
L1 fitting exploits (Section 4.8 of the lesson): the L1 sensitivity to a datum is
$\pm1$ regardless of its residual, so no single sample can pull the fit with
$2r_k$ force as it does under L2.

---

## ★★★9 — Normal equations against QR on nearly parallel rays

**(a)** The three routes implemented:

* **Normal equations**: form $A = G^{\mathsf T}G$, $b = G^{\mathsf T}d$ in
  floating point, solve the $2\times2$ system by Cramer's rule.
* **Householder QR**: build $Q$ implicitly from the two Householder reflections
  that reduce $G$ to upper triangular $R$, apply them to $d$, back-substitute.
* **Exact reference**: solve the same normal equations in rational arithmetic
  (`Fraction`) from the *same* floating-point entries of $G$ and $d$, so the
  comparison isolates the solve and not the data.

**(b)** Data generated from $m = (0.05, -0.02)$; relative error is the maximum
over the two parameters against the rational reference:

| $\delta$ | $\kappa_2(G)$ | $\det(G^{\mathsf T}G)$ in float | normal-equation error | QR error | ratio |
|---|---|---|---|---|---|
| $10^{-2}$ | $4.020\times10^{2}$ | $1.000\times10^{-4}$ | $2.14\times10^{-11}$ | $2.06\times10^{-14}$ | $1.0\times10^{3}$ |
| $10^{-4}$ | $4.000\times10^{4}$ | $1.000\times10^{-8}$ | $1.39\times10^{-7}$ | $5.66\times10^{-12}$ | $2.5\times10^{4}$ |
| $10^{-6}$ | $4.000\times10^{6}$ | $9.992\times10^{-13}$ | $2.08\times10^{-3}$ | $1.65\times10^{-10}$ | $1.3\times10^{7}$ |
| $10^{-8}$ | $4.000\times10^{8}$ | $0.000\times10^{0}$ | fails (zero determinant) | $7.97\times10^{-9}$ | — |

The normal-equation error grows roughly as $\kappa^{2}u$: from $10^{-11}$ to
$10^{-3}$ for a factor $10^{4}$ in $\kappa$. The QR error grows roughly as
$\kappa u$: from $10^{-14}$ to $10^{-9}$, i.e. by $10^{5}$ for $10^{4}$ in
$\kappa$ — a slower growth and five to seven orders of magnitude smaller at every
$\delta$ except the smallest.

**(c)** At $\delta = 10^{-8}$ the computed $G^{\mathsf T}G$ has determinant
*exactly* $0.000\times10^{0}$: the matrix has become numerically singular in
binary64, $\kappa^{2} = 1.6\times10^{17}$ exceeds $1/u = 4.5\times10^{15}$, and
the normal-equation route has no solution to return. QR still recovers both
parameters to about nine significant digits ($7.97\times10^{-9}$ relative), which
is the entire practical argument for the factorisation: the loss of rank happened
in the *formation* of $G^{\mathsf T}G$, not in the data.

**(d)** $\kappa$ at $\delta = 10^{-8}$ is $4\times10^{8}$; forming
$G^{\mathsf T}G$ in binary64 destroys the information needed to compute it,
because $\sigma_{\min}^{2} \approx 6\times10^{-18}$ is below $u$ times
$\sigma_{\max}^{2}$. The demonstration therefore evaluates $\kappa$ in 60-digit
`Decimal` arithmetic; "measuring $\kappa$ badly" means computing it from the
rounded matrix and reporting the number, which would return either zero, infinity,
or a value that describes the round-off rather than the problem. The same
distinction shows up in the determinant column: the true determinant of the exact
matrix is $10^{-16}$ at $\delta = 10^{-8}$, and the computed value is $0$.

---

## ★★★10 — A small residual with an oscillating model

**(a)** The model is
$\hat m = (G^{\mathsf T}G)^{-1}G^{\mathsf T}d$, and the resolution operator is the
projection $R_m = (G^{\mathsf T}G)^{-1}G^{\mathsf T}G = I$ in exact arithmetic — so
the oscillation is not a resolution effect but an *amplification* effect. Writing
the solution in the SVD basis,
$\hat m = \sum_i(\mathbf v_i^{\mathsf T}G^{\mathsf T}d/\sigma_i^{2})\mathbf v_i$:
the coefficients in the small-$\sigma_i$ directions are the data projections
divided by $\sigma_i^{2}$, so a component of the data of order $u\|d\|$ in a weak
direction appears in the model as $u\|d\|/\sigma_i^{2}$. Those directions are
precisely the oscillatory ones, because the kernel of a gravity profile loses
sensitivity to short-wavelength structure with depth — the basis vectors
$\mathbf v_i$ of a gravity kernel are ordered polynomials and increasingly
oscillatory. The oscillation is the **noise level divided by the smallest
singular values**, and at $\kappa\sim10^{8}$ that factor of $10^{16}$ is what
turns a $10^{-11}$ mGal residual into a visible model wiggle.

**(b)** A small residual says $G\hat m$ approximates $d$, nothing more. The
identity that governs the model error is

$$\hat m - m_{\text{true}} = (G^{\mathsf T}G)^{-1}G^{\mathsf T}e
= \sum_i\frac{\mathbf v_i^{\mathsf T}G^{\mathsf T}e}{\sigma_i^{2}}\mathbf v_i,$$

so the model error can be $\kappa^{2}$ times the relative data error — here
$10^{16}u$, i.e. everything. Both statements are true at once because the
oscillatory directions fit the data almost exactly (they are nearly in the data
subspace, so they reduce the residual) while being almost unconstrained by it
(their coefficients carry the $1/\sigma_i^{2}$ amplification). A small residual is
evidence about $Gm$, not about $m$.

**(c)** In order:

1. **Do not use oscillations as a model.** Truncate or regularise: use the
   truncated SVD $m = \sum_{i:\,\sigma_i>\tau}(\mathbf v_i^{\mathsf T}G^{\mathsf T}d/\sigma_i^{2})\mathbf v_i$,
   or add Tikhonov damping $\alpha\|m - m_{\text{ref}}\|^{2}$. Both remove the
   amplification; the truncation removes the associated model variance too, at the
   price of a resolution length that must be reported.
2. **Change the parameterisation** (or add prior information): a coarser basis in
   depth removes the directions rather than damping them, which is the honest
   version of the same decision, and it makes the conditioning a modelling choice
   instead of an accident.

Neither change recovers information the data never contained; both convert an
uncontrolled error into a reported trade-off between resolution and variance.

**(d)** Report the **resolution matrix** $R = (G^{\mathsf T}G)^{-1}G^{\mathsf T}G$
in its regularised form
$R = (G^{\mathsf T}G + \alpha I)^{-1}G^{\mathsf T}G$ (and, for the truncated SVD,
$R = V_{\text{kept}}V_{\text{kept}}^{\mathsf T}$), together with the model
covariance $\hat\sigma^{2}(G^{\mathsf T}G+\alpha I)^{-1}G^{\mathsf T}G(G^{\mathsf T}G+\alpha I)^{-1}$
computed from the same matrices. The rows of $R$ are the averaging kernels: they
show exactly which oscillatory combinations of the true model the estimate cannot
distinguish, and their width is the resolution length. A reader who sees $R$ and
the covariance can judge the oscillation; a reader who sees only the model and a
residual cannot.
