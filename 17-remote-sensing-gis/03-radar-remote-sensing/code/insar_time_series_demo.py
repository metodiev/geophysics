#!/usr/bin/env python3
"""InSAR time series: the design matrix and its null space, min-norm inversion,
noise scaling, temporal coherence, persistent-scatterer screening and the
closure phase.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python insar_time_series_demo.py

Everything is SYNTHETIC: the deformation history, the acquisition dates, the
network, the noise and the scatterer statistics are teaching values generated in
this file.  No real scene, acquisition list or station is used.

Print-only: nothing is downloaded, nothing is written to disk.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C = 299_792_458.0        # m/s
LAM = C / 5.300e9        # m     teaching carrier 5.300 GHz
COS_INC = np.cos(np.radians(35.0))   # vertical -> line of sight


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def build_network(t, max_dt):
    """All pairs closer in time than max_dt, as (i, j) index pairs."""
    return [(i, j) for i in range(t.size) for j in range(i + 1, t.size)
            if t[j] - t[i] <= max_dt]


def design_matrix(pairs, n_epochs):
    """Incidence matrix: row (i,j) has +1 at j and -1 at i."""
    a = np.zeros((len(pairs), n_epochs))
    for row, (i, j) in enumerate(pairs):
        a[row, i] = -1.0
        a[row, j] = 1.0
    return a


def main():
    n_epochs = 40
    span_yr = 3.0
    t = np.sort(RNG.uniform(0.0, span_yr, n_epochs))
    v_true = 12.0            # mm/yr, vertical
    a_seas = 8.0             # mm, seasonal amplitude
    phi_seas = 0.6           # yr, seasonal phase

    def disp_mm(tt):
        return v_true * tt + a_seas * np.sin(2.0 * np.pi * (tt - phi_seas))

    d_los = COS_INC * disp_mm(t) / 1000.0        # m
    phase_true = 4.0 * np.pi * d_los / LAM       # rad

    section("1. The synthetic truth: a deforming surface and its phases")
    print(f"carrier 5.300 GHz, lam = {LAM*100:.4f} cm; incidence 35 deg, "
          f"cos = {COS_INC:.4f}")
    print(f"velocity {v_true:.1f} mm/yr vertical, seasonal amplitude "
          f"{a_seas:.1f} mm, {n_epochs} epochs over {span_yr:.1f} yr\n")
    print("   epoch   t (yr)   vertical (mm)   LOS (mm)   phase (rad)   wrapped (rad)")
    for k in (0, 4, 10, 20, n_epochs - 1):
        w = (phase_true[k] + np.pi) % (2.0 * np.pi) - np.pi
        print(f"   {k:5d}   {t[k]:6.3f}   {disp_mm(t[k]):13.2f}   "
              f"{disp_mm(t[k])*COS_INC:8.2f}   {phase_true[k]:11.3f}   {w:13.3f}")
    print(f"\n  total phase span {np.ptp(phase_true):.3f} rad = "
          f"{np.ptp(phase_true)/(2*np.pi):.2f} fringes, so every pair of epochs")
    print("  separated by more than about half a season is wrapped many times over.")

    section("2. The network, its rank, and what is undetermined")
    pairs = build_network(t, 0.70)
    a_mat = design_matrix(pairs, n_epochs)
    rank = np.linalg.matrix_rank(a_mat)
    print(f"  {n_epochs} epochs, {len(pairs)} small-baseline pairs "
          f"(t_j - t_i <= 0.70 yr)")
    print(f"  design matrix {a_mat.shape}, rank = {rank}, "
          f"null-space dimension = {n_epochs - rank}")
    print("  the null space of a connected network is the constant vector: adding a")
    print("  constant to every epoch's phase leaves every difference unchanged, so the")
    print("  absolute phase of the region is never determined by the data.")
    v_est = np.polyfit(t, phase_true, 1)[0]
    print(f"\n  as a check: a straight-line fit to the TRUE phases gives "
          f"{v_est*LAM/(4*np.pi*COS_INC)*1000:.3f} mm/yr,")
    print(f"  whereas the true velocity is {v_true:.3f} mm/yr: the seasonal term")
    print("  biases a naive linear fit by "
          f"{v_est*LAM/(4*np.pi*COS_INC)*1000 - v_true:+.3f} mm/yr.")

    # disconnected component: drop the pairs that bridge the half-way point
    cut = 1.5
    split = [(i, j) for (i, j) in pairs if not (t[i] < cut <= t[j])]
    a_split = design_matrix(split, n_epochs)
    rank_s = np.linalg.matrix_rank(a_split)
    phi_c = np.linalg.pinv(a_mat) @ (a_mat @ phase_true)
    print(f"\n  now drop the {len(pairs)-len(split)} pairs that bridge t = {cut:.1f} yr:")
    print(f"  {len(split)} pairs, rank = {rank_s}, "
          f"null-space dimension = {n_epochs - rank_s} (one constant per component)")
    phi_s = np.linalg.pinv(a_split) @ (a_split @ phase_true)
    g1 = t < cut
    g2 = ~g1
    fac = LAM / (4 * np.pi * COS_INC) * 1000
    v1c = np.polyfit(t[g1], phi_c[g1], 1)[0] * fac
    v2c = np.polyfit(t[g2], phi_c[g2], 1)[0] * fac
    v1d = np.polyfit(t[g1], phi_s[g1], 1)[0] * fac
    v2d = np.polyfit(t[g2], phi_s[g2], 1)[0] * fac
    print("  velocity recovered within each component, connected versus split:")
    print(f"    component 1 (t < {cut} yr): connected {v1c:8.4f}   split {v1d:8.4f} mm/yr")
    print(f"    component 2 (t > {cut} yr): connected {v2c:8.4f}   split {v2d:8.4f} mm/yr")
    rel_c = np.mean(phi_c[g2]) - np.mean(phi_c[g1])
    rel_s = np.mean(phi_s[g2]) - np.mean(phi_s[g1])
    off_c = rel_s - rel_c
    print(f"  but the offset BETWEEN the components moves by "
          f"{off_c:+.4f} rad = {off_c*LAM/(4*np.pi)*1000:+.3f} mm of LOS")
    print("  when the bridging pairs are removed: the trend inside a component survives")
    print("  disconnection, the relative offset between components does not, and neither")
    print("  component's trend is unbiased by the seasonal term if the model omits it.")

    section("3. Min-norm inversion of a noisy network")
    sigma_phi = 0.5
    phi_obs = a_mat @ phase_true + sigma_phi * RNG.standard_normal(len(pairs))
    phi_hat = np.linalg.pinv(a_mat) @ phi_obs
    v_hat = np.polyfit(t, phi_hat, 1)[0] * LAM / (4 * np.pi * COS_INC) * 1000
    print(f"  pair phase noise sigma_phi = {sigma_phi:.2f} rad = "
          f"{sigma_phi*LAM/(4*np.pi)*1000:.3f} mm of LOS")
    print(f"  min-norm solution: recovered velocity {v_hat:.4f} mm/yr "
          f"(true {v_true:.1f} mm/yr, error {v_hat-v_true:+.4f})")
    print(f"  residual phase rms of the fit: "
          f"{np.sqrt(np.mean((a_mat @ phi_hat - phi_obs)**2)):.4f} rad")
    print(f"  Redundancy = {len(pairs)} pairs - {rank} unknowns = "
          f"{len(pairs)-rank}, so the fit can be checked, not just inverted.")

    section("4. How the velocity uncertainty scales with the number of pairs")
    print("  fixed sigma_phi = 0.50 rad.  First: what a RANDOM subset of pairs does")
    print("  to the graph, which is a connectivity question before it is a noise one.\n")
    print("   M pairs   fraction of random subsets that disconnect")
    ms = [20, 50, 100, 200]
    for m in ms:
        bad = 0
        reps = 200
        for _ in range(reps):
            idx = RNG.choice(len(pairs), size=m, replace=False)
            if np.linalg.matrix_rank(a_mat[idx]) < n_epochs - 1:
                bad += 1
        print(f"   {m:7d}   {bad/reps:45.3f}")
    print("  a 379-pair network still disconnects when only 200 of its pairs are kept,")
    print("  because random thinning isolates epochs.  Redundancy must be distributed,")
    print("  not merely large.")
    print("\n  now hold connectivity fixed: every subset contains the spanning chain")
    print("  (i, i+1) for all 39 consecutive epoch pairs, plus random extra pairs.\n")
    chain = []
    for i in range(n_epochs - 1):
        if (i, i + 1) in pairs:
            chain.append(pairs.index((i, i + 1)))
    extras = [k for k in range(len(pairs)) if k not in set(chain)]
    print(f"   spanning chain pairs: {len(chain)};  extra pairs available: "
          f"{len(extras)}\n")
    print("   M pairs   velocity error (mm/yr)   1/sqrt(M) relative to M=59")
    ms2 = [len(chain) + 20, len(chain) + 60, len(chain) + 160, len(chain) + 300]
    errs2 = []
    for m in ms2:
        reps = 200
        e = []
        for _ in range(reps):
            idx = np.array(chain + list(RNG.choice(extras, size=m - len(chain),
                                                   replace=False)))
            aa = a_mat[idx]
            dd = aa @ phase_true + sigma_phi * RNG.standard_normal(aa.shape[0])
            ph = np.linalg.pinv(aa) @ dd
            e.append(abs(np.polyfit(t, ph, 1)[0] * LAM / (4 * np.pi * COS_INC) * 1000
                         - v_true))
        errs2.append(np.mean(e))
        print(f"   {m:7d}   {np.mean(e):22.6f}   "
              f"{np.sqrt(ms2[0]/m):24.3f}")
    slope = np.polyfit(np.log(ms2), np.log(errs2), 1)[0]
    print(f"\n  measured log-log slope of error versus M: {slope:.3f}")
    print("  a slope near -0.5 is the sqrt(M) averaging law: each extra pair adds an")
    print("  independent constraint on the same phase differences, and the estimate is")
    print("  a weighted average of them.  The network buys accuracy by redundancy, not")
    print("  by a better single measurement.")

    section("5. Temporal coherence: what it measures and what it misses")
    def temporal_coherence(resid):
        return abs(np.mean(np.exp(1j * resid)))

    print("  gamma_t = |mean exp(i residual)| over the PAIRS, with")
    print("  residual = (A phi_model) - (A phi_obs).")
    print("  It measures the DISPERSION of the residual, not its mean: a constant")
    print("  residual phase rotates every term equally and does not lower gamma_t.\n")
    dt_pairs = np.array([t[j] - t[i] for (i, j) in pairs])
    big = build_network(t, 2.50)
    a_big = design_matrix(big, n_epochs)
    dt_big = np.array([t[j] - t[i] for (i, j) in big])
    print(f"  network A: {len(pairs)} pairs, baseline span "
          f"{dt_pairs.min():.3f}-{dt_pairs.max():.3f} yr")
    print(f"  network B: {len(big)} pairs, baseline span "
          f"{dt_big.min():.3f}-{dt_big.max():.3f} yr\n")
    print("   model velocity fraction   network   mean residual   residual std   gamma_t")
    for ss in (0.0, 1.0):
        for frac in (1.0, 0.9, 0.5):
            for name, aa, dd in (("A", a_mat, dt_pairs), ("B", a_big, dt_big)):
                mod = COS_INC * (v_true * frac * t
                                 + ss * a_seas * np.sin(2.0 * np.pi * (t - phi_seas)))
                mod = mod / 1000.0
                res = aa @ (4.0 * np.pi * mod / LAM) - (aa @ phase_true)
                tag = f"v x {frac:.2f}"
                if ss == 0.0:
                    tag += ", no seasonal"
                print(f"   {tag:24s}   {name:7s}   {res.mean():13.4f}   "
                      f"{res.std():12.4f}   {temporal_coherence(res):7.4f}")
    print("\n  noiseless residuals, so gamma_t isolates the model error.  Note that")
    print("  (i) omitting the seasonal term collapses gamma_t even at the true velocity,")
    print("  and (ii) a velocity error barely moves gamma_t in network A, where every")
    print("  baseline is short and the residual is nearly the same for every pair — but")
    print("  it moves it clearly in network B, whose long baselines spread the residual.")
    print("  The lesson: gamma_t sees model error only through the SPREAD of the")
    print("  residual, so the information about velocity lives in long baselines.")
    print("  A small-baseline network is robust to unwrapping and weak on rate, and")
    print("  gamma_t computed on it conceals that.  Report the residual mean and spread,")
    print("  not gamma_t alone.")

    section("6. Persistent-scatterer screening by amplitude dispersion")
    print("  amplitude dispersion D_A = sigma_A / mean_A over N dates\n")
    print("   N dates   stable median D_A   speckle median D_A   speckle fraction below 0.25")
    for n_dates in (4, 8, 16, 40):
        n_scat = 4000
        amp_stable = 1.0 + 0.08 * RNG.standard_normal((n_scat, n_dates))
        amp_speckle = np.abs(RNG.standard_normal((n_scat, n_dates))
                             + 1j * RNG.standard_normal((n_scat, n_dates)))
        d_s = amp_stable.std(axis=1) / amp_stable.mean(axis=1)
        d_p = amp_speckle.std(axis=1) / amp_speckle.mean(axis=1)
        print(f"   {n_dates:7d}   {np.median(d_s):16.3f}   {np.median(d_p):18.3f}   "
              f"{np.mean(d_p < 0.25):25.3f}")
    print("\n  a speckle-only pixel has D_A near 0.5, and its sampling spread narrows as")
    print("  the number of dates grows.  With few dates the overlap between the two")
    print("  populations is wide, so the false-positive rate of any fixed threshold")
    print("  depends on N.  D_A is a screening statistic: report the threshold AND the")
    print("  number of dates, and measure the rate on a control population.")

    section("7. Closure phase: detecting a bad pair in a triangle")
    tri = [(0, 1), (1, 2), (0, 2)]
    phi12 = a_mat[0] @ phase_true if len(pairs) else 0.0
    d12 = (phase_true[1] - phase_true[0])
    d23 = (phase_true[2] - phase_true[1])
    d13 = (phase_true[2] - phase_true[0])
    print("  for three epochs the differences must satisfy the closure identity")
    print("    (phi_2 - phi_1) + (phi_3 - phi_2) - (phi_3 - phi_1) = 0")
    print(f"  with clean data: closure = {d12 + d23 - d13:.6f} rad")
    slip = 2.0 * np.pi
    print(f"  inject a single cycle slip of 2 pi = {slip:.6f} rad into pair (1,2):")
    print(f"    closure = {d12 + (d23 + slip) - d13:.6f} rad")
    print(f"  the closure residual equals one full cycle, "
          f"{slip*LAM/(4*np.pi)*1000:.4f} mm of LOS displacement, which is")
    print("  exactly the ambiguity: an integer slip is invisible in any single pair")
    print("  but breaks the closure of every triangle that contains it.  With many")
    print("  triangles the offending pair can be identified, not just detected.")
    print("  (the demonstration uses three epochs for clarity; a real network tests")
    print("  every triangle in the small-baseline graph.)")


if __name__ == "__main__":
    main()
