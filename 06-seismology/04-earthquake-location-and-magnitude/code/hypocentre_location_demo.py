"""Hypocentre location as a least-squares problem, with conditioning.

Run:  .venv/bin/python hypocentre_location_demo.py
Requires: numpy, obspy.

Companion to lesson 06-04-01.

WHAT IS COMPUTED

1. The Jacobian.  For a homogeneous half-space the travel time from a source
   at (x, y, z) to a station at (xi, yi, 0) is
       T = sqrt((xi-x)^2 + (yi-y)^2 + z^2) / v ,
   so the derivatives are available in closed form, using the ray parameter
   unit vector u = ((xi-x), (yi-y), z)/r:
       dT/dx = -u_x / v ,  dT/dy = -u_y / v ,  dT/dz = +u_z / v ,
       dT/dt0 = 1 .
   Each analytic derivative is checked against a central finite difference.

2. The trade-off between depth and origin time.  For a surface array the
   columns dT/dz and dT/dt0 are nearly parallel, because at regional distances
   u_z is nearly the same for every station.  The script measures the cosine
   between the two columns, the condition number of the normal matrix, and the
   null direction of J^T J.

3. A synthetic location.  With exact travel times, Gauss-Newton recovers the
   true hypocentre; the script reports the iteration count, the final residual
   and the difference from the truth.

4. The confidence ellipsoid.  sigma^2 (J^T J)^-1 is formed with a chosen pick
   uncertainty, and the 95 per cent semi-axes are reported.  A single-station
   problem is demonstrated to be exactly singular.

All parameters are SYNTHETIC and printed.  The velocity model is a homogeneous
half-space chosen for tractability, and the lesson says what that costs.
"""

import numpy as np

V = 6000.0            # m/s, SYNTHETIC homogeneous P velocity
SIGMA_T = 0.05        # s, SYNTHETIC pick uncertainty (one standard deviation)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def travel_time(m, x, y, z, t0):
    dx, dy = x - m[0], y - m[1]
    return t0 + np.sqrt(dx ** 2 + dy ** 2 + z ** 2) / V


def jacobian(m, x, y, z, t0):
    """Rows: one per station.  Columns: dx, dy, dz, dt0."""
    dx, dy = x - m[0], y - m[1]
    r = np.sqrt(dx ** 2 + dy ** 2 + z ** 2)
    j = np.empty((len(x), 4))
    j[:, 0] = -dx / (V * r)
    j[:, 1] = -dy / (V * r)
    j[:, 2] = z / (V * r)
    j[:, 3] = 1.0
    return j


def main():
    print("Hypocentre location as a least-squares problem")
    print(f"numpy {np.__version__}")
    print()
    print(f"  SYNTHETIC model: homogeneous half-space, v = {V:.0f} m/s,")
    print(f"  pick uncertainty sigma_t = {SIGMA_T:.3f} s")

    truth = np.array([12.0e3, -8.0e3, 7.5e3])     # x, y, z (z positive down)
    t0_true = 1.50                                # s

    section("1. The Jacobian, analytic against finite difference")
    x = np.array([-30e3, -20e3, -10e3, 0.0, 10e3, 20e3, 30e3])
    y = np.array([40e3, 20e3, 5e3, -5e3, -20e3, -40e3, 0.0]) + 12e3
    j_an = jacobian(truth, x, y, truth[2], t0_true)
    h = 1.0
    j_fd = np.empty_like(j_an)
    for k in range(3):
        mp = truth.copy()
        mn = truth.copy()
        mp[k] += h
        mn[k] -= h
        # travel_time takes the depth explicitly, so it must be the perturbed
        # depth, not truth[2]: otherwise the depth column is differenced at a
        # fixed depth and collapses to zero.
        j_fd[:, k] = (travel_time(mp, x, y, mp[2], t0_true)
                      - travel_time(mn, x, y, mn[2], t0_true)) / (2 * h)
    j_fd[:, 3] = 1.0
    print(f"  {'station':>8}{'dT/dx an':>14}{'dT/dx fd':>14}"
          f"{'dT/dz an':>14}{'dT/dz fd':>14}")
    for i in range(len(x)):
        print(f"  {i:8d}{j_an[i,0]:14.3e}{j_fd[i,0]:14.3e}"
              f"{j_an[i,2]:14.3e}{j_fd[i,2]:14.3e}")
    print()
    print(f"  worst relative difference between analytic and finite-difference")
    print(f"  derivatives (s/m) = {np.max(np.abs(j_an-j_fd)):.3e}")
    print("  (units: seconds per metre for the spatial columns, dimensionless for")
    print("  the origin-time column.)")

    section("2. The depth / origin-time trade-off")
    print("  Columns 2 (depth) and 3 (origin time) of the Jacobian:")
    print()
    cosine = float(j_an[:, 2] @ j_an[:, 3]
                   / (np.linalg.norm(j_an[:, 2]) * np.linalg.norm(j_an[:, 3])))
    print(f"  cosine between dT/dz and dT/dt0 = {cosine:.6f}")
    print("  Compare column 2 with column 3: if the depth were resolved, this")
    print("  cosine would be far from 1.")
    print()
    print(f"  {'array':>28}{'cos(dT/dz, dt0)':>17}{'rank':>6}"
          f"{'null dim':>10}{'cond(J^T J)':>14}{'corr(dz, dt0)':>15}")
    arrays = [("7 stations, apertures 60 km", x, y)]
    # a tight array and a single station, for contrast
    xt = np.array([-2e3, -1e3, 0.0, 1e3, 2e3])
    yt = np.array([-2e3, -1e3, 0.0, 1e3, 2e3]) + 12e3
    arrays.append(("5 stations, aperture 4 km", xt, yt))
    arrays.append(("1 station", np.array([0.0]), np.array([12e3])))
    for (name, xa, ya) in arrays:
        ja = jacobian(truth, xa, ya, truth[2], t0_true)
        cos_a = float(ja[:, 2] @ ja[:, 3]
                      / (np.linalg.norm(ja[:, 2]) * np.linalg.norm(ja[:, 3])))
        nrm = ja.T @ ja
        sv = np.linalg.svd(ja, compute_uv=False)
        rank = int(np.sum(sv > sv[0] * 1e-12))
        null_dim = 4 - rank
        cond = (sv[0] ** 2 / sv[rank - 1] ** 2 if (rank > 0 and null_dim == 0)
                else np.inf)
        # conditional covariance using only the resolved subspace
        cov = SIGMA_T ** 2 * np.linalg.pinv(nrm)
        if null_dim == 0:
            corr = cov[2, 3] / np.sqrt(cov[2, 2] * cov[3, 3])
            corr_s = f"{corr:+15.6f}"
        else:
            corr_s = f"{'--':>15}"
        print(f"  {name:>28}{cos_a:17.6f}{rank:6d}{null_dim:10d}"
              f"{cond:14.3e}{corr_s}")
    print()
    print("  Read the columns in order.  With a single arrival the Jacobian has")
    print("  rank 1 out of 4, so three directions in parameter space are entirely")
    print("  unconstrained: one arrival time cannot separate distance from origin")
    print("  time, and the whole distance-origin-time family is a null direction.")
    print("  A tight aperture removes the numerical singularity but not the")
    print("  trade-off: cos(dT/dz, dt0) = 0.9998, because every station then looks")
    print("  down very nearly the same ray.  The wide array has the smallest")
    print("  cosine and the smallest condition number.")
    print()
    print("  The last column is the correlation between the recovered depth and")
    print("  origin time.  A value near +/-1 means the data cannot tell a deeper")
    print("  event later from a shallower event earlier.")

    section("3. Synthetic location by Gauss-Newton")
    m = np.array([20.0e3, 0.0, 15.0e3, 0.0])       # a deliberately wrong start
    t_obs = np.array([travel_time(truth, xi, yi, truth[2], t0_true)
                      for xi, yi in zip(x, y)])
    print(f"  true hypocentre (x, y, z) = ({truth[0]/1e3:.1f}, "
          f"{truth[1]/1e3:.1f}, {truth[2]/1e3:.1f}) km, t0 = {t0_true:.3f} s")
    print(f"  start           (x, y, z) = ({m[0]/1e3:.1f}, {m[1]/1e3:.1f}, "
          f"{m[2]/1e3:.1f}) km, t0 = {m[3]:.3f} s")
    print()
    print(f"  {'iter':>5}{'x (km)':>10}{'y (km)':>10}{'z (km)':>10}"
          f"{'t0 (s)':>10}{'rms residual (s)':>18}")
    for it in range(12):
        r = np.array([travel_time(m[:3], xi, yi, m[2], m[3]) - to
                      for xi, yi, to in zip(x, y, t_obs)])
        rms = float(np.sqrt(np.mean(r ** 2)))
        print(f"  {it:5d}{m[0]/1e3:10.4f}{m[1]/1e3:10.4f}{m[2]/1e3:10.4f}"
              f"{m[3]:10.4f}{rms:18.3e}")
        if rms < 1e-9:
            break
        j = jacobian(m[:3], x, y, m[2], m[3])
        dm = np.linalg.lstsq(j, -r, rcond=None)[0]
        m = m + dm
    print()
    print(f"  recovered hypocentre minus truth (m): "
          f"({m[0]-truth[0]:+.3e}, {m[1]-truth[1]:+.3e}, {m[2]-truth[2]:+.3e})")
    print(f"  recovered origin time minus truth (s): {m[3]-t0_true:+.3e}")
    print("  Gauss-Newton on exact data converges to the exact answer, which is")
    print("  the only thing this part of the demonstration claims.")

    section("4. The 95 per cent confidence ellipsoid")
    j = jacobian(truth, x, y, truth[2], t0_true)
    cov = SIGMA_T ** 2 * np.linalg.inv(j.T @ j)
    vals, vecs = np.linalg.eigh(cov)
    order = np.argsort(vals)[::-1]
    vals, vecs = vals[order], vecs[:, order]
    # chi-square with 4 degrees of freedom, 95 per cent
    chi2_r4_95 = 9.4877
    print(f"  assuming independent Gaussian picks with sigma = {SIGMA_T:.3f} s,")
    print("  and the CORRECT velocity model, the covariance is sigma^2 (J^T J)^-1")
    print(f"  and the 95 per cent ellipsoid in 4 parameters uses chi2 = "
          f"{chi2_r4_95}")
    print()
    print(f"  {'semi-axis':>10}{'length (m or s)':>18}   direction (x, y, z, t0)")
    labels = ("dx", "dy", "dz", "dt0")
    for i in range(4):
        semi = np.sqrt(chi2_r4_95 * vals[i])
        v = vecs[:, i]
        norm = np.linalg.norm(v)
        v = v / norm * (1.0 if v[3] > 0 else -1.0)
        print(f"  {labels[i]:>10}{semi:18.4f}   "
              f"({v[0]:+.4f}, {v[1]:+.4f}, {v[2]:+.4f}, {v[3]:+.4f})")
    print()
    corr = cov[2, 3] / np.sqrt(cov[2, 2] * cov[3, 3])
    print("  The longest semi-axis is the direction in which the data are least")
    print("  informative; here its components are horizontal and depth, with")
    print("  essentially no origin-time part, so for this array the poorly")
    print("  resolved direction is source geometry rather than source time.")
    print()
    print(f"  The depth/origin-time correlation, corr(dz, dt0) = {corr:+.4f}.")
    print("  That single number is the trade-off: a correlation of 1 would mean")
    print("  the two parameters are indistinguishable, 0 that they are separate.")
    print("  Compare it with the single-station case, where the trade-off is exact")
    print("  and no correlation of this kind can even be formed.")
    print()
    print("  Every number in this section is conditional on three assumptions")
    print("  that are all false in practice: Gaussian pick errors, a correct")
    print("  velocity model, and errors that are independent between stations.")
    print("  Lesson 06-04-02 shows what the second one costs.")
    print()
    print("=" * 72)
    print("All parameters SYNTHETIC.  The velocity model is a homogeneous")
    print("half-space, so the travel times are exact and the experiment measures")
    print("the inversion, not the Earth.")
    print("=" * 72)


if __name__ == "__main__":
    main()
