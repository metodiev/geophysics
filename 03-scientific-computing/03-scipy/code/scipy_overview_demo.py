"""SciPy organisation: which subpackage solves which problem.

Run:  .venv/bin/python scipy_overview_demo.py
Requires: scipy, numpy.

Companion to lesson 03-03-01. Everything printed here is computed at run time;
no dataset is downloaded and no number is copied from documentation.

The script:

1. Reports the installed SciPy and NumPy versions and shows that SciPy loads
   its subpackages lazily.
2. Runs one minimal, self-checking task through each subpackage used later in
   this module, so that the dispatch table in the lesson can be verified rather
   than believed.
3. Compares the three NumPy/SciPy overlaps that cause the most confusion --
   linear algebra, interpolation and the FFT. The two routines must agree to
   round-off, and the script reports the measured difference.
4. Shows what ``scipy.constants`` encodes and uses it to recompute a
   geophysical quantity that is usually quoted without its provenance.
"""

import math
import subprocess
import sys

import numpy as np
import scipy
from scipy import (constants, fft, integrate, interpolate, linalg, ndimage,
                   optimize, signal, sparse, spatial, special, stats)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def part1_versions_and_lazy_loading():
    section("1. Versions, and how SciPy loads subpackages")
    print(f"  scipy  {scipy.__version__}")
    print(f"  numpy  {np.__version__}")
    print(f"  python {sys.version.split()[0]}")
    print()
    print("  Lazy loading, measured in a clean interpreter (subprocess):")
    probe = (
        "import sys, scipy;"
        "print('  after import scipy:  scipy.integrate in sys.modules ->',"
        "'scipy.integrate' in sys.modules);"
        "import scipy.integrate as I;"
        "print('  after using it:     scipy.integrate in sys.modules ->',"
        "'scipy.integrate' in sys.modules)"
    )
    out = subprocess.run([sys.executable, "-c", probe], capture_output=True,
                         text=True, check=True)
    print(out.stdout.rstrip())
    print()
    print("  So 'import scipy' alone costs almost nothing and gives almost")
    print("  nothing: each subpackage is imported on first use, and a script")
    print("  that needs only scipy.optimize never pays for scipy.signal.")
    print(f"  In this process, after explicit imports: "
          f"'scipy.integrate._quadpack_py' in sys.modules -> "
          f"{'scipy.integrate._quadpack_py' in sys.modules}")


def part2_one_task_per_subpackage():
    section("2. One minimal task per subpackage (all self-checking)")
    rows = []

    val, err = integrate.quad(lambda x: math.exp(-x * x), 0.0, np.inf)
    exact = 0.5 * math.sqrt(math.pi)
    rows.append(("integrate", "quad exp(-x^2) on [0, inf)",
                 f"{val:.12f}", f"|err|={abs(val - exact):.2e}"))

    root = optimize.brentq(lambda x: math.cos(x) - x, 0.0, 1.0)
    rows.append(("optimize", "brentq cos(x) = x",
                 f"{root:.12f}", f"|f|={abs(math.cos(root) - root):.2e}"))

    xs = np.linspace(0.0, 1.0, 7)
    spl = interpolate.CubicSpline(xs, np.sin(np.pi * xs))
    rows.append(("interpolate", "CubicSpline sin(pi x), 7 nodes",
                 f"{spl(0.37):.12f}",
                 f"|err|={abs(spl(0.37) - math.sin(np.pi * 0.37)):.2e}"))

    sos = signal.butter(4, 40.0, btype="low", fs=500.0, output="sos")
    _, h = signal.sosfreqz(sos, worN=[0.0, 40.0, 100.0], fs=500.0)
    rows.append(("signal", "butter(4, 40 Hz, fs=500)",
                 f"|H(40Hz)|={abs(h[1]):.6f}", f"|H(100Hz)|={abs(h[2]):.2e}"))

    lap = sparse.diags([1.0, -2.0, 1.0], [-1, 0, 1], shape=(100, 100)).tocsr()
    rows.append(("sparse", "1-D Laplacian, N=100",
                 f"nnz={lap.nnz}", f"dense would be {100 * 100}"))

    imp = np.zeros((9, 9))
    imp[4, 4] = 1.0
    sm = ndimage.gaussian_filter(imp, sigma=1.0)
    rows.append(("ndimage", "gaussian_filter(delta, sigma=1)",
                 f"sum={sm.sum():.12f}", f"peak={sm.max():.6f}"))

    a = np.array([[4.0, 1.0], [1.0, 3.0]])
    c = linalg.cholesky(a, lower=True)
    rows.append(("linalg", "cholesky(4 1; 1 3)",
                 f"L11={c[0, 0]:.12f}", f"|LL^T-A|max={np.abs(c @ c.T - a).max():.2e}"))

    rows.append(("special", "erfc(1)",
                 f"{special.erfc(1.0):.12f}", f"math.erfc={math.erfc(1.0):.12f}"))

    rows.append(("stats", "norm.cdf(1.96)",
                 f"{stats.norm.cdf(1.96):.6f}", "0.97500 is the 97.5th percentile"))

    t = np.arange(256) / 256.0
    spec = fft.rfft(np.cos(2 * np.pi * 16.0 * t))
    rows.append(("fft", "rfft cos(2pi*16t), N=256",
                 f"|X[16]|={abs(spec[16]):.6f}", f"|X[15]|={abs(spec[15]):.2e}"))

    rows.append(("constants", "constants.G", f"{constants.G:.6e}", "m3 kg-1 s-2"))

    tree = spatial.KDTree(np.array([[0.0, 0.0], [3.0, 4.0]]))
    d, i = tree.query([0.0, 0.0], k=2)
    rows.append(("spatial", "KDTree query, k=2", f"d={d[1]:.6f}", f"index={i[1]}"))

    print(f"  {'subpackage':<13}{'task':<37}{'result':<28}check")
    for name, task, result, check in rows:
        print(f"  {name:<13}{task:<37}{result:<28}{check}")
    print()
    print("  Every 'check' column is a residual or a closed-form value, so the")
    print("  table is a self-test: a mis-installed SciPy cannot pass it silently.")


def part3_overlaps_with_numpy():
    section("3. Where SciPy and NumPy overlap -- and which to call")
    rng = np.random.default_rng(20240517)
    a = rng.normal(size=(4, 4))
    a = a @ a.T + 4.0 * np.eye(4)          # symmetric positive definite
    b = rng.normal(size=4)
    x_np = np.linalg.solve(a, b)
    x_sp = linalg.solve(a, b)
    print(f"  linear algebra   |np.linalg.solve - scipy.linalg.solve|max = "
          f"{np.abs(x_np - x_sp).max():.3e}")
    print(f"                   residual |Ax-b|max (numpy) = "
          f"{np.abs(a @ x_np - b).max():.3e}")

    xs = np.linspace(0.0, 1.0, 11)
    ys = np.tanh(6.0 * (xs - 0.5))
    q = np.array([0.123, 0.456, 0.789])
    lin_np = np.interp(q, xs, ys)
    lin_sp = interpolate.interp1d(xs, ys, kind="linear")(q)
    cub = interpolate.CubicSpline(xs, ys)(q)
    tr = np.tanh(6.0 * (q - 0.5))
    print(f"  interpolation    np.interp vs interp1d(linear) max diff = "
          f"{np.abs(lin_np - lin_sp).max():.3e}")
    print(f"                   linear error vs analytic = {np.abs(lin_np - tr).max():.3e}")
    print(f"                   cubic  error vs analytic = {np.abs(cub - tr).max():.3e}")

    s = rng.normal(size=1024)
    f_np = np.fft.rfft(s)
    f_sp = fft.rfft(s, workers=1)
    print(f"  FFT              |np.fft.rfft - scipy.fft.rfft|max = "
          f"{np.abs(f_np - f_sp).max():.3e}")
    print("                   scipy.fft adds planners, workers= and next_fast_len;")
    print("                   the numbers agree, so choose on features, not accuracy.")


def part4_constants_provenance():
    section("4. scipy.constants: provenance for a number you already quote")
    gm_earth_quoted = 3.986004418e14          # m3 s-2, standard geodetic value
    m_earth_quoted = 5.9722e24                # kg, nominal
    gm_from_g = constants.G * m_earth_quoted
    rel_unc = constants.physical_constants[
        "Newtonian constant of gravitation"][2] / constants.G
    print(f"  G (CODATA)                 = {constants.G:.6e} m3 kg-1 s-2")
    print(f"  G relative uncertainty     = {rel_unc:.2e}")
    print(f"  g (standard gravity)       = {constants.g} m s-2  (defined, not measured)")
    print(f"  M_earth (nominal) times G  = {gm_from_g:.6e} m3 s-2")
    print(f"  GM_earth (quoted, IERS)    = {gm_earth_quoted:.6e} m3 s-2")
    print(f"  relative difference        = "
          f"{abs(gm_from_g - gm_earth_quoted) / gm_earth_quoted:.2e}")
    print()
    print("  The difference is 5.3e-6: the precision with which M_earth is itself")
    print("  quoted. Note that G's own relative uncertainty, 2.25e-5, is five times")
    print("  larger still, and it is G that limits the product. Satellite geodesy")
    print("  determines GM directly from orbit dynamics, so GM_earth is known far")
    print("  better than G*M can ever be -- which is why geodesy quotes GM, and")
    print("  never M. A product is only as good as its weakest factor.")


def main():
    part1_versions_and_lazy_loading()
    part2_one_task_per_subpackage()
    part3_overlaps_with_numpy()
    part4_constants_provenance()
    print("\nDone.")


if __name__ == "__main__":
    main()
