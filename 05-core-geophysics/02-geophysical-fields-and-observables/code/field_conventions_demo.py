"""Field conventions: what an instrument measures, and in what units.

Four independent checks, all offline:

  1. mGal and gamma are DEFINED, so their conversions to SI are exact ratios.
     We derive the factors rather than quoting them.
  2. Gravity is the GRADIENT OF A POTENTIAL.  We differentiate
     V = -G m / |r| numerically and compare with the analytic G m d / r^3.
     Agreement confirms that the observable is a derivative of the potential,
     which is why it decays faster (1/r^2) than the potential (1/r).
  3. A magnetometer measures a COMPONENT or the TOTAL FIELD, and the total-
     field anomaly is a projection.  We show |B|, the components, and dT for
     the same dipole.
  4. EM fields DIFFUSE.  We solve the 1-D diffusion equation numerically with
     a harmonic boundary condition and compare the measured amplitude decay
     and phase lag with the closed-form skin depth delta = sqrt(2/(mu sigma w)).

Constants are SI and cited.  Model inputs are SYNTHETIC and stated.

Run:  python3 field_conventions_demo.py
"""

from __future__ import annotations

import numpy as np

G = 6.67430e-11         # m^3 kg^-1 s^-2 (CODATA 2018, NIST)
MU0 = 1.25663706212e-6  # H/m            (CODATA 2018, NIST)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main() -> None:
    # ------------------------------------------------------------------
    section("1. Field units are DEFINED: derive the conversion factors")
    # 1 Gal := 1 cm/s^2 = 1e-2 m/s^2  (definition of the Gal)
    # 1 mGal := 1e-3 Gal = 1e-5 m/s^2
    gal_si = 1.0e-2
    mgal_si = 1.0e-3 * gal_si
    print(f"  1 Gal    = 1e-2 m/s^2  (by definition)")
    print(f"  1 mGal   = 1e-3 Gal = {mgal_si:.1e} m/s^2")
    # 1 gamma := 1 nT = 1e-9 T  (definition of the gamma)
    gamma_si = 1.0e-9
    print(f"  1 gamma  = 1 nT = {gamma_si:.1e} T  (by definition)")
    print(f"  check: a 2 mGal anomaly = {2*mgal_si:.3e} m/s^2")
    print(f"         a 500 nT anomaly = {500*gamma_si:.3e} T")

    # ------------------------------------------------------------------
    section("2. Gravity is minus the gradient of the potential")
    depth, mass = 250.0, 1.0e10        # m, kg  (SYNTHETIC)
    # V(r) = -G m / |r|  with r from the source; g_z (downward) = -dV/dz.
    def potential(z_obs):
        return -G * mass / np.hypot(0.0, z_obs - depth)

    z0 = 0.0
    h = 1.0e-4
    dV_dz = (potential(z0 + h) - potential(z0 - h)) / (2.0 * h)
    g_numeric = -dV_dz
    # g_z = G m d / r^3 with r = d directly above the source  =>  G m / d^2.
    g_analytic = G * mass * depth / (depth**2) ** 1.5
    print(f"  SYNTHETIC point mass {mass:.1e} kg at {depth:.0f} m depth")
    print(f"  -dV/dz by central difference = {g_numeric:.9e} m/s^2")
    print(f"  analytic   G m d / r^3        = {g_analytic:.9e} m/s^2")
    print(f"  relative difference = "
          f"{abs(g_numeric - g_analytic)/g_analytic:.3e}")
    print(f"  = {g_numeric/1.0e-5:.6f} mGal")
    print("  The observable is a DERIVATIVE of the potential, so it decays")
    print("  one power of r faster than the potential itself.")

    # ------------------------------------------------------------------
    section("3. Magnetometer: components versus total field")
    m = np.array([0.0, 0.0, 5.0e6])     # A m^2, SYNTHETIC dipole, vertical
    rvec = np.array([300.0, 0.0, 0.0])  # source -> observer, due north
    r = np.linalg.norm(rvec)
    rhat = rvec / r
    B = MU0 / (4.0 * np.pi) * (3.0 * np.dot(m, rhat) * rhat - m) / r**3
    NT = 1.0e-9
    print(f"  SYNTHETIC dipole |m| = {np.linalg.norm(m):.3e} A m^2, "
          f"observer {r:.0f} m due north of it")
    print(f"  B_x = {B[0]/NT:+.6f} nT   B_y = {B[1]/NT:+.6f} nT   "
          f"B_z = {B[2]/NT:+.6f} nT")
    print(f"  |B|  = {np.linalg.norm(B)/NT:.6f} nT")
    for inc_deg in (0.0, 60.0, 90.0):
        inc = np.radians(inc_deg)
        bhat = np.array([np.cos(inc), 0.0, np.sin(inc)])
        print(f"    dT for ambient inclination {inc_deg:4.0f} deg: "
              f"{np.dot(bhat, B)/NT:+10.6f} nT")
    print("  Same field, three different 'measurements'.  A fluxgate gives")
    print("  components; a proton precession magnetometer gives |B|; the")
    print("  anomaly dT is the PROJECTION of the anomaly on the main field.")

    # ------------------------------------------------------------------
    section("4. EM diffusion: measured skin depth vs closed form")
    # Solve dB/dt = D d2B/dz2 with B(0,t) = B0 cos(w t), semi-infinite.
    # Closed form: B(z,t) = B0 e^{-z/delta} cos(w t - z/delta),
    #              delta = sqrt(2 D / w).
    sigma = 1.0                          # S/m  (SYNTHETIC)
    D = 1.0 / (MU0 * sigma)              # m^2/s
    period = 100.0                       # s
    w = 2.0 * np.pi / period
    delta = np.sqrt(2.0 * D / w)
    print(f"  SYNTHETIC: conductivity {sigma:.2f} S/m, period {period:.0f} s")
    print(f"  diffusion coefficient D = 1/(mu0 sigma) = {D:.4e} m^2/s")
    print(f"  closed form delta = sqrt(2D/w) = {delta:.3f} m")

    def march(nz):
        """Explicit finite-difference march; return (delta_meas, phase_meas)."""
        # The domain extends to 6 delta, where the field has decayed to
        # e^-6 = 0.25% of its surface value, so the artificial far boundary
        # does not measurably reflect.
        z = np.linspace(0.0, 6.0 * delta, nz)
        dz = z[1] - z[0]
        dt = 0.4 * dz**2 / D             # explicit-scheme stability limit
        spp = int(round(period / dt))
        B = np.zeros(nz)
        hist = np.zeros((spp, nz))
        for step in range(5 * spp):
            t = step * dt
            B_new = B.copy()
            B_new[0] = np.cos(w * t)
            B_new[1:-1] = (B[1:-1]
                           + dt * D * (B[2:] - 2 * B[1:-1] + B[:-2]) / dz**2)
            B_new[-1] = B_new[-2]        # zero-flux far end
            B = B_new
            if step >= 4 * spp:
                hist[step - 4 * spp] = B
        amp = np.max(np.abs(hist), axis=0)
        amp /= amp[0]
        # Fit only the clean exponential region; farther out the residual
        # finite-domain effect is visible at the 1% level.
        mask = (z > 0.1 * delta) & (z < 1.2 * delta)
        d_meas = -1.0 / np.polyfit(z[mask], np.log(amp[mask]), 1)[0]
        j = int(np.argmin(np.abs(z - 0.75 * delta)))
        lag = (np.argmax(hist[:, j]) - np.argmax(hist[:, 0])) * dt
        lag = lag % period
        return d_meas, w * lag, z[j], dz

    print("   nz    dz/delta    delta_meas(m)   rel.err   phase_meas  "
          "phase_pred")
    for nz in (31, 61, 121):
        d_meas, ph_meas, z_j, dz = march(nz)
        print(f"  {nz:3d}   {dz/delta:9.4f}   {d_meas:11.3f}   "
              f"{abs(d_meas-delta)/delta:.3e}   {ph_meas:9.5f}   "
              f"{z_j/delta:9.5f}")
    print("  Both the amplitude decay and the phase lag of the semi-infinite")
    print("  closed form are recovered, and the residual error falls as the")
    print("  grid is refined: it is discretisation error (the explicit scheme")
    print("  is first order in dt and second order in dz), not a modelling")
    print("  error.  Reporting the grid and the residual is part of the")
    print("  result.  Skin depth is the depth over which the field falls to")
    print("  1/e and lags by 1 rad, so slow fields penetrate deeper -- the")
    print("  basis of every frequency-domain EM method.")

    print("\nSUMMARY: measure the right quantity in the right unit, and know")
    print("whether your observable is a potential, a gradient, or a projection.")


if __name__ == "__main__":
    main()
