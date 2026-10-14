#!/usr/bin/env python3
"""Soil moisture remote sensing and its validation: a synthetic brightness-
temperature model, retrieval sensitivity, the vegetation bias, and how footprint
mismatch degrades validation statistics.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python soil_moisture_rs_demo.py

Everything here is SYNTHETIC.  The dielectric model, the temperatures, the
vegetation opacity and the validation scatter are chosen teaching values, not
measurements or a real field campaign.  No file is read or written and no
network access is used.

Contents
--------
1. Soil moisture -> dielectric constant -> emissivity -> brightness temperature.
2. Retrieval sensitivity and a retrieval by inversion.
3. Vegetation: what an unmodelled canopy does to the answer.
4. Validation against in-situ points, and the cost of a footprint mismatch.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

T_SOIL = 300.0        # K
T_VEG = 295.0         # K
TAU_TRUE = 0.15       # vegetation opacity (SYNTHETIC)
NE_DT = 0.40          # radiometer noise, K


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def soil_eps(mv):
    """Synthetic soil dielectric constant from volumetric moisture (m3/m3)."""
    return 3.0 + 30.0 * mv + 20.0 * mv ** 2


def emissivity(mv):
    """Smooth-surface nadir emissivity from the Fresnel reflectivity."""
    eps = soil_eps(mv)
    r = ((np.sqrt(eps) - 1.0) / (np.sqrt(eps) + 1.0)) ** 2
    return 1.0 - r


def brightness_T(mv, tau=0.0):
    """Brightness temperature (K): soil emission attenuated by a canopy."""
    e = emissivity(mv)
    if tau <= 0.0:
        return e * T_SOIL
    return e * T_SOIL * np.exp(-tau) + (1.0 - np.exp(-tau)) * T_VEG


MV = np.linspace(0.0, 0.50, 1001)


def retrieve(TB, tau=0.0):
    """Invert brightness temperature for soil moisture by table lookup."""
    grid = np.array([brightness_T(m, tau) for m in MV])
    order = np.argsort(grid)
    return np.interp(TB, grid[order], MV[order])


def main():
    section("1. From moisture to brightness temperature (SYNTHETIC)")
    print("  mv (m3/m3)   eps        emissivity   TB (K)")
    for mv in (0.05, 0.10, 0.20, 0.30, 0.40):
        print(f"  {mv:10.2f}   {soil_eps(mv):8.2f}   {emissivity(mv):10.4f}   "
              f"{brightness_T(mv):6.2f}")
    print(f"soil temperature = {T_SOIL:.0f} K")
    print("Wetter soil has a higher dielectric constant, so it reflects more of")
    print("the sky and emits less: brightness temperature FALLS as moisture rises.")

    section("2. Sensitivity and a retrieval (SYNTHETIC)")
    m0 = 0.20
    d = 0.005
    sens = (brightness_T(m0 + d) - brightness_T(m0 - d)) / (2 * d)
    print(f"dTB/dmv at mv = {m0:.2f} = {sens:.2f} K per (m3/m3)")
    print(f"a noise of {NE_DT:.2f} K in TB is therefore "
          f"{NE_DT / abs(sens):.4f} m3/m3 of moisture")
    tb_obs = brightness_T(0.28)
    print(f"observe TB = {tb_obs:.3f} K -> retrieved mv = "
          f"{retrieve(tb_obs):.4f} (truth 0.2800)")

    section("3. Vegetation: the dominant retrieval bias (SYNTHETIC)")
    print(f"canopy opacity assumed 0.00, true opacity {TAU_TRUE:.2f}")
    print("  true mv   TB observed (K)   retrieved mv   bias")
    for mv in (0.10, 0.20, 0.30):
        tb = brightness_T(mv, tau=TAU_TRUE)
        mh = retrieve(tb, tau=0.0)
        print(f"  {mv:7.2f}   {tb:15.3f}   {mh:12.4f}   {mh - mv:+.4f}")
    print("Ignoring the canopy makes the soil look wetter than it is, because")
    print("vegetation adds warm emission the model attributes to soil moisture.")

    section("4. Validation against in-situ points (SYNTHETIC)")
    n = 300
    m_true = np.clip(RNG.normal(0.20, 0.06, n), 0.02, 0.45)   # area-mean truth
    retrieval = retrieve(brightness_T(m_true) + RNG.normal(0.0, NE_DT, n))
    print(f"{n} matchups; retrieval noise {NE_DT:.2f} K "
          f"(~{NE_DT / abs(sens):.4f} m3/m3)")
    print("  heterogeneity (sd)   r      bias      RMSD     slope")
    for het in (0.0, 0.02, 0.04):
        in_situ = m_true + RNG.normal(0.0, het, n)   # point vs footprint value
        r = float(np.corrcoef(retrieval, in_situ)[0, 1])
        bias = float(np.mean(retrieval - in_situ))
        rmsd = float(np.sqrt(np.mean((retrieval - in_situ) ** 2)))
        slope = float(np.polyfit(in_situ, retrieval, 1)[0])
        print(f"  {het:18.2f}   {r:.3f}   {bias:+.4f}   {rmsd:.4f}   {slope:.3f}")
    print("With a perfectly homogeneous footprint the model validates almost")
    print("exactly. Real sub-footprint variability raises the RMSD and pulls the")
    print("regression slope below one: the product is right about the area and")
    print("wrong about the point, and a point is what the ground station measures.")


if __name__ == "__main__":
    main()
