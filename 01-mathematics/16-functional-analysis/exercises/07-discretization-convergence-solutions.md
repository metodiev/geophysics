# Solutions — 01-16-07 Discretisation, Convergence and Regularisation Discrepancy

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked "computed for these solutions" come
> from the calculation shown.

---

## ★1 — The three errors

1. **Discretisation error.** The model space cannot represent structure finer than
   the grid; it decreases with $h$ and then saturates.
2. **Regularisation bias.** The filter discards a band of singular values; it is
   fixed by $\alpha$ and **does not shrink with $h$**. This is the term that makes
   the answer flat in the bias-dominated regime: the measured error at
   $\alpha = 10^{-1}$ is 0.094265, 0.094342, 0.095429, 0.095080 over an eightfold
   refinement.
3. **Propagated data error.** Noise amplified by the retained singular values; at
   fixed $\alpha$ it *grows* as $h\to0$, because refining adds singular directions
   below the knee that are still transmitted.

Without a regulariser the third term diverges. With a fixed regulariser the second
term never goes away. Only when $\alpha$ is tied to $\delta$ and allowed to fall do
all three shrink together — the convergence of Section 5 of the lesson.

---

## ★2 — The regularisation discrepancy

**Definition.** The regularisation discrepancy is the difference between the
regularised solution of the discretised problem and the exact solution of the
underlying continuous problem, evaluated at a *finite* data error $\delta$ and a
*finite* regularisation $\alpha$.

**Why it matters.** The convergence theorem is a statement about the limit
$\delta\to0$ with $\alpha(\delta)$ chosen so that $\delta^2/\alpha\to0$. Real data
have a fixed $\delta$ that cannot be reduced, so the theorem's hypothesis is never
satisfied and its conclusion — convergence to $m^\dagger$ — is never directly
observed. What one sees instead is a sequence of errors that falls and then
flattens, and the flattening is the discrepancy. It is the practically relevant
object because it is what determines whether more data, a finer grid, or a better
regulariser would actually help.

The demonstration's discrepancy-principle sequence makes it concrete: the model
error falls 0.016824, 0.015865, 0.014252, 0.010524 as $n$ doubles — monotone, but
with the last ratio 0.738; three more doublings would be needed to halve the error
again at that rate, and the rate itself is deteriorating.

---

## ★3 — Conditions for convergence, and the source condition

**The two conditions.** With $\lVert d^\delta-d\rVert\le\delta$, Tikhonov
regularisation with $\alpha = \alpha(\delta)$ converges to the minimum-norm
solution if

$$\alpha(\delta)\to0 \qquad\text{and}\qquad \frac{\delta^2}{\alpha(\delta)}\to0
\quad\text{as }\delta\to0 .$$

- **If $\alpha\not\to0$:** the bias does not vanish, so the limit is the regularised
  solution at some fixed $\alpha$, not $m^\dagger$. The measurement is the bias
  floor of the lesson's Section 3.
- **If $\delta^2/\alpha\not\to0$** (i.e. $\alpha$ too small): the noise term
  $\delta^2/\alpha$ does not vanish and the limit is the unregularised
  least-squares solution, whose norm blows up. The measurement is the
  full-rank amplification of lesson 01-16-05.

The discrepancy principle satisfies both: it gives $\alpha \sim \delta$ (or
$\delta^{2}$ depending on the source condition), in either case with
$\delta^2/\alpha \sim \delta \to 0$.

**Why no rate without a source condition.** Convergence alone says the error goes
to zero; the *rate* is determined by how strongly the truth is aligned with the
well-determined singular directions. The standard source condition
$m^\dagger = F^{\mathsf T}Fw$ for some $w$ with $\lVert w\rVert\le\rho$ says the
truth has no content in the poorly determined directions at all, and with it one
obtains $O(\delta^{2/3})$ for Tikhonov; with a stronger condition, $O(\delta)$;
without any, convergence can be arbitrarily slow. Since a geophysical model is
never known to satisfy a source condition, **the honest practice is to report the
observed error sequence and the noise level, not a rate.**

---

## ★4 — Conditioning of the discretisation

From the lesson's table (computed ratios):

| $n$ | $\lambda_{\min}$ | $\lambda_{\min}$ ratio | condition number | condition ratio |
|---|---|---|---|---|
| 20 | $1.025\times10^{-1}$ | — | $8.863$ | — |
| 40 | $4.422\times10^{-3}$ | 0.0431 | $2.036\times10^{2}$ | 22.97 |
| 80 | $8.264\times10^{-6}$ | 0.001869 | $1.088\times10^{5}$ | 534.4 |
| 160 | $2.884\times10^{-11}$ | $3.490\times10^{-6}$ | $3.115\times10^{10}$ | $2.863\times10^{5}$ |

$\lambda_1$ stays at 0.900–0.908, so the condition number grows exactly as
$1/\lambda_{\min}$: the collapse of the smallest singular value *is* the loss of
conditioning.

**Linearity of $\log_{10}$ of the condition number.** $\log_{10}(\text{cond})$ takes
the values 0.9476, 2.3088, 5.0366, 10.4935. Fitting over the whole range,

$$\text{slope} = \frac{10.4935-0.9476}{160-20} = 0.0682\ \text{per node},$$

so $\text{cond}\approx10^{0.0682n}$ — exponential in $n$, i.e. geometric in $h$
with a very high effective power. Since the growth is exponential in the number of
nodes rather than a power of $h$, extrapolating a condition number from one grid to
another is quantitatively unreliable; the useful statement is the *pair*
$(n,\text{cond}_n)$ or the qualitative statement that the operator is compact so the
condition number is unbounded.

---

## ★5 — Bias-dominated versus noise-dominated refinement

| $\alpha$ | error at $n=20$ | error at $n=160$ | ratio |
|---|---|---|---|
| $10^{-1}$ | 0.094265 | 0.095080 | 1.0087 |
| $10^{-3}$ | 0.018000 | 0.011450 | 0.6361 |

**$\alpha = 10^{-1}$: ratio 1.009.** The error is unchanged by an eightfold
refinement, because it is dominated by the bias of the regulariser. With
$\operatorname{tr}R_\alpha\approx7.75$ at every $n$, the retained band is already
represented on the coarsest grid; there is nothing for the extra nodes to
contribute. Note that the residual at this $\alpha$ is 15.8 times the noise level:
**the model is deliberately under-fitting, and that is the correct behaviour when
the data are noisy.**

**$\alpha = 10^{-3}$: ratio 0.636.** The error falls, but non-monotonically: 0.0180
at $n=20$, 0.0272 at $n=40$, 0.0201 at $n=80$, 0.0115 at $n=160$. The intermediate
grids are worse than the coarse one because they expose ill-conditioned directions
(the condition number goes from 8.9 to $2\times10^2$) while the regularisation is
too weak to suppress them; and at every grid the residual is *below* the noise
level (0.22 to 0.99 of $\delta$), i.e. the fit is over-fitting the noise. So the
ratio 0.636 is a net improvement achieved along a non-monotone path, and the
$n=20$ value is good for a reason that does not generalise — the discretisation
itself is doing the regularising.

---

## ★6 — The discrepancy principle at $n = 40$

**Monotonicity.** $R(\alpha) = \lVert Km_\alpha-d^\delta\rVert$ is increasing in
$\alpha$: mode $k$ contributes
$\lvert 1-f_k\rvert^2\lvert\langle d,u_k\rangle\rvert^2$ with
$R^2 = \sum_k(1-f_k)^2\langle d,u_k\rangle^2$, and $1-f_k =
\alpha/(\lambda_k+\alpha)$ increases in $\alpha$ for every mode. So $R$ is
continuous and strictly increasing on $(0,\infty)$, with
$R(0) = 0$ (full rank) and $R(\infty) = \lVert d\rVert$. A unique root exists for
any $0<\delta<\lVert d\rVert$.

**Bracket.** At $n = 40$ the lesson's fixed-$\alpha$ table gives
$R(10^{-3}) = 2.031\times10^{-3} < \delta = 3.067\times10^{-3}$; and
$R(5\times10^{-3}) > \delta$ from the monotonicity and the fact that
$\alpha_{\text{disc}} = 3.224\times10^{-3}$ is reported. So the root lies in
$(10^{-3},5\times10^{-3})$.

**Bisection.** Iterating $\alpha_{m+1} =
\sqrt{\alpha_{\text{lo}}\alpha_{\text{hi}}}$ with the update
$\alpha_{\text{lo}}\to\alpha_{m+1}$ if $R(\alpha_{m+1})<\delta$ and
$\alpha_{\text{hi}}\to\alpha_{m+1}$ otherwise converges to
$\alpha_{\text{disc}} = 3.224\times10^{-3}$; about
$\log_2(5) \approx 2.3$ bisections per significant figure, so 8 bisections give
three figures. (The lesson's program runs 120 because each step is cheap and
$\log$-spaced bisection converges at half speed in the exponent.)

**Triangle-inequality check.** The residual measured against the exact data at that
$\alpha$ is $2.200\times10^{-3}$ (computed for these solutions). Then

$$\big\lvert\lVert Km-d^\delta\rVert - \lVert Km-d\rVert\big\rvert
= \lvert 3.067\times10^{-3} - 2.200\times10^{-3}\rvert = 8.67\times10^{-4}
\le \lVert d^\delta-d\rVert = 3.067\times10^{-3},$$

so the reverse triangle inequality is satisfied. It is a check worth running after
any parameter-choice computation: it detects a mix-up between the exact and noisy
data vectors, which is a common implementation error.

---

## ★7 — The moving cutoff of the Landweber iteration

Computed for these solutions at $n = 80$ with $\tau = 0.61872$
($\tau = 0.5/\lVert K^{\mathsf T}K\rVert$), using the cutoff
$\lambda^\ast = \ln 2/(\tau j)$ obtained from $f_k^{(j)} = 1-(1-\tau\lambda_k)^j =
0.5$ under the small-$\lambda$ approximation $1-\tau\lambda \approx
e^{-\tau\lambda}$:

| $j$ | model error | residual | $\lambda^\ast$ | nearest $k$ | $\lambda_k$ | filter factor at $k$ |
|---|---|---|---|---|---|---|
| 25 | 0.031262 | 0.008232 | $4.480\times10^{-2}$ | 21 | $4.412\times10^{-2}$ | 0.4994 |
| 50 | 0.014686 | 0.004105 | $2.240\times10^{-2}$ | 25 | $2.403\times10^{-2}$ | 0.5272 |
| 100 | 0.005719 | 0.003066 | $1.120\times10^{-2}$ | 30 | $1.123\times10^{-2}$ | 0.5021 |
| 200 | 0.005597 | 0.002881 | $5.600\times10^{-3}$ | 35 | $5.240\times10^{-3}$ | 0.4777 |
| 400 | 0.009370 | 0.002825 | $2.800\times10^{-3}$ | 39 | $2.843\times10^{-3}$ | 0.5056 |

**(a)–(b)** The identified index increases monotonically with $j$ — 21, 25, 30, 35,
39 — and the filter factor at that index is $0.48$ to $0.53$ in every case. So the
cutoff really does move like $\lambda^\ast \propto 1/j$, and the iteration is a
low-pass filter whose passband widens at a known rate. (The model errors here differ
from the lesson's printed history by a few per cent — 0.031262 against 0.0318 at
$j=25$ — because this rerun draws its own noise realisation from the same
generator; the residual column is new information not printed in the lesson.)

**(c) Predicting the optimum.** The error is minimised when the filter has just
included the modes that the data determine and no more; that is when
$\sigma_{k^\ast}^2 \approx \delta^2/\lVert d\rVert^2$-scale of the noise, i.e. when
the cutoff reaches the singular value at which the signal-to-noise ratio falls to
1. An operational version: with 1 per cent noise the residual should be brought down
to about $\delta$, and the table shows that happens at $j \approx 100$ (residual
$3.066\times10^{-3}$, essentially equal to $\delta = 3.066\times10^{-3}$), where the
error is 0.005719 — close to the measured optimum $j \approx 200$ with error
0.005597. **Stopping when the residual equals the noise level lands within a factor
of two of the optimal model**, which is the practical rule for iterative
regularisation; stopping when the residual is *smallest* (at $j = 400$, then
beyond) gives error 0.009370 and rising.

---

## ★8 — Refinement without the inverse crime

**Setup.** Synthesise on the $n = 320$ grid: sample the truth there, form
$d = K_{320}m$, add 1 per cent Gaussian noise
($\lVert d\rVert = 0.306629$, $\delta = 3.066\times10^{-3}$). Then invert on
$n = 20, 40, 80, 160$, using the **subset** of the 320 nodes that each coarse grid
occupies (320 is divisible by each), so the coarse data are exact samples of the
noisy fine data. The coarse forward operator uses the coarse trapezoid weights, so
the coarse datum is *not* in the range of the coarse operator: this is the model
mismatch that the crime-committing study removes.

Computed for these solutions:

| $n$ | $\alpha$ | model error | residual | $\delta$ | residual/$\delta$ |
|---|---|---|---|---|---|
| 20 | $10^{-3}$ | 0.020684 | 0.000651 | $2.186\times10^{-3}$ | 0.298 |
| 20 | $3.406\times10^{-3}$ (disc.) | 0.022452 | 0.002186 | $2.186\times10^{-3}$ | 1.000 |
| 40 | $10^{-3}$ | 0.027323 | 0.001552 | $2.592\times10^{-3}$ | 0.599 |
| 40 | $3.010\times10^{-3}$ (disc.) | 0.019158 | 0.002592 | $2.592\times10^{-3}$ | 1.000 |
| 80 | $10^{-3}$ | 0.020115 | 0.002500 | $2.910\times10^{-3}$ | 0.859 |
| 80 | $2.287\times10^{-3}$ (disc.) | 0.015372 | 0.002910 | $2.910\times10^{-3}$ | 1.000 |
| 160 | $10^{-3}$ | 0.014886 | 0.002788 | $2.983\times10^{-3}$ | 0.935 |
| 160 | $1.786\times10^{-3}$ (disc.) | 0.012348 | 0.002983 | $2.983\times10^{-3}$ | 1.000 |

**(a)–(b) Comparison.**

- **Fixed $\alpha = 10^{-3}$** gives a non-monotone sequence — 0.020684, 0.027323,
  0.020115, 0.014886 — closely paralleling the crime-committing sequence
  (0.018000, 0.027175, 0.020125, 0.011450) but *worse at every grid*, exactly as the
  model mismatch requires. The residual is below the noise level at every grid
  (0.298 to 0.935 of $\delta$), so the over-fitting diagnosis survives the removal
  of the crime.
- **With the discrepancy principle** the sequence is monotone decreasing —
  0.022452, 0.019158, 0.015372, 0.012348 — and higher than the crime-committing
  sequence (0.016824, 0.015865, 0.014252, 0.010524) at three of the four grids.
  Interestingly it is *worse* than fixed $\alpha = 10^{-3}$ at $n = 20$
  (0.022452 against 0.020684): on the coarsest grid the discrepancy principle
  over-regularises, because much of the misfit there is model mismatch rather than
  noise, so matching the residual to $\delta$ forces $\alpha$ too high. **This is
  the failure mode of the discrepancy principle identified in lesson 01-16-06: it
  assumes the model can fit the data at the noise level.**

**(c) The plateau.** No plateau appears *in this study* that is not explained by the
noise level: the discrepancy-principle errors keep falling, and the fixed-$\alpha$
errors keep improving after the $n = 40$ excursion. The reason is that the truth
here is representable on every coarse grid (the nodes are a subset of the fine
grid), so the only model mismatch is the quadrature difference between the coarse
and fine forward operators, which is small. **To see the existence floor of lesson
01-16-05 one must reduce the model space's representational power rather than its
resolution** — for instance by restricting the model to a coarse basis while keeping
the fine datum, or by including a feature narrower than the shallowest resolvable
scale. That is the experiment that produces a residual floor independent of $\alpha$,
and it is the reason lesson 01-16-05 emphasised that existence failures are cured by
changing the model space, not by damping.

## ★9 — The resolved band and the mesh

**(a)** The $k$-th singular function on $[0,1]$ has approximately $k/2$ cycles per
unit length, so its Fourier multiplier is
$\sigma_k \approx e^{-2\pi z(k/2)} = e^{-\pi zk}$. Setting
$\sigma_{k^\ast} = \sqrt\alpha$:

$$e^{-\pi zk^\ast} = \alpha^{1/2}
\ \Longrightarrow\
k^\ast = \frac{\ln(1/\alpha)}{2\pi z} .$$

Evaluating at $z = 0.05$:

$$\alpha = 10^{-1}:\ k^\ast = \frac{2.302585}{0.314159} = 7.33 ;\qquad
\alpha = 10^{-3}:\ k^\ast = \frac{6.907755}{0.314159} = 21.99 ;\qquad
\alpha = 10^{-8}:\ k^\ast = \frac{18.420681}{0.314159} = 58.63 .$$

**(b)** Against the measured traces:

| $\alpha$ | $k^\ast$ (predicted) | $\operatorname{tr}R_\alpha$ (measured) | ratio |
|---|---|---|---|
| $10^{-1}$ | 7.33 | 7.75 | 1.058 |
| $10^{-3}$ | 21.99 | 22.56 | 1.026 |
| $10^{-8}$ | 58.63 | 60.24 | 1.027 |

The prediction is 2.6–5.8 per cent low, and the offset is systematic: the count
$\operatorname{tr}R_\alpha$ includes the modes on the *upper* side of the knee,
where $f_k$ is still appreciable (0.3–0.7), so it slightly exceeds the number of
modes with $\sigma_k > \sqrt\alpha$. That the ratio is nearly constant across five
decades of $\alpha$ is the evidence that the approximation $\sigma_k \approx
e^{-\pi zk}$ is the right model for this spectrum.

**(c) Mesh independence.** $k^\ast$ depends only on $\alpha$ and $z$ — not on $h$.
The resolved band is therefore a band of *physical* wavenumbers (about
$f^\ast = k^\ast/2 = \ln(1/\alpha)/(4\pi z)$ cycles per unit length), fixed by the
depth and the damping. The number of nodes representing it,
$k^\ast$, is likewise fixed; what grows with refinement is the *rest* of the grid:
the Nyquist wavenumber is $f_N = 1/(2h)$, so the retained fraction
$f^\ast/f_N = 2hf^\ast$ falls like $h$. Every added node is damped by a factor
$\alpha/(\lambda_k+\alpha)$ smaller than its predecessor.

**Why no polynomial scaling works.** If $\alpha_n = \alpha_0h^p$, then
$k^\ast_n = [\ln(1/\alpha_0) + p\ln(1/h)]/(2\pi z)$ — only *logarithmically*
dependent on $h$. To make the resolved band proportional to the Nyquist wavenumber
one would need $k^\ast \propto 1/h$, i.e. $\ln(1/\alpha) \propto 1/h$, which no
power law can provide. **This is a restatement of the central negative result of
the whole module: refining a discretisation cannot recover information that the
data do not carry, and the resolved band is set by the physics and the noise level,
not by the mesh.**
