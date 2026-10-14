"""Laboratory electrical measurements on rocks: a synthetic walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (the geometric factor of a sample holder,
Ohm's law in a four-electrode array, the Cole-Cole complex resistivity, the
Debye relaxation).  No instrument specification or measured rock property is
reproduced.
"""

import numpy as np

RNG_SEED = 20261014
EPS0 = 8.8541878128e-12


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "Two-electrode versus four-electrode: the contact impedance")
    rho, area, length = 50.0, 1.14e-3, 0.080       # ohm m, m2, m
    r_true = rho * length / area
    print(f"  rho = {rho:.1f} ohm m, A = {area*1e4:.2f} cm2, L = {length*1e3:.1f} mm")
    print(f"  specimen resistance R = rho L / A = {r_true:9.2f} ohm")
    print(f"  {'contact (ohm)':>15}{'apparent rho':>15}{'error':>10}")
    for rc in (0.0, 100.0, 500.0, 1000.0, 5000.0):
        app = rho * (1.0 + 2.0 * rc / r_true)
        print(f"  {rc:15.1f}{app:15.2f}{100*(app/rho-1):9.2f} %")
    print("  -> a two-electrode measurement adds both contacts to a resistance of")
    print("     a few kilohm; the four-electrode array removes them from the")
    print("     measurement because no current flows through the sense circuit.")


def section_2():
    banner(2, "Four-electrode geometry and the error in the spacing")
    area, length, rho = 1.14e-3, 0.080, 50.0
    k_factor = area / length
    print(f"  geometric factor K = A / L = {k_factor*1e3:.4f} mm  "
          f"(rho = K * dV / I)")
    print(f"  {'sense spacing (mm)':>21}{'apparent rho':>15}{'error':>10}")
    for l_eff in (78.0, 79.0, 79.5, 80.0, 80.5, 81.0, 82.0):
        app = rho * (l_eff / 80.0)
        print(f"  {l_eff:21.2f}{app:15.3f}{100*(app/rho-1):9.2f} %")
    print("  -> the apparent resistivity is linear in the sense-electrode")
    print("     separation, so a 0.5 mm spacing error on an 80 mm specimen is")
    print("     0.63 %: the geometry, not the voltmeter, is the accuracy limit.")


def section_3():
    banner(3, "Spectral IP: a Cole-Cole response and the frequency effect")
    rho0, m_pol, tau, c_exp = 50.0, 0.30, 1.0, 0.50
    print(f"  Cole-Cole: rho0 = {rho0:.0f} ohm m, m = {m_pol:.2f}, "
          f"tau = {tau:.1f} s, c = {c_exp:.2f}")
    print(f"  {'f (Hz)':>9}{'|rho| (ohm m)':>16}{'phase (mrad)':>14}")
    f_peak = 1.0 / (2 * np.pi * tau)
    for f in (0.01, 0.1, 1.0, 10.0, 100.0):
        w = 2 * np.pi * f
        z = 1.0 - 1.0 / (1.0 + (1j * w * tau) ** c_exp)
        rho = rho0 * (1.0 - m_pol * z)
        print(f"  {f:9.2f}{abs(rho):16.4f}{np.angle(rho)*1e3:14.3f}")
    w1, w2 = 2 * np.pi * 0.1, 2 * np.pi * 10.0
    r1 = rho0 * (1 - m_pol * (1 - 1 / (1 + (1j * w1 * tau) ** c_exp)))
    r2 = rho0 * (1 - m_pol * (1 - 1 / (1 + (1j * w2 * tau) ** c_exp)))
    pfe = (abs(r1) - abs(r2)) / abs(r1) * 100.0
    print(f"  peak of the imaginary part at {f_peak:.4f} Hz "
          f"(tau = {tau:.1f} s, c = {c_exp:.2f})")
    print(f"  percent frequency effect 0.1 -> 10 Hz = {pfe:.4f} %")
    print("  -> the phase is the robust IP observable: it is dimensionless, it is")
    print("     not affected by the absolute resistivity or by contact impedance,")
    print("     and it peaks near 1/(2 pi tau).")


def section_4():
    banner(4, "Dielectric response: from impedance to complex permittivity")
    area, length = 1.14e-3, 0.080
    c0 = EPS0 * area / length
    eps_s, eps_inf, tau_d = 20.0, 5.0, 1.0e-6
    print(f"  C0 = {c0*1e12:.4f} pF, Debye: eps_s = {eps_s:.1f}, "
          f"eps_inf = {eps_inf:.1f}, tau = {tau_d*1e6:.1f} us")
    print(f"  {'f (Hz)':>10}{'eps_prime':>12}{'eps_double':>13}{'tan delta':>12}"
          f"{'|Z| (kohm)':>13}")
    for f in (1e3, 1e4, 1e5, 1e6, 1e7):
        w = 2 * np.pi * f
        eps_c = eps_inf + (eps_s - eps_inf) / (1.0 + 1j * w * tau_d)
        z = 1.0 / (1j * w * c0 * eps_c)
        print(f"  {f:10.0f}{eps_c.real:12.4f}{-eps_c.imag:13.4f}"
              f"{-eps_c.imag/eps_c.real:12.4f}{abs(z)/1e3:13.4f}")
    f_peak = 1.0 / (2 * np.pi * tau_d)
    f_tan = f_peak * np.sqrt(eps_s / eps_inf)
    print(f"  eps'' peaks at {f_peak/1e3:.3f} kHz, but tan delta peaks at")
    print(f"  f_peak * sqrt(eps_s/eps_inf) = {f_tan/1e3:.3f} kHz, where tan delta =")
    print(f"  (eps_s - eps_inf) / (2 sqrt(eps_s eps_inf)) = "
          f"{0.5*(eps_s-eps_inf)/np.sqrt(eps_s*eps_inf):.4f}")
    print("  -> the permittivity is a spectrum, not a number: a 'dielectric")
    print("     constant' quoted without its frequency is a measurement waiting")
    print("     to be misinterpreted.")


def section_5():
    banner(5, "What dominates the uncertainty of a laboratory resistivity")
    rho = 50.0
    terms = [("voltage", 0.5), ("current", 0.5), ("length", 0.1), ("area", 0.2),
             ("temperature (2 %/degC)", 1.0), ("pore-fluid salinity", 2.0)]
    tot = sum((v / 100.0) ** 2 for _, v in terms)
    print(f"  {'term':<26}{'relative (%)':>14}{'variance share (%)':>20}")
    for name, v in terms:
        print(f"  {name:<26}{v:14.2f}{(v/100.0)**2/tot*100:20.2f}")
    print(f"  combined relative uncertainty {np.sqrt(tot)*100:8.3f} %")
    print(f"  {'salinity offset (%)':>21}{'apparent rho (ohm m)':>22}")
    for s in (-5.0, -2.0, 0.0, 2.0, 5.0):
        print(f"  {s:21.1f}{rho*(1.0+0.02*s)**-1:22.4f}")
    print("  -> the pore fluid dominates: the fluid, not the instrument, sets the")
    print("     accuracy, which is why the salinity is measured and reported.")


def main():
    print()
    banner(0, "LABORATORY ELECTRICAL MEASUREMENTS: SYNTHETIC WALK-THROUGH")
    section_1()
    section_2()
    section_3()
    section_4()
    section_5()
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no instrument")
    print("specification or measured rock property is reproduced.")


if __name__ == "__main__":
    main()
