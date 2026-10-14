#!/usr/bin/env python3
"""GPR survey design: spatial sampling rules, grid and time-window sizing, CMP
offset ranges, cross-hole ray coverage, and detection probability versus line
spacing.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_survey_design_demo.py

Everything here is SYNTHETIC.  The site dimensions, target depths, permittivities
and the acquisition rate are CHOSEN DESIGN ASSUMPTIONS, labelled where used; the
only physical constants are the speed of light and the permeability of vacuum.

Contents
--------
1. Sampling rules: the maximum unaliased dip for a given trace spacing, and the
   spacings required by the lambda/2 and lambda/4 rules.
2. Grid sizing for a chosen SYNTHETIC site: lines, traces, volume, time.
3. Time-window sizing from the deepest target plus a guard.
4. CMP design: the offset range that carries a measurable moveout, and the
   velocity error implied by a pick error at maximum offset.
5. Cross-hole (transillumination) ray coverage: hits per pixel and ray angles.
6. Detection probability versus line spacing, by geometry and by Monte Carlo.
7. Verification: the designed grid against the target dip and wavelength.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_M_NS = 0.299792458

# SYNTHETIC design assumptions (chosen, not measured)
SITE_X_M, SITE_Y_M = 40.0, 20.0     # survey area
TRACE_STEP_M = 0.05                 # along-line sampling
LINE_STEP_M = 0.25                  # between-line sampling
TARGET_DEPTH_M = 1.50               # shallowest target of interest
DEEPEST_TARGET_M = 3.00             # deepest target to be recorded
EPS_R = 9.0                         # wet sand
V_M_NS = C_M_NS / np.sqrt(EPS_R)
F_MHZ = 200.0                       # nominal antenna frequency
DT_NS = 0.025                       # time sampling
TRACES_PER_S = 15.0                 # chosen acquisition rate


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main():
    lam = V_M_NS / (F_MHZ / 1000.0)
    print(f"SYNTHETIC design: v = {V_M_NS:.5f} m/ns (eps_r = {EPS_R:.1f}), "
          f"f = {F_MHZ:.0f} MHz, lambda = {lam:.4f} m")

    section("1. Spatial sampling rules")
    print("   A zero-offset section records a time dip dt/dx = 2 sin(theta)/v, so")
    print("   its spatial wavenumber is k_x = 2 omega sin(theta)/v.  Nyquist")
    print("   requires |k_x| <= pi/dx, which gives")
    print("       sin(theta_max) = v / (4 f dx) = lambda / (4 dx).")
    print("   dx (m)  dx/lambda   theta_max (deg)   rule")
    for dx, rule in ((lam / 4.0, "lambda/4"), (lam / 2.0, "lambda/2"),
                     (lam, "lambda"), (2 * lam, "2 lambda")):
        s = min(1.0, lam / (4.0 * dx))
        print(f"   {dx:6.3f}  {dx/lam:9.3f}   {np.degrees(np.arcsin(s)):15.2f}   "
              f"{rule}")
    print("   Only dx <= lambda/4 records every dip without aliasing; dx = lambda/2")
    print("   is the usual compromise, and it aliases dips steeper than 30 deg.")
    print("\n   required along-line step for dip limits, three frequencies and two")
    print("   permittivities (dx = lambda/(4 sin theta_max)):")
    print("   f (MHz)  theta_max   eps_r = 4   eps_r = 16")
    for f_mhz in (100.0, 200.0, 400.0, 900.0):
        for th in (90.0, 45.0, 30.0):
            req = [C_M_NS / np.sqrt(e) * (1000.0 / f_mhz)
                   / (4.0 * np.sin(np.radians(th))) for e in (4.0, 16.0)]
            print(f"   {f_mhz:7.0f}  {th:9.0f}   {req[0]:9.3f} m  {req[1]:9.3f} m")

    section("2. Grid sizing for the chosen SYNTHETIC site")
    n_lines = int(np.ceil(SITE_Y_M / LINE_STEP_M)) + 1
    n_traces_line = int(np.ceil(SITE_X_M / TRACE_STEP_M)) + 1
    total = n_lines * n_traces_line
    print(f"   site {SITE_X_M:.0f} m x {SITE_Y_M:.0f} m, along-line step "
          f"{TRACE_STEP_M:.3f} m, line spacing {LINE_STEP_M:.3f} m")
    print(f"   lines: {n_lines}, traces per line: {n_traces_line}, "
          f"total traces: {total}")
    t_window = 2.0 * DEEPEST_TARGET_M / V_M_NS + 20.0     # + 20 ns guard
    n_samples = int(np.ceil(t_window / DT_NS))
    print(f"   time window: 2 x {DEEPEST_TARGET_M:.2f} m / "
          f"{V_M_NS:.5f} m/ns + 20 ns guard = {t_window:.1f} ns "
          f"-> {n_samples} samples at {DT_NS:.3f} ns")
    vol_mb = total * n_samples * 2.0 / 1e6
    print(f"   data volume at 2 bytes per sample: {vol_mb:.1f} MB")
    print(f"   at the chosen rate of {TRACES_PER_S:.0f} traces/s: "
          f"{total/TRACES_PER_S/60.0:.1f} minutes of recording")
    print(f"   linear profiling distance: {total*TRACE_STEP_M:.0f} m of line, "
          f"or {n_lines} passes of {SITE_X_M:.0f} m")
    print("   The volume and the time are INPUTS to the design, not outputs: the")
    print("   resolution rule decides the spacing and everything else follows.")

    section("3. CMP design: offset range carrying a measurable moveout")
    t0 = 2.0 * TARGET_DEPTH_M / V_M_NS
    print(f"   target at {TARGET_DEPTH_M:.2f} m: t0 = {t0:.2f} ns; "
          f"t^2 = t0^2 + x^2/v^2")
    print("   moveout (ns)   required x (m)   x/depth")
    for ddt in (2.0, 5.0, 10.0, 20.0):
        x = V_M_NS * np.sqrt((t0 + ddt) ** 2 - t0 ** 2)
        print(f"   {ddt:12.1f}   {x:14.3f}   {x/TARGET_DEPTH_M:7.2f}")
    x_max = V_M_NS * np.sqrt((t0 + 10.0) ** 2 - t0 ** 2)
    n_off = int(np.ceil(x_max / 0.10))
    print(f"   a chosen 10 ns of moveout needs x_max = {x_max:.2f} m "
          f"({x_max/TARGET_DEPTH_M:.1f} target depths)")
    print(f"   at 0.10 m minimum separation that is {n_off} offsets; below about")
    print(f"   one target depth of offset the moveout is under 5 ns and the")
    print("   velocity becomes poorly determined (see the velocity-analysis demo).")
    print("\n   velocity error from a time-pick error at maximum offset:")
    print("   t^2 = t0^2 + x^2/v^2 -> dv = v^3 t dt / x^2")
    for dt_pick in (0.025, 0.25):
        for x in (1.0, 2.0, 4.0):
            t = np.sqrt(t0 ** 2 + x ** 2 / V_M_NS ** 2)
            dv = V_M_NS ** 3 * t * dt_pick / x ** 2
            print(f"     pick error {dt_pick:5.3f} ns, x = {x:.1f} m -> "
                  f"dv = {dv:.5f} m/ns ({dv/V_M_NS*100:5.2f}%)")
    print("   The error falls as x^-2: doubling the maximum offset quarters the")
    print("   velocity uncertainty, which is why a CMP or wide-offset profile is")
    print("   worth the extra effort.")

    section("4. Cross-hole geometry: ray coverage and angles")
    bh_sep, bh_depth = 5.0, 10.0
    n_src = n_rec = 21
    src_z = np.linspace(0.0, bh_depth, n_src)
    rec_z = np.linspace(0.0, bh_depth, n_rec)
    nx, nz = 50, 100
    xg = np.linspace(bh_sep / nx, bh_sep * (nx - 1) / nx, nx)
    zg = np.linspace(bh_depth / nz, bh_depth * (nz - 1) / nz, nz)
    hits = np.zeros((nz, nx))
    angles = []
    for zs in src_z:
        for zr in rec_z:
            # straight ray from (0, zs) to (bh_sep, zr)
            slope = (zr - zs) / bh_sep
            ang = np.arctan(slope)
            for iz, z in enumerate(zg):
                x = (z - zs) / slope if abs(slope) > 1e-12 else None
                if x is not None and 0.0 < x < bh_sep:
                    jx = int(round(x / bh_sep * nx - 0.5))
                    if 0 <= jx < nx:
                        hits[iz, jx] += 1.0
                        angles.append(abs(np.degrees(ang)))
    print(f"   SYNTHETIC panel: boreholes {bh_sep:.1f} m apart, "
          f"{n_src} sources and {n_rec} receivers over {bh_depth:.0f} m")
    print(f"   straight rays: {n_src*n_rec} source-receiver pairs")
    print(f"   pixels with at least one ray: {int(np.sum(hits > 0))} of "
          f"{hits.size} ({np.sum(hits > 0)/hits.size*100:.1f}%)")
    print(f"   pixels with at least 5 rays: {int(np.sum(hits >= 5))} "
          f"({np.sum(hits >= 5)/hits.size*100:.1f}%)")
    print(f"   hits per pixel: min {hits.min():.0f}, mean {hits.mean():.2f}, "
          f"max {hits.max():.0f}")
    print("   The uncovered pixels lie in the two triangles at the top corners and")
    print("   at the bottom centre: no straight ray reaches them.  Coverage, not")
    print("   the number of rays, is what a tomographic inversion can use.")
    print("\n   angular aperture at the panel centre (the ray-crossing angle of a")
    print("   vertical pair vs a dipping pair), from the same geometry:")
    z_mid = bh_depth / 2.0
    a_vert = 0.0
    a_diag = np.degrees(np.arctan((bh_depth - z_mid) / bh_sep)) \
        - np.degrees(np.arctan((0.0 - z_mid) / bh_sep))
    print(f"     a ray at mid depth nearly horizontal: crossing angle about "
          f"{a_diag:.1f} deg")
    print(f"     a ray that is vertical at mid depth: {a_vert:.1f} deg to itself")
    print("   The maximum crossing angle sets the transverse resolution; the")
    print("   coverage map sets where the answer is trustworthy at all.")

    section("5. Detection probability versus line spacing")
    d_target = TARGET_DEPTH_M
    r_fres = np.sqrt(lam * d_target / 2.0 + lam ** 2 / 16.0)
    D = 2.0 * r_fres
    print(f"   target at {d_target:.2f} m; first Fresnel diameter "
          f"D = {D:.3f} m = {D/lam:.2f} lambda")
    print("   a target is detected if a line passes within D/2, so the geometric")
    print("   probability is min(1, D/line_spacing); Monte Carlo places 20000")
    print("   random targets (RNG seed 20261014) and counts the hits:")
    print("   line spacing (m)   spacing/lambda   geometric   Monte Carlo")
    for spacing in (0.10, 0.50, 1.00, 1.25, 1.50, 2.00, 4.00):
        n = 20000
        y_target = RNG.uniform(0.0, SITE_Y_M, n)
        y_lines = np.arange(0.0, SITE_Y_M + 1e-9, spacing)
        dist = np.min(np.abs(y_target[:, None] - y_lines[None, :]), axis=1)
        mc = float(np.mean(dist <= D / 2.0))
        geo = min(1.0, D / spacing)
        print(f"   {spacing:15.2f}   {spacing/lam:14.3f}   {geo:9.3f}   "
              f"{mc:11.3f}")
    print("   The Monte Carlo counts coincide with the geometric expression.  A")
    print("   line spacing finer than the Fresnel diameter adds no detection")
    print("   probability, only resolution: the two requirements are different.")

    section("6. Verification: does the designed grid meet the target dips?")
    theta_target = 45.0
    dx_required = lam / (4.0 * np.sin(np.radians(theta_target)))
    print(f"   chosen along-line step {TRACE_STEP_M:.3f} m; for dips up to")
    print(f"   {theta_target:.0f} deg the requirement is "
          f"{dx_required:.3f} m -> "
          f"{'MET' if TRACE_STEP_M <= dx_required else 'NOT MET'}")
    s_max = min(1.0, lam / (4.0 * TRACE_STEP_M))
    print(f"   the chosen step records dips up to "
          f"{np.degrees(np.arcsin(s_max)):.1f} deg at {F_MHZ:.0f} MHz")
    print(f"   chosen line spacing {LINE_STEP_M:.3f} m vs the Fresnel diameter")
    print(f"   {D:.3f} m -> "
          f"{'adequate' if LINE_STEP_M <= D else 'INSIDE THE FRESNEL ZONE'}")
    print("   Every number above comes from the SYNTHETIC design assumptions of")
    print("   this script; no field survey or instrument specification is quoted.")


if __name__ == "__main__":
    main()
