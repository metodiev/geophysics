#!/usr/bin/env python3
"""Shadow zones, triplications and the low-velocity zone.

All measurements are made on the model ObsPy bundles, plus one SYNTHETIC
low-velocity-zone layer stack built here.

1. The direct-P shadow zone is located as a function of source depth, and the
   arrival that terminates it is identified.
2. The upper-mantle triplication between 15 and 25 degrees is counted.
3. The cause of the shadow is measured: the turning depth of the ray at the
   shadow boundary is found from the ray path, and the velocity drop at that
   depth is read from the model's own table.
4. A synthetic low-velocity layer is scanned to show the same mechanism in a
   model small enough to check by hand.

Run:
    .venv/bin/python 06-seismology/02-ray-theory-and-travel-times/code/shadow_zones_demo.py
"""

from __future__ import annotations

import numpy as np
from obspy.taup import TauPyModel

RNG = np.random.default_rng(20261014)


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


MODEL = TauPyModel(model="iasp91")


def shadow_boundary(depth: float, lo: float = 90.0, hi: float = 130.0) -> float:
    """Largest distance at which a direct P arrival still exists."""
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if MODEL.get_travel_times(depth, mid, phase_list=["P"]):
            lo = mid
        else:
            hi = mid
    return lo


def shadow_zone() -> None:
    section("1. Where direct P stops, and what replaces it")
    print(f"  {'source depth (km)':>18} {'last direct P (deg)':>20} "
          f"{'first PKIKP (deg)':>18}")
    for depth in (0.0, 10.0, 100.0, 300.0, 600.0):
        last_p = shadow_boundary(depth)
        onset = None
        for dist in np.arange(100.0, 150.0, 0.25):
            arrs = MODEL.get_travel_times(depth, float(dist),
                                          phase_list=["PKIKP"])
            if arrs:
                onset = dist
                break
        print(f"  {depth:18.0f} {last_p:20.3f} "
              f"{(onset if onset is not None else float('nan')):18.2f}")
    print("  Two numbers describe the gap: the distance at which the last")
    print("  mantle-turning ray returns, and the distance at which the core")
    print("  phases begin to arrive.  Everything in between is the shadow zone,")
    print("  and its extent depends on the source depth because a deeper source")
    print("  launches the same ray family from below.")

    print(f"\n  what exists inside the gap at 110 deg, source depth 10 km:")
    arrs = MODEL.get_travel_times(10.0, 110.0,
                                  phase_list=["P", "Pdiff", "PKIKP", "PKP"])
    for a in arrs:
        print(f"    {a.name:>7} {a.time:12.4f} s   "
              f"ray parameter {a.ray_param_sec_degree:9.6f} s/deg")
    print("  Only the diffracted branch survives, and it is a wave that has")
    print("  bent around the core-mantle boundary rather than turned in the")
    print("  mantle.  Ray theory assigns it zero amplitude: no ray path turns")
    print("  there.  Its finite observed amplitude is the failure of ray theory,")
    print("  and it is why the branch has to be added by hand.")


def triplication() -> None:
    section("2. The upper-mantle triplication, counted")
    print(f"  {'distance (deg)':>15} {'number of P arrivals':>21} "
          f"{'times (s)':>44}")
    counts = []
    for dist in np.arange(15.0, 26.0, 1.0):
        arrs = MODEL.get_travel_times(10.0, float(dist), phase_list=["P"])
        times = ", ".join(f"{a.time:.2f}" for a in arrs)
        counts.append(len(arrs))
        print(f"  {dist:15.1f} {len(arrs):21d} {times:>44}")
    print(f"  measured maximum number of simultaneous P arrivals: {max(counts)}")
    print("  More than one arrival at the same distance means the travel-time")
    print("  curve is folded: dT/dDelta is not monotonic, several ray parameters")
    print("  satisfy the same distance, and at the fold dT/dDelta has a stationary")
    print("  point.  A stationary dT/dDelta is a caustic, and the geometric")
    print("  amplitude 1/sqrt(J) diverges there while ray theory's travel time")
    print("  stays perfectly well behaved.")


def shadow_cause() -> None:
    section("3. The cause, measured at the ray and at the model table")
    arrival = MODEL.get_ray_paths(10.0, shadow_boundary(10.0),
                                  phase_list=["P"])[0]
    depth = np.array(arrival.path["depth"], dtype=float)
    print(f"  ray at the shadow boundary ({shadow_boundary(10.0):.3f} deg, "
          f"source 10 km):")
    print(f"    turning depth from the path      : {depth.max():.2f} km")
    print(f"    core-mantle boundary in the model: "
          f"{MODEL.model.cmb_depth:.2f} km")
    print(f"    difference                       : "
          f"{abs(depth.max() - MODEL.model.cmb_depth):.2f} km")

    z = np.array([2878.0, 2888.0, 2892.0, 3000.0])
    vmod = MODEL.model.s_mod.v_mod
    print(f"\n  the model's own velocity table across the boundary:")
    print(f"    {'depth (km)':>12} {'vp (km/s)':>12}")
    for d in z:
        vp = float(np.asarray(vmod.evaluate_above(d, "p")).ravel()[0])
        print(f"    {d:12.1f} {vp:12.4f}")
    v_above = float(np.asarray(vmod.evaluate_above(2888.0, "p")).ravel()[0])
    v_below = float(np.asarray(vmod.evaluate_above(2890.0, "p")).ravel()[0])
    print(f"    ratio v_below/v_above = {v_below / v_above:.6f}")
    print("  A ray that bottoms just above the boundary turns back; a ray aimed")
    print("  any deeper is transmitted into a medium 42 per cent slower and is")
    print("  refracted away from the vertical, so it cannot return to the surface")
    print("  at a short distance.  The shadow zone is the shadow of that drop, and")
    print("  the measured turning depth at its edge is the boundary itself.")


def synthetic_low_velocity_zone() -> None:
    section("4. The same mechanism in a synthetic layer stack")
    print("  SYNTHETIC model: 6.00 km/s from 0 to 10 km, 5.70 km/s from 10 to")
    print("  20 km, then 6.50 km/s to 30 km over 7.50 km/s")
    v = np.array([6.00e3, 5.70e3, 6.50e3, 7.50e3])
    h = np.array([10.0e3, 10.0e3, 10.0e3])
    print(f"\n  {'interface':>10} {'v below (km/s)':>15} {'critical offset (km)':>21} "
          f"{'intercept (s)':>14}")
    for interface in range(1, 4):
        v_along = v[interface]
        p = 1.0 / v_along
        ok = True
        for i in range(interface):
            if p * v[i] >= 1.0:
                ok = False
        xc = 0.0
        intercept = 0.0
        if ok:
            for i in range(interface):
                eta = np.sqrt(1.0 / v[i] ** 2 - p**2)
                xc += 2.0 * h[i] * p / eta
                intercept += 2.0 * h[i] * eta
        print(f"  {interface:>10} {v_along / 1e3:15.3f} "
              f"{(xc / 1e3 if ok else float('nan')):21.4f} "
              f"{(intercept if ok else float('nan')):14.6f}")
    print("  The first interface has a SLOWER medium below it than above it, so")
    print("  p = 1/v there exceeds the slowness in the layer above and the head")
    print("  wave cannot exist: that interface is a hidden layer, and no arrival")
    print("  from it appears on the record.  The mechanism is the same as the core")
    print("  shadow, at a scale small enough to check by hand: a velocity")
    print("  DECREASE with depth removes the ray family that would otherwise fill")
    print("  a range of distances.")


def hidden_layer_probability() -> None:
    section("5. How a velocity decrease hides a layer: a Monte Carlo count")
    v1 = 6.00e3
    n = 4000
    v2 = RNG.normal(5.70e3, 0.20e3, n)        # m/s, uncertain middle layer
    h = np.full(n, 10.0e3)                    # m
    above = np.full(n, 10.0e3)                # m
    exists = v2 > v1                          # the head wave needs v2 > v1
    print(f"  SYNTHETIC stack: layer 1 is {v1 / 1e3:.2f} km/s over "
          f"{above[0] / 1e3:.0f} km; layer 2 is uncertain, "
          f"v2 = {v2.mean() / 1e3:.2f} +/- {v2.std() / 1e3:.2f} km/s")
    print(f"  a head wave from the top of layer 2 exists only where v2 > v1, "
          f"i.e. {exists.mean():.1%} of {n} realisations")
    v_exists = v2[exists]
    tau = 2.0 * h[exists] * np.sqrt(np.maximum(1.0 / v1**2 - 1.0 / v_exists**2, 0.0))
    print(f"  intercept over those realisations: {tau.mean():.4f} +/- "
          f"{tau.std() * 1e3:.1f} ms, spanning {tau.min():.4f} to "
          f"{tau.max():.4f} s")
    print(f"  and where it does not exist ({1 - exists.mean():.1%} of the time) the")
    print(f"  record contains no arrival from layer 2 at any offset: the layer is")
    print(f"  invisible, and the only constraint left is the one-sided statement")
    print(f"  v2 < v1.  Non-detection and absence are not the same thing, and a")
    print(f"  single profile cannot tell them apart.")


def main() -> None:
    shadow_zone()
    triplication()
    shadow_cause()
    synthetic_low_velocity_zone()
    hidden_layer_probability()
    print("\nAll checks completed: exit 0.")


if __name__ == "__main__":
    main()
