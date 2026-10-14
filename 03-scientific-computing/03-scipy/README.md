# Module 03-03 — SciPy for Scientific Computing

**Stages:** intermediate → advanced · **Prerequisites:**
[03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
for the array model that every SciPy routine consumes and returns,
[03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
for how a subpackage is imported and called, and
[01-05-05 Integration](../../01-mathematics/05-single-variable-calculus/05-integration.md)
for what a quadrature rule is approximating.

NumPy gives you arrays. SciPy gives you the algorithms that operate on them:
quadrature, ODE solvers, optimisers, interpolants, filter design, sparse
linear algebra, image processing on grids, special functions and
distributions. This module is organised the way SciPy itself is organised —
subpackage by subpackage — and for each one it answers a single question
first: **which geophysical task is this routine for?**

The module has three habits that distinguish it from a function reference:

- **Every routine is verified against something independent.** A quadrature
  is checked against an analytic integral; a spline against the function that
  generated its nodes; a filter's group delay against a cross-correlation; a
  sparse solve against a closed-form solution of a Poisson problem; a
  distribution fit against the distribution that generated the sample. Each
  lesson quotes the measured agreement, and each demo prints the residuals it
  reports.
- **Every routine's assumptions are stated where it is used.** Smoothness for
  a spline, stationarity for Welch, causality for a filter, positive
  definiteness for Cholesky, validity of a p-value when parameters are
  estimated from the same data. Almost every silent wrong answer in this
  module traces back to an assumption that was never checked.
- **Numbers in the lessons are the demo output.** The `code/` scripts use
  only synthetic data generated in the script from stated parameters, and the
  lessons quote the actual printed values. Nothing is copied from
  documentation, and no dataset is downloaded.

Two facts about the module's structure matter for reading it. First, the
lessons are ordered by *subpackage*, not by difficulty of the geophysics; a
reader who needs only the filter material can start at
[lesson 05](./05-signal.md) and read backwards when a term is unfamiliar.
Second, `scipy.linalg` and `numpy.linalg` overlap, `scipy.interpolate` and
`numpy.interp` overlap, and `scipy.fft` and `numpy.fft` overlap. Lesson
[01](./01-scipy-overview.md) measures those overlaps and gives the rule for
choosing between them.

## Learning objectives

By the end of this module you will be able to:

1. Name the SciPy subpackage that solves a given task, state why the
   overlapping NumPy routine may be the better choice, and explain what SciPy's
   lazy subpackage loading implies for a script's start-up cost.
2. Integrate a function by adaptive quadrature until the residual is at the
   level the problem needs, handle an improper integral and an integrand with
   known structure, solve an initial-value problem with `solve_ivp`, verify
   the numerical answer against a closed form, and decide when a stiff solver
   is required.
3. Fit a non-linear model with `curve_fit`, turn the covariance matrix into
   honest 1σ errors, identify a degenerate parameter pair from the correlation
   matrix, and explain what an analytic Jacobian buys.
4. Choose between linear, cubic, PCHIP and smoothing interpolants for a well
   log; interpolate a two-dimensional velocity field on a regular grid; and
   state what happens — quantitatively — when a query leaves the data.
5. Design and verify a Butterworth filter, apply it causally and with zero
   phase, measure the group delay it introduces, and explain from measured
   evidence why a zero-phase filter cannot run in real time.
6. Choose a window function from its measured mainlobe width and sidelobe
   level, and read a spectrogram knowing its time–frequency trade.
7. Assemble a finite-difference Laplacian in sparse form, quantify the memory
   it saves against dense, solve a sparse linear system, and explain what
   fill-in does to the factorisation.
8. Apply `ndimage` filters to a potential-field grid, separate the noise error
   from the discretisation error in a numerical derivative, and use
   `scipy.linalg` knowing the cost of forming normal equations.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md) | intermediate | Eight subpackages, one dispatch question, and where SciPy and NumPy overlap without disagreeing |
| 02 | [scipy.integrate: Quadrature and ODE Integration](./02-integrate.md) | intermediate | Adaptive quadrature for the gravity anomaly of an arbitrary body; `solve_ivp` for decay and cooling, verified against the exponential |
| 03 | [scipy.optimize: Root Finding, Minimisation and Curve Fitting](./03-optimize.md) | intermediate | `curve_fit` with honest error bars, root finding for an equation of state, and what a Jacobian is worth |
| 04 | [scipy.interpolate: Splines, Griddata and RegularGrid](./04-interpolate.md) | intermediate | Well logs and velocity fields, the cost of overshoot, and the measured failure of extrapolation |
| 05 | [scipy.signal: Filters, Windows and Spectral Estimation](./05-signal.md) | advanced | Butterworth design, causal against zero-phase, windows and sidelobes, and the causality test that decides real-time use |
| 06 | [scipy.sparse: Storage Formats and Sparse Solvers](./06-sparse.md) | advanced | The five-point Laplacian, the memory it saves, the fill-in it costs, and a Poisson solve with a measured convergence order |
| 07 | [scipy.ndimage and scipy.linalg for Field Data](./07-ndimage-linalg.md) | advanced | Smoothing a potential-field grid, the bias–variance optimum in a derivative, and Cholesky against QR |
| 08 | [scipy.special and scipy.stats in Practice](./08-special-stats.md) | advanced | `erfc` in the diffusion solution, `erfcx` where `erfc` underflows, and a magnitude fit with a calibrated goodness-of-fit test |

## Suggested path

**If you are working through the computing folder in order:** all eight
lessons in numeric order. Lessons 01–04 are the backbone of everyday
geophysical scripting; lessons 05–08 are the ones that appear when a dataset
gets large, a grid gets dense or a statistic has to be defended.

**If you are here for potential-field work:** read
[02](./02-integrate.md) §3 (the gravity anomaly of an arbitrary body by
quadrature), [04](./04-interpolate.md) §4 (gridding scattered stations) and
[07](./07-ndimage-linalg.md) in full (smoothing, derivatives and the boundary
term). Then [07-gravity-geodesy](../../07-gravity-geodesy/README.md).

**If you are here for seismology or signal processing:** read
[05](./05-signal.md) in full, [02](./02-integrate.md) §4 (stiff ODE
integration) and [06](./06-sparse.md) §5 (why an implicit solver is a sparse
solve). Then
[20-signal-processing](../../20-signal-processing/README.md) and
[06-seismology](../../06-seismology/README.md).

**If you are here for inverse problems or statistics:** read
[03](./03-optimize.md) (fitting penalties and Jacobians),
[07](./07-ndimage-linalg.md) §5 (the squared condition number of normal
equations), [06](./06-sparse.md) §5 (large sparse systems) and
[08](./08-special-stats.md) §3–§4 (distributions, calibrated tests and
p-values that scale with n). Then
[18-inverse-problems](../../18-inverse-problems/README.md) and
[21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md).

**If you already know SciPy:** attempt ★★★ problems in
[02](./02-integrate.md), [05](./05-signal.md) and [06](./06-sparse.md) first.
Those three carry the module's verification load, and if they close cleanly
the rest is reference material.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-scipy-overview.md`](./01-scipy-overview.md) … [`08-special-stats.md`](./08-special-stats.md) | The eight lessons |
| [`code/scipy_overview_demo.py`](./code/scipy_overview_demo.py) | Subpackage inventory; one self-checking task per subpackage; the NumPy overlaps measured; `scipy.constants` provenance |
| [`code/integrate_demo.py`](./code/integrate_demo.py) | Quadrature accuracy; the gravity anomaly of an arbitrary polygon and of a sphere; `solve_ivp` decay chain and stiff-solver comparison |
| [`code/optimize_demo.py`](./code/optimize_demo.py) | `curve_fit` with covariance; Birch–Murnaghan inversion; `leastsq` versus `minimize` with and without a Jacobian |
| [`code/interpolate_demo.py`](./code/interpolate_demo.py) | Five interpolants on a synthetic log; `RegularGridInterpolator`; extrapolation; `griddata` outside the hull |
| [`code/signal_demo.py`](./code/signal_demo.py) | Synthetic seismogram; Butterworth design and group delay; windows and scalloping loss; spectrogram and Parseval; the truncation test for causality |
| [`code/sparse_demo.py`](./code/sparse_demo.py) | 1-D and 2-D Laplacians; memory counts; Poisson convergence order; factorisation fill-in; CG iteration count |
| [`code/ndimage_linalg_demo.py`](./code/ndimage_linalg_demo.py) | Smoothing and median filtering; the derivative bias–variance table; `map_coordinates`; Cholesky versus QR |
| [`code/special_stats_demo.py`](./code/special_stats_demo.py) | `erfc`/`ndtr`/`erfcx`; Gutenberg–Richter MLE against cumulative least squares; calibrated KS test; lognormal against normal |
| [`exercises/`](./exercises) | Exercises and full worked solutions for every lesson |

Every demo runs on the repository virtual environment and requires only
SciPy, NumPy and a Python 3 interpreter:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/signal_demo.py
```

No demo downloads data, and none quotes a wall-clock time: timings are
machine-dependent, so where performance matters the demos count function
evaluations, non-zeros or iterations instead.

## Related modules

- [03-02-numpy](../02-numpy/README.md) — the array model that everything here
  consumes.
- [03-01-python-fundamentals](../01-python-fundamentals/README.md) — modules,
  exceptions and the import system that SciPy's laziness relies on.
- [03-04-pandas](../04-pandas/README.md) — tabular data, which starts where
  array programming stops being convenient.
- [03-05-plotting-and-visualisation](../05-plotting-and-visualisation/README.md)
  — for turning the grids and traces of lessons 05 and 07 into figures.
- [01-12-numerical-methods](../../01-mathematics/12-numerical-methods/README.md)
  — the theory behind these routines, derived rather than called.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  what to do when the sparse matrix of lesson 06 no longer fits.

## Self-assessment checklist

- [ ] I can name the subpackage for a given task without searching.
      (§Lesson 01)
- [ ] I can explain what `import scipy` alone does and does not do. (§01)
- [ ] I can verify a numerical integral against a closed form and report the
      residual. (§02)
- [ ] I can pass `points=` to `quad` when the integrand has local structure.
      (§02)
- [ ] I can choose between `RK45`, `BDF` and `Radau` from the problem, not
      from habit. (§02)
- [ ] I can turn a `curve_fit` covariance matrix into 1σ errors and read the
      correlation matrix for a degeneracy. (§03)
- [ ] I can explain why a root finder needs a bracket and what happens when it
      has none. (§03)
- [ ] I can choose an interpolant from its overshoot behaviour, not from its
      name. (§04)
- [ ] I can state the measured error of extrapolating 10% beyond my data.
      (§04)
- [ ] I can design a filter to a specification and verify the specification.
      (§05)
- [ ] I can measure the group delay my filter introduces and say whether it
      matters. (§05)
- [ ] I can explain, from the truncation test, why `filtfilt` cannot run in
      real time. (§05)
- [ ] I can build a 2-D Laplacian sparsely and say how much memory it saves.
      (§06)
- [ ] I can state what fill-in is and why the factor is not as sparse as the
      matrix. (§06)
- [ ] I can separate the noise error from the discretisation error in a
      numerical derivative. (§07)
- [ ] I can say why `cond(A^T A) = cond(A)^2` matters, in digits. (§07)
- [ ] I can pick the right member of the `erf` family for the argument range.
      (§08)
- [ ] I can quote a goodness-of-fit p-value that accounts for estimated
      parameters. (§08)
