"""Line, scatter and error-bar plots that carry uncertainty honestly.

Run:  .venv/bin/python 02_line_scatter_plots_demo.py
Requires: numpy, matplotlib (headless Agg backend).

Companion to lesson 03-05-02.

The synthetic data are a straight line plus Gaussian scatter whose standard
deviation grows with x (heteroscedastic). Because the generating process is
known here, the empirical coverage of the plotted error bars can be *measured*
rather than assumed: the script counts what fraction of the simulated points
fall inside 1 sigma and inside 2 sigma, and prints those counts next to the
68.3 % and 95.4 % the error model predicts. A bar whose coverage is never
checked is a drawing, not a statement about uncertainty.

The weighted least-squares fit is computed from first principles so that the
reported slope, its standard error and the reduced chi-square are all
reproducible from the printed numbers.

Images are written to a temporary directory, never into the repository.
"""

import os
import tempfile

import matplotlib

matplotlib.use("Agg")  # headless: no window, so the script cannot block
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

OUTDIR = tempfile.mkdtemp(prefix="plotting_demo02_")
RNG = np.random.default_rng(19580827)  # named seed -> reproducible stream


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def part1_synthetic_data_and_weights():
    section("1. SYNTHETIC data with a known noise model")

    n = 60
    x = np.linspace(0.0, 10.0, n)
    true_a, true_b = 3.0, 1.5
    # Proportional noise: relative uncertainty 6 %, floor of 0.05.
    sigma = np.hypot(0.06 * (true_a + true_b * x), 0.05)
    y_true = true_a + true_b * x
    y_obs = y_true + sigma * RNG.standard_normal(n)

    print(f"generating model: y = {true_a} + {true_b} x + noise(x)")
    print("  noise standard deviation sigma(x) = "
          "hypot(0.06*(3+1.5x), 0.05)")
    print(f"  n = {n} points")
    print(f"  sigma at x=0 : {sigma[0]:.4f}")
    print(f"  sigma at x=10: {sigma[-1]:.4f}   (grows by a factor "
          f"{sigma[-1] / sigma[0]:.2f})")
    print()
    print("The weights in a least-squares fit are w_i = 1/sigma_i^2. Using")
    print("equal weights on heteroscedastic data would let the noisiest points")
    print("dominate the slope, which is the opposite of what the measurement")
    print("deserves.")
    print(f"  max/min weight ratio: {(sigma[0] / sigma[-1]) ** 2:.3f}")
    return x, y_obs, sigma


def weighted_line_fit(x, y, sigma):
    """Return slope, intercept, their standard errors and chi-square/dof."""
    w = 1.0 / sigma ** 2
    A = np.column_stack([np.ones_like(x), x])          # design matrix [1, x]
    W = np.diag(w)
    cov = np.linalg.inv(A.T @ W @ A)                   # parameter covariance
    coef = cov @ (A.T @ (w * y))                       # weighted normal eqns
    resid = y - A @ coef
    chi2 = float(np.sum(w * resid ** 2))
    dof = x.size - 2
    return coef, np.sqrt(np.diag(cov)), chi2, dof, resid


def part2_fit_and_coverage(x, y, sigma):
    section("2. Weighted least squares: the line is a claim with error bars too")

    coef, err, chi2, dof, resid = weighted_line_fit(x, y, sigma)
    a, b = coef
    print(f"  intercept a = {a:.4f} +/- {err[0]:.4f}  (true 3.0)")
    print(f"  slope     b = {b:.4f} +/- {err[1]:.4f}  (true 1.5)")
    print(f"  chi^2 = {chi2:.3f} for {dof} degrees of freedom"
          f"  ->  chi^2/dof = {chi2 / dof:.3f}")
    print()
    print("chi^2/dof near 1.0 means the scatter is consistent with the stated")
    print("sigma. A value far below 1 would say the error bars are too big; far")
    print("above 1 would say they are too small or the model is wrong. Either")
    print("way, the number to report is the ratio, because it diagnoses whether")
    print("the bars and the model tell the same story.")

    z = resid / sigma
    print()
    print("  empirical coverage of the drawn error bars (n = %d):" % x.size)
    for k in (1, 2, 3):
        inside = int(np.sum(np.abs(z) <= k))
        print(f"    within {k} sigma: {inside:>2}/{x.size} = {inside / x.size:6.3f}"
              f"   (expected {[0.683, 0.954, 0.997][k - 1]:.3f} for Gaussian noise)")
    print()
    print("  A bar of half-length k*sigma therefore means something only when k")
    print("  is stated. 'y = 5.0 +/- 0.3' with no coverage is compatible with a")
    print("  68 % interval, a 95 % interval, or a standard error of the mean;")
    print("  those are different claims and a reader cannot tell them apart.")
    return coef, err


def part3_figures(x, y, sigma, coef, err):
    section("3. Drawing the three canonical panels")

    a, b = coef
    fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.6), dpi=150)

    xf = np.linspace(x.min(), x.max(), 200)
    yf = a + b * xf

    ax = axes[0]
    ax.errorbar(x, y, yerr=sigma, fmt="o", ms=3.2, color="C0",
                ecolor="0.6", elinewidth=0.8, capsize=2, zorder=3,
                label=r"data, $\pm 1\sigma$")
    ax.plot(xf, yf, color="C3", lw=1.4, label="weighted fit")
    ax.set_title("(a) line + scatter + 1-sigma bars")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(frameon=False, fontsize=8)
    ax.grid(True, lw=0.4, alpha=0.35)

    ax = axes[1]
    ax.errorbar(x, y, yerr=2 * sigma, fmt="s", ms=3.0, color="C1",
                ecolor="0.7", elinewidth=0.8, capsize=2,
                label=r"$\pm 2\sigma$ (95 %)")
    ax.set_title("(b) the same data, 2-sigma bars")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(frameon=False, fontsize=8)
    ax.grid(True, lw=0.4, alpha=0.35)

    ax = axes[2]
    sizes = 8.0 + 3.0 * np.sin(x)  # a third, purely decorative variable
    sc = ax.scatter(x, y, s=sizes ** 2 / 4, c=np.abs(y - (a + b * x)),
                    cmap="viridis", edgecolor="k", linewidth=0.3)
    fig.colorbar(sc, ax=ax, label="|residual| (arb. units)")
    ax.set_title("(c) size and colour encode extra variables")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    fig.suptitle("Error bars carry a coverage claim; the fit carries an error too",
                 fontsize=10)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "02_errorbars.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"saved {os.path.basename(path)}  (150 dpi, 3 panels)")
    print("  panel (a) and (b) show identical data and identical bars of")
    print("  different length; only the caption makes (b) a 95 % interval.")


def part4_loglog_power_law():
    section("4. Why log axes are not decoration for a power law")

    # SYNTHETIC: a decaying power law y = A x^-p with multiplicative noise.
    x = np.logspace(-1.0, 2.0, 40)
    A_true, p_true = 12.0, 1.4
    rel = 0.10
    y_true = A_true * x ** (-p_true)
    y = y_true * (1.0 + rel * RNG.standard_normal(x.size))
    yerr = rel * y

    # Fit in log space: log y = log A - p log x, weights from relative error.
    lx, ly = np.log10(x), np.log10(y)
    sig_ly = yerr / (y * np.log(10.0))
    w = 1.0 / sig_ly ** 2
    M = np.column_stack([np.ones_like(lx), lx])
    cov = np.linalg.inv(M.T @ (w[:, None] * M))
    c = cov @ (M.T @ (w * ly))
    logA, slope = c
    elogA, eslope = np.sqrt(np.diag(cov))
    print(f"  recovered exponent p = {-slope:.4f} +/- {eslope:.4f}  (true {p_true})")
    print(f"  recovered A          = {10 ** logA:.4f}  (true {A_true})")
    print()
    print("On linear axes these 40 points span four orders of magnitude in x and")
    print("would collapse the small-x structure into the first pixel column. The")
    print("log-log axes turn the unknown exponent into a straight line, which is")
    print("the only reason a two-parameter fit suffices.")

    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.4), dpi=150)
    axes[0].errorbar(x, y, yerr=yerr, fmt="o", ms=3, capsize=2,
                     color="C0", ecolor="0.7", elinewidth=0.7)
    axes[0].plot(x, y_true, color="0.4", ls="--", lw=1.2, label="true model")
    axes[0].set_xscale("log")
    axes[0].set_yscale("log")
    axes[0].set_xlabel("x (log scale)")
    axes[0].set_ylabel("y (log scale)")
    axes[0].legend(frameon=False, fontsize=8)
    axes[0].set_title("same exponents, log axes")

    axes[1].errorbar(x, y, yerr=yerr, fmt="o", ms=3, capsize=2,
                     color="C0", ecolor="0.7", elinewidth=0.7)
    axes[1].plot(x, y_true, color="0.4", ls="--", lw=1.2)
    axes[1].set_xlabel("x (linear scale)")
    axes[1].set_ylabel("y (linear scale)")
    axes[1].set_title("same data, linear axes")
    fig.tight_layout()
    path = os.path.join(OUTDIR, "02_loglog.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {os.path.basename(path)}  (150 dpi, side-by-side)")


def part5_x_and_y_errors():
    section("5. Errors in both variables: a bar that disappears when small")

    # SYNTHETIC stations with position uncertainty and a measured field value.
    n = 14
    east = np.linspace(0.0, 60.0, n)
    field = 20.0 - 0.25 * east + 0.6 * RNG.standard_normal(n)
    ex = np.full(n, 1.5)          # horizontal tie error, in km
    ey = np.full(n, 0.4)          # field measurement error

    fig, ax = plt.subplots(figsize=(5.6, 3.6), dpi=150)
    ax.errorbar(east, field, xerr=ex, yerr=ey, fmt="o", ms=4, color="C0",
                ecolor="0.65", elinewidth=0.9, capsize=2)
    ax.set_xlabel("distance east (km)")
    ax.set_ylabel("anomaly (mGal, SYNTHETIC)")
    ax.set_title("Horizontal and vertical uncertainty")
    ax.grid(True, lw=0.4, alpha=0.35)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "02_xyerr.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)

    ratio = ex[0] / ey[0]
    print(f"  horizontal bar {ex[0]} km, vertical bar {ey[0]} mGal -> aspect"
          f" ratio of the numbers {ratio:.2f}")
    print("  Whether the horizontal bar looks 'long' or 'short' depends on the")
    print("  axis scaling, which is a *choice*: the same uncertainty is a wide")
    print("  bar on a zoomed axis and an invisible one on a compressed axis.")
    print("  An uncertainty that is smaller than a marker must be stated in the")
    print("  caption, not silently drawn.")
    print(f"  saved {os.path.basename(path)}  (150 dpi)")


def main():
    x, y, sigma = part1_synthetic_data_and_weights()
    coef, err = part2_fit_and_coverage(x, y, sigma)
    part3_figures(x, y, sigma, coef, err)
    part4_loglog_power_law()
    part5_x_and_y_errors()
    print()
    print("Images written to:", OUTDIR)
    print("Nothing was written inside the repository.")


if __name__ == "__main__":
    main()
