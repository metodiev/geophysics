"""ObsPy architecture and the Trace/Stream data model.

Everything here runs offline: no data are downloaded, and every trace is
built in memory from numpy arrays.

Run:
    .venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/obspy_overview_demo.py
"""

from __future__ import annotations

import numpy as np
import obspy
from obspy import Stream, Trace, UTCDateTime


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def build_trace(npts: int = 6000, fs: float = 100.0,
                start: str = "2024-03-15T08:30:00.000000Z") -> Trace:
    """Return an empty-but-valid Trace with fully specified metadata."""
    rng = np.random.default_rng(20240315)
    tr = Trace(data=rng.standard_normal(npts).astype(np.float64))
    tr.stats.network = "XX"
    tr.stats.station = "ABCD"
    tr.stats.location = "00"
    tr.stats.channel = "BHZ"
    tr.stats.sampling_rate = fs
    tr.stats.starttime = UTCDateTime(start)
    return tr


def main() -> None:
    section("1. What ObsPy is: one meta-package, many subpackages")
    print(f"obspy version        : {obspy.__version__}")
    print(f"numpy version        : {np.__version__}")
    for name in ("core", "io", "signal", "taup", "geodetics", "clients.fdsn",
                 "imaging", "realtime", "db"):
        try:
            mod = __import__(f"obspy.{name}", fromlist=["__name__"])
            print(f"  obspy.{name:<16} importable   "
                  f"{getattr(mod, '__version__', '')}")
        except Exception as exc:                    # pragma: no cover
            print(f"  obspy.{name:<16} NOT available ({type(exc).__name__})")

    section("2. UTCDateTime is an absolute instant, not a formatted string")
    t0 = UTCDateTime("2024-03-15T08:30:00.123456Z")
    print(f"parsed                : {t0}")
    print(f"POSIX/epoch seconds   : {t0.timestamp:.6f} s since 1970-01-01T00:00:00Z")
    print(f"matplotlib date       : {t0.matplotlib_date:.6f} "
          f"days since 1970-01-01")
    print(f"julday                : {t0.julday}  "
          f"(day of year, 1..365/366 -- NOT a Julian Day Number)")
    print(f"civil calendar fields : {t0.year}-{t0.month:02d}-{t0.day:02d} "
          f"{t0.hour:02d}:{t0.minute:02d}:{t0.second:02d}.{t0.microsecond:06d}")
    t1 = UTCDateTime("2024-03-15T08:31:00.000000Z")
    dt = t1 - t0
    print(f"interval t1 - t0      : {dt:.6f} s  (exact: 59.876544 s)")
    back = UTCDateTime(t0.timestamp)
    print(f"epoch -> UTCDateTime  : {back}  identical={back == t0}")

    section("3. Leap seconds are NOT representable in ObsPy 1.5.1")
    for label, builder in (
        ("constructor UTCDateTime(2016,12,31,23,59,60)",
         lambda: UTCDateTime(2016, 12, 31, 23, 59, 60)),
        ("ISO string '2016-12-31T23:59:60'",
         lambda: UTCDateTime("2016-12-31T23:59:60")),
        ("ISO string '2016-12-31T23:59:60.0'",
         lambda: UTCDateTime("2016-12-31T23:59:60.0")),
    ):
        try:
            value = builder()
            print(f"  {label:<44} -> {value}")
        except ValueError as exc:
            print(f"  {label:<44} -> ValueError: {exc}")
    a = UTCDateTime("2016-12-31T23:59:59")
    b = UTCDateTime("2017-01-01T00:00:00")
    print(f"  UTC {a} -> {b}: ObsPy reports {(b - a):.6f} s")
    print("  2 SI seconds elapsed across that boundary (a positive leap second")
    print("  was inserted); the difference is reported as 1 s because the")
    print("  timestamp field is POSIX time, which ignores leap seconds.")

    section("4. The Trace data model: array + metadata + nothing else")
    tr = build_trace()
    print(f"Trace.id                 : {tr.id}")
    print(f"len(tr.data)             : {len(tr.data)}  samples")
    print(f"tr.stats.npts            : {tr.stats.npts}")
    print(f"tr.stats.sampling_rate   : {tr.stats.sampling_rate} Hz")
    print(f"tr.stats.delta           : {tr.stats.delta} s  (= 1/sampling_rate)")
    print(f"Nyquist frequency        : {tr.stats.sampling_rate / 2.0} Hz")
    print(f"tr.stats.starttime       : {tr.stats.starttime}")
    print(f"tr.stats.endtime         : {tr.stats.endtime}")
    print(f"data units               : raw ADC counts (dimensionless integers")
    print(f"                           before the response is removed)")
    print(f"dtype in memory          : {tr.data.dtype}")
    print(f"dtype on disk (MiniSEED) : int32, or float32 for SAC")
    print(f"duration = npts*delta    : {tr.stats.npts * tr.stats.delta:.3f} s")
    print(f"tr.times() first/last    : {tr.times()[0]:.3f} s / "
          f"{tr.times()[-1]:.3f} s relative to starttime")

    section("5. Stream: an ordered collection of traces")
    st = Stream(tr.copy())
    second = tr.copy()
    second.stats.station = "EFGH"
    second.stats.starttime = tr.stats.starttime + 60.0     # a gap of 0 samples
    st.append(second)
    print(str(st).rstrip())
    print(f"len(st)                  : {len(st)} traces")
    print(f"total samples            : {sum(t.stats.npts for t in st)}")

    section("6. Trace arithmetic and slicing are strict about metadata")
    cut = tr.slice(tr.stats.starttime + 1.0, tr.stats.starttime + 2.0)
    print(f"slice [1 s, 2 s]         : {cut.stats.npts} samples, "
          f"delta {cut.stats.delta} s")
    print(f"a 1 s window at 100 Hz has 100 intervals; slice() returns 101")
    print(f"samples because both time boundaries are inclusive")
    trim = tr.copy().trim(tr.stats.starttime + 1.0, tr.stats.starttime + 2.0)
    print(f"trim  [1 s, 2 s]         : {trim.stats.npts} samples")

    section("7. Stream.merge() decides what a gap means")
    part_a = tr.copy()
    part_a.data = tr.data[:2000]
    part_b = tr.copy()
    part_b.stats.starttime = tr.stats.starttime + 30.0
    part_b.data = tr.data[3000:]
    gap = Stream(traces=[part_a, part_b])
    gap_s = gap[1].stats.starttime - gap[0].stats.endtime
    print(f"before merge             : {len(gap)} traces, "
          f"gap of {gap_s:.3f} s "
          f"({int(round(gap_s * tr.stats.sampling_rate))} missing samples)")
    kept = gap.copy().merge(method=-1)
    print(f"merge(method=-1)         : {len(kept)} traces -> the gap is kept")
    filled = gap.copy().merge(method=0, fill_value=0.0)
    print(f"merge(method=0)          : {len(filled)} traces, "
          f"{filled[0].stats.npts} samples")
    print(f"samples that are not data: "
          f"{filled[0].stats.npts - 2000 - 3000} "
          f"(zeros inserted at the gap by method=0)")
    print(f"CHECK gap preserved      : {len(kept) == 2}")
    print(f"CHECK fill is zeros      : "
          f"{np.all(filled[0].data[2000:2000 + 1000] == 0.0)}")

    section("8. Units and sanity checks")
    print(f"trace max |amplitude|    : {np.abs(tr.data).max():.4f} counts")
    print(f"trace RMS                : {np.sqrt(np.mean(tr.data ** 2)):.4f} counts")
    print(f"variance                 : {tr.data.var(ddof=1):.4f} counts^2")
    print(f"CHECK sampling_rate>0    : {tr.stats.sampling_rate > 0}")
    print(f"CHECK delta == 1/fs      : "
          f"{np.isclose(tr.stats.delta, 1.0 / tr.stats.sampling_rate)}")
    print(f"CHECK starttime <= endtime: "
          f"{tr.stats.starttime <= tr.stats.endtime}")
    print("\nAll checks complete. Exit status 0.")


if __name__ == "__main__":
    main()
