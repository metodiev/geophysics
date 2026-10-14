"""Travel times with TauP: phases, depth, ray parameter, and the shadow zone.

Uses ObsPy's bundled velocity models, so no network access is required.

Run:
    .venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/taup_travel_times_demo.py
"""

from __future__ import annotations

import numpy as np
from obspy.taup import TauPyModel

MODEL = "iasp91"


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main() -> None:
    model = TauPyModel(model=MODEL)

    section("1. The model is a table of (radius, vp, vs, density) -- bundled")
    print(f"model name                    : {MODEL}")
    print(f"model radius                  : {model.model.radius_of_planet:.1f} km")
    print(f"moho depth                    : {model.model.moho_depth:.1f} km")
    print(f"core-mantle boundary depth    : {model.model.cmb_depth:.1f} km")
    print(f"inner-core boundary depth     : {model.model.iocb_depth:.1f} km")
    vmod = model.model.s_mod.v_mod
    print(f"number of constant-velocity layers: {len(vmod.layers)}")
    for depth in (10.0, 30.0, 100.0, 700.0, 2890.0, 4000.0, 5200.0, 6000.0):
        vp = float(np.asarray(vmod.evaluate_above(depth, "p")).ravel()[0])
        vs = float(np.asarray(vmod.evaluate_above(depth, "s")).ravel()[0])
        rho = float(np.asarray(vmod.evaluate_above(depth, "d")).ravel()[0])
        print(f"  depth {depth:8.1f} km : vp = {vp:7.3f} km/s, "
              f"vs = {vs:7.3f} km/s, rho = {rho:6.3f} g/cm^3")
    print("The S branch vanishes at 2890 km: the outer core is liquid and")
    print("cannot carry shear waves, which is why SKS exists and S does not.")

    section("2. P and S travel times at fixed source depth, varying distance")
    depth = 10.0
    print(f"source depth                  : {depth:.1f} km")
    print(f"{'distance (deg)':>15} {'P (s)':>10} {'S (s)':>10} "
          f"{'PcP (s)':>10} {'S-P (s)':>10} {'P speed (km/s)':>15}")
    for distance in (10.0, 20.0, 30.0, 45.0, 60.0, 80.0, 95.0):
        arrivals = model.get_travel_times(
            source_depth_in_km=depth, distance_in_degree=distance,
            phase_list=["P", "S", "PcP"])
        first = {}
        for arr in arrivals:
            first.setdefault(arr.name, arr)
        p = first.get("P")
        s = first.get("S")
        pc = first.get("PcP")
        if p is None or s is None:
            continue
        surface_km = distance * 111.195
        print(f"{distance:15.1f} {p.time:10.4f} {s.time:10.4f} "
              f"{(pc.time if pc else float('nan')):10.4f} "
              f"{s.time - p.time:10.4f} {surface_km / p.time:15.4f}")

    section("3. Depth matters, but far less than distance")
    print(f"{'depth (km)':>11} {'P at 60 deg (s)':>16} {'dT/dz (s/km)':>14} "
          f"{'takeoff (deg)':>14} {'incidence (deg)':>16}")
    previous = None
    for d in (0.0, 10.0, 50.0, 100.0, 300.0, 600.0):
        arr = model.get_travel_times(source_depth_in_km=d, distance_in_degree=60.0,
                                     phase_list=["P"])[0]
        slope = "" if previous is None else f"{(arr.time - previous[1]) / (d - previous[0]):14.5f}"
        print(f"{d:11.1f} {arr.time:16.4f} {slope if slope else '          --':>14} "
              f"{arr.takeoff_angle:14.4f} {arr.incident_angle:16.4f}")
        previous = (d, arr.time)
    print("The first line of the difference column is a finite difference of")
    print("T(depth) at 60 deg; it is small compared with dT/d(distance), which")
    print("is the ray parameter in s/deg.")

    section("4. The ray parameter IS dT/dDelta -- verified numerically")
    print(f"{'distance (deg)':>15} {'T (s)':>10} {'p from TauP (s/deg)':>21} "
          f"{'dT/dDelta measured':>20} {'difference':>12}")
    for distance in (30.0, 45.0, 60.0, 75.0):
        step = 0.01
        arr = model.get_travel_times(source_depth_in_km=depth,
                                     distance_in_degree=distance,
                                     phase_list=["P"])[0]
        t_plus = model.get_travel_times(source_depth_in_km=depth,
                                        distance_in_degree=distance + step,
                                        phase_list=["P"])[0].time
        t_minus = model.get_travel_times(source_depth_in_km=depth,
                                         distance_in_degree=distance - step,
                                         phase_list=["P"])[0].time
        numeric = (t_plus - t_minus) / (2 * step)
        print(f"{distance:15.1f} {arr.time:10.4f} "
              f"{arr.ray_param_sec_degree:21.6f} {numeric:20.6f} "
              f"{numeric - arr.ray_param_sec_degree:12.2e}")
    print("This is the slowness identity p = dT/dDelta. It is the single most")
    print("useful check on a travel-time table, and it is the definition the")
    print("ray parameter is derived from.")

    section("5. Phase names are ray paths, not labels")
    print(f"source depth {depth:.1f} km")
    for distance, phases in ((20.0, ["P", "S", "PcP"]),
                             (103.0, ["P", "PKIKP", "PKP", "SKS", "Pdiff"]),
                             (140.0, ["P", "PKIKP", "PKP", "SKS", "Pdiff"])):
        arrivals = model.get_travel_times(source_depth_in_km=depth,
                                          distance_in_degree=distance,
                                          phase_list=phases)
        listed = ", ".join(f"{a.name} {a.time:.3f} s" for a in arrivals)
        print(f"  at {distance:6.1f} deg : {listed if listed else 'no arrival'}")
    print("At 20 deg there are six separate P branches (the upper-mantle")
    print("triplication): the same phase name, different ray paths, different")
    print("arrival times. Reporting 'the P arrival' without an index is ambiguous.")
    print()
    print("P  = compressional wave in the mantle")
    print("S  = shear wave in the mantle")
    print("c  = reflected off the core-mantle boundary (PcP)")
    print("K  = compressional wave through the outer core")
    print("I  = compressional wave through the inner core (PKIKP)")
    print("diff = diffracted along the core-mantle boundary (Pdiff)")

    section("6. The P-wave shadow zone, measured")
    print(f"{'distance (deg)':>15} {'#P arrivals':>13} {'#first-arrival P':>18} "
          f"{'first reported phase':>22}")
    for distance in (95, 100, 103, 105, 110, 115, 120, 125, 130, 135, 140, 143,
                     145, 150):
        arrivals = model.get_travel_times(source_depth_in_km=depth,
                                          distance_in_degree=float(distance),
                                          phase_list=["P", "Pdiff", "PKIKP",
                                                      "PKP", "SKS"])
        n_p = sum(1 for a in arrivals if a.name == "P")
        direct = [a for a in arrivals if a.name == "P"]
        print(f"{distance:15d} {n_p:13d} {len(direct):18d} "
              f"{(arrivals[0].name if arrivals else 'none'):>22}")
    print("Between about 103 and 143 degrees no direct P arrival exists: the")
    print("core casts a shadow. The first arrival in the shadow is the")
    print("diffracted Pdiff or the core-phase PKIKP, and the amplitudes of")
    print("those arrivals are one to two orders of magnitude smaller.")

    section("7. Take-off and incidence angle")
    print(f"{'distance (deg)':>15} {'takeoff (deg)':>14} {'incidence (deg)':>16} "
          f"{'p (s/deg)':>11}")
    for distance in (20.0, 40.0, 60.0, 80.0, 95.0):
        arr = model.get_travel_times(source_depth_in_km=depth,
                                     distance_in_degree=distance,
                                     phase_list=["P"])[0]
        print(f"{distance:15.1f} {arr.takeoff_angle:14.4f} "
              f"{arr.incident_angle:16.4f} {arr.ray_param_sec_degree:11.4f}")
    print("The take-off angle is measured from straight down at the source; the")
    print("incidence angle is measured from vertical at the receiver. They are")
    print("different numbers because refraction at the surface and at every")
    print("interface changes the angle but not the ray parameter.")

    section("8. A distance-to-time inversion: how a location problem is posed")
    measured_s_minus_p = 900.0        # seconds, an arbitrary S-P time
    print(f"assumed S-P time at unknown distance : {measured_s_minus_p:.1f} s")
    best = None
    for distance in np.arange(20.0, 100.0, 0.05):
        arrivals = model.get_travel_times(source_depth_in_km=depth,
                                          distance_in_degree=float(distance),
                                          phase_list=["P", "S"])
        first = {}
        for arr in arrivals:
            first.setdefault(arr.name, arr)
        if "P" not in first or "S" not in first:
            continue
        diff = first["S"].time - first["P"].time
        if best is None or abs(diff - measured_s_minus_p) < best[1]:
            best = (distance, abs(diff - measured_s_minus_p), diff)
    print(f"best-fit distance                    : {best[0]:.2f} deg")
    print(f"S-P at that distance                 : {best[2]:.4f} s")
    print(f"1 deg of distance is about           : "
          f"{(model.get_travel_times(source_depth_in_km=depth, distance_in_degree=60.5, phase_list=['S'])[0].time - model.get_travel_times(source_depth_in_km=depth, distance_in_degree=59.5, phase_list=['S'])[0].time):.3f} s of S at 60 deg")
    print("A single station with P and S gives a distance, not a location: the")
    print("solution is a circle of radius d around the station.")

    section("9. Two models, one distance")
    for name in ("iasp91", "prem", "ak135"):
        try:
            m = TauPyModel(model=name)
            arr = m.get_travel_times(source_depth_in_km=depth,
                                     distance_in_degree=60.0, phase_list=["P"])[0]
            print(f"  {name:<8} P at 60 deg : {arr.time:9.4f} s "
                  f"  p = {arr.ray_param_sec_degree:.4f} s/deg")
        except Exception as exc:                       # pragma: no cover
            print(f"  {name:<8} not available: {type(exc).__name__}")
    print("Differences between published models are 1-3 s at teleseismic")
    print("distances. They matter for tomography and they do not matter for a")
    print("first-look association of a phase.")


if __name__ == "__main__":
    main()
