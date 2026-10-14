"""Event catalogs: QuakeML, magnitudes, and geodesy between events and stations.

Everything is built in memory and written to a scratch file that is deleted on
exit. No catalog is downloaded.

Run:
    .venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/catalog_and_events_demo.py
"""

from __future__ import annotations

import shutil
from pathlib import Path

import numpy as np
from obspy import Catalog, UTCDateTime, read_events
from obspy.core.event import (Arrival, CreationInfo, Event, Magnitude, Origin,
                              Pick, QuantityError, ResourceIdentifier,
                              WaveformStreamID)
from obspy.geodetics import (degrees2kilometers, gps2dist_azimuth,
                             kilometer2degrees, locations2degrees)

SCRATCH = Path(__file__).resolve().parent / "_scratch_catalog"


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def build_catalog() -> Catalog:
    ev = Event(resource_id=ResourceIdentifier("smi:local/2024-03-15-0830"))
    origin = Origin(
        resource_id=ResourceIdentifier("smi:local/origin-1"),
        time=UTCDateTime("2024-03-15T08:30:12.345Z"),
        latitude=48.1043, longitude=11.2058,
        depth=11500.0,                       # metres, not kilometres
        depth_type="from location",
        latitude_errors=QuantityError(uncertainty=1.1, confidence_level=90.0),
        longitude_errors=QuantityError(uncertainty=1.4, confidence_level=90.0),
        depth_errors=QuantityError(uncertainty=2.0, confidence_level=90.0),
        time_errors=QuantityError(uncertainty=0.05),
        method_id=ResourceIdentifier("smi:local/nlloc"))
    ev.origins.append(origin)
    ev.preferred_origin_id = origin.resource_id

    ev.magnitudes.append(Magnitude(
        mag=3.84, magnitude_type="ML",
        creation_info=CreationInfo(author="demo", agency_id="XX")))
    ev.preferred_magnitude_id = ev.magnitudes[0].resource_id

    for index, (station, phase, residual) in enumerate(
            (("ABCD", "P", 0.12), ("EFGH", "P", -0.07), ("IJKL", "S", 0.31))):
        pick = Pick(
            resource_id=ResourceIdentifier(f"smi:local/pick-{index}"),
            time=UTCDateTime("2024-03-15T08:30:15.000Z") + index * 3.0,
            phase_hint=phase, onset="impulsive",
            waveform_id=WaveformStreamID(network_code="XX",
                                         station_code=station,
                                         channel_code="BHZ"))
        ev.picks.append(pick)
        origin.arrivals.append(Arrival(pick_id=pick.resource_id, phase=phase,
                                       time_residual=residual,
                                       azimuth=45.0 + 10.0 * index,
                                       distance=0.8 + 0.4 * index))
    return Catalog(events=[ev])


def main() -> None:
    SCRATCH.mkdir(exist_ok=True)
    try:
        run()
    finally:
        shutil.rmtree(SCRATCH, ignore_errors=True)
        print(f"\nscratch directory removed: {SCRATCH.name}")


def run() -> None:
    cat = build_catalog()

    section("1. A Catalog is Events -> Origins -> Arrivals -> Picks")
    print(str(cat).rstrip())
    ev = cat[0]
    origin = ev.preferred_origin()
    print(f"events                        : {len(cat)}")
    print(f"origins in event              : {len(ev.origins)}")
    print(f"picks in event                : {len(ev.picks)}")
    print(f"arrivals in preferred origin  : {len(origin.arrivals)}")
    print(f"preferred origin time         : {origin.time}")
    print(f"origin latitude/longitude     : {origin.latitude}, "
          f"{origin.longitude} deg")
    print(f"origin depth                  : {origin.depth:.1f} m")
    print("UNIT TRAP: QuakeML stores depth in METRES. 11500.0 is 11.5 km,")
    print("not 11500 km, and a factor-1000 error looks plausible on a map.")

    section("2. Uncertainties are first-class, in the units of the field")
    print(f"time error                    : "
          f"{origin.time_errors.uncertainty:.4f} s")
    print(f"latitude error (90% conf.)    : "
          f"{origin.latitude_errors.uncertainty:.4f} deg")
    print(f"depth error                   : "
          f"{origin.depth_errors.uncertainty:.1f} m")
    print(f"1 deg of latitude             : "
          f"{degrees2kilometers(1.0):.3f} km")
    print(f"so 1.1 deg is                 : "
          f"{origin.latitude_errors.uncertainty * degrees2kilometers(1.0):.1f} km")
    print(f"depth error as a fraction     : "
          f"{origin.depth_errors.uncertainty / origin.depth * 100:.4f} % "
          f"of the hypocentral depth")

    section("3. Round trip through QuakeML")
    path = SCRATCH / "event.xml"
    cat.write(str(path), format="QUAKEML")
    print(f"file size                     : {path.stat().st_size} bytes")
    back = read_events(str(path))
    o2 = back[0].preferred_origin()
    print(f"origin time identical         : {o2.time == origin.time}")
    print(f"latitude identical            : {o2.latitude == origin.latitude}")
    print(f"depth identical               : {o2.depth == origin.depth}")
    print(f"magnitude identical           : "
          f"{back[0].preferred_magnitude().mag == ev.preferred_magnitude().mag}")
    print(f"pick phase hints              : "
          f"{[p.phase_hint for p in back[0].picks]}")
    print(f"arrival residuals             : "
          f"{[a.time_residual for a in o2.arrivals]}")
    print(f"first pick minus origin time  : "
          f"{back[0].picks[0].time - o2.time:.3f} s")

    section("4. Geodesy: three different definitions of 'distance'")
    ev_lat, ev_lon = origin.latitude, origin.longitude
    st_lat, st_lon = 48.95, 11.60           # some 95 km north of the event
    deg = locations2degrees(ev_lat, ev_lon, st_lat, st_lon)
    metres, az, baz = gps2dist_azimuth(ev_lat, ev_lon, st_lat, st_lon)
    print(f"angular distance              : {deg:.6f} deg")
    print(f"great-circle distance (WGS84) : {metres / 1000.0:.4f} km")
    print(f"azimuth event->station        : {az:.4f} deg   "
          f"(station is {az:.1f} deg from the event)")
    print(f"backazimuth station->event    : {baz:.4f} deg")
    print(f"spherical mean-radius convert : "
          f"{degrees2kilometers(deg):.4f} km")
    print(f"difference WGS84 vs sphere    : "
          f"{metres / 1000.0 - degrees2kilometers(deg):.4f} km "
          f"({(metres / 1000.0) / degrees2kilometers(deg) - 1:+.4f} relative)")
    print(f"kilometer2degrees(100 km)     : {kilometer2degrees(100.0):.6f} deg")
    print(f"111.195 km in degrees         : "
          f"{kilometer2degrees(111.195):.6f} deg (the 1-deg rule of thumb)")
    print("TauP and every travel-time table use a SPHERICAL Earth or the model's")
    print("own radius; gps2dist_azimuth uses the WGS84 ellipsoid. A 0.3% radius")
    print("difference is 5 s of P travel time at 100 km, so state which you use.")

    section("5. Magnitudes: formulas, and why they do not average")
    m0 = 1.0e18                      # seismic moment in N m
    mw = (np.log10(m0) - 9.1) / 1.5
    ml = ev.preferred_magnitude().mag
    print(f"seismic moment M0             : {m0:.3e} N m")
    print(f"Mw = (log10 M0 - 9.1)/1.5     : {mw:.4f}")
    print(f"reported ML                   : {ml:.4f}")
    print(f"difference Mw - ML            : {mw - ml:+.4f} magnitude units")
    print(f"one magnitude unit            : {10 ** 1.5:.4f} x the seismic moment")
    print(f"one magnitude unit            : {10 ** (1.5 * 1.5):.4f} x the radiated energy")
    print(f"energy ratio Mw vs ML         : {10 ** (1.5 * (mw - ml)):.3f}")
    print("ML saturates near 6-7 because it is measured at short periods; Mw")
    print("does not. Averaging ML and mb, or comparing ML across networks with")
    print("different instruments, compares different physical quantities.")

    section("6. Gutenberg-Richter and the smallest magnitude a network sees")
    b_value, a_value = 1.0, 4.0
    print(f"{'M':>5} {'N(>=M) (a=4, b=1)':>20} {'spacing to next 10x':>21}")
    for m in (1.0, 2.0, 3.0, 4.0, 5.0):
        print(f"{m:5.1f} {10 ** (a_value - b_value * m):20.1f} "
              f"{1 / 10 ** (a_value - b_value * m):21.3f}")
    print("log10 N = a - b M. With b = 1 each unit of magnitude is a factor 10")
    print("fewer events, so a completeness magnitude 0.5 too high halves the")
    print("catalog you would use for any statistics.")

    section("7. Consistency checks that catch broken catalogs")
    print(f"CHECK depth is positive       : {origin.depth > 0}")
    print(f"CHECK depth in plausible range: "
          f"{0.0 < origin.depth < 700.0e3}")
    print(f"CHECK latitudes in range      : {all(-90 <= o.latitude <= 90 for e in cat for o in e.origins)}")
    print(f"CHECK arrivals <= picks       : "
          f"{len(origin.arrivals) <= len(ev.picks)}")
    residuals = [a.time_residual for a in origin.arrivals]
    print(f"arrival residual RMS          : "
          f"{np.sqrt(np.mean(np.square(residuals))):.4f} s")
    print(f"CHECK residuals < 1 s         : "
          f"{all(abs(r) < 1.0 for r in residuals)}")


if __name__ == "__main__":
    main()
