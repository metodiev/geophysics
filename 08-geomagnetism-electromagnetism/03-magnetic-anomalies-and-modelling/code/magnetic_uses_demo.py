#!/usr/bin/env python3
"""Applications of magnetic surveying: induced moments with demagnetisation,
detection depths for compact targets, sampling, gradiometry and the practical
non-uniqueness of a deep large body against a shallow small one.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_uses_demo.py

Everything here is SYNTHETIC.  The objects, their susceptibilities and the noise
level are chosen teaching values, not data from any survey or site.

Contents
--------
1. The induced moment of a sphere: demagnetisation, and a numerical check
   against the exact dipole field.
2. Detection depths for compact ferrous targets.
3. Sampling: what a coarse station spacing does to the peak of a small anomaly.
4. Gradiometry: separating two nearby shallow targets.
5. A deep large body that mimics a shallow small one.
6. An archaeological order-of-magnitude estimate, with its validity stated.
7. Summary for the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi
C = MU0 / (4.0 * np.pi)
KM = 1.0e3
NT = 1.0e-9
H0_AM = 40.0          # ambient field / mu0, A/m (SYNTHETIC)
NOISE_NT = 0.1
THRESHOLD = 3.0       # detect at three times the noise


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def dipole_anomaly_T(moment, r_m):
    """On-axis total-field anomaly in the pole configuration: 2 C m / r^3."""
    return 2.0 * C * moment / r_m ** 3


def sphere_moment(radius_m, chi):
    """Induced moment of a sphere: m = 3 chi/(3+chi) H0 V."""
    V = 4.0 / 3.0 * np.pi * radius_m ** 3
    return 3.0 * chi / (3.0 + chi) * H0_AM * V, V


def main():
    section("1. The induced moment of a sphere")
    print("a sphere in a uniform field is uniformly magnetised, so its external field")
    print("is EXACTLY a dipole.  Demagnetisation limits the induced moment:")
    print("   M = 3 chi/(3 + chi) H0,  m = M V,  V = (4/3) pi a^3")
    a = 0.05
    chi = 100.0
    m_sph, V_sph = sphere_moment(a, chi)
    M_sph = 3.0 * chi / (3.0 + chi) * H0_AM
    print(f"   a = {a * 100:.1f} cm, chi = {chi:.0f} (synthetic), V = {V_sph:.4e} m^3")
    print(f"   M = {M_sph:.3f} A/m; for chi -> infinity M saturates at 3 H0 = "
          f"{3 * H0_AM:.1f} A/m")
    print(f"   m = {m_sph:.5f} A m^2")
    n = 24
    ax = (np.arange(n) + 0.5) / n * 2 * a - a
    XX, YY, ZZ = np.meshgrid(ax, ax, ax, indexing="ij")
    inside = (XX ** 2 + YY ** 2 + ZZ ** 2) <= a ** 2
    dV = (2 * a / n) ** 3
    src = np.stack([XX[inside], YY[inside], ZZ[inside]], axis=1)
    print(f"   discretised into {inside.sum()} cubes of {dV:.3e} m^3")
    print("   distance   numeric/anlytic")
    for r_m in (3 * a, 5 * a, 10 * a):
        p = np.array([0.0, 0.0, -r_m])
        d = p[None, :] - src
        r = np.linalg.norm(d, axis=1)
        rh = d / r[:, None]
        mm = np.array([0.0, 0.0, M_sph * dV])
        B = C * np.sum((3 * np.sum(mm[None, :] * rh, axis=1)[:, None] * rh
                        - mm[None, :]) / r[:, None] ** 3, axis=0)
        print(f"   {r_m / a:6.0f} a   {B[2] / dipole_anomaly_T(m_sph, r_m):11.5f}")

    section("2. Detection depths for compact ferrous targets")
    print(f"sensor noise {NOISE_NT:.2f} nT rms; detection threshold "
          f"{THRESHOLD:.0f}x noise = {THRESHOLD * NOISE_NT:.2f} nT")
    print("   target                    m (A m^2)   dT at 1 m   max detection depth (m)")
    targets = [("steel sphere r = 2 cm", 0.02, 100.0),
               ("steel sphere r = 5 cm", 0.05, 100.0),
               ("steel sphere r = 10 cm", 0.10, 100.0),
               ("iron cylinder 0.3 x 0.3 m", None, 100.0)]
    for name, rad, chi_t in targets:
        if rad is not None:
            m_t, _ = sphere_moment(rad, chi_t)
        else:
            V_t = 0.3 * np.pi * (0.15 ** 2)
            m_t = 3.0 * chi_t / (3.0 + chi_t) * H0_AM * V_t
        dt1 = dipole_anomaly_T(m_t, 1.0) / NT
        thresh_T = THRESHOLD * NOISE_NT * NT
        r_det = (2.0 * C * m_t / thresh_T) ** (1.0 / 3.0)
        print(f"   {name:26s} {m_t:11.5f}   {dt1:9.2f}   {r_det:22.2f}")
    print("   dT falls as r^-3: doubling the range needs eight times the moment for")
    print("   the same signal, so detectability is set by the smallest target you must")
    print("   find, not by the largest one you can find.")

    section("3. Sampling: what coarse stations do to a small anomaly")
    m_t, _ = sphere_moment(0.05, 100.0)
    z_t = 0.5
    print(f"a steel sphere r = 5 cm at {z_t:.1f} m depth; its anomaly is "
          f"{dipole_anomaly_T(m_t, z_t) / NT:.2f} nT on the axis")
    prof = np.linspace(-4, 4, 4001)
    dT_cont = 2 * C * m_t * (2 * z_t ** 2 - prof ** 2) / (prof ** 2 + z_t ** 2) ** 2.5
    peak_true = dT_cont.max()
    print("   a survey cannot choose where a station lands, so for each spacing the")
    print("   recorded peak is averaged over 50 offsets drawn uniformly within one")
    print("   spacing; the worst case is listed too")
    print("   spacing (m)   samples over the anomaly   mean loss (%)   worst loss (%)")
    half = np.sqrt(2) * z_t
    for spacing in (0.05, 0.1, 0.25, 0.5, 0.75, 1.0, 2.0):
        losses = []
        for off in RNG.uniform(0.0, spacing, 50):
            st = np.arange(-4, 4 + 1e-9, spacing) + off
            dt = 2 * C * m_t * (2 * z_t ** 2 - st ** 2) / (st ** 2 + z_t ** 2) ** 2.5
            losses.append((1 - dt.max() / peak_true) * 100)
        losses = np.array(losses)
        print(f"   {spacing:13.2f}   {2 * half / spacing:23.1f}   "
              f"{losses.mean():13.2f}   {losses.max():14.2f}")
    print(f"   the anomaly half-width is sqrt(2) z = {half:.2f} m.  The mean loss grows")
    print("   smoothly while the worst case jumps between values: whether a survey")
    print("   records the peak is partly a matter of where the stations fall.")

    section("4. Gradiometry: separating two nearby shallow targets")
    sep = 1.0
    z_t = 0.8
    m2 = 0.02
    xs_ = np.linspace(-3, 3, 6001)
    h = 1e-4

    def pair_profile(z_p, x0s):
        out = np.zeros_like(xs_)
        for x0 in x0s:
            d = xs_ - x0
            out += 2 * C * m2 * (2 * z_p ** 2 - d ** 2) / (d ** 2 + z_p ** 2) ** 2.5
        return out

    def dip_ratio(v):
        seg = (xs_ > -(sep / 2 - 0.05)) & (xs_ < (sep / 2 - 0.05))
        i = np.where(seg)[0][np.argmin(np.abs(v[seg]))]
        return abs(v[i]) / np.abs(v).max()

    print(f"two dipoles of m = {m2:.3f} A m^2 at {z_t:.1f} m depth, separation varied")
    print("metric: |value halfway between the targets| / |largest value|;")
    print("smaller means the two targets are better resolved")
    print("   separation (m)   field   vertical gradient")
    for sp in (0.6, 1.0, 1.5, 2.0):
        x0s = (-sp / 2, sp / 2)
        f_prof = pair_profile(z_t, x0s)
        g_prof = (pair_profile(z_t + h, x0s) - pair_profile(z_t - h, x0s)) / (2 * h)
        print(f"   {sp:14.1f}   {dip_ratio(f_prof):5.3f}   {dip_ratio(g_prof):17.3f}")
    print("now add a smooth regional field (a deep body plus a linear ramp):")
    regional = (2 * C * 1.0e3 * (2 * 20.0 ** 2 - xs_ ** 2)
                / (xs_ ** 2 + 20.0 ** 2) ** 2.5) + 5 * NT / KM * (xs_ + 3)
    x0s = (-sep / 2, sep / 2)
    f_prof = pair_profile(z_t, x0s)
    g_prof = (pair_profile(z_t + h, x0s) - pair_profile(z_t - h, x0s)) / (2 * h)
    ft = f_prof + regional
    gt = g_prof + np.gradient(regional, xs_)
    detrended = ft - np.polyval(np.polyfit(xs_, ft, 1), xs_)
    print(f"   separation {sep:.1f} m: field {dip_ratio(f_prof):.3f}, with regional "
          f"{dip_ratio(ft):.3f}, field after a linear detrend {dip_ratio(detrended):.3f}")
    print(f"                        gradient {dip_ratio(g_prof):.3f}, with regional "
          f"{dip_ratio(gt):.3f}")
    print("   the gradient is unaffected by the smooth regional field; the field needs")
    print("   a trend removal that can itself remove target signal.  The price is the")
    print("   |k| factor: differentiating amplifies high-wavenumber noise.")

    section("5. A deep large body that mimics a shallow small one")
    target = dipole_anomaly_T(1.0e9, 1000.0)     # a teaching reference anomaly
    print(f"reference: m = 1.0e9 A m^2 at 1.0 km gives "
          f"{target / NT:.2f} nT")
    print("   depth (km)   required moment (A m^2)   required volume at 5 A/m (km^3)")
    for z_km in (0.5, 1.0, 2.0, 4.0):
        m_req = target * (z_km * KM) ** 3 / (2 * C)
        print(f"   {z_km:10.1f}   {m_req:22.4e}   {m_req / 5.0 / KM ** 3:32.4f}")
    print("   the same anomaly is produced by a small shallow body and by a large")
    print("   deep one: amplitude alone cannot separate them.")

    section("6. An archaeological estimate, with its validity stated")
    dchi = 1.0e-3            # susceptibility contrast, SI (synthetic)
    V_pit = np.pi * (1.0 ** 2) * 0.5
    m_pit = dchi * H0_AM * V_pit
    h_sensor = 0.3
    z_pit = 0.5
    r_eff = h_sensor + z_pit
    print(f"SYNTHETIC pit or kiln: contrast dchi = {dchi:.4f} SI, "
          f"V = {V_pit:.3f} m^3, top at {z_pit:.1f} m")
    print(f"   induced moment m = dchi H0 V = {m_pit:.4f} A m^2")
    print(f"   sensor at {h_sensor:.1f} m above the ground, effective range "
          f"{r_eff:.1f} m")
    print(f"   dipole estimate: dT = {dipole_anomaly_T(m_pit, r_eff) / NT:.2f} nT "
          f"against a noise of {NOISE_NT:.2f} nT")
    print(f"   BUT the pit is 2 m across and the range is only {r_eff:.1f} m, or "
          f"{r_eff / 2.0:.2f} of its width.")
    print("   The dipole approximation needs the range to be several body widths; here")
    print("   it is less than one, so the number above is only an order-of-magnitude")
    print("   estimate and a real survey would model the pit as a magnetised volume.")

    section("7. Summary for the lesson")
    print(f"  sphere r = 5 cm, chi = 100: m = {m_sph:.5f} A m^2, "
          f"M = {M_sph:.2f} A/m (saturated at 3 H0 = {3 * H0_AM:.0f} A/m)")
    print(f"  that target gives {dipole_anomaly_T(m_sph, 1.0) / NT:.2f} nT at 1 m "
          f"and is detected to "
          f"{(2 * C * m_sph / (THRESHOLD * NOISE_NT * NT)) ** (1 / 3):.2f} m")
    print(f"  a station spacing approaching {np.sqrt(2) * 0.5:.2f} m aliases the")
    print("  anomaly of a 0.5 m deep target")
    print("  the vertical gradient removes a smooth regional field that distorts the")
    print("  field profile, at the cost of amplifying high-wavenumber noise")


if __name__ == "__main__":
    main()
