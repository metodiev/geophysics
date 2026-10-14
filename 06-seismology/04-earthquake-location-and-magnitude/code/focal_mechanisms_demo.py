#!/usr/bin/env python3
"""Focal mechanisms: first-motion polarities inverted by grid search, and the
moment tensor decomposed.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python focal_mechanisms_demo.py

Requires: numpy.  No network access.

Everything is SYNTHETIC: the mechanism, the station distribution and the
polarity errors are chosen teaching values.  No real earthquake, station or
catalogue is used.  The moment tensor is built from the standard
strike/dip/rake formulas and checked against the defining properties of a
double couple (zero trace, eigenvalues M0 / 0 / -M0) rather than trusted.

WHAT IS COMPUTED

1. A double-couple moment tensor from strike, dip and rake, with two checks:
   the trace is zero and the eigenvalues are (+M0, 0, -M0).
2. P-wave polarities expected at a synthetic station distribution, from the
   exact sign of n^T M n.
3. The mechanism recovered by grid search over strike, dip and rake, with no
   polarity errors (an exact test) and with 10 per cent of the polarities
   flipped (the honest test).
4. The family of mechanisms that fit the noisy data equally well: how many
   there are and how far apart they are.  This is focal-mechanism
   non-uniqueness, measured rather than asserted.
5. Decomposition of a moment tensor into isotropic, double-couple and
   compensated-linear-vector-dipole parts, with a round-trip check, and the
   moment magnitude that follows from M0.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

M0_TRUE = 3.5e17          # N m, SYNTHETIC scalar moment
STRIKE_TRUE = 225.0       # degrees
DIP_TRUE = 45.0           # degrees
RAKE_TRUE = -90.0         # degrees
N_STATIONS = 24
FLIP_FRACTION = 0.10      # SYNTHETIC fraction of polarities assigned wrongly
ACCEPT_EXTRA = 0.04       # extra misfit allowed when collecting the family


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def moment_tensor(strike_deg, dip_deg, rake_deg, m0=1.0):
    """Moment tensor in (north, east, up), from strike, dip and rake.

    The formulas are the standard ones for a double couple on a fault plane.
    The result is checked against the trace and eigenvalue properties in
    Section 1 rather than assumed.
    """
    phi = np.radians(strike_deg)
    delta = np.radians(dip_deg)
    lam = np.radians(rake_deg)
    s2p, c2p = np.sin(2.0 * phi), np.cos(2.0 * phi)
    sd, cd = np.sin(delta), np.cos(delta)
    s2d = 2.0 * sd * cd
    c2d = cd ** 2 - sd ** 2
    sl, cl = np.sin(lam), np.cos(lam)
    sd_cl = sd * cl
    m = np.empty((3, 3))
    m[0, 0] = -m0 * (sd_cl * s2p + s2d * sl * np.sin(phi) ** 2)
    m[1, 1] = m0 * (sd_cl * s2p - s2d * sl * np.cos(phi) ** 2)
    m[2, 2] = m0 * s2d * sl
    m[0, 1] = m[1, 0] = m0 * (sd_cl * c2p + 0.5 * s2d * sl * s2p)
    m[0, 2] = m[2, 0] = -m0 * (cd * cl * np.cos(phi) + c2d * sl * np.sin(phi))
    m[1, 2] = m[2, 1] = m0 * (cd * cl * np.sin(phi) - c2d * sl * np.cos(phi))
    return m


def station_directions(n_stations):
    """Unit vectors from the source to stations, uniform over the focal sphere.

    A uniform distribution is the wrong model for any real network (stations
    sit on one side of the source and cluster in azimuth) and is used here so
    that the measured non-uniqueness of Section 4 is the BEST case.
    """
    i = np.arange(n_stations) + 0.5
    z = 1.0 - 2.0 * i / n_stations
    phi = 2.0 * np.pi * RNG.random(n_stations)
    r = np.sqrt(np.clip(1.0 - z ** 2, 0.0, None))
    return np.column_stack([r * np.cos(phi), r * np.sin(phi), z])


def polarities(directions, m):
    """Sign of the P-wave radiation n^T M n at every station."""
    return np.sign(np.einsum("ij,jk,ik->i", directions, m, directions))


def grid_mechanisms():
    """Every mechanism on a coarse grid: (axes..., flat tensors)."""
    strikes = np.arange(0.0, 360.0, 5.0)
    dips = np.arange(5.0, 90.0, 5.0)
    rakes = np.arange(-175.0, 180.0, 5.0)
    s, d, r = np.meshgrid(strikes, dips, rakes, indexing="ij")
    s, d, rr = s.ravel(), d.ravel(), r.ravel()
    tensors = np.array([moment_tensor(a, b, c) for a, b, c in zip(s, d, rr)])
    sizes = (strikes.size, dips.size, rakes.size)
    return sizes, s, d, rr, tensors


def misfit_grid(directions, observed, tensors):
    """Fraction of stations whose polarity the candidate mechanism gets wrong."""
    pred = np.einsum("ij,kjl,il->ki", directions, tensors, directions)
    return np.mean(np.sign(pred) != observed[None, :], axis=1)


def tensor_distance(m_a, m_b):
    """Difference between two mechanisms, independent of the parameterisation.

    Each tensor is normalised by its largest eigenvalue magnitude and the
    largest absolute component difference is returned.  This is what makes it
    possible to say whether (strike 225, dip 45, rake -90) and (strike 45,
    dip 40, rake -90) are different mechanisms or the same one described from
    the other nodal plane.
    """
    a = m_a / np.max(np.abs(np.linalg.eigvalsh(m_a)))
    b = m_b / np.max(np.abs(np.linalg.eigvalsh(m_b)))
    return float(np.max(np.abs(a - b)))


def decompose(m):
    """ISO / DC / CLVD split of a symmetric moment tensor, with an exact rebuild.

    Writing the deviatoric part in the eigenvector basis as

        d = a (1, 0, -1) + b (2, -1, -1) ,      a = d1 + 2 d2 ,  b = -d2 ,

    separates a double couple from a compensated linear vector dipole exactly,
    because those two basis tensors are linearly independent and span every
    traceless symmetric tensor.  The percentages are the Frobenius lengths of
    the three parts; the sign of the CLVD part records which eigenvector it is
    aligned with.  `rebuild` is the tensor reconstructed from the split, so the
    split can be tested instead of believed.
    """
    vals, vecs = np.linalg.eigh(m)
    order = np.argsort(vals)[::-1]
    vals = vals[order]
    vecs = vecs[:, order]
    iso = vals.sum() / 3.0
    d = vals - iso
    a = d[0] + 2.0 * d[1]
    b = -d[1]
    dc_mag = abs(a) * np.sqrt(2.0)
    clvd_mag = abs(b) * np.sqrt(6.0)
    iso_mag = abs(iso) * np.sqrt(3.0)
    tot = dc_mag + clvd_mag + iso_mag
    pct = (100.0 * iso_mag / tot if iso >= 0 else -100.0 * iso_mag / tot,
           100.0 * dc_mag / tot,
           100.0 * clvd_mag / tot if b >= 0 else -100.0 * clvd_mag / tot)
    dev_back = a * np.array([1.0, 0.0, -1.0]) + b * np.array([2.0, -1.0, -1.0])
    rebuilt = vecs @ np.diag(dev_back + iso) @ vecs.T
    return pct, vals, rebuilt


def mw_from_m0(m0):
    """Standard moment magnitude, M0 in N m."""
    return (2.0 / 3.0) * (np.log10(m0) - 9.1)


def main():
    print("Focal mechanisms from first motions, and the moment-tensor split")
    print(f"numpy {np.__version__}")
    print()
    print(f"  SYNTHETIC mechanism: strike = {STRIKE_TRUE:.0f} deg, "
          f"dip = {DIP_TRUE:.0f} deg, rake = {RAKE_TRUE:.0f} deg,")
    print(f"  scalar moment M0 = {M0_TRUE:.2e} N m "
          f"(Mw = {mw_from_m0(M0_TRUE):.2f})")
    print(f"  {N_STATIONS} stations distributed uniformly over the focal sphere")

    section("1. The moment tensor from strike, dip and rake, and two checks")
    m = moment_tensor(STRIKE_TRUE, DIP_TRUE, RAKE_TRUE, M0_TRUE)
    labels = ("N", "E", "U")
    print("  moment tensor (N m):")
    for i in range(3):
        print("    " + "  ".join(f"{labels[j]}:{m[i, j]:12.4e}"
                                 for j in range(3)))
    vals = np.linalg.eigvalsh(m)
    print()
    print(f"  trace = {np.trace(m):.4e} N m (must be zero for a double couple)")
    print(f"  eigenvalues (N m) = {np.array2string(vals, precision=4)}")
    print(f"  largest magnitude {np.max(np.abs(vals)):.4e} N m against the input "
          f"{M0_TRUE:.4e} N m")
    print(f"  ratio (sum of |eigenvalues|) / (2 M0) = "
          f"{np.sum(np.abs(vals)) / (2 * M0_TRUE):.6f}")
    print()
    print("  The trace vanishes and the three eigenvalues are +M0, 0, -M0: that")
    print("  is the definition of a double couple without a volume change, and")
    print("  the check is why the strike/dip/rake formulas can be used without")
    print("  re-deriving them.  Zero trace means the source changes the shape of")
    print("  the medium and not its volume, which is the physical statement an")
    print("  isotropic part would violate.")

    section("2. First-motion polarities at the synthetic stations")
    dirs = station_directions(N_STATIONS)
    obs = polarities(dirs, m)
    n_up = int(np.sum(obs > 0))
    n_dn = int(np.sum(obs < 0))
    print(f"  {'station':>8}{'north':>9}{'east':>9}{'up':>8}"
          f"{'n^T M n (N m)':>16}{'polarity':>10}")
    amp = np.einsum("ij,jk,ik->i", dirs, m, dirs)
    for i in range(N_STATIONS):
        print(f"  {i:8d}{dirs[i, 0]:9.3f}{dirs[i, 1]:9.3f}{dirs[i, 2]:8.3f}"
              f"{amp[i]:16.4e}{'compression' if obs[i] > 0 else 'dilatation':>12}")
    print()
    print(f"  compression: {n_up}, dilatation: {n_dn}")
    print("  The two families are separated by two nodal planes, on which the")
    print("  amplitude passes through zero.  A station near a nodal plane carries")
    print("  almost no polarity information, which is why amplitude and station")
    print("  geometry matter as much as the number of stations.")

    section("3. Inverting the polarities by grid search")
    sizes, strikes, dips, rakes, tensors = grid_mechanisms()
    print(f"  grid: {sizes[0]} strikes x {sizes[1]} dips x {sizes[2]} rakes = "
          f"{sizes[0] * sizes[1] * sizes[2]} mechanisms")
    m_true_unit = moment_tensor(STRIKE_TRUE, DIP_TRUE, RAKE_TRUE, 1.0)
    mis = misfit_grid(dirs, obs, tensors)
    best = int(np.argmin(mis))
    exact = np.where(mis == 0.0)[0]
    dist_exact = np.array([tensor_distance(tensors[i], m_true_unit)
                           for i in exact])
    print()
    print("  (a) no polarity errors")
    print(f"      grid best: strike {strikes[best]:.0f}, dip {dips[best]:.0f}, "
          f"rake {rakes[best]:.0f}, misfit {mis[best]:.3f}")
    print(f"      the true mechanism is on the grid and has misfit "
          f"{mis[np.where((strikes == STRIKE_TRUE) & (dips == DIP_TRUE) & (rakes == RAKE_TRUE))[0][0]]:.3f}")
    print(f"      grid mechanisms that reproduce ALL {N_STATIONS} polarities: "
          f"{exact.size} of {mis.size}")
    print(f"      tensor distance from the true mechanism over that family: "
          f"{dist_exact.min():.4f} to {dist_exact.max():.4f} "
          f"(mean {dist_exact.mean():.4f})")
    print(f"      the shortest distance is "
          f"{dist_exact.min():.2e}, i.e. one member IS the true tensor")
    print(f"      the grid best is {tensor_distance(tensors[best], m_true_unit):.4f}"
          f" away in tensor terms, although its strike differs by")
    print(f"      {abs(strikes[best] - STRIKE_TRUE):.0f} deg and its dip by "
          f"{abs(dips[best] - DIP_TRUE):.0f} deg")
    equiv = moment_tensor((STRIKE_TRUE + 180.0) % 360.0, 180.0 - DIP_TRUE,
                          -RAKE_TRUE, 1.0)
    print(f"      check of the standard equivalence: "
          f"(strike+180, 180-dip, -rake) = "
          f"({(STRIKE_TRUE + 180) % 360:.0f}, {180 - DIP_TRUE:.0f}, "
          f"{-RAKE_TRUE:.0f})")
    print(f"      has tensor distance {tensor_distance(equiv, m_true_unit):.2e} "
          f"from the true mechanism")
    print()
    print("  Two separate ambiguities are visible here, and both are real.")
    print("  First, one tensor can be written by several parameter triples: the")
    print("  equivalence printed above is exact, so a 180 deg strike difference")
    print("  between two answers can mean agreement, and a parameter comparison")
    print("  cannot tell the two cases apart.  Second, different tensors can fit")
    print("  the same polarities: " + f"{exact.size} grid mechanisms reproduce all")
    print(f"  {N_STATIONS} signs exactly, and the farthest of them is "
          f"{dist_exact.max():.3f} away")
    print("  in unit-tensor terms.  Each polarity is one bit, and bits are coarse.")
    print("  A mechanism inverted from polarities is a constraint, not a")
    print("  measurement, even when the data are perfect.")

    n_flip = int(round(FLIP_FRACTION * N_STATIONS))
    idx = RNG.choice(N_STATIONS, size=n_flip, replace=False)
    obs_noisy = obs.copy()
    obs_noisy[idx] *= -1.0
    mis_n = misfit_grid(dirs, obs_noisy, tensors)
    best_n = int(np.argmin(mis_n))
    print()
    print(f"  (b) {n_flip} of {N_STATIONS} polarities flipped "
          f"({100 * n_flip / N_STATIONS:.0f} per cent)")
    print(f"      best mechanism: strike {strikes[best_n]:.0f}, dip "
          f"{dips[best_n]:.0f}, rake {rakes[best_n]:.0f}, "
          f"misfit {mis_n[best_n]:.3f}")
    print(f"      tensor difference from the truth: "
          f"{tensor_distance(tensors[best_n], m_true_unit):.4f}")
    print("      The misfit it cannot remove is of the order of the injected flip")
    print("      fraction: the inversion recovers a mechanism close to the truth,")
    print("      and the distance from the truth grows with the noise.")

    section("4. The family of mechanisms that fit equally well")
    tol = mis_n[best_n] + ACCEPT_EXTRA
    accept = np.where(mis_n <= tol)[0]
    acc_dist = np.array([tensor_distance(tensors[i], m_true_unit)
                         for i in accept])
    print(f"  accept every mechanism with misfit <= {tol:.3f} "
          f"(the best plus {ACCEPT_EXTRA:.2f}):")
    print(f"    {accept.size} of {mis_n.size} grid mechanisms "
          f"({100 * accept.size / mis_n.size:.2f} per cent of the grid)")
    print(f"    tensor distance from the true mechanism: "
          f"{acc_dist.min():.4f} to {acc_dist.max():.4f} "
          f"(mean {acc_dist.mean():.4f})")
    print(f"    accepted strikes span {strikes[accept].min():.0f} to "
          f"{strikes[accept].max():.0f} deg, dips {dips[accept].min():.0f} to "
          f"{dips[accept].max():.0f} deg,")
    print(f"    rakes {rakes[accept].min():.0f} to {rakes[accept].max():.0f} deg")
    print()
    print("  This family is the honest answer to a focal-mechanism inversion:")
    print("  not one triple but a set of tensors, here spanning unit-tensor")
    print("  distances up to the printed maximum.  Report the count and the")
    print("  distances, or report a single mechanism and be wrong about how well")
    print("  it is known.")
    print()
    fewer = station_directions(8)
    obs_few = polarities(fewer, m)
    flip_few = RNG.choice(8, size=max(1, int(round(FLIP_FRACTION * 8))),
                          replace=False)
    obs_few[flip_few] *= -1.0
    mis_few = misfit_grid(fewer, obs_few, tensors)
    best_few = int(np.argmin(mis_few))
    acc_few = np.where(mis_few <= mis_few[best_few] + ACCEPT_EXTRA)[0]
    dist_few = np.array([tensor_distance(tensors[i], m_true_unit)
                         for i in acc_few])
    print(f"  the same experiment with 8 stations instead of {N_STATIONS}:")
    print(f"    best misfit {mis_few[best_few]:.3f}, accepted family "
          f"{acc_few.size} mechanisms "
          f"({100 * acc_few.size / mis_few.size:.1f} per cent of the grid)")
    print(f"    tensor distance from the truth: {dist_few.min():.4f} to "
          f"{dist_few.max():.4f}, against {acc_dist.min():.4f} to "
          f"{acc_dist.max():.4f} with {N_STATIONS} stations")
    print("  Fewer stations, a wider family of tensors.  This is the honest")
    print("  trade: a focal mechanism from a sparse network is a constraint, not")
    print("  a measurement, and it should be quoted with the alternatives attached.")

    section("5. The moment tensor decomposed, with a round-trip check")
    pct, vals, rebuilt = decompose(m)
    err = np.max(np.abs(rebuilt - m)) / np.max(np.abs(m))
    print("  pure double couple (Section 1):")
    print(f"    ISO {pct[0]:+8.2f} %   DC {pct[1]:8.2f} %   CLVD {pct[2]:+8.2f} %")
    print(f"    round-trip rebuild error = {err:.2e} (relative, max component)")
    print()
    dc_unit = moment_tensor(210.0, 60.0, 30.0, 1.0)
    clvd_unit = np.diag([2.0, -1.0, -1.0]) / 3.0
    mixed = 0.55 * dc_unit + 0.30 * clvd_unit + 0.15 * np.eye(3)
    pct, vals, rebuilt = decompose(mixed)
    err = np.max(np.abs(rebuilt - mixed)) / np.max(np.abs(mixed))
    print("  a deliberately mixed tensor, built as")
    print("    0.55 x double couple + 0.30 x CLVD + 0.15 x isotropic:")
    print(f"    eigenvalues {np.array2string(vals, precision=4)}")
    print(f"    ISO {pct[0]:+8.2f} %   DC {pct[1]:8.2f} %   CLVD {pct[2]:+8.2f} %")
    print(f"    round-trip rebuild error = {err:.2e} (relative, max component)")
    print()
    print("  The split is exactly reversible, so the three percentages are a")
    print("  complete description of the tensor.  Read them as a decomposition of")
    print("  the DATA, not as physics: a real fault slips on a plane, so a large")
    print("  CLVD percentage is far more often a sign of a poor velocity model, a")
    print("  mislocated event or a noisy inversion than of a real")
    print("  non-double-couple source.  Reporting the percentages without that")
    print("  sentence is the standard way this quantity is misused.")
    print()
    print(f"  for the synthetic event, M0 = {M0_TRUE:.2e} N m gives "
          f"Mw = {mw_from_m0(M0_TRUE):.2f}")
    print()
    print("=" * 72)
    print("Mechanism, stations and polarity errors are SYNTHETIC.  The moment")
    print("tensor formulas are standard and are verified in Section 1.")
    print("=" * 72)


if __name__ == "__main__":
    main()
