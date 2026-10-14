"""Porosity logs: forward-model a synthetic well, then invert it forward.

The workflow is the one a petrophysicist actually runs, and its failure modes are
the point of the exercise:

  1. LAYER MODEL.  Five SYNTHETIC layers with stated mineralogy, porosity and
     fluid.
  2. FORWARD MODEL.  Density, neutron and sonic logs are generated from the layer
     properties using the volume-balance relations of module 05-04.
  3. INVERSION.  Each log is inverted for porosity *assuming a single matrix
     mineral*.  The recovery is reported layer by layer, together with the error.
  4. FAILURE.  The gas-bearing layer is reported in detail: the density log
     over-reads porosity and the neutron log under-reads it, so a wrong choice of
     fluid makes both wrong in opposite directions -- the classic gas effect.

All mineral densities, slownesses, hydrogen indices and fluid properties are
STATED SYNTHETIC INPUTS drawn from the ranges used in module 05-04.  They are not
quotations of a specific tool or a specific formation.

Run:  python3 porosity_demo.py
"""

from __future__ import annotations

import numpy as np

# SYNTHETIC matrix properties: bulk density (kg/m^3), sonic slowness (us/m),
# neutron-matrix hydrogen index (dimensionless, 1.0 = water-equivalent).
MATRIX = {
    "quartz":  {"rho": 2650.0, "dt": 182.0, "hi": -0.02},
    "calcite": {"rho": 2710.0, "dt": 156.0, "hi": 0.00},
    "dolomite": {"rho": 2870.0, "dt": 143.0, "hi": 0.02},
}
# SYNTHETIC fluids: bulk density (kg/m^3), slowness (us/m), hydrogen index.
FLUID = {
    "water": {"rho": 1000.0, "dt": 620.0, "hi": 1.00},
    "oil":   {"rho": 800.0,  "dt": 760.0, "hi": 0.95},
    "gas":   {"rho": 150.0,  "dt": 1150.0, "hi": 0.35},
}

# SYNTHETIC layers: (top, base, matrix, fluid, porosity)
LAYERS = [
    (1000.0, 1010.0, "quartz",  "water", 0.30),
    (1010.0, 1020.0, "quartz",  "water", 0.15),
    (1020.0, 1030.0, "calcite", "water", 0.10),
    (1030.0, 1040.0, "quartz",  "gas",   0.20),
    (1040.0, 1050.0, "dolomite", "oil",  0.12),
]


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def forward(layer):
    """Density, neutron-porosity and sonic slowness for one layer."""
    _, _, matrix, fluid, phi = layer
    m, f = MATRIX[matrix], FLUID[fluid]
    rho = phi * f["rho"] + (1.0 - phi) * m["rho"]
    phi_n = phi * f["hi"] + (1.0 - phi) * m["hi"]
    dt = phi * f["dt"] + (1.0 - phi) * m["dt"]           # Wyllie time-average
    return rho, phi_n, dt


def main() -> None:
    section("1. The synthetic well")
    print("layer (m)         matrix    fluid    phi   rho_b     phi_N     dt")
    for layer in LAYERS:
        rho, phi_n, dt = forward(layer)
        print(f"{layer[0]:6.0f}-{layer[1]:6.0f}   {layer[2]:8s} {layer[3]:7s} "
              f"{layer[4]:5.2f}  {rho:7.0f}  {phi_n:7.3f}  {dt:7.1f}")

    section("2. Inverting each log assuming quartz matrix and water fluid")
    mq, wf = MATRIX["quartz"], FLUID["water"]
    print("layer (m)        phi_true   phi_density   phi_neutron   phi_sonic")
    worst = {"density": (0.0, None), "neutron": (0.0, None), "sonic": (0.0, None)}
    for layer in LAYERS:
        rho, phi_n, dt = forward(layer)
        phi_d = (rho - mq["rho"]) / (wf["rho"] - mq["rho"])
        phi_n_inv = (phi_n - mq["hi"]) / (wf["hi"] - mq["hi"])
        phi_s = (dt - mq["dt"]) / (wf["dt"] - mq["dt"])
        print(f"{layer[0]:6.0f}-{layer[1]:6.0f}   {layer[4]:8.2f}   "
              f"{phi_d:11.3f}   {phi_n_inv:11.3f}   {phi_s:9.3f}")
        for name, val in (("density", phi_d), ("neutron", phi_n_inv),
                          ("sonic", phi_s)):
            err = abs(val - layer[4])
            if err > worst[name][0]:
                worst[name] = (err, f"{layer[0]:.0f}-{layer[1]:.0f} m")
    for name, (err, where) in worst.items():
        print(f"largest {name} porosity error: {err:.3f} fraction "
              f"({100 * err:.1f} porosity units) at {where}")
    print("The sonic and neutron inversions are exact in the water-bearing layers\n"
          "because the model used to invert is the model used to generate them.  The\n"
          "density inversion is exact for the same reason.  Every error below comes\n"
          "from the matrix or fluid assumption, not from the data.")

    section("3. The gas layer: why the density and neutron logs disagree")
    layer = LAYERS[3]
    rho, phi_n, dt = forward(layer)
    phi_d = (rho - mq["rho"]) / (wf["rho"] - mq["rho"])
    phi_n_inv = (phi_n - mq["hi"]) / (wf["hi"] - mq["hi"])
    print(f"true porosity = {layer[4]:.2f}, fluid = {layer[3]}")
    print(f"density-derived porosity, water assumed = {phi_d:.3f}")
    print(f"neutron-derived porosity, water assumed = {phi_n_inv:.3f}")
    print(f"apparent crossover = {phi_n_inv - phi_d:+.3f} porosity units")
    print(f"true hydrogen index of the fluid = {FLUID['gas']['hi']:.2f} "
          f"(water = {FLUID['water']['hi']:.2f})")
    print("The gas has a low hydrogen index and a low density.  Assuming water makes\n"
          "the density log over-read porosity (too little mass) and the neutron log\n"
          "under-read it (too little hydrogen).  The *difference* between the two\n"
          "logs is therefore the diagnostic: a negative neutron-density crossover\n"
          "means light hydrocarbon, and it is the reason both logs are always run.")

    section("4. What a wrong matrix costs")
    layer = LAYERS[4]      # dolomite with oil
    rho, phi_n, dt = forward(layer)
    print(f"true layer: {layer[2]} with {layer[3]}, phi = {layer[4]:.2f}")
    for assumed in ("quartz", "calcite", "dolomite"):
        ma = MATRIX[assumed]
        phi_d = (rho - ma["rho"]) / (wf["rho"] - ma["rho"])
        print(f"  density porosity assuming {assumed:9s} (rho_ma = "
              f"{ma['rho']:6.0f}): {phi_d:7.3f}  "
              f"({100 * (phi_d - layer[4]) / layer[4]:+7.1f} per cent)")
    print("A wrong matrix moves the density porosity by several porosity units, and\n"
          "the error is largest where the matrix densities differ most.  This is why\n"
          "mineralogy is identified from a crossplot or an independent measurement\n"
          "before porosity is computed, rather than assumed.")
    sonic_to_time()


def sonic_to_time():
    """Why a slowness log integrates to a time, verified numerically."""
    section("5. A slowness log integrates to a time")
    step = 0.02
    depths = np.arange(1000.0, 1050.0, step)
    dt_log = np.zeros_like(depths)
    for i, z in enumerate(depths):
        for top, base, matrix, fluid, phi in LAYERS:
            if top <= z < base:
                dt_log[i] = forward((top, base, matrix, fluid, phi))[2]
    one_way = float(np.sum(dt_log * step)) * 1e-6      # us/m * m -> s
    print(f"depth interval              = {depths[0]:.0f} to {depths[-1]:.0f} m")
    print(f"sample interval             = {step * 100:.0f} cm, "
          f"{depths.size} samples")
    print(f"one-way time from the log   = {one_way:.6f} s")
    print(f"two-way time from the log   = {2 * one_way:.6f} s")
    print("The identity is exact: travel time is the integral of slowness, so a")
    print("sonic log IS a time-depth curve sampled along the hole.  That is why it")
    print("ties a seismic section to a well, and why an interval of missing or")
    print("washed-out log over even a metre corrupts the tie.")
    missing = 1.0
    dt_shale = forward(LAYERS[0])[2]
    dt_res = forward(LAYERS[1])[2]
    err = (dt_res - dt_shale) * 1e-6 * missing
    print(f"")
    print(f"effect of substituting 1 m of {LAYERS[0][2]} at {LAYERS[0][4]:.2f} "
          f"porosity ({dt_shale:.0f} us/m)")
    print(f"for 1 m of {LAYERS[1][2]} at {LAYERS[1][4]:.2f} porosity "
          f"({dt_res:.0f} us/m): {1000 * err:+.3f} ms two-way")
    print("A few milliseconds of tie error is tens of metres of depth error at")
    print("typical velocities, which is the same statement as the velocity-to-depth")
    print("table in lesson 05-08-06.")


if __name__ == "__main__":
    main()
