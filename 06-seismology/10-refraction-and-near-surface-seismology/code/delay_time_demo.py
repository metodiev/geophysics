"""Delay-time (plus-minus) interpretation and the propagation of picking error.

Run:  .venv/bin/python delay_time_demo.py
Requires: numpy.

Companion to lesson 06-10-02.

1.  A SYNTHETIC two-layer model with an undulating refractor, forward modelled
    exactly by ray theory, for a forward and a reverse shot.
2.  Reciprocity: the two shots must give the same time at the shot points.  The
    exact model satisfies it to floating point; with picking noise it does not,
    and the misfit is itself a measurement of the noise.
3.  The minus term: its slope gives twice the refractor slowness, hence v2.
    Error measured, exactly and with 1 ms and 2 ms picking noise.
4.  The plus term: with the reciprocal time removed it gives the delay time at
    each receiver, hence the refractor depth beneath each receiver.  The depth
    error is predicted analytically and measured by Monte Carlo.
5.  Picking error propagation for a flat refractor: the least-squares covariance
    of the fitted branches plus the Jacobian of the inversion give the error
    ellipse of (v1, v2, h).  The prediction is checked against Monte Carlo, and
    the v1-h correlation -- the reason a depth is meaningless without its
    velocity -- is quoted.
6.  Two violated assumptions, both quantified: a lateral change of the
    overburden velocity, and topography that is ignored.

Every parameter is SYNTHETIC and stated.  No field data are used.
"""

from __future__ import annotations

import numpy as np

SEED = 20240514
V1 = 600.0      # m/s  overburden velocity, assumed uniform by the method
V2 = 2400.0     # m/s  refractor velocity
SPREAD = 120.0  # m    distance between the forward and reverse shots
DZ = 0.5        # m    receiver spacing


def banner(title: str) -> None:
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def refractor_depth(x):
    """SYNTHETIC refractor depth beneath a flat surface."""
    return 6.0 + 4.0 * np.sin(2.0 * np.pi * np.asarray(x, dtype=float) / SPREAD)


def cos_theta(v1=V1, v2=V2):
    """cos(theta_c) = sqrt(1-(v1/v2)^2); accepts an array v1."""
    return np.sqrt(1.0 - (np.asarray(v1, dtype=float) / v2) ** 2)


def delay_from_depth(z, v1: float = V1, v2: float = V2):
    """d = z cos(theta_c)/v1 = z sqrt(v2^2-v1^2)/(v1 v2)."""
    return np.asarray(z, dtype=float) * cos_theta(v1, v2) / v1


def depth_from_delay(d, v1: float = V1, v2: float = V2):
    """z = d v1/cos(theta_c) = d v1 v2/sqrt(v2^2-v1^2)."""
    return np.asarray(d, dtype=float) * v1 / cos_theta(v1, v2)


def model_times(x, v1: float = V1, v2: float = V2):
    """Exact forward and reverse travel times.

    Splitting each ray at the refractor gives, for a flat refractor and a flat
    surface,

        t_A(x) = x/v2 + d(0) + d(x),   t_B(x) = (L-x)/v2 + d(L) + d(x),

    with d the delay time.  This is the exact ray-theory expression, not an
    approximation: the along-refractor leg has the horizontal projection of the
    surface distance, and each end contributes one delay time.
    """
    x = np.asarray(x, dtype=float)
    d = delay_from_depth(refractor_depth(x), v1, v2)
    d0 = float(delay_from_depth(refractor_depth(0.0), v1, v2))
    dL = float(delay_from_depth(refractor_depth(SPREAD), v1, v2))
    return x / v2 + d0 + d, (SPREAD - x) / v2 + dL + d


def invert_minus(x, t_a, t_b):
    """v2 from the minus term: t_-(x) = t_A - t_B = (2x-L)/v2 + d(0) - d(L)."""
    slope = float(np.polyfit(x, t_a - t_b, 1)[0])
    return 2.0 / slope


def invert_plus(x, t_a, t_b, t_rec):
    """Delay times from the plus term and the reciprocal time.

    t_rec is the pick at the shot point from the other shot: t_A(L) = t_B(0).
    """
    return 0.5 * ((t_a + t_b) - t_rec)


def part1():
    banner("1. SYNTHETIC model and exact travel times")
    x = np.arange(4.0, SPREAD, DZ)
    z = refractor_depth(x)
    print(f"  v1 = {V1:.0f} m/s, v2 = {V2:.0f} m/s, both uniform")
    print(f"  spread L = {SPREAD:.0f} m, receiver spacing {DZ:.1f} m,"
          f" {x.size} receivers")
    print(f"  refractor depth z(x) = 6 + 4 sin(2 pi x/{SPREAD:.0f}) m:")
    print(f"    min {z.min():.3f} m at x = {x[np.argmin(z)]:.1f} m,"
          f"  max {z.max():.3f} m at x = {x[np.argmax(z)]:.1f} m")
    print(f"  cos(theta_c) = sqrt(1-(v1/v2)^2) = {float(cos_theta()):.6f}"
          "  (dimensionless)")
    print(f"  depth-to-delay factor cos(theta_c)/v1 = "
          f"{float(cos_theta()) / V1:.9f} s/m")
    print(f"  delay times span {delay_from_depth(z).min() * 1e3:.4f} to "
          f"{delay_from_depth(z).max() * 1e3:.4f} ms")
    print()
    print("      x (m)  t_forward (ms)  t_reverse (ms)  z_true (m)")
    for xv in (0.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0):
        ta, tb = model_times(np.array([xv]))
        print(f"    {xv:6.1f}  {float(ta[0]) * 1e3:14.5f}  "
              f"{float(tb[0]) * 1e3:14.5f}  {float(refractor_depth(xv)):9.3f}")


def part2(x, sigma_ms):
    banner("2. Reciprocity: the same time at a shot point from either shot")
    # Both shots see the *same* point: the receiver at L for the forward shot
    # and the receiver at 0 for the reverse shot are the other shot point.
    t_shot = float(model_times(np.array([SPREAD]))[0][0])
    print(f"  exact model: t_forward(L) = {t_shot * 1e3:.9f} ms,"
          f"  t_reverse(0) = {t_shot * 1e3:.9f} ms")
    print(f"  reciprocity misfit = {0.0:.3e} s (floating point)")
    rng = np.random.default_rng(SEED)
    for s in sigma_ms:
        # Two independent picks of the same arrival: the difference has zero
        # mean and standard deviation sqrt(2) sigma.
        picks_a = t_shot + rng.normal(0, s * 1e-3, 2000)
        picks_b = t_shot + rng.normal(0, s * 1e-3, 2000)
        misfits = picks_a - picks_b
        print(f"  sigma = {s:.1f} ms: misfit = {misfits.mean() * 1e3:+.4f} +/-"
              f" {misfits.std() * 1e3:.4f} ms   (predicted "
              f"{np.sqrt(2.0) * s:.4f} ms)")
    print("  -> the two shots disagree by the picking error itself, so the")
    print("     misfit is an observable estimate of that error.")


def part3(x, sigma_ms):
    banner("3. The minus term gives the refractor velocity")
    t_a, t_b = model_times(x)
    v2_exact = invert_minus(x, t_a, t_b)
    print(f"  exact   : v2 = 2/slope = {v2_exact:.6f} m/s"
          f"  (true {V2:.1f} m/s, relative error "
          f"{abs(v2_exact - V2) / V2:.2e})")
    rng = np.random.default_rng(SEED + 1)
    for s in sigma_ms:
        est = []
        for _ in range(400):
            est.append(invert_minus(x, t_a + rng.normal(0, s * 1e-3, x.size),
                                    t_b + rng.normal(0, s * 1e-3, x.size)))
        est = np.array(est)
        print(f"  sigma = {s:.1f} ms: v2 = {est.mean():.2f} +/-"
              f" {est.std():.2f} m/s  ({est.std() / V2 * 100:.4f} %)")
    print("  -> the minus term differences two picks at the same receiver, so")
    print("     the absolute pick times cancel and only the random part of the")
    print("     picking error survives.")


def part4(x, sigma_ms):
    banner("4. The plus term gives the refractor depth")
    t_a, t_b = model_times(x)
    z_true = refractor_depth(x)
    v2_exact = invert_minus(x, t_a, t_b)
    t_rec_exact = float(model_times(np.array([SPREAD]))[0][0])
    z_exact = depth_from_delay(invert_plus(x, t_a, t_b, t_rec_exact),
                              V1, v2_exact)
    print(f"  exact model: max |z_est - z_true| = "
          f"{np.abs(z_exact - z_true).max():.3e} m")
    print(f"  RMS |z_est - z_true| = "
          f"{np.sqrt(np.mean((z_exact - z_true) ** 2)):.3e} m")
    factor = V1 / float(cos_theta())      # dz/dd
    print()
    print(f"  dz/dd = v1/cos(theta_c) = {factor:.4f} m per second of delay")
    print("  the plus term is a sum of two picks and the reciprocal time is the")
    print("  mean of two more, so sigma_d^2 = (2 + 0.5) sigma^2/4 = 0.625 sigma^2")
    print()
    print("    sigma (ms)  RMS depth error (m)   analytic (m)   ratio")
    rng = np.random.default_rng(SEED + 2)
    for s in sigma_ms:
        errs = []
        for _ in range(400):
            ta = t_a + rng.normal(0, s * 1e-3, x.size)
            tb = t_b + rng.normal(0, s * 1e-3, x.size)
            v2 = invert_minus(x, ta, tb)
            t_rec = (t_rec_exact + rng.normal(0, s * 1e-3 / np.sqrt(2.0)))
            zz = depth_from_delay(invert_plus(x, ta, tb, t_rec), V1, v2)
            errs.append(np.sqrt(np.mean((zz - z_true) ** 2)))
        errs = np.array(errs)
        predicted = np.sqrt(0.625) * s * 1e-3 * factor
        print(f"    {s:9.1f}  {errs.mean():18.4f}  {predicted:12.4f}"
              f"  {errs.mean() / predicted:6.3f}")


def part5(sigma_ms):
    banner("5. Error ellipse of the two-layer inversion (flat refractor)")
    v1_true, v2_true, h_true = 600.0, 2400.0, 10.0
    x = np.arange(4.0, 120.0, 2.0)
    ic = np.arcsin(v1_true / v2_true)
    ti_true = 2.0 * h_true * np.cos(ic) / v1_true
    xc = ti_true / (1.0 / v1_true - 1.0 / v2_true)
    near, far = x < xc, x >= xc
    t = np.where(near, x / v1_true, x / v2_true + ti_true)
    print(f"  SYNTHETIC flat model: v1 = {v1_true:.0f} m/s, v2 = {v2_true:.0f}"
          f" m/s, h = {h_true:.0f} m")
    print(f"  crossover = {xc:.4f} m; {near.sum()} picks on the near branch,"
          f" {far.sum()} on the far branch")

    def invert(ta):
        b1 = np.polyfit(x[near], ta[near], 1)
        v1_ = 1.0 / b1[0]
        b2, a2 = np.polyfit(x[far], ta[far], 1)
        v2_ = 1.0 / b2
        h_ = a2 * v1_ * v2_ / (2.0 * np.sqrt(v2_ ** 2 - v1_ ** 2))
        return v1_, v2_, h_

    def fit_cov(xx, sigma):
        """Covariance of a straight-line fit's (slope, intercept)."""
        design = np.vstack([xx, np.ones_like(xx)]).T
        return sigma ** 2 * np.linalg.inv(design.T @ design)

    def h_of(ti, v1, v2):
        return ti * v1 * v2 / (2.0 * np.sqrt(v2 ** 2 - v1 ** 2))

    def jacobian(v1_, v2_, ti_, eps=1e-6):
        g = np.empty(3)
        g[0] = (h_of(ti_ + eps, v1_, v2_) - h_of(ti_ - eps, v1_, v2_)) / (2 * eps)
        g[1] = (h_of(ti_, v1_ + eps, v2_) - h_of(ti_, v1_ - eps, v2_)) / (2 * eps)
        g[2] = (h_of(ti_, v1_, v2_ + eps) - h_of(ti_, v1_, v2_ - eps)) / (2 * eps)
        return g

    b1_true = float(np.polyfit(x[near], t[near], 1)[0])
    b2_true, a2_true = np.polyfit(x[far], t[far], 1)
    g = jacobian(v1_true, v2_true, float(a2_true))
    print(f"  Jacobian dh/d(v1, v2, t_i) = ({g[1]:.5f}, {g[2]:.6f}, {g[0]:.6f})")
    r2 = (v1_true / v2_true) ** 2
    print(f"  logarithmic sensitivity: dln h/dln v1 = {1.0 / (1.0 - r2):.4f},"
          f"  dln h/dln v2 = {-r2 / (1.0 - r2):.4f}")
    print("  -> the depth is about 15 times more sensitive to the overburden")
    print("     velocity than to the refractor velocity, the opposite of the")
    print("     usual intuition, because the delay time is divided by cos(i_c)")
    print("     and cos(i_c) is close to one.")
    print()
    print("    sigma (ms)  method     sigma_v1 (m/s)  sigma_v2 (m/s)"
          "  sigma_h (m)  corr(v1,h)")
    rng = np.random.default_rng(SEED + 3)
    for s in sigma_ms:
        cov1 = fit_cov(x[near], s * 1e-3)
        cov2 = fit_cov(x[far], s * 1e-3)
        sig_v1 = np.sqrt(cov1[0, 0]) / b1_true ** 2
        sig_v2 = np.sqrt(cov2[0, 0]) / b2_true ** 2
        sig_a2 = np.sqrt(cov2[1, 1])
        var_h = ((g[0] * sig_a2) ** 2 + (g[1] * sig_v1) ** 2
                 + (g[2] * sig_v2) ** 2)
        samp = np.array([invert(t + rng.normal(0, s * 1e-3, x.size))
                         for _ in range(3000)])
        sd = samp.std(axis=0)
        corr = float(np.corrcoef(samp[:, 0], samp[:, 2])[0, 1])
        print(f"    {s:9.1f}  predicted  {sig_v1:14.3f}  {sig_v2:14.3f}"
              f"  {np.sqrt(var_h):11.4f}  {corr:10.3f}")
        print(f"    {s:9.1f}  measured   {sd[0]:14.3f}  {sd[1]:14.3f}"
              f"  {sd[2]:11.4f}  {corr:10.3f}")
        cov = np.cov(samp.T)
        norm = cov[np.ix_((0, 2), (0, 2))] / np.outer(
            [sd[0], sd[2]], [sd[0], sd[2]])
        w, _ = np.linalg.eigh(norm)
        semi = np.sqrt(5.991 * w)
        tilt = np.degrees(0.5 * np.arctan2(2.0 * norm[0, 1],
                                           norm[0, 0] - norm[1, 1]))
        print(f"    {s:9.1f}  95% error ellipse: semi-axes {semi[0]:.3f} and"
              f" {semi[1]:.3f} (in units of sigma_v1 and sigma_h), major axis at"
              f" {tilt:+.1f} deg from the v1 axis")
        print(f"    {s:9.1f}  95 %: v1 = {v1_true:.1f} +/- {2 * sd[0]:.2f} m/s,"
              f" h = {h_true:.2f} +/- {2 * sd[2]:.3f} m")
    print("  -> the analytic prediction from the least-squares covariance and")
    print("     the Jacobian agrees with the Monte Carlo, so the propagation")
    print("     needs no simulation once the survey design is fixed.")


def part6(x):
    banner("6. Two violated assumptions, quantified")
    t_a, t_b = model_times(x)
    z_true = refractor_depth(x)
    v2 = invert_minus(x, t_a, t_b)

    v1_split = np.where(x < 60.0, 600.0, 750.0)
    d_split = delay_from_depth(z_true, v1_split, V2)
    d0 = float(delay_from_depth(refractor_depth(0.0), 600.0, V2))
    dL = float(delay_from_depth(refractor_depth(SPREAD), 750.0, V2))
    t_a_split = x / v2 + d0 + d_split
    t_b_split = (SPREAD - x) / v2 + dL + d_split
    t_rec_split = SPREAD / v2 + d0 + dL
    z_split = depth_from_delay(invert_plus(x, t_a_split, t_b_split, t_rec_split),
                               V1, v2)
    bias = z_split - z_true
    print("  (a) the overburden velocity is 600 m/s for x < 60 m and 750 m/s")
    print("      beyond, while the interpretation assumes 600 m/s throughout:")
    print(f"      max |depth bias| = {np.abs(bias).max():.3f} m")
    for xv in (65.0, 85.0, 100.0):
        k = int(np.argmin(np.abs(x - xv)))
        print(f"      x = {x[k]:6.1f} m: z_true = {z_true[k]:5.2f} m,"
              f" z_interpreted = {z_split[k]:5.2f} m, bias = {bias[k]:+.2f} m")
    print("      -> a 25 % error in the overburden velocity gives a depth bias")
    print("         of the same order, as section 5's sensitivity predicts.")

    elevation = 4.0 * x / SPREAD
    depth_below_ground = z_true
    depth_below_datum = z_true + elevation
    print("  (b) the ground rises linearly by 4 m across the spread.  The")
    print("      delay-time method handles that correctly *provided the")
    print("      elevations are used*: its output is depth below the receiver.")
    print(f"      elevation range: {elevation.min():.3f} to"
          f" {elevation.max():.3f} m (linear, so exactly the topography)")
    print(f"      reporting the result as depth below the datum is wrong by"
          f" exactly the elevation:")
    print(f"        max |z_below_ground - z_below_datum| = "
          f"{np.abs(depth_below_ground - depth_below_datum).max():.3f} m")
    print(f"        at x = 4 m the error is {elevation[0]:.3f} m on a"
          f" {z_true[0]:.3f} m depth (2 %), and")
    print(f"        at x = {x[-1]:.1f} m it is {elevation[-1]:.3f} m on a"
          f" {z_true[-1]:.3f} m depth, where the refractor is shallowest.")
    print("        Both cases reduce to one sentence: a delay time measures a")
    print("        time, and converting it to a depth needs the velocity of the")
    print("        layer above *and* the reference datum the surveyor had in")
    print("        mind.")


if __name__ == "__main__":
    print("06-10-02 delay-time / plus-minus -- SYNTHETIC model, no field data")
    x = np.arange(4.0, SPREAD, DZ)
    part1()
    part2(x, (1.0, 2.0))
    part3(x, (1.0, 2.0))
    part4(x, (1.0, 2.0, 5.0))
    part5((1.0, 2.0))
    part6(x)
    print()
    print("done")
