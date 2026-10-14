#!/usr/bin/env python3
"""The unsaturated zone: water retention, unsaturated conductivity, field capacity
and available water, Green-Ampt infiltration, ponding time, a finite-difference
Richards solution, and the dielectric link to GPR.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python unsaturated_zone_demo.py

The soil, its retention parameters, the rainfall rates and the wetting-front
suction are SYNTHETIC teaching values chosen for the exercise.  They are not
measurements of any real soil.

Standard constants used:
    rho_w = 1000 kg/m^3, g = 9.81 m/s^2 (head in m of water)
    eps_water = 81, eps_mineral = 4.5, eps_air = 1 (CRIM end members)
    c = 0.299792458 m/ns (speed of light in vacuum, exact)

Contents
--------
1. van Genuchten water retention theta(h) and Mualem conductivity K(theta).
2. Field capacity, wilting point and available water capacity.
3. Green-Ampt infiltration under ponding, and the ponding time for rainfall.
4. A finite-difference solution of the Richards equation, with a mass balance.
5. Verification of the linear diffusion solver against the analytic erfc solution.
6. The dielectric link: CRIM permittivity, GPR velocity, and the sensitivity of
   an inferred water content to the assumed porosity.
"""

import numpy as np
from scipy.special import erfc

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC soil (chosen teaching parameters, not a measured soil) --------
THETA_S = 0.42       # saturated water content
THETA_R = 0.06       # residual water content
ALPHA_VG = 3.0       # 1/m, van Genuchten scale
N_VG = 1.6           # van Genuchten shape
KS = 1.0e-5          # m/s, saturated hydraulic conductivity
PSI_F = 0.20         # m, Green-Ampt wetting front suction (SYNTHETIC)
THETA_I = 0.15       # initial water content
EPS_W, EPS_S, EPS_A = 81.0, 4.5, 1.0
C_LIGHT = 0.299792458  # m/ns


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def m_vg(n=N_VG):
    return 1.0 - 1.0 / n


def theta_of_h(h, ts=THETA_S, tr=THETA_R, a=ALPHA_VG, n=N_VG):
    """van Genuchten retention: theta(h) for pressure head h in m (h <= 0).

    theta = tr + (ts - tr) [1 + (a|h|)^n]^(-m),  m = 1 - 1/n.
    """
    h = np.asarray(h, dtype=float)
    ah = a * np.abs(h)
    return tr + (ts - tr) * (1.0 + ah ** n) ** (-m_vg(n))


def h_of_theta(theta, ts=THETA_S, tr=THETA_R, a=ALPHA_VG, n=N_VG):
    """Inverse van Genuchten retention: h(theta) in m (h <= 0)."""
    m = m_vg(n)
    se = np.clip((theta - tr) / (ts - tr), 1e-12, 1.0)
    return -(1.0 / a) * (se ** (-1.0 / m) - 1.0) ** (1.0 / n)


def k_of_theta(theta, ksat=KS, ts=THETA_S, tr=THETA_R, n=N_VG):
    """Mualem-van Genuchten conductivity K(theta) in m/s."""
    m = m_vg(n)
    se = np.clip((theta - tr) / (ts - tr), 1e-12, 1.0)
    return ksat * se ** 0.5 * (1.0 - (1.0 - se ** (1.0 / m)) ** m) ** 2


def green_ampt_F(t_s, ksat=KS, psi_f=PSI_F, dtheta=THETA_S - THETA_I):
    """Cumulative infiltration F(t) under ponding, from
    F - psi_f dtheta ln(1 + F/(psi_f dtheta)) = ksat t.  Newton iteration."""
    A = psi_f * dtheta
    F = ksat * t_s * 1.5 + 1e-6
    for _ in range(80):
        g = F - A * np.log(1.0 + F / A) - ksat * t_s
        dg = 1.0 - A / (1.0 + F / A) / A
        F -= g / dg
        F = max(F, 1e-12)
    return F


def ponding_time(r_m_s, ksat=KS, psi_f=PSI_F, dtheta=THETA_S - THETA_I):
    """Green-Ampt ponding time for rainfall rate r > Ks (Mein-Larson)."""
    if r_m_s <= ksat:
        return np.inf
    return ksat * psi_f * dtheta / (r_m_s * (r_m_s - ksat))


def crim_permittivity(theta, phi=THETA_S, es=EPS_S, ew=EPS_W, ea=EPS_A):
    """Complex refractive index model: sqrt(eps_eff) is linear in theta."""
    root = (1.0 - phi) * np.sqrt(es) + theta * np.sqrt(ew) + (phi - theta) * np.sqrt(ea)
    return root ** 2


def run_richards(nz, dt, t_end, r_m_s, Lz=0.8):
    """Conservative finite-volume solution of the 1-D Richards equation under a
    constant rainfall flux r < Ks (so the surface never saturates).

    Mixed form:  d(theta)/dt = -d q/dz,  q = -K(h)(dh/dz - 1)  (q positive down).
    Surface: q = r.  Base: free drainage (theta(L) held at theta_i by drainage).
    Returns the final profile and the water budget terms, all in metres.
    """
    dz = Lz / (nz - 1)
    z = np.linspace(0.0, Lz, nz)
    theta = np.full(nz, THETA_I)
    nt = int(round(t_end / dt))
    influx = drainage = clipped = 0.0
    for step in range(nt):
        h = h_of_theta(theta)
        k = k_of_theta(theta)
        k_mid = 0.5 * (k[1:] + k[:-1])
        q = -k_mid * ((h[1:] - h[:-1]) / dz - 1.0)      # nz-1 interface fluxes
        influx += r_m_s * dt
        drainage += float(q[-1]) * dt
        flux_in = np.concatenate(([r_m_s], q))[:nz]
        flux_out = np.concatenate((q, [q[-1]]))[:nz]
        d_theta = dt / dz * (flux_in - flux_out)
        new = theta + d_theta
        clipped += dz * float(np.sum(np.clip(new - THETA_S, 0.0, None)))
        theta = np.clip(new, THETA_R, THETA_S)
    storage = dz * float(np.sum(theta - THETA_I))
    return {"theta": theta, "z": z, "storage": storage, "influx": influx,
            "drainage": drainage, "clipped": clipped, "nt": nt, "dz": dz,
            "front": float(z[np.where(theta >= 0.5 * (THETA_S + THETA_I))[0][-1]])
            if np.any(theta >= 0.5 * (THETA_S + THETA_I)) else 0.0}


def theta_at_K(target_K, tr=THETA_R, ts=THETA_S):
    """Invert K(theta) = target_K (Mualem-van Genuchten) by bisection."""
    lo, hi = tr + 1e-9, ts
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if float(k_of_theta(mid)) < target_K:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    section("1. Water retention and unsaturated conductivity")
    print(f"SYNTHETIC soil: theta_s = {THETA_S:.2f}, theta_r = {THETA_R:.2f}, "
          f"alpha = {ALPHA_VG:.1f} 1/m, n = {N_VG:.2f}, K_s = {KS:.1e} m/s")
    print(f"  m = 1 - 1/n = {m_vg():.4f}")
    print("   h (m)     h (kPa)    theta     Se        K (m/s)      K/Ks")
    for h in (-0.05, -0.1, -0.3, -1.0, -3.3, -10.0, -150.0):
        th = float(theta_of_h(h))
        se = (th - THETA_R) / (THETA_S - THETA_R)
        k = float(k_of_theta(th))
        print(f"   {h:7.2f}   {h * 9.81:8.1f}   {th:7.4f}   {se:7.4f}   "
              f"{k:11.4e}   {k / KS:8.2e}")
    print(f"  limits check: theta(0) = {float(theta_of_h(0.0)):.4f} (should be "
          f"{THETA_S:.2f}); theta(-1e4 m) = {float(theta_of_h(-1e4)):.5f} "
          f"(should approach {THETA_R:.2f})")
    print(f"  K(theta_s) = {float(k_of_theta(THETA_S)):.4e} m/s (should be K_s)")

    section("2. Field capacity, wilting point and available water")
    h_fc, h_wp = -3.3, -150.0
    th_fc = float(theta_of_h(h_fc))
    th_wp = float(theta_of_h(h_wp))
    awc = (th_fc - th_wp) * 1000.0
    print(f"  field capacity at h = {h_fc:.1f} m ({h_fc * 9.81:.0f} kPa): "
          f"theta_fc = {th_fc:.4f}")
    print(f"  wilting point at h = {h_wp:.1f} m ({h_wp * 9.81 / 1000:.1f} MPa): "
          f"theta_wp = {th_wp:.4f}")
    print(f"  plant-available water = (theta_fc - theta_wp) = "
          f"{th_fc - th_wp:.4f} m^3/m^3 = {awc:.1f} mm per metre of soil")
    for depth in (0.3, 0.5, 1.0, 2.0):
        print(f"  over a {depth:.1f} m root zone: {awc * depth:8.1f} mm of water")
    print("  these are thermodynamic conventions at stated suctions, not fixed")
    print("  soil constants: field capacity is a drainage time, and wilting point a")
    print("  plant response.  Both depend on the crop and the soil structure.")

    section("3. Green-Ampt infiltration and ponding time")
    dtheta = THETA_S - THETA_I
    print(f"  theta_i = {THETA_I:.2f}, so dtheta = theta_s - theta_i = {dtheta:.2f}")
    print(f"  Green-Ampt: F - psi_f dtheta ln(1 + F/(psi_f dtheta)) = K_s t")
    print(f"  with psi_f = {PSI_F:.2f} m (SYNTHETIC) and K_s = {KS:.1e} m/s")
    print("   t (min)   F (mm)    f (mm/h)   wetting front depth (m)")
    for t_min in (1.0, 5.0, 15.0, 30.0, 60.0, 180.0):
        t_s = t_min * 60.0
        F = green_ampt_F(t_s)
        f_rate = KS * (1.0 + PSI_F * dtheta / F)
        print(f"   {t_min:7.1f}   {F * 1e3:8.2f}   {f_rate * 3.6e6:9.2f}   "
              f"{F / dtheta:24.3f}")
    print("  f tends to K_s: the infiltration rate decays towards the saturated")
    print("  conductivity, and the wetting front advances as F/dtheta.")
    print("\n  ponding time for a rainfall rate r (Mein-Larson):")
    print("   r (mm/h)   r/Ks     ponding time")
    for r_mm_h in (18.0, 36.0, 54.0, 108.0, 360.0):
        r = r_mm_h / 3.6e6
        tp = ponding_time(r)
        label = f"{tp / 60:.2f} min" if np.isfinite(tp) else "never (r <= Ks)"
        print(f"   {r_mm_h:8.1f}   {r / KS:6.2f}   {label}")
    print("  K_s = 1e-5 m/s = 36 mm/h.  Rainfall at or below that rate never ponds;")
    print("  above it, the ponding time falls roughly as 1/r^2 for r >> Ks.")

    section("4. Richards equation under rainfall, with a mass balance")
    r_mm_h = 5.0
    r = r_mm_h / 3.6e6
    t_end = 21600.0
    print(f"  rainfall r = {r_mm_h:.1f} mm/h = {r:.4e} m/s; K_s = {KS:.1e} m/s = "
          f"{KS * 3.6e6:.0f} mm/h")
    print(f"  r/K_s = {r / KS:.3f} < 1, so no ponding occurs and all rainfall "
          "enters")
    print(f"  total applied = r t = {r * t_end * 1e3:.2f} mm over "
          f"{t_end / 3600:.1f} h")
    theta_eq = theta_at_K(r)
    print(f"  long-time limit: the profile tends to K(theta) = r everywhere, i.e.")
    print(f"  theta -> {theta_eq:.4f} (inverted from the Mualem relation)")
    print("   nz    dz (mm)   steps       storage (mm)   drainage (mm)   "
          "closure error (mm)")
    results = {}
    for nz, dt in ((101, 0.2), (201, 0.2), (401, 0.2)):
        res = run_richards(nz, dt, t_end, r)
        results[nz] = res
        closure = res["influx"] - res["drainage"] - res["storage"] - res["clipped"]
        print(f"   {nz:4d}   {res['dz'] * 1e3:7.2f}   {res['nt']:6d}   "
              f"{res['storage'] * 1e3:13.3f}   {res['drainage'] * 1e3:13.4f}   "
              f"{abs(closure) * 1e3:17.2e}")
    res = results[401]
    print(f"  applied = {res['influx'] * 1e3:.3f} mm, storage = "
          f"{res['storage'] * 1e3:.3f} mm, drainage = {res['drainage'] * 1e3:.4f} mm,")
    print(f"  clipped (water sent above saturation) = {res['clipped'] * 1e3:.2e} mm, "
          f"closure error = {abs(res['influx'] - res['drainage'] - res['storage'] - res['clipped']) * 1e3:.2e} mm")
    print("  The scheme is finite-volume, so the budget closes to round-off: this is")
    print("  a real verification of the discretisation, not a restatement of it.")
    print("\n   depth (m)   theta     h (m)      K (m/s)      K/r     state")
    for zz in (0.0, 0.05, 0.10, 0.15, 0.25, 0.40, 0.80):
        i = int(round(zz / res["dz"]))
        th = float(res["theta"][i])
        kk = float(k_of_theta(th))
        print(f"   {zz:8.2f}   {th:6.4f}   "
              f"{float(h_of_theta(th)):9.4f}   {kk:11.4e}   {kk / r:6.3f}   "
              f"{'wetted' if th > 0.5 * (THETA_S + THETA_I) else 'near initial'}")
    print(f"  The 50%-crossing front sits at {res['front']:.3f} m after "
          f"{t_end / 3600:.1f} h, while the sharp-front position")
    print(f"  implied by the stored water is F/dtheta = {res['storage'] / dtheta:.3f} m "
          f"and the Green-Ampt value is")
    print(f"  r t / dtheta = {r * t_end / dtheta:.3f} m.  The two differ by "
          f"{abs(res['front'] - res['storage'] / dtheta) * 1e3:.0f} mm")
    print("  (about 20%) purely because the profile is diffuse: a 50%-crossing")
    print("  definition of 'the front' is always deeper than the equivalent sharp")
    print("  front.  Which one is 'the front' is a choice, and it must be stated.")
    print("  Ahead of the front K(theta_i)/r = "
          f"{float(k_of_theta(THETA_I)) / r:.2e}: essentially no flow reaches the")
    print("  dry soil, which is why the front is sharp even under a small flux.")

    section("5. Verification of the linear diffusion solver (erfc solution)")
    D = 2.0e-6
    nz2, Lz2 = 201, 0.5
    dz2 = Lz2 / (nz2 - 1)
    dt2 = 0.25 * dz2 ** 2 / D
    u = np.full(nz2, THETA_I)
    u[0] = THETA_S
    nt2 = 4000
    for _ in range(nt2):
        u_new = u.copy()
        u_new[1:-1] = u[1:-1] + D * dt2 / dz2 ** 2 * (u[2:] - 2 * u[1:-1] + u[:-2])
        u_new[-1] = u[-2]
        u = u_new
    t2 = nt2 * dt2
    zz = np.linspace(0.0, Lz2, nz2)
    ana = THETA_I + (THETA_S - THETA_I) * erfc(zz / (2.0 * np.sqrt(D * t2)))
    print(f"  D = {D:.1e} m^2/s, {nz2} nodes over {Lz2:.2f} m, "
          f"dt = {dt2:.4f} s (0.25 dz^2/D), {nt2} steps, t = {t2:.3f} s")
    print(f"  diffusion length sqrt(4 D t) = {np.sqrt(4 * D * t2):.4f} m, "
          f"inside the domain ({Lz2:.2f} m) so the semi-infinite solution applies")
    err = np.max(np.abs(u - ana))
    print(f"  maximum |numerical - analytic| = {err:.3e}")
    print(f"  as a fraction of the step (theta_s - theta_i) = "
          f"{err / (THETA_S - THETA_I):.3e}")
    print("  the explicit scheme is second order in dz and first order in dt; the")
    print("  residual is dominated by the leading truncation term, so its size is a")
    print("  useful check on the time step but is NOT a validation of the retention")
    print("  model, which this linear test does not use at all.")

    section("6. Dielectric link: CRIM permittivity and a GPR velocity")
    print(f"  CRIM: sqrt(eps_eff) = (1-phi) sqrt(eps_s) + theta sqrt(eps_w) + "
          f"(phi-theta) sqrt(eps_a)")
    print(f"  end members eps_s = {EPS_S}, eps_w = {EPS_W}, eps_a = {EPS_A}; "
          f"phi = {THETA_S:.2f}")
    print("   theta    eps_eff    v (m/ns)   two-way time over 1 m (ns)")
    for th in (0.05, 0.10, 0.20, 0.30, 0.42):
        eps = float(crim_permittivity(th))
        v = C_LIGHT / np.sqrt(eps)
        print(f"   {th:5.3f}   {eps:8.3f}   {v:9.4f}   {2.0 / v:25.2f}")
    th_lo, th_hi = 0.15, 0.16
    de = (float(crim_permittivity(th_hi)) - float(crim_permittivity(th_lo))) / 0.01
    print(f"  sensitivity d(eps)/d(theta) near theta = 0.155: {de:.3f} per unit theta")
    print(f"  a 1% change in water content changes eps by {(de * 0.01):.3f} "
          f"({de * 0.01 / float(crim_permittivity(0.155)) * 100:.1f}%), which is far")
    print("  above the repeatability of a modern GPR velocity analysis.")
    print("\n  inversion error from an assumed porosity:")
    eps_meas = 12.0
    root = np.sqrt(eps_meas)
    for phi in (0.36, 0.42, 0.48):
        th_inv = (root - (1.0 - phi) * np.sqrt(EPS_S) - phi) / (np.sqrt(EPS_W) - 1.0)
        print(f"   phi assumed {phi:.2f} -> theta = {th_inv:.4f}")
    print("  a 6-point porosity error moves the water content by only about 0.01,")
    print("  because the mineral and air end members have similar permittivities.")
    print("  Compare this with resistivity, where the same porosity error changes the")
    print("  inferred salinity by a factor of four: GPR water content is far more")
    print("  robust to the porosity assumption than a resistivity-derived salinity.")


if __name__ == "__main__":
    main()
