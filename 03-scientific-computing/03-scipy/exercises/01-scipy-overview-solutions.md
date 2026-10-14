# Solutions — 03-03-01 SciPy Organisation and When to Use Which Subpackage

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output, produced with SciPy 1.18.1, NumPy 2.5.4 and
> Python 3.14.4 on the repository virtual environment.

---

## ★1 — Dispatch

| Task | Subpackage | NumPy alternative? |
|---|---|---|
| (a) integrate $4/(1+x^2)$ | `scipy.integrate.quad` | no adaptive quadrature |
| (b) zero of $\cos x - x$ | `scipy.optimize.brentq` | no |
| (c) fit $Ae^{-t/\tau}+c$ | `scipy.optimize.curve_fit` | `numpy.polyfit` only for polynomials |
| (d) 40 Hz low-pass | `scipy.signal.butter` + `sosfilt`/`sosfiltfilt` | no |
| (e) five-point Laplacian | `scipy.sparse` (`diags`, `kron`) | no |
| (f) $\mathrm{erfc}(2.5)$ | `scipy.special.erfc` | `math.erfc` for a scalar only |
| (g) one-sided PSD | `scipy.signal.welch` | no (a raw periodogram only) |
| (h) $G$ with uncertainty | `scipy.constants` | no |

Note the pattern: NumPy supplies array mechanics and a few dense linear-algebra
routines; everything algorithmic is SciPy. The two places where NumPy offers a
genuine alternative are linear algebra (`numpy.linalg`) and the FFT, and
interpolation (`numpy.interp`) for the linear case.

---

## ★2 — Reading the smoke-test table

**(a)** $\int_0^\infty e^{-x^2}dx = \tfrac12\sqrt\pi = 0.8862269254527579$.
The quoted `0.886226925453` rounds correctly at twelve decimals, and the
residual column reports `0.00e+00`, so the agreement is at the level of the
printing precision — better than $5\times10^{-13}$.

**(b)** `brentq` terminates when the bracket is smaller than
$2\,|x|\,\mathrm{eps} + \mathrm{xtol}$, which for a root of size 0.74 is about
$3\times10^{-16}$. The reported $|f| = 7.88\times10^{-15}$ is consistent with
that: for a function with $|f'|$ of order 1 near the root, an argument error of
$10^{-15}$ gives a function value of $10^{-15}$, and the two differ by an order
of magnitude because $|f'|$ at the Dottie number is about $1+\sin x \approx 1.67$.

**(c)** For $A = \begin{pmatrix}4&1\\1&3\end{pmatrix}$,
$L_{11} = \sqrt{4} = 2$, $L_{21} = 2^{-1}\cdot 1 = 0.5$,
$L_{22} = \sqrt{3 - 0.5^2} = \sqrt{2.75} = 1.6583123951777$.
The table's `L11=2.000000000000` and `|LL^T-A|max=0.00e+00` are both correct.

**(d)** The peak of the two-dimensional Gaussian filter kernel with
$\sigma = 1$ pixel is $1/(2\pi) = 0.1591549430919$, so `0.159156` is that value
to six decimals. The `sum=1.000000000000` column verifies normalisation: a
smoothing kernel that does not sum to 1 changes the mean level of the data,
which would be a silent offset in every grid it was applied to. Normalisation
of the kernel and the residual of the Cholesky factor are the two properties
worth checking in any filter library.

---

## ★3 — Lazy loading

**(a)** SciPy imports each subpackage the first time it is accessed, rather
than at `import scipy`.

**(b)** `scipy.ndimage` would be in `sys.modules` immediately after the import
statement, and `scipy.integrate` would not: the probe would print
`False`/`True` for `ndimage` and, for `integrate`, `False` both before and
after any use of `ndimage`.

**(c)** `scipy.stats` resolves as an attribute lookup on the package object,
and the lookup triggers the import. The cost of the first call is the import of
`scipy.stats` (and its dependencies) plus the computation; subsequent calls
pay only the computation.

**(d)** A curve-fitting command-line tool pays for `scipy.optimize` and
nothing else, so its start-up time is not the sum of the whole stack. The
practical consequence is that adding `from scipy import signal` to a module
that only needs a solver is a real, measurable regression in start-up cost for
every invocation — and, more importantly, an undeclared dependency that a
reader cannot see.

---

## ★4 — Constants and provenance

**(a)** If $M_\oplus$ were exact, the relative uncertainty of $GM$ would equal
$G$'s: $2.25\times10^{-5}$.

**(b)** $2.25\times10^{-5} / 10^{-9} = 2.25\times10^{4}$, so the direct
determination is about 22 500 times better.

**(c)** The difference of $5.28\times10^{-6}$ is *smaller* than $G$'s own
relative uncertainty of $2.25\times10^{-5}$. A discrepancy smaller than the
uncertainty of one of the inputs is consistent with both values being correct;
it reflects the precision to which the Earth's mass is quoted
($M_\oplus = 5.9722\times10^{24}$ kg is a nominal figure) rather than an error
in either constant.

**(d)** The uncertainty of $GM/G$ is dominated by the *worse* of the two
relative uncertainties, so it is $2.25\times10^{-5}$ — 22 500 times larger than
the claimed $10^{-9}$. Division by a poorly known constant cannot recover the
precision that the quotient was measured to; the reported uncertainty must be
at least as large as $G$'s contribution.

---

## ★5 — Choosing between the overlaps

**(a)** `CubicSpline`. Linear interpolation has a discontinuous first
derivative, so a derivative computed from it is a staircase; this is the
measured 67 m s⁻¹ against 18 m s⁻¹ in [lesson 04](../04-interpolate.md) §1.2.

**(b)** `cho_factor` then `cho_solve`. One factorisation serves all 500
right-hand sides; 500 dense solves would repeat the same $O(n^3)$ work.
[Lesson 07](../07-ndimage-linalg.md) §4.1 shows the first solution is
bit-identical to a fresh `spsolve`/`solve`.

**(c)** `scipy.fft.rfft` with `workers=-1`. The numbers agree to round-off
(demo: $2.8\times10^{-14}$), so the choice is made on the planner cache and
multithreading, which is exactly what 20 000 transforms need.

**(d)** `scipy.linalg.lstsq`. A degree-11 design matrix has a condition number
of $1.2\times10^{8}$ on 60 equispaced samples, so the normal matrix has
$1.4\times10^{16}$ and the Cholesky coefficients are wrong in the second digit
(lesson 07 §5.1). Form the normal equations only when the conditioning is
known to be benign, or when regularisation is what makes it so.

**(e)** `griddata`. The stations are irregular, so there is no tensor-product
grid to interpolate on; `RegularGridInterpolator` requires one.

---

## ★6 — A five-line smoke test

```python
import numpy as np
from scipy import signal, sparse, special, stats

print("erf      ", abs(special.erf(1.0) - 0.8427007929497148))     # ~0
print("norm.ppf ", abs(stats.norm.ppf(0.975) - 1.959963984540054)) # ~0
print("sparse   ", sparse.eye(10, format="csr").nnz - 10)          # 0 exactly
sos = signal.butter(4, 40.0, btype="low", fs=500.0, output="sos")
print("butter   ", abs(abs(signal.sosfreqz(sos, worN=[40.0], fs=500.0)[1])[0]
                      - 2 ** -0.5))                               # ~0
print("shape    ", sos.shape)                                      # (2, 6)
```

Each residual is a difference from an independently known value:
$\mathrm{erf}(1) = 0.8427007929497148$ is a tabulated constant,
$\Phi^{-1}(0.975) = 1.959963984540054$ is the normal quantile that makes a 95%
two-sided interval, the identity matrix has exactly one non-zero per row, and a
fourth-order Butterworth filter is *defined* to be $-3$ dB at its cut-off, so
$|H(f_c)| = 2^{-1/2}$ exactly. A passing run prints four numbers below
$10^{-15}$ and the shape `(2, 6)` — two second-order sections, each with three
numerator and three denominator coefficients.

The check detects a missing install (import error), a wrong build (large
residual), and a shadowed package: a file named `signal.py` in the working
directory would make `from scipy import signal` return your own module, and the
`sosfreqz` call would fail with an `AttributeError` that names the wrong
problem.

---

## ★7 — What agreement between the two libraries proves

**(a)** Both functions call the same LAPACK routine. The difference is not
algorithmic but consists of the different orderings of the same floating-point
operations: the two wrappers prepare arguments differently, so the last bit can
differ. A difference of $1.8\times10^{-18}$ on a solution of order 1 is
$10^{-17}$ relative, i.e. below the unit round-off of 1.1 × 10⁻¹⁶.

**(b)** The relative difference is $2.8\times10^{-14}/20 \approx 1.4\times
10^{-15}$, which is about ten times the unit round-off. An FFT of 1024 points
performs about $n\log_2 n \approx 10^4$ floating-point operations, and errors of
order $\epsilon$ accumulate; a factor of ten over one rounding is exactly the
expected growth.

**(c)** The check has no diagnostic power because both routines execute the
same code. If the result is wrong, it is wrong in both — the input is wrong, the
question is mis-posed, or the model is wrong. A useful check compares two
*different* methods (a quadrature against an analytic value, a spline against
the function that generated its nodes), which is the pattern used throughout
this module.

---

## ★8 — A methods-section critique

**(a)** $GM$ is the correct constant. A gravity anomaly is a *field* quantity:
the potential is $GM/r$ and the anomaly is its second derivative, so the only
mass-related parameter that enters is the product $GM$. Using $G$ and $M$
separately reintroduces the factor-22 500 uncertainty of (★4b) into a quantity
that does not need it.

**(b)** Converting a density to a mass requires $M = \rho V$ and then, if the
result is used in a potential, $GM$. The relative uncertainty contributed by
$G$ is $2.25\times10^{-5}$, i.e. 0.002%; the density and volume uncertainties
are almost certainly larger, but the constant's contribution is not negligible
and must be stated.

**(c)** Two sentences that would fix it: "The gravity field was computed with
the geodetic gravitational parameter $GM = 3.986\,004\,418\times10^{14}\
\mathrm{m^3\,s^{-2}}$, which is determined from satellite orbit dynamics to a
relative uncertainty of about $10^{-9}$." and "Where masses were required, they
were obtained as $M = GM/G$ with the CODATA value
$G = 6.67430(15)\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$, so all derived
masses carry a relative uncertainty of at least $2.25\times10^{-5}$."

**(d)** A 0.1 mGal anomaly is a relative perturbation of the background field
of order $10^{-6}$–$10^{-7}$ in the field's own units, and the $5.28\times10^{-6}$
difference in $GM$ propagates linearly into a field value, so it is comparable
to but below the measurement precision at the 0.1 mGal level for a typical
$9.8\ \mathrm{m\,s^{-2}}$ field ($10^{-6}$ relative is $0.1$ mGal, so this is
right at the boundary and worth stating). Orbit determination is a different
problem: the *time integral* of the field over many revolutions amplifies a
constant fractional error in $GM$, present-day orbital ranging reaches
$10^{-9}$–$10^{-10}$ relative, and a $5\times10^{-6}$ error in $GM$ would
produce an along-track drift many orders of magnitude above the noise.

---

## ★9 — An environment report module

The specification, line by line:

| Line | Verifies | Failure mode detected |
|---|---|---|
| Python version | the interpreter is the expected one | a system Python without the venv's packages |
| NumPy and SciPy versions | the stack matches the study's record | a silent upgrade that changes iteration counts |
| Five subpackage imports | each is installed and importable | a partial install, a shadowed module name |
| One residual per subpackage | each routine computes the right thing | single-precision BLAS, a broken compiled extension |
| Three constants with uncertainties | provenance is available | a stale CODATA table or a missing constants data file |

```python
"""Print a verifiable environment report for a geophysical script."""
import math
import platform

import numpy as np
import scipy
from scipy import constants, integrate, linalg, signal, sparse, stats


def main():
    print(f"python  {platform.python_version()}  ({platform.platform()})")
    print(f"numpy   {np.__version__}")
    print(f"scipy   {scipy.__version__}")

    val, err = integrate.quad(lambda x: math.exp(-x * x), 0.0, np.inf)
    print(f"integrate  residual {abs(val - 0.5 * math.sqrt(math.pi)):.2e}")

    a = np.array([[4.0, 1.0], [1.0, 3.0]])
    L = linalg.cholesky(a, lower=True)
    print(f"linalg     residual {np.abs(L @ L.T - a).max():.2e}")

    sos = signal.butter(4, 40.0, btype="low", fs=500.0, output="sos")
    h = abs(signal.sosfreqz(sos, worN=[40.0], fs=500.0)[1])[0]
    print(f"signal     residual {abs(h - 2 ** -0.5):.2e}")

    print(f"sparse     nnz(eye(10)) - 10 = {sparse.eye(10, format='csr').nnz - 10}")

    print(f"stats      residual {abs(stats.norm.ppf(0.975) - 1.959963984540054):.2e}")

    for name in ("Newtonian constant of gravitation",
                 "standard acceleration of gravity",
                 "Boltzmann constant"):
        value, unit, unc = constants.physical_constants[name]
        print(f"constants  {name}: {value:.6g} +/- {unc:.2g} {unit}")


if __name__ == "__main__":
    main()
```

**Why no timing.** A timing measurement reports a property of the machine, the
load and the caches, not of the installation. Two runs on the same machine
disagree by tens of per cent, so a timing threshold is not a reproducible test
and fails under a shared runner. A *residual* is reproducible to the last digit
on any compliant build, which is why every check above compares a computed
value against a known one, exactly as the demo's self-checking table does. Where
performance genuinely matters, count function evaluations, non-zeros or
iterations — all deterministic — as lessons 03, 06 and 07 do.
