---
id: 01-16-07
title: "Discretisation, Convergence and Regularisation Discrepancy"
level: doctoral
prereqs: ["01-16-06", "01-12-07"]
estimated_minutes: 90
tags: [discretisation, convergence, regularization-discrepancy, semiconvergence, landweber]
---

# Discretisation, Convergence and Regularisation Discrepancy

## Learning objectives

By the end of this lesson you will be able to:

1. **Separate** the three errors that a regularised inversion carries — the
   discretisation error, the regularisation bias, and the propagated data error —
   and say which dominates in which regime.
2. **Measure** what happens to the model error when the grid is refined at fixed
   $\alpha$, including the non-monotone behaviour and the over-fitting of noise.
3. **Explain** why a fixed $\alpha$ resolves an asymptotically fixed number of
   degrees of freedom regardless of the mesh, and why that makes $\alpha$ a
   property of the noise rather than of the discretisation.
4. **Choose** $\alpha$ by the discrepancy principle at each level of refinement and
   demonstrate that the resulting sequence of models converges.
5. **State** the conditions under which a regularised solution converges to the
   minimum-norm solution of the underlying continuous problem, and what the
   regularisation discrepancy is.
6. **Demonstrate** semiconvergence of the Landweber iteration, identify the
   optimal stopping index, and show that it grows with the discretisation.
7. **Explain** why a residual below the noise level is evidence of a mistake rather
   than of accuracy, in the context of a refinement study.

## Prerequisites

- [01-16-06 Tikhonov Regularisation and the L-Curve](./06-regularization-theory.md)
  — the filter factors, $\operatorname{tr}R_\alpha$ and the parameter-choice rules
  used throughout.
- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](../12-numerical-methods/07-pde-discretisation.md)
  — the forward-side version of this lesson: a scheme is consistent, stable and
  hence convergent.
- [01-16-05 Ill-Posedness in the Sense of Hadamard](./05-ill-posedness.md) — the
  growth of the condition number with refinement that motivates everything here.

## 1. The question, and why it is not the forward-problem question

For a well-posed forward problem solved on a mesh of size $h$, the story is
familiar and satisfying: as $h\to0$ the discrete solution converges to the
continuous one at a rate set by the order of the scheme. Halving the mesh halving
the error. **For an ill-posed inverse problem that story fails**, and the way it
fails is the subject of this lesson.

Three errors are in play, and only one of them shrinks with the mesh:

| Error | Source | Behaviour with $h\to0$ |
|---|---|---|
| Discretisation | the model space cannot represent fine structure | decreases, then saturates |
| Regularisation bias | the filter discards a band of singular values | fixed by $\alpha$, independent of $h$ |
| Propagated data error | noise amplified by the retained singular values | grows with $h\to0$ at fixed $\alpha$ |

Without a regulariser the third term diverges; with a fixed regulariser the second
term never goes away. The resolution is that $\alpha$ must be tied to the noise
level and allowed to shrink as the grid is refined — which is the classical theory
of Section 6 and the numerics of Sections 3–5.

### 1.1 The setting, and one honest caveat

The demonstration uses the gravity kernel
$K(s) = (z/\pi)/(s^2+z^2)$, $z = 0.05$, discretised on $n$ nodes for
$n = 20, 40, 80, 160$, with the *same* discretisation used to synthesise and to
invert the data:

```text
        n           h      lambda_1    lambda_min       cond(K)
       20     0.05263      0.908068     1.025e-01     8.863e+00
       40     0.02564      0.900201     4.422e-03     2.036e+02
       80     0.01266      0.898952     8.264e-06     1.088e+05
      160     0.00629      0.898357     2.884e-11     3.115e+10
```

Note $\lambda_1$ is essentially mesh-independent ($0.9081\to0.8984$) while
$\lambda_{\min}$ collapses by ten orders of magnitude: the operator's *scale* is a
property of the physics, and its *conditioning* is a property of the mesh.

**The caveat, stated rather than buried.** Using one discretisation for the
synthesis and the inversion is an **inverse crime**. It removes the model error
that a real experiment has (the truth is representable on the grid) and thereby
isolates the effect of the discretisation — which is exactly what this lesson
wants — but it makes the computed model errors optimistically small in absolute
terms, and any study that reports *resolution* must not do it. A realistic study
synthesises with a finer grid, a different scheme, or an analytic solution. The
qualitative conclusions below survive; the absolute error values do not.

## 2. What a refinement actually does

Since $\lambda_1$ does not change but $\lambda_{\min}$ collapses, refining the grid
adds model parameters whose singular values lie deeper in the noise. Three
consequences, each measured below:

- At fixed $\alpha$, the estimator keeps damping the same band of *physical*
  wavenumbers, so the number of resolved parameters converges (Section 4).
- The residual, however, falls: the finer grid offers more small singular
  directions for the estimator to use, and with $\alpha$ unchanged they are used.
- The model error therefore behaves non-monotonically, because it is the sum of a
  decreasing discretisation term and a growing noise term.

## 3. Fixed $\alpha$ while the grid is refined

```text
        alpha    n     model error   residual ||Km-d||   delta (noise)  residual / delta
        1e-01   20        0.094265            0.048101        0.003089           15.5726
        1e-01   40        0.094342            0.048694        0.003067           15.8778
        1e-01   80        0.095429            0.048495        0.003066           15.8144
        1e-01  160        0.095080            0.048565        0.003066           15.8381
        1e-03   20        0.018000            0.000694        0.003089            0.2248
        1e-03   40        0.027175            0.002031        0.003067            0.6624
        1e-03   80        0.020125            0.002783        0.003066            0.9075
        1e-03  160        0.011450            0.003036        0.003066            0.9901
```

**The strong regulariser, $\alpha = 10^{-1}$: bias-dominated.** The model error is
flat — 0.094265, 0.094342, 0.095429, 0.095080 — over an eightfold refinement of
the mesh, and the residual stays 15.8 times the noise level. Refining buys
essentially nothing, because the error is the *bias* of the regulariser and the
mesh cannot remove it. This is the regime in which "the answer is limited by the
regularisation, not by the discretisation" and it is the regime most inversions
should be in.

**The weak regulariser, $\alpha = 10^{-3}$: non-monotone, and over-fitting.** The
model error is 0.018000, 0.027175, 0.020125, 0.011450 — non-monotone in $n$ — and
the residual is **below the noise level at every grid**, rising from 0.22 to 0.99
of $\delta$. So:

- **A residual below the noise level is a warning, not an achievement.** The
  estimator is fitting noise, and the model error at $n = 40$ (0.027) is worse than
  at the coarse $n = 20$ (0.018) despite the finer mesh.
- **Non-monotonicity has a mechanism.** At $n = 20$ the discretisation *is* the
  regulariser: there are only 20 parameters and the condition number is 8.9
  (table above), so the problem is benign with almost no help from $\alpha$. The
  intermediate grids expose the ill-conditioned directions without yet resolving
  the answer, so the error rises; only at $n = 160$ does the resolved band catch up
  and the error fall below the coarse-grid value.
- **The honest reading is that refining a mesh without adjusting $\alpha$ is not a
  monotone improvement.** It can make the model worse.

## 4. A fixed $\alpha$ resolves a fixed number of degrees of freedom

The reason the error is flat in the bias-dominated case is that $\alpha$ selects a
band of *physical* wavenumbers, and the mesh only has to be fine enough to
represent that band:

```text
        alpha    n    trace(R_alpha)    of    lambda_1^2/alpha
        1e-01   20            8.5736    20                 8.2
        1e-01   40            7.9056    40                 8.1
        1e-01   80            7.7976    80                 8.1
        1e-01  160            7.7477   160                 8.1
        1e-03   20           19.4168    20               824.6
        1e-03   40           23.0671    40               810.4
        1e-03   80           22.6895    80               808.1
        1e-03  160           22.5605   160               807.0
```

For $\alpha = 10^{-1}$ the effective number of parameters converges to about 7.75;
for $\alpha = 10^{-3}$ it converges to about 22.6. It does **not** grow with the
mesh. The knee of the filter sits at $\sigma_k = \sqrt\alpha$ in *physical*
wavenumber, which the mesh does not change, so all the nodes beyond the resolved
band are damped to zero and contribute nothing.

This is the theoretical core of the lesson:

> **The discretisation determines what a regularised inversion *could* represent;
> the regularisation parameter determines what it *does* represent. Adding nodes
> does not add information.**

It also explains the two regimes of Section 3 in one sentence: with $\alpha$ fixed,
a refinement either does nothing (resolved band already covered) or admits noise
(resolved band not covered, and the extra nodes are at or below the noise).

### Physical interpretation

The convergence of $\operatorname{tr}R_\alpha$ to about 22.6, independent of the
mesh, is the statement that **the resolvable band is a physical band.** Its extent
is set by the depth of the source and by the noise level through
$\sigma_k \approx \sqrt\alpha$; the grid only has to be fine enough to sample that
band. Every additional node represents wavenumbers that the kernel attenuates
below the noise, and its coefficient is damped to zero — which is why a finer grid
gives a smoother-looking model at fixed $\alpha$ rather than a more detailed one,
and why refining a mesh without re-examining $\alpha$ can make the model worse
(Section 3). The same reasoning answers a question that arises in every field
programme: "would a denser survey help?" Only if the measurement geometry, not the
grid, is what limits the band — that is, only if it raises $\sigma_k$ at the
wavenumbers of interest.

## 5. Choosing $\alpha$ from the noise at each level

Now let $\alpha$ be chosen at each $n$ by the discrepancy principle, so that the
residual equals the noise norm:

```text
        n    alpha_disc      residual         delta     model error    trace(R)
       20     4.580e-03      0.003089      0.003089        0.016824      17.771
       40     3.224e-03      0.003067      0.003067        0.015865      19.115
       80     1.978e-03      0.003066      0.003066        0.014252      20.447
      160     1.158e-03      0.003066      0.003066        0.010524      22.079
```

The model error now **falls monotonically** — 0.016824, 0.015865, 0.014252,
0.010524 — and the residual sits exactly at the noise level at every grid. The
regularised solution converges. Two further observations:

- **$\alpha_{\text{disc}}$ falls with $n$** (4.58, 3.22, 1.98, 1.16 $\times
  10^{-3}$), because on a coarse grid the limited dimension of the model space
  already supplies part of the damping, as we saw at $n = 20$. As the grid is
  refined the discretisation supplies less and $\alpha$ must fall further to keep
  doing the job itself.
- **$\operatorname{tr}R_\alpha$ rises slowly** (17.77 to 22.08) even though the
  parameter count rises from 20 to 160: a factor of 8 more unknowns buys a 24 per
  cent increase in resolved parameters. That is the quantitative version of "the
  data carry a fixed amount of information".

## 6. Convergence theory and the regularisation discrepancy

### 6.1 The theorem, and its hypotheses

The convergence visible in Section 5 is not an accident of this example. The
classical result (Engl, Hanke & Neubauer, Theorem 5.2 for Tikhonov
regularisation), stated here without proof, is:

> Let $F$ be compact and injective with dense range, let the data be
> $d^\delta$ with $\lVert d^\delta - d\rVert \le \delta$, and let
> $\alpha = \alpha(\delta)$ satisfy
> $$\alpha(\delta)\to0 \quad\text{and}\quad \frac{\delta^2}{\alpha(\delta)}\to0
> \qquad\text{as } \delta\to0 .$$
> Then $m_{\alpha(\delta)}^\delta \to m^\dagger$, the minimum-norm solution of
> $Fm = d$.

The two conditions are the content: $\alpha$ must go to zero (so that the bias
disappears) but not too fast (so that the amplified noise does not take over). The
discrepancy principle satisfies both, which is the theoretical reason it performed
well in lesson 01-16-06. **Rates** of convergence need an additional *source
condition* — a statement about how well the truth lies in the range of
$F^{\mathsf T}F$ — and without one no rate can be claimed; with the standard
condition $\lVert m^\dagger\rVert$-type bounds give $O(\delta^{2/3})$ for
Tikhonov. Quoting a rate without a source condition is a common and real error.

### 6.2 The regularisation discrepancy

The theorem is about $\delta\to0$ at fixed continuous $F$. In practice one has a
discretisation, and the object of interest is:

> **The regularisation discrepancy** is the difference between the regularised
> solution of the discretised problem and the exact solution of the underlying
> continuous problem, for a *fixed* regularisation and a *finite* data error.

It is what remains when the theory's limits are not available. It has two parts
visible in the tables:

- **The bias floor.** With $\alpha$ fixed and $\delta$ fixed, the error saturates
  (Section 3, $\alpha = 10^{-1}$: 0.094 over all grids). No refinement removes it.
- **The noise floor.** With $\alpha$ chosen from $\delta$, the error falls but
  flattens: the observed sequence of Section 5 has last ratio
  $0.010524/0.014252 = 0.738$ for a *doubling* of $n$. A factor of 0.74 per
  doubling would reach a factor of 2 improvement only after three doublings, and
  the flattening continues. **With 1 per cent noise and this regulariser there is
  little left to gain from refining**, which is the practical content of the
  discrepancy.

The honest way to report this is a small table of $(\alpha, \text{residual},
\text{model error}, \operatorname{tr}R_\alpha)$ against $n$ — as Section 5 does —
rather than a single convergence order, because with a fixed $\delta$ there is no
order to report.

## 7. Iterative regularisation and semiconvergence

### 7.1 Landweber iteration

Applying the gradient step of lesson 01-16-03 to the least-squares misfit, starting
from $m_0 = 0$, gives the **Landweber** (or steepest-descent) iteration

$$m_{j+1} = m_j + \tau\,K^{\mathsf T}(d - Km_j) , \qquad
0 < \tau < 1/\lVert K\rVert^2 ,$$

whose solution in the eigenbasis is a spectral filter with factor
$f_k^{(j)} = 1 - (1-\tau\lambda_k)^j$: a low-pass filter whose cutoff *moves* as $j$
grows. **The iteration index is the regularisation parameter.** The demonstration
carries it out on the coefficients (algebraically identical, and $O(n)$ rather than
$O(n^2)$ per step):

```text
        n           tau  iterations     error at k*        k*    error at j=4000
       40     6.170e-01        4000        0.008901       100          0.050276
       80     6.187e-01        4000        0.006756       200          0.038424
      160     6.195e-01        4000        0.003914       200          0.023247
```

with the full history for $n = 80$ and $n = 160$:

```text
   n= 80: j=1: 0.2712, j=5: 0.1304, j=10: 0.0762, j=25: 0.0318, j=50: 0.0159,
          j=100: 0.0076, j=200: 0.0068, j=400: 0.0102, j=800: 0.0157,
          j=1600: 0.0236, j=2400: 0.0295, j=4000: 0.0384
   n=160: j=1: 0.2710, j=5: 0.1302, j=10: 0.0757, j=25: 0.0307, j=50: 0.0146,
          j=100: 0.0061, j=200: 0.0039, j=400: 0.0056, j=800: 0.0085,
          j=1600: 0.0129, j=2400: 0.0167, j=4000: 0.0232
```

### 7.2 Reading the table

- **The error falls, reaches a minimum, and then rises.** For $n = 80$ it falls
  from 0.2712 at $j = 1$ to 0.006756 at $j \approx 200$ and then rises to 0.038424
  at $j = 4000$ — a factor of 5.7 worse than the minimum. That is
  **semiconvergence**: the iteration first recovers the well-determined modes
  (converging fast, because they have large $\lambda_k$) and then starts to fit the
  noise in the poorly determined ones (converging slowly). Stopping at the right
  index is a regularisation whose parameter is $j$.
- **The optimal index grows with the discretisation.** $k^\ast = 100$ at $n = 40$
  and 200 at $n = 80$ and $n = 160$ (on the sampled grid; the true optimum moves
  later as $n$ grows because the finer grid exposes smaller singular values that
  take longer to converge). So an iteration count tuned on a coarse grid is
  **wrong** on a fine one, in the unsafe direction: too many iterations.
- **The minimum error improves with $n$**, from 0.008901 at $n = 40$ to 0.003914 at
  $n = 160$: the finer grid offers a better achievable model, provided the
  iteration is stopped at the right point.
- **Stopping "when the residual is small enough" destroys the property.** The
  residual is monotonically decreasing in $j$ and is *smallest* at $j=4000$ — the
  worst model. Early stopping must be based on an estimate of the noise level (the
  discrepancy principle for iterations) or on an independent validation set, never
  on the misfit alone.

### 7.3 Relation to Krylov methods and Tikhonov

Conjugate gradients on the normal equations is a Krylov method that implements an
optimal polynomial filter rather than Landweber's geometric one; it reaches the
same kind of minimum in far fewer iterations, and it too must be stopped early
(its iteration count is the regularisation parameter). LSQR and CGLS are the
standard implementations in geophysics. **Tikhonov damping and early stopping are
two dialects of the same idea** — a spectral filter — and their parameters trade
off against each other: running a damped iteration for many steps and stopping an
undamped one early can give nearly the same model, which is why a reported model
should always be accompanied by *both* the number of iterations and the damping
used, if either was.

## 8. Assumptions and regime of validity

1. **The data noise model is fixed.** All three tables assume independent Gaussian
   noise at a fixed relative level. Correlated noise invalidates the discrepancy
   principle and changes the optimal $\alpha$ and the optimal stopping index.
2. **$\delta$ must be known for Section 5.** If it is estimated, the "convergence"
   of the model error is convergence to whatever the estimate implies; an
   underestimate of $\delta$ produces under-regularisation at every grid, which
   looks like a convergence failure.
3. **The inverse crime.** Section 1.1. Real data do not lie in the range of the
   discretised operator, so a genuine refinement study also shows the existence
   floor of lesson 01-16-05 and the model errors are larger.
4. **The convergence theorem needs a source condition for any rate.** Without one,
   only convergence, not a rate, can be claimed.
5. **"Convergence" is in the norm used.** All errors here are weighted $L^2$ on the
   model grid. Pointwise or $L^\infty$ convergence is a different and stronger
   statement, and does not follow.
6. **Semiconvergence requires a starting model and a noise level.** Starting from a
   good prior (a reference model rather than zero) changes both the optimal index
   and the achievable error, as does the choice of $\tau$.
7. **The discretisation is itself a regulariser.** The $n = 20$ result of Section 3
   is stable because of its small dimension. This is a real effect, exploited
   deliberately in coarse-parameterisation geophysics, and it is also the reason a
   coarse grid can hide an ill-posed problem.

## 9. Common mistakes

- **Reporting a convergence order for a regularised inversion with fixed $\delta$.**
  There is no order to report: the error saturates at a bias floor and then at a
  noise floor.
- **Choosing $\alpha$ on a coarse grid and using it on a fine one.** The resolved
  band is a property of $\alpha$ and the physics, so this is usually *safe* in the
  bias-dominated regime and *unsafe* if $\alpha$ was tuned to the coarse grid's
  small dimension.
- **Stopping an iterative inversion when the misfit stops improving.** Chapter and
  verse of Section 7.2: the misfit is smallest at the worst model.
- **Refining the mesh to improve accuracy without re-examining the regularisation.**
  Section 3, $\alpha = 10^{-3}$: the error got worse.
- **Reading a low residual as a good model.** Residual below $\delta$ means
  over-fitting; the diagnostic is the pair (residual, model norm) and, if
  available, the model error against a synthetic truth.
- **Forgetting that an inverse crime was committed.** Comparing two inversion codes
  on data generated by one of them measures the difference of the codes, not the
  accuracy of either.
- **Assuming the theory's convergence implies practical convergence.** The theorem
  needs $\delta\to0$; at fixed $\delta$ the discrepancy flattens, as measured.

## 10. Real-world applications

- **Grid design for inversion.** The resolved band is set by $\alpha$ and the
  physics, so a model grid finer than the resolved band adds parameters without
  adding information — and, at fixed $\alpha$, adds variance. Production inversions
  often use a coarse parameterisation for exactly this reason.
- **Tomographic resolution studies.** Checkerboard and spike tests are refinement
  experiments: they measure the achievable model error as a function of the model
  grid, and their reported resolution is a discretisation-dependent statement.
- **Full-waveform inversion workflows.** Frequency continuation is a form of
  iterative regularisation with the frequency band as the parameter; the
  semiconvergence phenomenon is the reason FWI can diverge if run to convergence on
  noisy high frequencies.
- **Palaeoclimate and geothermal inversion.** A fixed smoothness $\alpha$ gives a
  bias floor; the reported "resolution of the last N years" is a statement about
  $\alpha$, not about the data alone.
- **Machine-learning inversion.** Early stopping of a training run is the same
  semiconvergence phenomenon, with the iteration count as the implicit regulariser;
  validation-based stopping is the analogue of the discrepancy principle.
- **Benchmarking inversion codes.** Any comparison must avoid an inverse crime;
  the standard practice of generating synthetic data with an independent (finer or
  analytic) forward model exists precisely because of Section 1.1.

## 11. Python demonstration

`code/discretization_convergence.py` performs, in order:

1. the singular spectra and condition numbers for $n = 20, 40, 80, 160$, with the
   inverse-crime caveat printed alongside;
2. the fixed-$\alpha$ refinement table for $\alpha = 10^{-1}$ and $10^{-3}$, with
   the residual-to-noise ratio;
3. the effective-parameter-count table showing that $\operatorname{tr}R_\alpha$
   converges rather than growing with $n$;
4. the discrepancy-principle table with $\alpha$ chosen at each $n$, and the
   observed error sequence and its flattening;
5. the Landweber iteration at $n = 40, 80, 160$, with the error history showing
   semiconvergence, the optimal stopping index, and the error at $j = 4000$.

It uses the standard library only and runs in about nine seconds, most of it in the
Jacobi eigensolver for the $160\times160$ matrix.

> **Breaking exercise.** Before running Section 5, predict what happens to the
> model-error sequence if the noise level is reduced by a factor of ten while
> everything else is unchanged. Then change `delta_rel` in the program and report
> the new sequence, the new $\alpha_{\text{disc}}$ values, and whether the
> flattening in $n$ persists. A flattening that persists at a *lower* error level
> is the regularisation discrepancy; a flattening that moves to a finer grid is
> merely a noise floor.

## 12. Further reading

- **Engl, H. W., Hanke, M., & Neubauer, A. (1996). *Regularization of Inverse
  Problems*. Kluwer.** Level: doctoral. The convergence theorem of Section 6.1,
  source conditions and rates, and the discrepancy principle as a theorem.
- **Hansen, P. C. (2010). *Discrete Inverse Problems: Insight and Algorithms*.
  SIAM.** Level: graduate. Discrete semiconvergence, stopping rules, and the
  practical behaviour of iterative methods.
- **Vogel, C. R. (2002). *Computational Methods for Inverse Problems*. SIAM.**
  Level: graduate. Iterative regularisation in detail: Landweber, CGLS, stopping
  rules, and the analysis of their filter factors.
- **Hansen, P. C. (1998). *Rank-Deficient and Discrete Ill-Posed Problems:
  Numerical Aspects of Linear Inversion*. SIAM.** Level: doctoral. The
  discretisation of ill-posed problems, generalised SVD, and the pitfalls of
  refinement.
- **Kaipio, J., & Somersalo, E. (2005). *Statistical and Computational Inverse
  Problems*. Springer.** Level: graduate. The Bayesian counterpart, including the
  treatment of discretisation as a modelling error and the notion of an
  approximation error.
- **Aster, R. C., Borchers, B., & Thurber, C. H. (2018). *Parameter Estimation
  and Inverse Problems* (3rd ed.). Academic Press.** Level: graduate. Resolution,
  parameter choice and iterative methods in geophysical practice.
- **Hanke, M. (1995). *Conjugate Gradient Type Methods for Ill-Posed Problems*.
  Longman.** Level: doctoral. Krylov methods as regularisation, with stopping
  rules.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 13. Exercises

Solutions are in
[`exercises/07-discretization-convergence-solutions.md`](./exercises/07-discretization-convergence-solutions.md),
and the problems are in
[`exercises/07-discretization-convergence-exercises.md`](./exercises/07-discretization-convergence-exercises.md).

**★1.** Name the three errors of a regularised inversion and state how each
behaves as the mesh is refined. Which one does not shrink?

**★2.** From the condition-number table of Section 1.1, compute the ratio of
$\lambda_{\min}$ between consecutive grids and state the empirical growth rate of
the condition number in $n$.

**★★3.** Using the fixed-$\alpha$ table, compute the ratio of the $\alpha = 10^{-1}$
model errors at $n = 20$ and $n = 160$ and the same ratio for $\alpha = 10^{-3}$.
Explain the difference.

**★★4.** Explain, using the $\operatorname{tr}R_\alpha$ table, why the number of
resolved parameters converges but the residual does not.

**★★5.** Verify the discrepancy-principle table: for $n = 40$, show by bisection on
$\log\alpha$ (a few steps by hand, then a program) that
$\alpha = 3.224\times10^{-3}$ makes the residual equal $\delta$.

**★★6.** State the two conditions on $\alpha(\delta)$ in the convergence theorem and
explain what fails if each is violated.

---

**★★★7.** Reproduce the Landweber iteration at $n = 80$ and, for
$j = 25, 50, 100, 200, 400$, report the error, the residual and the filter factor
of the mode whose $\lambda_k$ is closest to $1/j$. Show that the effective cutoff
moves like $1/j$ and use this to predict the optimal $j$ from the noise level.

**★★★8.** Redo the refinement study with the inverse crime removed: synthesise the
data on the $n = 320$ grid, invert on $n = 20, 40, 80, 160$. Report the model-error
sequence at fixed $\alpha = 10^{-3}$ and with the discrepancy principle, and compare
with the crime-committing results. State whether the existence floor of lesson
01-16-05 appears as a plateau.

**★★★9.** For this kernel on $[0,1]$ the singular values are well approximated by
$\sigma_k \approx e^{-\pi z k}$, because the $k$-th singular function has about
$k/2$ cycles per unit length and the Fourier multiplier is
$e^{-2\pi z f}$.

(a) Using the filter knee $\sigma_k = \sqrt\alpha$, derive the resolved index
$k^\ast(\alpha) = \ln(1/\alpha)/(2\pi z)$ and evaluate it for
$\alpha = 10^{-1}, 10^{-3}, 10^{-8}$ and $z = 0.05$.
(b) Compare each with the measured $\operatorname{tr}R_\alpha$ from the lesson's
table ($7.75$, $22.56$, $60.24$) and report the ratio.
(c) Hence show that the resolved index (and the resolved physical wavenumber) is
*independent of the mesh*, while the retained fraction of the Nyquist band falls
like $h$. Explain why no polynomial scaling $\alpha_n \propto h^p$ can make the
resolved band scale like the Nyquist wavenumber.

## 14. Self-assessment checklist

- [ ] I can name the three errors and state which one does not shrink with the mesh.
- [ ] I can explain why a fixed $\alpha$ resolves an asymptotically fixed number of
      degrees of freedom.
- [ ] I can describe and explain the non-monotone model error at fixed weak
      $\alpha$.
- [ ] I can recognise a residual below the noise level as over-fitting.
- [ ] I can choose $\alpha$ by the discrepancy principle at each grid and show that
      the resulting sequence converges.
- [ ] I can state the conditions on $\alpha(\delta)$ for convergence and explain the
      role of a source condition for rates.
- [ ] I can demonstrate semiconvergence, identify the optimal stopping index, and
      explain why it grows with the discretisation.
- [ ] I can state the inverse-crime caveat and what it changes.

## Related lessons

- [01-16-06 Tikhonov Regularisation and the L-Curve](./06-regularization-theory.md)
  — the filter and the parameter-choice rules refined here.
- [01-16-05 Ill-Posedness in the Sense of Hadamard](./05-ill-posedness.md) — the
  condition-number growth and the existence floor that re-appear without the
  inverse crime.
- [01-16-03 Linear Operators, Adjoints and Compactness](./03-operators.md) — the
  gradient iteration whose semiconvergence is measured here.
- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](../12-numerical-methods/07-pde-discretisation.md)
  — the forward-problem version, where refinement *is* a monotone improvement.
- [01-14-04 Linear and Nonlinear Least Squares](../14-optimization/04-least-squares.md)
  — the least-squares problem the Landweber iteration solves.
- [01-07-08 Singular Value Decomposition and Rank Truncation](../07-linear-algebra/08-svd.md)
  — the discrete picture of the filters used throughout.
- [18-inverse-problems](../../18-inverse-problems/README.md) — parameter choice,
  resolution and reporting conventions in operational inversion.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — how
  discretisation decisions are made in production modelling and inversion codes.
