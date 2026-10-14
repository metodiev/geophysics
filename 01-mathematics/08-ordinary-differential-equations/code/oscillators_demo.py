"""Damped and driven oscillators: resonance, Q and instrument response.

Run:  python3 oscillators_demo.py
Requires: Python standard library only.

Companion to lesson 01-08-03.

Model, throughout:

    m x'' + c x' + k x = F0 cos(omega t)

with omega0 = sqrt(k/m), zeta = c/(2 sqrt(k m)), Q = 1/(2 zeta), and
steady-state amplitude

    A(omega) = (F0/m) / sqrt((omega0^2 - omega^2)^2 + (2 zeta omega0 omega)^2).

The analytic amplitude is cross-checked against a time-domain integration of
the ODE (after the transient has decayed), and the phase and the peak location
are computed rather than asserted.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def amplitude(omega, omega0, zeta, f0):
    """Steady-state amplitude for forcing F0 cos(omega t), mass m = 1."""
    return f0 / math.sqrt((omega0 ** 2 - omega ** 2) ** 2
                          + (2 * zeta * omega0 * omega) ** 2)


def phase_lag(omega, omega0, zeta):
    """Phase by which the response lags the forcing, radians."""
    return math.atan2(2 * zeta * omega0 * omega, omega0 ** 2 - omega ** 2)


def integrate_steady_amplitude(omega, omega0, zeta, f0, periods=400.0):
    """Amplitude of the steady-state oscillation, measured from a time series."""
    h = min(2 * math.pi / omega / 200.0, 2 * math.pi / omega0 / 400.0)
    t_end = periods * 2 * math.pi / omega
    n = int(t_end / h)
    t = y = v = 0.0
    peak = 0.0
    window_start = 0.85 * t_end
    for _ in range(n):
        a = f0 * math.cos(omega * t) - 2 * zeta * omega0 * v - omega0 ** 2 * y
        v += h * a                      # semi-implicit (symplectic) Euler
        y += h * v
        t += h
        if t > window_start:
            peak = max(peak, abs(y))
    return peak


def main():
    section("1. The resonance curve: A(omega) for several damping ratios")
    omega0, f0 = 1.0, 1.0
    print(f"omega0 = {omega0}, F0/m = {f0}")
    omegas = [0.1, 0.25, 0.5, 0.75, 0.9, 0.99, 1.0, 1.01, 1.1, 1.5, 2.0, 4.0]
    head = "     omega " + "".join(f"{f'z={z}':>14}" for z in (0.5, 0.2, 0.05, 0.01))
    print(head)
    for om in omegas:
        row = f"{om:>10.2f} "
        for z in (0.5, 0.2, 0.05, 0.01):
            row += f"{amplitude(om, omega0, z, f0):>14.6f}"
        print(row)
    print("At zeta = 0.5 the response is monotone; at zeta <= 0.7 a peak appears")
    print("near omega0 and grows as 1/(2 zeta) .")

    section("2. Peak location and peak height")
    print(f"{'zeta':>8}{'omega_peak':>14}{'A_peak':>12}{'A(omega0)':>14}"
          f"{'1/(2 zeta)':>12}")
    for zeta in (0.5, 0.2, 0.1, 0.05, 0.01, 0.001):
        if zeta < 1 / math.sqrt(2):
            om_p = omega0 * math.sqrt(1 - 2 * zeta ** 2)
        else:
            om_p = 0.0
        print(f"{zeta:>8.3f}{om_p:>14.6f}{amplitude(om_p, omega0, zeta, f0):>12.4f}"
              f"{amplitude(omega0, omega0, zeta, f0):>14.4f}{1 / (2 * zeta):>12.4f}")
    print("The peak sits at omega0 sqrt(1 - 2 zeta^2), slightly below omega0;")
    print("at omega0 the response is exactly Q = 1/(2 zeta) in these units.")
    print("The sqrt(1-2zeta^2) shifts the peak by only 1 % at zeta = 0.1, which")
    print("is why 'resonance at omega0' is a good working rule for high Q.")

    section("3. Analytic amplitude versus a time-domain integration")
    print(f"{'zeta':>8}{'omega':>9}{'analytic':>14}{'integrated':>14}{'rel. diff':>12}")
    for zeta in (0.2, 0.05):
        for om in (0.5, 1.0, 2.0):
            an = amplitude(om, omega0, zeta, f0)
            nu = integrate_steady_amplitude(om, omega0, zeta, f0)
            print(f"{zeta:>8.3f}{om:>9.2f}{an:>14.6f}{nu:>14.6f}"
                  f"{abs(nu - an) / an:>12.2e}")
    print("Relative differences are dominated by the finite integration window")
    print("and the fixed step, not by the analytic formula.")

    section("4. Phase lag: 0, 90 and 180 degrees")
    print(f"{'omega/omega0':>14}" + "".join(f"{f'z={z}':>14}" for z in (0.5, 0.2, 0.05)))
    for ratio in (0.1, 0.5, 0.9, 1.0, 1.1, 2.0, 10.0):
        row = f"{ratio:>14.2f}"
        for z in (0.5, 0.2, 0.05):
            row += f"{math.degrees(phase_lag(ratio * omega0, omega0, z)):>14.3f}"
        print(row)
    print("Every curve passes through exactly 90 degrees at omega = omega0; the")
    print("steepness of that passage is the sharpness of the resonance.")

    section("5. Instrument response: what a seismometer measures")
    # Inertial velocity sensor, normalised transfer function:
    #   H(omega) = omega^2 / (omega0^2 - omega^2 + 2 i zeta omega0 omega)
    # so |H| -> 1 for omega >> omega0 (flat in velocity) and |H| -> omega^2/omega0^2
    # for omega << omega0 (proportional to acceleration).
    print("velocity-sensor response |H| = omega^2 / |omega0^2 - omega^2"
          " + 2 i zeta omega0 omega|")
    print(f"{'omega/omega0':>14}{'|H| z=0.7':>14}{'|H| z=0.1':>14}"
          f"{'(omega/omega0)^2':>18}")
    for ratio in (0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 100.0):
        row = f"{ratio:>14.3f}"
        for z in (0.7, 0.1):
            om, om0 = ratio * omega0, omega0
            h = om ** 2 / abs(complex(om0 ** 2 - om ** 2, 2 * z * om0 * om))
            row += f"{h:>14.6f}"
        row += f"{ratio ** 2:>18.6f}"
        print(row)
    print("Below the corner frequency the response tracks acceleration")
    print("(omega^2) and is useless for ground velocity; above it, the response")
    print("is flat in velocity. The corner is omega0 = 2 pi f_corner.")

    section("6. Corner frequency and usable band for a broadband sensor")
    for T0 in (120.0, 40.0, 1.0):
        f_c = 1.0 / T0
        om0 = 2 * math.pi / T0
        print(f"T0 = {T0:6.1f} s (omega0 = {om0:.4f} rad/s): flat in velocity")
        print(f"          above f = {f_c:.6f} Hz = {1000 * f_c:.4f} mHz")
    print("A 120 s broadband sensor is flat in velocity above ~8.3 mHz; that is")
    print("why long-period and normal-mode work needs long-period instruments.")

    section("7. Energy bookkeeping at resonance: why Q matters")
    zeta = 0.01
    Q = 1.0 / (2 * zeta)
    print(f"zeta = {zeta}, Q = {Q}")
    print(f"half-power bandwidth: delta_omega / omega0 = 2 zeta = {2 * zeta:.5f}")
    print(f"   -> omega in [{1 - zeta:.5f}, {1 + zeta:.5f}] rad/s (about omega0)")
    print(f"build-up time of the resonant response ~ 2 Q / omega0 = "
          f"{2 * Q / omega0:.3f} s")
    print(f"   = Q / pi = {Q / math.pi:.3f} forced cycles")
    print(f"steady-state energy stored ~ Q times the energy injected per radian")
    # Exact half-power points, found by bisection on A(omega).
    om_p = omega0 * math.sqrt(1 - 2 * zeta ** 2)
    a_peak = amplitude(om_p, omega0, zeta, f0)
    target = a_peak / math.sqrt(2.0)

    def bisect(lo, hi, increasing):
        """Bisect for A(omega) = target on a monotone branch."""
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            a = amplitude(mid, omega0, zeta, f0)
            if (a < target) == increasing:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    lo_hp = bisect(0.5, om_p, True)      # rising branch
    hi_hp = bisect(om_p, 3.0, False)     # falling branch
    print(f"exact half-power points: omega = {lo_hp:.6f} and {hi_hp:.6f}")
    print(f"first-order estimate omega0(1 -/+ zeta) = {1 - zeta:.6f} and "
          f"{1 + zeta:.6f}")
    print(f"   fractional error of that estimate: "
          f"{abs(lo_hp - (1 - zeta)) / lo_hp:.2e} and "
          f"{abs(hi_hp - (1 + zeta)) / hi_hp:.2e}")
    print("So 'half power at omega0(1 +/- zeta)' is a first-order-in-zeta rule:")
    print("the residual error is 1.5e-4 in omega, about 1.5 % of the")
    print("half-bandwidth itself. Good enough for design, not an identity.")

    section("8. The same mathematics in a tuned EM receiver coil")
    print("A coil of inductance L, self-capacitance C and resistance R obeys")
    print("   L q'' + R q' + q/C = E(t),  omega0 = 1/sqrt(LC), "
          "zeta = R/(2 sqrt(L/C))")
    for L, C, R in ((1e-2, 1e-10, 25.0), (1e-2, 1e-10, 400.0)):
        w0 = 1.0 / math.sqrt(L * C)
        z = R / (2.0 * math.sqrt(L / C))
        print(f"   L = {L:.0e} H, C = {C:.0e} F, R = {R:5.1f} ohm: "
              f"f0 = {w0 / (2 * math.pi) / 1e3:8.3f} kHz, zeta = {z:.4f}, "
              f"Q = {1 / (2 * z):.2f}")
    print("The first coil rings (Q = 400); the second is far better damped")
    print("(Q = 25) because the input resistance was raised by design. A ringing")
    print("receiver lengthens every transient and smears the early-time signal.")
    print("Note the contrast with the *ground*: EM diffusion in a conductor gives")
    print("a first-order lag whose imaginary part grows with frequency, not a")
    print("Lorentzian resonance. Both are second-order-looking responses, and")
    print("mixing them up corrupts an interpretation -- check the constitutive")
    print("model before reading a curve as resonance.")


if __name__ == "__main__":
    main()
