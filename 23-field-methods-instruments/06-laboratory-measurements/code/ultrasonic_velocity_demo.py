"""Ultrasonic velocity measurement: a synthetic laboratory walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (travel time with a transducer delay, the
elastic-moduli relations from P- and S-wave velocities, wavelength and
resolution, first-order error propagation).  No instrument specification,
calibration standard or measured rock property is reproduced.
"""

import numpy as np

RNG_SEED = 20261014


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "Travel time and the transducer delay")
    v_true, t0_true = 4500.0, 2.5e-6            # m/s, s
    lengths = np.array([0.040, 0.060])          # m
    times = t0_true + lengths / v_true
    print(f"  synthetic true velocity {v_true:.0f} m/s, delay {t0_true*1e6:.2f} us")
    for l, t in zip(lengths, times):
        naive = l / t
        print(f"    L = {l*1e3:5.1f} mm, t = {t*1e6:7.4f} us -> naive v = "
              f"{naive:7.1f} m/s ({100*(naive/v_true-1):+6.2f} %)")
    v_fit = (lengths[1] - lengths[0]) / (times[1] - times[0])
    t0_fit = (times[0] * lengths[1] - times[1] * lengths[0]) / (lengths[1] - lengths[0])
    print(f"  two-length solution: v = {v_fit:8.2f} m/s, t0 = {t0_fit*1e6:6.3f} us "
          f"({100*(v_fit/v_true-1):+5.3f} %, {100*(t0_fit/t0_true-1):+5.3f} %)")
    print("  -> ignoring the delay gives a 22 % velocity error; the delay is")
    print("     measured, not assumed, and two lengths are enough to measure it.")
    return v_fit, t0_fit


def section_2():
    banner(2, "Frequency, wavelength and the specimen length")
    v = 4500.0
    print(f"  at v = {v:.0f} m/s:")
    print(f"  {'f (MHz)':>9}{'lambda (mm)':>13}{'min L for L >= 5 lambda (mm)':>31}")
    for f_mhz in (0.25, 0.5, 1.0, 2.25, 5.0):
        lam = v / (f_mhz * 1e6)
        print(f"  {f_mhz:9.2f}{lam*1e3:13.3f}{5*lam*1e3:31.2f}")
    print("  and for a 40 mm specimen, L >= 5 lambda requires")
    print(f"    f >= 5 v / L = {5*v/0.040/1e6:.3f} MHz")
    print("  -> the specimen length sets a *minimum* frequency; attenuation and")
    print("     beam spread set the maximum, and the usable window between them")
    print("     is the design space of the measurement.")


def section_3():
    banner(3, "Elastic moduli from the two velocities")
    rho, v_p, v_s = 2650.0, 4500.0, 2600.0
    m_mod = rho * v_p ** 2
    g_mod = rho * v_s ** 2
    k_mod = rho * (v_p ** 2 - (4.0 / 3.0) * v_s ** 2)
    nu = (v_p ** 2 - 2 * v_s ** 2) / (2 * (v_p ** 2 - v_s ** 2))
    e_mod = 2 * g_mod * (1 + nu)
    print(f"  rho = {rho:.0f} kg/m3, Vp = {v_p:.0f} m/s, Vs = {v_s:.0f} m/s")
    print(f"  M = rho Vp^2               = {m_mod/1e9:7.2f} GPa")
    print(f"  G = rho Vs^2               = {g_mod/1e9:7.2f} GPa")
    print(f"  K = rho(Vp^2 - 4/3 Vs^2)   = {k_mod/1e9:7.2f} GPa")
    print(f"  nu = (Vp^2-2Vs^2)/(2(Vp^2-Vs^2)) = {nu:7.4f}")
    print(f"  E = 2G(1+nu)               = {e_mod/1e9:7.2f} GPa")
    print(f"  Vp/Vs = {v_p/v_s:6.4f},  K/rho = {(k_mod/rho)/1e6:6.3f} km2/s2")
    print("  -> the S velocity carries the shear information; a chain that cannot")
    print("     generate a shear wave cannot produce G, K or E to better than a guess.")


def section_4(v_fit, t0_fit):
    banner(4, "Pressure dependence and the effective pressure")
    v0, a, b = 4500.0, 5.0e-3, 1.2e-5           # km/s at 0 MPa, and MPa coefficients
    print(f"  synthetic relation Vp(P) = {v0/1000:.2f} + {a:.4f} P - {b:.2e} P^2  [km/s, MPa]")
    print(f"  {'P (MPa)':>9}{'Vp (m/s)':>11}{'dVp/dP (m/s/MPa)':>19}")
    for p in (0.0, 10.0, 25.0, 50.0, 100.0, 150.0):
        h = 0.5
        dv = ((v0 + 1000 * (a * (p + h) - b * (p + h) ** 2))
              - (v0 + 1000 * (a * (p - h) - b * (p - h) ** 2))) / (2 * h)
        vp = v0 + 1000 * (a * p - b * p ** 2)
        print(f"  {p:9.1f}{vp:11.1f}{dv:19.2f}")
    print(f"  {'confining':>11}{'pore':>7}{'Pe (MPa)':>11}{'Vp (m/s)':>11}{'Vs (m/s)':>11}")
    for pc, pp in ((50.0, 0.0), (50.0, 10.0), (100.0, 20.0), (150.0, 50.0)):
        pe = pc - pp
        vp = v0 + 1000 * (a * pe - b * pe ** 2)
        vs = 2600.0 + 1000 * (3.0e-3 * pe - 7.0e-6 * pe ** 2)
        print(f"  {pc:11.1f}{pp:7.1f}{pe:11.1f}{vp:11.1f}{vs:11.1f}")
    print("  -> what stiffens a rock is the effective pressure, not the confining")
    print("     pressure: two specimens at the same Pc differ if their Pp differ.")


def section_5(v_fit, t0_fit):
    banner(5, "Uncertainty of a velocity measurement")
    length = 0.040
    dt, dl = 0.01e-6, 0.01e-3
    t_net = length / v_fit
    rel_t = dt / t_net
    rel_l = dl / length
    rel_v = np.hypot(rel_t, rel_l)
    print(f"  L = {length*1e3:.1f} mm +- {dl*1e3:.3f} mm, t = {t_net*1e6:.4f} us net")
    print(f"  timing resolution {dt*1e6:.3f} us -> relative contribution "
          f"{rel_t*100:7.4f} %")
    print(f"  length resolution {dl*1e3:.3f} mm -> relative contribution "
          f"{rel_l*100:7.4f} %")
    print(f"  combined relative uncertainty      {rel_v*100:7.4f} % "
          f"= {rel_v*v_fit:6.2f} m/s")
    print(f"  {'delay error (us)':>18}{'velocity error (%)':>20}")
    for d0 in (0.0, 0.05, 0.10, 0.25):
        v_err = (t_net) / (t_net + d0 * 1e-6) - 1.0
        print(f"  {d0:18.2f}{v_err*100:20.3f}")
    print("  -> the timing term dominates, and an error in the *delay* is a")
    print("     systematic velocity error, not a scatter.")


def main():
    print()
    banner(0, "ULTRASONIC VELOCITY: SYNTHETIC WALK-THROUGH")
    v_fit, t0_fit = section_1()
    section_2()
    section_3()
    section_4(v_fit, t0_fit)
    section_5(v_fit, t0_fit)
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no instrument")
    print("specification or measured rock property is reproduced.")


if __name__ == "__main__":
    main()
