# Solutions — 18-02-01 Overdetermined Problems and Least Squares

> **Read after attempting the exercises.** Lesson:
> [01 Overdetermined Problems](../01-overdetermined.md).

---

## ★1 — Normal equations

$G^{\!\top}G\hat{\mathbf{m}} = G^{\!\top}\mathbf{d}$, or
$G^{\!\top}(\mathbf{d}-G\hat{\mathbf{m}}) = \mathbf{0}$. Geometrically, $G\hat{\mathbf{m}}$
is the orthogonal projection of $\mathbf{d}$ onto $\operatorname{range}(G)$, and the
residual is perpendicular to that subspace.

---

## ★2 — Predicted uncertainties

$$\operatorname{sd}(m_1) = \frac{\sigma}{\sqrt{N}} = \frac{0.05}{4.4721}
= 0.011180\ \mathrm{mGal},$$

$$\operatorname{sd}(m_2) = \frac{\sigma}{\sqrt{\sum x_i^{2}}}
= \frac{0.05}{54.2897} = 0.000921\ \mathrm{mGal\,km^{-1}} .$$

Both match the demonstration's measured scatter to three digits.

---

## ★3 — Reduced chi-squared

$\chi^{2} = 0.2484^{2}/0.05^{2} = 0.0617/0.0025 = 24.69$;
$\chi^{2}/18 = 1.3717$. The standard deviation of a $\chi^{2}_{18}/18$ is
$\sqrt{2/18} = 0.3333$, so this is $1.12$ standard deviations high: acceptable.
The proper statement is "consistent with the stated noise at the $1\sigma$ level",
not "an excellent fit".

---

## ★4 — Squared conditioning

(a) $\kappa(G)^{2} = 12.1395^{2} = 147.3684$ ✔ (identical to the printed value to
six digits).

(b) With $\kappa(G) = 10^{7}$: the SVD/QR route loses
$\log_{10}(10^{7}) = 7$ digits, leaving about $16-7 = 9$ usable digits. The normal
equations lose $\log_{10}(10^{14}) = 14$ digits, leaving about $2$ — effectively
none. Use QR or the SVD.

---

## ★5 — Halving the slope uncertainty

(a) $\operatorname{sd}(m_2)\propto1/\sqrt{\sum x_i^{2}}$, so halving it requires
$\sum x_i^{2}$ to increase by a factor $4$; for a fixed $N$ spread uniformly,
$\sum x_i^{2}\propto X^{2}$, so double the half-spread (from $\pm20$ to
$\pm40\ \mathrm{km}$).

(b) Keeping the spread and doubling $N$ to $40$ multiplies $\sum x_i^{2}$ by $2$
only, so $\operatorname{sd}(m_2)$ falls by $\sqrt{2} = 1.414$, not by $2$.

(c) Two extra stations (widening) is usually far cheaper than twenty extra
stations, and it is four times more effective for the *slope*. The trade-off: a
wider spread degrades the assumption that a single straight line applies over the
whole profile, and increases the sensitivity to long-wavelength unmodelled
structure. Widening buys precision in the model you assumed; it does not buy
correctness of that model.

---

## ★6 — Weighting

(a) $\hat{\mathbf{m}} = (G^{\!\top}W G)^{-1}G^{\!\top}W\mathbf{d}$ with
$W = \operatorname{diag}(1/\sigma_i^{2})$.

(b) Variance ratio $= (0.001170/0.000756)^{2} = 2.3906$; the unweighted estimate is
$\sqrt{2.3906} = 1.546$ times noisier.

(c) Because the station design is symmetric and the model is a straight line, the
*effective* average variance seen by the slope is close to the rms of the true
variances. A wrong variance model therefore barely changes the predicted sd here —
but it changes the *estimator* (the unweighted fit is $1.55\times$ noisier). With
clustered stations and a strongly varying $\sigma$ the error model is wrong for
the reported numbers as well
([18-02-06 §5](../06-weighting-and-covariance.md)).

---

## ★★★7 — Separating three failure modes of chi-squared

**Simulations.** (i) Fix $\sigma$ but simulate with $1.5\sigma$; (ii) fix
$\sigma$ but generate data with an extra quadratic term that $G$ does not model;
(iii) fix $\sigma$ but generate errors with $\rho = 0.7$.

**Statistics and decisiveness.**

- *Wrong $\sigma$*: reduced $\chi^{2}$ shifts by exactly the variance ratio
  ($2.25\times$ for $1.5\sigma$) and the residual *autocorrelation* stays near
  zero. Test: rescale $\hat\sigma^{2} = \lVert\mathbf{r}\rVert^{2}/(N-M)$ and check
  whether the scalar is stable across sub-samples.
- *Unmodelled physics*: the residual is **structured** — its autocorrelation and
  its correlation with the omitted basis function are non-zero, and
  $\chi^{2}$ grows with the number of data once $N$ is large enough to resolve the
  misfit. Test: residual-versus-$x$ plot and a runs test.
- *Correlated errors*: the residual is smooth **and** the empirical
  autocorrelation of the residuals has a long, positive tail at lags far beyond any
  omitted physics. Test: whiten with a candidate $C_d$ and re-run $\chi^{2}$; if it
  moves to 1, the correlation model was the issue.

**Decisiveness.** The three are not separated by a single number. $\chi^{2}$ alone
detects all three; only the *shape* of the residual (autocorrelation, run structure,
correlation with candidate basis functions) distinguishes them. Report the
diagnostics, not just the scalar.

---

## ★★★8 — When "optimal" is true

**Theorem.** Gauss–Markov: among **linear unbiased** estimators, the
generalised least-squares estimator
$(G^{\!\top}C_d^{-1}G)^{-1}G^{\!\top}C_d^{-1}\mathbf{d}$ has minimum variance.

**Hypotheses and violations.**

1. *$C_d$ is the true covariance (up to scale).* Violation: errors are correlated by
   processing but treated as white → the estimator stays unbiased but is no longer
   minimum variance, and the reported covariance is wrong by whatever factor the
   geometry imposes (measured up to $33\times$ in
   [18-02-06 §5](../06-weighting-and-covariance.md)).
2. *The model is linear in the estimated parameters, and correct ($\mathbf{d}$ has
   zero mean given $\mathbf{m}$).* Violation: an unmodelled trend component →
   **bias** in every parameter, which no weighting repairs.
3. *Linear estimators only.* Violation: for non-Gaussian errors (e.g. heavy-tailed,
   spiky) a nonlinear/robust estimator can beat any linear one; least squares can be
   dragged arbitrarily far by a single outlier
   ([21-01-04](../../../21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md)).
