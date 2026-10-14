"""Reading and writing MiniSEED and SAC: the on-disk sample formats.

All data are synthesised in memory; nothing is downloaded. Scratch files are
written inside ``code/_scratch_roundtrip/`` and deleted before exit, so the
repository stays clean.

Run:
    .venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/reading_waveforms_demo.py
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

import numpy as np
from obspy import Stream, Trace, UTCDateTime, read

SCRATCH = Path(__file__).resolve().parent / "_scratch_roundtrip"


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def make_trace(dtype=np.int32, npts: int = 3000, fs: float = 100.0,
               station: str = "ABCD", start: str = "2024-03-15T08:30:00.000000Z"
               ) -> Trace:
    rng = np.random.default_rng(4242)
    raw = rng.normal(0.0, 1000.0, npts)
    tr = Trace(raw.astype(dtype))
    tr.stats.network = "XX"
    tr.stats.station = station
    tr.stats.location = "00"
    tr.stats.channel = "BHZ"
    tr.stats.sampling_rate = fs
    tr.stats.starttime = UTCDateTime(start)
    return tr


def main() -> None:
    SCRATCH.mkdir(exist_ok=True)
    try:
        run()
    finally:
        shutil.rmtree(SCRATCH, ignore_errors=True)
        print(f"\nscratch directory removed: {SCRATCH.name}")


def run() -> None:
    tr = make_trace()

    section("1. What the formats store")
    print(f"samples                  : {tr.stats.npts} x 4 bytes = "
          f"{tr.stats.npts * 4} bytes of raw int32 sample data")
    print(f"MiniSEED  = header + Steim-compressed integer samples")
    print(f"SAC       = 632-byte header + float32 samples (default)")

    section("2. Integer round trip: MiniSEED (int32) and SAC (float32)")
    for name, fmt in (("mseed", "MSEED"), ("sac", "SAC")):
        path = SCRATCH / f"roundtrip.{name}"
        tr.write(str(path), format=fmt)
        size = os.path.getsize(path)
        back = read(str(path))[0]
        identical = np.array_equal(back.data, tr.data)
        print(f"{name.upper():<7} size {size:6d} bytes  "
              f"({size / (tr.stats.npts * 4):.3f} x raw int32)  "
              f"bit-identical={identical}  "
              f"dt={back.stats.delta:g} s  starttime equal="
              f"{back.stats.starttime == tr.stats.starttime}")
        print(f"        dtype after read : {back.data.dtype}")

    section("3. Steim compression is the reason MiniSEED is smaller")
    for amp in (1, 1000, 10 ** 7):
        tr_amp = make_trace()
        tr_amp.data = np.round(tr_amp.data / np.abs(tr_amp.data).max()
                               * amp).astype(np.int32)
        path = SCRATCH / f"steim_{amp}.mseed"
        tr_amp.write(str(path), format="MSEED")
        size = os.path.getsize(path)
        print(f"peak amplitude {amp:>9}: file {size:6d} bytes for "
              f"{tr_amp.stats.npts} samples = "
              f"{size / tr_amp.stats.npts:.4f} bytes/sample "
              f"(uncompressed int32 = 4.0000)")

    section("4. SAC stores float32 -- and that loses precision")
    tr_dbl = make_trace(dtype=np.float64)
    tr_dbl.data = tr_dbl.data * 1e-6 + 1e-12          # small, non-integer values
    path = SCRATCH / "precision.sac"
    tr_dbl.write(str(path), format="SAC")
    back = read(str(path))[0]
    err = np.abs(back.data - tr_dbl.data)
    rel = err / np.abs(tr_dbl.data).max()
    print(f"largest |value| stored   : {np.abs(tr_dbl.data).max():.6e}")
    print(f"max |round-trip error|   : {err.max():.6e}")
    print(f"relative error           : {rel.max():.6e}   "
          f"(float32 machine epsilon = {np.finfo(np.float32).eps:.6e})")
    print(f"CHECK error < 1e-6 max   : {rel.max() < 1e-6}")

    section("5. A gap written as two files is a Stream of two traces")
    first = make_trace(station="ABCD", npts=1000, fs=100.0)
    second = make_trace(station="ABCD", npts=1000, fs=100.0)
    second.stats.starttime = first.stats.endtime + 1.0        # 1 s gap
    second.data = second.data + 100
    p1, p2 = SCRATCH / "seg1.mseed", SCRATCH / "seg2.mseed"
    first.write(str(p1), format="MSEED")
    second.write(str(p2), format="MSEED")
    st = read(str(p1)) + read(str(p2))
    print(f"read two files            : {len(st)} traces")
    gap = st[1].stats.starttime - st[0].stats.endtime
    print(f"gap between segments      : {gap:.3f} s "
          f"({int(round(gap * 100))} missing samples)")
    print(f"merge(method=-1)          : "
          f"{len(st.copy().merge(method=-1))} traces (gap kept)")
    print(f"merge(method=0)           : "
          f"{len(st.copy().merge(method=0))} traces (gap zero-filled)")

    print("\n  The integer/float trap that catches almost everyone:")
    try:
        st.copy().merge(method=0, fill_value=0.0)
        print("    merge(fill_value=0.0) on int32 data succeeded (unexpected)")
    except Exception as exc:
        print(f"    merge(fill_value=0.0) on int32 data -> "
              f"{type(exc).__name__}: {exc}")
    filled = st.copy().merge(method=0, fill_value=0)
    off = np.where(filled[0].data == 0)[0]
    print(f"    merge(fill_value=0)   -> {len(filled)} trace(s), "
          f"{filled[0].stats.npts} samples, fill at indices "
          f"{off.min()}..{off.max()} = {len(off) / 100.0:.3f} s")
    print("    Transfer function: never interpolate into a gap unless the science")
    print("    justifies it. Zero-filled samples are not measurements.")

    section("6. Header fields survive a round trip; units do not")
    tr_full = make_trace()
    tr_full.stats.calib = 5.1e8            # counts per m/s, stored in the header
    path = SCRATCH / "meta.mseed"
    tr_full.write(str(path), format="MSEED")
    back = read(str(path))[0]
    for key in ("network", "station", "location", "channel", "sampling_rate",
                "starttime", "calib"):
        print(f"  {key:<14}: {back.stats[key]}")
    print("  NOTE: the samples are still counts. `calib` is metadata; it does")
    print("  not convert anything until remove_response() or remove_sensitivity()")
    print("  is called, and MiniSEED has no field to store it: we wrote")
    print("  calib=5.1e+08 and read back calib=1.0 above.")

    section("7. Format sniffing: read() decides from the bytes, not the name")
    odd = SCRATCH / "actually_mseed.bin"
    tr.write(str(odd), format="MSEED")
    auto = read(str(odd))[0]
    print(f"file named '.bin', read as : {auto.id} "
          f"npts={auto.stats.npts} dt={auto.stats.delta:g} s")
    print(f"CHECK identical samples    : {np.array_equal(auto.data, tr.data)}")

    section("8. Channel naming encodes sample rate and band (SEED convention)")
    print("  BHZ : broadband, 10-80 Hz sample rate (here 100 Hz), vertical")
    print("  HHZ : high broadband, 80-250 Hz sample rate")
    print("  LHZ : long period, 1 Hz sample rate")
    print(f"  parsed id for our trace  : {tr.id}")
    print(f"  network.station.location.channel = XX.ABCD.00.BHZ")


if __name__ == "__main__":
    main()
