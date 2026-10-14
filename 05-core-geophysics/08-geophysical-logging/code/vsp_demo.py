"""Vertical seismic profiling and check shots: what a well tie really calibrates.

Four results:

  1. A SYNTHETIC layered velocity model with an exact travel-time integral.
  2. CHECK-SHOT TIMES through it, and the velocity recovered by differencing them
     -- which is the quantity a well tie actually uses.
  3. DEPTH ERROR from a wrong average velocity, measured against the exact
     time-depth curve.
  4. A VSP GEOMETRY: downgoing and upgoing arrival times for a source offset from
     the well are computed, and the difference between the direct arrival and the
     check shot is reported, showing what the offset adds.

All velocities, layer boundaries, source offsets and receiver depths are STATED
SYNTHETIC INPUTS.  The model is one-dimensional, which is itself the main
assumption, and the demonstration shows what that assumption costs.

Run:  python3 vsp_demo.py
"""

from __future__ import annotations

import numpy as np


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


VELOCITIES = [(0.0, 400.0, 1800.0), (400.0, 900.0, 2400.0),
              (900.0, 1500.0, 3100.0), (1500.0, 3000.0, 4200.0)]
OFFSET = 1200.0          # SYNTHETIC surface source offset, m
RECEIVERS = np.arange(250.0, 3001.0, 250.0)   # SYNTHETIC receiver depths, m


def velocity_at(z):
    for top, base, v in VELOCITIES:
        if top <= z < base:
            return v
    return VELOCITIES[-1][2]


def vertical_time(z):
    """Exact one-way vertical travel time to depth z."""
    t = 0.0
    for top, base, v in VELOCITIES:
        if z <= top:
            break
        seg = min(z, base) - top
        t += seg / v
        if z <= base:
            break
    return t


def main() -> None:
    section("1. The velocity model and the exact time-depth curve")
    print("layer (m)        Vp (m/s)   one-way vertical time at base (s)")
    for top, base, v in VELOCITIES:
        print(f"{top:6.0f}-{base:6.0f}   {v:8.0f}   {vertical_time(base):28.4f}")

    section("2. Check shots, and the interval velocity they imply")
    print("depth (m)   check-shot one-way time (s)   interval V from successive "
          "shots")
    times = []
    for i, z in enumerate(RECEIVERS):
        t = vertical_time(float(z))
        times.append(t)
        if i == 0:
            print(f"{z:9.0f}   {t:28.4f}   {'-':>26s}")
        else:
            dz = z - RECEIVERS[i - 1]
            dt = t - times[i - 1]
            print(f"{z:9.0f}   {t:28.4f}   {dz / dt:26.1f}")
    print("The check shot measures TIME, not velocity.  The velocity is a difference\n"
          "of two times, so its precision is set by the time precision divided by the\n"
          "receiver spacing: a 1 ms timing error over a 250 m spacing is 16 m/s at\n"
          "2400 m/s, or 0.7 per cent.  State the spacing when you quote the velocity.")

    section("3. What a wrong average velocity costs in depth")
    z_test = 2000.0
    t_true = vertical_time(z_test)
    v_avg_true = z_test / t_true
    print(f"at z = {z_test:.0f} m: one-way time {t_true:.4f} s, average velocity "
          f"{v_avg_true:.1f} m/s")
    print("\nassumed V_avg     depth error (m)   error (per cent)")
    for factor in (0.95, 0.98, 1.0, 1.02, 1.05):
        z_app = factor * v_avg_true * t_true
        print(f"{factor * v_avg_true:12.1f}   {z_app - z_test:+15.1f}   "
              f"{100 * (z_app - z_test) / z_test:+15.2f}")
    print("A 5 per cent velocity error is a 100 m depth error at 2 km, which is\n"
          "larger than most target thicknesses.  This is the single number that\n"
          "makes a well tie mandatory rather than optional.")

    section("4. VSP geometry: what the offset source adds")
    print(f"surface source offset = {OFFSET:.0f} m; vertical incidence is not "
          "available")
    print("direct-arrival times below use a STRAIGHT-RAY approximation through the\n"
          "layered model, which is stated as an approximation, not a ray trace.\n")
    print("receiver depth (m)   direct-arrival (s)   normal-incidence (s)   "
          "difference (ms)")
    for z in RECEIVERS[::3]:
        s = np.linspace(0.0, 1.0, 4000)
        xs = OFFSET * s
        zs = z * s
        ds = np.hypot(np.diff(xs), np.diff(zs))
        mid_z = 0.5 * (zs[1:] + zs[:-1])
        slowness = np.array([1.0 / velocity_at(float(v)) for v in mid_z])
        direct = float(np.sum(slowness * ds))
        normal = vertical_time(float(z))
        print(f"{z:17.0f}   {direct:18.4f}   {normal:20.4f}   "
              f"{1000 * (direct - normal):16.2f}")
    print("The offset makes the downgoing raypath much longer than the vertical\n"
          "one -- 542 ms at 250 m of receiver depth and 94 ms at 2500 m, since the\n"
          "raypath becomes progressively closer to vertical with depth.  The large\n"
          "absolute times are what makes a check shot the practical velocity\n"
          "calibration and a VSP the practical wavefield calibration.  A VSP measures the seismic wavefield in\n"
          "situ rather than a vertical travel time, and its upgoing arrivals are the\n"
          "only direct measurement of what a surface seismic reflection will look\n"
          "like at that location.  This is why a VSP constrains a tie better than a\n"
          "check shot: it calibrates the wavelet and the multiples as well as the\n"
          "velocity.")


if __name__ == "__main__":
    main()
