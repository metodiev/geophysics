# Solutions — 18-03-01 Why Regularisation Is Physically and Statistically Justified

> **Read after attempting the exercises.** Numbers below were computed, not
> estimated by hand; where a demonstration value is quoted, it is the value the
> demonstration prints.

Lesson: [01 Why Regularisation Is Physically and Statistically Justified](../01-why-regularize.md).
All models are **SYNTHETIC**.

---

## ★1 — Noise level

Peak anomaly $221.27\ \mathrm{mGal}$, so

$$\sigma_e = 0.005\times221.27 = 1.1064\ \mathrm{mGal}.$$

The demonstration prints $1.1063\ \mathrm{mGal}$ — the same number; the
difference is rounding of the peak value.

The single-coefficient noise level is $\sqrt{\mathbb E[(u_i^{\mathsf T}e)^2]}$.
Because $U$ is orthogonal, $u_i^{\mathsf T}e$ is a linear combination of the
noise components with $\|u_i\|_2 = 1$, so

$$\mathrm{Var}(u_i^{\mathsf T}e) = \sigma_e^2\|u_i\|_2^2 = \sigma_e^2
\;\Rightarrow\; \sqrt{\mathbb E[(u_i^{\mathsf T}e)^2]} = \sigma_e
= 1.106\ \mathrm{mGal}.$$

The two numbers are equal because orthonormal projection preserves the noise
variance. That is exactly why the Picard plot's horizontal axis needs no
rescaling.

---

## ★2 — Two worst-case bounds

With $n = 64$, $\|e\| = \sigma_e\sqrt{64} = 1.1063\times8 = 8.850\ \mathrm{mGal}$:

$$\text{one datum: } \frac{\kappa_2\sigma_e}{\|d\|}
= \frac{1.163\times10^{6}\times1.1063}{969.5} = 1.327\times10^{3},$$

$$\text{whole vector: } \frac{\kappa_2\|e\|}{\|d\|}
= \frac{1.163\times10^{6}\times8.850}{969.5} = 1.062\times10^{4}.$$

Both agree with the demonstration's printed values ($1.327\times10^{3}$ and
$1.062\times10^{4}$).

**What neither bound claims.** Neither says that an error of that size *will*
occur: they are worst-case statements over perturbations of the stated norm, and
they say nothing about the typical error. The measured ordinary-case error is
$2.231\times10^{3}$, which lies between the two bounds — larger than the
single-datum bound by a factor of $1.7$ and smaller than the whole-vector bound
by a factor of $4.8$. A worst-case bound that the ordinary case violates is
either mis-stated or too optimistic; here the ordinary case respects both.

---

## ★3 — Resolution and the fitted decay

With $\sigma_i \sim i^{-q}$ and $\sigma_1$ as reference:

- $q = 3.24$: $\sigma_{32}/\sigma_1 = 32^{-3.24}
  = e^{-3.24\ln 32} = e^{-3.24\times3.4657} = e^{-11.229}
  = 1.33\times10^{-5}$.
- $q = 1.64$: $\sigma_{32}/\sigma_1 = e^{-1.64\times3.4657} = e^{-5.684}
  = 3.40\times10^{-3}$.

The demonstration prints $\sigma_{32}/\sigma_1 = 9.555\times10^{-4}$ for the
$0.6\ \mathrm{km}$ target, and reports $\kappa_2 = 7.661\times10^{2}$ with
$q = 1.64$ for the $0.3\ \mathrm{km}$ target at the same spacing. The power law
is a global fit over $i = 1,\dots,48$ and does not reproduce every single
singular value (it gives $32^{-3.24} = 1.33\times10^{-5}$, smaller than the
tabulated $9.555\times10^{-4}$). The robust conclusion is the
ratio of the two decays: the deep target's spectrum is between two and three
orders of magnitude smaller at $i = 32$, so **the $0.3\ \mathrm{km}$ target is
better resolved**, and it is better resolved because it is shallower, not
because it is easier to compute.

---

## ★★★4 — Exact-data against noisy-data error

$$\frac{2.231\times10^{3}}{1.316\times10^{-10}} = 1.70\times10^{13}.$$

**Why.** With exact data the least-squares solution is $m_{\mathrm{true}}$ up to
round-off, and the round-off error is amplified by $\kappa_2$, giving
$\sim10^{-16}\times10^{6} = 10^{-10}$. With noise, each coefficient gains
$u_i^{\mathsf T}e/\sigma_i$, and the *total* error is dominated by the smallest
singular values:

$$\mathbb E\|m_{\mathrm{LS}}-m_{\mathrm{true}}\|^2
= \sum_i \frac{\sigma_e^2}{\sigma_i^2}
\approx \frac{\sigma_e^2}{\sigma_{\min}^2}\times(\text{tail mass})
= \sigma_e^2\,\kappa_2^2/\sigma_1^2\times O(1).$$

Numerically, $\sigma_e/\sigma_{\min} = 1.1063/8.6\times10^{-7}\,\sigma_1
= 1.29\times10^{6}\sigma_1^{-1}$, whose square is $\sim10^{12}$, and the
observed squared error is $(2.231\times10^{3})^2 = 4.98\times10^{6}$ in
model-norm units — the difference is the $1/\|m_{\mathrm{true}}\|^2$ normalisation
and the fact that the noise is not fully concentrated in the last direction. The
essential statement is that the exact-data error is set by machine precision,
while the noisy-data error is set by $\sigma_e$ divided by the small singular
values: **thirteen orders of magnitude apart, from the same matrix.**

---

## ★★5 — Why the Picard index can differ from the truncation optimum

The Picard index (5) counts coefficients whose exact value exceeds the noise
level by more than $10\times$. It is a property of the *signal-to-noise ratio per
coefficient*: $|\sigma_i x_i| > 10\sigma_e$.

The truncation optimum (7) minimises the *total* error
$\sum_i[(1-f_i)^2x_i^2 + \sigma_e^2f_i^2/\sigma_i^2]$. It can exceed the Picard
index because components with $|x_i|$ small but non-negligible can be worth
retaining: their squared bias $(1-f_i)^2x_i^2$ is tiny, while discarding them
costs a real piece of the model. Reading the demonstration's rank table:

| $k$ | relative error |
|---|---|
| 4 | $1.72\times10^{-1}$ |
| 6 | $3.56\times10^{-2}$ |
| 8 | $7.91\times10^{-3}$ |
| 7 (optimum) | $7.36\times10^{-3}$ |

Interpolating between $k = 4$ and $k = 6$ for $k = 5$ gives roughly
$10^{-1}$: choosing 5 instead of 7 costs about a factor of 14 — the error is
*not* flat in the rank here, which is itself a measurement worth reporting.

---

## ★★6 — Refining the grid

Refining from 64 to 256 cells at fixed station spacing adds cells closer together
relative to the $0.6\ \mathrm{km}$ depth. The columns of the new $K$ for adjacent
cells are more nearly parallel, so

- $\sigma_{\min}$ falls rapidly (the fitted $q \approx 3.2$ suggests
  $\sigma_{256}/\sigma_{64} \sim (1/4)^{3.2} \approx 10^{-2}$ at the same index),
- $\kappa_2$ rises by a comparable factor or more,
- the **unregularised** error rises proportionally to $\kappa_2$, i.e. by at
  least an order of magnitude,
- the **regularised** error barely changes, because the newly added components
  lie below the noise floor and are filtered.

The falsifiable prediction: the truncated-SVD optimum error should stay of order
$10^{-2}$ while the unregularised error grows by a factor of 10 or more. A
refinement that *reduces* the unregularised error would indicate that the new
cells are not actually being resolved, i.e. that the model grid and the data grid
are being confused.

---

## ★★★7 — Experiment design (specification)

**Statistic.** The truncation index $k^\star$ defined as the smallest $k$ such
that the truncated-SVD relative error is within 10% of its minimum over
$k = 1,\dots,64$; report its median over realisations plus the 10–90% range.

**Design.** Hold $d_{\text{target}}\cdot\Delta x = \text{const}$ while varying
$d_{\text{target}} \in \{0.3, 0.6, 1.2\}\ \mathrm{km}$ and
$\Delta x \in \{254, 127, 63.5\}\ \mathrm{m}$; fix the noise at $0.5\%$ of the
peak anomaly and use 200 realisations per cell of the design.

**Prediction.** $k^\star$ depends on the ratio $d/\Delta x$, not on either alone;
on the locus $d\Delta x = \text{const}$ the measured $k^\star$ should be
approximately constant.

**Falsification.** If $k^\star$ depends strongly on $\Delta x$ along that locus,
then the resolution is set by the discretisation rather than by depth, and the
"resolution is set by depth" claim in the lesson would need qualifying. This is
the interesting outcome, and the experiment is designed to be able to produce it.

---

## ★★★8 — Scaling of the second-kind control

With $A = cI + K$ and data $d = A m_{\mathrm{true}} + e$,

$$m_A - m_{\mathrm{true}} = A^{-1}e .$$

Because $A$ is symmetric with eigenvalues $c + \lambda_i(K)$, and
$\|A^{-1}\|_2 = 1/(c+\lambda_{\min}(K))$,

$$\mathbb E\|A^{-1}e\|^2 = \sigma_e^2\sum_i\frac{1}{(c+\lambda_i)^2}
\;\le\; \frac{n\sigma_e^2}{(c-\sigma_{\max})^2},$$

so for $c \gg \sigma_{\max}$ the error is $\sim\sigma_e\sqrt n/c$ and **the
relative error grows as $c$ shrinks**, not as it grows. Reducing $c$ by a factor
of 100 with the data generated by $A$ itself multiplies
$\sigma_{\max}/c$ by 100 and drives the error towards the first-kind behaviour:
at $c = \sigma_{\max}$ the operator becomes singular, since
$\lambda_{\min}(K) = -\sigma_{\max}$ can cancel $c$.

**Conclusion.** Adding a constant to the diagonal removes the ill-posedness only
by changing what was measured. The demonstration's $1.76\times10^{-2}$ error is
small *because its data were generated by $A$*, so inverting with $A$ is exact
up to noise. Applied instead to data from the true first-kind operator $K$,
$A^{-1}d$ is a biased estimator of $m_{\mathrm{true}}$: the shift $cI$ acts as a
Tikhonov penalty, and the bias it introduces has to be argued for, exactly as an
$\alpha$ does in [02 Tikhonov Regularisation](../02-tikhonov.md).
