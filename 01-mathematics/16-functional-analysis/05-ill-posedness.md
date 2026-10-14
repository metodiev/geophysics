---
id: 01-16-05
title: "Ill-Posedness in the Sense of Hadamard"
level: graduate
prereqs: ["01-16-03", "01-09-07"]
estimated_minutes: 90
tags: [ill-posedness, hadamard, inverse-problems, stability, potential-fields]
---

# Ill-Posedness in the Sense of Hadamard

## Learning objectives

By the end of this lesson you will be able to:

1. **State** Hadamard's three conditions — existence, uniqueness, stability —
   precisely, and explain why a problem that fails any of them is ill posed.
2. **Diagnose** which of the three fails in a given geophysical inverse problem,
   and say why the diagnosis matters: each failure has a different remedy and
   only one of them is repaired by regularisation.
3. **Show** that failure of existence is a property of the continuous operator
   (whose range is not closed) and that a discretisation hides it behind a
   ringing solution of enormous norm.
4. **Construct** near-null-space models explicitly from the small singular values
   of a gravity-like kernel and compute how large a model perturbation can be
   before it becomes visible at a stated noise level.
5. **Measure** the noise amplification of an unregularised inversion, relate it to
   the reciprocal of the smallest resolvable singular value, and show that
   truncation converts an unstable problem into a biased but stable one.
6. **Explain** the observational version of ill-posedness — the depth–wavenumber
   trade-off in potential fields and electromagnetics — in terms of the singular
   spectrum.
7. **Quantify** how the condition number of the discretised problem behaves as
   the discretisation is refined, and state what that implies for any claim of
   resolution.

## Prerequisites

- [01-16-03 Linear Operators, Adjoints and Compactness](./03-operators.md) —
  compactness, the singular value expansion and the fact that a compact operator
  has no bounded inverse.
- [01-09-07 Boundary and Initial-Boundary Value Problems](../09-partial-differential-equations/07-boundary-value-problems.md)
  — well-posedness for forward problems, and the backward-heat example of failure.
- [01-07-04 Rank, Null Space and Solvability](../07-linear-algebra/04-rank-and-nullspace.md)
  — the finite-dimensional null space and the rank conditions for solvability.

## 1. Hadamard's conditions

A problem is **well posed** (Hadamard, 1902) if its solution

1. **exists** for every admissible datum;
2. is **unique**;
3. depends **continuously** on the data.

The third condition is the one that is often forgotten and the one that damages
geophysics most, so it is worth stating quantitatively: there must exist a
function $\omega$ with $\omega(\delta)\to0$ as $\delta\to0$ such that

$$\lVert d_1 - d_2\rVert \le \delta
\ \Longrightarrow\
\lVert m_1 - m_2\rVert \le \omega(\delta) .$$

If no such $\omega$ exists, then arbitrarily small data errors can produce
arbitrarily large model errors, and no measurement precision will ever be enough.

| Condition | Fails when | Geophysics | Remedy |
|---|---|---|---|
| Existence | the datum is outside the range of $F$ | a shallow, thin source whose response the kernel cannot produce | change the parameterisation or the physics; accept a misfit |
| Uniqueness | $\dim\ker F > 0$ | the null space of potential-field inversion; two density distributions with the same external field | prior information, and therefore regularisation |
| Stability | $F^{-1}$ unbounded | every first-kind Fredholm problem: gravity, magnetics, EM | damping or truncation of the small singular values |

The table is the whole lesson in three lines. **Conflating the three is the most
common error in the applied literature**, because "ill posed" is often used as a
synonym for "needs regularisation", and regularisation addresses uniqueness and
stability but never existence.

## 2. The operator, and why its spectrum is the diagnosis

Take the surface gravity profile of a line mass at depth $z$,

$$d(x) = \int_0^1 K(x-y)m(y)\,dy, \qquad
K(s) = \frac{z}{\pi}\frac{1}{s^2+z^2} , \qquad z = 0.05, \tag{1}$$

with $m$ a density contrast and the units absorbed into the constant. $K$ is a
probability density, so a constant model produces a constant datum of the same
value — a useful sanity check on any implementation. Its Fourier transform is
$\hat K(f) = e^{-2\pi z\lvert f\rvert}$, which is the entire physical content of
the problem: **the operator multiplies the $f$-th wavenumber by a factor that
decays exponentially in the depth.** Everything below follows from that.

Discretised on $n = 80$ nodes with trapezoid weights, $K$ is a symmetric Toeplitz
matrix, so its singular values are the absolute values of its eigenvalues (a
point developed in lesson 01-16-03). The demonstration reports

```text
    sigma_1 = 0.898952, sigma_80 = 8.264e-06
    condition number sigma_1 / sigma_80 = 1.088e+05
    its reciprocal, 9.19e-06, is far above the double-precision
    unit round-off of 2.2e-16, so the condition number is a genuine
    property of the matrix and not a round-off artefact
```

with the normalised spectrum

```text
       k   sigma_k / sigma_1   k   sigma_k / sigma_1
       1          1.0000e+00   9          3.0158e-01
       2          8.6053e-01  10          2.5934e-01
       4          6.3904e-01  12          1.9176e-01
       8          3.5057e-01  16          1.0472e-01
```

The decay is slow in the low indices and then steep. **The condition number of
$1.09\times10^5$ is meaningful**: it is well above the precision limit, so an
unregularised inversion of this 80-parameter problem loses about five digits of
the model. That is the good case, and it already costs half the double-precision
digits.

### 2.1 Refining the discretisation destroys the conditioning

The continuous operator is compact; the matrix is not. The bridge is the
refinement:

```text
        n   sigma_min / sigma_1    condition number    resolvable modes
       40             4.912e-03           2.036e+02                  40
       80             9.193e-06           1.088e+05                  80
      160             3.211e-11           3.115e+10                 160
```

Adding nodes adds model parameters and reduces $\sigma_{\min}$ without bound:
$4.9\times10^{-3}$, $9.2\times10^{-6}$, $3.2\times10^{-11}$ for $n = 40, 80, 160$.
The condition number grows by roughly a factor of 500 and then 300 000 per
doubling. So:

- **Ill-posedness is a property that appears in the limit.** Every finite
  discretisation is technically well posed, which is why one can always obtain a
  "solution" by solving a linear system — and why that solution can be meaningless.
- **Refining a mesh does not add information.** It adds parameters whose singular
  values are below the noise, and therefore adds variance to the estimate. Lesson
  01-16-07 measures this directly.
- **A condition number can always be made to look acceptable** by choosing a
  coarse enough grid. Reporting one without the discretisation is uninformative.

## 3. Failure of existence

### 3.1 The measurable residual floor

If the datum lies outside the range of $K$, no model fits it exactly. In the
discrete problem one must retain a truncated set of singular modes for the
statement to be testable, because a square full-rank system can always be solved.
The demonstration fits a 0.012-wide Gaussian datum — a source shallower than the
kernel can image — with increasing numbers of retained modes:

```text
     rank used   attainable: rel. residual   unattainable: rel. residual
             8                   9.056e-03                      0.833498
            16                   9.526e-05                      0.649715
            32                   1.531e-06                      0.321427
            48                   2.760e-08                      0.116843
```

For the *attainable* datum (the response of a genuine 0.10-wide Gaussian model)
the residual falls to round-off as modes are added. For the unattainable one it
**stalls**: 0.83, 0.65, 0.32, 0.12 and then a floor. The residual is the part of
the datum outside the range of the operator, and no model removes it.

### 3.2 What the full-rank solution looks like

Push the discretisation to full rank and the residual does go to zero — at a
price:

```text
               datum   rel. residual    ||m|| (weighted)     max |m|
          attainable       1.842e-15           4.210e-01   9.987e-01
        unattainable       4.102e-13           1.739e+02   6.493e+02
    ||m_true|| (weighted) = 0.421005
```

The model that fits the unattainable datum exactly has norm 173.9 against a true
model norm of 0.42 — a factor of 413 — and a peak value of 649. That is the
classical **ringing solution**: a wildly oscillating, physically absurd model made
of the small-singular-value modes, which is what an exact fit to a datum outside
the range must look like.

**Why existence fails in the continuous problem.** The range of a compact
operator is not closed. It is dense in a sense — one can approximate any datum
arbitrarily well — but the limit of the approximating models is not in the model
space. So in the continuum there is genuinely no solution, while in every
discretisation there is one, and the two statements are reconciled by noting that
the discrete solution does not converge as $n\to\infty$: the model norm blows up.

**The remedy is not regularisation.** Damping the ring makes the answer finite
and useless. What fixes a failure of existence is changing the question: a
shallower layer in the parameterisation, a different kernel (a different physical
assumption about the source depth), or an explicit acceptance of the misfit floor
with a statement of what it implies. Regularisation will happily return a smooth
model that fits an unattainable datum to whatever level you ask, and the residual
will tell you the truth if you look at it.

## 4. Failure of uniqueness

### 4.1 The null space is physical

Two different models give the same data if their difference is in $\ker K$. For
the gravity kernel the null space is infinite-dimensional in the continuum and
large but not exact in a discretisation. The physical statement is the
depth–wavenumber trade-off: a shallow, thin, large-amplitude body and a deep,
thick, small-amplitude one can produce the same surface field, so the inversion
cannot choose between them without additional information.

### 4.2 Quantifying invisibility

The demonstration evaluates $m_k(x) = \sin(2\pi k x)$ and compares the measured
amplification with the prediction $e^{-2\pi z k}$ from the Fourier transform of
the kernel:

```text
       k     ||K m_k|| / ||m_k||    exp(-2 pi z k)    measured / predicted
       1            7.614611e-01      7.304027e-01                1.042522
       2            5.641750e-01      5.334881e-01                1.057521
       4            3.114734e-01      2.846095e-01                1.094388
       8            1.026001e-01      8.100259e-02                1.266628
      12            4.337767e-02      2.305411e-02                1.881559
```

The agreement is within 4–9 per cent for the low wavenumbers and degrades towards
the Nyquist wavenumber $1/(2h) = 39.5$, as it must: at very high wavenumber the
discrete kernel aliases and the continuum prediction no longer applies. The
physics is confirmed — **the amplification of wavenumber $k$ falls like
$e^{-2\pi zk}$** — and the practical consequence is that the ratio between the
largest and smallest models that fit the data at a given noise level grows
exponentially with wavenumber.

### 4.3 The computable near-null vectors

The abstract statement becomes a number when the perturbation is built from the
singular functions. The demonstration takes perturbations of weighted norm 0.3
(against $\lVert m_{\text{true}}\rVert = 0.421$) along $v_k$ and reports the
resulting relative change in the data, compared with a 1 per cent noise level:

```text
      mode k   sigma_k/sigma_1   data change / ||d||   as a multiple of 1% noise
           4         6.390e-01             5.220e-01                   5.220e+01
           8         3.506e-01             2.864e-01                   2.864e+01
          16         1.047e-01             8.554e-02                   8.554e+00
          32         9.212e-03             7.525e-03                   7.525e-01
          48         7.952e-04             6.495e-04                   6.495e-02
          64         6.689e-05             5.464e-05                   5.464e-03
```

with $\lVert K m_{\text{true}}\rVert = 0.330152$. Reading the last column, which is
the ratio of the data change to the noise:

- Modes 4 and 8 change the data by 52 and 29 times the noise: **well determined**.
- Mode 32 changes it by 0.75 of the noise: **marginal**.
- Modes 48 and 64 change it by 0.065 and 0.0055 of the noise:
  **undetectable in principle**.

So a model perturbation of 71 per cent of the true model norm can be invisible:
the boundary between the determined and the undetermined is not a property of the
data or of the model but of the *ratio* of the two, and it moves with the noise
level. This is what makes the null space of a real inversion a matter of degree
rather than a binary property, and it is why a regulariser — which encodes
information that is not in the data — is not optional. **Any model reported from
such data is one member of an equivalence class, and the honest report describes
the class.**

## 5. Failure of stability

### 5.1 The measurement

Add Gaussian noise at relative level $\varepsilon$ to the exact datum and invert
at full rank (the unregularised least-squares solution):

```text
       noise level eps    ||Km-d||/||d||   rel. model error, full rank   amplification
                 1e-04             1e-04                     2.352e+00       2.352e+04
                 1e-05             1e-05                     3.362e-01       3.362e+04
                 1e-06             1e-06                     3.197e-02       3.197e+04
```

The amplification is roughly constant at $2.4\times10^4$ to $3.4\times10^4$,
comparable with the reciprocal of the smallest singular value ratio,
$1/(\sigma_{80}/\sigma_1) = 1.088\times10^5$. It is smaller than that reciprocal
by about a factor of four because random noise does not align with the last
singular vector; a noise vector that did align would be amplified by the full
$1.09\times10^5$. Note the practical horror in the first row: **0.01 per cent of
noise in the data produces a model error of 235 per cent.** The model is not a
slightly noisy version of the truth; it is not the truth at all.

The scaling is linear in $\varepsilon$ — $2.352$, $0.336$, $0.032$ for
$\varepsilon = 10^{-4}, 10^{-5}, 10^{-6}$ — which is the discrete face of an
unbounded inverse: the amplification constant is finite at fixed $n$ but grows
without bound as $n$ grows (Section 2.1). No measurement precision is sufficient,
because the constant is not bounded in the limit.

### 5.2 The remedy, and its price

Truncating the singular expansion at a rank $r$ (the crudest regularisation)
replaces the amplification with a bias:

```text
       noise level eps    rank      rel. model error   amplification
                 1e-04      12             2.383e-03       2.383e+01
                 1e-04      20             8.529e-04       8.529e+00
                 1e-05      12             2.380e-03       2.380e+02
                 1e-05      20             8.092e-04       8.092e+01
                 1e-05      28             3.671e-04       3.671e+01
                 1e-06      12             2.380e-03       2.380e+03
                 1e-06      20             8.085e-04       8.085e+02
                 1e-06      28             3.558e-04       3.558e+02
```

Three readings, each of which generalises beyond truncation:

- **The error is no longer proportional to the noise, once the noise is small.**
  At rank 12 the error is $2.38\times10^{-3}$ for all three noise levels: that
  plateau is the *bias* of discarding modes 13–80, and it does not shrink with
  better data.
- **The optimal rank depends on the noise level.** At $\varepsilon = 10^{-4}$ the
  best of the three is rank 20; at $10^{-6}$ it is rank 28. More noise demands a
  smaller rank.
- **The amplification column is now bounded** — 8 to 41 — because the truncated
  inverse has all its retained singular values above a threshold. This is what
  "stabilising an ill-posed problem" means operationally.

The bias–variance trade-off visible here is derived and quantified in lesson
01-16-06, where the truncation is replaced by a smooth filter and the parameter is
chosen by the L-curve or the discrepancy principle.

## 6. Physical interpretation

The mathematics above has a physical summary that is worth stating on its own,
because it is how the subject is discussed in practice.

- **Potential fields cannot see depth and wavenumber independently.** The kernel
  multiplies wavenumber $k$ by $e^{-2\pi z k}$; a feature at depth $z$ is
  attenuated more the shorter its wavelength. The **depth–wavenumber trade-off**
  is therefore not a limitation of the algorithm but of the physics: no inversion
  can recover a high-wavenumber feature at depth from surface data at finite
  precision, because the sensitivity is exponentially small.
- **Electromagnetic and DC problems have the same structure with a different
  scale.** The skin depth $\delta = \sqrt{2/(\omega\mu\sigma)}$ plays the role that
  the source depth plays here: resolution in depth is controlled by the ratio of
  the target dimension to the skin depth, and the sensitivity kernels decay
  exponentially with depth divided by skin depth. Deep, thin, resistive targets
  are the unattainable data of Section 3.
- **Tomography is different, and the difference is instructive.** Travel-time
  inversion is well posed in the continuum for sufficiently complete ray coverage,
  and its sensitivity kernels do not decay exponentially. So "inverse problems are
  ill posed" is not a general truth: it is a statement about operators whose
  kernels are smooth, and it must be checked rather than assumed.
- **Downward continuation is the purest example.** Continuing a potential field
  towards the source multiplies wavenumber $k$ by $e^{+2\pi zk}$ — the exact
  inverse of (1) — and hence is unstable by construction. Any noise at all makes
  it diverge; the only meaningful version is band-limited, i.e. regularised.

## 7. Assumptions and regime of validity

1. **The kernel must be fixed and known.** All statements are conditional on (1).
   If the depth $z$ is itself unknown, the problem becomes nonlinear and the
   singular spectrum changes with the model; the diagnosis must then be made
   locally, about the current estimate.
2. **The noise model matters.** The amplification formula assumes independent
   noise. Correlated noise excites particular singular vectors and can be
   amplified far more than the average; whitening changes the answer.
3. **"Resolvable" depends on the noise level.** Section 4.3 defines the boundary
   explicitly. A statement like "the data resolve the top 20 parameters" is
   meaningless without the noise level it assumes.
4. **The discretisation bounds the condition number.** A quoted condition number
   is a property of the matrix, not of the operator, and grows without bound as
   the mesh is refined (Section 2.1).
5. **Existence failures are not repaired by damping.** They are repaired by
   changing the model space, the kernel, or the accepted misfit.
6. **A unique discrete solution is not evidence of a well-posed problem.** A
   square matrix with full numerical rank is invertible; the solution is still
   unstable and still not a property of the underlying physical problem.

## 8. Common mistakes

- **Using "ill posed" as a synonym for "needs regularisation".** Regularisation
  addresses the near-null space and the amplification; it cannot create
  information that a datum does not contain.
- **Diagnosing a problem from its condition number alone.** A large condition
  number implies instability only relative to a noise level; and a coarse
  discretisation can hide the true conditioning entirely.
- **Reporting a smooth model without its residual.** If the residual is at the
  noise level, the model is one representative of a large equivalence class. If it
  is below the noise level, the inversion is over-fitting.
- **Believing that a finer mesh resolves more.** It adds parameters with
  singular values below the noise and increases the variance of the estimate.
- **Forgetting that the null space is defined by the data type.** Adding a
  different measurement (a borehole constraint, a gravity gradient, a seismic
  travel time) shrinks the near-null space; no algorithm operating on the old data
  can.
- **Attributing an unstable result to a bug.** Divergence on refinement is the
  expected behaviour of an unregularised first-kind problem; a bug is not needed
  to explain it.

## 9. Real-world applications

- **Gravity and magnetic inversion.** The classical example: non-uniqueness is
  described in every textbook, and the depth–wavenumber trade-off determines what
  a survey can claim. Modern practice reports a regularised model with a residual
  and a resolution estimate.
- **Electromagnetic and magnetotelluric inversion.** The skin depth sets the
  depth–resolution relationship; deep conductive targets in resistive hosts are
  among the hardest problems, and the difficulty is exactly the exponential decay
  of Section 2.
- **Downward and upward continuation.** Upward continuation is stable smoothing;
  downward continuation is unstable and must be band-limited.
- **Seismic waveform inversion.** The null space is enormous at long periods; the
  low-wavenumber/long-wavelength ambiguity is the same structure at a different
  scale, and it is why FWI is run in a frequency cascade.
- **Palaeoclimate and geothermal inversion.** The surface temperature history is
  recovered from a borehole profile through a diffusive (Gaussian-like) kernel,
  whose singular values decay like a Gaussian; the recent past is recoverable and
  the distant past is not.
- **Reservoir history matching.** The near-null space contains combinations of
  permeabilities that produce identical production histories; regularisation
  expresses a geological prior about which combinations are plausible.
- **Experimental design.** Since the near-null space is a property of the
  operator, the way to reduce it is to change the experiment — different source
  depths, offsets or frequencies — not the algorithm.

## 10. Python demonstration

`code/ill_posedness.py` performs, in order:

1. the singular spectrum of the 80-node gravity kernel, the precision argument for
   its condition number, and the refinement table $n = 40, 80, 160$;
2. the residual floor for an unattainable datum at ranks 8–48, and the norm and
   peak of the full-rank ringing solution for attainable and unattainable data;
3. the oscillating-model amplification against the prediction $e^{-2\pi zk}$, and
   the near-null vectors built from the singular functions with the data change
   expressed as a multiple of the 1 per cent noise level;
4. the noise-amplification measurement at full rank for three noise levels, and
   the truncated inversions at ranks 12, 20 and 28 that stabilise it.

It uses the standard library only and runs in about nine seconds; most of that is
the Jacobi eigensolver on the $160\times160$ matrix.

> **Breaking exercise.** Before running Section 3, predict what happens to the
> residual floor if the unattainable datum is made *narrower* (say 0.006 wide
> instead of 0.012) and if it is made *wider* (0.05 wide). Then run both and
> explain the result in terms of which part of the datum lies in the range of the
> kernel: widening a feature lowers its wavenumber content, and low wavenumbers
> are exactly what the operator transmits.

## 11. Further reading

- **Hadamard, J. (1902). Sur les problèmes aux dérivées partielles et leur
  signification physique. *Princeton University Bulletin*, 13, 49–52.** Level:
  graduate. The original statement of the three conditions.
- **Tikhonov, A. N., & Arsenin, V. Y. (1977). *Solutions of Ill-Posed Problems*.
  Wiley.** Level: graduate. The classical theory of regularisation built as a
  response to Hadamard's third condition.
- **Engl, H. W., Hanke, M., & Neubauer, A. (1996). *Regularization of Inverse
  Problems*. Kluwer.** Level: doctoral. The rigorous treatment: compact operators,
  singular value expansions, spectral theory of regularisation, convergence
  rates.
- **Hansen, P. C. (2010). *Discrete Inverse Problems: Insight and Algorithms*.
  SIAM.** Level: graduate. The discrete diagnosis: the L-curve, generalised
  cross-validation, and the interpretation of the singular spectrum in floating
  point.
- **Menke, W. (2018). *Geophysical Data Analysis: Discrete Inverse Theory*
  (4th ed.). Academic Press.** Level: graduate. Null spaces, non-uniqueness and
  the practical treatment of both in geophysics.
- **Parker, R. L. (1994). *Geophysical Inverse Theory*. Princeton University
  Press.** Level: doctoral. The infinite-dimensional treatment with geophysical
  examples, including the potential-field depth–wavenumber trade-off.
- **Zhdanov, M. S. (2002). *Geophysical Inverse Theory and Regularization
  Problems*. Elsevier.** Level: graduate. Regularisation as practised in
  electromagnetic and potential-field geophysics.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 12. Exercises

Solutions are in
[`exercises/05-ill-posedness-solutions.md`](./exercises/05-ill-posedness-solutions.md),
and the problems are in
[`exercises/05-ill-posedness-exercises.md`](./exercises/05-ill-posedness-exercises.md).

**★1.** State Hadamard's three conditions. For each, give one geophysical
problem that fails it and the remedy that addresses that failure.

**★2.** Show that $K(s) = (z/\pi)/(s^2+z^2)$ is a probability density and that
its Fourier transform is $e^{-2\pi z\lvert f\rvert}$. Hence compute the
wavenumber at which the amplification has fallen to $10^{-3}$ for $z = 0.05$.

**★★3.** Using the refinement table of Section 2.1, compute the factor by which
the condition number grows per doubling of $n$ at each step and state the
empirical scaling with $h$.

**★★4.** For the unattainable datum of Section 3, explain why the residual stops
improving at rank 48 and continues to improve at full rank, and what distinguishes
the two regimes.

**★★5.** Using the amplification table of Section 4.2, compute the largest model
perturbation (in units of $\lVert m_{\text{true}}\rVert = 0.421$) that is invisible
at a 1 per cent noise level for each of the modes $k = 8, 16, 32, 48, 64$.

**★★6.** Reproduce the noise-amplification table of Section 5.1 and verify that
the amplification is roughly constant. Explain why it is smaller than
$1/(\sigma_{80}/\sigma_1)$ and what noise vector would achieve the full
amplification.

---

**★★★7.** Construct a datum that is exactly in the range of the 40-node kernel
and one that is not, and show numerically that the residual floor is a property of
the datum rather than of the algorithm, by reporting the floor for five different
out-of-range data.

**★★★8.** Truncation at rank $r$ was used as the crude regulariser. Implement a
smooth spectral filter $\lambda_k^2/(\lambda_k^2+\alpha)$ instead, choose $\alpha$
so that the residual matches the noise level, and compare the model error with the
best truncated result at the same noise level. Which does better, and why?

**★★★9.** Take the diffusive (borehole palaeoclimate) kernel
$K(s,t) \propto \exp(-s^2/(4\kappa t))$ with a plausible $\kappa = 10^{-6}$
m²/s and a 3 km borehole, and compute the singular values of the discretised
operator. Report the effective number of resolvable time steps for a 0.05 K noise
level, and compare the depth–wavenumber trade-off here with that of the gravity
kernel.

## 13. Self-assessment checklist

- [ ] I can state the three Hadamard conditions and identify which one is
      addressed by regularisation and which is not.
- [ ] I can explain why a compact operator has an unbounded inverse and a
      non-closed range, and what each failure costs.
- [ ] I can compute the residual floor of an out-of-range datum and interpret it.
- [ ] I can construct near-null models from the small singular values and compute
      the model perturbation that a stated noise level can hide.
- [ ] I can measure the noise amplification of an unregularised inversion and
      relate it to the reciprocal of the smallest resolvable singular value.
- [ ] I can explain how truncation converts instability into bias with a
      quantified plateau.
- [ ] I can explain the depth–wavenumber trade-off physically and connect it to
      the skin depth in electromagnetic sounding.
- [ ] I can say why refining a discretisation does not add resolution.

## Related lessons

- [01-16-03 Linear Operators, Adjoints and Compactness](./03-operators.md) — the
  compactness that guarantees the failures diagnosed here.
- [01-16-04 Spectral Theory of Operators and Eigenfunction Bases](./04-spectral-theory.md)
  — the singular spectrum and the resolution matrix used throughout.
- [01-09-07 Boundary and Initial-Boundary Value Problems](../09-partial-differential-equations/07-boundary-value-problems.md)
  — well-posedness for forward problems, and the backward-heat example.
- [01-07-04 Rank, Null Space and Solvability](../07-linear-algebra/04-rank-and-nullspace.md)
  — the finite-dimensional version of the uniqueness failure.
- [01-16-06 Tikhonov Regularisation and the L-Curve](./06-regularization-theory.md)
  — the systematic remedy for the near-null space and the amplification.
- [01-16-07 Discretisation, Convergence and Regularisation Discrepancy](./07-discretization-convergence.md)
  — what happens to the regularised solution as the discretisation is refined.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the same
  taxonomy in operational language, with covariance and Bayesian variants.
