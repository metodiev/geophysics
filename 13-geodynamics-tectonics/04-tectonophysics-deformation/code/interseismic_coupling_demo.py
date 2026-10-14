#!/usr/bin/env python3
"""Interseismic coupling: the surface-velocity profile of a partially locked
megathrust, and the depth-coupling trade-off that limits what the profile can say.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python interseismic_coupling_demo.py

Everything is SYNTHETIC.  The plate rate, the coupling distribution and the
noise are chosen teaching values.  No real subduction zone, GNSS site or
published coupling model is used or quoted.  The elastic model is the exact
2-D anti-plane (screw dislocation) solution for a vertical fault, which is a
teaching analogue of a dipping megathrust and is labelled as such.

Contents
--------
1. The 2-D locked-fault profile and its limiting cases.
2. Back-slip superposition onto a patchwise coupling distribution, checked
   against the single-patch closed form.
3. The depth-coupling trade-off: two different coupling models, one data set.
4. Inverting for coupling on ten patches, with a resolution and covariance view.
5. From coupling to moment deficit and recurrence.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
V_PLATE_MM_YR = 40.0        # long-term slip rate, SYNTHETIC
NOISE_MM_YR = 1.0           # SYNTHETIC velocity noise per component
MAX_DEPTH_KM = 80.0         # base of the modelled fault zone
N_PATCH = 10                # patches for the discretised coupling model
SHEAR_MODULUS_PA = 30.0e9   # SYNTHETIC shear modulus
FAULT_LENGTH_KM = 200.0     # SYNTHETIC along-strike length of the coupled zone
SITES_X_KM = np.array([5.0, 10.0, 20.0, 35.0, 50.0, 75.0, 110.0, 160.0,
                       220.0, 300.0, -5.0, -15.0, -30.0, -60.0, -120.0,
                       -200.0])


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def patch_bounds():
    """Depth bounds of the coupling patches, km."""
    return np.linspace(0.0, MAX_DEPTH_KM, N_PATCH + 1)


def kernel_matrix(x_km):
    """K[i, j]: surface velocity at x_i from unit coupling on patch j.

    The back-slip contribution of a patch spanning [z_j, z_{j+1}] is
    -(V/pi)[atan2(z_{j+1}, x) - atan2(z_j, x)], normalised here to the plate
    rate so that the entries are dimensionless weights.
    """
    z = patch_bounds()
    K = np.zeros((x_km.size, N_PATCH))
    for j in range(N_PATCH):
        K[:, j] = -(np.arctan2(z[j + 1], x_km) - np.arctan2(z[j], x_km)) / np.pi
    return K


def forward(coupling, x_km):
    """Surface fault-parallel velocity, mm/yr, for a coupling distribution."""
    half = 0.5 * V_PLATE_MM_YR * np.sign(x_km)
    return half + V_PLATE_MM_YR * (kernel_matrix(x_km) @ coupling)


def single_patch_profile(d_km, coupling, x_km):
    """Closed form for one patch spanning [0, d]: exact, used as a check."""
    half = 0.5 * V_PLATE_MM_YR * np.sign(x_km)
    return half - coupling * V_PLATE_MM_YR * np.arctan2(d_km, x_km) / np.pi \
        + coupling * V_PLATE_MM_YR * np.where(x_km < 0.0, 1.0, 0.0)


def main():
    section("1. The 2-D locked-fault profile")
    print("  Model: a vertical fault at x = 0 in anti-plane strain.  The medium")
    print("  moves only along strike; the fault slips at the long-term rate below")
    print("  the coupled zone and not inside it.  Superposing a uniform creep of")
    print(f"  {V_PLATE_MM_YR:.0f} mm/yr with the back-slip on [0, d]:")
    print("      v(x) = (V/2) sgn(x) - (V/pi)[atan2(d,x) - atan2(0,x)] chi")
    print("  Limiting cases, which the closed form reproduces exactly:")
    x = np.array([0.001, 10.0, 50.0, 1e6])
    for chi, label in ((1.0, "chi = 1 (fully locked)"),
                       (0.5, "chi = 0.5 (half coupled)"),
                       (0.0, "chi = 0 (no coupling)")):
        prof = single_patch_profile(30.0, chi, x)
        print(f"    {label:24s}: v(0+) = {prof[0]:6.2f}, v(10 km) = "
              f"{prof[1]:6.2f}, v(50 km) = {prof[2]:6.2f}, "
              f"v(inf) = {prof[3]:6.2f} mm/yr")
    print("  The relative velocity across the fault is V(1-chi) at the surface and")
    print("  V far away, which is exactly the statement that the deficit is being")
    print("  stored inside the coupled zone.")

    section("2. Discretised back-slip versus the closed form")
    d = 30.0
    chi_dense = np.where(patch_bounds()[:-1] < d, 1.0, 0.0)
    # fade the patch that straddles d so that the discrete model represents the
    # same continuous coupling as the closed form.
    z = patch_bounds()
    for j in range(N_PATCH):
        lo, hi = z[j], z[j + 1]
        if lo < d < hi:
            chi_dense[j] = (d - lo) / (hi - lo)
    print(f"  Closed form: one patch [0, {d:.0f} km] with coupling 1.")
    print(f"  Discrete: {N_PATCH} patches to {MAX_DEPTH_KM:.0f} km, with the patch")
    print(f"  straddling {d:.0f} km partially coupled so the two describe the same")
    print("  continuous distribution.")
    xs = np.concatenate((SITES_X_KM, np.array([0.5, 2.0, 4.0, 8.0, 15.0, 25.0])))
    closed = single_patch_profile(d, 1.0, xs)
    disc = forward(chi_dense, xs)
    print(f"  max |discrete - closed form| = {np.max(np.abs(disc - closed)):.4f} "
          f"mm/yr over {xs.size} stations")
    print("  The discretisation error is far below the 1 mm/yr noise, so the")
    print("  patch model can be used in place of the closed form.")

    section("3. The depth-coupling trade-off")
    x_sites = SITES_X_KM
    z_hi = patch_bounds()
    deep = np.zeros(N_PATCH)
    for j in range(N_PATCH):
        lo, hi = z_hi[j], z_hi[j + 1]
        if lo < 40.0:
            deep[j] = 0.60 * min(1.0, (40.0 - lo) / (hi - lo))
    shallow = np.where(z_hi[:-1] < 20.0, 1.0, 0.0)
    for j in range(N_PATCH):
        lo, hi = z_hi[j], z_hi[j + 1]
        if lo < 20.0 < hi:
            shallow[j] = (20.0 - lo) / (hi - lo)
    v_shallow = forward(shallow, x_sites)
    v_deep = forward(deep, x_sites)
    print("  Model A: coupling 1.0 from 0 to 20 km.")
    print("  Model B: coupling 0.6 from 0 to 40 km.")
    print("  Both store the same slip deficit rate, 20 x V and 0.6 x 40 x V.")
    print("\n    x (km)   v A (mm/yr)   v B (mm/yr)   A - B")
    for xi, va, vb in zip(x_sites, v_shallow, v_deep):
        print(f"    {xi:7.1f}   {va:11.3f}   {vb:11.3f}   {va - vb:+8.4f}")
    diff = v_shallow - v_deep
    near = np.abs(x_sites) <= 30.0
    far = np.abs(x_sites) >= 50.0
    print(f"\n  near the fault (|x| <= 30 km) the two models differ by up to "
          f"{np.max(np.abs(diff[near])):.3f} mm/yr,")
    print(f"  which is {np.max(np.abs(diff[near])) / NOISE_MM_YR:.1f} times the "
          f"{NOISE_MM_YR:.1f} mm/yr SYNTHETIC noise.")
    print(f"  inland (|x| >= 50 km) they differ by at most "
          f"{np.max(np.abs(diff[far])):.3f} mm/yr,")
    print(f"  which is {np.max(np.abs(diff[far])) / NOISE_MM_YR:.1f} times the noise.")
    print("  Coupling depth and coupling value trade off strongly: only stations")
    print("  close to the fault trace resolve the depth extent, and a land network")
    print("  that starts tens of kilometres inland cannot see it at all.  That is")
    print("  why offshore or seafloor geodesy, and independent observables such as")
    print("  seismicity and tsunami data, matter so much for coupling models.")

    section("4. Inverting for coupling on ten patches")
    chi_true = np.zeros(N_PATCH)
    chi_true[:5] = 1.0            # fully coupled to 40 km, free below
    v_clean = forward(chi_true, x_sites)
    K = kernel_matrix(x_sites) * V_PLATE_MM_YR            # mm/yr per unit chi
    D = np.zeros((N_PATCH - 1, N_PATCH))                  # first differences
    for j in range(N_PATCH - 1):
        D[j, j], D[j, j + 1] = -1.0, 1.0
    lam = 2.0                                             # mm/yr per unit chi
    G = np.vstack([K, lam * D])
    n_real = 200
    recovered = np.zeros((n_real, N_PATCH))
    for i in range(n_real):
        v_obs = v_clean + NOISE_MM_YR * RNG.standard_normal(v_clean.size)
        b = np.concatenate([v_obs - 0.5 * V_PLATE_MM_YR * np.sign(x_sites),
                            np.zeros(N_PATCH - 1)])
        chi_hat, *_ = np.linalg.lstsq(G, b, rcond=None)
        recovered[i] = chi_hat
    mean = recovered.mean(axis=0)
    std = recovered.std(axis=0)
    damp = np.linalg.inv(G.T @ G)
    Rres = (damp @ K.T @ K).diagonal()
    print(f"  true coupling:      {np.array2string(chi_true, precision=2)}")
    print(f"  recovered mean:     {np.array2string(mean, precision=2)}")
    print(f"  recovered std:      {np.array2string(std, precision=2)}")
    print(f"  resolution diag:    {np.array2string(Rres, precision=2)}")
    print(f"  {n_real} realizations, {NOISE_MM_YR:.1f} mm/yr noise, first-difference")
    print(f"  smoothing with weight {lam:.1f} mm/yr per unit coupling")
    print("\n    patch   depth range (km)   true   mean   std   resolution")
    for j in range(N_PATCH):
        print(f"    {j + 1:5d}   {z_hi[j]:5.0f} - {z_hi[j + 1]:5.0f}      "
              f"{chi_true[j]:5.2f}  {mean[j]:5.2f}  {std[j]:5.2f}   "
              f"{Rres[j]:8.2f}")
    widths = np.diff(z_hi)
    print(f"\n  coupled depth extent: true = {np.sum(chi_true * widths):.1f} km, "
          f"recovered = {np.sum(mean * widths):.1f} km")
    print(f"  slip deficit rate integral: true = "
          f"{np.sum(chi_true * widths) * V_PLATE_MM_YR:.1f} mm/yr km,")
    print(f"  recovered = {np.sum(mean * widths) * V_PLATE_MM_YR:.1f} mm/yr km")
    print("  The integral is recovered far better than the individual patches: the")
    print("  deep patches have overlapping kernels and a resolution diagonal well")
    print("  below one, so their values are only meaningful in combination.")

    section("5. From coupling to moment deficit and recurrence")
    print("  Slip deficit rate on patch j = chi_j V.  With a coupled area of")
    print(f"  {FAULT_LENGTH_KM:.0f} km along strike and a coupled depth extent, the")
    print("  moment deficit rate is mu x V x L x sum(chi_j dz_j).")
    z_hi = patch_bounds()
    widths = np.diff(z_hi)
    coupled_depth_km = float(np.sum(chi_true * widths))
    area_m2 = FAULT_LENGTH_KM * 1e3 * coupled_depth_km * 1e3
    mdot = SHEAR_MODULUS_PA * (V_PLATE_MM_YR * 1e-3) * FAULT_LENGTH_KM * 1e3 \
        * coupled_depth_km * 1e3
    print(f"  coupled depth extent = {coupled_depth_km:.1f} km")
    print(f"  coupled area = {FAULT_LENGTH_KM:.0f} km x {coupled_depth_km:.0f} km "
          f"= {area_m2 / 1e6:.1f} km^2 = {area_m2:.3e} m^2")
    print(f"  moment deficit rate = mu V A = {SHEAR_MODULUS_PA:.1e} x "
          f"{V_PLATE_MM_YR * 1e-3:.3f} m/yr x {area_m2:.3e} m^2")
    print(f"                      = {mdot:.3e} N m/yr")
    print(f"  over 100 yr the accumulated moment is {mdot * 100:.3e} N m")
    mw = (2.0 / 3.0) * (np.log10(mdot * 100.0) - 9.1)
    print("  Mw from the standard relation Mw = (2/3)(log10 M0 - 9.1) with")
    print(f"  M0 = {mdot * 100:.3e} N m gives Mw = {mw:.2f}")
    print("  This is the arithmetic that connects a coupling model to a hazard")
    print("  statement, and it inherits every uncertainty in the model.  A coupling")
    print("  error of 0.1 over the same area changes the moment rate by 10% and the")
    print(f"  magnitude by {np.log10(1.1) * 2.0 / 3.0:.3f} units.  That is the honest")
    print("  size of the penalty: coupling errors matter, but they matter far less")
    print("  than not knowing the coupled area at all, which changes the moment")
    print(f"  rate in proportion to that area.")
    print("  The modelled fault is a vertical 2-D analogue: a real megathrust dips,")
    print("  so coupling is defined on a dipping interface and the surface")
    print("  projection of the coupled area is not the area itself.")


if __name__ == "__main__":
    main()
