#!/usr/bin/env python3
"""Particle motion and polarisation attributes: covariance eigen-analysis of
SYNTHETIC three-component wave packets.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python particle_motion_demo.py

Everything here is SYNTHETIC.  The wave packets are constructed below; no data
are read and no published number is used.

Sections
--------
1. Rectilinear P motion: eigenvalues, rectilinearity and azimuth.
2. Rayleigh (elliptical, retrograde) and Love (linear transverse) motion.
3. Azimuth uncertainty versus SNR, and why circular motion has no azimuth.
4. A mis-oriented sensor rotates the measured azimuth by the tilt angle.
5. A window that mixes two phases destroys the polarisation estimate.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

FS = 100.0            # sampling rate, Hz
N = 512               # samples (5.12 s)
DT = 1.0 / FS
F0 = 8.0              # wave-packet dominant frequency, Hz
T0 = 2.0              # packet centre time, s


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def wavelet(t):
    """Gaussian-enveloped cosine wave packet, unit peak amplitude."""
    env = np.exp(-((t - T0) / 0.35) ** 2)
    return env * np.cos(2.0 * np.pi * F0 * (t - T0))


def covariance_attributes(data):
    """Eigen-decomposition of the 3x3 covariance of a 3xN array of components.

    Returns (eigenvalues descending, rectilinearity, planarity, azimuth_deg,
    incidence_deg_from_vertical).
    """
    c = np.cov(data)
    vals, vecs = np.linalg.eigh(c)          # ascending order
    vals = vals[::-1]
    v = vecs[:, -1].copy()
    v[np.argmax(np.abs(v))] = abs(v[np.argmax(np.abs(v))])   # fix the sign
    rect = 1.0 - (vals[1] + vals[2]) / (2.0 * vals[0])
    plan = 1.0 - 2.0 * vals[2] / (vals[0] + vals[1])
    az = np.degrees(np.arctan2(v[1], v[0])) % 180.0   # polarisation axis, mod 180
    inc = np.degrees(np.arccos(np.clip(abs(v[2]), -1.0, 1.0)))
    return vals, rect, plan, az, inc


def rotate_horizontals(data, angle_deg):
    """Rotate the N and E components by angle_deg about the vertical."""
    a = np.radians(angle_deg)
    out = data.copy()
    out[0] = np.cos(a) * data[0] + np.sin(a) * data[1]
    out[1] = -np.sin(a) * data[0] + np.cos(a) * data[1]
    return out


def main():
    t = np.arange(N) * DT
    w = wavelet(t)

    section("1. Rectilinear P motion")
    az_true, inc_true = 45.0, 30.0   # azimuth is reported modulo 180 deg
    v_hat = np.array([np.sin(np.radians(inc_true)) * np.cos(np.radians(az_true)),
                      np.sin(np.radians(inc_true)) * np.sin(np.radians(az_true)),
                      np.cos(np.radians(inc_true))])
    data = np.outer(v_hat, w)
    vals, rect, plan, az, inc = covariance_attributes(data)
    print(f"  SYNTHETIC P packet: true azimuth {az_true:.0f} deg, "
          f"incidence {inc_true:.0f} deg from vertical")
    print(f"  eigenvalues (descending) = {vals[0]:.4e}, {vals[1]:.2e}, {vals[2]:.2e}")
    print(f"  rectilinearity = {rect:.4f}   planarity = {plan:.4f}")
    print(f"  recovered azimuth  = {az:.2f} deg mod 180   (true {az_true:.0f})")
    print(f"  recovered incidence = {inc:.2f} deg  (true {inc_true:.0f})")
    print("  -> a single linear packet gives three eigenvalues of which only the")
    print("     first is non-zero: rectilinearity 1, azimuth exact.")

    section("2. Rayleigh (elliptical) and Love (linear transverse) motion")
    env = np.exp(-((t - T0) / 0.35) ** 2)
    h = env * np.cos(2.0 * np.pi * F0 * (t - T0))
    z = 0.70 * env * np.sin(2.0 * np.pi * F0 * (t - T0))     # 90 deg quadrature
    ray = np.vstack([h, np.zeros_like(h), z])                # motion in the N-Z plane
    sense = h * np.gradient(z, DT) - z * np.gradient(h, DT)
    vals, rect, plan, az, inc = covariance_attributes(ray)
    print(f"  Rayleigh-type packet: horizontal N in quadrature with Z at ratio 0.70")
    print(f"  eigenvalues = {vals[0]:.4e}, {vals[1]:.4e}, {vals[2]:.2e}")
    print(f"  rectilinearity = {rect:.4f}   planarity = {plan:.4f}")
    print(f"  azimuth = {az:.2f} deg   incidence = {inc:.2f} deg")
    print(f"  mean sense h*dz/dt - z*dh/dt = {sense.mean():+.4f} for z = +A sin")
    print(f"                                       {-sense.mean():+.4f} for z = -A sin")
    print("  -> the two vertical polarities give equal and opposite sense: the")
    print("     NEGATIVE value is the retrograde (surface Rayleigh) case.")
    love = np.vstack([np.zeros_like(h), h, np.zeros_like(h)])  # pure E
    vals_l, rect_l, plan_l, az_l, inc_l = covariance_attributes(love)
    print(f"  Love-type packet (pure transverse): rectilinearity = {rect_l:.4f}, "
          f"azimuth = {az_l:.2f} deg")
    print("  -> ellipticity lowers rectilinearity and spreads energy over two")
    print("     eigenvalues; the sign of the cross-product gives the sense.")

    section("3. Azimuth uncertainty versus SNR")
    print("  rectilinear vs circular packet, 200 noise realisations each")
    circ = np.vstack([env * np.cos(2.0 * np.pi * F0 * (t - T0)),
                      env * np.sin(2.0 * np.pi * F0 * (t - T0)),
                      0.02 * env])

    def wrap(x):
        return ((x + 90.0) % 180.0) - 90.0   # azimuth is an AXIS: defined mod 180

    print("     SNR (amp)   linear az. s.d. (deg)   circular az. s.d. (deg)")
    for snr in (1.0, 2.0, 5.0, 10.0, 20.0):
        errs_l = np.empty(200)
        errs_c = np.empty(200)
        for r in range(200):
            noise = RNG.standard_normal((3, N)) / snr
            errs_l[r] = wrap(covariance_attributes(data + noise)[3] - az_true)
            errs_c[r] = wrap(covariance_attributes(circ + noise)[3] - 45.0)
        print(f"     {snr:8.1f}   {errs_l.std():20.3f}   {errs_c.std():20.3f}")
    print("  -> the azimuth of a linear particle motion has a well-defined answer")
    print("     whose scatter falls with SNR.  A circular motion has no")
    print("     preferred axis, and its azimuth scatter stays large at every SNR.")

    section("4. A mis-oriented sensor shifts the measured azimuth")
    print("     sensor rotation   recovered azimuth (deg)   shift (deg)")
    for rot in (0.0, 10.0, 20.0, -15.0):
        rot_data = rotate_horizontals(data, rot)
        vals, rect, plan, az_r, inc_r = covariance_attributes(rot_data)
        print(f"     {rot:15.0f}   {az_r:23.2f}   "
              f"{((az_r - az_true + 90.0) % 180.0) - 90.0:11.2f}")
    print("  -> the recovered azimuth is measured in the sensor frame: rotating the")
    print("     sensor by +theta reports an azimuth smaller by theta.  Orientation")
    print("     must be known, or the azimuth is only relative to the sensor.")

    section("5. A window mixing two phases degrades the estimate")
    p_hat = np.array([np.sin(np.radians(30)) * np.cos(np.radians(20)),
                      np.sin(np.radians(30)) * np.sin(np.radians(20)),
                      np.cos(np.radians(30))])
    s_hat = np.array([np.sin(np.radians(80)) * np.cos(np.radians(110)),
                      np.sin(np.radians(80)) * np.sin(np.radians(110)),
                      np.cos(np.radians(80))])
    w_s = np.exp(-((t - (T0 + 1.0)) / 0.35) ** 2) * \
        np.cos(2.0 * np.pi * 6.0 * (t - T0 - 1.0))
    mixed = np.outer(p_hat, w) + 0.6 * np.outer(s_hat, w_s)
    vals, rect, plan, az_m, inc_m = covariance_attributes(mixed)
    print(f"  P at azimuth 20 deg (t = 2.0 s) and S at azimuth 110 deg (t = 3.0 s)")
    print(f"  single 5.12 s window: rectilinearity = {rect:.4f}, "
          f"azimuth = {az_m:.2f} deg, incidence = {inc_m:.2f} deg")
    win = (np.abs(t - T0) < 0.7)
    vals_p, rect_p, plan_p, az_p, inc_p = covariance_attributes(mixed[:, win])
    win_s = (np.abs(t - T0 - 1.0) < 0.7)
    vals_s, rect_s, plan_s, az_s, inc_s = covariance_attributes(mixed[:, win_s])
    print(f"  P window only: rectilinearity = {rect_p:.4f}, "
          f"azimuth = {az_p:.2f} deg, incidence = {inc_p:.2f} deg")
    print(f"  S window only: rectilinearity = {rect_s:.4f}, "
          f"azimuth = {az_s:.2f} deg, incidence = {inc_s:.2f} deg")
    print("  -> one window over both arrivals returns a meaningless average of two")
    print("     polarisations; separating the phases restores two clean estimates.")


if __name__ == "__main__":
    main()
