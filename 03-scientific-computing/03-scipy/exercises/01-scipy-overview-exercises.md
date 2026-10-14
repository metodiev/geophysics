# Exercises — 03-03-01 SciPy Organisation and When to Use Which Subpackage

Attempt these **closed-book** before opening the
[solutions](./01-scipy-overview-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to
[`../code/scipy_overview_demo.py`](../code/scipy_overview_demo.py) require you
to run it and report its actual output. The command is

```
.venv/bin/python 03-scientific-computing/03-scipy/code/scipy_overview_demo.py
```

---

## ★ Foundational

**★1.** Name the SciPy subpackage that owns each task, and say whether
`numpy` also has a routine for it.

(a) Integrate $4/(1+x^2)$ from 0 to 1.
(b) Find the zero of $\cos x - x$.
(c) Fit $A e^{-t/\tau} + c$ to 25 measurements.
(d) Low-pass filter a 500 Hz seismogram at 40 Hz.
(e) Build the five-point Laplacian for a $200 \times 200$ grid.
(f) Evaluate $\mathrm{erfc}(2.5)$.
(g) Compute the one-sided power spectral density of a 60 s record.
(h) Return the CODATA value of the Newtonian constant of gravitation with
its uncertainty.

---

**★2.** The demo's self-checking table reports

```
  integrate    quad exp(-x^2) on [0, inf)           0.886226925453              |err|=0.00e+00
  optimize     brentq cos(x) = x                    0.739085133215              |f|=7.88e-15
  linalg       cholesky(4 1; 1 3)                   L11=2.000000000000          |LL^T-A|max=0.00e+00
  ndimage      gaussian_filter(delta, sigma=1)      sum=1.000000000000          peak=0.159156
```

(a) Compute the exact value of $\int_0^\infty e^{-x^2}dx$ and verify that the
quoted result is right to twelve decimals.
(b) Verify that $|f| = 7.88\times10^{-15}$ is what you would expect for a
bisection-type method whose interval width is at the level of machine epsilon
for a root of size 0.74.
(c) For the $2\times2$ matrix $\begin{pmatrix}4&1\\1&3\end{pmatrix}$, compute
the Cholesky factor by hand and check `L11`.
(d) The Gaussian filter's peak value is 0.159156. What is it exactly, and what
does the `sum=1.000000000000` column verify?

---

**★3.** In a clean interpreter the demo reports

```
  after import scipy:  scipy.integrate in sys.modules -> False
  after using it:     scipy.integrate in sys.modules -> True
```

(a) State in one sentence what SciPy does when a subpackage is first used.
(b) Predict the output of the same probe if the script began with
`from scipy import ndimage`.
(c) Explain why `import scipy` followed by `scipy.stats.norm.cdf(0)` works,
and what the cost of the first such call is.
(d) Give one practical consequence for a command-line tool that fits a curve.

---

## ★★ Applied

**★4.** The demo reports

```
  G (CODATA)                 = 6.674300e-11 m3 kg-1 s-2
  G relative uncertainty     = 2.25e-05
  GM_earth (quoted, IERS)    = 3.986004e+14 m3 s-2
  relative difference        = 5.28e-06
```

(a) If the Earth's mass were known exactly, what would be the relative
uncertainty of the product $G M_\oplus$?
(b) Satellite geodesy determines $GM_\oplus$ with a relative uncertainty of
about $10^{-9}$ (treat this as a stated premise). How many times better is that
than the product in (a)?
(c) Explain why the observed relative difference of $5.28\times10^{-6}$ is not
evidence that either value is wrong.
(d) A student reports the Earth's mass as $M = GM_\oplus/G$ with an uncertainty
of $10^{-9}$ relative. Identify the error in the uncertainty statement.

---

**★5.** For each pair, state which routine you would call and justify it in one
sentence.

(a) `numpy.interp` or `scipy.interpolate.CubicSpline` for a 221-sample
depth–velocity log from which you must compute a derivative.
(b) `numpy.linalg.solve` or `scipy.linalg.cho_factor` plus `cho_solve` for a
symmetric positive-definite system solved 500 times with 500 different
right-hand sides.
(c) `numpy.fft.rfft` or `scipy.fft.rfft` for 20 000 transforms of 4096-sample
windows.
(d) `scipy.linalg.lstsq` or forming `A.T @ A` and calling `cho_solve` for a
degree-11 polynomial fit.
(e) `scipy.interpolate.griddata` or `scipy.interpolate.RegularGridInterpolator`
for 60 gravity stations at irregular positions.

---

**★6.** Write a five-line smoke test for an installed SciPy that verifies
`scipy.special.erf`, `scipy.stats.norm.ppf`, `scipy.sparse.eye` and
`scipy.signal.butter`. Each check must compare against an independently known
value or an exact identity, and each must print a residual. State what each
residual would be if the check passed.

---

**★7.** The demo reports

```
  linear algebra   |np.linalg.solve - scipy.linalg.solve|max = 1.843e-18
  FFT              |np.fft.rfft - scipy.fft.rfft|max = 2.842e-14
```

(a) Explain why the difference between the two `solve` calls is at the level of
round-off rather than zero.
(b) The FFT difference is $2.8\times10^{-14}$ on a transform whose largest
component is about 20. What is the relative difference, and why is it not
$10^{-16}$?
(c) A colleague "checks" a suspicious result by calling both routines and
finding agreement. Explain why this check has no diagnostic power.

---

## ★★★ Research-oriented

**★8.** A published paper states: "The gravity field was computed using
$GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$ and $G = 6.674\times10^{-11}\
\mathrm{m^3\,kg^{-1}\,s^{-2}}$."

(a) Which of the two is the appropriate constant for computing a gravity
anomaly, and why?
(b) The paper also converts a density to a mass using $G$. State the relative
uncertainty introduced by that step, using the demo's figure for $G$.
(c) Write the two sentences that should have appeared in the methods section
instead.
(d) The demo measures a $5.28\times10^{-6}$ difference between $G M_\oplus$ and
the IERS value. Explain why this difference is *invisible* in a gravity anomaly
computed to 0.1 mGal but would dominate an orbit determination.

---

**★9.** Design a single Python module `geoenv.py` whose only job is to print a
verifiable environment report for a geophysical script: the versions of Python,
NumPy and SciPy; the presence and version of five subpackages; a residual for
one routine in each; and the values of three physical constants with their
uncertainties. Specify what each line verifies and what failure mode it
detects, then write the module. Do not use any timing measurement in the
report, and justify that omission.
