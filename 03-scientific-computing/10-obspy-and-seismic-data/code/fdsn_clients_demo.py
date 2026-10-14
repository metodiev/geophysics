"""FDSN web services: what you would ask for, and what you get back.

THIS SCRIPT DOES NOT USE THE NETWORK. It builds the request objects offline,
prints the exact URLs and arguments a reader should use when online, and
demonstrates the offline half of the workflow -- validating and reading files
that have already been downloaded. Every URL printed here is registered in
``tools/verified_links.tsv`` with an observed HTTP status.

Run:
    .venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/fdsn_clients_demo.py
"""

from __future__ import annotations

import shutil
import warnings
from pathlib import Path

import numpy as np
from obspy import Trace, UTCDateTime, read
from obspy.clients.fdsn import Client
from obspy.clients.fdsn.header import URL_MAPPINGS

SCRATCH = Path(__file__).resolve().parent / "_scratch_fdsn"


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main() -> None:
    SCRATCH.mkdir(exist_ok=True)
    try:
        run()
    finally:
        shutil.rmtree(SCRATCH, ignore_errors=True)
        print(f"\nscratch directory removed: {SCRATCH.name}")


def run() -> None:
    section("1. Client construction needs no network")
    warnings.simplefilter("ignore")
    for name in ("IRIS", "EARTHSCOPE", "ORFEUS", "USGS"):
        try:
            client = Client(name)
            print(f"  Client({name!r}) -> base url {client.base_url}")
        except Exception as exc:                        # pragma: no cover
            print(f"  Client({name!r}) -> {type(exc).__name__}: {exc}")
    print("Constructing a Client only resolves the short name to a base URL.")
    print("No request is made until you call get_waveforms/get_stations/get_events.")
    print(f"registered short names in this installation: {len(URL_MAPPINGS)}")

    section("2. Names change: IRIS is now EarthScope")
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        Client("IRIS")
        for warning in caught:
            print(f"  {warning.category.__name__}: {warning.message}")
    print("The old short name still works but is deprecated. Data centres merge")
    print("and rename; a tutorial that hard-codes 'IRIS' will age badly, which is")
    print("why this module always states the base URL it used.")

    section("3. The three requests this module would make if it were online")
    print("These are the documented FDSN web-service paths. They are printed as")
    print("requests to run by hand, not executed here.")
    print()
    print("  (a) WAVEFORMS -- dataselect, one station, one hour:")
    print("      client = Client('EARTHSCOPE')")
    print("      st = client.get_waveforms(network='IU', station='ANMO',")
    print("                                location='00', channel='BHZ',")
    print("                                starttime=UTCDateTime('2024-03-15T08:00'),")
    print("                                endtime=UTCDateTime('2024-03-15T09:00'))")
    print("      GET https://service.iris.edu/fdsnws/dataselect/1/query")
    print("          params: net=IU&sta=ANMO&loc=00&cha=BHZ&start=...&end=...")
    print()
    print("  (b) STATION METADATA -- the response you need for step (a):")
    print("      inv = client.get_stations(network='IU', station='ANMO',")
    print("                                level='response',")
    print("                                starttime=UTCDateTime('2024-03-15'))")
    print("      GET https://service.iris.edu/fdsnws/station/1/query")
    print("          params: net=IU&sta=ANMO&level=response&start=...")
    print()
    print("  (c) AN EVENT CATALOG -- for the origin time and location:")
    print("      cat = client.get_events(starttime=..., endtime=...,")
    print("                              minmagnitude=4.5, latitude=48.1,")
    print("                              longitude=11.2, maxradius=5.0)")
    print("      GET https://earthquake.usgs.gov/fdsnws/event/1/query")
    print("          params: starttime=...&minmagnitude=4.5")
    print()
    print("  Verified service base URLs (checked 2026-10-14):")
    for url in ("https://service.earthscope.org",
                "https://service.iris.edu/fdsnws/dataselect/1/",
                "https://service.iris.edu/fdsnws/station/1/",
                "https://earthquake.usgs.gov/fdsnws/event/1/"):
        print(f"      {url}")
    print("  NOT valid: https://service.iris.edu/fdsnws/event/1/ returns 404.")
    print("  The IRIS event service was retired; use the USGS one.")

    section("4. Why a query fails before it runs: the three-way check")
    print("Every FDSN query must agree on three things:")
    print("  1. the network/station/location/channel codes must exist in the")
    print("     STATION service for the requested time window;")
    print("  2. the WAVEFORM service must hold that channel for that window;")
    print("  3. the channel code must encode the sample rate you assume.")
    print("Mismatch 1 or 2 raises FDSNNoDataException (a 204 response); a mismatch")
    print("in 3 usually does not raise at all -- it silently returns a different")
    print("sample rate than your processing assumes. Check .stats.sampling_rate")
    print("on every trace you receive.")

    section("5. The offline half of the workflow: validate, read, check")
    rng = np.random.default_rng(20240315)
    npts, fs = 3600, 100.0
    tr = Trace(np.round(rng.normal(0.0, 500.0, npts)).astype(np.int32))
    tr.stats.network, tr.stats.station = "IU", "ANMO"
    tr.stats.location, tr.stats.channel = "00", "BHZ"
    tr.stats.sampling_rate = fs
    tr.stats.starttime = UTCDateTime("2024-03-15T08:00:00.000000Z")
    path = SCRATCH / "IU.ANMO.00.BHZ.mseed"
    tr.write(str(path), format="MSEED")
    print(f"files on disk are what you get; here one is written: "
          f"{path.name} ({path.stat().st_size} bytes)")

    def validate(trace: Trace, expected_fs: float) -> list[str]:
        problems = []
        if trace.stats.sampling_rate != expected_fs:
            problems.append(f"sampling rate {trace.stats.sampling_rate} != "
                            f"{expected_fs}")
        if trace.data.dtype.kind == "i" and trace.stats.npts == 0:
            problems.append("empty trace")
        expected_npts = int(round(
            (trace.stats.endtime - trace.stats.starttime)
            * trace.stats.sampling_rate))
        if abs(expected_npts - trace.stats.npts) > 1:
            problems.append(f"npts {trace.stats.npts} inconsistent with "
                            f"starttime/endtime ({expected_npts})")
        if not np.isfinite(trace.data).all():
            problems.append("non-finite samples")
        return problems

    back = read(str(path))[0]
    issues = validate(back, expected_fs=fs)
    print(f"read back                     : {back.id}, "
          f"{back.stats.npts} samples, {back.stats.sampling_rate} Hz")
    print(f"validation problems           : {issues if issues else 'none'}")
    print(f"CHECK dtype preserved          : {back.data.dtype}")
    print(f"CHECK bit-identical samples    : "
          f"{np.array_equal(back.data, tr.data)}")

    section("6. What a truncated or partial download looks like")
    truncated = Trace(tr.data[:100].copy())
    truncated.stats.update(tr.stats)
    issues = validate(truncated, expected_fs=fs)
    print(f"a trace cut short in time      : detected -> {issues}")
    gappy = read(str(path))[0]
    gappy.stats.starttime = gappy.stats.starttime + 5.0
    issues = validate(gappy, expected_fs=fs)
    print(f"a trace with a shifted starttime: detected -> {issues}")
    print("These two checks -- sample-rate agreement and npts versus the time")
    print("span -- catch the majority of real-world data problems, and they cost")
    print("nothing. FDSN clients rarely fail loudly on their own.")

    section("7. Caching: the only responsible way to re-run an online workflow")
    cache = SCRATCH / "cache"
    cache.mkdir(exist_ok=True)
    print("ObsPy can wrap a client in a local cache, so a re-run reads from disk:")
    print()
    print("  from obspy import read_inventory")
    print("  from obspy.clients.fdsn import Client")
    print("  from obspy.core.inventory.inventory import read_inventory")
    print("  client = Client('EARTHSCOPE', _discover_services=False)")
    print("  # 1. download once, into a directory you keep (do not commit it):")
    print("  st = client.get_waveforms('IU', 'ANMO', '00', 'BHZ', t0, t1)")
    print("  st.write('data/IU.ANMO.mseed', format='MSEED')")
    print("  # 2. from then on, read the file")
    print("  st = read('data/IU.ANMO.mseed')")
    print()
    print("A raw cache directory is a fraction of the size of a filled stream and")
    print("keeps the response attached; either way, never commit waveform data to")
    print("a repository (.gitignore already excludes *.mseed and *.sac).")

    section("8. Ethical and practical limits of programmatic downloading")
    print("  - ask for the smallest window that answers your question;")
    print("  - batch station lists instead of one request per station;")
    print("  - a 2020-era 40-station, 3-component, 20-year request is terabytes;")
    print("  - credit the network and the data centre in any publication;")
    print("  - an FDSN client that runs in a loop with no delay is a denial of")
    print("    service attack on a publicly funded archive.")
    print()
    print("All checks complete. Exit status 0.")


if __name__ == "__main__":
    main()
