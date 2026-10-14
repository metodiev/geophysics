#!/usr/bin/env python3
"""Satellite gravimetry, part 1: what a satellite-to-satellite range link
measures, what limits its resolution, and how a gravity coefficient becomes a
mass.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python grace_gracefo_demo.py

Everything here is SYNTHETIC.  The orbit altitude, the satellite separation, the
repeat cycle, the instrument noise and the Love number below are *teaching
values chosen for this module*, not the parameters of any real mission, and no
measured gravity field is used anywhere in this file.

Contents
--------
1. Orbit geometry from Kepler's third law: period, speed, revolutions per day.
2. What the range link actually measures: the projection of the gravity
   gradient onto the separation direction, for a synthetic surface mass anomaly.
3. The resolution limit: downward-continuation noise amplification (1+h/R)^(l+1)
   versus harmonic degree, and the half-wavelength it permits.
4. Temporal sampling: repeat cycle, ground-track spacing, monthly solutions.
5. From a Stokes coefficient to a mass: equivalent water height, and an
   independent check of the formula against exact mass balance at degree 0.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard constants (exact or rounded, stated with units) ---------------
G = 6.67430e-11             # m^3 kg^-1 s^-2, CODATA 2018
GM_EARTH = 3.986004418e14   # m^3 s^-2, standard adopted value of the Earth's GM
R_EARTH = 6371.0e3          # m, rounded mean Earth radius
RHO_W = 1000.0              # kg m^-3, density of water
OMEGA_EARTH = 7.2921150e-5  # rad s^-1, standard Earth rotation rate

# --- SYNTHETIC teaching parameters (not any real mission's values) ----------
ALTITUDE_KM = 500.0         # m -> below
SEPARATION_KM = 220.0
REPEAT_DAYS = 61.0
NOISE_RANGE_ACC = 1.0e-10   # m s^-2, synthetic single-sample noise on the link
K_LOVE2 = -0.30             # synthetic degree-2 LOAD Love number (teaching value)
EWH_DISC_M = 0.10           # m, water-equivalent thickness of the test anomaly
DISC_RADIUS_KM = 300.0

M_EARTH = GM_EARTH / G


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def orbit_period(a):
    """Kepler's third law for a circular orbit: T = 2 pi sqrt(a^3 / GM)."""
    return 2.0 * np.pi * np.sqrt(a ** 3 / GM_EARTH)


def main():
    section("1. Orbit geometry from Kepler's third law (SYNTHETIC orbit)")
    a = R_EARTH + ALTITUDE_KM * 1e3
    T = orbit_period(a)
    v = np.sqrt(GM_EARTH / a)
    rev_per_day = 86400.0 / T
    print(f"mean radius used          R       = {R_EARTH/1e3:.1f} km")
    print(f"synthetic orbit altitude  h       = {ALTITUDE_KM:.1f} km")
    print(f"semi-major axis           a       = {a/1e3:.1f} km")
    print(f"orbital period            T       = {T/60.0:.3f} min "
          f"= {T:.2f} s")
    print(f"orbital speed             v       = {v/1e3:.4f} km/s")
    print(f"revolutions per day       n       = {rev_per_day:.4f} rev/day")
    print(f"equatorial track spacing  d       = {2*np.pi*R_EARTH/rev_per_day/1e3:.1f} km")
    print("  (the ground track advances 360 deg per day minus one revolution per")
    print("   orbit, so a repeat cycle of k days gives a track spacing that sets")
    print("   the EAST-WEST sampling of the monthly field.)")
    print(f"synthetic separation      rho     = {SEPARATION_KM:.1f} km")
    print(f"repeat cycle              N       = {REPEAT_DAYS:.1f} days -> "
          f"{REPEAT_DAYS*rev_per_day:.1f} revolutions")

    section("2. What the range link measures: the gravity gradient along the link")
    # Two satellites on a circular orbit, separated by an arc rho.  The measured
    # range acceleration is the projection of the DIFFERENCE of the gravitational
    # accelerations onto the separation unit vector, i.e. the second derivative
    # of the potential along the link.
    rho = SEPARATION_KM * 1e3
    th1 = 0.0
    th2 = th1 + rho / a                      # small arc, radians
    r1 = a * np.array([np.cos(th1), np.sin(th1)])
    r2 = a * np.array([np.cos(th2), np.sin(th2)])
    thm = 0.5 * (th1 + th2)
    rm = R_EARTH * np.array([np.cos(thm), np.sin(thm)])
    rho_hat = (r2 - r1) / np.linalg.norm(r2 - r1)
    print(f"chord between the two satellites = {np.linalg.norm(r2-r1)/1e3:.3f} km")

    def accel_mono(r):
        """Monopole (spherically symmetric) gravitational acceleration."""
        return -GM_EARTH * r / np.linalg.norm(r) ** 3

    def accel_point(r, m_point, r_point):
        """Acceleration from a point mass only."""
        d = r - r_point
        return -G * m_point * d / np.linalg.norm(d) ** 3

    # A synthetic surface mass anomaly: a water-equivalent layer t over a disc.
    m_point = RHO_W * EWH_DISC_M * np.pi * (DISC_RADIUS_KM * 1e3) ** 2
    a_mono = np.dot(rho_hat, accel_mono(r2) - accel_mono(r1))
    a_anom = np.dot(rho_hat, accel_point(r2, m_point, rm) - accel_point(r1, m_point, rm))
    print(f"SYNTHETIC anomaly: {EWH_DISC_M*100:.1f} cm water equivalent over a "
          f"disc of radius {DISC_RADIUS_KM:.0f} km")
    print(f"  anomaly mass                = {m_point:.4e} kg")
    print(f"  range acceleration, monopole    = {a_mono:+.6e} m/s^2")
    print(f"  range acceleration, anomaly     = {a_anom:+.6e} m/s^2")
    print(f"  signal / background             = {abs(a_anom/a_mono):.3e}"
          "   (about eight orders of magnitude)")
    print(f"  synthetic sample noise          = {NOISE_RANGE_ACC:.1e} m/s^2")
    print(f"  signal / noise, single sample   = {abs(a_anom)/NOISE_RANGE_ACC:.2f}")
    print("  The monopole term is the modelled orbit; the anomaly term is eight")
    print("  orders of magnitude smaller.  That ratio is the whole engineering")
    print("  problem: the gravity signal is a differencing residual.")
    # Exact identity.  With q1 = r1 - r_m and q2 = r2 - r_m and |q1| = |q2| = q
    # by symmetry about the arc midpoint,
    #     rho_hat . (a2 - a1) = -G m (q2.q_hat - q1.q_hat)/q^3 = -G m rho/q^3.
    chord = float(np.linalg.norm(r2 - r1))
    q = np.linalg.norm(r1 - rm)
    exact = -G * m_point * chord / q ** 3
    print(f"  EXACT identity for a point mass: rho_hat.(a2-a1) = -G m rho/q^3")
    print(f"    endpoint distance q = {q/1e3:.3f} km, chord = {chord/1e3:.3f} km")
    print(f"    closed form {exact:.6e} m/s^2  vs  differenced {a_anom:.6e} m/s^2")
    print(f"    agreement = {abs((exact-a_anom)/exact):.2e} relative")
    print(f"    arc length 220.000 km vs chord 219.991 km is the only difference")
    print(f"    when the closed form is given the arc instead: "
          f"{abs(((-G*m_point*rho/q**3)-a_anom)/(-G*m_point*rho/q**3)):.2e} relative")
    # The measured quantity is a DIFFERENCE over a baseline, not a point
    # derivative: compare with rho times the local second derivative of the
    # point-mass potential along the arc.
    def phi_at(th):
        hh = a ** 2 + R_EARTH ** 2 - 2 * a * R_EARTH * np.cos(th - thm)
        return -G * m_point / np.sqrt(hh)
    eps = 1.0e-4
    d2 = (phi_at(thm + eps) - 2.0 * phi_at(thm) + phi_at(thm - eps)) / (eps * a) ** 2
    h_mid = np.linalg.norm(a * np.array([np.cos(thm), np.sin(thm)]) - rm)
    print(f"  local curvature d2(phi)/ds2 at the link midpoint = {d2:.6e} m/s^2")
    print(f"    Gm/h^3 at the midpoint (h = {h_mid/1e3:.1f} km) = "
          f"{G*m_point/h_mid**3:.6e} m/s^2")
    print(f"    chord * curvature = {chord*d2:.6e} m/s^2 vs measured "
          f"{abs(a_anom):.6e} m/s^2 -> agree only to "
          f"{abs((chord*d2-abs(a_anom))/(chord*d2))*100:.2f}%")
    print("  The observable is the second difference of the potential over the")
    print("  baseline, not the gradient at a point: a longer baseline averages")
    print("  over a longer piece of the field.")

    section("3. Resolution limit: downward-continuation noise amplification")
    # A potential coefficient measured at radius a must be continued to the
    # surface; a degree-l coefficient scales as (R/a)^(l+1), so an error at
    # altitude is amplified by (a/R)^(l+1) when it is used at the surface.
    amp = (a / R_EARTH) ** (np.arange(1, 121) + 1)
    print(f"  continuation factor (a/R) = {a/R_EARTH:.5f}")
    print("   degree l   amplification (a/R)^(l+1)   half-wavelength pi R / l (km)")
    for l in (10, 20, 40, 60, 80, 100, 120):
        print(f"   {l:7d}   {amp[l-1]:23.2f}   {np.pi*R_EARTH/l/1e3:26.1f}")
    l10 = int(np.max(np.where(amp < 10.0)[0]) + 1)
    l100 = int(np.max(np.where(amp < 100.0)[0]) + 1)
    print(f"  amplification stays below  10x up to degree {l10}"
          f"  -> half-wavelength {np.pi*R_EARTH/l10/1e3:.0f} km")
    print(f"  amplification stays below 100x up to degree {l100}"
          f"  -> half-wavelength {np.pi*R_EARTH/l100/1e3:.0f} km")
    print("  Noise at altitude is amplified before it reaches the ground, so the")
    print("  usable degree is a noise decision, not a mission-design constant.")
    # A noise realisation: white coefficient noise at altitude, continued down.
    lmax = 120
    noise = RNG.standard_normal(lmax + 1) * 1.0e-12
    sig_at_alt = np.sqrt(np.sum((noise / np.sqrt(2 * np.arange(lmax + 1) + 1)) ** 2))
    sig_at_gr = np.sqrt(np.sum((amp * noise[:lmax] / np.sqrt(2 * np.arange(1, lmax + 1) + 1)) ** 2))
    print(f"  SYNTHETIC white coefficient noise 1e-12 per degree:")
    print(f"    rms geoid error at altitude     = {sig_at_alt:.4e} (arbitrary units)")
    print(f"    rms geoid error continued to surface = {sig_at_gr:.4e} "
          f"-> ratio {sig_at_gr/sig_at_alt:.2f}x")

    section("4. Temporal sampling of a monthly solution")
    n_month = 30.0 * rev_per_day
    print(f"  synthetic repeat cycle        = {REPEAT_DAYS:.0f} days")
    print(f"  revolutions per 30-day solution = {n_month:.0f}")
    print(f"  ground-track spacing at equator = {2*np.pi*R_EARTH/rev_per_day/1e3:.1f} km")
    print("  A month of samples gives densely spaced tracks but NO independent")
    print("  information about periods shorter than the repeat cycle: a 30-day")
    print("  solution is a 30-day average, so shorter variability is aliased.")
    # Aliasing demonstration: a synthetic 3.7-day oscillation, sampled monthly.
    period = 3.7
    t_days = np.arange(0.0, 24.0 * 30.0, 0.05)
    sig = 0.05 * np.sin(2 * np.pi * t_days / period)     # 5.0 cm amplitude
    monthly = sig.reshape(24, 600).mean(axis=1)
    f_sig, f_samp = 1.0 / period, 1.0 / 30.0
    f_alias = abs(f_sig - round(f_sig / f_samp) * f_samp)
    print(f"  SYNTHETIC oscillation of amplitude 5.0 cm, period {period:.1f} days:")
    print(f"    30-day means: min {monthly.min()*100:+.3f} cm, "
          f"max {monthly.max()*100:+.3f} cm, rms {np.std(monthly)*100:.3f} cm")
    print(f"    monthly INSTANTANEOUS samples fold to period "
          f"{1.0/f_alias:.0f} days ({1.0/f_alias/30.0:.1f} months)")
    print("  A sub-monthly signal appears in a monthly solution either as a small")
    print("  bias (if averaged) or as a spurious multi-month oscillation (if")
    print("  sampled).  Neither is the signal, and neither can be undone.")

    section("5. From a Stokes coefficient to a mass: equivalent water height")
    rho_e = M_EARTH / (4.0 / 3.0 * np.pi * R_EARTH ** 3)
    print(f"  Earth mass from GM/G            M      = {M_EARTH:.4e} kg")
    print(f"  mean density of the Earth       rho_e  = {rho_e:.1f} kg/m^3")
    print(f"  (computed, not quoted: M / (4/3 pi R^3))")

    def ewh_from_c(l, dc, k_l):
        """Equivalent water height from a fully normalised coefficient change."""
        return (R_EARTH * rho_e / (3.0 * RHO_W)) * (2.0 * l + 1.0) / (1.0 + k_l) * dc

    dc20 = 1.0e-11
    print(f"  SYNTHETIC change dC_20 = {dc20:.1e} with k_2 = {K_LOVE2:+.2f}:")
    print(f"    equivalent water height = {ewh_from_c(2, dc20, K_LOVE2)*1000:.4f} mm")
    print("    (the same coefficient change spread uniformly over the globe")
    print("     would be a thinner layer, because a low-degree coefficient")
    print("     describes a long-wavelength pattern, not a local deposit)")
    # Independent check at degree 0: a uniform layer of thickness t has
    # dC_00 = 4 pi R^2 (rho_w t) / M, and the same formula must return t.
    t_layer = 0.01
    dc00 = 4.0 * np.pi * R_EARTH ** 2 * RHO_W * t_layer / M_EARTH
    recovered = ewh_from_c(0, dc00, 0.0)
    print(f"  INDEPENDENT CHECK at degree 0 (a uniform layer of {t_layer*100:.1f} cm):")
    print(f"    exact mass balance gives dC_00 = {dc00:.6e}")
    print(f"    the degree-0 formula returns   = {recovered*1000:.6f} mm"
          f"  (relative error {abs(recovered-t_layer)/t_layer:.2e})")
    print("  The (2l+1)/(1+k_l) factor is therefore normalised as expected: the")
    print("  formula reproduces exact mass balance in the one case we can also")
    print("  compute by hand.")


if __name__ == "__main__":
    main()
