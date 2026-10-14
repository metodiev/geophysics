#!/usr/bin/env python3
"""Reference frames and plate motion: Euler poles, velocity fields, frame
rotations and the 14-parameter transformation of positions and velocities.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python itrf_and_plate_models_demo.py

All models and data in this module are SYNTHETIC.  The Euler poles, plate names,
rotation rates, station coordinates and frame-rotation rates below are chosen
teaching values.  No real terrestrial reference frame, plate model or station is
used, and no published pole or rate is quoted.

Contents
--------
1. An Euler pole, the angular velocity vector, and the velocity it predicts.
2. Inverting a synthetic velocity field for the Euler vector.
3. The observability of the radial component of the rotation from a network.
4. Two plates: the relative velocity across a boundary.
5. A frame rotation rate: what it does to apparent velocities.
6. A 14-parameter position-and-velocity transformation, applied and inverted.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

R_EARTH = 6371000.0                          # m, representative mean radius
MM = 1.0e-3
DEG_PER_MYR = np.pi / 180.0 / 1.0e6          # rad/yr per deg/Myr


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ecef(lat_deg, lon_deg, r=R_EARTH):
    lat, lon = np.radians(lat_deg), np.radians(lon_deg)
    return r * np.array([np.cos(lat) * np.cos(lon),
                         np.cos(lat) * np.sin(lon),
                         np.sin(lat)])


def enu_basis(lat_deg, lon_deg):
    lat, lon = np.radians(lat_deg), np.radians(lon_deg)
    east = np.array([-np.sin(lon), np.cos(lon), 0.0])
    north = np.array([-np.sin(lat) * np.cos(lon),
                      -np.sin(lat) * np.sin(lon), np.cos(lat)])
    up = np.array([np.cos(lat) * np.cos(lon),
                   np.cos(lat) * np.sin(lon), np.sin(lat)])
    return east, north, up


def omega_from_pole(lat_deg, lon_deg, rate_deg_per_myr):
    """Angular velocity vector in rad/yr from a pole position and rate."""
    return ecef(lat_deg, lon_deg, rate_deg_per_myr * DEG_PER_MYR)


def pole_from_omega(vec):
    rate = np.linalg.norm(vec)
    lat = np.degrees(np.arcsin(vec[2] / rate))
    lon = np.degrees(np.arctan2(vec[1], vec[0]))
    return lat, lon, rate / DEG_PER_MYR


def main():
    section("1. An Euler pole and the velocity field it predicts")
    pole_lat, pole_lon, rate = 50.0, -120.0, 0.90        # SYNTHETIC (deg, deg, deg/Myr)
    om = omega_from_pole(pole_lat, pole_lon, rate)
    print(f"SYNTHETIC pole: latitude {pole_lat:.1f} deg, longitude "
          f"{pole_lon:.1f} deg, rate {rate:.3f} deg/Myr")
    print(f"  angular velocity vector |Omega| = {np.linalg.norm(om):.6e} rad/yr")
    print(f"  one degree per million years = {DEG_PER_MYR:.6e} rad/yr = "
          f"{DEG_PER_MYR * R_EARTH / MM:.2f} mm/yr per Earth radius")
    stations = [(0.0, 0.0), (35.0, 20.0), (60.0, -100.0), (-40.0, 150.0)]
    print("   station lat/lon     east (mm/yr)   north (mm/yr)   up (mm/yr)   "
          "horizontal speed (mm/yr)")
    for lat, lon in stations:
        r = ecef(lat, lon)
        v = np.cross(om, r)
        e, n, u = enu_basis(lat, lon)
        ve, vn, vu = v @ e, v @ n, v @ u
        print(f"  {lat:6.1f} / {lon:7.1f}   {ve / MM:13.2f}   {vn / MM:12.2f}   "
              f"{vu / MM:11.2f}   {np.hypot(ve, vn) / MM:18.2f}")
    print("  The vertical component is identically zero: Omega x r is perpendicular")
    print("  to r, and the local up direction is r.  A rigid rotation therefore")
    print("  predicts no vertical motion at all, vertically moving stations require")
    print("  something else -- elastic strain, loading, or a non-rigid plate.")

    section("2. Inverting a synthetic velocity field for the Euler vector")
    net = [(10.0, 0.0), (30.0, 40.0), (45.0, -80.0), (-20.0, 120.0),
           (55.0, 10.0), (-35.0, -60.0), (5.0, -150.0), (70.0, 100.0)]
    rows, rhs = [], []
    for lat, lon in net:
        r = ecef(lat, lon)
        e, n, u = enu_basis(lat, lon)
        # dv = Omega x r, written as a linear map in Omega
        B = np.column_stack([np.cross(np.eye(3)[k], r) for k in range(3)])
        v = np.cross(om, r)
        rows.append(e @ B)
        rhs.append(e @ v)
        rows.append(n @ B)
        rhs.append(n @ v)
    A = np.array(rows)
    d = np.array(rhs)
    sol, *_ = np.linalg.lstsq(A, d, rcond=None)
    lat_f, lon_f, rate_f = pole_from_omega(sol)
    print(f"  {len(net)} SYNTHETIC stations, east and north components only "
          f"({A.shape[0]} observations)")
    print(f"  fitted pole: latitude {lat_f:.6f} deg, longitude {lon_f:.6f} deg, "
          f"rate {rate_f:.6f} deg/Myr")
    print(f"  true  pole: latitude {pole_lat:.6f} deg, longitude {pole_lon:.6f} deg, "
          f"rate {rate:.6f} deg/Myr")
    resid = A @ sol - d
    print(f"  rms residual = {np.sqrt(np.mean(resid ** 2)) / MM:.6f} mm/yr "
          "on noiseless data")
    print("  Three parameters (the Euler vector) explain two components at every")
    print("  station: a plate's horizontal velocity field on a sphere is rigid, and")
    print("  a rigid field has exactly three degrees of freedom.")

    section("3. Observability of the radial part of the rotation")
    print("  a station observes only two horizontal components, so the component of")
    print("  Omega parallel to its own radius produces no horizontal motion at that")
    print("  station.  The network therefore has to supply the third direction.")
    print("   stations   fitted pole lat/lon (deg)      fitted rate (deg/Myr)   "
          "error (%)   rms of recovered Omega over 200 noise runs (rad/yr)")
    for n_st in (1, 2, 3, 8):
        used = net[:n_st]
        rows, rhs = [], []
        for lat, lon in used:
            r = ecef(lat, lon)
            e, n, u = enu_basis(lat, lon)
            B = np.column_stack([np.cross(np.eye(3)[k], r) for k in range(3)])
            v = np.cross(om, r)
            rows.append(e @ B)
            rhs.append(e @ v)
            rows.append(n @ B)
            rhs.append(n @ v)
        A1 = np.array(rows)
        d1 = np.array(rhs)
        s1, *_ = np.linalg.lstsq(A1, d1, rcond=None)
        la1, lo1, r1 = pole_from_omega(s1)
        errs = []
        for _ in range(200):
            noise = 1.0 * MM * RNG.standard_normal(d1.size)
            sn, *_ = np.linalg.lstsq(A1, d1 + noise, rcond=None)
            errs.append(np.linalg.norm(sn - om))
        print(f"  {n_st:9d}   {la1:8.3f} / {lo1:9.3f}   {r1:21.6f}   "
              f"{100.0 * abs(r1 - rate) / rate:9.3f}   {np.mean(errs):41.3e}")
    print("  With one station the RATE comes out 1.7 % wrong and the pole is wrong,")
    print("  because the null direction is a rotation axis parallel to that station's")
    print("  radius.  Adding stations closes the null space: the noise-driven scatter")
    print("  in the recovered Euler vector falls from 2.9e-9 rad/yr with one station")
    print("  to 1.1e-10 rad/yr with eight.  That is why plate-motion estimates need")
    print("  geographically spread networks, not more precise single stations.")

    section("4. Two plates and the relative velocity across a boundary")
    om_b = omega_from_pole(-20.0, 40.0, 0.35)             # SYNTHETIC second plate
    print("  plate A pole: (50.0, -120.0) at 0.900 deg/Myr  [SYNTHETIC]")
    print("  plate B pole: (-20.0, 40.0) at 0.350 deg/Myr   [SYNTHETIC]")
    om_rel = om - om_b
    lat_r, lon_r, rate_r = pole_from_omega(om_rel)
    print(f"  relative rotation: pole ({lat_r:.2f}, {lon_r:.2f}) at "
          f"{rate_r:.4f} deg/Myr")
    print("   station lat/lon    A speed (mm/yr)   B speed (mm/yr)   "
          "relative speed (mm/yr)   fraction of a great-circle rate")
    for lat, lon in [(0.0, -120.0), (20.0, -100.0), (40.0, -80.0), (60.0, -60.0)]:
        r = ecef(lat, lon)
        va = np.cross(om, r)
        vb = np.cross(om_b, r)
        vrel = va - vb
        print(f"  {lat:6.1f} / {lon:7.1f}   {np.linalg.norm(va) / MM:15.2f}   "
              f"{np.linalg.norm(vb) / MM:15.2f}   "
              f"{np.linalg.norm(vrel) / MM:21.2f}   "
              f"{np.linalg.norm(vrel) / (rate_r * DEG_PER_MYR * R_EARTH) * 100:28.1f}")
    print("  The relative velocity reaches the full rigid-rotation speed "
          "(rate x radius)")
    print("  only where the station is 90 degrees from the relative pole, and falls")
    print("  to zero at it.  A transform fault on a 90-degree boundary moves at that")
    print("  full speed; a boundary near the pole barely moves.")

    section("5. A frame rotation rate: what it does to apparent velocities")
    print("  A station's coordinates and velocity are only defined once a frame is")
    print("  named.  If frame B rotates relative to frame A at omega_BA, then")
    print("  v_B = v_A - omega_BA x r, so an unmodelled frame rotation appears as a")
    print("  velocity field indistinguishable from a rigid plate rotation.")
    print("   rotation rate (mas/yr)   |omega| (rad/yr)   speed at the equator "
          "(mm/yr)   shear error it adds to a naive estimate (1/yr)")
    for mas in (0.01, 0.03, 0.10, 0.30):
        om_frame = np.array([0.0, 0.0, mas * 1e-3 / 3600.0 * np.pi / 180.0])
        speed = np.linalg.norm(np.cross(om_frame, ecef(0.0, 0.0))) / MM
        print(f"  {mas:22.2f}   {np.linalg.norm(om_frame):16.6e}   "
              f"{speed:32.3f}   {np.linalg.norm(om_frame):24.6e}")
    print("  A rotation produces no strain: the induced velocity field is rigid and")
    print("  its own strain rate is zero by construction (its velocity gradient is")
    print("  antisymmetric).  Yet it contributes exactly |omega| to the shear that a")
    print("  naive finite-difference strain estimate reports, so a 0.30 mas/yr frame")
    print("  rotation shows up as 1.45e-9 1/yr of fictitious shear -- the same")
    print("  ambiguity that a three-station rosette cannot resolve on its own.")

    section("6. A 14-parameter transformation of positions and velocities")
    T = np.array([30.0, -20.0, 50.0])                     # m (SYNTHETIC)
    eps = np.array([0.5, -0.2, 0.8]) * 1e-3 / 3600.0 * np.pi / 180.0   # rad
    s = 3.0e-9                                            # dimensionless
    dT = np.array([1.0, -0.5, 0.8]) * MM                  # m/yr (SYNTHETIC)
    deps = np.array([0.2, 0.1, -0.3]) * 1e-3 / 3600.0 * np.pi / 180.0
    ds = 0.2e-9                                           # 1/yr
    print(f"SYNTHETIC parameters at a reference epoch:")
    print(f"  translation T = {T} m")
    print(f"  rotation eps = {eps} rad = "
          f"{eps / (1e-3 / 3600.0 * np.pi / 180.0)} mas")
    print(f"  scale s = {s:.1e}, translation rate dT = {dT / MM} mm/yr")
    print(f"  rotation rate deps = "
          f"{deps / (1e-3 / 3600.0 * np.pi / 180.0)} mas/yr, scale rate "
          f"ds = {ds:.1e} 1/yr")

    def station_set():
        return [(0.0, 0.0), (45.0, 20.0), (-30.0, 150.0), (60.0, -80.0),
                (-60.0, 30.0), (20.0, -120.0), (-10.0, -20.0), (35.0, 100.0)]

    def ep_cross(e):
        return np.array([[0.0, -e[2], e[1]],
                         [e[2], 0.0, -e[0]],
                         [-e[1], e[0], 0.0]])

    rows_p, rhs_p, rows_v, rhs_v = [], [], [], []
    for lat, lon in station_set():
        r = ecef(lat, lon)
        v = np.cross(om, r)
        dp = T + s * r + (ep_cross(eps) @ r)
        dv = dT + ds * r + (ep_cross(deps) @ r)
        rows_p.append([1, 0, 0, r[0], 0.0, r[2], -r[1]])
        rows_p.append([0, 1, 0, r[1], -r[2], 0.0, r[0]])
        rows_p.append([0, 0, 1, r[2], r[1], -r[0], 0.0])
        rhs_p.extend(dp)
        rows_v.append([1, 0, 0, r[0], 0.0, r[2], -r[1]])
        rows_v.append([0, 1, 0, r[1], -r[2], 0.0, r[0]])
        rows_v.append([0, 0, 1, r[2], r[1], -r[0], 0.0])
        rhs_v.extend(dv)
    sp = np.linalg.lstsq(np.array(rows_p), np.array(rhs_p), rcond=None)[0]
    sv = np.linalg.lstsq(np.array(rows_v), np.array(rhs_v), rcond=None)[0]
    mas = 1e-3 / 3600.0 * np.pi / 180.0
    print(f"  {len(station_set())} SYNTHETIC stations, {len(rhs_p)} components each")
    print("  from positions:")
    print(f"    fitted T = {sp[:3] / MM / 1000} m (true {T} m)")
    print(f"    fitted s = {sp[3]:.4e} (true {s:.1e})")
    print(f"    fitted eps = {sp[4:] / mas} mas (true {eps / mas} mas)")
    print("  from velocities:")
    print(f"    fitted dT = {sv[:3] / MM} mm/yr (true {dT / MM} mm/yr)")
    print(f"    fitted ds = {sv[3]:.4e} 1/yr (true {ds:.1e})")
    print(f"    fitted deps = {sv[4:] / mas} mas/yr (true {deps / mas} mas/yr)")
    print("  Both sets are recovered from a full three-component network.  In")
    print("  practice positions constrain the translation and scale well and the")
    print("  rotations poorly, while velocities constrain the rotation rates best --")
    print("  which is why reference-frame products carry both position and velocity")
    print("  parameters, and a stated reference epoch.")


if __name__ == "__main__":
    main()
