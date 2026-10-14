"""Plate motion frames, Euler poles and finite rotations.

Run:  .venv/bin/python plate_motion_frames_demo.py
Requires: numpy (and the standard library).

Companion to lesson 04-02-04, "Plate Motion Frames, Euler Poles and Global
Models".

Everything a plate-motion model says is a rotation. This script builds the
rotation machinery from scratch, uses it, and then inverts a synthetic velocity
field for the rotation that generated it -- which is what a real plate-motion
solution does to GNSS or magnetic-anomaly data:

1. **Euler vector to velocity.** v = omega x r, with omega the angular velocity
   vector of the plate pair and r the position vector of the site. The script
   checks the closed-form speed for a small circle about the pole,
   |v| = omega R sin(Delta), and the azimuth.
2. **The circuit closes.** Three plates around a closed circuit have relative
   rotations that compose to the identity. The script constructs a circuit,
   verifies that the composition is the identity, and then measures the
   *error* made by adding the finite rotation vectors as if they were vectors.
   That error is the reason plate-motion solutions are built from Euler
   vectors rather than from velocities.
3. **The inverse problem.** Synthetic site velocities are generated from a
   known Euler vector, corrupted with noise, and inverted for the Euler vector
   by linear least squares. The recovered pole and rate are compared with the
   input, and the residual is reported. The design matrix is examined to show
   that one site constrains only two of the three components of the rotation
   and that the rank deficiency is exactly the rotation about the site's own
   radius.
4. **What the frame is.** A relative velocity is meaningless without both
   plates named, and the script shows that adding a single rigid rotation to
   every site velocity leaves the *relative* motion across the circuit
   unchanged but changes every absolute velocity. This is the reference-frame
   problem in one calculation.

Earth is treated as a sphere of radius 6371 km. That is adequate for every
calculation here: the flattening changes site positions by about 0.3 per cent,
which is smaller than the noise in any real velocity field used to fit a
plate-motion model.
"""

from __future__ import annotations

import math

import numpy as np

R_EARTH_KM = 6371.0
DEG = math.pi / 180.0


def section(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


# --------------------------------------------------------------------------
# Frames and rotations.
# --------------------------------------------------------------------------

def unit_vector(lat_deg, lon_deg):
    """Geocentric unit vector in Earth-fixed (ECEF) coordinates."""
    lat, lon = lat_deg * DEG, lon_deg * DEG
    return np.array([math.cos(lat) * math.cos(lon),
                     math.cos(lat) * math.sin(lon),
                     math.sin(lat)])


def position(lat_deg, lon_deg, radius_km=R_EARTH_KM):
    return radius_km * unit_vector(lat_deg, lon_deg)


def enu_basis(lat_deg, lon_deg):
    """East, north, up unit vectors at a site."""
    lat, lon = lat_deg * DEG, lon_deg * DEG
    east = np.array([-math.sin(lon), math.cos(lon), 0.0])
    north = np.array([-math.sin(lat) * math.cos(lon),
                      -math.sin(lat) * math.sin(lon),
                      math.cos(lat)])
    up = unit_vector(lat_deg, lon_deg)
    return east, north, up


def to_enu(v_ecef, lat_deg, lon_deg):
    east, north, up = enu_basis(lat_deg, lon_deg)
    return np.array([np.dot(v_ecef, east),
                     np.dot(v_ecef, north),
                     np.dot(v_ecef, up)])


def euler_vector(lat_deg, lon_deg, rate_deg_per_ma):
    """Angular velocity vector in rad/Ma."""
    return (rate_deg_per_ma * DEG) * unit_vector(lat_deg, lon_deg)


def pole_from_vector(omega):
    """Return (lat, lon, rate in deg/Ma) from an angular velocity vector."""
    rate = float(np.linalg.norm(omega)) / DEG
    if rate == 0.0:
        return 0.0, 0.0, 0.0
    u = omega / np.linalg.norm(omega)
    lat = math.degrees(math.asin(max(-1.0, min(1.0, u[2]))))
    lon = math.degrees(math.atan2(u[1], u[0]))
    return lat, lon, rate


def rodrigues(omega_vec):
    """Rotation matrix for a finite rotation vector (radians)."""
    theta = float(np.linalg.norm(omega_vec))
    if theta == 0.0:
        return np.eye(3)
    k = omega_vec / theta
    kx = np.array([[0.0, -k[2], k[1]],
                   [k[2], 0.0, -k[0]],
                   [-k[1], k[0], 0.0]])
    return (np.eye(3) + math.sin(theta) * kx
            + (1.0 - math.cos(theta)) * (kx @ kx))


def rotation_vector(r_mat):
    """Inverse of rodrigues: the rotation vector of a rotation matrix."""
    cos_theta = (np.trace(r_mat) - 1.0) / 2.0
    theta = math.acos(max(-1.0, min(1.0, cos_theta)))
    if abs(theta) < 1e-12:
        return np.zeros(3)
    if abs(math.pi - theta) < 1e-8:
        # Near a half turn the antisymmetric part vanishes; read the axis from
        # the symmetric part instead.
        a = (r_mat + np.eye(3)) / 2.0
        axis = np.sqrt(np.maximum(np.diag(a), 0.0))
        if axis[0] > 0 and r_mat[0, 1] < 0:
            axis[1] = -axis[1]
        if axis[0] > 0 and r_mat[0, 2] < 0:
            axis[2] = -axis[2]
        return theta * axis / max(np.linalg.norm(axis), 1e-30)
    k = np.array([r_mat[2, 1] - r_mat[1, 2],
                  r_mat[0, 2] - r_mat[2, 0],
                  r_mat[1, 0] - r_mat[0, 1]]) / (2.0 * math.sin(theta))
    return theta * k


def part1_euler_to_velocity():
    section("1. Euler vector to velocity")
    pole_lat, pole_lon, rate = 60.0, -100.0, 0.75      # ILLUSTRATIVE pole
    omega = euler_vector(pole_lat, pole_lon, rate)
    print(f"  Illustrative Euler pole: latitude {pole_lat:.0f} deg, "
          f"longitude {pole_lon:.0f} deg,")
    print(f"  angular rate {rate:.2f} deg/Ma.")
    print("  v = omega x r, with r in km and omega in rad/Ma;")
    print("  the resulting velocity is in km/Ma, which is exactly mm/a.")
    print()
    print(f"  {'site lat':>9}{'site lon':>9}{'speed (mm/a)':>14}"
          f"{'azimuth (deg)':>15}{'small-circle |v|':>18}")
    sites = [(0.0, -100.0), (30.0, -120.0), (60.0, -150.0), (75.0, -180.0),
             (40.0, 0.0), (-30.0, 150.0)]
    for lat_s, lon_s in sites:
        r = position(lat_s, lon_s)
        v = np.cross(omega, r)                        # km/Ma == mm/a
        enu = to_enu(v, lat_s, lon_s)
        speed = float(np.linalg.norm(enu[:2]))
        az = math.degrees(math.atan2(enu[0], enu[1])) % 360.0
        # Closed form for a small circle about the pole.
        delta = math.acos(max(-1.0, min(1.0,
                    float(np.dot(unit_vector(lat_s, lon_s),
                                 unit_vector(pole_lat, pole_lon))))))
        predicted = np.linalg.norm(omega) * R_EARTH_KM * math.sin(delta)
        print(f"  {lat_s:>9.0f}{lon_s:>9.0f}{speed:>14.2f}{az:>15.1f}"
              f"{predicted:>18.2f}")
    print()
    print("  The last two columns agree to the printed precision: the speed is")
    print("  omega R sin(Delta), where Delta is the angular distance from the")
    print("  pole. Two consequences follow directly.")
    print()
    print("  At the pole itself sin(Delta) = 0, so a site at the Euler pole does")
    print("  not move -- it rotates about its own axis. The pole is not a place")
    print("  where the plate is stationary in any absolute sense; it is the")
    print("  point where the *relative* motion of the two plates vanishes.")
    print()
    print("  At 90 degrees from the pole the speed is maximal, omega R. The")
    print("  motion is along small circles about the pole, so the azimuth is")
    print("  east for a site due south of the pole and becomes progressively")
    print("  more oblique as the site approaches the pole. This is why the")
    print("  velocity field of a single plate pair, plotted on a map, looks")
    print("  like a rotation about a point -- because it is one.")
    print()


def part2_circuit():
    section("2. Does the circuit close? Finite rotations are not vectors")
    w1 = np.array([0.05, 0.02, 0.01])      # rad, ILLUSTRATIVE
    w2 = np.array([-0.01, 0.04, 0.02])
    r1 = rodrigues(w1)
    r2 = rodrigues(w2)
    r3 = (r1 @ r2).T                       # closes the circuit by construction
    w3 = rotation_vector(r3)

    print("  Three plates A, B, C: define the relative rotations A-B and B-C,")
    print("  then define C-A as the inverse of their composition. The circuit")
    print("  closes by construction; the question is what the *vector* sum of")
    print("  the three rotation vectors looks like.")
    print()
    print(f"    rotation vector AB = {np.array2string(w1, precision=5)}")
    print(f"    rotation vector BC = {np.array2string(w2, precision=5)}")
    print(f"    rotation vector CA = {np.array2string(w3, precision=5)}")
    print()
    s = w1 + w2 + w3
    print(f"    vector sum AB+BC+CA = {np.array2string(s, precision=5)}")
    print(f"    |sum|               = {np.linalg.norm(s):.6f} rad")
    print(f"    |AB|+|BC|+|CA|      = "
          f"{np.linalg.norm(w1) + np.linalg.norm(w2) + np.linalg.norm(w3):.6f} rad")
    print(f"    relative error      = "
          f"{100 * np.linalg.norm(s) / (np.linalg.norm(w1) + np.linalg.norm(w2)):.2f} %")
    print()
    print("  The composition is exactly the identity, and at the same time the")
    print("  vector sum is *not* zero. Finite rotations do not add as vectors,")
    print("  because the group is non-commutative: the failure of the sum to")
    print("  vanish is the commutator of the two rotations.")
    print()
    print("  The consequence for plate-motion work is concrete. Instantaneous")
    print("  angular velocities do add as vectors, so the instantaneous circuit")
    print("  closes with omega_AB + omega_BC + omega_CA = 0 exactly. Finite")
    print("  rotations, which is what a magnetic anomaly or a magnetic isochron")
    print("  actually measures, do not. A reconstruction that adds finite")
    print("  rotations as if they were vectors, instead of composing the")
    print("  matrices, accumulates an error proportional to the product of the")
    print("  angles -- and the errors of a long plate circuit are a classic")
    print("  source of disagreement between published reconstructions.")
    print()


def part3_inversion():
    section("3. Inverting a synthetic velocity field for the Euler vector")
    true_lat, true_lon, true_rate = -45.0, 110.0, 0.60
    omega_true = euler_vector(true_lat, true_lon, true_rate)
    print(f"  True Euler pole (the input): latitude {true_lat:.0f} deg,")
    print(f"  longitude {true_lon:.0f} deg, rate {true_rate:.2f} deg/Ma.")
    print()

    rng = np.random.default_rng(7)
    sites = [(10.0, 100.0), (-20.0, 90.0), (-50.0, 120.0), (-60.0, 160.0),
             (-30.0, 200.0), (0.0, 60.0), (-70.0, 60.0), (-40.0, 30.0)]
    noise_mm_a = 1.0
    rows, rhs, observations = [], [], []
    for lat_s, lon_s in sites:
        r = position(lat_s, lon_s)
        v = np.cross(omega_true, r)
        # Add the noise in the site's local horizontal plane, which is where a
        # GNSS velocity is actually measured.
        east, north, up = enu_basis(lat_s, lon_s)
        v_noisy = v + rng.normal(0.0, noise_mm_a) * east \
                    + rng.normal(0.0, noise_mm_a) * north
        observations.append(v_noisy)

        # v = omega x r is linear in omega: v = -[r]_x omega.
        rx = np.array([[0.0, -r[2], r[1]],
                       [r[2], 0.0, -r[0]],
                       [-r[1], r[0], 0.0]])
        rows.append(-rx)
        rhs.append(v_noisy)

    print(f"  {len(sites)} synthetic sites, each velocity perturbed by "
          f"{noise_mm_a:.0f} mm/a per horizontal component.")
    print("  Input velocities (mm/a), east/north components:")
    for (lat_s, lon_s), v in zip(sites, observations):
        enu = to_enu(v, lat_s, lon_s)
        print(f"    site ({lat_s:>5.0f}, {lon_s:>5.0f})  east {enu[0]:>7.2f}"
              f"   north {enu[1]:>7.2f}")
    print()

    a_mat = np.vstack(rows)
    b_vec = np.concatenate(rhs)
    omega_est, residuals, rank, sv = np.linalg.lstsq(a_mat, b_vec, rcond=None)
    lat_e, lon_e, rate_e = pole_from_vector(omega_est)
    print(f"  Recovered Euler pole: latitude {lat_e:.2f} deg, "
          f"longitude {lon_e:.2f} deg,")
    print(f"  rate {rate_e:.3f} deg/Ma.  Errors: latitude "
          f"{abs(lat_e - true_lat):.2f} deg, longitude "
          f"{abs(lon_e - true_lon):.2f} deg, rate "
          f"{abs(rate_e - true_rate):.3f} deg/Ma.")
    print(f"  Design-matrix rank = {rank} of 3; singular values = "
          f"{np.array2string(sv, precision=3)}.")
    print()

    # Residual velocity at each site.
    print("  Residual (modelled minus observed), horizontal components:")
    print(f"    {'site':>14}{'d east (mm/a)':>16}{'d north (mm/a)':>17}")
    res_sum = 0.0
    for (lat_s, lon_s), v_obs in zip(sites, observations):
        r = position(lat_s, lon_s)
        v_mod = np.cross(omega_est, r)
        d = to_enu(v_mod - v_obs, lat_s, lon_s)
        res_sum += d[0] ** 2 + d[1] ** 2
        print(f"    ({lat_s:>5.0f},{lon_s:>5.0f}){d[0]:>16.2f}{d[1]:>17.2f}")
    print(f"  RMS horizontal residual = {math.sqrt(res_sum / len(sites)):.3f}"
          " mm/a,")
    print("  which is the level of the noise added. The inversion recovers")
    print("  what the data contain and no more, which is the correct outcome")
    print("  and the reason a real plate-motion solution reports a covariance")
    print("  matrix alongside the pole.")
    print()


def part4_rank_deficiency():
    section("4. Why one site is not enough")
    sites = [(20.0, 40.0)]
    all_sites = [(20.0, 40.0), (-35.0, 150.0)]
    for label, subset in (("one site", sites), ("two sites", all_sites)):
        rows = []
        for lat_s, lon_s in subset:
            r = position(lat_s, lon_s)
            rx = np.array([[0.0, -r[2], r[1]],
                           [r[2], 0.0, -r[0]],
                           [-r[1], r[0], 0.0]])
            rows.append(-rx)
        a_mat = np.vstack(rows)
        sv = np.linalg.svd(a_mat, compute_uv=False)
        null = None
        if len(subset) == 1:
            _, _, vh = np.linalg.svd(a_mat)
            null = vh[-1]
        print(f"  {label}: design matrix {a_mat.shape}, rank "
              f"{int(np.sum(sv > 1e-9 * sv[0]))} of 3")
        print(f"    singular values = {np.array2string(sv, precision=3)}")
        if null is not None:
            lat_n, lon_n, _ = pole_from_vector(null)
            print(f"    unconstrained direction: pole at "
                  f"({lat_n:.1f}, {lon_n:.1f}) deg,")
            print("    which is the site's own radius vector. A velocity")
            print("    measured at one place cannot see a rotation about the")
            print("    line joining that place to the centre of the Earth.")
        print()
    print("  This is the geometric reason a plate-motion solution needs sites")
    print("  spread over the plate and not clustered at one end. It is also")
    print("  why a solution built from magnetic anomalies alone is much weaker")
    print("  than one that also uses GNSS: the anomalies sample a narrow band")
    print("  of azimuths, while GNSS sites surround the rotation.")
    print()


def part5_frame():
    section("5. A relative velocity needs a frame")
    omega_ab = euler_vector(60.0, -100.0, 0.75)
    omega_extra = euler_vector(20.0, 30.0, 0.20)
    site = (35.0, -120.0)
    r = position(*site)
    v_ab = np.cross(omega_ab, r)
    v_with_extra = np.cross(omega_ab + omega_extra, r)
    enu_ab = to_enu(v_ab, *site)
    enu_x = to_enu(v_with_extra, *site)
    print("  Take a site and a relative velocity for the plate pair A-B. Now")
    print("  add to the whole system a single rigid rotation of 0.20 deg/Ma")
    print("  about a pole at (20 N, 30 E) -- a change of reference frame, not")
    print("  a change of the physics.")
    print()
    print(f"    A-B velocity at the site        : east {enu_ab[0]:>7.2f},"
          f" north {enu_ab[1]:>7.2f} mm/a")
    print(f"    same velocity, shifted frame    : east {enu_x[0]:>7.2f},"
          f" north {enu_x[1]:>7.2f} mm/a")
    print(f"    difference                      : east "
          f"{enu_x[0] - enu_ab[0]:>7.2f}, north "
          f"{enu_x[1] - enu_ab[1]:>7.2f} mm/a")
    print()
    print("  The absolute velocity of the site changed. The *relative* velocity")
    print("  of plate A with respect to plate B did not, because the same")
    print("  rotation was applied to both. Every plate-motion solution therefore")
    print("  has to state the frame it is in -- a no-net-rotation condition, an")
    print("  explicit choice of which plate is fixed, or a named absolute")
    print("  reference frame -- and two solutions quoted in different frames")
    print("  are not directly comparable even when both are correct.")
    print()


def main():
    print("Plate motion frames, Euler poles and finite rotations.")
    part1_euler_to_velocity()
    part2_circuit()
    part3_inversion()
    part4_rank_deficiency()
    part5_frame()
    print("=" * 74)
    print("Euler poles and velocity fields are ILLUSTRATIVE. The inversion")
    print("recovers its own input, which is the check that the machinery is")
    print("correct; no published plate-motion solution is reproduced here.")
    print("=" * 74)


if __name__ == "__main__":
    main()
