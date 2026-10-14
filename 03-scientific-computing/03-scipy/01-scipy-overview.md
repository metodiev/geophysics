---
id: 03-03-01
title: "SciPy Organisation and When to Use Which Subpackage"
level: intermediate
prereqs: ["03-02-01", "03-01-04"]
estimated_minutes: 75
tags: [scipy, scientific-computing, libraries, workflow]
---

# SciPy Organisation and When to Use Which Subpackage

SciPy is not a program; it is about twenty programs wearing one name. Each of
its subpackages was written by different people for a different class of
problem, and the first skill this module teaches is **dispatch**: given a
task, knowing which subpackage owns it before you start typing. That skill
saves more time than any amount of reading documentation, because the wrong
subpackage usually produces a plausible answer rather than an error.

This lesson has four jobs:

1. Lay out the subpackage map and the geophysical task each one serves.
2. Show how SciPy loads itself, and what that implies for a script.
3. Measure the three places where SciPy and NumPy overlap, so that the choice
   between them is a decision rather than a habit.
4. Show `scipy.constants`, because a number without its provenance is not a
   measurement.

Everything below is printed by
[`code/scipy_overview_demo.py`](./code/scipy_overview_demo.py). Run it before
reading on:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/scipy_overview_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Map** a stated task to the SciPy subpackage that owns it, for the twelve
   subpackages used in this curriculum.
2. **Explain** SciPy's lazy subpackage loading and state its consequence for
   start-up cost and for what `import scipy` alone gives you.
3. **Choose** between `numpy.linalg` and `scipy.linalg`, between `numpy.interp`
   and `scipy.interpolate`, and between `numpy.fft` and `scipy.fft`, and give
   the criterion for each choice.
4. **Write** a smoke test that verifies an installed SciPy against closed-form
   values rather than against documentation.
5. **Trace** a physical constant to its uncertainty and explain why geodesy
   quotes $GM$ rather than $M$.

## Prerequisites

- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
  — SciPy speaks in arrays; every routine here takes and returns them.
- [03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
  — how `from scipy import integrate` resolves, and what a module attribute is.
- [02-05-01 Temperature, Heat, Internal Energy and Specific Heat](../../02-physics/05-thermodynamics/01-temperature-and-heat.md)
  — the physical quantities whose provenance §4 examines.

## 1. The subpackage map

SciPy is organised by **mathematical problem class**, not by application
domain. That is why a seismologist and an economic forecaster can both use
`scipy.signal` without either being the intended user. The map below is the
one this module follows; the geophysical task in the third column is the
reason each row exists in the curriculum.

| Subpackage | Problem class | Geophysical task |
|---|---|---|
| `scipy.integrate` | Definite integrals; initial-value problems | Gravity anomaly of an arbitrary body; cooling and decay |
| `scipy.optimize` | Roots, minima, curve fitting | Inverting an equation of state; fitting a decay curve |
| `scipy.interpolate` | Reconstruction between samples | Well logs; gridding scattered stations; 2-D velocity fields |
| `scipy.signal` | Filtering, windows, spectra | Seismogram conditioning; spectrograms; anticausal filtering |
| `scipy.sparse` | Matrices that are mostly zero | Finite-difference operators; large implicit solves |
| `scipy.sparse.linalg` | Iterative and direct sparse solves | Poisson problems; the inner loop of an implicit scheme |
| `scipy.ndimage` | Filters on regular grids | Smoothing potential fields; edge and derivative estimation |
| `scipy.linalg` | Dense linear algebra | Least-squares normal equations; Cholesky and QR |
| `scipy.special` | Named mathematical functions | `erfc` in diffusion solutions; Bessel and gamma functions |
| `scipy.stats` | Distributions and inference | Magnitude–frequency statistics; goodness-of-fit tests |
| `scipy.fft` | Fast Fourier transforms | Spectra of traces and grids; fast convolutions |
| `scipy.constants` | Physical constants with uncertainties | Putting a provenance on every number quoted |

Three more subpackages appear in the curriculum but not in this module:
`scipy.spatial` (neighbourhood queries on stations), `scipy.cluster`
and `scipy.interpolate`'s scattered-data triangulation routines. The pattern is
that a new problem usually maps to an existing subpackage, and a new
*subpackage* appears only when a new problem class does.

The demo runs one minimal, self-checking task through each subpackage. This
is the fastest way to confirm that an unfamiliar installation is the one you
think it is:

```
  subpackage   task                                 result                      check
  integrate    quad exp(-x^2) on [0, inf)           0.886226925453              |err|=0.00e+00
  optimize     brentq cos(x) = x                    0.739085133215              |f|=7.88e-15
  interpolate  CubicSpline sin(pi x), 7 nodes       0.917711474923              |err|=4.32e-05
  signal       butter(4, 40 Hz, fs=500)             |H(40Hz)|=0.707107          |H(100Hz)|=1.56e-02
  sparse       1-D Laplacian, N=100                 nnz=298                     dense would be 10000
  ndimage      gaussian_filter(delta, sigma=1)      sum=1.000000000000          peak=0.159156
  linalg       cholesky(4 1; 1 3)                   L11=2.000000000000          |LL^T-A|max=0.00e+00
  special      erfc(1)                              0.157299207050              math.erfc=0.157299207050
  stats        norm.cdf(1.96)                       0.975002                    0.97500 is the 97.5th percentile
  fft          rfft cos(2pi*16t), N=256             |X[16]|=128.000000          |X[15]|=9.32e-14
  constants    constants.G                          6.674300e-11                m3 kg-1 s-2
  spatial      KDTree query, k=2                    d=5.000000                  index=1
```

Read the last column, not the third. `quad` returns
$0.886226925453$ for $\int_0^\infty e^{-x^2}dx$, and the exact value is
$\tfrac12\sqrt{\pi}$, so the reported error is exactly zero at the printed
precision. `brentq` finds the root of $\cos x - x$ and reports
$|f| = 7.88\times10^{-15}$. `cholesky` returns a factor whose product
reproduces the input to $0$. `rfft` of a cosine at bin 16 puts
$128.000000$ in that bin and $9.32\times10^{-14}$ in the neighbouring one.
**Every one of those checks is a residual against a value that does not come
from SciPy.** A table of outputs with no residual column verifies nothing; a
mis-linked BLAS, a stale installation or a wrong-precision build all produce
plausible-looking numbers.

## 2. How SciPy loads itself

NumPy is one import statement and one shared library. SciPy is roughly twenty
subpackages, most of them wrapping compiled Fortran or C. Importing all of
them costs real time, so SciPy does not: **each subpackage is imported the
first time it is used.**

The demo measures this in a clean interpreter rather than asserting it, using
a subprocess so that its own imports cannot contaminate the answer:

```
  Lazy loading, measured in a clean interpreter (subprocess):
  after import scipy:  scipy.integrate in sys.modules -> False
  after using it:     scipy.integrate in sys.modules -> True
```

Three consequences follow, and all three change how you write code:

- **`import scipy` is close to free, and close to useless.** It binds a
  package object with lazily-evaluated attributes. Code that does
  `import scipy` and then calls `scipy.optimize.minimize` works, but the
  import on that line is where the cost is paid, not the top of the file.
- **Import the subpackage explicitly.** `from scipy import integrate` is the
  form that makes the dependency visible and that a reader can grep for. It
  is also the form that fails loudly and early if the installation is broken.
- **A script that needs one subpackage does not pay for the other nineteen.**
  A command-line tool that only fits a curve should not import
  `scipy.signal`, and it will not, unless something in its import graph does.

The version facts printed at the top of the demo — SciPy 1.18.1, NumPy 2.5.4,
Python 3.14.4 — are the versions this module's outputs were produced with.
SciPy's API is stable across minor versions but not across major ones, so a
residual that suddenly becomes $10^{-6}$ where it was $10^{-15}$ is usually a
version change rather than a mistake in your code. Quote versions in a
methods section for exactly this reason.

## 3. Where SciPy and NumPy overlap

Three pairs of routines do the same job. The demo measures all three, and
the result is that **the numbers agree and the features do not**:

```
  linear algebra   |np.linalg.solve - scipy.linalg.solve|max = 1.843e-18
                   residual |Ax-b|max (numpy) = 2.220e-16
  interpolation    np.interp vs interp1d(linear) max diff = 0.000e+00
                   linear error vs analytic = 2.173e-02
                   cubic  error vs analytic = 3.072e-03
  FFT              |np.fft.rfft - scipy.fft.rfft|max = 2.842e-14
```

### 3.1 Linear algebra

`numpy.linalg` is a thin wrapper over LAPACK, always available with NumPy, and
sufficient for `solve`, `inv`, `eig`, `svd` and `lstsq` on ordinary matrices.
`scipy.linalg` is the same LAPACK wrapped more completely and with more
control: it exposes the factorisations individually (`lu`, `cholesky`,
`qr`, `schur`, `ldl`), lets you declare the matrix class with
`assume_a='pos'` so the right routine is chosen without a pivoting search,
and adds the structured solvers (`solve_triangular`, `solveh_banded`,
`cho_solve`) that turn a factorisation into repeated cheap solves.

The measured difference between the two `solve` calls is $1.8\times10^{-18}$:
they are calling the same LAPACK. The rule is therefore about features, not
accuracy:

> Use `numpy.linalg` when it has the routine and you need nothing else. Use
> `scipy.linalg` when you need a factorisation rather than a solution, when
> the matrix has structure you want declared, or when you need the
> decomposition for a second purpose.

Lesson [07](./07-ndimage-linalg.md) makes this concrete: `cho_factor` followed
by two `cho_solve` calls replaces two `solve` calls, and the difference
between a Cholesky solve and a QR solve of the same normal equations is
measurable in digits.

### 3.2 Interpolation

`np.interp` does linear interpolation on one increasing 1-D axis, supports
no extrapolation control beyond a fill value, and is fast. `scipy.interpolate`
does linear interpolation with the same arithmetic — the demo reports a
maximum difference of exactly $0$ — and everything else as well: cubic
splines, shape-preserving PCHIP, Akima, smoothing splines, 2-D regular-grid
interpolation and triangulation-based interpolation of scattered data.

The second and third lines of the interpolation block are the ones worth
reading. Interpolating $\tanh(6(x-1/2))$ on 11 nodes, linear interpolation is
off by $2.2\times10^{-2}$ at the query points while the cubic spline is off by
$3.1\times10^{-3}$, a factor of seven. **When a routine offers a `kind` or
`method` argument, the default is chosen for robustness, not for accuracy.**
Lesson [04](./04-interpolate.md) quantifies exactly this trade.

### 3.3 The FFT

`numpy.fft` and `scipy.fft` agree to $2.8\times10^{-14}$ on the same input.
`scipy.fft` adds a planner cache and a `workers=` argument for multithreaded
transforms, `next_fast_len` for choosing a transform length with small prime
factors, and the DCT/DST families. Neither is more accurate. For a single
transform of a moderate array, `numpy.fft` is fine; for a loop over thousands
of transforms, `scipy.fft` with `workers=-1` is the routine you want, and the
speed-up is the only reason to change.

## 4. `scipy.constants`: provenance for a number you already quote

A physical constant in a paper without a source is a rumour. `scipy.constants`
carries the CODATA values *with their uncertainties*, which is what makes it
worth using in preference to a literal typed from memory:

```
  G (CODATA)                 = 6.674300e-11 m3 kg-1 s-2
  G relative uncertainty     = 2.25e-05
  g (standard gravity)       = 9.80665 m s-2  (defined, not measured)
  M_earth (nominal) times G  = 3.986025e+14 m3 s-2
  GM_earth (quoted, IERS)    = 3.986004e+14 m3 s-2
  relative difference        = 5.28e-06
```

The last two lines are the lesson. Multiplying the CODATA $G$ by a nominal
Earth mass gives a gravitational parameter that differs from the standard
geodetic value by $5.3\times10^{-6}$ — and $G$'s own relative uncertainty is
$2.25\times10^{-5}$, five times larger. **The product is limited by its worst
factor.** Satellite geodesy does not measure $G$ and $M$ and multiply; it
measures $GM$ directly from orbit dynamics, and therefore knows $GM$ far
better than the product $G\times M$ can ever be. That is why gravitational
parameters are quoted in $\mathrm{m^3\,s^{-2}}$ and never as a mass.

The `physical_constants` dictionary carries the uncertainty as a third
element, so traceability is one line of code:

```python
import scipy.constants as C
value, unit, uncertainty = C.physical_constants["Newtonian constant of gravitation"]
```

`g = 9.80665` is marked "defined, not measured" because it is: it is the
1971 standard gravity, fixed by convention so that instruments can be
calibrated against it. A measured gravity value is always a *relative*
quantity, which is why gravimeters report mGal differences rather than
absolute accelerations.

## Worked code

The whole of §3 in three lines each, so that the criterion is testable:

```python
import numpy as np
from scipy import fft, interpolate, linalg

a = np.array([[4.0, 1.0], [1.0, 3.0]])
b = np.array([1.0, 2.0])

x_np = np.linalg.solve(a, b)          # fine: numpy has the routine
x_sp = linalg.solve(a, b, assume_a="pos")   # declares structure, skips pivoting
L = linalg.cholesky(a, lower=True)          # numpy.linalg not imported
x_chol = linalg.cho_solve((L, True), b)     # second solve is nearly free

xs = np.linspace(0.0, 1.0, 11)
ys = np.tanh(6.0 * (xs - 0.5))
q = np.array([0.123, 0.456, 0.789])
lin = np.interp(q, xs, ys)                                  # numpy: linear only
cub = interpolate.CubicSpline(xs, ys)(q)                    # scipy: order 3

s = np.random.default_rng(0).normal(size=4096)
X_np = np.fft.rfft(s)                 # one transform: numpy is enough
X_sp = fft.rfft(s, workers=-1)        # many transforms: threads, and it shows
```

The three decisions are visible in the code: `assume_a="pos"` is a *claim*
about the matrix (see §6), `cho_solve` reuses a factorisation, and
`workers=-1` is a performance request rather than a correctness one.

## Physical interpretation

A dispatch table looks bureaucratic until you notice that each row encodes a
physical assumption. `scipy.integrate.quad` assumes the integrand is
*evaluable at arbitrary points* — an assumption a finite-difference gravity
model breaks, because it knows the field only on its grid. `scipy.interpolate`
assumes the field between samples is *smooth in the way its basis is smooth* —
an assumption a well log crossing a 3 m bed violates. `scipy.fft` assumes
the record is *periodic* in the transform length, which is why
windowing exists. `scipy.sparse` assumes the *operator is local*, which is
true for a finite-difference Laplacian and false for a gravity kernel.

So the map is not a filing cabinet of functions; it is a list of assumptions
about the Earth. Choosing the subpackage is choosing which assumption you are
willing to make, and this module's later lessons measure the consequences of
getting that choice wrong.

## Assumptions and limits

- **Lazy loading is an implementation detail, not a contract.** Do not write
  code whose correctness depends on `scipy.signal` *not* being imported.
- **Version stability.** This module's numbers come from SciPy 1.18.1, NumPy
  2.5.4 and Python 3.14.4. Minor-version changes can alter iteration counts
  and, occasionally, defaults; a residual that moves by orders of magnitude
  after an upgrade is expected and should be re-measured, not assumed.
- **`scipy.constants` is CODATA-based.** CODATA adjusts constants as
  measurements improve, so a constant retrieved in 2030 will differ in its
  last digits from the value printed here.
- **`assume_a='pos'` is a promise.** If the matrix is not positive definite,
  LAPACK may return a solution without an error. The promise must be checked
  once (`cholesky` raises when it fails) before it is assumed thereafter.

## Python demonstration

The full demo is [`code/scipy_overview_demo.py`](./code/scipy_overview_demo.py).
The self-checking table in §1 is the part to rerun on any new machine: it
takes a fraction of a second and it distinguishes four different failures
that otherwise look identical — a missing install, a wrong NumPy, a
single-precision BLAS, and a package shadowed by a file of the same name in
the working directory. The last of these is worth knowing about, because
`scipy.py` in the current directory will be imported instead of SciPy and the
symptom is an `AttributeError` that mentions nothing about the real problem.

The measured overlaps in §3 come from the same script and are reproducible to
the last digit on a given platform; the last digits of the FFT and solve
differences depend on the BLAS, so treat $2.8\times10^{-14}$ as "round-off"
rather than as a constant.

## Common mistakes

- **`import scipy` then `scipy.integrate.quad(...)`.** Works, but hides the
  dependency from a reader and from a linter. Import the subpackage.
- **Calling `numpy.linalg.solve` and then `scipy.linalg.solve` on the same
  matrix "to check".** They call the same LAPACK; agreement proves only that
  both were installed.
- **Using `np.interp` when the physics needs a smooth derivative.** Linear
  interpolation has a discontinuous first derivative, and every derivative
  computed from it inherits a staircase. See [lesson 04](./04-interpolate.md).
- **Quoting a constant without its uncertainty.** $G$ is known to $2\times
  10^{-5}$; a result that depends on $G$ cannot be better than that, whatever
  the arithmetic does afterwards.
- **Assuming a subpackage is imported somewhere because it is used
  somewhere.** A script that works in a notebook can fail from a clean
  interpreter, because the notebook has already imported half the stack.

## Real-world applications

- **A processing script's structure.** Production geophysical scripts are
  built as thin command-line front ends over SciPy; knowing which subpackage
  does the work is what makes such a script editable by someone else.
- **Environmental packaging.** Shipping an application that links only
  `scipy.optimize` rather than all of SciPy reduces an interpreter image by
  hundreds of megabytes, and lazy loading is what makes that possible.
- **Reproducibility statements.** "Computed with SciPy 1.18.1, method `BDF`,
  `rtol=1e-8`" is a reproducible sentence; "computed with SciPy" is not.
- **Gravity and geodesy.** The $GM$-versus-$G\times M$ distinction is why
  every gravity model in the ICGEM archive is distributed as coefficients of
  a potential with $GM$ as the scale factor rather than as densities.

## Further reading

- **Virtanen, P., et al. "SciPy 1.0: fundamental algorithms for scientific
  computing in Python." *Nature Methods*, 2020.** The paper that describes the
  library's scope and its organisation subpackage by subpackage. Level:
  intermediate; read §1 and the subpackage list.
- **Harris, C. R., et al. "Array programming with NumPy." *Nature*, 2020.**
  The companion paper for the array model that SciPy consumes.
- **Oliphant, T. E. *A Guide to NumPy* (Trelgol Publishing, 2006).** Dated,
  but the chapters on how a scientific Python stack is layered remain the
  clearest statement of why SciPy is split the way it is. Level: beginner.
- **Heath, M. T. *Scientific Computing: An Introductory Survey* (2nd ed.,
  SIAM, 2018).** The taxonomy of numerical problems that SciPy's subpackage
  structure mirrors. Level: intermediate.
- **Golub, G. H., & Van Loan, C. F. *Matrix Computations* (4th ed., Johns
  Hopkins University Press, 2013).** What sits under `scipy.linalg`, and the
  reason `assume_a` is worth having. Level: advanced.
- **The SciPy project's own documentation at [scipy.org](https://scipy.org)**
  — the subpackage reference, and the only external URL this lesson relies on.

> Note on citations: bibliographic details are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text;
> confirm editions and availability through your library before citing them
> yourself.

## Related lessons

- [02 scipy.integrate: Quadrature and ODE Integration](./02-integrate.md) — the
  first subpackage in depth, with the verification pattern this lesson
  introduces.
- [03 scipy.optimize](./03-optimize.md) and
  [04 scipy.interpolate](./04-interpolate.md) — the two subpackages whose
  defaults most often surprise a new user.
- [05 scipy.signal](./05-signal.md) — where the assumptions listed under
  'Assumptions and limits' become measurable.
- [03-02-05 Linear Algebra with numpy.linalg](../02-numpy/05-linear-algebra-numpy.md)
  — the NumPy side of the overlap in §3.1.
- [03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
  — the import machinery that makes lazy loading possible.
- [03-04-pandas](../04-pandas/README.md) — the next module, and the point at
  which labelled data becomes worth the abstraction over arrays.

Exercises:
[`exercises/01-scipy-overview-exercises.md`](./exercises/01-scipy-overview-exercises.md)
and
[`exercises/01-scipy-overview-solutions.md`](./exercises/01-scipy-overview-solutions.md).

## Self-assessment checklist

- [ ] I can name the subpackage for each of the twelve tasks in §1 without
      looking at the table. (§1)
- [ ] I can explain what `import scipy` does and does not import. (§2)
- [ ] I can write a residual-based smoke test for an installed SciPy. (§1)
- [ ] I can state the criterion for choosing `scipy.linalg` over
      `numpy.linalg`. (§3.1)
- [ ] I can quantify what cubic interpolation buys over linear on 11 nodes.
      (§3.2)
- [ ] I can say which extra features `scipy.fft` adds, and that accuracy is
      not one of them. (§3.3)
- [ ] I can retrieve a constant with its uncertainty from
      `scipy.constants`. (§4)
- [ ] I can explain why geodesy quotes $GM$ and not $M$. (§4)
- [ ] I can list two assumptions encoded in the dispatch table of §1 and
      the assumptions list.
