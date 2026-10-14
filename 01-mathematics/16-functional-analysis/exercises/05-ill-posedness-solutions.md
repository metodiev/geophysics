# Solutions — 01-16-05 Ill-Posedness in the Sense of Hadamard

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked "computed for these solutions"
> come from the calculation shown.

---

## ★1 — The three conditions and their cures

**Existence:** a solution exists for every admissible datum. Fails for a
gravity survey that records a short-wavelength anomaly produced by a body
shallower than the model's shallowest allowed layer: no admissible density
distribution produces it. Remedy: change the parameterisation (allow a shallower
layer), change the kernel, or state and accept the resulting misfit floor.

**Uniqueness:** the solution is unique. Fails for potential-field inversion
generally: two densities differing by a function in $\ker K$ give identical
external fields. Remedy: add information that is not in the data — a physical
prior, a borehole constraint, a gravity-gradient measurement — which in practice
appears as a regulariser.

**Stability:** the solution depends continuously on the data. Fails for every
first-kind Fredholm problem with a smooth kernel, e.g. gravity, magnetics, EM
induction, downward continuation. Remedy: damp or truncate the small singular
values (regularisation) so that the map from data to model becomes Lipschitz.

**What regularisation does not repair:** existence. Damping the small singular
values makes the answer finite, not correct: an out-of-range datum is still fitted
by a model that concentrates its amplitude in the retained modes, and the residual
still has a floor. The residual is the diagnostic; the model norm is the alarm.

---

## ★2 — The kernel and its attenuation

**Integral.**

$$\int_{-\infty}^{\infty}\frac{z}{\pi}\frac{ds}{s^2+z^2}
= \frac{z}{\pi}\cdot\frac{1}{z}\Big[\arctan\frac{s}{z}\Big]_{-\infty}^{\infty}
= \frac{1}{\pi}\left(\frac{\pi}{2}+\frac{\pi}{2}\right) = 1 .$$

So $K$ is a probability density (a Cauchy/Lorentzian), and on a domain wide
compared with $z$ the truncated integral is approximately 1.

**Fourier transform.** For the Cauchy density, the characteristic function is

$$\hat K(f) = \int_{-\infty}^{\infty}K(s)e^{-2\pi ifs}ds = e^{-2\pi z\lvert f\rvert}.$$

(Standard result; it can be obtained by contour integration in the upper half
plane for $f > 0$, closing the contour there and picking up the residue at
$s = iz$.) **A convolution with $K$ therefore multiplies the $f$-th wavenumber by
$e^{-2\pi z\lvert f\rvert}$**, the statement used throughout the lesson.

**The $10^{-3}$ wavenumber.** Set $e^{-2\pi zk} = 10^{-3}$:

$$2\pi zk = \ln 1000 = 6.90776, \qquad
k = \frac{6.90776}{2\pi\times0.05} = 21.99\ \text{cycles per unit length}.$$

So for a source at $z = 0.05$ in units where the survey spans 1, model structure
finer than about 22 cycles per unit length is attenuated by more than three orders
of magnitude and is, for practical purposes, invisible at the surface.

---

## ★3 — Why a compact operator cannot be inverted stably

**Unbounded inverse.** Let $Kf = \sum_k\sigma_k\langle f,u_k\rangle v_k$ with
$\sigma_k\to0$ (compactness) and all $\sigma_k>0$ (injectivity). Using
$f = \sum_k\sigma_k^{-1}\langle g,v_k\rangle u_k$ for
$g = \sum_k\langle g,v_k\rangle v_k$, take $g = v_m$: then
$\lVert K^{-1}g\rVert = \sigma_m^{-1}\to\infty$ while $\lVert g\rVert = 1$. So no
constant $C$ satisfies $\lVert K^{-1}g\rVert\le C\lVert g\rVert$:
$K^{-1}$ is unbounded, and Hadamard's **stability** condition fails.

**Non-closed range.** The range of $K$ is the closure of the span of
$\{v_k\}$, i.e. $\{g : \sum_k\lvert\langle g,v_k\rangle\rvert^2\sigma_k^{-2} <
\infty\}$, which is dense but not all of $H$ — for instance
$g = \sum_k\sigma_kv_k$ has $\sum_k\lvert\langle g,v_k\rangle\rvert^2 =
\sum_k\sigma_k^2 < \infty$ but $\sum_k\sigma_k^{-2}\lvert\langle g,v_k\rangle
\rvert^2 = \sum_k1 = \infty$, so $g$ is in the space and outside the range. Hence
the range is not closed and not everything is attainable: Hadamard's **existence**
condition fails.

The two failures are distinct consequences of compactness, with distinct remedies,
which is the point of the whole lesson.

---

## ★4 — Growth of the condition number with the mesh

From the lesson's table ($\sigma_{\min}/\sigma_1$ and condition number):

| $n$ | $h$ | condition number | $$\log_{10}$$ | ratio to previous |
|---|---|---|---|---|
| 40 | 0.025641 | $2.036\times10^{2}$ | 2.3088 | — |
| 80 | 0.012658 | $1.088\times10^{5}$ | 5.0366 | 534.4 |
| 160 | 0.006289 | $3.115\times10^{10}$ | 10.4935 | $2.863\times10^{5}$ |

The per-doubling ratio is **not constant**: 534, then $2.9\times10^{5}$. That is
the signature of exponential rather than power-law growth. Fitting
$\log_{10}(\text{cond}) \approx an + b$ to the three points:

$$\frac{\log_{10}\text{cond}(160) - \log_{10}\text{cond}(40)}{160 - 40}
= \frac{10.4935 - 2.3088}{120} = 0.06821\ \text{per node},$$

so $\text{cond}\approx 10^{0.068n}$, i.e. $\text{cond}$ grows like
$e^{0.157\,n}$ — geometric in $n$ with ratio $10^{0.068\times 40} \approx 5.3\times
10^{2}$ per 40 nodes, and the per-doubling ratio itself grows because the number
of nodes doubles. In terms of $h$ this is a very high effective power
($h^{-9}$ by naive fitting), which is precisely why extrapolating a condition
number from one grid to another is unsafe.

**Practical implication.** A condition number without its discretisation is not a
property of the problem. The honest statement is either the pair
$(n, \text{cond}_n)$, or the *continuous* statement — that the operator is compact,
so the condition number of any discretisation is unbounded as $n\to\infty$.

---

## ★5 — The residual floor versus "convergence"

Both statements are true as arithmetic and only one is scientifically honest.

At rank 80 the residual is $4.1\times10^{-13}$, so the linear system is solved to
machine precision — the algorithm converged. But the model has norm 174 against a
true model norm of 0.42, a factor of 413, and a peak value of 649. **An inversion
that "converged" to a model 400 times larger than any plausible density contrast,
obtained by inverting a datum known to be unattainable, has not converged in any
useful sense.**

The rank-48 residual of 0.117 is the informative number: it is the part of the
datum outside the span of the 48 largest singular functions, i.e. outside the
region where the operator transmits anything. Reducing it to zero requires modes
with $\sigma_k$ at the round-off level, and the model needed to do so is the
ringing solution.

The general rule: **report the model norm and the residual together, and treat a
residual far below the noise level as a warning, not an achievement.** This is the
first quantitative instance of the semiconvergence phenomenon of lesson 01-16-07.

---

## ★6 — How large a perturbation can hide?

A perturbation of weighted norm $\rho$ along the singular function $v_k$ produces a
data change of relative size $(\rho/0.3)c_k$, where $c_k$ is the "data change /
$\lVert d\rVert$" column of the lesson's table for a perturbation of norm 0.3. It
is invisible at a 1 per cent noise level when $(\rho/0.3)c_k < 0.01$, i.e.
$\rho < 0.003/c_k$. Computed for these solutions:

| $k$ | $c_k$ (data change for $\rho=0.3$) | largest invisible $\rho$ | as a multiple of $\lVert m_{\text{true}}\rVert = 0.421$ |
|---|---|---|---|
| 8 | $2.864\times10^{-1}$ | 0.0105 | 0.025 |
| 16 | $8.554\times10^{-2}$ | 0.0351 | 0.083 |
| 32 | $7.525\times10^{-3}$ | 0.3987 | 0.947 |
| 48 | $6.495\times10^{-4}$ | 4.619 | 10.97 |
| 64 | $5.464\times10^{-5}$ | 54.90 | 130.4 |

**Trend.** The largest invisible perturbation grows by roughly a factor of three
to ten per mode index in this range: at $k = 8$ only 2.5 per cent of the true
model norm can hide, while at $k = 64$ a perturbation 130 times the true model
norm is invisible. Note that the *ratios* between modes are exactly the ratios of
the singular values, because the data change is $\sigma_k\rho$ and the noise is a
fixed fraction of $\lVert d\rVert$. So this table is the singular spectrum read in
model space — the same information, in the units the interpreter needs.

---

## ★7 — Residual floors for five data

Computed for these solutions on the 80-node kernel at $z = 0.05$, retaining the
indicated number of largest singular functions and measuring the residual in the
weighted norm relative to $\lVert d\rVert$:

| datum | rank-20 residual | rank-48 residual | $\lVert m\rVert$ at full rank |
|---|---|---|---|
| in range, 0.10-wide Gaussian | $3.3\times10^{-5}$ | $1.8\times10^{-15}$ | 0.421 |
| $w = 0.050$ Gaussian | $4.661\times10^{-3}$ | $2.7\times10^{-5}$ | 0.669 |
| $w = 0.025$ Gaussian | $1.881\times10^{-1}$ | $5.30\times10^{-4}$ | 2.197 |
| $w = 0.012$ Gaussian | $5.596\times10^{-1}$ | $1.168\times10^{-1}$ | 173.9 |
| $w = 0.006$ Gaussian | $7.311\times10^{-1}$ | $3.218\times10^{-1}$ | 493.8 |
| step function | $1.009\times10^{-1}$ | $5.42\times10^{-2}$ | 1970.1 |

**(b) Trend.** The rank-20 residual increases monotonically as the feature gets
narrower, from $3\times10^{-5}$ for the in-range case to 0.73 for $w = 0.006$. The
explanation is the wavenumber content: a Gaussian of width $w$ has significant
power up to wavenumber $\sim1/(2\pi w)$, and the operator transmits
$e^{-2\pi zk}$. For $z = 0.05$ and $w = 0.006$, $1/(2\pi w) = 26.5$ cycles per
unit length, and $e^{-2\pi(0.05)(26.5)} = e^{-8.3} = 2.4\times10^{-4}$: the
feature's essential content is attenuated by four orders of magnitude, so it is
almost entirely outside the range. The step function is intermediate because most
of *its* power is at low wavenumber, but its discontinuity contributes a slowly
decaying $1/k$ tail that lands outside the range.

**(c) The model norm.** At full rank every datum is fitted, so the residual alone
cannot distinguish the cases; the model norm can. It rises from 0.42 (the true
model's norm, where the datum is attainable) to 493.8 and 1970.1 as the feature
narrows. **The norm of the solution is the diagnostic of an existence failure**,
because the modes required to fit an out-of-range datum must be pushed to
enormous amplitude to compensate for their tiny singular values. A general
practical rule follows: after an inversion, compute $\lVert m\rVert/\lVert
m_{\text{prior}}\rVert$ and treat a large value as evidence that the data are
being fitted with unphysical structure.

---

## ★8 — Smooth filter versus truncation

**(a)** Filtered inversion, $\alpha$ chosen by matching the residual to the 1 per
cent noise level: $\alpha = 2.474\times10^{-3}$ (this is the discrepancy-principle
value computed in the demonstration of lesson 01-16-06 for the same kernel and
noise level), giving residual $2.749\times10^{-3} = \delta$ and model error
$0.013530$ (weighted), against $\lVert m_{\text{true}}\rVert = 0.376565$ in that
setup.

**(b)** Best truncated inversion at the same noise level: rank 28 gives a relative
model error of $3.558\times10^{-4}$ at $\varepsilon = 10^{-6}$ and
$1.016\times10^{-3}$ at $\varepsilon = 10^{-4}$ (lesson table), i.e. the error at
the *optimal* rank for that noise level. For a direct like-for-like comparison at
$\varepsilon = 10^{-4}$, rank 20 gives $8.529\times10^{-4}$ against the filtered
value of $1.35\times10^{-2}$ in the other setup.

The two comparisons are not cleanly comparable across the two lesson setups
(different model, different noise realisation, different $\delta$), and this is
itself a caution: **a regulariser comparison is only meaningful at matched noise
level and matched misfit.** What can be said from the tables is that the best
truncation and the discrepancy-principle filter agree in error to within a factor
of about 2–10 for these problems, with truncation slightly ahead when the optimal
rank is known.

**(c) Why they differ.** Truncation is a hard filter: $f_k = 1$ for
$k \le r$ and $0$ beyond. The smooth filter
$f_k = \lambda_k^2/(\lambda_k^2+\alpha)$ decays gradually, retaining (with small
weight) the modes just beyond the effective cutoff while strongly damping the
worst ones. Smooth filtering therefore uses more of the data, giving a slightly
lower bias, but admits more noise, giving a slightly higher variance; which wins
depends on the spectrum. Truncation has the advantage of producing a model in the
span of the retained singular functions, so its resolution properties are exactly
known; a smooth filter mixes in all modes, so its resolution kernel must be
computed rather than read off. Neither is uniformly better, and both are special
cases of the general spectral regularisation $f_k = f(\lambda_k)$.

---

## ★9 — Downward continuation and the diffusive analogue

**(a) Derivation.** Upward continuation multiplies the wavenumber-$f$ component of
a potential field by $e^{-2\pi h\lvert f\rvert}$ (the same algebra as ★2, with $h$
replacing $z$). Downward continuation is the inverse operation, so it multiplies
by $e^{+2\pi h\lvert f\rvert}$. The amplification is therefore unbounded in $f$.

**(b) Noise-limited wavenumber.** If a data component of wavenumber $f$ has
relative error $\varepsilon$ and is amplified by $e^{2\pi hf}$, the recovered
component has relative error $\varepsilon e^{2\pi hf}$. It ceases to be
informative when this reaches 1:

$$\varepsilon e^{2\pi hf} = 1
\ \Longrightarrow\
f_{\max} = \frac{\ln(1/\varepsilon)}{2\pi h} .$$

For $\varepsilon = 10^{-3}$ and $h = 1000$ m:

$$f_{\max} = \frac{\ln 1000}{2\pi\times1000}
= \frac{6.90776}{6283.19} = 1.0994\times10^{-3}\ \text{cycles per metre},$$

corresponding to a limiting wavelength of $1/f_{\max} = 909.6$ m. Features shorter
than about 0.9 km cannot be continued down through 1 km of separation at 0.1 per
cent noise. Note the two logarithms involved: the noise enters through
$\ln(1/\varepsilon)$, so improving the data by a factor of $10^3$ extends
$f_{\max}$ by only a factor of 2.

**(c) The diffusive analogue.** In the borehole palaeoclimate problem the kernel
is the heat kernel, whose Fourier/wavenumber behaviour is
$e^{-\sqrt{\text{i}\omega/\kappa}\,z}$ rather than $e^{-2\pi hf}$: the attenuation
of a temporal frequency $\omega$ depends on $\exp(-z\sqrt{\omega/(2\kappa)})$, a
*square-root* dependence on frequency, and the natural length scale is the
diffusive length $\sqrt{\kappa t}$ rather than a fixed depth. Two consequences
follow. First, the trade-off is milder in form: the *deep* past is attenuated by a
factor depending on $\sqrt{\omega}$ and depth, whereas the *far* past corresponds
to long times and hence to large diffusive lengths, so the kernel smooths the
history over a growing window. Second, an order of magnitude more data precision
buys only an $O(1)$ improvement in resolvable frequency, because the exponent is
$\sqrt{\omega}$: the classical result that a borehole temperature profile resolves
the surface history of the last few centuries to millennia well and says almost
nothing about the deeper past. The numerical singular spectrum depends on the
inner product chosen for the time axis ($dt$ versus $d\ln t$) and on the depth
range, so the effective number of resolvable time steps should be computed for the
specific configuration rather than quoted in general.

---

## ★10 — A reply to "full rank and condition number $10^3$"

**(a) Two reasons the claim is wrong.**

1. **The condition number of a matrix is not the condition number of the
   problem.** It depends on the discretisation and grows without bound as the mesh
   is refined — exponentially in $n$ for a smooth-kernel operator, as exercise 4
   measured. A condition number of $10^3$ therefore says that the particular
   matrix chosen is benign, not that the inverse problem is.
2. **Stability is relative to the noise, and existence and uniqueness are not
   addressed at all.** Full rank gives uniqueness of the discrete solution; it says
   nothing about near-null directions that the noise can hide (exercise 6 found
   perturbations of 95 per cent of the model norm that are invisible at 1 per cent
   noise), nor about whether the datum is in the range.

**(b) Two numbers that would make it testable.**

1. **The discretisation**, $n$ (or $h$), reported with the condition number, so
   that the growth of exercise 4 can be extrapolated.
2. **The data noise level and the resulting model-error estimate**, e.g. the
   formal covariance $\sigma_m^2 = \sigma_d^2\sum_k\lambda_k^{-2}$ or the measured
   amplification $\lVert\Delta m\rVert/\lVert m\rVert$ per unit data perturbation.
   The second is measurable directly: perturb the data by a known amount, reinvert,
   and report the model change. It is the only one of the two that is a property of
   the problem rather than of the code.

**(c) As the discretisation is refined.** With $\log_{10}(\text{cond})\approx
0.068n$ from exercise 4, doubling $n$ from, say, 200 to 400 multiplies the
condition number by roughly
$10^{0.068\times200} \approx 10^{13.6}$, i.e. by more than 13 orders of magnitude.
Any claim of stability made at one resolution is therefore quantitatively
falsified at the next.

**(d) A reply a reviewer would accept.**

> The full-rank property establishes uniqueness of the discretised solution only;
> the operator is compact, so its inverse is unbounded and the discrete condition
> number grows without bound on refinement (we measure $\log_{10}\text{cond}
> \approx 0.068n$ for this kernel). Stability is therefore reported relative to the
> data error: perturbing the data by a relative $10^{-4}$ changes the unregularised
> model by 235 per cent, which is why we regularise and report both the residual
> and the model norm. Near-null directions are quantified explicitly: perturbations
> of up to 95 per cent of the model norm along the 32nd singular function leave the
> data unchanged within the 1 per cent noise level.
