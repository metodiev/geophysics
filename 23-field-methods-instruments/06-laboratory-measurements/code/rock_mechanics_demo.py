"""Rock mechanics laboratory tests: a synthetic walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (linear elasticity, the Mohr-Coulomb
criterion and its UC S conversion, Byerlee's friction law, elastic machine
compliance, rate-dependent friction, size effect).  No laboratory standard,
instrument specification or measured rock property is reproduced.
"""

import numpy as np

RNG_SEED = 20261014


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "Uniaxial compression: moduli, Poisson's ratio and machine compliance")
    eps = np.array([0.0, 0.2857e-3, 0.5714e-3, 0.8571e-3, 1.1429e-3])
    sig = np.array([0.0, 10.0, 20.0, 30.0, 40.0])          # MPa
    fit = np.polyfit(eps, sig, 1)
    e_true = fit[0]
    print(f"  axial stress 0-{sig[-1]:.0f} MPa, axial strain 0-{eps[-1]:.4e}")
    print(f"  secant E over the range = {e_true/1e3:.3f} GPa")
    eps_lat = -0.25 * eps
    print(f"  lateral strain at peak = {eps_lat[-1]:.4e} -> Poisson's ratio "
          f"= {abs(eps_lat[-1]/eps[-1]):.4f}")
    area, length = 1.13e-3, 0.080
    print(f"  {'machine stiffness (kN/mm)':>27}{'apparent E (GPa)':>18}{'error':>9}")
    for km in (1.0e10, 5.0e9, 2.0e9, 1.0e9):
        comp = area / (km * length)
        e_app = 1.0 / (1.0 / (e_true * 1e6) + comp) / 1e9
        print(f"  {km/1e6:27.0f}{e_app:18.3f}{100*(e_app/(e_true/1e3)-1):8.1f} %")
    print("  -> the measured strain includes the machine's own compliance: a")
    print("     soft frame makes a stiff rock look compliant, and the error is")
    print("     systematic and one-signed unless the compliance is measured.")
    return e_true / 1e3


def section_2():
    banner(2, "Triaxial tests and the Mohr-Coulomb fit")
    s3 = np.array([5.0, 20.0, 50.0])          # MPa
    s1 = np.array([60.0, 105.0, 180.0])       # MPa
    print(f"  {'sigma3 (MPa)':>13}{'sigma1 peak (MPa)':>19}{'fitted':>10}"
          f"{'residual':>10}")
    q, ucs = np.polyfit(s3, s1, 1)
    for a, b in zip(s3, s1):
        pred = q * a + ucs
        print(f"  {a:13.1f}{b:19.1f}{pred:10.2f}{b-pred:10.2f}")
    phi = np.degrees(np.arcsin((q - 1.0) / (q + 1.0)))
    c_coh = ucs * (1.0 - np.sin(np.radians(phi))) / (2.0 * np.cos(np.radians(phi)))
    print(f"  fit: sigma1 = {q:.4f} sigma3 + {ucs:.4f}  [MPa]")
    print(f"  friction angle phi = asin((q-1)/(q+1)) = {phi:.2f} deg")
    print(f"  cohesion c = UCS (1 - sin phi) / (2 cos phi) = {c_coh:.4f} MPa")
    print(f"  the three tests span sigma3 = {s3[0]:.0f}-{s3[-1]:.0f} MPa; the fit is")
    print("  an extrapolation to sigma3 = 0, which is why at least three tests are")
    print("  required and the residual pattern must be inspected.")


def section_3():
    banner(3, "Friction: Byerlee's law and the reactivation ratio")
    print(f"  {'sigma_n (MPa)':>14}{'tau (MPa)':>11}{'tau/sigma_n':>13}")
    for sn in (5.0, 10.0, 50.0, 200.0, 400.0, 800.0):
        if sn <= 200.0:
            tau = 0.85 * sn
        else:
            tau = 50.0 + 0.6 * sn
        print(f"  {sn:14.1f}{tau:11.2f}{tau/sn:13.4f}")
    print("  a critically oriented fault in a stress field with a ratio")
    print(f"  {'sigma1/sigma3':>14}{'shear/normal':>14}{'reactivated?':>14}")
    for ratio in (3.0, 5.0, 8.0, 12.33, 15.0, 20.0):
        # (s1-s3)/2 vs (s1+s3)/2 for the optimally oriented plane, s3 = 1
        shear = (ratio - 1.0) / 2.0
        normal = (ratio + 1.0) / 2.0
        need = 0.85
        r = shear / normal
        state = "at the limit" if abs(r - need) < 1e-6 else ("yes" if r > need else "no")
        print(f"  {ratio:14.1f}{r:14.4f}{state:>14}")
    print("  -> the threshold is a stress ratio (about 12.3 here for mu = 0.85),")
    print("     not a stress: raise the pore pressure and the effective normal")
    print("     stress falls, so the same ratio reactivates at a lower differential.")


def section_4():
    banner(4, "Post-peak behaviour and the brittle-ductile transition")
    peak, residual = 180.0, 60.0
    print(f"  peak {peak:.0f} MPa, residual {residual:.0f} MPa")
    print(f"  drop = {peak-residual:.0f} MPa, brittleness index "
          f"= {(peak-residual)/peak:.4f}")
    print(f"  {'sigma3 (MPa)':>13}{'peak':>9}{'residual':>10}{'drop':>8}{'B':>8}")
    for s3 in (0.0, 10.0, 25.0, 50.0, 100.0, 200.0):
        pk = 180.0 - 0.4 * s3
        res = 60.0 + 0.55 * s3
        print(f"  {s3:13.1f}{pk:9.2f}{res:10.2f}{pk-res:8.2f}{(pk-res)/pk:8.4f}")
    s3c = (180.0 - 60.0) / (0.4 + 0.55)
    print(f"  peak and residual meet at sigma3 = {s3c:.2f} MPa: above that the")
    print("  behaviour is ductile, the brittleness index is meaningless and the")
    print("  failure criterion is a yield envelope rather than a strength.")


def section_5():
    banner(5, "Strain rate, size effect and the numbers that must be stated")
    a_rate, sn_eff = 0.010, 50.0
    print(f"  rate-and-state style: dtau = a sigma_eff ln(V/V0), "
          f"a = {a_rate:.3f}, sigma_eff = {sn_eff:.0f} MPa")
    print(f"  {'rate ratio':>12}{'dtau (MPa)':>13}{'dtau/sigma_eff':>16}")
    for ratio in (2.0, 10.0, 100.0, 1000.0):
        print(f"  {ratio:12.1f}{a_rate*sn_eff*np.log(ratio):13.4f}"
              f"{a_rate*np.log(ratio):16.5f}")
    print(f"  {'size ratio':>12}{'strength ratio':>16}")
    for ratio in (2.0, 5.0, 10.0, 50.0):
        print(f"  {ratio:12.1f}{ratio**-0.20:16.4f}")
    print("  -> a 10x rate change is a ~1 MPa effect and a 10x size change is a")
    print("     ~37 % effect: the size effect is the bigger one, and neither is")
    print("     visible in a report that quotes a single strength number.")


def main():
    print()
    banner(0, "ROCK MECHANICS LABORATORY: SYNTHETIC WALK-THROUGH")
    section_1()
    section_2()
    section_3()
    section_4()
    section_5()
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no laboratory standard,")
    print("instrument specification or measured rock property is reproduced.")


if __name__ == "__main__":
    main()
