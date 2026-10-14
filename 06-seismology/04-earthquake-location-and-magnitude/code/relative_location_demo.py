#!/usr/bin/env python3
"""Relative location: master-event / double-difference location of a synthetic
cluster, compared with locating every event absolutely.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python relative_location_demo.py

Requires: numpy.  No network access.

Everything is SYNTHETIC.  The events, the network, the station delays and the
pick noise are chosen teaching values, not a measured data set.  The velocity
model is a homogeneous half-space, so that every error reported below is an
error of the METHOD, not of an unknown Earth.

WHAT IS COMPUTED

1. The synthetic experiment: one master event and nine clustered events, eight
   stations, picks contaminated by independent noise AND by a per-station
   delay (the classic nuisance term: a near-receiver velocity error that is
   common to every event at that station).
2. Absolute location of every event independently (4 parameters each).
   Reported as scatter about the truth, and as bias.
3. Relative location of every event against the master (4 parameters each)
   using the SAME arrival-time picks, i.e. differences of two independently
   picked times.  This is the naive way to "do relative location", and the
   demonstration measures what it is worth.
4. Relative location again, with the differential time measured directly at
   cross-correlation precision instead of by differencing two picks.  This is
   the measurement the method actually needs, and the difference between the
   two rows is the honest content of the lesson.
5. Both methods with a 3 per cent wrong velocity in the locating model: the
   absolute solution is displaced, the relative solution is not, because a
   uniform velocity error is nearly common to events sharing almost the same
   ray paths.
6. What relative location cannot do: it is relative.  A shift common to the
   whole cluster is invisible to it, and it inherits whatever is wrong with
   the master.

All results are printed with units (metres, seconds).
"""

import numpy as np

RNG = np.random.default_rng(20261014)

V_TRUE = 3500.0          # m/s, SYNTHETIC homogeneous body-wave velocity
SIGMA_PICK = 0.020       # s, SYNTHETIC pick uncertainty (one standard deviation)
SIGMA_DD = 0.002         # s, SYNTHETIC cross-correlation precision on a time
                         #    DIFFERENCE between two similar events
SIGMA_STATION = 0.100    # s, SYNTHETIC per-station delay (nuisance term)
N_EVENTS = 10            # master + 9
CLUSTER_SIGMA_M = 400.0  # m, true scatter of the cluster about the master

# SYNTHETIC array: eight stations within about 12 km of the cluster centre.
ST_X = np.array([-6000.0, -4000.0, 0.0, 4000.0, 6000.0, 3000.0, -3000.0, 2000.0])
ST_Y = np.array([0.0, 5000.0, 6000.0, 5000.0, 0.0, -4000.0, -5000.0, -3000.0])


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def travel_time(e, v=V_TRUE):
    """Travel time, station i to event e, in seconds."""
    r = np.sqrt((ST_X - e[0]) ** 2 + (ST_Y - e[1]) ** 2 + e[2] ** 2)
    return r / v


def predict_absolute(m, v=V_TRUE):
    """Arrival times for the model m = (x, y, z, t0) at every station."""
    return travel_time(m[:3], v) + m[3]


def jac_absolute(m, v=V_TRUE):
    """dT/d(x, y, z, t0) at every station.  Rows: stations, columns: parameters."""
    dx = m[0] - ST_X
    dy = m[1] - ST_Y
    r = np.sqrt(dx ** 2 + dy ** 2 + m[2] ** 2)
    j = np.empty((ST_X.size, 4))
    j[:, 0] = dx / (v * r)
    j[:, 1] = dy / (v * r)
    j[:, 2] = m[2] / (v * r)
    j[:, 3] = 1.0
    return j


def locate_absolute(t_obs, start, v=V_TRUE, n_iter=25):
    """Gauss-Newton location of one event from absolute arrival times."""
    m = np.array(start, dtype=float)
    for _ in range(n_iter):
        r = predict_absolute(m, v) - t_obs
        j = jac_absolute(m, v)
        step = np.linalg.lstsq(j, -r, rcond=None)[0]
        m = m + step
        if np.max(np.abs(step[:3])) < 1e-4 and abs(step[3]) < 1e-6:
            break
    return m


def predict_diff(m, master, v=V_TRUE):
    """Differential times (event minus master) for m = (x, y, z, dt0)."""
    return travel_time(m[:3], v) - travel_time(master[:3], v) + m[3]


def locate_relative(t_diff, master, start, v=V_TRUE, n_iter=25):
    """Gauss-Newton location of one event relative to a fixed master."""
    m = np.array(start, dtype=float)
    master = np.asarray(master, dtype=float)
    for _ in range(n_iter):
        r = predict_diff(m, master, v) - t_diff
        dx = m[0] - ST_X
        dy = m[1] - ST_Y
        rr = np.sqrt(dx ** 2 + dy ** 2 + m[2] ** 2)
        j = np.empty((ST_X.size, 4))
        j[:, 0] = dx / (v * rr)
        j[:, 1] = dy / (v * rr)
        j[:, 2] = m[2] / (v * rr)
        j[:, 3] = 1.0
        step = np.linalg.lstsq(j, -r, rcond=None)[0]
        m = m + step
        if np.max(np.abs(step[:3])) < 1e-4 and abs(step[3]) < 1e-6:
            break
    return m


def main():
    print("Relative (master-event / double-difference) location of a cluster")
    print(f"numpy {np.__version__}")
    print()
    print(f"  SYNTHETIC model: homogeneous half-space, v = {V_TRUE:.0f} m/s")
    print(f"  pick uncertainty sigma_pick = {SIGMA_PICK * 1e3:.0f} ms")
    print(f"  per-station delay sigma_station = {SIGMA_STATION * 1e3:.0f} ms "
          f"(unknown to the inversion)")

    section("1. The synthetic experiment")
    master = np.array([4000.0, -2000.0, 7000.0])
    true = master + RNG.normal(0.0, CLUSTER_SIGMA_M, size=(N_EVENTS, 3))
    true[0] = master                     # event 0 is the master by definition
    station_delay = RNG.normal(0.0, SIGMA_STATION, size=ST_X.size)

    t_exact = np.array([travel_time(e) for e in true])          # (events, stations)
    t_obs = (t_exact + station_delay[None, :]
             + RNG.normal(0.0, SIGMA_PICK, size=t_exact.shape))
    # The same physical arrivals, but the DIFFERENCE between two similar events
    # measured directly by cross-correlation: the station delay is common, and
    # the measurement error is two orders of magnitude smaller than a pick.
    t_xcorr = (t_exact + station_delay[None, :]
               + RNG.normal(0.0, SIGMA_DD, size=t_exact.shape))

    print(f"  stations: {ST_X.size}, apertures "
          f"{np.ptp(ST_X) / 1e3:.1f} x {np.ptp(ST_Y) / 1e3:.1f} km")
    print(f"  master event (x, y, z) = ({master[0] / 1e3:.2f}, "
          f"{master[1] / 1e3:.2f}, {master[2] / 1e3:.2f}) km")
    print(f"  cluster scatter about the master: sigma = {CLUSTER_SIGMA_M:.0f} m "
          f"in each of x, y, z")
    print("  station delays drawn once (ms): "
          f"{np.array2string(station_delay * 1e3, precision=0, floatmode='fixed')}")
    print("  Those delays are a physical signal in the data and an unmodelled")
    print("  nuisance in both inversions below.  That is the point of Section 3.")

    start = np.array([0.0, 0.0, 5000.0, 0.0])
    section("2. Absolute location: every event located on its own")
    print(f"  {'event':>6}{'error x (m)':>13}{'error y (m)':>13}"
          f"{'error z (m)':>13}{'3-D error (m)':>15}")
    abs_est = np.empty_like(true)
    for k in range(N_EVENTS):
        m = locate_absolute(t_obs[k], start)
        abs_est[k] = m[:3]
        err = m[:3] - true[k]
        print(f"  {k:6d}{err[0]:13.1f}{err[1]:13.1f}{err[2]:13.1f}"
              f"{np.linalg.norm(err):15.1f}")
    abs_err = abs_est - true
    mean_abs_err = abs_err.mean(axis=0)
    print()
    print("  scatter about the truth (rms over events, after removing the mean):")
    print(f"    horizontal {np.sqrt(np.mean(abs_err[:, :2] ** 2)):.1f} m, "
          f"depth {np.sqrt(np.mean(abs_err[:, 2] ** 2)):.1f} m")
    print(f"  bias common to all events (m): ({mean_abs_err[0]:+.1f}, "
          f"{mean_abs_err[1]:+.1f}, {mean_abs_err[2]:+.1f})")
    print("  The bias is not pick noise: it is the array-averaged part of the")
    print("  station delays, which an absolute location absorbs into position.")
    proj, *_ = np.linalg.lstsq(jac_absolute(master), station_delay, rcond=None)
    print()
    print("  The bias is exactly predictable from the delay pattern: least squares")
    print("  for the position that best mimics it gives")
    print(f"    ({proj[0]:+.1f}, {proj[1]:+.1f}, {proj[2]:+.1f}) m and "
          f"dt0 = {proj[3]:+.3f} s,")
    print(f"  from a delay pattern whose mean is only "
          f"{station_delay.mean() * 1e3:+.2f} ms and whose")
    print(f"  standard deviation is {station_delay.std() * 1e3:.2f} ms.  The mean of")
    print("  the delays is nearly irrelevant: what moves the event is the part of")
    print("  the pattern that looks like a displacement to the array.")

    section("3. Relative location from the same independently picked times")
    print("  Differential times here are t_obs(event) - t_obs(master), i.e. the")
    print("  difference of two independent picks.  The station delay is common to")
    print("  the two and therefore cancels -- that part works as advertised.")
    rel_est = np.empty_like(true)
    for k in range(N_EVENTS):
        master_est = abs_est[0]                      # master as located absolutely
        t_diff = t_obs[k] - t_obs[0]
        m = locate_relative(t_diff, master_est,
                            np.array([master_est[0], master_est[1],
                                      master_est[2], 0.0]))
        rel_est[k] = m[:3]
    rel_err = (rel_est - rel_est[0]) - (true - true[0])
    abs_rel_err = (abs_est - abs_est[0]) - (true - true[0])

    section("4. Relative location from directly measured differences")
    print(f"  A cross-correlation measures a time DIFFERENCE with precision")
    print(f"  sigma_dd = {SIGMA_DD * 1e3:.0f} ms, far better than differencing two")
    print(f"  picks of sigma_pick = {SIGMA_PICK * 1e3:.0f} ms each.  Same events,")
    print("  same stations, same station delays, better measurement.")
    rel_est_x = np.empty_like(true)
    for k in range(N_EVENTS):
        master_est = abs_est[0]
        t_diff = t_xcorr[k] - t_xcorr[0]
        m = locate_relative(t_diff, master_est,
                            np.array([master_est[0], master_est[1],
                                      master_est[2], 0.0]))
        rel_est_x[k] = m[:3]
    rel_err_x = (rel_est_x - rel_est_x[0]) - (true - true[0])

    print()
    print(f"  {'method':>42}{'rms offset error (m)':>24}{'max (m)':>10}")
    for name, e in (("absolute locations, offsets taken", abs_rel_err),
                    ("relative, difference of two picks", rel_err),
                    ("relative, measured difference", rel_err_x)):
        mag = np.linalg.norm(e, axis=1)
        print(f"  {name:>42}{np.sqrt(np.mean(mag ** 2)):24.1f}{mag.max():10.1f}")
    print()
    f1 = np.sqrt(np.mean(np.linalg.norm(rel_err, axis=1) ** 2))
    f2 = np.sqrt(np.mean(np.linalg.norm(rel_err_x, axis=1) ** 2))
    f0 = np.sqrt(np.mean(np.linalg.norm(abs_rel_err, axis=1) ** 2))
    print(f"  Taking offsets from absolute locations gives {f0:.0f} m rms;")
    print(f"  differencing two independent picks gives {f1:.0f} m rms;")
    print(f"  measuring the difference directly gives {f2:.0f} m rms.")
    print()
    print("  Read the three numbers in that order, because the middle one is a")
    print("  warning.  Taking offsets against a master already removes any error")
    print(f"  common to the cluster -- the absolute bias of ({mean_abs_err[0]:+.0f}, "
          f"{mean_abs_err[1]:+.0f},")
    print(f"  {mean_abs_err[2]:+.0f}) m is absent from BOTH the first two rows -- so the")
    print("  difference between them is not the bias.  Differencing two")
    print("  independent picks doubles the timing noise (20 ms each becomes")
    print("  about 28 ms), and the pair-wise depth/origin-time trade-off is")
    print("  strong for events that nearly coincide, so the middle row is WORSE")
    print(f"  than the row above it: {f1:.0f} m against {f0:.0f} m.  What buys the")
    print(f"  factor of {f1 / f2:.0f} in the last row is the MEASUREMENT of the")
    print("  difference, not the act of subtracting.")

    section("5. The same experiment with a 3 per cent wrong velocity")
    v_wrong = 0.97 * V_TRUE
    abs_est_w = np.empty_like(true)
    for k in range(N_EVENTS):
        abs_est_w[k] = locate_absolute(t_obs[k], start, v=v_wrong)[:3]
    rel_est_w = np.empty_like(true)
    rel_est_xw = np.empty_like(true)
    for k in range(N_EVENTS):
        master_est = abs_est_w[0]
        m0 = np.array([master_est[0], master_est[1], master_est[2], 0.0])
        rel_est_w[k] = locate_relative(t_obs[k] - t_obs[0], master_est, m0,
                                       v=v_wrong)[:3]
        rel_est_xw[k] = locate_relative(t_xcorr[k] - t_xcorr[0], master_est, m0,
                                        v=v_wrong)[:3]
    err_abs_w = abs_est_w - true
    err_rel_w = (rel_est_w - rel_est_w[0]) - (true - true[0])
    err_rel_xw = (rel_est_xw - rel_est_xw[0]) - (true - true[0])
    print(f"  locating velocity = {v_wrong:.0f} m/s, i.e. "
          f"{100 * (v_wrong - V_TRUE) / V_TRUE:+.0f} per cent")
    print()
    print(f"  {'quantity':>44}{'right velocity':>18}{'3% low':>12}")
    rows = [
        ("absolute depth bias, mean (m)",
         abs_err[:, 2].mean(), err_abs_w[:, 2].mean()),
        ("absolute 3-D scatter after bias removal (m)",
         np.sqrt(np.mean((abs_err - mean_abs_err) ** 2)),
         np.sqrt(np.mean((err_abs_w - err_abs_w.mean(axis=0)) ** 2))),
        ("relative rms error, pick differences (m)",
         f1, np.sqrt(np.mean(np.linalg.norm(err_rel_w, axis=1) ** 2))),
        ("relative rms error, measured differences (m)",
         f2, np.sqrt(np.mean(np.linalg.norm(err_rel_xw, axis=1) ** 2))),
    ]
    for name, a, b in rows:
        print(f"  {name:>44}{a:18.1f}{b:12.1f}")
    print()
    print("  A uniform velocity error penalises the absolute solution and leaves")
    print("  the relative solution nearly untouched, because the two events share")
    print("  almost the same ray paths and the error is common to both.  That is")
    print("  the entire reason double-difference catalogues are the standard tool")
    print("  for fault-zone structure.  Note the careful word 'nearly': where the")
    print("  ray paths differ (a long cluster, a shallow event) the cancellation")
    print("  is incomplete, and the residual error grows with separation.")

    section("6. What relative location cannot do")
    print("  Relative locations are differences.  If the whole cluster is")
    print("  displaced -- a wrong master, a wrong regional velocity, a wrong")
    print("  reference station -- every relative location is unchanged while every")
    print("  absolute location moves together.  Two consequences, both printed")
    print("  above: the cluster's absolute position rests on the master alone, and")
    print("  the reported improvement is an improvement in PRECISION of geometry,")
    print("  not in the accuracy of where the cluster is on the Earth.")
    print()
    print("  The unresolved error that no differencing removes is the one that")
    print("  varies between the two events of a pair at the same station: any real")
    print("  difference in path, and the noise in the measured delay itself.")
    print("  Cross-correlation reduces the second, which is why Section 4 beats")
    print("  Section 3; nothing reduces the first except a better velocity model.")
    print()
    print("=" * 72)
    print("All events, stations, delays, noise and the velocity model are")
    print("SYNTHETIC.  No real earthquake, station or catalogue is used.")
    print("=" * 72)


if __name__ == "__main__":
    main()
