#!/usr/bin/env python3
"""Tidal response and the quality factor of the whole Earth.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tidal_response_demo.py

Everything here is a SYNTHETIC teaching model.  The ephemeris, the Love numbers,
the density and the quality factors are adopted inputs; no measured tide, Love
number or observation is quoted.

Contents
--------
1. The phase lag of a complex Love number, and how it relates to Q.
2. A numerical check of the hysteresis rule: dissipated work per cycle is
   pi*k*tan(delta)*x0^2, so the average power is omega*E*tan(delta).
3. The M2 tide: potential amplitude, equilibrium height, stored energy, and the
   dissipation rate in terawatts for several Q.
4. Direct measurement of a phase lag from a synthetic record by least squares.
5. Why one relaxation time cannot fit the Earth: Q versus frequency across the
   tidal and seismic bands.
6. The tidal torque and the length-of-day change implied by the dissipation.
7. Verification summary.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

GM_MOON = 4.9028e12      # m^3/s^2, adopted lunar gravitational parameter
D_MOON = 3.844e8         # m, adopted mean lunar distance
R_EARTH = 6.371e6        # m, mean radius (nominal)
G_SURF = 9.81            # m/s^2
RHO = 3300.0             # kg/m^3, adopted mean density of the deforming shell
H2 = 0.60                # adopted elastic displacement Love number
K2_EL = 0.30             # adopted elastic potential Love number
OMEGA_M2 = 2.0 * np.pi / (12.4206 * 3600.0)   # rad/s, semidiurnal M2 frequency
OMEGA_EARTH = 7.292115e-5
C_EARTH = 8.04e37        # kg m^2, adopted polar moment of inertia


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. The phase lag of a complex Love number")
    print(f"adopted elastic Love numbers: h2 = {H2:.2f}, k2 = {K2_EL:.2f}")
    print("a dissipative response makes k2 complex: k2(omega) = k2_el*(1 + i*tan"
          " delta)")
    print("   Q      tan(delta)      delta (deg)      (180/pi)/Q (deg)"
          "   relative difference")
    for q in (50.0, 100.0, 200.0, 400.0):
        delta = np.arctan(1.0 / q)
        approx = np.degrees(1.0 / q)
        print(f"  {q:5.0f} {1.0 / q:13.5f} {np.degrees(delta):16.4f}"
              f" {approx:20.4f} {abs(np.degrees(delta) - approx) / np.degrees(delta):20.2e}")
    print("\nfor Q >= 50 the small-angle replacement delta_deg = (180/pi)/Q is")
    print("accurate to a per cent; at Q = 10 the error would be about 0.2% of the")
    print("angle and the exact arctangent should be used")

    section("2. Checking the hysteresis rule numerically")
    k = 1.0
    x0 = 1.0
    omega = 2.0 * np.pi * 0.7
    t = np.linspace(0.0, 2.0 * np.pi / omega, 200001)
    x = x0 * np.cos(omega * t)
    for q in (20.0, 50.0, 100.0):
        delta = np.arctan(1.0 / q)
        force = k * (x - np.tan(delta) * np.gradient(x, t) / omega)
        work = np.trapezoid(force * np.gradient(x, t), t)
        analytic = -np.pi * k * x0**2 * np.tan(delta)
        print(f"  Q = {q:5.0f}: work per cycle {work:+.6f} J,"
              f" analytic -pi*k*tan(delta)*x0^2 = {analytic:+.6f} J,"
              f" difference {abs(work - analytic):.2e}")
    print("\nthe dissipative force is k*(x - tan(delta)*xdot/omega), i.e. the")
    print("quadrature term opposes motion; the work per cycle is negative (energy")
    print("leaves the system) and its magnitude is the hysteresis area")

    section("3. The M2 tide: potential, height, energy and dissipation")
    v2 = (GM_MOON / D_MOON) * (R_EARTH / D_MOON) ** 2
    xi_rigid = v2 / G_SURF
    xi_body = H2 * xi_rigid
    print(f"degree-2 tidal potential amplitude at the surface:"
          f" (GM/d)*(R/d)^2 = {v2:.4f} m^2/s^2")
    print(f"  equilibrium (rigid) tide height: {xi_rigid:.4f} m")
    print(f"  actual surface displacement h2*xi: {xi_body:.4f} m")
    energy = 0.5 * RHO * G_SURF * xi_body**2 * R_EARTH**2 * (4.0 * np.pi / 5.0)
    print(f"\nstored energy of the degree-2 deformation,"
          f" (1/2)*rho*g*xi^2*R^2*(4*pi/5) = {energy:.4e} J"
          f" ({energy / 1e18:.2f} EJ)")
    print(f"M2 angular frequency: {OMEGA_M2:.6e} rad/s"
          f" (period {2 * np.pi / OMEGA_M2 / 3600.0:.4f} h)")
    print("\n   Q      power P = omega*E*tan(delta) (TW)   dLOD/dt (ms/century)")
    for q in (50.0, 100.0, 200.0):
        power = OMEGA_M2 * energy * np.tan(np.arctan(1.0 / q))
        torque = power / OMEGA_EARTH
        domegadt = -torque / C_EARTH
        dloddt = -(86400.0 / OMEGA_EARTH) * domegadt * 3.1557e9 * 1e3
        print(f"  {q:5.0f} {power / 1e12:33.4f} {dloddt:30.4f}")
    print("\nboth quantities scale as 1/Q, so a factor-of-two uncertainty in Q is a")
    print("factor-of-two uncertainty in the dissipation and in the LOD trend")
    print("note: this is the SOLID-Earth contribution only; an ocean tide carries")
    print("its own dissipation, which this model does not contain")

    section("4. Measuring a phase lag from a synthetic record")
    delta_true = np.radians(0.5730)
    tt = np.linspace(0.0, 30.0 * 2.0 * np.pi / OMEGA_M2, 4000)
    forcing = np.cos(OMEGA_M2 * tt)
    response = np.cos(OMEGA_M2 * tt - delta_true) + RNG.normal(0.0, 0.02, tt.size)
    design = np.vstack([np.cos(OMEGA_M2 * tt), np.sin(OMEGA_M2 * tt)]).T
    coeffs = np.linalg.lstsq(design, response, rcond=None)[0]
    delta_fit = np.arctan2(coeffs[1], coeffs[0])
    amp = np.hypot(coeffs[0], coeffs[1])
    print(f"adopted phase lag: {np.degrees(delta_true):.4f} deg")
    print(f"least-squares fit: {np.degrees(delta_fit):.4f} deg,"
          f" amplitude {amp:.4f}")
    print(f"difference: {np.degrees(delta_fit) - np.degrees(delta_true):+.4f} deg")
    print(f"a lag of {np.degrees(delta_fit):.4f} deg corresponds to"
          f" Q = 1/tan(delta) = {1.0 / np.tan(delta_fit):.1f}")

    section("5. One relaxation time cannot fit the Earth")
    print("a standard linear solid has Q^-1 = Delta*omega*tau/(1 + (omega*tau)^2)")
    q_tide = 200.0
    tau = 1.0 / OMEGA_M2
    delta_strength = 2.0 / q_tide
    print(f"adopted: Q = {q_tide:.0f} at the tidal frequency, so the peak of the"
          f" absorption is placed at omega*tau = 1")
    print(f"  Delta = {delta_strength:.5f}, tau = {tau:.3e} s")
    print("\n   frequency (Hz)    omega*tau    Q from this single relaxation")
    for f in (OMEGA_M2 / (2 * np.pi), 1.0e-4, 1.0e-3, 1.0e-2, 1.0):
        w = 2.0 * np.pi * f
        qinv = delta_strength * w * tau / (1.0 + (w * tau) ** 2)
        print(f"  {f:15.6f} {w * tau:12.4e} {1.0 / qinv:31.1f}")
    w_seis = 2.0 * np.pi * 1.0
    q_seis = 1.0 / (delta_strength * w_seis * tau / (1.0 + (w_seis * tau) ** 2))
    nominal_seismic_q = 400.0
    print(f"\nthe same relaxation predicts Q = {q_seis:.3e} at 1 Hz, a factor"
          f" {q_seis / nominal_seismic_q:.1e} above the adopted nominal seismic")
    print(f"value of Q = {nominal_seismic_q:.0f} used here purely as a comparison"
          " anchor")
    print("the Earth instead shows Q rising slowly with frequency over many")
    print("decades, which requires a broad absorption band: Q proportional to"
          " omega^alpha")
    alpha_needed = np.log10(2.0) / np.log10(w_seis / OMEGA_M2)
    print(f"to go from Q = {q_tide:.0f} at the tidal frequency to Q = 400 at 1 Hz")
    print(f"requires an exponent alpha = log10(2)/log10(omega ratio) ="
          f" {alpha_needed:.4f}")

    section("6. The tidal torque and the length of day")
    for q in (50.0, 100.0, 200.0):
        power = OMEGA_M2 * energy * np.tan(np.arctan(1.0 / q))
        torque = power / OMEGA_EARTH
        print(f"  Q = {q:5.0f}: torque = P/Omega = {torque:.4e} N m,"
              f" dOmega/dt = -tau/C = {-torque / C_EARTH:.4e} rad/s^2")
    q_ref = 100.0
    power_ref = OMEGA_M2 * energy * np.tan(np.arctan(1.0 / q_ref))
    print(f"\nat Q = {q_ref:.0f} the Earth's rotation loses"
          f" {power_ref / 1e12:.4f} TW to the solid-body tide")
    print("the angular momentum goes into the lunar orbit, not out of the system,")
    print("so the effect on the length of day is a transfer and not a loss")

    section("7. Verification")
    print("  hysteresis check: the numerically integrated work per cycle matched")
    print("  -pi*k*tan(delta)*x0^2 to the quadrature tolerance (printed above)")
    print(f"  energy identity: P/(omega*E) = {np.tan(np.arctan(1.0 / q_ref)):.6f}"
          f" against tan(delta) = {1.0 / q_ref:.6f}")
    print(f"  lag recovery: {np.degrees(delta_fit):.4f} deg against"
          f" {np.degrees(delta_true):.4f} deg")
    dlod_fit = np.degrees(delta_fit)
    print(f"  LOD check: dLOD/dt from the torque at Q = {q_ref:.0f} ="
          f" {-(86400.0 / OMEGA_EARTH) * (-(power_ref / OMEGA_EARTH) / C_EARTH) * 3.1557e9 * 1e3:.4f}"
          " ms/century (matches section 3)")
    print("  Q of the fitted lag: "
          f"{1.0 / np.tan(delta_fit):.2f} against the adopted 100.0")
    print("\nSYNTHETIC teaching model; no measured tide or Love number is used.")


if __name__ == "__main__":
    main()
